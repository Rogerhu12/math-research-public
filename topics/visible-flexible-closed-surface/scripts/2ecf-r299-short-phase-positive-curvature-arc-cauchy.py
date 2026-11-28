#!/usr/bin/env python3
"""True short-phase moving circular patch on a closed unit-speed convex planar inlet and its full D2 Gauss--Codazzi ramp."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
from types import SimpleNamespace
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import betainc
from scipy import fft
def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
class Inlet:
    half=.5;blend=.5;low=.2
    def __init__(self):
        self.high=(np.pi-self.low*(2*self.half+self.blend))/(np.pi-2*self.half-self.blend);self.nodes,self.weights=np.polynomial.legendre.leggauss(30);self.A,self.B=self.integrals(np.array([np.pi/2]))[0]
    def qangle(self,u):
        x=np.clip((u-self.half)/self.blend,0,1);S=betainc(8,8,x);I=x*S-.5*betainc(9,8,x);return self.low*u+(self.high-self.low)*(self.blend*I+np.maximum(u-self.half-self.blend,0))
    def k(self,u):
        a=abs((u+np.pi/2)%np.pi-np.pi/2);return self.low+(self.high-self.low)*betainc(8,8,np.clip((a-self.half)/self.blend,0,1))
    def integrals(self,a):
        vals=np.zeros((len(a),2))
        for lo,hi in ((0.,self.half),(self.half,self.half+self.blend),(self.half+self.blend,np.pi/2)):
            h=np.clip(a-lo,0,hi-lo);t=lo+h[:,None]*(1+self.nodes)/2;beta=self.qangle(t);vals[:,0]+=h/2*(np.sin(beta)@self.weights);vals[:,1]+=h/2*(np.cos(beta)@self.weights)
        return vals
    def geometry(self,u):
        u=np.asarray(u,dtype=float);q=np.floor((u+np.pi/2)/np.pi).astype(int);v=u-q*np.pi;d=self.integrals(abs(v));sgn=np.where(q%2,-1.,1.);X=np.stack([sgn*(self.A-d[:,0]),sgn*np.sign(v)*d[:,1],0*u],axis=1);b=np.sign(v)*self.qangle(abs(v))+q*np.pi
        T=np.stack([-np.sin(b),np.cos(b),0*u],axis=1);W=np.stack([np.cos(b),np.sin(b),0*u],axis=1);return X,T,W
class Candidate:
    def __init__(self,length,v):self.length=length;self.v=v;self.ellipse=SimpleNamespace(A=1.,B=1.,a0=1.)
    def profile(self,s):
        s=np.asarray(s);t=np.clip(s/self.length,0,1);v=self.v;S=126*t**5-420*t**6+540*t**7-315*t**8+70*t**9;J=21*t**6-60*t**7+67.5*t**8-35*t**9+7*t**10
        return 1+v*self.length*J+v*np.maximum(s-self.length,0),v*S,(v/self.length)*630*t**4*(1-t)**4
def hermite(nodes,P,s,c,u,G,fc):
    i=min(len(nodes)-2,int(np.searchsorted(nodes,s,side='right')-1));h=nodes[i+1]-nodes[i];x=(s-nodes[i])/h;nd=len(u);val=np.zeros((6,nd,3));waves=fc
    def angular(idx,d):
        if idx==0:
            X,V,NN=G.geometry(u);kk=G.k(u);ex=np.zeros_like(X);ex[:,2]=1
            if d==0:X[:,2]+=c;return [X,ex,np.zeros_like(X)]
            if d==1:return [V,np.zeros_like(X),np.zeros_like(X)]
            return [-kk[:,None]*NN,np.zeros_like(X),np.zeros_like(X)]
        co=P[idx]*(1j*waves[None,:,None])**d
        return list(fft.irfft(co,n=nd,axis=1,norm='forward'))
    for j in range(3):
        a,b,l=angular(i,j);p,v,k=angular(i+1,j);a,b,l=a,h*b,h*h*l/2;r=p-a-b-l;rr=h*v-b-2*l;rrr=h*h*k-2*l;poly=np.stack([a,b,l,10*r-4*rr+rrr/2,-15*r+7*rr-rrr,6*r-3*rr+rrr/2])
        def ev(order):
            import math
            return sum(poly[k]*x**(k-order)*math.factorial(k)/math.factorial(k-order) for k in range(order,6))/h**order
        for order,index in ([(0,0),(1,1),(2,3)] if j==0 else ([(0,2),(1,4)] if j==1 else [(0,5)])):val[index]=ev(order)
    return val
def main():
    p=argparse.ArgumentParser();p.add_argument('--scripts',type=Path,required=True);p.add_argument('--modes',type=int,default=127);p.add_argument('--nodes',type=int,default=65);p.add_argument('--length',type=float,default=.06);p.add_argument('--speed',type=float,default=.006);p.add_argument('--out',type=Path,required=True);a=p.parse_args();H=load(a.scripts/'fd2d-gc-ellipse-hybrid-flow.py','r299_actual_hybrid');g=Inlet();c=.2;C=Candidate(a.length,a.speed)
    class Actual(H.Hybrid):
        def initial(self):
            u=np.asarray(self.theta,float);X,T,N=g.geometry(u);v=np.zeros((self.work,14));v[:,0]=g.k(u);v[:,2:5]=X;v[:,4]+=c;v[:,7]=1;v[:,8:11]=T;v[:,11:14]=-N;return self.encode(v)
        def rhs(self,s,state):
            self.calls+=1;v=self.decode(state);n,m=v[:,:2].T;assert np.min(n)>0;f,fp,fpp=(a[0] for a in C.profile([s]));l=(m*m-fpp/f)/n;lu,mu=self.derivative(np.stack([l,m],axis=1)).T;N=v[:,11:14];e1=v[:,5:8];e2=v[:,8:11];V=np.zeros_like(v);V[:,0]=mu/f+fp/f*(l-n);V[:,1]=lu/f-2*fp/f*m;V[:,2:5]=e1;V[:,5:8]=l[:,None]*N;V[:,8:11]=m[:,None]*N;V[:,11:14]=-l[:,None]*e1-m[:,None]*e2;return self.encode(V)
    flow=Actual(C,a.modes,2,60000);init=flow.initial();mesh=np.linspace(0,a.length,a.nodes);sol=solve_ivp(flow.rhs,(0,a.length),init,method='DOP853',rtol=2e-12,atol=2e-14/(1+flow.active_wave)**2,t_eval=mesh,max_step=a.length/75);assert sol.success and sol.t[-1]==a.length
    P=[];mins=[]
    for t,v in zip(sol.t,sol.y.T):
        F=flow.decode(v);n,m=F[:,:2].T;f,fp,fpp=(a[0] for a in C.profile([t]));l=(m*m-fpp/f)/n;mins.append(float(n.min()));J=np.stack([F[:,2:5],F[:,5:8],l[:,None]*F[:,11:14]]);P.append(fft.rfft(np.asarray(J,float),axis=1,norm='forward'))
    P=np.array(P);w=np.arange(P.shape[2]);np.savez_compressed(a.out.with_suffix('.npz'),radialNodes=mesh,portPVA=P,terminalShape=np.asarray(flow.decode(sol.y[:,-1])[:,:2],float))
    nd=2*flow.work+16;u=np.arange(nd)*2*np.pi/nd;qs=(1-np.sqrt(3/5),1.,1+np.sqrt(3/5));out=[]
    for jump in ([4,2,1] if (a.nodes-1)%4==0 else [1]):
        nodes=mesh[::jump];pp=P[::jump];maximum=ks=0.;at=None
        for i in range(len(nodes)-1):
            for xx in qs:
                s0=nodes[i]+(nodes[i+1]-nodes[i])*xx/2;J=hermite(nodes,pp,s0,c,u,g,w);p0,vs,vu,vss,vsu,vuu=J;f=C.profile([s0])[0][0];E=(vs*vs).sum(-1);F=(vs*vu).sum(-1);B=(vu*vu).sum(-1);N=np.cross(vs,vu);det=(N*N).sum(-1);N/=np.sqrt(det)[:,None];L=(N*vss).sum(-1);M=(N*vsu).sum(-1);Q=(N*vuu).sum(-1);tr=(B*L-2*F*M+E*Q)/det;K=(L*Q-M*M)/det;curv=abs(tr)/2+np.sqrt(np.maximum(tr*tr/4-K,0));ks=max(ks,curv.max());AA=E-1;CC=B/f**2-1;op=abs(AA+CC)/2+np.hypot((AA-CC)/2,F/f);j=op.argmax()
                if op[j]>maximum:maximum=float(op[j]);at=[s0,u[j]]
        out.append(dict(radialNodes=len(nodes),locationsPerCell=3,angles=nd,metric=maximum,curvature=ks,worst=at))
    utest=np.linspace(.05,.45,137);X,T,N=g.geometry(utest);eta=.5;XX,_,_=g.geometry(utest-eta);rot=lambda x,v:x@np.array([[np.cos(v),np.sin(v),0],[-np.sin(v),np.cos(v),0],[0,0,1.]])
    ctr=np.array([g.A-5,0,0]);actual=rot(XX,eta);formula=rot(ctr+rot(X-ctr,-eta/5),eta);end=flow.decode(sol.y[:,-1]);report=dict(schema='R299-short-partial-period-positive-circular-central-arc-closed-unit-speed-Cauchy-data',entrySHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),hybridSHA=hashlib.sha256((a.scripts/'fd2d-gc-ellipse-hybrid-flow.py').read_bytes()).hexdigest(),modes=a.modes,angular=flow.work,rampLength=a.length,rampSpeed=a.speed,centralHalfLength=c,A=g.A,B=g.B,kappaPlateau=g.low,kappaUpper=g.high,phase=eta,materialPatch=[.05,.45],rigidAngle=4*eta/5,rigidPositionResidual=float(np.max(np.linalg.norm(actual-formula,axis=-1))),fullCauchyExit=dict(success=sol.success,rhs=sol.nfev,minRecordedN=min(mins),terminalN=[float(end[:,0].min()),float(end[:,0].max())],terminalMAbs=float(abs(end[:,1]).max()),rawFile=str(a.out.with_suffix('.npz').name),rawSHA=hashlib.sha256(a.out.with_suffix('.npz').read_bytes()).hexdigest()),physicalHermiteObservers=out)
    hb=np.linspace(1.5+.01,np.pi-1-.01,131);hx,_,_=g.geometry(hb);hy,_,_=g.geometry(hb-eta);hc=np.array([0.,g.B-1/g.high,0.]);hobs=rot(hy,eta);hcalc=rot(hc+rot(hx-hc,-g.high*eta),eta)
    report['secondRigidMaterialPatch']={'interval':[1.5,np.pi-1],'rigidAngle':(1-g.high)*eta,'relativeRigidAngle':(g.high-g.low)*eta,'testPositionResidual':float(np.max(np.linalg.norm(hobs-hcalc,axis=-1)))}
    txt=json.dumps(report,indent=2)+'\n'
    with a.out.open('x') as f:f.write(txt)
    print(report,flush=True)
if __name__=='__main__':main()
