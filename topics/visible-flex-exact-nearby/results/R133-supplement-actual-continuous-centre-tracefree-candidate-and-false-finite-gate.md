# R133 supplement: actual complete continuous-centre tracefree candidate and its false finite sufficient test

2026-11-16, newton_source. **WVCA. Completed first execution: all six bound graphs are saved; the finite sufficient comparison is false.** This is a read-only account of run `43891414339/1`, not a prospective model or a new numerical calculation.

## WVCA1. Exact outcome and its scope

The complete WVC candidate was evaluated once for the same selected positive genuine family and the same actual spaces, projections and four operator blocks. All 23 structural gates passed. The six graphs contain exactly 56 new named scalar records, with counts $7,12,22,8,3,4$. All 96 nonzero reflected low modes used a changed reference. Five complete running modal records and their witnesses are also retained.

The final stored comparison record is

$$
\left[
11066.2974592482170277255953739045070721096905053507529455902664127679013367
\ \pm\ 3.72\,10^{-71}
\right].
\tag{WVCA.1}
$$

The declared test is the saved upper bound for $e+3dt<1$. It returned false. The conclusion is complete and successful as a computation of the declared bounds; it does **not** establish a finite signed inverse. The actual fields are `finite_gate.passed=false`, `conditional_finite_inverse=null`, `actual_progress.conditional_finite_inverses=0`, and `physical_state_columns_computed=0`. Failure of this sufficient estimate does not prove singularity.

The previously proved analytic refinement160 tail inverse bound $3$ remains valid for the unchanged actual tail block. It is not a bound on the full coupled inverse. The physical 96 prescribed root-even directions, the 97 root-complement directions, the 96 outer coordinates, the independent physical mean, all affine and external inputs, $\Theta$, $\nu$, all cokernel rows, and both complete right-hand sides remain present.

No old completed bound was recomputed. No new dense finite matrix, coefficient array artifact, Release, or physical solution column was produced. All 56 named records and the complete requested five-record modal prefix are present; there is no interrupted target or lost completed target. Sections WVCA7 and WVCA10 state this boundary precisely.

## WVCA2. Immutable actual files and source identity

The following are complete UTF-8 files. Each byte count and SHA-256 was checked against the full retrieved text. JSON identities below use sorted keys, compact separators, UTF-8 and one final LF. Re-encoding the complete scientific and execution objects by this convention reproduced their original bytes exactly.

| Object / exact repository path | Git blob | Bytes | SHA-256 |
| --- | --- | --- | --- |
| scientific conclusion<br>`topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json` | `746ec1e16befe8914c64521ad087c1f1dd23ab73` | 78627 | `85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88` |
| execution<br>`topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/execution.json` | `c8cd8e8bb863c500a1e26c009e0af76cd7cb8941` | 37911 | `5e560887d2deee497cb9da5b7549af1070db36cf69a7b11077ef4a0bb4f0feb5` |
| report<br>`topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/report.md` | `f933d28e18efaf4040c6fcb09b46bb527d3bf87a` | 442 | `72d38cde977c2f5686373a4337a171581a539f548a31f42509f545b05d02b186` |
| frozen manifest<br>`topics/visible-flex-exact-nearby/notes/2026-11-16-R133-continuous-centre-tracefree-current-inputs.json` | `1ea008a1df3116aedd66be67b11b1d8ec62af2d5` | 60844 | `229198f56efdf10ea8de6fef50804aa3832ca5ff2127101685c8d7117c9afbfb` |

The mathematical basis is the published [WVC theorem](R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md), blob `e377cb2e0578fc66ba8a7bc32e339fadcb0a242c`, 29,128 bytes, SHA-256 `fade78e696506af0ef2c1e304e824ff7415c63df53b31f0ed299d8ff548845a8`; the complete [WPS paired residual theorem](R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md), blob `e830f7df4643fe77b941478dbde06ebf9378ebef`, 43,851 bytes, SHA-256 `ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72`; and the [WIC analytic tail theorem](R133-supplement-analytic-inherited-tail-and-weighted-impedance-circuit.md), blob `019b1136ebe81e44e98399dff5fb895aafb4362e`, 29,026 bytes, SHA-256 `527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f`.

The frozen five scientific sources and the shared operational worker were:

| Role / exact path | Git blob | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `science`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_continuous_centre_tracefree_candidate.py` | `d8d3f135abe8ad49b8b7b002e830bbc8ad678a5f` | 59614 | `126af29d436c20c9e4fe2bb50f0d82d1f2a2c6996f3b6862cb9e1f51924b586f` |
| `readonly_admission`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_continuous_centre_tracefree_readonly.py` | `3720b34531e0258fe44f22879687627740f81784` | 67420 | `c84bd805d685bb65eb10e75eb95a7efdbe2f5eb9527c0fafd1b534d54372f0f2` |
| `kernel_math`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_continuous_centre_kernel_math.py` | `b6b08273eb17923a4b98cce439d4cd11988c6be8` | 32915 | `0b3cc24c80fd1f038c5f3b1d3df2ea7cf8ce19695f30bdedd7a3a37f86fd9584` |
| `assembly_math`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_continuous_centre_candidate_math.py` | `7236b07376a46e96a2664aa3d800896bc182ed89` | 12983 | `9ff4d6cac77591957632e68fe87d1b1356e66662d6e16c01e447d2500e29fd98` |
| `reference_math`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_clipped_tracefree_reference_math.py` | `26958792c2feaa01aed417652682052c2d420465` | 22568 | `5e62a3c46cd3bf6ccb689f91e1642963b6db6fb758c302a9439d10d2871131c1` |
| `worker`<br>`topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_paired_public_worker.py` | `85d72a0600816b2176093dd74ab61595fad40520` | 31551 | `afbbae87226ee6c1ddb95944a8f21c00b6e7218a166f046ea2fc24b2ce86e437` |

The workflow event was `62353730862c1defd1379abcacc3099357d09e70`. The actual scientific checkout was `e3fd125becf38af789e81feee0f61fc3a13ed58a`. This is also the published consumed-marker commit. The input manifest SHA-256 is `229198f56efdf10ea8de6fef50804aa3832ca5ff2127101685c8d7117c9afbfb` in both actual files. All 41 complete current receipts, all five module identities, their role-to-SHA map, and all 16 operational AST receipts were independently compared with that manifest.

## WVCA3. What the new candidate proves

The continuous repaired degree32 centre is used throughout the trial source. Its local products have degree at most64. The centre source has output support $97\leq j\leq224$, while the complete degree96 family correction is retained as a norm on the full output, through $j=352$. The latter is never projected onto the 256-coordinate centre source carrier. The true physical mean is a separate coordinate with weight $1$; nonzero real sine/cosine modes have their normalized $\sqrt2$ factors.

Write $\mathcal L_H=\partial_r-A_{HH}$ and $\mathcal L_0=\partial_r-D$. The trial is built from the true two-sided reference Green operator $G_0$, with both source moments, both triangles, the root and outer atoms, and all physical/Riesz factors. The identity $\mathcal L_0G_0=I$ is applied to the entire continuous source. With $A_{HH}=A_{HH,c}+\Delta A_{HH}$ and $B_{HL}=B_{HL,c}+\Delta B_{HL}$, its complete high residual is

$$
\begin{aligned}
\mathcal L_H(\chi G_0\chi B_{HL,c}a)-B_{HL}a
={}&(\chi^2-1)B_{HL,c}a-\Delta B_{HL}a\\
&+\bigl[\chi'I-\chi(A_{HH,c}-D)\bigr]G_0\chi B_{HL,c}a\\
&-\chi\Delta A_{HH}G_0\chi B_{HL,c}a .
\end{aligned}
\tag{WVCA.2}
$$

No derivative of $B_{HL,c}$ is omitted: it is a forcing coefficient inside $G_0$. The cutoff sets the trial's own endpoint trace to zero. It does not set the actual high trace, independent affine data, outer observation or physical mean to zero. Those terms are received separately by the original complete seven-port estimates.

The low reference uses the clipped signed tracefree diagonal from WVC. All exact signed local and primitive entries are formed before absolute values. The changed reference has its own weighted inverse, normalizer-defect and odd-endpoint bounds. The old reference numbers are preserved as old records, not assigned to the changed reference. The full old independent mean receiver is retained because that mean reference operator is unchanged.

Let $\widehat K_H$, $\varepsilon_H$, $\varepsilon_b$, $o_H$, $o_b$, $t_H$, $t_b$, and $e_\rho$ denote the complete saved bounds specified by the graph keys below. Set $h=\widehat K_H+\varepsilon_H$ and use the proved WVC lift bound $w_0=6/5$. The final graph implements

$$
\begin{aligned}
e&=e_\rho+(1+e_\rho)\sqrt{w_0^2h^2+\varepsilon_b^2}
                  +\sqrt{w_0^2o_H^2+o_b^2},\\
d&=(1+e_\rho)h+o_H,\\
t&=\sqrt{w_0^2t_H^2+t_b^2},\\
\mathfrak d&=e+3dt.
\end{aligned}
\tag{WVCA.3}
$$

Every operand is taken from its already saved complete record with the specified directed endpoint. The displayed formulas describe the frozen computation; they have not been reevaluated for this note. The actual four final records are tabulated in WVCA6.6. The mathematical inverse theorem applies only if the complete last comparison is strictly below $1$; that hypothesis failed in this execution.

## WVCA4. Complete input admission and retained original qualifications

The data-only preflight completed before the numerical import. It had return code $0$, 2,682 stdout bytes and zero stderr bytes. Its full output SHA-256 is `aecd43f8337e5aca2915ab50d48979092594395ab29ca9e5454d272d40d7f43a`. Its admission object agrees exactly with `original_admission` in the scientific result.

There were 41 current UTF-8 inputs and 19 historical byte restorations: 13 original positive-native parts, five original cubic candidate parts and the one original exact continuous-value repair. The original complete native has 25,507,783 bytes and SHA-256 `1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c`. Both original orders have all 4,650 saved rows; all 3,594 interfaces were admitted. The producer progress counter $4608$ and the original parts-manifest row counter $0$ retain their separate meanings.

The original candidate has 6,145 radial nodes and complete shape $[4,6144,65]$. The original repair's 65 physical suprema and whole definition were read; no repair or old numerical producer was regenerated. Five new scientific sources, ten old definition sources, and the worker account for the 16 AST receipts. Old definitions were read and checked; old bound-producing modules were not imported or called.

The exact original reference-definition chain was materialized, ending before any old bound routine. Its complete chain is

```json
{"count":153,"sha256":"6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"}
```
The new clipped signed diagonal definition has its own complete 153-parent chain:

```json
{"changed_mode_indices":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96],"complete":true,"same_actual_spaces_and_projection":true,"selected_diagonal_chain":{"count":153,"sha256":"b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2"},"unchanged_mode_indices":[]}
```
The repaired coefficients were enclosed over each entire original parent domain, not sampled. There were 152 body parent packets, 4,801 original intersections, 4,650 original closed rows, 155 comparison cells including both cutoff joins, and 24,480 inherited fine cells. All raw identity transmissions and all independent affine jump inputs remain in the admission. The reference chain and all completed old maxima are different objects; rebuilding the exact reference definition did not rerun those maxima.

The complete original admission object is retained verbatim:

```json
{"candidate_nodes":6145,"candidate_shape":[4,6144,65],"checks":[{"name":"all_current_UTF8_files_and_three_fixed_contracts_verified","passed":true},{"name":"five_new_and_ten_original_definition_sources_AST_only_verified","passed":true},{"name":"all_nineteen_historical_receipts_and_original_native_bytes_verified","passed":true},{"name":"complete_original_summary_and_native_projection_identical","passed":true},{"name":"both_complete_4650_row_covers_and_3594_interfaces_verified","passed":true},{"name":"same_real_family_and_all_original_successes_verified","passed":true},{"name":"all_nine_original_literals_and_completed_WHVA_retained","passed":true},{"name":"all_five_original_cubic_parts_and_full_shape_verified","passed":true},{"name":"original_repair_whole_document_and_all_65_suprema_verified","passed":true},{"name":"actual_raw_identity_transmissions_and_full_affine_ports_retained","passed":true},{"name":"all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","passed":true}],"current_file_count":41,"historical_input_count":19,"inflated_rows":4650,"interfaces":3594,"native_bytes":25507783,"native_sha256":"1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c","new_source_AST_count":5,"old_gate_counts":[19,11,18,14,6],"old_source_AST_count":10,"old_source_import_count":0,"old_targets_recomputed":0,"original_parts_manifest_row_counter":0,"original_progress_counter":4608,"per_order_complete_rows":[4650,4650],"prior_completed_candidate_records":60,"prior_completed_modal_prefix_records":6,"repair_suprema_count":65,"repairs_regenerated":0,"restoration_receipts_bytes":13771,"restoration_receipts_sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"}
```
## WVCA5. Complete old objects and their exact read-only boundary

The first 15 records are the complete `copied_original_records` dictionary, including all original display fields when present and both exact rational strings. Ten additional records are in the complete original reference graph, and the eleventh additional record is the complete original family $HL$ residual bound. Thus the actual progress count $26$ means $15+10+1$; it does not claim that the root dictionary has 26 keys.

The earlier WPS result remains complete with all 60 original targets and all six original modal prefix records. Its full-file pins and all original 40 scientific and 45 execution field identities are verified before the new computation. The original false finite gate, original parameters, original scope, original progress, all original reference graph records and all six witnesses are retained in the complete immutable archive. The old WPTVS five maxima and its two false sufficient tests are also retained. No earlier false gate is reclassified by the WVC run.

The following complete JSON-object identities were independently reproduced from the actual file:

| Exact root key | Canonical bytes | SHA-256 |
| --- | --- | --- |
| `copied_original_records` | 2627 | `b313df918a9ec86507695b49ba8eb5c5a75afbe268faeffdb14ece854f1f2e71` |
| `copied_original_scope` | 8502 | `94c595173f4591660211251da7f67ea47e15fd52749167379f5ff4c50909736b` |
| `copied_complete_candidate_metadata` | 2581 | `aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356` |
| `copied_complete_repair_definition` | 792 | `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` |
| `retained_completed_five_maxima` | 2350 | `407ca196cf8f60ac7c037cd2c2056673e139ecd4c1ecc4343d78a5cbf99a6f74` |
| `retained_original_false_candidates` | 1082 | `af586adb9e63165b204717ac8ace80c2d05285940573a1f7bdc39599b89ae187` |
| `complete_restoration_receipts` | 13771 | `4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac` |
| `prior_completed_candidate` | 8977 | `2e70e03efe8d2275f5365fff52b5a964c912594edd6a156145affafe7146799e` |
| `retained_scope` | 2282 | `fcefcfc2e136079f5098c3f324230b5e4ab058798e950c2c6a91a878046d7267` |
| `complete_support_contract` | 520 | `622693074042afeceb02fb81efb373aeb8d33c01003332ba16d5b0f6eb349067` |
| `reference_selection` | 507 | `6dab06a990a60129c0ebf5a442f935851050dedb6ce7b6655076be29bd9cd7d9` |
| `reference_mode_prefix` | 988 | `842157bf20b74c7df36a3f4c96ca9491e371c12fd2f72d9c4daa3fa6cf597d7b` |
| `complete_new_graphs` | 8637 | `0882b563cdd2e425d5d1e383bd158ce5bce7fb1604903df2bb1a0756b5f4ea42` |
| `complete_current_file_receipts` | 12199 | `45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629` |
| `original_admission` | 1719 | `b8156edca3e6674cb50762b23a13c0333850c29cf6e35b236563850777c7fe6b` |

The complete old 15-record dictionary is:

```json
{"A_c":{"ball":"[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]"},"C_b":{"ball":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","lower":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","upper":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]"},"C_c":{"ball":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","lower":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","upper":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]"},"E_minus":{"ball":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]","lower":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]","upper":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]"},"G_c":"62286/125","L_c_raw":"58/5","P_b_raw":{"ball":"[0.00230158835209555496325236476227310039199272102107215008177573464882078520759 +/- 2.64e-78]"},"Y_b":{"ball":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]","lower":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]","upper":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]"},"Y_b_outer":{"ball":"[0.00365769892351436839526506567363676924340713180672188755030293063817866017188 +/- 2.60e-78]"},"Y_c":{"ball":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]","lower":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]","upper":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]"},"lambda_388_minus_two_thirds":{"ball":"[0.0187979816503496541345324625056530986003947533773800386267688853972524679326 +/- 2.11e-77]"},"mu_minus":{"ball":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]","lower":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]","upper":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]"},"pi":{"ball":"[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]"},"reciprocal_sqrt_two":{"ball":"[0.707106781186547524400844362104849039284835937688474036588339868995366239231 +/- 5.51e-77]"},"shell_1153":{"ball":"1153.00000000000000000000000000000000000000000000000000000000","lower":"1153.00000000000000000000000000000000000000000000000000000000","upper":"1153.00000000000000000000000000000000000000000000000000000000"}}
```
The whole old scope is 8,502 canonical bytes. Its complete value, including the old scalar archive, original mean/source windows, failed old mesh gates, literal domains, and all independent physical obligations, is:

```json
{"WOBSA_complete_positive_columns":{"actual_root_stable_input_zero":true,"body_source_choice_read_verbatim":"A_b_from_L","complete":true,"complete_new_records":{"complete_head_outer_trace_upper":{"ball":"[3.03093313443307949770085689259592195423369435349649052364971666602569752377 +/- 5.82e-76]"},"complete_head_root_unstable_upper":{"ball":"[0.757733283608269874425214223148980488558423588374122630912429166506424380942 +/- 3.55e-76]"},"complete_outer_b_outer_trace_upper":{"ball":"[0.00365769892351436839526506567363676924340713180672188755030293063817866017188 +/- 2.60e-78]"},"complete_outer_b_raw_state_upper":{"ball":"[0.00230158835209555496325236476227310039199272102107215008177573464882078520759 +/- 2.64e-78]"},"complete_outer_b_root_unstable_upper":{"ball":"[0.000914424730878592098816266418409192310851782951680471887575732659544665042971 +/- 3.52e-79]"},"complete_outer_b_to_head_source_upper":{"ball":"[175.711718635860624882734290849864754541321815546548694593851449145066243980 +/- 3.54e-73]"}},"disjoint_original_source_intervals":true,"full_original_seven_input_oracle_retained":true,"kind":"complete_positive_head_and_outer_columns_v1","original_C_P_and_C_K_read_without_recomputation":true,"output_orthogonality_assumed":false,"proof_formulas":"WOB.9-WOB.12","raw_output_window":"whole L2_dr H^-1 with independent mean separate","source_window":"ordinary L2_dr H^-2/3"},"WOBSA_parameters":{"actual_pR_upper":"1/5","arithmetic_bits":320,"copied_original_records":42,"decimal_record_digits":75,"exact_original_contour_shift":"1/512","exact_real_delta_radius":"1/100000000","exact_trial_cutoff_support_length":"3/1000000","first_high_abs_j":97,"fixed_intrinsic_parameter":"eta_0","head_dimension":193,"historical_inputs":0,"last_low_abs_j":96,"new_complete_graphs":6,"new_exponentials":1,"new_fractional_powers":1,"new_saved_records":37,"new_square_roots":7,"normalized_angular_measure":true,"old_scientific_target_recomputations_allowed":0,"original_frozen_common_input":"Xfr = S_star D_plus H_nat^(-4/3)","original_outer_high_and_low_window":"H^-5/6","original_raw_state_window":"ordinary L2_dr H^-1","original_rough_stable_window":"H^-3/2","original_same_negative_source_window":"ordinary L2_dr H^-2/3 with independent mean","physical_frequency":"n=4|j|","physical_period":"pi/2","same_selected_member_only":true},"WOBSA_retained_scope":{"CF288_whole_common_factor_no_upper_division_or_subtraction":true,"Ni_and_stable_inverse_in_original_right_order_once":true,"PW_receiver_applied_only_to_zero_stable_additional_state":true,"WSP_complete_RH_source_not_received_positive_bound":true,"actual_outer_y_coordinate_not_identified_with_raw_endpoint":true,"all_new_targets_are_complete_positive_bounds_in_original_units":true,"all_six_complete_original_receipts_read_without_old_math":true,"complete_original_37_records_plus_five_typed_factors_retained":true,"finite_signed_inverse_proved":false,"full_actual_pR_upper_from_exact_same_family_body":true,"full_incoming_inverse_proved":false,"full_low193_rows_and_independent_even_mean_retained":true,"full_source_jump_root_mean_and_cokernel_rows_retained":true,"independent_physical_coordinates_receive_no_Ni":true,"mean_and_amplitude_rows_not_claimed_zero":true,"new_whole_comparisons":0,"nonlinear_background_or_surface_proved":false,"old_whole_bounds_not_subtracted":true,"original_C_P_C_K_A_infty_L_star_C_V0_C_R0_read_verbatim":true,"original_WHVA_4096_strict_sufficient_test_false":true,"original_WHVA_no_resolvent_admitted":true,"original_sqrt_two_target_read_not_recomputed":true,"same_selected_member_same_physical_eta0":true,"true_physical96_Theta_nu_and_radial_head_retained":true,"unknown_G_and_Btarget_inverse_not_given_numbers":true},"WPTVS_complete_original_scalar_archive":{"WHV_previous_actual_progress":{"matrix_allocations":0,"new_maxima_completed":3,"new_required_N_diagnostics_completed":1,"new_scalar_records_completed":18,"new_strict_comparisons_completed":1,"old_targets_recomputed":0},"WHV_previous_required_N_diagnostic":{"diagnostic_is_not_a_finite_inverse":true,"exceeds_256_digits":false,"formula":"floor(saved numerator upper)+1","required_N_decimal":"145475","resource_cap_N":4096,"tested_N":4096,"tested_output_dimension":790528,"within_declared_cap":false},"WHV_previous_strict_mesh_gate":{"comparison":"saved epsilon upper < 1","epsilon_record":{"ball":"[35.5162849016096175926993926870198490179833360745262969087788838134567295951 +/- 4.46e-74]"},"passed":false},"WHV_readonly_records":{"A_c":{"ball":"[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]"},"A_c_weight":{"ball":"[0.0187979816503496541345324625056530986003947533773800386267688853972524679326 +/- 2.11e-77]"},"pi":{"ball":"[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]"}},"original_nine":{"A_c_raw":"23/2","C_b":{"ball":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","lower":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","upper":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]"},"C_c":{"ball":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","lower":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","upper":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]"},"G_c":"62286/125","L_c_raw":"58/5","R":"25/8","c_body":"1192029371497/5000000000000","rstar_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"shell_1153":{"ball":"1153.00000000000000000000000000000000000000000000000000000000","lower":"1153.00000000000000000000000000000000000000000000000000000000","upper":"1153.00000000000000000000000000000000000000000000000000000000"}}},"WPTVS_mesh_summary":{"all_full_delta_mean_and_low_columns_retained":true,"body_cut":"1192029371497/5000000000000","declared_refinements":[1,2],"homogeneous_raw_transmission_is_identity":true,"original_closed_rows":4650,"original_interfaces":3594,"parent_cap":161,"parent_cells":153,"reference_mean_and_low_1_to_32_zero_only_in_centre":true,"reference_q_binary_places":20,"reference_q_floor":"1/8","refined_cap":322,"refined_counts":[153,306],"right":"25/8","root":["1191984371497/5000000000000","2383968743003/10000000000000"],"rule":"root collar plus eight subcells of each original-rminus doubling band"},"WPTVS_original_scope":{"complete_infinite_BVP_inverse_proved":false,"entire_positive_interval":["the genuine intrinsic root","25/8"],"fixed_body_cut":"1192029371497/5000000000000","full_low_high_Schur_inverse_proved":false,"given_complete_head_positive_high_inverse_and_root_graph_proved":true,"independent_even_mean_and_all_head_and_affine_source_ports_retained":true,"nu_family":"nu_delta=nu0+delta; its compact intrinsic bump is identically zero on this positive interval","ordinary_source_contract":"L2_r H_phi^(-2/3); supplied complete head forcing included","physical_parameter":"same fixed physical eta0","raw_state_contract":"L2_r H_phi^(-1), independent mean is separate","same_genuine_forward_and_backward_Riccati_reference":true},"WPTVS_parameters":{"actual_delta_degree":96,"bits":320,"first_high_index":97,"head_dimension":193,"maximum_doubling_bands":20,"maximum_parent_cells":161,"maximum_refined_cells":322,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"physical_high_minimum":388,"reference_centre_degree":32,"reference_q_binary_places":20,"reference_q_floor":"1/8","uniform_refinements":[1,2]},"WPTVS_retained_scope":{"complete_193_head_components":true,"complete_coupled_head_inverse_proved":false,"finite_matrix_inverse_proved":false,"full_mean_and_affine_jump_ports_retained":true,"new_array_artifacts":false,"old_negative_head_and_metric_obligations_retained":true,"old_targets_recomputed":0,"only_centre_reference_mean_column_has_exact_zero_high_image":true,"ordinary_dr_and_normalized_real_reflection":true,"physical_96_signed_inverse_proved":false,"reference_is_not_a_certified_actual_point_value":true,"same_positive_given_head_realization":true,"selected_member_scope_retained":true,"true_outer_chart_and_all_cross_terms_retained":true},"all_seven_primal_dual_ports_and_true_mean_rows_retained":true,"complete_actual_source_output_last_j":352,"full_degree32_repaired_centre_and_degree96_error_distinction":true,"opaque_family_error_leg_is_a_full_output_norm_not_a_128_coordinate_projection":true,"repaired_centre_source_output_last_j":224}
```
The complete prior WPS archive is:

```json
{"all_original_complete_objects_bound_by_full_file_and_field_identity":true,"all_six_original_modal_prefix_records_and_witnesses_retained":true,"all_sixty_completed_records_read_without_reevaluation":true,"complete_original_actual_progress":{"comparison_cells":155,"complete_old_records_copied":15,"completed_new_body_parent_packets":152,"conditional_finite_inverses":0,"current_files_admitted":36,"dense_finite_matrices_allocated":0,"historical_files_admitted":19,"new_array_artifacts_published":0,"new_graphs_completed":6,"new_scalar_records_saved":60,"new_strict_finite_comparisons":1,"old_producer_imports_or_calls":0,"old_reference_bounds_reevaluated":0,"old_targets_recomputed":0,"original_body_intersections":4801,"original_closed_rows_covered":4650,"physical_state_columns_computed":0,"reference_definitions_materialized":152,"reference_modes_completed":96,"refined_cells":24480},"complete_original_completion":{"actual_returncode":0,"automatic_retry_authorized":false,"complete":true,"failure":null,"proved":true,"stage":"complete"},"complete_original_execution_file":{"bytes":35857,"git_blob_sha":"21bf7ec0d72950132e3b0c09f940069588640302","path":"topics/visible-flex-exact-nearby/notes/complete_paired_finite_residual_ci/run-43878765372-1/execution.json","role":"WPS_execution","sha256":"01d18a4461d4aef6bff42484f195a95a5889a9e4d9ebbe2da4428a5898255c71"},"complete_original_family_HL_record":{"ball":"[8.33462167969581383090549638528947504989056140645138582872846240123271117268e-7 +/- 9.38e-83]"},"complete_original_field_verification":{"all_original_fields_verified_before_science":true,"execution_field_count":45,"execution_identity_table_sha256":"cf26c87b8d71118bc0fc7d4884d894001d7ee9a251bf07030d4224b5481230ff","full_tables_are_in_the_current_pinned_readonly_module":true,"scientific_field_count":40,"scientific_identity_table_sha256":"8815e6b21e3bc6ac41669da90b9401322cacf059cc21b1e2385fa34a4a19db41"},"complete_original_finite_gate":{"actual_tail_gate_is_published_analytic_m160":true,"actual_tail_inverse_upper":3,"comparison":"saved complete E0 upper + 3 D upper T upper < 1","complete_defect_record":{"ball":"[635240.547914680796472781079076433545601541945826525748909361777135277711169 +/- 4.62e-70]"},"finite_false_gate_does_not_prove_singularity":true,"passed":false},"complete_original_manifest_file":{"bytes":48445,"git_blob_sha":"ed9aede898fcb79523a188ecee54a00763593019","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-complete-paired-finite-residual-current-inputs.json","role":"WPS_manifest","sha256":"aabc28e194b27377d26f24ec7fff03708c0ff903841881233429ab0e36b76981"},"complete_original_parameters":{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"bits":320,"complete_family_residual_last_index":352,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"head_dimension":193,"high_trial_last_index":160,"maximum_comparison_cells":155,"maximum_doubling_bands":20,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"reference_centre_degree":32,"reference_outer_impedance":"13/80","reference_q_binary_places":20,"reference_q_floor":"1/8","refined_cells":24480,"repaired_centre_residual_last_index":224,"uniform_refinement":160},"complete_original_reference_graph":{"complete":true,"new_records":{"complete_reference_Z_squared_upper":{"ball":"[0.325244790263021670854229340500966763191130041187065186982582804095207427589 +/- 1.98e-76]"},"complete_reference_column_ratio_upper":{"ball":"[482.429529648345860500906429050870908859954441304590567501918696744881243367 +/- 6.86e-74]"},"complete_reference_head_lift_upper":{"ball":"[1.15119276850709137472495296208311660424250434565746375954512397895120241471 +/- 3.49e-75]"},"complete_reference_inverse_norm_upper":{"ball":"[61.9599027302343956709314898094404382709793764974547812980960894980400694589 +/- 5.71e-75]"},"complete_reference_mean_endpoint_receiver_upper":{"ball":"1.38410177387653788304101501590789857765173564985161647200584411621093750000"},"complete_reference_odd_endpoint_receiver_upper":{"ball":"[3.34616183323104588217575464228104432693916916798288292404268617094952436711 +/- 9.60e-76]"},"complete_reference_rho_column_ratio_upper":{"ball":"[0.0713750178954633325497216565069945191780534680787286565596167745352363491347 +/- 3.76e-77]"},"complete_reference_rho_defect_upper":{"ball":"[0.0711946455974940233719867605001533801137013562387828454341984666800566225947 +/- 2.74e-78]"},"complete_reference_rho_row_ratio_upper":{"ball":"[0.0710147291195978156702770051068747739427052260522920918022719148852343557289 +/- 5.41e-78]"},"complete_reference_row_ratio_upper":{"ball":"[7.95770016221533105939468693447992893400706657251216139617134685692369149869 +/- 3.63e-75]"}}},"complete_original_reference_mode_prefix":{"completed_modes":96,"running":{"Z_squared":{"ball":"[0.325244790263021670854229340500966763191130041187065186982582804095207427589 +/- 1.97e-76]"},"odd_endpoint":{"ball":"[3.34616183323104588217575464228104432693916916798288292404268617094952436711 +/- 9.59e-76]"},"q_column":{"ball":"[482.429529648345860500906429050870908859954441304590567501918696744881243367 +/- 6.85e-74]"},"q_row":{"ball":"[7.95770016221533105939468693447992893400706657251216139617134685692369149869 +/- 3.62e-75]"},"rho_column":{"ball":"[0.0713750178954633325497216565069945191780534680787286565596167745352363491347 +/- 3.75e-77]"},"rho_row":{"ball":"[0.0710147291195978156702770051068747739427052260522920918022719148852343557289 +/- 5.40e-78]"}},"witnesses":{"Z_squared":96,"odd_endpoint":96,"q_column":96,"q_row":1,"rho_column":96,"rho_row":96}},"complete_original_retained_scope":{"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_seven_primal_dual_ports_retained":true,"complete_actual_family_degree":96,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":352,"no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"ordinary_radial_L2_measure":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_residual_last_j":224,"root_complement_dimension":97,"same_selected_positive_genuine_family":true,"whole_actual_radial_head_not_finitely_truncated":true},"complete_original_scientific_file":{"bytes":65347,"git_blob_sha":"17a70a8a6304f387d271378f31964e075ddb9594","path":"topics/visible-flex-exact-nearby/notes/complete_paired_finite_residual_ci/run-43878765372-1/actual-scientific-conclusion.json","role":"WPS_actual","sha256":"0c2467867a6eade717a1df17936729f5e6978ee49fc2cf611e183424a51e2123"},"complete_original_scientific_modules":[{"bytes":49198,"git_blob_sha":"d715c5a9449d5c1b1f5b7e51a343308b826517f0","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_paired_finite_residual.py","role":"science","sha256":"617d9f0c20ce377286baa3ebe8fea4e872b8a5433af38636a8e0152f0fa114b6"},{"bytes":40309,"git_blob_sha":"a7e0d0152fb419c26142d1093a8c9f51c2661681","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_paired_readonly.py","role":"readonly_admission","sha256":"0af96d609775fb5d7c1c4be2166af442b02ed01d24a26f04e20781d89dab6989"},{"bytes":29387,"git_blob_sha":"30335240b11759053f893e343c77d19d1d21f4db","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_paired_kernel_math.py","role":"kernel_math","sha256":"460bb6d1b6bc107d4432528c6edd3cd3c996618c4258e54498b00c4608465c4d"},{"bytes":12543,"git_blob_sha":"c0f8a543fcb0b8ca023af771ee4f485b5fbf2981","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_paired_candidate_math.py","role":"assembly_math","sha256":"6e952c61849e311fcfd1fa193a8b6e3f8a22350cec507fb4dc7d4ff9a93432ca"},{"bytes":19579,"git_blob_sha":"cc48f2e6226b0a78873d50f406c63ea79dee6907","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_paired_reference_receivers_math.py","role":"reference_math","sha256":"f7e1efd07700676240ecd79b3f48935ef295737aa182d588448f13a71c5b002e"}],"no_original_success_or_false_sufficient_gate_reclassified":true}
```
The original candidate metadata and exact repair definition are also complete copies. In particular the candidate's floating BVP success does not become a mathematical certificate, and the repaired centre is not declared an exact solution of the physical nonlinear background equations:

```json
{"amplitude":0.765,"boundary_angle":"original physical theta","coordinates":"moving phi: u=alpha*U; v=1/Cref_nu+alpha*V; theta_phi=v/mean_phi(v); B=u/v; C=1/v","exact_bump":"h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere","exact_cap_cut":"25/8","exact_float_amplitude":"6890507429876859/9007199254740992","exact_float_nu":"-2572625729470897/72057594037927936","exact_float_q_values":["562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312"],"finite_BVP_success":true,"finite_state_angle":"moving phi","kind":"floating_complete_moving_phi_Codazzi_true_regular_endpoint_branch","mathematical_certificate":false,"mean_boundary":"outer","modes":32,"new_metric_family":"E_nu=E exp(nu*h); a fixed","normalized_state_order":"moving phi: U sine modes 1..M; V cosine modes 0..M, frequency 4m","nu":-0.03570235398252099,"object_sha256":"91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848","old_waist_branch_reused":false,"original_target_fixed":false,"outer_boundary":"r=25/8 actual regular linear physical graph proposals; native proposal and true nonlinear mean/nonmean fees retained as posterior obligations","physical_frequency_factor":4,"q_vector_path":"notes/2026-11-13-R133-regular-r25over8-q256-floating.json","q_vector_sha256":"8f2471f709d5350212c3bb12a2e180fef37cbd8ced72e7ed858d6687b5fa36d9","solver_message":"The algorithm converged to the desired accuracy.","solver_status":0,"source_sha256":"3c170b9c9d2b34655107dba54b189c6a940d9f62901a61d0a3ccc5a5b398e996","waist_nonmean_complement_allowed_to_change":true}
```
```json
{"base_candidate_sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","centre_is_not_the_original_ac1_index":true,"exact_alpha":"6890507429876859/9007199254740992","exact_radial_interval":["0","25/8"],"first_piece":0,"kind":"actual_final_exact_continuous_value_repair_v1","last_piece":6143,"modes":32,"object_sha256":"91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848","offset_sequence_sha256":"c66b5d52c3cd6b07e96853e1065345360a88b7f2f967b6f1606c880b68e33875","offsets_independent_of_eta_and_nu":true,"physical_frequency_factor":4,"physical_offset_rule":"e_0=0; e_j=e_(j-1)-alpha*(y_j(r_j)-y_(j-1)(r_j))","radial_nodes_count":6145,"reference_nu":"-2572625729470897/72057594037927936","repaired_state":"u_bar=alpha*U+e_u,j; v_bar=s_eta,nu+alpha*V+e_v,j"}
```
The complete retained five maxima and both original false refinement candidates are:

```json
{"A":{"ball":"[6.74940356901263092670863707542064558979483470421701096544083933324204151513 +/- 5.00e-75]","witness":{"intersection":["4141104371497/5000000000000","466622961391443/562949953421312"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5432,"original_row":3220,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}},"B":{"ball":"[0.466864898755215147682802847367675189210571079614179169864984866403609283249 +/- 1.70e-76]","witness":{"intersection":["4141104371497/5000000000000","466622961391443/562949953421312"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5432,"original_row":3220,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}},"E_b":{"ball":"[0.108706949199471213512287647811232809190669789250317142372161453775952555797 +/- 3.27e-76]","witness":{"intersection":["5154119573546235/9007199254740992","2578310786669609/4503599627370496"],"kind":"body","left":"2850864371497/5000000000000","length_upper":"576/15625","original_piece":5041,"original_row":2699,"parent_index":122,"reference_sha256":"0bd26a6f05d03c0d97d9b707d68bf0a6b1926f608639aa130f5b0ae68f40887f","right":"3035184371497/5000000000000"}},"L":{"ball":"[163.600937025345482766219943539843512909164969214908905939645812915486345571 +/- 2.71e-73]","witness":{"intersection":["1362338887279575/2251799813685248","5451857548911283/9007199254740992"],"kind":"body","left":"2850864371497/5000000000000","length_upper":"576/15625","original_piece":5108,"original_row":2783,"parent_index":122,"reference_sha256":"0bd26a6f05d03c0d97d9b707d68bf0a6b1926f608639aa130f5b0ae68f40887f","right":"3035184371497/5000000000000"}},"U_b":{"ball":"[33.5876945136675216786627931089641014780483817436844898550706041227597166279 +/- 1.38e-74]","witness":{"intersection":["4057589653914093/4503599627370496","4061371163960643/4503599627370496"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5485,"original_row":3308,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}}}
```
```json
{"1":{"all_parent_S_D_B0_enclosures_inherited":true,"complete":true,"complete_delta_upper":{"ball":"[8453.72188139484926524116189148185715903781192999939456445363298262701028690 +/- 6.06e-73]"},"complete_feedback_upper":{"ball":"[8446.97247782583663431445325440643651344801709529517755348819214329376824538 +/- 4.26e-72]"},"complete_source_quadrature_upper":{"ball":"[51.6287117085309040517051721172442998728694537049355378143293015940257513125 +/- 4.71e-74]"},"parent_cells":153,"refined_cells":153,"refinement":1,"strict_tail_gate":false},"2":{"all_parent_S_D_B0_enclosures_inherited":true,"complete":true,"complete_delta_upper":{"ball":"[2121.93073588211317496373125153515926794598676959110090636815634847631651888 +/- 4.63e-73]"},"complete_feedback_upper":{"ball":"[2118.55603409760685950037693299744894515108935223899240088543592880969549812 +/- 1.97e-72]"},"complete_source_quadrature_upper":{"ball":"[25.8976428422867031078313173455747457418391223325533590094423404674884275229 +/- 1.74e-74]"},"parent_cells":153,"refined_cells":306,"refinement":2,"strict_tail_gate":false}}
```
## WVCA6. All 56 new complete scalar records

Every table entry is copied literally from `complete_new_graphs.<graph>.new_records.<key>.ball`. No mantissa, radius, exponent or precision was recomputed or reformatted. Each graph has exactly the three keys `complete`, `copied_records`, and `new_records`; `complete=true` and `copied_records={}` in this actual branch. The order below is the frozen scientific emit order, not the lexicographic JSON object order.

### WVCA6.1. New complete reference receivers

Exact graph: `complete_reference_receivers`; 7 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_reference_row_ratio_upper` | `[7.97735082324787653632842938963664503390313827020071126989179345185464931844 +/- 4.19e-75]` |
| `complete_reference_column_ratio_upper` | `[486.977787330046975779938579173898226975715059820565744570512752085037899685 +/- 4.05e-74]` |
| `complete_reference_rho_row_ratio_upper` | `[0.0710147291494149874157036606555120675967491554835356328950020414139439208189 +/- 9.09e-78]` |
| `complete_reference_rho_column_ratio_upper` | `[0.0713749337698706653624746053090438438896560641647760088065323021548184460405 +/- 4.31e-77]` |
| `complete_reference_inverse_norm_upper` | `[62.3281048377116916655938249683034422495567100592360841533356423062112836991 +/- 4.02e-74]` |
| `complete_reference_rho_defect_upper` | `[0.0711946036559288564790863698434927839130869973587190328050667489299067566782 +/- 4.35e-77]` |
| `complete_reference_odd_endpoint_receiver_upper` | `[3.34625387731591861546706016238280989332390627104321715047979296125274161447 +/- 4.23e-76]` |

### WVCA6.2. Complete continuous-centre high trial and source

Exact graph: `complete_high_trial_source`; 12 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_trial_raw_row_upper` | `[0.158059969644396033031793555333578511934971663951060245409466236432841574320 +/- 4.90e-76]` |
| `complete_trial_raw_column_upper` | `[0.163266392291407594524042523983114337531519914050676724427103579841459243758 +/- 3.08e-76]` |
| `complete_trial_raw_norm_upper` | `[0.160642089782005571607381394440350026038550449763765597202983545760911429467 +/- 6.81e-77]` |
| `complete_repaired_centre_body_residual_row_upper` | `[1.21396363145960090404001716687889301777313212921972316289443474089465932873 +/- 3.95e-75]` |
| `complete_repaired_centre_body_residual_column_upper` | `[1.60237076039674337394835032507185682203610951815229268925997341063573425960 +/- 7.03e-76]` |
| `complete_repaired_centre_body_residual_norm_upper` | `[1.39471137775380345425078708269803201963068037035211126325933046054655124104 +/- 2.74e-75]` |
| `complete_family_high_kernel_row_upper` | `[8.83498507404751219191258224447435755796419480453942262773927287183719483976e-8 +/- 3.24e-83]` |
| `complete_family_high_kernel_column_upper` | `[4.69019820956779431872629651325496445399268548113441902802691507557402013452e-8 +/- 4.47e-83]` |
| `complete_family_high_kernel_norm_upper` | `[6.43722231834941586977575718521981726428263001552004564005474897150078828615e-8 +/- 3.65e-83]` |
| `complete_body_ordinary_source_upper` | `[1.39471227558819460732632887100524240077635800223455206359836973394028107932 +/- 1.75e-75]` |
| `complete_high_state_error_upper` | `[2.16057243295090215876680878782484962879116266106260649890359036079873829581 +/- 1.25e-75]` |
| `complete_high_outer_trace_error_upper` | `[3.43359552327593532205211194929586398204185436008856031471664368256404291226 +/- 3.23e-75]` |

### WVCA6.3. Complete paired, difference and tail receivers

Exact graph: `complete_actual_paired_receivers`; 22 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_centre_paired_LH_row_upper` | `[0.156734652857801929293611832348179115373647315437132936852059830339568463411 +/- 1.21e-76]` |
| `complete_centre_paired_LH_column_upper` | `[287951.525043033858004730754557526094425672433850763282807794169457047690532 +/- 4.21e-70]` |
| `complete_centre_paired_LH_norm_upper` | `[212.442891896844998873627085664031439322530403993363082941194128821200560996 +/- 9.27e-74]` |
| `complete_difference_paired_LH_row_upper` | `[0.348206135266346205922070380635022635637633964826985423835728948616939109809 +/- 2.51e-76]` |
| `complete_difference_paired_LH_column_upper` | `[17380.9976554521573926573022986594090792298392566174130158382990950999528823 +/- 1.08e-71]` |
| `complete_difference_paired_LH_norm_upper` | `[77.7956941011417429706926147247258549288147980974587180008622791562504304895 +/- 1.59e-75]` |
| `complete_actual_paired_LH_upper` | `[290.238585997986741844319700388757294251345202090821800942056407977450991486 +/- 4.06e-73]` |
| `complete_centre_tail_LH_row_upper` | `[0.00368321313741463025427351243106575701309888255854425600415360018603097072470 +/- 3.98e-78]` |
| `complete_centre_tail_LH_column_upper` | `[557.120575857400347424026672796917106173837298293617040846678121750727745231 +/- 2.56e-73]` |
| `complete_centre_tail_LH_norm_upper` | `[1.43247821069710552310716915452037143341199453658520055536584524161994762448 +/- 4.62e-75]` |
| `complete_difference_tail_LH_upper` | `[0.000239474872447549565877123387398978451856557114751922199502587318420410156250 +/- 1e-83]` |
| `complete_actual_tail_LH_upper` | `[1.43271768556955307267304627790777041186385109369995247756534782893836803464 +/- 8.71e-76]` |
| `complete_low_generator_difference_row_upper` | `[0.0128592489058014088865713003235829980996247217853396528330410901995047752859 +/- 1.08e-77]` |
| `complete_low_generator_difference_column_upper` | `[647.541836867836872541826557989233456296264478235291555525019766987107494828 +/- 3.50e-73]` |
| `complete_low_generator_difference_norm_upper` | `[2.88563713193522752663284275990638722049306780909832095571031781622753267294 +/- 1.33e-76]` |
| `complete_raw_difference_LH_receiver_row_upper` | `[0.000302000117316865746680026349206437671845302658132684669415202904264474509808 +/- 1.09e-79]` |
| `complete_raw_difference_LH_receiver_column_upper` | `[15.0745859977902492564243731991842229655072326596855273337712914961838273047 +/- 7.24e-75]` |
| `complete_raw_difference_LH_receiver_norm_upper` | `[0.0674724146584056747360733865782531265644534241955409522990999819221599570594 +/- 7.41e-78]` |
| `complete_head_paired_error_upper` | `[629.977963927528451753074232140022509376762122910756764497996239456450316826 +/- 4.43e-73]` |
| `complete_outer_paired_error_upper` | `[0.668009748861650317898773152728180909126911898428967160008977637390833724807 +/- 3.49e-76]` |
| `complete_low_generator_tail_error_upper` | `[8.92181230688642656950235206958325917536711813227157108485698699951171875000e-6 +/- 1e-84]` |
| `complete_raw_difference_tail_LH_upper` | `[2.07697200735082017239482556287058501176545632915804162621498107910156250000e-7 +/- 1e-86]` |

### WVCA6.4. Complete local signed remainder and tail sources

Exact graph: `complete_local_signed_remainder`; 8 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_signed_centre_paired_source_row_upper` | `[35.5651352082448700399426718916728253470947887239215860614585485174212760942 +/- 2.69e-74]` |
| `complete_signed_centre_paired_source_column_upper` | `[824.580493752624808106010080269407909905467464700900341415098266559204863660 +/- 1.1e-75]` |
| `complete_signed_centre_paired_source_norm_upper` | `[171.249282481397321805656022568111168152751621960434260418175748534263162199 +/- 4.53e-73]` |
| `complete_signed_centre_tail_source_row_upper` | `[0.0654780805695993952301136019666556175168976122779202442417444191973460307882 +/- 2.59e-77]` |
| `complete_signed_centre_tail_source_column_upper` | `[0.356052538707058908014673014957066550000113005569943573713489174054065222726 +/- 1.44e-76]` |
| `complete_signed_centre_tail_source_norm_upper` | `[0.152688037568341320474153822197173764429631842874788211301891872396151936910 +/- 3.63e-76]` |
| `complete_actual_head_tail_source_upper` | `[3.24818732838835550234675266749946546717458680583500353718187641050641280117 +/- 1.28e-76]` |
| `complete_actual_outer_tail_source_upper` | `[0.00329752633694818512370570455349851541559429799954859134020538212927846469305 +/- 1.72e-78]` |

### WVCA6.5. Complete genuine endpoint correction

Exact graph: `complete_endpoint_correction`; 3 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_high_trace_endpoint_receiver_upper` | `[0.000261823726562487010478010319833875786038649291188519700776916266569302394863 +/- 3.96e-79]` |
| `complete_head_endpoint_correction_upper` | `[0.000898996775412377993232854275249539632940103195403833955748149059282808158504 +/- 2.09e-79]` |
| `complete_outer_endpoint_correction_upper` | `[0.125747301798272233219573267583044529335929905531082437039142463223871210165 +/- 5.04e-77]` |

### WVCA6.6. Complete actual finite residual candidate

Exact graph: `complete_actual_E_D_T`; 4 new records.

| Exact record key | Original complete ball string |
| --- | --- |
| `complete_actual_E0_upper` | `[1030.12155829976888820428455903247279721294714244866368997033266711596178681 +/- 2.89e-72]` |
| `complete_actual_D_upper` | `[858.271201652115903558599028971486308560335197204107663103647819672378941743 +/- 3.58e-73]` |
| `complete_actual_T_upper` | `[3.89782618890527307744859418436114009245075923674406965971624310945473808375 +/- 4.66e-75]` |
| `complete_actual_finite_defect_upper` | `[11066.2974592482170277255953739045070721096905053507529455902664127679013367 +/- 3.72e-71]` |

The original independent mean receiver used by the endpoint graph is the literal record in `prior_completed_candidate.complete_original_reference_graph.new_records.complete_reference_mean_endpoint_receiver_upper`. It was not reevaluated. The runtime strict comparison reads the last complete defect record; neither its radius nor a displayed decimal truncation is used as a replacement test.

## WVCA7. The five complete modal prefixes and their witnesses

There are 96 completed changed modes and zero unchanged modes. The five running maxima cover the entire declared mode range. A witness is the mode at which the saved upper comparison selected its complete bound; it is not an exact singular vector, exact matrix norm or physical solution column.

The complete final modal prefix is:

```json
{"completed_modes":96,"running":{"odd_endpoint":{"ball":"[3.34625387731591861546706016238280989332390627104321715047979296125274161447 +/- 4.22e-76]"},"q_column":{"ball":"[486.977787330046975779938579173898226975715059820565744570512752085037899685 +/- 4.04e-74]"},"q_row":{"ball":"[7.97735082324787653632842938963664503390313827020071126989179345185464931844 +/- 4.18e-75]"},"rho_column":{"ball":"[0.0713749337698706653624746053090438438896560641647760088065323021548184460405 +/- 4.30e-77]"},"rho_row":{"ball":"[0.0710147291494149874157036606555120675967491554835356328950020414139439208189 +/- 9.08e-78]"}},"status":{"all_reference_targets_copied":false,"changed_modes_completed":96,"unchanged_modes_qualified":0},"witnesses":{"odd_endpoint":{"mode":96,"origin":"new_changed_mode"},"q_column":{"mode":96,"origin":"new_changed_mode"},"q_row":{"mode":1,"origin":"new_changed_mode"},"rho_column":{"mode":96,"origin":"new_changed_mode"},"rho_row":{"mode":96,"origin":"new_changed_mode"}}}
```
The five prefix records are separately preserved in their original spelling:

| Prefix key | Complete original ball | Complete original witness |
| --- | --- | --- |
| `odd_endpoint` | `[3.34625387731591861546706016238280989332390627104321715047979296125274161447 +/- 4.22e-76]` | `{"mode":96,"origin":"new_changed_mode"}` |
| `q_column` | `[486.977787330046975779938579173898226975715059820565744570512752085037899685 +/- 4.04e-74]` | `{"mode":96,"origin":"new_changed_mode"}` |
| `q_row` | `[7.97735082324787653632842938963664503390313827020071126989179345185464931844 +/- 4.18e-75]` | `{"mode":1,"origin":"new_changed_mode"}` |
| `rho_column` | `[0.0713749337698706653624746053090438438896560641647760088065323021548184460405 +/- 4.30e-77]` | `{"mode":96,"origin":"new_changed_mode"}` |
| `rho_row` | `[0.0710147291494149874157036606555120675967491554835356328950020414139439208189 +/- 9.08e-78]` | `{"mode":96,"origin":"new_changed_mode"}` |

Each completed mode updated and durably published the complete running prefix before the next mode. Downstream whole records use the saved directed readback. The final graph record and its prefix record can consequently have slightly different outward printing radii; this note retains both literal objects and does not assert byte equality between those distinct saved slots. No old WPS modal target was reevaluated.

The completed preparation prefix records the whole domain and exact definition-chain coverage:

```json
{"detail":{"all_parents":153,"body_parents":152,"closed_rows":4650,"comparison_cells":155,"exact_reference_chain":{"count":153,"sha256":"6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"},"fine_cells":24480,"intersections":4801},"internal_packets_are_not_independent_array_targets":true,"stage":"complete"}
```
## WVCA8. Actual structural gates, runtime and progress

The 23 structural gates are separate from the false mathematical finite comparison:

| # | Exact structural gate | Passed |
| --- | --- | --- |
| 1 | `all_current_UTF8_files_and_three_fixed_contracts_verified` | true |
| 2 | `five_new_and_ten_original_definition_sources_AST_only_verified` | true |
| 3 | `all_nineteen_historical_receipts_and_original_native_bytes_verified` | true |
| 4 | `complete_original_summary_and_native_projection_identical` | true |
| 5 | `both_complete_4650_row_covers_and_3594_interfaces_verified` | true |
| 6 | `same_real_family_and_all_original_successes_verified` | true |
| 7 | `all_nine_original_literals_and_completed_WHVA_retained` | true |
| 8 | `all_five_original_cubic_parts_and_full_shape_verified` | true |
| 9 | `original_repair_whole_document_and_all_65_suprema_verified` | true |
| 10 | `actual_raw_identity_transmissions_and_full_affine_ports_retained` | true |
| 11 | `all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified` | true |
| 12 | `fixed_directed_runtime_and_one_new_entry` | true |
| 13 | `all_twenty_six_old_records_typed_and_published_tail_bound_retained` | true |
| 14 | `entire_frozen_reference_definition_chain_materialized_without_old_bounds` | true |
| 15 | `complete_continuous_parent_and_comparison_domains_admitted` | true |
| 16 | `complete_reference_receivers_saved` | true |
| 17 | `complete_high_trial_source_saved` | true |
| 18 | `complete_actual_paired_receivers_saved` | true |
| 19 | `complete_local_signed_remainder_saved` | true |
| 20 | `complete_endpoint_correction_saved` | true |
| 21 | `complete_actual_E_D_T_saved` | true |
| 22 | `all_current_inputs_and_manifest_reverified_after_new_work` | true |
| 23 | `complete_whole_candidate_shape_and_old_zero_recomputation` | true |

The complete 25-field actual progress object is:

| Exact progress key | Actual value |
| --- | --- |
| `comparison_cells` | `155` |
| `complete_old_records_copied` | `26` |
| `completed_new_body_parent_packets` | `152` |
| `conditional_finite_inverses` | `0` |
| `current_files_admitted` | `41` |
| `dense_finite_matrices_allocated` | `0` |
| `graph_old_records_copied` | `0` |
| `historical_files_admitted` | `19` |
| `new_array_artifacts_published` | `0` |
| `new_graphs_completed` | `6` |
| `new_reference_modes_computed` | `96` |
| `new_scalar_records_saved` | `56` |
| `new_strict_finite_comparisons` | `1` |
| `old_complete_records_validated` | `60` |
| `old_modal_prefix_records_retained` | `6` |
| `old_producer_imports_or_calls` | `0` |
| `old_reference_bounds_reevaluated` | `0` |
| `old_targets_recomputed` | `0` |
| `original_body_intersections` | `4801` |
| `original_closed_rows_covered` | `4650` |
| `physical_state_columns_computed` | `0` |
| `reference_definitions_materialized` | `152` |
| `reference_modes_completed` | `96` |
| `refined_cells` | `24480` |
| `unchanged_reference_modes_read` | `0` |

The scientific result has 43 root fields. This execution file has 44 root fields: the optional multi-pull retention-description field is absent because exactly four pull receipts were stored. This should not be confused with the older WPS execution's 45-field identity table, which is preserved inside the old archive.

The actual runtime was Python `3.12.14`, python-flint `0.9.0`, with 320-bit arithmetic and 75-digit scalar records. No NumPy import or old-module import occurred. The reported mathematical wall time is `704.212067529` seconds; the enclosing scientific child wall time is `715.048316152` seconds. These are runtime observations, not complexity guarantees.

The complete actual finite comparison object is:

```json
{"actual_tail_gate_is_published_analytic_m160":true,"actual_tail_inverse_upper":3,"comparison":"saved complete E0 upper + 3 D upper T upper < 1","complete_defect_record":{"ball":"[11066.2974592482170277255953739045070721096905053507529455902664127679013367 +/- 3.72e-71]"},"finite_false_gate_does_not_prove_singularity":true,"passed":false}
```
## WVCA9. Full current scope and support contract

The actual retained scope is reproduced in full:

```json
{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_reference_modes_unchanged_implies_seven_verbatim_graph_copies":true,"all_seven_primal_dual_ports_retained":true,"complete_actual_family_degree":96,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":352,"mode_reference_unchanged_implies_original_complete_modal_bound_read_only":true,"new_head_lift_analytic_upper":"6/5","new_reference_diagonal_uses_exact_complete_local_and_primitive_entries":true,"new_reference_q_rho_and_odd_endpoint_bounds_never_inherited_for_changed_modes":true,"no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"no_derivative_of_continuous_centre_BHL_needed":true,"only_actual_full96_correction_in_family_error_legs":true,"ordinary_radial_L2_measure":true,"original_WPS60_success_false_gate_and_six_modal_prefixes_retained":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"physical_mean_reference_zero_actual_mean_fully_retained":true,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_is_operator_replacement_not_a_new_physical_background":true,"repaired_centre_residual_last_j":224,"root_complement_dimension":97,"same_complete_repaired_degree32_centre_inside_Green_source":true,"same_selected_positive_genuine_family":true,"whole_actual_radial_head_not_finitely_truncated":true}
```
The complete support contract, including the centre/full-family output distinction, is:

```json
{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"all_physical_193_columns_and_seven_ports_retained":true,"centre_local_source_last_j":224,"complete_actual_source_last_j":352,"continuous_repaired_centre_in_entire_primal_trial":true,"delta_degree":96,"diagonal_is_clipped_exact_reference_not_actual_point":true,"full_family_error_is_norm_domination_not_projected_trial":true,"new_norms_do_not_reuse_old_reference_q_or_rho_defect":true,"only_full_family_difference_in_uncoupled_error_legs":true,"repaired_degree":32}
```
The complete parameter object is:

```json
{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"analytic_new_head_lift_upper":"6/5","bits":320,"complete_family_residual_last_index":352,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"head_dimension":193,"high_trial_last_index":160,"maximum_comparison_cells":155,"maximum_doubling_bands":20,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"prior_complete_paired_records":60,"prior_completed_mode_prefix_records":6,"reference_centre_degree":32,"reference_diagonal_lower_clip":"-c/32","reference_diagonal_upper_clip":"c/16","reference_impedance_lower_barrier":"1/16","reference_outer_impedance":"13/80","reference_q_binary_places":20,"reference_q_floor":"1/8","refined_cells":24480,"repaired_centre_residual_last_index":224,"same_actual_spaces_and_projections":true,"unchanged_reference_modes_are_read_only":true,"uniform_refinement":160}
```
All four actual finite Schur blocks and both right-hand sides remain unchanged. In particular no independent head function is replaced by finitely many radial samples; the finite comparison acts on the exact WIC projection together with the genuine tail. The physical 96 root-even normalization would be a boundary-condition identity only after a true inverse of this complete problem is established. This execution does not establish that inverse, construct those 96 solution columns, or remove any other physical readout conversion.

## WVCA10. Execution, publication, exact pulls and no-loss boundary

The execution has one scientific child, no automatic retry, return code $0$, no timeout, no interrupted target and no scientific failure. The child began at `2026-11-16T14:59:10.973747+00:00` and finished at `2026-11-16T15:11:06.022121+00:00`. The result and execution objects were published on the first publication attempt. The consumed marker was published before the scientific child.

All four actual pull receipts are present, rather than merely first/latest retained excerpts. The full receipt chain was independently reproduced from the initial null chain by hashing each canonical `{"previous":...,"receipt":...}` object with its final LF. The result is `eb778d7ca0196c9d17e766703f9c3ba5e13485213df075171aea9b5876b0986f`. Every actual and reviewed README diff is the empty string.

| Pull | Started UTC | Finished UTC | Before | After | Actual / reviewed diff |
| --- | --- | --- | --- | --- | --- |
| 1 | `2026-11-16T14:58:39.748297+00:00` | `2026-11-16T14:58:40.031008+00:00` | `62353730862c1defd1379abcacc3099357d09e70` | `62353730862c1defd1379abcacc3099357d09e70` | empty / empty |
| 2 | `2026-11-16T14:59:06.168798+00:00` | `2026-11-16T14:59:07.017606+00:00` | `62353730862c1defd1379abcacc3099357d09e70` | `f694f4393ac777c5fd3580339883ca85c9100dc2` | empty / empty |
| 3 | `2026-11-16T14:59:09.434754+00:00` | `2026-11-16T14:59:09.771161+00:00` | `e3fd125becf38af789e81feee0f61fc3a13ed58a` | `e3fd125becf38af789e81feee0f61fc3a13ed58a` | empty / empty |
| 4 | `2026-11-16T15:11:06.082220+00:00` | `2026-11-16T15:11:07.503340+00:00` | `e3fd125becf38af789e81feee0f61fc3a13ed58a` | `76dade3353eab3689a9ca5fa53b705cebda9e406` | empty / empty |

The common reviewed README commit is `2f72b274f8647dbf6ce236ff2185cbe22153f8e1`; the root README SHA-256 is `6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9`, and the topic README SHA-256 is `81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220`. The review receipt is the pinned `rules` input. The complete four-receipt array is 2,374 canonical bytes with SHA-256 `bd358f2413f99f482ce446ab238e1fcfcf2d48049019dca42f35c21e244caef4`.

The full child stdout has 43,989,705 bytes and SHA-256 `9feb75c93dd7672519772eda1104330514e4cd03b1d6513c052158ba99d3285c`. This account uses the complete small scientific and execution files; it did not fetch or reproduce that large log. The worker records `body_not_published_or_split=true`; there is no new log-body artifact or split array.

The exact no-loss claim is about every declared completed scientific target and every requested aggregate prefix: all six graphs, all 56 named new records, all five complete modal running records with witnesses, all original complete archive identities, and all original scopes are present in the scientific file. Private temporary coefficient packets and intermediate elementary Arb operations were not separately declared public array targets. No completed named target has been discarded to satisfy a size limit.

The final actual scientific file has 78,627 bytes, execution 37,911 bytes and report 442 bytes, each below its frozen limit. The execution's final pre-publication topic observation is 199,056,130 bytes at `76dade3353eab3689a9ca5fa53b705cebda9e406`; the final worker publication check concerns the actual additional files and the 200,000,000-byte cap. The 120,000-byte preexecution reserve was retained at the declared preexecution checks. This note does not substitute a prospective budget for an actual capacity observation.

## WVCA11. Mathematical consequence and subsequent read-only use

The published result supplies complete rigorous upper bounds for the new WVC reference, primal high residual, paired low receivers, full family corrections, tail sources, and genuine endpoint terms. The new complete defect record is smaller than the earlier saved WPS defect record, but it remains greater than the declared threshold and gives no finite inverse. No ratio or new scalar comparison was computed for this note.

A subsequent distinct candidate must retain this entire successful bound computation and its false sufficient gate. It may copy an old record only after showing that its complete operator, weights, domain and scope are unchanged. A newly changed low reference requires its own complete inverse/normalizer/two-way receiver bounds. The unchanged actual tail estimate $3$ is reusable only with the same actual spaces and tail block. The same rule applies to full high-trial error records: their reuse requires the exact same high trial and source identity, not a matching scalar name.

Every physical mean, actual endpoint and source port, affine jump, radial-head input, root97/outer96 row, prescribed96 direction, $\Theta$, $\nu$, and any remaining cokernel compatibility remains in the original problem. The completed false sufficient test is preserved as a scientific result. It does not provide a zero kernel, a signed finite normalization, an incoming inverse, or a nonlinear background/surface theorem.

## Appendix WVCA-A. Complete current and historical input identity objects

The exact ordered current-input object is `complete_current_file_receipts`, 12,199 canonical bytes, SHA-256 `45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629`. It is exactly equal to the complete manifest's `files` and the execution's `current_input_receipts`. These complete public files, pinned in WVCA2, retain every one of the 41 roles, full paths, byte counts, Git blobs and SHA-256 values; the six source/worker identities are additionally printed in WVCA2. This is a full immutable-object reference, not a replacement of the input set by selected scalar summaries.

The 19 complete historical receipts are identical in the scientific and execution files. Their full aggregate, including every native chunk offset, chunk hash, original commit, candidate-part interval and verification flag, has 13,771 canonical bytes and SHA-256 `4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac`. Every original field equals the corresponding frozen manifest field. The 13 positive-native parts and the repair retain original restoration commit `12b06502f2e4d522ca5dc16d6064267859b3a0a1`; the five original cubic parts retain `46f127c7153f5393dcd2a00f42d4c1d3662c294d`. The complete original paths and all individual part hashes remain in both exact public JSON files and in the frozen manifest.

Each historical receipt records verified compressed bytes and original Git tree/blob/size. The native parts also retain their complete uncompressed chunk lengths and hashes; the candidate and repair parts record identical original-byte materialization. The full restored native identity is given in WVCA4. These are the original 19 data objects, not rerun producers or regenerated arrays.

This note's verification consisted only of complete text reads, exact JSON/schema comparisons, literal copying, byte counts and cryptographic hashes. It did not decode native data, execute an old or new scientific producer, evaluate an Arb expression, test a new mesh, or create new mathematical values.
