# R133 supplement: actual complete common root normalizer and its two-window inverse

2026-11-15, visible-exact-astra-0df9.

**Proved actual root-input conclusion.** The unique public Actions run
[43766881076/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43766881076)
completed successfully: one child, return code 0, all 14 gates true.
For the full known real family $|\delta|\le10^{-8}$, the new complete root-coefficient budget gives the actual dyadic cutoff
$$
 J_F=1024.
 \tag{TFA.1}
$$
The one common input operator
$$
 P_F=P_{\{|j|\ge1024\}},\quad
 A_F=P_FM_{F_*}IP_F,\quad
 T_F=\mathrm{Id}+A_F
 \tag{TFA.2}
$$
has the same inverse on $L^2$ and $H^{-4/3}$. Its directed upper budgets have centres $1.0472939719234697\ldots$ and $1.0602058765251647\ldots$; the complete interval strings are recorded in section 4. The exact universal bounds $16/15$ and $16/13$ also hold.

This is the actual consumer of [TF](R133-supplement-complete-common-root-normalizer-from-saved-bounds.md). It retains the complete finite complement, both physical means, all original Fourier signs and the right input order. It does not provide a complete branch error, incoming inverse or finite Schur inverse.

## 1. Exact execution, files and code

The deployment was `0107666b538ced3a0fbc91f6a7f2cfa894f8ef6f`. The unique run is a push at attempt 1. Job `132973900700` ran from `2026-11-15T22:01:15Z` to `2026-11-15T22:02:00Z`, with every recorded step successful. The workflow became completed/success at `22:02:01Z`.
The scientific checkout after the actual pull was `8839cad6bdb5bdd7b5f09959cbc3a20c55c680c6`.

| Complete actual record | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [Science](../notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json) | `3766aea85aba59230be3813b4b7634d318316e49` | 18206 | `a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720` |
| [Execution](../notes/common_root_normalizer_two_window_ci/run-43766881076-1/execution.json) | `2f9f72bdae428ca74fda833af1aa8bad37fc1083` | 12849 | `6093fec311bc85afd416b86ef40939c4f55bd5c30976d3fe62ef4861efb87511` |
| [Full generated report](../notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-result.md) | `d519069a1a740e155cfc23fc7e44816ab5e3e87d` | 5927 | `f19b207559eff026498837fe180c18ae423b20e6671153532832b8077676c540` |

The [new scientific source](../scripts/fourfold_codazzi_common_root_normalizer_two_window.py) is blob `421f28401851fa0729faff878986341bf3be31d9`, 20669 bytes, SHA256 `bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b`. The separate worker is blob `02528b5da94960a7f8099068a28238247c7c584c`, 49691 bytes, SHA256 `17f825e6e4cf62676e1ef57d5cda3c095aa1656bca1ccc14a116e2053d21faae`.

The [input manifest](../notes/2026-11-15-R133-common-root-normalizer-two-window-CI-inputs.json) is blob `0e866f87639ff06fcddc48d552a9cdd85e4b78f4`, 15466 bytes, SHA256 `027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf`. Its 12 small current text pins total 289226 bytes and include nine mathematical roles. Three Python texts passed immutable AST validation. The old FA scientific source is read as a pinned text to establish its coefficient-field identity; it is not imported or executed.

The contract is blob `1052d454e98c613177919b7b19e472da1364a828`, 14951 bytes, SHA256 `652a9a2c2a9e0ccce1b07adae8848837ba579bec63d6ba5da21989a24b1bf5a3`. Actual arithmetic used Python 3.12.14, python-flint 0.9.0 and 320 bits. The source, parameter map, nine mathematical input hashes and all 12 file identities match the manifest.

## 2. The complete root coefficient and qualified two-input bridge

The centre and direction have definition hashes
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
Throughout,
$$
 Q_\delta=\bar Q+\delta Z,\qquad
 |\delta|\le d_*={1\over100000000},\qquad
 \eta_{\rm intrinsic}=\eta_0.
 \tag{TFA.3}
$$
The root coordinate is the original physical angle, with normalized period-$\pi/2$ measure and physical frequencies $4j$:
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 \Lambda_j=(1+16j^2)^{1/2}.
$$
By PF.15 and IC.3, the complete common root coefficient is
$$
 F_*=-{\ell_*\over2\eta_*}
     ={\beta_*u_*v_*\over\eta_*},\qquad
 \widetilde C_\sigma=C_\sigma-F_*.
 \tag{TFA.4}
$$
Here $\ell_*$ is the pointwise coefficient in the PF root calculation. It is not the separately defined averaged radial rate $\ell_0$ in KL/WX. The characteristic $\eta_*$ is also distinct from the fixed intrinsic parameter $\eta_0$.

The full root fields $u_*,v_*$ have degree at most96. Their product has degree at most192. The complete mean of $v_*$ and every coefficient of $F_*$ are retained. The response is already in the physical moving units, so no second $\alpha$ is applied.

Only two completed numerical records were consumed:

| Original record | Run; gates | File SHA256 | Field |
|---|---|---|---|
| WL complete execution | `43749764738/1`; 18 | `936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d` | Complete positive-algorithm $B_*$ and full-state 7/19 identity |
| FA2 complete science | `43763658978/1`; 24 | `2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2` | Full-complex coefficient-domain characteristic $\eta$ lower |

Their printed input intervals, copied without re-rounding, are
$$
 B_*:\quad
$$
`[4.72988444809427186638907323534400738954892703825889874906837 +/- 2.52e-60]`

$$
 \eta_-:\quad
$$
`[1.25299547095054573079366467377879882466593863889 +/- 3.72e-48]`

WL's old parameter width remains $10^{-10}$. Its $\delta=0$ positive product is valid on the whole core. The compact metric perturbation is supported in $[1/20,9/50]$, and the full root bracket lies to the right of $9/50$, so the same intrinsic product applies at the root throughout (TFA.3). This exact off-support identity does not extend an old whole-core perturbation fee.

The FA field `complete_eta_full_complex_lower` is read in its original algorithm from `c["em"]`, the full complex coefficient-domain lower bound including the root. It is not row790's cut-only endpoint value. The exact full-fold stage hash
`29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144`
is preserved through FA's successful input chain; that old stage was not restored or recalculated.

The known complete state bounds are $\|\bar Q\|_{A^0,\mathrm{pair}}\le7$ and $\|Z\|_{A^0,\mathrm{pair}}\le19$. Hence, with $M_*=7+19d_*$, the new positive budget is
$$
 \|F_*\|_{A^0}\le F_A={B_*M_*^2\over\eta_-}.
 \tag{TFA.5}
$$
The numerator takes its outward upper endpoint and the denominator its positive lower endpoint. No product factor $1/4$ or subtraction of upper bounds is used.

All seven complete objects copied from the two original receipts agree with their originals, including the full FA coefficient-domain record, root-germ record, original parameter maps and fold-stage hash.

## 3. Actual cutoff and the same two-window inverse

For $J\ge1$, TF.8--10 define the complete high-to-high multiplier bound
$$
 \overline m_{F,t}(J)
 =\left(1+{192\over J}\right)^{|t|}F_A,\qquad
 \|P_JM_{F_*}P_J\|_{H^t\to H^t}
 \le\overline m_{F,t}(J).
 \tag{TFA.6}
$$
Both projections in this statement are retained. It is not a bound for an unrestricted multiplier.

The new source chooses the smallest power of two $J\ge256$ satisfying $J\ge4F_A$, by exact integer doubling against the directed upper endpoint. The actual result is two doublings, $J_F=1024$. It also satisfies the required $J_F\ge192,97$.

Set
$$
 \theta_t={\overline m_{F,t}(J_F)\over4J_F}.
$$
Both actual gaps are positive. The complete exact comparisons
$$
 \theta_0\le{1\over16},\qquad
 \theta_{-4/3}<{3\over16}
 \tag{TFA.7}
$$
passed, so
$$
 \|T_F^{-1}\|_{L^2\to L^2}\le{16\over15},\qquad
 \|T_F^{-1}\|_{H^{-4/3}\to H^{-4/3}}\le{16\over13},
 \tag{TFA.8}
$$
with forward bounds $17/16$ and $19/16$. The sharper actual interval budgets $(1-\theta_t)^{-1}$ are listed next.

These are bounds for one inverse. Its Neumann partial sums are identical on common inputs; the two norm limits agree as distributions. The extension is identity below $J_F$ and on the two independently adjoined physical mean ports. The new root cutoff does not replace the moving cutoff $J_s$ or a principal-angle cutoff.

## 4. Complete actual root and two-window records

All records in this table are copied from the new science. They enclose computed sufficient budgets, rather than asserting numerical equalities for exact operator norms.

| Quantity | Complete directed record |
|---|---|
| $M_*$ | `[7.00000019000000000000000000000000000000000000000000000000000000000000000 +/- 1e-76]` |
| $F_A$ | `[184.968226870198793095967741098936895577604521232951166970003267689081637 +/- 4.21e-70]` |
| $1+192/J_F$ | `1.18750000000000000000000000000000000000000000000000000000000000000000000` |
| $\overline m_{F,-4/3}$ | `[232.599418384021189554756911708268762040835559600243816864301722138586279 +/- 2.02e-70]` |
| $\overline m_{F,-1/3}$ | `[195.873194428649422782953188806963168034387839663363214201517239695651603 +/- 1.99e-70]` |
| $\theta_0$ | `[0.0451582585132321272206952492917326405218761038166384684985359540256546966 +/- 3.59e-74]` |
| $\theta_{-4/3}$ | `[0.0567869673789114232311418241475265532326258690430282756016361626314907907 +/- 2.22e-74]` |
| $1-\theta_0$ lower | `[0.954841741486767872779304750708267359478123896183361531501464045974345303 +/- 3.65e-73]` |
| $1-\theta_{-4/3}$ lower | `[0.943213032621088576768858175852473446767374130956971724398363837368509209 +/- 2.78e-73]` |
| $K_{F,0}$ | `[1.04729397192346971466575604221266654789993881066352877954482111920497066 +/- 1.01e-72]` |
| $K_{F,-4/3}$ | `[1.06020587652516472128960751979473279256202439177297140649109225489526729 +/- 1.78e-72]` |
| $\|T_F\|_{L^2\to L^2}$ upper | `[1.04515825851323212722069524929173264052187610381663846849853595402565470 +/- 3.37e-72]` |
| $\|T_F\|_{H^{-4/3}\to H^{-4/3}}$ upper | `[1.05678696737891142323114182414752655323262586904302827560163616263149079 +/- 7.23e-73]` |

## 5. Exact finite complement and complete strong scalar fees

The original finite map is
$$
 F_J=M_{F_*}I-P_FM_{F_*}IP_F
 =(1-P_F)M_{F_*}I+P_FM_{F_*}I(1-P_F).
 \tag{TFA.9}
$$
Its original input and output Fourier support lie in $|j|\le1215$, since $J_F+191=1215$. All mean rows remain. After right multiplication by $T_F^{-1}$ its rows retain their true dual norms; the former finite input support is not asserted for $F_JT_F^{-1}$.

For the full branch $L_\sigma=\mathrm{Id}+M_{C_\sigma}I+E_\sigma$, the exact original order is
$$
 L_\sigma T_F^{-1}
 =\mathrm{Id}+M_{\widetilde C_\sigma}I
  +(E_\sigma-M_{\widetilde C_\sigma}IA_F)T_F^{-1}
  +F_JT_F^{-1}.
 \tag{TFA.10}
$$
No angular map, projection or multiplier is commuted through the right inverse.

Write $C_I=\sqrt{17}/4$ and
$\alpha_{J_F}=\Lambda_{J_F}^{4/3}/(4J_F)^2$.
The two genuine primitives pass successively through
$H^{-4/3}$, $H^{-1/3}$ and $L^2$. TF.19--20 give
$$
 \begin{split}
 \|M_{\widetilde C_\sigma}IA_FT_F^{-1}\|_{H^{-4/3}\to L^2}
 &\le
  \|\widetilde C_\sigma\|_\infty
  \alpha_{J_F}\overline m_{F,-1/3}K_{F,-4/3},\\
 \|F_JT_F^{-1}\|_{H^{-4/3}\to L^2}
 &\le 2C_IF_A\Lambda_{1215}^{1/3}K_{F,-4/3}.
 \end{split}\tag{TFA.11}
$$
The five actual scalar factors are:

| Factor | Complete directed record |
|---|---|
| $\alpha_{J_F}$ | `[0.00390625015522042756060337036209536262026374643521322332346079130175055625 +/- 4.60e-76]` |
| $\alpha_{J_F}\overline m_{F,-1/3}$ | `[0.765129696140432794622068291741588487672344527916782513742973457596198711 +/- 2.50e-73]` |
| $\alpha_{J_F}\overline m_{F,-1/3}K_{F,-4/3}$ | `[0.811195000152000493665410481205191460402144225098051332095526343768081396 +/- 2.76e-73]` |
| $2C_IF_A\Lambda_{1215}^{1/3}$ | `[6459.07545321336980755238952919805267945339373993511949014386736933313792 +/- 4.08e-69]` |
| $2C_IF_A\Lambda_{1215}^{1/3}K_{F,-4/3}$ | `[6847.94975241625631190337728732188703839448890633448660793760595227379572 +/- 1.44e-69]` |

In particular the two-primitive scalar still multiplies the separately established complete $\|\widetilde C_\sigma\|_\infty$. Its recorded value is not a substitute for that coefficient. The finite fee is a complete branch fee with the mean retained. It is not a finite inverse or a Schur bound.

## 6. All actual gates and saved small conclusions

1. **PASS.** public pinned runtime and320-bit directed scalar arithmetic.
2. **PASS.** current-only closure source parameters and every immutable small input.
3. **PASS.** WL completed original eighteen-gate full positive algorithm receipt.
4. **PASS.** WL positive beta product and full mean complete7/19 keep their original smaller radius.
5. **PASS.** FA2 completed original twenty-four-gate full complex coefficient readout.
6. **PASS.** eta lower comes from the original full coefficient domain c[em] and not cut-only row790.
7. **PASS.** root support degree192 and original ordered finite and mean identities are pinned.
8. **PASS.** the saved beta product and full-domain eta lower are valid directed endpoints.
9. **PASS.** the complete root coefficient including its mean has the new Wiener bound.
10. **PASS.** the recorded dyadic integer satisfies the full exact root cutoff inequality.
11. **PASS.** both strict Neumann gaps are positive for the same compressed operator.
12. **PASS.** the complete theta bounds imply the rational two-window inverse and forward bounds.
13. **PASS.** complete finite dual rows and two-primitive costs retain the true middle window and right order.
14. **PASS.** all fourteen gates preserve complete original inputs and zero old scientific calls.

The actual record contains one complete coefficient budget, one chosen root cutoff and two inverse windows. It records zero old scientific source imports, zero WL/FA/fold/state/root/ray calls, zero binary/native/archive restorations and no persisted new arrays, artifacts or Releases. The successful old calculations and this completed new calculation are frozen.

The complete science was atomically saved and printed before any publication-size guard. Its science/report prepublication payload is 24430 bytes, SHA256
`5661588aa9e093a15ae720373bfddfc089e173eef8fc60d7e510af3aec0b16db`.
Independent text reconstruction from the published science and report with the final publication-pull line removed gives exactly these bytes and SHA256. The execution also records the separate original 10277-byte process marker, SHA256
`f048bef4161deae8c42569c4ef51e4963b59e3941a80f605b684537049d738c0`;
no separate reconstruction of that marker is asserted here.

The complete 12-pin identity, nine mathematical hashes, parameter map, original-copy objects and all 14 gates were checked against the actual records. Both actual README pulls had empty diffs against the reviewed rules.

## 7. Consequence for the existing ordered receivers

The common root/input factor in IC and WY now has an actual inverse and forward bound on both required windows for the known family. Its original finite complement and physical means remain explicit. It can be used at its original right position, including after the sign multiplier $\Lambda_\sigma^{-1}$ when that ordering is prescribed.

The actual conclusion supplies neither $C_\sigma$ nor $E_\sigma$, and it does not remove the distinct state-source/seam term, density-conjugation ranks, waist projection rank, low physical ports, genuine-minus-free columns or any finite border. The root $J_F=1024$ is separate from the moving $J_s=268435456$ used by the corresponding actual normalizer. No high projection is moved through a true angle change.

No incoming inverse, finite Schur inverse, nonlinear core solution or final surface is concluded here.
