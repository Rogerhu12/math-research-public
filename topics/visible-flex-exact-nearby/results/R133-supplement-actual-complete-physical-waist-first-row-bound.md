# R133 supplement: actual complete physical waist first-row bound

2026-11-16, visible-exact / tail_connector.

**Actual success, with one new scientific child and no repeated old target.** Public push run [43803459418/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43803459418) completed the nine new scalar records specified by [WAD.32--36](R133-supplement-complete-adjoint-physical-waist-row-and-saved-first-row-receiver.md). All 16 gates passed. The complete new first-row candidate was selected over the saved whole-state candidate.

The selected outward record is
`[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]`.

Here and below, the upper endpoint of an entire displayed ball is the sufficient upper bound. Its midpoint alone is not used. This result bounds the same reflected natural-root input to the original raw moving-angle primitive waist row. It does not assert a small-perturbation gate, an incoming or finite Schur inverse, a signed-adjoint cancellation certificate, or a numerical bound in WPL's different normalization.

## WADA1. Exact target and conclusion

Retain the full repaired family, original terminal-Ai reference, fixed intrinsic parameter $\eta_0$, and selected parameter of WAD and SW. The characteristic coefficient $\eta(r)=-\gamma(r)\langle v(r)\rangle$ is distinct from $\eta_0$. Let
$$
 r_c=\frac{76285779072683}{320000000000000},\qquad
 J_c=97,\qquad J_s=268435456.
 \tag{WADA.1}
$$
The original moving angle has period $\pi/2$, normalized angular measure and physical frequencies $n=4|j|$. The volume measure is the actual ordinary $dr$ on $[0,r_c]$.

With the same exact homogeneous reference state $Y_A$ and the same compressed single-symbol trial $Y_{W,J}$ as WAD, put
$$
 E_\partial=\mathcal B_\partial Q_{\mathcal R}(Y_A-Y_{W,J}),
 \qquad
 \mathcal B_\partial(y_+,y_-;z_+,z_-)
                  =\frac{y_++y_-}{\sqrt2}.
 \tag{WADA.2}
$$
The completed assertion is
$$
 \|E_\partial\|_{\mathcal H_{\rm nat,\,|j|\ge97}^{-4/3}
                      \longrightarrow L^2_{\rm even,0}}
       \le C_\partial^\# ,
 \tag{WADA.3}
$$
where $C_\partial^\#$ is the upper endpoint of the selected record above. The physical reflection constraint is the original natural one. No full signed-circle extension or different high-input space is inferred.

The density state is $(I w,\Pi w)$ with $w=n_gT(q)h$. Consequently the precise primitive row in (WADA.2) equals
$$
 \mathcal B_\partial(Iw,\Pi w)
       =\frac{n_g(0)}{\sqrt{q(0)}}\,Ih_1 .
 \tag{WADA.4}
$$
The name “raw moving-angle primitive row” in the receipt specifies the angle and row realization, not a deletion of this factor. A bound for the unscaled $Ih_1$ would require the separately saved waist input factor once. Reconstructing $h_1$ by differentiation gives an $H^{-1}$ readout, not a free $L^2$ derivative bound.

The uniform ST coefficient and propagation input has real radius $10^{-8}$. The present same-trial result retains SW's selected common-angle qualification
$|\delta_*|\le0.00000000009368259853002$. Reading a uniform propagation input does not extend a selected SW assertion to a different parameter. The continuous centre and response definition hashes remain
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` and `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`, respectively.

## WADA2. Unique execution and immutable result files

The event was a natural push, not a workflow dispatch. The event head and the actual checked-out scientific commit are recorded separately.

| Item | Exact recorded value |
|---|---|
| Run / attempt | `43803459418/1` |
| Workflow event head | `6433bd5fe4cf2b56925ace506699621f9453b93f` |
| Actual scientific checkout | `7d7ce88415ed4a23e73ee49abaa1d3c059379a37` |
| Workflow | `.github/workflows/visible-exact-physical-waist-first-row-receiver.yml` |
| Job | `133088756006` |
| Run created / last API update | `2026-11-16T04:19:59Z` / `2026-11-16T04:20:38Z` |
| Job status / conclusion | completed / success |
| Job steps | 12 recorded, each completed with success |
| Scientific runtime | Python 3.12.14; python-flint 0.9.0; 320 bits |
| New scientific child processes | 1 |
| Actual child return code | 0 |
| Complete / proved / stage | true / true / complete |
| Old scientific source calls / successful targets recomputed | 0 / 0 |
| Current small input files / Python AST files / mathematical roles | 7 / 3 / 4 |

The exact result directory is
`notes/physical_waist_first_row_receiver_ci/run-43803459418-1/`.

| Result file | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| `actual-scientific-conclusion.json` | `7cc6acb1023bb9fc110f8fcd4d436da51d6b917a` | 29708 | `77d17dad4d55fb5d7cc7d8b146eabf0f1ac6073e0195a64a841f93ff5905f4b5` |
| `execution.json` | `a841f7d3091ae5276fe0c7f25bd61222d712aa6c` | 11226 | `588b9c7304df609cd140f6acb3faa551c31b809019c6c7dab20d7ba3a102ca4d` |
| `actual-result.md` | `b9fea14dcb71d3e1d412657191fcb8d881d056ed` | 4018 | `0a2eb04220362e34c9088b176f673fe51fa995d77fddb0bb816f62ff886f0581` |

All three files were fetched independently as complete small UTF8 texts and their byte lengths and SHA256 values were checked. The scientific JSON has exactly 32 top-level fields. Its entire canonical byte sequence equals the published 29,708-byte file. The complete new scalar graphs are retained; the result is not reconstructed from rounded prose.

The immutable source and wrapper are the exact ones reviewed before this run. The manifest and workflow identities are:

| Item | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Manifest | `50088f4e3b925b60ffe062358ccc1577b4039b96` | 12910 | `a0c625e411fdaeda94935da07540f9bdc8b6ad10f8fb7116f53444c6d28425e9` |
| Workflow | `f60c8c298d1df416c0408ec384cfe2b1e36ec020` | 4783 | `9b1a3c1f95badcbb39f8b3faf2461c7d07602fcec37cd9a0ca954412d9d18784` |

## WADA3. Complete current input closure

The seven current inputs total exactly 250,616 bytes. They are the following immutable texts; no history, binary, old artifact or native array was restored.

| Role and topic-relative path | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| `source` — `scripts/fourfold_codazzi_physical_waist_first_row_receiver.py` | `8cd75a860b37ca4d22e63851dc69bc3d9401db8e` | 32693 | `437b69ea0d6790d2880b381e6747f2ced0da86a35ded73767886ded1657a1684` |
| `worker` — `scripts/fourfold_codazzi_physical_waist_first_row_public_worker.py` | `8f9d482f560d9c16ef6c79c30594554c70b3349e` | 62016 | `c4f211cdaa63b5ead89343d96efe61c3a496fe4cb9f33e9ca65aac4fe9cb0656` |
| `rules` — `notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json` | `5c5d020913d717bb5bc8ce891297e00eaa8944f7` | 2461 | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |
| `contract` — `results/R133-supplement-complete-adjoint-physical-waist-row-and-saved-first-row-receiver.md` | `1dfa6d56a249157b27d23d6249fb451cb9fdb6d0` | 28366 | `0a92e2e5e5c1f0e1e93bc509ad5883d20630ad9909be3b33eaff7546f641702a` |
| `st_execution` — `notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json` | `94eb4c7d643edc33f696d101753e4d23a7936a26` | 47282 | `b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637` |
| `sw_science` — `notes/single_root_first_symbol_trial_ci/run-43781399696-1/actual-scientific-conclusion.json` | `3dbcf931b1b98fb7a7822ef5c1ed7df10135b894` | 27687 | `f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659` |
| `st_source` — `scripts/fourfold_codazzi_strict_tail_true_cut_to_waist.py` | `e47bdce4d3716b800f6282be6a45cc3323b8119b` | 50111 | `743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5` |

The four mathematical roles are contract, ST execution, SW science and ST source. The manifest is checked separately by its own SHA256. The three Python files were parsed as a complete immutable AST closure before the new child. The original ST source was read for its positive-algorithm identity and was never imported or called.

The actual seven-file receipt inventory has canonical SHA256
`a029868d72d4f38b7a2a25c4d8560fc990e24267019642341f6209f6d4f4e9de`.
The three-file AST inventory has canonical SHA256
`165682457ab268ac90a0cd3fda2b0b2144fcd4e71437c8a31e7c2adfb1a131a0`.

The old ST receipt is run 43757644616/1, with its own **25** complete gates. The old SW science is run 43781399696/1, with its distinct **24** complete gates. Their kinds, original source hashes, original manifest hashes, runtimes, completion flags and return codes were compared to the original records. The new 16-gate schema is not substituted for either original schema. The complete accepted identity object is retained in Appendix B.

## WADA4. The four new first-row gain records

The saved positive ST reverse matrix acts on the ungauged two-component norm vector
$$
 Y=\sqrt q\,\|I\,T(q)h\|_2,\qquad
 Z=\sqrt q\,|\Pi T(q)h|.
 \tag{WADA.5}
$$
Its first row is read directly. The second row is still present in the copied complete positive-propagation object. No component is inferred from a whole Frobenius bound. The original positive construction retains all shorter ordered products and source insertions.

Read the original upper records $m_{11},m_{12},O_0,I_c,J_*$, with
$$
 O_0\ge\frac{n_g(0)}{\sqrt{q(0)}},\qquad
 I_c\ge\frac{\sqrt{q(r_c)}}{n_g(r_c)},\qquad
 J_*\ge\sup_{[0,r_c]}\sqrt q .
 \tag{WADA.6}
$$
The last qualification is the original ST positive-source construction, including the full prefix. No denominator lower bound is recovered by dividing an upper bound.

The unique new child formed
$$
 \begin{aligned}
 r_1&=\sqrt{m_{11}^2+m_{12}^2},&
 g_c&=O_0I_c r_1,\\
 g_y&=O_0J_*m_{11},&
 g_z&=O_0J_*m_{12}.
 \end{aligned}
 \tag{WADA.7}
$$
Each original matrix entry is first replaced by its complete upper endpoint. The source uses multiplication for each square and an outward square root. The exact saved records are:

| Symbol | Field in complete_new_first_row_gain_conclusion | Complete outward record |
|---|---|---|
| `r_1` | `complete_first_matrix_row_L2_upper` | `[188.432913268467968358875795246164698642503509985045809808829091554700833 +/- 4.32e-70]` |
| `g_c` | `complete_density_cut_row_gain_upper` | `[25.1716699151329125544412692036391961187725820720351296329671295047140499 +/- 3.41e-71]` |
| `g_y` | `complete_ungauged_primitive_row_gain_upper` | `[204.159653834300462612406113807938615827913665301580648191544296000342776 +/- 1.30e-70]` |
| `g_z` | `complete_ungauged_mean_row_gain_upper` | `[39.0656638395227706895560719439749728116223385221487756487002935658404962 +/- 3.81e-71]` |

The cut gain receives a complete density cut error. The other two gains receive an ungauged primitive or complete mean source. A point impulse receives the same gain without a radial-length factor. The old SW volume-source bounds are already ordinary $L^1(dr)$ budgets, so no new length or square-root-length is inserted.

The $m_{12}$ column remains in (WADA.7). Reflection does not permit deletion of the propagated even mean, and the two physical mean slots in the original full system remain recorded.

## WADA5. Complete new candidate and actual whole selection

Write the complete saved ordinary budgets as
$F_{\rm lead}^\#,F_{\mathcal Q}^\#,F_{\rm mean}^\#,J_y^\#$,
and retain the complete density cut upper $E_c^\#$ and complete physical waist correction $E_0^\#$. The new expressions are
$$
 \begin{aligned}
 C_{\rm cut}&=g_c E_c^\#,\\
 C_{\rm primitive}&=g_y(F_{\rm lead}^\#+F_{\mathcal Q}^\#),\\
 C_{\rm mean}&=g_zF_{\rm mean}^\#,\\
 C_{\rm jump}&=g_yJ_y^\#,\\
 C_{\partial,1}&=C_{\rm PC}+C_{\rm ST4}
        +C_{\rm cut}+C_{\rm primitive}+C_{\rm mean}
        +C_{\rm jump}+E_0^\# .
 \end{aligned}
 \tag{WADA.8}
$$
This is precisely the complete WAD.35 candidate. The full $\mathcal Q$ record contains $Q,F_0,F_1,T_1F_2$. All 3070 jumps are present: 2549 genuine locations and 521 conservative artificial locations. Their complete saved sum has no additional $dr$ factor. The waist record already includes its single $n_g(0)$ factor.

| Symbol | Field in complete_new_whole_row_candidate_conclusion | Complete outward record |
|---|---|---|
| `C_cut` | `complete_cut_contribution_upper` | `[2736068400045373073430725520115824623463042027546.96382038149626170636211 +/- 1.18e-24]` |
| `C_primitive` | `complete_primitive_source_contribution_upper` | `[4.74811985701985644655978079913349647844946763054638092045674772948381287e+83 +/- 7.40e+10]` |
| `C_mean` | `complete_independent_mean_source_contribution_upper` | `[6.78742861532309053328839023271334669171345937891697481975991900494226807e+79 +/- 9.17e+6]` |
| `C_jump` | `complete_all_3070_interface_contribution_upper` | `[5322085697206910450627411811246732244263668509901801959902435955353323.89 +/- 3.37e-3]` |
| `C_partial,1` | `complete_first_row_candidate_upper` | `[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]` |

The same-trial old whole-state bound is independently an upper bound for (WADA.2), because the physical row and reflection projection are contractions in the original complete density state. Both complete candidates were serialized and retained before comparison.

| Index | Candidate | Entire retained upper record |
|---:|---|---|
| 0 | `saved_old_complete_Cstar` | `[7.05994136031959095363926517592982151842539431001952856359080309257433083e+83 +/- 8.01e+10]` |
| 1 | `new_complete_first_row_candidate` | `[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]` |

The actual selection has index **1**, label
`new_complete_first_row_candidate`,
and
`new_candidate_upper_strictly_smaller=true`.
The selected complete record is byte-for-byte the new candidate record. The old candidate wins a tie. Both
`entrywise_minimum_used` and `different_trial_or_different_output_unit_minimum_used` are false.

No old total was reduced by subtracting an upper bound. No source summand was chosen independently from another candidate. Neither a different full-$T$ trial nor a coefficient-only or differently normalized estimate entered this minimum.

**Proof of (WADA.3).** The complete actual error tuple is the WAD.26 tuple: the AW/PC-ST4 bracket, the original full density cut discrepancy, the complete ordinary source, all trial impulses, and the waist $F_TW$ correction. WAD.29--33 bound each contribution to its first physical primitive row by (WADA.7), with the true radial coordinate factors and the complete mean column. WAD.35 therefore gives the new whole upper (WADA.8). WAD.36 admits the old whole-state upper for exactly the same row and trial. The actual outward comparison selects one entire sufficient upper, proving (WADA.3). This proof reads the new saved records; it does not repeat their arithmetic.

## WADA6. All fourteen original records, copied literally

In the exact paths below, $S$ denotes the original ST execution's
`actual_scientific_receipt`,
and $W$ denotes the original SW scientific JSON. The two original files and their hashes are in WADA3.

| Original symbol | Exact original JSON path |
|---|---|
| `m11` | `S.complete_new_strict_propagation_conclusion.complete_reverse_matrix[0][0]` |
| `m12` | `S.complete_new_strict_propagation_conclusion.complete_reverse_matrix[0][1]` |
| `O0` | `S.complete_endpoint_and_source_conclusion.waist_output_factor` |
| `Ic` | `S.complete_endpoint_and_source_conclusion.cut_input_factor` |
| `Jstar` | `S.complete_endpoint_and_source_conclusion.complete_source_injection_upper` |
| `Flead` | `W.complete_new_source_and_interface_conclusion.complete_ordinary_leading_defect_L1_upper` |
| `FQ` | `W.complete_new_source_and_interface_conclusion.complete_ordinary_Q_F0_F1_T1F2_L1_upper` |
| `Fmean` | `W.complete_new_source_and_interface_conclusion.complete_ordinary_independent_mean_L1_upper` |
| `Jy` | `W.complete_new_source_and_interface_conclusion.complete_all_interface_impulses_upper` |
| `Ecut` | `W.complete_new_full_and_compressed_trial_conclusion.original_fullT_cut_error_read_verbatim` |
| `Ewaist` | `W.complete_new_full_and_compressed_trial_conclusion.complete_physical_waist_FT_W_correction_upper` |
| `C_PC` | `W.copied_complete_scalar_inputs_read_verbatim.C_PC` |
| `C_ST4` | `W.copied_complete_scalar_inputs_read_verbatim.C_ST4` |
| `Cold` | `W.complete_new_ordered_paid_conclusion.complete_Cstar_singleW_upper` |

| Original symbol | Complete saved ball, unchanged |
|---|---|
| `m11` | `[185.0751745325951770396074382417460543669648347869247 +/- 3.95e-50]` |
| `m12` | `[35.41387545258786435202220073980917616836528283484184 +/- 3.88e-51]` |
| `O0` | `[1.039997532916801925720475226447926064508270286842373 +/- 9.19e-54]` |
| `Ic` | `[0.1284467015892411290166196957202694739508333804424883 +/- 1.01e-53]` |
| `Jstar` | `[1.060692368019358917200479394016357116911461949707612 +/- 4.22e-52]` |
| `Flead` | `[1.39125528787585232356039646242549455101209454401411572353052660018434744e+75 +/- 4.07e+3]` |
| `FQ` | `[2.32568821873666154790001953071109290090672851761327897392605182256721628e+81 +/- 7.06e+8]` |
| `Fmean` | `[1.73744100271918131327852495430241667068211546348222966022823843693667448e+78 +/- 3.97e+6]` |
| `Jy` | `[26068253924090251771055095541078778509210288709213647765609021158428.0753 +/- 4.17e-5]` |
| `Ecut` | `[108696340340951351029091710450393091694320015823.775959403613733467161487 +/- 2.79e-26]` |
| `Ewaist` | `[3.42739034160440778168038604016822220168975407915791350551389662598981006e+71 +/- 0.209]` |
| `C_PC` | `[1018227964328341484881354948482360.900886437770295542 +/- 1.43e-19]` |
| `C_ST4` | `[285704814464526022070.2591010762034890706384188211054 +/- 2.24e-33]` |
| `Cold` | `[7.05994136031959095363926517592982151842539431001952856359080309257433083e+83 +/- 8.01e+10]` |

The complete fourteen-record object has canonical size **1370 bytes** and SHA256
`070b718bed4a386dea25f0570c17a8573e8d1f33befea4edb81db9ebf0d4dc66`.
Every path was independently compared to the corresponding original successful receipt. The copied object also equals the exact pre-execution model; no scalar has been replaced by a displayed midpoint or a reconstructed value.

The nine whole scope objects in Appendix A have canonical size **17,163 bytes** and SHA256
`fa01be532e31dc611aaf858b505115afb2596120f54de30de59ddb4b537ddec7`.
They were compared both to the original ST/SW objects and to the frozen model. Keeping their complete old matrix and source records is preservation of already completed small conclusions, not a new matrix or source calculation.

## WADA7. All sixteen actual gates

| Gate | Exact recorded condition | Passed |
|---:|---|---|
| 1 | public runtime and exact 320-bit arithmetic with actual workflow and checkout identities | true |
| 2 | four exact current mathematical texts and their complete manifest closure are frozen | true |
| 3 | only bounded current UTF8 JSON proof and source texts are read with no archive or old import | true |
| 4 | original ST execution and its complete embedded science retain all 25 original gates | true |
| 5 | original SW complete science retains its distinct 24-gate schema and same successful target | true |
| 6 | same repaired real family cut selected parameter root input and original normalizer remain typed | true |
| 7 | saved complete reverse matrix contains both means and every shorter ordered source insertion | true |
| 8 | original positive algorithm and exact row proof are only read with true radial endpoint and source directions | true |
| 9 | SW separately saved primitive full Q mean and all interfaces refer to the same complete compressed trial | true |
| 10 | fourteen entire old scalar records and nine whole scope objects are copied literally with finite positive budgets | true |
| 11 | four new first-row scalar records retain cut density and separate ungauged primitive mean source units | true |
| 12 | the complete new candidate sums all four physical contributions PC ST4 and the one saved waist correction | true |
| 13 | only final serialized complete same-row uppers are compared with the old complete record retained on a tie | true |
| 14 | all fourteen old balls nine scopes and all independent physical obligations remain unchanged | true |
| 15 | every old mathematical byte and the actual manifest still have their original exact hashes | true |
| 16 | all sixteen gates nine new scalar records and the complete 32-field small schema retain their declared scope | true |

The actual progress object has **12 fields**, preserved in Appendix B. In particular it records two original receipts read, 14 complete scalar records copied, nine complete scope objects copied, one completed gain graph with four scalar records, one completed candidate graph with five scalar records, and one completed whole selection. The final read-only input-check count is five: the four mathematical roles and the actual manifest. The counts of old source calls and old successful scientific targets recomputed are both zero.

A structural success does not certify every later mathematical gate. The actual scope keeps the signed-adjoint numerical certificate, raw derivative readout, physical leading square inverse, full incoming inverse, finite Schur inverse, whole return $R_0$, nonlinear background and final surface flags false.

## WADA8. Preservation and publication audit

The complete scientific file was written atomically and printed before format or publication guards. The wrapper reprinted the full atomic scientific result and retained the complete child stdout. The execution's exact preservation records are:

| Preserved item | Bytes | SHA256 |
|---|---:|---|
| Complete child scientific JSON | 29708 | `77d17dad4d55fb5d7cc7d8b146eabf0f1ac6073e0195a64a841f93ff5905f4b5` |
| Complete scientific child stdout | 29899 | `6c1d76f78035646d302a88153d5753d925c8e9ebe5abbb2df3f36aa6e897e40f` |
| Complete prepublication science/report payload | 34123 | `e83934d0567014cb7540ae33e36d37b49d49d1295833f79a2b1b76bf2350beb7` |
| Independent execution prepublication payload | 8646 | `2eb348789665e4eb31d44a1330a1585d75fda2e07601191483e3a0ea6b4e72b2` |

These prepublication identities are recorded by the immutable worker and actual execution. The published science itself was independently checked to have its original canonical bytes. No whole job log or large binary was fetched for this note.

Both recorded README checks followed actual Git pulls. Both have empty diffs and preserve these exact reviewed hashes:

| README | SHA256 |
|---|---|
| `README.md` | `6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9` |
| `topics/visible-flex-exact-nearby/README.md` | `81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220` |

The two pull checks are at `2026-11-16T04:20:28.223901+00:00` and `2026-11-16T04:20:32.298647+00:00`, at actual commit
`7d7ce88415ed4a23e73ee49abaa1d3c059379a37`.
The live rule index and complete capacity inventory were read from that actual state.

The complete output sizes are below their respective hard limits: science 29,708 of 75,000 bytes, report 4018 of 8000, prepublication science/report 34,123 of 90,000, execution 11,226 of 59,000. The pre-science reserve is 150,000 bytes. Publication started from **199,700,442** topic bytes and the execution records the exact projected **199,745,394** bytes after the three owned outputs. The only published outputs of the scientific job are the three files in WADA2.

The execution records zero old artifacts downloaded, zero binary parts restored, zero old numerical enclosures, old producers or integrals, old exponentials or logarithms, old flow/root/Airy calculations, and old coordinate/leading calculations recomputed. It also records zero new artifacts and zero Releases. No new reproducible per-row array persists.

The pre-run static model was a serialization audit, not a scientific result. It retained all 32 fields, old complete objects, nine new scalar slots and both complete candidate records. Its final small budget receipt is
`898a529f981d2f97b8ccbe2e395949204d0febba`, 9089 bytes, SHA256 `3ca3b69b94f56c6f71df11725708cb1c9da54623b14805b78116c8dbe35dec38`.
The actual smaller records replace no old evidence and authorize no repeat of this completed target.

## WADA9. Exact remaining scope

The new first-row bound is a complete positive bound. It is not a numerical evaluation of the signed adjoint sum of WAD.28. The latter still requires a certificate for every admissible dual datum, the full angular complement, the original coefficient pieces, complete even-mean dual column, both endpoints and all 3070 interfaces.

All ordinary source contributions, both physical mean slots, the actual even-mean equation, amplitude and true metric-parameter row, radial head, independent second-reference or PW inputs, finite matching rows and cross blocks remain as required by their original domains. The reflected redundancy of the raw odd first-row mean does not remove the even mean or amplitude data.

The WPL selected-coordinate state row is, symbolically and in the original order,
$$
 \frac1{\sqrt2}\,U_{\mathcal H^{-1}}E_\partial N_i .
 \tag{WADA.9}
$$
No new numerical left density or right input-coordinate multiplication is made here. Its leading row must undergo the same coordinate change. There is no additional WT inverse in this particular readout, and a coordinate isomorphism cannot remove an interior source.

The old ST and SW successes and this one new WAD success are frozen. This proof performs only source audit, exact copying, canonical hashing and analytic identification of the saved conclusion.

## Appendix A. All nine original scope objects

The following object is the complete original copied scope object, with every mean, matrix, source and endpoint qualification retained. Canonical compact JSON with a final newline has the exact 17,163-byte identity stated in WADA6.

```json
{
  "ST_complete_endpoint_and_source": {
    "affine_impulse_is_a_raw_state_jump_not_a_density_jump": true,
    "affine_impulses_have_no_radial_length_factor": true,
    "affine_raw_state_jump_to_raw_cut_density_upper": {
      "ball": "[49.65065419752953029564292873868667048669500725359082 +/- 4.16e-51]"
    },
    "affine_raw_state_jump_to_waist_density_upper": {
      "ball": "[303.3367407712688206758072680976046671055110227440295 +/- 1.17e-50]"
    },
    "both_independent_means_and_complete_finite_blocks_retained": true,
    "complete_new_cut_absolute_mean_upper": {
      "ball": "[1.119757777425368108015867372481352713298498882782617 +/- 2.75e-52]"
    },
    "complete_new_cut_ng_lower": {
      "ball": "[0.9599548695266653840650933988066207983966154782959841 +/- 4.54e-53]"
    },
    "complete_new_cut_physical_radius_lower": {
      "ball": "[1.097108287143454652401430848840391263368828152229148 +/- 2.49e-52]"
    },
    "complete_new_tail_source_injection_upper": {
      "ball": "[1.030776406404415137455352463993519256286799806343405 +/- 1.10e-52]"
    },
    "complete_raw_cut_to_waist_density_upper": {
      "ball": "[36.73318013558955353160134784914924794029878928743332 +/- 4.18e-51]"
    },
    "complete_source_injection_upper": {
      "ball": "[1.060692368019358917200479394016357116911461949707612 +/- 4.22e-52]"
    },
    "complete_waist_to_raw_cut_density_upper": {
      "ball": "[45.02650184508654924873396851481709324057609004445807 +/- 1.42e-51]"
    },
    "cut_input_factor": {
      "ball": "[0.1284467015892411290166196957202694739508333804424883 +/- 1.01e-53]"
    },
    "cut_output_factor": {
      "ball": "[7.834187101286307687304344973961189376644653945502396 +/- 2.79e-52]"
    },
    "density_impulses_require_their_own_radial_entry_factor": true,
    "exact_full_radial_length": "76285779072683/320000000000000",
    "old_N_radius_1over200_not_moved_to_the_true_cut": true,
    "saved_TC_L2_density_read_verbatim": {
      "ball": "[1.000000684576802559025927739507150912467809335811206 +/- 2.55e-52]"
    },
    "saved_TC_L2_inverse_density_read_verbatim": {
      "ball": "[1.000000684577739851106428559523941257366292837918195 +/- 3.63e-52]"
    },
    "saved_TN_L2_forward_normalizer_read_verbatim": {
      "ball": "[1.001669649816389437916461198297920696771426256888629 +/- 1.08e-52]"
    },
    "saved_TN_L2_inverse_normalizer_read_verbatim": {
      "ball": "[1.001672387764244768693237132423321294220230365454558 +/- 3.00e-53]"
    },
    "saved_complete_cut_ng_upper_read_verbatim": {
      "ball": "[0.9599802235196803377895035292146442136698495710352981 +/- 1.85e-53]"
    },
    "saved_prefix_source_injection_read_verbatim": {
      "ball": "[1.060692368019358917200479394016357116911461949707611578132153810 +/- 4.80e-64]"
    },
    "strict_L1_Hminus1_source_to_raw_cut_density_upper": {
      "ball": "[49.65065419752953029564292873868667048669500725359082 +/- 4.16e-51]"
    },
    "strict_L1_Hminus1_source_to_true_phase_normalized_cut_upper": {
      "ball": "[49.73372339067287248533501733589547794551664011065138 +/- 1.28e-51]"
    },
    "strict_L1_Hminus1_source_to_waist_density_upper": {
      "ball": "[303.3367407712688206758072680976046671055110227440295 +/- 1.17e-50]"
    },
    "strict_L2_Hminus1_source_to_raw_cut_density_upper": {
      "ball": "[24.24218599088885916654346852568581238767884438637571 +/- 3.10e-51]"
    },
    "strict_L2_Hminus1_source_to_true_phase_normalized_cut_upper": {
      "ball": "[24.28274494953384255097357750369687835361390105011107 +/- 6.67e-52]"
    },
    "strict_L2_Hminus1_source_to_waist_density_upper": {
      "ball": "[148.1057159567703969146927049489537130817999309856401 +/- 3.47e-50]"
    },
    "true_phase_normalized_cut_to_waist_upper": {
      "ball": "[36.79453687172750048664644452948271772394949658495257 +/- 2.24e-51]"
    },
    "volume_source_window": "L1 or L2 true dr with full H^(-1) moving-circle state",
    "waist_input_factor": {
      "ball": "[0.9619060944431472420235047833379563700408296156189220 +/- 2.11e-53]"
    },
    "waist_output_factor": {
      "ball": "[1.039997532916801925720475226447926064508270286842373 +/- 9.19e-54]"
    },
    "waist_to_true_phase_normalized_cut_upper": {
      "ball": "[45.10183449152979903476969312514776900165583207813093 +/- 2.74e-51]"
    }
  },
  "ST_complete_family_identity": {
    "complete_original_eta_enclosures_restricted_without_recomputation": true,
    "continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_response_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "exact_alpha": "6890507429876859/9007199254740992",
    "exact_nu_centre": "-2572625729470897/72057594037927936",
    "exact_selected_nu_interval": [
      "-1004932207049545851281/28147497671065600000000",
      "-1004931644099592429969/28147497671065600000000"
    ],
    "fixed_current_eta": "eta_0",
    "original_candidate_sha256": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    "original_eta_half_width": "1/1000000000",
    "original_object_sha256": "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
  },
  "ST_complete_parameter_scope": {
    "arithmetic_bits": 320,
    "canonical_response_pair_A0": "19",
    "canonical_response_pair_angle_A0": "83",
    "complete_mean_coordinates": 2,
    "density_state": "(I*w,mean(w)), w=(a_phys^2/m^2)*T(q)*h",
    "exact_centre_repair_A0": "0.000000000000000003861",
    "exact_centre_repair_angle_A0": "0.00000000000000001970",
    "exact_compact_support": [
      "1/20",
      "9/50"
    ],
    "exact_old_strict_cut": "2333968743003/10000000000000",
    "exact_original_strict_endpoint": "1191939371497/5000000000000",
    "exact_real_delta_radius": "1/100000000",
    "exact_root_interval": [
      "1191984371497/5000000000000",
      "2383968743003/10000000000000"
    ],
    "exact_true_branch_cut": "76285779072683/320000000000000",
    "expected_actual_gate_count": 25,
    "exponential_scaled_row_norm_upper": "1/4",
    "exponential_series_degree": 18,
    "fixed_intrinsic_parameter": "eta_0",
    "full_incoming_or_high_BVP_or_return_R0_claimed": false,
    "new_body_norm_forcing_archives_restored": 0,
    "old_successful_scientific_calls_allowed": 0,
    "original_final_body_row": 3070,
    "original_final_norm_row": 790,
    "original_old_cut_row": 2803,
    "original_parameter_half_width": "1/1000000000",
    "original_strict_complete_rows": 3071,
    "original_strict_container_parts": 5,
    "physical_column_input": "H^(-4/3), both reference columns and both signs |j|>=97",
    "physical_column_output": "waist old-circle L2 density pair plus two independent means",
    "physical_frequency": "n=4|j|",
    "strict_state": "sqrt(q)*(L2 norm of I*T(q)*h, Euclidean norm of mean(T(q)*h))"
  },
  "ST_complete_positive_propagation": {
    "all_shorter_ordered_subproducts_and_affine_insertions_retained": true,
    "complete_both_mean_and_all_Fourier_coordinates_retained": true,
    "complete_final_tail_forward_exponential": [
      [
        {
          "ball": "[1.000007515928206131906625643594779790043441461139945 +/- 3.57e-52]"
        },
        {
          "ball": "[4.713366107649632359842179468210934803820796182213217e-6 +/- 2.47e-58]"
        }
      ],
      [
        {
          "ball": "[1.874745179132572495225763004502573635401113742824078e-5 +/- 3.81e-57]"
        },
        {
          "ball": "[1.000003481784826560764151782001327734779849178399787 +/- 1.48e-52]"
        }
      ]
    ],
    "complete_final_tail_reverse_exponential": [
      [
        {
          "ball": "[1.000007515928206131906625643594779790043441461139945 +/- 3.57e-52]"
        },
        {
          "ball": "[4.713366107649632359842179468210934803820796182213217e-6 +/- 2.47e-58]"
        }
      ],
      [
        {
          "ball": "[1.874745179132572495225763004502573635401113742824078e-5 +/- 3.81e-57]"
        },
        {
          "ball": "[1.000003481784826560764151782001327734779849178399787 +/- 1.48e-52]"
        }
      ]
    ],
    "complete_first_tail_forward_product": [
      [
        {
          "ball": "[1.009941599161915184226630862101540538726303424980391 +/- 1.75e-52]"
        },
        {
          "ball": "[0.004954919746548073910565364128511323266766231005879868 +/- 9.55e-56]"
        }
      ],
      [
        {
          "ball": "[0.02352109272714036325319381981586191432971315177907831 +/- 6.74e-55]"
        },
        {
          "ball": "[1.004573067457923470897239805677146630849859808412816 +/- 1.49e-52]"
        }
      ]
    ],
    "complete_first_tail_reverse_product": [
      [
        {
          "ball": "[1.008545894832801356257797362314995234542699764168888 +/- 1.66e-53]"
        },
        {
          "ball": "[0.004950105688588079880958375211822434220942850480099428 +/- 3.62e-55]"
        }
      ],
      [
        {
          "ball": "[0.02348730229538864122749248502503590391255612316273925 +/- 1.86e-54]"
        },
        {
          "ball": "[1.003199547757263117610970591670068015117576853052770 +/- 4.03e-52]"
        }
      ]
    ],
    "complete_forward_matrix": [
      [
        {
          "ball": "[3.890127491431193495577063915964570269488878611507963 +/- 2.66e-52]"
        },
        {
          "ball": "[0.8055727435692119907405490359664115238931488518212950 +/- 3.98e-54]"
        }
      ],
      [
        {
          "ball": "[2.967836825742209459702833534151305932153941436676732 +/- 3.60e-52]"
        },
        {
          "ball": "[3.333337006277949761389162272546182701503663110922792 +/- 3.05e-52]"
        }
      ]
    ],
    "complete_forward_operator_upper": {
      "ball": "[5.975050658063412272696062789601746551224967356482983 +/- 4.39e-52]"
    },
    "complete_new_final_forward_log_upper": {
      "ball": "0"
    },
    "complete_new_final_reverse_log_upper": {
      "ball": "[0.4416405119213984551291193867796383673361665884349769 +/- 4.38e-53]"
    },
    "complete_new_tail_audit_sha256": "d709a485ea04784c1a88ad378a242e155bef23299cf95b0fdfca73bd3f08252f",
    "complete_new_tail_forward_product": [
      [
        {
          "ball": "[1.009949300673988146216563576937863649717412327782157 +/- 1.34e-52]"
        },
        {
          "ball": "[0.004959691908017969915500721060174597468183956798457439 +/- 9.06e-56]"
        }
      ],
      [
        {
          "ball": "[0.02354010845396646715335326868983486322038593797444850 +/- 4.59e-54]"
        },
        {
          "ball": "[1.004576658057305995796033621138732551328467363805781 +/- 3.10e-52]"
        }
      ]
    ],
    "complete_new_tail_reverse_product": [
      [
        {
          "ball": "[1.008553567793207267425310014053170762435552240805961 +/- 3.64e-52]"
        },
        {
          "ball": "[0.004954876569829670375452205410676838687934222349753270 +/- 4.46e-55]"
        }
      ],
      [
        {
          "ball": "[0.02350628625942510814524792215088197998183434559417002 +/- 2.61e-54]"
        },
        {
          "ball": "[1.003203151386481110676603816115746877511655543367564 +/- 1.13e-52]"
        }
      ]
    ],
    "complete_new_tail_row_count": 269,
    "complete_new_tail_scalar_maxima": {
      "A": {
        "ball": "[6.105111176832846119434696222498663069545711027284573 +/- 8.00e-53]"
      },
      "Bphi": {
        "ball": "[4.070074117888564079623130814999108713030474018189715 +/- 2.81e-52]"
      },
      "D": {
        "ball": "[0.4226268039375846785245606608235669535042156830965591 +/- 3.02e-53]"
      },
      "L": {
        "ball": "[3.703839003728273923029649525469969400179000000529434 +/- 1.92e-52]"
      },
      "Ngamma": {
        "ball": "[3.843464266188288341243270064219729480189967365619659 +/- 3.59e-52]"
      },
      "Ny": {
        "ball": "[2.789954842016122063384550898294955682645006703234015 +/- 4.77e-52]"
      },
      "Nz": {
        "ball": "[0.5087592647360705099528913518748885891288092522737144 +/- 1.01e-53]"
      },
      "R": {
        "ball": "[1.911031808335595067603982284913451435900000151239369 +/- 1.28e-52]"
      },
      "beta": {
        "ball": "[0.2105517212355066777463689845224985519808281242898028 +/- 4.54e-53]"
      },
      "complete_state_square_difference": {
        "ball": "[8.531629840552301018870553710636809046626320076448994e-7 +/- 2.77e-59]"
      },
      "forward_rate": {
        "ball": "[2.706154170083172132851225818754175600790719530678347 +/- 1.36e-52]"
      },
      "gamma": {
        "ball": "1.119938872755483316723257303237915039062500000000000"
      },
      "qplus": {
        "ball": "0.7230911851220298558473587036132812500000000000000000"
      },
      "reverse_rate": {
        "ball": "[2.706154170083172132851225818754175600790719530678347 +/- 1.36e-52]"
      }
    },
    "complete_reverse_matrix": [
      [
        {
          "ball": "[185.0751745325951770396074382417460543669648347869247 +/- 3.95e-50]"
        },
        {
          "ball": "[35.41387545258786435202220073980917616836528283484184 +/- 3.88e-51]"
        }
      ],
      [
        {
          "ball": "[136.4718471026230383722720882358536746362810911487932 +/- 1.11e-52]"
        },
        {
          "ball": "[146.5715631052427213859118586972819672326586208430323 +/- 2.15e-52]"
        }
      ]
    ],
    "complete_reverse_operator_upper": {
      "ball": "[274.9813647605194377536931735582094747961989233717470 +/- 2.18e-50]"
    },
    "exact_complete_interval": [
      "0",
      "76285779072683/320000000000000"
    ],
    "exact_new_tail_interval": [
      "2333968743003/10000000000000",
      "76285779072683/320000000000000"
    ],
    "no_old_upper_subtraction_or_division": true,
    "original_0_ra_curvature_cost_reused_as_one_whole_budget": true,
    "original_prefix_matrices_read_verbatim": true
  },
  "SW_complete_original_scope": {
    "complete_changed_trial_source_and_all_interfaces_paid": true,
    "complete_old_CG_positive_budget_used_without_subtracting_upper": true,
    "complete_second_normalizer_and_Q_F0_F1_T1F2_retained": true,
    "exact_Maslov_commonout_and_all_infinite_other_sign_blocks_remain_separate": true,
    "full_CT_coefficient_root_finite_part_and_scalar_mean_retained": true,
    "incoming_finite_inverse_nonlinear_state_and_R0_not_claimed": true,
    "no_old_source_integral_or_successful_target_repeated": true,
    "no_radial_family_declared_finite_rank": true,
    "only_complete_actual_paid_candidates_compared": true,
    "same_WT_Js_inverse_after_new_physical_waist_FT_correction": true,
    "same_original_Bc_and_complete_cut_error": true,
    "same_terminal_Ai_and_original_root_input_not_a_different_basis": true,
    "selected_common_angle_only_at_same_original_selected_parameter": true,
    "two_physical_means_and_all_six_retained_rows_remain": true
  },
  "SW_complete_parameter_scope": {
    "arithmetic_bits": 320,
    "complete_Q_F0_F1_T1F2_retained": true,
    "continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_response_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "exact_complete_radial_interval": [
      "0",
      "76285779072683/320000000000000"
    ],
    "exact_moving_normalizer_cutoff_abs_j": 268435456,
    "exact_real_delta_radius": "1/100000000",
    "exact_single_first_symbol": "W=A(1+M_C I)Lc with complete C including Fstar and full mean",
    "exact_source": "(P[T DW-Q W], -Zy T W)",
    "exact_strict_cut": "76285779072683/320000000000000",
    "expected_actual_gate_count": 24,
    "fixed_intrinsic_parameter": "eta_0",
    "full_Ei_Eo_or_incoming_or_Schur_or_R0_claimed": false,
    "independent_physical_mean_coordinates": 2,
    "input_cutoff_abs_j": 97,
    "jump_bound": "all3070 interfaces times a complete one-sided two-Z maximum; no length",
    "new_complete_global_ordinary_source_bound_count": 1,
    "new_grid_integrals_or_array_inputs": 0,
    "new_trial": "(P T W,0)",
    "old_CG_reuse": "forward domination of identified positive terms",
    "old_scientific_calls_allowed": 0,
    "original_conservative_refinements": 521,
    "original_genuine_joins": 2549,
    "original_interface_rows": 3070,
    "original_source_rows": 3071,
    "physical_frequency": "n=4|j|",
    "physical_input_signs": [
      -1,
      1
    ],
    "physical_waves": [
      -1,
      1
    ],
    "reference_column": "same terminal Ai free P8 first column",
    "retained_mode": "exact-border-unpaid",
    "returned_trial": "(P TJ W,0)",
    "selected_common_input_order": "S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)",
    "source_bound": "one complete global maximum times exact rc",
    "state_operator_order": "S U_Xminus_sigma_inverse J_sigma Twaist_inverse E_star P97 Lambda_sigma_inverse TF_inverse S_inverse",
    "whole_selection": "compare final retained outward complete paid upper; old wins ties"
  },
  "SW_complete_selected_scope": {
    "exact_order": "S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)",
    "inverse_order": "S_inverse = U_X_minus_inverse U_H",
    "only_same_selected_actual_conjugacy": true,
    "selected_parameter_absolute_upper": "0.00000000009368259853002"
  },
  "SW_complete_source_and_interface": {
    "both_genuine_and_artificial_locations_retained": true,
    "complete_all_interface_impulses_upper": {
      "ball": "[26068253924090251771055095541078778509210288709213647765609021158428.0753 +/- 4.17e-5]"
    },
    "complete_conservative_interface_count": 521,
    "complete_genuine_interface_count": 2549,
    "complete_interface_count": 3070,
    "complete_ordinary_L1_source_upper": {
      "ball": "[2.32742705099466860506562161606185774307196164517130521770200359153075314e+81 +/- 4.72e+8]"
    },
    "complete_ordinary_Q_F0_F1_T1F2_L1_upper": {
      "ball": "[2.32568821873666154790001953071109290090672851761327897392605182256721628e+81 +/- 7.06e+8]"
    },
    "complete_ordinary_independent_mean_L1_upper": {
      "ball": "[1.73744100271918131327852495430241667068211546348222966022823843693667448e+78 +/- 3.97e+6]"
    },
    "complete_ordinary_leading_defect_L1_upper": {
      "ball": "[1.39125528787585232356039646242549455101209454401411572353052660018434744e+75 +/- 4.07e+3]"
    },
    "every_jump_uses_complete_two_one_sided_Z_bounds": true,
    "exact_ordinary_radial_interval": [
      "0",
      "76285779072683/320000000000000"
    ],
    "full_Zy_mean_row_retained": true,
    "jump_has_no_radial_length_factor": true,
    "original_SJ_source_integrals_and_jump_sum_not_reused_for_changed_W": true,
    "original_full_Q_including_F0_F1_T1F2_retained": true,
    "original_successful_source_integrals_and_jump_sum_not_recomputed": true,
    "source_window": "L1(dr; L2 nonmean pair plus two independent physical means)"
  },
  "SW_complete_trial_and_endpoints": {
    "complete_TJ_singleW_waist_error_upper": {
      "ball": "[7.05994136031959095363926517592982151842539431001951838131115980630243387e+83 +/- 2.61e+11]"
    },
    "complete_all_interface_receiver_contribution": {
      "ball": "[7907459182931375899121652567298042130232666009188901419983168253868238.87 +/- 3.69e-4]"
    },
    "complete_cut_receiver_contribution": {
      "ball": "[3992762249823515605943393348782398646854779770498.67233900182442880416978 +/- 3.78e-24]"
    },
    "complete_fullT_singleW_waist_error_upper": {
      "ball": "[7.05994136031616356329766076814814113238522608781782862723200189279691998e+83 +/- 4.03e+11]"
    },
    "complete_ordinary_source_receiver_contribution": {
      "ball": "[7.05994136031608448870583145438914987593193060916137024113797651595873368e+83 +/- 4.26e+11]"
    },
    "complete_physical_mean_coordinates": 2,
    "complete_physical_waist_FT_W_correction_upper": {
      "ball": "[3.42739034160440778168038604016822220168975407915791350551389662598981006e+71 +/- 0.209]"
    },
    "cut_trial_is_exactly_the_same_Bc": true,
    "intermediate_SF_bounds_for_different_trials_not_compared": true,
    "inverse_is_only_same_actual_TJ_not_full_T": true,
    "original_complete_FT_strong_upper_read_verbatim": {
      "ball": "[16050292905094949719064990172560726.2454349520118664586230628555641170697 +/- 4.86e-38]"
    },
    "original_fullT_cut_error_read_verbatim": {
      "ball": "[108696340340951351029091710450393091694320015823.775959403613733467161487 +/- 2.79e-26]"
    },
    "physical_cut_error_and_original_FA_ranks_read_once": true,
    "source_receiver_already_contains_output_waist_ng": true,
    "waist_ng_times_FT_W_paid_once": true
  }
}
```

## Appendix B. Exact accepted identities, progress, selection and new retained scope

```json
{
  "accepted_old_receipts": {
    "st_execution": {
      "actual_returncode": 0,
      "complete": true,
      "execution_kind": "actual_public_strict_tail_true_cut_to_waist_execution",
      "gates": 25,
      "input_manifest_sha256": "e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80",
      "input_sha256": "b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637",
      "proved": true,
      "run_attempt": "1",
      "run_id": "43757644616",
      "runtime": {
        "numpy": "2.3.5",
        "python": "3.12.14",
        "python_flint": "0.9.0",
        "scipy": "1.17.0"
      },
      "scientific_kind": "actual_complete_strict_tail_true_branch_cut_to_waist_v1",
      "source_sha256": "743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5"
    },
    "sw_science": {
      "actual_returncode": 0,
      "complete": true,
      "gates": 24,
      "input_manifest_sha256": "5d62a5e758cd11d4325d1797666bb57683ee94f79e4d4fb4351c33b7f94d78e4",
      "input_sha256": "f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659",
      "proved": true,
      "run_attempt": "1",
      "run_id": "43781399696",
      "runtime": {
        "Python": "3.12.14",
        "python_flint": "0.9.0"
      },
      "scientific_kind": "actual_single_complete_root_first_symbol_trial_v1",
      "source_sha256": "d0380618d0e57fe4771ad0fb5b6a92990225abc9c6f2f379959653eab4e93fb9"
    }
  },
  "actual_progress": {
    "actual_old_scientific_targets_recomputed": 0,
    "actual_old_source_calls": 0,
    "complete_first_row_gain_graph_count": 1,
    "complete_whole_candidate_graph_count": 1,
    "complete_whole_selection_count": 1,
    "completed_old_receipts_read": 2,
    "completed_old_scalar_records_copied": 14,
    "completed_old_scope_objects_copied": 9,
    "entered_new_scalar_stage": true,
    "final_readonly_input_check_count": 5,
    "new_contribution_scalar_records_saved": 5,
    "new_gain_scalar_records_saved": 4
  },
  "complete_new_first_row_gain_conclusion": {
    "all_shorter_insertions_from_original_positive_algorithm": true,
    "complete_density_cut_row_gain_upper": {
      "ball": "[25.1716699151329125544412692036391961187725820720351296329671295047140499 +/- 3.41e-71]"
    },
    "complete_first_matrix_row_L2_upper": {
      "ball": "[188.432913268467968358875795246164698642503509985045809808829091554700833 +/- 4.32e-70]"
    },
    "complete_ungauged_mean_row_gain_upper": {
      "ball": "[39.0656638395227706895560719439749728116223385221487756487002935658404962 +/- 3.81e-71]"
    },
    "complete_ungauged_primitive_row_gain_upper": {
      "ball": "[204.159653834300462612406113807938615827913665301580648191544296000342776 +/- 1.30e-70]"
    },
    "full_mean_source_not_removed": true,
    "physical_frequency_and_ordinary_measure_retained": true,
    "uses_complete_saved_first_row_not_whole_Frobenius": true,
    "waist_output_and_cut_input_factors_in_true_directions": true
  },
  "complete_new_whole_row_candidate_conclusion": {
    "PC_ST4_and_waist_FT_retained_verbatim_once": true,
    "complete_all_3070_interface_contribution_upper": {
      "ball": "[5322085697206910450627411811246732244263668509901801959902435955353323.89 +/- 3.37e-3]"
    },
    "complete_cut_contribution_upper": {
      "ball": "[2736068400045373073430725520115824623463042027546.96382038149626170636211 +/- 1.18e-24]"
    },
    "complete_first_row_candidate_upper": {
      "ball": "[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]"
    },
    "complete_independent_mean_source_contribution_upper": {
      "ball": "[6.78742861532309053328839023271334669171345937891697481975991900494226807e+79 +/- 9.17e+6]"
    },
    "complete_primitive_source_contribution_upper": {
      "ball": "[4.74811985701985644655978079913349647844946763054638092045674772948381287e+83 +/- 7.40e+10]"
    },
    "interfaces_have_no_radial_length_factor": true,
    "no_new_source_integral_or_positive_product": true,
    "primitive_source_uses_both_complete_leading_and_Q_parts": true,
    "same_original_single_W_and_compressed_TJ_trial": true,
    "saved_waist_FT_correction_not_multiplied_by_ng_again": true,
    "source_gain_already_contains_waist_output_factor": true
  },
  "complete_whole_row_selection": {
    "comparison": "whole saved old Cstar and complete new first-row candidate",
    "complete_candidates": [
      {
        "label": "saved_old_complete_Cstar",
        "upper": {
          "ball": "[7.05994136031959095363926517592982151842539431001952856359080309257433083e+83 +/- 8.01e+10]"
        }
      },
      {
        "label": "new_complete_first_row_candidate",
        "upper": {
          "ball": "[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]"
        }
      }
    ],
    "complete_selected_row_upper": {
      "ball": "[4.74879859988486936681168611504295450063760366646214592528987914033956321e+83 +/- 1.36e+11]"
    },
    "different_trial_or_different_output_unit_minimum_used": false,
    "entrywise_minimum_used": false,
    "new_candidate_upper_strictly_smaller": true,
    "old_candidate_wins_ties": true,
    "selected_index": 1,
    "selected_label": "new_complete_first_row_candidate"
  },
  "scope": {
    "PC_ST4_cut_and_saved_waist_FT_each_retained_once": true,
    "actual_nonlinear_background_proved": false,
    "all_3070_interfaces_without_length_factor_retained": true,
    "complete_mean_source_and_both_physical_mean_coordinates_retained": true,
    "final_surface_proved": false,
    "finite_Schur_inverse_proved": false,
    "full_incoming_inverse_proved": false,
    "independent_even_mean_amplitude_nu_head_and_other_ports_retained": true,
    "input_window": "same reflected natural root H^(-4/3), original |j|>=97",
    "old_ST_and_SW_successes_read_only": true,
    "old_scientific_imports_calls_native_restoration_and_new_grids": 0,
    "output_window": "raw moving-angle even meanzero L2 primitive row",
    "physical_leading_row_square_inverse_proved": false,
    "raw_L2_derivative_readout_proved": false,
    "raw_h1_mean_redundancy_does_not_delete_even_mean_or_amplitude": true,
    "same_complete_reflected_primitive_waist_row": true,
    "same_selected_parameter_and_original_terminal_Ai_column": true,
    "same_single_W_and_same_compressed_TJ_trial": true,
    "signed_adjoint_cancellation_numerically_certified": false,
    "whole_return_R0_proved": false,
    "whole_selection_same_object_and_same_output_units_only": true
  }
}
```

## Appendix C. Recorded job steps

| Recorded step number | Name | Conclusion |
|---:|---|---|
| 1 | Set up job | success |
| 2 | Initialize containers | success |
| 3 | Install terminal Git | success |
| 4 | Partially check out only scripts parameters and reviewed READMEs | success |
| 5 | Verify the separately pinned worker | success |
| 6 | Hydrate only small source proof and provenance texts | success |
| 7 | Parse the entire frozen Python closure before any new arithmetic | success |
| 8 | Install the pinned directed arithmetic runtime | success |
| 9 | Read two immutable successes and evaluate only nine new complete physical-row scalars | success |
| 17 | Post Partially check out only scripts parameters and reviewed READMEs | success |
| 18 | Stop containers | success |
| 19 | Complete job | success |

The API step numbers contain the original gaps for post-job steps; there are exactly twelve recorded steps, not nineteen. No log body was needed to verify their success.
