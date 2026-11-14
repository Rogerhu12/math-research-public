# R746: the original ordinary coefficient as a strict-p Bockstein condition

Date: 2026-11-14. **Status: proved.** This result gives a complete
ordinary first-jet criterion with the original markings, including
the sufficient direction from a supported cochain to an ordinary
Hilbert quotient. Section 5 retains the difference from R743's
finite-flat quotient. Neither $J_\ell$ nor $b$ is numerically evaluated.

## 1. A precise criterion for the original ordinary coefficient

Use the original $M=LB$, $\Gamma,S,T$, and
$A_M=R_\Gamma/\pi^{43}$ of R657/R715, where
$\pi=\gamma-1$. The actual actions modulo $\pi^2$ are

$$
\gamma=1+\pi,\qquad s=1+i\pi,\qquad t=1+b\pi.
$$

Let $\kappa_S$ denote the scalar character normalized by
$\kappa_S(s)=1$, and retain the original $\kappa_p(t)=1$
and $\kappa_q(\gamma)=1$. Since the CM determinant on $s=1+p$
is $(1+p)^2$ and on the anti direction has first logarithm zero,

$$
\ell_{\rm cyc}=2\kappa_S.
\tag{746.1}
$$

At the original quadratic $q$ completion this gives
$\kappa_S(\operatorname{Fr}_{q^2})=32$, consistently with
$\ell_{\rm cyc}(\operatorname{Fr}_{q^2})=21$.

Fix $w$ as in R200/R743, with $w_p=0$ as a cochain and
$w_q=(27\varepsilon,-\varepsilon)$ in the original primal
finite/singular coordinates. For $z\in\mathbf F_{43}$, consider
the condition

$$
\begin{split}
\delta D_z
&=(-\ell_{\rm cyc}-2iz\kappa_p-2i\kappa_q)\cup w,\\
[D_z|_{G_p}]&=0,
\end{split}
\tag{746.2}
$$

with a continuous cochain for $G_{\mathbf Q,S}$ and
$S=\{2,p,q,\infty\}$. The $p$ localization is a cocycle because
$w_p=0$.

**Ordinary first-jet criterion.** Condition (746.2) holds if and
only if $z=b$.

The factors $2$ in (746.2) are essential. This is a deformation
over the characteristic-$p$ ring $k[\pi]/\pi^2$, where
$k=\mathbf F_{43^2}$, arising from the ordinary class module.
It is not a replacement of the actual mixed-characteristic
CM reference Bockstein by a formally similar expression.

## 2. The actual Hilbert quotient produces the necessary cochain

Use the full conjugate pair of character components as an actual
finite Galois group before identifying its chosen component with
$k[\pi]/\pi^2$. R657's tame-fixed splitting gives the ordinary
Hilbert quotient over $K$ as

$$
(A_M/\pi^2 A_M)\rtimes(\Delta\times\Gamma\times S\times T).
$$

The lifts of $\Gamma,S,T$ which centralize the fixed lift of
$\Delta$ are unique: $A^\Delta=0$ and
$H^1(\Delta,A)=0$. Thus this uses the actual marked generators,
not unspecified generators of cyclic factors. The subgroup of
order $44$ and complex conjugation can also be split because
its order $88$ is prime to $43$.

Choose the class generator with genus coordinate $1$. Complex
conjugation sends $\pi$ to $-\pi$ modulo $\pi^2$ and conjugates
$k$. If initially $\tau e=(1+c\pi)e$, the equality $\tau^2=1$
forces $c=\bar c$. Replacing $e$ by $(1+(c/2)\pi)e$ makes
$\tau e=e$. Changes of this normalization have the form
$(1+r\pi)e$ with $r+\bar r=0$.

The strict-$p$ genus coordinate of R657 is

$$
g_0=-\frac{\bar w}{\varepsilon}.
\tag{746.3}
$$

Indeed restriction from $\mathbf Q_q$ to $\mathbf Q_{q^2}$
doubles the finite coordinate. Formula (746.3) then gives
the original positive Frobenius value $32$ and the original
inertia value $-i$. These are exactly R657 (657.25).
The strict-$p$ genus space is one-dimensional, so the nonzero
marked value fixes the global normalization as well.

The class-field coordinate is a cocycle
$g_0+\pi g_1$ for the module with action

$$
\chi^-(1+\pi\lambda_b),\qquad
\lambda_b=\kappa_q+i\kappa_S+b\kappa_p.
$$

Taking its coefficient of $\pi$ gives

$$
\delta g_1=-\lambda_b\cup g_0.
\tag{746.4}
$$

Complex conjugation and multiplication by $i$ identify the
coefficient of $\pi$ with the original rational primal module
$W$. Set

$$
D_b=-2\varepsilon i\,\bar g_1.
$$

Substituting (746.3)--(746.4), with all cochain actions retained,
gives

$$
\begin{aligned}
\delta D_b
&=-2i\,\overline{\lambda_b}\cup w\\
&=(-2\kappa_S-2ib\kappa_p-2i\kappa_q)\cup w.
\end{aligned}
$$

This is exactly the first equation of (746.2) by (746.1).

The ordinary Hilbert quotient is actually split at every prime
over $p$ in this character component. It is unramified there by
definition; its relative unramified decomposition subgroup is
fixed by local inertia. The whole nontrivial $\Delta$ character
is inertial at $p$, so that subgroup is zero. Equivalently,
an unramified relative Frobenius is fixed by $\Delta$, whereas
the class kernel has no such fixed vector.

The local class-field cocycle therefore factors, over the original
$K_p=\mathbf Q_{p^2}$, through $\Delta\times S\times T$.
There is no $\Gamma$ direction in this actual decomposition
quotient: $L/F$ is completely split at $p$, so the chosen
completion of $M$ is the completion of $B$. The first cohomology
of this quotient in the nontrivial character is zero: after
taking cohomology of the $p$ subgroup, every cochain still has
the same nontrivial $\Delta$ character, and $|\Delta|$ is
invertible. Restriction from $\mathbf Q_p$ to its unramified
quadratic extension is injective on the relevant $p$-primary
cohomology, so the original rational local cocycle is also a
coboundary. Since the already fixed $g_0$
is exactly zero at $p$, and $H^0(\mathbf Q_p,W)=0$, its killing
cochain has zero constant term. Consequently $[D_{b,p}]=0$.
This proves necessity, including the ordinary local condition.

## 3. A strict-p primitive gives an ordinary Hilbert quotient

Conversely, suppose (746.2) holds. Define

$$
g_0=-\frac{\bar w}{\varepsilon},\qquad
g_1=-\frac{i}{2\varepsilon}\bar D_z,
\qquad
\lambda_z=\kappa_q+i\kappa_S+z\kappa_p.
$$

The same direct calculation gives
$\delta g_1=-\lambda_z\cup g_0$. Hence $g_0+\pi g_1$
is a cocycle for $\chi^-(1+\pi\lambda_z)$ and defines a finite
semidirect-product extension. The real descent is part of the
coefficient-module construction: $\tau$ conjugates $k$ and
sends $\pi$ to $-\pi$, while multiplication by $i$ identifies
the resulting anti-invariant coefficient with $W$. This is
why the displayed factor $-i/(2\varepsilon)$ is used.

Over $M$, all three characters in $\lambda_z$ vanish and
$\chi^-$ is trivial. The class-field kernel is thus an abelian
subgroup of $k[\pi]/\pi^2$. We check every possible place of
ramification of this relative extension.

At $p$, subtracting a global coboundary from $D_z$ makes its
local cochain zero, by the second equation of (746.2). Together
with $w_p=0$ this makes the relative extension split at $p$.

At $q$, wild inertia has no pro-$43$ quotient. In the pro-$43$
part of tame inertia, the original generator maps to an element
$(a,1+\pi)$ of the semidirect product. Its $p$th power has class
coordinate

$$
\sum_{j=0}^{p-1}(1+\pi)^j a
=p a+\binom p2\pi a=0
\quad\text{in }k[\pi]/\pi^2.
\tag{746.5}
$$

The diagonal coordinate is also $1$. Since $M$ already contains
the original totally ramified degree-$p$ $\Gamma$ extension,
its relative tame inertia is generated by these $p$th powers.
Thus the new extension is unramified above $q$. This does not
assume the value of a higher scalar class-action coefficient.

At $2$, the two subquotients of the coefficient module are
isomorphic to $W$ after the indicated multiplication by $i$.
R189 gives $H^1(\mathbf Q_2,W)=0$, so the short exact sequence
of coefficient modules gives zero local $H^1$ for the full
module as well. Its cocycle is locally a coboundary and adds
no relative ramification. The other finite places are handled
by the stipulated $S$ support. There is no odd-primary
archimedean obstruction.

The extension over $M$ is consequently ordinary and abelian.
Its image modulo $\pi$ is the nonzero original strict-$p$
genus quotient: that genus field is disjoint from $M$ by the
nontrivial $\Delta$ type, as proved in R657. The class kernel
is initially an additive $\mathbf F_p$ subspace, and it is
stable under both $\Delta$ and $\Gamma$. The actual $\Delta$
generator acts by $\omega^{-1}$, of order $44$. This scalar
is not in $\mathbf F_{43}$, whose multiplicative group has
order $42$. Hence $\mathbf F_{43}[\omega^{-1}]=k$, and
$\Delta$ stability makes the image a $k$ submodule.
A $\Gamma$-stable $k$ submodule of $k[\pi]/\pi^2$
surjecting modulo $\pi$ is the whole module,
because multiplication by $\gamma-1=\pi$ supplies its other
line. We therefore obtain a surjective ordinary quotient

$$
A_M\longrightarrow k[\pi]/\pi^2
$$

respecting the actual $\Gamma,S,T$ generators. Since
$A_M=R_\Gamma/\pi^{43}$ is cyclic and its unique length-two
quotient has $t$ action $1+b\pi$, whereas the constructed
quotient has action $1+z\pi$, it follows that $z=b$.
This proves the sufficient direction of (746.2).

## 4. The exact local functional which reads b

A supported primitive of the first equation of (746.2) exists for
every $z$, before imposing the strict-$p$ condition. At $p$ its
cup class is zero because $w_p=0$. At $q$ this can be checked
with the original quadratic local marking in genus coordinates:

$$
\lambda_z(\operatorname{Fr})=32i,\quad
\lambda_z(\tau_q)=1,\quad
g_0(\operatorname{Fr})=32,\quad
g_0(\tau_q)=-i.
$$

The local alternating cup is
$32i(-i)-1\cdot32=0$. The anti-$p$ character is zero there.
At $2$ and infinity the local $H^2$ vanishes. R743 proves the
needed $\Sha^2_S(W)=0$ using the complete dual space and its
injective $p$ localization. Thus the locally zero global class
vanishes with the required support.

Choose any supported $D_0$ with

$$
\delta D_0=(-\ell_{\rm cyc}-2i\kappa_q)\cup w.
$$

Let $B_p(w)$ be any supported pure-$p$ primitive
$\delta B_p(w)=-i\kappa_p\cup w$. Then

$$
D_z=D_0+2zB_p(w)
\tag{746.6}
$$

is a primitive for the first equation in (746.2).
The available global corrections are precisely
$\mathbf F_p c_p^{\rm Rob}\oplus\mathbf F_p w$ by R743.
The $p$ image of $w$ is zero; the nonzero $p$ image of
$c_p^{\rm Rob}$ is exactly the annihilator of $(d_0)_p$,
as follows from the two-dimensional local space and
R189's pairings $(6,10)$ against $(24,20)$.
Therefore a given $D_z$ can be made strictly zero at $p$
if and only if

$$
\langle[D_{z,p}],(d_0)_p\rangle_p=0.
\tag{746.7}
$$

The single anti-cyclotomic secondary reciprocity identity,
using $d_0(q)=0$ and R198's $e_p(d_0)_q=28K_0$, gives

$$
\langle[B_p(w)_p],(d_0)_p\rangle_p
=-\langle w_q,e_p(d_0)_q\rangle_q
=-13\varepsilon.
\tag{746.8}
$$

This value is unaffected by global primitive corrections.
Combining (746.2), (746.6)--(746.8) yields the exact original formula

$$
\boxed{
\langle[D_{0,p}],(d_0)_p\rangle_p=26\varepsilon b.
}
\tag{746.9}
$$

Thus the ordinary coefficient is read by the $d_0$ local
functional. R743 reads the finite-flat-normalized pure-$p$
primitive using the different functional
$\widetilde d_q=d_q-8d_0$.

## 5. The retained difference from the first-moment quotient

In the actual AH basis,

$$
(d_0)_p=(24,20),\qquad
(\widetilde d_q)_p=(0,41).
$$

They are linearly independent. Formula (746.9) is a statement
about the $\Gamma$/scalar primitive $D_0$, tested against
the first of these two vectors. R743 is a statement about
the pure-$p$ primitive $B_p(w)$, adjusted by the second vector,
and then tested in the local quotient
$H^1(\mathbf Q_q,W)/\mathbf F_p w_q$.

The precise remaining claim would have to compare these
different primitives and functionals by an additional marked
global exchange identity. The dimension of either final scalar
space does not supply that identity. In particular (746.9)
does not imply $J_\ell-18$ is proportional to $b-24$.

For checking against already published formulas, R720 makes
(746.9) equivalent to

$$
\langle[D_{0,p}],(d_0)_p\rangle_p
=\varepsilon(\mathcal L-31),
$$

because $\mathcal L=31+26b$. This leaves exactly the original
$\Gamma$-norm input unknown; it has not evaluated it.

## Dependencies

- [R657](R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md), Section 5: the actual tame-fixed splitting, positive Frobenius and inertia genus values, and the scalar coefficient $i$.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md): the proved ordinary endpoint $A_M=R_\Gamma/\pi^{43}$.
- [R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md), [R185](R185-p-local-robert-and-principal-unit-coordinates.md), and [R189](R189-primal-robert-generator-and-exact-local-pairings.md): the same local coordinates, finite-flat line, original primal generator, and complete local pairings.
- [R198](R198-p-squared-robert-norm-and-a-secondary-contribution.md) and [R200](R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md): the supported dual value $28K_0$ and the negative-adjoint secondary reciprocity identity.
- [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md): the original ordinary $\Theta$ comparison and $\mathcal L=31+26b$.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md): both complete supported $H^1$ spaces, the correct $\Sha^2_S(W)$ vanishing, and the distinct finite-flat primitive quotient.

All ramification checks and both directions of the ordinary criterion
are supplied in Sections 2--3. No new numerical computation or
uncomputed ordinary principalization is inserted into the proof.
