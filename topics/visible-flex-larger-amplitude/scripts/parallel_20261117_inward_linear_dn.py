#!/usr/bin/env python3
"""Finite material-mode DN on a fixed physical-r Hermite logw table.

A supplied homogeneous finite-far row is transported through every literal
Hermite cell in its local coordinate. State is height C and V=C_r;
C_r=V, V_r=(logw)_r*(m^2*C/r-V). This avoids dividing by tiny w in the ODE.
The unit Pcut normalization is applied only after reaching the right cut.
No actual nonaxisymmetric trace or infinite-tail error is asserted.
"""
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser(description=__doc__)
for k in ('background','columns','out'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--substeps',type=int,default=8);a=p.parse_args();start=time.perf_counter()
bg=json.loads(a.background.read_bytes());cols=json.loads(a.columns.read_bytes())
if cols['input_sha256']!=sha(a.background):raise ValueError('Different background identity')
table=[]
for v in bg['rows']:
 if not table or abs(v['r']-table[-1]['r'])>1e-15:table.append(v)
r=np.array([v['r']for v in table]);lw=np.array([v['logw']for v in table]);dlw=np.array([v['dlogwdr']for v in table])
if not np.all(np.diff(r)>0)or bg['shallow_at']!='right':raise ValueError('Require right-shallow physical table')
rows=cols['final']['modes'];m=np.array([v['mode']for v in rows]);bp=np.array([v['deepBoundary']['p']for v in rows]);bk=np.array([v['deepBoundary']['k']for v in rows])
if max(abs(v['deepBoundary']['r']-r[0])for v in rows)>1e-12:raise ValueError('Different deep port')
y=np.array([bk,m*bp/r[0]]);logs=np.zeros(len(m));peaks=np.full((4,len(m)),-np.inf);where=np.zeros((4,len(m)))
def measure(rr,ll):
 values=np.array([abs(-m*y[0]/rr),abs(y[1]),abs(y[0]),abs(y[1])]);powers=np.array([-1.,-1.,0.,0.])[:,None]
 value=np.log(np.maximum(values,1e-300))+logs+powers*ll
 mask=value>peaks;peaks[:]=np.maximum(peaks,value);where[mask]=rr
measure(r[0],lw[0]);spline=CubicHermiteSpline(r,lw,dlw);dt=1/a.substeps
for i,h in enumerate(np.diff(r)):
 c=spline.c[:,i]*np.array([h**3,h*h,h,1.])
 def rhs(t,v):return np.array([h*v[1],((3*c[0]*t+2*c[1])*t+c[2])*(m*m*v[0]/(r[i]+h*t)-v[1])])
 for j in range(a.substeps):
  t=j*dt;k1=rhs(t,y);k2=rhs(t+dt/2,y+dt*k1/2);k3=rhs(t+dt/2,y+dt*k2/2);k4=rhs(t+dt,y+dt*k3)
  y+=dt*(k1+2*k2+2*k3+k4)/6;t+=dt;measure(r[i]+h*t,((c[0]*t+c[1])*t+c[2])*t+c[3])
 norm=np.linalg.norm(y,axis=0);y/=norm;logs+=np.log(norm)
unit_log=np.log(r[-1]/m)+lw[-1]-np.log(abs(y[0]))-logs
result=[]
for j,mode in enumerate(m):
 result.append(dict(frequency=float(mode),cut_K_over_P=float(-r[-1]*y[1,j]/(mode*y[0,j])),
  P_gain=float(np.exp(peaks[0,j]+unit_log[j])),K_gain=float(np.exp(peaks[1,j]+unit_log[j])),
  height_gain=float(np.exp(peaks[2,j]+unit_log[j])),height_r_gain=float(np.exp(peaks[3,j]+unit_log[j])),
  K_peak_radius=float(where[1,j])))
report=dict(scope=__doc__,source_sha256=sha(__file__),background_sha256=sha(a.background),columns_sha256=sha(a.columns),
 intervals=len(r)-1,substeps=a.substeps,rows=result,seconds=time.perf_counter()-start)
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))
