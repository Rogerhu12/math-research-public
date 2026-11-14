"""Finite search comparison only: tolerate recorded central dot-product rounding.

The QP constraint remains its caller's original central lower bound. No
physical field, Gauss/Codazzi row, curvature cap, tail box, radius domain,
or final geometric condition is changed. The frozen provider remains intact.
"""
import numpy as np


def checked_search_domain(problem,vector,central_cap,central_floor):
    """Return (permitted, diagnostic); first try the original strict guard.

Only a central *lower* comparison within a conservative floating dot-sum
scale can be admitted. This is not a continuous curvature certificate.
    """
    if problem.parameter_domain(vector,central_cap,central_floor):
        return True,dict(original_strict_domain=True,roundoff_admitted=False)
    _,p=problem.unpack(np.asarray(vector,float))
    if not np.all(np.isfinite(p)):
        return False,dict(original_strict_domain=False,roundoff_admitted=False,reason='nonfinite parameters')
    coeff=p[:problem.K];n=problem.seed+problem.core_basis@coeff
    scale=float(np.max(np.abs(problem.seed)+np.abs(problem.core_basis)@np.abs(coeff)))
    eps=np.finfo(float).eps;k=int(problem.K)+2;gamma=k*eps/(1-k*eps)
    allowance=4*gamma*max(1.,scale)
    near=(float(n.min())<central_floor and float(n.min())>0.
          and float(n.min())>=central_floor-allowance
          and float(n.max())<=central_cap)
    accepted=bool(near and problem.parameter_domain(vector,central_cap,central_floor-allowance))
    return accepted,dict(original_strict_domain=False,roundoff_admitted=accepted,
        central_minimum=float(n.min()),central_maximum=float(n.max()),
        requested_QP_lower_bound=float(central_floor),search_comparison_allowance=allowance,
        observed_lower_difference=float(n.min()-central_floor),
        formula='4*gamma_(K+2)*max(1,max(abs(seed)+abs(B)@abs(c)))',
        all_other_domain_checks_unchanged=True,QP_constraint_changed=False,
        physical_field_or_equations_changed=False,continuous_geometry_claimed=False)
