# Positive spectral Gram QP with the physical-H² norm

Date: 2026-11-20 UTC. This note describes the new executed v6 coarse solver
[`resume_20261120_curvature_qp_v6_spectral.py`](../scripts/resume_20261120_curvature_qp_v6_spectral.py).
It consumes the independently checked exact block module
[`positive_spectral_gram_weights.py`](../scripts/resume_20261120/positive_spectral_gram_weights.py)
and [R660](../results/R660-positive-spectral-Gram-blocks-and-maximum-control.md).
The fixed surface model and metric are unchanged. The optimization objective
is explicitly changed from the previous weighted quadratic Gram sum to the
smoothed positive spectral objective below.

## 1. All rows and the true objective

At each original observed point, let

$$
E=\begin{pmatrix}e&f\\ f&g\end{pmatrix}
 =\begin{pmatrix}|F_s|^2-1&\langle F_s,F_\phi\rangle/(a\rho)\\
 \langle F_s,F_\phi\rangle/(a\rho)&|F_\phi|^2/(a\rho)^2-1\end{pmatrix}.
$$

The radial weights are the same strictly positive half-Simpson, half-Gauss
mixture on all 7,377 observation stages. Quarter-angle multiplicities are
2 at the two endpoints and 4 inside; their sum is the full N=2048. Write
C0=(sum of radial weights)·2048=4856.422137302683 and let omega be the product
of radial weight and angular multiplicity divided by C0. Thus all omega are
positive and sum to one.

The declared fixed parameters are p=8, k=p/2=4, epsilon=0.001 and c=0.05.
The true acceptance objective is

$$
\Phi(F)=\sum_{s,\phi}\omega_{s,\phi}
 \operatorname{tr}\left[\left(\frac{E(F)^2+\epsilon^2 I}{c^2}\right)^k\right].
$$

Neither epsilon nor c changes inside a direction or its line search. The old
Jw=sum w_s m_phi·(e²+2f²+g²), its mean, legacy/all raw sums, maximum Gram
operator norm, determinant, and geometry screen are still read for every
trial. Jw is a diagnostic in this version and may increase while Phi falls.
Changing this objective is not claimed to be equivalent to minimizing Jw.
Every original scalar and mixed Gram equation is still present with positive
weight; no physical row, angular mode in the field, or endpoint condition is
deleted.

## 2. Exact positive residual block and gradient units

Freeze at the current actual field E0 and define

$$
W=\left((E_0^2+\epsilon^2 I)/c^2\right)^{k-1}
  =\begin{pmatrix}u&v\\v&w\end{pmatrix},\qquad
K=\begin{pmatrix}u&v&0\\v&u+w&v\\0&v&w\end{pmatrix}.
$$

For the original raw three-vector r=(e,f,g),

$$
r^T K r=\operatorname{tr}(W E^2).
$$

The off-diagonal Frobenius factor is already inside K: **no additional
sqrt(2) is applied**. Since W is positive definite,

$$
r^TKr\ge (\epsilon^2/c^2)^{k-1}(e^2+2f^2+g^2)>0
$$

for nonzero r. The analytic eigenweight floor here is 6.4e-11. This is a
strictly positive objective, not truncation of small residual blocks.

Because W commutes with E0, differentiating the true matrix polynomial gives

$$
d\Phi=\frac{2k}{c^2 C_0}\sum w_s m_\phi\,r^TK\,dr.
$$

With J the original raw residual derivative restricted to the existing
physical coarse columns, form

$$
H_K=\sum w_sm_\phi J^T K J,\qquad
 g_K=\sum w_sm_\phi J^T K r.
$$

The v6 source returns N=(k/c²)H_K and g=(k/c²)g_K. Both are multiplied by
k/c²=1600, not only the gradient. The actual Phi gradient is 2g/C0. The
positive local data model is

$$
\Phi_0+2g^T\alpha/C_0+\alpha^TN\alpha/C_0.
$$

N is a positive frozen-weight approximation; it is not the exact nonlinear
Hessian. For p>2, that frozen model is not an MM upper bound. Every accepted
trial must decrease the independently reevaluated true Phi. The recorded
model decrease at step length t is

$$
(-2t g^T\alpha-t^2\alpha^TN\alpha)/C_0,
$$

excluding the step penalty. The trust update uses actual Phi decrease over
this prediction, not old Jw decrease over a differently scaled model.

## 3. Exact separated assembly without large Jacobian columns

The physical basis has radial position factors Y_b(s), velocity U_b(s),
and acceleration A_b(s), including the actual physical height column. Its
angular channels h_c(phi), with actual rotating-frame derivatives h'_c,
are unchanged from the executed three-jet construction. For V=F_s,
d=F_phi, and ar=a·rho, define angular residual-column families

$$
\mathcal A_c=(2V\cdot h_c,\ d\cdot h_c/ar,\ 0),\qquad
\mathcal B_c=(0,\ V\cdot h'_c/ar,\ 2d\cdot h'_c/ar^2).
$$

The exact column for pair (b,c) is U_b A_c+Y_b B_c. At each stage v6 passes
all 76 angular-family columns (38 A and 38 B) to the checked block module,
using angular multiplicities exactly once. It then assembles the radial
outer products using the returned four channel moment blocks and the two
gradient blocks. Radial weights are included exactly once. This gives the
same 1,964-column H_K and g_K as forming every full physical Jacobian column;
it does not approximate or subsample the residual objective.

A new one-direction probe compares this assembly against the original
complete operator Jv and the complex derivative of the polynomial Phi. It
checks both the positive quadratic and the true gradient units. The old
scalar oracle, original derivative, fixed core, and affine-port checks are
not redefined by the new module.

## 4. Physical norm, initial damping, and constraints

The exact positive coefficient norm G is unchanged from
[the v5 construction](2026-11-20-curvature-qp-physical-h2-first-result.md):

$$
\alpha^TG\alpha=
 \|\operatorname{DoubleIntegrated}^{-1}(A_{height}^{-1}B\alpha)/scale\|^2.
$$

It is an integrated coordinate step norm, not a claim of exact geometric
bending energy. Let R satisfy RᵀGR=I. In alpha=Rz variables, v6 solves the
same finite linear curvature-constrained QP with positive matrix

$$
C_{data}=R^TNR/C_0,\qquad C=C_{data}+\mu^2I.
$$

The first p8 batch declares the initial relative damping rule

$$
\mu_0^2=10^{-3}\operatorname{tr}(C_{data,0})/1964.
$$

Only the initial current parent determines that scale. Subsequent directions
use the existing actual-step trust update: reject multiplies mu by 10;
accepted alpha<1/4 or model ratio<1/4 multiplies mu by four; a full accepted
step with model ratio>3/4 halves mu; otherwise it is retained. The raw and
mean conventions, actual initial trace and mu, and subsequent values are
recorded. An explicitly supplied fixed `--damping` is a separate CLI option.
No claim is made that the numerical mu value is comparable to old diagonal
Gram damping or to an unnormalized p8 weight.

The complete finite screen remains 0.03·D_lb·max|kappa|≤0.992, with actual
current principal branches and D points, plus positive sampled determinant.
The 0.0002 linear margin, general halfspace repair including negative bounds,
protected basins, and per-direction pins are unchanged. The halfspace model
is accepted only after the actual nonlinear Phi and geometry checks.
The 0.992 constant is an algorithmic margin, not a proof of global reach or
a replacement for the README's 0.03 reach ratio.

## 5. Immutable paid geometry locations

The complete small generator
[`resume_20261120_export_curvature_history_manifest.py`](../scripts/resume_20261120_export_curvature_history_manifest.py)
collects locations from initial/final memories, every actual direction pin
and constraint, accepted and rejected trial maxima, and local searches. It
discards old values. Its first actual export for the 0241 parent has 377
curvature locations, 54 radius locations, and 7 protected optimizer seeds.
All are reread at descendants. Active linear rows may remain bounded while
fixed-point nonlinear screening keeps these locations.

In v6 every newly observed curvature/radius witness is also added to the
persistent fixed list. A limited active memory can therefore no longer
silently discard a paid nonlinear witness. This does not turn a finite
location list into continuous coverage, and local optimizer convergence is
not used as a global-bound claim.

## 6. Meaning of finite spectral control

Let M be the maximum absolute eigenvalue over this finite observation set
and omega_min the least positive normalized orbit weight. Then

$$
\max\{0,c^2(\Phi/2)^{1/k}-\epsilon^2\}\le M^2
 \le\max\{0,c^2(\Phi/\omega_{min})^{1/k}-\epsilon^2\}.
$$

These inequalities follow respectively by bounding both eigenvalues by M
and keeping the one summand that attains M. They concern only the finite
set. The reported floating evaluations are not outward intervals and give
no continuous metric, immersion, embedding or reach certificate. Actual
maximum Gram values remain explicit outputs rather than being replaced by
these often loose finite inequalities.

## 7. Frozen source identities and current starting field

| Item | SHA-256 |
|---|---|
| v6 solver, 48,485 bytes | 1872298863d3d0309c74a35f4f93bdf1373528c5e28d3cfd0e6c4545f3be0ea0 |
| Spectral block module | e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91 |
| History-location generator, 5,459 bytes | f2d7cda73b0b5634a869cb0971c811b24af00e540eff8e62ca6741aba762866f |
| Actual 0241 input bundle | 0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023 |
| Immutable 0241 history manifest | b00981e15137d35846a1c7c71acc58d533478ef51ca531b810853efc44fe3698 |

The starting Phi is 2.0068202402652498e-6, old Jw is
0.13368399851982452, and sampled max Gram is 0.024013578471355768.
After rereading the expanded immutable list, the starting known-point
product is 0.9918941656379898. The source is a new version; the executed v5
file and its earlier results were not overwritten. The complete actual CLI,
paid trial budget, final state, and numerical probe outputs belong to the
separate p8 result note. This formula note itself makes no completion claim.

