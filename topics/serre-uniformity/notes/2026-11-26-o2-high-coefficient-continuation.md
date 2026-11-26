# O2 continuation: the full finite Gauss companion and its exact defect

Date: 2026-11-26. Session: serre-public-astra-20261126-24b8836b.
Authoring agent: o2_high_coefficient.

**Status: proved polynomial identities and a precise continued source; the
all-prime high-coordinate nonvanishing remains open.** This note consumes,
without re-executing, R988 and R990. No finite-prime window or other numerical
mathematics was executed. All statements below follow symbolically from the
specified Gauss equations.

## 1. The actual input and the new finite polynomial

Use the original rows of R990:

$$
p\ge 41,\qquad p\equiv2,5\pmod9,\qquad
r=\begin{cases}2,&p\equiv11\pmod{12},\\8,&p\equiv5\pmod{12}.
\end{cases}
$$

Put

$$
k=\lfloor p/12\rfloor,\quad
\ell=(p+1)/3,\quad d=\ell-1,\quad
b=(r+1)/3,\quad m=\ell-b.
$$

All polynomial identities in this note are over $\mathbb F_p$. Write

$$
B(z)={}_2F_1(-k,k+4/3;4/3;z)
=\sum_{i=0}^k b_i z^i,
$$

for the actual degree-$k$ Jacobi polynomial of R990, normalized by $b_0=1$.
Define a second, **specified** polynomial by truncating the other actual
Gauss solution exactly before its first nonintegral coefficient:

$$
P(z)=\sum_{i=0}^{d} a_i z^i,\qquad
 a_i=\frac{(1/12)_i(7/12)_i}{(2/3)_i i!} \pmod p.
\tag{O2.1}
$$

Every denominator in (O2.1) is a unit. Its last denominator factor of the
form $3j+2$ is $3d-1=p-3$. Every numerator is a unit as well. Indeed, the
first index $j\ge0$ at which $12j+1$ or $12j+7$ is divisible by $p$ is
$5k+2$ in the row $p=12k+5$, or $5k+4$ in the row $p=12k+11$; these are
strictly larger than $d-1=4k$ or $4k+2$, respectively. Therefore

$$
\deg P=d,\qquad P(0)=1,\qquad a_d\ne0.
\tag{O2.2}
$$

The second rational input is the degree-$k$ polynomial

$$
C(z)=\sum_{i=0}^k\frac{b_i}{3i+1}z^i,
\qquad C+3zC'=B.
\tag{O2.3}
$$

The factors $3i+1$ are all units because $3k+1<p$. No index $\ell$ is
divided by $1-3\ell$.

## 2. Exact nonhomogeneous Gauss equation

Let

$$
\mathscr L_A=z(1-z)\partial_z^2+
\left(\frac23-\frac53z\right)\partial_z-\frac7{144}.
$$

The successive coefficient ratios in (O2.1) show that the coefficients of
$\mathscr L_A P$ at $z^0,\ldots,z^{d-1}$ vanish. The top coefficient is

$$
-\left(d+\frac1{12}\right)
 \left(d+\frac7{12}\right)a_d.
$$

Since $d\equiv-2/3\pmod p$, this gives the complete identity

$$
\boxed{\mathscr L_A P=-\frac7{144}a_d z^d.}
\tag{O2.4}
$$

In particular the truncated source is not a second polynomial solution
of the homogeneous Gauss equation. The right side is nonzero at every
nonzero finite $z$. It is precisely the global defect that would be lost
by extending the homogeneous equation past the first resonant index.

## 3. The complete Wronskian polynomial, with its fixed scalar

The Jacobi polynomial satisfies the exact reduced equation

$$
z(1-z)B''+\left(\frac43-\frac73z\right)B'
-\frac{55}{144}B=0.
\tag{O2.5}
$$

Set

$$
K(z)=(1-z)\{PB+3z(PB'-P'B)\}.
$$

Differentiating the bracket and using (O2.5) gives, for an arbitrary
polynomial $P$,

$$
K'=-3B\mathscr L_A P.
\tag{O2.6}
$$

For completeness, if $W=PB+3z(PB'-P'B)$, then

$$
(1-z)W'=W-3B\mathscr L_A P;
$$

this proves (O2.6) including its sign. Insert (O2.4). Since $K(0)=1$ and
$d+1=\ell$, termwise integration has only denominators $\ell+i$ with
$0\le i\le k$. These integers lie strictly between zero and $p$.
Because $\ell\equiv1/3\pmod p$, the exact result is

$$
K(z)=1+\frac7{16}a_d z^\ell C(z).
\tag{O2.7}
$$

There is no possible nonconstant $p$th-power integration constant:
$\deg K\le\ell+k<p$.

The scalar in (O2.7) is already determined by R990's proved first
resonance, and is not a new unknown period. Put

$$
H(z)=\frac1{(1-z)B(z)^2},\qquad q(z)=P(z)/B(z).
$$

Dividing (O2.7) by $(1-z)B^2$ gives

$$
q-3zq'=H\left(1+\frac7{16}a_d z^\ell C\right).
\tag{O2.8}
$$

The coefficient of $z^\ell$ on the left is zero. On the right it is
$H_\ell+(7/16)a_d$, since $H(0)=C(0)=1$. The already established
R990(990.35) says $H_\ell=B(1)^{-2}$. Hence

$$
\boxed{a_d=-\frac{16}{7 B(1)^2},}
\tag{O2.9}
$$

and the complete polynomial identity is

$$
\boxed{
(1-z)\{PB+3z(PB'-P'B)\}
=1-\frac{z^\ell C(z)}{B(1)^2}.
}
\tag{O2.10}
$$

Thus the actual continued source satisfies, as an identity of rational
functions and not just a jet,

$$
\boxed{
\frac PB-3z\left(\frac PB\right)'
=\frac{1-z^\ell C(z)/B(1)^2}{(1-z)B(z)^2}.
}
\tag{O2.11}
$$

The correction beginning at $z^\ell$ is necessary. It cancels the exact
nonzero obstruction to a homogeneous primitive. It cannot be discarded
when a global residue calculation uses $P/B$ outside the original jet.

Substitution $z=1$ in (O2.10) also gives a finite hypergeometric identity

$$
\boxed{C(1)=B(1)^2.}
\tag{O2.12}
$$

This last equality also follows from the terminating balanced
${}_3F_2$ sum for $C$, but no external summation theorem is needed:
(O2.12) has just been proved from the two specified differential equations
and R990's already proved residue normalization.

The numerator in (O2.11) has a simple zero at $z=1$. Indeed its derivative
there is $-1/(3B(1))\ne0$, by (O2.3). This provides a full polynomial
cusp normalization, not a nonvanishing assertion for the target at $z=0$.

## 4. What this does to the actual high coefficient

In the original required range $0\le i\le m<\ell$, $P$ agrees with the
characteristic-zero $A$ after reduction. Since $B(0)=P(0)=1$, R990's actual
fixed-exponent formula becomes exactly

$$
\boxed{
c_{p-r}^+=\frac{(-32)^m(r-1)!}{4}
[z^m]\left(4+12z\frac{B'}B-\frac z{1-z}\right)
\frac{B^r}{P^r}.
}
\tag{O2.13}
$$

The scalar is unchanged. Thus all necessary inputs are now honest
polynomials of degrees $k$ and $d$ with the full identity (O2.10).
There is no new locally chosen solution or free coefficient in $P$.
The original target is at $m=d$ for $r=2$, or at $m=d-2$ for $r=8$.

For a possible next global argument, define the rational differential

$$
\nu=\frac1{z^{m+1}}
\left(4+12z\frac{B'}B-\frac z{1-z}\right)
\frac{B^r}{P^r}\,dz.
\tag{O2.14}
$$

Its residue at zero is precisely the coefficient in (O2.13). Every root
of $B$ that is not also a root of $P$ is regular for $\nu$: the apparent
$B'/B$ pole is canceled by $B^r$, with $r\ge2$. Its only other finite
poles are at $1$ and the roots of $P$. There is no residue at infinity,
since its coefficient has order at most

$$
r(k-d)-m-1<-1
$$

there. Consequently the target is the negative of the **entire** residue
sum over $\{1\}\cup\{P=0\}$. If $P(1)\ne0$, the cusp contributes
$B(1)^r/P(1)^r$. A proof using just this cusp term must additionally
control every residue at $P=0$; (O2.10) does not allow those residues to
be dropped. If $P(1)=0$, the cusp and that root are one pole and must
be treated together, so the displayed quotient must not be used.

The new polynomial companion does not prove that this complete sum is
nonzero. It removes the former ambiguity about a continuation through
the Gauss resonance and gives a global object on which such a proof must
operate. Neither the nonzero leading coefficient (O2.9) nor the unit cusp
value (O2.12) is substituted for the varying coefficient in (O2.13).

## 5. External inputs considered and retained scope

The primary text of A. Lozano-Robledo, *Bernoulli--Hurwitz numbers,
Wieferich primes and Galois representations*, J. Number Theory 130
(2010), 539--558, was checked (Theorem 1.2 and §6.1, Theorem 6.3).
The all-but-finitely-many inert-prime assertion there is for a specified
Rohrlich deformation and excludes discriminants $-3,-4$. Its inert
Kummer criterion detects a pair of Frobenius-related pure Hurwitz
coefficients by requiring at least one to be nonzero. It therefore does
not give the individual high coordinate in R988. No result from that
paper is used in (O2.1)--(O2.14).

Primary author copy:
https://production.wordpress.uconn.edu/alozano/wp-content/uploads/sites/490/2014/01/lozano_robledo_BH.pdf

The unit/primitivity and conjugation information of R972 is unchanged.
Local Tate duality would introduce the actual cyclotomic dual character;
it cannot identify the two Artin--Hasse coordinates merely by complex
conjugation. This note makes no new claim about such a duality argument.

## 6. Remaining exact assertion

The open assertion is still the nonzero coefficient in (O2.13), for all
original primes or for all sufficiently large original primes. R988
transports this to the same original high coordinate and whole trace.
The same-label condition of O1 and the genuine global height issue
remain additional tasks even if this assertion is resolved.
