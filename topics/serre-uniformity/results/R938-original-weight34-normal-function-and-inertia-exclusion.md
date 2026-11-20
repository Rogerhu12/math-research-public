# R938 — Original weight-34 normal function and exclusion by full inertia

Date: 2026-11-20. Status: **proved subject to the explicit fixed bad integer of R937**. This extends the original normal-layer argument to the actual weight-34 label. It excludes both a lower Frobenius layer and a first-layer pole invisible to differentiation. The same-label critical sigma comparison, its possible low-coefficient vanishing, the fixed bad primes, and the main Serre-uniformity problem are not declared solved.

## 1. Original range and conclusion

Let
$$
p\ge41,\qquad p\equiv5\pmod{12},\qquad p\equiv2,5\pmod9,
\qquad p\nmid B_{34},
\tag{938.1}
$$
where $B_{34}$ is R937's explicit fixed bad integer for the Hecke kernel and the original marked value. Retain all the original markings. Put
$$
p=12g+5,\quad g\ge3,\quad M=\frac{p+1}{6}=2g+1\ge7,
\quad n=p+1=6M,\quad e=p^2-1,
$$
$$
h=\frac{p+33}{2}=6g+19,\qquad r_+=32,\qquad k_+=34.
\tag{938.2}
$$
On the original normal component of R921/R924 use
$$
D:\quad y^2=x(x^M+A_0),\qquad A_0\ne0,\qquad c_1=(0,0).
\tag{938.3}
$$
There are two original infinite nodes. At each, retain its actual equation
$$
UV=\epsilon\varpi^{12};
\tag{938.4}
$$
the unit $\epsilon$ is not removed by a new normalization.

For the actual primitive completed-Hom map at this $h$, write
$$
T_h=Y_h(\mathscr F_h),\qquad
\Omega_h=\mathscr F_h^*\omega_h.
$$
We prove:
$$
\boxed{
b_D(\Omega_h)=b_D(T_h)=b_0=34(p-1),\qquad
t_h^{\rm nor}=\kappa_h x^{g-3}y,\quad\kappa_h\ne0.
}
\tag{938.5}
$$
The normalized differential has poles exactly $R+1$ at both infinite nodes, is regular elsewhere, and
$$
R=\frac{2p-34}{12}=2g-2=M-3.
\tag{938.6}
$$
Moreover
$$
dt_h^{\rm nor}
=x^{g-3}(\alpha_hx^M+\beta_h)\frac{dx}{y},
$$
$$
\alpha_h=\kappa_h\frac{p-17}{6}\ne0,
\qquad
\beta_h=\kappa_hA_0\frac{p-35}{12}\ne0,
\qquad
\frac{\beta_h}{\alpha_h}=\frac{35A_0}{34}.
\tag{938.7}
$$
The first order at $c_1$ is
$$
J=2g-5=\frac{p-35}{6}.
\tag{938.8}
$$
After multiplication by the original Tate index and the original calibration,
$$
p^{-a_h}G_h\in wR_0\langle w\rangle,\qquad
\deg\overline{p^{-a_h}G_h}=J,
\tag{938.9}
$$
with unit highest coefficient. No assertion about its linear coefficient is included.

## 2. The actual completed Hom and its exact inertia character

Use the completed-Hom construction of R924 §§2–4 with the actual $e_h,a_h$ of (938.2). Its inputs are R906's actual Tate-image equality, the integral endomorphism lattice, and integral homomorphism approximation. These inputs do not require $k_+=10$.

Specifically, integral endomorphisms approximate $e_h$; the actual $p^{a_h}$ divisibility factors each corresponding finite homomorphism. Preserve the integral extension at the original nodes and take the formal limit. The resulting actual formal maps satisfy
$$
[p^{a_h}]\mathscr F_h=e_h\gamma,
\qquad \mathscr F_h^*\omega_h=\Omega_h.
\tag{938.10}
$$
Thus $T_h$ is integral in the original node rings, $T_h(c_1)=0$, and its reduction on $D$ is zero. A rational formal antiderivative would not suffice for the node bounds below; their input is this integral extension.

For $u\in\mu_e$, put $q_u=u^{p-1}\in\mu_n$. The original tame action is
$$
\varpi\longmapsto u\varpi,
\qquad x\longmapsto q_u^6x,
\qquad y\longmapsto q_u^3y,
\qquad Y_h\longmapsto u^{(p-1)h}Y_h.
\tag{938.11}
$$
Consequently, if $\varpi^ct_c$ is a first nonzero function layer, its character is
$$
u\cdot t_c=u^{(p-1)h-c}t_c.
\tag{938.12}
$$
The pointwise kernel on $D$ is $\mu_{3(p-1)}$. Since $t_c\ne0$, this kernel forces
$$
\boxed{c=k(p-1),\qquad k\equiv h\pmod3.}
\tag{938.13}
$$
In particular, divisibility of $c$ by $p-1$ is a consequence of the full original inertia, not an added restriction. The resulting $q_u$ character is $q_u^{h-k}$.

## 3. Exact differential order from the original Igusa node

R916 supplies primitive upper-Igusa content $\varpi^{32p}$. R937 supplies the original marked unit $V_{34}^\dagger/E_4$, so the fine Igusa order is exactly $2p-35$. On the node quotient the differential order is $R-1$, with $R$ as in (938.6).

The integral normal-layer comparison of R921 gives $b\ge32p$ and the same pointwise-kernel congruence
$$
b=k(p-1),\qquad k\equiv h\equiv1\pmod3.
$$
For $p\ge41$, the inequality $b\ge32p$ requires $k\ge33$. The least such integer congruent to $1$ modulo $3$ is $34$. Thus $b\ge b_0=34(p-1)$.

In the actual node equation (938.4), the nonzero upper-Igusa coefficient contributes on the other side at precisely
$$
32p+12R=32p+(2p-34)=34(p-1)=b_0.
\tag{938.14}
$$
The lower bound is attained. Its node coefficient retains a factor $\epsilon^R$, which is a unit. Hence the normalized differential, denoted $\nu$, has poles exactly $R+1$ at both nodes and no other poles. No choice of a new node parameter has erased $\epsilon$.

## 4. Excluding a lower function layer killed by differentiation

Let $\varpi^ct_c$ be the first nonzero layer of $T_h$. The original invariant differential is a unit formal series in $T_h$ times $dT_h$, so $c\le b_0$. If $c<b_0$, then $dt_c=0$.

Work over the perfect algebraically closed residue field, retaining the original inertia characters. For a one-variable function field,
$$
\ker(d:k(D)\to\Omega^1_{k(D)/k})=k(D)^p.
$$
Thus $t_c=f^p$. Since $t_c$ is regular on the affine part of $D$ and vanishes at $c_1$, so does $f$.

### 4.1. The integral node bound

An integral function in $UV=\epsilon\varpi^{12}$ has, after division by $\varpi^c$ and passage to its first layer on $D$, pole order at most $\lfloor c/12\rfloor$. A negative power $U^{-j}$ can only arise from a positive power $V^j$, at a cost of at least $12j$ in $\varpi$ valuation. The unit $\epsilon$ does not affect the bound.

Therefore the pole order of $f$ at each infinite point is at most
$$
\left\lfloor\frac{c}{12p}\right\rfloor\le2,
\qquad c<34(p-1)<36p.
\tag{938.15}
$$
Every affine-regular function is $P(x)+Q(x)y$. The function $x$ has a simple pole at each infinity; $y$ has pole order $g+1$ at each. The hyperelliptic involution $\iota$ exchanges the two infinities. If $f$ has pole order at most two at each, then so do
$$
P=(f+\iota f)/2,\qquad Qy=(f-\iota f)/2.
$$
Since $g+1\ge4$, this forces $Q=0$ and $\deg P\le2$. The center condition then gives
$$
f=b_1x+b_2x^2,
\qquad t_c=b_1^px^p+b_2^px^{2p}.
\tag{938.16}
$$

### 4.2. Full inertia contradicts the pole bound

By (938.13), $c=k(p-1)$ with $1\le k\le33$, and $t_c$ has character $q_u^{h-k}$. The candidate monomials have characters
$$
x^{jp}\longmapsto q_u^{6jp}x^{jp}=q_u^{-6j}x^{jp},
\qquad j=1,2.
\tag{938.17}
$$
They are distinct because $n\ge42$. A nonzero candidate must therefore satisfy
$$
k\equiv h+6j\pmod n.
\tag{938.18}
$$
For $p\ge41$, $1\le k\le33$, and $j=1,2$,
$$
0<h+6j-k<2n.
$$
Thus $h+6j-k=n$, and
$$
k=\frac{31+12j-p}{2}.
\tag{938.19}
$$
For $j=1$ this gives $k=(43-p)/2\le1$; for $j=2$ it gives $k=(55-p)/2\le7$.

But $x^{jp}$ has pole order $jp$ at each node. The integral bound requires
$$
jp\le\frac{k(p-1)}{12},
\qquad\text{hence }k\ge\frac{12jp}{p-1}>12j.
\tag{938.20}
$$
This contradicts the bounds just obtained. No $c<b_0$ layer exists, proving $b_D(T_h)=b_0$.

The weight-10 argument using a pole bound below $p$ cannot be copied here: the weight-34 bound can exceed $p$. Equations (938.17)–(938.20) supply the necessary exclusion using the full original character.

## 5. Excluding invisible poles of order p or 2p at the first layer

Write $t=t_h^{\rm nor}$. At $c=b_0$, its exact character is $q_u^{h-34}=q_u^{6g-15}$, with odd exponent. The element $q_u=-1$ is the hyperelliptic involution, so
$$
t=P(x)y.
\tag{938.21}
$$
For every nonzero coefficient of $x^jy$,
$$
6j+3\equiv h-34\pmod n,
\qquad\text{equivalently }j\equiv g-3\pmod M.
\tag{938.22}
$$
If $j$ is the highest degree in $P$, the pole order at both infinities is exactly
$$
S=j+g+1\equiv2g-2\equiv-3\pmod M.
\tag{938.23}
$$
There is no cancellation of this odd leading term at either infinity. Node integrality gives
$$
S\le\lfloor b_0/12\rfloor<3p.
\tag{938.24}
$$

We already know that $dt=\nu$ has pole order exactly $R+1$. If $S>R$ and $p\nmid S$, the leading differentiated pole has nonzero coefficient $-S$ and order $S+1>R+1$, impossible. Thus $S>R$ would require $p\mid S$; by (938.24), only $S=p$ or $S=2p$ are possible.

However, $p=6M-1$, so $p$ and $2p$ are respectively $-1$ and $-2$ modulo $M$. Neither equals $-3$ modulo $M$, since $M\ge7$. This contradicts (938.23).

Consequently $S\le R$, and the exact pole of $dt$ forces $S\ge R$. Therefore $S=R$ and $j=g-3$. Since every degree is congruent to $g-3$ modulo $M$, and $0\le g-3<M$, there is only one monomial:
$$
\boxed{t_h^{\rm nor}=\kappa_hx^{g-3}y,\qquad\kappa_h\ne0.}
\tag{938.25}
$$
This separately excludes the $p$ or $2p$ poles invisible to differentiation at $c=b_0$; knowing $dt$ alone would not justify omitting this step.

## 6. Differential, center order, and the lower endpoint

Direct differentiation of (938.3) gives, for every $j\ge0$,
$$
d(x^jy)
=x^j\left[\left(j+\frac{M+1}{2}\right)x^M
              +\left(j+\frac12\right)A_0\right]\frac{dx}{y}.
\tag{938.26}
$$
At $j=g-3$ this is exactly (938.7). All its displayed factors are nonzero for $p\ge41$.

At $c_1$,
$$
x=A_0^{-1}y^2+\text{higher terms},
$$
so
$$
t_h^{\rm nor}
=\kappa_hA_0^{-(g-3)}y^{2g-5}+\text{higher terms}.
\tag{938.27}
$$
Thus $J=2g-5=(p-35)/6$, with $0<J<p$, and $dt_h^{\rm nor}$ has center order $J-1$.

At the geometric lower endpoint $g=3$ ($p=41$), these formulas read $t=\kappa_hy$, $R=4$, and $J=1$, and all the pole and character inequalities remain valid. R937's marked constant has a factor $41$, however. Hypothesis (938.1) therefore does not claim to settle that already studied prime by this route.

## 7. Original calibration and retained Tate index

Use the original R924 coordinates and target normalization:
$$
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varpi^{3(p-1)}w.
\tag{938.28}
$$
The exact inertia character of $z$ is $u^{3(p-1)}$, because $a-1$ is fixed and $-3p\equiv3\pmod{p+1}$. Expand the primitive function near $c_1$ as $\sum c_jz^j$. Its integral normal order gives $v_\varpi(c_j)\ge b_0$, and (938.27) gives $v_\varpi(c_J)=b_0$. Its constant term is zero.

The exact target character implies, for every nonzero coefficient,
$$
v_\varpi(c_j)\equiv(h-3j)(p-1)\pmod e.
\tag{938.29}
$$
After the original calibration the corresponding coefficient has valuation
$$
v_\varpi(c_j)+3j(p-1)-h(p-1).
\tag{938.30}
$$
Since $h=34+3J$, the three ranges are as follows.

- If $j<J$, then $0<(h-3j)(p-1)<e$ and this number exceeds $b_0$. Its congruence class and $v_\varpi(c_j)\ge b_0$ make (938.30) nonnegative.
- If $j=J$, expression (938.30) is exactly zero.
- If $j>J$, expression (938.30) is positive and a multiple of $e$, hence at least $e$.

Thus the primitive calibrated series is integral over $R_0$ and reduces to a polynomial of exact degree $J$ with unit highest coefficient. Its tail tends to zero, since the lower bound in (938.30) grows with $j$.

Finally restore $[p^{a_h}]$. R924's formal multiplication estimate requires first valuation greater than $p+1$, and here $b_0=34(p-1)>p+1$. The original normal valuation increases by exactly $ea_h$ and the first normal function only acquires a unit factor.

The same estimate in the calibrated target coordinate gives integral $p^{-a_h}G_h$ and preserves its highest residue coefficient. Explicitly, $[p]'=p$ times an integral unit formal series implies that nonlinear coefficients of degrees less than $p$ are divisible by $p$; terms of degrees at least $p$ acquire sufficient valuation from the target scale $h(p-1)>p+1$. Successive division by $p$ preserves the reduced calibrated series. This proves (938.9), including coefficient ideal exactly $p^{a_h}R_0$.

The original $a_h$ has not been set to zero. No assertion about a lower coefficient, including $Q_h'(0)$, follows merely from the unit highest coefficient.

## 8. Remaining same-label comparison

The two extra weight-34 obstructions are now resolved: a lower Frobenius first layer and a first-layer pole of order $p$ or $2p$ invisible to differentiation. R935, R937, and this result still require the weight-34 version of the original R925 critical-product comparison, including its fixed top sigma normalization. That comparison, and nonvanishing of its actual low coefficient at a label with nonzero original Legendre factor, are not assumed here.

## Dependencies

- R906 and R924 §§2–4: actual Tate-image divisibility, integral completed Hom, and extension at the original nodes.
- R913/R916 and R935: the actual primitive label, upper Igusa content, full Norm extension, and complete weight-34 source space.
- R937: the original Hecke kernel and the marked unit outside $B_{34}$.
- R921/R924: original normal component, exact inertia action, node thickness, target coordinate, and calibration.

This is a paper proof. No new mathematical computation was executed.
