#!/usr/bin/env python3
"""Exact QQ exclusion for zero base mean in the unit 2+1+1 branch.
The q=+1,-1 fibers are cited from their separate proved sources and not rerun.
All generated polynomials remain in RAM; only execution metadata is printed.
Dependencies: SymPy 1.14.0 and python-flint 0.9.0.
"""
import hashlib,json,resource,time
from pathlib import Path
started=time.perf_counter()
import sympy as S
b,c,A,r,s,t,p,q=S.symbols('b c A r s t p q')
a=1-b-c
one=S.Matrix([1,0,1,1])
K=S.Matrix([[0,0,p,q],[0,A,r,s],[p,r,0,t],[q,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(z):return a*z[0]+z[1]+b*z[2]+c*z[3]
def dk(z):return S.Matrix([tau(mul(K.row(i),z)) for i in range(4)])
d=dk(one);F=tau(d)/2
def pp(z):
 w=z-tau(z)*one
 return tau(mul(mul(w,w),w))/2

def nn(z):return tau(mul(d-F*one,mul(z,z)))/2-tau(z)*tau(mul(d,z))+F*tau(z)**2+tau(mul(z,dk(z)))/4
hjet=S.symbols('hjet')
Pbase=pp(K.row(0).T+hjet*K.row(1).T)
Nbase=nn(K.row(0).T+hjet*K.row(1).T)
Ps=[S.factor(Pbase.subs(hjet,0)),S.factor(S.diff(Pbase,hjet).subs(hjet,0)),S.factor(pp(K.row(2).T)),S.factor(pp(K.row(3).T))]
Ns=[S.factor(Nbase.subs(hjet,0)),S.factor(S.diff(Nbase,hjet).subs(hjet,0)),S.factor(nn(K.row(2).T)),S.factor(nn(K.row(3).T))]
e=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=S.simplify(e-2*dk(d)-2*mul(d,d)+4*F*d)
def subfac(v,sub):return [S.factor(x.subs(sub,simultaneous=True)) for x in v]
def norms(P,N,aa,bb,cc):
 P0,P1,PB,PC=P;N0,N1,NB,NC=N
 return [3*P0*N1-2*N0*P1,3*N0*NB*NC-(3*aa*P0+P1)*NB*NC-3*bb*PB*N0*NC-3*cc*PC*N0*NB,N0**3*PB**2-NB**3*P0**2,N0**3*PC**2-NC**3*P0**2,NB**3*PC**2-NC**3*PB**2]

# Symbols x,y below are original d_B,d_C, not physical support parameters.
x,f=S.symbols('x f')
bb=-c*q;aa=1-bb-c;yy=x+(q-1)/2
sub={p:1,b:bb,c:c,q:q,r:x-aa-c*t,s:yy-aa*q-bb*t,A:2*f-2*bb*x-2*c*yy+2*bb*c*t}
EC=subfac(E,sub);rawP=subfac(Ps,sub);rawN=subfac(Ns,sub)
def eq(lhs,rhs):assert S.cancel(lhs-rhs)==0
def num(ex):return S.fraction(S.factor(ex))[0]
def jp(P,N,bv,cv):
    av=1-bv-cv
    return S.factor(av*P[0]+P[1]+bv*P[2]+cv*P[3]-3*(av*N[0]+N[1]+bv*N[2]+cv*N[3]))
def con(P,N,bv,cv):
    J=jp(P,N,bv,cv)
    return [S.factor(3*P[0]*N[1]-2*N[0]*P[1]),S.factor(2*N[0]**3+J*P[0]**2)]
def pgcd(fs,var):
    gg=S.Poly(fs[0],var,domain=S.QQ)
    for fi in fs[1:]:gg=S.gcd(gg,S.Poly(fi,var,domain=S.QQ))
    return gg.monic()
AB=t*t-(q+2*x+1)*t+2*x*(1-q)
AC=t*t-2*(q+x)*t+(q-1)*(q-1+2*x)
eq(EC[0],0)
eq(EC[2],c*AB+4*(x-1)*f-2*x*x+2*x-1)
eq(EC[3],-c*q*AC+(4*x-2*q-2)*f-2*x*x+2*x-(q*q+1)/2)
eq(EC[1],c*c*q*(-(q-1)**2+t*(q+3-4*x))+2*c*f*(q-1)*(2*x-1)+c*(q-1)*(4*x*x-4*x-q+1)/2+8*f*f)
LM=S.Matrix([[S.diff(EC[i],c),S.diff(EC[i],f)] for i in [2,3]])
wv=S.Matrix([-EC[i].subs({c:0,f:0}) for i in [2,3]])
D=S.factor(LM.det())
cs=S.factor(S.det(S.Matrix.hstack(wv,LM[:,1]))/D)
fs=S.factor(S.det(S.Matrix.hstack(LM[:,0],wv))/D)
Fbase=q*x-q+2*x*x-x
eq(cs*D,-2*(q-1)*Fbase)

# t=0, regular Cramer chart.
eq(D.subs(t,0),4*(q-1)**2*Fbase)
eq(cs.subs(t,0),-1/(2*(q-1)))
eq(fs.subs(t,0),(2*x-1)/4)
pt0=subfac(rawP,{c:-1/(2*(q-1)),f:(2*x-1)/4,t:0})
nt0=subfac(rawN,{c:-1/(2*(q-1)),f:(2*x-1)/4,t:0})
eq(3*pt0[0]*nt0[1]-2*nt0[0]*pt0[1],-3*q*q*(2*x-1)**2/128)
assert subfac([pt0[1],pt0[2],pt0[3]],{x:S.Rational(1,2)})==[0,0,0]
eq(pt0[0],-q*(q+1)/4)

# Singular Cramer fibers force Fbase=0. All following denominators and
# q=0,+/-1 cases are individually handled in the accompanying proof.
qq=x*(1-2*x)/(x-1)
Fa=2*x*x-2*x+1;Q1=2*x*x-1;Q2=2*x*x-4*x+1
ff0=S.factor(-EC[2].subs({q:qq,t:0,f:0},simultaneous=True)/(4*(x-1)))
E10=S.factor(EC[1].subs({q:qq,t:0,f:ff0},simultaneous=True))
eq(E10,Fa*(4*c*x*x-2*c-x+1)*(4*c*x**3-2*c*x-2*x**3+4*x*x-3*x+1)/(2*(x-1)**4))
cc0=(x-1)*Fa/(2*x*Q1)
case0={q:qq,t:0,c:cc0,f:ff0.subs(c,cc0)}
p0,n0=subfac(rawP,case0),subfac(rawN,case0)
cons0=con(p0,n0,-cc0*qq,cc0)
assert pgcd([num(v) for v in cons0],x)==S.Poly((2*x-1)**3*Fa**2,x,domain=S.QQ).monic()

# D=0,t!=0: an exact one-parameter t graph, then two c-resultants.
Lx=4*x**4-4*x**3-2*x+1
Tx=-Lx/((x-1)*Q2)
eq(D.subs(q,qq),-2*t*(2*x-1)*(t*(x-1)*Q2+Lx)/(x-1)**2)
assert S.gcd(S.Poly((x-1)*Q2,x),S.Poly(Lx,x)).degree()==0
ffD=S.factor(-EC[2].subs({q:qq,t:Tx,f:0},simultaneous=True)/(4*(x-1)))
caseD={q:qq,t:Tx,f:ffD}
pD,nD=subfac(rawP,caseD),subfac(rawN,caseD)
ED=num(EC[1].subs(caseD,simultaneous=True))
facs=[fi for fi,mult in S.factor_list(ED)[1] if S.degree(fi,c)>0]
assert len(facs)==1 and S.degree(facs[0],c)==2
EF=facs[0]
consD=con(pD,nD,-c*qq,c)
rD=[]
for val in consD:
    nv=num(val)
    while S.rem(nv,c,c)==0:nv=S.cancel(nv/c)
    rD.append(S.Poly(S.resultant(EF,nv,c),x,domain=S.QQ))
assert [rr.degree() for rr in rD]==[63,94]
assert pgcd([rr.as_expr() for rr in rD],x)==S.Poly(x**5*(2*x-1)**8*Q2**8,x,domain=S.QQ).monic()

# Direct x=1/2 fiber. This is retained, not divided out of later resultants.
H=2*t*t-3*(q+1)*t+(q-1)**2
ch=-(q-1)/(2*H)
fh=t*(q*q-q*t+4*q-t+1)/(4*H)
caseh={x:S.Rational(1,2),c:ch,f:fh}
ph,nh=subfac(rawP,caseh),subfac(rawN,caseh)
vh=[S.factor(EC[1].subs(caseh,simultaneous=True)),*con(ph,nh,-ch*q,ch)]
fhpoly=[]
for val in vh:
    facs=[fi for fi,mult in S.factor_list(num(val))[1] if S.degree(fi,t)>1]
    assert len(facs)==1
    fhpoly.append(facs[0])
rh=[S.Poly(S.resultant(fhpoly[0],fi,t),q,domain=S.QQ) for fi in fhpoly[1:]]
assert pgcd([rr.as_expr() for rr in rh],q)==S.Poly(q**4*(q-1)**2,q,domain=S.QQ)

# Regular chart D*t*q*(q-1)*(q+1)*Fbase !=0. Native rational arithmetic
# avoids expanding/factoring the large normB rational function in SymPy.
from flint import fmpq,fmpq_mpoly_ctx
ctx=fmpq_mpoly_ctx.get(('t','x','q'),'lex')
tf,xf,qf=ctx.gens();onef=ctx.constant(1);zerof=ctx.constant(0)
def fp(expr):return ctx.from_dict({m:fmpq(str(co)) for m,co in S.Poly(expr,t,x,q,domain=S.QQ).terms()})
def deg(poly):return tuple(max((m[i] for m in poly.to_dict()),default=-1) for i in range(3))
def rd(n,d=onef):
    assert d
    if not n:return zerof,onef
    gg=n.gcd(d)
    return n/gg,d/gg

def rat(expr):
    nn,dd=S.fraction(expr)
    return rd(fp(nn),fp(dd))
def add(U,V):return rd(U[0]*V[1]+V[0]*U[1],U[1]*V[1])
def mulr(U,V):return rd(U[0]*V[0],U[1]*V[1])
def powr(U,n):return U[0]**n,U[1]**n
def scale(U,z):return fmpq(z)*U[0],U[1]
def neg(U):return -U[0],U[1]
def strip(poly,known):
    powers=[]
    for kn in known:
        power=0
        while poly.gcd(kn).total_degree()>0:
            poly=poly/kn
            power+=1
        powers.append(power)
    return poly,powers

Preg=subfac(rawP,{c:cs,f:fs});Nreg=subfac(rawN,{c:cs,f:fs})
pn=[rat(ve) for ve in Preg];nn=[rat(ve) for ve in Nreg]
cr=rat(cs);br=mulr(cr,(-qf,onef));ar=add((onef,onef),neg(add(br,cr)))
JR=add(add(mulr(ar,pn[0]),pn[1]),add(mulr(br,pn[2]),mulr(cr,pn[3])))
JR=add(JR,scale(add(add(mulr(ar,nn[0]),nn[1]),add(mulr(br,nn[2]),mulr(cr,nn[3]))),-3))
C0=add(scale(mulr(pn[0],nn[1]),3),scale(mulr(nn[0],pn[1]),-2))[0]
N0=add(scale(powr(nn[0],3),2),mulr(JR,powr(pn[0],2)))[0]
NB=add(scale(powr(nn[2],3),2),mulr(JR,powr(pn[2],2)))[0]
ME=rat(S.factor(EC[1].subs({c:cs,f:fs},simultaneous=True)))[0]
FB=2*xf**2+xf*qf-xf-qf
M,mp=strip(ME,[tf,qf+1]);C,cp=strip(C0,[qf,qf-1,FB]);V0,np=strip(N0,[qf,qf-1,FB])
assert mp==[1,1] and cp==[2,4,2] and np==[2,6,3]
assert [deg(ve) for ve in [M,C,V0,NB]]==[(3,6,5),(4,6,7),(7,9,12),(13,21,20)]
known=[qf,qf-1,qf+1,FB]
r1,p1=strip(M.resultant(C,'t'),known)
r2,p2=strip(M.resultant(V0,'t'),known)
r3,p3=strip(C.resultant(V0,'t'),known)
rb,pb=strip(M.resultant(NB,'t'),known)
assert [p1,p2,p3,pb]==[[2,4,0,6],[7,6,1,9],[6,12,8,12],[10,24,0,18]]
assert [deg(ve) for ve in [r1,r2,r3,rb]]==[(0,21,19),(0,34,30),(0,35,34),(0,64,49)]
endpoly=[]
for other in [r2,r3,rb]:
    endpoly.append(r1.resultant(other,'q'))
assert [deg(ve)[1] for ve in endpoly]==[879,1020,1637]
GG=endpoly[0].gcd(endpoly[1]).gcd(endpoly[2])
expected=(xf-fmpq(1,2))**362
assert GG==expected
print(json.dumps({'schema':'r150-unit211-zero-base-mean-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,d0=b+cq=0,q not 0,+1,-1; t0, singular Cramer determinant, full regular chart, and xhalf fiber','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'singularResultantDegrees':[63,94],'regularResultantDegrees':[879,1020,1637],'regularGcd':'(x-1/2)^362','ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
