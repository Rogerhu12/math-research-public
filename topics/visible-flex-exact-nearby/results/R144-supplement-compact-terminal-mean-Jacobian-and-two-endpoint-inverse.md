# R144 supplement: the actual compact terminal-mean Jacobian and its two-endpoint inverse

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved for the actual fixed-metric compact centre.** Its complete
fixed-density scalar mean linearization has a terminal inverse with
ordinary $L^\infty\to C^0$ bound $0.605$, physical mean-jump bound
$1.518$, and complete physical nonmean-shape feedback bound $0.087$.
The compact density control has a nonzero *terminal-graph* waist
derivative between $0.002415$ and $0.002469$, and full mean-response
norm below $0.002576$. These give an explicit bounded inverse for
the mean equation with both endpoint means and one compact density
control, retaining every mean atom.

The controlled density is still an unknown in the nonmean equations.
Its derivative is not small merely because the selected value of
the control is tiny. The exact rank-one contribution and the
one-dimensional coordinate redundancy are given below. No full
Gauss--Codazzi inverse, phase transversality or nonlinear convergence
is asserted.

## 1. Terminal and forward derivatives are different

Use precisely the raw object, fixed $\eta_0,\nu_0$, cutoff $\chi$,
and notation of [SR](R144-supplement-sharp-compact-root-from-completed-forward-mean.md).
In particular, the *same* exact compact root has

$$
 -8\,10^{-13}<\xi_*<-7\,10^{-13},\quad
 \rho_s=8\,10^{-13},\quad b_s=2\,10^{-7}.
 \tag{MJ.1}
$$

Write $m$ for the raw mean, $w=v-m$, $V=\langle w^2\rangle$,
$U=\langle u^2\rangle$ and $H(r)=\exp\int_0^r2\beta U$.
For every $|\xi|\le\rho_s$ let $Y^f_\xi$ be the forward solution
with $Y^f_\xi(0)=1$, and let $Y^t_\xi$ be the solution with the
fixed terminal value $Y^t_\xi(R)=n(R)=a(R)^2/m(R)^2$.
The latter is positive by the complete SR mean-ball proof. Put

$$
 P(\xi)=\overline D-\overline a\xi-\overline b\xi^2.
$$

Both solutions have exactly the same inhomogeneous linear equation.
The difference of their endpoint values therefore gives

$$
 \boxed{
 Y^t_\xi(r)=Y^f_\xi(r)-H(r)P(\xi),\qquad
 Y^t_\xi(0)=1-P(\xi).
 }
 \tag{MJ.2}
$$

Thus $Y^t_{\xi_*}=Y^f_{\xi_*}$ as complete functions. Their
off-root derivatives are not the same. In particular

$$
 m^f_\xi(0)=-a_0,\qquad \partial_\xi m^f_\xi(0)=0,
$$
$$
 m^t_\xi(0)=-a_0(1-P(\xi))^{-1/2},\qquad
 \left.\partial_\xi m^t_\xi(0)\right|_{\xi_*}
       =\frac{a_0}{2}(\overline a+2\xi_*\overline b).
 \tag{MJ.3}
$$

Every control derivative below is the derivative of this **fixed
terminal-value graph**. It is not the zero waist derivative of the
forward family.

Let

$$
 m_*=m^t_{\xi_*},\quad q_*=m_*-m,\quad
 \lambda_*=1+\xi_*\chi,\quad
 j_*=1+\lambda_*w/m,\quad J_*=\langle j_*^2\rangle.
 \tag{MJ.4}
$$

The complete mean is continuous, $m_*<0$, and
$\|q_*\|_\infty\le b_s$. The density $j_*>0$ has normalized mean
one. The nonmean raw joins remain; the scalar analysis does not
declare the complete centre continuous.

## 2. The actual scalar operator is a small perturbation of the paid old operator

Hold $u,j_*$ and the original metric fixed. The physical mean
linearization is

$$
 L_*r=r'-a_*r,\qquad
 a_*=\beta(1-U-3Km_*^2J_*).
 \tag{MJ.5}
$$

The old full raw scalar operator, including its proven physical
source and transmission conventions, is

$$
 L_mr=r'-a_mr,\qquad
 a_m=\beta(1-U-KV-3Km^2).
 \tag{MJ.6}
$$

It is the operator in
[CR.3--10](R144-supplement-complete-C0-mean-receiver-and-compact-moments.md).
Its terminal inverse is denoted by $T_m$ when terminal value and
prescribed response jumps are zero. Since
$J_*=1+\lambda_*^2V/m^2$, direct expansion gives

$$
 L_*=L_m+p_*,
 \tag{MJ.7}
$$
$$
 \begin{aligned}
 p_*=\beta K\big[&V(2+6e+3e^2)
       +6(m+\lambda_*^2V/m)q_*\\
       &+3(1+\lambda_*^2V/m^2)q_*^2\big],
       \qquad e=\xi_*\chi.
 \end{aligned}
 \tag{MJ.8}
$$

This is exactly the derivative in $q$ of the full CP polynomial.
The already saved eleven profile receivers and (MJ.1) give

$$
 \|T_m(p_*r)\|_\infty
 \le L_s\|r\|_\infty,
 \qquad L_s<0.014241.
 \tag{MJ.9}
$$

All original mean atoms and the multiplicative raw-mean
transmission factors belong to $T_m$ as in CR. They are not removed
because the new mean itself is continuous. The new term $p_*r$ is
an ordinary source, so it does not introduce another artificial
response jump.

For any complete forcing and prescribed terminal value and jumps,
the equation is exactly

$$
                r=r_{\mathrm{old}}-T_m(p_*r).
 \tag{MJ.10}
$$

Apply the contraction in (MJ.9) in the product of the $C^0$ spaces
on the finitely many closed radial pieces, with the prescribed
affine jump and terminal constraints and their common sup norm.
The integral formula makes the fixed point piecewise absolutely
continuous. Thus it proves existence and uniqueness with exactly
those prescribed data. Equivalently
$(I+T_m p_*)^{-1}$ is a convergent Neumann inverse. It has norm

$$
                 (1-L_s)^{-1}<1.015.
 \tag{MJ.11}
$$

This is an actual scalar inverse at the compact centre, not the
full physical system's inverse.

## 3. Complete ordinary, mean-atom and terminal-value costs

The CP complete records, consumed in SR, give

$$
 K_0<0.595255,\quad K_J<1.495385,\quad K_1<0.085486.
 \tag{MJ.12}
$$

For the first two, (MJ.10) immediately yields the actual bounds

$$
 \|r\|_\infty
 <0.605\|f\|_\infty+1.518\sum_i|k_i|
 \tag{MJ.13}
$$

when $L_*r=f$, $r(R)=0$ and $[r]_i=k_i$ at the actual original
interfaces. The displayed coefficients are strict upper bounds;
the non-strict corresponding norm inequalities are understood when
all data are zero. There are no radial length factors multiplying
the independent atom sum.

A nonzero terminal value can also be retained explicitly. The old
homogeneous propagator satisfies

$$
 |H_m(r,R)|\le\Gamma\,\tau(r)^{-1}\tau(R),\qquad
 \tau=-2a^2/m^3>0,\qquad \Gamma<1.013237.
 \tag{MJ.14}
$$

The saved CP `prefix_inverse_tau_max` is the maximum after *all*
7721 rows, and is less than $2.378\,10^{12}$. The complete FM endpoint
balls give $a(R)<6.564\,10^{-6}$ and $|m(R)|>5.84$. Consequently
the terminal-value cost for $L_*$ is bounded by the exact rational
expression

$$
 \frac{1.013237(2.378\,10^{12})
                  2(6.564\,10^{-6})^2}
      {5.84^3(1-0.014241)}<1.058.
 \tag{MJ.15}
$$

The source of the global inverse-$\tau$ field is the full forward
maximum in
[`fourfold_codazzi_compact_mean_c0_receivers.py`](../scripts/fourfold_codazzi_compact_mean_c0_receivers.py);
it is not the shorter compact $H$ prefix. The bound (MJ.15) does
not set $\tau(R)$ to one and does not replace a physical mean by a
normalized reciprocal mean.

Thus $1.058|b_R|$ can be added to (MJ.13) for $r(R)=b_R$.
An additional body-source space, for example an arbitrary radial
$L^2$ source, is not silently admitted by these $L^\infty$ bounds.

## 4. The full linearized nonmean input to the mean row

Let $p=\delta u$ and let $k=\delta j$ be even with zero angular
mean. To retain the original physical input units write

$$
                         \eta=mk,\qquad \langle\eta\rangle=0.
 \tag{MJ.16}
$$

Here $m$ is the fixed raw mean, a known radial multiplier; it is
not the unknown varied mean $r$. At the compact centre the full
linearized mean equation on the same fixed metric is

$$
 L_*r=f_m-2\beta m_*\langle up\rangle
                -2\beta K m_*^3\langle j_*k\rangle.
 \tag{MJ.17}
$$

Since $\langle k\rangle=0$,
$\langle j_*k\rangle=\lambda_*\langle w\eta\rangle/m^2$.
The nonmean forcing in (MJ.17) is therefore *exactly* the old CR
nonmean source evaluated on

$$
 \widehat p=(m_*/m)p,\qquad
 \widehat\eta=(m_*/m)^3\lambda_*\eta.
 \tag{MJ.18}
$$

The old source is
$-2\beta m\langle u\widehat p+Kw\widehat\eta\rangle$.
No angular frequency or even mean has been discarded in this
identification. From $|m|>1.068$, $|q_*|\le2\,10^{-7}$ and
$|\xi_*|<8\,10^{-13}$, the joint diagonal multiplier in (MJ.18)
has norm at most

$$
 R_s=\left(1+\frac{2\,10^{-7}}{1.068}\right)^3
                         (1+8\,10^{-13})<1.000000562.
 \tag{MJ.19}
$$

The original $K_1$ receiver is in the normalized angular pair
$L^2$ norm and the radial $L^\infty$ norm. It follows that

$$
 \|r_{\mathrm{shape}}\|_\infty
 \le\frac{K_1R_s}{1-L_s}
       \|(p,\eta)\|_{L^\infty_rL^2_\phi,\mathrm{pair}}
 <0.087\|(p,\eta)\|_{L^\infty_rL^2_\phi,\mathrm{pair}}.
 \tag{MJ.20}
$$

The same joint norm is used on both sides of (MJ.18); no extra
$\sqrt2$ or change to a component-sum norm occurs.

For later original metric-$\nu$ variation with $a,\beta$ fixed,
the additional mean source is exactly
$-\beta m_*^3J_*\partial_\nu K\,\dot\nu$. It must be included in
$f_m$ with its own complete bound. The other metric terms in the
nonmean equations are still present. This identity does not import
the selected centre's old $\nu$ certificate to the raw-metric
compact centre.

## 5. The true compact-control derivative is paid on the full core

Define

$$
                  r_c=\left.\partial_\xi m^t_\xi\right|_{\xi_*}.
 \tag{MJ.21}
$$

The terminal graph is differentiable: its positive linear $Y^t_\xi$
is exactly quadratic in $\xi$, and the negative square-root map is
smooth on its complete positive range. Equivalently the uniform CP
contraction can be differentiated. The full terminal conditions are
$r_c(R)=0$ and $[r_c]_i=0$.

Differentiate the *whole* CP polynomial at fixed raw data. If
$C_{ab}$ denote its existing positive receivers, the resulting
inhomogeneous parameter derivative is bounded after applying $T_m$
by

$$
 \begin{aligned}
 D_\xi={}&C_{01}+2\rho_s C_{02}
    +(C_{11}+2\rho_s C_{12})b_s\\
   &+(C_{21}+2\rho_s C_{22})b_s^2
    +(C_{31}+2\rho_s C_{32})b_s^3.
 \end{aligned}
 \tag{MJ.22}
$$

The derivative in the unknown mean contributes exactly the
feedback (MJ.9), rather than being dropped. Using the rational
upper table in SR gives

$$
                  \|r_c\|_\infty
                 \le\frac{D_\xi}{1-L_s}<0.002576.
 \tag{MJ.23}
$$

For comparison, direct differentiation of the mean equation gives

$$
 L_*r_c=f_c,\qquad
 f_c=-2\beta K m_*^3\chi\lambda_*\frac V{m^2}.
 \tag{MJ.24}
$$

The sign is useful. On the compact negative-curvature support,
$\beta K<0$, $m_*<0$ and $\lambda_*>0$, so $f_c\le0$.
It is strictly negative on a set of positive measure by the
already proved positive compact moment. Thus the terminal scalar
Green formula gives $r_c\ge0$, and $r_c(0)>0$.

The exact quantitative waist value is (MJ.3). The old
[waist-radius theorem](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md),
(A.1), gives
$1.06873282<a_0<1.068732841$. Together with SR.7, the signed root
and $0\le\overline b\le\overline a/2$, this gives

$$
       0.002415<r_c(0)<0.002469,
       \qquad r_c(0)^{-1}<415,
       \qquad \frac{\|r_c\|_\infty}{r_c(0)}<1.067.
 \tag{MJ.25}
$$

For the lower bound, explicitly use
$a_0\overline a(1-\rho_s)/2$; for the upper bound, the negative
$\xi_*$ gives $a_0\overline a/2$.
In particular neither the size of $r_c$ nor the reciprocal in
(MJ.25) is proportional to the tiny number $|\xi_*|$.

## 6. Both endpoint mean conditions and every transmission source

Given $p,\eta,f_m$, actual mean jumps $k_i$, a desired outer
mean variation $b_R$, and a desired waist variation $b_0$, first
solve (MJ.17) with $r_b(R)=b_R$ and $[r_b]_i=k_i$.
This step is justified by Sections 2--4. Add one compact density
variation

$$
 \delta j=\eta/m+\dot\xi\,\chi w/m.
 \tag{MJ.26}
$$

The additional mean response is exactly $\dot\xi r_c$. Therefore

$$
 \boxed{
 \dot\xi=\frac{b_0-r_b(0)}{r_c(0)},\qquad
                 r=r_b+\dot\xi r_c
 }
 \tag{MJ.27}
$$

is the unique solution for this given uncontrolled shape input.
It has $r(0)=b_0$, $r(R)=b_R$ and the prescribed jumps $k_i$.
No independent mean row or interface is omitted.

Put

$$
 \mathcal E=0.605\|f_m\|_\infty
  +0.087\|(p,\eta)\|_{L^\infty_rL^2_\phi,\mathrm{pair}}
  +1.518\sum_i|k_i|+1.058|b_R|.
 \tag{MJ.28}
$$

Then

$$
 |\dot\xi|\le415(|b_0|+\mathcal E),\qquad
 \|r\|_\infty\le2.067\mathcal E+1.067|b_0|.
 \tag{MJ.29}
$$

These are complete scalar bounds. The first bound is deliberately
retained in the nonmean equations: differentiating the compact
control creates $\dot\xi\chi' w/m$ and all the other derivative
terms, even when $|\xi_*|$ is tiny.

There is also an exact scalar Green form which displays the
cancellation responsible for (MJ.27). Let

$$
 E_*(r)=\exp\int_0^r a_*(t)\,dt,\qquad
 H_*(r,s)=E_*(r)/E_*(s),
$$
$$
 \vartheta(r)=
  \frac{\int_0^r[-f_c(s)]/E_*(s)\,ds}
       {\int_0^R[-f_c(s)]/E_*(s)\,ds}.
 \tag{MJ.30}
$$

Its denominator is $r_c(0)>0$, so $0\le\vartheta\le1$.
It is zero for $r\le1/20$ and one for $r\ge9/50$. Set

$$
 \mathcal K(r,s)=H_*(r,s)
                  \bigl(\mathbf1_{s<r}-\vartheta(r)\bigr).
 \tag{MJ.31}
$$

For the full ordinary right side $F$ of (MJ.17), the same solution
is

$$
 \begin{aligned}
 r(r)={}&E_*(r)(1-\vartheta(r))b_0
       +H_*(r,R)\vartheta(r)b_R\\
       &+\int_0^R\mathcal K(r,s)F(s)\,ds
        +\sum_i\mathcal K(r,r_i)k_i.
 \end{aligned}
 \tag{MJ.32}
$$

At an atom, take the left value in the indicator for the left
trace and the right value for the right trace. The resulting jump
is exactly $k_i$. To prove (MJ.32), insert the complete terminal
variation-of-constants formula for $r_b$ into (MJ.27) and use
$r_c(r)/r_c(0)=E_*(r)(1-\vartheta(r))$. Thus every original atom
is carried by the same kernel, with no duplicate normalization.

Before the control support, (MJ.31) is the forward kernel from the
waist. After the support it is exactly the backward kernel from
the outer end: all earlier-source contributions cancel. In the
support it has the exact two weights $1-\vartheta$ and
$-\vartheta$. This cancellation must be taken before replacing the
two forward terms by separate absolute bounds. It does not make
the corresponding density-control column free in the nonmean rows.

## 7. A genuine coordinate reduction needs one shape slice

The representation (MJ.26) is redundant if $\eta$ is unrestricted.
Indeed let $\eta_c=\chi w$. For $p=f_m=b_0=b_R=0$, no jumps, and
$\eta=\eta_c$, the uncontrolled mean response is $r_b=r_c$.
Equation (MJ.27) then gives $\dot\xi=-1$, $r=0$ and
$\delta j=0$. This is a coordinate null vector, not a nontrivial
solution of the full linearized geometric problem.

An explicit bounded slice is available. Let $r_{0,\eta}$ be the
terminal, zero-jump scalar response in Section 4 to $(p,\eta)=(0,\eta)$,
and define

$$
 \ell(\eta)=r_{0,\eta}(0)/r_c(0).
 \tag{MJ.33}
$$

Then $\ell(\eta_c)=1$ and
$|\ell(\eta)|\le36.105\|\eta\|_{L^\infty_rL^2_\phi}$, by
(MJ.20) and (MJ.25). Hence

$$
              \eta=\eta_\perp+\ell(\eta)\eta_c,
               \qquad\ell(\eta_\perp)=0
 \tag{MJ.34}
$$

is a direct bounded decomposition. Use $\ker\ell$ for the
independent density shape, and the scalar $\dot\xi$ for its missing
direction. After (MJ.27), the full nonmean Jacobian must still
receive

$$
        \delta u=p,\qquad
 \delta v=j_*r+\frac{m_*}{m}
                     (\eta_\perp+\dot\xi\,\chi w).
 \tag{MJ.35}
$$

In particular (MJ.35), including its full control derivative,
must be substituted into both nonmean body equations, all nonmean
transmissions, the waist odd row, actual outer rows, and any
independent phase or height functional. The scalar estimates above
do not prove invertibility of those remaining rows or identify
their finite Schur matrix.

The fixed metric is unchanged in this construction. The actual
selected metric, regular cap, height and full nonlinear problem
remain separate obligations. The completed scalar inverse is a
usable component of that problem, not a relaxation of its
completion standard.

The rational constant comparisons in Sections 2--6 are reproduced
by
[`fourfold_codazzi_compact_mean_jacobian_saved_bounds.py`](../scripts/fourfold_codazzi_compact_mean_jacobian_saved_bounds.py).
It uses only the same complete small records as SR and the already
proved waist-radius bound; it evaluates no old numerical target.
