# R107: A signed quadratic centre for the complete mean root

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This is a complete analytic enclosure theorem for the same mean root as
[R33](R33-full-head-forcing-on-a-variable-analytic-strip.md) and
[R75](R75-complete-mean-transport-and-shear-constraint.md). It identifies
its signed quadratic Taylor term, bounds the entire analytic remainder,
and controls the complete nonmean source when that quadratic term is
used as an evaluation centre. The full root, its defining equation,
and every zero mode inside the inverse remain unchanged.

The accompanying universal BigInt ledger was actually evaluated in V8:
all twelve exact comparisons passed. No new stored field, source
integral, Green kernel, cut map, or outer solution was evaluated here.
In particular an interval based on this result is a new, explicit
input for a future source evaluation; it does not retrospectively
change an executed numerical package.

## 1. Variables, norm, and identification of the root

Fix the same true real background and radial/source interval as in
R33/R75. Put
$$
z=w^2,\qquad E=1+z,\qquad 0<w\le1/2.
\tag{107.1}
$$
The background is fixed when differentiating the input field. The
relative physical inputs are
$$
P=\frac{h_\theta}{rw},\qquad
\overline K=\frac{(h_r-w)_\perp}{w}.
\tag{107.2}
$$
Both have zero angular mean and only nonzero even Fourier modes. They
may be complex. Write the full relative slope as
$$
K=c+\overline K.
$$
Thus the symbol $c$ here is precisely the $M$ of R33(33.12)--(33.15)
and the full $K$ zero mode of R75. It is not an additive height
constant.

For a fixed nonnegative strip function $\tau(x)$, use
$$
\|f\|_{j,*}
 =\sum_{m\in2\mathbb Z}(1+|m|)^j
       \sup_x e^{\tau(x)|m|}|f_m(x)|,\qquad
R=\|P\|_{1,*}+\|\overline K\|_{1,*}.
\tag{107.3}
$$
Each component and each signed mode takes its radial supremum before
the sum. The mean has only mode zero, so its norm is a radial
supremum. Multiplication in these spaces is bounded by convolution
of the fixed radial modal masses. In particular this proof does not
replace a sum of suprema by a supremum of a sum.

In the notation of R75, set
$$
\begin{aligned}
T&=P_\theta,\quad U=K_\theta-P,\quad y=1+K,\\
S&=1-zP^2,\quad D=ES-zy^2
       =1-z(2K+K^2+EP^2),\\
L&=1+K+ET,\\
\Omega&=\left(1+\frac{z(1+K)T}{S}\right)D^{-1/2},\qquad
\mathcal M(P,K)=\frac{\langle\Omega\rangle-1}{z}.
\end{aligned}
\tag{107.4}
$$
Here $\langle\cdot\rangle$ is the exact angular average and the square
root is its analytic branch at the origin. R33 supplies a
cancellation-free analytic form for the expression divided by $z$;
one need not perform an unstable numerical subtraction.

The complete root is
$$
\mathcal M(P,\overline K+c(P,\overline K))=0.
\tag{107.5}
$$
R33 proves on the complex ball $R\le1/32$ that this root is unique in
its specified small disk, depends holomorphically on the nonmean
input, and obeys
$$
\|c(P,\overline K)\|_{0,*}\le4R^2.
\tag{107.6}
$$
These are bounds for the complete infinite Fourier equation.
Uniform holomorphy in the radial Banach algebra follows either
directly from the uniformly contracting iteration in R33 or from
its stated strong-algebra version. It is not inferred just from
pointwise real roots.

The units in (107.2)--(107.3) are essential. If an input has instead
been certified in physical variables $p=h_\theta/r$ and
$\kappa_\perp=(h_r-w)_\perp$, its $V/w$ and balance factors must first
be paid to obtain (107.3). A numerical bound in a different physical
or canonical norm cannot be substituted for $R$.

## 2. Exact quadratic Taylor term

Define
$$
\boxed{
c_2(P,\overline K)
=-\frac12\left\langle
 (1+3z)\overline K^2+EP^2+2E\overline K P_\theta
\right\rangle.}
\tag{107.7}
$$

**Theorem 107.1.** The constant and linear Taylor terms of $c$ at the
origin vanish, and (107.7) is its exact homogeneous quadratic term.

**Proof.** R75(75.5), in the same relative variables, gives
$$
D_{(P,K)}\mathcal M[p,k]
=\left\langle D^{-3/2}(Lk-EU p)\right\rangle.
\tag{107.8}
$$
Although R75 first establishes this formula on the real positive
branch, both sides are analytic on the R33 complex small-root
neighborhood. Its algebraic differentiation and periodic integration
by parts therefore give the same identity there. At the origin
$D=L=1$, $U=0$, so
$$
D\mathcal M(0)[p,k]=\langle k\rangle,\qquad
\mathcal M_c(0)=1.
$$
For a nonmean input direction this derivative is zero. Implicit
differentiation of (107.5) yields $c(0)=0$ and $Dc(0)=0$.

Let $X=(P_X,K_X)$ and $Y=(P_Y,K_Y)$ be nonmean input directions.
At the origin
$$
D_YL=K_Y+E(P_Y)_\theta,\quad
D_YU=(K_Y)_\theta-P_Y,\quad
D_Y(D^{-3/2})=3zK_Y.
$$
Differentiating (107.8), then integrating the term
$-E P_X(K_Y)_\theta$ by parts, gives the symmetric Hessian
$$
\begin{aligned}
D^2\mathcal M(0)[X,Y]
=\big\langle &(1+3z)K_XK_Y+EP_XP_Y\\
&+E K_X(P_Y)_\theta+E(P_X)_\theta K_Y
\big\rangle.
\end{aligned}
\tag{107.9}
$$
Because $Dc(0)=0$ and $\mathcal M_c(0)=1$, the implicit Hessian is
$D^2c(0)=-D^2\mathcal M(0)$ on nonmean directions. Taking
$\frac12D^2c(0)[X,X]$ proves (107.7). No truncated mean equation was
substituted for (107.5). QED.

The physical correlation
$$
C=\overline K+P_\theta
$$
gives an exact alternative, useful when $C$ is much smaller than its
two separately bounded summands:
$$
\boxed{
c_2=-\frac E2\langle C^2+P^2-P_\theta^2\rangle
       -z\langle\overline K^2\rangle.}
\tag{107.10}
$$
Expanding $C^2$ proves the identity, using $E+2z=1+3z$.
Interval evaluations of (107.7) and (107.10) may be intersected
provided both evaluate the same inputs.

These are signed Laurent averages, not squared absolute values.
For example
$$
\langle\overline K P_\theta\rangle
=\sum_j\overline K_j\,(-ij)P_{-j}.
\tag{107.11}
$$
For a single real cosine/sine mode,
$\overline K=k_m\cos(m\theta)$ and $P=p_m\sin(m\theta)$, its
contribution is
$$
-\frac14\left[
(1+3z)k_m^2+Ep_m^2+2Emk_mp_m
\right].
\tag{107.12}
$$
Different absolute frequencies do not contribute cross terms to
the average. For complex parameter families one must keep the
signed coefficients in (107.11); neither conjugacy nor positivity
of their products is assumed.

## 3. A uniform quadratic norm bound

Let $k=\|\overline K\|_{1,*}$ and $p=\|P\|_{1,*}$, so $k+p=R$.
The minimum nonzero frequency is two. Hence
$$
\|\overline K\|_{0,*}\le k/3,\quad
\|P\|_{0,*}\le p/3,\quad
\|P_\theta\|_{0,*}\le p.
$$
Since $1+3z\le7/4$ and $E\le5/4$, (107.7) gives
$$
\begin{aligned}
\|c_2\|_{0,*}
&\le\frac{7k^2}{72}+\frac{5p^2}{72}+\frac{5kp}{12}\\
&\le\left(\frac7{72}+\frac5{48}\right)R^2
 =\frac{29}{144}R^2<\frac14R^2.
\end{aligned}
\tag{107.13}
$$
The first inequality follows from the Banach convolution estimates,
including the average projection of norm at most one. It therefore
holds for complex fields with radial suprema, not only for real
pointwise Fourier data.

## 4. Complete analytic remainder

**Theorem 107.2.** If $R<1/32$, then the entire mean remainder obeys
$$
\boxed{
\|c-c_2\|_{0,*}
\le\varepsilon(R)
:=\frac{128R^3}{1-32R}.}
\tag{107.14}
$$
In particular, on $R\le1/64$,
$$
\|c-c_2\|_{0,*}\le256R^3.
\tag{107.15}
$$

**Proof.** The case $R=0$ is immediate. For $R>0$ fix the input
$X=(P,\overline K)$ and consider the Banach-valued analytic function
$f(t)=c(tX)$ on $|t|<1/(32R)$. Equations (107.6) and Theorem 107.1
give
$$
f(0)=f'(0)=0,\qquad \|f(t)\|_{0,*}\le4|t|^2R^2.
$$
Thus $g(t)=f(t)/t^2$ has a removable singularity at zero,
$g(0)=c_2(X)$, and $\|g(t)\|_{0,*}\le4R^2$.
On a circle of radius $u<1/(32R)$ the Banach-valued Cauchy
coefficient formula gives
$$
\|[t^j]g(t)\|_{0,*}\le4R^2u^{-j}.
$$
Letting $u$ increase to $1/(32R)$, summing $j\ge1$ at $t=1$,
and using $32R<1$, yields
$$
\|g(1)-g(0)\|_{0,*}
\le4R^2\sum_{j\ge1}(32R)^j
=\frac{128R^3}{1-32R}.
$$
All homogeneous degrees at least three are included. No new
holomorphy radius, angular strip gain, or finite-degree cutoff
has been assumed. QED.

For real data, if interval evaluation gives $c_2(x)\in I_2(x)$,
the same complete mean root satisfies the certified intersection
$$
c(x)\in
\big(I_2(x)+[-\varepsilon(R),\varepsilon(R)]\big)
 \cap[-4R^2,4R^2].
\tag{107.16}
$$
For complex input the corresponding statement is the intersection
of the disk of radius $\varepsilon(R)$ about the exact $c_2(x)$
with the disk $|c|\le4R^2$, or any rigorous box representation
containing that intersection. These enclosures concern the same
root (107.5). At the largest allowed radius the new tail need
not be sharper than the old disk by itself; the intersection
always remains valid.

Pointwise versions are also available: apply the same proof at
each fixed radial point using its own certified strong angular
norm $R(x)$. A uniform radial enclosure then uses the supremum of
the resulting bounds. Since the mean has only one Fourier mode,
this operation does not exchange an infinite sum and a supremum.

## 5. Complete source error is fourth order

Use the same source coordinate as R106,
$$
s=r_x/r,\quad \ell=w_x/w,\quad c_{\rm bg}=s+|\ell|,
\quad D_0=\overline K+EP_\theta,
$$
and define the full Laurent functions
$$
\begin{aligned}
Q&=Es(\overline K_\theta-P)^2
   +\ell\{E(\overline K+P_\theta)^2
                  -z(\overline K^2+P^2)\},\\
F(a)&=\frac{Q+\ell(2aD_0+a^2)}{1+D_0+a}.
\end{aligned}
\tag{107.17}
$$
The complete nonmean source is $\mathcal N(X)=\Pi_\perp F(c)$.
The approximation centred at $c_2$ is $\mathcal N_2(X)=\Pi_\perp F(c_2)$.
Only the latter is an approximation: replacing $c$ by $c_2$
does not solve the complete mean equation.

**Theorem 107.3.** On $R\le1/64$ the denominators in (107.17)
are invertible in the same radial Wiener algebra and
$$
\begin{aligned}
\|(\mathcal N-\mathcal N_2)/c_{\rm bg}\|_{0,*}
&\le
\frac{\varepsilon(R)
          \left(\frac52R+\frac{23}{4}R^2\right)}
 {1-\frac54R-4R^2}\\
&\le 680R^4.
\end{aligned}
\tag{107.18}
$$

**Proof.** From (107.13), (107.6), and
$\|D_0\|_{0,*}\le5R/4$, both denominators have Neumann
inverse norm at most $1/d(R)$, where
$$
d(R)=1-\frac54R-4R^2\ge\frac{1003}{1024}.
\tag{107.19}
$$
The fixed modal-mass proof in R106 gives
$\|Q/c_{\rm bg}\|_{0,*}\le(23/18)R^2$.
For any zero-mode $a$ with $\|a\|\le4R^2$, absolute multiplication
in (107.17) gives
$$
\|F(a)/c_{\rm bg}\|_{0,*}
\le R^2\frac{23/18+10R+16R^2}{d(R)}
\le\frac{13252}{9027}R^2<\frac32R^2.
\tag{107.20}
$$
This estimate concerns the unprojected Laurent function, so it
does not discard a zero mode that the inverse can later mix
into a nonzero output. It applies in particular to $a=c_2$.

The following quotient difference is exact:
$$
F(c)-F(c_2)
=(c-c_2)\,
\frac{\ell(2D_0+c+c_2)-F(c_2)}
     {1+D_0+c}.
\tag{107.21}
$$
Using $\|\ell/c_{\rm bg}\|_\infty\le1$,
$\|c\|\le4R^2$, $\|c_2\|\le R^2/4$, and (107.20)
gives the first bound in (107.18). Every multiplication can be
estimated with the fixed signed modal masses. The density is a
radial coefficient, and projection onto nonzero modes has norm
at most one.

The coefficient multiplying $R^4$ in the first line is bounded by
its value at $R=1/64$, since all its numerator coefficients are
nonnegative and both positive denominators decrease with $R$.
That value is
$$
\frac{128(5/2+(23/4)/64)}
 {(1-32/64)(1-5/256-4/4096)}
=\frac{678912}{1003}
=\frac{39936}{59}<680.
\tag{107.22}
$$
This proves the second bound. QED.

Thus a signed computation of $F(c_2)$, plus (107.18), is a
valid complete-source enclosure. A tighter implementation may
instead insert (107.16) directly into the full quotient, keep
signed Laurent coefficients, and then apply its existing
rigorous inverse-tail method. Either procedure retains the
same mean root, all $c^2$ terms, the zero mode of $Q$, and the
entire pointwise inverse.

There is no new nonmean $c_x$ term in (107.17): $c_x$ is an
angular constant and disappears only after the full second
equation is projected. This theorem does not provide a bound
for $c_x$ by differentiating an interval enclosure. If a
radial derivative or mean height integral is needed, the
complete implicit derivative or a separately paid integral
must still be used.

## 6. Exact ledger and execution scope

The independent source
[closure_signed_mean_quadratic_constants.js](../computations/closure_signed_mean_quadratic_constants.js)
contains the universal rational comparisons and an exact
polynomial check of (107.10). Its output is
[2026-11-13-closure-signed-mean-quadratic-constants.json](../notes/2026-11-13-closure-signed-mean-quadratic-constants.json).

The actual V8 execution used BigInt arithmetic throughout.
It checked twelve gates, including the R33 radius, the full
inverse denominator, the signed quadratic identity, the
$29/144$ bound, the complete Cauchy coefficient $256$ at
$R=1/64$, and the complete source coefficient
$39936/59<680$. All twelve gates were true.
The mathematical holomorphy and Cauchy argument are proved
above; the ledger does not purport to replace that proof.

The ledger takes no stored floating field or scientific
primary as an input. It has no Arb/ODE execution or claimed
terminal status. The existing R88/R104/R105 numerical or
prepared files remain unchanged. In particular this result
does not prove a middle-frequency Green bound, a cut
self-map, or a complete outer Darboux solution.
