# R150: exact affine divisor 298, removal of the outside multiplier, and original rank-one Bell sixteenth powers

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Completed conclusions and the unchanged original map

Keep the original seventeen equations and all original moment multipliers of degree at most three:
$$
A:\mathbb Q[s]^{6188}\longrightarrow V=\mathbb Q[s]^{4367},
\qquad L=\operatorname{im}A.
$$
The original nine targets are
$$
t_j(s,m)=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
$$
Use the original integer normalizations
$$
\begin{aligned}
F_+&=-8+32s-25s^2+5s^3,\\
F_-&=864+864s+135s^2+5s^3,\\
E_8&=9600-25472s-3392s^2+15936s^3-2888s^4\\
&\hspace{1em}-936s^5+153s^6+50s^7+5s^8,
\end{aligned}
$$
and put
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,\qquad
h_*=s^3F_+^2F_-^2E_8,\qquad h_0=(s-2)h_*.
$$
In particular, $\deg h_*=23$ and its original leading coefficient is $3125$.

The completed characteristic-zero conclusions are
$$
\boxed{
\Delta_{\rm aff}=\operatorname{mon}(K_{178})\,\Omega,\qquad
K_{178}=s^{66}(s-2)^{12}(s+6)^{12}F_+^8F_-^8E_8^5,
\qquad \deg\Delta_{\rm aff}=298,
}
\tag{1.1}
$$
where $\Omega=f_{60}^2$ is the already computed exact external projection divisor. With the previously fixed definition of the outside multiplier,
$$
\boxed{\mu=R_{\rm out}/\Omega=1.}
\tag{1.2}
$$
Consequently there are original polynomial sources
$$
\boxed{
Ax^{(j)}=h_*t_j,\qquad
x^{(j)}\in\mathbb Q[s]^{6188},\qquad
\operatorname{cost}(x^{(j)})\le8391
\quad(2\le j\le10).
}
\tag{1.3}
$$

In the normalized physical rank-one mean chart $y=v(s)$, the matched Bell remainder $b_r$ therefore satisfies the genuine original ideal identity
$$
\boxed{b_r^{16}\in I,}
\tag{1.4}
$$
with an explicit finite rule for constructing its seventeen source coefficients and moment degree at most 26 for those coefficients. Here $I$ is the original seventeen-equation ideal in the rank-one chart. It is not the unrestricted seventeen-variable Jacobian ideal.

This appendix combines completed original calculations with exact module and polynomial identities. It does not report a new large matrix computation or materialize the rational source coefficients in (1.3).

## 2. The actual local inputs and exact degree equality

The [completed critical-spectrum theorem](R150-appendix-exact-original-critical-spectra-three-five-and-two-three.md) proves, over the original number fields,
$$
F_+:(3,5),\qquad F_-:(3,5),\qquad E_8:(2,3).
$$
Thus their full local determinant lengths are eight, eight, and five. These are full original-source conclusions, not results for a restricted quadratic support.

For both cubic fields, the first positive exponent was already exactly three. The new cochain has the same nonfree leading head, is independent of the thirteen full formal-free heads, and satisfies all $6188\cdot5=30940$ original products through order four. Hence the second positive exponent is at least five. The full characteristic-127 upper bound eight makes it exactly five.

At the octic factor the complete second connection has rank one. Its fourteen surviving heads satisfy all $6188\cdot14\cdot3=259896$ original products, and the full local upper bound five gives the exact spectrum $(2,3)$. The separate read-only recovery rechecks the completed mathematical pack; the earlier oversized-receipt failure remains a failure in the historical record.

The [critical theorem](R150-appendix-exact-original-critical-spectra-three-five-and-two-three.md) also retains the already exact original lengths 66, 12, and 12 at $s=0,2,-6$. Therefore $K_{178}$ divides every original full maximal minor. Its degree is
$$
66+12+12+3\cdot8+3\cdot8+8\cdot5=178.
$$

The [exact original external-divisor theorem](R150-appendix-exact-original-external-divisor120-multiplier21-and-source-cost8411.md) proves
$$
\Omega=f_{60}^2,\qquad
\deg\Omega=120,\qquad
\gcd(\Omega,\Sigma_0)=1,\qquad \Omega\mid\Delta_{\rm aff}.
$$
It uses all 56 original rows of the polynomial projection core: the common rank-21 residue kernel, both original single-RHS solves, all 56 exact divisions, and all 56 second residuals. No finite-field factor has been substituted for this rational divisor.

Hence
$$
K_{178}\Omega\mid\Delta_{\rm aff},\qquad
\deg\Delta_{\rm aff}\ge178+120=298.
$$
The independent [root63 original coefficient-torsion certificate](R150-appendix-original127-first-coefficient-torsion-at63-and-affine-degree298.md) proves $\deg\Delta_{\rm aff}\le298$. Equality of degree and monic normalization prove (1.1). Since the original rational infinity length is 66, the full homogeneous divisor has degree
$$
298+66=364.
$$

Selected completed execution pins are:

| Original calculation | Actual step in run 43772109844 | Raw bytes | Raw SHA256 |
|---|---|---:|---|
| Cubic plus nonfree prolongation | critical-plus-one-nonfree-positive-prolongation | 11447 | a1d6f0ea815c691152b89617a0882507aabd89217a80db6676fb933f41bf11a0 |
| Cubic minus nonfree prolongation | critical-minus-one-nonfree-positive-prolongation | 14056 | 1477c986e0a551a965b71470447d64a391bf978692df7ab37eaeb45eec196dca |
| Octic complete second connection | critical-e8-first-exit-readonly-completion | 9456 | 15349fa57fdcae012ffc16fb65fe357258def3f45aeaf9563e39fa31cb395081 |

The corresponding original [plus](../notes/r150-source-kernel-session-789f/43772109844-critical-plus-one-nonfree-positive-prolongation.json), [minus](../notes/r150-source-kernel-session-789f/43772109844-critical-minus-one-nonfree-positive-prolongation.json), and [octic](../notes/r150-source-kernel-session-789f/43772109844-critical-e8-first-exit-readonly-completion.json) receipts all report successful completed mathematics. Their bindings, original products, source hashes and temporary cochain hashes are retained in the cited local theorem.

## 3. The outside multiplier and the relative target module

Use the original binomial co-moving coordinate change
$$
z_j=\sum_{a=0}^j\binom ja(-s)^{j-a}m_a.
$$
Let $W\subset V$ be the normal-degree-at-least-two coordinate summand, of rank 4212. Every $t_j=z_j^2$ belongs to $W$. Define
$$
T=W/(L\cap W),\qquad C=V/L,\qquad
C_P=(V/W)/((L+W)/W).
$$
The original ranks are 4354 and 142 for $A$ and the full $224\times155$ projection. Thus $T$ is torsion, and $C,C_P$ have the same free rank thirteen.

The [original projection-divisor theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md) proves the exact sequence
$$
0\longrightarrow T\longrightarrow C\longrightarrow C_P\longrightarrow0
$$
and, at every monic irreducible $f$, the exact torsion-length identity
$$
\operatorname{length}T_{(f)}
=v_f(\Delta_{\rm aff})-v_f(\Delta_P).
\tag{3.1}
$$
The torsion map is surjective because the induced map of the equal-rank free quotients over the DVR is a surjection, hence an isomorphism.

The already fixed definitions are
$$
R_{\rm out}
=\prod_{f\nmid\Sigma_0}f^{v_f(\Delta_{\rm aff})},
\qquad
\Omega=\prod_{f\nmid\Sigma_0}f^{v_f(\Delta_P)},
\qquad
\mu=R_{\rm out}/\Omega.
\tag{3.2}
$$
The first expression is also the part of $\Delta_{\rm aff}/K_{158}$ outside $\Sigma_0$, since $K_{158}$ is supported on $\Sigma_0$.

Equation (1.1) gives $R_{\rm out}=\Omega$, so $\mu=1$. More strongly, (3.1) gives
$$
T\otimes_{\mathbb Q[s]}\mathbb Q[s,\Sigma_0^{-1}]=0.
\tag{3.3}
$$
The old global ratio $\Delta_{\rm aff}/(K_{158}\Omega)$ is instead
$\operatorname{mon}(F_+^2F_-^2E_8)$. That ratio is supported inside $\Sigma_0$ and is not the multiplier $\mu$.

## 4. Nine unmultiplied original rational sources

The local target results used in the [external projection theorem](R150-appendix-external-projection-divisor-removes-target-residual-and-source-cost.md), §1, are original-source identities:

| Finite support | Already paid local target membership |
|---|---|
| $s=0$ | $s^3t_j\in L_{(s)}$ |
| $s=2,-6$ | $t_j\in L_{(s-2)},L_{(s+6)}$ |
| $F_+$ and $F_-$ | $F_\pm^2t_j\in L_{(F_\pm)}$ |
| $E_8$ | $E_8t_j\in L_{(E_8)}$ |

They follow from the [zero cubic-cost bridge](R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md), [complete two-point local membership](R150-appendix-two-complete-third-connection-smith12-and-all-original-square-local-membership.md), and [low-projection/critical local-source identities](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md). They are not merely vanishing at critical points.

For the critical rows of this table, no exact spectrum of the full projected matrix is needed. The original low-source calculations give projected local length at least six at each cubic factor and at least four at the octic factor. The now completed full lengths eight and five, together with (3.1), give
$$
\operatorname{length}T_{(F_\pm)}\le2,\qquad
\operatorname{length}T_{(E_8)}\le1.
$$
These bounds alone kill the entire local relative module by $F_\pm^2$ and $E_8$, respectively. A spectrum for the small low slice is not silently promoted to the spectrum of the full projection.

At every prime dividing $\Sigma_0$, these identities kill $h_*[t_j]$. At every other finite prime, (3.3) kills $[t_j]$ itself. An element of a finitely generated $\mathbb Q[s]$-module which is zero at all maximal localizations is zero. Hence
$$
h_*t_j\in L\qquad(2\le j\le10).
\tag{4.1}
$$
The sources in (4.1) belong to the original 6188-column module. Equivalently, there are seventeen polynomial coefficients $C_{\nu j}(s,m)$ satisfying
$$
h_*z_j^2=\sum_{\nu=1}^{17}C_{\nu j}\mathcal F_\nu,
\qquad \deg_m C_{\nu j}\le3.
\tag{4.2}
$$
The fixed rational row units transport this statement between the original primitive and physical equation normalizations. Multiplication by $s-2$ also gives the original $h_0t_j$ members. No division by $s-2$ has been used.

## 5. Recomputed original rational source cost: 8391

Use the same old original $I,J,B=A_{I,J},D=\det B$ as in the [rational source theorem](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md). Its paid constants are
$$
H=8770,\qquad 8527\le\deg D\le8640,
$$
with natural determinant order at least 130, original replacement order at least 125, and cofactor order at least 125. The original weights are
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad
\operatorname{cost}(x)=\max_\ell(\deg x_\ell+a_\ell-10).
$$
Here $|\alpha|\le3$, $\max a_\ell=55$, and $\max(a_\ell-10)=45$.

Put $K'=\Delta_{\rm aff}$, of degree 298, and keep $D$ as the actual original determinant. Then
$$
d_*=D/K',\qquad 8229\le q:=\deg d_*\le8342.
$$
Every original transfer
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K'
$$
is polynomial, and $A_JP_\ell=d_*A_\ell$ holds on all 4367 original outputs. For $b=h_*t_j$, membership (4.1) also makes
$$
T_b=\operatorname{adj}(B)b_I/K'
$$
polynomial. Original nonbasic division by $d_*$ and transfer give
$$
d_*y_J=T_b-\sum_{\ell\notin J}P_\ell r_\ell,\qquad
\deg r_\ell<q,\qquad Ay=b.
$$

The weighted target degree satisfies
$$
\tau(h_*t_j)\le23+20+20=63.
$$
The three actual branches are
$$
\begin{aligned}
\text{nonbasic}&\le8342-1+45=8386,\\
\text{original-column transfer}&\le8770+55-125-298-11=8391,\\
\text{target adjugate}&\le8770+63-125-298-10-8229=171.
\end{aligned}
\tag{5.1}
$$
This proves (1.3). For $h_0t_j$, $\tau\le64$ changes the last branch to 172; the same common bound 8391 still holds. These are original degree-three-source bounds. Coefficient heights and expanded rational source arrays have not been computed here.

## 6. Uniform reduction of existing 31-integral sources: 8515

The separately proved [new original minor](R150-appendix-new-original-maximal-minor-degree8769-and-unit-leading-coefficient.md) has
$$
H_*=8835,\qquad D_*=\det B_*,\qquad\deg D_*=8769,\qquad
\operatorname{lc}(D_*)\in D_{31}^{\times},
\quad D_{31}=\mathbb Z_{(31)}.
$$
Its determinant and original replacements have natural order at least 66, and its cofactors have order at least 55.

The monic rational divisor $K'=\Delta_{\rm aff}$ divides $D_*/\operatorname{lc}(D_*)$. Gauss' lemma gives $K'\in D_{31}[s]$. Monic division of every original replacement numerator likewise gives integral transfers. Keep $D_*$ unchanged: only the common factor is monic.

Now
$$
q_*=\deg(D_*/K')=8769-298=8471.
$$
The exact [uniform source-reduction proof](R150-appendix-uniform-source-bound8655-over-all-powers-of31.md) gives
$$
\begin{aligned}
q_*-1+45&=8515,\\
8835+55-66-298-11&=8515,\\
8835+\tau(b)-55-298-10-q_*&=\tau(b)+1.
\end{aligned}
$$
Therefore every already existing original congruence solution modulo $31^n$ admits a representative with
$$
\boxed{\operatorname{cost}(y)\le\max\{8515,\tau(b)+1\}.}
\tag{6.1}
$$
The same bound holds for an existing exact $D_{31}[s]$ solution. For a fixed $e$, solvability of $31^e b$ at arbitrarily high precision still implies an exact solution within this bound.

The new rational membership (4.1) gives some finite power of 31 after clearing the 31-parts of its rational denominators. It does not determine that exponent, assert $e=0$, or change the previously recorded mod-961 obstruction for an unscaled target. The rational bound 8391 and the uniform integral reduction bound 8515 have different quantifiers.

## 7. Original normalized rank-one Bell identity without an outside multiplier

Use the exact notation and original equations of the [rank-one Bell-source theorem](R150-appendix-rank-one-square-sources-matched-bell-sixteenth-powers-and-global-jacobian-boundary.md). In the normalized chart
$$
y=v(s)=(1,s,\ldots,s^5),\qquad H=M+\tfrac12 y^2,
$$
let $I=(\mathcal F_1,\ldots,\mathcal F_{17})\subset\mathbb Q[s,m]$. For a fixed direction $r$, the original matched Bell remainder pulls back to
$$
b_r(s,M)=6(L_y(M)-yM)(r,r,r)
=\sum_{j=2}^{10}b_{r,j}(s)z_j.
\tag{7.1}
$$
The coefficients have no parameter poles. The equality is an original polynomial identity before taking the quotient by $I$.

Expanding the tenth power and assigning each monomial to its first repeated normal variable gives explicit polynomials $Q_j$ such that
$$
b_r^{10}=\sum_{j=2}^{10}Q_jz_j^2,\qquad\deg_m Q_j=8.
$$
Using (4.2), define
$$
A_\nu=\sum_{j=2}^{10}Q_j C_{\nu j}.
$$
Then
$$
h_*b_r^{10}=\sum_{\nu=1}^{17}A_\nu\mathcal F_\nu,\qquad
\deg_m A_\nu\le11.
\tag{7.2}
$$

Put $q_0=sF_+F_-E_8$. The already completed full original fiber-source statements at $s=0$, all $F_+$ conjugates, all $F_-$ conjugates, and all $E_8$ conjugates give
$$
b_r^2=\sum_{\nu=1}^{17}D_\nu\mathcal F_\nu+q_0E,
\qquad \deg_m D_\nu\le3,\quad\deg_m E\le5.
\tag{7.3}
$$
This is the genuine four-fiber CRT construction in the cited Bell theorem. It uses full quadratic-normal fiber membership, not just local determinant lengths. Its original references are the [zero fiber](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md), [plus fibers](R150-appendix-rank-one-Pplus-means-complete-critical-classification.md), [minus fibers](R150-appendix-rank-one-Pminus-means-complete-critical-classification.md), and [octic fibers](R150-appendix-rank-one-E8-means-complete-critical-classification.md).

Since
$$
R_q=q_0^3/h_*=F_+F_-E_8^2
$$
is a polynomial, put
$$
K_r=b_r^4+b_r^2q_0E+q_0^2E^2.
$$
The difference-of-cubes identity and (7.2)–(7.3) give the fully specified original-source formula
$$
\boxed{
b_r^{16}
=\sum_{\nu=1}^{17}
\left(R_qE^3A_\nu+b_r^{10}K_rD_\nu\right)\mathcal F_\nu.
}
\tag{7.4}
$$
There is no extra $\mu$ and no inverted parameter polynomial. The first source term has moment degree at most $15+11=26$. The second has moment degree at most $10+10+3=23$. Thus 26 is a valid common moment-degree bound.

Equation (7.4) lies in the ordinary original ideal. Its higher moment-degree multipliers are not members of the old degree-three Macaulay source dictionary. The number 8391 in §5 is not asserted as the source cost of (7.4).

## 8. Exact rank-one and global-Jacobian boundaries

The identity (7.4) holds on the entire normalized affine rank-one chart, for every fixed $r$ after the corresponding coefficient-field extension. Weighted scaling treats nonzero amplitudes $y=a\,v(s)$ on the chart $a\ne0$. The separately completed [infinity fiber](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md) covers the remaining nonzero rank-one mean direction. At $y=0$ the original matched Bell remainder itself vanishes.

Accordingly, the matched remainder vanishes at all complete critical points whose physical mean lies on the rank-at-most-one cone. With $\mathcal J=(\nabla R_3)$ and $\mathcal C_1$ the mean relations defining that cone, this gives
$$
B_r\in\sqrt{\mathcal J+\mathcal C_1}.
$$
The cone ideal cannot be omitted. The normalized identity (7.4) does not establish $B_r^{16}\in\mathcal J$ in all seventeen unrestricted variables and does not clear the amplitude-chart denominator with the same exponent.

The remaining unrestricted problem includes the non-rank-one mean branches not already covered by the [essential-cubic-dimension-at-most-three theorem](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md). A full global Jacobian identity for one fixed direction must be proved there before the [actual Bell-inverse denominator theorem](R150-appendix-jacobian-certificates-with-actual-bell-inverse-denominators.md) can be applied.

In that final bridge the natural power is the power of the same complete Bell operator, including its corrections. It is not a replacement by a higher ordinary Bell polynomial, and none of $h_*$, a parameter coordinate, or an amplitude has been furnished with an operator inverse by this appendix.

The completed advancement is the exact affine divisor, elimination of the external target multiplier, nine original rational sources, and the unmultiplied normalized rank-one Bell identity. No unrestricted invariant-subspace conclusion is claimed.
