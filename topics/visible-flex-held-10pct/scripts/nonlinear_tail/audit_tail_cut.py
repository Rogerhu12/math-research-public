"""Compare actual upper-prefix jets with reflected actual tail cut jets.

At lambda != 1 this is explicitly a mismatch diagnostic, not an attempted seam.
Only an axial rigid rotation and translation align the independently fixed
Cartesian gauges. Material angle is not replaced by spatial polar angle.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--tail',type=Path,required=True);p.add_argument('--prefix',type=Path,required=True);p.add_argument('--lam',type=float,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
t=json.loads(gzip.decompress(a.tail.read_bytes()));b=np.load(a.prefix);names=['X','Xr','Xu','Xrr','Xru','Xuu'];j={n:np.array([row[n]for row in t['jets']])for n in names};n=len(j['X']);assert n==len(b['theta']);r=t['cut']['r'];w=t['cut']['w'];wr=t['cut']['wr'];rs=-1/np.sqrt(1+w*w);rss=-w*wr/(1+w*w)**2
q={'X':b['X'],'Xr':b['Xs']/rs,'Xu':b['Xtheta'],'Xrr':(b['Xss']-rss*b['Xs']/rs)/rs**2,'Xru':b['Xstheta']/rs,'Xuu':b['Xthetatheta']}
# Entire z coordinate, including the nonlinear mean derivative, is reflected.
for n in names:j[n][:,2]*=-1
c1=j['X'][:,0]+1j*j['X'][:,1];c2=q['X'][:,0]+1j*q['X'][:,1];phase=np.vdot(c1,c2);phase/=abs(phase)
for n in names:
 z=(j[n][:,0]+1j*j[n][:,1])*phase;j[n][:,0]=z.real;j[n][:,1]=z.imag
shift=q['X'].mean(0)-j['X'].mean(0);j['X']+=shift
fr,fu=j['Xr'],j['Xu'];normal=np.cross(fr,fu);area=np.linalg.norm(normal,axis=1);normal/=area[:,None];E=np.sum(fr*fr,axis=1);F=np.sum(fr*fu,axis=1);G=np.sum(fu*fu,axis=1);L=np.sum(j['Xrr']*normal,axis=1);M=np.sum(j['Xru']*normal,axis=1);N=np.sum(j['Xuu']*normal,axis=1);det=E*G-F*F;mean=(G*L+E*N-2*F*M)/(2*det);gauss=(L*N-M*M)/det;rad=np.sqrt(np.maximum(mean*mean-gauss,0));K=np.maximum(abs(mean+rad),abs(mean-rad));de=E/(1+w*w)-1;df=F/(r*np.sqrt(1+w*w));dg=G/(r*r)-1;mr=np.sqrt((de-dg)**2/4+df*df);metric=np.maximum(abs((de+dg)/2+mr),abs((de+dg)/2-mr))
out=dict(scope=__doc__,lam=a.lam,amplitude_is_target=a.lam==-1,tail_modes=t['parameters']['modes'],tail_sha256=hashlib.sha256(a.tail.read_bytes()).hexdigest(),prefix_sha256=hashlib.sha256(a.prefix.read_bytes()).hexdigest(),alignment=dict(axial_angle=float(np.angle(phase)),translation=shift.tolist()),cut=t['cut'],tail_geometry=dict(actual_metric_max=float(metric.max()),actual_curvature_max=float(K.max()),support_min=float(np.sum(j['X']*normal,axis=1).min()),area_min=float(area.min())),seam_max_norm={n:float(np.linalg.norm(j[n]-q[n],axis=1).max())for n in names},means=dict(prefix_Xr=q['Xr'].mean(0).tolist(),tail_Xr=j['Xr'].mean(0).tolist(),prefix_Xrr=q['Xrr'].mean(0).tolist(),tail_Xrr=j['Xrr'].mean(0).tolist()),limitations=['Tail planar rr uses the saved fourth-order profile finite difference.','Prefix is the full q18 target. A lambda smaller than 1 is not the same prefix and is expected not to match.','A nonzero residual or missing full-tail audit cannot be called a joined closed candidate.'])
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
