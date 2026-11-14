#!/usr/bin/env python3
"""Manufactured round surface and radial velocity derivative checks for chart code."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import argparse,importlib.util,json,sys
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
HERE=Path(__file__).resolve().parent;NOTES=HERE.parent/'notes';spec=importlib.util.spec_from_file_location('adapt',HERE/'950f-prefix-adaptive-chart-bvp.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.old.install_source(a.source_root)
cfg=json.loads((NOTES/'2026-11-09-950f-prefix-weighted-k6-profile.json').read_text());port=json.loads((NOTES/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json').read_text());chart=json.loads((NOTES/'2026-11-09-950f-prefix-adaptive-chart.json').read_text());_,BVP=m.build_classes(chart);o=BVP(cfg,port,.08,8,256,False,.08);f=o.flow(0.)
s=f.end*np.array([0.,.07,.13,.23,.37,.47,.59,.71,.79,.87,.93,1.]);N=512;B,B1,B2=f.basis(N);z=np.zeros((f.n,len(s)));fr,sp,dW=f.velocity_s(s,z,z,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v'];aa,ap,app=f.profile(s);bb=np.sqrt(1-ap*ap);bp=-ap*app/bb
Fsc=g['s1'].copy();Fsc[:,:,2]+=bb[:,None];Fssc=g['s2'].copy();Fssc[:,:,2]+=bp[:,None]
Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None];Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
Fst=(sp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None];Fss=Fssc-2*v[:,:,None]*sp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
er=g['pos']/aa[:,None,None];et=np.stack((-er[:,:,1],er[:,:,0],np.zeros_like(er[:,:,0])),axis=-1);trueFs=ap[:,None,None]*er;trueFs[:,:,2]+=bb[:,None];trueFss=app[:,None,None]*er;trueFss[:,:,2]+=bp[:,None]
row=dict(scope=__doc__,round_Fs=float(abs(Fs-trueFs).max()),round_Ftheta=float(abs(Ft-aa[:,None,None]*et).max()),round_Fss=float(abs(Fss-trueFss).max()),round_Fstheta=float(abs(Fst-ap[:,None,None]*et).max()),round_Fthetatheta=float(abs(Ftt+aa[:,None,None]*er).max()),round_velocity_s=float(abs(dW-Fssc).max()))
rng=np.random.default_rng(20261109);s0=f.end*np.array([.123,.357,.583,.823]);Y0=rng.normal(size=(f.n,len(s0)))*1e-4;Y1=rng.normal(size=Y0.shape)*1e-4;Y2=rng.normal(size=Y0.shape)*1e-4
_,_,target=f.velocity_s(s0,Y0,Y1)
checks=[]
for h in [1e-4,5e-5,2.5e-5,1.25e-5]:
 up=f.frame(s0+h,f.q*(Y0+h*Y1+h*h*Y2/2))['V'];dn=f.frame(s0-h,f.q*(Y0-h*Y1+h*h*Y2/2))['V'];der=(up-dn)/(2*h);checks.append(dict(step=h,max_error=float(abs(der-target).max())))
row['velocity_s_finite_difference']=checks;a.out.write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row))
