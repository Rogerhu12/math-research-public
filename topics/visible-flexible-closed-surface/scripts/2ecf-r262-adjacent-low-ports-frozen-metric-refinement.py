#!/usr/bin/env python3
"""Freeze a completed true-arc R262 design and refine its actual Cartesian position, retaining both positive radial functions."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import lsmr

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def action_args(a,z):
    for key,col in (('S','S'),('T','T'),('full_sleeve','fullSleeve'),('full_gate','fullGate'),('lift_end','liftEnd'),('low','low'),('anchor','anchor'),('lam','lam')):
        setattr(a,key,float(z[col]))
    if a.lam!=1:raise ValueError('Require the full true arc')
    a.extra={}
    if 'heightDropEnd' in z:
        a.height_drop_end=float(z['heightDropEnd'])
        a.extra['heightDropEnd']=a.height_drop_end
    if 'rawDropVelocity' in z:
        from fractions import Fraction
        kn=np.asarray(z['rawDropKnots']);v=np.asarray(z['rawDropVelocity'])
        total=sum(Fraction(float(value))*(Fraction(float(kn[i+9]))-Fraction(float(kn[i+3])))/6 for i,value in enumerate(v))
        c=a.full_sleeve;H=a.height_drop_end
        if total<=0:raise ValueError('Invalid exact vertical allocation')
        sp=BSpline(kn,np.pad(v,(3,3))*float(Fraction(c)/total),5,extrapolate=False)
        pr=sp.antiderivative()
        def drop(t):
            s=np.clip(t,0.,H)
            height=np.where(t>=H,c,np.where(t<=0,0.,pr(s)-pr(0.)))
            return height/c,sp(s)/c,sp(s,1)/c
        a.drop=drop
        a.extra.update(rawDropKnots=kn,rawDropVelocity=v)
    fld=a.work/'h2-c2-m48-g12-04r1'
    a.data=a.work/'m12-prefix-data.npz.gz'
    a.grid=fld/'grid.json'
    a.query_report=fld/'exact-tail-queries.json';a.query_cache=Path(str(a.query_report)+'.npz')
    a.field=fld/'result.json.field.npz'
    if str(z['fieldSHA'])!=sha(a.field) or str(z['sourceSHA'])!=sha(a.physical_source) or str(z['comparisonSHA'])!=sha(a.comparison):
        raise ValueError('Frozen actual field or geometric definition differs')

def refine(parentkn,pos,mnew):
    m=(pos.shape[1]-2)//3
    if mnew<m:raise ValueError('Angular modes must contain parent')
    knots=np.asarray(parentkn,float)
    unique=np.unique(knots)
    mids=unique[:-1]+np.diff(unique)/2
    spl=BSpline(knots,np.pad(pos,((3,3),(0,0))),5,axis=0)
    for v in mids:spl=spl.insert_knot(v)
    p=spl.c[3:-3];x=np.zeros((len(p),3*mnew+2))
    if np.any(spl.c[:3]) or np.any(spl.c[-3:]):raise ValueError('Clamped zero two-jets not preserved')
    x[:,:m+1]=p[:,:m+1]
    x[:,mnew+1:mnew+m+1]=p[:,m+1:2*m+1]
    x[:,2*mnew+1:2*mnew+m+2]=p[:,2*m+1:]
    return spl.t.copy(),x

def pack(proj,X):
    x=X[:,[s[0][0] for s in proj.cols]].ravel()
    if not np.array_equal(proj.expand(x),X.ravel()):raise ValueError('Parent not in full D3 subspace')
    return x

def grid(api,micro,src,geo,a,kn,metric,nr,nu,shift):
    G,parent,rows=api.make_grid(micro,src,geo,None,a,nr,nu,shift,metric)
    G.kn=kn;G.B=api.Bvals(G.t*src.S,kn)
    G.nb=G.B[0].shape[1];G.shape=(G.nb,G.na);G.nx=G.nb*G.na;G.nvar=G.nx
    return G

def geometry(G,x):
    J,Q,W,lo=G.jets(x)
    p=J[:,0];n=np.cross(J[:,2],J[:,1]);area=np.linalg.norm(n,axis=-1)
    sig=np.sum(p*n,axis=-1)/area
    iz=np.unravel_index(np.argmin(sig),sig.shape)
    return dict(minimumOutwardSupport=float(sig.min()),at=[float(G.t[iz[0]]*G.source.S),float(G.u[iz[1]])],
                minimumRadialHeightDerivative=float(J[:,1,:,2].min()),heightRange=[float(p[...,2].min()),float(p[...,2].max())],
                maximumOriginNorm=float(np.linalg.norm(p,axis=-1).max()),minimumArea=float(area.min()))

def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','work','physical-source','comparison','parent','out'):
        p.add_argument('--'+k,type=Path,required=True)
    for k,d in (('modes',30),('angles',162),('radial',105),('test-angles',273),('test-radial',183),('steps',4),('iterations',130)):
        p.add_argument('--'+k,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.85)
    p.add_argument('--cut',type=Path)
    a=p.parse_args()
    if a.cut is None:a.cut=a.scripts/'2ecf-r262-three-arcs-shortened-prefix-v2.py'
    physical=module(a.physical_source,'r262_adjacent_true_physical')
    if sha(a.physical_source)!='94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6':
        raise ValueError('The frozen source must be the actual adjacent-port family')
    api=module(a.cut,'r262_adjacent_cut_sampler')
    api.true_arc_position=physical.true_arc_position
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','r262_positive_radius_source')
    geo=physical.NormalCurve()
    with np.load(a.parent) as z:
        action_args(a,z)
        if str(z['cutSHA'])!=sha(a.cut) or a.low!=physical.LOW:
            raise ValueError('Parent cut or low-circle geometry differs')
        a.extra['cutSHA']=str(z['cutSHA'])
        originalKn=z['knots'].copy();oldX=z['actualPhysicalXYZ'].copy()
        if 'metricKnots' in z:mk=z['metricKnots'].copy()
        else:mk=originalKn
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
    src=micro.Source(a)
    if (src.S,src.T)!=(a.S,a.T):raise ValueError('Parent material lengths differ')
    kn,coeff=refine(originalKn,oldX,a.modes)
    a.spans=len(np.unique(kn))-1
    G=grid(api,micro,src,geo,a,kn,metric,a.radial,a.angles,False)
    proj=api.D3(G);x=pack(proj,coeff)
    X0=proj.expand(x);before=G.report(X0);geom0=geometry(G,X0)
    q=np.linspace(originalKn[0],originalKn[-1],513)
    op=BSpline(originalKn,np.pad(oldX,((3,3),(0,0))),5,axis=0)
    np0=BSpline(kn,np.pad(coeff,((3,3),(0,0))),5,axis=0)
    oldm=(oldX.shape[1]-2)//3
    keep=np.r_[np.arange(oldm+1),np.arange(a.modes+1,a.modes+oldm+1),np.arange(2*a.modes+1,2*a.modes+oldm+2)].astype(int)
    trans=[float(np.max(np.abs(op(q,j)-np0(q,j)[:,keep]))) for j in range(3)]
    Q=grid(api,micro,src,geo,a,kn,metric,a.test_radial,a.test_angles,True)
    independent0=Q.report(X0)
    history=[]
    for i in range(a.steps):
        full=proj.expand(x);b0=G.report(full)
        power=.45 if i<2 else .95
        pwr=5 if i<2 else 8
        lin,r,scale=proj.model(x,power)
        val0,peak0=G.objective(full,pwr)
        best=None
        for damp in (1e-6,3e-5,5e-4):
            dx=scale*lsmr(lin,-r,atol=2e-10,btol=2e-10,damp=damp,maxiter=a.iterations)[0]
            for alpha in (1.,.5,.25,.125,.0625):
                y=x+alpha*dx;yy=proj.expand(y);val,peak=G.objective(yy,pwr)
                if val>=val0 or peak>=peak0:continue
                report=G.report(yy)
                if report['curvature']>max(a.curvature_guide,b0['curvature']+1e-5):continue
                score=val+.18*peak
                if best is None or score<best[0]:best=(score,y,report,alpha,damp)
        if best is None:break
        _,x,report,alpha,damp=best
        history.append(dict(step=i+1,scale=alpha,damping=damp,training=report))
        print('ACCEPT FROZEN',i+1,report,flush=True)
    full=proj.expand(x);X=full.reshape(G.shape)
    stat=a.out.with_suffix('.npz')
    with stat.open('xb') as f:
        np.savez_compressed(f,fieldSHA=src.source_sha,sourceSHA=sha(a.physical_source),comparisonSHA=sha(a.comparison),S=src.S,T=src.T,fullGate=a.full_gate,fullSleeve=a.full_sleeve,liftEnd=a.lift_end,reduced=x,actualPhysicalXYZ=X,metricQ=metric['q'],metricW=metric['w'],metricKnots=mk,knots=kn,lam=a.lam,low=a.low,anchor=a.anchor,modes=a.modes,spans=a.spans,**a.extra)
    out=dict(schema='R262-adjacent-true-common-curvature-ports-frozen-metric-actual-h-refinement',
        entrySHA256=sha(__file__),physicalSourceSHA256=sha(a.physical_source),comparisonSHA256=sha(a.comparison),parentSHA256=sha(a.parent),fieldSHA256=src.source_sha,historicalMatch=src.source_sha==micro.HISTORICAL,stateSHA256=sha(stat),low=a.low,phase=physical.PHASE,cutSHA256=sha(a.cut),trueNormalEndpointAngles=[physical.V0,physical.V1],newAxisRadii=[geo.A,geo.Baxis],lam=a.lam,anchor=a.anchor,
        angularModes=a.modes,radialSpans=a.spans,actualPositionDOFs=proj.size,metricDOFs=0,
        frozenMetric=dict(unitMaterialAngle='original normalized R262 arclength',**metric),knotTransferMaxActual0th1st2nd=trans,
        initialTraining=before,initialShifted=independent0,initialGeometry=geom0,accepted=history,training=G.report(full),independent=Q.report(full),independentGeometry=geometry(Q,full),geometryFamily=('original-ring-complete axial allocation' if hasattr(a,'height_drop_end') else 'shortened interior surgery'),
        scope='The genuine full plateaux, original material angle, compact cut and both fixed radial functions are retained. Reports are finite grid observations; strict geometry and continuous Gram bounds are separate.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('REFINED FROZEN',a.low,out['independent'],flush=True)
if __name__=='__main__':main()
