#!/usr/bin/env python3
"""Compare saved actual-A prefix and tail Cartesian cut jets in one frame.

The saved physical quintic is authoritative. Its mean first/second jets use
the production 1552-angle rule. The cut angle is required to be the identity.
Position is compared with both mean heights set to zero at the cut, which
fixes one global vertical translation and does not adjust any derivative.
This is a finite sampled seam diagnostic, not a glued closed surface.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def angular(y,d):
    N=len(y);k=np.arange(N//2+1)[:,None]
    return np.fft.irfft(np.fft.rfft(y,axis=0)*(1j*k)**d,n=N,axis=0)


def maximum(v):
    norm=np.linalg.norm(v,axis=-1);j=int(np.argmax(norm))
    return dict(vector_linf=float(norm[j]),component_linf=np.max(abs(v),axis=0).tolist(),
        angular_index=j,theta=float(2*np.pi*j/len(v)),vector_at_worst=v[j].tolist())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','source-topic','tail-complete','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();begin=time.monotonic();own_source_sha=sha(__file__)
    topic=a.topic.resolve();comp=topic/'computations';notes=topic/'notes';source=a.source_topic.resolve()
    primary=notes/'2026-11-13-strong-q126-m32-tail2-actual-r1.json.gz'
    port=comp/'alternative-neck-provider-smallcut30-port32-r2048.json'
    helper=comp/'geometric-checkpoint-core-pullback.py'
    spec=importlib.util.spec_from_file_location('exact_cut_saved_prefix',helper)
    pb=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pb;spec.loader.exec_module(pb)
    saved,_=pb.load_saved(primary,source,port,angular=1280)
    if saved.M!=32 or saved.rec['config']['angular']!=1280 or saved.sol.sol.c.shape[0]!=6:
        raise ValueError('Original M32 actual quintic with production angular1280 required')
    report=read(a.tail_complete);N=report['angular'];rows=report['rows']
    if N!=512 or len(rows)<2:raise ValueError('Original 512-angle tail data required')
    def node(row):
        path=a.tail_complete.parent/row['file'];b=path.read_bytes();raw=gzip.decompress(b)
        if hashlib.sha256(b).hexdigest()!=row['sha256']or hashlib.sha256(raw).hexdigest()!=row['rawSha256']:
            raise ValueError('Changed tail sidecar')
        return np.frombuffer(raw,dtype='<f8').reshape(N,12)
    z=node(rows[0]);z1=node(rows[1]);r=rows[0]['geometry']['r'];r1=rows[1]['geometry']['r']
    f=saved.flow;s=np.array([f.end]);psi=2*np.pi*np.arange(N)/N;eta=psi[None,:]
    angle=saved.angle(s,eta)
    if max(float(np.max(abs(angle[k])))for k in ['theta_s','theta_ss','rho_s','rhop_s','rhop'])>1e-13 or np.max(abs(angle['rho']-1))>1e-13:
        raise ValueError('Cut material-angle chart is not the identity through order two')
    if np.max(abs(angle['theta']-eta))>1e-13:raise ValueError('Cut angles shifted')
    aa,ap,app=f.profile(s);ap=float(ap[0]);app=float(app[0]);radius=float(aa[0])
    if abs(radius-r)>2e-14 or not ap<0:raise ValueError('Cut profile differs or has wrong direction')
    B,B1,B2=f.basis(N);meanN=max(512,16*(3*f.M+1));_,mB1,mB2=f.basis(meanN)
    Y=saved.sol.sol(s);Ys=saved.sol.sol(s,1);Yss=saved.sol.sol(s,2)
    fr,Fsp,dW=f.velocity_s(s,Y,Ys,B1,B2);mf,_,md=f.velocity_s(s,Y,Ys,mB1,mB2)
    meanS=float(np.mean(mf['V'][0,:,2]));meanSS=float(np.mean(md[0,:,2]))
    g=fr['geo'];Fsc=g['s1']+saved.q*f.values(Ys,B);Fssc=g['s2']+saved.q*f.values(Yss,B)
    Fsc[0,:,2]+=meanS;Fssc[0,:,2]+=meanSS
    rho=g['rho'];v=g['v']
    Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
    Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
    Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
    Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
    P=(g['pos']+saved.q*f.values(Y,B))[0]
    Pr=Fs[0]/ap;Prr=(Fss[0]-app*Pr)/ap**2
    prefix=dict(position=P,radial_first=Pr,angular_first=Ft[0],radial_second=Prr,mixed=Fst[0]/ap,angular_second=Ftt[0])
    sigma=float(f.bridge.sigma)
    if sigma not in [-1.,1.]:raise ValueError('Unknown physical tail reflection')
    er=np.c_[np.cos(psi),np.sin(psi),np.zeros(N)];et=np.c_[-np.sin(psi),np.cos(psi),np.zeros(N)]
    localP=r*er+z[:,:3];localV=er+z[:,3:6]
    localFt=r*et+angular(z[:,:3],1);localFtt=-r*er+angular(z[:,:3],2);localFrt=et+angular(z[:,3:6],1)
    geometry=rows[0]['geometry'];w=geometry['w'];wr=w*geometry['dlogwdx']/geometry['drdx'];E=geometry['E'];gamma=w*wr/E
    cross=np.cross(localV,localFt);normal=cross/np.linalg.norm(cross,axis=1)[:,None]
    if np.min(normal[:,2])<=0:raise ValueError('No target-metric completion')
    secondGW=gamma*localV+(z[:,9]-gamma*localV[:,2])[:,None]*normal/normal[:,2,None]
    secondGW[:,2]=z[:,9]
    secondDifference=np.empty_like(secondGW);secondDifference[:,:2]=(z1[:,3:5]-z[:,3:5])/(r1-r);secondDifference[:,2]=z[:,9]
    reflection=np.array([1.,1.,sigma])
    tail=dict(position=localP*reflection,radial_first=localV*reflection,angular_first=localFt*reflection,
              radial_second=secondGW*reflection,mixed=localFrt*reflection,angular_second=localFtt*reflection)
    differences={key:maximum(prefix[key]-tail[key])for key in prefix}
    differences['radial_second_nonuniform_endpoint']=maximum(Prr-secondDifference*reflection)
    array_path=a.out.with_suffix('.npz')
    np.savez_compressed(array_path,**{'prefix_'+k:v for k,v in prefix.items()},**{'tail_'+k:v for k,v in tail.items()},tail_rr_nonuniform=secondDifference*reflection)
    output=dict(schema='actual-A-prefix-tail-cut-Cartesian-twojet-comparison-v1',finished=True,
        source_sha256_at_start=own_source_sha,input_sha256={str(q):sha(q)for q in [primary,port,helper,a.tail_complete]},
        modes=32,prefix_production_angular=1280,mean_angular=meanN,comparison_angular=N,
        prefix_physical_polynomial_degree=5,cut_chart_identity_through_order_two=True,
        cut=dict(radius=r,physical_s=f.end,r_s=ap,r_ss=app,background_w=w,background_wr=wr,
                 gamma_rr_r=gamma,reflection_z=sigma,mean_s=meanS,mean_ss=meanSS),
        background_conversion=dict(metric_E_minus_inverse_r_s_squared=E-1/ap**2,
            physical_r_ss_minus_target=-w*wr/E**2-app),
        one_fixed_frame='Same centered x/y axes and material angle; multiply all tail z jets by bridge.sigma. Both cut means zero, defining one global vertical translation; no fitted rotation or radial-varying correction.',
        absolute_global_mean_height_integral_evaluated=False,
        differences=differences,
        tail_cardinal_vs_saved_point_angular=maximum(localFt-(r*et+z[:,6:9])),
        tail_cardinal_vs_saved_point_mixed_z=float(np.max(abs(localFrt[:,2]-z[:,10]))),
        tail_cardinal_vs_saved_point_second_z=float(np.max(abs(localFtt[:,2]-z[:,11]))),
        tail_minimum_normal_z=float(normal[:,2].min()),array_file=array_path.name,array_sha256=sha(array_path),
        seconds=time.monotonic()-begin,
        limitations=['Finite 512-angle comparison only; exact angular matching is not proved.',
            'The saved prefix quintic and its true derivatives are retained, not replaced by the PDE second derivative.',
            'Target-metric tail rr is an explicitly defined completion; equality with actual ODE Cartesian rr is not established by this test.',
            'The vertical mean anchor is fixed at the cut for this seam comparison; actual global height for closed assembly remains to be integrated.',
            'No correction, glued C2 surface, reach or completion claim.'])
    with a.out.open('x')as f:json.dump(output,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),differences=differences,cut=output['cut'],seconds=output['seconds'])),flush=True)


if __name__=='__main__':main()
