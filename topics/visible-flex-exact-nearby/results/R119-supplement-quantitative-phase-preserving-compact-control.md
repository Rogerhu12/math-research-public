# R119 supplement: an actual compact C4 control with a quantitative compensated Wronskian derivative

2026-11-14, visible-exact / root. **Proved; 31 new exact rational gates passed.**

The quantitative kernel separation is now converted into a real compact
metric direction of bounded \(C_x^4\) norm. Both phase derivatives vanish
exactly, and the actual two-bump correction keeps the two phases constant
to all orders. The first derivative of the true normalized Wronskian has
an explicit lower bound, including the original \(dt\) measure and the
right resonant amplitude.

This is a local transversality statement at a true radial resonance.
It does not yet give a finite-parameter bad-set estimate, an inverse of
the coupled nonradial middle matrix, or permission to change the original
low-frequency radial source weight.

## 1. Same actual profile, kernels and normalization

Use the exact profile, \(J=[7/16,15/32]\), \(a,B,\Delta,\lambda=m^2\),
\(K_j,T\), fixed real Robin lines, and left unit wave state from
[the quantitative kernel theorem](R119-supplement-quantitative-transparent-resonance-kernel.md),
blob \(\mathtt{8b5e908a0da26a3a6038de2808cbe41c9849f439}\).
The real resonant solution gives
\[
 {\cal K}=\mu(h_t^2-2\lambda hh_t+\lambda h^2).
\]
That theorem proved the complete separation
\[
 \operatorname{dist}_{L^\infty(J)}
   ({\cal K},\{P/Q^{9/2}:\deg P\le19\})\ge\epsilon_0,
\]
\[
 \epsilon_0=
 2^{-32768}a^{382}B^{-1472}\lambda^{-383}K_j^{-510}
                        e^{-2^{67}T}.                  \tag{C.1}
\]
It also supplied the actual complex bound
\[
 \|{\cal K}\|_{|x-29/64|\le1024}\le
 M=2^{10}\lambda a^{-2}K_j^2e^{2^{60}T}.                \tag{C.2}
\]
In particular \(0<\epsilon_0<M\).
Both phase kernels have the exact form \(P/Q^{9/2}\) with
polynomial degree at most 19. The comparison in (C.1) is with
this whole larger polynomial space, not only the original two
phase kernels.

## 2. A derivative witness and an honest support interval

Let
\[
                         G(x)=Q(x)^{9/2}{\cal K}(x)
\]
on the real interval, using its positive square root.
All complex roots of \(Q\) have real part at most 0 or at least 1.
Thus \(Q^{9/2}\) has a single analytic branch on
\(|x-29/64|<1/4\) agreeing with this real value.

On that small disk,
\[
 |x|\le45/64,\quad |1-x|\le51/64,\quad |Q|<17B,
 \qquad |Q^{9/2}|<2^{20}B^5 .
\]
At every real point of \(J\), a Cauchy circle of radius \(1/8\)
lies inside the disk. The actual derivative bounds are therefore
\[
 \|G^{(21)}\|_{L^\infty(J)}
                    < M_{21}:=2^{152}B^5M,             \tag{C.3}
\]
and
\[
 \max_{0\le q\le4}\|(Q^{9/2})^{(q)}\|_{L^\infty(J)}
                                      <2^{37}B^5 .     \tag{C.4}
\]
For (C.3), \(21!<2^{66}\) and \(8^{21}=2^{63}\) leave a
strict margin in the displayed constant. No sampled derivative
or extrapolation through a branch point is used.

Taylor-expand \(G\) to degree 19 at the centre of \(J\).
Since its half-length is \(l=1/64\),
\[
 \inf_{\deg P\le19}\|{\cal K}-P/Q^{9/2}\|_J
 \le\frac{l^{20}}{20!\,\min_J Q^{9/2}}\|G^{(20)}\|_J
 \le\|G^{(20)}\|_J .
\]
Hence \(|G^{(20)}(x_0)|\ge\epsilon_0\) at some \(x_0\in J\).
This also follows by a finite grid and the uniform Lipschitz
bound (C.3), if an explicit interval search is desired.

Put
\[
                        r=\epsilon_0/(16M_{21}).       \tag{C.5}
\]
Then \(r<2^{-156}<1/128\).
Choose \(x_1\) by moving \(x_0\), only if necessary, into the
closed interval of points at distance at least \(2r\) from
both ends of \(J\). This moves it by at most \(2r\).
On the entire interval \([x_1-r,x_1+r]\),
\[
 |G^{(20)}(x)|>\epsilon_0/2
\]
and the sign is constant, because the change is at most
\(3rM_{21}=3\epsilon_0/16\).
This is a genuinely interior support interval even if the maximum
of \(|G^{(20)}|\) occurs at an endpoint of \(J\).

## 3. An explicit compact direction annihilates both phase rows

Use the complete real bump
\[
 b(y)=(1-y^2)_+^{30},\qquad
 f(x)=r^{24}b((x-x_1)/r).
\]
The zero extension of \(b\) is \(C^{29}\); consequently
\(f^{(20)}\) is \(C^9\), with the required endpoint jets zero.
Let \(s\in\{1,-1\}\) be the sign of \(G^{(20)}\) on its support and
define the actual metric direction
\[
 \boxed{\qquad
 \psi(x)=\frac{s\,Q(x)^{9/2} f^{(20)}(x)}
                         {2^{220}B^5} .
 \qquad}                                                   \tag{C.6}
\]
It is real, compactly supported strictly inside the unused ramp
interval, and \(C^9\), hence \(C^5\).

Define the \(C_x^4\) norm here to be
\(\sum_{q=0}^4\|\partial_x^q\psi\|_\infty\).
All 30-binomial coefficients of \(b\) have sum \(2^{30}\), and
its derivatives through order 24 have supremum at most
\(2^{30}60^{24}<2^{174}\).
In a derivative of (C.6) of order \(q\le4\), a term with \(l\)
derivatives on \(Q^{9/2}\) has factor
\(r^{4-q+l}\le1\).
Using (C.4) and all Leibniz coefficients gives
\[
 \sum_{q=0}^4\|\partial_x^q(Q^{9/2}f^{(20)})\|_\infty
 \le80\,2^{37}2^{174}B^5<2^{220}B^5.
\]
Thus
\[
                              \|\psi\|_{C_x^4}\le1 .    \tag{C.7}
\]
No high derivative of the original state or unknown Fourier tail
has been assigned a finite support bound.

For every polynomial \(P\) of degree at most 19, twenty ordinary
integrations by parts give exactly
\[
             \int_J(P/Q^{9/2})\psi\,dx
               =\frac{s}{2^{220}B^5}\int_JP f^{(20)}\,dx=0 .
 \tag{C.8}
\]
There are no boundary terms. Since \(dt=a\,dx\), both true phase
integrals with their original \(dt\) measure also vanish exactly:
\[
                              \dot S=\dot\beta=0 .      \tag{C.9}
\]
This construction imposes the whole polynomial annihilator and
therefore needs no approximate two-row projection.

## 4. The full kernel pairing, with its original measure

The same integration by parts, now applied to \(G\), gives
\[
 \left|\int_J{\cal K}\psi\,dx\right|
 =\frac1{2^{220}B^5}\left|\int_JG^{(20)}f\,dx\right|.
\]
The sign was fixed on the whole support. Moreover
\[
 \int_{-1}^1b(y)\,dy
 \ge(3/4)^{30}>2^{-15}.
\]
Therefore
\[
 \left|\int_J{\cal K}\psi\,dx\right|
 \ge 2^{-236}B^{-5}\epsilon_0 r^{25}
 =2^{-4136}B^{-130}\epsilon_0^{26}M^{-25}.              \tag{C.10}
\]
The powers include the support length, the \(r^{24}\) normalization,
the complete \(C^4\) factor, and the derivative bound \(M_{21}\).
A delta function or an unbounded-norm direction has not been used.

For the original material measure, multiply (C.10) by \(a\).
That factor cannot be omitted when passing from the fixed \(x\)
interval to the actual short radial ramp.

## 5. Exact phase compensation and the true normalized Wronskian

Apply the actual metric variation
\[
                  p_\varepsilon=p_0 e^{\varepsilon\psi}
\]
and use the two original disjoint bump parameters to keep \(S,\beta\)
exactly fixed, as in Section 9 of the input phase-control theorem.
Their actual two-by-two Jacobian is invertible.
Equation (C.9) means that both compensating parameters have
derivative zero at \(\varepsilon=0\).
Thus the first metric derivative of the compensated profile is
still precisely \(\psi\), and its first Wronskian derivative is
unchanged.

The small-parameter curve is real analytic in \(\varepsilon\)
in the stated finite-regularity profile class. It has the same
fixed physical endpoint data and root germs.
This assertion is local in \(\varepsilon\); a numerical size of
a finite parameter step and a bad-set measure are separate
subsequent estimates.

For complete normalization, let
\[
 \Delta_m(\varepsilon)=[r_m,C_m(\varepsilon)l_m],
 \qquad |l_m|=|r_m|=1 .
\]
At the actual resonance \(C_m(0)l_m=\alpha r_m\), with
\(0<|\alpha|\le K_j\).
The determinant-one change to the wave variables and the exact
Green identity give
\[
 \alpha\,\Delta_m'(0)
   =[Y_0,\dot Y]_b
   =\int_J{\cal K}\psi\,dt .                            \tag{C.11}
\]
To verify the last identity, differentiate
\((\mu h_t)_t+\lambda\mu Qh=0\), multiply by \(h\), and subtract
the original equation times \(\dot h\).
The compact metric variation gives
\[
 \int\{\dot\mu\,h_t^2-\lambda\dot{(\mu Q)}h^2\}\,dt
                       =\int{\cal K}\psi\,dt .
\]
All fixed-end terms vanish. The two compensating bumps have zero
first derivative, so they create no additional first-order term.
This also shows exactly where the right resonant amplitude enters;
it is not an unspecified nonzero normalization factor.

From (C.10)–(C.11),
\[
 |\Delta_m'(0)|
 \ge2^{-4136}aB^{-130}K_j^{-1}\epsilon_0^{26}M^{-25}.
 \tag{C.12}
\]
Substitute the complete values (C.1)–(C.2).
The resulting convenient strict lower bound is
\[
 \boxed{\quad
 |\Delta_m'(0)|\ge
 2^{-2^{20}}a^{9983}B^{-38402}\lambda^{-9983}K_j^{-13311}
                      \exp(-2^{72}T).
 \quad}                                                   \tag{C.13}
\]
The source checks every exponent. Before rounding, the binary
constant is \(856354<2^{20}\), and the exponential coefficient is
\(26\cdot2^{67}+25\cdot2^{60}<2^{72}\).

Using the actual \(\delta_j\) and \(J_0=j+5\) gives the completely
explicit coarser statement
\[
 \boxed{\quad
 |\Delta_m'(0)|\ge
 2^{-2^{27}}\delta^{285554}J_0^{-144890}|m|^{-19966}
  \exp\{-2^{74}J_0-2^{71}|m|\delta^{3/4}\sqrt{J_0}\}.
 \quad}                                                   \tag{C.14}
\]
Here the unrounded \(\delta\) exponent is \(285553.5\);
replacing it by \(285554\) lowers the right side because
\(0<\delta<1\).
The complete fixed binary exponent before the last rounding is
\[
 2^{20}+6000(13311)+5(48385)+2(38402)
                      =81233305<2^{27}.
\]
The layer-only exponential remains visible.

## 6. What this supplies to the actual middle problem

For every actual radial resonant mode, including a pure-rotation
resonance, there is now a real compact \(C^9\) metric direction
with the stronger sum \(C_x^4\) norm at most one, both exact first
phase integrals zero, an exactly phase-preserving compensated curve,
and the true normalized derivative bound (C.13).

The direction can depend on that mode and on its true resonant
solution. This theorem does not yet choose one common profile
for infinitely many modes, quantify the compensated second
derivative over a finite parameter interval, or estimate a bad
set of parameters. It also does not identify the radial scalar
Wronskian with the determinant of a coupled nonradial matrix.

All original ordinary and weak source components, both total
physical endpoint traces, bare-flux trace requirements, the
independent mean and height, and positive-DN cross contacts
remain as in the input theorem.
The compact perturbation generally changes mean resistance and
height integrals; the two phase equations do not make those
changes vanish.

To consume (C.14) in the original analytic source spaces, the
pure layer cost must first be converted using a verified
moving-middle frequency lower bound. It cannot be applied to
an entire layer's low-frequency source weight by calling it a
harmless radial power.

## 7. Actual execution

Source:
[scripts/fourfold_phase_preserving_compact_control.mjs](../scripts/fourfold_phase_preserving_compact_control.mjs).

Complete report:
[notes/2026-11-14-R119-phase-preserving-compact-control-rational.json](../notes/2026-11-14-R119-phase-preserving-compact-control-rational.json).

The complete function ran in the available V8 runtime. All 31
normalized BigInt gates passed, covering the local analytic branch,
Cauchy derivatives, compact support and all endpoint jets,
the full \(C^4\) normalization, positive integral, original
Wronskian normalization and every displayed exponent.
The native records a proved uniform construction and its constants;
it does not pretend that a lost numerical resonant trial or a
whole new global profile has been computed.
