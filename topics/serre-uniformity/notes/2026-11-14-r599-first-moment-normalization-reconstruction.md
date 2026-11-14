# Reconstructing the marked q-principalization first moment

Date: 2026-11-14. **Status: normalization reconstructed and proved;
the principalization and its numerical moment remain unevaluated.**

The public checkpoint refers to an unfinished R599, but does not preserve
its complete first-moment formula. This note therefore defines an explicit
quantity $J_\ell$ from the preserved original principalization conditions.
It does not claim byte-for-byte recovery of a lost R599, and does not
supply an unproved coefficient relating an older symbol $J$ to $b$.

## 1. The same field, prime, norm, and character projector

Keep the original $p=43$, the original 776-bit $q$, the original
$K=\mathbf Q(i)$ and degree-$44$ field $F$, and R591's actual
anti-scalar degree-$43$ field $F_t/F$. The generator is the same
positive $t=1+21pi$ at the first layer. Write
$T=\langle t\rangle$, and keep the original $\tau$-fixed prime
$P_0$ of $F_t$ above the marked prime $\mathfrak q_0$ of $F$.
All $43$ primes above $\mathfrak q_0$ split completely in $F_t/F$.

Put

$$
\alpha_F=1+89460y_F,\qquad
A_\alpha=P_+[\alpha_F],\qquad
P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j.
$$

There is no division by $44$. The coefficient of
$\mathfrak q_0$ in $\operatorname{div}(A_\alpha)$
and of $P_0$ in $P_+P_0$ is one.

All multiplicative expressions below are written additively
in the completed $\mathcal O=\mathbf Z_{43}[i]$ character
module. The intended principalization is

$$
\operatorname{div}_{F_t}(X)=P_+P_0,\qquad
N_TX=A_\alpha.
\tag{J.1}
$$

These are full ordinary divisor equalities. In particular
there are no unrecorded auxiliary prime divisors.

Existence in the completed q-unit lattice follows from the
proved pure-$p$ ordinary results. The character class group
of $F_t$ is zero, so a principalization of $P_+P_0$ exists.
Its norm differs from $A_\alpha$ by an ordinary base unit.
The entire unit lattice is
$E_{F_t}=\mathcal O[T]u_t$, with $N_Tu_t=u$ and
$E_F=\mathcal O u$, so this difference can be removed
by an ordinary unit without changing the divisor.

More explicitly, let $E_q(F_t)$ denote the genuine q-S-unit group,
completed and projected in this same character. The ordinary divisor
sequence on the finite set of q primes is

$$
0\longrightarrow E_{F_t}\longrightarrow E_q(F_t)
\longrightarrow \mathcal O[T]\,P_+P_0
\longrightarrow A_{F_t}\longrightarrow0.
$$

It remains exact: $\mathcal O$ is flat over $\mathbf Z$, the
prime-to-$p$ character projector is an integral direct summand,
and these unit and finite-support divisor modules are finitely
generated. Equivalently their $p$-adic completions give the same
exact finite-support sequence. The last term is zero by R619.
No $\mu_p$ term is hidden in the unit lattice: $F_t$ has absolute
degree $88p$, which is not divisible by $p-1=42$.
Thus the argument takes place in the complete ordinary q-S-unit
lattice and supplies an actual completed principalization, rather
than a point in a semilocal product.

## 2. A definition that includes the q-unit part at the pole

At the fixed completion $(F_t)_{P_0}=K_q$, define

$$
L_j=\ell\bigl(t^jX-\mathbf 1_{j=0}A_\alpha\bigr)
\in k=\mathbf F_{43^2},\qquad 0\le j\le42,
\tag{J.2}
$$

where $\ell$ is exactly the original Weil-normalized
power-residue logarithm. The expression in parentheses
has local valuation zero: only $X$ itself has valuation
one at $P_0$, and all other $t^jX$ have valuation zero
there. Thus (J.2) always evaluates a local unit. It is
also a well-defined homomorphism on the completed local
unit group, so no individual p-adic coefficient is treated
as a literal exponent of a complex algebraic number.

The norm condition gives

$$
\sum_{j=0}^{42}L_j
=\ell(N_TX-A_\alpha)=0.
\tag{J.3}
$$

Define the marked first moment by

$$
\boxed{J_\ell=\sum_{j=0}^{42}jL_j
       =\sum_{j=1}^{42}j\,\ell(t^jX).}
\tag{J.4}
$$

The first expression records the normalized local-unit
vector; the second is equivalent because the missing
pole term has coefficient zero. A future calculation
must retain the original positive $t$ and R591 prime
label when evaluating this sum.

## 3. Independence of the ordinary principalization choice

Suppose $X'$ satisfies the same two conditions (J.1).
Then $e=X'-X$ is an ordinary unit of $F_t$ with norm zero.
Freeness of the complete ordinary lattice
$\mathcal O[T]u_t$ gives

$$
e=(t-1)h\qquad(h\in E_{F_t}).
$$

With $D_T=\sum_{j=0}^{42}jt^j$, the change in (J.4) is

$$
\ell(D_T(t-1)h)=\ell((p-N_T)h)
=-\ell(N_Th).
$$

The norm belongs to $E_F=\mathcal O u$. The original
$\ell(u)=0$ follows also from $u=N_\Gamma y$:
the q extension is totally ramified of degree $p$,
and its residue norm is the pth power. Hence

$$
\boxed{J_\ell(X')=J_\ell(X).}
\tag{J.5}
$$

This argument uses the entire ordinary unit lattice.
It does not permit replacement of $X$ by a local norm
preimage or a field element with additional prime support.

## 4. Reality and the exact conversion of residue conventions

Use the semilinear involution on the chosen character
component, namely complex conjugation together with
conjugation of $\mathcal O$ coefficients. As in R708,
$A_\alpha$ is fixed; the marked $P_0$ is fixed and
$t$ is sent to $t^{-1}$. Averaging any solution of
(J.1) with its conjugate, with coefficient $1/2$,
preserves both exact conditions. By (J.5) it preserves
the moment. We may therefore compute the moment on
an involution-fixed solution.

At the inert q completion, conjugation acts on the
residue field as the qth power, and $q\equiv-1\bmod p$.
For the fixed original Weil root this gives

$$
L_{-j}=-\overline{L_j}.
$$

Reindexing the sum in (J.4) modulo $p$ now gives

$$
\boxed{J_\ell=\overline{J_\ell}\in\mathbf F_{43}.}
\tag{J.6}
$$

If $r_\mu$ denotes the direct exponent in the original
$\mu_{43}$ Weil root, the original relation is
$r_\mu=-2\ell$, not $r_\mu=\ell$. Thus the corresponding
direct-exponent moment is exactly

$$
\boxed{J_r=-2J_\ell.}
\tag{J.7}
$$

Changing the positive generator to $t^a$ would multiply
the first moment by $a^{-1}$; no such change is made.

## 5. The full residue image of ordinary norm-zero corrections

Let $\mathcal W$ be the set of all solutions of (J.1).
For two such solutions, their difference has zero full divisor
and zero norm, hence is an element of
$\ker(N_T:E_{F_t}\to E_F)$.
Conversely adding any element of this kernel preserves both
equations in (J.1). Under the actual integral basis $u_t$,

$$
N_T(h(t)u_t)=h(1)u\qquad(h\in\mathcal O[T]).
$$

Since $u$ is torsion free and primitive, its norm kernel is
exactly the augmentation ideal. Therefore, as a torsor under
the actual completed ordinary unit lattice,

$$
\boxed{\mathcal W=X+(t-1)E_{F_t}.}
\tag{J.8}
$$

This equality proves both inclusions integrally before reducing
any residue coordinate.

Put

$$
R=k[Z]/(Z^{43}-1)=k[Z-1]/(Z-1)^{43},
\qquad I=(Z-1).
$$

Use the coefficient convention

$$
\mathscr A_X(Z)=\sum_{j=0}^{42}L_jZ^{-j},
\qquad
\rho(e)=\sum_{j=0}^{42}\ell(t^je)Z^{-j}
\quad(e\in E_{F_t}).
\tag{J.9}
$$

Negative powers are taken in $R$. This convention is equivariant:
reindexing the finite sum gives $\rho(te)=Z\rho(e)$.
Equation (J.3) gives $\mathscr A_X\in I$, and

$$
\mathscr A_X'(1)=-J_\ell.
$$

For the actual generator $u_t$, R619 equations (619.6)-(619.8)
and the original R198 evaluation state

$$
A_u(Z):=\rho(u_t),\qquad
A_u(1)=0,\qquad A_u'(1)=-13i\ne0.
\tag{J.10}
$$

Thus $A_u=(Z-1)v$ for a unit $v\in R$.
For an arbitrary integral ordinary correction
$e=(t-1)h(t)u_t$, its actual residue vector is

$$
\rho(e)=(Z-1)\overline h(Z)A_u(Z),
$$

where $\overline h$ is reduction modulo $p$.
The reduction map $\mathcal O[T]\to R$ is surjective;
every polynomial in $R$ is the reduction of coefficients
of an element of the genuine completed ordinary unit lattice.
The residue group is finite and killed by $p$, so the continuous
residue map factors through this reduction. It follows that

$$
\boxed{\rho\bigl((t-1)E_{F_t}\bigr)=I^2.}
\tag{J.11}
$$

For clarity, the reverse inclusion is constructive: given
$(Z-1)^2g(Z)\in I^2$, choose $\overline h=g v^{-1}$,
lift its $43$ coefficients to $\mathcal O$, and use the
ordinary norm-zero unit $(t-1)h(t)u_t$.
No dimension count or local replacement of the unit lattice
is used.

Combining (J.8) and (J.11) gives the exact full image

$$
\boxed{
\{\mathscr A_{X'}:X'\in\mathcal W\}
=\mathscr A_X+I^2,\qquad
\mathscr A_X\bmod I^2=-J_\ell(Z-1).
}
\tag{J.12}
$$

Hence $J_\ell$ is the complete remaining coordinate after fixing
the original divisor and norm. The higher $41$ residue coordinates
can all be changed by actual ordinary norm-zero units.
In particular there exists a witness in $\mathcal W$ whose
whole residue vector is exactly $-J_\ell(Z-1)$.
Its only possibly nonzero coefficients are $L_0=J_\ell$ and
$L_{42}=-J_\ell$. This is an existence statement, not an
evaluation or a coordinate construction of that witness.

## 6. Exact zero test and the base-unit norm correction

The complete image calculation proves

$$
\boxed{
J_\ell=0
\iff
\text{some }X\in\mathcal W\text{ has }L_j=0
\text{ for every }0\le j\le42.
}
\tag{J.13}
$$

Equivalently, all the indicated normalized local-unit residue
classes are $43$rd powers, while the full ordinary divisor and
exact norm in (J.1) remain fixed. This asserts only the residue
conditions displayed in (J.2); it does not silently add a local
norm condition on the removed uniformizer.

If the exact norm is allowed to change by an ordinary base unit,
a correction $e=h(t)u_t$ always kills the whole normalized residue
vector: $(A_u)=I$ and $\mathscr A_X\in I$ imply that

$$
\overline h(Z)A_u(Z)=-\mathscr A_X(Z)
$$

has a solution in $R$. Lift it to $\mathcal O[T]$ and write
$c=h(1)\in\mathcal O$. Then

$$
\operatorname{div}(X+e)=P_+P_0,\qquad
N_T(X+e)=A_\alpha+c u.
$$

Differentiation at $Z=1$, with the signs in (J.9)-(J.10), yields

$$
\boxed{c\bmod p=-\frac{J_\ell}{13i}.}
\tag{J.14}
$$

Every residue-killing ordinary correction has this same
augmentation modulo $p$. Indeed
$\operatorname{Ann}_R(A_u)=I^{42}=kN_T$, and the augmentation
of $N_T$ is $43=0$ in $k$. Conversely the solution above always
lifts to an ordinary correction, so (J.14) is the exact required
mod-$p$ base-unit norm change. Since $J_\ell\in\mathbf F_{43}$,
the displayed coefficient belongs to $i\mathbf F_{43}$.

## 7. The original finite-flat normalization gives the counterterm 18

This comparison uses R185's actual classes and the same unit,
rather than an arbitrary generator of the ordinary unit line.

R185 (185.22)-(185.23) uses

$$
u_0=N_{K(A[p])/F}
\left(\frac{64^{10}}{\psi_{11,A}(P_2+P)}\right),
\qquad P_2=(i,1-i),
$$

with the original real $P$ and original $q$ embedding.
This is precisely the scalar norm underlying the $u_0$ of
R198/R613, since $\Delta_A=64$ and the marked point and function
agree. Thus its unaveraged field-character coefficient is
the same $u=P_+[u_0]$ used in (J.1)-(J.14), with
$N_Tu_t=u$. No new generator of $E_F$ is chosen.

To check the coefficient scale, R185 defines

$$
\mathcal B(a)=\sum_{j=0}^{43}[\sigma^ja]\otimes D_{\omega^j},
\qquad
\mathcal J(D_z)=D_{iz},
$$

and gives the exact mod-$p$ Kummer normalization

$$
d_p^{\mathrm{Rob}}=\frac1{1848}\mathcal J\mathcal B(u_0).
\tag{J.15}
$$

On the selected field-character summand, the coefficient of
$\mathcal B(u_0)$ is $P_+[u_0]=u$ and applying $\mathcal J$
multiplies that coefficient by $i$. This follows term by term
from $D_{\omega^j}\mapsto D_{i\omega^j}$.
The coefficient of the same unaveraged $\mathcal B(\alpha_F)$
is $A_\alpha$, so R185's $d_q$ is the class of precisely this
norm target. Consequently the two coefficients being compared are

$$
d_q\longleftrightarrow A_\alpha,\qquad
d_p^{\mathrm{Rob}}\longleftrightarrow\frac{i}{1848}u
\equiv-i u\pmod p.
\tag{J.16}
$$

There is no factor $1/44$ in either identification.
This is a comparison of the actual Kummer classes before local
evaluation, so no additional Frobenius restriction factor $1/2$
is introduced.

R185 computes the local Artin--Hasse coordinates
$(20,29)$ for $d_q$ and $(24,20)$ for $d_p^{\mathrm{Rob}}$.
Its finite-flat annihilator is the second coordinate line.
Therefore the exact mod-$p$ correction is
$d_q-8d_p^{\mathrm{Rob}}$, since $20/24=8$.
An integral completed norm target and witness representing
this correction are

$$
A_{\alpha,\mathrm{fl}}
=A_\alpha-\frac{8i}{1848}u,\qquad
X_{\mathrm{fl}}=X-\frac{8i}{1848}u_t.
\tag{J.17}
$$

Their full divisor and exact norm satisfy

$$
\operatorname{div}X_{\mathrm{fl}}=P_+P_0,\qquad
N_TX_{\mathrm{fl}}=A_{\alpha,\mathrm{fl}}.
$$

Only the mod-$p$ finite-flat class is being specified by R185;
a different integral lift of its coefficient changes (J.17)
by a multiple of $p$ of an ordinary unit and does not change
the residue moment below.

Define $J_{\mathrm{fl}}$ by the formula (J.4), using the
pair $(X_{\mathrm{fl}},A_{\alpha,\mathrm{fl}})$.
The correction at $j=0$ still makes a local unit.
It has coefficient zero in the first moment, and
$\ell(u)=0$ also shows that its change contributes no extra
term to the normalized residue vector.
Using the actual R198 value $\ell(D_Tu_t)=13i$ gives

$$
\boxed{
J_{\mathrm{fl}}
=J_\ell-\frac{8i}{1848}(13i)
=J_\ell-18\quad\hbox{in }\mathbf F_{43}.
}
\tag{J.18}
$$

Indeed $1848\equiv-1\bmod43$, so the coefficient of $u_t$
in (J.17) is $8i$ modulo $43$, and $8i\cdot13i=-104=-18$.
The semilinear marking is also preserved:
R185 has $\tau u_0=\sigma^{22}u_0$, hence
$\tau u=-u$ in this character, while $8i/1848$ changes sign.
Thus the correction to the fixed $A_\alpha$ is itself fixed
under the same semilinear involution.

More generally changing a norm target by $d u$ and its witness
by $d u_t$ changes this first moment by $13i\,d$ modulo $p$.
The fixed principal divisor alone does not determine the raw
moment; the original norm target is essential. Formula (J.18)
records the correction for the actual finite-flat normalization.

Neither $J_\ell$ nor $J_{\mathrm{fl}}$ has been numerically
evaluated. In particular this argument does not identify
$J_{\mathrm{fl}}=0$ with the original $b=24$ condition.
The additional chain comparison remains necessary.

## 8. Identification with the actual pure-p dual cup primitive

This paragraph identifies a genuine marked cochain value. It does
not exchange the two different cup products that occur below.

Write $d_q=\mathcal B(\alpha_F)$ and
$d_0=d_p^{\mathrm{Rob}}$ in the notation of R185. Thus their
$\chi^-$ scalar norm targets are $A_\alpha$ and
$(i/1848)u$, respectively. Let $e_p(d)$ denote an
$S$-supported primitive for the actual dual action

$$
\delta e_p(d)=-i\kappa_p\cup d,
\qquad S=\{2,p,q,\infty\}.
\tag{J.19}
$$

Choose the primitive obtained from the specified ordinary Norm
witness. With the original real branch and positive arithmetic
Artin convention, its full $q$ localization is

$$
\boxed{
e_p(d_q)|_q=\frac{J_\ell}{2}K_0,\qquad
e_p(d_q-8d_0)|_q=\frac{J_\ell-18}{2}K_0,
}
\tag{J.20}
$$

with zero singular coordinate in both cases. Here $K_0$ is
exactly the finite basis vector for $W(1)$ of R168/R198/R200;
the factors $1/2$ are in $\mathbf F_{43}$.

### 8.1 The positive Norm primitive and its sign

For an actual cyclic Norm pair $N_TX=U$, R191 (191.9)-(191.10)
uses

$$
B_j=\prod_{k<j}t^kX,\qquad
A_X=\prod_{k=0}^{p-1}(t^kX)^k,\qquad
a^p=A_X,\quad \beta^p=U.
$$

If $c(g)\in\{0,\ldots,p-1\}$ represents $\kappa_p(g)$, its
explicit cochain is

$$
Q(g)=\frac{aB_{c(g)}}{g(a)(g\beta)^{c(g)}}.
$$

It has $\delta Q=\kappa_p\cup\kappa(U)$. At a place split in
the $T$ extension one has $c(g)=0$, so

$$
Q|_v=-\kappa(A_X)=-\kappa(D_TX)|_v,
\qquad D_T=\sum_{j=0}^{42}jt^j.
\tag{J.21}
$$

This fixes the minus sign before multiplication by the actual
coefficient $-i$. It is the same positive Norm primitive used
in R198, not a derivative with a separately chosen sign.

The argument also applies to the completed $\chi^-$ witnesses
in this note. The $q$-unit group is finitely generated, and
tensoring with $\mathcal O$ followed by reduction modulo $p$
is represented by finite linear combinations of actual
$q$-units. Choose such representatives for $X$ and take their
actual norms. Their base Kummer class is the class of
$A_\alpha$, by the exact completed norm identity. Apply
(191.9) term by term and take the same character projection.
Changing the chosen representative of the base Kummer
cocycle changes a primitive by the corresponding cup with a
zero-cochain. This correction restricts to zero at the
specified split $q$ branch because $\kappa_p$ is zero there.
Thus (J.21) and its local finite value are independent of
these integral representatives. All actual representatives
are $q$-units, and the $T$ extension is ramified only at $p$,
so this construction retains the stated $S$ support.

### 8.2 The local pole, Kummer logarithm, and quadratic restriction

The full divisor condition gives

$$
\operatorname{ord}_{P_0}(D_TX)=0.
$$

Indeed only $X$ itself, the $j=0$ term, has a pole or zero at
the marked $P_0$ among these $T$ translates, and its
coefficient in $D_T$ is zero. The other character translates
are at the other marked $q$ primes. Consequently $D_TX$ is
an ordinary local unit at $P_0$ and

$$
\ell(D_TX)=J_\ell.
\tag{J.22}
$$

For the residue field $\mathbf F_{q^2}$, positive arithmetic
Frobenius acts on a $p$th root of a local unit $v$ by the
exponent

$$
\log_\zeta\bigl(\bar v^{(q^2-1)/p}\bigr)=\ell(v).
$$

Thus the scalar finite Kummer value of (J.21) is $-J_\ell$.
Multiplication by the actual dual coefficient $-i$ gives
$iJ_\ell$.

In the original Weil basis, the finite dual vector
$K_0=JF_0$ has $\chi^-$ scalar $i$ at the unramified
quadratic field $k_q=\mathbf Q_{q^2}$, whereas the singular
dual vector $F_0$ has scalar $1$. Hence $iJ_\ell$ is the
finite coefficient $J_\ell$ over $k_q$. Restriction from
$\mathbf Q_q$ to $k_q$ multiplies this finite coefficient
by $2$. Its inverse exists modulo $43$, giving the first
identity of (J.20). The vanishing valuation proves the
zero singular coordinate, and the original real branch
and $J_\ell\in\mathbf F_{43}$ give the same descent under
complex conjugation.

The identical computation for $X_{\mathrm{fl}}$ gives the
second identity. It can also be checked against the
already published exact normalization

$$
e_p(d_0)|_q=28K_0.
$$

Indeed $J_{\mathrm{fl}}=J_\ell-18$, and

$$
\frac{J_\ell}{2}-8\cdot28
=\frac{J_\ell-18}{2}\pmod {43}.
$$

This check retains $1848^{-1}$, the coefficient $i$ in
$d_0$, the positive primitive's minus sign, the actual
coefficient $-i$, and the quadratic restriction factor.
No average by $44$ is inserted.

### 8.3 The exact secondary pairing that has now been identified

R200 uses the original primal finite/singular coordinates

$$
w_q=(27\varepsilon,-\varepsilon)
$$

and the pairing $2(ad-bc)$. Therefore (J.20) gives

$$
\boxed{
\left\langle w_q,e_p(d_q-8d_0)|_q\right\rangle_q
=\varepsilon(J_\ell-18).
}
\tag{J.23}
$$

A different supported primitive adds a global dual class.
Its $q$ localization lies on the original line with
finite/singular slope $\lambda_q=16$, spanned by
$d_q|_q$, while $d_0|_q=0$. Since $w_q$ has the same
slope, this change has zero pairing with $w_q$.
Thus (J.23) is a well-defined secondary pairing, not just
a value attached to arbitrary roots. The specified Norm
witness selects the representative with zero singular
coordinate used in (J.20).

The original obstruction is instead

$$
\Omega_2=
\left\langle w_q,e_p(d_0)|_q+e_q(d_0)|_q\right\rangle_q,
\qquad
\delta e_q(d_0)=-2i\kappa_q\cup d_0.
\tag{J.24}
$$

Equations (J.23) and (J.24) involve different dual targets
and different cyclic characters. No cochain identity
exchanging $e_p(d_q)$ with $e_q(d_0)$ has been proved
here. Such an identity, including its supported and
local normalization terms, is still needed to turn
(J.23) into a numerical formula for $b$ or $\Omega_2$.

## 9. What is still required

The quantity (J.4) is fixed by the actual field,
ordinary divisor, norm, prime label, and residue
convention. Its value has not been computed. Equations (J.11)-(J.14)
identify the entire ordinary residue ambiguity, and (J.18)
fixes the finite-flat counterterm. Equations (J.20)-(J.23) identify
its actual pure-$p$ dual primitive and secondary pairing. The principalization existence proof does not supply a numerical
first moment or a principalization's coordinates.

R720 proves the original ordinary bridge
$C=9ib$ and
$\Omega_2=\varepsilon(22+17b)$; hence this last
obstruction vanishes exactly at $b=24$.
That critical value is not the numerical value of
the actual $b$, and is not identified with R204's
separate primal reference value $24$.

A further exact comparison is required before
assigning a coefficient connecting this explicit
$J_\ell$ to $b$ or to a lost, incompletely normalized
R599 symbol. No such coefficient is asserted here.

Dependencies: the explicit positive Norm primitive of
[R191](../results/R191-cyclotomic-principalization-and-eta-ray-field.md),
the original pure-$p$ calibration of
[R198](../results/R198-p-squared-robert-norm-and-a-secondary-contribution.md),
and the full supported secondary reciprocity of
[R200](../results/R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md);
the actual unit, unaveraged Kummer classes and finite-flat
normalization of
[R185](../results/R185-p-local-robert-and-principal-unit-coordinates.md);
the actual marked field and prime of
[R591](../results/R591-explicit-marked-anti-p-field-and-relative-maximal-order.md);
the pure-$p$ ordinary lattices and class vanishing in
[R619](../results/R619-ordinary-anti-p-class-group-and-actual-artin-nine.md),
[R657](../results/R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md),
and
[R686](../results/R686-all-p-power-layers-and-exact-ordinary-class-growth-law.md);
the fixed semilinear marking in
[R708](../results/R708-exact-isogeny-compression-and-the-43-valued-local-norm-fiber.md);
and the actual chain bridge in
[R720](../results/R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md).
