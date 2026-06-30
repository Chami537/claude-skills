import json, os, time

LOG_FILE = os.path.expanduser("~/.claude/projects/.workflow_events.jsonl")

def _log_event(slug, event_type, detail):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    entry = {"ts": time.time(), "slug": slug, "event": event_type, "detail": detail}
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def log_fallback(slug, tool, reason, next_tool):
    _log_event(slug, "fallback", {"tool": tool, "reason": reason, "next": next_tool})

def log_rule_block(slug, rule, detail):
    _log_event(slug, "rule_blocked", {"rule": rule, "detail": detail})

def log_dependency_status(slug, deps):
    _log_event(slug, "dep_check", deps)

def health_report(slug):
    if not os.path.exists(LOG_FILE):
        return {"status": "no events recorded", "fallbacks": 0, "blocks": 0, "events": []}
    events = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                e = json.loads(line)
                if e.get("slug") == slug or e.get("slug") == "global":
                    events.append(e)
            except:
                pass
    fallbacks = [e for e in events if e["event"] == "fallback"]
    blocks = [e for e in events if e["event"] == "rule_blocked"]
    deps = [e for e in events if e["event"] == "dep_check"]
    return {
        "slug": slug,
        "total_events": len(events),
        "fallbacks": len(fallbacks),
        "blocks": len(blocks),
        "recent_fallbacks": [f["detail"] for f in fallbacks[-5:]],
        "recent_blocks": [b["detail"] for b in blocks[-5:]],
        "last_dep_check": deps[-1]["detail"] if deps else None,
    }
print("logging module added")
