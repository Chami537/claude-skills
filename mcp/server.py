"""Claude MCP Server — session, patterns, checklist tools for dev workflows."""

from mcp.server.fastmcp import FastMCP
import tools.session as session
import tools.patterns as patterns
import tools.checklist as checklist

mcp = FastMCP("claude-mcp")


# ── Session tools ──────────────────────────────────────────────

@mcp.tool()
def session_read(slug: str) -> dict:
    """读取 session.json。slug 如 hita、qqbot。
    Returns session 或 {}。_expired=true 表示超过 24h。"""
    return session.read(slug)


@mcp.tool()
def session_write(
    slug: str,
    workflow: str | None = None,
    phase: str | None = None,
    checks: dict | None = None,
) -> dict:
    """写入/更新 session.json。只传要更新的字段。
    workflow: dev|fix|refactor。phase 自动校验。checks 部分更新。"""
    return session.write(slug, workflow=workflow, phase=phase, checks=checks)


@mcp.tool()
def session_cleanup(slug: str) -> dict:
    """删除 session.json（工作流完成时调用）。"""
    return session.cleanup(slug)


# ── Patterns tools ─────────────────────────────────────────────

@mcp.tool()
def patterns_match(slug: str, symptoms: list[str], files: list[str] | None = None) -> list[dict]:
    """用症状关键词+文件路径匹配已知 bug pattern。
    返回匹配列表，按置信度(high/low)+出现次数排序。"""
    return patterns.match(slug, symptoms, files)


@mcp.tool()
def patterns_append(slug: str, id: str, pattern: str, symptoms: list[str],
                    files: list[str], root_cause: str, fix: str) -> dict:
    """添加 bug pattern。同 id 已存在则 count+1 合并 symptoms。"""
    return patterns.append(slug, {
        "id": id,
        "pattern": pattern,
        "symptoms": symptoms,
        "files": files,
        "root_cause": root_cause,
        "fix": fix,
    })


@mcp.tool()
def patterns_list(slug: str) -> list[dict]:
    """列出项目所有 pattern，按出现次数降序。"""
    return patterns.list_all(slug)


# ── Checklist tools ────────────────────────────────────────────

@mcp.tool()
def checklist_read(slug: str) -> str:
    """读取项目的验证清单 markdown。"""
    return checklist.read(slug)


@mcp.tool()
def checklist_append(slug: str, module: str, step: str, source: str) -> dict:
    """追加手动验证步骤到 checklist。自动去重。
    module: 页面名。step: 验证描述。source: commit hash 或功能名。"""
    return checklist.append(slug, module, step, source)


# ── Entry ──────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
