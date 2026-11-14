# R744 — Original depth-four Abel root polynomials of degree at most three

Date: 2026-11-14. **Status: proved.**

This result controls the entire original closed candidate disc
$v_p(a-1)\ge4$, including the annuli not covered by R742's
depth-seven isometry. For a primitive component with first-jet
valuation at most one, the complete Abel function has at most
three noncentral zeros on that disc, counted with multiplicity.
An exact polynomial over $\mathbf Q_p$ of degree at most three
accounts for all of them. The polynomial is obtained from the
whole restricted series, not from a truncated Abel function.

This is a theorem about the original Abel component. It does
not turn the positive-rank rational-point condition into Abel
vanishing, and does not supply the missing height equations.

## 1. The same original component and its whole series

Let $p\ge41$, $p\equiv2,5\pmod9$, and $n=p+1$. Fix an original
primitive positive label

$$
(h,n)=1,\qquad h\equiv1\pmod6.
$$

Use exactly the positive R575/R588 marking, the original finite
Cartan vector, the original CM period, and the original coarse
coordinate $s=a-1$. Suppose

$$
M_{2,h}\ne0,\qquad \eta=v_p(M_{2,h})\le1.
\tag{744.1}
$$

R742 proves $\eta\in\mathbf Z$ and $\eta\ge-2$. Thus there are
only four possible valuations in (744.1). No auxiliary change
of tame representative or differential scale is made here.

Retain the full series and the full coordinate change of R730/R742:

$$
E_j=\frac{p^{3j}M_{3j-1,h}}{(3j)!},\qquad
\mathscr I(V)=\sum_{j\ge1}E_jV^j,\qquad
E_1=\frac{p^3M_{2,h}}6,
\tag{744.2}
$$

$$
\mathcal I_h(s)=\mathscr I\bigl(\Psi(s/p^3)\bigr),\qquad
\Psi(v)=\frac38v+\sum_{j\ge2}\psi_jv^j,
\quad \psi_j\in p\mathbf Z_p,
\quad \Psi\in\mathbf Z_p\langle v\rangle.
\tag{744.3}
$$

The original quotient component is $J_h=\gamma_h\mathcal I_h$
with its fixed nonzero Kodaira–Spencer comparison $\gamma_h$.
Multiplication by this scalar preserves every zero and its
multiplicity; its valuation is not assumed to be zero.

Define

$$
\beta_j=E_j/E_1\in\mathbf Q_p\quad(j\ge2),
\qquad
Q_h(u)=\frac{\mathscr I(pu)}{E_1pu}
=1+\sum_{k\ge1}a_ku^k,
\qquad a_k=p^k\beta_{k+1}.
\tag{744.4}
$$

The quotient at $u=0$ means its analytic extension, whose value
is exactly one. Rationality in (744.4) is R730's actual common
Abel line, retained by R742. It does not rescale different jets.

## 2. A bound for every coefficient, including the factorial tails

The complete one-$p$ Hodge estimate gives

$$
v_p(E_j)\ge\frac{3j-1}{p+1}-v_p(3j)>0,
\qquad v_p(E_j)\longrightarrow+\infty.
\tag{744.5}
$$

The strict inequality holds at every index. If $p\nmid3j$ it
is immediate. If $a=v_p(3j)\ge1$, then $j\ge p^a$ and the
lower bound is at least $(3p^a-1)/(p+1)-a>0$. This also tends
to infinity with $j$ because the subtracted valuation is only
logarithmic. Thus indices for which $p$ divides $(3j)!$ have
not been omitted.

R742 places all allowed jets in one unramified field. Therefore
each nonzero $E_j$ has integer valuation. Combining this with
(744.5), and treating a zero coefficient as having infinite
valuation, proves

$$
v_p(E_j)\ge1.
$$

Since $v_p(E_1)=3+\eta$, we obtain the sharper componentwise
form of R742's tail bound:

$$
\boxed{
v_p(\beta_j)\ge-\eta-2,\qquad
v_p(a_k)\ge k-\eta-2,\qquad
v_p(a_k)\longrightarrow+\infty.
}
\tag{744.6}
$$

In particular $Q_h\in\mathbf Q_p\langle u\rangle$. Every
coefficient of degree strictly greater than $\eta+2$ belongs
to $p\mathbf Z_p$. This is a bound on the complete infinite
series; it is not a statement just about its first four terms.

## 3. The exact Weierstrass factor on the closed unit disc

Put $a_0=1$, and define

$$
\mu=\min_{k\ge0}v_p(a_k),\qquad
d=\max\{k:v_p(a_k)=\mu\}.
\tag{744.7}
$$

These extrema exist because the coefficients tend to zero and
$a_0=1$. Equation (744.6) shows that both can be read from
the coefficients of degrees $0,\ldots,\eta+2$:

$$
\mu=\min_{0\le k\le\eta+2}v_p(a_k)\le0,
\qquad
\boxed{d\le\eta+2+\mu\le\eta+2\le3.}
\tag{744.8}
$$

Indeed, equality $v_p(a_k)=\mu$ at $k\ge1$ forces
$k\le\eta+2+\mu$ by (744.6). If $d=0$, the normalization
$a_0=1$ forces $\mu=0$, and the same bound applies. For
$\eta=-2$ one has $\mu=d=0$. If $\eta\ge-1$, then

$$
-\eta-1\le\mu\le0.
\tag{744.9}
$$

The restricted series $p^{-\mu}Q_h$ has integral coefficients,
Gauss norm one, a unit coefficient in degree $d$, and all
higher coefficients in $p\mathbf Z_p$. The one-variable
closed-disc Weierstrass preparation theorem gives uniquely

$$
\boxed{
Q_h(u)=p^\mu U_h(u)W_h(u),
\quad U_h\in\mathbf Z_p\langle u\rangle^\times,
\quad W_h\in\mathbf Z_p[u]\text{ monic},
\quad \deg W_h=d\le3.
}
\tag{744.10}
$$

Here the unit and its inverse are both integral restricted
series. To see the integrality in the stated normalization,
the theorem supplies a monic polynomial of Gauss norm one
and a Tate unit; multiplicativity of the Gauss norm makes
the unit have norm one. A norm-one Tate unit has constant
term a unit and all its other coefficients in $p\mathbf Z_p$,
so its inverse is integral as well.

The theorem being used is for a closed disc: the lower
coefficients of $W_h$ are integral, and need not all belong
to $p\mathbf Z_p$. See Bosch, *Lectures on Formal and Rigid
Geometry*, §2.2, Corollary 9 in the 2014 edition; the author's
2008 notes give the same statement in §1.2, Corollary 9,
printed p. 13. The source is linked below.

Evaluating (744.10) at zero yields two further exact facts:

$$
\boxed{W_h(0)\ne0,\qquad v_p(W_h(0))=-\mu.}
\tag{744.11}
$$

The polynomial is canonical for the full $Q_h$. The first
four jets suffice to determine $\mu,d$ and its reduction,
since for $d>0$

$$
\overline{W_h}(u)
=\overline{p^{-\mu}a_d}^{\,-1}
\sum_{k=0}^{d}\overline{p^{-\mu}a_k}\,u^k.
\tag{744.12}
$$

They do not, by themselves, determine the exact coefficients
of $W_h$ or its exact roots. The complete tail enters
Weierstrass preparation.

## 4. Transport back to the entire original depth-four disc

Write $s=p^4x$. Equation (744.3) gives

$$
u=\frac{V}{p}=\Phi(x),\qquad
\Phi(x)=\frac{\Psi(px)}p
=\frac38x+p^2R(x),
\quad R\in x^2\mathbf Z_p\langle x\rangle.
\tag{744.13}
$$

Because $3/8$ is a $p$-adic unit, this is an isometric
automorphism of the closed unit disc over any complete
valued extension of $\mathbf Q_p$. Its inverse is an
integral restricted series over $\mathbf Q_p$. For example,
for prescribed $u$, iteration of
$x=(8/3)u-(8/3)p^2R(x)$ is a strict contraction of the closed
disc. The same iteration in the complete Tate algebra gives
the stated analytic inverse. In particular

$$
v_p(\Phi(x))=v_p(x),\qquad
\Phi'(x)\in\mathcal O^\times.
\tag{744.14}
$$

Substituting (744.10) gives the full analytic factorization

$$
\boxed{
\mathcal I_h(p^4x)
=E_1p^{\mu+1}\Phi(x)\,
 U_h(\Phi(x))W_h(\Phi(x)).
}
\tag{744.15}
$$

Thus the center is a simple zero, because $M_{2,h}\ne0$ and
$W_h(0)\ne0$. Every noncentral zero, including one on the
boundary $v_p(s)=4$, corresponds with its multiplicity to
a root of $W_h$ in the closed unit disc.

Every root of a monic integral polynomial is integral:
if $v_p(u)<0$, its leading monomial has strictly smaller
valuation than every lower monomial and cannot cancel.
Over $\mathbf C_p$, therefore, $W_h$ has exactly $d$ roots
in that closed disc, counted with multiplicity. None is
zero by (744.11). The Tate unit has no zeros there.

**Theorem 744.1.** Under (744.1), the original complete Abel
component has exactly $1+d$ zeros on $v_p(s)\ge4$, counted
with multiplicity, of which the center is simple and

$$
\boxed{d\le\eta+2\le3.}
\tag{744.16}
$$

For a noncentral zero $s_i=p^4\Phi^{-1}(u_i)$,

$$
\mathbf Q_p(s_i)=\mathbf Q_p(u_i),\qquad
[\mathbf Q_p(s_i):\mathbf Q_p]\le d\le3.
\tag{744.17}
$$

Indeed $u_i$ is algebraic, and its finite extension of
$\mathbf Q_p$ is complete. Both the rational-coefficient
restricted series $\Phi$ and $\Phi^{-1}$ converge in that
field. Each coordinate consequently belongs to the field
generated by the other. This also proves that rational
$s_i$ correspond exactly to roots $u_i\in\mathbf Z_p$.

## 5. The exact depth budget and its rational consequences

List the noncentral roots with multiplicity. Monicity,
(744.11), and (744.14) give the exact identity

$$
\boxed{
\sum_{i=1}^{d}\bigl(v_p(s_i)-4\bigr)
=\sum_{i=1}^{d}v_p(u_i)=-\mu.
}
\tag{744.18}
$$

Each summand is nonnegative. Combining this with
(744.8)--(744.9) gives the following exhaustive bounds;
a row permits fewer roots when its degree bound is not
attained.

| First valuation $\eta$ | Gauss valuation $\mu$ | Noncentral degree $d$ | Depths of noncentral zeros |
|---|---|---|---|
| $-2$ | $0$ | $0$ | None |
| $-1$ | $0$ | $0$ or $1$ | Every existing zero has depth $4$ |
| $0$ | $-1$ | $1$ | Exactly one zero, of depth $5$ |
| $0$ | $0$ | At most $2$ | Every existing zero has depth $4$ |
| $1$ | $-2$ | $1$ | Exactly one zero, of depth $6$ |
| $1$ | $-1$ | $1$ or $2$ | Sum of depths minus $4$ is $1$ |
| $1$ | $0$ | At most $3$ | Every existing zero has depth $4$ |

When $\mu<0$, the degree cannot be zero because
$v_p(W_h(0))=-\mu>0$ whereas a monic degree-zero polynomial
is one. This explains the equalities in the two linear rows.
Each such linear root belongs to $\mathbf Q_p$.

In the remaining quadratic case $\eta=1,\mu=-1,d=2$, write
$W_h=u^2+cu+e$. One has $v_p(e)=1$. If $c$ is a unit,
the two simple reduction roots lift to two rational roots,
with depths $4$ and $5$. If $c\in p\mathbf Z_p$, the
polynomial is Eisenstein and the two zeros have depth
$9/2$; neither belongs to $\mathbf Q_p$. This alternative
is determined by the actual scaled reduction (744.12),
without inventing an uncomputed coefficient value.

In all cases a rational noncentral zero can have depth only
$4$, $5$, or $6$. The result allows such zeros: it does
not assert that the relevant linear or cubic factors have
no rational roots. No noncentral zero in $\mathbf C_p$
has depth greater than $6$, in agreement with R742's
depth-seven isometry.

## 6. Selection for every sufficiently large allowed prime

For the actual remaining prime classes $p\equiv2,5\pmod9$,
R742 proves that $M_{2,1}\ne0$ and $p\ge2^{160}$ imply
the existence of an original primitive label satisfying
(744.1). R729 establishes this nonvanishing for every
sufficiently large allowed prime. Hence Theorem 744.1
applies to some component of the original quotient for
every such prime.

For $p\ge2^{512}$ with the same nonvanishing premise,
more than $g/16$ of its actual primitive labels satisfy
(744.1), where $g=\varphi(p+1)/2$. Each has its own
canonical polynomial (744.10). These are labelled
components of the original quotient; the statement does
not require the same $h$ for all primes.

The theorem reduces the zeros of one complete Abel
component on the full candidate disc to a polynomial
of degree at most three. Computing that polynomial, or
its needed congruences, remains an actual finite-precision
task with the full tail bound. Most importantly, the
original height exterior products of R634/R724 are
different functions. The noncentral rational-point
exclusion still requires their actual coefficients and
their common-root certificate. Neither the small degree
here nor the absence of an Abel return supplies that
certificate.

## Sources and dependencies

- [R730](R730-fixed-depth-original-Abel-isometry-by-all-embedding-norm.md): original rational jet ratios and the all-order Hodge bound.
- [R742](R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md): original all-order unramified descent, integer first valuation, the actual component selection, and the complete coarse change.
- [R729](R729-uniform-full-Abel-nonvanishing-and-valuation-bound.md): sufficiently large-prime nonvanishing in the same original family.
- [R724](R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md): the separate original height input and its uncompleted common-root certificate.
- Siegfried Bosch, *Lectures on Formal and Rigid Geometry*, [author's April 2008 notes](https://www.uni-muenster.de/IVV5WS/WebHop/user/weckerm/heft378.pdf), §1.2, Theorem 8 and Corollary 9, printed pp. 12–13. The 2014 [Springer edition](https://link.springer.com/book/10.1007/978-3-319-04417-0), LNM 2105, gives the corresponding theorem in §2.2.

No new numerical computation is used. The coefficient bounds,
closed-disc preparation, and complete parameter transport are
proved above for the original series.
