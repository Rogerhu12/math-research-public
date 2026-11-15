#!/usr/bin/env python3
"""Request157: all-three residual quadratic square in all nine coordinates.

The finite polynomial optimizer is proposal work only. It preserves every
evaluated model candidate and uses no new physical RHS/J/Hessian calls.
Its selected displacement is tested on the original straight physical path
with the original full-three forward slope, domain and Armijo rule.
The separately labelled frozen149 normal fallback is unchanged.
"""
from __future__ import annotations
import hashlib
from decimal import DecimalException
import geometry_20261115_nine_control_decimal_ambient_trust as ambient
from geometry_20261115_nine_control_decimal_literal_model import (
    ZERO,ONE,TWO,ARM,TOL,NumericalFailure,dec,dot,norm,maxabs,sub,add,scale,
    transpose,mv,mm,eye,merit,encoded)

legacy=ambient.legacy
MODEL_POLICY=dict(
    complete_relative_dimension=9,complete_residual_dimension=3,
    maximum_model_updates=32,model_backtracks_per_candidate=20,
    candidate_slots_per_update=21,complete_residual_QR_solves_per_update=1,
    shift_bracket_trials=32,
    shift_bisections=32,Jacobi_sweeps=ambient.JACOBI_SWEEPS,
    finite_search_not_global_polynomial_optimum=True,
    no_new_original_primal_calls_inside_polynomial_optimizer=True,
    all_model_candidates_and_unvisited_indices_retained=True,
    original_physical_acceptance_unchanged=True)
MODEL_UPDATES=32
MODEL_BACKTRACKS=20
SHIFT_BRACKET=32
SHIFT_BISECTIONS=32
CANDIDATE_SLOTS=21
MODEL_TRIAL_COLUMNS=(
    'trial','beta','actual_relative_point','full_three_model_residual',
    'full_three_model_merit','model_Armijo_bound','formed_relative_point_L2',
    'within_formed_global_ball','formed_original_point_slope',
    'eligible_for_final_model_selection','global_candidate_index',
    'accepted_for_inner_model_update','exception')


def finite(v):
    return all(x.is_finite() for x in v)


def polynomial_residual(F,A,H,y):
    """Each of the original three residuals, not a quadratic merit surrogate."""
    return [F[i]+dot(A[i],y)+dot(y,mv(H[i],y))/TWO for i in range(3)]


def polynomial_state(F,A,H,y):
    q=polynomial_residual(F,A,H,y)
    K=[add(A[i],mv(H[i],y)) for i in range(3)]
    gradient=mv(transpose(K),q)
    gn=mm(transpose(K),K)
    B=[[ZERO]*9 for unused in range(9)]
    for i in range(9):
        for j in range(i,9):
            v=gn[i][j]+sum((q[k]*H[k][i][j] for k in range(3)),ZERO)
            B[i][j]=B[j][i]=v
    if (not finite(q) or not finite(gradient) or not all(finite(r) for r in K)
        or not all(finite(r) for r in B)):
        raise NumericalFailure('Nonfinite complete residual quadratic model')
    return q,dot(q,q)/TWO,K,gradient,B


def matrix_identity(value):
    raw=encoded(value)
    return dict(shape=[len(value),len(value[0]) if value else 0],
                canonical_Decimal_JSON_bytes=len(raw),
                canonical_Decimal_JSON_sha256=hashlib.sha256(raw).hexdigest(),
                full_words_not_retained_in_this_compact_shift_record=True)


def compact_shift_record(item):
    # The complete current Hessian and actual shift are already in the parent
    # record. Keep every solve/pivot and all nine residual words. Factor cells
    # are explicitly hash-only, not silently advertised as an array audit.
    for key in ('formed_matrix','complete_factor','factor_product_minus_formed_matrix'):
        if key in item:
            value=item.pop(key)
            item[key+'_identity']=matrix_identity(value)
    item['full_formed_linear_residual_retained']='formed_linear_residual' in item
    item['not_an_interval_factor_or_solve_error_bound']=True


def shift_proposal(B,gradient,local_radius,eigen,record):
    trials=[]
    record['shift_trials']=trials
    record['shift_budget']=dict(bracket=SHIFT_BRACKET,refinement=SHIFT_BISECTIONS)
    margin=ambient.SHIFT_RELATIVE_MARGIN*max(ONE,norm([v for row in B for v in row]))
    lower=max(ZERO,-min(eigen));upper=lower+margin;chosen=None
    bracket_used=refinement_used=0

    def solve(mu,label,index):
        item=dict(sequence=len(trials),stage=label,stage_index=index,complete=False)
        trials.append(item)
        try:
            z=ambient.shifted_cholesky(B,gradient,mu,item)
            item['within_formed_local_step_radius']=norm(z)<=local_radius
            return z
        except (NumericalFailure,DecimalException) as error:
            item['exception']=repr(error)
            return None
        finally:
            compact_shift_record(item)
            item['complete']=bool(item.get('returned') or 'exception' in item)

    try:
        for j in range(SHIFT_BRACKET):
            bracket_used=j+1
            z=solve(upper,'bracket',j)
            if z is not None and norm(z)<=local_radius:
                chosen=z
                break
            lower=upper
            upper=max(TWO*upper,upper+max(ONE,margin))
            if not upper.is_finite():
                break
        if chosen is not None:
            for j in range(SHIFT_BISECTIONS):
                mid=(lower+upper)/TWO
                if not lower<mid<upper:
                    break
                refinement_used=j+1
                z=solve(mid,'refinement',j)
                if z is not None and norm(z)<=local_radius:
                    upper,chosen=mid,z
                else:
                    lower=mid
                if norm(chosen)>=ambient.RELATIVE_BOUNDARY_TARGET*local_radius:
                    break
        return chosen
    finally:
        record.update(formed_shift_margin=margin,final_shift_lower=lower,
            final_shift_upper=upper,shifted_solution_returned=chosen is not None,
            unvisited_shift_bracket_indices=list(range(bracket_used,SHIFT_BRACKET)),
            unvisited_shift_refinement_indices=list(range(refinement_used,SHIFT_BISECTIONS)),
            finite_Jacobi_lower_bound_is_only_guidance=True,
            finite_positive_pivots_not_an_SPD_certificate=True)


def full_residual_GN_proposal(K,q,gradient,local_radius,record):
    """One complete12x9 QR preconditioner for the current polynomial residual."""
    gnorm=norm(gradient)
    record.update(complete=False,normal_matrix_used_for_solve=False,
                  original_three_residual_rows_not_reweighted=True)
    if gnorm==0:
        record.update(complete=True,reason='formed model gradient is exactly zero')
        return None
    ridge=gnorm/local_radius
    mu=ridge.sqrt()
    augmented=[list(row) for row in K]
    augmented += [[mu if i==j else ZERO for j in range(9)] for i in range(9)]
    rhs=[-x for x in q]+[ZERO]*9
    record.update(ridge=ridge,square_root_ridge=mu,
        ridge_formula='||complete model gradient|| / local step radius',
        augmented_shape=[12,9],complete_augmented_rhs=rhs)
    try:
        z,qr=legacy.qr_solve(augmented,rhs)
        record.update(complete_solution=z,formed_relative_L2=norm(z),
            complete_Q_identity=matrix_identity(qr.pop('complete_Q')),
            complete_R_identity=matrix_identity(qr.pop('complete_R')),
            complete_augmented_matrix_identity=matrix_identity(augmented),
            original_QR_readback=qr,
            complete_stationarity_residual=add(
                mv(transpose(K),add(mv(K,z),q)),scale(z,ridge)),
            exact_real_norm_and_descent_identity_not_a_floating_certificate=True)
        record['complete']=True
        return z
    except (NumericalFailure,DecimalException) as error:
        record.update(complete=True,exception=repr(error))
        return None


def project_endpoint(y,step,radius):
    endpoint=add(y,step)
    size=norm(endpoint)
    factor=radius/size if size>radius else ONE
    projected=scale(endpoint,factor) if factor!=ONE else endpoint
    return projected,dict(unprojected_relative_point=endpoint,
        formed_unprojected_L2=size,radial_projection_factor=factor,
        actual_projected_relative_point=projected,
        formed_projected_L2=norm(projected),
        formed_global_ball_test_is_repeated_for_each_model_trial=True,
        no_exact_floating_ball_membership_claimed=True)


def residual_model_direction(model,p,state,pilot,radius,record,checkpoint,event_sink):
    if radius<=0 or not radius.is_finite():
        raise NumericalFailure('A positive finite explicit polynomial exploration radius is required')
    with model.context('outer/full-nine-residual-second-forward'):
        J,H,second,second_state=model.curvature(p)
    F=list(state['equation']);scales=[max(ONE,abs(x)) for x in p]
    A=[[J[i][j]*scales[j] for j in range(9)] for i in range(3)]
    scaled_H=[[[ZERO]*9 for unused in range(9)] for row in range(3)]
    for k in range(3):
        for i in range(9):
            for j in range(i,9):
                value=H[k][i][j]*scales[i]*scales[j]
                scaled_H[k][i][j]=scaled_H[k][j][i]=value
    origin_gradient=mv(transpose(A),F)
    origin_merit=dot(F,F)/TWO
    record.update(path='residual-quadratic-square-straight-line',
        physical_path='p(alpha)=p+alpha*D*y_selected',
        complete_second_forward=second,complete_three_by_nine_J=J,
        complete_three_by_nine_by_nine_H=H,
        second_primal_equations=second_state['equation'],
        second_primal_words_equal_current=second_state['equation']==F,
        original_first_forward_axis_J=pilot,
        second_J_minus_original_axis_J=[[x-y for x,y in zip(a,b)] for a,b in zip(J,pilot)],
        original_current_equations=F,relative_parameter_scales=scales,
        complete_scaled_J=A,complete_scaled_residual_Hessians=scaled_H,
        scaled_Hessian_formation='upper pair H[k][i][j]*D[i]*D[j] mirrored exactly; original unscaled arrays retained',
        original_formed_relative_gradient=origin_gradient,origin_merit=origin_merit,
        original_relative_radius=radius,model_solver_policy=MODEL_POLICY,
        formula='Q_i(y)=F_i+A_i*y+0.5*y^T*H_i_scaled*y; Phi=0.5*sum_i Q_i^2',
        all_three_residuals_and_all_nine_coordinates_retained=True,
        no_linearized_normal_targets_in_primary=True,
        no_original_domain_or_RHS_calls_inside_polynomial_search=True,
        finite_model_points_not_accepted_physical_points=True,
        model_updates=[],global_model_candidate_count=0,
        model_trial_columns=list(MODEL_TRIAL_COLUMNS),
        model_optimizer_completed=False,
        normal_path_not_the_polynomial_path=True)
    if not finite(F) or not finite(origin_gradient):
        raise NumericalFailure('Nonfinite original data for the complete polynomial model')
    y=[ZERO]*9;local_radius=radius
    global_candidates=[];global_evaluated=0
    stop='internal polynomial optimizer did not complete'
    try:
        for iteration in range(MODEL_UPDATES):
            update=dict(index=iteration,current_relative_point=list(y),
                local_step_radius=local_radius,complete=False,
                candidate_pool=[],selected_candidate=None,
                unvisited_candidate_indices=list(range(CANDIDATE_SLOTS)))
            record['model_updates'].append(update)
            q,before,K,gradient,B=polynomial_state(F,A,scaled_H,y)
            update.update(full_three_model_residual=q,full_three_model_merit=before,
                complete_three_by_nine_model_J=K,complete_nine_model_gradient=gradient,
                complete_nine_by_nine_model_Hessian=B,
                model_Hessian_formula='K^T K + sum_i Q_i H_i_scaled',
                full_model_gradient_norm=norm(gradient))
            eigen,columns,spectral=ambient.jacobi_full(B)
            update['complete_spectral_guidance']=spectral
            shifted=shift_proposal(B,gradient,local_radius,eigen,update)
            update['complete_residual_GN_preconditioner']={}
            gn_step=full_residual_GN_proposal(K,q,gradient,local_radius,update['complete_residual_GN_preconditioner'])
            proposals=[('full-nine-complete-model-residual-GN',gn_step,{})]
            proposals.append(('full-nine-shifted-model-Newton',shifted,dict(
                selected_shift=update['final_shift_upper'])))
            gnorm=norm(gradient)
            cauchy=None
            if gnorm!=0:
                t=local_radius/gnorm
                gBg=dot(gradient,mv(B,gradient))
                if gBg>0:
                    t=min(t,gnorm*gnorm/gBg)
                cauchy=scale(gradient,-t)
            proposals.append(('full-nine-model-Cauchy',cauchy,dict(
                formed_gradient_exactly_zero=gnorm==0)))
            for j in range(9):
                v=[columns[i][j] for i in range(9)]
                vn=norm(v);curvature=dot(v,mv(B,v))
                for sign,label in ((ONE,'plus'),(-ONE,'minus')):
                    z=scale(v,sign*local_radius/vn) if vn!=0 and curvature<0 else None
                    proposals.append(('model-negative-curvature-column-'+str(j)+'-'+label,z,
                        dict(column=j,sign=sign,complete_column=v,formed_curvature=curvature,
                             nonnegative_or_zero_column_not_used_as_negative_curvature=z is None)))
            if len(proposals)!=CANDIDATE_SLOTS:
                raise RuntimeError('The complete predefined proposal pool changed')
            accepted_rays=[]
            for index,(label,raw_step,extra) in enumerate(proposals):
                candidate=dict(index=index,label=label,complete=False,extra=extra,
                    trials=[],original_model_trial_budget=MODEL_BACKTRACKS,
                    unvisited_model_trial_indices=list(range(MODEL_BACKTRACKS)),
                    raw_model_step=raw_step,eligible_direction=False)
                update['candidate_pool'].append(candidate)
                update['unvisited_candidate_indices']=list(range(index+1,CANDIDATE_SLOTS))
                if raw_step is None or not finite(raw_step) or norm(raw_step)==0:
                    candidate.update(reason='no nonzero finite proposed step',complete=True)
                    continue
                endpoint,projection=project_endpoint(y,raw_step,radius)
                step=sub(endpoint,y);step_size=norm(step)
                slope=dot(gradient,step);curvature=dot(step,mv(B,step))
                candidate.update(projection=projection,actual_relative_model_chord=step,
                    formed_chord_L2=step_size,formed_model_slope=slope,
                    formed_model_directional_curvature=curvature)
                # A zero-slope negative-curvature model escape is allowed here,
                # but never replaces the original strict physical slope test.
                if (step_size==0 or not finite(step) or not slope.is_finite()
                    or not curvature.is_finite() or slope>0
                    or (slope==0 and curvature>=0)):
                    candidate.update(reason='no bounded nonascending or negative-curvature model chord',
                                     complete=True)
                    continue
                candidate['eligible_direction']=True
                for trial in range(MODEL_BACKTRACKS):
                    beta=ONE/(TWO**trial)
                    bound=before+ARM*beta*slope
                    point=add(y,scale(step,beta))
                    values=[trial,beta,point,None,None,bound,None,False,None,False,None,False,None]
                    candidate['trials'].append(values)
                    try:
                        trial_q=polynomial_residual(F,A,scaled_H,point)
                        phi=dot(trial_q,trial_q)/TWO
                        point_size=norm(point);origin_slope=dot(origin_gradient,point)
                        complete_finite=(finite(point) and finite(trial_q) and phi.is_finite()
                            and point_size.is_finite() and origin_slope.is_finite())
                        within=complete_finite and point_size<=radius
                        eligible=within and origin_slope<0 and phi<origin_merit
                        values[3]=trial_q;values[4]=phi;values[5]=bound
                        values[6]=point_size;values[7]=within;values[8]=origin_slope
                        values[9]=eligible;values[10]=None
                        if complete_finite:
                            global_evaluated+=1
                        if eligible:
                            number=len(global_candidates)
                            values[10]=number
                            global_candidates.append((phi,number,list(point),
                                dict(update=iteration,candidate=index,trial=trial)))
                        inner_accept=within and phi<before and phi<=bound
                        values[11]=inner_accept
                        if inner_accept:
                            accepted_rays.append((phi,index,list(point),trial,beta))
                            candidate.update(accepted_model_trial=trial,
                                reason='complete polynomial squared residual passes its stated internal decrease rule')
                            break
                    except (NumericalFailure,DecimalException) as error:
                        values[12]=repr(error)
                    finally:
                        candidate['unvisited_model_trial_indices']=list(range(len(candidate['trials']),MODEL_BACKTRACKS))
                        record['global_model_candidate_count']=len(global_candidates)
                        record['complete_finite_model_points_evaluated']=global_evaluated
                if not accepted_rays or accepted_rays[-1][1]!=index:
                    candidate['reason']='all bounded model trials invalid or fail internal decrease'
                candidate['complete']=True
            if accepted_rays:
                phi,index,chosen,trial,beta=min(accepted_rays,key=lambda value:(value[0],value[1]))
                realized=sub(chosen,y);actual_step_size=norm(realized)
                local_prediction=-dot(gradient,realized)-dot(realized,mv(B,realized))/TWO
                revised,controller=legacy.next_radius(local_radius,ONE,actual_step_size,before-phi,local_prediction)
                local_radius=min(radius,revised)
                controller.update(next_radius_before_global_cap=revised,next_radius=local_radius,
                    global_radius_cap=radius,actual_selected_ray_beta=beta,
                    uses_realized_chord_with_controller_alpha_one=True,
                    no_automatic_halving_solely_for_model_ray_backtracking=True,
                    controller_does_not_accept_a_physical_point=True)
                update.update(selected_candidate=index,selected_model_trial=trial,
                    selected_relative_point=chosen,selected_model_merit=phi,
                    inner_radius_update=controller)
                y=chosen
            else:
                previous=local_radius;local_radius=local_radius/4
                update.update(reason='no complete internal ray decrease; model point unchanged',
                    inner_radius_update=dict(previous_radius=previous,next_radius=local_radius,
                        update_rule='quarter after the complete bounded model proposal pool rejects'),
                    selected_relative_point=list(y))
            update['complete']=True
            record.update(last_internal_relative_point=list(y),last_internal_step_radius=local_radius,
                unvisited_model_update_indices=list(range(iteration+1,MODEL_UPDATES)))
            checkpoint()
            event_sink(dict(event='decimal50-complete-residual-polynomial-model-update',
                index=iteration,complete=True,selected_candidate=update['selected_candidate'],
                selected_model_merit=update.get('selected_model_merit'),
                model_local_radius=local_radius,finite_original_slope_model_candidates=len(global_candidates)))
            if local_radius==0:
                stop='finite internal step radius became exactly zero; no optimum claimed'
                break
        else:
            stop='explicit complete polynomial update budget'
        record['model_optimizer_completed']=True
    finally:
        record.update(model_stop_reason=stop,
            unvisited_model_update_indices=list(range(len(record['model_updates']),MODEL_UPDATES)),
            complete_finite_model_points_evaluated=global_evaluated,
            global_model_candidate_count=len(global_candidates),
            finite_model_minimization_not_a_global_optimality_certificate=True)
    if not global_candidates:
        raise NumericalFailure('No completely evaluated model point supplies negative original formed slope and model decrease')
    phi,index,z,reference=min(global_candidates,key=lambda item:(item[0],item[1]))
    direction=[v*s for v,s in zip(z,scales)]
    with model.context('outer/chosen-residual-model-displacement-original-forward'):
        response,rr,rs=model.response(p,[[x] for x in direction],label='actual-residual-model-straight-direction')
    action=[row[0] for row in response];actual_slope=dot(F,action)
    record.update(selected_global_candidate=index,selected_model_reference=reference,
        selected_full_three_model_residual=polynomial_residual(F,A,scaled_H,z),
        selected_model_merit=phi,selected_model_predicted_reduction=origin_merit-phi,
        actual_relative_direction=z,actual_nine_parameter_direction=direction,
        scaled_direction_L2=norm(z),actual_direction_forward=rr,
        actual_direction_primal_equations=rs['equation'],
        actual_direct_full3_action=action,formed_axis_action=mv(J,direction),
        direct_minus_formed_axis_action=sub(action,mv(J,direction)),
        actual_full3_slope=actual_slope,
        selected_model_point_not_an_accepted_physical_point=True,
        full_curved_normal_target_not_used_to_form_primary=True,
        rounded_Decimal50_not_an_interval_or_global_error_certificate=True)
    if not actual_slope.is_finite() or actual_slope>=0:
        raise NumericalFailure('Model winner does not supply the original actual finite strict forward descent slope')
    return direction,action


def primary_prediction(record,alpha):
    F=record['original_current_equations'];A=record['complete_scaled_J']
    H=record['complete_scaled_residual_Hessians'];z=record['actual_relative_direction']
    point=scale(z,alpha)
    q=polynomial_residual(F,A,H,point)
    phi=dot(q,q)/TWO
    a=mv(A,z);b=[dot(z,mv(h,z)) for h in H]
    return record['origin_merit']-phi,dict(
        full_three_residual_quadratic_prediction=q,residual_quadratic_square_merit=phi,
        relative_point=point,complete_ray_linear_response=a,
        complete_ray_residual_second_response=b,
        formed_original_linear_term=alpha*dot(F,a),
        formed_ambient_quadratic_term=alpha*alpha*(dot(a,a)+dot(F,b))/TWO,
        formed_cubic_cross_term=alpha**3*dot(a,b)/TWO,
        formed_nonnegative_quartic_term=alpha**4*dot(b,b)/dec(8),
        formula_terms_not_a_rounded_word_identity_claim=True,
        prediction_uses_complete_quadratic_residual_not_quadratic_merit=True,
        actual_original_forward_slope_is_separately_used_for_Armijo=True)


def search(model,state,J,radius,status,checkpoint,event_sink):
    """Eight actual directions; finite polynomial work precedes unchanged real trials."""
    p=list(state['parameters']);accepted_points=0
    status['searches']=[];status['phase']='decimal50-complete-residual-quadratic-square-search'
    def save_owner():
        status.update(current_persistent_parameters=list(p),current_relative_trust_radius=radius,
            current_complete_equations=list(state['equation']),current_full112_right=list(state['full_right']),
            current_original_three_equation_merit=merit(state),
            original_Armijo_accepted_point_count=accepted_points,
            owner_parameter_encoding='finite-decimal-strings',
            owner_is_actual_accepted_state_or_fresh_initial_guess=True)
    save_owner();checkpoint()
    for iteration in range(8):
        residual=state['equation']
        if maxabs(residual)<=TOL:
            status['search_stop_reason']='all original unit equations meet their original stopping tolerance';break
        before=merit(state)
        if not before.is_finite():
            raise NumericalFailure('The original unweighted complete-three merit is nonfinite')
        row=dict(iteration=iteration,parameters=list(p),residual=list(residual),derivative=J,
            merit_before=before,relative_radius=radius,trials=[],accepted=False,
            accepted_point_count_before=accepted_points,direction_model={},
            path_status=dict(residual_quadratic_straight=dict(started=False,trial_budget=20),
                             original149_normal_fallback=dict(started=False,trial_budget=20,
                                 normal_iterations=12,normal_backtracks=20)))
        status['searches'].append(row);checkpoint()
        for path in ('residual_quadratic_straight','original149_normal_fallback'):
            path_record=row['path_status'][path]
            path_record['started']=True
            try:
                if path=='residual_quadratic_straight':
                    direction,action=residual_model_direction(model,p,state,J,radius,row['direction_model'],checkpoint,event_sink)
                    size=row['direction_model']['scaled_direction_L2']
                else:
                    row['fallback_direction_model']={}
                    direction,action=legacy.complete_direction(model,p,residual,J,radius,row['fallback_direction_model'])
                    frame,row['fallback_curve_frame']=legacy.curve_frame(p,residual,J,direction,action)
                    size=row['fallback_direction_model']['scaled_direction_L2']
                slope=dot(residual,action)
                path_record.update(actual_full3_slope=slope,actual_direction=direction,
                                   actual_direct_response=action)
                if not slope.is_finite() or slope>=0:
                    raise NumericalFailure('No actual finite strict descent for this separately labelled path')
            except (NumericalFailure,DecimalException) as error:
                path_record.update(direction_model_error=repr(error),trial_count=0,
                    unvisited_trial_indices=list(range(20)),
                    stop_reason='direction formation did not supply the original strict descent requirement')
                checkpoint();continue
            for trial in range(20):
                alpha=ONE/(TWO**trial);bound=before+ARM*alpha*slope
                item=dict(trial_index=len(row['trials']),trial=trial,path=path,alpha=alpha,
                    seed_parameters=add(p,scale(direction,alpha)),original_Armijo_bound=bound,
                    accepted=False,normal_correction={})
                row['trials'].append(item)
                try:
                    if path=='residual_quadratic_straight':
                        predicted,prediction=primary_prediction(row['direction_model'],alpha)
                        item['full_three_residual_quadratic_model']=prediction
                        with model.context('outer-'+str(iteration)+'/residual-model-straight-'+str(trial)):
                            candidate=model.evaluate(item['seed_parameters'])
                        item['normal_correction']=dict(called=False,
                            reason='primary is the actual straight physical path, not a normal curve')
                        prediction_label='full three residual quadratic square on p+alpha*d'
                    else:
                        candidate=legacy.curved_candidate(model,p,state,direction,action,frame,alpha,
                            item['normal_correction'],'outer-'+str(iteration)+'/legacy-fallback-'+str(trial))
                        predicted=before-dot(add(residual,scale(action,alpha)),add(residual,scale(action,alpha)))/TWO
                        prediction_label='unchanged149 linear residual model; not the primary residual polynomial'
                    actual=merit(candidate)
                    item.update(actual_merit=actual,actual_parameters=candidate['parameters'],
                        actual_unit_equations=candidate['equation'],actual_full112_right=candidate['full_right'],
                        actual_decimal_parameter_displacement=sub(candidate['parameters'],p),
                        actual_path_model_predicted_reduction=predicted,prediction_scope=prediction_label)
                    if path=='residual_quadratic_straight':
                        item['actual_minus_model_three_residuals']=sub(candidate['equation'],prediction['full_three_residual_quadratic_prediction'])
                        item['actual_merit_minus_complete_model_merit']=actual-prediction['residual_quadratic_square_merit']
                    if actual.is_finite() and actual<=bound:
                        radius,row['radius_update']=legacy.next_radius(radius,alpha,size,before-actual,predicted)
                        row['radius_update']['prediction_scope']=prediction_label
                        p,state=list(candidate['parameters']),candidate;accepted_points+=1
                        item['accepted']=row['accepted']=True;row['accepted_path']=path
                        item['reason']='actual candidate passes unchanged complete-three .2 Armijo'
                    else:
                        item['reason']='actual candidate fails unchanged complete-three .2 Armijo'
                except (NumericalFailure,DecimalException) as error:
                    item.update(reason='actual path domain or evaluation failure; no point adopted',exception=repr(error))
                save_owner();checkpoint()
                event_sink(dict(event='decimal50-residual-model-actual-outer-trial',iteration=iteration,
                    trial=trial,path=path,alpha=alpha,accepted=item['accepted'],
                    actual_merit=item.get('actual_merit'),original_Armijo_bound=bound,
                    actual_parameters=item.get('actual_parameters'),actual_unit_equations=item.get('actual_unit_equations'),
                    reason=item['reason']))
                if row['accepted']:
                    break
            count=sum(t['path']==path for t in row['trials'])
            path_record.update(trial_count=count,unvisited_trial_indices=list(range(count,20)),
                stop_reason='actual original merit acceptance' if row['accepted'] else 'all20 actual trials rejected')
            if row['accepted']:
                if path=='residual_quadratic_straight':
                    row['path_status']['original149_normal_fallback'].update(
                        reason='not reached because a straight candidate passed original merit',
                        unvisited_trial_indices=list(range(20)))
                break
        if not row['accepted']:
            previous=radius;radius=radius/4
            row.update(reason='both bounded proposal paths failed or rejected; current point unchanged',
                radius_update=dict(previous_radius=previous,next_radius=radius,multiplier=dec(0.25),
                    update_rule='quarter after complete direction rejection',
                    current_parameters_state_and_J_unchanged=True,parameter_point_accepted=False))
            save_owner();checkpoint();continue
        if iteration+1<8:
            with model.context('accepted-point/fresh-original-nine-forward'):
                J,jr,js=model.response(p,label='fresh-current-all-nine-axis')
            row['next_fresh_response_readback']=jr
    else:
        status['search_stop_reason']='explicit total direction budget completed, counting accepted and rejected directions'
    save_owner()
    status.update(last_accepted_parameters=list(p),final_relative_trust_radius=radius,
        total_direction_attempts=len(status['searches']),original_Armijo_accepted_point_count=accepted_points,
        rejected_direction_count=sum(not row['accepted'] for row in status['searches']),
        final_original_three_equation_merit=merit(state))
    checkpoint();return state,radius
