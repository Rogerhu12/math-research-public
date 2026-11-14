# R133 supplement: the actual fixed radial circle and complete Airy ports

2026-11-13, visible-exact / phase_inverse. **Status: proved and computed.**

This is the same complete M256 amplitude-$3/4$ reciprocal candidate,
SHA `45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`,
with its exact fixed $\nu$ and the whole original real affine parameter
interval. No different candidate or numerical turning constant is used.

Let $\delta=2^{-36}$ and retain the actual physical fold constructed in
[the fold theorem](R133-supplement-actual-physical-fold-and-full-Airy-collar.md).
The physical circle

$$r=r_*(\eta)-2^{-37}                                                   \tag{P.1}$$

is a genuine, nonconstant negative graph $T=t_g(X)$ in that chart. Both
directions between this graph and $T=-\delta$ are now constructed with
all Fourier modes, both independent means, and the complete ordinary
physical source. The concrete contracts are

$$
\begin{aligned}
 \|h\|_{L^2_\theta\text{ at }(P.1)}
 &<4.631103\|U(-\delta)\|_{H_X^1}
       +0.000171351\|f\|_{H^1(\Omega_g)},\\
 \|U(-\delta)\|_{\mathcal E(-\delta)}
 &<14.893622\|h\|_{H^1_\theta\text{ at }(P.1)}
       +0.000939849\|f\|_{H^1(\Omega_g)}.
\end{aligned}                                                        \tag{P.2}
$$

Here $\Omega_g$ is the exact physical inverse image of the domain between
the graph and $T=-\delta$. The source norm includes both $f_r$ and
$f_\theta$. The two input norms in (P.2) are deliberately stated: these
are complete contracts with an explicitly paid angular derivative,
not a same-space feedback inverse. The second line is in precisely the
full padded Airy norm of the preceding balanced collar theorem.

No inverse quarter-power of $\delta$ occurs in (P.2). The proof first
controls two differentiated symmetrized energies, then uses the actual
second row as a scalar transport equation. Converting the whole
degenerate energy into an ordinary two-state norm would lose this fact.

## 1. The unchanged equation and domains

The physical variation is $h=(\delta u,\delta v)$. With
$R=\operatorname{diag}(-1,1)$, the already proved exact transformations are

$$
 Rh=FU,\quad F=\operatorname{diag}(b^{-1/2},b^{1/2}),\quad b^2=T/K,
 \qquad U_T=J(T)U_X+\mathcal VU+g,
 \qquad g=M_f f=F^{-1}A_T^{-1}Rf,                         \tag{P.3}
$$

where

$$
 J(T)=\begin{pmatrix}0&T\\-1&0\end{pmatrix},\qquad
 \mathcal V=\begin{pmatrix}d_1&T e_{12}\\e_{21}&d_2\end{pmatrix}.       \tag{P.4}
$$

The actual inverse exists on $|T|\le T_b=2^{-34}$,
$|\operatorname{Im}X|\le1/4096$. The physical radial coordinate of
every point in this product obeys

$$|r-r_*|\le r_i<4.483414\cdot10^{-11}.                              \tag{P.5}$$

We consume (P.5), rather than bounding the entire larger preliminary
Picard box again. All objects used below are inside one true scalar germ
and one exact candidate PPoly piece. There is no unaccounted candidate
join inside this theorem.

The equation in (P.3) is the full physical linearization at the saved
approximate centre. Its derivation does not assume that the centre
satisfies the nonlinear PDE. In particular, this result does not erase
the residual-sensitive bridge required when it is coupled to a moving
coordinate linearization elsewhere.

## 2. Actual real geometry before taking derivative bounds

Write $u=r-r_*$ only in this section, and retain the actual analytic
functions from the fold construction:

$$T=uC,\quad C=(3G/2)^{2/3},\qquad X=\theta+uH.                     \tag{P.6}$$

They are defined on radial radius $R_1=512^{-2}$ and physical angle
strip $3\sigma/4$, $\sigma=1/1024$. The complete previous bounds are
$|G|\le M_G$, $|H|\le M_H$, and the exact root value is
$G(0,\theta)=2p(0,\theta)/3$, $p=a\sqrt{k}$.
Put $t_i=r_i/R_1$ and $Q=4/\sigma$. The radial power series and its
complete geometric tail give

$$
\begin{gathered}
 \varepsilon_G=M_Gt_i/(1-t_i),\quad
 G_-=(2/3)\inf\operatorname{Re}p-\varepsilon_G,\\
 G_r^*=M_G/[R_1(1-t_i)^2],\qquad
 G_{rr}^*=2M_G/[R_1^2(1-t_i)^3],\\
 G_\theta^*=(2/3)p_\theta^*+Q\varepsilon_G,\qquad
 G_{\theta\theta}^*=(2/3)p_{\theta\theta}^*+2Q^2\varepsilon_G,\qquad
 G_{r\theta}^*=QG_r^* .                                  \tag{P.7}
\end{gathered}
$$

The $p$ derivatives use the whole saved finite angular series and its
already certified coefficient envelopes:
$p_{\theta\theta}^*\le|\gamma|\sqrt{k^*}\,\|v_{\theta\theta}\|_{A_\sigma}$.
The intrinsic $k$ is radial. Thus no angular coefficient, mean term, or
nonconstant part is replaced by its average. Cauchy is used only for the
remaining radial tail in (P.7).

On the real domain $G>0$, so the lower bound is
$C_-=(3G_-/2)^{2/3}$, without the complex-sector factor used in the
preliminary holomorphic proof. Set $d_G=(3G_-/2)^{1/3}$. Differentiation
of the actual power gives

$$
\begin{aligned}
 C_r^*&=G_r^*/d_G,& C_\theta^*&=G_\theta^*/d_G,\\
 C_{rr}^*&=G_{rr}^*/d_G+(G_r^*)^2/(2d_G^4),\\
 C_{r\theta}^*&=G_{r\theta}^*/d_G+G_r^*G_\theta^*/(2d_G^4),\\
 C_{\theta\theta}^*&=G_{\theta\theta}^*/d_G+(G_\theta^*)^2/(2d_G^4).
\end{aligned}                                                       \tag{P.8}
$$

Also $H_\theta^*=QM_H$, $H_{\theta\theta}^*=2Q^2M_H$ and
$X_r^*=M_H/(1-t_i)^2$. Consequently

$$
\begin{gathered}
 |X_\theta-1|\le r_iH_\theta^*,\quad
 T_{r,-}=C_--r_iC_r^*>0,\quad T_r^*\le C^*+r_iC_r^*,\quad
 |T_\theta|\le r_iC_\theta^*,\\
 T_{rr}^*=2C_r^*+r_iC_{rr}^*,\quad
 T_{r\theta}^*=C_\theta^*+r_iC_{r\theta}^*,\quad
 T_{\theta\theta}^*=r_iC_{\theta\theta}^* .                 \tag{P.9}
\end{gathered}
$$

In particular the exact fixed-$T$ angular Jacobian is

$$
 \left.\frac{dX}{d\theta}\right|_T
   =X_\theta-X_rT_\theta/T_r,
 \qquad
 \left|\left.\frac{dX}{d\theta}\right|_T-1\right|
       <1.734353\cdot10^{-7}.                              \tag{P.10}
$$

This correlated expression is much tighter than separately dividing
the largest and smallest full two-dimensional Jacobian bounds.
With $J_f=T_rX_\theta-X_rT_\theta$, the actual inverse derivatives are
$r_X=-T_\theta/J_f$, $\theta_X=T_r/J_f$,
$r_T=X_\theta/J_f$, $\theta_T=-X_r/J_f$. Their complete real bounds are

$$
 |r_X|<3.087879\cdot10^{-10},\quad |\theta_X|<1.000000174,
 \quad |r_T|<0.380812,\quad |\theta_T|<0.359054.             \tag{P.11}
$$

The real frame and source matrix are bounded by

$$
 \|F^{\pm1}\|<2.190538,
 \quad\|A_T^{-1}\|<0.380812,
 \quad\|M_f\|<0.834181,
 \quad\|(M_f)_X\|<7.297098,
 \quad\|(M_f)_T\|<544624.007.                              \tag{P.12}
$$

For completeness, these derivative costs are obtained without assuming
an unproved real analytic extension. The exact matrix is
$A_T=A I-aT_\theta J(K)$, $A=T_r-dT_\theta$.
First use $A_->a^*T_\theta^*\|J(K)\|$ to bound its inverse. Then
differentiate this complete matrix in $(r,\theta)$ using (P.9), the
already proved $d_\theta,a_\theta$, and
$|d_r|\le d^*/(R-r_i)$, $|a_r|\le a^*/(R-r_i)$ from the original
complex radial radius $R=10^{-5}$. The inverse derivative is
$-(A_T)^{-1}(A_T)_j(A_T)^{-1}$. Frame derivatives use

$$
 |(\log b)_r|\le\tfrac12(C_r^*/C_-+k^*/[(R-r_i)k_-]),\qquad
 |(\log b)_\theta|\le C_\theta^*/(2C_-),                  \tag{P.13}
$$

followed by (P.11). These formulas, including both mixed derivative
terms, are evaluated in the native consumer.

As a further reusable real source contract, on every actual real
subdomain of this canonical rectangle,

$$
 \|g\|_{L^2_{T,X}}<2.197432\|f\|_{L^2_{r,\theta}},\qquad
 \|g\|_{L^2_TH_X^1}<23.617160\|f\|_{H^1_{r,\theta}},       \tag{P.14}
$$

and the interpolated $L^2_TH_X^{1/3}$ cost is less than $4.849380$.
The physical full $L^2$ reconstruction cost is less than $1.351779$.
The mixed-coordinate source in (P.14) explicitly includes the radial
derivative of $f$; it is not an angular-only source assertion.

## 3. The true graph and the complete foliation

Let $h_*=2^{-37}$. On the physical circle (P.1),
$T=-h_*C$ and $X=\theta-h_*H$. Its complete angular map has derivative
$X_\theta\ge1-h_*H_\theta^*>0$. Inverting that genuine circle map gives
the graph $t_g(X)$. Exact differentiation yields

$$
\begin{aligned}
 Q_-&=h_*C_-\le -t_g(X)\le h_*C^*=Q_+,\\
 |t_g'|&\le h_*C_\theta^*/(1-h_*H_\theta^*)=:p_*,\\
 |t_g''|&\le
 \frac{h_*C_{\theta\theta}^*}{(1-h_*H_\theta^*)^2}
 +\frac{h_*^2C_\theta^*H_{\theta\theta}^*}{(1-h_*H_\theta^*)^3}
 =:p_{2,*}.
\end{aligned}                                                       \tag{P.15}
$$

The actual enclosures are

$$
\begin{gathered}
 1.9107116472\cdot10^{-11}<-t_g(X)<5.0488770731\cdot10^{-11},\\
 p_*<1.315928\cdot10^{-10},\qquad p_{2,*}<2.382392\cdot10^{-8}.
\end{gathered}                                                       \tag{P.16}
$$

In particular $Q_->\delta$ and $Q_+<T_b$. The region between this graph
and $T=-\delta$ lies wholly in the established inverse product.

For either direction use the actual linear foliation

$$t(\tau,X)=(1-\tau)t_{m in}(X)+\tau t_{m out}(X),
 \qquad0\le\tau\le1,                                      \tag{P.17}$$

where the two ends are $t_g(X)$ and the constant $-\delta$, in the
chosen order. Put $\ell=t_\tau$, $p=t_X$, $Q=-t$ and $q=\sqrt Q$.
Then

$$
 L_-:=Q_--\delta\le|\ell|\le Q_+-\delta=:L_+,
 \quad |p|\le p_*,\quad |p_X|\le p_{2,*},\quad |\ell_X|\le p_* .      \tag{P.18}
$$

The exact transformed equation is

$$
 U_\tau=B U_X+C U+S,
 \quad B=d_fI+a_fJ(t),\quad
 a_f=\frac{\ell}{1-p^2Q},\quad d_f=a_fpQ,
 \quad C=a_f(I+pJ)\mathcal V,
 \quad S=a_f(I+pJ)M_f f.                                  \tag{P.19}
$$

This follows from $(I-pJ)U_T=J U_X+\mathcal VU+g$; it does not set
$t_X=0$. The denominator is positive since $p_*\sqrt{Q_+}<1/4$.
Thus the graph is uniformly spacelike for both real characteristic
families.

Every derivative in (P.19) is taken after pullback to $(\tau,X)$.
For example the coefficient derivative is
$\partial_X\mathcal V(t(\tau,X),X)=\mathcal V_X+p\mathcal V_T$.
The latter term is included in all bounds below.

## 4. Two symmetrized energy levels

Set

$$H=\operatorname{diag}(1,Q),\qquad
 E_0=\|H^{1/2}U\|_2,\qquad E_1=\|H^{1/2}U_X\|_2.         \tag{P.20}$$

$HB$ is exactly symmetric. For a smooth solution, integration on the
full circle gives

$$
 (E_0^2)'=\langle U,[H_\tau-(HB)_X+HC+C^*H]U\rangle
             +2\operatorname{Re}\langle HU,S\rangle.      \tag{P.21}
$$

There is no constraint on either mean in this identity. Define upper
bounds $a_*,a_{X,*},d_*,d_{X,*}$ for the four real foliation
coefficients. Explicitly, with $D_-=1-p_*^2Q_+$ and
$D_X^*=2p_*p_{2,*}Q_++p_*^3$, one may take

$$
\begin{gathered}
 a_*=L_+/D_-,\quad
 a_{X,*}=p_*/D_-+L_+D_X^*/D_-^2,\quad
 d_*=a_*p_*Q_+,\quad
 d_{X,*}=a_{X,*}p_*Q_++a_*p_{2,*}Q_++a_*p_*^2.
\end{gathered}                                                       \tag{P.22}
$$

Here $q_-:=\sqrt\delta$ and $q_+:=\sqrt{Q_+}$. Direct differentiation
of $HB=\left(\begin{smallmatrix}d_f&-a_fQ\\-a_fQ&d_fQ\end{smallmatrix}\right)$
shows that

$$
\begin{aligned}
 \|H^{-1/2}(HB)_XH^{-1/2}\|
 &\le d_{X,*}+d_*p_*/\delta+q_+a_{X,*}+a_*p_*/q_-=:B_s,\\
 \|H^{1/2}B_XH^{-1/2}\|
 &\le d_{X,*}+q_+a_{X,*}+a_*p_*/q_-=:B_1 .
\end{aligned}                                                       \tag{P.23}
$$

Both are less than $2.174725\cdot10^{-15}$ for this actual graph.
For the radial energy term, in either orientation,

$$
 \int_0^1\frac12\sup_X\frac{|\ell(X)|}{Q(\tau,X)}\,d\tau
 \le\log(q_+/q_-).                                      \tag{P.24}
$$

Indeed $L/[\delta+\tau L]$ is increasing in $L\ge0$, and the reverse
orientation replaces $\tau$ by $1-\tau$. This integrates the radial
variation before exponentiation.

Let $D_0,E_0^*$ bound the complete real diagonal and removable
off-diagonal functions in (P.4). The real estimates of Section 2 give
$D_0<81109.790$, $E_0^*<31.889730$. Therefore

$$V_H=D_0+q_+E_0^*,\qquad
 C_H=a_*(1+p_*q_+)V_H                                  \tag{P.25}$$

bounds $\|H^{1/2}CH^{-1/2}\|$.

For the derivative, retain the previous **complete complex** coefficient
envelopes $D_c,E_c$ from the balanced fold theorem. They give
$D_X=8192D_c$, $E_X=8192E_c$ and, on the present graph region,

$$D_T=D_c/(T_b-Q_+),\qquad E_T=E_c/(T_b-Q_+).              \tag{P.26}$$

These are holomorphic Cauchy bounds inside the previously proved
product, not bounds inferred from real suprema. In the upper-right
entry of $\partial_X\mathcal V(t(\tau,X),X)$ the exact extra term
$p e_{12}$ is retained. Consequently

$$
 V_{H,X}=D_X+p_*D_T+q_+(E_X+p_*E_T)+p_*E_0^*/q_-          \tag{P.27}
$$

is valid, and

$$
 C_{H,X}=a_{X,*}(1+p_*q_+)V_H
  +a_*(p_{2,*}q_++p_*^2/q_-)V_H
  +a_*(1+p_*q_+)V_{H,X}<0.096663064                       \tag{P.28}
$$

bounds the complete $H^{1/2}C_XH^{-1/2}$. The whole ordinary equation
and its first angular derivative now imply

$$
\begin{aligned}
 \sup E_0&\le G_0(E_{0,\rm in}+F_0),\\
 \sup E_1&\le G_1(E_{1,\rm in}+C_{H,X}\sup E_0+F_1),\qquad
 F_j=\|H^{1/2}\partial_X^jS\|_{L^1_\tau L^2_X},\\
 G_0&=(q_+/q_-)\exp(B_s/2+C_H)<1.862682,\qquad
 G_1=G_0e^{B_1}<1.862682 .
\end{aligned}                                                       \tag{P.29}
$$

This bounds all interior times and both directions. Existence can also
be proved within this finite negative annulus: the two smooth real
eigenvalues $d_f\pm a_fq$ admit their ordinary characteristic flows.
In their diagonal frame the remaining full two-state integral equation
has a bounded kernel on each compact time slab. Iterated Volterra
integration gives the $n!$ denominator and hence convergence on every
finite slab. Its differentiated equation gives the $H^1$ solution;
(P.29) supplies the displayed uniform bounds. Density then gives the
same result for the stated $H^1$ data and source. Thus (P.29) is not
merely a formal estimate for a solution whose existence is assumed.

## 5. The complete second row avoids inverse-$q$ reconstruction

The second component of (P.19) is exactly

$$
 (U_2)_\tau=d_f(U_2)_X-a_f(U_1)_X+C_{21}U_1+C_{22}U_2+S_2,            \tag{P.30}
$$

with

$$|C_{21}|\le a_*(E_0^*+p_*D_0)=:c_{21},\qquad
 |C_{22}|\le a_*(D_0+p_*Q_+E_0^*)=:c_{22}.              \tag{P.31}$$

Apply scalar transport energy to the actual real drift $d_f$.
Since $\|U_1\|_2\le E_0$ and $\|(U_1)_X\|_2\le E_1$,

$$
 \sup\|U_2\|_2\le
 G_2\bigl(\|U_{2,\rm in}\|_2+a_*\sup E_1+c_{21}\sup E_0
                    +\|S_2\|_{L^1_\tau L^2_X}\bigr),\quad
 G_2=e^{d_{X,*}/2+c_{22}}<1.000002915 .                  \tag{P.32}
$$

Neither (P.29) nor (P.32) divides the ordinary $U_2$ output by $q$.
This is the important ordered use of the two equations. Using
$\|U_2\|\le E_0/q_-$ in place of (P.32) would give a valid but much
larger contract, and is not the contract asserted here.

## 6. The true two-dimensional source on the between-graph domain

Let $m_0,m_X,m_T$ be the complete bounds for $M_f,(M_f)_X,(M_f)_T$
in (P.12). On the real domain $\|J(t)\|=1$. The source matrix
$P_s=a_f(I+pJ)M_f$ has

$$
\begin{aligned}
 P_0&=a_*(1+p_*)m_0,\\
 P_1&=a_{X,*}(1+p_*)m_0+a_*(p_{2,*}+p_*^2)m_0
                 +a_*(1+p_*)(m_X+p_*m_T).
\end{aligned}                                                       \tag{P.33}
$$

The exact $(\tau,X)$ angular derivatives of the physical coordinates
are bounded by
$r_X^g=|r_X|+p_*|r_T|$ and
$\theta_X^g=|\theta_X|+p_*|\theta_T|$.
Moreover the **actual** volume transformation is

$$d\tau\,dX=\frac{J_f}{|\ell|}\,dr\,d\theta.                       \tag{P.34}$$

It follows directly, with $\mathfrak m=(J_f^*/L_-)^{1/2}$, that

$$
\begin{gathered}
 F_0,\ \|S_2\|_{L^1L^2}
 \le s_0\|f\|_{H^1(\Omega_g)},\qquad s_0=\mathfrak mP_0
       <0.00003700000,\\
 F_1\le s_1\|f\|_{H^1(\Omega_g)},\qquad
 s_1=\mathfrak m[P_1+P_0(r_X^g+\theta_X^g)]<0.000496151 .             \tag{P.35}
\end{gathered}
$$

The time interval has length one, so $L^2_\tau$ controls the displayed
$L^1_\tau$ norms. Equation (P.33) includes both the mixed derivative of
$M_f$ and the derivative of the actual foliation; (P.35) includes the
physical radial derivative of $f$. No extension of $f$ beyond
$\Omega_g$ or conversion to an artificial rectangle is used.

## 7. Actual full Airy reconstruction at the flat endpoint

For the negative flat endpoint use exactly

$$
 \mathcal D=P^{1/6}\operatorname{diag}(W,W^{-1}),\quad
 W_m=(\delta+|m|^{-2/3})^{-1/4}\ (m\in4\mathbb Z\setminus\{0\}),
 \quad W_0=1,\quad P_m=\sqrt{1+m^2}.                     \tag{P.36}
$$

The two means have identity weight. The first component satisfies
$\|P^{1/6}WU_1\|_2\le\|U_1\|_{H^{1/3}}\le\|U_1\|_{H^1}$.
For the second, with $c_*=(\sqrt{17}/4)^{1/3}>1$,

$$
 \|P^{1/6}W^{-1}U_2\|_2^2
 \le q_-\|U_2\|_{H^{1/6}}^2+c_*\|U_2\|_2^2.             \tag{P.37}
$$

For nonzero modes this follows from
$P_m^{1/3}\sqrt{\delta+|m|^{-2/3}}
 \le q_-P_m^{1/3}+(P_m/|m|)^{1/3}$.
For $m=0$ its right side is larger than the exact weight one, so the
same inequality includes the means.

Write $H_*=(\sup E_0^2+\sup E_1^2)^{1/2}$ and
$Y_*:=\sup\|U_2\|_2$. Then
$\|U_1\|_{H^1}\le H_*$ and $\|U_2\|_{H^1}\le H_*/q_-$.
This latter intermediate weighted derivative estimate is used only
inside interpolation, where its negative power cancels:

$$
 \boxed{\|U(-\delta)\|_{\mathcal E}^2
  \le H_*^2+q_-^{2/3}Y_*^{5/3}H_*^{1/3}+c_*Y_*^2.}       \tag{P.38}
$$

Thus the final coefficient has a positive power of $q_-$, not an
inverse quarter-power. The ordinary output on a graph satisfies
$\|U\|_2\le[(\sup E_0)^2+Y_*^2]^{1/2}$.

Evaluate (P.29), (P.32), and (P.38) separately for the initial-data and
source columns. Linearity and the triangle inequality then combine the
two columns. In canonical ordinary $H^1$ input units the resulting
constants are

| Output or auxiliary quantity | Initial $H_X^1$ state | Physical $H^1(\Omega_g)$ source |
|---|---:|---:|
| $\sup E_0$ | $1.862682$ | $0.000068922$ |
| $\sup E_1$ | $2.198062$ | $0.000936581$ |
| $\sup\|U_2\|_2$ | $1.000002918$ | $0.000037001$ |
| Full ordinary state | $2.114141$ | $0.000078224$ |
| Flat full $\mathcal E$ state | $3.051486$ | $0.000939849$ |

The native report preserves the unrounded directed values.

## 8. Physical circle norms, both means, and exact scope

On (P.1), the angle derivative is the **fixed physical radius**
$X_\theta=1-h_*H_\theta$, not the fixed-$T$ derivative (P.10).
The full map $U=F^{-1}Rh$ obeys

$$
 \|U\|_{H_X^1}\le4.880777\|h\|_{H_\theta^1},\qquad
 \|h\|_{L^2_\theta}\le2.190538\|U\|_{L^2_X}.             \tag{P.39}
$$

To check the first bound directly, the fixed-$r$ derivative of the
frame is at most
$F_* C_\theta^*/[4C_-(1-h_*H_\theta^*)]$.
Use the two exact composition costs
$\sqrt{1+h_*H_\theta^*}$ and $(1-h_*H_\theta^*)^{-1/2}$
for the zeroth and derivative terms, then the Frobenius bound for their
two-row triangular product-rule matrix. No general exponential
composition estimate is inserted. Equations (P.39) and Section 7 give
precisely (P.2).

The actual physical means are always recovered with their actual
density. At the fixed-$r$ circle,

$$
 \langle h\rangle_\theta
 =\frac1{\pi/2}\int
    \frac{RF(t_g(X),X)U(t_g(X),X)}{X_\theta(r_*-h_*,\theta(X))}\,dX.
                                                                    \tag{P.40}
$$

At a fixed-$T$ circle the corresponding density is $T_r/J_f$.
These weighted expressions include both independent means. Neither
is replaced by a canonical zero-mean condition. Ordinary parameter
source columns, including the full target and centre parameter
derivatives when supplied to the physical equation, are covered by
the same complete source estimates.

This theorem attaches the actual inner fixed-$r$ circle to the true
negative Airy port. The further strict interval from the common-piece
left endpoint to (P.1) still needs its own propagation. The positive
regular graph and the entire body feedback inverse are also separate
obligations. In particular, the two different input norms in (P.2)
must remain visible when these operators are assembled.

## 9. Reproduction

Source:
`scripts/fourfold_codazzi_actual_fixed_radial_Airy_ports.py`.
Complete directed native report:
`notes/2026-11-13-R133-actual-alpha075-fixed-radial-Airy-ports-native.json.gz`.
All 15 gates pass. The report binds the actual complex germ, actual
fold, complete balanced collar, their source identities, and the
original exact candidate input SHA. It does not duplicate the large
reconstructible candidate array.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fourfold_codazzi_actual_fixed_radial_Airy_ports.py --out notes/2026-11-13-R133-actual-alpha075-fixed-radial-Airy-ports-native.json.gz
```

The consumer refuses to overwrite an existing report. Use a distinct
output name for any later independent run or refinement.
