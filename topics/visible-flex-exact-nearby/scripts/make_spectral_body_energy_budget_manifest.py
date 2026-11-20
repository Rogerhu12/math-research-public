#!/usr/bin/env python3
"""Metadata for complete SG spectral/body bounds; never executes science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-20-R138-spectral-body-energy-budget'
SOURCE = 'fourfold_codazzi_spectral_body_energy_budget.py'
WORKER = 'fourfold_codazzi_spectral_body_energy_budget_public_worker.py'
GENERATOR = 'make_spectral_body_energy_budget_manifest.py'
POSITIVE = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
GERM = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
SCIENCE_KIND = 'R138_complete_complementary_Gram_spectral_body_budget_v1'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--source-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    root,source_dir,out = args.repo.resolve(),args.source_dir.resolve(),args.out.resolve()
    out.mkdir(parents=True,exist_ok=True)

    def spec(role,relative,preferred=None):
        path = Path(preferred) if preferred is not None else root/relative
        raw = path.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError('complete small current input required: '+str(path))
        raw.decode('utf-8')
        if relative.endswith('.py'):
            ast.parse(raw,filename=relative)
        return dict(role=role,path=relative,bytes=len(raw),sha256=sha(raw),git_blob_sha=blob(raw))

    def selected(name,relative):
        path = source_dir/name
        return path if path.exists() else root/relative

    files = []
    for role,name in (('worker',WORKER),('science',SOURCE),('metadata_generator',GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name,relative)
        files.append(spec(role,relative,path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('spectral_body_contract',relative,selected(contract,relative)))
    current = [
        ('reviewed_rules','notes/2026-11-20-reviewed-public-CI-rules.json'),
        ('positive_parts_index','notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json'),
        ('original_restoration_manifest','notes/2026-11-20-R138-physical-energy-budget-inputs.json'),
        ('physical','notes/physical_energy_budget_ci/run-44737045152-1/physical-energy-conclusion.json'),
        ('physical_execution','notes/physical_energy_budget_ci/run-44737045152-1/execution.json'),
        ('composed','notes/composed_physical_energy_budget_ci/run-44740320925-1/composed-physical-energy-conclusion.json'),
        ('composed_execution','notes/composed_physical_energy_budget_ci/run-44740320925-1/execution.json'),
        ('body_budget','notes/capped_Hhalf_saved_budget_ci/run-44745355257-1/capped-Hhalf-body-budget.json'),
        ('body_execution','notes/capped_Hhalf_saved_budget_ci/run-44745355257-1/execution.json'),
        ('root_screen','notes/radial_weight_root_budget_screen_ci/run-44758362539-1/radial-weight-root-budget-screen.json'),
        ('screen_execution','notes/radial_weight_root_budget_screen_ci/run-44758362539-1/execution.json'),
        ('spectral_body_proof','results/R138-supplement-complementary-Gram-spectral-body-energy.md'),
        ('root_anchor_necessary_proof','results/R138-supplement-root-anchored-spectral-budget-necessary-screen.md'),
        ('root_anchored_drift_proof','results/R138-supplement-root-anchored-local-drift-and-capacity.md'),
        ('weighted_energy_capacity_proof','results/R138-supplement-localized-eta-balanced-energy-and-root-capacity.md'),
        ('capped_body_energy_proof','results/R138-supplement-capped-curvature-Hhalf-Grushin-and-root-budget.md'),
        ('actual_residual_budget_proof','results/R138-supplement-complete-physical-residual-multiplier-budget.md'),
        ('composed_Hessian_budget_proof','results/R138-supplement-composed-physical-Hessian-and-smoothing-budget.md'),
        ('actual_radial_screen_proof','results/R138-supplement-actual-radial-weight-root-budget-screen.md'),
        ('fixed_point_support_proof','results/R138-supplement-exact-residual-transport-and-fixed-interior-point.md'),
        ('continuous_repair_proof','results/R133-supplement-exact-continuous-repair-of-final-centre.md'),
        ('whole_positive_curvature_proof','results/R133-supplement-whole-positive-reference-floor-and-cached-producer.md'),
    ]
    for role,relative in current:
        target = TOPIC+'/'+relative
        path = selected(Path(relative).name,target) if relative.startswith('results/') else root/target
        files.append(spec(role,target,path))
    by_role = {record['role']:record for record in files}
    expected = {
        'science':'0ff56334fc9993a95442c08dc1a8c03e720cb5bc15e5e6595c7810eaf7fd1364',
        'spectral_body_contract':'badef522fb23b7e20cedce425ba0fd558caf6c4da8f759ca45c5352e11180af2',
        'physical':'1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec',
        'physical_execution':'999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92',
        'composed':'19b489ce0b8b85d4223ea334f7e2397188755d42605bf7613d2023ac69cb2cf3',
        'composed_execution':'2e4cea611a229dbf894bae1fb2478ebc2219f9c0282a84cae1abd32ceb54f084',
        'body_budget':'5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492',
        'body_execution':'9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f',
        'root_screen':'e1b27ffa5759b9b55bc785ef17d362a67f1d370d5ae26e68b422922d9a0229d8',
        'screen_execution':'ba15b1060c40e965b27cc325c7696a35202dbf54c83817dbfb508750acdf8f1c',
        'spectral_body_proof':'1d98d83fec3634db49e88ad8cbd3fcca1e6f2a28efaa24504332220c6388f6a0',
        'root_anchor_necessary_proof':'af42b4f244da9dd0141f752a9f8c02bf2bc2120ee16d293fe4c3668ccd3128c2',
        'root_anchored_drift_proof':'a5c4e29d22aadf634aff822637f4560d2383175f1aae3a0d116bcb7605b8dbef',
    }
    for role,value in expected.items():
        if by_role[role]['sha256'] != value:
            raise ValueError('complete original or final new input identity: '+role)
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path,expected_sha in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected_sha:
            raise ValueError('unread rule change: '+path)
    parts = json.loads((root/by_role['positive_parts_index']['path']).read_bytes())
    if parts['original_sha256'] != POSITIVE or len(parts['parts']) != 4:
        raise ValueError('whole original positive parts index')
    prior = json.loads((root/by_role['original_restoration_manifest']['path']).read_bytes())
    originals = [record for record in prior['historical_inputs']
                 if record['role'].startswith('original_positive_part_')
                 or record['role'] == 'original_root_germ']
    if (len(originals) != 5 or len({record['path'] for record in originals}) != 5
        or [record['role'] for record in originals] !=
              ['original_positive_part_'+str(i) for i in range(4)]+['original_root_germ']
        or originals[-1]['sha256'] != GERM):
        raise ValueError('exact original positive4 plus germ1 materialization')
    zeros = ('old_scientific_targets_called old_CE_targets_recomputed old_geometry_ODE_calls '
             'old_residual_targets_recomputed old_Gamma_and_root_trace_targets_recomputed '
             'old_wB_aBB_targets_recomputed old_RS_targets_recomputed '
             'new_drift_or_capacity_ODE_calls published_arrays').split()
    fields = ('identity complete proved failure stage expected_closed_cells completed_closed_cells '
              'current_exact_right spectral_max_prefix new_records saved_record_count '
              'whole_original_references reused_complete_scalar_records '
              'body_only_sufficient_comparison root_anchor_necessary_screen '
              'conditional_root_allowance scope seconds').split()+zeros
    if len(fields) != len(set(fields)) or len(fields) != 27:
        raise ValueError('exact four-upper/conditional-lower scientific schema')
    upper_names = ['C_spectral_upper','wE_spectral_upper','aEE_spectral_upper','aEB_spectral_upper']
    lower_name = 'root_allowance_spectral_lower'
    manifest = dict(kind='R138_complete_spectral_body_energy_budget_inputs_v1',repository=REPO,
        problem_id=SCIENCE_KIND,scientific_kind=SCIENCE_KIND,
        files=files,expected_current_input_count=len(files),historical_inputs=originals,
        accepted_natives=dict(positive=POSITIVE,germ=GERM,candidate=CANDIDATE),
        runtime=dict(python='3.12.14',packages={'python-flint':'0.9.0'}),
        parameters=dict(arithmetic_bits=320,complete_original_cells=4651,
            exact_true_root_interval=['1191984371497/5000000000000','2383968743003/10000000000000'],
            exact_regular_right='25/8',full_pair_repair_A0='1/250000000000000000',
            same_fixed_point='(0,0,1/2)',same_support_lower='2/5',
            actual_spectral_domain='[r_star,25/8] x full original moving circle',
            body_drift_anchor='psi(25/8)=identity',intended_root_receiver='true-root-anchored RA flow',
            old_CE_wB_aBB_Gamma_root_trace_read_only=True,
            original_mean_and_all_interfaces_retained=True,
            exact_necessary_thresholds={'C_spectral_upper':'24','wE_spectral_upper':'45/2',
                                        'aEE_spectral_upper':'102/125'},
            necessity_not_sufficiency=True,conditional_allowance_requires_all_body_gates=True,
            complete_saved_scalar_before_every_downstream_use=True),
        allowed_scientific_fields=sorted(fields),zero_call_counters=zeros,
        required_new_upper_record_names=upper_names,conditional_new_lower_record_name=lower_name,
        allowed_complete_new_scalar_record_counts=[4,5],
        scope=dict(new_target='complete SG spectral maximum and its changed body-energy coefficients',
            unconditional_upper_targets=4,conditional_lower_targets=1,
            old_producer_calls=0,old_completed_targets_recomputed=0,
            no_new_geometry_or_drift_or_capacity_ODE_or_array=True,
            all4651_spectral_cells_required_before_old_CE_intersection=True,
            complete_false_necessary_or_body_gates_are_preserved=True,
            original_Gamma_root_receiver_exclusion_not_reopened=True,
            no_BVP_singularity_or_inverse_or_topic_completion=True),
        operation=dict(child_timeout_seconds=1800,readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000,reserve_bytes=160000,
            maximum_total_publication_bytes=140000,maximum_execution_bytes=70000,
            maximum_scientific_bytes=60000,
            output_base=TOPIC+'/notes/spectral_body_energy_budget_ci',
            consumed_marker=TOPIC+'/notes/spectral_body_energy_budget_ci/R138_spectral_body_energy_v1-consumed.json',
            automatic_scientific_retry=False,no_artifacts=True,no_Releases=True,no_new_arrays=True,
            publication='complete four-upper/conditional-lower outcome or genuine prefix, execution and receipts'))
    raw = (json.dumps(manifest,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = """name: R138 complete spectral body energy budget

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-spectral-body-energy-budget-public.yml

permissions:
  contents: write

concurrency:
  group: r138-spectral-body-energy-budget-v1
  cancel-in-progress: false

jobs:
  complete-spectral-body-budget:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_spectral_body_energy_budget_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-20-R138-spectral-body-energy-budget-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Restore five inputs and evaluate complete spectral body bounds
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_spectral_body_energy_budget_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-20-R138-spectral-body-energy-budget-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace('__MANIFEST_SHA__',sha(raw))
    (out/'fourfold-codazzi-spectral-body-energy-budget-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw),manifest_sha256=sha(raw),
        expected_current_input_count=len(files),historical_inputs=len(originals),
        complete_scientific_fields=len(fields),unconditional_upper_targets=4,
        conditional_lower_targets=1),sort_keys=True))


if __name__ == '__main__':
    main()
