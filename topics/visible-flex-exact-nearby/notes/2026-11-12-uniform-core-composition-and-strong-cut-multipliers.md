# Uniform finite core composition at the physical quarter cuts

This note concerns the actual finite angular compression with modes
$k=-4,\ldots,4$, including the mean, on the exact affine family
$\delta=\delta_5+p$, $|p|\le10^{-9}$. It does not replace the complete
high-channel weak problem by an infinite core Dirichlet map.

The local construction and all finite/infinite primitive, radial Taylor,
angular alias and time-tail budgets are given in
[the correlated radial Taylor note](2026-11-12-core-correlated-radial-Taylor-and-cell-flow.md).
The worker partitions every original common scalar span. A rejected analytic
box may be bisected inside that same scalar germ. The collector requires all
174 original spans and an exact adjacent accepted cover of $[0,1/4]$;
it never fills a missing interval with zero error.

## 1. Ordered propagation

Let $T_j$ be the saved exact dyadic local transfer center in the state
$(w,p/8)$, and let the actual transfer $T_j^\star(p)$ satisfy
$\|T_j^\star(p)-T_j\|\le\epsilon_j$ on the entire same parameter interval.
Define the exact rational prefixes $P_j=T_j\cdots T_1$, $P_0=I$.
Every required prefix inverse is independently enclosed by directed Acb
matrix inversion. For the true prefix $P_j^\star=P_jZ_j$,
$$
 Z_j=(I+D_j)Z_{j-1},\qquad
 D_j=P_j^{-1}(T_j^\star-T_j)P_{j-1}.
$$
Consequently, with
$$
 B=\sum_j\|P_j^{-1}\|\epsilon_j\|P_{j-1}\|,
 \qquad
 \|P_m^\star-P_m\|\le\|P_m\|(e^B-1).                  \tag{1}
$$
The bound is uniform in the single real parameter. No independence of
parameter errors in different cells is assumed or needed: each actual
ordered product for one fixed parameter satisfies all these inequalities.

Matrix norms are directed upper bounds obtained from exact Gram matrices.
All hashes, exact rational endpoints, accepted local reports and complete
array identities are checked before a leaf enters (1). Nonfinite JSON,
nonfinite arrays and nonfinite norm bounds are rejected.

## 2. Reflection and two Cauchy channels

The explicitly symmetric graph gives radial parity
$a,c,\tau,\sigma$ even and $b$ odd. Here the angularly odd coefficient $\sigma=\omega\ell$ is radially even: both $\omega=c_0-c$ and $\ell=(F_z/r)_\theta/(F_z/r)-(F\cdot F_\theta)/(F\cdot F)$ are even in $r$. Angular and radial parity must not be conflated. Thus the finite generator obeys
$$
 {\cal F}(-r)=-J{\cal F}(r)J,\qquad J=\operatorname{diag}(I,-I).
$$
For the positive-half transfer $P^\star$, the full transfer from
$-1/4$ to $1/4$ is therefore exactly
$$
 {\cal T}^\star=P^\star J(P^\star)^{-1}J.             \tag{2}
$$
This is a statement about the actual finite Cauchy system; no Dirichlet
invertibility is used.

If $\|P^\star-P\|\le e$, $q=\|P^{-1}\|$, $p=\|P\|$, and $qe<1$,
then
$$
 \|{\cal T}^\star-PJP^{-1}J\|
 \le \frac{eq(1+pq)}{1-qe}.                          \tag{3}
$$
A second, often sharper bound applies (1) to the complete reflected ordered
chain. Each inverse local center has error at most
$$
 \frac{\|T_j^{-1}\|^2\epsilon_j}
      {1-\|T_j^{-1}\|\epsilon_j}.
$$
The negative half uses these factors in reversed physical order, conjugated
by $J$, followed by the original positive factors. Its exact rational
center equals the expression in (2). The collector takes the minimum of
the two proved bounds; enclosure-comparison error is included when the
separately computed rational expressions are compared.

## 3. Finite DN conversion

Write the exact rational full reference as
$$
 {\cal T}=\begin{pmatrix}A&B\\C&D\end{pmatrix}
$$
in the scaled Cauchy state. Only if the actual finite $B^\star$ is
proved invertible is the finite physical DN map formed:
$$
 \Lambda^\star=8\begin{pmatrix}
 (B^\star)^{-1}A^\star&-(B^\star)^{-1}\\
 C^\star-D^\star(B^\star)^{-1}A^\star&D^\star(B^\star)^{-1}
 \end{pmatrix}.                                      \tag{4}
$$
The port order is left outward $-p$, right outward $+p$.

For a full transfer error $e_T$, put $q_B=\|B^{-1}\|$.
The test $q_Be_T<1$ gives
$$
 q_\star=\frac{q_B}{1-q_Be_T},\qquad
 d_Q=\frac{q_B^2e_T}{1-q_Be_T}.
$$
Valid four-block error bounds for (4), before the factor 8, are
$$
 \begin{aligned}
 d_{11}&=d_Q\|A\|+q_\star e_T,&d_{12}&=d_Q,\\
 d_{22}&=\|D\|d_Q+e_Tq_\star,&
 d_{21}&=e_T+e_Tq_\star(\|A\|+e_T)+\|D\|d_{11}.
 \end{aligned}
$$
The scalar two-by-two Frobenius norm bounds the whole operator error.
For each real parameter, the finite DN form is Hermitian. Hermitian
projection of the reference is contractive relative to this true form.
The selected exact dyadic Hermitian center has its separate directed
selection error added. This pays the finite radial propagation error that
was missing in the earlier floating low-block diagnostic.

The complete infinite core may still have Dirichlet poles. Formula (4)
is not used to discard its two Cauchy channels. Omitted Fourier channels,
body residuals, both exterior regular ports and the complete high Schur
feedback remain separate inputs.

## 4. Uniform ordinary-cut multipliers and stronger output norms

The old quarter-cut multiplier report was a center-only computation.
The new family entry point forms complete central and direction scalar
germs first, then adds the single increment $p\in[-10^{-9},10^{-9}]$.
It reruns the true complex angular domain, complete native primitive
errors, DFT aliases and infinite Fourier tails at the physical cut $r=1/4$.
No root-port $H^{1/3}$ constant is transferred to this cut.

For a coefficient error sequence $e_k$, let
$$
 E_j=\sum_k(4|k|)^j|e_k|,\qquad j=0,1,2.
$$
The zero-frequency term occurs in $E_0$, not in $E_1,E_2$.
With multiplication weights $(1+4|k|)^s$, valid complete bounds are
$$
 \begin{array}{c|c}
 s&\hbox{multiplier error}\\ \hline
 0&E_0\\
 1/2&E_0+\sqrt{E_0E_1}\\
 1&E_0+E_1\\
 3/2&\sqrt{(E_0+E_1)(E_0+2E_1+E_2)}\\
 2&E_0+2E_1+E_2 .
 \end{array}                                           \tag{5}
$$
The half-order bounds follow from weighted Cauchy--Schwarz; all Fourier
modes and all error components are included. These stronger multipliers
allow true high height outputs in $H^1$ or $H^{3/2}$, and shear outputs
in $H^0$ or $H^{1/2}$, once their finite all-output Gram matrices are
included. They do not upgrade the cap's existing $H^{-1/2}$ flux error
to a positive-order norm.

## 5. Actual evidence and scope

Actual reports and exact arrays are saved by the remote workflow under
their distinct run IDs. The first full local cover is run 43307149760:
all nine pieces completed, with 175 accepted leaves over 174 common spans;
one rejected outer box was bisected. The global composition and new
family interface are separate actual executions, whose report hashes
must be cited before using their numerical constants.

Nothing in this note proves the infinite high feedback inverse or the
nonlinear isometric deformation. Those remaining tasks require the actual
weak body sources and full high boundary residuals with their stated
strong Sobolev weights.

## Correction of radial versus angular parity

The first published wording incorrectly grouped sigma with b in radial parity. The corrected statement in section 2 is a,c,tau,sigma even in r and b odd in r; b and sigma are both odd in theta. The 175 completed positive-half certificates do not use negative-half coefficient reflection. The full product collector has not yet executed, and the reflection formula remains valid with the corrected parity because H=tau+sigma_theta is radially even. The new weak-residual negative-side adapter was corrected before any numerical execution; no negative-side result is transferred from its earlier unexecuted version.
