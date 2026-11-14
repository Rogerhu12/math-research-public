from explore_inverse import *
from scipy.optimize import brentq
from scipy.integrate import quad

def real_roots(c):
 return sorted(float(z.real)for z in P.polyroots(c)if abs(z.imag)<1e-7 and 0<z.real<1)

def analytic_data(gamma,alpha):
 c=coefficients(gamma,alpha);R,A=quotients(c)
 crit=real_roots(P.polyder(R));check=np.array([0,1]+crit)
 minimum=float(min(P.polyval(check,R)))
 return c,R,A,crit,minimum

def accurate_ratio(gamma,alpha):
 c,R,A,crit,minimum=analytic_data(gamma,alpha)
 if minimum<=0:return None
 def f(t):return -(a+h*t)*P.polyval(t,A)/(h*P.polyval(t,R))
 value,error=quad(f,0,1,epsabs=2e-9,epsrel=2e-10,points=crit,limit=200)
 return value

def solve_alpha(gamma,al1):
 t=np.linspace(0,1,8193)
 _,R,_,_,_=analytic_data(gamma,[0,al1]);_,one,_,_,_=analytic_data(gamma,[1,al1]);slope=P.polysub(one,R)
 z,d=P.polyval(t,R),P.polyval(t,slope)
 lo=max(-10.,float(np.max(-z[d>1e-10]/d[d>1e-10]))) if np.any(d>1e-10)else -10.
 hi=min(10.,float(np.min(-z[d<-1e-10]/d[d<-1e-10]))) if np.any(d<-1e-10)else 10.
 if not lo<hi:return None
 margin=max(1e-8,(hi-lo)*1e-7)
 lo+=margin;hi-=margin
 target=math.log(.1/w0)
 def fun(v):
  q=accurate_ratio(gamma,[v,al1]);return None if q is None else q-target
 xs=np.linspace(lo,hi,17);prev=None
 for x in xs:
  y=fun(x)
  if y is None:continue
  if prev is not None and prev[1]*y<0:
   alpha=brentq(fun,prev[0],x,xtol=1e-12)
   return alpha
  prev=x,y
 return None

def profile(gamma,alpha,ngrid=256):
 c,R,A,crit,minimum=analytic_data(gamma,alpha)
 if minimum<=0:return None
 t=np.unique(np.r_[np.linspace(0,1,ngrid+1),crit,real_roots(A)])
 def f(s):return -(a+h*s)*P.polyval(s,A)/(h*P.polyval(s,R))
 z=[math.log(w0)];err=0
 for l,u in zip(t[:-1],t[1:]):
  v,e=quad(f,l,u,epsabs=1e-10,epsrel=2e-10,limit=80);z.append(z[-1]+v);err+=e
 z=np.array(z)
 if max(z)>100:return dict(logw_max=float(max(z)),failed='large slope')
 w=np.exp(z);r=a+h*t;k=-(r)*P.polyval(t,A)/(h*h*P.polyval(t,R))
 H=P.polyval(t,c);Hr=P.polyval(t,P.polyder(c))/h;Hrr=P.polyval(t,P.polyder(c,2))/(h*h)
 J=t*(1-t)*P.polyval(t,R)/r
 E=1+w*w;dl=-Hrr/np.sqrt(E);dn=-np.sqrt(E)*J/r;dm=2*H/r**2-2*Hr/r
 gamma_chart=J/w-4*H*w/r
 return dict(gamma=gamma,alpha=list(alpha),w_end=float(w[-1]),w_peak=float(max(w)),
  background_curvature=float(max(abs(w*k/E**1.5))),Gamma=float(max(abs(gamma_chart))),
  II_row=float(max(np.maximum(abs(dl)+abs(dm),abs(dn)+abs(dm)))),Hrr=float(max(abs(Hrr))),
  Hmax=float(max(abs(H))),Jmax=float(max(abs(J))),minimum_N_quotient=minimum,
  logarithm_quadrature_error_estimate=err,coefficients=c.tolist())

if __name__=='__main__':
 results=[]
 for gamma in [.047074026251901865,.01,.001]:
  for a1 in np.linspace(-.3,.2,26):
   alpha=solve_alpha(gamma,float(a1))
   if alpha is None:continue
   r=profile(gamma,[alpha,float(a1)])
   results.append(r)
   print(json.dumps({k:v for k,v in r.items()if k!='coefficients'}),flush=True)
 Path('root-screen-01.json').write_text(json.dumps({'scope':'Finite inverse-profile scalar screen; no continuous certificate or tail solve','results':results},indent=2)+'\n')
