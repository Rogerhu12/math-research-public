# Exact inverse leading-transport column and five complete density-zero sources

2026-11-15.

**Analytic contract; new numerical comparisons await public Actions.** The leading transport and the genuine inverse can be multiplied before taking norms. The resulting principal column has no inverse denominator and has no separate c_T*y term in its second component. The complete frequency-dependent correction and all output means remain. This note supplies the exact identity, a finite derivative recipe, and the five unchanged source types to which it applies.

The primary sources are [F, exact leading-matrix factorization](R133-supplement-exact-leading-matrix-factorization-of-complete-transport-source.md), [G, complete factored source budget](R133-supplement-complete-scalar-budget-for-factored-transport-and-companion-sources.md), [the original ordered source identity](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), [C.2/C.5, the positive column functional](R133-supplement-positive-linear-reuse-and-complete-genuine-negative-sources.md), and [HP, the exact normalized p columns](R133-supplement-exact-normalized-p-columns-and-complete-h-source-ledger.md). The already successful SV, AJ, RV and DG outputs are read only. The new consumer also requires the successful HP small conclusion; it must not reevaluate HP to manufacture that input.

## 1. Fixed physical object, complete matrices and original means

Keep piece2549, the exact negative support and uncertain-root band, the fixed intrinsic parameter eta_0, both genuine columns and both carrier signs. Write
$$
 s=i\epsilon,\quad \epsilon\in\{-1,1\},\quad
 n=4|j|\ge388,\quad q=n^{-2},\quad q_*=388^{-2},
$$
$$
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\quad
 x=X_\phi,\quad y=T_\phi,\quad
 \zeta=y/T,\quad B_+=x^2+Ty^2,\quad
 W=QG,\quad \Delta=B_+-qVy^2 .
 \tag{BG.1}
$$
The symbol K in (BG.1) is the canonical matrix. The potential V is the full V_j(T) on its accepted domain. The quotient zeta has the original analytic extension
$\zeta=(2/3)A_\phi/A$; no division by a small pointwise T is made.

The principal and genuine matrices and inverses are
$$
 H_0=sxI+yK,\qquad H_V=H_0-qVyE_{12},
$$
$$
 B_0=H_0^{-1}
   =B_+^{-1}\begin{pmatrix}-sx&Ty\\y&-sx\end{pmatrix},
 \qquad
 B_V=H_V^{-1}
   =\Delta^{-1}\begin{pmatrix}-sx&(T-qV)y\\y&-sx\end{pmatrix}.
 \tag{BG.2}
$$
The already proved positive B_+ gap and physical-label Delta gap are retained. The latter is uniform on its original angle strip for each physical n. It is not an inverse theorem for an independent complex frequency.

The exact leading column is
$$
 w_0=G(x^2-Ty^2,-2sxy)^t.
$$
Let $D=\partial_r-d\partial_\phi$, and use the same complete transport and companion:
$$
 \mathcal G_0w=Dw+s\partial_\phi(QKw),\qquad
 p_0=-sQKw_0-qR_0,\qquad
 g_0=\mathcal G_0w_0+q\partial_\phi R_0,
$$
$$
 R_0=-\frac{WV B_+}{\Delta}(xy,sy^2)^t .
 \tag{BG.3}
$$
Thus $g_0=Dw_0-\partial_\phi p_0$. The exact radial gauge, full G scalar, amplitude zero mode and independent physical even mean all remain.

## 2. The principal inverse cancellation

Put $c=c_T$, $\xi=\Xi=c_X/T$. These are the regular coefficients in F and G. The exact previously proved leading transport is
$$
 \mathcal G_0w_0
  =-\frac{WB_+}{2}
     (cx+Ty\xi,\ s(x\xi-cy-\zeta))^t.
 \tag{BG.4}
$$
Define $t=B_0\mathcal G_0w_0$. Multiplication in the actual row order gives
$$
 \boxed{\quad
 t=\frac W2
       \binom{s(cB_++y^2)}{x\zeta-B_+\xi}.
 \quad}                                                           \tag{BG.5}
$$
To verify the first row, set $d=cx+Ty\xi$ and
$\ell=x\xi-cy-\zeta$. Then
$$
 xd-Ty\ell=cB_++Ty\zeta=cB_++y^2 .
$$
For the second row,
$$
 yd+x\ell=B_+\xi-x\zeta .
$$
The factor B_+ in (BG.4) cancels the principal inverse denominator. This cancellation occurs between signed analytic expressions before any absolute value. It is not subtraction of numerical upper bounds.

In particular the complete second component in (BG.5) has only x*zeta and B_+*xi. Its root zero is kept, and the c*y terms have cancelled. The nonzero angular mean and radial part of the first component are not removed.

## 3. The full frequency-dependent column

The exact resolvent identity, in the displayed order, is
$$
 B_V-B_0
   =B_V(H_0-H_V)B_0
   =qVy\,B_Ve_1e_2^tB_0 .
 \tag{BG.6}
$$
Consequently the full normalized transport column is
$$
 \boxed{\quad
 Z_g:=B_Vg_0
   =t+q\left\{
       \frac{Vy}{\Delta}\binom{-sx}{y}\,t_b
                  +B_V\partial_\phi R_0
          \right\}.
 \quad}                                                           \tag{BG.7}
$$
Here t_b is the complete second component of (BG.5). Both terms inside braces are retained. In particular B_V is not commuted through the angular derivative of R_0, and the potential inside R_0 is differentiated as part of that complete analytic function.

The q outside the braces is the actual input n^(-2). Any q_* used to bound the entries of B_V pays a distinct q in those entries. Differentiation is at fixed physical input label, so it creates no derivative of q.

## 4. Saved inputs and their precise domains

The common cover is
$$
 I_-=\left[\frac{2147184947341121}{9007199254740992},
                 \frac{2383968743003}{10^{13}}\right],
 \qquad h=\frac{125978014066294748203}
                   {10995116277760000000000000}.
 \tag{BG.8}
$$
Retain the complete original root bracket, the same six source-row intersections and the original true-dr squared-envelope weight. The fold radius and strip are
$R_G=3/8000$, $S_G=3/128$. The genuine inverse product has radius
$1/20000>h$ and strip $S_B=1/64<S_G$.

Read the following successful inputs with exact source, manifest, run, bytes and hashes:

- SV supplies x and y derivative majorants through order three, zeta through order two, the complete potential modulus M_V and the strict physical-label determinant lower bound d_Delta.
- AJ supplies the complete c_T and Xi real-angle derivative majorants through order three, the original positive B_+ gap, and the **full-S_G holomorphic Xi modulus** M_Xi.
- RV supplies the saved whole negative T modulus T_h. Its producer identifies it with the original full-S_G fold expression, so this is not a supremum inferred from a narrower image strip.
- HP supplies W derivative majorants through order three, its saved complete B_+ modulus, and both components of Z_p=B_V p_0 through order three.
- C and D supply the same eighteen positive coefficients, the complete directed words, all original source rows and the saved true-dr weight.
- The immediate accepted ledger is the successful HP ledger after the successful S1, ER and SV updates.

The zeroth x,y,zeta,W and B_+ moduli just listed are available on their original full holomorphic fold strip. Their higher angular derivative arrays are real-circle derivative bounds; they are not promoted to positive-width derivative suprema. The AJ real Xi zeroth bound is also not substituted for M_Xi in a holomorphic product.

The only additional derivative of a previously bounded fold quantity needed here is
$$
       \zeta^{[3]}_{\rm new}=3!\,\zeta^{[0]}/S_G^3 .
 \tag{BG.9}
$$
It follows by Cauchy from the accepted full-strip zeta modulus. It does not recompute a fold coefficient, restriction or finite Taylor sum. All parameter products and physical-label interpretations remain as in the original successful receipts.

## 5. Complete principal real-angle jets

For derivative majorants use the full binomial product
$$
 (U*V)_k=\sum_{\ell=0}^k
                   \binom{k}{\ell}U_\ell V_{k-\ell}.
 \tag{BG.10}
$$
Use the saved W_k, x_k, y_k, c_k and xi_k for k through three, together with (BG.9). Set $T_0=T_h$ and $T_k=y_{k-1}$ for k=1,2,3.

The zeroth B_+ modulus is read from HP. For k=1,2,3, bound the exact derivative of x^2+Ty^2 by the complete products in (BG.10). Denote the resulting four majorants by P_k. These are complete bounds for B_+, not positive lower bounds.

The principal component jets from (BG.5) may then be bounded by
$$
 t_{a,k}^+
   =\frac12\,[\,W*(c*P+y*y)\,]_k,\qquad
 t_{b,k}^+
   =\frac12\,[\,W*(x*\zeta+P*\xi)\,]_k,\qquad0\le k\le3 .
 \tag{BG.11}
$$
The plus in the second bound is the triangle inequality after the signed cancellation in (BG.5). The factors s have modulus one and preserve both carrier estimates. The complete zero-order c, xi and W are retained.

## 6. Holomorphic moduli for both correction terms

All quantities in this section are moduli on the full S_B strip, at a fixed physical input n. Write $P_0$ for the saved HP holomorphic B_+ modulus, and set
$$
 T_b^+=\frac{W_0}{2}(x_0\zeta_0+P_0M_\Xi).
 \tag{BG.12}
$$
This uses the accepted holomorphic M_Xi, not the sharper real-circle Xi value.

For the first correction inside braces in (BG.7), valid component moduli are
$$
 C_a=\frac{M_Vy_0x_0}{d_\Delta}\,T_b^+,\qquad
 C_b=\frac{M_Vy_0^2}{d_\Delta}\,T_b^+.
 \tag{BG.13}
$$
For the R_0 vector and the B_V entries use
$$
 U=\frac{W_0M_VP_0}{d_\Delta}(x_0y_0,y_0^2)^t,
$$
$$
 M_B=\frac1{d_\Delta}
       \begin{pmatrix}
         x_0&(T_h+q_*M_V)y_0\\
         y_0&x_0
       \end{pmatrix}.
 \tag{BG.14}
$$
These are complete componentwise bounds on analytic functions on S_B. They are not a matrix with entries chosen from incompatible operator norms.

For k=0,1,2,3, Cauchy and the full Leibniz rule give
$$
 \left|\partial_\phi^k(B_V\partial_\phi R_0)_i\right|
   \le\frac{(k+2)!}{2S_B^{k+1}}
                           \sum_{j=1}^2(M_B)_{ij}U_j .
 \tag{BG.15}
$$
Indeed the term with ell derivatives on B_V has coefficient
$$
 \binom{k}{\ell}\ell!(k-\ell+1)!
                  =k!(k-\ell+1).
$$
Summing over ell=0,...,k yields (k+2)!/2. The sum over the two matrix entries remains separately in (BG.15). This estimate includes all derivatives of the potential, Delta and the fold factors through their complete holomorphic products; no derivative of an interval error is taken.

Combining (BG.7), (BG.11), (BG.13) and (BG.15) gives the complete real-angle bounds
$$
 Z_{g,i}^{[k]}
   =t_{i,k}^+
     +q_*\left\{\frac{k!C_i}{S_B^k}
         +\frac{(k+2)!}{2S_B^{k+1}}
                       \sum_{j=1}^2(M_B)_{ij}U_j\right\},
 \qquad0\le k\le3 .
 \tag{BG.16}
$$
The one exterior q_* is included exactly once. There is no further n factor in the density-zero operator recipe. The principal part does not receive the coarse whole-correction Cauchy charge.

## 7. Full density-zero means and the two companions

Let $\mathcal A$ be the original C.2/C.5 positive functional, summing all three branches and six component derivative entries in their accepted order. For a complete column Z with four derivative bounds, abbreviate
$$
 \mathcal A_0(Z)=\mathcal A(Z^{[0]},Z^{[1]},Z^{[2]}),\qquad
 \mathcal A_1(Z)=\mathcal A(Z^{[1]},Z^{[2]},Z^{[3]}).
$$
Each call retains both components, both genuine columns, both carrier signs and the output mean. By the original G.16--G.17 density identity,
$$
 \Gamma_{g,0}=\mathcal A_0(Z_g)+\mathcal A_1(Z_g),
 \qquad M_{g,0}=\mathcal A_1(Z_g).
 \tag{BG.17}
$$
No B_V is applied a second time.

For an original source row let v be its complete scalar physical background, including its mean, and let v_k be the saved angular majorants through order four. Read the successful HP column Z_p=B_Vp_0. The exact companions are
$$
 B_V(vg_0-v_\phi p_0)=vZ_g-v_\phi Z_p,\qquad
 B_V(vp_0)=vZ_p.
 \tag{BG.18}
$$
The scalar v commutes with the pointwise B_V at a fixed input label. No Fourier operator is moved past a relabelling of the input.

For k=0,1,2,3, use the complete row-dependent majorants
$$
 Q_{i,k}
 =\sum_{\ell=0}^k\binom{k}{\ell}
   \bigl(v_\ell Z_{g,i}^{[k-\ell]}
               +v_{\ell+1}Z_{p,i}^{[k-\ell]}\bigr),
$$
$$
 Y_{i,k}
 =\sum_{\ell=0}^k\binom{k}{\ell}
                      v_\ell Z_{p,i}^{[k-\ell]} .
 \tag{BG.19}
$$
Then the two needed complete functionals are
$$
 \Gamma_{q,0}=\mathcal A_0(Q)+\mathcal A_1(Q),\qquad
 M_{y,0}=\mathcal A_1(Y).
 \tag{BG.20}
$$
The exact q amplitude is v*g_0-v_phi*p_0, as in the existing compressed source convention. It is not D(v*w_0); no unproved Dv term or cancellation is inserted.

## 8. Exactly five complete source terms

Read the complete directed whole words K_RQJ, K_primitive and K_uJ on their same accepted radius and both declared source windows. For a complete old row, let J_out be its outer scalar J, c_B its complete mean prefactor, m_T its m0_T0 bound and e its independent-mean prefactor. The only new coefficients are
$$
 \begin{array}{ll}
 \mathrm{density0\_complete\_RQ\_J\_g}:&
                   J_{\rm out}K_{RQJ}\Gamma_{g,0},\\
 \mathrm{density0\_complete\_primitive}:&
                   J_{\rm out}K_{\rm primitive}\Gamma_{q,0},\\
 \mathrm{density0\_old\_mean\_transported}:&
                   J_{\rm out}(c_Bv_1v_0/4+m_T)M_{g,0},\\
 \mathrm{density0\_old\_mean\_vphi}:&
                   J_{\rm out}c_Bv_1M_{y,0},\\
 \mathrm{density0\_complete\_uJ\_g}:&
                   eK_{uJ}\Gamma_{g,0}.
 \end{array}
 \tag{BG.21}
$$
The last line is the independent physical even-mean row and has no outer scalar J. The first four are the original first-source row. The whole words already include their internal factors; no additional R, Q, J, u or primitive prefactor is multiplied into those words.

The transported mean in (BG.21) retains both original contributions, including the full radial mean in T0. No supplied independent mean source is set to zero.

Evaluate (BG.21) on all six original source rows. With the saved squared-envelope radial weight W2, each complete new term is bounded by
$$
       L_{\rm new}=\sqrt{W_2}
                         \max_{\text{six original rows}}C_{\rm row}.
 \tag{BG.22}
$$
The true dr measure, root interval, one-sided uncertain-root band, common abs(rho)^(-1/4) envelope, input H^(-4/3) window and first-output H^(-2/3) window remain unchanged. There is no new radial integration.

For each of the five exact term names, retain the minimum of its prior complete bound and (BG.22). The other twenty-six term balls are copied byte for byte from the successful HP ledger. This preserves all three local terms, all density-one terms, all SV/S1 terms outside the displayed five, and all ten h-source terms paid by HP. Only the nonlocal, first, independent-mean and combined scalar aggregates are recombined. Every minimum is between complete bounds for the same term; no two upper bounds are subtracted.

## 9. Public execution and exact remaining scope

The consumer must freeze the successful HP receipt, its scientific source and manifest before running. It checks the full accepted DG/RV/SV/AJ/C/D identities, original complete rows and words, all old parameter and image products, positive denominators, both physical-label signs, original zero modes, and exact retained term names. All new arithmetic is confined to the new products and derivative comparisons above in the public repository's Actions.

No old fold, inverse, potential, W recurrence, p column, signed finite sum, Taylor/Fourier tail, profile, positive calibration, source-row producer or radial integral is called again. The saved HP W and Z_p arrays and the other accepted conclusions are read unchanged. New intermediate derivative and row arrays remain temporary; only the bounded final scalar conclusions, source/run identities, hashes and complete small ledger may be published.

A smaller five-term volume bound is not yet a source-to-wave estimate, an actual incoming-root comparison, a positive growing-column choice or a strong-return contraction. All physical and reference seams, true jumps, root data, independent boundary charges, complete parameter rows, the two-ended body problem and the actual low/high interface remain as independent obligations.
