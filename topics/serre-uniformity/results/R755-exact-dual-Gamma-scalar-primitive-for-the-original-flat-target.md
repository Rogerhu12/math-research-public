# R755: the exact dual Gamma/scalar primitive for the original flat target

Date: 2026-11-14. **Status: proved.** This result realizes R752's
choice-independent invariant $I_0$ as an exact regularized local
pairing of a supported dual primitive. It includes the negative
adjoint, the local quadratic and cubic corrections, and the original
flat-target correction. The primitive and its pairing are not
numerically evaluated. No value of $J_\ell$ or $b$ is inferred.

Retain every original marking and the support
$\Sigma=\{2,p,q,\infty\}$. Put

$$
d_{\rm fl}=d_q-8d_0,\qquad
x=-\ell_{\rm cyc}-2i\kappa_q.
$$

The adjoint for the original trace pairing and its negative are

$$
x^\dagger=-\ell_{\rm cyc}+2i\kappa_q,\qquad
y=-x^\dagger=\ell_{\rm cyc}-2i\kappa_q.
\tag{755.1}
$$

Thus taking the negative adjoint reverses the scalar sign and
retains the $-2i\kappa_q$ sign. There is a $\Sigma$-supported
dual cochain $E_{\rm fl}$ with

$$
\delta E_{\rm fl}=y\cup d_{\rm fl}.
\tag{755.2}
$$

Section 2 defines its rational, regularized local class
$\mathscr S_{\rm fl}$ at $q$. The main identity is

$$
\boxed{I_0=-\langle w_q,\mathscr S_{\rm fl}\rangle_q.}
\tag{755.3}
$$

For the original uncorrected class $d_q=\kappa(A_\alpha)$,
choose a supported $E_\alpha$ with
$\delta E_\alpha=y\cup d_q$ and define its corresponding
regularized class $\mathscr S_\alpha$. Then

$$
\boxed{
I_\alpha:=-\langle w_q,\mathscr S_\alpha\rangle_q
=\mathscr L_q(D_0)+\langle[D_{0,p}],d_{q,p}\rangle_p,
}
\tag{755.4}
$$

and

$$
I_0=I_\alpha+7\varepsilon b,\qquad
\boxed{I_\alpha=\varepsilon(21\sigma_2+2bJ_\ell).}
\tag{755.5}
$$

Here $D_0$, $\mathscr L_q$, and $\sigma_2$ are exactly those
of R752. Formula (755.5) preserves the genuine second scalar
coefficient and the remaining global Gamma/scalar input.

## 1. Supported existence and the complete dual direction

The adjoint signs in (755.1) follow from the original trace
pairing: scalar multiplication is self-adjoint, while multiplication
by $i$ is skew-adjoint. These are the same signs as
R200 (200.7), applied to the sum of the scalar and q directions.

The complete primal space, proved in R743, is

$$
H^1(G_{\mathbf Q,\Sigma},W)
=\mathbf F_{43}c_p^{\rm Rob}\oplus\mathbf F_{43}w.
$$

Its q localizations are $(10,0)$ and
$(-16\varepsilon,-\varepsilon)$. Their determinant is
$-10\varepsilon\ne0$. Hence localization at $q$ is already
injective on the entire supported space, and

$$
\Sha^1_\Sigma(W)=0.
$$

Poitou--Tate duality gives
$\Sha^2_\Sigma(W(1))=0$. The direction is the dual of
$\Sha^1_\Sigma(W)$; it is not the opposite duality used for
a primal primitive.

At $p$, $H^2(\mathbf Q_p,W(1))=0$, since
$H^0(\mathbf Q_p,W)=0$ in the original nontrivial tame
type. At $2$ the original coefficient cohomology vanishes,
and at the real place $p$ is odd. Section 2 gives an
explicit q primitive, proving that the class of
$y\cup d_{\rm fl}$ is zero there as well. Thus this
supported global two-cocycle is locally trivial everywhere
in $\Sigma$, and the displayed Sha vanishing proves (755.2).
Exactly the same argument applies to $d_q$.

Any two supported primitives in (755.2) differ, up to a
coboundary, by the complete dual space

$$
H^1(G_{\mathbf Q,\Sigma},W(1))
=\mathbf F_{43}d_0\oplus\mathbf F_{43}d_q.
\tag{755.6}
$$

This will be used below to prove independence of the local
pairing, not to identify two different local normalizations.

## 2. Rational quadratic regularization at q

Use R752's local coefficient algebra $k=\mathbf F_{43^2}$.
For $W$, identify $F_0=1$, $K_0=i$, and let rational
Frobenius act by conjugation. For $W(1)$, its action in
the same algebra is negative conjugation. Put

$$
v=\kappa_S+i\kappa_q,\qquad
w^0=-\varepsilon v,\qquad
d^0=i\bar v.
\tag{755.7}
$$

The original positive quadratic Frobenius $f$ and marked
tame inertia $x_q$ have

$$
v(f)=32,\qquad v(x_q)=i.
$$

Thus $w^0$ represents the actual primal coordinates
$(-16\varepsilon,-\varepsilon)$, and $d^0$ represents
the actual dual coordinates $(16,1)$. Both $d_q$ and
$d_{\rm fl}$ have this latter local class, because
$d_{0,q}=0$.

On this local algebra,

$$
x=-2v,\qquad y=2\bar v.
$$

The rational quadratic cochains are

$$
\mathfrak q=-\varepsilon v^2,\qquad
\mathfrak p=-i\bar v^2.
\tag{755.8}
$$

Their differentials are

$$
\delta\mathfrak q=x\cup w^0,\qquad
\delta\mathfrak p=y\cup d^0.
\tag{755.9}
$$

For example,
$\delta(-i\bar v^2)=2i\,\bar v\cup\bar v
=(2\bar v)\cup(i\bar v)$.
The map $z\mapsto-i\bar z^2$ changes by negative
conjugation when $z$ changes by conjugation. Thus the
second cochain belongs to the rational dual coefficient
module; it is not merely a cochain after quadratic base
change.

Let $d$ denote either $d_{\rm fl}$ or $d_q$, and $E$ the
corresponding supported primitive. Choose a local
$0$-cochain $k_q$ with

$$
d|_{G_q}=d^0+\delta k_q.
$$

Put

$$
E^0=E+y\cup k_q,\qquad
\mathscr S_d=[E^0-\mathfrak p]\in H^1(\mathbf Q_q,W(1)).
\tag{755.10}
$$

The degree-one Leibniz sign proves that $E^0$ has
differential $y\cup d^0$, so the class is defined.
An invariant dual $0$-cochain is $ic$ with
$c\in\mathbf F_{43}$. Changing $k_q$ by $ic$ changes
$\mathscr S_d$ by $2c\,d^0$, whose pairing with $w_q$
is zero. Thus the pairing in (755.3) is independent of
the local killing cochain.

A direct evaluation makes this independence valid even
when calculations are done before choosing the rational
gauge. For a rational dual cocycle of finite/singular
coordinates $(u,v_1)$, restriction gives

$$
S(f)=2iu,\qquad S(x_q)=v_1,
$$

and hence

$$
\langle w_q,S\rangle_q
=\varepsilon\bigl(-iS(f)-32S(x_q)\bigr).
\tag{755.11}
$$

For any $k_q\in k$, the correction $yk_q$ has values
$64k_q$ and $-2ik_q$. Its contribution to (755.11)
is zero. Thus the pairing can be read directly from
the quadratic restriction of $E-\mathfrak p$.

Finally, a change of the global supported primitive
adds a combination from (755.6). Its local class adds
a multiple of $(16,1)$, since $d_{0,q}=0$.
This again pairs to zero with $w_q$. Coboundaries make
no change. The pairing in (755.3), and similarly that
in (755.4), is therefore fully choice-independent.

## 3. A global two-cocycle with the correct adjoint sign

Let $d$ be either of the two dual targets, and choose
the corresponding $E$. Retain a global $D_0$ with

$$
\delta D_0=x\cup w,\qquad
\delta E=-x^\dagger\cup d.
$$

Define the diagonal homotopy cochain

$$
H_x(g)=x(g)w(g).
$$

For the opposite-order product

$$
R_x(g,h)=g x(h)\,w(g),
$$

the cocycle identities for $x$ and $w$ give, by direct
expansion,

$$
\delta H_x=-x\cup w-R_x.
\tag{755.12}
$$

The trace-adjoint identity identifies
$\operatorname{tr}(R_x\cup d)$ with
$\operatorname{tr}(w\cup x^\dagger\cup d)$.
Consequently

$$
\mathcal C_d
=\operatorname{tr}\left(
 D_0\cup d+w\cup E+H_x\cup d
 \right)
\tag{755.13}
$$

is a global $2$-cocycle. Indeed the three differentials
are respectively

$$
\operatorname{tr}(x\cup w\cup d),\qquad
\operatorname{tr}(w\cup x^\dagger\cup d),\qquad
-\operatorname{tr}(x\cup w\cup d+R_x\cup d).
$$

They cancel exactly. Using $x^\dagger$ in place of
$-x^\dagger$ in the differential of $E$ would fail this
identity.

At $p$, the original gauge is $w_p=0$ as a cochain.
Thus $H_{x,p}=0$ and

$$
\operatorname{inv}_p(\mathcal C_d)
=\langle[D_{0,p}],d_p\rangle_p.
\tag{755.14}
$$

At places where both $w$ and $d$ are coboundaries, the
class in (755.13) is zero. Here is a direct verification
which also handles the $2$-local contribution. Write
$w=\delta h_0$, $d=\delta k_0$, and set

$$
D'=D_0+x\cup h_0,\qquad E'=E-x^\dagger\cup k_0.
$$

These are local cocycles. An expansion using
$x(gh)=x(g)+g x(h)$ shows that (755.13) is the
coboundary of

$$
-\operatorname{tr}(D'\cup k_0)
+\operatorname{tr}(h_0\cup E')
+L,\qquad
L(g)=\operatorname{tr}(x(g)h_0,gk_0).
\tag{755.15}
$$

For clarity, the remaining non-cup terms in that
expansion are

$$
\begin{split}
&-\operatorname{tr}(x(g_1)h_0,g_1g_2k_0-g_1k_0)\\
&\quad+\operatorname{tr}
  (g_1x(g_2)(g_1h_0-h_0),g_1g_2k_0).
\end{split}
$$

Here $g_1,g_2$ are group elements and $h_0,k_0$ are
the fixed local $0$-cochains. The displayed terms
are exactly $\delta L(g_1,g_2)$. Formula (755.15)
shows that no secondary $2$-local contribution is
left by killing the two primary cocycles.

The original coefficient cohomology at $2$ makes
both primary classes coboundaries, so this applies
there. At infinity the relevant $p$-cohomology
vanishes. Outside $\Sigma$, every cochain in (755.13)
is unramified, and the unramified group has
$p$-cohomological dimension one. These contributions
are zero as well.

## 4. The q quadratic part is an explicit cubic coboundary

On the quadratic local group, the residual coefficients
are trivial. Its restrictions of $w$ and $d$ are exactly
$w^0$ and $d^0$: any rational local $0$-cochain correction
has zero coboundary after this restriction.

First make the rational gauge adjustments from R752
and §2 and write

$$
D_0^0=\mathfrak q+R,\qquad E^0=\mathfrak p+S.
$$

Here $R$ and $S$ are rational local cocycles. The local
invariant is unchanged by these gauge adjustments.
To see this directly on the quadratic group, the
changes in (755.13) are

$$
\operatorname{tr}((xh_q)\cup d^0)
\quad\hbox{and}\quad
\operatorname{tr}(w^0\cup(yk_q)).
$$

Each has zero tame alternating product. For the first,
the values of $xh_q$ are $(-64h_q,-2ih_q)$ at
$(f,x_q)$, and those of $d^0$ are $(32i,1)$.
The two terms in the trace alternating product are
both $-64(h_q+\bar h_q)$. The second vanishes by
the same computation, or by (755.11). Restriction
multiplies local invariants by $2$, a unit modulo
$43$, so the rational local invariants are unchanged.

The trace on the original coefficient algebra is

$$
\operatorname{tr}(z,d)=z\bar d+\bar z d.
$$

For the primary representatives (755.7), the homotopy
cochain is $H_x=2\varepsilon v^2$.
Thus the part of (755.13) containing only the
quadratic representatives is

$$
\operatorname{tr}\left(
 \varepsilon v^2\cup i\bar v
 +(-\varepsilon v)\cup(-i\bar v^2)
\right).
\tag{755.16}
$$

For two group elements $g,h$, its value is

$$
i\varepsilon\left(
 \bar v(g)^2\bar v(h)+\bar v(g)\bar v(h)^2
 -v(g)^2v(h)-v(g)v(h)^2
\right).
$$

It is exactly the coboundary of

$$
\boxed{
\mathfrak c(g)=\frac{i\varepsilon}{3}
 \left(v(g)^3-\bar v(g)^3\right).
}
\tag{755.17}
$$

This follows from
$\delta(v^3)=-3(v(g)^2v(h)+v(g)v(h)^2)$
on the quadratic group. The expression in (755.17)
is in $\mathbf F_{43}$, and changes by a minus sign
under conjugation, as required for the rational
coefficient $\mathbf F_{43}(1)$. Alternatively,
the quadratic restriction already suffices to
prove the vanishing of its rational invariant.
The denominator $3$ is a unit at $43$.

After removing this cubic coboundary, the q
invariant in (755.13) is exactly

$$
\operatorname{inv}_q(\mathcal C_d)
=\langle R,d|_{G_q}\rangle_q
 +\langle w_q,S\rangle_q
=\mathscr L_q(D_0)+\langle w_q,\mathscr S_d\rangle_q.
\tag{755.18}
$$

The first equality uses the actual local dual
coordinates $(16,1)$, so its first term is
$2(a_R-16c_R)$. In particular the nonzero q
localization of $d_{\rm fl}$ has not been omitted.

## 5. Global reciprocity gives the original invariant

Apply global reciprocity to (755.13), using
(755.14), (755.15), and (755.18). For either target
$d$ one obtains

$$
\boxed{
\langle[D_{0,p}],d_p\rangle_p
+\mathscr L_q(D_0)
+\langle w_q,\mathscr S_d\rangle_q=0.
}
\tag{755.19}
$$

For $d=d_{\rm fl}$, observe that
$20+23=43$, so $20/23=-1$ in $\mathbf F_{43}$.
The first two terms of (755.19) are therefore
precisely R752's definition

$$
I_0=\mathscr L_q(D_0)
-\frac{20}{23}\langle[D_{0,p}],d_{{\rm fl},p}\rangle_p.
$$

This proves (755.3). For $d=d_q$, it proves
(755.4).

To retain the original flat correction, R746 gives

$$
\langle[D_{0,p}],d_{0,p}\rangle_p
=26\varepsilon b.
$$

Hence

$$
\begin{split}
I_0
&=I_\alpha-8\langle[D_{0,p}],d_{0,p}\rangle_p\\
&=I_\alpha-208\varepsilon b
 =I_\alpha+7\varepsilon b.
\end{split}
\tag{755.20}
$$

Substitute R752's exact exchange
$I_0=\varepsilon(21\sigma_2+2b(J_\ell-18))$.
Because $-36-7=-43$, this gives

$$
I_\alpha=\varepsilon(21\sigma_2+2bJ_\ell),
$$

as claimed. Thus the same original correction
$J_\ell\mapsto J_\ell-18$ appears in both complete
cochain descriptions with no missing scalar term.

## 6. The known reference contribution is retained explicitly

There is a further check against the actual norm
targets. Let $e_c(d_0)$ and $e_q(d_0)$ be R200's
supported dual primitives, with respective differentials
$-\ell_{\rm cyc}\cup d_0$ and
$-2i\kappa_q\cup d_0$. Then one may choose

$$
E_{\rm fl}
=E_\alpha+8e_c(d_0)-8e_q(d_0).
\tag{755.21}
$$

Its differential is exactly $y\cup(d_q-8d_0)$.
The q quadratic representative is unchanged,
because $d_{0,q}=0$.

R749 gives the actual value
$\langle w_q,e_c(d_0)_q\rangle_q=9\varepsilon$.
The original R200/R720 formula gives

$$
\langle w_q,e_q(d_0)_q\rangle_q
=\Omega_2-\langle w_q,e_p(d_0)_q\rangle_q
=\varepsilon(9+17b).
$$

Substitution in (755.21) reproduces
$I_0=I_\alpha+7\varepsilon b$.
The constant $9\varepsilon$ cancels against the
constant part of the genuine q primitive; it does
not remove the unknown $b$ term or evaluate
$\mathscr S_\alpha$.

In the original completed unit notation, the targets
being used throughout are

$$
A_\alpha=P_+[1+89460y_F],\qquad
A_{\rm fl}=A_\alpha-\frac{8i}{1848}u.
$$

The desired further construction must supply the
supported dual primitive for these actual targets
through the ordinary Gamma/scalar norm chains, or
supply an equally explicit global reciprocity
evaluation. The existence proof of §1 and the
local polynomials of §§2--4 do not by themselves
construct an ordinary global norm witness.
In particular no arbitrary q-local root is
inserted into (755.21).

## Dependencies

- [R185](R185-p-local-robert-and-principal-unit-coordinates.md),
  [R189](R189-primal-robert-generator-and-exact-local-pairings.md),
  and [R200](R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md):
  the original trace pairing, local coefficients, negative-adjoint
  convention, supported primitives, and reference correction.
- [R743](R743-original-first-moment-and-the-exact-flat-primal-secondary-slope.md):
  both complete supported cohomology spaces and the actual flat target.
- [R746](R746-original-ordinary-coefficient-as-a-strict-p-bockstein-condition.md):
  $\langle D_{0,p},d_{0,p}\rangle_p=26\varepsilon b$.
- [R749](R749-original-scalar-primitive-and-the-exact-reference-pairing.md):
  the actual $9\varepsilon$ reference pairing.
- [R752](R752-exact-Gamma-scalar-exchange-with-the-retained-second-coefficient.md):
  the intrinsic $I_0$, the rational local affine functional,
  and the retained scalar coefficient $\sigma_2$.
- J. S. Milne, *Arithmetic Duality Theorems*, second edition,
  Chapter I, Theorem 4.10(a), printed pp. 56--57:
  <https://www.jmilne.org/math/Books/ADTnot.pdf>.

