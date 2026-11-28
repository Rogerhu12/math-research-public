#!/usr/bin/env python3
"""Full fixed-metric Newton step on the actual adjacent-port cut using true normal-angle-targeted nodes and physical inlet profiles."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def node_angles(src,phys,geo,a,grid,transition,shift):
    fraction=(np.arange(transition)+(.671 if shift else .229))/transition
    vs=phys.V0+(phys.V1-phys.V0)*np.r_[0.,fraction,1.]
    us=geo.integ(vs)[:,0]
    raw=np.concatenate([(j*phys.PERIOD+sign*us-a.anchor)%(2*np.pi) for j in range(3) for sign in (-1.,1.)])
    theta=raw.copy();lo=np.zeros_like(raw);hi=np.full_like(raw,2*np.pi)
    for _ in range(48):
        delta=src.center.arc(theta)-raw
        done=abs(delta)<8e-15
        if np.all(done):break
        speed=np.linalg.norm(src.center.base.derivative(theta,1),axis=-1)
        lo=np.where(delta<0,theta,lo);hi=np.where(delta>0,theta,hi)
        n=theta-delta/speed
        theta=np.where(done,theta,np.where((n>lo)&(n<hi),n,(lo+hi)/2))
    err=float(np.max(abs(src.center.arc(theta)-raw)))
    if err>1e-13:raise ArithmeticError('Original arclength inverse missed true transition nodes')
    uniform=(np.arange(grid)+(.5 if shift else 0.))*2*np.pi/grid
    return np.unique(np.r_[uniform,theta]),dict(fullUniform=grid,additionalMaterialTargets=len(raw),perTransitionInterior=transition,originalMaterialInverseError=err)

class SourceAt:
    """Original X+C+W at an explicit native-angle vector, including all original material derivatives."""
    def __init__(self,source,theta):
        self.source=source;self.center=source.center;self.base=source.base;self.S=source.S;self.T=source.T
        self.theta=theta;self.source_sha=source.source_sha
        central=self.center.raw
        v=central.derivative(theta,1);a=central.derivative(theta,2)
        s=np.linalg.norm(v,axis=-1);u=self.center.arc(theta)
        r=s/central.a;r1=np.sum(v*a,axis=-1)/(s*central.a)
        j=source.joint
        old=j.traces.old_port_traces(source.pos.src,j.LD(0),u,r,r1,source.pos.src.metric.lam)
        target=np.zeros_like(old)
        for order in range(3):target[0,order]=self.center.base.derivative(theta,order)
        target[1,0,:,2]=1
        self.chart={len(theta):(u,r,r1,target-old)}
        self.ep=np.exp(1j*source.pm[:,None]*theta);self.eh=np.exp(1j*source.hm[:,None]*theta)
    def prefix(self,t,n,shift):
        S=self.source
        if n!=len(self.theta):raise ValueError('Wrong actual angle axis')
        w=[];r=[]
        for b in range(0,len(t),16):
            v,r0=S.joint.background(S.pos.src,self.center.raw,t[b:b+16],n,self.chart)
            w.append(np.asarray(v,float));r.append(np.asarray(r0,float))
        J=np.concatenate(w);rho=np.concatenate(r)
        z=t*S.S/S.T;scale,scaleq=S.chart.scales(z)
        co=[S.spline(z,i) for i in range(3)]
        co[2]=co[2]/(S.T*scale[:,None])**2-co[1]*scaleq[:,None]/(S.T*scale[:,None]**3)
        co[1]/=S.T*scale[:,None]
        for j,(r,d) in enumerate(self.base.O):
            p=(co[r][:,:len(S.pm)]*(1j*S.pm)**d)@self.ep
            h=(co[r][:,len(S.pm):]*(1j*S.hm)**d)@self.eh
            J[:,j]+=np.stack((p.real,p.imag,h.real),axis=-1)
        return self.theta,J,rho

class AtAngles:
    def __init__(self,micro,theta):
        self.micro=micro;self.theta=theta;self.tables={}
    def __getattr__(self,name):return getattr(self.micro,name)
    def fft_forward(self,coeff,m,n,offset,d):
        if n!=len(self.theta):raise ValueError('Wrong spectral angle axis')
        if (m,d) not in self.tables:
            k=np.arange(m+1)
            self.tables[m,d]=((1j*k[:,None])**d)*np.exp(1j*k[:,None]*self.theta)
        f=self.tables[m,d]
        return np.stack((coeff[:,:m+1]@f.real,coeff[:,m+1:2*m+1]@f[1:].imag,coeff[:,2*m+1:]@f.real),axis=-1)

def angles_profile(phys,api,src,geo,a,nu,shift):
    c=a.full_sleeve;th,j,rr=src.prefix(np.array([c/src.S]),nu,shift)
    orig,diff,sp=api.central_delta(src,geo,None,th,1.,a.anchor)
    spp=np.sum(orig[1]*orig[2],axis=-1)/sp;u=src.center.arc(th)
    _,beta,k=geo.at(u,a.anchor);sector=np.floor((u+a.anchor+phys.HALF)/phys.PERIOD)
    rel=beta-(sector*phys.PERIOD-a.anchor);v=abs(rel)
    gap=phys.V1-phys.V0;x=np.clip((v-phys.V0)/gap,0.,1.)
    w=phys.sw(x);wp=30*x**2*(1-x)**2/gap;wpp=60*x*(1-x)*(1-2*x)/gap**2
    co=np.cos(v[:,None]*phys.F);si=np.sin(v[:,None]*phys.F)
    spectrum=geo.weights[1:]
    b=geo.weights[0]+co@spectrum
    bp=-si@(spectrum*phys.F)
    bpp=-co@(spectrum*phys.F**2)
    rad=(1-w)/phys.LOW+w*b
    rp=wp*(b-1/phys.LOW)+w*bp
    rpp=wpp*(b-1/phys.LOW)+2*wp*bp+w*bpp
    if np.max(abs(rad*k-1))>1e-12:raise ArithmeticError('Inlet differential and normalized physical section differ')
    k1=-np.sign(rel)*rp/rad**3;k2=3*rp**2/rad**5-rpp/rad**4
    N=np.exp(1j*beta);T=1j*N;Vu=T-k1*N/k**2
    Vuu=-(k1/k)*T+(-k-k2/k**2+2*k1**2/k**3)*N
    nk=np.stack([api.xyz(N/k),api.xyz(Vu*sp),api.xyz(Vuu*sp**2+Vu*spp)])
    hz=np.zeros_like(nk);hz[0,:,2]=1/k**2
    grow=-2*k1/k**3;hz[1,:,2]=grow*sp;hz[2,:,2]=(-2*k2/k**3+6*k1**2/k**4)*sp**2+grow*spp
    cyl=orig+diff;cyl[0,:,2]+=c
    D=j[0,[0,2,5]]+(1-api.smooth(c/a.lift_end))*diff-cyl
    fac=rr[0]/sp
    return np.stack((nk,D,hz),axis=2).transpose(0,3,2,1),dict(f=float(fac[0]),angularRange=float(np.ptp(fac)),maxAbsD2Nk=float(np.max(abs(Vuu))),minK=float(k.min()),maxK=float(k.max()))

def main():
    p=argparse.ArgumentParser()
    for key in ('scripts','work','physical-source','cut','comparison','refinement-source','angular-source','direct-source','profile-source','parent','out'):
        p.add_argument('--'+key,required=True,type=Path)
    p.add_argument('--split',action='store_true')
    for key,default in (('modes',0),('radial',113),('test-radial',171),('angles',216),('test-angles',321),('guard-angles',579),('holdout-angles',867),('steps',4)):
        p.add_argument('--'+key,type=int,default=default)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    phys=module(a.physical_source,'r317_adjacent_physical_definition');api=module(a.cut,'r317_raw_cut')
    if sha(a.physical_source)!='29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902':
        raise ValueError('This solver requires the R317 normalized adjacent low-curvature curve')
    api.true_arc_position=phys.true_arc_position
    geo=phys.NormalCurve()
    ref=module(a.refinement_source,'r317_dense_span_geometry');ar=module(a.angular_source,'r317_position_model')
    direct=module(a.direct_source,'r317_banded_normal');core=module(a.profile_source,'r317_inlet_common')
    core.profiles=lambda api,s,g,aa,n,sh:angles_profile(phys,api,s,g,aa,n,sh)
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','r317_old_true_cut_background')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z or str(z['cutSHA'])!=sha(a.cut) or a.low!=phys.LOW:
            raise ValueError('Parent is a different physical cut')
        if 'inletProfileSourceSHA' in z and str(z['inletProfileSourceSHA'])!=sha(__file__):raise ValueError('Different angular profile source')
        oldX=z['inletNativeXYZ'].copy() if 'physicalInletProfiles' in z else z['actualPhysicalXYZ'].copy()
        extra0=z['physicalInletProfiles'].copy() if 'physicalInletProfiles' in z else np.zeros((len(oldX),3))
        oldkn=z['knots'].copy();m0=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
        frozen={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','cutSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor','metricQ','metricW')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles):raise ValueError('Uniform angles must resolve native modes')
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    src=micro.Source(a)
    if (src.S,src.T)!=(a.S,a.T):raise ValueError('Different original common source')
    # Exact arbitrary-angle evaluator checked on ordinary independent nodes.
    nn=57;t=np.array([0.,a.full_sleeve,a.full_sleeve+a.full_gate,a.lift_end,src.S])/src.S
    th,j0,r0=src.prefix(t,nn,True)
    sa=SourceAt(src,th);_,j1,r1=sa.prefix(t,nn,True)
    oldAgreement=[float(np.max(abs(j1-j0))),float(np.max(abs(r1-r0)))]
    if max(oldAgreement)>2e-9:raise ArithmeticError('Actual old field at explicit angles differs '+str(oldAgreement))
    def axis(n,nt,sh):
        th,info=node_angles(src,phys,geo,a,n,nt,sh)
        return AtAngles(micro,th),SourceAt(src,th),info
    extra=core.prolong_extra(oldkn,extra0,a.split)
    def model(nr,n,nt,sh):
        mm,ss,inf=axis(n,nt,sh)
        G,fi=core.joint_model(ref,api,mm,ss,geo,ar,direct,a,kn,oldkn,oldX,metric,nr,len(ss.theta),sh,extra0)
        return G,fi,inf
    G,fi,ni=model(a.radial,a.angles,13,False);Q,qi,nj=model(a.test_radial,a.test_angles,21,True)
    X=np.zeros(G.shape)
    mg,sg,ng=axis(a.guard_angles,33,True)
    Ag=core.Audit(api,mg,sg,geo,a,kn,metric,len(sg.theta),(.11,.54,.89),True)
    nc=lambda x:core.merged_native(G,seed,x,a.modes)
    ex=lambda x:extra+x[:,-3:]
    guard=lambda x:Ag.report(nc(x),ex(x))
    base=G.report(X);test0=Q.report(X);guard0=guard(X);currguard=guard0
    trial,info=core.leading(api,geo,a,G,fi,kn,metric,seed,extra)
    rawlead=dict(training=G.report(trial),secondary=Q.report(trial),angularGuard=guard(trial))
    history=[];log=[];check=None
    def choose(dx,before,second,initialGuard):
        peak=max(before['peak'],second['peak'],initialGuard['peak'])
        cand=[]
        for t in np.r_[1.,2.**(-np.arange(1,23)/2)]:
            Z=X+t*dx
            e=G.metrics(Z)[3];v=Q.metrics(Z)[3]
            val=max(float(e.max()),float(v.max()))
            if val<peak and val<max(before['peak'],second['peak'])*(1-1e-11):
                cand.append((val,float(t)))
        for _,t in sorted(cand):
            Z=X+t*dx;r=G.report(Z);s=Q.report(Z)
            def good(y,b):
                return y['curvature']<=max(a.curvature_guide,b['curvature']+1e-6) and y['minimumSupport']>=min(.115,b['minimumSupport'])
            if not good(r,before) or not good(s,second):continue
            z=guard(Z)
            if max(r['peak'],s['peak'],z['peak'])>=peak*(1-1e-11) or not good(z,initialGuard):continue
            return (max(r['peak'],s['peak'],z['peak']),Z,r,s,z,t)
        return None
    leadingStep=choose(trial,base,test0,currguard)
    if leadingStep is not None:
        _,X,r,s,currguard,t=leadingStep
        history.append(dict(kind='physical cubic inlet direction',alpha=t,training=r,secondary=s,angularGuard=currguard))
    for it in range(a.steps):
        before=G.report(X);second=Q.report(X);best=None
        for power in ((.65,1.5) if it<2 else (1.1,2.2)):
            ab,grad=direct.assemble(G,X,power)
            if check is None:check=direct.check_normal(G,X,power,ab,grad)
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));N=len(sc)
            for k in range(min(len(ab),N)):ab[k,:N-k]*=sc[k:]*sc[:N-k]
            diag=ab[0].copy()
            for mu in (1e-10,1e-7,1e-4,.003):
                ab[0]=diag+mu
                try:dx=(sc*solveh_banded(ab,-sc*grad,lower=True,check_finite=False)).reshape(X.shape)
                except LinAlgError:continue
                v=choose(dx,before,second,currguard)
                if v is not None and (best is None or v[0]<best[0]):
                    best=(*v,power,mu)
            if best is not None:break
        log.append(dict(step=it+1,accepted=best is not None))
        if best is None:break
        _,X,r,s,currguard,t,power,mu=best
        history.append(dict(kind='full physical banded update',step=it+1,alpha=t,damping=mu,weight=power,training=r,secondary=s,angularGuard=currguard))
        print('ACCEPT_INLET',it+1,r,s,currguard,flush=True)
    total=nc(X);extra=ex(X)
    del Ag,G,Q
    mf,sf,nf=axis(a.holdout_angles,47,False)
    hold=core.Audit(api,mf,sf,geo,a,kn,metric,len(sf.theta),(.149,.433,.817),False)
    initialHeld=hold.report(seed,core.prolong_extra(oldkn,extra0,a.split));end=hold.report(total,extra)
    state=a.out.with_suffix('.npz')
    with state.open('xb') as w:
        np.savez_compressed(w,**frozen,inletNativeXYZ=total,physicalInletProfiles=extra,inletProfileSourceSHA=sha(__file__),metricKnots=mk,knots=kn,modes=a.modes,spans=a.spans)
    out=dict(schema='R321-two-moment-W040-full-normal-angle-targets-physical-profile-Newton-v1',entrySHA256=sha(__file__),stateSHA256=sha(state),parentSHA256=sha(a.parent),fieldSHA256=src.source_sha,
             R317PreservedRadiusSourceSHA=geo.reference_sha,twoMomentCoefficients=geo.adjustments.tolist(),physicalSourceSHA256=sha(a.physical_source),cutSHA256=sha(a.cut),denseSpanSourceSHA256=sha(a.refinement_source),profileSourceSHA256=sha(a.profile_source),directSourceSHA256=sha(a.direct_source),
             metricVariables=0,actualPositionVariables=int(X.size),additionalPhysicalVariables=3*len(extra),exactProfile=info,coordinateEvaluatorsAgreement=oldAgreement,
             trueTransitionAngleGrids=[ni,nj,ng,nf],angularPhysicalProfiles=[fi,qi],unscaledExactCubicStep=rawlead,initial=base,initialSecondary=test0,initialGuard=guard0,
             accepted=history,attempts=log,normalAndRhsAgreement=check,finalAngularGuard=currguard,initialIndependent=initialHeld,independent=end,
             scope='Finite all-span and true normal-angle targeted evidence. Both endpoints and disjoint internal samples enter all six 0.040 normal-angle transitions using the actual material inverse and arbitrary native-angle source. The full nonuniform Gram and curvature are tested at every such angular column.')
    with a.out.open('x') as out_file:json.dump(out,out_file,indent=2);out_file.write('\n')
    print('END_ADJACENT_CAUCHY',end,flush=True)
if __name__=='__main__':main()
