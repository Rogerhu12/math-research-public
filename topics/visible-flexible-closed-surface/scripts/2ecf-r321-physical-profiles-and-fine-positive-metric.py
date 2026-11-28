#!/usr/bin/env python3
"""Design a fine positive radial metric and all native position variables on the actual W040 two-moment outer half."""
import argparse,hashlib,importlib.util,json,os,sys,time
from fractions import Fraction as F
from pathlib import Path
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solveh_banded,LinAlgError
from scipy.interpolate import BSpline

def mod(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(z):return F.from_float(float(z))

def main():
    p=argparse.ArgumentParser()
    for key in ('design-source','cut','adjacent-source','scripts','work','physical-source','refinement-source','angular-source','direct-source','comparison','parent','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--split',action='store_true')
    for key,d in (('modes',0),('angles',481),('test-angles',691),('radial',123),('test-radial',173),('holdout-angles',1111),('holdout-radial',233),('steps',6)):
        p.add_argument('--'+key,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69);a=p.parse_args()
    ref=mod(a.refinement_source,'design_cut_dense');ar=mod(a.angular_source,'design_spatial_operator')
    direct=mod(a.direct_source,'design_complete_band');api=mod(a.cut,'design_actual_blend')
    phys=mod(a.physical_source,'actual_w040_two_moment_curve')
    adj=mod(a.adjacent_source,'actual_nonuniform_native_angles')
    prior=mod(a.design_source,'fine_positive_boehm_and_physical_normals')
    if sha(a.physical_source)!='29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902':raise ValueError('Require the W040 two-moment curve')
    api.true_arc_position=phys.true_arc_position;geo=phys.NormalCurve()
    micro=mod(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','design_R262')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z or str(z['cutSHA'])!=sha(a.cut) or a.low!=phys.LOW:raise ValueError('Physical cut or port differs')
        if 'physicalInletProfiles' not in z or str(z['inletProfileSourceSHA'])!=sha(a.adjacent_source):
            raise ValueError('Require the actual W040 physical-profile parent')
        oldX=z['inletNativeXYZ'].copy();oldkn=z['knots'].copy();oldProfiles=z['physicalInletProfiles'].copy()
        if oldProfiles.shape!=(len(oldX),3):raise ValueError('Wrong three physical inlet profiles')
        mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        aq=z['metricQ'].copy();aw=z['metricW'].copy()
        root={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','cutSHA','S','T','fullSleeve','fullGate','liftEnd','lam','low','anchor')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles,a.holdout_angles):raise ValueError('Native modes reach Nyquist')
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    extraSpline=BSpline(oldkn,np.pad(oldProfiles,((3,3),(0,0))),5)
    for v in np.setdiff1d(np.unique(kn),np.unique(oldkn)):extraSpline=extraSpline.insert_knot(v)
    seedProfiles=extraSpline.c[3:-3]
    if not np.array_equal(extraSpline.t,kn):raise ValueError('Physical profile refinement differs')
    mc=prior.exact_metric_transfer(mk,aq,aw,kn);mf=np.array([[float(t) for t in row] for row in mc]);metric=dict(knots=mk.tolist(),q=aq.tolist(),w=aw.tolist())
    src=micro.Source(a)
    if (src.S,src.T)!=(a.S,a.T):raise ValueError('Different original physical section')
    def model(nr,nu,points,shift,which_metric):
        th,info=adj.node_angles(src,phys,geo,a,nu,points,shift)
        half=np.pi/3
        th=np.sort(np.r_[0.,th[(th>1e-11)&(th<half-1e-11)],half])
        th=th[np.r_[True,np.diff(th)>1e-11]]
        mm,ss=adj.AtAngles(micro,th),adj.SourceAt(src,th)
        m=a.modes;a.modes=0
        try:G=ar.Model(ref,api,mm,ss,geo,a,kn,oldkn,oldX,which_metric,nr,len(th),shift)
        finally:a.modes=m
        direct.native_basis(G,th)
        phi,profile_info=adj.angles_profile(phys,api,ss,geo,a,len(th),shift)
        basis=api.Bvals(G.G.t*src.S,oldkn)
        for i,(r,d) in enumerate(G.orders):
            C=basis[r]@oldProfiles
            for axis in range(3):G.base[:,i,:,axis]+=C@phi[d,axis]
        G.phi=np.concatenate((G.phi,phi),axis=2);G.ch=G.ch+[('special',i) for i in range(3)]
        G.shape=(G.B[0].shape[1],len(G.ch));G.nvar=int(np.prod(G.shape))
        info['maximumProfileSecondDerivative']=profile_info['maxAbsD2Nk']
        G.Q0=G.Q.copy();G.W0=G.W.copy()
        info.update(actualAngles=len(th),radialRows=len(G.G.t))
        return G,info
    G,ga=model(a.radial,a.angles,17,False,metric);T,ta=model(a.test_radial,a.test_angles,29,True,metric)
    Y=np.zeros((G.shape[0],G.shape[1]+2));init=prior.report(G,Y);ind=prior.report(T,Y);ind0=ind
    hist=[];checks=None;times=[]
    for it in range(a.steps):
        start=time.monotonic();power=.6 if it<2 else 1.1;pwr=6 if it<3 else 10
        before=prior.report(G,Y);_,_,_,e=G.metrics(Y[:,:-2]);v0=float(np.mean(e**pwr)**(1/pwr))
        pk0=max(before['peak'],ind['peak']);best=None
        for pow0 in (power,2.0):
            ab,g,chk=prior.joint_system(G,Y,pow0,checks is None,direct)
            if chk is not None:checks=chk
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));N=len(sc)
            for d in range(min(len(ab),N)):ab[d,:N-d]*=sc[d:]*sc[:N-d]
            diag=ab[0].copy()
            for mu in (1e-12,1e-9,1e-6,1e-4,.003):
                ab[0]=diag+mu
                try:dy=(sc*solveh_banded(ab,-sc*g,lower=True,check_finite=False)).reshape(Y.shape)
                except LinAlgError:continue
                lg=prior.line(G,Y,dy);lt=prior.line(T,Y,dy);proposals=[]
                for alpha in 2.**(-np.arange(0,23)/2):
                    cand=Y+alpha*dy
                    if min((1+mf+cand[:,-2:]).min(),1.)<=0:continue
                    val,pk=lg(alpha,pwr)
                    if val>=v0 or pk>=pk0:continue
                    _,ph=lt(alpha,pwr);pnew=max(pk,ph)
                    if pnew<pk0:proposals.append((val/v0+.40*pnew/pk0,float(alpha)))
                for score,alpha in sorted(proposals):
                    if best is not None and score>=best[0]:break
                    cand=Y+alpha*dy;rr=prior.report(G,cand);qq=prior.report(T,cand)
                    if rr['curvature']>max(a.curvature_guide,before['curvature']+1e-5) or qq['curvature']>max(a.curvature_guide,ind['curvature']+1e-5):continue
                    if min(rr['minimumSupport'],qq['minimumSupport'])<.115:continue
                    normmax=max(float(np.max(np.linalg.norm(g.base[:,0]+g.forward_field(cand[:,:-2],0,0),axis=-1))) for g in (G,T))
                    if normmax>1.915:continue
                    best=(score,cand,rr,qq,alpha,mu,pow0);break
            if best is not None:break
        times.append(time.monotonic()-start)
        if best is None:break
        _,Y,rr,ind,alpha,mu,pow0=best
        hist.append(dict(step=it+1,stepLength=alpha,diagonalDamping=mu,weightPower=pow0,actualTraining=rr,actualSecondary=ind));print('JOINT_ACTUAL',it+1,rr,ind,flush=True)
    # The optimization used the unchanged old spline plus fine increments.
    # Select one final dyadic fine metric and re-evaluate that field from zero.
    exact=[(r[0]+fq(a0),r[1]+fq(a1)) for r,(a0,a1) in zip(mc,Y[:,-2:])]
    choose=np.array([[float(t) for t in row] for row in exact])
    rounderr=max(abs(fq(v)-t) for row,ex in zip(choose,exact) for v,t in zip(row,ex))
    if min(1+fq(v) for v in choose.flat)<=0:raise ValueError('Final fine metric not positive in coefficient hull')
    newmetric=dict(knots=kn.tolist(),q=choose[:,0].tolist(),w=choose[:,1].tolist());m=a.modes;total=seed.copy()
    totalProfiles=seedProfiles+Y[:,-5:-2]
    for j,(tag,mode) in enumerate(G.ch[:-3]):
        if tag=='height':total[:,2*m+1+mode]+=Y[:,j]
        else:total[:,abs(mode)]+=Y[:,j];total[:,m+abs(mode)]+=np.sign(mode)*Y[:,j]
    outputKn=kn
    if not hist:
        newmetric=metric;outputKn=mk;choose=np.column_stack((aq,aw));rounderr=F(0)
    del G,T
    U,ua=model(a.holdout_radial,a.holdout_angles,53,False,metric)
    initialFresh=U.report(np.zeros(U.shape))
    delta=Y[:,:-2]
    # U.base contains exactly the parent position. Evaluate the frozen dyadic target at the very same sites.
    U.Q=(1+api.Bvals(U.G.t*src.S,outputKn)[0]@choose[:,0])[:,None]
    U.W=(1+api.Bvals(U.G.t*src.S,outputKn)[0]@choose[:,1])[:,None]
    fixed=U.report(delta)
    fixed['maximumOriginNorm']=float(np.max(np.linalg.norm(U.base[:,0]+U.forward_field(delta,0,0),axis=-1)))
    _,_,components,error=U.metrics(delta)
    worst=np.unravel_index(np.argmax(error),error.shape)
    fixed['relativeE_F_GatPeak']=[float(components[0][worst]),float(components[1][worst]/np.sqrt(2)),float(components[2][worst])]
    state=a.out.with_suffix('.npz')
    with state.open('xb') as h:
        np.savez_compressed(h,**root,inletNativeXYZ=total,physicalInletProfiles=totalProfiles,inletProfileSourceSHA=sha(a.adjacent_source),knots=kn,metricKnots=outputKn,metricQ=choose[:,0],metricW=choose[:,1],
                            modes=m,spans=a.spans,metricDesignEntrySHA=sha(__file__),metricDesignParentSHA=sha(a.parent))
    metric_key=hashlib.sha256(np.asarray(outputKn,dtype='<f8').tobytes()+np.asarray(choose[:,0],dtype='<f8').tobytes()+np.asarray(choose[:,1],dtype='<f8').tobytes()).hexdigest()
    out=dict(schema='R321-W040-three-physical-profiles-and-fine-positive-metric-v1',entrySHA256=sha(__file__),fieldSHA256=src.source_sha,
        parentSHA256=sha(a.parent),stateSHA256=sha(state),chosenMetricSHA256=metric_key,
        physicalCurveSHA=sha(a.physical_source),cutSHA=sha(a.cut),angularTargetSHA=sha(a.adjacent_source),parentFineDesignSHA=sha(a.design_source),
        trueGrids=[ga,ta,ua],actualPositionVariables=int(delta.size),newMetricVariables=2*len(mc),parentMetricCoefficients=2*len(aq),
        exactBoehmInitialContainsOriginalMetric=True,finalMetricRoundingBoundExact=str(rounderr),positiveMetricControlMinimum=float(min(1.,(1+choose).min())),
        initial=init,initialSecondary=ind0,initialIndependent=initialFresh,accepted=hist,completeDifferentialAgreement=checks,secondsPerStep=times,
        finalFrozenCandidate=fixed,scope='The exact radial Boehm lift represents the parent metric identically. Joint steps are a new metric design. The saved final dyadic functions define the metric for subsequent frozen spatial refinement; the cuff, true tail parent, and central rigid windows keep the same physical source.')
    with a.out.open('x') as h:json.dump(out,h,indent=2);h.write('\n')
    print('FROZEN_ACTUAL_W040_METRIC',metric_key,fixed,flush=True)
if __name__=='__main__':main()
