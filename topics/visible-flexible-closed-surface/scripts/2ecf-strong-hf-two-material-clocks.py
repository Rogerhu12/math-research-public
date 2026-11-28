#!/usr/bin/env python3
"""A true two-variable material map on the new positive-length metric and full HF64M80 geometry."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy import sparse
from scipy.interpolate import BSpline
from scipy.optimize import linprog

def load(p,name):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
hf=load(Path(__file__).with_name("2ecf-strong-hf-diagonal-clock.py"),"newdiag")
c=hf.c
PAIRS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
POLY=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])
class Wave:
    def __init__(self,knots,modes,sine):
        self.knots=np.array(knots);n=len(knots)-6
        self.B=BSpline(knots,np.eye(n)[:,3:-3],5,extrapolate=False)
        self.nr=n-6;self.k=np.array(modes);self.sine=sine;self.n=self.nr*len(self.k)
    def angular(self,u,j):
        w=np.asarray(u)[...,None]*self.k
        return self.k**j*(np.sin(w+j*np.pi/2) if self.sine else np.cos(w+j*np.pi/2))
    def tensor(self,x,u,v,ri,aj):
        return (self.B(x,nu=ri)@v.reshape(self.nr,-1))@self.angular(u,aj).T
    def paired(self,x,u,v):
        return [np.sum((self.B(x,nu=i)@v.reshape(self.nr,-1))*self.angular(u,j),axis=1) for i,j in PAIRS]
    def matrix(self,x,u,ri,aj):
        return (self.B(x,nu=ri)[:,:,None]*self.angular(u,aj)[:,None,:]).reshape(len(x),self.n)
    def der_control(self):
        eye=np.eye(self.n).reshape(self.nr,len(self.k),self.n)
        full=np.pad(eye,((3,3),(0,0),(0,0)))
        return 5*np.diff(full,axis=0)/(self.knots[6:-1]-self.knots[1:-6])[:,None,None]
    def bounds(self,v):
        coef=v.reshape(self.nr,-1)
        return float(np.max(np.sum(abs(np.tensordot(self.der_control(),v,axes=([2],[0]))),axis=1))),float(np.max(abs(coef)@self.k))

def chain(jets,r,u):
    X,R,U,A,B,C=jets
    rx,ru,rxx,rxu,ruu=r[1:];ux,uu,uxx,uxu,uuu=u[1:]
    col=lambda x:x[:,None]
    first=lambda a,b:col(a)*R+col(b)*U
    second=lambda a,b,e,f,g,h:col(a*e)*A+col(a*f+b*e)*B+col(b*f)*C+first(g,h)
    return (X,first(rx,ux),first(ru,uu),second(rx,ux,rx,ux,rxx,uxx),
        second(rx,ux,ru,uu,rxu,uxu),second(ru,uu,ru,uu,ruu,uuu))

class ArbitraryHF:
    def __init__(self,args):
        data=np.load(args.field);self.T=data["knots"];self.Z=data["coefficients"];self.m=np.arange(self.Z.shape[2])
        self.ws=BSpline(data["Wknots"],np.pad(data["physicalW"],((3,3),(0,0))),5,extrapolate=False)
        raw=load(args.scripts/"6a65-geometry-nonfold-polar-connector.py","fresh_angular_ports")
        self.ports=raw.NonfoldPolarConnector(args.scripts,args.ramp,args.coast).providers
        state=json.loads(args.angular_clock.read_text())
        self.orig=Wave(state["radialKnots"],state["frequencies"],False)
        self.ao=np.asarray(state["coefficients"])
    def base(self,x,u):
        idx=np.minimum(np.maximum(np.searchsorted(self.T,x,side="right")-1,0),len(self.T)-2)
        h=self.T[idx+1]-self.T[idx];t=(x-self.T[idx])/h
        phase=np.exp(1j*u[:,None]*self.m)
        T=np.zeros((len(x),2,3,3,3))
        for side in (0,1):
            ind=idx+side
            inside=(ind!=0)&(ind!=len(self.T)-1)
            co=self.Z[ind[inside]]
            for j in (0,1,2):
                T[inside,side,:,j,:]=np.einsum("nm,nrmc->nrc",phase[inside]*(1j*self.m)**j,co,optimize=True).real
            for pos,pix in ((0,0),(len(self.T)-1,1)):
                m=ind==pos
                if np.any(m):
                    exact=self.ports[pix](np.mod(u[m],2*np.pi))
                    T[m,side]=np.stack([np.stack([exact[k+"u"*j] for j in range(3)],axis=1) for k in ("P","V","A")],axis=1)
        T=T.reshape(len(x),6,3,3)
        wave=u[:,None]*np.arange(1,25)
        trig=[]
        for j in range(3):
            f=np.ones((len(x),49));f[:,0]=float(j==0)
            f[:,1::2]=np.arange(1,25)**j*np.cos(wave+j*np.pi/2)
            f[:,2::2]=np.arange(1,25)**j*np.sin(wave+j*np.pi/2)
            trig.append(f)
        positions=[]
        for i,j in PAIRS:
            # Factorials here are exact integers. Keep multiplication in real arithmetic.
            powers=np.stack([t**(a-i)*(math.factorial(a)//math.factorial(a-i)) for a in range(i,6)],axis=-1)
            W=(powers@POLY[:,i:].T)*h[:,None]**(np.arange(6)%3-i)
            value=np.einsum("nl,nlc->nc",W,T[:,:,j],optimize=True)
            value+=np.einsum("nck,nk->nc",self.ws(x,nu=i).reshape(len(x),3,49),trig[j],optimize=True)
            positions.append(value)
        return positions
    def original(self,x,u):
        x=np.asarray(x);u=np.asarray(u)
        shift=self.orig.paired(x,u,self.ao)
        shift[0]+=x;shift[1]+=1
        original_angle=[u,np.zeros_like(x),np.ones_like(x),np.zeros_like(x),np.zeros_like(x),np.zeros_like(x)]
        src=self.base(np.clip(shift[0],self.T[0],self.T[-1]),u)
        return chain(src,shift,original_angle)
    def actual(self,x,u,p,q,pv,qv):
        x,u=np.broadcast_arrays(x[:,None],u[None,:]);shape=x.shape
        x=x.ravel();u=u.ravel();ans=np.empty((len(x),6,3))
        for i in range(0,len(x),256):
            sl=slice(i,i+256);xx=x[sl];uu=u[sl]
            px=p.paired(xx,uu,pv);qx=q.paired(xx,uu,qv)
            px[0]+=xx;px[1]+=1;qx[0]+=uu;qx[2]+=1
            base=self.original(np.clip(px[0],self.T[0],self.T[-1]),qx[0])
            ans[sl]=np.stack(chain(base,px,qx),axis=1)
        return ans.reshape(*shape,6,3).swapaxes(1,2)

def train(groups,p,q,clock,basis,ca):
    cls=[];br=[];n=p.n+q.n
    for wave,maxdx,offset in ((p,.18,0),(q,2.5,p.n)):
        der=wave.der_control().reshape(-1,wave.n)
        D=np.zeros((len(der),n));D[:,offset:offset+wave.n]=der
        cls.append(sparse.csr_matrix(np.c_[np.r_[D,-D],np.zeros(2*len(D))]))
        br.append(np.full(2*len(D),maxdx/len(wave.k)))
    info=[];points={}
    for name in ("training","observer"):
        inp=groups[name];cache=inp["cache"]
        ix=np.flatnonzero((cache.nodes>=basis.c)&(cache.nodes<=basis.end))
        x=cache.nodes[ix];u=cache.u
        _,h,_=clock.jets(x);h=h[:,None]
        a=hf.d.radius_jets(inp["radius"],basis,ca)[ix,0,None]
        X,V,U,SS,SU,UU=inp["jets"][ix].swapaxes(0,1)
        dot=lambda a,b:np.sum(a*b,axis=-1)
        E,F,G=dot(V,V),dot(V,U),dot(U,U)
        d0=np.stack((E/h**2-1,F/(h*a),G/a**2-1),axis=-1)
        J=np.stack([np.stack(t,axis=-1) for t in [
            (2*dot(V,SS)/h**2,(dot(SS,U)+dot(V,SU))/(h*a),2*dot(U,SU)/a**2),
            (2*E/h**2,F/(h*a),np.zeros_like(G)),(np.zeros_like(E),E/(h*a),2*F/a**2),
            (2*dot(V,SU)/h**2,(dot(SU,U)+dot(V,UU))/(h*a),2*dot(U,UU)/a**2),
            (2*F/h**2,G/(h*a),np.zeros_like(G)),(np.zeros_like(E),F/(h*a),2*G/a**2)]],axis=2)
        points[name]=(x,u,d0,J)
    v=np.zeros(n)
    for it in range(9):
        maxerror=0.
        for name,(x,u,d0,J) in points.items():
            shapes=[w.tensor(x,u,vec,i,j) for w,vec in ((p,v[:p.n]),(q,v[p.n:])) for i,j in PAIRS[:3]]
            distort=d0+np.einsum("rujg,ruj->rug",J,np.stack(shapes,axis=-1),optimize=True)
            E,F,G=distort.transpose(2,0,1);tr=(E+G)/2;rad=np.hypot((E-G)/2,F);err=abs(tr)+rad
            maxerror=max(maxerror,float(err.max()))
            selected=[]
            for ids in np.array_split(np.arange(len(x)),48):
                hot=np.argpartition(err[ids].ravel(),-4)[-4:]
                selected.extend((ids[i//len(u)],i%len(u)) for i in hot)
            hot=np.argpartition(err.ravel(),-180)[-180:];selected.extend(zip(*np.unravel_index(hot,err.shape)))
            ir,iu=np.unique(np.asarray(selected),axis=0).T
            e=E[ir,iu];f=F[ir,iu];g=G[ir,iu];r=rad[ir,iu]
            sign=np.where(tr[ir,iu]>=0,1.,-1.)
            cos2=sign*(e-g)/(2*np.maximum(r,1e-30));sin2=sign*f/np.maximum(r,1e-30)
            direction=np.column_stack(((1+cos2)/2,sin2,(1-cos2)/2))
            scalar=np.einsum("ij,ikj->ik",direction,J[ir,iu])
            base=sign*np.sum(direction*d0[ir,iu],axis=1)
            matrices=[]
            for k,w in enumerate((p,q)):
                matrices.append(sum((scalar[:,3*k+a,None]*w.matrix(x[ir],u[iu],i,j) for a,(i,j) in enumerate(PAIRS[:3]))))
            jac=sign[:,None]*np.hstack(matrices)
            cls.append(sparse.csr_matrix(np.c_[jac,-np.ones(len(ir))]));br.append(-base)
        if it and maxerror<info[-1]["lp"]+.00015:break
        res=linprog(np.r_[np.zeros(n),1.],A_ub=sparse.vstack(cls,format="csr"),b_ub=np.concatenate(br),
            bounds=[(-.0015,.0015)]*p.n+[(-.009,.009)]*q.n+[(0.,1.)],method="highs")
        if not res.success:raise ArithmeticError(res.message)
        v=res.x[:-1]
        info.append(dict(it=it,lp=float(res.x[-1]),previousFullLinearMax=maxerror))
        print(json.dumps(info[-1]),flush=True)
    return v[:p.n],v[p.n:],info

def main(args):
    tic=time.monotonic()
    saved,definition,basis,mods,groups,basecheck=hf.build(args)
    target=json.loads(args.diagonal.read_text())
    spec=target["definition"]
    if spec["basePositionFile"]!=c.sha(args.field) or spec["baseAngleClock"]!=c.sha(args.angular_clock) or target["definitionSHA256"]!=c.stable(spec):
        raise ValueError("Actual fixed HF diagonal new physical metric required")
    ce=np.array([float.fromhex(v) for v in spec["CEradialHex"]]);ca=np.array([float.fromhex(v) for v in spec["CGangularHex"]])
    clk=hf.d.SquareClock(basis,ce)
    arb=ArbitraryHF(args);p=Wave(arb.orig.knots,range(0,10,2),False);q=Wave(arb.orig.knots,range(2,12,2),True)
    pv,qv,history=train(groups,p,q,clk,basis,ca)
    pd,pu=p.bounds(pv);qd,qu=q.bounds(qv)
    determinant=(1-pd)*(1-qu)-pu*qd
    if determinant<=0 or pd>=1 or qu>=1:raise ArithmeticError("Entire two-dimensional clock orientation not established")
    baseline_jets={n:g["jets"] for n,g in groups.items()}
    def observe(factor,names):
        local={n:dict(groups[n]) for n in names}
        for n,group in local.items():
            x=group["cache"].nodes;u=group["cache"].u
            ix=np.flatnonzero((x>=basis.c)&(x<=basis.end))
            jet=baseline_jets[n].copy()
            if factor:
                for j in range(0,len(ix),12):
                    sl=ix[j:j+12]
                    jet[sl]=arb.actual(x[sl],u,p,q,factor*pv,factor*qv)
            group["jets"]=jet
        _,cache=hf.physical(args,local,basis,ce,ca)
        return hf.sample(cache,mods,saved,definition,clk,args)
    # A full chart comparison samples interior, both boundary cells, and both exact endpoints.
    test=groups["training"];x=test["cache"].nodes;u=test["cache"].u
    idx=np.flatnonzero((x>=basis.c)&(x<=basis.end));take=idx[np.unique(np.r_[0,1,2,4,np.linspace(0,len(idx)-1,10,dtype=int),-3,-2,-1])]
    err=np.max(abs(arb.actual(x[take],u,p,q,0*pv,0*qv)-baseline_jets["training"][take]),axis=(0,2,3))
    if max(err)>3e-7:raise ArithmeticError(("True arbitrary-angle identity consumer differs",err))
    print("zero-consumer six jets",err.tolist(),flush=True)
    rows=[dict(factor=0.,G10={k:target["stats"][k] for k in ("training","observer")})]
    for factor in (1.,.5,.25):
        grp=observe(factor,("training","observer"))
        rows.append(dict(factor=factor,G10=grp))
        print(json.dumps(dict(factor=factor,G10=max(z["metric"] for z in grp.values()),cost=sum(z["original"] for z in grp.values()))),flush=True)
    peak=lambda r:max(z["metric"] for z in r["G10"].values())
    cost=lambda r:sum(z["original"] for z in r["G10"].values())
    good=[i for i in range(1,len(rows)) if peak(rows[i])<peak(rows[0]) and cost(rows[i])<cost(rows[0])]
    chosen=min(good,key=lambda i:peak(rows[i])) if good else 0
    independent=observe(rows[chosen]["factor"],("independent",))["independent"]
    out=dict(schema="new-physical-HF-full-two-dimensional-material-clock-v1",entry=c.sha(__file__),target=c.sha(args.diagonal),
        fixedMetric=target["definitionSHA256"],baseField=c.sha(args.field),baseAngleClock=c.sha(args.angular_clock),
        exactEndpoints="original Gamma95 and R205 providers freshly evaluated at displaced material angles in boundary cells",
        pCoefficientHex=[float(z).hex() for z in pv],qCoefficientHex=[float(z).hex() for z in qv],radialKnots=p.knots.tolist(),
        pFrequencies=p.k.tolist(),qFrequencies=q.k.tolist(),derivativeBounds=dict(px=pd,pu=pu,qx=qd,qu=qu),
        determinantUniformLower=determinant,zeroSixJetComparison=err.tolist(),linearizedHistory=history,actualG10Trials=rows,
        chosenGridIndependent=True,chosen=chosen,accepted=bool(chosen),actualG11=independent,wholeClosedReachCertified=False,
        allGeometryPointSetsInvariantForExactDiffeomorphism=True,seconds=time.monotonic()-tic)
    h=c.save(args.output,out)
    print(json.dumps(dict(SHA=h,chosen=chosen,G11=independent,seconds=out["seconds"])),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser();hf.args_hf(ap)
    for k in ("diagonal","output"):ap.add_argument("--"+k,type=Path,required=True)
    main(ap.parse_args())
