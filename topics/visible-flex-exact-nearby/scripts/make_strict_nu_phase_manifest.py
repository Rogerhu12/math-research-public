"""Metadata-only entry for the first signed nonlocal phase pairing."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
OWNER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_owner.py'
WORKER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-phase-complete-inputs.json'
WORKFLOW = '.github/workflows/visible-exact-strict-nu-phase-complete.yml'
WORKFLOW_TEMPLATE = '''name: R147 first strict parameter nonlocal phase
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-strict-nu-phase-complete.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-strict-nu-nonlocal-phase-20261127
  cancel-in-progress: false
jobs:
  first-whole-signed-phase-functional:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 135
    env:
      OMP_NUM_THREADS: '1'
      OPENBLAS_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_support_localized_nu_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-phase-complete-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the same original carrier runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Pair the true strict parameter with the complete nonlocal phase row
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-strict-nu-phase-complete-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def load(root,path,name):
    raw = (root/path).read_bytes();require(0 < len(raw) < 100000,'whole small source')
    ast.parse(raw.decode(),filename=path)
    spec = importlib.util.spec_from_file_location(name,root/path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build(root,tree_metadata=None):
    require(not any(x in sys.modules for x in ('numpy','flint','scipy')),'metadata-only generation')
    sys.dont_write_bytecode = True
    owner = load(root,OWNER,'_PHI_metadata_owner');worker = load(root,WORKER,'_PHI_metadata_worker')
    math = load(root,owner.MATH,'_PHI_pure_new_functional')
    carrier = load(root,owner.CARRIERS,'_PHI_pure_input_definitions')
    load(root,owner.RESTORE,'_PHI_original_input_restore_definitions')
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER
        and list(math.OUTPUT_ORDER) == owner.TARGETS and math.SIGNED_INDICES == owner.SIGNED_INDICES,
        'the complete concrete new phase entry')
    compile(worker.build_adapter(root),WORKER,'exec')
    declared = owner.gather(root,tree_metadata);files,history,roles = (declared[x] for x in ('files','historical_inputs','roles'))
    raws = {x['path']:(root/x['path']).read_bytes() for x in files}
    paths = {x['path']:root/x['path'] for x in files}
    small = [x for x in history if x['role'].startswith('NP_RW_')]
    require(len(small) == 4,'all original small whole conjugacy/phase definitions')
    for item in small:
        raw = subprocess.run(['git','show',item['commit']+':'+item['path']],cwd=root,
            check=True,capture_output=True).stdout
        require(len(raw) == item['bytes'] and owner.sha(raw) == item['sha256'],'whole original saved native')
        raws[item['path']] = raw
    admitted = owner.admit(declared,raws,paths)
    require(admitted['NP']['complete'] is admitted['SB']['complete'] is True,
        'the actual whole completed strict particular and short receiver')
    require(history == [dict(x,role='NP_'+x['role']) for x in admitted['NP_manifest']['historical_inputs']],
        'all original NP descriptors unchanged except role namespace')
    expanded = carrier.expand(declared['phase_input_plan'])
    require(len(expanded) == 264,'all necessary original phase/scalar natives and both whole error inputs')
    review = owner.parse(raws[roles['reviewed_rules']])
    require(review['repository'] == owner.REPO
        and review['new_unread_rules_must_still_be_reported_and_applied'] is True
        and set(review['readme_sha256']) == {'README.md',TOPIC+'/README.md'},'both explicitly reviewed READMEs')
    for path,digest in review['readme_sha256'].items():
        require(owner.sha((root/path).read_bytes()) == digest,'already reviewed README unchanged: '+path)
    require(review['large_data_policy']['maximum_topic_bytes'] == 200000000
        and review['large_data_policy']['original_completed_mathematics_must_not_be_recomputed'] is True
        and not any(x in sys.modules for x in ('numpy','flint','scipy')),'no local scientific target evaluation')
    manifest = {'repository':owner.REPO,'kind':owner.MANIFEST_KIND,'scientific_kind':owner.KIND,'stage':owner.STAGE,
        'problem_id':'R147_complete_strict_nu_nonlocal_phase_20261127','parameters':owner.PARAMETERS,
        'runtime':owner.RUNTIME,'target_order':owner.TARGETS,'complete_record_counts':[6],
        'allowed_scientific_fields':owner.SCI_FIELDS,'files':files,'expected_current_input_count':len(files),
        'historical_inputs':history,'roles':roles,'phase_input_plan':declared['phase_input_plan'],
        'operation':{'topic_maximum_bytes':200000000,'reserve_bytes':120000,'readme_pull_interval_seconds':1800,
            'automatic_scientific_retry':False,'consumed_marker':TOPIC+'/notes/strict_nu_phase_ci/consumed-target.json',
            'output_base':TOPIC+'/notes/strict_nu_phase_ci','maximum_scientific_bytes':26000,
            'maximum_execution_bytes':65000,'maximum_total_publication_bytes':95000,'child_timeout_seconds':6120},
        'scope':{'same_original_selected_Q_delta':True,'same_complete_four_original_NP_array_hashes':True,
            'same_whole_original131_phase_and_scalar_germs':True,'same_full_original1572_two_leg_polynomial_hashes':True,
            'same_full_original131_two_leg_endpoints':True,'original_phase_constant_retained':True,
            'first_new_signed_nonlocal_phase_pairing':True,'true_squared_label_weight_and_full_mean':True,
            'full_selected_background_direct_metric_and_infinite_response_error_paid':True,
            'every_accepted_new_germ_prefix_preserved':True,'new_trial_selected':False,
            'old_residual_norm_pairing_or_KAM_targets_recomputed':False,'full_regular_boundary_response_proved':False,
            'physical_height_or_rigid_ports_proved':False,'true_phase_Schur_or_topic_completion_proved':False}}
    raw = owner.canonical(manifest);require(len(raw) < 100000,'whole small complete immutable manifest')
    return raw,WORKFLOW_TEMPLATE.replace('@MANIFEST_SHA@',owner.sha(raw)).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',default='.',type=Path)
    parser.add_argument('--tree-metadata',type=Path)
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    raw,workflow = build(root,args.tree_metadata)
    for relative,content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({'ready':True,'manifest':MANIFEST,'manifest_bytes':len(raw),
        'manifest_sha256':hashlib.sha256(raw).hexdigest(),'workflow':WORKFLOW,
        'local_scientific_targets_evaluated':0},sort_keys=True))


if __name__ == '__main__':main()
