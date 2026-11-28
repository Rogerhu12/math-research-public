#!/usr/bin/env python3
"""Continue the physical full half using true second fundamental form inequalities on the frozen metric."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
from types import SimpleNamespace
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):os.environ[key]='1'
import numpy as np


def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('field-source','wall-source','scripts','work','physical-source','cut','comparison','refinement-source','adjacent-source','angular-source','direct-source','parent','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--heat-source',type=Path);p.add_argument('--seed',type=Path);p.add_argument('--split',action='store_true')
    p.add_argument('--tail-spans',type=int,default=12);p.add_argument('--modes',type=int,default=36);p.add_argument('--steps',type=int,default=5)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    original=module(a.field_source,'published_clamped_whole_field')
    walls=module(a.wall_source,'physical_curvature_inequalities')
    if sha(a.field_source)!='86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841':raise ValueError('Different exact full-half field definition')
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
        kn=original.original_knots(oldkn,a.full_sleeve,src.S,src.T,a.tail_spans)
        seed=np.zeros((len(kn)-12,3*a.modes+2))
    else:
        with np.load(a.seed,allow_pickle=False) as s:
            if str(s['parentSHA'])!=sha(a.parent) or str(s['sourceSHA']) not in (sha(a.field_source),sha(__file__)) or str(s['fieldSHA'])!=src.source_sha:raise ValueError('Different full-half family')
            kn,seed=direct.transfer(s['unitKnots'].copy(),s['wholeTailXYZ'].copy(),a.modes,a.split)
    phys_kn=a.full_sleeve+(src.T-a.full_sleeve)*kn
    breaks=np.unique(np.r_[a.full_sleeve,oldkn,phys_kn[(phys_kn>a.full_sleeve+1e-13)&(phys_kn<src.S-1e-13)],src.S])
    sampling_knots=np.r_[np.full(5,a.full_sleeve),breaks,np.full(5,src.S)]
    def model(role,nr,n,nt,shift):
        th,ang=adj.node_angles(src,phys,geo,a,n,nt,shift);half=np.pi/3
        th=np.sort(np.r_[0.,th[(th>1e-11)&(th<half-1e-11)],half]);th=th[np.r_[True,np.diff(th)>1e-11]]
        ss=adj.SourceAt(src,th);mm=adj.AtAngles(micro,th)
        q0,J0,r0,Q0,W0=original.parent_prefix(src,ss,mm,ref,api,geo,phys,adj,a,th,oldkn,sampling_knots,old,extra,metric,nr,shift,heatdata,heat)
        zs=original.actual_tail_nodes(src,record,role);J1,r1,H,Hq,r,other,otherRadius=original.tail_data(src,ss,zs)
        delta=np.max(np.linalg.norm(J0[-1]-other,axis=-1),axis=-1)
        q=np.r_[q0,zs*src.T];allH=np.r_[np.ones(len(q0)),H];allHq=np.r_[np.zeros(len(q0)),Hq]
        B=original.field_basis(api,kn,q,allH,allHq,a.full_sleeve,src.T)
        G=ar.Model.__new__(ar.Model);G.G=SimpleNamespace(t=q/src.S,u=th,source=ss);G.micro=micro
        G.B=B;G.ch=ar.channels(a.modes);G.phi=np.zeros((3,3,len(G.ch),len(th)));direct.native_basis(G,th)
        G.shape=(len(kn)-12,len(G.ch));G.nvar=int(np.prod(G.shape));G.orders=src.base.O;G.base=np.concatenate((J0,J1))
        G.rho=np.concatenate((r0,r1));G.Q=np.r_[Q0,np.ones(len(zs))][:,None];G.W=np.r_[W0,np.ones(len(zs))][:,None]
        G.u=src.center.arc(th)
        for j,(i,d) in enumerate(G.orders):G.base[:,j]+=mm.fft_forward(B[i]@seed,a.modes,len(th),th[0],d)
        seamB=np.asarray([v[-1] for v in original.field_basis(api,kn,np.array([src.S]),np.ones(1),np.zeros(1),a.full_sleeve,src.T)])
        return G,len(q0),dict(angular=ang,actualAngles=len(th),prefixRows=len(q0),exactTailRadiusQueries=len(zs),originalGauss=int(record['gauss']),
                     tailSplit=['all original training rule','even local indices in original higher rule','odd local indices in original higher rule'][role],trueCuff=float(src.chart.cuff),
                     minimumTailH=float(H.min()),maximumTailH=float(H.max()),minimumTailRadius=float(r.min()),maximumTailRadius=float(r.max()),
                     baseSixJetTraceDifference=delta.tolist(),baseAngularRadiusTraceDifference=float(np.max(abs(r0[-1]-otherRadius))),
                     commonCutTraceMapRank=int(np.linalg.matrix_rank(seamB)),positiveInteriorSupportColumns=int(np.sum(abs(seamB[0])>1e-14)))
    G,ix,ga=model(0,123,401,17,False);T,jx,ta=model(1,183,607,29,True)
    X=np.zeros(G.shape);initial=original.record_geometry(G,X,src,ix);second=original.record_geometry(T,X,src,jx)
    hist=[];logs=[]
    for step in range(a.steps):
        best,log=walls.same_metric_step(G,T,X,direct,a.curvature_guide)
        logs.append(log)
        if best is None:break
        score,X,record=best
        record.update(step=step+1,training=original.record_geometry(G,X,src,ix),secondary=original.record_geometry(T,X,src,jx))
        hist.append(record);print('ACCEPT_PHYSICAL_CURVATURE_WALL',record,flush=True)
    total=seed.copy();m=a.modes
    for j,(tag,k) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+k]+=X[:,j]
        else:total[:,abs(k)]+=X[:,j];total[:,m+abs(k)]+=np.sign(k)*X[:,j]
    del G,T
    U,kx,ua=model(2,233,1109,57,False);baseheld=original.record_geometry(U,0*X,src,kx);end=original.record_geometry(U,X,src,kx)
    Bc=original.field_basis(api,kn,np.array([src.S]),np.ones(1),np.zeros(1),a.full_sleeve,src.T)
    seam=[float(np.max(np.abs(b@total))) for b in Bc]
    ends=original.field_basis(api,kn,np.array([a.full_sleeve,src.T]),np.ones(2),np.zeros(2),a.full_sleeve,src.T)
    sf=a.out.with_suffix('.npz')
    with sf.open('xb') as f:np.savez_compressed(f,sourceSHA=sha(a.field_source),solverSHA=sha(__file__),wallSHA=sha(a.wall_source),parentSHA=sha(a.parent),fieldSHA=src.source_sha,unitKnots=kn,wholeTailXYZ=total,modes=a.modes,c=a.full_sleeve,actualCommonCut=src.S,actualCuffCoordinate=src.T)
    out=dict(schema='actual-full-half-same-metric-curvature-constrained-GN-v1',sourceSHA=sha(a.field_source),solverSHA=sha(__file__),wallSHA=sha(a.wall_source),parentSHA=sha(a.parent),fieldSHA=src.source_sha,stateSHA=sha(sf),
             exactTailQueryReportSHA=sha(a.query_report),exactTailQueryCacheSHA=sha(a.query_cache),seedSHA=sha(a.seed) if a.seed else None,radialUnitSpans=len(np.unique(kn))-1,positionVariables=int(X.size),metricVariables=0,
             physicalCommonCut=src.S,physicalCuffCoordinate=src.T,grids=[ga,ta,ua],actualMeanAndFullFrequencyCommonCutCoefficientTraceMax=seam,actualTwoEndpointBasisZeroJets=[float(np.max(abs(b))) for b in ends],
             initial=initial,initialSecondary=second,accepted=hist,directionProjections=logs,initialIndependent=baseheld,independent=end,
             scope='The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds.')
    out['independent']['maximumNorm']=float(np.max(np.linalg.norm(U.base[:,0]+U.forward_field(X,0,0),axis=-1)))
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('END_TRUE_FULL_HALF',end,flush=True)
if __name__=='__main__':main()
