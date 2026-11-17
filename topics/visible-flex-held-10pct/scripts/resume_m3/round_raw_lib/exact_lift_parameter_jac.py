"""Analytical fixed-material core jets for the untruncated planar reference.

This removes parameter finite differences for the core variables.  It does
not turn floating quadrature or a finite collocation rank into a proof.
The post-H metric control is still differentiated by a centered difference.
"""
import numpy as np


def parameter_jets(core,theta):
    """Derivatives of Gamma, Gamma_u, Gamma_uu at fixed material u."""
    g=core.rho_material_jets(theta);phi=g['phi'];rho=g['rho'];rp=g['rho_phi']
    f,f1,f2,f3=core._basis(phi);U,_=core.unit_geometry(phi)
    delta_arc=np.concatenate((U[None,:],f+f2-core.f0[:,None]-core.f20[:,None]),axis=0)
    delta_rho_normal=np.concatenate((core.unit_rho(phi)[None,:],f1+f3),axis=0)
    delta_phi=-delta_arc/rho[None,:]
    delta_rho_fixed=delta_rho_normal+delta_phi*rp[None,:]
    n=g['normal'][None,:,:];t=g['Ft'][None,:,:]
    d0=core.parameter_derivatives(theta)
    d1=-delta_phi[:,:,None]*n
    d2=-delta_phi[:,:,None]*t/rho[None,:,None]+delta_rho_fixed[:,:,None]*n/rho[None,:,None]**2
    return d0,d1,d2


def install_analytic_lift_jac(BVP,window=(.25,.6),control='stop_acceleration'):
    original=BVP.fun_jac
    def fun_jac(self,t,y,p):
        self.initial(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=f.fun_jac(s,y,p)
        if f.warp_e!=0:raise ValueError('Analytical reference parameter jets require the physical angle chart')
        M=len(p);PJ=np.zeros((self.n,M,len(t)));N=f.B.shape[1]
        key=(self._core_key,N)
        if key!=getattr(self,'_analytic_lift_parameter_key',None):
            theta=2*np.pi*np.arange(N)/N
            dj=parameter_jets(self._core,theta)
            scales=np.r_[self.support_amplitude if self.fixed else 0.,self.pscale]
            fields=[]
            for derivative,B in zip(dj,(f.B,f.B1,f.B2)):
                full=derivative*scales[:,None,None]
                projected=f.values(self.q*self._initial_jac,B)
                fields.append(full-projected)
            self._analytic_lift_parameter_fields=fields;self._analytic_lift_parameter_key=key
        H,H1,H2=self._analytic_lift_parameter_fields
        a,v,_=f.profile(s);lo,hi=window;span=(hi-lo)*f.prefix_end
        x=np.clip((s-lo*f.prefix_end)/span,0.,1.)
        chi=1-x**3*(10-15*x+6*x*x);chip=-30*x*x*(1-x)**2/span
        h=a*chi;hp=v*chi+a*chip
        for first in range(0,len(s),64):
            sl=slice(first,first+64);fr=f.frame(s[sl],self.q*y[:,sl])
            for j in range(0 if self.fixed else 1,M):
                d1=h[sl,None,None]*H1[j][None,:,:]
                d2=h[sl,None,None]*H2[j][None,:,:]
                dV=f.frame_jvp(fr,d1,d2)
                ds1=hp[sl,None,None]*H[j][None,:,:]
                PJ[:,j,sl]=ds[sl][None,:]*f.project(dV-ds1,f.B)/self.q
        if not self.fixed:
            value=self.cfg['window_parameters'][control]+p[0]
            step=2e-6*max(1.,abs(value));plus=p.copy();minus=p.copy();plus[0]+=step;minus[0]-=step
            PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.initial(p)
        return ds[None,None,:]*J,PJ
    BVP.fun_jac=fun_jac
    return original


if __name__=='__main__':
    import argparse,json,math
    from pathlib import Path
    from plateau_core import PlateauSupportCore
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    args=dict(q=.02,corrections=[.01,-.015,.02],halfwidth=.2,transition=.1,homotopy=.7,center=math.pi/3)
    core=PlateauSupportCore(**args);u=np.linspace(.017,2*np.pi-.023,257);exact=parameter_jets(core,u);rows=[]
    for j in range(4):
        step=2e-6 if j else 2e-7
        plus={**args,'corrections':args['corrections'].copy()};minus={**args,'corrections':args['corrections'].copy()}
        if j:plus['corrections'][j-1]+=step;minus['corrections'][j-1]-=step
        else:plus['q']+=step;minus['q']-=step
        P=PlateauSupportCore(**plus).evaluate(u);Q=PlateauSupportCore(**minus).evaluate(u)
        for derivative,name in enumerate(('F','Ft','Ftt')):
            finite=(P[name]-Q[name])/(2*step);error=float(np.max(abs(finite-exact[derivative][j])))
            rows.append(dict(parameter=j,derivative=derivative,absolute_error=error,scale=float(np.max(abs(exact[derivative][j])))))
    out=dict(scope=__doc__,centered_difference_checks=rows)
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
