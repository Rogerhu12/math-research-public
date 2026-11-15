# R133 supplement: signed first forcing for the genuine common radial reference

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities and a root cancellation.** Replacing the free Airy columns by the two genuine common-radial columns changes the first normalized forcing by one explicit scalar potential. At the true root its large common radial term cancels exactly. The remaining expression contains the complete finite-frequency correction, nonradial Fourier products, and the independent old-circle remainder.

This is an analytic result, not a new numerical source norm or a cutoff inverse. It concerns the same explicit finite-background family, fixed intrinsic $\eta_0$, both signs of $j$, and the original physical seams. All products at complex $\delta$ are bilinear; no conjugation of the family is introduced.

## 1. Same mode, same fold, and the exact differential replacement

Use [the common radial reference](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md), (C.19)--(C.22), and [its complete old-circle interface](R133-supplement-common-radial-reference-old-circle-primitive-and-mean-interface.md). Fix
$$
 n=4|j|,\quad \epsilon=\operatorname{sgn}j,\quad |j|\ge97,
 \qquad Y_{j,TT}=(n^2T-V_j(T))Y_j.
 \tag{F.1}
$$
Either of the two independent genuine columns may be used. The normalized decaying column at the positive reference endpoint does not by itself impose the physical positive boundary condition.

In the original nonradial fold write
$$
 \mathcal U_j^V(w)=e^{i\epsilon nX}
          (w_1Y_j+n^{-1}w_2Y_{j,T}),\quad
 \mathcal K=\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \quad x=X_\phi,\quad y=T_\phi .
$$
The function $V_j$ is evaluated at the actual $T(r,\phi)$, after its radial-reference definition has been fixed. It is not silently replaced by its value at the same physical $r$ in the radial chart.

Let
$$
 D=\partial_r-d\partial_\phi,\quad
 \mu=Q^2(x^2+Ty^2),\quad
 H=i\epsilon x\,\mathrm{Id}+y\mathcal K,\quad
 H_D=i\epsilon DX\,\mathrm{Id}+DT\,\mathcal K .
$$
The correct principal sign is $\partial_T^2+T\partial_X^2$.
For the differential part
$D^2+\eta^2K\partial_\phi^2-T_0D+V_0$, put
$$
 c_T=\frac{D^2T+\eta^2K T_{\phi\phi}-T_0DT}{\mu}.
 \tag{F.2}
$$
This coefficient is analytic on the paid fold; (F.2) never divides by $T$ or $K$.

Retain the exact free-reference degree-zero operator of
[the first-forcing theorem](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md):
$$
 \mathcal L_0w
 =\mu^{-1}\{(D^2+\eta^2K\partial_\phi^2-T_0D+V_0)w
                         -\vartheta H^{-1}H_Dw\}.
 \tag{F.3}
$$
Its $\vartheta$ term is the retained first part of the complete old primitive/inverse. It is not a local coefficient that can be deleted.

For any amplitude pair define
$$
 \mathcal C_j(w)=E_{12}\{2V_jw_T+(V_{j,T}+c_TV_j)w\}.
 \tag{F.4}
$$
Direct substitution of $Y_{TT}=(n^2T-V_j)Y$ into the two derivative rules gives the exact differential replacement
$$
              -V_jw-n^{-1}\mathcal C_j(w).
 \tag{F.5}
$$
The ordinary $T$ derivative in (F.4) is taken in the same canonical chart. If implemented in old variables it must use the exact inverse Jacobian and its true one-sided traces.

## 2. The complete retained inverse term and its finite correction

Set
$$
 H_j^V=H-\frac{yV_j}{n^2}E_{12},\qquad B_j=(H_j^V)^{-1}.
$$
The actual whole-circle gap for this matrix was paid separately; its application still requires the original parity combination and the original $J$ domain. By (I.12),
$$
 B_jH_{D,j}^V
 =H^{-1}H_D-\frac{QV_j}{n^2}
                    B_je_1(i\epsilon y,\ x),
 \qquad H^{-1}H_D=-i\epsilon Q\mathcal K.
 \tag{F.6}
$$
Consequently the retained term $-\vartheta B_jH_{D,j}^Vw$ differs from the old one by the **positive**
$$
 \frac1{n^2}\mathcal R_j(w),\qquad
 \mathcal R_j(w)=\vartheta QV_j B_je_1(i\epsilon y,\ x)w.
 \tag{F.7}
$$
All matrix orders and input powers in this identity are fixed. The finite-frequency factor does not license commuting $n^{-2}$ through a full output operator.

There is an explicit exact remainder, not an implicit discarded error. In (U.13)--(U.19) of
[the complete old-circle decomposition](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md), replace
$$
 \mathcal U\mapsto\mathcal U_j^V,\quad
 H^{-1}H_D\mapsto B_jH_{D,j}^V,\quad
 W\mapsto W^V=nH_{D,j}^Vw+Dw .
 \tag{F.8}
$$
Keep the original $P,I,J,L,S_Q,S_V,R_Q$ and every mean in their original order. More explicitly set
$$
 h^V=\eta^{-1}B_jH_{D,j}^Vw,\qquad
 y^V=B_j(vH_{D,j}^Vw),
$$
$$
 E_D^V=P\mathcal U_j^V(Dw-\eta h^V_\phi)
                       -LP\mathcal U_j^V(h^V).
$$
Then the exact reconstruction is
$JD_0P\mathcal U_j^V(w)=P\mathcal U_j^V(h^V)+JE_D^V$.
The six terms of (U.17) with these substitutions give
$\mathcal E_R^V$, and
$$
 \mathcal N^V(w)
 =S_VP\mathcal U_j^V(w)-\mathcal E_R^V(w)
   +P(T_0)\Pi\mathcal U_j^V(W^V)
   -P(V_0)\Pi\mathcal U_j^V(w).
 \tag{F.9}
$$
Thus the complete projected scalar identity is
$$
 \boxed{\;
 \mathcal P_{\rm sc}P\mathcal U_j^V(w)
 =P\mathcal U_j^V\!\left[
    \mu\{n\mathcal T_\epsilon w+(\mathcal L_0-V_j)w
                         -n^{-1}\mathcal C_j(w)\}
                    +n^{-2}\mathcal R_j(w)\right]
                 +\mathcal N^V(w).\;}
 \tag{F.10}
$$
This follows by the exact derivative identities and the same finite projected algebra used for (U.18). No large-$n$ limit is needed. On a reference matching interface all actual distributional jumps in (I.7)--(I.10) must be added. Formula (F.10) is first an identity on one common smooth branch.

## 3. Normalization changes exactly one forcing component

Keep the original leading amplitudes
$$
 a_0=G(x^2-Ty^2),\qquad b_0=-2i\epsilon Gxy,\qquad
 w_0=\binom{a_0}{b_0},\qquad
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix}.
 \tag{F.11}
$$
Here $b_0$ is an amplitude; the local coefficient called $b_0$ in (U.5) is denoted $B_{\rm coef}$ below.
The leading transport is unchanged, $\mathcal T_\epsilon w_0=0$.
Its exact determinant is $G^2(x^2+Ty^2)^2$.

Let the previously defined signed first forcing and its normalization be
$$
 F=\binom{F_b}{F_a}=-\mathcal L_0w_0,\qquad
 f=\binom{f_b}{f_a}=M_0^{-1}F .
$$
The new first forcing is
$$
 F^V=-(\mathcal L_0-V_j)w_0=F+V_jw_0 .
$$
Because $M_0e_1=w_0$, **before any absolute-value estimate**
$$
 \boxed{\qquad f_b^V=f_b+V_j,\qquad f_a^V=f_a.\qquad}
 \tag{F.12}
$$
This is the same input label $j$ throughout. A mode-dependent potential or gauge cannot be moved through a physical convolution and assigned to its output label.

The original Fuchsian transport recurrence may now be used with $f^V$ to define $w_1^V=M_0(A^V,B^V)^t$. Its analytic root normalization is
$$
 A^V(0,X)=0,\qquad B^V(0,X)=f_b(0,X)+V_j(0).
 \tag{F.13}
$$
Thus the nonzero integration constant is retained, with a new exact value. The old $w_1$ has not been relabeled as $w_1^V$.

For $w=w_0+n^{-1}w_1^V$, (F.10) gives the complete retained local expression
$$
 \begin{split}
 &\frac{\mu}{n}\{(\mathcal L_0-V_j)w_1^V-\mathcal C_j(w_0)\}\\
 &+\frac1{n^2}\{-\mu\mathcal C_j(w_1^V)+\mathcal R_j(w_0)\}
       +\frac1{n^3}\mathcal R_j(w_1^V),
 \end{split}
 \tag{F.14}
$$
in addition to $\mathcal N^V(w_0+n^{-1}w_1^V)$.
It must be reconstructed by the same full $J$ and accompanied by the independent even-mean row.

The extra terms have exact root zeros. Write $b_0=T^2\widetilde b_0$ and $y=T^2\widetilde y$. Then
$$
 \mathcal C_j(w_0)
 =T e_1\{4V_j\widetilde b_0+
       2V_jT\,\partial_T\widetilde b_0
       +T(V_{j,T}+c_TV_j)\widetilde b_0\},
$$
$$
 (i\epsilon y,\ x)w_0=-i\epsilon G y(x^2+Ty^2).
 \tag{F.15}
$$
Therefore $\mathcal C_j(w_0)=O(T)$ and
$\mathcal R_j(w_0)=O(T^2)$ on a fixed paid common germ. Their numerical bounds and all needed derivatives remain to be consumed.

## 4. A signed formula at the true root

All quantities in this section are evaluated at the actual root after taking derivatives at fixed old angle. Set
$$
 C=d_\phi|_*,\quad a_\infty=\eta\sqrt{k},\quad
 L=(a_{\infty,r}/a_\infty)|_*,\quad
 t=(\eta_r/\eta-4b\langle S\rangle)|_*,
$$
$$
 E_\infty=\langle e\rangle,\quad
 B_\infty=\langle B_{\rm coef}\rangle,\quad
 q_\infty=E_\infty-B_\infty+\eta_r/\eta,\qquad
 \kappa_*=(\eta_*\sqrt{k_*})^{2/3}.
 \tag{F.16}
$$
The symbol $C$ is a complete angular function, not a norm. Let
$V_\infty(0)=V(0,0)$ denote the $z=0$ value of the same rational-frequency potential; at $K=0$ its explicit $K$-multiple correction vanishes.

The root fold satisfies $x=1$, $y=y_r=0$. Differentiating the exact old-$\rho$ equations (L.16) twice and using $\partial_r=-\partial_\rho$ gives
$$
 \begin{split}
 A_r/A&=\tfrac35(L+C),\\
 A_{rr}/A&=\tfrac37 a_{\infty,rr}/a_\infty
       +\tfrac67LC+\tfrac37C_r+\tfrac37C^2
                              +\tfrac{27}{35}dC_\phi,\\
 x_r&=C,\qquad x_{rr}=C_r+C^2+dC_\phi,\qquad
 y_{rr}=\tfrac45\kappa_* C_\phi .
 \end{split}
 \tag{F.17}
$$
In particular these are true signed derivatives, not derivatives of an upper enclosure.

If $g=G_{\infty,r}/G_\infty|_*$, the exact closed leading formula gives
$g=t/2-2L/5$ and $G_r=g+C/10$.
A direct product differentiation of (F.11), followed by
$D^2=\partial_r^2-2d\partial_r\partial_\phi+
(d d_\phi-d_r)\partial_\phi+d^2\partial_\phi^2$, yields
$$
 \begin{split}
 (D^2a_0)_*={}&G_{\infty,rr}|_*+
       \left(\tfrac4{175}L+\tfrac{21}{5}g\right)C
       +\tfrac{619}{140}C^2
       +\tfrac{29}{14}(C_r-dC_\phi),\\
 (Da_0)_*&=g+\tfrac{21}{10}C,\qquad
 (D^2b_0)_*=-\tfrac85 i\epsilon\kappa_* C_\phi .
 \end{split}
 \tag{F.18}
$$

For the local operator coefficient one must differentiate its full expression before putting $K=0$:
$$
 B_{\rm coef}-B_\infty=d_\phi-2bK P(v^2).
$$
Consequently
$$
 (V_0)_*-
 \{(\eta_r/\eta+E_\infty)B_\infty-B_{\infty,r}\}_*
 =(t+3B_\infty)C+4C^2-DC+2bK_rP(v^2).
 \tag{F.19}
$$
The last term cannot be dropped by substituting $K=0$ too early.

The radial two-row elimination gives exactly
$$
 \kappa_*^2 V_\infty(0)
 =G_{\infty,rr}|_*-t\,G_{\infty,r}|_*+
       \{(\eta_r/\eta+E_\infty)B_\infty-B_{\infty,r}\}_* .
$$
Combining this identity with (F.3), (F.6), and (F.18)--(F.19) proves
$$
 \boxed{
 \begin{split}
 f_b^V(0,\phi)={}&V_j(0)-V_\infty(0)
 -\frac1{\kappa_*^2}\left[
   \left(\tfrac{12}{35}L-\tfrac32q_\infty\right)C
   -\tfrac{291}{140}C^2+\tfrac{15}{14}DC
                               +2bK_rP(v^2)\right],\\
 f_a^V(0,\phi)={}&\frac{i\epsilon}{\kappa_*}
                       \left(\tfrac85 C_\phi-\vartheta_*\right).
 \end{split}}
 \tag{F.20}
$$
The full $\vartheta_*$ remains; the second equation is not a radial approximation.

Since $\langle C\rangle=\langle C_r\rangle=0$ and
$\langle DC\rangle=\langle C^2\rangle$ by periodic integration by parts,
the **complete old-angle scalar coefficient** is
$$
 \boxed{\quad
 \langle f_b^V(0,\cdot)\rangle
   =V_j(0)-V_\infty(0)
       +\frac{141}{140\kappa_*^2}\langle C^2\rangle .
 \quad}
 \tag{F.21}
$$
At complex parameters this square is bilinear, not $|C|^2$. It may subsequently be bounded in modulus.

The finite-frequency difference in (F.21) also has a removable factor. Write $z=j^{-2}$,
$D_{uu}=zU(z)$, $D_{vv}=zW(z)$, and $a/\eta=1+z\alpha/\eta$ as in (C.1). Then
$$
 Q_1(z)=-2bU(z)+2bK W(z)
            +\frac{\partial_r(\alpha/\eta)}{1+z\alpha/\eta},
 \qquad q(z)-q_\infty=zQ_1(z).
$$
At the root, exactly,
$$
 V_j(0)-V_\infty(0)
 =\frac{z}{\kappa_*^2}
       \left\{\frac{Q_{1,r}}2-\frac{q_\infty Q_1}2
                                  -\frac{zQ_1^2}4\right\}_* .
 \tag{F.22}
$$
The $r$ derivative is taken at fixed $z$. All finite denominators and complete repaired means remain in it.

As a useful exact audit, for an angle-independent background $u=0,v=m(r)$ one has $d=\vartheta=\alpha=D_{uu}=D_{vv}=0$, the actual fold is the radial fold, $w_0=(G_\infty,0)$, and
$\mathcal L_0w_0=V_jw_0$. Thus the whole first forcing $F^V$ vanishes on that background, while both ordinary physical source rows and the independent mean continue to have their original equations.

## 5. A minimal genuinely new numerical consumer

No old target, FFT, cubic repair, fold coefficient or successful Taylor degree is to be recomputed. The root values in (F.20)--(F.22) require only original accepted signed intrinsic/background coefficients through the displayed radial orders. The actual primitive uses all modes of the degree-$96$ explicit family. Products such as $C^2$, $dC_\phi$ and the coefficient of $\vartheta$ can reach degree $384$ and must not be projected back to $96$.

A first public consumer can assemble these full Laurent polynomials and the rational $z$ dependence directly, with all repairs and the physical mean, then enclose $0\le z\le97^{-2}$ and the declared complex $\delta$ box. It must report finite signed terms, their complete Fourier support, the exact scalar/nonconstant split, and the true parameter identity. It must not evaluate $f_b^V$ by adding a numerical upper bound for $f_b$ to an unrelated upper bound for $V$.

Extending beyond the root needs the actual analytic functions on the same auxiliary/root piece. One valid finite recipe is to reuse the accepted signed Taylor coefficients, form $F+V_jw_0$ or the normalized expression (F.12) coefficientwise, and retain the complete analytic tails of every factor and reciprocal. The $V_j$ composition uses the actual $T$, so its Taylor and derivative remainders require the common potential domain and the fold image gate. A finite polynomial sum is not the whole function.

This new forcing does not reuse the old first correction unchanged. The new Fuchsian solve keeps (F.13), all genuine nonzero-entry data at later physical seams, and both signed branches. The $G_j/G_\infty$ physical gauge and the full input/output transforms of (C.18) are not commuted through the old circle. Their fees remain explicit if that different physical reference normalization is used.

Finally, (F.9), the independent even mean, the actual positive two-end graph, all true source jumps, and the full low/high feedback remain. The paid real reference-column bounds and $H_j^V$ inverse bounds do not supply an unproved complex-column norm or a complete strong return estimate.
