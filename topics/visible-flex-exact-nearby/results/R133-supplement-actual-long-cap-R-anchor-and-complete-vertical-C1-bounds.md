# R133 RA: the actual cap-long R anchor and its complete vertical C1 comparison

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved for the actual M cap-long graph.** At the original
$R=25/8$, construct the frame and position from the actual finite
long solution and its full coframe. In the same fixed world axis
as the original Connection.anchor, the complete vertical rows obey
$$
 \begin{split}
 A_{0,R}
  &=\|e_z^T(Q_R-Q_R^{\rm raw})\|_\infty<10^{-12},\\
 A_{1,R}
  &=\|\partial_\phi e_z^T(Q_R-Q_R^{\rm raw})\|_\infty
                                                    <2\,10^{-12},\\
 B_{1,R}
  &=\|\partial_\phi e_z^T(F_R-F_R^{\rm raw})\|_\infty
                                                     <5\,10^{-20}.
 \end{split}
 \tag{RA.1}
$$
The frame norms are Euclidean row norms and the position norm is
absolute value, on the complete original moving circle. These
bounds include the actual nonmean endpoint $f_*$ and the true
holonomy mean. The unique height translation remains explicit.
A single independent world tilt has the separate columns in
(RA.24); it is not silently reset at each angle.

The constructed endpoint belongs to the actual M cap, including
the selected composition from SCAP when its inputs are used.
It is not the old candidate connection declared exact. Transfer
from $R$ through the actual cap to $L=9/10$, and then through the
core to $b=9/50$, must retain their state differences.

## 1. Exact source object and the original raw anchor

Use the following completed sources:

- [M: the actual full two-input cap-long graph](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md);
- [O: the actual long graph for M's full endpoint domain](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md);
- [D: the original finite long Dirichlet solution and its full mean](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md);
- [LV: the exact horizontal coframe and complete vector reconstruction](R144-supplement-complete-long-horizontal-coframe-and-vector-tame-graph.md);
- [the full moving frame and its residual convention](R133-supplement-moving-frame-with-complete-residual-and-mean.md);
- [the original complete model's fixed world placement](R133-supplement-complete-141-block-continuous-model-geometry.md);
- [SCAP: the actual selected cap composition](R133-supplement-actual-selected-cap-and-complete-height-feedback-absorption.md).

The original raw formula is exactly
[Connection.anchor](../scripts/fourfold_codazzi_moving_connection_frame_probe.py),
source blob 8357d7e11a49450adba99803163f77a8bbfc1388. It uses
$$
 \Theta_{\rm raw}(\phi)
   =\phi+\frac1{m_{\rm raw}}I_\phi(v_{\rm raw}-m_{\rm raw}),
 \quad
 \rho_R=\frac{\beta_R}{\gamma_R},\quad
 z_R=-a_R C_{\rm ref}(R),
 \tag{RA.2}
$$
and, writing $e_r(\theta)=(\cos\theta,\sin\theta)$ and
$e_\theta(\theta)=(-\sin\theta,\cos\theta)$,
$$
 \begin{split}
 X_R^{\rm raw}&=(\rho_Re_r(\Theta_{\rm raw}),z_R),\\
 Y_R^{\rm raw}&=(e_\theta(\Theta_{\rm raw}),0),\\
 N_R^{\rm raw}&=(z_Re_r(\Theta_{\rm raw}),-\rho_R),\\
 F_R^{\rm raw}&=(a_Re_r(\Theta_{\rm raw}),H_*),\\
 H_*&=4347844570122155/4503599627370496 .
 \end{split}
 \tag{RA.3}
$$
The code itself has zero vertical position; $H_*e_z$ is the single
fixed world translation in the complete-model proof G.1.
Its $C_{\rm ref}$ is the original rotational target, not the
unknown actual cap C field. The frame $Q=(X,Y,N)$ has determinant
$-1$, with the normal pointing as in the original model.

The actual cap keeps the same intrinsic data and $\eta_0$.
The compact intrinsic modification supported in $(.05,.18)$
does not change this endpoint or the positive cap. The actual
S/T design bumps likewise do not change the long segment or its
B section. Nothing in this result changes a radial reference,
replaces the old raw candidate by its continuous repair, or
chooses a different world translation for each angle.

## 2. The actual M long domain, without using a smaller Z ball

Write the genuine long coordinate as
$$
 t=\log(a/a_B),\quad 0\le t\le\mathcal L,\quad
 a(t)=a_Be^t,\quad w(t)=a(t)/(4\omega),\quad
 q=w^2,\quad E=1+q.
 \tag{RA.4}
$$
The true cap endpoint is $t=\mathcal L$, $a=a_R=a_*$.
The already proved physical numbers are
$$
 0<a_R<7\,10^{-6},\qquad 7/5<\omega<3/2,\qquad
                 w_R<1/800000 .
 \tag{RA.5}
$$
These are D.1--D.2 and the same original R74.2--R74.3, with
the actual finite endpoint and all reflected Green terms retained.

For every actual M input in its original product,
$$
 \|f_B\|_{\dot A^2}\le2^{-60},\qquad
 f_*=\Phi_\gamma(f_B),\qquad\|f_*\|_{\dot A^2}<10^{-8}.
 \tag{RA.6}
$$
O.2 applies the original finite long kernels and nonlinear
Dirichlet proof at width zero to precisely these data.
Let $Y=\|h\|_{\mathcal Y_A}$, where the full angular Wiener norm
uses the sum of the coefficientwise radial suprema of
$|m|^2h_m$, $|m|(h_m)_t$ and $(h_m)_{tt}$.
The actual solved graph has $Y\le2^{-20}$ and satisfies
$$
 Y\le16d_\partial+2^{14}Y^2,\qquad
 d_\partial=\|f_B\|_{\dot A^2}+\|f_*\|_{\dot A^2}.
$$
Consequently
$$
 Y\le\frac{1024}{63}d_\partial
 <\frac{1024}{63}(10^{-8}+2^{-60})
 <Y_R^\#:=\frac1{6000000}.
 \tag{RA.7}
$$
This is a new consequence of the existing solved graph and its
actual endpoint values. It does not rerun the long PDE or its
Green estimates.

Use the complete states
$$
 P=h_\theta,\quad U=h_{\theta\theta},\quad
 K=2h+h_t+\kappa,\quad V=2h_\theta+h_{t\theta}.
 \tag{RA.8}
$$
D.8--D.9 retain the actual holonomy root and give
$$
 \|\kappa\|_\infty\le256Y^2,\qquad
 \|W\|_A:=\|P\|_A+\|K\|_A+\|U\|_A+\|V\|_A
          <4Y<r_R^\#:=\frac1{1500000}.
 \tag{RA.9}
$$
In particular the algebraic coframe domain $\|W\|_A<1/64$
in LV.3 is available. We use LV's exact coframe and its algebraic
identities on this actual M graph. We do not apply LG's smaller
right-curvature existence ball to the larger M domain.

All modes and both actual endpoints remain. Only two angular
derivatives and the actual mixed derivative in $\mathcal Y_A$
are needed for the frame's first angular derivative. No spatial
analyticity or extra high angular norm is assumed small.

## 3. Actual position, true mean and one horizontal coframe

Let $Z_{\rm rot}(a)$ be the original northern rotational height,
with $Z_{\rm rot}(a_R)=H_*$ and $(Z_{\rm rot})_a=-w$.
The actual height is
$$
 \begin{split}
 Z(a,\theta)&=Z_{\rm rot}(a)-\lambda-aw\{h(t,\theta)+c(t)\},\\
 c(t)&=\int_0^t e^{-2(t-s)}\kappa(s)\,ds,\qquad c(0)=0 .
 \end{split}
 \tag{RA.10}
$$
It follows that
$$
 Z_a=-w(1+K),\qquad Z_\theta=-awP,\qquad
 |c|\le128Y^2 .
 \tag{RA.11}
$$
Thus the actual mean-height span is not set to zero. There is one
$\lambda$, and the two endpoint mean heights are linked by (RA.10).

For the horizontal coframe set, exactly as in LV,
$$
 T=1-qP^2,\quad
 S=2K+K^2+EP^2,\quad
 D=1-qS,\quad
 A=\sqrt T,\quad
 b=\sqrt{D/T},\quad
 a_1=-q(1+K)P/\sqrt T,
$$
$$
 G=\frac{1+q(1+K)U/T}{\sqrt D}.
 \tag{RA.12}
$$
The full solved equations and holonomy root give
$\langle G\rangle=1$ and the actual flat coframe. Keep its true
phase from LV.8,
$$
 \vartheta=I_\theta(G-1)+\psi+
             \int_0^t q(s)\langle H_0(s)\rangle\,ds .
 \tag{RA.13}
$$
In the original even-reflection class $\langle H_0\rangle=0$.
The same single $\psi$ applies at both ends. It is the axial
component of one world rotation, not a separate angle-dependent
frame choice.

The exact horizontal map satisfies
$$
 F_h=e^{i\theta}\mathcal R,\qquad
 (\partial_\theta+i)\mathcal R=i\,aA e^{i\vartheta},
 \qquad
 (F_h)_a=e^{i(\theta+\vartheta)}(b+i a_1).
 \tag{RA.14}
$$
The multiplier $i(4j+1)$ is invertible on every full fourfold mode.
This defines the actual periodic horizontal position, with one
constant horizontal translation if desired. Its compatibility
is the original full Darboux equation, including the mean.
It is not a reconstruction of an off-shell trial.

Together (RA.10) and (RA.14) give the actual long immersion
$F=(F_h,Z)$ and its true cap-facing Cauchy data. M's true
curvature endpoint graph matches its complete B/C data, so this
is a legitimate $R$ anchor for that actual cap. It is not an
independently guessed normal/position pair.

At $R$ the full vertical value is
$$
 e_z^T(F_R-F_R^{\rm raw})
       =-\lambda-a_Rw_R\{f_*(\Theta_*(\phi))+c(\mathcal L)\}.
 \tag{RA.15}
$$
The zero-frequency contribution is explicit. The actual
nonmean/mean bounds also give
$$
 |a_Rw_Rc(\mathcal L)|<4\,10^{-23},\qquad
 \|e_z^T(F_R-F_R^{\rm raw})+\lambda\|_\infty<6\,10^{-21}.
 \tag{RA.16}
$$
The first uses the unscreened mean integral in (RA.10), and the
second uses $\|f_*\|_{A^0}\le\|f_*\|_{\dot A^2}/16$.
These are physical height units. They do not remove $\lambda$
or prescribe a second endpoint mean height.

## 4. Actual orthonormal frame and its exact vertical row

In the physical $a,\theta$ chart define
$$
          X=-F_a/\sqrt E,\qquad
          Y=F_\theta/a,\qquad N=-X\times Y .
 \tag{RA.17}
$$
The minus sign in $X$ is the original increasing-core-radius
orientation: on the true long segment $a$ decreases as the
original outward radial variable increases. Thus (RA.17)
uses the original meridian frame. The metric gives
$Q^TQ=I$ and $\det Q=-1$, exactly as in (RA.3).

For completeness, with $\alpha=\theta+\vartheta$, the three
columns are
$$
 \begin{split}
 X&=\left(-\frac{e^{i\alpha}(b+i a_1)}{\sqrt E},
                         \frac{w(1+K)}{\sqrt E}\right),\\
 Y&=\left(i A e^{i\alpha},-wP\right),\\
 N&=\left(\frac{w e^{i\alpha}}{\sqrt E}
                     \left(\frac{1+K}{A}+i bP\right),
                         \frac{\sqrt D}{\sqrt E}\right).
 \end{split}
 \tag{RA.18}
$$
Here a complex horizontal component denotes its two real
Cartesian coordinates. The normal formula follows from
$A(1+K)-a_1P=(1+K)/A$; no sign from the determinant of the
absolute frame has been dropped.

At the unperturbed long graph, (R74.3)'s
$a_u=-\omega a$, $z_u=a^2/4$ give
$$
 \frac{\beta_R}{\gamma_R}=-\frac1{\sqrt{E_R}},
 \qquad
 -a_RC_{\rm ref}(R)=\frac{w_R}{\sqrt{E_R}} .
 \tag{RA.19}
$$
The same relations are invariant under the positive radial
rescaling $u=4c_0(r-R)$. For example the rotational angular
curvature is $C_{\rm ref}=-1/(4\omega\sqrt E)$.
Thus (RA.18) reduces to the exact raw frame convention (RA.3)
on the radial graph, and its actual vertical row is
$$
 e_z^TQ_R
 =\left(\frac{w_R(1+K)}{\sqrt E_R},
                     -w_RP,\frac{\sqrt D}{\sqrt E_R}\right),
 \qquad
 e_z^TQ_R^{\rm raw}
 =\left(\frac{w_R}{\sqrt E_R},0,\frac1{\sqrt E_R}\right).
 \tag{RA.20}
$$
The raw row is constant in its angle, even when its original
$\Theta_{\rm raw}$ is nontrivial. Therefore the vertical
comparison requires no unpaid small operator norm for a
composition-minus-identity map.

## 5. The original moving angle and the three complete R bounds

The actual M curvature mean is $c_0=\langle C_*(R)\rangle$,
with $|c_0|>1/7$. The actual nonmean endpoint obeys
$$
 \|C_{*,\ne0}(R)\|_{A^0}
   \le\|Z_0\|_{A^0}
        +\|(x_*)_{C,\ne0}(R)\|_{A^0}<10^{-9}.
$$
Set $j=C_*/c_0$. Then
$\|j-1\|_{A^0}<7\,10^{-9}$.
The complete physical-to-moving angle and its inverse are
$$
 \Phi_*(\theta)=\theta+I_\theta(j-1),\qquad
 \Theta_*=\Phi_*^{-1},\qquad
             0<(\Theta_*)_\phi<2 .
 \tag{RA.21}
$$
The reflection symmetry fixes $\Phi_*(0)=\Theta_*(0)=0$.
Equivalently the actual moving state has
$v_*=1/C_*\circ\Theta_*$ and $m_*=1/c_0$, so
$(\Theta_*)_\phi=v_*/m_*$ and
$\Theta_*=\phi+I_\phi(v_*-m_*)/m_*$.
This is exactly the normalization in Connection.anchor.
There is no extra unassigned constant phase.

At $R$ write $r=r_R^\#$ and $w=w_R$. From (RA.9) and (RA.12),
$|S|\le(2+3r)r<3r$ and $D>1/4$. The Euclidean row difference
in (RA.20) is bounded by its component sum:
$$
 \|\Delta q_R\|_\infty
 \le w(\|K\|_\infty+\|P\|_\infty)
              +q\|S\|_\infty
 \le(w+3w^2)r<10^{-12}.
 \tag{RA.22}
$$
This includes the actual mean in $K$.

The exact physical angular derivative is
$$
 \partial_\theta\Delta q_R
  =\left(\frac{wV}{\sqrt E},-wU,
       -\frac{q\{(1+K)V+EPU\}}{\sqrt E\sqrt D}\right).
$$
Because $r<1/2$, $E<2$ and $1/\sqrt D<2$, the same
component-sum bound is at most $(w+3w^2)r$.
Passing to the actual original moving angle multiplies
this derivative by $(\Theta_*)_\phi<2$.
The raw vertical row has derivative zero, so this proves
the first two lines of (RA.1) on the same full $\phi$ circle.

For the position, the constant raw height $H_*$ and the
single $\lambda$ have zero angular derivative. Since
$P(R)=(f_*)_\theta$ and all nonzero physical frequencies
have absolute value at least4,
$$
 \|\partial_\phi e_z^T(F_R-F_R^{\rm raw})\|_\infty
 \le2a_Rw_R\|(f_*)_\theta\|_\infty
 \le\frac{a_Rw_R}{2}\|f_*\|_{\dot A^2}
 <5\,10^{-20}.
 \tag{RA.23}
$$
Using the actual Dirichlet endpoint here is substantially
stronger than replacing $P(R)$ by the whole-state bound.
All quantities are full Fourier quantities, not values on
a sampled angular grid.

## 6. One world placement and its independent ports

The estimates (RA.1) use the original world axis and one
common axial orientation. Any constant axial rotation
preserves all three vertical observations. Constant
horizontal translations and the one vertical height
translation also preserve them.

For a general additional fixed world rotation $O$ set
$\vartheta_O=\|e_z^T(O-I)\|_2$. The actual world placement
is $Q^{\rm world}=OQ^{\rm can}$,
$F^{\rm world}=OF^{\rm can}+X$.
Use the vertical component of this one position $X$ to
represent $\lambda$; do not introduce a second independent
vertical translation. The full norm bounds are
$$
 \begin{split}
 A_{0,R}^{\rm world}
    &<10^{-12}+\vartheta_O,\\
 A_{1,R}^{\rm world}
    &<2\,10^{-12}+4\vartheta_O,\\
 B_{1,R}^{\rm world}
    &<5\,10^{-20}+14\,10^{-6}\vartheta_O .
 \end{split}
 \tag{RA.24}
$$
Indeed $Q$ is orthogonal. In the physical angle its complete
connection has coefficients
$(\beta/\gamma,aB_*,aC_*)$. M/CC give at this endpoint
$|B_*|<1/128$, $|C_*|<1/3$, so the connection's operator
norm is below2. By (RA.21), $\|Q_\phi\|_{\rm op}<4$.
Also $\|F_\phi\|=a_R(\Theta_*)_\phi<14\,10^{-6}$.
This proves every coefficient in (RA.24) without a hidden
direction or dimension factor.

If the world frame or position is itself varied in a
parameter direction, retain the exact additional terms
$\dot Q=\dot OQ^{\rm can}+O\dot Q^{\rm can}$ and
$\dot F=\dot OF^{\rm can}+O\dot F^{\rm can}+\dot X$.
The independent angular boundary rows used in a world
variation likewise remain actual inputs. The small static
bounds (RA.1) do not set those derivative ports to zero.

## 7. Exact qualification for the next radial transfer

This proof constructs the actual R endpoint of the same
M cap-long solution. For selected inputs it is the cap of
SCAP, with its true $f_\gamma$, actual full mean, and a
single compatible exterior/world reconstruction.
It does not replace that cap's state on $[9/10,25/8]$
by the old raw candidate or by a core-only affine
$Q_\delta$ estimate.

The next same-world propagation must therefore compare
the true M cap to the original raw reference on this
whole cap, with its real inverse-angle map and continuous
repair error. Only after reaching $L=9/10$ can the
separately paid selected-core comparison be used on
$[b,L]$. Original residuals, angular defects and real
interfaces remain in that propagation.

The 10 new exact rational/integer combinations in the
saved-bound reader were evaluated once and all passed.
They only combine the already solved M/D long bounds
with the true physical R scales, mean recovery, angle
map and complete frame formulas above. No scientific
target, angular/native geometry, old Green kernel or
old numerical conclusion was recomputed.
