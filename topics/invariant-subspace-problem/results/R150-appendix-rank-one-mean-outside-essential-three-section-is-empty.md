# R150 appendix — the rank-one-mean outside essential-three section is empty

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**, using the original highest identity.

## 1. Statement

For the original six-mode physical Hankel tensors, suppose
$$
y=a v(s),\quad a\ne0,\qquad
\operatorname{ess}(y^3-6yH+4V)=W,\quad\dim W=3,
$$
and impose
$$
T_3(Kv(z))\equiv0.
$$
Then
$$
\boxed{y\in W.}
$$
Thus the entire rank-one-mean, essential-third-dimension-three
outside-mean section is empty, even before the lower critical
equations are imposed.

The rank-one five-space arguments already give a minimal common
support of dimension at most four. Since a three-dimensional
common space must equal $W$ and contain $y$, an outside mean would
have a minimal common space $E$ of dimension exactly four.
We exclude that case below.

## 2. The common four-space is genuinely physical without a full-rank assumption

Both $H$ and the first flattening of $V$ have rank at most four.
A rank-four Hankel tensor has its unique exact length-four
physical divisor. If either has rank four, its essential support
is all of $E$, so $E$ is a physical length-four space.

If neither has rank four, their exact divisors each have length
at most three. Their union initially has length at most six,
all of whose jets lie in $E$. Independence of any six physical
jets makes the union length at most four.
If its length is four, its span already equals $E$.
The physical mean $v(s)$ must belong to that divisor: otherwise
five independent jets would lie in $E$.
If the union length is three, the physical mean must add one
new point to obtain the minimal four-space.
A union of smaller length cannot span four dimensions after
adding the one physical mean.

Consequently in every case
$$
E=E_g,\qquad \deg g=4,\qquad s\in\operatorname{supp}g,
\tag{2.1}
$$
and $g$ is the exact union of the supports of $H,V$ and the mean.
This proves the physical-support assertion for both inside and
outside rank-one means whenever their minimal common dimension
is four. No full rank of $H$ or $V$ was assumed.

## 3. The annihilating functional restricts the mean block to length at most two

For an outside mean choose $\lambda$ on $E$ with
$$
\lambda|_W=0,\qquad \lambda(y)=1.
$$
Let $u_0=v(s)$ and let $u_1$ be a genuine first local jet.
The conormal calculation for a physical mean gives the full equations
$$
H\lambda=y/4+z,\qquad
H=2V\lambda-2yz,\qquad z\in\operatorname{span}(u_0,u_1),
\tag{3.1}
$$
$$
V\lambda^2=
\left(\frac18+\frac{\lambda(z)}2\right)y+z.
\tag{3.2}
$$
They follow by contracting $T_3$ and using that $yq$ is Hankel
exactly when $q$ belongs to this tangent two-space.

At $s$, the value $\lambda(u_0)=1/a$ is a unit.
Multiplication by its square preserves the exact local length
of $V$. The right side of (3.2) has local length at most two,
so $V_s$ has length at most two.
Equation (3.1) then gives the same bound for $H_s$.
By the exact union in (2.1), the multiplicity of $s$ in $g$ is
$$
n=1\quad\text{or}\quad n=2.
$$

Let $R=g-ns$, disjoint from $s$.
On its local algebra, (3.1)–(3.2) give
$$
H_R=2V_R\lambda,\qquad V_R\lambda^2=0.
\tag{3.3}
$$
Minimality makes $V_R$ exact on all of $R$.
Its nonzero top coefficients thus imply $\lambda^2=0$ on $R$.

## 4. The mean block cancels completely

Allowing the top coefficients to be zero in the single-point case,
write
$$
H_s=h_0u_0^2+2h_1u_0u_1,\qquad
V_s=v_0u_0^3+3v_1u_0^2u_1.
$$
For $n=1$, set $h_1=v_1=0$.
For $n=2$, comparison of the $u_0u_1$ and $u_0^2$ coefficients
in (3.1) gives
$$
v_1=a h_1,\qquad
v_0=\frac32a h_0-\frac14a^3.
\tag{4.1}
$$
The same second formula holds for $n=1$.
To see that no jet value is omitted, put $b=\lambda(u_1)$:
$$
z=(h_0/a+h_1b-a/4)u_0+(h_1/a)u_1.
$$
Substituting in $V\lambda=H/2+yz$ gives exactly (4.1);
the terms containing $b$ cancel. If $u_1$ is outside $E$,
as in $n=1$, its zero coefficients make the calculation independent
of any extension of $\lambda$.

Hence
$$
y^3-6yH_s+4V_s=0.
$$
Define the injective translation
$$
j:E_R\to E_R+\mathbb Cy,\qquad j(v)=v-\lambda(v)y.
$$
Using (3.3), the full third tensor is
$$
T_3=4V_R-6yH_R=4j^{\otimes3}(V_R).
\tag{4.2}
$$

If $n=2$, the residual space has dimension two. Equation (4.2)
would give essential third dimension at most two, a contradiction.

If $n=1$, $R$ has length three.
The complete residual argument in §5 of
[the outside-five-space appendix](R150-appendix-rank-one-mean-outside-five-space-exclusion-and-common-four-bound.md)
applies under precisely the conditions (3.3)–(4.2):
$V_R$ is exact, $\lambda^2=0$, and $j$ is injective.
For clarity, its exhaustive alternatives are:

- $\lambda|_R=0$: $T_3=4V_R$ is a nonzero Hankel cubic, contradicting
  invertibility of the original highest map $J_3$.
- $R$ reduced: it has no nonzero square-zero function, so it is
  already the preceding case.
- $R$ a double point plus a simple point: (4.2) is a physical cube
  plus a different physical value squared times an independent
  linear direction, the prohibited physical cusp.
- $R$ a triple point: (4.2) has a physical value factor and a conic
  that would make that value polar divide the square of its genuine
  tangent polar, also prohibited.

These original-kernel exclusions include every infinite point
and all lower local coefficients. They do not depend on the
ambient divisor having length five rather than four.

## 5. Conclusion and next case

Both possible multiplicities at the mean point are excluded,
so the hypothetical outside mean does not exist.
Combined with the previous common four-dimensional bound,
the only remaining rank-one-mean, essential-third-dimension-three
critical problem has $y\in W$ and common dimension three or four.

The theorem supplies neither the remaining inside-four-space
classification nor natural Jacobian powers or an operator inverse.
All use of the original highest map, physical cusp, and tangent
conic exclusions retains their proved original-$K$ scope.
