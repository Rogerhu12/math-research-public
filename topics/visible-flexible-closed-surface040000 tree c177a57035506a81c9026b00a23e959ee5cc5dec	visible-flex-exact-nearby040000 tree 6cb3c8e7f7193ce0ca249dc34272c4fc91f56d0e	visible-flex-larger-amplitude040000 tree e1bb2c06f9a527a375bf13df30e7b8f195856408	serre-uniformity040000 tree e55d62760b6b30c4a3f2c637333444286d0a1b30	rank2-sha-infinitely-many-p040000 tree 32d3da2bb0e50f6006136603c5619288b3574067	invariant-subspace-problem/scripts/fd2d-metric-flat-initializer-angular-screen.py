#!/usr/bin/env python3
"""Finite angular projection screen of the actual flat-prefix initial guess.

Recovered source after executor loss. This program neither solves a BVP nor
certifies a surface. It compares complete analytic lifting plus finite Fourier
correction at selected actual radial nodes. Dense angular samples remain samples.
Every new report binds its own source and input bytes; old missing arrays/reports
must be recomputed and are never reconstructed from quoted numerical maxima.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_flat_prefix_initializer import ActualFlatPrefixInitializer

HERE=Path(__file__).resolve().parent
TOP=HERE.parent


def identity(path):
    path=Path(path);raw=path.read_bytes()
    return dict(path=str(path.resolve()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def step5(value):
    t=np.clip(np.asarray(value,float),0.,1.)
    return t**3*(10-15*t+6*t*t)


def flat_shape(amplitude,r,u):
    """Full II of A*S9 in n,m,l order, including the flat clipped arcs."""
    r,u=np.broadcast_arrays(np.asarray(r,float),np.asarray(u,float))
    sn,cs=np.sin(u),np.cos(u)
    raw=(np.abs(r*sn)-.34)/.46
    q=np.clip(raw,0.,1.)
    k=np.where((raw>0.)&(raw<1.),float(amplitude)*630*q**4*(1-q)**4/.46,0.)
    return np.stack((k*cs*cs,-k*sn*cs,k*sn*sn),axis=-1)


def target_and_lift(problem,source,x,xi,amplitude):
    """Exact initial-function formula before finite Fourier correction.

    x and xi are one-dimensional and the output axes are angle,node,component.
    The original actual IVP is used only on its stored interval. Its extension
    is the same explicit initial guess used by RawLiftedDAE.initializer.
    """
    x=np.atleast_1d(np.asarray(x,float));xi=np.atleast_1d(np.asarray(xi,float))
    jet=problem.profile.jet(x)
    a,ap,K,s=[np.asarray(jet[k],float) for k in ('a','a_s','K','s')]
    coordinate={k:np.asarray(v,float) for k,v in problem.chart.coordinates(x,coordinate=xi).items()}
    U=coordinate['u']
    nr=np.sqrt(np.maximum(0.,1-ap*ap))/a
    seed=1/np.asarray(problem.geometry.radius(xi),float)
    if problem.base_kind=='circle':
        seed=np.full_like(seed,1/float(problem.geometry.a0))
    wt=step5((x-.42*problem.profile.end)/(.58*problem.profile.end))
    wc=1-step5(x/min(.55,.4*problem.profile.end))
    tailcut=flat_shape(amplitude,.8,U)
    n=seed[:,None]*(nr[None,:]*float(problem.geometry.a0))+wt[None,:]*tailcut[:,:,0]
    m=wt[None,:]*tailcut[:,:,1]
    if abs(float(source.T)-float(problem.profile.T))>1e-14:
        raise ValueError('The stored actual initializer and selected T differ')
    end=float(source.interval[1]);keep=s<=end
    if np.any(keep):
        actual=source.evaluate_material(s[None,keep],U[:,keep])
        n[:,keep],m[:,keep]=actual['n'],actual['m']
    if np.any(~keep):
        angle=U[:,~keep]
        last=source.evaluate_material(np.full_like(angle,end),angle)
        aa,vv,_=source.candidate.profile(np.array([end]))
        nr_last=float(np.sqrt(1-vv[0]*vv[0])/aa[0])
        if not nr_last>0.:
            raise ArithmeticError('The actual extension port must have positive rotational n')
        weight=step5((s[~keep]-end)/(problem.profile.current.end-end))
        n[:,~keep]=last['n']*(nr[None,~keep]/nr_last)+weight[None,:]*tailcut[:,~keep,0]
        m[:,~keep]=(1-weight[None,:])*last['m']+weight[None,:]*tailcut[:,~keep,1]
    l=np.divide(K[None,:]+m*m,n,out=np.zeros_like(n),where=np.abs(n)>1e-13)
    total=np.stack((n,m,l),axis=-1)
    lift=wt[None,:,None]*flat_shape(amplitude,a[None,:],U)
    lift[:,:,0]+=wc[None,:]*seed[:,None]
    at_end=x==problem.profile.end
    if np.any(at_end):total[:,at_end]=lift[:,at_end]
    return total,lift,jet,coordinate


def fourier_values(y,xi,K):
    xi=np.asarray(xi,float)
    f=2*np.arange(K+1)
    E=np.cos(xi[:,None]*f)
    O=np.sin(xi[:,None]*f[1:])
    e,d=K+1,2*K+1
    return np.stack((E@y[:,:e].T,O@y[:,e:d].T,E@y[:,d:].T),axis=-1)


def retained_even_part(value,K):
    count=value.shape[0]
    if 4*K>=count:raise ValueError('Dense angle count is too small for the retained modes')
    coeff=np.fft.rfft(value,axis=0)
    masked=np.zeros_like(coeff)
    masked[2*np.arange(K+1)]=coeff[2*np.arange(K+1)]
    return np.fft.irfft(masked,n=count,axis=0)


def shape_radius(fields):
    n,m,l=fields[...,0],fields[...,1],fields[...,2]
    d=np.hypot(n-l,2*m)
    return np.maximum(np.abs((n+l+d)/2),np.abs((n+l-d)/2))


def point_report(index,problem,xi,fields,exact,jet,coordinate,gauss):
    i,j=index
    a=float(jet['a'][j]);u=float(coordinate['u'][i,j])
    return dict(angle_index=int(i),node_index=int(j),x=float(problem.x[j]),
        s=float(jet['s'][j]),a=a,a_s=float(jet['a_s'][j]),K=float(jet['K'][j]),
        computational_xi=float(xi[i]),material_u=u,
        flat_edge_material_angle=float(np.arcsin(min(1.,.34/a))),
        projected_nml=fields[i,j].tolist(),unprojected_initial_nml=exact[i,j].tolist(),
        gauss_defect=float(gauss[i,j]))


def screen_one(K,args):
    started=time.monotonic()
    problem=RawLiftedDAE(args.candidate,modes=K,max_step=args.mesh_step,gap=.9,
        profile_kind='positive_clock',tail_kind='positive_bernstein')
    problem.profile.set_parameter(args.T)
    source=ActualFlatPrefixInitializer(args.trajectory,args.candidate,geometry=problem.geometry)
    theta=np.asarray(problem.chart.theta,float)
    exact_work,lift_work,jet_work,coords_work=target_and_lift(
        problem,source,problem.x,theta,args.amplitude)
    corr=exact_work-lift_work
    y=np.concatenate(((problem.PE@corr[:,:,0]).T,
        (problem.PO@corr[:,:,1]).T,(problem.PE@corr[:,:,2]).T),axis=1)
    # This is the explicit initializer's central/cut definition, not a cleanup
    # of a previously saved finite solution.
    y[0]=0.;y[-1]=0.
    p=np.zeros(2*K+2);p[K:-1]=args.amplitude;p[-1]=args.T
    prefix=Path(str(args.out_prefix)+f'-k{K}')
    prefix.parent.mkdir(parents=True,exist_ok=True)
    arrays=Path(str(prefix)+'-initial.npz')
    np.savez_compressed(arrays,mesh=problem.x,corrections=y,parameters=p)
    workfields=fourier_values(y,theta,K)+lift_work
    workG=workfields[:,:,0]*workfields[:,:,2]-workfields[:,:,1]**2-np.asarray(jet_work['K'])[None,:]
    xi=2*np.pi*np.arange(args.angles)/args.angles
    exact,lift,jet,coords=target_and_lift(problem,source,problem.x,xi,args.amplitude)
    fields=fourier_values(y,xi,K)+lift
    G=fields[:,:,0]*fields[:,:,2]-fields[:,:,1]**2-np.asarray(jet['K'])[None,:]
    Gexact=exact[:,:,0]*exact[:,:,2]-exact[:,:,1]**2-np.asarray(jet['K'])[None,:]
    low=retained_even_part(G,K);omitted=G-low
    minimum=np.unravel_index(np.argmin(fields[:,:,0]),fields[:,:,0].shape)
    worst=np.unravel_index(np.argmax(np.abs(G)),G.shape)
    maxl=np.unravel_index(np.argmax(np.abs(exact[:,:,2])),exact[:,:,2].shape)
    radial=[]
    for j in np.argsort(-np.max(np.abs(G),axis=0))[:8]:
        radial.append(dict(node=int(j),x=float(problem.x[j]),s=float(jet['s'][j]),
            n_min=float(np.min(fields[:,j,0])),gauss_max=float(np.max(np.abs(G[:,j]))),
            low_gauss_max=float(np.max(np.abs(low[:,j]))),
            omitted_gauss_max=float(np.max(np.abs(omitted[:,j]))),
            formal_curvature_max=float(np.max(shape_radius(fields[:,j]))),
            unprojected_formal_curvature_max=float(np.max(shape_radius(exact[:,j])))))
    compare=None
    if K==7 and args.reference_k7 and Path(args.reference_k7).is_file():
        with np.load(args.reference_k7,allow_pickle=False) as ref:
            same_mesh=np.array_equal(ref['mesh'],problem.x)
            compare=dict(path=identity(args.reference_k7),mesh_bitwise_equal=bool(same_mesh),
                parameter_bitwise_equal=bool(np.array_equal(ref['parameters'],p)),
                coefficients_max_difference=(float(np.max(np.abs(ref['corrections']-y)))
                    if same_mesh and ref['corrections'].shape==y.shape else None),
                interpretation='same-chart reconstruction check only; fixed-chart wrapper changes the represented coordinate')
    result=dict(schema='fd2d-flat-initializer-angular-projection-screen-recovery-v1',
        status='FINITE_INITIAL_GUESS_SCREEN_ONLY',modes=K,radial_nodes=problem.N,
        source_work_angles=len(theta),dense_angles=args.angles,physical_T=args.T,
        amplitude=args.amplitude,angular_chart='radially blended fixed-seed-phi to material-u',
        blend_interval=list(problem.blend),profile_kind=problem.profile_kind,tail_kind=problem.tail_kind,
        candidate=identity(args.candidate),trajectory=identity(args.trajectory),
        source=identity(__file__),raw_problem_source=identity(HERE/'fd2d_gc_raw_lifted_dae.py'),
        initializer_source=identity(HERE/'fd2d_flat_prefix_initializer.py'),
        arrays=identity(arrays),initializer_definition=source.definition(),
        n_min=float(np.min(fields[:,:,0])),negative_n_samples=int(np.count_nonzero(fields[:,:,0]<0)),
        gauss_max=float(np.max(np.abs(G))),low_gauss_max=float(np.max(np.abs(low))),
        omitted_gauss_max=float(np.max(np.abs(omitted))),
        formal_curvature_max=float(np.max(shape_radius(fields))),
        unprojected_gauss_max=float(np.max(np.abs(Gexact))),
        unprojected_formal_curvature_max=float(np.max(shape_radius(exact))),
        source_grid_n_min=float(np.min(workfields[:,:,0])),
        source_grid_gauss_max=float(np.max(np.abs(workG))),
        negative_minimum=point_report(minimum,problem,xi,fields,exact,jet,coords,G),
        maximum_gauss=point_report(worst,problem,xi,fields,exact,jet,coords,G),
        maximum_unprojected_l=point_report(maxl,problem,xi,fields,exact,jet,coords,G),
        largest_radial_defects=radial,reference_K7=compare,
        elapsed_seconds=time.monotonic()-started,
        no_BVP_or_ODE_solve=True,no_continuous_or_final_surface_claim=True,
        recovery='Recomputed reports, when run, have new identities; historical missing outputs are not regenerated from summary numbers.')
    out=Path(str(prefix)+'.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(K=K,nodes=problem.N,n_min=result['n_min'],G=result['gauss_max'],
        G_low=result['low_gauss_max'],G_omitted=result['omitted_gauss_max'],
        formal_curvature=result['formal_curvature_max'],report=str(out))),flush=True)
    return result


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,default=TOP/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    p.add_argument('--trajectory',type=Path,default=TOP/'notes/2026-11-12-fd2d-flat-prefix-balanced-ivp-01-trajectory.npz.gz')
    p.add_argument('--reference-k7',type=Path,default=TOP/'notes/2026-11-12-fd2d-root-flat-positive-full01-initial.npz')
    p.add_argument('--out-prefix',type=Path,default=TOP/'notes/2026-11-12-fd2d-metric-flat-initializer-angular-screen-recovery01')
    p.add_argument('--modes',type=int,nargs='+',default=[7,15,31])
    p.add_argument('--mesh-step',type=float,default=.04)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--T',type=float,default=.02)
    p.add_argument('--amplitude',type=float,default=.9)
    return p


def main():
    args=parser().parse_args()
    result=[screen_one(K,args) for K in args.modes]
    output=Path(str(args.out_prefix)+'-report.json')
    output.write_text(json.dumps(dict(schema='fd2d-flat-initializer-angular-screens-recovery-v1',
        source=identity(__file__),reports=result,continuous_certificate=False),indent=2)+'\n')
    print(json.dumps(dict(complete=True,report=str(output))),flush=True)


if __name__=='__main__':main()
