#!/usr/bin/env python3
"""Complete finite moving-curvature-angle equations and physical moments.

u=alpha*U, v=s+alpha*V now use the moving angle phi. The full nonlinear
drift keeps its degree-2M intermediate support before any degree-M output
projection. All mean and parameter columns and physical boundary moment
derivatives remain. Boundary quadrature and infinite tails are unpaid
floating errors here; N>6M dealiasses only the cubic interior.
"""
from __future__ import annotations
import time
import numpy as np
from fourfold_codazzi_reciprocal_cap_cut_system import ReciprocalCapCut


COORDINATES='moving phi: u=alpha*U; v=1/Cref_nu+alpha*V; theta_phi=v/mean_phi(v); B=u/v; C=1/v'


class MovingPolynomial(ReciprocalCapCut):
    radial_batch=16

    def primitive(self,field):
        """The complete mean-zero fourfold primitive, without an M cutoff."""
        field=np.asarray(field);f=np.fft.fft(field,axis=0)
        shape=(self.angular_grid,)+(1,)*(field.ndim-1)
        divisor=(1j*self.physical_fft_frequency).reshape(shape)
        out=np.zeros_like(f);out[1:]=f[1:]/divisor[1:]
        return np.fft.ifft(out,axis=0).real

    def moving_data(self,r,y,p):
        y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        z=super().reciprocal_data(r,y,p)
        K=z['target'][3];beta=z['target'][2]
        z['mean']=z['s']+self.alpha*y[self.modes]
        z['S']=self.alpha**2*z['U']**2+K*z['v']**2
        z['drift']=-beta*self.primitive(z['S'])
        return z

    def physical_normalized_fields(self,*args,**kwargs):
        raise TypeError('moving-angle fields are not sampled at uniform physical theta; use complete boundary moments')

    def moving_rhs(self,r,y,p):
        z=self.moving_data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=z['target']
        U,V,Ut,Vt,s,v,m,d=(z[k] for k in ('U','V','Ut','Vt','s','v','mean','drift'))
        al=self.alpha;T=3*s*s*V+3*al*s*V*V+al*al*V*V*V
        fu=d*Ut+g*m*K*Vt-b*U*(1+al*al*U*U+K*v*v)
        fv=d*Vt-g*m*Ut+b*(V-K*T-al*v*U*U)
        return fu,fv,z

    def physical_rhs(self,*args,**kwargs):
        raise TypeError('the physical-theta reciprocal RHS is not the moving-phi RHS')

    def evaluate(self,r,y,p):
        r=np.atleast_1d(np.asarray(r,dtype=float));y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        if y.shape!=(2*self.modes+1,len(r)):raise ValueError('incomplete moving finite state')
        out=np.empty_like(y);vmin=np.inf;vmax=-np.inf
        for start in range(0,len(r),self.radial_batch):
            stop=min(start+self.radial_batch,len(r))
            fu,fv,z=self.moving_rhs(r[start:stop],y[:,start:stop],p)
            out[:,start:stop]=self.project(fu,fv)
            vmin=min(vmin,float(np.min(z['v'])));vmax=max(vmax,float(np.max(z['v'])))
        self.calls+=1
        if time.monotonic()-self.last_log>20:
            print(dict(chart='complete_moving_phi',amplitude=self.alpha,nu=float(p[0]),
                rhs_calls=self.calls,jac_calls=self.jac_calls,radial_nodes=len(r),
                sampled_v_min=vmin,sampled_v_max=vmax),flush=True)
            self.last_log=time.monotonic()
        return out

    def moving_linear_fields(self,r,y,p):
        z=self.moving_data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=z['target']
        U,V,Ut,Vt,s,ds,dK,v,m,d=(z[k] for k in ('U','V','Ut','Vt','s','ds','dK','v','mean','drift'))
        al=self.alpha;ones=np.ones_like(U)
        z.update(a11=d,a12=ones*(g*m*K),a21=-ones*(g*m),a22=d,
            b11=-b*(1+3*al*al*U*U+K*v*v),b12=-2*b*al*K*U*v,
            b21=-2*b*al*v*U,b22=b*(1-3*K*v*v-al*al*U*U))
        dSnu=dK*v*v+2*K*v*ds;dnu=-b*self.primitive(dSnu)
        T=3*s*s*V+3*al*s*V*V+al*al*V*V*V
        z['fpu']=dnu*Ut+(dg*m*K+g*ds*K+g*m*dK)*Vt-b*U*dSnu
        z['fpv']=dnu*Vt-(dg*m+g*ds)*Ut+b*(-dK*T-K*(6*s*V+3*al*V*V)*ds-al*ds*U*U)
        return z

    def rectangular_multiplication(self,field,*,out_odd,in_odd,out_modes,in_modes):
        """All Toeplitz and Hankel entries, including the exact mean row."""
        N=self.angular_grid;f=np.fft.fft(field,axis=0)/N
        rows=np.arange(1 if out_odd else 0,out_modes+1)[:,None]
        cols=np.arange(1 if in_odd else 0,in_modes+1)[None,:]
        coeff=f.real if out_odd==in_odd else f.imag
        value=coeff[(rows-cols)%N]+(-1 if in_odd else 1)*coeff[(rows+cols)%N]
        if out_odd and not in_odd:value=-value
        if not out_odd:value[0]*=.5
        return value

    def jacobian(self,r,y,p):
        z=self.moving_linear_fields(r,y,p);m=self.modes;n=2*m+1
        nr=np.asarray(y).shape[1];freq=self.frequency[None,:,None]
        def mul(f,*,out_odd,in_odd):
            return self.rectangular_multiplication(f,out_odd=out_odd,in_odd=in_odd,out_modes=m,in_modes=m)
        Juu=mul(z['b11'],out_odd=True,in_odd=True)+mul(z['a11'],out_odd=True,in_odd=False)[:,1:]*freq
        Juv=mul(z['b12'],out_odd=True,in_odd=False)
        Juv[:,1:]-=mul(z['a12'],out_odd=True,in_odd=True)*freq
        Jvu=mul(z['b21'],out_odd=False,in_odd=True)+mul(z['a21'],out_odd=False,in_odd=False)[:,1:]*freq
        Jvv=mul(z['b22'],out_odd=False,in_odd=False)
        Jvv[:,1:]-=mul(z['a22'],out_odd=False,in_odd=True)*freq
        out=np.empty((n,n,nr));out[:m,:m]=Juu;out[:m,m:]=Juv;out[m:,:m]=Jvu;out[m:,m:]=Jvv
        beta=z['target'][2];K=z['target'][3];al=self.alpha
        # delta d=-beta I(2 alpha^2 U deltaU+2 alpha K v deltaV).
        # The intermediate has EVERY mode through 2M. Truncating here to M
        # would change the complete finite Jacobian after the final product.
        su=self.rectangular_multiplication(2*al*al*z['U'],out_odd=False,in_odd=True,out_modes=2*m,in_modes=m)[1:]
        sv=self.rectangular_multiplication(2*al*K*z['v'],out_odd=False,in_odd=False,out_modes=2*m,in_modes=m)[1:]
        dd=np.concatenate((su,sv),axis=1)*(-beta[None,None,:]/(4*np.arange(1,2*m+1))[:,None,None])
        tu=self.rectangular_multiplication(z['Ut'],out_odd=True,in_odd=True,out_modes=m,in_modes=2*m)
        tv=self.rectangular_multiplication(z['Vt'],out_odd=False,in_odd=True,out_modes=m,in_modes=2*m)
        out+=np.einsum('ikr,kjr->ijr',np.concatenate((tu,tv),axis=0),dd,optimize=True)
        # mean(v)=s+alpha V0: this entire rank-one column must remain.
        g=z['target'][1]
        out[:,m,:]+=self.project(al*g*K*z['Vt'],-al*g*z['Ut'])
        self.jac_calls+=1
        return out,self.project(z['fpu'],z['fpv'])[:,None,:]

    def full_action(self,r,y,p):
        """Independent full FFT action; no rectangular Jacobian is reused."""
        z=self.moving_linear_fields(r,y,p);al=self.alpha;g=z['target'][1];beta=z['target'][2];K=z['target'][3]
        def action(delta,parameter):
            dU,dV,dUt,dVt=self.fields_with_derivatives(delta)
            dd=-beta*self.primitive(2*al*al*z['U']*dU+2*al*K*z['v']*dV)
            dm=al*np.asarray(delta)[self.modes]
            fu=z['a11']*dUt+z['a12']*dVt+z['b11']*dU+z['b12']*dV+dd*z['Ut']+g*K*z['Vt']*dm+z['fpu']*parameter
            fv=z['a21']*dUt+z['a22']*dVt+z['b21']*dU+z['b22']*dV+dd*z['Vt']-g*z['Ut']*dm+z['fpv']*parameter
            return self.project(fu,fv)
        return action

    def boundary_jet(self,r,y,p):
        """Complete quadrature-defined physical b,c moments and every column."""
        if self.alpha<=0:raise ValueError('this moving physical-moment implementation requires alpha>0')
        z=super().reciprocal_data([r],np.asarray(y)[:,None],p)
        al=self.alpha;modes=self.modes;n=2*modes+1;N=self.angular_grid
        U=z['U'][:,0];V=z['V'][:,0];s=float(z['s'][0]);ds=float(z['ds'][0])
        Cr=float(z['target'][5][0]);dCr=float(z['target'][8][0]);m=s+al*float(y[modes])
        if m==0 or np.any(z['v']>=0):raise ValueError('the real moving boundary chart is not negative')
        phi=(np.pi/2)*np.arange(N)/N;IV=self.primitive(V)
        theta=phi+al*IV/m;k=self.frequency[:,None]
        ss=np.sin(k*phi);cc=np.cos(k*phi)
        st=np.sin(k*theta);ct=np.cos(k*theta)
        bv=2*np.mean(st*U,axis=1)/m
        cv=np.r_[-Cr*y[modes]/m,2*np.mean(ct,axis=1)/(al*m)]
        # Column zero of the even state is its true mean, not a projected-out row.
        thetaV=np.zeros((N,modes+1));thetaV[:,1:]=al/m*(ss/k).T
        thetaV[:,0]=-al*al*IV/(m*m)
        jb=np.zeros((modes,n));jc=np.zeros((modes+1,n))
        jb[:,:modes]=(2/(m*N))*(st@ss.T)
        jb[:,modes:]=(2/(m*N))*((k*ct*U)@thetaV)
        jb[:,modes]-=al*bv/m
        jc[1:,modes:]=(-2/(al*m*N))*((k*st)@thetaV)
        jc[1:,modes]-=al*cv[1:]/m
        jc[0,modes]=-1/(m*m)
        theta_nu=-al*IV*ds/(m*m)
        pb=-ds*bv/m+(2/m)*np.mean(k*ct*U*theta_nu,axis=1)
        pc=np.r_[-dCr*y[modes]*(2*s+al*y[modes])/(m*m),
            -ds*cv[1:]/m-(2/(al*m))*np.mean(k*st*theta_nu,axis=1)]
        return bv,cv,jb,jc,pb,pc

    def rhs_tail(self,r,y,p):
        fu,fv,z=self.moving_rhs(r,y,p);N=self.angular_grid;m=self.modes
        f=np.fft.fft(np.stack((fu,fv)),axis=1)/N
        modes=abs(np.fft.fftfreq(N,1/N))
        return dict(normalized_complete_moving_rhs_tail_l1=float(np.max(np.sum(abs(f[:,modes>m]),axis=1))),
            roundoff_beyond_exact_cubic_support_l1=float(np.max(np.sum(abs(f[:,modes>3*m]),axis=1))),
            exact_polynomial_support_index=3*m,complete_intermediate_drift_support_index=2*m,
            all_cubic_coefficients_resolved_by_grid=bool(N>6*m),boundary_quadrature_still_unpaid=True)
