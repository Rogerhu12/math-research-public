#!/usr/bin/env python3
"""Adjacent true material circle ports with a shorter phase and a normalized material-curvature return."""
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
LOW=0.617
PHASE=1.035
PLATEAU=.790
RISE=.304
ADJUST=np.array([.480,-.221,.135])
# The original twelve R21 support coefficients define the smooth ambient reference curve.
CS=np.array([0.09999976505231697,0.00017340635052370438,-0.000020726030862500148,2.732239542665825e-9,1.364904959536114e-9,-6.697024595314116e-10,2.5420195020236015e-11,2.7693941053364423e-11,2.279645039764186e-11,7.050341026639808e-10,5.749608505622311e-11,2.4233142751359304e-10])
J=np.arange(1,len(CS)+1)
B=(1-9*J**2)*(-1.)**J*CS
F=3*J
GN,GW=np.polynomial.legendre.leggauss(16)
HARM=np.arange(1,4)*np.pi
WIDTH=HALF-PLATEAU
JOINS=np.array([PLATEAU,PLATEAU+RISE*WIDTH,HALF])
def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj;spec.loader.exec_module(obj)
    return obj
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def support_inverse(u):
    u=np.asarray(u);flat=u.reshape(-1)
    v=flat.copy()
    # Safeguarded Newton on the monotone material primitive.
    lo=np.zeros_like(v);hi=np.full_like(v,HALF)
    for _ in range(40):
        a=v[:,None]*F;cos=np.cos(a);sin=np.sin(a)
        r=1+cos@B;err=v+sin@(B/F)-flat
        done=abs(err)<7e-15
        if np.all(done):break
        lo=np.where(err<=0,v,lo);hi=np.where(err>=0,v,hi)
        nxt=v-err/r
        v=np.where(done,v,np.where((nxt>lo)&(nxt<hi),nxt,(lo+hi)/2))
    else:raise ArithmeticError('Physical baseline inverse was not enclosed numerically')
    r1=-sin@(B*F);r2=-cos@(B*F*F)
    return [z.reshape(u.shape) for z in (v,1/r,-r1/r**3,3*r1*r1/r**5-r2/r**4)]
def switch(x):
    t=np.clip(x,0,1);on=(x>0)&(x<1)
    s=t**3*(10+t*(-15+6*t))
    return s,30*t*t*(1-t)**2*on,60*t*(1-t)*(1-2*t)*on
def integrate(fun,lo,hi):
    lo,hi=np.broadcast_arrays(lo,hi);d=(hi-lo)/2
    return np.einsum('...j,j->...',fun((hi+lo)[...,None]/2+d[...,None]*GN),GW)*d
class NormalCurve:
    LOW=LOW
    P=PERIOD
    def __init__(self):
        self.u0=PLATEAU
        self.edges=np.unique(np.r_[0.,PLATEAU,np.linspace(JOINS[0],JOINS[1],13),np.linspace(JOINS[1],HALF,25)])
        self.bias=0.
        L,R=self.edges[:-1],self.edges[1:]
        mass=integrate(lambda u:self.positive_jets(u)[0],L,R).sum()
        denom=HALF-PLATEAU-RISE*WIDTH/2
        self.bias=(HALF-mass)/denom
        # Antiderivative tables are numerical evaluations of the same physical integrals.
        # Use one polynomial per smooth subinterval, and integrate the Chebyshev series before evaluation.
        self.bpoly=[];self.ppoly=[];beta=0.;spatial=0j
        xs=np.cos(np.arange(25)*np.pi/24)
        forward=np.linalg.inv(np.polynomial.chebyshev.chebvander(xs,24))
        self.tableDisagreement=0.
        for l,r in zip(L,R):
            mid=(r+l)/2;h=(r-l)/2
            kval=self.positive_jets(mid+h*xs)[0]
            coeff=np.polynomial.chebyshev.chebint(forward@kval)*h
            coeff[0]+=beta-np.polynomial.chebyshev.chebval(-1,coeff)
            beta=np.polynomial.chebyshev.chebval(1,coeff);self.bpoly.append(coeff)
            vector=np.exp(1j*np.polynomial.chebyshev.chebval(xs,coeff))
            pc=np.polynomial.chebyshev.chebint(forward@vector)*h
            pc[0]+=spatial-np.polynomial.chebyshev.chebval(-1,pc)
            delta=np.polynomial.chebyshev.chebval(1,pc)-spatial
            check=h*np.dot(np.exp(1j*np.polynomial.chebyshev.chebval(GN,coeff)),GW)
            self.tableDisagreement=max(self.tableDisagreement,abs(delta-check))
            spatial+=delta;self.ppoly.append(pc)
        if abs(beta-HALF)>2e-12 or self.tableDisagreement>2e-12:
            raise ArithmeticError('Material curve quadrature agreement failed')
        self.bpoly=np.asarray(self.bpoly);self.ppoly=np.asarray(self.ppoly)
        self.A=float(spatial.imag+spatial.real/np.tan(HALF))
        self.Baxis=float(spatial.real/np.sin(HALF))
    def positive_jets(self,u):
        u=np.asarray(u);t=(u-PLATEAU)/WIDTH;gate,g1,g2=switch(t/RISE)
        g1/=(WIDTH*RISE);g2/=(WIDTH*RISE)**2
        _,b,b1,b2=support_inverse(u)
        a=t[...,None]*HARM;co,si=np.cos(a),np.sin(a)
        e=b+self.bias+co@ADJUST-LOW
        a1=b1-si@(ADJUST*HARM/WIDTH)
        a2=b2-co@(ADJUST*(HARM/WIDTH)**2)
        return [LOW+gate*e,g1*e+gate*a1,g2*e+2*g1*a1+gate*a2]
    def idx(self,u):
        return np.clip(np.searchsorted(self.edges,u,side='right')-1,0,len(self.edges)-2)
    def tables(self,u):
        v=np.asarray(u);i=self.idx(v)
        x=(2*v-self.edges[i]-self.edges[i+1])/(self.edges[i+1]-self.edges[i])
        b=np.polynomial.chebyshev.chebval(x,self.bpoly[i].T,tensor=False)
        z=np.polynomial.chebyshev.chebval(x,self.ppoly[i].T,tensor=False)
        return b,z
    def at(self,u,anchor):
        ua=np.asarray(u)+anchor;sector=np.floor((ua+HALF)/PERIOD);r=ua-sector*PERIOD
        q=np.minimum(abs(r),HALF);beta,base=self.tables(q);curv=self.positive_jets(q)[0]
        rot=sector*PERIOD-anchor;sign=np.sign(r)
        return np.exp(1j*rot)*(self.A-base.imag+1j*sign*base.real),rot+sign*beta,curv
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
    v=np.linspace(0,HALF,max(4096,2*a.compare_nodes)+1)
    k0,k1,k2=geo.positive_jets(v)
    h2=6*k1*k1/k0**4-2*k2/k0**3
    n2=np.hypot(2*k1*k1/k0**3-k2/k0**2-k0,k1/k0)
    return dict(schema='true-R262-material-unit-speed-curvature-window-inlet',inputSHA=digest(data),entrySHA=digest(__file__),
                comparisonSHA=digest(a.comparison),cutSHA=digest(a.cut),materialPlateau=PLATEAU,phase=PHASE,k=LOW,anchor=a.anchor,
                rise=RISE,materialWidth=WIDTH,bias=geo.bias,radiusModulation=ADJUST.tolist(),axisRadii=[geo.A,geo.Baxis],
                gridComparisons=obs,observedInletSecondDerivativePeaks=[float(n2.max()),float(abs(h2).max())],
                materialCenters=[PHASE/2-a.anchor,PERIOD+PHASE/2-a.anchor],
                heldRelativeTranslation=2*np.sqrt(3)*abs(geo.A-1/LOW)*np.sin(LOW*PHASE/2))

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
    out=dict(schema='R262-original-cut-physical-material-curvature-k617-eta1035-v1',sourceSHA=digest(Path(__file__)),comparisonSHA=digest(a.comparison),fieldSHA=src.source_sha,historicalMatch=src.source_sha==micro.HISTORICAL,originalDataSHA=digest(a.data),stateSHA=digest(state),lam=a.lam,low=a.low,phase=PHASE,anchor=a.anchor,centralOriginalComparison=obs,cutSHA=digest(a.cut),
             numericalPhysicalCoordinates=dict(S=src.S,T=src.T,halfSleeve=a.full_sleeve*a.lam,gateLength=a.full_gate*a.lam,liftEnd=a.lift_end),nativeD3Correction=dict(angularModes=a.modes,radialSpans=a.spans,independentRealPositionVariables=nx,positiveMetricVariables=2*P.nb),circlePort=dict(unitSpeedCenters=obs['materialCenters'],phaseInterval=[0,PHASE],normalAnglePlateau=[-LOW*PLATEAU,LOW*PLATEAU],width=.27),
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
