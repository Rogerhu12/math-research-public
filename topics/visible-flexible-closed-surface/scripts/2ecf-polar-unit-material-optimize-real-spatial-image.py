#!/usr/bin/env python3
"""Optimize true post-map metric, shape operator and geometry in all original physical coordinates."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np
def module(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
radius=module(here/'2ecf-polar-material-implicit-coupled-radius.py','physical_image_radius')
base=radius.base;imp=radius.impl
sphere=module(here/'2ecf-polar-material-spatial-guard-true-spheres.py','physical_image_true_spheres')
class Image(radius.Designed):
    def value(self,x,with_gradient=True):
        P,V,A,delta,stuff=self.field(x)
        j=np.stack([P,V,base.angular(P,1),A,base.angular(V,1),base.angular(P,2)],axis=1)
        if not hasattr(self,'real_radius'):self.real_radius=self.rad*np.exp(self.BR@self.alpha0)[:,None]
        total=0.;gx=[];extreme=0.;kmax=0.;held=1e3
        for start in range(0,len(self.ns),12):
            sl=slice(start,start+12)
            if with_gradient:J,pull=sphere.transform(j[sl],self.ends.master.A,self.args.eps,True)
            else:J=sphere.transform(j[sl],self.ends.master.A,self.args.eps)
            f=self.real_radius[sl];w={key:v[sl] for key,v in self.weights.items()}
            pt=self.point.PointLinearized(J.swapaxes(1,2),f,self.cfg,w)
            ar=self.area.AreaPacket(J,f,w['metric'],.5)
            total+=np.vdot(pt.residual,pt.residual)+np.vdot(ar.residual,ar.residual)
            extreme=max(extreme,float(np.max(abs(pt.metric))));kmax=max(kmax,float(np.max(abs(pt.curvature['eigenvalues']))));held=min(held,float(np.min(pt.geometry['held_distance'])))
            if with_gradient:
                g=2*pt.vjp(pt.residual).swapaxes(1,2);gs,gu=ar.vjp(2*ar.residual)
                g[:,1]+=gs;g[:,2]+=gu;gx.append(pull(g))
        if not with_gradient:
            return dict(collocationGeometricObjective=float(total),designTotal=float(total),closurePenalty=0.,maxThreeComponentRepair=0.,postMapMetricComponentMax=extreme,postMapCurvatureMax=kmax,postMapHeld=held,**self.last)
        g=np.concatenate(gx)
        bp=g[:,0]-base.angular(g[:,2],1)+base.angular(g[:,5],2)
        bv=g[:,1]-base.angular(g[:,4],1)
        bV=base.local(np.einsum('ij,iuc->juc',self.I,bp,optimize=True)+bv,self.u)
        bA=base.local(g[:,3],self.u)
        tang,der,U,q,Qs,Us,H,h,hp=stuff
        bUs=self.v[...,None]*bA
        bU=self.v[...,None]*bV+self.vd[...,None]*bA-(bUs*imp.dot(U,Qs)[...,None]+Qs*imp.dot(bUs,U)[...,None])/q[...,None]
        bQ=imp.Japply(U,q,bU)-U*(imp.dot(bUs,Us)/q)[...,None]
        bQs=imp.Japply(U,q,bUs)
        multiplier=np.linalg.solve(H,np.sum(h*bQ+hp*bQs,axis=0)[...,None])[...,0]
        bT=bQ-(self.I[-1,:,None]*self.v)[...,None]*imp.Japply(U,q,multiplier[None])
        T,Tp,Tb,Tpp,Tpb,Tbb=tang;ps,bs=der;parts=[]
        for F,dT,dTp,dTb in ((self.F[0],Tp,Tpp,Tpb),(self.F[1],Tb,Tpb,Tbb)):
            ga=imp.dot(bT,dT)+imp.dot(bQs,dTp*ps[...,None]+dTb*bs[...,None]);gd=imp.dot(bQs,dT)
            parts.append(((self.B.T@ga+self.D.T@gd)@F).ravel())
        return float(total),np.concatenate(parts)

def run(a):
    if not .01<=a.eps<=.07:raise ValueError('Certified sphere transition rectangle required')
    dest=a.output;radius.Designed=Image
    if a.mode=='observe':sphere.observe(a);return
    assert a.frozen is not None and a.start is not None
    with TemporaryDirectory(dir=dest.parent) as temp:
        q=Path(temp)/'design.json';a.output=q;radius.design(a);data=base.read(q)
    data.update(physicalImageSolverSHA256=base.sha(__file__),physicalSpatialMapSHA256=base.sha(sphere.__file__),epsilon=a.eps,fieldArchiveContainsPreimage=True,completePhysicalImageObtainedByApplyingGuard=True)
    base.stores(dest,data)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent','start','frozen'):p.add_argument('--'+k,type=Path)
    for k,v in [('angles',96),('radials',97),('spans',24),('modes',12),('iterations',240),('fine-radials',769),('fine-angles',320),('cells',96),('stored-modes',100),('trace-nodes',2048),('radius-spans',12)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',0.),('curvature',2.),('geometry',60.),('eps',.05)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
