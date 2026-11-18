"""Add the two original RMS-point domain checks to the original Newton trials.

The finite collocation residual, its Jacobian, affine-invariant merit and all
thresholds stay unchanged. The original col_fun four-tuple is returned as-is.
The two additional calls use the original wrapped RHS and original spline;
their values do not enter the Newton residual or a new RMS acceptance test.

This also records original Newton states, including every accepted assignment,
both return paths, and the most recent evaluation if an exception escapes.
These are raw numerical states, not accepted BVP or geometric certificates.
"""
import ast
import copy
import hashlib
import json
from pathlib import Path
import traceback
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()
def function_text(path,name):
    text=Path(path).read_text();node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return ''.join(text.splitlines(keepends=True)[node.lineno-1:node.end_lineno])+'\n'
def replace_once(text,old,new):
    if text.count(old)!=1:raise ValueError('Original Newton source anchor changed: '+old[:100])
    return text.replace(old,new,1)


def recording_newton_source(path):
    """Only observation calls are inserted into the original Newton algebra."""
    text=function_text(path,'solve_newton')
    text=replace_once(text,"    STATS['calls']+=1", "    STATS['calls']+=1\n    RMS_GUARD_HOOK.newton_begin(n,m,h,y,p,B,bvp_tol,bc_tol)")
    text=replace_once(text,'    data=evaluate(y,p);refresh=True;factors=0;threshold=h*(bvp_tol/30.)',
        "    data=evaluate(y,p);refresh=True;factors=0;threshold=h*(bvp_tol/30.)\n    RMS_GUARD_HOOK.save_current('initial_domain_pass',y,p,data,newton_iteration=None)")
    text=replace_once(text,'            except RuntimeError:return y,p,True',
        "            except RuntimeError:\n                RMS_GUARD_HOOK.save_current('singular_return',y,p,data,singular=True,newton_iteration=iteration)\n                return y,p,True")
    marker="        y,p,data,step,cost,alpha=accepted;STATS['accepted_steps']+=1;STATS['minimum_alpha']=min(STATS['minimum_alpha'],alpha);refresh=alpha!=1."
    text=replace_once(text,marker,marker+"\n        RMS_GUARD_HOOK.save_current('accepted_assignment',y,p,data,alpha=alpha,newton_iteration=iteration)")
    text=replace_once(text,'    return y,p,False',
        "    RMS_GUARD_HOOK.save_current('ordinary_return',y,p,data,singular=False,newton_iteration=iteration)\n    return y,p,False")
    compile(text,str(path)+'-recorded','exec')
    return text


class GuardAndSnapshots:
    def __init__(self,owner,bvp,domain):
        self.owner,self.bvp,self.domain=owner,bvp,domain
        self.original_prepare_sys=bvp.prepare_sys
        self.system_number=0;self.newton_number=0;self.snapshot_number=0
        self.last_evaluation=None;self.latest_accepted=None
        self.extra_domain_rejections=0;self.original_domain_rejections=0

    def prepare_sys(self,n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        original_col_fun,original_jac=self.original_prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h)
        # Keep the actual original x and h. Do not reconstruct x by cumsum.
        self.x,self.h,self.wrapped_fun=x,h,fun
        self.system_number+=1
        self.owner.event('rms_guard_system_prepared',prepared_system=self.system_number,nodes=m,parameters=k)
        def col_fun(Y,P):
            state=dict(y=np.asarray(Y).copy(),p=np.asarray(P).copy(),node_rhs=None,cubic=None,
                       phase='original_node_midpoint_rhs',extra_points_passed=False)
            self.last_evaluation=state
            try:values=original_col_fun(Y,P)
            except FloatingPointError as error:
                self.original_domain_rejections+=1;state['error']=repr(error);raise
            cr,ym,ff,fm=values
            # This is precisely the spline and point construction used by
            # estimate_rms_residuals in the bound installed SciPy source.
            sol=self.bvp.create_spline(Y,ff,x,h)
            state.update(node_rhs=np.asarray(ff).copy(),cubic=sol)
            x_middle=x[:-1]+0.5*h
            s=0.5*h*(3/7)**0.5
            x1=x_middle+s
            x2=x_middle-s
            try:
                state['phase']='original_RMS_x1_rhs'
                fun(x1,sol(x1),P)
                state['phase']='original_RMS_x2_rhs'
                fun(x2,sol(x2),P)
            except FloatingPointError as error:
                self.extra_domain_rejections+=1;state['error']=repr(error)
                self.owner.event('extra_RMS_point_domain_rejection',prepared_system=self.system_number,
                    newton_call=self.newton_number,point=state['phase'],error=repr(error),
                    extra_domain_rejections=self.extra_domain_rejections)
                raise
            state.update(phase='all_original_RMS_points_passed',extra_points_passed=True)
            return values  # Identical original tuple, without reassembly.
        return col_fun,original_jac

    def newton_begin(self,n,m,h,y,p,B,bvp_tol,bc_tol):
        if len(self.x)!=m or binary_sha(h)!=binary_sha(self.h):
            raise ValueError('The observed Newton no longer belongs to its original prepared mesh')
        self.newton_number+=1;self.snapshot_number=0
        self.last_evaluation=None;self.latest_accepted=None
        self.anchor=self.owner.inner_anchor(self.owner.rebuilt['obj'])
        self.common=dict(plan=self.owner.plan_path.as_posix(),inner=self.owner.inner_count-1,
            prepared_system=self.system_number,newton_call=self.newton_number,
            coordinate='Original normalized adaptive collocation chart',
            core_kind='exact_m3_circle_trace_replacement_integral',
            core_control_path='circle-trace-replace-last-two-v1',
            core_round_settings=copy.deepcopy(self.owner.plan['design']['new_core_settings']),
            q_gauge=float(self.owner.rebuilt['obj'].q),fixed_metric=False,
            base_frozen_profile=copy.deepcopy(self.owner.plan['design']['physical_profile']),
            parameter_scales=self.owner.rebuilt['obj'].pscale.tolist(),
            x=np.asarray(self.x).tolist(),h=np.asarray(self.h).tolist(),
            singular_left_matrix=None if B is None else np.asarray(B).tolist(),
            original_bvp_tolerance=float(bvp_tol),original_bc_tolerance=float(bc_tol),
            BVP_returned=False,solver_success=None,bvp_message=None,rms_residuals=None,
            recovery_scope='Actual numerical state only. Accepted-step snapshots omit LU/step/cost/refresh and are not an exact restart of Newton control flow; a returned-state snapshot can be used to reconstruct the original subsequent RMS/mesh calculation.',
            scope='Raw Newton state only. No BVP success/RMS/message exists at this layer; no mean-height primitive is silently supplied.')
        self.save_state('before_initial_evaluation',y,p,node_rhs=None,cubic=None,
                        acceptance='Not evaluated; this also preserves an initially invalid state.')

    def save_state(self,stage,y,p,node_rhs,cubic,**extra):
        data=dict(**self.common,stage=stage,y=np.asarray(y).tolist(),p=np.asarray(p).tolist(),
            physical_controls=(np.asarray(p)[1:]*self.owner.rebuilt['obj'].pscale).tolist(),
            node_rhs=None if node_rhs is None else np.asarray(node_rhs).tolist(),
            cubic_available=cubic is not None,newton_stats=dict(self.domain.STATS),**extra)
        if cubic is not None:
            data['raw_cubic']=dict(x=cubic.x.tolist(),c=cubic.c.tolist(),axis=int(cubic.axis),extrapolate=bool(cubic.extrapolate))
        tag=f'inner-{self.owner.inner_count-1:02d}-newton-{self.newton_number:03d}-state-{self.snapshot_number:03d}-{stage}'
        self.snapshot_number+=1
        self.owner.save_raw(tag,data,self.anchor)
        return tag

    def save_current(self,stage,y,p,data,**extra):
        ff=data[3]
        sol=self.bvp.create_spline(y,ff,self.x,self.h)
        tag=self.save_state(stage,y,p,ff,sol,original_RMS_domain_checked=True,**extra)
        if stage=='accepted_assignment':self.latest_accepted=tag

    def escaped_exception(self,error):
        # Preserve the actual most recent evaluation, whether it was an
        # original node/midpoint failure, an extra-point failure, or a later
        # BC/Jacobian exception. Never relabel it as an accepted Newton state.
        state=self.last_evaluation
        if state is not None:
            self.save_state('exception_evaluation',state['y'],state['p'],state['node_rhs'],state['cubic'],
                acceptance='Unaccepted evaluation observed before an escaping exception',
                evaluation_phase=state['phase'],extra_points_passed=state['extra_points_passed'],
                recorded_evaluation_error=state.get('error'),escaping_error=repr(error))
        self.owner.event('guarded_newton_exception',newton_call=self.newton_number,
            latest_saved_accepted_state=self.latest_accepted,error=repr(error),traceback=traceback.format_exc())


def install(owner):
    import scipy
    import scipy.integrate._bvp as bvp
    import f6curve_domain_newton as domain
    binding=owner.plan['lobatto_guard']
    if scipy.__version__!=binding['scipy_version'] or sha(bvp.__file__)!=binding['scipy_bvp']['sha256']:
        raise ValueError('The bound installed SciPy RMS/spline definition changed')
    if sha(domain.__file__)!=binding['original_domain_newton']['sha256']:
        raise ValueError('The original domain-aware Newton changed')
    path=Path(binding['recording_newton_source']['path'])
    if sha(path)!=binding['recording_newton_source']['sha256'] or path.read_text()!=recording_newton_source(domain.__file__):
        raise ValueError('The observation-only Newton excerpt changed')
    hook=GuardAndSnapshots(owner,bvp,domain)
    domain.RMS_GUARD_HOOK=hook
    exec(compile(path.read_text(),str(path),'exec'),domain.__dict__)
    recorded_newton=domain.solve_newton
    def solve_newton(n,m,h,col_fun,bc,jac,y,p,B,bvp_tol,bc_tol):
        try:return recorded_newton(n,m,h,col_fun,bc,jac,y,p,B,bvp_tol,bc_tol)
        except BaseException as error:hook.escaped_exception(error);raise
    # The existing trace wrapper installed by the parent delegates to this
    # module's solve_newton. Its original splu/Jac logging remains in place.
    domain.solve_newton=solve_newton
    bvp.prepare_sys=hook.prepare_sys
    owner.event('same_original_RMS_point_domain_guard_installed',**binding,
        collocation_tuple_preserved=True,original_jacobian_preserved=True,
        additional_RMS_threshold=False,original_merit_and_gates_preserved=True)
    return hook
