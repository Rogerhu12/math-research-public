# R133 supplement: the complete normalized angle gauge, residual Hessian, and radial rotation row

2026-11-15, visible-exact-astra-0df9.

**Proved analytic identities and a fixed-centre all-mode Hessian bound.** The normalized moving-to-physical map has a weighted, rather than unweighted, angle-variation mean outside the reflection class. This note derives its complete first and second differentials, the radial rotation term of the original moving field, and the residual source required when recovering that field at a non-solution centre.

The exact repaired centre, all its original residuals, and the physical target are unchanged. The reference candidate index is ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413; the continuous repair definition is 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47. Quantitative residual statements below are only at the actual fixed parameter $\eta_0,\delta=0$. The identities themselves apply to every smooth periodic state with $m=\langle v\rangle_\phi\ne0$ and $v/m>0$. The actual target has $C_{\rm ref}<0$; neither $v$ nor $C$ is replaced by its absolute value in any algebraic identity.

The paid background coefficients and original reflection formula are in [the continuous repaired cap](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md); the complete physical Green and its independent two mean ports are in [the all-mode cap theorem](R133-supplement-actual-final-all-mode-physical-cap-Green.md). This note does not silently extend an odd/even angle convention to arbitrary $4\mathbb Z$ variations.

## 1. Normalize the actual lift before differentiating

All circular means below use normalized measure on the circle of period $\pi/2$. Write $I_\phi=\partial_\phi^{-1}P_{\ne0}$, and similarly $I_\theta$, with physical frequencies $4\mathbb Z$. Define
$$
 \Theta_Q(\phi)=\phi+\frac1mI_\phi(v-m),\qquad
 \Phi_Q=\Theta_Q^{-1},\qquad
 W=\Psi(Q)=(B,C)=(u/v,1/v)\circ\Phi_Q .
 \tag{G.1}
$$
The additive normalization is $\langle\Theta_Q-\mathrm{id}\rangle_\phi=0$. It is fixed once in the definition; no reflection hypothesis occurs in (G.1).

The exact inverse satisfies
$$
 \Phi_{Q,\theta}=mC,\qquad C_0=1/m,\qquad
 \Phi_Q(\theta)=\theta+mI_\theta(C-C_0).
 \tag{G.2}
$$
Indeed the first equality follows from $\Theta_{Q,\phi}=v/m$. To determine the constant, put $\psi=\Theta_Q-\mathrm{id}$. The change of variables $\theta=\phi+\psi(\phi)$ gives
$$
 \langle\Phi_Q-\mathrm{id}\rangle_\theta
 =-\langle\psi(1+\psi_\phi)\rangle_\phi=0,
$$
because $\langle\psi\rangle_\phi=0$ and the integral of $\psi\psi_\phi$ vanishes. Thus (G.2) is also valid when both physical curvature means are nonzero.

## 2. The complete first differential and its mean

For a moving direction $h=(h_1,h_2)$ held fixed as a function of $\phi$, use the same symbols for its pullback to the physical angle. Define
$$
 z_h=\langle h_2\rangle_\phi,\qquad
 \mu_h=z_h/m=\langle Ch_2\rangle_\theta,\qquad
 E_h=(D\Theta_Q[h])\circ\Phi_Q .
$$
Differentiating (G.1), including its normalization, gives
$$
 (E_h)_\theta=Ch_2-\mu_h,\qquad
                   \langle CE_h\rangle_\theta=0 .
 \tag{G.3}
$$
The second equality is the actual moving-angle mean condition after multiplying the Jacobian $mC$; it is not $\langle E_h\rangle_\theta=0$. Consequently
$$
 \boxed{\quad
 E_h=I_\theta(Ch_2)-m\langle C I_\theta(Ch_2)\rangle_\theta,\qquad
 x=D\Psi(Q)h=Ph-W_\theta E_h,
 \quad}
 \tag{G.4}
$$
where
$$
 P=\begin{pmatrix}C&-BC\\0&-C^2\end{pmatrix}.
$$
The second term in $E_h$ is a genuine rank-one angular operator. Its omission would choose another angle normalization for general variations.

Conversely, for $x=(b,c)$, put
$$
 p_c=I_\theta\{c-mC\langle c\rangle_\theta\},\qquad
 S'=\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix}.
$$
Differentiate (G.2), using $\delta m=-m^2\langle c\rangle_\theta$. The result is
$$
 \boxed{\quad
 E_h=-v p_c,\qquad
 h=S'\{x-vW_\theta p_c\},\qquad
 \langle x_C\rangle_\theta=-z_h/m^2 .
 \quad}
 \tag{G.5}
$$
In particular the displayed inverse differential in the old reflection theorem remains the correct inverse on the full two-mean space. It is the forward angle primitive that needs its weighted constant in (G.4). No component of $h_2$, $c$, or the independent $B$ mean has been projected away.

## 3. An exact second differential with the same gauge

Let $R$ be any moving direction held fixed in the same $\phi$ coordinate, and set
$$
 t=PR,\qquad e=E_R,\qquad
 g_R=CR_2,\qquad \mu_R=\langle CR_2\rangle_\theta .
$$
At fixed physical angle, variation in direction $R$ has
$$
 \delta_R h=-e h_\theta,\qquad
 \delta_R C=t_C-C_\theta e=-(Ce)_\theta-\mu_R C .
$$
Writing $g_h=Ch_2$, one therefore obtains
$$
 \delta_R g_h=-(eg_h)_\theta-\mu_Rg_h,\qquad
                 \delta_R\mu_h=-\mu_R\mu_h .
 \tag{G.6}
$$
Differentiating (G.3) yields
$\delta_RE_h=-e g_h-\mu_RE_h+\kappa$, with $\kappa$ constant in $\theta$.
Its value is fixed by the differentiated weighted mean:
$$
 \begin{aligned}
 0&=\delta_R\langle CE_h\rangle_\theta\\
  &=\langle-(Ce)_\theta E_h-Ce g_h
               -2\mu_RCE_h+C\kappa\rangle_\theta\\
  &=-\mu_h\langle Ce\rangle_\theta+\kappa C_0=\kappa/m .
 \end{aligned}
$$
Thus
$$
                         \delta_RE_h=-eCh_2-\mu_RE_h .
 \tag{G.7}
$$
Using $Ph=x+W_\theta E_h$ in the derivative of (G.4) cancels both second angular derivatives of $W$ and all differentiated unknowns except a common transport. The exact result is
$$
 \boxed{\quad
 D^2\Psi(Q)[R,h]
 =-e x_\theta+DP[t]h-t_\theta E_h+
       W_\theta\{(CR_2)E_h+e\mu_h\},
 \quad}
 \tag{G.8}
$$
with
$$
 DP[t]=
 \begin{pmatrix}t_C&-Ct_B-Bt_C\\0&-2Ct_C\end{pmatrix}.
$$
There is no additional unweighted primitive-normalization mean in (G.8): its effect is already in the weighted constant of (G.4). For the original even/odd state and even/odd direction, that constant and the old final mean pairing both vanish by parity, so (G.8) agrees with the previously used reflection formula.

As an independent check, (G.2) implies the exact, generally nonzero mean
$$
       \left\langle(D^2\Psi[R,h])_C\right\rangle_\theta
                    =2z_Rz_h/m^3 .
 \tag{G.9}
$$
No radial derivative of $R$ occurs in (G.8).

## 4. The radial rotation of the original moving equation

Use the same scalar radial coefficients $\beta,\gamma,K$ as the original cap. Set
$$
 S=u^2+Kv^2,\quad d=-\beta I_\phi S,\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},
$$
$$
 F(Q)=dQ_\phi+\gamma mJ(K)Q_\phi+
                 \beta(-u,v)-\beta SQ .
 \tag{G.10}
$$
The signs in (G.10) are those of the unchanged [actual moving residual producer](../scripts/fourfold_codazzi_moving_continuous_residual.py): its angular terms are $+\gamma mK\,v_\phi$ and $-\gamma m\,u_\phi$. They also give the positive two-mode couplings of the original physical cap reference. All coefficient constants below, such as $C_*,U,V$, denote norms; the signed functions in (G.1)--(G.22) keep their actual signs.

Define the scalar, radial rotation rate
$$
                    A(Q)=\left\langle\frac{dv}{m}-\gamma u\right\rangle_\phi .
 \tag{G.11}
$$
For $Q_r=F(Q)$, integration by parts gives
$$
 m_r=\beta m(1-\langle S\rangle_\phi),\qquad
 (\Theta_{Q,r})_\phi
       =\partial_\phi\left(\frac{dv}{m}-\gamma u\right).
$$
The normalization in (G.1) then determines
$$
        \Theta_{Q,r}=\frac{dv}{m}-\gamma u-A(Q).
 \tag{G.12}
$$
The final constant vanishes on the original reflection background, but its differential need not vanish on an arbitrary $4\mathbb Z$ direction.

For clarity, write the physical Gauss curvature component
$\mathcal A=(B^2+K)/C$. The actual physical Codazzi field in these conventions is
$$
 F_{\rm phys}(B,C)
      =\bigl(\gamma\mathcal A_\theta-2\beta B,\
                       \gamma B_\theta+\beta(\mathcal A-C)\bigr).
 \tag{G.13}
$$
Substitution of (G.10)--(G.12) in $PF-W_\theta E_F$ cancels the full $d$ transport and gives
$$
                 D\Psi(Q)F(Q)=F_{\rm phys}(\Psi(Q))+A(Q)W_\theta .
 \tag{G.14}
$$
This is a direct identity of the vector fields, without assuming that the centre solves either equation.

The rotation rule for a fixed scalar $s$ is
$$
 Q_s(\phi)=Q(\phi+s),\quad
 \Theta_{Q_s}(\phi)=\Theta_Q(\phi+s)-s,\quad
 \Psi(Q_s)(\theta)=W(\theta+s).
 \tag{G.15}
$$
Thus $D\Psi[Q_\phi]=W_\theta$. Define the field in the complete normalized physical gauge by
$$
          F_{\rm cov}(Q)=F(Q)-A(Q)Q_\phi .
$$
It satisfies the exact covariance
$$
                     D\Psi(Q)F_{\rm cov}(Q)=F_{\rm phys}(\Psi(Q)).
 \tag{G.16}
$$
This is an explicit angle-coordinate correction. It changes neither the rotational target nor the physical surface.

## 5. Recover the original field and retain the full phase port

The scalar $A$ is invariant under angular translations and $F$ is translation equivariant. If
$$
 Q_{{\rm cov},r}=F_{\rm cov}(Q_{\rm cov}),\qquad
 a'(r)=A(Q_{\rm cov}(r)),\qquad a(L)=a_L ,
$$
then
$$
                  Q_{\rm orig}(r,\phi)=Q_{\rm cov}(r,\phi+a(r))
 \tag{G.17}
$$
satisfies $Q_{{\rm orig},r}=F(Q_{\rm orig})$. The physical angle associated with the original field is
$$
 \theta_{\rm phys}=\Theta_{Q_{\rm orig}}(\phi)+a(r)
                 =\Theta_{Q_{\rm cov}}(\phi+a(r)).
 \tag{G.18}
$$
In this same physical angle, its physical $(B,C)$ field is exactly that of $Q_{\rm cov}$. The phase $a_L$ fixes one angular origin. Its propagated difference $a(R)-a(L)$ is true endpoint data; it is not reset on each piece. All parameter derivatives and any holonomy or material matching condition read the same propagated phase.

For an inhomogeneous equation with $f_{\rm cov}$, the right side of the original equation is the translated source $f_{\rm cov}(r,\phi+a(r))$. This matters at a non-solution centre.

At the actual reflection centre $Q_0$, one has $A(Q_0)=0$ and
$$
 R_0=Q_{0,r}-F(Q_0)=Q_{0,r}-F_{\rm cov}(Q_0).
$$
Let
$$
 L_{\rm orig}=\partial_r-DF(Q_0),\qquad
 L_{\rm cov}=\partial_r-DF_{\rm cov}(Q_0).
$$
Then
$$
 L_{\rm cov}h=L_{\rm orig}h+Q_{0,\phi}DA(Q_0)[h].
 \tag{G.19}
$$
If $a'=DA(Q_0)[h]$ and $h_{\rm orig}=h+aQ_{0,\phi}$, exact translation equivariance gives
$$
 \boxed{\quad
 L_{\rm orig}h_{\rm orig}=L_{\rm cov}h+a\,R_{0,\phi}.
 \quad}
 \tag{G.20}
$$
Indeed $L_{\rm orig}Q_{0,\phi}=R_{0,\phi}$ and
$DA(Q_0)[Q_{0,\phi}]=0$. The second term in (G.20) cannot be discarded because the numerical centre has nonzero residual. Therefore a statement about the original moving forced problem must retain the coupled scalar phase equation, this residual ordinary source, the complete endpoint phase, and their parameter derivatives.

An explicit, derivative-free scalar row for that phase is
$$
 \begin{aligned}
 DA[h]={}&\left\langle\frac{\delta d\,v+d h_2}{m}
                   -\frac{dv}{m^2}z_h-\gamma h_1\right\rangle_\phi,\\
 \delta d={}&-\beta I_\phi(2u h_1+2Kv h_2).
 \end{aligned}
 \tag{G.21}
$$
This row uses the entire mean. It is not the physical curvature $B_0$ equation.

## 6. The complete residual covariance in the normalized gauge

For any centre set $R_{\rm cov}=Q_r-F_{\rm cov}(Q)$.
Differentiating (G.16), and then subtracting the radial chain rule, gives
$$
 \boxed{\quad
 L_{\rm phys}(D\Psi h)
   =D\Psi(L_{\rm cov}h)+D^2\Psi[R_{\rm cov},h].
 \quad}
 \tag{G.22}
$$
The second differential is the actual full-gauge expression (G.8). For the repaired reflection centre, $R_{\rm cov}=R_0$ is exactly the already accepted residual, including its repair fees. No target or residual value is recomputed.

The centre and all its angular derivatives are continuous across the original interfaces. Hence (G.1), (G.4), and (G.5) also agree there. Affine jumps are transformed by the complete $D\Psi$, and their means are retained. Ordinary one-sided residual jumps create no radial delta term in (G.8). A recovered phase from (G.17) is one continuous scalar with its actual derivative; it does not introduce an arbitrary composition jump at every interface.

## 7. All-mode fixed-centre bounds from the existing local Hessian certificate

This section uses the already certified physical Green $G$ with its stated complete inner, outer Robin, and independent outer mean ports. The actual long-tail $B_0$ feedback is a further explicit boundary column, as in [the complete fourfold cap--long graph](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md); it is not silently set to zero by choosing the reflection centre.

Let
$$
 w=(v-m)/m,\qquad
 J_*=(1-\|w\|_{\mathscr A_{1/32}})^{-1}.
$$
The paid bound $\|w\|_{\mathscr A_{1/32}}<.015211829<1/64$ and the already paid inverse-angle composition imply
$$
 \|mC-1\|_{\mathscr A_0}\le J_*-1,\qquad
                         1\le J_*<64/63<33/32 .
 \tag{G.23}
$$
Here the norm is the joint coefficientwise-radial-supremum norm of the cap theorem. Because $I_\theta(Ch_2)$ has unweighted mean zero, the rank-one term in (G.4) can be written as
$\langle(mC-1)I_\theta(Ch_2)\rangle_\theta$. Therefore
$$
                   \|E_h\|_2\le\frac{J_* C_*}{4}\|h_2\|_2 .
 \tag{G.24}
$$
The inverse (G.5), and consequently the bounds $H_C,H_2$ of the [local triangular Hessian certificate](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md), are valid for arbitrary full $x=(b,c)$. Their proof did not require parity.

The actual $R_{0,2}$ and $C$ are even. Thus $e=E_{R_0}=I_\theta(CR_{0,2})$ exactly, and the old complete $E_A,E_\infty,E_1$ budgets are unchanged. Write (G.8) as
$$
                  H_Rx=-e x_\theta+Z_{\rm full}x .
$$
For the last bracket use
$$
 \|(CR_{0,2})E_h+e\mu_h\|_2
 \le\left(\frac{J_*C_*^2r_{V,0}}4+C_*E_\infty\right)\|h_2\|_2
 \le J_* b_*\|h_2\|_2 ,
$$
where $b_*=C_*^2r_{V,0}/4+2C_*E_\infty$ is the original complete coefficient. The $DP[t]h$ terms are unchanged and $t_\theta E_h$ costs at most $J_*$ times its old bound. Hence, on every original true cell,
$$
 \begin{pmatrix}\|(Z_{\rm full}x)_B\|_2\\
                 \|(Z_{\rm full}x)_C\|_2\end{pmatrix}
 \le J_*
 \begin{pmatrix}Z_{BB}&Z_{BC}\\0&Z_{CC}\end{pmatrix}
 \begin{pmatrix}\|x_B\|_2\\\|x_C\|_2\end{pmatrix}.
 \tag{G.25}
$$
This retains the triangular dependence and both means. It only multiplies already accepted positive inequalities; no new directed numerical experiment is used.

Finally split the transport in the exact order
$$
             -e x_\theta=\partial_\theta(-e x)+e_\theta x .
$$
The original complete divergence-source module applies to $-e x$, and the original ordinary gains apply to $e_\theta x+Z_{\rm full}x$. Consequently the old complete unknown-input estimate gives
$$
 \boxed{\quad
       \|G H_R\|_{\mathfrak M\to\mathfrak M}
               \le J_*\chi_H<\frac1{128},
       \qquad \chi_H<.003840162<\frac1{256}.
 \quad}
 \tag{G.26}
$$
The last comparison follows directly from $J_*<2$; no new decimal value is asserted. Thus the full-gauge residual operator at this fixed centre has a Neumann inverse in the physical Hilbert module, with all the original complete ports. In particular arbitrary nonreflection unknowns have been paid here, rather than inferred from a reflection-only inverse.

## 8. Scope for subsequent Sobolev and parameter work

Equations (G.1)--(G.26) pay the normalized all-$4\mathbb Z$ differential, its exact residual Hessian, and its $L^2$-based module contraction at the fixed repaired centre. To use this result in negative or high Sobolev orders, one must still control the conjugated complete Green, the rank-one mean operators, and every boundary column in those norms. An $L^2$ contraction by itself is not that statement.

For the original, uncorrected moving forced equation the extra phase row and $aR_{0,\phi}$ in (G.20) remain part of the inverse problem. A result stated in the normalized physical gauge instead uses (G.16) as its exact nonlinear equation and retains the propagated phase when returning to the original representation. Neither choice permits deleting a true endpoint, totalflux, curvature mean, or holonomy condition.

A nonzero $\delta$ neighbourhood, the entire coupled tail/body inverse, the true $\nu$ response, a nonlinear state ball, and all final geometric matching are not obtained here. The next analysis consumes the corrected full-gauge Hessian and the already proved complex angular shift family to pay the required Sobolev conjugations.
