# R657: the full ordinary class module and the exact scalar unit-Norm criterion

**Status: proved.** Retain the original p=43, q, positive Artin and Weil
marking of R561/R619. Put \(M'=LB\), where
\(\operatorname{Gal}(B/F)=S\times T\), and put \(N=LF_t=(M')^S\).
The ordinary character class group has the form

\[
 A_{M'}\simeq R_\Gamma/\pi^m,\qquad 1\le m\le43,
 \quad R_\Gamma=\mathcal O[\zeta_{43}],\quad \pi=\gamma-1.
 \tag{657.1}
\]

If \(m\ge2\), its actual marked scalar action is

\[
 s=1+i\pi\pmod{\pi^2},                            \tag{657.2}
\]

as an endomorphism of this cyclic module. This uses the ordinary Hilbert
class field and the actual genus Artin character. It is not a coefficient
transported from a ray module.

The endpoint has the following exact arithmetic characterization:

\[
 \boxed{
 m=43
 \iff j_{M'/N}:A_N\longrightarrow A_{M'}\text{ is injective}
 \iff N_S E_{M'}=E_N
 \iff y\in N_S E_{M'}.
 }                                                   \tag{657.3}
\]

Here \(E\) denotes **ordinary** completed character units, and y is the
actual original norm unit of R561, not an arbitrarily chosen norm
primitive. If \(m\le42\), the entire class line \(A_N\) capitulates,
the ordinary unit norm has index \(|k|\), and y is not an ordinary unit
norm. Every ordinary character unit of N is nevertheless a norm of a
completed multiplicative element of M'. Thus the last condition in
(657.3) cannot be replaced by the Hasse field-Norm condition.

This result does **not** decide which case holds. In particular it does
not restore the lost assertion \(m=43\), compute the original first
moment J, or assign the original \(C,b,\lambda,n,\mathcal L\).

## 1. Fields, units and ordinary divisor conventions

Use

\[
 K=\mathbf Q(i),\quad A:y^2=x^3-x,\quad p=43,
 \quad F=K(A[p])^{\mathbf F_p^\times},
\]
\[
 \Delta=\langle\sigma\rangle=C_{44},\quad
 \mathcal O=\mathbf Z_{43}[i],\quad k=\mathcal O/43,
 \quad P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j
            =44e_{\chi^-},
\]

where \(\omega=8+25i\), \(\sigma\) is the positive primary
\(\beta=-1+2i\) direction, and the q component of sigma is 1. There is
no division by 44 in the divisor and unit representatives denoted by
\(P_+\). For every field V here, set

\[
 E_V=(\mathcal O_V^\times\otimes\mathcal O)_{\chi^-},\quad
 D_V=(\operatorname{Div}_{\rm fin}V\otimes\mathcal O)_{\chi^-},
 \quad A_V=(\operatorname{Cl}(V)\otimes\mathcal O)_{\chi^-}.
\]

Let \(P_V\subset D_V\) be the principal divisors. Multiplicative
groups are written additively in this completed summand. All class
modules are finite p-primary modules. Flatness and the prime-to-p
idempotent preserve the exact sequences below. All finite divisors,
including those outside \(\{2,p,q\}\), remain in \(D_V\).

The extensions and generators are

\[
 L=FL_q,\quad \Gamma=\langle\gamma\rangle=C_{43},
 \quad B=K(A[p^2])^{\mu_{42}},
\]
\[
 S=\langle s=1+p\rangle,\quad
 T=\langle t=1+21pi\rangle,\quad \kappa_p(t)=1,
 \quad F_t=B^S,\quad N=LF_t,\quad M'=LB.
\]

The group over F is the direct product \(\Gamma\times S\times T\).
All three factors commute with Delta. The extension B/F ramifies only
at p. At p, Delta is inertial, and its whole nontrivial character
contributes no prime divisor. The extension L/F is split at p and 2
and tame totally ramified at q. At q, the decomposition subgroup of
B/F is S and its positive \(K_q\)-Frobenius is

\[
 \operatorname{Fr}_{K_q}=s^{32};                    \tag{657.4}
\]

T is split. These are the actual marked groups of R561/R613, not newly
chosen abstract generators.

The exact common Robert units of R613/R619 satisfy

\[
 N_{S\times T}u_B=u,\quad N_Su_B=u_t,\quad
 N_Sc_B=c_t,\quad N_\Gamma c_B=(1-s^{11})u_B.
 \tag{657.5}
\]

Both \(u_B\) and \(c_B\) are ordinary units in their respective
completed character channels. The Robert correction \((1-s^{11})u_B\)
has not been deleted. The established inputs are

\[
 E_F=\mathcal O u,\quad u\text{ primitive},\quad A_F=0,
 \quad E_{F_t}=\mathcal O[T]u_t,\quad A_{F_t}=0,
 \tag{657.6}
\]
\[
 A_N=ke_N,\quad e_N=[P_+Q_N],\quad
 \Gamma,T\text{ act trivially on }A_N,              \tag{657.7}
\]

from R163/R210 and R619. R633 gives the complete ordinary unit lattice

\[
 E_N=\mathcal O[T]u_t+\mathcal O y+R_\Gamma[T]c_t.
 \tag{657.8}
\]

Here \(N_\Gamma y=u\), and y has the original R561 definition and
balanced derivative relation. We use the integral lattice (657.8),
not a rational finite-index candidate for it.

## 2. Complete pure-p units and class group

We first prove

\[
 \boxed{E_B=\mathcal O[S,T]u_B,\qquad A_B=0.}       \tag{657.9}
\]

Dirichlet's logarithmic representation in the nontrivial Delta
character is the regular \(S\times T\) representation. Consequently
\(E_B\) is a torsion-free \(\mathcal O\)-lattice of rank \(p^2\).
There is no p-power root of unity: \([B:\mathbf Q]=88p^2\) is not
divisible by 42. Taking invariants gives \(E_B^{S\times T}=E_F\).
If u were in \(pE_B\), its p-division would be invariant, contradicting
the primitivity of u in E_F. Thus \(\bar u\ne0\) in \(E_B/pE_B\).

Modulo p put x=s-1 and z=t-1. The group algebra is

\[
 k[S,T]=k[x,z]/(x^p,z^p).
\]

It is a local Artin ring whose socle is the one-dimensional space
\(k x^{p-1}z^{p-1}=kN_SN_T\). Every nonzero ideal meets this socle:
successively multiply a nonzero element by x and z until it is killed
by both, or use the last nonzero power of the maximal ideal on the
ideal. The map

\[
 k[S,T]\longrightarrow E_B/pE_B,\quad f\longmapsto f\bar u_B
\]

is nonzero on the socle by (657.5). Hence its kernel is zero. Both
spaces have dimension \(p^2\), so it is an isomorphism. The integral
map \(\mathcal O[S,T]\to E_B\) therefore has unit determinant and is
an isomorphism. This proves the saturated unit assertion.

For the class assertion, use B/F_t with group S. At p the character
divisor module is zero; all other primes are unramified. Therefore

\[
 D_B^S=jD_{F_t}.                                   \tag{657.10}
\]

Hilbert 90 injects \(H^1(S,P_B)\) into \(H^2(S,E_B)=0\), since
the unit lattice just proved is S-free. Invariants of the ordinary
divisor sequence show that \(A_B^S\) is generated by invariant
divisors. They descend from \(F_t\), whose character class group is
zero. Thus \(A_B^S=0\), and the invariants property of finite p-group
modules gives \(A_B=0\).

## 3. The Gamma ambiguity calculation at the full p layer

Let

\[
 A_\ell(T)=\sum_{j=0}^{42}\ell_{P_0}(t^ju_t)T^{-j}
              \in k[T].
\]

The exact R198/R619 normalization is

\[
 A_\ell(1)=0,\qquad A_\ell'(1)=-13i\ne0,
 \qquad (A_\ell)=(T-1).                            \tag{657.11}
\]

At q the base B has p T-translates of the marked prime, with residue
degree p over F. The Gamma extension M'/B is tame totally ramified
of degree p. Local reciprocity is compatible with the unramified
S-extension: the local Gamma character on a unit of B is its character
on the local S norm in \(F_t\). Since \(N_Su_B=u_t\), the local
obstruction vector of \(u_B\) is the same vector \(A_\ell\), up to
one invertible reciprocity scalar. S acts trivially on the local
order-p obstruction, and T translates it. By (657.9), the image of
all ordinary units is exactly the ideal \((A_\ell)\subset k[T]\),
of length 42.

At p and 2 the Gamma extension is split; at every other finite place
it is unramified and units are norms. The cyclic Hasse Norm theorem,
after the same flat tensoring as in R619, gives

\[
 \operatorname{length}_{\mathcal O}
 \frac{E_B}{E_B\cap N_\Gamma(M'^\times\otimes\mathcal O)_{\chi^-}}
 =42.                                              \tag{657.12}
\]

The full invariant divisor quotient is

\[
 D_{M'}^\Gamma/jD_B=k[T].                           \tag{657.13}
\]

Indeed the only ramified character divisors are q divisors, with
ramification index p. No divisor outside q is removed; its invariant
orbit descends with ramification index one. Since \(A_B=0\), the
ordinary principal and class exact sequences give

\[
 0\longrightarrow H^1(\Gamma,E_{M'})
 \longrightarrow k[T]\longrightarrow A_{M'}^{\rm st}
 \longrightarrow0,                                \tag{657.14}
\]
\[
 0\longrightarrow A_{M'}^{\rm st}
 \longrightarrow A_{M'}^\Gamma
 \longrightarrow
 \frac{E_B\cap N_\Gamma(M'^\times\otimes\mathcal O)_{\chi^-}}
      {N_\Gamma E_{M'}}
 \longrightarrow0.                                \tag{657.15}
\]

The first cohomology of the full divisor module is zero, as for every
permutation lattice, so the latter sequence has no discarded outside
term. The Dirichlet representation is \(p^2\) copies of the regular
Gamma representation. Its ordinary unit Herbrand quotient is 1:
regular lattices have quotient 1, and finite modules have equal Tate
cohomology sizes. Write \(h_j=\operatorname{length}H^j(\Gamma,E_{M'})\).
Then \(h_1=h_2\), and (657.12)--(657.15) give

\[
 \operatorname{length}_{\mathcal O} A_{M'}^\Gamma
 =43-h_1+(h_2-42)=1.                               \tag{657.16}
\]

The norm to B is zero on class groups, so \(N_\Gamma\) annihilates
\(A_{M'}\). Thus it is a module over the DVR
\(R_\Gamma=\mathcal O[\Gamma]/(N_\Gamma)\).
Its Gamma invariants are its pi-socle. The elementary divisor theorem
and (657.16) prove

\[
 A_{M'}\simeq R_\Gamma/\pi^m\quad(m\ge1).          \tag{657.17}
\]

At this point no value or upper bound for m has been inferred from the
one-dimensional socle.

## 4. All N units are field Norms in the scalar extension

For M'/N, the only ramification is at p. At an unramified place,
ordinary local units are norms. At p the complete local norm quotient
is, by local class field theory, the cyclic scalar group S. Delta
fixes the p primes and conjugates S trivially because the extension
over K is abelian. Consequently this local norm quotient has zero
\(\chi^-\) summand. This includes all its unit and valuation
coordinates. There is no real-place obstruction.

The cyclic Hasse Norm theorem therefore proves

\[
 E_N\subset N_S(M'^\times\otimes\mathcal O)_{\chi^-}.
 \tag{657.18}
\]

In particular y is a field Norm. This assertion concerns ordinary
units as targets, but allows a norm preimage with nonzero finite
divisor. It does not assert that the preimage is an ordinary unit.

All S-invariant character divisors descend, since p is the only
ramified place and its character divisor module is zero:

\[
 D_{M'}^S=jD_N.                                    \tag{657.19}
\]

Hilbert 90 therefore identifies the ordinary capitulation kernel
with \(H^1(S,E_{M'})\). The strongly ambiguous classes are exactly
\(jA_N\). The ambiguous/strongly ambiguous quotient is

\[
 H^1(S,P_{M'})=
 \frac{E_N\cap N_S(M'^\times\otimes\mathcal O)_{\chi^-}}
      {N_S E_{M'}}
 =E_N/N_SE_{M'},                                   \tag{657.20}
\]

using (657.18). The ordinary S unit Herbrand quotient is 1, by the
same regular-representation argument as above. Hence if \(c\) is
the length of the capitulation kernel, it is also the length of
(657.20). Since \(A_N=k\), its length is 1, and the two contributions
give

\[
 \operatorname{length}A_{M'}^S=(1-c)+c=1.           \tag{657.21}
\]

The same exact sequences prove the precise equivalence

\[
 j_{M'/N}\text{ injective}
 \iff H^1(S,E_{M'})=0
 \iff N_SE_{M'}=E_N.                              \tag{657.22}
\]

## 5. Canonical tame-fixed lifts in the ordinary Hilbert extension

We determine the first scalar coefficient with the actual marking.
This step is necessary: a ray class calculation alone would not
identify the action on (657.17).

Take the p-primary Hilbert class extension of M', and its Delta-stable
nontrivial type in which \(A_{M'}\) occurs. Work after the indicated
\(\mathcal O\) tensor and \(\chi^-\) projection. Equivalently, one
may first use the full conjugate pair of characters as an actual
finite Galois group; its Delta invariants are zero. The extension is
Galois over K. Denote its group by G and its abelian class kernel by
A. Its quotient is \(\Delta\times\Gamma\times S\times T\).

Choose a lift of Delta, of order 44, by Schur--Zassenhaus. Its fixed
subgroup on A is zero. Every element of the p-group quotient
\(\Gamma\times S\times T\) has a unique Delta-fixed lift in G.
For completeness, the commutators with Delta of any lift form a
1-cocycle in A. Averaging over Delta gives \(H^1(\Delta,A)=0\),
so an A-translate of the lift centralizes Delta. Its uniqueness is
\(A^\Delta=0\). The product of two such lifts is again fixed;
therefore these lifts form a subgroup isomorphic to
\(\Gamma\times S\times T\). In particular they commute and have
order p. Denote them by \(\gamma_0,s_0,t_0\).

The strict-p genus field H/F of R561/R619 supplies the quotient

\[
 \varphi:A_{M'}\longrightarrow k.                  \tag{657.23}
\]

Here H/F is the elementary abelian q-ray extension of order \(p^2\)
in the nontrivial two-dimensional Delta type. Its intersection with
M' is F, because M'/F has trivial Delta conjugation. The base change
HM'/M' is unramified: at q the compositum over F is abelian of
exponent p, so its tame inertia has order at most p, already supplied
by L; at p and 2, H is split, and elsewhere it is unramified. This
checks every finite place. The resulting quotient (657.23) is onto
and annihilated by \(\pi\); by (657.17) it identifies
\(A_{M'}/\pi A_{M'}\) with k.

Choose a generator of (657.17) whose image under \(\varphi\) is 1.
The canonical lifts \(\gamma_0,s_0,t_0\) have zero H-coordinate:
their H-coordinates are Delta-fixed, whereas the type of H has no
Delta invariants.

At the marked q prime, let x be the actual tame inertia generator
projecting to gamma and let f be positive Frobenius of \(K_q\).
In semidirect coordinates they have the form

\[
 x=(a_q,\gamma_0),\qquad f=(b_q,s_0^{32}).          \tag{657.24}
\]

The q-ray uniformizer convention of R561 has no Gamma unramified
component, and (657.4) fixes the scalar component. R561's original
strict-p genus normalization is

\[
 \varphi(a_q)=-i,\qquad \varphi(b_q)=32.            \tag{657.25}
\]

These are respectively the \(K_0\mapsto-i\) inertia coordinate and
the positive finite coordinate \(2\cdot16\). No unramified
restriction factor is introduced a second time.

The Hilbert extension is unramified over M', so x has order p.
The local tame relation is
\(fxf^{-1}=x^{q^2}=x\), since \(q^2\equiv1\pmod p\).
Writing it in (657.24) gives the actual ordinary-module identity

\[
 (s^{32}-1)a_q=\pi b_q.                            \tag{657.26}
\]

Every order-p automorphism of the cyclic module (657.17) is scalar
over \(R_\Gamma\), because it commutes with Gamma. Modulo pi it is
1, since \(k^\times\) has order prime to p. If \(m\ge2\), write
\(s=1+a_s\pi\pmod{\pi^2}\). Then (657.25)--(657.26) imply

\[
 32a_s(-i)=32,\qquad a_s=i.                        \tag{657.27}
\]

For \(m=1\), there is no first-order coefficient to determine. We
do not use (657.27) to assert \(m\ge2\).

Similarly write \(t=1+b\pi\pmod{\pi^2}\) when \(m\ge2\).
The semilinear tau action conjugates coefficients, sends
\(\pi\) to \(-\pi\) modulo \(\pi^2\), and sends t to its inverse.
Consequently \(b=\bar b\in\mathbf F_{43}\). This is only its
coefficient field; no value of b has been computed.

## 6. The sharp upper bound and the two transfer possibilities

In \(R_\Gamma\), the cyclotomic relation gives

\[
 p\equiv-\pi^{p-1}\pmod{\pi^p}.                   \tag{657.28}
\]

Suppose first \(m\ge2\) and lift its s-action to
\(v\in R_\Gamma^\times\) with \(v=1+i\pi\pmod{\pi^2}\).
In the binomial expansion of \(v^p-1\), only the linear and the
p-th terms contribute at valuation p. All intermediate binomial
coefficients are divisible by p and contribute valuation at least
p+1. Thus

\[
 v^p-1\equiv(i^p-i)\pi^p=-2i\pi^{43}
          \pmod{\pi^{44}}.                        \tag{657.29}
\]

The coefficient is nonzero because \(i^{43}=-i\). The s-action has
order dividing p, so \(v^p-1\in\pi^mR_\Gamma\), forcing
\(m\le43\). The case \(m=1\) satisfies the same bound trivially.
This completes (657.1).

When \(m\ge2\), divide (657.29) by \(v-1\) to obtain the norm
operator on the actual class module:

\[
 N_S=1+s+\cdots+s^{42}
       \equiv-2\pi^{42}\pmod{\pi^{43}}.            \tag{657.30}
\]

Therefore it is zero if \(m\le42\), and nonzero if \(m=43\).
For \(m=1\), it is also zero, since the action is trivial and
\(pA_{M'}=0\). Formula (657.30) is independent of the chosen lift
when interpreted in the finite quotient.

The class norm

\[
 \operatorname{Nm}_{M'/N}:A_{M'}\longrightarrow A_N
 \tag{657.31}
\]

is surjective. Indeed M'/N is a ramified cyclic extension of prime
degree, whereas the Hilbert class field of N is unramified. They
have trivial intersection over N. Base change of the latter field
and functoriality of Artin therefore make the norm onto, including
in the specified character summand.

Composition of (657.31) with extension of ideals is the group-ring
operator \(N_S\). Since \(A_N=k\), (657.30) and surjectivity show

\[
 \begin{cases}
 m=43 &: j_{M'/N}\ne0,\text{ hence injective},\\
 1\le m\le42 &: j_{M'/N}=0.
 \end{cases}                                      \tag{657.32}
\]

Together with (657.22), this proves the first three equivalences in
(657.3), as well as the asserted index \(|k|\) at the lower endpoint
range. It does not prove that the nonzero norm operator occurs.

## 7. The missing ordinary unit is exactly the original y

The norms in (657.5) already put \(u_t\) and \(c_t\), with all their
commuting Gamma and T translates, in \(N_SE_{M'}\). The full ordinary
unit lattice (657.8) then gives

\[
 N_SE_{M'}=E_N\iff y\in N_SE_{M'}.                 \tag{657.33}
\]

This proves the last equivalence in (657.3). In the range \(m\le42\)
the quotient \(E_N/N_SE_{M'}\) has length one and the image of y
generates it. It is not possible to establish (657.33) merely by
choosing a Hasse norm preimage Y: (657.18) always supplies such a Y,
but its full finite divisor can obstruct replacing it by an ordinary
unit. That divisor is the ordinary capitulation obstruction measured
by (657.32).

For comparison, the original R599 element \(X_t\) is a specified
q-principalization in \(F_t\), satisfying
\(\operatorname{div}X_t=P_+P_0\) and
\(N_TX_t=P_+(89460y_F+1)\). Its residue first moment J has not been
evaluated here. Neither (657.3) nor (657.33) constitutes a numerical
evaluation of J or a bridge assigning the original scalar C.

## 8. Source and recovery boundary

All finite arithmetic used above is already contained in R198,
R561, R613 and R619: the anti-p derivative \(-13i\), q Frobenius
\(s^{32}\), and the strict-p genus coordinates \((-i,32)\).
The only new arithmetic in the upper-bound step is the displayed
cyclotomic binomial expansion. No large Robert evaluation or class
group computation was rerun.

The unit and ordinary class inputs are R163/R210, R619 and R633.
The cyclic Hasse Norm theorem is J. S. Milne, *Class Field Theory*,
Chapter VIII, Theorem 3.1, printed p.234:
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>.
The divisor/cohomology arguments, tame-fixed lifts, first scalar
coefficient, transfer dichotomy and ordinary-unit criterion are proved
above. The lost R570/R573/R577 texts are not used as proofs or as
numerical evidence for the unresolved endpoint.
