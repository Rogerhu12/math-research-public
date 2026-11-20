#!/usr/bin/env python3
"""Strict small launcher adaptation: actual parent -> current coarse PCG + SOC.

Forwards the published SOC launcher's CLI (including --model, actual parent
report/bundle/carrier, every --manifest, R671 node/scalar inputs, and explicit
--soc-tau). Defaults remain one direction, 256 advances, atol=0. The only
solver selection added here is the frozen v4 with the declared coarse SPD.
beta is fixed by the augmenter to 1/(this actual direction damping)^2.

The old SOC launcher is not edited. A complete AST-derived copy changes only
the composite deriver identity/default path, adds the two component paths,
binds the explicit v4/fallback sources, and appends enabled PCG driver flags.
Its existing actual-parent/model/mu/all-position and Actions-only machinery
is retained. Future pure SOC and composite parents use the composite
deriver's explicit whole-body source binding, never a changed parent report.

Extra preparation options: --launcher-base PATH and --prepare-source-only.
--print-command retains the complete stdlib preparation mode with no arrays.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


BASE_LAUNCHER_SHA = '9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a'
COMPOSITE_DERIVER_SHA = '40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e'
AUGMENTER_SHA = 'f96cb48933d1356b97b5a687d25cc05cd33188b08c14cd0b439f170b027fce18'
COMPONENTS = {
    'coarse_frame': ('full_phi_coarse_frame.py',
        '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da'),
    'coarse_moments': ('full_phi_coarse_moments.py',
        'da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719'),
    'qp': ('fullspace_feasible_active_pcg_v4.py',
        'dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b'),
    'coarse_qp_v3': ('fullspace_feasible_active_cg_v3.py',
        'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'),
}
EXPECTED_EDITS = dict(composite_deriver_SHA=1,component_arguments=1,
    composite_deriver_default=1,component_binding=1,enabled_driver_flags=1,
    composite_plan_identity=1,actual_return_status=1)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def file_record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def _same(a,b):
    return ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)


def _assigned(node,name):
    return (isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name)


def derive_launcher(base,destination,composite_deriver):
    if sha(base)!=BASE_LAUNCHER_SHA or sha(composite_deriver)!=COMPOSITE_DERIVER_SHA:
        raise ValueError('Use the exact published SOC launcher and complete composite body deriver')
    tree=ast.parse(Path(base).read_text(),filename=str(base))
    lineage=dict(schema='exact-SOC-launcher-to-complete-coarse-PCG-SOC-v1',
        source_sha256=sha(__file__),frozen_SOC_launcher_sha256=BASE_LAUNCHER_SHA,
        complete_composite_deriver_sha256=COMPOSITE_DERIVER_SHA,
        coarse_PCG_augmentation_sha256=AUGMENTER_SHA,
        numerical_component_sha256s={role:value[1] for role,value in COMPONENTS.items()},
        edit_sites=EXPECTED_EDITS,
        actual_parent_report_not_edited=True,complete_body_source_binding_retained=True,
        original_objective_mother_norm_and_all_permanent_points_retained=True,
        preconditioner_enabled_explicitly=True,
        background_inverse_scale='1/(actual direction damping)^2',
        SOC_tau_remains_explicit=True,preconditioner_success_not_presumed=True)
    counts={key:0 for key in EXPECTED_EDITS}
    binding='''
pcg_components = {}
a.coarse_frame_source = (a.coarse_frame_source or source_dir/'full_phi_coarse_frame.py').resolve()
a.coarse_moments_source = (a.coarse_moments_source or source_dir/'full_phi_coarse_moments.py').resolve()
a.qp_source = (a.qp_source or source_dir/'fullspace_feasible_active_pcg_v4.py').resolve()
v3_fallback_source = a.qp_source.with_name('fullspace_feasible_active_cg_v3.py')
for role,path,digest in (
    ('coarse_frame',a.coarse_frame_source,FRAME_SHA),
    ('coarse_moments',a.coarse_moments_source,MOMENTS_SHA),
    ('qp',a.qp_source,PCG_SHA),
    ('coarse_qp_v3',v3_fallback_source,V3_SHA)):
    required_sha(path,digest,'complete coarse-PCG '+role)
    pcg_components[role]=file_record(path)
'''
    for key,role in (('FRAME_SHA','coarse_frame'),('MOMENTS_SHA','coarse_moments'),
                     ('PCG_SHA','qp'),('V3_SHA','coarse_qp_v3')):
        binding=binding.replace(key,repr(COMPONENTS[role][1]))

    class Transform(ast.NodeTransformer):
        def visit_Assign(self,node):
            node=self.generic_visit(node)
            if _assigned(node,'DERIVER_SHA'):
                if not isinstance(node.value,ast.Constant) or node.value.value!='805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a':
                    raise ValueError('Unknown frozen SOC launcher deriver anchor')
                node.value=ast.Constant(COMPOSITE_DERIVER_SHA)
                counts['composite_deriver_SHA']+=1
            if _assigned(node,'deriver_path'):
                hits=0
                for child in ast.walk(node.value):
                    if isinstance(child,ast.Constant) and child.value=='derive_full_phi_parent_row_soc.py':
                        child.value='derive_full_phi_coarse_pcg_soc.py';hits+=1
                if hits!=1:
                    raise ValueError('Unknown frozen SOC deriver default path')
                counts['composite_deriver_default']+=1
            if (_assigned(node,'plan') and isinstance(node.value,ast.Call)
                    and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict'):
                keys={kw.arg for kw in node.value.keywords}
                if {'schema','derived_driver','full_scientific_command','tau'} <= keys:
                    for kw in node.value.keywords:
                        if kw.arg=='schema':
                            kw.value=ast.Constant('actual-full-Phi-parent-to-current-coarse-PCG-and-SOC-v1')
                    node.value.keywords.extend([
                        ast.keyword(arg='pcg_soc_launcher_derivation',value=ast.Name(id='PCG_SOC_LAUNCHER_LINEAGE',ctx=ast.Load())),
                        ast.keyword(arg='coarse_preconditioner_components',value=ast.Name(id='pcg_components',ctx=ast.Load())),
                        ast.keyword(arg='coarse_preconditioner_enabled',value=ast.Constant(True)),
                        ast.keyword(arg='coarse_preconditioner_beta_rule',value=ast.Constant('1/(actual direction damping)^2'))])
                    counts['composite_plan_identity']+=1
            return node
        def visit_Expr(self,node):
            node=self.generic_visit(node)
            call=node.value
            if (isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute)
                    and isinstance(call.func.value,ast.Name) and call.func.value.id=='command'
                    and call.func.attr=='extend' and len(call.args)==1
                    and isinstance(call.args[0],ast.List)
                    and any(isinstance(v,ast.Constant) and v.value=='--soc-tau' for v in call.args[0].elts)):
                counts['enabled_driver_flags']+=1
                return [node]+ast.parse("command.extend(['--enable-coarse-preconditioner', '--coarse-frame-source', str(a.coarse_frame_source), '--coarse-moments-source', str(a.coarse_moments_source)])").body
            if (isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute)
                    and isinstance(call.func.value,ast.Name) and call.func.value.id=='result'
                    and call.func.attr=='update' and any(k.arg=='accepted_SOC_directions' for k in call.keywords)):
                call.keywords.extend([
                    ast.keyword(arg='actual_coarse_preconditioner_setup',value=ast.parse("outcome.get('coarse_preconditioner_setup')",mode='eval').body),
                    ast.keyword(arg='actual_coarse_preconditioner_directions',value=ast.parse("[dict(index=v['index'],preconditioner=v.get('coarse_preconditioner'),qp_schema=v.get('qp',{}).get('schema'),qp_status=v.get('qp',{}).get('status')) for v in outcome.get('directions',[])]",mode='eval').body)])
                counts['actual_return_status']+=1
            return node
        def visit_FunctionDef(self,node):
            node=self.generic_visit(node)
            if node.name!='main':
                return node
            new=[]
            for st in node.body:
                if (_assigned(st,'a') and isinstance(st.value,ast.Call)
                        and isinstance(st.value.func,ast.Attribute) and st.value.func.attr=='parse_args'):
                    new.extend(ast.parse("p.add_argument('--coarse-frame-source',type=Path)\np.add_argument('--coarse-moments-source',type=Path)").body)
                    counts['component_arguments']+=1
                new.append(st)
                if _assigned(st,'source_dir'):
                    new.extend(ast.parse(binding).body)
                    counts['component_binding']+=1
            node.body=new
            return node
    tree=ast.fix_missing_locations(Transform().visit(tree))
    if counts!=EXPECTED_EDITS:
        raise ValueError('The frozen SOC launcher edit sites changed: '+repr(counts))
    pos=1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos]=ast.parse('PCG_SOC_LAUNCHER_LINEAGE = '+repr(lineage)).body
    tree=ast.fix_missing_locations(tree)
    compile(tree,str(base)+'-complete-PCG-SOC-launcher','exec')
    text=('#!/usr/bin/env python3\n# Exact source-derived complete coarse-PCG plus SOC launcher.\n'
          +ast.unparse(tree)+'\n')
    destination=Path(destination)
    if destination.exists() and destination.read_text()!=text:
        raise FileExistsError('Use a fresh composite launcher destination for different bytes')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(text)
    return dict(**file_record(destination),derivation=lineage,
                source_preparation_only=True,scientific_execution_performed=False)


def main():
    if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
        print(__doc__)
        print('Required forwarded arguments: --repo --work --outdir --model --parent-report --bundle --carrier --manifest --soc-tau.')
        print('R671 additionally requires --node-report --scalar-input. Use --parent-source for a derived parent. --print-command reads metadata only.')
        return
    p=argparse.ArgumentParser(add_help=False)
    for flag in ('repo','work','outdir'):
        p.add_argument('--'+flag,type=Path,required=True)
    p.add_argument('--soc-deriver',type=Path)
    p.add_argument('--launcher-base',type=Path)
    p.add_argument('--prepare-source-only',action='store_true')
    a,_=p.parse_known_args()
    source_dir=a.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    base=(a.launcher_base or source_dir/'launch_full_phi_parent_row_soc.py').resolve()
    composite=(a.soc_deriver or source_dir/'derive_full_phi_coarse_pcg_soc.py').resolve()
    destination=a.work.resolve()/(a.outdir.resolve().name+'-continuation-inputs')/'launch-complete-coarse-PCG-SOC.py'
    derived=derive_launcher(base,destination,composite)
    if a.prepare_source_only:
        print(json.dumps(derived,indent=2))
        return
    forwarded=list(sys.argv[1:])
    if '--launcher-base' in forwarded:
        i=forwarded.index('--launcher-base');del forwarded[i:i+2]
    if '--prepare-source-only' in forwarded:
        forwarded.remove('--prepare-source-only')
    returned=subprocess.run([sys.executable,derived['path'],*forwarded])
    raise SystemExit(returned.returncode)


if __name__=='__main__':
    main()
