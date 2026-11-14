#!/usr/bin/env python3
"""Actual finite m2 linear trajectory and relative second-form amplification.

The invariant q=a'*f/b+g avoids subtractive cancellation in the mixed second
form. Non-coast intervals use adaptive DOP853, while every coast is propagated
by its exact affine-radius formula. Two tolerances and an independent (f,g)
formulation measure finite numerical sensitivity. These checks are not an
interval ODE certificate or a nonlinear closed-surface construction.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,hashlib,importlib.util,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('fd2d_full_m2_candidate',HERE/'fd2d_frozen_ellipse_candidate.py')
fm=importlib.util.module_from_spec(sp);sp.loader.exec_module(fm)


def radial_jet(candidate,p,u):
    u=np.atleast_1d(np.asarray(u,dtype=float));a,v,acc=candidate._jet(p,u)
    if p['kind']=='hermite':b=np.sqrt((1-v)*(1+v))
    else:
        phi,_=fm.phase(p,u);b=np.cos(phi)
    if np.any(b<=0):raise ValueError('The positive b chart was left')
    return a,v,b,acc


class LinearTrace:
    def __init__(self,candidate,initial_fg=(1.,0.),*,rtol=2e-12,atol=2e-14,max_step=.04,
                 coordinates='fq',backward=False):
        self.candidate=candidate;self.coordinates=coordinates;self.rtol=rtol;self.atol=atol
        self.max_step=max_step;self.backward=backward;self.parts=[None]*len(candidate.segments)
        self.calls=0
        initial_fg=np.asarray(initial_fg,dtype=float)
        first=candidate.segments[-1] if backward else candidate.segments[0]
        _,vv,bb,_=radial_jet(candidate,first,[1. if backward else 0.])
        y=initial_fg.copy()
        if coordinates=='fq':y[1]+=vv[0]*y[0]/bb[0]
        ids=range(len(candidate.segments)-1,-1,-1) if backward else range(len(candidate.segments))
        for j in ids:
            p=candidate.segments[j];anchor_u=1. if backward else 0.
            a0,v0,b0,_=radial_jet(candidate,p,[anchor_u])
            if p['kind'] in ('coast','coast_to'):
                q=y[1] if coordinates=='fq' else y[1]+v0[0]*y[0]/b0[0]
                part=dict(kind='exact_coast',anchor_u=anchor_u,anchor_radius=a0[0],
                          f=y[0],q=q,v=v0[0],b=b0[0])
                self.parts[j]=part
                values=self.values(j,np.array([0. if backward else 1.]))
                y=np.array([values['f'][0],values['q' if coordinates=='fq' else 'g'][0]])
                continue
            def rhs(u,state):
                a,v,b,acc=radial_jet(candidate,p,[u]);a,v,b,acc=a[0],v[0],b[0],acc[0]
                if coordinates=='fq':
                    f,q=state
                    return p['L']*np.array([(v*f-4*b*q)/a,acc*f/b**3])
                f,g=state
                return p['L']/a*np.array([-3*v*f-4*b*g,3*v*v*f/b+4*v*g])
            sol=solve_ivp(rhs,(1.,0.) if backward else (0.,1.),y,method='DOP853',
                rtol=rtol,atol=atol,max_step=max_step,dense_output=True)
            if not sol.success:raise ArithmeticError(sol.message)
            self.parts[j]=dict(kind='numerical',solution=sol.sol)
            y=sol.y[:,-1];self.calls+=sol.nfev
        self.final_fg=self.endpoint(start=backward)

    def values(self,index,u):
        p=self.candidate.segments[index];part=self.parts[index]
        u=np.atleast_1d(np.asarray(u,dtype=float));a,v,b,acc=radial_jet(self.candidate,p,u)
        if part['kind']=='exact_coast':
            q=np.zeros_like(u)+part['q'];ratio=a/part['anchor_radius']
            if abs(part['v'])<1e-14:
                f=part['f']-4*part['b']*part['q']*p['L']*(u-part['anchor_u'])/part['anchor_radius']
            else:f=ratio*part['f']+4*part['b']*part['q']/part['v']*(1-ratio)
            g=q-v*f/b
        else:
            state=part['solution'](u);f=state[0]
            if self.coordinates=='fq':q=state[1];g=q-v*f/b
            else:g=state[1];q=v*f/b+g
        eta=3*f/(a*b*b);zeta=-6*q/(a*b)
        eta_s=2*v*acc/(b*b)*eta+2*zeta/a
        zeta_s=-2*acc/(b*b)*eta-(v/a-v*acc/(b*b))*zeta
        return dict(s=p['s0']+p['L']*u,u=u,a=a,v=v,b=b,acc=acc,f=f,g=g,q=q,
                    eta=eta,zeta=zeta,eta_s=eta_s,zeta_s=zeta_s,
                    k_meridian=abs(acc/b),k_circumferential=b/a,n_reference=b/a)

    def endpoint(self,start=False):
        j=0 if start else len(self.parts)-1;data=self.values(j,[0. if start else 1.])
        return np.array([data['f'][0],data['g'][0]])

    def extrema(self,grid=129):
        global_extrema={name:dict(value=0.,absolute=0.) for name in ('f','g','q','eta','zeta')}
        rows=[]
        for j,p in enumerate(self.candidate.segments):
            u=np.linspace(0,1,grid);data=self.values(j,u);candidates=list(u)
            for name in ('eta','zeta'):
                d=data[name+'_s']
                for k in range(len(u)-1):
                    if d[k]*d[k+1]<0:
                        root=brentq(lambda x:float(self.values(j,[x])[name+'_s'][0]),u[k],u[k+1],xtol=2e-13)
                        candidates.append(root)
            u=np.unique(np.asarray(candidates));data=self.values(j,u)
            row=dict(index=j,label=p.get('label'),kind=p['kind'],s0=p['s0'],s1=p['s1'],length=p['L'],
                     minimum_b=float(data['b'].min()),minimum_n_reference=float(data['n_reference'].min()),
                     maximum_rotational_meridian_curvature=float(data['k_meridian'].max()),
                     samples_and_stationary_points=len(u),end_fg=[float(data['f'][-1]),float(data['g'][-1])])
            for name in global_extrema:
                k=int(np.argmax(abs(data[name])));record=dict(value=float(data[name][k]),absolute=float(abs(data[name][k])),
                    s=float(data['s'][k]),piece=j,label=p.get('label'),u=float(u[k]),
                    a=float(data['a'][k]),v=float(data['v'][k]),b=float(data['b'][k]),
                    f=float(data['f'][k]),g=float(data['g'][k]),q=float(data['q'][k]))
                row['maximum_abs_'+name]=record
                if record['absolute']>global_extrema[name]['absolute']:global_extrema[name]=record
            rows.append(row)
        return dict(global_extrema=global_extrema,pieces=rows,stationary_grid=grid,
                    extrema_scope='Dense finite samples plus sign-bracketed stationary points; no continuous enclosure is claimed.')

    def sample(self,grid=257):
        arrays={name:[] for name in ('s','u','a','v','b','acc','f','g','q','eta','zeta','k_meridian','n_reference')}
        arrays['piece']=[]
        for j in range(len(self.parts)):
            count=grid if self.candidate.segments[j]['L']>=.03 else 33
            u=np.linspace(0,1,count);data=self.values(j,u)
            for name in arrays:
                arrays[name].append(np.full(len(u),j,dtype=np.int32) if name=='piece' else data[name])
        return {name:np.concatenate(values) for name,values in arrays.items()}


def compare(first,second,grid=65,second_scale=1.):
    maxima={k:0. for k in ('f','g','q','eta','zeta')}
    for j in range(len(first.parts)):
        u=np.linspace(0,1,grid);x=first.values(j,u);y=second.values(j,u)
        for name in maxima:maxima[name]=max(maxima[name],float(abs(x[name]-second_scale*y[name]).max()))
    return maxima


def analyse(candidate,terminal=None,*,full_checks=True):
    trace=LinearTrace(candidate,rtol=3e-14,atol=3e-16,max_step=.02)
    ext=trace.extrema(129);end=trace.endpoint();scale=max(ext['global_extrema']['eta']['absolute'],ext['global_extrema']['zeta']['absolute'])
    out=dict(final_fg=end.tolist(),rhs_calls=trace.calls,extrema=ext,
        suggested_initial_amplitudes=dict(relative_shape_1_percent=.01/scale,relative_shape_5_percent=.05/scale,
            scope='Finite linear estimates only, before nonlinear error control.'),minimum_b=min(r['minimum_b'] for r in ext['pieces']),
        minimum_n_reference=min(r['minimum_n_reference'] for r in ext['pieces']))
    if terminal is not None:
        target=np.asarray(terminal,dtype=float)
        out['normalized_terminal_direction_residual']=float((end[0]*target[1]-end[1]*target[0])/(np.linalg.norm(end)*np.linalg.norm(target)))
        out['actual_terminal_height_gain']=float(end[1])
    if full_checks:
        loose=LinearTrace(candidate,rtol=2e-12,atol=2e-14,max_step=.04)
        independent=LinearTrace(candidate,rtol=2e-13,atol=2e-15,max_step=.02,coordinates='fg')
        fine_ext=trace.extrema(257)
        out['finite_error_checks']=dict(tolerance_comparison=compare(trace,loose),coordinate_comparison=compare(trace,independent),
            doubled_stationary_grid_change={name:abs(fine_ext['global_extrema'][name]['absolute']-ext['global_extrema'][name]['absolute']) for name in ('eta','zeta')},
            original_candidate_linear_endpoint=candidate.linear([1.,0.]).tolist(),
            original_endpoint_difference=(end-candidate.linear([1.,0.])).tolist(),
            rigorous_interval_error_bound=False)
        if terminal is not None:
            back=LinearTrace(candidate,terminal,rtol=3e-14,atol=3e-16,max_step=.02,backward=True)
            core=back.endpoint(start=True);factor=1/core[0]
            out['finite_error_checks'].update(backward_core_fg=core.tolist(),backward_normalized_core_g=float(factor*core[1]),
                forward_backward_normalized_difference=compare(trace,back,second_scale=factor))
    return trace,out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json')
    p.add_argument('--out-prefix',type=Path,required=True);args=p.parse_args();start=time.monotonic()
    bundle=json.loads(args.candidate.read_text());candidate=fm.Candidate(bundle)
    terminal=bundle['finite_linear_screen']['terminal_direction']
    trace,out=analyse(candidate,terminal)
    state=args.out_prefix.with_name(args.out_prefix.name+'-trajectory.npz');np.savez_compressed(state,**trace.sample())
    report=dict(schema='fd2d-full-m2-relative-second-form-amplification-v1',scope=__doc__,
        source_sha256=fm.digest(__file__),candidate_file=args.candidate.name,candidate_sha256=fm.digest(args.candidate),
        provider_sha256=fm.digest(HERE/'fd2d_frozen_ellipse_candidate.py'),trajectory_file=state.name,
        trajectory_sha256=fm.digest(state),trajectory_bytes=state.stat().st_size,
        numerical_representation='f,q with q=v*f/b+g; phase b evaluated as cos(phi); exact coast propagation',
        exact_relative_forms=dict(eta='3*f/(a*b^2)',zeta='-6*q/(a*b)'),
        initial_fg=[1.,0.],analysis=out,seconds=time.monotonic()-start,
        nonlinear_solution=False,continuous_interval_certificate=False)
    path=args.out_prefix.with_name(args.out_prefix.name+'-report.json');path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=path.name,endpoint=out['final_fg'],maxima=out['extrema']['global_extrema'],
        finite_error_checks=out['finite_error_checks'],suggested_initial_amplitudes=out['suggested_initial_amplitudes'],seconds=report['seconds']),indent=2))


if __name__=='__main__':main()
