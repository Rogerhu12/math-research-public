# R133 supplement: the actual nonlinear regular graph in H^s and its complete outer Riccati ports

2026-11-14, phase_inverse. **Proved; 33 exact rational gates executed.**
The centre throughout is the complete final moving candidate
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\),
at the actual outer radius \(R=25/8\), with the original whole
\(|\eta|\le10^{-9}\) interval. This result extends the **nonlinear**
long-boundary derivative, not merely its Hilbert principal row, to
the Sobolev orders required by the actual Airy/Riccati normalization.

The actual physical background satisfies
\(\|Z\|_{A^0}<2.533\,10^{-13}\), where
\(Z=(C-C_{\rm ref})_{\ne0}\).
The independent outer height background is retained in the original
allowed analytic class
\[
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60},\qquad \sigma\ge1/16 .
 \tag{S.1}
\]
This is a stated restriction on the background, already allowed in
the true cap--long matching theorem; it is not inferred for arbitrary
\(\dot H^2\) backgrounds. Directions and affine sources have the
complete Sobolev norms specified below.

The main new bounds for the actual graph
\[
 J_\theta B+Q_\theta Z=d(Z,f_B),\qquad
 C_0-C_{\rm ref}=c_0(Z,f_B),\qquad B_0=0
 \tag{S.2}
\]
are
\[
\begin{array}{c|ccc}
 &L^2&H^{1/6}&H^1\\ \hline
 D_Zd&5.898255\,10^{-6}&1.11\,10^{-5}&1/4000\\
 D_{f_B}d\,|D|^{-2}
     &6.55362\,10^{-7}&1.25\,10^{-6}&2.7\,10^{-5}.
\end{array}
\tag{S.3}
\]
Every entry includes all allowed Fourier modes and the full nonlinear
long solution. The true mean rows remain
\[
 \|D_Zc_0\|<7.372818\,10^{-7},\qquad
 \|D_{f_B}c_0\,|D|^{-2}\|<8.19203\,10^{-8}.
 \tag{S.4}
\]
They are not set to zero at higher order.

In the exact moving variables, the whole homogeneous graph has
\(H^s\) lift norm below 50 for \(0\le s\le1\), and its complete
nonmean \(h_2\) parameterization is onto with inverse norm below
\(.03\). In a radial positive-reference frame with
\[
 p_M(R)=p_*:=q_*/(-m_R),\qquad
 q_*=(1+w_R^2)^{-1/2},
 \tag{S.5}
\]
the actual high outer graph has reflection norm below
\(2.22\,10^{-5}\) in the same \(L^2\) Airy-state space.
The entire head, actual mean row, independent \(f_B\), and ordinary
boundary residuals remain in its affine equation.

This is an outer-boundary theorem. It does not supply the missing
whole positive-body coefficient table, negative return inverse,
global \(\nu\) scalar denominator, or nonlinear whole BVP.

## 1. Input identities and the full physical derivative of the background

The input text identities are:

- R133-supplement-final-moving-centre-actual-regular-boundary.md,
  Git blob \(\mathtt{40463b6917c943e4ac991a597603cf41095baeb9}\).
- R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md,
  Git blob \(\mathtt{a7ff7d2ca24df41ccd242ff9799b21fdcab2aec0}\).
- R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md,
  Git blob \(\mathtt{fe1468feaf7447077d569402cc4133a9dfbeb05c}\).
- R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md,
  Git blob \(\mathtt{5fd83130fead0160cece059b7bb95f2f83b07eae}\).

Only the first two contain current-centre endpoint quantities.
The last two supply the same exact outer radial metric, complete
nonlinear long equation, and universal algebra/Green constants.
No old body field or old nonradial candidate bound is transferred.

All norms on the fourfold circle use normalized measure. The
inhomogeneous Sobolev convention is
\[
 \|f\|_{H^s}^2=\sum_{k\in4\mathbb Z}\langle k\rangle^{2s}|f_k|^2,
 \qquad \langle k\rangle=(1+k^2)^{1/2}.
\]
The independent nonmean height direction uses
\[
 \|f_B\|_{\dot H^{2,s}}
   :=\|\langle D\rangle^s|D|^2f_B\|_2 .
 \tag{S.6}
\]
Thus the second row of (S.3) means
\(\dot H^{2,s}\to H^s\), without silently exchanging homogeneous
and inhomogeneous weights.

The actual endpoint proof gives
\[
 \|Z\|_{A^0}<Z_a:=2.533\,10^{-13},\quad
 |\widehat Z_{4j}|
 \le\frac{4|j|P}{5.8}e^{-4|j|d},
 \quad
 P=1.480385\,10^{-11},\quad d>0.124999999985 .
 \tag{S.7}
\]
Both frequency signs are included. The original physical field has
infinite Fourier support; we do not treat it as the finite moving
polynomial.

Set \(x=607/1000\). The positive Taylor polynomial through order 8
at \(4(0.124999999985)\) is strictly larger than \(1/x\).
Thus \(e^{-4d}<x\), a gate checked in rational arithmetic.
Use the actual \(A^0\) norm on \(1\le|j|\le32\), and the entire
analytic tail on the remaining modes:
\[
 \|Z_\theta\|_{A^0}
 \le128Z_a+\frac{32P}{5.8}\sum_{j=33}^{\infty}j^2x^j
 <3.25\,10^{-11}.
 \tag{S.8}
\]
The complete series is evaluated by the exact identity
\[
 \sum_{j=n}^{\infty}j^2x^j
 =x^n\left(\frac{n^2}{1-x}
    +\frac{2nx}{(1-x)^2}+\frac{x(1+x)}{(1-x)^3}\right).
\]
In particular no finite-input assumption is used for an infinite
output tail. From (S.1),
\[
 \|(f_B)_\theta\|_{\dot A^2}\le16\,2^{-60}.
 \tag{S.9}
\]
The crude \(1/\sigma\) Cauchy fee is sufficient and includes every
mode of the independent background.

## 2. A larger complex background ball, with the full L2 module

We use the already proved square-zero Banach module
\(\mathfrak A\oplus\varepsilon\mathfrak M\), where the background
has the complete Fourier \(\ell^1\) norm and the direction has
the full \(\ell^2\) norm. In both, the radial supremum is taken
per Fourier mode before the final sum. The exact long Green and
two boundary lifts act on this module by their proved individual
mode kernels. This is the reason an operator-valued Cauchy estimate
is legitimate.

For positive background radii \(z,b\), put
\[
 r_f=10(z+b),\quad F=r_f+b,\quad
 \kappa=36R_CF,\quad
 J_f=\frac9{1-\kappa},\quad
 J_B=\frac{\epsilon+\kappa}{1-\kappa},
 \tag{S.10}
\]
where
\[
 R_C=2^{12},\quad R_D=2^{14},\quad R_0=2^{11},
 \qquad 0<\epsilon=2^{-512}.
\]
The same exact nonlinear long equations and complete regular
reflection fees give
\[
\begin{split}
 T(z,b)&:=\epsilon+4R_DFJ_f,\\
 C(z,b)&:=4R_0FJ_f,\\
 U(z,b)&:=\epsilon+4R_DF(1+J_B),\\
 V(z,b)&:=4R_0F(1+J_B).
\end{split}
\tag{S.11}
\]
These bound respectively \(D_Zd,D_Zc_0,
D_{f_B}d|D|^{-2},D_{f_B}c_0|D|^{-2}\) on complete \(L^2\).

For the new background Cauchy disks take
\[
 \bar z=10^{-10},\quad \bar b=10^{-11},\qquad
 \rho_Z=9\,10^{-11},\quad \rho_B=9\,10^{-12}.
 \tag{S.12}
\]
The actual background plus either corresponding complex disk is
strictly inside the wider product ball. This includes the
\(f_B\) disk: it is not taken outside a fixed \(2^{-60}\) boundary
radius without paying the enlargement.

The original full long theorem permits
\(\|(f_B,f_*)\|_{\partial}<2^{-25}\), and not only the smaller
later cap-matching choice. Here \(2\bar F<2^{-25}\) and
\(6\bar F<2^{-20}\). The true \(C\)-to-Dirichlet fixed point on
the wider product ball has
\[
 9\bar z+\epsilon\bar b+9R_C\bar F^2<\bar r_f,\qquad
 \bar\kappa<1/1000 .
 \tag{S.13}
\]
The rational report checks both inequalities. Thus the enlarged
background balls are legitimate complex domains for the same
holonomy small root and exact long BVP. Their use changes no
actual background or prescribed outer data.

The module derivative is holomorphic on these balls: differentiate
the uniformly convergent complete contraction in the square-zero
component, or solve its module Neumann equation. Cauchy therefore
gives
\[
\begin{split}
 \|D_Z(D_Zd)[a]\|_{L^2\to L^2}
       &\le\frac{\bar T}{\rho_Z}\|a\|_{A^0},\\
 \|D_{f_B}(D_Zd)[b]\|_{L^2\to L^2}
       &\le\frac{\bar T}{\rho_B}\|b\|_{\dot A^2}.
\end{split}
\tag{S.14}
\]
For \(D_{f_B}d|D|^{-2}\), the same two bounds hold with
\(\bar U\). In particular all mixed second derivative columns
are retained.

## 3. Translation covariance proves the actual H1 derivative

Write \(T=D_Zd\) and
\(U=D_{f_B}d|D|^{-2}\) at the actual background.
The exact radial long equation, true holonomy mean, Fourier
regular multiplier and curvature map commute with real angular
translation. For finite Fourier directions, differentiating this
covariance gives the exact identities
\[
\begin{split}
 [\partial_\theta,T]
   &=D_ZT[Z_\theta]+D_{f_B}T[(f_B)_\theta],\\
 [\partial_\theta,U]
   &=D_ZU[Z_\theta]+D_{f_B}U[(f_B)_\theta].
\end{split}
\tag{S.15}
\]
The full fourfold complex extension in the long theorem is used here;
translations may move the reflection axis. Its algebra and individual-mode
Green bounds were proved before imposing reflection, so the odd translation
directions are legitimate. Restrict back to the actual even/odd tangent
space after obtaining the operator bounds.
The fixed multiplier \(|D|^{-2}\) commutes with translations.
The nonlinear background is not held constant while its spatial
coefficients are differentiated.

The positive background number
\[
 \Xi=\frac{3.25\,10^{-11}}{\rho_Z}
       +\frac{16\,2^{-60}}{\rho_B}<.361113
 \tag{S.16}
\]
therefore gives complete commutator bounds
\(\|[\partial,T]\|\le\Xi\bar T\) and
\(\|[\partial,U]\|\le\Xi\bar U\).
On the actual smaller ball
\(z=10^{-12}, b=2^{-60}\), the already paid \(L^2\) bounds
are \(T_0=T(z,b)\), \(U_0=U(z,b)\).
The exact triangle inequality in
\(L^2\oplus L^2\), applied to
\((Tf,\partial Tf)=(Tf,T\partial f)+
(0,[\partial,T]f)\), yields
\[
 \|T\|_{H^1\to H^1}\le T_0+\Xi\bar T<1/4000,\qquad
 \|U\|_{H^1\to H^1}\le U_0+\Xi\bar U<2.7\,10^{-5}.
 \tag{S.17}
\]
Density identifies these operators with the unique complete
\(L^2\) derivatives already constructed. This is a proof of their
higher Sobolev action, not an assertion that an arbitrary \(A^0\)
multiplier is bounded on \(H^1\).

Complex interpolation of these same two realizations gives every
\(0\le s\le1\). For \(s=1/6\), the report verifies without root
rounding
\[
 (5.898255\,10^{-6})^5(1/4000)<(1.11\,10^{-5})^6,
\]
\[
 (6.55362\,10^{-7})^5(2.7\,10^{-5})
                                  <(1.25\,10^{-6})^6.
 \tag{S.18}
\]
This proves (S.3).

The mean outputs are scalar constants. Their original \(L^2\)
functional bounds already give (S.4) on every \(H^s\), \(s\ge0\),
without differentiating a constant into a spurious source.
Their translation identities and every dependence on the true
holonomy small root remain in (S.14)--(S.15).

Since the true \(q_k>.9999999999993\) and \(J_\theta\) is unitary
on the complete nonmean subspace,
\[
 \|(D_ZB)^{-1}\|_{H^{1/6}\to H^{1/6}}<1.0000112,
 \quad
 \|(D_ZB)^{-1}\|_{H^1\to H^1}<1.000251 .
 \tag{S.19}
\]
Neither estimate is a finite Fourier inverse.

## 4. Pay every coefficient in the actual moving variation

At the true endpoint write
\[
 v=m+w,\quad \theta=\phi+\psi,\quad j=\theta_\phi=v/m,
 \qquad \mathcal C f=f\circ\theta .
\]
The published bounds include
\[
 \|u\|_{A^0_{1/8}}<U_\sigma=1.643190\,10^{-9},\quad
 \|w\|_{A^0_{1/8}}<V_\sigma=9.603792\,10^{-9},
\]
\[
 5.84461145233<|m|<7,\qquad \|\psi\|_{A^0_{1/8}}<P .
 \tag{S.20}
\]
Use the complete multiplier norm
\(\|a\|_{\mathfrak B^1}=\sum(1+|k|)|a_k|\).
Leibniz at \(H^1\), followed by interpolation with \(L^2\),
gives \(\|M_a\|_{H^s\to H^s}\le\|a\|_{\mathfrak B^1}\)
for \(0\le s\le1\). This avoids an unpaid Bessel convolution factor.

The full analytic coefficient budgets are
\[
 U:=9U_\sigma,\quad W:=9V_\sigma,\quad V:=7+W,\qquad
 U_1:=136U_\sigma,\quad V_1:=136V_\sigma .
 \tag{S.21}
\]
For example \(136=8+2(8)^2\) pays both
\(u_\phi\) and \(u_{\phi\phi}\); no angular derivative is sampled.
The same \(\mathfrak B^1\) Neumann series proves
\(\|1/v\|_{\mathfrak B^1}<1/5.8\).

Let \(\epsilon_1=8P\) and \(c_\theta=(1-\epsilon_1)^{-1}\).
The proved complete change-of-angle estimates give
\(\|\mathcal C^{\pm1}\|_{H^s\to H^s}\le c_\theta\)
for \(0\le s\le1\). The true Hilbert conjugation obeys
\[
 \|\mathcal C J_\theta\mathcal C^{-1}-J_\phi\|_{H^s\to H^s}
       <K_H:=7.190442\,10^{-9}.
 \tag{S.22}
\]
There is no assertion that \(\mathcal C-I\) is small at the same order.

For actual physical variations set
\(f=\delta B\circ\theta,\ g=\delta C\circ\theta\).
The complete moving variation is exactly
\[
 h_1=vf-uvg-u_\phi I(vg),\qquad
 h_2=-v^2g-v_\phi I(vg).
 \tag{S.23}
\]
The primitive has its mean-zero convention and norm \(1/4\).
Reflection gives the exact mean identity
\[
 z:=\langle h_2\rangle_\phi=-m^2\delta C_0 .
 \tag{S.24}
\]
This is a derivative of the actual angle map at the approximate
centre and does not require that centre to solve the body PDE.

Using (S.3)--(S.4) and (S.21), (S.23) gives
\[
\begin{split}
 \|h_1\|_{H^s}
   &\le V\|f\|_{H^s}+V(U+U_1/4)\|g\|_{H^s},\\
 \|h_2\|_{H^s}
   &\le (V^2+V_1V/4)\|g\|_{H^s}.
\end{split}
\tag{S.25}
\]
For the homogeneous graph, the two-row Euclidean norm is below
\(50\|\delta Z\|_{H^s}\), even with the larger \(H^1\) bound.
The inverse variation is
\[
 \chi=v^{-1}I(h_2-zv/m),\quad
 k_2=h_2-v_\phi\chi,\quad g=-k_2/v^2 .
\]
All multipliers have just been paid on \(H^s\). Hence
\[
 \|\delta Z\|_{H^s}<.03\|h_2\|_{H^s}.
 \tag{S.26}
\]
This recovery bound is not inferred from an \(L^2\) change of measure.

## 5. The complete nonmean h2 chart is onto, with the true mean attached

Write \(y=P_{\ne0,\phi}h_2\). The exact map from
\(\delta Z\in H^s_{\ne0,\theta}\) to \(y\) is
\[
 \Psi=-m^2P_{\ne0,\phi}\mathcal C+\mathcal R_2 .
\]
The leading map is an isomorphism. Indeed the pullback of a physical
nonmean function has zero \(j\)-weighted mean, and the inverse of
ordinary nonmean projection in that space is
\(z\mapsto z-\langle jz\rangle_\phi\).
Its norm is at most \(1+\epsilon_1\).
Consequently
\[
 \|(-m^2P_{\ne0}\mathcal C)^{-1}\|
 \le L_*:=c_\theta(1+\epsilon_1)/(5.8)^2 .
\]
The full remainder from (S.23) satisfies
\[
 \|\mathcal R_2\|
 \le E_2:=[W(14+W)+V_1V/4]\,
                         c_\theta(1+7.372818\,10^{-7}).
 \tag{S.27}
\]
This includes the true constant \(D_Zc_0\), because only the
constant leading term vanishes after the ordinary projection.
The rational budget gives \(L_*E_2<10^{-6}\) and
\[
                 \|\Psi^{-1}\|<.03 .                   \tag{S.28}
\]
Thus (S.26) has now also been accompanied by the onto statement
needed for a graph parameterization.

The mean is an actual output
\[
 z=-m^2D_Zc_0\,\Psi^{-1}y,\qquad
 |z|<1.084\,10^{-6}\|y\|_{H^s}.
 \tag{S.29}
\]
It remains a nonzero finite-rank row, and the allowed odd mean
\(h_{1,0}=0\) remains the stated reflection constraint.

## 6. A true Robin graph in the same moving Sobolev space

Define \(p_*=q_*/(-m)>0\) as in (S.5), and put
\[
 \mathcal R h=P_{\ne0,\phi}(-J_\phi h_1-p_*h_2).
\]
On the full homogeneous graph, (S.28) gives an actual bounded operator
\[
                 \mathcal R h=\mathcal E_s y .
\]
Here the subscript records the same operator's norm realization.
This row retains all low/nonzero frequencies; no high compression
has yet occurred.

For completeness, let \(T_s\) denote the first row of (S.3), and
\(C_0=7.372818\,10^{-7}\). The leading part of
\(-J_\phi h_1-p_*h_2\) is
\[
       -m(J_\phi f+q_*g).
\]
By the true physical row and (S.22),
\[
 \|J_\phi f+q_*g\|_{H^s}
 \le [c_\theta(T_s+\epsilon+C_0)
           +K_Hc_\theta(1+T_s)]\|\delta Z\|_{H^s}.
 \tag{S.30}
\]
The regular multiplier difference \(Q-q_*I\) has the already paid
strictly positive fee below \(\epsilon\); it has not been set to zero.
The \(C_0\) contribution explicitly includes the physical mean.
Projection can improve this estimate, but we do not use that improvement.

The remaining exact coefficient error in (S.23) is at most
\[
\begin{split}
 &W c_\theta(1+T_s)\\
 &+\left[V(U+U_1/4)+\frac1{5.8}
          \{W(14+W)+V_1V/4\}\right]c_\theta(1+C_0)
\end{split}
\tag{S.31}
\]
times \(\|\delta Z\|_{H^s}\).
Multiply (S.30) by 7, add (S.31), then use (S.28).
The new exact gates give
\[
 \boxed{\ \|\mathcal E_{1/6}\|<2.6\,10^{-6},\qquad
                \|\mathcal E_1\|<5.3\,10^{-5}.\ }
 \tag{S.32}
\]
Every term has a fixed order in the exact formula; no same-order
smallness of the raw angle composition is used.

## 7. The actual outer Riccati ports, all head paths retained

Use the radial principal reference of the positive-root theorem,
but choose its outer backward Riccati boundary value to be
\(p_M(R)=p_*\), independent of frequency. A positive variational
definition on any positive radial body interval uses the actual
outer Robin form coefficient \(Mp_*\); its scaling degree is 1,
so the prior logarithmic-frequency estimate
\(|M\partial_M\log p_M|\le1\) still holds.
This is a specified new reference choice, not an assertion that
the previous short-collar reference already has this outer value.

At the endpoint only, let \(g_M(R)>0\) be any chosen positive
forward radial Riccati value, and set
\[
 W_M=p_*+g_M,\qquad
 T_M=W_M^{-1/2}
       \begin{pmatrix}p_*&-g_M\\1&1\end{pmatrix}.
\]
For \(M=|4j|>0,\ \sigma=\operatorname{sgn}j\), put
\[
 x_j=(-i\sigma h_{1,j},h_{2,j})^t,\qquad
 Z_j=M^{1/6}T_M^{-1}x_j.
\]
Then exactly
\[
 Z_{u,j}=-M^{1/6}W_M^{-1/2}\mathcal R h_j,\qquad
 h_{2,j}=M^{-1/6}W_M^{-1/2}(Z_{s,j}+Z_{u,j}).
 \tag{S.33}
\]
The zero mode is not inserted in these powers; it remains (S.24),
(S.29) and the finite head.

From \(w_R<1/800000\), \(q_*>1-1/[2(800000)^2]\), and \(|m|<7\),
\[
                        W_M\ge p_*>1/8 .
\]
Thus no numerical upper bound for \(g_M\), or unseen body coefficient
table, is needed for the following boundary statement.

Let \(P_H={\bf1}_{|j|\ge97}\), \(P_L={\bf1}_{1\le|j|\le96}\).
Denote
\(D_o=M^{1/6}W_M^{-1/2}\) and
\(D_i=M^{-1/6}W_M^{-1/2}\) on the nonzero modes.
The exact high boundary equation is
\[
 (I+A_H)Z_{u,H}=-A_H Z_{s,H}
        -P_HD_o\mathcal E_{1/6}P_Ly+\text{affine sources},
 \quad A_H=P_HD_o\mathcal E_{1/6}P_HD_i .
 \tag{S.34}
\]
The low states in this equation are true independent head variables;
they are not discarded by high compression.

The homogeneous/Bessel comparison on \(M\ge4\) costs at most
\(17/16\). Using (S.32),
\[
 \|A_H\|<8(17/16)(2.6\,10^{-6})=.0000221=:a .
\]
The equality defines an outward rational budget; the actual
operator inequality is strict because (S.32) is strict.
Neumann inversion of \(I+A_H\) gives
\[
 \boxed{\ \|Z_{u,H}\|
     <.0000222\,\|Z_{s,H}\|
            +.0000235\,\|P_Ly\|
            +\text{affine-source terms}.\ }
 \tag{S.35}
\]
For the head column use
\(\|P_Ly\|_{H^{1/6}}\le\langle384\rangle^{1/6}\|P_Ly\|<3\|P_Ly\|\)
and \(W_M^{-1/2}<3\), then divide by \(1-a\).
This includes **all** head-to-high entries of the real nonlinear
graph, even though that boundary graph is not finitely banded.
There is no claim that only the body's band-64 shell contributes
at this nonlinear exterior boundary.

## 8. Independent fB and ordinary residuals, including the mean row

For an affine boundary problem retain the exact complete rows
\[
\begin{split}
 J_\theta\delta B+Q_\theta\delta Z
   &=D_Zd\,\delta Z+D_{f_B}d\,\delta f_B+r_B,\\
 \delta C_0&=D_Zc_0\,\delta Z
                    +D_{f_B}c_0\,\delta f_B+r_C .
\end{split}
\tag{S.36}
\]
Here \(r_B\) is the physical nonmean Robin residual, \(r_C\) the
independent scalar mean residual. For the \(H^{1/6}\) contract,
set \(F_B=\|\delta f_B\|_{\dot H^{2,1/6}}\).
The direct physical columns have
\[
 \|f_{\rm aff}\|_{H^{1/6}}
    \le c_\theta(1.25\,10^{-6}F_B+\|r_B\|_{H^{1/6}}),
\quad
 |g_{\rm aff}|\le8.19203\,10^{-8}F_B+|r_C|.
\]
The second is constant before and after the angle composition.

Let \(B_2=V^2+V_1V/4\), and
\[
 B_{\rm aff}=Vc_\theta,\quad
 C_{\rm aff}=V(U+U_1/4)+B_2/5.8+(2.6\,10^{-6})B_2 .
\]
The last term pays the exact shift of the \(h_2\) chart:
\(\delta Z=\Psi^{-1}(y-P_{\ne0}h_{2,\rm aff})\).
Consequently the affine remainder in \(\mathcal R h=\mathcal E y+\rho\)
has norm at most
\[
 \|\rho\|_{H^{1/6}}
 \le B_{\rm aff}(\,1.25\,10^{-6}F_B+\|r_B\|_{H^{1/6}})
      +C_{\rm aff}(8.19203\,10^{-8}F_B+|r_C|).
\]
After the actual \(D_o\) conversion and \((I+A_H)^{-1}\), the
complete version of (S.35) is
\[
\begin{split}
 \|Z_{u,H}\|<&\ .0000222\|Z_{s,H}\|
          +.0000235\|P_Ly\|\\
 &+.000030 F_B+22\|r_B\|_{H^{1/6}}+26|r_C|.
\end{split}
\tag{S.37}
\]
These are executed rational budgets, not suppressed source columns.

The true moving mean equation in the same affine chart is
\[
 z=-m^2\{D_Zc_0\,\Psi^{-1}(y-P_{\ne0}h_{2,\rm aff})
                  +D_{f_B}c_0\,\delta f_B+r_C\}.
\]
Thus
\[
 |z|<1.084\,10^{-6}\|y\|_{H^{1/6}}
             +4.1\,10^{-6}F_B+50|r_C|.
 \tag{S.38}
\]
The mean boundary datum has not been used as a nonzero-mode
normalization. The independent overall mean height translation
remains a separate free geometric parameter; the curvature equations
do not determine it.

The full low nonzero Robin rows are still (S.36) after the exact
moving map. Equations (S.34)--(S.38) grant no inverse for those
finite rows or for their feedback through the body. The actual
\(\nu\) column still belongs to the global augmented problem.

## 9. Executed source, scope and continuation

The source is
scripts/fourfold_codazzi_final_regular_Hs_Riccati.mjs.
The complete new text report is
notes/2026-11-14-R133-final-regular-Hs-Riccati-rational.json.
The same normalized BigInt core was actually run in the available
JavaScript environment; all 33 gates passed. It can be reproduced by
\[
 \texttt{node scripts/fourfold_codazzi_final_regular_Hs_Riccati.mjs
 --out notes/2026-11-14-R133-final-regular-Hs-Riccati-rational.json}.
\]
It does not read binary native data or claim to recover a lost
candidate array. It consumes only the explicit rigorous text bounds
and exact same-object identities listed in Section 1.

The result supplies the actual outer graph in the same
\(H^{1/6}\) space used by an Airy-normalized full positive reference,
including nonlinear derivatives, all frequency tails, the true mean,
ordinary residuals and independent outer-height input.
It deliberately does not upgrade arbitrary rough nonlinear
backgrounds: the analytic background condition (S.1) is part of the
theorem. The full positive-body coefficients and complete global
return/parameter inverse remain the next operator obligations.
