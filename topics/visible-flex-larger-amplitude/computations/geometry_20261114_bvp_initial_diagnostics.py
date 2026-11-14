#!/usr/bin/env python3
"""Reproduce the short-end BVP initialization and principal phase diagnostics.

This does not solve a BVP. Curvature and metric readouts are sampled finite
field values. The oscillator phase comparison is an axisymmetric principal
model, not a theorem about the nonaxisymmetric full BVP conditioning.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import numpy as np

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('initial_diagnostic_driver',P/'geometry_20261114_r225_free_core_bvp.py')
driver=importlib.util.module_from_spec(spec);spec.loader.exec_module(driver)


def geometry(q,s,y):
    frame=q.frame(s,y)
    yp,ypp=driver.finite_second_derivative(q,s,y)
    velocity,mixed,unused=q.jet(yp)
    acceleration=q.jet(ypp)[0]
    normal=np.cross(velocity,frame['d'])
    normal/=np.linalg.norm(normal,axis=1)[:,None]
    E=np.sum(velocity**2,axis=1);F=np.sum(velocity*frame['d'],axis=1);G=np.sum(frame['d']**2,axis=1)
    e=np.sum(acceleration*normal,axis=1);f=np.sum(mixed*normal,axis=1);g=np.sum(frame['dd']*normal,axis=1)
    gauss=(e*g-f*f)/(E*G-F*F)
    row=q.stats(s,y)
    return dict(s=float(s),a=frame['a'],ap=frame['ap'],app=frame['app'],
                gauss_min=float(gauss.min()),gauss_max=float(gauss.max()),
                det_II_min=float((e*g-f*f).min()),II_phi_phi_min=float(g.min()),
                metric_sample=row['metric_sample'],kappa_sample=row['surface_kappa_sample'],
                point_domain_min=float(frame['margin'].min()))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seed',type=Path,required=True)
    ap.add_argument('--profile',type=Path,required=True)
    ap.add_argument('--far-profile',type=Path,required=True)
    ap.add_argument('--prepared',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    seed=driver.fixed.read(args.seed);profile=driver.fixed.read(args.profile)
    far=driver.fixed.read(args.far_profile)
    law=seed['metric_identity']['law'];M=seed['numerical_parameters']['M'];N=seed['numerical_parameters']['N']
    c=np.array([float(Fraction(v))for v in seed['metric_identity']['coefficients_rational']])
    q=driver.native.outward.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    scalar=driver.fixed.FixedProfile(profile['geometry']);q.profile=scalar.profile;driver.fixed.fft.enable_fft(q)
    s0=float(seed['state_locations'][-1]);y0=np.array(seed['coefficient_states'][-1])
    yp,ypp=driver.finite_second_derivative(q,s0,y0)
    rows=[dict(kind='actual_native_seed',**geometry(q,s0,y0))]
    for ds in (.0002,.00025,.0005):
        for order in (1,2):
            yy=y0+ds*yp+(.5*ds*ds*ypp if order==2 else 0)
            rows.append(dict(kind='Taylor_predictor',order=order,delta=ds,**geometry(q,s0+ds,yy)))
    q.profile=driver.fixed.FixedProfile(far['geometry']).profile
    s1=1.0005;a0=q.profile(s0)[0];a1,v1,unused=q.profile(s1)
    homothetic=y0.copy();index=2*M+1;mean=homothetic[index];homothetic[index]=0
    homothetic*=a1/a0;homothetic[index]=mean+(s1-s0)*np.sqrt(1-v1*v1)
    rows.append(dict(kind='old_homothetic_predictor',**geometry(q,s1,homothetic)))
    phase=[];omega=2*M*np.sqrt(law['k0'])
    for step in (.025,.005):
        z=1j*omega*step
        stability=(1+z/2+z*z/12)/(1-z/2+z*z/12)
        numerical=float(np.angle(stability));exact=float(omega*step)
        phase.append(dict(M=M,k0=law['k0'],omega=float(omega),step=step,exact_phase=exact,
                          collocation_phase=numerical,phase_error_per_step=numerical-exact,
                          modulus=float(abs(stability))))
    prepared=driver.fixed.read(args.prepared)if args.prepared else None
    keys=('M','N','end','initial_boundary_max','initial_collocation_max','metric_sample',
          'kappa_sample','point_domain_min','maximum_RSS_kib','source_sha256','assembly_source_sha256',
          'seed_sha256','profile_sha256')
    report=dict(scope=__doc__,rows=rows,axis_principal_phase=phase,
                prepared={k:prepared[k]for k in keys}if prepared else None,
                prepared_nodes=len(prepared['mesh'])if prepared else None,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                driver_sha256=hashlib.sha256((P/'geometry_20261114_r225_free_core_bvp.py').read_bytes()).hexdigest(),
                inputs={name:dict(path=str(getattr(args,name)),sha256=hashlib.sha256(getattr(args,name).read_bytes()).hexdigest())
                        for name in ('seed','profile','far_profile')})
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),rows=len(rows),prepared_nodes=report['prepared_nodes'])))


if __name__=='__main__':
    main()
