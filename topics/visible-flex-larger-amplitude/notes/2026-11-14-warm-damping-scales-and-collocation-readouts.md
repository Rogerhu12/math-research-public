# Warm damping, coordinate scales, and the saved collocation readouts

This is a source interpretation using the frozen optimizer and the
already executed request39/40 reports. No ODE, residual vector,
matrix action, norm, SVD, optimization step or new numerical
experiment was evaluated for this note.

The precise conclusion is that lambda270 and the coordinate/row
scales define the optimization step and merit. They do not change
the original collocation equations, the physical boundary formula,
or the formula for the material metric. A decrease in the saved
weighted sum of squares does not require a comparable decrease in
the separately printed unweighted maximum collocation component.
The current reports do not locate that maximum component.

## 1. The original residual and exact coordinates

The frozen implementation is
[`geometry_20261114_constrained_collocation.py`](../computations/geometry_20261114_constrained_collocation.py),
SHA256
`70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8`.
[R256](../results/R256-exact-constraint-collocation-and-damped-descent.md)
establishes the exact-coordinate reduction. The current finite
problem has338 physical entries at each of699 nodes,109 free inlet
core coefficients and3 global scalar controls. Its reduced
dimension is236036.

For a coordinate vector q, `ExactCoordinates.expand` sets all core
and scalar-control rows constant across nodes and enforces the full
left endpoint relation. The inlet radial/core coefficient variation
dc_j also produces inlet tangential variation

$$
dt_j=-2j\,dc_j.
$$

The fixed first three core coefficients, inlet r0 and inlet height
conditions are retained. These constraints are identities of the
chart; they are not softly penalized residual rows.

`CompleteResidual.evaluate` computes the actual nodal RHS, actual
Hermite midpoint, midpoint RHS and original collocation defect:

$$
y_{i+1/2}=\frac{y_i+y_{i+1}}2
 -\frac{h_i}{8}(f_{i+1}-f_i),
$$

$$
C_i=y_{i+1}-y_i-rac{h_i}{6}
 (f_i+f_{i+1}+4f_{i+1/2}).
$$

The reduced residual R(q) contains all338 physical components of
every C_i, followed by all112 right-boundary rows. It deletes no
physical Fourier frequency. At present the warm path uses the
explicitly affine actual zero-T112 DN map in that right boundary;
it does not claim that the new warm's nonzero height has a solved
nonlinear tail.

## 2. The diagonal S is a step penalty and an invertible scale

Let k_j=2j. The positive diagonal `chart.scale`, denoted S, assigns
the following physical-coordinate weights at each noninitial node:

| Coordinate | S entry |
|---|---|
| Radial mean r0 | 1 |
| Radial mode $r_j$ | $(1+k_j)^2$ |
| Tangential mode $t_j$ | $(1+k_j)^2$ |
| Full height mean z0 | 1 |
| Height mode $z_j$ | $1+k_j^2$ |

The free inlet core coordinate has the pullback weight

$$
S_{c_j}=\sqrt{S_{r_j}^2+k_j^2S_{t_j}^2}.
$$

This includes both inlet dr_j=dc_j and dt_j=-k_j dc_j. In
particular its large-frequency growth includes the tangential
cubic-frequency cost. Treating the free-core scale as just the
radial quadratic-frequency weight would omit part of this chosen
algorithmic penalty.

Each control's scale is at least1 and otherwise the largest saved
sample magnitude among its scalar0/1/2 derivatives. Samples include
the profile knots and33 evenly spaced points on each control bump.
This is the actual optimization definition, not a certified maximum
over a continuous support interval. In the request40 coordinate
description the minimum and maximum S entries are1 and
`11340113.00166912`.

The original physical coordinate step is

$$
\delta q=S^{-1}z.
$$

All entries of S are positive, so this scaling removes no
coordinate direction. It changes the meaning of a Euclidean step
penalty in z. It is not a certified geometric C2 norm, a reach
bound, a metric modification, or a Fourier-tail estimate.

## 3. Row weights and the role of lambda270

At the beginning of each model, the physical residual row weight is

$$
(W_r)_{i,a}=\frac{1}{h_i(1+|f_{i+1/2,a}(q_0)|)}.
$$

Every right-boundary row has weight100000. These weights are fixed
at q0 during the model and every actual trial. They are refreshed
when a new model starts from a new saved warm. The physical weight
removes the integrated h scale and uses the componentwise midpoint
RHS magnitude; it resembles a relative ODE-defect scale but is not
the original solver's complete Lobatto RMS estimator.

For the actual model define

$$
b=W_rR(q_0),\qquad A=W_rJ(q_0)S^{-1}.
$$

The regularized quadratic is

$$
f(z)=\frac12\|b+Az\|_2^2+rac{\lambda^2}{2}\|z\|_2^2,
\qquad \lambda=270.
$$

Equivalently, in the original coordinate increment it is

$$
\frac12\|W_r(R(q_0)+J(q_0)\delta q)\|_2^2
+\frac{\lambda^2}{2}\|S\delta q\|_2^2.
$$

Lambda270 therefore controls a positive penalty on the proposed
step. Its square multiplies that penalty. It is not added to the
physical ODE, to the right-boundary residual, or to the scalar
profile a(s;p). The profile still determines the material metric
through its actual current p values. The optimizer may choose a
different p as part of a design step, but lambda is not a fourth
geometric design control and does not enter the metric formula.

The optional original LSMR column diagonal is a separate object:

$$
C_{jj}=\sqrt{\|A e_j\|_2^2+\lambda^2}.
$$

The frozen `regularized_operator` applies $[A;\lambda I]C^{-1}$,
recovers z by division by C, and passes `damp=0` to LSMR. Thus the
column preconditioner does not replace the physical step scale S,
and it does not change the intended lambda-squared penalty. In
request40 the complete QR used its `none` column-preconditioner
option; the baseline C projection retained its own original C
metric and fixed correction support. These are explicitly separate
roles in [R268](../results/R268-complete-regularized-chain-border-QR.md).

Although lambda is an algorithm parameter, the current frozen
[`full_angle_projection_warm` entry](../computations/geometry_20261114_full_angle_projection_warm.py)
hard-checks that its CLI value is270. Changing this value is not a
currently supported invocation of that frozen experiment. A future
algorithmic change would need its own explicit source identity and
actual execution; there is no reason to change a scientific
tolerance to permit it.

## 4. The actual trial merit contains no damping penalty

The trial is q0+alpha S^{-1}z. Its actual merit is

$$
\mathcal M_{q_0}(q)=\frac12\|W_r(q_0)R(q)\|_2^2.
$$

The damping penalty is used in selecting a direction, but is absent
from the actual nonlinear merit. The source explicitly records
`damping_penalty_not_in_actual_merit=True`. Its prediction uses

$$
-\alpha b^TAz-\frac{\alpha^2}{2}\|Az\|_2^2.
$$

Every finite trial recomputes the physical RHS and boundary. A
strict actual merit decrease and the original ratio test are
required; the accepted trial is then checked at both original RMS
query grids. Those checks establish that the queried RHS remains
in its domain. They do not assert that the original final solver's
RMS residual is below1e-6. The current warm has explicitly false
full-BVP acceptance flags.

The complete solver's later original augmented and frozen-physical
RMS gates, its1e-11 right-boundary gate, and fresh true-native audit
remain distinct. No value of the optimization damping can declare
those gates passed.

## 5. Why the two printed progress measures need not move together

`physical_collocation_max` is implemented as
`max(abs(col[:, :flow.n]))`. It is the unweighted maximum absolute
entry of the integrated collocation array. It is not divided by h
or by1+abs(fmid), does not include the boundary rows, and is not a
reported metric tensor defect or the final relative RMS residual.

The actual model merit instead sums squares of all weighted
physical rows and all weighted boundary rows. Decreasing this sum
does not force a proportional change in its largest unweighted
physical entry. A step can reduce many other weighted components
while leaving the unweighted maximum nearly unchanged. This is a
property of the defined measurements; it does not identify which
components changed in the actual run.

The controlled same-parent request39/40 readouts are:

| Saved quantity | Request39 C step | Request40 selected H step |
|---|---:|---:|
| Current-model merit before | `44.292419650985686` | `44.292419650985686` |
| Actual merit after | `44.29019103902422` | `44.28040624161529` |
| Recorded actual merit decrease | `0.0022286119614634003` | `0.012013409370396744` |
| Physical collocation maximum before | `0.007110320785400957` | `0.007110320785400957` |
| Physical collocation maximum after | `0.007110317266439588` | `0.0071103080271700675` |
| Complete boundary maximum after | `8.053357926995966e-8` | `7.997334910447051e-8` |

The request40 direction first passed through the full-vector radial
factor `0.00959007921159372`. The saved final scaled direction norm
was `2.744173569251269e-5`, and its largest original-coordinate
component was `1.710782559494892e-6`. Its alpha1 therefore does not
describe an unscaled Newton step. This small repaired step and the
two different measurements are consistent with the observed
progress. They are not a proof that damping alone caused the
remaining maximum or that a different damping would solve it.

One additional distinction follows algebraically from the existing
readouts. At the current-model base, the entire boundary maximum is
below8.1e-8, and there are112 right rows of weight1e5. Hence their
contribution to the mathematical merit has the upper bound

$$
\mathcal M_{\rm right}(q_0)
\le\frac{112}{2}(10^5\,8.1\,10^{-8})^2
=0.00367416.
$$

The right contribution at the trial is nonnegative. The saved total
decrease0.012013409370396744 is larger than this entire initial
right-block bound. Interpreting the recorded sums through their
defining algebra, the decrease cannot consist solely of boundary
improvement: the physical weighted aggregate also decreases. This
argument uses a loose scalar upper bound, not a newly evaluated
vector or dot product. It is an algebraic interpretation of the
ordinary floating readouts, not a validated floating-error
certificate. It still says nothing about the location or relative
change of the unweighted maximum component.

## 6. The saved records do not locate the maximum

The current evaluator computes only the physical maximum value,
not its `argmax`, cell, Fourier component or sign. Although the
returned in-process state contains the complete collocation array,
the warm writer saves the complete y and nodal RHS plus summary
maxima; it does not save the entire midpoint RHS or collocation
array. The domain operator retains selected original midpoint
inputs, not all698 midpoint RHS vectors. The full-H archive saves
directions, original A/B actions and model evidence, which do not
substitute for the actual full nonlinear collocation vector at the
trial.

The read-only midpoint observer also preserves only the residual
vector identity, not all its numeric entries, unless its separate
bad-domain diagnostics apply. No bad midpoint was observed in
request40. Consequently the existing records do not justify
claiming that the maximum0.0071103 occurs at interval470,473, a
particular high Fourier mode, or the final bridge. Those positions
have appeared in domain constraints or prior solver failures; they
are not saved locations of this current maximum.

No such location was reconstructed locally. If later decisions
require it, the original evaluator already has the exact actual
collocation array in memory, so an explicitly declared read-only
observer could record its location and selected per-component
values without another RHS or Jacobian evaluation. That would be
a new output identity, not a reason to relabel the current reports
or to change a scientific acceptance gate. No such code or
experiment is introduced here.

## 7. Implication for the currently selected next step

The available evidence supports the already specified increase
from16 to32 working inequality rows through the same frozen QR
entry. Request40 reached its working-row budget with an accurate
unrepaired full-model stationarity residual but1804 violated full
inequality rows; radial repair then substantially scaled the
direction. This is a measured limitation. The present reports do
not isolate lambda270, a particular component weight, or a
particular maximum-residual cell as the cause of slow maximum-norm
progress.

Keep the new model's actual weights explicit, read its complete
slacks and true trial results, and retain all original final
acceptance gates. The authoritative actual values and saved-byte
ledger are in
[the request40 note](2026-11-14-actual-request40-complete-QR-H-working-row-limit.md).
No scientific source was modified for this analysis.
