# Retained radial coefficients and complete density-one transport sources

2026-11-15.

**Proved analytic identities and complete-bound recipe; the new numerical comparison awaits public Actions.** The genuine first correction has already been bounded on the entire negative root piece. This note reuses those fourteen completed amplitude derivatives and retains the radial parts of its transport coefficients when taking angular derivatives. It does not recompute the correction, the fold, the potential, their Taylor coefficients, any source integral, or a completed scalar closure.

The primary inputs are [DG, direct physical transport](R133-supplement-direct-physical-transport-of-genuine-first-correction.md), [RV, the frozen correlated radial local producer](../scripts/fourfold_codazzi_correlated_radial_local_sources.py), [SV, the exact leading inverse column](R133-supplement-exact-leading-inverse-column-and-density-zero-SV-source.md), [HP, the normalized p columns](R133-supplement-exact-normalized-p-columns-and-complete-h-source-ledger.md), [BG, the exact normalized leading transport](R133-supplement-exact-inverse-leading-transport-and-five-density-zero-sources.md), [C.2/C.5, the complete positive column functional](R133-supplement-positive-linear-reuse-and-complete-genuine-negative-sources.md), and [D, the two directed matrix windows](R133-supplement-two-window-directed-word-reuse-for-genuine-sources.md). Each new consumer must bind the actual successful input receipts and their original algorithms. A theorem alone does not authorize replacing a missing successful input by a new execution of its producer.

## 1. Fixed object, physical labels and domains

Retain the original reflected family at fixed intrinsic parameter $\eta_0$, the complete complex $\delta$ square of halfwidth $10^{-8}$, both physical carrier signs and every input label $|j|\ge97$. Write
$$
 n=4|j|\ge388,\qquad s=i\epsilon,\quad \epsilon=\pm1,\qquad
 \chi=n^{-2},\qquad \chi_*=388^{-2},
 \tag{RJ.1}
$$
$$
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 x=X_\phi,\qquad y=T_\phi,\qquad
 \zeta=y/T,\qquad B_+=x^2+Ty^2,\qquad
 \Delta=B_+-\chi V_j(T)y^2 .
 \tag{RJ.2}
$$
Here $K$ is the canonical two-by-two matrix. The scalar potential is the full common-reference $V_j$, including the complete parameter dependence. The quotient $\zeta$ is the already proved analytic extension $(2/3)A_\phi/A$, not a pointwise division by a small $T$.

The exact negative support is
$$
 \left[
 \frac{2147184947341121}{9007199254740992},
 \frac{2383968743003}{10^{13}}
 \right],\qquad
 h=\frac{125978014066294748203}{10995116277760000000000000}.
 \tag{RJ.3}
$$
The same six original coefficient intersections, uncertain-root band and physical $dr$ measure remain. Set
$$
 R_G=\frac3{8000},\qquad S_G=\frac3{128},\qquad
 R_B=\frac1{20000},\qquad S_B=\frac1{64}.
 \tag{RJ.4}
$$
The original fold and its $G^{-1}$ modulus hold on $R_G\times S_G$; the accepted genuine inverse has its physical-label determinant gap on the specified inverse product. Since $h<R_B<R_G$, restriction to the negative interval is legitimate. The successful receipts must retain these exact domains.

All positive-order angular bounds below are **real-circle derivative bounds**, uniform on the complete negative interval and their accepted parameter products. The global analytic columns keep their original complex parameter products; the six original coefficient-row bounds keep their already proved real-family parameter range. No real-row bound is promoted to a complex parameter square. A full-strip zeroth bound may be used on this real circle. A real-circle derivative bound is never promoted to a positive strip. The potential is evaluated through the actual $T(r,\phi)$; no old radial variable is substituted for it.

Let $w=w_1^V=(a,b)^t$ be the same genuine correction as DG and RV:
$$
 w_1^V=w_1+\binom{Tb_0}{a_0}\mathcal B(T).
 \tag{RJ.5}
$$
Read the four angular orders $0,\ldots,3$ and three mixed orders $\partial_r\partial_\phi^k$, $k=0,1,2$, for each component from DG/RV. These are fourteen completed bounds. The original convention $\partial_r=-\partial_\rho$ has already been included in the mixed derivatives. None of them is differentiated numerically or recomputed.

The complete amplitude zero mode, both carrier signs, the original independent even physical mean, physical seam sources and reference jumps remain separate and unchanged.

## 2. Finite derivative calculus

For a scalar function $f$, let $f_k$ denote an upper bound for $|\partial_\phi^k f|$, uniformly on the product in Section 1. For a vector use this convention componentwise. For nonnegative derivative arrays define
$$
 (u\star v)_k=\sum_{\ell=0}^k\binom{k}{\ell}u_\ell v_{k-\ell}.
 \tag{RJ.6}
$$
Repeated products use this full Leibniz convolution. There is no factorial normalization in these arrays. All numerical sums, products, divisions by positive gaps, and final comparisons are rounded outward.

Suppose $|f^{-1}|\le I_0$ and $f_1,\ldots,f_m$ are complete real-circle derivative bounds. Differentiating $f\,f^{-1}=1$ gives the complete recurrence
$$
 I_k=I_0\sum_{\ell=1}^k\binom{k}{\ell}f_\ell I_{k-\ell},
 \qquad 1\le k\le m.
 \tag{RJ.7}
$$
Then $|\partial_\phi^k(f^{-1})|\le I_k$. This uses the already paid zeroth inverse bound; it is not a new nonvanishing assertion and requires no derivative of the parameter label.

## 3. A new quotient bound for Q using completed W and G

The exact scalar is $W=QG$. HP has already computed its complete angular derivatives $W_0,\ldots,W_3$ on the negative piece, retaining its nonzero radial part. SV has already computed $G_0,\ldots,G_3$ there.

Read the original full $G^{-1}$ bound $G_{\rm inv}$ from the natural 4501-byte reference-majorant stage. Its precise definition is the quantity named Gi in the original fold_budget algorithm, which directly bounds the modulus of $G^{-1}$ on $R_G\times S_G$. It is not the full matrix inverse Bi, and these quantities must not be interchanged. The original stage SHA, publication receipt, source, helper, manifest and runtime are all retained.

Apply (RJ.7) to $G$, starting with $I_0=G_{\rm inv}$. Define
$$
 \mathcal Q_0=Q_0^{\rm saved},\qquad
 \mathcal Q_k=(W\star I)_k\quad(1\le k\le3).
 \tag{RJ.8}
$$
The saved $Q_0^{\rm saved}$ is the complete zeroth principal-Q modulus in DG and the original fold. Then
$$
 |\partial_\phi^k Q|\le\mathcal Q_k,\qquad 0\le k\le3.
$$
This is a new reciprocal/product bound using successful scalar outputs. It does not rerun the older unrecorded Q derivative recurrence. The identity $Q=W/G$ keeps the full radial value of $Q$ and every mean.

The exact angular identities also give
$$
 Q_\phi=-\frac12Q\zeta,\qquad
 (QT)_\phi=Q_\phi T+Qy=\frac12Qy.
 \tag{RJ.9}
$$
Consequently a complete new bound for the product $QT$ is
$$
 \mathcal T_0=\mathcal Q_0 T_h,\qquad
 \mathcal T_k=\frac12(\mathcal Q\star Y)_{k-1}
 \quad(1\le k\le3),
 \tag{RJ.10}
$$
where $T_h$ is the saved full negative image bound and $Y_k$ is the saved SV bound for $\partial_\phi^k y$. Formula (RJ.10) uses the signed cancellation in (RJ.9) before absolute values. It does not apply ordinary angular Cauchy to the large radial value of $QT$.

## 4. The potential chain rule and an existing Cauchy budget

Use the original successful potential case with radial radius $1/6000$, complex frequency-square halfwidth $1/9409$, complex $\delta$ square halfwidth $10^{-8}$ and fixed $\eta_0$. Let its full bounds be
$$
 P_0\ge|V_j|,\qquad P_1\ge|V_{j,T}|,\qquad
 P_2\ge|V_{j,TT}|.
$$
Let $I_T$ be the accepted common-reference image radius and $T_h$ the actual negative image. RV has already checked and recorded
$$
 d_T=I_T-T_h>0.
 \tag{RJ.11}
$$
The same closed product must be used. For every actual $T$ in the negative image, a fixed-$j$ complex $T$ disk of radius $d_T$ lies in the complete potential domain. Cauchy therefore gives $|V_{j,TTT}|\le P_2/d_T$ there.

No new computation of $P_2/d_T$ is necessary. In the frozen RV source, the first additional Fuchsian derivative budget was formed by the literal algorithm
$$
 U_3=\operatorname{up}\!\left(\frac{P_2}{7d_T}\right).
 \tag{RJ.12}
$$
It was saved as the first entry of complete_additional_Fuchsian_derivatives_3_4. Reading the upper endpoint of this **budget number** gives
$$
 P_3:=7\,U_3^{\rm upper}\ \ge\ P_2/d_T\ \ge\ |V_{j,TTT}|.
 \tag{RJ.13}
$$
This conclusion uses the exact positive numerical expression in (RJ.12) and its input identity. It is not an inference from an upper bound on the actual function $\mathcal B'''$ to an upper bound on $V'''$. Without the frozen producer identity and the same $P_2,d_T$ product, (RJ.13) is not licensed.

Since $T_\phi=y$, complete real-circle potential jets are
$$
 \mathcal V_0=P_0,\qquad
 \mathcal V_1=P_1Y_0,\qquad
 \mathcal V_2=P_1Y_1+P_2Y_0^2,
$$
$$
 \mathcal V_3=P_1Y_2+3P_2Y_0Y_1+P_3Y_0^3 .
 \tag{RJ.14}
$$
The complete radial potential value remains. All its angular change is charged through the actual coordinate derivatives. These bounds hold for each physical $n$ and all accepted parameters; the potential's larger complex frequency-square domain remains an input but is not transferred to a new inverse.

## 5. Full determinant and rank derivatives

Read $B_+$ through angular order three from the successful BG small conclusion. In particular, its zeroth holomorphic modulus comes from HP, and BG's positive orders are already computed bounds. Do not reproduce these products in a later consumer.

Let $\delta_\Delta>0$ be the accepted SV determinant gap on its physical-label inverse product. It is the same exact stored gap used by HP and BG. A separately rounded RV version need only be checked against its own successful domain and positivity; it must not be required to have identical printed ball radius.

For $k=1,2,3$, put
$$
 D_k=(B_+)_k+
       \chi_*\,(\mathcal V\star Y\star Y)_k.
 \tag{RJ.15}
$$
The signed determinant remains $\Delta=B_+-\chi V_jy^2$. Equation (RJ.15) is its complete derivative majorant, not a change of determinant. Set
$$
 J_0=\delta_\Delta^{-1},\qquad
 J_k=\delta_\Delta^{-1}
       \sum_{\ell=1}^k\binom{k}{\ell}D_\ell J_{k-\ell}.
 \tag{RJ.16}
$$
Thus $J_k$ bounds the angular derivatives of $\Delta^{-1}$. No zeroth determinant gap is estimated by subtracting two upper bounds; the original positive gap is read.

For the genuine correction the exact rank is
$$
 R(w)=\frac{QV_j}{\Delta}
       \binom{-sx}{y}\,(sya+xb).
 \tag{RJ.17}
$$
There is no reaction coefficient $\vartheta$ in this transport rank. The factor $\chi=n^{-2}$ is outside it in both physical source identities below.

Using the saved amplitude arrays and SV coordinate arrays, form
$$
 U=Y\star A+X\star B,\qquad
 F=\mathcal Q\star\mathcal V\star J,
$$
$$
 \mathcal R_a=F\star X\star U,\qquad
 \mathcal R_b=F\star Y\star U,
 \qquad 0\le k\le3 .
 \tag{RJ.18}
$$
Here $A,B$ denote bounds for the two components $a,b$, not the principal matrix or a new leading column. The order in (RJ.17) is fixed: first the row $(sy,x)$ acts on $w$, then the column $(-sx,y)^t$, then the scalar factor. Formula (RJ.18) is the complete absolute majorant of that ordered expression. It preserves both full component means, both signs, the factor $y$ in the second component and every term of the scalar row.

The internal appearances of $\chi_*$ in (RJ.15) and the external $\chi_*$ in (RJ.19) have different exact origins. Neither may be removed or duplicated.

## 6. Direct physical p and g on each original row

The exact identities on the original physical coordinates are
$$
 p(w)=-sQKw-\chi R(w),\qquad
 g(w)=\mathcal G_0w+\chi\partial_\phi R(w),
$$
$$
 \mathcal G_0w=
 \binom{a_r-d\,a_\phi+s\,\partial_\phi(QTb)}
       {b_r-d\,b_\phi+s\,\partial_\phi(Qa)} .
 \tag{RJ.19}
$$
In particular $g=Dw-\partial_\phi p$ with $D=\partial_r-d\partial_\phi$. No fixed-$X$ derivative is substituted for a physical $r$ derivative.

For $k=0,1,2$, a complete new p bound is
$$
 \mathcal P_{a,k}=(\mathcal T\star B)_k+
                      \chi_*\mathcal R_{a,k},
 \qquad
 \mathcal P_{b,k}=(\mathcal Q\star A)_k+
                      \chi_*\mathcal R_{b,k}.
 \tag{RJ.20}
$$
For an original coefficient intersection $I_i$, read the full drift derivative bounds $d_{i,0},d_{i,1},d_{i,2}$ from its saved D array. That array is the same physical drift used in the original complete_nonlocal_row expression for $D w$. It is not a new coordinate velocity or a substitute obtained from $c_T$.

Writing $A_r,B_r$ for the saved mixed arrays, define
$$
 \mathcal G^{(i)}_{a,k}
  =(A_r)_k+\sum_{\ell=0}^k\binom{k}{\ell}
                    d_{i,\ell}A_{k-\ell+1}
       +(\mathcal T\star B)_{k+1}
       +\chi_*\mathcal R_{a,k+1},
$$
$$
 \mathcal G^{(i)}_{b,k}
  =(B_r)_k+\sum_{\ell=0}^k\binom{k}{\ell}
                    d_{i,\ell}B_{k-\ell+1}
       +(\mathcal Q\star A)_{k+1}
       +\chi_*\mathcal R_{b,k+1}.
 \tag{RJ.21}
$$
Only amplitude angular orders at most three, mixed orders at most two, and rank orders at most three are used. These are new complete source bounds assembled from successful derivatives. They neither call the old DG source closure nor re-bound any completed amplitude derivative.

The first correction's physical input weights are the original ones in C/DG. In particular the external $\chi_*$ in (RJ.20)--(RJ.21) is exactly the old transport-rank multiplier; it is not an additional outer Sobolev factor. No $n^{-1}$ or $n^{-2}$ is inserted after the completed positive column functional.

This direct route does not use $c_T$ or $\Xi$. Their full-strip and real-angle budgets are therefore not mixed or silently changed.

## 7. Exact companion identities, means and the positive functional

Let $\mathscr A$ be the same complete positive functional from C.2/C.5, with all eighteen coefficients and all three genuine column-profile branches. Its input consists of the two ordinary angular arrays of orders zero through two. On density one,
$$
 \Gamma(z)=M(z)=\mathscr A(z).
 \tag{RJ.22}
$$
This is the already proved density-one window $H^{-5/3}$ with the original $H^{-4/3}$ input, not the density-zero inverse window. No $B_j$ is applied to $w_1^V$, $p(w_1^V)$ or $g(w_1^V)$ in this step.

In row $I_i$, distinguish the physical background scalar $v_i$ from the reference potential $V_j$. Read its complete derivatives from the old V array, and read the physical scalar $u_i$ from the old U array. Then
$$
 q_i=v_i g-v_{i,\phi}p,\qquad y_i=v_i p,\qquad h=\eta^{-1}p.
 \tag{RJ.23}
$$
The exact minus sign in $q_i$ is retained in the identity. For a complete majorant use
$$
 \widehat q_i=V_i\star\mathcal G^{(i)}
                       +V_i^{[1]}\star\mathcal P,\qquad
 \widehat y_i=V_i\star\mathcal P ,
 \tag{RJ.24}
$$
componentwise and only through order two. All ordinary zero modes remain. The background $\eta$ is radial, so its rowwise inverse does not create angular derivatives but still must be charged.

Define
$$
 \Gamma_{g,i}=M_{g,i}=\mathscr A(\mathcal G^{(i)}),\quad
 \Gamma_{q,i}=M_{q,i}=\mathscr A(\widehat q_i),\quad
 M_{y,i}=\mathscr A(\widehat y_i),
$$
$$
 \Gamma_{h,i}=M_{h,i}
       =\frac{\mathscr A(\mathcal P)}{\eta_{i,-}},\qquad
 M_{uh,i}=\frac{\mathscr A(U_i\star\mathcal P)}{\eta_{i,-}} .
 \tag{RJ.25}
$$
The final U product includes every Leibniz term. The independent physical even mean is not identified with an amplitude mean and is not removed by an angular normalization.

The common genuine-column envelope is the original $|\rho|^{-1/4}$. A bound number produced by $\mathscr A$ is its coefficient; it is not a constant pointwise column norm at the root.

## 8. Ten complete density-one source coefficients

Read the same six complete rows, the existing complete matrix-word constants and the original scalar outer-J and mean factors. Write $J_i$ for C_J_scalar, $c_i$ for cB, $m_i$ for m0_T0, $r_i$ for m0_rQ and $e_i$ for exact_nonlocal_even_mean_row_factor. Each symbol is the already saved nonnegative bound for that whole factor.

The six word constants used here are
$$
 K_{RQJ},\ K_{\rm primitive},\ K_{uJ},\
 K_{SQ},\ K_{RQJL},\ K_{uJL}.
$$
They already contain their full inner factors and were proved in both required directed windows. There is no separate multiplication by any inner $C_R$, $C_Q$, $C_J$, $C_L$ or inverse constant.

The seven first-row coefficients are
$$
 \begin{array}{ll}
 RQJg:&J_iK_{RQJ}\Gamma_{g,i},\\
 {\rm primitive}:&J_iK_{\rm primitive}\Gamma_{q,i},\\
 {\rm transported\ old\ mean}:&
   J_i\{c_i(V_i)_1(V_i)_0M_{g,i}/4+m_iM_{g,i}\},\\
 {\rm v_\phi\ old\ mean}:&J_ic_i(V_i)_1M_{y,i},\\
 SQ:&J_iK_{SQ}\Gamma_{h,i},\\
 RQJLh:&J_iK_{RQJL}\Gamma_{h,i},\\
 {\rm rQ\ old\ mean}:&J_ir_iM_{h,i}.
 \end{array}
 \tag{RJ.26}
$$
The three independent physical-mean coefficients are
$$
 e_iK_{uJ}\Gamma_{g,i},\qquad
 e_iK_{uJL}\Gamma_{h,i},\qquad e_iM_{uh,i}.
 \tag{RJ.27}
$$
The outer $J_i$ occurs only in (RJ.26). All factors in (RJ.26)--(RJ.27) are the original complete source factors; in particular the primitive mean, transported mean, background $v_\phi$ and radial $\eta^{-1}$ remain.

For each of these ten terms, take the largest coefficient over the identical six original intersections, then multiply by the square root of the already saved whole squared-envelope radial measure. The exact physical interval, one-sided uncertain-root contribution and root measure are unchanged. This uses the previous complete integral; it does not execute a new quadrature.

Compare each resulting complete bound with the same named term in the latest accepted full ledger, retaining the smaller complete bound only when the strict directed comparison proves it. All fourteen density-zero terms, both density-one w-only first terms and their two independent mean terms, and all three local terms remain byte-identical: exactly twenty-one unchanged term objects. Equivalently the only declared changes are the seven density-one first terms in (RJ.26) and three density-one physical-mean terms in (RJ.27).

The complete local sum stays unchanged. Nonlocal, first, independent mean and pair aggregates may then be recombined from their entire retained terms. No upper bound is subtracted from another upper bound.

## 9. Read-only inputs, new work and remaining scope

A conforming consumer must:

1. Read the successful HP, BG, SV, DG, RV, potential, C and directed-word receipts with full source/manifest/runtime identities and successful gates.
2. Preserve the HP/BG physical domains, the potential case and the exact negative $T_h$; validate the original 4501-byte fold stage and read Gi without calling its producer.
3. Copy the fourteen completed DG/RV amplitude derivatives, the HP W arrays, SV coordinate/G arrays, BG Bplus arrays, original determinant gap and all six original coefficient rows.
4. Bind the literal RV positive budget (RJ.12) before using (RJ.13). No scalar-potential, Fuchsian, inverse-image or original closure function is invoked.
5. Compute only the new reciprocal/product/chain-rule arrays (RJ.7)--(RJ.21), the complete same-window functionals and ten complete comparisons. New row arrays remain temporary.
6. Check the entire latest accepted 31-term ledger and preserve all twenty-one undeclared terms byte for byte. If BG is not yet successful, the consumer must not silently use an older ledger or rerun BG.
7. Publish only small final conclusions, exact input identities, gates, counters and hashes. Completed arrays and native output remain temporary.

This theorem bounds complete ordinary negative-volume sources. It retains the full original nonlocal, mean, seam, reference-jump and positive-graph obligations. It does not assert that the source-to-wave map, a true cut-to-quarter-return operator, the coupled two-ended high-mode inverse, the positive growing-column selection or the strong-return contraction is already proved. The existing typed source-to-density result at a strict negative cut remains a separate input; a smaller volume bound cannot supply a missing trace, frame or boundary map.
