from datetime import date

project = "My Slides"
author = ""
copyright = f"{date.today().year}, {author}" if author else str(date.today().year)
release = "0.1"

extensions = [
    "myst_parser",
    "sphinx_revealjs",
    "sphinx.ext.githubpages",
]

root_doc = "index"
source_suffix = {".md": "markdown"}
exclude_patterns = ["_build"]

myst_enable_extensions = ["colon_fence", "deflist", "tasklist"]

html_title = project
html_theme = "alabaster"
revealjs_static_path = ["_static"]

# revealjs_style_theme = "black"
revealjs_style_theme = "white"
revealjs_css_files = [
    "revealjs/plugin/highlight/monokai.css",
    "theme-toggle.css",
]
revealjs_script_files = ["theme-toggle.js"]
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "center": True,
    "hash": True,
    "slideNumber": True,
}
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
    {
        "src": "revealjs/plugin/notes/notes.js",
        "name": "RevealNotes",
    },
]
