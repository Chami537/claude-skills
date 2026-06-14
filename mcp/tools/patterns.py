"""Bug pattern storage and matching."""

import json
import os

BASE_DIR = os.path.expanduser("~/.claude/projects")


def _path(slug: str) -> str:
    return os.path.join(BASE_DIR, slug, "patterns.json")


def _load(slug: str) -> list:
    p = _path(slug)
    if not os.path.exists(p):
        return []
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(slug: str, patterns: list):
    os.makedirs(os.path.join(BASE_DIR, slug), exist_ok=True)
    with open(_path(slug), "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2, ensure_ascii=False)


def match(slug: str, symptoms: list[str], files: list[str] | None = None) -> list[dict]:
    """Find matching patterns by symptoms and/or files. Returns sorted by confidence."""
    if not symptoms and not files:
        return []
    patterns = _load(slug)
    results = []
    for p in patterns:
        p_symptoms = [s.lower() for s in p.get("symptoms", [])]
        p_files = p.get("files", [])

        # Symptom match: any query symptom substring-matches a stored symptom
        symptom_hit = any(
            any(q.lower() in ps for ps in p_symptoms)
            for q in symptoms
        ) if symptoms else False

        # File match: any query file matches a stored glob (simple substring)
        file_hit = False
        if files and p_files:
            file_hit = any(
                any(ff.replace("*", "") in qf for qf in files)
                for ff in p_files
            )

        if symptom_hit or file_hit:
            confidence = "high" if (symptom_hit and file_hit) else "low"
            results.append({**p, "confidence": confidence})

    # Sort: high first, then by count desc
    results.sort(key=lambda r: (0 if r["confidence"] == "high" else 1, -r.get("count", 0)))
    return results


def append(slug: str, pattern: dict) -> dict:
    """Add or update a pattern. If same id exists, increment count."""
    pid = pattern.get("id", "")
    if not pid or not pid.strip():
        return {"error": "pattern 'id' must not be empty"}
    symptoms = pattern.get("symptoms", [])
    if not symptoms or len(symptoms) == 0:
        return {"error": "pattern 'symptoms' must not be empty"}
    if any(not s or not s.strip() for s in symptoms):
        return {"error": "pattern 'symptoms' must not contain empty entries"}

    patterns = _load(slug)
    existing = None
    for i, p in enumerate(patterns):
        if p.get("id") == pid:
            existing = i
            break

    if existing is not None:
        # Update count, merge new symptoms
        patterns[existing]["count"] = patterns[existing].get("count", 1) + 1
        existing_symptoms = patterns[existing].get("symptoms", [])
        for s in pattern.get("symptoms", []):
            if s not in existing_symptoms:
                existing_symptoms.append(s)
        patterns[existing]["symptoms"] = existing_symptoms
        result = patterns[existing]
    else:
        pattern.setdefault("count", 1)
        patterns.append(pattern)
        result = pattern

    _save(slug, patterns)
    return result


def list_all(slug: str) -> list[dict]:
    """List all patterns for a project, sorted by count desc."""
    patterns = _load(slug)
    patterns.sort(key=lambda p: -p.get("count", 0))
    return patterns
