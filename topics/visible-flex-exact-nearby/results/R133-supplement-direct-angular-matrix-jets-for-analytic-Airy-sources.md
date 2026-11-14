# R133 supplement: direct angular matrix jets for complete analytic Airy source bounds

2026-11-14, phase_inverse.

**Proved finite derivative recipe.** This supplies the analytic amplitude
inputs for
[the complete exponential Fourier estimate](R133-supplement-analytic-Airy-columns-and-complete-exponential-Fourier-bound.md).
It preserves the two Airy components separately and uses the existing
first-forcing angular variational records. No new ray or amplitude
solve, no extra radial derivative and no angular Cauchy loss are needed.

All statements below are on the same actual real radial pieces and
real explicit parameter disk as the completed larger-root calculation.
The old angle is complex on its paid strip. The original even mean
and every projected operator source remain.

## 1. Actual input strip and ordinary angular jets

Use the complete first-forcing records at a chosen radius $R$.
Their original domain gate is
$$
 E(\sigma_a+O_+)<1/16,\qquad
 E=e^{D_1R},\quad \sigma_a=3/64 ,
 \tag{J.1}
$$
where $R$ includes the true root uncertainty.
Thus the actual leading coefficients and their recorded derivatives
are analytic on the whole strip $\sigma_a$. Their constants
$C_2,C_3,c_{A,1},c_{A,2},c_{A,3}$ are from (L.13)--(L.14)
of the complete first-forcing proof, not newly fitted derivatives.

Write
$$
 X_1=E,\quad X_2=RC_2,\quad X_3=RC_3,\qquad
 A_k=Rc_{A,k}\quad(k=1,2,3).
 \tag{J.2}
$$
They bound the indicated actual old angular derivatives of $X$
and $A$, with $|A|\le A_+$ and $\operatorname{Re}A\ge A_->0$.
Complete bounds for $T=-\rho A^{2/3}$ are

$$
 \begin{split}
 T_0&=RA_+^{2/3},\\
 T_1&=\tfrac23R A_-^{-1/3}A_1,\\
 T_2&=\tfrac23R\{A_-^{-1/3}A_2+
                       \tfrac13 A_-^{-4/3}A_1^2\},\\
 T_3&=\tfrac23R\{A_-^{-1/3}A_3+
          A_-^{-4/3}A_1A_2+
                       \tfrac49 A_-^{-7/3}A_1^3\}.
 \end{split}                                          \tag{J.3}
$$

Here $T_k$ denotes a nonnegative bound for
$|\partial_\phi^k T|$, not the coefficient called $T_0$
in the scalar operator. The two meanings are distinguished
by context and by separate keys in the consumer.

The original $a_0,b_0$ leading derivative tables supply their
two angular derivatives and the first angular derivative of
their first radial derivatives on the same strip.
All are ordinary derivatives; product rules below include
their binomial coefficients.

## 2. Full two-by-two point inverse and its first two angular derivatives

Let $g_*>0$ be the actual complete lower bound for
$|X_\phi^2+TT_\phi^2|$ on this domain. The exact matrix is
$$
 H=i\epsilon X_\phi\,1+
         T_\phi\begin{pmatrix}0&T\\1&0\end{pmatrix}.
$$
Its inverse has the entrywise absolute bound

$$
 \mathsf B_0={1\over g_*}
 \begin{pmatrix}X_1&T_0T_1\\T_1&X_1\end{pmatrix}.
 \tag{J.4}
$$

Direct differentiation gives bounds for the entire first
and second derivatives of $H$:

$$
 \mathsf H_1=
 \begin{pmatrix}
 X_2&T_1^2+T_0T_2\\T_2&X_2
 \end{pmatrix},\qquad
 \mathsf H_2=
 \begin{pmatrix}
 X_3&3T_1T_2+T_0T_3\\T_3&X_3
 \end{pmatrix}.
 \tag{J.5}
$$

The exact inverse identities, with their full order retained,
are
$$
 (H^{-1})_\phi=-H^{-1}H_\phi H^{-1},
$$
$$
 (H^{-1})_{\phi\phi}
 =2H^{-1}H_\phi H^{-1}H_\phi H^{-1}
                         -H^{-1}H_{\phi\phi}H^{-1}.
$$
Consequently entrywise nonnegative matrix bounds are

$$
 \mathsf B_1=\mathsf B_0\mathsf H_1\mathsf B_0,\qquad
 \mathsf B_2=
 2\mathsf B_0\mathsf H_1\mathsf B_0\mathsf H_1\mathsf B_0+
                    \mathsf B_0\mathsf H_2\mathsf B_0 .
 \tag{J.6}
$$

The multiplication here is actual two-by-two multiplication.
The off-diagonal bounds remain small when the true
$T_\phi,T_{\phi\phi}$ are small. They are not replaced by
the full scalar matrix norm before acting on an amplitude.

## 3. The radial characteristic matrix retains its angular structure

Use the exact old identities
$$
 DX=-\tfrac23a\rho^2A_\phi,\qquad
 DT=aA^{-1/3}X_\phi,\qquad D=\partial_r-d\partial_\phi.
$$
The radial scalar $a$ is independent of $\phi$.
Set
$$
 s_0=A_-^{-1/3},\quad
 s_1=\tfrac13A_-^{-4/3}A_1,\quad
 s_2=\tfrac13A_-^{-4/3}A_2+
                         \tfrac49A_-^{-7/3}A_1^2.
$$
For $k=0,1,2$ the following are complete derivative bounds:
$$
 Z_k=\tfrac23a_+R^2A_{k+1},
$$
$$
 Y_0=a_+s_0X_1,\quad
 Y_1=a_+(s_0X_2+s_1X_1),\quad
 Y_2=a_+(s_0X_3+2s_1X_2+s_2X_1).
 \tag{J.7}
$$
The matrices for $H_D=i\epsilon DX\,1+DT\left(\begin{smallmatrix}0&T\\1&0\end{smallmatrix}\right)$ are therefore bounded entrywise by

$$
 \mathsf D_0=
 \begin{pmatrix}Z_0&Y_0T_0\\Y_0&Z_0\end{pmatrix},\qquad
 \mathsf D_1=
 \begin{pmatrix}Z_1&Y_1T_0+Y_0T_1\\Y_1&Z_1\end{pmatrix},
$$
$$
 \mathsf D_2=
 \begin{pmatrix}
 Z_2&Y_2T_0+2Y_1T_1+Y_0T_2\\Y_2&Z_2
 \end{pmatrix}.
 \tag{J.8}
$$

These bounds keep the genuine radial coefficient variation.
They use neither a frozen radial model nor a numerical
difference of two unrelated coefficient intervals.

## 4. Finite vector-jet arithmetic for every old source amplitude

For matrix derivative bounds $\mathsf M_k$ and two-component
vector bounds $v_k$ use the ordinary rule
$$
 (\mathsf Mv)_k\le
       \sum_{\ell=0}^k{k\choose\ell}\mathsf M_\ell v_{k-\ell}.
 \tag{J.9}
$$
All products on the right are entrywise nonnegative bounds.
Scalar products use the same binomial rule. This proves all
computed bounds without assuming commutativity of matrices.

Let $w=w_0$ and retain its two components separately.
The required amplitude expressions are exactly
$$
 h=\eta^{-1}H^{-1}H_Dw,\quad
 y=H^{-1}(vH_Dw),\quad
 Dw=w_r-dw_\phi,
$$
$$
 g_d=Dw-\eta h_\phi,\qquad q_v=vDw-y_\phi .
 \tag{J.10}
$$
The symbol $v$ on the right is the actual background second
component, including its original even mean.

Using (J.2)--(J.9) and the original complete coefficient
bounds on width $1/16$ gives $h,y,H_Dw$ through angular
order two and $Dw,g_d,q_v$ through order one on width
$3/64$. The first radial derivative of $w$ and its first
angular derivative are already in the completed leading
table. No new radial derivative is introduced here.

For $\mathfrak D z=\partial_\phi(H^{-1}z)$, the exact
identities U.20--U.23 now use only
$$
 H^{-1}z,\quad \mathfrak Dz,\quad
             \mathfrak D^2(H_Dw),\quad \mathfrak D(Dw).
 \tag{J.11}
$$
The second iteration is evaluated by the ordered
matrix-vector rule, not by treating $H^{-1}$ as scalar.
For example its zeroth-order bound is
$$
 \mathfrak D^2z\ \le\
 (\mathsf B_1\mathsf B_1+\mathsf B_0\mathsf B_2)z_0+
 (2\mathsf B_0\mathsf B_1+\mathsf B_1\mathsf B_0)z_1+
                      \mathsf B_0\mathsf B_0 z_2 .
 \tag{J.12}
$$

Each two-component value in (J.11)--(J.12) is inserted
directly into (A.16)--(A.18) of the analytic Airy theorem.
In particular the derivative Airy profile retains its
$R^{1/2}$ or $R^{1/4}N^{-1/6}$ fee; a large second
component is not charged as a first Airy component.

## 5. Same complete operator products and true radial source integrations

Use the already completed directed matrix constants for
$S_V,S_Q,R_QJ,R_QJL,c_BT_{v_\phi}I$ and the three mean
functionals. Their exact words and old projections are
unchanged. Formula (M.18) in the directed matrix theorem
uses the new analytic $\mathscr A,\mathscr B,M_0,M_D$;
(M.19) retains the independent even mean in full.

The common composition constant uses the original real
ray bounds $m=2-E$, $M=E$, $F_2=RC_2$, $F_3=RC_3$.
The actual inverse phase strip for the new Fourier factor
is
$$
                   \tau=(2-E)\,3/64>0 .
 \tag{J.13}
$$
The source consumer must check these domain and
noncharacteristic conditions against the completed
actual case records. It then pays the whole exponential
tail in (A.4), including mean output.

Finally integrate the same squared $|\rho|^{-1/4}$
envelope, separately on both sides of the uncertain root
bracket. The true positive collar/body cut, independent
mean, all nonmean output frequencies and the complete
negative Cauchy/primitive factors are retained.

This is a norm refinement on the same actual leading
remainder. It does not pay $\mathcal L_0w_1$, change the
first corrected trial or remove any of its original
1079 seams. Numerical improvement requires its own
actual public computation.
