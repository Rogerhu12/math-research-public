# R133 supplement: ordered complete sources for the genuine reference and a whole-domain correlated forcing identity

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities and a conditional norm recipe.** This keeps the two genuine reference columns, the actual first correction, the complete old-circle inverse, both physical source rows and all interface terms. It also gives a whole-domain cancellation formula for the normalized forcing. No numerical strong-source constant or full high inverse is asserted.

Use the same fixed intrinsic parameter $\eta_0$, repaired finite-background family, complex $\delta$ square, original physical root and physical pieces as in [the signed first-forcing theorem](R133-supplement-signed-first-forcing-and-root-cancellation-for-genuine-common-reference.md). The actual complete derivative tables are [the whole original root-piece result](R133-supplement-actual-whole-root-piece-signed-reference-Taylor-bounds.md). The new amplitude is $w_1^V$, not the old $w_1$.

All identities below are first used on one common smooth reference branch. At a physical or reference matching interface the corresponding distributional terms must be restored. The same old-angle parity domain is required whenever the genuine inverse $J$ is applied.

## 1. Eliminate the canonical derivative without dividing by T

Fix $j$, $n=4|j|$, $\epsilon=\operatorname{sgn}j$, $|j|\ge97$, and the two independent solutions of
$$
 Y_{j,TT}=(n^2T-V_j(T))Y_j .                              \tag{G.1}
$$
Write
$$
 D=\partial_r-d\partial_\phi,\quad x=X_\phi,\quad y=T_\phi,
 \quad \mathcal K=\begin{pmatrix}0&T\\1&0\end{pmatrix},
$$
$$
 DT=Qx,\qquad DX=-QTy,\qquad
 \eta^2K=Q^2T,\qquad \mu=Q^2(x^2+Ty^2).                  \tag{G.2}
$$
Here $r$, not $\rho=r_*-r$, is the radial coordinate. The Jacobian in this orientation is
$$
 \mathcal J_r=T_rX_\phi-T_\phi X_r=Q(x^2+Ty^2),
 \qquad \mu/\mathcal J_r=Q .                            \tag{G.3}
$$
The scalar $Q$ in (G.2) is not the ordered operator called $Q$ in the scalarization.

Set $A_T=D^2T+\eta^2K T_{\phi\phi}-T_0DT$.
The correction from (F.4) has the exact old-variable expression
$$
 \boxed{\quad
 \mathfrak C_j(w):=\mu\mathcal C_j(w)
 =E_{12}\{2QV_j[xDw+QTy\,w_\phi]
                 +(\mu V_{j,T}+A_TV_j)w\}.\quad}        \tag{G.4}
$$
Indeed $w_\phi=yw_T+xw_X$ and $Dw=Qxw_T-QTyw_X$, so
$xDw+QTyw_\phi=Q(x^2+Ty^2)w_T$. This proves (G.4) directly.
It contains neither $1/T$ nor a derivative of an inverse coordinate map. The analytic root extension uses the paid fold and nonzero $\mu$.

Every $V_j,V_{j,T}$ is evaluated at the same actual $T(r,\phi)$. The matrix $E_{12}$ stays on the left. Differentiation uses the full ordered Leibniz rule; $E_{12}$ is not commuted through a subsequent matrix.

## 2. Three retained local vectors with exact input weights

Let
$$
 H=i\epsilon x\,1+y\mathcal K,\qquad
 H_D=i\epsilon DX\,1+DT\,\mathcal K,\qquad
 H_j^V=H-\frac{yV_j}{n^2}E_{12},
$$
$$
 B_j=(H_j^V)^{-1},\qquad
 H_{D,j}^V=H_D-\frac{DT\,V_j}{n^2}E_{12}.                 \tag{G.5}
$$
Use the actual old-circle inverse gap of [the two-column interface](R133-supplement-actual-genuine-common-radial-columns-and-old-circle-inverse.md), only on its stated domain. Exactly,
$$
 B_jH_{D,j}^V=-i\epsilon Q\mathcal K
             -\frac{QV_j}{n^2}B_je_1(i\epsilon y,\ x).
$$
Define
$$
 \begin{split}
 \mathfrak A_j(w)={}&
 (D^2+\eta^2K\partial_\phi^2-T_0D+V_0-\mu V_j)w
                       +i\epsilon\vartheta Q\mathcal K w,\\
 \mathfrak R_j(w)={}&
 \vartheta QV_jB_je_1(i\epsilon y,\ x)w .
 \end{split}                                            \tag{G.6}
$$
The row vector in $\mathfrak R_j$ acts before $B_je_1$; their matrix order is fixed.

Let $w_0$ be the original leading amplitude and let
$$
 w_1^V=w_1+(Tb_0,a_0)^t\mathcal B_j(T),\qquad
 2T\mathcal B_j'+\mathcal B_j=V_j,\quad \mathcal B_j(0)=V_j(0).
$$
Its normalized forcing is $(f_b+V_j,f_a)^t$. Put
$$
 L_{1,j}=\mathfrak A_j(w_1^V)-\mathfrak C_j(w_0),\quad
 L_{2,j}=-\mathfrak C_j(w_1^V)+\mathfrak R_j(w_0),\quad
 L_{3,j}=\mathfrak R_j(w_1^V).                           \tag{G.7}
$$
The complete retained local scalar residual of $w_0+n^{-1}w_1^V$ is
$$
 P\mathcal U_j^V\{n^{-1}L_{1,j}
                  +n^{-2}L_{2,j}+n^{-3}L_{3,j}\}.       \tag{G.8}
$$
This is (F.14) with the unnormalized numerator displayed. A bound for normalized $\mathcal L_0w_1^V$ alone would omit $\mu$ and the new terms.

Define
$$
 \mathsf S^V(w)c=\sum_j n^{1/6}\mathcal U_j^V(w_j)c_j,\qquad
 \mathsf T^V(w)c=\sum_j n^{7/6}\mathcal U_j^V(w_j)c_j .
$$
Amplitudes may depend on the input label. With $Nc_j=nc_j$, (G.8) becomes
$$
 P\{\mathsf S^V(L_1)+\mathsf S^V(L_2)N^{-1}
                            +\mathsf S^V(L_3)N^{-2}\}.  \tag{G.9}
$$
The powers are on the input, before physical convolution or output projection. On $|j|\ge J_0$ they have norms at most $(4J_0)^{-1}$ and $(4J_0)^{-2}$ in this order. They are not output Fourier multipliers.

## 3. Explicit complete old-circle remainder

Retain exactly $P,I,J,L,S_Q,S_V,R_Q$ and $B_{\rm op}$ from [U.1--U.19](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md). Set
$$
 h_j=\eta^{-1}B_jH_{D,j}^Vw_j,\qquad
 y_j=B_j(vH_{D,j}^Vw_j),\qquad
 g_j=Dw_j-\eta(h_j)_\phi,\quad q_j=vDw_j-(y_j)_\phi .
 \tag{G.10}
$$
The symbol $q_j$ here is an amplitude, not the later radial logarithmic coefficient. If
$E_D^V=P\mathcal U_j^V(g_j)-LP\mathcal U_j^V(h_j)$, then
$$
 JD_0P\mathcal U_j^V(w_j)
        =P\mathcal U_j^V(h_j)+JE_D^V .                  \tag{G.11}
$$
With $c_B=-2bK$ and $W_j=nH_{D,j}^Vw_j+Dw_j$, the full six terms are
$$
 \begin{split}
 \mathcal E_R^V(w)={}&
 S_QP\mathcal U_j^V(h_j)+R_QJE_D^V
       +c_BT_{v_\phi}IP\mathcal U_j^V(q_j)\\
 &-Pr_Q\,\Pi\mathcal U_j^V(h_j)
       -c_BP v_\phi\,\Pi\mathcal U_j^V(y_j)\\
 &-c_BT_{v_\phi}I(Pv)\,\Pi\mathcal U_j^V(W_j).
 \end{split}                                            \tag{G.12}
$$
Thus
$$
 \mathcal N^V(w)=S_VP\mathcal U_j^V(w)-\mathcal E_R^V(w)
       +P(T_0)\Pi\mathcal U_j^V(W_j)
       -P(V_0)\Pi\mathcal U_j^V(w).                      \tag{G.13}
$$
Every mean is at fixed old $r,\phi$. The vector $T_{v_\phi}I(Pv)$ multiplies the old scalar mean; replacing it by an operator acting on that mean could erase it incorrectly.

An exact compression, without a discarded input frequency, is
$$
 D\mathcal U_j^V(w_j)-\partial_\phi\mathcal U_j^V(\eta h_j)
                    =\mathcal U_j^V(g_j),\qquad
 \Pi\mathcal U_j^V(W_j)=\Pi\mathcal U_j^V(g_j).           \tag{G.14}
$$
The second equality follows by the full-circle first identity and holds for either density exponent. It is not a mean in the variable $X$.

## 4. Typed complete source bounds

The following is a conditional norm recipe at real allowed parameter values. Holomorphic parameter domains are used to bound coefficients and amplitudes; they do not by themselves give Sobolev bounds for a complex phase. At a fixed real radial circle, suppose that a bound
$$
 \mathcal A^V(w)\ \ge\
 \|\mathsf S^V(w):H^{-4/3}_{|j|\ge J_0}\longrightarrow H^{-5/3}\|
 \tag{G.15}
$$
has actually been paid for the chosen genuine columns, both input signs and every output, including the mean. It must allow the input-label dependence of $V_j,B_j,w_j$. An amplitude supremum alone is not (G.15).

Put $\mathfrak D_jw=\partial_\phi(B_jw)$. The exact derivative rule, with the full differentiated $B_j$, gives
$$
 \mathsf T^V(w)=\partial_\phi\mathsf S^V(Bw)
                         -\mathsf S^V(\mathfrak Dw).
 \tag{G.16}
$$
Define
$$
 \begin{array}{c|c|c|c|c}
 i&X_i&Y_i&\Gamma_i(w)&M_i(w)\\ \hline
 0&H^{-8/3}&H^{-5/3}&
 \mathcal A^V(Bw)+\mathcal A^V(\mathfrak Dw)&
 \mathcal A^V(\mathfrak Dw)\\
 1&H^{-5/3}&H^{-2/3}&\mathcal A^V(w)&\mathcal A^V(w)
 \end{array}
 \tag{G.17}
$$
Thus $\Gamma_0$ bounds the density $\mathsf T^V$ into $X_0$ and $\Gamma_1$ bounds $\mathsf S^V$ into $X_1$. The corresponding full old means are bounded by $M_i$, since the mean of the first term in (G.16) is zero. The input space is always the one in (G.15).

For each $i$, use genuine coefficient bounds
$$
 \begin{gathered}
 c_{J,i}:J:X_i\to Y_i,\qquad
 c_{L,i}:L:X_i\to X_i,\quad c_{B,i}:B_{\rm op}:X_i\to X_i,\\
 c_{R,i}:R_Q:Y_i\to Y_i,\qquad
 c_{Q,i}:S_Q:X_i\to Y_i,\quad c_{V,i}:S_V:X_i\to Y_i .
 \end{gathered}
 \tag{G.18}
$$
The actual old-circle coefficient algorithms U.24--U.25 and U.7--U.11 provide these windows when evaluated on the same coefficient domain. An ordinary $L^2$ norm of $J$ does not replace either declared one-gain bound.

Write $m_q(f)=\sum_\ell(1+|4\ell|)^q|\widehat f_\ell|$ and $C_I=\sqrt{17}/4$. Set
$$
 E_i(w)=\Gamma_i(g)+c_{L,i}\Gamma_i(h).
$$
Then a complete bound for (G.13), into $Y_i$, is
$$
 \begin{split}
 N_i(w)={}&c_{V,i}\Gamma_i(w)+c_{Q,i}\Gamma_i(h)
                           +c_{R,i}c_{J,i}E_i(w)\\
 &+|c_B|m_3(v_\phi)C_I\Gamma_i(q)\\
 &+m_0(r_Q)M_i(h)+|c_B|m_0(v_\phi)M_i(y)\\
 &+\{|c_B|m_0(v_\phi)m_0(v)/4+m_0(T_0)\}M_i(g)
                                  +m_0(V_0)M_i(w).
 \end{split}
 \tag{G.19}
$$
The compressed mean in the penultimate line is exactly (G.14), not a bound for $Dw$ alone. In particular all five mean contributions remain.

The reconstructed nonmean trial is
$$
 h_2=P\mathcal U_j^V(w),\qquad
 h_1=P\mathcal U_j^V(h)+J\{E_D^V-B_{\rm op}P\mathcal U_j^V(w)\}.
$$
For its independent even-mean residual, a sufficient complete bound at density $i$ is
$$
 \begin{split}
 M_i^{\rm phys}(w)=2|bm|\{&
 M_i(uh)+m_3(u)c_{J,i}[E_i(w)+c_{B,i}\Gamma_i(w)]\\
 &+|K|M_i((v-m)w)\}.
 \end{split}
 \tag{G.20}
$$
This follows from the exact row
$g_2=2bm\langle u h_1+K(v-m)h_2\rangle$.
Only the specified trial has zero reconstructed mean. Independent supplied mean sources and their ports are not set to zero. A constant output has the same Bessel Sobolev norm in both output windows.

Since $Y_1$ embeds contractively in $Y_0$, the complete first original-row source of $w_0+n^{-1}w_1^V$ is bounded in $H^{-2/3}$ by
$$
 \begin{split}
 c_{J,1}\{&
 \mathcal A^V(L_1)+(4J_0)^{-1}\mathcal A^V(L_2)
                  +(4J_0)^{-2}\mathcal A^V(L_3)\\
 &+N_0(w_0)+N_1(w_1^V)\}.
 \end{split}
 \tag{G.21}
$$
The second, independent constant row costs
$M_0^{\rm phys}(w_0)+M_1^{\rm phys}(w_1^V)$.
Both rows must subsequently be integrated in the actual physical radial measure and connected to the actual source-to-port maps. No final inverse is inferred by adding these scalar expressions.

The previously paid real reference-column and inverse-matrix bounds do not by themselves prove (G.15) on a tilted complex circle. On the oscillatory side it can be established by a true all-output column estimate with the needed old angular derivatives. On the positive side an unrestricted growing reference column has no uniform polynomially weighted input bound of this kind on a fixed interval. Its coefficient has to be supplied by the actual two-ended positive graph, or an explicitly proved weighted Green construction. Choosing the decaying column alone does not impose that graph.

## 5. Physical and reference seams remain explicit

At a fixed physical seam suppose the coefficient traces $d,B_{\rm op},J$ are common, as in the original continuous repaired background. For $f=P\mathcal U_j^V(w)$, the physical two-trace jump is exactly
$$
 [h_2]=[f],\qquad
 [h_1]=J\{[f_r]-d\,\partial_\phi[f]-B_{\rm op}[f]\}.
 \tag{G.22}
$$
This formula is used with the actual one-sided first-correction traces; no jump is inferred to vanish merely from a formal asymptotic order. If a coefficient or a reference normalization itself changes, its actual trace change must also be included before applying (G.22).

A fixed old circle can cross a reference matching curve. On each smooth subarc (G.16) holds. Writing $F=\mathsf S^V(Bw)$, the distributional version includes
$$
 \mathsf T^V(w)=\partial_\phi F-\mathsf S^V(\mathfrak Dw)
                         -\sum_{\phi_s}[F]_{\phi_s}\delta_{\phi_s}.
 \tag{G.23}
$$
The corresponding primitive has the explicit negative term
$-I\sum_s[F]_{\phi_s}\delta_{\phi_s}$. Both column traces and their normalization must therefore be checked; two-port matching of $Y,Y_T$ alone is not a proof that $B_jw$ has a common trace. Formula (G.14) likewise requires the full-circle distributional terms when such an interface is present.

Finally, if a paid source envelope is $C|\rho|^{-1/4}$, its squared radial cost on one side of the true root over length $R$ is $2C^2\sqrt R$. The two sides, and the two portions of an uncertain-root bracket, are charged separately. This is an integration rule for a paid envelope, not a substitute for (G.15).

## 6. Separate the exact radial part before taking a modulus

This section gives a whole-domain identity for the first normalized forcing. It is not obtained by subtracting two numerical upper bounds.

Use the exact original coefficients U.5 and U.10, writing $b_{\rm c}$ for their local coefficient to distinguish it from $b_0$ in $M_0$. Put
$$
 \begin{gathered}
 E_{\rm m}=\langle e\rangle,\qquad B_{\rm m}=\langle b_{\rm c}\rangle,
 \qquad a_{\rm c}=\eta_r/\eta+E_{\rm m},\\
 t=a_{\rm c}+B_{\rm m}
           =\eta_r/\eta-4b\langle u^2+Kv^2\rangle,\\
 C=d_\phi=-bP(u^2+Kv^2),\qquad Z=2bK P(v^2).
 \end{gathered}
 \tag{G.24}
$$
All means are actual old-angle means of the full repaired family. At complex parameters the products remain bilinear. The exact decompositions are
$$
 e=E_{\rm m}+3C+Z,\qquad
 b_{\rm c}=B_{\rm m}+C-Z,\qquad
 t_Q=a_{\rm c}+4C+Z,\qquad T_0=t+5C.
 \tag{G.25}
$$
Define $V_{\rm m}=a_{\rm c}B_{\rm m}-(B_{\rm m})_r$. Since
$V_0=t_Qb_{\rm c}-Db_{\rm c}-K v_{AC}$,
$$
 \begin{split}
 \Delta V_0:=V_0-V_{\rm m}
 ={}&(a_{\rm c}+4B_{\rm m})C+(B_{\rm m}-a_{\rm c})Z
       +4C^2-3CZ-Z^2\\
    &-DC+DZ-Kv_{AC},\qquad
 v_{AC}=\ell^2-4b\eta v u_\phi .
 \end{split}
 \tag{G.26}
$$
The full derivative $DZ$ is retained. In particular its root value includes $2bK_rP(v^2)$; substituting $K=0$ before differentiating is invalid.

Let $a_\infty=\eta\sqrt{k}$ and use the radial fold
$$
 \bar A(\rho)=\frac32\int_0^1\sqrt s\,a_\infty(s\rho)\,\mathrm ds,
 \qquad \bar T=-\rho\bar A^{2/3},\qquad
 \kappa=\partial_r\bar T=a_\infty\bar A^{-1/3}.
$$
The radial leading amplitude is defined with the same complete mean integral as the actual amplitude:
$$
 \begin{gathered}
 \mathcal E(r)=\exp\!\left[-2\int_{r_*}^r
                         b\langle u^2+Kv^2\rangle\,\mathrm dr\right],\\
 \bar G=(k_*/\eta_*)^{1/6}\bar A^{1/6}k^{-1/4}\mathcal E,\qquad
 G/\bar G=(A/\bar A)^{1/6}.
 \end{gathered}
 \tag{G.27}
$$
Thus $\bar G$ is not obtained by setting $u=0,v=m$ in the actual coefficients. It retains their complete radial means.

Write
$$
 \ell_\kappa=\kappa_r/\kappa,\qquad
 q_{\rm rad}=a_{\rm c}-B_{\rm m},\qquad
 V_{\rm rad}(\bar T)
 =\kappa^{-2}\left\{
 \frac{(q_{\rm rad})_r-(\ell_\kappa)_r}{2}
            +\frac{\ell_\kappa^2-q_{\rm rad}^2}{4}\right\}.
 \tag{G.28}
$$
Then, exactly,
$$
 \bar G_r/\bar G=(t-\ell_\kappa)/2,\qquad
 (\partial_r^2-t\partial_r+V_{\rm m})\bar G
                 =\kappa^2V_{\rm rad}(\bar T)\bar G .
 \tag{G.29}
$$
For the second identity substitute the first and use
$t=a_{\rm c}+B_{\rm m}$, $q_{\rm rad}=a_{\rm c}-B_{\rm m}$.
There is no division by $\rho$ or $K$.

Set $\bar w=(\bar G,0)^t$ and $\delta w=w_0-\bar w$. Define the exact vector
$$
 \begin{split}
 \Delta R={}&
 (D^2+\eta^2K\partial_\phi^2-T_0D+V_0)\delta w
        -5C(\bar G_r,0)^t+\Delta V_0\,\bar w
        +i\epsilon\vartheta Q\mathcal K w_0 .
 \end{split}
 \tag{G.30}
$$
It follows from (G.25)--(G.29) that
$\mu\mathcal L_0w_0=\kappa^2V_{\rm rad}(\bar T)\bar w+\Delta R$.
Since $M_0^{-1}w_0=e_1$, the whole normalized forcing satisfies
$$
 \boxed{\quad
 f^V=
 [V_j(T)-V_{\rm rad}(\bar T)]e_1
 -\mu^{-1}M_0^{-1}
       \{\Delta R+V_{\rm rad}(\bar T)[\kappa^2\bar w-\mu w_0]\}.
 \quad}
 \tag{G.31}
$$
This is the same $(f_b+V_j,f_a)^t$ as in (F.12), on the entire common domain. The last difference can be written
$(\kappa^2-\mu)\bar w-\mu\delta w$.
The large common radial term has cancelled before taking a norm. The matrices, the mode label and the original physical gauge have not been changed.

## 7. The finite-frequency term away from the root

Use the exact rational-frequency functions from the common radial reference. With $z=j^{-2}$ write
$$
 D_{uu}=zU(z),\qquad D_{vv}=zW(z),\qquad
 a_j=\eta+z\alpha(z),
$$
$$
 Q_1(z)=-2bU(z)+2bK W(z)
          +\frac{\partial_r(\alpha/\eta)}{1+z\alpha/\eta}.
$$
The full logarithmic coefficient is
$q_j=q_{\rm rad}+zQ_1(z)$. At the same radial-reference point,
$$
 \boxed{\quad
 V_j(\bar T)-V_{\rm rad}(\bar T)
 =\kappa^{-2}\left\{
 \frac z2(Q_1)_r-\frac z2q_{\rm rad}Q_1
 -\frac{z^2}{4}Q_1^2-16K(2\eta\alpha+z\alpha^2)\right\}.
 \quad}
 \tag{G.32}
$$
Indeed $n^2=16/z$ and
$n^2K(a_j^2-\eta^2)=16K(2\eta\alpha+z\alpha^2)$.
All derivatives are at fixed $z$ and use the original $r$ orientation.

In particular, away from $K=0$ the $z=0$ potential generally differs from $V_{\rm rad}$ by
$-32K\eta\alpha(0)/\kappa^2$. The root formula (F.22) has a factor $z$ because this curvature term vanishes there; that factor cannot be extended to a whole radial piece.

For the actual nonradial evaluation, use the exact split
$$
 \begin{split}
 V_j(T)-V_{\rm rad}(\bar T)
   ={}&[V_j(T)-V_j(\bar T)]\\
     &+[V_j(\bar T)-V_{\rm rad}(\bar T)] .
 \end{split}
 \tag{G.33}
$$
If the segment between $T$ and $\bar T$ lies in the paid common potential disk, the first bracket is bounded by
$\sup|V_{j,T}|\,|T-\bar T|$. The second is the signed expression (G.32). The segment inclusion is a domain condition, not a consequence of the equality of two root values.

## 8. A finite whole-domain budget and its exact remaining inputs

All norms in this section are holomorphic suprema on one declared common product domain. They are not joint Wiener coefficient norms. Suppose that the same domain has the actual gaps of $\mu,M_0,\kappa,\bar A,1+z\alpha/\eta$ and a bound for the same-branch divided powers below.

For $r_A=A/\bar A-1$, the complete differences can be evaluated as
$$
 \begin{split}
 \delta w_1&=\bar G\{(1+r_A)^{1/6}(x^2-Ty^2)-1\},\\
 \delta w_2&=-2i\epsilon\bar G(1+r_A)^{1/6}xy,\\
 \mu-\kappa^2&=\kappa^2\{(1+r_A)^{-2/3}(x^2+Ty^2)-1\},\\
 T-\bar T&=\bar T\{(1+r_A)^{2/3}-1\}.
 \end{split}
 \tag{G.34}
$$
These are differences of analytic functions, not differences of interval upper endpoints. For example, when $|r_A|<1$, the exact identity
$(1+r_A)^a-1=a r_A\int_0^1(1+s r_A)^{a-1}\,\mathrm ds$
retains the small factor. Derivatives are taken in the displayed expression before bounding. The angular mean in $\mathcal E$ remains complete and does not acquire a false angular derivative.

Let $d_0,d_D,d_{DD},d_{\phi\phi}$ bound respectively
$\delta w,D\delta w,D^2\delta w,\partial_\phi^2\delta w$.
Let $\delta_\mu$ bound the third difference in (G.34), and let
$\delta_T$ bound the last. Then the following direct bound is sufficient:
$$
 \begin{split}
 B_{\Delta R}={}&d_{DD}+\|\eta^2K\|d_{\phi\phi}
                  +\|T_0\|d_D+\|V_0\|d_0\\
 &+5\|C\|\|\bar G_r\|+\|\Delta V_0\|\|\bar G\|
                   +\|\vartheta Q\mathcal K w_0\|,\\
 \|f^V\|\le{}&
 \|V_{j,T}\|\delta_T+\|V_j(\bar T)-V_{\rm rad}(\bar T)\|\\
 &+\|\mu^{-1}\|\|M_0^{-1}\|
   \{B_{\Delta R}+\|V_{\rm rad}\|
                    [\delta_\mu\|\bar G\|+\|\mu\|d_0]\}.
 \end{split}
 \tag{G.35}
$$
In (G.35), $\Delta V_0$ is evaluated by (G.26), the potential difference by (G.32), and the differences in (G.34) by complete signed formulas. None is formed by subtracting saved norm bounds. Componentwise versions can be kept separately to preserve the smaller second forcing component.

The inputs are the original finite background and its real-or-complex radial jets, the same root anchor and full repaired mean, the accepted actual fold and leading coefficients, and the accepted rational-frequency potential with its exact image. The displayed second derivatives do not call for a new target, FFT, repair or higher intrinsic solve. They do require actual whole-domain bounds for the differences and reciprocals. A previously accepted Taylor coefficient is read exactly; it is not recomputed merely to obtain a new tail bound.

Use the original same branch $Q=a_\infty A^{-1/3}$ and root anchor $X(0,\phi)=\phi$, so $x(0,\phi)=1$ and $A(0,\phi)=\bar A(0)=a_\infty(0)$. A useful radial-difference identity, if its actual complex characteristic paths stay inside the declared domain, is
$$
 2\rho(\partial_\rho+d\partial_\phi)(A-\bar A)
       +3(A-\bar A)=3a_\infty(x-1),\qquad
 (A-\bar A)|_{\rho=0}=0 .
 \tag{G.36}
$$
It follows directly by inserting $T=-\rho A^{2/3}$ in (G.2). Along those paths its regular integrating-factor solution has kernel $(3/2)\sqrt s$. This can bound $A-\bar A$ from the genuine $x-1$, with all path and strip losses paid explicitly. It is not a license to use a real-circle bound along an unproved complex path.

To convert a new whole supremum into the full Taylor/Fourier tail, keep a strictly larger radial disk and a strictly wider angular strip. The double Cauchy sum is exactly T.23--T.25 of [the whole-piece Taylor theorem](R133-supplement-whole-root-piece-signed-reference-potential-and-first-correction-Taylor.md), including both Fourier signs and the constant coefficient. A supremum of the Wiener norm at each radial point is not silently exchanged with a sum of radial suprema of individual coefficients.

The same actual forced-transport formula may then bound $w_1^V$ from this new $f^V$, with its root value $(0,f_b^V(0,X))$ and its actual paths. At later physical pieces every inherited nonzero entry and scalar integration constant remains. The known identity
$w_1^V-w_1=(Tb_0,a_0)^t\mathcal B_j(T)$
does not allow an old separate upper bound for $w_1$ to be subtracted from a new one.

Existing potential/image and fold receipts can be consumed to check a proposed larger inner disk, but such an enlargement is a new scalar gate. In particular the factor $1/2$ used to choose an earlier image-safe radius is not an obstruction theorem, nor can it be removed without checking the actual fold image against the entire common potential domain. No enlarged radius is claimed here.

This supplies a concrete finite recipe for a new whole-domain cancellation budget. A public consumer must report its actual domain, all nonzero gaps, complete finite coefficients and tail convention, both signs and the fixed intrinsic parameter. Only the small final conclusions and reproducibility metadata are retained. Even after that consumer succeeds, (G.15), the complete positive graph, all physical/reference seams, the independent even mean, the low/high feedback and the numerical strong-return threshold remain separate tasks.

