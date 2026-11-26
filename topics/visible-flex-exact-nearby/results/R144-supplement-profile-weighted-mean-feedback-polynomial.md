# R144 supplement: complete profile-weighted mean feedback polynomial

2026-11-26, visible-exact-astra-198c63d-20261126.

This supplies a tighter, directly executable version of the complete
scalar small-ball criterion in
[CR.16–20](R144-supplement-complete-C0-mean-receiver-and-compact-moments.md).
It retains the original scalar inverse, every actual mean jump, the raw
centre at fixed eta0/nu0 and the compact density parameter. It introduces
eleven genuinely new weighted source rows. No old completed Green target
is recomputed, and no new numerical inequality is asserted here.

## CP1. Exact polynomial before taking any norm

Use the same negative raw mean $m$, normalized angular variance
$V=\langle(v-m)^2\rangle$, original operator $L_m$, residual $R_0$,
and $e=\xi\chi$, $\lambda=1+\xi\chi$ as CR.3/13.
Write $q=m_{\rm new}-m$ and
$J_\xi=1+\lambda^2V/m^2$. Expanding the exact new mean equation yields

$$
\begin{aligned}
 L_mq=-R_0-\beta K\big[
 &mV(2e+e^2)+V(2+6e+3e^2)q\\
 &+3(m+\lambda^2V/m)q^2
 +(1+\lambda^2V/m^2)q^3\big].
\end{aligned}
\tag{CP.1}
$$

For example the linear term is
$-2\beta KV\lambda q-\beta KV(4e+3e^2)q$ in CR.16.
Their sum is the full linear coefficient of (CP.1).
The constant term is $-\beta KmV(2e+e^2)$.
Thus the original fixed-density kernel difference is present, including
its value at $\xi=0$. No old nonmean feedback has been omitted.

The boundary and transmission data remain

$$
q(R)=0,\qquad [q]_i=-[m]_i.
\tag{CP.2}
$$

The nonlinear terms in (CP.1) are ordinary sources. They do not create
additional response-jump data for the inverse $L_m^{-1}$.

## CP2. Eleven complete nonnegative coefficient weights

Put $M(r)=|m(r)|>0$ and $B(r)=|\beta(r)K(r)|$.
Since $m<0$, the two summands in $m+V/m$ have the same sign.
The following table gives exact absolute coefficient weights for
(CP.1), with powers of $\xi$ and $q$ factored out:

| Index | Complete nonnegative weight $w_{ab}(r)$ |
| --- | --- |
| 01 | $2BMV\chi$ |
| 02 | $BMV\chi^2$ |
| 10 | $2BV$ |
| 11 | $6BV\chi$ |
| 12 | $3BV\chi^2$ |
| 20 | $3B(M+V/M)$ |
| 21 | $6BV\chi/M$ |
| 22 | $3BV\chi^2/M$ |
| 30 | $B(1+V/M^2)$ |
| 31 | $2BV\chi/M^2$ |
| 32 | $BV\chi^2/M^2$ |

The first index is the power of the unknown $q$; the second is the
power of the scalar parameter $\xi$.
The indices01/02 are constant in $q$.
These are complete radial functions, including the original full
angular variance and every original cell; they are not sampled weights.

For any nonnegative weight $w$, define an upper bound

$$
 C[w]\ge
 \Gamma\max_i b_i
       \sum_{j\ge i} t_j\int_{I_j}w(r)\,dr,
 \qquad
 b_i\ge\sup_{I_i}\tau^{-1},\quad
 t_j\ge\sup_{I_j}\tau .
\tag{CP.3}
$$

Here $\Gamma,\tau$ and all original cells are exactly those of CR.1–10.
The complete backward transformed propagator includes all its
multiplicative interfaces. For any ordinary $f$,

$$
 \|L_m^{-1}(wf)\|_\infty\le C[w]\|f\|_\infty
\tag{CP.4}
$$

when this response has zero terminal value and zero prescribed jumps.
To prove it, use the positive physical homogeneous kernel in CR.6,
integrate separately on every original cell and overestimate the
terminal part of the cell containing the observation point by its
whole cell. This produces (CP.3) uniformly in the observation point.
No extra transform or derivative is introduced.

Let $C_{ab}$ denote a complete bound (CP.3) for $w_{ab}$.
They preserve the actual radial correlation between the weight and
the scalar inverse. In particular $C_{10}$ directly bounds the full
linear feedback $2\beta KVq$, instead of separately multiplying a
full nonmean source receiver by a global variance ratio.

## CP3. Complete uniform contraction criterion

For $0\le\rho<1$ put

$$
 A_0(\rho)=\rho C_{01}+\rho^2C_{02},\qquad
 A_j(\rho)=C_{j0}+\rho C_{j1}+\rho^2C_{j2}
 \quad(j=1,2,3).
\tag{CP.5}
$$

With the original ordinary residual and fixed jump fees,

$$
 E_*=K_0\|R_0\|_\infty+K_J\sum_i|[m]_i|,
\tag{CP.6}
$$

define

$$
 S_{\rm prof}(b,\rho)=
 E_*+A_0+A_1b+A_2b^2+A_3b^3,\qquad
 L_{\rm prof}(b,\rho)=A_1+2A_2b+3A_3b^2.
\tag{CP.7}
$$

If the same complete input has a negative mean gap $m_*>0$ and the
actual saved bounds prove

$$
 0<b<m_*,\qquad
 S_{\rm prof}(b,\rho)\le b,\qquad
 L_{\rm prof}(b,\rho)<1,
\tag{CP.8}
$$

then for every real $|\xi|\le\rho$ there is exactly one fixed point
of the mean equation in $\|q\|_\infty\le b$ with (CP.2).

Indeed each term in (CP.1) is bounded by (CP.4), giving $S_{\rm prof}$.
For two functions in the same ball,
$|q_1^2-q_2^2|\le2b|q_1-q_2|$ and
$|q_1^3-q_2^3|\le3b^2|q_1-q_2|$.
The same complete weights then give $L_{\rm prof}$.
The fixed raw residual and jump map cancel in this difference.
The contraction theorem and the integral representation prove existence,
uniqueness, piecewise absolute continuity and the exact response jumps.
The new mean $m+q$ is continuous and strictly negative.

This is an alternative sufficient gate to CR.19–20.
Both may be retained and evaluated as distinct proved formulas, but
neither is declared successful before its actual saved-ball inequalities
have been checked. A failed gate does not prove nonexistence.

## CP4. Exact compact integration and private execution

The original common partition already has the mandatory support cuts
$1/20$ and $9/50$. Every weight has the form $a(r)\chi(r)^d$ with
$d=0,1,2$ and nonnegative $a$. A whole-cell upper $a_j$ gives

$$
 \int_{I_j}w\le
 \begin{cases}
 a_j|I_j|,&d=0,\\
 a_j\int_{I_j\cap[1/20,9/50]}\chi^d,&d=1,2 .
 \end{cases}
\tag{CP.9}
$$

The last integrals are exact rational integrals of the fixed polynomial
$4096t^6(1-t)^6$ or its square. Thus compact coefficients contribute
exactly zero outside their true support, and no sampled cutoff maximum
replaces their integral.

The original native supplies complete $m,V,\beta,K,\tau$ balls.
Use positive directed lower endpoints for every $M^{-1}$ or $M^{-2}$.
A verified point-centre mean gap may tighten an enclosing affine-box
lower endpoint, because the target is the fixed centre, but its original
identity and parameter membership must be proved.

All eleven suffix sums and their complete row maxima may be accumulated
in one new reverse pass through those saved original rows.
This is a new weighted receiver computation. It is not a recomputation
of the already saved $\mathcal R_m,\mathcal R_{\rm nm},\Gamma$ or the
old mean Green certificate. Their existing whole scalars remain read-only.
The private fine trace is not published as a new reproducible array.

Every accepted reverse-cell checkpoint must preserve all eleven sums,
all eleven maxima and its exact original row cursor together.
A partial prefix is not a whole-body bound. Only after all original
cells have been accepted, the new scalar output has been saved and
read back, and the complete counters have been checked can it be
consumed as the complete $C_{ab}$ set.

## CP5. What still must match

The same $\rho$ must satisfy the genuine compact-root gate using the
actual saved $D_R/H_R$ and the new positive moments, and the independent
density-positivity gate in CR.21. Then the terminal solution from
(CP.8) is identified with the forward root by the scalar linear-ODE
uniqueness argument in CR5.

The physical-angle composition fee, full moving nonmean residual,
cutoff derivative $\xi\chi'$, all raw nonmean jumps, radial cap jets,
height, position, holonomy and true design phase are unchanged
obligations. This scalar criterion does not supply the full coupled
inverse or the final closed fixed-metric family.
