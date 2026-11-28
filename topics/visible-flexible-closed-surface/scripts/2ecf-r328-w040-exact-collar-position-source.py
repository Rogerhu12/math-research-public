#!/usr/bin/env python3
"""Evaluate the full periodic W040 collar of R328, from its true cylindrical trace to x=4/25."""
import argparse,hashlib,importlib.util,json,os,sys,traceback
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np

L=4/25
C=.350
ANCHOR=np.pi/3
ORDERS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
PHYSICAL='29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def phys_module(p):
    if sha(p)!=PHYSICAL:raise ValueError('Require the actual R321 W040 two-moment source')
    sp=importlib.util.spec_from_file_location('accurate_w040_material_curve',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def metric(x):
    f=1+10*x**4
    return f,40*x**3/f,120*x*x/f
def own_central(geo,u):
    p,beta,k=geo.at(np.asarray(u),ANCHOR);n=np.stack((np.cos(beta),np.sin(beta),np.zeros_like(beta)),axis=-1)
    T=np.stack((-n[:,1],n[:,0],0*beta),axis=-1)
    return np.stack((p.real,p.imag,0*beta),axis=-1),T,-k[:,None]*n,k
def collar_flow(geo,n,nr,substeps):
    theta=2*np.pi*np.arange(n)/n;gamma,T,_,k=own_central(geo,theta)
    Y=np.zeros((n,14));Y[:,1]=1/k;Y[:,2:5]=gamma;Y[:,4]=C;Y[:,7]=1;Y[:,8:11]=T
    Y[:,11:14]=np.cross(Y[:,5:8],T)
    modes=np.arange(n//2+1);der=(1j*modes)*(modes<=n//3)
    def rhs(x,Y):
        b,q=Y[:,0],Y[:,1];f,c,mu2=metric(x)
        if np.min(q)<=0 or not np.all(np.isfinite(q)):raise ArithmeticError('Codazzi positive normal branch failed')
        du=np.fft.irfft(np.fft.rfft(Y[:,:2],axis=0)*der[:,None],n=n,axis=0)
        bu,qu=du.T
        L0=(b*b-mu2*q*q)/q;M=b/q;e1=Y[:,5:8];e2=Y[:,8:11];normal=Y[:,11:14]
        dy=np.empty_like(Y)
        dy[:,0]=(b*bu-mu2*q*qu)/f-c*b*(1+b*b-mu2*q*q)
        dy[:,1]=(b*qu-q*bu)/f+c*q*(1-b*b+mu2*q*q)
        dy[:,2:5]=e1;dy[:,5:8]=L0[:,None]*normal;dy[:,8:11]=M[:,None]*normal
        dy[:,11:14]=-L0[:,None]*e1-M[:,None]*e2
        return dy
    mesh=np.linspace(0,L,nr+1);rows=[];dt=L/(nr*substeps)
    for j,x in enumerate(mesh):
        base=gamma.copy();base[:,2]=C+x
        ez=np.zeros_like(base);ez[:,2]=1
        delta=np.stack((Y[:,2:5]-base,Y[:,5:8]-ez,rhs(x,Y)[:,5:8]))
        if j==0:delta[:]=0
        rows.append(np.fft.rfft(delta,axis=1,norm='forward'))
        if j==nr:break
        for t in range(substeps):
            s=(j*substeps+t)*dt
            k1=rhs(s,Y);k2=rhs(s+dt/2,Y+k1*(dt/2));k3=rhs(s+dt/2,Y+k2*(dt/2));k4=rhs(s+dt,Y+k3*dt)
            Y+=(dt/6)*(k1+2*k2+2*k3+k4)
    return mesh,np.asarray(rows)

def polynomials(T,d):
    # Left/right endpoint value, derivative and second derivative Hermite factors.
    coef=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
                   [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])
    for _ in range(d):coef=coef[:,1:]*np.arange(1,coef.shape[1])
    return np.array([np.polynomial.polynomial.polyval(T,row) for row in coef]).T

class Collar:
    def __init__(self,geo,mesh,spectrum):
        self.geo=geo;self.mesh=mesh;self.spectrum=spectrum
    @classmethod
    def load(cls,physical_source,state):
        phys=phys_module(physical_source)
        with np.load(state,allow_pickle=False) as z:
            if str(z['physicalSHA'])!=PHYSICAL or str(z['entrySHA'])!=sha(__file__) or float(z['end'])!=L:
                raise ValueError('Different physical collar definition')
            return cls(phys.NormalCurve(),z['mesh'].copy(),z['deltaSpectrum'].copy())
    def coefficients(self,x,d):
        x=np.atleast_1d(np.asarray(x,float))
        if np.any((x<0)|(x>L)):raise ValueError('Outside R328')
        j=np.clip(np.searchsorted(self.mesh,x,side='right')-1,0,len(self.mesh)-2)
        h=self.mesh[j+1]-self.mesh[j];v=(x-self.mesh[j])/h
        B=polynomials(v,d)
        P=0.
        for a in (0,1):
            for r in (0,1,2):P=P+(B[:,3*a+r]*h**(r-d))[:,None,None]*self.spectrum[j+a,r]
        return P
    def jets(self,x,u):
        x=np.atleast_1d(np.asarray(x,float));u=np.atleast_1d(np.asarray(u,float))
        gamma,T,acc,_=own_central(self.geo,u);cs=[self.coefficients(x,j) for j in (0,1,2)]
        modes=np.arange(cs[0].shape[1]);w=np.where(modes==0,1.,2.);w[-1]=1.
        phase=np.exp(1j*modes[:,None]*u)*w[:,None];out=[]
        for r,d in ORDERS:
            angular=phase*((1j*modes)**d)[:,None]
            val=np.einsum('rmc,ma->rac',cs[r],angular,optimize=True).real
            if r==0:
                val+=(gamma,T,acc)[d][None]
                if d==0:val[:,:,2]+=(C+x)[:,None]
            elif r==1 and d==0:val[:,:,2]+=1.
            out.append(val)
        return np.stack(out,axis=1)
    def portjets(self,u):return self.jets([L],u)[0]

def observe(obj,phys,n,m):
    extra=np.linspace(phys.V0,phys.V1,37);u0=obj.geo.integ(extra)[:,0]
    nodes=np.unique(np.r_[(np.arange(n)+.317)*2*np.pi/n,
        np.concatenate([(j*phys.PERIOD+sgn*u0-ANCHOR)%(2*np.pi) for j in range(3) for sgn in (-1,1)])])
    xs=np.unique(np.r_[0.,L,(np.arange(m)+.673)*L/m])
    peak=0.;kmax=0.;supp=np.inf;rmax=0.;wz=[np.inf,-np.inf];areaMin=np.inf;worst=(0.,0.)
    for a in range(0,len(xs),8):
        z=xs[a:a+8];J=obj.jets(z,nodes);P,V,U,A,B,D=[J[:,j] for j in range(6)]
        E=np.sum(V*V,axis=-1);F=np.sum(V*U,axis=-1);G=np.sum(U*U,axis=-1)
        f=metric(z)[0][:,None];e=E-1;g=G/f**2-1
        error=abs(e+g)/2+np.hypot((e-g)/2,F/f);ij=np.unravel_index(np.argmax(error),error.shape)
        if error[ij]>peak:peak=float(error[ij]);worst=(float(z[ij[0]]),float(nodes[ij[1]]))
        N=np.cross(V,U);ar=np.sum(N*N,axis=-1);N/=np.sqrt(ar)[...,None]
        aa=np.sum(A*N,axis=-1);bb=np.sum(B*N,axis=-1);dd=np.sum(D*N,axis=-1)
        t=(G*aa-2*F*bb+E*dd)/ar;k=(aa*dd-bb*bb)/ar
        kmax=max(kmax,float(np.max(abs(t)/2+np.sqrt(np.maximum(0,t*t/4-k)))))
        supp=min(supp,float(np.min(-np.sum(N*P,axis=-1))));rmax=max(rmax,float(np.linalg.norm(P,axis=-1).max()));areaMin=min(areaMin,float(np.sqrt(ar).min()))
        if z[-1]==L:wz=[float(P[-1,:,2].min()),float(P[-1,:,2].max())]
    return dict(testRadial=len(xs),testAngles=len(nodes),metric=peak,worst=worst,curvature=kmax,minimumSupport=supp,maximumNorm=rmax,minimumArea=areaMin,exitHeight=wz)

def main():
    p=argparse.ArgumentParser();p.add_argument('--physical-source',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--levels',type=int,nargs='+',default=[768,1536,3072]);p.add_argument('--substeps',type=int,default=8)
    a=p.parse_args();phys=phys_module(a.physical_source);geo=phys.NormalCurve();table=[]
    for n in a.levels:
        if n<96 or n%24:raise ValueError('Use angular multiples of 24')
        nr=n//24;mesh,cs=collar_flow(geo,n,nr,a.substeps);C0=Collar(geo,mesh,cs)
        obs=observe(C0,phys,829,2*nr+5);obs.update(angularCount=n,radialCells=nr,internalRK4Steps=nr*a.substeps);table.append(obs);print('R328_ACTUAL_COLLAR',obs,flush=True)
    state=a.out.with_suffix('.npz')
    with state.open('xb') as h:np.savez_compressed(h,entrySHA=sha(__file__),physicalSHA=sha(a.physical_source),mesh=mesh,deltaSpectrum=cs,end=L,anchor=ANCHOR,halfHeight=C)
    j=dict(schema='R328-actual-W040-exact-collar-numerical-position-source-v1',entrySHA=sha(__file__),physicalSHA=sha(a.physical_source),stateSHA=sha(state),
           levels=table,terminalWarp=metric(L)[0],terminalWarpDerivative=40*L**3,terminalGauss=-metric(L)[2],
           scope='Analytic R328 isometry follows from its exact periodic Codazzi proof. These computed position maps are explicit radial quintic and angular Fourier approximants plus the true nonanalytic inlet. Finite residuals use their own six jets.')
    with a.out.open('x') as h:json.dump(j,h,indent=2);h.write('\n')
if __name__=='__main__':
    try:main()
    except Exception as exc:
        if '--out' in sys.argv:
            f=Path(sys.argv[sys.argv.index('--out')+1]).with_suffix('.failure.json');f.write_text(json.dumps(dict(error=type(exc).__name__,message=str(exc),frames=[(Path(z.filename).name,z.lineno,z.name) for z in traceback.extract_tb(exc.__traceback__)]),indent=2)+'\n')
        raise
