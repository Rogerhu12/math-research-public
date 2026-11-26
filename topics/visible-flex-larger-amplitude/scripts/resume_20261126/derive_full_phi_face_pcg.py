#!/usr/bin/env python3
"""Explicit whole-body all-row-SOC -> v5 constrained-face PCG source chain."""
import argparse
import ast
import hashlib
import importlib.util
from pathlib import Path
import sys

PREVIOUS_SHA='94ea77107305c058425877a3ff93cf7e8b58575e982f5ca6c1040a32279a0f73'
OLD_QP_SHA='dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b'
NEW_QP_SHA='76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'
V3_SHA='fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
LINEAGE_SCHEMA='all-old-row-SOC-with-constrained-active-face-PCG-v5'
BASES={
    'original':('fullclosed_gauss_inequality_qp.py','5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671':('fullclosed_gauss_exact_tail_inequality_qp.py','b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'),
}

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def same(a,b): return ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)
def assigned(node,name):
    return isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name

def previous():
    path=Path(__file__).with_name('derive_full_phi_all_rows_soc.py')
    if sha(path)!=PREVIOUS_SHA: raise ValueError('The declared all-row source chain changed')
    spec=importlib.util.spec_from_file_location('v5_previous_allrow_deriver',path)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    return mod

def build_ast(base,manifest_source,**unused):
    prior=previous()
    tree,oldlineage=prior.build_ast(base,manifest_source)
    model=oldlineage['model']
    lineage=dict(schema=LINEAGE_SCHEMA,model=model,derivation_source_sha256=sha(__file__),
        previous_deriver_sha256=PREVIOUS_SHA,previous_all_rows_lineage=oldlineage,
        runtime_QP_source_sha256=NEW_QP_SHA,original_v3_fallback_sha256=V3_SHA,
        new_face_map='B-BQ^T(QBQ^T)^-1QB',original_global_B_unchanged=True,
        same_QP_full_space_norm_rows_stopping_release_SOC_true_acceptance_and_damping=True,
        previous_lineages_are_source_generation_history_not_the_actual_v5_QP_identity=True,
        scientific_execution_performed=False)
    counts=dict(runtime_QP_guard=0,original_v3_path=0,report=0)
    class Change(ast.NodeTransformer):
        def visit_FunctionDef(self,node):
            if node.name=='_coarse_preconditioner_sources':
                for st in node.body:
                    if assigned(st,'expected') and isinstance(st.value,ast.Dict):
                        for k,v in zip(st.value.keys,st.value.values):
                            if isinstance(k,ast.Constant) and k.value=='qp':
                                if not isinstance(v,ast.Constant) or v.value!=OLD_QP_SHA:
                                    raise ValueError('Live QP source guard changed')
                                v.value=NEW_QP_SHA;counts['runtime_QP_guard']+=1
                    if isinstance(st,ast.Assign) and len(st.targets)==1 and same(st.targets[0],ast.parse("paths['coarse_qp_v3'] = None").body[0].targets[0]):
                        st.value=ast.parse("paths['coarse_frame'].with_name('fullspace_feasible_active_cg_v3.py')",mode='eval').body
                        counts['original_v3_path']+=1
                for value in ast.walk(node):
                    if isinstance(value,ast.Constant) and value.value=='v4 returns a truthful truncated status; no within-solve replacement or automatic retry':
                        value.value='v5 uses explicit whole-new-face PBP fallback on Schur construction failure; failed active application still truncates without mid-chain metric substitution'
            return self.generic_visit(node)
        def visit_Assign(self,node):
            if assigned(node,'report') and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict':
                keys={kw.arg for kw in node.value.keywords}
                if {'all_rows_soc_derivation','coarse_preconditioner_setup','schema'}<=keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema': kw.value=ast.Constant('fullclosed-gauss-'+model+'-all-row-SOC-face-PCG-v5')
                    node.value.keywords.append(ast.keyword(arg='face_pcg_derivation',value=ast.Name(id='FACE_PCG_LINEAGE',ctx=ast.Load())))
                    counts['report']+=1
            return self.generic_visit(node)
    tree=Change().visit(tree)
    if counts!=dict(runtime_QP_guard=1,original_v3_path=1,report=1):
        raise ValueError('Complete v5 live source sites changed: '+repr(counts))
    lineage['exact_edit_counts']=counts
    pos=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos]=ast.parse('FACE_PCG_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree);compile(tree,str(base)+'-face-PCG-v5','exec')
    return tree,lineage

def derive_driver(base,destination,manifest_source,**kwargs):
    tree,lineage=build_ast(base,manifest_source,**kwargs)
    text='#!/usr/bin/env python3\n# Complete all-row SOC followed by explicit constrained-face PCG v5.\n'+ast.unparse(tree)+'\n'
    destination=Path(destination)
    if destination.exists() and destination.read_text()!=text: raise FileExistsError('Use a fresh v5 driver destination')
    destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(text)
    return dict(path=str(destination.resolve()),sha256=sha(destination),bytes=destination.stat().st_size,
        derivation=lineage,scientific_execution_performed=False)

def bind_soc_parent(report,supplied,source_dir,manifest_source,**unused):
    prior=previous()
    if 'face_pcg_derivation' not in report:
        return prior.bind_soc_parent(report,supplied,source_dir,manifest_source)
    if supplied is None: raise ValueError('A v5 parent requires its actual complete source')
    path=Path(supplied).resolve()
    if report.get('source_sha256')!=sha(path): raise ValueError('Actual v5 source bytes do not match the report')
    model=report['face_pcg_derivation'].get('model')
    if model not in BASES: raise ValueError('Unknown v5 physical model')
    expected,lineage=build_ast(Path(source_dir)/BASES[model][0],manifest_source)
    if report['face_pcg_derivation']!=lineage or not same(expected,ast.parse(path.read_text())):
        raise ValueError('The complete actual v5 body differs from its explicit derivation')
    allrows=lineage['previous_all_rows_lineage']
    composite=allrows['published_composite_lineage']
    if (report.get('schema')!='fullclosed-gauss-'+model+'-all-row-SOC-face-PCG-v5'
            or report.get('all_rows_soc_derivation')!=allrows
            or report.get('pcg_soc_derivation')!=composite
            or report.get('soc_derivation')!=composite['SOC_lineage']):
        raise ValueError('The actual v5 schema or preserved source history differs')
    roles=report.get('source_sha256_by_role',{})
    if roles.get('soc')!=prior.NEW_HELPER_SHA or report.get('parent_row_soc',{}).get('helper_sha256')!=prior.NEW_HELPER_SHA:
        raise ValueError('The actual all-row helper differs')
    components=prior.load_old(source_dir).COMPONENTS
    for role,(_,digest) in components.items():
        required=NEW_QP_SHA if role=='qp' else digest
        if roles.get(role)!=required: raise ValueError('The runtime v5 component differs: '+role)
    if report.get('coarse_preconditioner_setup',{}).get('enabled') is not True:
        raise ValueError('The declared complete coarse preconditioner branch is disabled')
    oldcoarse=[ast.literal_eval(kw.value) for node in ast.walk(expected)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='dict'
        for kw in node.keywords if kw.arg=='coarse_preconditioner_derivation']
    if len(oldcoarse)!=1 or report.get('coarse_preconditioner_derivation')!=oldcoarse[0]:
        raise ValueError('Preserved original global-B construction identity differs')
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,model=model,
        declared_derivation=lineage,actual_entire_body_AST_matched=True,
        parent_report_edited=False,old_guard_bypassed=False)

def main():
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',type=Path,required=True);p.add_argument('--manifest-source',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    print(json.dumps(derive_driver(a.base,a.out,a.manifest_source),indent=2))
if __name__=='__main__':main()
