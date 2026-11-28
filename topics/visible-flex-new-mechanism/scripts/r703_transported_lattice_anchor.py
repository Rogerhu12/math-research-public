"""Mixed actual jets of the R687 terminal field and its two recorded slope replacements."""
from __future__ import annotations
from math import factorial
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import BSpline
from numpy.polynomial import Polynomial


class Mixed:
    """Normalized Taylor coefficients in radius and auxiliary angle."""
    def __init__(self,c,nr=2,na=3):
        self.c=c;self.nr=nr;self.na=na
    def const(self,x):return Mixed({(0,0):x},self.nr,self.na)
    def __add__(self,x):
        if not isinstance(x,Mixed):x=self.const(x)
        out=dict(self.c)
        for k,b in x.c.items():out[k]=out.get(k,0)+b
        return Mixed(out,self.nr,self.na)
    __radd__=__add__
    def __neg__(self):return Mixed({k:-w for k,w in self.c.items()},self.nr,self.na)
    def __sub__(self,b):return self+(-b)
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Mixed):return Mixed({k:a*b for k,a in self.c.items()},self.nr,self.na)
        out={}
        for (i,j),v in self.c.items():
            for (k,l),y in b.c.items():
                key=i+k,j+l
                if key[0]<=self.nr and key[1]<=self.na:out[key]=out.get(key,0)+v*y
        return Mixed(out,self.nr,self.na)
    __rmul__=__mul__
    def unary(self,coeff):
        f=self.c[(0,0)];d=Mixed({k:a for k,a in self.c.items() if k!=(0,0)},self.nr,self.na)
        h=self.const(1);out=self.const(coeff(f,0))
        for j in range(1,self.nr+self.na+1):
            h=h*d;out=out+h*coeff(f,j)
        return out
    def sin(self):return self.unary(lambda x,i:(np.sin,np.cos,lambda z:-np.sin(z),lambda z:-np.cos(z))[i%4](x)/factorial(i))
    def cos(self):return self.unary(lambda x,i:(np.cos,lambda z:-np.sin(z),lambda z:-np.cos(z),np.sin)[i%4](x)/factorial(i))
    def exp(self):return self.unary(lambda x,i:np.exp(x)/factorial(i))
    def power(self,p):
        b=[1.]
        for i in range(1,self.nr+self.na+1):b.append(b[-1]*(p-i+1)/i)
        return self.unary(lambda x,i:b[i]*x**(p-i))
    def dp(self):return Mixed({(i,j-1):j*a for (i,j),a in self.c.items() if j},self.nr,self.na-1)
    def restrict(self,p):return Mixed({k:v for k,v in self.c.items() if k[1]<=p},self.nr,p)


def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def times(a,x):return [v*x for v in a]
def add(a,b):return [x+y for x,y in zip(a,b)]


def ramp(r,soft):
    a,b,d=.075,.22,.05
    t=np.minimum((r-a)/d,(b-r)/d);sign=np.where(r<(a+b)/2,1.,-1.)
    z=Polynomial([0.,1.]);base=3*z*z-2*z**3
    result=np.array([np.where(t<1,base.deriv(i)(t)*(sign/d)**i,float(i==0)) for i in range(3)])
    if soft:
        # Evaluate at distance to the constant branch in local scaled coordinates.
        v=16*(1-t);f=Polynomial([0.,1.]);eta=f/16
        S=10*f**3-15*f**4+6*f**5
        profile=1-(3-2*eta)*eta**2*S
        choose=(v>0)&(v<1)
        for i in range(3):result[i,choose]=profile.deriv(i)(v[choose])*(-16*sign[choose]/d)**i
    return result


def actual_angle(r,count):
    a,b,d=.075,.22,.05
    def source(x):
        t=min((x-a)/d,(b-x)/d,1.);return t*t*(3-2*t)/x
    def I(y):
        if y==b:return 0.
        count['original_analytic_angle_integrals']+=1
        return quad(source,y,b,points=[x for x in (a+d,b-d) if y<x<b],epsabs=3e-14,epsrel=3e-14)[0]
    theta=np.arcsin(.27);M=theta/I(a);p=-M*ramp(r,False)
    q=np.stack((np.array([M*I(float(x)) for x in r]),p[0]/r,p[1]/r-p[0]/r**2))
    return M,q,p


def wave(angles,m,odd,deriv):
    if m==0:return np.full_like(angles,float(not odd and deriv==0))
    name=(np.sin,np.cos,lambda a:-np.sin(a),lambda a:-np.cos(a))
    return m**deriv*name[(deriv+int(not odd))%4](m*angles)


def scalar_field(spl,r,psi,coeff,parity,padding,npsi=3):
    mats=[spl(r,k)[:,padding:-padding] if padding else spl(r,k) for k in range(3)]
    modes=range(int(parity),coeff.shape[0]+int(parity))
    basis=[np.array([wave(psi,m,parity,j) for m in modes]) for j in range(npsi+1)]
    return Mixed({(i,j):((mats[i]@coeff.T)@basis[j])/(factorial(i)*factorial(j))
                  for i in range(3) for j in range(npsi+1)},2,npsi)


def unpack_vector(v,psi,r):
    def entry(x,i,j):
        c=x.c.get((i,j),0);return np.broadcast_to(c,(len(r),len(psi)))*factorial(i)*factorial(j)
    return {(i,j):np.stack([entry(x,i,j) for x in v],axis=-1) for i in range(3) for j in range(3)}


def transported(data,r,psi,count):
    from r687_darboux_frame_transport_20261128 import Frame
    original_count=len(psi);psi=np.r_[psi,np.pi]
    sp=data['actual_space'];src=Frame(sp,count)
    pars=np.array(data['all_parameters']);K=sp['body_modes'];M,q,p=actual_angle(r,count)
    body=pars[:src.body].reshape(len(src.blocks),src.na);row=pars[src.body:src.body+src.nc]
    def radial(x,n=3):return Mixed({(i,0):y[:,None]/factorial(i) for i,y in enumerate(x)},2,n)
    theta=radial(q);phi=Mixed({(0,0):psi[None,:],(0,1):1.})
    ca,sa=theta.cos(),theta.sin();c,s=phi.cos(),phi.sin();z=phi.const(0);one=phi.const(1)
    def rotate(v):return [ca*v[0]+sa*v[2],v[1],ca*v[2]-sa*v[0]]
    O=[rotate(v) for v in ([c,s,z],[-s,c,z],[z,z,one])]
    for axis in range(3):
        f=scalar_field(src.spl,r,psi,body[np.array([i==axis for i,j in src.blocks])],axis!=1,3)
        st,ct=f.sin(),f.cos();i,j=(axis+1)%3,(axis+2)%3
        u,v=O[i],O[j];O[i],O[j]=add(times(u,ct),times(v,st)),add(times(u,-st),times(v,ct))
    T=[t.restrict(2) for t in O[1]];A=[t.dp() for t in O[1]]
    Kvec=cross(T,A);B=times(Kvec,dot(A,A).power(-.5))
    rho=radial([src.spl(r,i)[:,2:-2]@row for i in range(3)],2)
    beta=ramp(r,True)
    def slope(pv):
        q=radial(pv,2);z=-q*(c.restrict(2)+1.01)
        e=(1+q*q*(1.01**2+.5)).power(.5)*rho.exp()
        P0=[x.restrict(2) for x in O[0]];N0=[x.restrict(2) for x in O[2]]
        D=times(add(P0,times(N0,z)),e*(1+z*z).power(-.5))
        bf=dot(D,Kvec)
        return {k:np.broadcast_to(v,(len(r),len(psi)))*factorial(k[0])*factorial(k[1]) for k,v in bf.c.items()}
    old=slope(p);soft=slope(-M*beta)
    g=src.at(r,original_count);literal=src.state(pars,g,1.)
    count['original_numeric_anchor_comparisons']+=1
    Tpack=unpack_vector(T,psi,r);Bpack=unpack_vector(B,psi,r)
    def split_pack(k):
        return {n:vs[:,:original_count] for n,vs in k.items()},{n:vs[:,original_count:] for n,vs in k.items()}
    Tpack,Tpi=split_pack(Tpack);Bpack,Bpi=split_pack(Bpack);soft,spi=split_pack(soft);old,opi=split_pack(old)
    reflection=dict(T=Tpi,B=Bpi,b=spi,old_b=opi,beta=beta,M=M,q_jets=q)
    errors=dict(analytic_T_to_original_grid=float(np.max(np.linalg.norm(Tpack[0,0]-literal['T'],axis=-1))),
                analytic_Tpsi_to_original_grid=float(np.max(np.linalg.norm(Tpack[0,1]-literal['Tp'],axis=-1))),
                old_center_velocity_gap=float(np.max(np.linalg.norm(literal['gap'],axis=-1))),
                original_curl_norm=float(np.max(np.linalg.norm(literal['G'],axis=-1))),
                old_to_C2_binormal_slope=float(np.max(abs(old[0,0]-soft[0,0]))))
    return dict(T=Tpack,B=Bpack,b=soft,old_b=old,beta=beta,M=M,q_jets=q,reflection=reflection,
                original_center=src.center(pars,r),original_center_slope=literal['C0'],original_center_acc=literal['C1'],
                original_D=literal['EP'],original_e=literal['e'],original_e_target=literal['design_e'],original_G=literal['G'],errors=errors)


class CalibratedGrid:
    def __init__(self,source,order,M,aux_spans,count,extra=()):
        self.a,self.b=.075,.22;self.theta=np.arcsin(.27);self.phi=2*np.pi*np.arange(M)/M
        d=.05;self.breaks=np.unique(np.r_[np.linspace(self.a,self.b,source['actual_space']['radial_spans']+1),
               np.linspace(self.a,self.b,aux_spans+1),self.a+d,self.b-d,self.a+15*d/16,self.b-15*d/16,extra])
        g,w=np.polynomial.legendre.leggauss(order); edges=self.breaks;h=np.diff(edges)/2
        nodes=((edges[:-1]+edges[1:])[:,None]/2+h[:,None]*g).ravel()
        self.r=np.sort(np.r_[edges,nodes]);self.w=np.zeros(len(self.r));self.edge_ids=np.arange(len(edges))*(order+1)
        for j in range(len(h)):self.w[self.edge_ids[j]+1:self.edge_ids[j+1]]=h[j]*w
        width=np.diff(self.r);self.guard_weights=(np.r_[0.,width]+np.r_[width,0.])/2
        basis=np.polynomial.legendre.legvander(g,order-1);invers=np.linalg.inv(basis)
        ant=np.polynomial.legendre.legint(invers,axis=0)
        local=np.polynomial.legendre.legval(g,ant).T-np.polynomial.legendre.legval(-1.,ant)
        self.integral=np.zeros((len(self.r),len(self.r)))
        self.c_value=np.eye(len(self.r));self.c_value[self.edge_ids]=0.
        self.c_derivative=np.zeros_like(self.c_value)
        self.left_value=np.zeros((len(edges),len(self.r)));self.left_derivative=np.zeros_like(self.left_value)
        coeffdot=np.polynomial.legendre.legder(invers,axis=0)
        evalu=lambda x,co:np.polynomial.legendre.legval(x,co).T
        deriv=evalu(g,coeffdot)
        for j in range(len(h)):
            lo,hi=self.edge_ids[j:j+2];rows=slice(lo+1,hi)
            self.integral[lo:hi,lo:]=-self.w[lo:]
            self.integral[rows,rows]+=h[j]*local
            self.c_derivative[rows,rows]=deriv/h[j]
            self.c_value[lo,rows]=evalu(-1.,invers);self.c_derivative[lo,rows]=evalu(-1.,coeffdot)/h[j]
            self.left_value[j+1,rows]=evalu(1.,invers);self.left_derivative[j+1,rows]=evalu(1.,coeffdot)/h[j]
        self.left_value[0]=self.c_value[0];self.left_derivative[0]=self.c_derivative[0]
        self.c_value[-1]=self.left_value[-1];self.c_derivative[-1]=self.left_derivative[-1]
        self.anchor=transported(source,self.r,self.phi,count)
        count['new_transported_grids']+=1
