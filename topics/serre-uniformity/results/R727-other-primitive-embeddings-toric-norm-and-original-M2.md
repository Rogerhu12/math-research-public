# R727 — Other primitive embeddings: the actual toric norm and an original $M_2$ criterion

Date: 2026-11-14. Status: **proved, with the arithmetic conditions displayed
below**. This result keeps the actual positive cubic quotient, its tame
marking, the cusp-normalized split vector and its Cartan average.
It does not prove that the original $C_p$ is always a unit.

Let $p\ge41$, $p\equiv5\pmod6$, $n=p+1$, and choose

$$
7\le h\le p-4,\qquad h\equiv1\pmod6,\qquad (h,p+1)=1.
\tag{727.1}
$$

Put $\theta_h=\theta_{-1}^{\,h}$, with the original Teichmueller
orientation $\theta_h(y)=[y]^{-h(p-1)}$.
Let $M_{m,h}$ denote the jets of the same actual $c_1$ marking for this
coefficient embedding. The index $h=1$ is deliberately excluded from
(727.1); its exceptional Fourier cancellation is exactly the one treated
in R595/R605.

## 1. Statements

Write $\mathsf T_\zeta$ for the original CM torus in the period basis
$(\zeta,1)$, and retain the R588 finite Hermitian form and average:

$$
G(e_r,e_s)=p\delta_{rs}-1,\qquad
u_h=\frac1{p+1}\operatorname{Tr}_{\mathsf T_\zeta}e_0,\qquad
N_h=G(e_0,\operatorname{Tr}_{\mathsf T_\zeta}e_0).
\tag{727.2}
$$

Let $P_d(X)$ be the Legendre polynomial normalized by $P_d(1)=1$.
Then $N_h$ is integral in the unramified character field, is nonzero,
and

$$
\boxed{
N_h\equiv-
 P_{h-1}\!\left(\frac1{\sqrt{-3}}\right)^2\pmod p.
}
\tag{727.3}
$$

The value inside the square is rational because $h-1$ is even; its
denominator is prime to $p$. Formula (727.3) is the norm of the
original pair consisting of the split vector and the CM torus. Moving
the torus to trace-zero coordinates while leaving $e_0$ fixed would
give a different expression.

Let

$$
R=R_-=\frac{x^2(x^6+34x^3-8)}
 {x^9-228x^6+48x^3-64},\qquad
\mathfrak r_k=[z^{(p-1)k}]R\pmod p,
$$
$$
B=(-1)^{(p-1)/2-(p-2)/3}
 \binom{(p-1)/2}{(p-2)/3},\qquad
C_0=72\beta/\alpha,\quad\alpha^3=4,\quad\beta^2=3.
\tag{727.4}
$$

All are in the original R588/R595 normalization. Set
$Q_h=(h-2)(h-1)h(h+1)(h+2)$.
The full original finite sums satisfy

$$
\boxed{
\frac{p^4S_{2,h}S_{3,h}}{C_0^2}
 \equiv-\frac{B^5}{144}\,Q_h\,
       \mathfrak r_{h-2}\mathfrak r_{p-h-2}\pmod p,
}
\tag{727.5}
$$

and the actual original norm gives

$$
\boxed{
\frac{(p^2M_{2,h})^2}{\zeta^2}
 \equiv\frac{864N_hB^5}{\alpha^2}\,Q_h\,
       \mathfrak r_{h-2}\mathfrak r_{p-h-2}\pmod p.
}
\tag{727.6}
$$

In particular, if the three original residues

$$
N_h,\qquad C_{h-2},\qquad C_{p-h-2}
\tag{727.7}
$$

are units, then $v_p(M_{2,h})=-2$. Under precisely these hypotheses
the corresponding original scalar Abel primitive has only the center
as a zero in the entire open disc

$$
v_p(a-1)>3.
\tag{727.8}
$$

This zero assertion includes the complete infinite tail and the original
flat/coarse change. It does not assume that R434's special integral
lattice for $\theta_{\pm1}$ remains integral for $\theta_h$.

For $h=7$, the finite norm simplifies to

$$
\boxed{N_7\equiv-(47/9)^2\pmod p.}
\tag{727.9}
$$

Thus, when $7\nmid p+1$ and $p\ne47$, the single additional condition
$C_{p-9}\ne0\pmod p$ suffices for (727.8), since $C_5=9/2$.
The excluded norm prime $p=47$ is a genuine exception to this particular
norm-unit assertion: $h=7$ is primitive there and $N_7\equiv0$.
It is not a zero of the original $C_p$, and it does not contradict
the original $h=1$ coefficient criterion.

## 2. Why these are actual coefficient embeddings with the same tame direction

The original character satisfies
$\theta_{-1}(\zeta)=\zeta^{-1}$ and
$\theta_{-1}(\sqrt{-3})=-1$. The conditions in (727.1) imply

$$
\theta_h(\zeta)=\zeta^{-1},\qquad
\theta_h(\sqrt{-3})=-1,\qquad
\operatorname{ord}(\theta_h)=p+1.
$$

The cyclotomic automorphism sending a character value to its $h$-th
power fixes $\zeta_3$. It therefore leaves the positive cubic
character $\kappa_4$, the actual tame vector
$H_0-4\zeta^2H_2$, and its degree rule $m\equiv2\pmod3$ unchanged.
The resulting newform is a coefficient conjugate of the same actual
R575 isotypic factor. Distinct labels need not be counted as distinct
embeddings for this argument; it uses only that each is an embedding
of that same factor.

There is no need to extend this automorphism so that it artificially
fixes every auxiliary square root in the eighteen-point description.
The $H_0,H_2$ vector is defined using its displayed $\mu_3$ values.
A change of the auxiliary sign of $\beta$ changes the two finite
sums together and leaves their product, $C_0^2$, and the norm identities
unchanged. We use the fixed labeled sums throughout.

The exact character/period formulas are therefore still

$$
\xi_{5,h}((a))=a^5\chi_6(a)\theta_h(a)^{-1},\qquad
\xi_{7,h}((a))=a^7\chi_6(a)\theta_h(a),
$$
$$
L(\xi_{5,h},3)=\frac{\Omega\,2!\mathcal A^2}{36p}S_{2,h},\qquad
L(\xi_{7,h},4)=\frac{\Omega\,3!\mathcal A^3}{36p}S_{3,h}.
\tag{727.10}
$$

The finite sums keep the same CRT signs:

$$
S_{2,h}=-\sum_a\theta_h(a)H_2(P_a),\qquad
S_{3,h}=-\sum_a\theta_h(a)^{-1}H_3(P_a).
\tag{727.11}
$$

R588's finite $p$-factor is $N_h/(p+1)^2$; the other local and
archimedean factors and the two factorials do not change.
The norm identity is consequently

$$
M_{2,h}\overline M_{2,h}
 =\frac{8N_h}{(p+1)^2}S_{2,h}S_{3,h},\qquad
\overline M_{2,h}=-\zeta M_{2,h}.
\tag{727.12}
$$

For the first equality, the local argument only uses the primitive
cuspidal finite representation and its actual torus average; its norm
is retained as $N_h$, without a unit substitution.
For the second, the Weyl coefficients remain real: Frobenius on
$\mathbf F_{p^2}$ preserves every norm/trace fiber and interchanges
$\theta_h$ with $\theta_h^{-1}$. The character is odd, so the
normalizer reflection fixes the plus line. The transported tame
anti-linear matrix of R588 is unchanged and still sends
$(1,-4\zeta^2)^t$ to its factor $-\zeta$.
This proves (727.12) before applying the selected $p$-adic embedding.

## 3. The full finite-field fiber identity

The following calculation replaces the constant fiber sum special to
$h=1$. Work in characteristic $p$; let $h$ be odd,
$1\le h<p$, and put $d=h-1$. Then for every $r,s\in\mathbf F_p$,

$$
\boxed{
\sum_{\substack{y\in\mathbf F_{p^2}^{\times}\\
                 r\operatorname N(y)+\operatorname{Tr}(y)=s}}
 y^{h(p-1)}
 =P_d(1+2rs).
}
\tag{727.13}
$$

The same formula holds with exponent $-h(p-1)$, since Frobenius
interchanges the two weights and preserves the fiber.

If $r=0,s=0$, every nonzero trace-zero element satisfies
$y^{p-1}=-1$. There are $p-1$ such elements and $h$ is odd,
so the sum is one. If $r=0,s\ne0$, the roots are those of
$F(Y)=Y^p+Y-s$, and

$$
\prod_{F(y)=0}(1-T/y)=1-T/s-T^p/s.
$$

Taking a formal logarithmic derivative through degree $h-1<p-1$
shows $\sum_y y^{-j}=s^{-j}$ for $1\le j\le h$.
Expanding $(s/y-1)^h$ then gives one. This agrees with $P_d(1)=1$.

For $r\ne0$, put $z=1+ry$ and $t=1+rs$. The condition is
$\operatorname N(z)=t$, with $z\ne1$.
When $t=0$, only $z=0$ contributes, with weight one.
When $t=1$, the allowed $z$'s are $\mu_{p+1}\setminus\{1\}$;
the weight is $(-1/z)^h$, whose sum is one.
These are exactly $P_d(-1)=P_d(1)=1$, since $d$ is even.

For $t\ne0,1$, the $p+1$ roots of $F(Z)=Z^{p+1}-t$ are all
allowed and

$$
y^{h(p-1)}
 =\left(\frac{t-z}{z(z-1)}\right)^h.
$$

The root sum equals minus the residue at $z=1$ of

$$
\left(\frac{t-z}{z(z-1)}\right)^h
 \frac{z^p}{z^{p+1}-t}\,dz.
$$

There is no residue at $0$, because $h<p$, and none at infinity.
Writing $z=1+u$, terms of degree at least $p$ cannot affect the
needed coefficient. As $h$ is odd, the result is

$$
[u^{h-1}](1-t+u)^{h-1}(1+u)^{-h}
 =\sum_{i=0}^{d}(-1)^i\binom di\binom{d+i}{i}(1-t)^i
 =P_d(2t-1).
$$

This proves (727.13), including all exceptional fibers.

## 4. Matrix coefficients: integrality without the old special lattice

Use the Mercuri–Schoof left-module model. The upper Borel acts by
affine permutations and

$$
we_r=-\frac1p\sum_{y\in\mathbf F_{p^2}^{\times}}
 \theta_h(y)e_{r\operatorname N(y)+\operatorname{Tr}(y)}.
\tag{727.14}
$$

This is the general primitive cuspidal model, not just its
$\theta_{\pm1}$ case. Its invariant Hermitian form is the same $G$:
the Borel representation on functions modulo constants is irreducible,
so its positive invariant form is unique up to scale; the normalization
$G(e_0,e_0)=p-1$ fixes it as in (727.2).
Using the dual convention for a right-slash action changes neither
a torus trace nor the matrix-coefficient formula below.

Pairing (727.14) with $e_s$ cancels the apparent denominator $p$:

$$
G(e_s,we_r)
 =-\sum_{r\operatorname N(y)+\operatorname{Tr}(y)=s}
       \overline{\theta_h(y)}.
\tag{727.15}
$$

Here the term involving $\sum_y\theta_h(y)$ is exactly zero.
Thus these matrix coefficients are integral even though the entire
old lattice need not be stable under $w$.

For $g=\left(\begin{smallmatrix}a&b\\c&d_0\end{smallmatrix}\right)$,
write $\Delta=ad_0-bc$. The Bruhat decomposition, followed by
(727.13), gives

$$
\boxed{
G(e_0,ge_0)\equiv-
 P_{h-1}\!\left(\frac{ad_0+bc}{\Delta}\right)\pmod p.
}
\tag{727.16}
$$

Indeed, if $c\ne0$, use

$$
g=u(a/c)\operatorname{diag}(\Delta/c^2,1)\,w\,u(d_0/c).
$$

The fiber parameters are $r=d_0/c$ and $s=-ac/\Delta$.
Their argument is $1+2rs=-(ad_0+bc)/\Delta$; the minus sign
disappears because $h-1$ is even.
If $c=0$, the vector is an affine translate of $e_0$;
its pairing is $-1$ modulo $p$, also the displayed formula.
The same decomposition proves integrality for all $g$.

Summing over the $p+1$ torus elements proves $N_h$ integral.
Its coefficients lie in the character field, unramified at $p$.
Moreover it is the cyclotomic conjugate of the original $N_1$;
R434/R588 prove $N_1\ne0$. Thus $N_h\ne0$, even when its
reduction vanishes.

## 5. The original $\zeta$-torus and its Legendre square

In the original period basis the CM torus in $\mathrm{PGL}_2(\mathbf F_p)$
is

$$
\mathsf T_\zeta=
\left\{
 \begin{pmatrix}a&-b\\b&a+b\end{pmatrix}:
 (a,b)\ne(0,0)
\right\}/\mathbf F_p^\times.
\tag{727.17}
$$

It fixes $\zeta$, since $\zeta^2+\zeta+1=0$.
For $b\ne0$, let $m=a/b$. Formula (727.16) has argument

$$
x_m=\frac{m^2+m-1}{m^2+m+1},
$$

and the element with $b=0$ has argument one.
Choose $s_0^2=-3$ and set

$$
t=m+\frac12,\qquad
q=\frac{t-s_0/2}{t+s_0/2}.
$$

Since $-3$ is a nonsquare modulo $p$, this is a bijection
$\mathbf P^1(\mathbf F_p)\to\mu_{p+1}$, with $m=\infty$
mapping to $q=1$. Direct substitution gives

$$
x_m=-\frac13+\frac43\frac{q+q^{-1}}2.
\tag{727.18}
$$

A Laurent polynomial of degree at most $h-1<p+1$ has its
$\mu_{p+1}$-sum equal to $p+1$ times its constant coefficient.
Modulo $p$, this factor is one. Hence

$$
N_h\equiv-
 \operatorname{CT}_q
 P_{h-1}\!\left(-\frac13+\frac43\frac{q+q^{-1}}2\right).
\tag{727.19}
$$

The polynomial form of the Legendre addition theorem is

$$
\operatorname{CT}_q
 P_d\!\left(x^2+(1-x^2)\frac{q+q^{-1}}2\right)=P_d(x)^2.
\tag{727.20}
$$

For real $x$ in an interval this follows by integrating the finite
addition formula over the angular variable; it then holds as a
polynomial identity. Its coefficients have only powers of two in their
denominators, so its reduction here is legitimate. Taking
$x=1/s_0$ in (727.20) proves (727.3).
The addition identity used is the integer-degree formula
[NIST DLMF 14.18.2](https://dlmf.nist.gov/14.18.E2); only its constant
angular coefficient is required.

The precise transport in R588 is compatible with this calculation.
There one chooses $L\equiv0\pmod p$, $L\equiv1\pmod{12}$, and

$$
\tau_*=\frac{-L+\sqrt{-3}}2
 =\zeta+k,\qquad k=(1-L)/2\in6\mathbf Z.
$$

Modulo $p$, $k=1/2$. This conjugates the torus to a trace-zero
torus and transports the split vector at the same time:
in the affine convention it becomes $e_k$.
The invariant pairing preserves
$G(e_0,\operatorname{Tr}_{\mathsf T_\zeta}e_0)$.
Replacing this transported $e_k$ by $e_0$ would instead produce
a central-binomial expression and would change the scalar.
No such replacement is made in (727.19).

Finally,

$$
P_6(X)=\frac{231X^6-315X^4+105X^2-5}{16},
\qquad
P_6(1/\sqrt{-3})=-47/9.
$$

This proves (727.9) exactly, without a finite-prime fit.

## 6. The two complete original Fourier tails for $h\ne1$

Use the original integral $\mu_{p^2-1}$-equivariant CM coordinate $Y$.
Let $e=p^2-1$, $\varpi=Y(P)$, and $T_0=\varpi^e$.
R710 proves

$$
T_0\in p\mathcal O_{K_0},\qquad T_0/p\equiv1\pmod p,
$$

over a finite unramified field $K_0$, and the fixed original
completed primitive satisfies the full R595 bounds.
The character $\theta_h$ selects

$$
a=h(p-1),\qquad b=(p+1-h)(p-1),\qquad a+b=e.
\tag{727.21}
$$

If $H_2=\sum A_jY^j$ and $H_3=\sum B_jY^j$, the exact sums are

$$
S_{2,h}=-e\varpi^a\sum_{j\ge0}A_{a+je}T_0^j,\qquad
S_{3,h}=-e\varpi^b\sum_{j\ge0}B_{b+je}T_0^j.
\tag{727.22}
$$

For both $a,b<e$, all coefficients in the first five selected
blocks use positive primitive exponents below $5p^2$.
By the actual exponent class $5\bmod6$, none has two uncancelled
powers of $p$ in its primitive denominator. Thus

$$
v_p(A_{a+je})\ge-2,\qquad
v_p(B_{b+je})\ge-3\qquad(0\le j\le4).
$$

This uses the complete decompositions of R595:
$H_2=B_0+ZB_1+Z^2B_2$, $Z=E-Y^{-1}$,
and the analogous integral polynomial in $Z$ for $H_3$.
The apparent pole terms cancel before the bound is applied.

For $j\ge5$, every positive primitive index is below
$(j+1)p^2$, giving the uniform bounds

$$
v_p(A_{a+je})\ge-4-2\lfloor\log_p(j+1)\rfloor,\qquad
v_p(B_{b+je})\ge-6-3\lfloor\log_p(j+1)\rfloor.
$$

After the factors $p^2T_0^j$ and $p^3T_0^j$, respectively,
the tails have valuation at least one, since

$$
j-2-2\lfloor\log_p(j+1)\rfloor\ge1,\qquad
j-3-3\lfloor\log_p(j+1)\rfloor\ge1
\quad(p\ge41,\ j\ge5).
$$

For logarithm floor zero this is immediate. For floor $r\ge1$,
use $j\ge p^r-1$; the resulting lower bounds increase with $r$.
The first four tail blocks also gain at least one power of $p$
from $T_0^j$. Therefore both normalized sums

$$
-\frac{p^2S_{2,h}}{eC_0\varpi^a},\qquad
-\frac{p^3S_{3,h}}{eC_0\varpi^b}
\tag{727.23}
$$

are integral, and their reductions are precisely
$p^2A_a/C_0$ and $p^3B_b/C_0$.
Every discarded block has been covered; there is no assumption that
the first reductions are nonzero.

## 7. Coefficient extraction and the original norm constant

R595's full rational kernels have top completed-primitive coefficients

$$
[ E^2]H_2=\frac{C_0}{4}D^2R,\qquad
[ E^3]H_3=\frac{C_0}{36}D^3R.
$$

In the required degrees, the actual Cartier identity is
$pE\equiv-BY^p\pmod p$.
The first selected degrees $a,b$ are below $p^2$.
Here the derivative and flat/integral-coordinate comparisons are in
the proved integral range, so reduction gives

$$
\frac{p^2A_a}{C_0}
 \equiv\frac{B^2}{4}(h-2)(h-1)\mathfrak r_{h-2},
\tag{727.24}
$$
$$
\frac{p^3B_b}{C_0}
 \equiv-\frac{B^3}{36}h(h+1)(h+2)\mathfrak r_{p-h-2}.
\tag{727.25}
$$

For example the first target exponent of $R$ is

$$
a-2p+2=(p-1)(h-2);
$$

the two derivative factors reduce to
$(2-h)(1-h)=(h-2)(h-1)$.
The second target exponent is

$$
b-3p+3=(p-1)(p-h-2),
$$

and its three derivative factors reduce to $(h+2)(h+1)h$.
This verifies the indices and signs directly in the original kernels.

Multiplying (727.23)–(727.25), and using
$e^2\equiv1$, $T_0/p\equiv1$, proves (727.5).
Then (727.12), with $C_0^2=15552/\alpha^2$, gives (727.6).
No local finite norm was set equal to $-1$.

The original R683 comparison is

$$
\mathfrak r_k=c(-3B)^{-(k-1)}C_k,\qquad
c=(3/p)\alpha^2/2,\qquad
2\le k\le p,\quad k\equiv2\pmod3.
\tag{727.26}
$$

Both $k=h-2$ and $k=p-h-2$ lie in this exact range.
All conversion factors and all five factors in $Q_h$ are units.
Thus, if $\nu_h=v_p(N_h)$, the full sums and exact norm imply

$$
v_p(M_{2,h})\ge-2+\nu_h/2,
$$

with equality if and only if
$C_{h-2}C_{p-h-2}\not\equiv0\pmod p$.
In particular (727.7) gives $v_p(M_{2,h})=-2$.
When (727.3) vanishes, $\nu_h\ge1$; that case has not been replaced
by a unit assertion.

## 8. A uniform one-$p$ Hodge denominator for arbitrary $h$

The old lattice
$\Lambda=\mathcal O^{\mathbf F_p}/\mathcal O\mathbf1$
need not be stable for $\theta_h$. We instead use the direct bound
visible in the Bruhat formula.

Every $g\in\mathrm{PGL}_2(\mathbf F_p)$ lies in $B$ or $BwB$.
Borel matrices permute the indicator classes, and the single Weyl
formula (727.14) has at most one factor $1/p$. Hence

$$
p\,g e_0\in\Lambda\qquad\text{for every }g.
$$

It follows, without multiplying two denominator bounds, that

$$
p\,g u_h=\frac1{p+1}\sum_{t\in\mathsf T_\zeta}p\,(gt)e_0
 \in\Lambda\qquad\text{for every }g.
\tag{727.27}
$$

Thus $p$ times the actual averaged vector is integral at every cusp.
The underlying normalized theta newform has algebraic-integral Fourier
coefficients and trivial $p$-Euler factor, so the relation
$e_r\mapsto\sum a_j\zeta_p^{-jr}Q^j$ is the same one as R592.
The displayed tame $S,T$ matrices are integral units and commute
with the $p$-factor. The all-cusp integral $q$-expansion principle
and the actual fine CM disc of R592 now apply to $p\mathcal F_h$.

None of this changes the normalization of $M_{m,h}$. It proves the
full bound, including every factorial,

$$
\boxed{
v_p\!\left(\frac{M_{m,h}}{m!}\right)
 \ge-1-m\sigma,\qquad \sigma=\frac p{p+1},\qquad m\ge0.
}
\tag{727.28}
$$

The same Gauss–Manin flat change and the same
$\lambda$-scaled fine parameter are used. This proof supplies the
one extra denominator rather than transferring R434's stronger
special-lattice theorem to $\theta_h$.

## 9. The same rational Abel line and the entire infinite tail

Assume (727.7). The actual real Hecke coefficient field is contained
in $\mathbf Q(\zeta_{p+1})^+$, so $p$ splits completely in it,
as in R711. The selected component differential is defined over
$\mathbf Q_p$. The same original quotient and the rational parameter
$s=a-1$ give a scalar Abel increment $J_h(s)\in s\mathbf Q_p[[s]]$.

The unchanged Hodge/flat comparison has one nonzero constant,
independent of the order of differentiation:

$$
J_h(s)=c_h\mathcal I_h(z_{\rm f}(s)),\qquad
\mathcal I_h(z_{\rm f})
 =\sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}z_{\rm f}^{3j}.
\tag{727.29}
$$

The full flat/coarse inverse belongs to $\mathbf Q_p[[z_{\rm f}^3]]$.
Therefore $c_hM_{3j-1,h}\in\mathbf Q_p$ for all $j$.
Since $M_{2,h}\ne0$, we may divide by that same nonzero jet, obtaining

$$
M_{3j-1,h}/M_{2,h}\in\mathbf Q_p.
\tag{727.30}
$$

As $v_p(M_{2,h})=-2$, every allowed jet now has an integer valuation.
This deduction uses the original quotient and one comparison scalar;
it does not assume an arbitrary CM value is unramified.

Put $V=z_{\rm f}^3/p^3$ and

$$
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!}.
$$

The complete Hodge bound (727.28) gives

$$
\boxed{
v_p(E_{j,h})\ge
 \frac{3j-1}{p+1}-v_p(3j).
}
\tag{727.31}
$$

If $p\nmid3j$, the right side is strictly positive.
If $a=v_p(3j)\ge1$, then $3j\ge3p^a$, and the lower bound is at least

$$
\frac{3p^a-1}{p+1}-a>1.
$$

For $a=1$, this is $2-4/(p+1)>1$, and it increases with $a$.
Since the actual valuations are integers, every $E_{j,h}$ has
valuation at least one. The bound also tends to infinity with $j$,
including all indices divisible by $p$.

Define the original first unit

$$
b_h=\frac{p^2M_{2,h}}6,\qquad v_p(b_h)=0.
$$

Equations (727.30)–(727.31) yield the full restricted series

$$
\boxed{
\mathcal G_h(V):=\frac{\mathcal I_h(z_{\rm f})}{p\,b_h}
 =V+\sum_{j\ge2}g_jV^j\in\mathbf Z_p\langle V\rangle.
}
\tag{727.32}
$$

Thus its linear term strictly dominates at every nonzero $V$ of
positive valuation. The only zero in $v_p(V)>0$ is the simple center.

The full original coarse change is still
$V=\Psi(s/p^3)$, with
$\Psi=(3/8)v+\sum_{r\ge2}\psi_rv^r$,
$\psi_r\in p\mathbf Z_p$, and $\Psi$ an integral analytic
automorphism. It depends on the elliptic deformation, not on $h$.
This proves (727.8) and the exact valuation

$$
v_p(\mathcal I_h(s))=v_p(s)-2\qquad
(0\ne s,\ v_p(s)>3).
\tag{727.33}
$$

On the closed candidate disc the stronger identity is

$$
\frac{\mathcal I_h(p^4u)}{p^2b_h}
 =\frac38u+pH_h(u),\qquad
H_h\in u^2\mathbf Z_p\langle u\rangle.
\tag{727.34}
$$

It is an analytic automorphism, and its unit linear term gives

$$
v_p\bigl(\mathcal I_h(s_1)-\mathcal I_h(s_2)\bigr)
 =v_p(s_1-s_2)-2\qquad(s_1,s_2\in p^4\mathcal O).
$$

For the actual component $J_h$, one adds $v_p(c_h)$ to this
difference valuation. The comparison constant remains nonzero;
it is not asserted to be a unit.

## 10. The concrete $h=7$ channel and the limit of the conclusion

For $h=7$, the fixed-CM pair in (727.7) is exactly

$$
(C_5,C_{p-9}),
$$

not $(C_p,C_{p-3})$. The first factor is the known unit $9/2$.
Formula (727.9) makes the remaining finite norm a unit whenever
$p\ne47$. Primitivity separately requires $7\nmid p+1$;
for example $p=41$ does not satisfy that requirement.
The prime $47$ does satisfy primitivity, but its finite norm has
positive valuation. These two restrictions are not conflated.

At $p=137147$, the preserved R710 certificate gives
$C_{p-9}\equiv122674\ne0$, and $7\nmid137148$.
Consequently the actual $h=7$ component satisfies
$v_p(M_{2,7})=-2$ and the complete unique-center statement
(727.8). This is a different coefficient embedding of the same
actual factor. The original $h=1$ result remains the independently
certified $v_p(M_2)=0$ of R722.

Any vanishing of the whole Abel increment would force vanishing of
each of its components, so one component satisfying (727.8) is enough
to rule out such a simultaneous return to the center. The actual
positive-rank rational-point problem does not assert that its Abel
increment must vanish. No height identity, rational-point exclusion,
or all-prime unit assertion follows from this observation.

The only new source beyond the already fixed interfaces is the general
finite cuspidal model of Mercuri–Schoof, §4 and Proposition 2.1:
[author offprint](https://reneschoof.github.io/mcom3503.pdf).
The fiber sums, scalar reduction, full Fourier tails, one-$p$
all-cusp bound and coefficient-dominance argument are proved above.
No new prime window or target computation was performed.
