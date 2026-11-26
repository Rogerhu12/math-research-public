# R144 supplement: complete C0 mean receiver and compact normalized moments

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Analytic receiver, using an already saved complete Green row bound.**
This note identifies the original whole-body kernel row integrals as
$L^\infty\to C^0$ receivers and gives a complete nonlinear small-ball
criterion for the compact density construction. It also reduces the new
compact moments to positive integrals on $[1/20,9/50]$. No new numerical
value, passed small-ball gate, or completed scientific run is asserted.

The input is the original full ac1 raw centre at $\nu_0$, with the fixed
intrinsic centre $\eta_0$ and all 6143 original interfaces. It is not the
selected continuous $Q_{\delta_*}$. The original full affine box may be
used only with its original centre and parameter convention verified;
its valid enclosure then also encloses the fixed intrinsic centre.
This use does not turn a full-box bound into a sharp point carrier.

## CR1. The old complete scalar Green already saved the required row integrals

Use the definitions in
[the full mean proof](R133-supplement-complete-mean-triangular-Green-and-cached-consumer.md)
and its
[actual completed result](R133-supplement-actual-final-complete-mean-Green.md).
The complete original native is

$$
\texttt{e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b}.
$$

It contains 7721 closed common cells and 6143 actual mean interfaces.
Its original producer
[fourfold_codazzi_final_scalar_mean_cached.py](../scripts/fourfold_codazzi_final_scalar_mean_cached.py)
has already saved

- `complete_triangular_Schur_integral_upper.mean_source_row`;
- `complete_triangular_Schur_integral_upper.nonmean_row`;
- `complete_log_Gamma_upper`;
- the original complete interface records.

These saved whole scalars are read, not recomputed. Write them as
$\mathcal R_m,\mathcal R_{\rm nm},\log\Gamma$. If $I_i$ has length
$\ell_i$, the producer's exact meanings are

$$
\begin{aligned}
 \mathcal R_m&\ge
 \max_i b_i\sum_{j\ge i}\ell_j t_j,\\
 \mathcal R_{\rm nm}&\ge
 \max_i b_i\sum_{j\ge i}\ell_j e_j,\\
 b_i&\ge\sup_{I_i}\tau^{-1},\qquad
 t_i\ge\sup_{I_i}\tau,\\
 e_i&\ge\sup_{I_i}
       4|\beta|n\sqrt{U+K^2V},
 \qquad n=a^2/m^2,\quad \tau=-2a^2/m^3>0,\\
 U&=\langle u^2\rangle,\qquad V=\langle(v-m)^2\rangle.
\end{aligned}
\tag{CR.1}
$$

Every angular norm below uses the normalized circle measure. The physical
frequency is $4k$. The quantities in (CR.1) concern the full angular input
space; a finite unknown Fourier cutoff is not introduced.

The actual original bound is $\Gamma<1.013237$. The displayed old
number $0.538112$ is an $L^2\to L^2$ bound. It is not substituted for
either of the new receivers

$$
 K_0=\Gamma\mathcal R_m,\qquad
 K_1=\Gamma\mathcal R_{\rm nm}.
\tag{CR.2}
$$

Their numerical values must be read from the full saved native and
multiplied with directed rounding if a numerical gate uses them.

## CR2. Exact scalar operator, all original jumps, and the C0 proof

Let

$$
\begin{aligned}
 R_0&=m'-\beta m(1-U-KV-Km^2),\\
 L_m q&=q'-a_m q,\qquad
 a_m=\beta(1-U-KV-3Km^2),\\
 \widetilde c&=2\beta(U+KV)-3R_0/m.
\end{aligned}
\tag{CR.3}
$$

On every open original piece,

$$
 \frac{\tau'}{\tau}+a_m=\widetilde c.
\tag{CR.4}
$$

At an original mean jump,

$$
 T_i=\frac{\tau_i^+}{\tau_i^-}
     =\left(\frac{m_i^-}{m_i^+}\right)^3.
\tag{CR.5}
$$

Thus the physical scalar homogeneous propagator for $L_m$ is bounded by

$$
 0<H_m(r,s)\le \Gamma\,\tau(r)^{-1}\tau(s),
 \qquad 0\le r\le s\le R.
\tag{CR.6}
$$

The factors $T_i^{-1}$ in the backward transformed propagator are exactly
those already included in $\Gamma$. They are not deleted. Formula
(CR.6) also follows directly by transforming $y=\tau q$, retaining
(CR.5), and using the complete negative-part and mean-jump bound in the
old proof.

For $q(R)=0$, $L_mq=f$, and specified physical response jumps
$[q]_i=k_i$, variation of constants gives

$$
 q(r)=-\int_r^R H_m(r,s)f(s)\,ds
      -\sum_{r<r_i\le R}H_m(r,r_i^-)\,k_i.
\tag{CR.7}
$$

The one-sided convention in each atom must match its homogeneous
propagator. Equivalently one may inject $\tau_i^+ k_i$ into the
transformed right-hand state and propagate through $T_i^{-1}$.

The ordinary-source part of (CR.7) satisfies

$$
 \|q_f\|_{L^\infty_r}\le K_0\|f\|_{L^\infty_r}.
\tag{CR.8}
$$

Indeed, integrate (CR.6) cell by cell and use the first row sum in
(CR.1). The full cell containing $r$ overestimates its actual terminal
subinterval, which is valid for an upper bound.

For the full nonmean forcing

$$
 f_{\rm nm}=-2\beta m
       \langle u\,h_u+K(v-m)h_v\rangle,\qquad \langle h_v\rangle=0,
$$

normalized angular Cauchy--Schwarz gives

$$
 \|\mathcal G_{\rm nm}(h_u,h_v)\|_{L^\infty_r}
 \le K_1\|(h_u,h_v)\|_{L^\infty_rL^2_\phi}.
\tag{CR.9}
$$

This is precisely the second row sum in (CR.1), since
$\tau(-2\beta m)=4\beta n$. It does not change the old kernel.

A sufficient complete jump receiver is

$$
 K_J=\Gamma
 \max_{\text{interface }j}
  \left(t_j^+\max_{\text{cells strictly left of }r_j}b_i\right),
 \qquad
 \|q_{\rm jumps}\|_\infty\le K_J\sum_j|k_j|.
\tag{CR.10}
$$

Here $\Gamma$ is the complete backward negative-log and multiplicative
majorant, including the terminal interface $j$ itself. In the transformed
jump formula the injection $\tau_j^+ k_j$ crosses $T_j^{-1}$, and that
factor is already paid by this choice of $\Gamma$. Merely substituting
$\tau_j^+$ for the left trace $\tau_j^-$ in (CR.6) would not justify
(CR.10).

The $t_j^+$ may be bounded using the already saved right cell's
$\tau$ upper bound. This finite maximum, if not previously saved for
this receiver, is a new inexpensive scalar consumption of the old
complete rows. It is not a rerun of the old Green integral or of any
intrinsic carrier.

For the actual mean-correcting response $q=m_{\rm new}-m$, continuity
of the new mean requires

$$
 [q]_i=-[m]_i.
\tag{CR.11}
$$

These are genuine source atoms. Their sum is not set to zero. One may
read their exact absolute values from the original interface records.
Alternatively, if $M\ge\sup|m|$, the already paid logarithmic jump
quantity yields

$$
 \sum_i|[m]_i|
 \le \frac{M}{3}J_m,\qquad
 J_m=3\sum_i\frac{|[m]_i|}
                    {\min(|m_i^-|,|m_i^+|)}
 <1.169345\,10^{-18}.
\tag{CR.12}
$$

The very small size of (CR.12) does not authorize omitting (CR.10).

## CR3. Compact density change and exact nonlinear mean equation

Use the same admissible compact window and normalized bump as in
[the compact quadratic construction](R144-supplement-compact-density-quadratic-mean-compensator.md):

$$
 I=[1/20,9/50],\quad
 \chi(r)=4096t^6(1-t)^6,\quad
 t=\frac{r-1/20}{13/100}
 \quad(r\in I),
$$

and $\chi=0$ elsewhere. Thus $0\le\chi\le1$, $\chi\in C^5$,
and its first five endpoint derivatives vanish.

Put

$$
 z=\frac{v-m}{m},\quad
 e=\xi\chi,\quad\lambda=1+e,\quad
 j_\xi=1+\lambda z,\qquad
 v_\xi=(m+q)j_\xi,\qquad u_\xi=u.
\tag{CR.13}
$$

At this stage $\xi$ is any fixed real number. Both its sign and its
whole allowed interval will be retained. The mean equation for
$m+q$ is exactly

$$
 (m+q)'=\beta(m+q)
 \left[1-U-KJ_\xi(m+q)^2\right],
 \qquad
 J_\xi=1+\lambda^2V/m^2.
\tag{CR.14}
$$

Subtract the raw equation in (CR.3). The full change of its nonmean
part is

$$
 h_v=(v_\xi-\langle v_\xi\rangle)-(v-m)
     =z(\lambda q+em),
 \qquad \langle h_v\rangle=0.
\tag{CR.15}
$$

No angular derivative or variation of $\chi$ is needed in this mean
identity. Direct expansion gives the exact decomposition

$$
\begin{aligned}
 L_mq={}&-R_0
        -2\beta K V(\lambda q+em)
        -\beta K\,\mathcal N_\xi(q),\\
 \mathcal N_\xi(q)={}&
        mV e^2+V(4e+3e^2)q
        +J_\xi(3mq^2+q^3).
\end{aligned}
\tag{CR.16}
$$

The second term in the first line is exactly the old nonmean forcing
in (CR.9) with $h_u=0$ and $h_v$ from (CR.15). In particular the
fixed-density kernel difference $-2\beta KVq$ has not been ignored:
it is represented as a full old-operator feedback input.

For $\xi=0$, (CR.16) reduces to

$$
 L_mq=-R_0-2\beta KVq
       -\beta K(1+V/m^2)(3mq^2+q^3).
\tag{CR.17}
$$

This explains why the old scalar inverse can be reused, but cannot be
declared identical to the new fixed-density scalar inverse.

## CR4. A uniform complete nonlinear C0 small-ball criterion

Choose a parameter interval $|\xi|\le\rho<1$ and a mean radius $b>0$.
Suppose the following actual whole-body bounds are available:

$$
\begin{aligned}
 m_*&\le\inf|m|,\qquad M\ge\sup|m|,\qquad
 V_*\ge\sup V,\\
 Z&\ge\sup\frac{\sqrt V}{|m|},\qquad
 B\ge\sup|\beta K|,\qquad
 R_*\ge\|R_0\|_\infty,\qquad
 J_*\ge\sum_i|[m]_i|.
\end{aligned}
\tag{CR.18}
$$

They may be valid enclosing bounds over the original affine box,
provided that the fixed centre is in that original box. Actual
positive endpoints must be used for all denominator operations.
No cancellation-dependent derivative is estimated here.

Define

$$
\begin{aligned}
 \mathcal J_\rho&=1+(1+\rho)^2 Z^2,\\
 E_*&=K_0R_*+K_JJ_*,\\
 S(b,\rho)&=E_*+
 K_1\big((1+\rho)Zb+\rho\sqrt{V_*}\big)\\
 &\quad+K_0B\left[
 MV_*\rho^2+V_*(4\rho+3\rho^2)b
 +\mathcal J_\rho(3Mb^2+b^3)\right],\\
 L(b,\rho)&=K_1Z(1+\rho)
 +K_0B\left[
 V_*(4\rho+3\rho^2)
 +\mathcal J_\rho(6Mb+3b^2)\right].
\end{aligned}
\tag{CR.19}
$$

The ordinary nonlinear coefficient may also be paid by a tighter complete
weighted-source receiver. With the same original cells and complete
$\Gamma$, define the genuinely new row bound

$
 K_{\beta K}\ge
 \Gamma\max_i b_i
       \sum_{j\ge i}\ell_j t_j\sup_{I_j}|\beta K|.
 \tag{CR.19a}
$

The same cellwise proof as (CR.8) gives
$\|L_m^{-1}(\beta K f)\|_\infty\le K_{\beta K}\|f\|_\infty$,
with zero terminal data and zero response jumps. All transformed
coefficient jumps are still paid by the same $\Gamma$.
Consequently every occurrence of $K_0B$ in both $S$ and $L$ may
consistently be replaced by
$K_2=\min(K_0B,K_{\beta K})$, if both complete bounds are available.
This does not assume a sign cancellation or remove the separate fixed
jump source. Computing this new weighted row maximum from the saved
complete cells is a new receiver target; it does not repeat the already
saved unweighted row integrals or the original $\Gamma$ computation.

If

$
 b<m_*,\qquad S(b,\rho)\le b,\qquad L(b,\rho)<1,
\tag{CR.20}
$$

then, for every $|\xi|\le\rho$, (CR.14) has a unique solution in
$\|q\|_\infty\le b$ with $q(R)=0$ and jumps (CR.11).
Its mean $m+q$ is continuous across all original interfaces and
strictly negative on the whole body.

**Proof.** Apply the exact inverse (CR.7) to (CR.16), with the fixed
jump data (CR.11). This defines a map on the closed $L^\infty$ ball
$\|q\|_\infty\le b$. The ordinary source and jump terms give $E_*$.
Equation (CR.15) gives

$$
 \|h_v\|_{L^\infty_rL^2_\phi}
 \le (1+\rho)Zb+\rho\sqrt{V_*}.
$$

Further, $J_\xi\le\mathcal J_\rho$ and

$$
 \|\mathcal N_\xi(q)\|_\infty
 \le MV_*\rho^2+
 V_*(4\rho+3\rho^2)b+
 \mathcal J_\rho(3Mb^2+b^3).
$$

These are precisely the terms of $S$. The nonmean input in (CR.15)
has Lipschitz constant $(1+\rho)Z$. The remaining polynomial has
Lipschitz constant

$$
 V_*(4\rho+3\rho^2)+
 \mathcal J_\rho(6Mb+3b^2).
$$

Thus the map has Lipschitz constant at most $L$. The contraction theorem
gives a unique fixed point. The integral representation supplies
piecewise absolute continuity and the specified jumps. The cancellation
of those jumps in $m+q$ is exact, and $b<m_*$ gives strict negativity.
This proves the assertion without assuming the forward $Y$ enclosure
is already positive. $\square$

The result is uniform over the whole chosen interval $[-\rho,\rho]$.
It is not a claim that (CR.20) has numerically passed for the current
centre. A scientific consumer must read back all complete output
scalars and verify the inequalities before making that claim.

## CR5. Positivity, closeness, and identification with the forward quadratic root

Let the actual raw field satisfy $v\le-g_*<0$. A sufficient independent
density gate is

$$
 8\rho\sqrt{V_*}<g_*.
\tag{CR.21}
$$

Indeed the raw nonmean part has 32 cosine modes, so
$\|v-m\|_{A_0}\le\sqrt{64V}\le8\sqrt{V_*}$. The numerator
$v+\xi\chi(v-m)$ of $j_\xi$ is negative by (CR.21); its denominator
$m$ is negative. Thus $j_\xi>0$ on every whole cell. This argument
does not infer density positivity from mean positivity.

The fixed point from CR4 therefore gives $v_\xi<0$. Its function

$$
 Y_\xi=\frac{a^2}{(m+q)^2}>0
$$

solves exactly

$$
 Y_\xi'=2\beta UY_\xi+2\beta Ka^2
       \left(1+(1+\xi\chi)^2V/m^2\right),
 \qquad Y_\xi(R)=n(R).
\tag{CR.22}
$$

The forward construction in the compact proof starts instead at
$Y_\xi(0)=1$ and gives
$Y_\xi(R)-n(R)=D_R+\xi A_R+\xi^2B_R$.
If its certified small root is $\xi_*$, uniqueness for this scalar
linear equation implies that the forward function and the positive
terminal solution (CR.22) are the same whole function. In particular
(CR.20)--(CR.21) can prove positivity of the root solution even when
a direct forward interval enclosure of $Y_0$ is inconclusive.

Let

$$
 Z_A\ge\sup\|z\|_{A_0};
 \quad\text{for example } Z_A=8\sqrt{V_*}/m_*.
$$

The full moving-field change satisfies

$$
 \|v_\xi-v\|_{L^\infty_rA_0}
 \le b\big(1+(1+\rho)Z_A\big)+8\rho\sqrt{V_*},
 \qquad u_\xi=u.
\tag{CR.23}
$$

This bound controls the actual full nonmean change as well as the
mean. It is not obtained by declaring the new $j$ fixed.
The material angle changes in the compact window by

$$
 \Theta_\xi-\Theta=\xi\chi\,\mathcal I z,\qquad
 \|\Theta_\xi-\Theta\|_\infty\le\rho Z_A/4.
\tag{CR.24}
$$

For comparison at fixed physical angle, the inverse-chart
composition term from CD.26--29 must also be paid. Formula (CR.23)
alone is a moving-coordinate bound.

At the outer root, $\chi=0$ near $R$, $q(R)=0$, and therefore the entire
outer moving state, its material angle, and its physical $B/C$ point
values agree exactly with the raw input. Its radial derivative need
not agree: the original mean residual remains in
$m_\xi'(R)-m'(R)=-R_0(R)$.

None of (CR.20)--(CR.24) repairs the raw nonmean interface jumps,
solves the ordinary nonmean equations, or supplies the selected
design phase. The exact changed residual formulas CD.33--40,
including the term $\xi\chi' z$, remain mandatory.

## CR6. Compact normalized moments need no whole-body primitive reconstruction

Let $H$ denote the forward homogeneous factor for the new scalar
equation, to distinguish it from the old majorant $\Gamma$:

$$
 H(r)=\exp\left(\int_0^r2\beta U\,dt\right)>0.
\tag{CR.25}
$$

The full fixed-density scientific consumer already propagates this
quantity as its whole state $G$; a complete endpoint record therefore
contains $H_R$ together with the signed complete $D_R$.
The correct scalar for the compact equation is

$$
 \overline D=\frac{D_R}{H_R},
 \qquad
 \overline a=-\frac{A_R}{H_R}
   =4\int_I\frac{-\beta Ka^2V}{m^2H}\chi\,dr,
 \qquad
 \overline b=-\frac{B_R}{H_R}
   =2\int_I\frac{-\beta Ka^2V}{m^2H}\chi^2\,dr.
\tag{CR.26}
$$

The normalized endpoint equation is exactly

$$
 \overline D-\overline a\,\xi-\overline b\,\xi^2=0,
 \qquad 0\le\overline b\le\overline a/2.
\tag{CR.27}
$$

All the original initial mismatch, signed ordinary mean source, and
6143 mean atoms remain inside the actual saved $D_R$. A small waist
mismatch is not substituted for it.

The strict-negative certificate
[SP actual](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md)
covers $[0,2333968743003/10^{13}]$, which contains $I$.
For the actual controlled metric it gives $K<0$ there. From
$(a'/\sqrt{E_\nu})'=-a\sqrt{E_\nu}K$ and $a'(0)=0$,
$\beta>0$ for $r\in I$. Consequently all integrands in (CR.26)
are nonnegative. Positivity of $\overline a$ still requires an actual
positive amount of $V$ in the compact window.

Only the existing complete row carriers for $0\le r\le9/50$ are
needed to enclose (CR.26):

1. Read the original rows and their exact endpoints, preserving the
   old native identity and the fixed-centre membership in its affine box.
2. Propagate $H$ on this prefix using $c=2\beta U\ge0$. Full original
   row enclosures are valid; no signed near-cancellation is involved.
3. On each row meeting $I$, form a positive enclosure of
   $P=4(-\beta K)a^2V/(m^2H)$ using positive endpoint reciprocals.
   The original row width need not be refined merely to reproduce
   an old target.
4. Integrate the fixed polynomials $\chi$ and $\chi^2$ exactly on
   each intersected row. If $P_i^-\le P\le P_i^+$ then

$$
 P_i^-\int_{I_i\cap I}\chi
 \le\int_{I_i\cap I}P\chi
 \le P_i^+\int_{I_i\cap I}\chi,
\tag{CR.28}
$$

and the same formula with $\chi^2/2$ encloses $\overline b$.

The support edges $1/20,9/50$ are exact mandatory cuts.
Within the compact window, the original nonnegative variance $V$
is a finite candidate quantity, independent of the affine target
parameter. It is never replaced by an unsigned bound for the old
signed mean residual.

A strict lower bound may integrate any specified subcollection of
whole rows where $V$ has a positive lower bound; the omitted
integrand is nonnegative. An upper bound must cover the full support.
These are genuinely new compact moments. The old full-eta forward
retraction and its completed unknown gates remain frozen.

If the complete actual endpoint readback gives
$|\overline D|\le d$ and the new compact result gives
$\overline a\ge a_->0$, then

$$
 d<a_-\rho(1-\rho/2),\qquad 0<\rho<1
\tag{CR.29}
$$

proves a unique root in $[-\rho,\rho]$, by CD.15--20.
The same $\rho$ must be used in the nonlinear and density gates
(CR.20)--(CR.21). If the interval division $D_R/H_R$ is wide, the
output remains a valid enclosure and its unresolved gate is retained;
no point midpoint substitutes for it.

## CR7. The root correction is a normalized positive-mass profile

For any fixed $|\xi|<1$ define

$$
 d\mu_\xi(s)=
 \frac{4(-\beta K)a^2V}{m^2H(s)}
 \chi(s)\left(1+\frac{\xi}{2}\chi(s)\right)\,ds.
\tag{CR.30}
$$

This measure is nonnegative and supported on $I$. If
$\overline a>0$ then its total mass is strictly positive. Put

$$
 F_\xi(r)=\frac{\mu_\xi([0,r])}{\mu_\xi([0,R])}.
$$

It satisfies $0\le F_\xi\le1$, is nondecreasing, is zero before
$1/20$, and is one after $9/50$. At a nonzero root $\xi_*$,
the whole scalar correction has the exact form

$$
 Y_{\xi_*}(r)-Y_0(r)
 =-D_R\,\frac{H(r)}{H_R}\,F_{\xi_*}(r).
\tag{CR.31}
$$

This follows from
$\xi A(r)+\xi^2B(r)=-\xi H(r)\mu_\xi([0,r])$
and the endpoint root equation
$D_R=\xi H_R\mu_\xi([0,R])$.
If the root is zero then $D_R=0$ and the correction is identically zero.

In particular,

$$
 |Y_{\xi_*}(r)-Y_0(r)|
 \le |D_R|\frac{H(r)}{H_R}.
\tag{CR.32}
$$

This whole-profile bound does not require unrelated absolute upper
bounds for $A$ and $B$. After the compact support it gives the exact
terminal subtraction
$Y_{\xi_*}=Y_0-H(r)D_R/H_R$ already identified in CD.31.
It does not erase any old signed residual or mean atom.

The nonmean change, the angle change, all raw jumps, the physical
outer derivative and cap data, and the true design phase are still
those explicitly retained above and in the compact construction.
The present result supplies a concrete small-ball route for the
scalar mean part; it is not the whole coupled inverse or the
nonlinear closed-surface completion.
