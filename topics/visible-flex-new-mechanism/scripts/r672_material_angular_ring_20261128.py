"""Interval angle jets and the continuous mean/zero-mean primitive on a true material ring."""
import math
from fractions import Fraction

import r663_actual_dense_denominator_intervals_20261128 as iv

I,rat=iv.I,iv.rat
PI=I(iv.iv.down(float(iv.iv.original.DECIMAL_PI)),iv.iv.up(float(iv.iv.original.DECIMAL_PI)))


class Jet:
    """Normalized Taylor coefficients in the local angular fraction z in [0,1]."""
    def __init__(self,c):
        self.c=tuple(c)

    def const(self,v):
        if isinstance(v,Jet):
            if len(v.c)!=len(self.c):
                raise ValueError('different angular jet orders')
            return v
        return Jet((v if isinstance(v,I) else I(v),)+(I(0),)*(len(self.c)-1))

    def __add__(self,b):
        b=self.const(b)
        return Jet([x+y for x,y in zip(self.c,b.c)])

    __radd__=__add__

    def __neg__(self):
        return Jet([-v for v in self.c])

    def __sub__(self,b):
        return self+-self.const(b)

    def __rsub__(self,b):
        return self.const(b)+-self

    def __mul__(self,b):
        b=self.const(b)
        return Jet([sum((self.c[j]*b.c[k-j] for j in range(k+1)),I(0)) for k in range(len(self.c))])

    __rmul__=__mul__

    def __truediv__(self,b):
        b=self.const(b)
        z=[]
        for k,x in enumerate(self.c):
            z.append((x-sum((b.c[j]*z[k-j] for j in range(1,k+1)),I(0)))/b.c[0])
        return Jet(z)

    def __rtruediv__(self,b):
        return self.const(b)/self

    def __pow__(self,n):
        if n<0:
            return 1/self**(-n)
        if n==2:
            q=self*self
            return Jet((self.c[0]**2,)+q.c[1:])
        v=self.const(1)
        for _ in range(n):
            v=v*self
        return v

    def sqrt(self):
        if self.c[0].lo<=0:
            raise ArithmeticError('strictly positive angular square root not proved')
        a=[iv.iv.sqrt_i(self.c[0])]
        for k in range(1,len(self.c)):
            a.append((self.c[k]-sum((a[j]*a[k-j] for j in range(1,k)),I(0)))/(2*a[0]))
        return Jet(a)

    def sincos(self):
        s,c=[iv.sin(self.c[0])],[iv.cos(self.c[0])]
        for k in range(1,len(self.c)):
            sc=sum((j*self.c[j]*c[k-j] for j in range(1,k+1)),I(0))/k
            cc=-sum((j*self.c[j]*s[k-j] for j in range(1,k+1)),I(0))/k
            s.append(sc)
            c.append(cc)
        return Jet(s),Jet(c)

    def tanh(self):
        def point(v):
            z=iv.exp(-2*I(abs(v)))
            y=(1-z)/(1+z)
            return y if v>=0 else -y
        a=[I(max(-1.,point(self.c[0].lo).lo),min(1.,point(self.c[0].hi).hi))]
        for k in range(1,len(self.c)):
            z=I(0)
            for j in range(1,k+1):
                n=k-j
                d=I(1 if n==0 else 0)-sum((a[i]*a[n-i] for i in range(n+1)),I(0))
                z+=j*self.c[j]*d
            a.append(z/k)
        return Jet(a)

    def cut(self,n):
        return Jet(self.c[:n+1])

    def angular(self,h):
        return Jet([k*self.c[k]/h for k in range(1,len(self.c))])


def angle(n,index,order,whole):
    h=2*PI/n
    t=h*(I(index,index+1) if whole else I(index))
    return Jet([t,h]+[I(0)]*max(0,order-1)).cut(order)


def fourier(theta,coeff):
    out=[theta.const(0) for _ in range(len(next(iter(coeff.values()))))]
    for j,fields in coeff.items():
        co=(theta*int(j)).sincos()[1]
        out=[v+co*c for v,c in zip(out,fields)]
    return out


def raw_angle(radial,n,i,m,whole):
    # Third radial derivative optional; the primary metric needs just second-order data.
    t=angle(n,i,m+2,whole)
    h=2*PI/n
    v=fourier(t,radial['pre'])
    post=fourier(t,radial['post'])
    sigma=rat('3/20')
    w=(v[0]/sigma).tanh()
    d1=1-w**2
    d2=-2*w*d1/sigma
    f=[w*sigma+post[0],d1*v[1]+post[1],d1*v[2]+d2*v[1]**2+post[2]]
    if len(v)==4:
        d3=-2*d1*(1-3*w**2)/sigma**2
        f.append(d1*v[3]+3*d2*v[1]*v[2]+d3*v[1]**3+post[3])
    # base[j] = rotational Z derivative j, including the exact fixed512 subtraction.
    q,t2=f[0].angular(h),f[0].angular(h).angular(h)
    pt=f[1].angular(h)
    out={k:t.const(radial[k]).cut(m) for k in ('r','E','Er')}
    out.update(p=(f[1]+radial['base'][0]).cut(m),pr=(f[2]+radial['base'][1]).cut(m),
               q=q.cut(m),t=t2.cut(m),pt=pt.cut(m))
    if len(v)==4:
        out.update(Err=t.const(radial['Err']).cut(m),prr=(f[3]+radial['base'][2]).cut(m),
                   prt=f[2].angular(h).cut(m),tr=f[1].angular(h).angular(h).cut(m))
    return out


def mean_primitive(left,whole):
    """Input left derivatives of orders <m and whole-sector order m; no sampled FFT."""
    n=len(left)
    h=2*PI/n
    degree=len(left[0].c)-1
    if len(whole)!=n or n<4 or degree<1:
        raise ValueError('a complete ordered equal-angle ring and Taylor remainder required')
    co=[a.c[:degree]+(w.c[degree],) for a,w in zip(left,whole)]
    mass=[sum((x/(k+1) for k,x in enumerate(c)),I(0)) for c in co]
    moments=[sum((x/((k+1)*(k+2)) for k,x in enumerate(c)),I(0)) for c in co]
    mean=sum(mass,I(0))/n
    p=I(0)
    starts=[]
    for a in mass:
        starts.append(p)
        p=p+h*(a-mean)
    offset=sum((v+h*(b-mean/2) for v,b in zip(starts,moments)),I(0))/n
    out=[[],[]]
    for i,c in enumerate(co):
        at=starts[i]-offset
        cc=(c[0]-mean,)+c[1:]
        partial=I(0)
        for k in reversed(range(len(cc))):
            partial=cc[k]/(k+1)+I(0,1)*partial
        for which,(sector,constant) in enumerate(((left[i],at),(whole[i],at+h*I(0,1)*partial))):
            derivatives=[constant]+[h*((sector.c[j]-mean) if j==0 else sector.c[j])/(j+1)
                                    for j in range(degree)]
            out[which].append(Jet(derivatives))
    return mean,out


def local(raw):
    r,E,Er,p,pr,q,t,pt=[raw[k] for k in ('r','E','Er','p','pr','q','t','pt')]
    b=(r**2-q**2).sqrt()
    u=(E-r**2*p**2/b**2).sqrt()
    N=r/b+r**2*p*t/b**3
    if N.c[0].lo<=0:
        raise ArithmeticError('positive turning numerator not separated')
    nsmall=q**2/(b*(r+b))+r**2*p*t/b**3
    ushift=E-1-r**2*p**2/b**2
    am1=(2*nsmall+nsmall**2-ushift)/(u*(N+u))
    a=1+am1
    v=-p*q/b
    br=(r-q*pt)/b
    bt=-q*t/b
    ur=(Er/2-r*p**2/b**2-r**2*p*pr/b**2+r**2*p**2*br/b**3)/u
    ut=-r**2*p*pt/(u*b**2)-r**2*p**2*q*t/(u*b**4)
    C=E*t+r*p
    B=pt-q/r
    M=r+p*t-q**2/r
    omega=r**2/(u**3*b**3)
    D=C*pr-E*B**2-Er*M/2
    R=omega*D
    K=r**2*p*B/(u*b**3)
    d=dict(b=b,u=u,N=N,a=a,am1=am1,v=v,br=br,bt=bt,ur=ur,ut=ut,R=R,K=K)
    if 'prr' in raw:
        Err,prr,prt,tr=[raw[k] for k in ('Err','prr','prt','tr')]
        Cr,Br,Mr=Er*t+E*tr+p+r*pr,prt-pt/r+q/r**2,1+pr*t+p*tr-2*q*pt/r+q**2/r**2
        Dr=Cr*pr+C*prr-Er*B**2-2*E*B*Br-Err*M/2-Er*Mr/2
        Rr=omega*Dr+(2/r-3*ur/u-3*br/b)*R
        Kr=(2*r*p*B+r**2*(pr*B+p*Br))/(u*b**3)-K*(ur/u+3*br/b)
        Kt=r**2*(pt*B+p*(tr-t/r))/(u*b**3)-K*(ut/u+3*bt/b)
        vr=-(pr*q+p*pt)/b+p*q*br/b**2
        Nr=1/b-r*br/b**2+(2*r*p*t+r**2*(pr*t+p*tr))/b**3-3*r**2*p*t*br/b**4
        d.update(Rr=Rr,Nr=Nr,utr=(Kt+R)*v+a*vr-br*K-b*Kr)
    return d


def frame_fields(g,theta,F,A,G,Gr,pa,pr,prr):
    b,u,N,ut,K=[g[k] for k in ('b','u','N','ut','K')]
    phi=theta+pa/A
    s,c=phi.sincos()
    T=(-s,c)
    JT=(-c,-s)
    Q=pr-pa*G/A
    Fover=F/A
    HT=N*Fover
    HJ=ut*Fover+b*Q/A
    h=(K+pr)/A-pa*G/A**2
    d={'T':T,'JT':JT,'H':[tt*HT+nn*HJ for tt,nn in zip(T,JT)],'h':h,'k':g['a']/A}
    if prr is not None:
        Qr=prr-(K+pr)*G/A-pa*Gr/A+pa*G**2/A**2
        HrT=N*G/A**2+g['Nr']*Fover-h*HJ
        HrJ=ut*G/A**2+g['utr']*Fover+Q*(g['br']/A-b*G/A**2)+b*Qr/A+h*HT
        d['Hr']=[tt*HrT+nn*HrJ for tt,nn in zip(T,JT)]
    return d


def ring(radial,n,degree,check=None):
    if n<4 or n%4 or not 1<=degree<=12:
        raise ValueError('whole even-symmetry ring and finite positive Taylor degree required')
    def sectors(whole):
        level=[]
        for i in range(n):
            if check is not None:
                check()
            level.append(raw_angle(radial,n,i,degree,whole))
        return level
    raw=[sectors(whole) for whole in (False,True)]
    loc=[[local(v) for v in level] for level in raw]
    def integrate(key):
        return mean_primitive([v[key] for v in loc[0]],[v[key] for v in loc[1]])
    F,pa=integrate('am1')
    A=1+F
    G,pr=integrate('R')
    has3='prr' in raw[0][0]
    Gr,prr=integrate('Rr') if has3 else (None,None)
    if A.lo<=0:
        raise ArithmeticError('positive full continuous normalization not separated')
    frames=[[frame_fields(g,angle(n,i,degree,level==1),F,A,G,Gr,pa[level][i],pr[level][i],
                          prr[level][i] if has3 else None) for i,g in enumerate(layer)]
            for level,layer in enumerate(loc)]
    pi={}
    for key in (('H','Hr') if has3 else ('H',)):
        pi[key]=[mean_primitive([v[key][k] for v in frames[0]],[v[key][k] for v in frames[1]]) for k in (0,1)]
    return {'raw':raw,'loc':loc,'frames':frames,'A':A,'G':G,'Gr':Gr,
            'pa':pa,'pr':pr,'prr':prr,'pi':pi,'has_third':has3}
