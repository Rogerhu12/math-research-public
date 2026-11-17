# Resumed n4 local circularization and matched angular coordinates

This package contains source and physical parameters. It contains no solved
closed surface. The finite prefix still uses the original physical **linear**
mode-4 tail DN. Every design changes delta and vd; a table of these designs
is not a fixed-metric convergence sequence.

## Source preparation

`prepare_scripts.py` copies the exact existing dependencies from the sibling
`even_circle/double_prefix_first` and `even_circle/material_restart` packages,
checking their recorded SHA256 values. Work in a scratch destination:

```bash
python TOPIC/scripts/resume_n4/prepare_scripts.py --dest WORK/n4
python TOPIC/scripts/even_circle/double_prefix_first/recover_m3_source.py --repo REPO --dest WORK/n4/source
python TOPIC/scripts/even_circle/double_prefix_first/export_original_worker_port.py --source-topic WORK/n4/source/bundle/topics/visible-flexible-closed-surface --config TOPIC/scripts/even_circle/double_prefix_first/mode4_physical_config24.json --out WORK/n4/mode4_port24.json
```

The original port hash is
`2a3412f96702f409b2e074ac23b3223d4e0f1d0fe1f1114e7ae34911a5bf9095`.
The 70-file historical source recovery is unchanged. The commands below
assume the working directory is `WORK/n4` and refer to its recovered source.

## New definitions

`local_flatten_core.py` uses the R22 optimum eta=.3674128048915633 and a
C4 cutoff supported in the circle plus its transition. It replaces the
original global plateau waveform by a local flattening and one complementary
mean correction. It retains all actual core parameter derivatives and the
original positive-rho gate, with the correct eta>1/3 radius bounds.

`bimodal_chart_loader.py` explicitly transforms both the inlet and the
s-dependent angular chart to the complete two-harmonic arclength map. It
includes every first and second coordinate derivative. The physical metric,
Frenet equation, terminal DN, root guard and acceptance conditions are not
changed. The chart becomes the identity, with two derivatives, at the cut.

`dual_material_restart.py` and `bimodal_material_restart.py` only construct
initial guesses. They pull the old full reference lift and perturbation
back at fixed material angle, then project. Both physical profile parameters
are predicted. The latter refuses a checkpoint from a different angle
chart unless an explicit conversion is provided. `--previous` adds a secant
from two accepted same-family amplitude states. None of this is a solved
continuation step until the original BVP accepts and full metric is audited.

## Exact actual design commands

The original single-harmonic chart and the new local target:

```bash
python -u run_local_flatten.py --source-topic source/bundle/topics/visible-flexible-closed-surface --port mode4_port24.json --profile root03-profile.json --out local-q005-m8-opteta --q .005 --modes 8 --bimodal-eta .3674128048915633 --lambdas 0 .05 .1 .2 .4 .7 1 --nodes 201 --max-nodes 2400 --tol 1e-6 --angular 512
python -u run_local_flatten.py --source-topic source/bundle/topics/visible-flexible-closed-surface --port mode4_port24.json --profile root03-profile.json --out local-q005-m12-opteta --q .005 --modes 12 --bimodal-eta .3674128048915633 --lambdas 0 .05 .1 .2 .4 .7 1 --nodes 201 --max-nodes 3000 --tol 3e-7 --angular 768
```

The second historical run was intentionally canceled during lambda=.05,
after the accepted lambda-zero outcome. It has no terminal mathematical
outcome for lambda=.05. The first stops at its actual failed lambda=.2.

The lower-curvature vu=.35 profile, original physical port and full matched
angle chart:

```bash
python -u run_bimodal_chart.py --source-topic source/bundle/topics/visible-flexible-closed-surface --port mode4_port24.json --profile vu035-profile.json --out bimodal-chart-vu035-q005-m8 --q .005 --modes 8 --bimodal-eta .3674128048915633 --lambdas 0 .05 .1 .2 .4 .7 1 --nodes 201 --max-nodes 3000 --tol 3e-7 --angular 512
python -u run_bimodal_chart.py --source-topic source/bundle/topics/visible-flexible-closed-surface --port mode4_port24.json --profile vu035-profile.json --out bimodal-chart-vu035-q005-m16 --q .005 --modes 16 --bimodal-eta .3674128048915633 --lambdas 0 .02 .05 .1 .2 .4 .7 1 --nodes 201 --max-nodes 3200 --tol 3e-7 --angular 1024 --restart bimodal-chart-vu035-q005-m8-lam0.json.gz
```

The M16 run is a new design, not a fixed-metric refinement. Only completed
rows explicitly recorded in `local_design_runs.json` are asserted. Other
steps in these command lines are prospective or still running.

## Diagnostics and hashes

`audit_local_target.py` and `audit_bimodal_chart.py` use `bundle/...` as the
source path; symlink the recovered `source/bundle` as `bundle` in scratch or
change that literal scratch path. `design_vu035.py` regenerates the new finite
linear double root using the unmodified source profile and original DN.
Its finite root and sampled geometry do not establish nonlinear existence.

`nested_terminal_provenance.json` separately records the old unreported J8
nested M12 mesh-limit failure; it does not rerun a registered calculation.
`local_design_runs.json` gives physical parameters, actual solver results,
small scalar diagnostics, output hashes and intentional cancellations.
No coefficient arrays or generated checkpoints belong in Git or Releases.
