# R43 supplement: correlated true root potential through both sides

For the unchanged old R37 actual family, including every original parameter,
every angular mode and the mean, the complete canonical potential now satisfies

\[
 \boxed{|V|<22575.093446}
 \tag{C.1}
\]

on the entire already proved product

\[
 \operatorname{dist}(\xi,[-L,L])\le10^{-5},\qquad
 |\Im\phi|\le1/40000,\qquad L=1/4000.
 \tag{C.2}
\]

The old bound was \(752813.541687\). The factor exceeding \(33.34\) comes
from exact correlations in the same true density and characteristic
equations. The new calculation does not change the potential, substitute
an averaged phase, or drop finite-head paths.

The radial derivative bound \(|V_\xi|<2257509344.518\) holds on real
\(-L\le\xi\le L\), with the same full complex angle strip. It is not
asserted on the radial halo boundary. The exact constant-\(5050\)
negative reference has full height Volterra norm below
\(.000863284171\), including its independent mean. On the positive
finite collar the zero-two-trace coercivity exceeds
\(.999857041550\). These last statements retain their specified boundary
conditions; they are not a new full cap or returned inverse.

## 1. The exact second-order removable quantity

Use the same seven complete analytic fields as the preceding full-root
potential proof. Put \(U=U_0\), \(k=(2U)^{-1}\), and

\[
 C=-\frac{U_\rho+qU_\theta}{U}-q_\theta,\quad
 {\cal W}=G+U/8+\rho U_1/4,
\]
\[
 T=(S_{\rm reg})_\theta-\tfrac12U_{1,\rho}
                        -\tfrac12(q_\theta U_1+qU_{1,\theta}),\qquad
 D=(kL_\theta)_\theta.
 \tag{C.3}
\]

Here \(L_\theta\) is the named original seven-field quantity.
The old exact invariant-density calculation gives

\[
 H=k{\cal W}+\rho C/4+\rho^2kT+\rho^3kD/2,
\]
\[
 V\circ\Psi=
 \frac{N}{\rho^2\Delta^{4/3}},\qquad
 N=(H+5/16){\cal R}-5/16,\qquad
 {\cal R}=\frac{\Delta^2}{F_+F_-}.
 \tag{C.4}
\]

The actual signed fields obey

\[
 (\partial_\rho+(q-\sigma\sqrt\rho\,k)\partial_\theta)F_\sigma
      =CF_\sigma,\qquad F_\sigma(0,\theta)=1.
\]
The exact common equation is

\[
 (\partial_\rho+q\partial_\theta)\Delta
       =\frac3{2\rho}\left(\frac{F_++F_-}{2}-\Delta\right),
 \qquad\Delta(0,\theta)=1.
 \tag{C.5}
\]

The individual signed equations are understood on the square-root cover.
Their product and \(\Delta\) are even and analytic in \(\rho\).
Let \(C_0(\theta)=C(0,\theta)\). Reading the first jets in (C.5) yields

\[
 F_\sigma=1+\rho C_0+O(\rho^2),\qquad
 \Delta=1+\tfrac35\rho C_0+O(\rho^2),\qquad
 {\cal R}=1-\tfrac45\rho C_0+O(\rho^2).
 \tag{C.6}
\]

The earlier exact local canonical construction already proved \(N(0)=
N_\rho(0)=0\); this is qualitative analyticity, independent of the new
bound. Equations (C.4)–(C.6) therefore give \(H_\rho(0)=C_0/4\).
Since \(k(0)\ne0\), they imply the exact true identities

\[
 {\cal W}(0,\theta)={\cal W}_\rho(0,\theta)=0.
 \tag{C.7}
\]

Thus, with \(H=\rho C_0/4+\rho^2H_2\),

\[
 H_2=k({\cal W}/\rho^2+T)
        +\frac{C-C_0}{4\rho}+\frac\rho2kD.
 \tag{C.8}
\]

If \({\cal R}=1-\frac45\rho C_0+\rho^2R_2\), exact multiplication gives

\[
 \boxed{\frac N{\rho^2}
    =H_2{\cal R}-\frac{C_0^2}{5}
                  +\left(\frac{\rho C_0}{4}+\frac5{16}\right)R_2.}
 \tag{C.9}
\]

The cubic cross term is retained in (C.9). No uncertain root coefficient
has been replaced by an exact zero.

## 2. Complete Fourier evaluation and deflation errors

The physical analytic field domain remains
\(R_0=7/25000=.00028\), \(S_0=1/400=.0025\). The new outer evaluation
uses

\[
 R=27/100000=.00027,\qquad S=11/5000=.0022,\qquad
 S_1=3/2000=.0015.
 \tag{C.10}
\]

The degree-80, Fourier-degree-650 center coefficients and their already
paid true-parameter and infinite-field errors are unchanged. Forming
\({\cal W}\) raises the finite radial degree to 81. Deflating its full
finite polynomial retains degrees 2 through 81.

If \(\epsilon_{\cal W}=\epsilon_G+\epsilon_U/8+
R_0\epsilon_{U_1}/4\), the complete error after removing both Taylor
coefficients and dividing by \(\rho^2\) is at most

\[
 \frac{\epsilon_{\cal W}}{R_0^2(1-R/R_0)}.
 \tag{C.11}
\]

Indeed each coefficient \(e_n\) of the full analytic error is bounded
by \(\epsilon_{\cal W}R_0^{-n}\); summing every \(n\ge2\) proves (C.11).
The exact zero identities (C.7), not a small residual interval, justify
the polynomial deflation.

For a field derivative \(\partial_\rho^a\partial_\theta^b\), the true
analytic error is bounded by

\[
 \frac{a!\,b!\,\epsilon}{(R_0-R)^a(S_0-S)^b}.
 \tag{C.12}
\]

Every finite coefficient is evaluated on 128 radial phase cells and 2048
angular cells with directed FFT arithmetic. Its complete cell movement
uses \((n-a)\pi/128+|k|\pi/2048\), multiplied by the full differentiated
coefficient modulus. Both angular boundary signs are supplied by the
actual Schwarz reflection; successive maximum principles supply the
interior. The positive real part of \(U\) is checked before its quotient
is used. In particular the full derivatives

\[
 C_\rho=-\frac{U_{\rho\rho}+q_\rho U_\theta+qU_{\rho\theta}}U
    +\frac{(U_\rho+qU_\theta)U_\rho}{U^2}-q_{\rho\theta},
\]
\[
 C_\theta=-\frac{U_{\rho\theta}+q_\theta U_\theta+qU_{\theta\theta}}U
    +\frac{(U_\rho+qU_\theta)U_\theta}{U^2}-q_{\theta\theta}
 \tag{C.13}
\]

retain every radial, mixed and angular error.

The full closed-bidisk results are:

| Quantity | Complete upper bound |
|---|---:|
| \(|C|\) | \(101.346226095\) |
| \(|C_0|\) | \(94.287603404\) |
| \(|C_\rho|\) | \(19203.037357265\) |
| \(|C_\theta|\) | \(1481.869986952\) |
| \(|q|\) | \(.823358975\) |
| \(|k|\) | \(21.733679045\) |
| \(|{\cal W}/\rho^2|\) | \(430.838970213\) |
| \(|T|\) | \(2485.708081971\) |
| \(|D|\) | \(157.412514990\) |
| \(|H_2|\) | \(14198.342143363\) |

For the last line the actual terms \(k({\cal W}/\rho^2+T)+\rho kD/2\)
are combined on each entire boundary cell before taking their modulus;
the remaining difference in (C.8) costs \(M_{C_\rho}/4\). Holomorphy
extends the resulting bound inward. Directly subtracting independent
interval evaluations of \(C\) and \(C_0\), then dividing by \(\rho\),
gave the poorer bound \(71698.951\). The native retains that diagnostic,
as well as the separate-term bound \(68188.519\), and takes the proved
minimum. It does not claim an improvement from the poorer evaluation.

The complete nested path movement is

\[
 2M_qR+\frac23M_kR^{3/2},
 \qquad
 g=S-S_1-2M_qR-\frac23M_kR^{3/2}>0.
 \tag{C.14}
\]

All common and signed paths below, and the straight angular segments
joining corresponding paths, lie in the strip \(S-g\).
Cauchy therefore gives \(|q_\theta|\le M_q/g\) on precisely those paths.
The native bound is \(M_q/g<4308.424736\). This is a complex path bound;
no purely real derivative bound is substituted.

## 3. Pair both signed densities through the same common flow

Let the genuine auxiliary field \(f\) solve

\[
 D_0f=Cf,\qquad D_0=\partial_\rho+q\partial_\theta,\qquad f(0)=1.
 \tag{C.15}
\]

It is a nonvanishing exponential along the full complex common flow.
Consider a signed and a common backward characteristic with the same
endpoint \((\rho,\theta)\). Along the radial ray, their angular difference
at radius \(s\) is at most

\[
 \frac23M_k e^{(M_q/g)|\rho|}
       (|\rho|^{3/2}-|s|^{3/2}).
\]

Integrating the complete \(C_\theta\) bound gives

\[
 \frac{F_\sigma}{f}=e^{\delta I_\sigma},\qquad
 |\delta I_\sigma|\le K_b|\rho|^{5/2},\qquad
 K_b=\frac25M_kM_{C_\theta}e^{(M_q/g)R}.
 \tag{C.16}
\]

This comparison retains the actual signed drift. It does not replace
either \(F_\sigma\) by \(f\).

Write \(b=K_bR^{5/2}\) and
\(B_b=K_be^b\). The common solution of the \(\Delta\) integral would have
ratio

\[
 Z=\frac32\int_0^1 t^{1/2}
       \exp\!\left[-\int_{t\rho}^{\rho}C(s,\Theta_s)\,ds\right]dt,
 \tag{C.17}
\]

where \(\Theta_\rho=\theta\). Dividing the true \(\Delta\) formula by
\(f(\rho,\theta)\), and using (C.16) at each point of that same common
path, gives

\[
 \frac{\Delta}{f}=Z+\delta Z,\qquad
 |\delta Z|\le D_b|\rho|^{5/2},\qquad
 D_b=\frac38e^{M_CR}B_b.
 \tag{C.18}
\]

The coefficient \(3/8\) is exactly
\((3/2)\int_0^1t^3dt\), with the signed remainder evaluated at
\(t\rho\). All nested paths are within (C.14).

## 4. A correlated second remainder for the full ratio

Let \(M_0\) be the smaller of the native \(|C_0|\) bound and \(M_C\).
Along the common path,

\[
 |C(s,\Theta_s)-C_0(\theta)|
 \le M_{C_\rho}|s|+M_qM_{C_\theta}(|\rho|-|s|).
\]

Using this in (C.17), and Taylor's formula for its scalar exponential,
proves

\[
 Z=1-\frac25\rho C_0+\rho^2E_Z,\qquad |E_Z|\le Z_2,
\]
\[
 Z_2=
 e^{M_CR}\left(\frac27M_{C_\rho}
                  +\frac4{35}M_qM_{C_\theta}\right)
       +\frac4{35}M_0^2e^{M_0R}.
 \tag{C.19}
\]

The coefficients come from the exact weighted moments
\(\mathbb E t=3/5\), \(\mathbb E t^2=3/7\), and
\(\mathbb E(1-t)^2=8/35\) for density \((3/2)t^{1/2}\).
Define

\[
 Z_* =1+\frac25RM_0+R^2Z_2,\qquad
 R_{2,c}=2Z_2+\frac4{25}M_0^2+\frac45RM_0Z_2+R^2Z_2^2.
\]

Then \(|Z|\le Z_*\), and
\(|[Z^2-1+(4/5)\rho C_0]/\rho^2|\le R_{2,c}\).
The true ratio, retaining both signed fields, is exactly

\[
 {\cal R}=(Z+\delta Z)^2e^{-\delta I_+-\delta I_-}.
 \tag{C.20}
\]

Consequently the additional branch fee after dividing by \(\rho^2\) is

\[
 R_{2,b}=e^{2b}\left[
 2Z_*D_b\sqrt R+D_b^2R^3+2Z_*^2K_b\sqrt R\right].
 \tag{C.21}
\]

Thus

\[
 |R_2|\le R_{2,c}+R_{2,b}<17125.455010,\qquad
 |{\cal R}|\le(Z_*+D_bR^{5/2})^2e^{2b}<1.021614564.
 \tag{C.22}
\]

The separate values are \(R_{2,c}<15213.426963\),
\(R_{2,b}<1912.028047\), and \(b<.000049387442\).
In particular the true signed-branch difference has been paid, rather
than declared zero because the common-flow expression is simpler.

## 5. Complete potential, fixed domain and all physical conventions

The already proved \(|\Delta-1|\le e=e^{M_CR}-1<
.027741299362\), together with (C.9), yields

\[
 |V\circ\Psi|\le
 \frac{M_{H_2}M_{\cal R}+M_0^2/5+
             (RM_0/4+5/16)(R_{2,c}+R_{2,b})}
      {(1-e)^{4/3}}
 <22575.093446.
 \tag{C.23}
\]

This is a full physical bidisk bound, including the removable root.
The already proved two-sided canonical inverse has

\[
 |\rho|<.000268958<R,\qquad
 |\Im\theta|<.000560004<S_1
\]

throughout (C.2). The new physical bound therefore applies on that entire
same canonical product, with no new positive-side approximate chart.
Cauchy on a radius-\(10^{-5}\) disk about each real
\(\xi\in[-L,L]\) gives the derivative bound stated above. No such disk
is asserted at the boundary of the halo.

The exact negative equation still has residual \(V-5050\), bounded by
\(27625.093446\). The complete Sonin Green bound
\(|G_{5050}(t,s;n)|\le|t-s|\), including the independent cosine/sine
mean, gives

\[
 \eta\le\frac{L^2}{2}(22575.093446+5050)
 <.000863284171,\qquad
 (1-\eta)^{-1}<1.000864031.
 \tag{C.24}
\]

On the positive side the same exact canonical operator remains
\(-\partial_y^2-y\partial_\phi^2-V(-y,\phi)\).
With zero height at both \(y=0,L\), its relative potential fee is

\[
 L^2M_V/\pi^2<.000142958450.
 \tag{C.25}
\]

This finite Dirichlet statement retains every mode and all mixing,
but does not substitute for the separately specified full-cap boundary
condition.

The old physical ordinary-source Piola factor, the actual positive
height, the conormal height shear, all normalized means, and the
independent regular scalar ports are unchanged. No source is redefined
by (C.15): \(f\) there is only an auxiliary characteristic density.
The full returned \(R^*\), original first phase, high-block cutoff and
complete finite head remain distinct operator obligations.

## 6. Native files and reproducibility

The final complete field calculation is
scripts/fourfold_actual_root_correlated_potential_v2.py, with report
notes/2026-11-13-actual-root-correlated-potential-v2.json.
It took about 259.27 seconds in the shared executor. The preceding
separate-bound producer and report with the same names without _v2
are retained as the smaller earlier calculation; no large intermediate
arrays are saved.

The final exact common-flow consumer is
scripts/fourfold_actual_root_common_flow_potential.py, with report
notes/2026-11-13-actual-root-common-flow-potential.json.
It took about .042 seconds and binds the complete v2 native and all
upstream inputs. Reproduce with fresh outputs:

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_root_correlated_potential_v2.py \
  --out /tmp/actual-root-correlated-potential-v2.json

PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_root_common_flow_potential.py \
  --native /tmp/actual-root-correlated-potential-v2.json \
  --out /tmp/actual-root-common-flow-potential.json
~~~

For completeness, the v2 report also retains the independent initial
ratio bound. If
\(I_2=(M_{C_\rho}+M_qM_{C_\theta})/2+
(2/5)M_kM_{C_\theta}\sqrt R\), then
\[
 E_F=e^{M_CR}I_2+
       \frac{e^{M_CR}-1-M_CR}{R^2},\qquad
 E_\Delta=\frac37E_F+\frac6{35}M_qM_{C_\theta}.
\]
These follow by integrating the exact signed logarithm and (C.5).
Multiplying their full first-jet expansions gives
\[
 P_2=2E_F(1+RM_C)+M_C^2+R^2E_F^2,\quad
 D_2=2E_\Delta+\frac9{25}M_C^2+
              \frac65RM_CE_\Delta+R^2E_\Delta^2,
\]
\[
 |R_2|\le e^{2M_CR}
 \left[D_2+(1+\tfrac45RM_C)P_2+\tfrac85M_C^2\right].
\]
This valid but larger estimate produced \(45998.587108\) after the
pointwise \(H_2\) improvement. The final value (C.1) uses the strictly
more correlated identity (C.20).

