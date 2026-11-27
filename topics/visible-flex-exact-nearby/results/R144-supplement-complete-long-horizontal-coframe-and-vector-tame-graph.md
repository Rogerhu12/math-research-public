# R144 LV: the complete long horizontal coframe and vector tame graph

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 28 new saved-rational combinations pass.** The actual finite long graph of LG has a complete horizontal
reconstruction, including its true radial rotation mean, at every angular
order. Its value, first parameter derivative and Hessian are controlled in
the strong Fourier norm of coefficientwise radial suprema of all physical
two-jets. After the actual curvature chart, the estimates lose three
directional angular derivatives and contain only one high endpoint
background factor. The two height means, two endpoint slopes, one initial
rotation and the world position/frame ports remain explicit.

This supplies the vector reconstruction missing from LG. It concerns the
same finite long annulus and its two genuine ends. It does not solve the
body-to-annulus matching equations or replace the remaining far-end
simultaneous selection problem.

## LV1. The actual graph, full Fourier states and physical jets

Use the physical angle and actual finite long interval of
[LG.1--LG.13](R144-supplement-all-angular-strong-long-height-graph-with-complete-means.md).
Write

$$
 \begin{gathered}
 q=w^2,\qquad E=1+q,\qquad a_t=a,\quad q_t=2q,\\
 P=h_\theta,\quad U=h_{\theta\theta},\quad
 K=2h+h_t+\kappa,\quad V=2h_\theta+h_{t\theta},\\
 W=(P,K,U,V).
 \end{gathered}
 \tag{LV.1}
$$

The same holonomy-one root is \(\kappa\). In particular the complete
equations, including the mean, are

$$
 \begin{gathered}
 K_t=\mathcal Q_{\rm full}-2K-U,\qquad P_t=V-2P,\\
 K_\theta=V,\qquad P_\theta=U,\\
 \mathcal Q_{\rm full}
 ={E(V-P)^2+K^2+2EKU+EU^2-qP^2\over1+K+EU}.
 \end{gathered}
 \tag{LV.2}
$$

All frequencies in \(4\mathbb Z\) are retained. For a radial Fourier
coefficient use its \(C_t^0\) norm before the Fourier sum.
The state algebra is the component sum of these \(\ell^1(C_t^0)\)
norms, and its direction module is the component sum of
\(\ell^2(\langle k\rangle^{2n};C_t^0)\).
The exact linear map from \(\mathcal H=(h,\kappa,c)\) in LG to \(W\)
has module norm at most \(4\), at every order. Thus throughout the
wide physical function-parameter ball of LG,

$$
 \|W\|_{\mathcal A}<8r_y<1/128,\qquad r_y=2^{-24}.
 \tag{LV.3}
$$

No spatial analyticity is imposed on an unknown \(W\).

For a horizontal map \(F_h\), define its six rotating jet entries,
with the reference planar map subtracted, by

$$
 \begin{gathered}
 J_0=e^{-i\theta}F_h-a,\qquad
 J_a=e^{-i\theta}(F_h)_a-1,\qquad
 J_\theta=e^{-i\theta}a^{-1}(F_h)_\theta-i,\\
 J_{aa}=e^{-i\theta}(F_h)_{aa},\\
 J_{a\theta}=e^{-i\theta}
       \{a^{-1}(F_h)_{a\theta}-a^{-2}(F_h)_\theta\},\\
 J_{\theta\theta}=e^{-i\theta}
       \{a^{-2}(F_h)_{\theta\theta}+a^{-1}(F_h)_a\}.
 \end{gathered}
 \tag{LV.4}
$$

The last three are precisely the Hessian in an orthonormal polar
input frame. Define \(\mathfrak J_n\) as the sum of the six
\(\ell^2(\langle k\rangle^{2n};C_t^0)\) norms, counting the mixed
entry twice; its algebra version uses \(\ell^1\).
This stronger radial norm is not inferred from a pointwise Sobolev
estimate. The formulas below act directly on the coefficientwise
radial Banach spaces.

## LV2. The missing radial rotation mean

The exact original coframe is
[119.22--119.24](R119-actual-final-connector-all-label-continuation.md).
In the present variables put

$$
 \begin{gathered}
 T=1-qP^2,\qquad
 S=2K+K^2+EP^2,\qquad D=1-qS,\\
 A=\sqrt T,\qquad
 b=\sqrt{D/T},\qquad a_1=-{q(1+K)P\over\sqrt T},\\
 G={1+q(1+K)U/T\over\sqrt D}.
 \end{gathered}
 \tag{LV.5}
$$

Square roots are their actual branches near \(1\).
The original holonomy equation is exactly \(\langle G\rangle=1\).
Here \(k=w(1+K)\), \(p=wP\) and \(l=aA\) in the original notation.
Define the full scalar-free angular expression

$$
 H_0=-{(1+K)PG\over T}
       +{(1+K)V+EPU\over\sqrt D\,T}
       -{\sqrt D\,PU\over T^2}.
 \tag{LV.6}
$$

Direct differentiation of \(b\), using only
\(K_\theta=V\) and \(P_\theta=U\), gives the exact identity

$$
 {a_1G-b_\theta\over aA}={q\over a}H_0 .
 \tag{LV.7}
$$

Let \(I_\theta\) be the original zero-mean primitive on nonzero
\(4\mathbb Z\), with norm at most \(1/4\).
Keep one initial rotation \(\psi\), and set

$$
 \begin{gathered}
 \rho(t)=\psi+\int_0^t q(s)\langle H_0(s)\rangle\,ds,\\
 \gamma(t,\theta)=I_\theta(G-1)+\rho(t).
 \end{gathered}
 \tag{LV.8}
$$

On the genuine solved graph the complete Darboux equation says
\(G_t=q\,\partial_\theta H_0\). Equivalently this is the vanishing
curvature of the original flat horizontal coframe; it follows from
the two full equations in (LV.2), with no discarded mean.
Consequently

$$
                  \gamma_\theta=G-1,\qquad
                  \gamma_t=qH_0 .
 \tag{LV.9}
$$

The second identity would in general fail if \(\rho\) were deleted.
For the original even-reflection subclass, \(P,V,H_0\) are odd
and \(K,U,G\) even. Then \(\langle H_0\rangle=0\), and (LV.8)
is exactly the old reflection gauge with constant \(\psi\).
For a general full Fourier direction, its radial rotation mean
and both of its parameter derivatives must instead be retained.

Choose \(\psi=0\) only to express the canonical graph below.
Since \(q_t=2q\), its normalized rotation is

$$
 {\gamma\over q}
   = I_\theta {G-1\over q}
      +\int_0^t e^{-2(t-s)}\langle H_0(s)\rangle\,ds .
 \tag{LV.10}
$$

The integral has norm at most \(1/2\), independent of the actual
long length. No inverse of the extremely small \(q(0)\) is used.
The two endpoint rotation values are linked by the exact integral
in (LV.8); they are not independently specifiable.

The actual horizontal map is

$$
 \begin{gathered}
 F_h=e^{i\theta}R,\qquad
 (\partial_\theta+i)R=i\,aA e^{i\gamma},\\
 R_a=e^{i\gamma}(b+i a_1).
 \end{gathered}
 \tag{LV.11}
$$

The first equation determines \(R\) uniquely in the full
\(4\mathbb Z\) space: every multiplier \(i(k+1)\) is invertible
and its inverse has norm at most \(1\).
The real and imaginary coframe compatibility equations are
\(\gamma_a=(a_1G-b_\theta)/(aA)\) and
\((aA)_a=(a_1)_\theta+bG\).
Together with (LV.9), these prove the second equation in
(LV.11) for that same \(R\).
There is no horizontal translation period: the horizontal
one-form has frequencies \(4j+1\), never zero.

For real data,
\[
 |(F_h)_a|^2=E-k^2,\qquad
 |(F_h)_\theta|^2=a^2(1-p^2),\qquad
 (F_h)_a\cdot(F_h)_\theta=-a k p .
\]
Adding the actual height \(Z_0-v\), whose two derivatives are
\(-k\) and \(-ap\), gives exactly
\((1+w^2)da^2+a^2d\theta^2\).
Thus this is the complete vector surface inducing the same
metric, including for the full Fourier graph.

## LV3. A complete physical two-jet bound without height third derivatives

All estimates in this section hold in the coefficientwise radial
algebra, and in its square-zero direction module.
Take \(\|W\|\le r=1/64\); this is an algebraic neighborhood of
the actual graph, not a new long-PDE existence domain.
Use \(q\le1\), \(E\le2\).
The bounds \(\|S\|\le(2+3r)r<3r\) and
\(\|1-T\|\le r^2\) give all the needed reciprocal and square-root
norms below \(2\), while
\(\|(1+\sqrt D)^{-1}\|\), \(\|(1+\sqrt T)^{-1}\|<1\).
Also \(\|b^2-1\|\le2(2r+2r^2)<1/8\), so
\(\|(1+b)^{-1}\|<1\).

The apparent divisions by \(q\) have the following exact removable
expressions:

$$
 \begin{gathered}
 {G-1\over q}
 ={S\over\sqrt D(1+\sqrt D)}
       +{(1+K)U\over T\sqrt D},\\
 {A-1\over q}=-{P^2\over1+\sqrt T},\qquad
 {b-1\over q}=-{2K+K^2+qP^2\over T(1+b)},\\
 {a_1\over q}=-{(1+K)P\over\sqrt T}.
 \end{gathered}
 \tag{LV.12}
$$

Their norms are at most \(16r,r^2,5r,4r\), respectively;
\(\|G\|<2\) and \(\|H_0\|<32r\).
Equation (LV.10) then gives \(\|\gamma/q\|<32r\).
Since \(q\|\gamma/q\|\le1/2\), the power series for the
exponential gives

$$
 \|e^{i\gamma}\|<2,\qquad
 \left\|{e^{i\gamma}-1\over q}\right\|<64r .
 \tag{LV.13}
$$

Equations (LV.11)--(LV.13) bound the value and the two first
jet entries, in their true physical scales, by

$$
 \|J_0\|<128\,a q\,r,\qquad
 \|J_a\|,\|J_\theta\|<128\,q\,r .
 \tag{LV.14}
$$

For the second jets do not differentiate \(U\) or \(V\)
radially. The complete equation in (LV.2) gives

$$
 \begin{gathered}
 \|\mathcal Q_{\rm full}\|\le32r^2,\qquad
 \|K_t\|<4r,\quad \|P_t\|<3r,\\
 \|D_t/q\|<23r,\qquad \|T_t/q\|\le8r^2,\\
 \|b_t/q\|<64r,\quad \|(a_1)_t/q\|<32r,\\
 \|b_\theta/q\|<16r,\quad
 \|(a_1)_\theta/q\|<8r,\quad \|A_\theta/q\|<r .
 \end{gathered}
 \tag{LV.15}
$$

For example \(S_t=2(1+K)K_t+2qP^2+2EP P_t\),
\(D_t=-q(2S+S_t)\), and
\(T_t=-2q(P^2+P P_t)\).
These are identities in the four-state algebra.
The exact second-jet formulas are

$$
 \begin{aligned}
 J_{aa}
 &= {e^{i\gamma}\over a}
     \{b_t+i(a_1)_t+iqH_0(b+i a_1)\},\\
 J_{a\theta}
 &= {e^{i\gamma}\over a}
       \{i(Gb-A)-G a_1+b_\theta+i(a_1)_\theta\},\\
 J_{\theta\theta}
 &= {e^{i\gamma}\over a}
       \{b-GA+i(a_1+A_\theta)\}.
 \end{aligned}
 \tag{LV.16}
$$

In particular no height third derivative is present.
Both \((Gb-A)/q\) and \((b-GA)/q\) have norm below \(38r\).
The resulting three bounds are

$$
 \|J_{aa}\|<512{q\over a}r,\qquad
 \|J_{a\theta}\|<256{q\over a}r,\qquad
 \|J_{\theta\theta}\|<128{q\over a}r .
 \tag{LV.17}
$$

Put

$$
 \beta_*=\sup_{0\le t\le L}{q(t)\over a(t)}
       ={q(L)\over a(L)}
       <{7\,10^{-6}\over16}.
 \tag{LV.18}
$$

This is the already proved physical coefficient in
[D.29--D.30](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md).
Since \(a<1\), both \(a q\) and \(q\) are bounded by \(q/a\).
Counting the mixed Hessian entry twice,
\(3(128)+512+2(256)+128=1536<2^{12}\).
Hence the full algebra jet map satisfies

$$
                       \|\mathcal J(W)\|_{\mathfrak J_A}
                    \le2^{12}\beta_*\|W\|_{\mathcal A}.
 \tag{LV.19}
$$

For arbitrary algebraic \(W\), use (LV.10)--(LV.12) for the
value and first jets, and (LV.2), (LV.15)--(LV.16) to define
the formal second jets. These are holomorphic formulas on
the displayed ball. On the genuine solved graph all of them
are compatible actual physical jets.
Thus the graph's parameter derivatives are actual two-jet
derivatives, by the closed compatible-jet identities.
This is the same precise use of an algebraic jet extension
as in LG.9--LG.11; it does not solve a different off-shell PDE.

## LV4. The genuine strong direction module

The proof of (LV.19) uses only bounded coefficientwise products,
means, the primitive, the radial exponential integral, and absolutely
convergent reciprocal, root and exponential series.
The same proof therefore holds in the normed square-zero algebra
\(\mathcal A\oplus\varepsilon\mathcal M_0\).
It does not assume that an arbitrary \(L^2\) direction is Wiener.
For a base state of norm at most \(1/128\), give the distinguished
direction amplitude \(1/128\); its total norm is at most \(1/64\).
The full output norm in (LV.19) is at most \(64\beta_*\).
The actual direction coefficient is consequently bounded by

$$
             \|D_W\mathcal J:\mathcal M_0\to\mathfrak J_0\|
                            \le2^{13}\beta_* .
 \tag{LV.20}
$$

This is also obtained by the same power-series Cauchy estimate
in that square-zero algebra. In particular it is a module
bound for the radial suprema, not a deduction from a scalar
Wiener value estimate alone.

Compose with the actual wide graph \(\mathcal H(Z,g)\) of LG.
Its full two-column module norm is below \(2^{15}\), and
\(\mathcal H\mapsto W\) has norm at most \(4\).
The holomorphic family of complete horizontal jet derivatives
therefore has the uniform bound

$$
 \|D_Z\mathcal J\|+\|D_g\mathcal J\|
       \le M_{\rm hor}:=2^{30}\beta_* .
 \tag{LV.21}
$$

All its scalar rotation outputs are the actual integrals in
(LV.8). They are included even when the output angular
frequency is zero.
The wide value bound is
\(\|\mathcal J\|_{\mathfrak J_A}<2^{15}\beta_*r_y\).

## LV5. Every angular order and one high background factor

Use the exact physical parameter mass and moments \(\Gamma_n\)
from LG.14, including \(\Gamma_0=1\), and the explicit

$$
 J_n=2^{2n+4}(n+1)!,\qquad
 K_n=2^{2n+44}(n+1)!
 \tag{LV.22}
$$

from [OX.15](R144-supplement-physical-output-boundary-differential-and-all-angular-Hessian.md).
For physical curvature/height direction pairs \(X,Y\),

$$
 \begin{aligned}
 \|D\mathcal J[Y]\|_{\mathfrak J_n}
 &\le M_{\rm hor}J_n
          \{|Y|_{H^n}+\Gamma_n|Y|_{L^2}\},\\
 \|D^2\mathcal J[X,Y]\|_{\mathfrak J_n}
 &\le M_{\rm hor}K_n
   \{|X|_{A^0}|Y|_{H^n}
       +|X|_{A^n}|Y|_{L^2}
       +\Gamma_n|X|_{A^0}|Y|_{L^2}\}.
 \end{aligned}
 \tag{LV.23}
$$

Indeed the entire map into the rotating jets is angular-translation
covariant. The shifted inverse \((\partial_\theta+i)^{-1}\)
commutes with translations, and the additional scalar mean
integral in (LV.8) does so as well.
Taylor coefficients of the actual operator family in (LV.21)
thus have the complete frequency-conserving convolution bounds
\(3^dM_{\rm hor}\).
Take the norm of each full output radial coefficient before
the nonnegative convolution sum. Young's
\(\ell^1*\ell^2\to\ell^2\) inequality applies in precisely
\(\mathfrak J_n\).
The same complete Taylor moment sums OX.23--OX.26 then give
(LV.23), including all zero-frequency output paths.

An all-order value bound, by the corresponding value-series
argument in LG.16, is

$$
 \|\mathcal J(Z,g)\|_{\mathfrak J_n}
       \le2^{2n+20}(n+1)!\,\beta_*r_y(1+\Gamma_n).
 \tag{LV.24}
$$

No product of two strong \(L^2(C_t)\) direction states has been
estimated here. In particular there is no hidden extra loss
from making a direction into a radial Wiener multiplier.
The second derivative is bounded as a derivative of the whole
actual boundary-parameter family, with one algebra direction
and one direction-module factor, exactly as in LG3.

Now take the actual endpoint curvature chart
\[
 \widehat{\mathcal J}(Q,g)
   =\mathcal J(P_{\perp,\theta}(C_Q-C_{\rm ref}),g).
\]
Use \(E_s,B_s,P_n,C_n,\mathcal T_n\) exactly as OX.13--OX.16:
\[
 E_s(h,p)=\|h_1\|_{H^s_\phi}+\|h_2\|_{H^s_\phi}
                    +\|p\|_{H^s_\theta},\qquad
 B_s=1+\|Q(R)\|_{A^s,\oplus_1},
\]
\[
 \mathcal T_n(x,y)
   =E_{n+3}(x)E_3(y)+E_{n+3}(y)E_3(x)
                         +B_{n+2}E_3(x)E_3(y).
\]
Here \(p=|D_\theta|^2\dot f_B\), and the raw endpoint
directions are genuine separately supplied endpoint data.
The output remains in the fixed physical angle.
Exactly the two chart chain-rule terms used in LG4 give

$$
 \boxed{\begin{aligned}
 \|D\widehat{\mathcal J}[x]\|_{\mathfrak J_n}
 &\le2^{30}\beta_* C_n
           \{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 \|D^2\widehat{\mathcal J}[x,y]\|_{\mathfrak J_n}
 &\le2^{30}\beta_* C_n\,\mathcal T_n(x,y).
 \end{aligned}}
 \tag{LV.25}
$$

The low factors use the already paid OX.29 low chart bounds;
only one factor receives a high chart estimate.
Thus no square of \(B_{n+2}\) is introduced.
The unknown endpoint still only needs the original
\(A^3\le10^{-9}\) neighborhood; no high norm is required small.
All actual cap curvature means and the independent left
height remain those of LG/OX.

## LV6. Complete vector jets, endpoint outputs and genuine rigid ports

The physical-height two-jet reconstruction (LG.20) is a linear
map from \(\mathfrak Y_n\) to the same coefficientwise radial
two-jet module, of norm at most \(16\).
The \(11/10\) embedding factor in LG.21 is only needed when
taking pointwise angular suprema, not for this module statement.
Combine (LG.18) with (LV.25) and define

$$
       M_{\rm vec}=2^{30}\beta_*+2^{19},\qquad
       C^{\rm vec}_n=4^{n+2}M_{\rm vec}C_n .
 \tag{LV.26}
$$

Changing the polar input frame and the rotating output frame
to fixed Cartesian components is multiplication by trigonometric
polynomials with shifts of absolute size at most \(3\).
The total component-sum charge is at most \(16\), and
\(\langle k+\ell\rangle^n\le4^n\langle k\rangle^n\)
for \(|\ell|\le3\). Hence, for the complete canonical vector
graph \(\widehat F=(F_h,Z_0-v)\), its actual Cartesian two-jets
obey

$$
 \begin{aligned}
 \|D\widehat F[x]\|_{{\rm Cart},n}
 &\le C^{\rm vec}_n
           \{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 \|D^2\widehat F[x,y]\|_{{\rm Cart},n}
 &\le C^{\rm vec}_n\,\mathcal T_n(x,y).
 \end{aligned}
 \tag{LV.27}
$$

The independent constant vertical translation contributes
exactly \(-\dot\lambda e_z\) at first order and zero Hessian.
For actual physical \(C^2\) estimates, the full integer-frequency
Cauchy--Schwarz embedding at order \(1\) costs less than \(2\).
In particular

$$
 \begin{aligned}
 \|D\widehat F[x,\dot\lambda]\|_{C^2}
 &\le2C^{\rm vec}_1\{E_4(x)+B_3E_3(x)\}+|\dot\lambda|,\\
 \|D^2\widehat F[x,y]\|_{C^2}
 &\le2C^{\rm vec}_1\mathcal T_1(x,y).
 \end{aligned}
 \tag{LV.28}
$$

These are genuine strong derivatives. Smooth Fourier inputs
give compatible classical jets; the complete module estimates
pass to their limits, and the unique low long graph identifies
those limits. No raw angular composition inside a radial
supremum space has been used.
Taylor remainders and differences follow by integrating the
actual Hessian (LV.27) on a segment in the same admitted domain.
In particular their terms have exactly one high direction
factor or one \(B_{n+2}\) times two low direction factors.

At both actual endpoints, restrict (LV.11), (LV.16) and the
full height traces (LG.19). These restrictions are bounded
observations of the displayed strong modules, and include
the full horizontal radial/angle coframe, both mean slopes,
the actual mean-height difference, and the rotation difference
\[
             \rho(L)-\rho(0)=\int_0^Lq\langle H_0\rangle\,dt .
\]
No endpoint is replaced by an infinite end or given a new
independent phase/height mean. The outward radial signs at
the two ends remain opposite.

The canonical origin and \(\psi=0\) were only coordinates for
the estimates. A genuine world placement is an independent
rigid frame \(O\in SO(3)\) and position \(X\in\mathbb R^3\):
\[
                        F^{\rm world}=O F^{\rm can}+X .
\]
The initial axial phase is the corresponding axial component
of \(O\); the one overall height translation is the corresponding
position component in the chosen local frame. They must not
be fixed afresh at the other endpoint or counted as extra
independent mean conditions.
For a local exponential frame chart, the exact additional
derivative columns and mixed Hessian terms are

$$
 \begin{aligned}
 DF^{\rm world}[x,\Omega,\xi]
    &=O\{DF^{\rm can}[x]+\Omega F^{\rm can}\}+\xi,\\
 D^2F^{\rm world}[(x,\Omega,\xi),(y,\Lambda,\zeta)]
    &=O\{D^2F^{\rm can}[x,y]
          +\Omega DF^{\rm can}[y]+\Lambda DF^{\rm can}[x]\\
    &\hspace{32mm}
          +\tfrac12(\Omega\Lambda+\Lambda\Omega)F^{\rm can}\}.
 \end{aligned}
 \tag{LV.29}
$$

These finite rigid columns keep their actual value factors;
they are not assigned the small \(\beta_*\) fee of a cap
curvature variation. For the scalar axial phase, this simply
says \(F_h^\psi=e^{i\psi}F_h^{\rm can}+X_h\), with
\(\partial_\psi F_h^\psi=i e^{i\psi}F_h^{\rm can}\).

Finally, on the actual real wide graph, (LV.3) and (LV.19)
give a complete horizontal Cartesian perturbation smaller
than \(10^{-7}\), including the component frame charge \(16\).
A path inside the physical annulus joining two points can
be chosen with length less than \(3\) times their Euclidean
distance: use the smaller-radius arc followed by a radial
segment. Thus the horizontal perturbation has Lipschitz
constant below \(3\,10^{-7}<1\); its projection is injective.
The entire actual finite long vector graph is therefore a
\(C^2\) embedded annulus. This local annulus conclusion
does not assert that the remaining body, far connector and
world placement equations have been solved.

## LV7. New saved-rational combinations

The companion
[reader](../scripts/fourfold_codazzi_long_vector_tame_saved_bounds.py)
only combines the completed \(r_y\), wide derivative columns,
actual \(q/a\) bound and the explicit algebraic fees above.
It does not read or regenerate an old long solution, native
coefficient array, reference Green function, or completed
scientific target.
