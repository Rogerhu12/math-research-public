"""Metadata-only explicit PHI continuation after run45913335399 started no child."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
WORKER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_resume_worker.py'
GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_resume_manifest.py'
ORIGINAL_GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_manifest.py'
MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-phase-after-45913335399-inputs.json'
WORKFLOW = '.github/workflows/visible-exact-strict-nu-phase-after-45913335399.yml'


def require(ok,message):
    if not ok:raise ValueError(message)


def load(root,path,name):
    raw = (root/path).read_bytes();ast.parse(raw.decode(),filename=path)
    spec = importlib.util.spec_from_file_location(name,root/path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def descriptor(root,role,path):
    raw = (root/path).read_bytes();raw.decode()
    require(0 < len(raw) < 100000,'one whole small continuation input')
    if path.endswith('.py'):ast.parse(raw.decode(),filename=path)
    return {'role':role,'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
        'git_blob_sha':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}


def build(root):
    require(not any(x in sys.modules for x in ('flint','numpy','scipy')),'metadata only')
    sys.dont_write_bytecode = True
    worker = load(root,WORKER,'_PHI_resume_metadata');failed,old = worker.admitted_failure(root)
    compile(worker.build_adapter(root),WORKER,'exec')
    original = load(root,ORIGINAL_GENERATOR,'_PHI_original_manifest_definitions')
    specs = {x['role']:dict(x) for x in old['files']}
    for item in old['files']:
        require(descriptor(root,item['role'],item['path']) == item,'same whole original current input: '+item['role'])
    for role,old_role in (('failed_worker','worker'),('failed_generator','generator')):
        specs[role] = dict(specs[old_role],role=role)
    for role,path in (('worker',WORKER),('generator',GENERATOR),
        ('failed_execution',worker.FAILED),('failed_manifest',worker.OLD_MANIFEST)):
        specs[role] = descriptor(root,role,path)
    require(len(specs) == 89 and len({x['path'] for x in specs.values()}) == 89,
        'the entire original85 files plus four complete continuation objects')
    review = json.loads((root/specs['reviewed_rules']['path']).read_bytes())
    for path,digest in review['readme_sha256'].items():
        require(hashlib.sha256((root/path).read_bytes()).hexdigest() == digest,'same already read current README')
    roles = dict(old['roles'])
    for role in ('worker','generator','failed_worker','failed_generator','failed_execution','failed_manifest'):
        roles[role] = specs[role]['path']
    manifest = dict(old)
    manifest.update(problem_id='R147_complete_strict_nu_nonlocal_phase_after_45913335399',
        files=[specs[k] for k in sorted(specs)],expected_current_input_count=89,roles=roles,
        continuation={'run':'45913335399/1','failed_execution_sha256':worker.FAILED_SHA,
            'scientific_children_started':0,'complete_old_scientific_targets':[],
            'missing_targets':list(old['target_order']),
            'first_whole315_input_restoration_completed':True,
            'historical_descriptors_sha256':failed['historical_restoration']['whole_original_descriptors_sha256'],
            'scientific_owner_math_and_carrier_recipe_unchanged':True,
            'only_idempotent_historical_snapshot_reuse_changed':True,
            'same_complete_bytes_and_sha_required_before_reuse':True})
    manifest['operation'] = dict(old['operation'],consumed_marker=
        TOPIC+'/notes/strict_nu_phase_ci/consumed-after-45913335399.json')
    raw = (json.dumps(manifest,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()
    require(len(raw) < 100000 and not any(x in sys.modules for x in ('flint','numpy','scipy')),
        'whole small continuation manifest without a local scientific target')
    workflow = original.WORKFLOW_TEMPLATE
    for before,after in ((original.WORKFLOW,WORKFLOW),(original.MANIFEST,MANIFEST),(original.WORKER,WORKER),
        ('visible-flex-exact-strict-nu-nonlocal-phase-20261127','visible-flex-exact-strict-nu-phase-after-45913335399'),
        ('name: R147 first strict parameter nonlocal phase','name: R147 explicit strict phase continuation after zero child')):
        workflow = workflow.replace(before,after)
    insertion = ''.join('            /'+path+'\n' for path in (worker.ADAPTER,worker.FAILED,worker.OLD_MANIFEST))
    workflow = workflow.replace('            /'+WORKER+'\n','            /'+WORKER+'\n'+insertion)
    workflow = workflow.replace('@MANIFEST_SHA@',hashlib.sha256(raw).hexdigest())
    return raw,workflow.encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',default='.',type=Path)
    args = parser.parse_args();root = args.repo.resolve();sys.dont_write_bytecode = True
    raw,workflow = build(root)
    for relative,payload in ((MANIFEST,raw),(WORKFLOW,workflow)):
        path = root/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(payload)
    print(json.dumps({'ready':True,'manifest':MANIFEST,'manifest_bytes':len(raw),
        'manifest_sha256':hashlib.sha256(raw).hexdigest(),'workflow':WORKFLOW,
        'local_scientific_targets_evaluated':0},sort_keys=True))


if __name__ == '__main__':main()
