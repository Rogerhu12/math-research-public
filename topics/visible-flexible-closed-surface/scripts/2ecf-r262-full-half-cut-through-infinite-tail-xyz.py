#!/usr/bin/env python3
"""Add one physical XYZ field across the actual R317-family prefix, common cut, entire infinite tail and true flat cuff, retaining the fixed g."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
from types import SimpleNamespace
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def field_basis(api,kn,xi,H,Hq,c,T):
    span=T-c;t=(xi-c)/span
    t=np.where(xi<=c,0.,np.where(xi>=T,1.,t))
    B=api.Bvals(t,kn)
    # For xi<c this complete correction vanishes on an open sleeve.
    use=(xi>=c)&(xi<=T)
    b1=B[1]/(span*H[:,None])
    b2=B[2]/(span*H[:,None])**2-B[1]*Hq[:,None]/(span*H[:,None]**3)
    return [x*use[:,None] for x in (B[0],b1,b2)]
def original_knots(oldkn,c,S,T,tail_count):
    # Save unit knots; 0,1 stand for the actual physical sleeve and true cuff.
    x=np.unique(np.r_[oldkn,np.linspace(S,T,tail_count+1)])
    v=np.unique(np.clip((x-c)/(T-c),0.,1.))
    return np.r_[np.zeros(5),v,np.ones(5)]
def actual_tail_nodes(src,record,role):
    mesh=np.asarray(record['unit_mesh'],float);ng=int(record['gauss'])
    g=ng if role==0 else ng+2;weights=np.polynomial.legendre.leggauss(g)[0]
    z=(mesh[:-1,None]+mesh[1:,None])/2+np.diff(mesh)[:,None]*weights/2
    mask=np.broadcast_to(np.arange(g)[None,:],z.shape)
    cut=np.asarray(z,np.longdouble)*src.chart.total>src.chart.S
    if role==1:cut=cut&(mask%2==0)
    if role==2:cut=cut&(mask%2==1)
    return np.unique(np.r_[z[cut],1.])
def tail_data(src,ss,zs):
    n=len(ss.theta);angle=ss.chart[n][:3]
    base=src.pos;old=base.angular_cache.get(n);base.angular_cache[n]=angle
    try:
        rows=[];rhos=[];rads=[]
        for zz in zs:
            r=src.chart.radius(zz)[0];J,b=base.tail_point(r,n)
            rows.append(J);rhos.append(b);rads.append(float(r))
        seam,seamrho=base.tail_point(src.chart.c,n)
    finally:
        if old is None:base.angular_cache.pop(n,None)
        else:base.angular_cache[n]=old
    H,Hq=src.chart.scales(zs)
    J=np.asarray(rows);rr=np.asarray(rhos)
    def restore(jet,z,h,hq):
        co=[src.spline(z,k) for k in range(3)]
        co[2]=co[2]/(src.T*h[:,None])**2-co[1]*hq[:,None]/(src.T*h[:,None]**3);co[1]/=src.T*h[:,None]
        for j,(r,d) in enumerate(src.base.O):
            f=(co[r][:,:len(src.pm)]*(1j*src.pm)**d)@ss.ep
            v=(co[r][:,len(src.pm):]*(1j*src.hm)**d)@ss.eh
            jet[:,j]+=np.stack((f.real,f.imag,v.real),axis=-1)
    restore(J,zs,H,Hq)
    restore(seam[None],np.array([float(src.chart.S/src.chart.total)]),np.array([1.]),np.array([0.]))
    return J,rr,H,Hq,np.asarray(rads),seam,seamrho
def parent_prefix(src,ss,mm,ref,api,geo,phys,adj,a,th,oldkn,sampling_knots,old,extra,metric,nr,sh,heatdata,heat):
    m=a.modes;a.modes=0
    try:g=ref.cut_grid(api,mm,ss,geo,a,sampling_knots,metric,nr,len(th),sh)
    finally:a.modes=m
    q=g.t*src.S;J=g.base.copy()
    if heatdata:
        gain,order,horder,time,late=heatdata
        H=heat.HeatOrbit(phys,geo,a,ss,api,th,int(order),int(horder),time,late)
        J+=gain*H.correction(q,J)
    B=api.Bvals(q,oldkn);mold=(old.shape[1]-2)//3
    extraPhi=adj.angles_profile(phys,api,ss,geo,a,len(th),sh)[0] if extra is not None else None
    for j,(r,d) in enumerate(src.base.O):
        J[:,j]+=mm.fft_forward(B[r]@old,mold,len(th),th[0],d)
        if extra is not None:
            c=B[r]@extra
            for k in range(3):J[:,j,:,k]+=c@extraPhi[d,k]
    Q=1+g.M@np.asarray(metric['q']);W=1+g.M@np.asarray(metric['w'])
    return q,J,g.rho,Q,W
def record_geometry(G,X,src,ix):
    r=G.report(X);J=G.base.copy()
    for j,(p,d) in enumerate(G.orders):J[:,j]+=G.forward_field(X,p,d)
    _,e,_=G.micro.gram(J,G.Q,G.W,G.rho);cur,_=G.micro.curvature(J)
    r['prefixPeak']=float(np.max(e[:ix]));r['tailPeak']=float(np.max(e[ix:]))
    r['prefixCurvature']=float(np.max(cur[:ix]));r['tailCurvature']=float(np.max(cur[ix:]))
    for key in ('worstMetric','worstCurvature'):
        x=r[key][0];r[key+'TailRadius']=float(src.chart.radius(x/src.T)[0]) if x>src.S else None
    return r

def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','work','physical-source','cut','comparison','refinement-source','adjacent-source','angular-source','direct-source','parent','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--heat-source',type=Path);p.add_argument('--seed',type=Path);p.add_argument('--split',action='store_true')
    p.add_argument('--tail-spans',type=int,default=12);p.add_argument('--modes',type=int,default=36);p.add_argument('--steps',type=int,default=5)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    phys=module(a.physical_source,'whole_tail_actual_adjacent_ports');api=module(a.cut,'whole_tail_actual_physical_cut')
    geo=phys.NormalCurve();api.true_arc_position=phys.true_arc_position
    ref=module(a.refinement_source,'whole_tail_all_spans');ar=module(a.angular_source,'whole_tail_cartesian_expansion')
    adj=module(a.adjacent_source,'whole_tail_true_material_targets');direct=module(a.direct_source,'whole_tail_banded')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','whole_tail_original_E3')
    heatdata=None;heat=None
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z or str(z['cutSHA'])!=sha(a.cut) or a.low!=phys.LOW:raise ValueError('Parent is a different half-map')
        if 'heatGain' in z:
            if a.heat_source is None or str(z['heatSourceSHA'])!=sha(a.heat_source):raise ValueError('Missing actual parent heat source')
            old=z['heatInletXYZ'].copy();extra=z['heatInletProfiles'].copy();heatdata=[float(z[k]) for k in ('heatGain','heatOrder','heightOrder','heatAmplitude','heatLate')]
            heat=module(a.heat_source,'whole_tail_actual_parent_heat')
        elif 'physicalInletProfiles' in z:
            old=z['inletNativeXYZ'].copy();extra=z['physicalInletProfiles'].copy()
        else:old=z['actualPhysicalXYZ'].copy();extra=None
        if extra is not None and str(z['inletProfileSourceSHA'])!=sha(a.adjacent_source):raise ValueError('Different physical inlet profiles')
        oldkn=z['knots'].copy()
        mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
    src=micro.Source(a);record=json.loads(a.grid.read_text())
    if (src.S,src.T)!=(a.S,a.T):raise ValueError('Physical common chart differs')
    a.spans=len(np.unique(oldkn))-1;a.material_modes=a.modes
    if a.seed is None:
        kn=original_knots(oldkn,a.full_sleeve,src.S,src.T,a.tail_spans)
        seed=np.zeros((len(kn)-12,3*a.modes+2))
    else:
        with np.load(a.seed,allow_pickle=False) as s:
            if str(s['parentSHA'])!=sha(a.parent) or str(s['sourceSHA'])!=sha(__file__) or str(s['fieldSHA'])!=src.source_sha:raise ValueError('Different full-half family')
            kn,seed=direct.transfer(s['unitKnots'].copy(),s['wholeTailXYZ'].copy(),a.modes,a.split)
    phys_kn=a.full_sleeve+(src.T-a.full_sleeve)*kn
    breaks=np.unique(np.r_[a.full_sleeve,oldkn,phys_kn[(phys_kn>a.full_sleeve+1e-13)&(phys_kn<src.S-1e-13)],src.S])
    sampling_knots=np.r_[np.full(5,a.full_sleeve),breaks,np.full(5,src.S)]
    def model(role,nr,n,nt,shift):
        th,ang=adj.node_angles(src,phys,geo,a,n,nt,shift);half=np.pi/3
        th=np.sort(np.r_[0.,th[(th>1e-11)&(th<half-1e-11)],half]);th=th[np.r_[True,np.diff(th)>1e-11]]
        ss=adj.SourceAt(src,th);mm=adj.AtAngles(micro,th)
        q0,J0,r0,Q0,W0=parent_prefix(src,ss,mm,ref,api,geo,phys,adj,a,th,oldkn,sampling_knots,old,extra,metric,nr,shift,heatdata,heat)
        zs=actual_tail_nodes(src,record,role);J1,r1,H,Hq,r,other,otherRadius=tail_data(src,ss,zs)
        delta=np.max(np.linalg.norm(J0[-1]-other,axis=-1),axis=-1)
        q=np.r_[q0,zs*src.T];allH=np.r_[np.ones(len(q0)),H];allHq=np.r_[np.zeros(len(q0)),Hq]
        B=field_basis(api,kn,q,allH,allHq,a.full_sleeve,src.T)
        G=ar.Model.__new__(ar.Model);G.G=SimpleNamespace(t=q/src.S,u=th,source=ss);G.micro=micro
        G.B=B;G.ch=ar.channels(a.modes);G.phi=np.zeros((3,3,len(G.ch),len(th)));direct.native_basis(G,th)
        G.shape=(len(kn)-12,len(G.ch));G.nvar=int(np.prod(G.shape));G.orders=src.base.O;G.base=np.concatenate((J0,J1))
        G.rho=np.concatenate((r0,r1));G.Q=np.r_[Q0,np.ones(len(zs))][:,None];G.W=np.r_[W0,np.ones(len(zs))][:,None]
        G.u=src.center.arc(th)
        for j,(i,d) in enumerate(G.orders):G.base[:,j]+=mm.fft_forward(B[i]@seed,a.modes,len(th),th[0],d)
        seamB=np.asarray([v[-1] for v in field_basis(api,kn,np.array([src.S]),np.ones(1),np.zeros(1),a.full_sleeve,src.T)])
        return G,len(q0),dict(angular=ang,actualAngles=len(th),prefixRows=len(q0),exactTailRadiusQueries=len(zs),originalGauss=int(record['gauss']),
                     tailSplit=['all original training rule','even local indices in original higher rule','odd local indices in original higher rule'][role],trueCuff=float(src.chart.cuff),
                     minimumTailH=float(H.min()),maximumTailH=float(H.max()),minimumTailRadius=float(r.min()),maximumTailRadius=float(r.max()),
                     baseSixJetTraceDifference=delta.tolist(),baseAngularRadiusTraceDifference=float(np.max(abs(r0[-1]-otherRadius))),
                     commonCutTraceMapRank=int(np.linalg.matrix_rank(seamB)),positiveInteriorSupportColumns=int(np.sum(abs(seamB[0])>1e-14)))
    G,ix,ga=model(0,113,240,15,False);T,jx,ta=model(1,173,351,25,True)
    X=np.zeros(G.shape);initial=record_geometry(G,X,src,ix);second=record_geometry(T,X,src,jx)
    hist=[];verify=None
    for step in range(a.steps):
        before=G.report(X);other=T.report(X);peak=max(before['peak'],other['peak']);best=None
        for power in (.65,1.7):
            ab,grad=direct.assemble(G,X,power)
            if verify is None:verify=direct.check_normal(G,X,power,ab,grad)
            sc=1/np.sqrt(np.maximum(1e-25,ab[0]));nn=len(sc)
            for d in range(min(nn,len(ab))):ab[d,:nn-d]*=sc[d:]*sc[:nn-d]
            diag=ab[0].copy()
            for mu in (1e-11,1e-8,1e-5,.002):
                ab[0]=diag+mu
                try:dx=(sc*solveh_banded(ab,-sc*grad,lower=True,check_finite=False)).reshape(X.shape)
                except LinAlgError:continue
                options=[]
                for al in 2.**(-np.arange(0,25)/2):
                    y=X+al*dx;pk=max(G.metrics(y)[3].max(),T.metrics(y)[3].max())
                    if pk<peak*(1-1e-11):options.append((pk,float(al)))
                for pk,al in sorted(options):
                    if best is not None and pk>=best[0]:break
                    y=X+al*dx;r=G.report(y);s=T.report(y)
                    if r['curvature']>max(a.curvature_guide,before['curvature']+1e-6) or s['curvature']>max(a.curvature_guide,other['curvature']+1e-6):continue
                    if min(r['minimumSupport'],s['minimumSupport'])<min(.115,before['minimumSupport'],other['minimumSupport']):continue
                    best=(pk,y,r,s,al,power,mu);break
            if best is not None:break
        if best is None:break
        _,X,r,s,al,power,mu=best;hist.append(dict(step=step+1,alpha=al,weight=power,diagonalDamping=mu,training=record_geometry(G,X,src,ix),shifted=record_geometry(T,X,src,jx)))
        print('ACCEPT_FULL_TRUE_TAIL',step+1,r,s,flush=True)
    total=seed.copy();m=a.modes
    for j,(tag,k) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+k]+=X[:,j]
        else:total[:,abs(k)]+=X[:,j];total[:,m+abs(k)]+=np.sign(k)*X[:,j]
    del G,T
    U,kx,ua=model(2,219,621,47,False);baseheld=record_geometry(U,0*X,src,kx);end=record_geometry(U,X,src,kx)
    Bc=field_basis(api,kn,np.array([src.S]),np.ones(1),np.zeros(1),a.full_sleeve,src.T)
    seam=[float(np.max(np.abs(b@total))) for b in Bc]
    ends=field_basis(api,kn,np.array([a.full_sleeve,src.T]),np.ones(2),np.zeros(2),a.full_sleeve,src.T)
    sf=a.out.with_suffix('.npz')
    with sf.open('xb') as f:np.savez_compressed(f,sourceSHA=sha(__file__),parentSHA=sha(a.parent),fieldSHA=src.source_sha,unitKnots=kn,wholeTailXYZ=total,modes=a.modes,c=a.full_sleeve,actualCommonCut=src.S,actualCuffCoordinate=src.T)
    out=dict(schema='actual-new-strong-half-same-metric-full-XYZ-across-r06-to-the-true-cuff-v1',sourceSHA=sha(__file__),parentSHA=sha(a.parent),fieldSHA=src.source_sha,stateSHA=sha(sf),
             exactTailQueryReportSHA=sha(a.query_report),exactTailQueryCacheSHA=sha(a.query_cache),seedSHA=sha(a.seed) if a.seed else None,radialUnitSpans=len(np.unique(kn))-1,positionVariables=int(X.size),metricVariables=0,
             physicalCommonCut=src.S,physicalCuffCoordinate=src.T,grids=[ga,ta,ua],actualMeanAndFullFrequencyCommonCutCoefficientTraceMax=seam,actualTwoEndpointBasisZeroJets=[float(np.max(abs(b))) for b in ends],
             initial=initial,initialSecondary=second,accepted=hist,matrixAndRhsAgreement=verify,initialIndependent=baseheld,independent=end,
             scope='The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('END_TRUE_FULL_HALF',end,flush=True)
if __name__=='__main__':main()
