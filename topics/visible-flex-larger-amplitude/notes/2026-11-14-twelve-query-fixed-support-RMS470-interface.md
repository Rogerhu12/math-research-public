# Twelve complete query grids with fixed projection-correction support

This is an executable interface for one further unaccepted warm step,
not a numerical result. It continues the actual request37 field, adds
the observed left-RMS470 constraint, and keeps the correction made by
the local C projection on the previous physical nodes471–482 and the
three original global controls. The complete domain operator still
contains node470 and every original exact-coordinate column.

The evidence is recorded in
[the actual37 note](2026-11-14-actual-request37-eleven-query-warm-and-RMS470.md).
During that actual request37 execution, the nearest rejected step, alpha1/8, had finite
original nodes and collocation midpoints and positive values on all
eleven modeled grids. The original complete left-RMS test nevertheless
rejected interval470, with minimum beta squared
`-0.2501880308616917`. Alpha1/4 also failed that same original query.
This justifies adding that complete query. It does not separate the
causal effects of the raw LSMR direction and the previous local
projection correction. Fixing the correction support is an explicit
algorithm choice to examine that boundary behavior.

All original nonlinear equations, finite field, scalar formula, full
linear model A, merit, real node/mid/RMS tests, material rho guard,
seventeen backtracking trials and fresh affine boundary FD remain.
The original completed zero-H T112 Jacobian is held explicitly affine;
there is no asserted nonlinear native solution at the new height.

## 1. Frozen independent sources and actual parent

All paths in this table are under `computations/`.

| Source | Bytes | SHA256 |
|---|---:|---|
| `geometry_20261114_twelve_query_domain_operator.py` | 27284 | `6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f` |
| `geometry_20261114_fixed_support_halfspaces.py` | 16950 | `0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68` |
| `geometry_20261114_twelve_query_projection_warm.py` | 15035 | `10ed25405930f3775d8fb88f007aa50be4a53f4b3421904be959f1890ed67477` |
| `geometry_20261114_twelve_query_projection_response.py` | 3367 | `1989a8a9925c6e606d39451b1625b49de7b33d048061e69668162895642d4783` |

The first call consumes these two original request37 files together:

| Original request37 file | SHA256 |
|---|---|
| `eleven-query-warm/warm-001.json.gz` | `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8` |
| `eleven-query-warm/driver-status.json` | `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0` |

The parent status must identify that same completed progressed warm,
and its complete identity must agree with the warm producer. The
entire original `resume_producer` subtree is preserved. The current
source ledger adds these three mathematical implementation sources
(operator, fixed-support helper and warm entry) to the existing
twenty-four-source parent ledger. None of the frozen eleven-query,
earlier operator, original solver, or actual request37 files is edited.

The wrapper retains the original accepted96, prepared699, truezero112
and config112 byte locks. Its first parent is the actual37 eleven-query
schema, while later calls may consume a genuinely produced warm of this
new schema with its own paired status and all current source hashes.
No prepared field is relabeled as an accepted parent.

## 2. Complete B and its typed query inputs

The typed query order is:

| Kind | Original interval indices | Original query rule |
|---|---|---|
| left RMS | 470, 471, 472, 473, 475, 477, 479, 480, 481 | fraction `0.17267316464601146` in that actual interval |
| collocation midpoint | 473, 475, 477 | original returned `state.middle` and `problem.mid` |

Every query retains all 2048 original physical-phi angles. There are
24576 rows in the complete operator and 236036 columns in the original
scaled exact-coordinate space. The endpoint capture uses the same
unique full A construction; its nine distinct intervals contain
thirteen physical nodes470–482. The full B local-column union has
4397 coordinates: thirteen times338 physical coefficients plus three
global controls. These are dimension counts of the new interface;
actual shapes and identities must still be measured in Actions.

The twelve-query operator is an independent copy of the frozen eleven
implementation with the declared left interval list, source origin and
schema updated. Original typed rows, full-coordinate scatter actions,
source bindings, direct midpoint inputs and endpoint-J/P chains are
preserved. The midpoint derivative is still

$$
\delta Y_{\rm mid}
=\frac{\delta Y_L+\delta Y_R}{2}
 +\frac h8(\delta f_L-\delta f_R),
$$

with the full original physical and global-control derivatives in
both endpoint RHS variations. The beta derivative also retains the
direct scalar-control term at the query. There is no second full
Jacobian construction and no substituted RMS fraction for a midpoint.

In particular the new left-RMS470 block contains the physical node470
column block. That column remains in full B verification, the complete
matvec/rmatvec, original B exports and all selected-direction slacks.
Restricting a correction below does not trim the mathematical domain
derivative.

## 3. Fixed correction support and the necessary outside offset

Let z0 denote the complete original raw LSMR direction in the original
scaled-z coordinates. Let B be the complete derivative of the selected
beta-squared values at this model's actual base field. As in the
original projection engine, theta is one half and

$$
c=(1-\theta)\beta^2>0,
\qquad c+Bz\ge0
$$

is an algorithmic linear reserve. It is not a new scientific tolerance
or a guarantee of nonlinear domain membership.

Let S be the 4059 coordinates comprising physical nodes471–482 and all
three global controls. Free inlet-core columns are not correction
columns. Write E_S and E_O for the coordinate injections on S and its
complement. The local projection candidate has the form

$$
z=E_S z_S+E_O(z0)_O.
$$

Consequently its complete inequalities are exactly

$$
B_S z_S+c+B_O(z0)_O\ge0.
$$

The helper forms the full outside vector by copying z0 and setting its
S coordinates to zero, then calls the complete original B matvec:

$$
d=B(E_O(z0)_O),\qquad c_{\rm eff}=c+d.
$$

This operation retains all outside contributions, including node470.
No outside direction is silently removed and no corresponding row
offset is silently set to zero. The complete original c remains
positive as required by the original engine. The effective local
offset c_eff is allowed to be negative; it has no positivity gate.

Let C_S be the original positive diagonal column preconditioner
restricted to S. With x=C_S z_S and x0=C_S(z0)_S, the local problem is

$$
\min_x\frac12\|x-x0\|_2^2,
\qquad B_S C_S^{-1}x\ge-c_{\rm eff}.
$$

This is a weighted projection around the actual raw direction. It is
not minimization of the complete damped quadratic from R265. C is the
original unprojected regularized column scale; it is not relabeled as
a new exact projected-Hessian factor.

For each nonzero computed row a_i of B_S C_S inverse, set

$$
\widehat a_i=a_i/\|a_i\|_2,
\qquad \ell_i=-(c_{\rm eff})_i/\|a_i\|_2.
$$

The retained cyclic Hildreth update is

$$
\mu_i^{\rm new}
=\max\!\left(0,\mu_i+
 \frac{\ell_i-\widehat a_i x}{\|\widehat a_i\|_2^2}\right),
\qquad
x\leftarrow x+(\mu_i^{\rm new}-\mu_i)\widehat a_i^{\mathsf T}.
$$

Rows are compiled once by query block. Shared physical nodes and the
global controls use the original scatter updates. There are no
24576-by236036 dense arrays and no repeated Gamma/J multiplication
inside the sweep. The original budget of200 sweeps is retained.

The restricted halfspace set is not assumed feasible. A computed
binary64 zero row with a negative effective offset is reported as an
infeasible row of that assembled floating subproblem. Division
underflow is not excluded, so this is not an exact-real infeasibility
certificate. Such a diagnostic does not reject the original nonlinear
problem or bypass the full later checks. A finite incomplete local
iterate may still be useful to the original global radial repair. If
local normalization or the iterative coordinates become unrepresentable,
the helper explicitly returns the complete original raw direction,
records a failed local projection and leaves the original global
backup and real trial machinery in charge. Arbitrary programming
exceptions are not swallowed as projection success.

The helper reports the original unnormalized full slack, local
stationarity and complementarity, normalized and original-row
multipliers, all complete outside offsets and the raw/candidate offset
reconstruction differences. Those multipliers belong only to this
restricted projection problem; they are not complete-model R265 KKT
multipliers. The final authoritative slack is always a fresh full B
action on the entire candidate. The reconstruction comparisons are
diagnostics rather than additional acceptance conditions.

## 4. Whole-vector repair and the actual direction used in trials

Before the original global repair, the helper writes only the S
coordinates back to a copy of z0. It checks and records byte identity
outside S at that stage. This statement is deliberately limited to the
local candidate.

The unchanged original selection then retains both the corrected
candidate and the original raw-ray backup. Its global radial repair
acts on every coordinate of a vector v. For the original positive c,
set

$$
\rho=\max_i\frac{[-(c+Bv)_i]_+}{c_i},\qquad
t=\frac1{1+\rho}.
$$

Since c+Bv is at least minus rho times c componentwise, in exact
arithmetic

$$
c+B(tv)=(1-t)c+t(c+Bv)\ge0.
$$

The original implementation still recomputes the complete floating
slacks. The repair may scale node470 and all other outside raw
coordinates. The later same-model segment between feasible candidates
may scale them again. Therefore the final trial direction does not
claim to preserve the outside raw direction unchanged.

The unchanged selector uses the same complete damped quadratic

$$
f(z)=\tfrac12\|b+Az\|_2^2+\tfrac12\lambda^2\|z\|_2^2,
\qquad\lambda=270,
$$

for its original backup and feasible-segment comparison. It reports
actual complete A actions, the true merit derivative, modeled decrease
and all full B slacks after the final combination. The selected scaled
direction is converted to coefficient coordinates by dividing by the
original chart scale exactly once. The local C metric does not become
another chart scale and is not applied again to that direction.

All seventeen original actual trial evaluations remain. Their complete
nodes, actual collocation midpoints, both original RMS query sets,
rho checks and fixed-model merit remain authoritative. A modeled
linear reserve alone cannot pass them, as the larger actual37 trials
already demonstrate. The read-only original midpoint observer is
retained: it observes the same returned middle states and never
recomputes the full flow, changes original flags, or inserts a new
scientific gate.

## 5. Exact Actions invocation and preserved outputs

Run from this topic's `computations` directory after restoring the
original inputs and the two actual37 parent files. All scientific
calculation is in the public repository's own Actions.

```bash
python geometry_20261114_twelve_query_projection_warm.py \
  --accepted "$ACCEPTED96" \
  --prepared "$PREPARED699" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --resume "$ACTUAL37/eleven-query-warm/warm-001.json.gz" \
  --expected-resume-sha dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8 \
  --parent-status "$ACTUAL37/eleven-query-warm/driver-status.json" \
  --expected-parent-status-sha 37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0 \
  --out "$VISIBLE_OUT/twelve-query-warm" \
  --iterations 1 --lsmr-iterations 200 --damping 270 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200
```

If that call produces a real progressed warm, run the fresh response:

```bash
python geometry_20261114_twelve_query_projection_response.py \
  --accepted "$ACCEPTED96" \
  --prepared "$VISIBLE_OUT/twelve-query-warm/warm-001.json.gz" \
  --tail-anchor "$TRUE_ZERO112" \
  --tail-config "$CONFIG112" \
  --out "$VISIBLE_OUT/physical-response"
```

The output preserves complete typed B/Gamma/Pi rows, original base
states and endpoint factors, raw LSMR and selected directions, outside
offsets and local coordinates, projection history, all actual trial
readouts, original observer bytes, new warm and paired status. The
new FD binds the actual new warm and complete producer, reruns all
original directions, centered steps and Richardson comparisons, and
keeps the `5e-5` implementation threshold. It does not relabel an old
FD pass or call a new nonlinear native tail. Every saved warm still
declares false full-BVP and closed-surface acceptance.

The original engine supports one model per call. A later genuinely
produced twelve-query warm and its paired status can be consumed by
the same frozen entry in a separate output directory, with their
actual hashes. Each model refreshes and then fixes its own weights;
merits from distinct models cannot be subtracted as though those
weights were unchanged. No such later sequence has been executed by
this interface, and no extra numerical budget is implicitly granted.

## 6. Extension hook for a separately declared full-H candidate

The warm entry exposes `engine=observed.engine`, `domain` and `support`.
At entry it sets `engine.local_halfspace_projection` to
`support.fixed_support_projection`; it does not wrap the original
`choose_feasible_descent`. A separate caller that needs to capture the
actual C diagonal must therefore wrap the support function before this
main call, rather than only setting the engine slot earlier and having
that assignment overwritten. The entry saves and restores all its
patched engine attributes on exit.

The fixed-support statement describes the baseline C projection. A
separately declared global full-H candidate may use all236036 original
coordinates. Such a caller must distinguish those candidate scopes,
retain the complete B and original same-model comparison, and report
which actual candidate is used. This interface does not assert that
such a full-H extension has run, improved the direction, or passed any
new nonlinear native solve.
