# R1005 — The finite Gauss companion and its complete resonance defect

Date: 2026-11-26. Session: Astra-serre-24b8836b-20261126.
Authors: o2_high_coefficient / root.

**Status: proved polynomial identities and exact original-coefficient interface.** The root independently checked the nonhomogeneous Gauss equation, the signed Wronskian derivative and its integration constant. These identities preserve the full resonance defect. They do not assert all-prime nonvanishing or Serre uniformity. No new prime window was executed.

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
\tag{1005.1}
$$

Every denominator in (1005.1) is a unit. Its last denominator factor of the
form $3j+2$ is $3d-1=p-3$. Every numerator is a unit as well. Indeed, the
first index $j\ge0$ at which $12j+1$ or $12j+7$ is divisible by $p$ is
$5k+2$ in the row $p=12k+5$, or $5k+4$ in the row $p=12k+11$; these are
strictly larger than $d-1=4k$ or $4k+2$, respectively. Therefore

$$
\deg P=d,\qquad P(0)=1,\qquad a_d\ne0.
\tag{1005.2}
$$

The second rational input is the degree-$k$ polynomial

$$
C(z)=\sum_{i=0}^k\frac{b_i}{3i+1}z^i,
\qquad C+3zC'=B.
\tag{1005.3}
$$

The factors $3i+1$ are all units because $3k+1<p$. No index $\ell$ is
divided by $1-3\ell$.

## 2. Exact nonhomogeneous Gauss equation

Let

$$
\mathscr L_A=z(1-z)\partial_z^2+
\left(\frac23-\frac53z\right)\partial_z-\frac7{144}.
$$

The successive coefficient ratios in (1005.1) show that the coefficients of
$\mathscr L_A P$ at $z^0,\ldots,z^{d-1}$ vanish. The top coefficient is

$$
-\left(d+\frac1{12}\right)
 \left(d+\frac7{12}\right)a_d.
$$

Since $d\equiv-2/3\pmod p$, this gives the complete identity

$$
\boxed{\mathscr L_A P=-\frac7{144}a_d z^d.}
\tag{1005.4}
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
\tag{1005.5}
$$

Set

$$
K(z)=(1-z)\{PB+3z(PB'-P'B)\}.
$$

Differentiating the bracket and using (1005.5) gives, for an arbitrary
polynomial $P$,

$$
K'=-3B\mathscr L_A P.
\tag{1005.6}
$$

For completeness, if $W=PB+3z(PB'-P'B)$, then

$$
(1-z)W'=W-3B\mathscr L_A P;
$$

this proves (1005.6) including its sign. Insert (1005.4). Since $K(0)=1$ and
$d+1=\ell$, termwise integration has only denominators $\ell+i$ with
$0\le i\le k$. These integers lie strictly between zero and $p$.
Because $\ell\equiv1/3\pmod p$, the exact result is

$$
K(z)=1+\frac7{16}a_d z^\ell C(z).
\tag{1005.7}
$$

There is no possible nonconstant $p$th-power integration constant:
$\deg K\le\ell+k<p$.

The scalar in (1005.7) is already determined by R990's proved first
resonance, and is not a new unknown period. Put

$$
H(z)=\frac1{(1-z)B(z)^2},\qquad q(z)=P(z)/B(z).
$$

Dividing (1005.7) by $(1-z)B^2$ gives

$$
q-3zq'=H\left(1+\frac7{16}a_d z^\ell C\right).
\tag{1005.8}
$$

The coefficient of $z^\ell$ on the left is zero. On the right it is
$H_\ell+(7/16)a_d$, since $H(0)=C(0)=1$. The already established
R990(990.35) says $H_\ell=B(1)^{-2}$. Hence

$$
\boxed{a_d=-\frac{16}{7 B(1)^2},}
\tag{1005.9}
$$

and the complete polynomial identity is

$$
\boxed{
(1-z)\{PB+3z(PB'-P'B)\}
=1-\frac{z^\ell C(z)}{B(1)^2}.
}
\tag{1005.10}
$$

Thus the actual continued source satisfies, as an identity of rational
functions and not just a jet,

$$
\boxed{
\frac PB-3z\left(\frac PB\right)'
=\frac{1-z^\ell C(z)/B(1)^2}{(1-z)B(z)^2}.
}
\tag{1005.11}
$$

The correction beginning at $z^\ell$ is necessary. It cancels the exact
nonzero obstruction to a homogeneous primitive. It cannot be discarded
when a global residue calculation uses $P/B$ outside the original jet.

Substitution $z=1$ in (1005.10) also gives a finite hypergeometric identity

$$
\boxed{C(1)=B(1)^2.}
\tag{1005.12}
$$

This last equality also follows from the terminating balanced
${}_3F_2$ sum for $C$, but no external summation theorem is needed:
(1005.12) has just been proved from the two specified differential equations
and R990's already proved residue normalization.

The numerator in (1005.11) has a simple zero at $z=1$. Indeed its derivative
there is $-1/(3B(1))\ne0$, by (1005.3). This provides a full polynomial
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
\tag{1005.13}
$$

The scalar is unchanged. Thus all necessary inputs are now honest
polynomials of degrees $k$ and $d$ with the full identity (1005.10).
There is no new locally chosen solution or free coefficient in $P$.
The original target is at $m=d$ for $r=2$, or at $m=d-2$ for $r=8$.

For a possible next global argument, define the rational differential

$$
\nu=\frac1{z^{m+1}}
\left(4+12z\frac{B'}B-\frac z{1-z}\right)
\frac{B^r}{P^r}\,dz.
\tag{1005.14}
$$

Its residue at zero is precisely the coefficient in (1005.13). Every root
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
control every residue at $P=0$; (1005.10) does not allow those residues to
be dropped. If $P(1)=0$, the cusp and that root are one pole and must
be treated together, so the displayed quotient must not be used.

The new polynomial companion does not prove that this complete sum is
nonzero. It removes the former ambiguity about a continuation through
the Gauss resonance and gives a global object on which such a proof must
operate. Neither the nonzero leading coefficient (1005.9) nor the unit cusp
value (1005.12) is substituted for the varying coefficient in (1005.13).


## 5. Cusp normalization and the complete residue sum in the original r=2 row

This section retains the original row $p\equiv11\pmod{12}$, $p\ge41$,
$r=2$, $m=d=\ell-1$. Put $b=B(1)$ and $\kappa=1/(9b^2)$.
Equations (1005.4) and (1005.9) give
$\mathscr L_AP=\kappa z^d$.

### 5.1 A permitted change of global continuation

Let $Y=z^\ell B$. Since $\ell\equiv1/3\pmod p$, direct substitution gives
$
\mathscr L_A(z^\ell B)=z^\ell\mathscr L_BB=0.
\tag{1005.15}
$
Indeed the coefficient of $z^{-1}B$ is $\ell(\ell-1/3)=0$;
the new derivative coefficients are $4/3-7z/3$, and the constant term
is $-\ell(\ell+2/3)-7/144=-55/144$.
Consequently
$
S_\lambda=P+\lambda z^\ell B
\tag{1005.16}
$
has the same nonhomogeneous equation and the same complete $K$ of
(1005.10). It also agrees with $P$ modulo $z^\ell$, so the actual coefficient
$
J=[z^d]QB^2/S_\lambda^2,\qquad
Q=4+12zB'/B-z/(1-z)
\tag{1005.17}
$
is independent of $\lambda$.

Choose the unique $\lambda_*=-P(1)/b$ and write $S=S_{\lambda_*}$.
Then $S(1)=0$, while evaluating the equation at $1$ gives
$
S'(1)=-\kappa\ne0.
\tag{1005.18}
$
Also $S(0)=1$, and its degree is $d$ if $\lambda_*=0$, or $\ell+k$
otherwise. Both are less than $p$.
Every root $\alpha\ne0,1$ of $S$ has multiplicity at most two:
multiplicity at least three would force
$\mathscr L_AS(\alpha)=0$, contrary to $\kappa\alpha^d\ne0$.
No coprimality of $S$ and $B$ is assumed.

### 5.2 The exact cusp residue

Write $t=z-1$, $B=b\sum\beta_jt^j$ and $S=\sum s_jt^j$.
Their exact differential equations give
$
\beta_0=1,\qquad
\beta_{j+1}=-\frac{(j+5/12)(j+11/12)}{(j+1)^2}\beta_j,
$
$
s_0=0,\qquad
(j+1)^2s_{j+1}
=-(j+1/12)(j+7/12)s_j-\kappa\binom dj.
\tag{1005.19}
$
Only $j=0,1,2$ is needed. Since $d\equiv-2/3$, this yields
$
B=b\left(1-\frac{55}{144}t+
            \frac{21505}{82944}t^2+O(t^3)\right),
$
$
S=-\kappa t\left(1-\frac{343}{576}t+
                \frac{311905}{746496}t^2+O(t^3)\right),
$
$
Q=t^{-1}+\frac5{12}-\frac{385}{3456}t+O(t^2).
\tag{1005.20}
$
Together with $z^{-\ell}=1-t/3+2t^2/9+O(t^3)$, these give
$
z^{-\ell}B^2/S^2=
81b^6t^{-2}\left(1+\frac3{32}t+
 \frac{187147}{2985984}t^2+O(t^3)\right).
\tag{1005.21}
$
For the actual rational differential
$
\nu=z^{-\ell}QB^2/S^2\,dz
$
we obtain the full residue at the coincident cusp and denominator root:
$
\begin{aligned}
\operatorname{Res}_{1}\nu
&=81b^6\left(\frac{187147}{2985984}
 +\frac3{32}\frac5{12}-\frac{385}{3456}\right)\\
&=\boxed{-\frac{28853}{36864}b^6.}
\end{aligned}
\tag{1005.22}
$
All displayed denominators have only the primes $2,3$.
Furthermore $28853=11\cdot43\cdot61$, so (1005.22) is a unit
at every prime in this original $r=2$ row: $p\ge41$ and $p\equiv11\pmod{12}$
exclude all three factors.

One may also verify the same calculation without first multiplying
the $B^2$ expansion: division in (1005.20) gives
$
S/B=-\frac{t}{9b^3}
 \left(1-\frac{41}{192}t+\frac{57475}{746496}t^2+O(t^3)\right).
$
Substitution in $z^{-\ell}Q/(S/B)^2$ yields exactly (1005.22).

### 5.3 The remaining roots cannot be discarded

The finite poles other than zero are contained in
$\{1\}\cup\{S=0\}$, retaining common roots with $B$ at their actual orders.
There is no residue at infinity: $\deg S\ge d$ gives coefficient order
at most $2(k-d)-\ell<-1$.
Thus the complete residue theorem says exactly
$
\boxed{
J=\frac{28853}{36864}b^6-
 \sum_{\substack{S(\alpha)=0\\\alpha\ne1}}
       \operatorname{Res}_{\alpha}\nu.
}
\tag{1005.23}
$
Each geometric point is counted once, with its actual pole order.
The unit cusp term is not the full answer.

The existing certified $p=47$ row of R973 gives a concrete check of this
boundary without a new computation. Its original $c_{45}^-=4$, hence
$c_{45}^+=43$; the separate report field named original-B is $10$ and must
not be read as $c_{45}^-$. Here
$
b=(-1)^3\,3!/(4/3)_3=34,\quad b^6=3,\quad
(-32)^{15}/4=31\qquad\text{in }\mathbb F_{47}.
$
The unchanged (1005.13) therefore gives $J=12$,
while (1005.22) gives $\operatorname{Res}_1\nu=45$.
Consequently
$
\sum_{\substack{S(\alpha)=0\\\alpha\ne1}}
       \operatorname{Res}_\alpha\nu=37\ne0
       \qquad\text{in }\mathbb F_{47}.
\tag{1005.24}
$
This consumes R973's old certified coefficient and the displayed exact
identities; it does not rerun that finite point.
It disproves the claim that the other root residues automatically sum
to zero after this cusp normalization. It does not disprove possible
nonvanishing of the complete sum, which remains the required input.

## 6. Dependencies and scope

- [R988](R988-original-pure-balanced-Cartier-contraction-and-high-trace.md) gives the original high-coordinate/whole-trace equivalence.
- [R990](R990-original-hypergeometric-fixed-r-coefficient.md), especially (990.35), supplies the precisely normalized first resonance and the original fixed-r coefficient formula. All new finite-polynomial identities used here are proved above.
- [R973](R973-certified-balanced-Kronecker-coefficients-at-four-primes.md), §3: the already certified original $p=47$ coefficient used in (1005.24).
- [R1003](R1003-global-scope-and-remaining-branches.md) records the distinction between this specified auxiliary source and the full Serre problem.

The remaining assertion is the nonzero coefficient in (1005.13). The unit leading coefficient and the normalized cusp identity do not determine it. Every root of the actual denominator polynomial must remain in a residue argument.
