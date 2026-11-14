# R684: ordinary intermediate class groups and all pure-p transfer directions

**Status: proved, with the exact arithmetic inputs of R561, R613, R619,
R633 and R657.** This result determines the ordinary character class
groups in all 42 mixed pure-p directions and gives the complete transfer
and ordinary unit-Norm alternatives. It does not evaluate the original
scalar $C$, the first moment $J$, the ordinary coefficient $b$, or
$\mathcal L$.

Write $M'=LB$ as in R657, and retain its actual marked class module

$$
A=A_{M'}=R_\Gamma/\pi^m,
\qquad R_\Gamma=\mathcal O[\zeta_{43}],\quad
\pi=\gamma-1,\qquad 1\le m\le43.
\tag{684.1}
$$

For $r\in\mathbf F_{43}$ put

$$
H_r=\langle ts^r\rangle,\quad F_r=B^{H_r},\quad M_r=LF_r.
\tag{684.2}
$$

Thus $M_0=LF_s$ is the original scalar field. The anti-p field is
$N=LF_t=(M')^S$, with $S=\langle s\rangle$; it is recorded as the
additional direction $H_\infty=S$.

For every $r\ne0$ one has

$$
\boxed{A_{M_r}\simeq k=\mathcal O/43.}
\tag{684.3}
$$

The class norm $A_{M_r}\to A_L$ is an isomorphism, and extension of
ideals $A_L\to A_{M_r}$ is zero. More precisely, the norm from the
full layer is an isomorphism

$$
\boxed{
A/(ts^r-1)A\ \xrightarrow{\ \mathrm{Nm}_{M'/M_r}\ }\ A_{M_r}.
}
\tag{684.4}
$$

For these 42 fields, extension $A_{M_r}\to A$ is injective if $m=43$
and zero if $m\le42$. The corresponding ordinary unit-Norm quotient
is respectively $0$ or $k$. The proof of (684.4) includes the complete
ordinary divisor and unit terms; it does not deduce descent from the
abstract top class module alone.

## 1. Fixed fields, character, and inputs

Use the same original $p=43$, 776-bit prime $q$, curve
$A_0:y^2=x^3-x$, CM and Weil markings as R561/R613. In particular,

$$
K=\mathbf Q(i),\quad F=K(A_0[p])^{\mathbf F_p^\times},
\quad \Delta=\langle\sigma\rangle=C_{44},
$$
$$
L=FL_q,\quad \Gamma=\langle\gamma\rangle=C_p,
\quad B=K(A_0[p^2])^{\mu_{42}},
$$
$$
S=\langle s=1+p\rangle,
\qquad T=\langle t=1+21pi\rangle.
\tag{684.5}
$$

The field $M'/F$ has group $\Gamma\times S\times T$, and all these
factors commute with $\Delta$. Put $\mathcal O=\mathbf Z_{43}[i]$ and
$k=\mathbf F_{43}[i]$. For a field $V$ in this diagram, write

$$
E_V=(\mathcal O_V^\times\otimes\mathcal O)_{\chi^-},\qquad
D_V=(\operatorname{Div}_{\rm fin}V\otimes\mathcal O)_{\chi^-},\qquad
A_V=(\operatorname{Cl}(V)\otimes\mathcal O)_{\chi^-}.
\tag{684.6}
$$

Here $\chi^-(\sigma)=\widehat\omega^{-1}$, with
$\omega=8+25i$. The element representatives still use the unaveraged
$P_+=44e_{\chi^-}$ of R561. Let $P_V\subset D_V$ denote all principal
divisors. No prime outside $\{2,p,q\}$ is removed.

The arithmetic inputs used below are the following exact published
statements:

- R619: $A_N=k e_N$, where $e_N=[P_+Q_N]$ is the original marked
  $q$-prime class, and $A_L=k e_q$.
- R657: (684.1), and, if $m\ge2$, the ordinary class actions
  $$s=1+i\pi\pmod{\pi^2},\qquad t=1+b\pi\pmod{\pi^2},
  \quad b\in\mathbf F_{43}.$$
- At $p$, the inertia in $M'/K$ is $\Delta\times S\times T$, while
  $\Gamma$ splits. At the marked $q$ prime, inertia is $\Gamma$,
  decomposition over $F$ is $\Gamma\times S$, and the positive
  unramified Frobenius is $s^{32}$; $T$ splits.

The restriction $b\in\mathbf F_{43}$ has its actual conjugation
meaning. Coefficient conjugation sends $i$ to $-i$ and sends
$\pi$ to $-\pi$ modulo $\pi^2$. Since $\tau t\tau=t^{-1}$,
comparison of the first coefficients gives $\bar b=b$. It is not
a choice of a scalar action after forgetting the field marking.

## 2. A descent calculation for every pure-p direction

Let $H$ be any order-$p$ subgroup of $S\times T$, and put
$V=(M')^H$. All assertions in this section hold for each of the 44
actual directions, including $S$ and $T$.

### 2.1 Ramification and full invariant divisors

The extension $M'/V$ is ramified at $p$: its inertia there is all of
$H$, since $H\subset S\times T$. It is unramified at every other
finite prime. At $p$, $\Delta$ fixes each prime and is inertial,
so the entire nontrivial $\chi^-$ divisor summand is zero. Hence

$$
D_{M'}^H=jD_V.
\tag{684.7}
$$

To check that no unramified term is missing, an invariant divisor on
one orbit of primes over an unramified prime of $V$ has a constant
coefficient on that orbit. Extension of that base prime is exactly
the sum of those primes, with coefficient one. Its residue degree
does not enter this extension-of-divisors assertion. The only
possible ramification-index cokernel is at $p$, whose character
summand was just shown to vanish.

### 2.2 Ordinary units are field norms, without assuming unit norms

At every unramified finite place of $M'/V$, local units are norms.
At a prime over $p$, the full local multiplicative norm cokernel is
the cyclic group $H$, by local reciprocity. The action of $\Delta$
on this cokernel is conjugation on $H$, hence trivial, since
$M'/K$ is abelian. The $p$ primes are individually fixed by $\Delta$,
so their direct sum has zero $\chi^-$ summand. All fields are totally
imaginary. The cyclic Hasse Norm theorem therefore gives

$$
E_V\subset
\mathrm{Nm}_{M'/V}(M'^\times\otimes\mathcal O)_{\chi^-}.
\tag{684.8}
$$

As in R619/R657, this passage to completed character summands is
legitimate: the global norm cokernel injects into the local norm
cokernels; tensor with the flat ring $\mathcal O$ and take the
prime-to-$p$ integral $\Delta$ idempotent. These cokernels are killed
by $p$. Formula (684.8) permits a preimage with a finite divisor and
does not assert that $E_V=\mathrm{Nm}_{M'/V}E_{M'}$.

### 2.3 The exact ordinary cohomology terms

Hilbert 90 and (684.7) identify

$$
\ker(j:A_V\longrightarrow A)=H^1(H,E_{M'}).
\tag{684.9}
$$

Indeed, invariant principal divisors modulo principal divisors
extended from $V$ are $H^1(H,E_{M'})$; by (684.7) those are precisely
the base divisor classes which become principal. Every divisor
outside the named primes is included.

The full divisor module is a sum of permutation lattices and has
$H^1(H,D_{M'})=0$. Applying invariants to the ordinary class sequence
therefore gives

$$
0\longrightarrow jA_V\longrightarrow A^H
\longrightarrow H^1(H,P_{M'})\longrightarrow0.
\tag{684.10}
$$

The multiplicative exact sequence and (684.8) identify the last term
as the ordinary unit norm quotient:

$$
H^1(H,P_{M'})
=\frac{E_V\cap\mathrm{Nm}_{M'/V}(M'^\times\otimes\mathcal O)_{\chi^-}}
       {\mathrm{Nm}_{M'/V}E_{M'}}
=\frac{E_V}{\mathrm{Nm}_{M'/V}E_{M'}}
=\widehat H^0(H,E_{M'}).
\tag{684.11}
$$

The rational Dirichlet representation in the nontrivial $\Delta$
character is regular for $\Gamma\times S\times T$. Its restriction
to $H$ is $p^2$ copies of the regular representation. Consequently
the ordinary unit Herbrand quotient in this summand is one:

$$
\operatorname{length}_{\mathcal O}H^1(H,E_{M'})
=\operatorname{length}_{\mathcal O}\widehat H^0(H,E_{M'}).
\tag{684.12}
$$

One can check this integrally by choosing an $H$-equivariant rational
isomorphism with $\mathcal O[H]^{p^2}$ and passing across two finite
index inclusions of lattices. A finite cyclic module has Tate groups
of equal cardinality, while the regular lattice has vanishing Tate
groups. Thus no factor from the trivial $\Delta$ character enters
(684.12).

Taking lengths in (684.9)--(684.12) proves the exact cancellation

$$
\boxed{\operatorname{length}_{\mathcal O}A_V
       =\operatorname{length}_{\mathcal O}A^H.}
\tag{684.13}
$$

The equality is the result of retaining both the capitulation kernel
and the ordinary unit-Norm cokernel. Neither is assumed zero.

### 2.4 Surjectivity of the class norm and the coinvariant isomorphism

The class norm $A\to A_V$ is onto. Here is the arithmetic reason.
The extension $M'/V$ has prime degree and is ramified at $p$, whereas
the Hilbert class field of $V$ is unramified. Their intersection over
$V$ is therefore trivial. Base changing the Hilbert class field to
$M'$ gives an unramified abelian extension with its original Galois
group. Functoriality of the ideal Artin maps identifies its quotient
map from $\operatorname{Cl}(M')$ with the class norm to
$\operatorname{Cl}(V)$. It is surjective; so is its $\chi^-$ summand.

The class norm kills $(h-1)A$, where $h$ generates $H$. On the cyclic
$R_\Gamma$ module (684.1), put

$$
d_H=\min\{m,v_\pi(h-1)\},
\tag{684.14}
$$

where $h-1$ denotes its scalar endomorphism, and set $d_H=m$ when
that endomorphism is zero. This definition is independent of any
lift to $R_\Gamma$. Then

$$
A/(h-1)A\simeq R_\Gamma/\pi^{d_H},\qquad
\operatorname{length}_{\mathcal O}A^H=d_H.
\tag{684.15}
$$

The surjective class norm from the first module in (684.15) has a
target of exactly the same finite length by (684.13). Its kernel
is therefore zero. This proves, as a $\Gamma$-equivariant assertion,

$$
\boxed{
A/(h-1)A\xrightarrow{\sim} A_V,
\qquad A_V\simeq R_\Gamma/\pi^{d_H}.
}
\tag{684.16}
$$

This establishes (684.4) without losing a ramification term or an
unproved unit-saturation premise.

## 3. The 42 mixed directions and the scalar field

If $m=1$, every $d_H=1$. Suppose $m\ge2$. The actual first
coefficient of $h_r=ts^r$ is

$$
h_r=1+(b+ir)\pi\pmod{\pi^2}.
\tag{684.17}
$$

For $r\ne0$, the coefficient is nonzero because $b,r\in\mathbf F_{43}$
and $i\notin\mathbf F_{43}$. Thus $d_{H_r}=1$. Formula (684.16)
proves (684.3) for all 42 fields. For $S$, the coefficient $i$ is
also nonzero, recovering $A_N=k$ with its existing marking.

For the original scalar field put

$$
n_T=d_T=\min\{m,v_\pi(t-1)\}.
\tag{684.18}
$$

Then the exact remaining ordinary class module is

$$
\boxed{A_{M_0}\simeq R_\Gamma/\pi^{n_T}.}
\tag{684.19}
$$

For $m\ge2$, $b\ne0$ is equivalent to $n_T=1$, and $b=0$ is
equivalent to $n_T\ge2$. The number $n_T$ is defined here by the
actual ordinary $T$ action and has not been evaluated.

## 4. Every transfer operator to the full layer

Let $v\in R_\Gamma$ lift the scalar action of an order-$p$ generator
$h$, and write $v=1+\alpha\pi+O(\pi^2)$. The cyclotomic relation
gives $p\equiv-\pi^{42}\pmod{\pi^{43}}$. With $\delta=v-1$,

$$
1+v+\cdots+v^{42}
=\sum_{j=0}^{42}\binom{43}{j+1}\delta^j
\equiv p+\delta^{42}
\equiv(\alpha^{42}-1)\pi^{42}\pmod{\pi^{43}}.
\tag{684.20}
$$

All terms $1\le j\le41$ have valuation at least $42+j\ge43$.
This also covers $\alpha=0$; it does not divide by $v-1$.

Under the norm identification (684.16), extension of ideals
$j:A_V\to A$ is the map induced by (684.20), since
$j\circ\mathrm{Nm}_{M'/V}=N_H$ on ideal classes.

For $S$, the coefficient in (684.20) is $i^{42}-1=-2$. For $r\ne0$,

$$
(b+ir)^{42}-1
=\frac{b-ir}{b+ir}-1
=\frac{-2ir}{b+ir}\ne0.
\tag{684.21}
$$

Consequently, for $H=S$ and for every $H=H_r$, $r\ne0$,

$$
\begin{array}{c|c|c}
 & j:A_V\to A & E_V/N_HE_{M'}\\ \hline
m=43 & \text{injective, image }\pi^{42}A & 0\\
1\le m\le42 & 0 & k.
\end{array}
\tag{684.22}
$$

The last column follows from (684.9), (684.11), and (684.12).
In the zero-transfer case the source class group has length one,
so the ordinary unit norm quotient also has length one and hence
is $k$. In the injective case both cohomology groups vanish.

For $T$, (684.20) gives zero when $b\ne0$ and $-\pi^{42}$ when
$b=0$, interpreted in $A$. Combining with (684.19), the full
classification is

$$
\begin{array}{c|c|c}
\text{case}&\ker(j:A_{M_0}\to A)&
\operatorname{length}_{\mathcal O}(E_{M_0}/N_TE_{M'})\\ \hline
m\le42 & A_{M_0} & n_T\\
m=43,\ b\ne0 & A_{M_0}=k & 1\\
m=43,\ b=0 & \pi A_{M_0} & n_T-1.
\end{array}
\tag{684.23}
$$

In the last line $n_T\ge2$, and the transfer image is the one
dimensional socle of $A$. We assert the length of the unit norm
quotient in (684.23); we do not identify the two Tate cohomology
modules from equality of their lengths alone.

## 5. Marked q-primes, and the original scalar obstruction

Let $e'=[P_+Q_{M'}]$ be the prime above the original $Q_N$. Since
$M'/N$ is unramified of residue degree $p$ at this prime and has
only one prime there, extension of divisors gives

$$
e'=j_{M'/N}(e_N).
\tag{684.24}
$$

By (684.22) and the nonzero basis $e_N$, $e'=0$ when $m\le42$;
when $m=43$, it is a nonzero generator of $\pi^{42}A$.

For every finite $r$, the subgroup $H_r=\langle ts^r\rangle$ has
trivial intersection with the $q$ decomposition factor $S$.
Thus $q$ splits in $M'/M_r$, and the norm of the chosen prime has
residue degree one. Under (684.16), therefore,

$$
\mathrm{Nm}_{M'/M_r}(e')=[P_+Q_{M_r}].
\tag{684.25}
$$

For $r\ne0$ the quotient has length one, so the image of the socle
element in (684.25) is zero even when $m=43$. This proves that the
marked $q$-prime class is zero in every one of the 42 mixed fields.
The class norm $A_{M_r}\to A_L$ is onto because $M_r/L$ is ramified
at $p$ and of prime degree, by the same Hilbert-class-field argument
as in Section 2.4. Both class groups have length one, so it is an
isomorphism. Extension sends $e_q$ to the vanishing marked prime
class, and is zero. This recovers R613's capitulation conclusion
and also determines the whole target ordinary class group.

For the scalar field, (684.25) has image in
$R_\Gamma/\pi^{n_T}$. It is nonzero exactly when $m=n_T=43$.
Since $M_0/L$ is unramified of residue degree $p$ at $q$,
$j_{M_0/L}(e_q)$ is exactly that prime class. Hence

$$
\boxed{
j_{M_0/L}:A_L\to A_{M_0}\text{ is injective}
\iff m=n_T=43.
}
\tag{684.26}
$$

The original R561 Hilbert--90 divisor class $C e_q$ lies in the
kernel of this last transfer. In particular,

$$
m=n_T=43\ \Longrightarrow\ C=0
\ \Longrightarrow\ \mathcal L=31,
\tag{684.27}
$$

using the original identity $\mathcal L=31-22iC$. Conversely, no
claim that $C=0$ forces this endpoint is made. The particular
Hilbert--90 class can vanish even if a capitulation kernel is
nonzero. Nor does (684.27) establish the still missing proposed
bridge $C=-34ib$.

## 6. Consequence for the next exact computation

The single $m=43$ alternative is now equivalent to ordinary unit
Norm surjectivity in **every** non-scalar pure-p direction, as well
as in the original anti-p direction. One may test any one of these
43 actual directions, with its correct units, to determine that
alternative. Field-Norm solvability cannot perform this test:
(684.8) holds in all cases.

The original scalar arithmetic is still the remaining information:
the actual value of $m$, the scalar action and $n_T$, the original
$C/J/b$, and the residue $\mathcal L$. No existing finite Robert
evaluation was rerun, and no auxiliary value $C_t=9$ or pure-p
residue was substituted for $C$.

The class-field tools used in Section 2 are the cyclic Hasse Norm
theorem and functoriality of the ideal Artin map. Reference:
J. S. Milne, *Class Field Theory*, version 4.03 (2020), Chapter V
(ideal Artin maps and Hilbert class fields), Chapter VIII,
Theorem 3.1 (printed p.234):
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>.
The ordinary divisor/cohomology cancellation, descent isomorphism,
all transfer coefficients, and the marked-prime consequences are
proved above.
