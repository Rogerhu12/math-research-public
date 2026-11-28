"""GJS on each outer true cubic seam and its true physical negative-order receiver."""
from fractions import Fraction as Q
from math import factorial
from flint import arb,acb,acb_series,arb_series
from fourfold_codazzi_signed_density_transport_arithmetic import exact,hull,LP
from fourfold_codazzi_true_phase_original_inputs import ALPHA,DELTA,CONTROL,check
from fourfold_codazzi_true_phase_signed_speed import restricted,coordinate_polys

N=388


def at(inp,cell,lo,hi,derivative=False):
    _,_,k,i=cell
    origin,models=inp.rows[i];xr=hull(lo-origin,hi-origin);xc=hull(lo-inp.nodes[k],hi-inp.nodes[k])
    co=inp.piece(k)
    def poly(j):return ((co[3][j]*xc+co[2][j])*xc+co[1][j])*xc+co[0][j]
    u=poly(0)+inp.du;v=poly(1)+inp.dv+restricted(models['s'],xr,0)
    gamma=restricted(models['gamma'],xr,0);beta=restricted(models['beta'],xr,0)
    q=restricted(models['q'],xr,0);K=-q*q
    Kr=-2*q*restricted(models['q'],xr,1) if derivative else arb(0)
    a,b=CONTROL
    if a<=cell[0] and cell[1]<=b:
        t=hull((lo-a)/(b-a),(hi-a)/(b-a));s=t*(1-t);y=1-2*t
        s2=s*s;s4=s2*s2;w=4096*s4*s2;wp=exact(Q(24576)/(b-a))*s4*s*y
        T=restricted(models['T'],xr,0);delta=arb(0,exact(DELTA))
        f=(-delta*w).exp();raw=K+delta*T*wp
        if derivative:
            T1=restricted(models['T'],xr,1);wpp=exact(Q(24576)/(b-a)**2)*s4*(5*y*y-2*s)
            Kr=f*(Kr+delta*(T1*wp+T*wpp-wp*raw))
        K=f*raw;gamma=gamma*(delta*w/2).exp()
    eta=-gamma*v.mean();check(K.upper()<0 and eta.lower()>0,'true physical orientation and independent mean')
    return u,v,beta,K,Kr,eta


def slopes(inp,dirc,k):
    h=inp.nodes[k]-inp.nodes[k-1]
    def vector(data):
        # All four arrays are dyadic originals. The difference is evaluated
        # exactly BEFORE a conversion to any outward interval or repair.
        old=data[:,k-1,:];new=data[2,k,:]
        return [Q(float(rr))-Q(float(ll))-2*h*Q(float(c2))-3*h*h*Q(float(c3))
                for rr,ll,c2,c3 in zip(new,old[2],old[1],old[0])]
    center=vector(inp.cubics);direction=vector(dirc)
    ua,va=coordinate_polys([exact(ALPHA*x) for x in center])
    uz,vz=coordinate_polys([exact(x) for x in direction]);d=arb(0,exact(DELTA))
    return ua+uz*d,va+vz*d,center,direction


def normalized(p,k,errors=()):
    z=p.mean() if k==0 else arb(0)
    high=sum((abs(c).upper()*abs(4*j)**k for j,c in enumerate(p.p,p.lo) if j),arb(0))/factorial(k)
    if errors:high+=errors[k]
    return z+arb(0,high.upper())


def series(v,precision=3):return acb_series([acb(i) for i in v[:precision]],prec=precision)


def der(x):
    return acb_series([(j+1)*x[j+1] for j in range(x.prec-1)],prec=x.prec-1)


def pos(x,lower):
    check(x.upper()>=lower.lower(),'actual independent positive old lower bound')
    return max(x.lower(),lower.lower()).union(x.upper())


def geom(rows,errors):
    plus,minus=[sum(v,LP()) for v in rows]
    xx=(plus+minus)/2;ww=(minus-plus)/2
    xp=[(a+b)/2 for a,b in zip(errors[0],errors[1])]
    def derivative_jets(p,e):
        return [(k+1)*normalized(p,k+1,e) for k in range(3)]
    ap=derivative_jets(plus,errors[0]);am=derivative_jets(minus,errors[1])
    x=derivative_jets(xx,xp);t=derivative_jets(ww,errors[2])
    ap[0]=pos(ap[0]+1,exact(Q(1,27)));am[0]=pos(am[0]+1,exact(Q(1,27)))
    x[0]=pos(x[0]+1,exact(Q(1,27)))
    for j in range(3):
        x[j]=x[j].intersection((ap[j]+am[j])/2)
        t[j]=t[j].intersection((am[j]-ap[j])/2)
    old_floor=exact(Q(2,3))*exact(Q(1,20)).sqrt()**3
    om=pos(normalized(ww,0,errors[2]),old_floor)
    s0=(arb_series([om,t[0],t[1]/2],prec=3)*exact(Q(3,2))).log()
    s=(s0/3).exp()
    sl,su=s[0].lower(),s[0].upper()
    check(sl>0,'complete real nonzero optical length at the actual original seam')
    x,t,pp,pm=map(series,(x,t,ap,am))
    return x,t,series([s[i] for i in range(3)]),pp*pm,sl,su,min(ap[0].lower(),am[0].lower())


def vector_bound(w,factor):
    return abs(w[0][0]).upper()+factor*abs(w[1][0]).upper()


def receive(inp,dirc,cell,k,r,rows,errors,scale):
    u,v,beta,K,Kr,eta=at(inp,cell,r,r,True);q=(-K).sqrt()
    du,dv,cd,dd=slopes(inp,dirc,k)
    m=dv.mean()/v.mean()
    B=(v*dv*K-u*du)*(2*beta)+(1+u*u-v*v*K)*(m*beta)+m*Kr/(4*K)
    C=((v*du+u*dv-u*v*m)*(-2*beta))*(1/eta)
    x,t,s,gap,sl,su,pmin=geom(rows,errors)
    S=series([normalized(B,j) for j in range(3)])
    C=series([normalized(C,j) for j in range(3)])
    G=(s.log()/2).exp()*(scale/q.sqrt());b=eta*q
    w=[-acb(0,1)*G*(S*t/b+C*x)/2,G*(S*x/b+C*t)/(2*s)]
    y=-t/s;T=-s*s;ii=acb(0,1)
    def inv(v):
        return [(-ii*x*v[0]+T*y*v[1])/gap,(y*v[0]-ii*x*v[1])/gap]
    v1=inv(w);v2=inv(v1);der1=list(map(der,v1));bd=inv(der1)
    one=[der(v)+z for v,z in zip(v2,bd)];two=list(map(der,bd))
    theta=(arb(N).root(3)**(-2)+su*su).sqrt()
    phase=(2/pmin.sqrt())*(exact(Q(6,5))*(1+exact(Q(5,8))*(su**2/sl**2).log()))
    # GIV strengthens both rows and GAF's monotone asymptotic gain can also apply.
    mod=min(exact(Q(18,25)),(arb(2)/(1+arb(N).root(3)**2*sl**2)).root(4))
    cost=phase*mod*(vector_bound(v2,theta)+exact(Q(4,17))*vector_bound(one,theta)+
                     exact(Q(1,17))*vector_bound(two,theta))
    cost*=((1+exact(Q(1,N*N)))/arb(N).sqrt())
    # The actual strict point port takes H^-1. Two ordered true J identities
    # lift H^-2 to H^-1; the original L² inverse is invoked only on L².
    p=arb(17).sqrt()/(4*eta.lower())
    U,U1=u.a(),u.a(1);V,V1,V2=v.a(),v.a(1),v.a(2)
    Lm=2*abs(beta).upper()*(U*V+U1*V+U*V1+(V1+V2)*(U+U1)/4)
    J=p+p*p*Lm*(1+exact(Q(7,5))*exact(Q(1855913,500000)))
    at_waist=cost*J*192*exact(Q(719,1000))
    check(all(z.is_finite() and z>=0 for z in (cost,J,at_waist)),'complete outer-atom physical receiver')
    return dict(raw=cost.upper(),strict_J=J.upper(),waist=at_waist.upper(),
                pmin=pmin,optical_min=sl,optical_max=su),cd,dd
