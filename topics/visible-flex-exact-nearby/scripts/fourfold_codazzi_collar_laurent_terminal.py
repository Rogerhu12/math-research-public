"""Signed physical terminal Ai and companion series, preserving each angular lag."""
from fractions import Fraction as Q
from math import factorial
from flint import acb,arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_true_characteristic_root_input import cauchy_tail,radial_laurent
from fourfold_codazzi_collar_signed_laurent_enclosure import Field,WIDTH,angular_taylor
import fourfold_codazzi_correlated_collar_reference as F


def geometry(arr,major,raw,tail,outer,rho):
    def field(key,r=0,k=0):
        m,R,s=major[key];lp=radial_laurent(arr[key],rho,r)
        if k:lp=lp.theta(k)
        return Field(lp.lo,lp.c,cauchy_tail((m,R,s-WIDTH),abs(rho).upper(),len(arr[key]),r,k))
    def numerator(name):
        p=radial_laurent(raw[name],rho,0)
        fee=tail[name]*(abs(rho).upper()/exact(outer))**len(raw[name])
        return Field(p.lo,p.c,fee)
    t=field('T');x=field('Xp');q=field('Q');y=field('T',0,1)
    d=field('d');t0=field('T0')
    mu=q*q*(x*x+t*y*y)
    def D(key):return -field(key,1)-d*field(key,0,1)
    def Dt(key):return q*(x*D(key)+q*t*y*field(key,0,1))
    at=D('Q')*x+q*D('Xp')+q*q*t*field('T',0,2)-t0*q*x
    a,b=field('a0'),field('b0');fb,fa=field('fb'),field('fa')
    return dict(T=t,x=x,y=y,q=q,mu=mu,at=at,vq=field('vq'),w0=(a,b),
       w1=(field('w1a'),field('w1b')),dw0=(Dt('a0'),Dt('b0')),dw1=(Dt('w1a'),Dt('w1b')),
       A0=(-mu*(a*fb+t*b*fa),-mu*(b*fb+a*fa)),N=(numerator('Nraw_a'),numerator('Nraw_b')),
       chi=field('chi'))


def potential(c,t):
    v=F.bounded_potential(c,32)
    # Scaled original analytic V(R t) and its B average share the same scalar disk.
    b=[z/(2*k+1) for k,z in enumerate(v)]
    return (angular_taylor(t,v,arb(276)),angular_taylor(t,v,arb(276),1).scale(1/exact(F.R)),
            angular_taylor(t,b,arb(276)),angular_taylor(t,b,arb(276),1).scale(1/exact(F.R)),
            angular_taylor(t,b,arb(276),2).scale(1/exact(F.R)**2))


def combined_physical(g,inv,params,sign):
    T,x,y,mu,at,vq=(g[k] for k in ('T','x','y','mu','at','vq'))
    V,Vt,B,Bt,Btt=params
    a,b=g['w0'];b=b.scale(sign)
    a1,b1=g['w1'];a1=a1.scale(sign)
    da,db=g['dw0'];db=db.scale(sign);db1=g['dw1'][1]
    f1,f2=g['A0'];f2=f2.scale(sign)
    na,nb=g['N'];na=na.scale(sign)
    ca=a1+B*T*b;cb=b1+B*a;h=mu*Btt+at*Bt
    L1=(na+B*T*f2-mu*V*ca-(Bt*T*db).scale(2)-h*T*b-mu*Bt*b,
        nb+B*f1-mu*V*cb+(Bt*da).scale(2)+h*a)
    dcb=db1+B*da+mu*Bt*a
    cfirst=(V*dcb).scale(2)+(mu*Vt+at*V)*cb
    ig=(x*x+T*y*y-(y*y*V).scale(inv*inv)).reciprocal()
    ii=acb(0,sign)
    def rank(aa,bb):
        z=-vq*V*((y*aa).scale(ii)+x*bb)*ig
        return (x*z).scale(ii),-y*z
    r0=rank(a,b);r1=rank(ca,cb)
    return (L1[0]+(r0[0]-cfirst).scale(inv)+r1[0].scale(inv**2),
            L1[1]+r0[1].scale(inv)+r1[1].scale(inv**2))


def terminal(t,c,lo,hi):
    # Root-normalized physical columns, retaining the terminal shear on the right.
    nn=arb(4*lo).union(arb(4*hi));R=exact(F.R);n2=nn*nn;scale=n2*R**3
    check(scale.upper()+276*R**2<1,'true scaled generator bound on the complex t disk')
    v=F.bounded_potential(c,66)
    a=1/((arb(3).log()*2/3).exp()*exact(Q(2,3)).gamma())
    d=-((nn.log()*2/3).exp()*R)/((arb(3).log()/3).exp()*exact(Q(1,3)).gamma())
    roots=((a,d),(a*arb(3).sqrt(),-d*arb(3).sqrt()))
    cols=[]
    for v0,v1 in roots:
        coeff=[v0,v1]
        for k in range(62):
            prior=coeff[k-1] if k else arb(0)
            vv=sum((v[h]*coeff[k-h] for h in range(k+1)),arb(0))
            coeff.append((scale*prior-R*R*vv)/((k+1)*(k+2)))
        radius=3*max(abs(v0).upper(),abs(v1).upper())
        cols.append((angular_taylor(t,coeff,radius),angular_taylor(t,coeff,radius,1).scale(1/(R*nn))))
    shear=arb(0,(100/(arb(4*lo).log()*4/3).exp()).upper())
    return cols,shear


def rows(g,c,lo,hi):
    nn=arb(4*lo).union(arb(4*hi));inv=exact(Q(1,4*hi)).union(exact(Q(1,4*lo)))
    t=g['T'].scale(1/exact(F.R));co=F.scaled_potential(c,lo,hi)
    params=potential(co,t);cols,shear=terminal(t,co,lo,hi)
    _,chi=g['chi'].separated_mean()
    result=[];caps=[]
    for sign in (1,-1):
        A,B=combined_physical(g,inv,params,sign)
        phase=chi.scale(acb(0,sign)*nn).exponential()
        pure,comp=[(A*v+B*d)*phase for v,d in cols]
        result.append((pure+comp.scale(shear),comp))
        caps.append([A.cap(),B.cap(),phase.cap(),pure.error,comp.error])
    return result,caps
