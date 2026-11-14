#!/usr/bin/env python3
"""One local new-core initial field, retaining the accepted exterior exactly.

The accepted f198 source is replayed from its four complete published inputs.
Only a and the horizontal tangent angle are changed near the core. The entire
old b and its query-independent common primitive are retained. No optimizer,
coefficient projection, height proposal, or whole-basis transport is called.
Research construction requires this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time
import traceback

import numpy as np

from ellipse_frame_port import EllipticCylinderPort
from frame_collar_bvp import atomic_save,periodic_operator
from frame_collar_residual_audit import digest
from frame_core_transport_audit import (audit_data,paired_angle_comparison,
    implementation_hashes as core_audit_hashes)
from frame_entry_paired_repair_audit import require_public_actions,JETS
from frame_entry_short_bounded_audit import (build_grid,artificial_inputs,
    default_configuration as short_defaults,implementation_hashes as short_hashes)
from frame_entry_paired_repair import EntryRepairProblem
from frame_entry_bounded_height import BoundedEntryHeightProblem
from frame_height_polytope_audit import (load_short_model,proposal_polytope,
    stage_configuration as height_configuration,implementation_hashes as height_hashes)
from frame_height_quartic_joint_audit import (prepare_run,InputReplayFailure,
    implementation_hashes as replay_hashes)
from frame_independent_height_solve import state_record,point_values,extremum

SCHEMA='localized-core-retained-accepted-physical-exterior-initial-audit-v1'
S11_COEFFICIENTS=['0']*6+['462','-1980','3465','-3080','1386','-252']


def implementation_hashes():
    result=replay_hashes();result.update(core_audit_hashes())
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration(artificial=False):
    return {'target_minor':'4/5' if artificial else '37/100','local_length':'81/500',
        'radial_nodes':9 if artificial else 121,'old_entry_subdivisions':6 if artificial else 24,
        'local_subdivisions':6 if artificial else 24,'angular_nodes':64 if artificial else 384,
        'doubled_angular_nodes':128 if artificial else 768,
        'query_quadrature_order':3 if artificial else 8,
        'target_reach':'61/1000','reference_selection':'accepted nine-height final state, not post-quartic',
        'no_optimizer_or_height_step':True}


def local_cutoff(radial,left,length):
    """1-S11 with exact constant extensions and stable reflected evaluation."""
    t=np.asarray(radial,float);x=(t-left)/length;y=np.clip(x,0.,1.)
    small=np.minimum(y,1-y)
    value=small**6*(462+small*(-1980+small*(3465+small*(-3080+small*(1386-252*small)))))
    chi=np.where(y<=.5,1-value,value)
    first=-2772*y**5*(1-y)**5/length
    second=-13860*y**4*(1-y)**4*(1-2*y)/length**2
    chi=np.where(x<=0,1.,np.where(x>=1,0.,chi))
    inside=(x>0)&(x<1)
    return chi,np.where(inside,first,0.),np.where(inside,second,0.)


def vertical_cross(value):
    out=np.zeros_like(value);out[...,0]=-value[...,1];out[...,1]=value[...,0]
    return out


def rotate_vertical(value,angle):
    c,s=np.cos(angle),np.sin(angle);out=np.empty_like(value)
    out[...,0]=c*value[...,0]-s*value[...,1]
    out[...,1]=s*value[...,0]+c*value[...,1]
    out[...,2]=value[...,2]
    return out


class LocalizedCoreField:
    """An immutable physical initializer, not a parameterized optimization class."""
    def __init__(self,reference,state,target_minor,local_length='81/500',*,artificial=False):
        old=reference.port;target=Q(target_minor)
        if artificial:
            if (old.A_exact,old.B_exact,old.width_exact,target)!=(Q(9,10),Q(18,25),Q(1,50),Q(4,5)):
                raise ValueError('artificial construction is restricted to the declared mild core pair')
        else:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),[])
            if (old.A_exact,old.B_exact,old.width_exact,target,old.side)!=(Q(1),Q(7,25),Q(1,50),Q(37,100),1):
                raise ValueError('this research initializer is the unique declared positive B=.28 to B=.37 change')
        if reference.metric_free or not old.B_exact<target<=old.A_exact:
            raise ValueError('a frozen reference and a strictly increased admissible minor radius are required')
        self.reference=reference;self.artificial=bool(artificial)
        self._state=np.asarray(state,dtype=np.float64).copy();self._state.setflags(write=False)
        if self._state.shape!=(reference.nunknown,) or not np.all(np.isfinite(self._state)):
            raise ValueError('one complete finite reference vector required')
        self.reference_identity=copy.deepcopy(reference.identity(self._state))
        self.reference_identity_sha256=digest(self.reference_identity)
        self.reference_metric=copy.deepcopy(reference.metric_model(self._state))
        self.port=EllipticCylinderPort(old.A_exact,target,old.width_exact,old.side)
        self.left_exact=reference.seed.length_exact*reference.seed.core_fraction_exact
        self.length_exact=Q(local_length);self.right_exact=self.left_exact+self.length_exact
        patch_left_exact=(reference.seed.length_exact*(1-reference.seed.flat_fraction_exact)
            -Q(reference.source.support_exact))
        if self.length_exact<=0 or not self.right_exact<patch_left_exact:
            raise ValueError('positive localization ending strictly before the old natural-cap patch required')
        self.left=float(self.left_exact);self.length=float(self.length_exact);self.right=float(self.right_exact)
        self.delta_a0=self.port.a0-old.a0
        if not self.delta_a0>0:raise ArithmeticError('numerical perimeter difference contradicts exact monotonicity')
        self.cutoff_definition={'schema':'local-core-S11-cutoff-v1','left_exact':str(self.left_exact),
            'length_exact':str(self.length_exact),'right_exact':str(self.right_exact),
            'piecewise_definition':'1 before left; 1-S11((s-left)/length) on interval; 0 after right',
            'S11_coefficients_ascending_exact':S11_COEFFICIENTS,
            'first_five_derivatives_match_at_both_ends':True}
        self.metric_definition={'schema':'localized-core-additive-complete-frozen-radius-v1',
            'reference_complete_metric':self.reference_metric['mathematical_definition'],
            'reference_complete_metric_sha256':self.reference_metric['mathematical_definition_sha256'],
            'old_core_identity':old.identity,'new_core_identity':self.port.identity,
            'a0_definition':'exact perimeter of each named ellipse divided by 2*pi',
            'radius_definition':'a_new(s)=a_reference_complete(s)+chi(s)*(a0_new-a0_old)',
            'cutoff':self.cutoff_definition,'metric_definition':'ds^2+a_new(s)^2*dtheta^2',
            'positivity_proof':'B_new>B_old implies exact a0_new>a0_old; 0<=chi<=1; a_new>=a_reference>0',
            'old_seed_retained_only_as_reference_definition_and_chart_layout':True,
            'new_metric_design_not_a_refinement_of_the_old_fixed_metric':True}
        self._identity={'schema':'localized-core-exact-physical-field-initializer-v1',
            'accepted_reference_physical_state_sha256':self.reference_identity_sha256,
            'reference_definition_available_in_the_bound_complete_source_state':True,
            'old_core_identity':old.identity,'new_core_identity':self.port.identity,
            'new_port_identity':self.port.port_identity,'tail_identity':reference.tail.identity,
            'complete_new_metric':self.metric_definition,'cutoff':self.cutoff_definition,
            'angle_definition':'d(s,theta)=chi(s)*(u_core_new(theta)-u_core_old(theta))',
            'tangent_definition':'T_new=R_z(d)*T_reference; vertical component unchanged',
            'position_definition':'a_new*Pi_zero_angular_mean(T_new)+reference_zc*e_z',
            'full_b_bprime_bsecond_and_zc_are_the_accepted_reference_functions':True,
            'same_Pi_gauge_and_same_initial_center_height':True,
            'all_exterior_position_two_jets_equal_reference_from_local_right_onward':True,
            'all_reference_parameter_bits_retained_without_new_basis_interpretation':True,
            'immutable_original_c0_lineage_is_not_replaced':True,
            'no_isometry_embedding_reach_or_finite_error_guarantee':True,
            'evaluation_rules_do_not_enter_physical_identity':True}

    def __getattr__(self,name):
        return getattr(self.reference,name)

    def _check_state(self,state):
        values=np.asarray(state,dtype=np.float64)
        if values.shape!=self._state.shape or values.tobytes()!=self._state.tobytes():
            raise ValueError('this read-only physical initializer accepts only its exact reference coefficients')
        if self.reference.identity(values)!=self.reference_identity:
            raise ValueError('the reference physical definition changed')
        return values

    def initial_state(self):return self._state.copy()

    def identity(self,state):
        self._check_state(state);return copy.deepcopy(self._identity)

    def metric_model(self,state):
        self._check_state(state)
        return {'schema':'frozen-localized-core-additive-radius-v1',
            'mathematical_definition':copy.deepcopy(self.metric_definition),
            'mathematical_definition_sha256':digest(self.metric_definition),
            'frozen':True,'new_design':True,'free_metric_coefficients':0}

    def metric(self,state,radial,jacobian=False):
        self._check_state(state)
        if jacobian:raise NotImplementedError('this initializer has no variable parameter family')
        base=self.reference.metric(self._state,radial);chi,first,second=local_cutoff(radial,self.left,self.length)
        a=base['a']+self.delta_a0*chi;ap=base['a_s']+self.delta_a0*first
        app=base['a_ss']+self.delta_a0*second
        if np.any(a<=0) or not np.all(np.isfinite(a)):raise FloatingPointError('nonpositive or nonfinite evaluated new radius')
        return {'a':a,'a_s':ap,'a_ss':app,'K':-app/a}

    def evaluation_definition(self):
        return {'schema':'localized-core-physical-field-evaluator-v1',
            'reference_evaluation':self.reference.evaluation_definition(),
            'old_a0_evaluated':self.reference.port.a0,'new_a0_evaluated':self.port.a0,
            'delta_a0_evaluated':self.delta_a0,
            'core_phase_evaluation':'unchanged EllipticCylinderPort exact-integral inverse evaluator for each core',
            'new_tangent_derivatives':'analytic vertical-rotation product rule through s^2 and theta',
            'Pi_evaluation':'same complete uniform angular FFT rule; bandwidth specified per audit',
            'common_height_evaluation':'reuse the accepted query-independent center and b jets without recomputing b0',
            'no_continuous_error_bound':True}

    def geometry_from_reference(self,state,data):
        self._check_state(state)
        t,theta=np.asarray(data['radial']),np.asarray(data['theta'])
        old=self.reference.port.scalar_jets(0.,theta)['u']
        new=self.port.scalar_jets(0.,theta)['u']
        du=new['value']-old['value'];dut=new['theta']-old['theta']
        chi,cs,css=local_cutoff(t,self.left,self.length)
        angle=chi[:,None]*du[None,:];ds=cs[:,None]*du[None,:]
        dss=css[:,None]*du[None,:];dtheta=chi[:,None]*dut[None,:]
        T,Ts,Tss,Ttheta=(data[key] for key in ['T','Ts','Tss','Ttheta'])
        JT=vertical_cross(T)
        newT=rotate_vertical(T,angle)
        newTs=rotate_vertical(Ts+ds[...,None]*JT,angle)
        newTss=rotate_vertical(Tss+2*ds[...,None]*vertical_cross(Ts)
            +dss[...,None]*JT+ds[...,None]**2*vertical_cross(JT),angle)
        newTtheta=rotate_vertical(Ttheta+dtheta[...,None]*JT,angle)
        P,Ps,Pss=[periodic_operator(value,-1) for value in [newT,newTs,newTss]]
        metric=self.metric(state,t);a,ap,app=(metric[key][:,None,None] for key in ['a','a_s','a_ss'])
        center=data['center'];height=data['height']
        X=a*P;X[...,2]+=center[:,None]
        Xs=ap*P+a*Ps;Xs[...,2]+=height['b'][:,None]
        Xss=app*P+2*ap*Ps+a*Pss;Xss[...,2]+=height['b_s'][:,None]
        result=dict(data)
        result.update(X=X,Xs=Xs,Xt=a*newT,Xss=Xss,Xst=ap*newT+a*newTs,Xtt=a*newTtheta,
            T=newT,Ts=newTs,Tss=newTss,Ttheta=newTtheta,metric=metric,primitive=P,
            center=center.copy(),height={key:value.copy() for key,value in height.items()})
        return result

    def geometry(self,state,radial,theta,quadrature_order=4,*,jacobian=False,full_two_jet_jacobian=False):
        if jacobian or full_two_jet_jacobian:
            raise NotImplementedError('no optimization Jacobian is advertised for this immutable initializer')
        self._check_state(state)
        data=self.reference.geometry(self._state,radial,theta,quadrature_order)
        return self.geometry_from_reference(state,data)

    def direct_residual_and_jacobian(self,*args,**kwargs):
        raise NotImplementedError('initial-only class; use explicit read-only direct metric audits')

    def frozen_metric_copy(self,state):
        self._check_state(state);return self,self._state.copy()

    def evaluation_variant(self,state,**settings):
        self._check_state(state)
        other=self.reference.evaluation_variant(self._state,**settings)
        result=LocalizedCoreField(other,self._state,self.port.B_exact,self.length_exact,artificial=self.artificial)
        if result.identity(state)!=self.identity(state):raise ArithmeticError('evaluation refinement changed new physical identity')
        return result


def structure_grid(problem,cfg):
    base,theta,original=build_grid(problem.reference,cfg['radial_nodes'],
        cfg['old_entry_subdivisions'],cfg['angular_nodes'])
    count=int(cfg['local_subdivisions'])
    if count<4:raise ValueError('at least four local support subintervals required')
    extra=[problem.left_exact+problem.length_exact*Q(j,count) for j in range(count+1)]
    exact_nodes=sorted(set(map(Q,original['radial_nodes_exact']))|set(extra))
    radial=np.array([float(x) for x in exact_nodes])
    if np.any(np.diff(radial)<=0):raise ArithmeticError('exact localized query nodes collapsed in binary64')
    definition={'schema':'old-complete-structure-plus-local-core-support-grid-v1',
        'old_reference_grid':original,'local_support_nodes_exact':[str(x) for x in extra],
        'radial_nodes_exact':[str(x) for x in exact_nodes],
        'angular_nodes':len(theta),'angular_rule':'theta_j=2*pi*j/N',
        'query_grid_does_not_change_the_retained_common_primitive':True,
        'objective_weights':'uniform over this declared complete grid; diagnostics only'}
    definition['definition_sha256']=digest(definition)
    return radial,theta,definition


def local_regions(problem,data):
    values=point_values(problem,data);t,theta=data['radial'],data['theta']
    bounds=[('new_open_core',0.,problem.left),('localized_change',problem.left,problem.right),
        ('unchanged_body',problem.right,problem.source.support_start),
        ('unchanged_natural_patch',problem.source.support_start,problem.source.active_end),
        ('unchanged_open_physical_tail',problem.source.active_end,problem.seed.length)]
    answer={}
    for name,left,right in bounds:
        keep=(t>=left)&(t<=right)
        answer[name]={'closed_interval_evaluated':[float(left),float(right)],'radial_nodes':int(keep.sum())}
        if np.any(keep):
            answer[name]['extrema']={key:extremum(values[key][keep],t[keep],theta,
                'min' if key=='area' else 'abs' if key in ['E_minus_one','F_over_a'] else 'max')
                for key in ['E_minus_one','F_over_a','metric_operator_error','area','principal_curvature_absolute']}
            answer[name]['coordinate_min_sample']=data['X'][keep].min(axis=(0,1)).tolist()
            answer[name]['coordinate_max_sample']=data['X'][keep].max(axis=(0,1)).tolist()
    return {'regions':answer,'shared_boundary_rows_intentionally_repeat':True,'sampled_only':True}


def exterior_comparison(problem,old,new):
    if not np.array_equal(old['radial'],new['radial']) or not np.array_equal(old['theta'],new['theta']):
        raise ValueError('one common grid required for the exterior identity comparison')
    mask=new['radial']>=problem.right
    if not np.any(mask):raise ValueError('the complete exterior must be sampled')
    return {'exterior_starts_exact':str(problem.right_exact),'exterior_radial_nodes':int(mask.sum()),
        'all_six_position_jet_max_differences':{key:float(np.max(abs(new[key][mask]-old[key][mask]))) for key in JETS},
        'all_exterior_target_metric_jet_differences':{key:float(np.max(abs(new['metric'][key][mask]-old['metric'][key][mask])))
            for key in ['a','a_s','a_ss','K']},
        'entire_common_center_max_difference':float(np.max(abs(new['center']-old['center']))),
        'entire_b_jet_max_differences':{key:float(np.max(abs(new['height'][key]-old['height'][key]))) for key in ['b','b_s','b_ss']},
        'entire_vertical_tangent_max_difference':float(np.max(abs(new['T'][...,2]-old['T'][...,2]))),
        'finite_mean_new_tangent_max_norm':float(np.max(np.linalg.norm(new['T'].mean(axis=1),axis=-1))),
        'unit_new_tangent_max_error':float(np.max(abs(np.sum(new['T']**2,axis=-1)-1))),
        'exact_identity_has_separate_paper_proof_not_derived_from_this_sampling':True}


def summary_path(out):return out.with_name(out.stem+'-summary.json')


def compact_summary(report,out):
    answer={key:report[key] for key in ['schema','status','phase','configuration','source_files_sha256',
        'exact_input_storage','accepted_reference_physical_state_sha256','new_physical_state_sha256',
        'old_complete_metric_sha256','new_complete_metric_sha256','old_core_identity','new_core_identity',
        'retained_b0_definition_sha256','retained_cap_identity_sha256','cutoff_definition',
        'artificial_inputs_only','optimizer_calls','height_proposal_calls','elapsed_seconds','peak_rss_kib_linux',
        'exterior_identity_comparison','sparse_dense_query_comparison','same_parameter_Pi_refinement',
        'freeze_preserves_full_new_definition','error','input_failure'] if key in report}
    for name in ['old_reference_same_grid_audit','new_initial_audit','new_doubled_angle_audit']:
        if name in report:answer[name]={k:v for k,v in report[name].items() if k!='radial_distribution'}
    for name in ['new_initial_regions','new_doubled_regions']:
        if name in report:answer[name]=report[name]
    raw=out.read_bytes();answer['full_report']={'path':str(out),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    answer.update(sampled_only=True,task_complete=False,isometry_embedding_or_reach_proved=False)
    return answer


def save_report(out,report):
    atomic_save(out,report);atomic_save(summary_path(out),compact_summary(report,out))


def run_from_files(args,cfg,*,artificial=False):
    started=time.monotonic();answer={'schema':SCHEMA,'status':'before-source-replay',
        'configuration':dict(cfg),'source_files_sha256':implementation_hashes(),
        'artificial_inputs_only':bool(artificial),'optimizer_calls':0,'height_proposal_calls':0,
        'field_coefficients_reoptimized':False,'no_embedding_or_reach_claim':True}
    def save(status):
        answer['status']=status;answer['elapsed_seconds']=time.monotonic()-started
        answer['peak_rss_kib_linux']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save_report(args.out,answer)
    save('source-replay-started')
    try:
        answer['phase']='strict-four-input-accepted-height-reference-replay'
        reference,unused_initial,state,height_report,receipt,source_cfg=prepare_run(args,artificial=artificial)
        answer.update(source_receipt=receipt,exact_input_storage=receipt['exact_input_storage'],
            accepted_reference_state=state_record(reference,state),
            accepted_reference_physical_state_sha256=digest(reference.identity(state)),
            old_complete_metric_sha256=reference.metric_model(state)['mathematical_definition_sha256'],
            old_core_identity=reference.port.identity)
        answer['phase']='construct-one-explicit-local-new-core-field'
        if cfg['doubled_angular_nodes']!=2*cfg['angular_nodes']:
            raise ValueError('one same-state exact angular doubling required')
        problem=LocalizedCoreField(reference,state,cfg['target_minor'],cfg['local_length'],artificial=artificial)
        before=problem.identity(state);frozen,same=problem.frozen_metric_copy(state)
        if frozen.identity(same)!=before or same.tobytes()!=state.tobytes():
            raise ArithmeticError('freezing the already fixed new metric changed the state')
        answer.update(new_initial_state=state_record(problem,state),new_physical_state_sha256=digest(before),
            new_complete_metric_sha256=problem.metric_model(state)['mathematical_definition_sha256'],
            new_core_identity=problem.port.identity,cutoff_definition=problem.cutoff_definition,
            retained_b0_definition_sha256=digest(reference.height_base_definition),
            retained_cap_identity_sha256=digest(reference.tail.identity),
            freeze_preserves_full_new_definition=True,
            new_metric_not_interpreted_as_same_g_refinement=True,
            original_c0_reference_not_replaced_by_accepted_current_coefficients=True)
        if answer['new_complete_metric_sha256']==answer['old_complete_metric_sha256']:
            raise ArithmeticError('the declared new metric unexpectedly has the old identity')
        save('exact-reference-and-new-model-defined')
        radial,theta,grid=structure_grid(problem,cfg);order=int(cfg['query_quadrature_order'])
        answer['sampling_grid']=grid;answer['phase']='same-grid-reference-and-new-field-audit'
        old=reference.geometry(state,radial,theta,order)
        new=problem.geometry_from_reference(state,old)
        answer['old_reference_same_grid_audit']=audit_data(reference,state,old,cfg['target_reach'])
        answer['new_initial_audit']=audit_data(problem,state,new,cfg['target_reach'])
        answer['new_initial_regions']=local_regions(problem,new)
        answer['exterior_identity_comparison']=exterior_comparison(problem,old,new)
        save('one-new-field-and-exact-exterior-diagnostic-complete')
        sparse_exact=sorted({Q(0),problem.left_exact,problem.right_exact,
            problem.seed.length_exact*(1-problem.seed.flat_fraction_exact),problem.seed.length_exact})
        sparse=np.array([float(x) for x in sparse_exact]);where=np.searchsorted(radial,sparse)
        if not np.array_equal(radial[where],sparse):raise ArithmeticError('sparse interface points absent from full structure grid')
        small=problem.geometry(state,sparse,theta,order)
        answer['sparse_dense_query_comparison']={
            'radial_points_exact':[str(x) for x in sparse_exact],
            'all_six_position_jet_max_differences':{key:float(np.max(abs(small[key]-new[key][where]))) for key in JETS},
            'common_center_max_difference':float(np.max(abs(small['center']-new['center'][where]))),
            'same_accepted_query_independent_primitive':True}
        save('same-common-height-sparse-dense-interface-audit-complete')
        answer['phase']='same-new-state-Pi-angle-doubling'
        theta2=np.arange(cfg['doubled_angular_nodes'])*2*np.pi/cfg['doubled_angular_nodes']
        double=problem.geometry(state,radial,theta2,order)
        if problem.identity(state)!=before:raise ArithmeticError('read-only evaluation changed the physical model')
        answer['new_doubled_angle_audit']=audit_data(problem,state,double,cfg['target_reach'])
        answer['new_doubled_regions']=local_regions(problem,double)
        answer['same_parameter_Pi_refinement']=paired_angle_comparison(problem,state,new,double)
        save('complete-one-localized-new-core-initial-audit')
        return answer
    except Exception as error:
        if isinstance(error,InputReplayFailure) and args.out.exists():
            try:answer['input_failure']=json.loads(args.out.read_text())
            except (ValueError,OSError):pass
        answer['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        save('failed-with-preserved-initial-only-diagnostics')
        return answer


def artificial_fixture(directory):
    """Four honest artificial replay records; no LP, QP or nonlinear solver."""
    base,state,unused_prior,source_receipt,selected_bytes,anchor=artificial_inputs()
    cfg=short_defaults();cfg.update(entry_length='3/25',entry_mean_nodes=32,uniform_panels=8,
        primitive_order=3,radial_nodes=9,angular_nodes=16,collar_subdivisions=6)
    pair=EntryRepairProblem(base,state,'3/25',entry_mean_nodes=32,uniform_panels=8,primitive_order=3)
    bounded=BoundedEntryHeightProblem(pair,state,uniform_panels=8,primitive_order=3)
    _,_,shared=build_grid(pair,9,6,16)
    short={'schema':'short-entry-paired-bounded-one-height-step-audit-v1',
        'status':'complete-two-initial-fields-and-at-most-one-height-step-each',
        'source_files_sha256':short_hashes(),'source_receipt':source_receipt,
        'source_exact_state':state_record(base,state),'configuration':cfg,
        'selected_original_fixed_metric':base.metric_model(state),'sampling_grid':shared,
        'cases':{'bounded_short':{'final_state':state_record(bounded,state)}},'artificial_inputs_only':True}
    paths=[directory/name for name in ['selected.json','anchor.json','short.json.gz','height.json.gz']]
    short_raw=json.dumps(short,sort_keys=True).encode()
    paths[0].write_bytes(selected_bytes);paths[1].write_bytes(anchor);paths[2].write_bytes(gzip.compress(short_raw))
    sha=[hashlib.sha256(x).hexdigest() for x in [selected_bytes,anchor,short_raw]]
    p,ref,receipt,source_cfg=load_short_model(json.loads(selected_bytes),anchor,short,*sha[:2],'bounded_short',artificial=True)
    receipt['exact_input_storage']={'short':{'decoded_sha256':sha[2]}}
    t,theta,grid=build_grid(p,9,6,16);data=p.geometry(ref,t,theta,3)
    h=p.port.side*float(data['center'][-1]);hc=height_configuration()
    poly,_=proposal_polytope(p,ref,data,hc,artificial=True,artificial_override=(h-.001,10.,-10.))
    if not poly.decision(ref[p.slices['height']])['eligible_under_declared_sampled_floating_tolerances']:
        raise ArithmeticError('artificial reference must satisfy the explicitly relaxed fixture rows')
    heights=ref[p.slices['height']]
    height={'schema':'fixed-T-a-all-height-polytope-stage-audit-v1',
        'status':'complete-one-height-polytope-stage-no-joint-metric-solve',
        'source_files_sha256':height_hashes(),'source_receipt':receipt,'configuration':hc,
        'initial_state':state_record(p,ref),'final_state':state_record(p,ref),'sampling_grid':grid,
        'artificial_inputs_only':True,'complete_frozen_metric_retained':True,
        'tangent_step_applied':False,'metric_step_applied':False,'joint_metric_solver_calls':0,
        'height_stage':{'polytope':poly.record(),'selected':{
            'height_coefficients_binary64':heights.tolist(),
            'height_coefficients_exact_binary64':[str(Q.from_float(float(x))) for x in heights],
            'exact_delta_from_reference':['0']*len(heights)}},
        'full_reconstruction_checks':{'independent_reconstruction_passes_declared_sample_tolerances':True},
        'explicit_artificial_fixture_no_optimizer_or_candidate_selection_called':True}
    raw=json.dumps(height,sort_keys=True).encode();paths[3].write_bytes(gzip.compress(raw));sha.append(hashlib.sha256(raw).hexdigest())
    args=argparse.Namespace(input=paths[0],anchor_input=paths[1],short_audit=paths[2],height_audit=paths[3],
        expected_input_sha256=sha[0],expected_anchor_sha256=sha[1],expected_short_sha256=sha[2],
        expected_height_sha256=sha[3],out=directory/'localized.json')
    return args


def developer_check():
    with tempfile.TemporaryDirectory(prefix='localized-core-artificial-',dir='/dev/shm') as folder:
        directory=Path(folder);args=artificial_fixture(directory);cfg=configuration(True)
        result=run_from_files(args,cfg,artificial=True)
        summary=json.loads(summary_path(args.out).read_text())
        summary_bound=summary['full_report']['sha256']==hashlib.sha256(args.out.read_bytes()).hexdigest()
        reference,unused,state,prior,receipt,source_cfg=prepare_run(args,artificial=True)
        local=LocalizedCoreField(reference,state,'4/5',cfg['local_length'],artificial=True)
        theta=np.arange(64)*2*np.pi/64
        samples=local.left+local.length*np.array([.19,.53,.87]);step=2e-6
        def tangent_rows(points):
            rows=np.r_[0.,points,local.seed.length]
            data=local.geometry(state,rows,theta,3)
            return {key:data[key][1:-1] for key in ['T','Ts','Tss']}
        center=tangent_rows(samples);plus=tangent_rows(samples+step);minus=tangent_rows(samples-step)
        errors={}
        for value,derivative in [('T','Ts'),('Ts','Tss')]:
            fd=(plus[value]-minus[value])/(2*step)
            errors[derivative]=float(np.max(abs(fd-center[derivative]))/max(1.,np.max(abs(center[derivative]))))
        rows=np.r_[0.,samples,local.seed.length]
        exact=local.geometry(state,rows,theta,3)['Ttheta'][1:-1]
        plus_angle=local.geometry(state,rows,theta+step,3)['T'][1:-1]
        minus_angle=local.geometry(state,rows,theta-step,3)['T'][1:-1]
        errors['Ttheta']=float(np.max(abs((plus_angle-minus_angle)/(2*step)-exact))/max(1.,np.max(abs(exact))))
        wrong=copy.copy(args);wrong.expected_height_sha256='0'*64;wrong.out=directory/'bad-sha.json'
        failed=run_from_files(wrong,cfg,artificial=True)
        bad_sha=(failed['status']=='failed-with-preserved-initial-only-diagnostics'
            and failed.get('input_failure',{}).get('phase')=='height_polytope-byte-binding')
        changed=state.copy();changed[0]=np.nextafter(changed[0],np.inf)
        try:local.identity(changed);state_rejected=False
        except ValueError:state_rejected=True
        try:LocalizedCoreField(reference,state,'37/100',artificial=True);real_target_rejected=False
        except ValueError:real_target_rejected=True
        variant=local.evaluation_variant(state,height_angular_nodes=48)
        same_variant=variant.identity(state)==local.identity(state)
    comparison=result.get('exterior_identity_comparison',{})
    outside=max(comparison.get('all_six_position_jet_max_differences',{'missing':np.inf}).values())
    query=result.get('sparse_dense_query_comparison',{})
    query_max=max(query.get('all_six_position_jet_max_differences',{'missing':np.inf}).values())
    core=result.get('new_doubled_angle_audit',{}).get('core_prefix',{}).get('complete_open_core_prefix_position_two_jet_errors',{})
    core_max=max(core.values(),default=np.inf)
    passed=bool(result['status']=='complete-one-localized-new-core-initial-audit' and summary_bound
        and outside<1e-11 and query_max<1e-11 and core_max<1e-8 and max(errors.values())<2e-5
        and comparison.get('entire_common_center_max_difference')==0
        and max(comparison.get('entire_b_jet_max_differences',{'missing':np.inf}).values())==0
        and bad_sha and state_rejected and real_target_rejected and same_variant)
    return {'schema':'localized-core-full-IO-and-rotation-artificial-check-v1',
        'artificial_inputs_only':True,'research_candidate_evaluated':False,'optimizer_calls':0,
        'full_four_input_read_only_IO':result['status'],'new_core_position_two_jet_max_error':core_max,
        'full_IO_error':result.get('error'),
        'exterior_all_six_position_jet_max_difference':outside,
        'sparse_dense_all_six_jet_max_difference':query_max,
        'analytic_rotation_radial_and_angular_derivative_relative_differences':errors,
        'summary_byte_binding':summary_bound,'wrong_SHA_small_failure_saved':bad_sha,
        'changed_reference_coefficient_rejected':state_rejected,
        'research_core_rejected_on_artificial_path':real_target_rejected,
        'height_mean_evaluation_variant_same_physical_identity':same_variant,
        'retained_center_and_all_b_jets_exact_in_evaluation':comparison.get('entire_common_center_max_difference')==0,
        'new_metric_identity_differs':result.get('old_complete_metric_sha256')!=result.get('new_complete_metric_sha256'),
        'same_state_Pi_refinement':result.get('same_parameter_Pi_refinement'),'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path);parser.add_argument('--anchor-input',type=Path)
    parser.add_argument('--short-audit',type=Path);parser.add_argument('--height-audit',type=Path)
    for name in ['input','anchor','short','height']:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.check_only:
        try:
            result=developer_check();result['source_files_sha256']=implementation_hashes()
            atomic_save(args.out,result)
            print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
            if not result['passed']:raise SystemExit(1)
        except Exception as error:
            atomic_save(args.out,{'schema':'localized-core-development-error-v1','artificial_inputs_only':True,
                'passed':False,'source_files_sha256':implementation_hashes(),
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        return
    result=run_from_files(args,configuration(),artificial=False)
    print(json.dumps({'out':str(args.out),'status':result['status']}),flush=True)
    if result['status']!='complete-one-localized-new-core-initial-audit':raise SystemExit(1)


if __name__=='__main__':main()
