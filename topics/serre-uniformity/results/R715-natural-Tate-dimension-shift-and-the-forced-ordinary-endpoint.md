# R715: natural Tate dimension shift forces the ordinary endpoint m = 43

Date: 2026-11-14. **Status: proved.** All groups below are the original
completed ordinary character groups of R561/R633/R657/R700, with the
same $p=43$, original $q$, positive $\Gamma$ marking, and unaveraged
projector. No new computation or substitute norm unit is used.

The actual ordinary class length is

$$
\boxed{m=43,\qquad A_{M'}\simeq R_\Gamma/\pi^{43}.}
\tag{715.1}
$$

Consequently the scalar ordinary unit norm is onto, and the full
two-direction ordinary norm has the exact image

$$
\boxed{N_SE_{M'}=E_N,\qquad
N_SN_TE_{M'}=(p,\pi)E_L.}
\tag{715.2}
$$

In particular the original $y$ is an ordinary $S$-norm. These facts
do not evaluate $C,J,b,\mathcal L$, nor do they by themselves prove
the old bridge $C=-34ib=9ib$. The proof retains the finite ordinary
quotient in R700 and uses its natural integral cohomology.

## 1. The exact lattices, invariant group, and commuting actions

Put

$$
\mathcal O=\mathbf Z_{43}[i],\quad k=\mathcal O/p,\quad
R_0=\mathcal O[\Gamma],\quad
R_\Gamma=R_0/(N_\Gamma),\quad \pi=\gamma-1,
$$
$$
P=S\times T=\langle s,t\rangle\simeq C_p^2,\qquad
M'=LB,\qquad N=(M')^S.
$$

Here $E_V=(\mathcal O_V^\times\otimes_{\mathbf Z}\mathcal O)_{\chi^-}$
means the full completed ordinary unit lattice. R210 proves

$$
E_L=R_0y,\qquad N_\Gamma y=u.
\tag{715.3}
$$

R700 gives the actual reciprocity sequence

$$
0\longrightarrow E:=E_{M'}
\longrightarrow U:=U_{M'}
\longrightarrow X:=X_{M'}^{(p)}
\longrightarrow A:=A_{M'}\longrightarrow0,
\tag{715.4}
$$

where $U\simeq\mathcal O[P]^{86}$ and
$X\simeq\mathcal O[P]^{43}$. All arrows are the actual localization,
reciprocity, and ordinary-class maps. In particular $A$ is retained;
there is no replacement of an ordinary norm by a field norm.

The extensions defining $M'/K$ are abelian. Thus the actual
$\Gamma$ and $P$ actions commute, including on local units,
reciprocity, ordinary units, and ordinary ideal classes. A choice of
free $P$-bases for $U$ or $X$ need not respect $\Gamma$; none will
be made in the dimension-shift argument.

We also have the full integral equality

$$
E^P=E_L.
\tag{715.5}
$$

Indeed $(\mathcal O_{M'}^\times)^P=\mathcal O_L^\times$ before
completion. Taking invariants is the kernel of the finitely many
endomorphisms $g-1$, and tensoring a finitely generated abelian group
with the flat $\mathbf Z$-module $\mathcal O$ preserves that kernel.
The tame character projector commutes with $P$. Hence (715.5)
holds after completion and projection, with no hidden finite-index
overlattice. There is no $p$-power root of unity: the absolute degree
$88p^3$ of $M'$ is not divisible by $p-1=42$, so it cannot contain
$\mu_p$. Prime-to-$p$ torsion disappears on completion. This also
shows that the unit modules in (715.4) are torsion-free over
$\mathcal O$.

## 2. Natural dimension shift, including its R0 linearity

Let $I=\operatorname{im}(U\longrightarrow X)$. Split (715.4) into

$$
0\longrightarrow E\longrightarrow U\longrightarrow I\longrightarrow0,
\qquad
0\longrightarrow I\longrightarrow X\longrightarrow A\longrightarrow0.
\tag{715.6}
$$

For every subgroup $H\le P$, the restrictions of $U$ and $X$
are free $\mathcal O[H]$-modules. Their Tate cohomology vanishes
in every degree. The connecting maps of (715.6) therefore give
canonical isomorphisms

$$
\boxed{\widehat H^j(H,E)\simeq
\widehat H^{j-2}(H,A)\qquad(j\in\mathbf Z).}
\tag{715.7}
$$

This assertion includes negative degrees, restriction, and
corestriction. All the short exact sequences are sequences of
modules with the commuting $\Gamma$ action. Connecting maps
are natural for each $\gamma$, so (715.7) is $R_0$-linear.
It does not assert that an arbitrary $P$-free isomorphism of
the middle lattices is $\Gamma$-linear.

For $H=P$ and $j=0$, Tate degree $-2$ is ordinary group
homology in degree $1$. Thus

$$
\boxed{E_L/N_PE\simeq H_1(P,A)
\quad\hbox{as }R_0\hbox{-modules}.}
\tag{715.8}
$$

The left hand side is a quotient of the actual cyclic
$R_0$-module (715.3). This cyclicity is the decisive extra
condition; it is stronger than an equality of orders of
cohomology groups.

## 3. The integral degree-one homology calculation

Use the standard two-periodic integral resolution of a cyclic
group, with differentials $h-1,N_H,h-1,N_H,\ldots$. Tensor the
resolutions for $S$ and $T$ over $\mathbf Z$, with the
usual total-complex sign. The resolutions are free over
$\mathbf Z$, so this gives a free integral resolution for
the product $P$. In degrees $2,1,0$, after tensoring with
the actual module $A$, its maps are

$$
A^3\xrightarrow{d_2} A^2\xrightarrow{d_1} A,
$$
$$
d_1(x,z)=(s-1)x+(t-1)z,
$$
$$
d_2(c,d,e)=
\bigl(N_Sc-(t-1)d,\ (s-1)d+N_Te\bigr).
\tag{715.9}
$$

This is an integer resolution: the operators $N_S,N_T$
have not been replaced by zero or by $p$ until their
actual action on the specified $A$ is checked. The same
standard bases give the $\Gamma$ action only on the
coefficients $A$, so every subsequent map is $R_0$-linear.

R657 proves

$$
A=R_\Gamma/\pi^m,\qquad 1\le m\le43.
\tag{715.10}
$$

If $m\ge2$, it proves for the original marked generators

$$
s-1=\pi\alpha_S,\quad \alpha_S\bmod\pi=i,\qquad
t-1=\pi\alpha_T,\quad \alpha_T\bmod\pi=b\in\mathbf F_p.
\tag{715.11}
$$

Here $\alpha_S$ is a unit of $A$; $\alpha_S,\alpha_T$
denote action coefficients, not ordinary Robert units.
For $m=1$, both $s,t$ act
trivially, and no coefficient $b$ is assigned.

## 4. Every length below 43 contradicts the cyclic ordinary norm quotient

First suppose $m=1$. Then $A=k$, both augmentation
operators vanish, and both norm operators are multiplication
by $p=0$ on $A$. Both maps in (715.9) are zero. Hence

$$
H_1(P,A)=k^2,
\tag{715.12}
$$

with trivial $\Gamma$ action. This case uses no fictitious
first-order coefficient.

Now suppose $2\le m\le42$. In $R_\Gamma$,
$v_\pi(p)=42$, so $pA=0$. For any action
$h=1+\pi c$ with $c$ integral, its cyclic norm is the
polynomial

$$
N_h=\sum_{j=1}^{p}\binom pj(\pi c)^{j-1}.
\tag{715.13}
$$

Every term has valuation at least $42$. This includes
$c=0$, where the displayed polynomial is exactly $p$.
Therefore $N_S=N_T=0$ on $A$.

Choose $\eta\in A$ such that $\alpha_T=\alpha_S\eta$. Then
$t-1=(s-1)\eta$. The choice is only relevant modulo the
annihilator of $\pi$, and any one choice suffices for the
following $R_\Gamma$-linear calculation. Write

$$
K=\operatorname{Ann}_A(\pi)=\pi^{m-1}A\simeq k.
$$

The change of variables

$$
(x,z)\longmapsto (z,w=x+\eta z)
\tag{715.14}
$$

identifies $\ker d_1$ with $A\oplus K$. The only
nonzero type of boundary in (715.9) is
$(-(t-1)d,(s-1)d)$; under (715.14) it is
$(\pi\alpha_S d,0)$. Since $\alpha_S$ is a unit, these
boundaries are exactly $\pi A\oplus0$. Thus

$$
\boxed{H_1(P,A)\simeq
(A/\pi A)\oplus \operatorname{Ann}_A(\pi)
\simeq k\oplus k}
\tag{715.15}
$$

as $R_\Gamma$-modules, not only as groups. In particular
$\pi$ acts as zero on both summands.

The local ring $R_0=\mathcal O[C_p]$ has maximal ideal
$(p,\pi)$. The module $k\oplus k$, on which this maximal
ideal acts as zero, requires two generators. It cannot be a
quotient of the cyclic $R_0$-module $R_0y$. Equations
(715.8), (715.12), and (715.15) therefore exclude every
$1\le m\le42$. The upper bound (715.10) proves (715.1).

This argument does not infer the ordinary quotient from a
free $p$-ramified module alone. It uses the full exact
sequence, its natural two-step connecting isomorphism, and
the separately proved cyclic **ordinary** invariant lattice.

## 5. The endpoint calculation retains the term that removes the second line

It is useful to check the actual endpoint in the same
integer resolution. In $R_\Gamma$,

$$
\frac p{\pi^{42}}\equiv-1\pmod\pi.
\tag{715.16}
$$

For $s=1+\pi\alpha_S$, (715.13) therefore gives

$$
\frac{N_S}{\pi^{42}}
\equiv \alpha_S^{42}-1
\equiv i^{42}-1=-2\pmod\pi.
\tag{715.17}
$$

Consequently $N_SA=\pi^{42}A=\operatorname{Ann}_A(\pi)$
when $m=43$. This is a nonzero line. It would be lost
if one reduced the integer resolution modulo $p$ too early.

Apply the change of variables (715.14) again. The mixed
boundary kills $\pi A\oplus0$, and the $N_S$ boundary
kills $0\oplus K$. The $N_T$ boundary cannot kill the
remaining $A/\pi A$ term: (715.13) shows its first
coordinate is in $\pi^{42}A\subset\pi A$. Thus

$$
\boxed{H_1(P,A)\simeq k,\qquad
E_L/N_PE\simeq k.}
\tag{715.18}
$$

In particular the unique submodule of $R_0y$ with this
quotient is $(p,\pi)R_0y$, giving the second equality of
(715.2) directly.

For an independent ordinary-unit check, R657 proves
$m=43\Longleftrightarrow N_SE=E_N$. R633 gives

$$
E_N=\mathcal O[T]u_t+\mathcal Oy+R_\Gamma[T]c_t,
\quad N_Tu_t=u,\quad N_Tc_t=c_q,
$$
$$
py=u+aD_\Gamma^{\rm bal}c_q,\qquad
\pi y=a\gamma^{22}c_q,\qquad a=15i/7.
$$

Therefore

$$
N_TE_N=\mathcal Ou+p\mathcal Oy+R_\Gamma c_q
=(p,\pi)E_L.
\tag{715.19}
$$

This proves (715.2) using the original units as well. The
first equality means that at least one actual ordinary unit
has $S$-norm exactly the original $y$. A coordinate
description of such a unit has not been computed here.

The homology cycle generating the remaining line may be
taken as $(-\eta,1)$. Its image in
$H_1(P,A/\pi A)=k^2$ is

$$
(-b/i,1)=(ib,1).
\tag{715.20}
$$

Formula (715.20) records a tangent line of class-module
homology. Identifying it with the two original Robert
cocycles requires an additional chain comparison; the
formula alone is not a proof that $C/9=ib$.

## 6. The natural chain value of each original capitulation cocycle

For completeness, the degree-one version of (715.7) can be
computed without choosing compatible free bases. Because
$N_PA=0$, it is

$$
\Theta:H^1(P,E)\xrightarrow{\;\sim\;}
\widehat H^{-1}(P,A)=A/(s-1,t-1)A=A/\pi A.
\tag{715.21}
$$

For an actual unit cocycle $f$, its value is obtained by
the following chain construction.

1. Regard $f$ as a cocycle in $U$. Since $H^1(P,U)=0$,
   choose $z\in U$ with $(g-1)z=f(g)$ for every $g\in P$.
2. Its image $x\in X$ is $P$-invariant. Since $X$ is
   $P$-free, choose $x_0\in X$ with $N_Px_0=x$.
3. Let $a_0$ be the image of $x_0$ in the ordinary
   quotient $A$. Then $N_Pa_0=0$.
4. Set $\Theta[f]=a_0\bmod(s-1,t-1)A$.

The signs here are those of the two usual connecting maps:
the degree $-1$ Tate differential is $N_P$, and the
degree $0$ cochain differential is $z\mapsto(g-1)z$.
There is no unrecorded Artin inversion.

Independence can also be checked directly. Changing $z$
by a $P$-invariant element of $U$ changes it by $N_Pz_0$.
After changing $x_0$ by the image of $z_0$, the remaining
choice belongs to $\ker N_P$ in $X$, which equals
$(s-1,t-1)X$ by Tate vanishing. Its image is zero in the
coinvariants of $A$. A coboundary change of $f$ is
absorbed by a change of $z$ in $E$, with zero image in
$X$. All these operations commute with $\Gamma$.

Apply this construction to R695's original cocycles, using
its notation for Robert units:

$$
f_s(s)=u_s-y+aD_\Gamma^{\rm bal}c_s,\quad f_s(t)=0,
$$
$$
f_t(s)=0,\quad f_t(t)=u_t-y+aD_\Gamma^{\rm bal}c_t.
\tag{715.22}
$$

Their ordinary divisor classes are $Ce_q$ and $9e_q$.
If $a_s=\Theta[f_s]$ and $a_t=\Theta[f_t]$, then
$a_t\ne0$ and the exact, marking-independent ratio is

$$
\boxed{C=9\,a_s/a_t.}
\tag{715.23}
$$

This formula retains the actual reciprocity map and its
ordinary quotient. The inputs $a_s,a_t$ have not been
numerically evaluated. In particular the second cocycle's
known coefficient $9$ has not been substituted for $C$.

## 7. Restriction boundaries and why zero restrictions do not determine b

Naturality of (715.21) makes restriction to a cyclic
subgroup $H\le P$ the negative-degree Tate restriction

$$
[a]\longmapsto
\left[\sum_{g\in P/H}ga\right]
\in\ker N_H/(h-1)A.
\tag{715.24}
$$

Write $n_T=\min\{43,v_\pi(t-1)\}$, with $n_T=43$
when $t$ acts trivially on $A$. For $H=S$, the
numerator in (715.24) is $N_Ta\in\pi^{42}A$, which
vanishes modulo $(s-1)A=\pi A$. For
$H=\langle ts^r\rangle$, $r\in\mathbf F_p^\times$,
the leading coefficient $b+ri$ is nonzero in $k$;
the denominator ideal is again $\pi A$, while the
coset norm is $N_S$. The restriction is again zero.

For $H=T$, the coset norm is $N_S$, whose image is
the nonzero socle $\pi^{42}A$. It vanishes modulo
$(t-1)A=\pi^{n_T}A$ exactly when $n_T\le42$.
If $n_T=43$, restriction is nonzero. Hence

$$
\boxed{\operatorname{res}^P_H H^1(P,E)=0
\text{ for every actual cyclic }H
\text{ unless }H=T\text{ and }n_T=43.}
\tag{715.25}
$$

This agrees with all ordinary descent and transfer
statements of R684. In the exceptional $m=n_T=43$
case, R684 gives $C=0$ and $\mathcal L=31$.
In the other cases the vanishing restrictions do not
give a value for $C$ or $b$. In particular no
non-Galois line over $k$ is treated as an actual
degree-$p$ subgroup.

## 8. Exact advancement and remaining arithmetic

The former alternatives $m=1$ and $1<m<43$ are now
excluded by the same original ordinary sequence. The
boundary $m=1$ was handled before introducing $b$;
at the actual endpoint $m=43$, $b\in\mathbf F_p$
is defined but still unevaluated.

The original scalar ordinary Norm is now proved onto,
and the full $P$-norm image is exactly (715.2). This
settles the existence issue left in R657. The original
marked first moment $J$, the ordinary coefficient
$C$, and the identity relating them to an actual
numerical $b$ remain separate arithmetic tasks.

Dependencies: [R210](R210-ordinary-class-units-and-ray-residue.md),
[R633](R633-complete-ordinary-unit-lattice-in-the-anti-pq-layer.md),
[R657](R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md),
[R684](R684-ordinary-intermediate-class-groups-and-all-p-direction-transfers.md),
[R695](R695-original-C-second-Gamma-ordinary-division.md), and
[R700](R700-p-ramified-free-lattices-and-the-retained-ordinary-quotient.md).
The resolution calculation, natural integral dimension shift,
cyclicity contradiction, and original-cocycle chain values
have been given explicitly above.
