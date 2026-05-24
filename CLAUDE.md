# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development

```bash
# Install Hugo (extended version, ≥0.146.0, currently v0.161.1)
# Development server with draft content
hugo server -D

# Production build (also done in CI)
hugo --gc --minify
```

Hugo modules (the Hextra theme) are managed via Go modules. Run `hugo mod get -u github.com/imfing/hextra && hugo mod tidy` to update the theme.

## Architecture

This is a **Hugo static site** using the [Hextra](https://github.com/imfing/hextra) theme (v0.12.3). The site is deployed to Tencent Cloud Object Storage via GitHub Actions on push to `master`.

Hextra's Tailwind classes use the `hx:` prefix (e.g. `hx:flex`, `hx:text-center`). Custom CSS lives in `assets/css/custom.css` — Hextra auto-loads this file. Override CSS custom properties (`--primary-hue`, `--primary-saturation`, `--primary-lightness`) to change the color scheme.

**IMPORTANT CSS selector note**: When writing CSS selectors that target Hextra's `hx:` prefixed utility classes, the colon must be escaped: `.hx\:mb-10`, `.hx\:mt-4`, `.hx\:flex`, etc. Unescaped colons will be parsed as pseudo-classes.

**Multilingual setup**: Two languages — `zh-cn` (default) and `en`. Content files with `.en.md` suffix serve the English version; plain `.md` serves Chinese. Custom `i18n/zh-cn.yaml` provides Chinese translations for menu labels and UI strings.

**Content sections** (each under `content/`):
- `blog/` — blog articles with date-sorted listing, displayed with tags
- `docs/` — "hot trends" / tech documentation
- `training/` — programming development tutorials, organized in subdirectories by topic
- `github/` — auto-generated GitHub trending posts (~494 files), displayed **without** tags
- `about/` — personal about page

**Custom layouts** (`layouts/`): The `github/` and `training/` sections have custom list and single layouts; `training` includes sidebar + TOC, `github` omits sidebar and tags. Every other section uses the Hextra theme defaults.

**Custom partials** (`layouts/partials/custom/`):
- `head-end.html` — loads quicklink for prefetching
- `footer.html` — Chinese ICP/beian registration links (required by law for sites hosted in China)

**Home page** (`content/_index.md` and `_index.en.md`): Uses `layout: hextra-home` with hero section, stats row, and two rows of feature cards. Custom CSS classes:
- `.home-hero` — wraps hero badge, headline, subtitle, buttons for fade-in animation
- `.home-stats` / `.home-stat-item` / `.home-stat-number` / `.home-stat-label` — stats counter row
- `.hextra-feature-card` — hover lift animation (theme class, styled in custom.css)

**Key config highlights** (`hugo.yaml`):
- CJK language enabled (`hasCJKLanguage: true`)
- Goldmark passthrough for `\[ \]` / `$$ $$` (block) and `\( \)` (inline) LaTeX math
- FlexSearch with `tokenize: forward` for CJK-friendly search
- Code copy buttons on hover
- Git info enabled for last-modified dates
