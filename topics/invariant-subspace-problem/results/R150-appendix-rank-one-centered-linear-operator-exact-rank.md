# R150 appendix — the exact rank of the centered rank-one-mean linear operator

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved for the original matrix over $\mathbb C$**.

## 1. Statement

Use the centered rank-one-mean notation of
[the complete reduction](R150-appendix-rank-one-physical-mean-centered-complete-critical-reduction.md):
$$
y=a\,v(s),\quad a\ne0,\qquad
A_y=B_y^{\mathsf T}J_3^{-1}B_yJ_2,
$$
where $B_y$ is multiplication by $p_y(z)=y^{\mathsf T}Kv(z)$.
This is an operator on the eleven physical Hankel quadratic
coefficients.

Let
$$
\begin{aligned}
E_8(s)={}&5s^8+50s^7+153s^6-936s^5-2888s^4\\
        &+15936s^3-3392s^2-25472s+9600,
\end{aligned}
$$
and use the already fixed support polynomials
$$
P_+(s)=s^3-5s^2+\frac{32}{5}s-\frac85,\qquad
P_-(s)=s^3+27s^2+\frac{864}{5}s+\frac{864}{5}.
$$
Define the projective exceptional set
$$
\mathcal S=
\{0,2,-6,\infty\}\ \cup\
\{s:P_+(s)P_-(s)E_8(s)=0\}.
\tag{1.1}
$$

**Theorem.**
$$
\boxed{
\operatorname{rank}A_y=
\begin{cases}
9,&s\notin\mathcal S,\\
8,&s\in\mathcal S.
\end{cases}}
\tag{1.2}
$$
Consequently $\ker A_y$ has dimension two or three, respectively.
Away from $\mathcal S$ it is exactly
$$
\ker A_y=\operatorname{span}\{u^2,\operatorname{sym}(u\,u_1)\},
\qquad y=a u,
\tag{1.3}
$$
the tangent quadratic space which is also the kernel of
$L_y-y(\cdot)$.

This is a statement about the full exact operator, not just
its rank at finitely many parameter samples.

## 2. Replacing an eleven-dimensional inverse by a five-dimensional Gram form

The nonzero scalar $a$ multiplies $A_y$ by $a^2$, so it suffices
to take $y=v(s)$.
Let $D_s$ be the zero divisor of the nonzero homogeneous quintic
$p_s=K(v(s),v(\cdot))$. It has degree five, including infinity.

The map $B_s:S_{10}\to S_{15}$ is injective.
In the dual coefficient pairing put
$$
U_s=\ker B_s^{\mathsf T}.
$$
Then $\dim U_s=5$, and $U_s$ is precisely the physical cubic
jet space supported on $D_s$.
Indeed its elements are the functionals on degree-fifteen
binary forms which kill $p_sS_{10}$.
Finite division and the Chinese remainder theorem identify
them with the value and Taylor jet functionals at $D_s$.
This is finite binary algebra; no extension to an infinite
moment sequence is used.

The following explicit isomorphism controls the nullity:
$$
\boxed{
\ker A_s\ \longrightarrow\
\operatorname{rad}(J_3|_{U_s}),\qquad
M\longmapsto J_3^{-1}B_sJ_2M=L_s(M).
}
\tag{2.1}
$$
If $A_sM=0$, the image $V$ is in $U_s$, and
$J_3V=B_sJ_2M$ is perpendicular, in the coefficient pairing,
to $U_s=\ker B_s^{\mathsf T}$. Thus $V$ belongs to that radical.
Conversely, for a radical vector $V$, $J_3V$ lies in
$U_s^\perp=\operatorname{im}B_s$.
Injectivity of $B_s$ and invertibility of $J_2$ recover a unique $M$.
This proves (2.1).

The Gram form in (2.1) has a direct physical meaning.
For physical cube jets at $t,u$ it is the corresponding
Taylor coefficient of
$$
k(t,u)^3.
\tag{2.2}
$$
Equivalently it is the symmetric-cube pairing induced by $K$.

Let $E_{D_s}$ be the physical linear jet space of the same
degree-five divisor. Its dimension is five, and
$$
E_{D_s}=v(s)^{\perp_K}.
\tag{2.3}
$$
Every defining jet is killed by $p_s$, giving the inclusion;
equal dimensions give equality.
In particular any cubic tensor with a factor $v(s)$ annihilates
every cubic tensor supported on $E_{D_s}$ under (2.2).

## 3. The original possible divisors

The unchanged kernel is
$$
k(s,z)=-(z-s)^2q(s,z),
$$
$$
q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2
 +(s^3-3s^2+22s)z+s^3-5s^2.
$$
The original pure kernel results in §2 of
[the three-distinct-support appendix](R150-appendix-three-distinct-physical-support-complete-critical-classification.md)
give:

- no projective cubic $q(s,\cdot)$ is a pure cube;
- $\operatorname{disc}_zq(s,z)=s^2E_8(s)$;
- $E_8$ is square free;
- the only exceptional self-contact points are $0,2,-6,\infty$.

The precise remaining root multiplicities follow also from
[the physical tangent-polar theorem](R150-appendix-original-physical-tangent-polars-never-square-divide.md).
Away from those four self-contact points, the divisor is either
$$
D_s=2s+t_1+t_2+t_3
\tag{3.1}
$$
with all four points different, or
$$
D_s=2s+2t+u
\tag{3.2}
$$
with three different points.
The second case occurs exactly at $E_8(s)=0$.

At $s=2,-6$ the divisor is $3s+t+u$ with three different points.
At $s=0$ it is $4[0]+[5]$.
At $s=\infty$ it is $4[\infty]+[-1]$.

All these statements are projective.
For example at $s=-1$, $q$ has a simple root at infinity and
two distinct finite roots, so it belongs to (3.1).

The polynomial $E_8$ has no common root with either $P_\pm$.
The two exact degree-preserving Bézout certificates for this
fact were proved in the
[distinct physical polar square-divisibility appendix](R150-appendix-distinct-physical-value-polars-never-square-divide.md).
Neither $2$ nor $-6$ is a root of $P_+$ or $P_-$.

## 4. Self multiplicity two and three other distinct points

Assume (3.1). The two local cubic jets at $s$ are
$$
u_0^3,\qquad 3u_0^2u_1.
$$
Both have the factor $u_0=v(s)$, so (2.3) makes them radical
vectors in the entire five-dimensional Gram space.

The remaining three cube values have Gram matrix
$$
G=
\begin{pmatrix}
0&k_{12}^3&k_{13}^3\\
k_{12}^3&0&k_{23}^3\\
k_{13}^3&k_{23}^3&0
\end{pmatrix},
\qquad k_{ij}=K(v(t_i),v(t_j)).
$$
Its determinant is
$$
\det G=2(k_{12}k_{13}k_{23})^3.
\tag{4.1}
$$
If all three pairings are nonzero, the Gram radical therefore
has dimension exactly two and (2.1) gives rank $A_s=9$.

If one pairing, say $k_{12}$, is zero, the three distinct
physical points $s,t_1,t_2$ are pairwise orthogonal.
The
[complete isotropic length-three classification](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)
says that their support is exactly the roots of $P_+$ or $P_-$.
Thus $P_+(s)P_-(s)=0$.

Conversely, if $s$ is a root of $P_\pm$, the other two roots
are among the three $t_i$ and their mutual pairing is zero.
These means do belong to the current distinct-root case:
the support roots avoid the four self-contact points and
the roots of $E_8$.

In this exceptional situation $G$ has rank exactly two.
It cannot be the zero matrix, because then four distinct
physical vectors would span a totally isotropic four-space
for the nondegenerate six-dimensional $K$, which is impossible.
A nonzero symmetric zero-diagonal three by three matrix with
zero determinant has rank two: any nonzero off-diagonal entry
gives a nonzero two by two minor.
The total radical dimension is therefore three, and
$\operatorname{rank}A_s=8$.

This proves (1.2) throughout case (3.1), including all simple
roots at infinity.

## 5. The residual double-root case

Assume $D_s=2s+2t+u$.
The two cubic jets at $s$ are again radical.
For the remaining three directions use
$$
v(t)^3,\qquad 3v(t)^2v'(t),\qquad v(u)^3.
$$
The prime means any genuine local first derivative.
Its addition by a multiple of the value does not affect ranks.

Put $c=K(v(t),v(u))$ and $d=K(v'(t),v(u))$.
The remaining Gram block is
$$
G=
\begin{pmatrix}
0&0&c^3\\
0&0&3c^2d\\
c^3&3c^2d&0
\end{pmatrix}.
\tag{5.1}
$$
The zero upper two by two block follows from
$K(v(t),v(t))=K(v(t),v'(t))=0$.

We have $c\ne0$.
Otherwise $s,t,u$ would be a distinct physical isotropic triple,
so $s$ would be a root of $P_+$ or $P_-$.
But the present case has $E_8(s)=0$, contrary to the proved
coprimality.
Thus the minor using the first and third coordinates is
$-c^6\ne0$.
The matrix (5.1) has rank exactly two and radical dimension one.
Adding the two mean radical vectors gives total dimension three,
hence rank $A_s=8$ at every root of $E_8$.

## 6. The four exceptional self-contact points

At $s=2$ or $s=-6$, write $D_s=3s+t+u$.
The three local cubic jets at $s$ are
$$
u_0^3,\qquad 3u_0^2u_1,\qquad
3u_0^2u_2+3u_0u_1^2.
$$
All have a factor $u_0$, so they are radical by (2.3).
The remaining two cube values have Gram block
$$
\begin{pmatrix}0&c^3\\c^3&0\end{pmatrix},
\qquad c=K(v(t),v(u)).
$$
If $c=0$, the physical isotropic triple $s,t,u$ would force
$P_+(s)P_-(s)=0$, which fails at both displayed values.
Thus this block is nondegenerate.
The radical dimension is exactly three.

At $s=0$ or $\infty$, the same three jets are radical.
The fourth local cube jet is
$$
3u_0^2u_3+6u_0u_1u_2+u_1^3.
$$
Modulo the radical its pairing is that of $u_1^3$.
The last independent cube value is at $t=5$ or $t=-1$,
respectively.
In both cases $K(u_1,u_1)=0$, and the two remaining directions
therefore have Gram block
$$
\begin{pmatrix}0&d^3\\d^3&0\end{pmatrix},
\qquad d=K(u_1,v(t)).
$$
The unchanged original matrix gives explicitly
$$
d=-4000\quad(s=0,t=5),\qquad
d=5\quad(s=\infty,t=-1).
$$
The block is nondegenerate.
Again the radical dimension is exactly three.

By (2.1), rank $A_s=8$ at all four points.
Every possible divisor of $p_s$ has now been treated, completing
the theorem.

## 7. The exact generic consequence for the critical equations

The centered reduction already proves that
$\ker(L_y-y(\cdot))$ is the two-dimensional tangent quadratic
space in (1.3), and that it is contained in $\ker A_y$.
At a nonexceptional mean the dimensions now coincide, proving
(1.3).

One immediate conditional consequence is useful:
if a complete critical point has a rank-one mean
$s\notin\mathcal S$ and its centered tensor satisfies $MKM=0$,
then the original second-gradient identity gives
$$
J_2A_yM=0.
$$
Since $J_2$ is invertible, $A_yM=0$, hence $T_3=0$.
Thus any remaining high-essential-dimension critical point
with such a mean must have $MKM\ne0$.

This last condition does not assert that the full critical
equations force $MKM=0$.
The exceptional means and the nonzero $MKM$ branch remain part
of the original seventeen-equation problem.
No sampling result, positivity assumption or unproved
natural-power assertion is used in (1.2).
