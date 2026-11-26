#!/usr/bin/env python3
"""Create exact metadata for one new fixed-eta0 correlated mean integral; no science."""
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PREFIX = '2026-11-26-R144-fixed-eta0-correlated-mean'
SOURCE = 'fourfold_codazzi_fixed_eta0_correlated_mean_retraction.py'
WORKER = 'fourfold_codazzi_fixed_eta0_correlated_mean_public_worker.py'
GENERATOR = 'make_fixed_eta0_correlated_mean_manifest.py'
CURRENT = [
  [
    "reviewed_rules",
    "notes/2026-11-20-reviewed-public-CI-rules.json"
  ],
  [
    "raw_parts_index",
    "notes/2026-11-14-R133-final-complete-moving-residual-parts.json"
  ],
  [
    "candidate_index",
    "data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json"
  ],
  [
    "object",
    "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"
  ],
  [
    "definition_arb",
    "scripts/fourfold_phase_beta_interval.py"
  ],
  [
    "definition_bulk",
    "scripts/fourfold_phase_beta_bulk_interval.py"
  ],
  [
    "definition_affine",
    "scripts/fourfold_phase_beta_affine.py"
  ],
  [
    "definition_graft",
    "scripts/fourfold_phase_natural_exterior_graft.py"
  ],
  [
    "definition_entry",
    "scripts/fourfold_phase_exterior_entry_jet.py"
  ],
  [
    "definition_full_target",
    "scripts/fourfold_codazzi_full_body_graft_target_jets.py"
  ],
  [
    "definition_compact_target",
    "scripts/fourfold_codazzi_reciprocal_compact_target_jets.py"
  ],
  [
    "definition_candidate_loader",
    "scripts/fourfold_codazzi_candidate_shards.py"
  ],
  [
    "definition_old_raw",
    "scripts/fourfold_codazzi_merge_complete_moving_residual.py"
  ],
  [
    "rotational_reference_proof",
    "results/R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md"
  ],
  [
    "reference_subtraction_proof",
    "results/R144-supplement-fixed-density-rotational-reference-subtraction.md"
  ],
  [
    "nonlinear_mean_proof",
    "results/R144-supplement-exact-nonlinear-mean-elimination-and-retraction.md"
  ],
  [
    "old_complete_forward_proof",
    "results/R144-supplement-actual-forward-mean-enclosure-and-unresolved-gates.md"
  ]
]
METADATA = json.loads(r'''{
  "kind": "R144_fixed_eta0_correlated_mean_inputs_v1",
  "repository": "Rogerhu12/math-research-public",
  "problem_id": "R144_fixed_eta0_correlated_rotational_mean_retraction_v1",
  "scientific_kind": "R144_fixed_eta0_correlated_rotational_mean_retraction_v1",
  "expected_current_input_count": 21,
  "historical_inputs": [
    {
      "role": "original_raw_part_0",
      "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-moving-residual-parts-part000.bin.gz",
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "bytes": 1910756,
      "git_blob_sha": "ec854e372d249bb90698a6ed6db8af7ca2132022",
      "sha256": "e1833d0aa945a6ff506f894c17b93bc267f98d37482fcfbbc5ebd48f98a06a5c"
    },
    {
      "role": "original_raw_part_1",
      "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-moving-residual-parts-part001.bin.gz",
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "bytes": 1947563,
      "git_blob_sha": "97e74ae8e99b2f0db8faf9843c4bb84b2e2a62dc",
      "sha256": "852c89558b7df5c6d8df93939f6012f394b207e426f2499dd0db58ae4ce49386"
    },
    {
      "role": "original_raw_part_2",
      "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-moving-residual-parts-part002.bin.gz",
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "bytes": 571365,
      "git_blob_sha": "6d71d1e7929968f75b3e6f0ab843f6a5ed1535b1",
      "sha256": "47535b9239be1e168921d8339515da3caabb7ae8275cc0ffc8b06437b33c1dbf"
    },
    {
      "bytes": 2738500,
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "git_blob_sha": "634c08e6d18ed7d16308881b378cc5a9420be3a4",
      "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part000.npz.gz",
      "role": "original_candidate_part_0",
      "sha256": "5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4"
    },
    {
      "bytes": 2738003,
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "git_blob_sha": "ed630e376a1e91b19e34ac8be8080161a15f6200",
      "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part001.npz.gz",
      "role": "original_candidate_part_1",
      "sha256": "3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"
    },
    {
      "bytes": 2738686,
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "git_blob_sha": "5cc4d26fb15282ec922057eead9d6728e2a2b0cc",
      "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part002.npz.gz",
      "role": "original_candidate_part_2",
      "sha256": "a317c6f491295d8e46aa5d4b3da84c1f26bd16d5fb65260f3d3459e1f9c6210e"
    },
    {
      "bytes": 2732843,
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "git_blob_sha": "7a4ce33c8adf353574c34085e2cd8713245f59d3",
      "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part003.npz.gz",
      "role": "original_candidate_part_3",
      "sha256": "7b67e5a4b11ae45476d1507e842ae23919ca44e4ed2d64bc81bdea78e0b4007c"
    },
    {
      "bytes": 1532492,
      "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
      "git_blob_sha": "7c9414280441e5831fa4507fab8707043511c57a",
      "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part004.npz.gz",
      "role": "original_candidate_part_4",
      "sha256": "314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c"
    },
    {
      "role": "original_affine_origin_inputs",
      "path": "topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz",
      "commit": "3731c70d223185aaafa76815924609747d175cf9",
      "bytes": 386775,
      "git_blob_sha": "ff0847846fee05f421b26449caa3caa35344df9f",
      "sha256": "0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b"
    },
    {
      "role": "original_affine_direction",
      "path": "topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz",
      "commit": "3731c70d223185aaafa76815924609747d175cf9",
      "bytes": 137851,
      "git_blob_sha": "064aba18dc55c1bdf618d13ec37db4f3dfa7664c",
      "sha256": "8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab"
    }
  ],
  "accepted_natives": {
    "raw": "6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1",
    "candidate": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    "source": "24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
  },
  "runtime": {
    "python": "3.12.14",
    "packages": {
      "python-flint": "0.9.0",
      "numpy": "2.3.5"
    }
  },
  "parameters": {
    "arithmetic_bits": 320,
    "exact_eta": "-7789843107295549/4611686018427387904",
    "exact_nu": "-2572625729470897/72057594037927936",
    "exact_alpha": "6890507429876859/9007199254740992",
    "intrinsic_parameter_half_width": "0",
    "exact_interval": [
      "0",
      "25/8"
    ],
    "original_closed_rows": 7296,
    "original_PPoly_pieces": 6144,
    "original_interfaces": 6143,
    "raw_nonmean_modes": 32,
    "Taylor_source_degree": 24,
    "primitive_nodes": 512,
    "angular_strip": "8/25",
    "radial_Cauchy_radius_to_halfwidth": "8",
    "maximum_new_local_bisection_depth": 18,
    "fixed_shapes": "original u and j=v/mean(v)",
    "initial_W": "0",
    "initial_Y": "1",
    "comparison_radius": "1/10000",
    "same_r_source": "2 beta a^2 (U/s^2+K V/m^2)",
    "same_r_D_recovery": "W+a^2 w(2s+w)/(s^2 m^2)",
    "full_signed_D_initial_bulk_atoms_retained": true,
    "physical_outer_Cmean_shift_retained": true
  },
  "allowed_scientific_fields": [
    "identity",
    "complete",
    "proved",
    "failure",
    "stage",
    "completed_common_cells",
    "expected_common_cells",
    "completed_mean_interfaces",
    "expected_mean_interfaces",
    "completed_subcells",
    "current_exact_right",
    "active_original_row",
    "interface_consumed_for_active_row",
    "current_candidate_piece",
    "complete_new_scalars",
    "continuation_state",
    "first_unresolved_positivity",
    "certified_negative_Y_witness",
    "certified_violation_witness",
    "strict_gates",
    "rematerialization",
    "scope",
    "private_trace",
    "seconds",
    "old_completed_scientific_targets_called",
    "old_mean_Green_targets_called",
    "old_residual_targets_called",
    "old_response_targets_called",
    "old_angular_solver_calls",
    "published_arrays"
  ],
  "allowed_new_scalar_fields": [
    "W_at_current_right",
    "forward_multiplier_at_current_right",
    "signed_mean_atoms_at_current_right",
    "v_difference_upper_on_positive_cells",
    "maximum_local_D_Cauchy_remainder",
    "initial_D",
    "propagated_initial_D",
    "Y_lower_over_completed_cells",
    "D_at_current_right",
    "Y_at_current_right",
    "n_at_current_right",
    "a_at_current_right",
    "s_at_current_right",
    "m_at_current_right",
    "signed_bulk_D_at_current_right",
    "mean_shift_at_current_right",
    "physical_Cmean_shift_at_current_right",
    "maximum_complete_primitive_tail"
  ],
  "required_complete_scalar_fields": [
    "W_at_current_right",
    "forward_multiplier_at_current_right",
    "signed_mean_atoms_at_current_right",
    "v_difference_upper_on_positive_cells",
    "maximum_local_D_Cauchy_remainder",
    "initial_D",
    "propagated_initial_D",
    "Y_lower_over_completed_cells",
    "D_at_current_right",
    "Y_at_current_right",
    "n_at_current_right",
    "a_at_current_right",
    "s_at_current_right",
    "m_at_current_right",
    "signed_bulk_D_at_current_right",
    "maximum_complete_primitive_tail"
  ],
  "zero_call_counters": [
    "old_completed_scientific_targets_called",
    "old_mean_Green_targets_called",
    "old_residual_targets_called",
    "old_response_targets_called",
    "old_angular_solver_calls",
    "published_arrays"
  ],
  "scope": {
    "mathematical_target_count": 1,
    "old_producer_calls": 0,
    "old_completed_targets_recomputed": 0,
    "old_7296_native_read_only": true,
    "new_high_precision_carrier_materialized_only_for_new_integral": true,
    "necessary_new_input_interval": [
      "0",
      "25/8"
    ],
    "all_original_metric_germs_compact_cuts_graft_and_raw_joins": true,
    "complete_false_and_unknown_outcomes_retained": true,
    "no_selected_delta_or_Qrepair_inheritance": true,
    "no_nonmean_BVP_or_inverse_or_topic_completion": true
  },
  "operation": {
    "child_timeout_seconds": 18000,
    "readme_pull_interval_seconds": 1800,
    "topic_maximum_bytes": 200000000,
    "reserve_bytes": 120000,
    "maximum_total_publication_bytes": 95000,
    "maximum_execution_bytes": 65000,
    "maximum_scientific_bytes": 28000,
    "output_base": "topics/visible-flex-exact-nearby/notes/fixed_eta0_mean_retraction_ci",
    "consumed_marker": "topics/visible-flex-exact-nearby/notes/fixed_eta0_mean_retraction_ci/R144_fixed_eta0_correlated_mean_v1-consumed.json",
    "automatic_scientific_retry": false,
    "no_artifacts": true,
    "no_Releases": true,
    "no_new_arrays": true,
    "accepted_subcell_continuation_state_saved": true,
    "publication": "whole small signed outcome or genuine accepted-subcell prefix, complete execution, parameters and hashes"
  }
}''')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    root, source_dir, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def spec(role, relative, preferred=None):
        path = Path(preferred) if preferred is not None else root/relative
        raw = path.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError('complete small current input required: '+str(path))
        raw.decode('utf-8')
        if relative.endswith('.py'):
            ast.parse(raw, filename=relative)
        return dict(role=role, path=relative, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw))

    def selected(name, relative):
        candidate = source_dir/name
        return candidate if candidate.exists() else root/relative

    files = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('correlated_mean_contract', relative, selected(contract, relative)))
    files.extend(spec(role, TOPIC+'/'+path) for role, path in CURRENT)
    if len(files) != METADATA['expected_current_input_count']:
        raise ValueError('complete current input closure')
    if len({x['role'] for x in files}) != len(files) or len({x['path'] for x in files}) != len(files):
        raise ValueError('unique pinned current inputs')
    by_role = {x['role']: x for x in files}
    if by_role['candidate_index']['sha256'] != METADATA['accepted_natives']['candidate']:
        raise ValueError('same complete original candidate index')
    if by_role['definition_old_raw']['sha256'] != METADATA['accepted_natives']['source']:
        raise ValueError('same old native defining source')
    if by_role['object']['sha256'] != '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848':
        raise ValueError('same exact affine object')
    doc = dict(METADATA, files=files)
    body = (json.dumps(doc, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                       allow_nan=False)+'\n').encode()
    destination = out/(PREFIX+'-inputs.json')
    if destination.exists():
        raise FileExistsError('preserve every generated exact manifest')
    destination.write_bytes(body)
    print(json.dumps(dict(path=str(destination), bytes=len(body), sha256=sha(body),
                          current_inputs=len(files), historical_inputs=len(doc['historical_inputs']))))


if __name__ == '__main__':
    main()
