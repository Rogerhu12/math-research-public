"""Fixed-radius-profile Frenet-flow BVP with a nonzero stable terminal circle.

Author: solver_audit; GPT-6 Astra Pro; AI-assisted, 2026-11-08.
This is a finite Fourier / collocation experiment, not a rotational collar.
The exact rectifying initial core is varied through reflection-preserving modes.
The full unprojected velocity, actual metric and Darboux tensor are audited.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,gzip,hashlib,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp,solve_ivp
from scipy.interpolate import PPoly
from curve_linear_control import ramp,upward,cycle_record
from construct_general_reflected_core import ReflectedCore,curve_geometry


def load_checkpoint(path):
    path=Path(path)
    with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as f:out=json.load(f)
    if 'pp_coefficient_chunks' in out:
        chunks=[]
        for item in out['pp_coefficient_chunks']:
            with gzip.open(path.parent/item['file'],'rb') as f:chunks.append(np.load(f,allow_pickle=False))
        out['pp_coefficients']=np.concatenate(chunks,axis=2)
    return out


def save_checkpoint(path,out):
    path=Path(path);out=dict(out)
    if 'pp_coefficients' in out:
        coef=np.asarray(out.pop('pp_coefficients'));out.pop('values',None)
        stem=path.name.removesuffix('.gz').removesuffix('.json');chunks=[]
        block=max(1,int(4400000/(coef.shape[0]*coef.shape[1]*coef.dtype.itemsize)))
        for index,first in enumerate(range(0,coef.shape[2],block)):
            last=min(first+block,coef.shape[2]);part=path.with_name(f'{stem}_coeff_{index:02d}.npy.gz')
            with gzip.open(part,'wb',compresslevel=9) as f:np.save(f,coef[:,:,first:last],allow_pickle=False)
            if part.stat().st_size>5000000:raise RuntimeError('Coefficient chunk exceeds repository 5 MB limit')
            chunks.append(dict(file=part.name,state_first=first,state_last_exclusive=last,
                               bytes=part.stat().st_size,sha256=hashlib.sha256(part.read_bytes()).hexdigest()))
        out['pp_coefficient_chunks']=chunks
        out['array_format']='Exact float64 NumPy arrays, gzip-compressed, partitioned by state; no coefficient rounding.'
    encoded=json.dumps(out,indent=2,allow_nan=False)+'\n'
    if path.suffix=='.gz':
        with gzip.open(path,'wt') as f:f.write(encoded)
    elif len(encoded)>1000000:raise RuntimeError('Metadata exceeds 1 MB; choose .json.gz')
    else:path.write_text(encoded)
    return out


class Prefix:
    def __init__(self,modes=2,amplitude=.001,delta=1.,vu=.93,vd=.93,eps=.2,
                 cycles=1,angular=128,terminal_c4=0.,arc_nodes=1024):
        self.M=modes;self.q=amplitude;self.delta=delta;self.vu=vu;self.vd=vd
        self.eps=eps;self.cycles=cycles;self.nt=angular;self.arc_nodes=arc_nodes
        self.c4=terminal_c4;self.Tu=delta/(vu*(1-eps));self.Td=delta/(vd*(1-eps))
        self.period=self.Tu+self.Td;self.end=self.period*cycles
        self.odd=np.arange(1,2*modes+2,2);self.even=np.arange(2,2*modes+1,2)
        self.n=3*modes+2;self.ix=0;self.iy=modes+1;self.iz=2*(modes+1)
        self.B,self.B1,self.B2=self.basis(angular)
        self.rhos=[];self.multipliers=[]
        for m in self.even:
            u=upward(int(m),delta,vu,eps);d=upward(int(m),delta,vd,eps)
            r=cycle_record(int(m),delta,vu,vd,eps,u,d)
            if r['kind']!='hyperbolic':raise ValueError(f'Mode {m} is not hyperbolic')
            self.rhos.append(r['stable_slope_g_over_f']);self.multipliers.append(r['stable_multiplier'])
        self.rhos=np.array(self.rhos);self.h0=-1/(4*self.rhos[0])
        if self.h0<=0:raise ValueError('The selected reflected core needs a negative m2 stable slope')
        self.pscale=np.array([1.]+[max(amplitude**j,1e-8) for j in range(2,modes+1)])
        self.bscale=np.array([max(amplitude**j,1e-8) for j in range(1,modes+1)])
        self._cache=None;self._cached=None;self.calls=0

    def basis(self,n):
        theta=2*np.pi*np.arange(n)/n
        B=np.zeros((self.n,n,3));B1=B.copy();B2=B.copy()
        for j,k in enumerate(self.odd):
            B[j,:,0]=np.cos(k*theta);B1[j,:,0]=-k*np.sin(k*theta);B2[j,:,0]=-k*k*np.cos(k*theta)
            i=self.iy+j;B[i,:,1]=np.sin(k*theta);B1[i,:,1]=k*np.cos(k*theta);B2[i,:,1]=-k*k*np.sin(k*theta)
        for j,k in enumerate(self.even):
            i=self.iz+j;B[i,:,2]=np.cos(k*theta);B1[i,:,2]=-k*np.sin(k*theta);B2[i,:,2]=-k*k*np.cos(k*theta)
        return B,B1,B2

    def profile(self,s):
        s=np.asarray(s);t=np.mod(s,self.period);up=t<self.Tu
        q=np.where(up,t/self.Tu,(t-self.Tu)/self.Td)
        w,I=ramp(q,self.eps)
        wp=np.where(q<self.eps,np.pi/(2*self.eps)*np.sin(np.pi*q/self.eps),
             np.where(q>1-self.eps,-np.pi/(2*self.eps)*np.sin(np.pi*(1-q)/self.eps),0.))
        a=np.where(up,1+self.delta*I/(1-self.eps),1+self.delta*(1-I/(1-self.eps)))
        ap=np.where(up,self.vu*w,-self.vd*w)
        app=np.where(up,self.vu*wp/self.Tu,-self.vd*wp/self.Td)
        return a,ap,app

    def base(self,s,derivative=0):
        a,ap,app=self.profile(s);z=(a,ap,app)[derivative]
        out=np.zeros((self.n,len(np.atleast_1d(s))));out[self.ix]=z;out[self.iy]=z
        return out

    @staticmethod
    def values(C,B):return np.einsum('kn,kpc->npc',C,B,optimize=True)

    @staticmethod
    def project(F,B):return 2/len(B[0])*np.einsum('npc,kpc->kn',F,B,optimize=True)

    def frame(self,s,C,B1=None,B2=None):
        B1=self.B1 if B1 is None else B1;B2=self.B2 if B2 is None else B2
        d=self.values(C,B1);dd=self.values(C,B2)
        lam=np.sqrt(np.sum(d*d,axis=2));T=d/lam[:,:,None]
        dt=np.sum(dd*T,axis=2);nvec=dd-dt[:,:,None]*T
        nn=np.sqrt(np.sum(nvec*nvec,axis=2));N=nvec/nn[:,:,None]
        kap=nn/lam**2;Bin=np.cross(T,N)
        a,ap,app=self.profile(s);alpha=-ap[:,None]/(a[:,None]*kap)
        margin=1-alpha**2
        if np.min(margin.real)<=0 or np.min(lam.real)<=0 or np.min(nn.real)<=0:
            raise FloatingPointError(f'Frenet domain failure: min root {np.min(margin.real):.9g}')
        beta=np.sqrt(margin);V=alpha[:,:,None]*N+beta[:,:,None]*Bin
        return dict(d=d,dd=dd,lam=lam,T=T,dt=dt,nn=nn,N=N,kap=kap,Bin=Bin,
                    a=a,ap=ap,app=app,alpha=alpha,beta=beta,margin=margin,V=V)

    @staticmethod
    def frame_jvp(fr,delta_d,delta_dd):
        T=fr['T'];N=fr['N'];lam=fr['lam'];nn=fr['nn'];kap=fr['kap']
        dl=np.sum(T*delta_d,axis=2)
        dT=(delta_d-T*dl[:,:,None])/lam[:,:,None]
        ddt=np.sum(delta_dd*T+fr['dd']*dT,axis=2)
        dq=delta_dd-ddt[:,:,None]*T-fr['dt'][:,:,None]*dT
        dn=np.sum(N*dq,axis=2);dN=(dq-N*dn[:,:,None])/nn[:,:,None]
        dk=dn/lam**2-2*kap*dl/lam
        dB=np.cross(dT,N)+np.cross(T,dN)
        da=-fr['alpha']*dk/kap;db=-fr['alpha']*da/fr['beta']
        return da[:,:,None]*N+fr['alpha'][:,:,None]*dN+db[:,:,None]*fr['Bin']+fr['beta'][:,:,None]*dB

    def fun(self,s,y,p):
        self.calls+=1;C=self.base(s)+self.q*y;fr=self.frame(s,C)
        return (self.project(fr['V'],self.B)-self.base(s,1))/self.q

    def fun_jac(self,s,y,p):
        C=self.base(s)+self.q*y;fr=self.frame(s,C);out=np.empty((self.n,self.n,len(s)))
        for j in range(self.n):
            dv=self.frame_jvp(fr,self.B1[j][None,:,:],self.B2[j][None,:,:])
            out[:,j,:]=self.project(dv,self.B)
        return out,np.zeros((self.n,self.M,len(s)))

    def parameters(self,p):
        h=self.h0+p[0];rad=np.zeros(self.M//2);hei=np.zeros((self.M+1)//2);hei[0]=self.q
        for j,m in enumerate(self.even[1:],start=1):
            value=p[j]*self.pscale[j]
            if m%4==0:rad[m//4-1]=value
            else:hei[(m-2)//4]=value
        # Eliminate horizontal radius using the exact central perimeter a0=1.
        phi=2*np.pi*np.arange(self.arc_nodes)/self.arc_nodes;R=max(.2,math.sqrt(max(.04,1-2*self.q**2)))
        for it in range(20):
            g=curve_geometry(phi,R,rad,hei);a0=float(np.mean(g['speed']))
            if abs(a0-1)<3e-15:break
            erp=np.c_[-np.sin(phi),np.cos(phi),np.zeros(len(phi))]
            derivative=float(np.mean(np.sum(g['d1']*erp,axis=1)/g['speed']))
            R-=(a0-1)/derivative
            if R<=.05:raise FloatingPointError('Core perimeter normalization left positive radius range')
        return dict(R=float(R),radial=rad.tolist(),height=hei.tolist(),halfwidth=float(h))

    def initial(self,p):
        if self._cache is not None and np.array_equal(p,self._cache):return self._cached
        par=self.parameters(p);core=ReflectedCore(par['R'],par['radial'],par['height'],self.arc_nodes)
        nt=max(256,8*(2*self.M+1));theta=2*np.pi*np.arange(nt)/nt
        exact=core.evaluate(par['halfwidth'],theta)
        if np.min(exact['den'])<=0:raise FloatingPointError('Exact rectifying core loses regularity')
        B,_,_=self.basis(nt);C=self.project(exact['F'][None,:,:],B)[:,0]
        out=(C-self.base(np.array([0.]))[:,0])/self.q
        self._cache=p.copy();self._cached=out
        return out

    def modal(self,y):
        f=[];g=[]
        for j,m in enumerate(self.even):
            k=(m-2)//2
            f.append(.5*(y[self.ix+k]-y[self.iy+k]+y[self.ix+k+1]+y[self.iy+k+1]))
            g.append(y[self.iz+j])
        return np.array(f),np.array(g)

    def bc(self,ya,yb,p):
        f,g=self.modal(yb);z=self.q*(g-self.rhos*f)
        if self.M>=2:z[1]-=self.c4*(self.q*g[0])**2
        terminal=z/(np.hypot(1,self.rhos)*self.bscale)
        return np.r_[ya-self.initial(p),terminal]

    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
        B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        fm,gm=self.modal(np.eye(self.n));f,g=self.modal(yb)
        J=self.q*(gm-self.rhos[:,None]*fm)
        if self.M>=2:J[1]-=2*self.c4*self.q**2*g[0]*gm[0]
        B[self.n:]=J/(np.hypot(1,self.rhos)*self.bscale)[:,None]
        # Differentiate the exact core with a physical perturbation, not a tiny
        # normalized coefficient perturbation lost under arclength inversion.
        for j in range(self.M):
            step=2e-5 if j==0 else 2e-6/(self.pscale[j]*(j+1)**2)
            v=np.zeros(self.M);v[j]=step
            deriv=(-self.initial(p+2*v)+8*self.initial(p+v)-8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
            P[:self.n,j]=-deriv
        return A,B,P

    def seed(self,nodes):
        p=np.zeros(self.M)
        if self.M>=2:p[1]=1.81124*self.q**2/self.pscale[1]
        x=np.linspace(0,self.end,nodes)
        def rhs(s,y):
            a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return [-(3*v*y[0]+4*b*y[1])/a,3*v*v*y[0]/(a*b)+4*v*y[1]/a]
        lin=solve_ivp(rhs,[0,self.end],[1/self.rhos[0],1],method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True,max_step=self.period/100)
        f,g=lin.sol(x);y=np.zeros((self.n,len(x)))
        y[0]=.75*f;y[self.iy]=-.75*f;y[1]=.25*f;y[self.iy+1]=.25*f;y[self.iz]=g
        # First-order circle-frame perturbation has the required tangential term.
        return x,y,p

    def jacobian_check(self):
        x=np.array([.031,.49,1.11,1.79,2.31])%self.end
        y=np.zeros((self.n,len(x)));y[self.iz]=.2;y[1]=.03
        rng=np.random.default_rng(20261108);v=rng.normal(size=y.shape)
        J,_=self.fun_jac(x,y,np.zeros(self.M));pred=np.einsum('ijk,jk->ik',J,v)
        step=1e-25;actual=self.fun(x,y.astype(complex)+1j*step*v,np.zeros(self.M)).imag/step
        return dict(max_abs=float(np.max(abs(pred-actual))),relative=float(np.max(abs(pred-actual))/max(1,np.max(abs(actual)))))

    def c2_interpolant(self,sol):
        s=sol.x;C=self.base(s)+self.q*sol.y;fr=self.frame(s,C)
        Cp=self.project(fr['V'],self.B)
        dV=self.frame_jvp(fr,self.values(Cp,self.B1),self.values(Cp,self.B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
        be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        Cpp=self.project(dV,self.B);dy=(Cp-self.base(s,1))/self.q;ddy=(Cpp-self.base(s,2))/self.q
        # Construct from local differences in extended precision. Conversion
        # through Bernstein control points subtracts O(1) coordinates to form
        # O(h^5) terms and creates visible artificial second-jet jumps.
        Y=sol.y.astype(np.longdouble).T;D=dy.astype(np.longdouble).T;Q=ddy.astype(np.longdouble).T
        h=np.diff(s).astype(np.longdouble)[:,None]
        e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2
        e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
        u=10*e0-4*h*e1+h*h*e2/2;v=-15*e0+7*h*e1-h*h*e2;w=6*e0-3*h*e1+h*h*e2/2
        c=np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1])).astype(float)
        return PPoly.construct_fast(c,s,extrapolate=True,axis=1)

    def height_integral(self,sol,s,angular=256,order=6):
        """Mean-height antiderivative on individual collocation segments.

        A global irregular Simpson mesh can contain nearly coincident output
        and collocation points, making its weights ill-conditioned. Positive
        Gauss weights on each original segment avoid that representation issue.
        """
        _,B1,B2=self.basis(angular);g,w=np.polynomial.legendre.leggauss(order)
        def integrate_intervals(left,right):
            left=np.asarray(left);right=np.asarray(right);h=right-left
            q=((left+right)[:,None]+h[:,None]*g[None,:])/2
            flat=q.ravel();means=np.empty_like(flat)
            for first in range(0,len(flat),128):
                t=flat[first:first+128];C=self.base(t)+self.q*sol.sol(t)
                fr=self.frame(t,C,B1,B2);means[first:first+128]=np.mean(fr['V'][:,:,2],axis=1)
            return h/2*(means.reshape(q.shape)@w)
        full=integrate_intervals(sol.x[:-1],sol.x[1:]);prefix=np.r_[0.,np.cumsum(full)]
        idx=np.clip(np.searchsorted(sol.x,s,side='right')-1,0,len(sol.x)-2)
        return prefix[idx]+integrate_intervals(sol.x[idx],np.asarray(s))

    def audit(self,sol,points=401,angular=512):
        s=np.unique(np.r_[np.linspace(0,self.end,points),sol.x,(sol.x[:-1]+sol.x[1:])/2]);y=sol.sol(s)
        C=self.base(s)+self.q*y;Cp=self.base(s,1)+self.q*sol.sol(s,1)
        Cpp=self.base(s,2)+self.q*sol.sol(s,2);B,B1,B2=self.basis(angular)
        fr=self.frame(s,C,B1,B2);V=self.values(Cp,B);mean=np.mean(fr['V'][:,:,2],axis=1)
        V[:,:,2]+=mean[:,None]
        dV=self.frame_jvp(fr,self.values(Cp,B1),self.values(Cp,B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
        be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        mean2=np.mean(dV[:,:,2],axis=1);V2=self.values(Cpp,B);V2[:,:,2]+=mean2[:,None]
        Ft=fr['d'];Ftt=fr['dd'];Vt=self.values(Cp,B1);a=fr['a'][:,None]
        E=np.sum(V*V,axis=2);F=np.sum(V*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a,G/a**2-1),axis=2)
        coef=np.fft.fft(errors,axis=1)/angular;l1=np.sum(abs(coef),axis=1)
        metric=float(np.max(abs(errors)));metric_bound=float(np.max(l1))
        flowdef=np.linalg.norm(V-fr['V'],axis=2)
        normal=np.cross(V,Ft);normal/=np.linalg.norm(normal,axis=2)[:,:,None]
        L=np.sum(V2*normal,axis=2);MM=np.sum(Vt*normal,axis=2);NN=np.sum(Ftt*normal,axis=2)
        detI=E*G-F**2;trace=(L*G-2*MM*F+NN*E)/detI;detII=(L*NN-MM**2)/detI
        disc=np.sqrt(np.maximum(0,trace**2-4*detII));kmax=np.maximum(abs((trace+disc)/2),abs((trace-disc)/2))
        Hss=V2;Hst=(Vt-(fr['ap']/fr['a'])[:,None,None]*Ft)/a[:,:,None]
        Htt=(Ftt+(fr['a']*fr['ap'])[:,None,None]*V)/a[:,:,None]**2
        gram=np.eye(3)[None,None,:,:]-V[:,:,:,None]*V[:,:,None,:]-(Ft/a[:,:,None])[:,:,:,None]*(Ft/a[:,:,None])[:,:,None,:]
        tensor=.5*(Hss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Hss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]
        tensor+=(fr['app']/fr['a'])[:,None,None,None]*gram
        tensor_norm=np.max(abs(np.linalg.eigvalsh(tensor)),axis=2)
        tensor_coef=np.fft.fft(tensor,axis=1)/angular
        tensor_bound=float(np.max(np.sum(np.sqrt(np.sum(abs(tensor_coef)**2,axis=(2,3))),axis=1)))
        par=self.parameters(sol.p);core=ReflectedCore(par['R'],par['radial'],par['height'],self.arc_nodes)
        theta=2*np.pi*np.arange(angular)/angular;port=core.evaluate(par['halfwidth'],theta)
        init=self.values(C[:,:1],B)[0];init[:,2]+=np.mean(port['F'][:,2])
        central=curve_geometry(theta,par['R'],par['radial'],par['height'])
        pv=float(np.ptp(central['gamma'][:,2]));LB=2*(par['halfwidth']+self.end)
        f,g=self.modal(y);noncircle=np.sqrt(np.mean(np.sum((self.values(C-self.base(s),B))**2,axis=2),axis=1))
        # This centered fixed-axis measure is not a best free 3D-circle fit.
        heightmean=self.height_integral(sol,s,angular,6)
        position=self.values(C,B);position[:,:,2]+=heightmean[:,None]
        box=np.ptp(position.reshape(-1,3),axis=0)
        cross2=lambda u,v:u[...,0]*v[...,1]-u[...,1]*v[...,0]
        rho2=np.sum(position[:,:,:2]**2,axis=2)
        theta_num=cross2(position,Ft);s_num=cross2(position,V)
        axial_jac=theta_num*V[:,:,2]-s_num*Ft[:,:,2]
        scalars=np.stack((rho2,theta_num,axial_jac),axis=2)
        sc=np.fft.fft(scalars,axis=1)/angular
        tails=np.sum(abs(sc[:,1:]),axis=1)
        angular_lower=sc[:,0].real-tails
        portmean=float(np.mean(port['F'][:,2]));absolute_z=position[:,:,2]+portmean
        zcoef=np.fft.fft(absolute_z,axis=1)/angular
        radial_upper=float(np.sqrt(np.max(sc[:,0,0].real+tails[:,0])))
        zabs_upper=float(np.max(np.sum(abs(zcoef),axis=1)))
        interior=sol.x[1:-1];delta=np.minimum(np.diff(sol.x)[:-1],np.diff(sol.x)[1:])*1e-7
        jumps=self.q*(sol.sol(interior+delta,2)-sol.sol(interior-delta,2)) if len(interior) else np.zeros((self.n,1))
        pc=sol.sol.c;degree=len(pc)-1;hs=np.diff(sol.x)
        d2c=np.array([j*(j-1) for j in range(degree,1,-1)])[:,None,None]*pc[:-2]
        left=np.zeros_like(pc[0,:-1])
        for coeff in d2c:left=left*hs[:-1,None]+coeff[:-1]
        exact_jump=self.q*(left-2*pc[-3,1:])
        return dict(samples_s=len(s),samples_theta=angular,metric_sampled_max=metric,metric_theta_Fourier_l1_bound=metric_bound,
            metric_component_bounds=np.max(l1,axis=0).tolist(),full_unprojected_flow_defect=float(np.max(flowdef)),
            projected_collocation_ode_defect=float(np.max(abs(sol.sol(s,1)-self.fun(s,y,sol.p)))),
            darboux_tensor_spectral_max=float(np.max(tensor_norm)),darboux_tensor_times_Wr_squared=float(np.max(tensor_norm)*self.delta**2),
            darboux_tensor_times_Lband_squared=float(np.max(tensor_norm)*LB**2),
            darboux_tensor_theta_Fourier_l1_frobenius_bound=tensor_bound,
            minimum_root_margin=float(np.min(fr['margin'])),minimum_curve_kappa=float(np.min(fr['kap'])),
            maximum_surface_principal_curvature=float(np.max(kmax)),kappa_times_Wr=float(np.max(kmax)*self.delta),
            kappa_times_Lband=float(np.max(kmax)*LB),radial_excursion_Wr=self.delta,Lband=LB,
            central_PV=pv,central_PV_over_Wr=pv/self.delta,central_PV_over_Lband=pv/LB,
            initial_exact_core_projection_error=float(np.max(np.linalg.norm(init-port['F'],axis=1))),
            initial_first_jet_error=float(np.max(np.linalg.norm(V[0]-port['Fx'],axis=1))),
            initial_second_jet_error=float(np.max(np.linalg.norm(V2[0]-port['Fxx'],axis=1))),
            exact_core_a0=core.a0,core_halfwidth=par['halfwidth'],core_denominator_min=float(np.min(port['den'])),
            boundary_residual_max=float(np.max(abs(self.bc(y[:,0],y[:,-1],sol.p)))),
            endpoint_modes=[dict(mode=int(m),f=float(self.q*f[j,-1]),g=float(self.q*g[j,-1])) for j,m in enumerate(self.even)],
            fixed_axis_noncircle_rms_initial=float(noncircle[0]),fixed_axis_noncircle_rms_final=float(noncircle[-1]),
            finite_prefix_position_box_diagonal=float(np.linalg.norm(box)),
            sampled_prefix_cylindrical_projection_margins=[float(np.min(z)) for z in (rho2,theta_num,axial_jac)],
            angular_certified_prefix_cylindrical_projection_margins=np.min(angular_lower,axis=0).tolist(),
            finite_symmetric_band_cylinder_diameter_upper=2*math.hypot(radial_upper,zabs_upper),
            finite_symmetric_band_diameter_bound_over_Wr=2*math.hypot(radial_upper,zabs_upper)/self.delta,
            prefix_height_integral=float(heightmean[-1]),port_mean_height=portmean,
            height_integral_quadrature_order=6,
            exact_polynomial_second_derivative_join_error=float(np.max(abs(exact_jump))) if len(interior) else 0.,
            estimated_nonmean_second_derivative_jump=float(np.max(abs(jumps))))

    def audit_streamed(self,sol,points=401,angular=256,block=96):
        """Same complete geometric audit with bounded peak memory."""
        s=np.unique(np.r_[np.linspace(0,self.end,points),sol.x,(sol.x[:-1]+sol.x[1:])/2])
        height=self.height_integral(sol,s,angular,6);B,B1,B2=self.basis(angular)
        par=self.parameters(sol.p);core=ReflectedCore(par['R'],par['radial'],par['height'],self.arc_nodes)
        theta=2*np.pi*np.arange(angular)/angular;port=core.evaluate(par['halfwidth'],theta)
        portmean=float(np.mean(port['F'][:,2]));central=curve_geometry(theta,par['R'],par['radial'],par['height'])
        pv=float(np.ptp(central['gamma'][:,2]));LB=2*(par['halfwidth']+self.end)
        hi={k:0. for k in ('metric','metric_bound','flow','ode','D','D_bound','kappa','rho_upper','z_upper')}
        lo={k:math.inf for k in ('root','kappa')};metric_components=np.zeros(3)
        sample_margins=np.full(3,np.inf);angular_margins=np.full(3,np.inf)
        box_min=np.full(3,np.inf);box_max=-box_min;initial_errors=None;noncircle=[]
        for first in range(0,len(s),block):
            t=s[first:first+block];y=sol.sol(t);C=self.base(t)+self.q*y
            Cp=self.base(t,1)+self.q*sol.sol(t,1);Cpp=self.base(t,2)+self.q*sol.sol(t,2)
            fr=self.frame(t,C,B1,B2);V=self.values(Cp,B);mean=np.mean(fr['V'][:,:,2],axis=1);V[:,:,2]+=mean[:,None]
            dV=self.frame_jvp(fr,self.values(Cp,B1),self.values(Cp,B2))
            ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
            be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
            V2=self.values(Cpp,B);V2[:,:,2]+=np.mean(dV[:,:,2],axis=1)[:,None]
            Ft=fr['d'];Ftt=fr['dd'];Vt=self.values(Cp,B1);a=fr['a'][:,None]
            E=np.sum(V*V,axis=2);F=np.sum(V*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
            errors=np.stack((E-1,F/a,G/a**2-1),axis=2)
            l1=np.sum(abs(np.fft.fft(errors,axis=1)/angular),axis=1)
            metric_components=np.maximum(metric_components,np.max(l1,axis=0))
            hi['metric']=max(hi['metric'],float(np.max(abs(errors))));hi['metric_bound']=max(hi['metric_bound'],float(np.max(l1)))
            hi['flow']=max(hi['flow'],float(np.max(np.linalg.norm(V-fr['V'],axis=2))))
            hi['ode']=max(hi['ode'],float(np.max(abs(sol.sol(t,1)-self.fun(t,y,sol.p)))))
            normal=np.cross(V,Ft);normal/=np.linalg.norm(normal,axis=2)[:,:,None]
            L=np.sum(V2*normal,axis=2);MM=np.sum(Vt*normal,axis=2);NN=np.sum(Ftt*normal,axis=2)
            detI=E*G-F**2;tr=(L*G-2*MM*F+NN*E)/detI;detII=(L*NN-MM**2)/detI
            disc=np.sqrt(np.maximum(0,tr**2-4*detII));kap=np.maximum(abs((tr+disc)/2),abs((tr-disc)/2))
            hi['kappa']=max(hi['kappa'],float(np.max(kap)))
            Hst=(Vt-(fr['ap']/fr['a'])[:,None,None]*Ft)/a[:,:,None]
            Htt=(Ftt+(fr['a']*fr['ap'])[:,None,None]*V)/a[:,:,None]**2
            gram=np.eye(3)[None,None,:,:]-V[:,:,:,None]*V[:,:,None,:]-(Ft/a[:,:,None])[:,:,:,None]*(Ft/a[:,:,None])[:,:,None,:]
            tensor=.5*(V2[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*V2[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]
            tensor+=(fr['app']/fr['a'])[:,None,None,None]*gram
            hi['D']=max(hi['D'],float(np.max(abs(np.linalg.eigvalsh(tensor)))))
            cf=np.fft.fft(tensor,axis=1)/angular
            hi['D_bound']=max(hi['D_bound'],float(np.max(np.sum(np.sqrt(np.sum(abs(cf)**2,axis=(2,3))),axis=1))))
            lo['root']=min(lo['root'],float(np.min(fr['margin'])));lo['kappa']=min(lo['kappa'],float(np.min(fr['kap'])))
            pos=self.values(C,B);pos[:,:,2]+=height[first:first+len(t),None]
            box_min=np.minimum(box_min,np.min(pos,axis=(0,1)));box_max=np.maximum(box_max,np.max(pos,axis=(0,1)))
            rho2=np.sum(pos[:,:,:2]**2,axis=2)
            cross=lambda u,v:u[...,0]*v[...,1]-u[...,1]*v[...,0]
            thnum=cross(pos,Ft);snum=cross(pos,V);jac=thnum*V[:,:,2]-snum*Ft[:,:,2]
            scalars=np.stack((rho2,thnum,jac),axis=2);sc=np.fft.fft(scalars,axis=1)/angular
            tails=np.sum(abs(sc[:,1:]),axis=1);lower=sc[:,0].real-tails
            sample_margins=np.minimum(sample_margins,np.min(scalars,axis=(0,1)))
            angular_margins=np.minimum(angular_margins,np.min(lower,axis=0))
            hi['rho_upper']=max(hi['rho_upper'],float(np.sqrt(np.max(sc[:,0,0].real+tails[:,0]))))
            zcoef=np.fft.fft(pos[:,:,2]+portmean,axis=1)/angular
            hi['z_upper']=max(hi['z_upper'],float(np.max(np.sum(abs(zcoef),axis=1))))
            nc=np.sqrt(np.mean(np.sum(self.values(C-self.base(t),B)**2,axis=2),axis=1))
            noncircle.extend(nc[[0,-1]].tolist())
            if first==0:
                f0=pos[0].copy();f0[:,2]+=portmean
                initial_errors=[float(np.max(np.linalg.norm(u-v,axis=1))) for u,v in ((f0,port['F']),(V[0],port['Fx']),(V2[0],port['Fxx']))]
        ends=sol.sol(np.array([0.,self.end]));f,g=self.modal(ends)
        interior=sol.x[1:-1];hs=np.diff(sol.x);delta=np.minimum(hs[:-1],hs[1:])*1e-7
        jumps=self.q*(sol.sol(interior+delta,2)-sol.sol(interior-delta,2))
        pc=sol.sol.c;degree=len(pc)-1;d2c=np.array([j*(j-1) for j in range(degree,1,-1)])[:,None,None]*pc[:-2]
        left=np.zeros_like(pc[0,:-1])
        for coeff in d2c:left=left*hs[:-1,None]+coeff[:-1]
        exact_jump=self.q*(left-2*pc[-3,1:]);diameter=2*math.hypot(hi['rho_upper'],hi['z_upper'])
        return dict(samples_s=len(s),samples_theta=angular,audit_stream_block=block,
            metric_sampled_max=hi['metric'],metric_theta_Fourier_l1_bound=hi['metric_bound'],metric_component_bounds=metric_components.tolist(),
            full_unprojected_flow_defect=hi['flow'],projected_collocation_ode_defect=hi['ode'],
            darboux_tensor_spectral_max=hi['D'],darboux_tensor_times_Wr_squared=hi['D']*self.delta**2,
            darboux_tensor_times_Lband_squared=hi['D']*LB**2,darboux_tensor_theta_Fourier_l1_frobenius_bound=hi['D_bound'],
            minimum_root_margin=lo['root'],minimum_curve_kappa=lo['kappa'],maximum_surface_principal_curvature=hi['kappa'],
            kappa_times_Wr=hi['kappa']*self.delta,kappa_times_Lband=hi['kappa']*LB,radial_excursion_Wr=self.delta,Lband=LB,
            central_PV=pv,central_PV_over_Wr=pv/self.delta,central_PV_over_Lband=pv/LB,
            initial_exact_core_projection_error=initial_errors[0],initial_first_jet_error=initial_errors[1],initial_second_jet_error=initial_errors[2],
            exact_core_a0=core.a0,core_halfwidth=par['halfwidth'],core_denominator_min=float(np.min(port['den'])),
            boundary_residual_max=float(np.max(abs(self.bc(ends[:,0],ends[:,-1],sol.p)))),
            endpoint_modes=[dict(mode=int(m),f=float(self.q*f[j,-1]),g=float(self.q*g[j,-1])) for j,m in enumerate(self.even)],
            fixed_axis_noncircle_rms_initial=noncircle[0],fixed_axis_noncircle_rms_final=noncircle[-1],
            finite_prefix_position_box_diagonal=float(np.linalg.norm(box_max-box_min)),
            sampled_prefix_cylindrical_projection_margins=sample_margins.tolist(),
            angular_certified_prefix_cylindrical_projection_margins=angular_margins.tolist(),
            finite_symmetric_band_cylinder_diameter_upper=diameter,finite_symmetric_band_diameter_bound_over_Wr=diameter/self.delta,
            prefix_height_integral=float(height[-1]),port_mean_height=portmean,height_integral_quadrature_order=6,
            exact_polynomial_second_derivative_join_error=float(np.max(abs(exact_jump))),
            estimated_nonmean_second_derivative_jump=float(np.max(abs(jumps))))


class CylindricalPrefix(Prefix):
    """Truncate complete physical modes in the (er,etheta,ez) frame.

    An independent Cartesian x/y cutoff leaves a partial highest physical mode
    without its height or stable boundary condition. This basis excludes that
    artificial incomplete mode while retaining every component of each mode.
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ir=1;self.it=self.M+1;self.iz=2*self.M+1

    def basis(self,n):
        self.n=3*self.M+1;theta=2*np.pi*np.arange(n)/n
        er=np.c_[np.cos(theta),np.sin(theta),np.zeros(n)]
        et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(n)]
        ez=np.tile([0.,0.,1.],(n,1));B=np.zeros((self.n,n,3));B1=B.copy();B2=B.copy()
        B[0]=er;B1[0]=et;B2[0]=-er
        for j,m in enumerate(self.even):
            co=np.cos(m*theta)[:,None];si=np.sin(m*theta)[:,None]
            r=1+j;t=self.M+1+j;z=2*self.M+1+j
            B[r]=co*er;B1[r]=-m*si*er+co*et;B2[r]=-(m*m+1)*co*er-2*m*si*et
            B[t]=si*et;B1[t]=m*co*et-si*er;B2[t]=-(m*m+1)*si*et-2*m*co*er
            B[z]=co*ez;B1[z]=-m*si*ez;B2[z]=-m*m*co*ez
        return B,B1,B2

    @staticmethod
    def project(F,B):
        norm=np.sum(B*B,axis=(1,2))
        return np.einsum('npc,kpc->kn',F,B,optimize=True)/norm[:,None]

    def base(self,s,derivative=0):
        a,ap,app=self.profile(s);z=(a,ap,app)[derivative]
        out=np.zeros((self.n,len(np.atleast_1d(s))));out[0]=z
        return out

    def modal(self,y):return y[1:self.M+1],y[2*self.M+1:]

    def seed(self,nodes):
        p=np.zeros(self.M)
        if self.M>=2:p[1]=1.81124*self.q**2/self.pscale[1]
        x=np.linspace(0,self.end,nodes)
        def rhs(s,y):
            a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return [-(3*v*y[0]+4*b*y[1])/a,3*v*v*y[0]/(a*b)+4*v*y[1]/a]
        lin=solve_ivp(rhs,[0,self.end],[1/self.rhos[0],1],method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True,max_step=self.period/100)
        f,g=lin.sol(x);y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/2;y[2*self.M+1]=g
        return x,y,p

    def jacobian_check(self):
        x=np.array([.031,.49,1.11,1.79,2.31])%self.end
        y=np.zeros((self.n,len(x)));y[self.iz]=.2;y[1]=.03
        rng=np.random.default_rng(20261108);v=rng.normal(size=y.shape)
        J,_=self.fun_jac(x,y,np.zeros(self.M));pred=np.einsum('ijk,jk->ik',J,v)
        step=1e-25;actual=self.fun(x,y.astype(complex)+1j*step*v,np.zeros(self.M)).imag/step
        return dict(max_abs=float(np.max(abs(pred-actual))),relative=float(np.max(abs(pred-actual))/max(1,np.max(abs(actual)))))


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--modes',type=int,default=2)
    p.add_argument('--amplitude',type=float,default=.001);p.add_argument('--delta',type=float,default=1.)
    p.add_argument('--v-up',type=float,default=.93);p.add_argument('--v-down',type=float,default=.93)
    p.add_argument('--ramp',type=float,default=.2);p.add_argument('--cycles',type=int,default=1)
    p.add_argument('--angular',type=int,default=128);p.add_argument('--nodes',type=int,default=101)
    p.add_argument('--max-nodes',type=int,default=3000);p.add_argument('--tol',type=float,default=2e-7)
    p.add_argument('--bc-tol',type=float,default=2e-7);p.add_argument('--terminal-c4',type=float,default=0.)
    p.add_argument('--basis',choices=['cartesian','cylindrical'],default='cylindrical')
    p.add_argument('--interpolant',choices=['cubic','quintic'],default='quintic')
    p.add_argument('--restart');p.add_argument('--audit-points',type=int,default=401);p.add_argument('--audit-angular',type=int,default=512)
    args=p.parse_args();cls=CylindricalPrefix if args.basis=='cylindrical' else Prefix
    obj=cls(args.modes,args.amplitude,args.delta,args.v_up,args.v_down,args.ramp,args.cycles,args.angular,args.terminal_c4)
    initial=None
    if args.restart:
        old=load_checkpoint(args.restart)
        oc=old['config'];oldM=oc['modes'];oldq=oc['amplitude']
        ocls=CylindricalPrefix if oc.get('basis','cartesian')=='cylindrical' else Prefix
        oldobj=ocls(oldM,oldq,oc['delta'],oc['v_up'],oc['v_down'],oc['ramp'],oc['cycles'],args.angular,oc['terminal_c4'])
        x=np.array(old['mesh']);P=PPoly.construct_fast(np.array(old['pp_coefficients']),x,extrapolate=True,axis=1)
        if any(abs(getattr(obj,k)-getattr(oldobj,k))>1e-12 for k in ('delta','vu','vd','eps')):
            raise ValueError('A restart must use the same fixed radius profile')
        if obj.cycles<oldobj.cycles:raise ValueError('Restart cycle shortening is not implemented')
        def project_old(t):return obj.project(oldobj.values(P(t),oldobj.B),obj.B)
        if obj.cycles==oldobj.cycles:
            trial=np.unique(np.r_[x,np.linspace(0,obj.end,args.nodes)]) if len(x)<args.nodes else x
            xnew=trial[np.r_[True,np.diff(trial)>1e-11*obj.end]];y=project_old(xnew)
        else:
            if args.basis!='cylindrical':raise ValueError('Cycle extension requires the complete physical-mode basis')
            oldlast=(oldobj.cycles-1)*oldobj.period
            lastmesh=x[x>=oldlast]-oldlast
            if lastmesh[0]>1e-11:lastmesh=np.r_[0.,lastmesh]
            shapes=[project_old(x)];meshes=[x];lastvalue=shapes[-1][:,-1]
            base_last=project_old(oldlast+lastmesh);lam=obj.multipliers[0]
            order=np.r_[2,np.arange(1,obj.M+1),np.arange(1,obj.M+1),np.arange(1,obj.M+1)]
            for extra in range(1,obj.cycles-oldobj.cycles+1):
                scale=lam**(extra*order);part=base_last*scale[:,None]
                correction=lastvalue-part[:,0];tau=lastmesh/obj.period
                part+=correction[:,None]*(1-tau)[None,:]**3
                meshes.append(lastmesh[1:]+(oldobj.cycles+extra-1)*obj.period)
                shapes.append(part[:,1:]);lastvalue=part[:,-1]
            xnew=np.concatenate(meshes);y=np.concatenate(shapes,axis=1)
        par=np.zeros(obj.M);oldpar=np.array(old['parameters']);par[0]=oldpar[0]*(obj.q/oldq)**2
        for j in range(1,min(oldM,obj.M)):
            # Preserve the natural order coefficient under amplitude continuation.
            par[j]=oldpar[j]*max(oldq**(j+1),1e-8)*(obj.q/oldq)**(j+1)/obj.pscale[j]
        x=xnew
    else:x,y,par=obj.seed(args.nodes)
    check=obj.jacobian_check();tic=time.perf_counter()
    try:
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,
                      fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=1)
        if not np.all(np.isfinite(sol.sol.c)) or not np.all(np.isfinite(sol.rms_residuals)):
            raise FloatingPointError('Nonfinite collocation state/residual; no geometric audit accepted')
        if args.interpolant=='quintic':sol.sol=obj.c2_interpolant(sol)
        audit=obj.audit_streamed(sol,args.audit_points,args.audit_angular)
        out=dict(author='solver_audit; GPT-6 Astra Pro; AI-assisted',scope=__doc__,config=vars(args),
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            success=bool(sol.success),status=int(sol.status),message=sol.message,seconds=time.perf_counter()-tic,
            calls=obj.calls,nodes=len(sol.x),jacobian_check=check,parameters=sol.p.tolist(),core=obj.parameters(sol.p),
            stable_slopes=obj.rhos.tolist(),stable_multipliers=obj.multipliers,summary=audit,
            mesh=sol.x.tolist(),pp_coefficients=sol.sol.c,
            max_rms_collocation_residual=float(np.max(sol.rms_residuals)))
    except Exception as exc:
        out=dict(author='solver_audit',config=vars(args),success=False,message=repr(exc),seconds=time.perf_counter()-tic,
                 jacobian_check=check,calls=obj.calls)
    out=save_checkpoint(args.out,out)
    print(json.dumps({k:out[k] for k in out if k not in ('scope','mesh','values','pp_coefficients')},indent=2),flush=True)


if __name__=='__main__':main()
