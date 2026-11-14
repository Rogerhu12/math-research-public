# R150 appendix — the entire zero-A section for a rank-one mean has zero third tensor

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, including all exceptional complex mean points.

## 1. Statement

Use the original centered reduction
$$
y=a\,v(s),\quad a\ne0,\qquad
M=H-\frac12y^2,\qquad
V=\frac32L_y(M)+\frac12y^3,
$$
$$
T_3=6(L_y(M)-yM),\qquad
A_yM=(L_y(M))_{Ky}.
$$
The displayed formula for $V$ is the unique complete highest
solution. The original second-gradient equation is
$$
v(z)^{\mathsf T}K\bigl(4MKM+6A_yM\bigr)Kv(z)\equiv0.
\tag{1.1}
$$

**Theorem.** For any nonzero physical mean, the highest and
second-gradient equations, together with $A_yM=0$, force
$$
\boxed{T_3=0.}
\tag{1.2}
$$

Thus the complete critical points with $A_yM=0$ are precisely
the already classified rank-one-mean zero-third-tensor families:
a single physical support, with a genuine tangent coefficient
allowed only at $s=0,2,-6,\infty$.
In particular all their matched Bell values vanish.

Two further consequences are:

- Every rank-one-mean complete critical point with $MKM=0$
  has $T_3=0$.
- There are no rank-one-mean complete critical points with
  essential cubic dimension exactly three.

The proof uses complete polynomial coprimality certificates
at the exceptional means. It is not an enumeration of points
over a finite field.

## 2. Generic means and the exact remaining kernel

Weighted scaling reduces $a$ to one.
The
[exact-rank theorem for $A_y$](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)
proves that its kernel is the tangent quadratic space except
at
$$
\mathcal S=\{0,2,-6,\infty\}\cup
\{s:P_+(s)P_-(s)E_8(s)=0\}.
$$
At each exceptional mean the kernel has dimension exactly three.

For a nonexceptional mean, $A_yM=0$ already implies
$L_y(M)=yM$, hence $T_3=0$.
It remains to treat the three-dimensional kernels at
every point of $\mathcal S$.

In a finite source chart define the polynomial translation
matrix on the eleven quadratic Hankel coefficients by
$$
T(s)_{nj}=
\begin{cases}
\binom nj s^{n-j},&j\le n,\\
0,&j>n,
\end{cases}
\qquad 0\le n,j\le10.
\tag{2.1}
$$
It sends moments about the translated coordinate $z-s$ to
the original moments.
Its first two columns are the two tangent quadratic sequences:
$$
(t_0)_n=s^n,\qquad (t_1)_n=n s^{n-1}.
$$
Their tensor representatives are
$v(s)^2$ and $v(s)v'(s)^{\mathsf T}+v'(s)v(s)^{\mathsf T}$.

Put
$$
\mathcal A(s)=B_s^{\mathsf T}J_3^{-1}B_sJ_2T(s)
$$
and let $S(s)$ be its submatrix with rows $0,\ldots,7$
and columns $2,\ldots,10$.
This is an eight by nine polynomial matrix with rational
coefficients.
Its only constant denominators divide powers of $\det J_3$.

For $0\le j\le8$, set
$$
u_{j+2}(s)=(-1)^j\det S(s)_{\widehat j},\qquad
u_0=u_1=0,
$$
where the hat deletes column $j$ of this eight by nine matrix.
In particular
$$
u_{10}(s)=\Delta(s)
=\det\mathcal A(s)_{\{0,\ldots,7\},\{2,\ldots,9\}}.
\tag{2.2}
$$
Let $M_*(s)$ be the Hankel tensor whose coefficient sequence
is $T(s)u(s)$.

The certificates below prove that $\Delta(s)$ is nonzero
at every finite exceptional mean.
Consequently the selected eight rows are independent there.
Since the full operator has rank eight by the exact-rank theorem,
the cofactor vector belongs to its full kernel.
It is independent of the first two tangent columns because
$u_{10}=\Delta\ne0$.
Therefore every kernel vector has the unique form
$$
M=eM_*+ct_0+dt_1.
\tag{2.3}
$$
At infinity the identical construction is made in reversed
coordinates, using the original matrix with its rows and
columns reversed and the local source equal to zero.

## 3. The remaining second equation is a four-column system

For symmetric tensors $X,Y$ define the eleven-vector
$$
\mathscr P(X,Y)_m
=[z^m]\,v(z)^{\mathsf T}KXKYKv(z),\qquad 0\le m\le10.
$$
It is bilinear, and $\mathscr P(X,X)$ is the physical polar
coefficient vector of $XKX$.

On $A_yM=0$, equation (1.1) is exactly
$\mathscr P(M,M)=0$.
Using (2.3), it becomes
$$
e^2C_0+ecC_1+edC_2+d^2C_3=0,
\tag{3.1}
$$
where
$$
\begin{aligned}
C_0&=\mathscr P(M_*,M_*),\\
C_1&=\mathscr P(t_0,M_*)+\mathscr P(M_*,t_0),\\
C_2&=\mathscr P(t_1,M_*)+\mathscr P(M_*,t_1),\\
C_3&=\mathscr P(t_1,t_1).
\end{aligned}
\tag{3.2}
$$
There are no $c^2$ or $cd$ terms, because
$K(v(s),v(s))=K(v(s),v'(s))=0$.

At a root of $P_+$, $P_-$ or $E_8$, the four columns in
(3.2) are linearly independent.
At $s=0,2,-6,\infty$, the column $C_3$ is zero and the first
three columns are linearly independent.
The exact determinant certificates proving these assertions
are given next.

Thus (3.1) forces $e^2=0$ in every exceptional case.
Over $\mathbb C$ this gives $e=0$.
The tensor $M$ is then tangent quadratic, and the fixed-mean
highest map has exactly that kernel.
Hence $T_3=0$, proving the theorem.

## 4. Compact exact determinant certificates

All coefficient lists below are ascending in $s$ and are
computed modulo $103$.
The source polynomials are the integer representatives
$$
F_+=5P_+=5s^3-25s^2+32s-8,\qquad
F_-=5P_-=5s^3+135s^2+864s+864,
$$
and $E_8$ as in the exact-rank theorem.
For the individual means use $F=s$, $s-2$ or $s+6$.
Infinity uses the reversed-coordinate matrix and $F=s$.

Let $\eta$ be the following determinant of the original
cofactor columns (3.2):

| Source class | Rows of $(C_0,C_1,C_2,C_3)$ | Columns used |
|---|---|---|
| $F_+$, $F_-$, $E_8$ | $0,1,2,3$ | $0,1,2,3$ |
| $s=0$ | $0,6,5$ | $0,1,2$ |
| $s=2$ or $-6$ | $0,1,2$ | $0,1,2$ |
| $s=\infty$ in the reciprocal chart | $0,6,5$ | $0,1,2$ |

The following residues satisfy
$$
\Delta D\equiv1\pmod{103,F},\qquad
\eta E\equiv1\pmod{103,F}.
\tag{4.1}
$$

| $F$ | $\Delta\bmod(103,F)$ | $D$ |
|---|---|---|
| $F_+$ | $(16,18,94)$ | $(74,11,90)$ |
| $F_-$ | $(68,78,100)$ | $(61,6,82)$ |
| $E_8$ | $(22,46,91,50,44,25,27,59)$ | $(100,81,40,77,24,86,31,54)$ |
| $s$ | $(94)$ | $(80)$ |
| $s-2$ | $(99)$ | $(77)$ |
| $s+6$ | $(102)$ | $(102)$ |
| reciprocal $s$ | $(80)$ | $(94)$ |

| $F$ | $\eta\bmod(103,F)$ | $E$ |
|---|---|---|
| $F_+$ | $(102,5,96)$ | $(25,36,52)$ |
| $F_-$ | $(53,9,19)$ | $(89,53,51)$ |
| $E_8$ | $(14,54,41,37,41,14,5,69)$ | $(86,43,55,9,4,83,102,48)$ |
| $s$ | $(84)$ | $(65)$ |
| $s-2$ | $(15)$ | $(55)$ |
| $s+6$ | $(63)$ | $(18)$ |
| reciprocal $s$ | $(75)$ | $(11)$ |

The executable reconstructs $J_2,J_3$ directly by convolving the
unchanged original integer $K$.
It obtains $\det J_3\equiv75\pmod{103}$, so reduction of every
rational coefficient in the cofactor construction is valid.

For an economical calculation of $\eta$, solve the eight
selected rows with the translated coefficient $u_{10}$ normalized
to one. If $\rho$ is the corresponding second-gradient minor,
Cramer's rule gives exactly
$$
\eta=\Delta^4\rho.
\tag{4.2}
$$
Indeed the first column is quadratic in $M_*$, the next two
are linear, and the fourth is independent of it.
The same exponent four applies to the three-column minors.
The executable verifies the reductions of the cofactor
determinants through (4.2), as well as all eleven kernel rows,
every entry in (4.1), and the zero column $C_3$ in the four
self-contact cases.

Here is why these computations prove the characteristic-zero
claims. Clear denominators using a power of the nonzero integer
$\det J_3$, which is a unit modulo $103$.
Each displayed source polynomial is primitive and its leading
coefficient is a unit modulo $103$.
If it had a nonconstant common factor over $\mathbb Q$ with
either cleared determinant, Gauss's lemma would give a
primitive integer common factor whose positive degree is
preserved modulo $103$.
That would contradict the corresponding unit identity (4.1).
Thus the two determinants have no zero at any complex root
of the source polynomial.

This argument controls the whole algebraic source classes,
including the roots of $E_8$ and $P_-$ which are not visible
as source points over the prime field itself.

## 5. Complete critical classification on this section

Once $T_3=0$, the
[original zero-third-moment classification](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)
gives exactly
$$
\begin{aligned}
y&=a u,\\
H&=c\,u^2+d(uu_1^{\mathsf T}+u_1u^{\mathsf T}),\\
V&=\frac{6ac-a^3}{4}u^3+
ad\,(u\otimes u\otimes u_1+
u\otimes u_1\otimes u+
u_1\otimes u\otimes u),
\end{aligned}
\tag{5.1}
$$
with
$$
d=0\quad\text{or}\quad s\in\{0,2,-6,\infty\}.
$$
These are full critical points, not just highest solutions.
Their complete mean gradients vanish because their cumulants
are supported on an isotropic line or one of the four
isotropic tangent planes.
Conversely their centered $M$ lies in the kernel of $L_y-y(\cdot)$,
hence in $\ker A_y$.

If a rank-one-mean complete critical point has $MKM=0$,
(1.1) and invertibility of $J_2$ force $A_yM=0$.
The theorem therefore gives $T_3=0$ in that whole section,
including all exceptional means.

Finally suppose a rank-one-mean critical point had
$\dim\operatorname{ess}(T_3)=3$.
The
[complete rank-one essential-three classification](R150-appendix-rank-one-mean-essential-three-complete-critical-classification.md)
would place $y,H,V$ on a physical totally isotropic $W_\pm$.
Its centered $M$ is supported there too, so $MKM=0$.
The previous paragraph would give $T_3=0$, a contradiction.
This proves the stated empty essential-three stratum; it
refines the earlier necessary and sufficient support criterion.

## 6. Reproducible record and remaining branch

Author files:

- [exact polynomial determinant verifier](../notes/2026-11-14-rank-one-zero-A-section-verify.js);
- [execution record and all seven certificates](../notes/2026-11-14-rank-one-zero-A-section-verification.json).

All seven polynomial-quotient calculations passed in code mode.
They are algebraic unit certificates with a written
characteristic-zero lift, rather than finite-field point counts.

A rank-one-mean complete critical point with nonzero $T_3$
must now satisfy all of
$$
\dim\operatorname{ess}(T_3)\ge4,\qquad
A_yM\ne0,\qquad MKM\ne0.
$$
The remaining centered seventeen-equation problem has not
been replaced by these necessary conditions.
No new natural Jacobian power or original operator conclusion
is asserted.
