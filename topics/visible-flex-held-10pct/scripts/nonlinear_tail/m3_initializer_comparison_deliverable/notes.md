# Three initializations for one q=.025 trial height vector

**Numerical algorithm evidence.** All three trials have exactly the same
physical tail, complete target height vector, M16/parts8 discretization,
local positive-root guards, full boundary residual, sparse Newton linear
equations, line search and final 2e-9 acceptance threshold. The target
vector came from the q=.025 prefix *initial guess*, obtained by scaling
the accepted q≈.020001546 field. It is not an actual q=.025 coupled-prefix
endpoint. These failures do not establish a coupled-amplitude bound.

| Initializer | First complete residual | Local root result | Final status |
|---|---:|---|---|
| Original common scaling plus cut correction | not available | stage38 local root stops near numerical A floor .05 | initialization failure, no complete shooting iteration |
| Unscaled previous accepted nodes | .19993815097 | minA .44089884, minD .99972592 | cancelled after two accepted original line-search steps, not a solver failure |
| Complete original linearized predictor | 2484.139389 | full predictor minA .24522231, minD .99965657 | original line search fails at iteration3; last residual2249.115964, minA .05144545 |

The first row and the exact pointwise diagnostic are already frozen in
the preceding amplitude-initializer package. This appendix records the
other two actual experiments and their source.

## Why the previous state is a valid initial guess

Let stored node states be Y_n=(Q_n,P_n), local flow maps Phi_n, and deep
linear graph G_N. The original residual already contains every row

    Phi_n(Y_{n+1})-Y_n,  Q_0-H/r_cut^4,  P_N-G_N Q_N.

Its original Newton system contains the new cut boundary column as well
as all interior and deep rows. Initial guesses are therefore not required
to satisfy the new Dirichlet condition. Changing H changes only that
boundary residual and its normalizing scalar; it does not alter any
local flow or local root of a given complete state.

More precisely, if alpha=||H_new||_infinity/||H_old||_infinity, the internal
and deep residuals of an unchanged old state, in the new normalization,
are the old values divided by alpha. The new cut residual is computed
directly from its actual Q_0. For exactly proportional targets and an
exact old cut this gives max(R_internal/alpha,|alpha-1|/alpha). Here
alpha=1.24990336835 and the actual complete evaluation gives
.19993815096588216 while retaining every old local-root margin.

The unscaled-state trial subsequently takes two accepted line-search
steps, with residuals .19837613416 and .19682632061. Their cut-dominated
reduction is about 1/128 each. This targeted comparison was then explicitly
cancelled to continue the linearized-predictor experiment and the q=.021
coupled branch. Its observed exit code is130; no mathematical failure or
terminal nonlinear solution is inferred from cancellation.

## The full linearized predictor is only an initial guess

The second runner evaluates the original all-node Jacobian at the accepted
old state and solves the original Newton correction system with the new
Dirichlet right-hand side. It tests that predicted state with the original
complete evaluate function. Lambda1 passes every local root, but its
residual is2484.139389. This is not an accepted line-search step from the
old residual .199938. It is explicitly chosen as a new initial guess,
after which the unchanged original nonlinear solver runs and must pass
the original final acceptance threshold.

That solver produces residuals2484.14,2330.64,2257.94,2249.12, with minimum
A falling toward .05, and then reaches its genuine original line-search
failure. The failed state is retained in scratch for diagnosis; it is
not an accepted checkpoint. Root positivity was not deleted or relaxed,
and no larger iteration limit was substituted.

This isolates two separate facts: a full nonlinear linearization provides
a healthier initial state than common amplitude scaling for this vector;
it does not yet yield an accepted solution for that fixed vector. The
actual q=.021 prefix/tail run remains separate and active at freeze time.
Its complete initial tail vector has passed, and its prefix is being
solved with the original actual-DN outer check.

## Reproduction

The previous packages regenerate the accepted refined response and the
q=.025 initial request. For the direct-state control use:

```text
node solve_m3_tail_from_previous.mjs SOURCE_TOPIC OLD_ACCEPTED_RESPONSE \
  Q025_REQUEST_RESPONSE OUTPUT_JSON_GZ
```

For the predictor experiment first run:

```text
python make_m3_tangent_predictor_runner.py \
  --source solve_m3_tail_from_previous.mjs --output WORK/predictor.mjs
```

Invoke the generated runner with the same four arguments. Set
`VISIBLE_FLEX_SPARSE_LINEAR_HELPER` to the original frozen sparse helper.
The generator verifies exactly one occurrence of each of its five
anchors and records both source hashes. The original DN source is never
edited. Full states, H vectors and traces remain runtime data; this
appendix contains code, compact scalar records and output hashes only.
