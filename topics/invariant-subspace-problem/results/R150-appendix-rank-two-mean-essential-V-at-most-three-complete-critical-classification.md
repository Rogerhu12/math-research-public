# R150 appendix — complete rank-two-mean classification when the third cumulant has at most three essential variables

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, for the complete original six-mode cubic critical system.

## 1. Complete statement and the remaining common-dimension-four case

Use the original physical Hankel tensors $y,H,V$ and
$$
T_3=y^3-6yH+4V.
$$
Assume
$$
\operatorname{rank}\operatorname{Cat}(y)=2,\qquad
\operatorname{ess}(T_3)=W,\quad\dim W=3,\qquad
\operatorname{ess}(V)\le3.
\tag{1.1}
$$
Then the following criterion is necessary and sufficient:
$$
\nabla\mathcal Q_3=0
\quad\Longleftrightarrow\quad
\begin{cases}
y,H,V\text{ are supported on }W_+\text{ or }W_-,\\
Q_\pm\mid T_3|_{W_\pm}.
\end{cases}
\tag{1.2}
$$
All three original matched first Bell cubics therefore vanish on
this whole class.

The proof below excludes the last possible common dimension four.
The outside-mean case is already empty by
[the low-$V$ outside theorem](R150-appendix-rank-two-mean-essential-V-at-most-three-outside-section-is-empty.md).
The common-support bound is four by
[the maximal-five-jet exclusion](R150-appendix-rank-two-mean-maximal-five-jet-section-is-empty.md).
The complete common-dimension-three case is classified in
[the preceding appendix](R150-appendix-rank-two-mean-common-three-dimensional-critical-classification.md).

Thus it remains to assume $y\in W$ and that the minimal common
support $E$ of $y,H,V$ has dimension four. We will obtain a contradiction.
No rank-one or zero-mean class, higher essential dimension of $T_3$,
global Jacobian-power statement, or operator inverse is included.

## 2. The exact mean companion must be outside W

Let $D$ be the unique exact physical mean divisor of length two.
Choose its companion
$$
\begin{array}{ll}
D=s+t:&x=a v(s),\ z=b v(t),\quad
y=x+z,\quad u=x-z,\quad ab\ne0;\\
D=2s:&y=a u_0+b u_1,\quad u=u_0,\quad b\ne0.
\end{array}
\tag{2.1}
$$
The second line uses a genuine local first jet, including at infinity.
The conormal computation already proved for rank-two means says
that $yz$ is Hankel precisely when $z$ is proportional to $u$.

Let $\lambda$ be a nonzero functional on $E$ annihilating $W$.
Since $\lambda(y)=0$, contraction of $T_3$ gives
$$
V\lambda=y(H\lambda).
$$
The left side is Hankel. Consequently
$$
H\lambda=c u,\qquad V\lambda=c yu
\tag{2.2}
$$
for some $c\ne0$. If $c=0$, $\lambda$ would annihilate the essential
supports of all of $y,H,V$, contradicting the minimality of $E$.

The tensor $V$ has its unique exact divisor $D_V$, of length at most
three. In its local Artin algebra it is Frobenius: every top local
coefficient is nonzero. If a local block has length $n$ and $\lambda$
has order $j$, the contraction $V\lambda$ has exact local length
$n-j$ when nonzero.

Suppose $u\in W$. Then $\lambda(y)=\lambda(u)=0$, and (2.2) gives
$V\lambda^2=0$. Frobenius nondegeneracy means $\lambda^2=0$ on
$D_V$. The quadratic $yu$ has exact physical divisor $D$: in the
reduced case it is $x^2-z^2$, and in the double case it has a
nonzero first-jet coefficient. At a mean block of length $m$,
(2.2) therefore gives $n-j=m$, while $\lambda^2=0$ gives $2j\ge n$.
Thus $n\ge2m$ at every mean point, so $\deg D_V\ge2\deg D=4$.
This contradicts (1.1).

We have proved $u\notin W$. Normalize $\lambda(u)=1$.
The symmetric conormal form is
$$
H=H_W+c u^2,\qquad H_W\in\operatorname{Sym}^2W,\quad c\ne0.
\tag{2.3}
$$

## 3. An exact disjoint decomposition D plus R

In (2.1), $\lambda$ is a unit at every mean point.
For a reduced mean its values on $x,z$ are $1/2,-1/2$.
For a double mean its values on $u_0,u_1$ are $1,-a/b$.
Multiplication by a unit preserves the entire local $V$ length.
Equation (2.2) therefore shows that $D_V$ has exactly the mean
multiplicities on $D$, with at most one residual simple point
disjoint from $D$.

The part $V_D$ on $D$ is fixed by (2.2). Define a matching physical
quadratic $H_D$ by the following formulas; after the residual support
is identified below, it is also the actual $D$ part of $H$.

For a reduced mean, put $\rho=2c\ne0$:
$$
H_D=\rho(x^2+z^2),\qquad V_D=\rho(x^3+z^3),\qquad
\kappa=1-2\rho.
\tag{3.1}
$$
For a double mean, put $\eta=c\ne0$:
$$
H_D=\eta u^2,\qquad V_D=\frac{3\eta}{2}yu^2,\qquad
\kappa=1.
\tag{3.2}
$$
For example, direct contraction of (3.1) by $\lambda$ gives
$H_D\lambda=(\rho/2)u$ and $V_D\lambda=(\rho/2)yu$.
The double formula gives the same required contractions.
The uniqueness of $V_D$ follows block by block from the unit values
of $\lambda$ and the exact Frobenius representation. At this stage
$H_D$ is simply the displayed Hankel quadratic whose contraction
matches $H\lambda$; no common physical support for $H$ is assumed.

Define
$$
H_R=H-H_D,\qquad V_R=V-V_D.
$$
Both are Hankel and supported on $W$, and $\operatorname{ess}(V_R)\le1$.
In either case the entire third tensor is
$$
T_3=\kappa y^3-6yH_R+4V_R.
\tag{3.3}
$$

The rank of $H_R$ is at most two. Otherwise its exact length-three
physical space would equal $W$, and uniqueness of the length-two
mean on its union with that divisor would put all of $E_D$ in $W$,
including $u$, a contradiction.

Let $R$ be the union of the exact divisors of $H_R,V_R$.
Initially its length is at most three. If it were three, the same
argument would make $W$ a physical length-three space and put
$u$ in $W$. Essential dimension three in (3.3) then forces
$$
\deg R=2,\qquad y\notin E_R,\qquad W=\mathbb Cy\oplus E_R.
\tag{3.4}
$$
Moreover $D$ and $R$ are disjoint. An intersection of length one
would put a physical value from $D$ in $W$; together with its exact
length-two mean $y$, it spans $E_D$ and again puts $u$ in $W$.
An intersection of length two is even more immediate.
Therefore
$$
E=E_{D+R},\qquad D\cap R=\varnothing,\qquad \deg D=\deg R=2.
\tag{3.5}
$$
This has been derived for the actual low-$V$ tensors, rather than
assumed from a full-rank-$V$ classification.

## 4. A double complementary block is already impossible

Suppose $R=2r$, with value $X=v(r)$ and genuine first jet $Z$.
Since $V_R$ has rank at most one and the union support is exactly $R$,
$$
H_R=h_0X^2+2h_1XZ,\quad h_1\ne0,\qquad V_R=v_0X^3.
$$

For $\kappa=0$, the pure
[zero-cube double-block theorem](R150-appendix-zero-cube-coefficient-double-physical-block-is-empty.md)
excludes (3.3) under exactly these hypotheses, even without low gradients.

For $\kappa\ne0$, an irreducible cubic image is excluded by
[the physical tangent cubic-companion theorem](R150-appendix-no-physical-tangent-two-jet-cubic-companion.md).
To check the conic alternative without importing a nonzero top
$V_R$ coefficient, factor the third tensor in the only possible form
$$
T_3=(Y-A)\,[\kappa Y^2+\kappa AY+\kappa A^2-6H_R],
\qquad
4V_R=-\kappa A^3+6AH_R.
$$
The absent $Z^3$ coefficient forces $A=aX$. The absent $X^2Z$
coefficient then forces $a h_1=0$, hence $a=0$ and $v_0=0$.
The conic is
$$
Q=\kappa Y^2-6h_0X^2-12h_1XZ.
$$
The physical value coordinate $X=0$ is a tangent line to $Q$.
This is forbidden by the main, rank-free theorem in
[the physical first-jet conic appendix](R150-appendix-no-conic-tangent-coordinate-from-physical-first-jet.md).
Thus every double $R$ is excluded, including $V_R=0$.

## 5. Reduced R and the exact complete low blocks

The remaining divisor consists of two distinct physical points.
Use their representatives $X,Z$. Since $V_R$ has at most one
support point, after interchanging them we may write
$$
H_R=hX^2+kZ^2,\qquad V_R=vX^3,\qquad k\ne0.
\tag{5.1}
$$
If $v=0$, exact union support gives $h\ne0$.
If $v\ne0$ but $h=0$, the cubic
$$
\kappa Y^3-6kYZ^2+4vX^3
$$
is smooth for $\kappa\ne0$, so it cannot be rationally parameterized
by the independent physical polars. For $\kappa=0$ it is the
prohibited physical cusp, with cubed direction $X$ and repeated
direction $Z$, covered by the original no-secant cuspidal-companion
lemma. Consequently
$$
hk\ne0.
\tag{5.2}
$$

Put
$$
F=\tfrac12K(y,y),\quad
l_i=K(y,R_i),\quad n_i=K(u,R_i),\quad g=K(X,Z),
\qquad (R_1,R_2)=(X,Z).
$$
In the basis $(y,u,X,Z)$ the original Gram matrix is
$$
K_E=
\begin{pmatrix}
2F&0&l_1&l_2\\
0&\epsilon&n_1&n_2\\
l_1&n_1&0&g\\
l_2&n_2&g&0
\end{pmatrix},
\qquad
\epsilon=\begin{cases}-2F&\text{reduced }D,\\0&\text{double }D.\end{cases}
\tag{5.3}
$$
These entries follow from the physical self and value-tangent
pairings, without changing the original $K$.

Let $\Gamma$ be the original full mean gradient after removing
its invertible factor $3K$. Its $y,Z$ components are, in both cases,
$$
\Gamma_y=\kappa^2F^2-2\kappa(hl_1^2+kl_2^2)+4hkg^2,
\tag{5.4}
$$
$$
\Gamma_Z=-4\kappa Fk l_2+8hkg l_1.
\tag{5.5}
$$
The $u$ component vanishes identically. The unused $X$ component
is also checked in the certificate.

The complete second gradient gives the original quadratic
$$
N=T_{3,Ky}-F(yy^{\mathsf T}-2H)+4HKH,
\qquad N(Kv,Kv)=0.
$$
Its lower right block in the $X,Z$ coordinates is always
$$
N_{RR}=
\begin{pmatrix}
-2Fh+4vl_1&4hkg\\
4hkg&-2Fk
\end{pmatrix}.
\tag{5.6}
$$
Its other entries are exactly:
$$
\begin{array}{c|cc}
 &\text{reduced }D&\text{double }D\\ \hline
N_{yy}&(1-\rho)\kappa F&F\\
N_{uu}&\rho\kappa F&2\eta F\\
N_{yu}&0&0\\
N_{yR}&-2(1-\rho)(hl_1,kl_2)&-2(hl_1,kl_2)\\
N_{uR}&2\rho(hn_1,kn_2)&4\eta(hn_1,kn_2)
\end{array}
\tag{5.7}
$$
The constants $\rho,\eta$ in their respective columns are nonzero.

The supplied exact BigInt verifier reconstructs the original tensor
formula for every component of $\Gamma$ and $N$ in both cases.
It checks all forty block identities and the two consequences used
in §7, with no numerical specialization.

## 6. Projection facts used below

The
[length-four physical projection theorem](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)
applies to the actual space (3.5), without critical or mean-rank
restrictions. It gives:
the four polars of $E$ have common divisor degree $\delta_E\le1$;
after removing it they parameterize a nondegenerate quartic or
quintic curve birationally. Any basepoint belongs to the physical
support of $D+R$. The last fact follows also directly: a basepoint
outside that support would make the nonzero binary cubic
$q(s,\cdot)$ vanish on a divisor of length four.

The projection to $W$ has center
$$
\lambda=[0:1:0:0]\in\mathbb P(E^*).
$$
If its common divisor has degree larger than $\delta_E$, the center
belongs to the four-dimensional image curve, hence to every
quadratic $N=0$ vanishing on that curve.
Conversely, if $N(\lambda,\lambda)\ne0$, no extra common divisor is
created, so $\delta_W=\delta_E$.
This follows by evaluating the three $W$ coordinates on the
basepoint-free four-dimensional parameterization; it holds with
all multiplicities.

For a cubic image, the degree equation is $5-\delta_W=3$,
so $\delta_W=2$ and the map is its normalization.
For a conic, the only possibilities are $(\delta_W,d)=(3,1),(1,2)$.

We will also use the same original theorem's pure assertion
$$
\deg\gcd(p_X,p_Z)\le3
\tag{6.1}
$$
for two different physical value polars. No restricted outside-mean
Gram-rank theorem is used anywhere in this proof.

## 7. The case V_R=0: a complete conic contradiction

Now $v=0$. The highest identity for (3.3) forces
$$
Q=\kappa Y^2-6hX^2-6kZ^2=0
\tag{7.1}
$$
on the physical image. Here $\kappa\ne0$; if it were zero,
$T_3$ would be a product of three linear forms, impossible on a
nondegenerate irreducible image. By (5.2), $Q$ is nondegenerate.

Evaluation at the two physical points of $R$ gives
$$
\kappa l_1^2=6kg^2,\qquad \kappa l_2^2=6hg^2.
\tag{7.2}
$$
Combining these with (5.4) gives the exact relation
$$
\kappa^2F^2=20hkg^2.
\tag{7.3}
$$
In fact the polynomial identity is
$\Gamma_y+2h(\kappa l_1^2-6kg^2)+
2k(\kappa l_2^2-6hg^2)=\kappa^2F^2-20hkg^2$.

If $F=0$, (7.2)–(7.3) imply $g=l_1=l_2=0$.
Equations (5.6)–(5.7) then make $N$ a nonzero constant multiple of
$u(hn_1X+kn_2Z)$, unless $n_1=n_2=0$.
Its vanishing on physical polars, which are independent and live
in an integral domain, forces $n_1=n_2=0$.
Then every entry in (5.3) is zero.
A nondegenerate symmetric bilinear form on a six-dimensional space
cannot have a totally isotropic subspace of dimension four.
Thus $F\ne0$, and (7.3) also gives $g\ne0$.

By (5.7), $N(\lambda,\lambda)\ne0$.
Section 6 therefore gives $\delta_W=\delta_E\le1$.
Since the image is a conic, both degrees equal one:
$E$ has a physical basepoint.

For a reduced mean, neither of its two support points can be that
basepoint, since their mutual pairing is $K(x,z)=F\ne0$.
Neither point of $R$ can be a basepoint, since $g\ne0$.
This exhausts the support and is a contradiction.

For a double mean $D=2s$, the basepoint must be $s$ itself.
It follows that
$$
n_1=n_2=0.
$$
Evaluate $N$ at the physical point $X$ using the double-mean column
of (5.7). Its coordinates are $(l_1,0,0,g)$, and (7.2) with
$\kappa=1$ gives
$$
0=N(l_1,0,0,g)=4kg(Fg-l_1l_2).
$$
Thus $Fg=l_1l_2$. Squaring and using both relations in (7.2) yields
$$
F^2=36hkg^2.
$$
But (7.3) says $F^2=20hkg^2$.
This contradicts $hkg\ne0$, finishing every $v=0$ case.

## 8. The case V_R nonzero and kappa zero

Assume $v\ne0,\kappa=0$. By (5.2),
$$
C=-6Y(hX^2+kZ^2)+4vX^3
\tag{8.1}
$$
is irreducible: as a polynomial linear in $Y$ its two coefficients
are coprime in $\mathbb C[X,Z]$.
It has an ordinary node at $P=[1:0:0]$, with nondegenerate quadratic
part $-6(hX^2+kZ^2)$ in the chart $Y=1$.

The physical map is therefore the cubic normalization with common
divisor of degree two. Both $X,Z$ vanish at both preimages of the
node. On either branch their common order is at least one.
Restoring the common quadratic gives
$$
\deg\gcd(p_X,p_Z)\ge2+2=4,
$$
contradicting (6.1).
This branch is excluded by the highest identity alone.

## 9. The case V_R nonzero and kappa nonzero

Now $v\kappa hk\ne0$. The cubic
$$
C=\kappa Y^3-6Y(hX^2+kZ^2)+4vX^3
\tag{9.1}
$$
is irreducible.
Indeed a line with a nonzero $Z$ coefficient cannot divide it:
substituting $Z=aY+bX$ leaves the nonzero coefficient $4v$ of $X^3$.
A line involving only $Y,X$ would have $Y=cX$ for $c\ne0$,
but substitution leaves the nonzero term $-6kcXZ^2$.
The coordinate lines are excluded by inspection.
Thus the physical image is a cubic.

Since $\delta_W=2>\delta_E$, the center lies on $N=0$.
Equation (5.7), with $\rho\kappa\ne0$ or $\eta\ne0$, gives
$$
F=0.
\tag{9.2}
$$
Equation (5.5) now gives
$$
g l_1=0.
\tag{9.3}
$$

If $g=0$, evaluation of the highest identity at the physical point
$X$ gives $\kappa l_1^3=0$, so $l_1=0$.
Equation (5.4) then gives $l_2=0$.
Again (5.6)–(5.7) make $N$ a scalar multiple of
$u(hn_1X+kn_2Z)$, forcing $n_1=n_2=0$.
All of (5.3) vanishes, the same impossible four-dimensional
totally isotropic space.

Suppose instead $g\ne0$. Then $l_1=0$.
The remaining mean equation gives
$$
\kappa l_2^2=2hg^2.
$$
The highest identity at the physical point $Z$ is
$$
\kappa l_2^3-6hl_2g^2+4vg^3=0.
$$
Together these imply
$$
l_2=vg/h,\qquad \kappa=2h^3/v^2.
\tag{9.4}
$$
The point $Z$ therefore maps, without a basepoint since its
$X$ coordinate equals $g\ne0$, to
$$
P=[v/h:1:0].
$$
This is the ordinary node of (9.1).
In the affine chart $X=1$, write $Y=v/h+t$.
The quadratic part at $P$ is
$$
(6h^2/v)t^2-(6kv/h)Z^2.
$$
Both coefficients are nonzero. In particular the line $Z=0$
is transverse to each of the two nodal branches.

On the normalization, a transverse line through an ordinary node
has order exactly one at either preimage.
But the coordinate $Z$ here is the original polar of the physical
source point $Z$, which has self order at least two.
No common factor can alter this at that parameter because its
$X$ coordinate is nonzero. This is a contradiction.

All nonzero-$v$, nonzero-$\kappa$ cases are excluded.

## 10. Completion of the low-V class and exact record

Sections 2–3 derived the exact disjoint support for every hypothetical
minimal common four-space. Section 4 eliminated a double complementary
block. Sections 7–9 eliminated every reduced complementary block,
including every zero coefficient and both mean divisor types.
Hence no common dimension-four critical point satisfying (1.1) exists.

The outside mean is already excluded, and the only remaining common
dimension is three. Its complete criterion is (1.2).
The sufficiency uses the full ordinary-moment functional through
degree six supported on $W_\pm$, not just the support of $T_3$.
The original three matched directions satisfy both physical conic
equations, so their Bell cubics vanish throughout this class.

Author reconstruction files:

- [exact low-block verifier](../notes/2026-11-14-rank-two-mean-low-V-inside-four-space-verify.js);
- [exact execution record](../notes/2026-11-14-rank-two-mean-low-V-inside-four-space-verification.json).

The verifier reconstructs $8\Gamma$ and $4N$ over an integer
polynomial ring, storing the original tensors as $4H,4V$ to avoid
fractions. All forty component identities and two conic consequences
were checked with actual BigInt arithmetic in code mode.
The geometric arguments and support decompositions are proved above;
no finite-field point sampling, unperformed terminal run, or
independent approval gate is asserted.

The full-$V$ dimension-four class, lower mean ranks, higher essential
dimension of $T_3$, global natural powers, and the original operator
inverse remain their own tasks. This theorem is a complete scalar
stratum classification, not a solution of the ordinary Hilbert ISP.
