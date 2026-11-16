# R897 — An actual quotient theta basis and the original same-label source in its ramified Gauss expansion

Date: 2026-11-16. Status: proved an integral basis of the actual descended theta module by a normalized original trace, the exact leading content of its original Gauss map, and the appearance of R889's same-label Frobenius-source section with an explicit unit coefficient. The coefficient's specified fifth jet is the original sigma product. Nonvanishing of that jet, the original Legendre factor, and the modular normal/height comparison remain open.

## 1. Fixed source and the available precision

Use the original objects and signs of R886/R889/R892/R895:
$$
p\ge41,\quad p\equiv5\pmod6,\quad
k=\mathbf F_{p^2},\quad e=p^2-1,\quad n=p+1,
$$
$$
E_0:y^2=x^3-1,\quad dz=dx/(2y),\quad
\kappa=-6B\in\mathbf F_p^\times,\quad
[D,Q]=1,\quad D^p=Q^p=0.
\tag{897.1}
$$
Write
$$
\mathcal B_R=
H^0(E_0,O(6pO))\otimes_R H^0(E_0,O(6pO)),
\qquad R=W(k),
$$
allowing the original unramified extension for the tame marking. Let $R'$ be the original ramified torsion ring, with
$$
\varpi=Y(P_1),\qquad
\operatorname{ord}_\varpi(p)=e,\qquad
\varpi^e/p\equiv+1.
\tag{897.2}
$$
Neither the parameter nor the differential is rescaled. In expansions put
$$
\lambda=\varpi^{p-1}.
\tag{897.3}
$$

Let $\pi_L$ be the actual quotient of R886 and $\mathcal U_L$ its rank-$36$ descended theta module. Its pullback is the saturated invariant submodule of $\mathcal B_{R'}$:
$$
\pi_L^*\mathcal U_L=\mathcal B_{R'}^{\tau(L)}.
\tag{897.4}
$$
On the special fiber put
$$
\mathcal H_0=\ker D
=\{f^ps_{6p}:f\in H^0(E_0,O(6O))\},\qquad
\mathcal M=\mathcal H_0\otimes_k\mathcal H_0.
$$
As in R895, write $|r,s\rangle m=(Q^r\otimes Q^s)m$, for $m\in\mathcal M$. The indices are $0,\ldots,p-1$; the index $p$ is absent.

Choose the original ordered tame basis
$$
1,\ x,\ y,\ x^2,\ -xy,\ x^3
$$
on each factor of $H^0(O(6O))$, and use its Frobenius basis on $\mathcal M$. In the fixed original integral rational-section basis of $\mathcal B_R$, choose an unramified lift $\widetilde v_m$ of $|p-1,p-1\rangle m$ for each of these $36$ basis vectors. Coefficientwise Teichmueller lifts in that basis make this a definite choice if desired. The construction does not choose an arbitrary ramified lift.

R895's trace formula gives the actual congruence
$$
\mathcal T_L(\widetilde v_m)
\equiv
-\lambda^2
 \sum_{r=0}^{p-1}\frac{(\kappa\lambda)^r}{r!}
 |r,r\rangle m
\pmod{\varpi^{e+1}\mathcal B_{R'}}.
\tag{897.5}
$$
Every coefficient on the right is lifted from the unramified basis. Its leading coefficient is exactly $-m$: the two factors $(p-1)!=-1$ in the first trace band multiply to $+1$, and the trace band itself has the minus sign. There is no residual $\kappa$ power in that coefficient.

## 2. A genuine integral quotient basis

The original trace takes values in (897.4). Formula (897.5) proves that it is divisible in $\mathcal B_{R'}$ by $\varpi^{2(p-1)}$. Saturation in (897.4) proves the same divisibility before pullback. Define
$$
\boxed{
u_m=-\varpi^{-2(p-1)}
 (\pi_L^*)^{-1}\mathcal T_L(\widetilde v_m)
 \in\mathcal U_L.
}
\tag{897.6}
$$
This is an actual integral section of the descended line bundle. It is not defined only in a generic Schrödinger model.

Division in (897.5) gives
$$
\boxed{
\pi_L^*u_m
\equiv V(\lambda)m:=
 \sum_{r=0}^{p-1}\frac{(\kappa\lambda)^r}{r!}
 |r,r\rangle m
\pmod{\varpi^{(p-1)^2+1}\mathcal B_{R'}}.
}
\tag{897.7}
$$
In particular its reduction is $m$. The $36$ reductions are independent. Since the saturated image of $\mathcal U_L$ has rank $36$, Nakayama's lemma gives
$$
\boxed{\{u_m\}\text{ is an }R'\text{-basis of }\mathcal U_L,\qquad
 \overline{\pi_L^*\mathcal U_L}=\mathcal M.}
\tag{897.8}
$$
This also specifies the tame multiplicity normalization; it is not an unspecified invertible change of the $36$ channels.

Changing $\widetilde v_m$ by $p$ times another unramified section changes (897.6) by an element of $p\mathcal U_L$: R895's trace has minimum valuation $2(p-1)$ on the entire unramified section module. Consequently all precision statements below are independent of that unramified lift choice. They are not asserted for an arbitrary element of $\mathcal U_L$ with the same reduction but a difference only divisible by $\varpi$.

## 3. The original Gauss map and its first possible indices

Keep the original odd primitive label
$$
7\le h\le p-4,\qquad h\equiv1\pmod6,\qquad (h,p+1)=1.
\tag{897.9}
$$
The actual map of R886 is
$$
\Gamma_h=\mathcal G_{\theta_h^{-1}}\pi_L^*,
\qquad
\theta_h(d)=[d]^{-h(p-1)}.
\tag{897.10}
$$
After the same legitimate complete-sum reindexing as R895, its reduced Gauss operator is
$$
\mathscr G_h^-=
\sum_{d\in k^\times}d^{h(p-1)}
 \mathscr R_d(X)\otimes\mathscr R_{\overline d}(X).
\tag{897.11}
$$
The inverse character in (897.11) is essential: the reverse map $\mathcal C_h$ uses the other character.

The Gauss operator has valuation at least $p-1$ on the entire integral section module. Its degree-zero sum is exactly zero; every smaller positive degree has zero reduced finite power sum, and any unreduced coefficient correction by $p$ has valuation at least $e+1>p-1$. Thus the error in (897.7), after applying the actual Gauss map, has valuation at least
$$
(p-1)^2+1+(p-1)=p(p-1)+1.
\tag{897.12}
$$
The distribution approximation itself is valid modulo $\varpi^{e+1}$ by R892, and $p(p-1)<e$. Therefore (897.7), (897.11) determine $\Gamma_h(u_m)$ completely through degree $\varpi^{p(p-1)}$. No higher trace coefficient, hidden constant multiple of $p$, or full reduction of a nonintegral sigma series is required.

Consider a term of degree $\lambda^j$ in $\mathscr G_h^-V$. Suppose the input from $V$ has index $u,u$, and the Gauss band has index $l\ge1$, so $j=u+l$. The finite power sums and norm-one weights give output indices
$$
r\equiv j-h,\qquad s\equiv j+h\pmod n.
\tag{897.13}
$$
For $j\le p$, the normal $Q$ degree bound in R895 excludes every case except
$$
j\ge H_h:=\max(h,n-h),\qquad
r=j-h,\quad s=j+h-n.
\tag{897.14}
$$
Indeed before both indicated reductions modulo $n$ occur, the total primary degree increase from $2u$ would be $2l$ or $2l+n$, larger than the sum of the two quotient digits, which is at most $l-1$. A missing index $p$ also gives zero.

In the remaining case the required degree change is $2l-n$. This is exactly the maximum ordinary-branch difference for two distribution indices summing to $l(p-1)$. Every genuine cross-$p$ correction of R895 lowers it by $n$, as does the other possible digit sum. Consequently only the ordinary normal branches contribute at this precision. This argument includes $l=p$ and retains the cross-$p$ terms everywhere else.

## 4. Exact coefficients of the ramified Gauss source

Write
$$
a=h-1,\qquad b=p-h,\qquad a+b=p-1.
\tag{897.15}
$$
Both $a$ and $b$ are even. For $H_h\le j\le p$, put
$$
r=j-h,\qquad s=j+h-n.
$$
There is a scalar $\gamma_{h,j}$, acting identically on the actual $\mathcal M$, such that
$$
\boxed{
\Gamma_h(u_m)\equiv
\sum_{j=H_h}^{p}
 \gamma_{h,j}\lambda^j|j-h,j+h-n\rangle m
\pmod{\varpi^{p(p-1)+1}\mathcal B_{R'}}.
}
\tag{897.16}
$$
Here and below the left side means its original inclusion in $\mathcal B_{R'}$.

The exact coefficient is
$$
\boxed{
\gamma_{h,j}
=-\kappa^{j-1}
 \sum_{v=0}^{\min(r,s)}
 \frac{2^{j-1-v}}
 {v!(r-v)!(s-v)!(p-j+v)!}.
}
\tag{897.17}
$$
A derivation also checks the sign and all the powers of two. For the ordinary branches justified in §3, write the finite normal expression
$$
e^{\kappa d^pX^pQ_1}e^{dXD_1}
e^{\kappa dX^pQ_2}e^{d^pXD_2}
e^{\kappa d^{p+1}X^{p+1}}.
$$
Acting on $V=e^{\kappa X^{p-1}Q_1Q_2}$ at the permitted coefficients gives
$$
V\,
 e^{2\kappa X^p(d^pQ_1+dQ_2)}
 e^{2\kappa d^{p+1}X^{p+1}}.
\tag{897.18}
$$
This follows by the two polynomial translations $Q_1\mapsto Q_1+dX$ and $Q_2\mapsto Q_2+d^pX$. It is not a full theta exponential assertion.

If the contribution from $V$ in (897.18) is $v$, the two creation powers are $r-v,s-v$, and the scalar exponential degree forced by $\lambda^j$ is
$$
t=p+v-j.
$$
It is nonnegative and satisfies
$$
t\le p-H_h<p.
$$
The exponent of $d$, including the original inverse character $d^{h(p-1)}$, is exactly $e$. Its sum over $k^\times$ is $-1$ in $k$. The remaining $\kappa$ exponent is $j-1$ and the power of two is $j-1-v$, proving (897.17).

All factorials displayed in (897.17) are below $p$. One can justify (897.18) initially as an identity of rational generating series: the added terms of $V$ with index above $p$ cannot reach degree $\lambda^p$ after the positive-degree Gauss operator. The sole boundary term with $V$ index $p$ would use the degree-zero Gauss sum, which is exactly zero already over the unramified ring, before reduction or division by $p!$. On the contributing right-hand terms $v,r-v,s-v,t$ are all below $p$. Thus the generating-series calculation introduces no hidden $p$ denominator. It computes exactly the actual ordinary branches selected in §3.

## 5. Zero and unit coefficients, including the critical coefficient

For a closed evaluation put $d=p-j$, so
$$
r=b-d,\qquad s=a-d,\qquad 0\le d\le\min(a,b).
$$
The finite binomial identity for the symmetric Jacobi polynomial gives
$$
\gamma_{h,p-d}
=-\frac{(2\kappa)^{p-d-1}}{b!(a-d)!}
 P_{b-d}^{(d,d)}(0).
\tag{897.19}
$$
For completeness, expanding
$$
{}_2F_1(-r,-s;d+1;1/2)
$$
as a finite sum gives the sum in (897.17) multiplied by $r!s!d!$. Here
$-s\equiv r+2d+1\pmod p$, so its usual finite binomial expansion is
$r!/(d+1)_r$ times $P_r^{(d,d)}(0)$, with
$(d+1)_r=b!/d!$. Every denominator is a factorial below $p$; this proves (897.19) purely as a finite identity in $k$.

The value in (897.19) is particularly explicit:
$$
P_r^{(d,d)}(0)
=2^{-r}[z^r](1-z^2)^{r+d}
=
\begin{cases}
0,&r\text{ odd},\\
(-1)^{r/2}2^{-r}\binom{r+d}{r/2},&r\text{ even}.
\end{cases}
\tag{897.20}
$$
This follows directly from the two-binomial formula for a Jacobi polynomial at zero. Since $r+d=b<p$, every nonzero binomial in (897.20) is a unit. Because $a,b$ are even, (897.19)--(897.20) prove
$$
\boxed{
\gamma_{h,j}=0\text{ for even }j,\qquad
\gamma_{h,j}\in k^\times\text{ for odd }j
\quad(H_h\le j\le p).
}
\tag{897.21}
$$
Both $h$ and $n-h$ are odd, so $H_h$ is odd. In particular the leading coefficient in (897.16) is a unit.

At the critical coefficient $j=p$, formula (897.17) reads
$$
\gamma_{h,p}
=-\frac{\kappa^{p-1}2^{p-1}}{a!b!}
 \sum_v\binom av\binom bv\,2^{-v}.
$$
The exact original constants give
$$
\kappa^{p-1}=2^{p-1}=1,\qquad a!b!=-1.
$$
The finite Legendre expansion, using $b\equiv-1-a\pmod p$, therefore yields
$$
\boxed{
\gamma_{h,p}=P_{h-1}(0)
=(-1)^{(h-1)/2}2^{-(h-1)}
 \binom{h-1}{(h-1)/2}\in\mathbf F_p^\times.
}
\tag{897.22}
$$
There is no omitted negative sign, $\kappa$ power, or independent phase in (897.22). The minus in the Gauss power sum and the minus from $a!b!$ cancel; the minus in the quotient basis was already fixed in (897.6).

The basis in §2 also gives an exact content statement for the actual map:
$$
\boxed{
\operatorname{ord}_\varpi\Gamma_h(u)
=H_h(p-1)+\operatorname{ord}_\varpi u
\qquad(0\ne u\in\mathcal U_L).
}
\tag{897.23}
$$
To see this, factor out the common minimum valuation of the coefficients of $u$ in the basis $\{u_m\}$. At the first remaining layer, (897.16) sends its nonzero reduction $m$ to the single primary vector
$\gamma_{h,H_h}|H_h-h,H_h+h-n\rangle m$, which is nonzero by (895.2) and (897.21). Thus no cancellation between the $36$ channels is possible. Higher layers are not needed for this statement.

In particular $\Gamma_h/\varpi^{H_h(p-1)}$ is an integral map whose image is saturated: its reduction is injective between free modules, so a maximal minor is a unit. This is a statement about this actual Gauss image and its explicitly established scaling. Since $H_h<n$, it does not make $\Gamma_h/p$ integral.

## 6. The same original sigma product is an actual coefficient of this source

Choose the specific original tame basis vector
$$
m_{G,F}=\bigl((-xy)^ps_{6p}\bigr)\otimes
        \bigl(x^ps_{6p}\bigr)\in\mathcal M,
$$
and let $u_{G,F}$ be its actual trace-normalized quotient section (897.6), independent of $h$.

Formula (897.22) identifies a particular ramified coefficient of the original split-source map:
$$
\boxed{
[\varpi^{p(p-1)}]_{\rm res}\Gamma_h(u_{G,F})
=P_{h-1}(0)\,
 (Q^{p-h}(-xy)^ps_{6p})\otimes
 (Q^{h-1}x^ps_{6p}).
}
\tag{897.24}
$$
The notation means the coefficient in the fixed unramified section basis, reduced in $k$. It is unambiguous at this precision: $p(p-1)<e$, so changing any unramified lift of a preceding coefficient by $p$ cannot change it. The whole list of preceding coefficients is given by (897.16), not silently set to zero.

This is exactly R889's flipped same-label Frobenius-source section, now obtained as a coefficient of an actual integral $\Gamma_h$ on a specified section of the actual quotient. It is not an identification with the unpowered enlarged source $S_{F,G}$.

Write the original indices
$$
p=6N+5,\qquad h=6i+7,\qquad j=N-1-i,
$$
$$
F=x\sigma^6=z^4f(z^6),\qquad
G=-xy\sigma^6=z\,g(z^6).
\tag{897.25}
$$
Let $J_{3,2}$ be the ordinary local coefficient in the original two rational section frames $s_{6p}/Y^{6p}$ at $(O,O)$. It is an integral functional on the section module. R889's exact formula and (897.24) give
$$
\boxed{
[\varpi^{p(p-1)}]_{\rm res}
 J_{3,2}\bigl(\Gamma_h(u_{G,F})\bigr)
=
P_{h-1}(0)\,
 \frac{(6B)^5}{12}(f_i g_j)^p.
}
\tag{897.26}
$$
The factor preceding $(f_i g_j)^p$ is a unit. The differentiation/frame convention is the original one; neither the physical period nor the six-level phase is replaced.

The nonvanishing of the original sigma product is therefore equivalent to nonvanishing of this specified coefficient of the actual Gauss-source jet. This does not follow from (897.23): the latter proves a vector-content statement at the earlier layer $H_h(p-1)$, whereas (897.26) applies a particular local functional at a later layer. A nonzero vector at either layer need not have a nonzero $J_{3,2}$.

## 7. Exact scope of the comparison

The source $u_{G,F}$ is fixed by the original trace, original rational-section basis, and the unramified lift class. It is not asserted that every ramified lift of $m_{G,F}$ has the same critical coefficient. A change only divisible by $\varpi$ in $\mathcal U_L$ can affect layers below $p(p-1)$. This is why the construction in §2 is retained.

The primitive character is exactly $\chi^{2h}$, with the full character $\theta_h$ in (897.10). The construction does not identify $h$ with $h+n/2$. The original CM average $\mathcal A_h$ is still the separate generic-fiber operator of R886 §7; no preservation of the theta lattice or of the ramified filtration by that operator is inferred.

In particular the original additional condition
$$
P_{h-1}(1/\sqrt{-3})\ne0
$$
is not replaced by the always-unit coefficient $P_{h-1}(0)$ in (897.22). The latter is the explicit coefficient transporting the original sigma product into $\Gamma_h$, not the original Legendre visibility factor. The exact scalar identity
$$
\mathcal C_h\mathcal A_h\Gamma_h=p^2N_h,\qquad
N_h\bmod p=-P_{h-1}(1/\sqrt{-3})^2
$$
remains as in R886, and does not make its three individual maps integral after their displayed divisions.

Thus the new bridge is an actual fixed quotient section, an actual ramified Gauss source, and the exact same-$h$ coefficient (897.26), with unit transport and no unspecified tame matrix. What remains is its required scalar nonvanishing and its compatibility with the original CM visibility/normal-height conditions. No claim of Serre uniformity follows from this source comparison alone.

## Sources

- [R886](R886-original-two-flag-theta-descent-and-split-contraction.md), §§2--7: actual quotient, theta descent, original $\Gamma_h$, Gauss character, and the scope of the generic CM average.
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md), §§2--7: original $D,Q$ and the exact flipped fifth-jet identity.
- [R892](R892-original-theta-recursion-and-divided-split-contraction.md), §§3--6: all genuine distributions, unramified coefficient precision, original uniformizer, and saturated descent.
- [R895](R895-original-all-band-theta-contraction-and-unramified-content.md), §§2--4: normal-branch bound and full trace factorization, including the cross-$p$ correction branch.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the original primitive/Legendre/sigma target at the same label.

All computations here are symbolic coefficient proofs in the stated original models. No local mathematical execution, new finite prime scan, or new numerical assertion is used.
