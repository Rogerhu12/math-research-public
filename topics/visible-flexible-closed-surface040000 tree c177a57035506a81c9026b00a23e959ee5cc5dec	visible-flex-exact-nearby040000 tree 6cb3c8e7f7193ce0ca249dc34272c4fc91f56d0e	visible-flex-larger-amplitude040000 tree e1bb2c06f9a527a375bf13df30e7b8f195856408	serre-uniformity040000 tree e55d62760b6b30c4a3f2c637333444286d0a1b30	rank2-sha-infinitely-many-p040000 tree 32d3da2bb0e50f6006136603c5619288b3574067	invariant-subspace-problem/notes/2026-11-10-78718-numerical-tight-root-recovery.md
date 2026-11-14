# Optional tight implicit arithmetic and the actual fast05 precision question

**Subsequent decision:** the one-stage original/tight and with/without-Jacobian
flows were identical. This tighter branch was not selected for fast06. The
actual fast06 command and the supported centered-retraction repair are in
[centered recovery](2026-11-10-78718-numerical-centered-recovery.md). The
conditional command below records the earlier unexecuted proposal.

2026-11-10, Astra-visible-flex-78718bd0. This is a numerical investigation and
an available recovery command. It does not assert that tighter root tolerances
will cure the observed shooting residual, and does not change the original
`2e-9` shooting target.

## 1. Actual unresolved residual and observed endpoint roots

Root observed fast05 naturally complete with **`9fa811`, exit 2**, after
1385.588147 seconds and zero inner prefix solves. Its iteration 3 had norm
`3.3366011642270125e-9`; the original ten trial steps did not decrease that
norm. This is a finite numerical failure, not a nonexistence result.

Read-only observation `1823c3` found the maximum at stage 12, raw cell 0,
raw segment 7, momentum component 42 at W22, hence physical frequency 63.
The absolute residual was `2.141778724366807e-12`, divided by the original
height scale `0.0006419043268729995`. The target absolute residual at that
scale is `1.283808653745999e-12`. The saved left high-mode coordinate is only
`-5.192449055198756e-16`, so rounding this stored near-zero coordinate itself
by one ulp does not explain the residual.

The ordinary momentum root stops at

$$
\|m(L)-\tau\pi\|_\infty
\le 8\cdot10^{-14}\max(\text{maxQuad},\|\tau\pi\|_\infty),
$$

and has a separate `5e-12` roundoff fallback. A threshold is a possible
backward-error allowance, not an observation that this error occurred. At the
left endpoint, read-only `882d40` found max absolute momentum `9.62075016254745`,
in frequency 3. Merely converting `8e-14` times that quantity to the shooting
scale gives `1.1990260554141317e-9`; the analogous fallback scale is
`7.493912846338324e-8`. These are not bounds on the propagated flow error.

The decisive permitted endpoint experiment was performed by the tail agent:
`b153f3/session7091` followed by **`565062`, natural exit 0**, 2.698 seconds,
with zero ODE/DN/BVP calls. At both actual stage endpoints the old root was
already much more accurate than its stopping threshold: relative residuals
about `9.19341e-17` and `1.65085e-16`, each after two Newton iterations.
Tighter roots from the default guess and from the old L were identical in all
saved L, mean, Gram and leading values. Frequency-63 equivalent momentum
residuals were only about `3.96e-19` and `1.50e-18`. The Gram condition numbers
were about 1.002378 and 1.001226. Thus **the two endpoint stopping thresholds
are not an observed cause** of the `2.14e-12` flow discrepancy.

The actual scalar report is
`2026-11-10-78718-tail-root-precision-point-01.json`; the implementation is
`78718-tail-root-precision-point-diagnostic.mjs`. A first environment-only
attempt lacked the existing source cache setting and exited before any
mathematical call; that failed attempt is retained in the tail agent's record.
The next authorized causal comparison is one original stage-12 flow, old/tight
and with/without Jacobian, at the same S32. No whole-tail rerun is required to
answer this local question.

## 2. Existing stable algebra and the remaining places to inspect

The active root does not naively subtract `omega-1`. It already computes the
stable quadratic correction `quad` and then `moments=L+quad`. The split RHS
also projects its linear angular flux exactly. Therefore replacing an
imagined naive omega subtraction would not target the implementation used in
this run.

For a fixed state and geometry, let sigma be `r_x/r`, tau the momentum factor,
and N_j the nonlinear angular flux projection. The implemented momentum RHS
has the exact form

$$
R_{\pi,j}(L)=4\sigma\pi_j+
\frac{\sigma n_j}{\tau}
\big[-n_jL_j+(n_j^2-1)p_j+N_j(L,Q)\big].
$$

Thus replacing an approximate root L by another L+delta changes this RHS by

$$
\Delta R_{\pi,j}=\frac{\sigma n_j}{\tau}
\big[-n_j\delta_j+\Delta N_j\big].
$$

This identity shows why small high-mode root or angular-projection effects
can be amplified. It is not an error estimate: the nonlinear term may add or
cancel, and the actual RK propagation must be checked. Existing engines
already count RHS root evaluations, maximum relative residual and roundoff
fallbacks. The previous worker did not emit those counters. The new optional
worker emits them without evaluating any extra root or ODE.

## 3. Explicit optional implementation

Default `--tail-root-precision original` retains all previous factories.
`--tail-root-precision tight` selects four new files:

- `78718-tail-fourier-root-tight-momentum.mjs`: nominal root and mean tolerance
  `4e-15`, fallback `2e-14`; the original equations, 30 iterations, 20 inner
  backtracks and projection floor remain.
- `78718-tail-fourier-root-tight-split-engine.mjs`: the same split RHS and R89
  variational flow around that explicitly tighter root factory.
- `78718-tail-geometric-newton-retraction-tight-v3.mjs`: the same R95 mean-seeded
  retraction, with its mean tolerance also `4e-15`.
- `78718-prefix-tail-geometric-precision-worker.mjs`: explicit selection and
  actual root-counter progress; it can use geometric or momentum trials.

The generic driver and client add only this explicit future selection. The
worker and root source of fast05 are retained unchanged. Physical cfg gets no
new precision field; source identities, ready labels and run metadata record
the actual algorithm separately. Root mean precision does not replace the
unchanged finite-DN and final closed-map tolerances.

Limited entry checks actually completed: `2d5a74` parsed Python and selected
the new worker and all ten present dependencies, exit 0 with no worker/solver;
`b83bfe`, `82b7ed`, `72061a` were successful syntax checks of the new root,
worker and mean helper. These checks are not evidence of a new DN solution.

## 4. Concrete recovery command, if selected after the local comparison

The actual iteration-3 input is retained byte for byte in
`2026-11-10-78718-numerical-m15-w22-fast-05-iteration3-root-diagnostic-input.json.gz`
(385541 bytes, SHA256
`18996bebb3b93b2b092c31e7e16f956a3826071133d40c01ac20dfe931adf7d9`).
It is explicitly **UNCONVERGED**. Read-only `f50e2b` actually compared its cut
height to `.125` times the padded successful seed height: every binary64 value
was identical, maximum difference zero and the worker's first amplitude ratio
exactly 1. There is no second multiplication of the saved state by 1/8.

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --tail-trial geometric --tail-root-precision tight \
  --bootstrap-height-scale 0.125 \
  --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-05-iteration3-root-diagnostic-input.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-06
```

The known successful W15 packet still supplies the old physical parameters
and original H; it is not relabelled as a W22 solution. The new W22 response
must actually solve H/8 and then return the unchanged original H through the
existing real continuation. This command is available, not a claim that the
endpoint test has proved it necessary or sufficient.
