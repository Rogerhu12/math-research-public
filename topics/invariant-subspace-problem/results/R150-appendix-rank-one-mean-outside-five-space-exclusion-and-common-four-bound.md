# R150 appendix — rank-one outside means exclude the common five-space

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved**.

## 1. Statement and resulting common four-dimensional bound

Retain the original physical Hankel tensors and
$$
T_3=y^3-6yH+4V.
$$
Assume
$$
y=a v(s),\quad a\ne0,\qquad
\operatorname{ess}(T_3)=W,\quad\dim W=3,\qquad
T_3(Kv(z))\equiv0.
\tag{1.1}
$$
If $y\notin W$, the minimal common support of $y,H,V$ cannot have
dimension five.

Together with
[the rank-one conormal bound and inside-five-space exclusion](R150-appendix-rank-one-mean-five-dimensional-bound-and-inside-five-space-exclusion.md),
this proves that every tuple satisfying (1.1) has a common support
of dimension at most four. Only the original highest identity is
used in the final exclusions; no low critical gradient is needed.

The result includes all local multiplicities, zero lower coefficients,
and the physical point at infinity. It does not classify the remaining
common three- and four-dimensional cases.

## 2. The two annihilating directions and their exact equations

Suppose a minimal common five-space $E$ exists.
As proved in the preceding appendix, every such hyperplane is the
physical jet space $E_g$ of a unique divisor $g$ of length five.
Both $H,V$ have their actual local representations on $g$, allowing
zero top coefficients before taking their exact sub-divisors.

Let $u_0=v(s)$ and choose a genuine first jet $u_1$ at $s$.
Write
$$
T_s=\operatorname{span}(u_0,u_1),\qquad y=a u_0.
$$
The exact conormal assertion is that $yz$ is Hankel if and only
if $z\in T_s$.

Since $W$ has codimension two in $E$ and $y\notin W$, choose
independent $\lambda_0,\lambda_1\in\operatorname{ann}_E W$ with
$$
\lambda_0(y)=0,\qquad \lambda_1(y)=1.
$$
Contraction of the same original $T_3$ gives
$$
H\lambda_0=z_0\in T_s,\qquad V\lambda_0=yz_0,
\qquad z_0\ne0.
\tag{2.1}
$$
The nonvanishing follows from minimality of $E$: if $H\lambda_0=0$,
then $V\lambda_0=0$ as well and $\lambda_0$ annihilates all common
supports.

The other contraction gives
$$
H-2V\lambda_1=-2y(H\lambda_1-y/4).
$$
The left side is Hankel, so for some $z_1\in T_s$ we obtain
$$
H\lambda_1=y/4+z_1,\qquad
H=2V\lambda_1-2yz_1,
\tag{2.2}
$$
$$
V\lambda_1^2=
\left(\frac18+\frac{\lambda_1(z_1)}2\right)y+z_1.
\tag{2.3}
$$
These are full tensor equations, not a central-trace substitution.

## 3. The mean block has exactly length two, and V has full length five

Let the exact local lengths of $H,V$ at $s$ be $m,n$.
They are nonzero by (2.1).
All contractions in (2.1) have support only at $s$;
at any other local support the top-coefficient Frobenius pairing
therefore makes $\lambda_0$ vanish on the full $H$ and $V$ blocks.

Let $j$ be the order of the local function $\lambda_0$ at $s$.
Because $\lambda_0(u_0)=0$, $j\ge1$.
The vector $z_0$ has exact local length $r=1$ or $2$, and the
Hankel quadratic $yz_0$ has the same exact length $r$.
Frobenius contraction at the exact local tops in (2.1) gives
$$
m-j=r,\qquad n-j=r.
$$
Thus
$$
m=n\ge2.
\tag{3.1}
$$

On the other hand $\lambda_1(u_0)=1/a$ is a unit at $s$.
Its square preserves the entire exact local length of $V$.
The right side of (2.3) lies in $T_s$, so $n\le2$.
Consequently
$$
m=n=2,\qquad j=1,\qquad z_0\in\mathbb C u_0.
\tag{3.2}
$$

Write the remaining divisor as $R=g-2s$.
It has length three and is disjoint from $s$.
On it (2.2)–(2.3) give
$$
H_R=2V_R\lambda_1,\qquad V_R\lambda_1^2=0.
\tag{3.3}
$$
In particular the exact support of $H_R$ is contained in that
of $V_R$. Minimality of the common space now makes $V_R$ exact
on all of $R$. At $s$ the top $V$ coefficient is nonzero by (3.2).
Thus
$$
g=2s+R,\qquad \operatorname{ess}(V)=5.
\tag{3.4}
$$
This conclusion has been proved from the two real annihilating
equations; it was not assumed from the common-space dimension.

The exact local representation of $V_R$ is Frobenius, so (3.3)
also says that $\lambda_1^2=0$ in the length-three algebra of $R$.

## 4. The entire mean double block cancels in the third tensor

Normalize $\lambda_0(u_1)=1$, and put $b=\lambda_1(u_1)$.
The local tensors at $s$ are
$$
H_s=h_0u_0^2+2h_1u_0u_1,\qquad
V_s=v_0u_0^3+3v_1u_0^2u_1,\qquad h_1v_1\ne0.
$$
Equation (2.1) first gives
$$
v_1=a h_1.
\tag{4.1}
$$
The local coordinates of $z_1=H\lambda_1-y/4$ are
$$
z_1=(h_0/a+h_1b-a/4)u_0+(h_1/a)u_1.
$$
There is no exterior component because (2.2) already places it
in $T_s$. Comparing the $u_0^2$ coefficient in
$V\lambda_1=H/2+yz_1$, and using (4.1), gives
$$
v_0=\frac32 a h_0-\frac14 a^3.
\tag{4.2}
$$
The other coefficient is exactly (4.1), so none is omitted.

Direct substitution now yields the complete cancellation
$$
y^3-6yH_s+4V_s=0.
\tag{4.3}
$$
Indeed its $u_0^3$ coefficient is
$a^3-6ah_0+4v_0=0$, and its $u_0^2u_1$ coefficient is
$-12ah_1+12v_1=0$.

Define
$$
j:E_R\longrightarrow E_R+\mathbb Cy,\qquad
j(v)=v-\lambda_1(v)y.
$$
This is injective because $y$ is outside $E_R$.
Equations (3.3), (4.3) and $\lambda_1^2=0$ on $R$ give
$$
T_3=4V_R-6yH_R=4j^{\otimes3}(V_R).
\tag{4.4}
$$
The image $j(E_R)$ is $W$: it is annihilated by both $\lambda_0$
and $\lambda_1$ and has dimension three.

## 5. Every length-three residual algebra is excluded

If $\lambda_1|_R=0$, then $T_3=4V_R$ is a nonzero physical Hankel
cubic. The invertibility of the
[original highest Hankel map $J_3$](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)
contradicts the highest identity.

Otherwise $\lambda_1|_R$ is a nonzero square-zero element.
A reduced three-point algebra has none. Only two multiplicity
types remain.

For a double point plus a different simple point, take physical
jets $w_0,w_1$ and a physical value $q$ at the other point.
Then
$$
V_R=\eta_0w_0^3+3\eta_1w_0^2w_1+\beta q^3,
\qquad \eta_1\beta\ne0,
$$
$$
\lambda_1(w_0)=\lambda_1(q)=0,\qquad
\lambda_1(w_1)=\tau\ne0.
$$
Equation (4.4) becomes
$$
T_3=4\beta q^3+
12\eta_1w_0^2
\left(w_1-\tau y+\frac{\eta_0}{3\eta_1}w_0\right).
$$
The three displayed directions are independent by injectivity of $j$.
This is the prohibited physical cusp: its repeated direction is
the physical value $w_0$ and its cubed direction is the other physical
point $q$. The pure
[physical repeated-factor/secant-cube exclusion](R150-appendix-no-physical-repeated-factor-secant-cuspidal-companion.md)
applies with a rank-one cubed direction, within its proved scope.

For a triple point, use Taylor jets $w_0,w_1,w_2$. A nonzero
square-zero function has values $0,0,\tau$, $\tau\ne0$.
Write
$$
V_R=\eta_0w_0^3+3\eta_1w_0^2w_1+
3\eta_2(w_0^2w_2+w_0w_1^2),\qquad\eta_2\ne0.
$$
Equation (4.4) gives
$$
T_3=12\eta_2w_0\left[
w_0(w_2-\tau y)+w_1^2+
\frac{\eta_1}{\eta_2}w_0w_1+
\frac{\eta_0}{3\eta_2}w_0^2
\right].
$$
The nonzero physical polar of $w_0$ can be cancelled from the
highest polynomial identity. The remaining conic would make that
value polar divide the square of its genuine first-jet polar.
This is impossible by the
[original tangent polar nondivisibility theorem](R150-appendix-original-physical-tangent-polars-never-square-divide.md).

These arguments include local charts at infinity and every zero
lower coefficient. All possibilities for $R$ have been exhausted.

## 6. Exact conclusion and continuing scope

A rank-one outside mean cannot have a common five-dimensional
support under the original highest identity.
The preceding inside-five-space theorem and the general conormal
bound now give
$$
\boxed{\operatorname{rank}\operatorname{Cat}(y)=1,\ 
\operatorname{ess}(T_3)=3,\ T_3(Kv)=0
\ \Longrightarrow\ \dim E\le4.}
$$

The proof uses finite local algebra, the two complete annihilating
equations, and the already proved original physical kernel lemmas.
The only local cancellation needed is displayed coefficient by
coefficient in (4.1)–(4.3); no independent audit gate or unperformed
computer run is claimed.

The common dimension-four class and the exact three-space critical
classification remain separate work. No global Jacobian-power
membership or operator-theoretic conclusion follows automatically
from this support bound.
