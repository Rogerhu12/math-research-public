#!/usr/bin/env python3
"""Physical Cauchy inlet profiles for the full three-arc cut; fixed radial metric, all original XYZ modes."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def profiles(api,src,geo,a,nu,shift):
    c=a.full_sleeve
    theta,old,rr=src.prefix(np.array([c/src.S]),nu,shift)
    orig,diff,sp=api.central_delta(src,geo,None,theta,1.,a.anchor)
    u=src.center.arc(theta)
    speed1=np.sum(orig[1]*orig[2],axis=-1)/sp
    beta,k=geo.target_angle(u,a.anchor)
    n=np.exp(1j*beta);t=1j*n
    v=(u+a.anchor+geo.P/2)%geo.P-geo.P/2
    x=np.clip((abs(v)-geo.L0/2)/geo.TAU,0.,1.)
    dk=geo.HIGH-geo.LOW
    k1=dk/geo.TAU*51480*x**7*(1-x)**7*np.sign(v)
    k2=dk/geo.TAU**2*(7*51480)*x**6*(1-x)**6*(1-2*x)
    v0=n/k
    vu=t-k1*n/k**2
    vuu=-(k1/k)*t+(-k-k2/k**2+2*k1**2/k**3)*n
    nk=np.stack([api.xyz(v0),api.xyz(vu*sp),api.xyz(vuu*sp**2+vu*speed1)])
    h=1-api.smooth(c/a.lift_end)
    cyl=orig+diff;cyl[0,:,2]+=c
    interface=old[0,[0,2,5]]+h*diff-cyl
    normal_height=np.zeros_like(nk)
    normal_height[0,:,2]=1/k**2
    du=-2*k1/k**3
    normal_height[1,:,2]=du*sp
    normal_height[2,:,2]=(-2*k2/k**3+6*k1**2/k**4)*sp**2+du*speed1
    phi=np.stack([nk,interface,normal_height],axis=2).transpose(0,3,2,1)
    fr=rr[0]/sp
    return phi,dict(f=float(fr[0]),angularRange=float(np.ptp(fr)),kMin=float(k.min()),kMax=float(k.max()))

def joint_model(ref,api,micro,src,geo,ar,direct,a,kn,parentKn,parentXYZ,metric,nr,nu,shift,extra_parent):
    G=ar.Model(ref,api,micro,src,geo,a,kn,parentKn,parentXYZ,metric,nr,nu,shift)
    direct.native_basis(G,G.G.u)
    phi,info=profiles(api,src,geo,a,nu,shift)
    G.phi=np.concatenate((G.phi,phi),axis=2)
    G.ch=G.ch+[('special',0),('special',1),('special',2)]
    G.shape=(G.B[0].shape[1],len(G.ch));G.nvar=int(np.prod(G.shape))
    if extra_parent is not None:
        for i,(r,d) in enumerate(src.base.O):
            C=api.Bvals(G.G.t*src.S,parentKn)[r]@extra_parent
            for j in range(3):G.base[:,i,:,j]+=C@phi[d,j]
    return G,info

def prolong_extra(oldkn,extra,split):
    if not split:return extra.copy()
    s=BSpline(oldkn,np.pad(extra,((3,3),(0,0))),5,axis=0)
    cells=np.unique(oldkn)
    for v in cells[:-1]+np.diff(cells)/2:s=s.insert_knot(v)
    return s.c[3:-3]

def leading(api,geo,a,G,fi,kn,metric,native,extra):
    # B'''_0(c+)/6 is the first interior quintic coefficient's ordinary cubic multiplier.
    c=a.full_sleeve
    mkn=np.asarray(metric['knots'])
    w=BSpline(mkn,np.pad(np.asarray(metric['w']),(3,3)),5)
    q=BSpline(mkn,np.pad(np.asarray(metric['q']),(3,3)),5)
    bs=BSpline(kn,np.eye(len(kn)-6)[:,3:-3],5)
    first=bs(c,3)/6
    if np.count_nonzero(first)!=1 or first[0]<=0:raise ArithmeticError('Unexpected clamped inlet third jet')
    gate=10/a.full_gate**3
    g3=2*gate*(fi['f']-1)+w(c,3)/6
    m=a.modes
    want=np.zeros(G.shape)
    for j,(tag,mode) in enumerate(G.ch[:-3]):
        want[0,j]=-native[0,2*m+1+mode] if tag=='height' else -native[0,abs(mode)]
    want[0,-3:]=np.array([g3/2,-gate,0.])/first[0]-extra[0]
    return want,dict(g3=float(g3),e3=float(q(c,3)/6),clampedCubicCoefficient=float(first[0]),oldMetricRadiusAngleSpread=fi['angularRange'])

def merged_native(G,seed,X,m):
    total=seed.copy()
    for j,(tag,k) in enumerate(G.ch[:-3]):
        if tag=='height':total[:,2*m+1+k]+=X[:,j]
        else:total[:,abs(k)]+=X[:,j];total[:,m+abs(k)]+=np.sign(k)*X[:,j]
    return total

class Audit:
    """Compute full six jets on all requested angles, batching the original field by radial rows."""
    def __init__(self,api,micro,src,geo,a,kn,metric,nu,fractions,shift):
        self.m=micro;self.nu=nu;self.modes=a.modes
        c=a.full_sleeve;d=a.full_gate;cells=np.unique(kn)
        self.q=np.unique(np.r_[0,c,c+d,a.lift_end,src.S,cells,(cells[:-1,None]+np.diff(cells)[:,None]*np.array(fractions)).ravel()])
        q=self.q;B=api.Bvals(q,kn);self.B=B
        self.phi,_=profiles(api,src,geo,a,nu,shift)
        self.base=np.empty((len(q),6,nu,3));self.rho=np.empty((len(q),nu))
        self.orders=src.base.O
        for j in range(0,len(q),16):
            ix=slice(j,j+16);v=q[ix]
            th,old,rr=src.prefix(v/src.S,nu,shift)
            if j==0:
                self.th=th;self.u=src.center.arc(th)
                orig,diff,sp=api.central_delta(src,geo,None,th,1.,a.anchor)
            cyl=np.zeros_like(old)
            for k,n in ((0,0),(2,1),(5,2)):cyl[:,k]=orig[n]+diff[n]
            cyl[:,0,:,2]+=v[:,None];cyl[:,1,:,2]=1
            h=api.step(v,0,a.lift_end);lift=(1-h[0],-h[1],-h[2])
            for k,(r,n) in enumerate(self.orders):old[:,k]+=lift[r][:,None,None]*diff[n][None]
            gate,g1,g2=api.step(v,c,c+d)
            J=cyl+gate[:,None,None,None]*(old-cyl)
            J[:,1]+=g1[:,None,None]*(old[:,0]-cyl[:,0])
            J[:,3]+=2*g1[:,None,None]*(old[:,1]-cyl[:,1])+g2[:,None,None]*(old[:,0]-cyl[:,0])
            J[:,4]+=g1[:,None,None]*(old[:,2]-cyl[:,2])
            self.base[ix]=J;self.rho[ix]=(1-gate[:,None])*sp+gate[:,None]*rr
        M=api.Bvals(q,np.asarray(metric['knots']))[0]
        self.Q=1+(M@np.asarray(metric['q']))[:,None]
        self.W=1+(M@np.asarray(metric['w']))[:,None]
    def report(self,native,extra):
        out=dict(peak=-1.,curvature=-1.,minimumSupport=float('inf'),minimumArea=float('inf'),minimumZs=float('inf'))
        count=0;ss=0.
        for i in range(0,len(self.q),16):
            ix=slice(i,i+16);J=self.base[ix].copy()
            for j,(r,d) in enumerate(self.orders):
                B=self.B[r][ix]
                J[:,j]+=self.m.fft_forward(B@native,self.modes,self.nu,self.th[0],d)
                C=B@extra
                for z in range(3):J[:,j,:,z]+=C@self.phi[d,z]
            _,err,_=self.m.gram(J,self.Q[ix],self.W[ix],self.rho[ix])
            cur,ar=self.m.curvature(J);normal=np.cross(J[:,2],J[:,1])
            sig=np.sum(normal*J[:,0],axis=-1)/np.sqrt(ar)
            for tag,xx,coord in (('peak',err,'worstMetric'),('curvature',cur,'worstCurvature')):
                z=np.unravel_index(xx.argmax(),xx.shape);val=float(xx[z])
                if val>out[tag]:out[tag]=val;out[coord]=[float(self.q[i+z[0]]),float(self.th[z[1]]),float(self.u[z[1]])]
            out['minimumSupport']=min(out['minimumSupport'],float(sig.min()))
            out['minimumArea']=min(out['minimumArea'],float(np.sqrt(ar).min()))
            out['minimumZs']=min(out['minimumZs'],float(J[:,1,:,2].min()))
            ss+=float(np.sum(err**2));count+=err.size
        out.update(rms=float(np.sqrt(ss/count)),radialRows=len(self.q),angles=self.nu)
        return out

def main():
    p=argparse.ArgumentParser()
    for n in ('direct-source','scripts','work','physical-source','refinement-source','angular-source','comparison','parent','out'):
        p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--split',action='store_true')
    for n,d in (('modes',0),('angles',216),('test-angles',321),('radial',125),('test-radial',181),('holdout-angles',1725),('steps',4),('guard-angles',1152)):
        p.add_argument('--'+n,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    direct=module(a.direct_source,'r262_physical_banded_support')
    ref=module(a.refinement_source,'direct_r262_cut_grid')
    ar=module(a.angular_source,'direct_r262_d3_physical_eval')
    api=module(a.physical_source,'direct_r262_true_cut')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','direct_r262_background')
    geo=module(a.comparison,'direct_r262_central')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z:raise ValueError('Direct cut consumer needs its full-amplitude cut state')
        oldX=z['inletNativeXYZ'].copy() if 'physicalInletProfiles' in z else z['actualPhysicalXYZ'].copy()
        extra0=z['physicalInletProfiles'].copy() if 'physicalInletProfiles' in z else np.zeros((len(oldX),3))
        if 'inletProfileSourceSHA' in z and str(z['inletProfileSourceSHA'])!=sha(__file__):raise ValueError('Input has a different inlet profile definition')
        oldkn=z['knots'].copy()
        m0=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
        frozen={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor','metricQ','metricW')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles):raise ValueError('Native frequency reaches Nyquist')
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    geo.LOW=a.low;geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    src=micro.Source(a)
    extra=prolong_extra(oldkn,extra0,a.split)
    def model(nr,nu,shift):
        return joint_model(ref,api,micro,src,geo,ar,direct,a,kn,oldkn,oldX,metric,nr,nu,shift,extra0)
    G,fi=model(a.radial,a.angles,False);Q,qi=model(a.test_radial,a.test_angles,True)
    X=np.zeros(G.shape)
    Ag=Audit(api,micro,src,geo,a,kn,metric,a.guard_angles,(.5,),True)
    nc=lambda x:merged_native(G,seed,x,a.modes)
    ex=lambda x:extra+x[:,-3:]
    guard=lambda x:Ag.report(nc(x),ex(x))
    base=G.report(X);test0=Q.report(X);guard0=guard(X);currguard=guard0
    trial,info=leading(api,geo,a,G,fi,kn,metric,seed,extra)
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
    hold=Audit(api,micro,src,geo,a,kn,metric,a.holdout_angles,(.137,.439,.823),False)
    initialHeld=hold.report(seed,prolong_extra(oldkn,extra0,a.split));end=hold.report(total,extra)
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:
        np.savez_compressed(f,**frozen,inletNativeXYZ=total,physicalInletProfiles=extra,inletProfileSourceSHA=sha(__file__),metricKnots=mk,knots=kn,modes=a.modes,spans=a.spans)
    result=dict(schema='R262-cut-own-three-material-Cauchy-inlet-profiles-and-frozen-metric-v1',entrySHA256=sha(__file__),stateSHA256=sha(state),parentSHA256=sha(a.parent),fieldSHA256=src.source_sha,
                physicalSourceSHA256=sha(a.physical_source),angularSourceSHA256=sha(a.angular_source),directSourceSHA256=sha(a.direct_source),refinementSourceSHA256=sha(a.refinement_source),
                metricVariables=0,positionVariables=int(X.size),additionalInletVariables=3*len(kn[6:-6]),formalLeading=info,angularFactorReports=[fi,qi],unscaledCubicCorrection=rawlead,
                initial=base,initialSecondary=test0,initialGuard=guard0,accepted=history,attempts=log,normalAndRhsAgreement=check,finalAngularGuard=currguard,initialIndependent=initialHeld,independent=end,
                stateUse='The three physicalInletProfiles columns multiply N/k, the actual lifted old center-to-sleeve discrepancy at q=c, and the vertical 1/k^2. Use this source profiles() or Audit() for all three. The native part is deliberately named inletNativeXYZ and must be combined with all three columns.')
    with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('END_INLET',end,flush=True)
if __name__=='__main__':main()
