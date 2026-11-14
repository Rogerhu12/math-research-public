#!/usr/bin/env python3
"""Cheap exact-geometry and differentiation checks; no nonlinear solve.

The spectral table concerns the finite trial space, not truncation of the exact
ellipse inlet (which is evaluated analytically in core_to_tail_bvp.py).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from core_to_tail_bvp import Problem, ellipse_inlet, ellipse_phase, fourier, warm_angular_basis


def settings(basis, major=1., minor=.3):
    return SimpleNamespace(radial_free=3, modes=4, angular_basis=basis, design_metric=True,
        core_profile='ellipse', ellipse_major=major, ellipse_minor=minor, inlet_angles=128,
        inlet_s=.23, quadrature=48, background='unit', length=1., cut_radius=.28,
        flat_start=.26, cuff_radius=.23, beta_wiggle=.8, tail_height=None,
        tail_plus=.04, tail_minus=-.03, radius_floor=.24, radius_ceiling=.95,
        radius_weight=20.)


def maxnorm(x):
    return float(np.max(np.linalg.norm(x, axis=-1)))


def truncate(x, modes):
    c=np.fft.rfft(x, axis=0)
    c[modes+1:]=0
    return np.fft.irfft(c, n=len(x), axis=0)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--spectral-points',type=int,default=4096)
    args=parser.parse_args()
    rng=np.random.default_rng(74103)
    result={'status':'cheap_development_checks_no_optimization','task_complete':False,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'solver_sha256':hashlib.sha256(Path(__file__).with_name('core_to_tail_bvp.py').read_bytes()).hexdigest(),
            'checks':{}}
    theta=(np.arange(83)+.317)*2*np.pi/83
    material=Problem(settings('material'))
    ellipse=Problem(settings('ellipse'))
    default_args=settings('material')
    del default_args.angular_basis
    default=Problem(default_args)
    grid=ellipse.prepare(np.linspace(0,1,13),64)
    material_grid=material.prepare(grid['u'],64)
    default_grid=default.prepare(grid['u'],64)
    result['checks']['default_material_basis_max_error']=max(
        float(np.max(np.abs(x-y))) for x,y in zip(default_grid['f'],material_grid['f']))
    result['checks']['material_basis_formula_max_error']=max(
        float(np.max(np.abs(material_grid['f'][d]-fourier(grid['theta'],4,d)))) for d in range(3))

    def basis_jet(th,d):
        ph,pp,ppp,_,_=ellipse_phase(th,1.,.3)
        f0,f1,f2=[fourier(ph,4,k) for k in range(3)]
        return (f0,f1*pp[:,None],f2*pp[:,None]**2+f1*ppp[:,None])[d]

    h=3e-5
    diffs=[]
    for d in (0,1):
        fd=(basis_jet(theta-2*h,d)-8*basis_jet(theta-h,d)+
            8*basis_jet(theta+h,d)-basis_jet(theta+2*h,d))/(12*h)
        exact=basis_jet(theta,d+1)
        diffs.append({'derivative':d+1,'absolute_error':float(np.max(np.abs(fd-exact))),
                      'relative_l2_error':float(np.linalg.norm(fd-exact)/np.linalg.norm(exact))})
    result['checks']['ellipse_basis_material_derivatives']=diffs
    ph,_,_,_,_=ellipse_phase(theta,1.,.3)
    phplus,_,_,_,_=ellipse_phase(theta+2*np.pi,1.,.3)
    result['checks']['phase_periodicity_error']=float(np.max(np.abs(phplus-ph-2*np.pi)))

    circle_radius=ellipse.a0
    circle_e=Problem(settings('ellipse',circle_radius,circle_radius))
    circle_m=Problem(settings('material',circle_radius,circle_radius))
    ge=circle_e.prepare(np.linspace(0,1,13),64)
    gm=circle_m.prepare(ge['u'],64)
    result['checks']['circle_basis_max_error']=max(
        float(np.max(np.abs(x-y))) for x,y in zip(ge['f'],gm['f']))
    circle_seed=circle_e.seed()
    circle_seed[-4:-2]=0
    result['checks']['round_reference_metric_error']=circle_e.audit(circle_seed,41,128)['relative_metric_operator_sample_max']

    z=ellipse.seed()
    z[:ellipse.np]=rng.normal(size=ellipse.np)*.002
    z[ellipse.np:ellipse.np+ellipse.na]=rng.normal(size=ellipse.na)*.002
    geom=ellipse.geometry(z,grid,True)
    tail=ellipse.tail(grid['theta'],z[-4:])
    endpoint={}
    for name,rd,td in [('x',0,0),('xs',1,0),('xt',0,1),
                       ('xss',2,0),('xst',1,1),('xtt',0,2)]:
        expected=np.stack((grid['inlet'][td][rd],tail[td][rd]))
        endpoint[name]=float(np.max(np.abs(geom[name][[0,-1]]-expected)))
    result['checks']['endpoint_position_second_jet_errors']=endpoint
    jac=ellipse.jacobian(z,grid)
    jac_checks=[]
    for k in range(3):
        direction=rng.normal(size=ellipse.size)
        direction/=np.linalg.norm(direction)
        eps=2e-6
        num=(ellipse.residual(z+eps*direction,grid)-ellipse.residual(z-eps*direction,grid))/(2*eps)
        den=max(np.linalg.norm(num),1e-30)
        jac_checks.append(float(np.linalg.norm(num-jac@direction)/den))
    result['checks']['jacobian_directional_relative_errors']=jac_checks
    accepted=[]
    rejected=[]
    for old,new in [('material','material'),('ellipse','ellipse'),('material','ellipse'),('ellipse','material')]:
        try:
            warm_angular_basis({'discretization':{'angular_basis':old}},new)
            accepted.append([old,new])
        except ValueError:
            rejected.append([old,new])
    result['checks']['warm_basis_accepted']=accepted
    result['checks']['warm_basis_rejected']=rejected
    result['checks']['legacy_warm_defaults_to_material']=warm_angular_basis({},'material')

    nt=args.spectral_points
    th=np.arange(nt)*2*np.pi/nt
    ph,pp,ppp,a0,err=ellipse_phase(th,1.,.3)
    curve=[ellipse_inlet(th,1.,.3,0.,d)[0][0] for d in range(3)]
    speed=np.sqrt(np.cos(ph)**2+.09*np.sin(ph)**2)
    radius_normal=np.column_stack((-speed**2*np.sin(ph)/a0,
                                  speed**2*np.cos(ph)/(.3*a0),np.zeros_like(ph)))
    Rformula=np.column_stack((-(1.27*np.sin(ph)+.91*np.sin(3*ph))/(4*a0),
                             (3.09*np.cos(ph)+.91*np.cos(3*ph))/(1.2*a0),np.zeros_like(ph)))
    exact_phi=fourier(ph,3)
    phi_coef=np.linalg.lstsq(exact_phi,np.column_stack((curve[0],radius_normal)),rcond=None)[0]
    exact_fit=exact_phi@phi_coef
    result['checks']['phi_mode_three_gamma_and_radius_normal_fit_max_error']=float(
        np.max(np.abs(exact_fit-np.column_stack((curve[0],radius_normal)))))
    result['checks']['radius_normal_one_plus_three_mode_identity_error']=maxnorm(radius_normal-Rformula)
    result['spectral_material_basis']={'points':nt,'major':1.,'minor':.3,'perimeter_radius':a0,
        'arc_length_inversion_error':err,
        'quantity_radius_normal':'rho * inward_planar_normal / a0',
        'exact_inlet_is_not_truncated':True,'rows':[]}
    for m in [6,12,16,24,32,48,64,96,128]:
        row={'modes':m}
        for key,value in zip(('gamma','gamma_theta','gamma_theta_theta','radius_normal'),[*curve,radius_normal]):
            row[key+'_tail_max_vector_norm']=maxnorm(value-truncate(value,m))
        result['spectral_material_basis']['rows'].append(row)
    checks=result['checks']
    success=(checks['default_material_basis_max_error']==0 and
             checks['material_basis_formula_max_error']==0 and
             checks['circle_basis_max_error']<1e-12 and
             checks['round_reference_metric_error']<1e-10 and
             max(endpoint.values())<1e-11 and max(jac_checks)<2e-7 and
             max(x['relative_l2_error'] for x in diffs)<1e-8 and
             len(rejected)==2 and checks['phi_mode_three_gamma_and_radius_normal_fit_max_error']<1e-12)
    result['development_checks_passed']=bool(success)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'checks_passed':success,'checks':checks}))
    if not success:
        raise SystemExit(1)


if __name__=='__main__':
    main()
