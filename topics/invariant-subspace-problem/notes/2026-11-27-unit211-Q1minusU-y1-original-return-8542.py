#!/usr/bin/env python3
"""Exact original return for Q=1-u and singleton mean coordinate y=1.
Assembled from the successful small 2026-11-27 QQ probes and the explicit
last rational fibre. This assembled file has not itself been executed at
assembly time: the executor was unavailable. No scratch input is required.
"""
import json, time, signal, resource
from flint import fmpq, fmpq_poly, fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(**kw):
    kw["seconds"]=time.perf_counter()-start
    print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("ell","u","unusedQ","x","y","t","zeta","unused"),"lex")
lp,up,qp,xp,yp,tp,zp,dp=ctx.gens(); zero=ctx.constant(0); one=ctx.constant(1)
def po(v): return v if hasattr(v,"to_dict") else ctx.constant(v)
class R:
    def __init__(self,n=0,d=None,reduce=True):
        if isinstance(n,R): self.n=n.n;self.d=n.d;return
        n=po(n);d=one if d is None else po(d);assert d
        if not n:self.n=zero;self.d=one;return
        if reduce:
            g=n.gcd(d);nn=n/g;dd=d/g
            assert nn*g==n and dd*g==d
            n,d=nn,dd
        c=d.coefficient(0);self.n=n/c;self.d=d/c
    def __bool__(self):return bool(self.n)
    def __add__(self,o):
        o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
    __radd__=__add__
    def __neg__(self):return R(-self.n,self.d,False)
    def __sub__(self,o):return self+-R(o)
    def __rsub__(self,o):return R(o)+-self
    def __mul__(self,o):
        o=R(o);return R(self.n*o.n,self.d*o.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=R(o);assert o
        z=R(self.n*o.d,self.d*o.n)
        assert z.n*o.n*self.d==z.d*o.d*self.n
        return z
    def __rtruediv__(self,o):return R(o)/self
    def __pow__(self,n):
        assert n>=0
        return R(self.n**n,self.d**n)
    def __eq__(self,o):
        o=R(o);return self.n*o.d==o.n*self.d
ell,u,unusedQ,x,y,t,zeta=map(R,ctx.gens()[:7]);Q=1-u
class E:
    def __init__(self,a=0,b=0):
        if isinstance(a,E):self.a=a.a;self.b=a.b;return
        self.a=R(a);self.b=R(b)
    def __add__(self,o):
        o=E(o);return E(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return E(-self.a,-self.b)
    def __sub__(self,o):return self+-E(o)
    def __rsub__(self,o):return E(o)+-self
    def __mul__(self,o):
        o=E(o);return E(self.a*o.a+u*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        out=E(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self,o):
        o=E(o);return self.a==o.a and self.b==o.b
    def conj(self):return E(self.a,-self.b)
b=E(ell/2,(u-ell)/(2*u));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj();bc=(b*c).a
assert not (b*c).b and b+c==ell and b*p+c*q==u
V2=2*u-ell*Q;T0=V2-2*u*u
P02=(2-3*u)*V2-Q*u+2*u**3
M=ell*V2-u*u
assert M==4*bc*u
X=E(x,y);Y=X.conj()
f=(u*x+(u-ell*Q)*y-T0/2)/(2*u)
W2=V2*x+(2*u-u*Q-ell*Q)*y
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-ell
rg=X-a*p-c*E(t);sg=Y-a*q-b*E(t)
A1=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A1,rg,sg],[p,rg,E(),E(t)],[q,sg,E(t),E()]]
unit=[E(1),E(),E(1),E(1)]
def va(v,w):return [a0+b0 for a0,b0 in zip(v,w)]
def vs(k,v):return [E(k)*z for z in v]
def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
dd=DK(unit);F2=tau(dd);Kd=DK(dd)
assert F2==2*f
def mean(j):
    ev=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
    return ev-2*Kd[j]-2*vm(dd,dd)[j]+2*F2*dd[j]
assert mean(0)==0
E1=mean(1);EB=mean(2);EC=mean(3)
assert not E1.b and EB.conj()==EC
def N4(v):
    return 2*tau(vm(dd,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(dd,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
def P2(v):
    cen=va(v,vs(-tau(v),unit))
    return tau(vm(cen,vm(cen,cen)))
v=rows[0];z=rows[1]
vc=va(v,vs(-tau(v),unit));zc=va(z,vs(-tau(z),unit))
Pj=3*tau(vm(vm(vc,vc),zc))
Nv=N4(va(v,z))-N4(v)-N4(z)
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b
assert P2(rows[0])==P02 and N4(rows[0])==2*lam*P02
assert Pj==3*(lam-1-T)*P02
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(ell+2*T+A))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(ell+3*T+3*A+B))
assert not NS.b and not PS.b
nu=(u-ell*Q)/u
Rt=u*(EB.b+nu*EB.a/u)/(2*bc);Ry=-EB.a+ell*Rt/2
H=(2*u-1)*ell+u
def evaluate(rr,values):
    rr=R(rr)
    def ep(pp):
        out=R()
        for m,aa in pp.to_dict().items():
            v0=R(aa)
            for j,ee in enumerate(m):
                if ee:v0*=values[j]**int(ee)
            out+=v0
        return out
    return ep(rr.n)/ep(rr.d)
def coeff(rr,j,index=5):
    pp=ctx.from_dict({tuple(int(v0)-(j if i==index else 0) for i,v0 in enumerate(m)):aa for m,aa in rr.n.to_dict().items() if int(m[index])==j})
    return R(pp,rr.d)
values=list(map(R,ctx.gens()));values[4]=R(1)
assert evaluate(Ry,values)==-(u-1)*H*(ell*(u+1-x)-u)/M
assert coeff(E1.a,1)==4*bc*(x-u-1)
def checkden(rr,atoms):
    pp=R(rr).d
    for at in atoms:
        while pp:
            gg=pp.gcd(at)
            if gg.total_degree()==0:break
            qq=pp/gg;assert qq*gg==pp;pp=qq
    assert pp.total_degree()==0
def strip(pp,atoms,constant):
    original=pp;pd=constant;hist=[]
    for name,at in atoms:
        n=0
        while pp:
            gg=pp.gcd(at)
            if gg.total_degree()==0:break
            qq=pp/gg;assert qq*gg==pp;pp=qq;pd*=gg;n+=1
        if n:hist.append((name,n))
    assert pp*pd==original
    return pp,hist
def univar(pp,index):
    assert all(all(int(m[j])==0 for j in range(len(m)) if j!=index) for m in pp.to_dict())
    out=[fmpq(0)]*(int(pp.degrees()[index])+1)
    for m,aa in pp.to_dict().items():out[int(m[index])]+=aa
    return fmpq_poly(out)
def xgcdcheck(a0,b0):
    gg,s0,t0=a0.xgcd(b0)
    assert s0*a0+t0*b0==gg
    return gg,s0,t0

# H != 0. Ry at y=1 forces ell != 0 and x=u+1-u/ell.
val=list(map(R,ctx.gens()));val[3]=u+1-u/ell;val[4]=R(1)
ee=evaluate(E1.a,val);aa=coeff(ee,1);bb=coeff(ee,0)
assert ee==aa*t+bb and aa==-4*bc*u/ell
val[5]=-bb/aa
assert evaluate(E1.a,val)==0 and evaluate(Ry,val)==0
pc=fmpq_mpoly_ctx.get(("h","u"),"lex");h,uu=pc.gens();p1=pc.constant(1)
def trans_h(pp):
    assert all(all(int(m[i])==0 for i in range(2,8)) for m in pp.to_dict())
    return pc.from_dict({(int(m[0]),int(m[0])+int(m[1])):aa for m,aa in pp.to_dict().items()})
atoms_h=[("h",h),("u",uu),("u-1",uu-1),("M",trans_h(M.n)),("P02",trans_h(P02.n)),("H",trans_h(H.n))]
ps=[]
for name,rr in [("Rt",Rt),("N1",NH.a),("NS",NS.a),("PS",PS.a)]:
    ev=evaluate(rr,val)
    checkden(ev,[lp,up,up-1,M.n,P02.n,H.n])
    pp,hist=strip(trans_h(ev.n),atoms_h,p1);ps.append(pp)
    say(stage="Hnonzero_original_bivariate",name=name,degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),paid=hist)
C=ps[0].resultant(ps[1],"u");S=ps[0].resultant(ps[2],"u")
assert C.degrees()==(69,0) and S.degrees()==(102,0)
content,fac=C.factor();prod=pc.constant(content)
for ff,mm in fac:prod*=ff**int(mm)
assert prod==C
c14=[ff for ff,mm in fac if ff.degrees()==(14,0) and int(mm)==1]
assert len(c14)==1
known=h**22*(h-2)**12*(2*h-1)**4*(h*h-2*h+2)**8*(h+1)
qq=C/(known*c14[0]);assert qq.total_degree()==0 and qq*known*c14[0]==C
gg,ss,tt=xgcdcheck(univar(c14[0],0),univar(S,0));assert gg==1
say(stage="Hnonzero_complete_QQ_cover",degree=69,traceDegree=102,degree14Bezout=True)

# Full quotient-algebra fibres h=-1,1/2,2,h^2-2h+2, with actual
# coefficient inverses, polynomial divisions and extended identities.
def fibre(phi,label):
    k0=fmpq_poly([]);k1=fmpq_poly([1])
    def ka(a0,b0):return (a0+b0)%phi
    def km(a0,b0):return (a0*b0)%phi
    def ki(a0):
        gg,s0,t0=xgcdcheck(a0,phi)
        assert gg.degree()==0 and gg
        z0=(s0/gg[0])%phi;assert km(a0,z0)==k1;return z0
    def trim(v):
        v=v[:]
        while v and not v[-1]:v.pop()
        return v
    def cv(pp):
        v=[k0]*(int(pp.degrees()[1])+1)
        for m,aa in pp.to_dict().items():
            v[int(m[1])]=ka(v[int(m[1])],fmpq_poly([0]*int(m[0])+[aa]))
        return trim(v)
    def add(a0,b0):
        return trim([ka(a0[i] if i<len(a0) else k0,b0[i] if i<len(b0) else k0) for i in range(max(len(a0),len(b0)))])
    def neg(a0):return [-v for v in a0]
    def sub(a0,b0):return add(a0,neg(b0))
    def mul(a0,b0):
        if not a0 or not b0:return []
        v=[k0]*(len(a0)+len(b0)-1)
        for i,x0 in enumerate(a0):
            for j,y0 in enumerate(b0):v[i+j]=ka(v[i+j],km(x0,y0))
        return trim(v)
    def div(a0,b0):
        original=a0[:];a0=a0[:];v=[k0]*max(0,len(a0)-len(b0)+1);ib=ki(b0[-1])
        while a0 and len(a0)>=len(b0):
            j=len(a0)-len(b0);cc=km(a0[-1],ib);v[j]=ka(v[j],cc)
            a0=sub(a0,[k0]*j+[km(cc,z0) for z0 in b0])
        assert add(mul(v,b0),a0)==original
        return trim(v),a0
    def egcd(a0,b0):
        aa,bb=a0[:],b0[:];s0,s1=[k1],[];t0,t1=[],[k1]
        while bb:
            qq,rr=div(aa,bb);aa,bb=bb,rr
            s0,s1=s1,sub(s0,mul(qq,s1));t0,t1=t1,sub(t0,mul(qq,t1))
        if not aa:return [],[],[]
        iv=ki(aa[-1]);aa=[km(v,iv) for v in aa];s0=[km(v,iv) for v in s0];t0=[km(v,iv) for v in t0]
        assert add(mul(s0,a0),mul(t0,b0))==aa
        return aa,s0,t0
    data=list(map(cv,ps));gg=data[0]
    for p0 in data[1:]:gg=egcd(gg,p0)[0]
    rawdeg=len(gg)-1;history=[]
    for name,at in atoms_h:
        az=cv(at)
        if not az:continue
        while gg:
            dd=egcd(gg,az)[0]
            if len(dd)<=1:break
            qq,rr=div(gg,dd);assert not rr;gg=qq;history.append((name,len(dd)-1))
    assert len(gg)==1 and gg[0]
    say(stage="whole_original_h_fibre",label=label,originalGcdDegree=rawdeg,paid=history,remainingDegree=0)
for phi,label in [(fmpq_poly([1,1]),"-1"),(fmpq_poly([-1,2]),"1/2"),(fmpq_poly([-2,1]),"2"),(fmpq_poly([2,-2,1]),"quadratic")]:
    fibre(phi,label)

# H=0. u !=0 forces 2u-1 !=0. The x=u+1 first-line boundary is paid
# before the following t division.
vh=list(map(R,ctx.gens()));vh[0]=-u/(2*u-1);vh[4]=R(1)
assert evaluate(M,vh)==-u**3*(4*u-1)/(2*u-1)**2
assert evaluate(P02,vh)==u*(4*u-1)*(u-1)**2/(2*u-1)
vb=vh[:];vb[3]=u+1
assert evaluate(E1.a,vb)==-(u-1)*(4*u-1)*(3*u-1)/(2*(2*u-1)**2)
vp=list(map(R,ctx.gens()));vp[0]=R(1);vp[1]=R(fmpq(1,3));vp[3]=R(fmpq(4,3));vp[4]=R(1)
assert evaluate(Rt,vp)==t*(t-4)
assert evaluate(NH.a,vp)==-t*t/9+t/9+fmpq(20,27)
for tv in [0,4]:
    vz=vp[:];vz[5]=R(tv);assert evaluate(NH.a,vz)
# Therefore x-u-1 may be inverted on H=0,y=1.
ee=evaluate(E1.a,vh);aa=coeff(ee,1);bb=coeff(ee,0)
assert ee==aa*t+bb;vh[5]=-bb/aa
assert evaluate(E1.a,vh)==0 and evaluate(Ry,vh)==0
rc=fmpq_mpoly_ctx.get(("u","x"),"lex");ru,rx=rc.gens();r1=rc.constant(1)
def trans_u(pp):
    assert all(all(int(m[i])==0 for i in [0,2,4,5,6,7]) for m in pp.to_dict())
    return rc.from_dict({(int(m[1]),int(m[3])):aa for m,aa in pp.to_dict().items()})
atoms_u=[("u",ru),("u-1",ru-1),("2u-1",2*ru-1),("x-u-1",rx-ru-1),("M",trans_u(evaluate(M,vh).n)),("P02",trans_u(evaluate(P02,vh).n))]
qs=[]
for name,rr in [("Rt",Rt),("N1",NH.a),("NS",NS.a),("PS",PS.a)]:
    ev=evaluate(rr,vh)
    checkden(ev,[up,up-1,2*up-1,xp-up-1,evaluate(M,vh).n,evaluate(P02,vh).n])
    pp,hist=strip(trans_u(ev.n),atoms_u,r1);qs.append(pp)
    say(stage="Hzero_original_bivariate",name=name,degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),paid=hist)
C0=qs[0].resultant(qs[1],"x");S0=qs[0].resultant(qs[2],"x")
assert C0.degrees()==(18,0) and S0.degrees()==(41,0)
known0=ru**6*(2*ru-1)*(4*ru-1)**2*(3*ru-1)**5*(8*ru*ru-4*ru+1)*(32*ru*ru-16*ru+1)
cc=C0/known0;assert cc.total_degree()==0 and cc*known0==C0
gg,ss,tt=xgcdcheck(univar(C0,0),univar(S0,0))
expected=fmpq_poly([0,1])**6*fmpq_poly([-1,2])*fmpq_poly([-1,3])**5
expected=expected/expected[expected.degree()]
assert gg==expected
say(stage="Hzero_complete_QQ_cover",degree=18,traceDegree=41,exactGcd="monic u^6(2u-1)(3u-1)^5")
# Last physical u=1/3 fibre: direct original, not an abstract resultant root.
vp=list(map(R,ctx.gens()));vp[0]=R(1);vp[1]=R(fmpq(1,3));vp[4]=R(1)
assert evaluate(f,vp)==x/2-fmpq(1,3)
assert evaluate(lam,vp)==fmpq(1,2)+3*x/4+3*t/8
assert evaluate(T,vp)==-fmpq(1,2)-3*x/4+9*t/8
assert evaluate(E1.a,vp)==-(x-fmpq(4,3))*(t+6*x-4)/3
assert evaluate(Rt,vp)==t*(t-2*x-fmpq(4,3))
v1=vp[:];v1[3]=R(fmpq(1,3));v1[5]=R(2)
assert evaluate(NH.a,v1)==-fmpq(4,27)
v2=vp[:];v2[3]=R(fmpq(2,3));v2[5]=R(0)
assert evaluate(PS.a,v2)==fmpq(8,27)
say(stage="complete",scope="Q=1-u and singleton mean y=1 excluded",wholeBoundaryExcluded=False,ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
