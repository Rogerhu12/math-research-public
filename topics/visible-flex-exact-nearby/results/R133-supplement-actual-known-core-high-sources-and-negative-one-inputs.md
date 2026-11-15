# R133 supplement: actual complete known high sources and negative-one inputs

2026-11-15. **Proved by the first public run, with all 18 structural gates passed.** The known selected residual now has complete ordinary and $H^{-1}$ bounds above quarter-index thresholds $96$, $160$ and $224$. Its support above $288$ is exactly zero. All estimates refer to the same complete source in the original moving angle. They do not assert a bound for an unknown core correction.

The unique public run is [43759656502/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43759656502), job `132951372132`, from the push of `9bf1c00cebf2f15f1f08ae1106022981ba3a4737`. It ran from 20:43:20 to 20:44:02 UTC and completed successfully. The scientific child returned zero, its complete receipt passed $18/18$ gates, and the science was printed and saved before the publication-size check. This success is frozen.

## HSA1. Exact source, full mean and norm

Use the same objects as [CRA](R133-supplement-actual-complete-core-residual-restriction-and-selected-ordinary-source.md), [RH](R133-supplement-exact-selected-residual-frequency-bands-and-complete-known-high-forcing.md) and the [HS contract](../notes/2026-11-15-R133-known-core-high-source-and-negative-one-contract.md):
$$
 I_-=[0,L],\quad L=9/10,\quad d=10^{-10},\quad
 Q_\delta=Q_0+\delta Z,\quad \nu_\delta=\nu_0+\delta,\quad
 |\delta|\le d,\qquad
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta).
 \tag{HSA.1}
$$
The original $\eta_0$ is fixed. The exact centre and direction definitions remain
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.

The measure is ordinary $dr$ and the normalized original moving-circle measure $(2/\pi)d\phi$. The state norm is the complete two-component Euclidean norm. Both Fourier signs are retained. Set
$$
 n_j=4j,\qquad \Lambda_j=(1+16j^2)^{1/2},\qquad
 H_J=1-\Pi_{\le J}.
 \tag{HSA.2}
$$
The original low space has 96 odd and 97 even real coordinates, including the full even mean with weight one. That mean is retained in every complete original record and is removed only by an explicitly displayed $H_J$.

The source has already been converted to physical moving amplitudes. There is no further $\alpha$, $\sqrt2$, radial $P$, physical-angle composition or true-phase transformation. The exact continuous-$Z$ source already includes the raw mean and continuity offsets; they are not charged again.

## HSA2. Complete original inputs and the new scalar calculation

The new consumer read only eight immutable small current texts, of total size $156406$ bytes, and parsed two Python sources. Its five mathematical inputs are the CR science, CR execution, HS contract, RH support proof and ST continuation contract. It restored no original row, native container, archive or array.

The complete original inner-$Z$ full/low/high object, the independent high $97,\ldots,160$ record, the $D$ source, the $WL$ whole-core positive coefficient product, the saved quadratic contribution and both CR background choices are copied unchanged into the new science. Their entire nested objects were compared with CR after the run. The original CR gate inventory and its five-input identity chain were also compared exactly.

In particular, the ordinary source input
$$
 S_H\ge\|H_{96}s_0\|_{L^2(dr;L^2_\phi)},\qquad
 s_0=\mathcal F_\nu-(\partial_r-A_0)Z
 \tag{HSA.3}
$$
is the already completed `high97_through160.L2_L2_radial` record. It is not obtained by subtracting squared upper bounds. Its separately saved radial-supremum record remains present but is not substituted for the ordinary radial norm. The exact ordinary ball is:

`[1.1552729696177228953944813436940959820725773419132475681280993389431013575145154e-6 +/- 3.30e-86]`

The saved $E_d=(d/2)D_{\rm core}$ is read verbatim from CR. The actual source calculation does not repeat that multiplication or any original $D$, $Z$, $WL$, CR, Green or propagation target.

RH proves
$$
 \deg_\phi Q_0\le32,\quad \deg_\phi Z\le96,\quad
 \deg_\phi f_0\le96,\quad \deg_\phi s_0\le160,\quad
 \deg_\phi f_\delta\le288.
 \tag{HSA.4}
$$
For the cubic state argument, the radial coefficients are fixed at their actual $\nu_\delta$ first. Their dependence on $\delta$ in the intrinsic bump is retained; the whole-core family is not identified with a cubic polynomial in $\delta$.

Write $\mathsf B$ for the copied complete positive-algorithm bound on
$\sup_{I_-,|\delta|\le d}|\beta_\delta|\max(1,|K_\delta|)$. Using the already paid complete known-state bounds $7,6,19,83$, the only new coefficient combinations are
$$
 \begin{split}
 T_2&=\mathsf B\left(\frac{19^2\,6}{4}
       +\frac{7\,19\,83}{2}+3\,7\,19^2\right),\\
 T_3&=\mathsf B\left(\frac{19^2\,83}{4}+19^3\right).
 \end{split}\tag{HSA.5}
$$
All displayed balls in this report are copied verbatim from the successful science; their radii are retained.

| Quantity | Complete directed ball |
|---|---|
| $T_2$ | `[64525.0836409020568012797370765629488082264626559278967347907379178401385 +/- 3.56e-68]` |
| $T_3$ | `[67872.6593590407777147166036588776700381797157672556323244438785688701457 +/- 2.29e-68]` |
| $dS_H$ | `[1.15527296961772289539448134369409598207257734191324756812809933894310136e-16 +/- 2.49e-88]` |
| saved $E_d$ | `[2.16219514268118601346015690219221144174206236807112177913704404016450000e-16 +/- 6.09e-89]` |

## HSA3. All ordinary candidates and the actual choices

For $x=|\delta|$, the two independent complete arguments are
$$
 \begin{split}
 \|H_{96}f_\delta\|&\le xS_H+(x/d)^2E_d,\\
 \|H_{160}f_\delta\|&\le(x/d)^2E_d,\\
 \|H_{160}f_\delta\|&\le\sqrt L\,(x^2T_2+x^3T_3),\\
 \|H_{224}f_\delta\|&\le\sqrt L\,x^3T_3,\qquad H_{288}f_\delta=0.
 \end{split}\tag{HSA.6}
$$
These are ordinary $L^2(dr;L^2_\phi)$ bounds on the complete two-component source. The $H_{224}$ source also contracts from the complete $H_{160}$ bound. In particular, all three high sources vanish exactly at $\delta=0$.

The table retains every candidate evaluated at $x=d$. Each choice compares the outward upper endpoints of the final stored records, keeping the first candidate on a tie. Each candidate is a bound on the whole indicated norm.

| Threshold $J$ | Complete candidate | Complete directed ball | Choice |
|---|---|---|---|
| 96 | complete_original_high_linear_plus_saved_parameter_remainder | `[3.31746811229890890885463824588630742381463970998436934726514337910760136e-16 +/- 1.88e-88]` | selected |
| 160 | saved_complete_selected_parameter_remainder | `[2.16219514268118601346015690219221144174206236807112177913704404016450000e-16 +/- 6.09e-89]` | selected |
| 160 | complete_fixed_parameter_state_quadratic_and_cubic | `[6.12138691618751839182291259126512820951012507261148324577168219664004476e-16 +/- 3.41e-88]` | retained |
| 224 | complete_fixed_parameter_state_cubic | `[6.43896583281938770320413715636280727228164476580884610087931737777643922e-26 +/- 3.48e-98]` | selected |
| 224 | orthogonal_contraction_of_complete_H160 | `[2.16219514268118601346015690219221144174206236807112177913704404016450000e-16 +/- 6.09e-89]` | retained |

Thus the saved parameter remainder is sharper for $H_{160}$, whereas the independent cubic state argument is sharper for $H_{224}$. This comparison does not mix components or infer a shell norm from a difference of two upper bounds.

## HSA4. Exact shells and complete negative-one bounds

The only nonzero possible high shells are
$$
 97\le|j|\le160,\qquad161\le|j|\le224,\qquad225\le|j|\le288.
 \tag{HSA.7}
$$
Their exact physical frequency and Sobolev weights are:

| Shell | Minimum physical frequency | Exact $\Lambda_{\min}^2$ | Complete ordinary shell bound |
|---|---:|---:|---|
| $97,\ldots,160$ | $388$ | $150545$ | the selected complete $H_{96}$ bound |
| $161,\ldots,224$ | $644$ | $414737$ | the selected complete $H_{160}$ bound |
| $225,\ldots,288$ | $900$ | $810001$ | the selected complete $H_{224}$ bound |

Each shell bound follows by orthogonal contraction of its indicated tail. With $F_J$ denoting the selected ordinary bound, the direct and shell arguments give
$$
 \begin{split}
 \|H_Jf_\delta\|_{L^2(dr;H^{-1}_\phi)}
 &\le\frac{F_J}{\Lambda_{J+1}},\\
 \|H_Jf_\delta\|_{L^2(dr;H^{-1}_\phi)}
 &\le\left(\sum_{\substack{a\in\{97,161,225\}\\a>J}}
                   \frac{F_{a-1}^2}{\Lambda_a^2}\right)^{1/2}.
 \end{split}\tag{HSA.8}
$$
The second sum uses complete shells, not pointwise minima of contributions. The arithmetic implementation uses exact $\Lambda_a^2$ and an outward square root. It does not divide by an upper bound on $\Lambda_a$.

The complete actual candidates are:

| Threshold $J$ | Argument | Complete directed ball | Choice |
|---|---|---|---|
| 96 | direct tail | `[8.55014714970707005976769866740167251678269644697710474553415325376700124e-19 +/- 4.63e-91]` | selected |
| 96 | orthogonal shells | `[9.18571891018461823311106656069760250443540211937038355385514526490495286e-19 +/- 4.60e-91]` | retained |
| 160 | direct tail | `[3.35744182604544261919347755348161769949251952752271781043893955178221316e-19 +/- 4.15e-91]` | selected |
| 160 | orthogonal shells | `[3.35744182604544261926970444221738617446612072187109421277906319538052229e-19 +/- 1.95e-91]` | retained |
| 224 | direct tail | `[7.15440206461422308578190253439148217901459700328561700022947913630365288e-29 +/- 1.12e-101]` | selected |
| 224 | orthogonal shells | `[7.15440206461422308578190253439148217901459700328561700022947913630365288e-29 +/- 1.12e-101]` | retained |

The direct argument is selected at all three thresholds; the $J=224$ displayed records tie and the first-candidate rule applies. All three shell records, both candidates for each negative-one tail, their physical weights and both Fourier signs remain in the science.

For every $|\delta|\le d$,
$$
 \|H_{288}f_\delta\|_{L^2(dr;L^2_\phi)}
 =
 \|H_{288}f_\delta\|_{L^2(dr;H^{-1}_\phi)}
 =0.
 \tag{HSA.9}
$$
This is exact known-source support. It is not a bound on the high part of an unknown solution or a receiver output.

## HSA5. Precise ST input and remaining source separation

The [ST theorem](R133-supplement-complete-strict-tail-from-true-branch-cut-to-waist.md) has the actual radial interval
$$
 [0,r_c],\qquad
 r_c=\frac{76285779072683}{320000000000000}.
 \tag{HSA.10}
$$
Restriction of this same known source from $[0,L]$ to $[0,r_c]$ cannot increase any displayed norm. No interval-length scaling is used. The restriction is still in the original moving angle, with the physical frequency $4j$ and the same complete physical state-source convention.

ST.9 retains its own ordered $T(q)$, primitive and mean source channels. Its output includes both independent propagated means. A high input projection does not justify deleting those output means or commuting $H_J$ through the propagation.

No ST propagation gain, endpoint map or phase-coordinate map was evaluated in this run. The part of the core outside $[0,r_c]$ is not included in ST's domain. There is no transfer here to a physical-angle source, a true-phase source, or an $H^{-4/3}$ receiver. Such a transfer requires its own actual map and norms.

The original CR low193 ordinary source, including its complete mean, remains a separate input. Its full and low bounds, including the global fallback, remain in `complete_original_input_conclusion`; this run does not replace them by a high-source number.

## HSA6. Complete actual gates

Every gate below passed in the first scientific child. These gates certify the source identities, complete finite combinations and typed scope; they are not unknown-state, cap-entry, inverse or final-surface gates.

| Gate | Actual complete check | Result |
|---|---|---|
| 1 | pinned public runtime and 320-bit directed arithmetic | pass |
| 2 | current-only immutable manifest source parameters and all five small mathematical inputs | pass |
| 3 | original CR child and all eighteen complete structural gates succeeded | pass |
| 4 | original CR execution binds the exact saved science and same immutable successful run | pass |
| 5 | same continuous centre direction selected width moving angle and complete ordinary pair | pass |
| 6 | complete original Z D WL identity chain and old no-recomputation claims remain exact | pass |
| 7 | complete original high 97-through160 record is retained without squared-upper subtraction | pass |
| 8 | whole-core positive coefficient product and complete D source have the same selected width | pass |
| 9 | old complete quadratic and full low source records are copied rather than recomputed | pass |
| 10 | RH exact support and ST true subinterval use physical 4j in the original moving angle | pass |
| 11 | new fixed-parameter complete quadratic and cubic coefficients are finite and nonnegative | pass |
| 12 | H96 uses the complete original high source and the saved whole quadratic remainder | pass |
| 13 | H160 selects one complete valid candidate by its retained outward upper endpoint | pass |
| 14 | H224 keeps both complete candidates and source above 288 is exactly zero | pass |
| 15 | all three complete shells pay their exact physical-frequency negative-one factors | pass |
| 16 | every negative-one tail retains both complete candidates without receiver or phase substitution | pass |
| 17 | all original small bytes remain unchanged and no old scientific target is executed | pass |
| 18 | all eighteen gates describe known sources only with complete means and independent unknown inputs | pass |

The historical mixed-$Z$ failed-plan run `43612904296` and its successful finish `43613560173` remain recorded with the original plan and native hashes. The raw-mean and direction-offset completion is preserved. No historical failure or earlier coarse bound was overwritten.

## HSA7. Immutable scientific and publication receipts

The actual output paths below are relative to the topic root. The workflow path is relative to the repository root.

| Actual file | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [Science](../notes/known_core_high_source_negative_one_ci/run-43759656502-1/actual-scientific-conclusion.json) | `8291a32699db5d6a732194aa162a1d4414c66f23` | 21970 | `1da7f66a5587f5aab0847361107d5b5a85d0ab004b2b382d01be09a13aa7fec9` |
| [Execution](../notes/known_core_high_source_negative_one_ci/run-43759656502-1/execution.json) | `eeb9f08d012e266a1868a4a1d94e2ad1e55c6e7a` | 11432 | `2a397ac797947163e78f649d7fb5aa9798ab69b91da34fda5a2a17244dc5e800` |
| [Worker report](../notes/known_core_high_source_negative_one_ci/run-43759656502-1/actual-result.md) | `d080b9cf2c2ae00244526f4c9e6d499de74bd6e7` | 5634 | `8e640b8b881a193bee5eedb233b6bf2c207bf5ff8f6d751c18ffb457e1a632dc` |

The scientific source is
`scripts/fourfold_codazzi_known_core_high_source_and_negative_one.py`,
blob `68f2746820b0cfde3bd3af8bbf42ad6c2b30496f`,
$23007$ bytes,
SHA256 `a352961b0e3eb619d248fc4da0ee08e52cc96007a33226d56e9e275a85fd585b`.
The manifest is
`notes/2026-11-15-R133-known-core-high-source-and-negative-one-CI-inputs.json`,
blob `91f57106e9ee9dcfa48322c91cd884a433da0e47`,
$11709$ bytes,
SHA256 `8f2cdb5ee41bc5a65a0f75ccb981992e9b272dc8c68a1ece9d0f583a87147224`.

The worker is blob `22f1c5386aa962d7522f0e933bb49d22a04531d1`,
$48517$ bytes,
SHA256 `4f4f0fbff5dae6ed5f6b38115377b8cd47fc5eb9c55bc041d4edb670ba21c57c`.
The workflow is
`.github/workflows/visible-exact-known-core-high-source-negative-one.yml`,
blob `7f7a755866bc4f2c536a5f16238436747d9c6641`,
$4703$ bytes,
SHA256 `eabf8cee7ab0fd9c5c98d7efe5d1c391408419a6f6dd937d50143b8a0adc1168`.

The runtime was Python $3.12.14$, python-flint $0.9.0$, with $320$-bit directed arithmetic. The science's parameter object, source hash and all five mathematical input hashes agree with the immutable manifest. All eight actual input receipts agree with their pinned texts.

The complete science-and-report payload printed before Git publication is $27907$ bytes,
SHA256 `b8a9b7a67262bb4e12f31913621907c1f609a042596192715c51d4fb6436959c`.
It was independently reconstructed using the exact scientific JSON tokens and the report at that publication stage. The result matches byte count and hash. The execution separately records the prepublication process payload as $8850$ bytes with SHA256
`2358a514e4033ed2e3353873fcbfae01bf3153916bd08f3eb9b8b88a62ff8b43`;
this identity is not confused with the later final execution file.

The worker made the actual README pulls at 20:43:51.193378 UTC to
`fe4ec5cfcf01d252fe050aeb70da3e30c480733a`
and at 20:43:55.905610 UTC to
`e7e9aad184ff4c096bad13b53676933b1ad04bd6`.
Both reviewed README diffs were empty. The measured projected topic size was $199440880$ bytes; the publication passed the prescribed capacity check.

No old scientific producer, integral, source target, Green/Gram computation or propagation was repeated. No original binary or artifact was restored. No new array, artifact or Release was persisted.

## HSA8. Result available to subsequent work

The complete known-source ordinary and negative-one tails in HSA3--HSA4 are now actual inputs. A later receiver may consume them only in its matching original-angle source space and actual radial domain. The old ordinary low source and all means remain independent.

The nonlinear state, whole-core correction ball, actual cut trace, high-body and high-cut responses, physical curvature entry, complete boundary matching and final surface are not supplied by this source calculation. In particular, the small known high forcing is not substituted for any unknown high-state bound in NF, SR, VR or NG.
