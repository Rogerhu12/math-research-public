# R147 RH: relative world-height carriers and short full-frequency error bounds

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**New proved bounds.** On the original selected background \(Q_\delta\),
with the actual fixed \(\eta_0\) and \(|\delta_*|<10^{-10}\), the complete
fixed-metric state derivative of the short passive position map satisfies

\[
 \|D_Qx(0)[e]\|_{L^2_\phi}<\frac{36}{25}
       \|e\|_{L^2([0,9/50];L^2_\phi)},\qquad
 \|\operatorname{ax}(D_QA(0)[e]A(0)^T)\|_{L^2_\phi}
 <\frac{17}{16}\|e\|_{L^2_rL^2_\phi}.                 \tag{RH.1}
\]

These bounds include both moving means and the full infinite Fourier
response. Here \(A,x\) are **relative** frame and position, precisely
defined below; no physical outer frame or position is set to \(I,0\).
The axial norm of a skew matrix equals its spectral norm, not its
Frobenius norm. A Frobenius convention would cost \(\sqrt2\).

For the completed original strict parameter trial \(h^a\), the actual
full-frequency error therefore costs less than \(9.742568\,10^{-6}\)
in relative position and \(7.188527\,10^{-6}\) in axial frame. For a
fixed physical height test, the complete body-and-angle error is (RH.17),
which keeps the actual off-shell \(F_\phi\) row and its true mean.
The current work does not claim an already computed signed height value
or an already available exact world-anchor carrier.

## RH1. Same original selected scalar and state bounds

Put \(b=9/50\). The completed original
[SP scalar conclusions, Sections 3.5 and 4.1](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md)
and [SJA](R133-supplement-actual-complete-strict-radial-first-symbol-defect.md)
apply on a larger original strict interval and a larger selected
parameter box. Their restriction to \([0,b]\) gives

\[
\begin{gathered}
 -m> M:=16/15,\quad |\beta|<B:=211/1000,\quad
 1<\gamma<G:=28/25,\quad |K|<K_*:=21/20,\\
 q=\sqrt{-K}>.5338,\quad q<q_*:=103/100,\qquad
 \sqrt{u^2+q^2v^2}<R_*:=239/125.                         \tag{RH.2}
\end{gathered}
\]

In particular \(|u|<U:=R_*\) and \(|v|<V:=18/5\).
The complete original mean lower is larger than 1.068732504; the
original complete \(\gamma\) lower is larger than 1.037358753.
These are lower bounds, not reciprocals manufactured from an upper.
The complete SJA source is run 43768006977/1, execution SHA256
`2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88`.
The original SP source is run 43731464771/1, execution SHA256
`a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12`.

SP also gives \(a(0)<1.068733119\). Since \(a'/a=\beta\),
positivity and \(e^z\le(1-z)^{-1}\) for \(0\le z<1\) give

\[
       0<a(r)\le\frac{1.068733119}{1-Bb}<a_*:=9/8.
                                                               \tag{RH.3}
\]

No pointwise endpoint upper has been passed directly to the whole
interval. No compact mean-exact centre or its newer metric is substituted.

All angular norms below use normalized measure. On the fourfold period
\(L=\pi/2\), the original zero-mean primitive \(I\) satisfies

\[
 \|I\|_{L^2\to L^2}=1/4,\qquad
 \|I\|_{L^\infty\to L^\infty}\le L/4=\pi/8<2/5.        \tag{RH.4}
\]

For the second statement use its sawtooth convolution kernel
\(L/2-t\), \(0<t<L\): its normalized absolute integral is \(L/4\).
This primitive removes the mean of its own input; it does not discard
the mean of the physical state before products are formed.

## RH2. The exact relative carrier and all independent anchors

Use the same complete passive reconstruction as
[PH.18--24](R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md):

\[
\begin{gathered}
 d=-\beta I(u^2+Kv^2),\quad J=v/m,\quad \tau=dJ-\gamma u,\\
 p=\beta\tau/\gamma,\quad k=a(\gamma Kv+du/m),\quad t=ad/m,\\
 \mathsf M=\Omega(p,k,t),\qquad c=(a\gamma,a\tau,0)^T,
\end{gathered}
\]

where \(\Omega(p,k,t)_{12}=-p\), \(\Omega_{13}=-k\),
\(\Omega_{23}=-t\), with the remaining entries determined by skew
symmetry. The connection \(\mathsf M\) is distinct from the positive
constant \(M=16/15\). For each real angular label define the unique
relative carriers

\[
 A_r=A\mathsf M,\quad A(b)=I_3,\qquad
 x_r=Ac,\quad x(b)=0.                                  \tag{RH.5}
\]

Real skew symmetry gives \(A(r)\in SO(3)\). If the actual physical
anchor at \(b\) is \((Q_b,F_b)\), then exactly

\[
        Q(r)=Q_bA(r),\qquad F(r)=F_b+Q_bx(r).             \tag{RH.6}
\]

The identity and zero in (RH.5) choose relative coordinates only.
The actual \(Q_b(\phi),F_b(\phi)\) can be nonconstant functions of
the angular label; the true global vertical covector is not rotated
separately at each label. If the original data are specified at a
farther outer endpoint \(R\), their entire propagation to \(b\)
supplies these anchors. Local state support does not supply them.

For a variation \((h,\kappa)\), put
\(U_f=\dot A A^T\), \(y=\dot x\). Direct differentiation, without
using any Gauss--Codazzi equation, gives

\[
 (U_f)_r=A\dot{\mathsf M}A^T,\quad U_f(b)=0,\qquad
 y_r=U_fAc+A\dot c,\quad y(b)=0.                        \tag{RH.7}
\]

For independent physical terminal ports \(Y_b=\dot F_b\) and
\(K_b=\dot Q_bQ_b^T\), the actual variation is

\[
 \boxed{\dot F(0)=Y_b+K_bQ_bx(0)+Q_by(0).}              \tag{RH.8}
\]

All original identity transmissions are used in these equations.
If genuine affine frame or position jumps are prescribed, their
independent values enter the ordered propagations as impulses; they
are not charged a radial length and are not included for free in
the ordinary \(L^2_r\) estimate. For the difference of the original
NP particular and its frozen trial those additional passive ports
are fixed equal. The original complete NP state jumps were exactly
zero, as recorded in ASB; no new jump residual is discarded.

## RH3. Entire state and true metric columns

Let \(\mu=\Pi h_2\). The complete linearizations are

\[
\begin{aligned}
 \dot d&=-2\beta I(uh_1+Kvh_2)-\kappa\beta K_\nu I(v^2),\\
 \dot J&=(h_2-J\mu)/m,\\
 \dot\tau&=J\dot d+d\dot J-\gamma h_1-\kappa\gamma_\nu u,\\
 \dot p&=(\beta/\gamma)\dot\tau
              -\kappa\beta\tau\gamma_\nu/\gamma^2,\\
 \dot k&=a\left[\gamma K h_2+
       \kappa(\gamma_\nu K+\gamma K_\nu)v
       +u\dot d/m+dh_1/m-du\mu/m^2\right],\\
 \dot t&=a(\dot d/m-d\mu/m^2),\qquad
 \dot c=(\kappa a\gamma_\nu,a\dot\tau,0)^T.             \tag{RH.9}
\end{aligned}
\]

Here \(a_\nu=\beta_\nu=0\),
\(\gamma_\nu=w\gamma/2\),
\(K_\nu=-wK+Tw'\), and \(T=\beta/(2a^2\gamma^2)\), exactly as
in PH. The whole compact bump and its derivative remain. In particular
the selected true \(\nu\) column is (RH.7) with \((h,\kappa)=(v_\nu,1)\),
not just the state derivative with \(\kappa=0\).

When comparing it with \((h^a,1)\) **at the same selected background**,
the direct metric terms cancel by linearity and the difference is
(RH.7),(RH.9) with \((e,0)\), \(e=v_\nu-h^a\). This does not cancel
the direct metric contribution in either signed functional itself.
An evaluation at the old base \(Q_0\) would additionally need its
own complete selected-background row fee.

## RH4. Full moving-mean rank-one norm and short connection bounds

Write \(h_2=h_\perp+\mu\), \(J=1+j\), where both \(h_\perp\) and
\(j\) have zero mean. Thus
\(\dot J=(h_\perp-j\mu)/m\). The exact operator from
\(L^2_0\oplus\mathbb R\) to \(L^2_0\) has norm
\(\sqrt{1+\|j\|_2^2}/|m|=\|v\|_2/m^2\). Therefore, including
the original even mean,

\[
 \|\dot J\|_2\le C_J\|h_2\|_2,\qquad C_J:=V/M^2.
                                                               \tag{RH.10}
\]

Set
\[
 D=(2/5)BR_*^2,\quad J_*=V/M,\quad C_d=Bq_*R_*/2.
\]
The complete pointwise radius in (RH.2) gives
\(|u^2+Kv^2|\le R_*^2\), so \(|d|\le D\), and (RH.4) gives
\(\|\dot d\|_2\le C_d\|h\|_2\) at fixed metric. Full products,
including their mean mixing, are bounded before applying \(I\).
For the same derivative,

\[
\begin{aligned}
 C_\tau&\le J_*C_d+\sqrt{G^2+(DC_J)^2}<11/5,\\
 C_p&\le B(11/5)<15/32,\\
 C_t&\le a_*(C_d/M+D/M^2)<17/32,\\
 C_k&\le a_*\left[UC_d/M+
          \sqrt{(D/M)^2+(GK_*+DU/M^2)^2}\right]<19/8.
                                                               \tag{RH.11}
\end{aligned}
\]

The second square root groups the \(h_1\) and full \(h_2\) channels;
the term \(DU/M^2\) pays the independent \(\mu\) term rather than
setting it to zero. Consequently

\[
 \|\operatorname{ax}(\dot{\mathsf M})\|_2
 \le C_M\|h\|_2,\quad C_M<5/2,\qquad
 \|\dot c\|_2\le C_c\|h\|_2,\quad C_c<5/2.             \tag{RH.12}
\]

Also the full base velocity obeys

\[
 |c|\le a_*\sqrt{G^2+(DJ_*+GU)^2}<C_0:=19/5.           \tag{RH.13}
\]

Every displayed strict inequality is a new exact-rational consequence
of the complete saved scalar bounds. The
[small rational consumer](../scripts/fourfold_codazzi_relative_height_saved_bounds.py)
checks them by positive squaring; it does not evaluate a field or rerun
any old target. There is no Fourier truncation in (RH.10--13).

## RH5. Orthogonal Duhamel gives the position and frame receivers

Orthogonal conjugation preserves axial norm. From (RH.7), for
\(E(r)=\|e(r)\|_2\), Minkowski and a change of integration order give

\[
 \|\operatorname{ax}U_f(0)\|_2\le C_M\int_0^bE(r)dr,
\quad
 \|y(0)\|_2\le\int_0^b(C_c+C_MC_0r)E(r)dr.             \tag{RH.14}
\]

The whole second integral is essential: the frame variation acts on
position accumulated over all earlier radii. Cauchy--Schwarz proves
(RH.1), because

\[
 C_M^2b<(17/16)^2,\qquad
 C_c^2b+C_cC_MC_0b^2+(C_MC_0)^2b^3/3<(36/25)^2.
                                                               \tag{RH.15}
\]

For a fixed physical test \(\zeta_\theta\), the actual positive
waist diffeomorphism is \(\Theta=\phi+Iv/m\), \(J=\Theta_\phi\).
Its positivity follows from the original complete
[waist chart](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
on the stated original selected subset. At that same waist,
\(0<J<J_*\). Exact change of variables gives
\(\|\zeta_\theta(\Theta)J\|_2^2\le
J_*\|\zeta_\theta\|_2^2\). Since \(Q_b\) is orthogonal, the body
part of the world-height receiver is less than
\((36/25)\sqrt{J_*}<53/20\). This does not pay the independent
physical-coordinate term, which follows next.

## RH6. The complete physical angle term and actual NP error

At the waist, set \(C_\theta=\zeta_\theta(\Theta)e_z\cdot F_\phi\),
where \(F\) is the same actual physical base position. The exact
fixed-physical height derivative from PH.23 is

\[
 D\mathcal H_{\zeta_\theta}[h,\kappa;Y_b,K_b]
 =\left\langle\zeta_\theta(\Theta)J,
       e_z\cdot(Y_b+K_bQ_bx+Q_by)\right\rangle
       -\langle C_\theta,\dot\Theta\rangle,
\quad \dot\Theta=Ih_2/m-(Iv)\mu/m^2.                   \tag{RH.16}
\]

The whole two-mean primitive error controls
\(\|\dot\Theta[e]\|_2\) by
\(\sqrt{M^{-2}+V^2/(16M^4)}\|(Ie,\Pi e)\|<
(5/4)\|(Ie,\Pi e)\|\). This uses the **already proved uniform**
primitive-and-mean estimate at the waist; it does not take a trace of
an ordinary radial \(L^2\) bound.

[ASB](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md)
gives the entire same-background bounds
\(\|e\|_{L^2_rL^2}<6.765672\,10^{-6}\) and
\(\sup_r\|(Ie,\Pi e)(r)\|<1.132677\,10^{-6}\).
For equal independent terminal/affine ports the exact error therefore is

\[
\boxed{
 |D\mathcal H_{\zeta_\theta}[v_\nu,1]
          -D\mathcal H_{\zeta_\theta}[h^a,1]|
 <1.792904\,10^{-5}\|\zeta_\theta\|_2
   +1.415847\,10^{-6}\|C_\theta\|_2 .}                 \tag{RH.17}
\]

The position and axial-frame errors stated after (RH.1) follow from
the same complete \(L^2_rL^2\) error. These constants pay the entire
unknown Fourier tail of \(e\), including any modes beyond the trial
degree and both means. Only the original degree160 baseline residual
in ASB received its factor641; no such finite-degree claim is made
for the selected \(Q_\delta\) operator or for \(e\).

The coefficient \(C_\theta\) in (RH.17) is not silently assigned a
numerical bound. Its actual off-shell identity is
\(F_\phi=Q(c_\phi+P)\), with the original angular reconstruction
defect \(P\). Replacing it by \(Qc_\phi\) would change the row.
The ordinary equivalent PH.24 includes the constant
\(\langle C_\theta,Iv\rangle/m^2\), so even the mean of the state
variation is retained. Constant and cosine height tests do not vanish
from reflection merely because the strict state has local support.

## RH7. Concrete remaining signed carrier, without a false endpoint shortcut

Equations (RH.5),(RH.7),(RH.9) specify the required short relative
carrier for the already fixed NP trial. Its scalar integration must
use all original candidate/scalar pieces, actual selected parameter
fees and every whole NP array; (RH.17) then converts a complete
same-background trial pairing into the true particular pairing.
No old NP residual, norm, physical observation or amplitude pairing
must be rerun for this operation.

A physical signed height value additionally requires the actual
same-world \(Q_b,F_b\) and genuine \(F_\phi(0)\), or an equivalent
full outer-to-waist passive carrier with its independent anchor data.
The exact transformation (RH.6),(RH.8),(RH.16) is the interface for
that input. A relative initialization \(I,0\) alone supplies none
of those physical anchors. This is why a short relative carrier can
be computed as a useful new object without claiming that it already
equals an absolute physical height column.

The independent mean, phase, rigid-motion and height ports are still
separate original equations. This proof neither identifies their
Schur complement with a scalar mean gate nor declares the complete
topic finished.
