# R133 supplement: the selected-parameter cap-row transfer, including unknown high input

2026-11-15, visible-exact-astra-0df9.

**Proved analytic transfer theorem.** On the original real explicit family
$Q_\delta=Q_0+\delta Z$, with $|\delta|\le10^{-10}$, the complete 97
moving boundary rows formed with the fixed old physical cap operator
change by less than $10^{-4}$ as operators on the entire even
$L^2_\phi$ input. The mean row and every unknown high input are included.
This is a finite-output estimate obtained from the genuine adjoint
regularity of the old cap. It is not a small same-order estimate for an
arbitrary composition operator.

The new exact cap operator, if used instead of this fixed old operator,
has its separate already proved physical-angle difference fee. The
theorem below states that additional fee explicitly; it does not assume
a true core solution or the actual inner-data gates.

## 1. Exact objects and already certified inputs

The old centre is the continuous repair with definition
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.
The continuous physical response $Z=(\xi,\zeta)$ has definition
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The fixed intrinsic parameter is $\eta_0$. The selected actual phase
parameter has $|\delta_*|<9.368259853002\,10^{-11}<10^{-10}$, by
[the actual selected family](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md).
No exact PDE branch is inferred from this explicit family.

All traces here are at $L=9/10$, in the original moving coordinate.
The $\nu$-metric bump is supported in $[1/20,9/50]$, so the intrinsic
positive cap is unchanged. Write
$$
 Q_0=(u_0,v_0),\quad Q_\delta=(u_\delta,v_\delta),\quad
 E_0\ge\|Q_\delta-Q_0\|_{A^0,\mathrm{pair}},\quad
 E_1\ge\|\partial_\phi(Q_\delta-Q_0)\|_{A^0,\mathrm{pair}}.
 \tag{Cδ.1}
$$
The pair norm is the sum of the two complete Wiener norms.

The old full-body response budget
[43597921732](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json)
gives raw-response pair norms below $18.844974$ and $82.074100$.
Its complete continuous repair is below $2.292\,10^{-16}$ in
$A_{1/64}$, including its mean, by
[the continuous direction](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md),
(Q.8). Its Fourier support is at most 96, so its ordinary first
derivative is at most $384$ times its $A^0$ norm. Therefore the
strict, deliberately wider full-interval bounds
$$
 \|Z\|_{A^0,\mathrm{pair}}<19,\qquad
 \|Z_\phi\|_{A^0,\mathrm{pair}}<83
 \tag{Cδ.2}
$$
follow without a new evaluation of any coefficient. We may take
$$
 E_0=19\,10^{-10},\qquad E_1=83\,10^{-10}.
 \tag{Cδ.3}
$$
The argument also applies to any smaller verified fees. We use
$E_0,E_1\le10^{-6}$ in elementary auxiliary inequalities.

The complete joint table after (C.5) of
[the old physical cap](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
gives
$$
 \begin{gathered}
 3.1914104290<|m_0|<5.8639401366,\qquad m_0=\langle v_0\rangle_\phi,\\
 \|j_0-1\|_{A_{1/32}}<.015211829,\qquad
 \|(j_0)_\phi\|_{A_{1/32}}<.061779810,\\
 \|C_0\|_{A_{1/64}}<.318181201,\qquad
 \|(C_0)_\theta\|_{A_{1/64}}<.020269146.
 \end{gathered}
 \tag{Cδ.4}
$$
Here $j_0=v_0/m_0$; $C_0(\theta)$ in this table denotes the full old
physical curvature function, not its scalar Fourier mean. The function
and mean are distinguished by explicit angle brackets below.
Also $\|u_0\|_\infty<7$, $\|(u_0)_\phi\|_\infty<6$, and
$\|(v_0)_\phi\|_\infty<1$; the last follows from the first line and
the $j_0$ derivative bound. These are weaker than the original table.

## 2. Real coordinate changes with the full mean

Set
$$
 m_\delta=\langle v_\delta\rangle_\phi,\quad
 j_\delta=v_\delta/m_\delta,\quad
 \Theta_\delta=\mathrm{id}+I_\phi(j_\delta-1),\quad
 \Phi_\delta=\Theta_\delta^{-1},\quad
 V_\delta f=f\circ\Phi_\delta.
 \tag{Cδ.5}
$$
The signed $m_\delta,v_\delta$ are retained in every identity.
The original reflection normalization fixes the additive angle.

The exact difference is
$$
 j_\delta-j_0=
 \frac{(v_\delta-v_0)-j_0(m_\delta-m_0)}{m_\delta}.
 \tag{Cδ.6}
$$
Equations (Cδ.1)--(Cδ.4) give, throughout the straight real state segment,
$$
 |m|,|v|\ge3,\quad |m|<6,\quad
 \frac78<j<\frac98,\quad |v_\phi|<1,
 \tag{Cδ.7}
$$
and
$$
 |m_\delta-m_0|\le E_0,\quad
 \|j_\delta-j_0\|_\infty\le\frac{17}{24}E_0,\quad
 \|\Theta_\delta-\Theta_0\|_\infty<\frac{E_0}{3},\quad
 \|\Phi_\delta-\Phi_0\|_\infty<\frac{E_0}{2}.
 \tag{Cδ.8}
$$
The primitive fee is its actual $L^\infty$ norm $\pi/8$, not $1/4$.
The inverse estimate uses $\Phi_\theta\le8/7$.
In addition $\|\Theta-\mathrm{id}\|_\infty<1/64$.

For real circle diffeomorphisms $F_0,F_1$ with $F_i'\ge a>0$, the
linear interpolation $F_t=(1-t)F_0+tF_1$ has the same lower bound.
The fundamental theorem of calculus and change of variables give
$$
 \|k\circ F_1-k\circ F_0\|_2
 \le a^{-1/2}\|F_1-F_0\|_\infty\|k'\|_2,\qquad k\in H^1.
 \tag{Cδ.9}
$$
Only the known adjoint test will use this inequality. It is not applied
with a derivative of an arbitrary unknown $L^2$ trace.

Define the actual physical functions
$$
 C_\delta=(1/v_\delta)\circ\Phi_\delta,\qquad
 B_\delta=(u_\delta/v_\delta)\circ\Phi_\delta.
$$
One has
$$
 \|C_\delta-C_0\|_\infty\le E_0/8,\qquad
 \|(C_\delta)_\theta-(C_0)_\theta\|_\infty
                 \le E_0+E_1/4,\qquad
 |C_\delta|\le1/3,\quad |(C_\delta)_\theta|<1/16.
 \tag{Cδ.10}
$$
Here is a derivative check. At a common moving angle
$(C_\delta)_\theta\circ\Theta_\delta=-m_\delta(v_\delta)_\phi/v_\delta^3$.
The absolute partial derivative bounds with respect to $m,v,v_\phi$
are $1/27,2/9,2/9$, by (Cδ.7). The old physical second derivative
satisfies $\|(C_0)_{\theta\theta}\|_\infty<2$, because
$|k|\le64e^{|k|/64}$ and (Cδ.4).
Changing its argument costs at most $2E_0/3$.
Thus the derivative difference is at most
$25E_0/27+2E_1/9<E_0+E_1/4$.
Similarly the reciprocal difference costs $E_0/9$, and the old
physical $C$-derivative costs at most $E_0/96$; their sum is below
$E_0/8$.

## 3. The exact 97 rows and their adjoint

Use the same operators as (P.6)--(P.14) of
[the complete moving interface](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md):
$$
 \begin{aligned}
 S_Qb&=v(b\circ\Theta),\qquad S_Q^*f=m(f\circ\Phi),\\
 H_{B,Q}&=-M_{BC}V-M_{B_\theta}I_\theta M_CV,\\
 H_{C,Q}&=-M_{C^2}V-M_{C_\theta}I_\theta M_CV .
 \end{aligned}
 \tag{Cδ.11}
$$
All means use normalized physical or moving circle measure as indicated.
Let $K=(K_B,K_C^0)$ be the old known physical cap operator. Its scalar
second component is the old $K_0$ of (P.12).
For a moving direction $h=(h_1,h_2)$, define
$$
 {\cal B}_Q^K h=
 \left(
 P_{\mathrm{o},96}\{h_1+S_Q(H_{B,Q}-K_BP_{\perp,\theta}H_{C,Q})h_2\},
 -m^{-2}\langle h_2\rangle_\phi-K_C^0P_{\perp,\theta}H_{C,Q}h_2
 \right).
 \tag{Cδ.12}
$$
The output norm is the Euclidean norm of the 96 orthonormal odd
coefficients and the one mean row. The input $h_2$ is an arbitrary
even $L^2_\phi$ function, including its mean and all modes above 96.

The old-cap theorem
[H: complete first-angular adjoint bound](R133-supplement-small-first-angular-adjoint-bound-for-fixed-known-M32-cap.md)
proves
$$
 \|K\|_{L^2_{\perp,\theta}\to L^2_\theta\oplus_1\mathbb R}<16,\qquad
 \|K^*(m_0V_0f,a)\|_{H^1_\theta}\le2^{16}\|\lambda\|_2,
 \tag{Cδ.13}
$$
where $f=\sum_{j=1}^{96}\lambda_j\sqrt2\sin(4j\phi)$ and
$a=\lambda_{97}$. Its complete $C$-mean, auxiliary $B$-mean
feedback, residual Hessian and genuine exterior derivative are retained.
It is only a theorem about this fixed old known analytic exterior
background.

For such $f$, (Cδ.8)--(Cδ.9) give
$$
 \|(S_\delta^*-S_0^*)f\|_2
 \le\left(\frac98+6\frac98\frac{384}{2}\right)E_0\|f\|_2
 <1300E_0\|f\|_2 .
 \tag{Cδ.14}
$$
The derivative bound $384$ applies to the actual moving test $f$,
not to $V_0f$ or to any unknown input.
Also
$$
 \|H_{C,\delta}\|_{L^2_\phi\to L^2_\theta}
 \le\frac98\left(\frac19+\frac1{192}\right)<\frac16.
 \tag{Cδ.15}
$$

The exact adjoint of the curvature row is
$$
 H_{C,Q}^*k
 =-\frac{k\circ\Theta}{mv}
       +\frac1m\{I_\theta(C_\theta k)\}\circ\Theta .
 \tag{Cδ.16}
$$
It follows from $V^*g=j(g\circ\Theta)$ and $I_\theta^*=-I_\theta$.
This formula keeps the density and signed mean.

For every $k\in H^1_\theta$,
$$
 \|(H_{C,\delta}^*-H_{C,0}^*)k\|_2
 \le (E_0/4+E_1/32)\|k\|_{H^1_\theta}.
 \tag{Cδ.17}
$$
For completeness, the two terms in (Cδ.16) give the following positive
bounds, in the same order. In the first term,
$$
 \left\|\Delta\left(\frac{k\circ\Theta}{mv}\right)\right\|_2
 \le\frac{16E_0}{189}\|k\|_2+\frac{8E_0}{189}\|k'\|_2.
 \tag{Cδ.18}
$$
For the second, use
$|\Delta(m^{-1})|\le E_0/9$,
$\|I_\theta(C_{\delta,\theta}k)\circ\Theta_\delta\|_2
 \le\|k\|_2/56$,
the original $(C_0)_\theta$ bound $<1/32$ from (Cδ.4),
and the mean-retaining derivative
$\partial_\theta I_\theta(C_{0,\theta}k)=P_\perp(C_{0,\theta}k)$.
The resulting bound is
$$
 \left\|\Delta\left(m^{-1}I_\theta(C_\theta k)\circ\Theta\right)\right\|_2
 \le\left(\frac{E_0}{504}+\frac{2E_0}{21}
              +\frac{E_0}{252}+\frac{E_1}{42}\right)\|k\|_2.
 \tag{Cδ.19}
$$
The coefficient of $E_0$, including that of $\|k'\|_2$, is less
than $1/4$; $1/42<1/32$. Since each of $\|k\|_2,\|k'\|_2$ is
at most $\|k\|_{H^1}$, this proves (Cδ.17). No differentiability of
the unknown trace was used.

## 4. The local row also has an exact moving expression

Put $D=u/v$, $\psi=\Theta-\mathrm{id}$, and
$$
 A_Qh=I_\phi h-\langle h\rangle_\phi\psi .
$$
For an even $h$, reflection fixes the constant in the primitive and
gives
$$
 [I_\theta(CVh)]\circ\Theta=m^{-1}A_Qh,\qquad
 S_QH_{B,Q}h=-Dh-D_\phi A_Qh .
 \tag{Cδ.20}
$$
Both formulas retain $\langle h\rangle_\phi$. In particular
$\|A_Q\|_{L^2\to L^2}<1/3$ and
$\|A_\delta-A_0\|\le E_0/3$.

At a common moving angle the elementary quotient bounds give
$$
 \|\Delta D\|_\infty\le10E_0/9,\quad
 \|\Delta D_\phi\|_\infty\le4E_0/3+10E_1/9,\quad
 \|(D_0)_\phi\|_\infty<3 .
 \tag{Cδ.21}
$$
For example the difference of $u v_\phi/v^2$ is split into the
three factors in that displayed order, using
$|\Delta(v^{-2})|\le2E_0/27$.
Thus
$$
 \|\Delta(SH_B)\|_{L^2\to L^2}\le3E_0+E_1/2,\qquad
 |\Delta(m^{-2})|\le2E_0/27<E_0/8.
 \tag{Cδ.22}
$$
The complete local 97-row difference is consequently at most
$4E_0+E_1$. Projection to the first 96 odd tests is a contraction;
it does not remove a row needed in (Cδ.12).

## 5. Complete operator difference and the selected parameter

Pair the last term of (Cδ.12) with $\lambda=(f,a)$.
Its cap contribution is
$$
 -\langle K^*(S_Q^*f,a),H_{C,Q}h_2\rangle_\theta .
 \tag{Cδ.23}
$$
The input nonmean projection may be omitted in this pairing only
because $K^*(S_Q^*f,a)$ lies in the actual nonmean input space.
The scalar $a$ remains present.

Split its difference into the change of the first test and the
change of $H_C$. Equations (Cδ.13)--(Cδ.17) give
$$
 \|\Delta(\hbox{complete cap contribution})\|
 \le\frac{16\cdot1300}{6}E_0
       +2^{16}(E_0/4+E_1/32).
$$
Adding (Cδ.22), and using a larger rational bound, proves
$$
 \boxed{\quad
 \|{\cal B}_{Q_\delta}^{K}-{\cal B}_{Q_0}^{K}\|_{L^2_\phi\to\mathbb R^{97}}
 \le 2^{15}E_0+2^{12}E_1
 \le\frac{2^{15}\cdot19+2^{12}\cdot83}{10^{10}}
 <10^{-4}.
 \quad}
 \tag{Cδ.24}
$$
The full two-component moving input has the same bound, since its
$h_1$ coefficient does not change. This is a single operator estimate
for every linear combination of the 97 rows. It has no $\sqrt{97}$
fee and applies equally to a low input or an unknown high even input.

This bound concerns the coordinate and multiplier change with **fixed
old $K$**. In particular it does not silently identify the derivative
of a new cap graph with that old operator.

## 6. Add the actual cap difference in its physical input units

Suppose a new complete physical cap pair $K_*$, at the same fixed
intrinsic data and physical angle, obeys the already established
[inner Poisson comparison](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md)
$\|K_*-K\|_{L^2_{\perp,\theta}\to L^2_\theta\oplus_1\mathbb R}\le\kappa_*$.
Its stated hypotheses, including the true input domains, remain required.
In the proved actual cap ball one may use $\kappa_*=1/5$.

Put
$$
 \begin{aligned}
 j_+&=1.015211829+17E_0/24,\\
 m_+&=5.8639401366+E_0,\qquad s_\delta=m_+\sqrt{j_+},\\
 C_+&=.318181201+E_0/8,\qquad
 C_{1,+}=.020269146+E_0+E_1/4,\\
 c_\delta&=\sqrt{j_+}\{C_+^2+C_{1,+}C_+/4\}.
 \end{aligned}
 \tag{Cδ.25}
$$
These are explicit bounds for $\|S_\delta\|$ and $\|H_{C,\delta}\|$
on the correct normalized measures. The first follows from
$S_\delta^*=m_\delta V_\delta$.

The independent physical cap change now gives
$$
 \|{\cal B}_{Q_\delta}^{K_*}-{\cal B}_{Q_\delta}^{K}\|
 \le\max(s_\delta,1)c_\delta\kappa_* .
 \tag{Cδ.26}
$$
Therefore an admissible total boundary perturbation for both low and
high inputs is
$$
 \epsilon_{\rm row}
 =2^{15}E_0+2^{12}E_1+\max(s_\delta,1)c_\delta\kappa_* .
 \tag{Cδ.27}
$$
One may use tighter previously certified signed cap columns instead
of this uniform last fee, with their original covariance. This formula
does not replace those columns by an entrywise minimum.

Only the derivative row has been estimated here. Particular-source
traces, affine cap defects, the independent ordinary mean data, and
the actual $\nu$ response must also be transferred in their original
units. The body operator difference and the two-output finite Green
feedback are independent parts of the same-parameter argument.
The complete high inverse, full nonlinear core graph, and physical
$H^1/H^{8193}$ inner-trace gates are not conclusions of this theorem.
