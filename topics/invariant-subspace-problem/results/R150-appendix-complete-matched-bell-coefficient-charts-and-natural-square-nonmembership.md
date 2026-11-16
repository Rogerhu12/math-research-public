# R150 appendix — complete matched Bell coefficient charts and nonmembership of every natural square

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: **proved by the complete original formulas and the actual exact
computation identified in §7.** All six mean variables and all eleven
physical Hankel variables remain free. No fixed-mean result is used as
a full-parameter identity.

## 1. Statement and unchanged model

Let
$$
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix},\qquad
H=(H_{i+j})_{0\le i,j\le5}.
$$
Use the original polynomial
$$
R_3(y,H)=G_6(y,H)-\frac12\ell(y,H)^{\mathsf T}J_3^{-1}\ell(y,H)
$$
and its complete gradient ideal
$$
\mathcal J=(\partial_{H_0}R_3,\ldots,\partial_{H_{10}}R_3,
            \partial_{y_0}R_3,\ldots,\partial_{y_5}R_3)
        \subset\mathbb Q[y_0,\ldots,y_5,H_0,\ldots,H_{10}].
$$
Here the literal definitions of $G_6,\ell,J_3$ are those of the
[original Schur reduction](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md).
The source in this appendix reconstructs them from $K$; it does not
import a rank-one specialization.

Let
$$
f(d)=3725d^3-43931504d^2+6080833024d+52565262336,\qquad
E=\mathbb Q[d]/(f),
$$
and put
$$
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\qquad
r=(A,A+d,0,0,0,1)\in E^6.
$$
These are the unchanged three matched directions after taking the
three embeddings of $E$ into $\mathbb C$. Write the original reduced
Bell cubic as
$$
B_r=(r\cdot y)^3-6(r\cdot y)r^{\mathsf T}Hr
     -c(r)^{\mathsf T}J_3^{-1}\ell(y,H).
\tag{1.1}
$$

The following two conclusions hold.

1. There are six explicitly specified original Hankel coefficients
   $L_k(y)$, for $k=2,1,0,3,4,5$, forming an $E$-linear coordinate
   system on the six mean variables. Every point with $B_r\ne0$
   belongs to at least one of the six principal open sets $L_k(y)\ne0$.
   Each such chart permits exact elimination of $H_k$ from $B_r=1$,
   with only the parameter denominator $L_k(y)$.

2. For every matched embedding $\sigma:E\hookrightarrow\mathbb C$,
   $$
   \boxed{B_{\sigma(r)}^2\notin
           \mathcal J\,\mathbb C[y,H].}
   \tag{1.2}
   $$
   This excludes natural power two in the complete original gradient
   ideal, allowing source polynomials of arbitrary degree. It does
   not assert that a higher power is absent.

The second conclusion also applies to the original full Bell cubic
$S_{\sigma(r)}$ and the full thirty-three-variable gradient ideal,
by the exact triangular Schur ideal equivalence. Fixed nonzero
complex scalar factors from the original realification do not
change this conclusion.

## 2. Complete original polynomial verification

Set $p=Ky$, $F=\frac12y^{\mathsf T}Ky$ and
$$
b=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_2=\operatorname{tr}((KH)^2),\quad
\tau_3=\operatorname{tr}((KH)^3).
$$
The source uses
$$
G_6=F^3-6Fb+6F\tau_2+12c-8\tau_3,
$$
$$
\ell_m=[z^m]\left((p^{\mathsf T}v(z))^3
 -6(v(z)^{\mathsf T}KHKv(z))(p^{\mathsf T}v(z))\right),
\quad v(z)=(1,z,\ldots,z^5)^{\mathsf T}.
$$
It reconstructs all entries of
$$
(J_3)_{mn}=[z^m w^n](v(z)^{\mathsf T}Kv(w))^3
$$
and checks the actual integer determinant
$$
\det J_3=23366320238786911411830138211362846399922176000.
$$
Both inverse products are verified in all $512$ coordinates.

Differentiation is performed before any specialization of $y$ or
$H$. For an independent check, insert
$V=-\frac14J_3^{-1}\ell$ into the original contractions
$$
N_{ij}=Fy_i y_j-2FH_{i+j}
 -2\big(y_i(Hp)_j+(Hp)_i y_j\big)
 +4\sum_k V_{i+j+k}p_k+4(HKH)_{ij}
$$
and
$$
\Gamma_i=(F^2-2b+2\tau_2)y_i-4F(Hp)_i+8(HKHp)_i
 +4\sum_{j,k}V_{i+j+k}p_jp_k
 -8\sum_{j,k}V_{i+j+k}(KHK)_{jk}.
$$
Every polynomial coefficient of all seventeen identities
$$
\partial_{H_m}R_3=-6\sum_{i+j=m}(KNK)_{ij},
\qquad
\nabla_yR_3=3K\Gamma
\tag{2.1}
$$
is checked exactly over $\mathbb Q$.

The actual $R_3$ has $3124$ nonzero monomials. The complete
seventeen gradient term counts, in original $H$-then-$y$ order, are
$$
(309,343,372,375,379,379,379,375,372,343,309,
 1161,1202,1246,1246,1202,1161).
$$
The complete weighted Euler identity
$$
6R_3=\sum_{i=0}^5 y_i\partial_{y_i}R_3
      +2\sum_{m=0}^{10}H_m\partial_{H_m}R_3
$$
is also multiplied back. These are polynomial identities in all
seventeen original variables, not evaluations at selected means.

The field $E$ is independently certified: the degree-three integer
polynomial $f$ has nonzero leading coefficient modulo $109$ and no
root in $\mathbb F_{109}$. All $109$ evaluations are performed, and
their recorded hash is
~~~
a9a303089efe97a54f664a60ee2d4a650c2cf1b1860517f586d0d605b1d95ff4
~~~
Hence $f$ is irreducible over $\mathbb Q$. All inverses used in $E$,
including $160(5d-704)$, are verified by multiplication modulo $f$.

## 3. Six exact coefficient charts

Write
$$
B_r(y,H)=\beta_r(y)+\sum_{m=0}^{10}H_m L_m(y),\qquad
L_m(y)=\sum_{j=0}^5 L_{mj}y_j.
\tag{3.1}
$$
The source retains all three rational field components of (1.1),
each with $112$ nonzero monomials. It verifies that each
$\partial_{H_m}B_r$ is exactly linear in $y$, and that the remaining
$\beta_r$ is independent of $H$.

For a separate coefficient construction, put
$$
a_m=\sum_{i+j=m}r_i r_j,\qquad
w=J_3^{-1}c(r),
$$
and let $Q_m$ be the physical Hankel matrix whose $(a,b)$ entry is
$1$ if $a+b=m$ and $0$ otherwise. Define
$$
q_{m,k}=\sum_{i+j=k}(KQ_mK)_{ij}.
$$
Then the complete original coefficient formula is
$$
L_{mj}=6\left(
 \sum_{k=0}^{10}\sum_{i=0}^5 w_{k+i}q_{m,k}K_{ij}
 -a_mr_j\right).
\tag{3.2}
$$
All $66$ entries obtained from (3.2) equal the entries obtained
by differentiating (1.1).

The actual matrix $L\in E^{11\times6}$ has rank $6$.
In the ordered original rows
$$
\mathcal R=(2,1,0,3,4,5),
$$
the square matrix $L_{\mathcal R}$ is invertible. The exact inverse
is retained with the complete original model. Both products
$L_{\mathcal R}L_{\mathcal R}^{-1}$ and
$L_{\mathcal R}^{-1}L_{\mathcal R}$ are checked in all $72$ field
coordinates. In particular,
$$
(L_2,L_1,L_0,L_3,L_4,L_5)=(y_0,\ldots,y_5)
\quad\text{as ideals in }E[y,H].
\tag{3.3}
$$

Equation (1.1) vanishes identically at $y=0$. Consequently
$B_r\ne0$ implies $y\ne0$, and (3.3) gives the stated complete
six-open cover. The inverse matrix is over $E$, so every matched
embedding preserves its invertibility.

## 4. Exact saturation interface on the six charts

The original weights are
$$
\operatorname{wt}(y_i)=1,\qquad
\operatorname{wt}(H_m)=2,\qquad
\operatorname{wt}(B_r)=3.
$$
The critical equations are homogeneous of weights four and five.
Over an algebraic closure, a critical point with $B_r\ne0$ can be
rescaled to $B_r=1$: choose $\lambda$ with
$\lambda^3 B_r=1$, then replace $(y,H)$ by
$(\lambda y,\lambda^2H)$.

For each $k\in\mathcal R$, the chart ring has the explicit identity
$$
\frac{E[y,H,L_k^{-1}]}{(B_r-1)}
 \;\simeq\;
 E[y,H_0,\ldots,\widehat{H_k},\ldots,H_{10},L_k^{-1}],
$$
where the inverse substitution is
$$
H_k=\frac{1-\beta_r(y)-\sum_{m\ne k}H_mL_m(y)}{L_k(y)}.
\tag{4.1}
$$
Thus the Bell-nonzero critical question is precisely the six
original-gradient systems obtained by applying (4.1) to all
seventeen equations, with the indicated localization retained.
No critical equation is dropped, and no denominator depending
on an unsolved Hankel coordinate is introduced.

This is a complete reduction of that question, not a claim that
any of these six saturated ideals has yet been proved to be the
unit ideal. One matched field with all its embeddings handles
each of the original three Bell directions. Saturating by the
product of the three Bell values would instead test only the
locus where all three are nonzero, so that replacement is not
made.

The already proved
[essential-dimension classification](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)
shows that any point remaining in these six systems has
$\dim\operatorname{ess}(T_3)\ge4$.

## 5. The complete weighted-six source space

Because the original weights are strictly positive,
the weight-six component of $\mathcal J$ is spanned by exactly
$$
\{\,m\,\partial_{H_j}R_3:
 0\le j\le10,\ \operatorname{wt}(m)=2\,\}
\;\cup\;
\{\,y_i\,\partial_{y_j}R_3:0\le i,j\le5\,\}.
\tag{5.1}
$$
There are $21$ quadratic mean monomials and $11$ Hankel
variables of weight two. Hence (5.1) has
$$
11(21+11)+6\cdot6=388
$$
original source columns.

All weight-six output monomials are retained. Their number is
$$
\binom{11}{5}
+11\binom95
+\binom{12}{2}\binom75
+\binom{13}{3}
=462+1386+1386+286=3520.
\tag{5.2}
$$
The four summands correspond respectively to
$y^6$, $y^4H$, $y^2H^2$, and $H^3$.

Expand the exact field-valued natural square as
$$
B_r^2=b_0+d\,b_1+d^2b_2,\qquad b_i\in\mathbb Q[y,H]_6.
\tag{5.3}
$$
The complete matrix of (5.1) is $M\in\mathbb Q^{3520\times388}$;
the three columns of (5.3) form $T\in\mathbb Q^{3520\times3}$.
The source constructs every column from the verified original
polynomials. All their rational denominators are checked to be
units at $127$.

The actual ranks are
$$
\operatorname{rank}_{\mathbb F_{127}}\overline M=388,
\qquad
\operatorname{rank}_{\mathbb F_{127}}
 [\,\overline M\mid\overline T\,]=391.
\tag{5.4}
$$
These ranks are the full column counts. Nonzero minors in
(5.4) therefore give
$$
\operatorname{rank}_{\mathbb Q}M=388,\qquad
\operatorname{rank}_{\mathbb Q}[\,M\mid T\,]=391.
\tag{5.5}
$$
There is no assumption about good reduction of a cokernel:
(5.5) uses only nonzero specialized minors and the elementary
column-count upper bounds.

In particular the three classes of $b_0,b_1,b_2$ are linearly
independent in $\mathbb Q[y,H]_6/\mathcal J_6$.

## 6. Why this proves full natural-square nonmembership

For any embedding $\sigma:E\hookrightarrow\mathbb C$, tensoring
(5.5) with $\mathbb C$ preserves independence of the three
classes. Their combination
$$
[b_0]+\sigma(d)[b_1]+\sigma(d)^2[b_2]
$$
cannot vanish, because its first coefficient is $1$. This is
the class of $B_{\sigma(r)}^2$, proving (1.2).

No higher-weight source can evade this obstruction. If an
arbitrary polynomial identity expressed the weight-six polynomial
$B_{\sigma(r)}^2$ in the homogeneous gradient ideal, taking its
weight-six component would express it in precisely (5.1), which
(5.5) excludes.

The original Schur coordinate change gives
$$
(\nabla\mathcal Q_3)=(Z,\nabla R_3),\qquad
S_r=B_r+4c(r)^{\mathsf T}Z.
$$
Reducing modulo $Z$ shows that
$S_{\sigma(r)}^2\in(\nabla\mathcal Q_3)$ would imply (1.2)'s
negation. Thus the same negative result holds for every full
matched Bell natural square.

This does not conflict with the rank-one
[Bell eighth-power theorem](R150-appendix-all-high-normal-source-cost8391-and-rank-one-bell-eighth-powers.md).
That theorem is on the stated rank-one pullback; the present
calculation uses all seventeen original low variables. It also
does not disprove radical membership: a successful full
Jacobian natural-power certificate, if one exists, must have
exponent at least three.

## 7. Reproduction and actual execution identity

The executable source is
[the full-parameter matched Bell driver](../notes/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py).
Its complete SHA-1 blob is
~~~
7e5244c7c9177d483bb2dbe2a1dc7a2dc86904a3
~~~
and its $16964$ bytes have SHA-256
~~~
31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10
~~~

The [frozen parameters](../notes/2026-11-16-r150-original-matched-bell-full-parameter-inputs-789f.json)
specify Python $3.12.14$, python-flint $0.9.0$, the literal matched
cubic, prime $127$, and a $180$-second/$2048$-MiB bound.
The [local execution manifest](../notes/r150-nonrankone-execution-789f/20261116-local-matched-bell-full-parameter-charts.json)
records the actual local tool identity and all output hashes.
No Actions run is invented for this local calculation.

Actual completion was at $2026$-$11$-$16$ $04{:}34{:}19.248237$
UTC. Elapsed time was $4.414020731004712$ seconds, exit code zero.
The semantic binding is
~~~
ba1bdf0ccf6937579f2b38b51b0d19e8cfad0cfb2b25e152c3a62befbde87b9c
~~~
The original $2789$-byte receipt has SHA-256
~~~
c37ab21681d4cb77a272aee345bbd36174cc0adea217c33a9c9ec100ce495ef2
~~~
The complete temporary model has $1850453$ canonical logical
bytes and logical SHA-256
~~~
adab3268447f90c430c9d219fc988ddc8e54cb5f8697dd05fe6599a61166908d
~~~
Its $504873$-byte gzip SHA-256 is
~~~
7fe125c8cc6019c5e7c756cac3fb9265b9fcf817b1d2acea3f7580c2c5b024dc
~~~

The weighted-six source and output dictionary hashes are,
respectively,
~~~
b6b6ab7b9a39cdd59e5891a20c2b71bc372010bbe168f4bd41143e38c6506e28
3adc598e09fffaeb80865b1c08c2f55a14e512b142dbb712c5f75ab7d947eedc
~~~
The original column-major field matrix and the three target
column hashes are
~~~
431e2eef6bb7f34096e8630735138a87fa9f32596f816b43818c59e813fb1f73
011fe6453fa806949452c3008dd910609fcc0c1f877cc8e7a948c41f2d99f315
~~~

The first independent v1 attempt stopped after $0.4212$ seconds
at JSON serialization of FLINT exponent integers. The v2 source
only converts those exact exponent integers to Python integers
during serialization, and uses an independent path, format,
binding, and output directory. The failed receipt is preserved
as such in the execution identity; it is not relabeled as a
successful run.

Only source code, parameters, execution identity, hashes, and
this proof belong in the repository. The complete polynomial
model and matrix arrays remain temporary. No full non-rank-one
Bell radical conclusion is asserted by this appendix.
