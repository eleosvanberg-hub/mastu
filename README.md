# MAST Disruption Predictor

A machine-learning system that watches a MAST tokamak plasma shot as it unfolds and raises an alarm before a disruption happens, using only information available up to that moment. Built as a portfolio research project — see `docs/SPEC.md` for the full design and `NOTES.md` for the working log.

## Status

**Phase 0 — scaffold only.** The repository layout, config, and one smoke test exist. No data has been downloaded, no model has been trained, no results exist yet. Every number below is `TBD — not yet run`, per project policy of never fabricating results.

## Why

Disruptions are an uncontrolled loss of plasma confinement; in large machines they can damage the machine, so predicting them early enough to act is an open problem. This project builds a leak-free, honestly-evaluated pipeline on public MAST data (FAIR-MAST) as a way to learn the full ML workflow — labelling, features, models, evaluation — on real physics data.

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

The full pipeline is also runnable end-to-end from `notebooks/colab_pipeline.ipynb` (designed to run from an iPad via Google Colab).

## Results

TBD — not yet run.

## Limitations

Labels are algorithmic and imperfect (see `docs/SPEC.md` Section 5). Only 4 global signals are used (`ip`, `power_radiated`, `neutron_rates_total`, `power_nbi`), with no magnetics or profile diagnostics. Data is from MAST (2000–2013), not MAST-U. Evaluation is offline, not real-time control. Results, once they exist, come from a subset of shots unless stated otherwise.

## Credits

Data: FAIR-MAST, UKAEA, CC BY-SA 4.0.
