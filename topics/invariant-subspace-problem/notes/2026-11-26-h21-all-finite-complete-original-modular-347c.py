#!/usr/bin/env python3
"""NEW direct COMPLETE-original modular probe after the 12-equation timeout.
This gate starts from all 39 generators; it never reruns the 12-only GB.
Not a characteristic-zero theorem.
H 2+1, Hp=0, all four physical sources finite, rankV=2, essT3=6.
s,w are H sources, x=alpha+beta,z=alpha*beta. Auxiliary l=lambda^2,
v=scale(Sstar)^2, q=mu/lambda, t=scale(P-S)/scale(Sstar), h=1/k(s,w).
The first 12 equations retain all physical nonzero assumptions:
v*qpair*Ns=e forces qpair*Ns nonzero;
l*q^2*bs=b forces l*q*bs nonzero;
4*e^2*Ns*l=Delta*qpair forces Delta nonzero;
h*k=1 forces k and w-s nonzero.
Ns contains (s^2-s*x+z)^2, so source-factor division is paid.
The original highest Hermite equations and original full N/cubic
coefficients are generated below. No arbitrary N-matrix zero is imposed.
"""
import os,sys,time,json,hashlib,subprocess,shutil,tempfile
import sympy as S
from flint import fmpz_mpoly_ctx
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
p,ee=1031,700
iv=lambda a:pow(int(a)%p,-1,p)
need((16*ee**9-108*ee**8+36*ee**7-15*ee**6+18*ee**4-1)%p==0,"original G9 root")
bb=-(2*ee**3+1)*iv(6)%p;cc=-iv(4)%p
QQ=(4*ee**3-1)%p;DD=(2*ee**3+1-12*ee**4)%p;RR=DD*iv(QQ)%p
need(ee*bb*QQ*DD*(1-ee)*(1-2*ee)*(QQ+6*ee)%p!=0,"all constant chart units at actual prime")
h,l,v,q,t,s,w,x,z,r,a=S.symbols('h l v q t s w x z r a')
gens=(h,l,v,q,t,s,w,x,z)
def ker(u,vv):
 return S.expand(-(vv-u)**2*(u**3-5*u*u+(u**3-3*u*u+22*u)*vv-(3*u*u+3*u+5)*vv*vv+(u+1)*vv**3))
rem=S.rem(ker(s,a),a*a-x*a+z,a)
As=S.Poly(rem,a).nth(0);Bs=S.Poly(rem,a).nth(1)
Ar,Br=As.subs(s,r),Bs.subs(s,r)
Aw,Bw=As.subs(s,w),Bs.subs(s,w)
Ns=S.expand(As*As+As*Bs*x+Bs*Bs*z)
Nr=S.expand(Ar*Ar+Ar*Br*x+Br*Br*z)
Sstar=S.expand(As*Br-Bs*Ar)
J0=S.expand(As*S.diff(Bs,s)-Bs*S.diff(As,s))
need(S.expand(Sstar.subs(r,s))==0,"Sstar original source value")
need(S.expand(S.diff(Sstar,r).subs(r,s)-J0)==0,"Sstar original source derivative")
Es=s*s-s*x+z
Jred,jrem=S.div(S.Poly(J0,z),S.Poly(Es,z))
need(jrem.is_zero,"entire physical source-factor identity")
Jred=S.expand(Jred.as_expr())
C3,crem=S.div(S.Poly(Sstar.subs(r,w)-(w-s)*J0,w),S.Poly((w-s)**2,w))
need(crem.is_zero,"entire original double-source identity")
C3=S.expand(C3.as_expr())
DH=(r-s)**2*(r-w);EV=r*r-x*r+z;ZZ=S.expand(DH*EV)
Bstar,Brmd=S.div(S.Poly(Sstar,r),S.Poly(DH,r))
Bstar=S.expand(Bstar.as_expr())
need(S.expand(Sstar-DH*Bstar-Brmd.as_expr())==0,"monic Bstar division identity")
B0=S.expand(Bstar.subs(r,s));B1=S.expand(S.diff(Bstar,r).subs(r,s));Bww=S.expand(Bstar.subs(r,w))
Ew=w*w-x*w+z
ksw=ker(s,w);ks=S.diff(ksw,s);bs=-2*s*s*(s-2)*(s+6)
delta=x*x-4*z
qpair=x**3-5*x*x+x*x*z-6*x*z+32*z-5*z*z
lst2=S.expand(2*As*Aw+(As*Bw+Bs*Aw)*x+2*Bs*Bw*z)
Wnum=S.expand(ksw*S.diff(Ns,s)-2*Ns*ks)
K=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
KM=3200*K.inv();need(all(a.q==1 for a in KM),"integer inverse norm matrix")
zc=S.Matrix([S.Poly(ZZ,r).nth(i) for i in range(6)])
Zn=S.expand((zc.T*KM*zc)[0])
eqs=[
 ("source_derivative",Jred),
 ("isolated_H_source",C3),
 ("Sstar_scale",v*qpair*Ns-ee),
 ("lambda_scale",4*ee*ee*Ns*l-delta*qpair),
 ("jet_norm",l*q*q*bs-bb),
 ("genuine_H_pairing",h*ksw-1),
 ("complete_jet_ratio",q*Wnum+4*bb*Ns*ksw),
 ("complete_single_ratio",lst2-2*RR*l*ksw*Ns),
 ("highest_s_value",2*ee*Es*t-(1-2*ee)*B0),
 ("highest_w_value",(QQ+6*ee)*Bww+6*ee*t*Ew),
 ("highest_s_derivative",q*((1-2*ee)*B1-2*ee*t*(2*s-x))-4*bb*B0),
 ("original_mean_norm",v*t*t*Zn-6400*(1-ee)),
]
ctx=fmpz_mpoly_ctx.get(tuple(str(g) for g in gens))
def red(ex):
 poly=S.Poly(ex,*gens)
 outd={}
 for mon,coef in poly.terms():
  need(coef.q==1,"only integer pre-modular coefficients")
  c=int(coef)%p
  if c>p//2:c-=p
  if c:outd[mon]=c
 return ctx.from_dict(outd)
def meta(f):
 return dict(degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
ge=[]
for label,expr in eqs:
 ff=red(expr);need(bool(ff),label+" nonzero polynomial")
 ge.append(ff);out("original_equation",label=label,**meta(ff))
# Exact original polar formulas in this chart. Inverses below are only
# nonzero constants of the selected coefficient field. All variable units
# were enforced by the twelve original equations.
ctx10=fmpz_mpoly_ctx.get(tuple(str(g) for g in gens)+(str(r),))
def cv10(ex):
 outd={}
 for mon,coef in S.Poly(ex,*gens,r).terms():
  need(coef.q==1,"integer factor before modular expansion")
  c=int(coef)%p
  if c>p//2:c-=p
  if c:outd[mon]=c
 return ctx10.from_dict(outd)
hh,ll,vv,qq,tt,ss,ww,xx,zz,rr=ctx10.gens()
FF=cv10(ker(s,r));JJ=cv10(S.diff(ker(s,r),s));GG=cv10(ker(w,r))
KS=cv10(ks);BB=cv10(bs);QP=cv10(qpair)
SS=cv10(Sstar);ZZP=cv10(ZZ);NN=cv10(Nr)
jpart=qq*(JJ-hh*KS*FF)
Hcal=2*ll*FF*(jpart+cc*FF)+iv(2)*qq**2*BB*iv(bb)*hh**2*GG**2
Jcal=bb*ll*FF**2+(jpart+2*cc*FF)*hh*GG
Omega=vv*QP*qq**2*BB*iv(4*ee*ee*bb)
Pstar=SS+tt*ZZP
Ncal=vv*(Pstar**2+2*ee*SS**2)+4*ee*Omega*NN-2*Hcal+4*Jcal
Ccal=vv*(Pstar**3+2*SS**3)-6*Pstar*Hcal+6*Omega*SS*NN
full=[]
for label,pol in (("N",Ncal),("highest",Ccal)):
 slots=[{} for _ in range(max(0,int(pol.degrees()[-1]))+1)]
 for mon,coef in pol.to_dict().items():
  c=int(coef)%p
  if c>p//2:c-=p
  if c:slots[mon[-1]][mon[:-1]]=c
 for i,terms in enumerate(slots):
  ff=ctx.from_dict(terms)
  if ff:
   full.append(ff);out("complete_original_coefficient",label=label,index=i,**meta(ff))
need(int(Ncal.degrees()[-1])<=10 and int(Ccal.degrees()[-1])<=15,"full original degrees")
sing=shutil.which("Singular")
need(sing is not None,"Singular dependency must be installed by the dedicated workflow")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr)[:4000])
script="ring isp=1031,(h,l,v,q,t,s,w,x,z),dp;\noption(redSB);\n"
script+="ideal I="+",\n".join(map(str,ge+full))+";\n"
script+='print("ISP_BEGIN_DIRECT_COMPLETE_ORIGINAL");\nideal G=slimgb(I);\nprint("ISP_COMPLETE_BASIS_SIZE");print(size(G));\n'
script+='if (size(G)==1 && G[1]==1) {print("ISP_MODULAR_UNIT_COMPLETE");}\nelse {print("ISP_MODULAR_NONUNIT_COMPLETE");print(dim(G));print(vdim(G));}\nquit;\n'
out("singular_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),physical_variables=["s","w","x","z"],auxiliary_variables=["h","l","v","q","t"],geometric_count=len(ge),complete_coefficient_count=len(full),constant_prime=p,constant_e=ee)
with tempfile.TemporaryDirectory(prefix="isp-h21-finite-original-") as td:
 path=os.path.join(td,"input.sing")
 with open(path,"w") as o:o.write(script)
 try:
  rr=subprocess.run([sing,"-q",path],capture_output=True,text=True,timeout=180)
  output=rr.stdout+rr.stderr
  outcome=("unit_twelve" if "ISP_MODULAR_UNIT_TWELVE" in output else
           "unit_complete" if "ISP_MODULAR_UNIT_COMPLETE" in output else
           "nonunit_complete" if "ISP_MODULAR_NONUNIT_COMPLETE" in output else "unresolved_or_error")
  out("singular_output",returncode=rr.returncode,outcome=outcome,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  out("singular_bounded_timeout",outcome="unresolved",limit_seconds=180,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
out("complete_probe",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="modular direction only; no QQ/Ke/complex exclusion claim")
