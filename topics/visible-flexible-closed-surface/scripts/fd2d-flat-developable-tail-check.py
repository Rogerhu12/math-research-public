#!/usr/bin/env python3
"""Reproduce R128's actual port, checks, and monotone interval h2 bounds."""
from __future__ import annotations
import argparse
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
from fd2d_flat_developable_tail import FlatDevelopableTail


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interval_height(amplitude_numerator, amplitude_denominator, bins):
    # Positive weight in R128 (14) is integrated exactly on each bin.
    # Monotonicity of S and sin on [0,6/5] makes endpoint enclosure valid.
    mp.mp.dps = 80
    mp.iv.dps = 60
    iv = mp.iv
    a, c = iv.mpf(4)/5, iv.mpf(17)/50
    L = a-c
    A = iv.mpf(amplitude_numerator)/amplitude_denominator
    zero = iv.mpf(0)
    weight_primitive, sin_values = [], []
    for j in range(bins+1):
        t = iv.mpf(j)/bins
        s = zero if j == 0 else (iv.mpf(1) if j == bins else
            t**5*(126+t*(-420+t*(540+t*(-315+70*t)))))
        sin_values.append(iv.sin(A*s))
        if j == bins:
            weight_primitive.append(zero)
        else:
            y = c+L*t
            d = a*a-y*y
            weight_primitive.append(d*iv.sqrt(d)/3)
    lo, hi, hlo, hhi = zero, zero, zero, zero
    for j in range(bins):
        w = weight_primitive[j]-weight_primitive[j+1]
        lo += sin_values[j]*w
        hi += sin_values[j+1]*w
        hlo += sin_values[j]*L/bins
        hhi += sin_values[j+1]*L/bins
    lo, hi = 4*lo/(iv.pi*a*a), 4*hi/(iv.pi*a*a)
    lower = lambda x: str(mp.mp.make_mpf(x._mpi_[0]))
    upper = lambda x: str(mp.mp.make_mpf(x._mpi_[1]))
    return dict(amplitude_rational=[amplitude_numerator,amplitude_denominator],
                bins=bins, interval_decimal_digits=60,
                absolute_h2=[lower(lo),upper(hi)],
                maximum_height=[lower(hlo),upper(hhi)],
                method='monotone endpoint interval sums; exact integral of y*sqrt(a^2-y^2); mpmath.iv directed intervals')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    ap.add_argument('--bins',type=int,default=8192)
    args = ap.parse_args()
    started = time.monotonic()
    source = Path(__file__).with_name('fd2d_flat_developable_tail.py')
    report = dict(schema='r128-flat-developable-tail-check-v1',
                  status='finite checks plus separately identified interval height bounds',
                  source_sha256=sha(source),check_sha256=sha(__file__),
                  exact_definition='R128 equations (1)-(16); all listed decimal parameters are their displayed exact rationals',
                  parameters=dict(cuff_radius=.32,flat_radius=.34,cut_radius=.8,plane_height=1.25),
                  amplitudes=[], finite_checks={}, quadrature_refinement=[],target_h2_examples=[])
    r = np.linspace(.32,.8,25)[:,None]
    u = (2*np.pi*np.arange(512)/512)[None,:]
    maxima = {key:0.0 for key in ('metric_relative','gauss','II_from_twojet','frame_orientation',
                                  'fixed_collar_position','fixed_collar_twojet','periodic_twojet')}
    for A in (0.,.01,.25,.5,1.,1.2):
        model = FlatDevelopableTail(amplitude=A)
        coeff = model.real_height_coefficients(32,4096)
        q = model.cut_port(np.array([np.pi/2]))
        report['amplitudes'].append(dict(amplitude=A,
            exact_curvature_max_formula_evaluated=model.exact_curvature_max,
            h_max_quadrature=float(q['H'][0]),height_coefficients=coeff))
        for phase in (0.,.317,np.pi/2):
            out = model.evaluate(r,u,phase=phase)
            e1,e2,N = out['e1'],out['e2'],out['N']
            metric = np.stack((np.sum(e1*e1,axis=-1)-1,
                               np.sum(e1*e2,axis=-1),np.sum(e2*e2,axis=-1)-1),axis=-1)
            maxima['metric_relative']=max(maxima['metric_relative'],float(np.max(np.abs(metric))))
            maxima['gauss']=max(maxima['gauss'],float(np.max(np.abs(out['l']*out['n']-out['m']**2))))
            actualII = np.stack((np.sum(out['X_ss']*N,axis=-1),
                np.sum(out['X_su']*N,axis=-1)/r,np.sum(out['X_uu']*N,axis=-1)/r**2),axis=-1)
            targetII = np.stack((out['l'],out['m'],out['n']),axis=-1)
            maxima['II_from_twojet']=max(maxima['II_from_twojet'],float(np.max(np.abs(actualII-targetII))))
            maxima['frame_orientation']=max(maxima['frame_orientation'],float(np.max(np.abs(np.cross(e1,e2)-N))))
            rc = np.array([.32,.329,.34])[:,None]
            collar = model.evaluate(rc,u,phase=phase)
            plain = FlatDevelopableTail(amplitude=0).evaluate(rc,u)
            maxima['fixed_collar_position']=max(maxima['fixed_collar_position'],float(np.max(np.abs(collar['X']-plain['X']))))
            for key in ('X_s','X_u','X_ss','X_su','X_uu'):
                maxima['fixed_collar_twojet']=max(maxima['fixed_collar_twojet'],float(np.max(np.abs(collar[key]-plain[key]))))
            periodic = model.evaluate(np.linspace(.32,.8,17)[:,None],np.array([0.,2*np.pi])[None,:],phase=phase)
            for key in ('X','X_s','X_u','X_ss','X_su','X_uu'):
                maxima['periodic_twojet']=max(maxima['periodic_twojet'],float(np.max(np.abs(periodic[key][:,0]-periodic[key][:,1]))))
    report['finite_checks']=dict(maxima,radial_points=25,angular_points=512,
                                phases=[0.,.317,float(np.pi/2)],scope='finite implementation diagnostics; exact claims are proved in R128')
    for A in (1.,1.2):
        baseline = FlatDevelopableTail(amplitude=A,quadrature_order=160).cut_port(2*np.pi*np.arange(8192)/8192)
        h2_ref = float(2*np.mean(baseline['H']*np.cos(2*(2*np.pi*np.arange(8192)/8192))))
        for order in (32,64,96,128):
            model = FlatDevelopableTail(amplitude=A,quadrature_order=order)
            q = model.cut_port(2*np.pi*np.arange(8192)/8192)
            report['quadrature_refinement'].append(dict(amplitude=A,order=order,
                reference_order=160,max_position_difference=float(np.max(np.abs(q['X']-baseline['X']))),
                h2=float(2*np.mean(q['H']*np.cos(2*(2*np.pi*np.arange(8192)/8192)))),
                h2_difference=float(abs(float(2*np.mean(q['H']*np.cos(2*(2*np.pi*np.arange(8192)/8192))))-h2_ref))))
    rj = np.linspace(.45,.8,13)
    uj = np.linspace(.11,2.9,13)
    core = FlatDevelopableTail(amplitude=.8)
    jvp = core.amplitude_jvp(rj,uj,phase=.2)
    report['parameter_jvp_checks']=[]
    for eps in (1e-3,5e-4,2.5e-4):
        plus=replace(core,amplitude=core.amplitude+eps).evaluate(rj,uj,phase=.2)
        minus=replace(core,amplitude=core.amplitude-eps).evaluate(rj,uj,phase=.2)
        errors={key:float(np.max(np.abs((plus[key]-minus[key])/(2*eps)-jvp[key])))
                for key in ('X','X_s','X_u','X_ss','X_su','X_uu','gc_values')}
        report['parameter_jvp_checks'].append(dict(step=eps,max_errors=errors))
    angular = 2*np.pi*np.arange(4096)/4096
    for height in (.005,.02,.05,.1):
        def residual(A):
            H=FlatDevelopableTail(amplitude=A,quadrature_order=64).cut_port(angular)['H']
            return float(-2*np.mean(H*np.cos(2*angular)))-height
        A=brentq(residual,0.,1.2,xtol=1e-13)
        model=FlatDevelopableTail(amplitude=A)
        coeff=model.real_height_coefficients(16,8192)
        report['target_h2_examples'].append(dict(requested_negative_h2=-height,
            numerical_amplitude=A,actual_height_coefficients=coeff,
            curvature_max=model.exact_curvature_max,
            scope='numerical amplitude root; other boundary modes and complete jets are those of the exact family, not arbitrary Dirichlet data'))
    report['interval_height']=[interval_height(1,1,args.bins),interval_height(6,5,args.bins)]
    report['analytic_all_amplitude_bounds']=dict(amplitude_range=[0.,1.2],
        curvature_max_rational=[4725,736],outward_support_min_rational=[7,20],
        z_min_rational=[487,500],z_max_rational=[5,4],ball_radius_squared_max_rational=[881,400],
        slab_phase_zero=.8,whole_closed_surface_reach='conditional on remaining true closed core satisfying R10; not inferred from this tail alone')
    report['elapsed_seconds']=time.monotonic()-started
    report['body_completed']=True
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(output=args.output,elapsed_seconds=report['elapsed_seconds'],
        finite_checks=report['finite_checks'],interval_height=report['interval_height'],
        target_h2_examples=[dict(h2=x['requested_negative_h2'],A=x['numerical_amplitude'],kappa=x['curvature_max'])
                            for x in report['target_h2_examples']]),indent=2))


if __name__=='__main__':
    main()
