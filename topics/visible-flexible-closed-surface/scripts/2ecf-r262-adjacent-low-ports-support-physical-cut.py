#!/usr/bin/env python3
"""Two adjacent actual equal-curvature attachment arcs on the original R262 material coordinate."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.sparse.linalg import lsmr

PERIOD=2*np.pi/3
HALF=PERIOD/2
LOW=.63
PHASE=1.15
V0=.536
V1=.548
CS=np.array([0.09999976505231697,0.00017340635052370438,-0.000020726030862500148,2.732239542665825e-9,1.364904959536114e-9,-6.697024595314116e-10,2.5420195020236015e-11,2.7693941053364423e-11,2.279645039764186e-11,7.050341026639808e-10,5.749608505622311e-11,2.4233142751359304e-10])
J=np.arange(1,1+len(CS))
B=(1-9*J**2)*(-1.)**J*CS
F=3*J
GN,GW=np.polynomial.legendre.leggauss(32)

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def base_radius(v):
    return 1+np.cos(np.asarray(v)[...,None]*F)@B

def sw(t):
    t=np.clip(t,0.,1.)
    return t**3*(10+t*(-15+6*t))

def weighted_integral(v,scale):
    """Integrate (r,r*sin,r*cos) from V0 to the given transition angles."""
    length=np.asarray(v)-V0
    z=V0+length[...,None]*(1+GN)/2
    g=sw((z-V0)/(V1-V0))
    r=(1-g)/LOW+g*scale*base_radius(z)
    return np.stack(tuple(length/2*(a@GW) for a in (r,r*np.sin(z),r*np.cos(z))),axis=-1)

def outside_primitive(v):
    v=np.asarray(v)
    z=v[...,None]
    def c(k):return np.sin(k*z)/k
    def s(k):return (2*np.sin(.5*k*z)**2)/k
    return np.stack((v+c(F)@B,2*np.sin(v/2)**2+((s(1+F)+s(1-F))/2)@B,
                     np.sin(v)+((c(1+F)+c(1-F))/2)@B),axis=-1)

class NormalCurve:
    LOW=LOW
    P=PERIOD
    def __init__(self):
        self.lo=np.array([V0,2*np.sin(V0/2)**2,np.sin(V0)])/LOW
        self.prim_left=outside_primitive(V1)
        old=outside_primitive(HALF)-self.prim_left
        a=weighted_integral(V1,0.)
        b=weighted_integral(V1,1.)-a
        self.scale=float((HALF-self.lo[0]-a[0])/(old[0]+b[0]))
        self.hi=self.lo+weighted_integral(V1,self.scale)
        end=self.hi+self.scale*old
        self.A=float(end[1]+end[2]/np.tan(HALF))
        self.Baxis=float(end[2]/np.sin(HALF))
        if not self.scale>0 or abs(end[0]-HALF)>1e-13:
            raise ArithmeticError('Failed physical half-period normalization')

    def integ(self,v):
        v=np.asarray(v)
        shape=v.shape
        v=v.reshape(-1)
        y=np.empty((len(v),3))
        a=v<=V0
        b=(v>V0)&(v<V1)
        c=v>=V1
        y[a]=np.column_stack((v[a],2*np.sin(v[a]/2)**2,np.sin(v[a])))/LOW
        if np.any(b):y[b]=self.lo+weighted_integral(v[b],self.scale)
        if np.any(c):y[c]=self.hi+self.scale*(outside_primitive(v[c])-self.prim_left)
        return y.reshape(shape+(3,))

    def at(self,u,anchor):
        u=np.asarray(u)+anchor
        sector=np.floor((u+HALF)/PERIOD)
        t=u-sector*PERIOD
        q=np.minimum(abs(t),HALF)
        lo=np.zeros_like(q)
        hi=np.full_like(q,HALF)
        v=np.where(q<=self.lo[0],LOW*q,V1+(HALF-V1)*(q-self.hi[0])/(HALF-self.hi[0]))
        v=np.clip(v,0,HALF)
        for _ in range(36):
            g=sw((v-V0)/(V1-V0))
            r=(1-g)/LOW+g*self.scale*base_radius(v)
            y=self.integ(v)
            err=y[...,0]-q
            done=abs(err)<=6e-15
            if np.all(done):break
            lo=np.where(err<=0,v,lo)
            hi=np.where(err>=0,v,hi)
            n=v-err/r
            v=np.where(done,v,np.where((n>lo)&(n<hi),n,(lo+hi)/2))
        else:raise ArithmeticError('Normal angle inverse failed to reach tolerance')
        direction=sector*PERIOD-anchor
        sign=np.sign(t)
        p=np.exp(1j*direction)*(self.A-y[...,1]+1j*sign*y[...,2])
        beta=direction+sign*v
        return p,beta,1/r

    def target_angle(self,u,anchor):
        _,b,k=self.at(u,anchor)
        return b,k

def true_arc_position(geo,u,anchor):
    return geo.at(u,anchor)[0]

def compare(a,comparison,geo):
    data=a.work/'m12-prefix-data.npz.gz'
    with gzip.open(data,'rb') as f:
        with np.load(f) as arr:row=arr['jets'][0,0].copy()
    obs=[]
    for n in (a.compare_nodes,2*a.compare_nodes):
        center=comparison.MaterialCenter(row,n)
        u=center.u
        z,T,N,k=center.original(u)
        p,b,g=geo.at(u,a.anchor)
        n1=np.exp(1j*b)
        t1=1j*n1
        def stat(y):
            y=np.abs(y);i=int(np.argmax(y))
            return dict(maximum=float(y[i]),atPhysicalU=float(u[i]),rms=float(np.sqrt(np.mean(y*y))))
        obs.append(dict(angles=n,position=stat(p-z),unitTangent=stat(t1-T),normalAngle=stat(np.angle(n1*N.conj())),
                        signedCurvature=stat(g-k),curvatureVector=stat(g*n1-k*N),newCurvatureRange=[float(g.min()),float(g.max())],
                        sourceCurvatureRange=[float(k.min()),float(k.max())]))
    return dict(schema='actual-R262-unit-speed-original-versus-adjacent-true-low-circle-traces',
                inputSHA=digest(data),entrySHA=digest(__file__),comparisonSHA=digest(a.comparison),cutSHA=digest(a.cut),
                normalPlateau=[-V0,V0],normalTransition=[V0,V1],k=LOW,phase=PHASE,anchor=a.anchor,
                supportCoefficients=CS.tolist(),exteriorRadiusScale=geo.scale,axisRadii=[geo.A,geo.Baxis],
                planarMouthWidth=.27,materialCenters=[PHASE/2-a.anchor,PERIOD+PHASE/2-a.anchor],
                heldRelativeTranslation=2*np.sqrt(3)*abs(geo.A-1/LOW)*np.sin(LOW*PHASE/2),gridComparisons=obs)

def run(a):
    S=a.scripts
    micro=module(S/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','R262DA')
    comparison=module(a.comparison,'R262OriginalArcMap')
    cut=module(a.cut,'R262ActualAdjacentLowCut')
    cut.true_arc_position=true_arc_position
    make_grid=cut.make_grid
    D3=cut.D3
    geo=NormalCurve()
    obs=compare(a,comparison,geo)
    if a.compare_only:
        with a.out.open('x') as f:json.dump(obs,f,indent=2);f.write('\n')
        print('ADJACENT_ACTUAL_ORIGINAL',json.dumps(obs['gridComparisons']),flush=True)
        return
    W=a.work;fielddir=W/'h2-c2-m48-g12-04r1'
    a.data=W/'m12-prefix-data.npz.gz';a.grid=fielddir/'grid.json'
    a.query_report=fielddir/'exact-tail-queries.json';a.query_cache=Path(str(a.query_report)+'.npz');a.field=fielddir/'result.json.field.npz'
    src=micro.Source(a)
    orig=None  # Unit-speed target uses the original material-angle map directly.
    P,parent,rows=make_grid(micro,src,geo,orig,a,a.radial,a.angles,False)
    proj=D3(P)
    nx=proj.size
    x=np.zeros(nx+2*P.nb)
    if a.seed:
        with np.load(a.seed) as z:
            if str(z['sourceSHA'])!=digest(Path(__file__)) or str(z['fieldSHA'])!=src.source_sha or float(z['fullSleeve'])!=a.full_sleeve or float(z['fullGate'])!=a.full_gate or float(z['liftEnd'])!=a.lift_end:raise ValueError('Seed source or surgery differs')
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
    with state.open('xb') as f:np.savez_compressed(f,fieldSHA=src.source_sha,sourceSHA=digest(Path(__file__)),comparisonSHA=digest(a.comparison),cutSHA=digest(a.cut),S=src.S,T=src.T,fullGate=a.full_gate,fullSleeve=a.full_sleeve,liftEnd=a.lift_end,reduced=x,actualPhysicalXYZ=X,metricQ=metric['q'],metricW=metric['w'],knots=P.kn,lam=a.lam,low=a.low,anchor=a.anchor,modes=a.modes,spans=a.spans)
    out=dict(schema='R262-original-cut-adjacent-low-ports-physical-source-v1',sourceSHA=digest(Path(__file__)),comparisonSHA=digest(a.comparison),fieldSHA=src.source_sha,historicalMatch=src.source_sha==micro.HISTORICAL,originalDataSHA=digest(a.data),stateSHA=digest(state),lam=a.lam,low=a.low,phase=PHASE,anchor=a.anchor,centralOriginalComparison=obs,cutSHA=digest(a.cut),
             numericalPhysicalCoordinates=dict(S=src.S,T=src.T,halfSleeve=a.full_sleeve*a.lam,gateLength=a.full_gate*a.lam,liftEnd=a.lift_end),nativeD3Correction=dict(angularModes=a.modes,radialSpans=a.spans,independentRealPositionVariables=nx,positiveMetricVariables=2*P.nb),circlePort=dict(unitSpeedCenters=obs['materialCenters'],phaseInterval=[0,PHASE],normalAnglePlateau=[-V0,V0],width=.27),
             trueOriginalPrefixAtProbeRows=rows,originalTraining=parent,originalIndependent=oldQ,initial=init,accepted=history,finalTraining=final,finalIndependent=ind,independentPhysicalGeometry=micro.physical_geometry(Q,X.ravel()),
             metricDefinition=dict(base='radial one times unit native arclength on sleeve, smooth blend to old radial reference; both positive multipliers vanish as perturbations at sleeve and old prefix end',**metric),
             fullDomain='Beyond the original prefix end the original continuous oscillating tail and its entire input-specific physical field have the same position, the same old metric, and the same true cuff. Positive/negative original cap shapes are replaced by their true flat disks. No new displacement, total height, or old bound is assigned to the compact changed prefix.',
             scope='The adjacent constant-curvature windows have distinct centers. Their relative translations vary along the true material phase. The actual thick arms are external to this prefix experiment. Closed shape, quantitative reach and full-domain metric tolerance require their own continuous certificates.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('FINAL',a.lam,init,ind,'historical',out['historicalMatch'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','work','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--comparison',type=Path)
    p.add_argument('--cut',type=Path)
    p.add_argument('--compare-only',action='store_true')
    p.add_argument('--compare-nodes',type=int,default=4096)
    p.add_argument('--seed',type=Path)
    p.add_argument('--anchor',type=float,default=HALF)
    for k,v in (('full-sleeve',.78),('full-gate',.40),('lift-end',1.5),('curvature-guide',8.85)):
        p.add_argument('--'+k,type=float,default=v)
    for k,v in (('spans',20),('modes',18),('angles',120),('radial',62),('test-angles',195),('test-radial',103),('steps',4),('iterations',110),('arc-nodes',24576)):
        p.add_argument('--'+k,type=int,default=v)
    a=p.parse_args()
    a.low=LOW
    a.lam=1.
    if a.comparison is None:a.comparison=a.scripts/'2ecf-r262-three-circular-arcs-material-comparison.py'
    if a.cut is None:a.cut=a.scripts/'2ecf-r262-three-arcs-shortened-prefix-v2.py'
    run(a)
