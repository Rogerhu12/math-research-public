# R110 supplement: characteristic densities, retained mean and complete weak sources

2026-11-13, reproduce-newton.

**Status.** The full equations, source conversion, mean equation and
two-layer comparison below are proved. The actual all-time R106 certificate
gives a complete $L^2$ diagonal-density transport bound below $6.202$,
verified by sixteen exact BigInt gates. The continuous coupling coefficients
and the resulting whole strict-core comparison have not been numerically
computed. No root, positive-collar or full Schur inverse is inferred.

The object is the same explicitly symmetric exact affine family
$$
 p_0=-7789843107295549/4611686018427387904,\qquad
 |p-p_0|\le10^{-9}.
$$
All statements concerning the PDE apply only on a declared closed strictly
negative radial interval inside $(-t(p),t(p))$. The finite quarter-core
$[-1/4,1/4]$ contains positive collars and is not such an interval.

## 1. Exact weak-source state

Use the actual R37/R107 operator and physical angle:
$$
 \mathcal Pu=\partial_r(a u_r+bDu)+D(bu_r+c_{\rm pr}Du)+d u,
 \quad D=\partial_\theta,\quad d=\tau+D\sigma,
$$
$$
 \alpha=a^{-1}>0,\qquad v=b/a,\qquad
 \gamma=bv-c_{\rm pr}>0.
$$
The angular period is $\pi/2$, so the nonzero physical frequencies are
$4k$, not $k$. The letter $c_{\rm pr}$ here denotes the modified angular
principal coefficient. The positive characteristic speed below is a
different quantity.

For
$$
 \mathcal Pu=f_0+\partial_r f_r+D f_\theta
$$
define the exact shifted momentum
$$
 q=Du,\qquad p=a u_r+bq-f_r .
$$
Then
$$
 \begin{aligned}
 u_r&=\alpha p-vq+\alpha f_r,\\
 q_r&=D(\alpha p-vq)+D(\alpha f_r),\\
 p_r&=D(\gamma q-vp)-d u+
              f_0+D(f_\theta-vf_r).                         \tag{D.1}
 \end{aligned}
$$
No radial derivative of $f_r$ is used in this state equation. For the
saved finite reference the exact R107 choice remains
$$
 f_0=-R_0,\qquad f_r=R_r,\qquad f_\theta=R_\theta,\qquad p=p_N.
 \tag{D.2}
$$
Here $p_N$ is the physical momentum, not its saved scale $p_N/8$.
For the reference-minus-true error, $p=p_N-p_{\rm true}$.

## 2. Exact density diagonalization

Put
$$
 A=(\gamma/\alpha)^{1/4}>0,\quad
 c=\sqrt{\alpha\gamma}>0,\quad
 s_\pm=v\mp c,\quad
 y_\pm=Aq\pm A^{-1}p.                                       \tag{D.3}
$$
Thus
$$
 q=\frac{A^{-1}}2(y_++y_-),\qquad
 p=\frac A2(y_+-y_-),\qquad
 \alpha=c/A^2,\quad\gamma=cA^2 .
$$
Define
$$
 B_\pm=\left(\partial_r+(v\pm c)D\right)\log A,\qquad
 t=dA^{-1},
$$
$$
 F_\pm=A D(\alpha f_r)
       \ \pm A^{-1}\{f_0+D(f_\theta-vf_r)\}.                 \tag{D.4}
$$
Direct substitution in (D.1) gives the two exact density equations
$$
 \boxed{\quad
 (y_\pm)_r+D(s_\pm y_\pm)=B_\pm y_\mp\mp t u+F_\pm .
 \quad}                                                       \tag{D.5}
$$
For example, the coefficient of $D y_+$ in $(y_+)_r$ is $c-v$,
the coefficient of $y_+$ is $(c-v)_\theta$, and that of $y_-$ is
$A_r/A+(v+c)A_\theta/A$. These give the plus equation without
leaving an uncharged diagonal potential. The minus equation follows
from the same substitution with the opposite sign.

The two $B_\pm$ are genuine remaining couplings. They are not being
set to zero because the principal flow has been conjugated, nor replaced
by their angular means. The full sign-changing $d=\tau+D\sigma$ is retained.

## 3. Exact mean equation and the factor $1/4$

Let $\langle\cdot\rangle$ be the normalized physical angular mean,
$m=\langle u\rangle$, and let
$$
 \mathcal R=D^{-1}(I-P_0),\qquad
 \mathcal R e^{4ik\theta}=(4ik)^{-1}e^{4ik\theta}\quad(k\ne0).
$$
For every real Sobolev index used below,
$$
 \|\mathcal R:H^s\longrightarrow H^s\|=\frac14.              \tag{D.6}
$$
The exact constraint $\langle q\rangle=0$ gives
$$
 u=m+\mathcal R q
   =m+\frac12\mathcal R\{A^{-1}(y_++y_-)\}.                 \tag{D.7}
$$
Consequently the complete mean equation is
$$
 \boxed{\quad
 m_r=\langle h_+y_++h_-y_-+\alpha f_r\rangle,\qquad
 h_\pm=\frac12(\pm\alpha A-vA^{-1}).
 \quad}                                                       \tag{D.8}
$$
The mean is a scalar evolution coupled to both density channels.
It is not a deleted compatibility condition. Likewise $\langle p\rangle$
is retained inside $y_+-y_-$.

The factor $1/8$ in the estimates below is exactly the product of
$1/2$ in (D.7) and $1/4$ in (D.6). It must not be replaced by a
normalized-label inverse derivative without paying the physical factor.
The paired regular cap variable has zero direct core source column;
it remains present in the complete six-dimensional retained system.

For the spectral convention
$\|f\|_{H^s}^2=\sum_k\max(1,|4k|)^{2s}|f_k|^2$,
the same constraint gives the useful exact identity
$$
 \|u\|_{H^{s+1}}^2=|m|^2+\|q\|_{H^s}^2.                    \tag{D.9}
$$
If a later interface uses $(1+|4k|^2)^{s/2}$ instead, the usual norm
conversion must be included once. For $s\ge0$, its ratio to the
present weight is at most $(17/16)^{s/2}$ on nonzero modes and is
exactly one on the mean.

## 4. Both diagonal flows from the actual R106 certificate

R106 has proved the actual all-time forward characteristic
$\Theta_+(r,x,p)$, with normalized label $x$ of period $2\pi$,
physical angle period $\pi/2$, and initial value $H_5(x)/4$ at one root.
It is not the label identity. Its complete real parameter tube satisfies
$$
 0<m_J=\frac{213831}{7812500}
       <J_+(r,x,p)=\partial_x\Theta_+,
 \qquad
 J_+(r,x,p)<M_J=\frac{8223669}{7812500}.                     \tag{D.10}
$$
These bounds hold at all intermediate times and all real labels, not
just at the endpoint return.

The exact R105 parity is $\alpha(-r)=\alpha(r)$,
$\gamma(-r)=\gamma(r)$ and $v(-r)=-v(r)$. It implies
$$
 s_+(-r,\theta)=-s_-(r,\theta).
$$
Therefore define the opposite characteristic by
$$
 \Theta_-(r,x,p)=\Theta_+(-r,x,p).
 \tag{D.11}
$$
It solves the other physical characteristic equation and carries its
labels from the opposite root. Its Jacobian has precisely the same
bounds (D.10). If the saved forward convention names the opposite sign,
the two names are interchanged.

This is a construction of two coordinate families with different
initial radial endpoints. It is not a second application of the
half-return to a possibly wider label image. Hence it does not bypass
R106's explicit warning about an uncharged second passage. No complex
composition through a second return is used here.

For a homogeneous density equation
$$
 z_r+s z_\theta+\omega s_\theta z=0
$$
along either characteristic family, the exact solution is
$$
 z(r,\Theta(r,x))
  =\left(\frac{J(t,x)}{J(r,x)}\right)^\omega z(t,\Theta(t,x)).
 \tag{D.12}
$$
Change variables in normalized physical $L^2$. The ratio of measures is
$J(r,x)/J(t,x)$, so
$$
 \|T_\omega(r,t)\|_{2\to2}
 \le \left(\frac{M_J}{m_J}\right)^{|\omega-1/2|}.             \tag{D.13}
$$
The factor four relating the normalized label and physical measures
cancels in this relative estimate. In particular, with
$$
 Q_J=M_J/m_J=\frac{913741}{23759},
$$
the complete actual bounds are
$$
 \boxed{
 \|T_1(r,t)\|_{2\to2}<6.202,\qquad
 \|T_{3/2}(r,t)\|_{2\to2}<38.459,\qquad
 \|T_{1/2}(r,t)\|_{2\to2}=1 .
 }                                                            \tag{D.14}
$$
They hold for either radial order and arbitrary intermediate radii in
the declared strict interval. The local differential equations and
couplings below still cannot be evaluated at a degenerate root.

The separate critical composition calculation in R116 addresses
height $H^{1/2}$ and density $H^{-1/2}$. Its inexpensive constants are
**not** constants for the density channels $y_\pm$ in $H^{+1/2}$.
The next section pays that higher density through its exact commutator,
not by relabeling a negative-order port estimate.

## 5. Complete two-layer strong comparison

Let $J=\max(1,|D|)^{1/2}$ as in R110, and write $Z_\pm=Jy_\pm$.
For any scalar speed $s$,
$$
 J\{y_r+D(sy)\}
 =Z_r+sDZ+\frac32(Ds)Z+R_s y,\qquad
 R_s=D[J,s]-\tfrac12(Ds)J.                                  \tag{D.15}
$$
Thus its high principal transport is exactly $T_{3/2}$ in (D.14).
The remainder drives the base $L^2$ state only. It is not placed
in a single high-energy exponential rate.

Write $\mathcal A(a)$ for any proved full bound for $\|[J,a]\|_{2\to2}$,
and $\mathcal K(s)$ for one for $\|R_s\|_{2\to2}$.
The complete Fourier bounds in R110 are permitted. Alternatively,
the new [periodic-kernel supplement](R110-complete-periodic-kernel-tame-bounds.md)
provides
$$
 \mathcal A(a)\le O_a+\frac4{\sqrt\pi}\sqrt{O_a\|Da\|_\infty},
$$
$$
 \mathcal K(s)\le\frac6{\sqrt{2\pi}}
       \sqrt{\|Ds\|_\infty\|D^2s\|_\infty}
                       +\frac32\|Ds\|_\infty .              \tag{D.16}
$$
Here $O_a$ is the complete oscillation about an actual constant.
The mean corrections in both formulas are already included.

For each actual radial piece put
$$
 a_*=\|A^{-1}\|_\infty,\quad a^*=\|A\|_\infty,\quad
 t_*=\|t\|_\infty,\quad b_\pm=\|B_\pm\|_\infty,\quad
 h_\pm^*=\|h_\pm\|_2,
$$
$$
 P=\frac18t_*a_*,\qquad
 E_P=\frac18\{\mathcal A(t)a_*+t_*\mathcal A(A^{-1})\}.
$$
A valid complete base coupling majorant, in coordinate order
$(m,y_+,y_-)$, is
$$
 C=
 \begin{pmatrix}
 0&h_+^*&h_-^*\\
 t_*&P&b_++P\\
 t_*&b_-+P&P
 \end{pmatrix}.                                               \tag{D.17}
$$
The same $C$ is sufficient for the high principal couplings, and the
full additional low-to-high forcing is bounded by
$$
 R=
 \begin{pmatrix}
 0&0&0\\
 \mathcal A(t)&\mathcal K(s_+)+E_P&\mathcal A(B_+)+E_P\\
 \mathcal A(t)&\mathcal A(B_-)+E_P&\mathcal K(s_-)+E_P
 \end{pmatrix}.                                               \tag{D.18}
$$

To verify the potential part, set
$$
 U_h=m+\tfrac12\mathcal R\{A^{-1}(Z_++Z_-)\}.
$$
Since $J$ commutes with $\mathcal R$,
$$
 Ju-U_h=\tfrac12\mathcal R\{[J,A^{-1}](y_++y_-)\},
$$
$$
 J(tu)-tU_h=[J,t]u+
             \tfrac12t\mathcal R\{[J,A^{-1}](y_++y_-)\}.
$$
Use (D.6) and
$\|u\|_2\le |m|+a_*(\|y_+\|_2+\|y_-\|_2)/8$ to get exactly
the potential entries in (D.18). The $B_\pm$ entries are
$J(B_\pm y_\mp)=B_\pm Z_\mp+[J,B_\pm]y_\mp$.
The remaining diagonal entries come from (D.15).
Finally the high mean row uses
$|\langle h_\pm y_\pm\rangle|\le\|h_\pm\|_2\|Z_\pm\|_2$;
it introduces no hidden derivative of the mean.

### Complete source matrices

Let $\mathcal M_s(a)$ be a proved multiplier bound on the present $H^s$.
For example the full Wiener sum
$\sum_k(1+|4k|)^s|a_k|$ is sufficient for $s\ge0$.
Also
$$
 \mathcal M_{1/2}(a)\le\|a\|_\infty+\mathcal A(a).             \tag{D.19}
$$
Use the common strong source vector
$$
 F(r)=\bigl(\|f_0\|_{H^{1/2}},
           \|f_r\|_{H^{3/2}},\|f_\theta\|_{H^{3/2}}\bigr)^t.
$$
Both the base and high mean source are bounded by
$\|\alpha\|_2 F_r$, where the subscript here selects the second vector
entry, not a radial derivative. Define
$$
 S_0=
 \begin{pmatrix}
 0&\|\alpha\|_2&0\\
 a_*&a^*\mathcal M_1(\alpha)+a_*\mathcal M_1(v)&a_*\\
 a_*&a^*\mathcal M_1(\alpha)+a_*\mathcal M_1(v)&a_*
 \end{pmatrix},
$$
$$
 S_h=
 \begin{pmatrix}
 0&\|\alpha\|_2&0\\
 \mathcal M_{1/2}(A^{-1})&
 \mathcal M_{1/2}(A)\mathcal M_{3/2}(\alpha)+
 \mathcal M_{1/2}(A^{-1})\mathcal M_{3/2}(v)&
 \mathcal M_{1/2}(A^{-1})\\
 \mathcal M_{1/2}(A^{-1})&
 \mathcal M_{1/2}(A)\mathcal M_{3/2}(\alpha)+
 \mathcal M_{1/2}(A^{-1})\mathcal M_{3/2}(v)&
 \mathcal M_{1/2}(A^{-1})
 \end{pmatrix}.                                               \tag{D.20}
$$
They follow from the complete signed sources (D.4),
$\|Dg\|_{H^{1/2}}\le\|g\|_{H^{3/2}}$, and the corresponding
base inequality. They keep both source slots and all means.
If the actual joint source Gram is computed directly, the signs and
cross terms in (D.4) may be retained for a sharper result.

### Ordered comparison, without a factor per artificial spline cell

Set
$$
 X_0=(|m|,\|y_+\|_2,\|y_-\|_2)^t,\quad
 X_h=(|m|,\|Z_+\|_2,\|Z_-\|_2)^t,\quad
 X=(X_0,X_h)^t,
$$
$$
 D_0=\operatorname{diag}(1,6.202,6.202),\quad
 D_h=\operatorname{diag}(1,38.459,38.459),\quad
 D_*=\operatorname{diag}(D_0,D_h),
$$
$$
 C_*=\begin{pmatrix}C&0\\R&C\end{pmatrix},\qquad
 S_*=\binom{S_0}{S_h}.
$$
Variation of constants for the exact diagonal characteristic transports
and (D.14) give the positive vector inequality
$$
 X(r)\le D_*X(t)+\int_t^r
       D_*\{C_*(z)X(z)+S_*(z)F(z)\}\,dz
 \qquad(r\ge t).                                             \tag{D.21}
$$
Backward propagation uses the reversed radial order and the same absolute
majorants. Let $\Phi$ be the ordered positive propagator of
$V'=D_*C_*V$. A sufficient complete comparison is
$$
 X(r)\le \Phi(r,t)D_*X(t)
          +\int_t^r\Phi(r,z)D_*S_*(z)F(z)\,dz.                \tag{D.22}
$$
For piecewise coefficient bounds, $\Phi$ is the ordered product of the
actual comparison matrices. The factor $D_*$ is inserted once for the
initial diagonal evolution, not once at every arbitrary knot.
The true diagonal group already propagates through those knots, with
the same global root labels. Its variation-of-constants kernels are
what justify the factors multiplying actual coupling events.

For a full five-input source Gram
$$
 \int_I \bigl(\|f_0(z;\xi)\|_{H^{1/2}}^2+
              \|f_r(z;\xi)\|_{H^{3/2}}^2+
              \|f_\theta(z;\xi)\|_{H^{3/2}}^2\bigr)\,dz
 \le \xi^*G\xi,
$$
the zero-initial forced component obeys
$$
 X_i(r;\xi)^2\le K_i^2\,\xi^*G\xi,\qquad
 K_i^2=\int_I\sum_{j=1}^3
     |(\Phi(r,z)D_*S_*(z))_{ij}|^2\,dz.                      \tag{D.23}
$$
This is Cauchy--Schwarz over the complete radial interval and three
source components. It is not an inference from a local transfer-error
sum or from separately unweighted columns.

## 6. Physical reconstruction and actual available field inputs

The exact half-order reconstruction bounds are
$$
 \|q\|_{H^{1/2}}
 \le\frac{a_*}{2}(\|Z_+\|_2+\|Z_-\|_2)
      +\frac{\mathcal A(A^{-1})}{2}(\|y_+\|_2+\|y_-\|_2),
$$
$$
 \|p\|_{H^{1/2}}
 \le\frac{a^*}{2}(\|Z_+\|_2+\|Z_-\|_2)
      +\frac{\mathcal A(A)}{2}(\|y_+\|_2+\|y_-\|_2).
 \tag{D.24}
$$
Combine the first with (D.9) to recover $u$ in $H^{3/2}$.
The actual canonical/root/label frame and its source injection still
have their own fees. No complete high inverse follows from the physical
strict-core estimate alone.

All coefficient quantities above can be obtained from the same complete
nine-field rectangle; no new geometric primitive is needed.
For example, put $l=\log A$:
$$
 l_\theta=\tfrac14(\gamma_\theta/\gamma-\alpha_\theta/\alpha),
 \quad l_r=\tfrac14(\gamma_r/\gamma-\alpha_r/\alpha),
$$
$$
 l_{\theta\theta}=\tfrac14\left[
  \gamma_{\theta\theta}/\gamma-(\gamma_\theta/\gamma)^2
 -\alpha_{\theta\theta}/\alpha+(\alpha_\theta/\alpha)^2\right],
$$
$$
 l_{r\theta}=\tfrac14\left[
 \gamma_{r\theta}/\gamma-\gamma_r\gamma_\theta/\gamma^2
 -\alpha_{r\theta}/\alpha+\alpha_r\alpha_\theta/\alpha^2\right],
$$
$$
 (B_\pm)_\theta=l_{r\theta}
          +(v_\theta\pm c_\theta)l_\theta
          +(v\pm c)l_{\theta\theta}.
$$
Together with $d_\theta=\tau_\theta+\sigma_{\theta\theta}$, these supply
the first derivatives needed for $\mathcal A(t)$,
$\mathcal A(A^{\pm1})$ and $\mathcal A(B_\pm)$.
The true $c_{\theta\theta}$ follows by differentiating
$c=\sqrt{\alpha\gamma}$ and supplies $\mathcal K(s_\pm)$.
The saved rectangle already includes complete physical-r derivative
errors through angular order two, so the mixed $r\theta$ term has a
declared complete error contract. Positivity of $\alpha,\gamma$ and
every division must be verified on each actual closed cell.

In a native implementation, squares of cross-zero interval values must
be evaluated bilinearly. The actual flint 0.9 cross-zero-power failure
is not remedied by silently replacing a ball by its midpoint.

No completed continuous tables for (D.17)--(D.20) are currently saved.
Their evaluation and the ordered strong comparison remain work to do.
The six-dimensional retained mean/regular Schur and the true roots and
positive caps retain their earlier separate contracts.

## 7. Executed finite arithmetic and precise scope

The source is
[scripts/fourfold_characteristic_density_budget_exact.mjs](../scripts/fourfold_characteristic_density_budget_exact.mjs).
It checks the exact UTF8 SHA256 of the completed R106 ray report and
the three cited R106/R105/R77 proofs, checks all original 24 ray gates,
the whole real parameter interval and actual object/reference identities,
and performs sixteen exact rational gates.
Its complete output is
[notes/2026-11-13-R110-characteristic-density-transport.json](../notes/2026-11-13-R110-characteristic-density-transport.json).

The exact ratios prove
$Q_J=913741/23759<(3101/500)^2$ and $Q_J<38459/1000$.
The identical pure function actually ran in V8. Its native CLI is only
a file-replay wrapper and has not run.

These are genuine full-family, all-time diagonal **$L^2$** transport
constants. They do not certify the complete coupled PDE, do not upgrade
density $H^{-1/2}$ into $H^{1/2}$, do not replace the lost nine-field
arrays by a receipt, and do not supply a nonlinear isometric family.
