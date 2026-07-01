"""Claude MCP Server — session, patterns, checklist + workflow orchestration engine.

All workflow logic lives in tools/workflow.py. SKILL.md files are thin wrappers
that call MCP tools. The agent reads returned steps and executes them.
"""

from mcp.server.fastmcp import FastMCP
import tools.session as session
import tools.patterns as patterns
import tools.checklist as checklist
import tools.workflow as wf

mcp = FastMCP("claude-mcp")


# ── Session tools ──────────────────────────────────────────────

@mcp.tool()
def session_read(slug: str) -> dict:
    """Read session.json for a project slug (e.g. hita, qqbot). Returns {} if not found, _expired=true if >24h."""
    return session.read(slug)


@mcp.tool()
def session_write(slug: str, workflow: str | None = None, phase: str | None = None,
                  checks: dict | None = None, scale: str | None = None,
                  has_tests: bool | None = None, branch: str | None = None,
                  platform: str | None = None) -> dict:
    """Write/merge session.json. Only pass fields you want to update. Phase transitions validated server-side."""
    return session.write(slug, workflow=workflow, phase=phase, checks=checks, scale=scale, has_tests=has_tests, branch=branch, platform=platform)


@mcp.tool()
def session_cleanup(slug: str) -> dict:
    """Delete session.json when a workflow is complete."""
    return session.cleanup(slug)


# ── Patterns tools ─────────────────────────────────────────────

@mcp.tool()
def patterns_match(slug: str, symptoms: list[str], files: list[str] | None = None) -> list[dict]:
    """Match known bug patterns by symptoms + file paths. Returns sorted by confidence (high/low) + occurrence count."""
    return patterns.match(slug, symptoms, files)


@mcp.tool()
def patterns_append(slug: str, id: str, pattern: str, symptoms: list[str],
                    files: list[str], root_cause: str, fix: str) -> dict:
    """Add a bug pattern. Same id -> count+1 and merge symptoms."""
    p = {"id": id, "pattern": pattern, "symptoms": symptoms,
         "files": files, "root_cause": root_cause, "fix": fix}
    return patterns.append(slug, p)


@mcp.tool()
def patterns_list(slug: str) -> list[dict]:
    """List all bug patterns for a project, sorted by count desc."""
    return patterns.list_all(slug)


# ── Checklist tools ────────────────────────────────────────────

@mcp.tool()
def checklist_read(slug: str) -> dict:
    """Read verification checklist for a project."""
    return checklist.read(slug)


@mcp.tool()
def checklist_append(slug: str, module: str = "", step: str = "",
                     source: str = "") -> dict:
    """Append a verification step. Auto-dedup and auto-sort by module."""
    return checklist.append(slug, module=module, step=step, source=source)


# ── Workflow orchestration tools ───────────────────────────────

@mcp.tool()
def workflow_step(slug: str, workflow: str, phase: str, scale: str | None = None,
                  context: dict | None = None) -> dict:
    """THE core tool. Call at the start of ANY workflow phase.
    
    Returns the exact ordered steps the agent MUST execute for this phase.
    All workflow logic (what to do, when, with fallbacks) lives here — not in SKILL.md.
    
    Args:
        slug: project slug (hita, qqbot, etc.)
        workflow: dev | fix | refactor | start | continue | wrap | code-audit
        phase: current phase (plan, build, review, diagnose, measure, etc.)
        scale: for dev — S | M | L
        context: optional dict with task description, has_tests, etc.
    
    Returns: {workflow, phase, scale, steps: [{action, skill/tool, reason, condition, fallback}], total}
    """
    return wf.step(slug, workflow, phase, scale=scale, context=context)


@mcp.tool()
def code_graph_resolve(slug: str, task: str, mode: str = "explore") -> dict:
    """Unified code graph query with built-in fallback chain.
    
    Resolution order (the agent tries each in sequence, advancing on empty result):
    1. graphify-out/GRAPH_REPORT.md (offline full-project graph, zero token)
    2. tokensave_context (online NL code graph)
    3. tokensave_search (symbol name search)
    4. tokensave_dependencies (dependency chain trace)
    5. tokensave_similar (similar code finder)
    6. Agent(Explore) — last resort full scan
    
    Rule: NEVER fall back to manual Read + Grep. Follow the chain.
    """
    return wf.code_graph_resolve(slug, task, mode=mode)


# ── Health & observability ─────────────────────────────────────

@mcp.tool()
def workflow_health(slug: str) -> dict:
    """Check workflow health: how many fallbacks triggered, how many hard rules blocked, dependency status.
    
    Call this at /wrap start and whenever the user asks "anything go wrong?".
    Returns summary of all fallback events and rule blocks for this project.
    """
    return wf.health_report(slug)


@mcp.tool()
def workflow_log_event(slug: str, event_type: str, detail: dict | None = None) -> dict:
    """Log a workflow event: fallback, rule_blocked, or dep_check.
    
    The agent calls this whenever a tool falls back or a hard rule fires.
    This creates an audit trail that workflow_health() surfaces later.
    
    Args:
        slug: project slug
        event_type: "fallback" | "rule_blocked" | "dep_check"
        detail: {"tool": "...", "reason": "...", "next": "..."} for fallbacks,
                {"rule": "...", "detail": "..."} for blocks,
                {"claude_mem": "online"|"offline", "graphify": "exists"|"missing", ...} for deps
    """
    detail = detail or {}
    if event_type == "fallback":
        wf.log_fallback(slug, detail.get("tool", ""), detail.get("reason", ""), detail.get("next", ""))
    elif event_type == "rule_blocked":
        wf.log_rule_block(slug, detail.get("rule", ""), detail.get("detail", ""))
    elif event_type == "dep_check":
        wf.log_dependency_status(slug, detail)
    return {"logged": True, "event": event_type}

if __name__ == "__main__":
    mcp.run()


# ── Auto-save tools ───────────────────────────────────────────

@mcp.tool()
def claude_md_append(slug: str, project_path: str, summary: str) -> dict:
    """Append a dev summary to the project's CLAUDE.md. MCP writes directly to disk — no agent interpretation."""
    import tools.auto_save as au
    return au.claude_md_append(slug, project_path, summary)


@mcp.tool()
def memory_save(slug: str, memory_type: str, name: str, content: str,
                description: str = "") -> dict:
    """Save a memory file. MCP writes directly to disk — no agent interpretation.
    
    Args:
        slug: project slug (hita, qqbot, etc.)
        memory_type: feedback | project | user | reference
        name: filename without .md
        content: markdown body
        description: one-line for the frontmatter
    """
    import tools.auto_save as au
    return au.memory_save(slug, memory_type, name, content, description=description)


# ── Step gating ───────────────────────────────────────────────

@mcp.tool()
def mark_step_done(slug: str, step_index: int, result: dict | None = None) -> dict:
    """Mark a workflow step as completed. Call this after executing each step from workflow_step().
    
    Args:
        slug: project slug
        step_index: 0-based index of the completed step
        result: optional result data from the step
    """
    import tools.workflow as wf
    return wf.mark_step_done(slug, step_index, result=result)
