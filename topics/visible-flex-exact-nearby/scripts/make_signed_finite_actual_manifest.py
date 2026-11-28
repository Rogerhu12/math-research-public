"""Metadata-only SC launch after whole actual P224/TC/RW/JC completion.

Missing or failed predecessors produce only a readiness record.  No numerical
manifest or workflow is made until all complete actual predecessor objects,
their executions, and their original definitions have passed full admission.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys, types
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
OWNER = TOPIC+'/scripts/fourfold_codazzi_signed_finite_actual_owner.py'
WORKER = TOPIC+'/scripts/fourfold_codazzi_signed_finite_actual_public_worker.py'
GENERATOR = TOPIC+'/scripts/make_signed_finite_actual_manifest.py'
ADMISSION = TOPIC+'/scripts/fourfold_codazzi_signed_finite_actual_inputs.py'
DEFAULT_MANIFEST = TOPIC+'/notes/2026-11-27-actual-signed-finite-inputs.json'
DEFAULT_WORKFLOW = '.github/workflows/fourfold-codazzi-actual-signed-finite-public.yml'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def load_bytes(raw, path, name):
    """Only metadata-only modules; no numerical producer main is called."""
    module = types.ModuleType(name)
    module.__file__ = str(path)
    exec(compile(ast.parse(raw, filename=str(path)), str(path), 'exec'), module.__dict__)
    return module


def workflow(manifest_path, workflow_path, digest, problem):
    return '''name: R149 actual complete signed96 PDE columns and gates
on:
  push:
    branches: [main]
    paths:
      - '@WORKFLOW@'
  workflow_dispatch:
permissions:
  contents: write
  actions: read
concurrency:
  group: @PROBLEM@
  cancel-in-progress: false
jobs:
  complete-actual-columns-and-two-whole-matrices:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 360
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the unchanged original carrier runtime
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
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_finite_actual_public_worker.py
            /@MANIFEST@
      - name: Trust only the explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the original exact-carrier and directed runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Whole actual predecessors, same carriers, and complete new SC gates
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_signed_finite_actual_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest @MANIFEST@
          --manifest-sha @SHA@
'''.replace('@WORKFLOW@', workflow_path).replace('@PROBLEM@', problem).replace(
        '@MANIFEST@', manifest_path).replace('@SHA@', digest).encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--tc-result-dir')
    parser.add_argument('--tc-manifest')
    parser.add_argument('--wpn-result-dir')
    parser.add_argument('--wpn-manifest')
    parser.add_argument('--jc-result-dir', default=TOPIC+'/notes/joint_compound_row_ci/run-45887337009-1')
    parser.add_argument('--jc-manifest', default=TOPIC+'/notes/2026-11-27-joint-compound-waist-row-inputs.json')
    parser.add_argument('--manifest-out', default=DEFAULT_MANIFEST)
    parser.add_argument('--workflow-out', default=DEFAULT_WORKFLOW)
    parser.add_argument('--route-out', type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    sys.dont_write_bytecode = True
    route = {'kind': 'actual_signed_finite_whole_input_readiness_v1', 'ready': False,
             'whole_actual_predecessors': [], 'reason': None,
             'numerical_imports_or_scientific_calls': 0,
             'numerical_manifest_created': False, 'workflow_created': False}

    def relative(path, topic=True):
        value = Path(path)
        if value.is_absolute():
            value = value.resolve().relative_to(root)
        name = value.as_posix()
        require(all(part not in ('', '.', '..') for part in name.split('/'))
                and (name.startswith(TOPIC+'/') if topic else name.startswith('.github/workflows/')),
                'one exact repository destination')
        return name

    def finish(reason):
        route['reason'] = reason
        require(not any(name in sys.modules for name in ('numpy', 'flint', 'scipy')),
                'readiness remains metadata only')
        raw = canonical(route)
        if args.route_out is not None:
            require(not args.route_out.exists(), 'new complete readiness snapshot only')
            args.route_out.parent.mkdir(parents=True, exist_ok=True)
            args.route_out.write_bytes(raw)
        print(raw.decode(), end='')

    paths = {}
    # A false or incomplete whole precursor never turns into placeholder data.
    for stage, result_name in (('TC', 'actual-trial-state.json'),
                               ('wpn', 'actual-physical-stage.json'),
                               ('JC', 'actual-joint-compound-waist-row-error.json')):
        directory = getattr(args, stage.lower()+'_result_dir')
        manifest_path = getattr(args, stage.lower()+'_manifest')
        if directory is None or manifest_path is None:
            finish(stage+'_whole_actual_result_and_manifest_not_supplied'); return
        directory, manifest_path = relative(directory), relative(manifest_path)
        role = 'TC_state' if stage == 'TC' else stage+'_actual'
        found = {role: directory+'/'+result_name, stage+'_execution': directory+'/execution.json',
                 stage+'_manifest': manifest_path}
        if not all((root/path).is_file() for path in found.values()):
            finish(stage+'_whole_actual_files_not_yet_present'); return
        actual = json.loads((root/found[role]).read_bytes())
        execution = json.loads((root/found[stage+'_execution']).read_bytes())
        route['whole_actual_predecessors'].append({
            'stage': stage, 'actual_path': found[role], 'complete': actual.get('complete'),
            'proved': actual.get('proved'), 'failure': actual.get('failure'),
            'completed_targets': actual.get('completed_targets'),
            'execution_complete': execution.get('complete')})
        if not (actual.get('complete') is True and actual.get('proved') is True
                and actual.get('failure') is None and execution.get('complete') is True
                and execution.get('failure') is None and execution.get('actual_child_returncode') == 0):
            finish(stage+'_whole_incomplete_failed_or_sufficient_gate_false'); return
        paths.update(found)
        if stage == 'TC':
            for name, filename in (('matrix', 'complete-signed-trial-matrices.json'),
                                   ('negative', 'complete-negative-trial-sources.json'),
                                   ('positive', 'complete-positive-trial-sources.json'),
                                   ('prefix', 'complete-radial-integration-prefix.json')):
                paths['TC_'+name] = directory+'/'+filename
        elif stage == 'wpn':
            for prefix in ('gate', 'ports'):
                for suffix in ('actual', 'execution', 'manifest'):
                    name = prefix+'_'+suffix
                    paths[name] = actual['whole_completed_inputs'][name]['file']['path']
    if not all((root/path).is_file() for path in paths.values()):
        finish('a_complete_TC_object_or_whole_positive_chain_file_is_missing'); return

    contents, specs = {}, {}
    def add(role, path, expected=None):
        path = relative(path)
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, 'one whole small actual input: '+role)
        raw.decode('utf-8')
        if path.endswith('.py'):
            ast.parse(raw, filename=path)
        spec = {'role': role, 'path': path, 'bytes': len(raw), 'sha256': sha(raw), 'git_blob_sha': blob(raw)}
        if expected is not None:
            require(all(spec[key] == expected[key] for key in ('path', 'bytes', 'sha256', 'git_blob_sha')),
                    'unchanged whole completed definition: '+role)
        require(role not in specs, 'unique whole actual role')
        specs[role], contents[role] = spec, raw
        return spec

    for role, path in paths.items():
        add(role, path)
    additions = {
        'science': OWNER, 'worker': WORKER, 'generator': GENERATOR, 'input_admission': ADMISSION,
        'carrier_restore': TOPIC+'/scripts/fourfold_codazzi_signed_finite_trial_carrier_restore.py',
        'joint_math': TOPIC+'/scripts/fourfold_codazzi_joint_signed_finite_trial_error_math.py',
        'joint_proof': TOPIC+'/results/R149-supplement-joint-signed-finite-matrix-error.md',
        'composition_proof': TOPIC+'/results/R149-supplement-joint-compound-waist-row-error.md',
        'execution_contract': TOPIC+'/notes/2026-11-27-actual-signed-finite-execution.md',
        'positive_metadata_reference': TOPIC+'/scripts/fourfold_codazzi_positive_inverse_negative_receivers_owner.py',
        'positive_port_math': TOPIC+'/scripts/fourfold_codazzi_completed_physical_gate_ports_math.py',
        'WX_execution': TOPIC+'/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json',
        'reviewed_rules': TOPIC+'/notes/2026-11-20-reviewed-public-CI-rules.json',
    }
    for role, path in additions.items():
        add(role, path)
    owner = load_bytes(contents['science'], root/OWNER, '_SC_metadata_owner')
    admission = load_bytes(contents['input_admission'], root/ADMISSION, '_SC_metadata_full_admission')
    tc_manifest = json.loads(contents['TC_manifest'])
    tc_specs = {item['path']: item for item in tc_manifest['files']}
    tc_execution = json.loads(contents['TC_execution'])
    tc_checkout = tc_execution['actual_scientific_checkout']
    require(len(tc_checkout) == 40 and all(x in '0123456789abcdef' for x in tc_checkout),
            'the actual completed TC checkout is immutable')
    tc_owner_path = tc_manifest['roles']['owner']
    tc_owner_spec = tc_specs[tc_owner_path]
    current = root/tc_owner_path
    tc_owner_raw = current.read_bytes() if current.is_file() else b''
    if sha(tc_owner_raw) != tc_owner_spec['sha256']:
        tc_owner_raw = subprocess.check_output(['git', 'show', tc_checkout+':'+tc_owner_path], cwd=root)
    require(len(tc_owner_raw) == tc_owner_spec['bytes'] and sha(tc_owner_raw) == tc_owner_spec['sha256']
            and blob(tc_owner_raw) == tc_owner_spec['git_blob_sha'],
            'the original complete TC metadata validator, not a changed successor source')
    tc_owner = load_bytes(tc_owner_raw, root/tc_owner_path, '_SC_original_TC_metadata')
    tc = admission.admit_complete_TC(contents, specs, tc_owner)
    reference = load_bytes(contents['positive_metadata_reference'], root/additions['positive_metadata_reference'], '_SC_positive_reference')
    family = tc['state']['input_identity']['same_selected_family']
    require(family['continuous_centre_definition_sha256'] == reference.CENTRE
            and family['continuous_response_definition_sha256'] == reference.DIRECTION
            and family['fixed_current_eta'] == 'eta_0'
            and tc_manifest['parameters']['root_interval'] == reference.ROOT_INTERVAL,
            'the same original positive and negative family and exact root')
    ports = load_bytes(contents['positive_port_math'], root/additions['positive_port_math'], '_SC_positive_port_definition')
    admission.admit_positive_chain(contents, specs, reference.FIXED_REFERENCE_IDENTITY, ports)
    jc_manifest = json.loads(contents['JC_manifest'])
    jc_source = next(item for item in jc_manifest['files'] if item['role'] == 'science')
    add('JC_definition_source', jc_source['path'], jc_source)
    jc_owner = load_bytes(contents['JC_definition_source'], root/jc_source['path'], '_SC_JC_original_metadata')
    admission.admit_JC(contents, specs, jc_owner, family,
                        tc_specs[tc_manifest['roles']['RW_manifest']]['sha256'])
    admission.admit_WX(contents['WX_execution'], specs['WX_execution'], tc_manifest['parameters']['root_interval'])
    review = json.loads(contents['reviewed_rules'])
    for path, expected in review['readme_sha256'].items():
        require(sha((root/path).read_bytes()) == expected, 'current whole README matches the explicit review')
    identity = sha(canonical({name: specs[name]['sha256'] for name in ('TC_state', 'TC_execution', 'ports_actual', 'wpn_actual', 'JC_actual')}))
    problem = 'R149_complete_actual_signed96_'+identity[:20]
    manifest = {
        'repository': owner.REPO, 'kind': owner.MANIFEST_KIND, 'scientific_kind': owner.KIND,
        'stage': owner.STAGE, 'problem_id': problem, 'parameters': owner.PARAMETERS,
        'runtime': owner.RUNTIME, 'target_order': owner.TARGETS,
        'files': sorted(specs.values(), key=lambda item: item['role']),
        'expected_current_input_count': len(specs), 'original_TC_checkout': tc_checkout,
        'original_TC_manifest_transitively_restored_whole': True,
        'same_original_TC_trial_and_matrix_carrier_hashes_required': True,
        'whole_actual_prerequisite_counts': {'positive': [58, 224, 32], 'TC': 3, 'RW': 96, 'JC': 7},
        'operation': {
            'topic_maximum_bytes': 200000000, 'reserve_bytes': 120000,
            'readme_pull_interval_seconds': 1800, 'automatic_scientific_retry': False,
            'child_timeout_seconds': 18600,
            'consumed_marker': TOPIC+'/notes/signed_finite_actual_ci/consumed-'+identity[:20]+'.json',
            'output_base': TOPIC+'/notes/signed_finite_actual_ci',
            'maximum_state_bytes': 45000, 'maximum_columns_bytes': owner.MAXIMUM_COLUMNS_BYTES,
            'maximum_matrix_bytes': 35000, 'maximum_execution_bytes': 65000,
            'maximum_total_publication_bytes': 290000,
        },
        'scope': {
            'complete_root96_passively_saved_from_same_single_column_error_call': True,
            'passive_root_record_additional_scientific_calls': 0,
            'whole_positive_chain_before_arithmetic': True, 'all_TC_targets_before_arithmetic': True,
            'whole_RW_and_actual_JC_used_without_old_target_replay': True,
            'both_physical_density_means_retained': True, 'true_target_orthonormality_only': True,
            'complete_signed96_entries_before_matrix_gate': True,
            'original_nodal_QR_recomputed': False, 'old_residual_norm_targets_recomputed': False,
            'necessary_exact_carrier_rematerialization_separately_counted': True,
            'full_mean_phase_nu_high_Schur_proved': False, 'topic_completion_proved': False,
        },
    }
    manifest_path, workflow_path = relative(args.manifest_out), relative(args.workflow_out, topic=False)
    require(not (root/manifest_path).exists() and not (root/workflow_path).exists(),
            'never overwrite a concrete actual target or a prior failure')
    raw = canonical(manifest)
    require(len(raw) < 100000, 'one whole small actual-input manifest')
    entry = workflow(manifest_path, workflow_path, sha(raw), problem)
    require(not any(name in sys.modules for name in ('numpy', 'flint', 'scipy')),
            'all whole admission is metadata only')
    for path, body in ((manifest_path, raw), (workflow_path, entry)):
        (root/path).parent.mkdir(parents=True, exist_ok=True)
        (root/path).write_bytes(body)
    route.update(ready=True, numerical_manifest_created=True, workflow_created=True,
                 manifest={'path': manifest_path, 'bytes': len(raw), 'sha256': sha(raw)},
                 workflow={'path': workflow_path, 'bytes': len(entry), 'sha256': sha(entry)})
    finish('all_whole_actual_predecessors_admitted_no_scientific_call')


if __name__ == '__main__':
    main()
