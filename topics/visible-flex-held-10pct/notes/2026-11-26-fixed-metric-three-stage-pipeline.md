# 2026-11-26: fixed-metric unknown-core refinement entry

Session: `Astra-held10-06bbeb39-20261126 / fixed_metric`.

This record concerns the fixed metric interpretation proved in
`results/R63-fixed-metric-and-solution-core-variables.md`. It does not establish
a fixed-metric solution sequence, exact held arc, nonlinear tail, closed
surface, time family, reach, or the 10 percent displacement objective.

## What is frozen and what is solved

The first accepted portable source run supplies its actual
`delta = physical_profile.delta + raw.p[0]`. The new constructor uses
`fixed=True` with that entire physical profile. The original tail parameters,
cut, bridge, material core homotopy settings, angular chart, warp reference,
gauge amplitude, and branch interval `[.055,.065]` are retained.

The parameter `p[0]` now means `log(q_actual/q_seed)`; it never changes delta.
The remaining support coefficients, and the field, are unknowns of the same
boundary problem. Increasing their representation dimension is useful only
if the actual full solutions converge in C2 to a single nonzero core and
field. Merely preserving delta or producing three finite returns proves no
such convergence. The fixed finite vertical mean rule is always 1168 nodes.
Its gap to the exact angular mean remains an explicit analytic debt.

The original `WarpedBVP.terminal` is

    q * (dy_z - sigma * (Dmatrix @ y_z) / sqrt(E_cut)) / bcweights.

Consequently `terminal * bcweights` is the unscaled physical linear DN
residual. The new entry checks both that residual and the original full
scaled boundary vector. The pipeline fixes each literal floating
`bcweights[j]` to `.02` instead of re-forming a ratio that can differ by one
binary rounding unit across stages.

## Preserved numerical problem

`fixed_m3_branch_refinement.py` uses the original installed analytic Jacobian,
domain-aware Newton, RMS off-midpoint domain guard, boundary equations and
physical quintic exporter. Pointwise Jacobian evaluation is divided into
batches of 8 radial nodes to limit temporary storage; the derivative formula
is not replaced. The source raw return and physical field hashes are checked.

Original design and fixed constructors can have different numerical
meridian coordinates. The initializer therefore maps old raw `t` to old
physical `s`, and then applies the new fixed inverse chart. It never silently
interprets old `t` as the new coordinate. For mode enlargement it uses the
registered exact-lift transfer

    Y_new = embed(Y_old) + a(s) * chi(s) * (I_new - embed(I_old)).

The coefficient is exactly one, with no homotopy-lambda multiplier. This is
an initializer identity, not a claim that the newly interpolated or solved
field is already accepted.

The entry deliberately handles the original linear terminal equation. It
rejects an input labelled as having requested the actual nonlinear tail;
such an input must not be silently converted to a linear boundary problem.

## Declared three-stage pipeline

`fixed_m3_refinement_pipeline.py` requires an actually converged M24 portable `run.json`
and its same-worker `physical.npz`, plus an M32 linear port generated from the
same physical tail data. It calls three separate solver processes:

| stage | modes | equation angular nodes | initializer radial refinement | RHS tolerance | scaled BC tolerance | physical BC gate |
|---|---:|---:|---:|---:|---:|---:|
| first fixed-g solve | 24 | 768 | 1 | 1e-6 | 1e-7 | 2e-9 |
| same-M numerical refinement | 24 | 1536 | 2 | 1e-8 | 1e-9 | 2e-11 |
| first modal increment | 32 | 2048 | 1 | 1e-9 | 1e-10 | 2e-12 |

Every stage requires the original finite component FFT metric gate <=1e-6,
the independently reconstructed sampled relative operator gate <=1e-6, the
declared nonzero branch, actual BVP success, and its displayed BC gates.
The vertical mean1168 and boundary normalization .02 are identical. A
missing, interrupted, unaccepted, or metric-rejected stage stops this
pipeline and records its actual return. It is never promoted to accepted.

Example after placing the scripts in `scripts/resume_20261126/`:

```sh
python -u scripts/resume_20261126/fixed_m3_refinement_pipeline.py \
  --repo /same-runner/math-research-public \
  --source-run /same-runner/m24-accepted/run.json \
  --port32 /same-runner/same-physical-m32-port.json \
  --q-branch .055 .065 \
  --jac-batch 8 \
  --max-nodes 6000 \
  --outdir /same-runner/fixed-g-refinement
```

The input files named by the original portable command must still exist in
the same runner. No new token, authenticated URL, or private data belongs in
the generated records.

## What the C2 comparison actually evaluates

`fixed_m3_compare_c2.py` requires identical physical/profile/chart/core/gauge
metadata and original source hashes. It reconstructs both fields in one
common computational `(s,psi)` chart. With the same mean rule, it evaluates
the six Cartesian jets `F, Fs, Fpsi, Fss, Fspsi, Fpsipsi` on the union of
the two grids, their midpoints, uniform radial nodes, and samples immediately
left of the interior knots. The angular diagnostics use 512, 1024, and 2048
points. Position uses the true primitive of the finite mean rule, evaluated
numerically with positive Gauss6 and Gauss12 cell quadrature. Their observed
difference is recorded; it is not declared a certified integration bound.

The complete-map formulas include the non-Fourier exact reference lift and
its derivatives:

    F = geo.pos + q * values(Y,B) + height * ez
    Fs = geo.s1 + q * values(Ys,B) + mean * ez
    Fpsi = geo.p1 + q * values(Y,B1)
    Fss = geo.s2 + q * values(Yss,B) + mean_s * ez
    Fspsi = geo.sp + q * values(Ys,B1)
    Fpsipsi = geo.p2 + q * values(Y,B2).

The derivative of the mean uses the original `velocity_s`, evaluated on the
same 1168 angular nodes. No free mean constant, slope, or second derivative
is optimized. Both height primitives use the same zero origin.

The finite literal support coefficient differences are also summed exactly
as rational numbers in weighted l1_0, l1_2 and l1_4 norms, after zero extension.
These sums bound the displayed finite coefficient differences; they do not
bound any uncomputed exact-solution Fourier tail. The pair with constant M
and the pair with increased M are labelled separately. One modal increment
cannot establish a Cauchy sequence. All continuous-C2 and limiting-core
flags remain false.

## Actual execution status at reconstruction

Before the temporary execution environment reset, an earlier version of the
fixed-g entry was run once locally on the explicitly unaccepted M24 raw
snapshot. It reached an initial-domain event with 418 nodes, delta
`.06413464104697915`, actual q `.06`, and maximum RHS
`4.6999814719027`, at elapsed `3.2079702819901286` seconds. The process later
returned exit 137/SIGKILL before a Jacobian-return or accepted BVP was
recorded. The cause of that external termination was not proved. It is not
a mathematical failure certificate. No fixed-g field, metric pass, or C2
comparison resulted from that attempt.

The reset removed the earlier unpublished driver and local attempt files.
This driver/model/pipeline was reconstructed from the published original
source and the preserved task record. The three entry files and comparison
passed `py_compile`; the main solver's `--help` invocation also returned
normally. No large local BVP was rerun after the reset. Numerical evidence
must come from subsequent actually observed same-runner returns.
