# R133 supplement: exact-fold source envelopes with complete old-circle and prefix reuse

2026-11-14, root. **Proved algebraic evaluation contract; new numerical bounds remain pending public Actions.**

This supplements [the exact fold cancellation](R133-supplement-exact-fold-matrix-cancellation-and-leading-inverse-defect.md), (C.1)--(C.15). It changes only the bounds on the exact same $h,g_d,q_v$ entering the completed old-circle source calculation. It preserves the original physical parameter $\eta_0$, repaired M32 centre, complete direction disk and six real radial windows. All original seams, means, primitive remainders and two Airy components remain.

The previously successful radial-reference profiles, leading amplitude tensors, complete Fourier factor, and $1328$ original moment and directed matrix rows are immutable inputs. No target, characteristic, amplitude, matrix or Airy-profile solve is repeated.

## 1. The only new scalar jets

On one of the six previously paid real radial windows, put $R$ equal to its radius plus the complete uncertain-root bracket width. The exact closed leading scalar is
$$
 G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}E_G,\qquad
 (\log E_G)_r=-2\beta\langle u^2+Kv^2\rangle .
 \tag{N.1}
$$
The last factor and $k$ are radial. All angular suprema below use the already paid old-angle strip $3/64$.

Let $A_->0$, $k_->0$, $G_+$ be the original complete root bounds, and let $A_{pq}$ bound $|\partial_r^p\partial_\phi^q A|$. Let $k_1$ bound $|k_r|$ and $L_E$ bound $|(\log E_G)_r|$. These quantities are retained in the original complete seam native, in its refined radius cases; $G_+$ is retained in the original root case. Set
$$
 L_r=\frac{A_{10}}{6A_-}+\frac{k_1}{4k_-}+L_E,\qquad
 L_\phi=\frac{A_{01}}{6A_-},
$$
$$
 L_{r\phi}=\frac16\left(\frac{A_{11}}{A_-}
                +\frac{A_{10}A_{01}}{A_-^2}\right),\qquad
 L_{\phi\phi}=\frac16\left(\frac{A_{02}}{A_-}
                +\frac{A_{01}^2}{A_-^2}\right).
$$
Then
$$
 |G_r|\le G_+L_r,\quad |G_\phi|\le G_+L_\phi,\quad
 |G_{r\phi}|\le G_+(L_{r\phi}+L_rL_\phi),\quad
 |G_{\phi\phi}|\le G_+(L_{\phi\phi}+L_\phi^2).
 \tag{N.2}
$$
These follow by differentiating (N.1). In particular no derivative of a value-only error enclosure, no new intrinsic fourth derivative, and no auxiliary complex extension is used. The original complete mean in $L_E$ is retained.

Let $a_+$ be the original bound for the radial characteristic coefficient $a=\eta\sqrt{k}$ and put $Q=aA^{-1/3}$. Complete angular bounds are
$$
 Q_0=a_+A_-^{-1/3},\qquad Q_1=Q_0A_{01}/(3A_-),
$$
$$
 Q_2=Q_0\left\{A_{02}/(3A_-)+4A_{01}^2/(9A_-^2)\right\}.
 \tag{N.3}
$$
The exact derivatives of $T=-\rho A^{2/3}$ yield
$$
 T_0=R A_+^{2/3},\quad
 T_1=\tfrac23R A_-^{-1/3}A_{01},\quad
 T_2=\tfrac23R\{A_-^{-1/3}A_{02}
                      +\tfrac13A_-^{-4/3}A_{01}^2\}.
 \tag{N.4}
$$
The already paid variational fields give
$|X_\phi|\le x_0=C_1$ and $|X_{\phi\phi}|\le x_1=RC_2$.
Use $y_0=T_1,y_1=T_2$ and
$$
 B_0=x_0^2+T_0y_0^2,\qquad
 B_1=2x_0x_1+T_1y_0^2+2T_0y_0y_1 .
 \tag{N.5}
$$
Here $B_0,B_1$ are positive bounds for $B=X_\phi^2-TT_\phi^2$ and $B_\phi$, not a redefinition of that signed expression.

## 2. Exact cancellation before taking source bounds

Write $D=\partial_r-d\partial_\phi$ and let $D_j$ bound $|\partial_\phi^j d|$ on the actual closed coefficient row. For
$Z=DG+2Gd_\phi$, its exact angular derivative is
$$
 Z_\phi=G_{r\phi}+d_\phi G_\phi-dG_{\phi\phi}+2Gd_{\phi\phi}.
$$
Thus
$$
 Z_0=G_r^++D_0G_\phi^++2G_+D_1,\qquad
 Z_1=G_{r\phi}^++D_1G_\phi^++D_0G_{\phi\phi}^++2G_+D_2 .
 \tag{N.6}
$$
The exact two components already established in (C.10) are
$$
 (g_d)_a=ZB+2QTG_\phi X_\phi T_\phi ,
$$
$$
 (g_d)_b=i\epsilon\left\{-2ZX_\phi T_\phi+
       \frac{QGA_\phi}{2A}B+QG(T_\phi)^3\right\}.
 \tag{N.7}
$$
Apply the ordinary product rule to (N.7) through angular order one, using (N.2)--(N.6). The logarithmic factor has bounds
$$
 |A_\phi/A|\le A_{01}/A_-,\qquad
 |\partial_\phi(A_\phi/A)|\le A_{02}/A_-+A_{01}^2/A_-^2.
$$
All signs may be discarded only after the exact cancellation (N.7). There is no division by $T$ at the root.

For the saved complete leading vector $w_0$ define $P=QK(T)$, where
$K(T)=\left(\begin{smallmatrix}0&T\\1&0\end{smallmatrix}\right)$.
Its angular jets through order two are bounded entrywise by
$$
 P_0=\begin{pmatrix}0&Q_0T_0\\Q_0&0\end{pmatrix},\quad
 P_1=\begin{pmatrix}0&Q_1T_0+Q_0T_1\\Q_1&0\end{pmatrix},
$$
$$
 P_2=\begin{pmatrix}0&Q_2T_0+2Q_1T_1+Q_0T_2\\Q_2&0\end{pmatrix}.
 \tag{N.8}
$$
The exact identities
$$
 h=-i\epsilon\,\eta^{-1}Pw_0,\qquad
 y=-i\epsilon\,vPw_0,\qquad
 q_v=v g_d+i\epsilon v_\phi Pw_0
 \tag{N.9}
$$
pay complete $h,y$ jets through order two and $q_v$ jets through order one by finite Leibniz sums. The old row's positive $\eta_-$ pays $\eta^{-1}$; $\eta$ is radial, so no angular derivative is missing. The full $v$, including its independent even mean, is used throughout.

## 3. The unchanged complete old-circle source maps

Use exactly the completed two-component profile functional $\mathcal A$ and inverse-matrix jets from the original analytic/radial-reference source consumer. In particular its real composition factor, central/negative/positive Airy estimates and complete infinite Fourier factor are copied from the successful native. For a vector amplitude jet $z$, define
$$
 \mathfrak D z=\partial_\phi(H^{-1}z),\quad
 \mathcal B(z)=\mathcal A(H^{-1}z)+\mathcal A(\mathfrak D z),\quad
 \mathcal M_0(z)=\mathcal A(\mathfrak D z),\quad
 \mathcal M_1(z)=\mathcal A(\mathfrak D^2z).
$$
The six changed complete nonlocal envelopes are
$$
 C_{SQ}\mathcal B(h),\quad C_{RQJ}\mathcal B(g_d),\quad
 C_{RQJL}\mathcal B(h),\quad C_{\rm primitive}\mathcal B(q_v),
$$
$$
 m_{rQ}\mathcal M_0(h),\qquad c_B V_1\mathcal M_0(y).
 \tag{N.10}
$$
Their ordered matrix coefficients remain the original directed whole-operator bounds. The other three complete envelopes, $SV$, raw $D$ and $V_0$, are copied directly from the original row. In particular the original raw-$D$ estimate
$\mathcal M_1(H_Dw_0)+\mathcal M_0(Dw_0)$ is not silently removed or reinterpreted by (N.7).

The exact full even-mean source is bounded by the same formula
$$
 C_{\rm mean}\{\mathcal M_0(uh)
       +C_{uJ}\mathcal B(g_d)+C_{uJL}\mathcal B(h)
       +C_{uJB}\mathcal B(w_0)
       +|K|\mathcal M_0(v_{\ne0}w_0)\}.
 \tag{N.11}
$$
Only the last displayed term uses $v_{\ne0}$, exactly as in the original mean equation. It does not remove the mean from (N.9), (N.10), or any source port.

For each complete individual expression, either its new bound or its previously completed bound may be used, and the minimum of the two remains a bound. Thus a consumer may take minima separately in the six matching expressions (N.10), and may take the minimum of the two complete bounds for (N.11). It must not match only fragments with different domains or discard cross terms.

## 4. Reusing positive split integrals without recomputing old weights

Each original nonzero row saves a complete radial weight $W$ and envelopes $F_{\rm old},M_{\rm old}$. It also saves the positive collar/body upper integrals
$J_{\rm old}^\ell\ge W_\ell(F_{\rm old}^2+M_{\rm old}^2)$.
Let $N_->0$ be a directed lower bound for
$F_{\rm old}^2+M_{\rm old}^2$ obtained from those saved envelope records. For new complete envelopes $F,M$,
$$
 W_\ell(F^2+M^2)
 \le \frac{J_{\rm old}^\ell}{N_-}(F^2+M^2).
 \tag{N.12}
$$
The inequality follows by first dividing the old upper integral by a positive lower bound for its old squared envelope. It does not treat a bound on an envelope as a lower bound for the true source. $N_-$ is only a lower bound for the previously used numerical upper envelope.

The complete unsplit row uses the saved upper bound for $W$ directly. Exact zero radial pieces stay exact zero. New squared source integrals and the two positive split integrals are accumulated with the complete old partition and true uncertain-root convention. The previously certified negative Cauchy source-to-primitive gain is copied unchanged.

## 5. Scientific execution and remaining obligations

The new consumer must verify original root/seam/moment/radial-reference native hashes, exact real parameter radius, all six domains, complete row identities and the actual zero-return receipts. It evaluates only the six new scalar-jet tables and the new $h,g_d,q_v$ envelopes/integrals. It saves each completed case and every accepted row prefix. A resume must match source, manifest, runtime and all original native identities exactly.

This refinement is independent of the separate auxiliary complex-root extension: no larger complex domain is claimed here. It does not pay $L_0w_1$, the positive-source-to-root conversion, a complete strong-return norm, the numerical cutoff-$97$ inverse, or a true PDE branch. Original seam terms and all other source budgets remain separate obligations, with their completed evidence retained.
