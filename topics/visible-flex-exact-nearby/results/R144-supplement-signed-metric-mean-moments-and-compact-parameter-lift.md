# R144 supplement: three signed metric-mean moments and a genuinely compact parameter lift

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved identities and a directed integral construction.** At the
actual compact centre, the fixed-terminal mean derivative for the
genuine intrinsic parameter $\nu$ is determined by three signed
compact moments. The unknown corrected mean cancels out of their
integrands. Existing completed compact moments and the saved
integrating-factor endpoint suffice for a new enclosure without
repeating the old mean retraction or its integrating-factor target.

Combining this true metric derivative with the already proved
density-control column produces a physical parameter lift supported
entirely in $[1/20,9/50]$. Subtracting its complete physical
differential from the true metric source leaves a mean-zero source
of moving degree at most 96, with every original interface source
retained. This is an exact source transformation, not a proof of the
remaining nonmean inverse or true physical Schur transversality.
The numerical signed enclosure is a separate new public Actions
target; this proof does not forecast its sign.

## 1. Fixed extrinsic coordinates and the true metric derivative

Use the same raw state, compact root and terminal graph as
[SR](R144-supplement-sharp-compact-root-from-completed-forward-mean.md),
[MJ](R144-supplement-compact-terminal-mean-Jacobian-and-two-endpoint-inverse.md)
and
[RI](R144-supplement-compact-mean-rank-one-interface-for-full-nonmean-inverse.md).
Set

$$
 U=\langle u^2\rangle,\quad V=\langle(v-m)^2\rangle,\quad
 q=V/m^2,\quad \lambda_*=1+\xi_*\chi,\quad
 J_*=\langle j_*^2\rangle=1+\lambda_*^2q.
 \tag{VM.1}
$$

The internal density parameter $\xi$ is distinct from the
intrinsic parameter $\nu$. The original metric bump and the
chosen density cutoff are the same scalar function $\chi$,
as specified in CD.5:

$$
 \chi(r)=4096t^6(1-t)^6,\quad
 t=(r-1/20)/(13/100),\quad 1/20<r<9/50,
 \tag{VM.2}
$$

and zero outside. Their two uses are different: changing $\nu$
changes the metric, whereas changing $\xi$ changes the density.

For the true intrinsic variation
$E_{\nu+s}=E_\nu e^{s\chi}$, with $a$ and $\beta=a'/a$ fixed, put

$$
 \rho=\frac{a'^2}{E_\nu}=\frac{\beta^2}{\gamma^2},\qquad
 \rho'=-2\beta a^2K,\qquad
 K_\nu=-K\chi+\frac{\beta}{2E_\nu}\chi'.
 \tag{VM.3}
$$

Consequently

$$
                    2\beta a^2K_\nu=(\rho\chi)'.
 \tag{VM.4}
$$

These are the original metric identities, also used in
[R147, NM.11--NM.14](R147-selected-negative-nu-source-and-complete-mean-row.md).
The use here is at the new **exact-mean compact centre**, not
at the selected approximate state in that theorem.

Hold the physical $u$ and density $j_*$ fixed while varying
$\nu$, and keep the outer mean fixed. Define

$$
 r_\nu=\partial_\nu m^t\big|_{\nu_0,\xi_*},\qquad
 L_*r_\nu=-\beta m_*^3J_*K_\nu,\qquad
 r_\nu(R)=0,\quad [r_\nu]_i=0.
 \tag{VM.5}
$$

This is a scalar terminal-graph derivative. It is not the
physical Gauss--Codazzi parameter response, whose uncontrolled
nonmean shape generally also changes.

## 2. Exact cancellation of the corrected mean in the signed waist pairing

Let

$$
 Y_*=\frac{a^2}{m_*^2},\qquad
 \tau_*=-\frac{2a^2}{m_*^3}>0,\qquad
 H(r)=\exp\int_0^r2\beta U,\qquad H(0)=1.
 \tag{VM.6}
$$

The exact mean equation gives
$Y_*'=2\beta UY_*+2\beta a^2KJ_*$. Its metric derivative
$y_\nu=\tau_*r_\nu$ therefore satisfies

$$
 y_\nu'=2\beta U y_\nu+(\rho\chi)'J_*,
 \qquad y_\nu(R)=0,\quad [y_\nu]_i=0.
 \tag{VM.7}
$$

Here $\tau_*$ is continuous because $m_*$ is continuous.
There is no residual correction in the coefficient of
$y_\nu$: the compact mean is an actual exact scalar solution.
The raw nonmean density and all its jumps remain in $J_*$.

At the selected compact root, $m_*(0)=-a_0$ and
$\tau_*(0)=2/a_0$. The complete terminal formula gives

$$
 \boxed{\quad
 \kappa_\nu:=r_\nu(0)
  =-\frac{a_0}{2}
       \int_{1/20}^{9/50}\frac{(\rho\chi)'J_*}{H}\,dr .
 \quad}
 \tag{VM.8}
$$

All factors $m_*^3$ have cancelled. The only state data in the
integral are the original $u,V,m$ and the known $\xi_*$.
In particular its evaluation does not require another solve
for $m_*$, another full forward endpoint, or a new nonmean PDE
response.

## 3. Radial integration by parts, including every raw nonmean jump

On the complete original partition, let the sum below range
over every original interface inside the compact window.
Since $\rho,\chi,H$ are continuous and $\chi$ vanishes at
both ends, piecewise integration by parts in (VM.8) gives

$$
 \kappa_\nu=\frac{a_0}{2}
 \left[
 \int_{1/20}^{9/50}\frac{\rho\chi}{H}
                  (J_*'-2\beta UJ_*)\,dr
 +\sum_i\frac{\rho(r_i)\chi(r_i)}{H(r_i)}[J_*]_i
 \right].
 \tag{VM.9}
$$

The sign of the jump term is positive: summing the piecewise
endpoint terms in $\int f'g$ gives $-\sum_i f_i[g]_i$.
In the present coordinates

$$
                      [J_*]_i=\lambda_*(r_i)^2[q]_i.
 \tag{VM.10}
$$

None of these jumps is the mean-response jump in (VM.5),
which is zero. Omitting (VM.10) when using (VM.9) would
change the exact pairing.

There is a second useful expression retaining the nonmean
residual explicitly. On every open piece put

$$
 R_v=(v_*)_r-F_2(Q_*,\nu_0),\qquad
 \mathcal F_j=R_v/m_* .
$$

The exact scalar mean makes $\langle R_v\rangle=0$.
The complete density identity is
$j_*'=(d_*j_*-\gamma u)_\phi+\mathcal F_j$,
where $d_*=-\beta I_\phi(u^2+Km_*^2j_*^2)$.
Angular integration by parts therefore yields

$$
 \begin{aligned}
 J_*'-2\beta UJ_*
 ={}&-\beta\bigl[
   \langle u^2j_*^2\rangle+UJ_*
    +Km_*^2(\langle j_*^4\rangle-J_*^2)\bigr]\\
 &-2\gamma\langle j_*u_\phi\rangle
       +2\langle j_*\mathcal F_j\rangle .
 \end{aligned}
 \tag{VM.11}
$$

The last term is not set to zero. Neither (VM.9) nor (VM.11)
is a monotonicity theorem.

For the rotation-invariant case $u=0$, $j_*=1$ and no
nonmean jumps, $H=1$, and (VM.8) is exactly
$-(a_0/2)[\rho\chi]_{1/20}^{9/50}=0$.
Both (VM.9) and (VM.11) give the same zero. Thus the sign
of $K$ on the support and the nonzero density-control pivot
do not imply $\kappa_\nu\ne0$.

## 4. Three new signed moments with the old positive moments reused

Define the three exact signed quantities

$$
 \begin{aligned}
 M_0&=-\int\frac{(\rho\chi)'(1+q)}H\,dr,\\
 M_1&=-\int\frac{(\rho\chi)'\chi q}H\,dr,\\
 M_2&=-\int\frac{(\rho\chi)'\chi^2q}H\,dr ,
 \end{aligned}
 \tag{VM.12}
$$

where all integrals in this section are over $[1/20,9/50]$.
Then the desired fixed-terminal derivative is exactly

$$
 \boxed{\quad
 \kappa_\nu=\frac{a_0}{2}
                (M_0+2\xi_*M_1+\xi_*^2M_2).
 \quad}
 \tag{VM.13}
$$

The completed CP moments already give

$$
 \overline a=2\int\rho'\chi q/H,\qquad
 \overline b=\int\rho'\chi^2q/H.
 \tag{VM.14}
$$

These two completed targets must be read, not recomputed.
For a new computation it suffices to form

$$
 I_U=\int\rho\beta U\chi/H,\qquad
 E_n=\int\rho q\,\chi^n\chi'/H\quad(n=0,1,2),\qquad
 A_3=\int\rho'\chi^3q/H.
 \tag{VM.15}
$$

The constant rotational part is integrated by parts once,
using only the continuous $H$:
$-\int(\rho\chi)'/H=-2I_U$. Hence

$$
 M_0=-2I_U-\overline a/2-E_0,\qquad
 M_1=-\overline b-E_1,\qquad M_2=-A_3-E_2.
 \tag{VM.16}
$$

Unlike integrating (VM.9), (VM.15) differentiates no
piecewise candidate data. Evaluating it on every original
piece therefore automatically retains the original raw
discontinuities; it does not require approximating or
deleting the jump sum in (VM.9).

### Complete directed evaluation from the saved original rows

On $[0,9/50]$ the already proved strict metric signs give
$\beta\ge0$, $U\ge0$. Thus $H$ is nondecreasing, and the
previously saved complete CP endpoint implies the rigorous
whole-window enclosure

$$
                     1\le H(r)\le H(9/50)_{\rm upper}.
 \tag{VM.17}
$$

The first new consumer uses this saved enclosure. It does
not solve the old $H$ equation again. Its width is retained
in every signed integral; a failed nonzero test is not
replaced by a midpoint estimate.

The original complete scalar-mean native has 7721 common
rows and 6143 original mean interfaces. Each row contains
whole-cell balls for $a,\beta,K,\gamma,m,U,V$. On an
original compact row these give

$$
 q=V/m^2,\quad \rho=\beta^2/\gamma^2,\quad
 \rho'=-2\beta a^2K
 \tag{VM.18}
$$

with their actual correlations safely enclosed by interval
arithmetic. The original affine input box is used only as
an enclosure of its fixed $\eta_0,\nu_0$ centre.

These particular saved fields are **function-value ranges**,
not balls around receiver upper bounds. In
[the original producer](../scripts/fourfold_codazzi_final_scalar_mean_cached.py),
the function *row_budget* obtains the full closed-cell cubic
Horner ranges from *polynomial_ranges*, then calls
[*scalar_mean*](../scripts/fourfold_codazzi_final_moving_strict_energy_v2.py).
That function constructs
$m=s+\alpha y^m$,
$U=(\alpha^2/2)\sum_{k=1}^{32}(y^o_k)^2$ and
$V=(\alpha^2/2)\sum_{k=1}^{32}(y^e_k)^2$
as complete Arb expressions and returns them without taking
an upper endpoint. The *actual_target* fields similarly
come from *target_values* as full $a,\gamma,\beta,K$ ranges.
The original *record* writes both directed endpoints of
each such value. The separately named
*ordinary_nonmean_L2_to_transformed_mean_rate*, which really
is an upper-bound receiver, is not used here. Restricting
the $U,V,\beta,-K$ ranges to their already proved nonnegative
half-line is valid; treating a receiver upper as a function
lower bound would not be.

For a subinterval $[s,t]$ within one such row, integrate
$\chi,\chi^3$ exactly as rational polynomials. For the
signed moments use the exact masses

$$
 \int_s^t\chi^n\chi'\,dr
   =\frac{\chi(t)^{n+1}-\chi(s)^{n+1}}{n+1}.
 \tag{VM.19}
$$

Any row crossing the maximum $r=23/200$ is split there.
On each resulting subinterval $\chi^n\chi'$ has one sign.
Thus multiplying its signed mass by the whole-cell ball
for $\rho q/H$ is a valid enclosure of the integral.
Without this sign split, multiplying a coefficient range
by a cancelling signed mass would be invalid.

For $I_U$ and $A_3$ use the nonnegative exact masses and
the whole-cell ranges of $\rho\beta U/H$ and $\rho'q/H$.
Sum all resulting interval contributions with directed
rounding. Equations (VM.16), the already proved
$-8\,10^{-13}<\xi_*<-7\,10^{-13}$, and the old waist-radius
interval then give a complete interval for (VM.13).
Only complete scalar integrals, their signed conclusion,
counts, parameters and hashes are published.

This method neither selects a sign for $E_n$ nor regards
an interval containing zero as proof of a zero derivative.
It provides a new signed enclosure of the same exact
quantity, independently of whether the first enclosure
separates zero.

## 5. A physical metric lift supported entirely in the compact window

Recall the existing nonzero density-control derivative

$$
 \kappa_0=\frac{a_0}{2}
                   (\overline a+2\xi_*\overline b)>0.
$$

The unique density-control coefficient which cancels the
true metric derivative of the waist mean is

$$
 t_\nu=-\frac{\kappa_\nu}{\kappa_0}
       =-\frac{M_0+2\xi_*M_1+\xi_*^2M_2}
                    {\overline a+2\xi_*\overline b}.
 \tag{VM.20}
$$

The factor $a_0/2$ cancels in this ratio. Set

$$
 h_\nu^c=(0,j_*r_\nu)+t_\nu h_c,\qquad
 s_\nu=r_\nu+t_\nu r_c.
 \tag{VM.21}
$$

Both $s_\nu(0)$ and $s_\nu(R)$ vanish, and its mean
response jumps vanish. Before $1/20$, both metric and
control forcing in the scalar equation vanish. The
homogeneous initial problem with $s_\nu(0)=0$ gives
$s_\nu=0$ there. After $9/50$, the same terminal argument
gives $s_\nu=0$. The explicit density-control term also
vanishes on both regions. Therefore

$$
 \boxed{\quad h_\nu^c=0
       \text{ on }[0,1/20]\cup[9/50,R].\quad}
 \tag{VM.22}
$$

This is stronger than a terminal-mean column merely
vanishing on the positive interval. It gives zero direct
waist, root and outer state/jet columns.

The original true physical metric source is
$F_\nu=\partial_\nu F(Q_*,\nu_0)$, with its full $K_\nu$,
$\gamma_\nu$ and primitive terms. The new ordinary source
for a remaining physical correction is

$$
             \widehat F_\nu=F_\nu-\mathcal D_*h_\nu^c.
 \tag{VM.23}
$$

The mean derivative identity gives

$$
 \langle(\widehat F_\nu)_2\rangle=0,\qquad
 P_{\ge97}\widehat F_\nu=0.
 \tag{VM.24}
$$

For the second identity, $Q_*,h_\nu^c$ have moving degree
at most 32; the complete physical differential has degree
at most 96 on this column, as in RI.6--RI.10. The true
$F_\nu$ is also a complete cubic/primitive expression
of degree at most 96. This support statement is made
before any density division or physical-angle composition.

On every original interface the corresponding right side
is exactly $-[h_\nu^c]_i$. Its mean is zero, but its
nonmean part need not vanish. These signed interface data
are part of (VM.23), and an ordinary $L^2$ norm does not
pay them. All local endpoint rows are unchanged by
(VM.22); a global height, frame or phase functional still
receives its original action on the compact lift.

The lifting operation is invertible at the level of the
full original equations: if $q_\nu$ is a true parameter
response, then $q_\nu-h_\nu^c$ has exactly the source
(VM.23), the stated interface data and the translated
functional rows. Adding the lift recovers $q_\nu$.
No unknown high response or negative-to-positive return
has been set to zero by the finite support of the source.

## 6. Relation to genuine transversality

The positive scalar $\kappa_0$ only permits (VM.20).
The signed value $\kappa_\nu$ only measures the genuine
metric's fixed-density terminal mean derivative. Neither
is the full physical parameter Schur determinant.

The actual nonmean inverse must still receive
$\widehat F_\nu$, every $-[h_\nu^c]_i$, the independent
physical mean/height data and all retained functional
rows. A true remaining output $b$ then evaluates the
complete reconstructed column, including $b[h_\nu^c]$.
This is the same full signed Schur pairing of RI.27--RI.32,
expressed after an exact compact lift.

In particular the old selected proposal $Z$, its source
discrepancy and the WVC hybrid-to-actual coefficient
difference are not replaced by this new column. The
fixed-metric exact family, full nonmean inverse, nonlinear
iteration, genuine cap/height matching and final geometric
conditions remain the original tasks.
