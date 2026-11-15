# R133 supplement: actual complete ordinary core residual restriction

2026-11-15. **Proved by the first public run, with all 18 structural gates passed.** The saved complete background residual has now been restricted to the actual core $[0,9/10]$. The new ordinary source bound includes the complete even mean, the exact continuous-centre repair, the previously completed continuous-$Z$ source, and the complete selected-parameter remainder. The original global bound remains a separate valid fallback.

The actual run is [43757468943/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43757468943), job `132944606347`, from the unique push of `9c0e3263200f63ea61420d0d691b7ef763263feb`. Its scientific child returned $0$, all $18/18$ gates passed, and the workflow completed successfully. No old producer, complete global integral, $Z$, $D$, $WL$, Green or Gram calculation was repeated.

## CRA1. Exact same object and ordinary norm

This is the actual evaluation of the [core-restriction contract](../notes/2026-11-15-R133-complete-core-residual-restriction-contract.md) and the transfer proved in [RF](R133-supplement-complete-core-residual-reuse-for-the-selected-centre.md). Fix
$$
 L=9/10,\qquad d=10^{-10},\qquad
 Q_\delta=Q_0+\delta Z,\qquad \nu_\delta=\nu_0+\delta,\qquad |\delta|\le d,
 \tag{CRA.1}
$$
at the original fixed $\eta_0$. The exact definitions are
$$
 \operatorname{SHA}(Q_0)
 =\texttt{440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47},
$$
$$
 \operatorname{SHA}(Z)
 =\texttt{6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04}.
$$
The signed source is
$$
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta).
 \tag{CRA.2}
$$
Use ordinary $dr$, the normalized original moving-circle measure $(2/\pi)d\phi$, and the Euclidean two-component $L^2$ norm. The low projection $\Pi_{96}$ retains all 96 odd and 97 even coordinates, including the full even mean with weight one. The physical amplitude
$$
 \alpha=\frac{6890507429876859}{9007199254740992}
 \tag{CRA.3}
$$
is applied exactly once to the original unscaled background residual. There is no radial $P$, physical-angle composition, old weighted-state conversion, or second amplitude factor on the already physical continuous direction $Z$.

The complete background state and its exact repair have angular degree $32$. Their cubic residual $f_0$ has degree at most $96$ in the original moving angle. This finite support belongs to the known source; it is not a truncation assumption on an unknown core correction.

## CRA2. Original input recovery and the only new integral

The worker restored the three original compressed byte parts at the immutable history commit
`7c130fb94528de8f003a43e7049fb42768a64eec`. It verified their compressed and decompressed hashes, offsets, and concatenation to the original container:
- Bytes: `4592623`.
- SHA256: `6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`.

All $7296$ original closed rows and $6143$ paid seams were checked. The complete partition hash is
`6d200bc4b7a4dfc9a20f942161dac51a0b7688386586206ee26ef0b68c2a9518`.
The new core restriction consumes exactly $5956$ rows, indices $0,\ldots,5955$, with exact total intersection length $9/10$.

The first intersection is
$$
 \left[0,\frac{7686143364045647}{36893488147419103232}\right].
$$
The last is
$$
 \left[\frac{4052614164685201}{4503599627370496},\frac9{10}\right],
$$
inside the old last row whose right endpoint is
$\frac{8106479329266893}{9007199254740992}$.
The complete new intersection-inventory SHA256 is
`c3fe6032345d86fe65d0be6ee36ccd3c12625caa175c0ad97d6d3559141616d1`.

For each component $a=U,V$, the new integral is the exact positive sum
$$
 I_a^{\rm core}
   =\sum_i |[r_i,r_{i+1}]\cap[0,L]|\,(R_{a,i})^2,
 \qquad
 F_{\rm raw}^{\rm core}
   =|\alpha|\sqrt{I_U^{\rm core}+I_V^{\rm core}},
 \tag{CRA.4}
$$
where $R_{a,i}$ is the original complete ordinary residual supremum on that closed row. No old integrated-cell bound is scaled by an intersection-length ratio. The mean is present in the original complete $V$ residual before squaring.

The whole-interval integral was only read from its old record. The old raw terminal-domain failure at index $7271$ remains in the recovery receipt; its failed graft rows are not reused. The successful original completed cover is the input of CRA.4. The old mixed-$Z$ failed-plan run `43612904296` also remains recorded, together with its successful finish `43613560173`; neither historical failure is rewritten as a success.

## CRA3. Actual core restriction and complete repair

All displayed balls below are copied verbatim from the successful small scientific conclusion. Their radii are retained. The raw restriction gives:

| Quantity | Complete actual directed ball |
|---|---|
| Unscaled $I_U^{\rm core}$ | `[1.35617770679055975780512292503422947493652614301621072712288903800041142e-15 +/- 3.49e-87]` |
| Unscaled $I_V^{\rm core}$ | `[2.66137329252290801157394245333338089860257557660572971960476439528677205e-15 +/- 3.31e-87]` |
| $F_{\rm raw}^{\rm core}$, with $\alpha$ once | `[4.84888779368343834769439454346442824068533197828925809666765999900442928e-8 +/- 4.94e-80]` |

The complete raw-to-repaired segment lies in the already checked known-state bounds $7$ and $6$. With the original whole-core positive product bounds $B_*,G_*$, RF gives
$$
 C_0=169B_*+6G_*,
 \qquad C_1=\frac{49}{4}B_*+7G_*,
 \tag{CRA.5}
$$
and
$$
 E_{\rm centre}
 =\sqrt L\left(C_0\,3.861\,10^{-18}
                  +C_1\,1.970\,10^{-17}\right).
 \tag{CRA.6}
$$
The exact continuous repair is piecewise constant in $r$, so its ordinary radial derivative is zero almost everywhere. Its original value jumps cancel the saved raw jumps exactly. No distributional interface source is omitted.

| Quantity | Complete actual directed ball |
|---|---|
| $C_0$ | `[882.521701141286635746566891203601979891159021397003888592554955892001716 +/- 2.44e-70]` |
| $C_1$ | `[154.974185471401969077881913968506276755596433471796509676087563384000124 +/- 4.42e-70]` |
| $E_{\rm centre}$ | `[6.12888092333024374544776599203284183856032229971784695449868404436730321e-15 +/- 1.63e-87]` |

## CRA4. The complete selected source, including the old raw mean

The successful original mixed-$Z$ certificate supplies the full source
$-s_0=(\partial_r-A_0)Z-\mathcal F_\nu$. Its saved inner-body bound already includes the raw even mean, the correlated source completion, and the exact continuous-direction offsets. The entire nested full/low/high record is copied unchanged into this result.

Let $S_{\rm full}$ and $S_{\rm low}$ be its complete inner-body $L^2(dr;L^2_\phi)$ bounds, and let $D_{\rm core}$ be the already successful complete additional-response-source bound on the same core and $|\delta|\le d$. RF and R give, for each such $\delta$,
$$
 \|f_\delta\|
 \le F_0+|\delta|S_{\rm full}
                 +\frac{\delta^2}{2d}D_{\rm core},
 \tag{CRA.7}
$$
$$
 \|\Pi_{96}f_\delta\|
 \le F_0+|\delta|S_{\rm low}
                 +\frac{\delta^2}{2d}D_{\rm core}.
 \tag{CRA.8}
$$
Here $F_0=F_{\rm raw}+E_{\rm centre}$ and $f_0=\Pi_{96}f_0$ exactly. The source $D_{\rm core}$ is only the additional selected-parameter remainder; it is not relabelled as the full ordinary $f_\delta$.

The actual uniform contributions at $d$ are:

| Quantity | Complete actual directed ball |
|---|---|
| $dS_{\rm full}$ | `[1.57474091914550656073726482055653024104310237956401152663478883505252573e-16 +/- 3.44e-88]` |
| $dS_{\rm low}$ | `[1.57099275206002702728713743959252040536263067482827384311762954054345382e-16 +/- 3.56e-88]` |
| $dD_{\rm core}/2$ | `[2.16219514268118601346015690219221144174206236807112177913704404016450000e-16 +/- 6.09e-89]` |

The two complete background choices remain separate:

| Background choice | Complete repaired $F_0$ | Uniform full $\|f_\delta\|$ | Uniform low193 $\|\Pi_{96}f_\delta\|$ |
|---|---|---|---|
| `new_core_restriction` | `[4.84888840657153068071876908824102744396951583432148806845235544887283372e-8 +/- 1.67e-80]` | `[4.84888844394089129898569483021524467145693266217313554480368850659116247e-8 +/- 3.84e-80]` | `[4.84888844390340962813089949571397086181683430536841849744631167141956953e-8 +/- 1.26e-80]` |
| `old_global_fallback` | `[7.04465000340915142415857782993569784428154644203644539962459595665359970e-8 +/- 2.41e-80]` | `[7.04465004077851204242550357190991507176896326988809287597592901437192845e-8 +/- 2.34e-81]` | `[7.04465004074103037157070823740864126212886491308337582861855217920033550e-8 +/- 4.68e-80]` |

Thus the new core restriction gives the explicit safe ordinary bound
$$
 \boxed{\ \|f_\delta\|_{L^2([0,9/10];L^2_\phi)}
                     <4.848889\,10^{-8}
        \quad (|\delta|\le10^{-10}).\ }
 \tag{CRA.9}
$$
The complete low193 bound is the distinct ball in the table. Both inequalities retain the full even mean. The old global fallback remains valid and is not used to replace a smaller component of the new case. The existing $Z$ mean and $384E_Z$ offset fee are not charged again.

The scale of the resulting estimate is already present in the known background-source bound. The record is an upper bound on that source, not a lower bound on the unknown correction or a failure test for the coupled problem.

## CRA5. Complete gate inventory and public execution

The actual directed arithmetic used Python `3.12.14`, python-flint `0.9.0`, and $320$ bits. The new scientific stage took `0.7173647139999986` seconds; the child wall time was `1.0230378330000036` seconds. The workflow began at `2026-11-15T20:20:02Z` and completed successfully by `20:20:55Z`.

The complete actual gate list is:

1. **PASS:** public pinned runtime and320-bit directed arithmetic.
2. **PASS:** unchanged complete manifest source parameters and all five mathematical receipts.
3. **PASS:** successful original mixed-Z finish and six complete actual gates.
4. **PASS:** same complete continuous centre direction raw mean and inner-Z source.
5. **PASS:** copied full and low inner-Z sources are finite with no repeated mean or offset charge.
6. **PASS:** successful original selected-D child with all twelve complete gates.
7. **PASS:** complete original D core ordinary source and selected parameter interval.
8. **PASS:** complete raw-to-repaired known-state segment lies inside the same7 and6 bounds.
9. **PASS:** successful original WL child with all eighteen complete gates.
10. **PASS:** same wholecore positive-algorithm products and complete centre direction definitions.
11. **PASS:** original complete7296 index and three exact byte-part receipts.
12. **PASS:** same complete fixed-eta raw candidate amplitude nu and full primitive residual.
13. **PASS:** entire original7296-row cover and6143 paid seams retain their exact partition.
14. **PASS:** new core restriction covers precisely zero to9/10 with true radial intersections.
15. **PASS:** two new complete core square integrals retain full mean and one physical amplitude.
16. **PASS:** complete centre repair uses known full operators and exact degree32 offsets.
17. **PASS:** complete selected full and low bounds retain their distinct linear and quadratic sources.
18. **PASS:** only the new core restriction and complete scalar combinations are claimed.

There was one new scientific child. All $21$ small text inputs and three historical byte parts match the manifest exactly. The eight Python files in the immutable AST closure passed; old scientific sources were not imported or executed. The copied $Z$ inner record, $D$ whole-core source record, and $WL$ positive-product record were independently compared with their original successful small receipts and match in full.

The worker recorded three real README pulls with empty diffs. It retained the live reviewed rules and the 120 KB publication reserve. The measured projected topic size was `198917990` bytes, below `200000000`. No new artifact, Release, row array, or reproducible binary was published. Original binary parts and the new intersection audit were runner-temporary only.

## CRA6. Immutable scientific and publication identities

The complete result is available in:

- [Scientific conclusion](../notes/complete_core_residual_restriction_ci/run-43757468943-1/actual-scientific-conclusion.json).
- [Execution record](../notes/complete_core_residual_restriction_ci/run-43757468943-1/execution.json).
- [Actual report](../notes/complete_core_residual_restriction_ci/run-43757468943-1/actual-result.md).

| Item | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Scientific conclusion | `772803d85d577c704bce6d51309c72697557cd36` | 15435 | `dbae6acdde2de41375aaa0886b847fee8ef92c0344150bf176716b88d0cb5734` |
| Execution | `77831103d37c5f0b2554663f46f3dc8dc452715a` | 18517 | `8d54c07e363b23a8b4be66ff1d73beafb5840fab9b82c1126c308cfcbfb43391` |
| Report | `ea9dee32631f16c7839266aea5c06020a4725acf` | 5187 | `439eb780a35601066850e8acf0439000668e12be3a2ee294de3629b5b1bc5b73` |
| SCI | `5af6cb4194815eeb6b87d2ba5e6596a562703d8e` | 22267 | `59f9130e024c51ce63b6138960535f986d0eaaa63dd724a1015a55729ff98f54` |
| Worker | `252f22542fe1e35da5411ef723eca1a75a94b1dc` | 47287 | `96401306459ceadca70659876f9219477c98098cd5a49d7fbd64a53775585a1d` |
| Manifest | `4d49b44afa00dcd9641f47bdd70d76af85a7e08d` | 19120 | `88a732839ec83e5661efdf7417d163b46784c7f4865f658463ba4b6540aabbf9` |
| Contract | `fc5e005f033c39cb17061299d80f5fa0a377b9ec` | 10408 | `206a2d5650f45577e6e8583a3ac1712fca4563be10c050945743cfabf4a73a10` |

The complete prepublication science/report payload is `20815` bytes with SHA256
`174c0583209adea2b23fea8a22c2bda14a09510bc8162c9b799a6e77cce10655`.
It was independently reconstructed from the exact scientific JSON tokens and the report before the last two README-pull rows; the bytes and SHA match the saved execution record. This check preserved all original decimal tokens. The execution additionally records its prepublication execution payload as `13451` bytes with SHA256
`b5061e1e8e96c73787edb1d87e6b690c9549dbfd045483351865f37d49a66327`.
The scientific original was atomically saved and printed before all formatting/publication guards.

## CRA7. Exact receiver use and remaining obligations

The new source bounds can enter the ordinary-source column of RF, NF, SR and [VR](R133-supplement-selected-value-and-difference-absorption-with-complete-cap-and-collar-inputs.md), provided the same selected centre, fixed intrinsic parameters, moving angle, source convention, and complete waist/cap rows are used. The original finite193 normalization is already the ordinary physical-amplitude moving pair; no $\alpha$, $\sqrt2$ or radial $P$ is inserted into its body-source input.

This actual result supplies the known $f_\delta$ term. It does not bound an unknown correction by the same number. Complete cap affine data, the independently evaluated waist source and its receiver, the nonlinear divergence source, unknown high-body and high-cut inputs, the whole-core and cut $H^1$ radii, same-state right-collar data, and the physical-curvature product-domain entrance retain their separate roles. Known high-source support is not an inverse estimate for unknown high modes.

The successful science is frozen. Any later sharper receiver or high-source scalar combination must consume these immutable small records and the existing complete certificates; it must not rerun the completed $7296$ producer, this core restriction, or the previously successful source and inverse calculations.
