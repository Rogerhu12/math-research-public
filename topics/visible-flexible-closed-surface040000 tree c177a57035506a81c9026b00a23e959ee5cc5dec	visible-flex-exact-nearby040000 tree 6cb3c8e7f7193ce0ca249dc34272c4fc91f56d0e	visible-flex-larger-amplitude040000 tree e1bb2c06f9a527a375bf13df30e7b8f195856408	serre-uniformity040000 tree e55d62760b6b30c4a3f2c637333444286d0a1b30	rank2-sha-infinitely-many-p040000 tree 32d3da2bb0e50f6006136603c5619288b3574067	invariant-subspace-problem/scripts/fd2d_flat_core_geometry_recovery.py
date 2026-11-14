"""R133 geometry consumers reconstructed after executor loss.

This is a new source identity. Point evaluation uses finite quadrature; all
continuous distance bounds are conditional on supplied true error budgets.
No nonlinear prefix or complete strong surface is asserted by this module.
"""
from __future__ import annotations
from fractions import Fraction
import numpy as np
from fd2d_balanced_curvature_core import FixedBalancedGeometry, BalancedCurvatureCore


def _maxabs(x):
    x=np.asarray(x)
    return float(np.max(np.abs(x))) if x.size else 0.


def central_linear_domain(modes, geometry=None, base_kind='balanced_seed',
                          samples=512, reach_radius=Fraction(17,125)):
    geom=FixedBalancedGeometry() if geometry is None else geometry
    count=int(modes)
    if count<0 or int(samples)<4: raise ValueError("invalid central sample size")
    core=BalancedCurvatureCore(np.zeros(count),base_kind=base_kind,geometry=geom)
    phi=2*np.pi*np.arange(int(samples))/int(samples)
    row=core.curvature(phi)
    B=np.asarray(row['parameter_basis'],float)
    n0=np.asarray(row['n'],float)
    rho=float(reach_radius)
    if not rho>0: raise ValueError("positive reach radius required")
    return dict(phi=phi,basis=B,base_curvature=n0,
                strict_lower_rhs=-n0,upper_rhs=1/rho-n0,
                inequality="strict_lower_rhs < basis @ d <= upper_rhs",
                reach_radius=rho,definition=core.definition(),
                sampled_necessary_only=True,
                positive_curvature_is_selected_ansatz=True,
                floating_halfspaces_are_not_interval_certified=True)


def central_geometry(coefficients,geometry=None,base_kind='balanced_seed',
                     samples=512,reach_radius=Fraction(17,125)):
    geom=FixedBalancedGeometry() if geometry is None else geometry
    core=BalancedCurvatureCore(coefficients,base_kind=base_kind,geometry=geom)
    phi=2*np.pi*np.arange(int(samples))/int(samples)
    fields=core.evaluate_normal_angle(phi)
    axes=core.axis_intercepts_and_jacobian()
    definition=core.definition()
    lower=Fraction(definition['conservative_curvature_lower_exact'])
    upper=Fraction(definition['conservative_curvature_upper_exact'])
    rho=Fraction(reach_radius)
    summary=dict(A=float(axes['A']),B=float(axes['B']),gap=float(axes['gap']),
        sampled_n_min=float(np.min(fields['n'])),sampled_n_max=float(np.max(fields['n'])),
        exact_conservative_lower=str(lower),exact_conservative_upper=str(upper),
        global_convexity_from_exact_l1_bound=lower>0,
        central_curvature_cap_from_exact_l1_bound=upper<=1/rho,
        axis_intercepts_are_supports_under_proved_convexity=lower>0,
        central_gap_at_least_point9_sample=float(axes['gap'])>=.9,
        actual_curve_point_evaluation_interval_certified=False,
        strong_prefix_solved=False)
    return dict(core=core,fields=fields,axes=axes,summary=summary,
                definition=definition,
                domain=central_linear_domain(len(coefficients),geom,base_kind,samples,reach_radius))


def _frame(data):
    return np.stack([np.asarray(data[k],float) for k in ('e1','e2','N')],axis=-1)


def register_tail_from_actual_cut(tail,material_u,actual_cut,anchor=0):
    u=np.asarray(material_u,float)
    if u.ndim!=1 or not len(u): raise ValueError("one nonempty material-u vector required")
    port=tail.cut_port(u)
    Fc,Ft=_frame(actual_cut),_frame(port)
    if Fc.shape!=Ft.shape: raise ValueError("cut frames have different shapes")
    j=int(anchor)
    raw=Fc[j]@Ft[j].T
    U,sv,Vt=np.linalg.svd(raw)
    sign=np.sign(np.linalg.det(U@Vt))
    D=np.diag([1.,1.,sign])
    R=U@D@Vt
    xc=np.asarray(actual_cut['X'],float)
    translation=xc[j]-R@np.asarray(port['X'][j],float)
    vector_keys=('X','e1','e2','N','X_s','X_u','X_ss','X_su','X_uu')
    errors={}
    for key in vector_keys:
        if key in actual_cut and key in port:
            mapped=np.asarray(port[key],float)@R.T
            if key=='X': mapped=mapped+translation
            errors[key]=_maxabs(np.asarray(actual_cut[key],float)-mapped)
    scalar_errors={key:_maxabs(np.asarray(actual_cut[key])-np.asarray(port[key]))
                   for key in ('l','m','n') if key in actual_cut}
    plane_origin=translation+R@np.array([0.,0.,tail.plane_height])
    plane_normal=R[:,2]
    eye=np.eye(3)
    return dict(rotation=R,translation=translation,raw_anchor_rotation=raw,
        polar_correction_norm=float(np.linalg.norm(R-raw,ord=2)),
        raw_rotation_singular_values=sv,
        core_frame_gram_defect=_maxabs(np.swapaxes(Fc,-1,-2)@Fc-eye),
        tail_frame_gram_defect=_maxabs(np.swapaxes(Ft,-1,-2)@Ft-eye),
        full_sample_vector_errors=errors,full_sample_II_errors=scalar_errors,
        template_plane_height=float(tail.plane_height),
        actual_plane_origin=plane_origin,actual_plane_normal=plane_normal,
        actual_plane_height=float(plane_origin[2]),
        tilt_from_horizontal=float(np.linalg.norm(plane_normal[:2])),
        horizontal_axis_offset=float(np.linalg.norm(plane_origin[:2])),
        height_is_uniform_world_z_only_if_plane_exactly_horizontal=True,
        alignment_is_interval_certified=False,
        scope="One anchor defines a rigid candidate; all-angle complete cut compatibility remains to be proved.")


def tail_budget_at_registered_height(tail,registration,Aq,
                                     upright_centered_proved=False,
                                     reach_radius=Fraction(17,125)):
    bounds=tail.sufficient_bounds()
    if not bounds.get('selected_box_0_to_6_over_5',False):
        raise ValueError("R130 uniform budget here requires the R132 selected positive Bernstein box")
    Z=float(registration['actual_plane_height'])
    a=float(tail.cut_radius);Aq=float(Aq);rho=float(reach_radius)
    drop=float(bounds['absolute_deflection_upper'])
    Kt=float(bounds['absolute_curvature_upper'])
    relevant=Aq>=a and Z>=drop
    distance_squared=(Aq-a)**2+(Z-drop)**2 if relevant else None
    return dict(actual_Z=Z,actual_Aq=Aq,deflection_upper=drop,
        height_lower=Z-drop,height_upper=Z,xy_radius_upper=a,
        world_sphere_radius_squared_upper=a*a+max(Z*Z,(Z-drop)**2),
        held_distance_squared_lower=distance_squared,
        held_formula_domain_valid=relevant,
        held_at_least_point9_conditional=relevant and distance_squared>=.81,
        slab_half_width_upper=a,curvature_upper=Kt,
        complete_cylinder_reach_lower=(1/Kt if Kt>0 else "unbounded"),
        internal_normal_pair_radius_pass=Kt*rho<=1,
        upright_centered_alignment_is_proved=bool(upright_centered_proved),
        scope="R130 consequences conditional on actual upright centered registration and rigorous evaluation; no prefix geometry supplied.")


def _point_error_array(value,shape,name):
    q=np.broadcast_to(np.asarray(value,float),shape).reshape(-1)
    if np.any(q<0) or not np.all(np.isfinite(q)): raise ValueError("invalid "+name)
    return q


def flat_disk_cross_normal_balls(P,N,tail,registration=None,
        reach_radius=Fraction(17,125),angle_nodes=513,point_chunk=128,
        point_error=0.,normal_error=0.,tail_position_error=0.,
        tail_normal_error=0.,arithmetic_error=0.,errors_are_certified=False,
        tail_curvature_upper=None):
    P,N=np.broadcast_arrays(np.asarray(P,float),np.asarray(N,float))
    if P.shape[-1]!=3: raise ValueError("points and normals need last dimension three")
    shape=P.shape[:-1]
    if not np.all(np.isfinite(P)) or not np.all(np.isfinite(N)):
        raise ValueError("finite representatives required")
    p=P.reshape(-1,3);n=N.reshape(-1,3)
    if registration is not None:
        R=np.asarray(registration['rotation'],float)
        t=np.asarray(registration['translation'],float)
        p=(p-t)@R
        n=n@R
    rho=float(reach_radius)
    if not rho>0 or int(angle_nodes)<2: raise ValueError("positive radius and endpoint grid required")
    v=np.linspace(-np.pi/2,np.pi/2,int(angle_nodes))
    a=float(tail.cut_radius);y=a*np.sin(v);width=np.maximum(a*np.cos(v),0.)
    width[[0,-1]]=0.
    curve=tail.curve(y)
    base=np.column_stack((curve['X'],tail.plane_height-curve['Z']))
    normal=np.column_stack((curve['sin_alpha'],curve['cos_alpha']))
    bound=tail.sufficient_bounds()
    Kt=float(bound['absolute_curvature_upper'] if tail_curvature_upper is None else tail_curvature_upper)
    if not np.isfinite(Kt) or Kt<0: raise ValueError("finite nonnegative true tail curvature bound required")
    maxgap=float(np.max(np.diff(v)))
    loss=np.array([a,a,a*(1+rho*Kt),a*(1+rho*Kt)])*maxgap/2
    sampled=np.empty((len(p),4))
    for first in range(0,len(p),max(1,int(point_chunk))):
        last=min(len(p),first+max(1,int(point_chunk)))
        pp,nn=p[first:last],n[first:last]
        centers=(pp-rho*nn,pp+rho*nn,pp,pp)
        sections=(base,base,base-rho*normal,base+rho*normal)
        for k,(cc,ss) in enumerate(zip(centers,sections)):
            dx=np.maximum(np.abs(cc[:,0,None])-width[None,:],0.)
            dy=cc[:,1,None]-ss[None,:,0]
            dz=cc[:,2,None]-ss[None,:,1]
            sampled[first:last,k]=np.sqrt(np.min(dx*dx+dy*dy+dz*dz,axis=1))
    ex=_point_error_array(point_error,shape,'point_error')
    en=_point_error_array(normal_error,shape,'normal_error')
    et=_point_error_array(tail_position_error,shape,'tail_position_error')
    ent=_point_error_array(tail_normal_error,shape,'tail_normal_error')
    ea=_point_error_array(arithmetic_error,shape,'arithmetic_error')
    e1=ex+rho*en+et+ea
    e2=ex+et+rho*ent+ea
    errors=np.column_stack((e1,e1,e2,e2))
    lower=sampled-loss[None,:]-errors
    covered=np.all(lower>=rho,axis=1)
    return dict(sampled_minimum_distances=sampled.reshape(shape+(4,)),
        continuous_conditional_lower_bounds=lower.reshape(shape+(4,)),
        target_radius=rho,lipschitz_grid_loss=loss,
        supplied_error_loss=errors.reshape(shape+(4,)),
        covered_by_conditional_bound=covered.reshape(shape),
        covered_count=int(np.sum(covered)),point_count=len(p),
        errors_are_certified_by_caller=bool(errors_are_certified),
        normal_unit_defect_sample=_maxabs(np.linalg.norm(N,axis=-1)-1),
        tail_curvature_upper=Kt,angle_nodes=int(angle_nodes),max_v_gap=maxgap,
        four_cases=['prefix_minus_to_tail','prefix_plus_to_tail','prefix_to_tail_minus','prefix_to_tail_plus'],
        certificate=False,
        scope="Exact one-dimensional reduction with finite sampled distance minus a conditional Lipschitz/error loss. Caller must certify all evaluation, registration, unit-normal and rounding errors; seams with zero margin require local analysis.")
