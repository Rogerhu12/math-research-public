#!/usr/bin/env python3
"""Create metadata for one new radial-weight root screen; no science execution."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-20-R138-radial-weight-root-budget-screen'
SOURCE = 'fourfold_codazzi_radial_weight_root_budget_screen.py'
WORKER = 'fourfold_codazzi_radial_weight_root_budget_screen_public_worker.py'
GENERATOR = 'make_radial_weight_root_budget_screen_manifest.py'
POSITIVE = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
GERM = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'


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
        p = source_dir/name
        return p if p.exists() else root/relative

    files = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('root_screen_contract', relative, selected(contract, relative)))
    current = [
        ('reviewed_rules', 'notes/2026-11-20-reviewed-public-CI-rules.json'),
        ('definition_helper', 'scripts/fourfold_codazzi_root_axis_support.py'),
        ('positive_parts_index', 'notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json'),
        ('candidate_index', 'data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json'),
        ('original_axis_restoration_manifest', 'notes/2026-11-20-R138-root-axis-support-inputs.json'),
        ('high', 'notes/original_high_root_lower_bound_ci/run-44750653724-1/original-high-root-lower-bound.json'),
        ('high_execution', 'notes/original_high_root_lower_bound_ci/run-44750653724-1/execution.json'),
        ('two_mode', 'notes/root_two_mode_form_ci/run-44745192261-1/root-two-mode-conclusion.json'),
        ('two_mode_execution', 'notes/root_two_mode_form_ci/run-44745192261-1/execution.json'),
        ('physical', 'notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json'),
        ('physical_execution', 'notes/physical_energy_budget_ci/run-44737045152-1/execution.json'),
        ('body_budget', 'notes/capped_Hhalf_saved_budget_ci/run-44745355257-1/capped-Hhalf-body-budget.json'),
        ('body_execution', 'notes/capped_Hhalf_saved_budget_ci/run-44745355257-1/execution.json'),
        ('root_screen_proof', 'results/R138-supplement-radial-weight-independent-root-budget-screen.md'),
        ('weighted_energy_capacity_proof', 'results/R138-supplement-localized-eta-balanced-energy-and-root-capacity.md'),
        ('relative_root_receiver_proof', 'results/R138-supplement-original-high-compression-and-relative-root-receivers.md'),
        ('actual_original_high_proof', 'results/R138-supplement-actual-original-high-root-lower-bound.md'),
        ('actual_signed_two_mode_proof', 'results/R138-supplement-actual-negative-original-root-96-97-form.md'),
        ('actual_GB_proof', 'results/R138-supplement-actual-capped-Hhalf-body-absorption-and-root-allowance.md'),
        ('actual_residual_budget_proof', 'results/R138-supplement-complete-physical-residual-multiplier-budget.md'),
        ('fixed_interior_point_proof', 'results/R138-supplement-exact-residual-transport-and-fixed-interior-point.md'),
        ('continuous_repair_proof', 'results/R133-supplement-exact-continuous-repair-of-final-centre.md'),
        ('whole_positive_curvature_proof', 'results/R133-supplement-whole-positive-reference-floor-and-cached-producer.md'),
    ]
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in current)
    by_role = {item['role']: item for item in files}
    expected = {
        'science': 'c411610ffc855e748c3e3d76ab880c0c0ae1503db753bde38b6f27fb3be8c102',
        'root_screen_contract': 'aeb4f0ed2432680cc450ecaa0410cdaef1d555eae401ae5cc573667523a581a6',
        'definition_helper': 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79',
        'candidate_index': CANDIDATE,
        'high': 'f3f97be683009e9c8ae461c25dfd17d782a61ea6feaf9b8b7967b3e28a9e835d',
        'high_execution': 'e753dd0ea848302ccbe41dc90a3cd8ab1a1a211985d7a7d3691d7ab6384a7687',
        'two_mode': '95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2',
        'two_mode_execution': 'f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2',
        'physical': '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec',
        'physical_execution': '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92',
        'body_budget': '5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492',
        'body_execution': '9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f',
        'root_screen_proof': 'f0255a6ae1dfda9c88da44d7002944175669605c23debbc0baef6449d446d77c',
    }
    for role, value in expected.items():
        if by_role[role]['sha256'] != value:
            raise ValueError('complete original or final new input identity: '+role)
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected_sha in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected_sha:
            raise ValueError('unread rule change: '+path)
    parts = json.loads((root/by_role['positive_parts_index']['path']).read_bytes())
    if parts['original_sha256'] != POSITIVE or len(parts['parts']) != 4:
        raise ValueError('whole original positive index')
    prior = json.loads((root/by_role['original_axis_restoration_manifest']['path']).read_bytes())
    originals = prior['historical_inputs']
    if (len(originals) != 10 or len({r['path'] for r in originals}) != 10
            or [r['role'] for r in originals] !=
               ['original_positive_part_'+str(i) for i in range(4)]
               + ['original_candidate_part_'+str(i) for i in range(5)] + ['original_root_germ']
            or originals[-1]['sha256'] != GERM):
        raise ValueError('same complete original ten-blob materialization')
    zeros = ('old_scientific_targets_called old_axis_targets_called old_mean_targets_called '
             'old_high_41_targets_recomputed old_signed_matrix_entries_recomputed '
             'old_GB_X_targets_recomputed old_geometry_ODE_calls new_capacity_ODE_calls published_arrays').split()
    fields = ('identity complete proved failure stage expected_common_cells completed_common_cells '
              'expected_subcells completed_subcells completed_positive_rows integral_prefix '
              'complete_test_integral current_exact_right whole_original_references scope strict_gates seconds').split()+zeros
    if len(fields) != len(set(fields)) or len(fields) != 26:
        raise ValueError('exact scalar scientific schema')
    manifest = dict(kind='R138_radial_weight_root_budget_screen_inputs_v1', repository=REPO,
        problem_id='R138_radial_weight_independent_root_budget_screen_v1',
        scientific_kind='R138_radial_weight_independent_root_budget_screen_v1',
        files=files, expected_current_input_count=len(files), historical_inputs=originals,
        accepted_natives=dict(positive=POSITIVE, germ=GERM, candidate=CANDIDATE),
        runtime=dict(python='3.12.14', packages={'python-flint': '0.9.0', 'numpy': '2.3.5'}),
        parameters=dict(arithmetic_bits=320, fixed_test_length='1/100',
            subdivisions_per_original_cell=32, reflection_axes=['0','pi/4'],
            original_low_modes=[1,96], original_high_modes='j>=97',
            exact_true_root_interval=['1191984371497/5000000000000','2383968743003/10000000000000'],
            full_repair_A0='1/250000000000000000', support_vector_norm_upper='222/125',
            analytic_root_L2_upper='26/25', analytic_root_derivative_L2_upper='385',
            independent_mean_retained=True, original_parent_enclosures_not_shrunk=True,
            original_Gamma_threshold='225', all_scalar_Jacobian_threshold='160',
            original_selected_GB_budget_retained=True, complete_saved_upper_before_comparison=True),
        allowed_scientific_fields=sorted(fields), zero_call_counters=zeros,
        expected_complete_new_scalar_record_count=1,
        scope=dict(new_target='one whole positive short-root integral for radial-weight independent necessary screen',
            mathematical_target_count=1, old_producer_calls=0, old_completed_targets_recomputed=0,
            no_new_capacity_ODE_or_finite_Gram=True, original_mean_and_interfaces_retained=True,
            false_comparisons_are_complete_inconclusive_screen=True,
            no_BVP_singularity_or_inverse_or_topic_completion=True),
        operation=dict(child_timeout_seconds=1800, readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000, reserve_bytes=120000,
            maximum_total_publication_bytes=170000, maximum_execution_bytes=90000,
            maximum_scientific_bytes=70000,
            output_base=TOPIC+'/notes/radial_weight_root_budget_screen_ci',
            consumed_marker=TOPIC+'/notes/radial_weight_root_budget_screen_ci/R138_radial_weight_root_budget_screen_v1-consumed.json',
            automatic_scientific_retry=False, no_artifacts=True, no_Releases=True, no_new_arrays=True,
            publication='complete small scalar outcome or genuine prefix, execution, parameters and hashes'))
    raw = (json.dumps(manifest,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = """name: R138 radial weight independent root budget screen

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-radial-weight-root-budget-screen-public.yml

permissions:
  contents: write

concurrency:
  group: r138-radial-weight-root-budget-screen-v1
  cancel-in-progress: false

jobs:
  complete-short-root-integral:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 60
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_radial_weight_root_budget_screen_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-20-R138-radial-weight-root-budget-screen-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore old inputs and evaluate one complete new short-root integral
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_radial_weight_root_budget_screen_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-20-R138-radial-weight-root-budget-screen-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow=workflow.replace('__MANIFEST_SHA__',sha(raw))
    (out/'fourfold-codazzi-radial-weight-root-budget-screen-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw),manifest_sha256=sha(raw),
        expected_current_input_count=len(files),historical_inputs=len(originals),
        complete_scientific_fields=len(fields),new_target_count=1),sort_keys=True))


if __name__ == '__main__':
    main()
