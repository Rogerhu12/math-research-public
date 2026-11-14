# R758: a natural ordinary cocycle map and the original first-moment torsor

Date: 2026-11-14. **Status: proved.** There is a natural map from
the original ordinary $P$ cohomology into the socle of the ordinary
$S$ cohomology computed in R756. Its values on the two original
Robert cocycles are computed below with their actual signs. The
original first moment is the remaining coordinate of an
antiderivative torsor for this map. This result does not evaluate
$J_\ell$ or $b$, and does not identify a finite-flat local condition
with an arbitrary choice of antiderivative.

## 1. The actual ordinary modules and their marked coordinates

Retain $p=43$, $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/p$,
$P=S\times T=\langle s,t\rangle$, $M=LB$, and
$\Gamma=\langle\gamma\rangle$ from R561/R657. Write
$\pi=\gamma-1$. All modules are the original completed ordinary
unit modules in the character component selected by the
unaveraged $P_+=44e_{\chi^-}$. Multiplicative groups are written
additively. In particular no field-norm preimage is being called
an ordinary unit preimage.

Put $E=E_M$ and

$$
K_\Gamma=\ker(N_\Gamma:E\longrightarrow E_B),\qquad
J_B=N_\Gamma E.
$$

The full ordinary norm theorem R731 gives

$$
E_B=\mathcal O[S,T]u_B,\qquad
J_B=(p,s-1,N_T)E_B.
\tag{758.1}
$$

Use the same actual descendants

$$
u_s=N_Tu_B,\qquad u_t=N_Su_B,\qquad
u=N_Pu_B=N_Tu_t=N_Su_s.
$$

R715 supplies $H^1(S,E)=\widehat H^0(S,E)=0$ and

$$
H^1(P,E)\simeq A_M/\pi A_M\simeq k.
\tag{758.2}
$$

The group actions in (758.1)--(758.2) are the actual commuting
actions. In particular the assertions about integral invariant
unit lattices do not replace those lattices by rational spans.

For $D_S=\sum_{j=0}^{42}js^j$ and
$D_T=\sum_{j=0}^{42}jt^j$, R756 computes the positive connecting
map of the exact sequence

$$
0\longrightarrow K_\Gamma\longrightarrow E
 \xrightarrow{N_\Gamma}J_B\longrightarrow0.
\tag{758.3}
$$

It gives the marked isomorphism

$$
H^1(S,K_\Gamma)\simeq
\widehat H^0(S,J_B)
\simeq\mathcal O[T]/(p,N_T)
=k[X]/X^{42},\qquad X=t-1.
\tag{758.4}
$$

The sign convention is explicit: if an ordinary unit $z$ satisfies
$N_\Gamma z=h(t)u_t$, its connecting cocycle has value
$(s-1)z$ at $s$ and corresponds to $\bar h$ in (758.4).
Here

$$
J_B^S=\mathcal O[T]u_t,\qquad
N_SJ_B=(p,N_T)\mathcal O[T]u_t.
\tag{758.5}
$$

Thus the actual $T$-fixed part of (758.4) is exactly its socle:

$$
H^1(S,K_\Gamma)^T=kX^{41}.
\tag{758.6}
$$

## 2. The norm of every original $P$ cocycle is a coboundary

Retain the original balanced operator and coefficient

$$
D=D_\Gamma^{\rm bal}=\sum_{j=-21}^{21}j\gamma^j,
\qquad a=15i/7.
$$

The ordinary units $y,c_s,c_t$ and the two original cocycles are

$$
\begin{aligned}
v_s&=u_s-y+aDc_s,& f_s(s)&=v_s,& f_s(t)&=0,\\
v_t&=u_t-y+aDc_t,& f_t(s)&=0,& f_t(t)&=v_t.
\end{aligned}
\tag{758.7}
$$

Their defining exact identities include $N_\Gamma y=u$ and
$N_\Gamma D=0$. Consequently

$$
\begin{aligned}
N_\Gamma v_s&=pu_s-u=(s-1)D_Su_s,\\
N_\Gamma v_t&=pu_t-u=(t-1)D_Tu_t.
\end{aligned}
\tag{758.8}
$$

These give actual $J_B$-valued coboundaries. Indeed
$u_s=N_Tu_B\in J_B$, and

$$
u_t=N_Su_B,\qquad N_S=p-(s-1)D_S\in(p,s-1),
$$

so $u_t\in J_B$ as well. Therefore

$$
N_\Gamma f_s=\delta(D_Su_s),\qquad
N_\Gamma f_t=\delta(D_Tu_t)
\quad\hbox{in }C^1(P,J_B),
\tag{758.9}
$$

where $\delta j(g)=(g-1)j$. Their other components are zero
because $u_s$ is $T$-fixed and $u_t$ is $S$-fixed.

It is necessary to know this for every class, rather than only for
the two displayed representatives. R619/R715 identify the
ordinary class of $f_t$ as $9e_q\ne0$, and (758.2) says the
whole $H^1(P,E)$ is one-dimensional over $k$. Hence $[f_t]$
generates this actual group. The norm homomorphism

$$
H^1(P,E)\xrightarrow{N_\Gamma}H^1(P,J_B)
$$

is $\mathcal O$-linear and kills $[f_t]$ by (758.9).
It therefore vanishes identically. It follows that for every
$f\in Z^1(P,E)$ there is an actual $j_0\in J_B$ such that

$$
N_\Gamma f=\delta j_0.
\tag{758.10}
$$

This argument uses the known nonzero original auxiliary class
only to prove generation. It does not substitute its coefficient
$9$ for the independent scalar coefficient $C$.

## 3. A natural map, with the full integral ambiguity removed

For $f\in Z^1(P,E)$ choose $j_0$ as in (758.10), and then an
ordinary unit $z_0\in E$ with $N_\Gamma z_0=j_0$.
The latter exists by the definition of the proved image $J_B$.
The cocycle

$$
F=f-\delta z_0
\tag{758.11}
$$

takes its values in $K_\Gamma$. Define

$$
\psi([f])=[F|_S]\in H^1(S,K_\Gamma).
\tag{758.12}
$$

We prove independence of all choices integrally.

First, with $j_0$ fixed, two choices of $z_0$ differ by an
ordinary element of $K_\Gamma$. Their full $P$ cocycles
differ by a coboundary from that same module.

Second, two choices of $j_0$ differ by $J_B^P$. The regular
ordinary lattice $E_B=\mathcal O[P]u_B$ has invariants
$E_B^P=\mathcal O u$: in a regular integral group ring,
invariance says that all coefficients are equal. Since
$u=N_Tu_t\in J_B$, this proves the exact equality

$$
J_B^P=\mathcal O u.
\tag{758.13}
$$

If $j_0$ is changed to $j_0+c u$, there is an actual
$P$-invariant ordinary norm lift of this change: use $cy$,
because $y\in E_L=E^P$ and $N_\Gamma y=u$.
Replacing $z_0$ by $z_0+cy$ leaves the entire corrected
$P$ cocycle (758.11) unchanged. Any other norm lift differs
from this one by $K_\Gamma$ and is covered by the first
check. After restricting to $S$, the same vanishing is
also visible as $cN_T=0$ in (758.4), or as
$c u\in N_SJ_B$ in (758.5).

Third, replacing $f$ by $f+\delta e$ for an ordinary $e\in E$
is absorbed by replacing $j_0$ with $j_0+N_\Gamma e$ and
$z_0$ with $z_0+e$. The corrected cocycle in (758.11) is
then exactly unchanged. These three checks prove that $[F]$
is well defined in $H^1(P,K_\Gamma)$ and that $\psi$ is
a well-defined $\mathcal O$-linear map on cohomology.

In fact the preceding facts identify the map even before
restriction. The invariants map $E^P\to J_B^P$ is onto,
by the actual norm preimage $y$. The degree-one norm map
is zero by §2. The long exact sequence of (758.3) therefore
gives the natural isomorphism

$$
H^1(P,K_\Gamma)\xrightarrow{\sim}H^1(P,E).
$$

Its inverse is $[f]\mapsto[F]$, and $\psi$ is that inverse
followed by the usual restriction to $S$.

Its image is $T$-fixed. In fact (758.11) is a $P$ cocycle
with values in $K_\Gamma$, so, writing
$A=F(s)$ and $B=F(t)$, the commutativity of $s,t$ gives

$$
(t-1)A=(s-1)B.
$$

The right side is an $S$ coboundary in $K_\Gamma$.
Consequently

$$
\boxed{\psi:H^1(P,E)\longrightarrow
H^1(S,K_\Gamma)^T=kX^{41}.}
\tag{758.14}
$$

This construction is also the natural lift-and-restrict map
from the long exact sequence of (758.3). The preceding
integral calculation of $J_B^P$ is what makes it independent
of the possible lifts; the mere equality of dimensions would
not do so.

## 4. The exact image of the original anti-p cocycle

For $f=f_t$ use the nullhomotopy $j_0=D_Tu_t$ supplied by
(758.9), and choose an ordinary $z_0$ with that norm.
Since $f_t(s)=0$, the restricted corrected cocycle is

$$
F(s)=-(s-1)z_0.
$$

The ordinary primitive $-z_0$ has
$N_\Gamma(-z_0)=-D_Tu_t$. By the positive convention
fixed in (758.4),

$$
\psi([f_t])=-D_T\pmod{(p,N_T)}.
\tag{758.15}
$$

In characteristic $p=43$, inside $k[T]$,

$$
N_T=X^{42},\qquad
D_T=T\frac{dN_T}{dT}=-X^{41}-X^{42}.
$$

Therefore the exact marked value is

$$
\boxed{\psi([f_t])=X^{41}.}
\tag{758.16}
$$

In particular $\psi$ is an isomorphism onto the actual socle:
it is nonzero on the known generator of (758.2). The minus
sign in (758.15) comes from subtracting the ordinary norm
lift in (758.11); it is not an Artin or reciprocity convention.

## 5. The exact image of the original scalar cocycle

For $f=f_s$ use $j_0=D_Su_s$. Since $H^1(S,E)=0$, choose
an ordinary $z_s\in E$ with

$$
(s-1)z_s=v_s.
\tag{758.17}
$$

Equation (758.8) shows that
$N_\Gamma z_s-D_Su_s$ is $S$-invariant. The exact invariant
lattice of $E_B$ is $\mathcal O[T]u_t$, so there is a unique
$h_s(t)\in\mathcal O[T]$ with

$$
N_\Gamma z_s=D_Su_s+h_s(t)u_t.
\tag{758.18}
$$

If $z_0$ is the ordinary lift of $D_Su_s$ used in §3, then
$z_s-z_0$ is an ordinary primitive of the corrected
$S$ cocycle. Thus

$$
\psi([f_s])=\bar h_s\pmod{N_T}.
\tag{758.19}
$$

We now compute this class using the original full q-phase
convention. R561 gives the direct $\mu_p$ phase of $u_s$
as $25$, and writes that of $y$ as $r_y$. At q, $\Gamma$
is inertia and the balanced operator $D$ has augmentation
zero, so $Dc_s$ has zero phase. Every term of $v_s$ is
$T$-fixed. Hence at all $43$ marked translates,

$$
r_\mu(t^jv_s)=25-r_y.
\tag{758.20}
$$

For an ordinary local unit with $\mu_{p^2}$ phase $\xi^e$,
$s-1$ multiplies the exponent by $2p$, whereas its
$\Gamma$ norm raises its residue to the $p$th power.
Converting the resulting direct $\mu_p$ exponent to the
original logarithm by $r_\mu=-2\ell$ gives the factor $-4$
in R756. There is no pole or uniformizer term for $z_s$.
Furthermore $D_Su_s$ has zero phase: $u_s$ has
$\mu_p$ phase and $\sum_{j=0}^{42}j=43\cdot21$.

With the original inverse-power polynomial

$$
A_u(T)=\sum_{j=0}^{42}\ell(t^ju_t)T^{-j}
       =X(v_0+v_1X+\cdots),\qquad v_0=-13i,
$$

equations (758.18)--(758.20) therefore give

$$
-4\bar h_s A_u=(25-r_y)N_T,
\qquad
\bar h_s A_u=\frac{r_y-25}{4}N_T.
\tag{758.21}
$$

Since $A_u=X$ times a unit and $N_T=X^{42}$, this uniquely
determines $\bar h_s$ modulo $X^{42}$:

$$
\bar h_s
=\frac{r_y-25}{4(-13i)}X^{41}
=\frac{i(r_y-25)}9X^{41}.
\tag{758.22}
$$

The scalar reciprocity normalization of R561 is
$C=i(r_y-25)$, and the complete original chain comparison
R720 proves $C=9ib$. Hence

$$
\boxed{\psi([f_s])=\frac C9X^{41}=ibX^{41}.}
\tag{758.23}
$$

This computation uses the actual ordinary primitive (758.17),
the exact norm nullhomotopy $D_Su_s$, and all original
phase constants. It does not choose an isomorphism between
two abstract one-dimensional spaces after seeing $C/9$.
The value in (758.23) is also consistent with the original
$\Theta$ ratio of R720, with the common sign fixed by
(758.15).

Changing $z_s$ by an $S$-fixed ordinary unit changes $h_s$
by exactly $(p,N_T)\mathcal O[T]$: the full lower norm
image is $N_\Gamma E_M^S=(p,N_T)\mathcal O[T]u_t$.
Thus (758.21)--(758.23) respect the entire integral
ordinary ambiguity, not only its phase at one prime.

## 6. The original first moment is an antiderivative torsor coordinate

Let $Y$ be the same ordinary-principalization construction
of R736/R756, and put $U_Y=(s-1)Y$. Its divisor is zero,
$N_\Gamma U_Y=N_SU_Y=0$, and R756 defines its canonical
class

$$
\eta_\alpha=[U_Y]\in H^1(S,K_\Gamma).
$$

With $J_\ell$ the original marked moment, R756 proves

$$
\eta_\alpha\ \leftrightarrow\
19X^{40}
+\left(\frac{J_\ell+i/4}{v_0}
       -19\frac{v_1}{v_0}\right)X^{41}
\pmod{X^{42}}.
\tag{758.24}
$$

Multiplication by $X$ and (758.16) give the actual comparison

$$
\boxed{(t-1)\eta_\alpha=19\,\psi([f_t]).}
\tag{758.25}
$$

The set of solutions of (758.25) in the full group
$H^1(S,K_\Gamma)$ is precisely

$$
19X^{40}+kX^{41}
=19X^{40}+\psi(H^1(P,E)).
\tag{758.26}
$$

Indeed multiplication by $X$ on $k[X]/X^{42}$ has kernel
$kX^{41}$, and (758.16) identifies that kernel using the
original $f_t$. Equivalently there is an exact sequence

$$
0\longrightarrow H^1(P,E)
 \xrightarrow{\psi}H^1(S,K_\Gamma)
 \xrightarrow{\,t-1\,}(t-1)H^1(S,K_\Gamma)
\longrightarrow0.
\tag{758.27}
$$

The original $\eta_\alpha$ is a fixed point of this affine
torsor, determined by its original principalization and norm
target. Its coordinate in (758.24) is not freely adjustable
while retaining those data. The remaining coordinate contains
$J_\ell$; equation (758.25) alone does not determine it.

## 7. Exact displacement under the original finite-flat correction

There is a useful marked displacement formula for changing
the target, distinct from changing an ordinary witness for
the same target. Let $c\in\mathbf Z_p$ and replace the target
by the actual base-unit correction

$$
A(c)=A_\alpha+\frac{ci}{1848}u.
\tag{758.28}
$$

The original $T$ principalization changes by
$\frac{ci}{1848}u_t$. Since
$\ell(D_Tu_t)=13i$ and $1848\equiv-1\pmod{43}$, its
moment changes by

$$
J_\ell(c)=J_\ell+13c\pmod{43}.
\tag{758.29}
$$

The correction has zero base q phase, so the pole contribution
$-ij$ in the full phase vector of R756 is unchanged. Apply
the same $Y$ construction and let $\eta(c)$ denote its class.
Subtracting (758.24) for the two targets gives

$$
\boxed{\eta(c)-\eta_\alpha
=icX^{41}=ic\,\psi([f_t]).}
\tag{758.30}
$$

This formula depends only on $c\bmod43$; changing the
integral lift changes neither class. For the actual R185
finite-flat target, $c=-8$. Therefore

$$
\boxed{
\eta_{\rm fl}-\eta_\alpha=-8i\,\psi([f_t]),\qquad
J_{\rm fl}=J_\ell-18.
}
\tag{758.31}
$$

Thus the original finite-flat correction is now located
inside the same natural ordinary cohomology module as the
two original Robert cocycles. This is an exact displacement
between two already specified points. It does not choose
an origin or a section of the torsor (758.26).

## 8. The precise remaining arithmetic

The cocycle images (758.16), (758.23), the exact sequence
(758.27), and the flat displacement (758.31) are all proved
with their ordinary integral choices accounted for.
They hold as well when $b=0$; then $\psi([f_s])=0$,
while $\psi([f_t])$ remains the nonzero marked socle
generator. The actual endpoint $m=43$ was already proved
in R715. No extra hypothesis that $t-1$ have its first
possible nonzero valuation is used here.

What is still required is the actual map from the original
$p$-local finite-flat normalization to a section or a
linear functional on this ordinary antiderivative torsor.
Neither its existence nor its value follows from
one-dimensionality of the socle. In particular, an arbitrary
section of multiplication by $t-1$ would arbitrarily change
the surviving $J_\ell$ coordinate.

The simultaneous ordinary division tests of R756 and the
dual exchange invariants of R752/R755 retain that input.
This result does not set the independent second scalar
coordinate $\sigma_2$ to zero and does not evaluate
$I_\alpha$. The full $J_\ell/b$ comparison remains open.

## Dependencies

- [R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md):
  the actual scalar cocycle, direct phase $25$, and genus normalization.
- [R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md):
  the actual auxiliary class $9$, inverse-power convention, and $A_u'(1)=-13i$.
- [R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md):
  the natural ordinary cohomology and the actual endpoint $m=43$.
- [R720](R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md):
  the original integral chain comparison $C=9ib$.
- [R731](R731-complete-ordinary-Gamma-norms-and-marked-q-principalizations.md):
  the exact ordinary image $J_B$.
- [R736](R736-original-three-norm-exchange-and-minus-four-moment-phase.md):
  the original common norm construction.
- [R756](R756-original-three-norm-ordinary-lattice-and-exact-scalar-cohomology.md):
  the exact scalar cohomology, full phase vector, and coefficient $19$.
- [The reconstructed first-moment note](../notes/2026-11-14-r599-first-moment-normalization-reconstruction.md):
  the ordinary principalization torsor and the actual finite-flat correction.
