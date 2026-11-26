# R144 supplement: terminal mean small ball gives the normalized forward constant

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

This is a new small-scalar route to the compact mean root. It requires
neither recomputation nor completion of a forward W target. It consumes
the complete new C0/profile receiver, the already saved initial mean
difference, and optionally the old complete waist L2 source coefficient.
Every actual numerical gate remains the responsibility of a separate
public scalar consumer.

## TM1. Same fixed raw object and the zero-parameter terminal solution

Fix the original raw centre at eta0 and nu0. Keep all original pieces,
the same $u$ and $j=v/m$, and all actual mean jumps. Write
$n=a^2/m^2$, $D_0=1-n(0)$ and

$$
 c=2\beta U,\qquad
 H(r)=\exp\left(\int_0^r c(s)\,ds\right),\qquad H(0)=1 .
$$

The forward mean variable of RS/CD is the globally defined linear-ODE
solution

$$
 Y_f'=cY_f+2\beta Ka^2\left(1+V/m^2\right),\qquad Y_f(0)=1.
\tag{TM.1}
$$

Its existence as a real scalar function does not assume that it is
positive. Both $Y_f$ and $H$ are continuous across the original
candidate joins. The raw $n$ can jump.

At compact parameter $\xi=0$, use the actual CP constants and set

$$
 E_*=K_0R_*+K_JJ_*,\qquad
 S_0(b)=E_*+C_{10}b+C_{20}b^2+C_{30}b^3,\qquad
 L_0(b)=C_{10}+2C_{20}b+3C_{30}b^2 .
\tag{TM.2}
$$

If the saved actual scalars prove

$$
 0<b_0<m_*,\qquad S_0(b_0)\le b_0,\qquad L_0(b_0)<1,
\tag{TM.3}
$$

CP8 supplies a unique exact scalar solution $m_t=m+q_0<0$ in
$\|q_0\|_\infty\le b_0$, with $q_0(R)=0$ and
$[q_0]_i=-[m]_i$. In particular $m_t$ is continuous. Its positive
function

$$
 Y_t=a^2/m_t^2
$$

solves the same linear equation as (TM.1), and
$Y_t(R)=n(R)$. This follows from the exact fixed-density mean equation,
not from any approximate raw equation.

Let

$$
 \overline D=\frac{Y_f(R)-n(R)}{H(R)}.
$$

The difference $Y_f-Y_t$ solves the homogeneous equation with no
interface atoms. Therefore, exactly,

$$
 \boxed{
 \overline D
 =Y_f(0)-Y_t(0)
 =D_0+n(0)-\frac{a(0)^2}{(m(0)+q_0(0))^2}.
 }
\tag{TM.4}
$$

The original initial mismatch is present. So are the full raw ordinary
mean residual and all mean atoms: they entered the terminal problem
through $R_*$ and $J_*$ and the exact data in (TM.3).
There is no sign reversal or free terminal condition in (TM.4).

## TM2. A sharper waist value uses only an old complete scalar receiver

The whole bound $|q_0(0)|\le b_0$ is always available after (TM.3).
A sharper bound does not require an additional radial solve.

The old complete mean readable record contains the whole coefficient

`complete_waist_mean_gain_if_log_Gamma_below_100/ordinary_mean_source_L2_r`.

Call its valid upper $L_{w,2}$. It is a bound for the same original
operator $L_m$, including its actual multiplicative mean interfaces.
Its already published strict rational upper is $0.732535123$.
No new Gamma or kernel integral is evaluated here.

The raw ordinary source is $R_0=\langle R_v\rangle$, so its complete
piecewise $L^2_r$ norm is at most the actual physical raw second
residual bound

$$
 E_v=\alpha\,8.194504\,10^{-8}.
$$

The complete old residual note supplies this value at the same eta0,
nu0 and original raw candidate. It does not include the mean jumps;
those remain a separate contribution. Applying the waist receiver to
the raw source and the already proved complete C0 receivers to the
nonlinear sources in the true fixed point gives

$$
 |q_0(0)|
 \le B_w:=
 L_{w,2}E_v+K_JJ_*+
 C_{10}b_0+C_{20}b_0^2+C_{30}b_0^3.
\tag{TM.5}
$$

Consequently set

$$
 b_w=\min(b_0,B_w).
\tag{TM.6}
$$

This is a minimum of two valid bounds for the same true point value.
It is not a subtraction of unrelated norm uppers. Either the coarse
choice $b_w=b_0$ or the sharper choice (TM.6) is valid.

## TM3. Normalized endpoint error without new waist metric evaluation

Let $d_0$ bound the absolute value of the full saved initial $D_0$ ball.
The complete original forward run 45772466407/1 already saved that
ball. It is an initial-value enclosure over the original affine box
and hence encloses the fixed intrinsic centre. Only that field is read;
its already completed signed forward target is not rerun.

Take

$$
 t=\frac{b_w}{m_*}<1.
$$

At the waist, $|q_0(0)/m(0)|\le t$. Since $n(0)=1-D_0$,

$$
 Y_t(0)=n(0)\left(1+\frac{q_0(0)}{m(0)}\right)^{-2}.
$$

For every real $|x|\le t<1$,

$$
 |(1+x)^{-2}-1|
 \le(1-t)^{-2}-1
 =\frac{t(2-t)}{(1-t)^2}.
$$

Thus (TM.4) gives the complete bound

$$
 \boxed{
 |\overline D|
 \le d:=
 d_0+(1+d_0)\frac{t(2-t)}{(1-t)^2}.
 }
\tag{TM.7}
$$

All quantities in (TM.7) come from complete small scalar records.
The identity $Y_f(0)=1$ is the original RS initial condition;
it is not a reinitialization of the raw mean. The identity
$n(0)=1-D_0$ is exact for that same raw centre.

## TM4. A complete root and positive mean from one uniform parameter interval

The completed compact target supplies $\overline a>0$ and the
structural inequality
$0\le\overline b\le\overline a/2$. Let $a_-$ be the lower endpoint of
the full actual $\overline a$ ball. For an exact chosen $0<\rho<1$,

$$
 d<a_-\rho(1-\rho/2)
\tag{TM.8}
$$

gives the unique exact root of

$$
 \overline D-\overline a\,\xi-\overline b\,\xi^2=0
$$

in $[-\rho,\rho]$, by CD.16--21. The constant term need not have a
signed interval narrow enough to identify the root sign.

With that same $\rho$, form all four complete CP polynomials
$A_0(\rho),A_1(\rho),A_2(\rho),A_3(\rho)$. If

$$
\begin{aligned}
 0<b<m_*,\qquad
 E_*+A_0+A_1b+A_2b^2+A_3b^3&\le b,\\
 A_1+2A_2b+3A_3b^2&<1,
\end{aligned}
\tag{TM.9}
$$

then a strictly negative terminal mean with positive $Y$ exists for every
$|\xi|\le\rho$.
The exact scalar linear-ODE uniqueness argument in CR5 identifies
the root solution with the forward solution having waist value
$Y(0)=1$. In particular, its whole mean is positive in $Y$ coordinates
and equals $-a(0)$ at the waist, while its outer mean returns to
the original raw value.

The independent density inequality is

$$
 8\rho\sqrt{V_*}<g_*.
\tag{TM.10}
$$

It implies $j_\xi>0$ for the same entire parameter interval.
Neither (TM.9) nor (TM.10) is inferred from an inconclusive
direct interval lower bound for the old forward $Y_f$.

## TM5. Exact small-scalar selection and actual readback

A public consumer may choose its radii from the complete saved
upper bounds, and then independently verify every inequality.
For example, when $1-C_{10}^{+}>0$, take an exact rational
upper endpoint of

$$
 b_0^{\rm proposal}=\frac{17E_*^+}{16(1-C_{10}^+)}.
$$

It must still check (TM.3). After saving and reading back (TM.7),
take an exact rational upper endpoint of
$17d^+/(16a_-)$ as a proposed $\rho$.
It must still check (TM.8), $\rho<1$, and all density gates.

For the uniform ball one may analogously propose

$$
 b^{\rm proposal}=
 \frac{17(E_*+A_0)^+}{16(1-A_1^+)}
$$

when its denominator is positive, and then check both inequalities
in (TM.9). Subtracting a valid contraction upper from the exact
number one supplies a lower gap; it does not estimate an operator
difference by subtracting unrelated uppers.

Every proposed radius is a specified exact rational number.
Each derived whole scalar is saved and actually read back before
it is used by a subsequent dependent gate. A failed sufficient
inequality is retained as a failed test and does not prove that
the true scalar problem has no solution. No radius is silently
changed after a failed test.

The ordinary moving-field norm still needs its own check, for example

$$
 \|v_\xi-v\|_{L^\infty_rA_0}
 \le b\big(1+(1+\rho)8Z_*\big)+8\rho\sqrt{V_*}.
\tag{TM.11}
$$

Here $Z_*\ge\sup\sqrt V/|m|$ is the saved whole bound.
Using the actual compact profile can improve its last term, but
that is a different complete input. Even a passed (TM.11) is a
same-material-angle bound. Physical-angle composition, the full
ordinary/divergence residual in CS, all raw nonmean jumps,
selected design phase, radial cap jets and height remain independent
obligations.

This route, if its actual numerical gates pass, closes the scalar
mean construction for the original raw metric. It is not a complete
coupled inverse, an exact full Codazzi field, or the final closed
fixed-metric family.
