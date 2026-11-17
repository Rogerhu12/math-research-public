"""Analytic constant-speed negative-curvature meridian with exact endpoint data."""
import numpy as np
from scipy.optimize import brentq
from scipy.special import ellipe,ellipeinc
from gauged_cap_homotopy_base import Model as Base
class Model(Base):
 def __init__(self,*args,bend=.4,**kwargs):
  super().__init__(*args,**kwargs);self.bend=bend
  self.em=1-(self.B/self.A)**2;self.a0=2*self.A*ellipe(self.em)/np.pi
  self.qnodes,self.qweights=np.polynomial.legendre.leggauss(128)
  s=(self.qnodes+1)/2;w=self.qweights/2;target=self.a0-self.rc
  def equation(c):
   beta,_=self.beta(s,c);return self.height*np.dot(w,np.cos(beta))+target*np.dot(w,np.sin(beta))
  probes=np.linspace(-1.2,1.2,49);roots=[]
  for l,r in zip(probes[:-1],probes[1:]):
   if equation(l)*equation(r)<0:roots.append(brentq(equation,l,r,xtol=1e-14))
  if not roots:raise ValueError('no meridian aspect root in bracket')
  self.asym=min(roots,key=abs);beta,_=self.beta(s,self.asym);self.speed=target/(-np.dot(w,np.cos(beta)))
  if self.speed<=0:raise ValueError('nonpositive reference length')
 def beta(self,s,c=None):
  if c is None:c=self.asym
  s=np.asarray(s);S=s**3*(10+s*(-15+6*s));Sp=30*s*s*(1-s)**2
  val=np.pi/2+np.pi/2*S+self.bend*np.sin(2*np.pi*S)+c*np.sin(np.pi*S)
  der=Sp*(np.pi/2+2*np.pi*self.bend*np.cos(2*np.pi*S)+np.pi*c*np.cos(np.pi*S))
  return val,der
 def curve(self,u):
  u=np.mod(u,2*np.pi);p=self.inv(u);a,b=self.A,self.B;m=self.em
  for _ in range(5):
   v=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2);arc=a*(ellipeinc(p+np.pi/2,m)-ellipe(m));p-=(arc-self.a0*u)/v
  v=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2);pp=self.a0/v;ppp=-self.a0**2*(a*a-b*b)*np.sin(p)*np.cos(p)/v**4
  c=np.stack((a*np.cos(p),b*np.sin(p),np.zeros_like(p)),axis=-1);cp=np.stack((-a*np.sin(p),b*np.cos(p),np.zeros_like(p)),axis=-1);cpp=np.stack((-a*np.cos(p),-b*np.sin(p),np.zeros_like(p)),axis=-1)
  return c,cp*pp[:,None],cpp*pp[:,None]**2+cp*ppp[:,None]
 def prepare(self,s,u):
  s,u=np.asarray(s),np.asarray(u);q=s[:,None]*(1+self.qnodes[None,:])/2
  beta,_=self.beta(q);r=self.a0+self.speed*s/2*(np.cos(beta)@self.qweights);z=self.speed*s/2*(np.sin(beta)@self.qweights)
  b,bp=self.beta(s);rp=self.speed*np.cos(b);zp=self.speed*np.sin(b);rpp=-self.speed*np.sin(b)*bp;zpp=self.speed*np.cos(b)*bp
  circles=[np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1),np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1),np.stack((-np.cos(u),-np.sin(u),np.zeros_like(u)),axis=-1)]
  curve=self.curve(u);delta=[curve[i]-self.a0*circles[i]for i in range(3)]
  polynomial=np.array([1,0,0,-10,15,-6]);H=[np.polynomial.polynomial.polyval(s,np.polynomial.polynomial.polyder(polynomial,d))for d in range(3)]
  radial=[r,rp,rpp];axial=[z,zp,zpp];ez=np.array([0.,0.,1.]);geom=[]
  for ds,du in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
   row=radial[ds][:,None,None]*circles[du]+H[ds][:,None,None]*delta[du]
   if du==0:row+=axial[ds][:,None,None]*ez
   geom.append(row)
  return dict(s=s,u=u,geom=geom,r=self.radial(s),ang=self.angles(u))
