#!/usr/bin/env python3
"""Separate a verified physical base identity from complete driver lineage.

The unmodified published 7b3e... whole-body/role binder runs FIRST. Only
after it succeeds is the canonical physical BASES entry independently
read and byte checked. No report or declared_derivation is rewritten.
Source derivation is delegated unchanged to that same published module.
The preparation-only planner preserves its literal DRIVER_SHA comparison.
All work in this module uses the standard library, never scientific arrays.
"""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

PUBLISHED_DERIVER_SHA='7b3e7911b35beab8a5979e91cecdd1d35f467bc39dddb57e1035d327896067ed'
BASES={
    'original':('fullclosed_gauss_inequality_qp.py','5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671':('fullclosed_gauss_exact_tail_inequality_qp.py','b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8')}
PLANNERS={
    'original':('launch_full_phi_from_completed_report.py','18ba10e5a37f5032b37388a7bfcdede97d11dc680685d73520732f9a278697f7'),
    'R671':('launch_full_phi_exact_tail_from_completed_report.py','425fd1d1254450afac26b2ca29ca4ffbb6fb93d59588163bef726e34999e4703')}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def file_record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def same(left,right):
    return ast.dump(left,include_attributes=False)==ast.dump(right,include_attributes=False)


def assigned(node,name):
    return (isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name)


def published(source_dir):
    path=Path(source_dir).resolve().parent/'resume_20261126/derive_full_phi_face_pcg.py'
    if sha(path)!=PUBLISHED_DERIVER_SHA:
        raise ValueError('Keep the original complete v5 source derivation and binder')
    name='physical_base_adapter_published_v5_'+PUBLISHED_DERIVER_SHA[:12]
    module=sys.modules.get(name)
    if module is None:
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module
        spec.loader.exec_module(module)
    if module.BASES!=BASES:
        raise ValueError('The independently declared canonical physical base table differs')
    return module


def build_ast(base,manifest_source,**kwargs):
    return published(Path(base).resolve().parent).build_ast(base,manifest_source,**kwargs)


def derive_driver(base,destination,manifest_source,**kwargs):
    # The returned complete scientific body and all its lineage are EXACTLY
    # the published v5 source construction. This adapter adds no driver edit.
    return published(Path(base).resolve().parent).derive_driver(base,destination,manifest_source,**kwargs)


def bind_soc_parent(report,supplied,source_dir,manifest_source,**kwargs):
    original=published(source_dir)
    bound=original.bind_soc_parent(report,supplied,source_dir,manifest_source,**kwargs)
    if bound.get('actual_entire_body_AST_matched') is not True:
        raise ValueError('A separately verified physical base requires the complete actual parent body match first')
    model=bound.get('model')
    if model not in BASES:
        raise ValueError('The original full binder returned an unknown physical model')
    name,digest=BASES[model]
    physical=(Path(source_dir)/name).resolve()
    if sha(physical)!=digest:
        raise ValueError('The independently selected canonical physical base source changed')
    if 'verified_physical_base' in bound:
        raise ValueError('The immutable published binder unexpectedly already owns this new result field')
    result=dict(bound)
    result['verified_physical_base']=dict(model=model,**file_record(physical),
        complete_parent_body_binder_sha256=PUBLISHED_DERIVER_SHA,
        verification_order='Original complete parent source/AST/roles first; independent canonical BASES file bytes second',
        scope='Canonical physical base, distinct from the actual derived executable driver identity')
    result['physical_base_adapter']=dict(**file_record(__file__),
        declared_derivation_preserved=True,parent_report_edited=False,
        original_complete_body_and_component_checks_retained=True)
    return result


FAILED_PREPARATION = """if prepared.returncode != 0:
    if prepared.stdout:
        print(prepared.stdout, file=sys.stderr, end='' if prepared.stdout.endswith('\\n') else '\\n', flush=True)
    if prepared.stderr:
        print(prepared.stderr, file=sys.stderr, end='' if prepared.stderr.endswith('\\n') else '\\n', flush=True)
    raise subprocess.CalledProcessError(prepared.returncode, prepared.args,
        output=prepared.stdout, stderr=prepared.stderr)
"""


def expose_preparation_failure(function):
    """Replace one actual captured preparation with check=False + diagnostics."""
    count=0;body=[]
    for statement in function.body:
        if assigned(statement,'prepared') and isinstance(statement.value,ast.Call):
            call=statement.value
            if not same(call.func,ast.parse('subprocess.run',mode='eval').body):
                raise ValueError('The captured preparation call is no longer subprocess.run')
            keywords={kw.arg:kw for kw in call.keywords}
            if (set(keywords)!={'check','capture_output','text'}
                    or any(not isinstance(keywords[k].value,ast.Constant)
                        or keywords[k].value.value is not True for k in keywords)):
                raise ValueError('Expected the exact original captured check=True preparation')
            keywords['check'].value=ast.Constant(False)
            body.append(statement);body.extend(ast.parse(FAILED_PREPARATION).body);count+=1
        else:body.append(statement)
    if count!=1:raise ValueError('Expected exactly one complete captured preparation in main')
    function.body=body
    return count


def prepare_parent_planner(base,destination,model,*,adapter_path=None):
    """Only full binding, verified base lookup and error visibility change.

    Both original and R671 canonical source hashes remain literal frozen
    values in the planner. Its model, terminal damping, observation/mesh,
    objective and complete exact-position gates remain the original code.
    """
    if model not in PLANNERS:raise ValueError('Unknown complete physical planner')
    base=Path(base).resolve();adapter=Path(__file__ if adapter_path is None else adapter_path).resolve()
    if sha(base)!=PLANNERS[model][1]:raise ValueError('Changed complete immutable parent planner')
    if sha(adapter)!=sha(__file__):raise ValueError('Use this complete separately identified physical-base adapter')
    # Even source preparation verifies that the original whole binder and
    # exact model table are present; it does not bind a fictitious report.
    published(base.parent)
    tree=ast.parse(base.read_text())
    old_parent=ast.parse('history.bound_parent_source(report,source_dir,args.parent_source)',mode='eval').body
    old_base=ast.parse("parent_source.get('declared_derivation',{}).get('frozen_driver_sha256',parent_source['sha256'])",mode='eval').body
    old_guard=ast.parse('original_base != DRIVER_SHA',mode='eval').body
    guards=[ast.dump(node,include_attributes=False) for node in ast.walk(tree)
        if isinstance(node,ast.Compare) and same(node,old_guard)]
    assignments=[node for node in tree.body if assigned(node,'DRIVER_SHA')]
    if (len(guards)!=1 or len(assignments)!=1
            or ast.literal_eval(assignments[0].value)!=BASES[model][1]):
        raise ValueError('The frozen literal physical DRIVER_SHA guard changed')
    original_driver_assignment=ast.dump(assignments[0],include_attributes=False)
    counts=dict(complete_parent_binder=0,verified_physical_base_lookup=0,
        preparation_only_guard=0,captured_preparation_failure=0)
    class Change(ast.NodeTransformer):
        def visit_Assign(self,node):
            node=self.generic_visit(node)
            if assigned(node,'parent_source'):
                if not same(node.value,old_parent):raise ValueError('The original parent-source call changed')
                node.value=ast.parse('soc_source_binder.bind_soc_parent(report,args.parent_source,source_dir,derivation_path)',mode='eval').body
                counts['complete_parent_binder']+=1
            if assigned(node,'original_base'):
                if not same(node.value,old_base):raise ValueError('The actual nested-provenance failure site changed')
                node.value=ast.parse("parent_source['verified_physical_base']['sha256']",mode='eval').body
                counts['verified_physical_base_lookup']+=1
            return node
        def visit_FunctionDef(self,node):
            node=self.generic_visit(node)
            if node.name!='main':return node
            body=[]
            for statement in node.body:
                body.append(statement)
                if (assigned(statement,'args') and isinstance(statement.value,ast.Call)
                        and isinstance(statement.value.func,ast.Attribute)
                        and statement.value.func.attr=='parse_args'):
                    body.extend(ast.parse(
                        "if not args.print_command:\n"
                        "    raise RuntimeError('The verified-base parent planner is preparation-only')\n"
                        "if args.parent_source is None:\n"
                        "    raise ValueError('A derived parent needs its actual complete source')\n"
                        "soc_binder_path=Path("+repr(str(adapter))+")\n"
                        "if source_sha(soc_binder_path)!="+repr(sha(adapter))+":\n"
                        "    raise ValueError('Verified physical-base adapter source changed')\n"
                        "soc_source_binder=load('complete_parent_then_physical_base',soc_binder_path)\n"
                    ).body);counts['preparation_only_guard']+=1
            node.body=body
            counts['captured_preparation_failure']+=expose_preparation_failure(node)
            return node
    tree=ast.fix_missing_locations(Change().visit(tree))
    if counts!=dict(complete_parent_binder=1,verified_physical_base_lookup=1,
            preparation_only_guard=1,captured_preparation_failure=1):
        raise ValueError('Expected exactly the complete explicit planner repair sites')
    after=[node for node in tree.body if assigned(node,'DRIVER_SHA')]
    if (len(after)!=1 or ast.dump(after[0],include_attributes=False)!=original_driver_assignment
            or [ast.dump(node,include_attributes=False) for node in ast.walk(tree)
                if isinstance(node,ast.Compare) and same(node,old_guard)]!=guards):
        raise ValueError('The original literal DRIVER_SHA declaration/comparison must remain unchanged')
    compile(tree,str(destination),'exec')
    provenance=dict(schema='full-parent-binder-then-verified-physical-base-planner-v1',model=model,
        frozen_planner=file_record(base),source_adapter=file_record(adapter),
        published_complete_parent_binder_sha256=PUBLISHED_DERIVER_SHA,
        exact_edit_counts=counts,literal_physical_DRIVER_SHA_guard_preserved=True,
        parent_report_edited=False,declared_derivation_rewritten=False,
        all_original_model_objective_terminal_mu_and_positions_checks_preserved=True,
        captured_child_stdout_and_stderr_visible_on_failure=True,
        scientific_execution_allowed=False)
    text='#!/usr/bin/env python3\n# Explicit verified-base preparation: '+json.dumps(provenance,sort_keys=True)+'\n'+ast.unparse(tree)+'\n'
    destination=Path(destination)
    if destination.exists() and destination.read_text()!=text:raise FileExistsError(destination)
    destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(text)
    return dict(**file_record(destination),derivation=provenance)
