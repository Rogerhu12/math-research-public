# R150: all high-normal targets have source cost 8391 and normalized rank-one Bell eighth powers have original sources

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. The newly available whole-module premise

Use the unchanged original rank-one family
$$
A:\mathbb Q[s]^{6188}\longrightarrow V=\mathbb Q[s]^{4367},
\qquad L=\operatorname{im}A,
$$
with all original seventeen equations and moment multipliers of degree at most three. In the original binomial coordinates
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a,
\qquad c=z_0,\quad d=z_1,
$$
let $W=(z_2,\ldots,z_{10})^2_{\le5}$, the rank-4212 coordinate summand of normal degree at least two.

The [completed zero-projection and relative-module theorem](R150-appendix-zero-projection61-and-complete-relative-nine-target-module25.md) proves
$$
\dim_{\mathbb Q}W/(L\cap W)=25,\qquad
W/(L\cap W)=\sum_{j=2}^{10}\mathbb Q[s]\,[z_j^2],
$$
and hence
$$
\boxed{h_*W\subseteq L,\qquad h_*=s^3F_+^2F_-^2E_8.}
\tag{1.1}
$$
The original polynomial $h_*$ has degree 23 and leading coefficient 3125. This whole-$W$ statement is stronger than knowing only the nine diagonal identities.

The conclusion of this appendix is
$$
\boxed{
\text{each of the 4212 original co-moving basis targets }h_*w
\text{ has a rational original source of cost at most }8391,
}
\tag{1.2}
$$
and, in the normalized rank-one mean chart,
$$
\boxed{b_r^8\in I}
\tag{1.3}
$$
with a specified original seventeen-source construction whose moment degrees are at most eighteen. Equation (1.3) improves the previous sixteenth power. It does not remove the rank-one mean restriction.

No new arithmetic execution is needed for this appendix. Its only new steps are the source-cost substitution and the polynomial identity below, using already completed original-source premises.

## 2. Source cost for an arbitrary already proved member

Keep the same selected original $I,J,B=A_{I,J}$ and actual determinant $D_B=\det B$ used in the [completed affine-divisor and original-source theorem](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md), §5. The paid values are
$$
H=8770,\qquad
8527\le\deg D_B\le8640,
$$
with natural determinant order at least 130, original replacement order at least 125, and cofactor order at least 125.

The exact common divisor is
$$
K'=\Delta_{\rm aff}
=\operatorname{mon}\!\left(
s^{66}(s-2)^{12}(s+6)^{12}F_+^8F_-^8E_8^5
\right)\Omega,
\qquad \deg K'=298.
$$
Here $D_B$ remains the actual determinant; only $K'$ is monic. Therefore
$$
d_*=D_B/K',\qquad q=\deg d_*,
\qquad 8229\le q\le8342.
\tag{2.1}
$$

For an original source $m^\alpha N_i$ or $m^\alpha\Gamma_i$, its weight is
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,
\qquad |\alpha|\le3.
$$
For an original output monomial $m^\beta$, put
$$
b_\beta^{\rm wt}=10|\beta|,\qquad
\tau(b)=\max_\beta\bigl(\deg_s b_\beta(s)+10|\beta|\bigr).
$$
For source coefficients $x$, the original cost is
$$
\operatorname{cost}(x)=\max_\ell(\deg_s x_\ell+a_\ell-10).
$$

Fix any target $b\in L$, with its membership actually proved in this original module. The original identities
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K'\in\mathbb Q[s]^{4354},
\qquad A_JP_\ell=d_*A_\ell
$$
hold on all 4367 outputs. Membership also gives
$$
T_b=\operatorname{adj}(B)b_I/K'\in\mathbb Q[s]^{4354}.
$$
Dividing nonbasic source coefficients by $d_*$, transferring their quotients through $P_\ell$, and retaining their remainders gives an equivalent source with
$$
d_*y_J=T_b-\sum_{\ell\notin J}P_\ell r_\ell,
\qquad \deg r_\ell<q.
$$
The three established weighted-degree branches are consequently
$$
\begin{aligned}
\text{nonbasic}&\le8342-1+45=8386,\\
\text{original-column transfer}
&\le8770+55-125-298-11=8391,\\
\text{target adjugate}
&\le8770+\tau(b)-125-298-10-8229=108+\tau(b).
\end{aligned}
$$
Thus the same original proof yields the general form
$$
\boxed{
b\in L\quad\Longrightarrow\quad
\exists\,x:\ Ax=b,\qquad
\operatorname{cost}(x)\le\max\{8391,108+\tau(b)\}.
}
\tag{2.2}
$$
No assumption about the selected determinant's leading 31 coefficient is needed for this rational statement.

## 3. Applying the bound to all 4212 co-moving basis targets

Let
$$
w=\prod_{j=0}^{10}z_j^{\beta_j},
\qquad |\beta|\le5,\qquad \sum_{j=2}^{10}\beta_j\ge2.
$$
These monomials are exactly the co-moving basis of $W$. Set
$$
d=|\beta|,\qquad \omega=\sum_{j=0}^{10}j\beta_j.
$$
Each $z_j$ is homogeneous of original moment degree one, and its parameter degree is at most $j$. Every original moment coefficient of $w$ therefore has parameter degree at most $\omega$, and every original output monomial has degree $d$. In particular,
$$
d\le5,\qquad\omega\le10d\le50.
$$
Since $\deg h_*=23$,
$$
\tau(h_*w)\le23+\omega+10d\le23+50+50=123.
\tag{3.1}
$$
The target has already been proved to lie in $L$ by (1.1). Equation (2.2) gives
$$
\operatorname{cost}(x_w)\le
\max\{8391,108+123\}
=\max\{8391,231\}=8391.
$$
This proves (1.2), separately for every one of the 4212 original co-moving basis targets. Each resulting source still uses only degree-at-most-three moment multipliers.

For a general polynomial combination $w\in W$, its parameter coefficients can have arbitrarily high degree. The applicable statement is then (2.2) with the actual $\tau(h_*w)$; the bound 123 is specifically the bound for the basis monomials just displayed.

The argument establishes existence and degree bounds. It does not materialize the 4212 source vectors, control their coefficient heights, or impose a common $31$-integral or $127$-integral denominator condition.

## 4. Two completed original identities for the Bell remainder

Work in the normalized physical mean chart
$$
y=v(s)=(1,s,\ldots,s^5),\qquad H=M+\tfrac12y^2.
$$
Fix a matched direction $r$ over its coefficient field. Extending the constant field does not change any of the preceding polynomial identities or the original source-degree bounds.

The [rank-one Bell-source theorem](R150-appendix-rank-one-square-sources-matched-bell-sixteenth-powers-and-global-jacobian-boundary.md) identifies the original matched Bell remainder as
$$
b=b_r(s,M)=6(L_y(M)-yM)(r,r,r)
=\sum_{j=2}^{10}b_{r,j}(s)z_j.
\tag{4.1}
$$
The coefficients have no parameter poles, and the equality holds as an original polynomial identity.

In particular $b^2\in W$. The new whole-module identity (1.1) supplies
$$
h_*b^2=\sum_{\nu=1}^{17}A_\nu\mathcal F_\nu,
\qquad \deg_m A_\nu\le3.
\tag{4.2}
$$
This is the only replacement for the old diagonal-pigeonhole argument: one uses the degree-two element $b^2$ itself, rather than first raising $b$ to degree ten.

The independently completed four-fiber source construction remains
$$
b^2=\sum_{\nu=1}^{17}D_\nu\mathcal F_\nu+q_0E,
\qquad
q_0=sF_+F_-E_8,
\tag{4.3}
$$
where
$$
\deg_m D_\nu\le3,\qquad \deg_m E\le5.
$$
It is the same genuine polynomial CRT identity used in the [previous unmultiplied Bell theorem](R150-appendix-exact-affine-divisor298-unmultiplied-nine-sources-and-rank-one-bell16.md), §7. Its inputs are the original complete fiber sources at the [zero fiber](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md), [plus fibers](R150-appendix-rank-one-Pplus-means-complete-critical-classification.md), [minus fibers](R150-appendix-rank-one-Pminus-means-complete-critical-classification.md), and [octic fibers](R150-appendix-rank-one-E8-means-complete-critical-classification.md). It is not inferred merely from determinant lengths.

The four parameter factors are pairwise coprime. Combining their full original fiber identities uses only parameter-polynomial coefficients, preserving the moment-degree-three source bound. Dividing the resulting numerator by $q_0$ gives the stated moment-degree-five bound on $E$.

We do not assert $E\in W$. That extra premise is neither needed nor supplied.

## 5. The explicit eighth-power source formula

The parameter polynomial
$$
R_q=\frac{q_0^3}{h_*}=F_+F_-E_8^2
$$
has no denominator. Put
$$
K_b=b^4+b^2q_0E+q_0^2E^2.
$$
The ordinary difference-of-cubes identity gives
$$
b^6-q_0^3E^3=(b^2-q_0E)K_b.
$$
Multiplying by $b^2$ and applying (4.2) and (4.3) yields
$$
\begin{aligned}
b^8
&=b^2(b^6-q_0^3E^3)+q_0^3E^3b^2\\
&=b^2K_b\sum_{\nu=1}^{17}D_\nu\mathcal F_\nu
  +R_qE^3\sum_{\nu=1}^{17}A_\nu\mathcal F_\nu.
\end{aligned}
$$
Therefore the original seventeen-source identity is
$$
\boxed{
b_r^8=
\sum_{\nu=1}^{17}
\left(R_qE^3A_\nu+b_r^2K_bD_\nu\right)\mathcal F_\nu.
}
\tag{5.1}
$$
No outside multiplier, inverted parameter polynomial or new equation has been introduced.

The moment degrees of the two source terms satisfy
$$
\deg_m(R_qE^3A_\nu)\le3\cdot5+3=18,
$$
and
$$
\deg_m(b_r^2K_bD_\nu)
\le2+\max\{4,2+5,2\cdot5\}+3=15.
$$
Thus eighteen is a valid common moment-degree bound for the source coefficients in (5.1).

Formula (5.1) is an ordinary ideal identity. Its degree-eighteen source coefficients lie outside the old degree-three Macaulay multiplier family. The rational source-cost bound 8391 from §§2–3 is not assigned to those final Bell source coefficients. Their parameter degrees and coefficient heights have not been newly computed.

This proof does not give a sixth-power identity: that would require another argument about the CRT remainder or a different original relation.

## 6. Scope in the original Bell and Jacobian problem

The ideal in (5.1) is
$$
I=(\mathcal F_1,\ldots,\mathcal F_{17})
$$
in the normalized rank-one mean chart. The fixed nonzero rational row scales between physical and primitive equations preserve the identity after transporting the seventeen coefficients.

For a nonzero rank-one mean $y=a\,v(s)$, weighted scaling transports the normalized identity on the chart $a\ne0$. This statement does not claim that clearing the amplitude-chart denominators leaves the same exponent eight in the unrestricted original ring. The separately completed infinity fiber supplies the remaining nonzero rank-one direction, and the matched Bell remainder vanishes at $y=0$.

Hence the already proved radical conclusion on the rank-at-most-one mean cone remains valid, now with the stronger normalized polynomial identity (5.1). If $\mathcal J=(\nabla R_3)$ and $\mathcal C_1$ is the mean-cone ideal, the conclusion remains
$$
B_r\in\sqrt{\mathcal J+\mathcal C_1}.
$$
The cone ideal cannot be discarded. Neither the whole-$W$ result nor (5.1) proves $B_r^8\in\mathcal J$ for all unrestricted seventeen-variable means.

The actual Bell-inverse denominator theorem therefore still needs its unrestricted Jacobian premise. Here the natural power remains a power of the same complete Bell operator, including its corrections; it is not replaced by a higher ordinary Bell polynomial.

The new conclusions are precisely the uniform original-source bound for every degree-at-most-five high-normal basis target and the eighth-power original ideal identity in the normalized rank-one chart. The coefficient-31 saturation problem and the non-rank-one critical branches remain separate.
