# R133 supplement: finite193, the middle band, and the genuine infinite collar trace

2026-11-15. Analytic trace interface for one actual two-sided state.
This note consumes ordinary body norms and ordinary residual norms. It
does not infer a body solution or a nonlinear matching from an operator
gain. The finite cut, the intermediate angular band and the infinite
tail are kept separately.

The energy identity is
[E](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md).
The complete source identity is
[MC](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md),
and the available true-solution high window is precisely the five
corrected cases in
[MA](R133-supplement-actual-raw-mean-fee-and-restored-high-collar-domain.md).
No old numerical calculation is repeated in this proof.

## 1. Same state, same angle, and exact source units

Take the true positive collar
$$
 I=[c-2\ell,c+2\ell],\qquad c=9/10,
 \qquad P=\operatorname{diag}(K^{-1/4},K^{1/4}).        \tag{LT.1}
$$
Both sides belong to one real continuous $H^1$ moving state $Q$.
The reference is the same continuous selected state $Q_\delta$, with
the same intrinsic coefficients. Define
$$
 h=Q-Q_\delta,\quad z=Ph,\quad W^0=PQ_\delta,\quad
 F=P(f-f_\delta),                                    \tag{LT.2}
$$
where $f$ is the actual ordinary residual of $Q$. Its value is not set
to zero for an approximate iterate.

Angular measure is $(2/\pi)d\phi$ and radial measure is $dr$.
For signed quarter index $j$, the physical frequency is $4j$ and
$$
 \Lambda_j=\sqrt{1+16j^2},\quad
 \Pi_J=\mathbf1_{\{|j|\le J\}},\quad H_J=I-\Pi_J.
                                                               \tag{LT.3}
$$
The reflection restriction has 193 coordinates in $\Pi_{96}$: 96 odd
first-component coordinates and the complete 97 even second-component
coordinates, including its mean. Proofs before this restriction use
the full signed circle. Neither scalar mean is removed from the
equation.

Use actual coefficient bounds from E.9 and E.14:
$a\ge a_->0$, $|d|\le d_+$, $|a_r/a|\le L$,
$|\alpha|\le\alpha_+$, $|b|\le b_+$, $|g|\le g_+$,
$|W^0|\le M_0$, $|W^0_\phi|\le M_1$,
$|W^0_{\phi\phi}|\le M_2$, and $|z|\le\eta$.
Set $M=M_0+\eta$ and
$$
\begin{aligned}
 c_p&=2/a_-,&c_r&=1+2d_+/a_-,&
 D_1&=2b_+M^2,\\
 A_0&=\alpha_++3b_+M^2+(b_+M/2+g_+)M_1,\\
 A_1&=\alpha_++5b_+M^2,&
 B_{10}&=8b_+MM_1+(b_+M/2+g_+)M_2 .
\end{aligned}                                                   \tag{LT.4}
$$
Thus $|d_\phi|\le D_1$. The factor $L$ includes the independent actual
residual mean $\langle f_2\rangle/m$ in E.7. In particular an ordinary
$L^2$ residual alone does not supply this radial $L^\infty$ coefficient
bound. For the true solutions covered by MA, $f=0$ and the already
paid true-solution value of $L$ applies.

## 2. A projected first energy with no unknown angular derivative on the right

Write $\mathcal L=\partial_r-d\partial_\phi+aJ_0\partial_\phi$.
Since $a$ is radial and $P,\Pi_J,H_J$ commute,
$$
 \mathcal L H_Jz
 =H_J(\mathcal Lz)+[H_J,d]z_\phi .                    \tag{LT.5}
$$
The commutator is exactly
$$
 [H_J,d]z_\phi
 =H_Jd(\Pi_Jz)_\phi-\Pi_Jd(H_Jz)_\phi .
$$
For $N_J=4J$, its low leg is bounded by
$N_Jd_+\|\Pi_Jz\|_2$. In the high leg integrate the angular derivative
onto the finite output:
$$
 -\Pi_Jd(H_Jz)_\phi
 =-\partial_\phi\Pi_J(dH_Jz)+\Pi_J(d_\phi H_Jz).
                                                               \tag{LT.6}
$$
Its bound is $(N_Jd_++D_1)\|H_Jz\|_2$. No infinite high angular
derivative has been assumed bounded in this step.

Put
$$
 Z_{\le J}=\|\Pi_Jz\|_{L^2(I)},\quad
 Z_{>J}=\|H_Jz\|_{L^2(I)},\quad
 Z=(Z_{\le J}^2+Z_{>J}^2)^{1/2},\quad
 F_J=\|H_JF\|_{L^2(I)} .
$$
Choose a real radial cutoff $\chi$ supported in $I$, equal to one on
$I_1=[c-\ell,c+\ell]$, with $|\chi'|\le\ell^{-1}$.
E.13--E.15, (LT.5)--(LT.6), and E.11 give
$$
\begin{split}
 E_J={}&F_J+A_0Z+N_Jd_+Z_{\le J}\\
       &+(N_Jd_++D_1+L+\ell^{-1})Z_{>J},\\
 \|\partial_\phi(\chi H_Jz)\|_2&\le c_p E_J,\qquad
 \|\partial_r(\chi H_Jz)\|_2\le c_r E_J .
\end{split}                                                   \tag{LT.7}
$$
The full $Z$ in $A_0Z$ includes the mean and both low components.
The rank-one principal-mean term of E.13 is included in $A_0$.
A smaller rigorously proved upper bound for the first line of (LT.7)
may be used in the same two conclusions.

## 3. Half a derivative at the cut, with the exact endpoint factor

For a Hilbert-valued Fourier coefficient $u_j$ that vanishes at both
ends of $I$, average the left and right fundamental-theorem identities.
The result is
$$
 |u_j(c)|^2
 \le\int_I |u_j(r)|\,|u'_j(r)|\,dr.                  \tag{LT.8}
$$
There is no extra factor two. Summing with the full physical weight
$\Lambda_j$ and using Cauchy--Schwarz yields
$$
 \|u(c)\|_{H^{1/2}_\phi}^2
 \le\|\Lambda u\|_{L^2(I)}\|u_r\|_{L^2(I)}.           \tag{LT.9}
$$
For $u=\chi H_Jz$ the smallest physical frequency is $4(J+1)$.
Hence, with
$$
 \kappa_J=\sqrt{1+[4(J+1)]^{-2}},\qquad
 p_c=\max\{K(c)^{1/4},K(c)^{-1/4}\},
$$
we have $\|\Lambda u\|_2\le\kappa_J\|u_\phi\|_2$. Therefore
$$
 \boxed{\ \|H_Jh(c)\|_{H^{1/2}}
 \le V_J:=p_c\sqrt{\kappa_Jc_pc_r}\,E_J.\ }            \tag{LT.10}
$$
The raw trace is recovered by the single factor $p_c$.
The radial scaling does not change angular support or the normalization
of the even mean.

This bound needs only the ordinary $H_JF$ in $L^2$. It applies before
the residual is zero, subject to the stated actual mean-speed bound.
It is an interior estimate for a common two-sided state, not a
regularity statement for arbitrary data prescribed on one side of
the cut.

## 4. Two exact finite-band cancellations above 288

For the selected reference $Q_\delta=Q_0+\delta Z$, the continuous
centre has angular degree 32 and the continuous response has degree 96.
All their repairs are within these same finite angular supports.
Thus $W^0$ has degree at most 96. Put
$$
 d^0=-bI_\phi|W^0|^2.
$$
The exact linear coefficient operator obtained from E.13 at $z=0$ is
$$
\begin{split}
 A^*u={}&\alpha Du
 -b\{|W^0|^2u+2W^0(W^0\cdot u)\}\\
 &-2bW^0_\phi I_\phi(W^0\cdot u)
       +g\langle u_2\rangle J_0W^0_\phi .             \tag{LT.11}
\end{split}
$$
Its non-rank Fourier bandwidth is at most 192. The rank-one output
has degree at most 96. The primitive removes its zero mode and never
increases support. Consequently the following identities are exact:
$$
 H_{288}A^*\Pi_{96}=0,\qquad
 H_{288}d^0\partial_\phi\Pi_{96}=0.                   \tag{LT.12}
$$
Both signs of the Fourier indices and the full mean input are included.
This uses the actual finite reference, not a truncation of the unknown
state.

Write the right side of E.13 as $A(z)z+F$. Direct subtraction gives
$$
\begin{split}
 [A(z)-A^*]u
 ={}&-b\{(2W^0\cdot z+|z|^2)u+W^0(z\cdot u)\}\\
    &-bW^0_\phi I_\phi(z\cdot u).
\end{split}
$$
The exact $L^2$ primitive norm is $1/4$, so
$$
 \|A(z)-A^*\|_{2\to2}\le
 a_\Delta:=b_+\eta(3M_0+\eta+M_1/4).                 \tag{LT.13}
$$
The normalized inverse-derivative kernel on the circle of length
$\pi/2$ has $L^1$ norm $\pi/8<1/2$. Therefore
$$
 \|d-d^0\|_\infty\le
 d_\Delta:=\tfrac12b_+(2M_0+\eta)\eta.                \tag{LT.14}
$$
The $1/4$ in (LT.13) is an $L^2$ operator norm; it is not substituted
for the $L^\infty$ bound used in (LT.14).

Let
$$
 Z_L=\|\Pi_{96}z\|_2,\quad
 Z_M=\|(\Pi_{288}-\Pi_{96})z\|_2,\quad
 Z_F=\|H_{288}z\|_2,\quad
 Z_H=(Z_M^2+Z_F^2)^{1/2}.
$$
An admissible replacement for $E_{288}$ in (LT.7)--(LT.10) is
$$
\begin{split}
 E_F={}&F_{288}+A_*Z_H+a_\Delta Z+384d_\Delta Z_L\\
       &+1152d_+Z_M
          +(1152d_++D_1+L+\ell^{-1})Z_F,\\
 A_*={}&\alpha_++3b_+M_0^2+(b_+M_0/2+g_+)M_1 .
\end{split}                                                   \tag{LT.15}
$$
Indeed the two pure finite-to-far reference legs vanish by (LT.12).
All remaining legs are the complete nonlinear difference, the middle
band, or the far-band commutator (LT.6). In particular $D_1$ is still
present.

If only $Z_L$ and the whole $Z_H$ are supplied, use
$$
\begin{split}
 E_F\le{}&F_{288}
 +(a_\Delta+384d_\Delta)Z_L\\
 &+\left[A_*+a_\Delta+
 \sqrt{(1152d_+)^2+
 (1152d_++D_1+L+\ell^{-1})^2}\right]Z_H .
\end{split}                                                   \tag{LT.16}
$$
Here $Z\le Z_L+Z_H$ was used only to obtain an explicit positive
linear expression. No actual high body norm has been set to zero.

## 5. The complete source support and the restored high window

The residual identity (MA.2) is
$$
 f_\delta=f_0-\delta b_0+\delta r_0e_2
                -\delta^2T_2-\delta^3T_3 .
$$
The degree of $f_0$ is 96, that of $b_0$ is at most 160, and the
degrees of $T_2,T_3$ are at most 224 and 288. The independent raw mean
is degree zero. The actual selected residual therefore has full
support at most 288. In particular
$$
 H_{96}Pf_0=0,\quad H_{96}P(r_0e_2)=0,\quad
 H_{288}Pf_\delta=0.                                  \tag{LT.17}
$$
The first identity uses the original degree-32 centre. It must not be
applied to a different degree-96 reference's full cubic residual.

For a true solution $f=0$, (LT.17) gives $F_{288}=0$ and
$$
 F_{96}\le dS_{96}+d^2T_{2,I}+d^3T_{3,I},             \tag{LT.18}
$$
where $S_{96}$ is any complete bound for $H_{96}Pb_0$ on $I$.
The existing complete $Pb_0$ budget is one such bound; a new restriction
of the saved complete nonmean rows can provide a sharper one.
The new MC mean fee is required for the full equation, but is
identically absent from this high projection.

For an approximate state, add its true $\|H_{96}Pf\|_2$ to (LT.18)
and use $F_{288}=\|H_{288}Pf\|_2$. These source terms are never
discarded by a claim about the reference support.

Now suppose the same true solution and the same radius satisfy one of
the five corrected MA cases. Its raw high trace is bounded by
$2^{377903}$ in $H^{8193}$. Interpolating (LT.10) with that bound gives
$$
 \|H_{288}h(c)\|_{H^1}
 \le 2^{377903/16385}V_{288}^{16384/16385}
 <2^{24}V_{288}^{16384/16385},                         \tag{LT.19}
$$
with the zero case understood as equality zero. This finite high norm
is used only at the same actual cut and for the same state. It is
not transferred to an arbitrary approximate iterate.

## 6. A finite/middle/infinite sufficient cut gate

Let $c_L$ be a rigorous bound for the actual raw finite trace
$\|\Pi_{96}h(c)\|_{L^2}$, including its mean.
The orthogonal decomposition into the three bands gives
$$
 \boxed{
 \|h(c)\|_{H^1}\le
 T_{\rm cut}:=
 \left[
 \Lambda_{96}^2c_L^2+
 \Lambda_{288}V_{96}^2+
 2^{48}V_{288}^{32768/16385}
 \right]^{1/2}. }                                    \tag{LT.20}
$$
The middle-band estimate uses
$\Lambda_j^2\le\Lambda_{288}\Lambda_j$ for $97\le|j|\le288$.
Thus only this finite band pays the complete known reference source;
the factor $2^{24}$ is used solely for the genuinely infinite tail.

The sharp known-base theorem
[W.29--W.33](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md)
then applies if $T_{\rm cut}\le2^{-10}$ and
$$
 \frac{13|\delta|}{200}+\frac{T_{\rm cut}}{15}
                  <\frac{10^{-9}}{128}.              \tag{LT.21}
$$
In particular $T_{\rm cut}<63\cdot10^{-10}/320$ is a uniform
sufficient gate for $|\delta|\le10^{-10}$.
This is an explicit condition on actual unknown correction bounds.
This note does not report that it has passed.

## 7. An ordinary derivative alternative for approximate iterates

When no high window is available, the half trace (LT.10) remains
valid. A complete ordinary first-angular source also gives a direct
$H^1$ alternative. Start from the already differentiated full
E.16, which includes $d_\phi p$ for $p=z_\phi$, and then project.
It is incorrect to differentiate only the projected first equation
and omit that coefficient.

Set $F_{J,1}=\|H_JF_\phi\|_{L^2(I)}$ and take the second cutoff
supported in $I_1$, equal to one near $c$, with derivative at most
$2/\ell$. Since
$\|\Pi_Jp\|_{L^2(I_1)}\le N_JZ_{\le J}$ and
$\|H_Jp\|_{L^2(I_1)}\le c_pE_J$, the same commutator calculation gives
$$
\begin{split}
 E_{J,1}={}&F_{J,1}+B_{10}Z+
       (A_1N_J+N_J^2d_+)Z_{\le J}\\
       &+(A_1+N_Jd_++D_1+L+2\ell^{-1})c_pE_J .
\end{split}                                                   \tag{LT.22}
$$
The compact cutoff of $H_Jp$ has $L^2$ norm at most $c_pE_J$
and radial derivative norm at most $c_rE_{J,1}$. Applying (LT.8) to
this function proves
$$
 \|H_Jh(c)\|_{H^1}
 \le p_c\kappa_J\sqrt{c_pc_r E_JE_{J,1}}.              \tag{LT.23}
$$
The difference-quotient passage in E/H supplies the weak formulation;
the required ordinary $F_\phi$ is an actual input. For a true solution
and $J=288$, (LT.17) makes this source derivative exactly zero too.
One may take the minimum of the two complete far-band estimates
(LT.19) and (LT.23) when both sets of hypotheses hold.

## 8. What the available Green output does and does not supply

The existing finite193 Green output uses the original moving angle,
the raw pair $h=(h_u,h_v)$, and the normalized orthogonal odd/even
basis. The artificial second-row $R=\operatorname{diag}(I_{96},
\rho I_{97})$ scaling has already been removed in that output.
Thus its true cut norm can contribute $c_L$ in (LT.20) without
another $\rho^{-1}$, $\alpha$, or dimension factor.

Its whole inner body is exactly $[0,9/10]$. It can be restricted to
the left half of $I$, but not to the right cap half. If actual raw
low and high body bounds are supplied separately as
$B_L^-,B_H^-$ on the left and $B_L^+,B_H^+$ on the right, then
$$
 Z_L\le p_I\sqrt{(B_L^-)^2+(B_L^+)^2},\qquad
 Z_H\le p_I\sqrt{(B_H^-)^2+(B_H^+)^2},
 \quad
 p_I=\sup_I\max(K^{1/4},K^{-1/4}).                    \tag{LT.24}
$$
Sharper already scaled bounds may be substituted with their exact units.

The three available finite193 families have different meanings:
ordinary body-source Green gain, true right Poisson gain, and the
specialized old body-high-to-low gain for the original finite
$97,\ldots,160$ input block. The last is not the ordinary Green gain.
None of these operator norms, by itself, is a norm of the actual
correction. Its true source, boundary, parameter and high-block loads
must first be supplied and charged.

For this interface a consumer must therefore receive:

- the actual low cut bound $c_L$ for the same selected reference;
- same-state low and high body bounds on both halves of $I$;
- full ordinary high residuals, and the actual residual mean needed
  for $L$, unless the state has already been proved to solve the PDE;
- a same-state high-trace authorization for (LT.19), or the ordinary
  derivative source for (LT.23).

The original Green's left-only body window and the cap's right-half
window cannot be joined merely by relabelling a norm. The underlying
state must already be the same continuous state through the cut.
If it has a jump, the true seam term in E.8 must be paid. This note
does not set a boundary mismatch or an independent flux charge to zero.

## 9. Mean and shape refinements retain the independent charge

Let $\eta_v=h_v(c)$ and $\mu=\langle\eta_v\rangle_\phi$.
The selected normalized density $j_\delta=v_\delta/m_\delta$ has
degree at most 96. Consequently
$$
 \partial_\phi(\eta_v-j_\delta\mu)
 =\partial_\phi(\Pi_{96}\eta_v-j_\delta\mu)
                  +\partial_\phi H_{96}\eta_v        \tag{LT.25}
$$
is an orthogonal low/high split. If a correlated finite-cut certificate
supplies the first term's norm $c_{\rm shape}$ and the true mean
$|\mu|$, W's complete J estimate permits
$$
 \|\gamma\|_{A_0}
 \le\frac{13|\delta|}{200}
 +\frac1{16}
    \sqrt{c_{\rm shape}^2+
          \Lambda_{288}V_{96}^2+
          2^{48}V_{288}^{32768/16385}}
 +\frac{|\mu|}{576}.                                 \tag{LT.26}
$$
Its small-neighbourhood hypotheses must also hold. This improvement
requires the actual correlated finite data; the scalar $c_L$ alone is
not silently promoted to that certificate.

Under the true physical change of angle,
$\langle C\rangle_\theta=1/m$ and
$\langle B\rangle_\theta=\langle u\rangle_\phi/m$.
Therefore a complete $C$-mean comparison can control
$$
 \mu=
 \frac{\langle C_\delta\rangle_\theta-\langle C\rangle_\theta}
      {\langle C\rangle_\theta\langle C_\delta\rangle_\theta}.
                                                               \tag{LT.27}
$$
It does not control the nonmean shape in (LT.25).
Reflection gives the expected odd $B$ mean, but supplies no missing
bound for that even nonmean shape. These algebraic mean identities
preserve the charges; they do not replace (LT.20) or prove a core
selfmap.

The resulting interface is quantitative and directly consumable once
the listed true body/cut inputs exist. It preserves both means,
finite193 normalization, genuine source support, all seam terms and
the unresolved actual core/high-block matching.
