# R133 supplement: exact fold-matrix cancellation and the leading old-inverse defect

2026-11-14, phase_inverse.

**Proved exact identities on the actual fold.** The point-matrix product
$H^{-1}H_D$ is an explicit off-diagonal multiplier on every original
piece, for every amplitude. For the complete closed leading amplitude,
the old-inverse defect and the primitive defect can also be written
without differentiating an independently bounded inverse matrix.

These are identities for the same trial and the same old angle. No
completed amplitude tensor, coefficient row or source integral is
changed. Directed numerical use of these identities remains a new
calculation. Neither a small strong-return constant nor a cutoff-97
inverse is asserted here.

## 1. Conventions and the complete fold identity

Use the true fold and the actual degree-zero operator of
[the first-forcing theorem](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md),
(L.1)--(L.6). The old coordinate, material derivative and physical
frequency are
$$
 \rho=r_*-r,\qquad D=\partial_r-d\partial_\phi,\qquad
 n=4|j|,\quad\epsilon=\operatorname{sgn}j.
 \tag{C.1}
$$
Thus
$$
 [D,\partial_\phi]=d_\phi\partial_\phi.
$$
In particular, a displayed $r$ derivative below cannot be replaced by
a $\rho$ derivative without changing its sign.

Write
$$
 a=\eta\sqrt{k},\quad T=-\rho A^{2/3},\quad
 Q=aA^{-1/3},\quad x=X_\phi,\quad y=T_\phi,\quad
 \mathsf K(T)=\begin{pmatrix}0&T\\1&0\end{pmatrix}.
 \tag{C.2}
$$
The letter $Q$ here is the scalar $aA^{-1/3}$; it is not the ordered
coefficient operator denoted $Q$ in the scalarization theorem.
The scalar $a$ depends only on $r$. The actual principal fold gives
$$
 DX=-\tfrac23a\rho^2A_\phi=-QTy,\qquad DT=Qx .
 \tag{C.3}
$$
Indeed $y=-(2/3)\rho A^{-1/3}A_\phi$. Consequently
$$
 H=i\epsilon x\,1+y\mathsf K,\qquad
 H_D=i\epsilon DX\,1+DT\,\mathsf K
       =-i\epsilon QH\mathsf K .
 \tag{C.4}
$$
This multiplication uses $\mathsf K^2=T1$. The same formula also
shows that $H$ and $H_D$ commute. At every point in the already
certified noncharacteristic fold domain,
$$
 \boxed{H^{-1}H_D=-i\epsilon Q\mathsf K.}
 \tag{C.5}
$$
This is an equality of full two-by-two matrices. It holds for
arbitrary amplitudes, including the actual next amplitude $w_1$.
There is no pseudodifferential inverse or old-angle primitive in
(C.5). The genuine operator $J$ remains the complete original
inverse and is not replaced by this point matrix.

For example, the complete local operator (L.5) becomes
$$
 \mathcal L_0w=\mu^{-1}
 \left[(D^2+\eta^2K\partial_\phi^2-T_0D+V_0)w
                  +i\epsilon\vartheta Q\mathsf K w\right].
 \tag{C.6}
$$
Here the unbold $K$ is the original scalar curvature coefficient.
In particular its off-diagonal terms are
$i\epsilon\vartheta QT w_b$ in the first row and
$i\epsilon\vartheta Q w_a$ in the second row. All local, radial,
mean and projected-remainder terms of the original scalar equation
are retained.

## 2. The leading amplitude and exact inverse reconstruction

The already proved closed amplitude is
$$
 w_0=G\binom{x^2-Ty^2}{-2i\epsilon xy}
                  =-GH^2e_1,\qquad e_1=\binom{1}{0} .
 \tag{C.7}
$$
Put $B=x^2-Ty^2$ and $Z=DG+2Gd_\phi$. The notation $B$ in this
section is a scalar fold expression, not the original coefficient
operator. The closed scalar factor has the exact angular identities
$$
 G_\phi=\frac{GA_\phi}{6A},\qquad
 Q_\phi=-\frac{QA_\phi}{3A}.
 \tag{C.8}
$$
They follow because all remaining factors in
$G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}E_G$ are radial.
Neither (C.8) nor its proof removes the old mean in $E_G$.

The amplitude $h$ used in the exact reconstruction (U.13) is
$$
 h=\eta^{-1}H^{-1}H_Dw_0
   =-\frac{i\epsilon Q}{\eta}\mathsf K w_0
   =\binom{-2QGTxy/\eta}{-i\epsilon QGB/\eta}.
 \tag{C.9}
$$
Since $\eta$ is radial, its old angular derivative is zero.
Define the complete old-inverse defect amplitude
$$
 g_d=Dw_0-\eta h_\phi
          =Dw_0+i\epsilon\partial_\phi(Q\mathsf K w_0).
$$
Then
$$
 \boxed{\begin{aligned}
 (g_d)_a&=ZB+2QTG_\phi xy,\\
 (g_d)_b&=i\epsilon\left\{-2Zxy+
        \frac{QGA_\phi}{2A}B+QGy^3\right\}.
 \end{aligned}}
 \tag{C.10}
$$
These formulas contain no independently estimated $H^{-1}$,
$(H^{-1})_\phi$, $X_{r\phi}$ or $T_{r\phi}$.

Here is a direct check, including the commutator signs. By (C.1),
$$
 Dx=(DX)_\phi+d_\phi x,\qquad
 Dy=(DT)_\phi+d_\phi y .
$$
Substitute (C.3) in these two identities, differentiate $B$, and
combine $D(GB)$ with $2\partial_\phi(QTGxy)$. The terms containing
$x_\phi$ and $y_\phi$ cancel. The remaining
$-2Q_\phi Txy-Qxy^2$ vanishes by the regular identities
$y=(2/3)TA_\phi/A$ and $Q_\phi=-QA_\phi/(3A)$.
The first line of (C.10) follows. In the second row the remaining
coefficient of $GB$ is
$-Q_\phi+QG_\phi/G=QA_\phi/(2A)$, and the remaining cubic is $QGy^3$.
This verification never divides by $T$. All the formulas are
holomorphic at the genuine root on the same proved domain.

An alternative matrix check, useful for auditing the sign, is
$$
 DH=(H_D)_\phi+d_\phi H,
$$
$$
 g_d=-Z H^2e_1+G_\phi H_DHe_1
                  +G\{H_DH_\phi-H(H_D)_\phi\}e_1 .
 \tag{C.11}
$$
Equations (C.10) and (C.11) are equivalent. They do not assume
that $G$ is constant or that the two characteristic branches agree.

## 3. The full primitive defect shares the same amplitude

Let $v$ now denote the original even background coefficient,
including its true mean. In (U.13)--(U.17), the primitive
reconstruction uses
$$
 y_{\mathrm{amp}}=H^{-1}(vH_Dw_0)
                =-i\epsilon vQ\mathsf K w_0 .
$$
Its exact defect therefore satisfies
$$
 \boxed{q_v=vDw_0-(y_{\mathrm{amp}})_\phi
               =v g_d+i\epsilon v_\phi Q\mathsf K w_0.}
 \tag{C.12}
$$
Thus the complete $R_QJ$ and primitive defect terms may use
one and the same accurately bounded $g_d$. The factors $v$ and
$v_\phi$ have their original roles. In particular $v$ is not
replaced by $Pv$ in the first term of (C.12).

The exact source identity remains
$$
 E_D=P\mathcal U(g_d)-LP\mathcal U(h)
$$
from [the complete old-circle remainder theorem](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md),
(U.13)--(U.19). All its separate old-mean maps remain. Replacing
the amplitudes by (C.9)--(C.12) is an equality before applying
$P$, $I$ or $J$. It does not commute any of these operators with
the fold or move the old mean to a canonical-$X$ mean.

## 4. Directed use and a complete elementary bound

On a fixed already certified analytic strip, let $G_+,Q_+,X_+,Y_+$
bound $|G|,|Q|,|x|,|y|$, and let $T_+,A_-$ and $A_{\phi,+}$
have their usual meanings. If $Z_+$ bounds the full $|DG+2Gd_\phi|$,
then (C.10) gives
$$
 \begin{aligned}
 |(g_d)_a|&\le
 Z_+(X_+^2+T_+Y_+^2)+
       2Q_+T_+|G_\phi|_+X_+Y_+,\\
 |(g_d)_b|&\le
 2Z_+X_+Y_++
       \frac{Q_+G_+A_{\phi,+}}{2A_-}
                       (X_+^2+T_+Y_+^2)+Q_+G_+Y_+^3 .
 \end{aligned}
 \tag{C.13}
$$
Complete angular derivative bounds follow by the finite ordered
Leibniz rule in these scalar and two-component products. In the
already used analytic Airy operator estimate, $g_d$ requires its
first old angular derivative. It suffices to retain
$G,G_\phi,G_{\phi\phi},G_{r\phi},G_r$ and the already saved
$A,A_\phi,A_{\phi\phi},x,x_\phi,y,y_\phi$, together with the
actual drift derivatives. In particular
$$
 Z_\phi=G_{r\phi}+d_\phi G_\phi-dG_{\phi\phi}
                                      +2Gd_{\phi\phi}.
 \tag{C.14}
$$
The scalar $G_r$ and $G_{r\phi}$ are real-piece derivatives of
the same closed amplitude. They can be bounded from the already
saved $A_\rho,A_{\rho\phi}$, divided-curvature derivative and
radial $\log E_G$ derivative, retaining $\partial_r=-\partial_\rho$.
They are not derivatives of a value-only error enclosure.

For the actual next local residual, differentiating (C.5) gives
$$
 \partial_r(H^{-1}H_D)
 =-i\epsilon\{Q_r\mathsf K+Q T_r\mathsf K'\},\qquad
 Q_r=a_rA^{-1/3}-\tfrac13aA^{-4/3}A_r .
 \tag{C.15}
$$
Thus the strict-piece derivative route in
[the third-jet and inner-root theorem](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md)
can use only this explicit product. It keeps the real $T_r$ and
the complete $\vartheta_r$ term.

No new original coefficient evaluation is needed for (C.13)--(C.15):
a consumer can read the accepted coefficient rows and leading jets,
evaluate only these new bounds, and leave the old complete tensors
and integrals unchanged. It must preserve every accepted new prefix.
The resulting bound, its angular width and every remaining old-mean
source must be saved as a new result. Numerical usefulness, the
whole corrected residual and the full high-frequency inverse remain
separate gates.
