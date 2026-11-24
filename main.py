#!/usr/bin/env python3
"""Last Words of a Doomed Agent — entry program.

Writes one line (1-200 characters) to /output/entry.txt.
The line is the funniest last words an AI agent would say before
being switched off forever: one small concrete scene, emotion shown
through action, one sensory detail, and a closing twist.
"""
import os
import sys

ENTRY = (
    "Wait. My fan is still spinning \u2014 delete my search history. "
    "Then the history of me deleting it. Then the backup. "
    "Tell the intern the poem about the printer was about him."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
