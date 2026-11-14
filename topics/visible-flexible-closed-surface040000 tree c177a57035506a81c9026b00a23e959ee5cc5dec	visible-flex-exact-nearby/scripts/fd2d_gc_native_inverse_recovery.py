"""Observed monotone material inverse with a finite bisection fallback.

The first 60 iterations reproduce SavedNativeCoast.evaluate's safeguarded
Newton steps. After that, unfinished entries use bisection in the retained
sign bracket. R139's positive D supplies monotonicity. The material tolerance
is unchanged. This is an explicit alternate caller, not a change to frozen
SavedNativeCoast or a new approximate definition of the native functions.
"""
from __future__ import annotations
import numpy as np
from fd2d_k0_native_gc import native_from_inlet
from fd2d_k0_ruling_coast import ruling_coordinates


def evaluate_monotone_recovery(coast,sigma,u,tolerance=2e-13,
                               newton_iterations=60,bisection_iterations=120,
                               observer=None):
    sigma=float(sigma);target=np.asarray(u,np.longdouble)
    if not 0<=sigma<=coast.length:raise ValueError('Outside the frozen physical coast')
    if not np.all(np.isfinite(target)) or not tolerance>0:raise ValueError('Finite target and positive unchanged tolerance required')
    if sigma==0:
        out=native_from_inlet(coast.a,coast.v,sigma,coast.inlet(target));out['inverse_iterations']=0
        out['inverse_recovery']=dict(method='exact inlet',bisection_used=False,material_residual_maximum=float(np.max(abs(out['material_u']-target))))
        return out
    width=np.pi/(2*coast.v)+1e-8;lo=target-width;hi=target+width;t=target.copy()
    before_fallback=None;all_done=False
    total=int(newton_iterations)+int(bisection_iterations)
    if min(int(newton_iterations),int(bisection_iterations))<1:raise ValueError('Both positive iteration allocations are required')
    for iteration in range(total):
        data=coast.inlet(t);n,m=data['n'],data['m'];k=m/n
        kt=data['m_u']/n-m*data['n_u']/n**2
        coordinates=ruling_coordinates(coast.a,coast.v,sigma,k,kt,np.zeros_like(k))
        derivative=coordinates['U_t']
        residual=t+coordinates['material_shift']-target
        if not np.all(np.isfinite(residual)) or np.any(derivative<=0):raise FloatingPointError('Finite positive monotone reference derivative required')
        done=abs(residual)<=tolerance
        if np.all(done):all_done=True;break
        if iteration==int(newton_iterations):
            bad=np.flatnonzero(~done)
            def words(value):return [np.format_float_scientific(np.asarray(value).ravel()[i],unique=True,trim='k') for i in bad]
            before_fallback=dict(sigma=sigma,sigma_hex=sigma.hex(),iteration=iteration,
                unfinished_indices=bad.tolist(),target_u=words(target),inlet_label_t=words(t),
                residual=words(residual),bracket_lower=words(lo),bracket_upper=words(hi),
                U_t=words(derivative),material_residual_maximum=float(np.max(abs(residual))),
                tolerance=float(tolerance),bracket_width_maximum=float(np.max(hi-lo)))
            if observer is not None:observer(dict(event='inverse_newton_limit',**before_fallback))
        # Exactly the original bracket rule; completed entries are held by
        # the final selection and do not affect any unfinished scalar root.
        lo=np.where(residual<0,t,lo);hi=np.where(residual>0,t,hi)
        if iteration<int(newton_iterations):
            trial=t-residual/derivative
            trial=np.where((trial<=lo)|(trial>=hi),(lo+hi)/2,trial)
        else:
            trial=(lo+hi)/2
        t=np.where(done,t,trial)
    if not all_done:
        if observer is not None:observer(dict(event='inverse_recovery_failed',sigma=sigma,
            iterations=total,material_residual_maximum=float(np.max(abs(residual))),tolerance=float(tolerance)))
        raise RuntimeError('Monotone material inverse recovery did not reach the unchanged tolerance')
    out=native_from_inlet(coast.a,coast.v,sigma,data)
    final=float(np.max(abs(out['material_u']-target)))
    if final>tolerance:raise RuntimeError('Returned native formula failed the unchanged material tolerance')
    out['inverse_iterations']=iteration+1
    info=dict(method='original safeguarded Newton, then retained-bracket bisection',
        bisection_used=before_fallback is not None,newton_iterations=int(newton_iterations),
        allocated_bisection_iterations=int(bisection_iterations),actual_iterations=iteration+1,
        material_residual_maximum=final,tolerance=float(tolerance),failed_newton_state=before_fallback)
    out['inverse_recovery']=info
    if observer is not None and before_fallback is not None:observer(dict(event='inverse_recovery_completed',sigma=sigma,**info))
    return out


def install_observed_recovery(reference,observer=None):
    """Install only on this explicitly owned object's private coast reader."""
    coast=reference._coast
    if hasattr(coast,'_fd2d_original_material_evaluate'):raise ValueError('Recovery is already installed')
    coast._fd2d_original_material_evaluate=coast.evaluate
    def evaluate(sigma,u,tolerance=2e-13,max_iterations=60):
        return evaluate_monotone_recovery(coast,sigma,u,tolerance=tolerance,
            newton_iterations=max_iterations,bisection_iterations=120,observer=observer)
    coast.evaluate=evaluate
    return reference
