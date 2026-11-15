# R133 supplement: shape and mean resolved selected-parameter cap-row transfer

2026-11-15, visible-exact-astra-0df9.

**Proved analytic comparison.** The complete 97 moving boundary rows with the old physical cap operator admit a more detailed scalar perturbation bound. It separates the two state components, the genuine even mean, the change of angular coordinate, and the zeroth and first derivatives of the known cap adjoint test. It applies to the entire even $L^2$ input, including every unknown high mode. Its numerical value is to be evaluated from the actual saved cut coefficients.

The exact row and adjoint identities are those of [the full-input selected-parameter comparison](R133-supplement-selected-parameter-cap-row-transfer-with-unknown-high-input.md), denoted Cdelta below. The old complete cap bounds are [the first-angular adjoint theorem](R133-supplement-small-first-angular-adjoint-bound-for-fixed-known-M32-cap.md). No new cap solution or core solution is assumed in the fixed-operator comparison.

## 1. Same cut, true mean and scalar inputs

Keep the repaired centre with definition
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
the continuous response with definition
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04,
the fixed intrinsic parameter $\eta_0$, and the physical cut $L=9/10$.
The real explicit reference is
$$
 Q_\delta=Q_0+\delta Z,\qquad |\delta|\le d=10^{-10}.
 \tag{CS.1}
$$
Write $Q_0=(u_0,v_0)$, $Q_\delta-Q_0=(a,b)$ and
$$
 m_0=\langle v_0\rangle,\quad
 m_\delta=\langle v_\delta\rangle,\quad
 \mu=\langle b\rangle,\quad
 j_0=v_0/m_0,\quad e=b-j_0\mu .
 \tag{CS.2}
$$
All means are genuine normalized moving-angle means. In particular
$\langle e\rangle=0$. No mean is discarded when forming $e$.

Let nonnegative complete scalar bounds satisfy
$$
 \begin{aligned}
 \|a\|_\infty&\le U_0,&\quad \|a_\phi\|_\infty&\le U_1,\\
 \|b\|_\infty&\le V_0,&\quad \|b_\phi\|_\infty&\le V_1,\\
 |\mu|&\le M,&\quad \|e\|_{A^0}&\le S_0 .
 \end{aligned}
 \tag{CS.3}
$$
Here $A^0$ is the full Fourier Wiener norm, including its zero mode.
Full Wiener bounds also suffice for the four pointwise bounds in (CS.3).
The bounds may come directly from the saved signed cut coefficients.
For the real family (CS.1), the previously paid global bounds permit
$U_0+V_0\le19d$ and $U_1+V_1\le83d$. More generally it suffices
that both sums are at most $10^{-6}$, so the elementary Cdelta
bounds hold on the entire straight state segment.

Those bounds, used throughout, are
$$
 |m|,|v|\ge3,\quad |m|<6,\quad
 7/8<j=v/m<9/8,\quad |v_\phi|<1,\quad
 \|\Theta-\mathrm{id}\|_\infty<1/64.
 \tag{CS.4}
$$
The old quantities also obey
$$
 \|u_0\|_\infty<7,\quad \|(u_0)_\phi\|_\infty<6,\quad
 \|(j_0)_\phi\|_\infty<1/16,\quad
 \|(C_0)_\theta\|_\infty<1/32,\quad
 \|(C_0)_{\theta\theta}\|_\infty<2 .
 \tag{CS.5}
$$
These are the already paid bounds in Cdelta.4, Cdelta.7 and
Cdelta.10. The physical function is $C_0=(1/v_0)\circ\Phi_0$.
The signed negative $m,v$ remain in every exact identity.

## 2. Coordinate change depends on the shape component

The exact identity
$$
 j_\delta-j_0=\frac{e}{m_\delta}
 \tag{CS.6}
$$
gives a complete angle bound without replacing $e$ by the whole state
difference. On the fourfold circle, the zero-mean primitive has
$A^0$ operator norm at most $1/4$. Therefore, with
$$
 T=\frac{S_0}{12},\qquad P=\frac87T,
 \tag{CS.7}
$$
we have
$$
 \|\Theta_\delta-\Theta_0\|_\infty\le T,\qquad
 \|\Phi_\delta-\Phi_0\|_\infty\le P .
 \tag{CS.8}
$$
The latter uses the lower Jacobian $7/8$. The reflection normalization
fixes the additive angle in both maps. The Wiener hypothesis in
(CS.3) is essential for the factor $1/4$ in this step; it is not an
$L^\infty$ primitive estimate.

If an additional complete bound $S_1\ge\|e_\phi\|_\infty$ is available,
then
$$
 \|b\|_\infty\le S_0+\frac98M,\qquad
 \|b_\phi\|_\infty\le S_1+\frac1{16}M .
 \tag{CS.9}
$$
These are optional bounds for the pointwise quantities used below.
They preserve $\mu$ exactly. A consumer may use either these bounds
or the corresponding complete bounds in (CS.3).

## 3. Separate the two norms of the known adjoint test

Let $K=(K_B,K_C^0)$ be the complete old physical cap pair,
with its actual independent scalar mean output. It has
$$
 \|K\|_{L^2_{\perp,\theta}\to L^2_\theta\oplus_1\mathbb R}<16 .
 \tag{CS.10}
$$
For a unit combination of all 97 original rows, put
$$
 f=\sum_{j=1}^{96}\lambda_j\sqrt2\sin(4j\phi),\quad
 a_*=\lambda_{97},\quad
 k=K^*(S_0^*f,a_*),\qquad
 \|\lambda\|_2=1 .
 \tag{CS.11}
$$
In this section $S_0^*$ is the operator at the old state:
$S_Q^*f=m(f\circ\Phi)$, as in Cdelta.11. It is distinct from
the scalar shape bound $S_0$ in (CS.3).

The proved first-angular adjoint theorem gives
$\|k\|_{H^1_\theta}\le2^{16}$. Its zeroth-order norm also has the
separate much smaller bound
$$
 \|k\|_2\le108,\qquad \|k_\theta\|_2\le2^{16}.
 \tag{CS.12}
$$
Indeed, $\|V_0 f\|_2\le(9/8)\|f\|_2$ and $|m_0|<6$.
The dual of the output sum norm in (CS.10) is the maximum norm, so
$$
 \|K^*(S_0^*f,a_*)\|_2
 \le16\max\{6(9/8)\|f\|_2,|a_*|\}\le108\|\lambda\|_2.
$$
This is a bound for one arbitrary joint test, including its mean
coordinate. It introduces no $\sqrt{97}$ factor.

By Cdelta.9, composition of a known $H^1$ function with the two
inverse angle maps costs at most $(9/8)P$ times its derivative norm.
Since $\|f_\phi\|_2\le384\|f\|_2$, define
$$
 L_S=\frac98M+2592P .
 \tag{CS.13}
$$
Then
$$
 \|(S_\delta^*-S_0^*)f\|_2\le L_S\|f\|_2 .
 \tag{CS.14}
$$
The first term changes the signed mean multiplier; the second changes
the coordinate of the known finite test.

## 4. Curvature adjoint: multiplication and composition separately

At a common moving angle,
$$
 (C_Q)_\theta\circ\Theta_Q=-\frac{m v_\phi}{v^3}.
$$
The absolute partial derivative bounds with respect to
$m,v,v_\phi$ are $1/27,2/9,2/9$, respectively, by (CS.4).
Changing the old physical argument costs at most $2T$ by (CS.5).
Consequently
$$
 D_C=\frac{M}{27}+\frac{2V_0}{9}+\frac{2V_1}{9}+2T
 \tag{CS.15}
$$
is a complete bound for
$\|(C_\delta)_\theta-(C_0)_\theta\|_\infty$.
Throughout this same family $|C|\le1/3$ and
$|C_\theta|<1/16$, by Cdelta.10.

Use the exact adjoint, with its density and signed mean,
$$
 H_{C,Q}^*k
 =-\frac{k\circ\Theta_Q}{mv}
   +\frac1m\{I_\theta(C_\theta k)\}\circ\Theta_Q .
 \tag{CS.16}
$$
The first term has difference bounded by
$$
 \frac{8(M+V_0)}{189}\|k\|_2
       +\frac{8T}{63}\|k_\theta\|_2 .
 \tag{CS.17}
$$
For the multiplication part,
$|\Delta(1/(mv))|\le(M+V_0)/27$ and the composition norm
is at most $8/7$. For the remaining part, the old multiplier is
at most $1/9$ and Cdelta.9 gives $(8/7)T\|k_\theta\|_2$.

Split the second term of (CS.16) into the change of $1/m$,
the change of $C_\theta$, and the change of its final argument.
Their respective bounds are
$$
 \frac{M}{504}\|k\|_2,\qquad
 \frac{2D_C}{21}\|k\|_2,\qquad
 \frac{T}{84}\|k\|_2 .
 \tag{CS.18}
$$
For the first, $|\Delta(1/m)|\le M/9$ and
$$
 \|I_\theta(C_{\delta,\theta}k)\circ\Theta_\delta\|_2
 \le\frac87\frac14\frac1{16}\|k\|_2=\frac1{56}\|k\|_2.
$$
The second uses $(1/3)(8/7)(1/4)D_C$.
For the third,
$\partial_\theta I_\theta(C_{0,\theta}k)
=P_{\perp,\theta}(C_{0,\theta}k)$ has norm at most $\|k\|_2/32$;
use $(1/3)(8/7)T/32=T/84$.
Thus the primitive's genuine mean is handled by its actual nonmean
projection, whose norm is one.

Set
$$
 q_0=\frac{8(M+V_0)}{189}+\frac{M}{504}
                 +\frac{2D_C}{21}+\frac{T}{84},\qquad
 q_1=\frac{8T}{63}.
 \tag{CS.19}
$$
For every known $k\in H^1_\theta$,
$$
 \|(H_{C,\delta}^*-H_{C,0}^*)k\|_2
 \le q_0\|k\|_2+q_1\|k_\theta\|_2 .
 \tag{CS.20}
$$
Only the second term needs the first-angular norm of the test.
The unknown input is still an arbitrary even $L^2_\phi$ function.

## 5. Complete local row

Write $D_Q=u/v$, $\psi_Q=\Theta_Q-\mathrm{id}$ and
$$
 A_Q h=I_\phi h-\langle h\rangle\psi_Q .
$$
The exact moving expression is
$$
 S_QH_{B,Q}h=-D_Qh-(D_Q)_\phi A_Qh .
 \tag{CS.21}
$$
Cdelta.20 gives $\|A_Q\|_{2\to2}<1/3$ and
$\|A_\delta-A_0\|_{2\to2}\le T$.

Directly splitting the displayed quotients, using old
$\|u_0\|_\infty<7$, $\|(u_0)_\phi\|_\infty<6$, gives
$$
 \|\Delta D\|_\infty\le D_0^\#:=U_0/3+7V_0/9
 \tag{CS.22}
$$
and
$$
 \|\Delta D_\phi\|_\infty
 \le D_1^\#:=U_1/3+U_0/9+32V_0/27+7V_1/9 .
 \tag{CS.23}
$$
For example, in
$D_\phi=u_\phi/v-u v_\phi/v^2$, the first summand costs
$U_1/3+2V_0/3$. Splitting the three factors of the second
summand costs $U_0/9+7V_1/9+14V_0/27$.
Their sum is (CS.23); no derivative of an unknown trace is taken.

The old $\|(D_0)_\phi\|_\infty<3$ therefore gives
$$
 L_{\rm odd}=D_0^\#+D_1^\#/3+3T,\qquad
 \|\Delta(SH_B)\|_{2\to2}\le L_{\rm odd}.
 \tag{CS.24}
$$
The independent mean row changes by
$|\Delta(m^{-2})|\le2M/27$. The full local contribution is
at most $L_{\rm odd}+2M/27$.

## 6. Final complete 97-row estimate

The full moving row is Cdelta.12:
$$
 {\cal B}_Q^K h=
 \left(
 P_{\mathrm{o},96}\{h_1+S_Q(H_{B,Q}-K_BP_{\perp,\theta}H_{C,Q})h_2\},
 -m^{-2}\langle h_2\rangle-K_C^0P_{\perp,\theta}H_{C,Q}h_2
 \right).
 \tag{CS.25}
$$
Pair the cap contribution with one joint test $(f,a_*)$:
$-\langle K^*(S_Q^*f,a_*),H_{C,Q}h_2\rangle_\theta$.
The change of the first test costs at most $(16/6)L_S$,
because the complete curvature map has norm less than $1/6$.
The change of $H_C$ costs at most $108q_0+2^{16}q_1$,
by (CS.12) and (CS.20). All scalar means in these identities remain.

Adding the local contribution proves
$$
 \boxed{
 \|{\cal B}_{Q_\delta}^{K}-{\cal B}_{Q_0}^{K}\|_{L^2_\phi\to\mathbb R^{97}}
 \le \epsilon_{\rm shape}
 :=L_{\rm odd}+\frac{2M}{27}+\frac83L_S
                    +108q_0+2^{16}q_1 .}
 \tag{CS.26}
$$
This includes the full two-component moving input: its $h_1$
coefficient is unchanged. It is a single operator estimate for every
joint linear combination of the original 97 rows, including the
independent even mean, and applies to both low and unknown high input.

If $b=\mu j_0$, the angular coordinate is exactly unchanged.
Then $S_0=T=P=q_1=0$; the remaining mean and multiplier terms in
(CS.26) are still paid. This explains why a shape-resolved bound can
be substantially better than using one global state bound everywhere.
The actual improvement must be checked from the complete cut scalars.

For the explicit family (CS.1), one may take
$$
 \begin{aligned}
 U_0&=d\|\xi(L)\|_{A^0},& U_1&=d\|\xi_\phi(L)\|_{A^0},\\
 V_0&=d\|\zeta(L)\|_{A^0},& V_1&=d\|\zeta_\phi(L)\|_{A^0},\\
 M&=d|\langle\zeta(L)\rangle|,&
 S_0&=d\|\zeta(L)-j_0\langle\zeta(L)\rangle\|_{A^0}.
 \end{aligned}
 \tag{CS.27}
$$
The continuous centre and response repairs, including their means,
must be included in those same-cut quantities. The signed subtraction
inside the last norm occurs before the positive upper bound is taken.
Old finite boundary residuals are not substitutes for these full
physical coefficients.

## 7. Separate actual-cap perturbation and later uses

If a different complete physical cap pair $K_*$ satisfies
$\|K_*-K\|_{L^2_\perp\to L^2\oplus_1\mathbb R}\le\kappa$,
under all of its original actual-cap hypotheses, define
$$
 \begin{aligned}
 j_+&=1.015211829+S_0/3,& m_+&=5.8639401366+M,\\
 C_+&=.318181201+V_0/9+T/32,&
 C_{1,+}&=.020269146+D_C,\\
 s_+&=m_+\sqrt{j_+},&
 c_+&=\sqrt{j_+}(C_+^2+C_{1,+}C_+/4).
 \end{aligned}
 \tag{CS.28}
$$
The first line follows from (CS.6) and the original old joint table.
For $C_+$, change the reciprocal at a common moving angle, then
change the old physical argument by $T$ and use
$\|(C_0)_\theta\|_\infty<1/32$.
The bound for $C_{1,+}$ is (CS.15).

The complete boundary perturbation then obeys
$$
 \epsilon_{\rm row}
 \le\epsilon_{\rm shape}+\max(s_+,1)c_+\kappa .
 \tag{CS.29}
$$
It is permissible to choose the smaller of (CS.26) and Cdelta.24
as two complete bounds for the same fixed-$K$ operator difference.
Similarly, the two complete valid coefficients for the independent
physical-cap perturbation can be compared. No entrywise change to a
signed Poisson Gram follows from either scalar comparison.

These fees can be consumed in [the finite193 feedback contract](../notes/2026-11-15-R133-selected-parameter-finite193-scalar-feedback-contract.md).
The original three feedback gates, true ordinary source gains, and
three distinct body, negative and cut outputs remain required.
All affine boundary defects, independent waist and mean data, the
complete $\nu$ source and the true high inverse remain independent.
This theorem gives neither the actual-cap input domain for an unknown
core trace nor a nonlinear core solution.
