#!/usr/bin/env python3
"""Continue a real completed parent using all-row SOC and face-metric PCG v5.

Forward the complete prior continuation CLI. Old/all-row/v5 parents are
bound by their own full actual source bodies. --maxiter remains explicit;
no iteration-limit result is called converged. Extra source flags are
--face-qp-source, --face-deriver and --prepare-source-only.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

PREVIOUS_LAUNCHER_SHA='67350cf54390b4a62b8fb7e0ca3b05750433ab1397aeadd0a066b471fae1bc1d'
PREVIOUS_DERIVER_SHA='94ea77107305c058425877a3ff93cf7e8b58575e982f5ca6c1040a32279a0f73'
NEW_DERIVER_SHA='7b3e7911b35beab8a5979e91cecdd1d35f467bc39dddb57e1035d327896067ed'
OLD_QP_SHA='dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b'
NEW_QP_SHA='76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def record(path):
    p=Path(path).resolve();return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
def assigned(node,name):
    return isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name

def derive_launcher(source_dir,destination,new_qp,new_deriver):
    here=Path(__file__).resolve().parent
    old_path=here/'launch_full_phi_all_rows_soc.py'
    prior_deriver=here/'derive_full_phi_all_rows_soc.py'
    for p,d in ((old_path,PREVIOUS_LAUNCHER_SHA),(prior_deriver,PREVIOUS_DERIVER_SHA),
                (new_qp,NEW_QP_SHA),(new_deriver,NEW_DERIVER_SHA)):
        if sha(p)!=d:raise ValueError('The declared v5 source dependency changed: '+str(p))
    spec=importlib.util.spec_from_file_location('v5_previous_allrow_launcher',old_path)
    old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)
    destination=Path(destination)
    prior_path=destination.with_name('published-all-row-SOC-launcher.py')
    prior=old.derive_launcher(source_dir,prior_path,here/'full_phi_all_rows_soc.py',prior_deriver)
    tree=ast.parse(prior_path.read_text())
    counts=dict(deriver_SHA=0,deriver_default=0,QP_default=0,QP_guard=0,v3_path=0,plan=0)
    lineage=dict(schema='complete-all-row-launcher-to-face-metric-PCG-v5',
        derivation_source_sha256=sha(__file__),previous_all_row_launcher=prior,
        actual_v5_source=record(new_qp),actual_deriver=record(new_deriver),
        old_or_new_parent_body_binding_retained=True,same_original_v3_fallback_source=True,
        same_model_norm_all_positions_and_true_acceptance=True,
        no_automatic_iteration_limit_success=True,scientific_execution_performed_by_deriver=False)
    class Change(ast.NodeTransformer):
        def visit_Assign(self,node):
            if assigned(node,'DERIVER_SHA'):
                if not isinstance(node.value,ast.Constant) or node.value.value!=PREVIOUS_DERIVER_SHA:
                    raise ValueError('The all-row deriver SHA site changed')
                node.value=ast.Constant(NEW_DERIVER_SHA);counts['deriver_SHA']+=1
            if assigned(node,'deriver_path'):
                for value in ast.walk(node.value):
                    if isinstance(value,ast.Constant) and value.value==str(prior_deriver.resolve()):
                        value.value=str(Path(new_deriver).resolve());counts['deriver_default']+=1
            if (isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Attribute)
                    and isinstance(node.targets[0].value,ast.Name) and node.targets[0].value.id=='a'
                    and node.targets[0].attr=='qp_source'):
                for value in ast.walk(node.value):
                    if isinstance(value,ast.Constant) and value.value=='fullspace_feasible_active_pcg_v4.py':
                        value.value=str(Path(new_qp).resolve());counts['QP_default']+=1
            if assigned(node,'v3_fallback_source'):
                node.value=ast.parse("source_dir/'fullspace_feasible_active_cg_v3.py'",mode='eval').body
                counts['v3_path']+=1
            if assigned(node,'plan') and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict':
                keys={k.arg for k in node.value.keywords}
                if {'all_rows_soc_launcher_derivation','derived_driver','full_scientific_command'}<=keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema':kw.value=ast.Constant('actual-complete-parent-to-all-row-SOC-face-PCG-v5')
                        if kw.arg=='source_and_model_transitions':
                            kw.value=ast.Constant('Same physical model, original QP and global B; explicit all-row SOC and constrained-face PCG v5, with all old/new parent bodies fully bound.')
                    node.value.keywords.append(ast.keyword(arg='face_pcg_launcher_derivation',value=ast.Name(id='FACE_PCG_LAUNCHER_LINEAGE',ctx=ast.Load())))
                    counts['plan']+=1
            return self.generic_visit(node)
        def visit_FunctionDef(self,node):
            if node.name=='main':
                # Only the live runtime component-binding tuple is changed;
                # earlier immutable generation provenance remains historical.
                for st in node.body:
                    if isinstance(st,ast.For) and isinstance(st.target,ast.Tuple):
                        names=[x.id for x in st.target.elts if isinstance(x,ast.Name)]
                        if names==['role','path','digest']:
                            for value in ast.walk(st.iter):
                                if isinstance(value,ast.Constant) and value.value==OLD_QP_SHA:
                                    value.value=NEW_QP_SHA;counts['QP_guard']+=1
            return self.generic_visit(node)
    tree=Change().visit(tree)
    expected=dict(deriver_SHA=1,deriver_default=1,QP_default=1,QP_guard=1,v3_path=1,plan=1)
    if counts!=expected:raise ValueError('Exact v5 continuation sites changed: '+repr(counts))
    lineage['exact_edit_counts']=counts
    pos=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos]=ast.parse('FACE_PCG_LAUNCHER_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree);compile(tree,str(destination),'exec')
    text='#!/usr/bin/env python3\n# Explicit all-row SOC plus constrained-face PCG v5 continuation.\n'+ast.unparse(tree)+'\n'
    if destination.exists() and destination.read_text()!=text:raise FileExistsError('Use a fresh v5 launcher destination')
    destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(text)
    return dict(**record(destination),derivation=lineage,scientific_execution_performed=False)

def main():
    if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
        print(__doc__);return
    p=argparse.ArgumentParser(add_help=False)
    for name in ('repo','work','outdir'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--face-qp-source',type=Path);p.add_argument('--face-deriver',type=Path)
    p.add_argument('--prepare-source-only',action='store_true');a,_=p.parse_known_args()
    here=Path(__file__).resolve().parent
    qp=(a.face_qp_source or here/'fullspace_feasible_active_pcg_v5.py').resolve()
    deriver=(a.face_deriver or here/'derive_full_phi_face_pcg.py').resolve()
    source_dir=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    out=a.work.resolve()/(a.outdir.resolve().name+'-continuation-inputs')/'launch-face-PCG-v5.py'
    result=derive_launcher(source_dir,out,qp,deriver)
    if a.prepare_source_only:print(json.dumps(result,indent=2));return
    forwarded=list(sys.argv[1:])
    for flag in ('--face-qp-source','--face-deriver'):
        if flag in forwarded:
            i=forwarded.index(flag);del forwarded[i:i+2]
    if '--prepare-source-only' in forwarded:forwarded.remove('--prepare-source-only')
    returned=subprocess.run([sys.executable,result['path'],*forwarded])
    raise SystemExit(returned.returncode)
if __name__=='__main__':main()
