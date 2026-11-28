"""Conditional consumer of actual, naturally completed fixed-metric fields. No independent workflow."""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
import math
import re
import os
import time


def public_only():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):raise RuntimeError('Public Actions only.')


def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def rational(x):return F.from_float(x) if type(x) is float else F(x)


class Jet:
    """Ordinary Taylor coefficients; the caller sets one real ball type and finite order per evaluation."""
    scalar=None; order=0
    def __init__(self,values):self.c=list(values)+[self.scalar(0)]*(self.order+1-len(values))
    @classmethod
    def cast(cls,x):
        if isinstance(x,Jet):return x
        return cls([cls.scalar(str(x)) if isinstance(x,F) else cls.scalar(x)])
    def __add__(self,y):return Jet([a+b for a,b in zip(self.c,self.cast(y).c)])
    __radd__=__add__
    def __neg__(self):return Jet([-a for a in self.c])
    def __sub__(self,y):return self+-self.cast(y)
    def __rsub__(self,y):return self.cast(y)+-self
    def __mul__(self,y):
        if not isinstance(y,Jet):
            v=self.cast(y).c[0];return Jet([a*v for a in self.c])
        return Jet([sum((self.c[j]*y.c[i-j] for j in range(i+1)),self.scalar(0)) for i in range(self.order+1)])
    __rmul__=__mul__
    def inv(self):
        one=self.scalar(1);v=[one/self.c[0]]
        for i in range(1,self.order+1):v.append(-v[0]*sum((self.c[j]*v[i-j] for j in range(1,i+1)),self.scalar(0)))
        return Jet(v)
    def __truediv__(self,y):return self*self.cast(y).inv()
    def __rtruediv__(self,y):return self.inv()*y
    def __pow__(self,n):
        if n==0:return self.cast(1)
        if n<0:return (self.inv())**(-n)
        half=self**(n//2);out=half*half;return out*self if n%2 else out
    def exp(self):
        v=[self.c[0].exp()]
        for i in range(1,self.order+1):v.append(sum((j*self.c[j]*v[i-j] for j in range(1,i+1)),self.scalar(0))/i)
        return Jet(v)
    def log(self):
        inv=self.inv();v=[self.c[0].log()]
        for i in range(1,self.order+1):v.append(sum((j*self.c[j]*inv.c[i-j] for j in range(1,i+1)),self.scalar(0))/i)
        return Jet(v)
    def sqrt(self):
        v=[self.c[0].sqrt()]
        for i in range(1,self.order+1):v.append((self.c[i]-sum((v[j]*v[i-j] for j in range(1,i)),self.scalar(0)))/(2*v[0]))
        return Jet(v)
    def trig(self):
        s,c=[self.c[0].sin()],[self.c[0].cos()]
        for i in range(1,self.order+1):
            s.append(sum((j*self.c[j]*c[i-j] for j in range(1,i+1)),self.scalar(0))/i)
            c.append(-sum((j*self.c[j]*s[i-j] for j in range(1,i+1)),self.scalar(0))/i)
        return Jet(s),Jet(c)


def vc(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def vd(a,b):return sum((x*y for x,y in zip(a,b)),Jet.cast(0))
def va(a,b):return [x+y for x,y in zip(a,b)]
def vs(v,k):return [x*k for x in v]
def vdifference(a,b):return [x-y for x,y in zip(a,b)]
def rot(v,c,s):return [c*v[0]+s*v[2],v[1],c*v[2]-s*v[0]]
def jy(v):return [v[2],Jet.cast(0),-v[0]]
def mpoly(a,x):
    v=Jet.cast(0)
    for z in reversed(a):v=v*x+z
    return v

def pder(p):return [i*v for i,v in enumerate(p) if i]

def pprod(p,q):
    y=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):y[i+j]+=a*b
    return y

def padd(a,b):return [(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0) for j in range(max(len(a),len(b)))]


def basis_on(knots,center):
    # Exact polynomials in r-center, including the actual stored knot vector.
    active={i:[F(1)] for i in range(len(knots)-1) if knots[i]<=center<knots[i+1]}
    for d in range(1,6):
        new={}
        for i in range(len(knots)-d-1):
            ls=knots[i+d]-knots[i];rs=knots[i+d+1]-knots[i+1];v=[]
            if ls and i in active:v=pprod(active[i],[(center-knots[i])/ls,1/ls])
            if rs and i+1 in active:v=padd(v,pprod(active[i+1],[(knots[i+d+1]-center)/rs,-1/rs]))
            if v:new[i]=v
        active=new
    return active


def spline_piece(co,base,padding):
    out=[F(0)]*6
    for i,p in base.items():
        if 0<=i-padding<len(co):
            y=co[i-padding]
            for j,c in enumerate(p):out[j]+=y*c
    return out


class Profile:
    def __init__(self,kind):
        self.a=F(3,40);self.b=F(11,50);self.width=F(4,125) if kind=='R691' else F(1,20)
        self.theta=Jet.scalar(str(F(9,25) if kind=='R691' else F(27,100))).asin()
        self.breaks=[self.a,self.a+self.width,self.b-self.width,self.b];self.polys=[]
        for c,d in ((-self.a/self.width,1/self.width),(0,0),(self.b/self.width,-1/self.width)):
            if d:
                u=[c,d];u2=pprod(u,u);self.polys.append(padd([3*x for x in u2],[-2*x for x in pprod(u2,u)]))
            else:self.polys.append([F(1)])
        def prim0(poly,y):
            z=Jet.scalar(str(y));return Jet.scalar(str(poly[0]))*z.log()+sum((Jet.scalar(str(co))*z**j/j for j,co in enumerate(poly) if j),Jet.scalar(0))
        self.prim0=prim0;self.suffix=[Jet.scalar(0)]*4
        for i in (2,1,0):self.suffix[i]=self.suffix[i+1]+prim0(self.polys[i],self.breaks[i+1])-prim0(self.polys[i],self.breaks[i])
        self.M=self.theta/self.suffix[0]
    def calc(self,r,mid):
        i=0 if mid<self.breaks[1] else (2 if mid>self.breaks[2] else 1);poly=self.polys[i]
        primitive=r.log()*poly[0]+sum(((r**j)*(co/j) for j,co in enumerate(poly) if j),Jet.cast(0))
        angle=(Jet.cast(self.suffix[i+1]+self.prim0(poly,self.breaks[i+1]))-primitive)*self.M
        p=mpoly(poly,r)*(-self.M);dp=mpoly(pder(poly),r)*(-self.M)
        return angle,p/r,dp/r-p/r**2,p,dp


def actual_knots(raw,profile):
    if not raw:raise ValueError('Missing actual knot vector.')
    k=[rational(x) for x in raw];a,b=k[0],k[-1]
    if k!=sorted(k) or a==b:raise ValueError('Invalid actual knot vector.')
    # Canonical physical material uses the exact rational rims. Apply the unique affine map of the actual float material coordinate.
    return [profile.a+(t-a)*(profile.b-profile.a)/(b-a) for t in k]


def curve_polynomials(kind,sp,knots,coeff,mid):
    base=basis_on(knots,mid);nb=len(knots)-6;na=nb-6;nc=nb-4;K=sp.get('K',sp.get('body_modes'))
    blocks=([(i,j) for i in range(3) for j in range(int(i==1),K+1)] if kind=='R691' else
            [(i,j) for i in range(3) for j in range(int(i!=1),K+1)])
    rows=[spline_piece(coeff[j*na:(j+1)*na],base,3) for j in range(len(blocks))];tail=coeff[len(blocks)*na:]
    if kind=='R691':
        if len(tail)!=2:raise ValueError('Wrong actual Cartesian column count.')
        return blocks,rows,tail
    if len(tail)!=3*nc:raise ValueError('Wrong actual frame column count.')
    return blocks,rows,[spline_piece(tail[j*nc:(j+1)*nc],base,2) for j in range(3)]


def cartesian(profile,part,r,phi,mid,q):
    blocks,co,trans=part;ang,ar,arr,p,dp=profile.calc(r,mid);z0=Jet.cast(0);span=profile.b-profile.a
    L=profile.breaks[2]-profile.breaks[1]
    if profile.breaks[1]<=mid<=profile.breaks[2]:
        v=2*(r-profile.breaks[1])/L-1;u=1-v*v;H=F(9,2500)*u**3;Hp=-12*F(9,2500)*v*u**2/L;Hpp=-24*F(9,2500)*u*(1-5*v*v)/L**2
    else:H,Hp,Hpp=z0,z0,z0
    s,c=phi.trig();er=[c,s,z0];et=[-s,c,z0];ez=[z0,z0,Jet.cast(1)]
    def pose(mult):
        si,cs=(ang*mult).trig();R,T=rot(er,cs,si),rot(et,cs,si);wr=ar*mult;wrr=arr*mult
        return [va(vs(R,r),vs(ez,H)),va(va(R,vs(jy(R),r*wr)),vs(ez,Hp)),vs(T,r),
                va(va(vs(jy(R),2*wr+r*wrr),vs(jy(jy(R)),r*wr*wr)),vs(ez,Hpp)),va(T,vs(jy(T),r*wr)),vs(R,-r)]
    ref=pose(Jet.cast(1));out=pose(Jet.cast(1)+q/Jet.cast(profile.theta));x=r-mid
    for (i,j),P in zip(blocks,co):
        sj,cj=(phi*j).trig();f,df=(sj,j*cj) if i==1 else (cj,-j*sj);dd=-j*j*f
        val,dv,d2=[mpoly(poly,x)*span for poly in (P,pder(P),pder(pder(P)))]
        for m,y in enumerate((val*f,dv*f,val*df,d2*f,dv*df,val*dd)):out[m][i]=out[m][i]+y
    for k,i in enumerate((0,2)):
        for m,pw in ((0,ang),(1,ar),(3,arr)):out[m][i]=out[m][i]+pw*(span*trans[k])/Jet.cast(profile.theta)
    return ref,out


def material_invariants(ref,out,r,T0,eps,angle,outer):
    D,Y=out[1],vs(out[2],1/r);d,y=ref[1],vs(ref[2],1/r);n=vc(D,Y);area=vd(n,n)
    g=[vd(D,D),vd(D,Y),vd(Y,Y)];g0=[vd(d,d),vd(d,y),vd(y,y)];E=[a-b for a,b in zip(g,g0)];result={}
    for sign in (-1,1):
        mat=[a*eps+sign*b for a,b in zip(g0,E)];result[f'metric_trace_{sign}']=mat[0]+mat[2];result[f'metric_det_{sign}']=mat[0]*mat[2]-mat[1]**2
    b=[vd(n,index) for index in (out[3],vs(out[4],1/r),vs(out[5],1/r**2))]
    u=g[2]*b[0]+g[0]*b[2]-2*g[1]*b[1];v=b[0]*b[2]-b[1]**2;w=area**2+T0**2*v
    si,cs=angle.trig();result.update(area=area,outer_axis=n[2],inner_axis=n[0]*si+n[2]*cs,
                                      principal_trace=4*area**3-T0**2*u**2,principal_det_sum=w,
                                      principal_det_product=w**2-T0**2*area*u**2)
    # Sufficient actual side bound without square root of the uncertain horizontal radius.
    B,c,H=outer;lam=(B+c)/H;z=out[0][2];rho2=out[0][0]**2+out[0][1]**2
    cover=Jet.cast(B+F(1,50)+F(1,25)*lam)-2*T0*Jet.cast(1+lam**2).sqrt()+lam*(z+F(9,200))
    result.update(side_positive=cover,side_square=cover**2-rho2,horizontal_cut=(B-F(1,100000)-2*T0)**2-rho2)
    return result


def dar_frame(profile,part,r,phi,mid,fixedrow,archive_row,calibration):
    blocks,polys,tail=part;ang,wr,wrr,p,dp=profile.calc(r,mid);s,c=phi.trig();sa,ca=ang.trig();v0=Jet.cast(0);v1=Jet.cast(1)
    P,T,N=[rot(v,ca,sa) for v in ([c,s,v0],[-s,c,v0],[v0,v0,v1])];O=[P,T,N]
    Or=[v0,wr,v0];Orr=[v0,wrr,v0];Op=N.copy();x=r-mid
    for axis in range(3):
        f,fp,fr,frr=[Jet.cast(0) for _ in range(4)]
        for (i,j),poly in zip(blocks,polys):
            if i!=axis:continue
            sj,cj=(phi*j).trig();vv,dv=(cj,-j*sj) if axis==1 else (sj,j*cj)
            u=mpoly(poly,x);f=f+u*vv;fp=fp+u*dv;fr=fr+mpoly(pder(poly),x)*vv;frr=frr+mpoly(pder(pder(poly)),x)*vv
        V=O[axis];Vx=vc(Or,V);Orr=va(Orr,va(vs(V,frr),vs(Vx,fr)));Or=va(Or,vs(V,fr));Op=va(Op,vs(V,fp))
        ss,cc=f.trig();i,j=(axis+1)%3,(axis+2)%3
        a,b=O[i],O[j];O[i],O[j]=va(vs(a,cc),vs(b,ss)),va(vs(a,-ss),vs(b,cc))
    P,T,N=O;Tr=vc(Or,T);Trr=va(vc(Orr,T),vc(Or,Tr));Tp=vc(Op,T)
    z=-p*(F(101,100)+c);d=1+z*z;ed=d.sqrt();zp=p*s
    P=vs(va(P,vs(N,z)),1/ed);Pp=vc(va(Op,vs(T,-zp/d)),P)
    base_e=(1+(F(101,100)**2+F(1,2))*p*p).sqrt()
    e=base_e*mpoly(fixedrow,x).exp()
    ar,br,width,scale,mu=calibration
    if mid<ar+width:t=(r-ar)/width
    elif mid>br-width:t=(br-r)/width
    else:t=Jet.cast(1)
    source_p=-scale*t**2*(3-2*t)
    archive_e=(1+mu*source_p**2).sqrt()*mpoly(archive_row,x).exp()
    EP=vs(P,e);G=vdifference(vdifference(vs(Pp,e),T),vs(Tr,r))
    w=-F(101,100)*p;dw=-F(101,100)*dp;ez=rot([v0,v0,v1],ca,sa);ex=rot([v1,v0,v0],ca,sa)
    cp=va([mpoly(tail[1],x),v0,mpoly(tail[2],x)],vs(ez,w))
    cpp=va([mpoly(pder(tail[1]),x),v0,mpoly(pder(tail[2]),x)],va(vs(ez,dw),vs(ex,w*wr)))
    return dict(G=G,density=vdifference(cp,EP),T=T,Tr=Tr,Trr=Trr,Tp=Tp,cp=cp,cpp=cpp,e=[e],archived_e=[archive_e])


@lru_cache(maxsize=None)
def cardinal(degree,order):
    vals=[F(-1)+F(2*j,order) for j in range(degree+1)];out=[]
    for j,t in enumerate(vals):
        p=[F(1)];den=F(1)
        for k,u in enumerate(vals):
            if j!=k:p=pprod(p,[-u,1]);den*=t-u
        out.append([v/den for v in p]);
    return out


class BoxPoly:
    """Bivariate polynomial in two independent unit variables with a uniform real ball remainder."""
    degree=0
    def __init__(self,terms,tail=0):
        self.terms=terms;self.tail=Jet.scalar(tail)
    @classmethod
    def const(cls,x):return cls({(0,0):Jet.scalar(str(x)) if isinstance(x,F) else Jet.scalar(x)})
    @classmethod
    def cast(cls,x):return x if isinstance(x,cls) else cls.const(x)
    def __add__(self,x):
        other=self.cast(x); out=dict(self.terms)
        for k,v in other.terms.items():out[k]=out.get(k,Jet.scalar(0))+v
        return BoxPoly(out,self.tail+other.tail)
    __radd__=__add__
    def __neg__(self):return BoxPoly({k:-v for k,v in self.terms.items()},self.tail)
    def __sub__(self,v):return self+-self.cast(v)
    def __rsub__(self,v):return self.cast(v)-self
    def bound(self):return sum((abs(v).upper() for v in self.terms.values()),Jet.scalar(0))+self.tail
    def range(self):
        c=self.terms.get((0,0),Jet.scalar(0));extra=self.tail+sum((abs(v).upper() for k,v in self.terms.items() if k!=(0,0)),Jet.scalar(0))
        return c+Jet.scalar(0,1)*extra
    def __mul__(self,x):
        if not isinstance(x,BoxPoly):
            y=self.const(x).terms[(0,0)];return BoxPoly({k:v*y for k,v in self.terms.items()},self.tail*abs(y).upper())
        ma=self.bound();mb=x.bound();rem=self.tail*mb+x.tail*ma;terms={}
        for (i,j),a in self.terms.items():
            for (h,l),b in x.terms.items():
                k=(i+h,j+l);v=a*b
                if sum(k)>self.degree:rem+=abs(v).upper()
                else:terms[k]=terms.get(k,Jet.scalar(0))+v
        return BoxPoly(terms,rem)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:raise ValueError('Only division-free invariant polynomials are used after enclosure.')
        if n==0:return self.const(1)
        v=self**(n//2);return v*v*self if n%2 else v*v
    def mean(self):
        out={}
        for (i,j),v in self.terms.items():
            if not j%2:out[(i,0)]=out.get((i,0),Jet.scalar(0))+v/(j+1)
        return BoxPoly(out,self.tail)
    def integral(self,half,axis,side):
        # Primitive from normalized -1 or +1; multiply by physical cell halfwidth.
        t={};rem=2*abs(half).upper()*self.tail
        for key,v in self.terms.items():
            p=key[axis]+1;v=v*half/p;lo=list(key);lo[axis]=0;lo=tuple(lo)
            t[lo]=t.get(lo,Jet.scalar(0))-v*side**p
            hi=list(key);hi[axis]=p;hi=tuple(hi)
            if sum(hi)>self.degree:rem+=abs(v).upper()
            else:t[hi]=t.get(hi,Jet.scalar(0))+v
        return BoxPoly(t,rem)
    def end(self,axis,sign):
        t={}
        for key,v in self.terms.items():
            k=list(key);k[axis]=0;k=tuple(k);t[k]=t.get(k,Jet.scalar(0))+v*sign**key[axis]
        return BoxPoly(t,self.tail)


def taylor_box(fn,rc,rh,pc,ph,n):
    # For total order k the coefficients in slope are the true mixed Taylor coefficients.
    Jet.order=n;directions=[]
    for j in range(n+1):
        slope=Jet.scalar(str(F(-1)+F(2*j,n)));directions.append(fn(Jet([rc,rh]),Jet([pc,ph*slope])))
    Jet.order=n+1;u=Jet.scalar(0,1)
    remainder=fn(Jet([rc+u*rh,u*rh]),Jet([pc+u*ph,u*ph]));out={}
    for key,values in remainder.items():
        result=[]
        for j,v in enumerate(values):
            terms={}
            for k in range(n+1):
                matrix=cardinal(k,n)
                for y in range(k+1):
                    terms[k-y,y]=sum((Jet.scalar(str(matrix[i][y]))*directions[i][key][j].c[k] for i in range(k+1)),Jet.scalar(0))
            result.append(BoxPoly(terms,abs(v.c[n+1]).upper()))
        out[key]=result
    return out


def bdot(a,b):return sum((x*y for x,y in zip(a,b)),BoxPoly.const(0))
def bnorm(a):return sum((abs(x.range()).upper()**2 for x in a),Jet.scalar(0)).sqrt().upper()


def geometric_polys(out,r_inv,T0,angle,outer,cap_limits):
    D,Y=out[1],vs(out[2],r_inv);n=vc(D,Y);area=bdot(n,n)
    g=[bdot(D,D),bdot(D,Y),bdot(Y,Y)];b=[bdot(n,v) for v in (out[3],vs(out[4],r_inv),vs(out[5],r_inv**2))]
    u=g[2]*b[0]+g[0]*b[2]-2*g[1]*b[1];w=area**2+T0**2*(b[0]*b[2]-b[1]**2)
    si,co=angle.sin(),angle.cos();res=dict(area=area,outer_axis=n[2],inner_axis=n[0]*si+n[2]*co,
            principal_trace=4*area**3-T0**2*u**2,principal_det_sum=w,principal_det_product=w**2-T0**2*area*u**2)
    B,c,H=outer;l=(B+c)/H; z=out[0][2];rho2=out[0][0]**2+out[0][1]**2
    R=BoxPoly.const(Jet.scalar(str(B+F(1,50)+F(1,25)*l))-Jet.scalar(str(2*T0))*Jet.scalar(str(1+l*l)).sqrt())+(z+F(9,200))*l
    res.update(side_positive=R,side_square=R**2-rho2,horizontal_cut=(B-F(1,100000)-2*T0)**2-rho2)
    # Verify sufficient split annulus envelopes; these are used with the independently enclosed real peg centre.
    rad,lo,hi=cap_limits;res.update(ring_radius=BoxPoly.const(rad**2)-rho2,ring_lower=z-lo,ring_upper=hi-z)
    return res


def positive_lower(values):
    result={}
    for name,val in values.items():
        b=val.range() if isinstance(val,BoxPoly) else val
        if not b.is_finite():return False,{'unclosed':name,'reason':'nonfinite interval image'}
        result[name]=str(b.lower().fmpq())
    return all(F(v)>0 for v in result.values()),result


def pack_ball(a):
    if not a.is_finite():raise ValueError('Finite outward enclosure required.')
    return [str(a.lower().fmpq()),str(a.upper().fmpq())]


def unball(pair):
    a,b=map(F,pair);return Jet.scalar(str((a+b)/2),str((b-a)/2))


def pack_poly(a):return {'c':[[i,j,*pack_ball(v)] for (i,j),v in a.terms.items()],'tail':pack_ball(a.tail)}
def unpoly(x):return BoxPoly({(i,j):unball((a,b)) for i,j,a,b in x['c']},unball(x['tail']))


def primitive_ring(cells,key,half):
    n=len(cells);bounds=[];allmeans=[]
    for coord in range(3):
        f=[cell[key][coord] for cell in cells];mu=sum((v.mean() for v in f),BoxPoly.const(0))*(F(1,n));total=BoxPoly.const(0);J=[]
        for v in f:
            a=(v-mu).integral(half,1,-1)+total;J.append(a);total=a.end(1,1)
        c=sum((v.mean() for v in J),BoxPoly.const(0))*F(1,n)
        bounds.append([v-c for v in J]);allmeans.append(mu)
    return [[bounds[axis][j] for axis in range(3)] for j in range(n)],allmeans


def metric_forms(ref,D,Y,eps):
    g=(bdot(D,D),bdot(D,Y),bdot(Y,Y));err=[x-y for x,y in zip(g,ref)];out={}
    for s in (-1,1):
        d,m,n=[eps*x+s*y for x,y in zip(ref,err)];out['metric_trace_'+str(s)]=d+n;out['metric_det_'+str(s)]=d*n-m*m
    return out


def endpoints(kind,profile,config,cx,cz,angle):
    a=Jet.scalar;co,si=angle.cos(),abs(angle.sin());z=unball(pack_ball(cz));d=abs(cx)
    B,cc,H=[a(str(t)) for t in config['outer']];l=(B+cc)/H;T=a('3/100');J=a('4501/100000')
    radius,lo,hi=[a(str(t)) for t in config['ring']]
    peg=[(d+a('.075')+a('.0336')*si,z-a('.075')*si,z+a('.0336')*co+a('.075')*si),
         (d+a('.043')+a('.28')*si,z-a('.043')*si,z+a('.28')*co+a('.043')*si)]
    gap=H*co-(B+cc)*si
    vals={'inclined_projection':co, 'far_spherical_support_cone':a('.00499')*gap-a('.00001')*((B+cc)**2+H*H).sqrt(),
          'peg_tube':a('.22')-d-a('.075')-(a('.28')+T)*si,'anchor_open_grip':a('.201')-a('.2'),
          'outer_shell_diameter':1-2*B-2*J,'outer_mixed_ends':1-((B+cc)**2+H*H).sqrt()-2*J}
    parts=[(radius,lo,hi)]+peg;source=(H+a('.045'))*co-cc*si+a('.04499')
    for j,(rad,low,high) in enumerate(parts):
        vals['support_'+str(j)]=source-rad*si+co*low
        if j:
            vals['opening_'+str(j)]=B-a('.00001')-2*T-rad
            vals['side_'+str(j)]=B+a('.02')+a('.04')*l-(rad+l*(-low-a('.045'))+2*T*(1+l*l).sqrt())
        for k,(c,z0) in enumerate(((B,-a('.045')),(cc,-H-a('.045')))):
            for i,v in enumerate((low,high)):
                vals[f'mixed_diameter_{j}_{k}_{i}']=(1-J)**2-(c+rad)**2-(v-z0)**2
    for i,(r1,a1,b1) in enumerate(parts):
        for j,(r2,a2,b2) in enumerate(parts):
            vals[f'inner_diameter_{i}_{j}']=1-(r1+r2)**2-(b1-a2)**2
    if kind=='R687':vals['entire_phase_support']=2*cc*si-a('.3')
    return positive_lower(vals)


def native_input(kind,record,threshold):
    if kind=='R691':
        d=record['independent_crossed']['both'];q=record['actual_q'];spec=record['actual_space'];coeff=record['actual_parameters'];knots=record['actual_knots']
        if not d['sampled_whole_shell_pass'] or not 0<=d['finite_fixed_g_eta']<=threshold:return None,'actual same-g independent gate unpassed'
        return dict(q=q,spec=spec,coeff=coeff,knots=knots,domain='one finite pose only'),None
    if kind!='R687':raise ValueError('Unsupported actual native field.')
    d=record['independent_crossed']['both'];f=record.get('fixed_metric')
    if (not f or record['attempted_level']!=1 or not any(p['fixed'] and p['accepted']>0 for p in record['stages'])
        or not d['sampled_whole_geometry_gate'] or not 0<=d['sampled_rotational_eta']<=threshold or not 0<=d['ring_unit_tangent_closure']<=threshold):
        return None,'actual frozen radial reference, correction, or independent gate missing'
    # The archived radial E uses the original frozen space. Its data are independent of subsequent prolongations.
    import numpy as np
    from r683_proper_phase_metric_transport_20261128 import ProperPhase
    def source_knots(s):
        if (str(s['a']),str(s['b']),str(s['tilt_sine'])) != ('0.075','0.22','0.27'):
            raise ValueError('Different R680 physical profile.')
        return np.r_[[s['a']]*5,np.linspace(s['a'],s['b'],s['radial_spans']+1),[s['b']]*5].tolist()
    raw_knots=source_knots(f['space'])
    # Rebuild only the original scalar logarithm/ramp-series calibration. It is not stored in the terminal.
    anchor=object.__new__(ProperPhase);anchor.a,anchor.b,anchor.d=f['space']['a'],f['space']['b'],.05
    anchor.left=anchor.a+anchor.d;anchor.right=anchor.b-anchor.d
    scale=math.asin(f['space']['tilt_sine'])/float(anchor.tail(np.array([anchor.a]))[0])
    calibration=[rational(z) for z in (anchor.a,anchor.b,anchor.d,scale,1.01**2+.5)]
    return dict(q=0.,spec=record['actual_space'],coeff=record['all_parameters'],knots=source_knots(record['actual_space']),
                frozen=f,reference_knots=raw_knots,calibration=calibration,domain='all published proper material phases'),None


def validate_frontier(cut,frontier,closed,partial_count):
    # A decreasing traversal integrates C from the outer rim. The paid and unpaid parts must tile exactly.
    intervals=[(F(a),F(b)) for a,b,*_ in frontier]
    intervals += [tuple(map(F,row['interval'])) for row in reversed(closed)]
    if not intervals or intervals[0][0]!=cut[0] or intervals[-1][1]!=cut[-1]:
        raise ValueError('Incomplete native radial domain.')
    if any(a>=b for a,b in intervals) or any(x[1]!=y[0] for x,y in zip(intervals,intervals[1:])):
        raise ValueError('Overlapping or missing native radial intervals.')
    if not set(cut).issubset({a for a,b in intervals}|{intervals[-1][1]}):
        raise ValueError('An original knot or physical ramp break was lost.')
    if partial_count and (not frontier or partial_count>frontier[-1][3]):
        raise ValueError('Invalid paid angular prefix.')


def compare_completed(kind,literal_final,origin,options,*,saved=None,saved_sha256=None,progress=None):
    """Native read-only source consumer. `progress` may persist every paid radial/azimuthal checkpoint."""
    public_only();import flint
    from pathlib import Path
    native_file={'R691':'r691_same_metric_bowed_pose_continuation_20261128.py','R687':'r687_darboux_frame_transport_20261128.py'}[kind]
    src=Path(__file__).with_name(native_file);fixedsrc=Path(__file__).with_name('r675_bowed_endpoint_pose_response_20261128.py' if kind=='R691' else 'r683_proper_phase_metric_transport_20261128.py')
    cfgfile=src.parent.parent/'computations'/({'R691':'r691-same-metric-bowed-pose-continuation-20261128.json',
        'R687':'r687-darboux-frame-transport-20261128.json'}[kind])
    if (not isinstance(literal_final,bytes) or origin.get('natural_success') is not True
            or str(origin.get('repository','')).lower()!='rogerhu12/math-research-public'
            or any(type(origin.get(k)) is not int or origin[k]<=0 for k in ('run_id','job_id'))
            or not re.fullmatch('[0-9a-f]{40}',origin.get('source_commit','')) or origin.get('literal_terminal_sha256')!=hashlib.sha256(literal_final).hexdigest()
            or origin.get('native_solver_sha256')!=hashlib.sha256(src.read_bytes()).hexdigest()
            or origin.get('native_geometry_sha256')!=hashlib.sha256(cfgfile.read_bytes()).hexdigest()
            or origin.get('fixed_profile_source_sha256')!=hashlib.sha256(fixedsrc.read_bytes()).hexdigest()):
        raise ValueError('Completed original artifact, exact source bindings and fixed reference are required.')
    native_cfg=json.loads(cfgfile.read_bytes())
    if kind=='R691' and (native_cfg['radii']!=[.075,.22] or (native_cfg['ramp'],native_cfg['height'],native_cfg['sine'])!=(.032,.0036,.36)):
        raise ValueError('Source is a different fixed physical endpoint.')
    target=F(options.get('threshold','1/1000000'));start=time.monotonic();limit=float(options['seconds']);n=int(options.get('order',5))
    if not(0<target<=F(1,1000000) and 2<=n<=10 and 1<=limit<=3300):raise ValueError('Invalid validated budget or order.')
    record=json.loads(literal_final)
    if record.get('kind')!='terminal':raise ValueError('Expected actual native terminal.')
    try:
        native,why=native_input(kind,record,float(target))
    except (KeyError,TypeError,ValueError) as exc:
        native,why=None,'Exact native state or reference unavailable: '+str(exc)
    if why:return dict(status='ineligible_actual_gate',reason=why,origin=origin,scientific_enclosures=0,README_completion_claim=False)
    flint.ctx.prec=int(options.get('bits',176));Jet.scalar=flint.arb;BoxPoly.degree=n;profile=Profile(kind)
    knots=actual_knots(native['knots'],profile);fixed=[];literal_fixed=[]
    if kind=='R687':
        fs=native['frozen']['space'];spans=fs['radial_spans']
        def uniform(n):
            return [profile.a]*5+[profile.a+(profile.b-profile.a)*i/n for i in range(n+1)]+[profile.b]*5
        fixed=uniform(spans)
        literal_fixed=[rational(z) for z in native['reference_knots']]
        if (literal_fixed[0]>profile.a or literal_fixed[-1]<profile.b
                or len(native['frozen']['log_radial_coefficients'])!=len(literal_fixed)-10):
            return dict(status='missing_exact_frozen_spline',origin=origin,scientific_enclosures=0,README_completion_claim=False)
    calibration=native.get('calibration')
    extra=[calibration[0]+calibration[2],calibration[1]-calibration[2]] if calibration else []
    cut=sorted(set(t for t in knots+fixed+literal_fixed+profile.breaks+extra if profile.a<=t<=profile.b))
    coeff=[rational(x) for x in native['coeff']];q=rational(native['q']);A=Jet.scalar
    q_radius=F(options.get('pose_interval_radius','0'))
    if q_radius<0 or (kind=='R687' and q_radius!=0):raise ValueError('Invalid material pose radius.')
    q_field=A(str(q),str(q_radius));angle=profile.theta+q_field
    if q_radius>0:native['domain']='explicit constant-coefficient Cartesian lift over the declared full q interval'
    outer=(F(1,3),F(5,12),F(7,20)) if kind=='R691' else (F(57,200),F(14,25),F(29,100))
    ring=tuple(F(s) for s in options.get('ring_envelope',['.221','-.08','.08']))
    if len(ring)!=3 or ring[0]<=0 or ring[1]>=ring[2]:raise ValueError('An ordered true annular envelope is required.')
    cfg=dict(outer=outer,ring=ring)
    key=digest(dict(origin=origin,archived_calibration=[str(x) for x in calibration] if calibration else None,options={k:v for k,v in options.items() if k not in ('seconds','maximum_azimuth_bins','radial_depth')},kind=kind,canonical_rims=['3/40','11/50'],consumer_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
    base_ang=int(options.get('azimuth_bins',48));max_ang=int(options.get('maximum_azimuth_bins',768));max_depth=int(options.get('radial_depth',12));T0=F(3,100)
    if not(8<=base_ang<=max_ang<=6144 and 0<=max_depth<=24):raise ValueError('Invalid interval frontier.')
    prior_seconds=0.
    if saved is None:
        frontier=[[str(a),str(b),0,base_ang] for a,b in zip(cut[:-1],cut[1:])];cent=[A(0)]*3;cost={'paid_cells':0,'closed_radial_slabs':0};current=[];last_reason=None;closed=[]
    else:
        if saved.get('status') not in ('paid_partial','unclosed_at_resolution') or saved_sha256 is None or saved_sha256!=digest(saved) or saved.get('consumer_input_sha')!=key or saved.get('resume_content_sha256')!=digest({k:v for k,v in saved.items() if k!='resume_content_sha256'}):raise ValueError('Different paid native radius partition.')
        frontier=[list(row) for row in saved['unpaid_radial_stack']];cent=[unball(v) for v in saved['outer_integrated_center']];cost=dict(saved['counts']);closed=list(saved['closed_slabs']);last_reason=saved.get('last_reason')
        current=[{k:[unpoly(p) for p in v] for k,v in cell.items()} for cell in saved['paid_current_angular_tiles']]
        prior_seconds=float(saved['total_scientific_seconds'])
        old_limits=saved['permitted_resolution']
        if max_ang<old_limits['maximum_azimuth_bins'] or max_depth<old_limits['radial_depth']:
            raise ValueError('A funded subdivision cannot be removed on resume.')
        if saved['status']=='unclosed_at_resolution':
            if current or not frontier:raise ValueError('Inconsistent terminal enclosure prefix.')
            aa,bb,depth,M=frontier[-1]
            if M<max_ang:frontier[-1]=[aa,bb,depth,min(2*M,max_ang)]
            elif depth<max_depth:
                mid=(F(aa)+F(bb))/2;frontier.pop()
                frontier.extend([[aa,str(mid),depth+1,base_ang],[str(mid),bb,depth+1,base_ang]])
            else:raise ValueError('Increase a subdivision ceiling to continue an unfinished bound.')
    validate_frontier(cut,frontier,closed,len(current))
    def report(status,extra=None):
        out=dict(status=status,kind=kind,domain=native['domain'],consumer_input_sha=key,source=origin,unpaid_radial_stack=frontier,closed_slabs=closed,
                 outer_integrated_center=[pack_ball(v) for v in cent],counts=cost,last_reason=last_reason,
                 paid_current_angular_tiles=[{k:[pack_poly(p) for p in v] for k,v in tile.items()} for tile in current],
                 elapsed_current_seconds=time.monotonic()-start,README_completion_claim=False)
        out['permitted_resolution']=dict(maximum_azimuth_bins=max_ang,radial_depth=max_depth)
        out['validated_field_definition']='analytic continuous reconstruction with archived coefficients and actual knots affinely pulled to the common exact material rims'
        out['literal_original_evaluator_surface_certified']=False
        out['actual_pose_interval']=[str(q-q_radius),str(q+q_radius)] if kind=='R691' else None
        out['original_radial_scale_reconstructions_this_call']=int(kind=='R687')
        out['original_binary_profile_calibration']=[str(x) for x in calibration] if calibration else None
        out['total_scientific_seconds']=prior_seconds+out['elapsed_current_seconds']
        if extra:out.update(extra)
        out['resume_content_sha256']=digest(out)
        if progress is not None:progress(out)
        return out
    while frontier:
        if time.monotonic()-start>limit:return report('paid_partial')
        aa,bb,depth,M=frontier[-1];a,b=F(aa),F(bb);mid=(a+b)/2;half=(b-a)/2
        rc,rh=A(str(mid)),A(str(half));ph=A.pi()/M;part=curve_polynomials(kind,native['spec'],knots,coeff,mid)
        if kind=='R687':
            fr=[rational(x) for x in native['frozen']['log_radial_coefficients']]
            fx=spline_piece(fr,basis_on(fixed,mid),2);ax=spline_piece(fr,basis_on(literal_fixed,mid),2)
        def fn(r,phi):
            if kind=='R691':
                ref,out=cartesian(profile,part,r,phi,mid,Jet.cast(q_field));values=material_invariants(ref,out,r,T0,target,Jet.cast(angle),outer)
                rad,lo,hi=ring;values.update(ring_radius=rad**2-out[0][0]**2-out[0][1]**2,ring_lower=out[0][2]-lo,ring_upper=hi-out[0][2])
                return {k:[v] for k,v in values.items()}
            values=dar_frame(profile,part,r,phi,mid,fx,ax,calibration);values['ri']=[1/r];return values
        regular=True;success=True;lower={};new_center=None
        for j in range(len(current),M):
            if time.monotonic()-start>limit:return report('paid_partial')
            try:cell=taylor_box(fn,rc,rh,(2*j+1)*ph,ph,n)
            except (ValueError,ZeroDivisionError,OverflowError):regular=False;last_reason='interval expression domain';break
            if any(not z.bound().is_finite() for vv in cell.values() for z in vv):regular=False;last_reason='nonfinite Taylor enclosure';break
            current.append(cell);cost['paid_cells']+=1
        if regular and kind=='R691':
            for j,tile in enumerate(current):
                ok,low=positive_lower({k:v[0] for k,v in tile.items()});success&=ok
                if 'unclosed' in low:last_reason=low;break
                for name,val in low.items():lower[name]=min(F(val),lower.get(name,F(val)))
                if not ok:last_reason={'angle_bin':j,'nonpositive':[k for k,v in low.items() if F(v)<=0]};break
        elif regular:
            U,meanT=primitive_ring(current,'T',ph);Ur,meanTr=primitive_ring(current,'Tr',ph);Urr,_=primitive_ring(current,'Trr',ph)
            d=[sum((tile['density'][i].mean() for tile in current),BoxPoly.const(0))*F(1,M) for i in range(3)]
            cp=current[0]['cp'];cpp=current[0]['cpp'];C=[z.integral(rh,0,1)+BoxPoly.const(c) for z,c in zip(cp,cent)]
            new_center=[z.end(0,-1).range() for z in C];R=BoxPoly({(0,0):rc,(1,0):rh})
            dg=max(bnorm(tile['G']) for tile in current);eg=min(tile['e'][0].range().lower() for tile in current)
            # Local means give a direct closure bound on this slab, independent of the global curl estimate.
            slope=(bnorm(d)+A.pi()*dg/A(3).sqrt())/eg if eg>0 else A('inf')
            local=(slope*slope+bnorm(meanT)**2).sqrt();local_bound=2*local+local*local
            literal_upper=A(0)
            for j,tile in enumerate(current):
                h=vdifference(tile['T'],meanT);dr=va(cp,va(U[j],vs(Ur[j],R)));ri=tile['ri'][0]
                out=[va(C,vs(U[j],R)),dr,vs(h,R),va(cpp,va(vs(Ur[j],2),vs(Urr[j],R))),va(h,vs(vdifference(tile['Tr'],meanTr),R)),vs(tile['Tp'],R)]
                gates=geometric_polys(out,ri,T0,angle,outer,ring)
                if not(local_bound<A(str(target))):gates.update(metric_forms([tile['e'][0]**2,BoxPoly.const(0),BoxPoly.const(1)],dr,h,target))
                # The exact frozen coefficients are also checked using the literal solver basis, evaluated at the same r.
                # Preserve cancellation by transporting the proved normalized metric allowance when the two e's differ.
                archive_e=tile['archived_e'][0];declared_e=tile['e'][0]
                diff=(archive_e**2-declared_e**2).range()
                ar_lo=(archive_e**2).range().lower()
                native_bound=(local_bound*max(A(1),((declared_e**2).range().upper()/ar_lo).upper())
                              +abs(diff).upper()/ar_lo) if ar_lo>0 else A('inf')
                literal_upper=max(literal_upper,native_bound.upper()) if native_bound.is_finite() else A('inf')
                if not native_bound<A(str(target)):
                    raw=metric_forms([archive_e**2,BoxPoly.const(0),BoxPoly.const(1)],dr,h,target)
                    gates.update({'literal_frozen_'+k:v for k,v in raw.items()})
                ok,low=positive_lower(gates);success&=ok
                if 'unclosed' in low:last_reason=low;break
                for name,val in low.items():lower[name]=min(F(val),lower.get(name,F(val)))
                if not ok:last_reason={'angle_bin':j,'nonpositive':[k for k,v in low.items() if F(v)<=0]};break
            if local_bound.is_finite():lower['slab_curl_based_metric_upper']=F(str(local_bound.upper().fmpq()))
            if literal_upper.is_finite():lower['slab_literal_metric_transfer_upper']=F(str(literal_upper.upper().fmpq()))
            lower['source_delta_upper']=F(str(dg.upper().fmpq()));lower['source_gamma_upper']=F(str(bnorm(d).upper().fmpq()));lower['source_e_lower']=F(str(eg.fmpq()))
        if regular and success and new_center is not None and any(not z.is_finite() for z in new_center):
            success=False;last_reason='nonfinite propagated center enclosure'
        if regular and success:
            frontier.pop();closed.append(dict(interval=[aa,bb],azimuth_bins=M,validated_values={k:str(v) for k,v in lower.items()}));cost['closed_radial_slabs']+=1
            if new_center is not None:cent=new_center
            current=[];continue
        # A closed slab or its center is never reprocessed; a failed enclosure itself grants no qualification.
        current=[]
        if M<max_ang and (depth%2==0 or depth>=max_depth):frontier[-1]=[aa,bb,depth,min(2*M,max_ang)]
        elif depth<max_depth:
            frontier.pop();frontier.extend([[aa,str(mid),depth+1,base_ang],[str(mid),bb,depth+1,base_ang]])
        else:return report('unclosed_at_resolution')
    if kind=='R691':cent=[A(str((profile.b-profile.a)*coeff[-2])),A(0),A(str((profile.b-profile.a)*coeff[-1]))]
    yes,bounds=endpoints(kind,profile,cfg,cent[0],cent[2],angle)
    extras=dict(rigid_endpoint_bounds=bounds,continuous_material_metric_verified=True,all_rigid_geometry_verified=yes,
                temporal_domain=native['domain'],continuous_angle_interval_verified=((kind=='R687' or q_radius>0) and yes),
                arbitrary_refinement_or_exact_family_certified=False)
    if kind=='R691':
        extras['actual_pose_interval']=[str(q-q_radius),str(q+q_radius)]
        if yes and q_radius>0:
            center_angle=profile.theta+A(str(q));B,c,H=outer
            half_difference=(A(str(c))-cent[0])*center_angle.cos()+(A(str(H+F(9,200)))+cent[2])*center_angle.sin()
            diff=abs(2*A(str(q_radius)).sin()*half_difference)
            extras['fixed_grip_whole_image_support_difference']=pack_ball(diff)
            extras['macroscopic_support_threshold_certified']=bool(diff>A('3/10'))
    if kind=='R687':
        dg=max(F(t['validated_values']['source_delta_upper']) for t in closed)
        gam=max(F(t['validated_values']['source_gamma_upper']) for t in closed)
        emin=min(F(t['validated_values']['source_e_lower']) for t in closed)
        if emin>0:
            B=((A(str(gam))+A.pi()*A(str(dg))/A(3).sqrt())**2/A(str(emin))**2
               +A(str((profile.b-profile.a)*dg/profile.a))**2).sqrt()
            extras['global_curl_metric_upper']=pack_ball(2*B+B**2)[1]
    return report('validated_analytic_reconstruction_metric_and_geometry' if yes else 'unclosed_rigid_envelopes',extras)
