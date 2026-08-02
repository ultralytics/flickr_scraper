# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Dev install (CI adds --system; drop it inside a venv)
uv pip install -r requirements.txt pytest ultralytics

# Run all tests (hermetic — no network or Flickr credentials needed)
pytest -q

# Single file / single test
pytest tests/test_flickr_scraper.py
pytest tests/test_flickr_scraper.py::test_get_urls_uses_json_search_and_redacts_output -v

# Byte-compile every file, as CI does before tests
python -m compileall -q .

# Run the scraper (needs Flickr API credentials)
python flickr_scraper.py --search 'honeybees on flowers' --n 10 --download
```

- CI (`ci.yml`) runs on ubuntu-latest / Python 3.11, on push and PR to `main` plus a daily 08:00 UTC cron; its steps are the uv install, `compileall`, then `pytest -q`. README states Python 3.8+.
- No local Ruff or pytest config exists — formatting is applied by Ultralytics Actions (`format.yml`), not a repo config file, so there is nothing to run locally beyond the bot.

## Architecture

Single-script scraper, not a package. `flickr_scraper.py` is the entry point: `resolve_credentials()` reads the API key/secret from `--key`/`--secret`, then the `FLICKR_API_KEY`/`FLICKR_API_SECRET` env vars, then the module-level `key`/`secret` constants; `get_urls()` calls the Flickr `photos.search` JSON API, keeps only photos exposing `url_o`, de-dupes URLs within a run, and (with `--download`) saves via `utils.general.download_uri` into `./images/<search>/`, with spaces in the search term replaced by underscores (e.g. `./images/honeybees_on_flowers/`).

- `utils/general.py` — the shared helpers (`safe_filename_from_uri`, `download_uri`); this is the only module imported by both `flickr_scraper.py` and the tests.
- `utils/` also holds standalone scripts run directly, never imported: `clean_images.py` (dedupe/resize a scraped folder; needs OpenCV, which is **not** in `requirements.txt`), `multithread_example.py`, and `flickr_scraper_noapi.py`.
- `tests/conftest.py` puts the repo root on `sys.path`; tests monkeypatch `FlickrAPI` and `requests.get`, so the suite never hits the network or needs credentials.

## Conventions

- Every Python file and workflow YAML starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Google-style docstrings; the Actions bot runs Ruff, docformatter, prettier (YAML/JSON/Markdown), and codespell on PRs, and its prettier output can differ from local — expect bot commits on the PR branch.
- Keep tests self-contained: no live Flickr calls and no credentials; new tests should monkeypatch `FlickrAPI`/`requests` rather than reach the network.
- No version string or release process — the repo ships as a script, not a PyPI package (README cites a Zenodo DOI for citation).
