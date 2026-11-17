#!/usr/bin/env python3
"""Literal radial quadrature calibration on an accepted integral-K height.

The scalar background, finite C2 height and initial angular curve all come
from the same accepted weak-tail field. No height projection or outer-round
condition is applied. The output concerns this finite patch only. This is an
independent frozen diagnostic, not the mutable direct-height optimizer.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,sys,time
import numpy as np

HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'scripts'))
from parallel_20261117_dynamic_tail import Background

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out

def derivative(value,axis):
    n=value.shape[axis];f=1j*np.fft.fftfreq(n,d=1/n);f[n//2]=0
    shape=[1]*value.ndim;shape[axis]=n
    return np.fft.ifft(np.fft.fft(value,axis=axis)*f.reshape(shape),axis=axis).real

def gauss_integrator(order):
    z,w=np.polynomial.legendre.leggauss(order);V=np.polynomial.legendre.legvander(z,order-1)
    I=np.empty_like(V)
    for j in range(order):
        p=np.zeros(order);p[j]=1;q=np.polynomial.legendre.legint(p)
        I[:,j]=(np.polynomial.legendre.legval(z,q)-np.polynomial.legendre.legval(-1.,q))/2
    return (z+1)/2,w/2,np.linalg.solve(V.T,I.T).T

def main(args):
    angular=module('exact_warm_angular','2026-11-17-parallel-model-angular-reconstruct.py')
    modes=module('exact_warm_modes','2026-11-17-parallel-geometry-height-mode-api.py')
    start=time.perf_counter();hm=modes.HeightModes(args.state,args.background,mean_anchor=args.mean_anchor)
    bg=Background(args.background,'physical-r');r0,r1=bg.r[[0,-1]]
    if args.template:
        params=json.loads(args.template.read_text())['parameters']
    else:
        knots=[row['r']-r0 for row in bg.data['rows'] if row['x'] in (0,1)]
        knots.extend([.001,.003,.005,.015,.04,.08,.15,.25,.4])
        params=dict(trace=str(args.trace),angles=args.angles,metric_stride=args.metric_stride,height_knots=json.dumps(sorted(set(knots))))
    trace=json.loads(Path(params['trace']).read_text());N=params['angles']
    phi=2*np.pi*np.arange(N)/N;rf=2*np.arange(1,len(trace['rho_cos_coefficients'])+1);rc=np.array(trace['rho_cos_coefficients'])
    rho=1+np.cos(phi[:,None]*rf)@rc;theta=phi+np.sin(phi[:,None]*rf)@(rc/rf)
    rhop=-np.sin(phi[:,None]*rf)@(rc*rf);f=hm.frequency;co=np.cos(theta[:,None]*f);si=np.sin(theta[:,None]*f)
    knots=np.array(json.loads(params['height_knots']));knots=knots[(knots>0)&(knots<r1-r0)]
    chosen=[row['r'] for i,row in enumerate(bg.rows) if i%params['metric_stride']==0 or row['x'] in (0,1)]
    base_edges=np.unique(np.r_[r0,chosen,r1,r0+knots])
    u=hm.at_r([r0]);w0=np.exp(bg.spline(r0));wr0=w0*bg.spline(r0,1)
    h=u['h0'][0]+co@u['C'][0];hr=u['h0r'][0]+co@u['Cr'][0];hrr=u['h0rr'][0]+co@u['Crr'][0]
    hp=-rho*(si@(f*u['C'][0]));hrp=-rho*(si@(f*u['Cr'][0]))
    hpp=-rho*rho*(co@(f*f*u['C'][0]))-rhop*(si@(f*u['C'][0]))
    hrpp=-rho*rho*(co@(f*f*u['Cr'][0]))-rhop*(si@(f*u['Cr'][0]))
    initial=angular.reconstruct_slice(r=r0,w=w0,wr=wr0,h=h,hr=hr,hrr=hrr,
        h_phi=hp,h_phiphi=hpp,hr_phi=hrp,hr_phiphi=hrpp,rho=rho,rho_phi=rhop)
    xy0=initial['F'][:,:2];alpha0=initial['alpha'];answers=[]
    for gauss,refinement in [(4,1),(8,1),(16,1),(8,2)]:
        edges=np.unique((base_edges[:-1,None]+np.diff(base_edges)[:,None]*np.linspace(0,1,refinement+1)).ravel())
        width=np.diff(edges);gx,gw,gI=gauss_integrator(gauss)
        rr=edges[:-1,None]+width[:,None]*gx;r=rr.ravel();v=hm.at_r(r)
        w=np.exp(bg.spline(r));E=1+w*w
        hp=-rho[None,:]*((v['C']*f)@si.T);hr=v['h0r'][:,None]+v['Cr']@co.T
        hrp=-rho[None,:]*((v['Cr']*f)@si.T)
        S=1-(hp/(r[:,None]*rho[None,:]))**2;D=E[:,None]*S-hr*hr
        if min(S.min(),D.min())<=0:raise ValueError('Projection branch is not positive')
        a=np.sqrt(D/S);q=r[:,None]*rho[None,:]*np.sqrt(S);b=-hr*hp/q
        A=hr*(hrp-hp/r[:,None])/(r[:,None]*rho[None,:]*S*np.sqrt(D))
        AA=A.reshape(len(width),gauss,N);da=width[:,None]*np.einsum('q,cqn->cn',gw,AA)
        before=np.concatenate((np.zeros_like(da[:1]),np.cumsum(da,axis=0)[:-1]),axis=0)
        alpha=(alpha0+before[:,None,:]+width[:,None,None]*np.einsum('ij,cjn->cin',gI,AA)).reshape(-1,N)
        tt=np.stack((np.cos(alpha),np.sin(alpha)),axis=-1);nn=np.stack((np.sin(alpha),-np.cos(alpha)),axis=-1)
        V=b[:,:,None]*tt+a[:,:,None]*nn;VV=V.reshape(len(width),gauss,N,2)
        dx=width[:,None,None]*np.einsum('q,cqnk->cnk',gw,VV)
        before_xy=np.concatenate((np.zeros_like(dx[:1]),np.cumsum(dx,axis=0)[:-1]),axis=0)
        xy=(xy0+before_xy[:,None,:,:]+width[:,None,None,None]*np.einsum('ij,cjnk->cink',gI,VV)).reshape(-1,N,2)
        xp=derivative(xy,1);er=(np.sum(V*V,axis=2)+hr*hr)/E[:,None]-1
        gr=(np.sum(xp*xp,axis=2)+hp*hp)/(r[:,None]*rho[None,:])**2-1
        fr=(np.sum(V*xp,axis=2)+hr*hp)/(np.sqrt(E)[:,None]*r[:,None]*rho[None,:])
        op=(abs(er+gr)+np.hypot(er-gr,2*fr))/2;i,j=np.unravel_index(np.argmax(op),op.shape)
        result=dict(gauss=gauss,refinement=refinement,panels=len(width),points=op.size,max_gram=float(op[i,j]),
            worst_r=float(r[i]),worst_phi=float(phi[j]),worst_rr=float(er[i,j]),worst_pp=float(gr[i,j]),
            worst_rp=float(fr[i,j]),minimum_D=float(D.min()),maximum_alpha_motion=float(abs(alpha-alpha0).max()),seconds=time.perf_counter()-start)
        answers.append(result);print(json.dumps(result),flush=True)
        sources={str(p):hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in [__file__,args.state,args.background,params['trace'],HERE/'2026-11-17-parallel-model-angular-reconstruct.py',HERE/'2026-11-17-parallel-geometry-height-mode-api.py']}
        args.out.write_text(json.dumps(dict(scope=__doc__,source_sha256=sources,angles=N,mean_anchor=args.mean_anchor,
            r0=float(r0),r1=float(r1),cases=answers,mean_quadrature=hm.mean_quadrature,initial_angular_density_gap=float(abs(initial['angular_density_gap']).max()),
            limitations=['Finite field only','No outer-round constraint','Sampled quadrature comparison, not a rigorous global bound','No closed-surface or reach claim']),indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--template',type=Path);p.add_argument('--trace',type=Path)
    p.add_argument('--angles',type=int,default=512);p.add_argument('--metric-stride',type=int,default=64)
    p.add_argument('--state',type=Path,required=True);p.add_argument('--background',type=Path,required=True)
    p.add_argument('--mean-anchor',type=float,required=True);p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
