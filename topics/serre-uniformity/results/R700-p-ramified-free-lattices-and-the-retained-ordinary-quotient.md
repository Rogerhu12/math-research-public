# R700: p-ramified free lattices with the ordinary finite quotient retained

Date: 2026-11-14. **Status: proved.** This is an integral comparison theorem for the original
$p=43$, original $q$, and original $\chi^-$ character. It computes the
$p$-ramified character module and proves a free presentation surrounding
the ordinary class group. It does **not** compute the finite ordinary
quotient or the original $C,J,b,m,\mathcal L$.

Put $\mathcal O=\mathbf Z_{43}[i]$, $k=\mathcal O/43$,
$R_0=\mathcal O[\Gamma]$, $R_\Gamma=R_0/(N_\Gamma)$,
$\Gamma=\langle\gamma\rangle=C_{43}$, and $\pi=\gamma-1$.
Use R686's actual fields

$$
B_n=K(A_0[p^{n+1}])^{\mu_{42}},\quad
M_n=LB_n,\quad P_n=S_n\times T_n=\operatorname{Gal}(M_n/L).
$$

Here $B_0=F$, $M_0=L$ and $|P_n|=p^{2n}$. Every symbol
denoting a character module below means the same completed $\chi^-$
summand as R561/R657/R686/R695. The element projector remains
$P_+=44e_{\chi^-}$; no new normalization of a unit or Frobenius is made.

## 1. Statement

For a field $V$ in this tower, write $X_V^{(p)}$ for the character
summand of the Galois group of its maximal abelian pro-$p$ extension
unramified away from $p$. Write $U_V$ for the corresponding summand
of the product of principal local units at all primes above $p$.
The ordinary unit lattice and ordinary class group remain $E_V,A_V$.

First, at the original $q$ layer,

$$
\boxed{
U_L/E_L\simeq R_0,
\qquad X_L^{(p)}\simeq\mathcal O\oplus R_\Gamma.
}
\tag{700.1}
$$

The second isomorphism is an $R_0$-module isomorphism. More precisely,
after choosing a basis of the first module, the **pair** consisting
of $X_L^{(p)}$ and its sublattice $U_L/E_L$ is

$$
\boxed{
\left(\mathcal O\oplus R_\Gamma,
\{(a,b):a\bmod p=b\bmod\pi\}\right).
}
\tag{700.2}
$$

Thus the ordinary quotient is still $A_L=k$. In particular,
$X_L^{(p)}$ is torsion-free over $\mathcal O$, but it is **not**
being identified with the ordinary class group or with $R_0$.

At every higher full pure-$p$ level,

$$
\boxed{
X_{M_n}^{(p)}\simeq\mathcal O[P_n]^{43},
\qquad U_{M_n}\simeq\mathcal O[P_n]^{86}.
}
\tag{700.3}
$$

The character localization of the entire ordinary unit lattice
is injective, and actual local reciprocity gives an exact sequence

$$
\boxed{
0\longrightarrow E_{M_n}
\longrightarrow U_{M_n}
\xrightarrow{\operatorname{Art}_p}X_{M_n}^{(p)}
\longrightarrow A_{M_n}\longrightarrow0.
}
\tag{700.4}
$$

Consequently the two middle terms in (700.4) are free
$\mathcal O[P_n]$-modules of ranks $86$ and $43$, while its
finite cokernel is the actual, still unevaluated ordinary module

$$A_{M_n}=R_\Gamma/\pi^{m_n},\qquad
m_n=\min(d,42n+1)$$

from R686. The determinant minors or integral entries of the actual
reciprocity map in (700.4) have not been computed by this theorem.

## 2. The two actual primitive inputs

R327 proves the full $p$-adic saturation of the ordinary units of
$F$ in the principal local units at its unique $p$ prime. In the
present character this says

$$
U_F\simeq\mathcal O^2,
\qquad E_F=\mathcal O u\subset U_F
\quad\hbox{is a direct summand}.
\tag{700.5}
$$

Here $u$ is R163/R210's same primitive Robert unit. The equality
of a finite-index Robert subgroup with this entire character unit
lattice was already proved there; no new unit-index assumption
is made in (700.5). Since $A_F=0$, ordinary ray class reciprocity
also gives

$$X_F^{(p)}=U_F/E_F\simeq\mathcal O.$$

The second input is the **original marked** $q$ Frobenius in this
line. R377 computes the quotient of the full $p$-ramified
abelianization by all $44$ actual $q$ Frobenii. Its free character
types are $0,22$, and its only finite nonzero types are $16,28$.
The present character has type $-1=43$ relative to the same
$\omega=8+25i$; its contragredient has type $1$. Neither occurs
in that quotient. Since each such original $p$-ramified block
has rank one, R377 proves that

$$
h_F:=P_+\operatorname{Frob}_{\mathfrak q_0}
\in X_F^{(p)}
\quad\hbox{is primitive over }\mathcal O.
\tag{700.6}
$$

Multiplying by $P_+$ instead of the averaged idempotent multiplies
by the unit $44$ and preserves this assertion. The argument uses
the original $\alpha=1+89460y_F$ and the original prime label in
R377. It does not replace $h_F$ by a freely chosen ray coefficient.

## 3. The entire base local-unit quotient

The $q$ extension $L/F$ is completely split at $p$. Therefore

$$U_L\simeq R_0\otimes_{\mathcal O}U_F\simeq R_0^2.$$

R210 proves $E_L=R_0y$ and $N_\Gamma y=u$. Write the localization
of $y$ in a basis of $R_0^2$ as a column $(a,b)$. Applying
$N_\Gamma$ says that the augmentation column $(a(1),b(1))$
is exactly the primitive local vector $u$ of (700.5).

The ring $R_0$ is local, with maximal ideal $(p,\gamma-1)$.
At least one of $a,b$ is consequently a unit of $R_0$.
The column is unimodular and is part of an $R_0$ basis.
Thus localization is injective on $E_L$, with the full integral
quotient

$$V_L:=U_L/E_L\simeq R_0.$$

Taking the inverse limit of the ordinary ray class sequences at
$p$ gives the actual sequence

$$0\longrightarrow V_L\longrightarrow X_L^{(p)}
\longrightarrow A_L=k\longrightarrow0.
\tag{700.7}
$$

The last term has not been inverted or removed. No global or
local $p$-power roots of unity intervene: the local ramification
indices in the pure-$p$ tower are $44p^{2n}$, not divisible by
$p-1=42$, and the global fields likewise do not contain $\mu_p$.

## 4. q Frobenius excludes the possible torsion summand

Let $\mathcal T$ be the $\mathcal O$-torsion of $X_L^{(p)}$.
It intersects $V_L$ trivially, and (700.7) embeds it into $k$.
Hence $\mathcal T$ is either zero or $k$.

Let $\mathfrak Q_0$ be the original prime of $L$ over
$\mathfrak q_0$, and let

$$h_L=P_+\operatorname{Frob}_{\mathfrak Q_0}\in X_L^{(p)}.$$

This is defined since the extension represented by $X_L^{(p)}$
is unramified at $q$. The prime $\mathfrak Q_0$ is fixed by
$\Gamma$, so $h_L$ is fixed as well. The field-norm map

$$\nu:X_L^{(p)}\longrightarrow X_F^{(p)}$$

is $\Gamma$-invariant and sends $h_L$ to $h_F$: the residue
degree of $\mathfrak Q_0/\mathfrak q_0$ is one. This is the
usual ideal norm, not multiplication by its ramification index.

Suppose $\mathcal T=k$. Its map to the last term of (700.7)
is an isomorphism, and therefore

$$X_L^{(p)}=V_L\oplus\mathcal T\simeq R_0\oplus k.$$

Since $X_F^{(p)}$ is torsion-free, $\nu$ kills $\mathcal T$.
The invariant submodule of $R_0$ is $\mathcal O N_\Gamma$.
For any $v\in V_L$,
$\nu(N_\Gamma v)=p\nu(v)$, so

$$\nu\bigl((X_L^{(p)})^\Gamma\bigr)
\subset pX_F^{(p)}.$$

This contradicts (700.6) applied to $h_L$. Thus

$$\mathcal T=0.$$
\tag{700.8}

This argument uses the primitive actual Frobenius to distinguish
the two extensions of the same finite ordinary quotient. Knowing
only $U_L/E_L$ and $A_L$ would not have justified (700.8).

## 5. Exact classification of the index-k overlattice

Identify $V_L$ with $R_0$. Because $X_L^{(p)}$ is torsion-free
and $X_L^{(p)}/V_L=k$, view it as an overlattice in
$R_0\otimes\mathbf Q_p$. For $x$ lifting a nonzero element
of this quotient, $px=r\in R_0$ and $\pi x\in R_0$.
It follows that $\pi r\in pR_0$.

In
$R_0/pR_0=k[\pi]/(\pi^p)$, the kernel of multiplication by
$\pi$ is the line $k\pi^{p-1}=kN_\Gamma$. Therefore

$$r=cN_\Gamma+pr',\qquad c\in\mathcal O,\quad r'\in R_0.$$

Here $c$ is a unit, since otherwise $x$ would already belong
to $R_0$. Hence the entire overlattice is

$$X_L^{(p)}=R_0+\mathcal O\frac{N_\Gamma}{p}.$$

Under evaluation at $\gamma=1$ and $\gamma=\zeta_p$, the ring
$R_0$ embeds in $\mathcal O\oplus R_\Gamma$ as
$\{(a,b):a\bmod p=b\bmod\pi\}$, and $N_\Gamma/p$ maps
to $(1,0)$. Adjoining it gives the whole direct sum. This proves
(700.1)--(700.2), including the index and its finite ordinary
quotient.

## 6. The needed cohomology block vanishes

Let $G=G_p(L)$ be the Galois group of the maximal, possibly
nonabelian, pro-$p$ extension of $L$ unramified outside $p$.
Let $\chi^\vee$ denote the contragredient block to our class
module character, so

$$H^1(G,k)_{\chi^\vee}
 =\operatorname{Hom}_k(X_L^{(p)}/p,k)$$

has dimension $p=43$ by (700.8).

Let $\mathscr G$ first denote the full restricted-ramification
Galois group, allowing the primes above $p$ and, for the tame
character coefficient, those above $2$. Its maximal pro-$p$
quotient is still $G$. Indeed $\Gamma$ is split at $2$, the
residue degrees in $F/K$ divide $44$, and $2$ has order $14$
modulo $43$. No such completion has $\mu_{43}$, and passing
to a pro-$43$ unramified extension cannot change this: the
residue degree is multiplied by a power of $43$. A nontrivial
tame pro-$43$ inertia quotient would force Frobenius to act
trivially on its order-$43$ quotient, contrary to that residue
order. Thus allowing $2$ adds no pro-$43$ ramification.

The global Euler--Poincare formula for $\mathscr G$ gives,
in the indicated character,

$$
\dim_k H^1(\mathscr G,k)_{\chi^\vee}
-\dim_k H^2(\mathscr G,k)_{\chi^\vee}=p.
\tag{700.9}
$$

For completeness, the constant is the multiplicity $p$ of
$\chi^\vee$ in the permutation representation on the complex
places of $L$. There is no $H^0$ in a nontrivial character.
One can apply the usual formula to the one-dimensional character
coefficient over $L^\Delta$, whose number of complex places is
$p$, and use the prime-to-$p$ Hochschild--Serre isomorphism.

The first cohomology of $\mathscr G$ is the same as that of
its maximal pro-$p$ quotient, and inflation in
degree two for trivial $p$ coefficients is injective. The latter
fact follows from the five-term sequence: a nonzero invariant
$\mathbf F_p$ quotient of the kernel would give a further
pro-$p$ quotient, contrary to maximality. The full second
cohomology in the indicated block is already zero by the Euler
formula and the computed first dimension. We obtain

$$\boxed{H^2(G,k)_{\chi^\vee}=0.}
\tag{700.10}
$$

Only this one block (and its conjugate) is asserted to vanish.
The argument does not assert that the entire field $L$ is
$p$-rational or that the entire group $G$ is free.

## 7. An integral freeness lemma for the higher layers

We give the group-cohomological argument, so that (700.3) does
not depend on an informal assertion about generators and relations.
Let $H=G_p(M_n)$ and $P=P_n$. Since $M_n/L$ is a $p$ extension
unramified outside $p$, $H$ is the open normal subgroup of $G$
with quotient $P$. The tame group $\Delta$ acts trivially on
$P$, as the actual field $M_n/F$ is abelian over $K$.

Let $M$ be any finite $k[P]$ module, inflated to $G$, with
trivial external $\Delta$ action on its coefficient space.
Because $P$ is a $p$ group, $M$ has a composition series whose
quotients are trivial one-dimensional $k$ modules. The long
cohomology sequences and (700.10) show

$$H^2(G,M)_{\chi^\vee}=0.$$

Also $H^0(G,M)$ has trivial $\Delta$ type, so it has no
$\chi^\vee$ component. The functor

$$M\longmapsto H^1(G,M)_{\chi^\vee}$$

is consequently exact on finite $k[P]$ modules.

The five-term Hochschild--Serre sequence for $H\triangleleft G$
has its $H^1(P,M)$ and $H^2(P,M)$ terms in the trivial
$\Delta$ type. Since $H$ acts trivially on $M$, it gives

$$
H^1(G,M)_{\chi^\vee}
\simeq
\operatorname{Hom}_{k[P]}(X_{M_n}^{(p)}/p,M).
\tag{700.11}
$$

Thus the Hom functor represented by $X_{M_n}^{(p)}/p$ is
exact. This finite $k[P]$ module is projective, and hence free
because $k[P]$ is local. Taking $M=k$ in (700.11) shows its
free rank is the original first-cohomology dimension $p$:

$$X_{M_n}^{(p)}/p\simeq k[P]^p.$$

No Leopoldt statement at level $n$ has been assumed in this
step. The ordinary ray class sequence always gives

$$\operatorname{rank}_{\mathcal O}X_{M_n}^{(p)}
\ge 2p|P|-p|P|=p|P|,$$

since the local unit rank is $2p|P|$ and the ordinary global
unit rank in this character is $p|P|$. The computed dimension
modulo $p$ is exactly $p|P|$. It follows simultaneously that
the global character localization has zero kernel, that
$X_{M_n}^{(p)}$ is $\mathcal O$-torsion-free, and that its
$\mathcal O$ rank is $p|P|$.

Lift the $p$ free $k[P]$ basis vectors to $X_{M_n}^{(p)}$.
Nakayama gives a surjection $\mathcal O[P]^p\to X_{M_n}^{(p)}$.
Its source and target have the same $\mathcal O$ rank; the
kernel is a torsion-free module of rank zero, and is therefore
zero. This proves the global assertion of (700.3) integrally.

## 8. The entire local lattice and the ordinary comparison sequence

At $p$, $B_n/F$ is totally ramified with group $P_n$, and
$\Delta$ is inertial. The local norm cokernel is the abelian
group $P_n$ under reciprocity. The tame group centralizes it,
so its nontrivial character summand is zero. The norm on
the present character principal-unit lattice is therefore onto
$U_F=\mathcal O^2$.

Choose two norm preimages of a basis of $U_F$. This gives a map
$\mathcal O[P_n]^2\to U_{B_n}$. Modulo $p$, the group ring
$k[P_n]$ has its one-dimensional socle generated by the full
group norm. The two socle vectors map to the two primitive
base local units. They remain independent modulo $p$ in the
upper lattice, because the invariant lattice $U_F$ is
$p$-saturated in the torsion-free upper unit lattice.

Every nonzero submodule of the finite free $k[P_n]$ module
meets its socle. Hence this map is injective modulo $p$;
the equal dimensions make it an isomorphism. Nakayama and
equal ranks now give

$$U_{B_n}\simeq\mathcal O[P_n]^2.$$

Since $L/F$ is split at $p$, there are $p$ such completions
in $M_n$, so

$$U_{M_n}\simeq\mathcal O[P_n]^{2p}.$$

The inverse limit of the full ordinary ray class sequences at
$p$ has kernel the closure of the global ordinary units and
cokernel the full ordinary class group. The character
localization was proved injective in Section 7. The finitely
generated completed ordinary unit lattice is compact, so its
image is closed. This proves exactly (700.4).

The $p$-prime divisor modules have zero character part; thus
replacing ordinary units by $p$ units at this particular
intermediate comparison would not change its character module.
Nevertheless (700.4) has been stated and derived with ordinary
units and the ordinary class group throughout, and no $q$
prime or other outside-support term is removed.

## 9. What this does and does not identify

The new free presentation concerns the actual semilocal-to-global
reciprocity map. It provides an integral setting for testing R695's
original $\Gamma^2$ divisibility criterion and for attempting a
comparison with the class action. Its finite cokernel is essential:
the two free ranks in (700.3) do not imply that this map is onto.

In particular the proven $p$-ramified torsion vanishing does not
say $A_{M_n}=0$, and it does not settle $m=43$ or the ordinary
unit-Norm condition of R657. The class parameter $b$ remains
undefined when $m=1$; no first-order coefficient is manufactured
from the free $p$-ramified module in that case.

## Sources

- R327 supplies actual local $p$ saturation; R377 supplies the
  primitive actual $q$ Frobenius in the indicated character.
- R210 supplies $E_L=\mathcal O[\Gamma]y$, $N_\Gamma y=u$,
  and $A_L=k$. R657/R686 retain the actual ordinary higher
  class modules and their unknown lengths.
- Global Euler--Poincare and the prime-to-$p$ cohomology
  comparison are classical. A primary source for the exact
  Euler formula used in Section 6 is J. S. Milne,
  *Arithmetic Duality Theorems*, second edition (2006),
  Chapter I, Theorem 5.1, printed p.67:
  <https://www.jmilne.org/math/Books/ADTnot.pdf>.
- The ordinary ray class exact sequence and norm/Frobenius
  compatibility are used in their usual full-ideal form; see
  J. S. Milne, *Class Field Theory*, version 4.03 (2020),
  Chapter V, Theorem 1.7 (the full ray class exact sequence) and Sections 3–5 (reciprocity): <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

The torsion exclusion, complete index-$k$ lattice classification,
exact-Hom freeness argument, local socle proof, and retained finite
ordinary comparison have all been proved above.
