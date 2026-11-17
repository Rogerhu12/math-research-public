#!/usr/bin/env python3
"""Independent one-column, matrix-free audit of a saved mixed-boundary step."""
import argparse,gzip,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigvals,solve

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--topic',type=Path,required=True)
p.add_argument('--field',type=Path,required=True)
p.add_argument('--linear-report',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
args=p.parse_args()
helper=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
spec=importlib.util.spec_from_file_location('mixed_check_helper',helper)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
data=json.loads(gzip.decompress(args.field.read_bytes()))
previous=json.loads(args.linear_report.read_text())
q=h.Frenet(data['M'],data['N']);reader=h.Frenet(q.M,8192)
profile=h.profile_from(data);x=np.array(data['mesh']);ys=np.array(data['states'])
dy=np.array(data['rhs']);ddy=np.array(data['d2']);delta=np.array(previous['linear_response']['delta_initial_coefficients'])
coefficients=[]
for i,w in enumerate(np.diff(x)):
 c0=ys[i];c1=w*dy[i];c2=w*w*ddy[i]/2
 a=ys[i+1]-c0-c1-c2;b=w*dy[i+1]-c1-2*c2;c=w*w*ddy[i+1]-2*c2
 coefficients.append(np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2]))
def reference(s):
 i=min(len(x)-2,max(0,int(np.searchsorted(x,s,side='right')-1)))
 return np.polynomial.polynomial.polyval((s-x[i])/(x[i+1]-x[i]),coefficients[i])
_,d,_=q.jet(ys[-1]);V,dV,_=q.jet(dy[-1]);Acc,_,_=q.jet(ddy[-1])
cross=np.cross(V,d);area=np.linalg.norm(cross,axis=1)
T,Ts=h.moving_frame_map(q,dict(d=d,V=V,dV=dV,Acc=Acc,normal=cross/area[:,None],area=area))
a,ap,_=profile(x[-1]);A=q.jacobian(ys[-1],ap/a);B=solve(T.T,(T@A+Ts).T).T
ev=np.sort(eigvals(B).real);free=q.M-3;threshold=(ev[-free-1]+ev[-free])/2
schur,LB=h.selected_left(B,lambda re:re>threshold,q.M,None)
if schur['dimension']!=free:raise ValueError('Wrong full real-Schur block count')
L=LB@T;tail=np.zeros(q.n);m=np.arange(previous['linear_response']['target_cutoff']+1,q.M+1)
tail[m]=ys[-1,m];tail[q.M+m]=ys[-1,q.M+m];tail[2*q.M+1+m]=ys[-1,2*q.M+1+m]
target=-L@tail
def rhs(s,v):
 a,ap,_=profile(s)
 return q.jvp(reference(s),ap/a,v)
rows=[];responses=[]
for divisor,rtol,atol in [(256,1e-11,1e-18),(512,1e-12,1e-19)]:
 begin=time.perf_counter();step=(x[-1]-x[0])/divisor
 sol=solve_ivp(rhs,(x[0],x[-1]),delta,method='DOP853',rtol=rtol,atol=atol,
               first_step=step,max_step=step,t_eval=[x[-1]])
 if not sol.success:raise RuntimeError(sol.message)
 response=sol.y[:,-1];responses.append(response);residual=L@response-target
 row=dict(max_step=float(step),rtol=rtol,atol=atol,nfev=sol.nfev,seconds=time.perf_counter()-begin,
          right_row_residual_max=float(np.max(abs(residual))),right_row_residual_norm=float(np.linalg.norm(residual)),
          relative_to_target_norm=float(np.linalg.norm(residual)/np.linalg.norm(target)),
          right_delta_F_Fphi_Fphiphi_max=[float(np.linalg.norm(v,axis=1).max()) for v in reader.jet(response)])
 rows.append(row);print(json.dumps(row),flush=True)
diff=responses[1]-responses[0]
_,dd,ee=reader.jet(ys[0]+delta);Q=np.sum(dd*dd,axis=1);W=np.sum(np.cross(dd,ee)**2,axis=1)
a,ap,_=profile(x[0]);H=W-(ap/a)**2*Q**3
out=dict(source_sha256=h.sha(__file__),helper_sha256=h.sha(helper),reference_sha256=h.sha(args.field),
         linear_report_sha256=h.sha(args.linear_report),scope=__doc__,runs=rows,
         refined_difference_coeff_max=float(np.max(abs(diff))),refined_difference_row_norm=float(np.linalg.norm(L@diff)),
         refined_difference_F_Fphi_Fphiphi_max=[float(np.linalg.norm(v,axis=1).max()) for v in reader.jet(diff)],
         trial_initial_domain=dict(Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()),
                                   H_min_angle=float(reader.angle[np.argmin(H)])))
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True);print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out))),flush=True)
