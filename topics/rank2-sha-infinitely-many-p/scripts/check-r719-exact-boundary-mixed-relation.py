#!/usr/bin/env python3
"""R719 exact boundary identity over Q(omega), omega^2+omega+1=0.

No output tables are inputs. Rebuild the original R594 algorithm in memory.
Use homogeneous sigma logarithms and python-flint multivariate polynomials.
All arithmetic in this file is executed by public Actions, not an auxiliary
V8 session. No recomputable output is persisted.
Dependencies: python-flint 0.9.0 and Node.js; intended public command:
python check-r719-exact-boundary-mixed-relation.py --workers=4 --taus=2,3,4,5
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, math, multiprocessing, os
from pathlib import Path
import subprocess, sys, time
from flint import fmpq, fmpq_mat, fmpq_mpoly_ctx

START=time.time()
ARG=argparse.ArgumentParser()
ARG.add_argument("--workers",type=int,default=4)
ARG.add_argument("--taus",default="2,3,4,5")
ARGS=ARG.parse_args()
TAUS=[int(t) for t in ARGS.taus.split(",")]
assert TAUS==[2,3,4,5], "the fixed degree-three tau identity uses these four exact values"
Q=fmpq
Z=(Q(0),Q(0));ONE=(Q(1),Q(0));OM=(Q(0),Q(1))
def K(a=0,b=0,d=1):return (Q(a)/Q(d),Q(b)/Q(d))
def ka(x,y):return (x[0]+y[0],x[1]+y[1])
def kn(x):return (-x[0],-x[1])
def ks(x,y):return ka(x,kn(y))
def km(x,y):
    ab=x[1]*y[1]
    return (x[0]*y[0]-ab,x[0]*y[1]+x[1]*y[0]-ab)
def kr(x,c):return (x[0]*c,x[1]*c)
def ki(x):
    d=x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
    assert d
    return ((x[0]-x[1])/d,-x[1]/d)
def kd(x,y):return km(x,ki(y))
def kp(x,n):
    y=ONE
    while n:
        if n&1:y=km(y,x)
        x=km(x,x);n//=2
    return y
def kc(x):return (x[0]-x[1],-x[1])
def ksum(xs):
    s=Z
    for x in xs:s=ka(s,x)
    return s
def kread(x):return (Q(x[0]),Q(x[1]))
def kstr(x):return [str(x[0]),str(x[1])]
def kmod(x,p=1009,w=374):
    def r(a):return (int(a.p)%p)*pow(int(a.q)%p,-1,p)%p
    return (r(x[0])+w*r(x[1]))%p

CAP=30;DEM=12;MAXOBS=36;MAXV=5
FAC=[math.factorial(i) for i in range(100)]
CTX=fmpq_mpoly_ctx.get(("D","E","G","Y","V"),"degrevlex")
PZERO=(CTX.constant(0),CTX.constant(0))
PONE=(CTX.constant(1),CTX.constant(0))
def pa(P,R):return (P[0]+R[0],P[1]+R[1])
def pn(P):return (-P[0],-P[1])
def pr(P,c):return (P[0]*c,P[1]*c)
def pk(P,c):
    return (P[0]*c[0]-P[1]*c[1],
            P[0]*c[1]+P[1]*(c[0]-c[1]))
def trim(A,cap,zmax,vmax):
    return CTX.from_dict({m:c for m,c in A.terms()
      if m[0]+m[1]<=DEM and sum(m[:3])<=cap
      and m[3]+m[4]<=zmax and m[4]<=vmax})
def pm(P,R,cap=CAP,zmax=MAXOBS,vmax=MAXV):
    if P[0].is_zero() and P[1].is_zero():return PZERO
    if R[0].is_zero() and R[1].is_zero():return PZERO
    ac=P[0]*R[0];bd=P[1]*R[1]
    ad=P[0]*R[1];bc=P[1]*R[0]
    return (trim(ac-bd,cap,zmax,vmax),trim(ad+bc-bd,cap,zmax,vmax))
def pdict(P):
    d={m:(c,Q(0)) for m,c in P[0].terms()}
    for m,c in P[1].terms():d[m]=(d.get(m,Z)[0],c)
    return d
def linear_power(row,n,cap,zmax,vmax):
    powers=[[kp(x,j) for j in range(n+1)] for x in row]
    a,b={},{}
    for d in range(min(DEM,cap,n)+1):
      for e in range(min(DEM-d,cap-d,n-d)+1):
       if row[1]==Z and e:continue
       for g in range(min(cap-d-e,n-d-e)+1):
        h=d+e+g
        for v in range(min(vmax,n-h)+1):
         y=n-h-v
         if y<0 or y+v>zmax:continue
         co=ONE
         for j,t in enumerate((d,e,g,y,v)):
            co=km(co,powers[j][t])
         if co==Z:continue
         den=FAC[d]*FAC[e]*FAC[g]*FAC[y]*FAC[v]
         co=kr(co,Q(FAC[n],den))
         m=(d,e,g,y,v)
         if co[0]:a[m]=co[0]
         if co[1]:b[m]=co[1]
    return CTX.from_dict(a),CTX.from_dict(b)

SER=11
def conv(a,b,n=SER):
    return [sum((a[j]*b[i-j] for j in range(i+1)
                 if j<len(a) and i-j<len(b)),Q(0)) for i in range(n+1)]
def spow(a,k,n=SER):
    x=[Q(1)]
    for _ in range(k):x=conv(x,a,n)
    return x
xx=[Q(1),Q(-1,7)]
for n in range(2,SER+1):
    xx.append(sum((xx[j]*xx[n-j] for j in range(1,n)),Q(0))/Q((6*n+1)*(n-1)))
ls=[Q(0)]+[-xx[n]/Q(6*n*(6*n-1)) for n in range(1,SER+1)]
sig=[Q(1)]
for n in range(1,SER+1):
    sig.append(sum((j*ls[j]*sig[n-j] for j in range(1,n+1)),Q(0))/n)
my=[Q(1)]+[-(3*n-1)*xx[n] for n in range(1,SER+1)]
ss2,ss3,ss6=spow(sig,2),spow(sig,3),spow(sig,6)
f3=conv(my,ss6);f1=conv(xx,f3);theta=conv(xx,ss2)
bc=conv(my,ss3)
bc=[x/Q((-27)**n) for n,x in enumerate(bc)]
assert bc[1]==Q(-1,90) and bc[2]==Q(-19,3742200)
def slog(a):
    r=[Q(0)]
    for n in range(1,len(a)):
        r.append(a[n]-sum((j*r[j]*a[n-j] for j in range(1,n)),Q(0))/n)
    return r
LOG={"sig":ls,"f1":slog(f1),"f3":slog(f3),"ss2":slog(ss2),
     "theta":slog(theta),"bc":slog(bc)}

A=[K(-2,1,2),K(4,3,2),K(2,4)]
D=[K(-19,19,174),K(31,-37,58),K(-43,-21,29)]
E=[K(-133,133,429),K(217,-259,143),K(-602,-294,143)]
G=[K(-5843,-3715,858),ka(K(-1593,0,286),K(0,-123,22)),K(1324,-266,143)]
LC=[K(-1),K(1596,0,143),K(-789,526,143)]
RAT=K(-789,526,1596)
BY=K(20,3,17)

def setup(mode,zero):
    if mode=="mass":
        rows=[[D[j],Z if zero else E[j],
                ks(G[j],km(RAT,E[j])) if zero else G[j],Z,Z] for j in range(3)]
        cap,zmax,vmax,base=28,0,0,4
    else:
        i=1 if mode=="frozen1" else 0
        endpoint=mode in ("mixed","W")
        ei=K(-170,-291,9135) if i else K(-170,-117,9135)
        hh=K(-5,-3) if i else K(-5,-9)
        obs=A+[K(2),K(-1)] if i else A+[K(1),K(2)]
        if mode=="W":obs=A+[K(3,6),K(4)]
        wr=[ka(D[j],kr(km(ei,A[j]),5)) for j in range(3)]+[kr(ei,-87),kr(ei,-29)]
        if endpoint:
            v=[kr(x,5) for x in A]+([K(-24),K(97)] if i else [K(39),K(-92)])
            wr=[ka(x,kr(km(hh,v[j]),Q(1,315))) for j,x in enumerate(wr)]
        er=E+[Z,Z];gr=G+[Z,Z]
        dr=[Z]*5
        if mode=="mixed":
            wo=A+[K(3,6),K(4)]
            dr=[ks(x,km(BY,obs[j])) for j,x in enumerate(wo)]
        rows=[[wr[j],Z if zero else er[j],
               ks(gr[j],km(RAT,er[j])) if zero else gr[j],obs[j],dr[j]] for j in range(5)]
        cap,zmax,vmax,base=CAP,(30 if mode.startswith("frozen") else 36),(5 if mode=="mixed" else 0),6
    lc=[LC[0],Z,ks(LC[2],km(RAT,LC[1]))] if zero else LC
    rows.append(lc+[Z,Z])
    return rows,cap,zmax,vmax,base

def generate(job):
    mode,zero=job
    rows,cap,zmax,vmax,base=setup(mode,zero)
    nmax=(cap+zmax-base)//6
    print("exact generator",mode,zero,"nmax",nmax,flush=True,file=sys.stderr)
    terms=len(rows)-1
    # Both flat terms have the same sigma tail and the complete B_C factor.
    names_plus=["f1","ss2"]+["sig"]*(terms-2)+["bc"]
    names_minus=["f3","theta"]+["sig"]*(terms-2)+["bc"]
    powcache={}
    def lp(j,n):
        key=(j,n)
        if key not in powcache:powcache[key]=linear_power(rows[j],n,cap,zmax,vmax)
        return powcache[key]
    logs=[]
    for n in range(1,nmax+1):
        common=PZERO
        for j in range(2,len(rows)):
            nm="bc" if j==len(rows)-1 else "sig"
            common=pa(common,pr(lp(j,6*n),LOG[nm][n]))
        plus=pa(common,pa(pr(lp(0,6*n),LOG["f1"][n]),pr(lp(1,6*n),LOG["ss2"][n])))
        minus=pa(common,pa(pr(lp(0,6*n),LOG["f3"][n]),pr(lp(1,6*n),LOG["theta"][n])))
        logs.append((plus,minus))
    prefplus=pm(lp(0,1),lp(1,2),cap,zmax,vmax)
    prefminus=lp(0,3)
    for j in range(2,terms):
        prefplus=pm(prefplus,lp(j,1),cap,zmax,vmax)
        prefminus=pm(prefminus,lp(j,1),cap,zmax,vmax)
    Fs=[[prefplus],[prefminus]]
    result={}
    for n in range(nmax+1):
        if n:
            for side in (0,1):
                val=PZERO
                for k in range(1,n+1):
                    val=pa(val,pr(pm(logs[k-1][side],Fs[side][n-k],cap,zmax,vmax),Q(k,n)))
                Fs[side].append(val)
        out=pr(pa(Fs[0][n],pn(Fs[1][n])),Q(-1 if mode=="frozen1" else 1,42))
        for m,c in pdict(out).items():
            d,e,g,y,v=m;deg=d+e+g
            allowed=(deg in (0,4,10,16,22,28)) if mode=="mass" else (deg in (0,6,12,18,24,30))
            if not allowed:continue
            if mode=="mass":
                if y or v:continue
            elif mode=="mixed":
                if (y+v)%6 or y+v>36:continue
            elif v or y%6:continue
            # k! changes the epsilon coefficient into the actual Z^k moment.
            c=kr(c,FAC[v])
            if c!=Z:result[(d,e,g,y,v)]=kstr(c)
    print("exact generator done",mode,zero,"entries",len(result),"seconds",round(time.time()-START,2),flush=True,file=sys.stderr)
    return mode,zero,result

def p_add(P,R,c=ONE):
    Qd=dict(P)
    for m,a in R.items():
        v=ka(Qd.get(m,Z),km(c,a))
        if v==Z:Qd.pop(m,None)
        else:Qd[m]=v
    return Qd
def p_mul(P,R):
    Qd={}
    for a,x in P.items():
      for b,y in R.items():
        m=tuple(a[i]+b[i] for i in range(3))
        Qd[m]=ka(Qd.get(m,Z),km(x,y))
    return {m:x for m,x in Qd.items() if x!=Z}
def p_shift(P,h):return {(d,e,g+h):v for (d,e,g),v in P.items()}
def p_e0(P):return {m:v for m,v in P.items() if m[1]==0}
def p_der2(P):
    return {(d-2,e,g):kr(v,d*(d-1)) for (d,e,g),v in P.items() if d>=2}
def matrix_mul(A,B):
    return [[ksum(km(a,b) for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def read_poly(P):return {tuple(map(int,m.split(","))):kread(v) for m,v in P.items()}
def vec_add(x,y):return [ka(a,b) for a,b in zip(x,y)]
def vec_sub(x,y):return [ks(a,b) for a,b in zip(x,y)]
def vec_scale(x,c):return [km(a,c) for a in x]
def dot(x,y):return ksum(km(a,kc(b)) for a,b in zip(x,y))
def perp(x,y):return vec_sub(x,vec_scale(y,kd(dot(x,y),dot(y,y))))
def B_polys():
    ar=[K(1,2),K(2,4),K(3,1),K(2,-1),Z,Z]
    dr=[K(1),K(-1,-1),K(0,-2),Z,Z,Z]
    cr=vec_scale([K(1),Z,K(-1),K(1),Z,Z],ki(K(1,2)))
    hr=[K(-1),K(2),K(0,1),K(1,1),Z,Z]
    br=[K(426,263),K(63),K(121,342),K(-305,79),K(2,-71),K(217,77)]
    ds=perp(dr,ar);cp=perp(cr,ds);hp=perp(hr,ds)
    er=vec_scale(cp,K(14));gp=vec_add(vec_scale(hp,K(13)),vec_scale(cp,K(3,-2)))
    bp=perp(perp(br[:4]+[Z,Z],ar),ds)
    ab=None
    for i in range(6):
      for j in range(i+1,6):
        den=ks(km(er[i],gp[j]),km(er[j],gp[i]))
        if den!=Z:
          aa=kd(ks(km(bp[i],gp[j]),km(bp[j],gp[i])),den)
          bb=kd(ks(km(er[i],bp[j]),km(er[j],bp[i])),den)
          ab=(aa,bb);break
      if ab:break
    assert ab
    aa,bb=ab
    assert vec_add(vec_scale(er,aa),vec_scale(gp,bb))==bp
    P={(0,j,6-j):kr(km(kp(aa,j),kp(bb,6-j)),math.comb(6,j)) for j in range(7)}
    return P,{(0,0,6):kp(bb,6)}

if __name__=="__main__":
    path=Path(__file__).with_name("check-r594-two-source-six-carry-compensation.js")
    raw=subprocess.check_output(["node",str(path)],text=True)
    source=json.loads(raw)
    inputsha=hashlib.sha256(path.read_bytes()).hexdigest()
    jobs=[(mode,zero) for mode in ("frozen0","frozen1","mixed","W","mass") for zero in (False,True)]
    data={}
    with concurrent.futures.ProcessPoolExecutor(max_workers=ARGS.workers,mp_context=multiprocessing.get_context("fork")) as ex:
        for mode,zero,d in ex.map(generate,jobs):
            data[(mode,zero)]={m:(Q(v[0]),Q(v[1])) for m,v in d.items()}
    def moment(P,mode,y=0,v=0,zero=False):
        Dd=data[(mode,zero)]
        return ksum(kr(km(c,Dd.get((d,e,g,y,v),Z)),FAC[d]*FAC[e]*FAC[g])
                    for (d,e,g),c in P.items())
    assert data[("mixed",False)].get((0,0,0,6,0),Z)==ONE
    assert data[("W",False)].get((0,0,0,6,0),Z)==K(6,12)
    assert data[("mixed",False)].get((0,0,0,5,1),Z)==K(33,84,17)
    BP,BP0=B_polys()
    AP=[[kread(v) for v in R] for R in source["matrix"]["Aplus"]]
    AZ=[[kread(v) for v in R] for R in source["matrix"]["Azero"]]
    BMs=[[[kread(v) for v in R] for R in M] for M in source["polynomial_right_inverse"]["B"]]
    base=read_poly(source["matrix"]["base"])
    cols=[read_poly(P) for P in source["matrix"]["polys"]]
    piv=[0,1,2,3,4,13,15,16,17,18,19]
    labels=[("frozen0",6*j,0) for j in range(6)]+[("frozen1",6*j,0) for j in range(6)]
    labels += [("mixed",6*j,0) for j in range(6)]+[("W",6*j,0) for j in range(1,7)]
    for k in range(1,6):
      for j in range(6):
        r=6-k+6*j;odd=r%2;a=(31-r)//2 if odd else (34-r)//2
        if a>=0:labels.append(("mixed",r,k))
    assert len(labels)==52
    selected=list(range(23))+[25,26,36,37,47,48]+list(range(104,111))+list(range(116,122))+list(range(127,132))+list(range(137,141))+[147]
    assert len(selected)==52
    def family(tau):
        at=[[ka(a,kr(b,tau)) for a,b in zip(r,s)] for r,s in zip(AP,AZ)]
        bt=[[kr(ka(a,kr(b,tau)),Q(1,tau-1)) for a,b in zip(r,s)] for r,s in zip(BMs[0],BMs[1])]
        ba=matrix_mul(bt,at)
        pi=[[ks(ONE if i==j else Z,ba[i][j]) for j in range(20)] for i in range(20)]
        ds=[]
        for j in piv:
            P={}
            for i,C in enumerate(cols):P=p_add(P,C,pi[i][j])
            ds.append(P)
        ext=[(p_shift(P,6*h),False) for h in range(5) for P in ds]
        ext += [(p_shift(P,6*h),True) for h in range(4) for P in ds]
        for i in range(1,6):
          for j in range(13-i):
            P={};g=12-i-j
            for a in range(i+1):
              for bb in range(j+1):
                co=K(((-1)**a)*math.comb(i,a)*math.comb(j,bb)*(13**bb),0,14**(i+j))
                m=(a+bb,i+j-a-bb,g)
                P[m]=ka(P.get(m,Z),co)
            ext.append(({m:c for m,c in P.items() if c!=Z},False))
        assert len(ext)==149
        rhs=[ks(ks(kread(x),kread(y)),kr(kread(z),tau))
             for x,y,z in zip(source["matrix"]["target"],source["matrix"]["basePlus"],source["matrix"]["baseZero"])]
        xp=matrix_mul(bt,[[v] for v in rhs])
        Pold=dict(base)
        for i,C in enumerate(cols):Pold=p_add(Pold,C,xp[i][0])
        return ext,Pold
    def evaluate(P,isB,lab,tau,eta,derivative=False):
        mode,y,v=lab
        if derivative:P=p_der2(P)
        E0=p_e0(P)
        if isB:
            full=p_mul(P,BP);cut=p_mul(E0,BP);cut0=p_mul(E0,BP0)
        else:full=P;cut=E0;cut0=E0
        return ka(moment(full,mode,y,v),
          kr(ka(moment(cut,mode,y,v),kr(moment(cut0,mode,y,v,True),eta)),tau-1))
    def make(tau,eta):
        ext,old=family(tau)
        mat=[[evaluate(P,B,lab,tau,eta) for P,B in ext] for lab in labels]
        jrow=[evaluate(P,B,("mass",0,0),tau,eta,True) for P,B in ext]
        oval=[evaluate(old,False,lab,tau,eta) for lab in labels]
        jold=evaluate(old,False,("mass",0,0),tau,eta,True)
        return mat,jrow,oval,jold
    print("exact 52-row boundary matrix",flush=True,file=sys.stderr)
    M,J,O,JO=make(2,1)
    # Solve M_selected^T c = J_selected over K by its rational regular representation.
    R=[[Q(0) for _ in range(104)] for __ in range(104)]
    rhs=[[Q(0)] for _ in range(104)]
    for i,col in enumerate(selected):
        rhs[2*i][0]=J[col][0];rhs[2*i+1][0]=J[col][1]
        for j in range(52):
            a,b=M[j][col]
            R[2*i][2*j]=a;R[2*i][2*j+1]=-b
            R[2*i+1][2*j]=b;R[2*i+1][2*j+1]=a-b
    sol=fmpq_mat(R).solve(fmpq_mat(rhs),algorithm="dixon")
    co=[(sol[2*j,0],sol[2*j+1,0]) for j in range(52)]
    coeff_json=json.dumps([kstr(x) for x in co],separators=(",",":"))
    print("exact relation solved",len(coeff_json),"bytes",flush=True,file=sys.stderr)
    cases=[];verified=True;first_fail=None
    for tau in TAUS:
      for eta in (1,-1):
        MM,JJ,OO,JOO=make(tau,eta)
        failures=[]
        for j in range(149):
            rem=ks(JJ[j],ksum(km(co[i],MM[i][j]) for i in range(52)))
            if rem!=Z:failures.append((j,rem))
        aff=ks(JOO,ksum(km(x,y) for x,y in zip(co,OO)))
        ok=not failures and aff==Z
        verified &= ok
        if not ok and first_fail is None:
            first_fail={"tau":tau,"eta":eta,"column":failures[0][0] if failures else "affine",
                        "value":kstr(failures[0][1] if failures else aff)}
        cases.append({"tau":tau,"eta":eta,"all_149_columns":not failures,"affine_zero":aff==Z,
                      "nonzero_columns":len(failures)})
    # Fixed full-source target for the symmetric three-S family.
    def cser(a,k,n):
        return spow(a,k,n)
    Sbase=conv(spow(sig,34,5),spow(xx,14,5),5)
    # S has x^14[1-53/(7X)-12/(7X^2)-80/(7X^3)-128/(7X^4)] and starts z^6.
    Sjet=[Q(0)]*6
    sco=[Q(0),Q(1),Q(-53,7),Q(-12,7),Q(-80,7),Q(-128,7)]
    for j in range(6):
        if not sco[j]:continue
        cv=conv(spow(sig,34,5),spow(xx,17-3*j,5),5)
        for h in range(j,6):Sjet[h]+=sco[j]*cv[h-j]
    Wjet=[data[("W",False)].get((0,0,0,6*j,0),Z) for j in range(1,7)]
    target=[K(Sjet[j]) for _ in range(3) for j in range(6)]+Wjet+[Z]*28
    dsym=ks(ONE,ksum(km(x,y) for x,y in zip(co,target)))
    # The raw symmetry/density implication is reported only after the exact identity.
    dden=1
    for x in co:
        for a in x:dden=math.lcm(dden,int(a.q))
    out={"format":"R719 exact boundary relation over Q(omega)",
         "source_input_sha256":inputsha,"taus":TAUS,"eta_values":[1,-1],
         "complete_hidden_degrees":[6,12,18,24,30],"maximum_original_total_moment":66,
         "old_and_mixed_row_labels":labels,"actual_selected_columns":selected,
         "coefficients_sha256":hashlib.sha256(coeff_json.encode()).hexdigest(),
         "coefficient_json_bytes":len(coeff_json),
         "coefficients":json.loads(coeff_json) if len(coeff_json)<=22000 else None,
         "coefficients_mod1009":[kmod(x) for x in co],
         "fixed_denominator_bits":dden.bit_length(),
         "fixed_denominator_sha256":hashlib.sha256(str(dden).encode()).hexdigest(),
         "all_exact_identities_verified":verified,"cases":cases,"first_failure":first_fail,
         "symmetric_target_remainder":kstr(dsym),
         "symmetric_target_remainder_mod1009":kmod(dsym),
         "neutral_target_remainder":["1","0"],
         "scope":"Four exact tau values prove a degree <=3 polynomial identity after multiplying by tau-1. This is the kappa=u=0 boundary; actual corrections in (kappa,u) are not discarded.",
         "seconds":round(time.time()-START,3),"outputs_persisted":False}
    print(json.dumps(out,separators=(",",":")))
