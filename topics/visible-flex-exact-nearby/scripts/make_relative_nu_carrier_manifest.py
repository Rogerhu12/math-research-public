"""Metadata-only entry for complete relative strict-parameter carriers."""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path

TOPIC='topics/visible-flex-exact-nearby'
OWNER=TOPIC+'/scripts/fourfold_codazzi_relative_nu_carrier_owner.py'
WORKER=TOPIC+'/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py'
MANIFEST=TOPIC+'/notes/2026-11-27-relative-nu-carriers-inputs.json'
WORKFLOW='.github/workflows/visible-exact-relative-nu-carriers.yml'


def require(ok,message):
    if not ok:raise ValueError(message)


def load(root,path,name):
    raw=(root/path).read_bytes();require(0<len(raw)<100000,'whole small source')
    ast.parse(raw.decode(),filename=path)
    spec=importlib.util.spec_from_file_location(name,root/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def workflow(files,manifest_sha):
    bootstrap=[TOPIC+'/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py',
        TOPIC+'/scripts/fourfold_codazzi_support_localized_nu_public_worker.py',
        TOPIC+'/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py',
        TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py']
    paths=sorted({'README.md',TOPIC+'/README.md',MANIFEST,*bootstrap,*[x['path'] for x in files]})
    lines=['name: R147 complete relative strict parameter carriers','on:','  push:','    branches: [main]',
        '    paths:',"      - '"+WORKFLOW+"'",'  workflow_dispatch:','permissions:','  contents: write',
        'concurrency:','  group: visible-exact-relative-nu-carriers-20261127','  cancel-in-progress: false',
        'jobs:','  first-complete-relative18-carrier:',
        "    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1",
        '    runs-on: ubuntu-24.04','    timeout-minutes: 350','    env:',
        "      OMP_NUM_THREADS: '1'","      OPENBLAS_NUM_THREADS: '1'","      MKL_NUM_THREADS: '1'",
        "      NUMEXPR_NUM_THREADS: '1'","      BLIS_NUM_THREADS: '1'","      VECLIB_MAXIMUM_THREADS: '1'",
        '    steps:','      - uses: actions/checkout@v4','        with:','          ref: main',
        '          fetch-depth: 0','          filter: blob:none','          persist-credentials: false',
        '          sparse-checkout-cone-mode: false','          sparse-checkout: |']
    lines+=['            /'+path for path in paths]
    lines+=['      - uses: actions/setup-python@v5','        with:',"          python-version: '3.12.14'",
        '      - name: Install the same original NP directed runtime',
        '        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0',
        '      - name: Compute all relative profiles and complete signed parameter means','        env:',
        '          GITHUB_TOKEN: '+'$'+'{{ secrets.GITHUB_TOKEN }}','        run: >-',
        '          python '+WORKER,'          --repo "$GITHUB_WORKSPACE"','          --manifest '+MANIFEST,
        '          --manifest-sha '+manifest_sha]
    return ('\n'.join(lines)+'\n').encode()


def build(root):
    require(not any(x in sys.modules for x in ('numpy','flint','scipy')),'metadata-only generation')
    sys.dont_write_bytecode=True
    owner=load(root,OWNER,'_RHI_metadata_owner')
    worker=load(root,WORKER,'_RHI_metadata_worker')
    math=load(root,owner.MATH,'_RHI_pure_relative_algebra')
    load(root,owner.RESTORE,'_RHI_original_carrier_restore_definitions')
    require(owner.SOURCE==OWNER and owner.WORKER==WORKER and list(math.TARGETS)==owner.TARGETS
        and list(math.ZERO_MEANS)==owner.PARAMETERS['proved_reflection_zero_mean_indices'],
        'whole concrete new relative entry')
    compile(worker.build_adapter(root),WORKER,'exec')
    declared=owner.gather(root);files,history,roles=(declared[x] for x in ('files','historical_inputs','roles'))
    raws={x['path']:(root/x['path']).read_bytes() for x in files}
    paths={x['path']:root/x['path'] for x in files}
    small=[x for x in history if x['role'].startswith('NP_RW_')]
    require(len(small)==4,'four full original small reflected conjugacy natives')
    for item in small:
        raw=subprocess.run(['git','show',item['commit']+':'+item['path']],cwd=root,
            check=True,capture_output=True).stdout
        require(len(raw)==item['bytes'] and owner.sha(raw)==item['sha256'],'whole original native')
        raws[item['path']]=raw
    admitted=owner.admit(declared,raws,paths)
    require(admitted['NP']['complete'] is admitted['SB']['complete'] is True
        and history==[dict(x,role='NP_'+x['role']) for x in admitted['NP_manifest']['historical_inputs']],
        'the actual complete NP/SB same-selected results and unchanged native closure')
    review=owner.parse(raws[roles['reviewed_rules']])
    require(review['repository']==owner.REPO and review['new_unread_rules_must_still_be_reported_and_applied'] is True
        and set(review['readme_sha256'])=={'README.md',TOPIC+'/README.md'},'both reviewed README contracts')
    for path,digest in review['readme_sha256'].items():
        require(owner.sha((root/path).read_bytes())==digest,'already reviewed README unchanged: '+path)
    require(review['large_data_policy']['maximum_topic_bytes']==200000000
        and review['large_data_policy']['original_completed_mathematics_must_not_be_recomputed'] is True
        and not any(x in sys.modules for x in ('numpy','flint','scipy')),'no local scientific target')
    manifest={'repository':owner.REPO,'kind':owner.MANIFEST_KIND,'scientific_kind':owner.KIND,'stage':owner.STAGE,
        'problem_id':'R147_complete_relative_strict_nu_carriers_20261127','parameters':owner.PARAMETERS,
        'runtime':owner.RUNTIME,'target_order':owner.TARGETS,'complete_record_counts':[4],
        'allowed_scientific_fields':owner.SCI_FIELDS,'files':files,'expected_current_input_count':len(files),
        'historical_inputs':history,'roles':roles,
        'operation':{'topic_maximum_bytes':200000000,'reserve_bytes':120000,'readme_pull_interval_seconds':1800,
            'automatic_scientific_retry':False,'consumed_marker':TOPIC+'/notes/relative_nu_carriers_ci/consumed-target.json',
            'output_base':TOPIC+'/notes/relative_nu_carriers_ci','maximum_scientific_bytes':32000,
            'maximum_execution_bytes':75000,'maximum_total_publication_bytes':120000,'child_timeout_seconds':18600},
        'scope':{'same_original_selected_Q_delta':True,'same_four_whole_original_NP_array_hashes':True,
            'all_original2472_cells_and_true_seams_retained':True,'full18_component_relative_profile_retained':True,
            'whole_new_private_carrier_hash_and_complete_angular_profile_errors':True,
            'complete_direct_metric_state_mean_and_numerical_impulse_terms':True,
            'three_exact_reflection_zero_means_and_all_six_signed_outputs':True,
            'full_infinite_PDE_response_error_paid':True,
            'actual_world_anchors_rigid_ports_and_physical_coordinate_term_independent':True,
            'every_accepted_new_cell_prefix_preserved':True,'old_scientific_targets_recomputed':False,
            'new_NP_trial_selected':False,'full_regular_response_proved':False,
            'actual_world_height_or_true_Schur_or_topic_completion_proved':False}}
    raw=owner.canonical(manifest);require(len(raw)<100000,'whole small immutable input manifest')
    return raw,workflow(files,owner.sha(raw))


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',default='.',type=Path)
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args();root=args.repo.resolve();sys.dont_write_bytecode=True
    raw,yaml=build(root)
    for relative,content in ((MANIFEST,raw),(WORKFLOW,yaml)):
        path=root/relative
        if args.check_only:require(path.read_bytes()==content,'exact current complete metadata entry: '+relative)
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
    print(json.dumps({'ready':True,'manifest':MANIFEST,'manifest_bytes':len(raw),
        'manifest_sha256':hashlib.sha256(raw).hexdigest(),'workflow':WORKFLOW,
        'local_scientific_targets_evaluated':0},sort_keys=True))


if __name__=='__main__':main()
