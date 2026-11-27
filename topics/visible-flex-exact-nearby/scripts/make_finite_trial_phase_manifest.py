"""Metadata-only first entry for the complete phase row on original96 trials."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
OWNER = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_owner.py'
WORKER = TOPIC+'/scripts/fourfold_codazzi_finite_trial_phase_public_worker.py'
MANIFEST = TOPIC+'/notes/2026-11-27-finite-trial-phase-complete-inputs.json'
WORKFLOW = '.github/workflows/visible-exact-finite-trial-phase-complete.yml'
CONTAINER = 'python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7'
BOOTSTRAP = [TOPIC+'/scripts/fourfold_codazzi_'+name+'_public_worker.py' for name in
             ('negative_nu_waist','support_localized_nu','strict_nu_particular','strict_nu_phase')]
WORKFLOW_TEMPLATE = '''name: R149 original96 complete candidate phase row
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/visible-exact-finite-trial-phase-complete.yml'
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original96-complete-phase-20261127
  cancel-in-progress: false
jobs:
  first-complete-original96-phase-row:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: @CONTAINER@
    timeout-minutes: 350
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the same original immutable Python container
        run: |
          apt-get update -qq
          apt-get install -y --no-install-recommends git ca-certificates
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
@SPARSE_PATHS@
      - name: Trust the explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the original TC and phase directed runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Pair every original finite trial with the complete nonlocal phase row
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_finite_trial_phase_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-finite-trial-phase-complete-inputs.json
          --manifest-sha @MANIFEST_SHA@
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(root, path, name):
    raw = (root/path).read_bytes()
    require(0 < len(raw) < 100000, 'whole small source')
    ast.parse(raw.decode(), filename=path)
    spec = importlib.util.spec_from_file_location(name, root/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root, tree_metadata, complete_cover):
    require(not any(x in sys.modules for x in ('numpy','flint','scipy')),
            'only metadata is evaluated locally')
    sys.dont_write_bytecode = True
    owner = load(root, OWNER, '_P96_metadata_owner')
    worker = load(root, WORKER, '_P96_metadata_worker')
    math = load(root, owner.MATH, '_P96_new_math_definitions')
    carrier = load(root, owner.CARRIERS, '_P96_complete_input_definitions')
    load(root, owner.RESTORE, '_P96_original_carrier_restore_definitions')
    require(owner.SOURCE == OWNER and owner.WORKER == WORKER
            and list(math.OUTPUT_ORDER) == owner.TARGETS,
            'all complete new target definitions agree')
    compile(worker.build_adapter(root), WORKER, 'exec')
    declared = owner.gather(root, tree_metadata, complete_cover)
    files, history, roles = (declared[x] for x in ('files','historical_inputs','roles'))
    raws = {x['path']:(root/x['path']).read_bytes() for x in files}
    paths = {x['path']:root/x['path'] for x in files}
    small = [x for x in history if x['role'].startswith('NP_RW_')]
    require(len(small) == 4, 'all whole original phase/conjugacy definition objects')
    for item in small:
        raw = subprocess.run(['git','show',item['commit']+':'+item['path']],cwd=root,
                             check=True,capture_output=True).stdout
        require(len(raw) == item['bytes'] and owner.sha(raw) == item['sha256'],
                'one whole original already-completed native')
        raws[item['path']] = raw
    admitted = owner.admit(declared, raws, paths)
    require(admitted['original_TC_partial_cells'] == 992
            and history == [dict(x,role='NP_'+x['role']) for x in admitted['NP_manifest']['historical_inputs']],
            'the unchanged original input closure and the true unfinished TC status')
    original, unused = carrier.original(root/owner.OLD_PHASE_CARRIERS)
    expanded = carrier.expand(declared['phase_input_plan'], original)
    require(len(expanded) == 340, 'all169 original phase and scalar germs plus both error natives')
    review = owner.parse(raws[roles['reviewed_rules']])
    require(review['repository'] == owner.REPO
            and review['new_unread_rules_must_still_be_reported_and_applied'] is True
            and set(review['readme_sha256']) == {'README.md',TOPIC+'/README.md'},
            'both explicitly reviewed README definitions')
    for path, digest in review['readme_sha256'].items():
        require(owner.sha((root/path).read_bytes()) == digest, 'reviewed README unchanged: '+path)
    require(review['large_data_policy']['maximum_topic_bytes'] == 200000000
            and review['large_data_policy']['original_completed_mathematics_must_not_be_recomputed'] is True
            and not any(x in sys.modules for x in ('numpy','flint','scipy')),
            'no old or new numerical target has run locally')
    manifest = {
        'repository':owner.REPO,'kind':owner.MANIFEST_KIND,'scientific_kind':owner.KIND,'stage':owner.STAGE,
        'problem_id':'R149_complete_original96_finite_trial_phase_20261127',
        'parameters':owner.PARAMETERS,'runtime':owner.RUNTIME,
        'target_order':owner.TARGETS,'complete_record_counts':[6],
        'allowed_scientific_fields':owner.SCI_FIELDS,
        'files':files,'expected_current_input_count':len(files),'historical_inputs':history,
        'roles':roles,'phase_input_plan':declared['phase_input_plan'],
        'operation':{'topic_maximum_bytes':200000000,'reserve_bytes':120000,
            'readme_pull_interval_seconds':1800,'automatic_scientific_retry':False,
            'consumed_marker':TOPIC+'/notes/finite_trial_phase_ci/consumed-target.json',
            'output_base':TOPIC+'/notes/finite_trial_phase_ci',
            'maximum_scientific_bytes':97000,'maximum_execution_bytes':80000,
            'maximum_total_publication_bytes':185000,'child_timeout_seconds':18600},
        'scope':{'same_original_selected_Q_delta':True,
            'all_four_complete_original_TC_arrays_and_original_factory':True,
            'all169_original_phase_and_scalar_germs':True,'all3095_two_leg_polynomial_hashes':True,
            'same_full_original169_two_leg_endpoints':True,'true_root_sliver_separately_paid':True,
            'complete_adjoint_row_before_exact_degree96_pairing':True,
            'eight_exact_radial_moments_for_all96_columns':True,
            'complete_original_phase_mean_and_both_independent_means_retained':True,
            'complete_selected_label_and_background_change_paid':True,
            'whole_signed96_and_exact_dyadic_centres_saved_separately':True,
            'joint_radius_includes_all_final_ball_radii':True,
            'every_accepted_complete_germ_prefix_preserved':True,
            'necessary_original_TC_factory_rematerialization_count':1,
            'unused_Z14_restoration_count':0,'original_nodal_QR_count':0,
            'old_residual_norm_pairing_matrix_or_KAM_targets_recomputed':False,
            'new_trial_selected':False,'original_TC_negative_result_complete':False,
            'true_PDE_corrected_columns_proved':False,'full_phase_Schur_or_topic_completion_proved':False},
    }
    raw = owner.canonical(manifest)
    require(len(raw) < 100000, 'one entire small immutable manifest')
    sparse = sorted({'README.md',TOPIC+'/README.md',MANIFEST,*BOOTSTRAP,*(x['path'] for x in files)})
    require(all((root/x).is_file() for x in sparse if x != MANIFEST),
            'every current input and worker bootstrap is present in the sparse checkout')
    workflow = WORKFLOW_TEMPLATE.replace('@CONTAINER@',CONTAINER)
    workflow = workflow.replace('@MANIFEST_SHA@',owner.sha(raw))
    workflow = workflow.replace('@SPARSE_PATHS@','\n'.join('            /'+x for x in sparse))
    return raw, workflow.encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',default='.',type=Path)
    parser.add_argument('--tree-metadata',required=True,type=Path)
    parser.add_argument('--complete-cover',required=True,type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    raw, workflow = build(root,args.tree_metadata,args.complete_cover)
    for relative, content in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(content)
    print(json.dumps({'ready':True,'manifest':MANIFEST,'manifest_bytes':len(raw),
        'manifest_sha256':hashlib.sha256(raw).hexdigest(),'workflow':WORKFLOW,
        'local_scientific_targets_evaluated':0},sort_keys=True))


if __name__ == '__main__':
    main()
