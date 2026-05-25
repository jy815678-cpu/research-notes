#!/usr/bin/env python3
"""
Markdown to HTML static site generator for research-notes.
Scans src/ for .md files, converts to HTML with unified styling,
and auto-generates index.html.
"""

import os
import sys
import markdown
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SRC_DIR = Path(__file__).parent.parent / "src"
OUT_DIR = Path(__file__).parent.parent / "output"

# Markdown extensions
MD_EXTENSIONS = [
    "toc",
    "tables",
    "fenced_code",
    "extra",
    "codehilite",
    "nl2br",
    "smarty",
    "meta",
]

MD_EXTENSION_CONFIGS = {
    "toc": {"permalink": "", "toc_depth": "2-4", "title": "目录"},
    "codehilite": {"css_class": "highlight", "guess_lang": False, "linenums": False},
}


# ---------------------------------------------------------------------------
# HTML Template
# ---------------------------------------------------------------------------
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{css}</style>
</head>
<body>
<header class="site-header">
  <div class="container nav-bar">
    <a class="site-title" href="{root}index.html">Research Notes</a>
    <nav class="nav-links">
      <a href="{root}index.html">首页</a>
      {nav_links}
    </nav>
    <button id="theme-toggle" aria-label="切换主题">🌙</button>
  </div>
</header>

<main class="container content-wrapper">
  <article class="markdown-body">
    {content}
  </article>
  {toc}
</main>

<footer class="site-footer">
  <div class="container">
    <p>Research Notes &middot; Generated on {date}</p>
  </div>
</footer>

<script>
{js}</script>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Research Notes</title>
<style>
{css}</style>
</head>
<body>
<header class="site-header">
  <div class="container nav-bar">
    <a class="site-title" href="index.html">Research Notes</a>
    <nav class="nav-links">
      <a href="index.html">首页</a>
    </nav>
    <button id="theme-toggle" aria-label="切换主题">🌙</button>
  </div>
</header>

<main class="container index-page">
  <h1>调研报告</h1>
  <p class="lead">知识沉淀与技术调研的集合</p>

  <div class="report-grid">
    {cards}
  </div>
</main>

<footer class="site-footer">
  <div class="container">
    <p>Research Notes &middot; Generated on {date}</p>
  </div>
</footer>

<script>
{js}</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# CSS (embedded)
# ---------------------------------------------------------------------------
CSS = """
/* ========== Variables ========== */
:root {
  --bg: #ffffff;
  --fg: #1f2328;
  --muted: #656d76;
  --border: #d1d9e0;
  --surface: #f6f8fa;
  --accent: #0969da;
  --accent-fg: #ffffff;
  --code-bg: #f5f5f5;
  --toc-bg: #f6f8fa;
  --shadow: 0 1px 3px rgba(31,35,40,0.12);
  --radius: 8px;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  --font-mono: "SF Mono", "Fira Code", "JetBrains Mono", Consolas, monospace;
}

[data-theme="dark"] {
  --bg: #0d1117;
  --fg: #c9d1d9;
  --muted: #8b949e;
  --border: #30363d;
  --surface: #161b22;
  --accent: #58a6ff;
  --accent-fg: #0d1117;
  --code-bg: #161b22;
  --toc-bg: #161b22;
  --shadow: 0 1px 3px rgba(0,0,0,0.3);
}

/* ========== Reset ========== */
*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--fg);
  line-height: 1.75;
  transition: background 0.3s, color 0.3s;
}

/* ========== Layout ========== */
.container {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 24px;
}

.content-wrapper {
  display: flex;
  gap: 40px;
  padding-top: 40px;
  padding-bottom: 80px;
}

@media (max-width: 900px) {
  .content-wrapper { flex-direction: column-reverse; gap: 20px; }
}

/* ========== Header ========== */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  transition: background 0.3s;
}
[data-theme="dark"] .site-header {
  background: rgba(13,17,23,0.85);
}

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
  gap: 16px;
}

.site-title {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--fg);
  text-decoration: none;
  white-space: nowrap;
}

.nav-links {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.nav-links a {
  color: var(--muted);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s;
}
.nav-links a:hover { color: var(--accent); }

#theme-toggle {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 6px 10px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.2s;
}
#theme-toggle:hover { background: var(--border); }

/* ========== Article ========== */
article.markdown-body {
  flex: 1;
  min-width: 0;
}

article h1 { font-size: 2rem; margin-top: 0; border-bottom: 2px solid var(--border); padding-bottom: 12px; }
article h2 { font-size: 1.5rem; margin-top: 2em; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
article h3 { font-size: 1.2rem; margin-top: 1.5em; }
article h4 { font-size: 1.05rem; }
article a { color: var(--accent); text-decoration: none; }
article a:hover { text-decoration: underline; }
article img { max-width: 100%; border-radius: var(--radius); }
article blockquote {
  margin: 1em 0;
  padding: 0.5em 1em;
  border-left: 4px solid var(--accent);
  background: var(--surface);
  border-radius: 0 var(--radius) var(--radius) 0;
}
article blockquote > p:first-child { margin-top: 0; }
article blockquote > p:last-child { margin-bottom: 0; }
article hr { border: none; border-top: 1px solid var(--border); margin: 2em 0; }

/* ========== Table ========== */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.2em 0;
  font-size: 0.92rem;
  box-shadow: var(--shadow);
  border-radius: var(--radius);
  overflow: hidden;
}
th, td { padding: 10px 14px; border: 1px solid var(--border); text-align: left; }
th { background: var(--surface); font-weight: 600; }
tr:nth-child(even) { background: rgba(150,150,150,0.04); }

/* ========== Code ========== */
code {
  font-family: var(--font-mono);
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.88em;
}
pre {
  background: var(--code-bg);
  padding: 16px;
  border-radius: var(--radius);
  overflow-x: auto;
  font-size: 0.88rem;
  line-height: 1.6;
  border: 1px solid var(--border);
}
pre code { padding: 0; background: none; }

/* Pygments / highlight */
.highlight { background: var(--code-bg); border-radius: var(--radius); }
.hll { background-color: rgba(150,150,150,0.1); }
.c, .cm, .c1, .cs { color: #6e7781; font-style: italic; }
.k, .kc, .kd, .kn, .kp, .kr, .kt { color: #cf222e; }
.o, .ow { color: #953800; }
.m, .mb, .mf, .mh, .mi, .mo { color: #0550ae; }
.s, .sa, .sb, .sc, .dl, .sd, .s2, .se, .sh, .si, .sx, .s1 { color: #0a3069; }
.na, .nb, .nc, .nd, .ne, .nf, .nl, .nn, .no, .nt, .nv { color: #8250df; }
[data-theme="dark"] .c, [data-theme="dark"] .cm, [data-theme="dark"] .c1 { color: #8b949e; }
[data-theme="dark"] .k, [data-theme="dark"] .kc, [data-theme="dark"] .kd { color: #ff7b72; }
[data-theme="dark"] .o, [data-theme="dark"] .ow { color: #ffa657; }
[data-theme="dark"] .m, [data-theme="dark"] .mb { color: #79c0ff; }
[data-theme="dark"] .s, [data-theme="dark"] .s2, [data-theme="dark"] .s1 { color: #a5d6ff; }
[data-theme="dark"] .na, [data-theme="dark"] .nb { color: #d2a8ff; }

/* ========== TOC ========== */
.toc-sidebar {
  width: 240px;
  flex-shrink: 0;
  position: sticky;
  top: 76px;
  align-self: flex-start;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
}
.toc-sidebar h3 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  margin: 0 0 12px;
}
.toc-sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 0.88rem;
}
.toc-sidebar li { margin: 6px 0; }
.toc-sidebar a {
  color: var(--muted);
  text-decoration: none;
  display: block;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s;
}
.toc-sidebar a:hover { color: var(--accent); background: var(--surface); }
.toc-sidebar ul ul { padding-left: 12px; }

@media (max-width: 900px) {
  .toc-sidebar { width: 100%; position: static; max-height: none; margin-bottom: 20px; }
}

/* ========== Index Page ========== */
.index-page { padding-top: 60px; padding-bottom: 80px; }
.index-page h1 { font-size: 2.2rem; margin-bottom: 8px; }
.lead { color: var(--muted); font-size: 1.15rem; margin-bottom: 40px; }

.report-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}

.report-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  transition: transform 0.2s, box-shadow 0.2s;
  text-decoration: none;
  color: inherit;
  display: block;
}
.report-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow);
  border-color: var(--accent);
}
.report-card h3 {
  margin: 0 0 8px;
  font-size: 1.15rem;
  color: var(--accent);
}
.report-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.6;
}
.report-card .meta {
  margin-top: 16px;
  font-size: 0.82rem;
  color: var(--muted);
}

/* ========== Footer ========== */
.site-footer {
  border-top: 1px solid var(--border);
  padding: 24px 0;
  text-align: center;
  color: var(--muted);
  font-size: 0.85rem;
}
"""


# ---------------------------------------------------------------------------
# JS (embedded)
# ---------------------------------------------------------------------------
JS = """
(function() {
  // Theme toggle
  const btn = document.getElementById('theme-toggle');
  const html = document.documentElement;
  const saved = localStorage.getItem('theme');
  if (saved) html.setAttribute('data-theme', saved);
  function updateIcon() {
    btn.textContent = html.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
  }
  updateIcon();
  btn.addEventListener('click', () => {
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateIcon();
  });

  // TOC active highlight on scroll
  const toc = document.querySelector('.toc-sidebar');
  if (toc) {
    const links = toc.querySelectorAll('a[href^="#"]');
    const headings = Array.from(document.querySelectorAll('article [id]'));
    if (headings.length && links.length) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            links.forEach(l => l.style.color = '');
            const link = toc.querySelector('a[href="#' + entry.target.id + '"]');
            if (link) link.style.color = 'var(--accent)';
          }
        });
      }, { rootMargin: '-80px 0px -60% 0px' });
      headings.forEach(h => observer.observe(h));
    }
  }
})();
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def md_to_html(md_path: Path) -> tuple[str, str, str]:
    """Convert a Markdown file to HTML. Returns (title, toc_html, body_html)."""
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_EXTENSION_CONFIGS)
    text = md_path.read_text(encoding="utf-8")
    body = md.convert(text)
    toc = md.toc if hasattr(md, "toc") else ""

    # Extract title from first H1 or filename
    title = md_path.stem.replace("-", " ").replace("_", " ").title()
    for line in text.splitlines():
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            break
    return title, toc, body


def make_nav_links(pages: list[tuple[str, str]], current: str) -> str:
    """Generate nav links HTML."""
    links = []
    for label, href in pages:
        if href == current:
            continue
        links.append(f'<a href="{href}">{label}</a>')
    return "\n".join(links)


def make_card(title: str, desc: str, href: str, date_str: str = "") -> str:
    meta = f'<div class="meta">{date_str}</div>' if date_str else ""
    return f"""
<a class="report-card" href="{href}">
  <h3>{title}</h3>
  <p>{desc}</p>
  {meta}
</a>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Find all .md files
    md_files = sorted(SRC_DIR.rglob("*.md"))
    if not md_files:
        print("No Markdown files found in src/")
        sys.exit(1)

    pages: list[tuple[str, str]] = []  # (label, href)
    generated: list[dict] = []

    for md_path in md_files:
        rel = md_path.relative_to(SRC_DIR)
        out_path = OUT_DIR / rel.with_suffix(".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        title, toc, body = md_to_html(md_path)
        depth = len(rel.parent.parts)
        root = "../" * depth if depth > 0 else "./"

        # Build TOC sidebar if present
        toc_html = ""
        if toc:
            toc_html = f'<aside class="toc-sidebar">{toc}</aside>'

        # Build page-relative nav links
        page_nav = []
        for _, href in pages:
            # href is relative to output root, convert to page-relative
            if href.startswith("./"):
                page_href = root + href[2:]
            else:
                page_href = root + href.lstrip("/")
            # Extract label from previous generation
            page_nav.append(("Report", page_href))  # simplified

        # Re-build nav with current pages
        nav_html = make_nav_links(pages, "")  # show all pages in nav

        html = HTML_TEMPLATE.format(
            title=title,
            css=CSS,
            js=JS,
            content=body,
            toc=toc_html,
            root=root,
            nav_links=nav_html,
            date=datetime.now().strftime("%Y-%m-%d"),
        )
        out_path.write_text(html, encoding="utf-8")

        href = "./" + str(rel.with_suffix(".html"))
        pages.append((title, href))
        generated.append({
            "title": title,
            "path": out_path,
            "href": href,
            "rel": rel,
        })
        print(f"  ✓ {rel} → {out_path.relative_to(OUT_DIR.parent)}")

    # Generate index.html
    cards = []
    for info in generated:
        rel = info["rel"]
        # description: first paragraph after H1
        md_text = (SRC_DIR / rel).read_text(encoding="utf-8")
        desc = "调研报告"
        lines = md_text.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("# ") and i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith("#") and not next_line.startswith(">"):
                    desc = next_line[:140]
                    if len(next_line) > 140:
                        desc += "..."
                    break
                elif next_line.startswith(">"):
                    desc = next_line.lstrip("> ").strip()[:140]
                    break
        cards.append(make_card(info["title"], desc, info["href"]))

    index_html = INDEX_TEMPLATE.format(
        css=CSS,
        js=JS,
        cards="\n".join(cards),
        date=datetime.now().strftime("%Y-%m-%d"),
    )
    index_path = OUT_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  ✓ index.html → {index_path.relative_to(OUT_DIR.parent)}")

    print(f"\nDone. Output in: {OUT_DIR}")


if __name__ == "__main__":
    main()
