"""Cartesian cap solve starting from a numerically integrated genuine GC prefix.

The prefix is a finite Fourier/ODE approximation, not an existence certificate.
Only the following tail is optimized; its full incoming two-jet is fixed.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipe,ellipeinc
from negative_entry_envelope_base import Model as Bounded
class Model(Bounded):
 def __init__(self,*args,prefix=.28,gc_c=4.,gc_k=10.,gc_ramp=.03,gc_n=128,**kwargs):
  kwargs.pop('bend',None);super().__init__(*args,**kwargs);self.asym=None
  self.prefix,self.gc_c,self.gc_k,self.gc_ramp,self.gc_n=prefix,gc_c,gc_k,gc_ramp,gc_n
  a,b=self.A,self.B;em=1-(b/a)**2;self.a0=2*a*ellipe(em)/np.pi;n=gc_n;u=np.arange(n)*2*np.pi/n;p=self.inv(u)
  for _ in range(5):
   h=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2);p-=(a*(ellipeinc(p+np.pi/2,em)-ellipe(em))-self.a0*u)/h
  h=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2)
  X=np.stack((a*np.cos(p),b*np.sin(p),np.zeros(n)))
  e1=np.tile([0.,0.,1.],(n,1)).T;e2=np.stack((-a*np.sin(p)/h,b*np.cos(p)/h,np.zeros(n)))
  M=np.zeros(n);N=self.a0*self.a0*a*b/h**3;y0=np.r_[M,N,X.ravel(),e1.ravel(),e2.ravel()];freq=np.fft.fftfreq(n,1/n);self.freq=freq
  def du(x):return np.fft.ifft(1j*freq*np.fft.fft(x,axis=-1),axis=-1).real
  def rhs(s,y):
   aa,ap,app=self.profile(s);M=y[:n];N=y[n:2*n];L=(M*M-aa*app)/N;e1=y[5*n:8*n].reshape(3,n);e2=y[8*n:11*n].reshape(3,n);normal=np.cross(e1.T,e2.T).T
   return np.r_[du(L)-ap/aa*M,du(M)+ap/aa*N+aa*ap*L,e1.ravel(),(normal*L).ravel(),(normal*M/aa).ravel()]
  def event(s,y):return np.min(y[n:2*n])-.005
  event.terminal=True;event.direction=-1
  sol=solve_ivp(rhs,[0,prefix],y0,rtol=2e-10,atol=2e-11,method='DOP853',max_step=.002,dense_output=True,events=event)
  if not sol.success or sol.t[-1]<prefix-1e-12:raise RuntimeError('GC prefix failed before requested endpoint')
  y=sol.y[:,-1];aa,ap,app=self.profile(prefix);M=y[:n];N=y[n:2*n];L=(M*M-aa*app)/N;X=y[2*n:5*n].reshape(3,n);e1=y[5*n:8*n].reshape(3,n);e2=y[8*n:11*n].reshape(3,n);normal=np.cross(e1.T,e2.T).T
  self.incoming=np.stack((X,self.speed*e1,self.speed**2*normal*L))
  self.incoming_coeff=np.fft.fft(self.incoming,axis=-1)/n
  coorderr=float(np.max(np.linalg.norm(du(X)-aa*e2,axis=0)))
  self.prefix_info={'A':a,'B':b,'n':n,'prefix':prefix,'c':gc_c,'k':gc_k,'ramp':gc_ramp,'rtol':2e-10,'atol':2e-11,'nfev':sol.nfev,'coordinate_error_at_end':coorderr,'N_min':float(N.min()),'a_end':aa,'ap_end':ap,'app_end':app,'boundary_min':X.min(axis=1).tolist(),'boundary_max':X.max(axis=1).tolist()}
 def profile(self,s):
  c,k,ramp=self.gc_c,self.gc_k,self.gc_ramp
  if s<=ramp:
   q=np.pi*s/ramp
   return self.a0+c*(s*s/4+ramp*ramp/(2*np.pi*np.pi)*(np.cos(q)-1)),c*(s/2-ramp/(2*np.pi)*np.sin(q)),c*(1-np.cos(q))/2
  t=s-ramp;p0=c*ramp/2;a1=self.a0+c*ramp*ramp*(1/4-1/np.pi**2)
  return a1+p0*t+c*(1-np.cos(k*t))/k**2,p0+c*np.sin(k*t)/k,c*np.cos(k*t)
 def prepare(self,s,u):
  s,u=np.asarray(s),np.asarray(u)
  polynomials=[np.array([1,0,0,-10,15,-6]),np.array([0,0,0,10,-15,6]),np.array([0,1,0,-6,8,-3]),np.array([0,0,0,-4,7,-3]),np.array([0,0,.5,-1.5,1.5,-.5])]
  H=[[np.polynomial.polynomial.polyval(s,np.polynomial.polynomial.polyder(p,d))for p in polynomials]for d in range(3)]
  exponential=np.exp(1j*u[:,None]*self.freq[None,:])
  incoming=[np.einsum('jcn,un->juc',self.incoming_coeff*(1j*self.freq)**d,exponential,optimize=True).real for d in range(3)]
  circles=[np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1),np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1),np.stack((-np.cos(u),-np.sin(u),np.zeros_like(u)),axis=-1)]
  ez=np.array([0.,0.,1.]);geom=[]
  for ds,du in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
   h=H[ds];endpoint=self.rc*circles[du]+(self.height*ez if du==0 else 0)
   row=h[0][:,None,None]*incoming[du][0]+h[2][:,None,None]*incoming[du][1]+h[4][:,None,None]*incoming[du][2]+h[1][:,None,None]*endpoint-h[3][:,None,None]*self.speed*circles[du]
   geom.append(row)
  return dict(s=s,u=u,geom=geom,r=self.radial(s),ang=self.angles(u))
