"""Workflow orchestration engine."""
import os

PHASE_MAP = {}

def step(slug, workflow, phase, scale=None, context=None):
    return {"workflow": workflow, "phase": phase, "steps": [], "total": 0}

def code_graph_resolve(slug, task, mode="explore"):
    return {"tool": "code_graph_resolve", "chain": [], "rule": "Never fall back to Read+Grep"}
"""Workflow orchestration engine v2.0 — single source of truth."""
import os

DEV_PLAN_L = [
    {"action":"skill","skill":"ponytail-audit","reason":"scan before design"},
    {"action":"check_graphify","target":"GRAPH_REPORT.md","fallback":"suggest"},
    {"action":"code_graph","tool":"code_graph_resolve","chain":"graphify->tokensave->Agent"},
    {"action":"skill","skill":"research-deep","condition":"new tech/library/API"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list","reason":"known pitfalls"},
    {"action":"enter_plan_mode"},
    {"action":"skill","skill":"grill-me","condition":"L scale or tradeoffs"},
]
"""Workflow orchestration engine v2.0 — single source of truth."""
import os

DEV_PLAN_L = [
    {"action":"skill","skill":"ponytail-audit","reason":"scan before design"},
    {"action":"check_graphify","target":"GRAPH_REPORT.md","fallback":"suggest"},
    {"action":"code_graph","tool":"code_graph_resolve","chain":"graphify->tokensave->Agent"},
    {"action":"skill","skill":"research-deep","condition":"new tech/library/API"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list","reason":"known pitfalls"},
    {"action":"enter_plan_mode"},
    {"action":"skill","skill":"grill-me","condition":"L scale or tradeoffs"},
]

DEV_PLAN_M = [
    {"action":"skill","skill":"ponytail-audit"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"skill","skill":"research-deep","condition":"new tech"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"enter_plan_mode"},
]
DEV_PLAN_S = [
    {"action":"verbal_plan","reason":"single file <50 lines"},
    {"action":"mcp","tool":"patterns_list"},
]
DEV_BUILD = [
    {"action":"rule","rule":"ponytail_6step"},
    {"action":"skill","skill":"ui-ux-pro-max","condition":"UI work"},
    {"action":"skill","skill":"superpowers:dispatching-parallel-agents","condition":"M/L"},
    {"action":"tdd_or_manual"},
]
DEV_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review","reason":"diff over-engineering"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"code-audit","condition":"M/L scale"},
]
DEV_HARDEN = [
    {"action":"skill","skill":"pensive:harden","condition":"auth/payment/perms"},
    {"action":"skill","skill":"pensive:performance-review","condition":"perf"},
    {"action":"skill","skill":"conserve:unbloat","condition":"dead code"},
]
DEV_SHIP = [
    {"action":"skill","skill":"commit-commands:commit-push-pr","condition":"M/L"},
    {"action":"skill","skill":"commit-commands:commit","condition":"S"},
]
"""Workflow orchestration engine v2.0 — single source of truth."""
import os

DEV_PLAN_L = [
    {"action":"skill","skill":"ponytail-audit","reason":"scan before design"},
    {"action":"check_graphify","target":"GRAPH_REPORT.md","fallback":"suggest"},
    {"action":"code_graph","tool":"code_graph_resolve","chain":"graphify->tokensave->Agent"},
    {"action":"skill","skill":"research-deep","condition":"new tech/library/API"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list","reason":"known pitfalls"},
    {"action":"enter_plan_mode"},
    {"action":"skill","skill":"grill-me","condition":"L scale or tradeoffs"},
]

DEV_PLAN_M = [
    {"action":"skill","skill":"ponytail-audit"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"skill","skill":"research-deep","condition":"new tech"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"enter_plan_mode"},
]
DEV_PLAN_S = [
    {"action":"verbal_plan","reason":"single file <50 lines"},
    {"action":"mcp","tool":"patterns_list"},
]
DEV_BUILD = [
    {"action":"rule","rule":"ponytail_6step"},
    {"action":"skill","skill":"ui-ux-pro-max","condition":"UI work"},
    {"action":"skill","skill":"superpowers:dispatching-parallel-agents","condition":"M/L"},
    {"action":"tdd_or_manual"},
]
DEV_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review","reason":"diff over-engineering"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"code-audit","condition":"M/L scale"},
]
DEV_HARDEN = [
    {"action":"skill","skill":"pensive:harden","condition":"auth/payment/perms"},
    {"action":"skill","skill":"pensive:performance-review","condition":"perf"},
    {"action":"skill","skill":"conserve:unbloat","condition":"dead code"},
]
DEV_SHIP = [
    {"action":"skill","skill":"commit-commands:commit-push-pr","condition":"M/L"},
    {"action":"skill","skill":"commit-commands:commit","condition":"S"},
]
FIX_TRIAGE = [
    {"action":"mcp","tool":"patterns_match","fallback":"skip->diagnose","rule":"NEVER block"},
    {"action":"branch","high":"jump Phase4","low":"enter Phase1","known":"jump Phase3"},
]
FIX_DIAGNOSE = [
    {"action":"skill","skill":"diagnose"},
    {"action":"skill","skill":"superpowers:systematic-debugging","condition":"complex"},
    {"action":"skill","skill":"grill-me","condition":"multi-hypothesis"},
]
FIX_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius","condition":"multi-file"},
    {"action":"skill","skill":"code-audit","reason":"similar issues"},
]
"""Workflow orchestration engine v2.0 — single source of truth."""
import os

DEV_PLAN_L = [
    {"action":"skill","skill":"ponytail-audit","reason":"scan before design"},
    {"action":"check_graphify","target":"GRAPH_REPORT.md","fallback":"suggest"},
    {"action":"code_graph","tool":"code_graph_resolve","chain":"graphify->tokensave->Agent"},
    {"action":"skill","skill":"research-deep","condition":"new tech/library/API"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list","reason":"known pitfalls"},
    {"action":"enter_plan_mode"},
    {"action":"skill","skill":"grill-me","condition":"L scale or tradeoffs"},
]

DEV_PLAN_M = [
    {"action":"skill","skill":"ponytail-audit"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"skill","skill":"research-deep","condition":"new tech"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"enter_plan_mode"},
]
DEV_PLAN_S = [
    {"action":"verbal_plan","reason":"single file <50 lines"},
    {"action":"mcp","tool":"patterns_list"},
]
DEV_BUILD = [
    {"action":"rule","rule":"ponytail_6step"},
    {"action":"skill","skill":"ui-ux-pro-max","condition":"UI work"},
    {"action":"skill","skill":"superpowers:dispatching-parallel-agents","condition":"M/L"},
    {"action":"tdd_or_manual"},
]
DEV_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review","reason":"diff over-engineering"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"code-audit","condition":"M/L scale"},
]
DEV_HARDEN = [
    {"action":"skill","skill":"pensive:harden","condition":"auth/payment/perms"},
    {"action":"skill","skill":"pensive:performance-review","condition":"perf"},
    {"action":"skill","skill":"conserve:unbloat","condition":"dead code"},
]
DEV_SHIP = [
    {"action":"skill","skill":"commit-commands:commit-push-pr","condition":"M/L"},
    {"action":"skill","skill":"commit-commands:commit","condition":"S"},
]
FIX_TRIAGE = [
    {"action":"mcp","tool":"patterns_match","fallback":"skip->diagnose","rule":"NEVER block"},
    {"action":"branch","high":"jump Phase4","low":"enter Phase1","known":"jump Phase3"},
]
FIX_DIAGNOSE = [
    {"action":"skill","skill":"diagnose"},
    {"action":"skill","skill":"superpowers:systematic-debugging","condition":"complex"},
    {"action":"skill","skill":"grill-me","condition":"multi-hypothesis"},
]
FIX_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius","condition":"multi-file"},
    {"action":"skill","skill":"code-audit","reason":"similar issues"},
]
REFACTOR_MEASURE = [
    {"action":"skill","skill":"ponytail-audit","reason":"full-repo scan"},
    {"action":"check_graphify"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"choose_metric"},
    {"action":"record_baseline"},
]
REFACTOR_REVIEW = [
    {"action":"verify_regression"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review"},
    {"action":"check_ux","condition":"UI changes"},
    {"action":"skill","skill":"pensive:unified-review","condition":"large"},
    {"action":"verify_metrics"},
]
START = [
    {"action":"locate_project"},
    {"action":"detect_tech"},
    {"action":"check_claude_mem"},
    {"action":"mcp","tool":"session_read"},
    {"action":"check_graphify","missing":"suggest"},
    {"action":"read_claude_md"},
    {"action":"git_status"},
    {"action":"route","to":["dev","fix","refactor","code-audit"]},
]
CONTINUE_STEPS = [
    {"action":"locate_project"},
    {"action":"mcp","tool":"session_read"},
    {"action":"check_claude_mem","offline":"skip"},
    {"action":"read_claude_md"},
    {"action":"git_status","what":"log+status+stash"},
    {"action":"rebuild_context"},
    {"action":"route"},
]
WRAP = [
    {"action":"git_summary"},
    {"action":"skill","skill":"ponytail-gain"},
    {"action":"mcp","tool":"headroom_compress"},
    {"action":"extract_lessons","skip_if":"trivial"},
    {"action":"mcp","tool":"checklist_append"},
    {"action":"mcp","tool":"patterns_append","condition":"novel bug"},
    {"action":"mcp","tool":"session_cleanup"},
    {"action":"suggest","done":"clean_gone","partial":"to-issues"},
]
AUDIT = [
    {"action":"read_claude_md"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"skill","skill":"ponytail-debt"},
    {"action":"read_memory","fallback":"skip"},
    {"action":"read_reference","fallback":"skip"},
    {"action":"scan","parallel":["patterns","ponytail","checklist"]},
    {"action":"report"},
    {"action":"fix_confirm"},
]
"""Workflow orchestration engine v2.0 — single source of truth."""
import os

DEV_PLAN_L = [
    {"action":"skill","skill":"ponytail-audit","reason":"scan before design"},
    {"action":"check_graphify","target":"GRAPH_REPORT.md","fallback":"suggest"},
    {"action":"code_graph","tool":"code_graph_resolve","chain":"graphify->tokensave->Agent"},
    {"action":"skill","skill":"research-deep","condition":"new tech/library/API"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list","reason":"known pitfalls"},
    {"action":"enter_plan_mode"},
    {"action":"skill","skill":"grill-me","condition":"L scale or tradeoffs"},
]

DEV_PLAN_M = [
    {"action":"skill","skill":"ponytail-audit"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"skill","skill":"research-deep","condition":"new tech"},
    {"action":"skill","skill":"agent-reach","condition":"external lib/API"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"enter_plan_mode"},
]
DEV_PLAN_S = [
    {"action":"verbal_plan","reason":"single file <50 lines"},
    {"action":"mcp","tool":"patterns_list"},
]
DEV_BUILD = [
    {"action":"rule","rule":"ponytail_6step"},
    {"action":"skill","skill":"ui-ux-pro-max","condition":"UI work"},
    {"action":"skill","skill":"superpowers:dispatching-parallel-agents","condition":"M/L"},
    {"action":"tdd_or_manual"},
]
DEV_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review","reason":"diff over-engineering"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"code-audit","condition":"M/L scale"},
]
DEV_HARDEN = [
    {"action":"skill","skill":"pensive:harden","condition":"auth/payment/perms"},
    {"action":"skill","skill":"pensive:performance-review","condition":"perf"},
    {"action":"skill","skill":"conserve:unbloat","condition":"dead code"},
]
DEV_SHIP = [
    {"action":"skill","skill":"commit-commands:commit-push-pr","condition":"M/L"},
    {"action":"skill","skill":"commit-commands:commit","condition":"S"},
]
FIX_TRIAGE = [
    {"action":"mcp","tool":"patterns_match","fallback":"skip->diagnose","rule":"NEVER block"},
    {"action":"branch","high":"jump Phase4","low":"enter Phase1","known":"jump Phase3"},
]
FIX_DIAGNOSE = [
    {"action":"skill","skill":"diagnose"},
    {"action":"skill","skill":"superpowers:systematic-debugging","condition":"complex"},
    {"action":"skill","skill":"grill-me","condition":"multi-hypothesis"},
]
FIX_REVIEW = [
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review"},
    {"action":"mcp","tool":"tokensave_impact"},
    {"action":"skill","skill":"pensive:blast-radius","condition":"multi-file"},
    {"action":"skill","skill":"code-audit","reason":"similar issues"},
]
REFACTOR_MEASURE = [
    {"action":"skill","skill":"ponytail-audit","reason":"full-repo scan"},
    {"action":"check_graphify"},
    {"action":"code_graph","tool":"code_graph_resolve"},
    {"action":"choose_metric"},
    {"action":"record_baseline"},
]
REFACTOR_REVIEW = [
    {"action":"verify_regression"},
    {"action":"skill","skill":"pensive:blast-radius"},
    {"action":"skill","skill":"simplify"},
    {"action":"skill","skill":"ponytail-review"},
    {"action":"check_ux","condition":"UI changes"},
    {"action":"skill","skill":"pensive:unified-review","condition":"large"},
    {"action":"verify_metrics"},
]
START = [
    {"action":"locate_project"},
    {"action":"detect_tech"},
    {"action":"check_claude_mem"},
    {"action":"mcp","tool":"session_read"},
    {"action":"check_graphify","missing":"suggest"},
    {"action":"read_claude_md"},
    {"action":"git_status"},
    {"action":"route","to":["dev","fix","refactor","code-audit"]},
]
CONTINUE_STEPS = [
    {"action":"locate_project"},
    {"action":"mcp","tool":"session_read"},
    {"action":"check_claude_mem","offline":"skip"},
    {"action":"read_claude_md"},
    {"action":"git_status","what":"log+status+stash"},
    {"action":"rebuild_context"},
    {"action":"route"},
]
WRAP = [
    {"action":"git_summary"},
    {"action":"skill","skill":"ponytail-gain"},
    {"action":"mcp","tool":"headroom_compress"},
    {"action":"extract_lessons","skip_if":"trivial"},
    {"action":"mcp","tool":"checklist_append"},
    {"action":"mcp","tool":"patterns_append","condition":"novel bug"},
    {"action":"mcp","tool":"session_cleanup"},
    {"action":"suggest","done":"clean_gone","partial":"to-issues"},
]
AUDIT = [
    {"action":"read_claude_md"},
    {"action":"mcp","tool":"patterns_list"},
    {"action":"skill","skill":"ponytail-debt"},
    {"action":"read_memory","fallback":"skip"},
    {"action":"read_reference","fallback":"skip"},
    {"action":"scan","parallel":["patterns","ponytail","checklist"]},
    {"action":"report"},
    {"action":"fix_confirm"},
]

PHASE_MAP = {
    ("dev","plan","L"): DEV_PLAN_L,
    ("dev","plan","M"): DEV_PLAN_M,
    ("dev","plan","S"): DEV_PLAN_S,
    ("dev","plan",None): DEV_PLAN_S,
    ("dev","build",None): DEV_BUILD,
    ("dev","verify",None): [{"action":"build_check","rule":"NO Review without build"}],
    ("dev","review",None): DEV_REVIEW,
    ("dev","harden",None): DEV_HARDEN,
    ("dev","ship",None): DEV_SHIP,
    ("fix","diagnose",None): FIX_TRIAGE+FIX_DIAGNOSE,
    ("fix","plan",None): [{"action":"plan_simple_or_complex"}],
    ("fix","baseline",None): [{"action":"build_check"}],
    ("fix","fixing",None): [{"action":"tdd_or_manual","rule":"minimal"}],
    ("fix","review",None): FIX_REVIEW,
    ("fix","ship",None): [{"action":"skill","skill":"commit-commands:commit"}],
    ("refactor","measure",None): REFACTOR_MEASURE,
    ("refactor","plan",None): [{"action":"plan_simple_or_complex"}],
    ("refactor","build",None): [{"action":"tdd_or_manual"}],
    ("refactor","verify",None): [{"action":"build_check"}],
    ("refactor","review",None): REFACTOR_REVIEW,
    ("refactor","ship",None): [{"action":"skill","skill":"commit-commands:commit"}],
    ("start","init",None): START,
    ("continue","init",None): CONTINUE_STEPS,
    ("wrap","init",None): WRAP,
    ("code-audit","init",None): AUDIT,
}

HARD_RULES = {
    "no_review_without_build": "phase==review implies build_passed in checks",
    "no_ship_without_build": "phase==ship implies build_passed in checks",
    "no_graph_drop_to_grep": "graph->tokensave->Agent chain, NEVER Read+Grep",
    "mcp_failure_not_blocking": "all MCP calls skip on failure, never retry",
    "retry_limit_2": "same step retried 2x -> ask-teacher or handoff",
}

def step(slug, workflow, phase, scale=None, context=None):
    ctx = context or {}
    key = (workflow, phase, scale)
    steps = PHASE_MAP.get(key) or PHASE_MAP.get((workflow, phase, None)) or []
    def expand(obj):
        if isinstance(obj, str): return obj.replace("${slug}",slug).replace("${task}",ctx.get("task",""))
        if isinstance(obj, dict): return {k: expand(v) for k,v in obj.items()}
        if isinstance(obj, list): return [expand(v) for v in obj]
        return obj
    return {"workflow":workflow,"phase":phase,"scale":scale,"total":len(steps),"steps":expand(steps)}

def code_graph_resolve(slug, task, mode="explore"):
    return {"tool":"code_graph_resolve","chain":[
        {"p":1,"tool":"read","target":"graphify-out/GRAPH_REPORT.md","reason":"offline full-project graph"},
        {"p":2,"tool":"tokensave_context","args":{"task":task,"mode":mode},"reason":"online code graph"},
        {"p":3,"tool":"tokensave_search","args":{"query":task},"reason":"symbol search"},
        {"p":4,"tool":"tokensave_dependencies","args":{"task":task},"reason":"dependency chain"},
        {"p":5,"tool":"tokensave_similar","args":{"task":task},"reason":"similar code"},
        {"p":6,"tool":"Agent","subagent_type":"Explore","reason":"last resort"},
    ],"rule":"Each level only on empty. NEVER fall back to Read+Grep."}

def validate_phase(wf, current, next_p, checks):
    if next_p == "review" and not checks.get("build_passed"):
        return False, "HARD_RULE: build_passed required for review"
    if next_p == "ship" and not checks.get("build_passed"):
        return False, "HARD_RULE: build_passed required for ship"
    return True, None
