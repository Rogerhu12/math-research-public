# Positive budget separation and a new complete Taylor tail for the first genuine local source

**Status.** The analytic identities and the conditional comparison below are proved. The proposed enlarged amplitude product, its numerical gaps, and any numerical improvement require a new public Actions run. The previously accepted runs are immutable inputs.

This supplement concerns the same repaired $M_{32}$ family at the fixed intrinsic parameter $\eta_0$, the same complex $\delta$ and $z=1/j^2$ squares, both carrier signs, and both genuine common radial reference columns. It changes neither the root, the physical piece, its actual seams, the source windows, nor the reference normalization. All finite Taylor coefficients, old Fourier norms, old forcing, old profiles, old operator words, and old radial integrals are read without recomputation.

## 1. Exact accepted inputs and the proposed new computation

Use the following successful executions, with their published source and manifest identities.

| Role | Accepted run | Small execution |
|---|---|---|
| Whole original root piece, signed genuine correction Taylor degree $12$ | $43694458725/1$ | [whole Taylor execution](../notes/whole_root_signed_reference_Taylor_ci/run-43694458725-1/execution.json) |
| Correlated complete genuine forcing and correction bounds | $43698106023/1$ | [scalar execution](../notes/correlated_whole_reference_scalar_budget_ci/run-43698106023-1/execution.json) |
| Complete genuine columns and the already integrated $w_{1,rr}$ operator | $43700281022/1$ | [column execution](../notes/genuine_negative_reference_operators_ci/run-43700281022-1/execution.json) |
| Eighteen fixed positive operator coefficients and the complete original source budget | $43702688640/1$ | [complete source execution](../notes/complete_genuine_negative_sources_ci/run-43702688640-1/execution.json) |
| Complete directed word reuse, with the original local terms unchanged | $43703879926/1$ | [directed execution](../notes/directed_word_genuine_source_reuse_ci/run-43703879926-1/execution.json) |
| Exact regular transport first-local improvement | $43709396175/1$ | [accepted first-local execution](../notes/regular_transport_first_local_vector_ci/run-43709396175-1/execution.json) |

Every small execution path, byte count, and SHA is checked against the immutable input manifest. The new consumer reads the accepted whole Taylor and scalar execution tables, the eighteen positive coefficients, the accepted source ledgers, and the one original complete fold majorant stage. It does not reconstruct a finite Taylor polynomial.

Write
$$
 R_G=\frac3{8000},\quad \Sigma_G=\frac3{128},\quad
 H=\frac{893368603925465506687}{21990232555520000000000000}.
 \tag{B1}
$$
Here $H$ is the already accepted worst distance from the uncertain root to the entire original physical piece. The root interval and material piece endpoints remain
$$
 r_*\in\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}\right],
 \qquad
 r\in\left[
 \frac{2147184947341121}{9007199254740992},
 \frac{4295308144604611}{18014398509481984}\right].
 \tag{B2}
$$
The whole complex square is $|\Re\delta|,|\Im\delta|\le10^{-8}$ and $|\Re z|,|\Im z|\le1/9409$. Final real-column source norms use the same real parameter restriction as the accepted source consumer, after the complete complex coefficient estimates have been paid.

The first new operation will be a complete scalar amplitude estimate on a different, explicitly tested product. The second is a recovery of an upper bound for an already computed positive finite sum. The third is the replacement of its complete infinite tail. A separate positive comparison then recovers the rest of the accepted first-local operator and combines it with the new $w_{1,rr}$ estimate. These are new comparisons; no accepted numerical enclosure is rerun.

## 2. A positive-addend lemma, including directed rounding

Let an accepted algorithm use nonnegative numerical budgets $F,E$ and save a certified number $T$ with
$$
 F+E\le T.
$$
If the new consumer obtains a certified lower bound $0\le\ell\le E$ for **that same numerical addend**, then
$$
 F\le T-\ell.
 \tag{B3}
$$
With saved balls, take the upper endpoint $T^+$ and the lower endpoint $\ell^-$, and round $T^+-\ell^-$ upward. Require this result to be finite and nonnegative. Do not replace a failed consistency check by zero.

The interpretation in (B3) is essential. It is a statement about the positive arithmetic used by a specified accepted algorithm. It does not claim a positive lower bound for the true function or the true error. It also does not subtract one unrelated upper error estimate from another.

All repeated upward roundings in the accepted positive sum preserve (B3). For example, if the old algorithm first rounds a positive factor or a positive partial sum upward, its resulting addend is at least the corresponding exact positive expression. Thus a lower enclosure of that exact expression is a lower bound for the actual numerical addend that was used.

When a previously saved bound is the minimum of two distinct complete estimates, (B3) cannot be applied by choosing a positive addend from only one of those estimates. Section 5 below treats the particular minimum in the complete local source by proving a common positive addend for both alternatives.

## 3. Recovering the finite degree-$12$ contribution from the whole Taylor receipt

For $n\ge13$, $0<h<R$, and $p=0,1,2$, put
$$
 {\cal T}_{13,p}(M;R,h)=M R^{-p}T_{13,p}(h/R),
 \tag{B4}
$$
where, with $t=h/R$ and $d=1-t$,
$$
 \begin{aligned}
 T_{13,0}(t)&=\frac{t^{13}}d,\\
 T_{13,1}(t)&=t^{12}\left(\frac{13}d+\frac{t}{d^2}\right),\\
 T_{13,2}(t)&=t^{11}\left(\frac{156}d+
                         \frac{26t}{d^2}+\frac{2t^2}{d^3}\right).
 \end{aligned}
 \tag{B5}
$$
These are the full infinite positive sums
$\sum_{n\ge13}n!/(n-p)!\,t^{n-p}$, with no cutoff in the omitted tail.

For the physical Fourier frequency $4\ell$ define
$$
 {\cal S}_q(\sigma)=
 \sum_{\ell\in\mathbb Z}|4\ell|^q e^{-4|\ell|\sigma},
 \qquad q=0,1,2,
 \tag{B6}
$$
where the $q=0$ zero-mode contribution is $1$. In terms of $a=e^{-4\sigma}$,
$$
 {\cal S}_0=\frac{1+a}{1-a},\qquad
 {\cal S}_1=\frac{8a}{(1-a)^2},\qquad
 {\cal S}_2=\frac{32a(1+a)}{(1-a)^3}.
 \tag{B7}
$$
Both signs of $\ell$ and the complete mean are retained.

The frozen scientific source of run $43694458725/1$ has SHA256
a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be.
Its function derivative_budget saves, for each amplitude $u=a_1,b_1$ and each $p,q$,
$$
 T_{u,p,q}
 =
 \operatorname{up}\left(F_{u,p,q}
   +\bigl[
       {\cal T}_{13,p}(M_u^{\rm old};R_0,H)
       +{\cal T}_{13,p}(M_u^{\rm add};R_a,H)
     \bigr]{\cal S}_q(\Sigma_0-\sigma)\right),
 \tag{B8}
$$
with
$$
 R_0=\frac1{6000},\qquad R_a=\frac3{40000},
 \qquad \Sigma_0=\frac1{128}.
$$
The symbol $\operatorname{up}$ in (B8) includes the separately upward-rounded positive tail factors used in that source. The finite part $F$ is the already computed nonnegative sum of the complete signed Taylor coefficient norms, with the ordinary derivative factorials and powers of $H$. Signed Fourier convolutions were added before taking their norms in that accepted run. The source applies no subsequent minimum to (B8).

The old and added moduli are read from complete_tail_conclusion of that exact receipt. The new lower estimate
$$
 \ell_{u,p,q}
 \le
 \left[
 {\cal T}_{13,p}((M_u^{\rm old})^-;R_0,H)
 +{\cal T}_{13,p}((M_u^{\rm add})^-;R_a,H)
 \right]{\cal S}_q(\Sigma_0-\sigma)
 \tag{B9}
$$
is evaluated as a full interval expression and then rounded downward. Every denominator in (B5)--(B7) has a strictly positive interval gap. By monotonicity in the two moduli and by the old rounding convention, this is a lower bound for the **old algorithm's positive tail addend**. Therefore
$$
 F_{u,p,q}\le F^+_{u,p,q}
 :=\operatorname{up}\bigl(T^+_{u,p,q}-\ell^-_{u,p,q}\bigr).
 \tag{B10}
$$
The new consumer uses (B10) only on the original whole Taylor totals, not on the later scalar consumer's minimum of distinct complete bounds.

For this minimal consumer take only $p=2$, $q=0,1,2$, and $\sigma=0$. There are exactly six finite-budget recoveries. No Fourier coefficient, Fourier convolution, Taylor derivative, or original finite norm is reevaluated. In particular, the $q=0$ estimate still includes the full Fourier mean.

## 4. A new amplitude product using the already paid forcing

The accepted scalar run pays the complete raw regular forcing on
$$
 |\rho|\le R_F=\frac3{20000},\qquad
 |\Im\varphi|\le\Sigma_F=\frac1{64}.
$$
It also supplies the common potential image radius $I_T$ and the original inverse radial gap $g_T$, which is a lower bound for $|T/\rho|$ on the same inverse branch. The original fold stage supplies $A_+$, the angle displacement $B$, the complete $\chi=X-\varphi$ majorant, and $M,B_2,B_i$. Here $M$ bounds the leading first coefficient, $B_2$ bounds $b_0/T^2$, and $B_i$ is the original inverse leading branch bound. They are already valid on the canonical product obtained from $R_G$ by the original inverse theorem, whose radius is $\lambda R_G/2$ with $\lambda=9/2$. They are not limited to the scalar consumer's old choice $R_T=1/2000$.

Propose the distinct new product
$$
 R_T'=\frac3{5000},\quad
 \Sigma_A'=\frac{13}{2048},\quad
 \Sigma_X=\frac1{128},\quad
 \Delta_X=\frac1{1024},\quad
 R_s'=\frac1{8000},\quad
 \Sigma_s'=\frac3{512}.
 \tag{B11}
$$
The consumer must check all of the following with the accepted interval bounds:
$$
 \begin{gathered}
 H<R_s'<R_F<R_G,\qquad
 R_T'<\lambda R_G/2,\qquad R_T'/g_T<R_F,\\
 \Sigma_X+B<\Sigma_F,\qquad R_T'<I_T,\\
 \Sigma_A'+\frac23(R_T')^{3/2}+\Delta_X<\Sigma_X,\\
 R_s'A_+^{2/3}<R_T',\qquad
 \Sigma_s'+(R_s'/R_G)\|\chi\|<\Sigma_A'.
 \end{gathered}
 \tag{B12}
$$
The root vanishing of $\chi$ used in the last line is the same accepted root identity; its complete $R_G,\Sigma_G$ domain is checked. All strict gaps are saved as small final conclusions. No old failed large-radius case is relabelled as passed.

The first lines put every inverse image and every $sT$ segment, $0\le s\le1$, inside the actual already paid old product and common potential image. The optical displacement and the positive $\Delta_X$ margin put both regular forced paths in the forcing strip. The last line puts the new old-coordinate product inside the canonical amplitude product. Consequently the same regular normalized solution is continued to that product. Agreement on the original intersection follows from the same analytic regular transport equation and the same root normalization; no new solution or homogeneous constant is selected.

Let $F_a,F_b$ be the accepted complete raw forcing bounds, read without recomputation, and set
$$
 B_*=M+B_2(R_T')^{5/2},\qquad C_*=B_*B_i.
 \tag{B13}
$$
The already proved complete regular-forcing estimate, with the newly checked product, gives
$$
 \begin{aligned}
 M'_a={}&
 \frac{C_*R_T'}2F_a+
 \left[
 \frac{C_*(R_T')^2}{2\Delta_X}
 +B_2B_i\left(1+\frac{C_*}{6}\right)(R_T')^3
 \right]F_b,\\
 M'_b={}&
 C_*F_b+
 \left[
 \frac{C_*(R_T')^2}{5\Delta_X}
 +B_2B_i\left(\frac12+\frac{C_*}{7}\right)(R_T')^3
 \right]F_a .
 \end{aligned}
 \tag{B14}
$$
The full $F_b$ term and its mean are present. The quantities in (B14) are new scalar upper bounds for the same genuine $a_1,b_1$ on the new product (B11). Applying this formula on a new product does not rerun the original transport or its Taylor recursion.

Double Cauchy on this common product bounds every omitted joint coefficient. For the six requested derivatives,
$$
 N^+_{u,2,q}
 =\operatorname{up}\left(
     F^+_{u,2,q}
    +{\cal T}_{13,2}(M'_u;R_s',H)\,
       {\cal S}_q(\Sigma_s')\right).
 \tag{B15}
$$
This is the entire tail $n\ge13$, with both Fourier directions and the zero mode. The radial supremum and the Fourier sum are taken in the joint order used by the accepted coefficient norm; no exchange of a radial supremum with a Fourier sum is made.

The minimum of (B15), the corresponding original whole Taylor bound, and the corresponding accepted scalar bound is again a complete bound. This comparison is made for each of the six derivatives in the same norm. A worse new tail therefore does not invalidate an accepted bound. No assumption that it improves the answer appears in the proof.

## 5. Recovering the complete old remainder of the first local vector

Fix the same accepted fold, complete genuine profile, branch partition, and two-column input normalization. Let the eighteen positive numerical coefficients in run $43702688640/1$ define
$$
 {\cal A}_{\boldsymbol\kappa}(v)
 =\sum_{\nu=1}^3\sum_{i=1}^6\kappa_{\nu i}v_i,
 \qquad
 v=(a,a_\varphi,a_{\varphi\varphi},
       b,b_\varphi,b_{\varphi\varphi}).
 \tag{B16}
$$
These coefficients act on complete upper bounds. The common column envelope is $|\rho|^{-1/4}$, exactly as in the accepted source. The near and far row-symbol estimates, the mean output, and both genuine columns are already included in this functional.

The frozen complete source algorithm has SHA256
b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0.
Its function local_vectors forms the nonnegative derivative-majorant vectors
$$
 L_1=w_{1,rr}+{\rm Rest}
$$
and saves
$$
 T_{\rm loc}
 =\min\left\{
 {\cal A}^{\rm alg}(w_{1,rr}+{\rm Rest}),\
 \operatorname{up}\bigl(K_{rr}+{\cal A}^{\rm alg}({\rm Rest})\bigr)
 \right\}.
 \tag{B17}
$$
Here every operation in the superscripted positive algorithm rounds upward, and $K_{rr}$ is the already accepted complete $w_{1,rr}$ operator coefficient from run $43700281022/1$. The input weights are still $1,1/n,1/n^2$ for the three raw local vectors; (B17) is the first vector, with weight $1$.

Write $w^{\rm old}_{rr,i}$ for the six actual nonnegative budget numbers read by that old algorithm from the successful scalar receipt. Since (B16) is linear with nonnegative coefficients and all vector additions are upward-rounded,
$$
 T_{\rm loc}\ge
 {\cal A}_{\boldsymbol\kappa}({\rm Rest})
 +\min\left\{ {\cal A}_{\boldsymbol\kappa}(w^{\rm old}_{rr}),K_{rr}\right\}.
 \tag{B18}
$$
The same additive term has now been proved for **both** sides of the old minimum. Thus it is legitimate to calculate
$$
 \lambda_{rr}^-=
 \operatorname{lower}
 \min\left\{
 \sum_{\nu,i}(\kappa_{\nu i})^-(w^{\rm old}_{rr,i})^-,
 (K_{rr})^-\right\},
 \qquad
 R_{\rm rest}^+=
 \operatorname{up}\bigl(T_{\rm loc}^+-\lambda_{rr}^-\bigr).
 \tag{B19}
$$
All factors here are lower bounds for the algorithm's actual positive **budget numbers**, not lower bounds for true amplitudes. The original saved numbers and their exact component order are checked. Negative lower endpoints are replaced by zero only when nonnegativity of that budget is itself part of the accepted algorithm; the consistency check for $R_{\rm rest}^+$ is never clipped.

The full old Rest remains present: the ordered $D$ terms, the true $\rho$ to $r$ convention, $T_0$, $V_0$, $\mu V$, the $\vartheta Q$ term, and the complete left-$E_{12}$ correction of $w_0$. Its mean, Piola contribution, reference terms, and matrix multiplication order are not changed. No individual term is inferred to be small from a difference of two error bounds.

Apply the same fixed positive functional to the six new complete derivative bounds in (B15), using upper endpoints for the eighteen coefficients:
$$
 K'_{rr}
 =\min\left\{
 {\cal A}_{\boldsymbol\kappa^+}(N^+_{rr}),K_{rr}^+
 \right\}.
$$
Then a new complete first-local coefficient is
$$
 T'_{\rm loc}=R_{\rm rest}^++K'_{rr}.
 \tag{B20}
$$
The old $K_{rr}$ alternative is retained. This whole-operator comparison does not recompute that old operator and does not use any coefficient lower bound as an operator upper bound.

## 6. True radial measure and the accepted complete ledger

The original six negative source rows multiply the same complete first-local coefficient by their original outer $J$ factors and the same common $|\rho|^{-1/4}$ envelope. Their exact radial weights, including the uncertain-root band, were already integrated with the true $dr$ measure. The new calculation changes only this one uniform coefficient.

Let $\beta_{\rm loc}^->0$ be the lower endpoint of the accepted numerical $T_{\rm loc}$, and put
$$
 q_{\rm loc}=
 \min\left\{1,\,
 \operatorname{up}(T'_{\rm loc}/\beta_{\rm loc}^-)\right\}.
 \tag{B21}
$$
If the second entry is used, the new coefficient is bounded by $q_{\rm loc}$ times the actual old positive coefficient. Hence the old fully integrated local_raw_1 norm from the directed source ledger can be multiplied by this number. If the entry $1$ is selected, keep the old complete bound itself.

Let $L_D$ be that old directed-ledger local_raw_1 norm and $L_P$ its accepted regular-transport improvement from run $43709396175/1$. The updated term is
$$
 L_{\rm new}=\min\{q_{\rm loc}L_D,L_P\}.
 \tag{B22}
$$
The comparison is between complete bounds for the same source. It never subtracts integrated upper bounds or reconstructs radial weights from their totals.

All other twenty first-output terms and all ten independent physical-mean terms are copied from the accepted current ledger without numerical alteration. This retains the two distinct $J$ source windows, all nine old-circle operator words, the five old-mean terms and five independent physical-mean terms, both complete columns and signs, the ordinary-source normalization, all reference and physical seam jumps, and all Piola terms. The only new scalar recombinations are the complete local sum, first-source sum, and pair norm. The unchanged nonlocal and physical-mean totals are read exactly.

## 7. Execution and scope

The consumer must bind the successful execution identities, source hashes and input manifests, the one original fold stage and its publication receipt, the eighteen coefficient order, and the common physical/root/parameter domain before doing new arithmetic. The original natural stage bytes remain unchanged. A domain failure or a positive-budget inconsistency is reported as such, with the actual child return code and completed gates.

Only the six new derivative bounds, the new amplitude product gaps, the two recovered complete operator contributions, the uniform factor, and the resulting complete source totals are new mathematical conclusions. Complete intermediate subtraction/tail tables stay temporary. The new public receipts contain final small conclusions, exact source/parameter/run identities, and counts of every restored and new operation.

This supplement proves no new full high BVP inverse, no quarter-return smallness, no complete positive graph feedback, and no strong-return contraction. It neither deletes their source ports nor identifies an amplitude mean with the independent physical even mean. Those obligations remain exactly the ones in the accepted complete source contract.