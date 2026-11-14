"""Finite diagnostic for the exact D2 height-only cut-registration theorem.

Axis order is exactly u=(0,pi/2,pi,3pi/2).  This code reports finite
residuals and sign margins; it does not replace an actual registration by
identity merely because a sampled symmetry residual is small.
"""
from __future__ import annotations
import numpy as np
from fd2d_flat_core_geometry_recovery import register_tail_from_actual_cut


def height_only_cut_diagnostic(tail,material_u,actual_cut,actual_axis_positions,
                               axis_position_error=0.,
                               errors_are_certified=False):
    axis=np.asarray(actual_axis_positions,float)
    if axis.shape!=(4,3) or not np.all(np.isfinite(axis)):
        raise ValueError("Four actual axis positions in order 0,pi/2,pi,3pi/2 required")
    error=np.broadcast_to(np.asarray(axis_position_error,float),(4,))
    if np.any(error<0) or not np.all(np.isfinite(error)):
        raise ValueError("Finite nonnegative true point-error bounds required")
    u=np.asarray(material_u,float)
    registration=register_tail_from_actual_cut(tail,u,actual_cut)
    Z=float((axis[0,2]+axis[2,2])/2)
    Z_error=float((error[0]+error[2])/2)
    port=tail.cut_port(u)
    delta=np.array([0.,0.,Z-tail.plane_height])
    vertical_errors={}
    for name in ('X','e1','e2','N','X_s','X_u','X_ss','X_su','X_uu'):
        if name in actual_cut and name in port:
            target=np.asarray(port[name],float)+(delta if name=='X' else 0)
            vertical_errors[name]=float(np.max(np.abs(np.asarray(actual_cut[name],float)-target)))
    II_errors={name:float(np.max(np.abs(np.asarray(actual_cut[name],float)-port[name])))
               for name in ('l','m','n') if name in actual_cut}
    Sx=np.diag([-1.,1.,1.]);Sy=np.diag([1.,-1.,1.])
    mirror=dict(
        x_pair=float(np.linalg.norm(axis[2]-Sx@axis[0])),
        y_pair=float(np.linalg.norm(axis[3]-Sy@axis[1])),
        u0_fixed_y=float(np.linalg.norm(axis[0]-Sy@axis[0])),
        uhalfpi_fixed_x=float(np.linalg.norm(axis[1]-Sx@axis[1])))
    cutcurve=tail.curve(np.array([tail.cut_radius]))
    B=float(cutcurve['X'][0])
    sign_lower=np.array([axis[0,0]-error[0],axis[1,1]-error[1]])
    return dict(actual_Z_candidate=Z,axis_average_Z_error_upper=Z_error,
        actual_Z_conditional_interval=[Z-Z_error,Z+Z_error],
        tail_axis_y_intercept=B,tail_axis_y_intercept_is_numerical=True,
        ordered_axis_sign_lower=sign_lower,
        ordered_axis_signs_positive_given_error_bounds=bool(np.all(sign_lower>0)),
        axis_mirror_defects=mirror,
        height_only_full_sample_vector_errors=vertical_errors,
        height_only_full_sample_II_errors=II_errors,
        unconstrained_proper_registration=registration,
        errors_are_certified_by_caller=bool(errors_are_certified),
        certificate=False,
        exact_theorem_requires=[
            'same fixed material-u origin, orientation and mirror labels',
            'exact D2 central data and exact l/n-even,m-odd radial fields',
            'actual common cut metric and actual all-angle m,n equality',
            'proper same-oriented frame congruence',
            'strict positive ordered actual cut axis signs'],
        full_two_jet_seam_also_requires='actual l equality, including n=0 arcs',
        scope="Finite diagnostics only. Under the listed exact hypotheses the proof forces R=I and horizontal t=0; otherwise retain the full R133 registration and its errors.")
