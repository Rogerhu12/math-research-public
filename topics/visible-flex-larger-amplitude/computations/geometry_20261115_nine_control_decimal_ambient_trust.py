#!/usr/bin/env python3
"""Request154: complete ambient full3 curvature and real straight-path trials.

The primary Hessian models q=p+alpha*d only. It is never called the Hessian
of a normal-corrected path. If all20 straight trials reject, or forming its
descent proposal fails, the separately labelled original149 GN/normal path
may use its original20 outer/12x20 inner budgets. Every adoption still uses
the same original unweighted three equations, actual negative slope and .2
Armijo; there is no inner-target, eigenvalue, FD, or accuracy acceptance gate.
"""
from __future__ import annotations
from decimal import DecimalException
import geometry_20261115_nine_control_decimal_curved_search as legacy
from geometry_20261115_nine_control_decimal_literal_model import (
    ZERO,ONE,TWO,ARM,TOL,NumericalFailure,dec,dot,norm,maxabs,sub,add,scale,
    transpose,mv,mm,eye,merit)

JACOBI_SWEEPS=64
SHIFT_BRACKET=64
SHIFT_BISECTIONS=64
JACOBI_RELATIVE_STOP=dec('1e-40')
SHIFT_RELATIVE_MARGIN=dec('1e-35')
RELATIVE_BOUNDARY_TARGET=dec('0.999')


def finite(v):
    return all(x.is_finite() for x in v)


def jacobi_full(matrix):
    """All9 symmetric columns; finite spectral guidance, not an enclosure."""
    n=9
    if len(matrix)!=n or any(len(r)!=n for r in matrix) or not all(finite(r) for r in matrix):
        raise NumericalFailure('The complete nine-by-nine curvature matrix is malformed')
    a=[list(r) for r in matrix];q=eye(n);trace=[];rotations=0
    for sweep in range(JACOBI_SWEEPS):
        off=max(abs(a[i][j]) for i in range(n) for j in range(i+1,n))
        bound=JACOBI_RELATIVE_STOP*max(ONE,max(abs(a[i][i]) for i in range(n)))
        row=dict(sweep=sweep,maximum_offdiagonal=off,formed_relative_stop_bound=bound,
                 complete_rotations_before=rotations)
        trace.append(row)
        if off<=bound:
            row['stop']='finite offdiagonal iteration criterion';break
        for i in range(n):
            for j in range(i+1,n):
                b=a[i][j]
                if b==0:
                    continue
                tau=(a[j][j]-a[i][i])/(TWO*b)
                sign=ONE if tau>=0 else -ONE
                t=sign/(abs(tau)+(ONE+tau*tau).sqrt())
                c=ONE/(ONE+t*t).sqrt();s=t*c
                oldi,oldj=a[i][i],a[j][j]
                for k in range(n):
                    if k in (i,j):
                        continue
                    ki,kj=a[k][i],a[k][j]
                    a[k][i]=a[i][k]=c*ki-s*kj
                    a[k][j]=a[j][k]=s*ki+c*kj
                a[i][i]=oldi-t*b;a[j][j]=oldj+t*b
                a[i][j]=a[j][i]=ZERO
                for k in range(n):
                    qi,qj=q[k][i],q[k][j]
                    q[k][i]=c*qi-s*qj;q[k][j]=s*qi+c*qj
                rotations+=1
    else:
        trace.append(dict(stop='explicit complete Jacobi sweep budget',sweep=JACOBI_SWEEPS,
                          complete_rotations_before=rotations))
    diagonal=[a[i][i] for i in range(n)]
    residual=[[x-y*diagonal[j] for j,(x,y) in enumerate(zip(row,qr))]
              for row,qr in zip(mm(matrix,q),q)]
    gram=mm(transpose(q),q)
    return diagonal,q,dict(complete_matrix=matrix,complete_transformed_matrix=a,
        complete_nine_columns=q,complete_nine_diagonal=diagonal,sweeps=trace,
        actual_rotation_count=rotations,complete_BQ_minus_Qdiag=residual,
        complete_QtQ_minus_I=[[gram[i][j]-(ONE if i==j else ZERO) for j in range(n)] for i in range(n)],
        relative_iteration_tolerance=JACOBI_RELATIVE_STOP,
        no_eigenvalue_or_orthogonality_certificate=True,all_nine_columns_retained=True,
        no_singular_value_or_rank_cutoff=True,not_a_new_scientific_acceptance_gate=True)


def shifted_cholesky(matrix,g,shift,record):
    """Solve the actual full9 shifted matrix; retain formation/solve residuals."""
    n=9
    a=[[matrix[i][j]+(shift if i==j else ZERO) for j in range(n)] for i in range(n)]
    l=[[ZERO]*n for unused in range(n)];pivots=[]
    record.update(shift=shift,formed_matrix=a,pivot_squares=pivots,returned=False)
    for i in range(n):
        for j in range(i+1):
            value=a[i][j]-sum((l[i][k]*l[j][k] for k in range(j)),ZERO)
            if i==j:
                pivots.append(value)
                if value<=0 or not value.is_finite():
                    record.update(failed_pivot=i,failed_pivot_value=value,
                                  failure='finite Cholesky pivot not positive')
                    raise NumericalFailure('The proposed shift does not form positive finite Cholesky pivots')
                l[i][j]=value.sqrt()
            else:
                l[i][j]=value/l[j][j]
    y=[ZERO]*n;z=[ZERO]*n
    for i in range(n):
        y[i]=(-g[i]-sum((l[i][j]*y[j] for j in range(i)),ZERO))/l[i][i]
    for i in range(n-1,-1,-1):
        z[i]=(y[i]-sum((l[j][i]*z[j] for j in range(i+1,n)),ZERO))/l[i][i]
    if not finite(z):
        raise NumericalFailure('The complete shifted solve returned a nonfinite vector')
    record.update(returned=True,complete_factor=l,complete_solution=z,
        formed_linear_residual=add(mv(a,z),g),
        factor_product_minus_formed_matrix=[[x-y for x,y in zip(r,s)] for r,s in zip(mm(l,transpose(l)),a)],
        formed_relative_step_L2=norm(z),positive_finite_pivots_not_an_interval_SPD_proof=True)
    return z


def ambient_direction(model,p,state,pilot,radius,record):
    if radius<=0 or not radius.is_finite():
        raise NumericalFailure('The explicit ambient exploration radius must be positive and finite')
    with model.context('outer/full-nine-second-forward'):
        J,H,second,second_state=model.curvature(p)
    residual=state['equation'];scales=[max(ONE,abs(x)) for x in p]
    A=[[J[i][j]*scales[j] for j in range(9)] for i in range(3)]
    gradient=mv(transpose(A),residual)
    gn=mm(transpose(A),A)
    correction=[[ZERO]*9 for unused in range(9)]
    B=[[ZERO]*9 for unused in range(9)]
    for i in range(9):
        for j in range(i,9):
            v=sum((residual[k]*H[k][i][j]*scales[i]*scales[j] for k in range(3)),ZERO)
            correction[i][j]=correction[j][i]=v
            B[i][j]=B[j][i]=gn[i][j]+v
    record.update(path='ambient-straight-line',formula='q(alpha)=p+alpha*d',
        complete_second_forward=second,complete_three_by_nine_J=J,
        complete_three_by_nine_by_nine_H=H,original_current_equations=residual,
        second_primal_equations=second_state['equation'],
        second_primal_words_equal_current=second_state['equation']==residual,
        original_first_forward_axis_J=pilot,
        second_J_minus_original_axis_J=[[x-y for x,y in zip(a,b)] for a,b in zip(J,pilot)],
        relative_parameter_scales=scales,complete_scaled_J=A,
        complete_relative_gradient=gradient,complete_Gauss_Newton_term=gn,
        complete_residual_curvature_term=correction,complete_ambient_merit_Hessian=B,
        curvature_formula='(J D)^T(J D)+sum_k F_k D Hessian(F_k) D',
        no_normal_curve_Hessian_claimed=True,normal_correction_not_used_for_primary_trials=True,
        original_unweighted_full_three_merit=True,all_nine_axes_retained=True,
        radius=radius,shift_trials=[],finite_model_candidate_pool=[])
    if not finite(gradient) or not all(finite(row) for row in B):
        raise NumericalFailure('The complete ambient gradient or Hessian is nonfinite')
    gnorm=norm(gradient)
    if gnorm==0:
        raise NumericalFailure('The formed full merit gradient is exactly zero; original strict slope not supplied')
    eigen,q,spectral=jacobi_full(B);record['spectral_guidance']=spectral
    bnorm=norm([x for row in B for x in row])
    margin=SHIFT_RELATIVE_MARGIN*max(ONE,bnorm)
    lower=max(ZERO,-min(eigen));upper=lower+margin
    chosen=None

    def solve(shift,label):
        item=dict(index=len(record['shift_trials']),label=label)
        record['shift_trials'].append(item)
        try:
            z=shifted_cholesky(B,gradient,shift,item)
            item['within_requested_radius']=norm(z)<=radius
            return z
        except (NumericalFailure,DecimalException) as error:
            item['exception']=repr(error)
            return None

    for unused in range(SHIFT_BRACKET):
        z=solve(upper,'complete-shift-radius-bracket')
        if z is not None and norm(z)<=radius:
            chosen=z;break
        lower=upper
        upper=max(TWO*upper,upper+max(ONE,margin))
        if not upper.is_finite():
            break
    if chosen is not None:
        for unused in range(SHIFT_BISECTIONS):
            mid=(lower+upper)/TWO
            if not lower<mid<upper:
                break
            z=solve(mid,'complete-shift-arithmetic-refinement')
            if z is not None and norm(z)<=radius:
                upper,chosen=mid,z
            else:
                lower=mid
            if chosen is not None and norm(chosen)>=RELATIVE_BOUNDARY_TARGET*radius:
                break
    record.update(shift_relative_margin=SHIFT_RELATIVE_MARGIN,
        formed_shift_margin=margin,final_shift_lower=lower,final_shift_upper=upper,
        shifted_solve_returned=chosen is not None,
        no_spectrum_accuracy_or_shift_residual_gate=True)

    candidates=[]
    def consider(z,label,extra=None):
        item=dict(index=len(record['finite_model_candidate_pool']),label=label,
                  proposed_relative_direction=list(z),eligible=False)
        if extra:
            item.update(extra)
        record['finite_model_candidate_pool'].append(item)
        if not finite(z):
            item['reason']='nonfinite direction';return
        size=norm(z)
        if size==0:
            item['reason']='exactly zero direction';return
        if size>radius:
            item['explicit_proposal_rescale_factor']=radius/size
            z=scale(z,radius/size);size=norm(z)
        slope=dot(gradient,z);curvature=dot(z,mv(B,z))
        value=slope+curvature/TWO
        item.update(actual_relative_direction=z,actual_relative_step_L2=size,
            formed_linear_slope=slope,formed_quadratic_curvature=curvature,
            formed_quadratic_model_change=value)
        if not slope.is_finite() or slope>=0 or not value.is_finite():
            item['reason']='does not supply the original finite strict descent slope';return
        item.update(eligible=True,reason='finite full-model proposal; real Armijo still required')
        candidates.append((value,item['index'],z))

    if chosen is not None:
        consider(chosen,'full-nine-shifted-Newton-trust-proposal',dict(selected_shift=upper))
    gBg=dot(gradient,mv(B,gradient));t=radius/gnorm
    if gBg>0:
        t=min(t,gnorm*gnorm/gBg)
    consider(scale(gradient,-t),'full-nine-Cauchy-proposal',dict(cauchy_parameter=t))
    # Every spectral column is recorded; it is only an additional bounded
    # negative-curvature proposal, never a truncated solve or a rank decision.
    for j in range(9):
        v=[q[i][j] for i in range(9)];vn=norm(v)
        beta=dot(v,mv(B,v))
        if vn==0 or not beta.is_finite() or beta>=0:
            record['finite_model_candidate_pool'].append(dict(
                index=len(record['finite_model_candidate_pool']),label='spectral-column-'+str(j),
                complete_column=v,actual_formed_curvature=beta,eligible=False,
                reason='no finite negative curvature along this complete column'))
            continue
        z=scale(v,radius/vn)
        if dot(gradient,z)>0:
            z=scale(z,-ONE)
        consider(z,'negative-curvature-column-'+str(j),dict(
            complete_column=v,actual_formed_curvature=beta,
            finite_spectral_direction_is_not_an_eigenvalue_certificate=True))
    if not candidates:
        raise NumericalFailure('No full-model proposal supplied the original strict descent requirement')
    _,index,z=min(candidates,key=lambda item:(item[0],item[1]))
    direction=[x*s for x,s in zip(z,scales)]
    with model.context('outer/chosen-ambient-direction-original-forward'):
        response,rr,rs=model.response(p,[[x] for x in direction],label='actual-ambient-line-direction')
    action=[row[0] for row in response];actual_slope=dot(residual,action)
    record.update(selected_model_candidate=index,selected_candidate=record['finite_model_candidate_pool'][index],
        actual_nine_parameter_direction=direction,actual_relative_direction=z,
        scaled_direction_L2=norm(z),actual_direction_forward=rr,
        actual_direction_primal_equations=rs['equation'],
        actual_direct_full3_action=action,formed_axis_action=mv(J,direction),
        direct_minus_formed_axis_action=sub(action,mv(J,direction)),
        actual_full3_slope=actual_slope,ambient_directional_second=dot(z,mv(B,z)),
        finite_model_best_not_a_claim_of_best_nonlinear_trial=True,
        discrete_rounding_derivative_or_interval_certificate=False)
    if not actual_slope.is_finite() or actual_slope>=0:
        raise NumericalFailure('Selected proposal failed the original actual finite strict slope requirement')
    return direction,action


def search(model,state,J,radius,status,checkpoint,event_sink):
    """Eight actual directions, up to20 line trials then separate old fallback."""
    p=list(state['parameters']);accepted_points=0
    status['searches']=[];status['phase']='decimal50-full-ambient-curvature-search'
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
            path_status=dict(ambient_straight=dict(started=False,trial_budget=20),
                             original149_normal_fallback=dict(started=False,trial_budget=20,
                                 normal_iterations=12,normal_backtracks=20)))
        status['searches'].append(row);checkpoint()
        for path in ('ambient_straight','original149_normal_fallback'):
            path_record=row['path_status'][path]
            path_record['started']=True
            try:
                if path=='ambient_straight':
                    direction,action=ambient_direction(model,p,state,J,radius,row['direction_model'])
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
                    if path=='ambient_straight':
                        with model.context('outer-'+str(iteration)+'/ambient-straight-'+str(trial)):
                            candidate=model.evaluate(item['seed_parameters'])
                        item['normal_correction']=dict(called=False,
                            reason='ambient Hessian predicts only this actual straight path')
                        predicted=-alpha*slope-alpha*alpha*row['direction_model']['ambient_directional_second']/TWO
                        prediction_label='full ambient merit Hessian on q=p+alpha*d'
                    else:
                        candidate=legacy.curved_candidate(model,p,state,direction,action,frame,alpha,
                            item['normal_correction'],'outer-'+str(iteration)+'/legacy-fallback-'+str(trial))
                        predicted=before-dot(add(residual,scale(action,alpha)),add(residual,scale(action,alpha)))/TWO
                        prediction_label='unchanged149 linear residual model; not the ambient curvature model'
                    actual=merit(candidate)
                    item.update(actual_merit=actual,actual_parameters=candidate['parameters'],
                        actual_unit_equations=candidate['equation'],actual_full112_right=candidate['full_right'],
                        actual_decimal_parameter_displacement=sub(candidate['parameters'],p),
                        actual_path_model_predicted_reduction=predicted,prediction_scope=prediction_label)
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
                event_sink(dict(event='decimal50-curvature-actual-outer-trial',iteration=iteration,
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
                if path=='ambient_straight':
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
