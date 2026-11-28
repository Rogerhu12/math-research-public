#!/usr/bin/env python3
"""Physical all-row GN with a finite-grid active set for two held points and principal curvatures."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np
from scipy.optimize import minimize

def read(path):
    return json.loads(Path(path).read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path,value):
    with Path(path).open('x') as out:
        json.dump(value,out,separators=(',',':'),allow_nan=False)
        out.write('\n')

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

class Problem:
    def __init__(self,args):
        here=Path(__file__).parent
        self.args=args
        supplier=module(here/'2ecf-polar-raised-physical-ray-position-source.py','pc_source')
        self.manifest,de,full,caches,mods,*_=supplier.validate_prepared(args)
        self.basis=module(here/'2ecf-polar-fixed-prefix-position-basis.py','pc_basis').restrict(full)[0]
        self.stream=mods['stream']
        self.point=self.stream.point
        self.area=module(args.scripts/'6a65-geometry-area-ratio-power-two.py','pc_area')
        self.scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','pc_scan')
        self.cfg=self.point.PointConfig(**de['pointConfig'])
        self.grids={k:(c,self.basis.matrices(c.nodes),{n:.5*np.asarray(x) for n,x in self.manifest['caches'][k]['weights'].items()}) for k,c in caches.items()}
        self.prec=self.stream.BandedSobolev(self.basis,np.concatenate([g[0].nodes for g in self.grids.values()]),np.concatenate([g[2]['metric'] for g in self.grids.values()]),de['recipe']['preconditioner'])
        self.model=dict(basis=self.basis.definition,pointConfig=de['pointConfig'],frozenSource=de['sourceIdentity'],preconditioner=self.prec.definition,rows=4291840,entrySHA256=sha(__file__),sourceSHA256=sha(supplier.__file__),iterations=args.iterations,damping=args.damping,heldFloor=args.held,curvatureCeiling=args.curvature)

    def blocks(self,z):
        for name,(cache,mat,weights) in self.grids.items():
            N=len(cache.u)
            for start in range(0,len(cache.nodes),8):
                sel=slice(start,start+8)
                mm=tuple(op[sel] for op in mat)
                nodes=cache.nodes[sel]
                jets,rad=cache(nodes,N)
                j=jets+self.basis.packet(mm,z,N)
                w={k:v[sel,None]/N for k,v in weights.items()}
                yield name,start,mm,nodes,j,rad,w

    def value(self,z):
        vals=[]
        for key,(c,m,w) in self.grids.items():
            jets=c.jets+self.basis.packet(m,z,len(c.u))
            vals.append(self.scan.evaluate(self.stream,self.point,self.area,jets,c.radius,c.nodes,c.u,self.cfg,self.manifest['caches'][key]['weights']))
        return dict(R2=sum(v['R2'] for v in vals),metric=max(v['metric'] for v in vals),curvature=max(v['curvature'] for v in vals),held=min(v['held'] for v in vals),rows=sum(v['actualRows'] for v in vals))

    def normal(self,z,direction=None):
        adj=np.zeros_like(z)
        q=0.
        rows=0
        for _,_,m,ns,j,f,w in self.blocks(z):
            p=self.point.PointLinearized(j.swapaxes(1,2),f,self.cfg,w)
            ar=self.area.AreaPacket(j,f,w['metric'],.5)
            if direction is None:
                r=p.residual
                ra=ar.residual
            else:
                v=self.basis.packet(m,direction,j.shape[2])
                r=p.jvp(v.swapaxes(1,2))
                ra=ar.jvp(v[:,1],v[:,2])
            b=p.vjp(r).swapaxes(1,2)
            bs,bu=ar.vjp(ra)
            b[:,1]+=bs
            b[:,2]+=bu
            adj+=self.basis.packet_adjoint(m,b)
            q+=np.vdot(r,r)+np.vdot(ra,ra)
            rows+=r.size+ra.size
        assert rows==4291840
        return self.prec.transpose(adj),float(q)

    def cg_direction(self,z):
        gradient,R2=self.normal(z)
        r=-gradient
        d=r.copy()
        y=np.zeros_like(d)
        rr=r@r
        errors=[]
        for _ in range(self.args.iterations):
            h,q=self.normal(z,self.prec.unpack(d))
            err=abs(d@h-q)/max(1.,q)
            errors.append(float(err))
            if err>2e-9:
                raise ArithmeticError('Normal adjoint check failed')
            h+=self.args.damping*d
            step=rr/(d@h)
            y+=step*d
            r-=step*h
            rrnew=r@r
            if rrnew<1e-15:
                break
            d=r+(rrnew/rr)*d
            rr=rrnew
        return gradient,y,R2,errors

    def project(self,z,y):
        dz=self.prec.unpack(y)
        candidates={}
        center=np.array([0.,self.cfg.central_a,0.])
        args=self.args
        for key,first,m,ns,j,f,w in self.blocks(z):
            N=j.shape[2]
            v=self.basis.packet(m,dz,N)
            jets=j.swapaxes(1,2)
            ds=v.swapaxes(1,2)
            cur=self.point.curvature_cache(jets)
            A,B,C=np.moveaxis(cur['S'],-1,0)
            delta=(A-C)/2
            spread=np.hypot(delta,B)
            rho=np.maximum(spread,1e-100)
            dA,dB,dC=np.moveaxis(self.point.curvature_jvp(jets,cur,ds),-1,0)
            constraints=[]
            for sign in (1,-1):
                diff=j[:,0]-sign*center
                dist=np.linalg.norm(diff,axis=-1)
                deriv=-np.sum(diff*v[:,0],axis=-1)/dist
                constraints.append(('held',sign,deriv,args.held+.00006-dist))
            for idx,sign in enumerate((1,-1)):
                lam=cur['eigenvalues'][...,idx]
                deriv=np.sign(lam)*((dA+dC)/2+sign*(delta*(dA-dC)/2+B*dB)/rho)
                constraints.append(('curvature',sign,deriv,np.abs(lam)-(args.curvature-.35)))
            for kind,sign,deriv,raw in constraints:
                prediction=raw+deriv
                for i,k in np.argwhere(prediction>0):
                    score=float(prediction[i,k])
                    cell=(kind,int(ns[i]/.018),int(k*24/N))
                    if cell in candidates and candidates[cell][0]>=score:
                        continue
                    cot=np.zeros((6,3))
                    if kind=='held':
                        diff=j[i,0,k]-sign*center
                        cot[0]=-diff/np.linalg.norm(diff)
                    else:
                        ang=sign
                        idx=0 if sign==1 else 1
                        scale=np.sign(cur['eigenvalues'][i,k,idx])
                        d=delta[i,k]/rho[i,k]
                        bb=B[i,k]/rho[i,k]
                        s=scale*np.array([(.5+ang*d/2),ang*bb,(.5-ang*d/2)])
                        cc={n:x[i:i+1,k:k+1] for n,x in cur.items()}
                        cot=self.point.curvature_vjp(jets[i:i+1,k:k+1],cc,s[None,None,:])[0,0]
                    candidates[cell]=(score,key,first+int(i),int(k),cot,-float(raw[i,k]),float(deriv[i,k]),kind)
        chosen=[]
        for group in ('held','curvature'):
            chosen+=sorted((v for v in candidates.values() if v[-1]==group),key=lambda v:-v[0])[:40]
        rows=[]
        rhs=[]
        checks=[]
        kinds=[]
        for _,key,i,k,cot,b,analytic,kind in chosen:
            cache,mat,_=self.grids[key]
            N=len(cache.u)
            impulse=np.zeros((1,6,N,3))
            impulse[0,:,k]=cot
            op=tuple(a[i:i+1] for a in mat)
            row=self.prec.transpose(self.basis.packet_adjoint(op,impulse))
            checks.append(abs(row@y-analytic)/max(1.,abs(analytic)))
            norm=np.linalg.norm(row)
            if norm>1e-13:
                rows.append(row/norm)
                rhs.append(b/norm)
                kinds.append(kind)
        if not rows:
            return y,dict(count=0)
        if max(checks)>1e-8:
            raise ArithmeticError('Active physical gradient not its directional derivative')
        mat=np.stack(rows)
        rhs=np.asarray(rhs)
        gram=mat@mat.T
        offset=rhs-mat@y
        sol=minimize(lambda x:(.5*x@gram@x+offset@x,gram@x+offset),np.zeros(len(rows)),jac=True,bounds=[(0,None)]*len(rows),method='L-BFGS-B',options=dict(maxiter=800,ftol=1e-14,gtol=1e-10))
        projected=y-mat.T@sol.x
        return projected,dict(count=len(rows),heldRows=kinds.count('held'),curvatureRows=kinds.count('curvature'),derivativeCheck=max(checks),dualSuccess=bool(sol.success),dualIterations=int(sol.nit),maxNormalizedViolation=float(np.max(mat@projected-rhs)),relativeDisplacement=float(np.linalg.norm(projected-y)/max(np.linalg.norm(y),1e-100)))

def run(args):
    p=Problem(args)
    initial=read(args.state)
    assert initial['preparedSHA256']==sha(args.prepared) and initial['modelDefinition']['basis']==p.basis.definition
    z=np.asarray(initial['z']).reshape(p.basis.nb,p.basis.na)
    base=p.value(z)
    assert base['held']>=args.held and base['curvature']<=args.curvature
    history=[]
    own=0
    for i in range(args.steps):
        gradient,unconstrained,R2,checks=p.cg_direction(z)
        if abs(R2-base['R2'])>1e-8*max(R2,1.):
            raise ArithmeticError('Objective mismatch')
        y,active=p.project(z,unconstrained)
        slope=float(gradient@y)
        dz=p.prec.unpack(y)
        trials=[]
        accepted=False
        for exponent in range(12):
            alpha=2.**-exponent
            val=p.value(z+alpha*dz)
            trials.append(dict(alpha=alpha,**val))
            if slope<0 and val['held']>=args.held and val['curvature']<=args.curvature and val['R2']<=R2+2e-4*alpha*slope:
                z+=alpha*dz
                accepted=True
                own+=1
                break
        rec=dict(baseline=base,trials=trials,active=active,ownAccepted=own,accepted=accepted,adjointChecks=checks,slope=slope)
        history.append(rec)
        print(i+1,accepted,active,val,flush=True)
        if not accepted:
            break
        base=val
        save(str(args.prefix)+f'-step{i+1:02}-state.json',dict(z=z.ravel().tolist(),modelDefinition=p.model,preparedSHA256=sha(args.prepared),parentStateSHA256=sha(args.state),ownExtendedAcceptedSteps=own,acceptance=rec,fixedG=True,finiteOnly=True))
    save(str(args.prefix)+'-report.json',dict(entrySHA256=sha(__file__),preparedSHA256=sha(args.prepared),inputStateSHA256=sha(args.state),model=p.model,ownAccepted=own,history=history))

if __name__=='__main__':
    a=argparse.ArgumentParser()
    for k in ('scripts','prepared','state','prefix'):
        a.add_argument('--'+k,type=Path,required=True)
    a.add_argument('--steps',type=int,default=6)
    a.add_argument('--iterations',type=int,default=4)
    a.add_argument('--damping',type=float,default=.06)
    a.add_argument('--held',type=float,default=.64)
    a.add_argument('--curvature',type=float,default=16.5)
    run(a.parse_args())
