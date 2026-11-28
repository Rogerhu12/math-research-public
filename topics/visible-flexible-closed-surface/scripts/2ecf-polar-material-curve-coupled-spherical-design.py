#!/usr/bin/env python3
"""Joint physical 3D material meridian design using true spherical velocity, three-dimensional port closure and Cartesian six-jets."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np
from scipy.integrate import cumulative_simpson
from scipy.interpolate import BSpline,CubicHermiteSpline
from scipy.optimize import minimize

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p);obj=importlib.util.module_from_spec(spec)
    sys.modules[n]=obj;spec.loader.exec_module(obj);return obj

def stores(path,obj):
    with Path(path).open('x') as f:
        json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')

def sphere(phi,beta):
    p,c=np.sin(phi),np.cos(phi)
    b,d=np.sin(beta),np.cos(beta)
    zero=np.zeros_like(p)
    combine=lambda x,y,z:np.stack([x,y,z],axis=-1)
    T=combine(c*d,b,p*d)
    return T,combine(-p*d,zero,c*d),combine(-c*b,d,-p*b),combine(-c*d,zero,-p*d),combine(p*b,zero,-c*b),-T

def local(x,u):
    c,s=np.cos(u),np.sin(u)
    return np.stack([c*x[...,0]+s*x[...,1],-s*x[...,0]+c*x[...,1],x[...,2]],axis=-1)

def world(x,u):
    c,s=np.cos(u),np.sin(u)
    return np.stack([c*x[...,0]-s*x[...,1],s*x[...,0]+c*x[...,1],x[...,2]],axis=-1)

def angular(values,order):
    freq=np.fft.rfftfreq(values.shape[-2],1/values.shape[-2])
    symbol=(1j*freq)**order
    if order%2 and values.shape[-2]%2==0:symbol[-1]=0
    return np.fft.irfft(np.fft.rfft(values,axis=-2)*symbol[:,None],n=values.shape[-2],axis=-2)

def end_module(here,design):
    filename='2ecf-polar-returning-bend-full-ray-surface.py' if 'returningPortSHA256' in design else '2ecf-polar-raised-monotone-oblique-connector.py'
    return load(here/filename,'material_port_supplier')

def ports(ends,amp,flat,u):
    return (ends.base.higher_coast_port(ends.master,.02,u),ends.raised.raised_port(ends.warm,amp,flat,u,.8))

class Model:
    def __init__(self,args,ends,initial,ns,nu):
        self.args=args;self.ends=ends
        self.u=np.arange(nu)*2*np.pi/nu
        self.ns=np.linspace(initial.knots[0],initial.knots[-1],ns)
        self.L=self.ns[-1]-self.ns[0]
        self.t=t=(self.ns-self.ns[0])/self.L
        nkn=args.spans;knots=np.r_[np.zeros(4),np.arange(1,nkn)/nkn,np.ones(4)]
        bs=BSpline(knots,np.eye(len(knots)-4),3)
        self.B=bs(t)[:,2:-2];self.D=bs(t,nu=1)[:,2:-2]/self.L
        self.F=(np.cos(self.u[:,None]*(2*np.arange(args.modes+1))),np.sin(self.u[:,None]*(2*np.arange(1,args.modes+1))))
        self.counts=[b.shape[1]*self.B.shape[1] for b in self.F]
        self.I=cumulative_simpson(np.eye(len(t)),x=t,axis=0,initial=0.)*self.L
        self.S=np.stack([t**3*(10+t*(-15+6*t)),30*t*t*(1-t)**2/self.L,60*t*(1-t)*(1-2*t)/self.L**2])
        po=ports(ends,args.amp,args.flat,self.u)
        self.P0=po[0]['P'];self.P1=po[1]['P']
        vel=[local(p['V'],self.u) for p in po]
        acc=[local(p['A'],self.u) for p in po]
        v=np.array([np.linalg.norm(q,axis=-1) for q in vel])
        vprime=np.array([np.sum(q*k,axis=-1)/sp for q,k,sp in zip(vel,acc,v)])
        phi=[];beta=[];pd=[];bd=[]
        for j,(q,k,sp) in enumerate(zip(vel,acc,v)):
            r,w,z=q.T;ar,aw,az=k.T;h=np.hypot(r,z)
            ph=np.arctan2(z,r)
            phi.append(ph if j==0 else np.pi+np.angle(np.exp(1j*(ph-np.pi))))
            beta.append(np.arctan2(w,h))
            pd.append((r*az-z*ar)/(h*h))
            bd.append((aw-w*vprime[j]/sp)/h)
        def herm(val,der):
            f=CubicHermiteSpline(self.ns[[0,-1]],np.asarray(val),np.asarray(der),axis=0)
            return f(self.ns),f(self.ns,nu=1)
        self.v,self.vd=herm(v,vprime)
        self.base=[herm(phi,pd),herm(beta,bd)]
        self.reference=initial

    def unpack(self,x):
        b=self.B.shape[1]
        return [x[:self.counts[0]].reshape(b,-1),x[self.counts[0]:].reshape(b,-1)]

    def starting(self):
        j=np.concatenate([self.reference.position(self.ns[i:i+6],self.u)[:,1] for i in range(0,len(self.ns),6)])
        q=local(j,self.u);r,w,z=np.moveaxis(q,-1,0)
        old=[np.unwrap(np.arctan2(z,r),axis=0),np.arctan2(w,np.hypot(r,z))]
        coeff=[]
        for val,(base,_),F in zip(old,self.base,self.F):
            c=np.linalg.lstsq(self.B,val-base,rcond=1e-10)[0]
            c=np.linalg.lstsq(F,c.T,rcond=1e-10)[0].T
            coeff.append(c.ravel())
        return np.concatenate(coeff)

    def field(self,x):
        ang=[];der=[]
        for mat,(h,hp),F in zip(self.unpack(x),self.base,self.F):
            angular_coeff=mat@F.T
            ang.append(h+self.B@angular_coeff)
            der.append(hp+self.D@angular_coeff)
        tang=sphere(*ang)
        T,Tp,Tb=tang[:3]
        ps,bs=der
        v=self.v[...,None];vd=self.vd[...,None]
        V=world(v*T,self.u)
        A=world(vd*T+v*(Tp*ps[...,None]+Tb*bs[...,None]),self.u)
        Y=self.P0+np.einsum('ij,juc->iuc',self.I,V,optimize=True)
        delta=self.P1-Y[-1]
        P=Y+self.S[0,:,None,None]*delta
        Vel=V+self.S[1,:,None,None]*delta
        Acc=A+self.S[2,:,None,None]*delta
        return P,Vel,Acc,delta,(tang,der)

    def value(self,x,with_gradient=True):
        P,V,A,delta,(tang,der)=self.field(x)
        jets=np.stack([P,V,angular(P,1),A,angular(V,1),angular(P,2)],axis=1)
        pt=self.point.PointLinearized(jets.swapaxes(1,2),self.rad,self.cfg,self.weights)
        ar=self.area.AreaPacket(jets,self.rad,self.weights['metric'],.5)
        loss=float(np.vdot(pt.residual,pt.residual)+np.vdot(ar.residual,ar.residual))
        repair=float(np.mean(np.sum(delta*delta,axis=-1))*self.args.closure/self.L**2)
        if not with_gradient:
            st=pt.diagnostics() if hasattr(pt,'diagnostics') else {}
            return dict(collocationGeometricObjective=loss,closurePenalty=repair,maxThreeComponentRepair=float(max(np.linalg.norm(delta,axis=-1))),designTotal=loss+repair)
        g=2*pt.vjp(pt.residual).swapaxes(1,2)
        gs,gu=ar.vjp(2*ar.residual);g[:,1]+=gs;g[:,2]+=gu
        bp=g[:,0]-angular(g[:,2],1)+angular(g[:,5],2)
        bv=g[:,1]-angular(g[:,4],1)
        ba=g[:,3]
        bd=np.einsum('s,suc->uc',self.S[0],bp)+np.einsum('s,suc->uc',self.S[1],bv)+np.einsum('s,suc->uc',self.S[2],ba)
        bd+=2*self.args.closure*delta/(len(self.u)*self.L**2)
        bvel=local(np.einsum('ij,iuc->juc',self.I,bp,optimize=True)+bv-self.I[-1,:,None,None]*bd,self.u)
        bacc=local(ba,self.u)
        T,Tp,Tb,Tpp,Tpb,Tbb=tang
        ps,bs=der
        v=self.v[...,None];vd=self.vd[...,None]
        parts=[]
        for F,dT,dTp,dTb in ((self.F[0],Tp,Tpp,Tpb),(self.F[1],Tb,Tpb,Tbb)):
            ga=np.sum(bvel*v*dT+bacc*(vd*dT+v*(dTp*ps[...,None]+dTb*bs[...,None])),axis=-1)
            gd=np.sum(bacc*v*dT,axis=-1)
            parts.append(((self.B.T@ga+self.D.T@gd)@F).ravel())
        return loss+repair,np.concatenate(parts)

class MaterialField:
    def __init__(self,path,ends):
        z=np.load(path);self.coeff=z['coeff'];self.knots=z['knots'];self.ends=ends
        self.amp=float(z['amp']);self.flat=float(z['flat'])
    def position(self,ns,u):
        M=np.arange(self.coeff.shape[-2]);phase=np.exp(1j*M[:,None]*u)
        cell=np.clip(np.searchsorted(self.knots,ns,side='right')-1,0,len(self.knots)-2)
        h=self.knots[cell+1]-self.knots[cell]
        t=(ns-self.knots[cell])/h
        wt=np.array([[self.ends.warm.ports.hermite_weights(x,hh,j) for j in range(3)] for x,hh in zip(t,h)])
        po=ports(self.ends,self.amp,self.flat,u) if np.any((cell==0)|(cell==len(self.knots)-2)) else None
        arr=[]
        names=(('P','Pu','Puu'),('V','Vu','Vuu'),('A','Au','Auu'))
        for side in (0,1):
            idx=cell+side
            c=self.coeff[idx]
            ang=np.stack([np.einsum('nimu,ma->niau',c,phase*(1j*M[:,None])**j,optimize=True).real for j in range(3)],axis=2)
            mask=(idx==0 if side==0 else idx==len(self.knots)-1)
            if np.any(mask):
                ang[mask]=np.stack([np.stack([po[side][key] for key in keys]) for keys in names])
            arr.append(ang)
        full=np.einsum('nki,nijuc->nkjuc',wt,np.concatenate(arr,axis=1))
        return np.stack([full[:,i,j] for i,j in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))],axis=1)

def design(args):
    here=Path(__file__).parent
    old=read(args.seed_design);args.amp=old['amp'];args.flat=old['flat']
    assert sha(args.seed_field)==old['fieldSHA256'] and sha(args.ramp)==old['rampSHA256'] and sha(args.coast)==old['coastSHA256']
    en=end_module(here,old)
    ends=en.Ends(args.scripts,args.ramp,args.coast,args.amp,args.flat,2048)
    op=load(here/'2ecf-polar-raised-physical-ray-field-observe.py','material_seed_ray')
    initial=op.PhysicalRays(args.seed_field,ends)
    warm=Model(args,ends,initial,args.radials,args.angles)
    q=read(args.prepared)
    cache=q['caches']['training'];radpath=Path(cache['files']['radius'])
    assert sha(radpath)==cache['SHA256']['radius']
    rr=np.load(radpath)[:,0]
    idx=np.argsort(cache['nodes'])
    warm.rad=np.interp(warm.ns,np.asarray(cache['nodes'])[idx],rr[idx])[:,None]
    stream=load(args.scripts/'6a65-cartesian-complete-stream.py','material_point_stream')
    warm.point=stream.point
    warm.area=load(args.scripts/'6a65-geometry-area-ratio-power-two.py','material_area')
    warm.cfg=ends.raised.tall_config(stream.point.PointConfig)(**dict(q['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    w=np.ones((len(warm.ns),1));w[[0,-1]]=.5;w/=np.sum(w)*len(warm.u)
    warm.weights=dict(metric=w,geometry=args.geometry*w,curvature=args.curvature*w)
    x=warm.starting()
    v,g=warm.value(x)
    rng=np.random.default_rng(180426)
    d=rng.normal(size=x.shape);d/=np.linalg.norm(d)
    eps=1e-6
    fd=(warm.value(x+eps*d,False)['designTotal']-warm.value(x-eps*d,False)['designTotal'])/(2*eps)
    chk=abs(fd-g@d)/max(1.,abs(fd),abs(g@d))
    if chk>3e-4:raise ArithmeticError(('Actual 3D meridian gradient mismatch',fd,g@d,chk))
    start=warm.value(x,False);history=[]
    def callback(vec):
        row=warm.value(vec,False);history.append(row)
        if len(history)%10==0:print(len(history),row,flush=True)
    opt=minimize(warm.value,x,jac=True,method='L-BFGS-B',callback=callback,options=dict(maxiter=args.iterations,maxls=35,ftol=1e-14,gtol=2e-8,maxcor=18))
    dense=Model(args,ends,initial,args.fine_radials,args.fine_angles)
    P,V,A,delta,_=dense.field(opt.x)
    stride=(len(dense.ns)-1)//args.cells
    assert stride*args.cells==len(dense.ns)-1 and args.stored_modes<args.fine_angles//2
    pieces=np.stack([P[::stride],V[::stride],A[::stride]],axis=1)
    coeff=np.fft.rfft(pieces,axis=2)[:,:,:args.stored_modes+1]/args.fine_angles
    coeff[:,:,1:]*=2
    with args.field.open('xb') as f:
        np.savez_compressed(f,coeff=coeff,knots=dense.ns[::stride],amp=args.amp,flat=args.flat)
    r=dict(schema='coupled-physical-3D-material-meridians-all-jets-v1',entrySHA256=sha(__file__),seedFieldSHA256=sha(args.seed_field),seedDesignSHA256=sha(args.seed_design),endpointEntrySHA256=sha(en.__file__),preparedSHA256=sha(args.prepared),fieldSHA256=sha(args.field),rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),amp=args.amp,flat=args.flat,returningPort=('returningPortSHA256' in old),spans=args.spans,modes=args.modes,storedModes=args.stored_modes,cells=args.cells,controls=len(x),actualAcceptedLBFGSIterations=int(opt.nit),functionEvaluations=int(opt.nfev),termination=str(opt.message),collocationRadials=args.radials,collocationAngles=args.angles,designWeights=dict(closure=args.closure,curvature=args.curvature,geometry=args.geometry),directionalDerivativeError=float(chk),startingDiagnostics=start,history=history,final=warm.value(opt.x,False),denseMaximumRepair=float(max(np.linalg.norm(delta,axis=-1))),coefficients=opt.x.tolist(),finiteOnly=True)
    stores(args.output,r)
    print(r['final'],r['denseMaximumRepair'],opt.message,flush=True)

def observe(args):
    here=Path(__file__).parent;d=read(args.design)
    raw=read(args.seed_design);assert sha(args.seed_design)==d['seedDesignSHA256']
    en=end_module(here,raw)
    engine=load(here/'2ecf-polar-raised-physical-ray-field-observe.py','mat_obs_full')
    old=engine.load
    engine.PhysicalRays=MaterialField
    def supply(path,name):
        if Path(path).name=='2ecf-polar-raised-monotone-oblique-connector.py':return en
        return old(path,name)
    engine.load=supply
    dest=args.output
    with TemporaryDirectory(dir=dest.parent) as temp:
        args.output=Path(temp)/'obs.json';engine.run(args);q=read(args.output)
    q.update(schema='coupled-material-meridian-independent-full-original-physical-observations-v1',materialFieldEntrySHA256=sha(__file__),actualDesignSHA256=sha(args.design),actualSeedDesignSHA256=sha(args.seed_design))
    stores(dest,q)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent'):
        a.add_argument('--'+k,type=Path)
    for k,v in [('angles',96),('radials',65),('spans',12),('modes',8),('iterations',150),('fine-radials',513),('fine-angles',256),('cells',64),('stored-modes',80),('trace-nodes',2048)]:
        a.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',8.),('curvature',.75),('geometry',30.)]:
        a.add_argument('--'+k,type=float,default=v)
    args=a.parse_args();(design if args.mode=='design' else observe)(args)
