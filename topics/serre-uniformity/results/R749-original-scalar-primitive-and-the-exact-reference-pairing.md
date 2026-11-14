# R749: the original scalar primitive and the exact reference pairing

Date: 2026-11-14. **Status: proved.** The only numerical input is the
already published original scalar Robert calculation in R561. This
result uses that calculation to evaluate the cyclotomic primitive in
R200's complete $p^2$ Kummer-zero gauge. It makes no new finite-field
calculation and evaluates neither $J_\ell$ nor the ordinary coefficient
$b$.

Retain the original $p=43$, the original marked $776$-bit prime $q$,
the original CM and Weil identifications, and positive arithmetic
Frobenius. Let $d_0=d_p^{\rm Rob}$ and let $w$ be the original strict-$p$
primal class. In R168's rational local coordinates,

$$
w_q=(-16\varepsilon,-\varepsilon),\qquad d_{0,q}=0.
$$

There is a primitive $e_c$ supported on $\{2,p,\infty\}$ with

$$
\delta e_c=-\ell_{\rm cyc}\cup d_0
$$

whose localization, after the complete Kummer-zero normalization of
R200, is

$$
\boxed{e_{c,q}=26K_0,\qquad
       \langle w_q,e_{c,q}\rangle_q=9\varepsilon.}
\tag{749.1}
$$

Consequently the original Kummer reference class $z_0$ of R200 satisfies

$$
\boxed{\langle z_0,d_{0,p}\rangle_p=9\varepsilon.}
\tag{749.2}
$$

For a primitive with the larger support $\{2,p,q,\infty\}$, the first
formula in (749.1) is understood modulo the original global dual
localization line $\mathbf F_{43}(16,1)$. The pairing and (749.2) have
no such choice dependence.

## 1. The actual scalar witness and its original phase

Put $K=\mathbf Q(i)$,

$$
F=K(A[p])^{\mathbf F_p^\times},\qquad
B=K(A[p^2])^{\mu_{42}},\qquad F_s=B^T.
$$

Here $S=\langle s\rangle$ is the original scalar group with $s=1+p$,
and $T$ is the original anti-scalar group. All completed character
modules below use the actual tame lift and the unaveraged projector

$$
P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j.
$$

Write $u=P_+u_0$ and let $u_s$ be the actual scalar Robert witness
recovered in R561. Its exact ordinary-unit identity is

$$
N_Su_s=u.
\tag{749.3}
$$

R185 and R198 fix the normalization of the original dual class as

$$
d_0=\frac{i}{1848}\,\kappa(u),\qquad
\frac{i}{1848}\equiv-i\pmod {43},
\tag{749.4}
$$

with the same coefficient-component interpretation of $\kappa$ as in
R198 (198.16). Thus (749.4) contains neither a change of Robert
generator nor a division by $44$.

Let $K_q=\mathbf Q_{q^2}$ be the marked quadratic completion of $K$.
The original positive Frobenius satisfies

$$
\operatorname{Fr}_{q^2}|_{F_s}=s^{32}.
\tag{749.5}
$$

The scalar completion is the unramified extension of $K_q$ of degree
$p$. On its $\mu_{p^2}$, the action of $s$ is $1+2p$.
These statements use the actual CM Frobenius $[-q]$, not a freely
chosen generator of the scalar group. In particular

$$
v_p(q^2-1)=1,\qquad v_p(q^{2p}-1)=2.
\tag{749.6}
$$

Let $r_\mu$ denote the exponent of the $p$-primary Teichmüller part,
measured in the original Weil root $\zeta$. R561, §5 and §8.4,
proves

$$
\text{the $p$-primary residue of }u_s=\zeta^{25}.
\tag{749.7}
$$

This is an exponent in $\mu_p\subset\mu_{p^2}$, rather than an exponent
of a chosen primitive $p^2$-th root. In the published calculation the
high power-residue exponent is $9$, and the high exponent reduces to
$21$ on $\mu_p$. Hence the direct phase is $21^{-1}9=-2\cdot9=25$.
The same certificate verifies all $44$ exact norm ratios, the actual
tame-lift correction, and the $p^2$ closure. We use that complete
marked result.

The ordinary norm in (749.3) sends this phase to
$\zeta^{25p}=1$. Therefore $u$ has zero $p$-primary phase at the
marked bottom completion. No unknown ordinary norm preimage is
being used in this assertion.

## 2. What the complete $p^2$ Kummer-zero gauge requires

The distinction between a $p$-th root and a $p^2$-compatible root is
essential here, because the scalar character is nonzero at $q$.

At the bottom completion the $p$-primary subgroup of the residue
units is exactly $\mu_p$, by (749.6). Taking a $p^2$-th power
annihilates that subgroup, and is an automorphism on the
prime-to-$p$ residue part and on the principal $q$-adic units.
Since the phase of $u$ is zero, it has a local $p^2$-th root with
zero $p$-primary phase. If this root is denoted by $\alpha$, the
root

$$
\beta=\alpha^p,\qquad \beta^p=u
\tag{749.8}
$$

has phase zero. Conversely, the $p$-th roots $\beta\zeta^a$ with
$a\ne0$ do not arise by this construction in the bottom local
field: a $p$-th power there has trivial $p$-primary phase.
Thus the complete Kummer-zero condition fixes the phase of
$\beta$ to be zero.

This is precisely the normalization of R200, §3, for the original
$D/p^2$ Kummer lift, not an additional local choice. Indeed its
unramified $K_0$-line has quotient

$$
(\mathbf Z/p^2)K_0/(-q-1)K_0,
$$

whose reduction to the mod-$p$ unramified cohomology is an
isomorphism. The original class $d_0$ is zero there, so its complete
lift is a coboundary. A killing $0$-cochain is unique modulo $p$:
the invariants of $D/p^2$ reduce to zero. In the unit realization
this is exactly (749.8). Multiplication by the original
$i/1848$ and the original character projection preserve that
normalization.

The displayed root notation can be interpreted componentwise
before completing and applying $P_+$. At level $p^2$, only the
coefficients modulo $p^2$ enter the Kummer construction. Thus no
formal $p$-adic group-ring exponent is treated as an unconstructed
algebraic number.

## 3. The positive norm primitive at an unramified scalar point

We recall the actual sign and evaluate it directly, rather than
using the split-point formula for the anti-scalar direction.
For a cyclic extension of order $p$, generator $s$, and an
ordinary unit $X$ with $N_SX=U$, put, in multiplicative notation,

$$
B_j=\prod_{h=0}^{j-1}s^hX,\qquad
A_X=\prod_{h=0}^{p-1}(s^hX)^h,\qquad
a^p=A_X,\quad \beta^p=U.
$$

For the representative $c(g)\in\{0,\ldots,p-1\}$ of the scalar
exponent, R191 (191.9) is

$$
Q_X(g)=
\frac{aB_{c(g)}}{g(a)(g\beta)^{c(g)}}\in\mu_p.
\tag{749.9}
$$

The elementary identity

$$
B_j\,s^jB_h
=B_{j+h\bmod p}\,U^{\lfloor(j+h)/p\rfloor}
$$

gives

$$
\delta Q_X=\kappa_S\cup\kappa(U).
\tag{749.10}
$$

In particular this is the positive cup primitive. The expression
$-\kappa(A_X)$, valid at a locally split scalar extension, is not
used at the present unramified point.

Take $X=u_s$ and $U=u$. By (749.7), every $s^hX$ has the same phase
$\zeta^{25}$, because $s$ fixes $\mu_p$. Therefore

$$
r_\mu(B_{32})=32\cdot25=26,\qquad
r_\mu(A_X)=25\sum_{h=0}^{42}h=0.
\tag{749.11}
$$

The second equality is an exact statement that the $p$-primary
residue part of $A_X$ is trivial. Consequently the $p$-primary
phase of any $p$-th root $a$ lies in $\mu_p$.
The Frobenius $g=\operatorname{Fr}_{q^2}$ fixes that group, so
$a/g(a)$ contributes zero phase. The root $\beta$ in §2 has
phase zero, and so does $g\beta$. Taking the phase in (749.9)
now gives

$$
\boxed{Q_{u_s}(\operatorname{Fr}_{q^2})=26.}
\tag{749.12}
$$

Here and below a value in $\mu_p$ is written additively using the
original Weil identification. The quotient in (749.9) is already
in $\mu_p$, so reading its phase determines the value, not merely
one component of a possibly non-torsion unit.

All roots needed in this calculation can be taken in the maximal
unramified extension at $q$: they are roots of units and $q\ne p$.
The scalar extension is also unramified there. Thus (749.9) is
zero on local inertia in the Kummer-zero gauge, and the primitive
has zero singular coordinate.

## 4. The actual scalar coefficient, support, and rational restriction

The CM determinant on $s=1+p$ is $(1+p)^2$, and the original
anti-scalar direction has zero determinant logarithm. With the
actual tame lift removed, this gives the same identity as
R746 (746.1),

$$
\ell_{\rm cyc}=2\kappa_S.
\tag{749.13}
$$

Combine (749.4), (749.10), and (749.13). On the original
coefficient component a cyclotomic primitive is

$$
e_c=-\,2\,\frac{i}{1848}Q_{u_s}.
\tag{749.14}
$$

The construction is global with support $\{2,p,\infty\}$:
the original scalar extension and the Kummer extensions of its
ordinary Robert units are unramified away from $2,p$.
Taking the original tame character and conjugate pair, then
descending through the prime-to-$p$ group, preserves
(749.10) and this support. Equivalently this is the same
equivariant Kummer construction as R198, applied to the scalar
norm instead of the anti-scalar norm. Its local descent is fixed
by the original CM and Weil identifications.

From (749.12) and $1848^{-1}=-1$ modulo $43$, its finite value
on the quadratic local field is

$$
e_c(\operatorname{Fr}_{q^2})
=(-2)(-i)\cdot26=9i.
\tag{749.15}
$$

In the original identification the $i$-direction here is the
rational finite basis $K_0$. Restriction from $\mathbf Q_q$
to $K_q$ doubles that finite coordinate. Therefore

$$
e_{c,q}=(9/2)K_0=26K_0,
$$

with singular coordinate zero. This is the only division by $2$.
It is the same restriction convention used in R198 (198.17),
where $13i$ on $K_q$ becomes $(13/2)K_0$ on $\mathbf Q_q$.
Neither the scalar coefficient $2$ in (749.13) nor the local
restriction factor is omitted.

Two primitives with support $\{2,p,\infty\}$ differ by a class
in $\mathbf F_{43}d_0$, by R743 (743.5), and $d_{0,q}=0$.
Thus the displayed unramified local value is independent of
the remaining minimal-support choices. For support
$\{2,p,q,\infty\}$ the full dual space is
$\mathbf F_{43}d_0\oplus\mathbf F_{43}d_q$,
and $d_q$ has local coordinates $(16,1)$. This proves the
choice statement following (749.2).

## 5. The exact reference pairing and its independence

The original local Tate pairing in these coordinates is

$$
\langle(a,b),(c,d)\rangle_q=2(ad-bc).
$$

Substituting $w_q=(-16\varepsilon,-\varepsilon)$ and
$e_{c,q}=(26,0)$ gives

$$
\langle w_q,e_{c,q}\rangle_q
=2\bigl(0-(-\varepsilon)26\bigr)
=52\varepsilon=9\varepsilon.
\tag{749.16}
$$

Adding any multiple of $(16,1)$ to $e_{c,q}$ does not change
this pairing, since
$2((-16\varepsilon)\cdot1-(-\varepsilon)\cdot16)=0$.

For completeness, retain R200's exact-dual argument. Its
reference lattices are

$$
P=\chi_{\rm cyc}\omega^{-1}T,\qquad
D=\chi_{\rm cyc}T,\qquad
D'=\omega T=P^\vee(1).
$$

For the original supported Kummer lifts,
$\widetilde w_p=pz_0$ and $\widetilde d_q=0$ in the complete
Kummer-zero gauge. Since
$D'=D(1-p\ell_{\rm cyc})$ modulo $p^2$,

$$
\widetilde d'=\widetilde d-pe_c
$$

is a cocycle for the exact dual $D'/p^2$.
The global integral cup product
$\operatorname{tr}(\widetilde w\cup\widetilde d')$
has local contributions
$p\langle z_0,d_{0,p}\rangle_p$ at $p$ and
$-p\langle w_q,e_{c,q}\rangle_q$ at $q$.
The $2$-local cohomology vanishes and the remaining terms
are unramified, as in R200, §7. Global reciprocity therefore
gives

$$
\langle z_0,d_{0,p}\rangle_p
=\langle w_q,e_{c,q}\rangle_q
=9\varepsilon.
$$

This proves (749.2). It computes the pairing of the real
reference class; it does not set that local class equal to
zero.

## 6. Compatibility and the remaining ordinary/flat comparison

R746 gives
$\langle D_{0,p},d_{0,p}\rangle_p=26\varepsilon b$
and
$\langle\mathfrak b_p(w)_p,d_{0,p}\rangle_p=-13\varepsilon$.
The actual mixed-characteristic primitive in R200 is
$D_0+\mathfrak b_p(w)$, rather than $D_b$. Consequently
(749.2) recovers, with all constants fixed,

$$
\begin{split}
\Omega_2
&=9\varepsilon-
  \bigl(26\varepsilon b-13\varepsilon\bigr)\\
&=\varepsilon(22+17b)
 =\varepsilon(10-\mathcal L),
\qquad \mathcal L=31+26b.
\end{split}
\tag{749.17}
$$

This is consistent with the independent ordinary chain comparison
of R720. The proof of (749.1)--(749.2) used only the original
scalar witness, the full Kummer gauge, and exact-dual
reciprocity; it did not infer the scalar value from (749.17).

R743's first moment instead tests the finite-flat dual vector
$d_q-8d_0$, whose $p$ coordinates are $(0,41)$.
The ordinary condition in R746 and the reference pairing
above test $d_{0,p}=(24,20)$. These are different functionals.
The new exact scalar value supplies no identification of
them, and neither $J_\ell-18$ nor $b-24$ is evaluated here.
Their true exchange comparison remains a separate problem.

## Sources in the same original normalization

- [R185](R185-p-local-robert-and-principal-unit-coordinates.md),
  especially (185.27)--(185.28): the exact original Robert coefficient.
- [R191](R191-cyclotomic-principalization-and-eta-ray-field.md),
  §5: the positive norm primitive and its direct cochain proof.
- [R198](R198-p-squared-robert-norm-and-a-secondary-contribution.md),
  §5: the same coefficient and the rational restriction convention.
- [R200](R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md),
  §§3 and 7: the full Kummer-zero gauge and exact-dual reciprocity.
- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md),
  §§1, 5, 8.4: the actual scalar extension, Frobenius, ordinary
  norm witness, and phase $25$.
- [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md):
  the independently proved original ordinary coefficient.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md)
  and [R746](R746-original-ordinary-coefficient-as-a-strict-p-bockstein-condition.md):
  the complete supported spaces and the two distinct local conditions.
