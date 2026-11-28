#!/usr/bin/env python3
"""Shoot true material geodesics using a radial normal-curvature control and actual Cartesian port mismatches."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
for i in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[i]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize
def module(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
base=module(here/'2ecf-polar-material-curve-coupled-spherical-design.py','geodesic_material_source')
radius=module(here/'2ecf-polar-material-implicit-coupled-radius.py','geodesic_radius_implementation')
def du(a,o=1):return base.angular(a,o)
def dot(a,b):return np.sum(a*b,axis=-1)
def geometry(P,T):
    D=du(P);W=np.cross(T,D);w=np.linalg.norm(W,axis=-1)
    if np.min(w)<1e-7:raise ArithmeticError('Discrete material immersion lost')
    return D,W/w[...,None],w
def jet(P,T,k):
    D,n,w=geometry(P,T)
    return np.stack([P,T,D,k[...,None]*n,du(T),du(P,2)],axis=1)
def flow(y,k):
    P,T=y
    _,n,_=geometry(P,T)
    return np.stack([T,k[:,None]*n])
def vjp(y,k,b):
    P,T=y;D,n,w=geometry(P,T)
    bn=k[:,None]*b[1];bw=(bn-n*dot(n,bn)[:,None])/w[:,None]
    adj=np.stack([-du(np.cross(bw,T)),b[0]+np.cross(D,bw)])
    return adj,dot(n,b[1])
class Shooting:
    def __init__(self,a,N,radials,ends,ref):
        self.a=a;self.ns=np.linspace(ref.knots[0],ref.knots[-1],radials+1)
        self.N=N;self.step=(self.ns[-1]-self.ns[0])/radials
        self.u=2*np.pi*np.arange(N)/N
        self.half=np.linspace(self.ns[0],self.ns[-1],2*radials+1)
        self.po=base.ports(ends,a.amp,a.flat,self.u)
        self.target=np.stack([self.po[1][k] for k in ('P','V','Pu','A','Vu','Puu')])
        self.y0=np.stack([self.po[0]['P'],self.po[0]['V']])
        d=[];n0=[]
        for first in range(0,len(self.half),12):
            v=ref.position(self.half[first:first+12],self.u)
            n=np.cross(v[:,1],v[:,2]);n/=np.linalg.norm(n,axis=-1,keepdims=True)
            d.append(dot(n,v[:,3])/dot(v[:,1],v[:,1]))
        self.k0=np.concatenate(d)
        knots=np.r_[np.zeros(4),np.arange(1,a.spans)/a.spans,np.ones(4)]
        t=(self.half-self.half[0])/(self.half[-1]-self.half[0])
        self.B=BSpline(knots,np.eye(len(knots)-4),3)(t)[:,1:-1]
        self.C=np.cos(self.u[:,None]*2*np.arange(a.modes+1))
        q=base.read(a.prepared);c=q['caches']['training'];r=Path(c['files']['radius'])
        assert base.sha(r)==c['SHA256']['radius']
        ind=np.argsort(c['nodes']);f=np.interp(self.ns,np.array(c['nodes'])[ind],np.load(r)[:,0][ind])
        g=base.read(a.frozen);alpha=g['logRadiusCoefficients'];self.targetSHA256=g['targetSHA256']
        assert radius.target_hash(g['radiusSpans'],alpha,self.ns[0],self.ns[-1])==self.targetSHA256
        self.f=(f*np.exp(radius.radius_basis(t[::2],g['radiusSpans'])@alpha))[:,None]
        stream=module(a.scripts/'6a65-cartesian-complete-stream.py','geodesic_physical_point')
        self.point=stream.point;self.area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','geodesic_area')
        self.cfg=ends.raised.tall_config(self.point.PointConfig)(**dict(q['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
        w=np.ones((len(self.ns),1))/(N*radials);w[[0,-1]]*=.5
        self.weights=dict(metric=w,curvature=w*a.curvature,geometry=w*a.geometry)
        self.port_weights=np.array([a.position,a.velocity,.45*a.position,.008*a.velocity,.05*a.velocity,.008*a.position])
    def field(self,x):
        param=x.reshape(self.B.shape[1],self.C.shape[1])
        kval=self.k0+(self.B@param)@self.C.T
        path=[self.y0];mid=[]
        for i in range(len(self.ns)-1):
            y=path[-1];half=y+.5*self.step*flow(y,kval[2*i])
            path.append(y+self.step*flow(half,kval[2*i+1]));mid.append(half)
        Y=np.stack(path);return Y,np.array(mid),kval
    def value(self,x,gradient=True):
        Y,mid,kval=self.field(x);P,T=Y[:,0],Y[:,1]
        j=jet(P,T,kval[::2])
        pt=self.point.PointLinearized(j.swapaxes(1,2),self.f,self.cfg,self.weights)
        ar=self.area.AreaPacket(j,self.f,self.weights['metric'],.5)
        dif=j[-1]-self.target
        phys=float(np.vdot(pt.residual,pt.residual)+np.vdot(ar.residual,ar.residual))
        end=float(np.sum(self.port_weights[:,None]*dot(dif,dif))/self.N)
        penalty=self.a.reg*np.mean(x*x)
        loss=phys+end+penalty
        if not gradient:return dict(physical=phys,endpoint=end,regularizer=penalty,total=loss,rawEndMax=[float(z) for z in np.max(np.linalg.norm(dif,axis=-1),axis=1)],rawE=float(np.max(abs(pt.metric[...,0]))),rawMixedNormalized=float(np.max(abs(pt.metric[...,1])/np.sqrt(2))),rawG=float(np.max(abs(pt.metric[...,2]))),minJacobian=float(np.min(pt.curvature['w'])))
        g=2*pt.vjp(pt.residual).swapaxes(1,2);gs,gu=ar.vjp(2*ar.residual);g[:,1]+=gs;g[:,2]+=gu
        g[-1]+=2*self.port_weights[:,None,None]*dif/self.N
        D,n,w=geometry(P,T);bg=kval[::2,:,None]*g[:,3]
        bw=(bg-n*dot(n,bg)[...,None])/w[...,None]
        bp=g[:,0]-du(g[:,2])+du(g[:,5],2)-du(np.cross(bw,T))
        bt=g[:,1]-du(g[:,4])+np.cross(D,bw)
        bk=np.zeros_like(kval);bk[::2]=dot(n,g[:,3])
        bar=np.stack([bp[-1],bt[-1]])
        for i in reversed(range(len(mid))):
            bmid,bs=vjp(mid[i],kval[2*i+1],self.step*bar);bk[2*i+1]+=bs
            bleft,bs=vjp(Y[i],kval[2*i],.5*self.step*bmid);bk[2*i]+=bs
            bar+=bmid+bleft+np.stack([bp[i],bt[i]])
        grad=(self.B.T@bk@self.C).ravel()+2*self.a.reg*x/len(x)
        return loss,grad

def design(a):
    donor=base.read(a.donor);seed=base.read(a.seed_design);assert donor['fieldSHA256']==base.sha(a.input_field)
    en=base.end_module(here,seed);a.amp=seed['amp'];a.flat=seed['flat']
    ends=en.Ends(a.scripts,a.ramp,a.coast,a.amp,a.flat,2048)
    ref=base.MaterialField(a.input_field,ends)
    mdl=Shooting(a,a.angles,a.radials,ends,ref)
    x=np.zeros(mdl.B.shape[1]*mdl.C.shape[1]);start=mdl.value(x,False)
    loss,g=mdl.value(x);d=np.random.default_rng(17063).normal(size=len(x));d/=np.linalg.norm(d);eps=1e-6
    fd=(mdl.value(x+eps*d,False)['total']-mdl.value(x-eps*d,False)['total'])/(2*eps)
    error=abs(fd-g@d)/max(1.,abs(fd),abs(g@d))
    if error>3e-4:raise ArithmeticError(('Actual geodesic adjoint failed',fd,g@d,error))
    hist=[]
    def cb(x):
        q=mdl.value(x,False);hist.append(q)
        if len(hist)%10==0:print(len(hist),q,flush=True)
    opt=minimize(mdl.value,x,jac=True,method='L-BFGS-B',callback=cb,options=dict(maxiter=a.iterations,maxls=30,maxcor=15,ftol=1e-12,gtol=1e-7))
    dense=Shooting(a,a.fine_angles,a.fine_radials,ends,ref)
    raw=dense.value(opt.x,False);Y,_,k=dense.field(opt.x);X,T=Y[:,0],Y[:,1];J=jet(X,T,k[::2])
    dep=np.stack([dense.target[i]-J[-1,i] for i in (0,1,3)])
    b,S=dense.ns[[0,-1]];L=S-b
    wt=np.stack([[ends.warm.ports.hermite_weights((s-b)/L,L,j)[3:] for j in range(3)] for s in dense.ns])
    fix=np.einsum('sji,iuc->sjuc',wt,dep)
    pva=J[:,[0,1,3]]+fix
    stride=a.fine_radials//a.cells;assert stride*a.cells==a.fine_radials and a.stored_modes<a.fine_angles//2
    co=np.fft.rfft(pva[::stride],axis=2)[:,:,:a.stored_modes+1]/a.fine_angles;co[:,:,1:]*=2
    with a.field.open('xb') as f:np.savez_compressed(f,coeff=co,knots=dense.ns[::stride],amp=a.amp,flat=a.flat)
    frozen=base.read(a.frozen)
    base.stores(a.output,dict(schema='material-geodesic-normal-curvature-shoot-and-actual-end-PVA-repair-v1',entrySHA256=base.sha(__file__),donorSHA256=base.sha(a.donor),seedDesignSHA256=base.sha(a.seed_design),inputFieldSHA256=base.sha(a.input_field),fieldSHA256=base.sha(a.field),rampSHA256=base.sha(a.ramp),coastSHA256=base.sha(a.coast),preparedSHA256=base.sha(a.prepared),amp=a.amp,flat=a.flat,sourceType='Cartesian physical material Fourier Hermite, after endpoint repair',targetSHA256=mdl.targetSHA256,radiusSpans=frozen['radiusSpans'],logRadiusCoefficients=frozen['logRadiusCoefficients'],controls=len(x),coefficients=opt.x.tolist(),actualAccepted=int(opt.nit),adjointFiniteDifference=float(error),trainingStarts=start,trainingFinal=mdl.value(opt.x,False),rawDenseBeforeRepair=raw,maximumPVARepair=[float(z) for z in np.max(np.linalg.norm(fix,axis=-1),axis=(0,2))],history=hist,termination=str(opt.message),finiteOnly=True))
    print('dense',raw,flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','seed-design','donor','input-field','frozen','field','output'):p.add_argument('--'+k,type=Path,required=True)
    for k,v in [('angles',48),('radials',64),('spans',7),('modes',4),('iterations',65),('fine-angles',128),('fine-radials',192),('cells',96),('stored-modes',55)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('position',150.),('velocity',15.),('reg',1e-5),('geometry',5.),('curvature',.5)]:p.add_argument('--'+k,type=float,default=v)
    design(p.parse_args())
