"""Manual verification checklist management."""

import os

BASE_DIR = os.path.expanduser("~/.claude/projects")


def _path(slug: str) -> str:
    return os.path.join(BASE_DIR, slug, "checklist.md")


def read(slug: str) -> str:
    """Read checklist. Returns empty string if not found."""
    p = _path(slug)
    if not os.path.exists(p):
        return ""
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def append(slug: str, module: str, step: str, source: str) -> dict:
    """Append a verification step to a module section. Deduplicates."""
    if not module or not module.strip():
        return {"error": "module must not be empty"}
    if not step or not step.strip():
        return {"error": "step must not be empty"}
    if not source or not source.strip():
        return {"error": "source must not be empty"}
    os.makedirs(os.path.join(BASE_DIR, slug), exist_ok=True)
    p = _path(slug)

    # Read existing
    content = ""
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()

    # Build header if new file
    if not content:
        content = f"## <{slug}> 手动验证清单\n\n"

    # Normalize step for dedup
    step_line = f"- [ ] {step} — 来自 {source}"
    step_text = step.strip().lower()

    # Check if step already exists (dedup)
    if step_text in content.lower():
        return {"appended": False, "reason": "duplicate"}

    # Find or create module section
    module_header = f"### {module}"
    if module_header in content:
        # Append after module header, before next ###
        lines = content.split("\n")
        insert_idx = None
        in_section = False
        for i, line in enumerate(lines):
            if line.strip() == module_header:
                in_section = True
                continue
            if in_section and line.startswith("### "):
                insert_idx = i
                break
        if insert_idx is None:
            # End of file
            lines.append(step_line)
        else:
            lines.insert(insert_idx, step_line)
        content = "\n".join(lines)
    else:
        # New module section at end
        content += f"\n{module_header}\n{step_line}\n"

    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

    return {"appended": True, "module": module, "step": step}
