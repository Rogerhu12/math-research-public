# Same-state split-flux check and numerical subdivision screen

These are diagnostics of the fixed m3 physical metric from the coupled q=.02
seed. They neither prove an amplitude obstruction nor produce an accepted
M12/M16 refinement by themselves.

## Original M16 terminal iterate

The original Riccati-based M16, N256, 64 steps per shooting stage, two parts
per original segment warm solve stopped at iteration 10 with the original
multiple-shooting line-search failure. Its normalized residual was
6.872622581583858e-7, minimum A .44094616029086336, minimum D
.9997259416486404. It did not pass the original 2e-9 tolerance. The intermediate
Riccati projection's reported maximum condition number was
128258323142.35878. This large number is associated with this run; it alone
does not prove the cause of failure or a singularity of the physical surface.
The failed worker retained every node state for diagnosis and possible future
initial guesses. A failed saved state is not an accepted solution.

The exact original split-linear-flux-v1 factory was reconstructed at that
same saved iterate. Its state-only and state-plus-variational maps agree
component by component, and both reproduce the stated 6.872622581583858e-7
residual. Thus a discrepancy between these two evaluation paths is not the
observed issue in this comparison. The residual maximum is at shooting
stage14, physical cell0, original segment1. That stage's Jacobian infinity
norm is 2.255766853099976e20, also the maximum over the sampled stages.
No condition number for the full boundary-value problem follows from this
single map norm.

An early diagnostic accidentally constructed the unsplit stage-core engine
instead of the actual split wrapper. It gave a different numerical map and
is not used for the worker comparison. The wrong-backend script and result
are retained locally under names ending in `raw_core` or `raw-core-not-worker`.
The supplied diagnostic explicitly imports `950f-tail-stage-split.mjs` and
records its rhsEvaluation tag. It uses the actual physical cut radius.

## Why shorter shooting stages are a concrete next numerical test

The screen holds the physical factory and the total number of RK4 steps per
original segment fixed at 128. It varies only the shooting subdivision and
uses the original linearColumn background first-variation equation. It
covers physical cells0 through7 and represented frequencies3 through48.

| Parts per original segment | RK steps per new stage | Largest background stage norm, M16 | Location |
|---:|---:|---:|---|
| 2 | 64 | 2.2557147626e20 | cell0/segment1, raw [.5,1] |
| 4 | 32 | 1.6937700315e17 | cell0/segment1, raw [.5,.75] |
| 8 | 16 | 8.8744875604e12 | cell0/segment1, raw [.625,.75] |
| 16 | 8 | 6.5064161086e10 | cell0/segment1, raw [.625,.6875] |

For comparison, the already accepted M8 original two-part discretization has
maximum background stage norm 3.7016690246e13. This comparison motivates an
M16 eight-part trial; it is not a nonlinear feasibility or capacity bound.
Only a genuine full-height nonlinear solve with the unchanged root guards,
line search, and 2e-9 acceptance tolerance can establish a new accepted point.

All three current refinements use the identical full physical metric
descriptor SHA256
11a9de4da186d04dd1e925678582b0f6861425b4e0e2217937ec53ba052db125.
The eight-part trial has the same 128 nonlinear RK steps and 512 background
linear RK steps per original segment. Its regenerated canonical cut and
physical parameters match exactly; finite linear slopes differ from the
two-part arithmetic by at most 6.3155312091e-9 (roundoff/reordering, not a
changed physical profile). The original numerical angle chart also stays
fixed. These facts do not waive the final nonlinear acceptance test.

## Reproduction and status

Use the 70-source restore from the frozen m3 seed bundle. Given the retained
failed original M16 checkpoint, the actual same-state audit is

```
node audit_failed_map_consistency.mjs SOURCE_TOPIC FAILED_RESPONSE OUTPUT.json
```

The background subdivision screen needs no field or DN array:

```
node linear_stage_amplification.mjs SOURCE_TOPIC tail-numerics.json OUTPUT.json
```

The original M16 failure's source/config/checkpoint hashes and actual coupled
wrapper command are in record.json. Generated node states, matrices and DN
arrays remain outside the repository.

The record's active-run snapshots are explicitly **not terminal outcomes**.
The original M12 run and sparse two-part M16 run continue under their original
iteration caps. The sparse eight-part M16 test is a separate numerical
attempt. Their future accepted/failure outcomes belong in new records, not
retroactive changes to this frozen diagnostic.
