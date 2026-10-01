"""Build a single self-contained HTML file (scripture inlined, standalone-only tags removed).

Usage: python3 tools/build_preview.py OUT.html
"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent / "public"
html = (root / "index.html").read_text()
scripture = (root / "scripture.js").read_text()

html = re.sub(r'<script src="scripture.js" data-standalone></script>',
              lambda _: "<script>\n" + scripture + "\n</script>", html)
html = re.sub(r"<style data-standalone>.*?</style>\n", "", html, flags=re.S)
html = re.sub(r"^.*data-standalone.*\n", "", html, flags=re.M)
html = re.sub(r"^\s*</?(html|head|body)[^>]*>\n|^<!doctype html>\n", "", html, flags=re.M | re.I)
pathlib.Path(sys.argv[1]).write_text(html)
