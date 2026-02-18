# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website and blog for bradjanke.com, built with Hugo static site generator using the LoveIt theme.

## Commands

```bash
make run       # Start Hugo dev server with live reload
make build     # Build site (hugo -D, includes drafts)
```

There are no tests or linters configured.

## Architecture

- **Hugo v0.145.0** static site generator with **LoveIt** theme (Git submodule in `themes/LoveIt/`)
- **config.toml** — all site configuration (theme params, menus, social links, SEO)
- **content/** — Markdown files with TOML frontmatter
  - `content/posts/` — blog posts
  - `content/resume/index.md` — resume page (uses Hugo page bundles)
- **static/** — static assets (images, favicon) served at site root
- **archetypes/default.md** — template for `hugo new` content

## Deployment

GitHub Actions (`.github/workflows/ci.yml`) runs on every push: builds with Hugo and syncs `public/` to AWS S3 (`s3://mtn-bradjanke-com-origin/`). Drafts are included in the build (`-D` flag).

## Content Authoring

New posts: create a `.md` file in `content/posts/` with TOML frontmatter (`+++` delimiters). Key frontmatter fields: `title`, `date`, `draft`, `tags`, `categories`, `description`.
