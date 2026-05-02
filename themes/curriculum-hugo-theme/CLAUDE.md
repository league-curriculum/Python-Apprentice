# Curriculum Hugo Theme

Hugo theme for League of Amazing Programmers curricula.

## Version

The version in `theme.toml` must stay in sync with the parent project's
`pyproject.toml` version. Both use the format `0.YYYYMMDD.revision`.

**Do not bump the version manually.** Use `just bump-push` from the parent
curik repo — it updates both files, tags both repos, and pushes.

## This is a subdirectory of curik

This theme lives at `curriculum-hugo-theme/` inside the curik repo. It is
also published as a standalone repo at:

  https://github.com/league-infrastructure/curriculum-hugo-theme

When curik scaffolds a course, it copies this theme into
`themes/curriculum-hugo-theme/` in the course repo. Later it will become
a git submodule.

## Structure

```
layouts/
  _default/baseof.html     — base HTML template
  shortcodes/
    instructor-guide.html  — collapsible instructor content
    callout.html           — info/warning/tip boxes
    readme-shared.html     — content for site AND README
    readme-only.html       — README only, hidden from site
assets/
  css/instructor-guide.css — styling for instructor guides and callouts
theme.toml                 — Hugo theme manifest + version
```

## Shortcodes

- `{{</* instructor-guide */>}}...{{</* /instructor-guide */>}}` — instructor-only content
- `{{</* callout type="tip" */>}}...{{</* /callout */>}}` — info/warning/tip boxes
- `{{</* readme-shared */>}}...{{</* /readme-shared */>}}` — appears on site AND in README
- `{{</* readme-only */>}}...{{</* /readme-only */>}}` — README only, hidden from site
