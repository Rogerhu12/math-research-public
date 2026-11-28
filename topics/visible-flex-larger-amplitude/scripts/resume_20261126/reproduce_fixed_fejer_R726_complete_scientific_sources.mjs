#!/usr/bin/env node
// Complete source-text reproduction only. No Python import, AST, fixture or science.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const TOPIC = "topics/visible-flex-larger-amplitude";
const SPEC = [
  {
    "role": "meridian",
    "complete_parent": {
      "role": "meridian",
      "name": "fixed_fejer_r725_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_meridian_operator.py",
      "bytes": 40826,
      "sha256": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
      "complete_parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_operator.py",
        "name": "fixed_fejer_paired_halfwave_meridian_operator.py",
        "bytes": 40803,
        "sha256": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "git_blob_sha": "350c2e057e6af15e663d0fdb463a518bebc36234"
      },
      "git_blob_sha": "e6fae2e1729f5c9c325400a5d5261994a71ab961"
    },
    "complete_output": {
      "role": "meridian",
      "name": "fixed_fejer_r726_meridian_operator.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_meridian_operator.py",
      "bytes": 40841,
      "sha256": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
      "git_blob_sha": "25de5386e8f450ea16eaaf21eb5ba098e1df196e"
    },
    "complete_reversible_text_patches": [
      {
        "label": "accurate fixed seed description",
        "before": "complete fixed R725 paired-halfwave seed from original reference core/H; full complement, epsilon=1/8 three-piece C3 boundary cutoffs and equal opposite six-piece central halfwaves",
        "after": "complete fixed R726 spherical-boundary seed from original reference core/H; full complement, R725 epsilon=1/8 three-piece C3 cutoff and R724 equal opposite six-piece central halfwaves",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "before": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "new_moment_input",
    "complete_parent": {
      "role": "new_moment_input",
      "name": "fixed_fejer_r725_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_literal_zero_moment_input.py",
      "bytes": 40077,
      "sha256": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
      "complete_parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "name": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "bytes": 34886,
        "sha256": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "git_blob_sha": "4625d2775b960a8859ddd88de215cc736a84363f"
      },
      "git_blob_sha": "59c7ee5abe717226db17284b07c347d38d419a65"
    },
    "complete_output": {
      "role": "new_moment_input",
      "name": "fixed_fejer_r726_literal_zero_moment_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_literal_zero_moment_input.py",
      "bytes": 43818,
      "sha256": "b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7",
      "git_blob_sha": "bd8a61fb7315805c56c247224477964dd21eed9e"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current pure input description",
        "before": "Bind eighteen fixed Q words to one complete R725 paired-halfwave reference seed.",
        "after": "Bind eighteen fixed Q words to one complete R726 spherical-boundary paired-halfwave seed.",
        "occurrences": 1
      },
      {
        "label": "complete pure spherical definition",
        "before": "\ndef _supported_seed(",
        "after": "\nSPHERICAL_BOUNDARY_SCHEMA = \"complete-R726-spherical-boundary-working-value-and-angular-jets-v1\"\nSPHERICAL_SMALL_Q_MAX = 0.25\nSPHERICAL_SERIES_DEGREE = 32\nR726_PROOF_SHA256 = \"faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b\"\n\n\ndef _spherical_boundary_definition():\n    \"\"\"Complete declared formulas; this function evaluates no field or root.\"\"\"\n    return dict(\n        schema=SPHERICAL_BOUNDARY_SCHEMA,\n        source_sha256=SEED_MEAN_KERNEL_SOURCE_SHA,\n        theorem_source_sha256=R726_PROOF_SHA256,\n        accurate_boundary=\"S_chi(N(x),N(y)); S=sin((1-chi)*theta)/sin(theta)*u+sin(chi*theta)/sin(theta)*d\",\n        accurate_zero_angle=\"the analytic extension at u=d, with value u\",\n        accurate_domain=\"nonzero x,y and N(x) != -N(y); acute-root theorems have additional hypotheses\",\n        accurate_normal_extension=\"normalize both arguments; output normalization is the identity in exact Slerp arithmetic\",\n        working_coordinate=\"q=sum((N(x)-N(y))**2)/2; no clipping of q or dot products\",\n        working_output=\"N(f_(1-chi)(q)*N(x)+f_chi(q)*N(y))\",\n        working_small_q_interval=[0.0, SPHERICAL_SMALL_Q_MAX],\n        working_small_q_degree=SPHERICAL_SERIES_DEGREE,\n        working_coefficient_recurrence=\"c0=a; c[n+1]=(((n+1)**2-a*a)/((n+1)*(2*n+3)))*c[n]\",\n        working_q_derivatives=\"first and second simultaneous Horner derivatives of the same actual coefficient array\",\n        working_a_derivative=\"differentiate the same coefficient recurrence; never substitute a separately rounded derivative table\",\n        working_large_q=\"theta=acos(1-q); f=sin(a*theta)/sin(theta); explicit first/second chain derivatives\",\n        working_coefficient_endpoints=\"a=0 or1 uses the exact constant coefficient value and zero q derivatives; a derivative is retained\",\n        input_normalizations_and_output_normalization_differentiated=True,\n        small_series_truncation_is_not_an_exact_Slerp_identity=True,\n        branch_switch_is_not_claimed_exact_C2_in_working_arithmetic=True,\n        coefficient_rounding_trigonometric_quadrature_root_and_jet_errors_enclosed=False,\n        degree32_exact_coefficient_tail_bounds_at_q_quarter=dict(\n            value_strictly_below=\"2^-98\", q_first_strictly_below=\"2^-91\",\n            q_second_strictly_below=\"2^-84\", a_first_strictly_below=\"2^-96\",\n            scope=\"only infinite-series truncation in exact arithmetic; not floating-point or full-field error\"),\n        R709_Euclidean_potential_or_R722_posterior_formula_inherited=False,\n        R726_acute_existence_or_global_branch_verified=False,\n        working_antipodal_or_nonfinite_pairs_unavailable=True,\n        all_original_boundary_nodes_weights_and_two_angular_orders_retained=True)\n\n\n\ndef _supported_seed(",
        "occurrences": 1
      },
      {
        "label": "whole accurate spherical model equality",
        "before": "    working = seed.get('working_definition')\n",
        "after": "    spherical = _spherical_boundary_definition()\n    if (seed.get('spherical_boundary_definition') != spherical\n            or seed.get('accurate_definition') != 'fixed original unit T0 outside U; R726 S_chi(T0,d) on all boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals'\n            or seed.get('accurate_mean_definition') != 'Lc*v+integral_E S_chi(T0,N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)'):\n        raise ValueError('Bind the complete independent spherical boundary and actual new mean equation')\n    working = seed.get('working_definition')\n",
        "occurrences": 1
      },
      {
        "label": "complete spherical working graph binding",
        "before": "            or working.get('physical_central_profile_definition') != paired\n",
        "after": "            or working.get('physical_central_profile_definition') != paired\n            or working.get('spherical_boundary_definition') != spherical\n            or working.get('mean_and_field_use_same_raw_v_and_full_two_angular_jet_graph') is not True\n            or working.get('old_R709_potential_or_R722_posterior_formula_inherited') is not False\n            or working.get('R726_acute_domain_and_existence_hypotheses_certified') is not False\n",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "before": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "before": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-r726-reference-literal-zero-endpoint-Q-input-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "before": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-r726-reference-literal-two-bubble-endpoint-Q-v1",
        "occurrences": 1
      },
      {
        "label": "current schema paired-halfwave-flat-cutoff-reference-working-definition-v1",
        "before": "paired-halfwave-flat-cutoff-reference-working-definition-v1",
        "after": "R726-spherical-boundary-paired-halfwave-reference-working-definition-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_mean",
        "before": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "after": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "closure_values",
    "complete_parent": {
      "role": "closure_values",
      "name": "fixed_fejer_r725_closure_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_closure_values.py",
      "bytes": 59438,
      "sha256": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
      "complete_parent": {
        "role": "closure_values",
        "name": "fixed_fejer_paired_halfwave_closure_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_closure_values.py",
        "bytes": 59449,
        "sha256": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "git_blob_sha": "5e7230ce5dc57adffe58901b04257c1469fa8e8c"
      },
      "git_blob_sha": "f5e937ae12c4d769aeeae390fc1546dfa45f0375"
    },
    "complete_output": {
      "role": "closure_values",
      "name": "fixed_fejer_r726_closure_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_closure_values.py",
      "bytes": 59438,
      "sha256": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
      "git_blob_sha": "57b1e908bbd6ea4ad2f9e5d9d6d980e8363d0a50"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "analytic_J3",
    "complete_parent": {
      "role": "analytic_J3",
      "name": "fixed_fejer_r725_analytic_stage_jacobian.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_analytic_stage_jacobian.py",
      "bytes": 25695,
      "sha256": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
      "complete_parent": {
        "role": "analytic_J3",
        "name": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "bytes": 25706,
        "sha256": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "git_blob_sha": "aaa1d6b48f02d62b5a7a445932304d3e36730fa3"
      },
      "git_blob_sha": "168028b77a73803d685ea9cd8f41a6ad57497adb"
    },
    "complete_output": {
      "role": "analytic_J3",
      "name": "fixed_fejer_r726_analytic_stage_jacobian.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_analytic_stage_jacobian.py",
      "bytes": 25695,
      "sha256": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
      "git_blob_sha": "4168a22251e8664a141114076a764712717f9db8"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "analytic_frame",
    "complete_parent": {
      "role": "analytic_frame",
      "name": "fixed_fejer_r725_analytic_normal_frame.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_analytic_normal_frame.py",
      "bytes": 47429,
      "sha256": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
      "complete_parent": {
        "role": "analytic_frame",
        "name": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "bytes": 47440,
        "sha256": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
        "git_blob_sha": "263534a4e65f31b45cf1f9a40441f5896e213e2b"
      },
      "git_blob_sha": "ec3dcb2fbb86a0ddd3769088a7b22ec93eb712c1"
    },
    "complete_output": {
      "role": "analytic_frame",
      "name": "fixed_fejer_r726_analytic_normal_frame.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_analytic_normal_frame.py",
      "bytes": 47429,
      "sha256": "56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a",
      "git_blob_sha": "a5443a021de35952db79f420144f5f71f746bc87"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "frame_C1",
    "complete_parent": {
      "role": "frame_C1",
      "name": "fixed_fejer_r725_normal_frame_c1.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_normal_frame_c1.py",
      "bytes": 37361,
      "sha256": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
      "complete_parent": {
        "role": "frame_C1",
        "name": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "bytes": 37361,
        "sha256": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "git_blob_sha": "84a063e3efaa54b872b3ff0ff0f8a222ba0712e0"
      },
      "git_blob_sha": "a029d203db41ce32c0f12bfd1ba05f4750ad426f"
    },
    "complete_output": {
      "role": "frame_C1",
      "name": "fixed_fejer_r726_normal_frame_c1.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_normal_frame_c1.py",
      "bytes": 37361,
      "sha256": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
      "git_blob_sha": "bbcb2f37c72951108a60329a88fac9f3314645c1"
    },
    "complete_reversible_text_patches": [
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "stage_matrices",
    "complete_parent": {
      "role": "stage_matrices",
      "name": "fixed_fejer_r725_stage_matrices.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_stage_matrices.py",
      "bytes": 61280,
      "sha256": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
      "complete_parent": {
        "role": "stage_matrices",
        "name": "fixed_fejer_paired_halfwave_stage_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_stage_matrices.py",
        "bytes": 61280,
        "sha256": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "git_blob_sha": "9eabce7cdf2460213b8d2bea4005321ec9ab4591"
      },
      "git_blob_sha": "040cf58e8933d19b04485fd409b338e99480a47d"
    },
    "complete_output": {
      "role": "stage_matrices",
      "name": "fixed_fejer_r726_stage_matrices.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_stage_matrices.py",
      "bytes": 61280,
      "sha256": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
      "git_blob_sha": "c89d7d37bc133c4551a8703d8346b6e99797f766"
    },
    "complete_reversible_text_patches": [
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "adjacent_matrices",
    "complete_parent": {
      "role": "adjacent_matrices",
      "name": "fixed_fejer_r725_adjacent_matrices.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_adjacent_matrices.py",
      "bytes": 36766,
      "sha256": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
      "complete_parent": {
        "role": "adjacent_matrices",
        "name": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "bytes": 36766,
        "sha256": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "git_blob_sha": "6fcac6e4f16191b2b7be20f1c04bbab884632985"
      },
      "git_blob_sha": "4ff977c1672b0bbaecf2ae9d3cac047c0fad3670"
    },
    "complete_output": {
      "role": "adjacent_matrices",
      "name": "fixed_fejer_r726_adjacent_matrices.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_adjacent_matrices.py",
      "bytes": 36766,
      "sha256": "21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062",
      "git_blob_sha": "fe312ad5c70a67f961d78e8900fe1c5899dd4406"
    },
    "complete_reversible_text_patches": [
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      },
      {
        "label": "complete dependency stage_matrices",
        "before": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "after": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "reference_calibration",
    "complete_parent": {
      "role": "reference_calibration",
      "name": "fixed_fejer_r725_reference_calibration.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_reference_calibration.py",
      "bytes": 11850,
      "sha256": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
      "complete_parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_reference_calibration.py",
        "name": "fixed_fejer_paired_halfwave_reference_calibration.py",
        "bytes": 11872,
        "sha256": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "git_blob_sha": "812e981a9e4a6302c6241129dd812c251bb92691"
      },
      "git_blob_sha": "c1d612b7e403a9877e98501e799b9713a7a84389"
    },
    "complete_output": {
      "role": "reference_calibration",
      "name": "fixed_fejer_r726_reference_calibration.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_reference_calibration.py",
      "bytes": 11850,
      "sha256": "1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f",
      "git_blob_sha": "0600eb0f58eae935c95a6632b64f274379bbbd68"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_mean",
        "before": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "after": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "detached_meridian_values",
    "complete_parent": {
      "role": "detached_meridian_values",
      "name": "fixed_fejer_r725_detached_meridian_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_detached_meridian_values.py",
      "bytes": 41124,
      "sha256": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
      "complete_parent": {
        "role": "detached_meridian_values",
        "name": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "bytes": 41135,
        "sha256": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "git_blob_sha": "7075bca30d05c045023b7823b8f80b75bfd34d4f"
      },
      "git_blob_sha": "01d785136dc76b5d9e521ff8458e4feb75fdcfca"
    },
    "complete_output": {
      "role": "detached_meridian_values",
      "name": "fixed_fejer_r726_detached_meridian_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_detached_meridian_values.py",
      "bytes": 41124,
      "sha256": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
      "git_blob_sha": "30fac31454487f372536649b63fe4eed4cca704c"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "endpoint",
    "complete_parent": {
      "role": "endpoint",
      "name": "fixed_fejer_r725_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_normal_lift.py",
      "bytes": 96250,
      "sha256": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
      "complete_parent": {
        "role": "endpoint",
        "name": "fixed_fejer_paired_halfwave_normal_lift.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_lift.py",
        "bytes": 96271,
        "sha256": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
        "git_blob_sha": "f285b87e4705b534935dab238d531be22af90740"
      },
      "git_blob_sha": "f68cc3f67a8f64ac49149fa86ad10c3994736e0e"
    },
    "complete_output": {
      "role": "endpoint",
      "name": "fixed_fejer_r726_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_normal_lift.py",
      "bytes": 96262,
      "sha256": "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9",
      "git_blob_sha": "0d0ab3e7a6982ff50224adc9152fb78b2ae2f2bd"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "before": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "before": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-r726-reference-literal-zero-endpoint-Q-input-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_mean",
        "before": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "after": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency new_moment_input",
        "before": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
        "after": "b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_frame",
        "before": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
        "after": "56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      },
      {
        "label": "complete dependency stage_matrices",
        "before": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "after": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
        "occurrences": 1
      },
      {
        "label": "complete dependency adjacent_matrices",
        "before": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
        "after": "21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062",
        "occurrences": 1
      },
      {
        "label": "complete dependency reference_calibration",
        "before": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
        "after": "1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f",
        "occurrences": 1
      },
      {
        "label": "complete dependency detached_meridian_values",
        "before": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "after": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "root_packets",
    "complete_parent": {
      "role": "root_packets",
      "name": "fixed_fejer_r725_root_packets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_root_packets.py",
      "bytes": 75036,
      "sha256": "71f80c72819f70d62ce2be70e075aa0ebda4130db3ebf7de7616d8a173ffeea1",
      "complete_parent": {
        "role": "root_packets",
        "name": "fixed_fejer_paired_halfwave_root_packets.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_root_packets.py",
        "bytes": 74385,
        "sha256": "8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a",
        "git_blob_sha": "b340f47df551b4609e45ae547449adadbc3368b6"
      },
      "git_blob_sha": "acbd48bf27a4fbc00b77c11dba369a569c764605"
    },
    "complete_output": {
      "role": "root_packets",
      "name": "fixed_fejer_r726_root_packets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_root_packets.py",
      "bytes": 75687,
      "sha256": "9da481209cd48d82cb297b213650cc94c4f2148c097602f3495d57ba8f4508fc",
      "git_blob_sha": "960eba2300fb678725c68b3d93dbea14374a0cc9"
    },
    "complete_reversible_text_patches": [
      {
        "label": "new exact current normal registry entry; whole former registry retained",
        "before": "NORMALS = {\n",
        "after": "NORMALS = {\n    '335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9': dict(schema='complete-fixed-fejer-r726-detached-meridian-normal-layer-v1',\n        base='bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37',\n        adjacent='21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062',calibration='1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f',\n        analytic='81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4',analytic_frame='56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a',\n        closure_values='6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3'),\n",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "analytic_J3_binding",
    "complete_parent": {
      "role": "analytic_J3_binding",
      "name": "fixed_fejer_r725_source_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_source_binding.py",
      "bytes": 50527,
      "sha256": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
      "complete_parent": {
        "role": "analytic_J3_binding",
        "name": "fixed_fejer_paired_halfwave_source_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_source_binding.py",
        "bytes": 41966,
        "sha256": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
        "git_blob_sha": "1abdf0ca7867b1deb54a2a6d6e7c8130e42cf948"
      },
      "git_blob_sha": "f1f59a47b5f6eec2abf6d5b6cd247417a4a14c56"
    },
    "complete_output": {
      "role": "analytic_J3_binding",
      "name": "fixed_fejer_r726_source_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_source_binding.py",
      "bytes": 52866,
      "sha256": "77c4a98d8736f10edcb33e640749033499366e41acbe8b962a0877d304235cfa",
      "git_blob_sha": "cd39a09167892c0aa184bd5ef5edb2e0029c36dd"
    },
    "complete_reversible_text_patches": [
      {
        "label": "same complete spherical mean source/model and unpaid theorem scope",
        "before": "                or metadata.get('source_sha256') != roles['seed_mean']\n",
        "after": "                or metadata.get('source_sha256') != roles['seed_mean']\n                or metadata.get('spherical_boundary') != seed.get('spherical_boundary_definition')\n                or metadata.get('root_equations') != ['central_length*v + integral_boundary S_chi(N(T0),N(v)) - K = 0', 'a_delta(lambda) - norm(v) = 0']\n                or metadata.get('R709_Euclidean_potential_inherited') is not False\n                or metadata.get('R722_specialized_posterior_formula_inherited') is not False\n                or metadata.get('R726_acute_existence_uniqueness_verified') is not False\n                or metadata.get('working_domain_is_nonantipodal_not_an_acute_proof_gate') is not True\n",
        "occurrences": 1
      },
      {
        "label": "read real spherical pair diagnostics",
        "before": "        completed.extend(angles)\n",
        "after": "        spherical_count = metadata.get('actual_boundary_node_count')\n        if (isinstance(spherical_count,bool) or not isinstance(spherical_count,int)\n                or spherical_count < 1 or metadata.get('actual_angle_count') != len(angles)):\n            raise ValueError('Retain all actual spherical boundary nodes and angles')\n        pair_counts = [metadata.get('actual_spherical_small_series_pair_count'),\n                       metadata.get('actual_spherical_trigonometric_pair_count')]\n        if (any(isinstance(v,bool) or not isinstance(v,int) or v<0 for v in pair_counts)\n                or sum(pair_counts) != spherical_count*len(angles)):\n            raise ValueError('Keep both full working Slerp coefficient branches and their actual pair counts')\n        qlo, qhi = metadata.get('actual_spherical_minimum_q'), metadata.get('actual_spherical_maximum_q')\n        if (any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v)\n                for v in (qlo,qhi)) or not 0<=qlo<=qhi<2\n                or metadata.get('actual_sampled_acute_pairs') != (qhi<=1)\n                or metadata.get('sampled_acute_pairs_are_not_a_whole_domain_or_existence_certificate') is not True\n                or metadata.get('boundary_normalization_norm_scope') != 'output of the declared spherical coefficient sum, not the old Euclidean blend Y'):\n            raise ValueError('Read the actual nonantipodal sample domain without promoting it to a continuous root certificate')\n        completed.extend(angles)\n",
        "occurrences": 1
      },
      {
        "label": "complete spherical formula in pure seed readout",
        "before": "        boundary_cutoff_definition=seed['boundary_cutoff_definition'],\n",
        "after": "        boundary_cutoff_definition=seed['boundary_cutoff_definition'],\n        spherical_boundary_definition=seed['spherical_boundary_definition'],\n        R726_accurate_root_domain_and_angle_jet_certificate=False,\n        old_R709_or_R722_boundary_certificate_inherited=False,\n",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-source-model-and-report-binding-v1",
        "before": "complete-fixed-fejer-r725-source-model-and-report-binding-v1",
        "after": "complete-fixed-fejer-r726-source-model-and-report-binding-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1",
        "before": "complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1",
        "after": "complete-R726-spherical-boundary-paired-halfwave-seed-radial-plan-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1",
        "before": "complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1",
        "after": "complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename closure_values",
        "before": "fixed_fejer_r725_closure_values.py",
        "after": "fixed_fejer_r726_closure_values.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_J3",
        "before": "fixed_fejer_r725_analytic_stage_jacobian.py",
        "after": "fixed_fejer_r726_analytic_stage_jacobian.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_frame",
        "before": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
        "after": "56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_frame",
        "before": "fixed_fejer_r725_analytic_normal_frame.py",
        "after": "fixed_fejer_r726_analytic_normal_frame.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename frame_C1",
        "before": "fixed_fejer_r725_normal_frame_c1.py",
        "after": "fixed_fejer_r726_normal_frame_c1.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency stage_matrices",
        "before": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "after": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename stage_matrices",
        "before": "fixed_fejer_r725_stage_matrices.py",
        "after": "fixed_fejer_r726_stage_matrices.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency adjacent_matrices",
        "before": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
        "after": "21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename adjacent_matrices",
        "before": "fixed_fejer_r725_adjacent_matrices.py",
        "after": "fixed_fejer_r726_adjacent_matrices.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency reference_calibration",
        "before": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
        "after": "1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename reference_calibration",
        "before": "fixed_fejer_r725_reference_calibration.py",
        "after": "fixed_fejer_r726_reference_calibration.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency detached_meridian_values",
        "before": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "after": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename detached_meridian_values",
        "before": "fixed_fejer_r725_detached_meridian_values.py",
        "after": "fixed_fejer_r726_detached_meridian_values.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency endpoint",
        "before": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
        "after": "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename endpoint",
        "before": "fixed_fejer_r725_normal_lift.py",
        "after": "fixed_fejer_r726_normal_lift.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "envelope_transfer",
    "complete_parent": {
      "role": "envelope_transfer",
      "name": "fixed_fejer_r725_memory_transfer.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_memory_transfer.py",
      "bytes": 78945,
      "sha256": "d9615e37f3fd0da916147674ff8f47be69cb6876ba98aa71e78eccd4d2fcc637",
      "complete_parent": {
        "role": "envelope_transfer",
        "name": "fixed_fejer_halfwave_memory_transfer.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_memory_transfer.py",
        "bytes": 78920,
        "sha256": "64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef",
        "git_blob_sha": "27de8f1dbc5ff704be9457617cc8a0a4cec613e6"
      },
      "git_blob_sha": "f5758234ebe77f6f1f406acf35a40b607922885b"
    },
    "complete_output": {
      "role": "envelope_transfer",
      "name": "fixed_fejer_r726_memory_transfer.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_memory_transfer.py",
      "bytes": 78993,
      "sha256": "01e6f6a80b3556ec941d9f46431e7b5b6b6de7892865040c5f61a09117b5bc03",
      "git_blob_sha": "42f9aea478cd403e63145faf56afab91964dcb58"
    },
    "complete_reversible_text_patches": [
      {
        "label": "physical field mechanism is new, target and history stay precise",
        "before": "same predeclared Fejer target and full layout; distinct R725 epsilon=1/8 boundary law, full split seed plan and new seed/Q/calibration identities; old complete physical-model equality guards remain strict",
        "after": "same predeclared Fejer target and full layout; distinct R726 spherical boundary and complete new mean/two-angle chain, original R725 cutoff/full split plan and new seed/Q/calibration identities; old complete physical-model equality guards remain strict",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-history-and-same-source-continuation-v1",
        "before": "complete-fixed-fejer-r725-history-and-same-source-continuation-v1",
        "after": "complete-fixed-fejer-r726-history-and-same-source-continuation-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3_binding",
        "before": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
        "after": "77c4a98d8736f10edcb33e640749033499366e41acbe8b962a0877d304235cfa",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_J3_binding",
        "before": "fixed_fejer_r725_source_binding.py",
        "after": "fixed_fejer_r726_source_binding.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "geometry_selector",
    "complete_parent": {
      "role": "geometry_selector",
      "name": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_r725_curvature_cache.py",
      "bytes": 35982,
      "sha256": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
      "complete_parent": {
        "role": "geometry_selector",
        "name": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
        "bytes": 35982,
        "sha256": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
        "git_blob_sha": "a8c04e0044ae95d1debd4d96dcd753430f0fd797"
      },
      "git_blob_sha": "3df348d7a1b9c7a2926886c6dc6fc7cd4f49b4f7"
    },
    "complete_output": {
      "role": "geometry_selector",
      "name": "fullclosed_point_inequalities_v2_r726_curvature_cache.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_r726_curvature_cache.py",
      "bytes": 35982,
      "sha256": "4386ce195c9709e0bb204cd749b89429652a177bb497bbc2fcf2756564496253",
      "git_blob_sha": "20c916cdc2d097c10684cc5851c1bbac11fc69c8"
    },
    "complete_reversible_text_patches": [
      {
        "label": "complete dependency detached_meridian_values",
        "before": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "after": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
        "occurrences": 1
      },
      {
        "label": "complete dependency endpoint",
        "before": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
        "after": "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "geometry",
    "complete_parent": {
      "role": "geometry",
      "name": "so3_fixed_fejer_r725_dk_cache_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_r725_dk_cache_geometry.py",
      "bytes": 88422,
      "sha256": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
      "complete_parent": {
        "role": "geometry",
        "name": "so3_fixed_fejer_halfwave_dk_cache_geometry.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_halfwave_dk_cache_geometry.py",
        "bytes": 88487,
        "sha256": "da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316",
        "git_blob_sha": "624871ceac5955b78fe2ba0728ff50ddee99d64d"
      },
      "git_blob_sha": "bd8f50715b8fbe971e11634b5b7b0539c8a37844"
    },
    "complete_output": {
      "role": "geometry",
      "name": "so3_fixed_fejer_r726_dk_cache_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_r726_dk_cache_geometry.py",
      "bytes": 88434,
      "sha256": "b46cd96f5bfe019137b1332750ab3f81b3c100895cff33187898ab0e1daaaa65",
      "git_blob_sha": "ae9427232abb807586cbe108ea8e825c78eff524"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "before": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "before": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-r726-reference-literal-zero-endpoint-Q-input-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "before": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-r726-reference-literal-two-bubble-endpoint-Q-v1",
        "occurrences": 2
      },
      {
        "label": "current schema complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
        "before": "complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
        "after": "complete-fixed-fejer-r726-dk-cache-world-geometry-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_mean",
        "before": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "after": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency new_moment_input",
        "before": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
        "after": "b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      },
      {
        "label": "complete dependency stage_matrices",
        "before": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "after": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
        "occurrences": 1
      },
      {
        "label": "complete dependency adjacent_matrices",
        "before": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
        "after": "21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062",
        "occurrences": 1
      },
      {
        "label": "complete dependency reference_calibration",
        "before": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
        "after": "1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f",
        "occurrences": 1
      },
      {
        "label": "complete dependency detached_meridian_values",
        "before": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "after": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
        "occurrences": 1
      },
      {
        "label": "complete dependency endpoint",
        "before": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
        "after": "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9",
        "occurrences": 1
      },
      {
        "label": "complete dependency geometry_selector",
        "before": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
        "after": "4386ce195c9709e0bb204cd749b89429652a177bb497bbc2fcf2756564496253",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename geometry_selector",
        "before": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
        "after": "fullclosed_point_inequalities_v2_r726_curvature_cache.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "batched_geometry_binding",
    "complete_parent": {
      "role": "batched_geometry_binding",
      "name": "fixed_fejer_r725_dk_cache_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_dk_cache_binding.py",
      "bytes": 20516,
      "sha256": "d951f9e5f8088fdbd58357e29bca71f8057e5133693112657c288f57346c2819",
      "complete_parent": {
        "role": "batched_geometry_binding",
        "name": "fixed_fejer_halfwave_dk_cache_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_dk_cache_binding.py",
        "bytes": 20546,
        "sha256": "ca2a7884039df93f7b5b243d476c60d2e8e810bf1071545a84bbc283a460aaad",
        "git_blob_sha": "319ed19012c7b588e85108a98ace0efcca830c75"
      },
      "git_blob_sha": "622c9c7a5eb21430c268eb277cc8b81a71e6ae3a"
    },
    "complete_output": {
      "role": "batched_geometry_binding",
      "name": "fixed_fejer_r726_dk_cache_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r726_dk_cache_binding.py",
      "bytes": 20516,
      "sha256": "f24ff296f0a058d43a779c17d11916c4eec1fbcf26e337ede73f433b7db61422",
      "git_blob_sha": "4a58b6f53d4eadc040e052e9d0732bebe85e1c52"
    },
    "complete_reversible_text_patches": [
      {
        "label": "whole current geometry bytes",
        "before": "GEOMETRY_BYTES = 88422",
        "after": "GEOMETRY_BYTES = 88434",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
        "before": "complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
        "after": "complete-fixed-fejer-r726-dk-cache-world-geometry-v1",
        "occurrences": 1
      },
      {
        "label": "current schema actual-fixed-fejer-r725-dk-cache-report-binding-v1",
        "before": "actual-fixed-fejer-r725-dk-cache-report-binding-v1",
        "after": "actual-fixed-fejer-r726-dk-cache-report-binding-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency geometry_selector",
        "before": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
        "after": "4386ce195c9709e0bb204cd749b89429652a177bb497bbc2fcf2756564496253",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename geometry_selector",
        "before": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
        "after": "fullclosed_point_inequalities_v2_r726_curvature_cache.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency geometry",
        "before": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
        "after": "b46cd96f5bfe019137b1332750ab3f81b3c100895cff33187898ab0e1daaaa65",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename geometry",
        "before": "so3_fixed_fejer_r725_dk_cache_geometry.py",
        "after": "so3_fixed_fejer_r726_dk_cache_geometry.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "driver",
    "complete_parent": {
      "role": "driver",
      "name": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_r725_dk_cache_qp.py",
      "bytes": 99234,
      "sha256": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
      "complete_parent": {
        "role": "driver",
        "name": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
        "bytes": 99410,
        "sha256": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910",
        "git_blob_sha": "c0e24fb110b3f893bbd1fa1d52eb2457d78c6872"
      },
      "git_blob_sha": "a58a8ed42deb53dc87df487287e9abd3feb0deb3"
    },
    "complete_output": {
      "role": "driver",
      "name": "fullclosed_fixed_fejer_r726_dk_cache_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_r726_dk_cache_qp.py",
      "bytes": 99231,
      "sha256": "58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813",
      "git_blob_sha": "cbbfa6975d4e7254c29e33d0be518175354bcbee"
    },
    "complete_reversible_text_patches": [
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
        "before": "complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
        "after": "complete-fixed-fejer-r726-dk-cache-SO3-QP-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_reference",
        "before": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
        "after": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename seed_reference",
        "before": "fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
        "after": "fixed_fejer_R726_spherical_halfwave_meridian_reference.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency seed_mean",
        "before": "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917",
        "after": "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename seed_mean",
        "before": "supported_smooth_triangle_seed_mean_jets.py",
        "after": "fixed_fejer_R726_spherical_seed_mean_jets.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency meridian",
        "before": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "after": "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename meridian",
        "before": "fixed_fejer_r725_meridian_operator.py",
        "after": "fixed_fejer_r726_meridian_operator.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency new_moment_input",
        "before": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
        "after": "b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename new_moment_input",
        "before": "fixed_fejer_r725_literal_zero_moment_input.py",
        "after": "fixed_fejer_r726_literal_zero_moment_input.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency closure_values",
        "before": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "after": "6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename closure_values",
        "before": "fixed_fejer_r725_closure_values.py",
        "after": "fixed_fejer_r726_closure_values.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3",
        "before": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "after": "81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_J3",
        "before": "fixed_fejer_r725_analytic_stage_jacobian.py",
        "after": "fixed_fejer_r726_analytic_stage_jacobian.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_frame",
        "before": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
        "after": "56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_frame",
        "before": "fixed_fejer_r725_analytic_normal_frame.py",
        "after": "fixed_fejer_r726_analytic_normal_frame.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency frame_C1",
        "before": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "after": "2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename frame_C1",
        "before": "fixed_fejer_r725_normal_frame_c1.py",
        "after": "fixed_fejer_r726_normal_frame_c1.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency stage_matrices",
        "before": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "after": "4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename stage_matrices",
        "before": "fixed_fejer_r725_stage_matrices.py",
        "after": "fixed_fejer_r726_stage_matrices.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency adjacent_matrices",
        "before": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
        "after": "21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename adjacent_matrices",
        "before": "fixed_fejer_r725_adjacent_matrices.py",
        "after": "fixed_fejer_r726_adjacent_matrices.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency reference_calibration",
        "before": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
        "after": "1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename reference_calibration",
        "before": "fixed_fejer_r725_reference_calibration.py",
        "after": "fixed_fejer_r726_reference_calibration.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency detached_meridian_values",
        "before": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "after": "587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename detached_meridian_values",
        "before": "fixed_fejer_r725_detached_meridian_values.py",
        "after": "fixed_fejer_r726_detached_meridian_values.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency endpoint",
        "before": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
        "after": "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename endpoint",
        "before": "fixed_fejer_r725_normal_lift.py",
        "after": "fixed_fejer_r726_normal_lift.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency root_packets",
        "before": "71f80c72819f70d62ce2be70e075aa0ebda4130db3ebf7de7616d8a173ffeea1",
        "after": "9da481209cd48d82cb297b213650cc94c4f2148c097602f3495d57ba8f4508fc",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename root_packets",
        "before": "fixed_fejer_r725_root_packets.py",
        "after": "fixed_fejer_r726_root_packets.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency analytic_J3_binding",
        "before": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
        "after": "77c4a98d8736f10edcb33e640749033499366e41acbe8b962a0877d304235cfa",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_J3_binding",
        "before": "fixed_fejer_r725_source_binding.py",
        "after": "fixed_fejer_r726_source_binding.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency envelope_transfer",
        "before": "d9615e37f3fd0da916147674ff8f47be69cb6876ba98aa71e78eccd4d2fcc637",
        "after": "01e6f6a80b3556ec941d9f46431e7b5b6b6de7892865040c5f61a09117b5bc03",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename envelope_transfer",
        "before": "fixed_fejer_r725_memory_transfer.py",
        "after": "fixed_fejer_r726_memory_transfer.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency geometry_selector",
        "before": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
        "after": "4386ce195c9709e0bb204cd749b89429652a177bb497bbc2fcf2756564496253",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename geometry_selector",
        "before": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
        "after": "fullclosed_point_inequalities_v2_r726_curvature_cache.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency geometry",
        "before": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
        "after": "b46cd96f5bfe019137b1332750ab3f81b3c100895cff33187898ab0e1daaaa65",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename geometry",
        "before": "so3_fixed_fejer_r725_dk_cache_geometry.py",
        "after": "so3_fixed_fejer_r726_dk_cache_geometry.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency batched_geometry_binding",
        "before": "d951f9e5f8088fdbd58357e29bca71f8057e5133693112657c288f57346c2819",
        "after": "f24ff296f0a058d43a779c17d11916c4eec1fbcf26e337ede73f433b7db61422",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename batched_geometry_binding",
        "before": "fixed_fejer_r725_dk_cache_binding.py",
        "after": "fixed_fejer_r726_dk_cache_binding.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "launcher",
    "complete_parent": {
      "role": "launcher",
      "name": "launch_fixed_fejer_r725_dk_cache_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_r725_dk_cache_actions.py",
      "bytes": 22121,
      "sha256": "0673232700619911d4ab3c8fbe36c579bb52dc19f4e4e27eb84aa8e7ff7ff734",
      "complete_parent": {
        "role": "launcher",
        "name": "launch_fixed_fejer_halfwave_dk_cache_actions.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_halfwave_dk_cache_actions.py",
        "bytes": 22125,
        "sha256": "804bb61c3d26f4116dc486feb735afd73eb733a85399a7908525e40187ca2ffe",
        "git_blob_sha": "38498ca8650584030c38386d4efab9d17cdb404d"
      },
      "git_blob_sha": "5a4659259ea70a1e6b871336087e6cc3b5d6becd"
    },
    "complete_output": {
      "role": "launcher",
      "name": "launch_fixed_fejer_r726_dk_cache_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_r726_dk_cache_actions.py",
      "bytes": 22121,
      "sha256": "36a7a0a286c7a983cdec7bc1ed19299c1ec57901df7d0daea707e20891e412c1",
      "git_blob_sha": "c29c5701be654fe87f28f6ddb9e47cb2208c4396"
    },
    "complete_reversible_text_patches": [
      {
        "label": "complete dependency driver",
        "before": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
        "after": "58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename driver",
        "before": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
        "after": "fullclosed_fixed_fejer_r726_dk_cache_qp.py",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "reader",
    "complete_parent": {
      "role": "reader",
      "name": "read_fixed_fejer_r725_dk_cache_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_r725_dk_cache_report.py",
      "bytes": 92783,
      "sha256": "3f7c9861e8a6a836dd0e2021489212e10ca217b2f1238abd36a07a002f8fb2af",
      "complete_parent": {
        "role": "reader",
        "name": "read_fixed_fejer_halfwave_dk_cache_report.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_halfwave_dk_cache_report.py",
        "bytes": 99812,
        "sha256": "82a5c50f3006090398a054a1db12a607169bb1b074c25a00fae15ce447b704da",
        "git_blob_sha": "141407cc50df2d2043313fb168f779b0c018fc31"
      },
      "git_blob_sha": "1e56ac07a3a7b71676186b220e96d1bd696e6071"
    },
    "complete_output": {
      "role": "reader",
      "name": "read_fixed_fejer_r726_dk_cache_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_r726_dk_cache_report.py",
      "bytes": 92808,
      "sha256": "1aae949feefb2e6bfb457d755aaa6a16412d9b5333344fa351b4ab598287248c",
      "git_blob_sha": "49fddb8ce5d1536cf6b64ebbf1a582c9f868f62d"
    },
    "complete_reversible_text_patches": [
      {
        "label": "honest current pure metadata description",
        "before": "    \"\"\"The complete original pure reader, with actual R725 radial-plan binding.\"\"\"",
        "after": "    \"\"\"The complete pure reader with actual R726 mean and retained R725 radial-plan binding.\"\"\"",
        "occurrences": 1
      },
      {
        "label": "current source attribution _complete_r725_seed_reader_",
        "before": "_complete_r725_seed_reader_",
        "after": "_complete_r726_seed_reader_",
        "occurrences": 1
      },
      {
        "label": "current source attribution Bind the complete source of the R725 seed metadata reader",
        "before": "Bind the complete source of the R725 seed metadata reader",
        "after": "Bind the complete source of the R726 seed metadata reader",
        "occurrences": 1
      },
      {
        "label": "current source attribution The complete R725 seed metadata method changed",
        "before": "The complete R725 seed metadata method changed",
        "after": "The complete R726 seed metadata method changed",
        "occurrences": 1
      },
      {
        "label": "current source attribution The complete source changed during R725 seed metadata attribution",
        "before": "The complete source changed during R725 seed metadata attribution",
        "after": "The complete source changed during R726 seed metadata attribution",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "before": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
        "after": "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "before": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "before": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "before": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-r726-reference-literal-zero-endpoint-Q-input-v1",
        "occurrences": 1
      },
      {
        "label": "current schema fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "before": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-r726-reference-literal-two-bubble-endpoint-Q-v1",
        "occurrences": 1
      },
      {
        "label": "current schema complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
        "before": "complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
        "after": "complete-fixed-fejer-r726-dk-cache-SO3-QP-v1",
        "occurrences": 1
      },
      {
        "label": "current schema actual-fixed-fejer-r725-dk-cache-observed-SO3-readout-v1",
        "before": "actual-fixed-fejer-r725-dk-cache-observed-SO3-readout-v1",
        "after": "actual-fixed-fejer-r726-dk-cache-observed-SO3-readout-v1",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename new_moment_input",
        "before": "fixed_fejer_r725_literal_zero_moment_input.py",
        "after": "fixed_fejer_r726_literal_zero_moment_input.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename analytic_J3_binding",
        "before": "fixed_fejer_r725_source_binding.py",
        "after": "fixed_fejer_r726_source_binding.py",
        "occurrences": 1
      },
      {
        "label": "complete dependency driver",
        "before": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
        "after": "58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813",
        "occurrences": 1
      },
      {
        "label": "complete dependency basename driver",
        "before": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
        "after": "fullclosed_fixed_fejer_r726_dk_cache_qp.py",
        "occurrences": 1
      }
    ]
  }
];

const digest = b => crypto.createHash('sha256').update(b).digest('hex');
function whole(record, data, label) {
  if(data.byteLength!==record.bytes || digest(data)!==record.sha256)
    throw new Error(label+': complete source bytes differ');
  if(data.byteLength>=100000)throw new Error(label+': whole small-source limit');
}
function replaceCounted(value,before,after,count,label) {
  if(typeof before!=='string'||before.length===0||typeof after!=='string'||after.length===0)
    throw new Error('Empty complete literal anchor: '+label);
  const pieces=value.split(before);
  if(pieces.length-1!==count)throw new Error('Exact literal occurrence count changed: '+label);
  return pieces.join(after);
}
const argv={};
for(let i=2;i<process.argv.length;i+=2) {
  const key=process.argv[i],value=process.argv[i+1];
  if(!['--source-directory','--generated-directory'].includes(key)||!value||argv[key]!==undefined)
    throw new Error('Use --source-directory DIR --generated-directory DIR');
  argv[key]=value;
}
if(Object.keys(argv).length!==2)throw new Error('Both source directories are required');
const root=path.resolve(argv['--source-directory']),out=path.resolve(argv['--generated-directory']);
if(root===out)throw new Error('Generate into an independent directory');
fs.mkdirSync(out,{recursive:true});
function locate(record) {
  const relative=record.path.startsWith(TOPIC+'/')?record.path.slice(TOPIC.length+1):record.path;
  const candidates=[path.resolve(root,record.path),path.resolve(root,relative),path.resolve(root,record.name)];
  for(const candidate of [...new Set(candidates)])if(fs.existsSync(candidate))return candidate;
  throw new Error('Missing complete parent: '+record.path);
}
const generated=[];
for(const spec of SPEC) {
  const input=locate(spec.complete_parent),raw=fs.readFileSync(input);
  whole(spec.complete_parent,raw,'Parent '+spec.role);
  const original=raw.toString('utf8');
  if(!Buffer.from(original,'utf8').equals(raw))throw new Error('Parent UTF-8 was not lossless');
  let result=original;
  for(const patch of spec.complete_reversible_text_patches)
    result=replaceCounted(result,patch.before,patch.after,patch.occurrences,spec.role+': '+patch.label);
  const data=Buffer.from(result,'utf8');
  whole(spec.complete_output,data,'Output '+spec.role);
  let inverse=result;
  for(const patch of [...spec.complete_reversible_text_patches].reverse())
    inverse=replaceCounted(inverse,patch.after,patch.before,patch.occurrences,'inverse '+spec.role+': '+patch.label);
  if(inverse!==original)throw new Error('Complete inverse differed for '+spec.role);
  const destination=path.resolve(out,spec.complete_output.name);
  if(destination===input)throw new Error('Do not overwrite a complete parent');
  if(fs.existsSync(destination)) {
    if(!fs.readFileSync(destination).equals(data))throw new Error('Different existing generated output: '+destination);
  } else fs.writeFileSync(destination,data,{flag:'wx'});
  generated.push({role:spec.role,path:destination,complete_output:spec.complete_output,
    complete_parent:spec.complete_parent,text_patch_count:spec.complete_reversible_text_patches.length,
    complete_inverse_equal:true});
}
process.stdout.write(JSON.stringify({
  schema:'complete-R726-spherical-scientific-family-text-reproduction-v1',
  complete:true,scope:'whole source bytes only; not a numerical validation gate',
  outputs:generated,Python_import:false,AST:false,compile:false,fixture:false,
  scientific_field_root_or_J_evaluation:false,numerical_equivalence_or_speed_claimed:false,
  independent_seed_and_mean_reproducer:'reproduce_fixed_fejer_R726_spherical_seed_sources.mjs'
})+'\n');
