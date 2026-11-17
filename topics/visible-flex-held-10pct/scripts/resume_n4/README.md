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

## Freeze an accepted physical metric and reuse its full map

`refine_fixed_large_radius.py` provides `build_seed(source_topic, checkpoint,
modes, angular=1280, ...)`. It accepts either a design checkpoint or an actual
coupled checkpoint. It copies that checkpoint's complete `physical_profile`
and physical port, with delta and vd fixed. It never substitutes the linear
root profile when given a coupled state. The solved `parameters` and
`central_correction_scales` define the old core; `core_summary` is only checked
for a reported discrepancy. A design state has q equal to the gauge amplitude
and c8=0, whereas a fixed-metric state has q=gauge*exp(p0) and all its controls.

The returned dictionary contains `obj`, `par`, `x`, `y`, `adaptive`,
`diagnostics`, both BVP classes, the original record and the full physical
configuration. At lambda=0 it preserves all old low support moments when
changing the canonical control basis. At positive lambda it freezes one
projection order J and embeds the entire old compact core in the nested
space. The old reference lift is projected from the solved core parameters;
pp(0) is used only to measure the inlet residual. The physical mesh is
normalized before the established [0,1] merge helper is called, so all old
knots are retained. Diagnostics compare F, Ft, Ftt and the complete mapped field. The seed
is not a solved refinement; the full original equation and metric audit
remain necessary.

For the genuine nonlinear tail, a caller can install its existing TailMixin
without querying an uninitialized boundary operator:

```python
seed = build_seed(
    source_topic, actual_checkpoint, modes=20, angular=1280,
    bvp_transform=lambda B: type('Coupled', (TailMixin, B), {}),
    evaluate_boundary=False,
)
obj = seed['obj']
obj.tail = actual_tail
# Continue the original actual-tail outer solve with its unchanged gates.
```

The CLI itself still uses the finite actual linear port. A check-only seed
comparison, for example, is:

```bash
python -u refine_fixed_large_radius.py --source-topic source/bundle/topics/visible-flexible-closed-surface --checkpoint large-radius-eta010-vu035-q010-m16-lam0.json.gz --out eta010-q010-fixed-m20-check --modes 20 --angular 1280 --check-only
```

`refine_fixed_large_radius_pre_parameter_truth.py` is the exact frozen source
of the first q=.01/M20 run, whose input summary agrees exactly with its solved
parameters. New runs use the main driver. The archived variant is retained
only to make that run's source hash reproducible.
