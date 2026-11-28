#!/usr/bin/env python3
"""Retain every R262 ring and translate each entire outer half-tail outward, starting from the actual R317-family two-port sleeve."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solveh_banded,LinAlgError
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,vstack

def module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def knots(end,n):return np.r_[np.zeros(5),np.linspace(0,end,n+1),np.full(5,end)]
def axis(src,adj,phys,geo,a,n,nt,shift):
    theta,rep=adj.node_angles(src,phys,geo,a,n,nt,shift)
    # All spectral errors and the two signed Rayleigh cones are reflection
    # invariant. Actual native-angle columns are evaluated directly.
    half=np.pi/3;theta=np.sort(np.r_[0.,theta[(theta>1e-11)&(theta<half-1e-11)],half])
    theta=theta[np.r_[True,np.diff(theta)>1e-11]]
    return adj.SourceAt(src,theta),rep
def position(src,api,geo,a,s,drop=None):
    th,J,rho=src.prefix(s/src.S,len(src.theta),False)
    _,gamma,_=api.central_delta(src,geo,None,th,1.,a.anchor)
    h=api.step(s,0.,a.lift_end);w=(1-h[0],-h[1],-h[2])
    for j,(r,d) in enumerate(src.base.O):J[:,j]+=w[r][:,None,None]*gamma[d][None]
    if drop is not None:
        amount,v,dv=drop(s)
        levels=(np.where(s>=a.drop_end,a.tail_shift,a.full_sleeve-amount),-v,-dv)
        for j,(r,d) in enumerate(src.base.O):
            if d==0:J[:,j,:,2]+=levels[r][:,None]
    return J,rho
def exact_drop(a,vkn,raw):
    source=sum(F(float(x))*(F(float(vkn[i+9]))-F(float(vkn[i+3])))/6 for i,x in enumerate(raw))
    need=F(float(a.full_sleeve))-F(float(a.tail_shift))
    if need<=0 or source<=0:raise ValueError('Nonpositive exact height integral')
    scale=need/source
    sp=BSpline(vkn,np.pad(raw,(3,3))*float(scale),5,extrapolate=False);pr=sp.antiderivative()
    def drop(values):
        s=np.clip(values,0,a.drop_end)
        return np.where(values>=a.drop_end,float(need),pr(s)-pr(0)),sp(s),sp(s,1)
    return drop,dict(exactRawIntegral=str(source),exactRequiredIntegral=str(need),exactVelocityScale=str(scale),endTranslation=a.tail_shift)
def design(src,api,geo,a,kn,vkn):
    S=src.S;G=len(kn)-12;A=len(vkn)-12
    s=np.unique(np.r_[np.linspace(0,S,101),np.unique(kn),np.unique(vkn),a.lift_end,a.drop_end])
    J,rho=position(src,api,geo,a,s)
    p=J[:,1];u=J[:,2]/rho[...,None]
    E=np.sum(p*p,axis=-1);Fv=np.sum(p*u,axis=-1);Gv=np.sum(u*u,axis=-1)
    vr=api.Bvals(s,vkn)[0];ar=api.Bvals(s,kn)[0]
    rough=(a.full_sleeve-a.tail_shift)/a.drop_end
    sc=np.maximum(.06,.5*(np.max(E-2*rough*p[:,:,2]+rough**2,axis=1)+np.min(E-2*rough*p[:,:,2]+rough**2,axis=1)))
    wc=np.maximum(.15,.5*(np.max(Gv,axis=1)+np.min(Gv,axis=1)))
    rows=[];rhs=[];alpha=np.pi*np.arange(a.rayleigh)/a.rayleigh
    for i in range(len(s)):
        co=np.cos(alpha)/np.sqrt(sc[i]);si=np.sin(alpha)/np.sqrt(wc[i]);cc=co*co;ss=si*si;cs=2*co*si
        const=(E[i,:,None]-1)*cc+Fv[i,:,None]*cs+(Gv[i,:,None]-1)*ss
        v=(-2*p[i,:,2,None]*cc-u[i,:,2,None]*cs).reshape(-1,1)
        M=np.empty((len(v),A+2*G+1));M[:,:A]=v*vr[i]
        M[:,A:A+G]=-np.tile(cc,len(u[i]))[:,None]*ar[i];M[:,A+G:-1]=-np.tile(ss,len(u[i]))[:,None]*ar[i]
        M[:,-1]=-1.;rows.append(csr_matrix(M));rhs.append(-const.ravel())
        M[:,:-1]*=-1;rows.append(csr_matrix(M));rhs.append(const.ravel())
    eq=np.zeros((1,A+2*G+1));eq[0,:A]=(vkn[6:]-vkn[:-6])[3:-3]/6
    h=np.zeros((len(s),A+2*G+1));h[:,:A]=vr;rows.append(csr_matrix(h));rhs.append(np.maximum(0,p[:,:,2].min(axis=1)-.025))
    cost=np.zeros(A+2*G+1);cost[-1]=1
    sol=linprog(cost,A_ub=vstack(rows,format='csr'),b_ub=np.concatenate(rhs),A_eq=eq,b_eq=[a.full_sleeve-a.tail_shift],
                bounds=[(0,.85)]*A+[(-.98,3.)]*(2*G)+[(0,None)],method='highs')
    if not sol.success:raise ArithmeticError(sol.message)
    return sol.x[:A],sol.x[A:A+G],sol.x[A+G:-1],float(sol.fun)

def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','work','physical-source','cut','comparison','adjacent-source','angular-source','direct-source','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--seed',type=Path);p.add_argument('--split',action='store_true')
    for k,v in (('full-sleeve',.350),('tail-shift',.035),('drop-end',1.9),('lift-end',1.5),('anchor',np.pi/3),('curvature-guide',8.69)):
        p.add_argument('--'+k,type=float,default=v)
    for k,v in (('spans',32),('drop-spans',18),('modes',30),('rayleigh',12),('steps',5)):
        p.add_argument('--'+k,type=int,default=v)
    a=p.parse_args()
    phys=module(a.physical_source,'translated_adjacent_curve');api=module(a.cut,'translated_source_geometry');api.true_arc_position=phys.true_arc_position
    geo=phys.NormalCurve();adj=module(a.adjacent_source,'translated_true_material_angle_mesh')
    ar=module(a.angular_source,'translated_cartesian_full_basis');direct=module(a.direct_source,'translated_banded_normal')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','translated_raw_R262')
    path=a.work/'h2-c2-m48-g12-04r1';a.data=a.work/'m12-prefix-data.npz.gz';a.grid=path/'grid.json'
    a.query_report=path/'exact-tail-queries.json';a.query_cache=path/'exact-tail-queries.json.npz';a.field=path/'result.json.field.npz'
    src=micro.Source(a);a.material_modes=a.modes
    if not 0<a.tail_shift<a.full_sleeve or a.drop_end>=src.S:raise ValueError('Require genuine retained nonzero tail translation')
    initialKn=knots(src.S,a.spans);vkn=knots(a.drop_end,a.drop_spans)
    if a.seed is None:
        sc,lpaxis=axis(src,adj,phys,geo,a,252,21,False)
        raw,aq,aw,loss=design(sc,api,geo,a,initialKn,vkn)
        seed=np.zeros((len(initialKn)-12,3*a.modes+2));kn=initialKn.copy();mk=kn.copy()
    else:
        with np.load(a.seed,allow_pickle=False) as z:
            if str(z['sourceSHA'])!=sha(__file__) or str(z['physicalSHA'])!=sha(a.physical_source) or str(z['cutSHA'])!=sha(a.cut) or str(z['fieldSHA'])!=src.source_sha:raise ValueError('Different whole-ring family')
            for attr,tag in (('full_sleeve','sleeve'),('tail_shift','translation'),('drop_end','heightEnd'),('lift_end','liftEnd'),('anchor','anchor')):
                if float(z[tag])!=getattr(a,attr):raise ValueError('Different whole-ring physical parameter '+attr)
            aq=z['metricQ'].copy();aw=z['metricW'].copy();mk=z['metricKnots'].copy();raw=z['dropRaw'].copy();vkn=z['dropKnots'].copy()
            kn,seed=direct.transfer(z['knots'].copy(),z['translatedNativeXYZ'].copy(),a.modes,a.split)
        lpaxis=None;loss=None
    drop,ds=exact_drop(a,vkn,raw)
    def model(nr,n,nt,shift):
        ss,info=axis(src,adj,phys,geo,a,n,nt,shift);th=ss.theta
        c=np.unique(np.r_[kn,vkn,mk,0.,a.lift_end,src.S])
        frac=np.array([.109,.363,.629,.854]) if shift else np.array([.063,.281,.523,.779])
        q=np.unique(np.r_[c,(c[:-1,None]+np.diff(c)[:,None]*frac).ravel(),np.linspace(0,src.S,nr+1),src.S*(np.arange(nr)+(.693 if shift else .271))/nr])
        J,rho=position(ss,api,geo,a,q,drop);M=api.Bvals(q,mk)[0]
        G=ar.Model.__new__(ar.Model);G.G=SimpleNamespace(t=q/src.S,u=th,source=ss)
        G.micro=micro;G.B=api.Bvals(q,kn);G.ch=ar.channels(a.modes);G.phi=np.zeros((3,3,len(G.ch),len(th)))
        direct.native_basis(G,th);G.shape=(len(kn)-12,len(G.ch));G.nvar=int(np.prod(G.shape));G.orders=src.base.O
        G.rho=rho;G.Q=(1+M@aq+drop(q)[1]**2)[:,None];G.W=(1+M@aw)[:,None];G.base=J;G.u=src.center.arc(th)
        ang=adj.AtAngles(micro,th)
        for j,(r,d) in enumerate(G.orders):G.base[:,j]+=ang.fft_forward(G.B[r]@seed,a.modes,len(th),th[0],d)
        return G,dict(actualRadialRows=len(q),actualAngularRows=len(th),angleDefinition=info,minRadialMetric=float(G.Q.min()),minAngularMultiplier=float(G.W.min()))
    G,gi=model(89,228,13,False);T,ti=model(137,333,25,True)
    X=np.zeros(G.shape);init=G.report(X);ind0=T.report(X);hist=[];agr=None
    for it in range(a.steps):
        p0=G.report(X);p1=T.report(X);peak=max(p0['peak'],p1['peak']);best=None
        for power in (.6,1.5):
            ab,grad=direct.assemble(G,X,power)
            if agr is None:agr=direct.check_normal(G,X,power,ab,grad)
            sc=1/np.sqrt(np.maximum(1e-25,ab[0]));n=len(sc)
            for j in range(min(n,len(ab))):ab[j,:n-j]*=sc[j:]*sc[:n-j]
            diag=ab[0].copy()
            for mu in (1e-11,1e-8,1e-5,.002):
                ab[0]=diag+mu
                try:dx=(sc*solveh_banded(ab,-sc*grad,lower=True,check_finite=False)).reshape(X.shape)
                except LinAlgError:continue
                cand=[]
                for al in 2.**(-np.arange(0,21)/2):
                    Y=X+al*dx;pk=max(G.metrics(Y)[3].max(),T.metrics(Y)[3].max())
                    if pk<peak*(1-1e-11):cand.append((pk,float(al)))
                for pk,al in sorted(cand):
                    if best is not None and pk>=best[0]:break
                    Y=X+al*dx;r=G.report(Y);s=T.report(Y)
                    if r['curvature']>max(a.curvature_guide,p0['curvature']+1e-6) or s['curvature']>max(a.curvature_guide,p1['curvature']+1e-6):continue
                    if min(r['minimumSupport'],s['minimumSupport'])<min(.115,p0['minimumSupport'],p1['minimumSupport']):continue
                    best=(pk,Y,r,s,al,mu,power);break
            if best is not None:break
        if best is None:break
        _,X,r,s,al,mu,power=best;hist.append(dict(step=it+1,alpha=al,damping=mu,irlsPower=power,training=r,shifted=s))
        print('ACCEPT_TRANSLATED_TAIL',it+1,r,s,flush=True)
    total=seed.copy();m=a.modes
    for j,(tag,k) in enumerate(G.ch):
        if tag=='height':total[:,2*m+1+k]+=X[:,j]
        else:total[:,abs(k)]+=X[:,j];total[:,m+abs(k)]+=np.sign(k)*X[:,j]
    F0,fa=model(191,603,47,False);end=F0.report(X);old=F0.report(0*X)
    sf=a.out.with_suffix('.npz')
    with sf.open('xb') as f:
        np.savez_compressed(f,sourceSHA=sha(__file__),physicalSHA=sha(a.physical_source),cutSHA=sha(a.cut),fieldSHA=src.source_sha,translatedNativeXYZ=total,knots=kn,metricKnots=mk,metricQ=aq,metricW=aw,dropKnots=vkn,dropRaw=raw,
                            sleeve=a.full_sleeve,translation=a.tail_shift,heightEnd=a.drop_end,liftEnd=a.lift_end,anchor=a.anchor,modes=a.modes)
    res=dict(schema='actual-R317-type-all-original-rings-with-outward-translated-infinite-tails-and-frozen-positive-metric-v1',sourceSHA=sha(__file__),physicalSHA=sha(a.physical_source),stateSHA=sha(sf),fieldSHA=src.source_sha,
             seedSHA=sha(a.seed) if a.seed else None,originalS=src.S,originalT=src.T,newS=src.S+a.full_sleeve,newT=src.T+a.full_sleeve,eachHalfTailOutwardTranslation=a.tail_shift,
             trueAxialIntegral=ds,designedMetricCoefficients=len(aq)+len(aw),initialLPRayleighObjective=loss,initialLPGrid=lpaxis,frozenPositionVariables=G.nvar,
             grids=[gi,ti,fa],fixedMetricInitial=init,fixedMetricInitialSecondary=ind0,fixedMetricAccepts=hist,actualMatrixAgreement=agr,originalFixedHoldout=old,independent=end,
             scope='The prescribed axial translation term equals delta for original s>=H. Beyond the last XYZ support S the whole original tail, actual cuff and capping flat disk move rigidly by that amount. Local tail metric/curvature are unchanged relative to that same input; complete new diameter, mixed distances and nonlocal reach require actual new bounds.')
    with a.out.open('x') as f:json.dump(res,f,indent=2);f.write('\n')
    print('END_TRANSLATED_TAIL',end,flush=True)
if __name__=='__main__':main()
