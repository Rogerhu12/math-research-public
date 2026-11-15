# Actual factored transport and companion complete-source comparison

Public Actions run 43714194714/1.
Complete: True; proved: True.
Scientific source SHA256: a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7.
Input manifest SHA256: bbfbdbc206f4d724288f8ecb5d9613523f5103ae7c1276ff59f2aaa055476665.

The new calculation bounds the exact factored transport, its genuine rank correction,
the full y/q companions and ten complete source terms. Every original numerical enclosure
and the six-row integrated radial weight are restored. Density 0 uses w0; density 1 uses w1.
All three local terms, the latest complete local aggregate and the other mean terms remain unchanged.

## Complete product and regular quotient

{"accepted_complete_physical_T_image": {"ball": "[0.0001885014939156493405604600380508353022231710322120242938213671900 +/- 3.60e-68]"}, "accepted_complete_physical_X_image": {"ball": "[0.003907463687992234737068312076507931048789525948304580540934332751 +/- 1.32e-67]"}, "all_sT_segments_in_accepted_product": true, "complete_Xi_holomorphic_upper": {"ball": "[1.277575818416176627629578882132825321953048554993375844557244972e-5 +/- 3.38e-69]"}, "complete_cT_holomorphic_upper": {"ball": "[773.7842895657945341407240026516263258488737205448971242580932445 +/- 1.21e-62]"}, "complete_canonical_A_modulus": {"ball": "[0.06315854606777463707215513190297450288739319028739053229008249063 +/- 2.22e-66]"}, "complete_positive_gaps": {"A": {"ball": "[9.444534036403508516012860363711628132345977970829996989999985824 +/- 3.03e-64]"}, "Q_radial": {"ball": "[0.0003343742993999755750934582465561106801033020019531250000000000000 +/- 3e-72]"}, "T_margin": {"ball": "[0.0004114985060843506594395399619491646977768289677879757061786328100 +/- 3.61e-68]"}, "X_margin": {"ball": "[0.002440192562007765262931687923492068951210474051695419459065667249 +/- 1.33e-67]"}, "mu": {"ball": "[18.56551547693817035375544910133315243706114199759417999997004198 +/- 3.41e-63]"}}, "complete_regular_breg_modulus": {"ball": "[517462.0199937107332573523007527844307730711099155955085213995463 +/- 2.17e-59]"}, "exact_accepted_canonical_radius": "3/5000", "exact_accepted_canonical_strip": "13/2048", "exact_full_physical_cover": "893368603925465506687/21990232555520000000000000", "exact_original_fold_radius": "3/8000", "exact_original_fold_strip": "3/128", "exact_physical_phi_strip": "1/256", "exact_regular_root_condition": "B(0,X)=fb(0,X)", "full_mean_and_radial_G_scalar_retained": true, "old_image_fold_forcing_and_amplitude_enclosures_recomputed": false, "physical_T_image_definition_read_from_frozen_producer": true}

## Identified complete inverse remainder

{"accepted_Wiener_minimum": {"ball": "[1.000382715965857285840053227833616858827281705892793553461171534 +/- 1.99e-64]"}, "branch_lower_is_algorithm_number_not_function_lower": true, "complete_inverse_remainder_Wiener_upper": {"ball": "[0.0003827159658572858400532278336168588272817058927935534611715341990 +/- 2e-72]"}, "complete_real_remainder_derivative_upper": [{"ball": "[0.0003827159658572858400532278336168588272817058927935534611715341990 +/- 2e-72]"}, {"ball": "[0.0007653833691339030398484290994480837059728243308145195210218770891 +/- 1.11e-68]"}, {"ball": "[0.1959393141006769595340174558249000069267886928790908022432271163 +/- 2.84e-65]"}, {"ball": "[12.54011610244332541017711717279360044331447634426181134356653545 +/- 5.00e-63]"}], "exact_Wiener_phi_strip": "1/128", "exact_constant_minus_i_epsilon_identity_retained": true, "excluded_first_branch_strict_lower": {"ball": "[64.00635580082777741581709128805201712938343278582183290100222289 +/- 4.57e-63]"}, "original_inverse_or_Fourier_conversion_recomputed": false}

## Complete g operators in the two source windows

[{"Gamma_g": {"ball": "[821918154103.9147982922052434479377232565691570695519308259306723 +/- 4.68e-53]"}, "M_g": {"ball": "[814284607327.4203324577814455788649446750515631626963129645939965 +/- 5.65e-54]"}, "amplitude_identity": "w0", "complete_zero_mode_and_both_signed_carriers": true, "density": 0, "same_complete_column_envelope": "abs(rho)^(-1/4)"}, {"Gamma_g": {"ball": "[1324669328378.703681363049402137296442931819597085718677422883812 +/- 1.36e-52]"}, "M_g": {"ball": "[1324669328378.703681363049402137296442931819597085718677422883812 +/- 1.36e-52]"}, "amplitude_identity": "w1=MZ", "complete_zero_mode_and_both_signed_carriers": true, "density": 1, "same_complete_column_envelope": "abs(rho)^(-1/4)"}]

## Ten whole-term comparisons

| Term | New complete ordinary L2 bound | Selected complete bound | Strictly smaller |
|---|---|---|---|
| density0_complete_RQ_J_g | [99545097040820.28659653706305383417220475308420446859897216106867 +/- 2.82e-51] | [99545097040820.28659653706305383417220475308420446859897216106867 +/- 2.82e-51] | True |
| density0_complete_primitive | [1283932719592.558225150263893686211239669368415949789607387851637 +/- 9.31e-53] | [73558336300.15658716341787958956812671562854970711518503698733611 +/- 4.40e-54] | False |
| density0_old_mean_transported | [117353011057.6972339178681818418832754817901645858885380450472279 +/- 9.38e-54] | [117353011057.6972339178681818418832754817901645858885380450472279 +/- 9.38e-54] | True |
| density0_old_mean_vphi | [282.1288241697791685617203084087321563609975117194322288642006838 +/- 2.57e-62] | [282.1288241697791685617203084087321563609975117194322288642006838 +/- 2.57e-62] | True |
| density0_complete_uJ_g | [1278136241291.734278081507692625457060157813940290164454830924644 +/- 3.84e-52] | [1278136241291.734278081507692625457060157813940290164454830924644 +/- 3.84e-52] | True |
| density1_complete_RQ_J_g | [160434875640652.5783884429824104334510160697493852146502264198253 +/- 4.60e-50] | [160434875640652.5783884429824104334510160697493852146502264198253 +/- 4.60e-50] | True |
| density1_complete_primitive | [2002831988179.852486824699533949153052529577414911497076785185367 +/- 1.36e-52] | [111073115920.6186796122578574699764311328201557549160241521116979 +/- 4.66e-53] | False |
| density1_old_mean_transported | [190908599944.2342695853503431331238231311962123608483910223150323 +/- 1.86e-53] | [190908599944.2342695853503431331238231311962123608483910223150323 +/- 1.86e-53] | True |
| density1_old_mean_vphi | [1246.186417139469688132518206125585645120400462628019704243187054 +/- 2.39e-61] | [610.1586362438034081850446958651586178478567095451746484366636784 +/- 1.51e-62] | False |
| density1_complete_uJ_g | [2059947049319.394173934815262090277414501694998313552637677966001 +/- 2.59e-52] | [2059947049319.394173934815262090277414501694998313552637677966001 +/- 2.59e-52] | True |

## Complete physical source ledger

| Channel | Ordinary radial L2 upper ball |
|---|---|
| local_L2_upper | [292820957408553.9098304627698514918452578890552884273956489551063 +/- 4.28e-50] |
| nonlocal_total_L2_upper | [260780231827512.2165060328328031177898646952615167566168556715262 +/- 3.44e-51] |
| first_L2_upper | [553601189236066.1263364956026546096351225843168051840125046266325 +/- 4.63e-50] |
| mean_L2_upper | [3338315864266.082933296737943933621627342049304710558785120835132 +/- 4.38e-52] |
| combined_L2_upper | [553611254470496.0277809199507349102461437715614759105011257403224 +/- 4.23e-50] |

## All 21 first-output terms

| Term | Complete ordinary L2 upper ball |
|---|---|
| density0_complete_RQ_JL_h | [3526728154.408815581524109723122156257133812818199788002056347066 +/- 1.31e-55] |
| density0_complete_RQ_J_g | [99545097040820.28659653706305383417220475308420446859897216106867 +/- 2.82e-51] |
| density0_complete_SQ | [4285887804.389191901562518397516435257216602761605918354082475386 +/- 3.18e-55] |
| density0_complete_SV | [289595803409.8742397258768206030456943640112617530846354697488932 +/- 4.41e-53] |
| density0_complete_primitive | [73558336300.15658716341787958956812671562854970711518503698733611 +/- 4.40e-54] |
| density0_old_mean_V0 | [1862300951.204677315159507225827549654248405301392655992735589595 +/- 4.82e-55] |
| density0_old_mean_rQ | [7977782.699510422267976150788190366764187603554660304580085345113 +/- 2.61e-58] |
| density0_old_mean_transported | [117353011057.6972339178681818418832754817901645858885380450472279 +/- 9.38e-54] |
| density0_old_mean_vphi | [282.1288241697791685617203084087321563609975117194322288642006838 +/- 2.57e-62] |
| density1_complete_RQ_JL_h | [824668358.6916752076652701399343509503915912980165842435525992978 +/- 2.26e-56] |
| density1_complete_RQ_J_g | [160434875640652.5783884429824104334510160697493852146502264198253 +/- 4.60e-50] |
| density1_complete_SQ | [1002278534.146675412129182834954321844789535453344204807454704359 +/- 1.53e-55] |
| density1_complete_SV | [6218473105.138673351302335504592958060953294185564032732420234440 +/- 2.82e-55] |
| density1_complete_primitive | [111073115920.6186796122578574699764311328201557549160241521116979 +/- 4.66e-53] |
| density1_old_mean_V0 | [39989144.48690305262367955519313861252207563202639142760726342027 +/- 8.01e-58] |
| density1_old_mean_rQ | [1974679.316928390199099933875187769071303648956426235325814004821 +/- 4.97e-58] |
| density1_old_mean_transported | [190908599944.2342695853503431331238231311962123608483910223150323 +/- 1.86e-53] |
| density1_old_mean_vphi | [610.1586362438034081850446958651586178478567095451746484366636784 +/- 1.51e-62] |
| local_raw_1 | [172273911175373.3650514405275696321683717795654989357080938802316 +/- 2.93e-50] |
| local_raw_2 | [120547042738489.7913816171781132396531805348979984007481363754101 +/- 2.57e-50] |
| local_raw_3 | [3494690.753397405064168620023705574591791090939418699464587767446 +/- 8.27e-59] |

## All 10 independent physical-mean terms

| Term | Complete ordinary L2 upper ball |
|---|---|
| density0_complete_K_vminus_w | [1603.314024386500994670141610198657113938582472037557052557883909 +/- 3.79e-61] |
| density0_complete_uJB_w | [172607818.8390799835031770800300406727496506210245370299795187075 +/- 2.11e-56] |
| density0_complete_uJL_h | [45281810.15641255143314336789703229323116340321489893174594514776 +/- 5.80e-58] |
| density0_complete_uJ_g | [1278136241291.734278081507692625457060157813940290164454830924644 +/- 3.84e-52] |
| density0_complete_u_h | [323119.5412015090649186922358216582961095631252850408398416694129 +/- 1.84e-59] |
| density1_complete_K_vminus_w | [95.34009403293600232242050505722676591987116503313595129600318391 +/- 3.16e-63] |
| density1_complete_uJB_w | [3706378.943312939149911560475027498619596399407645193279102894478 +/- 4.97e-59] |
| density1_complete_uJL_h | [10588419.25948435151821342552595997202569402729203685218826087294 +/- 3.21e-57] |
| density1_complete_uJ_g | [2059947049319.394173934815262090277414501694998313552637677966001 +/- 2.59e-52] |
| density1_complete_u_h | [64409.56087152630862809916115533173427223432365249321881364816342 +/- 4.26e-60] |

## Actual identity and mathematical gates

- the source manifest exact products and new-only scalar scope have their reviewed identities: True.
- all seven accepted scientific receipts and every frozen source and legacy byte identity are exact: True.
- the complete fold and physical background retain their exact legacy payload and successful publication: True.
- accepted complete run 43698106023/1 is restored with its exact scientific identity: True.
- accepted complete run 43700281022/1 is restored with its exact scientific identity: True.
- accepted complete run 43702688640/1 is restored with its exact scientific identity: True.
- accepted complete run 43703879926/1 is restored with its exact scientific identity: True.
- accepted complete run 43709396175/1 is restored with its exact scientific identity: True.
- accepted complete run 43711480764/1 is restored with its exact scientific identity: True.
- accepted complete run 43688459733/1 is restored with its exact scientific identity: True.
- the full original complex squares fixed intrinsic root genuine signs and physical mean are unchanged: True.
- the latest refined local ledger is retained with all original nonlocal terms and source windows: True.
- the saved T image uses the whole SG fold modulus and M Bi B2 share the accepted canonical inverse product: True.
- the original 1328 complete coefficient rows retain their successful native and process identities: True.
- the identical six physical intersections and saved squared-envelope measure are restored without radial integration: True.
- the three complete words retain both full matrix windows and their entire original radius case: True.
- the eighteen accepted positive coefficients retain the identical complete profile branches and input ordering: True.
- all real forcing and correction jets and the two fourth derivatives are restored with complete tails and means: True.
- the accepted physical image is the identical full-fold expression and the larger regular product remains exact: True.
- every new complete regular-quotient margin and original nonzero gap is positive on the same physical strip: True.
- both complete density sources preserve the ordered genuine rank and their exact physical input weights: True.
- the frozen inverse minimum selected its constant-plus-remainder branch with a nonnegative recoverable remainder: True.
- ten complete source comparisons preserve every actual row, independent mean factor and unchanged local term: True.
- only the ten declared whole terms may change and the thirteen other first terms eight other means and full local aggregate remain verbatim: True.
- the complete new negative volume source is finite with both density windows true dr and independent physical mean: True.

## Counts and scope

{"all_actual_physical_seams_and_reference_matching_sources_retained": true, "all_input_abs_j_at_least97": true, "all_old_h_amplitude_source_terms_retained_verbatim": true, "both_complete_directed_word_windows_retained": true, "both_genuine_columns_and_both_carrier_signs": true, "complete_genuine_rank_and_exact_input_n_minus_two_retained": true, "complete_row_and_derivative_arrays_published": false, "cutoff97_strong_return_contraction_paid": false, "density_one_amplitude": "w1=MZ", "density_zero_amplitude": "w0", "exact_regular_B_root_condition_and_all_sT_paths_retained": true, "exact_signed_factorization_before_absolute_bounds": true, "final_operators_restrict_to_original_real_parameters": true, "full_G_radial_scalar_and_all_amplitude_means_retained": true, "full_complex_delta_and_z_squares_in_supporting_bounds": true, "full_negative_BVP_inverse_paid": false, "inverse_remainder_read_from_identified_frozen_minimum_branch": true, "latest_refined_first_local_result_and_all_local_terms_retained": true, "negative_side_only": true, "new_supporting_factor_jets_distinct_from_original_ordered_closure": true, "no_duplicate_inner_word_or_physical_mean_factors": true, "original_eighteen_positive_coefficients_only_read": true, "original_fixed_intrinsic_parameter": "eta_0", "original_physical_root_piece_2549_only": true, "original_positive_graph_and_outer_source_ports_retained": true, "original_source_rows_and_all_radial_integrals_only_read": true, "output_mean_and_complete_original_primitive_retained": true, "physical_J_only_on_its_proved_reflected_parity_domain": true, "physical_to_wave_readout_paid": false, "positive_growing_column_operator_paid": false, "q_is_v_Dw_minus_angle_derivative_of_vp_not_D_of_vw": true, "same_original_real_explicit_family": true}

Actual new scalar seconds: 0.1712966910000091.
Failure: None.
Temporary native SHA256: e9fe0bc314dea07e8a7315b7233a48dc226cc142aa6a308341766a98206edab0.
Full derivative and six-row coefficient tables remain temporary.
These volume-source bounds do not prove a physical-to-wave trace, positive graph, full high inverse or strong return.
