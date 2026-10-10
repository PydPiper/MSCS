# Markdown slides with Sphinx

This repository turns Markdown files into a browser based slide deck using Sphinx, MyST, and Reveal.js.

## Write slides

Edit [`docs/index.md`](docs/index.md). The first heading is the deck title; each `##` heading starts a new slide. Use normal Markdown for text, lists, links, images, and fenced code blocks. Press the **S** key during a presentation to open speaker view and see notes.

Keep each slide as a `##` section in `docs/index.md`; you can split a large deck into additional Markdown files as the project grows.

## Preview locally

```bash
python -m pip install .
sphinx-build -b revealjs docs docs/_build/revealjs
```

Open `docs/_build/revealjs/index.html` in a browser. On Windows PowerShell, use `python -m pip install .` and `python -m sphinx -b revealjs docs docs/_build/revealjs`.

## Publish with GitHub Pages

The workflow in `.github/workflows/pages.yml` builds and deploys the slides whenever you push to `main`. In the repository settings, open **Pages** and set **Build and deployment** to **GitHub Actions**. After the workflow finishes, the published deck URL appears in the Pages settings and in the workflow deployment.

GitHub Pages supports one published site per repository. If you already publish a different site from this repository, choose whether this slide deck should replace it or use a separate repository.
