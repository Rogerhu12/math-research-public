#!/usr/bin/env python3
"""Compare saved coupled prefixes on one frozen metric in physical coordinates.

These are sampled C2 Cauchy diagnostics, not an interval existence proof.
The actual nonlinear tail must be compared independently. No checkpoint or
physical parameter is modified, and no large numerical array is printed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('db6f_flat_source',HERE/'db6f-prefix-flat-geometry-source.py')
loader=importlib.util.module_from_spec(spec);spec.loader.exec_module(loader)

def jets(o,f,sol,s,h,N):
    B,B1,B2=f.basis(N);Y=sol.sol(s);Yp=sol.sol(s,1);Ypp=sol.sol(s,2)
    fr,Fsp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];v=g['v'];rho=g['rho']
    F=g['pos']+o.q*f.values(Y,B);F[:,:,2]+=h[:,None]
    Fsc=g['s1']+o.q*f.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
    Fssc=g['s2']+o.q*f.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
    return dict(F=F,Fs=Fsc-v[:,:,None]*fr['d'],Ft=fr['d']/rho[:,:,None],
      Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d'],
      Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None],
      Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--checkpoints',type=Path,nargs='+',required=True)
    p.add_argument('--linear-port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--radial',type=int,default=1201)
    p.add_argument('--angular',type=int,default=1024)
    a=p.parse_args();loaded=[loader.source(cp,a.linear_port,a.source_root)for cp in a.checkpoints]
    ref=loaded[0][0]
    for rec,_,_,_ in loaded:
        for key in ('frozen_profile','chart','warp_reference_q','physical_tail_parameters'):
            if rec[key]!=ref[key]:raise ValueError('Changed frozen material data: '+key)
        if not rec['solver_success'] or not rec['config']['actual_nonlinear_tail']:
            raise ValueError('A comparison checkpoint is not a completed nonlinear coupled solve')
    end=loaded[0][2].end
    if any(abs(f.end-end)>2e-14 for _,_,f,_ in loaded):raise ValueError('Changed physical meridian domain')
    s=np.unique(np.r_[np.linspace(0,end,a.radial),*[sol.x for _,_,_,sol in loaded]])
    heights=[f.height_integral(sol,s,a.angular,8)for _,_,f,sol in loaded]
    records=[]
    for cp,(rec,_,_,sol)in zip(a.checkpoints,loaded):
        records.append(dict(file=str(cp),sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
          modes=rec['config']['modes'],nodes=len(sol.x),amplitude=rec['actual_primary_amplitude'],
          prefix_metric=rec['summary']['metric_l1'],tail_parameters={k:rec['tail_config'][k]for k in ('depth','steps','shootingParts','quadrature')},
          tail_shooting_residual=rec['tail_seam']['tail_shooting_residual']))
    comparisons=[]
    for index in range(1,len(loaded)):
        maxima={k:0. for k in ('F','Fs','Ft','Fss','Fst','Ftt')}
        left,right=loaded[index-1],loaded[index]
        for begin in range(0,len(s),24):
            sl=slice(begin,begin+24)
            ja=jets(left[1],left[2],left[3],s[sl],heights[index-1][sl],a.angular)
            jb=jets(right[1],right[2],right[3],s[sl],heights[index][sl],a.angular)
            for k in maxima:maxima[k]=max(maxima[k],float(np.linalg.norm(jb[k]-ja[k],axis=2).max()))
        comparisons.append(dict(left=str(a.checkpoints[index-1]),right=str(a.checkpoints[index]),
          amplitude_difference=records[index]['amplitude']-records[index-1]['amplitude'],
          sampled_physical_jet_sup_difference=maxima,
          mean_cut_height_difference=float(heights[index][-1]-heights[index-1][-1])))
    out=dict(scope=__doc__,same_frozen_metric_checked=True,radial_nodes=len(s),angular=a.angular,
      records=records,comparisons=comparisons)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(same_frozen_metric_checked=True,radial_nodes=len(s),angular=a.angular,
                         comparisons=comparisons)),flush=True)

if __name__=='__main__':main()
