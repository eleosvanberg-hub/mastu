# NOTES

Dated log of data surprises, decisions, and anything not certain about. See `CLAUDE.md` for what belongs here.

## 2026-09-27 — Phase 0: scaffold

- Moved `SPEC.md` from repo root to `docs/SPEC.md` per `CLAUDE.md`'s expected location.
- Created the repository layout from SPEC Section 13: `src/`, `scripts/`, `notebooks/`, `tests/`, `results/`.
- `src/config.py` holds every parameter from SPEC Section 4 (`IP_ON`, `WINDOW_MS`, `STRIDE_MS`, `HORIZON_MS`, `K_CONSEC`, `MIN_WARNING_MS`, `CQ_DROP_FRAC`, `CQ_MAX_MS`, `MIN_PEAK_IP`, `RANDOM_SEED`), each with a one-line why-comment. No other parameters (shot counts, split ratios, feature offsets, etc.) were added yet — those belong to the phases that use them.
- All `src/` and `scripts/` modules are currently empty stubs (one-line docstring only, matching Section 13's module list). No logic implemented yet — that starts in Phase 1.
- `tests/` has one real test (`tests/test_smoke.py`) checking `src/config.py` imports and `RANDOM_SEED == 42`, so `pytest` has something to run before Phase 1 exists. The other `tests/test_*.py` files are stubs matching Section 13's list, to be filled in as the modules they test are built.
- Network check (2026-09-27, this cloud session): **both required hosts are blocked by the session's egress policy**, not by a code or credentials problem.
  - `pd.read_parquet("https://mastapp.site/parquet/level2/shots")` → `URLError: Tunnel connection failed: 403 Forbidden`.
  - `xr.open_zarr("https://s3.echo.stfc.ac.uk/mast/level2/shots/11860.zarr", group="summary")` → `403 Forbidden` on `.zmetadata`.
  - The proxy status endpoint (`$HTTPS_PROXY/__agentproxy/status`) confirms both as `connect_rejected` / "gateway answered 403 to CONNECT (policy denial or upstream failure)" for `mastapp.site:443` and `s3.echo.stfc.ac.uk:443` — i.e. the CONNECT tunnel itself was refused, before any request reached FAIR-MAST's servers.
  - This is an environment/policy limitation of this particular cloud session, not evidence the URLs or data are wrong. The owner should confirm these hosts work from the Colab notebook (which the spec says has no such restriction) before Phase 1 downloads data; Phase 1 code and tests must not depend on network access from this environment.
  - Dependencies installed cleanly into a local `.venv` (`requirements.txt`, `zarr==2.18.7`, correctly `<3`), so the pipeline itself is not blocked — only outbound access to the two data hosts is.
