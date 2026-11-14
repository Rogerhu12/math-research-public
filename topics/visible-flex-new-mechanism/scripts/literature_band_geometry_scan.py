#!/usr/bin/env python3
"""Bounded public design scan of the exact closed ruled-band seeds.

The symmetric branch has c=1/b, eta=1-1/(2*b*b)>0.  The exact reflection
and rotation identities close its two periods.  This is a geometry design
experiment, not fixed-metric refinement, a flexible closed surface, or a
continuous reach certificate.  Run research computations in public Actions.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np

import literature_band_seed as seed


def fields(parameters, n, amplitude=None):
    d = seed.spherical_data(parameters.q, parameters.a, parameters.kind, parameters.b, n)
    v, vp = seed.speed_data(parameters, d, amplitude)
    derivative = v[:, None] * d['raw']
    alpha = seed.periodic_primitive(derivative)
    N = d['B_theta'] / d['sphere_speed'][:, None]
    T = -np.cross(d['B'], N)
    omega_rhs = d['kappa_theta'] / (2 * np.sqrt(v))
    omega = seed.periodic_primitive(omega_rhs[:, None])[:, 0]
    return dict(data=d, v=v, vp=vp, alpha=alpha, N=N, T=T, omega=omega,
                closure=2*np.pi/n*np.sum(derivative, axis=0),
                omega_period=float(2*np.pi/n*np.sum(omega_rhs)))


def local_diagnostic(parameters, n, amplitude, halfwidth):
    f = fields(parameters, n, amplitude)
    d, v, vp = f['data'], f['v'], f['vp']
    band_ends = np.concatenate([f['alpha']-halfwidth*f['N'], f['alpha']+halfwidth*f['N']])
    diameter = seed.sampled_diameter(band_ends)
    kappa_s = d['kappa_theta']/d['sphere_speed']
    v_s = vp/d['sphere_speed']
    maximum = 0.
    for u in np.linspace(-halfwidth, halfwidth, 65):
        w = v-d['kappa']*u
        E = w*w+u*u
        trace = u*(v_s-kappa_s*u)/E**1.5
        principal = (np.abs(trace)+np.sqrt(trace*trace+4*(v/E)**2))/2
        maximum = max(maximum, float(np.max(principal)))
    # One compact characteristic strip contained strictly inside 0<u<halfwidth.
    h, om = np.sqrt(v), f['omega']
    left = max(float(np.max(h/halfwidth-om)), float(-np.min(om)))
    left += max(abs(left), 1.)*.1
    right = left+max(abs(left), 1.)
    u_outer, u_inner = h/(left+om), h/(right+om)
    return dict(theta_n=n, width_samples=65, halfwidth=halfwidth,
                closure_norm=float(np.linalg.norm(f['closure'])),
                omega_period=f['omega_period'],
                speed_min=float(np.min(v)), speed_max=float(np.max(v)),
                speed_contrast=float(np.max(v)/np.min(v)),
                sampled_band_diameter=diameter,
                sampled_max_abs_principal_curvature=maximum,
                local_principal_radius_over_sampled_band_D=1/(maximum*diameter),
                characteristic_strip=dict(left=left, right=right,
                    min_physical_width_over_sampled_band_D=float(np.min(u_outer-u_inner))/diameter,
                    max_physical_width_over_sampled_band_D=float(np.max(u_outer-u_inner))/diameter,
                    max_outer_u_over_halfwidth=float(np.max(u_outer))/halfwidth))


def normal_chord_screen(parameters, amplitude, halfwidth, theta_n=512, width_n=13):
    f=fields(parameters, theta_n, amplitude)
    u=np.linspace(-halfwidth,halfwidth,width_n)
    w=f['v'][:,None]-f['data']['kappa'][:,None]*u[None,:]
    E=w*w+u[None,:]**2
    points=(f['alpha'][:,None,:]+u[None,:,None]*f['N'][:,None,:]).reshape(-1,3)
    normals=((u[None,:,None]*f['T'][:,None,:]+w[:,:,None]*f['data']['B'][:,None,:])
             /np.sqrt(E)[:,:,None]).reshape(-1,3)
    squared=np.sum(points*points,axis=1)
    diameter=seed.sampled_diameter(points)
    best=float('inf'); best_pair=None
    for start in range(0,len(points),128):
        end=min(start+128,len(points))
        distance2=squared[start:end,None]+squared[None,:]-2*points[start:end]@points.T
        normal_dot=normals[start:end]@points.T-np.sum(normals[start:end]*points[start:end],axis=1)[:,None]
        mask=np.abs(normal_dot)>1e-13*diameter
        mask[np.arange(end-start),np.arange(start,end)]=False
        ratio=np.full_like(distance2,np.inf)
        np.divide(np.maximum(distance2,0),2*np.abs(normal_dot),out=ratio,where=mask)
        flat=int(np.argmin(ratio));row,col=np.unravel_index(flat,ratio.shape)
        if ratio[row,col]<best:
            best=float(ratio[row,col]);best_pair=[int(start+row),int(col)]
    return dict(theta_n=theta_n,width_n=width_n,sampled_band_diameter=diameter,
                normal_ball_ratio_sample_min=best,
                normal_ball_ratio_sample_min_over_sampled_D=best/diameter,
                pair_indices=best_pair,
                status='Finite necessary-scale screen only; no lower reach bound or embedding certificate')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--top',type=int,default=4)
    args=ap.parse_args()
    if not 1<=args.top<=6:ap.error('Bound detailed checks to 1..6 candidates')
    rows=[]
    choices=[('symmetric',q,a,b) for q,a,b in itertools.product([2,3,4],[.2,.35,.5],[1.1,1.3,1.5])]
    choices.append(('curvature',3,1/3,.85))
    for kind,q,a,b in choices:
        p=SimpleNamespace(kind=kind,q=q,a=a,b=b,c=1/b,power=1.,center=-3.,sigma=1.5,reference_n=32768)
        amplitude,_=seed.closing_amplitude(p)
        reference=fields(p,8192,amplitude)
        reference_D=seed.sampled_diameter(reference['alpha'][::4])
        for width in [.03,.06,.12]:
            halfwidth=width*reference_D
            diagnostic=local_diagnostic(p,1024,amplitude,halfwidth)
            row=dict(parameters=vars(p),amplitude=amplitude,
                     reference_centerline_sampled_D=reference_D,
                     fixed_physical_halfwidth=halfwidth,width_over_reference_D=width,
                     coarse=diagnostic)
            row['design_score']=min(diagnostic['local_principal_radius_over_sampled_band_D'],
                diagnostic['characteristic_strip']['min_physical_width_over_sampled_band_D'])
            rows.append(row)
        print(json.dumps({'kind':kind,'q':q,'a':a,'b':b,'cases_completed':len(rows)}),flush=True)
    chosen=sorted(range(len(rows)),key=lambda i:rows[i]['design_score'],reverse=True)[:args.top]
    for index in chosen:
        row=rows[index];p=SimpleNamespace(**row['parameters'])
        row['dense_same_geometry']=local_diagnostic(p,4096,row['amplitude'],row['fixed_physical_halfwidth'])
        row['normal_chord_screen']=normal_chord_screen(p,row['amplitude'],row['fixed_physical_halfwidth'])
    result=dict(schema='public-band-geometry-design-scan-v1',
        source='https://arxiv.org/html/2611.17269v1',
        status='Bounded geometry design scan; no finite flex or closed surface',
        formula='symmetric: c=1/b and eta=1-1/(2b^2)>0; exact analytic period closures are preserved',
        exact_target_metric_for_a_flex=False, fixed_metric_refinement_demonstrated=False,
        score_definition='minimum of sampled local principal-radius ratio and minimum characteristic-strip width ratio',
        selected_indices=chosen,rows=rows,
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        task_complete=False,
        caveats=['All widths and seed parameters label distinct geometry designs.',
                 'Normal-ball pair minima and curvature samples give necessary screens, not certified reach lower bounds.',
                 'The curve primitive removes explicitly reported closure quadrature defects.',
                 'No continuous isometric path, closed cap, fixed hold, or amplitude claim is made.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'cases':len(rows),'selected_indices':chosen}),flush=True)


if __name__=='__main__':main()
