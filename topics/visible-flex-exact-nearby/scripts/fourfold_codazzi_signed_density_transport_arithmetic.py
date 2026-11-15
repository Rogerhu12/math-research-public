#!/usr/bin/env python3
"""Complete finite-Laurent and radial Taylor arithmetic for the new SN target.

This module neither loads an intrinsic target nor executes a phase, circle,
residual, scalar-integral or response producer. All numerical callers must be
the declared public Actions child. Fourier index j always means physical 4j.
"""
from __future__ import annotations
import math
from fractions import Fraction
from flint import arb,acb,acb_poly,arb_series,ctx

def exact(x):
    q=Fraction(x);return arb(q.numerator)/q.denominator
def ball(x):
    if isinstance(x,arb):return x
    if isinstance(x,dict):
        if "lower" in x and "upper" in x:
            return arb(x["lower"]).lower().union(arb(x["upper"]).upper())
        return arb(x["ball"])
    return arb(x)
def up(x):return abs(x).upper()
def hull(a,b):return exact(a).union(exact(b))
def rat(x):
    a,e=map(int,x.mid().man_exp())
    return Fraction(a*2**e) if e>=0 else Fraction(a,2**(-e))
def real(z):
    if not z.imag.contains(0):raise ValueError("a real scalar lost its complete imaginary enclosure")
    return z.real
def rec(x):return {"ball":ball(x).str(48)}
def positive(x,label):
    if not x.is_finite() or not x>0:raise ArithmeticError("missing strict positive "+label)
    return x

class LP:
    """A complete finite Laurent polynomial; no multiplication truncation."""
    __slots__=("p","lo")
    def __init__(self,p=None,lo=0):
        self.p=p if isinstance(p,acb_poly) else acb_poly([] if p is None else p)
        self.lo=int(lo)
    @staticmethod
    def const(x):return LP([acb(x)],0)
    @property
    def hi(self):return self.lo+len(self.p)-1
    def coeff(self,j):
        return self.p[j-self.lo] if self.lo<=j<=self.hi else acb(0)
    def __neg__(self):return LP(-self.p,self.lo)
    def __add__(self,o):
        if not isinstance(o,LP):o=LP.const(o)
        if not len(self.p):return LP(o.p,o.lo)
        if not len(o.p):return LP(self.p,self.lo)
        l=min(self.lo,o.lo)
        return LP(self.p.left_shift(self.lo-l)+o.p.left_shift(o.lo-l),l)
    __radd__=__add__
    def __sub__(self,o):return self+(-o if isinstance(o,LP) else -acb(o))
    def __rsub__(self,o):return (-self)+o
    def __mul__(self,o):
        if isinstance(o,LP):return LP(self.p*o.p,self.lo+o.lo)
        return LP(self.p*acb(o),self.lo)
    __rmul__=__mul__
    def __truediv__(self,o):return LP([self.p[k]/acb(o) for k in range(len(self.p))],self.lo)
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError("only finite nonnegative Laurent powers")
        z=LP.const(1);a=self
        while n:
            if n&1:z=z*a
            n//=2
            if n:a=a*a
        return z
    def d(self,q=1):
        return LP([self.p[k]*(acb(0,4*(self.lo+k))**q)
                   for k in range(len(self.p))],self.lo)
    def primitive(self):
        return LP([self.p[k]/acb(0,4*(self.lo+k)) if self.lo+k else acb(0)
                   for k in range(len(self.p))],self.lo)
    def ne(self):
        return LP([acb(0) if self.lo+k==0 else self.p[k]
                   for k in range(len(self.p))],self.lo)
    def mean(self):return real(self.coeff(0))
    def scalar(self):
        if any(not self.coeff(j).is_zero() for j in range(self.lo,self.hi+1) if j):
            raise ValueError("a nonlinear Fourier reciprocal was not authorized")
        return self.mean()
    def project(self,N):
        return LP([self.coeff(j) for j in range(-N,N+1)],-N)
    def midpoint_real(self,N=None,mean_zero=False):
        N=max(abs(self.lo),abs(self.hi)) if N is None else N
        out=[acb(0) for _ in range(2*N+1)]
        if not mean_zero:out[N]=acb(exact(rat(self.mean())))
        for j in range(1,N+1):
            z=(self.coeff(j)+self.coeff(-j).conjugate())/2
            v=acb(exact(rat(z.real)),exact(rat(z.imag)))
            out[N+j]=v;out[N-j]=v.conjugate()
        return LP(out,-N)
    def a(self,q=0,width=0):
        w=exact(width) if isinstance(width,(int,Fraction)) else width
        return sum((abs(self.p[k])*(abs(4*(self.lo+k))**q)
                    *(abs(4*(self.lo+k))*w).exp()
                    for k in range(len(self.p))),arb(0)).upper()
    def l2(self,q=0):
        # Parseval is a positive sum. Take coefficient upper endpoints before
        # squaring, and the total upper endpoint before the real square root.
        # This retains every signed label and its mean; it is not clipping a
        # nonfinite coefficient or replacing an unproved domain by a number.
        if not self.finite():raise ArithmeticError("a complete Laurent L2 input is nonfinite")
        square=sum((abs(self.p[k]).upper()**2*(abs(4*(self.lo+k))**(2*q))
                    for k in range(len(self.p))),arb(0)).upper()
        if not square.is_finite() or square<0:
            raise ArithmeticError("a complete Laurent L2 positive sum is nonfinite")
        return square.sqrt().upper()
    def h3(self):
        if not self.finite():raise ArithmeticError("a complete Laurent H3 input is nonfinite")
        square=sum((abs(self.p[k]).upper()**2*(1+(4*(self.lo+k))**2)**3
                    for k in range(len(self.p))),arb(0)).upper()
        if not square.is_finite() or square<0:
            raise ArithmeticError("a complete Laurent H3 positive sum is nonfinite")
        return square.sqrt().upper()
    def finite(self):
        return all(z.is_finite() for z in self.p)

class Jet:
    """Normalized radial Taylor coefficients, with complete Fourier values."""
    __slots__=("c",)
    def __init__(self,coefficients):
        self.c=[v if isinstance(v,LP) else LP.const(v) for v in coefficients]
        if not self.c:raise ValueError("a Taylor jet must retain its value")
    @property
    def n(self):return len(self.c)
    @staticmethod
    def const(x,n):
        return Jet([x]+[0]*(n-1))
    def pad(self,n):return Jet(self.c[:n]+[LP()]*(max(0,n-self.n)))
    def __neg__(self):return Jet([-x for x in self.c])
    def __add__(self,o):
        if not isinstance(o,Jet):o=Jet.const(o,self.n)
        n=max(self.n,o.n);a=self.pad(n);b=o.pad(n)
        return Jet([a.c[k]+b.c[k] for k in range(n)])
    __radd__=__add__
    def __sub__(self,o):return self+(-o if isinstance(o,Jet) else -acb(o))
    def __rsub__(self,o):return (-self)+o
    def __mul__(self,o):
        if not isinstance(o,Jet):return Jet([x*o for x in self.c])
        n=max(self.n,o.n);a=self.pad(n);b=o.pad(n)
        return Jet([sum((a.c[j]*b.c[k-j] for j in range(k+1)),LP())
                    for k in range(n)])
    __rmul__=__mul__
    def scalar_series(self):
        return arb_series([x.scalar() for x in self.c],prec=self.n)
    def scalar_function(self,name):
        s=self.scalar_series()
        r={"inv":lambda:1/s,"sqrt":s.sqrt,"exp":s.exp}[name]()
        if r.prec<self.n:raise ArithmeticError("a scalar jet lost its derivative order")
        return Jet([r[k] for k in range(self.n)])
    def inv(self):return self.scalar_function("inv")
    def sqrt(self):return self.scalar_function("sqrt")
    def exp(self):return self.scalar_function("exp")
    def __truediv__(self,o):
        return self*o.inv() if isinstance(o,Jet) else self*(1/acb(o))
    def __rtruediv__(self,o):return self.inv()*o
    def __pow__(self,n):
        if not isinstance(n,int):raise ValueError("integer Taylor powers only")
        if n<0:return self.inv()**(-n)
        z=Jet.const(1,self.n);a=self
        while n:
            if n&1:z=z*a
            n//=2
            if n:a=a*a
        return z
    def dphi(self,q=1):return Jet([x.d(q) for x in self.c])
    def primitive(self):return Jet([x.primitive() for x in self.c])
    def ne(self):return Jet([x.ne() for x in self.c])
    def mean(self):return Jet([x.mean() for x in self.c])
    def derivative(self):
        if self.n<2:raise ValueError("a radial derivative needs a retained next coefficient")
        return Jet([(j+1)*self.c[j+1] for j in range(self.n-1)])
    def value(self):return self.c[0]
    def evaluate(self,h):
        z=LP()
        for x in reversed(self.c):z=z*h+x
        return z

class Dual:
    """One genuine parameter derivative. Radial jets of Z are never guessed."""
    __slots__=("v","t")
    def __init__(self,v,t=None):
        if not isinstance(v,Jet):raise TypeError("Dual requires an explicit finite Jet")
        self.v=v;self.t=t
    @property
    def n(self):return self.v.n
    def lift(self,o):
        return o if isinstance(o,Dual) else Dual(o if isinstance(o,Jet) else Jet.const(o,self.n))
    def __neg__(self):return Dual(-self.v,None if self.t is None else -self.t)
    def __add__(self,o):
        o=self.lift(o)
        t=self.t if o.t is None else o.t if self.t is None else self.t+o.t
        return Dual(self.v+o.v,t)
    __radd__=__add__
    def __sub__(self,o):return self+(-self.lift(o))
    def __rsub__(self,o):return self.lift(o)-self
    def __mul__(self,o):
        o=self.lift(o)
        t=None
        if self.t is not None:t=self.t*o.v
        if o.t is not None:t=(Jet.const(0,self.n) if t is None else t)+self.v*o.t
        return Dual(self.v*o.v,t)
    __rmul__=__mul__
    def inv(self):
        v=self.v.inv()
        return Dual(v,None if self.t is None else -(v*v*self.t))
    def sqrt(self):
        v=self.v.sqrt()
        return Dual(v,None if self.t is None else self.t/(2*v))
    def exp(self):
        v=self.v.exp()
        return Dual(v,None if self.t is None else v*self.t)
    def __truediv__(self,o):return self*self.lift(o).inv()
    def __rtruediv__(self,o):return self.lift(o)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        z=self.lift(1);a=self
        while n:
            if n&1:z=z*a
            n//=2
            if n:a=a*a
        return z
    def dphi(self,q=1):
        return Dual(self.v.dphi(q),None if self.t is None else self.t.dphi(q))
    def primitive(self):
        return Dual(self.v.primitive(),None if self.t is None else self.t.primitive())
    def ne(self):
        return Dual(self.v.ne(),None if self.t is None else self.t.ne())
    def mean(self):
        return Dual(self.v.mean(),None if self.t is None else self.t.mean())
    def pad(self,n):
        return Dual(self.v.pad(n),None if self.t is None else self.t.pad(n))

def source_algebra(u,v,b,gamma,q,qr,rho,root,mhat,sigma):
    """SN.9, including its full parameter derivative, on rho>0.

    Input radial jets are at fixed moving angle. q=positive sqrt(-K);
    qr is its original outward-r derivative. Root data are at the same
    true root; the bump vanishes there. mhat is a fixed scalar reference.
    Return the ordinary inward-r source F/(2sqrt(rho)), drift speed,
    exact radial mean derivative, and named signed intermediates.
    """
    s=rho.sqrt();k=q*q/rho;eta=-gamma*v.mean()
    A=1/(16*eta*k.sqrt())
    U=(u*u).ne();V=(v*v).ne()
    Ep=(u*u+q*q*v*v).ne();Em=(u*u-q*q*v*v).ne()
    d=-b*Em.primitive()
    arbar=-qr/(2*q)-1/(4*rho)-b*(1+(u*u).mean()+q*q*(v*v).mean())
    Bbar=8*A*arbar
    Cne=-4*b*Bbar*Ep+16*A*b*b*(Ep*Ep).ne()
    cross=u*v.dphi()-v*u.dphi()
    Dfull=64*A*b*b*k*u*u*v*v+2*b*k.sqrt()*cross
    Dne=Dfull.ne()
    g0=root["g0"];chi=root["chi"];Ustar=root["U"]
    J=b*(8*A+2*g0/3)
    Jstar=exact(Fraction(26,3))*root["b"]*g0
    quotient=(J*U-Jstar*Ustar)/rho
    F=(sigma*(quotient+b*k*(8*A-2*g0/3)*V-Cne+rho*Dne)
       -2*sigma*(d*(chi+s*mhat)).dphi()
       +s*d.dphi(2)-2*s*eta*k.sqrt()*chi.dphi())
    speed=d+sigma*eta*q
    ar=arbar-b*Ep
    Cmean=(16*A*ar*ar).mean()
    A2=(A-g0-rho*root["A1"])/(rho*rho)
    B1=(Bbar-root["B0"])/rho
    mprime=(-A2-B1-Cmean+rho*Dfull.mean())/(2*s)
    return F/(2*s),speed,mprime,{"d":d,"A":A,"Bbar":Bbar,"Cne":Cne,
        "Dne":Dne,"chi":chi,"quotient":quotient}

def restrict_scalar(row,name,left,right,derivative=0):
    """Read-only derivative of the previously proved degree-seven identity."""
    a,b=map(Fraction,row["interval"]);c0=Fraction(row["center"])
    if not a<=left<=right<=b or not 0<=derivative<=7:
        raise ValueError("a scalar read leaves the exact original cell or derivative order")
    j=derivative;m=row["models"][name]
    cc=list(map(Fraction,m["exact_centered_polynomial"]))
    pp=list(map(ball,m["point_jets"]));last=ball(m["whole_final_derivative"])
    if len(cc)!=8 or len(pp)!=7:raise ValueError("incomplete original Taylor identity")
    h=exact(max(abs(left-c0),abs(right-c0)))
    fee=sum((math.factorial(k)//math.factorial(k-j)*abs(pp[k]-exact(cc[k]))
             *h**(k-j) for k in range(j,7)),arb(0))
    fee+=abs(last-5040*exact(cc[7]))*h**(7-j)/math.factorial(7-j)
    x=hull(left-c0,right-c0);z=arb(0)
    for k in range(7,j-1,-1):z=z*x+exact(cc[k]*Fraction(math.factorial(k),math.factorial(k-j)))
    return z+arb(0,fee.upper())

def inward_scalar(row,name,left,right,n):
    if n>8:raise ValueError("only old saved derivatives zero through seven exist")
    return Jet([(-1)**j*restrict_scalar(row,name,left,right,j)/math.factorial(j)
                for j in range(n)])

def gram_error_step(z,h,source,drift):
    """SN.17--18 in ordinary inward dr. q=0 includes its full mean."""
    M=[[arb(0) for _ in range(4)] for _ in range(4)]
    for q in range(4):
        M[q][q]=((exact(q)+exact(Fraction(1,2)))*drift[1]).upper()
        for ell in range(2,q+2):
            M[q][q+1-ell]=(math.comb(q+1,ell)*drift[ell]).upper()
    lam=max(M[j][j] for j in range(4)).upper()
    N=[[M[i][j] if i>j else arb(0) for j in range(4)] for i in range(4)]
    def mul(A,B):
        return [[sum((A[i][k]*B[k][j] for k in range(4)),arb(0)).upper()
                 for j in range(4)] for i in range(4)]
    P=[[arb(int(i==j)) for j in range(4)] for i in range(4)]
    E=[[x for x in r] for r in P]
    for k in range(1,4):
        P=mul(P,N);a=h**k/math.factorial(k)
        E=[[ (E[i][j]+a*P[i][j]).upper() for j in range(4)] for i in range(4)]
    factor=(lam*h).exp().upper()
    rhs=[(z[k]+h*source[k]).upper() for k in range(4)]
    out=[(factor*sum((E[i][j]*rhs[j] for j in range(4)),arb(0))).upper()
         for i in range(4)]
    if not all(v.is_finite() for v in out):raise ArithmeticError("new complete H3 enclosure is nonfinite")
    return out,{"diagonal_rate":lam,"matrix":M}

def h3_columns(z):
    return (z[0]**2+3*z[1]**2+3*z[2]**2+z[3]**2).sqrt().upper()

def reference_step(initial,F,a,h,N,order=6):
    """An exact-dyadic proposal; no proposed coefficient is a proof."""
    if F.n<order or a.n<order:raise ValueError("a proposal lacks its finite Taylor inputs")
    v=[initial.midpoint_real(N,mean_zero=True)]
    for k in range(order):
        flux=sum((a.c[i]*v[k-i] for i in range(k+1)),LP())
        nextv=((F.c[k]-flux.d())/(k+1)).midpoint_real(N,mean_zero=True)
        v.append(nextv)
    result=Jet(v)
    endpoint=result.evaluate(h).midpoint_real(N,mean_zero=True)
    return result,endpoint

def complete_reference_residual(reference,force,speed,h):
    """All angular labels and radial polynomial terms; no aliasing or cutoff."""
    # force/speed retain orders 0..p-1 at the base point and a full pth
    # derivative coefficient on the whole cell. Their last coefficients
    # enclose their complete Taylor remainders, not only a finite jet.
    p=force.n-1
    if p<1 or speed.n!=force.n:raise ValueError("incomplete uniform Taylor enclosure")
    r=[LP() for _ in range(max(reference.n-1,speed.n+reference.n-1,force.n))]
    for k in range(reference.n-1):r[k]=r[k]+(k+1)*reference.c[k+1]
    for k in range(force.n):r[k]=r[k]-force.c[k]
    for i in range(speed.n):
        for j in range(reference.n):r[i+j]=r[i+j]+(speed.c[i]*reference.c[j]).d()
    whole=Jet(r).evaluate(arb(0,h))
    return [whole.l2(q) for q in range(4)],whole

def trig_polynomial(sines,cosines):
    if len(sines)!=len(cosines):raise ValueError("complete sine and cosine arrays required")
    N=len(sines);out=[acb(0) for _ in range(2*N+1)]
    for j,(a,b) in enumerate(zip(sines,cosines),1):
        z=acb(exact(Fraction(b)/2),exact(-Fraction(a)/2))
        out[N+j]=z;out[N-j]=z.conjugate()
    return LP(out,-N)

def finite_angle_derivative(Hs,Hc,Ks,Kc,width,degree):
    """Exact finite K o H derivative with complete exponential tail.

    No old terminal return, phase transport, or KAM iteration is evaluated.
    """
    H=trig_polynomial(Hs,Hc);Hp=H.d()+1
    K=trig_polynomial(Ks,Kc);full=Hp
    tail=arb(0);h=H.a(width=width);hp=Hp.a(width=width)
    powers=[LP.const(1)]
    for _ in range(degree):powers.append(powers[-1]*H)
    for j in range(1,len(Ks)+1):
        coeff=K.coeff(j)*acb(0,4*j)
        expo=LP()
        scale=acb(1)
        for k in range(degree+1):
            expo=expo+powers[k]*scale
            scale*=acb(0,4*j)/(k+1)
        pos=LP(expo.p,expo.lo+j)*coeff
        # Both signed Fourier directions, including their true complex phase.
        neg=LP([pos.coeff(-l).conjugate() for l in range(-pos.hi,-pos.lo+1)],-pos.hi)
        full=full+Hp*(pos+neg)
        z=4*j*h
        tail+=hp*2*abs(coeff)*(4*j*exact(width)).exp()*z.exp()*z**(degree+1)/math.factorial(degree+1)
    # Enforce the exact derivative mean; charge the entire changed constant.
    meanfee=abs(full.mean()-1).upper()
    full=full.ne()+1
    tail=(tail+meanfee).upper()
    a=exact(width)
    tailH=(1+3/a+6/a**2+6/a**3)*tail
    return full,tailH.upper(),{"complete_analytic_tail":tail,"width":str(width),
                              "degree":degree,"output_modes":max(abs(full.lo),abs(full.hi))}

def inverse_density_constant(Hs,Hc,Ks,Kc,selected):
    """SN.24--28, with the original physical selected A_(1/128) errors."""
    tau=exact(Fraction(1,128));E0=up(ball(selected["physical_true_conjugacy_minus_G_norm"]))
    E1=up(ball(selected["physical_true_conjugacy_derivative_minus_Gprime_norm"]))
    H=trig_polynomial(Hs,Hc);K=trig_polynomial(Ks,Kc)
    hh=[(H.d(i).a()+int(i==1)).upper() for i in range(1,5)]
    kk=[(K.d(i).a()+int(i==1)).upper() for i in range(1,5)]
    h1,h2,h3,h4=hh;k1,k2,k3,k4=kk
    gg=[k1*h1,k2*h1*h1+k1*h2,k3*h1**3+3*k2*h1*h2+k1*h3,
        k4*h1**4+6*k3*h1*h1*h2+3*k2*h2*h2+4*k2*h1*h3+k1*h4]
    def b(q):return arb(1) if not q else (q/((arb(1).exp())*tau))**q
    eps=[min(E1*b(q),E0*b(q+1)).upper() for q in range(4)]
    jlower=(2-gg[0]-eps[0]).lower();jupper=(gg[0]+eps[0]).upper()
    if not (jlower>=exact(Fraction(31,32)) and jupper<=exact(Fraction(33,32))):
        raise ArithmeticError("the same selected true j does not verify both literal AC endpoints: lower="+str(jlower)+", upper="+str(jupper))
    Js=[(gg[q]+eps[q]).upper() for q in (1,2,3)]
    J1,J2,J3=Js;a=exact(Fraction(32,31))
    D=[[a,arb(0),arb(0),arb(0)],
       [a**3*J1,a*a,arb(0),arb(0)],
       [3*a**5*J1**2+a**4*J2,3*a**4*J1,a**3,arb(0)],
       [15*a**7*J1**3+10*a**6*J1*J2+a**5*J3,
        15*a**6*J1**2+4*a**5*J2,6*a**5*J1,a**4]]
    weights=[arb(1),arb(3).sqrt(),arb(3).sqrt(),arb(1)]
    frob=sum(((weights[i]*D[i][j]/weights[j])**2 for i in range(4) for j in range(4)),arb(0)).sqrt()
    KH=(exact(Fraction(33,32)).sqrt()*frob).upper()
    Ej=h3_columns(eps)
    return KH,Ej,{"physical_width":"1/128","E0":E0,"E1":E1,
        "proved_j_lower":jlower,"proved_j_upper":jupper,
        "literal_31over32_33over32_gates_verified":True,
        "finite_H_derivatives":hh,"finite_K_derivatives":kk,
        "complete_G_derivatives":list(map(up,gg)),"angle_error_derivatives":eps,
        "true_j_derivatives":Js,"inverse_density_matrix":D,
        "complete_inverse_density_H3":KH,"complete_angle_derivative_H3_error":Ej}
