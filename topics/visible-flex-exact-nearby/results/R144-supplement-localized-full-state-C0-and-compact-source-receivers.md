# R144 supplement: localized full-state geometry norm and compact-centre source bounds

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

This note defines a new whole-domain consumer for the now certified
compact-density mean centre. The consumer uses the actual parameter
radius and uniform mean ball from
[TM](R144-supplement-terminal-mean-small-ball-controls-normalized-forward-constant.md)
and its
[complete public result](../notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/terminal-mean-small-scalar-gate.json).
It does not repeat the old mean receivers, compact moments, terminal
fixed-point gates, or forward retraction targets.

The primary geometry norm is the complete, unnormalized moving-state
norm at the **same moving angle** used in
[C.1](R133-supplement-complete-C0-state-and-nu-geometry-response.md).
A comparison at the same physical angle is a different possible output.
It is not an extra premise of that geometry theorem.

## LC1. Exact centre, actual radii, and full finite carriers

Fix the original candidate

`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`

at the exact original parameters

$$
 \alpha={6890507429876859\over9007199254740992},\qquad
 \nu_0={-2572625729470897\over72057594037927936},\qquad
 \eta_0={-7789843107295549\over4611686018427387904}.
\tag{LC.1}
$$

Its exact finite definition has 6144 cubic radial pieces and all
32 nonconstant sine/cosine modes, of physical frequencies
$4,8,\ldots,128$. Write

$$
 u=\sum_{k=1}^{32} b_k(r)\sin(4k\phi),\qquad
 w=v-m=\sum_{k=1}^{32} a_k(r)\cos(4k\phi),\qquad
 m=\langle v\rangle<0 .
\tag{LC.2}
$$

Both $a_k$ and $b_k$ include the actual multiplier $\alpha$ exactly
once. They are cubic PPoly coefficients, not interpolated samples.
The radial intrinsic baseline cancels out of $w$.

Use the original complete scalar-mean container

`e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b`.

Its 7721 closed rows refine all 6144 candidate pieces and have all
6143 actual mean interfaces. The intrinsic whole affine box is used
only as an enclosure of its exact original centre $\eta_0$.
No result about all nearby $\eta$ is inferred.

The full saved TM result provides exact rational $\rho,b$ and proves,
for every $|\xi|\le\rho$, a unique terminal mean $m_\xi=m+h_\xi$
satisfying $|h_\xi|\le b$. It also proves the unique compact root
$\xi_*$ in this interval, the negative mean and positive density.
Put

$$
 \chi=4096t^6(1-t)^6,\quad
 t={r-1/20\over13/100},\quad
 I=[1/20,9/50],
\qquad
 e=\xi\chi,\quad\lambda=1+e,\quad
 j_\xi=1+\lambda w/m .
\tag{LC.3}
$$

Here $\chi=0$ off $I$. The new moving state is exactly

$$
 u_\xi=u,\qquad v_\xi=m_\xi j_\xi .
\tag{LC.4}
$$

The parameter $\xi$ changes this density, not the fixed metric.
The completed TM result is read with every original whole decimal
ball and its execution identity; no displayed midpoint is a radius.

## LC2. The correct localized geometry norm

The complete state difference at the same moving angle is

$$
 u_\xi-u=0,\qquad
 v_\xi-v=h_\xi j_\xi+e w .
\tag{LC.5}
$$

Let one original closed radial row have valid bounds

$$
 |m|\ge M_->0,\quad |m|\le M_+,\quad
 \chi\le X,\quad
 \|u\|_{A_0}\le U_A,\quad \|w\|_{A_0}\le W_A .
$$

The two finite bounds are computed from the full cubic carriers:

$$
 U_A=\sum_{k=1}^{32}\sup_{\rm row}|b_k(r)|,\qquad
 W_A=\sum_{k=1}^{32}\sup_{\rm row}|a_k(r)|.
\tag{LC.6}
$$

Horner evaluation on the entire exact closed row supplies these
suprema. All coefficients are retained. A finite-centre definition
has no discarded Fourier tail; it supplies no truncation principle
for an unknown infinite-dimensional correction.

Define

$$
 J_+=1+(1+\rho X){W_A\over M_-},\qquad
 E_\phi=bJ_++\rho XW_A .
\tag{LC.7}
$$

Then the whole row, all angles and all $|\xi|\le\rho$ satisfy

$$
 \max\bigl(|u_\xi-u|,\ |v_\xi-v|\bigr)\le E_\phi.
\tag{LC.8}
$$

Taking the maximum over all 7721 rows gives the exact kind of
$C^0_{r,\phi}$ upper bound in the original geometry comparison.
Outside $I$, $X=0$, so the full mean contribution $bJ_+$ remains.
It is not valid to set the new state difference to zero there.

This uses the local full finite Fourier carrier rather than
$8\sqrt{V_*}$ from a separately maximized whole-domain variance.
The earlier complete TM sufficient bound is retained with its
original false gate; this new target evaluates a different,
localized receiver with necessary original coefficient input.

A successful $E_{\phi,*}\le10^{-4}$ gate places the new centre in
that **state** ball. A future exact GC correction about this centre
must still be added to $E_{\phi,*}$. The gate alone supplies neither
a GC solution nor the complete closed immersion in the geometric
conditional theorem.

## LC3. Sharper versions of the five complete CS receivers

Use the exact identities in
[CS](R144-supplement-compact-centre-ordinary-and-divergence-residual.md).
On each row read the old full scalar enclosures

$$
 U=\langle u^2\rangle,\qquad V=\langle w^2\rangle,\qquad
 Z={\sqrt V\over|m|},\qquad \kappa=Km^2,
$$

and $|\beta|,\gamma,|K|$. All angular $L^2$ norms use normalized
angular measure and all radial norms use the actual $dr$.

Set the valid upper functions

$$
 \widehat U_A=\min(U_A,8\sqrt U),\qquad
 \widehat Z_A=\min(W_A/|m|,8Z),\qquad E=\rho X,
$$

where interval implementation uses positive lower endpoints for
denominators and complete upper endpoints for the two minima.
Write

$$
 \begin{aligned}
 M_b&=|m|+b,\\
 K_\Delta&=|K|b(2|m|+b),\qquad K_b=|K|M_b^2,\\
 A_+&=K_\Delta+K_bE,\qquad
 B_+=K_\Delta+K_b(2E+E^2),\\
 T&={(2A_++B_+\widehat Z_A)Z\over4},\\
 D&={|\beta|\over4}
       \left[\widehat U_A\sqrt U+
                |\kappa|(2+\widehat Z_A)Z\right].
 \end{aligned}
\tag{LC.9}
$$

These are the same complete CS estimates with finite angular
$A_0$ bounds inserted before taking radial suprema. For example,
$\|u^2-U\|_2\le\|u\|_\infty\sqrt U
\le\widehat U_A\sqrt U$, and
$\|\mathcal I(z^2)\|_2\le\widehat Z_A Z/4$.
No mean term is removed except by the exact primitive identity in CS.

The five new whole receiver quantities are obtained from

$$
 \begin{aligned}
 f_u&=|\beta|(K_\Delta+B_+Z^2)\sqrt U,\\
 q_u&=|\beta|\widehat U_A T+\gamma A_+ Z,\\
 c_v&=(1+b/|m|)(1+E)\sqrt{1+Z^2},\\
 f_{v,\chi}&=M_b\rho|\chi'|Z,\\
 q_v&=M_b\left[E(D+\gamma\sqrt U)
                  +|\beta|(1+(1+E)\widehat Z_A)T\right].
 \end{aligned}
\tag{LC.10}
$$

Their complete outputs are

$$
 F_{u,+}=\|f_u\|_{L^2_r},\quad Q_{u,+}=\|q_u\|_{L^2_r},
 \quad C_{v,+}=\|c_v\|_\infty,\quad
 F_{v,\chi,+}=\|f_{v,\chi}\|_{L^2_r},\quad
 Q_{v,+}=\|q_v\|_{L^2_r}.
\tag{LC.11}
$$

All coefficients in (LC.9)--(LC.10) are bounded separately on their
actual original row. Whole-domain maxima of $\gamma$, $K$, $m$ or
variance are not substituted into these radial integrals.

For the $\chi'$ term one may use the exact rational row mass

$$
 \int_{\rm row}(\chi')^2\,dr
 ={24576^2\over13/100}
 \int_{t_-}^{t_+}t^{10}(1-t)^{10}(1-2t)^2\,dt
\tag{LC.12}
$$

when the row is inside $I$, and zero outside. Expanding the displayed
integer polynomial gives an exact rational value. The endpoints
$1/20,9/50$ are exact cuts, not floating-point support tests.

The four ordinary/flux norms are then bounded exactly as in CS:

$$
 \begin{aligned}
 \|F_u\|_2&\le
       \alpha(4.201205\,10^{-8})+F_{u,+},&
 \|Q_u\|_2&\le Q_{u,+},\\
 \|F_v\|_2&\le
       C_{v,+}\alpha(8.194504\,10^{-8})+F_{v,\chi,+},&
 \|Q_v\|_2&\le Q_{v,+}.
 \end{aligned}
\tag{LC.13}
$$

The unchanged physical raw residual numbers are read from their
[original complete record](../notes/2026-11-14-R133-final-complete-moving-residual.md).
They are not evaluated again. The exact scalar mean equation is
already solved, whereas the full nonmean residual is not.
The ordinary source $m_\xi\xi\chi'z$, the raw mean defect inside
$R_v-jR_0$, and every genuine coefficient difference remain paid.

If also outputting a weak source norm, apply CS.15 to these saved
four whole bounds: the zero-mean ordinary factor is $4^{-s}$ and
the finite flux factor is $384^{1-s}$ for $0\le s\le1$.
An $H^{-2/3}$ first-row divergence does not have unit conversion
cost.

## LC4. All actual mean and nonmean joins remain in the centre

The terminal mean is continuous and $[h_\xi]=-[m]$. The exact
moving jumps are

$$
 [u_\xi]=[u],\qquad
 [v_\xi]=m_\xi\lambda[z],\qquad z=w/m .
\tag{LC.14}
$$

All 6143 interfaces remain part of the complete object, including
their two one-sided traces. For any interface,

$$
 [z]={ [w]\over m^+}
       -{w^-[m]\over m^+m^-}.
\tag{LC.15}
$$

Projection away from the constant coefficient does not increase
the Fourier $A_0$ norm, so $\|[w]\|_{A_0}\le\|[v]\|_{A_0}$.

Let $M_*,M^*,W^*$ be complete lower/upper bounds for
$|m|,|m|,\|w\|_{A_0}$, respectively. Read the already proved raw
$A_0$ jump sum $J_v$ and complete mean jump sum $J_m$.
The latter is the actual C0 receiver result's
`raw_mean_jump_sum_upper`, not a discarded jump or a numerical zero.
Then a new complete moving jump bound is

$$
 \sum_i\|[v_\xi]_i\|_{A_0}
 \le (M^*+b)(1+\rho)
       \left({J_v\over M_*}
                   +{W^*J_m\over M_*^2}\right).
\tag{LC.16}
$$

The original physical $J_v$ upper is
$\alpha(6.408789\,10^{-13})$ and the unchanged physical $u$ jump
sum is at most $\alpha(4.404428\,10^{-13})$, from the same complete
raw record. Formula (LC.16) is a new bound for the normalized and
rescaled jump. It does not recompute either old raw jump target.
The complete mean jumps in $J_m$ have already been paid by TM.

These are moving-coordinate interface bounds. They do not by
themselves assert a physical-angle trace comparison or erase the
remaining nonmean discontinuities. The centre is still piecewise.

## LC5. A separate exact same-physical-angle identity

This section records an optional additional receiver, not a
hypothesis of (LC.8). No angular-grid evaluation is necessary for
the primary target above.

For fixed $r$, define the family of angular lifts

$$
 \Theta_t(\phi)=\phi+(1+t\chi){\mathcal Iw(\phi)\over m},
 \quad j_t={m+(1+t\chi)w\over m}>0 .
$$

For a fixed physical angle $\theta$, let
$\phi_t=\Theta_t^{-1}(\theta)$. The zero-mean primitive has
$\mathcal Iw(0)=0$ in the even cosine sector, so all these lifts
have the same angular origin. Exact differentiation gives

$$
 \dot\phi_t=-{\chi\mathcal Iw(\phi_t)\over m+\lambda_t w(\phi_t)},
 \qquad \lambda_t=1+t\chi .
\tag{LC.17}
$$

Put

$$
 P=u_\phi\mathcal Iw,\qquad F=w^2-w_\phi\mathcal Iw .
$$

Then

$$
 {d\over dt}u(\phi_t)
   =-\chi{P(\phi_t)\over m+\lambda_t w(\phi_t)},\qquad
 {d\over dt}\bigl(mj_t(\phi_t)\bigr)
   =\chi{m w(\phi_t)+\lambda_t F(\phi_t)
                  \over m+\lambda_t w(\phi_t)} .
\tag{LC.18}
$$

In the second identity **$m$ is the fixed raw mean**. First split the
actual final difference as

$$
 v_\xi(\phi_\xi)-v(\phi_0)
 =h_\xi j_\xi(\phi_\xi)
       +\bigl(mj_\xi(\phi_\xi)-mj_0(\phi_0)\bigr).
\tag{LC.19}
$$

Only the bracket is integrated using (LC.18). Therefore no bound
for $\partial_t m_t$ is used or silently omitted.

The exact finite polynomial identity is

$$
 F=\sum_k a_k^2
   +\sum_{k<l}a_ka_l\left[
       {(k+l)^2\over2kl}\cos(4(k-l)\phi)
       -{(k-l)^2\over2kl}\cos(4(k+l)\phi)\right].
\tag{LC.20}
$$

For a single cosine mode $F$ is exactly constant. Similarly

$$
 P={1\over2}\sum_{k,l}{k\over l}b_ka_l
       \left[\sin(4(l+k)\phi)+\sin(4(l-k)\phi)\right].
\tag{LC.21}
$$

These products must be formed as their joint trigonometric
polynomials before a sharp interval estimate; separately maximizing
$w_\phi$, $\mathcal Iw$ and $j_t^{-1}$ can lose their useful
cancellation. Complete radial polynomial and angular interval
coverage would give

$$
 \begin{aligned}
 |u_\xi(\phi_\xi)-u(\phi_0)|
 &\le\rho\chi\sup_{|t|\le\rho,\phi}
              \left|{P\over m+\lambda_t w}\right|,\\
 |v_\xi(\phi_\xi)-v(\phi_0)|
 &\le b\sup j_\xi+\rho\chi
          \sup_{|t|\le\rho,\phi}
              \left|{mw+\lambda_t F\over m+\lambda_t w}\right|.
 \end{aligned}
\tag{LC.22}
$$

Outside the support the angle maps agree exactly and only the mean
term remains. The physical curvature coordinates $B=u/v,C=1/v$
would require their actual reciprocal-density factors as well.
Neither (LC.22) nor a $B,C$ norm is called the geometry input
$C^0_{r,\phi}$ from (LC.8).

## LC6. Complete new target and saved-prefix semantics

The new consumer admits the complete actual TM/C0 results and their
execution records, the original complete mean native and process
receipt, all five original candidate shards and their complete index,
the raw residual note, and the analytic proofs. It performs only:

1. full closed-row evaluation of the original 32 cubic sine and
   32 nonconstant cosine coefficients needed in (LC.6);
2. the new whole maximum (LC.7), all five complete radial receivers
   (LC.11), and their derived ordinary/flux norms (LC.13);
3. the new rescaled full jump upper (LC.16), using the already saved
   complete old sums.

The original 7721 rows are consumed in their exact order.
The consumer checks piece containment, adjacency, both exact compact
cuts, the complete 6143 interface identities and the terminal point
$25/8$. Every radial integral uses the actual row length. Its finite
carrier reconstruction is necessary input for this new localized
target; it is not a new evaluation of an old raw residual or of a
completed mean/Green/compact-moment target.

Private per-row records are temporary on the public runner. The
published mathematical output contains only whole new scalar bounds,
the actual parameter/input identities, coverage counters and clear
true/false/unknown sufficient gates. Detailed coefficient arrays
and per-row reconstruction data are not published.

A row is accepted only after its prospective maxima, squared
integrals and coverage counters have been serialized and read back
as one complete checkpoint. On failure the last accepted checkpoint
is kept. A partial checkpoint explicitly bounds only its accepted
row prefix and cannot certify the whole geometry or source target.
A genuine continuation, if later needed, consumes these saved
maxima and squared sums and starts with the first unaccepted row.

The final complete gate is evaluated from the saved whole records
after all row and interface counts pass. A false sufficient
$10^{-4}$ test is not a lower-bound violation or nonexistence result.
The mean root, density and negative-mean results remain the already
completed TM conclusions regardless of this separate gate.

The fixed raw metric, selected-metric compatibility, remaining
nonmean equations and joins, full inverse, genuine phase, outer
radial jet, height and both exterior matches retain their distinct
obligations. No final topic completion is asserted here.
