# R133 supplement: correlated terminal-Ai leading scalar and its complete waist normalization

2026-11-15, visible-exact-astra-0df9.

**Proved exact identities and a minimal new scalar contract.**
This note closes the leading scalar left open in [WY](R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md) for the same terminal-Ai free reference column. It keeps the full reference mean residual and uses its correlation with the radial density. All four physical sign/wave choices have the same absolute scalar. A later public consumer evaluates only the explicitly listed new positive scalar combinations of accepted small conclusions.

This note does not claim an incoming inverse, a finite Schur gate, a true nonlinear core, or completion of the surface.

## 1. One fixed family and one fixed terminal column

Use the exactly continuous centre and direction with definition hashes
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
Throughout,
$$
 Q_\delta=Q_0+\delta Z,\qquad
 \nu_\delta=\nu_0+\delta,\qquad \eta_{\rm intrinsic}=\eta_0,
 \qquad |\delta|\le d_*:=10^{-8}.
 \tag{KL.1}
$$
The canonical state, both physical mean coordinates, original moving angle, reflection convention, true radial variable and original positive Fourier normalization are unchanged. The symbol $\eta_*=-G(r_*)\langle v(r_*)\rangle>0$ below is the characteristic coefficient at the root, not the fixed intrinsic parameter $\eta_0$.

The actual strict cut and root bracket are
$$
 \begin{split}
 r_c&={76285779072683\over320000000000000},\\
 [r_-,r_+]&=
 \left[{1191984371497\over5000000000000},
       {2383968743003\over10000000000000}\right],
 \qquad r_*\in[r_-,r_+],\\
 \Delta_*&=r_+-r_c
          ={1220703413\over320000000000000}.
 \end{split}\tag{KL.2}
$$
All root quantities are evaluated at the actual root. The bracket midpoint is never substituted for it.

The reference is precisely P.8--P.9 and FA.21 of the [complete free-Airy theorem](R133-supplement-complete-free-Airy-first-omitted-strict-cut-columns.md):
$$
 a_0(0,X)=1,\qquad b_0=O(T^2).
 \tag{KL.3}
$$
It is the terminal-Ai free column used in FA, AW and WY. No assertion about a second Bi column or another genuine root normalization is obtained by renaming this column.

## 2. Exact radial correlation, with the complete mean residual

Write
$$
 m=\langle v\rangle_\phi,\quad
 S_0=u^2+Kv^2,\quad
 n_g={a_{\rm phys}^2\over m^2},\quad
 \ell_0=-2\beta\langle S_0\rangle_\phi .
 \tag{KL.4}
$$
Let $R_0$ be the complete second moving mean residual of the same reference:
$$
 m_r=\beta m(1-\langle S_0\rangle_\phi)+R_0.
 \tag{KL.5}
$$
The ordinary primitive has zero mean. Thus (KL.5) follows from the complete moving PDE with its mean still present; it does not assume that the reference solves that PDE. Since $a_{{\rm phys},r}/a_{\rm phys}=\beta$,
$$
 (\log n_g)_r
 =2\beta-2m_r/m
 =-\ell_0-2R_0/m.
 \tag{KL.6}
$$
The true $m$ is nonzero on this negative branch, as in SP/PF. All functions are exactly continuous across the declared pieces. The identities hold almost everywhere on pieces, and their integrated forms have no extra value jump.

PF.20b defines the radial factor
$$
 E(r)=\exp\!\left(\int_{r_*}^{r}-{2R_0(s)\over m(s)}\,ds\right),
 \qquad E(r_*)=1 .
 \tag{KL.7}
$$
Set
$$
 k_{\rm root}(r)=\exp\!\left(\int_{r_*}^{r}\ell_0(s)\,ds\right).
$$
Integrating (KL.6) gives the exact equality
$$
 \boxed{\quad E(r)={n_g(r)\over n_g(r_*)}\,k_{\rm root}(r).\quad}
 \tag{KL.8}
$$
The nonzero residual $R_0$ has been retained throughout. Equation (KL.8) uses a correlation identity, not a subtraction of independent upper bounds and not a new estimate claiming $R_0=0$.

## 3. The four absolute leading scalars

Let
$$
 k_*=K_r(r_*)>0,\qquad
 \lambda_*=(\eta_*^2k_*)^{1/3}.
$$
Use the physical wave $\sigma=\pm1$ and input sign $\epsilon=\pm1$ of PF/WY; FA's printed oscillatory label has the fixed opposite physical-wave convention explained in WY. The P.8 root trace and (KL.3), substituted in FA.21, give
$$
 |\kappa_{\sigma\epsilon}|={1\over2\sqrt\pi}.
 \tag{KL.9}
$$
The Maslov phase and the factor $\sigma/(i\epsilon)$ remain in the exact operator. Only their absolute values are used for a scalar norm bound. There is no sum over the four phases in (KL.9).

PF.20b gives the root coefficient
$$
 \ell_{\sigma\epsilon}^*
 ={\sigma\sqrt2\over i\epsilon}\,
 n_g(r_*)\kappa_{\sigma\epsilon}
 \left({k_*\over\lambda_*}\right)^{1/4}.
$$
At the waist it is multiplied by $E(0)$. Applying (KL.8) before taking norms therefore gives
$$
 \ell_{\sigma\epsilon}
 ={\sigma\sqrt2\over i\epsilon}\,
 \kappa_{\sigma\epsilon}
 \left({k_*\over\lambda_*}\right)^{1/4}
 n_g(0)k_{\rm root}(0).
 \tag{KL.10}
$$
In particular the same root density cancels exactly. It is not replaced by an unrelated bound from a different endpoint. Since
$(k_*/\lambda_*)^{1/4}=(k_*/\eta_*)^{1/6}$,
$$
 \boxed{\quad
 |\ell_{\sigma\epsilon}|^{-1}
 =\sqrt{2\pi}\,{1\over n_g(0)}
       \left({\eta_*\over k_*}\right)^{1/6}
       {1\over k_{\rm root}(0)} .
 \quad}
 \tag{KL.11}
$$
All four choices share the right side. The two independent physical means and all transported finite rows of WY are still separate blocks.

For the input multiplier
$\Lambda_\sigma=\ell_{\sigma,+}\Pi_++\ell_{\sigma,-}\Pi_-$,
(KL.11) is its exact norm on each original nonmean Fourier Sobolev window. It does not move $\Lambda_\sigma^{-1}$ across the common root chart or its coefficient multipliers. In particular WY keeps
$$
 U_{X_{-\sigma}}^{-1}J_\sigma\widehat T_{J_s}(0)^{-1}
 E_*\Lambda_\sigma^{-1}T_F^{-1}\mathscr S^{-1}
 \tag{KL.12}
$$
in this order. The complete state error $E_*$ already contains both input signs. Taking their maximum adds no new $\sqrt2$ factor.

## 4. The correct directed strict factor and a new root-short budget

The same SF leading radial function on the strict interval is
$$
 k_{\rm SF}(r)=
 \exp\!\left(\int_{r_c}^{r}\ell_0(s)\,ds\right).
$$
Hence
$$
 k_{\rm root}(0)=k_{\rm root}(r_c)k_{\rm SF}(0).
 \tag{KL.13}
$$
By WX.29--WX.33 of the [true-waist coordinate theorem](R133-supplement-complete-true-waist-coordinates-from-saved-positive-products.md),
$$
 k_{\rm SF}(0)^{-1}
 =\exp\!\left(\int_0^{r_c}\ell_0\,dr\right)
 \le P_+,
 \tag{KL.14}
$$
where $P_+$ is the saved **forward** scalar radial exponential upper bound. The reverse scalar is a different quantity. No norm upper is divided by another norm upper.

It remains to bound only $[r_c,r_*]$. The exact metric formula (D.2) in the [selected-parameter difference theorem](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md) reads
$$
 G_\delta=G_0e^{\delta w/2},\qquad
 K_\delta=e^{-\delta w}(K_0+\delta T w'),
 \qquad \operatorname{supp}(w,w')\subset[1/20,9/50].
 \tag{KL.15}
$$
By (KL.2), $9/50<r_c<r_*\le r_+<9/10$. Thus $G_\delta=G_0$ and $K_\delta=K_0$ on the entire new short interval for every parameter in (KL.1).

Use the accepted WL complete positive-product bounds:
$$
 B_*\ge \sup_{[0,9/10]}|\beta|\max(1,|K_0|),\qquad
 G_*\ge \sup_{[0,9/10]}|G_0|\max(1,|K_0|).
 \tag{KL.16}
$$
The original WL products were uniform for its smaller parameter ball and hence include $\delta=0$. Their derivation from the same saved nonnegative algorithm is retained. Equation (KL.15), not an extrapolation of a perturbation fee, makes those zero-parameter products available on the short interval in the larger family (KL.1).

The accepted complete continuous-state bounds are
$\|Q_0\|_{A^0,\mathrm{pair}}\le7$ and $\|Z\|_{A^0,\mathrm{pair}}\le19$.
Their mean and constant repair are included. Put
$$
 M_*=7+19d_*.
$$
The response is already physical and receives no extra $\alpha$. Then on the short interval, including the actual root,
$$
 |m|\le M_*,\qquad
 \eta_*\le G_*M_*,
 \qquad
 |\ell_0|\le2B_*M_*^2.
 \tag{KL.17}
$$
The last inequality keeps the complete average of $u^2+Kv^2$ and is valid even when $K$ changes sign. It does not use a nonmean projection of this quadratic.

It follows that
$$
 {1\over k_{\rm root}(r_c)}
 =\exp\!\left(\int_{r_c}^{r_*}\ell_0\,dr\right)
 \le \exp(2B_*M_*^2\Delta_*).
 \tag{KL.18}
$$
This is the only new interval budget. No old flow, enclosure, root finder, integral, QR or mean-completion calculation is repeated.

## 5. Positive endpoint inputs and the complete sufficient scalar

Let $n_-$ be the accepted positive lower bound for $n_g(0)$ in the full SP family, copied verbatim by WT. Let $k_-$ be the accepted RR lower bound for $K_r$ on the complete original body germ containing
$[r_c,r_+]$, copied verbatim by FA2. The latter comes from
`intrinsic_whole_third_jets.K1` of common body row 3070. The RR gate includes
$$
 9/50<r_{\rm body,left}\le r_c<r_-\le r_+
                  \le r_{\rm body,right}.
 \tag{KL.19}
$$
It is not an extension of the cut-only normalizer row 790. That row's $\eta$ upper cannot be moved to the root. Here (KL.17) supplies the root $\eta$ upper directly.

Using outward upper endpoints for $B_*,G_*,P_+$ and positive lower endpoints for $n_-,k_-$, define
$$
 \boxed{\quad
 K_\Lambda^{\rm suff}
 =\sqrt{2\pi}\,
   {P_+\over n_-}
   \left({G_*M_*\over k_-}\right)^{1/6}
   \exp(2B_*M_*^2\Delta_*).
 \quad}
 \tag{KL.20}
$$
Equations (KL.11)--(KL.19) prove
$\|\Lambda_\sigma^{-1}\|_{H^t\to H^t}\le K_\Lambda^{\rm suff}$
for both waves and each $t=0,-1/3,-4/3$, on the same original nonmean input. This is one scalar multiplier, not three independently selected inverses.

For the actual common $J_s=268435456$ normalizer, a consumer may also record the two new complete left state-error prefactors
$$
 \begin{split}
 K_{\rm left,raw}
 &=B_{X^{-1},0}\,K_{WT,0}\,K_\Lambda^{\rm suff},\\
 K_{\rm left,selected}
 &=B_{\mathcal H^{-1},0}\,K_{WT,0}\,K_\Lambda^{\rm suff}.
 \end{split}\tag{KL.21}
$$
The first uses the true waist inverse-density bound from WX for the full family. The second uses the exact adjacent-angle cancellation in WY.35 at the already selected conjugacy only. It does not assert a family of selected conjugacies on all of (KL.1). Both keep the same WT inverse, the row $J_\sigma$ of norm at most one, the original right factors in (KL.12), all primitive/rank remainders, and both independent means. They multiply a future correctly typed complete state-error constant; no such constant is set to zero.

## 6. Four accepted small mathematical inputs

The minimal current-only consumer reads exactly these completed objects:

| Input | Exact field used | Mathematical purpose |
|---|---|---|
| WL execution, run 43749764738/1 | `complete_positive_product_conclusion.B_star`, `.G_star` and original complete state/definition identity | Same positive algorithm products in (KL.16); the existing full-state 7/19 bounds |
| WT science, run 43763134339/1 | `copied_complete_SP_waist_factors.density_radial_factor_lower`; the complete fixed-$J_s$ inverse row | Full-family true waist density lower and the same ordered inverse |
| WX execution, run 43763424840/1 | `complete_ungauged_leading_flow_conclusion.complete_forward_radial_exponential_upper`; complete true-waist and selected-$\mathcal H$ inverse $L^2$ rows | Correct orientation in (KL.14), and only the optional products (KL.21) |
| FA2 science, run 43763658978/1 | `complete_saved_cut_receiver_conclusion.RR_ng_q_and_means_read_verbatim.root_mean_value_q_bounds` | The whole-germ $K_r$ lower and exact root distance, with the complete terminal-Ai/family identity |

For execution records the fields in the table are inside their complete scientific receipt. The original objects and printed balls are copied without replacing their bytes by newly rounded substitutes. Their source hashes, gate counts, exact family, complete means and successful run identities are checked. The corresponding current proof/source texts are immutable metadata inputs; they are not imported as scientific programs.

The input closure also pins PF, WY, FA, WX, WL, WTA and D.2, including their exact mean/radial conventions. No old gzip, binary, artifact or native array is needed. The old WL smaller-$\delta$ perturbation conclusion remains at its original width. Only the exact off-support identity (KL.15) is used here.

The new scalar code must:

1. Check the full input closure, all four completed scientific receipts, common definitions, cut/root/family conventions, both positive lower endpoints, and the distinct selected-conjugacy scope.
2. Copy the original relevant complete objects, then evaluate (KL.17), (KL.18), (KL.20), and, if requested, the two whole products (KL.21).
3. Record the four sign/wave choices with the same resulting norm enclosure and retain the exact phase factors symbolically. It must not sum the four absolute values or move the input $\Lambda_\sigma^{-1}$ through $T_F^{-1}$ or $\mathscr S^{-1}$.
4. Save the full scientific receipt before any presentation or Git-publication size gate. Failed positivity or identity gates produce an explicit incomplete conclusion; they do not trigger an unrelated input choice.
5. Record zero old scientific calls and zero new array/artifact/Release persistence. Every new numerical evaluation is made only in the public Actions job.

## 7. What remains after this scalar

The current statement fixes the leading terminal-Ai scalar and its typed use in WY. It preserves the actual normalizer's finite complement, the distinct waist projection rank, both physical mean receivers, the two primitive products and their full coefficient fees, the complete strong source and seam budget, and the common root/input order.

The actual norms of $T_F^{-1}$ and the signed first-coefficient multipliers still require their own valid inputs. Genuine-minus-free columns and other reference columns keep their original AW/AD/RR fees. No infinite incoming inverse or finite Schur conclusion follows by treating the newly bounded scalar as one of those missing operators.
