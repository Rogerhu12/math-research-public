#!/usr/bin/env python3
"""Exact sampled block-banded normal step for the true large-amplitude R262 cut, with a fixed metric and the entire saved physical Cartesian map."""
import argparse,hashlib,importlib.util,json,os,sys,time
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solveh_banded,LinAlgError

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def native_basis(G,theta):
    for j,(tag,m) in enumerate(G.ch):
        co=np.cos(m*theta);si=np.sin(m*theta);G.phi[:,:,j]=0
        if tag=='plane':
            G.phi[0,0,j]=co;G.phi[0,1,j]=si
            G.phi[1,0,j]=-m*si;G.phi[1,1,j]=m*co
            G.phi[2,0,j]=-m*m*co;G.phi[2,1,j]=-m*m*si
        else:
            G.phi[0,2,j]=co;G.phi[1,2,j]=-m*si;G.phi[2,2,j]=-m*m*co

def band_action(ab,h):
    y=ab[0]*h
    for d in range(1,len(ab)):
        if d>=len(h):break
        v=ab[d,:len(h)-d];y[d:]+=v*h[:-d];y[:-d]+=v*h[d:]
    return y

def assemble(G,X,power):
    v,u,res,err=G.metrics(X);nr,na=G.shape
    B,D=G.B[:2];n=nr*na
    blocks=np.zeros((6,nr,na,na));gradient=np.zeros((nr,na))
    wt=np.maximum(.04,err/max(float(err.max()),1e-30))**power/np.sqrt(err.size)
    P0=G.phi[0];P1=G.phi[1]
    for i in range(len(B)):
        use=np.flatnonzero((B[i]!=0)|(D[i]!=0))
        if not len(use):continue
        if use[-1]-use[0]>5:raise ArithmeticError('Nonlocal span in quintic basis')
        w=wt[i,:,None];Q=G.Q[i,0];W=G.W[i,0];rho=G.rho[i,:,None]
        vs=v[i];us=u[i];q=np.sqrt(2)/(rho*np.sqrt(Q*W))
        def evaluate(vec,phi):
            return sum((vec[:,j,None]*phi[j].T for j in range(3)))
        # Coefficient of D_i in R_E,R_F and of B_i in R_F,R_G.
        E=2*w/Q*evaluate(vs,P0)
        Fd=w*q*evaluate(us,P0)
        Fb=w*q*evaluate(vs,P1)
        A=2*w/(rho*rho*W)*evaluate(us,P1)
        Jdd=E.T@E+Fd.T@Fd;Jbb=Fb.T@Fb+A.T@A;Jdb=Fd.T@Fb
        r=res[:,i]*wt[i][None]
        gd=E.T@r[0]+Fd.T@r[1];gb=Fb.T@r[1]+A.T@r[2]
        for j in use:
            gradient[j]+=D[i,j]*gd+B[i,j]*gb
            for h in use:
                if h<j:continue
                blocks[h-j,j]+=((D[i,h]*D[i,j])*Jdd+(B[i,h]*B[i,j])*Jbb+
                    (D[i,h]*B[i,j])*Jdb+(B[i,h]*D[i,j])*Jdb.T)
    diag=6*na-1;ab=np.zeros((diag+1,n))
    rr,cc=np.indices((na,na))
    for gap in range(6):
        off=gap*na+rr-cc;keep=off>=0
        for j in range(nr-gap):
            block=blocks[gap,j]
            ab[off[keep],j*na+cc[keep]]=block[keep]
    return ab,gradient.ravel()

def transfer(kn,X,newm,split):
    oldm=(X.shape[1]-2)//3
    if newm<oldm:raise ValueError('Do not remove parent angular modes')
    if split:
        b=BSpline(kn,np.pad(X,((3,3),(0,0))),5,axis=0);breaks=np.unique(kn)
        for z in breaks[:-1]+np.diff(breaks)/2:b=b.insert_knot(z)
        kn=b.t.copy();X=b.c[3:-3]
    Y=np.zeros((len(X),3*newm+2))
    Y[:,:oldm+1]=X[:,:oldm+1]
    Y[:,newm+1:newm+oldm+1]=X[:,oldm+1:2*oldm+1]
    Y[:,2*newm+1:2*newm+oldm+2]=X[:,2*oldm+1:]
    return kn,Y

def check_normal(G,x,power,ab,grad):
    op,res,sc=G.linear(x,power);sc=sc.ravel()
    rng=np.random.default_rng(20261128)
    h=rng.standard_normal(len(grad));z=op.rmatvec(op.matvec(h/sc))/sc
    g=op.rmatvec(res)/sc
    de=float(np.linalg.norm(band_action(ab,h)-z)/max(1e-25,np.linalg.norm(z)))
    dg=float(np.linalg.norm(g-grad)/max(1e-25,np.linalg.norm(g)))
    if max(de,dg)>1e-9:raise ArithmeticError('Band/physical differential mismatch '+str((de,dg)))
    return [de,dg]

def main():
    p=argparse.ArgumentParser()
    for n in ('scripts','work','physical-source','refinement-source','angular-source','comparison','parent','out'):
        p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--split',action='store_true')
    for n,d in (('modes',0),('angles',216),('test-angles',321),('radial',125),('test-radial',181),('holdout-angles',411),('holdout-radial',237),('steps',6)):
        p.add_argument('--'+n,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    ref=module(a.refinement_source,'direct_r262_cut_grid')
    ar=module(a.angular_source,'direct_r262_d3_physical_eval')
    api=module(a.physical_source,'direct_r262_true_cut')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','direct_r262_background')
    geo=module(a.comparison,'direct_r262_central')
    with np.load(a.parent,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z:raise ValueError('Direct cut consumer needs its full-amplitude cut state')
        oldX=z['actualPhysicalXYZ'].copy();oldkn=z['knots'].copy()
        m0=int(z['modes']);mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn.copy()
        metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
        frozen={k:z[k].copy() for k in ('fieldSHA','sourceSHA','comparisonSHA','S','T','fullGate','fullSleeve','liftEnd','lam','low','anchor','metricQ','metricW')}
    a.modes=a.modes or m0;a.material_modes=a.modes
    if 2*a.modes>=min(a.angles,a.test_angles):raise ValueError('Native frequency reaches Nyquist')
    kn,seed=transfer(oldkn,oldX,a.modes,a.split);a.spans=len(np.unique(kn))-1
    geo.LOW=a.low;geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    src=micro.Source(a)
    def model(nr,nu,shift):
        G=ar.Model(ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,nr,nu,shift)
        native_basis(G,G.G.u);return G
    G=model(a.radial,a.angles,False);Q=model(a.test_radial,a.test_angles,True)
    X=np.zeros(G.shape);initial=G.report(X);ind0=Q.report(X);ind=ind0
    log=[];history=[];verify=None
    for step in range(a.steps):
        t0=time.monotonic();before=G.report(X);pwr=6 if step<2 else 10
        e=G.metrics(X)[3];v0=float(np.mean(e**pwr)**(1/pwr))
        best=None
        for power in ((.55,1.4) if step<2 else (.9,2.1)):
            ab,grad=assemble(G,X,power)
            if verify is None:verify=check_normal(G,X,power,ab,grad)
            sc=1/np.sqrt(np.maximum(ab[0],1e-25));N=len(sc)
            for d in range(min(len(ab),N)):
                ab[d,:N-d]*=sc[d:]*sc[:N-d]
            base_diagonal=ab[0].copy()
            for mu in (1e-12,1e-9,1e-6,1e-4,.003):
                ab[0]=base_diagonal+mu
                try:y=solveh_banded(ab,-sc*grad,lower=True,check_finite=False)
                except LinAlgError:continue
                dx=(sc*y).reshape(X.shape)
                for alpha in (1.,.5,.25,.125,.0625,.03125):
                    T=X+alpha*dx;ee=G.metrics(T)[3];peak=float(ee.max());val=float(np.mean(ee**pwr)**(1/pwr))
                    if peak>=max(before['peak'],ind['peak']) or val>=v0:continue
                    r=G.report(T)
                    if r['curvature']>max(a.curvature_guide,before['curvature']+1e-5):continue
                    # The shifted actual full-gate support should also improve.
                    other=Q.report(T)
                    if max(peak,other['peak'])>=max(before['peak'],ind['peak']) or other['curvature']>max(a.curvature_guide,ind['curvature']+1e-5):continue
                    normalized=val/v0+.25*peak/before['peak']+.15*other['peak']/ind['peak']
                    if best is None or normalized<best[0]:best=(normalized,T,r,other,power,mu,alpha)
            # The second weight is a fallback if the first full direct family did not decrease.
            if best is not None:break
        log.append(dict(step=step+1,seconds=time.monotonic()-t0,accepted=best is not None))
        if best is None:break
        _,X,r,ind,power,mu,alpha=best
        history.append(dict(step=step+1,irlsPower=power,scaledNormalDiagonal=mu,scale=alpha,training=r,shifted=ind))
        print('ACCEPT_DIRECT',step+1,r,ind,'mu',mu,'alpha',alpha,flush=True)
    total=seed.copy();m=a.modes
    for j,(tag,mode) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+mode]+=X[:,j]
        else:
            f=abs(mode);total[:,f]+=X[:,j];total[:,m+f]+=np.sign(mode)*X[:,j]
    # Recompute the merged row coefficients through the normal saved-field entry.
    fresh=ref.cut_grid(api,micro,src,geo,a,kn,metric,a.holdout_radial,a.holdout_angles,True)
    final_holdout=fresh.report(total.ravel());base_holdout=fresh.report(seed.ravel())
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:np.savez_compressed(f,**frozen,actualPhysicalXYZ=total,metricKnots=mk,knots=kn,modes=m,spans=a.spans)
    out=dict(schema='R262-cut-frozen-metric-complete-banded-actual-Gauss-Newton-v1',entrySHA256=sha(__file__),stateSHA256=sha(state),parentSHA256=sha(a.parent),fieldSHA256=src.source_sha,
        physicalSourceSHA256=sha(a.physical_source),angularSourceSHA256=sha(a.angular_source),refinementSourceSHA256=sha(a.refinement_source),
        actualPositionVariables=G.nvar,actualMetricVariables=0,radialSpans=a.spans,angularModes=a.modes,lowerScalarDiagonals=6*len(G.ch),normalAndRhsAgreement=verify,initial=initial,initialIndependent=ind0,
        accepted=history,attempts=log,final=G.report(X),secondaryAcceptanceGrid=Q.report(X),initialFreshHoldout=base_holdout,independent=final_holdout,
        scope='All local supported columns and their cross blocks are assembled against the true two-jet source. The normalized complete normal matrix receives the reported diagonal damping. The saved field and fixed metric are available unchanged to the physical consumers.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('END_DIRECT',out['independent'],flush=True)
if __name__=='__main__':main()
