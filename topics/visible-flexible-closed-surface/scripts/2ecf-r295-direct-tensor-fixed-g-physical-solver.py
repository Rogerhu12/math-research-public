#!/usr/bin/env python3
"""Analytic fixed-g and principal-curvature position updates on one literal cubic polar tensor."""
import argparse,importlib.util,json,os,hashlib
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
p=Path(__file__).with_name('2ecf-r295-direct-physical-observe.py');sp=importlib.util.spec_from_file_location('r295direct',p);D=importlib.util.module_from_spec(sp);sp.loader.exec_module(D);O=D.obs
orders=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def axis(grid,n,cap):
    yy=np.clip(grid*n,0,cap);i=np.minimum(yy.astype(int),cap-1);x=yy-i;v=1-x
    return i[:,None]+np.arange(4)[None,:],(np.stack([v**3,3*x**3-6*x*x+4,-3*x**3+3*x*x+3*x+1,x**3],axis=1)/6,np.stack([-v*v/2,1.5*x*x-2*x,-1.5*x*x+x+.5,x*x/2],axis=1)*n,np.stack([v,3*x-2,1-3*x,x],axis=1)*n*n)
def inverse_clock(t,b):
    y=t.copy()
    for _ in range(12):y-=(O.src.clock(y,b)-t)/(1+b*(1-3*y*y)/2)
    return y
def tensorjets(rad,ang,x):
    return np.stack([(rad[i]@x)@ang[j].T for i,j in orders])
def rescale(rad,psi1,psi2,T):
    b,d,h=rad
    return [b,d/psi1[:,None]/T,h/(psi1[:,None]*T)**2-d*psi2[:,None]/(T*T*psi1[:,None]**3)]
class Basis:
    def __init__(self,g,source,radial,angular,n,p):
        with np.load(source) as f:self.data={k:f[k] for k in f.files}
        a=self.data;cp=a['cp'];N=int(a['N']);M=int(a['M']);sd=int(a['seamDen']);b=float(a['clockBias']);self.den=int(a['den']);K=N*(sd-1)//sd;self.T=g.T;self.A=int(a['Aint'])/(36*self.den);self.g=g;self.n=n;self.p=p;self.nr=n-2;self.modes=[p,p,p-1];self.off=np.cumsum([0,*[self.nr*k for k in self.modes]]);self.count=self.off[-1]
        # Finite training coordinate boxes include all physical gradients around the source's old knots and the terminal transition.
        rows,_=g.src.grid(radial,12,True);rows=rows[rows[:,0]<g.T*O.src.clock(1-1/sd,b)-1e-11];ids=np.unique(np.r_[np.linspace(0,len(rows)-1,radial,dtype=int),np.searchsorted(rows[:,0],np.array([.015,.025,.63,.70,.711,.88,.954,1.276]))]);rows=rows[ids];self.s=rows[:,0];self.r0=rows[:,1,None];t=self.s/g.T;y=inverse_clock(t,b);xi=np.linspace(0,1,angular);self.theta=xi*np.pi/2;ri,rr=axis(y,N,K);ai,aa=axis(xi,M,M);psi1=1+b*(1-3*y*y)/2;psi2=-3*b*y;rr=rescale(rr,psi1,psi2,g.T);aa=[z*(2/np.pi)**j for j,z in enumerate(aa)]
        local=cp[ri[:,None,:,None],ai[None,:,None,:]]/self.den
        self.base=[]
        for i,j in orders:self.base.append(np.einsum('nulkc,nl,uk->cnu',local,rr[i],aa[j],optimize=True))
        self.base=np.stack(self.base,axis=1);self.base[2]*=np.pi/2;self.rc=[];self.ac=[];self.rb=[];self.ab=[]
        fint=(np.arange(K+4)-1)/N;fa=(np.arange(M+4)-1)/M;e=.998;kn=np.r_[np.zeros(3),np.linspace(0,e,n+1),np.full(3,e)];bs=BSpline(kn,np.eye(n+3),3,extrapolate=False);fphys=O.src.clock(fint,b)
        valid=(fint>=0)&(fphys<e);raw=np.zeros((K+4,n+3));raw[valid]=bs(fphys[valid])
        for c,mc in enumerate(self.modes):
            if c==1:
                C=np.column_stack([raw[:,1]+3*raw[:,2],raw[:,3:n]]);C[1]=0;C[0]=-C[2]
            else:
                C=raw[:,2:n].copy();C[1]=-C[2]/2;C[0]=C[2]
            f=np.arange(mc)+(c==2);A=(np.sin if c==2 else np.cos)(np.pi*fa[:,None]*f);A[[1,M+1]]=0 if c==2 else A[[1,M+1]]
            self.rc.append(C);self.ac.append(A);self.rb.append([np.einsum('nl,nlk->nk',z,C[ri]) for z in rr]);self.ab.append([np.einsum('ul,ulk->uk',z,A[ai])*(np.pi/2 if c==2 else 1) for z in aa])
    def split(self,x):return [x[self.off[c]:self.off[c+1]].reshape(self.nr,self.modes[c]) for c in range(3)]
    def form(self,x):
        X=self.split(x);return self.base+np.array([tensorjets(self.rb[c],self.ab[c],X[c]) for c in range(3)])
    def geometry(self,x):
        P=self.form(x);R,z,U=P;rv,rs,rt,rss,rst,rtt=R;zz,zs,zt,zss,zst,ztt=z;_,us,ut,*_=U
        h=-us/ut;k=1/(self.r0*ut);A=np.stack([rt,rv,zt],-1);Vs=np.stack([rs,0*rs,zs],-1);V=Vs+h[...,None]*A;W=k[...,None]*A
        E=(V*V).sum(-1)-1;F=(W*V).sum(-1);H=(W*W).sum(-1)-1;pk=abs(E+H)/2+np.hypot((E-H)/2,F)
        zero=np.zeros_like(rv);pack=lambda q0,q1,q2:np.stack([q0,q1,q2],axis=-1)
        J=np.stack([pack(rv,zero,zz),Vs,A,pack(rss,zero,zss),pack(rst,rs,zst),pack(rtt-rv,2*rt,ztt)],axis=1)
        K,cov=O.G.F.v.curve(J);Y=rv*np.sin(self.theta);X=rv*np.cos(self.theta);dist=np.sqrt(X*X+(Y-self.A)**2+zz*zz);idx=np.unravel_index(np.argmax(pk),pk.shape);ik=np.unravel_index(np.argmax(abs(K)),K.shape)
        stats=dict(metric=float(pk[idx]),curvature=float(abs(K[ik])),areaRatioMin=float(np.sqrt(np.maximum((E+1)*(H+1)-F*F,0)).min()),maxY=float(Y.max()),minHeld=float(dist.min()),maxNorm=float(np.hypot(rv,zz).max()),clockMinimum=float(ut.min()),metricPoint=[float(self.s[idx[0]]),float(U[0][idx])],curvaturePoint=[float(self.s[ik[0]]),float(U[0][ik])])
        return (R,z,U,h,k,A,V,W,E,F,H,pk,K,cov,Y,dist),stats
    def assemble(self,x,mu,reg,power,trust=0.):
        (R,z,U,h,k,A,V,W,E,F,H,pk,K,cov,Y,dist),st=self.geometry(x);C=self.count;mat=np.zeros((C,C));rhs=np.zeros(C);ks=max(.3,abs(K).max()-9.6);pmax=pk.max();na=pk.shape[1];root2=np.sqrt(2);ssrow=[];sscol=[];ssval=[];limits=[]
        # Matrix columns are true six-jets of local spline coefficients. Rows are evaluated on the original fixed target.
        for i in range(len(self.s)):
            blocks=[];colids=[]
            for c in range(3):
                rb=self.rb[c];ids=np.flatnonzero(abs(rb[0][i])+abs(rb[1][i])+abs(rb[2][i])>1e-14)
                D=np.stack([(rb[a][i,ids,None,None]*self.ab[c][b][None,:,:]).transpose(1,0,2).reshape(na,-1) for a,b in orders]);p,ds,dt,dss,dst,dtt=D
                if c<2:
                    axis=0 if c==0 else 2;dv=ds+h[i,:,None]*dt;dw=k[i,:,None]*dt
                    dE=2*V[i,:,axis,None]*dv;dF=root2*(W[i,:,axis,None]*dv+V[i,:,axis,None]*dw);dH=2*W[i,:,axis,None]*dw
                    if c==0:
                        dE+=2*V[i,:,1,None]*h[i,:,None]*p;dF+=root2*(W[i,:,1,None]*h[i,:,None]+V[i,:,1,None]*k[i,:,None])*p;dH+=2*W[i,:,1,None]*k[i,:,None]*p
                    cs,ct,css,cst,ctt=[q[i] for q in cov];dK=cs[:,axis,None]*ds+ct[:,axis,None]*dt+css[:,axis,None]*dss+cst[:,axis,None]*dst+ctt[:,axis,None]*dtt
                    if c==0:dK+=(ct[:,1]-ctt[:,0])[:,None]*p+cst[:,1,None]*ds+2*ctt[:,1,None]*dt
                    dy=(np.sin(self.theta)[:,None]*p if c==0 else p*0);dd=((R[0,i]-self.A*np.sin(self.theta))/dist[i] if c==0 else z[0,i]/dist[i])[:,None]*p
                else:
                    ut=U[2,i,:,None];dh=-(ds+h[i,:,None]*dt)/ut;dk=-k[i,:,None]*dt/ut;va=(V[i]*A[i]).sum(-1)[:,None];wa=(W[i]*A[i]).sum(-1)[:,None]
                    dE=2*va*dh;dF=root2*(wa*dh+va*dk);dH=2*wa*dk;dK=p*0;dy=p*0;dd=p*0
                blocks.append(np.stack([dE,dF,dH,dK,dy,dd],axis=1));colids.extend((self.off[c]+ids[:,None]*self.modes[c]+np.arange(self.modes[c])).ravel())
            if not colids:continue
            JJ=np.concatenate(blocks,axis=2);r=np.stack([E[i],root2*F[i],H[i],np.sign(K[i])*np.maximum(abs(K[i])-9.6,0),np.maximum(Y[i]-.8937,0),np.minimum(dist[i]-.648,0)],axis=1)
            if trust:
                cols=np.array(colids);Krow=K[i];scale=np.hypot((E[i]-H[i])/2,F[i]);ix=(E[i]-H[i])/2/np.maximum(scale,1e-16);off=F[i]/np.maximum(scale,1e-16)
                def put(row,rhs,target=-1):
                    rr=len(limits);nz=np.flatnonzero(abs(row)>1e-13);ssrow.extend([rr]*len(nz));sscol.extend(cols[nz]);ssval.extend(row[nz])
                    if target>=0:ssrow.append(rr);sscol.append(C+target);ssval.append(-1.)
                    limits.append(rhs)
                for sign in (-1,1):
                    vals=(E[i]+H[i])/2+sign*scale
                    for k0 in set(np.r_[np.argmin(vals),np.argmax(vals),np.flatnonzero(abs(vals)>.80*pmax)[::3]]):
                        v=(1+sign*ix[k0])/2*JJ[k0,0]+sign*off[k0]/root2*JJ[k0,1]+(1-sign*ix[k0])/2*JJ[k0,2]
                        for side in (-1,1):put(side*v,-side*vals[k0],0)
                for k0 in set(np.r_[np.argmin(Krow),np.argmax(Krow),np.flatnonzero(abs(Krow)>9.0)[::4]]):
                    for side in (-1,1):put(side*JJ[k0,3],9.6-side*Krow[k0],1)
                for k0 in set(np.r_[np.argmax(Y[i]),np.flatnonzero(Y[i]>.8930)[::4]]):put(JJ[k0,4],.89425-Y[i,k0])
                for k0 in set(np.r_[np.argmin(dist[i]),np.flatnonzero(dist[i]<.655)[::3]]):put(-JJ[k0,5],dist[i,k0]-.646)
                continue
            w=(.03+(pk[i]/pmax)**power)**.5;weights=np.stack([w,w,w,mu*(.15+(np.maximum(abs(K[i])-9.6,0)/ks)**power)**.5*(abs(K[i])>9.6),5.0*(Y[i]>.8928),3.*(dist[i]<.65)],axis=1)
            J=(weights[:,:,None]*JJ).reshape(-1,len(colids));rr=(r*weights).ravel();ix=np.ix_(colids,colids);mat[ix]+=J.T@J;rhs[colids]+=J.T@rr
        if trust:
            n=len(limits);A=coo_matrix((ssval,(ssrow,sscol)),shape=(n,C+2)).tocsr();wt=np.concatenate([np.tile(1/(1+.06*np.arange(mc)**1.6),self.nr) for mc in self.modes]);bounds=[(-trust*w,trust*w) for w in wt]+[(0,None),(0,None)]
            opt=linprog(np.r_[np.zeros(C),1.,mu],A_ub=A,b_ub=np.array(limits),bounds=bounds,method='highs-ipm',options=dict(time_limit=45.));print('LP',opt.status,n,None if opt.x is None else opt.x[-2:].tolist(),flush=True)
            return None if not opt.success else opt.x[:C]
        sc=np.maximum(np.sqrt(np.diag(mat)),.002);dv=solve(mat/sc[:,None]/sc[None,:]+reg*np.eye(C),-rhs/sc,assume_a='pos')/sc;return dv
    def archive(self,x,path):
        C=self.data['cp'].copy();X=self.split(x)
        for c in range(3):C[...,c]+=np.rint((self.rc[c]@X[c]@self.ac[c].T)*self.den).astype(np.int64)
        # Enforce exact parity around the central and quarter-circle endpoints after the final integer rounding.
        C[0,:,0]=C[2,:,0];C[0,:,1]=-C[2,:,1];C[0,:,2]=C[2,:,2];M=int(self.data['M'])
        C[:,0]=C[:,2];C[:,0,2]*=-1;C[:,M+2]=C[:,M];C[:,M+2,2]=2*self.den-C[:,M+2,2];C[:,M+3]=C[:,M-1];C[:,M+3,2]=2*self.den-C[:,M+3,2]
        b=O.src.bernstein(C);d=dict(self.data,cp=C,Aint=int(b[0,0,0,0,0]));np.savez_compressed(path,**d)
def main():
    p=O.src.template(argparse.ArgumentParser())
    for k in ('source','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--trust',type=float,default=0.);p.add_argument('--radial',type=int,default=235);p.add_argument('--angular',type=int,default=85);p.add_argument('--space',type=int,default=32);p.add_argument('--modes',type=int,default=8);p.add_argument('--steps',type=int,default=12);p.add_argument('--mu',type=float,default=.035);a=p.parse_args();g=O.src.load(a);bn=Basis(g,a.source,a.radial,a.angular,a.space,a.modes);x=np.zeros(bn.count);history=[];steps=[];base=bn.geometry(x)[1];merit=lambda q:q['metric']+a.mu*max(0,q['curvature']-9.6)+8*max(0,q['maxY']-.8939)+3*max(0,.645-q['minHeld']);print('start',base,flush=True)
    for it in range(a.steps):
        old=bn.geometry(x)[1];history.append(old);accepted=None
        for reg,pw in (((1,1),(.35,1),(.12,1)) if a.trust else ((.006,4),(.055,2),(.001,6))):
            dx=bn.assemble(x,a.mu,reg,pw,a.trust*reg)
            if dx is None:continue
            for h in (1,.5,.25,.125,.0625,.03125,.015625):
                y=x+h*dx;q=bn.geometry(y)[1]
                if q['clockMinimum']>.15 and q['maxY']<.8945 and q['minHeld']>.644 and merit(q)<merit(old)*(1-2e-6):
                    if accepted is None or merit(q)<accepted[0]:accepted=(merit(q),y,q,reg,h)
            if accepted is not None:break
        if accepted is None:break
        _,x,q,reg,h=accepted;steps.append(dict(step=h,reg=reg));print('accepted',it,q,flush=True);bn.archive(x,a.out.with_suffix('.npz'))
    bn.archive(x,a.out.with_suffix('.npz'));q=bn.geometry(x)[1];result=dict(schema='direct-polar-physical-closed-shape-position-and-clock-steps',sourceSHA256=sha(a.source),outputSHA256=sha(a.out.with_suffix('.npz')),entrySHA256=sha(__file__),free=int(bn.count),radialCount=len(bn.s),quarterAngles=len(bn.theta),history=history,steps=steps,final=q,coefficients=x.tolist())
    with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
