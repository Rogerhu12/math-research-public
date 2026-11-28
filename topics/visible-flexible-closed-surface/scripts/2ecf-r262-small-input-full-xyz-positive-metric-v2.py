#!/usr/bin/env python3
"""New physical-input continuation of the R262 prefix with bounded-memory FFT Jacobians.

All old physical source modes are retained. Only the original prefix is changed;
the entire original tail, true cuff and caps retain their own definitions. The
first stage chooses a positive radial metric. Later spatial enrichments freeze
that same continuous metric. No historical byte identity is fabricated.
"""
import argparse, gc, hashlib, importlib.util, json, os, subprocess, sys, time
from pathlib import Path
from fractions import Fraction
from types import SimpleNamespace
for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import LinearOperator, lsmr

O=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
HISTORICAL="5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8"

def mod(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def knots(n):
    return np.r_[np.zeros(6),np.arange(1,n)/n,np.ones(6)]

def basis(n,t,length):
    k=knots(n)
    b=BSpline(k,np.eye(len(k)-6)[:,3:-3],5)
    return [b(t,i)/length**i for i in range(3)]

def chi(t,j):
    return np.polynomial.polynomial.polyval(t,
             np.polynomial.polynomial.polyder([1.,0,0,-10,15,-6.],j))

class Source:
    def __init__(self,a):
        self.a=a
        S=a.scripts
        base=mod(S/"2ecf-r262-minkowski-physical-continuation.py","smallR262Base")
        self.base=base
        j=base.load(S/"6a65-m12-global-common-cut-position-recovered.py","smallR262Joint")
        w=base.load(S/"6a65-m12-entire-half-cartesian-bvp.py","smallR262Whole")
        bg=base.load(S/"6a65-m12-original-tail-background.py","smallR262Background")
        g=json.loads(a.grid.read_text())
        a.background_tolerance=g["background_tolerance"]
        _,meta,bridge,_,_,self.chart=w.definition(a,j,bg)
        source=j.CommonCutSource(a.data,meta,bridge,a.query_report,a.query_cache)
        base.load(S/"2ecf-m12-h2-cached-direct-lm-v2.py","smallR262Cache").cache_tail_apply(w.TailQueries,[])
        tail=w.TailQueries(a.query_report,a.query_cache)
        self.center=base.Center(j,a.data)
        self.pos=w.WholePosition(source,self.center.raw,self.chart,tail,j)
        self.joint=j
        self.S=float(self.chart.S)
        self.T=float(self.chart.total)
        with np.load(a.field) as z:
            self.spline=BSpline(z["unit_knots"],np.pad(z["coefficients"],((3,3),(0,0))),5)
            self.pm=z["planar_modes"].copy()
            self.hm=z["vertical_modes"].copy()
        self.source_sha=digest(a.field)
        print("ACTUAL_INPUT",self.source_sha,"historical_match",self.source_sha==HISTORICAL,flush=True)

    def prefix(self,t,n,shift):
        # Shifted grids are obtained as an exact subset of a twice-finer
        # uniform native material-angle grid, with every old mode retained.
        raw=2*n if shift else n
        sl=slice(1,None,2) if shift else slice(None)
        u=np.arange(raw)*2*np.pi/raw
        theta=u[sl]
        js=[];rs=[]
        for begin in range(0,len(t),16):
            j,r=self.joint.background(self.pos.src,self.center.raw,t[begin:begin+16],raw,self.pos.prefix_cache)
            js.append(np.asarray(j[:,:,sl],dtype=float).copy())
            rs.append(np.asarray(r[:,sl],dtype=float).copy())
        J=np.concatenate(js)
        rho=np.concatenate(rs)
        del js,rs
        z=t*self.S/self.T
        scale,scaleq=self.chart.scales(z)
        v=[self.spline(z,i) for i in range(3)]
        v[2]=v[2]/(self.T*scale[:,None])**2-v[1]*scaleq[:,None]/(self.T*scale[:,None]**3)
        v[1]/=self.T*scale[:,None]
        ep=np.exp(1j*self.pm[:,None]*theta)
        eh=np.exp(1j*self.hm[:,None]*theta)
        for index,(rad,ang) in enumerate(O):
            p=(v[rad][:,:len(self.pm)]*(1j*self.pm)**ang)@ep
            h=(v[rad][:,len(self.pm):]*(1j*self.hm)**ang)@eh
            J[:,index]+=np.stack((p.real,p.imag,h.real),axis=-1)
        self.pos.prefix_cache.clear()
        return theta,J,rho

def fft_forward(radial,m,n,offset,order):
    nr=radial.shape[0]
    out=np.zeros((nr,n//2+1,3),complex)
    out[:,0,0]=radial[:,0]
    out[:,1:m+1,0]=radial[:,1:m+1]/2
    out[:,1:m+1,1]=-.5j*radial[:,m+1:2*m+1]
    out[:,0,2]=radial[:,2*m+1]
    out[:,1:m+1,2]=radial[:,2*m+2:3*m+2]/2
    k=np.arange(n//2+1)
    out*=((1j*k)**order*np.exp(1j*k*offset))[None,:,None]
    return np.fft.irfft(out,n=n,axis=1,norm="forward")

def fft_adjoint(g,m,offset,order):
    # This is the real Euclidean adjoint of fft_forward, including the
    # DC cosine and the unnormalised rfft sum.
    f=np.fft.rfft(g,axis=1)[:,:m+1]
    k=np.arange(m+1)
    d=((1j*k)**order*np.exp(1j*k*offset))[None,:,None]*f.conj()
    return np.concatenate((d[:,:,0].real,d[:,1:,1].imag,d[:,:,2].real),axis=1)

def gram(J,Q,W,rho):
    v,u=J[:,1],J[:,2]
    E=np.sum(v*v,axis=-1)
    F=np.sum(v*u,axis=-1)
    G=np.sum(u*u,axis=-1)
    p=E/Q-1
    q=F/(rho*np.sqrt(Q*W))
    r=G/(rho*rho*W)-1
    residual=np.stack((p,np.sqrt(2)*q,r))
    error=np.abs(p+r)/2+np.hypot((p-r)/2,q)
    return residual,error,(v,u,E,F,G)

def curvature(J):
    v,u=J[:,1],J[:,2]
    E=np.sum(v*v,axis=-1)
    F=np.sum(v*u,axis=-1)
    G=np.sum(u*u,axis=-1)
    N=np.cross(v,u)
    area=np.sum(N*N,axis=-1)
    N/=np.sqrt(area)[...,None]
    l,m,n=[np.sum(N*J[:,i],axis=-1) for i in (3,4,5)]
    tr=(G*l+E*n-2*F*m)/area
    gauss=(l*n-m*m)/area
    return np.abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-gauss)),area

class Grid:
    def __init__(self,source,eta,spans,modes,radial,angles,shift,metric):
        if 2*modes>=angles:
            raise ValueError("Angular correction requires frequencies below the Nyquist mode")
        self.source=source
        self.m=modes
        self.spans=spans
        self.n=angles
        self.na=3*modes+2
        self.t=np.unique(np.r_[np.linspace(0,1,radial+1),
                      np.arange(spans+1)/spans,
                      (np.arange(radial)+(.613 if shift else .317))/radial])
        self.u,self.old,self.rho=source.prefix(self.t,angles,shift)
        self.offset=float(self.u[0])
        self.B=basis(spans,self.t,source.S)
        self.nb=self.B[0].shape[1]
        self.shape=(self.nb,self.na)
        self.nx=self.nb*self.na
        self.metric=metric
        if metric is not None:
            self.M=basis(metric["spans"],self.t,source.S)[0]
        diff=np.asarray(source.center.difference(self.u,eta),float)
        self.base=self.old
        del self.old
        for index,(r,a) in enumerate(O):
            self.base[:,index]+=chi(self.t,r)[:,None,None]/source.S**r*diff[a][None]
        self.eta=eta
        self.nvar=self.nx+(2*self.nb if metric is None else 0)

    def unpack(self,x):
        X=x[:self.nx].reshape(self.shape)
        if self.metric is None:
            aq=x[self.nx:self.nx+self.nb]
            aw=x[self.nx+self.nb:]
            Q=1+self.B[0]@aq
            W=1+self.B[0]@aw
            lo=min(1.,float(1+aq.min()),float(1+aw.min()))
        else:
            aq=np.asarray(self.metric["q"])
            aw=np.asarray(self.metric["w"])
            Q=1+self.M@aq
            W=1+self.M@aw
            lo=min(1.,float(1+aq.min()),float(1+aw.min()))
        return X,Q[:,None],W[:,None],lo

    def jets(self,x,all_jets=True):
        X,Q,W,lo=self.unpack(x)
        J=self.base.copy()
        for k,(r,a) in enumerate(O):
            if all_jets or k in (1,2):
                J[:,k]+=fft_forward(self.B[r]@X,self.m,self.n,self.offset,a)
        return J,Q,W,lo

    def report(self,x):
        J,Q,W,lo=self.jets(x)
        res,err,_=gram(J,Q,W,self.rho)
        k,area=curvature(J)
        i,j=np.unravel_index(np.argmax(err),err.shape)
        return dict(peak=float(err.max()),rms=float(np.sqrt(np.mean(res*res))),
                    curvature=float(k.max()),positiveMetricCoefficientLower=lo,
                    areaRatioMinimum=float((np.sqrt(area/(Q*W))/self.rho).min()),
                    worstPhysicalRadialAndNativeTheta=[float(self.t[i]*self.source.S),float(self.u[j])],
                    radialRows=len(self.t),angles=self.n)

    def objective(self,x,p):
        J,Q,W,lo=self.jets(x,False)
        if lo<=.25:
            return np.inf,np.inf
        _,e,_=gram(J,Q,W,self.rho)
        peak=float(e.max())
        return float(np.mean(e**p)**(1/p)),peak

    def linear(self,x,power):
        J,Q,W,lo=self.jets(x,False)
        residual,error,(v,u,E,F,G)=gram(J,Q,W,self.rho)
        weight=(np.maximum(.04,error/max(float(error.max()),1e-30))**power)/np.sqrt(error.size)
        cross=np.sqrt(2)/(self.rho*np.sqrt(Q*W))
        data_shape=residual.shape
        def forward(dx):
            dX=dx[:self.nx].reshape(self.shape)
            dv=fft_forward(self.B[1]@dX,self.m,self.n,self.offset,0)
            du=fft_forward(self.B[0]@dX,self.m,self.n,self.offset,1)
            y0=2*np.sum(v*dv,axis=-1)/Q
            y1=cross*(np.sum(u*dv,axis=-1)+np.sum(v*du,axis=-1))
            y2=2*np.sum(u*du,axis=-1)/(self.rho*self.rho*W)
            if self.metric is None:
                dq=(self.B[0]@dx[self.nx:self.nx+self.nb])[:,None]
                dw=(self.B[0]@dx[self.nx+self.nb:])[:,None]
                y0-=E/Q**2*dq
                y1-=.5*residual[1]*(dq/Q+dw/W)
                y2-=G/(self.rho*self.rho*W**2)*dw
            return (np.stack((y0,y1,y2))*weight[None]).ravel()
        def adjoint(dy):
            y=dy.reshape(data_shape)*weight[None]
            gv=(2*y[0]/Q)[...,None]*v+(y[1]*cross)[...,None]*u
            gu=(y[1]*cross)[...,None]*v+(2*y[2]/(self.rho*self.rho*W))[...,None]*u
            out=self.B[1].T@fft_adjoint(gv,self.m,self.offset,0)+self.B[0].T@fft_adjoint(gu,self.m,self.offset,1)
            if self.metric is not None:
                return out.ravel()
            gq=(-y[0]*E/Q**2-.5*y[1]*residual[1]/Q).sum(axis=1)
            gw=(-y[2]*G/(self.rho*self.rho*W**2)-.5*y[1]*residual[1]/W).sum(axis=1)
            return np.r_[out.ravel(),self.B[0].T@gq,self.B[0].T@gw]
        # Exact diagonal of this weighted sampled J^T J, assembled one
        # angular channel at a time without allocating the full Jacobian.
        diagonal=np.zeros((self.nb,self.na))
        B0,B1=self.B[:2]
        channels=[(0,k,False) for k in range(self.m+1)]+[(1,k,True) for k in range(1,self.m+1)]+[(2,k,False) for k in range(self.m+1)]
        for index,(c,k,sine) in enumerate(channels):
            h0=np.sin(k*self.u) if sine else np.cos(k*self.u)
            h1=k*np.cos(k*self.u) if sine else -k*np.sin(k*self.u)
            a=2*v[:,:,c]/Q*h0*weight
            b=cross*u[:,:,c]*h0*weight
            d=cross*v[:,:,c]*h1*weight
            e=2*u[:,:,c]/(self.rho*self.rho*W)*h1*weight
            aa=np.sum(a*a+b*b,axis=1)
            bb=2*np.sum(b*d,axis=1)
            cc=np.sum(d*d+e*e,axis=1)
            diagonal[:,index]=(B1*B1).T@aa+(B0*B1).T@bb+(B0*B0).T@cc
        dd=diagonal.ravel()
        if self.metric is None:
            aq=(-E/Q**2)*weight
            bq=(-.5*residual[1]/Q)*weight
            aw=(-G/(self.rho*self.rho*W**2))*weight
            bw=(-.5*residual[1]/W)*weight
            dd=np.r_[dd,(B0*B0).T@np.sum(aq*aq+bq*bq,axis=1),
                     (B0*B0).T@np.sum(aw*aw+bw*bw,axis=1)]
        scale=1/np.sqrt(np.maximum(dd,1e-25))
        operator=LinearOperator((residual.size,self.nvar),
                  matvec=lambda y:forward(scale*y),
                  rmatvec=lambda y:scale*adjoint(y),dtype=float)
        return operator,(residual*weight[None]).ravel(),scale,forward,adjoint,weight

def checks(grid,x):
    op,res,scale,j,jt,w=grid.linear(x,.4)
    rng=np.random.default_rng(299262)
    v=rng.normal(size=grid.nvar)
    v/=np.linalg.norm(v)
    z=rng.normal(size=res.size)
    lhs=float(z@j(v))
    rhs=float(v@jt(z))
    adj=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
    eps=2e-6
    def residual(q):
        J,Q,W,_=grid.jets(q,False)
        return (gram(J,Q,W,grid.rho)[0]*w[None]).ravel()
    fd=(residual(x+eps*v)-residual(x-eps*v))/(2*eps)
    direction=float(np.linalg.norm(fd-j(v))/max(1e-20,np.linalg.norm(j(v))))
    if adj>2e-11 or direction>2e-5:
        raise ArithmeticError("Actual FFT Jacobian/adjoint mismatch")
    return dict(adjointRelative=adj,centralDirectionalRelative=direction,epsilon=eps)

def transfer(old,oldm,newn,newm):
    nold=old.shape[0]+1
    spline=BSpline(knots(nold),np.pad(old,((3,3),(0,0))),5)
    old_knots=set(float(v) for v in knots(nold))
    for v in np.arange(1,newn)/newn:
        if float(v) not in old_knots:
            spline=spline.insert_knot(float(v))
    if len(spline.t)!=len(knots(newn)) or np.max(abs(spline.t-knots(newn)))>1e-14:
        raise ValueError("Requested refinement is not a nested physical knot set")
    v=spline.c[3:-3]
    out=np.zeros((newn-1,3*newm+2))
    out[:,:oldm+1]=v[:,:oldm+1]
    out[:,newm+1:newm+1+oldm]=v[:,oldm+1:2*oldm+1]
    out[:,2*newm+1:2*newm+2+oldm]=v[:,2*oldm+1:]
    return out

def save_state(path,X,spans,modes,metric,eta):
    np.savez_compressed(path,xyz=X,spans=spans,modes=modes,
          metric_spans=metric["spans"],metric_q=metric["q"],metric_w=metric["w"],eta=eta)

def main(a):
    W=a.work
    g=W/"h2-c2-m48-g12-04r1"
    a.data=W/"m12-prefix-data.npz.gz"
    a.grid=g/"grid.json"
    a.query_report=g/"exact-tail-queries.json"
    a.query_cache=Path(str(a.query_report)+".npz")
    a.field=g/"result.json.field.npz"
    source=Source(a)
    stages=[(48,24,256,192,8),(96,64,384,384,14),(192,96,576,512,12)]
    history=[]
    metric=None;oldX=None;oldm=None
    elapsed=time.monotonic()
    for number,(spans,modes,nrad,nang,steps) in enumerate(stages):
        P=Grid(source,a.eta,spans,modes,nrad,nang,False,metric)
        x=np.zeros(P.nvar)
        if oldX is not None:
            x[:P.nx]=transfer(oldX,oldm,spans,modes).ravel()
        verification=checks(P,x)
        initial=P.report(x)
        print("STAGE",number+1,"variables",P.nvar,initial,verification,flush=True)
        accepted=[]
        diagnostics=[]
        for step in range(steps):
            power=.3 if step<3 else .7 if step<8 else 1.2
            op,res,scale,j,jt,weight=P.linear(x,power)
            before=P.report(x)
            exponent=4 if step<4 else 8
            old_obj,_=P.objective(x,exponent)
            best=None
            for damp in (1e-6,3e-5):
                sol=lsmr(op,-res,damp=damp,atol=2e-10,btol=2e-10,maxiter=a.iterations)
                direction=scale*sol[0]
                diagnostics.append(dict(step=step+1,damping=damp,stop=int(sol[1]),iterations=int(sol[2]),
                                        residual=float(sol[3]),normalResidual=float(sol[4])))
                for alpha in (1.,.5,.25,.125,.0625,.03125):
                    candidate=x+alpha*direction
                    objective,peak=P.objective(candidate,exponent)
                    if objective<old_obj and peak<before["peak"]*1.0001:
                        test=P.report(candidate)
                        if test["curvature"]>max(10.3,before["curvature"]+.0001):
                            continue
                        score=objective+.15*peak
                        if best is None or score<best[0]:
                            best=(score,candidate,test,alpha,damp)
                if best is not None:
                    break
            del op,res,scale,j,jt,weight,sol,direction
            if best is None:
                print("NO_ACCEPT",number+1,step+1,before,flush=True)
                break
            _,x,report,alpha,damp=best
            accepted.append(dict(step=step+1,scale=alpha,damping=damp,actual=report))
            print("ACCEPT",number+1,accepted[-1],flush=True)
            X,_,_,_=P.unpack(x)
            if metric is None:
                active_metric=dict(spans=spans,q=x[P.nx:P.nx+P.nb].tolist(),w=x[P.nx+P.nb:].tolist())
            else:
                active_metric=metric
            save_state(a.out.with_name(a.out.stem+"-partial.npz"),X,spans,modes,active_metric,a.eta)
            if report["peak"]<1e-9:
                break
        final_training=P.report(x)
        oldX=P.unpack(x)[0].copy()
        oldm=modes
        if metric is None:
            metric=dict(spans=spans,q=x[P.nx:P.nx+P.nb].tolist(),w=x[P.nx+P.nb:].tolist())
        del P
        gc.collect()
        # Construct the independent grid only after releasing the training
        # arrays; background evaluation itself uses sixteen radial rows.
        Q=Grid(source,a.eta,spans,modes,max(360,nrad+97),max(320,nang+128),True,metric)
        independent=Q.report(oldX.ravel())
        state=a.out.with_name(a.out.stem+"-stage"+str(number+1)+".npz")
        save_state(state,oldX,spans,modes,metric,a.eta)
        row=dict(stage=number+1,spans=spans,modes=modes,metricChosenThisStage=number==0,
                 fixedContinuousMetricSinceStage=1,sourceS=source.S,initialTraining=initial,
                 checks=verification,accepted=accepted,lsmr=diagnostics,
                 finalTraining=final_training,finalIndependent=independent,stateSHA256=digest(state))
        history.append(row)
        summary=dict(eta=a.eta,actualEntrySHA256=digest(__file__),activeEntrySourceCommit=os.environ.get("R262_ENTRY_SOURCE_COMMIT"),sourceFieldSHA256=source.source_sha,historicalSourceBytesMatched=source.source_sha==HISTORICAL,
                     actualStages=[{k:v for k,v in r.items() if k not in ("accepted","lsmr")}|
                                   {"acceptedSteps":len(r["accepted"])} for r in history],
                     originalTailAndCuffSpatiallyUnchanged=True,continuousMetricCertificateObtained=False,
                     originalWholeGeometryCertificateTransferred=False,elapsedSeconds=time.monotonic()-elapsed)
        out=dict(schema="R262-prefix-true-small-Minkowski-input-bounded-memory-FFT-XYZ-and-positive-common-metric-v2",
                 entrySHA256=digest(__file__),sourceScriptSHA256=digest(a.scripts/"2ecf-r262-minkowski-physical-continuation.py"),
                 summary=summary,metric=metric,history=history)
        a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
        print("INDEPENDENT",number+1,independent,flush=True)
        del Q
        gc.collect()
        if time.monotonic()-elapsed>a.maximum_seconds:
            break
    save_state(a.out.with_suffix(".npz"),oldX,history[-1]["spans"],oldm,metric,a.eta)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--scripts",type=Path,required=True)
    p.add_argument("--work",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--eta",type=float,default=1/8192)
    p.add_argument("--iterations",type=int,default=600)
    p.add_argument("--maximum-seconds",type=float,default=10800)
    a=p.parse_args()
    # The existing Actions job already owns the regenerated original data.
    # New full-amplitude source experiments consume those bytes before this
    # independent small-input branch, without recreating the old solve.
    prelude=Path.cwd()/"topics/visible-flexible-closed-surface/scripts/2ecf-r262-new-physical-inputs-prelude.py"
    if os.environ.get("GITHUB_RUN_ID") and prelude.exists():
        src_path="topics/visible-flexible-closed-surface/scripts/"+Path(__file__).name
        identity=subprocess.run(["git","log","-1","--format=%H","--",src_path],capture_output=True,text=True,check=True)
        os.environ["R262_ENTRY_SOURCE_COMMIT"]=identity.stdout.strip()
        code=subprocess.run([sys.executable,str(prelude),"--scripts",str(a.scripts),"--work",str(a.work)]).returncode
        print("FULL_INPUT_PRELUDE_EXIT",code,flush=True)
    main(a)
