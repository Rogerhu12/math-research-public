# R747 — A global real square root for the original toric period product

Date: 2026-11-14. Status: **proved**.

The original first jet has a smaller global field than the a priori
full-level CM ray field. After its exact tame normalization it gives
a single real cyclotomic algebraic number whose square is the original
product $2NP$. Its coefficient conjugates carry their signs from the
original form; no independent square-root choices are made.

## 1. Statement and normalization

Let $p\ge41$, $p\equiv5\pmod6$, and put

$$
n=p+1,\qquad A=\mathbf Q(\zeta_n),\qquad
F_0=A^+,\qquad K=\mathbf Q(\zeta)\subset A,
\qquad \zeta^2+\zeta+1=0.
\tag{747.1}
$$

Here $\zeta$ has the same positive complex embedding as R588.
Put $\alpha=\sqrt[3]4>0$ and retain

$$
C_0=72\sqrt3/\alpha,\qquad C_0^2=15552/\alpha^2.
\tag{747.2}
$$

For every primitive positive label $h$, namely
$(h,n)=1$ and $h\equiv1\pmod6$, let $M_{2,h}$,
$N_h$, and $P_h=S_{2,h}S_{3,h}/C_0^2$ be exactly the original
R588/R717/R727 objects. In particular the raw absolute
normalization and its complex-conjugation phase remain

$$
\frac{M_{2,h}^2}{\zeta^2}
 =-\frac{8N_hC_0^2}{n^2}P_h,\qquad
\overline{M_{2,h}}=-\zeta M_{2,h}.
\tag{747.3}
$$

The bar in (747.3) is the original algebraic complex conjugation.
It is used before passing to a chosen $p$-adic place.

Set

$$
u=1-\zeta^2,\qquad
T_h=\frac{\alpha n M_{2,h}}{144u}.
\tag{747.4}
$$

**Theorem 747.1.** One has

$$
\boxed{
M_{2,h}\in A(\alpha),\qquad
\alpha M_{2,h}\in A,\qquad
T_h\in F_0,\qquad T_h^2=2N_hP_h.
}
\tag{747.5}
$$

Moreover, with the original positive labelling,
$T_h=\sigma_h(T_1)$, where $\sigma_h$ is the corresponding
embedding of $F_0$. These are the original signed values, not
just an equality of squares.

There is an explicit integral denominator:

$$
\boxed{
2^{18}3^{13}p^2T_1\in\mathcal O_{F_0}.
}
\tag{747.6}
$$

The same statement applies to every conjugate $T_h$.
No assertion that $p^2T_h$, $N_h$, or either selected Cartier
coefficient is a unit follows from (747.5) or (747.6).

## 2. Fix the exact level-six CM ray field

For a positive integer $m$, write $K_m$ for the ray class field
of $K$ of modulus $m\mathcal O_K$. The ring
$\mathcal O_K=\mathbf Z[\zeta]$ is norm-Euclidean, so its ideal
class group is trivial. Since $2$ is inert and $3$ is ramified,

$$
|(\mathcal O_K/2)^\times|=3,\qquad
|(\mathcal O_K/3)^\times|=6.
$$

Reduction of the six units is injective modulo $3$ and hence
modulo $6$: $\zeta-1$ has valuation one at the prime over $3$,
whereas the modulus $3$ has valuation two there.
The ray-class exact sequence therefore gives

$$
[K_6:K]=\frac{3\cdot6}{6}=3.
\tag{747.7}
$$

To identify the field with the original choice of $\alpha$, use
the weight-zero level-six function

$$
R_6(\tau)=
 \frac{\wp_{\mathbf Z+\mathbf Z\tau}(1/3)}
      {\wp_{\mathbf Z+\mathbf Z\tau}(1/2)}.
\tag{747.8}
$$

Both numerator and denominator transform as weight-two
functions under $\Gamma(6)$, so their ratio is a modular
function of that full level. The usual Laurent/Fourier series
of $\wp/(2\pi i)^2$ has coefficients in $\mathbf Q(\zeta_6)$
at these torsion arguments. The common factor cancels in
(747.8), so $R_6\in\mathcal F_6$.

On the original curve $E_0:y^2=x^3-1$ with period
$\Omega>0$, the actual real torsion points have

$$
x(\Omega/2)=1,\qquad x(\Omega/3)=\alpha.
\tag{747.9}
$$

The first is the real nonzero two-torsion point. The
three-division equation is $3x(x^3-4)=0$; the real point
$\Omega/3$ has $x>1$, fixing the positive root in (747.9).
The scale $\Omega^{-2}$ cancels in (747.8), and therefore

$$
R_6(\zeta)=\alpha.
\tag{747.10}
$$

The CM reciprocity theorem places this finite value in $K_6$.
Since $X^3-4$ is irreducible over $K$, (747.7) gives

$$
\boxed{K_6=K(\alpha).}
\tag{747.11}
$$

This identifies the actual tame CM field, including the primes
$2$ and $3$; a larger unspecified ray field is not substituted.

One can also check its exact finite conductor directly in the
same ray-class quotient. The subgroup from
$(\mathcal O_K/2)^\times$ maps injectively and nontrivially into
the group of order three. Thus the conductor contains $2$,
with exponent one. At the prime
$\lambda=(1-\zeta)$ over $3$, the group
$(1+\lambda\mathcal O_K)/(1+\lambda^2\mathcal O_K)$
has order three. Its image is nontrivial: a representative
which is $\zeta$ modulo $3$ and one modulo $2$ is not a global
unit residue modulo $6$, since $\zeta$ has nontrivial residue
modulo $2$. The modulus already bounds the exponent by two.
Thus the conductor is exactly
$2\lambda^2=6\mathcal O_K$, up to its unit generator.

Finally $K(\alpha)/\mathbf Q$ is the splitting field of
$X^3-4$ and has Galois group $S_3$, not an abelian group.
This fact will fix the field intersection below.

## 3. The entire p-inertia group and its fixed field

Set

$$
E=K_{6p},\qquad B=K_6.
$$

In the ray-class exact sequence obtained by removing the
coprime factor $p$, the kernel is the image of
$(\mathcal O_K/p)^\times$. There is no remaining unit quotient
in this kernel: a global unit congruent to one modulo $6$
is already one. Hence

$$
\operatorname{Gal}(E/B)
 \simeq(\mathcal O_K/p)^\times,\qquad
[E:B]=p^2-1.
\tag{747.12}
$$

The image of the local units $\mathcal O_{K_p}^\times$ under
reciprocity is exactly this kernel. It is the full inertia
subgroup $I_p$ at $p$ in the abelian extension $E/K$. Thus

$$
\boxed{E^{I_p}=B=K_6.}
\tag{747.13}
$$

This is a global fixed-field identity established from the
ray-class sequence. It is not being inferred just from a local
valuation bound.

The coefficient field $A=\mathbf Q(\zeta_n)$ is unramified at
$p$, since $p\nmid n$. Therefore $A\cap E$ is an extension of
$K$ unramified at $p$, and (747.13) implies

$$
A\cap E\subset B.
$$

But $[B:K]=3$. If $A\cap B$ were $B$, then the nonabelian
Galois extension $B/\mathbf Q$ would be a subextension of the
abelian extension $A/\mathbf Q$, which is impossible.
Consequently

$$
\boxed{A\cap E=A\cap B=K.}
\tag{747.14}
$$

Both extensions of $K$ are Galois, so they are linearly
disjoint over $K$. In particular

$$
\operatorname{Gal}(AE/K)
 \simeq\operatorname{Gal}(A/K)\times\operatorname{Gal}(E/K).
\tag{747.15}
$$

Unramified local base change preserves the ramification index.
Thus the inertia subgroup at $p$ in (747.15) is exactly
$\{1\}\times I_p$, not a proper unidentified subgroup.
Its fixed field is

$$
\boxed{(AE)^{\{1\}\times I_p}=AB=A(\alpha).}
\tag{747.16}
$$

Equations (747.12)–(747.16) are the field-intersection and
inertia steps needed below.

## 4. Place the original first jet in that precise fixed field

R742 constructs from the unchanged original raw form $F_h$ the
weight-zero function

$$
\mathfrak J_h=
 \frac{\partial_4\partial_2F_h}{E_6},
\qquad
\partial_k=q\frac d{dq}-\frac{k}{12}E_2,
$$
$$
M_{2,h}=-864\,\mathfrak J_h(\zeta).
\tag{747.17}
$$

This equality has the original absolute period and the original
raw tame phase. R742 explicitly distinguishes it from
performing an additional tame slash operation on an already
fixed form.

For the global field statement we now retain the analytic
level $6p$ and treat $A$ as the coefficient extension, rather
than merely enlarging the full level to $6pn$.
The Fourier expansion of $F_h$ has coefficients in
$A(\zeta_{6p})$, by the explicit finite-type cusp realization.
The Serre operators and division by the rational level-one
form $E_6$ preserve this coefficient field. The function has
analytic level $6p$. The characteristic-zero full-level
$q$-expansion descent therefore gives

$$
\mathfrak J_h\in A\,\mathcal F_{6p}.
\tag{747.18}
$$

This is the usual constant-field extension of the arithmetic
modular-function field. One can see it by taking a basis of
the finite coefficient extension and descending the rational
function on the canonical full-level curve; invariance of its
Fourier expansion gives invariance of the function itself.

The corresponding CM point of that canonical curve has
residue field contained in $E=K_{6p}$. Base changing the
constant field by $A$ makes its residue field a subfield of
$AE$. A function in (747.18) which is finite there therefore
has its value in $AE$, including when a particular rational
presentation has removable poles. Since $E_6(\zeta)\ne0$,
this applies to $\mathfrak J_h$. It follows that

$$
M_{2,h}\in AE.
\tag{747.19}
$$

The full arithmetic invariance checked in R742 fixes the
value under $\{1\}\times I_p$. More explicitly, the idele
$x$ is an arbitrary unit at $p$ and one at all other places.
Its reciprocity matrix at $p$ is

$$
g_\zeta(A_0+B_0\zeta)
 =\begin{pmatrix}A_0-B_0&-B_0\\B_0&A_0\end{pmatrix},
\tag{747.20}
$$

which is exactly the original nonsplit Cartan.
The inverse matrix in the reciprocity law lies in the same
Cartan. At the conductor-six places and in the
prime-to-$p$ coefficient field its action is identity.
R742 verifies the determinant part on Fourier coefficients,
not merely the determinant-one slash action.
Thus (747.16) and (747.19) prove

$$
\boxed{M_{2,h}\in AB=A(\alpha).}
\tag{747.21}
$$

All simultaneous transports of the actual torus, split vector,
tame basis, and differential frame in R588/R738/R742 preserve
this statement. No new raw phase is applied in (747.17).

## 5. An odd-degree descent removes the cubic extension

The original norm (747.3) gives

$$
(\alpha M_{2,h})^2
 =-\frac{124416\,\zeta^2}{n^2}N_hP_h\in A,
\tag{747.22}
$$

because $N_h,P_h\in F_0\subset A$.
On the other hand $\alpha M_{2,h}\in A(\alpha)$ by (747.21).
The extension $A(\alpha)/A$ has degree three by (747.14).

An element of this extension whose square is in $A$ generates
an intermediate extension of degree dividing two, as well as
dividing three. Its degree is therefore one. This applies
also when the element is zero, and proves

$$
\boxed{\alpha M_{2,h}\in A.}
\tag{747.23}
$$

This descent does not infer that a square root lies in a field
merely because its square does. The odd extension degree is
the essential extra input.

The elementary identities for the original phase are

$$
u=1-\zeta^2,\qquad
u^2=-3\zeta^2,\qquad
\frac{\overline u}{u}=-\zeta.
\tag{747.24}
$$

Together with $\alpha>0$ and the actual
$\overline M_{2,h}=-\zeta M_{2,h}$, they show that
$\alpha M_{2,h}/u$ is fixed by complex conjugation.
By (747.23), it lies in $A^+=F_0$.
Thus $T_h\in F_0$.

Substituting the fixed constants gives

$$
\begin{aligned}
T_h^2
&=\frac{\alpha^2n^2}{144^2u^2}
  \left(-\frac{8\zeta^2N_hC_0^2}{n^2}P_h\right)\\
&=\frac{-124416\zeta^2}{20736(-3\zeta^2)}N_hP_h\\
&=2N_hP_h.
\end{aligned}
\tag{747.25}
$$

This proves the square-root identity with its exact rational
factor two.

The relation to the raw tame transport is particularly simple.
Let $s_0=\sqrt{-3}=1+2\zeta$. Since $u=-\zeta s_0$,
formula (747.4) is equivalently

$$
\boxed{
T_h=\frac n{432}\,
          \bigl(\alpha s_0\zeta^2M_{2,h}\bigr).
}
\tag{747.26}
$$

The factor $\zeta^2$ is precisely the raw $g_*$ phase recorded
in R742. Formula (747.26) displays it once. If the tame basis
has already been transported, it is not multiplied again.
This is compatible with first transporting the raw positive
form and then multiplying by $\alpha s_0$ in the arithmetic
Hodge normalization; it does not replace the still-required
comparison with a quotient's Néron differential by a unit claim.

## 6. The signs are transported by the original coefficient embeddings

A positive primitive label $h$ defines an automorphism of $A$
which fixes $K$, since $h\equiv1\pmod3$.
By (747.14) this automorphism extends to $AE$ by acting
trivially on $E$. It fixes the actual CM level point and
$\alpha\in B\subset E$, as well as $\zeta$ and $u$.

On the Fourier expansion, it sends
$\theta$ to $\theta^h$, fixes the original tame $\mu_3$ vector,
and preserves the $\zeta_p$ cusp phases in $E$.
Thus the original ideal-sum newform, finite Cartan average,
and complete raw normalization are sent to those with label
$h$. Applying the exact weight-zero identity (747.17) gives

$$
\sigma_h(M_{2,1})=M_{2,h},
\qquad
\sigma_h(T_1)=T_h.
\tag{747.27}
$$

The restriction map
$\operatorname{Gal}(A/K)\to\operatorname{Gal}(F_0/\mathbf Q)$
is an isomorphism, because $A=KF_0$ and $K\cap F_0=\mathbf Q$.
So these are all the real coefficient conjugates.
Equation (747.27) fixes their relative signs; there is no
independent choice of a square root at each $h$.

At the inert prime $p$, which splits completely in $F_0$,
the factor $\alpha n/(144u)$ is a unit. Hence

$$
v_p(T_h)=v_p(M_{2,h}).
\tag{747.28}
$$

The real square root therefore records the same original
first-jet valuation at each selected place.

## 7. The explicit integral denominator

R717 proves the global denominator

$$
D=2^{37}3^{26}p^5,\qquad DP_1\in\mathcal O_{F_0}.
\tag{747.29}
$$

R730 proves $N_1\in\mathcal O_{F_0}$.
Since $T_1^2=2N_1P_1$, these imply at every finite place
outside $2,3,p$ that $v(T_1)\ge0$.
At a place over $2$, normalized by $v(2)=1$, they give
$2v(T_1)\ge1-37=-36$, so $v(T_1)\ge-18$.
At a place over $3$, they give $v(T_1)\ge-13$.

At each place over $p$, R742 combines the one-$p$ full Hodge
bound with integral first-jet valuation to give

$$
v_p(M_{2,h})\ge-2.
$$

All places over $p$ are represented by the positive primitive
labels, and (747.28) transfers this bound to $T_1$.
Thus

$$
Z=2^{18}3^{13}p^2T_1
$$

is integral at every finite place of $F_0$.
It is an algebraic integer, proving (747.6).
The exact associated square is

$$
\boxed{
Z^2=\frac Dp\,N_1P_1\in\mathcal O_{F_0}.
}
\tag{747.30}
$$

There is no independent assumption that $D/p$ already clears
the denominators of $P_1$ alone; (747.30) concerns the
displayed product and follows from the actual first-jet bound.

## 8. Scope

The real algebraic number $T_1$ and its conjugates are fixed
by the original cusp-normalized form. They supply an exact
global field and square-root interface, and an explicit
integral denominator. Neither a complex central nonvanishing
statement nor the mere existence of a global square forces
a selected residue to be a $p$-adic unit.

For $h\ne1$, the simultaneous conditions
$N_h\ne0$, $C_{h-2}\ne0$, and $C_{p-h-2}\ne0$ modulo $p$
remain a separate question.
The original height condition and its fixed constants are
also unchanged. No Serre-uniformity or height-zero exclusion
is asserted here.

## Dependencies and sources

- R588/R727: the exact original norm, raw phase, and characters.
- R697: the fixed positive real two- and three-torsion values
  on $E_0$, also derived in (747.9).
- R717: the original product $P_1\in F_0$ and its full global
  integral denominator.
- R730/R742: the finite norm's integrality, the exact weight-zero
  first jet, complete arithmetic Cartan action, and first-jet
  lower bound.
- The arithmetic modular-function reciprocity used for the finite
  CM values is E. Rosu, *Central values of L-functions of cubic
  twists*, [§5, Theorem 35](https://link.springer.com/article/10.1007/s00208-020-02018-0).
  The relevant exact ray-class groups, conductor, intersection,
  and inertia fixed fields are proved explicitly above.

