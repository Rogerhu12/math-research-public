#!/usr/bin/env python3
"""Explicit Fourier / shared-two-jet Cartesian representation of an open prefix.

The background angular coefficients use the Jacobi--Anger formula, not an
uncontrolled FFT. Every retained Cartesian Fourier coefficient is a quintic
Hermite function with shared knot two-jets. The exact analytic center is
restored by a full Cartesian two-jet lift. The physical target metric is still
the checkpoint's fixed g. Audits here are numerical, not interval certificates.
No closed tail or infinite-dimensional solution is claimed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.special import jv, jvp


def chart_jets(flow,s):
    s=np.asarray(s);x=s/flow.end
    t=np.clip(4*x-3,0,1);fac=4/flow.end
    c=1-t**3*(10-15*t+6*t*t)
    cp=-30*t*t*(1-t)**2*fac
    cpp=-60*t*(1-t)*(1-2*t)*fac*fac
    h=flow.spline(x);hp=flow.spline(x,1)/flow.end
    hpp=flow.spline(x,2)/flow.end**2
    return (flow.warp_e*h*c,flow.warp_e*(hp*c+h*cp),
            flow.warp_e*(hpp*c+2*hp*cp+h*cpp))


class CartesianTensor:
    def __init__(self,old,SharedJetQuintic,max_frequency=63):
        if max_frequency<2*old.M+1 or max_frequency%2!=1:
            raise ValueError('An odd maximum frequency containing the old space is required')
        self.old=old;self.flow=old.flow;self.core=old.core;self.width=old.width
        self.M=old.M;self.q=old.q;self.sol=old.sol
        self.odd=np.arange(1,max_frequency+1,2);self.even=2*np.arange(1,self.M+1)
        self.nodd=len(self.odd);self.n=2*self.nodd+1+self.M
        self.iz=2*self.nodd;self.E0=old.E0;self.Epp=old.Epp
        self.max_frequency=max_frequency;self.cache={}
        # Resolve every polynomial/profile/chart piece before interpolating
        # the analytic background. The old solver mesh alone need not contain
        # all knots of the independent C2 angular chart.
        extra=np.r_[old.flow.breaks,old.flow.spline.x*old.flow.end,
                    .75*old.flow.end,old.width]
        extra=extra[(extra>=old.sol.x[0])&(extra<=old.sol.x[-1])]
        s=old.sol.x.copy();self.inserted_knots=0;self.near_existing_breaks=[]
        for value in np.unique(extra):
            distance=float(np.min(abs(s-value)))
            if distance<1e-10:
                if distance:self.near_existing_breaks.append([float(value),distance])
                continue
            s=np.sort(np.r_[s,value]);self.inserted_knots+=1
        data=np.zeros((3,self.n,len(s)))
        aa=old.flow.profile(s);ee=chart_jets(old.flow,s)
        # x+iy = a sum_n J_n(-e/2) exp(i(2n+1)psi).
        for j,k in enumerate(self.odd):
            cp=[];cm=[]
            for frequency,out in [(int(k),cp),(-int(k),cm)]:
                n=(frequency-1)//2;b=-ee[0]/2;bp=-ee[1]/2;bpp=-ee[2]/2
                J=jv(n,b);J1=jvp(n,b,1);J2=jvp(n,b,2)
                out.extend([aa[0]*J,aa[1]*J+aa[0]*J1*bp,
                    aa[2]*J+2*aa[1]*J1*bp+aa[0]*(J2*bp*bp+J1*bpp)])
            for d in range(3):
                data[d,j]=cp[d]+cm[d]
                data[d,self.nodd+j]=cp[d]-cm[d]
        # Exact algebraic conversion of the represented polar correction.
        Y=np.stack([old.sol.sol(s,j)for j in range(3)])*self.q
        data[:,0]+=Y[:,0];data[:,self.nodd]+=Y[:,0]
        for j,m in enumerate(self.even):
            R=Y[:,1+j];T=Y[:,self.M+1+j]
            lower=(int(m)-2)//2;upper=int(m)//2
            data[:,lower]+=(R-T)/2
            data[:,upper]+=(R+T)/2
            data[:,self.nodd+lower]+=(T-R)/2
            data[:,self.nodd+upper]+=(R+T)/2
            data[:,self.iz+1+j]=Y[:,2*self.M+1+j]
        data[:,self.iz]=np.stack([old.sol.mean_spline(s,j)[0]for j in range(3)])
        self.rep=SharedJetQuintic(s,data)

    def basis(self,psi,derivative=0):
        psi=np.asarray(psi);B=np.zeros((self.n,len(psi),3))
        k=self.odd[:,None];phase=k*psi[None,:]+derivative*np.pi/2
        B[:self.nodd,:,0]=k**derivative*np.cos(phase)
        B[self.nodd:2*self.nodd,:,1]=k**derivative*np.sin(phase)
        if derivative==0:B[self.iz,:,2]=1
        m=self.even[:,None]
        B[self.iz+1:,:,2]=m**derivative*np.cos(m*psi[None,:]+derivative*np.pi/2)
        return B

    @staticmethod
    def values(C,B):
        return np.einsum('ks,kuc->suc',C,B,optimize=True)

    def delta(self,psi):
        psi=np.asarray(psi);theta=psi-self.E0*np.sin(2*psi)/2
        rho=1-self.E0*np.cos(2*psi);rhop=2*self.E0*np.sin(2*psi)
        b=-self.Epp*np.sin(2*psi)/2;bp=-self.Epp*np.cos(2*psi)
        bpp=2*self.Epp*np.sin(2*psi)
        cg=self.core.evaluate(theta);ng=self.core.normal_geometry(cg['phi'])
        f=self.core.frequencies;co=self.core.coefficients
        rhocp=-np.sin(cg['phi'][:,None]*f)@(f*(1-f*f)*co)
        gt=cg['Ft'];gtt=cg['Ftt']
        gttt=-ng['et']/ng['rho'][:,None]**2+ng['er']*rhocp[:,None]/ng['rho'][:,None]**3
        C=self.rep.jets[:,:,0];out=[]
        for angular_order in range(3):
            old=self.values(C.T,self.basis(psi,angular_order))
            target=np.zeros_like(old)
            if angular_order==0:
                target[0]=cg['F'];target[1,:,2]=1;target[2]=b[:,None]*gt
            elif angular_order==1:
                target[0]=rho[:,None]*gt
                target[2]=bp[:,None]*gt+(b*rho)[:,None]*gtt
            else:
                target[0]=rho[:,None]**2*gtt+rhop[:,None]*gt
                target[2]=bpp[:,None]*gt+(2*bp*rho+b*rhop)[:,None]*gtt+(b*rho*rho)[:,None]*gttt
            out.append(target-old)
        return out

    def evaluate(self,s,psi):
        s=np.atleast_1d(np.asarray(s,float));psi=np.atleast_1d(np.asarray(psi,float))
        B=[self.basis(psi,j)for j in range(3)]
        C=[self.rep(s,j)for j in range(3)]
        pair=[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]
        result=[self.values(C[i],B[j])for i,j in pair]
        if np.any(s<=self.width):
            key=(len(psi),hashlib.sha256(psi.tobytes()).digest())
            if key not in self.cache:self.cache[key]=self.delta(psi)
            ds=self.cache[key];weights=[self.old.weights(s,j)for j in range(3)]
            for out,(i,j)in zip(result,pair):
                out+=np.einsum('sj,juk->suk',weights[i],ds[j])
        return result


def audit(tensor,angular=1536,radial=2049):
    flow=tensor.flow;old=tensor.old
    ss=np.unique(np.r_[np.linspace(0,flow.end,radial),tensor.rep.x,
        (tensor.rep.x[:-1]+tensor.rep.x[1:])/2,flow.breaks,np.linspace(0,tensor.width,401)])
    psi=np.arange(angular)*2*np.pi/angular
    maxima=dict(metric_l1=0.,curvature=0.,radius_3d=0.)
    minima=dict(support=np.inf,area=np.inf,witness_distance=np.inf)
    diff=np.zeros(6);center=None;p=old.core.evaluate(np.array([0.]))['F'][0]
    for first in range(0,len(ss),24):
        s=ss[first:first+24];vals=tensor.evaluate(s,psi)
        X,Xs,Xss,Xp,Xpp,Xsp=vals
        oldvals=old.grid(s,angular);g=oldvals[-1]
        for j in range(6):diff[j]=max(diff[j],float(np.linalg.norm(vals[j]-oldvals[j],axis=2).max()))
        Fs=Xs-g['v'][:,:,None]*Xp;Ft=Xp/g['rho'][:,:,None]
        a,_,_=flow.profile(s)
        errors=np.stack((np.sum(Fs*Fs,axis=2)-1,np.sum(Fs*Ft,axis=2)/a[:,None],
            np.sum(Ft*Ft,axis=2)/a[:,None]**2-1),axis=2)
        maxima['metric_l1']=max(maxima['metric_l1'],float(np.sum(abs(np.fft.fft(errors,axis=1)/angular),axis=1).max()))
        n=np.cross(Xp,Xs);area=np.linalg.norm(n,axis=2);n/=area[:,:,None]
        E=np.sum(Xs*Xs,axis=2);F=np.sum(Xs*Xp,axis=2);G=np.sum(Xp*Xp,axis=2)
        L=np.sum(n*Xss,axis=2);M=np.sum(n*Xsp,axis=2);N=np.sum(n*Xpp,axis=2)
        detI=E*G-F*F;tr=(L*G-2*M*F+N*E)/detI;det=(L*N-M*M)/detI
        kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*det)))/2
        maxima['curvature']=max(maxima['curvature'],float(kap.max()))
        maxima['radius_3d']=max(maxima['radius_3d'],float(np.linalg.norm(X,axis=2).max()))
        minima['support']=min(minima['support'],float(np.sum(n*X,axis=2).min()))
        minima['area']=min(minima['area'],float(area.min()))
        rot=np.stack((-X[:,:,1],X[:,:,0],X[:,:,2]),axis=2)
        minima['witness_distance']=min(minima['witness_distance'],float(np.linalg.norm(rot-p,axis=2).min()))
        if first==0:
            gamma=tensor.core.evaluate(g['theta'][0]);ez=np.zeros_like(Fs[0]);ez[:,2]=1
            # The physical second derivative uses the exact coordinate chain.
            Fss=Xss-2*g['v'][:,:,None]*Xsp+g['v'][:,:,None]**2*Xpp+(g['v']*g['vp']-g['vs'])[:,:,None]*Xp
            center={'position':float(np.linalg.norm(X[0]-gamma['F'],axis=1).max()),
                    'Fs':float(np.linalg.norm(Fs[0]-ez,axis=1).max()),
                    'Fss':float(np.linalg.norm(Fss[0],axis=1).max())}
    return dict(scope='Finite sampling of a new explicit C2 representation of the same physical metric; not an interval certificate.',
        radial_samples=len(ss),angular_samples=angular,maxima=maxima,minima=minima,
        position_and_twojet_changes=diff.tolist(),center=center)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','recovery','checkpoint','port','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--max-frequency',type=int,default=63);p.add_argument('--angular',type=int,default=1536)
    p.add_argument('--radial',type=int,default=2049);a=p.parse_args();beg=time.monotonic()
    sys.path.insert(0,str(a.scripts))
    from smallcut_c2_representative import load_model,build_mean,SharedJetQuintic
    from smallcut_center_lift import CenterLift
    r,obj,flow,sol,_,_=load_model(a.recovery,a.checkpoint,a.port,a.angular)
    sol.mean_spline=build_mean(flow,sol,a.angular,8);old=CenterLift(obj,flow,sol)
    tensor=CartesianTensor(old,SharedJetQuintic,a.max_frequency)
    data=a.output.with_suffix('.npz');a.output.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(data,knots=tensor.rep.x,jets=tensor.rep.jets,
        core_frequencies=tensor.core.frequencies,core_coefficients=tensor.core.coefficients,
        odd=tensor.odd,even=tensor.even,chart_E0=tensor.E0,chart_Epp=tensor.Epp,
        lift_width=tensor.width,primary_q=r['actual_primary_amplitude'])
    result=audit(tensor,a.angular,a.radial)
    result.update(checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        data_sha256=hashlib.sha256(data.read_bytes()).hexdigest(),state_count=tensor.n,
        max_frequency=tensor.max_frequency,knots=len(tensor.rep.x),fixed_profile=r['frozen_profile'],
        inserted_break_knots=tensor.inserted_knots,breaks_already_within_1e_10=tensor.near_existing_breaks,
        seconds=time.monotonic()-beg)
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)


if __name__=='__main__':main()
