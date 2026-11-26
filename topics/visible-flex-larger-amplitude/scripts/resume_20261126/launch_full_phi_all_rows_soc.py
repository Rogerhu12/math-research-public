#!/usr/bin/env python3
"""Continue the actual complete PCG/SOC parent with all-original-row SOC.

Forward the same actual --parent-report/--parent-source/--bundle/--carrier,
R671 --node-report/--scalar-input, every --manifest, and explicit --soc-tau.
The old source/body/model/mu/position binding is retained through a complete
new binder, which accepts exactly published old or explicitly new parents.

Extra flags: --all-rows-helper PATH, --all-rows-deriver PATH,
--prepare-source-only (stdlib source generation only).
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

OLD_LAUNCHER_SHA='3f1516c0997cc0bd2eeafbe1f9b9e1646380904ac2c055440c6e668129383e36'
OLD_COMPOSITE_SHA='40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e'
OLD_HELPER_SHA='5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
NEW_HELPER_SHA='a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
NEW_DERIVER_SHA='94ea77107305c058425877a3ff93cf7e8b58575e982f5ca6c1040a32279a0f73'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def file_record(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def assigned(node,name):
    return (isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name)

def derive_launcher(source_dir,destination,new_helper,new_deriver):
    source_dir=Path(source_dir).resolve()
    old_path=source_dir/'launch_full_phi_coarse_pcg_soc.py'
    for p,d in ((old_path,OLD_LAUNCHER_SHA),(new_helper,NEW_HELPER_SHA),(new_deriver,NEW_DERIVER_SHA)):
        if sha(p)!=d:
            raise ValueError('A declared complete source identity changed: '+str(p))
    spec=importlib.util.spec_from_file_location('all_rows_SOC_old_launcher_deriver',old_path)
    old=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=old
    spec.loader.exec_module(old)
    destination=Path(destination)
    previous_path=destination.with_name('published-complete-PCG-SOC-launcher.py')
    previous=old.derive_launcher(source_dir/'launch_full_phi_parent_row_soc.py',previous_path,
        source_dir/'derive_full_phi_coarse_pcg_soc.py')
    tree=ast.parse(previous_path.read_text())
    counts=dict(helper_SHA=0,deriver_SHA=0,helper_default=0,deriver_default=0,plan=0)
    lineage=dict(schema='published-complete-PCG-SOC-launcher-to-all-row-SOC-v1',
        derivation_source_sha256=sha(__file__),published_launcher_derivation=previous,
        new_helper=file_record(new_helper),new_deriver=file_record(new_deriver),
        old_parent_source_and_model_validation_retained=True,
        new_parent_full_body_validation_explicit=True,
        same_all_positions_and_damping_replay=True,
        scientific_execution_performed_by_deriver=False)
    class Change(ast.NodeTransformer):
        def visit_Assign(self,node):
            if assigned(node,'HELPER_SHA'):
                if not isinstance(node.value,ast.Constant) or node.value.value!=OLD_HELPER_SHA:
                    raise ValueError('Old launcher helper SHA anchor changed')
                node.value=ast.Constant(NEW_HELPER_SHA);counts['helper_SHA']+=1
            if assigned(node,'DERIVER_SHA'):
                if not isinstance(node.value,ast.Constant) or node.value.value!=OLD_COMPOSITE_SHA:
                    raise ValueError('Old launcher composite SHA anchor changed')
                node.value=ast.Constant(NEW_DERIVER_SHA);counts['deriver_SHA']+=1
            for name,old_name,new_path,key in (
                ('helper_path','full_phi_parent_row_soc.py',new_helper,'helper_default'),
                ('deriver_path','derive_full_phi_coarse_pcg_soc.py',new_deriver,'deriver_default')):
                if assigned(node,name):
                    for value in ast.walk(node.value):
                        if isinstance(value,ast.Constant) and value.value==old_name:
                            value.value=str(Path(new_path).resolve());counts[key]+=1
            if assigned(node,'plan') and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict':
                keys={k.arg for k in node.value.keywords}
                if {'pcg_soc_launcher_derivation','full_scientific_command','derived_driver'}<=keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema':
                            kw.value=ast.Constant('actual-complete-parent-to-all-row-constrained-SOC-v2')
                        if kw.arg=='source_and_model_transitions':
                            kw.value=ast.Constant('Same physical model and exact published PCG. Old parent or new parent is fully bound; only the explicitly identified all-row SOC helper changes.')
                    node.value.keywords.append(ast.keyword(arg='all_rows_soc_launcher_derivation',
                        value=ast.Name(id='ALL_ROWS_SOC_LAUNCHER_LINEAGE',ctx=ast.Load())))
                    counts['plan']+=1
            return self.generic_visit(node)
    tree=Change().visit(tree)
    expected=dict(helper_SHA=1,deriver_SHA=1,helper_default=1,deriver_default=1,plan=1)
    if counts!=expected:
        raise ValueError('Complete all-row launcher sites changed: '+repr(counts))
    lineage['exact_edit_counts']=counts
    pos=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos]=ast.parse('ALL_ROWS_SOC_LAUNCHER_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree)
    compile(tree,str(destination),'exec')
    text='#!/usr/bin/env python3\n# Explicit complete all-row SOC continuation launcher.\n'+ast.unparse(tree)+'\n'
    if destination.exists() and destination.read_text()!=text:
        raise FileExistsError('Use a fresh launcher destination for different bytes')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(text)
    return dict(**file_record(destination),derivation=lineage,scientific_execution_performed=False)

def main():
    if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
        print(__doc__)
        print('Same complete old launcher CLI; --repo --work --outdir are always required.')
        return
    p=argparse.ArgumentParser(add_help=False)
    for flag in ('repo','work','outdir'):
        p.add_argument('--'+flag,type=Path,required=True)
    p.add_argument('--all-rows-helper',type=Path)
    p.add_argument('--all-rows-deriver',type=Path)
    p.add_argument('--prepare-source-only',action='store_true')
    a,_=p.parse_known_args()
    source_dir=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    here=Path(__file__).resolve().parent
    helper=(a.all_rows_helper or here/'full_phi_all_rows_soc.py').resolve()
    deriver=(a.all_rows_deriver or here/'derive_full_phi_all_rows_soc.py').resolve()
    destination=a.work.resolve()/(a.outdir.resolve().name+'-continuation-inputs')/'launch-all-row-SOC.py'
    derived=derive_launcher(source_dir,destination,helper,deriver)
    if a.prepare_source_only:
        print(json.dumps(derived,indent=2))
        return
    forwarded=list(sys.argv[1:])
    for flag in ('--all-rows-helper','--all-rows-deriver'):
        if flag in forwarded:
            i=forwarded.index(flag);del forwarded[i:i+2]
    if '--prepare-source-only' in forwarded:
        forwarded.remove('--prepare-source-only')
    returned=subprocess.run([sys.executable,derived['path'],*forwarded])
    raise SystemExit(returned.returncode)

if __name__=='__main__':
    main()
