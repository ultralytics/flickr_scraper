# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

**Delete > Replace > Add.** Before writing any change, answer in order: what can I delete? what can I replace? only then, what must I add?

The most common agent failure in this repo is reaching for the locally-safest edit — a new guard, flag, or helper — instead of fixing ownership. These tripwires override that instinct:

1. **Never guard a symptom — relocate the trigger.** A fix that adds a condition to suppress bad behavior (a staleness check, an is-initialized flag, a skip-first-call guard, a try/except around broken logic) is wrong by default. Find the code path that should own the behavior, move the logic there, and delete the code that got it wrong. Example: a warning fired from stale state; the right fix was not a recency guard — it deleted the stale detection and moved the trigger into the code path that observes the event live.
2. **Bugfixes are net-negative by default.** A bugfix that adds more lines than it removes needs a one-sentence justification in the PR body naming why deletion and relocation were impossible.
3. **Search the repo before creating anything.** Before building a helper, search the whole repo — it likely exists (`utils/general.py` holds the shared helpers). If two scripts grow the same logic, consolidate into `utils/` and delete the duplicates. Avoid premature abstraction — three similar lines beat a helper nobody else calls.
4. **Deletion beats caution.** Zero regression means understanding the code you remove, not leaving it in place as insurance. Keeping broken or duplicated code "to be safe" is itself the regression: it is how repos rot. All changes must still ship debugged, validated, and production ready.

**Output gate:** every PR body must contain a `Deleted:` line naming the code removed (functions, branches, files, config). Features must name what they reused or consolidated. `Deleted: nothing` demands the rule-2 justification.

**Review gate:** adversarial reviewers must answer two questions before LGTM: (a) what could have been deleted instead of added? (b) does any added condition suppress a symptom rather than relocate a trigger? A finding on either blocks LGTM.

**This file is code — additions require deletions.** To add a rule here, remove or merge one. When everything is emphasized, nothing is.

**NEVER push to `main`. NEVER force push.** Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Launch an independent adversarial review agent with cold context (just the PR diff and this file) to hunt for bugs, regressions, and Core Principles violations — use the Codex CLI, one fresh `codex exec` run per round. Fix, push, and repeat until a fresh run reports LGTM.
3. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never force-push, reset, or revert commits you did not author.
4. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

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
