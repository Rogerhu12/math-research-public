#!/usr/bin/env python3
"""Derive the complete R684 design driver with R688 moments and R685 PCG.

Only stdlib source parsing/compilation occurs here. The whole frozen base
body is retained except the declared setup, QP call, bookkeeping and the
optional R687 scalar-statistics selection. No scientific driver is imported.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path


SCHEMA='R688-complete-mean-metric-face-PCG-driver-derivation-v1'
BASE_SHA='2d44a097e614f917fa133b1042e0fc7c6cdcb32a10b72d1bc2ac6362d54a94c3'
EXPECTED={
    'mean_coarse':'9e7ca6ba0cf3821ab8498226354d8422c2cfacee1ef07dafb8fc5868968fb9e3',
    'coarse_frame':'324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da',
    'coarse_qp_v3':'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4',
    'qp':'76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8',
    'mean_transform':'b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624',
    'spectral_hessian':'29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    'spectral':'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91',
}
CENTERED_SHA='5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def statements(text):
    return ast.parse(text).body


def assigned(node,name):
    return (isinstance(node,ast.Assign) and len(node.targets)==1
        and isinstance(node.targets[0],ast.Name) and node.targets[0].id==name)


SETUP='''
def _mean_coarse_sources(args, paths):
    if args.objective != 'spectral':
        raise ValueError('R688 consumes the declared current spectral mean-metric bridge')
    if args.coarse_moment_stage_block < 1:
        raise ValueError('Use a positive mean-moment radial block size')
    paths.update(mean_coarse=args.mean_coarse_source.resolve(),
        coarse_frame=args.coarse_frame_source.resolve(),
        coarse_qp_v3=args.coarse_v3_source.resolve())
    records={}
    for role,digest in MEAN_COARSE_EXPECTED_SOURCES.items():
        path=paths[role]
        if not path.is_file() or path.stat().st_size>100000 or sha(path)!=digest:
            raise ValueError('Unexpected R688 source identity: '+role)
        records[role]=dict(path=str(path),sha256=digest,bytes=path.stat().st_size)
    frame=load('R688_complete_original_coarse_frame',paths['coarse_frame'])
    moments=load('R688_complete_current_mean_coarse_moments',paths['mean_coarse'])
    centered=None
    if args.centered_loss_source is not None:
        paths['centered_loss']=args.centered_loss_source.resolve()
        if sha(paths['centered_loss'])!=MEAN_CENTERED_SOURCE_SHA:
            raise ValueError('The optional centered statistic source differs from R687')
        centered=load('R688_optional_R687_centered_statistics',paths['centered_loss'])
        records['centered_loss']=dict(path=str(paths['centered_loss']),
            sha256=MEAN_CENTERED_SOURCE_SHA,bytes=paths['centered_loss'].stat().st_size)
    selected='centered_phi_normalized' if centered is not None else 'phi_normalized'
    return frame,moments,centered,selected,dict(
        schema='R688-current-mean-coarse-face-PCG-source-binding-v1',
        source_records=records,mean_moment_stage_block=args.coarse_moment_stage_block,
        all_mean_normalization_derivatives_retained=True,
        material_weight_chain_retained_in_full_J=True,
        coarse_zero_core_contract_checked_by_bound_source=True,
        no_old_target_Gram_used=True,
        selected_scalar_objective_key=selected,
        same_Phi_up_to_fixed_constant=centered is not None,
        original_phi_normalized_field_retained=True,
        true_gradient_Hessian_and_damping_units_unchanged=True,
        near_zero_unit_rescaling_used=False,
        small_SPD_or_declared_coarse_layout_unavailable='Explicit original full-mean v3 solve before any PCG iteration',
        within_PCG_application_failure='Truthful v5 truncated status; no automatic retry or metric replacement',
        expected_extra_J_calls=0,actual_extra_J_calls_not_yet_measured=True)
'''

BEFORE_SOLVE='''
mean_parent_sha=next((item['accepted_bundle_sha256'] for item in reversed(report['directions'])
    if item.get('accepted') and item.get('accepted_bundle_sha256')),report['bundle_sha256'])
mean_provenance=dict(direction=index,parent_bundle_sha256=mean_parent_sha,
    mean_averaging=args.mean_averaging,
    current_spectral_parameters=dict(p=spectral_parameters.p,
        epsilon=spectral_parameters.epsilon,scale=spectral_parameters.scale),
    selected_scalar_objective_key=mean_objective_key,
    whole_driver_derivation=report['mean_coarse_driver_derivation'])
mean_outer_counts_before=counts.copy()
mean_preconditioner,mean_preconditioner_detail=mean_moments_module.prepare_current_mean_preconditioner(
    mean_frame_module,coordinates,height_map,basis,coarse_diagonal,coarse_chol,
    bridge,damping,stage_block=args.coarse_moment_stage_block,
    provenance=mean_provenance,
    progress=lambda value:event(direction=index,**value))
mean_preconditioner_detail['outer_A_entry_counts_during_preparation']={
    key:counts[key]-mean_outer_counts_before[key] for key in counts}
mean_preconditioner_kwargs=dict(preconditioner=mean_preconditioner,
    preconditioner_metadata=mean_preconditioner_detail.get('fixed_metadata',mean_preconditioner_detail),
    v3_source=paths['coarse_qp_v3'])
event(event='mean_metric_current_preconditioner_prepared',direction=index,
    status=mean_preconditioner_detail['status'],
    seconds=mean_preconditioner_detail['construction_seconds'],
    actual_operator_entry_calls=mean_preconditioner_detail['actual_operator_entry_calls'],
    fallback_to_v3=mean_preconditioner_detail.get('fallback_to_frozen_v3'))
'''

AFTER_SOLVE='''
mean_preconditioner_detail['actual_QP_schema']=qp_report.get('schema')
mean_preconditioner_detail['actual_QP_status']=qp_report.get('status')
mean_preconditioner_detail['automatic_retry_or_changed_target']=False
mean_preconditioner_kwargs.clear()
mean_preconditioner=None
mean_preconditioner_detail['frame_and_factor_released_after_solve']=True
'''


class MeanFaceDriver(ast.NodeTransformer):
    def __init__(self,lineage):
        self.lineage=lineage
        self.counts=dict(cli=0,paths=0,report=0,record=0,solve=0,statistics=0,objective=0)

    def visit_Expr(self,node):
        node=self.generic_visit(node)
        call=node.value
        if (isinstance(call,ast.Call) and isinstance(call.func,ast.Attribute)
                and call.func.attr=='add_argument' and call.args
                and isinstance(call.args[0],ast.Constant) and call.args[0].value=='--target'):
            self.counts['cli']+=1
            return [node]+statements('''
parser.add_argument('--mean-coarse-source',type=Path,required=True)
parser.add_argument('--coarse-frame-source',type=Path,required=True)
parser.add_argument('--coarse-v3-source',type=Path,required=True)
parser.add_argument('--coarse-moment-stage-block',type=int,default=8)
parser.add_argument('--centered-loss-source',type=Path)
''')
        return node

    def visit_FunctionDef(self,node):
        if node.name=='objective_value':
            self.counts['objective']+=1
            return statements('''
def objective_value(stats):
    return (stats['spectral'][mean_objective_key] if args.objective=='spectral'
        else stats['radial_weighted_mean_sse'])
''')[0]
        return self.generic_visit(node)

    def visit_Assign(self,node):
        node=self.generic_visit(node)
        if assigned(node,'paths') and isinstance(node.value,ast.DictComp):
            self.counts['paths']+=1
            return [node]+statements('''
mean_frame_module,mean_moments_module,centered_loss_module,mean_objective_key,mean_coarse_binding=\
    _mean_coarse_sources(args,paths)
''')
        if assigned(node,'report'):
            self.counts['report']+=1
            if not isinstance(node.value,ast.Call) or not isinstance(node.value.func,ast.Name) or node.value.func.id!='dict':
                raise ValueError('The base full report is no longer a literal dict')
            for keyword in node.value.keywords:
                if keyword.arg=='schema':
                    keyword.value=ast.Constant('R688-fullclosed-rotational-mean-metric-face-PCG-v1')
            node.value.keywords.extend([
                ast.keyword(arg='mean_coarse_driver_derivation',value=ast.parse(repr(self.lineage),mode='eval').body),
                ast.keyword(arg='mean_coarse_source_binding',value=ast.Name('mean_coarse_binding',ast.Load())),
                ast.keyword(arg='selected_scalar_objective_key',value=ast.Name('mean_objective_key',ast.Load())),
            ])
        if assigned(node,'record') and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='dict':
            self.counts['record']+=1
            node.value.keywords.append(ast.keyword(arg='mean_coarse_preconditioner',
                value=ast.Name('mean_preconditioner_detail',ast.Load())))
        target=node.targets[0] if len(node.targets)==1 else None
        if (isinstance(target,ast.Subscript) and isinstance(target.value,ast.Name)
                and target.value.id=='result' and isinstance(target.slice,ast.Constant)
                and target.slice.value=='spectral'):
            self.counts['statistics']+=1
            return [node]+statements('''
if centered_loss_module is not None:
    result['spectral']=centered_loss_module.augment_statistics(raw,stage_weights,
        problem.multiplicity,spectral_parameters,result['spectral'],stage_block=args.stage_block)
''')
        if (isinstance(target,ast.Tuple) and [v.id if isinstance(v,ast.Name) else None for v in target.elts]==['coordinate_step','qp_report']):
            self.counts['solve']+=1
            if (not isinstance(node.value,ast.Call) or not isinstance(node.value.func,ast.Attribute)
                    or not isinstance(node.value.func.value,ast.Name)
                    or node.value.func.value.id!='qp_module' or node.value.func.attr!='solve'):
                raise ValueError('The base QP invocation changed')
            node.value.keywords.append(ast.keyword(arg=None,value=ast.Name('mean_preconditioner_kwargs',ast.Load())))
            return statements(BEFORE_SOLVE)+[node]+statements(AFTER_SOLVE)
        return node


def derive(repo,base_source=None):
    repo=Path(repo).resolve()
    default=repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_mean_metric_design_qp.py'
    base=Path(base_source).resolve() if base_source else default
    if sha(base)!=BASE_SHA:
        raise ValueError('The complete R684 mean driver is not the frozen v3/exact-position version')
    lineage=dict(schema=SCHEMA,base_driver_sha256=BASE_SHA,
        source_deriver_sha256=sha(__file__),expected_runtime_source_sha256=EXPECTED,
        optional_centered_statistics_sha256=CENTERED_SHA,
        whole_base_body_retained=True,
        current_mean_target_changed=False,original_free_variables_changed=False,
        physical_norm_or_geometry_rows_changed=False,
        optional_centered_loss_is_only_fixed_constant_subtraction=True,
        new_current_mean_coarse_Gram=True,face_metric='R685 constrained inverse',
        new_scientific_execution_by_deriver=False)
    tree=ast.parse(base.read_text(),filename=str(base))
    transform=MeanFaceDriver(lineage)
    tree=transform.visit(tree)
    if any(value!=1 for value in transform.counts.values()):
        raise ValueError('The complete base edit sites changed: '+repr(transform.counts))
    insert=0
    if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant):
        insert=1
    while insert<len(tree.body) and isinstance(tree.body[insert],(ast.Import,ast.ImportFrom)):
        insert+=1
    tree.body[insert:insert]=statements('MEAN_COARSE_EXPECTED_SOURCES='+repr(EXPECTED)+'\nMEAN_CENTERED_SOURCE_SHA='+repr(CENTERED_SHA)+'\n'+SETUP)
    tree=ast.fix_missing_locations(tree)
    compile(tree,'<R688-complete-mean-face-driver>','exec')
    body=ast.unparse(tree)+'\n'
    text='#!/usr/bin/env python3\n# Complete R688 source derivation:\n# '+json.dumps(lineage,sort_keys=True)+'\n'+body
    return text,dict(**lineage,edit_site_counts=transform.counts,
        derived_driver_sha256=hashlib.sha256(text.encode()).hexdigest(),
        complete_AST_sha256=hashlib.sha256(ast.dump(ast.parse(body),include_attributes=False).encode()).hexdigest())


def bind_report(report,driver,repo,base_source=None):
    actual=Path(driver).resolve()
    if report.get('schema')!='R688-fullclosed-rotational-mean-metric-face-PCG-v1':
        raise ValueError('Need the actual R688 mean-face report')
    if sha(actual)!=report.get('source_sha256'):
        raise ValueError('The report source differs from its actual complete driver')
    expected,record=derive(repo,base_source)
    if actual.read_text()!=expected:
        raise ValueError('The complete driver differs from the frozen-body R688 derivation')
    if report.get('mean_coarse_driver_derivation')!=json.loads(expected.splitlines()[2][2:]):
        raise ValueError('The report lineage differs from the complete derived body')
    roles=report.get('source_sha256_by_role',{})
    for role,digest in EXPECTED.items():
        if roles.get(role)!=digest:
            raise ValueError('The actual runtime component identity differs: '+role)
    if report.get('selected_scalar_objective_key')=='centered_phi_normalized':
        if roles.get('centered_loss')!=CENTERED_SHA:
            raise ValueError('The selected centered target has no matching R687 helper')
    return dict(complete_report_and_source_binding=True,**record)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--base-source',type=Path)
    a=p.parse_args()
    text,record=derive(a.repo,a.base_source)
    if a.out.exists():
        raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(text)
    print(json.dumps(record,sort_keys=True))


if __name__=='__main__':
    main()
