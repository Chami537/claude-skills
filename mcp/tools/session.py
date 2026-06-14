"""Session state persistence with validation."""

import json
import os
import re
from datetime import datetime, timezone, timedelta

BASE_DIR = os.path.expanduser("~/.claude/projects")
SESSION_TTL = timedelta(hours=24)

VALID_WORKFLOWS = ["dev", "fix", "refactor"]
VALID_PHASES = {
    "dev": ["init", "plan", "build", "verify", "review", "harden", "ship"],
    "fix": ["init", "diagnose", "plan", "baseline", "fixing", "review", "ship"],
    "refactor": ["init", "measure", "plan", "build", "verify", "review", "ship"],
}
VALID_CHECKS = [
    "build_passed", "simplify_done", "blast_radius_done",
    "code_audit_done", "metrics_improved", "grill_me_done",
]

SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

ALLOWED_TRANSITIONS = {
    "dev": {
        "init": ["plan"], "plan": ["plan", "build"], "build": ["build", "verify"],
        "verify": ["verify", "review"], "review": ["review", "harden"],
        "harden": ["harden", "ship"], "ship": ["ship"],
    },
    "fix": {
        "init": ["diagnose"], "diagnose": ["diagnose", "plan"],
        "plan": ["plan", "baseline"], "baseline": ["baseline", "fixing"],
        "fixing": ["fixing", "review"], "review": ["review", "ship"],
        "ship": ["ship"],
    },
    "refactor": {
        "init": ["measure"], "measure": ["measure", "plan"],
        "plan": ["plan", "build"], "build": ["build", "verify"],
        "verify": ["verify", "review"], "review": ["review", "ship"],
        "ship": ["ship"],
    },
}


def _ensure_dir(slug: str) -> str:
    path = os.path.join(BASE_DIR, slug)
    os.makedirs(path, exist_ok=True)
    return path


def _validate_slug(slug: str) -> str | None:
    """Validate slug. Returns error string or None if valid."""
    if not slug or not slug.strip():
        return "slug must not be empty"
    if slug != slug.lower():
        return f"slug '{slug}' must be lowercase"
    if not SLUG_PATTERN.match(slug):
        return f"slug '{slug}' contains invalid characters (a-z, 0-9, -, _ only)"
    return None


def read(slug: str) -> dict:
    """Read session.json for a project slug. Returns {} if not found."""
    err = _validate_slug(slug)
    if err:
        return {"error": err}
    path = os.path.join(BASE_DIR, slug, "session.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Check expiry
    updated = data.get("updated", "")
    if updated:
        try:
            ts = datetime.fromisoformat(updated)
            age = datetime.now(timezone.utc) - ts
            if age > SESSION_TTL:
                return {"_expired": True, "workflow": data.get("workflow"),
                        "phase": data.get("phase"), "checks": data.get("checks", {})}
        except ValueError:
            pass
    # Return essential fields only
    return {
        "workflow": data.get("workflow"),
        "phase": data.get("phase"),
        "checks": data.get("checks", {}),
        "scale": data.get("scale"),
        "branch": data.get("branch"),
        "platform": data.get("platform"),
        "has_tests": data.get("has_tests"),
        "updated": data.get("updated"),
    }


def write(slug: str, workflow: str | None = None, phase: str | None = None,
          checks: dict | None = None, **kwargs) -> dict:
    """Write (merge) session.json. Validates fields. Returns updated data."""
    err = _validate_slug(slug)
    if err:
        return {"error": err}
    _ensure_dir(slug)

    # Read existing
    current = {}
    path = os.path.join(BASE_DIR, slug, "session.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            current = json.load(f)

    # Validate workflow
    if workflow and workflow not in VALID_WORKFLOWS:
        return {"error": f"Invalid workflow '{workflow}'. Must be one of {VALID_WORKFLOWS}"}

    # Validate phase against workflow
    wf = workflow or current.get("workflow")
    if phase and wf and wf in VALID_PHASES:
        if phase not in VALID_PHASES[wf]:
            return {"error": f"Invalid phase '{phase}' for workflow '{wf}'. Must be one of {VALID_PHASES[wf]}"}

    # Validate phase transition (no skipping phases)
    if phase and wf and wf in ALLOWED_TRANSITIONS:
        current_phase = current.get("phase")
        if current_phase:
            allowed = ALLOWED_TRANSITIONS[wf].get(current_phase, [])
            if phase not in allowed:
                return {"error": f"Invalid transition: {current_phase} -> {phase}. Allowed: {allowed}"}

    # Validate checks
    if checks:
        for k in checks:
            if k not in VALID_CHECKS:
                return {"error": f"Invalid check key '{k}'. Must be one of {VALID_CHECKS}"}

    # Merge
    current.update(kwargs)
    if workflow:
        current["workflow"] = workflow
    if phase:
        current["phase"] = phase
    if checks:
        current.setdefault("checks", {})
        current["checks"].update(checks)
    current["updated"] = datetime.now(timezone.utc).isoformat()

    with open(path, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2, ensure_ascii=False)

    return current


def cleanup(slug: str) -> dict:
    """Delete session.json (workflow completed)."""
    err = _validate_slug(slug)
    if err:
        return {"error": err}
    path = os.path.join(BASE_DIR, slug, "session.json")
    if os.path.exists(path):
        os.remove(path)
        return {"deleted": True}
    return {"deleted": False, "reason": "not found"}
