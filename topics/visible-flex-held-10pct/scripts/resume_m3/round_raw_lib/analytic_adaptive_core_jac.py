"""Analytic core-control Jacobian for the exact lift in an adaptive angle chart.
Includes the coordinate convection v*d(delta_X_psi). Physical profile-control
columns remain centered differences. No residual or geometry guard is changed.
"""
import numpy as np
from exact_lift_parameter_jac import parameter_jets

def install(BVP,window=(.5,.9)):
 old=BVP.fun_jac
 def fun_jac(self,t,y,p):
  self.initial(p);f=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=f.fun_jac(s,y,p);M=len(p);PJ=np.zeros((self.n,M,len(t)));N=f.B.shape[1];key=(self._core_key,N)
  if key!=getattr(self,'_adaptive_core_jac_key',None):
   ang=f.angular(N);d0,d1,d2=parameter_jets(self._core,ang[1]);rho=ang[2][None,:,None];rhop=ang[3][None,:,None]
   derivatives=[d0,d1*rho,d2*rho*rho+d1*rhop];scales=np.r_[self.support_amplitude if self.fixed else 0.,self.pscale];fields=[]
   for derivative,B in zip(derivatives,(f.B,f.B1,f.B2)):
    fields.append(derivative*scales[:,None,None]-f.values(self.q*self._initial_jac,B))
   self._adaptive_core_jac_fields=fields;self._adaptive_core_jac_key=key
  H,H1,H2=self._adaptive_core_jac_fields;a,v,_=f.profile(s);lo,hi=window;span=(hi-lo)*f.prefix_end;x=np.clip((s-lo*f.prefix_end)/span,0.,1.);chi=1-x**3*(10-15*x+6*x*x);chip=-30*x*x*(1-x)**2/span;h=a*chi;hp=v*chi+a*chip
  for first in range(0,len(s),64):
   sl=slice(first,first+64);fr=f.frame(s[sl],self.q*y[:,sl])
   for j in range(0 if self.fixed else 1,M):
    d1=h[sl,None,None]*H1[j][None,:,:];d2=h[sl,None,None]*H2[j][None,:,:]
    dV=f.frame_jvp(fr,d1,d2)+fr['geo']['v'][:,:,None]*d1
    PJ[:,j,sl]=ds[sl][None,:]*f.project(dV-hp[sl,None,None]*H[j][None,:,:],f.B)/self.q
  if not self.fixed:
   step=2e-6*max(.1,self.cfg['delta']+p[0]);plus=p.copy();minus=p.copy();plus[0]+=step;minus[0]-=step;PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step);self.initial(p)
  return ds[None,None,:]*J,PJ
 BVP.fun_jac=fun_jac;return old
