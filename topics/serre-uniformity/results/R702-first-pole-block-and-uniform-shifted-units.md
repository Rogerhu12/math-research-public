# R702 — The original sigma first pole block and uniform shifted units

## Statement

Let $p\ge41$ be prime, $p\equiv5\pmod6$, and use the original
$E_0:y^2=x^3-1$, $dz=dx/(2y)$, sigma function and arithmetic roots
$A_k$ of R697.  Put

$$
p=6N+5,\qquad \ell_2=(2/p),\qquad
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times.
\tag{702.1}
$$

Then for every integer $t$ with $2\le t\le p-1$ and
$t\equiv2\pmod3$,

$$
\boxed{A_{p+t+1}\equiv3\ell_2 B\,tA_t\pmod p.}
\tag{702.2}
$$

In particular the two actual fixed-character central-value roots at the
shifted weights satisfy, uniformly for all these primes,

$$
\boxed{A_{p+3}\equiv6\ell_2 B,\qquad
A_{p+6}\equiv90\ell_2 B\pmod p.}
\tag{702.3}
$$

Both are units.  With the unchanged R615/R697 normalization this gives

$$
\boxed{v_p(C_{p+3})=v_p(C_{p+6})=-1,\qquad
pC_{p+3}\equiv9B^2,\quad
pC_{p+6}\equiv-\frac{405}{2}B^2\pmod p.}
\tag{702.4}
$$

These are the weights $p+3,p+6$, not the two original target weights
$p,p-3$.  The result makes no assertion that $A_p$ or $A_{p-3}$ is a
unit, and it supplies no unproved identification with later Abel
coordinates $u_m$.

## 1. Exact residue of the first pole block

Retain the rational series $C,Z,H,T$ of R698:

$$
c_j=\binom{2j}{j}/4^j,\quad Z=\sum_{j\ge0}\frac{c_j}{6j+1}w^j,
\quad h_j=\prod_{a=1}^j\frac{6a-4}{6a-1},
\quad T=\exp\sum_{j\ge1}\frac{h_j}{j}w^j.
\tag{702.5}
$$

All assertions in this proof are in finite truncations.  Set $M=2N+2$.
For $j<M$, one has $j<p$.  The coefficients of $C,Z$ through this
range are $p$-integral.  For $Z$, the possible denominators $6j+1$
are at most $2p-3$; neither $p$ nor $2p$ is $1$ modulo $6$.
The denominator factors in $h_j$ are at most $2p-5$, and the only
one divisible by $p$ is $6(N+1)-1=p$.  Consequently

$$
h_j\in\mathbf Z_p\quad(j\le N),\qquad
ph_j\in\mathbf Z_p\quad(N+1\le j<M).
\tag{702.6}
$$

In $\mathbf F_p$, $1/3=2N+2$ and $5/6=-N$, so

$$
h_N\equiv\frac{(2N+2)_N}{(-N)_N}
=(-1)^N\frac{(3N+1)!}{(2N+1)!N!}.
\tag{702.7}
$$

Dividing (702.1) by this unit gives
$B/h_N=-(3N+2)/(N+1)=3$ modulo $p$.  Thus

$$
h_N\equiv B/3,\qquad ph_{N+1}\equiv-B.
\tag{702.8}
$$

For $0\le j\le N$, the remaining factors in the recurrence give

$$
\boxed{ph_{N+1+j}\equiv
-B\prod_{a=1}^j\frac{6a-3}{6a}
=-B c_j\pmod p.}
\tag{702.9}
$$

Since $N+1+j\equiv(6j+1)/6\pmod p$, this becomes

$$
p\frac{h_{N+1+j}}{N+1+j}
\equiv-6B\frac{c_j}{6j+1}\pmod p.
\tag{702.10}
$$

Define the integral auxiliary series

$$
T_0(w)=\exp\left(\sum_{j=1}^N\frac{h_j}{j}w^j\right)
\pmod{w^M}.
\tag{702.11}
$$

It is integral through degree $M-1$, because every factorial needed
in this truncated exponential has index $<p$.  The complementary
part of $\log T$ begins in degree $N+1$; its square begins in degree
$M$ and is absent in this truncation.  Therefore (702.10) proves

$$
\boxed{pT(w)\equiv-6B\,w^{N+1}Z(w)T_0(w)
\pmod{p,w^M}.}
\tag{702.12}
$$

This congruence is between integral finite series: the left side is
integral by the preceding one-pole argument.  No infinite sigma or
logarithm series has been reduced modulo $p$.

## 2. Transport to the original ordinary coordinate

As in R698, use $u=x^{-1/2}$ and $z=uZ(u^6)$.  Define the two
original sections

$$
F(z)=x(z)\sigma(z)^6=u^4T(u^6),\qquad
G(z)=-x(z)y(z)\sigma(z)^6=uT(u^6)\sqrt{1-u^6}.
\tag{702.13}
$$

Let $F_0,G_0$ be the expressions on the right with $T_0$ in place of
$T$.  The inverse coordinate $u(z)$ is $p$-integral to every degree
needed below, since $Z$ is integral in the stated finite range and its
constant coefficient is $1$.  In characteristic $p$,

$$
u(z)^p\equiv z^p\pmod{z^{2p}},
\tag{702.14}
$$

because $u(z)=z+O(z^7)$ and Frobenius sends the next possible term to
degree $7p$.  Substituting (702.12), and using
$u^{p+1}Z(u^6)=u^p z$, yields

$$
\boxed{pF(z)\equiv-6Bz^{p+1}F_0(z),\qquad
pG(z)\equiv-6Bz^{p+1}G_0(z)\pmod{p,z^{2p}}.}
\tag{702.15}
$$

The discarded $w^M$ terms first have $u$-degree at least $2p+3$
after multiplication by the smallest prefactor $u$; thus they do
not enter (702.15).  Moreover $F-F_0$ begins at degree $p+5$ and
$G-G_0$ at degree $p+2$.  In particular their coefficients of every
degree $\le p-2$ agree and are integral.

Write $f_n=F^{(n)}(0)$ and $g_n=G^{(n)}(0)$ for **ordinary**
derivatives.  For $1\le t\le p-1$, the factorial $(p+t)!$ contains
exactly one factor $p$, and

$$
\frac{(p+t)!}{p}\equiv-t!\pmod p.
\tag{702.16}
$$

Extracting the coefficient of degree $p+t$ in (702.15) and then
multiplying by this unit gives

$$
\boxed{f_{p+t}\equiv6Bt f_{t-1},\qquad
g_{p+t}\equiv6Bt g_{t-1}\pmod p.}
\tag{702.17}
$$

The factor $t$ is essential: it comes from
$t!/(t-1)!$.  In particular (702.17) is not a statement obtained by
replacing ordinary derivatives with divided powers.

## 3. Arithmetic-root normalization

When $t\equiv2\pmod6$, both $t-1$ and $p+t$ belong to the $G$
subsequence in R697.  When $t\equiv5\pmod6$, both belong to the
$F$ subsequence.  In each case the ratio of the two power-of-two
normalizations is

$$
2^{-(p+1)/2}\equiv\ell_2/2\pmod p.
\tag{702.18}
$$

Multiplying (702.17) by this ratio proves (702.2).  Since the exact
initial values are $A_2=1$ and $A_5=6$, (702.3) follows.  All factors
are units for $p\ge41$.

For $k=p+3$, R697 gives
$-2(p+2)!C_{p+3}=A_{p+3}^2$.  Since $(p+2)!/p\equiv-2$,
one gets $pC_{p+3}\equiv9B^2$.  For $k=p+6$, the identity is
$(p+5)!C_{p+6}/3=A_{p+6}^2$; now $(p+5)!/p\equiv-120$,
giving $pC_{p+6}\equiv-(405/2)B^2$.  These residues are nonzero,
which also proves both exact valuations in (702.4).

## 4. Scope and the boundary relevant to the original problem

The theorem identifies a complete first pole block of the original
sigma-six sections and proves actual all-prime units in two later
weights of the same fixed tame-character family.  It does not infer
anything from positivity of complex $L$-values or from a finite prime
window.

For $A_p$ and $A_{p-3}$, writing $k=p+t+1$ would give respectively
$t=-1$ and $t=-4$.  The coefficient extraction and the factorial
argument above require positive $t$, and there is no legitimate
backward extension across this boundary.  These lower-weight values are outside this theorem; no all-prime
unit assertion for the original two weights follows.  Relating the
proved shifted units to later coefficients of the actual Abel map
requires its original coordinate and Hodge-basis comparison; it
cannot be read off from the weight indices alone.

## 5. Independent finite normalization checks

[`R702_verify_ordinary_shift.py`](../scripts/R702_verify_ordinary_shift.py) evaluates the original six-isogeny
ordinary Bell derivative system of R697 through order $2p-1$.  It
checks (702.2) for every allowed $t$ at each supplied prime, including
the Pascal coefficients across order $p$, with no factorial division.
The two small certificates have the following distinguished values.

| $p$ | $A_{p+3}$ | $A_{p+6}$ | $pC_{p+3}$ | $pC_{p+6}$ |
|---:|---:|---:|---:|---:|
| 41 | 25 | 6 | 23 | 36 |
| 47 | 13 | 7 | 7 | 7 |

The complete checks and executable SHA256 are in
[`R702-prime41.json`](../notes/R702-prime41.json) and [`R702-prime47.json`](../notes/R702-prime47.json).  They verify the
normalization independently; sections 1--3 prove the congruence for
all primes in the stated range.

## Dependencies

- R697: exact original sigma-six arithmetic roots and $C_k$
  normalization for both weight classes.
- R698: the original algebraic coordinate and the rational series
  $C,Z,H,T$.
- Elementary finite-series algebra and Wilson's theorem.  No new
  analytic nonvanishing theorem is assumed.


本仓库直接依赖：[R697](R697-original-sigma-six-sections-and-integral-square-roots.md)、[R698](R698-two-actual-square-roots-at-one-low-degree.md)。
