#!/usr/bin/env python3
"""Construct jointly sampled real polar coordinates from the complete field, including signed endpoints and every angular meridian."""
import argparse,importlib.util,json,os
from fractions import Fraction
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import CubicHermiteSpline
p=Path(__file__).with_name('2ecf-r289-physical-query.py');sp=importlib.util.spec_from_file_location('r289_actual_meridians',p);Q=importlib.util.module_from_spec(sp);sp.loader.exec_module(Q)
def collect(g,rows,n,bare=False):
    u=np.linspace(0,np.pi/2,n);theta=u.copy();out=np.empty((len(rows),n,5))
    for i in range(0,len(rows),32):
        fit=g.m.Fit(g.src,rows[i:i+32],u,g.eps,g.d['spans'],g.d['modes']);J=g.mod.k.OldFit.field(fit,g.x) if bare else fit.field(g.x);P,S,U=J[:,0],J[:,1],J[:,2]
        for k,(p,s,v) in enumerate(zip(P,S,U)):
            r=np.hypot(p[:,0],p[:,1]);ph=np.arctan2(p[:,1],p[:,0]);ph[[0,-1]]=theta[[0,-1]]
            tu=(p[:,0]*v[:,1]-p[:,1]*v[:,0])/r**2;ts=(p[:,0]*s[:,1]-p[:,1]*s[:,0])/r**2;assert np.all(np.diff(ph)>0) and min(tu)>.05
            rs=(p[:,:2]*s[:,:2]).sum(axis=-1)/r;ru=(p[:,:2]*v[:,:2]).sum(axis=-1)/r
            f=CubicHermiteSpline(ph,np.stack([r,p[:,2],u],axis=1),np.stack([ru,v[:,2],np.ones_like(u)],axis=1)/tu[:,None]);out[i+k,:,:3]=f(theta);out[i+k,:,3]=np.interp(theta,ph,rs-ru*ts/tu);out[i+k,:,4]=np.interp(theta,ph,s[:,2]-v[:,2]*ts/tu)
    return theta,out
def section_stats(s,theta,V):
    keep=np.r_[True,np.diff(s)>2e-12];s=s[keep];V=V[keep];counts=[];first=None;maximum=0.
    for j,th in enumerate(theta):
        pts=V[:,j,:2];X=pts[:-1];Y=pts[1:];D=Y-X;mn=np.minimum(X,Y);mx=np.maximum(X,Y)
        hit=(mx[:,None,0]>=mn[None,:,0])&(mn[:,None,0]<=mx[None,:,0])&(mx[:,None,1]>=mn[None,:,1])&(mn[:,None,1]<=mx[None,:,1])
        ia,ib=np.where(np.triu(hit,3));ok=s[ib]-s[ia]>5e-7;ia=ia[ok];ib=ib[ok];cr=lambda a,b:a[:,0]*b[:,1]-a[:,1]*b[:,0]
        den=cr(D[ia],D[ib]);ok=np.abs(den)>1e-23;ia=ia[ok];ib=ib[ok];den=den[ok];v=X[ib]-X[ia];ta=cr(v,D[ib])/den;tb=cr(v,D[ia])/den;ok=(ta>=0)&(ta<=1)&(tb>=0)&(tb<=1);ia=ia[ok];ib=ib[ok];ta=ta[ok];total=len(ia)
        if total:
            k=np.argmax(s[ib]-s[ia]);a=ia[k];b=ib[k];d=s[b]-s[a]
            if d>maximum:
                maximum=d;first=dict(theta=float(th),rows=[int(a),int(b)],sBrackets=[[s[a],s[a+1]],[s[b],s[b+1]]],rz=(X[a]+ta[k]*D[a]).tolist(),materialU=[V[a,j,2],V[b,j,2]])
        counts.append(total)
    return dict(rows=len(s),angular=len(theta),selfIntersectionTotal=sum(counts),positiveAngleRows=int(np.count_nonzero(counts)),largestMaterialSeparation=maximum,worst=first)
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','meridian','buffer','tail-table','tail','state','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--radial',type=int,default=420);p.add_argument('--angular',type=int,default=161);a=p.parse_args();g=Q.Field(a.scripts,a.meridian,a.buffer,a.tail_table,a.state,Fraction(json.loads(a.tail.read_bytes())['scale']));rows,_=g.src.grid(a.radial,16,True);theta,V=collect(g,rows,a.angular);z=section_stats(rows[:,0],theta,V);z.update(cuffHeight=g.cutZ,capAboveRadiusMinimum=float(np.min(V[:,:,0][V[:,:,1]>g.cutZ+2e-8],initial=np.inf)));np.savez_compressed(a.out.with_suffix('.npz'),s=rows[:,0],rows=rows,theta=theta,physical=V);z['sampledMeridians']=g.m.base.sha(a.out.with_suffix('.npz'));z['stateSHA256']=g.m.base.sha(a.state)
    with a.out.open('x') as f:json.dump(z,f,indent=2);f.write('\n')
    print(z)
if __name__=='__main__':main()
