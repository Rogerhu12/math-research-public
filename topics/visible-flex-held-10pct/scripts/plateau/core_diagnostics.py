import json,math,argparse
from pathlib import Path
import numpy as np
from plateau_core import PlateauSupportCore
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args()
report={'scope':'Exact-core geometry, derivative checks and finite Fourier moment control ranks. Not a solved prefix or a closure proof.','geometries':[],'ranks':[],'derivative_checks':[]}
for R,a,b in [(.8,.2,.1),(.5,.6,.1),(.5,.9,.05),(.25,.6,.1),(.2,.5,.05),(2,.45,.05),(2,.3,.1),(3,.2,.1)]:
 q=abs(R-1)/8;center=0. if R<1 else np.pi/3;c=PlateauSupportCore(q,np.zeros(7),halfwidth=a,transition=b,center=center)
 phi=np.array([center]);g=c.normal_geometry(phi);C=(g['F']-R*g['er'])[0]
 row=c.summary()|dict(circle_center=C.tolist(),circle_center_norm=float(np.linalg.norm(C)))
 # Counter-held axis displacement for the expressly named trial phase widths.
 row['counter_hold_axis_displacements']={str(A):float(2*np.linalg.norm(C)*math.sin(A/(2*R))) for A in [.12,.2,.3]}
 report['geometries'].append(row)
for a in [.2,.3,.6,.8,.9]:
 for M in [4,8,12,16,24,32]:
  c=PlateauSupportCore(.01,np.zeros(M-1),halfwidth=a,transition=min(.05,(np.pi/3-a)/2),arc_nodes=128)
  z,w=np.polynomial.legendre.leggauss(max(128,4*M));phi=c.center+c.a+(z+1)*c.L/2
  f=c._basis(phi)[0];m=3*np.arange(2,M+1)
  matrix=(2/c.T)*m[:,None]*(np.sin(m[:,None]*phi[None,:])*w[None,:])@f.T*c.L/2
  sv=np.linalg.svd(matrix,compute_uv=False);cn=np.linalg.norm(matrix,axis=0);normed=matrix/cn[None,:];sn=np.linalg.svd(normed,compute_uv=False)
  report['ranks'].append(dict(halfwidth=a,normal_width=2*a,M=M,sigma_min=float(sv[-1]),sigma_max=float(sv[0]),condition=float(sv[0]/sv[-1]),column_normalized_sigma_min=float(sn[-1]),column_normalized_condition=float(sn[0]/sn[-1]),rank_tol_1e12=int(np.sum(sv>sv[0]*1e-12))))
c=PlateauSupportCore(.025,[.001,-.0007,.0005],halfwidth=.2);theta=np.linspace(0,2*np.pi,129,endpoint=False);J=c.parameter_derivatives(theta);h=1e-6
for j in range(4):
 q=c.q;coef=np.array(c.c);v=np.r_[q,coef];vp=v.copy();vm=v.copy();vp[j]+=h;vm[j]-=h
 plus=PlateauSupportCore(vp[0],vp[1:],halfwidth=.2).evaluate(theta)['F'];minus=PlateauSupportCore(vm[0],vm[1:],halfwidth=.2).evaluate(theta)['F'];num=(plus-minus)/(2*h)
 report['derivative_checks'].append(dict(parameter=j,max_error=float(np.linalg.norm(num-J[j],axis=1).max())))
args.out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'geometries':[{k:r[k] for k in ['plateau_radius_at_one','plateau_normal_width','circle_center_norm','curvature_max_sample','counter_hold_axis_displacements']}for r in report['geometries']], 'ranks':[r for r in report['ranks']if r['M']in [8,16,32]],'derivative_checks':report['derivative_checks']},indent=2))
