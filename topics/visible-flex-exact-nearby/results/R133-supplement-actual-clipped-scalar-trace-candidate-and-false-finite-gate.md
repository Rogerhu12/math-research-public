# WCTRA — Actual clipped scalar-trace candidate, complete saved bounds, and the false finite gate

**Status.** The first WCTR scientific run completed successfully with **36 new whole scalar records and 20 literal copies**, six complete graphs, all 24 structural gates true, and all 96 low nonzero modes classified as changed. Its sufficient finite-inverse comparison is **false**. This note records the completed outcome; it does not assert an actual finite inverse, singularity, or physical-column construction.

The run is **43901776543 / 1** for `WCTR_complete_clipped_scalar_trace_candidate_v1`. The scientific JSON has 45 top-level fields; the execution JSON has 44. All 56 final records and all five separately persisted modal-prefix records are reproduced below, together with their inherited domains and the complete old scope. No scientific expression was reevaluated to prepare this note: only complete UTF8 retrieval, exact JSON parsing, byte hashes, field equality, counts, and literal transcription were used.

## 1. Primary complete records and the executed sources

Paths in this note are relative to `topics/visible-flex-exact-nearby/`. The scientific result, execution receipt, original manifest, and marker are separate full objects.


| Object and path | Bytes | Git blob | SHA256 |
| --- | --- | --- | --- |
| `notes/clipped_scalar_trace_residual_ci/run-43901776543-1/actual-scientific-conclusion.json` | 86577 | `b123f0ec9a01bd02290777ef0f86622a3db0fd5e` | `2524a11005aa6ed1f20c2a91dc61a366a8f5c355d4e39d103249cd9fa4e0a5e0` |
| `notes/clipped_scalar_trace_residual_ci/run-43901776543-1/execution.json` | 39658 | `51c9089f70cdab615d3505133544fae95f04ad16` | `d5b4b8574344656af8344e5487aa59e5fa72e34311139dd086d1fdd847ff0f5c` |
| `notes/clipped_scalar_trace_residual_ci/run-43901776543-1/report.md` | 436 | `eb83a623361b89fb0003a2d1487b104c71803c42` | `356309d6da3c83a5a5a8db8f3bd274ca87ce9ca13976e7877ca5c39d56751bd6` |
| `notes/2026-11-16-R133-clipped-scalar-trace-current-inputs.json` | 70073 | `86a51414e293e11547054f87f67ff8134431caaa` | `acf4f84aca6a15f7e50640665448cf1b864ec9cd7918772ff9c38eb426406c02` |
| `notes/clipped_scalar_trace_residual_ci/WCTR_complete_clipped_scalar_trace_candidate_v1-consumed.json` | 631 | `2ef46cd38ab3e39e2be865845bdec9133cfdf846` | `d5480fcd8eb547417881cea9a071e5254eefd4ae6c03e9a69e2aa55630d00a6d` |
| `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json` | 78627 | `746ec1e16befe8914c64521ad087c1f1dd23ab73` | `85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88` |
| `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/execution.json` | 37911 | `c8cd8e8bb863c500a1e26c009e0af76cd7cb8941` | `5e560887d2deee497cb9da5b7549af1070db36cf69a7b11077ef4a0bb4f0feb5` |


The result is linked directly at [the complete WCTR scientific JSON](../notes/clipped_scalar_trace_residual_ci/run-43901776543-1/actual-scientific-conclusion.json), [the execution JSON](../notes/clipped_scalar_trace_residual_ci/run-43901776543-1/execution.json), and [the frozen manifest](../notes/2026-11-16-R133-clipped-scalar-trace-current-inputs.json). The mathematical contract is [WCTR](R133-supplement-clipped-scalar-trace-matrix-normalizers-and-paired-circuits.md), Git blob `21491641c33a4261d6364c2107d80882d11d0e49`, 26,966 bytes, SHA256 `efe08e59290ffb483dc97f59443eb4a7100390e7d655a846b954e409d5084295`. The same-operator residual construction remains the one in [WPS](R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md), and the original actual high-tail inverse bound remains the analytic result of [WIC](R133-supplement-analytic-inherited-tail-and-weighted-impedance-circuit.md).

The actual five-source mathematical binding is:


| Role | Path | Bytes | Git blob | SHA256 |
| --- | --- | --- | --- | --- |
| `science` | `scripts/fourfold_codazzi_clipped_scalar_trace_candidate.py` | 73502 | `ca466fff42f3489c38a68e80dda402e5c4e213f9` | `569fe7a44cc282e7e6e1c7ff5133a9a07115aac22755e14ac8d26b7d04833e0b` |
| `readonly_admission` | `scripts/fourfold_codazzi_clipped_scalar_trace_readonly.py` | 99368 | `fa1e50e3c5950236db14ae72a7f6920435a8f5a0` | `b161d5183894c5661ab3526b5399307810cc6995d88dfe21100a2f16b54eb8b2` |
| `kernel_math` | `scripts/fourfold_codazzi_two_rate_centre_kernel_math.py` | 39350 | `b718d4280a366487527bccd89702eac7d352ad38` | `7e995802fa167fba0a7601cd4af5ce6044eb0b4693dc57576673356abaa00ccd` |
| `assembly_math` | `scripts/fourfold_codazzi_scalar_trace_candidate_math.py` | 18821 | `93af9e0b4689016bf5c51449324b59f6452aa1d9` | `21c0b97e1ed766c354ee77af613a2f4d17c40762902ff7c52fd82142bf18e270` |
| `reference_math` | `scripts/fourfold_codazzi_clipped_scalar_trace_reference_math.py` | 24348 | `8e92982d16180da16330ae3aac36a2bcd5c42141` | `1732fb0f119ebff661da3892f63bb140de05e0c845e780a06ca115998f199c7a` |


The public worker was `scripts/fourfold_codazzi_complete_paired_public_worker.py`, Git blob `85d72a0600816b2176093dd74ab61595fad40520`, 31,551 bytes, SHA256 `afbbae87226ee6c1ddb95944a8f21c00b6e7218a166f046ea2fc24b2ce86e437`. Its only scientific child entered the new owner after the pure preflight and published consumption marker. The actual scientific checkout was `40a91573aa3169334c9dcbf6e0479e082f85cca9`; the workflow-event commit was `ef5a809c4bf3020b9e6473b98d1864eb71fe0ba8`.

## 2. Actual branch, mathematical spaces, and complete domain

The branch is `new_scalar_trace_candidate`, and the modal-prefix provenance is `new_current_reference`. The changed indices are exactly $1,\ldots,96$; the unchanged set is empty. Therefore the all-zero-trace whole-WVC-copy branch was **not** taken. That branch remains part of the frozen contract, but its original $6/5$ lift and original false comparison cannot be substituted for this run's changed reference.

The scalar trace changes only the low reference. The actual $S,P,Q,A,B,C,R$, the high-tail space, the genuine positive realization, ordinary $dr$, the physical Fourier frequency $4j$, and all original ports are unchanged. The real low fibre still has dimension 193: 96 odd modes, 96 nonconstant even modes, and the independent even mean. The root-complement input has dimension 97, the prescribed root-even input has dimension 96, and the actual outer chart has dimension 96 in its original $H^{-5/6}$ norm. Nonconstant real Fourier vectors carry their original normalization; the physical mean is not assigned an additional $\sqrt2$.

On each declared reference parent the low matrix is

$$

D=rI+\begin{pmatrix}a&cq^2\\c&-a\end{pmatrix},
\qquad
-\frac c{32}\le a\le\frac c{16},
\qquad
-\frac c{64}\le r\le\frac c{64},
\qquad
P_h=I+\frac{h^2D^2}{12}.
\tag{WCTRA.1}

$$

The matrix normalizer $P_h^{-1}$ is kept as a matrix in the actual physical $S$ coordinates. The two propagation directions retain their distinct rates. The root reference branch and independent mean remain separate. These are reference qualifications, not point-value assertions about the actual generator. The analytic changed-reference head-lift bound is $5/4$.

The complete fixed parameters and complete current support contract are copied verbatim:


```json
{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"analytic_new_head_lift_upper":"5/4","bits":320,"complete_family_residual_last_index":352,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"head_dimension":193,"high_trial_last_index":160,"maximum_comparison_cells":155,"maximum_doubling_bands":20,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"prior_complete_paired_records":60,"prior_complete_tracefree_records":56,"prior_completed_mode_prefix_records":6,"prior_completed_tracefree_modal_prefix_records":5,"reference_centre_degree":32,"reference_diagonal_lower_clip":"-c/32","reference_diagonal_upper_clip":"c/16","reference_impedance_lower_barrier":"1/16","reference_matrix_normalizer":"I+h^2*D^2/12","reference_outer_impedance":"13/80","reference_q_binary_places":20,"reference_q_floor":"1/8","reference_scalar_trace_lower_clip":"-c/64","reference_scalar_trace_upper_clip":"c/64","refined_cells":24480,"repaired_centre_residual_last_index":224,"same_actual_spaces_and_projections":true,"unchanged_reference_modes_are_read_only":true,"uniform_refinement":160,"whole_zero_trace_candidate_is_read_only":true}
```


```json
{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"all_physical_193_columns_and_seven_ports_retained":true,"both_distinct_Green_propagation_rates_and_all_twenty_copy_domains_retained":true,"centre_local_source_last_j":224,"complete_actual_source_last_j":352,"continuous_repaired_centre_in_entire_primal_trial":true,"delta_degree":96,"diagonal_is_clipped_exact_reference_not_actual_point":true,"full_family_error_is_norm_domination_not_projected_trial":true,"new_norms_do_not_reuse_old_reference_q_or_rho_defect":true,"only_full_family_difference_in_uncoupled_error_legs":true,"repaired_degree":32,"scalar_trace_changes_only_low_reference_with_full_matrix_normalizer":true}
```


The interval is the selected genuine positive interval from the intrinsic root to $25/8$. The original root enclosure, exact body cut, repaired degree-32 centre, and full degree-96 family-error domain are retained in §6. The repaired-centre residual output extends through angular index 224; the complete actual-family residual extends through 352. The latter is paid as a whole output norm, never relabelled as a projection to the finite centre trial coordinates.

The preparation completed 153 parents, of which 152 are body parents; 4,801 intersections cover all 4,650 original closed rows, while 155 comparison cells also retain the declared cutoff breakpoints. The inherited refinement is $m=160$, giving 24,480 reference cells. The formal finite dimension $193N+193=4,724,833$ is a coordinate count only: no such dense matrix and no physical state columns were allocated or computed.

All three definition chains are saved independently:


| Definition chain | Count | SHA256 |
| --- | --- | --- |
| Original exact reference chain | 153 | `6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac` |
| Complete clipped tracefree diagonal | 153 | `b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2` |
| Complete clipped scalar trace | 153 | `3b2d237885c9e0ab4b74a9662259e076c1a62794f97c06d81ae4e1d64ebde214` |


```json
{"detail":{"all_parents":153,"body_parents":152,"closed_rows":4650,"comparison_cells":155,"exact_reference_chain":{"count":153,"sha256":"6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"},"fine_cells":24480,"intersections":4801},"internal_packets_are_not_independent_array_targets":true,"stage":"complete"}
```


The complete current retained-scope object is:


```json
{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_seven_primal_dual_ports_retained":true,"all_zero_trace_implies_whole_completed_WVC_candidate_copy":true,"complete_actual_family_degree":96,"copied_whole_graphs_preserve_original_new_records_labels_as_original_provenance":true,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":352,"full_matrix_normalizer_and_both_distinct_Green_rates_retained":true,"mode_reference_unchanged_implies_original_complete_modal_bound_read_only":true,"new_head_lift_analytic_upper":"5/4","new_reference_diagonal_uses_exact_complete_local_and_primitive_entries":true,"new_reference_q_rho_and_odd_endpoint_bounds_never_inherited_for_changed_modes":true,"no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"no_derivative_of_continuous_centre_BHL_needed":true,"only_actual_full96_correction_in_family_error_legs":true,"ordinary_radial_L2_measure":true,"original_WPS60_success_false_gate_and_six_modal_prefixes_retained":true,"original_WVC56_success_false_gate_and_five_modal_prefixes_retained":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"physical_mean_reference_zero_actual_mean_fully_retained":true,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_is_operator_replacement_not_a_new_physical_background":true,"repaired_centre_residual_last_j":224,"root_complement_dimension":97,"same_complete_repaired_degree32_centre_inside_Green_source":true,"same_selected_positive_genuine_family":true,"scalar_trace_changes_low_reference_only_actual_spaces_are_unchanged":true,"twelve_high_seven_unchanged_tail_one_outer_tail_records_are_verbatim_copies":true,"whole_actual_radial_head_not_finitely_truncated":true,"whole_copy_branch_retains_original_six_fifths_lift_and_false_gate":true}
```


## 3. All six complete graphs: 36 new records and 20 literal copies

Every following `ball` string is transcribed from the complete scientific JSON. No decimal has been shortened, reparsed as a new bound, or rerounded for this note. Tables follow the declared target and record order in the frozen manifest, not the incidental sorted-key order of JSON.

A record labelled **COPY** is the exact old object at its declared WVC path. All 20 objects were independently compared with the complete WVC scientific file; their combined canonical JSON identity is 2,875 bytes, SHA256 `4a32dc9dcb5b3e6abf72eaf66cc74baa30bfa8bf309dfe2ac97d9ee3086995b6`. The copy split is twelve complete high-trial records, seven unchanged tail records, and one outer-tail record. Their qualification is operator-specific: none of these twenty requires the changed low Green receiver. New $q$, normalizer-defect, odd-endpoint, and low-reference-dependent receiver bounds are paid in this run.


### 3.1. complete_reference_receivers

Seven new complete reference receivers. These include all changed modes, both endpoint atoms, the independent mean, the real Fourier/Riesz factors, and the full matrix normalizer.

Saved slots: **7**; new: **7**; copied: **0**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_reference_row_ratio_upper` | NEW | `[7.97735082324787671512007645550532348964402484620298065746649809023094293050 +/- 3.04e-75]` |
| `complete_reference_column_ratio_upper` | NEW | `[485.535956532333528544402106907074355014233201912743563287156850198925573154 +/- 8.30e-74]` |
| `complete_reference_rho_row_ratio_upper` | NEW | `[0.114065604358634312080674619502544488866377081560718480846683981850253934885 +/- 4.28e-76]` |
| `complete_reference_rho_column_ratio_upper` | NEW | `[0.114641030159672787938484661390051662864872847175107035918517512063974650429 +/- 3.14e-76]` |
| `complete_reference_inverse_norm_upper` | NEW | `[62.2357667467803931290983358391391629968768690074526497838894698563621027221 +/- 4.33e-74]` |
| `complete_reference_rho_defect_upper` | NEW | `[0.114352955315809394196965510065258234159131876497051950974012931018004142920 +/- 8.98e-77]` |
| `complete_reference_odd_endpoint_receiver_upper` | NEW | `[3.34420175402704915823643478181500008600597782378873289041752104302084485659 +/- 4.78e-76]` |

### 3.2. complete_high_trial_source

Twelve exact copies of the complete prior high trial. The high trial, its continuous repaired-centre source, the full degree-96 error leg, both source intervals, and the actual trace domains are unchanged. No new high trial or high residual was computed.

Saved slots: **12**; new: **0**; copied: **12**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_trial_raw_row_upper` | COPY | `[0.158059969644396033031793555333578511934971663951060245409466236432841574320 +/- 4.90e-76]` |
| `complete_trial_raw_column_upper` | COPY | `[0.163266392291407594524042523983114337531519914050676724427103579841459243758 +/- 3.08e-76]` |
| `complete_trial_raw_norm_upper` | COPY | `[0.160642089782005571607381394440350026038550449763765597202983545760911429467 +/- 6.81e-77]` |
| `complete_repaired_centre_body_residual_row_upper` | COPY | `[1.21396363145960090404001716687889301777313212921972316289443474089465932873 +/- 3.95e-75]` |
| `complete_repaired_centre_body_residual_column_upper` | COPY | `[1.60237076039674337394835032507185682203610951815229268925997341063573425960 +/- 7.03e-76]` |
| `complete_repaired_centre_body_residual_norm_upper` | COPY | `[1.39471137775380345425078708269803201963068037035211126325933046054655124104 +/- 2.74e-75]` |
| `complete_family_high_kernel_row_upper` | COPY | `[8.83498507404751219191258224447435755796419480453942262773927287183719483976e-8 +/- 3.24e-83]` |
| `complete_family_high_kernel_column_upper` | COPY | `[4.69019820956779431872629651325496445399268548113441902802691507557402013452e-8 +/- 4.47e-83]` |
| `complete_family_high_kernel_norm_upper` | COPY | `[6.43722231834941586977575718521981726428263001552004564005474897150078828615e-8 +/- 3.65e-83]` |
| `complete_body_ordinary_source_upper` | COPY | `[1.39471227558819460732632887100524240077635800223455206359836973394028107932 +/- 1.75e-75]` |
| `complete_high_state_error_upper` | COPY | `[2.16057243295090215876680878782484962879116266106260649890359036079873829581 +/- 1.25e-75]` |
| `complete_high_outer_trace_error_upper` | COPY | `[3.43359552327593532205211194929586398204185436008856031471664368256404291226 +/- 3.23e-75]` |

### 3.3. complete_actual_paired_receivers

Fifteen new low-reference-dependent records and seven literal tail copies. The ordinary source and paired receivers retain all seven original ports; disjoint source intervals are combined in their original input norm, without assuming orthogonality of the resulting states.

Saved slots: **22**; new: **15**; copied: **7**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_centre_paired_LH_row_upper` | NEW | `[0.156640911330022427819946815928289252540731766714436038288708529946357460209 +/- 1.52e-76]` |
| `complete_centre_paired_LH_column_upper` | NEW | `[288017.538065216086875719798149904766665056838851601624372914888998084143407 +/- 3.23e-70]` |
| `complete_centre_paired_LH_norm_upper` | NEW | `[212.403694980960424032905708274465554110764909168135041923108124363626708160 +/- 4.50e-73]` |
| `complete_difference_paired_LH_row_upper` | NEW | `[0.348212281396251487263169844997615737351701049820744114462887914306288997770 +/- 5.88e-77]` |
| `complete_difference_paired_LH_column_upper` | NEW | `[17359.5944978410118055708639702880217544794008056949968510552493142516825541 +/- 8.27e-72]` |
| `complete_difference_paired_LH_norm_upper` | NEW | `[77.7484662498690930557153140263197033748107752732186812891743603205214203819 +/- 2.43e-74]` |
| `complete_actual_paired_LH_upper` | NEW | `[290.152161230829517088621022300785257485575684441353723212282484684148128542 +/- 3.75e-73]` |
| `complete_centre_tail_LH_row_upper` | COPY | `[0.00368321313741463025427351243106575701309888255854425600415360018603097072470 +/- 3.98e-78]` |
| `complete_centre_tail_LH_column_upper` | COPY | `[557.120575857400347424026672796917106173837298293617040846678121750727745231 +/- 2.56e-73]` |
| `complete_centre_tail_LH_norm_upper` | COPY | `[1.43247821069710552310716915452037143341199453658520055536584524161994762448 +/- 4.62e-75]` |
| `complete_difference_tail_LH_upper` | COPY | `[0.000239474872447549565877123387398978451856557114751922199502587318420410156250 +/- 1e-83]` |
| `complete_actual_tail_LH_upper` | COPY | `[1.43271768556955307267304627790777041186385109369995247756534782893836803464 +/- 8.71e-76]` |
| `complete_low_generator_difference_row_upper` | NEW | `[0.0128592566000879649160892363232816480874164766673083784912638737303048962293 +/- 7.82e-78]` |
| `complete_low_generator_difference_column_upper` | NEW | `[646.744446506878763837537358766252787630172538555204458453107191905661572249 +/- 2.00e-73]` |
| `complete_low_generator_difference_norm_upper` | NEW | `[2.88386074426519744016036321942911155160804353053646893690122951483987031239 +/- 1.89e-75]` |
| `complete_raw_difference_LH_receiver_row_upper` | NEW | `[0.000302005447871857317661031955765495002039636643383125858163822995929131828075 +/- 3.62e-79]` |
| `complete_raw_difference_LH_receiver_column_upper` | NEW | `[15.0560229816487526501048256463903050776057248965264500009152205674342433253 +/- 1.81e-74]` |
| `complete_raw_difference_LH_receiver_norm_upper` | NEW | `[0.0674314538160182940639334900488462301602868822837976420547912925589951607823 +/- 1.01e-77]` |
| `complete_head_paired_error_upper` | NEW | `[629.789453990379001011965154566845602506938043249166102048028818709284743990 +/- 2.73e-73]` |
| `complete_outer_paired_error_upper` | NEW | `[0.667810834624228678932961226826575225701415022810365157818698123230114942189 +/- 2.38e-76]` |
| `complete_low_generator_tail_error_upper` | COPY | `[8.92181230688642656950235206958325917536711813227157108485698699951171875000e-6 +/- 1e-84]` |
| `complete_raw_difference_tail_LH_upper` | COPY | `[2.07697200735082017239482556287058501176545632915804162621498107910156250000e-7 +/- 1e-86]` |

### 3.4. complete_local_signed_remainder

Seven new complete signed-centre and head-tail records plus the old complete outer-tail source. Signed local coefficients are combined before taking their majorants. The full family-error leg is not projected to the centre band.

Saved slots: **8**; new: **7**; copied: **1**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_signed_centre_paired_source_row_upper` | NEW | `[35.5651352082448700399426718916728253470947887239215860614585485174212760942 +/- 2.69e-74]` |
| `complete_signed_centre_paired_source_column_upper` | NEW | `[824.580493752622268233531811296656941217724339366021320972007586652414020187 +/- 4.69e-73]` |
| `complete_signed_centre_paired_source_norm_upper` | NEW | `[171.249282481397058064673308819680805690148583326065338419220824983053741332 +/- 3.04e-73]` |
| `complete_signed_centre_tail_source_row_upper` | NEW | `[0.0649534815463430897643177342950596245982727548242912991754259626467316821275 +/- 3.62e-77]` |
| `complete_signed_centre_tail_source_column_upper` | NEW | `[0.341275555933470341099257879085701668544216013380820319652855880822288095568 +/- 2.37e-76]` |
| `complete_signed_centre_tail_source_norm_upper` | NEW | `[0.148885981625345254511655139480378030591403991983897236471854749428392149118 +/- 4.70e-77]` |
| `complete_actual_head_tail_source_upper` | NEW | `[3.24438527244535943638425398478266973333635895494411256235183928753865301338 +/- 2.45e-75]` |
| `complete_actual_outer_tail_source_upper` | COPY | `[0.00329752633694818512370570455349851541559429799954859134020538212927846469305 +/- 1.72e-78]` |

### 3.5. complete_endpoint_correction

Three new complete endpoint records, including the actual high trace and the original outer-chart factors. The cutoff trial's own endpoint behaviour does not remove any independent physical boundary input.

Saved slots: **3**; new: **3**; copied: **0**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_high_trace_endpoint_receiver_upper` | NEW | `[0.000261701797601386560282886000127460109760245808370769103896361254892633142891 +/- 1.12e-79]` |
| `complete_head_endpoint_correction_upper` | NEW | `[0.000898578120677385801782442202522394936472936175960903345477061309343420136653 +/- 4.07e-80]` |
| `complete_outer_endpoint_correction_upper` | NEW | `[0.125670224799999098360887713913106021767478454704291257011292564065571577132 +/- 4.63e-76]` |

### 3.6. complete_actual_E_D_T

Four new final complete residual records. The conditional positive-gap and finite-inverse records are absent because the sufficient comparison is false.

Saved slots: **4**; new: **4**; copied: **0**. The graph's `complete` field is true.


| Record | Provenance | Complete saved ball |
| --- | --- | --- |
| `complete_actual_E0_upper` | NEW | `[1116.04013049930202499328385700767925382517418213356285462841890530482287939 +/- 2.75e-72]` |
| `complete_actual_D_upper` | NEW | `[892.640781887886161009562724215532270751116788155931016499052359716794865560 +/- 1.97e-73]` |
| `complete_actual_T_upper` | NEW | `[4.05548293117160566544731829486680362573969556407563708627708386733334580582 +/- 3.73e-75]` |
| `complete_actual_finite_defect_upper` | NEW | `[11976.3084943412975160733375622585417781999325190728969012943513815153166543 +/- 4.93e-71]` |


## 4. Five complete modal prefixes and their witnesses

Each completed mode was durably saved before the next mode. The last prefix contains 96 completed modes: 96 changed and zero unchanged. All five witnesses identify a genuinely new changed mode, rather than a restriction of an old global bound.

These prefix objects and the final graph records are **distinct complete saved objects**. The owner saves the prefix, reads the directed endpoint back, and then emits the final graph record. Consequently the centres coincide here while the final radii increase by one last displayed unit. Neither object is replaced by the other in this record.


| Prefix key | Complete prefix ball | Witness | Corresponding final record |
| --- | --- | --- | --- |
| `q_row` | `[7.97735082324787671512007645550532348964402484620298065746649809023094293050 +/- 3.03e-75]` | `{"mode":1,"origin":"new_changed_mode"}` | `complete_reference_row_ratio_upper` |
| `q_column` | `[485.535956532333528544402106907074355014233201912743563287156850198925573154 +/- 8.29e-74]` | `{"mode":96,"origin":"new_changed_mode"}` | `complete_reference_column_ratio_upper` |
| `rho_row` | `[0.114065604358634312080674619502544488866377081560718480846683981850253934885 +/- 4.27e-76]` | `{"mode":96,"origin":"new_changed_mode"}` | `complete_reference_rho_row_ratio_upper` |
| `rho_column` | `[0.114641030159672787938484661390051662864872847175107035918517512063974650429 +/- 3.13e-76]` | `{"mode":96,"origin":"new_changed_mode"}` | `complete_reference_rho_column_ratio_upper` |
| `odd_endpoint` | `[3.34420175402704915823643478181500008600597782378873289041752104302084485659 +/- 4.77e-76]` | `{"mode":96,"origin":"new_changed_mode"}` | `complete_reference_odd_endpoint_receiver_upper` |


The complete prefix status is:


```json
{"all_reference_targets_copied":false,"changed_modes_completed":96,"unchanged_modes_qualified":0}
```


## 5. Complete final comparison and exact completion boundary

Let $e_\rho$ be the new complete reference-normalizer defect; let $K_H$ be the complete signed-centre paired-source bound, $\epsilon_H,\epsilon_b$ the complete head and outer paired errors, $o_H,o_b$ the complete endpoint corrections, and $t_H,t_b$ the complete head and outer tail-source bounds, all in the units recorded above. With $w_0=5/4$, the ordered WCTR assembly retains

$$

\begin{aligned}
h&=K_H+\epsilon_H,\\
E_0&=e_\rho+(1+e_\rho)\sqrt{w_0^2h^2+\epsilon_b^2}
             +\sqrt{w_0^2o_H^2+o_b^2},\\
D&=(1+e_\rho)h+o_H,\\
T&=\sqrt{w_0^2t_H^2+t_b^2},\\
\delta_{\mathrm{finite}}&=E_0+3DT.
\end{aligned}
\tag{WCTRA.2}

$$

All four finite Schur blocks and both original right-hand sides remain represented. In particular, the old outer-tail source is copied as its original whole object, but the final $T$ is newly assembled with the changed-reference lift; it is not an inherited old final $T$.

The actual final gate, including its entire qualification, is:


```json
{"actual_tail_gate_is_published_analytic_m160":true,"actual_tail_inverse_upper":3,"comparison":"saved complete E0 upper + 3 D upper T upper < 1","complete_defect_record":{"ball":"[11976.3084943412975160733375622585417781999325190728969012943513815153166543 +/- 4.93e-71]"},"finite_false_gate_does_not_prove_singularity":true,"passed":false}
```


Its saved defect is much larger than one, so this particular sufficient comparison does not prove an actual finite inverse. The false comparison does not prove singularity. The published analytic same-actual-tail bound $\|R^{-1}\|\le3$ is retained; it does not convert the reference circuit or this failed finite comparison into an actual inverse.

The existing WVC false comparison remains its own complete result:


```json
{"actual_tail_gate_is_published_analytic_m160":true,"actual_tail_inverse_upper":3,"comparison":"saved complete E0 upper + 3 D upper T upper < 1","complete_defect_record":{"ball":"[11066.2974592482170277255953739045070721096905053507529455902664127679013367 +/- 3.72e-71]"},"finite_false_gate_does_not_prove_singularity":true,"passed":false}
```


The completed WCTR state is `complete=true`, `proved=true`, `stage="complete"`, `actual_returncode=0`, with `failure=null` and `current_target=null`. Here `proved` classifies completion of the declared positive-bound target, not a positive finite-inverse gate. The conditional inverse object is null; no conditional gap or inverse record was emitted. All six started target graphs are complete, so there is no interrupted graph and no missing completed scientific target.

The full 26-entry progress object is:


```json
{"comparison_cells":155,"complete_old_records_copied":44,"completed_new_body_parent_packets":152,"conditional_finite_inverses":0,"current_files_admitted":45,"dense_finite_matrices_allocated":0,"graph_old_records_copied":20,"historical_files_admitted":19,"new_array_artifacts_published":0,"new_graphs_completed":6,"new_reference_modes_computed":96,"new_scalar_records_saved":36,"new_strict_finite_comparisons":1,"old_complete_records_validated":116,"old_modal_prefix_records_retained":11,"old_producer_imports_or_calls":0,"old_reference_bounds_reevaluated":0,"old_targets_recomputed":0,"original_body_intersections":4801,"original_closed_rows_covered":4650,"physical_state_columns_computed":0,"reference_definitions_materialized":152,"reference_modes_completed":96,"refined_cells":24480,"unchanged_reference_modes_read":0,"whole_old_graphs_copied":0}
```


This supplies the exact zero-recomputation and no-loss boundary: old producer calls, old target recomputations, reevaluated old reference bounds, dense finite matrices, physical state columns, and conditional finite inverses are all zero. The 36 new scalar records, 20 graph copies, 44 initially retained old records, and eleven old modal prefixes are distinct accounting categories. None is silently counted as another.

## 6. Complete old records, scope, candidate, repair, and false predecessors

The following whole-object identities were recomputed by pure JSON serialization with the original number lexemes retained. Each object matches the completed WVC object's bytes and SHA256 as well as the WCTR manifest's immutable qualification.


| Complete object | Canonical bytes including LF | SHA256 |
| --- | --- | --- |
| `copied_original_records` | 2627 | `b313df918a9ec86507695b49ba8eb5c5a75afbe268faeffdb14ece854f1f2e71` |
| `copied_original_scope` | 8502 | `94c595173f4591660211251da7f67ea47e15fd52749167379f5ff4c50909736b` |
| `copied_complete_candidate_metadata` | 2581 | `aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356` |
| `copied_complete_repair_definition` | 792 | `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` |
| `retained_completed_five_maxima` | 2350 | `407ca196cf8f60ac7c037cd2c2056673e139ecd4c1ecc4343d78a5cbf99a6f74` |
| `retained_original_false_candidates` | 1082 | `af586adb9e63165b204717ac8ace80c2d05285940573a1f7bdc39599b89ae187` |
| `complete_restoration_receipts` | 13771 | `4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac` |
| `prior_completed_candidate` | 14022 | `02b6e495f027720d060e5a9c90b77cba2577ebe3d3e0f9ed8eb0260c301112bb` |


### 6.1. All fifteen original typed records

The complete objects are retained, including any original `lower` and `upper` display fields and exact rational strings. They are not replaced by new one-field `ball` objects.


```json
{"A_c":{"ball":"[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]"},"C_b":{"ball":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","lower":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","upper":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]"},"C_c":{"ball":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","lower":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","upper":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]"},"E_minus":{"ball":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]","lower":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]","upper":"[5.94160018366257742661582890287045114982937168544495011198565e-5 +/- 4.03e-65]"},"G_c":"62286/125","L_c_raw":"58/5","P_b_raw":{"ball":"[0.00230158835209555496325236476227310039199272102107215008177573464882078520759 +/- 2.64e-78]"},"Y_b":{"ball":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]","lower":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]","upper":"[0.608734661261768448195914731776755868299816356832885661258800 +/- 3.88e-61]"},"Y_b_outer":{"ball":"[0.00365769892351436839526506567363676924340713180672188755030293063817866017188 +/- 2.60e-78]"},"Y_c":{"ball":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]","lower":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]","upper":"[0.0434328598621432921156685860637129684053125066160929027915269 +/- 3.53e-62]"},"lambda_388_minus_two_thirds":{"ball":"[0.0187979816503496541345324625056530986003947533773800386267688853972524679326 +/- 2.11e-77]"},"mu_minus":{"ball":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]","lower":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]","upper":"[4.55188348365545288401339859218169180923420577078725734379278e-5 +/- 5.80e-66]"},"pi":{"ball":"[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]"},"reciprocal_sqrt_two":{"ball":"[0.707106781186547524400844362104849039284835937688474036588339868995366239231 +/- 5.51e-77]"},"shell_1153":{"ball":"1153.00000000000000000000000000000000000000000000000000000000","lower":"1153.00000000000000000000000000000000000000000000000000000000","upper":"1153.00000000000000000000000000000000000000000000000000000000"}}
```


The independent physical-mean reference bound and complete original full-family high-from-low error are separate original whole objects:


```json
{"complete_original_family_HL_record":{"ball":"[8.33462167969581383090549638528947504989056140645138582872846240123271117268e-7 +/- 9.38e-83]"},"complete_original_mean_reference_record":{"ball":"1.38410177387653788304101501590789857765173564985161647200584411621093750000"}}
```


### 6.2. Complete inherited scope

This is the full 8,502-byte compact canonical object `copied_original_scope`, not a selected subset. It retains the original exact root interval and body cut, ordinary source/state windows, rough stable and outer windows, selected member, full mean and affine ports, old WHVA failed $N=4096$ test and required-$N$ diagnostic, both original $m=1,2$ failed-tail domains, and all original finite/nonlinear obligations.


```json
{"WOBSA_complete_positive_columns":{"actual_root_stable_input_zero":true,"body_source_choice_read_verbatim":"A_b_from_L","complete":true,"complete_new_records":{"complete_head_outer_trace_upper":{"ball":"[3.03093313443307949770085689259592195423369435349649052364971666602569752377 +/- 5.82e-76]"},"complete_head_root_unstable_upper":{"ball":"[0.757733283608269874425214223148980488558423588374122630912429166506424380942 +/- 3.55e-76]"},"complete_outer_b_outer_trace_upper":{"ball":"[0.00365769892351436839526506567363676924340713180672188755030293063817866017188 +/- 2.60e-78]"},"complete_outer_b_raw_state_upper":{"ball":"[0.00230158835209555496325236476227310039199272102107215008177573464882078520759 +/- 2.64e-78]"},"complete_outer_b_root_unstable_upper":{"ball":"[0.000914424730878592098816266418409192310851782951680471887575732659544665042971 +/- 3.52e-79]"},"complete_outer_b_to_head_source_upper":{"ball":"[175.711718635860624882734290849864754541321815546548694593851449145066243980 +/- 3.54e-73]"}},"disjoint_original_source_intervals":true,"full_original_seven_input_oracle_retained":true,"kind":"complete_positive_head_and_outer_columns_v1","original_C_P_and_C_K_read_without_recomputation":true,"output_orthogonality_assumed":false,"proof_formulas":"WOB.9-WOB.12","raw_output_window":"whole L2_dr H^-1 with independent mean separate","source_window":"ordinary L2_dr H^-2/3"},"WOBSA_parameters":{"actual_pR_upper":"1/5","arithmetic_bits":320,"copied_original_records":42,"decimal_record_digits":75,"exact_original_contour_shift":"1/512","exact_real_delta_radius":"1/100000000","exact_trial_cutoff_support_length":"3/1000000","first_high_abs_j":97,"fixed_intrinsic_parameter":"eta_0","head_dimension":193,"historical_inputs":0,"last_low_abs_j":96,"new_complete_graphs":6,"new_exponentials":1,"new_fractional_powers":1,"new_saved_records":37,"new_square_roots":7,"normalized_angular_measure":true,"old_scientific_target_recomputations_allowed":0,"original_frozen_common_input":"Xfr = S_star D_plus H_nat^(-4/3)","original_outer_high_and_low_window":"H^-5/6","original_raw_state_window":"ordinary L2_dr H^-1","original_rough_stable_window":"H^-3/2","original_same_negative_source_window":"ordinary L2_dr H^-2/3 with independent mean","physical_frequency":"n=4|j|","physical_period":"pi/2","same_selected_member_only":true},"WOBSA_retained_scope":{"CF288_whole_common_factor_no_upper_division_or_subtraction":true,"Ni_and_stable_inverse_in_original_right_order_once":true,"PW_receiver_applied_only_to_zero_stable_additional_state":true,"WSP_complete_RH_source_not_received_positive_bound":true,"actual_outer_y_coordinate_not_identified_with_raw_endpoint":true,"all_new_targets_are_complete_positive_bounds_in_original_units":true,"all_six_complete_original_receipts_read_without_old_math":true,"complete_original_37_records_plus_five_typed_factors_retained":true,"finite_signed_inverse_proved":false,"full_actual_pR_upper_from_exact_same_family_body":true,"full_incoming_inverse_proved":false,"full_low193_rows_and_independent_even_mean_retained":true,"full_source_jump_root_mean_and_cokernel_rows_retained":true,"independent_physical_coordinates_receive_no_Ni":true,"mean_and_amplitude_rows_not_claimed_zero":true,"new_whole_comparisons":0,"nonlinear_background_or_surface_proved":false,"old_whole_bounds_not_subtracted":true,"original_C_P_C_K_A_infty_L_star_C_V0_C_R0_read_verbatim":true,"original_WHVA_4096_strict_sufficient_test_false":true,"original_WHVA_no_resolvent_admitted":true,"original_sqrt_two_target_read_not_recomputed":true,"same_selected_member_same_physical_eta0":true,"true_physical96_Theta_nu_and_radial_head_retained":true,"unknown_G_and_Btarget_inverse_not_given_numbers":true},"WPTVS_complete_original_scalar_archive":{"WHV_previous_actual_progress":{"matrix_allocations":0,"new_maxima_completed":3,"new_required_N_diagnostics_completed":1,"new_scalar_records_completed":18,"new_strict_comparisons_completed":1,"old_targets_recomputed":0},"WHV_previous_required_N_diagnostic":{"diagnostic_is_not_a_finite_inverse":true,"exceeds_256_digits":false,"formula":"floor(saved numerator upper)+1","required_N_decimal":"145475","resource_cap_N":4096,"tested_N":4096,"tested_output_dimension":790528,"within_declared_cap":false},"WHV_previous_strict_mesh_gate":{"comparison":"saved epsilon upper < 1","epsilon_record":{"ball":"[35.5162849016096175926993926870198490179833360745262969087788838134567295951 +/- 4.46e-74]"},"passed":false},"WHV_readonly_records":{"A_c":{"ball":"[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]"},"A_c_weight":{"ball":"[0.0187979816503496541345324625056530986003947533773800386267688853972524679326 +/- 2.11e-77]"},"pi":{"ball":"[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]"}},"original_nine":{"A_c_raw":"23/2","C_b":{"ball":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","lower":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]","upper":"[1.53217269674100423344574677508789880873905993470477766300072 +/- 9.68e-61]"},"C_c":{"ball":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","lower":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]","upper":"[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]"},"G_c":"62286/125","L_c_raw":"58/5","R":"25/8","c_body":"1192029371497/5000000000000","rstar_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"shell_1153":{"ball":"1153.00000000000000000000000000000000000000000000000000000000","lower":"1153.00000000000000000000000000000000000000000000000000000000","upper":"1153.00000000000000000000000000000000000000000000000000000000"}}},"WPTVS_mesh_summary":{"all_full_delta_mean_and_low_columns_retained":true,"body_cut":"1192029371497/5000000000000","declared_refinements":[1,2],"homogeneous_raw_transmission_is_identity":true,"original_closed_rows":4650,"original_interfaces":3594,"parent_cap":161,"parent_cells":153,"reference_mean_and_low_1_to_32_zero_only_in_centre":true,"reference_q_binary_places":20,"reference_q_floor":"1/8","refined_cap":322,"refined_counts":[153,306],"right":"25/8","root":["1191984371497/5000000000000","2383968743003/10000000000000"],"rule":"root collar plus eight subcells of each original-rminus doubling band"},"WPTVS_original_scope":{"complete_infinite_BVP_inverse_proved":false,"entire_positive_interval":["the genuine intrinsic root","25/8"],"fixed_body_cut":"1192029371497/5000000000000","full_low_high_Schur_inverse_proved":false,"given_complete_head_positive_high_inverse_and_root_graph_proved":true,"independent_even_mean_and_all_head_and_affine_source_ports_retained":true,"nu_family":"nu_delta=nu0+delta; its compact intrinsic bump is identically zero on this positive interval","ordinary_source_contract":"L2_r H_phi^(-2/3); supplied complete head forcing included","physical_parameter":"same fixed physical eta0","raw_state_contract":"L2_r H_phi^(-1), independent mean is separate","same_genuine_forward_and_backward_Riccati_reference":true},"WPTVS_parameters":{"actual_delta_degree":96,"bits":320,"first_high_index":97,"head_dimension":193,"maximum_doubling_bands":20,"maximum_parent_cells":161,"maximum_refined_cells":322,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"physical_high_minimum":388,"reference_centre_degree":32,"reference_q_binary_places":20,"reference_q_floor":"1/8","uniform_refinements":[1,2]},"WPTVS_retained_scope":{"complete_193_head_components":true,"complete_coupled_head_inverse_proved":false,"finite_matrix_inverse_proved":false,"full_mean_and_affine_jump_ports_retained":true,"new_array_artifacts":false,"old_negative_head_and_metric_obligations_retained":true,"old_targets_recomputed":0,"only_centre_reference_mean_column_has_exact_zero_high_image":true,"ordinary_dr_and_normalized_real_reflection":true,"physical_96_signed_inverse_proved":false,"reference_is_not_a_certified_actual_point_value":true,"same_positive_given_head_realization":true,"selected_member_scope_retained":true,"true_outer_chart_and_all_cross_terms_retained":true},"all_seven_primal_dual_ports_and_true_mean_rows_retained":true,"complete_actual_source_output_last_j":352,"full_degree32_repaired_centre_and_degree96_error_distinction":true,"opaque_family_error_leg_is_a_full_output_norm_not_a_128_coordinate_projection":true,"repaired_centre_source_output_last_j":224}
```


### 6.3. Complete original candidate metadata and repair definition

The original floating candidate is still explicitly labelled `mathematical_certificate=false`; its earlier finite solver status is not promoted to a rigorous inverse. The exact physical amplitude, all original rational $q$ values, metric bump, state ordering, full candidate identity, and independent continuous value-repair definition remain unchanged.


```json
{"amplitude":0.765,"boundary_angle":"original physical theta","coordinates":"moving phi: u=alpha*U; v=1/Cref_nu+alpha*V; theta_phi=v/mean_phi(v); B=u/v; C=1/v","exact_bump":"h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere","exact_cap_cut":"25/8","exact_float_amplitude":"6890507429876859/9007199254740992","exact_float_nu":"-2572625729470897/72057594037927936","exact_float_q_values":["562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312","562949953420957/562949953421312"],"finite_BVP_success":true,"finite_state_angle":"moving phi","kind":"floating_complete_moving_phi_Codazzi_true_regular_endpoint_branch","mathematical_certificate":false,"mean_boundary":"outer","modes":32,"new_metric_family":"E_nu=E exp(nu*h); a fixed","normalized_state_order":"moving phi: U sine modes 1..M; V cosine modes 0..M, frequency 4m","nu":-0.03570235398252099,"object_sha256":"91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848","old_waist_branch_reused":false,"original_target_fixed":false,"outer_boundary":"r=25/8 actual regular linear physical graph proposals; native proposal and true nonlinear mean/nonmean fees retained as posterior obligations","physical_frequency_factor":4,"q_vector_path":"notes/2026-11-13-R133-regular-r25over8-q256-floating.json","q_vector_sha256":"8f2471f709d5350212c3bb12a2e180fef37cbd8ced72e7ed858d6687b5fa36d9","solver_message":"The algorithm converged to the desired accuracy.","solver_status":0,"source_sha256":"3c170b9c9d2b34655107dba54b189c6a940d9f62901a61d0a3ccc5a5b398e996","waist_nonmean_complement_allowed_to_change":true}
```


```json
{"base_candidate_sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","centre_is_not_the_original_ac1_index":true,"exact_alpha":"6890507429876859/9007199254740992","exact_radial_interval":["0","25/8"],"first_piece":0,"kind":"actual_final_exact_continuous_value_repair_v1","last_piece":6143,"modes":32,"object_sha256":"91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848","offset_sequence_sha256":"c66b5d52c3cd6b07e96853e1065345360a88b7f2f967b6f1606c880b68e33875","offsets_independent_of_eta_and_nu":true,"physical_frequency_factor":4,"physical_offset_rule":"e_0=0; e_j=e_(j-1)-alpha*(y_j(r_j)-y_(j-1)(r_j))","radial_nodes_count":6145,"reference_nu":"-2572625729470897/72057594037927936","repaired_state":"u_bar=alpha*U+e_u,j; v_bar=s_eta,nu+alpha*V+e_v,j"}
```


### 6.4. Five old whole maxima and the two original failed refinements

These complete saved maxima, their witnesses, and the original $m=1,2$ false results are literal predecessors. Neither the first WPS run, the WVC run, nor this WCTR run reevaluates them.


```json
{"A":{"ball":"[6.74940356901263092670863707542064558979483470421701096544083933324204151513 +/- 5.00e-75]","witness":{"intersection":["4141104371497/5000000000000","466622961391443/562949953421312"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5432,"original_row":3220,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}},"B":{"ball":"[0.466864898755215147682802847367675189210571079614179169864984866403609283249 +/- 1.70e-76]","witness":{"intersection":["4141104371497/5000000000000","466622961391443/562949953421312"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5432,"original_row":3220,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}},"E_b":{"ball":"[0.108706949199471213512287647811232809190669789250317142372161453775952555797 +/- 3.27e-76]","witness":{"intersection":["5154119573546235/9007199254740992","2578310786669609/4503599627370496"],"kind":"body","left":"2850864371497/5000000000000","length_upper":"576/15625","original_piece":5041,"original_row":2699,"parent_index":122,"reference_sha256":"0bd26a6f05d03c0d97d9b707d68bf0a6b1926f608639aa130f5b0ae68f40887f","right":"3035184371497/5000000000000"}},"L":{"ball":"[163.600937025345482766219943539843512909164969214908905939645812915486345571 +/- 2.71e-73]","witness":{"intersection":["1362338887279575/2251799813685248","5451857548911283/9007199254740992"],"kind":"body","left":"2850864371497/5000000000000","length_upper":"576/15625","original_piece":5108,"original_row":2783,"parent_index":122,"reference_sha256":"0bd26a6f05d03c0d97d9b707d68bf0a6b1926f608639aa130f5b0ae68f40887f","right":"3035184371497/5000000000000"}},"U_b":{"ball":"[33.5876945136675216786627931089641014780483817436844898550706041227597166279 +/- 1.38e-74]","witness":{"intersection":["4057589653914093/4503599627370496","4061371163960643/4503599627370496"],"kind":"body","left":"4141104371497/5000000000000","length_upper":"1152/15625","original_piece":5485,"original_row":3308,"parent_index":129,"reference_sha256":"5482c3d096989a952a73b76f51c437579df2d187764e4800fc712e2e629877a1","right":"4509744371497/5000000000000"}}}
```


```json
{"1":{"all_parent_S_D_B0_enclosures_inherited":true,"complete":true,"complete_delta_upper":{"ball":"[8453.72188139484926524116189148185715903781192999939456445363298262701028690 +/- 6.06e-73]"},"complete_feedback_upper":{"ball":"[8446.97247782583663431445325440643651344801709529517755348819214329376824538 +/- 4.26e-72]"},"complete_source_quadrature_upper":{"ball":"[51.6287117085309040517051721172442998728694537049355378143293015940257513125 +/- 4.71e-74]"},"parent_cells":153,"refined_cells":153,"refinement":1,"strict_tail_gate":false},"2":{"all_parent_S_D_B0_enclosures_inherited":true,"complete":true,"complete_delta_upper":{"ball":"[2121.93073588211317496373125153515926794598676959110090636815634847631651888 +/- 4.63e-73]"},"complete_feedback_upper":{"ball":"[2118.55603409760685950037693299744894515108935223899240088543592880969549812 +/- 1.97e-72]"},"complete_source_quadrature_upper":{"ball":"[25.8976428422867031078313173455747457418391223325533590094423404674884275229 +/- 1.74e-74]"},"parent_cells":153,"refined_cells":306,"refinement":2,"strict_tail_gate":false}}
```


### 6.5. Full old WVC provenance remains independently bound

The 14,022-byte `prior_completed_candidate` archive binds the complete original WVC scientific, execution, and manifest files. It preserves all 56 original records, all five original modal-prefix records, all original completion and scope fields, the complete prior WPS archive identity, and the twenty copied whole objects. The complete old six-graph object is 8,637 bytes, SHA256 `0882b563cdd2e425d5d1e383bd158ce5bce7fb1604903df2bb1a0756b5f4ea42`; the prior WPS archive inside the old WVC file is 8,977 bytes, SHA256 `2e70e03efe8d2275f5365fff52b5a964c912594edd6a156145affafe7146799e`.

For this actual note, all 43 old WVC scientific fields and all 44 old execution fields were independently serialized as whole objects. The sorted field-identity tables reproduce the exact frozen hashes:


| Full old field table | Fields | Table bytes | SHA256 |
| --- | --- | --- | --- |
| WVC scientific | 43 | 4761 | `8d5018d148942b2448aef054683c037c0d640475cf68afe1282056cd837f8038` |
| WVC execution | 44 | 4867 | `fdd50b872d3288ac9f3006d93035322312e8739d402a77b51fbd550c55d98296` |


The original WVC retained scope is copied below in full, separately from the new WCTR scope in §2. In particular its $6/5$ qualification remains original provenance and has not been rewritten to $5/4$.


```json
{"actual_S_P_Q_A_B_C_R_and_high_space_unchanged":true,"actual_head_dimension":193,"actual_tail_inverse_bound_from_published_analytic_m160":3,"all_completed_old_bounds_maxima_and_m1_m2_false_gates_read_only":true,"all_four_finite_Schur_blocks_and_both_rhs_retained":true,"all_independent_mean_affine_head_cokernel_and_external_rows_retained":true,"all_original_4650_rows_3594_interfaces_and_4801_intersections_admitted":true,"all_original_two_order_native_rows_read_only":true,"all_reference_modes_unchanged_implies_seven_verbatim_graph_copies":true,"all_seven_primal_dual_ports_retained":true,"complete_actual_family_degree":96,"exact_reference_definition_materialization_only":true,"finite_false_sufficient_gate_does_not_prove_singularity":true,"finite_gate_is_complete_E0_plus_3_D_T_upper_less_than_one":true,"full_family_error_is_whole_output_norm_not_Q224_projection":true,"full_family_residual_last_j":352,"mode_reference_unchanged_implies_original_complete_modal_bound_read_only":true,"new_head_lift_analytic_upper":"6/5","new_reference_diagonal_uses_exact_complete_local_and_primitive_entries":true,"new_reference_q_rho_and_odd_endpoint_bounds_never_inherited_for_changed_modes":true,"no_automatic_scientific_retry":true,"no_dense_finite_matrix_or_new_array_artifact":true,"no_derivative_of_continuous_centre_BHL_needed":true,"only_actual_full96_correction_in_family_error_legs":true,"ordinary_radial_L2_measure":true,"original_WPS60_success_false_gate_and_six_modal_prefixes_retained":true,"other_physical_readouts_require_their_full_actual_conversion":true,"outer_chart_dimension":96,"physical_96_root_even_normalization_is_boundary_identity_if_inverse_proved":true,"physical_density_means_Theta_nu_and_actual_96_columns_not_deleted":true,"physical_frequency":4,"physical_mean_reference_zero_actual_mean_fully_retained":true,"prescribed_root_even_dimension":96,"raw_identity_transmissions_and_independent_affine_jumps_retained":true,"reference_only_degree":32,"repaired_centre_is_operator_replacement_not_a_new_physical_background":true,"repaired_centre_residual_last_j":224,"root_complement_dimension":97,"same_complete_repaired_degree32_centre_inside_Green_source":true,"same_selected_positive_genuine_family":true,"whole_actual_radial_head_not_finitely_truncated":true}
```


## 7. Complete admission, 45 current inputs, 19 historical inputs, and 16 AST checks

The complete scientific admission object is:


```json
{"candidate_nodes":6145,"candidate_shape":[4,6144,65],"checks":[{"name":"all_current_UTF8_files_and_three_fixed_contracts_verified","passed":true},{"name":"five_new_and_ten_original_definition_sources_AST_only_verified","passed":true},{"name":"all_nineteen_historical_receipts_and_original_native_bytes_verified","passed":true},{"name":"complete_original_summary_and_native_projection_identical","passed":true},{"name":"both_complete_4650_row_covers_and_3594_interfaces_verified","passed":true},{"name":"same_real_family_and_all_original_successes_verified","passed":true},{"name":"all_nine_original_literals_and_completed_WHVA_retained","passed":true},{"name":"all_five_original_cubic_parts_and_full_shape_verified","passed":true},{"name":"original_repair_whole_document_and_all_65_suprema_verified","passed":true},{"name":"actual_raw_identity_transmissions_and_full_affine_ports_retained","passed":true},{"name":"all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","passed":true},{"name":"all_fifty_six_old_WVC_records_full_false_scope_and_five_prefix_records_verified","passed":true}],"current_file_count":45,"historical_input_count":19,"inflated_rows":4650,"interfaces":3594,"native_bytes":25507783,"native_sha256":"1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c","new_source_AST_count":5,"old_gate_counts":[19,11,18,14,6],"old_source_AST_count":10,"old_source_import_count":0,"old_targets_recomputed":0,"original_parts_manifest_row_counter":0,"original_progress_counter":4608,"per_order_complete_rows":[4650,4650],"prior_completed_candidate_records":60,"prior_completed_modal_prefix_records":6,"prior_completed_tracefree_candidate_records":56,"prior_completed_tracefree_modal_prefix_records":5,"repair_suprema_count":65,"repairs_regenerated":0,"restoration_receipts_bytes":13771,"restoration_receipts_sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"}
```


The original body native has two complete 4,650-row orders and 3,594 original interfaces. The original scientific progress counter 4,608 and the original parts-manifest row counter zero remain separate recorded facts. The candidate contains 6,145 radial nodes with complete shape `[4,6144,65]`; all five original cubic parts and all 65 original repair suprema were admitted. No candidate, repair, old graph, or old row producer was regenerated.

The 24 ordered structural gates, all true, are:


| Index | Exact gate name | Passed |
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
| 12 | `all_fifty_six_old_WVC_records_full_false_scope_and_five_prefix_records_verified` | true |
| 13 | `fixed_directed_runtime_and_one_new_entry` | true |
| 14 | `all_forty_four_old_records_typed_and_published_tail_bound_retained` | true |
| 15 | `entire_frozen_reference_definition_chain_materialized_without_old_bounds` | true |
| 16 | `complete_continuous_parent_and_comparison_domains_admitted` | true |
| 17 | `complete_reference_receivers_saved` | true |
| 18 | `complete_high_trial_source_saved` | true |
| 19 | `complete_actual_paired_receivers_saved` | true |
| 20 | `complete_local_signed_remainder_saved` | true |
| 21 | `complete_endpoint_correction_saved` | true |
| 22 | `complete_actual_E_D_T_saved` | true |
| 23 | `all_current_inputs_and_manifest_reverified_after_new_work` | true |
| 24 | `complete_whole_candidate_shape_and_old_zero_recomputation` | true |


### 7.1. All current UTF8 receipts

All 45 full receipts agree exactly between the manifest, scientific file, and execution file. Their role/SHA map also agrees with the scientific `input_sha256` object. The mathematical binding is the five complete records in §1, rather than an inferred import list.


| Role | Exact relative path | Bytes | Git blob | SHA256 |
| --- | --- | --- | --- | --- |
| `negative_one_summary` | `notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/full-real-delta-negative-one-positive-graph-summary.json` | 41797 | `3abd0f6b7291e0f9318dc035a58a4b6e8dfb851c` | `0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef` |
| `negative_one_process` | `notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/process.json` | 16380 | `4dc9280cb3761b36af71f795fbafcb8749af4663` | `f4ac37531a76893b62050d3291f5227f343ad9f48e3365783bff1a52c451a3f1` |
| `negative_one_source` | `scripts/fourfold_codazzi_full_delta_negative_one_positive.py` | 22029 | `327f24e3c4a2864d8ba401f0d574f112a4a90d26` | `16ffa1a5b3753bc2a70fcf979814b18161df90ae8997510acc8feafac2a88509` |
| `collar_process` | `notes/full_delta96_root_collar_ci/run-43606747196-1/consumers/process.json` | 11340 | `d10f4681c84ab579b8121b16e6246604a608a715` | `f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae` |
| `collar_source` | `scripts/fourfold_codazzi_full_delta96_root_collar_budget.py` | 15041 | `602a8a3df10c4319446909a56d532ba88b0a6367` | `8d3ab188d47a1aa81cbc304350655f2172333b435fdf0e09482b245f957917bf` |
| `body_process` | `notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/process.json` | 11040 | `eb294ed3b3a1cef61a3a6a1ecf7e469a7842167c` | `1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395` |
| `body_summary` | `notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-positive-N97-high-inverse-summary.json` | 21555 | `ffea3e8fa1690c3c9492857728057d9d6e17bf64` | `2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9` |
| `body_source` | `scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py` | 19660 | `f4dd9ad8b324e39fed478183b88095c949d5c09a` | `0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117` |
| `body_parts_manifest` | `notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts.json` | 6002 | `aabe1eb46cb52e41c8191960a2a998b437ca47e7` | `7b1967565a0ff0a4d9855734a3f0a0621c8049160099e066d8f34ecb35cdd3a3` |
| `WHV_actual` | `notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json` | 12011 | `ebe7ae42c2482ce9b20e7af1d41e02f89b920010` | `ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72` |
| `WHV_readonly_inventory` | `notes/2026-11-16-R133-zero-Volterra-positive-head-readonly-input-inventory.json` | 23789 | `18428ac8d144863cf831a10eb8af17e51d3c2ddc` | `80f9f606f14f8cea41f3a4f18a5d6b9c7d59274ea8016199b1cc086cf58b59ce` |
| `WPT_contract` | `results/R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md` | 22954 | `b37c59bc05a2131b27014f37c1a6555d6f7e2c58` | `22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e` |
| `candidate_index` | `data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json` | 6750 | `2257c4327fcafcad3ed50f0362fb089e9cfd56d2` | `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` |
| `complete_coefficient_definition` | `scripts/fourfold_codazzi_current_positive_complete_coefficients.py` | 21756 | `45ce0d7171ad35aa3175ea03fdac22f5158fa855` | `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c` |
| `continuous_repair_definition` | `scripts/fourfold_codazzi_final_continuous_value_repair.py` | 9076 | `67d7de2adf36c916123f7c9cf7a5db09af3c7b58` | `51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b` |
| `repaired_value_inflation_definition` | `scripts/fourfold_codazzi_repaired_positive_high_Volterra.py` | 21932 | `538ca4f6c9f25f669daf2ce1a175fd0bfbacb40a` | `8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d` |
| `lossless_shard_format` | `scripts/fourfold_codazzi_candidate_shards.py` | 4187 | `81a21dba0077137601382781b6b3298bdd7d5ade` | `5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e` |
| `inventory` | `notes/2026-11-16-R133-frozen-cross-block-readonly-input-inventory.json` | 38086 | `18ec6014b06315aaf24cf9068e6fa31e05e6025a` | `f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547` |
| `proof_WPTV` | `results/R133-supplement-frozen-cross-block-value-enclosures-for-the-positive-head.md` | 21178 | `ddccd14e855ba95048fe92cbd21edfb82ebd8e6f` | `dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9` |
| `proof_WPTVR` | `results/R133-supplement-five-whole-maxima-and-inherited-positive-head-refinements.md` | 11659 | `49cb657d9aefd809857aeac0229124738978a05d` | `62adc53eedc1ea339e02f6e2a8fa654e38c92fe04784343557e23c84ddd696c2` |
| `WPTVS_actual` | `notes/frozen_cross_block_remaining_body_ci/run-43859287399-1/actual-scientific-conclusion.json` | 24767 | `c79f9de99b0f6e398c97f840e82a7e653b5e6626` | `bdd8857cf98d3497600b349b05fc81b8aab7441cd7020b6a5f337b6067f774ef` |
| `WOBSA_actual` | `notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json` | 60416 | `b21c6d0717bccd6827eff4792bb12b8b1cd40d05` | `ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79` |
| `proof_WIC` | `results/R133-supplement-analytic-inherited-tail-and-weighted-impedance-circuit.md` | 29026 | `019b1136ebe81e44e98399dff5fb895aafb4362e` | `527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f` |
| `proof_WPS` | `results/R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md` | 43851 | `e830f7df4643fe77b941478dbde06ebf9378ebef` | `ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72` |
| `proof_WQS` | `results/R133-supplement-bidirectional-impedance-generators-and-complete-high-trial.md` | 25336 | `ff2d61db92e89cc9397c6131675bbcd6294a025c` | `bea9137248b445405c7ae483fdc56c4875cc515820632b1d34fdee8b6bfc6fee` |
| `proof_WOB` | `results/R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md` | 41683 | `8a55c94d8decc25f33876665119b327eb1d1fd29` | `f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979` |
| `WIC_module` | `scripts/fourfold_codazzi_weighted_impedance_circuit_math.py` | 11013 | `b181bb80373c870769e2c35b28e764ab7be76e44` | `c5de896f603424c0fed3892287031d38d775843e55580f52f4759fe1daba4de3` |
| `WQS_module` | `scripts/fourfold_codazzi_bidirectional_impedance_generators_math.py` | 10070 | `d39ae08753f04a5b59c90231d605f8443b8cb9eb` | `878c4aec5ed14f4d5e5f3d24ecd23476373a5e26c7b1dd4119b2198e9b73bb02` |
| `completed_reference_definition` | `scripts/fourfold_codazzi_frozen_cross_block_value_tail.py` | 31266 | `ff79fe62e6a948b2536d2594e995047eb65fd820` | `159d8fdc153cadf844e1d28f2e0271ae12e55c38d560d7330ee28f164bf21d3c` |
| `science` | `scripts/fourfold_codazzi_clipped_scalar_trace_candidate.py` | 73502 | `ca466fff42f3489c38a68e80dda402e5c4e213f9` | `569fe7a44cc282e7e6e1c7ff5133a9a07115aac22755e14ac8d26b7d04833e0b` |
| `readonly_admission` | `scripts/fourfold_codazzi_clipped_scalar_trace_readonly.py` | 99368 | `fa1e50e3c5950236db14ae72a7f6920435a8f5a0` | `b161d5183894c5661ab3526b5399307810cc6995d88dfe21100a2f16b54eb8b2` |
| `kernel_math` | `scripts/fourfold_codazzi_two_rate_centre_kernel_math.py` | 39350 | `b718d4280a366487527bccd89702eac7d352ad38` | `7e995802fa167fba0a7601cd4af5ce6044eb0b4693dc57576673356abaa00ccd` |
| `assembly_math` | `scripts/fourfold_codazzi_scalar_trace_candidate_math.py` | 18821 | `93af9e0b4689016bf5c51449324b59f6452aa1d9` | `21c0b97e1ed766c354ee77af613a2f4d17c40762902ff7c52fd82142bf18e270` |
| `reference_math` | `scripts/fourfold_codazzi_clipped_scalar_trace_reference_math.py` | 24348 | `8e92982d16180da16330ae3aac36a2bcd5c42141` | `1732fb0f119ebff661da3892f63bb140de05e0c845e780a06ca115998f199c7a` |
| `worker` | `scripts/fourfold_codazzi_complete_paired_public_worker.py` | 31551 | `85d72a0600816b2176093dd74ab61595fad40520` | `afbbae87226ee6c1ddb95944a8f21c00b6e7218a166f046ea2fc24b2ce86e437` |
| `rules` | `notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json` | 2461 | `5c5d020913d717bb5bc8ce891297e00eaa8944f7` | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |
| `WPS_actual` | `notes/complete_paired_finite_residual_ci/run-43878765372-1/actual-scientific-conclusion.json` | 65347 | `17a70a8a6304f387d271378f31964e075ddb9594` | `0c2467867a6eade717a1df17936729f5e6978ee49fc2cf611e183424a51e2123` |
| `WPS_execution` | `notes/complete_paired_finite_residual_ci/run-43878765372-1/execution.json` | 35857 | `21bf7ec0d72950132e3b0c09f940069588640302` | `01d18a4461d4aef6bff42484f195a95a5889a9e4d9ebbe2da4428a5898255c71` |
| `WPS_manifest` | `notes/2026-11-16-R133-complete-paired-finite-residual-current-inputs.json` | 48445 | `ed9aede898fcb79523a188ecee54a00763593019` | `aabc28e194b27377d26f24ec7fff03708c0ff903841881233429ab0e36b76981` |
| `proof_WPSA` | `results/R133-supplement-actual-complete-paired-finite-residual-and-false-gate.md` | 50464 | `6bcd4484f596e39f94cb6adc870dec3b937ad984` | `470d2547de70dea45468103bc3518e6ed5bcc757c348543896df4edda65a2f92` |
| `proof_WVC` | `results/R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md` | 29128 | `e377cb2e0578fc66ba8a7bc32e339fadcb0a242c` | `fade78e696506af0ef2c1e304e824ff7415c63df53b31f0ed299d8ff548845a8` |
| `WVC_actual` | `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json` | 78627 | `746ec1e16befe8914c64521ad087c1f1dd23ab73` | `85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88` |
| `WVC_execution` | `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/execution.json` | 37911 | `c8cd8e8bb863c500a1e26c009e0af76cd7cb8941` | `5e560887d2deee497cb9da5b7549af1070db36cf69a7b11077ef4a0bb4f0feb5` |
| `WVC_manifest` | `notes/2026-11-16-R133-continuous-centre-tracefree-current-inputs.json` | 60844 | `1ea008a1df3116aedd66be67b11b1d8ec62af2d5` | `229198f56efdf10ea8de6fef50804aa3832ca5ff2127101685c8d7117c9afbfb` |
| `proof_WCTR` | `results/R133-supplement-clipped-scalar-trace-matrix-normalizers-and-paired-circuits.md` | 26966 | `21491641c33a4261d6364c2107d80882d11d0e49` | `efe08e59290ffb483dc97f59443eb4a7100390e7d655a846b954e409d5084295` |


### 7.2. All sixteen operational AST receipts

The admission records five new sources and ten original definition sources. The worker's independent AST adds the sixteenth receipt. Each role, path, and SHA256 below matches its complete current receipt above. AST parsing of an original definition source is not importing or executing that producer.


| AST role | Exact relative path | SHA256 |
| --- | --- | --- |
| `negative_one_source` | `scripts/fourfold_codazzi_full_delta_negative_one_positive.py` | `16ffa1a5b3753bc2a70fcf979814b18161df90ae8997510acc8feafac2a88509` |
| `collar_source` | `scripts/fourfold_codazzi_full_delta96_root_collar_budget.py` | `8d3ab188d47a1aa81cbc304350655f2172333b435fdf0e09482b245f957917bf` |
| `body_source` | `scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py` | `0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117` |
| `complete_coefficient_definition` | `scripts/fourfold_codazzi_current_positive_complete_coefficients.py` | `1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c` |
| `continuous_repair_definition` | `scripts/fourfold_codazzi_final_continuous_value_repair.py` | `51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b` |
| `repaired_value_inflation_definition` | `scripts/fourfold_codazzi_repaired_positive_high_Volterra.py` | `8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d` |
| `lossless_shard_format` | `scripts/fourfold_codazzi_candidate_shards.py` | `5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e` |
| `WIC_module` | `scripts/fourfold_codazzi_weighted_impedance_circuit_math.py` | `c5de896f603424c0fed3892287031d38d775843e55580f52f4759fe1daba4de3` |
| `WQS_module` | `scripts/fourfold_codazzi_bidirectional_impedance_generators_math.py` | `878c4aec5ed14f4d5e5f3d24ecd23476373a5e26c7b1dd4119b2198e9b73bb02` |
| `completed_reference_definition` | `scripts/fourfold_codazzi_frozen_cross_block_value_tail.py` | `159d8fdc153cadf844e1d28f2e0271ae12e55c38d560d7330ee28f164bf21d3c` |
| `science` | `scripts/fourfold_codazzi_clipped_scalar_trace_candidate.py` | `569fe7a44cc282e7e6e1c7ff5133a9a07115aac22755e14ac8d26b7d04833e0b` |
| `readonly_admission` | `scripts/fourfold_codazzi_clipped_scalar_trace_readonly.py` | `b161d5183894c5661ab3526b5399307810cc6995d88dfe21100a2f16b54eb8b2` |
| `kernel_math` | `scripts/fourfold_codazzi_two_rate_centre_kernel_math.py` | `7e995802fa167fba0a7601cd4af5ce6044eb0b4693dc57576673356abaa00ccd` |
| `assembly_math` | `scripts/fourfold_codazzi_scalar_trace_candidate_math.py` | `21c0b97e1ed766c354ee77af613a2f4d17c40762902ff7c52fd82142bf18e270` |
| `reference_math` | `scripts/fourfold_codazzi_clipped_scalar_trace_reference_math.py` | `1732fb0f119ebff661da3892f63bb140de05e0c845e780a06ca115998f199c7a` |
| `worker` | `scripts/fourfold_codazzi_complete_paired_public_worker.py` | `afbbae87226ee6c1ddb95944a8f21c00b6e7218a166f046ea2fc24b2ce86e437` |


### 7.3. Complete historical-restoration wrapper

The wrapper has **eleven keys**; its `historical_inputs` array has **nineteen entries**: thirteen original native chunks, five original candidate parts, and one original repair. These are different counts. The thirteen native chunks retain their offsets, inflated chunk sizes and hashes, and `chunk_sha256_verified`; the five parts and repair retain `identical_original_bytes_materialized`. All nineteen retain their original immutable commit/path/Git/byte/SHA identities and both compressed-byte and Git-tree checks.

The full wrapper, identical in the scientific and execution files and identical to its old WVC whole object, is reproduced here. Its compact canonical identity is 13,771 bytes, SHA256 `4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac`. It records actual Actions restoration; no binary body was fetched to prepare this note.


```json
{"candidate_index":{"bytes":6750,"git_blob_sha":"2257c4327fcafcad3ed50f0362fb089e9cfd56d2","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json","role":"candidate_index","sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"},"candidate_part_roles":["original_candidate_part_000","original_candidate_part_001","original_candidate_part_002","original_candidate_part_003","original_candidate_part_004"],"centre_repair_role":"original_continuous_centre_repair","historical_inputs":[{"bytes":1950382,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"29713df4531c214b0beb8a5dd2c0d4d979fe0cf5","git_tree_blob_and_size_verified":true,"index":0,"offset":0,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part000.bin.gz","role":"original_positive_native_part_000","sha256":"29ffdceeff0c76ab958e84fd74506bafb07a60e2f178ddb880f50dbe25189b1c","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"7fed6abf740c51d6cad803d734a12dfa1ffad16e8e1b8d0ee1ec7c644f21644e"},{"bytes":1942995,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"4101dbabd5e12148f0ace33a94ab196cc0f54a84","git_tree_blob_and_size_verified":true,"index":1,"offset":2000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part001.bin.gz","role":"original_positive_native_part_001","sha256":"04a4b04ccbe536783dddd37dd833fdf5623dab720b64a15432f3761d5b4b92dc","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"a7c6f631ffe919646be272ae4b47368f0ad03a2690ecf1887b5969f452dd820a"},{"bytes":1957508,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"f36fd4d2e7f726f1ec85de274d42eba951bb80f5","git_tree_blob_and_size_verified":true,"index":2,"offset":4000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part002.bin.gz","role":"original_positive_native_part_002","sha256":"45a7970b370f0db0c3f1e6bd398a3dda61e5b31a594843b30550ac1e7e4be41d","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"8682a419fcc1ce8e60a80b5ef4e1459d6703f14d4126f9f326522f11d021588e"},{"bytes":1947192,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"af0c21edcb2c1b8afd12d8912776761af98d6c97","git_tree_blob_and_size_verified":true,"index":3,"offset":6000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part003.bin.gz","role":"original_positive_native_part_003","sha256":"65f2753cd0a59d903f29520c3cad919d0b07658e90efab1bb27a1fbdb6fdc258","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"30125ee16d054b94801f16390b146c55ab11bff5c1d0399411775d346da3807f"},{"bytes":1958541,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"7ff35ffda99968c18a88ece1ac508c02d1bde8f7","git_tree_blob_and_size_verified":true,"index":4,"offset":8000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part004.bin.gz","role":"original_positive_native_part_004","sha256":"289daa745077005479ee1d5e2a025de70f7f9f6603ea55da085b5a03991d770e","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"ad6a1f7ee7246a05ebf12e6f0f4a9de32718596384d4de3e2d59257ce0d8e8c9"},{"bytes":1965294,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"9438fbad8a7341b04ba83a2fce83af92ebab2811","git_tree_blob_and_size_verified":true,"index":5,"offset":10000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part005.bin.gz","role":"original_positive_native_part_005","sha256":"737f041a4d3e85506ba180d188ec940958b6f0397694f4265b373c69f8e6b9bc","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"3f8557a19e436d568f8a865d6e50c81e8a503da6b506c5ef224d8495dd1b595e"},{"bytes":1973101,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"d1849d9d7036f4c7eb8208b74d0c11d263f6f4f4","git_tree_blob_and_size_verified":true,"index":6,"offset":12000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part006.bin.gz","role":"original_positive_native_part_006","sha256":"dc746368d68fa83b0a73d2a201f1657951eea22badda2ed834629df09c6cf3e6","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"08369d01142932fa08d03481d615b7fae3a0afc5747da94d73d6b1b9e2e66d3f"},{"bytes":1966242,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"2b2d0bd7348056ad39ba38f38461bcefba9b4f67","git_tree_blob_and_size_verified":true,"index":7,"offset":14000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part007.bin.gz","role":"original_positive_native_part_007","sha256":"68d3d37ed07b5da7c2152a1ba1276cc8b478e2f63186985229e02145b077ca66","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"902852b0176e85cead1ba5cbd25b9545b175cd0ca6f4e32292d8c2c997a9f7c1"},{"bytes":1904549,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"581826fdfd500573948c5a880e4862f7824d3059","git_tree_blob_and_size_verified":true,"index":8,"offset":16000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part008.bin.gz","role":"original_positive_native_part_008","sha256":"49e156dac95cb7d83c9b550e127fe6c9f5908132fae6cc366144ab6c08898006","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"e6a4a6fee10f6151711deccc7b5f2c8b50459aefc64572f5f143ee1f9520db3e"},{"bytes":1916409,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"ff6671fd2058a5dd986999f3371e3ab9be775246","git_tree_blob_and_size_verified":true,"index":9,"offset":18000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part009.bin.gz","role":"original_positive_native_part_009","sha256":"167ef3b72d2ffde736aa8f80d7291595a85e55195cac71cad3369b89d32762ea","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"0305608356742ef6e0719d35c57f4090d3e9f919dfc9aac6093f7d412719af7f"},{"bytes":1905000,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"54384fa7d28f5cabfbfcb6713f68be6c8bbf0f37","git_tree_blob_and_size_verified":true,"index":10,"offset":20000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part010.bin.gz","role":"original_positive_native_part_010","sha256":"3f01244217179906a6d72ad79b5bfb47a2590fd08089d44c05cbd920307a67f7","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"03a6099aa1c94ef48c5afe3fa9bf5f2a31a391c20b9a536700c5255e4e66e552"},{"bytes":1917716,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"b6b9beb2d1dc04414d876d3d8f54fe4c0d2b5dd4","git_tree_blob_and_size_verified":true,"index":11,"offset":22000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part011.bin.gz","role":"original_positive_native_part_011","sha256":"6ab32449559227533336ac0bbeb542db81ff77e2825b484d5f71da2d06094f2a","uncompressed_chunk_bytes":2000000,"uncompressed_chunk_sha256":"0d173d9c85d91c8fe9f17e47d156eb2586b9df04d3ff2461e0c051da7c861829"},{"bytes":1447672,"chunk_sha256_verified":true,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"git_blob_sha":"f729e93ca369c775c3b558672361e9e04c1f7807","git_tree_blob_and_size_verified":true,"index":12,"offset":24000000,"path":"topics/visible-flex-exact-nearby/notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/native-full-delta-complete-positive-N97-high-inverse.json.gz-1f3e5fa630f39a66-parts-part012.bin.gz","role":"original_positive_native_part_012","sha256":"4a8f09d4ea4ff3c62352a059f69f37017089b00da8cc853dd8b13c227a679819","uncompressed_chunk_bytes":1507783,"uncompressed_chunk_sha256":"0a12b0cccc436d3a6bd8fbbc48c13037788fb9a4bda359e417a1ae73e688faed"},{"bytes":2738500,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","compressed_sha256_verified":true,"first_interval":0,"git_blob_sha":"634c08e6d18ed7d16308881b378cc5a9420be3a4","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"last_interval_exclusive":1346,"path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part000.npz.gz","role":"original_candidate_part_000","sha256":"5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4"},{"bytes":2738003,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","compressed_sha256_verified":true,"first_interval":1346,"git_blob_sha":"ed630e376a1e91b19e34ac8be8080161a15f6200","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"last_interval_exclusive":2692,"path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part001.npz.gz","role":"original_candidate_part_001","sha256":"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"},{"bytes":2738686,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","compressed_sha256_verified":true,"first_interval":2692,"git_blob_sha":"5cc4d26fb15282ec922057eead9d6728e2a2b0cc","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"last_interval_exclusive":4038,"path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part002.npz.gz","role":"original_candidate_part_002","sha256":"a317c6f491295d8e46aa5d4b3da84c1f26bd16d5fb65260f3d3459e1f9c6210e"},{"bytes":2732843,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","compressed_sha256_verified":true,"first_interval":4038,"git_blob_sha":"7a4ce33c8adf353574c34085e2cd8713245f59d3","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"last_interval_exclusive":5384,"path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part003.npz.gz","role":"original_candidate_part_003","sha256":"7b67e5a4b11ae45476d1507e842ae23919ca44e4ed2d64bc81bdea78e0b4007c"},{"bytes":1532492,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","compressed_sha256_verified":true,"first_interval":5384,"git_blob_sha":"7c9414280441e5831fa4507fab8707043511c57a","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"last_interval_exclusive":6144,"path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part004.npz.gz","role":"original_candidate_part_004","sha256":"314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c"},{"bytes":14226,"commit":"12b06502f2e4d522ca5dc16d6064267859b3a0a1","compressed_sha256_verified":true,"decode":"check original compressed bytes, SHA256 and Git blob; gzip decode once as JSON only in authorized own Actions","git_blob_sha":"f5dc1d8e7f40cc6a97ca80de26455b12000c163a","git_tree_blob_and_size_verified":true,"identical_original_bytes_materialized":true,"path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz","role":"original_continuous_centre_repair","sha256":"6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc"}],"kind":"complete_readonly_native_cubic_repair_restoration_v1","native":{"bytes":25507783,"complete_concatenation_verified":true,"sha256":"1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c"},"new_arrays_published":0,"new_artifacts":0,"old_producers_executed":0,"original_repairs_regenerated":0,"scope":"Exact original data bytes only; scientific admission and new targets are separate."}
```


## 8. Actual runtime, public-consumption boundary, four pulls, and output limits

The exact runtime object is:


```json
{"Python":"3.12.14","bits":320,"numpy_imported":false,"old_module_imports":0,"python_flint":"0.9.0"}
```


| Actual field | Recorded value |
| --- | --- |
| Worker started | `2026-11-16T15:56:07.352490+00:00` |
| Scientific child started | `2026-11-16T15:56:38.128498+00:00` |
| Scientific child finished | `2026-11-16T16:04:16.950074+00:00` |
| Execution finished | `2026-11-16T16:04:16.999480+00:00` |
| Scientific mathematical wall seconds | `452.10128620600005` |
| Child wall seconds | `458.82150712000004` |
| Scientific children | `1` |
| Scientific child return code | `0` |
| Child timeout | `false` |
| Publication attempts | `1` |


The preflight was a pure data/AST admission: `flint_imported=false`, `old_scientific_calls=0`, return code zero, empty stderr. Its complete stdout was 3,286 bytes, SHA256 `927b4d445b96347ad3928b049b351389b05256a4cbfceabb51236593972872c6`. Independently serializing the full `complete_output` object from the execution file reproduces those bytes and hash. Its admission object is exactly the object in §7, and it binds both complete old WPS and WVC files.

The consumed marker was published before the new scientific child. Its complete contents are:


```json
{"event_commit":"ef5a809c4bf3020b9e6473b98d1864eb71fe0ba8","kind":"consumed_new_scientific_target_v1","manifest_sha256":"acf4f84aca6a15f7e50640665448cf1b864ec9cd7918772ff9c38eb426406c02","old_completed_targets_may_be_recomputed":false,"only_explicit_remaining_target_contract_can_continue_after_failure":true,"output_directory":"topics/visible-flex-exact-nearby/notes/clipped_scalar_trace_residual_ci/run-43901776543-1","prepared_utc":"2026-11-16T15:56:33.061819+00:00","problem_id":"WCTR_complete_clipped_scalar_trace_candidate_v1","run_attempt":"1","run_id":"43901776543","status":"readonly_preflight_passed_new_child_reserved"}
```


Four actual Git pulls were recorded. In this run **all four full receipts are retained**; the optional first-plus-latest-three truncation rule was never entered. Each actual README diff and each diff from the explicit reviewed rules is empty. The hash chain is independently reconstructed in order from the full receipts, starting with `previous=null`:

$$

h_k=\operatorname{SHA256}\bigl(\operatorname{canonicalJSON}
  (\{\texttt{previous}:h_{k-1},\texttt{receipt}:q_k\})+\texttt{LF}\bigr).
\tag{WCTRA.3}

$$

The final chain is `4bd61d085837c0b2098a1151a8336a68c12596e1d29ec99b0c4f40f720920014`. The complete four receipts are:


```json
[{"actual_diff":"","after":"3a4b2e457988d96a5f21c5291a8a8a7fee6117dc","before":"ef5a809c4bf3020b9e6473b98d1864eb71fe0ba8","diff_from_explicit_review":"","finished":"2026-11-16T15:56:08.339427+00:00","read_commit":"2f72b274f8647dbf6ce236ff2185cbe22153f8e1","readme_sha256":{"README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9","topics/visible-flex-exact-nearby/README.md":"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"},"review_sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1","started":"2026-11-16T15:56:07.645764+00:00"},{"actual_diff":"","after":"5cfcccb39b29f126b14c522dfa411d7b63948c9e","before":"3a4b2e457988d96a5f21c5291a8a8a7fee6117dc","diff_from_explicit_review":"","finished":"2026-11-16T15:56:34.206245+00:00","read_commit":"2f72b274f8647dbf6ce236ff2185cbe22153f8e1","readme_sha256":{"README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9","topics/visible-flex-exact-nearby/README.md":"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"},"review_sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1","started":"2026-11-16T15:56:33.063380+00:00"},{"actual_diff":"","after":"40a91573aa3169334c9dcbf6e0479e082f85cca9","before":"40a91573aa3169334c9dcbf6e0479e082f85cca9","diff_from_explicit_review":"","finished":"2026-11-16T15:56:37.047552+00:00","read_commit":"2f72b274f8647dbf6ce236ff2185cbe22153f8e1","readme_sha256":{"README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9","topics/visible-flex-exact-nearby/README.md":"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"},"review_sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1","started":"2026-11-16T15:56:36.746708+00:00"},{"actual_diff":"","after":"beb6e2e462ca66ec0c600b2331352f5e06a72903","before":"40a91573aa3169334c9dcbf6e0479e082f85cca9","diff_from_explicit_review":"","finished":"2026-11-16T16:04:18.012540+00:00","read_commit":"2f72b274f8647dbf6ce236ff2185cbe22153f8e1","readme_sha256":{"README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9","topics/visible-flex-exact-nearby/README.md":"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"},"review_sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1","started":"2026-11-16T16:04:17.001323+00:00"}]
```


The full scientific stdout was not published as a new array, artifact, or split certificate. Its retained complete receipt is:


```json
{"body_not_published_or_split":true,"bytes":49242838,"sha256":"3d60ddf2586026490573a360802b467b4f9ccfb72c0518118b1a81f14205a495"}
```


The 49,242,838-byte stdout body was not read for this note. Completion, all scientific records, all five prefix objects, and all inherited qualifications are available in the two complete small JSON files above. The stdout receipt is a byte-identity receipt, not a substitute for an absent scientific prefix.

The actual capacity and publication objects are retained without reinterpreting their units:


```json
{"consumed_marker_publication":{"already_present":false,"capacity":{"blob_count":14890,"head":"5cfcccb39b29f126b14c522dfa411d7b63948c9e","metadata_bytes":6774574,"metadata_sha256":"b86ab0fe98b173b21a066ac2111b162a1e58f19d6df7f62b03123ec3f217c92f","topic_blob_bytes":199622775,"topic_tree":"c408aa386956243d8202364c692617d7966e545f"},"commit":"40a91573aa3169334c9dcbf6e0479e082f85cca9","projected_topic_bytes":199623406},"final_capacity_metadata":{"blob_count":14883,"head":"beb6e2e462ca66ec0c600b2331352f5e06a72903","metadata_bytes":6772752,"metadata_sha256":"83c7aae3c57114aa24b6437b743370c05b2a84e2e1190a7665d637e771602745","topic_blob_bytes":199381122,"topic_tree":"75be949eebe87253a41774ed02857ff789edd0e3"},"immediate_pre_science_capacity":{"blob_count":14891,"head":"40a91573aa3169334c9dcbf6e0479e082f85cca9","metadata_bytes":6775143,"metadata_sha256":"90bca099b72383f991686eb273d6379be718039609b85f7e3a31c6b63838a73f","topic_blob_bytes":199623406,"topic_tree":"d44926698f1879afab41706183064205e4520626"},"pre_execution_capacity":{"blob_count":14890,"head":"3a4b2e457988d96a5f21c5291a8a8a7fee6117dc","metadata_bytes":6774574,"metadata_sha256":"b86ab0fe98b173b21a066ac2111b162a1e58f19d6df7f62b03123ec3f217c92f","topic_blob_bytes":199622775,"topic_tree":"c408aa386956243d8202364c692617d7966e545f"}}
```


The frozen per-file limits were 99,000 bytes for scientific JSON, 85,000 for execution JSON, and 8,000 for the report; total publication limit 192,000 bytes, with the pre-science 120,000-byte reserve. The actual files are 86,577, 39,658, and 436 bytes, respectively. The final-capacity receipt was taken before publication; it is not labelled as an after-publication tree size. Actual publication succeeded on the first recorded attempt.

The worker retains the original no-automatic-retry rule. No failure or interruption occurred here; `original_scientific_failure`, `failure`, and `interrupted_target` are null. New artifacts, releases, and published arrays are all zero. There is no lost completed target to reconstruct or rerun.

## 9. Read-only verification and mathematical conclusion

This actual-result transcription performed 91 pure JSON/byte checks, all true. They include full canonical reconstruction of the complete scientific and execution files with number lexemes preserved; all 45/44 fields; all 24 gate names and the 26-entry progress shape; all six graph shapes; each of the twenty literal copy equalities; the complete old scope/candidate/repair/maxima/false-result/restoration/archive hashes; the independently rebuilt 43/44 old WVC field tables; all current receipt maps; all nineteen typed historical receipts; all sixteen AST bindings; the complete preflight hash; the public marker binding; and the full four-pull hash chain. No Arb import, old scientific call, binary restoration, full stdout-body read, or new mathematical bound evaluation was performed for this note.

The completed new fact is a fully paid scalar-trace candidate on the same actual operator, with all 36 new bounds and 20 unchanged whole copies saved. Its finite sufficient gate is false. The genuine high tail retains its prior analytic inverse bound; the actual finite inverse, physical 96-column realization, other physical readout conversions, all independent mean/head/affine/cokernel rows, both full right-hand sides, and the metric/nonlinear obligations remain unclosed by this candidate. The saved false result is retained in full and supplies no permission or reason to reevaluate any of its completed targets.
