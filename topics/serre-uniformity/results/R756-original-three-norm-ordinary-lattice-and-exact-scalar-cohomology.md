# R756: the original three-norm ordinary lattice and its exact scalar cohomology class

Date: 2026-11-14. **Status: proved.** This result constructs an
integral ordinary-unit derivative cube from the same three-norm
element of R736. It also computes the exact cohomology quotient
in which the original unit $(s-1)Y$ lies, including its full
q-phase vector and its coefficient $19$. The remaining ordinary
$p$-division is isolated as an actual local-unit test. Neither
$J_\ell$, $b$, $\sigma_2$, nor $I_\alpha$ is evaluated.

Keep the original $p=43$, fields $F_t=B^S$, $N=LF_t$,
$M=LB$, and marked groups $\Gamma,S,T$. All units and divisors
are in the original completed $\mathcal O=\mathbf Z_{43}[i]$
character component, with the unaveraged $P_+$ of R561.
Put $k=\mathcal O/p$, and write all multiplicative groups
additively.

## 1. The same global three-norm element

R736 gives, with the actual original principalization $X_t$,

$$
\operatorname{div}(X_t)=P_+P_0,\qquad N_TX_t=A_\alpha,
$$

and a single global q-unit $Y$ such that

$$
\operatorname{div}_M(Y)=D_T\mathfrak q,\qquad
N_\Gamma Y=N_SY=D_TX_t.
\tag{756.1}
$$

Here $\mathfrak q=P_+Q_M$ and
$D_T=\sum_{j=0}^{42}jt^j$. Define, using this same $Y$,

$$
Z=X_t-(t-1)Y.
$$

The proved exact identities are

$$
\operatorname{div}_M Z=N_T\mathfrak q,\qquad
N_\Gamma Z=N_SZ=N_TZ=A_\alpha.
\tag{756.2}
$$

In particular there are no auxiliary prime divisors.
At $q$ the extension $M/F$ has ramification index $p$
from $\Gamma$, while $S$ is unramified and $T$ splits.
Consequently

$$
\operatorname{div}_M(A_\alpha)=pN_T\mathfrak q.
\tag{756.3}
$$

The divisor $N_T\mathfrak q$ is fixed by each of
$\Gamma,S,T$.

For $g_\Gamma=\gamma$, $g_S=s$, $g_T=t$, put

$$
D_i=\sum_{j=0}^{p-1}j g_i^j,\qquad
k_0=\frac{p-1}{2}=21,\qquad
n_0=pk_0.
$$

The exact integral identity is

$$
(g_i-1)D_i=p-N_i.
\tag{756.4}
$$

These are unbalanced derivative operators; no balanced
operator or generator shift is substituted for them.

## 2. An ordinary derivative cube, with every divisor removed

Define

$$
\mathcal U=A_\alpha-pZ,\qquad
\mathcal V_i=k_0A_\alpha-D_iZ.
\tag{756.5}
$$

All four elements are ordinary units. For $\mathcal U$,
this follows immediately from (756.2)--(756.3).
For $\mathcal V_i$, the divisor of $D_iZ$ is
$n_0N_T\mathfrak q$, because that divisor is fixed
by $g_i$. The divisor of $k_0A_\alpha$ is the same.

By (756.4),

$$
\boxed{(g_i-1)\mathcal V_i=\mathcal U.}
\tag{756.6}
$$

Moreover, for every $i,j\in\{\Gamma,S,T\}$,

$$
\boxed{N_j\mathcal U=N_j\mathcal V_i=0.}
\tag{756.7}
$$

For example $N_jA_\alpha=pA_\alpha$ and
$N_jZ=A_\alpha$. Also
$N_jD_iZ=D_iA_\alpha=n_0A_\alpha$, whether or
not $i=j$, because all operators commute.
This proves the second equality exactly over $\mathcal O$.

For distinct $i,j$, define

$$
\mathcal W_{ij}
=D_iD_jZ-pk_0^2A_\alpha.
\tag{756.8}
$$

The divisor of the first term is
$n_0^2N_T\mathfrak q=p^2k_0^2N_T\mathfrak q$.
By (756.3), the second term has exactly the same
divisor. Hence $\mathcal W_{ij}$ is an ordinary unit.
Its two exact boundaries are

$$
\boxed{
(g_i-1)\mathcal W_{ij}=-p\mathcal V_j,\qquad
(g_j-1)\mathcal W_{ij}=-p\mathcal V_i.
}
\tag{756.9}
$$

Indeed the first is
$pD_jZ-D_jA_\alpha
=pD_jZ-n_0A_\alpha=-p\mathcal V_j$.
Every one of its three norms is zero:

$$
N_l\mathcal W_{ij}=0\qquad(l=\Gamma,S,T).
\tag{756.10}
$$

Finally put

$$
\mathcal H
=D_\Gamma D_SD_TZ-p^2k_0^3A_\alpha.
\tag{756.11}
$$

Its two divisors are both
$p^3k_0^3N_T\mathfrak q$, so it too is an ordinary
unit. For $\{i,j,l\}=\{\Gamma,S,T\}$,

$$
\boxed{(g_i-1)\mathcal H=p\mathcal W_{jl},\qquad
       N_i\mathcal H=0.}
\tag{756.12}
$$

Thus all elements in (756.5), (756.8), and (756.11)
belong to the genuine ordinary unit lattice, and every
displayed boundary is an exact equality there.
No division by $p$ has yet been made.

There is also a useful factorization retaining the original
$X_t,Y$. For $i=\Gamma,S$ put

$$
\mathcal R_i=D_iY-k_0D_TX_t.
\tag{756.13}
$$

These are ordinary units: the divisors of the two terms
are respectively $n_0D_T\mathfrak q$ and
$k_0pD_T\mathfrak q$. They satisfy

$$
\mathcal V_i=(t-1)\mathcal R_i,\qquad
(\gamma-1)\mathcal R_\Gamma
=(s-1)\mathcal R_S=pY-D_TX_t.
\tag{756.14}
$$

Their $\Gamma$ and $S$ norms are zero.
These identities retain the original principalization
rather than an unspecified norm-equivalent unit.

## 3. The exact ordinary $S$-cohomology quotient

Let

$$
K_\Gamma=\ker(N_\Gamma:E_M\longrightarrow E_B),
\qquad
J_B=N_\Gamma E_M.
$$

The complete ordinary norm result R731, with R686's
primitive Robert lattice, gives

$$
E_B=\mathcal O[S,T]u_B,\qquad
J_B=(p,s-1,N_T)E_B.
\tag{756.15}
$$

Thus there is an exact sequence of integral ordinary
unit modules

$$
0\longrightarrow K_\Gamma\longrightarrow E_M
 \xrightarrow{N_\Gamma}J_B\longrightarrow0.
\tag{756.16}
$$

R715 proves both
$\widehat H^0(S,E_M)=0$ and $H^1(S,E_M)=0$.
The connecting map in the Tate sequence therefore gives
a natural isomorphism

$$
\widehat H^0(S,J_B)\xrightarrow{\sim}H^1(S,K_\Gamma).
\tag{756.17}
$$

Its sign is fixed as follows: for an $S$-invariant
$j\in J_B$, choose an ordinary $z\in E_M$ with
$N_\Gamma z=j$. The connecting cocycle has value
$(s-1)z$ at $s$.

We compute the left side integrally. The $S$ invariants
of $E_B$ are $\mathcal O[T]u_t$, where $u_t=N_Su_B$.
They all lie in $J_B$, since

$$
N_S=p-(s-1)D_S\in(p,s-1).
$$

Therefore

$$
J_B^S=\mathcal O[T]u_t,\qquad
N_SJ_B=(p,N_T)\mathcal O[T]u_t.
\tag{756.18}
$$

It follows that

$$
\boxed{
H^1(S,K_\Gamma)
\simeq\mathcal O[T]/(p,N_T)
=k[T]/(N_T).
}
\tag{756.19}
$$

This is an isomorphism of the actual $T$-modules.
The last ring is $k[t-1]/(t-1)^{42}$; its dimension
is $42$, not $43$.

For a cocycle with value $U\in K_\Gamma$ and $N_SU=0$,
the vanishing of the ordinary group $H^1(S,E_M)$
supplies an ordinary unit $z$ satisfying

$$
(s-1)z=U.
\tag{756.20}
$$

Write uniquely

$$
N_\Gamma z=f(t)u_t,\qquad f(t)\in\mathcal O[T].
\tag{756.21}
$$

The isomorphism (756.19) sends $[U]$ to the class
of $f$ modulo $(p,N_T)$.

This class is independent of $z$ in the precise integral
sense. Two choices differ by an ordinary unit in
$E_M^S=E_N$. The full ordinary lower norm image is

$$
N_\Gamma E_N=(p,N_T)\mathcal O[T]u_t,
\tag{756.22}
$$

by R633/R736. Hence their two $f$'s differ by exactly
this ideal. Conversely every element of the ideal
is the norm of such an ordinary unit and is realized
by changing $z$. This proves the complete quotient,
without a dimension argument or a field-norm substitution.

## 4. The phase map on the entire cohomology quotient

At the original q completion the residue field of
$M$ has $p$-primary roots of unity $\mu_{p^2}$.
The marked scalar action is $s=1+2p$ on them,
and $\Gamma$ is inertia. If the $p$-primary phase
of an ordinary unit $z$ is $\xi^e$, with
$\xi^p=\zeta$, then

$$
r_\mu((s-1)z)=2e,\qquad
r_\mu(N_\Gamma z)=e.
\tag{756.23}
$$

The norm raises its unit residue to the $p$-th power.
There is no uniformizer term here, because $z$ is
an ordinary unit.

For the original $u_t$, use the inverse-power convention

$$
A_u(T)=\sum_{j=0}^{42}\ell(t^ju_t)T^{-j}.
$$

R198/R619 prove

$$
A_u(1)=0,\qquad A_u'(1)=-13i.
\tag{756.24}
$$

Let $I=(T-1)k[T]$. Then $A_u=(T-1)v(T)$ for a
unit $v$, and

$$
\operatorname{Ann}(A_u)=kN_T.
\tag{756.25}
$$

Since a direct $\mu_p$ phase is $-2$ times the original
power-residue logarithm $\ell$, equations (756.21)--(756.23)
give, for every original ordinary cocycle $U$,

$$
\boxed{
A_U(T):=\sum_{j=0}^{42}r_\mu(t^jU)T^{-j}
=-4\,\bar f(T)A_u(T).
}
\tag{756.26}
$$

This descends to cohomology: an $S$ coboundary from
$K_\Gamma$ corresponds to zero norm in (756.21).
Equations (756.19), (756.25), and (756.26) prove the
explicit isomorphism

$$
H^1(S,K_\Gamma)\longrightarrow I,\qquad
[U]\longmapsto A_U,
$$

given in the marked coordinates by multiplication by
$-4A_u$. Its injectivity and surjectivity follow from
the exact annihilator and $(A_u)=I$; they are not
inferred merely from dimensions.

## 5. The full phase of the original $(s-1)Y$

Set

$$
U_Y=(s-1)Y.
$$

It is ordinary, because $S$ fixes every q prime in
$\operatorname{div}Y=D_T\mathfrak q$. Moreover

$$
N_SU_Y=0,\qquad
N_\Gamma U_Y=(s-1)D_TX_t=0,
$$

so it defines the actual class in (756.19).

For each $j\in\{0,\ldots,42\}$ let $n_j$ be the
representative of $-j$ in that set. The valuation of
$t^jY$ at the original marked prime is $n_j$.
Use the same real ray uniformizer $\theta$ as
R207/R736. It is $S$-fixed, and both
$\theta^p/q$ and $N_\Gamma\theta/q$ have zero
$p$-primary phase.

The original q finite coordinate of $d_q$ is $16K_0$.
After quadratic restriction this is $32i$. Hence, in
the same positive Kummer/Weil convention,

$$
h_q:=\ell(A_\alpha/q)=32i.
\tag{756.27}
$$

This uses the original real uniformizer convention.
It is not the logarithm of $A_\alpha$ with its pole
left in place.

Write $t^jY=n_j\theta+V_j$ locally, so $V_j$ is a unit.
The full ordinary norm relation in (756.1) gives

$$
N_SV_j=t^jD_TX_t-pn_j\theta.
$$

In the first-moment notation
$L_r=\ell(t^rX_t-\mathbf1_{r=0}A_\alpha)$,
one has $\sum_rL_r=0$ and $\sum_r rL_r=J_\ell$.
Reindexing $r=j+a$ in the derivative sum therefore yields

$$
\ell(t^jD_TX_t-n_jA_\alpha)=J_\ell.
$$

Using (756.27) and the phase of $\theta^p/q$,

$$
\ell(N_SV_j)=J_\ell+n_jh_q.
$$

The $S$ norm multiplies the $\mu_{p^2}$ exponent by
$p$, and $s-1$ acts on that exponent by $2p$.
Converting $\ell$ to the direct phase gives

$$
\begin{split}
r_\mu(t^jU_Y)
&=-4(J_\ell+n_jh_q)\\
&=\boxed{-4J_\ell-ij}.
\end{split}
\tag{756.28}
$$

The term $-ij$ is essential. Only at $j=0$ does the
formula reduce to R736's $-4J_\ell$. The pole cannot
be discarded at the other $42$ T translates.

In $k[T]$, using $T^{-j}$ as in (756.24),

$$
\sum_{j=0}^{42}jT^{-j}=-D_T,
$$

so the complete vector (756.28) is

$$
\boxed{A_{U_Y}(T)=-4J_\ell N_T+iD_T.}
\tag{756.29}
$$

This is not a constant phase vector.

## 6. The exact marked class and the coefficient 19

Apply (756.20)--(756.21) to $U_Y$. Its exact
cohomology class is the unique $\bar f\in k[T]/(N_T)$
satisfying

$$
\boxed{
\bar f A_u
=J_\ell N_T-\frac i4D_T.
}
\tag{756.30}
$$

Existence follows from the actual ordinary $z$ in
(756.20); uniqueness also follows directly from
(756.25). The formula is not a freely selected
solution of a local norm equation.

For a precise leading coefficient, put $X=T-1$.
In characteristic $43$,

$$
N_T=X^{42},\qquad
D_T=T\frac{dN_T}{dT}=-X^{41}-X^{42}.
$$

Write $A_u=X(v_0+v_1X+\cdots)$ with
$v_0=-13i$. Dividing (756.30) by this unit after
removing the one factor $X$ gives

$$
\bar f
=19X^{40}
+\left(\frac{J_\ell+i/4}{v_0}
       -19\frac{v_1}{v_0}\right)X^{41}
\pmod{X^{42}}.
\tag{756.31}
$$

Indeed its leading coefficient is

$$
\frac{i/4}{-13i}=-\frac1{52}
=-\frac19=19\pmod{43}.
$$

In particular,

$$
\boxed{(T-1)[U_Y]\ \leftrightarrow\ 19(T-1)^{41}}
\tag{756.32}
$$

under the fixed isomorphism (756.19).
This is an actual normalized statement about the
original class; its next coefficient still contains
the unknown $J_\ell$.

Changing the ordinary unit $z$ in (756.20) changes
$f$ by precisely $(p,N_T)$, as proved in §3.
Changing $Y$ with the same $X_t$, divisor, and two
norms changes $U_Y$ by an $S$ coboundary from
$K_\Gamma$, because the difference of the two
$Y$'s is an ordinary unit of $\Gamma$ norm zero.
If $X_t$ is changed within its original exact
principalization torsor, the reconstructed moment
$J_\ell$ is unchanged. Formula (756.28) is therefore
unchanged, and the injective map (756.26) proves
that the cohomology class is unchanged as well.
These checks include the actual ordinary ambiguity,
not only the value at the one prime with $n_0=0$.

For the finite-flat target, R736 gives the same
construction with $J_\ell$ replaced by
$J_\ell-18$. The correction is an ordinary base unit
of zero q phase, so $h_q$ and the $-ij$ term stay
unchanged. Equations (756.30)--(756.32) apply with
this replacement. No comparison with $b$ is made.

## 7. The exact ordinary p-division test

R700 proves the actual exact sequence

$$
0\longrightarrow E_M\longrightarrow U_M
 \xrightarrow{\operatorname{Art}_p}X_M^{(p)}
 \longrightarrow A_M\longrightarrow0
$$

and proves that $X_M^{(p)}$ is torsion-free over
$\mathcal O$. It follows that the ordinary unit
lattice is $p$-saturated in the full semilocal
principal-unit lattice:

$$
\boxed{E_M\cap pU_M=pE_M.}
\tag{756.33}
$$

To verify this implication, if $pu$ lies in $E_M$,
then $p\operatorname{Art}_p(u)=0$ in the torsion-free
module $X_M^{(p)}$. Hence
$\operatorname{Art}_p(u)=0$, so $u\in E_M$ by
exactness. The reverse inclusion is immediate.

For the concrete units of §2, this gives the exact
test

$$
\mathcal W_{ij}\in pE_M
\quad\Longleftrightarrow\quad
\operatorname{loc}_p(\mathcal W_{ij})\in pU_M.
\tag{756.34}
$$

If it holds, the ordinary unit
$\mathcal L_{ij}=-\mathcal W_{ij}/p$ satisfies

$$
(g_i-1)\mathcal L_{ij}=\mathcal V_j,\qquad
(g_j-1)\mathcal L_{ij}=\mathcal V_i,\qquad
N_l\mathcal L_{ij}=0.
$$

The division is then in the actual ordinary lattice.
It is not justified by taking an arbitrary local
$p$-th root.

The three prescribed norms alone do not force the
right side of (756.34). This can already be seen in
the free semilocal model
$\mathcal O[\Gamma,S,T]$. A change

$$
\delta Z=(\gamma-1)(s-1)(t-1)e
$$

has all three norms zero. Modulo $p$, its effect on
$\mathcal W_{\Gamma S}$ is

$$
D_\Gamma D_S\delta Z
=N_\Gamma N_S(t-1)e,
$$

which is nonzero for a free group-ring basis vector
$e$. This example concerns the semilocal norm
constraints; it does not assert that the arbitrary
$e$ is a global unit. It explains why the global
ordinary image and the actual $p$-flat condition
must still be imposed.

## 8. Connection to the original dual primitive, and the remaining input

The ordinary unit $\mathcal U=A_\alpha-pZ$ represents
the restriction of the original Kummer class
$d_q=\kappa(A_\alpha)$ to $M$, since subtracting
$pZ$ does not change that Kummer class.

If $E_\alpha$ is the genuine supported dual primitive
of R755, its restriction to $G_M$ is a cocycle.
The cochain equation

$$
\delta E_\alpha=(2\kappa_S-2i\kappa_q)\cup d_q
$$

implies the following exact conditions on that
restricted Kummer class $e_\alpha$:

$$
(s-1)e_\alpha=2[\mathcal U],\qquad
(\gamma-1)e_\alpha=-2i[\mathcal U],\qquad
(t-1)e_\alpha=0.
\tag{756.35}
$$

For example the cocycle $(d_q,E_\alpha)$ has
off-diagonal Galois action
$-(2\kappa_S-2i\kappa_q)$; invariance of its
restriction gives (756.35). Equivalently the same
formulas follow by expanding the original
inhomogeneous cochain identity under conjugation.

The three individual ordinary primitives
$\mathcal V_i$ do not automatically solve this
simultaneous system: their cross derivatives remain.
The mixed units $\mathcal W_{ij}$ record exact
integral positions at which a division by $p$ would
produce compatible further primitives. Formula
(756.34) specifies the genuine ordinary test for
such a division. It has not been evaluated here.

In particular (756.19) is not identified with the
ordinary class-action coefficient $b$ by an
abstract module shape. R752--R755 still retain the
actual second scalar coefficient $\sigma_2$ and
the regularized global pairing $I_\alpha$.
Further work must compute the original unit
coordinates or prove the necessary global
$p$-flat compatibility in the simultaneous system.
The local phase (756.29), the known scalar input,
and the abstract ordinary class lengths do not
supply that missing comparison.

## Dependencies

- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md)
  and [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  original q phase conventions and $A_u'(1)=-13i$.
- [R633](R633-complete-ordinary-unit-lattice-in-the-anti-pq-layer.md):
  the complete lower ordinary unit lattice and norm image.
- [R700](R700-p-ramified-free-lattices-and-the-retained-ordinary-quotient.md):
  the actual p-local sequence and torsion-free ramified module.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md):
  both vanishing cyclic ordinary $S$ Tate groups.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the full ordinary Gamma norm image.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md):
  the same $X_t,Y,Z$, their exact ordinary corrections,
  and the real q uniformizer.
- [First-moment reconstruction](../notes/2026-11-14-r599-first-moment-normalization-reconstruction.md):
  the exact principalization torsor, moment, and flat correction.
- [R752](R752-exact-Gamma-scalar-exchange-with-the-retained-second-coefficient.md)
  and [R755](R755-exact-dual-Gamma-scalar-primitive-for-the-original-flat-target.md):
  the retained scalar curvature and the true supported dual primitive.

