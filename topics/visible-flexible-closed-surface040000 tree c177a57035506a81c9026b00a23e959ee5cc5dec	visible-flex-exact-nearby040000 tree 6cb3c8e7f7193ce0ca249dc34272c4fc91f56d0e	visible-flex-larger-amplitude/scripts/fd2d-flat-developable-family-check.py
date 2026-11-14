#!/usr/bin/env python3
"""Actual frozen-interface/JVP check for the multi-parameter R128 family."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_flat_developable_family import FlatDevelopableFamily,angle_basis
from fd2d_flat_developable_tail import FlatDevelopableTail


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def maxabs(a):
    return float(np.max(np.abs(a)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    start=time.monotonic()
    folder=Path(__file__).resolve().parent
    report=dict(schema='r128-flat-developable-family-check-v1',
        source_sha256=sha(folder/'fd2d_flat_developable_family.py'),
        single_parameter_source_sha256=sha(folder/'fd2d_flat_developable_tail.py'),
        check_sha256=sha(__file__),coefficient_convention='[A,b0,...,b(K-1)], last Jacobian axis in the same order')
    K=47
    coeff=np.r_[.8, .003*(-1.)**np.arange(K)/(np.arange(K)+1.)**4]
    family=FlatDevelopableFamily(coeff)
    report['actual_coefficients']=coeff.tolist()
    report['sufficient_bounds']=family.sufficient_bounds()
    # Independent Clenshaw evaluation plus library Chebyshev differentiation.
    q=np.linspace(.0001,.9999,257)
    val,d1,d2=angle_basis(q,K)
    b=coeff[1:]
    cheb=np.polynomial.chebyshev
    f=cheb.chebval(2*q-1,b)
    f1=2*cheb.chebval(2*q-1,cheb.chebder(b))
    f2=4*cheb.chebval(2*q-1,cheb.chebder(b,2))
    p=1024*q**5*(1-q)**5
    p1=5120*q**4*(1-q)**4*(1-2*q)
    p2=5120*(4*q**3*(1-q)**3*(1-2*q)**2-2*q**4*(1-q)**4)
    report['independent_chebyshev_check']=dict(value=maxabs(val[:,1:]@b-p*f),
        first=maxabs(d1[:,1:]@b-p1*f-p*f1),second=maxabs(d2[:,1:]@b-p2*f-2*p1*f1-p*f2))
    # Original frozen one-parameter provider is a separate implementation.
    us=np.linspace(.13,6.1,257)
    old=FlatDevelopableTail(amplitude=1.).cut_port(us,phase=.17)
    new=FlatDevelopableFamily(np.r_[1.,np.zeros(K)]).cut_port(us,phase=.17)
    keys=('X','X_r','X_u','X_rr','X_ru','X_uu','X_s','X_ss','X_su','e1','e2','N','l','m','n','gc_values')
    report['zero_bubbles_vs_frozen_single_parameter']={key:maxabs(new[key]-old[key]) for key in keys}
    oldj=FlatDevelopableTail(amplitude=1.).amplitude_jvp(.8,us,phase=.17)
    report['first_parameter_jacobian_vs_frozen_single_parameter']={key:maxabs(new[key+'_jacobian'][...,0]-oldj[key]) for key in keys}
    # Entire l,m,n field: direct physical Codazzi and all parameter columns.
    r=np.linspace(.32,.8,19)[:,None]
    u=(2*np.pi*np.arange(256)/256)[None,:]
    out=family.evaluate(r,u,position_jets=False)
    c=-1/r
    Rm=out['m_s']-out['l_u']/r+2*c*out['m']
    Rn=out['n_s']-out['m_u']/r-c*(out['l']-out['n'])
    RmJ=out['m_s_jacobian']-out['l_u_jacobian']/r[...,None]+2*c[...,None]*out['m_jacobian']
    RnJ=out['n_s_jacobian']-out['m_u_jacobian']/r[...,None]-c[...,None]*(out['l_jacobian']-out['n_jacobian'])
    G=out['l']*out['n']-out['m']**2
    GJ=out['l_jacobian']*out['n'][...,None]+out['l'][...,None]*out['n_jacobian']-2*out['m'][...,None]*out['m_jacobian']
    report['physical_GC_checks']=dict(radial_points=19,angular_points=256,
        Rm=maxabs(Rm),Rn=maxabs(Rn),Gauss=maxabs(G),
        all_columns_Rm=maxabs(RmJ),all_columns_Rn=maxabs(RnJ),all_columns_Gauss=maxabs(GJ))
    rsmall=np.linspace(.41,.8,17)
    usmall=np.linspace(.17,2.95,17)
    full=family.evaluate(rsmall,usmall,phase=.27)
    metric=np.stack((np.sum(full['e1']**2,axis=-1)-1,
        np.sum(full['e1']*full['e2'],axis=-1),np.sum(full['e2']**2,axis=-1)-1),axis=-1)
    actual=np.stack((np.sum(full['X_ss']*full['N'],axis=-1),
        np.sum(full['X_su']*full['N'],axis=-1)/rsmall,
        np.sum(full['X_uu']*full['N'],axis=-1)/rsmall**2),axis=-1)
    report['actual_twojet_checks']=dict(metric=maxabs(metric),
        second_form=maxabs(actual-np.stack((full['l'],full['m'],full['n']),axis=-1)))
    collar=family.evaluate(np.array([.32,.33,.34])[:,None],us[None,:],phase=.72)
    plain=FlatDevelopableTail(amplitude=0.).evaluate(np.array([.32,.33,.34])[:,None],us[None,:])
    report['fixed_collar']={key:maxabs(collar[key]-plain[key]) for key in ('X','X_s','X_u','X_ss','X_su','X_uu')}
    report['fixed_collar_parameter_jacobians']={key:maxabs(collar[key+'_jacobian']) for key in ('X','X_s','X_u','X_ss','X_su','X_uu')}
    report['directional_parameter_checks']=[]
    direction=np.cos(np.arange(K+1)*.37)/(1+np.arange(K+1))
    direction/=np.linalg.norm(direction)
    exact=family.jvp(rsmall,usmall,direction,phase=.27)
    for eps in (1e-3,5e-4,2.5e-4):
        plus=FlatDevelopableFamily(coeff+eps*direction).evaluate(rsmall,usmall,phase=.27)
        minus=FlatDevelopableFamily(coeff-eps*direction).evaluate(rsmall,usmall,phase=.27)
        errors={key:maxabs((plus[key]-minus[key])/(2*eps)-exact[key]) for key in keys}
        errors['kappa_y']=maxabs((plus['kappa_y']-minus['kappa_y'])/(2*eps)-exact['kappa_y'])
        errors['height_jet']=max(maxabs((plus['height_jet'][key]-minus['height_jet'][key])/(2*eps)-exact['height_jet'][key]) for key in exact['height_jet'])
        report['directional_parameter_checks'].append(dict(step=eps,max_errors=errors))
    report['kappa_y_spatial_derivative_check']=[]
    ys=np.r_[np.linspace(-.77,-.38,19),np.linspace(.38,.77,19)]
    analytic=family.angle_jets(ys)
    for eps in (1e-4,5e-5,2.5e-5):
        plus=family.angle_jets(ys+eps)
        minus=family.angle_jets(ys-eps)
        report['kappa_y_spatial_derivative_check'].append(dict(step=eps,
            kappa_y=maxabs((plus['kappa']-minus['kappa'])/(2*eps)-analytic['kappa_y']),
            kappa_y_jacobian=maxabs((plus['kappa_jacobian']-minus['kappa_jacobian'])/(2*eps)-analytic['kappa_y_jacobian'])))
    # Projection can fail or kappa can change sign without affecting g: the API
    # reports that condition separately instead of clipping the coefficients.
    nc=FlatDevelopableFamily([.5,.2])
    nonconvex=nc.evaluate(rsmall,usmall)
    report['nonconvex_case']=dict(coefficients=[.5,.2],bounds=nc.sufficient_bounds(),
        sampled_kappa_min=float(np.min(nc.angle_jets(np.linspace(.34,.8,1025))['kappa'])),
        sampled_kappa_max=float(np.max(nc.angle_jets(np.linspace(.34,.8,1025))['kappa'])),
        metric=max(maxabs(np.sum(nonconvex['e1']**2,axis=-1)-1),maxabs(np.sum(nonconvex['e2']**2,axis=-1)-1)))
    # Quadrature refinement includes every position Jacobian column.
    reference=FlatDevelopableFamily(coeff,quadrature_order=192).curve(ys)
    report['quadrature_refinement']=[]
    for order in (48,64,96,128):
        item=FlatDevelopableFamily(coeff,quadrature_order=order).curve(ys)
        report['quadrature_refinement'].append(dict(order=order,reference_order=192,
            errors={key:maxabs(item[key]-reference[key]) for key in ('X','Z','X_jacobian','Z_jacobian')}))
    times=[]
    ub=2*np.pi*np.arange(128)/128
    for _ in range(20):
        t=time.perf_counter()
        family.cut_port(ub,position_jets=False)
        times.append(time.perf_counter()-t)
    report['shape_only_boundary_timing']=dict(points=128,parameters=48,repeats=20,
        median_seconds=float(np.median(times)),maximum_seconds=max(times),persistent_point_cache=False)
    report['max_rss_KiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['elapsed_seconds']=time.monotonic()-start
    report['scope']='Actual finite implementation/derivative checks; exact common g and collar follow from R128 and the displayed analytic basis. No new prefix BVP or completed surface is asserted.'
    report['body_completed']=True
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('source_sha256','physical_GC_checks','actual_twojet_checks','sufficient_bounds','shape_only_boundary_timing','max_rss_KiB','elapsed_seconds')},indent=2))


if __name__=='__main__':
    main()
