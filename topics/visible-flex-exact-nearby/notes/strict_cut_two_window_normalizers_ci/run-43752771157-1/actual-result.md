# Complete strict-cut two-window normalizers

All constants refer to the same original P22 moving-angle cut.
The finite complement and both means remain; the true phase and complete incoming inverse are separate.

```json
{
  "actual_mathematical_wall_seconds": 0.5567764159999982,
  "actual_returncode": 0,
  "arithmetic_bits": 320,
  "complete": true,
  "complete_normalized_four_piece_rows": [
    {
      "complete_normalized_four_pieces_upper": {
        "error_density_0": {
          "ball": "[294556810645547059.0912694981426007010831946621151287 +/- 4.02e-35]"
        },
        "error_density_1": {
          "ball": "[5669580209574408.882585951669705567455244642868663129 +/- 4.62e-37]"
        },
        "free_R2": {
          "ball": "[3047536161720808626.970040896157859753626580607000476 +/- 2.40e-34]"
        },
        "free_R3": {
          "ball": "[4443085466682536300.611862174932359527573165435360879 +/- 2.83e-34]"
        }
      },
      "complete_normalized_same_case_sum_upper": {
        "ball": "[7790848019258466395.555758520902525549738185347345148 +/- 4.02e-34]"
      },
      "original_norm_row": 790
    }
  ],
  "complete_normalized_physical_comparison_upper": {
    "ball": "[7790848019258466395.555758520902525549738185347345148 +/- 4.03e-34]"
  },
  "complete_selected_normalizer_conclusion": {
    "all_HL_LH_blocks_and_both_independent_means_retained": true,
    "complete_S2_upper": {
      "ball": "[18921160054105.22244381063520965029844777627259290663 +/- 1.78e-39]"
    },
    "complete_S_upper": {
      "ball": "[1775122.003397473788063705415879829137070478431890423 +/- 1.94e-46]"
    },
    "complete_dyadic_construction": {
      "complete_A1_upper": {
        "ball": "[34830408.82439016768549711417738420245347035797162840 +/- 2.90e-45]"
      },
      "complete_A2_upper": {
        "ball": "[524699837052451.0025502502835145792650470765909617770 +/- 3.01e-38]"
      },
      "first_dyadic_at_least_384": 512,
      "verified_J_ge_4A1": true,
      "verified_J_squared_ge_4A2": true
    },
    "complete_initial_cutoff97_window_verdicts": {
      "Hminus4_3": {
        "both_strict_tests_passed": false,
        "first_margin_lower": {
          "ball": "[-384852.1017270644146858390255315526280029725050548420 +/- 4.81e-47]"
        },
        "first_multiplier_upper": {
          "ball": "[149323003.4701009928981055419062424196651533319612787 +/- 1.47e-44]"
        },
        "first_tau": {
          "ball": "[384853.1017270644146858390255315526280029725050548420 +/- 4.81e-47]"
        },
        "second_margin_lower": {
          "ball": "[-29472157829.98150320723033043589454895246516226182390 +/- 2.38e-42]"
        },
        "second_multiplier_upper": {
          "ball": "[4436856528507279.418829282865141308977499915387544017 +/- 1.56e-37]"
        },
        "second_tau": {
          "ball": "[29472157830.98150320723033043589454895246516226182390 +/- 2.38e-42]"
        }
      },
      "L2": {
        "both_strict_tests_passed": false,
        "first_margin_lower": {
          "ball": "[-4574.056709787303577483776845051106023377521731676347 +/- 4.41e-49]"
        },
        "first_multiplier_upper": {
          "ball": "[1775122.003397473788063705415879829137070478431890423 +/- 1.94e-46]"
        },
        "first_tau": {
          "ball": "[4575.056709787303577483776845051106023377521731676347 +/- 4.41e-49]"
        },
        "second_margin_lower": {
          "ball": "[-125685247.5260470191027914444258841165890123325599601 +/- 1.01e-44]"
        },
        "second_multiplier_upper": {
          "ball": "[18921160054105.22244381063520965029844777627259290663 +/- 1.78e-39]"
        },
        "second_tau": {
          "ball": "[125685248.5260470191027914444258841165890123325599601 +/- 1.01e-44]"
        }
      }
    },
    "complete_selected_cutoff_window_verdicts": {
      "Hminus4_3": {
        "both_strict_tests_passed": true,
        "complete_forward_upper": {
          "ball": "[1.032908245269007140138050534060865412855663416354299 +/- 3.13e-52]"
        },
        "first_inverse_upper": {
          "ball": "[1.033525902830703367093307207978575321677142719534891 +/- 1.55e-52]"
        },
        "first_margin_lower": {
          "ball": "[0.9675616230431381117604538862550874656300049197359707 +/- 2.86e-53]"
        },
        "first_multiplier_upper": {
          "ball": "[34830442.04126045319441439310457385537490120835372519 +/- 1.54e-45]"
        },
        "first_tau": {
          "ball": "[0.03243837695686188823954611374491253436999508026402927 +/- 1.48e-54]"
        },
        "ordered_inverse_upper": {
          "ball": "[1.033996480244116132907373073959872215313214564764608 +/- 1.33e-52]"
        },
        "second_inverse_upper": {
          "ball": "[1.000455312645889097481028230721081893424472881997846 +/- 3.11e-52]"
        },
        "second_margin_lower": {
          "ball": "[0.9995448945693686817615907127253396510829733195252998 +/- 2.95e-53]"
        },
        "second_multiplier_upper": {
          "ball": "[524700837838206.4472692592961417935955260858284212705 +/- 1.75e-38]"
        },
        "second_tau": {
          "ball": "[0.0004551054306313182384092872746603489170266804747001705 +/- 3.31e-56]"
        }
      },
      "L2": {
        "both_strict_tests_passed": true,
        "complete_forward_upper": {
          "ball": "[1.001669649816389437916461198297920696771426256888629 +/- 1.08e-52]"
        },
        "first_inverse_upper": {
          "ball": "[1.001655948827599963856713014875849657654878470999194 +/- 4.49e-52]"
        },
        "first_margin_lower": {
          "ball": "[0.9983467888055392785108986260221527618010803326667376 +/- 3.50e-53]"
        },
        "first_multiplier_upper": {
          "ball": "[1775122.003397473788063705415879829137070478431890423 +/- 1.94e-46]"
        },
        "first_tau": {
          "ball": "[0.001653211194460721489101373977847238198919667333262435 +/- 1.92e-56]"
        },
        "ordered_inverse_upper": {
          "ball": "[1.001672387764244768693237132423321294220230365454558 +/- 3.00e-53]"
        },
        "second_inverse_upper": {
          "ball": "[1.000016411759610718614595060298662387573765930446697 +/- 1.21e-52]"
        },
        "second_margin_lower": {
          "ball": "[0.9999835885097307145385656356642494876400402978722646 +/- 3.51e-53]"
        },
        "second_multiplier_upper": {
          "ball": "[18921160054105.22244381063520965029844777627259290663 +/- 1.78e-39]"
        },
        "second_tau": {
          "ball": "[1.641149026928546143436433575051235995970212773543507e-5 +/- 1.13e-57]"
        }
      }
    },
    "exact_cutoff_abs_j": 268435456,
    "exact_physical_minimum_high_frequency": 1073741824,
    "finite_modes_97_through_J_minus_1_retained": true,
    "first_bandwidth": 192,
    "no_failed_test_interpreted_as_operator_noninvertibility": true,
    "same_inverse_on_common_trigonometric_domain": true,
    "second_bandwidth": 384,
    "selected_cutoff_in_original_moving_circle": true
  },
  "complete_strong_remainder_conclusion": {
    "all_two_original_physical_mean_coordinates_retained": true,
    "complete_A_squared_Hminus4_3_to_L2_upper": {
      "ball": "[1156957861.511165577818018908415946243499259714813034 +/- 2.41e-43]"
    },
    "complete_B_Hminus4_3_to_L2_upper": {
      "ball": "[500393235.6310750193271865979814334703426818252777718 +/- 3.03e-44]"
    },
    "complete_S2_H2_3_multiplier_upper": {
      "ball": "[524700337445090.1191626206830919961275556946044690199 +/- 4.73e-40]"
    },
    "complete_S_H2_3_multiplier_upper": {
      "ball": "[34830425.43282135068186403741954357386573305588713677 +/- 1.74e-46]"
    },
    "complete_S_Hminus1_3_multiplier_upper": {
      "ball": "[34830417.12860476924439366661908309045913177976787655 +/- 7.23e-46]"
    },
    "complete_forward_strong_remainder_upper": {
      "ball": "[501220491.3298527341200482728041020515908236697845435 +/- 2.79e-45]"
    },
    "complete_high_primitive_gain_upper": {
      "ball": "[1.000000000000000000433680868994201773508941572282194 +/- 3.17e-52]"
    },
    "complete_ordered_inverse_strong_remainder_upper": {
      "ball": "[1712923776.640779712602431596288453109737234585600165 +/- 3.77e-43]"
    },
    "complete_two_gain_and_high_embedding_upper": {
      "ball": "[9.536743164062500005514537417020184498345541487428301e-7 +/- 1.33e-59]"
    },
    "complete_uncompressed_first_symbol_finite_difference_upper": {
      "ball": "[3747336834.184293827011820228209080780492048319896249 +/- 2.05e-43]"
    },
    "exact_finite_input_and_output_max_abs_j": 268435647,
    "finite_difference_output_mean_retained": true,
    "first_symbol_sign_in_inverse": "minus S I",
    "inverse_remainder_has_high_input_and_high_output": true,
    "no_finite_schur_inverse_claimed": true,
    "no_phase_projection_identification": true,
    "ordered_inverse_identity": "(I+B)^(-1)(I+A)^(-1)",
    "strong_input_window": "H^(-4/3) in the original moving density circle",
    "strong_output_window": "L2 density; both independent means retained"
  },
  "expected_gates": 16,
  "failure": null,
  "input_manifest_sha256": "9e5688400b91714b189e2ed3865cf5448b54bf26d0ff8fef76ba3af06161646e",
  "kind": "actual_strict_cut_two_window_normalizers_and_strong_remainders_v1",
  "passed_gates": 16,
  "proved": true,
  "recorded_gates": 16,
  "run_attempt": "1",
  "run_id": "43752771157",
  "runtime": {
    "numpy": "2.3.5",
    "python": "3.12.14",
    "python_flint": "0.9.0",
    "scipy": "1.17.0"
  },
  "scope": {
    "actual_full_incoming_or_stable_or_finite_Schur_inverse_not_claimed": true,
    "all_finite_high_and_high_finite_blocks_retained": true,
    "all_two_physical_means_retained": true,
    "complete_radial_derivatives_retained": true,
    "complete_return_R0_not_claimed": true,
    "complete_same_inverse_on_L2_and_Hminus4_3": true,
    "complete_strong_remainder_in_moving_density_coordinates": true,
    "first_symbol_minus_SI_plus_complete_finite_difference": true,
    "full_real_delta_family": true,
    "normalized_physical_error_not_identified_with_whole_incoming_error": true,
    "old_full_q_and_four_physical_columns_read_verbatim": true,
    "original_moving_angle_projection_not_renamed_phase_projection": true,
    "same_exact_P22_cut": true,
    "strict_interval_flow_not_inferred_from_one_cut": true,
    "true_phase_coordinate_and_finite_dual_row_fees_still_separate": true
  },
  "source_sha256": "4dbc776babf0e8be12440bb21ac0765e2676c9cea02912326d46f53cfb627256"
}
```
