#!/usr/bin/env python3
"""Sample along-prefix amplification at existing literal double roots.

This does not re-solve the recorded root search.  The tail port and all
physical profile parameters are retained.  Samples are numerical guidance,
not uniform bounds or a nonlinear obstruction theorem.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from physical_linear_design import PhysicalDesign,geometry

def amplification(design,parameters,rtol=2e-11,samples=65):
    f=design.profile(parameters);port=design.port;m=np.array([4.,8.]);r=port['cut']['radius'];w=port['cut']['backgroundSlope']
    D=np.asarray(port['linearSlope'][:2]);state=np.stack((-w*(r*D-m*m)/(m*m-1),np.ones(2)),axis=1)
    state/=np.linalg.norm(state,axis=1)[:,None];terminal=state.copy();logs=np.zeros(2);segments=[]
    def rhs(s,y):
        a,v,_=f.profile([s]);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v);z=y.reshape(2,2)
        F=z[:,0];G=z[:,1]
        return (np.stack((-(m*m-1)*v*F-m*m*b*G,(m*m-1)*v*v*F/b+m*m*v*G),axis=1)/a).ravel()
    for lo,hi in reversed(list(zip(f.breaks[:-1],f.breaks[1:]))):
        sol=solve_ivp(rhs,(hi,lo),state.ravel(),method='DOP853',rtol=rtol,atol=rtol*.01,dense_output=True,max_step=(hi-lo)/3)
        if not sol.success:raise RuntimeError(sol.message)
        segments.append((lo,hi,sol,logs.copy()))
        state=sol.y[:,-1].reshape(2,2);scale=np.linalg.norm(state,axis=1);state/=scale[:,None];logs+=np.log(scale)
    fields=[]
    for lo,hi,sol,ll in segments:
        s=np.linspace(lo,hi,samples);y=sol.sol(s).reshape(2,2,-1)
        y*=np.exp(ll-logs)[:,None,None]/state[:,0,None,None]
        aa=f.profile(s)[0];fields.append((s,y,aa))
    all_s=np.concatenate([z[0]for z in fields]);all_y=np.concatenate([z[1]for z in fields],axis=2);all_a=np.concatenate([z[2]for z in fields])
    rows=[]
    for j in range(2):
        i=np.argmax(abs(all_y[j,0]));k=np.argmax(abs(all_y[j,1]));b=np.argmax(abs(all_y[j,0])/all_a)
        rows.append(dict(mode=int(m[j]),max_abs_F=float(abs(all_y[j,0,i])),s_F=float(all_s[i]),
            max_abs_G=float(abs(all_y[j,1,k])),s_G=float(all_s[k]),
            max_abs_F_over_radius=float(abs(all_y[j,0,b])/all_a[b]),s_F_over_radius=float(all_s[b]),
            core_tau=float(state[j,1]),relative_terminal_height=float(terminal[j,1]*np.exp(-logs[j])/state[j,0])))
    return dict(profile=parameters,rows=rows,background=geometry(f,circle_radius=1.99,halfwidth=.147,cylinder_length=.54),rtol=rtol,samples_per_piece=samples)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--recorded-roots',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    design=PhysicalDesign(a.source_root,a.port);old=json.loads(a.recorded_roots.read_text());rows=[]
    for record in old['double_roots']:
        row=amplification(design,record['profile']);row['old_index']=record['index'];rows.append(row)
        print(json.dumps(dict(index=record['index'],vu=record['profile']['vu'],ramp=record['profile']['ramp'],F4=row['rows'][0]['max_abs_F'],F8=row['rows'][1]['max_abs_F'],D_round=row['background']['sample_ball_D_with_nominal_tail'])),flush=True)
    a.out.write_text(json.dumps(dict(scope=__doc__,recorded_roots_sha256=hashlib.sha256(a.recorded_roots.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),runs=rows),indent=2)+'\n')
