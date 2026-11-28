#!/usr/bin/env python3
"""Exact angular-target parametrization of each full D3 spatial ring in two free scalar fields."""
import numpy as np
from scipy.interpolate import CubicSpline

def complex_xy(J):return J[...,0]+1j*J[...,1]
def realdot(z,w):return np.real(np.conj(z)*w)
def radial_square(f,f1,f2):return (f*f,2*f*f1,2*(f1*f1+f*f2))
def clock_bases(u,sp,spp,m):
    kh=3*np.arange(m+1)
    z=np.exp(1j*u[:,None]*kh);k=kh[None,:]
    h=[z.real,-k*z.imag*sp[:,None],-k*k*z.real*sp[:,None]**2-k*z.imag*spp[:,None]]
    a=[z[:,1:].imag,(k*z.real*sp[:,None])[:,1:],(-k*k*z.imag*sp[:,None]**2+k*z.real*spp[:,None])[:,1:]]
    return h,a

class Rings:
    def __init__(self,src,api,a,kn,metric,q,theta,parent,arms):
        self.src=src;self.a=a;self.q=q;self.th=theta;self.spline=api.Bvals(q,kn)
        self.nh=arms+1;self.nm=2*arms+1;self.shape=(self.spline[0].shape[1],self.nm)
        self.P=parent;self.xy=complex_xy(parent)
        self.z=parent[...,2]
        if min(abs(self.xy[:,2]).ravel())<=1e-10:raise ValueError('Parent rings have a vertical horizontal-angle degeneracy')
        P=2*np.pi/3;R=np.exp(1j*P)
        I=np.eye(len(theta))
        if theta[0]!=0 or abs(theta[-1]-P)>1e-14:raise ValueError('Need one full native D3 sector')
        ext=np.r_[theta[:-1]-P,theta,theta[1:]+P]
        bank=CubicSpline(ext,np.concatenate((I[:-1]/R,I,R*I[1:])),axis=0)
        H=bank.antiderivative();z=H(theta)-H(0)
        self.K=z+z[-1]/(R-1)
        # Physical derivatives of P_qq at all source points, in their actual
        # quasiperiodic angular charts. Their numerical use is confined to curvature.
        self.xyqqt=self.xy[:,3]@bank(theta,1).T
        scalar=CubicSpline(ext,np.concatenate((I[:-1],I,I[1:])),axis=0)
        self.zqqt=self.z[:,3]@scalar(theta,1).T
        v=np.asarray(src.center.base.derivative(theta,1),float);vv=np.asarray(src.center.base.derivative(theta,2),float)
        sp=np.linalg.norm(v,axis=1);spp=np.sum(v*vv,axis=-1)/sp;self.u=src.center.arc(theta)
        self.H,self.A=clock_bases(self.u,sp,spp,arms)
        b=a.full_sleeve;w=a.full_gate
        f,f1,f2=[np.asarray(t,float) for t in src.pos.src.metric.profile(q)]
        g,g1,g2=api.step(q,b,b+w)
        h=1+g*(f-1);h1=g1*(f-1)+g*f1;h2=g2*(f-1)+2*g1*f1+g*f2
        M=api.Bvals(q,np.asarray(metric['knots']));W,W1,W2=[v@np.asarray(metric['w']) for v in M];W+=1
        self.Q=1+M[0]@np.asarray(metric['q'])
        sq,s1,s2=radial_square(h,h1,h2)
        self.b2=(W*sq)[:,None]*sp[None]**2
        target1=(W1*sq+W*s1)[:,None]*sp[None]**2
        target2=(W2*sq+2*W1*s1+W*s2)[:,None]*sp[None]**2
        targett=(W*sq)[:,None]*(2*sp*spp)[None]
        V=self.P[:,2];A=self.P[:,4]
        ac=np.einsum('rtv,rtv->rt',V,V);ac1=2*np.einsum('rtv,rtv->rt',V,A)
        ac2=2*(np.sum(A*A,axis=-1)+realdot(self.xy[:,2],self.xyqqt)+self.z[:,2]*self.zqqt)
        act=2*np.einsum('rtv,rtv->rt',V,self.P[:,5])
        blend,b1,b2=api.step(q,a.lift_end,src.S)
        strength=a.angular_strength
        g=1-strength*(1-blend[:,None]);g1=strength*b1[:,None];g2=strength*b2[:,None]
        self.B2=self.b2+g*(ac-self.b2)
        self.B2q=(1-g)*target1+g*ac1+g1*(ac-self.b2)
        self.B2qq=(1-g)*target2+g*ac2+2*g1*(ac1-target1)+g2*(ac-self.b2)
        self.B2t=(1-g)*targett+g*act
        self.B0=self.xy[:,2]/abs(self.xy[:,2])
        self.oq=np.imag(self.xy[:,4]/self.xy[:,2])
        self.ot=np.imag(self.xy[:,5]/self.xy[:,2])
        self.oqq=np.imag(self.xyqqt/self.xy[:,2]-(self.xy[:,4]/self.xy[:,2])**2)
    def actions(self,X):
        w=self.nh;B,D,DD=self.spline;h,ang=self.H,self.A
        z=[];ph=[]
        for j,(r,d) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
            z.append(self.z[:,j]+([B,D,DD][r]@X[:,:w])@h[d].T)
            ph.append(([B,D,DD][r]@X[:,w:])@ang[d].T)
        return z,ph,self.zqqt+(DD@X[:,:w])@h[1].T
    def state(self,X,geom=False):
        z,p,zqqt=self.actions(X)
        h2=self.B2-z[2]**2
        if h2.min()<=1e-12:raise ValueError('Requested angular metric shorter than actual vertical angular derivative')
        h=np.sqrt(h2);hq=(self.B2q/2-z[2]*z[4])/h
        t=self.B0*np.exp(1j*p[0]);oq=self.oq+p[1]
        U=h*t
        Q=self.xy[:,1]+((hq+1j*h*oq)*t-self.xy[:,4])@self.K.T
        E=abs(Q)**2+z[1]**2;F=realdot(Q,U)+z[1]*z[2]
        norm=np.sqrt(self.Q[:,None]*self.b2)
        es=E/self.Q[:,None]-1;fs=F/norm;gs=self.B2/self.b2-1
        err=.5*abs(es+gs)+np.hypot(.5*(es-gs),fs)
        if not geom:return z,p,t,h,hq,oq,U,Q,es,fs,gs,err,norm
        xy=self.xy[:,0]+(U-self.xy[:,2])@self.K.T
        hqq=(self.B2qq/2-z[4]**2-z[2]*zqqt-hq**2)/h
        qt=((hq+1j*h*oq)*t)
        qq=self.xy[:,3]+(((hqq-h*oq**2)+1j*(2*hq*oq+h*(self.oqq+p[3])))*t-self.xyqqt)@self.K.T
        htt=(self.B2t/2-z[2]*z[5])/h
        tt=(htt+1j*h*(self.ot+p[2]))*t
        cols=np.stack([np.stack((v.real,v.imag,b),axis=-1) for v,b in zip((xy,Q,U,qq,qt,tt),z)],axis=1)
        return cols,err,h
    def report(self,X,micro):
        J,err,h=self.state(X,True);cur,area=micro.curvature(J);N=np.cross(J[:,2],J[:,1])/np.sqrt(area)[...,None]
        sig=np.sum(J[:,0]*N,axis=-1);ix=np.unravel_index(err.argmax(),err.shape);iy=np.unravel_index(cur.argmax(),cur.shape)
        return dict(peak=float(err[ix]),rms=float(np.mean(err**2)**.5),curvature=float(cur[iy]),minimumHorizontalAngularSpeed=float(h.min()),minimumSupport=float(sig.min()),minimumArea=float(np.sqrt(area).min()),minimumZs=float(J[:,1,:,2].min()),angularComponent=float(np.max(abs(self.B2/self.b2-1))),
                    worstMetric=[float(self.q[ix[0]]),float(self.th[ix[1]]),float(self.u[ix[1]])],worstCurvature=[float(self.q[iy[0]]),float(self.th[iy[1]]),float(self.u[iy[1]])])

def assemble(model,X,power):
    z,p,T,h,hq,oq,U,Q,e,f,g,err,norm=model.state(X)
    B,D=model.spline[:2];nr,nm=X.shape;w=model.nh
    C0=np.zeros((len(model.th),nm));C1=C0.copy();S0=C0.copy()
    C0[:,:w]=model.H[0];C1[:,:w]=model.H[1];S0[:,w:]=model.A[0]
    blocks=np.zeros((6,nr,nm,nm));gradient=np.zeros((nr,nm))
    wt=np.maximum(.04,err/max(1e-28,err.max()))**power/np.sqrt(err.size)
    for i in range(len(B)):
        use=np.flatnonzero((B[i]!=0)|(D[i]!=0))
        if not len(use):continue
        if use[-1]-use[0]>5:raise ValueError('Expected local physical quintics')
        t=T[i,:,None];v=h[i,:,None];a=hq[i,:,None];o=oq[i,:,None]
        zt=z[2][i,:,None];zqt=z[4][i,:,None];zq=z[1][i,:,None]
        dh=-zt*C1/v
        hb=-(zqt*C1+a*dh)/v
        hd=-zt*C1/v
        qu=model.K@(t*(hb+1j*dh*o+1j*S0*(a+1j*v*o)))
        qd=model.K@(t*(hd+1j*v*S0))
        ub=t*(dh+1j*v*S0)
        P=Q[i,:,None];V=U[i,:,None];ws=wt[i,:,None]
        Eb=ws*(2/model.Q[i])*realdot(P,qu)
        Ed=ws*(2/model.Q[i])*(realdot(P,qd)+zq*C0)
        Fb=ws*np.sqrt(2)/norm[i,:,None]*(realdot(V,qu)+realdot(P,ub)+zq*C1)
        Fd=ws*np.sqrt(2)/norm[i,:,None]*(realdot(V,qd)+zt*C0)
        bb=Eb.T@Eb+Fb.T@Fb;dd=Ed.T@Ed+Fd.T@Fd;db=Ed.T@Eb+Fd.T@Fb
        er=wt[i]*e[i];fr=wt[i]*np.sqrt(2)*f[i]
        gb=Eb.T@er+Fb.T@fr;gd=Ed.T@er+Fd.T@fr
        for j in use:
            gradient[j]+=B[i,j]*gb+D[i,j]*gd
            for k in use:
                if k<j:continue
                blocks[k-j,j]+=B[i,k]*B[i,j]*bb+D[i,k]*D[i,j]*dd+D[i,k]*B[i,j]*db+B[i,k]*D[i,j]*db.T
    ab=np.zeros((6*nm,nr*nm));rr,cc=np.indices((nm,nm))
    for k in range(6):
        off=k*nm+rr-cc;mask=off>=0
        for j in range(nr-k):ab[off[mask],j*nm+cc[mask]]=blocks[k,j][mask]
    return ab,gradient.ravel(),wt
