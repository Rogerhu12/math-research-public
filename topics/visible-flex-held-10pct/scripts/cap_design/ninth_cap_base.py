"""Ninth-degree radial spline design with exact elliptic-integral angle inversion."""
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import ellipe,ellipeinc
from gauged_cap_homotopy_base import Model as Base
class Model(Base):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs);degree=9
  if self.nc<=degree:raise ValueError('nc must exceed radial degree')
  interior=np.linspace(0,1,self.nc-degree+1)[1:-1]
  knots=np.r_[np.zeros(degree+1),interior,np.ones(degree+1)]
  self.spline=BSpline(knots,np.eye(self.nc),degree,extrapolate=False);self.intervals=np.unique(knots)
  self.elliptic_parameter=1-(self.B/self.A)**2;self.a0=2*self.A*ellipe(self.elliptic_parameter)/np.pi
 def curve(self,u):
  u=np.mod(u,2*np.pi);p=self.inv(u);a,b=self.A,self.B;m=self.elliptic_parameter
  for _ in range(5):
   v=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2)
   arc=a*(ellipeinc(p+np.pi/2,m)-ellipe(m))
   p-=(arc-self.a0*u)/v
  v=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2);pp=self.a0/v;ppp=-self.a0**2*(a*a-b*b)*np.sin(p)*np.cos(p)/v**4
  c=np.stack((a*np.cos(p),b*np.sin(p),np.zeros_like(p)),axis=-1);cp=np.stack((-a*np.sin(p),b*np.cos(p),np.zeros_like(p)),axis=-1);cpp=np.stack((-a*np.cos(p),-b*np.sin(p),np.zeros_like(p)),axis=-1)
  return c,cp*pp[:,None],cpp*pp[:,None]**2+cp*ppp[:,None]
