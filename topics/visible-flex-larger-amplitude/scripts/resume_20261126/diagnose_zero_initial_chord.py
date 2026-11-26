#!/usr/bin/env python3
"""Actual initial zero-input chord/meridian-length diagnostic.

This entry owns an INITIAL-INPUT binder. It does not weaken the accepted
zero-field checkpoint guards in the outward root consumer. It reads an
actual failed initial report, re-creates its exact original zero seed,
and encloses the necessary chord <= S condition without any endpoint
root, full field, residual, J, or Jtranspose evaluation.
"""
import argparse
import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import numpy as np

SCHEMA='actual-zero-initial-point-chord-necessity-v1'
TOPIC='topics/visible-flex-larger-amplitude'
PINS={
    'reference':('scripts/resume_20261126/so3_axisymmetric_reference.py','4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
    'operator':('scripts/resume_20261126/so3_axisymmetric_meridian_operator.py','7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'),
    'endpoint':('scripts/resume_20261126/so3_zero_closure_endpoint_operator.py','5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'),
    'failed_driver':('scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py','b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b'),
}
REPORT_SCHEMA='complete-independent-axisymmetric-fixed-deep-zero-closure-so3-QP-v1'
BASE_SCHEMA='complete-independent-axisymmetric-so3-meridian-with-core-lift-v1'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Actual initial input and rigorous chord checks require public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):
            h.update(block)
    return h.hexdigest()


def serial(value):
    if isinstance(value,F):
        return str(value)
    if isinstance(value,dict):
        return {k:serial(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [serial(v) for v in value]
    if hasattr(value,'tolist'):
        return serial(value.tolist())
    if isinstance(value,float) and not math.isfinite(value):
        raise ValueError('No nonfinite word can be evidence')
    return value


def canonical(value):
    return hashlib.sha256(json.dumps(serial(value),sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def load(name,path,expected):
    if sha(path)!=expected:
        raise ValueError('The complete bound source changed: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def write(path,value):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(serial(value),indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def literal_registry(path):
    values=[node.value for node in ast.parse(Path(path).read_text()).body
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS'
            for t in node.targets)]
    if len(values)!=1:
        raise ValueError('Require the exact one complete failed-driver source registry')
    return ast.literal_eval(values[0])


def actual_failure(value):
    expression=ast.parse(value,mode='eval').body
    if (not isinstance(expression,ast.Call) or not isinstance(expression.func,ast.Name)
            or expression.func.id!='EndpointRootFailure' or len(expression.args)!=1
            or expression.keywords):
        raise ValueError('Use the actual declared initial endpoint-root failure record')
    literal=ast.literal_eval(expression.args[0])
    if not isinstance(literal,str):
        raise ValueError('The actual exception record must contain its complete literal JSON')
    result=json.loads(literal)
    if (result.get('schema')!='actual-zero-closure-root-failure-v1'
            or result.get('failed_candidate_is_not_an_accepted_field') is not True):
        raise ValueError('A failed input cannot be relabeled an accepted initial field')
    return result


class ActualInitialInput:
    def __init__(self,args):
        require_actions()
        self.repo=args.repo.resolve()
        topic=self.repo/TOPIC
        paths={key:topic/relative for key,(relative,_) in PINS.items()}
        for key,path in paths.items():
            if sha(path)!=PINS[key][1]:
                raise ValueError('Changed complete initial-input source '+key)
        raw=args.failed_report.read_bytes()
        report=self.report=json.loads(raw)
        digest=hashlib.sha256(raw).hexdigest()
        if (report.get('schema')!=REPORT_SCHEMA or report.get('source_sha256')!=PINS['failed_driver'][1]
                or report.get('complete') is not False
                or report.get('stop_reason')!='actual_initial_zero_closure_field_read_failed'
                or report.get('initial') is not None or report.get('final_statistics') is not None
                or report.get('restart') is not None or report.get('direct_base_seed') is not None
                or report.get('new_zero_closure_seed_changes_physical_field') is not True):
            raise ValueError('This diagnostic binds the actual literal-zero original initial-input attempt only')
        for role,(relative,wanted) in literal_registry(paths['failed_driver']).items():
            if report['source_sha256_by_role'].get(role)!=wanted or sha(topic/relative)!=wanted:
                raise ValueError('The actual complete failed-driver role changed: '+role)
        for key,path in (('bundle_sha256',args.reference_bundle),
                ('observation_carrier_sha256',args.carrier),
                ('exact_tail_node_report_sha256',args.node_report),
                ('exact_tail_scalar_input_sha256',args.scalar_input)):
            if report.get(key)!=sha(path):
                raise ValueError('Changed actual initial reference input '+key)
        if report['independent_preparation_report']['sha256']!=sha(args.preparation_report):
            raise ValueError('Changed actual complete preparation')
        modules={key:load('_zero_chord_'+key,paths[key],PINS[key][1])
            for key in ('reference','operator','endpoint')}
        ref,op,endpoint=(modules[key] for key in ('reference','operator','endpoint'))
        working=report['working_evaluation']
        op.torch.set_num_threads(int(working['torch_threads']))
        op.torch.set_num_interop_threads(1)
        context=self.context=ref.AxisymmetricReferenceContext.from_files(repo=self.repo,
            reference_bundle=args.reference_bundle,carrier=args.carrier,node_report=args.node_report,
            scalar_input=args.scalar_input,preparation_report=args.preparation_report,panels=args.panels)
        parent,prepared=context.create_problem(N=int(report['N']),stage_block=64)
        base=self.base=op.ClosedMeridianOperator(parent,prepared,ref,
            cache_directory=args.work_directory/'unread-fixed-reference-cache',
            integration_order=int(working['integration_order']),angle_block=int(working['angle_block']),
            root_iterations=int(working['inverse_root_iterations']),
            root_tolerance=float(working['inverse_root_tolerance']),
            expected_parent_bundle_sha256=sha(args.reference_bundle))
        saved=working['endpoint_root_policy']
        policy=endpoint.EndpointPolicy(**{key:saved[key] for key in
            ('tolerance','maximum_iterations','maximum_backtracks','armijo','branch_radius')})
        if policy.metadata()!=saved:
            raise ValueError('Changed actual complete root policy')
        model=report['representation']
        q=self.q=endpoint.ZeroClosureOperator(base,
            expected_base_source_sha256=PINS['operator'][1],expected_base_schema=BASE_SCHEMA,
            bubble_nodes=working['exact_relative_bubble_nodes'],endpoint_policy=policy)
        if (q.model!=model or q.identity!=report['model_identity_sha256']
                or model['base_complete_model']!=base.model
                or model['base_model_identity_sha256']!=base.identity
                or base.model['complete_axisymmetric_reference_model']!=context.model
                or base.model['initial_reference_model_identity_sha256']!=context.identity
                or model['fixed_scalar_metric_identity_sha256']!=context.scalar_identity
                or model['fixed_scalar_profile_definition']!=context.scalar_definition
                or report['fixed_scalar_metric']['identity_sha256']!=context.scalar_identity
                or report['fixed_scalar_metric']['exact_profile_definition']!=context.scalar_definition):
            raise ValueError('The full zero/base/reference/fixed-target definitions do not agree')
        self.failure=actual_failure(report['actual_initial_read_error'])
        x=self.x=q.initial()
        q._select_point(x)
        if (self.failure['root_policy']!=saved
                or q._current_point_sha256!=self.failure['current_full_point_sha256']
                or report['latest_operator_metadata']['current_full_point_sha256']!=q._current_point_sha256):
            raise ValueError('This is not the actual original free point where the initial root failed')
        core,omega,height=q.unpack(x)
        if (not np.array_equal(core,context.core) or np.any(omega!=0)
                or height!=context.height or not np.isfinite(x).all()):
            raise ValueError('Keep the exact unchanged current=fixed core, zero omega and original H')
        x.setflags(write=False)
        self.core=tuple(F(float(v)) for v in core)
        self.height=F(height)
        self.height_float=float(height)
        self.identity=q.identity
        self.profile=context.scalar_identity
        self.d=context.modules['deep_scalar']
        self.S=(F(context.full.S[0],context.full.h.S),F(context.full.S[1],context.full.h.S))
        radius=context.model['radius_complete_enclosure']
        self.R=(F(radius['lower_exact']),F(radius['upper_exact']))
        if not 0<self.S[0]<=self.S[1] or not 0<self.R[0]<=self.R[1]:
            raise ValueError('The full exact scalar input must enclose positive S and R')
        if sha(args.failed_report)!=digest:
            raise ValueError('The actual failed report changed during binding')
        self.binding=dict(schema='actual-zero-original-initial-point-not-a-field-v1',
            source_sha256=sha(__file__),actual_failed_report=record(args.failed_report),
            actual_failed_driver_source_sha256=PINS['failed_driver'][1],
            actual_failed_driver_source_commit=report['source_commit'],
            actual_initial_point_sha256=q._current_point_sha256,
            actual_zero_model_identity_sha256=q.identity,
            actual_base_model_identity_sha256=base.identity,
            actual_reference_model_identity_sha256=context.identity,
            fixed_scalar_metric_identity_sha256=self.profile,
            fixed_scalar_profile_definition=context.scalar_definition,
            current_core_array_sha256=op.array_sha(core),
            complete_zero_omega_array_sha256=op.array_sha(omega),
            complete_core_coefficients=len(core),initial_H_hex=height.hex(),
            actual_inputs={role:record(getattr(args,role)) for role in
                ('failed_report','reference_bundle','preparation_report','carrier','node_report','scalar_input')},
            source_files={role:record(path) for role,path in paths.items()},
            complete_new_initial_field_exists=False,endpoint_root_solved_by_this_entry=False,
            failed_report_not_used_as_field_checkpoint=True,
            complete_original_free_point_reread=True,current_core_exactly_equals_fixed_chart_core=True)


class ChordEnclosure:
    def __init__(self,actual):
        self.a,self.d=actual,actual.d
        self.core=actual.core
        self.R=self.d.box(*actual.R)
        self.S=self.d.box(*actual.S)
        self.H2=self.d.box(actual.height**2)
        self.counts=dict(complete_angle_cell_enclosures=0,exact_point_enclosures=0,
            all_original_Fourier_terms_per_evaluation=len(self.core))

    def square(self,value):
        lo,hi=value
        lower=0 if lo<=0<=hi else min(lo*lo,hi*hi)
        upper=max(lo*lo,hi*hi)
        d=self.d
        return lower//d.SCALE,-((-upper)//d.SCALE)

    def as_fraction(self,value):
        return tuple(F(v,self.d.SCALE) for v in value)

    def display(self,value):
        lo,hi=self.as_fraction(value)
        return dict(lower_exact=str(lo),upper_exact=str(hi),
            lower_float=float(lo),upper_float=float(hi))

    def sqrt_bounds(self,value):
        lo,hi=self.as_fraction(value)
        if lo<0:
            raise ValueError('Square-root an actual nonnegative interval')
        scale=self.d.SCALE
        def root(q,up):
            numerator=q.numerator*scale*scale
            integer=math.isqrt(numerator//q.denominator)
            if up and integer*integer*q.denominator<numerator:
                integer+=1
            return integer
        return root(lo,False),root(hi,True)

    def endpoint(self,angle,*,axis=None):
        d=self.d
        p=d.box(1);pp=d.box(0);delta=d.box(0);rho=d.box(1)
        for m,c in enumerate(self.core,1):
            nu=2*m
            if axis=='zero':
                sine,cosine=d.box(0),d.box(1)
            elif axis=='quarter':
                sine,cosine=d.box(0),d.box((-1)**m)
            else:
                sine,cosine=d.sine_cosine(d.scale(angle,nu))
            p=d.add(p,d.scale(cosine,c))
            pp=d.add(pp,d.scale(sine,-nu*c))
            delta=d.add(delta,d.scale(sine,F(1-nu*nu,nu)*c))
            rho=d.add(rho,d.scale(cosine,(1-nu*nu)*c))
        sd,cd=d.sine_cosine(delta)
        radial=d.sub(d.mul(self.R,cd),p)
        tangent=d.sub(d.mul(self.R,sd),pp)
        horizontal=d.add(self.square(radial),self.square(tangent))
        chord=d.add(horizontal,self.H2)
        surplus=d.sub(chord,self.square(self.S))
        return dict(horizontal_squared=horizontal,chord_squared=chord,
            chord_squared_minus_S_squared=surplus,rho=rho,
            initial_support=p,initial_support_derivative=pp,
            exact_theta_minus_normal_angle=delta)

    def point(self,*,label,phi=None,axis=None):
        angle=self.d.box(F(0) if phi is None else F(phi))
        raw=self.endpoint(angle,axis=axis)
        self.counts['exact_point_enclosures']+=1
        ratio=self.d.mul(self.sqrt_bounds(raw['chord_squared']),self.d.inverse(self.S))
        return dict(label=label,axis_identity=axis,
            literal_phi_hex=None if phi is None else float(phi).hex(),
            literal_phi_exact=None if phi is None else str(F(phi)),
            every_core_mode_retained=True,raw=raw,
            distance_over_S=self.display(ratio),
            chord_squared_minus_S_squared=self.display(raw['chord_squared_minus_S_squared']),
            horizontal_squared=self.display(raw['horizontal_squared']))

    def cell(self,lo,hi):
        lo,hi=F(lo),F(hi)
        if not 0<=lo<hi<=F(1,2):
            raise ValueError('Keep a complete nonempty exact quarter interval')
        angle=self.d.mul(self.d.box(lo,hi),self.d.pi_box())
        self.counts['complete_angle_cell_enclosures']+=1
        return dict(low=lo,high=hi,**self.endpoint(angle))

    def summarize_cover(self,leaves,witnesses):
        d=self.d
        ordered=sorted(leaves,key=lambda row:row['low'])
        if (ordered[0]['low']!=0 or ordered[-1]['high']!=F(1,2)
                or any(a['high']!=b['low'] for a,b in zip(ordered,ordered[1:]))):
            raise ArithmeticError('Do not omit any exact closed angle')
        spread=sum((abs((1-(2*m)**2)*c) for m,c in enumerate(self.core,1)),F(0))
        rho_low=max(1-spread,min(F(row['rho'][0],d.SCALE) for row in ordered))
        rho_high=min(1+spread,max(F(row['rho'][1],d.SCALE) for row in ordered))
        if rho_low>rho_high:
            raise ArithmeticError('Independent true chart enclosures disagree')
        qlow=max([F(row['horizontal_squared'][0],d.SCALE) for row in ordered]
            +[F(row['raw']['horizontal_squared'][0],d.SCALE) for row in witnesses])
        qhigh=max(F(row['horizontal_squared'][1],d.SCALE) for row in ordered)
        if qlow>qhigh:
            raise ArithmeticError('A true point is outside the complete true angular cover')
        return ordered,rho_low,rho_high,qlow,qhigh


def main(args):
    require_actions()
    if (args.panels<1 or args.max_angle_leaves<1 or args.witness_angles<0
            or args.horizontal_squared_accuracy<=0
            or not math.isfinite(args.admission_seconds) or args.admission_seconds<0):
        raise ValueError('Use explicit finite natural budgets and positive requested precision')
    if args.output.exists():
        raise ValueError('Use a fresh actual diagnostic report')
    if args.work_directory==args.repo or args.repo in args.work_directory.parents:
        raise ValueError('Actual scientific scratch remains outside the git repository')
    args.work_directory.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    actual=ActualInitialInput(args)
    kernel=ChordEnclosure(actual)
    d=kernel.d
    witnesses=[kernel.point(label='exact phi=0',axis='zero'),
        kernel.point(label='exact phi=pi/2',axis='quarter')]
    for j,phi in enumerate(actual.q.phi[:args.witness_angles]):
        witnesses.append(kernel.point(label='actual first grid angle '+str(j),phi=float(phi)))
    leaves=[kernel.cell(F(0),F(1,2))]
    reason=None
    while True:
        ordered,rho_low,rho_high,qlow,qhigh=kernel.summarize_cover(leaves,witnesses)
        if rho_low>0 and qhigh-qlow<=args.horizontal_squared_accuracy:
            reason='complete angular enclosure reached the declared precision'
            break
        if len(leaves)>=args.max_angle_leaves:
            reason='natural complete-cover leaf admission budget'
            break
        if time.monotonic()-started>=args.admission_seconds:
            reason='natural complete-cover time admission budget'
            break
        if rho_low<=0:
            index=min(range(len(leaves)),key=lambda j:leaves[j]['rho'][0])
        else:
            index=max(range(len(leaves)),key=lambda j:leaves[j]['horizontal_squared'][1])
        parent=leaves[index]
        middle=(parent['low']+parent['high'])/2
        # Both complete children are computed before the parent is replaced.
        left=kernel.cell(parent['low'],middle)
        right=kernel.cell(middle,parent['high'])
        leaves[index:index+1]=[left,right]
    ordered,rho_low,rho_high,qlow,qhigh=kernel.summarize_cover(leaves,witnesses)
    h=actual.height
    Slo,Shi=actual.S
    surplus=(qlow+h*h-Shi*Shi,qhigh+h*h-Slo*Slo)
    point_obstruction=any(row['raw']['chord_squared_minus_S_squared'][0]>0 for row in witnesses)
    strict_obstruction=rho_low>0 and (point_obstruction or surplus[0]>0)
    all_chords_pass=rho_low>0 and surplus[1]<=0
    safe_height_squared=Slo*Slo-qhigh
    necessary_height_squared=Shi*Shi-qlow
    safe_height=None if safe_height_squared<0 else kernel.display(kernel.sqrt_bounds(d.box(safe_height_squared)))
    necessary_height=None if necessary_height_squared<0 else kernel.display(kernel.sqrt_bounds(d.box(necessary_height_squared)))
    floor=F(float(actual.report['amplitude_design_constraints']['budgets']['effective_height_floor']))
    safe_above_floor=(rho_low>0 and safe_height is not None
        and floor<=F(safe_height['lower_exact']))
    q=actual.q
    if (q.endpoint_counts['root_angles_solved']!=0
            or q.endpoint_counts['root_line_search_evaluations']!=0
            or q.counts['residual_calls']!=0 or q.counts['J_calls']!=0 or q.counts['Jtranspose_calls']!=0):
        raise ArithmeticError('The necessary input diagnostic must not evaluate a zero root or a full field/J')
    source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip()
    report=dict(schema=SCHEMA,source_sha256=sha(__file__),source_commit=source_commit,
        complete=True,actual_input=actual.binding,
        fixed_scalar_metric_identity_sha256=actual.profile,
        actual_zero_model_identity_sha256=actual.identity,
        actual_initial_point_sha256=q._current_point_sha256,
        initial_height=dict(literal_exact=str(h),literal_hex=float(h).hex(),value=actual.height_float),
        true_S=kernel.display(d.box(*actual.S)),true_R=kernel.display(d.box(*actual.R)),
        true_radius_box_includes_the_complete_R690_tail=True,
        true_length_box_is_original_exact_symbolic_S=True,
        current_and_fixed_core_equal_exactly=True,
        exact_initial_inverse_branch='phi_current=phi; unique real lift when the separately enclosed whole-circle rho is positive',
        complete_core_mode_count=len(actual.core),
        complete_closed_quarter_cover=True,
        full_circle_extension='p, rho and horizontal chord squared are pi-periodic and even, so reflection of [0,pi/2] covers all angles',
        complete_rho_enclosure=dict(lower_exact=str(rho_low),upper_exact=str(rho_high),
            lower_float=float(rho_low),upper_float=float(rho_high)),
        full_circle_rho_certified_positive=rho_low>0,
        global_maximum_horizontal_chord_squared=kernel.display(d.box(qlow,qhigh)),
        global_maximum_chord_squared_minus_S_squared=kernel.display(d.box(*surplus)),
        axis_zero=witnesses[0],axis_quarter=witnesses[1],
        actual_grid_point_witnesses=witnesses[2:],
        one_true_point_violates_necessary_chord_condition=point_obstruction,
        no_unit_meridian_closure_for_this_fixed_initial_core_H_certified=bool(strict_obstruction),
        all_angles_necessary_chord_inequality_certified=bool(all_chords_pass),
        obstruction_scope='only this exact initial core/H and fixed scalar target; all rotations/bubbles are unit but changing free core/H remains allowed',
        necessary_height_squared_upper_exact=str(necessary_height_squared),
        necessary_height_upper_enclosure=necessary_height,
        necessary_height_upper_exact=None if necessary_height is None else necessary_height['upper_exact'],
        sufficient_bound_for_all_chord_inequalities_only=safe_height,
        sufficient_chord_height_bound_lower_exact=None if safe_height is None else safe_height['lower_exact'],
        sufficient_chord_height_bound_upper_exact=None if safe_height is None else safe_height['upper_exact'],
        sufficient_height_squared_exact=str(safe_height_squared),
        actual_amplitude_height_floor_exact=str(floor),
        sufficient_chord_height_interval_above_actual_floor_certified=bool(safe_above_floor),
        a_root_or_embedded_isometry_follows_from_chord_inequalities=False,
        new_height_or_any_free_coordinate_written=False,
        zero_initial_field_or_checkpoint_manufactured=False,
        exact_closed_angle_partition=[dict(phi_over_pi=[row['low'],row['high']],
            rho=kernel.display(row['rho']),horizontal_squared=kernel.display(row['horizontal_squared']))
            for row in ordered],
        requested_horizontal_squared_accuracy=str(args.horizontal_squared_accuracy),
        requested_accuracy_reached=(qhigh-qlow<=args.horizontal_squared_accuracy),
        actual_complete_angle_leaves=len(ordered),interval_operation_counts=kernel.counts,
        zero_root_calls=0,full_residual_calls=0,full_J_calls=0,full_Jtranspose_calls=0,
        continuous_metric_certified=False,continuous_geometry_certified=False,
        closed_isometry_accepted=False,stop_reason=reason,actual_seconds=time.monotonic()-started)
    write(args.output,report)
    print(json.dumps(dict(schema=SCHEMA,source_sha256=sha(__file__),report_sha256=sha(args.output),
        target=actual.profile,actual_initial_point=q._current_point_sha256,
        full_circle_rho_positive=rho_low>0,
        necessary_chord_obstruction_certified=bool(strict_obstruction),
        all_chords_necessary_inequality_certified=bool(all_chords_pass),
        actual_complete_angle_leaves=len(ordered),stop_reason=reason),allow_nan=False),flush=True)


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','failed-report','reference-bundle','preparation-report',
                 'carrier','node-report','scalar-input','work-directory','output'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--admission-seconds',type=float,default=60.)
    p.add_argument('--max-angle-leaves',type=int,default=256)
    p.add_argument('--witness-angles',type=int,default=8)
    p.add_argument('--horizontal-squared-accuracy',type=F,default=F(1,10**10))
    args=p.parse_args()
    for key,value in vars(args).items():
        if isinstance(value,Path):
            setattr(args,key,value.resolve())
    return args


if __name__=='__main__':
    main(parse_args())
