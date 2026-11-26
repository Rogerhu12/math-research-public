#!/usr/bin/env python3
"""Complete support-complement chord necessity at an actual zero initial input.

This is an INITIAL-INPUT diagnostic, not a field/endpoint-root consumer.
It keeps the actual initial core, H, zero omega, exact scalar and two
bubble supports.  It encloses the unchanged meridian integral outside
the supports, and the length still available inside them.  No Newton,
F, Gram residual, J or Jtranspose is evaluated.
"""
import argparse
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

SCHEMA='actual-zero-initial-supported-meridian-chord-necessity-v1'
TOPIC='topics/visible-flex-larger-amplitude'
PINS={
    'initial':('scripts/resume_20261126/diagnose_zero_initial_chord.py','65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0'),
    'whole_scalar':('scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py','a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6'),
}
EXPECTED_FAILURE='4341323c805a3e4f38c20c6e5264e9875b8b717082793ece982c029f488ed744'
EXPECTED_POINT='cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3'
EXPECTED_NODES=(('1/32','1/4','15/32'),('17/32','3/4','31/32'))


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Actual scalar, support and chord science requires public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def load(name,path,expected):
    if sha(path)!=expected:
        raise ValueError('Changed complete supporting source: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def serial(value):
    if isinstance(value,F):
        return str(value)
    if isinstance(value,dict):
        return {key:serial(v) for key,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [serial(v) for v in value]
    if hasattr(value,'tolist'):
        return serial(value.tolist())
    if isinstance(value,float) and not math.isfinite(value):
        raise ValueError('No nonfinite diagnostic number is evidence')
    return value


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def write(path,value):
    temporary=path.with_name(path.name+'.partial')
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary.write_text(json.dumps(serial(value),indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


class ComplementIntegral:
    """Exact affine U-complement partition; complete c bounds on each cell."""
    def __init__(self,actual,whole_scalar):
        self.a,self.d=actual,actual.d
        self.scalar=whole_scalar.ScalarWholeInterval(actual)
        self.supports=[(F(row[0]),F(row[2])) for row in EXPECTED_NODES]
        self.complement=[(F(0),self.supports[0][0]),
            (self.supports[0][1],self.supports[1][0]),(self.supports[1][1],F(1))]
        self.support_length_fraction=sum((hi-lo for lo,hi in self.supports),F(0))
        if self.support_length_fraction!=F(7,8):
            raise ArithmeticError('Keep the actual two wide support lengths')
        self.calls=0

    def cell(self,lo,hi):
        lo,hi=F(lo),F(hi)
        if not 0<=lo<hi<=1:
            raise ValueError('Use nonempty exact radial fractions')
        left,right=(lo,F(0)),(hi,F(0))
        boxes,pieces=self.scalar.enclose(left,right)
        d=self.d
        vertical=(max(0,boxes[1][0]),min(d.SCALE,boxes[1][1]))
        if vertical[0]>vertical[1]:
            raise ArithmeticError('The same exact positive unit meridian missed 0<=c<=1')
        width=self.scalar.width_box(left,right)
        integral=d.mul(width,vertical)
        self.calls+=1
        return dict(low=lo,high=hi,complete_exact_interval=True,
            exact_affine_endpoints=[left,right],c_box=vertical,
            physical_width=width,vertical_integral=integral,pieces=pieces,
            complete_infinite_tail_retained=any(
                item.get('complete_infinite_tail') is True for item in pieces))

    def complete(self,rows):
        ordered=sorted(rows,key=lambda row:row['low'])
        cursor=0
        for lo,hi in self.complement:
            current=lo
            while cursor<len(ordered) and ordered[cursor]['low']<hi:
                row=ordered[cursor]
                if row['low']!=current or row['high']>hi:
                    raise ArithmeticError('A support-complement cell was omitted or overlapped')
                current=row['high']
                cursor+=1
            if current!=hi:
                raise ArithmeticError('The exact support complement is not fully covered')
        if cursor!=len(ordered):
            raise ArithmeticError('Unexpected radial cell outside the declared complement')
        result=self.d.ZERO
        for row in ordered:
            result=self.d.add(result,row['vertical_integral'])
        # This is an intersection of two proved enclosures, not a deletion.
        upper=self.d.scale(self.d.box(*self.a.S),1-self.support_length_fraction)
        result=max(result[0],0),min(result[1],upper[1])
        if result[0]>result[1]:
            raise ArithmeticError('Independent complete vertical integral bounds disagree')
        return ordered,result

    def effective_radial_coefficient(self):
        """R minus the unchanged horizontal integral, with R cancelling exactly."""
        p,d=self.a.context.full,self.d
        points=(F(0),F(1,32),F(15,32),F(17,32),F(31,32))
        values={}
        records=[]
        for alpha in points:
            # Every endpoint in this formula precedes the R690 replacement
            # anchor. The cap radius cancels algebraically, so no old radius
            # or tail integral is substituted for the new one.
            if (1-alpha)*self.a.S[0]<F(p.out)/4:
                raise ValueError('An a endpoint reaches the changed tail; use its complete new law')
            old=p.at_box(p.affine_time(alpha,F(0)))[0]
            value=d.box(F(old[0],p.h.S),F(old[1],p.h.S))
            values[alpha]=value
            records.append(dict(s_over_S=str(alpha),complete_a_box=value,
                actual_affine_definition=[alpha,F(0)],
                original_and_new_scalar_agree_at_this_point=True))
        # R-B_out = a(0)-a(S/32)+a(15S/32)-a(17S/32)+a(31S/32).
        result=d.add(d.sub(d.add(d.sub(values[F(0)],values[F(1,32)]),
            values[F(15,32)]),values[F(17,32)]),values[F(31,32)])
        return result,records


def supported_kernel_class(initial):
    class SupportedChord(initial.ChordEnclosure):
        def __init__(self,actual,radial,vertical,length):
            super().__init__(actual)
            self.R=radial
            self.S=length
            self.effective_height=self.d.sub(self.d.box(actual.height),vertical)
            self.H2=self.square(self.effective_height)

        def point(self,*,label,phi=None,axis=None):
            angle=self.d.box(F(0) if phi is None else F(phi))
            raw=self.endpoint(angle,axis=axis)
            self.counts['exact_point_enclosures']+=1
            ratio=self.d.mul(self.sqrt_bounds(raw['chord_squared']),self.d.inverse(self.S))
            return dict(label=label,axis_identity=axis,
                literal_phi_hex=None if phi is None else float(phi).hex(),
                literal_phi_exact=None if phi is None else str(F(phi)),
                every_core_mode_retained=True,raw=raw,
                required_distance_over_support_length=self.display(ratio),
                required_distance_squared_minus_support_length_squared=self.display(
                    raw['chord_squared_minus_S_squared']),
                horizontal_squared=self.display(raw['horizontal_squared']))
    return SupportedChord


def main(args):
    require_actions()
    if (args.panels<1 or args.max_angle_leaves<1 or args.max_radial_leaves<3
            or args.witness_angles<0 or args.horizontal_squared_accuracy<=0
            or args.vertical_integral_accuracy<=0
            or not math.isfinite(args.admission_seconds) or args.admission_seconds<0
            or not math.isfinite(args.radial_admission_seconds) or args.radial_admission_seconds<0):
        raise ValueError('Use positive exact precision requests and explicit natural budgets')
    if args.output.exists():
        raise ValueError('Use a fresh actual support-complement diagnostic')
    if args.work_directory==args.repo or args.repo in args.work_directory.parents:
        raise ValueError('Actual scientific scratch remains outside the git repository')
    args.work_directory.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    topic=args.repo/TOPIC
    paths={role:topic/relative for role,(relative,_) in PINS.items()}
    modules={role:load('_supported_chord_'+role,paths[role],PINS[role][1]) for role in PINS}
    initial,whole=modules['initial'],modules['whole_scalar']
    if sha(args.failed_report)!=EXPECTED_FAILURE:
        raise ValueError('Bind the actual wide/.75 original initial-input failure')
    actual=initial.ActualInitialInput(args)
    if (actual.q._current_point_sha256!=EXPECTED_POINT
            or tuple(tuple(str(F(v)) for v in row)
                for row in actual.report['working_evaluation']['exact_relative_bubble_nodes'])!=EXPECTED_NODES):
        raise ValueError('Keep the exact actual initial point and both wide bubble supports')
    if (whole.PINS['reference']!=initial.PINS['reference']
            or whole.PINS['operator']!=initial.PINS['operator']):
        raise ValueError('The complete whole-scalar kernel and initial input have different physical sources')
    complement=ComplementIntegral(actual,whole)
    radial_coefficient,a_points=complement.effective_radial_coefficient()
    # A complete first cover is constructed before any refinement admission
    # decision. Natural return always keeps every complement interval.
    radial=[complement.cell(lo,hi) for lo,hi in complement.complement]
    radial_started=time.monotonic()
    radial_reason=None
    while True:
        radial_ordered,vertical=complement.complete(radial)
        vertical_width=F(vertical[1]-vertical[0],actual.d.SCALE)
        if vertical_width<=args.vertical_integral_accuracy:
            radial_reason='complete vertical integral reached requested precision'
            break
        if len(radial)>=args.max_radial_leaves:
            radial_reason='natural complete radial-cover leaf admission budget'
            break
        if (time.monotonic()-radial_started>=args.radial_admission_seconds
                or time.monotonic()-started>=args.admission_seconds):
            radial_reason='natural complete radial-cover time admission budget'
            break
        index=max(range(len(radial)),key=lambda j:
            radial[j]['vertical_integral'][1]-radial[j]['vertical_integral'][0])
        parent=radial[index]
        mid=(parent['low']+parent['high'])/2
        left=complement.cell(parent['low'],mid)
        right=complement.cell(mid,parent['high'])
        radial[index:index+1]=[left,right]
    d=actual.d
    support_length=d.scale(d.box(*actual.S),complement.support_length_fraction)
    kernel=supported_kernel_class(initial)(actual,radial_coefficient,vertical,support_length)
    witnesses=[kernel.point(label='exact phi=0',axis='zero'),
        kernel.point(label='exact phi=pi/2',axis='quarter')]
    for j,phi in enumerate(actual.q.phi[:args.witness_angles]):
        witnesses.append(kernel.point(label='actual first grid angle '+str(j),phi=float(phi)))
    leaves=[kernel.cell(F(0),F(1,2))]
    angle_reason=None
    while True:
        ordered,rho_low,rho_high,qlow,qhigh=kernel.summarize_cover(leaves,witnesses)
        if rho_low>0 and qhigh-qlow<=args.horizontal_squared_accuracy:
            angle_reason='complete angular enclosure reached requested precision'
            break
        if len(leaves)>=args.max_angle_leaves:
            angle_reason='natural complete angular-cover leaf admission budget'
            break
        if time.monotonic()-started>=args.admission_seconds:
            angle_reason='natural complete angular-cover time admission budget'
            break
        if rho_low<=0:
            index=min(range(len(leaves)),key=lambda j:leaves[j]['rho'][0])
        else:
            index=max(range(len(leaves)),key=lambda j:leaves[j]['horizontal_squared'][1])
        parent=leaves[index]
        middle=(parent['low']+parent['high'])/2
        left=kernel.cell(parent['low'],middle)
        right=kernel.cell(middle,parent['high'])
        leaves[index:index+1]=[left,right]
    ordered,rho_low,rho_high,qlow,qhigh=kernel.summarize_cover(leaves,witnesses)
    distance=d.add(d.box(qlow,qhigh),kernel.H2)
    surplus=d.sub(distance,kernel.square(support_length))
    point_obstruction=any(row['raw']['chord_squared_minus_S_squared'][0]>0 for row in witnesses)
    strict_obstruction=rho_low>0 and (point_obstruction or surplus[0]>0)
    all_supported_chords_pass=rho_low>0 and surplus[1]<=0
    Il,Ih=kernel.as_fraction(vertical)
    length_low,length_high=kernel.as_fraction(support_length)
    guaranteed_margin=length_low**2-qhigh
    necessary_margin=length_high**2-qlow
    guaranteed_height=None
    necessary_height=None
    if guaranteed_margin>=0:
        radius=kernel.sqrt_bounds(d.box(guaranteed_margin))
        rlow=F(radius[0],d.SCALE)
        guaranteed_height=(Ih-rlow,Il+rlow)
        if guaranteed_height[0]>guaranteed_height[1]:
            guaranteed_height=None
    if necessary_margin>=0:
        radius=kernel.sqrt_bounds(d.box(necessary_margin))
        rhigh=F(radius[1],d.SCALE)
        necessary_height=(Il-rhigh,Ih+rhigh)
    floor=F(float(actual.report['amplitude_design_constraints']['budgets']['effective_height_floor']))
    guaranteed_above_floor=(rho_low>0 and guaranteed_height is not None
        and guaranteed_height[1]>=max(floor,guaranteed_height[0]))
    q=actual.q
    if (q.endpoint_counts['root_angles_solved']!=0
            or q.endpoint_counts['root_line_search_evaluations']!=0
            or q.counts['residual_calls']!=0 or q.counts['J_calls']!=0
            or q.counts['Jtranspose_calls']!=0):
        raise ArithmeticError('This necessary input diagnostic must not read an endpoint root or F/J')
    report=dict(schema=SCHEMA,source_sha256=sha(__file__),
        source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip(),
        complete=True,actual_initial_input=actual.binding,
        actual_initial_point_sha256=q._current_point_sha256,
        actual_original_zero_model_identity_sha256=q.identity,
        actual_base_model_identity_sha256=actual.base.identity,
        fixed_scalar_metric_identity_sha256=actual.profile,
        complete_sources={role:record(path) for role,path in paths.items()},
        exact_relative_bubble_nodes=[list(row) for row in EXPECTED_NODES],
        support_fraction=str(complement.support_length_fraction),
        exact_support_components=complement.supports,exact_complement_components=complement.complement,
        true_S=kernel.display(d.box(*actual.S)),true_support_length=kernel.display(support_length),
        actual_height=dict(exact=str(actual.height),hex=float(actual.height).hex(),value=actual.height_float),
        complete_complement_vertical_integral=kernel.display(vertical),
        effective_horizontal_coefficient=kernel.display(radial_coefficient),
        effective_height_after_unchanged_integral=kernel.display(kernel.effective_height),
        exact_cap_radius_cancelled_algebraically=True,
        every_a_endpoint_precedes_the_true_replacement_anchor=True,
        a_endpoint_enclosures=[dict(s_over_S=row['s_over_S'],
            exact_affine_definition=row['actual_affine_definition'],
            a=kernel.display(row['complete_a_box']),
            original_and_new_scalar_agree_at_this_point=True) for row in a_points],
        complete_complement_radial_cover=True,
        complete_infinite_tail_included=any(row['complete_infinite_tail_retained'] for row in radial_ordered),
        complete_closed_quarter_cover=True,full_circle_rho_certified_positive=rho_low>0,
        complete_rho_enclosure=dict(lower_exact=str(rho_low),upper_exact=str(rho_high),
            lower_float=float(rho_low),upper_float=float(rho_high)),
        full_circle_extension='The fixed initial p, rho and effective horizontal squared length are pi-periodic and even; reflection of the complete quarter covers all angles.',
        global_maximum_required_horizontal_squared=kernel.display(d.box(qlow,qhigh)),
        global_maximum_required_squared_minus_support_length_squared=kernel.display(surplus),
        one_true_angle_violates_supported_chord_condition=point_obstruction,
        no_supported_unit_rotation_closure_for_this_initial_point_certified=bool(strict_obstruction),
        all_angles_supported_chord_inequality_certified=bool(all_supported_chords_pass),
        supported_necessity_is_independent_of_Q_and_branch_radius=True,
        applies_to_any_rotation_equal_identity_outside_support_at_this_same_initial_point=True,
        new_moment_model_or_report_consumed=False,
        obstruction_scope='Only this exact initial zero-omega/core/H and the declared supports with unchanged T0 outside them. It is not an obstruction after changing full free omega/core/H, supports, or another representation.',
        guaranteed_interval_for_chord_inequalities_only=None if guaranteed_height is None else
            dict(lower_exact=str(guaranteed_height[0]),upper_exact=str(guaranteed_height[1])),
        necessary_height_interval_outer=None if necessary_height is None else
            dict(lower_exact=str(necessary_height[0]),upper_exact=str(necessary_height[1])),
        guaranteed_height_lower_exact=None if guaranteed_height is None else str(guaranteed_height[0]),
        guaranteed_height_upper_exact=None if guaranteed_height is None else str(guaranteed_height[1]),
        necessary_height_lower_exact=None if necessary_height is None else str(necessary_height[0]),
        necessary_height_upper_exact=None if necessary_height is None else str(necessary_height[1]),
        height_interval_interpretation_requires_whole_circle_rho_positive=True,
        no_height_can_pass_supported_necessity_for_this_core_zero_omega=bool(rho_low>0 and necessary_margin<0),
        actual_amplitude_height_floor_exact=str(floor),
        guaranteed_chord_height_interval_meets_actual_floor=bool(guaranteed_above_floor),
        guaranteed_height_interval_is_not_a_root_or_geometry_certificate=True,
        root_or_embedded_isometry_follows_from_necessary_inequality=False,
        new_Q_or_H_or_any_free_coordinate_written=False,
        new_zero_initial_field_or_checkpoint_manufactured=False,
        actual_complete_radial_leaves=len(radial_ordered),
        actual_complete_angular_leaves=len(ordered),
        requested_vertical_integral_accuracy=str(args.vertical_integral_accuracy),
        requested_vertical_integral_accuracy_reached=vertical_width<=args.vertical_integral_accuracy,
        requested_horizontal_squared_accuracy=str(args.horizontal_squared_accuracy),
        requested_horizontal_squared_accuracy_reached=qhigh-qlow<=args.horizontal_squared_accuracy,
        actual_whole_scalar_interval_calls=complement.scalar.calls,
        actual_new_radial_enclosures=complement.calls,interval_operation_counts=kernel.counts,
        radial_stop_reason=radial_reason,angular_stop_reason=angle_reason,
        exact_radial_partition=[dict(s_over_S=[row['low'],row['high']],
            c=kernel.display(row['c_box']),width=kernel.display(row['physical_width']),
            integral=kernel.display(row['vertical_integral']),pieces=row['pieces'],
            complete_infinite_tail_retained=row['complete_infinite_tail_retained'])
            for row in radial_ordered],
        exact_angular_partition=[dict(phi_over_pi=[row['low'],row['high']],
            rho=kernel.display(row['rho']),horizontal_squared=kernel.display(row['horizontal_squared']))
            for row in ordered],
        axis_zero=witnesses[0],axis_quarter=witnesses[1],actual_grid_witnesses=witnesses[2:],
        zero_root_calls=0,full_residual_calls=0,full_J_calls=0,full_Jtranspose_calls=0,
        continuous_metric_certified=False,continuous_geometry_certified=False,
        accepted_isometry=False,actual_seconds=time.monotonic()-started)
    if report['complete_infinite_tail_included'] is not True:
        raise ArithmeticError('The last unchanged interval includes the full accurate deep tail')
    write(args.output,report)
    print(json.dumps(dict(schema=SCHEMA,source_sha256=sha(__file__),report_sha256=sha(args.output),
        complete=True,target=actual.profile,original_point=q._current_point_sha256,
        full_circle_rho_positive=rho_low>0,supported_chord_obstruction=bool(strict_obstruction),
        all_supported_chords=bool(all_supported_chords_pass),
        radial_leaves=len(radial_ordered),angular_leaves=len(ordered)),allow_nan=False),flush=True)


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','failed-report','reference-bundle','preparation-report',
                 'carrier','node-report','scalar-input','work-directory','output'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--admission-seconds',type=float,default=75.)
    p.add_argument('--radial-admission-seconds',type=float,default=25.)
    p.add_argument('--max-radial-leaves',type=int,default=384)
    p.add_argument('--max-angle-leaves',type=int,default=256)
    p.add_argument('--witness-angles',type=int,default=8)
    p.add_argument('--vertical-integral-accuracy',type=F,default=F(1,10**8))
    p.add_argument('--horizontal-squared-accuracy',type=F,default=F(1,10**10))
    args=p.parse_args()
    for key,value in vars(args).items():
        if isinstance(value,Path):
            setattr(args,key,value.resolve())
    return args


if __name__=='__main__':
    main(parse_args())
