# R133 supplement: residual-sensitive vector height and full Airy contact

2026-11-14, phase_inverse. **Exact theorem, with 27 rational/Laurent
polynomial gates actually executed.** The background is the final
moving M32 centre with manifest

    ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413

and the same \(\alpha=6890507429876859/9007199254740992\),
\(\nu=-2572625729470897/72057594037927936\).
The root-germ numerical statements retain the whole original
\(|\eta_{\rm original}|\le10^{-9}\) interval.

This is the missing **contact identity** between actual passive
position variations and the moving curvature unknown. It is valid
at the unsolved centre. It uses all three Euclidean position
components and therefore requires no unproved lower bound for one
fixed component \(N_z\) of the normal. The complete base residual,
its linearized ordinary source, the even curvature mean, both
frame/position rigid ports, and the actual PPoly jumps remain.

The principal two-row normalization proves why the negative
quadratic-density gauge has the height-wave order \(-3/2\), and
why the corresponding current root curvature state must be scaled
by \(nM^{-5/3}\). Lower contact terms are not set to zero. In
particular the term containing the base position defect times the
curvature variation is a genuine order-zero feedback. This theorem
does not absorb that feedback or supply a whole-body inverse.

## 1. Same actual connection, without assuming an isometry

Use the notation and signs of
[R133's complete moving frame](R133-supplement-moving-frame-with-complete-residual-and-mean.md).
Write the moving state as \(\mathsf q=(u,v)\),
\(m=\langle v\rangle<0\), \(J=v/m>0\), and set

\[
 S=u^2+Kv^2,\quad d=-\beta I S,\quad
 \tau=dJ-\gamma u,\quad
 \theta=\phi+\frac1m I(v-m).                            \tag{H.1}
\]

Here \(I=\partial_\phi^{-1}P_{\ne0}\) is the actual fourfold,
zero-mean primitive. The complete ordinary residual is

\[
 R_u=u_r-F_1(\mathsf q),\quad R_v=v_r-F_2(\mathsf q),
 \quad R_0=\langle R_v\rangle,\quad
 m_r=\beta m(1-\langle S\rangle)+R_0 .                  \tag{H.2}
\]

The real coordinate derivative is

\[
 \theta_r=\tau+\rho,\qquad
 \rho=\frac1m I\left(R_v-\frac v mR_0\right),\qquad
 J_r=(\tau+\rho)_\phi .                                \tag{H.3}
\]

We do not replace \(\theta_r\) by \(\tau\).
For
\[
 \Omega(x,y,z)=
 \begin{pmatrix}0&-x&-y\\x&0&-z\\y&z&0\end{pmatrix},
\]
define the same complete radial and angular matrices
\[
\begin{split}
 M&=\Omega\left(\frac{\beta\tau}{\gamma},
       a(\gamma Kv+du/m),\,ad/m\right),\\
 L&=\Omega\left(\frac{\beta v}{\gamma m},\,au/m,\,a/m\right),\\
 {\bf c}_r&=(a\gamma,a\tau,0)^T,\qquad
 {\bf c}_\phi=(0,aJ,0)^T .                              \tag{H.4}
\end{split}
\]

All coefficients in (H.4) are those of the current centre.
In particular they contain no pointwise \(1/v\) in the radial
reconstruction. Let the actual radial reconstruction be
\[
 {\cal Q}_r={\cal Q}M,\qquad F_r={\cal Q}{\bf c}_r,
\tag{H.5}
\]
with the supplied orthogonal frame and position data.
The columns of \({\cal Q}\) are denoted \(X,Y,N\).
Only orthogonality is used; no orientation-dependent axial-vector
identification of skew matrices is needed.

Define complete component defects
\[
 E={\cal Q}^T{\cal Q}_\phi-L,\qquad
 P={\cal Q}^TF_\phi-{\bf c}_\phi,\qquad
 \widehat L=L+E,\quad {\bf t}={\bf c}_\phi+P .
\tag{H.6}
\]
Thus \({\cal Q}_\phi={\cal Q}\widehat L\) and
\(F_\phi={\cal Q}{\bf t}\) are exact even off shell.

The already proved curvature and torsion are
\[
\begin{split}
 {\cal R}&=L_r-M_\phi+[M,L]\\
 &=\Omega\left(
 \frac{\beta}{\gamma m}(R_v-vR_0/m),\
 \frac a m(R_u-uR_0/m),\
 -\frac a{m^2}R_0\right),\\
 {\cal T}&=(0,\ a(R_v-vR_0/m)/m,\ 0)^T .
\end{split}                                                       \tag{H.7}
\]
Consequently
\[
 E_r=[E,M]-{\cal R},\qquad
 P_r=-MP+E{\bf c}_r-{\cal T}.                           \tag{H.8}
\]

These are true defect equations for the reconstruction (H.5).
Their homogeneous propagations are orthogonal, including the
commutator propagation on skew matrices. Their sources do not
differentiate \(R_u,R_v\) in the angular variable.

## 2. Full linearized source and mean

Let \(h=(h_1,h_2)\) be a variation at fixed target metric and set
\(z=\langle h_2\rangle\). Its complete ordinary source is
\[
 g=h_r-DF(\mathsf q)h,\qquad g_0=\langle g_2\rangle.
\tag{H.9}
\]
Thus \(\delta R_u=g_1,\delta R_v=g_2,\delta R_0=g_0\).
This does not suppose \(g=0\) or \(R=0\).
At the present root germ the compact \(\nu\) bump is identically
zero; the physical \(\nu\) source has zero target variation there.
Elsewhere, a metric variation must be included by differentiating
the target coefficients in (H.4) and (H.7), rather than discarded.

For later exact consumption define
\[
\begin{split}
 G_v={}&g_2/m-R_vz/m^2-h_2R_0/m^2-vg_0/m^2
                                     +2vR_0z/m^3,\\
 G_u={}&g_1/m-R_uz/m^2-h_1R_0/m^2-ug_0/m^2
                                     +2uR_0z/m^3 .
\end{split}                                                       \tag{H.10}
\]
Then the full linearized defects are
\[
 \delta{\cal R}=
 \Omega\left(\frac\beta\gamma G_v,\ aG_u,\
             -ag_0/m^2+2aR_0z/m^3\right),\qquad
 \delta{\cal T}=(0,aG_v,0)^T .                         \tag{H.11}
\]

All of the terms linear in the base residual and the true mean
\(z,g_0\) are necessary. These formulas have been checked as
identities in the Laurent polynomial ring with \(m\ne0\), rather
than at sampled values.

The other radial variations are obtained without source derivatives:
\[
\begin{split}
 \delta d&=-2\beta I(uh_1+Kvh_2),\\
 \delta J&=h_2/m-vz/m^2,\\
 \delta\tau&=(\delta d)J+d\,\delta J-\gamma h_1,\\
 \delta M&=\Omega\left(
   \beta\delta\tau/\gamma,\
   a(\gamma Kh_2+\delta d\,u/m+d h_1/m-duz/m^2),\
   a(\delta d/m-dz/m^2)\right),\\
 \delta{\bf c}_r&=(0,a\delta\tau,0)^T .
\end{split}                                                       \tag{H.12}
\]

Let
\[
 S_f={\cal Q}^T\delta{\cal Q},\quad V={\cal Q}^T\delta F,
 \quad E_1=\delta E,\quad P_1=\delta P .
\]
Then \(S_f\) is skew, and direct differentiation gives
\[
\begin{split}
 (S_f)_r&=[S_f,M]+\delta M,\\
 (E_1)_r&=[E_1,M]+[E,\delta M]-\delta{\cal R},\\
 (P_1)_r&=-MP_1-\delta M\,P+E_1{\bf c}_r
                          +E\delta{\bf c}_r-\delta{\cal T}.
\end{split}                                                       \tag{H.13}
\]

For instance the full \(L^2_\phi\) source estimate is
\[
 \|E_1(r)\|_2\le\|E_1(r_0)\|_2+
 \int_{r_0}^r
  \bigl(2\|E\|_\infty\|\delta M\|_2+
                    \|\delta{\cal R}\|_2\bigr)\,dt
\tag{H.14}
\]
in the forward direction, with reversed limits for the other
direction. The analogous position inequality has integrand
\[
 \|\delta M\|_2\|P\|_\infty+
 \|E_1\|_2|{\bf c}_r|_\infty+
 \|E\|_\infty\|\delta{\bf c}_r\|_2+
 \|\delta{\cal T}\|_2 .
\tag{H.15}
\]
Initial geometric ports and all interfaces must be added.
There is no omitted exponential norm of a skew homogeneous
propagator. Angular differentiated estimates require their
corresponding full product bounds; they are not granted by
(H.14) alone.

## 3. True passive angle and cancellation of the false first-order height term

The coordinate variation at fixed moving angle is
\[
 \delta\theta=\frac1m I(h_2-zv/m).
\]
Its genuine material displacement in the moving label is
\[
 \chi=\frac{\delta\theta}{J}
      =\frac1v I(h_2-zv/m),\qquad
 \chi_\phi=\frac{h_2-v_\phi\chi}{v}-\frac z m .
\tag{H.16}
\]
The actual fixed-physical-angle state variation, pulled to the
base moving label, is
\[
 k=h-\mathsf q_\phi\chi,\qquad
 b=\delta B=\frac{k_1}{v}-\frac{u k_2}{v^2},\qquad
 c=\delta C=-\frac{k_2}{v^2}.                           \tag{H.17}
\]
These \(b,c\) are true variations of the reconstructed state
\(B=u/v,C=1/v\). The pointwise \(v\)-gap needed in (H.16)--(H.17)
is supplied by the current joint germ. The resulting relation
does not identify a moving mean with a physical mean.

The full variation of the residual coordinate drift is
\[
 \delta\rho=-\frac z m\rho+
 \frac1m I\left(g_2-\frac{h_2R_0}{m}
               -\frac{vg_0}{m}+\frac{vR_0z}{m^2}\right).
\tag{H.18}
\]
It follows that
\[
 \chi_r=\frac{\delta\tau+\delta\rho-\chi J_r}{J}.
\tag{H.19}
\]
All right sides in (H.18)--(H.19) keep the true means and use
ordinary \(g\), not \(g_\phi\).

The angular position column has the decisive exact identity
\[
                 \delta{\bf c}_\phi
                     =\partial_\phi({\bf c}_\phi\chi).
\tag{H.20}
\]
It follows from
\(v_\phi\chi+v\chi_\phi=h_2-vz/m\).
Without (H.20), an active moving position variation contains a
spurious first-order primitive of curvature and cannot be used
as the desired height state.

Define the actual passive quantities
\[
 W=S_f-\widehat L\chi,\qquad
 U=V-{\bf t}\chi,\qquad
 {\bf z}={\cal Q}U=\delta F-F_\phi\chi.                 \tag{H.21}
\]
The vector \({\bf z}\) is precisely the physical-angle variation
of the actual radially reconstructed position, pulled to its
base moving angle. This is an identity for the current centre;
it does not assert that its reconstructed position is already
isometric.

Write
\[
 \mathfrak E=E_1-\partial_\phi(E\chi),\qquad
 \Pi=P_1-\partial_\phi(P\chi),                         \tag{H.22}
\]
and introduce the full radial position source
\[
 \Psi=-a e_2(\delta\rho-\chi\rho_\phi)-P\chi_r .
\tag{H.23}
\]
The source (H.23) is genuinely residual-sensitive. In particular
it is zero when the base residual, the ordinary source and the
base position defect are all zero.

Let \(\nabla_\phi V=V_\phi+\widehat L V\) for vectors and
\(\nabla_\phi^{\rm ad}W=W_\phi+[\widehat L,W]\) for skew matrices.
Then the complete contact equations are
\[
\boxed{
\begin{split}
 \nabla_\phi^{\rm ad}W
    &=J\,\Omega(0,ab,ac)+\mathfrak E,\\
 \nabla_\phi U&=W{\bf t}+\Pi,\\
 U_r+MU&=W{\bf c}_r+\Psi .
\end{split}}
\tag{H.24}
\]

Here is an explicit check of the first line. The angular connection
variation satisfies
\[
 \delta L-\partial_\phi(L\chi)=J\,\Omega(0,ab,ac).
\tag{H.25}
\]
Its first coefficient is exactly zero; the next two are
\(a(k_1-uk_2/v)/m\) and \(-ak_2/(mv)\).
The Levi--Civita angular component therefore has not acquired a
false variation. Combining (H.25) with (H.22) proves that line.
The second line follows from (H.20).

For the third line, exact mixed derivatives of \(F\) give
\({\bf t}_r+M{\bf t}=({\bf c}_r)_\phi+\widehat L{\bf c}_r\).
The uncancelled radial vector is
\(\delta{\bf c}_r-({\bf c}_r)_\phi\chi-{\bf t}\chi_r\).
Its \(e_2\) coefficient, excluding \(-P\chi_r\), is
\(a(\delta\tau-\tau_\phi\chi-J\chi_r)\).
Equations (H.3) and (H.19) reduce this exactly to
\(-a(\delta\rho-\chi\rho_\phi)\), as asserted.

## 4. Vector heights, full rigid ports and actual means

The matrix and vector ambient forms of (H.24) are
\[
\begin{split}
 \partial_\phi({\cal Q}W{\cal Q}^T)
  &={\cal Q}[J\Omega(0,ab,ac)+\mathfrak E]{\cal Q}^T,\\
 {\bf z}_\phi
  &=({\cal Q}W{\cal Q}^T)F_\phi+{\cal Q}\Pi,\\
 {\bf z}_r
  &=({\cal Q}W{\cal Q}^T)F_r+{\cal Q}\Psi .
\end{split}                                                       \tag{H.26}
\]
Thus the rotation and position traces are two successive angular
contact equations. Their periodic primitives retain the ambient
rotation and translation constants and the full zero-mode
compatibility equations. They are not inverted by deleting the
constant coefficient of curvature.

The ambient vector components are considered on the full \(2\pi\)
circle. Under fourfold symmetry their horizontal components are
equivariant, not individually \(\pi/2\)-periodic. The body-frame
scalar contractions below are \(\pi/2\)-periodic and have physical
frequencies \(4j\). No factor-four primitive estimate is applied
to an arbitrary ambient horizontal component.

A fixed scalar height \(e\cdot{\bf z}\) may be used on a patch
where \(e\cdot N\) has a proved nonzero gap. We do not need such
a patch or claim it is already certified. The vector formulas
(H.24)--(H.26) are global and only use \(|N|=1\), which follows
from the skew radial frame. All rigid variations remain: for
example a translation can have a nonconstant \(N\cdot{\bf z}\);
its apparent principal derivatives are cancelled by the complete
lower contact terms below. It must not be discarded by a
high-mode projection of that scalar height alone.

## 5. Exact two-row curvature contact, with no \(q^{-1}\)

Put \(n=a^2/m^2\) and \(\eta=-\gamma m>0\).
For the scalar contact defects define
\[
\begin{split}
 B_\phi={}&e_3^T\{
      J\Omega(0,ab,ac)P+\mathfrak E{\bf t}
                     +W\nabla_\phi{\bf t}+\widehat L\Pi\},\\
 B_r={}&e_3^T\{
      \mathfrak E{\bf c}_r
                     +W\nabla_\phi{\bf c}_r+\widehat L\Psi\},\\
 C_\phi={}&B_\phi+\partial_\phi\Pi_3,\qquad
 C_r=B_r+\partial_\phi\Psi_3 .
\end{split}                                                       \tag{H.27}
\]

These are definitions of complete expressions. The first term of
\(B_\phi\) explicitly contains the base position defect times the
full curvature variation \((b,c)\). It is not a smoothing term.

Differentiating (H.24) in the actual angle gives exactly
\[
\begin{split}
 N\cdot{\bf z}_{\phi\phi}
      &=a^2J^2c+C_\phi,\\
 N\cdot{\bf z}_{r\phi}
      &=a^2J(\gamma b+\tau c)+C_r .
\end{split}                                                       \tag{H.28}
\]
For example \(J\Omega(0,ab,ac){\bf c}_\phi\) has third
component \(a^2J^2c\). All other terms are precisely those
in (H.27).

Using \(\tau+\gamma u=dJ\), (H.17) and (H.28) give
\[
\boxed{
\begin{split}
 n h_1={}&-\eta^{-1}N\cdot
                ({\bf z}_{r\phi}-d{\bf z}_{\phi\phi})
       +\eta^{-1}(C_r-dC_\phi)+n u_\phi\chi,\\
 n h_2={}&-N\cdot{\bf z}_{\phi\phi}
                              +C_\phi+n v_\phi\chi .
\end{split}}
\tag{H.29}
\]
The coefficients \(a,m,v\) have cancelled in the principal
two rows. No \(\sqrt{-K}\), no \(K^{-1}\), and no single-component
normal gap occur. Thus (H.29) remains legitimate at the actual
turning root. Both identities are exact Laurent-polynomial
checks in the supplied producer.

Set the true model-convected passive momentum and scalar heights
\[
 {\bf p}={\bf z}_r-d{\bf z}_\phi,\qquad
 f=N\cdot{\bf z},\qquad p=N\cdot{\bf p}.
\tag{H.30}
\]
This is a definition using the actual \(d\); it does not replace
the real \(\theta_r\) in (H.3). Its discrepancy from a physical
coordinate derivative is already retained in \(\Psi\).

Then (H.29) is equivalently
\[
 n h_1=-\eta^{-1}p_\phi+\mathcal L_1,\qquad
 n h_2=-f_{\phi\phi}+\mathcal L_2,                      \tag{H.31}
\]
where the full remainders are
\[
\begin{split}
 \mathcal L_1={}&
 \eta^{-1}\{N_\phi\cdot{\bf p}
       -d_\phi N\cdot{\bf z}_\phi+C_r-dC_\phi\}
                              +n u_\phi\chi,\\
 \mathcal L_2={}&
 2N_\phi\cdot{\bf z}_\phi+N_{\phi\phi}\cdot{\bf z}
                              +C_\phi+n v_\phi\chi .
\end{split}                                                       \tag{H.32}
\]
These include the residual-supported order-zero feedback just
identified. The formula does not call all of \(\mathcal L\)
a small lower-order operator.

Taking means gives the exact rows
\[
 n\langle h_1\rangle=\langle\mathcal L_1\rangle,\qquad
 nz=\langle\mathcal L_2\rangle .                        \tag{H.33}
\]
In the actual reflection class the first left side is zero.
The even second mean is retained. The independent height and
rigid ports are not determined by applying an inverse angular
derivative to these equations.

## 6. Exact negative wave and root Airy weights

On a strict negative interval let \(q=\sqrt{-K}>0\) and use the
already proved quadratic-density state
\[
 w_\sigma=\frac{n(h_1+\sigma qh_2)}{\sqrt{2q}} .
\]
Formula (H.31) gives the exact identity
\[
 w_\sigma=
 -\frac{\eta^{-1}p_\phi+\sigma q f_{\phi\phi}}{\sqrt{2q}}
       +\frac{\mathcal L_1+\sigma q\mathcal L_2}{\sqrt{2q}} .
\tag{H.34}
\]

For each nonzero physical frequency \(k=4j\), \(M=|k|\), its
homogeneous \(|D|^{-3/2}\) principal pair is therefore
\[
 \mathcal A_{\sigma,k}
 =\frac1{\sqrt2}
  \left(\sigma\sqrt{Mq}\,f_k
       -\frac{i\,{\rm sgn}(k)}{\eta\sqrt{Mq}}p_k\right).
\tag{H.35}
\]
In particular
\[
 |\mathcal A_{+,k}|^2+|\mathcal A_{-,k}|^2
     =Mq|f_k|^2+\frac{|p_k|^2}{\eta^2Mq}.
\tag{H.36}
\]
The two signs and the physical negative cone are explicit; no
antilinear real-surface shortcut is used.

The previously introduced Bessel state
\(Y=\Lambda^{-3/2}w\) differs in (H.35) by the exact radial
multiplier \((M/\langle M\rangle)^{3/2}\), plus the complete
Bessel transform of the second term of (H.34).
For all nonzero fourfold modes the inverse multiplier is at most
\(17/16\). The zero mode is handled by the original complete
wave/mean equations, not by assigning it a value of \(M^{-3/2}\).

At the **actual root**, use (H.31) directly instead of the singular
\(q\)-wave frame. For \(M>0\),
\[
\binom{M^{-4/3}nh_{1,k}}{M^{-5/3}nh_{2,k}}
 =
 \binom{-i\,{\rm sgn}(k)\eta^{-1}M^{-1/3}p_k}
       {M^{1/3}f_k}
 +\binom{M^{-4/3}\mathcal L_{1,k}}
        {M^{-5/3}\mathcal L_{2,k}} .                   \tag{H.37}
\]

The actual current Riccati/Airy state is
\(Z_k=M^{1/6}T_M^{-1}S_{{\rm sgn}(k)}Rh_k\).
The already proved root comparison (P.25) bounds this state
and \((M^{1/3}h_{1,k},h_{2,k})\) in both directions by 5.
Thus the **correct** height scaling of that same state is
\[
                       \widetilde Z_k=nM^{-5/3}Z_k .
\tag{H.38}
\]
It is compared, with the full remainder in (H.37), to
\((M^{1/3}f_k,\eta^{-1}M^{-1/3}p_k)\).
The additional \(M^{-5/3}\) is essential. A small estimate in
the negative density norm cannot be used directly as the old
unweighted curvature \(L^2\) inverse.

All projections in (H.34)--(H.38) apply **after** the complete
products have been formed. For example \(N\cdot{\bf z}\) is
not replaced by \(N\cdot P_H{\bf z}\), and a true physical
angle pullback is not commuted with \(P_H\). Consequently
all low-to-high, high-to-low, and rigid-data paths remain.

## 7. Actual high root contact for ordinary weak-source rows

A useful concrete consequence is available without differentiating
an ordinary source. Separate (H.27) into its algebraic rows
\(B_r,B_\phi\) and the displayed derivative rows. Then
\[
 C_r-dC_\phi
 = B_r-dB_\phi+
       \partial_\phi(\Psi_3-d\Pi_3)+d_\phi\Pi_3 .
\tag{H.39}
\]
This ordered product identity is used before taking any Fourier
norm. It includes the term created by differentiating \(d\).

On the complete current root germ, the previously proved bounds
give \(|\beta|<9/5\), range\((u^2+Kv^2)<13/5\), and hence
\(\|d_\phi\|_\infty<117/25<5\).
The actual odd \(\pi/2\)-periodic \(d\) vanishes at 0 and \(\pi/4\).
The nearest of these zeros is at distance at most \(\pi/8\);
therefore, using \(\pi<22/7\),
\[
               \|d\|_\infty<1287/700<2,\qquad
               \eta^{-1}<2 .                         \tag{H.40}
\]
This includes the actual negative side and the root. The sign
of \(S\) was not assumed positive there.

Take \(P_H=P_{\{|j|\ge97\}}\), so \(M\ge388>7^3\).
The contribution of \(\Psi,\Pi\) through the derivative rows
of (H.39) and \(C_\phi\), after the diagonal factors in (H.37),
has the complete pair bound
\[
\begin{split}
 \left\|
 \binom{\eta^{-1}|D|^{-4/3}
                 [\partial_\phi(\Psi_3-d\Pi_3)+d_\phi\Pi_3]}
       {|D|^{-5/3}\partial_\phi\Pi_3}
 \right\|_{\ell^2(H)}
 &\le \frac27\|\Psi\|_2+\frac35\|\Pi\|_2 .
\end{split}                                                       \tag{H.41}
\]
Indeed the separate coefficients of \(\Pi\) are bounded by
\(4/7+10/(388\cdot7)\) and \(1/49\); the sum of their squares
is strictly below \((3/5)^2\). Multiplication by \(d\) is performed
before the high projection, using its actual \(L^\infty\) bound.

After the same 5-fold Riccati comparison, the complete contact
contribution from \(C_r,C_\phi\) is at most
\[
 \boxed{
 \frac{10}{7}\|\Psi\|_2+3\|\Pi\|_2
  +\frac5{1358}\|B_r\|_2
  +\frac{145}{19012}\|B_\phi\|_2 .}
\tag{H.42}
\]
The last two coefficients are respectively below \(1/250\)
and \(1/125\). They follow by keeping the factor \(d\) in
\(B_r-dB_\phi\) and both output rows.

The bound (H.42) is for the **complete explicitly separated
contact rows**. The other terms of (H.32), and in particular
the unknown full-height and residual feedback, remain inputs.
Equations (H.10)--(H.19) show how an ordinary body source
produces \(E_1,P_1,\delta\rho\) without its angular derivative.
The weak derivative in (H.39) is paid by the stated fractional
output powers; no extra \(g_\phi\) was inserted into (H.42).

This is not an unproved promotion of the nonlinear exterior
graph to \(H^{-5/3}\), nor a whole positive/negative inverse in
that space. Those complete operator windows and their source
composition remain to be consumed.

## 8. Exact interfaces and physical-angle trace matching

For the current radial reconstruction we continue \({\cal Q},F\)
continuously across a saved candidate interface, while keeping
the actual jumps of \(u,v,m\). Then
\[
 E^+=E^--\Delta L,\qquad
 P^+=P^--\Delta{\bf c}_\phi .                           \tag{H.43}
\]
For a continuous geometric variation,
\[
 E_1^+=E_1^--\Delta(\delta L),\qquad
 P_1^+=P_1^--\Delta(\delta{\bf c}_\phi).                \tag{H.44}
\]
All mean jumps enter the differentiated coefficients explicitly
through (H.10), (H.12) and (H.16).
If prescribed geometric jump ports are supplied, the exact
additional connection jump is
\(\nabla_\phi^{\rm ad}\Delta S_f\); the position-defect jump is
\(\nabla_\phi\Delta V-\Delta S_f\,{\bf t}\).
They must be added to (H.44).

Even when \(S_f,V\) are continuous, the passive variables have
\[
 \Delta W=-\widehat L\,\Delta\chi,\qquad
 \Delta U=-{\bf t}\,\Delta\chi .                        \tag{H.45}
\]
Thus a moving-coordinate or physical-angle interface is not
silently replaced by an identity matrix.

If the two saved base coordinate maps differ, same physical
angle matching uses the actual circle lift
\[
        G=\theta_+^{-1}\circ\theta_- .
\]
For example the passive position trace is compared as
\({\bf z}^+\circ G-{\bf z}^-\), with the corresponding true
frame and source traces. This composition is not assumed to be
small in an equal Sobolev space or to commute with a Fourier
projection. On the current root collar all the cited formulas
lie inside the single common PPoly piece 2549; the actual
high root bound (H.42) crosses no such interface.

## 9. Scope and reproducible executed check

The algebra applies to the current complete moving centre and
its actual radial frame/position reconstruction, with supplied
true end ports. It proves a residual-sensitive contact, not
that those residuals have already been made zero.
The following still require their actual quantitative consumer:

* the full radial residual and interface sums producing \(E,P,E_1,P_1\);
* the zeroth-order feedback \(J\Omega(0,ab,ac)P\);
* the remaining complete terms in (H.32), both Sobolev directions,
  and all low-mode/rigid/regular ports;
* the whole positive graph and negative return in the matching
  height-weighted windows, followed by the finite-head and original
  parameter Schur.

Source:

    scripts/fourfold_codazzi_vector_height_Airy_contact.mjs

Actual executed report:

    notes/2026-11-14-R133-vector-height-Airy-contact-rational.json

The same pure arithmetic core ran in V8 and passed all 27 gates:
exact Laurent identities for the material angle, complete angular
and radial source cancellation, every residual/mean variation
column, both height-curvature rows, and the outward rational
bounds (H.40)--(H.42).
The standalone Node source verifies the SHA256 of its published
input proofs and reproduces the report without native field data:

    node scripts/fourfold_codazzi_vector_height_Airy_contact.mjs \
      --out notes/a-new-vector-height-contact-report.json

No binary native input was read into this calculation. The actual
joint-germ bounds and the current complete two-row Riccati norm
were already proved; they are identified by SHA in the report.
The infinite-dimensional contact and source statements are proved
above, not inferred from the finite arithmetic checks.
