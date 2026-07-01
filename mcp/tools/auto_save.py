"""Auto-save tools: write CLAUDE.md and memory files directly via MCP."""

import os
from datetime import datetime


def claude_md_append(slug: str, project_path: str, summary: str) -> dict:
    """Append a development summary to the project's CLAUDE.md."""
    path = os.path.join(project_path, "CLAUDE.md")
    if not os.path.exists(path):
        return {"error": f"CLAUDE.md not found at {path}"}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n\n## {timestamp}\n{summary}\n"

    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)

    return {"ok": True, "path": path, "appended": len(entry), "timestamp": timestamp}


def memory_save(slug: str, memory_type: str, name: str, content: str,
                description: str = "") -> dict:
    """Save a memory file to ~/.claude/projects/C--Users-Rinat/memory/.

    Args:
        slug: project slug
        memory_type: "feedback" | "project" | "user" | "reference"
        name: filename without .md (e.g. "abstraction-cost")
        content: markdown body
        description: one-line description for the frontmatter
    """
    base = os.path.expanduser("~/.claude/projects/C--Users-Rinat/memory")
    os.makedirs(base, exist_ok=True)

    filename = f"{memory_type}_{name}.md"
    path = os.path.join(base, filename)

    # Build frontmatter
    if not description:
        description = f"{memory_type}: {name}"

    entry = f"""---
name: {name}
description: {description}
type: {memory_type}
---

{content}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)

    # Update MEMORY.md index
    index_path = os.path.join(base, "MEMORY.md")
    index_line = f"- [{name}]({filename}) — {description[:100]}"
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
        if filename not in index_content:
            with open(index_path, "a", encoding="utf-8") as f:
                f.write(f"\n{index_line}")
    else:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"# Memory Index\n\n{index_line}\n")

    return {"ok": True, "path": path, "filename": filename, "memory_type": memory_type}
