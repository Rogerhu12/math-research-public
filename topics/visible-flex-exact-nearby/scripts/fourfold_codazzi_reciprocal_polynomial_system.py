#!/usr/bin/env python3
"""Complete finite Fourier system in u=alpha*U, v=1/Cref+alpha*V.

B=u/v, C=1/v. The interior right-hand side is polynomial of degree three,
with exact Fourier support at most 3M for finite M input. No sqrt(-K) is
used, so the same algebra crosses the true turning points. This does not
assert well-posed Cauchy evolution there.

The diagnostic boundary model retains the same physical waist amplitude,
all waist B rows, outer/waist C mean choice and every retained R74 LINEAR
Robin row. Its rational boundary tail and nonlinear regular correction
remain separate: finite boundary success is not a full regular certificate.
"""
from __future__ import annotations
import time
import numpy as np
from fourfold_codazzi_compact_metric_branch_probe import CompactNormalized


class ReciprocalPolynomial(CompactNormalized):
    def __init__(self,geometry,modes,angles,body,graft,*,mean_boundary='outer',right=3.125):
        super().__init__(geometry,modes,angles,body,graft)
        if angles<=6*modes:raise ValueError('the full cubic Fourier support requires angles > 6*modes')
        if mean_boundary not in ('waist','outer'):raise ValueError('unknown physical mean row')
        self.mean_boundary=mean_boundary;self.right_boundary=float(right)
        self.qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
        self.all_base_cache={}
        self.physical_fft_frequency=4*np.fft.fftfreq(angles,1/angles)

    def base(self,r):
        r=np.atleast_1d(np.asarray(r,dtype=float));key=r.tobytes()
        if key not in self.all_base_cache:self.all_base_cache[key]=super().base(r)
        return self.all_base_cache[key]

    def data(self,*args,**kwargs):
        raise TypeError('reciprocal coordinates require reciprocal_data; the old B,c data contract is invalid')

    def fields_with_derivatives(self,y):
        y=np.asarray(y,dtype=float)
        if y.ndim==1:y=y[:,None]
        m=self.modes;N=self.angular_grid
        if y.shape[0]!=2*m+1:raise ValueError('incomplete reciprocal Fourier state')
        U=np.zeros((N,y.shape[1]),dtype=complex);V=np.zeros_like(U)
        U[1:m+1]=-.5j*y[:m];U[-m:]=.5j*y[:m][::-1]
        V[0]=y[m];V[1:m+1]=.5*y[m+1:];V[-m:]=.5*y[m+1:][::-1]
        freq=1j*self.physical_fft_frequency[:,None]
        return (np.fft.ifft(U,axis=0).real*N,np.fft.ifft(V,axis=0).real*N,
                np.fft.ifft(freq*U,axis=0).real*N,np.fft.ifft(freq*V,axis=0).real*N)

    def fields(self,y):return self.fields_with_derivatives(y)[:2]

    def project(self,odd,even):
        m=self.modes;N=self.angular_grid
        fo=np.fft.fft(odd,axis=0)/N;fe=np.fft.fft(even,axis=0)/N
        out=np.concatenate([-2*fo.imag[1:m+1],2*fe.real[:m+1]],axis=0)
        out[m]*=.5
        return out

    def reciprocal_data(self,r,y,p):
        t=self.controlled(r,float(p[0]));a,g,b,K,ell,Cr,dg,dl,dCr=t
        U,V,Ut,Vt=self.fields_with_derivatives(y)
        s=1/Cr;ds=-dCr/(Cr*Cr);dK=dl*Cr*Cr+2*ell*Cr*dCr
        v=s+self.alpha*V
        return dict(target=t,U=U,V=V,Ut=Ut,Vt=Vt,s=s,ds=ds,dK=dK,v=v)

    def physical_normalized_fields(self,r,y,p):
        z=self.reciprocal_data(r,y,p);Cr=z['target'][5];v=z['v']
        if np.any(v==0):raise ZeroDivisionError('actual reciprocal chart v vanishes')
        return z['U']/v,-Cr*z['V']/v

    def actual_fields(self,r,y,p):
        z=self.reciprocal_data(r,y,p);v=z['v']
        if np.any(v==0):raise ZeroDivisionError('actual reciprocal chart v vanishes')
        return self.alpha*z['U']/v,1/v

    def physical_rhs(self,r,y,p):
        z=self.reciprocal_data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=z['target']
        U,V,Ut,Vt,s,v=(z[k] for k in ('U','V','Ut','Vt','s','v'));al=self.alpha
        T=3*s*s*V+3*al*s*V*V+al*al*V*V*V
        fu=g*(al*U*Ut+K*v*Vt)-b*U*(1+al*al*U*U+K*v*v)
        fv=g*(al*U*Vt-v*Ut)+b*(V-K*T-al*v*U*U)
        return fu,fv,z

    def evaluate(self,r,y,p):
        fu,fv,z=self.physical_rhs(r,y,p);self.calls+=1
        if time.monotonic()-self.last_log>20:
            with np.errstate(divide='ignore',invalid='ignore'):C=1/z['v']
            print(dict(chart='reciprocal_polynomial',amplitude=self.alpha,nu=float(p[0]),
                rhs_calls=self.calls,jac_calls=self.jac_calls,radial_nodes=len(np.atleast_1d(r)),
                sampled_v_min=float(np.min(z['v'])),sampled_v_max=float(np.max(z['v'])),
                sampled_C_min=float(np.min(C)),sampled_C_max=float(np.max(C))),flush=True)
            self.last_log=time.monotonic()
        return self.project(fu,fv)

    def linear_fields(self,r,y,p):
        z=self.reciprocal_data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=z['target']
        U,V,Ut,Vt,s,ds,dK,v=(z[k] for k in ('U','V','Ut','Vt','s','ds','dK','v'));al=self.alpha
        a11=g*al*U;a12=g*K*v;a21=-g*v;a22=a11
        b11=g*al*Ut-b*(1+3*al*al*U*U+K*v*v)
        b12=g*al*K*Vt-2*b*al*K*U*v
        b21=g*al*Vt-2*b*al*v*U
        b22=-g*al*Ut+b*(1-3*K*v*v-al*al*U*U)
        T=3*s*s*V+3*al*s*V*V+al*al*V*V*V
        fpu=dg*(al*U*Ut+K*v*Vt)+g*(dK*v+K*ds)*Vt-b*U*(dK*v*v+2*K*v*ds)
        fpv=dg*(al*U*Vt-v*Ut)-g*ds*Ut+b*(-dK*T-K*(6*s*V+3*al*V*V)*ds-al*ds*U*U)
        return (a11,a12,a21,a22,b11,b12,b21,b22,fpu,fpv)

    def multiplication_matrix(self,field,*,out_odd,in_odd):
        """Full trapezoidal multiplication, without dropping Fourier entries."""
        m=self.modes;N=self.angular_grid;f=np.fft.fft(field,axis=0)/N
        rows=np.arange(1 if out_odd else 0,m+1)[:,None]
        cols=np.arange(1 if in_odd else 0,m+1)[None,:]
        coeff=f.real if out_odd==in_odd else f.imag
        if in_odd:value=coeff[(rows-cols)%N]-coeff[(rows+cols)%N]
        else:value=coeff[(rows-cols)%N]+coeff[(rows+cols)%N]
        if out_odd and not in_odd:value=-value
        if not out_odd:value[0]*=.5
        return value

    def jacobian(self,r,y,p):
        a11,a12,a21,a22,b11,b12,b21,b22,fpu,fpv=self.linear_fields(r,y,p)
        m=self.modes;n=2*m+1;nr=np.asarray(y).shape[1];freq=self.frequency[None,:,None]
        mul=self.multiplication_matrix
        Juu=mul(b11,out_odd=True,in_odd=True)+mul(a11,out_odd=True,in_odd=False)[:,1:]*freq
        Juv=mul(b12,out_odd=True,in_odd=False)
        Juv[:,1:]-=mul(a12,out_odd=True,in_odd=True)*freq
        Jvu=mul(b21,out_odd=False,in_odd=True)+mul(a21,out_odd=False,in_odd=False)[:,1:]*freq
        Jvv=mul(b22,out_odd=False,in_odd=False)
        Jvv[:,1:]-=mul(a22,out_odd=False,in_odd=True)*freq
        out=np.empty((n,n,nr));out[:m,:m]=Juu;out[:m,m:]=Juv
        out[m:,:m]=Jvu;out[m:,m:]=Jvv
        self.jac_calls+=1
        return out,self.project(fpu,fpv)[:,None,:]

    def full_action(self,r,y,p):
        """Independent full FFT action for the complete block backward gate."""
        a11,a12,a21,a22,b11,b12,b21,b22,fpu,fpv=self.linear_fields(r,y,p)
        def action(delta,parameter):
            dU,dV,dUt,dVt=self.fields_with_derivatives(delta)
            return self.project(a11*dUt+a12*dVt+b11*dU+b12*dV+fpu*parameter,
                a21*dUt+a22*dVt+b21*dU+b22*dV+fpv*parameter)
        return action

    def boundary_jet(self,r,y,p):
        z=self.reciprocal_data([r],np.asarray(y)[:,None],p)
        Cr=z['target'][5];dCr=z['target'][8];s=z['s'];ds=z['ds'];v=z['v'];U=z['U'];V=z['V']
        if np.any(v==0):raise ZeroDivisionError('the physical boundary v vanishes')
        al=self.alpha;m=self.modes;n=2*m+1
        values=self.project(U/v,-Cr*V/v)[:,0]
        ju=np.zeros((m,n));jv=np.zeros((m+1,n))
        ju[:,:m]=self.multiplication_matrix(1/v,out_odd=True,in_odd=True)[:,:,0]
        ju[:,m:]=self.multiplication_matrix(-al*U/(v*v),out_odd=True,in_odd=False)[:,:,0]
        jv[:,m:]=self.multiplication_matrix(-1/(v*v),out_odd=False,in_odd=False)[:,:,0]
        pars=self.project(-U*ds/(v*v),-dCr*V*(2*s+al*V)/(v*v))[:,0]
        return values[:m],values[m:],ju,jv,pars[:m],pars[m:]

    def boundary(self,left,right,p):
        bl,cl,*_=self.boundary_jet(0.,left,p)
        br,cr,*_=self.boundary_jet(self.right_boundary,right,p)
        m=self.modes;mean=cl[0] if self.mean_boundary=='waist' else cr[0]
        return np.r_[left[:m],mean,cl[1]+1,br+self.qstar*cr[1:]]

    def boundary_jac(self,left,right,p):
        bl,cl,jbl,jcl,pbl,pcl=self.boundary_jet(0.,left,p)
        br,cr,jbr,jcr,pbr,pcr=self.boundary_jet(self.right_boundary,right,p)
        m=self.modes;n=2*m+1;jl=np.zeros((n+1,n));jr=np.zeros_like(jl);jp=np.zeros((n+1,1))
        jl[np.arange(m),np.arange(m)]=1
        if self.mean_boundary=='waist':jl[m]=jcl[0];jp[m,0]=pcl[0]
        else:jr[m]=jcr[0];jp[m,0]=pcr[0]
        jl[m+1]=jcl[1];jp[m+1,0]=pcl[1]
        jr[m+2:]=jbr+self.qstar*jcr[1:];jp[m+2:,0]=pbr+self.qstar*pcr[1:]
        return jl,jr,jp

    def rhs_tail(self,r,y,p):
        fu,fv,z=self.physical_rhs(r,y,p);N=self.angular_grid;m=self.modes
        f=np.fft.fft(np.stack((fu,fv)),axis=1)/N
        idx=np.abs(np.fft.fftfreq(N,1/N));tail=idx>m;outside=idx>3*m
        return dict(normalized_polynomial_rhs_tail_l1=float(np.max(np.sum(abs(f[:,tail]),axis=1))),
            roundoff_beyond_exact_cubic_support_l1=float(np.max(np.sum(abs(f[:,outside]),axis=1))),
            exact_polynomial_support_index=3*m,physical_frequency_max=12*m,
            all_cubic_coefficients_resolved_by_grid=bool(N>6*m))
