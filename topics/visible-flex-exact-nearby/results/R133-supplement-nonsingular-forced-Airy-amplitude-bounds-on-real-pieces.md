# R133 supplement: nonsingular quantitative forced Airy amplitudes on actual radial pieces

2026-11-14, phase_inverse. **Proved explicit norm theorem.** This
turns the exact forced characteristic formula into finite bounds for
both Airy amplitudes at the root and across every original radial
piece. It uses no radial Cauchy estimate across a cubic seam.

The hypotheses are the actual coefficient and fold envelopes in
[the piecewise real root construction](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md).
Numerical values are supplied only by its independently executed
consumer and a subsequent directed budget. The present theorem does
not evaluate the actual forcing of a next parametrix amplitude.

## 1. Domain, coefficient constants and the exact scalar kernels

Work at real radial distance $x=|r-r_*|\le R$ on either side of the
true root. The same estimates are uniform on a complex explicit
parameter disk whenever the preceding fold hypotheses hold there.
Let $\sigma_0$ be the paid old coefficient width and $M_R$ the
complete ray displacement. Choose a final old-angle width
$\sigma_f$ and a positive number $\omega$ such that
$$
 \sigma_f+M_R+\omega<\sigma_0.                         \tag{F.1}
$$
All forcing norms below are uniform complex suprema on the
intermediate old angular strip of width $\sigma_0-\omega$.
The actual characteristic compositions and their convex angular
comparison paths stay in this strip. Their underlying coefficient
paths are ordered root-to-point paths, as in (M.3)--(M.7).

Let $D_j$ bound $\partial_\phi^j d$, for $j=1,2,3$, on that complete
coefficient domain. If only the complete outer Wiener bound $D_2$
is supplied, it is valid to use
$$
 D_3=\frac{D_2}{e\omega}.                              \tag{F.2}
$$
Indeed $|n|e^{-\omega|n|}\le1/(e\omega)$ for every physical Fourier
frequency. This is an explicitly charged angular loss; it is not a
radial continuation or a derivative of an interval error.

Use the actual constants $a_-,a_+,A_-,A_+,j$ and $G_+,G_-$, where
$|G|\le G_+$, $|G|^{-1}\le G_-$ and
$|S_{\pm,\phi}-1|\le j<1$. Put
$$
 h=1-j,\quad H=1+j,\quad E=e^{D_1R}\le H,\quad
 \mathfrak c=\tfrac43 a_+H.                          \tag{F.3}
$$
The possible conservative numerical overcoverage of the uncertain
root is included in $R$ and in the input envelopes.

Retain exactly the labels in (M.13). Write
$$
 t=\sqrt{-T},\quad H_\sigma=X_\phi+\sigma tT_\phi,\quad
 V_\sigma=a+\sigma i\epsilon t b,\quad
 V_{\sigma,0}=G H_\sigma^2 ,
$$
$$
 K_\sigma=\frac{C_\sigma}{2V_{\sigma,0}}
 =\frac{a_{\rm rad}A^{-1/3}}{2G}
                     \frac{H_{-\sigma}}{H_\sigma^2}. \tag{F.4}
$$
Here $a_{\rm rad}=\eta\sqrt{k}$ is radial, while $a,b$ are the
forced amplitudes. For the finite transport recursion take the
common root trace $a(0)=0$. The exact integral is
$$
 V_\sigma=V_{\sigma,0}\int_{r_*}^r
       K_\sigma(F_a-\sigma i\epsilon F_b/t)
                         (s,\chi_\sigma(s;r,\phi))\,ds .          \tag{F.5}
$$
No primitive, mean or matrix inverse is silently incorporated into
$F_a,F_b$. They are precisely the two amplitude components of the
complete finite ordered forcing when that forcing is supplied.

## 2. Angular differences that remove the apparent root singularity

The characteristic variation equations give
$$
 |X_{\phi\phi}|\le D_2x e^{3D_1R},\qquad
 |S_{\pm,\phi\phi\phi}|
 \le(D_3x+3D_2^2x^2)e^{6D_1R}.                      \tag{F.6}
$$
For example the three scalar variation equations are
$J'=v_\phi J$,
$J_2'=v_\phi J_2+v_{\phi\phi}J^2$, and
$J_3'=v_\phi J_3+3v_{\phi\phi}JJ_2+v_{\phi\phi\phi}J^3$.
They apply equally to the backward characteristic and to the
common drift. Absolute Gronwall bounds prove (F.6), with room
in the displayed exponent.

Differentiating the exact ordered integral (M.7) twice gives
$$
 |A_\phi|\le c_{A1}x,\quad |A_{\phi\phi}|\le c_{A2}x,
$$
$$
 c_{A1}=\tfrac35a_+D_2e^{4D_1R},\quad
 c_{A2}=\{\tfrac35a_+D_3+2a_+D_2^2R\}e^{8D_1R}.      \tag{F.7}
$$
For the quadratic term in the second estimate the two exact
integration coefficients are $9/7$ and $6/35$; their sum is
$51/35<2$. This also pays the second angular derivative of the
common drift composition.

Since $T=-\rho A^{2/3}$, define
$$
 c_{T1}=\tfrac23A_-^{-1/3}c_{A1},
$$
$$
 c_{T2}=\tfrac23A_-^{-1/3}c_{A2}
                    +\tfrac29A_-^{-4/3}c_{A1}^2R .
$$
Then $|T_\phi|\le c_{T1}x^2$ and
$|T_{\phi\phi}|\le c_{T2}x^2$. Moreover
$$
 A_-^{1/3}\sqrt{x}\le|t|\le A_+^{1/3}\sqrt{x}.
                                                               \tag{F.8}
$$
Put
$$
 c_Y=A_+^{1/3}c_{T1},\quad
 c_{Y1}=A_+^{1/3}c_{T2}+
                    \frac{c_{T1}^2R}{2A_-^{1/3}},\quad
 c_H=D_2e^{3D_1R}+c_{Y1}R^{3/2}.
$$
For $y=tT_\phi$ one has
$$
 |y|\le c_Yx^{5/2},\quad |y_\phi|\le c_{Y1}x^{5/2},
 \quad |H_{\sigma,\phi}|\le c_Hx .                    \tag{F.9}
$$

The radial exponential in $G$ has a genuine old angular mean
in its exponent and is independent of $\phi$. The other radial
factors are also independent of $\phi$. Thus the exact identity
$G_\phi/G=A_\phi/(6A)$ holds. Define
$$
 P_*=\frac{a_+A_-^{-1/3}G_-}{2},\qquad
 K_0=P_*H/h^2,
$$
$$
 K_1=K_0\{c_{A1}/(2A_-)+3c_H/h\},\qquad
 K_\Delta=\frac{2P_*c_Y(3H^2+c_Y^2R^5)}{h^4}.         \tag{F.10}
$$
Then, at the same point $(r,\phi)$,
$$
 |K_\sigma|\le K_0,\quad
 |\partial_\phi K_\sigma|\le K_1x,\quad
 |K_+-K_-|\le K_\Delta x^{5/2}.                       \tag{F.11}
$$
The last estimate uses the exact numerator
$$
 \frac{H_-}{H_+^2}-\frac{H_+}{H_-^2}
       =-\frac{2y(3X_\phi^2+y^2)}{H_+^2H_-^2}.
$$
It is not a cancellation inferred from a diagonal symbol.

Also set
$$
 B_0=G_+H^2,\quad B_\Delta=4G_+Hc_Y .
$$
The true leading branch factors satisfy
$$
 |V_{\sigma,0}|\le B_0,\qquad
 |V_{+,0}-V_{-,0}|\le B_\Delta x^{5/2}.              \tag{F.12}
$$
These factors must still multiply a bound on the integral in (F.5).

For the $F_b/t$ term define
$$
 M_0=K_0A_-^{-1/3},\quad
 M_1=A_-^{-1/3}K_1+\tfrac13K_0A_-^{-4/3}c_{A1},
 \quad M_\Delta=A_-^{-1/3}K_\Delta .                 \tag{F.13}
$$
On each side $K_\sigma/t$ is a common constant of modulus one
times $M_\sigma/\sqrt{x}$, where
$M_\sigma=K_\sigma A^{-1/3}$.
Consequently $|M_\sigma|\le M_0$,
$|M_{\sigma,\phi}|\le M_1x$ and
$|M_+-M_-|\le M_\Delta x^{5/2}$.

## 3. Complete finite bounds for both forced amplitudes

For two true rays with the same terminal angle, at distance $s$
from the root, the scalar angular difference obeys
$$
 |\chi_+(s)-\chi_-(s)|
 \le\mathfrak c(x^{3/2}-s^{3/2}),\qquad0\le s\le x .
                                                               \tag{F.14}
$$
Indeed their speed difference has the radial term
$2\eta q$ and the actual Lipschitz drift. Integrating
$2a_+\sqrt{s}$ and paying $e^{D_1R}\le H$ gives (F.14).
This remains valid for the two complex rays on the positive side.

Let
$$
 F_{a,0}=\|F_a\|_\infty,\quad F_{a,1}=\|\partial_\phi F_a\|_\infty,
 \quad F_{b,0}=\|F_b\|_\infty,\quad
 F_{b,1}=\|\partial_\phi F_b\|_\infty
$$
on the complete intermediate strip from Section 1. All are
suprema over the actual radial pieces and both one-sided traces.

The following completely explicit bounds hold at every $x\le R$:
$$
 \boxed{\quad
 \|a\|_{\sigma_f,\infty}
 \le A_a F_{a,0}+A_{b0}F_{b,0}+A_{b1}F_{b,1},\qquad
 \|b\|_{\sigma_f,\infty}
 \le B_{a0}F_{a,0}+B_{a1}F_{a,1}+B_bF_{b,0}.
 \quad}                                                        \tag{F.15}
$$
Here
$$
 A_a=B_0K_0R,\qquad
 A_{b0}=\{B_\Delta M_0+
              \tfrac{B_0}{6}(M_\Delta+M_1\mathfrak c)\}R^3,
 \quad
 A_{b1}=\tfrac34 B_0M_0\mathfrak c R^2,               \tag{F.16}
$$
$$
 B_{a0}=
 \frac{B_\Delta K_0+
       B_0\{(2/7)K_\Delta+(3/14)K_1\mathfrak c\}}
              {2A_-^{1/3}}R^3,
$$
$$
 B_{a1}=\frac{3B_0K_0\mathfrak c}{10A_-^{1/3}}R^2,
 \qquad B_b=2B_0K_0A_-^{-2/3}.                       \tag{F.17}
$$
In particular $B_b$ is finite at the root; there is no artificial
factor $1/\sqrt{x}$ in the output amplitude norm.

For completeness, separate the two forcing terms in (F.5).
For the $F_a$ integrals the difference of kernels at the same
angle costs $K_\Delta s^{5/2}$. Comparing their true evaluation
angles costs
$(K_1sF_{a,0}+K_0F_{a,1})
 \mathfrak c(x^{3/2}-s^{3/2})$.
The three radial integrals are exactly
$$
 \int_0^x s^{5/2}ds=\tfrac27x^{7/2},\quad
 \int_0^x s(x^{3/2}-s^{3/2})ds=\tfrac3{14}x^{7/2},
$$
$$
 \int_0^x(x^{3/2}-s^{3/2})ds=\tfrac35x^{5/2}.          \tag{F.18}
$$
Include the final factor difference (F.12), then divide the
difference by $2|t|$ using (F.8). This is exactly (F.17)'s
$F_a$ contribution. The $a$ sum is bounded directly.

For the $F_b$ integrals use (F.13); the corresponding integrals
are $x^3/3$, $x^3/3$, and $3x^2/2$, since the additional weight
is $s^{-1/2}$. Their difference bounds the $a$ amplitude.
Their sum is bounded by $4M_0\sqrt{x}F_{b,0}$; dividing by
$2|t|$ and including $B_0$ gives precisely $B_b$.
These computations retain the distinct signs of the two rays
and the final leading factors. A quotient bound alone would
not prove (F.15).

## 4. Actual seams, forcing provenance and the remaining strong budget

Piecewise bounded forcing in the exact integral gives continuous
$a,b$. At the root the original analytic germ identifies their
unique regular extension, including $b(0)=F_b(0)$; the estimates
above extend by that continuity. At each strict original seam
their radial derivative jumps remain exactly (M.16). The
reconstructed two-row source remains (M.17), together with every
independent mean and second-row source term.

The norms in (F.15) are analytic sup norms. They directly bound
ordinary normalized $L^2$ on real old circles. They do not
automatically give a Wiener norm at the same width. If a later
step needs the latter, a further positive width loss $\zeta$
pays the explicit fourfold factor
$1+2/(e^{4\zeta}-1)$.
Higher angular derivatives require either differentiated
characteristic estimates or a declared further angular loss.

For the first recursive amplitude,
$(F_b,F_a)=-\mathcal L_0(a_0,b_0)$ must still be evaluated using
the entire ordered operator, including $R_{-1}D_0$ and the
retained old mean remainders. Formula (F.15) accepts those
actual source norms when they are supplied. It does not set
them to zero or replace them with a fitted finite Fourier
residual.

After every required finite amplitude is bounded, the full
volume source and every reconstructed seam must be corrected
with the actual positive and negative propagators on their
declared radial intervals and Sobolev windows. The complete
finite head, even mean and exterior columns stay independent.
No numerical $C_E,C_s$, cutoff-97 inverse or nonlinear solution
follows from this norm theorem alone.
