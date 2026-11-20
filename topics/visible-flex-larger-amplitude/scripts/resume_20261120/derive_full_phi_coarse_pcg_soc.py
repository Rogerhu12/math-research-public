#!/usr/bin/env python3
"""Exact complete source chain: frozen driver -> locations -> SOC -> coarse PCG.

Stdlib source preparation/binding only. No numerical component is imported.
The two original drivers, exact-location source, SOC deriver/helper, and
PCG augmenter remain unchanged. Future composite parents require rebuilding
this WHOLE body and matching the actual supplied source/report SHA.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


SOC_DERIVER_SHA = '805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a'
SOC_HELPER_SHA = '5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
MANIFEST_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
AUGMENTER_SHA = 'f96cb48933d1356b97b5a687d25cc05cd33188b08c14cd0b439f170b027fce18'
BASES = {
    'original': ('fullclosed_gauss_inequality_qp.py',
        '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671': ('fullclosed_gauss_exact_tail_inequality_qp.py',
        'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'),
}
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
LINEAGE_SCHEMA = 'frozen-full-driver-exact-locations-SOC-current-coarse-PCG-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def text_sha(value):
    return hashlib.sha256(value.encode()).hexdigest()


def load(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def same_ast(left,right):
    return ast.dump(left,include_attributes=False) == ast.dump(right,include_attributes=False)


def bound_transforms(*,soc_deriver=None,augmenter=None):
    here = Path(__file__).resolve().parent
    soc_path = Path(soc_deriver or here/'derive_full_phi_parent_row_soc.py').resolve()
    augment_path = Path(augmenter or here/'augment_full_phi_coarse_pcg.py').resolve()
    if sha(soc_path) != SOC_DERIVER_SHA or sha(augment_path) != AUGMENTER_SHA:
        raise ValueError('Complete PCG+SOC derivation requires both exact published transformation sources')
    soc = load('complete_composite_frozen_SOC_deriver',soc_path)
    augment = load('complete_composite_frozen_coarse_PCG_augmenter',augment_path)
    return soc,augment,soc_path,augment_path


def build_ast(base,manifest_source,*,soc_deriver=None,augmenter=None):
    if sha(manifest_source) != MANIFEST_SHA:
        raise ValueError('The exact complete-history location transformation changed')
    soc,augment,soc_path,augment_path = bound_transforms(soc_deriver=soc_deriver,augmenter=augmenter)
    # SOC805 itself proves the frozen base and all earlier exact AST edits.
    soc_tree,soc_lineage,soc_edits = soc.build_ast(base,manifest_source)
    original_SOC_text = ast.unparse(soc_tree)+'\n'
    augmented_text,augmentation = augment.augment_driver_text(original_SOC_text)
    if (augmentation.get('input_text_sha256') != text_sha(original_SOC_text)
            or augmentation.get('output_text_sha256') != text_sha(augmented_text)
            or augmentation.get('augmentation_source_sha256') != AUGMENTER_SHA):
        raise ValueError('The exact coarse augmenter returned inconsistent source identities')
    expected_components = dict(frame=COMPONENTS['coarse_frame'][1],
        moments=COMPONENTS['coarse_moments'][1],PCG=COMPONENTS['qp'][1],
        frozen_v3=COMPONENTS['coarse_qp_v3'][1])
    if augmentation.get('source_sha256s') != expected_components:
        raise ValueError('The complete coarse-PCG numerical component identities changed')
    model = soc_lineage['model']
    lineage = dict(schema=LINEAGE_SCHEMA,model=model,
        composite_derivation_source_sha256=sha(__file__),
        frozen_driver_sha256=soc_lineage['frozen_driver_sha256'],
        exact_location_derivation_sha256=MANIFEST_SHA,
        SOC_derivation_source_sha256=SOC_DERIVER_SHA,SOC_helper_sha256=SOC_HELPER_SHA,
        coarse_PCG_augmentation_source_sha256=AUGMENTER_SHA,
        numerical_component_sha256s={role:value[1] for role,value in COMPONENTS.items()},
        SOC_lineage=soc_lineage,SOC_edit_sites=soc_edits,coarse_PCG_augmentation=augmentation,
        derivation_order=['frozen_complete_driver','exact_binary_complete_locations',
                          'parent_row_SOC805','current_coarse_PCG_f96','explicit_composite_identity'],
        complete_field_observations_target_step_norm_and_SOC_damping_rules_retained=True,
        arbitrary_parent_source_or_comment_header_accepted=False,
        numerical_execution_performed_by_deriver=False)
    tree = ast.parse(augmented_text)
    report_count = 0
    for node in ast.walk(tree):
        if (isinstance(node,ast.Assign) and len(node.targets)==1
                and isinstance(node.targets[0],ast.Name) and node.targets[0].id=='report'
                and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name)
                and node.value.func.id=='dict'):
            keys = {kw.arg for kw in node.value.keywords}
            if {'schema','soc_derivation','coarse_preconditioner_derivation','directions'} <= keys:
                for kw in node.value.keywords:
                    if kw.arg=='schema':
                        kw.value=ast.Constant('fullclosed-gauss-'+model+'-coarse-PCG-parent-row-SOC-v1')
                node.value.keywords.append(ast.keyword(arg='pcg_soc_derivation',
                    value=ast.Name(id='PCG_SOC_LINEAGE',ctx=ast.Load())))
                report_count += 1
    if report_count != 1:
        raise ValueError('The complete augmented report identity site changed')
    pos = 1 if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) else 0
    tree.body[pos:pos] = ast.parse('PCG_SOC_LINEAGE = '+repr(lineage)).body
    tree = ast.fix_missing_locations(tree)
    compile(tree,str(base)+'-complete-PCG-SOC','exec')
    return tree,lineage


def derive_driver(base,destination,manifest_source,*,soc_deriver=None,augmenter=None):
    tree,lineage = build_ast(base,manifest_source,soc_deriver=soc_deriver,augmenter=augmenter)
    text = ('#!/usr/bin/env python3\n'
        '# Complete authenticated frozen -> locations -> SOC -> coarse PCG source chain.\n'
        +ast.unparse(tree)+'\n')
    destination = Path(destination)
    if destination.exists() and destination.read_text()!=text:
        raise FileExistsError('Use a fresh composite driver destination for different bytes')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(text)
    return dict(path=str(destination.resolve()),sha256=sha(destination),
        bytes=destination.stat().st_size,derivation=lineage,
        transformation_sources=dict(SOC=SOC_DERIVER_SHA,coarse_PCG=AUGMENTER_SHA),
        scientific_execution_performed=False)


def bind_soc_parent(report,supplied,source_dir,manifest_source,*,soc_deriver=None,augmenter=None):
    """Compatibility API for the strict SOC launcher, with explicit dispatch.

    Pure SOC805 parents delegate to that complete binder. Composite parents
    are rebuilt through the whole new chain. Old frozen/100e parents remain
    the unmodified 18ba/425f planner's responsibility, never relabelled here.
    """
    soc,_,soc_path,augment_path = bound_transforms(soc_deriver=soc_deriver,augmenter=augmenter)
    if 'pcg_soc_derivation' not in report:
        if 'soc_derivation' not in report:
            raise ValueError('This new binder only handles explicit pure-SOC or complete PCG+SOC sources')
        return soc.bind_soc_parent(report,supplied,source_dir,manifest_source)
    if supplied is None:
        raise ValueError('A composite parent needs its actual complete source file')
    path = Path(supplied).resolve()
    if report.get('source_sha256') != sha(path):
        raise ValueError('Composite parent report does not bind the actual supplied source bytes')
    lineage = report['pcg_soc_derivation']
    if (not isinstance(lineage,dict) or lineage.get('schema')!=LINEAGE_SCHEMA
            or lineage.get('composite_derivation_source_sha256')!=sha(__file__)
            or lineage.get('SOC_derivation_source_sha256')!=SOC_DERIVER_SHA
            or lineage.get('coarse_PCG_augmentation_source_sha256')!=AUGMENTER_SHA):
        raise ValueError('Unknown composite source lineage; do not inherit a pure SOC comment header')
    model = lineage.get('model')
    if model not in BASES:
        raise ValueError('Unknown composite physical model')
    expected,expected_lineage = build_ast(Path(source_dir)/BASES[model][0],manifest_source,
        soc_deriver=soc_path,augmenter=augment_path)
    actual = ast.parse(path.read_text(),filename=str(path))
    if lineage != expected_lineage or not same_ast(expected,actual):
        raise ValueError('Actual complete parent body differs from frozen -> locations -> SOC -> PCG reconstruction')
    if (report.get('schema')!='fullclosed-gauss-'+model+'-coarse-PCG-parent-row-SOC-v1'
            or report.get('soc_derivation')!=expected_lineage['SOC_lineage']):
        raise ValueError('Actual composite report model/SOC identity differs from its proven source')
    expected_coarse_lineages = [ast.literal_eval(kw.value)
        for node in ast.walk(expected) if isinstance(node,ast.Call)
        and isinstance(node.func,ast.Name) and node.func.id=='dict'
        for kw in node.keywords if kw.arg=='coarse_preconditioner_derivation']
    if len(expected_coarse_lineages)!=1 or report.get('coarse_preconditioner_derivation')!=expected_coarse_lineages[0]:
        raise ValueError('Actual composite report does not retain its exact runtime coarse derivation')
    roles = report.get('source_sha256_by_role',{})
    if roles.get('soc') != SOC_HELPER_SHA:
        raise ValueError('Actual composite parent uses another SOC helper')
    setup = report.get('coarse_preconditioner_setup',{})
    if setup.get('enabled') is not True:
        raise ValueError('This complete PCG+SOC launcher requires the explicit enabled branch')
    for role,(_,digest) in COMPONENTS.items():
        if roles.get(role) != digest:
            raise ValueError('Actual composite numerical component differs: '+role)
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,model=model,
        declared_derivation=expected_lineage,actual_entire_body_AST_matched=True,
        inherited_original_or_SOC_parent_guard_bypassed=False,
        numerical_preconditioner_success_claimed=False,
        scope='Source/model/component identity only; per-direction preparation/application status remains actual report evidence')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',type=Path,required=True)
    p.add_argument('--manifest-source',type=Path,required=True)
    p.add_argument('--soc-deriver',type=Path)
    p.add_argument('--augmenter',type=Path)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    print(json.dumps(derive_driver(a.base,a.out,a.manifest_source,
        soc_deriver=a.soc_deriver,augmenter=a.augmenter),indent=2))


if __name__=='__main__':
    main()
