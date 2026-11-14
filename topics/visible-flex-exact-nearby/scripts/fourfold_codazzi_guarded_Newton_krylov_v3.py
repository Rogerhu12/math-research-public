#!/usr/bin/env python3
"""The original actual-domain Newton guard, releasing each LU before rebuilding.

The full matrix-free Jacobian is solved by residual-checked GMRES. An actual trial that already passes the complete Newton tolerance gate is
accepted directly; this avoids an unnecessary second GMRES solve. All nonlinear residual evaluations,
actual-C/nu domain checks, line searches and convergence tests are unchanged.
The old factor must not coexist with the next sparse Jacobian and LU.
This v3 preserves the actual RuntimeError identity on construction failure;
no convergence test, nonlinear equation, full action or solve gate is altered.
"""
from __future__ import annotations
import resource
import numpy as np
from scipy.sparse.linalg import splu


def guarded_parameter_newton_krylov_v3(system,history,floor,ceiling,maxnu,max_iterations):
    def feasible(r,y,p):
        if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)) or abs(p[0])>=maxnu:return False
        try:B,C=system.actual_fields(r,y,p)
        except (ValueError,ZeroDivisionError,FloatingPointError):return False
        return bool(np.all(np.isfinite(B)) and np.all(np.isfinite(C)) and
            np.all(C < -floor) and np.all(C > -ceiling) and np.all(abs(B)<ceiling))
    def newton(n,m,h,col_fun,bc,jac,y,p,singular_projection,bvp_tol,bc_tol):
        r=np.r_[0.,np.cumsum(h)];midr=r[:-1]+h/2;threshold=(2/3)*h*.05*bvp_tol
        if not feasible(r,y,p):
            history.append(dict(reason='initial iterate leaves chosen actual C/nu search domain',nodes=m,nu=float(p[0])))
            return y,p,True
        for iteration in range(max_iterations):
            col,mid,f,fmid=col_fun(y,p);boundary=bc(y[:,0],y[:,-1],p)
            if not feasible(midr,mid,p) or not all(np.all(np.isfinite(z)) for z in (col,mid,f,fmid,boundary)):
                history.append(dict(reason='current midpoint leaves chosen actual search domain',nodes=m,iteration=iteration))
                return y,p,True
            residual=np.r_[col.ravel(order='F'),boundary]
            if np.all(abs(col)<threshold*(1+abs(fmid))) and np.all(abs(boundary)<bc_tol):
                history.append(dict(reason='collocation Newton tolerance reached',nodes=m,iteration=iteration,nu=float(p[0])))
                return y,p,False
            try:factor=jac(y,p,mid,f,fmid,boundary)
            except RuntimeError as error:
                item=dict(reason='full linearization/preconditioner construction failed',nodes=m,iteration=iteration,
                    exception_type=type(error).__name__,exception_message=str(error),
                    peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
                history.append(item);print(dict(actual_construction_exception=item),flush=True)
                return y,p,True
            try:step=factor.solve(residual)
            except RuntimeError as error:
                history.append(dict(reason=str(error),nodes=m,iteration=iteration));return y,p,True
            cost=float(step@step)
            if not np.isfinite(cost):
                history.append(dict(reason='nonfinite normalized Newton correction',nodes=m,iteration=iteration));return y,p,True
            dy=step[:n*m].reshape(n,m,order='F');dp=step[n*m:];accepted=False;fraction=1.;converged_trial=False
            for trial in range(24):
                proposed=y-fraction*dy;newp=p-fraction*dp
                if singular_projection is not None:proposed[:,0]=singular_projection@proposed[:,0]
                if feasible(r,proposed,newp):
                    cc,mm,ff,fm=col_fun(proposed,newp);bb=bc(proposed[:,0],proposed[:,-1],newp)
                    if feasible(midr,mm,newp) and all(np.all(np.isfinite(z)) for z in (cc,mm,ff,fm,bb)):
                        # Exactly the same complete tolerance test used at
                        # the top of this Newton loop. A converged trial needs
                        # no further inverse-Jacobian residual to be accepted.
                        if np.all(abs(cc)<threshold*(1+abs(fm))) and np.all(abs(bb)<bc_tol):
                            accepted=True;converged_trial=True;newcost=None;break
                        rr=np.r_[cc.ravel(order='F'),bb]
                        try:correction=factor.solve(rr)
                        except RuntimeError as error:
                            history.append(dict(reason=str(error),nodes=m,iteration=iteration,trial=trial));return y,p,True
                        newcost=float(correction@correction)
                        if np.isfinite(newcost) and newcost<(1-.1*fraction)*cost:accepted=True;break
                fraction*=.5
            history.append(dict(nodes=m,iteration=iteration,accepted=accepted,step_fraction=fraction,
                nu=float(p[0]),proposed_nu=float(newp[0]),affine_invariant_cost=cost,next_cost=newcost if accepted else None,
                max_collocation_residual=float(np.max(abs(col))),max_boundary_residual=float(np.max(abs(boundary))),
                trial_already_passed_complete_collocation_and_boundary_tolerances=converged_trial,
                converged_trial_collocation_residual=float(np.max(abs(cc))) if converged_trial else None,
                converged_trial_boundary_residual=float(np.max(abs(bb))) if converged_trial else None))
            if not accepted:
                history.append(dict(reason='no admissible decreasing step in 24 backtracks; not an asserted singularity',nodes=m))
                return y,p,True
            y,p=proposed,newp
            if hasattr(system,"accepted_checkpoint"):system.accepted_checkpoint(y,p,ff,history[-1])
            del factor
            history[-1]["peak_resident_KiB"]=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            print(dict(released_Newton_step=history[-1]),flush=True)
            if converged_trial:return y,p,False
        history.append(dict(reason='per-mesh Newton iteration limit',nodes=m,iterations=max_iterations));return y,p,False
    return newton

