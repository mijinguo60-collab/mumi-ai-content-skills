#!/usr/bin/env python3
"""Small structural gate for the generated WeChat HTML fragment."""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: validate_gzh_structure.py FILE")

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
errors = []
for token in ("<html", "<head", "<body", "<style", "<script", "<div"):
    if token in text.lower():
        errors.append(f"forbidden tag: {token}")
if not text.lstrip().startswith("<section"):
    errors.append("output must start with <section>")
if "<img" in text and "max-width:100%" not in text.replace(" ", ""):
    errors.append("image must declare max-width:100%")
if "<!-- IMG:" in text and not re.search(r"<!-- IMG:[^>]+ -->", text):
    errors.append("invalid image placeholder")
if errors:
    print("Mumi公众号 HTML: FAIL")
    print("\n".join(f"- {item}" for item in errors))
    raise SystemExit(1)
print("Mumi公众号 HTML: PASS")
