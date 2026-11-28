#!/usr/bin/env python3
"""Continue the true R262 central material curve to a complete true-arc sleeve while retaining every original ring and redistributing axial height."""
import argparse,gc,gzip,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import LinearOperator,lsmr

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def smooth(v):
    return v**3*(10-15*v+6*v*v)

def step(q,left,right):
    w=right-left
    v=np.clip((q-left)/w,0,1)
    return [smooth(v),30*v*v*(1-v)**2/w,60*v*(1-v)*(1-2*v)/w**2]

def physical_knots(c,width,S,n):
    # Positions are corrected on the entire old prefix [0,S], after the new cylinder.
    return np.r_[np.zeros(5),np.linspace(0,S,n+1),np.full(5,S)]

def Bvals(q,kn):
    n=len(kn)-6
    b=BSpline(kn,np.eye(n)[:,3:-3],5,extrapolate=False)
    use=(q>=kn[0])&(q<=kn[-1])
    result=[]
    for j in range(3):
        v=np.zeros((len(q),n-6))
        v[use]=b(q[use],j)
        result.append(v)
    return result

def xyz(z):
    return np.stack((np.real(z),np.imag(z),np.zeros_like(np.real(z))),axis=-1)

def true_arc_position(geo,u,anchor):
    """True centered target, using closed circular arcs and a short nonconstant turn."""
    # The continuous definition is the integral of i exp(i beta); all positions
    # and derivatives below refer to that same integral and the same beta.
    nodes,weights=np.polynomial.legendre.leggauss(100)
    a=geo.L0/2
    end=a+geo.TAU
    half=geo.P/2
    def circle(k,length):
        return np.expm1(1j*k*length)/k
    def transition(length):
        length=np.asarray(length)
        t=length[...,None]*(1+nodes)/2
        angle=geo.target_angle(a+t,0.)[0]-geo.LOW*a
        return 1j*np.exp(1j*geo.LOW*a)*length/2*(np.exp(1j*angle)@weights)
    t1=circle(geo.LOW,a)
    t2=t1+transition(geo.TAU)
    b2=geo.target_angle(np.array([end]),0.)[0][0]
    def from_low(v):
        v=np.asarray(v)
        return (circle(geo.LOW,np.minimum(v,a))+
                transition(np.clip(v-a,0,geo.TAU))+
                np.exp(1j*b2)*circle(geo.HIGH,np.maximum(v-end,0)))
    half_end=t2+np.exp(1j*b2)*circle(geo.HIGH,half-end)
    A=half_end.imag/np.tan(half)-half_end.real
    t=np.asarray(u)+anchor
    sector=np.floor((t+half)/geo.P).astype(int)
    v=t-sector*geo.P
    b=A+from_low(abs(v))
    return np.exp(1j*(sector*geo.P-anchor))*np.where(v<0,b.conjugate(),b)

def central_delta(src,geo,orig,theta,lam,anchor):
    if lam!=1.:
        raise ValueError('This physical source requires the full-amplitude circular-arc inlet')
    u=src.center.arc(theta)
    p,v,a=[np.asarray(src.center.base.derivative(theta,k),float) for k in range(3)]
    y=v[:,0]+1j*v[:,1]
    acc=a[:,0]+1j*a[:,1]
    speed=np.abs(y)
    if not np.all(speed>0):
        raise ValueError('Original arclength map is singular')
    u2=np.real(y.conjugate()*acc)/speed
    beta,curvature=geo.target_angle(u,anchor)
    normal=np.exp(1j*beta)
    tangent=1j*normal
    center=xyz(true_arc_position(geo,u,anchor))
    center1=xyz(tangent*speed)
    center2=xyz(-curvature*normal*speed**2+tangent*u2)
    original=np.stack((p,v,a))
    return original,np.stack((center,center1,center2))-original,speed

def normalized_drop(s,stop,w):
    # Positive C2 trapezoidal velocity; the total vertical drop is normalized to one.
    if not 2*w<stop:raise ValueError('Drop shoulders overlap')
    j=np.asarray(s);h=stop-w
    v=np.clip(j/w,0,1);z=np.clip((stop-j)/w,0,1)
    I=lambda t:t**4*(2.5-3*t+t*t)
    D=lambda t:30*t*t*(1-t)**2
    J=np.where(j<w,w*I(v),np.where(j<stop-w,j-w/2,np.where(j<stop,h-w*I(z),h)))/h
    J1=np.where(j<w,smooth(v),np.where(j<stop-w,1.,np.where(j<stop,smooth(z),0.)))/h
    J2=np.where(j<w,D(v),np.where(j<stop-w,0.,np.where(j<stop,-D(z),0.)))/(w*h)
    return J,J1,J2

def geometry(src,geo,orig,a,nrad,nang,shift):
    # The old material interval s in [0,S] is kept in its entirety. On the
    # complete new surface the physical radial material coordinate is c+s.
    c=a.full_sleeve;w=a.full_gate;H=a.height_drop_end;X=a.lift_end
    if not 0<2*w<H<src.S or not 0<X<src.S:raise ValueError('Require both transitions before the original end')
    s=np.unique(np.r_[np.linspace(0,src.S,nrad+1),src.S*(np.arange(nrad)+(.687 if shift else .267))/nrad,
               np.linspace(0,w,9),np.linspace(H-w,H,9),np.linspace(0,src.S,a.spans+1),X,H,w,H-w])
    theta,old,rr=src.prefix(s/src.S,nang,shift)
    old=np.asarray(old,float);rr=np.asarray(rr,float)
    refprev=old.copy()
    if 2*a.modes>=nang:raise ValueError('Angular correction touches Nyquist')
    ori,diff,sp=central_delta(src,geo,orig,theta,1.,a.anchor)
    h=step(s,0,X);h=[1-h[0],-h[1],-h[2]]
    j,j1,j2=normalized_drop(s,H,w)
    lift=c*(1-j);lift1=-c*j1;lift2=-c*j2
    for index,(r,v) in enumerate(src.base.O):
        old[:,index]+=h[r][:,None,None]*diff[v][None]
        if v==0:old[:,index,:,2]+=(lift,lift1,lift2)[r][:,None]
    return s,theta,old,rr,refprev,rr,0.,w

def make_grid(micro,src,geo,orig,a,nrad,nang,shift,metric=None):
    q,theta,base,rho,old,rr,c,d=geometry(src,geo,orig,a,nrad,nang,shift)
    G=micro.Grid.__new__(micro.Grid)
    G.source=src;G.spans=a.spans;G.m=a.modes;G.n=nang;G.na=3*G.m+2
    G.t=q/src.S;G.u=theta;G.offset=float(theta[0]);G.base=base;G.rho=rho
    G.kn=physical_knots(c,d,src.S,a.spans)
    G.B=Bvals(q,G.kn)
    G.nb=G.B[0].shape[1];G.shape=(G.nb,G.na);G.nx=G.nb*G.na
    G.metric=metric;G.eta=a.lam
    if metric is not None:G.M=Bvals(q,np.asarray(metric['knots']))[0]
    G.nvar=G.nx+(2*G.nb if metric is None else 0)
    def objective(x,power):
        J,Q,W,lo=G.jets(x,False)
        if lo<=0:return np.inf,np.inf
        err=micro.gram(J,Q,W,G.rho)[1]
        return float(np.mean(err**power)**(1/power)),float(err.max())
    G.objective=objective
    residual,err,_=micro.gram(old,1.,1.,rr)
    baseline=dict(peak=float(err.max()),curvature=float(micro.curvature(old)[0].max()))
    lens=[]
    for r in (0.,d,a.height_drop_end-d,a.lift_end,a.height_drop_end,src.S):
        i=np.argmin(abs(q-r));j=base[i]
        lens.append(dict(s=float(q[i]),newMaterialQ=float(a.full_sleeve+q[i]),oldHeight=[float(old[i,0,:,2].min()),float(old[i,0,:,2].max())],newHeight=[float(j[0,:,2].min()),float(j[0,:,2].max())],oldHorizontalDistanceToUnitSleeve=float(np.linalg.norm(old[i,0,:,:2]-base[0,0,:,:2],axis=-1).max()),oldAxialAcceleration=float(np.linalg.norm(old[i,3],axis=-1).max()),newZqRange=[float(j[1,:,2].min()),float(j[1,:,2].max())]))
    baseline["changedSourceZqRange"]=[float(base[:,1,:,2].min()),float(base[:,1,:,2].max())]
    return G,baseline,lens

class D3:
    """Orthogonal real threefold planar Fourier channels and vertical cos(3j theta)."""
    def __init__(self,g):
        self.g=g;m=g.m
        self.cols=[[(k,1.),(m+k,1. if k%3==1 else -1.)] for k in range(1,m+1) if k%3]
        self.cols+=[[(2*m+1+k,1.)] for k in range(0,m+1,3)]
        self.size=g.nb*len(self.cols)
    def expand(self,x):
        g=self.g
        v=x[:self.size].reshape(g.nb,len(self.cols))
        y=np.zeros(g.shape)
        for j,terms in enumerate(self.cols):
            for ix,c in terms:y[:,ix]=c*v[:,j]
        return np.r_[y.ravel(),x[self.size:]]
    def transpose(self,x,square=False):
        g=self.g;v=x[:g.nx].reshape(g.shape)
        J=np.column_stack([sum((c*c if square else c)*v[:,ix] for ix,c in terms) for terms in self.cols])
        return np.r_[J.ravel(),x[g.nx:]]
    def model(self,x,power):
        full=self.expand(x)
        _,res,sc,f,ft,_=self.g.linear(full,power)
        scale=1/np.sqrt(np.maximum(1e-24,self.transpose(1/sc**2,True)))
        op=LinearOperator((len(res),len(x)),matvec=lambda t:f(self.expand(t*scale)),rmatvec=lambda z:scale*self.transpose(ft(z)),dtype=float)
        return op,res,scale

def run(a):
    S=a.scripts
    micro=module(S/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','R262DA')
    geo=module(a.comparison,'R262D3Center')
    geo.LOW=a.low
    geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    W=a.work;fielddir=W/'h2-c2-m48-g12-04r1'
    a.data=W/'m12-prefix-data.npz.gz';a.grid=fielddir/'grid.json'
    a.query_report=fielddir/'exact-tail-queries.json';a.query_cache=Path(str(a.query_report)+'.npz');a.field=fielddir/'result.json.field.npz'
    src=micro.Source(a)
    orig=None  # Unit-speed target uses the original material-angle map directly.
    P,parent,rows=make_grid(micro,src,geo,orig,a,a.radial,a.angles,False)
    proj=D3(P)
    nx=proj.size
    x=np.zeros(nx+2*P.nb)
    empty=P.report(proj.expand(x))
    J=P.base
    EE=np.sum(J[:,1]**2,axis=-1)
    GG=np.sum(J[:,2]**2,axis=-1)/P.rho**2
    for offset,arr in ((nx,EE),(nx+P.nb,GG)):
        target=.5*(arr.max(axis=1)+arr.min(axis=1))-1
        val=np.linalg.lstsq(P.B[0],target,rcond=1e-12)[0]
        x[offset:offset+P.nb]=np.maximum(-.98,val)
    if a.seed:
        with np.load(a.seed) as z:
            if str(z['sourceSHA'])!=digest(Path(__file__)) or str(z['fieldSHA'])!=src.source_sha or float(z['fullSleeve'])!=a.full_sleeve or float(z['fullGate'])!=a.full_gate or float(z['liftEnd'])!=a.lift_end:raise ValueError('Seed source or surgery differs')
            if float(z['heightDropEnd'])!=a.height_drop_end:raise ValueError('Different drop end')
            if int(z['modes'])!=a.modes or int(z['spans'])!=a.spans or float(z['low'])!=a.low or abs(float(z['anchor'])-a.anchor)>1e-15:
                raise ValueError('Seed is on another center or coefficient space')
            x=np.asarray(z['reduced'])*a.lam/float(z['lam'])
    init=P.report(proj.expand(x))
    history=[]
    for i in range(a.steps):
        full=proj.expand(x);before=P.report(full);power=.35 if i<4 else .9
        op,r,scale=proj.model(x,power);old,_=P.objective(full,5 if i<5 else 8);best=None
        for damp in (2e-6,4e-5,.001):
            sol=lsmr(op,-r,damp=damp,atol=1e-10,btol=1e-10,maxiter=a.iterations)
            d=scale*sol[0]
            for alpha in (1.,.5,.25,.125,.0625):
                yy=x+alpha*d;b=proj.expand(yy);val,pk=P.objective(b,5 if i<5 else 8)
                if val>=old or pk>before['peak']*1.0001:continue
                tests=P.report(b)
                if tests['curvature']>max(a.curvature_guide,before['curvature']+1e-4):continue
                score=val+.12*pk
                if best is None or score<best[0]:best=(score,yy,tests,alpha,damp)
        if best is None:break
        _,x,tr,alpha,damp=best
        history.append(dict(step=i+1,scale=alpha,damping=damp,actual=tr));print('ACCEPT',a.lam,i+1,tr,flush=True)
    final=P.report(proj.expand(x))
    X,Q,ww,pos=P.unpack(proj.expand(x))
    metric=dict(knots=P.kn.tolist(),q=x[nx:nx+P.nb].tolist(),w=x[nx+P.nb:].tolist(),spans=a.spans)
    if pos<=0:raise ValueError('Nonpositive metric control')
    Q,oldQ,_=make_grid(micro,src,geo,orig,a,a.test_radial,a.test_angles,True,metric)
    ind=Q.report(X.ravel())
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:np.savez_compressed(f,fieldSHA=src.source_sha,sourceSHA=digest(Path(__file__)),comparisonSHA=digest(a.comparison),S=src.S,T=src.T,fullGate=a.full_gate,fullSleeve=a.full_sleeve,liftEnd=a.lift_end,heightDropEnd=a.height_drop_end,reduced=x,actualPhysicalXYZ=X,metricQ=metric['q'],metricW=metric['w'],knots=P.kn,lam=a.lam,low=a.low,anchor=a.anchor,modes=a.modes,spans=a.spans)
    out=dict(schema='R262-all-original-rings-vertical-redistribution-and-true-three-arc-sleeve-v1',sourceSHA=digest(Path(__file__)),comparisonSHA=digest(a.comparison),fieldSHA=src.source_sha,historicalMatch=src.source_sha==micro.HISTORICAL,originalDataSHA=digest(a.data),stateSHA=digest(state),lam=a.lam,low=a.low,high=geo.HIGH,anchor=a.anchor,
             numericalPhysicalCoordinates=dict(originalS=src.S,originalT=src.T,newS=src.S+a.full_sleeve,newT=src.T+a.full_sleeve,halfSleeve=a.full_sleeve,verticalShoulder=a.full_gate,dropEnd=a.height_drop_end,maximumVerticalVelocity=a.full_sleeve/(a.height_drop_end-a.full_gate),liftEnd=a.lift_end),nativeD3Correction=dict(angularModes=a.modes,radialSpans=a.spans,independentRealPositionVariables=nx,positiveMetricVariables=2*P.nb),circlePort=dict(unitSpeedCenters=[.205-a.anchor,float(np.pi+.205-a.anchor)],phaseInterval=[0,.41],realDefinition='integrate i exp(i beta) with D3 centered reflection; circular segments exact by expm1; nonconstant turn integrated by positive 100-node Gauss-Legendre'),
             trueOriginalPrefixAtProbeRows=rows,originalTraining=parent,originalIndependent=oldQ,unfittedRadialMetric=empty,initial=init,accepted=history,finalTraining=final,finalIndependent=ind,independentPhysicalGeometry=micro.physical_geometry(Q,X.ravel()),
             metricDefinition=dict(base='whole new sleeve has dq^2+du^2; on original s=q-c in [0,S] both positive radial multipliers of the original metric are designed then frozen, with exact clamped two-jets',**metric),
             fullDomain='Original material s in [0,S] includes every old cross section. In the new material q=c+s, the old tail s>=S has exactly its original position, metric, and true cuff; pure translation of the material chart adds c to its endpoint coordinate. Positive/negative original cap shapes are replaced by their true flat disks. No new displacement, total height, or old bound is assigned to the compact changed prefix.',
             scope='The full-amplitude material inlet has both genuine circular arcs. The actual thick arms are external to this prefix experiment. Closed shape, quantitative reach and full-domain metric tolerance require their own continuous certificates.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('FINAL',a.lam,init,ind,'historical',out['historicalMatch'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','work','comparison','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--seed',type=Path)
    p.add_argument('--lam',type=float,default=1.)
    p.add_argument('--low',type=float,default=.35)
    p.add_argument('--anchor',type=float,default=np.pi/3)
    for k,v in (('full-sleeve',.78),('full-gate',.22),('height-drop-end',1.90),('lift-end',1.5),('curvature-guide',8.85)):
        p.add_argument('--'+k,type=float,default=v)
    for k,v in (('spans',20),('modes',18),('angles',120),('radial',62),('test-angles',195),('test-radial',103),('steps',4),('iterations',110),('arc-nodes',24576)):
        p.add_argument('--'+k,type=int,default=v)
    a=p.parse_args()
    if a.lam!=1.:raise ValueError('Full-amplitude v2 requires lambda=1')
    run(a)
