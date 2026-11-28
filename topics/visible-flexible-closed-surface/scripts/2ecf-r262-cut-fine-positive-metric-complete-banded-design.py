#!/usr/bin/env python3
"""Joint true large-amplitude cut position and fine positive radial metric design using complete banded Gauss-Newton."""
import argparse,bisect,hashlib,importlib.util,json,os,sys,time
from fractions import Fraction as F
from pathlib import Path
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solveh_banded,LinAlgError

def mod(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(z):return F.from_float(float(z))

def exact_metric_transfer(kn0,q,w,kn):
    old=list(map(fq,kn0));goal=list(map(fq,kn));zero=(F(0),F(0))
    v=[zero]*3+[(fq(a),fq(b)) for a,b in zip(q,w)]+[zero]*3
    if len(v)!=len(old)-6:raise ValueError('Wrong clamped parent metric')
    for t in sorted(set(goal)):
        if old.count(t)>goal.count(t):raise ValueError('Coarse metric knots are not contained')
        for _ in range(goal.count(t)-old.count(t)):
            i=bisect.bisect_right(old,t)-1;s=old.count(t);z=[]
            for j in range(len(v)+1):
                if j<=i-5:z.append(v[j])
                elif j>i-s:z.append(v[j-1])
                else:
                    a=(t-old[j])/(old[j+5]-old[j])
                    z.append(tuple(a*v[j][k]+(1-a)*v[j-1][k] for k in range(2)))
            old.insert(i+1,t);v=z
    if old!=goal or v[:3]!=[zero]*3 or v[-3:]!=[zero]*3:raise ValueError('Exact matching refinement failed')
    return v[3:-3]

def set_field(G,Y):
    G.Q=G.Q0+(G.B[0]@Y[:,-2])[:,None]
    G.W=G.W0+(G.B[0]@Y[:,-1])[:,None]
    return Y[:,:-2]

def report(G,Y):return G.report(set_field(G,Y))
def get_model(G,Y,power):
    X=set_field(G,Y);v,u,res,err=G.metrics(X)
    weight=np.maximum(.04,err/max(float(err.max()),1e-30))**power/np.sqrt(err.size)
    return v,u,res,weight

def joint_system(G,Y,power,test,direct):
    v,u,res,wt=get_model(G,Y,power);B,D=G.B[:2];nb,nm=G.shape;m=nm+2;n=nb*m
    blocks=np.zeros((6,nb,m,m));gradient=np.zeros((nb,m))
    if test:
        rng=np.random.default_rng(20261128);h=rng.standard_normal(Y.shape);JtJh=np.zeros_like(Y);normIndependent=np.zeros_like(Y)
        # Independent application uses complete tangent maps from the spatial evaluator.
        hv=G.forward_field(h[:,:-2],1,0);hu=G.forward_field(h[:,:-2],0,1)
        dq=(B@h[:,-2])[:,None];dw=(B@h[:,-1])[:,None]
        Q,W,rho=G.Q,G.W,G.rho;cr=np.sqrt(2)/(rho*np.sqrt(Q*W))
        E=2*np.sum(v*hv,axis=-1)/Q-(res[0]+1)/Q*dq
        FF=cr*(np.sum(u*hv,axis=-1)+np.sum(v*hu,axis=-1))-.5*res[1]*(dq/Q+dw/W)
        GG=2*np.sum(u*hu,axis=-1)/(rho*rho*W)-(res[2]+1)/W*dw
        def trans(t):
            e,f,g=t*wt[None]**2
            gv=(2*e/Q)[...,None]*v+(cr*f)[...,None]*u
            gu=(cr*f)[...,None]*v+(2*g/(rho*rho*W))[...,None]*u
            dX=D.T@G.planes(gv,0)+B.T@G.planes(gu,1)
            dq=B.T@np.sum(-(res[0]+1)/Q*e-.5*res[1]/Q*f,axis=1)
            dw=B.T@np.sum(-(res[2]+1)/W*g-.5*res[1]/W*f,axis=1)
            return np.column_stack((dX,dq,dw)).ravel()
        JtJh=trans(np.stack((E,FF,GG)));normIndependent=trans(res)
    for i in range(len(B)):
        active=np.flatnonzero((B[i]!=0)|(D[i]!=0))
        if not len(active):continue
        if active[-1]-active[0]>5:raise ValueError('Nonlocal physical quintic')
        nu=len(G.G.u);W=G.W[i,0];Q=G.Q[i,0];rho=G.rho[i,:,None]
        wh=wt[i,:,None];cr=np.sqrt(2)/(rho*np.sqrt(Q*W))
        ed=np.zeros((nu,m));fd=ed.copy();eb=ed.copy();fb=ed.copy();gb=ed.copy()
        def proj(vv,r):return sum((vv[:,j,None]*G.phi[r,j].T for j in range(3)))
        ed[:,:nm]=2*wh/Q*proj(v[i],0)
        fd[:,:nm]=wh*cr*proj(u[i],0)
        fb[:,:nm]=wh*cr*proj(v[i],1)
        gb[:,:nm]=2*wh/(rho*rho*W)*proj(u[i],1)
        eb[:,-2]=-wt[i]*(res[0,i]+1)/Q
        fb[:,-2]=-.5*wt[i]*res[1,i]/Q;fb[:,-1]=-.5*wt[i]*res[1,i]/W
        gb[:,-1]=-wt[i]*(res[2,i]+1)/W
        Jdd=ed.T@ed+fd.T@fd;Jbb=eb.T@eb+fb.T@fb+gb.T@gb;Jdb=ed.T@eb+fd.T@fb
        r=res[:,i]*wt[i]
        gd=ed.T@r[0]+fd.T@r[1];gb0=eb.T@r[0]+fb.T@r[1]+gb.T@r[2]
        for j in active:
            gradient[j]+=D[i,j]*gd+B[i,j]*gb0
            for k in active:
                if k<j:continue
                blocks[k-j,j]+=(D[i,k]*D[i,j]*Jdd+B[i,k]*B[i,j]*Jbb+
                    D[i,k]*B[i,j]*Jdb+B[i,k]*D[i,j]*Jdb.T)
    ab=np.zeros((6*m,n));rr,cc=np.indices((m,m))
    for d in range(6):
        idx=d*m+rr-cc;mask=idx>=0
        for j in range(nb-d):ab[idx[mask],j*m+cc[mask]]=blocks[d,j][mask]
    g=gradient.ravel();verify=None
    if test:
        a=np.linalg.norm(direct.band_action(ab,h.ravel())-JtJh)/max(1e-32,np.linalg.norm(JtJh))
        b=np.linalg.norm(g-normIndependent)/max(1e-32,np.linalg.norm(normIndependent))
        verify=[float(a),float(b)]
        if max(verify)>1e-9:raise ArithmeticError('Augmented band disagrees with actual differential '+str(verify))
    return ab,g,verify

def line(G,Y,dy):
    X=set_field(G,Y);v,u=G.first(X)
    dv=G.forward_field(dy[:,:-2],1,0);du=G.forward_field(dy[:,:-2],0,1)
    dot=lambda a,b:np.sum(a*b,axis=-1)
    E=(dot(v,v),2*dot(v,dv),dot(dv,dv))
    F0=(dot(v,u),dot(dv,u)+dot(v,du),dot(dv,du));GG=(dot(u,u),2*dot(u,du),dot(du,du))
    dq=(G.B[0]@dy[:,-2])[:,None];dw=(G.B[0]@dy[:,-1])[:,None];q0=G.Q.copy();w0=G.W.copy()
    def observe(t,p):
        q=q0+t*dq;w=w0+t*dw
        if np.min(q)<=0 or np.min(w)<=0:return np.inf,np.inf
        val=lambda a:a[0]+t*(a[1]+t*a[2])
        e=val(E)/q-1;g=val(GG)/(G.rho**2*w)-1;f=val(F0)/(G.rho*np.sqrt(q*w))
        error=abs(e+g)/2+np.hypot((e-g)/2,f)
        return float(np.mean(error**p)**(1/p)),float(error.max())
    return observe

def main():
    p=argparse.ArgumentParser()
    for key in ('scripts','work','physical-source','refinement-source','angular-source','direct-source','comparison','parent','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--split',action='store_true')
    for key,d in (('modes',0),('angles',216),('test-angles',321),('radial',121),('test-radial',169),('holdout-angles',411),('holdout-radial',231),('steps',6)):
        p.add_argument('--'+key,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69);a=p.parse_args()
    ref=mod(a.refinement_source,'design_cut_dense');ar=mod(a.angular_source,'design_spatial_operator')
    direct=mod(a.direct_source,'design_complete_band');api=mod(a.physical_source,'design_true_cut')
    geo=mod(a.comparison,'design_true_curvatures');micro=mod(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','design_R262')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z:raise ValueError('Actual full cut required')
        m0=int(z['modes']);oldX=z['actualPhysicalXYZ'].copy();oldkn=z['knots'].copy()
        mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        aq=z['metricQ'].copy();aw=z['metricW'].copy()
        root={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','S','T','fullSleeve','fullGate','liftEnd','lam','low','anchor')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles,a.holdout_angles):raise ValueError('Native modes reach Nyquist')
    kn,seed=direct.transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    mc=exact_metric_transfer(mk,aq,aw,kn);mf=np.array([[float(t) for t in row] for row in mc]);metric=dict(knots=mk.tolist(),q=aq.tolist(),w=aw.tolist())
    geo.LOW=a.low;geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    src=micro.Source(a)
    def model(nr,nu,shift):
        G=ar.Model(ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,nr,nu,shift)
        direct.native_basis(G,G.G.u);G.Q0=G.Q.copy();G.W0=G.W.copy();return G
    G=model(a.radial,a.angles,False);T=model(a.test_radial,a.test_angles,True)
    Y=np.zeros((G.shape[0],G.shape[1]+2));init=report(G,Y);ind=report(T,Y);ind0=ind
    hist=[];checks=None;times=[]
    for it in range(a.steps):
        start=time.monotonic();power=.6 if it<2 else 1.1;pwr=6 if it<3 else 10
        before=report(G,Y);_,_,_,e=G.metrics(Y[:,:-2]);v0=float(np.mean(e**pwr)**(1/pwr))
        pk0=max(before['peak'],ind['peak']);best=None
        for pow0 in (power,2.0):
            ab,g,chk=joint_system(G,Y,pow0,checks is None,direct)
            if chk is not None:checks=chk
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));N=len(sc)
            for d in range(min(len(ab),N)):ab[d,:N-d]*=sc[d:]*sc[:N-d]
            diag=ab[0].copy()
            for mu in (1e-12,1e-9,1e-6,1e-4,.003):
                ab[0]=diag+mu
                try:dy=(sc*solveh_banded(ab,-sc*g,lower=True,check_finite=False)).reshape(Y.shape)
                except LinAlgError:continue
                lg=line(G,Y,dy);lt=line(T,Y,dy);proposals=[]
                for alpha in 2.**(-np.arange(0,23)/2):
                    cand=Y+alpha*dy
                    if min((1+mf+cand[:,-2:]).min(),1.)<=0:continue
                    val,pk=lg(alpha,pwr)
                    if val>=v0 or pk>=pk0:continue
                    _,ph=lt(alpha,pwr);pnew=max(pk,ph)
                    if pnew<pk0:proposals.append((val/v0+.40*pnew/pk0,float(alpha)))
                for score,alpha in sorted(proposals):
                    if best is not None and score>=best[0]:break
                    cand=Y+alpha*dy;rr=report(G,cand);qq=report(T,cand)
                    if rr['curvature']>max(a.curvature_guide,before['curvature']+1e-5) or qq['curvature']>max(a.curvature_guide,ind['curvature']+1e-5):continue
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
    for j,(tag,mode) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+mode]+=Y[:,j]
        else:total[:,abs(mode)]+=Y[:,j];total[:,m+abs(mode)]+=np.sign(mode)*Y[:,j]
    outputKn=kn
    if not hist:
        newmetric=metric;outputKn=mk;choose=np.column_stack((aq,aw));rounderr=F(0)
    fresh=ref.cut_grid(api,micro,src,geo,a,kn,newmetric,a.holdout_radial,a.holdout_angles,True)
    initialGrid=ref.cut_grid(api,micro,src,geo,a,kn,metric,a.holdout_radial,a.holdout_angles,True)
    fixed=fresh.report(total.ravel());initialFresh=initialGrid.report(seed.ravel())
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:np.savez_compressed(f,**root,actualPhysicalXYZ=total,knots=kn,metricKnots=outputKn,metricQ=choose[:,0],metricW=choose[:,1],modes=m,spans=a.spans)
    out=dict(schema='R262-complete-cut-fine-positive-metric-and-XYZ-banded-design-v1',entrySHA256=sha(__file__),fieldSHA256=src.source_sha,parentSHA256=sha(a.parent),stateSHA256=sha(state),
        fixedPhysicalGeometrySourceSHA256=sha(a.physical_source),directSourceSHA256=sha(a.direct_source),actualPositionVariables=G.nvar,actualNewMetricVariables=2*len(mc),originalMetricCoefficientCount=int(2*len(aq)),
        fullNormalBandwidth=6*Y.shape[1],normalAndRhsAgreement=checks,positiveFineMetricControlInfimum=float(min(1.,(1+choose).min())),finalMetricCoefficientRoundingBoundExact=str(rounderr),
        initial=init,initialSecondary=ind0,accepted=hist,secondsPerActualSystem=times,initialHeldOut=initialFresh,finalFrozenCandidate=fixed,
        scope='The actual position and both radial target functions are jointly designed; these steps change the metric and are not fixed-metric refinement. The resulting dyadic target may now be held fixed in a separate completed refinement.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('FINAL_NEW_METRIC',fixed,flush=True)
if __name__=='__main__':main()
