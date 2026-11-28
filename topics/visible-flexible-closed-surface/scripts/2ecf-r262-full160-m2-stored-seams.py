#!/usr/bin/env python3
"""Original frozen 160-cell weighted R262 background: propagated bounded m=2 line and relative/absolute shape gain."""
import argparse,hashlib,importlib.util,json,math,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import solve_ivp
from fractions import Fraction as Q
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
L=np.longdouble
def transfer(bg,N,keep):
    anchors={}
    for rq in (.16,.17,.18,.19,.20,.21,.23,.25,.28,.32,.36,.4):
        w,wr,_,_,n,j,xx=bg.point(L(rq));anchors.setdefault((n,j),[]).append((rq,xx))
    ring_index={}
    nodes,weights=np.polynomial.legendre.leggauss(4);c=(nodes+1)/2;weights=weights/2;s=np.array([.5-np.sqrt(3)/6,.5+np.sqrt(3)/6])
    weightsAt=[]
    for k,t in enumerate(c):
        pp=Polynomial.fromroots(np.delete(c,k))/np.prod(t-np.delete(c,k));v=pp.integ()
        weightsAt.append(v(s)-v(0))
    weightsAt=np.array(weightsAt).T
    y=np.array([1.,0.],dtype=L);ln=L(0);rows=[];count=0;maxangle=L(0);maxDi=L(0)
    for n in range(159,-1,-1):
        mu=bg.cuff**7*L(2)**(-L(11)*n/4)
        if n<159:y[1]*=L(2)**(-L(11)/4)
        for j in range(9):
            row=bg.profiles[9*n+j];pts=np.unique(np.r_[np.linspace(0,1,N+1,dtype=L),row.left,row.right,[v[1] for v in anchors.get((n,j),[])]]);lo=pts[:-1];h=np.diff(pts)
            x=lo[:,None]+h[:,None]*c;A,B,_,_=bg.source.evaluate(n,j,x);dr=A+bg.alpha*B
            total=h*(dr@weights);r0=row.r_left+np.r_[L(0),np.cumsum(total[:-1])]
            r=r0[:,None]+h[:,None]*(dr@weightsAt.T)
            x=lo[:,None]+h[:,None]*s;A,B,w,wd=bg.source.evaluate(n,j,x);dr=A+bg.alpha*B
            av=(np.sqrt(L(12))*mu/(r**8*w)*dr)*h[:,None];bv=(np.sqrt(L(12))*r**6*w/mu*dr)*h[:,None]
            aa=av.mean(axis=1);bb=bv.mean(axis=1);dd=-np.sqrt(L(3))/12*(av[:,1]*bv[:,0]-av[:,0]*bv[:,1])
            d2=dd**2-aa*bb;t=np.sqrt(abs(d2));maxangle=max(maxangle,t.max());maxDi=max(maxDi,abs(dd).max())
            cs=np.where(d2<=0,np.cos(t),np.cosh(t))
            sn=np.ones_like(t);ii=t>1e-13;sn[ii]=np.where(d2[ii]<=0,np.sin(t[ii]),np.sinh(t[ii]))/t[ii]
            m00=cs+sn*dd;m11=cs-sn*dd;m01=sn*aa;m10=-sn*bb
            if keep:A0,B0,w0,dw0=bg.source.evaluate(n,j,lo);wr0=dw0/(A0+bg.alpha*B0)
            stride=max(1,N//10)
            for k in range(len(h)):
                matched=[r for r,x in anchors.get((n,j),[]) if lo[k]==x]
                if keep and (k%stride==0 or k==len(h)-1 or matched):
                    for rpoint in matched:ring_index[rpoint]=len(rows)
                    rows.append([n,j,float(lo[k]),float(r0[k]),float(w0[k]),float(wr0[k]),float(np.log(mu)),float(y[0]),float(y[1]),float(ln)])
                yy=m00[k]*y[0]+m01[k]*y[1];zz=m10[k]*y[0]+m11[k]*y[1]
                norm=np.hypot(yy,zz);y[0],y[1]=yy/norm,zz/norm;ln+=np.log(norm)
            count+=len(h)
    r,w=bg.cut,L(.5);slope=4/r+np.sqrt(L(12))*mu*y[1]/(r**8*w*y[0]);logH=ln+np.log(abs(y[0]))+4*np.log(r)
    out=dict(stepsPerSegment=N,magnusIntervals=count,cutSlope=float(slope),cutLogHeightGain=float(logH),maxLocalExponent=float(maxangle),maxMagnusDiagonal=float(maxDi))
    if keep:
        a=np.array(rows,dtype=L);r,w,wr,lmu,q,p,logq=a[:,3:].T
        sg=np.sign(y[0]);sc=sg*np.exp(logq-logH);H=q*r**4*sc;J=np.sqrt(L(12))*np.exp(lmu)*p*sc/(r**4*w)
        Hr=4*H/r+J;P=-2*H/(r*w);Lr=J/w;E=1+w*w;n0=w/(r*np.sqrt(E));l0=wr/E**L(1.5)
        eta=-E*Lr;zeta=np.sqrt(E)*(3*P-2*Lr);dn=n0*eta;dm=n0*zeta;dl=-l0*eta
        out['unitCutMaxima']={}
        for key,vec in dict(H=H,Hr=Hr,P=P,L=Lr,relativeN=eta,relativeM=zeta,deltaN=dn,deltaM=dm,deltaL=dl,shapeRow=np.maximum(abs(dl)+abs(dm),abs(dn)+abs(dm))).items():
            i=np.argmax(abs(vec));out['unitCutMaxima'][key]=dict(value=float(vec[i]),cell=int(a[i,0]),profile=int(a[i,1]),x=float(a[i,2]),r=float(r[i]))
        out['samples']=len(a)
        out['anchors']=[]
        for rpoint,i in sorted(ring_index.items()):
            shape=np.maximum(abs(dl[:i+1])+abs(dm[:i+1]),abs(dn[:i+1])+abs(dm[:i+1]));out['anchors'].append(dict(r=rpoint,cell=int(a[i,0]),profile=int(a[i,1]),x=float(a[i,2]),w=float(w[i]),wr=float(wr[i]),H=float(H[i]),Hr=float(Hr[i]),innerShapePerUnitH=float(shape.max()/abs(H[i])),canonicalQ=float(q[i]),canonicalZ=float(p[i]),mu=float(np.exp(lmu[i]))))
    return out
def prefix(joint,data,meta,bridge,D):
    import gzip
    with gzip.open(data,'rb') as f:
        with np.load(f) as z:end=z['mesh'][-1]
    g=joint.ExactMetric(json.loads(meta.read_bytes()),json.loads(bridge.read_bytes()),end)
    T1=float(g.Tu);T2=float(g.prefix);S=float(g.total)
    def rhs(s,y):
        r,v,vv=g.profile(np.array([s],dtype=L));r,v,vv=map(lambda a:float(a[0]),(r,v,vv));b=math.sqrt(1-v*v)
        A=np.array([[v/r,-4*b/r],[vv/b**3,0.]])
        return (A@y.reshape(2,-1)).ravel()
    cuts=np.unique(np.r_[np.array(g.breakpoints,float)*S,0,T1,T2,S]);cuts=cuts[(cuts>=0)&(cuts<=S)]
    def flow(start,end):
        F=np.eye(2)
        pts=np.r_[start,cuts[(cuts>start+1e-12)&(cuts<end-1e-12)],end]
        for l,r in zip(pts[:-1],pts[1:]):
            if r-l<1e-13:continue
            q=solve_ivp(rhs,(l,r),F.ravel(),method='DOP853',rtol=1e-11,atol=1e-13)
            if not q.success:raise RuntimeError(q.message)
            F=q.y[:,-1].reshape(2,2)
        return F
    P1=flow(0,T1);P2=flow(T1,T2);P3=flow(T2,S)
    r=.6;w=.5;endv=-1/math.sqrt(1+w*w);b=w/math.sqrt(1+w*w)
    # The actual cut rate is H_r/H. For physical f and q=(v/b)f+H, it fixes
    # f=-w(rD-4)H/3, q=(rD-1)H/3. The two numbers define a projective line.
    target=np.array([-w*(r*D-4)/3,(r*D-1)/3]);target/=np.linalg.norm(target)
    normal=np.array([-target[1],target[0]]);initial=np.array([1.,0.]);B1=P1@initial
    B2=P2@B1;pred=P3@B2;values=[]
    for name,R,inlet,after in [('after_up',1+float(g.delta),B1,P3@P2),('before_bridge',1,B2,P3)]:
        derivative=after@np.array([-4*inlet[1]/R,0.]);ell=-float(normal@pred)/float(normal@derivative)
        Y=pred+ell*derivative;H=Y[1]-endv/b*Y[0]
        values.append(dict(at=name,coastLength=ell,positive=ell>=0,cutHeightGainForUnitCentral=H,normalizedCutVector=Y.tolist(),absoluteTerminalCross=float(abs(normal@Y))))
    return dict(S=S,Tu=T1,upPlusDown=T2,transferUp=P1.tolist(),transferDown=P2.tolist(),transferBridge=P3.tolist(),targetLine=target.tolist(),originalTerminalCross=float(normal@pred),coastMatches=values)
def main():
    p=argparse.ArgumentParser();p.add_argument('--scripts',type=Path,required=True);p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--steps',type=int,nargs='+',default=[48,96,192]);a=p.parse_args()
    S=a.scripts;n=S.parent/'notes';m=n/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json';c=n/'2026-11-09-db6f-tail-finite-source-calibrations.json'
    bg=load(S/'6a65-m12-original-tail-background.py','r262_m2_background').OriginalTailBackground(m,c,L('2e-18'))
    joint=load(S/'6a65-m12-global-common-cut-position-recovered.py','r262_m2_prefix')
    vals=[]
    for grid in a.steps:
        val=transfer(bg,grid,grid==a.steps[-1]);vals.append(val);print('full',grid,val,flush=True)
    out=dict(schema='original-R262-full160-protected-m2-line-and-inserted-round-coast-continuation-v1',entrySHA256=sha(__file__),manifestSHA256=sha(m),calibrationSHA256=sha(c),alphaValue=float(bg.alpha),finite=vals,
        prefix=prefix(joint,a.data,n/joint.ad.base.META_NAME,n/'2026-11-09-db6f-root-exact-bridge-m12.json',vals[-1]['cutSlope']),rigorousNumericalIntegration=False)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('prefix',out['prefix'],flush=True)
if __name__=='__main__':main()
