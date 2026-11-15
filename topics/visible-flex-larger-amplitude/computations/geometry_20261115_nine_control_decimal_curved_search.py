#!/usr/bin/env python3
"""Complete Decimal50 QR, original curved-path budgets and R299 selection.

This is an independent arithmetic implementation, not the old824c/146 source.
The original real equations, unweighted merit, .2 Armijo, radius rules, complete
nine-coordinate metric,8x20 outer and12x20 normal budgets remain explicit.
All primal parameters and candidate comparisons stay Decimal; no binary64
linear solve, SVD cutoff, implicit p3 restoration or new inner accuracy gate.
"""
from __future__ import annotations
import copy
from decimal import Decimal as D, DecimalException
from geometry_20261115_nine_control_decimal_literal_model import (
    ZERO,ONE,TWO,ARM,TOL,EPS64,NumericalFailure,dec,clean,digest,
    dot,norm,maxabs,sub,add,scale,transpose,mv,mm,eye,merit)


def finite_vector(v):
    return all(x.is_finite() for x in v)


def qr_factor(matrix):
    """Complete column-pivoted Householder QR, without a numerical rank cutoff."""
    a=[list(row) for row in matrix]
    m,n=len(a),len(a[0]) if a else 0
    if m<n or n==0 or any(len(r)!=n for r in a) or not all(finite_vector(r) for r in a):
        raise NumericalFailure('Malformed or nonfinite complete QR input')
    q=eye(m);pivot=list(range(n))
    for j in range(n):
        chosen=max(range(j,n),key=lambda k:sum((a[i][k]*a[i][k] for i in range(j,m)),ZERO))
        if chosen!=j:
            for row in a:
                row[j],row[chosen]=row[chosen],row[j]
            pivot[j],pivot[chosen]=pivot[chosen],pivot[j]
        x=[a[i][j] for i in range(j,m)]
        size=norm(x)
        if size==0:
            # A basis completion keeps its unused directions; a later actual
            # triangular solve still rejects an exactly zero required diagonal.
            continue
        target=-size if x[0]>=0 else size
        v=list(x);v[0]-=target
        vv=dot(v,v)
        if vv==0 or not vv.is_finite():
            raise NumericalFailure('A finite Householder reflector could not be formed')
        tau=TWO/vv
        for k in range(j,n):
            coeff=tau*sum((v[ii]*a[j+ii][k] for ii in range(len(v))),ZERO)
            for ii in range(len(v)):
                a[j+ii][k]-=coeff*v[ii]
        for i in range(m):
            coeff=tau*sum((q[i][j+ii]*v[ii] for ii in range(len(v))),ZERO)
            for ii in range(len(v)):
                q[i][j+ii]-=coeff*v[ii]
        a[j][j]=target
        for i in range(j+1,m):
            a[i][j]=ZERO
    if not all(finite_vector(r) for r in a+q):
        raise NumericalFailure('The complete QR returned a nonfinite factor')
    return q,a,pivot


def qr_solve(matrix,rhs):
    q,r,pivot=qr_factor(matrix)
    m,n=len(matrix),len(matrix[0])
    if len(rhs)!=m or not finite_vector(rhs):
        raise NumericalFailure('Complete QR right-hand side is nonfinite or malformed')
    if any(r[j][j]==0 for j in range(n)):
        raise NumericalFailure('A required complete QR column is exactly singular; no truncation')
    y=[sum((q[k][j]*rhs[k] for k in range(m)),ZERO) for j in range(n)]
    xp=[ZERO]*n
    for j in range(n-1,-1,-1):
        xp[j]=(y[j]-sum((r[j][k]*xp[k] for k in range(j+1,n)),ZERO))/r[j][j]
    x=[ZERO]*n
    for j in range(n):
        x[pivot[j]]=xp[j]
    if not finite_vector(x):
        raise NumericalFailure('The complete triangular solve is nonfinite')
    return x,dict(complete_Q=[row[:n] for row in q],complete_R=r[:n],
        column_permutation=pivot,complete_upper_diagonal=[r[j][j] for j in range(n)],
        original_linear_residual=sub(mv(matrix,x),rhs),
        normal_matrix_formed=False,singular_value_truncation=False)


def two_solve(matrix,rhs):
    if len(matrix)!=2 or any(len(r)!=2 for r in matrix) or len(rhs)!=2:
        raise NumericalFailure('Both original normal equations and both coordinates are required')
    row_scales=[norm(r) for r in matrix]
    if any(x==0 or not x.is_finite() for x in row_scales):
        raise NumericalFailure('A complete normal row is zero or nonfinite')
    a=[[x/s for x in r] for r,s in zip(matrix,row_scales)]
    b=[x/s for x,s in zip(rhs,row_scales)]
    x,qr=qr_solve(a,b)
    return x,dict(original_two_by_two=matrix,original_rhs=rhs,
        positive_row_scales=row_scales,formed_matrix=a,formed_rhs=b,
        **qr,solution=x,unscaled_original_linear_residual=sub(mv(matrix,x),rhs),
        row_scaling_changes_full3_merit=False)


def complete_direction(model,p,residual,pilot,radius,record):
    if radius<=0 or not radius.is_finite():
        raise NumericalFailure('Retain the original positive finite radius requirement')
    scales=[max(ONE,abs(x)) for x in p]
    a=[[pilot[i][j]*scales[j] for j in range(9)] for i in range(3)]
    rs=[norm(row) for row in a]
    row_scales=[ONE if x==0 else x for x in rs]
    qb,rb,piv=qr_factor(transpose([[x/s for x in row] for row,s in zip(a,row_scales)]))
    V=[[scales[i]*qb[i][j] for j in range(9)] for i in range(9)]
    G=[[V[i][j]/scales[i] for j in range(9)] for i in range(9)]
    record.update(original_pilot_axis_J=pilot,original_relative_scales=scales,
        original_scaled_pilot=a,full_nine_basis_Q=qb,full_basis_R=rb,basis_row_permutation=piv,
        physical_basis_V=V,actual_relative_metric_G=G,
        original_metric_lower_block_is_G_not_assumed_identity=True,
        all_nine_columns_retained=True,weak_columns_not_discarded=True)
    with model.context('outer/complete-nine-physical-basis-forward'):
        K,basis_forward,basis_state=model.response(p,V,label='complete-nine-physical-basis')
    record.update(complete_basis_response=K,basis_forward=basis_forward,
        basis_primal_equations=basis_state['equation'],
        pilot_axis_product_not_used_as_reformed_K=mm(pilot,V),
        reformed_K_minus_pilot_product=[[x-y for x,y in zip(row,old)]
            for row,old in zip(K,mm(pilot,V))])
    anorm=norm([x for row in a for x in row])
    floor=EPS64*max(ONE,anorm)
    rhs=[-x for x in residual]+[ZERO]*9
    searches=[]
    record['damping_search']=searches

    def solve(mu,label):
        if mu<=0 or not mu.is_finite():
            raise NumericalFailure('Positive finite damping is required')
        augmented=K+[[mu*x for x in row] for row in G]
        w,qr=qr_solve(augmented,rhs)
        direction=mv(V,w);relative=[x/s for x,s in zip(direction,scales)]
        size=norm(relative)
        item=dict(index=len(searches),label=label,damping_mu=mu,
            actual_formed_relative_step_L2=size,within_original_radius=size<=radius,
            complete_upper_diagonal=qr['complete_upper_diagonal'],
            column_permutation=qr['column_permutation'])
        searches.append(item)
        return dict(w=w,direction=direction,relative=relative,norm=size,mu=mu,
                    augmented=augmented,qr=qr,index=item['index'])

    lower=floor;low=solve(lower,'original-binary64-epsilon-parameter-floor')
    if low['norm']<=radius:
        chosen=low
    else:
        upper=max(ONE,anorm,TWO*floor);chosen=None
        for unused in range(64):
            high=solve(upper,'original-positive-damping-radius-bracket')
            if high['norm']<=radius:
                chosen=high;break
            lower=upper;upper*=TWO
            if not upper.is_finite():
                break
        if chosen is None:
            raise NumericalFailure('The original64-step damping bracket was exhausted')
        for unused in range(64):
            # Same positive geometric mean in the real formula. Decimal sqrt
            # replaces exp/log evaluation; it is not the old64 rounding path.
            midpoint=(lower*upper).sqrt()
            if not lower<midpoint<upper:
                break
            candidate=solve(midpoint,'same-model-geometric-bracket-refinement')
            if candidate['norm']<=radius:
                upper,chosen=midpoint,candidate
            else:
                lower=midpoint
            if chosen['norm']>=dec(0.999)*radius:
                break
    direction=chosen['direction']
    with model.context('outer/actual-chosen-physical-direction-forward'):
        ad,actual_forward,actual_state=model.response(p,[[x] for x in direction],
                                                     label='actual-chosen-physical-direction')
    action=[row[0] for row in ad]
    formed=mv(K,chosen['w'])
    penalty=mv(G,chosen['w'])
    stationarity=add(mv(transpose(K),add(formed,residual)),
                     scale(mv(transpose(G),penalty),chosen['mu']*chosen['mu']))
    record.update(positive_damping_mu=chosen['mu'],positive_damping_floor=floor,
        floor_uses_original_binary64_epsilon_as_algorithm_parameter=True,
        original_pilot_scaled_Frobenius_readback=anorm,
        complete_augmented_matrix=chosen['augmented'],complete_augmented_rhs=rhs,
        complete_solve=chosen['qr'],basis_coordinate_direction=chosen['w'],
        actual_nine_parameter_direction=direction,
        actual_relative_direction=chosen['relative'],scaled_direction_L2=chosen['norm'],
        original_radius=radius,actual_direction_forward=actual_forward,
        actual_direction_primal_equations=actual_state['equation'],
        direct_original_equation_action_used=action,
        formed_basis_action=formed,direct_minus_formed_basis_action=sub(action,formed),
        pilot_axis_action=mv(pilot,direction),
        formed_augmented_stationarity=stationarity,
        formed_augmented_stationarity_L2=norm(stationarity),
        original_unweighted_full3_slope=dot(residual,action),
        parameter_projection_to_binary64=False,no_rank_or_action_agreement_gate=True,
        derivative_is_not_a_rounded_program_derivative=True)
    return direction,action


def curve_frame(p,residual,J,direction,action):
    scales=[max(ONE,abs(x)) for x in p]
    C=J[1:]
    a=[[row[j]*scales[j] for j in range(9)] for row in C]
    rs=[norm(row) for row in a]
    if any(x==0 or not x.is_finite() for x in rs):
        raise NumericalFailure('The original two constraint rows cannot form a normal frame')
    q,r,pivot=qr_factor(transpose([[x/s for x in row] for row,s in zip(a,rs)]))
    if any(r[j][j]==0 for j in range(2)):
        raise NumericalFailure('The complete normal-frame QR has a zero required diagonal')
    N=[row[:2] for row in q];tangent=[row[2:] for row in q]
    P=[[scales[i]*N[i][j] for j in range(2)] for i in range(9)]
    projected=mm(C,P)
    correction,origin=two_solve(projected,sub(action[1:],mv(C,direction)))
    origin_direction=add(direction,mv(P,correction))
    frame=dict(scales=scales,N=N,tangent=tangent,physical_normal=P,constraint_row_scales=rs)
    record=dict(parameter_dimension=9,normal_dimension=2,tangent_dimension=7,
        complete_Q=q,complete_R=r,constraint_row_permutation=pivot,
        original_constraint_J=C,relative_parameter_scales=scales,
        positive_frame_row_scales=rs,physical_normal_columns=P,
        original_constraint_J_times_normal=projected,
        normal_coordinate_origin_derivative_solve=origin,
        formed_origin_parameter_derivative=origin_direction,
        formed_origin_full3_slope=dot(residual,mv(J,origin_direction)),
        actual_action_origin_slope_used=dot(residual,action),
        original_predictor_direction=direction,
        predictor_scaled_normal_coordinates=mv(transpose(N),[x/s for x,s in zip(direction,scales)]),
        predictor_scaled_tangent_coordinates=mv(transpose(tangent),[x/s for x,s in zip(direction,scales)]),
        full_constraint_times_tangent=mm(a,tangent),
        target_formula='c(p)+alpha*direct-forward-action[1:]',
        path_formula='q=seed+physical_normal*w',
        no_target_is_zeroed=True,not_an_exact_floating_Q_or_derivative_certificate=True)
    return frame,record


def next_radius(radius,alpha,scaled_norm,actual,predicted):
    ratio=actual/predicted if predicted.is_finite() and predicted>0 else None
    if alpha<1 or ratio is None or not ratio.is_finite() or ratio<dec(0.25):
        revised,rule=radius/TWO,'halve after an accepted backtrack or a poor/undefined model ratio'
    elif ratio>dec(0.75) and scaled_norm>=dec(0.8)*radius:
        revised,rule=min(ONE,TWO*radius),'double up to relative radius one after an accurate near-boundary full step'
    else:
        revised,rule=radius,'retain the declared relative radius'
    return revised,dict(previous_radius=radius,next_radius=revised,
        actual_reduction=actual,predicted_reduction=predicted,actual_to_predicted_reduction=ratio,
        update_rule=rule,radius_update_is_not_an_extra_acceptance_test=True)


def curved_candidate(model,p,state,direction,action,frame,alpha,record,label):
    target=add(state['equation'][1:],scale(action[1:],alpha))
    seed=add(p,scale(direction,alpha))
    P,rs=frame['physical_normal'],frame['constraint_row_scales']
    w=[ZERO,ZERO]
    record.update(alpha=alpha,direct_seed_parameters=seed,
        original_base_constraint_values=state['equation'][1:],actual_constraint_target=target,
        requested_original_unit_constraint_error_tolerance=TOL,
        inner_iterations_budget=12,inner_backtracks_budget=20,
        inner_scaled_merit_row_scales=rs,iterations=[],
        real_evaluation_attempts=0,real_evaluation_returns=0,
        axis_forward_attempts=0,axis_forward_returns=0,
        normal_forward_attempts=0,normal_forward_returns=0,
        original_domain_or_evaluation_failures=0,
        original_outer_merit_remains_unweighted=True,
        normal_target_tolerance_is_not_an_outer_gate=True,
        parameters_and_normal_coordinates_remain_decimal50=True)
    if alpha==0:
        record.update(stop_reason='alpha is exactly zero; return unchanged current state without projection',
                      returned_parameters=p,returned_original_equations=state['equation'],
                      returned_constraint_error=[ZERO,ZERO],requested_constraint_error_tolerance_met=True)
        return state

    def evaluate(q,context):
        record['real_evaluation_attempts']+=1
        try:
            with model.context(label+'/'+context):
                result=model.evaluate(q)
            record['real_evaluation_returns']+=1
            return result
        except NumericalFailure as error:
            record['original_domain_or_evaluation_failures']+=1
            record.setdefault('evaluation_errors',[]).append(dict(context=context,error=repr(error)))
            raise

    try:
        current=evaluate(seed,'uncorrected-seed')
    except NumericalFailure:
        record['stop_reason']='uncorrected seed failed original domain/evaluation; normal iterations not started'
        raise
    record.update(uncorrected_seed_original_equations=current['equation'],
                  uncorrected_seed_original_full3_merit=merit(current))
    record['same_trace_selection_samples_columns']=[
        'sample','source','inner_iteration','inner_trial','parameters','original_equations',
        'existing_original_full3_merit','finite_merit','normal_coordinates','strict_shadow_replacement']
    samples=[];record['same_trace_selection_samples']=samples
    shadow={'best':None}

    def consider(candidate,coords,existing,source,inner=None,trial=None):
        finite=existing.is_finite()
        best=shadow['best']
        replace=finite and (best is None or existing<best['merit'])
        index=len(samples)
        samples.append([index,source,inner,trial,list(candidate['parameters']),
                        list(candidate['equation']),existing,finite,list(coords),replace])
        if replace:
            shadow['best']=dict(state=copy.deepcopy(candidate),coordinates=list(coords),
                                merit=existing,index=index)
        return index

    consider(current,w,merit(current),'uncorrected-seed')
    for inner in range(12):
        error=sub(current['equation'][1:],target)
        scaled=[x/s for x,s in zip(error,rs)]
        before=dot(scaled,scaled)/TWO
        row=dict(iteration=inner,parameters=list(current['parameters']),
            original_equations=list(current['equation']),original_full3_merit=merit(current),
            constraint_target=target,actual_original_unit_constraint_error=error,
            normal_coordinates=list(w),scaled_constraint_merit=before,trials=[],accepted=False)
        record['iterations'].append(row)
        consider(current,w,row['original_full3_merit'],'working-before-normal-update',inner)
        if maxabs(error)<=TOL:
            record['stop_reason']='requested original-unit normal target accuracy reached'
            break
        try:
            record['axis_forward_attempts']+=1
            with model.context(label+'/normal-'+str(inner)+'/fresh-all-nine-axis-response'):
                J,jr,js=model.response(current['parameters'],label='fresh-all-nine-axis-response')
            record['axis_forward_returns']+=1
            row.update(fresh_current_full_three_by_nine_J=J,axis_response_readback=jr)
            record['normal_forward_attempts']+=1
            row['direct_normal_response_readback']=dict(completed=False,physical_columns=P,
                current_parameters=list(current['parameters']),current_equations=current['equation'])
            with model.context(label+'/normal-'+str(inner)+'/direct-two-P-forward'):
                response,rr,rs_state=model.response(current['parameters'],P,label='direct-two-P-forward')
            record['normal_forward_returns']+=1
            projected=response[1:]
            row['direct_normal_response_readback'].update(completed=True,full_report=rr,
                axis_J_times_P=mm(J[1:],P),direct_full_three_by_two=response,
                direct_minus_axis_projection=[[a-b for a,b in zip(x,y)]
                    for x,y in zip(projected,mm(J[1:],P))],
                axis_primal_equations=js['equation'],normal_primal_equations=rs_state['equation'],
                same_primal_equation_values_as_working=rs_state['equation']==current['equation'],
                agreement_is_not_a_gate=True)
            dw,solve=two_solve(projected,[-x for x in error])
            slope=dot(scaled,[x/s for x,s in zip(mv(projected,dw),rs)])
            row.update(normal_coordinate_direction=dw,full_normal_QR=solve,
                scaled_constraint_merit_slope=slope,
                pilot_full3_normal_slope=dot(current['equation'],mv(J,mv(P,dw))),
                direct_full3_normal_slope=dot(current['equation'],mv(response,dw)),
                original_outer_full3_merit_gate_not_changed=True)
        except (NumericalFailure,DecimalException) as failure:
            row['normal_model_exception']=repr(failure)
            record['stop_reason']='actual full normal model failed; preserve last finite candidate'
            break
        if not before.is_finite() or not slope.is_finite() or slope>=0:
            record['stop_reason']='no finite strict normal-target model descent; preserve actual candidate'
            break
        previous=list(current['parameters'])
        for backtrack in range(20):
            beta=ONE/(TWO**backtrack)
            trial_w=add(w,scale(dw,beta))
            q=add(seed,mv(P,trial_w))
            bound=before+ARM*beta*slope
            item=dict(trial=backtrack,beta=beta,parameters=q,normal_coordinates=trial_w,
                      accepted=False,scaled_constraint_Armijo_bound=bound)
            row['trials'].append(item)
            try:
                proposed=evaluate(q,'normal-'+str(inner)+'/backtrack-'+str(backtrack))
                proposed_error=sub(proposed['equation'][1:],target)
                ss=[x/s for x,s in zip(proposed_error,rs)]
                trial_merit=dot(ss,ss)/TWO
                item.update(original_equations=proposed['equation'],
                    original_full3_merit=merit(proposed),
                    actual_original_unit_constraint_error=proposed_error,
                    scaled_constraint_merit=trial_merit)
                consider(proposed,trial_w,item['original_full3_merit'],'evaluated-normal-trial',inner,backtrack)
                if trial_merit.is_finite() and trial_merit<=bound:
                    current,w=proposed,trial_w
                    item['accepted']=row['accepted']=True
                    item['reason']='normal target merit Armijo accepted; not an outer parameter acceptance'
                else:
                    item['reason']='normal target merit Armijo rejected'
            except NumericalFailure as failure:
                item.update(reason='original domain or evaluation failure during normal correction',
                            exception=repr(failure))
            if row['accepted']:
                break
        if not row['accepted']:
            record['stop_reason']='all normal backtracks rejected; preserve last finite candidate'
            break
        if current['parameters']==previous:
            record['stop_reason']='the actual normal update left finite Decimal parameter values unchanged'
            break
    else:
        record['stop_reason']='explicit normal-correction iteration budget completed'

    def diagnostics(candidate,coords):
        displacement=sub(candidate['parameters'],p)
        correction=sub(candidate['parameters'],seed)
        error=sub(candidate['equation'][1:],target)
        return dict(returned_parameters=list(candidate['parameters']),
            returned_original_equations=list(candidate['equation']),
            returned_original_full3_merit=merit(candidate),returned_constraint_error=error,
            returned_normal_coordinates=list(coords),actual_decimal_displacement=displacement,
            actual_decimal_normal_correction=correction,
            actual_relative_parameter_step_L2=norm([x/s for x,s in zip(displacement,frame['scales'])]),
            actual_tangent_gauge_leak=mv(transpose(frame['tangent']),
                                         [x/s for x,s in zip(correction,frame['scales'])]),
            requested_constraint_error_tolerance_met=maxabs(error)<=TOL,
            unresolved_normal_target_does_not_exclude_original_full3_Armijo_trial=True)
    record.update(diagnostics(current,w))
    working=dict(stop_reason=record['stop_reason'],**copy.deepcopy(diagnostics(current,w)))
    record['original_working_trajectory_return']=working
    working_sample=consider(current,w,working['returned_original_full3_merit'],'original-working-return')
    best=shadow['best']
    changed=best is not None and (not working['returned_original_full3_merit'].is_finite()
                                  or best['merit']<working['returned_original_full3_merit'])
    record['same_trace_full3_selection']=dict(
        schema='decimal50-completed-normal-trace-unweighted-full3-minimum-v1',
        complete_original_working_call_returned=True,
        actual_working_stop_reason=record['stop_reason'],
        original_working_return_sample=working_sample,
        selected_sample=best['index'] if changed else working_sample,
        selected_is_original_working_return=not changed,
        sample_count=len(samples),finite_sample_count=sum(bool(x[7]) for x in samples),
        original_working_merit=working['returned_original_full3_merit'],
        selected_saved_merit=best['merit'] if changed else working['returned_original_full3_merit'],
        tie_policy='prefer original working return; otherwise first strict finite shadow minimum',
        original_working_trace_not_changed_by_selector=True,
        incomplete_call_not_rescued=True,added_evaluation_or_response_calls=0,
        original_full3_outer_Armijo_not_bypassed=True,inner_target_not_a_gate=True)
    if changed:
        current,w=best['state'],best['coordinates']
        record.update(diagnostics(current,w))
    return current


def search(model,state,J,radius,status,checkpoint,event_sink):
    """One original8-direction child; every return keeps the actual owner state."""
    p=list(state['parameters']);accepted_points=0
    status['searches']=[]
    status['phase']='decimal50-complete-three-curved-search'
    def save_owner():
        status.update(current_persistent_parameters=list(p),
            current_relative_trust_radius=radius,
            current_complete_equations=list(state['equation']),
            current_full112_right=list(state['full_right']),
            current_original_three_equation_merit=merit(state),
            original_Armijo_accepted_point_count=accepted_points,
            owner_parameter_encoding='finite-decimal-strings',
            owner_is_actual_accepted_state_or_fresh_initial_guess=True)
    save_owner()
    checkpoint()
    for iteration in range(8):
        residual=state['equation']
        if maxabs(residual)<=TOL:
            status['search_stop_reason']='all original unit equations meet their original stopping tolerance'
            break
        before=merit(state)
        if not before.is_finite():
            raise NumericalFailure('The original unweighted complete-three merit is nonfinite')
        row=dict(iteration=iteration,parameters=list(p),residual=list(residual),
            derivative=J,merit_before=before,relative_radius=radius,trials=[],accepted=False,
            accepted_point_count_before=accepted_points)
        status['searches'].append(row)
        checkpoint()
        try:
            row['direction_model']={}
            direction,action=complete_direction(model,p,residual,J,radius,row['direction_model'])
            frame,row['curve_frame']=curve_frame(p,residual,J,direction,action)
        except (NumericalFailure,DecimalException) as error:
            row['direction_model_error']=repr(error)
            status['search_stop_reason']='the complete-three predictor or complete normal frame failed'
            break
        slope=dot(residual,action);row['true_model_merit_slope']=slope
        if not slope.is_finite() or slope>=0:
            row['reason']='No finite strict descent of the actual complete three-equation merit'
            status['search_stop_reason']=row['reason'];break
        for trial in range(20):
            alpha=ONE/(TWO**trial);bound=before+ARM*alpha*slope
            item=dict(trial=trial,alpha=alpha,seed_parameters=add(p,scale(direction,alpha)),
                original_Armijo_bound=bound,accepted=False,normal_correction={})
            row['trials'].append(item)
            try:
                candidate=curved_candidate(model,p,state,direction,action,frame,alpha,
                    item['normal_correction'],'outer-'+str(iteration)+'/trial-'+str(trial))
                actual=merit(candidate)
                item.update(actual_merit=actual,actual_parameters=candidate['parameters'],
                    actual_unit_equations=candidate['equation'],
                    actual_full112_right=candidate['full_right'],
                    actual_decimal_parameter_displacement=sub(candidate['parameters'],p))
                if actual.is_finite() and actual<=bound:
                    predicted=before-dot(add(residual,scale(action,alpha)),
                                         add(residual,scale(action,alpha)))/TWO
                    radius,row['radius_update']=next_radius(radius,alpha,
                        row['direction_model']['scaled_direction_L2'],before-actual,predicted)
                    p,state=list(candidate['parameters']),candidate
                    accepted_points+=1
                    item['accepted']=row['accepted']=True
                    item['reason']='actual curved candidate passes original unweighted complete-three Armijo'
                else:
                    item['reason']='actual curved candidate fails original unweighted complete-three Armijo'
            except (NumericalFailure,DecimalException) as error:
                item.update(reason='curved-candidate evaluation failed; candidate not adopted',exception=repr(error))
            save_owner()
            checkpoint()
            event_sink(dict(event='decimal50-original-outer-trial',iteration=iteration,
                trial=trial,alpha=alpha,accepted=item['accepted'],actual_merit=item.get('actual_merit'),
                original_Armijo_bound=bound,actual_parameters=item.get('actual_parameters'),
                actual_unit_equations=item.get('actual_unit_equations'),
                normal_stop_reason=item['normal_correction'].get('stop_reason'),
                normal_target_tolerance_met=item['normal_correction'].get('requested_constraint_error_tolerance_met'),
                reason=item['reason']))
            if row['accepted']:
                break
        if not row['accepted']:
            previous=radius;radius=radius/4
            row.update(reason='all original full3 curved-candidate backtracks rejected; no point adopted',
                radius_update=dict(previous_radius=previous,next_radius=radius,multiplier=dec(0.25),
                    update_rule='quarter radius after complete rejection',
                    current_parameters_state_and_J_unchanged=True,parameter_point_accepted=False))
            save_owner()
            checkpoint()
            continue
        if iteration+1<8:
            with model.context('accepted-point/fresh-all-nine-forward'):
                J,jr,js=model.response(p,label='fresh-current-all-nine-axis')
            row['next_fresh_response_readback']=jr
    else:
        status['search_stop_reason']='explicit total direction budget completed, counting accepted and rejected directions'
    save_owner()
    status.update(last_accepted_parameters=list(p),final_relative_trust_radius=radius,
        total_direction_attempts=len(status['searches']),
        original_Armijo_accepted_point_count=accepted_points,
        rejected_direction_count=sum(not r['accepted'] for r in status['searches']),
        final_original_three_equation_merit=merit(state))
    checkpoint()
    return state,radius
