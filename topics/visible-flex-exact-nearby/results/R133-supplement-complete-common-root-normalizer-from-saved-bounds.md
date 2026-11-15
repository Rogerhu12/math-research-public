# R133 supplement: a complete common root normalizer from saved bounds

2026-11-15, newton_source.

**Proved analytic statement and a minimal new scalar contract.** This note closes the two-window existence criterion for the common root input operator of IC.4 by an explicit finite cutoff. It retains the full root coefficient, both independent physical means, the exact finite complement and the original right multiplication order. No new numerical value of the root coefficient or chosen cutoff is asserted here.

## TF1. Object, circle and existing source identities

Use the exact continuous selected family
$$
 Q_\delta=\bar Q+\delta Z,\qquad |\delta|\le d_*:=10^{-8},
 \qquad \eta=\eta_0,
 \tag{TF.1}
$$
with the original repaired background and direction definitions
**440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47**
and
**6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04**.
The selected member used in IC and WY is contained in this family. The statement concerns the known family, without a finite-support assumption on an unknown solution.

The root is the same radial root $r_*$ and the root coordinate is the original physical angle: the root map satisfies $X(0,\phi)=\phi$. Work on the circle of length $\pi/2$, with normalized measure, physical frequencies $4j$ and
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 \|f\|_{H^t}^2=\sum_{j\in\mathbb Z}\Lambda_j^{2t}|\widehat f_j|^2.
 \tag{TF.2}
$$
The complete Wiener norm is
$\|f\|_{A^0}=\sum_{j\in\mathbb Z}|\widehat f_j|$.
Both Fourier signs and the coefficient at zero are included. The two physical mean ports are independently adjoined as in IC; they are not identified with a scalar Fourier mean introduced in an operator identity.

The exact pointwise root calculation PF.15 and the common input identity IC.3 give
$$
 F_*=-\frac{\ell_*}{2\eta_*}
     =\frac{\beta_*u_*v_*}{\eta_*},\qquad
 \widetilde C_\sigma=C_\sigma-F_*.
 \tag{TF.3}
$$
The same real $F_*$ occurs for both physical signs and both wave branches. This follows directly from its displayed root formula and the fixed root gauge, without identifying a scalar mean with the whole first coefficient. The complete selected $u_*,v_*$ have angular degree at most96, and $\beta_*,\eta_*$ are radial. Consequently $F_*$ has angular degree at most192. In particular the full mean of $v_*$ and every resulting coefficient of $F_*$ remain.

The primary analytic identities are the published
[pointwise root theorem PF](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md),
[common root input theorem IC](R133-supplement-individual-branch-first-coefficients-and-common-root-normalization.md),
[exact family theorem D](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md),
[positive-product theorem WL](R133-supplement-complete-waist-lifting-from-saved-positive-scalar-algorithm.md), and
[complete free-cut theorem FA](R133-supplement-complete-free-Airy-first-omitted-strict-cut-columns.md).
Their immutable identities are recorded in TF7.

## TF2. A complete root Wiener bound from two successful small receipts

The already proved complete state bounds, including all continuous repairs, are
$$
 \|\bar Q\|_{A^0,\mathrm{pair}}\le7,\qquad
 \|Z\|_{A^0,\mathrm{pair}}\le19.
$$
Define the exact rational
$$
 M_*=7+19d_*.
 \tag{TF.4}
$$
Then each of $\|u_*\|_{A^0}$ and $\|v_*\|_{A^0}$ is at most $M_*$. The response is already the physical direction; no extra background factor $\alpha$ is applied.

Let $B_*$ be the saved complete WL positive-product bound. Its original family has the smaller radius $10^{-10}$, and it proves
$$
 |\beta|\max(1,|K_\delta|)\le B_*
 \quad\hbox{on }[0,9/10]
 \tag{TF.5}
$$
there, including $\delta=0$. The derivation from the original nonnegative scalar algorithm is preserved; TF does not recover this product from an abstract operator norm.

The original compact metric variation has
$$
 G_\delta=G_0e^{\delta w/2},\qquad
 K_\delta=e^{-\delta w}(K_0+\delta T w'),\qquad
 \operatorname{supp}(w,w')\subset[1/20,9/50],
 \tag{TF.6}
$$
and $\beta$ is unchanged. The accepted strict cut and root interval satisfy
$9/50<r_c<r_*\le r_+<9/10$.
Thus the zero-parameter intrinsic products in (TF.5) apply at the root throughout (TF.1), by the exact off-support identity. This does not enlarge any old WL perturbation or operator-difference estimate.

Let $\eta_->0$ be the field
`complete_new_cut_domain_conclusion.complete_eta_full_complex_lower`
in the successful FA2 scientific receipt. Despite its containing object's cut-oriented name, this field is read from `c["em"]`, the original complete complex coefficient-domain lower bound, in FA's `new_domain_and_jets`. Its original domain contains the root and the full parameter disk used in (TF.1). It is not the cut-only bound of normalizer row790, nor an inferred lower bound obtained from an upper estimate. The original fold-stage SHA256 and the exact source/readout identity remain pinned.

The Wiener algebra property now proves
$$
 \boxed{\quad
 \|F_*\|_{A^0}\le
 F_A:=\frac{B_*M_*^2}{\eta_-}.
 \quad}
 \tag{TF.7}
$$
Here and in a future consumer, $B_*$ is evaluated by an outward upper endpoint and $\eta_-$ by a strictly positive lower endpoint. No coefficient is inferred by subtracting two norm bounds. No factor $1/4$ is assumed for the product $u_*v_*$, and the mean is not discarded.

Only (TF.7) is a new scalar product. Its accepted inputs, including their complete printed balls, are read without rerunning the old state, WL, fold or FA calculations.

## TF3. The exact compressed multiplication estimate

For an integer $J\ge1$, let
$$
 P_J=P_{\{|j|\ge J\}},\qquad
 \overline m_{F,t}(J)=
 \left(1+\frac{192}{J}\right)^{|t|}F_A.
 \tag{TF.8}
$$
Then, for every real $t$,
$$
 \|P_JM_{F_*}P_J\|_{H^t\to H^t}
 \le\overline m_{F,t}(J).
 \tag{TF.9}
$$
This is explicitly a bound for multiplication between two high projections. It does not assert the same estimate for unrestricted multiplication on $H^t$.

Indeed, a nonzero convolution coefficient satisfies $|m-n|\le192$. When $|m|,|n|\ge J$, the triangle inequality for $(1,4m)$ gives
$$
 \frac{\Lambda_m}{\Lambda_n}\le1+\frac{192}{J},
 \qquad
 \frac{\Lambda_n}{\Lambda_m}\le1+\frac{192}{J}.
 \tag{TF.10}
$$
Apply these ratios to the weighted Fourier matrix, then the complete $\ell^1$--$\ell^2$ convolution inequality. The required $\ell^1$ norm is precisely the full $A^0$ bound (TF.7), with both signs and the zero coefficient included. No square-root-of-bandwidth estimate or finite Fourier sampling is needed.

## TF4. Explicit common cutoff and the same inverse on both windows

Choose any integer
$$
 \boxed{\qquad
 J_F\ge\max\{192,97,\lceil4F_A\rceil\}.
 \qquad}
 \tag{TF.11}
$$
The cutoff may be rounded upward to a dyadic integer; the actual choice is recorded. Put
$$
 P_F=P_{J_F},\qquad
 A_F=P_FM_{F_*}IP_F,\qquad
 T_F=\mathrm{Id}+A_F.
 \tag{TF.12}
$$
Since $I$ commutes with $P_F$ and has same-window norm at most $(4J_F)^{-1}$ on its range, (TF.9) yields
$$
 \theta_t:=\frac{\overline m_{F,t}(J_F)}{4J_F},
 \qquad
 \|A_F\|_{H^t\to H^t}\le\theta_t.
 \tag{TF.13}
$$
At the two required windows,
$$
 \theta_0\le\frac1{16},\qquad
 \theta_{-4/3}\le\frac{2^{4/3}}{16}<\frac3{16}.
 \tag{TF.14}
$$
The strict final inequality follows from $16<27$ and does not rely on a floating comparison.

Both Neumann series converge and define the same operator:
$$
 \boxed{\quad
 \|T_F^{-1}\|_{L^2\to L^2}\le\frac{16}{15},
 \qquad
 \|T_F^{-1}\|_{H^{-4/3}\to H^{-4/3}}\le\frac{16}{13}.
 \quad}
 \tag{TF.15}
$$
For a trigonometric input, the partial sums are identical in both constructions. Their limits agree as distributions; density and boundedness extend this agreement to the common domain. These are two bounds for one inverse, not two independently selected inverses.

The corresponding complete forward bounds are
$$
 \|T_F\|_{L^2\to L^2}\le\frac{17}{16},\qquad
 \|T_F\|_{H^{-4/3}\to H^{-4/3}}\le\frac{19}{16}.
 \tag{TF.16}
$$
The operator acts identically below $J_F$ and on the two independently adjoined physical means. No smallness at cutoff97 is required. The root cutoff $J_F$, the moving strict-cut normalizer cutoff $J_s$, and a principal-angle cutoff are three different projections.

For a particular scalar result, the sharper complete values $(1-\theta_t)^{-1}$ may be recorded after their positive gaps are checked. The rational conclusions (TF.15) already follow from (TF.11), including the case $F_A=0$.

## TF5. Full finite complement and the original ordered branch identity

Define the exact finite map
$$
 F_J=M_{F_*}I-P_FM_{F_*}IP_F
     =(1-P_F)M_{F_*}I+P_FM_{F_*}I(1-P_F).
 \tag{TF.17}
$$
Its input and output Fourier support lie in $|j|\le J_F+191$. Multiplication shifts at most192 labels, while the low projection has $|j|\le J_F-1$. The output mean is retained. A physical mean block that was separate before this identity remains separate afterwards.

For the original complete root-reduced branch
$$
 L_\sigma=\mathrm{Id}+M_{C_\sigma}I+E_\sigma,
 \qquad E_\sigma:H^{-4/3}\longrightarrow L^2,
$$
IC.9 gives the exact order
$$
 \boxed{\;
 L_\sigma T_F^{-1}
 =\mathrm{Id}+M_{\widetilde C_\sigma}I
  +(E_\sigma-M_{\widetilde C_\sigma}IA_F)T_F^{-1}
  +F_JT_F^{-1}.
 \;}
 \tag{TF.18}
$$
All original finite rows receive the same right factor. Neither $T_F^{-1}$ nor an input-sign normalization is commuted past a true circle map, projection or multiplier. After right multiplication by $T_F^{-1}$, the row of $F_JT_F^{-1}$ is retained as a finite-rank functional with its actual dual norm; its former finite input Fourier support is not asserted.

For clarity, the complete strong costs can be kept separate. Let
$$
 \alpha_J=\frac{\Lambda_{J_F}^{4/3}}{(4J_F)^2},
 \qquad C_I=\frac{\sqrt{17}}4 .
$$
The two primitives and their high intermediate projection give
$$
 \|M_{\widetilde C_\sigma}IA_F\|_{H^{-4/3}\to L^2}
 \le
 \alpha_J\|\widetilde C_\sigma\|_\infty
              \overline m_{F,-1/3}(J_F).
 \tag{TF.19}
$$
Here the successive spaces are $H^{-4/3}$, $H^{-1/3}$, and $L^2$. Formula (TF.9) is applicable in the middle because that multiplication has both actual projections. The complete left multiplier is charged only after the second primitive, without a high-output assumption.

The existing finite support gives
$$
 \|F_JT_F^{-1}\|_{H^{-4/3}\to L^2}
 \le
 2C_I F_A\Lambda_{J_F+191}^{1/3}K_{F,-4/3}.
 \tag{TF.20}
$$
One may instead keep the exact finite rows and their complete dual $H^{4/3}$ fees. In either representation this term is retained. The present theorem does not supply $\|\widetilde C_\sigma\|_\infty$, $C_{E_\sigma}$, a finite Schur inverse, or a complete incoming inverse.

## TF6. Minimal new numerical consumer and preserved scope

The new scalar consumer needs two completed numerical objects:

| Role | Successful object | Exact fields |
|---|---|---|
| `WL_execution` | run43749764738/1, 18 true gates | `actual_scientific_receipt.complete_positive_product_conclusion.B_star`; `complete_original_input_conclusion.chosen_global_constants`, complete cover and definition identities |
| `FA2_science` | run43763658978/1, 24 true gates | `complete_new_cut_domain_conclusion.complete_eta_full_complex_lower`; full-family/source identities; copied RR exact cut/root domain |

The background and response bounds must be exactly the completed values7 and19, with the original definitions. The new radius is exactly $d_*=1/100000000$, justified as in TF1--TF2. The old WL radius remains exactly $1/10000000000$ in the copied receipt. Their roles are never conflated.

The analytic input closure pins the present theorem, IC, PF, D, WL and FA, plus the final FA scientific source proving the `c["em"]` readout identity. These are small current text files. A consumer does not import any of the old scientific producers. It needs no binary, gzip, artifact, native array, old row, root finder, Fourier enclosure or ray integration.

The new work consists only of:

1. Verify complete success, exact source/manifest/runtime identities and all gates for both accepted objects; verify the common repaired family and the coefficient-domain interpretation.
2. Copy the two original conclusions without re-rounding their printed balls; construct $M_*$ exactly and a complete outward $F_A$ by (TF.7).
3. Choose and record an integer satisfying (TF.11), with directed integer conversion. Record the complete $\theta_0,\theta_{-4/3}$ and both positive inverse gaps, as well as the rational comparisons in (TF.14).
4. Record the complete two inverse/forward bounds, the exact finite support $J_F+191$, and optionally the already specified scalar factor in (TF.19) and finite fee (TF.20). No missing $C_\sigma$ or $E_\sigma$ value is filled in.
5. Preserve the exact order (TF.18), both signs, both physical means and all original finite rows in the scope flags. Save the complete small science before presentation or publication guards. A failed identity/domain/positivity check does not become a successful inverse assertion.

Only a public Actions execution can supply this new numerical readout. The present text neither starts that execution nor reports it as complete. It does not modify the continuing signed-density transport, and no successful old numerical calculation is repeated.

## TF7. Immutable primary readout identities

| Text or receipt | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| IC full analytic input | bd4ed3ab5d72a10021df281542d080ef2f67fb0e | 17274 | 4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee |
| PF pointwise root normalization | e384f8711a44e1ad16dd05804faf65d62bf016c2 | 20413 | 5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026 |
| D exact compact metric family | c85b66866103ea021cebbc050ccead214d4cf9d9 | 15214 | 92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635 |
| WL positive algorithm proof | 3be45577db460dd222cae43bccaef7d74bd0e6ae | 11194 | e2e9d6d4dc98c8f0b2d9c6c5cc7700a3389d228c39470736f3a8706dccbd192e |
| WL complete execution | ac779c8c374e1d577f004eee3024f087d7e5034d | 25000 | 936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d |
| FA complete analytic contract | acfb0cfd9a2598c00a6b29c2db05041d0340cba9 | 27814 | 24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af |
| FA2 final scientific source | 9e0a75461e0b8302a82e0444828a2c86379c3443 | 48827 | a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954 |
| FA2 complete small science | 2001f4e2eeece1cda56b18b90dccab04b7f6d336 | 35718 | 2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2 |

The original full coefficient-domain stage is bound transitively by SHA256
**29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144**
in the successful FA2 science. It is not restored or recomputed for TF. The two successful small receipts and their exact source identities suffice for the new scalar readout above.
