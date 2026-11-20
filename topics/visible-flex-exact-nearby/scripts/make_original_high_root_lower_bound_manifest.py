#!/usr/bin/env python3
"""Build metadata for one complete original-high root bound; never run science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-20-R138-original-high-root-lower-bound'
SOURCE = 'fourfold_codazzi_original_high_root_lower_bound.py'
WORKER = 'fourfold_codazzi_original_high_root_lower_bound_public_worker.py'
GENERATOR = 'make_original_high_root_lower_bound_manifest.py'
GERM = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
DEFINITION = 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79'


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
        source = Path(preferred) if preferred is not None else root/relative
        raw = source.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError('one complete small text input: '+str(source))
        raw.decode('utf-8')
        if relative.endswith('.py'):
            ast.parse(raw, filename=relative)
        return dict(role=role, path=relative, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw))

    def selected(name, relative):
        p = source_dir/name
        return p if p.exists() else root/relative

    small = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        small.append(spec(role, relative, path))
    contract_name = PREFIX+'-contract.md'
    contract_path = TOPIC+'/notes/'+contract_name
    small.append(spec('original_high_contract', contract_path, selected(contract_name, contract_path)))
    current = [
        ('reviewed_rules', 'notes/2026-11-20-reviewed-public-CI-rules.json'),
        ('candidate_index', 'data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json'),
        ('definition_helper', 'scripts/fourfold_codazzi_root_axis_support.py'),
        ('actual_root_frame_transfer_proof', 'results/R138-supplement-actual-root-angular-comparison-and-mean-readout.md'),
        ('complete_root_angular_proof', 'results/R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md'),
        ('same_repaired_physical_object_proof', 'results/R138-supplement-actual-positive-support-for-repaired-physical-frame.md'),
        ('exact_continuous_repair_proof', 'results/R133-supplement-exact-continuous-repair-of-final-centre.md'),
        ('complete_actual_physical_defect_proof', 'results/R138-supplement-complete-physical-residual-multiplier-budget.md'),
        ('complete_axis_ball_and_source_proof', 'results/R138-supplement-root-source-elimination-and-concave-finite-gate.md'),
        ('same_fixed_point_proof', 'results/R138-supplement-exact-residual-transport-and-fixed-interior-point.md'),
        ('axis', 'notes/root_axis_support_ci/run-44730968113-1/axis-support-conclusion.json'),
        ('axis_execution', 'notes/root_axis_support_ci/run-44730968113-1/execution.json'),
        ('mean', 'notes/root_mean_angular_ci/run-44733403315-1/root-mean-conclusion.json'),
        ('mean_execution', 'notes/root_mean_angular_ci/run-44733403315-1/execution.json'),
        ('physical_budget', 'notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json'),
        ('physical_execution', 'notes/physical_energy_budget_ci/run-44737045152-1/execution.json'),
        ('two_mode', 'notes/root_two_mode_form_ci/run-44745192261-1/root-two-mode-conclusion.json'),
        ('two_mode_execution', 'notes/root_two_mode_form_ci/run-44745192261-1/execution.json'),
        ('original_high_principal_proof', 'results/R138-supplement-original-high-principal-and-signed-compact-bound.md'),
        ('relative_root_receiver_proof', 'results/R138-supplement-original-high-compression-and-relative-root-receivers.md'),
    ]
    small.extend(spec(role, TOPIC+'/'+relative) for role, relative in current)
    by_role = {r['role']: r for r in small}
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected:
            raise ValueError('README differs from the explicit existing rule review: '+path)
    expected = {
        'candidate_index': CANDIDATE, 'definition_helper': DEFINITION,
        'axis': 'b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92',
        'axis_execution': 'a8979dff609fd41e88be754e09e8fbb2a56528f101c729208e5e54a9ef1de73f',
        'mean': 'de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4',
        'mean_execution': '25d6e66fade5f838a33e62da0f502152115a34c5c572c662471b6c9acad38cb5',
        'physical_budget': '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec',
        'physical_execution': '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92',
        'two_mode': '95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2',
        'two_mode_execution': 'f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2',
        'original_high_principal_proof': 'be05ec41a0f5bc0af404aa0575ce942e2790dedc0608489b63e3c0553c4a3dee',
        'relative_root_receiver_proof': 'ec5b6d4d0c70089aac745c7c5a0014cfafce30754e179aaf811ecbc19762fe1b',
    }
    for role, expected_sha in expected.items():
        if by_role[role]['sha256'] != expected_sha:
            raise ValueError('same whole original input differs: '+role)

    # Restore the same six immutable original blobs; this is metadata only.
    old = json.loads((root/TOPIC/'notes/2026-11-20-R138-root-mean-angular-inputs.json').read_bytes())
    originals = old['historical_inputs']
    if (len(originals) != 6 or len({x['path'] for x in originals}) != 6
            or originals[-1]['role'] != 'original_root_germ'
            or originals[-1]['sha256'] != GERM):
        raise ValueError('same complete five candidate parts and root germ')

    allowed = sorted([
        'identity', 'complete', 'proved', 'failure', 'stage', 'completed_cells',
        'old_axis_targets_called', 'old_mean_targets_called', 'old_X_targets_called',
        'old_two_mode_matrix_entries_recomputed', 'old_ZP_propagations_called',
        'old_geometry_targets_called', 'published_arrays', 'whole_original_references',
        'scope', 'seconds', 'complete_new_scalar_bounds', 'complete_receiver_coefficients',
        'complete_high_lower_bound_terms', 'complete_actual_high_lower_bound',
        'high_lower_bound_positive', 'receiver_neumann_gate',
        'complete_nonhomogeneous_source_coefficients',
        'strict_gates_use_complete_saved_decimal_balls',
        'private_geometry_only_for_new_scalar_targets', 'old_signed_two_mode_scope_preserved',
    ])
    records = {
        'complete_new_scalar_bounds': sorted([
            'principal_a_second_upper', 'principal_a_minimum_lower',
            'A_qq_negative_upper', 'A_RR_negative_upper', 'A_TT_negative_upper',
            'A_Rq_absolute_upper', 'A_qT_absolute_upper', 'A_RT_absolute_upper',
            'k_0_upper', 'b_0_upper', 'c_0_upper', 'b_1_upper', 'b_2_upper',
            'c_1_upper', 'g_m_0_upper', 'G_0_upper', 'G_1_upper']),
        'complete_receiver_coefficients': sorted([
            'chi_0_upper', 'chi_1_upper', 'V_0_upper', 'V_1_upper', 'X_1_upper',
            'chi_q0_L2_upper', 'm_absolute_upper', 'rho_inverse_upper', 'kappa_upper']),
        'complete_high_lower_bound_terms': sorted([
            'Y_H_upper', 'E_H_upper', 'L_H_upper', 'V_H_upper', 'I_H_upper',
            'principal_error_upper', 'signed_local_error_upper', 'mean_rank_error_upper',
            'complete_primitive_error_upper']),
        'complete_nonhomogeneous_source_coefficients': sorted([
            'C_omega_L_upper', 'C_omega_H_upper', 'C_L_upper',
            'C_H_cross_upper', 'C_quad_upper']),
    }
    manifest = dict(kind='R138_same_Qrepair_original_high_root_lower_bound_inputs_v1', repository=REPO,
        problem_id='R138_same_Qrepair_original_high_root_lower_bound_v1',
        scientific_kind='R138_same_Qrepair_original_high_root_lower_bound_v1',
        files=small, expected_current_input_count=len(small), historical_inputs=originals,
        accepted_natives=dict(germ=GERM, candidate=CANDIDATE),
        runtime=dict(python='3.12.14', packages={'python-flint': '0.9.0', 'numpy': '2.3.5'}),
        parameters=dict(arithmetic_bits=320, angular_cells=32768,
            complete_angular_interval='[0,2*pi]', original_low_modes=[1,96],
            original_high_modes='j>=97', minimum_high_frequency=388,
            scalar_normalization='full-circle normalized L2',
            complete_axis_ball_not_clipped=True, original_D_complete_saved_ball=True,
            actual_periodic_frame_C0_fee='11/10000000', actual_position_C0_fee='1/25000',
            actual_C1_C2_from_saved_X_defects=True,
            principal_comparison_factor='2^(1/6)/32*388^(-4/3)',
            local_square_negative_parts_only=True,
            complete_mean_and_two_environment_primitives=True,
            mean_bprime_one_known_coefficient_derivative=True,
            primitive_near_far_cutoff=194, primitive_environment_norm=1,
            complete_scalar_readback_before_strict_gates=True),
        allowed_scientific_fields=allowed,
        expected_new_scalar_records=records,
        expected_complete_new_scalar_record_count=41,
        scope=dict(new_target='complete original j>=97 high compression lower bound and receiver scalar coefficients',
            mathematical_target_count=1, complete_mean_and_primitive_terms_retained=True,
            old_producer_calls=0, old_completed_targets_recomputed=0,
            old_signed_two_mode_matrix_entries_recomputed=0,
            W2C_context_constructed=False, candidate_definition_restoration_only=True,
            no_axis_mean_X_or_ZP_target_called=True, no_large_array_published=True,
            previous_negative_root_direction_preserved=True,
            actual_boundary_problem_singularity_proved=False, full_inverse_proved=False,
            final_topic_complete=False),
        operation=dict(child_timeout_seconds=5400, readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000, reserve_bytes=120000,
            maximum_total_publication_bytes=180000, maximum_execution_bytes=90000,
            maximum_scientific_bytes=80000,
            output_base=TOPIC+'/notes/original_high_root_lower_bound_ci',
            consumed_marker=TOPIC+'/notes/original_high_root_lower_bound_ci/R138_original_high_root_lower_bound_v1-consumed.json',
            automatic_scientific_retry=False,
            publication='complete small new scalar bounds or unfinished prefix, run metadata and hashes only',
            no_artifacts=True, no_Releases=True, no_new_arrays=True))
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('one complete small manifest')
    filename = PREFIX+'-inputs.json'
    (out/filename).write_bytes(raw)
    workflow = '''name: R138 complete original high root lower bound

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-original-high-root-lower-bound-public.yml

permissions:
  contents: write

concurrency:
  group: r138-original-high-root-lower-bound-v1
  cancel-in-progress: false

jobs:
  complete-original-high-root:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 120
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_high_root_lower_bound_public_worker.py
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore original bytes and enclose the complete original high block
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_high_root_lower_bound_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
'''.replace('MANIFEST_NAME', filename).replace('MANIFEST_SHA', sha(raw))
    (out/'fourfold-codazzi-original-high-root-lower-bound-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw), current_inputs=len(small),
        historical_inputs=len(originals), source_sha256=by_role['science']['sha256'],
        worker_sha256=by_role['worker']['sha256'], numerical_execution=False), sort_keys=True))


if __name__ == '__main__':
    main()
