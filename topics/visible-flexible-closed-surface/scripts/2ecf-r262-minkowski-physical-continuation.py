#!/usr/bin/env python3
"""Full original R262 geometry with a true equal-perimeter Minkowski central port and unrestricted integer angular corrections."""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
from fractions import Fraction as Q
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import ellipe,ellipeinc
from scipy.optimize import brentq
from scipy.linalg import solve
O=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def dot(a,b):return np.sum(a*b,axis=-1)
def xy_det(a,b):return a[:,0]*b[:,1]-a[:,1]*b[:,0]
def polynomial(t,j):
    from numpy.polynomial.polynomial import polyder,polyval
    return polyval(t,polyder([1.,0,0,-10,15,-6.],j))
def normalized_ellipse():
    gap=21/20
    b=brentq(lambda b:(2/np.pi)*(b+gap)*ellipe(1-(b/(b+gap))**2)-1,.1,1.,xtol=1e-15)
    return b+gap,b

class Center:
    def __init__(self,joint,data):
        _,c=joint.ad.exact_section(data,Q(0));self.raw=joint.ad.NativeCurve(c,512,32)
        self.base=joint.ad.FixedRadiusCurve(self.raw,1.);self.ellipse=normalized_ellipse()
        self.mat=joint.bvp.glue.material_angle
    def arc(self,t):
        return np.concatenate([self.mat(self.raw,np.clip(t[j:j+32],0,2*np.pi)) for j in range(0,len(t),32)])
    def native(self,t,eta,arc=False):
        p,v,a,b=[self.base.derivative(t,j) for j in range(4)];spd=np.linalg.norm(v,axis=1)
        T=v/spd[:,None];N=np.c_[T[:,1],-T[:,0],0*spd];ea,eb=self.ellipse
        h=np.hypot(ea*N[:,0],eb*N[:,1]);rho=(ea*eb)**2/h**3
        w=xy_det(v,a)/spd**2;ww=xy_det(v,b)/spd**2-2*dot(v,a)*w/spd**2
        qp=N*np.array([ea**2,eb**2,0])/h[:,None]
        qv=(rho*w)[:,None]*T
        drho=-3*rho*(eb**2-ea**2)*N[:,0]*N[:,1]/h**2
        qa=(drho*w*w+rho*ww)[:,None]*T-(rho*w*w)[:,None]*N
        if arc:
            # The eccentric anomaly of the ellipse contact, lifted to the same turn as theta.
            ang=np.arctan2(eb*N[:,1],ea*N[:,0]);ang+=2*np.pi*np.rint((t-ang)/(2*np.pi))
            return (1-eta)*self.arc(t)+eta*ea*(ellipeinc(ang+np.pi/2,1-(eb/ea)**2)-ellipe(1-(eb/ea)**2))
        return [(1-eta)*r+eta*s for r,s in ((p,qp),(v,qv),(a,qa))]
    def difference(self,t,eta):
        u=self.arc(t);th=t.copy()
        for j in range(12):
            v=self.native(th,eta)[1];res=self.native(th,eta,True)-u
            if abs(res).max()<1.3e-14:break
            th=np.clip(th-res/np.linalg.norm(v,axis=1),0.,2*np.pi)
        if abs(res).max()>1e-12:raise RuntimeError('Minkowski arclength inverse failed')
        p,v,a=self.native(th,eta);p0,v0,a0=self.native(t,0.);j0=np.linalg.norm(v0,axis=1);j1=np.linalg.norm(v,axis=1)
        t1=j0/j1;t2=(dot(v0,a0)/j0-dot(v,a)/j1*t1**2)/j1
        return np.asarray([p-p0,v*t1[:,None]-v0,a*t1[:,None]**2+v*t2[:,None]-a0])
class Source:
    def __init__(self,a):
        S=a.scripts;self.joint=j=load(S/'6a65-m12-global-common-cut-position-recovered.py','r262mk_joint')
        self.whole=w=load(S/'6a65-m12-entire-half-cartesian-bvp.py','r262mk_whole');bg=load(S/'6a65-m12-original-tail-background.py','r262mk_bg')
        g=json.loads(a.grid.read_text());a.background_tolerance=g['background_tolerance']
        _,meta,bridge,_,_,self.chart=w.definition(a,j,bg)
        src=j.CommonCutSource(a.data,meta,bridge,a.query_report,a.query_cache)
        load(S/'2ecf-m12-h2-cached-direct-lm-v2.py','r262mk_cache').cache_tail_apply(w.TailQueries,[])
        tail=w.TailQueries(a.query_report,a.query_cache);self.rlist=sorted([(float(Q(k)),k) for k in tail.lookup])
        self.center=Center(j,a.data);self.pos=w.WholePosition(src,self.center.raw,self.chart,tail,j)
        self.S=float(self.chart.S);self.T=float(self.chart.total)
        if sha(a.field)!='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8':raise ValueError('Wrong initial R262 actual field')
        with np.load(a.field) as f:
            self.spl=BSpline(f['unit_knots'],np.pad(f['coefficients'],((3,3),(0,0))),5)
            self.pm=f['planar_modes'];self.hm=f['vertical_modes']
        print('actual seed',self.S,self.T,self.center.ellipse,flush=True)
    def old(self,n,nt,ang,shift):
        ch=self.chart;rawang=ang*(2 if shift else 1);sl=slice(1,None,2) if shift else slice(None)
        N=rawang;tt=np.arange(N)*2*np.pi/N;th=tt[sl];idx=np.arange(n+1)/n
        if shift:idx=np.r_[0,(np.arange(n)+.5)/n,1]
        zpref=idx*self.S/self.T
        J,bb=self.joint.background(self.pos.src,self.center.raw,idx,N,self.pos.prefix_cache)
        xp=np.linspace(1,0,nt+1)
        if shift:xp=np.r_[1,1-(np.arange(nt)+.5)/nt,0]
        vals=np.array([p[0] for p in self.rlist]);ids=np.unique([np.argmin(abs(vals-(float(ch.cuff)+(float(ch.c)-float(ch.cuff))*v))) for v in xp])
        L=[];B=[];Z=[]
        for i in ids[::-1]:
            r=self.joint.ad.base.ld(Q(self.rlist[i][1]))
            if abs(r-ch.c)<1e-17:continue
            p,rho=self.pos.tail_point(r,N);L.append(p);B.append(rho);Z.append(float(ch.inverse_radius(r)))
        z=np.r_[zpref,Z];J=np.concatenate([J,np.array(L)])[:,:,sl,:];bb=np.concatenate([bb,np.array(B)])[:,sl]
        sc,scq=ch.scales(z)
        v=[self.spl(z,j) for j in range(3)];v[2]=v[2]/(self.T*sc[:,None])**2-v[1]*scq[:,None]/(self.T*sc[:,None]**3);v[1]/=self.T*sc[:,None]
        pm,hm=self.pm,self.hm
        for l,(i,j) in enumerate(O):
            a=v[i];p=(a[:,:len(pm)]*(1j*pm)**j)@np.exp(1j*pm[:,None]*th)
            h=(a[:,len(pm):]*(1j*hm)**j)@np.exp(1j*hm[:,None]*th)
            J[:,l]+=np.stack([p.real,p.imag,h.real],axis=-1)
        return z,th,sc,scq,J,bb
class Grid:
    def __init__(self,src,old,eta,nr,modes):
        z,t,H,Hq,self.old,self.bb=old;self.z=z;self.t=t;self.eta=eta;self.T=src.T
        k=np.r_[np.zeros(6),np.arange(1,nr)/nr,np.ones(6)]
        b=BSpline(k,np.eye(len(k)-6)[:,3:-3],5)
        self.B=self.scales([b(z,j) for j in range(3)],H,Hq)
        self.nb=self.B[0].shape[1];channels=[(d,m) for d in range(3) for m in range(1 if d==1 else 0,modes+1)]
        self.na=len(channels);self.ang=np.zeros((3,len(t),self.na,3))
        for a,(d,m) in enumerate(channels):
            c,s=np.cos(m*t),np.sin(m*t)
            for j,row in enumerate(((s,m*c,-m*m*s) if d==1 else (c,-m*s,-m*m*c))):self.ang[j,:,a,d]=row
        self.diff=src.center.difference(t,eta);Hh=self.scales([polynomial(z,j)[:,None] for j in range(3)],H,Hq)
        self.base=self.old+np.stack([p[:,None,:]*self.diff[j] for (i,j),p in zip(O,[Hh[i] for i,j in O])],axis=1)
    def scales(self,v,H,Hq):
        return [v[0],v[1]/(self.T*H[:,None]),v[2]/(self.T*H[:,None])**2-v[1]*Hq[:,None]/(self.T*H[:,None]**3)]
    def field(self,x):
        return self.base+np.stack([np.einsum('na,uad->nud',self.B[i]@x,self.ang[j],optimize=True) for i,j in O],axis=1)
    def metrics(self,x,old=False):
        J=self.old if old else self.field(x);p,v,u,a,b,c=J.swapaxes(0,1);rr=self.bb
        E,F,G=dot(v,v),dot(v,u),dot(u,u);e=E-1;g=G/rr**2-1
        M=abs(e+g)/2+np.hypot((e-g)/2,F/rr);N=np.cross(v,u);ar=np.linalg.norm(N,axis=-1);N/=ar[:,:,None]
        l,m,n=dot(N,a),dot(N,b),dot(N,c);tr=(E*n-2*F*m+G*l)/(ar*ar);K=abs(tr)/2+np.sqrt(np.maximum(0.,tr*tr/4-(l*n-m*m)/(ar*ar)))
        i=np.unravel_index(np.argmax(M),M.shape)
        return dict(metric=float(M[i]),point=[float(self.z[i[0]]),float(self.t[i[1]])],rms=float(np.mean(M*M)**.5),curvature=float(K.max()),areaRatioMin=float((ar/rr).min()),minimumUpperHeight=float(p[...,2].min()),maximumRadius=float(np.hypot(p[...,0],p[...,1]).max()))
    def step(self,x,reg,power):
        J=self.field(x);v,u=J[:,1],J[:,2];rr=self.bb;nvar=x.size;lhs=np.zeros((nvar,nvar));rhs=np.zeros(nvar)
        E,F,G=dot(v,v)-1,dot(v,u)/rr,dot(u,u)/rr**2-1
        M=abs(E+G)/2+np.hypot((E-G)/2,F);w=(.03+(M/(M.max()+1e-30))**power)**.5
        for i in range(len(self.z)):
            ids=np.nonzero(abs(self.B[0][i])+abs(self.B[1][i])>1e-15)[0]
            if not len(ids):continue
            b=self.B[0][i,ids];s=self.B[1][i,ids]
            inner=lambda d,j:np.einsum('uc,uac->ua',d,self.ang[j])
            row=np.stack([2*s[None,:,None]*inner(v[i],0)[:,None,:],np.sqrt(2)/rr[i,:,None,None]*(s[None,:,None]*inner(u[i],0)[:,None,:]+b[None,:,None]*inner(v[i],1)[:,None,:]),2*b[None,:,None]*inner(u[i],1)[:,None,:]/rr[i,:,None,None]**2],axis=1)
            jac=(row*w[i,:,None,None,None]).reshape(3*len(self.t),-1);f=(w[i,:,None]*np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=-1)).ravel()
            ix=(ids[:,None]*self.na+np.arange(self.na)).ravel();lhs[np.ix_(ix,ix)]+=jac.T@jac;rhs[ix]+=jac.T@f
        sc=np.maximum(np.sqrt(np.diag(lhs)),1.e-12);solver=lhs/sc[:,None]/sc[None,:]+reg*np.eye(nvar)
        return (solve(solver,-rhs/sc,assume_a='pos')/sc).reshape(x.shape)
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','data','grid','query-report','query-cache','field','output'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--eta',type=float,required=True);p.add_argument('--spans',type=int,default=12);p.add_argument('--modes',type=int,default=9);p.add_argument('--steps',type=int,default=6);p.add_argument('--parent',type=Path);a=p.parse_args()
    src=Source(a);parent=json.loads(a.parent.read_bytes()) if a.parent else None
    def make(n,m,k,shift):return Grid(src,src.old(n,m,k,shift),a.eta,a.spans,a.modes)
    g=make(74,33,120,False);x=np.zeros((g.nb,g.na))
    if parent:
        if (a.spans,a.modes)!=(parent['spans'],parent['modes']):raise ValueError('Coefficient spaces differ')
        x=np.asarray(parent['xyz'])*(a.eta/parent['eta'])
    obs=[g.metrics(x)];seed=g.metrics(x,True);print('seed',seed,'lift',obs[0],flush=True);hist=[]
    for i in range(a.steps):
        old=obs[-1];ok=False
        for reg in [.000003,.0001,.003,.05]:
            dx=g.step(x,reg,min(4,1+i))
            for scale in (1,.5,.25,.125,.0625):
                v=g.metrics(x+scale*dx)
                if v['metric']<old['metric']*(1-1e-4) and v['curvature']<max(10.15,old['curvature']+.01):
                    hist.append(dict(scale=scale,damping=reg));x+=scale*dx;obs.append(v);ok=True;print('step',i,v,flush=True);break
            if ok:break
        if not ok:break
    results=[]
    for c in [(121,65,192,False),(108,57,233,True)]:
        gg=make(*c);results.append(dict(rows=len(gg.z),angles=len(gg.t),parent=gg.metrics(x,True),actual=gg.metrics(x)));print('observer',c,results[-1],flush=True)
    out=dict(schema='R262-fixed-original-g-full-cuff-true-Minkowski-center-all-integer-physical-XYZ-continuation-v1',entrySHA256=sha(__file__),sourceFieldSHA256=sha(a.field),sourceGridSHA256=sha(a.grid),sourceDataSHA256=sha(a.data),parentSHA256=sha(a.parent) if a.parent else None,eta=a.eta,spans=a.spans,modes=a.modes,xyz=x.tolist(),nativeCentralRadiusPriorNormalization=src.center.raw.a,ellipseSemiaxes=src.center.ellipse,wholeT=float(src.chart.total),prefixS=float(src.chart.S),fixedOriginalG=True,originalSeed=seed,training=obs,accepted=hist,observers=results,exactNonzeroIsometry=False)
    with a.output.open('x') as h:json.dump(out,h,indent=2);h.write('\n')
if __name__=='__main__':main()
