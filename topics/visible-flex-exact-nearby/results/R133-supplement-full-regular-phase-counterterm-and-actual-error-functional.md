# R133 supplement: the complete phase counterterm and its actual response-error functional

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** The complete principal two-ray return has the parameter
variation (P.5)--(P.8), including the direct metric change, the full
regular response, its even mean, and the actual endpoint angle maps.
At the exactly continuous repaired final centre, its response-error
functional has the actual whole-negative-body bounds

$$
 \boxed{\quad
 \|D_QP[e]\|_\infty
 <1.273240\|e\|_{L^2_r(E_0)},\qquad
 \|D_QP[e]\|_\infty
 <1.274436\|e\|_{L^2_rL^2_\phi}.
 \quad}
 \tag{P.1}
$$

The even mean belongs to both norms; no inverse power of
$q=\sqrt{-K}$ is used. All 3,071 actual strict rows and the remaining
true root interval are included. These estimates compare response
directions at the **same** complete background. They do not yet bound
the difference between that background and an unknown nonlinear
solution.

An exact nearby possible rotation target is

$$
 \rho_*=[0;3,1,1,1,3,7,1,3,\overline1]
 =\frac{612575-\sqrt5}{2228182}
 =.274922441734103183577327\ldots .
 \tag{P.2}
$$

Its continued-fraction entries are all at most seven. Consequently
the explicit complete arithmetic bounds in Section 6 hold. This is
a counterterm **target**, not a claim that the present return already
has rotation number $\rho_*$. The actual first scalar phase
$\beta/j$, the complete strong remainder, and the nonlinear
parameter-with-conjugacy closure are still separate obligations.

## 1. Fixed target, full regular response and the two characteristic legs

Use the actual compact metric family

$$
 E_\nu=E\exp(\nu w),\qquad
 w=4096t^6(1-t)^6,\quad t=(r-1/20)/(13/100),
 \tag{P.3}
$$

on its support $[1/20,9/50]$, and $w=0$ outside. The radial $a$,
$\beta=a'/a$ and the true turning root are independent of $\nu$.
Set $\gamma=\sqrt{E_\nu}/a$, $K=K_\nu$, $q=\sqrt{-K}$, and
$T=\beta/(2E_\nu)$. The exact intrinsic identities are

$$
 \gamma_\nu=\tfrac12w\gamma,
 \qquad K_\nu=-wK+Tw'.
 \tag{P.4}
$$

These are the same signs and physical source units as
[the complete metric parameter source theorem](R133-supplement-compact-metric-parameter-source-and-ray-return-twist.md).
Let $Q=(u,v)$ denote a complete physical, unnormalized moving state,
$m=\langle v\rangle$, $S=u^2+Kv^2$ and $d=-\beta I S$.
For $\sigma=\pm1$ the actual negative characteristic field is

$$ F_\sigma=\beta I S-\sigma\gamma m q. \tag{P.5} $$

Write a full state response as $h=(\xi,\zeta)$ and its actual even
mean as $z=\langle\zeta\rangle$. Differentiation with respect to the
metric parameter, including the state response, gives exactly

$$
 \boxed{\begin{aligned}
 \dot F_\sigma={}&
    \beta I(v^2)(-wK+Tw')
    +2\beta I(u\xi+Kv\zeta)\\
   &+\sigma\left\{\frac{\gamma mT}{2q}w'
                                      -\gamma qz\right\}.
 \end{aligned}}
 \tag{P.6}
$$

In the direct metric part of the radial speed, the two terms
$-w\gamma m q/2$ and $\gamma m(-wK)/(2q)$ cancel exactly because
$K=-q^2$. The remaining apparent $q^{-1}$ multiplies $w'$ and
is supported strictly away from the root. The full state mean term
$-\sigma\gamma qz$ is not zero and is not part of the nonmean
primitive.

For the fixed-$\nu$ complete regular boundary operator write
$\mathcal A_{\rm reg}$ for the body Jacobi operator with all waist
$u$ rows and **all** physical outer mean/Robin rows, including the
physical fourth mode. When its true inverse is available, the response
is $q_\nu=\mathcal A_{\rm reg}^{-1}(+\partial_\nu F)$.
Thus (P.6) takes $h=q_\nu$, with no additional reference $s_\nu$
column. Adding such a column to an already physical response would
double count it. A finite response proposal is allowed as input to
the exact linear functional (P.6), but is not declared equal to
$q_\nu$ merely because its discrete QR or FFT residual is small.

Let $H_\sigma(r,x)$ solve

$$
 \partial_rH_\sigma=F_\sigma(r,H_\sigma),\qquad
 H_\sigma(0,x)=x.
 \tag{P.7}
$$

The period is $p_0=\pi/2$. At the true root $r_*$ define
$P=H_-(r_*)^{-1}\circ H_+(r_*)$. With
$J_\sigma=\partial_xH_\sigma$ and
$Y_\sigma=\partial_\nu H_\sigma$, the exact equations and complete
two-leg parameter derivative are

$$
 \begin{aligned}
 (J_\sigma)_r&=(F_\sigma)_\phi(H_\sigma)J_\sigma,
                      &J_\sigma(0)&=1,\\
 (Y_\sigma)_r&=(F_\sigma)_\phi(H_\sigma)Y_\sigma
                         +\dot F_\sigma(H_\sigma),
                      &Y_\sigma(0)&=0,\\
 \boxed{\quad\dot P(x)&=
 \frac{Y_+(r_*,x)-Y_-(r_*,P(x))}{J_-(r_*,P(x))}.\quad}
 \end{aligned}
 \tag{P.8}
$$

Both rays, the inverse on the second ray, and its genuine Jacobian
occur here. The value and parameter variation of each flow are
continuous across fixed radial coefficient interfaces; their one-sided
ODE coefficients are used on their actual pieces. No fictitious
moving-interface contribution is inserted. If the compact $w'$ term
is integrated by parts, the full actual radial derivatives and the
interface terms of N.9--N.11 in the cited source theorem must be kept.

## 2. The two endpoint coordinate maps

For any chosen complete state, let $\Theta_0$ and $\Theta_*$ be its
actual moving-to-physical angle maps at the waist and root. The two
physical legs are

$$
 L_\sigma=\Theta_*\circ H_\sigma\circ\Theta_0^{-1}.
$$

Consequently their actual principal return is

$$
 P_\theta=L_-^{-1}\circ L_+
       =\Theta_0\circ P\circ\Theta_0^{-1}.
 \tag{P.9}
$$

The parameter-dependent root maps cancel **exactly as maps** before
differentiation. They are not individually approximated by the identity.
This is the principal two-characteristic map. It does not delete the
genuine root amplitudes, Maslov constants, positive-cap reflection
remainder or first scalar phase of the full operator.

At the waist the complete angle variation is

$$
 \dot\Theta_0(\phi)=\frac1{m_0}
       I_\phi\left(\zeta_0-\frac{z_0}{m_0}v_0\right).
 \tag{P.10}
$$

For $x=\Theta_0^{-1}(\theta)$, differentiating (P.9) gives

$$
 \boxed{\quad
 \dot P_\theta(\theta)=
 \dot\Theta_0(P(x))+\Theta_0'(P(x))\dot P(x)
                    -P_\theta'(\theta)\dot\Theta_0(x).
 \quad}
 \tag{P.11}
$$

The last two angle terms cannot be removed from a fixed-physical-angle
return derivative. Their cancellation in a rotation functional is
a separate exact conjugacy fact, proved next; it is not a statement
that either endpoint angle has small same-order composition norm.

## 3. Rotation derivative and a parameter counterterm

Assume a genuine degree-one differentiable conjugacy has been constructed:

$$
 H\circ P=H+\Omega,
 \quad H(x+p_0)=H(x)+p_0,\quad H'>0.
 \tag{P.12}
$$

Its invariant probability measure is $d\mu=H'(x)dx/p_0$.
If the conjugacy and parameter family have the needed differentiable
meaning, differentiating (P.12) and integrating against $\mu$ gives

$$
 \boxed{\quad
 \dot\Omega=\int H'(P(x))\dot P(x)\,d\mu(x).
 \quad}
 \tag{P.13}
$$

Indeed invariance cancels the two terms containing $\dot H$. Equation
(P.13) is not asserted for an arbitrary circle-map family on an interval
containing rational plateaux. In particular a decimal orbit rotation
estimate does not establish its hypothesis.

The inverse physical conjugacy is $H_\theta=H\circ\Theta_0^{-1}$.
Substitution of (P.11) into (P.13), with its exact transformed measure,
shows that the contribution of its two $\dot\Theta_0$ terms is zero.
It is the integral of a coboundary. Thus the scalar derivative is
coordinate-invariant although the full pointwise return derivative
is not.

There is an equivalent formulation which avoids assuming a globally
smooth rotation-number function. Prescribe $\Omega_*=p_0\rho_*$,
introduce a genuine embedding $g$ and solve the full invariance equation

$$ P(Q,\nu)\circ g=g\circ R_{\Omega_*}. \tag{P.14} $$

At an exact solution, write $\delta g=g' a$. Differentiating the
invariance equation and using
$P'(g)g'=g'\circ R_{\Omega_*}$ gives the scalar cohomological row

$$
 a-a\circ R_{\Omega_*}
 +\frac{\delta P\circ g}{g'\circ R_{\Omega_*}}
 -\delta\Omega=0.
 \tag{P.15}
$$

The actual phase scalar is its complete average. Nonmean inversion
uses the proved arithmetic of the prescribed $\Omega_*$; the average
must be closed by the true parameter response. For a body equation
$\mathcal D h-(\partial_\nu F)\delta\nu=f$ with all original regular
rows retained, write $h=h_f+q_\nu\delta\nu$. If $L_\Omega$ is the
state contribution to (P.13) and $t_\nu$ its direct metric contribution,
then the exact scalar Schur coefficient is

$$
 S_\Omega=t_\nu+L_\Omega q_\nu,
 \quad
 \delta\nu=\frac{g_\Omega-L_\Omega h_f}{S_\Omega}.
 \tag{P.16}
$$

All original physical fourth-mode and mean boundary equations remain
inside $\mathcal A_{\rm reg}$ in this formula. The waist amplitude is
an output whose final geometric lower bound must be verified. Formula
(P.16) alone supplies neither the true body inverse nor a nonzero
$S_\Omega$; its response, dual, actual phase and remainder errors must
still be bounded. The complete root/strong normal form also retains
the first scalar phase and its nonmean part, not only (P.14).

## 4. A full response-error functional without a turning singularity

Now hold the complete background and target fixed and vary the state
response by $e=(e_1,e_2)$. The exact change of (P.6) is

$$
 D_QF_\sigma[e]=2\beta I(u e_1+Kve_2)
                     -\sigma\gamma q\langle e_2\rangle.
 \tag{P.17}
$$

On the fourfold circle with normalized $L^2$ measure,

$$
 \|I\|_{L^2\to L^\infty}
 =\left(\sum_{j\ne0}\frac1{(4j)^2}\right)^{1/2}
 =\frac{\pi}{4\sqrt3}=:c_I.
 \tag{P.18}
$$

Put

$$
 R_*(r)=\sup_\phi\sqrt{u^2+q^2v^2},\qquad
 E_0(e;r)=\left\langle |e_1|^2+q^2|e_2|^2\right\rangle^{1/2}.
 \tag{P.19}
$$

Cauchy--Schwarz gives
$\|u e_1-q^2ve_2\|_2\le R_*E_0$ and
$q|\langle e_2\rangle|\le E_0$. Hence

$$
 \|D_QF_\sigma[e](r)\|_\infty
 \le a_*(r)E_0(e;r),\qquad
 a_*=2|\beta|c_IR_*+\gamma.
 \tag{P.20}
$$

The true even mean is paid by the last term. This is precisely why
one need not introduce $q^{-1}$ near the root. The limiting inequality
remains valid at $q=0$ since the mean-speed term vanishes there.

Let

$$
 L_d=\int_0^{r_*}\|d_\phi(r)\|_\infty dr.
$$

The two true flows obey
$e^{-L_d}\le J_\sigma\le e^{L_d}$.
Variation of constants in (P.8), followed by the actual inverse-ray
denominator, proves

$$
 \|D_QP[e]\|_\infty
 \le2e^{2L_d}\int_0^{r_*}a_*E_0(e;r)dr
 \le2e^{2L_d}\|a_*\|_{L^2_r}\|e\|_{L^2_r(E_0)}.
 \tag{P.21}
$$

The factor two is the sum of the two distinct legs. For ordinary
$L^2_rL^2_\phi$ response error replace $a_*$ by
$a_*\max(1,q)$ inside its radial norm. No finite head or response
frequency truncation is used in (P.17)--(P.21).

If a genuine conjugacy has additionally supplied $\|H'\|_\infty\le H_*$,
then (P.13) gives the exact same-background scalar error contract

$$
 |L_\Omega e|
 <1.273240H_*\|e\|_{L^2_r(E_0)}
 \quad\text{or}\quad
 <1.274436H_*\|e\|_{L^2_rL^2_\phi}.
 \tag{P.22}
$$

This is not an error estimate for an unproved conjugacy, and it does
not silently absorb a change of background into a response error.

## 5. Actual same-centre consumption of all negative cells and the root

The complete strict native has 3,071 genuine closed rows from $0$ to

$$ r_a=1191939371497/5000000000000=.2383878742994. $$

Each row supplies the actual $\gamma,\beta,K,q$, the complete
$R_*$ bound, and the all-angle $d_\phi$ bound. Its exact continuous
repair adds the known complete pair correction $\epsilon_0$.
For each row, with old upper bounds $U\le R_*$ and $V\ge|v|$, use

$$
 \begin{aligned}
 \Delta S&\le2(R_*+|K|V)\epsilon_0
                  +\max(1,|K|)\epsilon_0^2,\\
 \|\bar d_\phi\|_\infty
     &\le\|d_\phi\|_\infty+2|\beta|\Delta S,\\
 \bar R_*&\le R_*+\max(1,q)\epsilon_0.
 \end{aligned}
 \tag{P.23}
$$

The factor two explicitly pays mean removal in $L^\infty$.
No old centre certificate is assigned the repaired identity.

The remaining interval has length at most $9.0000009\,10^{-6}$ and
lies entirely within the already paid same-centre root germ. The
whole-parameter true root interval is

$$
 [1191984371497/5000000000000,
             2383968743003/10000000000000].
 \tag{P.24}
$$

The true germ bounds $|K'|<60.465470$ and the exact root identity
give $|K|\le60.465470(r_*^{\rm upper}-r_a)$ on that remainder;
in particular $q<.023327865$. Its complete moving Fourier bounds
for $u,v$ then pay $R_*$ and
$\|d_\phi\|_\infty\le2|\beta|(\|u\|^2+|K|\|v\|^2)$.
The fixed strict endpoint is within the proved germ; no box is
extrapolated past a PPoly or intrinsic germ boundary.

The actual Arb sums give

$$
 \begin{aligned}
 L_d&<.036374621,\\
 .9642789870&<J_\sigma<1.037044272,\\
 \|a_*\|_{L^2_r}&<.591950779,\\
 2e^{2L_d}\|a_*\|_{L^2_r}&<1.273240,\\
 2e^{2L_d}\|a_*\max(1,q)\|_{L^2_r}&<1.274436.
 \end{aligned}
 \tag{P.25}
$$

These are complete same-object inequalities, not inferred from the
sampled Jacobian minimum of a floating ray run. They prove (P.1).
They retain the whole original affine interval; a final parameter
counterterm computation may and must restrict to the same chosen
$\eta$ used by its body residual and inverse.

## 6. Exact bounded-quotient arithmetic for a possible counterterm target

Let $\tau=(1+\sqrt5)/2$. The exact continued-fraction matrix for the
finite prefix in (P.2) gives

$$
 \rho_* =\frac{353\tau+91}{1284\tau+331},\qquad
 353\cdot331-91\cdot1284=-1.
 \tag{P.26}
$$

Substituting $\tau^2-\tau-1=0$ yields

$$
 1114091\rho_*^2-612575\rho_*+84205=0,
 \quad\operatorname{disc}=5,
 \tag{P.27}
$$

with the smaller root selected in (P.2). All partial quotients after
the specified finite prefix equal one, so every partial quotient is
at most $A=7$.

Here is the complete small-divisor consequence. For convergents
$p_n/q_n$, the exact continued-fraction error formula is

$$
 |q_n\rho_*-p_n|
 =\frac1{q_n\alpha_{n+1}+q_{n-1}}
 >\frac1{(A+2)q_n},
 \tag{P.28}
$$

where $\alpha_{n+1}<A+1$ is the remaining complete quotient.
The elementary best-approximation property of consecutive unimodular
convergents says that for $q_n\le q<q_{n+1}$,
$|q\rho_*-p|\ge|q_n\rho_*-p_n|$. One way to verify this property
is to write $(p,q)$ in the integer basis
$(p_n,q_n),(p_{n-1},q_{n-1})$: an improvement with denominator below
$q_{n+1}$ would have to be an intermediate positive combination;
its error is $(\alpha_{n+1}-k)|q_n\rho_*-p_n|$ with
$k\le a_{n+1}-1$, which is larger, not smaller.
The other sign choices cannot improve the error under that denominator
bound. Thus every integer $q\ge1$ obeys

$$
 \|q\rho_*\|_{\mathbb R/\mathbb Z}>rac1{9q}.
 \tag{P.29}
$$

It follows that, for every nonzero integer $j$,

$$
 |e^{2\pi i j\rho_*}-1|>\frac4{9|j|}.
 \tag{P.30}
$$

For any of the four possible unit constants $\zeta^4=1$, apply
(P.29) to the rational with denominator $4|j|$ instead. Since
$2|\sin(\pi x)|\ge4\operatorname{dist}(x,\mathbb Z)$, this gives

$$
 \boxed{\quad
 |e^{2\pi i j\rho_*}-\zeta|>\frac1{36|j|}
       \quad(\zeta^4=1).\quad}
 \tag{P.31}
$$

The constants do not deteriorate with the size 1,284 of the selected
finite convergent denominator. They come from the bounded partial
quotients. The target is therefore not selected by adding an
arbitrarily tiny irrational with an unpaid badly-approximable constant.

Equations (P.30)--(P.31) only control the principal arithmetic.
An actual order-$j^{-1}$ scalar phase can compete with these gaps.
Its complete value and the genuine strong remainder still have to be
paid in the same final return normal form. No complete operator inverse
is inferred by dropping that phase.

## 7. Quantifiers, numerical proposals and reproducibility

The exact final construction, if the remaining augmented equations
are closed, chooses **one** pair $(\eta_*,\nu_*)$ and **one** exact
closed nonaxisymmetric state $Q_*$. The entire flex family then has
the one fixed metric $g_{\eta_*,\nu_*}$. The flex parameter is a
different variable; it is never used to vary $\nu$ or the metric.
The physical waist amplitude can be an output of the phase-counterterm
problem, but must still satisfy the original visible-displacement and
reach inequalities after all errors are paid.

The separate full-response floating diagnostic found
$\Omega'\approx.0202241584$, with a substantial cancelling even-mean
contribution. Its inverse-conjugacy proposal gave
$\rho\approx.2749224469841854$. The exact target (P.2) differs from
that **proposal** by approximately $-5.2500822\,10^{-9}$.
Those numbers suggest a small parameter adjustment; neither a true
rotation interval nor a true allowed adjustment interval follows until
the response, flow, conjugacy and complete parameter Schur errors are
bounded. The actual inequality (P.25) is one of the required error
contracts, not a replacement for the remaining contracts.

The new exact consumer is
`scripts/fourfold_codazzi_final_phase_counterterm_budget.py`.
Its complete native is
`notes/2026-11-14-R133-final-ray-response-error-and-quadratic-native.json.gz`.
All twelve Arb/integer gates passed in about six seconds. The native
stores every one of the 3,071 consumed row bounds, the true root
remainder, the original and derived identities, and the exact
continued-fraction matrix and polynomial. It does not read a binary
certificate into the conversation or substitute a sampled flow for
its true closed-box bounds.

From the topic directory the command was

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python \
  scripts/fourfold_codazzi_final_phase_counterterm_budget.py \
  --strict /workspace/scratch/ac0d699811ad/phase-native-restored-20261114/final-strict-v2-ac1-complete-native.json.gz \
  --out notes/2026-11-14-R133-final-ray-response-error-and-quadratic-native.json.gz
```

The strict input SHA256 is
`23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a`;
the same-centre true root-germ SHA256 is
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`.
The original complete inputs remain unchanged. Replay must use a fresh
output path. No nonlinear branch, actual conjugacy, final parameter
value, full strong return inverse, or completed closed flex family is
claimed by this intermediate theorem.
