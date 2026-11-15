#!/usr/bin/env python3
"""Mapped primary/SOC arrays: existing154 tangent coefficients plus five null heights.

The old 163 physical bounds and norms act through an injective 163x159 map.
These are arrays only. No report loader or real geometry is evaluated here.
The artificial CLI has not been executed merely by storing this source.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import json
from pathlib import Path
import numpy as np

from frame_height_null_coordinates import FiveHeightCoordinates,digest
from frame_entry_tail_blocks import EntryTail154Subspace
from frame_entry_body_subspace import (
    RationalRowGrid,FullGridValues,ConstantCapGate,ArrayLP,finite,array_digest,
    initial_restriction_decision,constant_soft_budget_feasible,
    fixed_domain_summary as old_domain_summary)
from frame_second_order_correction_scaling import ScaledCorrectionLP

SCHEMA='same-physical163-entry-tail-five-null-height159-array-model-v1'
N=159
P=163


class EntryTailHeight159Subspace:
    """Exact support and independent coordinates; the complete physical map is explicit."""
    def __init__(self,actual_original_layout,coordinates):
        old=EntryTail154Subspace(actual_original_layout)
        if not isinstance(coordinates,FiveHeightCoordinates):
            raise ValueError('validated exact five-height coordinate map required')
        if (coordinates.basis.left_exact!=old.left or coordinates.basis.right_exact!=old.right
                or coordinates.basis.delta!=Q(81,1000)):
            raise ValueError('height and tangent supports must be the declared common interval')
        self.coordinates=coordinates
        self.body_columns=old.body_columns.copy();self.tail_columns=old.tail_columns.copy()
        self.height_coordinates=np.arange(154,159,dtype=np.int64)
        self.columns=np.arange(N,dtype=np.int64)
        self.left,self.right,self.length=old.left,old.right,old.length
        self.M=coordinates.M.copy()
        # The common radius is r_H=4*r_B. These are physical-coefficient weights.
        self.physical_weights=np.ones(P)
        self.physical_weights[self.body_columns]=1/4
        self.physical_weights[self.tail_columns]=1/32
        # Every independent coordinate has an original physical pivot of magnitude one.
        self.pivots=np.r_[np.arange(154),[154,155,156,160,161]].astype(np.int64)
        self.pivot_signs=np.r_[np.ones(154),[-1.,-1.,-1.,1.,1.]]
        if not np.array_equal(self.M[self.pivots],np.diag(self.pivot_signs)):
            raise ArithmeticError('declared physical pivots are not the exact coordinate pivots')
        self.definition={'schema':SCHEMA,
            'validated_original_layout':copy.deepcopy(old.layout),
            'coordinate_definition_sha256':coordinates.definition_sha256,
            'physical_map_exact':copy.deepcopy(coordinates.basis.identity['height_map_exact']),
            'physical_dimension':P,'independent_dimension':N,
            'body_coordinates':self.body_columns.tolist(),'tail_coordinates':self.tail_columns.tolist(),
            'height_coordinates':self.height_coordinates.tolist(),
            'physical_height_indices_unchanged':[158,159],
            'variable_radial_open_interval_exact':[str(self.left),str(self.right)],
            'physical_block_weights_for_common_height_radius':{'body':'1/4','tail':'1/32','height':'1'},
            'all_nine_original_height_boxes_are_coupled_rows':True,
            'constant_cap_is_mathematical_null_not_a_rounded_row_product':True,
            'row_classification_uses_proved_support_not_small_Jacobian':True}
        self.definition_sha256=digest(self.definition)
        for a in [self.body_columns,self.tail_columns,self.height_coordinates,self.columns,
                  self.M,self.physical_weights,self.pivots,self.pivot_signs]:a.flags.writeable=False

    def apply(self,state,step):
        state=finite(state,(N,));step=finite(step,(N,))
        out=state.copy();out[:]=state+step
        if not np.all(np.isfinite(out)):raise FloatingPointError('nonfinite independent candidate')
        return out

    def scales(self,lower,upper):
        lo,hi=finite(lower,(P,)),finite(upper,(P,))
        width=hi-lo
        if np.any(width<=0):raise ValueError('strictly ordered original physical boxes required')
        qscale=width[self.pivots]
        K=(self.M*qscale[None,:])/width[:,None]
        if not np.array_equal(K[self.pivots],np.diag(self.pivot_signs)):
            raise ArithmeticError('normalized pivots changed')
        return width,qscale,K

    def step_norms(self,step,width):
        step=finite(step,(N,));width=finite(width,(P,))
        if np.any(width<=0):raise ValueError('positive physical scales required')
        v=self.M@step/width
        body=float(np.max(abs(v[self.body_columns])))
        tail=float(np.max(abs(v[self.tail_columns])))
        height=float(np.max(abs(v[154:])))
        return {'body_physical_normalized':body,'tail_physical_normalized':tail,
            'height_physical_normalized':height,
            'physical_infinity':float(np.max(abs(v))),'physical_L1':float(np.sum(abs(v))),
            'common_body_radius_norm':max(body,8*tail,height/4),
            'common_height_radius_norm':max(4*body,32*tail,height),
            'five_coordinate_norm_is_not_the_physical_height_norm':True}


class SelectedMappedRows:
    def __init__(self,subspace,full_grid,original_ids,independent_jacobian):
        self.full=full_grid
        self.parts=full_grid.grid.classify(original_ids,subspace)
        self.ids=self.parts['ids']
        self.J=finite(independent_jacobian,(len(self.ids),N))
        self.values=full_grid.rows.reshape(-1)[self.ids]
        self.tolerances=full_grid.tolerances.reshape(-1)[self.ids]


def fixed_domain_summary(subspace,full_grids):
    result=old_domain_summary(subspace,full_grids)
    result['schema']=SCHEMA+'-fixed-domain'
    result['current_height_Jensen_lower_bound_evaluated']=result.pop('fixed_height_Jensen_lower_bound_evaluated')
    result['current_height_bound_location']=result.pop('fixed_height_bound_location')
    result.pop('fixed_b_Jensen_diagnostic_is_not_used_as_a_validated_numeric_rejection')
    for item in result['grids']:
        item['current_height_Jensen_lower_bound_evaluated']=item.pop('fixed_height_Jensen_lower_bound_evaluated')
        item['current_height_bound_location']=item.pop('fixed_height_bound_location')
        item['mean_Xs_minus_current_b_ez_max']=item.pop('mean_Xs_minus_fixed_b_ez_max')
    result.update(current_height_may_change_inside_the_support=True,
        current_b_bound_is_not_a_fixed_global_obstruction_or_preflight_rejection=True,
        outside_scope='t<=9/250 or t>=423/500; null primitive as well as all density jets vanishes',
        complete_two_grid_values_and_original_tolerances_unchanged=True)
    return result


def _center(subspace,state,lower,upper,cap):
    state=finite(state,(N,));lower=finite(lower,(P,));upper=finite(upper,(P,))
    if np.any(lower>=upper):raise ValueError('ordered original physical bounds required')
    exact=subspace.coordinates.exact_box_decision(state,lower,upper)
    if not exact['exact_original_box_pass']:
        raise ValueError('accepted exact affine physical coefficients must obey original boxes')
    report=cap.report()
    if not report['original_tolerance_pass']:raise ValueError('constant cap fails the original numerical gate')
    return state,lower,upper,report,exact


def _collect(subspace,full_grids,selections):
    summary=fixed_domain_summary(subspace,full_grids)
    if not summary['outside_hard_original_tolerance_pass']:
        raise ValueError('constant exterior hard rows fail original tolerances')
    if len(selections)!=2 or any(s.full is not f for s,f in zip(selections,full_grids)):
        raise ValueError('selected rows must be from both complete current grids')
    values=[];jac=[];groups=[];tols=[];tags=[];invariant=[];outside_max=0.
    for s in selections:
        hard=s.parts['groups']>=2
        if np.any(s.values[hard]<-s.tolerances[hard]):
            raise ValueError('accepted selected hard values violate original tolerances')
        variable=s.parts['variable']
        if np.any(~variable):outside_max=max(outside_max,float(np.max(abs(s.J[~variable]))))
        for i in np.flatnonzero(~variable):
            invariant.append({**s.full.grid.coordinate(int(s.ids[i])),
                'role':'outside-soft-aggregated' if s.parts['groups'][i]<2 else 'outside-hard-original-tolerance'})
        values.extend(s.values[variable]);jac.extend(s.J[variable])
        groups.extend(s.parts['groups'][variable]);tols.extend(s.tolerances[variable])
        tags.extend(s.full.grid.coordinate(int(i)) for i in s.ids[variable])
    return (summary,np.array(values,float),np.array(jac,float).reshape(-1,N),
            np.array(groups,int),np.array(tols,float),tags,invariant,outside_max)


def _physical_gaps(coordinates,state,lower,upper):
    physical=coordinates.physical_exact(state)
    up=np.array([float(Q.from_float(float(upper[j]))-physical[j]) for j in range(P)])
    down=np.array([float(physical[j]-Q.from_float(float(lower[j]))) for j in range(P)])
    return up,down


def build_primary(subspace,full_grids,selections,state,lower,upper,cap,*,
        trust_exact,fraction_to_boundary_exact='1/2',physical_norm_weight_exact='1/1000',
        strip_floor_exact='1/10000000',curvature_floor_exact='1/10000000'):
    state,lower,upper,cap_record,exact_box=_center(subspace,state,lower,upper,cap)
    summary,values,J,groups,tols,tags,invariant,outside_max=_collect(subspace,full_grids,selections)
    rB=float(Q(trust_exact));r=4*rB
    gamma,weight=float(Q(fraction_to_boundary_exact)),float(Q(physical_norm_weight_exact))
    strip,curve=float(Q(strip_floor_exact)),float(Q(curvature_floor_exact))
    if not(rB>0 and np.isfinite(r) and 0<gamma<=1 and weight>=0 and min(strip,curve)>=0):
        raise ValueError('positive finite radius and declared nonnegative model constants required')
    width,qscale,K=subspace.scales(lower,upper);step_scale=r*qscale
    m=len(values);soft=groups<2;hard=~soft
    target=values-gamma*(values+tols);target[soft]=0.
    for gs,floor in [([4,5],strip),([7,8,9,10],curve)]:
        mask=np.isin(groups,gs);target[mask]=np.maximum(target[mask],floor)
    # Scalar physical trust/box rows, followed by a true physical infinity epigraph.
    A=np.zeros((m+4*P,N+2));b=np.zeros(m+4*P)
    A[:m,:N]=-J*step_scale[None,:];b[:m]=values
    b[:m][hard]=values[hard]-target[hard];A[:m,N][soft]=-1.
    upper_gap,lower_gap=_physical_gaps(subspace.coordinates,state,lower,upper)
    A[m:m+P,:N]=K;A[m+P:m+2*P,:N]=-K
    b[m:m+P]=np.minimum(subspace.physical_weights,upper_gap/(width*r))
    b[m+P:m+2*P]=np.minimum(subspace.physical_weights,lower_gap/(width*r))
    A[m+2*P:m+3*P,:N]=K;A[m+3*P:,:N]=-K
    A[m+2*P:,-1]=-1.
    pivot_weights=subspace.physical_weights[subspace.pivots]
    lo=np.r_[-pivot_weights,summary['rho_out'],0.]
    hi=np.r_[pivot_weights,np.inf,1.]
    c=np.r_[np.zeros(N),1.,weight*r]
    rho0=max(summary['rho_out'],0.,float(np.max(-values[soft])) if np.any(soft) else 0.)
    signature={'subspace':subspace.definition_sha256,
        'state':array_digest(state),'lower':array_digest(lower),'upper':array_digest(upper),
        'selected_tags':tags,'values':array_digest(values),'J159':array_digest(J),
        'tolerances':array_digest(tols),'rho_out':summary['rho_out'],'cap':cap_record,
        'fraction_to_boundary_exact':str(Q(fraction_to_boundary_exact)),
        'physical_norm_weight_exact':str(Q(physical_norm_weight_exact)),
        'strip_floor_exact':str(Q(strip_floor_exact)),'curvature_floor_exact':str(Q(curvature_floor_exact))}
    info={'schema':SCHEMA+'-primary','trust_exact':str(Q(trust_exact)),
        'body_radius_evaluated':rB,'tail_radius_evaluated':rB/8,'height_radius_evaluated':r,
        'common_normalizing_radius_evaluated':r,
        'independent_step_definition':'delta_q=4*rB*diag(original_pivot_widths)*z',
        'physical_normalized_step_definition':'Dphys^-1 M delta_q = 4*rB*K*z',
        'primary_objective':'rho+.001*4*rB*h; h>=abs(K*z) in all163 physical slots',
        'physical_norm_weight_exact':str(Q(physical_norm_weight_exact)),
        'auxiliary_objective_coefficient':weight*r,
        'all_original_physical_boxes_kept_as_coupled_rows':True,
        'physical_box_and_trust_row_count':2*P,'physical_norm_row_count':2*P,
        'LP_free_independent_coordinates':N,'physical_dimension':P,
        'rho_out':summary['rho_out'],'initial_selected_and_constant_metric_slack':rho0,
        'fixed_domain':summary,'cap_invariant':cap_record,'exact_center_box':exact_box,
        'active_original_rows':tags,'invariant_original_rows':invariant,
        'in_domain_zero_J_rows_kept':int(np.sum(np.all(J==0,axis=1))),
        'outside_selected_J_max_diagnostic_only':outside_max,
        'row_classification_did_not_use_J_values':True,'no_constant_cap_LP_row_added':True,
        'radius_independent_model_sha256':digest(signature)}
    result=ArrayLP(A,b,c,lo,hi,information=info)
    result.subspace,result.full_grids,result.selections=subspace,full_grids,selections
    result.state,result.original_lower,result.original_upper=state,lower,upper
    result.active_values,result.active_J,result.active_groups,result.active_tolerances=values,J,groups,tols
    result.targets,result.width,result.qscale,result.K=target,width,qscale,K
    result.step_scale,result.trust,result.common_radius=step_scale,rB,r
    return result


def primary_independent_step(model,variables):
    x=finite(variables,model.c.shape)
    return model.step_scale*x[:N]


def predicted_slack(primary,step):
    p=finite(step,(N,));soft=primary.active_groups<2
    linear=primary.active_values+primary.active_J@p
    return max(primary.information['rho_out'],0.,float(np.max(-linear[soft])) if np.any(soft) else 0.)


def radius_mapped_witness(old_model,new_model,variables):
    if old_model.information['radius_independent_model_sha256']!=new_model.information['radius_independent_model_sha256']:
        raise ValueError('one fixed center/map/rows/widths/cost is required')
    if new_model.trust<old_model.trust:raise ValueError('only enlargement is the containment claim')
    x=finite(variables,old_model.c.shape).copy()
    ratio=old_model.trust/new_model.trust
    x[:N]*=ratio;x[-1]*=ratio
    return x


def build_correction(primary,trial_full_grids,primary_step,*,
        physical_margin_retention_exact='1/4',predicted_descent_retention_exact='1/2',
        correction_relative_radius_exact='1/2',strip_floor_exact='1/10000000',
        curvature_floor_exact='1/10000000',improvement_floor=1e-10):
    p=finite(primary_step,(N,))
    if len(trial_full_grids)!=2 or any(a.grid.definition!=b.grid.definition
            for a,b in zip(primary.full_grids,trial_full_grids)):
        raise ValueError('actual y rows on the identical two complete grids required')
    # Common b is allowed to change. It must still agree between the two angle grids.
    if not np.array_equal(trial_full_grids[0].b,trial_full_grids[1].b):
        raise ValueError('the two same-y grids do not share one common current height')
    trial=[]
    for old,actual in zip(primary.selections,trial_full_grids):
        trial.extend(actual.rows.reshape(-1)[old.ids[old.parts['variable']]])
    trial=np.array(trial,float);base,J,groups=primary.active_values,primary.active_J,primary.active_groups
    soft=groups<2;outside=primary.information['rho_out']
    rho0=primary.information['initial_selected_and_constant_metric_slack']
    rho1=predicted_slack(primary,p);gain=rho0-rho1
    norms=primary.subspace.step_norms(p,primary.width)
    retention=float(Q(predicted_descent_retention_exact));gamma=float(Q(physical_margin_retention_exact))
    relative=float(Q(correction_relative_radius_exact))
    if not(0<retention<=1 and 0<=gamma<=1 and relative>0):
        raise ValueError('valid declared SOC retention/radius required')
    info={'schema':SCHEMA+'-SOC','initial_metric_slack':rho0,
        'primary_predicted_metric_slack':rho1,'primary_predicted_improvement':gain,
        'primary_norms':norms,'rho_out':outside,'actual_y_rows_not_linear_predictions':True}
    if norms['common_body_radius_norm']==0 or gain<=improvement_floor:
        return None,dict(info,status='no-primary-predicted-restoration-for-SOC')
    body_radius=relative*norms['common_body_radius_norm'];radius=4*body_radius
    budget=rho0-retention*gain
    info.update(metric_slack_budget=budget,body_correction_radius=body_radius,
        tail_correction_radius=body_radius/8,height_correction_radius=radius,
        maximum_box_normalized_correction=radius)
    if not constant_soft_budget_feasible(outside,budget):
        return None,dict(info,status='SOC-budget-below-fixed-outside-soft-bound')
    target=gamma*np.maximum(base,0.)
    for gs,floor in [([4,5],float(Q(strip_floor_exact))),([7,8,9,10],float(Q(curvature_floor_exact)))]:
        if floor<0:raise ValueError('nonnegative proposal floors required')
        mask=np.isin(groups,gs);target[mask]=np.maximum(target[mask],floor)
    m=len(base);A=np.zeros((m+4*P,N+P));b=np.zeros(m+4*P)
    A[:m,:N]=-J*primary.qscale[None,:];b[:m]=trial-target;b[:m][soft]=trial[soft]+budget
    y=primary.subspace.apply(primary.state,p)
    up,down=_physical_gaps(primary.subspace.coordinates,y,primary.original_lower,primary.original_upper)
    K=primary.K
    A[m:m+P,:N]=K;A[m+P:m+2*P,:N]=-K
    b[m:m+P]=np.minimum(radius*primary.subspace.physical_weights,up/primary.width)
    b[m+P:m+2*P]=np.minimum(radius*primary.subspace.physical_weights,down/primary.width)
    A[m+2*P:m+3*P,:N]=K;A[m+3*P:,:N]=-K
    A[m+2*P:m+3*P,N:]=-np.eye(P);A[m+3*P:,N:]=-np.eye(P)
    pivot=primary.subspace.physical_weights[primary.subspace.pivots]
    lo=np.r_[-radius*pivot,np.zeros(P)];hi=np.r_[radius*pivot,np.full(P,radius)]
    model=ArrayLP(A,b,np.r_[np.zeros(N),np.ones(P)],lo,hi,information=info)
    model.subspace,model.width,model.qscale,model.radius=primary.subspace,primary.width,primary.qscale,radius
    model.active_trial_values,model.targets=trial,target
    model.original_row_group_labels=np.r_[groups,np.full(2*P,100),np.full(2*P,101)]
    info.update(status='original-unit-mapped159-SOC-arrays-ready',
        independent_correction_variables=N,physical_absolute_auxiliaries=P,
        original_unit_objective='sum_j h_j; h_j>=abs((Dphys^-1 M diag(pivot_widths)*v)_j)',
        correction_map='delta_q=diag(pivot_widths)*v',
        all_original_coupled_boxes_applied_to_y_plus_correction=True,
        no_constant_cap_or_external_hard_restoration_row_added=True,
        original_unit_residual_and_actual_two_grid_gates_still_required=True)
    return model,info


class MappedScaledCorrectionLP(ScaledCorrectionLP):
    @property
    def physical_dimension(self):
        # The inherited residual routine uses this property as the auxiliary start.
        return N

    def definition(self):
        out=super().definition()
        out.pop('physical_dimension')
        out.update(schema=SCHEMA+'-positive-SOC-scaling',
            independent_coordinate_dimension=N,physical_absolute_auxiliary_dimension=P,
            old_variables='159 pivot-normalized corrections v and163 absolute physical auxiliaries h',
            new_variables='v=radius*z and h=radius*t',
            physical_normalized_correction='K*v; not the159 coordinate vector v itself',
            new_objective='sum of163 t; old objective equals radius times this sum',
            scope='this already assembled coupled mapped159 SOC LP only',
            no_equivalence_to_old154_or_uniform163_proposal_domains=True)
        return out


def scale_mapped_correction(model):
    A,b,lo,hi=(np.asarray(x,float) for x in [model.A,model.b,model.lower,model.upper])
    r=float(model.radius)
    if (A.ndim!=2 or A.shape[1]!=N+P or b.shape!=(len(A),) or lo.shape!=(N+P,)
            or hi.shape!=lo.shape or not np.isfinite(r) or r<=0
            or not all(np.all(np.isfinite(x)) for x in [A,b,lo,hi]) or np.any(lo>hi)):
        raise ValueError('finite mapped159 plus163-auxiliary SOC arrays and positive radius required')
    if (not np.array_equal(lo[N:],np.zeros(P)) or not np.array_equal(hi[N:],np.full(P,r))
            or np.any(lo[:N]<-r) or np.any(hi[:N]>r)):
        raise ValueError('declared common radius and complete auxiliary bounds required')
    scaled=A*r
    magnitude=np.maximum(np.max(abs(scaled),axis=1),abs(b))
    _,exponent=np.frexp(magnitude);exponent=np.clip(exponent,-1022,1023).astype(np.int64)
    exponent[magnitude==0]=0;divisor=np.ldexp(np.ones(len(b)),exponent)
    result=MappedScaledCorrectionLP(A.copy(),b.copy(),lo.copy(),hi.copy(),r,divisor,exponent,
        scaled/divisor[:,None],b/divisor,lo/r,hi/r,np.r_[np.zeros(N),np.ones(P)])
    for value in [result.original_A,result.original_b,result.original_lower,result.original_upper,
            result.row_divisors,result.row_binary_exponents,result.A,result.b,result.lower,result.upper,result.objective]:
        if not np.all(np.isfinite(value)):raise FloatingPointError('nonfinite positive mapped SOC scaling')
        value.flags.writeable=False
    return result


def correction_independent_step(model,original_variables):
    v=finite(original_variables,model.c.shape)
    return model.qscale*v[:N]


def artificial_arrays():
    """Source-defined tiny values/J rows, with the real count/layout but no surface."""
    from frame_height_null_coordinates import ExactFiveHeightBasis,EXPECTED_LAYOUT
    from frame_entry_body_subspace import expected_layout
    left,right=Q(9,250),Q(423,500);delta=(right-left)/10
    basis_def={'schema':'paired-entry-weighted-center-speed-basis-v1',
        'original_basis':{'schema':'independent-center-speed-quintic-basis-v1',
            'interval_exact':[str(left),str(right)],'degree':5,'free_count':9,
            'clamped_knots_exact':[str(left)]*6+[str(left+i*delta) for i in range(1,10)]+[str(right)]*6,
            'retained_columns':'3 through count+2 inclusive; discard first and last three',
            'zero_extension_of_speed_basis_outside_interval':True},
        'entry_length_exact':str(delta),'entry_weight_power':4,
        'cutoff_definition':'plateau through x=ell/3, then 1-S9((3*x/ell-1)/2), zero at ell',
        'weight_definition':'1-chi+chi*(x/ell)^4'}
    basis=ExactFiveHeightBasis(basis_def);reference=np.zeros(P)
    canonical={'schema':'artificial-no-geometry-original-family','height_basis_definition':basis_def,
        'exact_coefficients':{'u':['0']*81,'v':['0']*73,'height':['0']*9}}
    coordinates=FiveHeightCoordinates(reference,canonical,copy.deepcopy(EXPECTED_LAYOUT),basis)
    sub=EntryTailHeight159Subspace(expected_layout(),coordinates)
    grids=[RationalRowGrid('coarse',['0','9/100','39/50','9/10'],4),
           RationalRowGrid('fine',['0','9/100','39/50','9/10'],8)]
    full=[];selected=[]
    for grid in grids:
        rows=np.ones((11,grid.nr,grid.nt));rows[:2]=-0.005
        rows[:2,1:3]=-0.01;rows[4,0]=-5e-10
        eta=np.full((grid.nr,grid.nt),.265);eta[1:3]=.27
        f=FullGridValues(grid,rows,eta,np.ones(grid.nr),np.full(11,1e-9))
        ids=np.array([grid.nt,grid.point_count+2*grid.nt,4*grid.point_count,
            8*grid.point_count+2*grid.nt],np.int64)
        J=np.zeros((4,N));J[0,0]=1.;J[1,154]=-.25
        full.append(f);selected.append(SelectedMappedRows(sub,f,ids,J))
    state=coordinates.initial_state();lo=np.r_[np.full(154,-8.),np.full(9,-1.)];hi=-lo
    cap=ConstantCapGate(-2e-17,-2e-17,1e-9,0.,1e-10)
    return sub,full,selected,state,lo,hi,cap


def developer_check():
    """Only new mapped-array identities; zero research surfaces or optimizers."""
    sub,full,selected,state,lo,hi,cap=artificial_arrays()
    model=build_primary(sub,full,selected,state,lo,hi,cap,trust_exact='1/4000')
    x=np.zeros(N+2);x[N]=.01
    p=np.zeros(N);p[0]=1e-5;p[154]=-1e-5
    rho=predicted_slack(model,p)
    variable=np.zeros(N+2);variable[:N]=p/model.step_scale
    variable[N]=rho;variable[-1]=sub.step_norms(p,model.width)['physical_infinity']/model.common_radius
    larger=build_primary(sub,full,selected,state,lo,hi,cap,trust_exact='1/2000')
    lifted=radius_mapped_witness(model,larger,variable)
    actual=[]
    for old,select in zip(full,selected):
        rows=old.rows.copy();flat=rows.reshape(-1)
        flat[select.ids]+=select.J@p
        actual.append(FullGridValues(old.grid,rows,old.eta,old.b+.001,old.tolerances))
    soc,info=build_correction(model,actual,p)
    if soc is None:raise AssertionError('the artificial primary has positive predicted improvement')
    scaled=scale_mapped_correction(soc)
    trial=np.zeros(N+P);trial[N:]=.2
    oldvars=scaled.to_original(trial)
    relation=np.max(abs(scaled.A@trial-scaled.b-(soc.A@oldvars-soc.b)/scaled.row_divisors))
    q=state.copy();q[154:]=[.1,-.1,.05,.02,-.01]
    exact_null=sum(sub.coordinates.basis.integrals[j]*
        (sub.coordinates.exact_heights(q)[j]-sub.coordinates.reference_exact[j]) for j in range(9))
    # A step in a null coordinate must pay compensation slots in its physical norm.
    t=np.zeros(N);t[-2]=1.
    norms=sub.step_norms(t,np.ones(P))
    checks={
        'original_163_coupled_box_and_trust_rows_present':model.A.shape[0]==len(model.active_values)+4*P,
        '159_coordinates_not_159_independent_physical_boxes':model.c.shape==(161,) and soc.c.shape==(322,),
        'zero_primary_with_soft_slack_is_feasible':model.residual(x)['maximum_original_linear_row_violation']<=1e-15,
        'outside_tolerance_qualified_strip_not_given_new_floor':len(model.information['invariant_original_rows'])==2,
        'interior_zero_Jacobian_curvature_rows_kept':model.information['in_domain_zero_J_rows_kept']==2,
        'constant_cap_original_negative_margin_passes_unchanged_tolerance':model.information['cap_invariant']['original_tolerance_pass'],
        'actual_same_y_soft_residual_used':np.allclose(soc.b[:len(model.active_values)][model.active_groups<2],
            soc.active_trial_values[model.active_groups<2]+info['metric_slack_budget'],rtol=0,atol=0),
        'current_height_can_change_but_same_y_grids_agree':info['status']=='original-unit-mapped159-SOC-arrays-ready',
        'positive_scaling_bijection_in_original_units':bool(relation<1e-12 and np.max(abs(scaled.to_scaled(oldvars)-trial))<4*np.finfo(float).eps),
        'physical_L1_counts_compensation_slot':norms['physical_L1']==2.5 and norms['physical_infinity']==1.5,
        'exact_null_unchanged_by_nonbinary_nine_coefficients':exact_null==0,
        'radius_enlargement_same_physical_step':np.allclose(primary_independent_step(model,variable),
            primary_independent_step(larger,lifted),rtol=0,atol=1e-20),
        'radius_enlargement_same_total_objective':bool(abs(model.c@variable-larger.c@lifted)<1e-15),
        'old_and_new_current_b_diagnostics_not_mislabeled_fixed':
            'fixed_height_Jensen_lower_bound_evaluated' not in model.information['fixed_domain']}
    return {'schema':SCHEMA+'-artificial-development','passed':all(checks.values()),'checks':checks,
        'positive_scaling_relation_error':float(relation),'physical_dimension':P,'independent_dimension':N,
        'primary_variables':len(model.c),'SOC_variables':len(soc.c),
        'research_geometry_calls':0,'optimizer_calls':0,'evaluated_only_when_explicitly_called':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args();result=developer_check()
    text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.out:args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(text)
    print(text,end='')
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
