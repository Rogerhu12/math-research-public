# R133 supplement: exact waist angular inverse and reduced finite reconstruction

2026-11-16, phase_inverse.

**Proved analytic identity.** At the actual waist, the metric coefficient in the original moving scalarization is exactly zero. The same complete angular inverse therefore reduces to one primitive. This eliminates each of the six inner mean terms and both inner terminal terms in FA.15 separately. It also reduces the finite residual polynomial to its degree-three term. The outer primitive mean, its terminal term, the independent physical mean state, all radial derivatives and the second waist normalizer remain.

This is an independent exact specialization of FA and WEJ. It does not change either earlier contract or any successful numerical record. All new bounds below are symbolic; no new scalar is evaluated here.

## WZR1. The identical metric coefficient and the actual waist

Use the original normalized circle of period $\pi/2$, with
$$
 \Pi f=\langle f\rangle,\qquad P=Id-\Pi,\qquad
 I=\partial_\phi^{-1}P,\qquad \|I\|_{L^2\to L^2}=\frac14.
 \tag{WZR.1}
$$
The physical modes are $4j$, including both signs. The reflected moving class is $u,h_1$ odd and $v,h_2$ even.

N.2 defines
$$
 b=\frac{a_{\rm phys}'}{a_{\rm phys}},\qquad
 m=\langle v\rangle,\qquad \eta=-\gamma m,\qquad
 S=u^2+Kv^2,\qquad d=-bIS.
 \tag{WZR.2}
$$
FA.4 uses precisely this radial $b$ in its $\ell$, $b_{\rm loc}$, $A$ and $B$. WPL explicitly names it $\beta_{\rm metric}=a_{\rm phys}'/a_{\rm phys}$ to distinguish it from unrelated phase and return parameters.

WPL.32--33, using the exact R77 parity, the germ-matching regularity and the original compact perturbation supported away from the waist, proves
$$
 b(0)=0,\qquad K_r(0)=q_r(0)=0.
 \tag{WZR.3}
$$
In particular, N.2 gives $d(0,\phi)=0$ for every angle. Hence all pure angular derivatives of the following actual waist functions vanish:
$$
 b_w=d_w=\ell_w=b_{{\rm loc},w}
   =L_{11,w}=L_{22,w}=0,\qquad
 \ell=-2buv,\quad b_{\rm loc}=b(1-u^2-3Kv^2).
 \tag{WZR.4}
$$
The subscript $w$ means evaluation at $r=0$. These are values of complete functions, not differences of upper bounds. They imply no vanishing of $b_r(0)$, $d_r(0)$, $u_r(0)$, $v_r(0)$ or any radial derivative of the angular operator.

The metric identity itself holds on the original family where WPL applies. The free-waist reconstruction below additionally uses the selected WES free-neighbourhood qualification $-T(0,\phi)>L=1/2000$; this latter qualification is not enlarged to a different parameter family.

## WZR2. The same complete inverse and the surviving physical mean

N.4--5 and FA.4 give, on the complete original angular spaces,
$$
 A_w=\eta_w\partial_\phi,\qquad
 B_w=E_w=0,\qquad C_w=-\eta_w\partial_\phi.
 \tag{WZR.5}
$$
Because the original $\eta_w$ is a nonzero radial scalar, the same complete inverse maps $H^s_{\rm even,0}$ to $H^{s+1}_{\rm odd}$; $A_w$ maps these spaces in the reverse direction. It is exactly
$$
 J_w=\eta_w^{-1}I,\qquad
 A_wJ_w=Id,\quad J_wA_w=Id,\qquad
 \|J_w\|_{H^s\to H^s}=\frac{1}{4|\eta_w|}
 \tag{WZR.6}
$$
for every fixed $s$ on the corresponding nonmean spaces. The identities also hold on the complete nonmean carrier before reflection. This is an infinite-dimensional identity; it uses no Fourier truncation and requires no new Neumann gate.

The remaining mean couplings in N.5 are
$$
 b_{2,w}=-\gamma_wu_{\phi,w},\qquad
 b_{1,w}=\gamma_wK_wv_{\phi,w},\qquad
 J_wb_{2,w}=-\frac{\gamma_w}{\eta_w}u_w=\frac{u_w}{m_w}.
 \tag{WZR.7}
$$
Here $Iu_\phi=u$ follows from the original odd parity. Since $\eta_w=-\gamma_wm_w\ne0$, this identity does not divide by a vanishing mean.

For the actual mean-completed trial, write $f=Ph_2$ and $z_{\rm phys}=\Pi h_2$. Its complete waist state remains
$$
 h_{1,w}=\eta_w^{-1}I f_{r,w}
                     -z_{\rm phys}(0)\frac{u_w}{m_w},
 \qquad h_{2,w}=f_w+z_{\rm phys}(0).
 \tag{WZR.8}
$$
Thus the endpoint vector $(-J_wb_{2,w},1)=(-u_w/m_w,1)$ remains nonzero. For the trial with zero second source, N.7 gives $z_{\rm phys}'(0)=0$, but its value at zero is determined by the full root-to-waist mean equation. An instantaneous zero derivative does not remove that value, its feedback, or either stored density mean.

Likewise the mean functional proportional to $b$ vanishes at the endpoint, but its radial derivative need not. The formulas for $J_r$, $e_r$, $e_\kappa$ and the ordinary mean propagator keep their complete original radial predecessors. In particular one may not radially differentiate (WZR.6) as if it held on a neighbourhood.

## WZR3. Exact finite reconstruction with the extended first amplitude

Fix $n=4|j|\ge N_0=388$, $\epsilon=\operatorname{sgn}j$ and $z_n=n^{-1}$. At the selected free waist, use either free reference column in FA.2, with its original scaled derivative. Put
$$
 W_n=w_0+z_nw_1^{\rm ext},\qquad
 H_\epsilon=i\epsilon X_\phi Id+T_\phi K_T,\qquad
 M_\epsilon=i\epsilon X_r Id+T_rK_T,\qquad
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix}.
 \tag{WZR.9}
$$
These are evaluated at the actual waist. The formula for $M_\epsilon$ uses $d_w=0$ only after evaluating the original $D=\partial_r-d\partial_\phi$. Both ordinary derivatives $w_{0,r}$ and $w_{1,r}^{\rm ext}$ remain.

The exact gap is
$$
 \det H_\epsilon
    =-(X_\phi^2+TT_\phi^2)
    =-\Phi_{+,\phi}\Phi_{-,\phi}<0.
 \tag{WZR.10}
$$
The same true phase gaps supply its inverse. The extended amplitude includes the complete $\mathcal B K_Tw_0$ contribution and all its derivatives. It need not solve the free transport equation for the finite algebra below. If its coefficients depend on the input label through the genuine potential, every displayed identity holds for that fixed label; uniform derivative bounds are supplied separately. No derivative in $n$ is used.

The original FA.13 specializes exactly to
$$
 \begin{split}
 g_0&=(\eta_wH_\epsilon)^{-1}M_\epsilon w_0,\\
 g_1&=(\eta_wH_\epsilon)^{-1}
       (M_\epsilon w_1^{\rm ext}+w_{0,r}-\eta_w\partial_\phi g_0),\\
 g_2&=(\eta_wH_\epsilon)^{-1}
       (w_{1,r}^{\rm ext}-\eta_w\partial_\phi g_1),\\
 g_3&=-H_\epsilon^{-1}\partial_\phi g_2,\qquad
 G(z_n)=g_0+z_ng_1+z_n^2g_2+z_n^3g_3.
 \end{split}
 \tag{WZR.11}
$$
Consequently the full FA.14 polynomial is
$$
 \begin{split}
 \mathcal R_w(z_n)
 &=z_n^{-1}\eta_wH_\epsilon G+\eta_w\partial_\phi G
                  -z_n^{-1}M_\epsilon W_n-\partial_rW_n\\
 &=z_n^3\eta_w\partial_\phi g_3 .
 \end{split}
 \tag{WZR.12}
$$
Indeed its degrees $-1,0,1,2$ vanish successively by the four displayed definitions. There are no degrees $4,5,6$ because all terms that could generate them in FA.14 contain $b_w$. The degree-three derivative is not set to zero.

## WZR4. Eight separate inner zero terms, with the outer mean retained

Write $m_F=\Pi\mathcal U(F)$ as in FA.15. Every mean may itself be nonzero. The exact multiplying coefficient makes the following complete terms vanish:

| Original inner term | Exact waist reason |
|---|---|
| $-P\ell\,m_G$ | $\ell_w=0$ |
| $2bPv_\phi\,m_{\mathcal I^{[3]}(uG)}$ | $b_w=0$ |
| $2b\,m_GPv_\phi Iu$ | $b_w=0$ |
| $-Pb_{\rm loc}\,m_W$ | $b_{{\rm loc},w}=0$ |
| $2bKPv_\phi\,m_{\mathcal I^{[3]}(vW)}$ | $b_w=0$ |
| $2bK\,m_WPv_\phi Iv$ | $b_w=0$ |
| $2bz_n^3Pv_\phi I\mathcal U(\partial_\phi\mathcal I_2(uG))$ | $b_w=0$ |
| $2bKz_n^3Pv_\phi I\mathcal U(\partial_\phi\mathcal I_2(vW))$ | $b_w=0$ |

Thus FA.15 gives the complete first-row residual
$$
 \mathcal E_w
   =\eta_wz_n^3P\mathcal U(\partial_\phi g_3),\qquad
 h_{1,w}^{\,0}-P\mathcal U(G)
   =-z_n^3I\mathcal U(\partial_\phi g_3),
 \tag{WZR.13}
$$
where $h_{1,w}^{\,0}=J_w\partial_rP\mathcal U(W_n)$ is the nonmean reconstructed row before the independent physical-mean correction in (WZR.8). The radial derivative of $m_W$ still disappears only under the explicit $P$ in this equation.

There is no corresponding reason to remove the outer primitive's mean or terminal. Set
$$
 \mathscr R_w=n_g(0)T(q_0),\qquad
 V(z_n)=\mathscr R_w\begin{pmatrix}G(z_n)\\W_n\end{pmatrix},\qquad
 \mathcal B(z_n)=\sum_{\ell=0}^2z_n^\ell\mathcal I_\ell V(z_n)
                  =\sum_{k=0}^5z_n^k\mathcal B_k .
 \tag{WZR.14}
$$
The rows in this formula are amplitude rows, exactly as in FA.18. The full radial density factor occurs inside $\mathscr R_w$ once. Matrix entries and their declared entry-sum norms retain both physical rows and both reference components.

The outer identity retains both
$z_n^3I\mathcal U(\partial_\phi\mathcal I_2V)$ and
$\Pi\mathcal U(\mathcal B)$. Their full bounds are the second and third terms below. The independent physical density mean is separately the vector in (WZR.8), not either of these auxiliary mean terms.

## WZR5. A direct complete second-order column bound

Let $P_*,P_1,P_2$ be the same complete real-profile bounds from FA.7 at the actual waist $t_-\le -T\le t_+$. They also cover Bi under the real remainder qualification already fixed by WES. No derivative of an Airy error bound is taken.

Use the complete real finite-mean functional $\mathfrak m_2$ from WEJ.42--43 and the coefficient norm $[\cdot]_{N_0}$. If $R_w$ bounds the actual matrix $\mathscr R_w$ on the physical Euclidean pair, then
$$
 \begin{split}
 C_{\rm rec}^{\,w}
  ={}&\frac{R_wP_*}{16}\|\partial_\phi g_3\|_\infty\\
    &+\frac{P_*}{4}[\partial_\phi\mathcal I_2V]_{N_0}
       +\mathfrak m_2(\mathcal B).
 \end{split}
 \tag{WZR.15}
$$
The first term follows directly from (WZR.13): the two actual primitives each cost $1/4$, while the input power $n^{7/6}$, $z_n^3$ and the complete profile decay $n^{-1/6}$ give $n^{-2}$. Equivalently it is the exact cancellation of the scalar $\eta_w$ in the full residual and the same angular inverse. It is not a subtraction from an earlier positive upper bound.

Retain the full Airy remainder
$$
 \begin{split}
 C_{\rm Airy}^{\,w}
 ={}&P_*\sum_{k=2}^5N_0^{-(k-2)}\|\mathcal B_k\|_\infty
       +P_1\|\mathcal B_1\|_\infty\\
 &+P_2\big(\|\mathcal B_0\|_\infty
                          +N_0^{-1}\|\mathcal B_1\|_\infty\big),\\
 C_{\rm pre}^{\,w}&=C_{\rm rec}^{\,w}+C_{\rm Airy}^{\,w}.
 \end{split}
 \tag{WZR.16}
$$
This is a complete common column bound for the same physical free map with the extended amplitude, after its stated input normalization. The sufficient endpoint derivative demand remains $w_0:C_\phi^6$, $w_{0,r}:C_\phi^5$, $w_1^{\rm ext}:C_\phi^5$, $w_{1,r}^{\rm ext}:C_\phi^4$, together with the full actual phase/matrix predecessors. No yet-unpaid derivative is inferred from this list.

The new WGS geometry and amplitude jets are ordinary derivative supremum/component-sum bounds, after restoring any displayed factorial normalization; they are not Wiener $A_0$ bounds. The finite maps $\mathcal I_\ell$ and $\mathfrak m_2$ use their explicit matrix, derivative and phase-integration formulas with these supremum bounds. The factors $1/4$ in (WZR.15) are used only for the two actual $L^2$ primitives. No $L^\infty$ or Wiener primitive estimate is inferred from a WGS supremum bound.

A future consumer may evaluate (WZR.11)--(WZR.16) directly. It can retain the eight exact zeros with their identity labels and all nonzero outer terms. If another complete bound for this identical map is already available, only complete candidates may be compared.

## WZR6. The four endpoint operators and the remaining equations

The new column constant can enter WEJ.47--55 without changing the exact endpoint maps. In particular:

- The full input scattering matrix $\mathsf S(D^{\rm root}+\mathcal J_\infty)$ keeps its order, original $C_n,\beta_n$ and both reference components.
- The complete second-order first-cancellation term keeps the $c_{B,n}^2$ and first-Airy cross coefficients.
- The second waist normalizer $A_2=P_{J_s}\mathbf Z(0)I^2P_{J_s}$ remains. Its $\mathbf S_r(0)$ and $b_r(0)$ contributions are not zero; the same WT whole remainder is read without subtraction.
- The physical mean endpoint $v_z z_{\rm end}$ remains with the full root-to-waist mean propagator.

Thus the resulting complete $C_{\rm end}$ is still the sum of all four endpoint contributions. The factor $n_g(0)$ in the WT/SW product of WEJ.52 occurs once, independently of its occurrence inside the distinct free-map factor $\mathscr R_w$.

This endpoint identity neither removes any strict ordinary source or true jump nor supplies a finite determinant, incoming inverse or nonlinear solution. The true transported input, the original finite complement, physical mean/amplitude rows, metric-parameter column and independent head/second input retain their original equations.

## WZR7. Immutable primary evidence

The three primary algebra sources (N, FA, WPL) were read in full as text for this specialization. The table also retains the complete WEJ and WES endpoint contracts. No old or new numerical helper was executed.

| Primary object and exact use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| N.2, N.4--9: same metric coefficient, angular operator and independent mean | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| FA.3--4, FA.9, FA.13--23: full finite reconstruction and all means | acfb0cfd9a2598c00a6b29c2db05041d0340cba9 | 27814 | 24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af |
| WPL.32--37: exact metric parity, waist zero and retained second normalizer | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| WEJ.41--55: same complete real-waist and four-endpoint recipe | da9d8461ca406a1c6f4b829a91147a860133567f | 59644 | 6b7644a978915550b5835b3492eda3bffde872b8e92f16c2db6c4538e405be8f |
| WES: selected free-waist qualification and exact old-trial endpoint difference | 02ca30d6e063e9bdfd158d8401361db74e92ce77 | 31293 | 8aa7eb5d210ed73b3e3e2b3c166432292725a603c23dda4d4d9c0a8292d72b00 |

The earlier WEJ and FA numerical targets remain frozen. This text adds a direct same-waist analytic recipe; any later numerical instantiation requires its own complete current input admission and actual successful receipt.
