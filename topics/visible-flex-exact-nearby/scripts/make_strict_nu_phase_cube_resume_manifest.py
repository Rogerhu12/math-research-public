"""Metadata-only PHI successor retaining the true zero-prefix q-jet failure."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
WORKER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_cube_resume_worker.py'
GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_cube_resume_manifest.py'
MATH = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_integer_power_math.py'
ORIGINAL_GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_manifest.py'
PREVIOUS_GENERATOR = TOPIC+'/scripts/make_strict_nu_phase_resume_manifest.py'
MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-phase-after-45914123725-inputs.json'
WORKFLOW = '.github/workflows/visible-exact-strict-nu-phase-after-45914123725.yml'


def require(ok,message):
    if not ok:raise ValueError(message)


def load(root,path,name):
    raw = (root/path).read_bytes();ast.parse(raw.decode(),filename=path)
    spec = importlib.util.spec_from_file_location(name,root/path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build(root):
    require(not any(x in sys.modules for x in ('flint','numpy','scipy')),'metadata only')
    sys.dont_write_bytecode = True
    worker = load(root,WORKER,'_PHI_cube_resume_metadata');failed,actual,old = worker.admitted_failure(root)
    compile(worker.build_adapter(root),WORKER,'exec')
    previous = load(root,PREVIOUS_GENERATOR,'_PHI_previous_generator_metadata')
    original = load(root,ORIGINAL_GENERATOR,'_PHI_first_generator_definitions')
    specs = {x['role']:dict(x) for x in old['files']}
    for item in old['files']:
        require(previous.descriptor(root,item['role'],item['path']) == item,
            'every whole previous input remains unchanged: '+item['role'])
    for role,old_role in (('pre_cube_worker','worker'),('pre_cube_generator','generator'),
        ('pre_integer_power_math','phase_math')):
        specs[role] = dict(specs[old_role],role=role)
    for role,path in (('worker',WORKER),('generator',GENERATOR),('phase_math',MATH),
        ('pre_cube_execution',worker.FAILED),('pre_cube_actual',worker.ACTUAL),('pre_cube_manifest',worker.OLD_MANIFEST)):
        specs[role] = previous.descriptor(root,role,path)
    require(len(specs) == 95 and len({x['path'] for x in specs.values()}) == 95,
        'all previous89 objects plus six complete new continuation inputs')
    new_math = load(root,MATH,'_PHI_same_full_jets_literal_cube')
    require(list(new_math.OUTPUT_ORDER) == old['target_order'] and new_math.SIGNED_INDICES == (0,5),
        'same full six signed/error targets')
    # One literal-product change in the one overwritten function; all other
    # scientific definitions come from the exact original whole source.
    original_tree = ast.parse((root/specs['pre_integer_power_math']['path']).read_text())
    new_tree = ast.parse((root/MATH).read_text())
    original_fun = next(x for x in original_tree.body if isinstance(x,ast.FunctionDef) and x.name == 'curvature_power_jets')
    new_fun = next(x for x in new_tree.body if isinstance(x,ast.FunctionDef) and x.name == 'curvature_power_jets')
    changes = 0
    class IntegralCube(ast.NodeTransformer):
        def visit_BinOp(self,node):
            nonlocal changes
            if isinstance(node.op,ast.Pow) and ast.dump(node) == ast.dump(ast.parse('r1**3',mode='eval').body):
                changes += 1;return ast.parse('r1*r1*r1',mode='eval').body
            return self.generic_visit(node)
    transformed = IntegralCube().visit(original_fun)
    require(changes == 1 and ast.dump(transformed) == ast.dump(new_fun),'exactly the one integer cube spelling changes')
    review = json.loads((root/specs['reviewed_rules']['path']).read_bytes())
    for path,digest in review['readme_sha256'].items():
        require(hashlib.sha256((root/path).read_bytes()).hexdigest() == digest,'same already read current README')
    roles = dict(old['roles'])
    for role in ('worker','generator','phase_math','pre_cube_worker','pre_cube_generator','pre_integer_power_math',
        'pre_cube_execution','pre_cube_actual','pre_cube_manifest'):
        roles[role] = specs[role]['path']
    manifest = dict(old)
    manifest.update(problem_id='R147_complete_strict_nu_nonlocal_phase_after_45914123725',
        files=[specs[k] for k in sorted(specs)],expected_current_input_count=95,roles=roles,
        continuation={'run':'45914123725/1','failed_execution_sha256':worker.FAILED_SHA,
            'failed_scientific_prefix_sha256':worker.ACTUAL_SHA,'complete_old_scientific_targets':[],
            'complete_new_phase_germ_prefix':None,'missing_targets':list(old['target_order']),
            'whole_original_NP_trial_restoration_succeeded':True,
            'whole_original_NP_trial_definition_sha256':actual['necessary_original_trial_receipts']['complete_original_trial_definition_sha256'],
            'scientific_owner_and_original_carrier_recipe_unchanged':True,
            'one_integer_power_replaced_by_the_same_literal_product':True,
            'all_original_whole_derivative_balls_and_Taylor_remainders_retained':True,
            'idempotent_same_whole_snapshot_reuse_retained':True})
    manifest['operation'] = dict(old['operation'],consumed_marker=
        TOPIC+'/notes/strict_nu_phase_ci/consumed-after-45914123725.json')
    raw = (json.dumps(manifest,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n').encode()
    require(len(raw) < 100000 and not any(x in sys.modules for x in ('flint','numpy','scipy')),
        'whole small immutable manifest; zero local scientific targets')
    workflow = original.WORKFLOW_TEMPLATE
    for before,after in ((original.WORKFLOW,WORKFLOW),(original.MANIFEST,MANIFEST),(original.WORKER,WORKER),
        ('visible-flex-exact-strict-nu-nonlocal-phase-20261127','visible-flex-exact-strict-nu-phase-after-45914123725'),
        ('name: R147 first strict parameter nonlocal phase','name: R147 explicit strict phase continuation with literal cube')):
        workflow = workflow.replace(before,after)
    extra = (worker.ADAPTER,original.WORKER,worker.FAILED,worker.ACTUAL,worker.OLD_MANIFEST,
        TOPIC+'/notes/strict_nu_phase_ci/run-45913335399-1/execution.json',original.MANIFEST)
    insertion = ''.join('            /'+path+'\n' for path in extra)
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
