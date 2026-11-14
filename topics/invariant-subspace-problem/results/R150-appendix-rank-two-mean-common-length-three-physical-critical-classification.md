# R150 appendix — rank-two means on a common physical divisor of length three

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved** for the original complete six-mode cubic critical system.

## 1. Statement and conventions

Retain the original nondegenerate matrix $K$, the rational normal quintic
$v$, the physical Hankel tensors $y,H,V$, and
$
T_3=y^3-6yH+4V.
$
Suppose the three tensors have a common physical jet divisor $C$ of
length three, the mean has catalecticant rank two, and the essential
support of $T_3$ has dimension three. Then
$
\nabla\mathcal Q_3=0
\quad\Longrightarrow\quad
C\text{ consists of three different points and }E_C=W_+\text{ or }W_-.
\tag{1.1}
$
Consequently the full critical criterion is $Q_\pm\mid T_3|_{W_\pm}$;
the three original matched first Bell values vanish.

All coefficients are complex. The result includes zero coefficients
of $H,V$, every nonreduced divisor, and the physical point at infinity.
It makes no assertion about a common space of dimension four, about
a common three-dimensional space not yet identified as physical, or
about global natural powers of the Jacobian ideal.

A rank-two mean has a unique exact divisor $D$ of length two.
Since $y\in E_C$, independence of any physical jets of total length
at most six gives $D\le C$. Indeed $D\vee C$ has length at most
five, and its independent jets give $E_D\cap E_C=E_{D\wedge C}$.
Thus the cases below exhaust the possible means.

The original kernel facts used here have complete proofs in
[the three-point appendix](R150-appendix-three-distinct-physical-support-complete-critical-classification.md), §§2–3,
and [the contact appendix](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md), §1.
In particular
$
k(s,z)=-(s-z)^2q(s,z),\qquad
q(s,s)=-s^2(s-2)(s+6).
$
There is no nonzero pure-cube cubic polar $q(s,\cdot)$, and the
bicubic $q$ has no singular point off the diagonal. The orders of
the value, first derivative and second derivative polars at their
physical point are respectively
$
(2,1,0),\quad(3,2,1),\quad(4,3,2),
\tag{1.2}
$
for a generic point, $2,-6$, and $0,\infty$.
Rescaling a jet or adding a lower jet does not change these statements.

## 2. Three different support points

Let $u_i=v(s_i)$ be independent physical representatives and write
$
y=\sum a_i u_i,\qquad H=\sum h_i u_i^2,\qquad V=\sum v_i u_i^3.
$
Exactly two $a_i$ are nonzero. Put
$
b_i=a_i^2-2h_i,\qquad c_i=a_i^3-6a_i h_i+4v_i,\qquad
p_i=u_i^{\mathsf T}Kv.
$
The ordinary moments in different node variables multiply, and
$
T_3=\sum c_iX_i^3+
3\sum_{i\ne j}b_i a_jX_i^2X_j
\tag{2.1}
$
because $a_1a_2a_3=0$.

We prove that all three off-diagonal pairings are zero.

### 2.1 All three pairings nonzero

Scale the three representatives so that each pairing is one, and
label the missing mean coefficient $a_3=0$, $a_1a_2\ne0$.
The nine node derivatives of the original complete objective give,
for every permutation $\{i,j,k\}=\{1,2,3\}$,
$
c_jb_k+c_kb_j=0,\qquad
c_ja_k+c_ka_j+2b_jb_k=0,\qquad
c_j+c_k+3(b_ja_k+b_ka_j)=0.
\tag{2.2}
$
They follow by differentiating the exact ordinary-moment polynomial
displayed in §4 of the three-point appendix; no nonzero assumption
on the missing $a_3$ is used in their derivation.

If $b_3\ne0$, the middle equations first give
$
b_1=t a_1,\quad b_2=t a_2,\quad c_3=-2tb_3.
$
The first equations then give $c_1=2t^2a_1,c_2=2t^2a_2$.
Their remaining member is $4t^3a_1a_2=0$, so $t=0$.
The last equations would now give $3b_3a_1=0$, a contradiction.

If $b_3=0$, (2.2) gives $c_3=c_1=c_2=0$, followed by
$b_1b_2=0$ and $b_1a_2+b_2a_1=0$. Hence $b_1=b_2=0$.
Equation (2.1) is then zero, contrary to essential dimension three.

### 2.2 Exactly one pairing zero

This case is excluded by the pure geometric argument in §5 of the
three-point appendix. Here are its hypotheses and mechanism, which
do not involve the coefficients of the mean.

With $k_{12}=0$ and $k_{13}k_{23}\ne0$, the common divisor of the
three quintic polars has length at most one. The highest identity
and essential dimension three therefore force a degree-two cover
of an irreducible conic, with common divisor exactly one.
The two different parameters $s_1,s_2$ map to $[0:0:1]$.
Both cover degrees there are one. The orders of $p_1/p_3$ at these
two preimages must agree, and the same holds for $p_2/p_3$.
The self-contact orders are at least two, so
$
q(s_1,s_2)=q_s(s_1,s_2)=q_t(s_1,s_2)=0,
$
contradicting off-diagonal smoothness. This uses the proved
projection degree identity $5-\delta=e d$, including all basepoints.

### 2.3 Exactly two pairings zero

Write $k_{12}=k_{13}=0,k_{23}=1$, so the original quadratic on this
space is $F_0=X_2X_3$. Evaluation of the highest identity at $s_2,s_3$
gives $c_2=c_3=0$.

First suppose the isolated node has nonzero mean. Interchanging
2 and 3 if necessary, $a_1a_2\ne0,a_3=0$.
The full mean gradient, along $u_1$ after applying $K^{-1}$, gives
$a_1b_2b_3=0$. The full second-physical gradient then reduces to
$
2a_1a_2b_3p_1p_3+2b_2b_3p_2p_3=0.
$
Thus $b_3=0$. Every term of $T_3$ now uses only $X_1,X_2$,
contradicting its essential dimension.

It remains that $a_1=0,a_2a_3\ne0$. The same complete second gradient is
$
b_1a_2a_3p_1^2+2b_2b_3p_2p_3=0.
\tag{2.3}
$
The physical-polar square lemma, §3 of the three-point appendix,
excludes $p_1^2$ proportional to $p_2p_3$ when $k_{23}\ne0$.
Since none of the polars vanishes identically, (2.3) gives
$
b_1=0,\qquad b_2b_3=0.
$
If $b_2=b_3=0$, the highest identity gives $c_1=0$, so $T_3=0$.
Otherwise interchange 2 and 3 and take $b_2\ne0,b_3=0$. The only
remaining highest relation is
$
p_1^3=\rho\,p_2^2p_3,\qquad \rho\ne0.
\tag{2.4}
$
At $s_2$, the nonzero value of $p_3$ implies that twice the self
order of $p_2$ is divisible by three. At $s_3$, its self order
must be divisible by three. By (1.2), both self orders equal three:
the two different points are exactly $2,-6$.

There is no third physical point orthogonal to both. An infinite
third point is excluded by $k(\infty,2)=-3$ and $k(\infty,-6)=5$.
A finite third point, different from 2 and -6, would satisfy
$
Q_2(z)=3z^2-17z+6=0,\qquad Q_{-6}(z)=5z^2+65z+66=0.
$
But
$
5Q_2-3Q_{-6}=-56(5z+3),\qquad Q_2(-3/5)=432/25\ne0.
$
This contradicts (2.4).

The only remaining graph has all three pairings zero. The common
space is therefore totally isotropic; the proved physical
length-three isotropic classification identifies it as $W_\pm$.

## 3. A double point and a distinct point: the mean uses the double jet

Let $u_0=v(s),u_1=v'(s),w=v(t)$, $s\ne t$, using a local chart at
infinity, and use coordinates $X,Y,Z$. The physical tensors are
$
H=h_0X^2+2h_1XY+h_2Z^2,\qquad
V=v_0X^3+3v_1X^2Y+v_2Z^3.
\tag{3.1}
$
Suppose $y=aX+bY$, $b\ne0$.
Put $k=u_0Kw,\ell=u_1Kw,g=u_1Ku_1$.

If $k\ne0$, the polar $p_t$ is a unit at $s$.
Evaluation of the highest identity first gives $v_2=0$.
Writing $r=\operatorname{ord}_s p_1\ge1$, the sole next term of
order $r$ is $-6b h_2p_1p_t^2$, so $h_2=0$.
Then all three tensors use only $X,Y$, a contradiction.
Thus $k=0$.

At $t$, the highest identity gives $b^3\ell^3=0$, hence $\ell=0$.
If $g\ne0$, the orders at $s$ are $2,1$ for $p_0,p_1$,
whereas $p_t$ has order at least two. The sole term of order three
in the highest identity is $b^3p_1^3$, again a contradiction.
Thus $g=0$. All entries of $K|_{E_{2s+t}}$ are zero, but the
physical isotropic classification excludes every divisor of type
$2+1$. This mean type is impossible.

## 4. A double point and a distinct point: the mean uses the two values

Now $y=aX+cZ$, $ac\ne0$, with (3.1).

Again $k\ne0$ is impossible. In that case the highest identity at
$s$ gives $c^3-6ch_2+4v_2=0$; its unique next term, of order
$r+1$, gives $h_2=c^2/2$, hence $v_2=c^3/2$.
After these cancellations,
$
T_3=X\{C X^2+12(v_1-ah_1)XY+
3c(a^2-2h_0)XZ-12ch_1YZ\},
\tag{4.1}
$
where $C=a^3-6ah_0+4v_0$.
At $s$, the $YZ$ term inside braces is the unique term of least
order whenever $h_1\ne0$, because $p_t$ is a unit and
$\operatorname{ord}p_1=r<r+1=\operatorname{ord}p_0$.
Thus $h_1=0$. The remaining braces have a factor $X$, so a
product of nonzero linear polars would have to vanish identically,
unless $T_3=0$. Both alternatives contradict essential dimension
three and the highest identity. Therefore $k=0$.

In this case the original Gram matrix and mean polar are
$
K|_{E_C}=
\begin{pmatrix}0&0&0\\0&g&\ell\\0&\ell&0\end{pmatrix},
\qquad p_y=(0,c\ell,0).
$
The complete second gradient is the vanishing on physical polars of
$
N=T_{3,p_y}-F T_2+4HKH.
$
Here $F=0$, and direct contraction gives the exact factorization
$
N=4X\{[c\ell(v_1-ah_1)+g h_1^2]X+
\ell h_1(2h_2-c^2)Z\}.
\tag{4.2}
$
Since $p_0,p_t$ are independent, both coefficients in braces vanish.

If $\ell\ne0$, $h_1=0$ in (4.2) would force $v_1=0$, reducing
the essential support to $X,Z$. Hence $h_1\ne0$ and $h_2=c^2/2$.
At $s$, $p_t$ has order one. All terms other than the coefficient
of $p_t^3$ have order at least four, so $v_2=c^3/2$.
Equation (4.1) holds again. If $m=\operatorname{ord}_s p_0\ge2$,
the orders of $p_0,p_1,p_t$ are $m,m-1,1$.
The $YZ$ term inside braces has exact order $m$; the other terms
have orders at least $m+1$. Its coefficient is nonzero, a contradiction.

If $\ell=0$, equation (4.2) gives $g h_1^2=0$.
When $g\ne0$, this forces $h_1=0$; essential dimension three then
requires $v_1\ne0$. The polars at $s$ have orders
$\operatorname{ord}p_0=2,\operatorname{ord}p_1=1,
\operatorname{ord}p_t\ge2$. The unique fifth-order term of the highest
identity is $12v_1p_0^2p_1$; every other term has order at least six.
This is impossible. Thus $g=0$, again yielding the prohibited
totally isotropic $2+1$ jet space.

## 5. One triple point

Let $u_0,u_1,u_2$ be the value, first and Taylor second jets at $s$.
The mean is $y=a u_0+b u_1$, $b\ne0$. In coordinates $X,Y,Z$,
$
H=h_0X^2+2h_1XY+h_2(2XZ+Y^2),\qquad
V=v_0X^3+3v_1X^2Y+3v_2(X^2Z+XY^2).
\tag{5.1}
$
Consequently $T_3$, as a plane cubic, is singular at $[0:0:1]$:
it has no $Z^3,XZ^2,YZ^2$ terms.

The three physical polars have no common zero away from $s$.
Indeed such a zero would give $q=q_s=q_{ss}=0$ in the other variable,
making one nonzero binary cubic polar a pure cube, which is prohibited.
At $s$ their exact common order is $m-2$, where the self order
$m$ is given by (1.2).

For a generic point $m=2$, the common divisor has degree zero.
The degree identity $5-\delta=e d$, $e=2$ or 3, immediately
excludes the highest identity with essential dimension three.

At $s=2,-6$, the common divisor has degree one. The image would
have to be a conic with covering degree two. The first two polars
have no common zero away from $s$: the complete original calculations
are
$
\operatorname{Res}_z(q(2,z),q_s(2,z))=-124928,\qquad
\operatorname{Res}_z(q(-6,z),q_s(-6,z))=-488208384.
$
They are recorded in §3 of
[the reduced-polar appendix](R150-appendix-inside-mean-reduced-support-and-simple-polars.md).
After removing the common divisor, the first two coordinates have
orders two and one at $s$, and the third is a unit.
Thus $[0:0:1]$ has exactly one preimage and that preimage is
unramified. This is impossible for a degree-two cover of a smooth conic.

At $s=0,\infty$, the common divisor has degree two, so the image
would be an irreducible cubic and the map its normalization.
The first two polars have no common zero other than $s$, as seen
directly in the local formulas
$
\begin{array}{ll}
s=0:&p_0=z^4(5-z),\quad p_1=z^3(-32+5z-z^2),\\
s=\infty:&p_0=z^4(-1-z),\quad p_1=5z^3(1+z+z^2).
\end{array}
$
After removing the common quadratic, their orders are two and one;
the third coordinate is a unit. Hence $[0:0:1]$ has one preimage
and the normalization is immersive there. It is therefore a smooth
point of an irreducible cubic: a nodal singularity has two preimages,
and a cuspidal singularity has a nonimmersive single preimage.
But (5.1) makes this point singular for $T_3$, the cubic equation
of that image. This contradiction finishes the triple-point case.

## 6. Complete criterion within the proved class

Every effective length-three divisor has been treated. Only the
three distinct, mutually orthogonal physical points remain, giving
$W_\pm$. Since the entire ordinary-moment functional through degree
six is supported there, the already proved
[isotropic-plane moment criterion](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)
applies without a mean-rank restriction:
$
\nabla\mathcal Q_3=0\quad\Longleftrightarrow\quad Q_\pm\mid T_3|_{W_\pm}.
$
It includes the present two-point means. The three original first
directions satisfy both physical conic equations, so their matched
Bell cubics are zero on this whole class.

The proof uses exact original identities and local orders only;
no finite-field sampling or additional verification gate is required.
It does not convert this scalar classification into a global
Jacobian-power statement or a Hilbert-space invariant-subspace result.
