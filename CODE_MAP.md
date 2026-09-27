# CODE_MAP — a tour of this repo

Written for a beginner. Read the files in roughly this order as each phase fills them in. Right now (end of Phase 0) every module below is an empty stub with a one-line docstring — nothing runs yet except the smoke test.

## Where to start
1. `docs/SPEC.md` — what we're building and why. Read this first, always.
2. `CLAUDE.md` — how we work (rules, style, workflow). Not code, but shapes every file here.
3. `src/config.py` — every tunable number in the project, each with a one-line comment explaining the choice. If you're ever unsure why a threshold has the value it does, look here first.

## `src/` — the library code
- **`config.py`** — parameters shared by every other module: `IP_ON`, `WINDOW_MS`, `STRIDE_MS`, `HORIZON_MS`, `K_CONSEC`, `MIN_WARNING_MS`, `CQ_DROP_FRAC`, `CQ_MAX_MS`, `MIN_PEAK_IP`, `RANDOM_SEED`. No functions yet — just constants.
- **`data.py`** — will hold `load_shot_table()` (the big parquet of all shots), `load_shot(shot_id)` (one shot's time-series signals), and `download_shots(ids)` (cache signals to disk). Empty stub for now.
- **`labels.py`** — will hold `note_label()` (parse the operator's text comment for "disrupted"), `parse_note_time()` (pull a disruption time out of that text), and `detect_disruption(time, ip)` (the real, signal-based detector described in SPEC Section 5.2). Empty stub for now.
- **`features.py`** — will hold `window_features(shot_df, t_end, t_start)` (turn one window of raw signal into a row of numbers) and `shot_windows(shot_df, ...)` (slide that window across a whole shot). Empty stub for now.
- **`dataset.py`** — will hold `select_shots()` (pick which shots to use), `build_windows()` (run `features.py` over every selected shot), and `make_splits()` (train/val/test, split by shot so no shot leaks across splits). Empty stub for now.
- **`models.py`** — will hold the physics baseline (B0) and factories for the three ML models (M1 logistic regression, M2 random forest, M3 HistGradientBoosting), all sharing a `fit`/`predict_proba` interface. Empty stub for now.
- **`alarms.py`** — will hold `first_alarm(scores, times, thr, k)`: turns a stream of model scores into a single alarm time using the `K_CONSEC` rule. Empty stub for now.
- **`evaluate.py`** — will hold `shot_metrics()`, `tradeoff_curve()`, `bootstrap_ci()`, and the plotting functions used for the results in Section 11 of the spec. Empty stub for now.

## `scripts/` — things you run from the command line
- **`download.py`** — caches raw shot signals to `data/raw/{shot_id}.parquet`.
- **`label_report.py`** — produces the Phase 2 note-vs-signal label reconciliation report.
- **`build_dataset.py`** — runs the full feature pipeline and writes `data/processed/windows.parquet`.
- **`run_experiment.py`** — trains one model and writes its results to `results/<exp_id>/`. Takes `--exp` and `--split`.

All are empty stubs for now.

## `tests/`
- **`synthetic.py`** — not a test file itself; generates fake shots (ramp-up, flat-top, then either a clean quench or a slow ramp-down) so the other tests don't need network access.
- **`test_labels.py`, `test_features.py`, `test_dataset.py`, `test_alarms.py`** — will hold the required tests from SPEC Section 12, one file per module under test. Empty stubs for now.
- **`test_smoke.py`** — the one real test right now: checks `src/config.py` imports and `RANDOM_SEED == 42`. Exists purely so `pytest` has something to run before Phase 1 exists.

## `notebooks/colab_pipeline.ipynb`
The end-to-end notebook the owner runs from an iPad. Currently just a title cell and a `pip install -r requirements.txt` cell; will grow one section per phase.

## `data/` and `results/`
`data/` is never committed (see `.gitignore`) — it holds downloaded shot signals and the built window table, both regenerable from `scripts/`. `results/` holds small, committed outputs (`metrics.json`, `config.json`, PNGs under ~500 KB) from `scripts/run_experiment.py`, one subfolder per experiment ID.

## Docs
- **`NOTES.md`** — dated log of data surprises and judgement calls, in the order they happened.
- **`README.md`** — the public-facing summary: what this is, how to run it, and (once they exist) the results.
