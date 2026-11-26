#!/usr/bin/env python3
"""Continue the unchanged v5 scientific chain through verified physical base.

The full published f092 launcher is derived first. This independent source
changes only its parent-source adapter, preparation planner and captured
failure visibility. Published scientific driver construction stays 7b3e...
and the actual v5/all-row scientific modules keep their original identities.

Forward the original CLI. Additional flag: --verified-parent-adapter PATH.
--prepare-source-only constructs complete source only, without a report or
scientific arrays. Actual parent/terminal-mu/model/positions remain checked.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

PUBLISHED_LAUNCHER_SHA='f092e359fac156f6673a428b1b1175a8607e127b0ec86f2e1dc3d812658c8476'
PUBLISHED_DERIVER_SHA='7b3e7911b35beab8a5979e91cecdd1d35f467bc39dddb57e1035d327896067ed'
ADAPTER_SHA='8c3d11bb55c029ffcae23b126d566108947e9a92523574a53bfda7a4556f487f'
QP_SHA='76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'
ORIGINAL_SOC_LAUNCHER_SHA='9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(path):
    path=Path(path).resolve();return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def load_bound(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete published source: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def same(left,right):
    return ast.dump(left,include_attributes=False)==ast.dump(right,include_attributes=False)


def assigned(node,name):
    return (isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name)


PLANNER_WRAPPER='''def prepare_soc_parent_planner(base,destination,deriver_path,model):
    """Independent complete binding and canonical physical-base preparation."""
    required_sha(deriver_path,DERIVER_SHA,'verified physical-base parent adapter')
    source_adapter=load('full_body_then_canonical_physical_base',deriver_path)
    return source_adapter.prepare_parent_planner(base,destination,model,adapter_path=deriver_path)
'''


def derive_launcher(source_dir,destination,adapter_path,qp_path,driver_deriver):
    source_dir=Path(source_dir).resolve();published=source_dir.parent/'resume_20261126'
    old_path=published/'launch_full_phi_face_pcg.py'
    adapter_path=Path(adapter_path).resolve();qp_path=Path(qp_path).resolve()
    driver_deriver=Path(driver_deriver).resolve();destination=Path(destination).resolve()
    old=load_bound('verified_base_original_face_launcher',old_path,PUBLISHED_LAUNCHER_SHA)
    adapter=load_bound('verified_base_complete_parent_adapter',adapter_path,ADAPTER_SHA)
    for path,digest in ((qp_path,QP_SHA),(driver_deriver,PUBLISHED_DERIVER_SHA)):
        if sha(path)!=digest:raise ValueError('The scientific v5 chain must remain unchanged')
    original_soc=source_dir/'launch_full_phi_parent_row_soc.py'
    if sha(original_soc)!=ORIGINAL_SOC_LAUNCHER_SHA:
        raise ValueError('The complete published original preparation function changed')
    original_functions=[node for node in ast.parse(original_soc.read_text()).body
        if isinstance(node,ast.FunctionDef) and node.name=='prepare_soc_parent_planner']
    if len(original_functions)!=1:raise ValueError('Expected one complete old preparation function')
    prior_path=destination.with_name('published-face-PCG-v5-launcher.py')
    prior=old.derive_launcher(source_dir,prior_path,qp_path,driver_deriver)
    tree=ast.parse(prior_path.read_text())
    counts=dict(adapter_SHA=0,adapter_default=0,complete_preparation_function=0,
        main_captured_failure=0,plan=0)
    lineage=dict(schema='complete-v5-launcher-explicit-verified-physical-base-v1',
        source=record(__file__),published_complete_v5_launcher=prior,
        actual_parent_source_adapter=record(adapter_path),
        unchanged_scientific_driver_deriver=record(driver_deriver),unchanged_v5_QP=record(qp_path),
        complete_parent_body_AST_and_roles_bound_before_base_lookup=True,
        canonical_BASES_actual_file_bytes_checked=True,
        declared_derivation_and_parent_report_preserved=True,
        literal_physical_DRIVER_SHA_guard_preserved=True,
        scientific_driver_body_or_parameters_changed=False,
        all_original_terminal_mu_model_objective_and_positions_checks_preserved=True,
        captured_preparation_failures_expose_real_stdout_and_stderr=True,
        scientific_execution_performed_by_deriver=False)
    class Change(ast.NodeTransformer):
        def visit_Assign(self,node):
            if assigned(node,'DERIVER_SHA'):
                if not isinstance(node.value,ast.Constant) or node.value.value!=PUBLISHED_DERIVER_SHA:
                    raise ValueError('The original live v5 deriver identity site changed')
                node.value=ast.Constant(ADAPTER_SHA);counts['adapter_SHA']+=1
            if assigned(node,'deriver_path'):
                for value in ast.walk(node.value):
                    if isinstance(value,ast.Constant) and value.value==str(driver_deriver):
                        value.value=str(adapter_path);counts['adapter_default']+=1
            if (assigned(node,'plan') and isinstance(node.value,ast.Call)
                    and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict'):
                keys={kw.arg for kw in node.value.keywords}
                if {'face_pcg_launcher_derivation','full_scientific_command','derived_driver'}<=keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema':
                            kw.value=ast.Constant('actual-complete-v5-continuation-with-verified-physical-base-v1')
                        if kw.arg=='source_and_model_transitions':
                            kw.value=ast.Constant('Same physical model and exact published v5 driver chain. Separate full-body-verified canonical base identity fixes preparation without rewriting source lineage or parent data.')
                    node.value.keywords.append(ast.keyword(arg='verified_physical_base_launcher_derivation',
                        value=ast.Name(id='VERIFIED_BASE_LAUNCHER_LINEAGE',ctx=ast.Load())))
                    counts['plan']+=1
            return self.generic_visit(node)
        def visit_FunctionDef(self,node):
            if node.name=='prepare_soc_parent_planner':
                if not same(node,original_functions[0]):
                    raise ValueError('Replace only the exact complete published preparation function')
                counts['complete_preparation_function']+=1
                return ast.parse(PLANNER_WRAPPER).body[0]
            node=self.generic_visit(node)
            if node.name=='main':
                counts['main_captured_failure']+=adapter.expose_preparation_failure(node)
            return node
    tree=Change().visit(tree)
    expected=dict(adapter_SHA=1,adapter_default=1,complete_preparation_function=1,
        main_captured_failure=1,plan=1)
    if counts!=expected:raise ValueError('Exact complete launcher repair sites changed: '+repr(counts))
    lineage['exact_edit_counts']=counts
    position=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[position:position]=ast.parse('VERIFIED_BASE_LAUNCHER_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree);compile(tree,str(destination),'exec')
    text='#!/usr/bin/env python3\n# Whole v5 parent verified before separate canonical physical base lookup.\n'+ast.unparse(tree)+'\n'
    if destination.exists() and destination.read_text()!=text:raise FileExistsError(destination)
    destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(text)
    return dict(**record(destination),derivation=lineage,scientific_execution_performed=False)


def main():
    if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:print(__doc__);return
    p=argparse.ArgumentParser(add_help=False)
    for name in ('repo','work','outdir'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--verified-parent-adapter',type=Path)
    p.add_argument('--face-qp-source',type=Path);p.add_argument('--face-deriver',type=Path)
    p.add_argument('--prepare-source-only',action='store_true');a,_=p.parse_known_args()
    source_dir=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    published=source_dir.parent/'resume_20261126'
    adapter=(a.verified_parent_adapter or Path(__file__).with_name('face_pcg_verified_parent_source.py')).resolve()
    qp=(a.face_qp_source or published/'fullspace_feasible_active_pcg_v5.py').resolve()
    driver_deriver=(a.face_deriver or published/'derive_full_phi_face_pcg.py').resolve()
    destination=a.work.resolve()/(a.outdir.resolve().name+'-continuation-inputs')/'launch-face-PCG-verified-base.py'
    result=derive_launcher(source_dir,destination,adapter,qp,driver_deriver)
    if a.prepare_source_only:print(json.dumps(result,indent=2));return
    forwarded=list(sys.argv[1:])
    for flag in ('--verified-parent-adapter','--face-qp-source','--face-deriver'):
        if flag in forwarded:
            index=forwarded.index(flag);del forwarded[index:index+2]
    if '--prepare-source-only' in forwarded:forwarded.remove('--prepare-source-only')
    result=subprocess.run([sys.executable,str(destination),*forwarded])
    raise SystemExit(result.returncode)


if __name__=='__main__':main()
