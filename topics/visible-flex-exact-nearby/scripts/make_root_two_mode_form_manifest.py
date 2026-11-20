#!/usr/bin/env python3
"""Build metadata for one complete root two-mode form; never run science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-20-R138-root-two-mode-form'
SOURCE = 'fourfold_codazzi_root_two_mode_form.py'
WORKER = 'fourfold_codazzi_root_two_mode_form_public_worker.py'
GENERATOR = 'make_root_two_mode_form_manifest.py'
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
    small.append(spec('two_mode_contract', contract_path, selected(contract_name, contract_path)))
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
        'old_geometry_targets_called', 'published_arrays', 'private_cache_representation',
        'whole_original_references', 'scope', 'current_frame_error_upper',
        'current_position_error_upper', 'seconds', 'complete_new_mean_functional',
        'maximum_new_ideal_frame_error_upper', 'maximum_new_ideal_position_error_upper',
        'complete_response_primitive_mean', 'complete_response_periodicity_check',
        'nonlocal_completed_cells', 'complete_affine_signed_form', 'complete_axis_q_ball',
        'complete_axis_s_ball', 'private_cache_sha256', 'private_response_prefix_sha256',
        'private_cache_bytes', 'complete_actual_signed_two_mode_matrix',
        'complete_actual_signed_determinant', 'determinant_strictly_negative',
        'negative_witness', 'strict_sign_uses_complete_saved_decimal_balls',
    ])
    manifest = dict(kind='R138_same_Qrepair_signed_root_two_mode_inputs_v1', repository=REPO,
        problem_id='R138_same_Qrepair_true_root_complete_signed_96_97_form_v1',
        scientific_kind='R138_same_Qrepair_true_root_complete_signed_96_97_form_v1',
        files=small, expected_current_input_count=len(small), historical_inputs=originals,
        accepted_natives=dict(germ=GERM, candidate=CANDIDATE),
        runtime=dict(python='3.12.14', packages={'python-flint': '0.9.0', 'numpy': '2.3.5'}),
        parameters=dict(arithmetic_bits=320, angular_cells=32768, physical_modes=[96,97],
            physical_frequencies=[384,388], complete_angular_interval='[0,2*pi]',
            original_low_modes=[1,96], original_high_modes='j>=97',
            normalized_sine_basis='sqrt(2)*sin(4j*phi)',
            complete_axis_ball_not_clipped=True, original_D_complete_saved_ball=True,
            actual_periodic_frame_C0_fee='11/10000000', actual_position_C0_fee='1/25000',
            actual_C1_C2_from_saved_X_defects=True, exact_signed_trigonometric_integrals=True,
            private_mid64_rad64_containment_at_every_write=True,
            complete_scalar_readback_before_sign=True),
        allowed_scientific_fields=allowed,
        scope=dict(new_target='three complete actual signed entries of the original root 96/97 form',
            mathematical_target_count=1, complete_mean_and_primitive_terms_retained=True,
            old_producer_calls=0, old_completed_targets_recomputed=0,
            W2C_context_constructed=False, candidate_definition_restoration_only=True,
            no_axis_mean_or_X_target_called=True, no_large_array_published=True,
            negative_direction_only_excludes_all_root_data_nonnegativity=True,
            actual_boundary_problem_singularity_proved=False, full_inverse_proved=False,
            final_topic_complete=False),
        operation=dict(child_timeout_seconds=5400, readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000, reserve_bytes=120000,
            maximum_total_publication_bytes=180000, maximum_execution_bytes=90000,
            maximum_scientific_bytes=80000,
            output_base=TOPIC+'/notes/root_two_mode_form_ci',
            consumed_marker=TOPIC+'/notes/root_two_mode_form_ci/R138_signed_root_96_97_v1-consumed.json',
            automatic_scientific_retry=False,
            publication='complete small signed form or unfinished prefix, run metadata and hashes only',
            no_artifacts=True, no_Releases=True, no_new_arrays=True))
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('one complete small manifest')
    filename = PREFIX+'-inputs.json'
    (out/filename).write_bytes(raw)
    workflow = '''name: R138 complete signed root 96 and 97 form

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-root-two-mode-form-public.yml

permissions:
  contents: write

concurrency:
  group: r138-root-two-mode-signed-v1
  cancel-in-progress: false

jobs:
  complete-root-two-mode:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_two_mode_form_public_worker.py
            topics/visible-flex-exact-nearby/notes/MANIFEST_NAME
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore original bytes and enclose the complete signed root form
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_two_mode_form_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/MANIFEST_NAME --manifest-sha MANIFEST_SHA
'''.replace('MANIFEST_NAME', filename).replace('MANIFEST_SHA', sha(raw))
    (out/'fourfold-codazzi-root-two-mode-form-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw), current_inputs=len(small),
        historical_inputs=len(originals), source_sha256=by_role['science']['sha256'],
        worker_sha256=by_role['worker']['sha256'], numerical_execution=False), sort_keys=True))


if __name__ == '__main__':
    main()
