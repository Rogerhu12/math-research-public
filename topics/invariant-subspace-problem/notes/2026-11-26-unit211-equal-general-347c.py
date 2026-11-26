#!/usr/bin/env python3
"""Original QQ certificate for the entire remaining equal-base unit 2+1+1 chart.
Scope: p=q=1, bc*t*l*(l-1)*(2*l-1) != 0. Prior complete results cover the boundary.
Reconstructs original active means, P/N values and jets, zero-point S/Lambda,
all denominator identities, exact resultants, and an explicit final ideal identity.
Only compact scalar receipt is printed; no polynomial matrices are persisted.
"""
import hashlib,json,resource,time
from pathlib import Path
started=time.perf_counter()
from flint import fmpq_mpoly_ctx,fmpq,fmpq_mat
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

def eq(left,right):assert S.cancel(left-right)==0
l,B,Z,V,delta,beta,U,W,k=S.symbols('l B Z V delta beta U W k')
cc=l-B;X=l+V
xx=X+cc*Z/l;yy=X-B*Z/l
chart={p:1,q:1,b:B,c:cc,r:xx-(1-l)-cc*t,s:yy-(1-l)-B*t,A:(1-2*l)*(X-S.Rational(1,2))+2*B*cc*t}
EC=subfac(E,chart);PP=subfac(Ps,chart);NN=subfac(Ns,chart)
eq(EC[0],0)
Pbar=(1-l)*PP[0]+PP[1]+B*PP[2]+cc*PP[3]
Nbar=(1-l)*NN[0]+NN[1]+B*NN[2]+cc*NN[3]
Sorig=Pbar-2*Nbar
C0=3*PP[0]*NN[1]-2*NN[0]*PP[1]
Lambda0=2*NN[0]**3-Nbar*PP[0]**2

def invariant(expr):
    expr=S.cancel(expr.subs(B,(l+delta)/2));num,den=S.fraction(expr)
    assert not den.has(Z,delta)
    out=0
    for (i,j),co in S.Poly(num,delta,Z).terms():
        assert i%2==j%2
        out+=co*(l*l-4*beta)**(i//2)*U**(j//2)*W**(i%2)
    return S.factor(out/den)
ME1=invariant(EC[1]);MEw=invariant((B*EC[2]+cc*EC[3])/l)
MEd=invariant(delta*(EC[2]-EC[3]));Sc=invariant(Sorig);Cc=invariant(C0)
LM=S.Matrix([[S.diff(z,U),S.diff(z,W)] for z in [ME1,MEw]])
eq(LM.det(),-8*beta**2*t/l**3)
sol=S.solve([ME1,MEw],[U,W],dict=True)
assert len(sol)==1
sol=sol[0]
for f in [ME1,MEw]:eq(f.subs(sol,simultaneous=True),0)
eq(sol[U],l*(-8*V**2*l+4*V**2+8*V*l-4*V+4*beta*t**2-16*beta*t+4*l*l-4*l+1)/(8*beta))
eq(sol[W],-l*(8*V**2*l-4*V**2-16*V*beta*t+8*V*l*l-12*V*l+4*V+4*beta*t*t-4*l*l+4*l-1)/(8*beta*t))
# Only already nonzero units can be removed. Every divisor is recorded.
variables=(l,beta,V,t)
allowed=[l,beta,t,l-1,2*l-1]
allowed_monic=[S.Poly(z,*variables).monic() for z in allowed]
removed=[];polys=[]
for idx,ex in enumerate([MEd,W**2-(l*l-4*beta)*U,Cc,Sc]):
    num,den=S.fraction(S.factor(ex.subs(sol,simultaneous=True)))
    unit,factors=S.factor_list(num);kept=[];ledger=[]
    for fac,n in factors:
        if S.Poly(fac,*variables).monic() in allowed_monic:ledger.append([str(fac),int(n)])
        else:kept.append(fac**n)
    polys.append(S.prod(kept));removed.append({'equation':idx,'denominator':str(den),'nonzeroNumeratorFactors':ledger,'rationalUnit':str(unit)})
# k=4 beta t/l is nonzero. In these exact numerators all t denominators cancel.
transformed=[]
for poly in polys:
    num,den=S.fraction(S.factor(poly.subs(beta,l*k/(4*t))))
    assert den==1
    transformed.append(num)
c0t=S.Poly(transformed[2],t)
assert c0t.degree()==1
eq(c0t.nth(1),k*l*l*(l-1)*(2*l-1))
tsol=S.factor(-c0t.nth(0)/c0t.nth(1))
eq(transformed[2].subs(t,tsol),0)
reduced=[];reduced_den=[]
for i in [0,1,3]:
    num,den=S.fraction(S.factor(transformed[i].subs(t,tsol)))
    quotient,rem=S.div(num,l,l);assert rem==0
    reduced.append(S.expand(quotient));reduced_den.append(str(den))
lam=invariant(Lambda0)
lam=S.factor(lam.subs(sol,simultaneous=True).subs(beta,l*k/(4*t)).subs(t,tsol))
num,den=S.fraction(lam)
eq(den,256*k)
norm,rem=S.div(num,l,l);assert rem==0
# Exact multivariate characteristic-zero elimination, including leading-drop fibers.
ctx=fmpq_mpoly_ctx.get(('k','V','l'),'lex')
def fp(ex):return ctx.from_dict({mm:fmpq(str(co)) for mm,co in S.Poly(ex,k,V,l,domain=S.QQ).terms()})
def deg(poly,i):return max(mm[i] for mm in poly.to_dict())
def monic(poly):return poly/poly.leading_coefficient()
known_units=[monic(fp(z)) for z in [l,l-1,2*l-1]]
def full_factor(poly):
    unit,facs=poly.factor();product=ctx.constant(unit)
    for fac,n in facs:product*=fac**n
    assert product==poly
    return unit,facs

def clean_resultant(poly):
    unit,facs=full_factor(poly);kept=ctx.constant(1);parts=[];units=[]
    for fac,n in facs:
        assert deg(fac,0)==0
        if deg(fac,1)==0:
            assert monic(fac) in known_units
            units.append([str(fac),int(n)])
        else:kept*=fac**n;parts.append((fac,int(n)))
    return kept,parts,units
f0,f1,f2,fn=map(fp,reduced+[norm])
raw=[f0.resultant(f1,'k'),f0.resultant(f2,'k'),f1.resultant(f2,'k'),f0.resultant(fn,'k')]
assert [[deg(rr,1),deg(rr,2)] for rr in raw]==[[16,38],[16,34],[16,40],[16,42]]
cl=[clean_resultant(rr) for rr in raw]
expected_parts=[([2,3],1),([10,12],1),([2,2],2)]
ordered=[]
for shape,power in expected_parts:
    candidates=[p for p,n in cl[0][1] if [deg(p,1),deg(p,2)]==shape and n==power]
    assert len(candidates)==1
    ordered.append(candidates[0])
assert len(cl[0][1])==3
assert [[deg(cl[i][0],1),deg(cl[i][0],2)] for i in [1,2,3]]==[[16,20],[16,20],[16,29]]
A2=4*V**2*l**3-12*V**2*l**2+12*V**2*l-4*V**2-12*V*l**3+26*V*l**2-18*V*l+4*V+10*l**3-14*l**2+7*l-1
C2=4*V**2+4*V*l**2+2*V*l-4*V-2*l+1
assert monic(ordered[0])==monic(fp(A2))
assert monic(ordered[2])==monic(fp(C2))
Q=5*l*l-4*l+1
expected_gcd=[l**16*(l-1)**10*Q,l**80*(l-1)**30*(2*l-1)**10*Q,l**16*(2*l-1)**4]
expected_degrees=[[88,88,106],[309,315,405],[59,59,79]]
resultant_ledger=[]
for i,part in enumerate(ordered):
    rr=[part.resultant(cl[j][0],'V') for j in [1,2,3]]
    assert all(deg(z,0)==deg(z,1)==0 for z in rr)
    ds=[deg(z,2) for z in rr];assert ds==expected_degrees[i]
    gcd=rr[0].gcd(rr[1]).gcd(rr[2])
    assert monic(gcd)==monic(fp(expected_gcd[i]))
    for z in rr:assert z%gcd==0
    resultant_ledger.append({'partBidegree':expected_parts[i][0],'partMultiplicity':expected_parts[i][1],'lResultantDegrees':ds,'monicGcd':str(monic(gcd))})
# The only non-excluded l fiber is Q=0. Prove k is in its exact ideal
# by an explicit degree-three multiplier identity, rather than only a reported basis.
Qmon=S.Poly(Q,l).monic().as_expr()
ps=[S.rem(z,Qmon,l) for z in reduced+[norm]]
bound=3
mons=[k**aa*V**bb*l**ell for ell in range(2) for aa in range(bound+1) for bb in range(bound+1-aa)]
cols=[S.Poly(S.rem(m*z,Qmon,l),k,V,l).as_dict() for z in ps for m in mons]
rows=sorted(set().union(*[set(col) for col in cols],{(1,0,0)}))
mat=fmpq_mat([[fmpq(str(col.get(row,0))) for col in cols]+[fmpq(int(row==(1,0,0)))] for row in rows])
rref,rank=mat.rref();nc=len(cols);coefs=[S.Integer(0)]*nc
assert (len(rows),nc,rank)==(72,80,70)
for i in range(rank):
    pivot=next(j for j in range(nc+1) if rref[i,j])
    assert pivot<nc
    coefs[pivot]=S.Rational(str(rref[i,nc]))
multipliers=[S.expand(sum(coefs[i*len(mons)+j]*mon for j,mon in enumerate(mons))) for i in range(4)]
identity=S.expand(sum(c*z for c,z in zip(multipliers,ps))-k)
assert S.rem(identity,Qmon,l)==0
cert_hash=hashlib.sha256(str(multipliers).encode()).hexdigest()
assert cert_hash=='81f5bdb609e64b3a733a08f611e9d03632eed779e8767baee001c2ea7dc834ad'
# Thus every point of Q=0 satisfying the original necessary numerators has k=0,
# contradicting k=4bc*t/l!=0. Boundary l=0,1/2,1 or t=0 is covered by prior proofs.
print(json.dumps({'schema':'r150-unit211-equal-general-20261126-v1','status':'all_original_QQ_checks_and_final_identity_pass','scope':'p=q=1,bc*t*l*(l-1)*(2*l-1) nonzero; all remaining equal-base points excluded','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'originalNumeratorLedger':removed,'reducedDenominators':reduced_den,'kResultantBidegrees':[[deg(z,1),deg(z,2)] for z in raw],'kResultantNonzeroUnits':[z[2] for z in cl],'lResultantLedger':resultant_ledger,'finalFiber':'5*l^2-4*l+1=0','finalCertificate':{'target':'k','multiplierDegreeInKV':3,'multiplierDegreeInL':1,'rows':72,'columns':80,'augmentedRank':70,'multiplierSha256':cert_hash,'identityRemainder':'0'},'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True,default=int))
