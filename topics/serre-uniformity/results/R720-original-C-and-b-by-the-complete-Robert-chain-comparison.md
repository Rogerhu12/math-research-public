# R720: the original Robert cocycles give C = 9ib by an integral chain comparison

Date: 2026-11-14. **Status: proved.** This note restores the original
bridge, after R715 has proved the previously missing ordinary endpoint.
All fields, units, tame and wild generators, the positive Artin
convention, and the unaveraged projector are those of
R561/R613/R619/R633/R657/R695/R700/R715.

For the actual first-order ordinary class action

$$
s=1+i\pi+O(\pi^2),\qquad
t=1+b\pi+O(\pi^2),\qquad b\in\mathbf F_{43},
$$

the original scalar cocycle has coefficient

$$
\boxed{C=9ib=-34ib.}
\tag{720.1}
$$

The numerical value of $b$ is still not evaluated. The original
secondary quantities now have the equivalent exact expressions

$$
\boxed{\mathcal L=31+26b=31-17b,\qquad
r_y=25+9b,\qquad
\Omega_2=\varepsilon(22+17b).}
\tag{720.2}
$$

No auxiliary $C_t$ is substituted for $C$. Its proved value $9$
normalizes the ratio of two actual cocycles only after the full
chain comparison below.

## 1. Original data and the precise missing comparison

Write

$$
p=43,\quad \mathcal O=\mathbf Z_p[i],\quad
k=\mathcal O/p,\quad R_0=\mathcal O[\Gamma],\quad
R_\Gamma=R_0/(N_\Gamma),\quad\pi=\gamma-1,
$$
$$
P=S\times T=\langle s,t\rangle,\quad M'=LB,\quad
E=E_{M'},\quad U=U_{M'},\quad X=X_{M'}^{(p)},\quad A=A_{M'}.
$$

R715 proves

$$
A=R_\Gamma/\pi^{43},\qquad
E^P=E_L=R_0y,\qquad
N_PE=(p,\pi)E_L.
\tag{720.3}
$$

R700 gives the actual full exact sequence

$$
0\longrightarrow E\longrightarrow U
\xrightarrow{\mathrm{Art}_p}X\longrightarrow A\longrightarrow0,
\tag{720.4}
$$

with both middle terms free over $\mathcal O[P]$. We retain
the ordinary quotient $A$ throughout. The two natural
dimension-shift isomorphisms are

$$
\Psi:\widehat H^0(P,E)\xrightarrow{\sim}H_1(P,A),
\qquad
\Theta:H^1(P,E)\xrightarrow{\sim}A/\pi A.
\tag{720.5}
$$

In the standard product-group resolution,

$$
d_1(x,z)=(s-1)x+(t-1)z,
$$
$$
d_2(c,d,e)=
\bigl(N_Sc-(t-1)d,\ (s-1)d+N_Te\bigr).
\tag{720.6}
$$

R715 proves that the map to reduced coefficients

$$
H_1(P,A)\longrightarrow H_1(P,A/\pi A)=k^2
$$

is injective, with image the line

$$
k(ib,1).
\tag{720.7}
$$

That homology line alone did not identify the original
cocycles. The purpose of this note is to prove, using
the original units, that their $\Theta$ coordinates are
the negatives of the two coordinates of $\Psi[y]$.

## 2. The original units supply a single compatible pair of norm equations

Use the actual ancestor and descendants

$$
c_s=N_Tc_B,\qquad c_t=N_Sc_B,\qquad
c_q=N_Pc_B,
$$
$$
N_Tu_B=u_s,\qquad N_Su_B=u_t,\qquad
N_Pu_B=u,\qquad N_\Gamma y=u.
$$

The original balanced derivative and coefficient are

$$
D=D_\Gamma^{\mathrm{bal}}
=\sum_{j=-21}^{21}j\gamma^j,\qquad a=15i/7,
$$

with the exact original relations

$$
py=u+aDc_q,\qquad \pi y=a\gamma^{22}c_q.
\tag{720.8}
$$

Define actual ordinary units, written additively in their
completed lattices, and an integral group-ring operator by

$$
z=a\gamma^{22}c_B,\qquad
\delta=\gamma^{-22}D,\qquad
w=u_B+\delta z=u_B+aDc_B.
\tag{720.9}
$$

The balanced derivative identity gives

$$
\boxed{\delta\pi=p-N_\Gamma,\qquad
\delta\in\pi R_0.}
\tag{720.10}
$$

The second assertion uses the zero augmentation of $D$;
there is no division by $p$ or $\pi$. Equations (720.8)
give the two exact norms

$$
N_Pz=\pi y,\qquad N_Pw=py.
\tag{720.11}
$$

R695's two original cocycles therefore have the single
common description

$$
f_s(s)=N_Tw-y,\qquad f_s(t)=0,
$$
$$
f_t(s)=0,\qquad f_t(t)=N_Sw-y.
\tag{720.12}
$$

They are precisely the original
$u_s-y+aDc_s$ and $u_t-y+aDc_t$, not replaced
by cohomologically convenient Robert families.
Their ordinary divisor classes, with the same sign
convention, are

$$
[f_s]=Ce_q,\qquad [f_t]=9e_q.
\tag{720.13}
$$

## 3. A simultaneous local norm preimage exists integrally

Because the original $\Gamma$ extension splits at every
$p$ prime, and all the $P$ and $\Gamma$ actions commute,
the actual local unit module is induced:

$$
U\simeq\mathcal O[\Gamma]\otimes_{\mathcal O}U_B.
$$

R700 proves $U_B\simeq\mathcal O[P]^2$, so

$$
U\simeq\mathcal O[P\times\Gamma]^2.
\tag{720.14}
$$

This freeness is asserted for the semilocal unit module;
it is not a freeness assertion about the global ordinary
units $E$.

We claim there is a local unit $Y\in U$ satisfying both

$$
\boxed{N_PY=y,\qquad N_\Gamma Y=u_B.}
\tag{720.15}
$$

Here $y\in U^P$ and $u_B\in U^\Gamma$, and their
necessary compatibility is the actual equality
$N_\Gamma y=N_Pu_B=u$.

To prove sufficiency integrally, work in one free
$\mathcal O[P\times\Gamma]$ summand. An invariant pair
can be written uniquely as

$$
y=N_P f(\gamma),\qquad
u_B=N_\Gamma g(s,t).
$$

The compatibility says exactly
$\operatorname{aug}_\Gamma f
=\operatorname{aug}_P g=c\in\mathcal O$.
The element

$$
Y=f(\gamma)+g(s,t)-c
$$

has the two prescribed norms. This proves (720.15)
componentwise in (720.14), with no averaging denominator.
Equivalently, the two augmentation maps have image the
integral fiber product over their common augmentation.
This also shows why specifying only one of the two
norms would not suffice for the later chain calculation.

## 4. The module NΓX is genuinely P-free

Put $X_B=X_B^{(p)}$. We first verify

$$
\boxed{X_B\simeq\mathcal O[P],\qquad
N_\Gamma X\simeq X_B
\quad\text{as }\mathcal O[P]\text{-modules}.}
\tag{720.16}
$$

R657 proves the full ordinary statements
$A_B=0$ and $E_B=\mathcal O[P]u_B$. R700 proves
$U_B=\mathcal O[P]^2$. The original norm
$N_Pu_B=u$ is primitive in $U_F=\mathcal O^2$
by R327. In a free $\mathcal O[P]$ basis of
$U_B$, the coordinate column of $u_B$ therefore
has a primitive augmentation column. Since
$\mathcal O[P]$ is local, one coordinate is a unit.
Thus $\mathcal O[P]u_B$ is a direct summand and

$$
X_B=U_B/E_B\simeq\mathcal O[P].
\tag{720.17}
$$

The equality with $X_B$ follows from the actual ray
class sequence and the proved $A_B=0$; no finite
ordinary quotient is discarded without proof.

Let

$$
\nu:X\longrightarrow X_B,\qquad
j:X_B\longrightarrow X
$$

be the norm and extension maps induced on the
$p$-ramified abelianizations by the ordinary idele
norm and extension of ideles. They commute with $P$
and satisfy

$$
\nu j=p,\qquad j\nu=N_\Gamma.
\tag{720.18}
$$

These are the usual actual norm/extension identities,
with no Artin inversion. For example, the product of
the $\Gamma$ translates of an upper idele is the
extension of its norm; for a lower idele its norm
after extension is its $p$th power.

The local norm $U\to U_B$ is onto because the
$p$ primes split completely in the $\Gamma$ extension:
on the induced module it is the ordinary augmentation
of the $\mathcal O[\Gamma]$ factor. Since
$U_B\to X_B$ is onto by (720.17), compatibility with
reciprocity proves that $\nu:X\to X_B$ is onto.
Since $X_B$ is torsion-free over $\mathcal O$,
$\nu j=p$ makes $j$ injective. Hence

$$
N_\Gamma X=j\nu(X)=jX_B
$$

is the claimed free $\mathcal O[P]$ module.
In addition,

$$
N_\Gamma X\subset
\ker(X\longrightarrow A),
\tag{720.19}
$$

since $N_\Gamma A=0$. This is also visible from
(720.17): extension of a lower local-unit class is
represented by an upper local-unit class.

The proof of (720.16), rather than the abstract
shape of $A$, is the additional arithmetic input
that will remove the possible extra chain terms.

## 5. Choose the homology chain of the original y

Choose $Y$ as in (720.15), and put

$$
x=\mathrm{Art}_p(Y)\in X.
$$

Then

$$
N_Px=0,\qquad N_\Gamma x=0,
\tag{720.20}
$$

because both prescribed norms of $Y$ are ordinary
global units. Since $X$ is $P$-free,
$\ker N_P=(s-1,t-1)X$. Choose $\xi_s,\xi_t\in X$ with

$$
x=(s-1)\xi_s+(t-1)\xi_t.
\tag{720.21}
$$

Writing a bar for the image in $A$, the pair
$(\bar\xi_s,\bar\xi_t)$ is a degree-one cycle.
The two connecting maps in (720.4) identify its
homology class with $\Psi[y]$: its first boundary
is $x$, its lift is $Y$, and its next Tate
differential is $N_PY=y$.

The class of $y$ generates
$E_L/N_PE=k$ by (720.3). Hence this cycle is a
generator of $H_1(P,A)$. Under (720.7) it follows that

$$
\bar\xi_t\bmod\pi\ne0,\qquad
\bar\xi_s\bmod\pi
=ib\,(\bar\xi_t\bmod\pi).
\tag{720.22}
$$

No representative of a class in $A$ or local-unit
basis has been declared to be the original marked
prime class. Only the ratio in (720.22) will be used.

## 6. The first exact cycle and its Gamma correction

By (720.11) and (720.15),
$z-\pi Y\in\ker N_P$ in the $P$-free module $U$.
Choose $R_s,R_t\in U$ with

$$
z-\pi Y=(s-1)R_s+(t-1)R_t.
\tag{720.23}
$$

Put $r_s=\mathrm{Art}_p(R_s)$ and
$r_t=\mathrm{Art}_p(R_t)$. Since $z\in E$,
applying reciprocity gives

$$
\pi x+(s-1)r_s+(t-1)r_t=0.
$$

Together with (720.21), this says
$(\pi\xi_s+r_s,\pi\xi_t+r_t)$ is a cycle in $X^2$.
The homology of the $P$-free module $X$ vanishes,
so there are $c,d,e\in X$ such that

$$
\pi\xi_s+r_s=N_Sc-(t-1)d,
$$
$$
\pi\xi_t+r_t=(s-1)d+N_Te.
\tag{720.24}
$$

There is also the cycle
$(N_\Gamma\xi_s,N_\Gamma\xi_t)$, because
$N_\Gamma x=0$. It is a cycle in the submodule
$N_\Gamma X$. By the proved freeness (720.16),
its homology vanishes within that submodule.
Thus we can choose $c_0,d_0,e_0\in N_\Gamma X$
with

$$
N_\Gamma\xi_s=N_Sc_0-(t-1)d_0,
$$
$$
N_\Gamma\xi_t=(s-1)d_0+N_Te_0.
\tag{720.25}
$$

In particular

$$
\bar c_0=\bar d_0=\bar e_0=0
\quad\text{in }A.
\tag{720.26}
$$

Multiply (720.24) by $\delta$ and add (720.25).
Using $\delta\pi=p-N_\Gamma$, set

$$
c'=\delta c+c_0,\qquad
d'=\delta d+d_0,\qquad
e'=\delta e+e_0.
$$

We obtain the exact identities in $X$,

$$
p\xi_s+\delta r_s=N_Sc'-(t-1)d',
$$
$$
p\xi_t+\delta r_t=(s-1)d'+N_Te'.
\tag{720.27}
$$

Since $\delta\in\pi R_0$, (720.26) gives the
crucial vanishing

$$
\boxed{\bar c'\equiv\bar e'\equiv0\pmod{\pi A}.}
\tag{720.28}
$$

Without resolving (720.25) in the actual free
submodule $N_\Gamma X$, these two terms could
not have been discarded. This is the chain-level
point omitted by a comparison of tangent lines alone.

## 7. Exact primitives of the two original cocycles

Let
$D_S=\sum_{j=0}^{42}js^j$ and
$D_T=\sum_{j=0}^{42}jt^j$, so

$$
(s-1)D_S=p-N_S,\qquad
(t-1)D_T=p-N_T.
$$

Equation (720.23) and the common norm choice give

$$
w-pY
=\delta\bigl((s-1)R_s+(t-1)R_t\bigr).
\tag{720.29}
$$

Define the two local units

$$
Z_s=N_T(D_SY+\delta R_s),\qquad
Z_t=N_S(D_TY+\delta R_t).
\tag{720.30}
$$

They satisfy all four cocycle equations:

$$
(s-1)Z_s=N_Tw-y,\qquad (t-1)Z_s=0,
$$
$$
(s-1)Z_t=0,\qquad (t-1)Z_t=N_Sw-y.
\tag{720.31}
$$

For example the first equality is
$N_T((p-N_S)Y+\delta(s-1)R_s)
=N_Tw-N_PY$, because
$N_T(t-1)R_t=0$. The other three follow by the
same displayed identities or the invariance of
the relevant norm. Thus (720.30) are local
primitives of the original entire $P$ cocycles.

Apply reciprocity to $Z_s$. From (720.21) and
(720.27),

$$
\begin{aligned}
\mathrm{Art}_p(Z_s)
&=N_T(D_Sx+\delta r_s)\\
&=N_T\bigl(
N_S(c'-\xi_s)+(t-1)(D_S\xi_t-d')\bigr)\\
&=N_P(c'-\xi_s).
\end{aligned}
\tag{720.32}
$$

Similarly,

$$
\mathrm{Art}_p(Z_t)=N_P(e'-\xi_t).
\tag{720.33}
$$

R715's explicit definition of $\Theta$ takes a
local primitive, applies reciprocity, takes an
$N_P$ preimage in $X$, and then its ordinary
class modulo $(s-1,t-1)A=\pi A$. Therefore
(720.28), (720.32), and (720.33) prove

$$
\boxed{
\Theta[f_s]=-\bar\xi_s\pmod{\pi A},\qquad
\Theta[f_t]=-\bar\xi_t\pmod{\pi A}.
}
\tag{720.34}
$$

The two signs are both negative. They come
from the displayed boundaries, not from a
choice of the Artin convention. The same
common sign cancels in the ratio.

## 8. The original coefficient and the remaining numerical input

By (720.13), the isomorphism $\Theta$ gives

$$
\frac C9=\frac{\Theta[f_s]}{\Theta[f_t]}.
$$

The denominator is nonzero, both because its
ordinary coefficient is $9$ and by (720.22).
Substituting (720.34) and then (720.22) yields

$$
\frac C9
=\frac{\bar\xi_s\bmod\pi}{\bar\xi_t\bmod\pi}
=ib.
$$

This proves (720.1) for the original marked
cocycles. R561/R613 give
$\mathcal L=31-22iC$ and $r_y=2\mathcal L+6$;
the original convention is
$\Omega_2=\varepsilon(10-\mathcal L)$.
Reducing the coefficients modulo $43$ gives
exactly (720.2).

The former $m=1$ boundary does not acquire a
spurious $b$: it was separately excluded in
R715 before this proof. At the actual endpoint
$m=43$, $b=0$ is allowed and (720.1) then gives
$C=0$ and $\mathcal L=31$, regardless of the
higher valuation of $t-1$. The old requirement
$m=n_T=43$ is sufficient for that conclusion,
but is no longer necessary once the full
chain bridge has been proved.

No numerical value of $b$ has been inserted.
The pure-$p$ secondary reference $24$ of R204,
the auxiliary anti-$p$ coefficient $C_t=9$,
and the original scalar $C$ retain their
distinct meanings. Determining the actual
first class-action coefficient $b$, or the
equivalent original ordinary class $C$,
remains the next arithmetic task.

Dependencies:
[R327](R327-complete-local-unit-saturation-and-free-43-ramification.md),
[R561](R561-restored-scalar-norm-cocycle-and-ordinary-artin-class.md),
[R613](R613-mixed-p-capitulation-and-the-exact-34-boundary.md),
[R619](R619-ordinary-anti-p-class-group-and-actual-artin-nine.md),
[R633](R633-complete-ordinary-unit-lattice-in-the-anti-pq-layer.md),
[R657](R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md),
[R695](R695-original-C-second-Gamma-ordinary-division.md),
[R700](R700-p-ramified-free-lattices-and-the-retained-ordinary-quotient.md),
and
[R715](R715-natural-Tate-dimension-shift-and-the-forced-ordinary-endpoint.md).

The simultaneous integral norm lift, the actual
norm/extension proof of $N_\Gamma X$ freeness,
and the complete sign-sensitive comparison
of both original cocycles are proved above.

