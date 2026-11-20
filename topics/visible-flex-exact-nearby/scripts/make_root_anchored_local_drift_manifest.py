#!/usr/bin/env python3
"""Create metadata for two new root-anchored local drift bounds; no science execution."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-20-R138-root-anchored-local-drift'
SOURCE = 'fourfold_codazzi_root_anchored_local_drift.py'
WORKER = 'fourfold_codazzi_root_anchored_local_drift_public_worker.py'
GENERATOR = 'make_root_anchored_local_drift_manifest.py'
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
    files.append(spec('local_drift_contract', relative, selected(contract, relative)))
    current = [
        ('reviewed_rules', 'notes/2026-11-20-reviewed-public-CI-rules.json'),
        ('positive_parts_index', 'notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json'),
        ('original_restoration_manifest', 'notes/2026-11-20-R138-physical-energy-budget-inputs.json'),
        ('physical', 'notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json'),
        ('physical_execution', 'notes/physical_energy_budget_ci/run-44737045152-1/execution.json'),
        ('root_anchored_drift_proof', 'results/R138-supplement-root-anchored-local-drift-and-capacity.md'),
        ('weighted_energy_capacity_proof', 'results/R138-supplement-localized-eta-balanced-energy-and-root-capacity.md'),
        ('relative_root_receiver_proof', 'results/R138-supplement-original-high-compression-and-relative-root-receivers.md'),
        ('actual_residual_budget_proof', 'results/R138-supplement-complete-physical-residual-multiplier-budget.md'),
        ('continuous_repair_proof', 'results/R133-supplement-exact-continuous-repair-of-final-centre.md'),
        ('whole_positive_curvature_proof', 'results/R133-supplement-whole-positive-reference-floor-and-cached-producer.md'),
    ]
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in current)
    by_role = {item['role']: item for item in files}
    expected = {
        'science': '9c468c51dfe5b2e6e4406ea39621bcf8a1d74b51afc4c740a00039e8a436b915',
        'local_drift_contract': 'c5507a548047c637bf398b9a71fd557f9b2350540b901cc56c6a16c37965c2bc',
        'physical': '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec',
        'physical_execution': '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92',
        'root_anchored_drift_proof': 'a5c4e29d22aadf634aff822637f4560d2383175f1aae3a0d116bcb7605b8dbef',
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
    prior = json.loads((root/by_role['original_restoration_manifest']['path']).read_bytes())
    originals = [r for r in prior['historical_inputs']
                 if r['role'].startswith('original_positive_part_') or r['role']=='original_root_germ']
    if (len(originals) != 5 or len({r['path'] for r in originals}) != 5
            or [r['role'] for r in originals] !=
               ['original_positive_part_'+str(i) for i in range(4)]+['original_root_germ']
            or originals[-1]['sha256'] != GERM):
        raise ValueError('exact original positive4 plus germ1 materialization')
    zeros = ('old_scientific_targets_called old_geometry_ODE_calls old_candidate_targets_called '
             'old_X_targets_recomputed new_flow_ODE_calls new_capacity_ODE_calls published_arrays').split()
    fields = ('identity complete proved failure stage expected_common_cells completed_common_cells '
              'completed_positive_rows current_exact_right integral_prefix complete_drift_integral '
              'complete_local_Gamma saved_record_count whole_original_references scope strict_comparisons seconds').split()+zeros
    if len(fields) != len(set(fields)) or len(fields) != 24:
        raise ValueError('exact two-scalar scientific schema')
    manifest = dict(kind='R138_true_root_anchored_local_drift_inputs_v1', repository=REPO,
        problem_id='R138_true_root_anchored_local_drift_budget_v1',
        scientific_kind='R138_true_root_anchored_local_drift_budget_v1',
        files=files, expected_current_input_count=len(files), historical_inputs=originals,
        accepted_natives=dict(positive=POSITIVE, germ=GERM, candidate=CANDIDATE),
        runtime=dict(python='3.12.14', packages={'python-flint': '0.9.0'}),
        parameters=dict(arithmetic_bits=320, fixed_local_length='1/100',
            exact_flow_initial_condition='psi(r_star,xi)=xi', fixed_close_to_one_threshold='101/100',
            exact_true_root_interval=['1191984371497/5000000000000','2383968743003/10000000000000'],
            full_pair_repair_A0='1/250000000000000000',
            independent_mean_retained=True, original_parent_enclosures_not_shrunk=True,
            complete_saved_upper_before_exponential_and_comparison=True),
        allowed_scientific_fields=sorted(fields), zero_call_counters=zeros,
        expected_complete_new_scalar_record_count=2,
        scope=dict(new_target='complete new local drift integral and its exponential on the true root layer',
            mathematical_target_count=2, old_producer_calls=0, old_completed_targets_recomputed=0,
            no_new_flow_or_capacity_ODE_or_finite_Gram=True, original_mean_and_interfaces_retained=True,
            false_comparisons_keep_complete_new_bounds=True,
            no_BVP_singularity_or_inverse_or_topic_completion=True),
        operation=dict(child_timeout_seconds=1800, readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000, reserve_bytes=120000,
            maximum_total_publication_bytes=100000, maximum_execution_bytes=60000,
            maximum_scientific_bytes=30000,
            output_base=TOPIC+'/notes/root_anchored_local_drift_ci',
            consumed_marker=TOPIC+'/notes/root_anchored_local_drift_ci/R138_root_anchored_local_drift_v1-consumed.json',
            automatic_scientific_retry=False, no_artifacts=True, no_Releases=True, no_new_arrays=True,
            publication='complete two-scalar outcome or genuine prefix, execution, parameters and hashes'))
    raw = (json.dumps(manifest,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = """name: R138 root anchored local drift bounds

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-root-anchored-local-drift-public.yml

permissions:
  contents: write

concurrency:
  group: r138-root-anchored-local-drift-v1
  cancel-in-progress: false

jobs:
  complete-local-drift:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_anchored_local_drift_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-20-R138-root-anchored-local-drift-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Restore five old inputs and evaluate two complete local drift bounds
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_anchored_local_drift_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-20-R138-root-anchored-local-drift-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow=workflow.replace('__MANIFEST_SHA__',sha(raw))
    (out/'fourfold-codazzi-root-anchored-local-drift-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw),manifest_sha256=sha(raw),
        expected_current_input_count=len(files),historical_inputs=len(originals),
        complete_scientific_fields=len(fields),new_target_count=2),sort_keys=True))


if __name__ == '__main__':
    main()
