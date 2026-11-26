#!/usr/bin/env python3
"""Explicit source chain: published complete PCG/SOC -> all-row constrained SOC.

Only stdlib source construction/binding is performed here. The frozen old
composite and all of its original guards remain unchanged. Old parents are
validated by the old complete binder; new parents are rebuilt in full here.
"""
import argparse
import ast
import hashlib
import importlib.util
from pathlib import Path
import sys

OLD_COMPOSITE_SHA='40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e'
OLD_HELPER_SHA='5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
NEW_HELPER_SHA='a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
LINEAGE_SCHEMA='complete-PCG-SOC-to-all-original-row-halfspace-SOC-v1'
BASES={
    'original':('fullclosed_gauss_inequality_qp.py','5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671':('fullclosed_gauss_exact_tail_inequality_qp.py','b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'),
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load_old(source_dir):
    path=Path(source_dir)/'derive_full_phi_coarse_pcg_soc.py'
    if sha(path)!=OLD_COMPOSITE_SHA:
        raise ValueError('The published complete PCG/SOC source deriver changed')
    spec=importlib.util.spec_from_file_location('all_rows_SOC_published_composite',path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod

def same(a,b):
    return ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)

def build_ast(base,manifest_source,**unused):
    base=Path(base).resolve()
    old=load_old(base.parent)
    tree,previous=old.build_ast(base,manifest_source)
    model=previous['model']
    lineage=dict(schema=LINEAGE_SCHEMA,model=model,
        derivation_source_sha256=sha(__file__),published_composite_deriver_sha256=OLD_COMPOSITE_SHA,
        published_composite_lineage=previous,new_helper_sha256=NEW_HELPER_SHA,
        old_SOC_and_PCG_lineages_retained_as_source_generation_history=True,
        actual_runtime_helper_identity_is_parent_row_soc_and_source_sha256_by_role=True,
        changed_numerical_operation='min ||e||^2/2 subject to C e <= min(b-C*d,-c(d)-tau*||d||^3) for every original row',
        same_parent_binding_field_model_objective_norm_QP_preconditioner_points_acceptance_and_damping=True,
        scientific_execution_performed=False)
    counts=dict(runtime_helper_guard=0,runtime_helper_metadata=0,report=0)
    class Change(ast.NodeTransformer):
        def visit_Compare(self,node):
            node=self.generic_visit(node)
            anchor=ast.parse("sha(paths['soc'])",mode='eval').body
            if same(node.left,anchor) and len(node.comparators)==1:
                rhs=node.comparators[0]
                if not isinstance(rhs,ast.Constant) or rhs.value!=OLD_HELPER_SHA:
                    raise ValueError('The old runtime helper guard site changed')
                rhs.value=NEW_HELPER_SHA
                counts['runtime_helper_guard']+=1
            return node
        def visit_Assign(self,node):
            # Preserve immutable previous source-generation provenance; edit
            # only the live report expression and runtime numeric helper check.
            if (len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
                    and node.targets[0].id=='report' and isinstance(node.value,ast.Call)
                    and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict'):
                keys={k.arg for k in node.value.keywords}
                if {'schema','soc_derivation','pcg_soc_derivation','parent_row_soc'}<=keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema':
                            kw.value=ast.Constant('fullclosed-gauss-'+model+'-coarse-PCG-all-row-SOC-v2')
                        if kw.arg=='parent_row_soc':
                            if not isinstance(kw.value,ast.Call):
                                raise ValueError('The live SOC report metadata changed')
                            for arg in kw.value.keywords:
                                if arg.arg=='helper_sha256':
                                    if not isinstance(arg.value,ast.Constant) or arg.value.value!=OLD_HELPER_SHA:
                                        raise ValueError('The old live helper identity changed')
                                    arg.value=ast.Constant(NEW_HELPER_SHA)
                                    counts['runtime_helper_metadata']+=1
                            kw.value.keywords.extend([
                                ast.keyword(arg='correction_optimization',value=ast.Constant('all-original-row-halfspace-projection')),
                                ast.keyword(arg='all_old_linear_margins_inside_correction_problem',value=ast.Constant(True)),
                                ast.keyword(arg='all_fixed_parent_nonlinear_targets_inside_correction_problem',value=ast.Constant(True))])
                    node.value.keywords.append(ast.keyword(arg='all_rows_soc_derivation',
                        value=ast.Name(id='ALL_ROWS_SOC_LINEAGE',ctx=ast.Load())))
                    counts['report']+=1
            return self.generic_visit(node)
    tree=Change().visit(tree)
    if counts!=dict(runtime_helper_guard=1,runtime_helper_metadata=1,report=1):
        raise ValueError('Exact live all-row SOC transformation sites changed: '+repr(counts))
    lineage['exact_runtime_edit_counts']=counts
    pos=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos]=ast.parse('ALL_ROWS_SOC_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree)
    compile(tree,str(base)+'-all-row-SOC','exec')
    return tree,lineage

def derive_driver(base,destination,manifest_source,**kwargs):
    tree,lineage=build_ast(base,manifest_source,**kwargs)
    text='#!/usr/bin/env python3\n# Complete published PCG/SOC followed by explicitly identified all-row SOC.\n'+ast.unparse(tree)+'\n'
    destination=Path(destination)
    if destination.exists() and destination.read_text()!=text:
        raise FileExistsError('Use a fresh driver destination for different bytes')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(text)
    return dict(path=str(destination.resolve()),sha256=sha(destination),bytes=destination.stat().st_size,
        derivation=lineage,scientific_execution_performed=False)

def bind_soc_parent(report,supplied,source_dir,manifest_source,**unused):
    old=load_old(source_dir)
    if 'all_rows_soc_derivation' not in report:
        return old.bind_soc_parent(report,supplied,source_dir,manifest_source)
    if supplied is None:
        raise ValueError('A constrained-SOC parent requires its actual full driver source')
    path=Path(supplied).resolve()
    if report.get('source_sha256')!=sha(path):
        raise ValueError('Constrained-SOC report does not bind the actual source bytes')
    model=report['all_rows_soc_derivation'].get('model')
    if model not in BASES:
        raise ValueError('Unknown constrained-SOC physical model')
    expected,lineage=build_ast(Path(source_dir)/BASES[model][0],manifest_source)
    if report['all_rows_soc_derivation']!=lineage or not same(expected,ast.parse(path.read_text())):
        raise ValueError('Actual new parent body differs from its complete explicit derivation')
    previous=lineage['published_composite_lineage']
    if (report.get('schema')!='fullclosed-gauss-'+model+'-coarse-PCG-all-row-SOC-v2'
            or report.get('pcg_soc_derivation')!=previous
            or report.get('soc_derivation')!=previous['SOC_lineage']
            or report.get('parent_row_soc',{}).get('helper_sha256')!=NEW_HELPER_SHA):
        raise ValueError('Actual new report runtime identity or preserved provenance differs')
    roles=report.get('source_sha256_by_role',{})
    if roles.get('soc')!=NEW_HELPER_SHA:
        raise ValueError('Actual constrained-SOC source role differs from the declared helper')
    if report.get('coarse_preconditioner_setup',{}).get('enabled') is not True:
        raise ValueError('The declared complete PCG branch is not enabled')
    for role,(_,digest) in old.COMPONENTS.items():
        if roles.get(role)!=digest:
            raise ValueError('Constrained-SOC changed an undeclared PCG component: '+role)
    actual_coarse=[ast.literal_eval(kw.value) for node in ast.walk(expected)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='dict'
        for kw in node.keywords if kw.arg=='coarse_preconditioner_derivation']
    if len(actual_coarse)!=1 or report.get('coarse_preconditioner_derivation')!=actual_coarse[0]:
        raise ValueError('The actual coarse preconditioner provenance differs')
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,model=model,
        declared_derivation=lineage,actual_entire_body_AST_matched=True,
        parent_report_edited=False,old_guard_bypassed=False)

def main():
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',type=Path,required=True)
    p.add_argument('--manifest-source',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    print(json.dumps(derive_driver(a.base,a.out,a.manifest_source),indent=2))

if __name__=='__main__':
    main()
