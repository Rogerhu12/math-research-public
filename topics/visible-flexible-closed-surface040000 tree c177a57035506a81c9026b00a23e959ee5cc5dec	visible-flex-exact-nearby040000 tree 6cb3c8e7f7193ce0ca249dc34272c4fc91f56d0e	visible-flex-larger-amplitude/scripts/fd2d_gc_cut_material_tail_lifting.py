"""R160 complete cut-material tail lifting, with fixed physical-s window.

This changes the actual finite representation.  It is not a same-field
conversion or a solution.  Where chi=1, the complete lift is the exact
cut rank-one II; zero raw correction followed by R155 then gives R157
without projecting its square root or its tail anisotropy.

The input old packet must carry actual values, physical-s/angle jets,
tail-parameter jets and physical-profile parameter jets.  Returned forcing
is recomputed from those new packets; stale old forcing is never retained.
"""
from __future__ import annotations
from math import comb
import numpy as np


def fixed_late_window(points, start, stop):
    """Stable S5 value and true physical-s derivative, clipped outside."""
    if not start < stop:
        raise ValueError('Use a positive fixed transition width')
    t=np.clip((np.asarray(points,float)-start)/(stop-start),0.,1.)
    u=np.minimum(t,1-t)
    small=u*u*u*(10+u*(-15+6*u))
    chi=np.where(t<=.5,small,1-small)
    chis=30*t*t*(1-t)*(1-t)/(stop-start)
    return chi,chis


def _positive_kappa_yy_parameters(tail, y):
    """True second-y curvature basis for the declared positive Bernstein tail."""
    y=np.asarray(y,float)
    raw=(np.abs(y)-tail.flat_radius)/tail.width
    q=np.clip(raw,0.,1.);inside=(raw>0)&(raw<1)
    degree=tail.parameter_count-1
    rows=[]
    for j in range(degree+1):
        A,B=j+4,degree-j+4
        second=(A*(A-1)*q**(A-2)*(1-q)**B
            -2*A*B*q**(A-1)*(1-q)**(B-1)
            +B*(B-1)*q**A*(1-q)**(B-2))
        rows.append(np.where(inside,630*comb(degree,j)*second/tail.width**3,0.))
    return np.stack(rows,axis=-1)


def cut_material_tail_packet(tail, coords, *, cut_radius=.8):
    """Whole cut II and full angular two-jets, including all tail columns.

    U and its coordinate jets are fixed with respect to profile/tail
    parameters.  Physical cut radius is fixed.  Thus this packet has no
    physical-profile parameter dependence.  Optional U_sxi enables the
    mixed jet.  R132 positive Bernstein is the explicit family here.
    """
    from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
    if not isinstance(tail,PositiveFlatDevelopableFamily):
        raise TypeError('Declare the exact R132 positive Bernstein family')
    if not np.isfinite(cut_radius) or cut_radius<=0:
        raise ValueError('Positive fixed physical cut radius required')
    U,Us,Uxi=np.broadcast_arrays(*(np.asarray(coords[k],float) for k in ('u','u_s','u_xi')))
    Uxixi=np.broadcast_to(np.asarray(coords['u_xixi'],float),U.shape)
    if U.ndim!=2 or any(not np.all(np.isfinite(x)) for x in (U,Us,Uxi,Uxixi)):
        raise ValueError('Expected finite (angles,radial-points) coordinate jets')
    sn,cs=np.sin(U),np.cos(U)
    y=cut_radius*sn;yu=cut_radius*cs;yuu=-cut_radius*sn
    curve=tail.angle_jets(y)
    kp,kyp=(np.asarray(curve[k],float) for k in ('kappa_jacobian','kappa_y_jacobian'))
    kyyp=_positive_kappa_yy_parameters(tail,y)
    kup=kyp*yu[...,None]
    kuup=kyyp*(yu*yu)[...,None]+kyp*yuu[...,None]
    B=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
    Bu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
    Buu=np.stack((-2*np.cos(2*U),2*np.sin(2*U),2*np.cos(2*U)),axis=-1)
    Vp=B[...,None]*kp[...,None,:]
    Vup=B[...,None]*kup[...,None,:]+Bu[...,None]*kp[...,None,:]
    Vuup=B[...,None]*kuup[...,None,:]+2*Bu[...,None]*kup[...,None,:]+Buu[...,None]*kp[...,None,:]
    packets=dict(parameters=Vp,x_parameters=Us[...,None,None]*Vup,
        xi_parameters=Uxi[...,None,None]*Vup,
        xixi_parameters=(Uxi*Uxi)[...,None,None]*Vuup+Uxixi[...,None,None]*Vup)
    if 'u_sxi' in coords:
        Usxi=np.broadcast_to(np.asarray(coords['u_sxi'],float),U.shape)
        packets['x_xi_parameters']=(Us*Uxi)[...,None,None]*Vuup+Usxi[...,None,None]*Vup
    names=dict(parameters='values',x_parameters='x',xi_parameters='xi',
               xixi_parameters='xixi',x_xi_parameters='x_xi')
    out=dict(packets)
    for key,value in packets.items():
        out[names[key]]=value@np.asarray(tail.coefficients,float)
    if any(not np.all(np.isfinite(v)) for v in out.values()):
        raise FloatingPointError('Nonfinite exact cut-material lifting jet')
    out.update(cut_radius=float(cut_radius),tail_parameter_count=tail.parameter_count,
        material_definition='kappa(cut_radius*sin(u))*B(u), fixed in physical material u',
        physical_profile_dependence=False,parameter_linear=True)
    return out


def full_lifting_forcing(values, radial, angular, operators):
    """Actual Codazzi forcing before angular projection; arbitrary extra axes."""
    values,radial,angular=(np.asarray(x,float) for x in (values,radial,angular))
    if values.shape!=radial.shape or values.shape!=angular.shape or values.shape[2]!=3:
        raise ValueError('Expected matching (angles,points,3,...) packets')
    extra=(1,)*(values.ndim-3)
    shape=values.shape[:2]+extra
    inv=np.asarray(operators['inv'],float).reshape(shape)
    adv=np.asarray(operators['adv'],float).reshape(shape)
    c=np.asarray(operators['jet']['c'],float).reshape((1,values.shape[1])+extra)
    fn=inv*angular[:,:,1]+c*(values[:,:,2]-values[:,:,0])+adv*angular[:,:,0]-radial[:,:,0]
    fm=inv*angular[:,:,2]-2*c*values[:,:,1]+adv*angular[:,:,1]-radial[:,:,1]
    return np.stack((fn,fm),axis=2)


def blend_cut_material_lifting(old, cut, weight, weight_s, *, operators=None,
                                project_even=None, project_odd=None):
    """Replace the complete lifting; no field coefficients are projected.

    Tail jets remain linear in the unchanged tail controls.  The cut
    reference has no delta dependence.  If operators are supplied, forcing
    is freshly computed; optional projectors return the solver's existing
    retained forcing arrays.  Without them stale old forcing is removed.
    """
    values=np.asarray(old['values'],float)
    if values.ndim!=3 or values.shape[-1]!=3 or np.shape(cut['values'])!=values.shape:
        raise ValueError('Expected matching complete lifting packets')
    N=values.shape[1]
    w=np.broadcast_to(np.asarray(weight,float),(N,))
    ws=np.broadcast_to(np.asarray(weight_s,float),(N,))
    if not np.all(np.isfinite(w)) or not np.all(np.isfinite(ws)) or np.any(w<0) or np.any(w>1):
        raise ValueError('Use a fixed physical-s window in [0,1] and its actual derivative')
    W=w[None,:,None];Ws=ws[None,:,None]
    P=W[...,None];Ps=Ws[...,None]
    out=dict(old)
    out['values']=(1-W)*values+W*cut['values']
    out['x']=(1-W)*old['x']+W*cut['x']+Ws*(cut['values']-values)
    out['xi']=(1-W)*old['xi']+W*cut['xi']
    out['parameters']=(1-P)*old['parameters']+P*cut['parameters']
    out['x_parameters']=(1-P)*old['x_parameters']+P*cut['x_parameters']+Ps*(cut['parameters']-old['parameters'])
    out['xi_parameters']=(1-P)*old['xi_parameters']+P*cut['xi_parameters']
    for plain,param in (('xixi','xixi_parameters'),('x_xi','x_xi_parameters')):
        if plain in old:
            out[plain]=(1-W)*old[plain]+W*cut[plain]
            if plain=='x_xi':out[plain]+=Ws*(cut['xi']-old['xi'])
        if param in old:
            out[param]=(1-P)*old[param]+P*cut[param]
            if param=='x_xi_parameters':out[param]+=Ps*(cut['xi_parameters']-old['xi_parameters'])
    profile=np.asarray(old['profile_parameters'],float)
    out['profile_parameters']=(1-P)*profile
    out['profile_x_parameters']=(1-P)*old['profile_x_parameters']-Ps*profile
    out['profile_s_parameters']=out['profile_x_parameters']
    out['profile_xi_parameters']=(1-P)*old['profile_xi_parameters']
    for name in ('profile_xixi_parameters','profile_x_xi_parameters'):
        if name in old:
            out[name]=(1-P)*old[name]
            if name=='profile_x_xi_parameters':out[name]-=Ps*old['profile_xi_parameters']
    for name in ('forcing','forcing_parameters','forcing_full','forcing_parameters_full'):
        out.pop(name,None)
    if operators is not None:
        out['forcing_full']=full_lifting_forcing(out['values'],out['x'],out['xi'],operators)
        out['forcing_parameters_full']=full_lifting_forcing(out['parameters'],out['x_parameters'],out['xi_parameters'],operators)
        if (project_even is None)!=(project_odd is None):
            raise ValueError('Supply both existing angular projectors, or neither')
        if project_even is not None:
            def project(packet):
                return np.concatenate((np.einsum('ew,wn...->ne...',project_even,packet[:,:,0]),
                    np.einsum('kw,wn...->nk...',project_odd,packet[:,:,1])),axis=1)
            out['forcing']=project(out['forcing_full'])
            out['forcing_parameters']=project(out['forcing_parameters_full'])
    elif project_even is not None or project_odd is not None:
        raise ValueError('Actual operators are required for projected forcing')
    out['cut_material_lifting_definition']=dict(schema='fd2d-complete-cut-material-tail-lifting-v1',
        cut_radius=cut['cut_radius'],tail_parameter_count=cut['tail_parameter_count'],
        values='(1-chi)*old_complete_lifting+chi*cut_material_rank_one_tail',
        fixed_physical_window=True,angular_coordinate_and_cut_radius_parameter_frozen=True,
        tail_parameters_linear=True,physical_profile_cut_reference_derivative_zero=True,
        old_actual_field_preserved=False,physical_metric_changed=False,
        nonlinear_trace_reapplied_to_complete_field=True,
        exact_cut_value_and_angular_jets_preserved=True,
        exact_cut_radial_II_derivative_preserved=False,
        stale_original_forcing_retained=False,Gauss_Codazzi_solution_claimed=False)
    return out
