# R750 — Global real descent of all original flat jets

Date: 2026-11-14. **Status: proved.**

All the allowed flat jets of one original positive component lie
on a single explicitly normalized line over the original real
cyclotomic coefficient field. This strengthens R742's local
unramified descent and R747's first-jet global descent to every
order, including when the first jet vanishes. The proof computes
one actual tame reciprocity action; it does not infer a global
field statement from a single $p$-adic rationality statement.

## 1. Statement in the original normalization

Let $p\ge41$, $p\equiv5\pmod6$, and put

$$
n=p+1,\qquad A=\mathbf Q(\zeta_n),\qquad
F_0=A^+,\qquad K=\mathbf Q(\zeta),\qquad
\zeta^2+\zeta+1=0.
\tag{750.1}
$$

Retain the original positive complex embedding of $\zeta$, the
positive real number $\alpha=\sqrt[3]4$, and

$$
u_0=1-\zeta^2.
$$

Fix an actual primitive positive label
$h\equiv1\pmod6$, $(h,n)=1$. Every $M_{m,h}$ below is the
unchanged flat jet of R588/R727/R742. The original cusp scale,
finite Cartan vector, six-level vector, period and CM marking
are retained together.

**Theorem 750.1.** For every $j\ge1$,

$$
\boxed{
M_{3j-1,h}\in A(\alpha),\qquad
\alpha M_{3j-1,h}\in A,\qquad
\mathcal T_{j,h}:=\frac{\alpha M_{3j-1,h}}{u_0}\in F_0.
}
\tag{750.2}
$$

All these assertions allow a zero jet. If an allowed jet
$M_{3\ell-1,h}$ is nonzero, then

$$
\boxed{
\frac{M_{3j-1,h}}{M_{3\ell-1,h}}\in F_0
\quad\text{for every }j\ge1.
}
\tag{750.3}
$$

The coefficient conjugates preserve the signs in every order:

$$
\mathcal T_{j,h}=\sigma_h(\mathcal T_{j,1}),
\tag{750.4}
$$

where $\sigma_h$ is the original positive embedding of $F_0$.
For $j=1$, R747's number is exactly
$T_h=(n/144)\mathcal T_{1,h}$. No independent square-root
selection is made in (750.2) or (750.4).

## 2. Every allowed jet has the same analytic level and coefficient field

Let $F_h$ be the actual raw weight-two form fixed in R742,
and let $X=E_2^*$. Its full raising expansion is

$$
\delta_2^mF_h=\sum_{r=0}^m A_{m,r}X^r,
\qquad \operatorname{wt}(A_{m,r})=2+2m-2r.
\tag{750.5}
$$

R742 proves the genuine modular recurrence, with $k=2+2m$,

$$
A_{m+1,r}=
\partial_{k-2r}A_{m,r}
 +\frac{k-r+1}{12}A_{m,r-1}
 -\frac{r+1}{12}E_4A_{m,r+1}.
\tag{750.6}
$$

Every term retains analytic full level $6p$ and has Fourier
coefficients in $A(\zeta_{6p})$. This follows from the original
finite-type Fourier realization and the rational Fourier
coefficients of $E_2,E_4$. For $m=3j-1$, put

$$
\mathfrak J_{j,h}=A_{3j-1,0}/E_6^j.
\tag{750.7}
$$

This is a weight-zero modular function, finite at $\zeta$,
and the exact original period comparison is

$$
M_{3j-1,h}=(-864)^j\mathfrak J_{j,h}(\zeta).
\tag{750.8}
$$

The $q$-expansion descent used in R747 applies at every
order and gives $\mathfrak J_{j,h}\in A\mathcal F_{6p}$.
Write $E=K_{6p}$ and $B=K_6$ for the same ray class fields.
The finite CM value in (750.8) therefore lies in $AE$.

R742 proves that the whole $p$ inertia subgroup fixes
every one of these functions at the original CM point,
using the complete arithmetic Cartan action. R747 proves
the exact global field identities

$$
B=K(\alpha),\quad A\cap E=K,\quad
(AE)^{I_p}=AB=A(\alpha),\quad [AB:A]=3.
\tag{750.9}
$$

It follows that $M_{3j-1,h}\in AB$ for every $j$. This
uses the complete global inertia fixed field, including
the conductor-six part, and is valid independently of
the value of $M_{2,h}$.

## 3. One specified tame idele fixes the whole coefficient field

Choose the finite idele $x$ of $K$ by

$$
x_2=\zeta\in\mathcal O_{K_2}^{\times},\qquad
x_v=1\quad(v\ne2).
\tag{750.10}
$$

At the inert prime two its local norm is
$\zeta\zeta^2=1$. Thus the idele norm to $\mathbf Q$ is
identically one. Reciprocity is compatible with this
norm, so $\operatorname{Art}_K(x)$ fixes every cyclotomic
constant, in particular $A$.

Equivalently, in the arithmetic modular-function action
the determinant of the reciprocity matrix is one at
every finite place. Its action on the cyclotomic constant
field is therefore trivial. This argument also treats
the primes dividing $n$; the coefficient field is not
silently assumed to be unramified at two.

In the right-action convention used in R742, the CM
reciprocity matrix is $g_\zeta(x^{-1})$. Since
$\zeta^{-1}=\zeta^2=-1-\zeta$, its two-component is

$$
g_\zeta(\zeta^2)
=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}
\equiv C:=\begin{pmatrix}0&1\\1&1\end{pmatrix}\pmod2.
\tag{750.11}
$$

Its components at three and at $p$ are identity. Its
determinant is one. For functions of level $6p$, a lift
in $\mathrm{SL}_2(\mathbf Z)$ with these congruences gives
the same arithmetic action. Let $\sigma$ denote the
restriction of this actual Artin action to $AB$.

## 4. Compute its action on the positive cube root

R747 identifies the positive tame root as the value of
the full-level-six weight-zero function

$$
R_6(\tau)=
\frac{\wp_{\mathbf Z+\mathbf Z\tau}(1/3)}
     {\wp_{\mathbf Z+\mathbf Z\tau}(1/2)},\qquad
R_6(\zeta)=\alpha.
\tag{750.12}
$$

Here is the right torsion-label action, with its direction
made explicit. If a torsion argument is $r\tau+s$ and
$g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$,
the weight-two slash of the corresponding $\wp$ value
has argument

$$
(ra+sc)\tau+(rb+sd).
\tag{750.13}
$$

Thus the row label $(r,s)$ is multiplied on the right by
$g$. The common weight factor cancels in the quotient.

The numerator label $(0,1/3)$ is fixed by the identity
three-component. The denominator label $(0,1/2)$ is
sent by $C$ to $(1/2,1/2)$. On the original curve
$E_0:y^2=x^3-1$, with $x=\wp_{\Omega\mathbf Z[\zeta]}$
and the original real period $\Omega$, one has

$$
x(\Omega/2)=1,\qquad
x\bigl(\Omega(1+\zeta)/2\bigr)=\zeta^2.
\tag{750.14}
$$

Indeed $1+\zeta=-\zeta^2$, $\wp$ is even, and
$\wp(\zeta^2z)=\zeta^2\wp(z)$. Applying reciprocity
to (750.12), with the inverse already included in
(750.11), gives

$$
\boxed{\sigma(\alpha)=\alpha/\zeta^2=\zeta\alpha.}
\tag{750.15}
$$

Since $\sigma$ fixes $A$ and $[AB:A]=3$, it generates
$\operatorname{Gal}(AB/A)$. This calculation specifies
the generator rather than leaving an undetermined
inverse in the cubic character.

## 5. Every Serre jet has the opposite tame character

In the original raw basis $(H_0,4H_2)$ the coefficient
vector is $v=(1,-\zeta^2)^{\mathsf t}$. R742 §3 fixes
the pure two-level right-slash convention and proves

$$
\rho_{\rm coeff}(C)=T_2S_2,
\qquad (T_2S_2)v=\zeta^2v.
\tag{750.16}
$$

The action in (750.11) has identity $p$ component, so
it leaves the original $p$-Cartan projection untouched.
It fixes $A$ and $\zeta$, as shown in Section 3. Hence
for the fixed original form

$$
F_h^{\,g_\zeta(x^{-1})}=\zeta^2F_h.
\tag{750.17}
$$

The raw $g_*$ phase at the R738 marking is precisely
the same two-level character. One may use the original
R588 representative or simultaneously transport the
form, level and frame; the eigencharacter (750.17)
is unchanged. It is not an instruction to multiply
another $\zeta^2$ into a jet that is already transported.

Serre differentiation commutes with the weight-graded
slash action, and $E_4,E_6$ are rational level-one forms.
The recurrence (750.6), being linear in the original
form, therefore preserves the eigenvalue $\zeta^2$
at every index. In particular

$$
\mathfrak J_{j,h}^{\,g_\zeta(x^{-1})}
=\zeta^2\mathfrak J_{j,h}.
$$

Reciprocity and (750.8) now give the all-order identity

$$
\boxed{\sigma(M_{3j-1,h})=\zeta^2M_{3j-1,h}.}
\tag{750.18}
$$

Combining (750.15) and (750.18) proves
$\sigma(\alpha M_{3j-1,h})=\alpha M_{3j-1,h}$.
By (750.9), this is exactly

$$
\alpha M_{3j-1,h}\in A.
\tag{750.19}
$$

Unlike the first-jet argument of R747, this proof needs
no square identity for a higher central-value product.
The actual tame character determines the cubic descent
for every order at once.

## 6. The real phase at every derivative order

R588 proves the actual conjugation phase by moving to
the period representative

$$
\tau_*=( -L+\sqrt{-3})/2,
\qquad p\mid L,\quad L\equiv1\pmod{12},
$$

and simultaneously transporting the finite vector,
period frame and level marking. Then
$-\overline{\tau_*}=\tau_*+L$. The $p$ translation is
identity, while the tame translation gives the same
anti-linear coefficient action as in R588 (588R.36–37),
namely eigenvalue $-\zeta$ on the actual positive vector.
The finite projected coefficients are real for every
primitive positive label, by the same Frobenius pairing
of the norm/trace fibers as in R727.

This calculation extends to every raising derivative.
For a Fourier series, $q\,d/dq$ commutes with
$F(\tau)\mapsto\overline{F(-\overline\tau)}$.
The additional term $-k/(4\pi\operatorname{Im}\tau)$
in the Maass operator is real and is unchanged by
that reflection. Translation by $L$ has $c=0,d=1$,
so raising the weight introduces no further slash
factor. Finally the original flat comparison has
period factor $(2\pi i/\Omega)^{6j}$, which is real.
Consequently

$$
\boxed{
\overline{M_{3j-1,h}}=-\zeta M_{3j-1,h}
\quad(j\ge1).
}
\tag{750.20}
$$

This is an algebraic complex-conjugation identity,
established before any $p$-adic embedding is selected.
It is not the assertion that complex conjugation
preserves a selected $p$-adic place.

Since $\alpha$ is positive real and
$\overline{u_0}/u_0=-\zeta$, (750.19)–(750.20)
show that $\mathcal T_{j,h}$ is in $A$ and fixed by
complex conjugation. Thus it belongs to $F_0$,
completing (750.2). The common scalar $u_0/\alpha$
cancels in the ratio of any two nonzero allowed
jets, proving (750.3).

## 7. Original coefficient embeddings and the p-adic consequence

The automorphism $\eta\mapsto\eta^h$ of $A$ fixes $K$.
Since $A\cap E=K$, it extends to $AE$ by the identity
on $E$. In particular it fixes the actual CM point,
$\alpha$, $\zeta$, and all the original $p$-cusp phases.
It sends the original finite character to its label
$h$ and commutes with every operation in (750.6).
Applying it to (750.8) proves (750.4).

At $p$, the Frobenius on $A$ is exponent
$p\equiv-1\pmod n$, hence is complex conjugation.
It acts trivially on $F_0$. Thus $p$ splits completely
in $F_0$, and (750.3) yields the actual rational
$p$-adic ratios at every selected place:

$$
M_{3j-1,h}/M_{3\ell-1,h}\in\mathbf Q_p.
\tag{750.21}
$$

This gives a global explanation of the rational jet
line used in R730/R742/R744, and allows any nonzero
allowed jet as its denominator. The first jet need
not be nonzero for the field statement.

The factor $u_0/\alpha$ is a $p$-adic unit and belongs
to the fixed tame field. Hence (750.2) also recovers
integer valuations for all the original jets. It
does not claim that a jet is a unit or evaluate a
chosen jet. The canonical Weierstrass polynomial
of R744 is still formed from a complete $p$-adic
restricted series; this result does not assert that
its coefficients lie in the global number field
$F_0$ merely because the Taylor coefficients do.

## Sources and scope

- [R588](R588-actual-toric-norm-and-CM-normalization.md), §§7–8: the original period comparison and the transported anti-linear tame phase.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), §2: the same actual primitive coefficient embeddings and unchanged positive phase.
- [R742](R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md), §§3–4.1: the complete arithmetic action, the right pure-two coefficient matrix, the all-order Serre recurrence, and original all-order flat identity.
- [R747](R747-global-real-square-root-of-original-toric-period-product.md), §§2–4 and 6: the exact conductor-six ray field, coefficient-field intersection, global inertia fixed field, and signed coefficient transport.
- E. Roşu, *Central values of L-functions of cubic twists*, [§5, Theorem 35](https://link.springer.com/article/10.1007/s00208-020-02018-0): arithmetic right-action CM reciprocity, including the inverse and determinant action. The specific tame character is computed in Sections 3–5 above.

No new numerical computation is used. The original simultaneous
Cartier-unit question, the actual period/map computation and
the complete height common-root problem remain separate.
