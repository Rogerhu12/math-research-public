#!/usr/bin/env python3
"""NEW LOWERED exact Ke gate: original jet d-degree8 is reduced to2.
Success requires actual characteristic-zero I*C=1.
The known modular GB is not rerun and is not used as a QQ certificate.
"""
import os,sys,time,json,hashlib,subprocess,shutil,tempfile
import sympy as S
from flint import fmpz_mpoly_ctx
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
ee=S.symbols("e")
QQ=4*ee**3-1
DD=2*ee**3+1-12*ee**4
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

# New elimination input: five scale auxiliaries removed, highest-w and
# mean-norm equations reduced to quadratics in d=w-s.
# This is a change of mathematical input after the 180s unresolved
# nine-variable probe, not a rerun of that computation.
n,d=S.symbols("n d")
de=S.Poly(Sstar.subs(r,s+d),d)
need(S.expand(de.nth(0))==0 and S.expand(de.nth(1)-J0)==0,"original Taylor coefficients")
U,V,W4,L=[S.expand(de.nth(i)) for i in (2,3,4,5)]
CD=S.expand(C3.subs(w,s+d))
need(S.expand(CD-U-d*V-d*d*W4-d**3*L)==0,"entire cubic Taylor identity")
B0d=S.expand(B0.subs(w,s+d));B1d=S.expand(B1.subs(w,s+d));Bwd=S.expand(Bww.subs(w,s+d))
need(S.expand(d*B0d+U-CD)==0,"only paid d division in source quotient")
need(S.expand(B1d-W4-d*L)==0,"source quotient derivative")
need(S.expand(Bwd-V-2*d*W4-3*d*d*L)==0,"isolated quotient value")
Qn,qr=S.div(S.Poly(Ns,z),S.Poly(Es**2,z))
need(qr.is_zero,"exact original source norm factor")
Qn=S.expand(Qn.as_expr())
qs0,qr=S.div(S.Poly(-ksw,w),S.Poly((w-s)**2,w))
need(qr.is_zero,"exact original kernel diagonal factor")
qs0=S.expand(qs0.as_expr())
Wmid,wr=S.div(S.Poly(Wnum,w),S.Poly(w-s,w))
need(wr.is_zero,"exact W diagonal factor")
Wred,wr=S.div(S.Poly(Wmid.as_expr(),z),S.Poly(Es,z))
need(wr.is_zero,"exact W source factor")
Wred=S.expand(Wred.as_expr())
Wd=S.expand(Wred.subs(w,s+d));qd=S.expand(qs0.subs(w,s+d))
Znd=S.expand(Zn.subs(w,s+d));Ls2=S.expand(lst2.subs(w,s+d))
need(S.Poly(Znd,d).degree()<=2,"dual norm is quadratic in isolated source")
c0=1-2*ee;H0=QQ+6*ee;Re=2*ee**3+1
H2=S.expand((H0*Es*W4+3*c0*U)*d*d+(2*H0*Es*V+3*c0*(2*s-x)*U)*d+12*ee*(ee*ee+1)*Es*U)
# This identity is now checked universally over QQ[e], before any field computation.
hcheck=S.Poly(d*(H0*Es*Bwd+3*c0*B0d*((s+d)**2-x*(s+d)+z))+H2-(3*H0*Es+3*c0*((s+d)**2-x*(s+d)+z))*CD,d,z,x,s)
need(S.expand(hcheck.as_expr())==0,"highest single-point quadratic identity over QQ[e]")

# Build large universal polynomials using FLINT, rather than expanding them
# through Sympy. The proof field is Ke=QQ[e]/G9; e remains symbolic here.
gens6=(n,d,z,x,s,ee)
ctx6=fmpz_mpoly_ctx.get(tuple(map(str,gens6)))
def cv(ex):
 dd={}
 for mon,c in S.Poly(ex,*gens6).terms():
  need(c.q==1,"integer universal coefficient")
  if c:dd[mon]=int(c)
 return ctx6.from_dict(dd)
NN,DDvar,ZZvar,XXvar,SSvar,EE=ctx6.gens()
US,VS,WS,LS=map(cv,(U,V,W4,L))
ES,QN,QP,DS,BS,WD,QW,ZN,L2,B1S,EP=map(cv,(Es,Qn,qpair,delta,bs,Wd,qd,Znd,Ls2,B1d,2*s-x))
C0=1-2*EE;RE=2*EE**3+1;QF=4*EE**3-1;DF=2*EE**3+1-12*EE**4
Pi=SSvar*(SSvar-2)*(SSvar+6)*DDvar*DS*QP*ES*QN*QW
polys=[
 ("source_Jred",cv(Jred)),
 ("source_C3",cv(CD)),
 ("highest_w_quadratic",cv(H2)),
 ("mean_norm_quadratic",C0**2*US**2*ZN-25600*EE*(1-EE)*QP*QN*ES**4*DDvar**2),
 ("original_jet_scale",3*EE**2*WD**2+2*RE*DS*QP*BS*QN*DDvar**2*QW**2),
 ("original_single_ratio",2*EE**2*QF*L2+DF*DS*QP*DDvar**2*QW),
 ("highest_source_derivative",WD*US+C0*QN*DDvar**2*QW*B1S*ES+C0*QN*DDvar*QW*US*EP),
 ("original_physical_units",NN*Pi-1),
]
expected=[
"19bc341ee6dd27f8216e6d5003ac6db37b13e28c4894d27f4ebf4db66c9770f2",
"9e44c51f99a96cd9e75b6a9778fac940970d06c3f385611a4424c63295a088f6",
"12a5b564fc0d93a2cfaba7d5526c13abe724d57b35f5ee2a0b6d8d4dad00e347",
"47c625d943bf791c06e8f954c7a5a9ee056a67f457b9201b01ba262a77237c94",
"0126c8527aa0b4190b7e0ac9fd3120408258d8cfb790fefe883e669fdc49552a",
"86c48a24fd9a0336c3ccccd6ef2590f270c70eb2135de74b0f73e99c00e34817",
"e7739330a0f5408ab7409794a179ac741d49cfb6bf08bd67a3038737f7b19707",
"fc213ed7bacd67885785f1d6e2ae2a356677f2ad53491f274d356b61d455cfe8"]
ctx5=fmpz_mpoly_ctx.get(('n','d','z','x','s'))
def spec_hash(f):
 dic={}
 for mon,c in f.to_dict().items():
  key=mon[:-1]
  dic[key]=(dic.get(key,0)+int(c)*pow(700,mon[-1],1031))%1031
 dic={m:(c if c<=515 else c-1031) for m,c in dic.items() if c}
 return hashlib.sha256(str(ctx5.from_dict(dic)).encode()).hexdigest()
for (label,f),oldsha in zip(polys,expected):
 need(bool(f),label+" universal nonzero")
 got=spec_hash(f);need(got==oldsha,label+" exact agreement with frozen modular input")
 out("universal_original_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest(),frozen_modular_sha256=got)
out("frozen_input_identity_complete",run_id=45807166646,job_id=139865351533,source_git_blob="8d084112f3c15ba913a54ee4fb97868154200b0c",no_modular_groebner_rerun=True)

# Exact universal transition from the frozen original seven equations to
# the lower-degree equations. No new open subset and no modular GB call.
old=dict(polys)
JF=old["source_Jred"];CF=old["source_C3"];HF=old["highest_w_quadratic"]
NF=old["mean_norm_quadratic"];GF=old["original_jet_scale"]
KF=old["original_single_ratio"];VF=old["highest_source_derivative"]
AF=cv(S.diff(Jred,s))
need(not(2*US-EP*JF-ES*AF),"2U=Esprime*Jred+Es*partial_s(Jred)")
TF=AF*(DDvar*EP-ES)-2*DDvar*VS
Cnew=ES*AF+2*DDvar*VS+2*DDvar**2*WS+2*DDvar**3*LS
H0=QF+6*EE
Hnew=(2*H0*WS+3*C0*AF)*DDvar**2+(4*H0*VS+3*C0*EP*AF)*DDvar+12*EE*(EE**2+1)*ES*AF
Nnew=C0**2*AF**2*ZN-102400*EE*(1-EE)*QP*QN*ES**2*DDvar**2
Vnew=WD*AF+C0*QN*QW*TF
Gnew=3*EE**2*C0**2*QN*TF**2+2*RE*DS*QP*BS*AF**2*DDvar**2
need(not(2*CF-Cnew-EP*JF),"cubic universal transition")
HU=3*C0*DDvar**2+3*C0*EP*DDvar+12*EE*(EE**2+1)*ES
need(not(2*HF-ES*Hnew-EP*JF*HU),"highest quadratic universal transition")
need(not(4*NF-ES**2*Nnew-C0**2*EP*JF*(2*US+ES*AF)*ZN),"mean norm universal transition")
need(not(2*VF-ES*Vnew-ES*C0*QN*QW*Cnew-EP*JF*(WD+C0*QN*DDvar*QW*EP)),"highest derivative universal transition")
need(not(AF**2*GF-QN*QW**2*Gnew-3*EE**2*(AF*WD-C0*QN*QW*TF)*Vnew),"jet norm universal transition")
polys=[
 ("source_Jred",JF),("lowered_source_cubic",Cnew),
 ("lowered_highest_w_quadratic",Hnew),("lowered_mean_norm_quadratic",Nnew),
 ("lowered_original_jet_quadratic",Gnew),("original_single_ratio",KF),
 ("lowered_highest_source_derivative",Vnew),("original_physical_units",old["original_physical_units"])]
for label,f in polys:
 need(bool(f),label+" exact nonzero")
 out("lowered_original_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
out("universal_lowering_identities_complete",count=6,new_open_factors=[],unit_A_reason="lowered norm and old Pi",unit_T_reason="lowered jet and old Pi plus A",scope="exactly equivalent to frozen original seven equations on the SAME original Pi chart")
sing=shutil.which("Singular");need(sing is not None,"dedicated Singular dependency")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script="ring isp=(0,e),(n,d,z,x,s),dp;\n"
script+="minpoly=(16*e^9-108*e^8+36*e^7-15*e^6+18*e^4-1)/16;\noption(redSB);\n"
script+='number fieldcheck=16*e^9-108*e^8+36*e^7-15*e^6+18*e^4-1;\nif(fieldcheck!=0){print("ISP_KE_FIELD_RELATION_FAILED");quit;}\nprint("ISP_KE_FIELD_RELATION_VERIFIED");\n'
script+='print("ISP_BEGIN_KE_LIFT_SMOKE");\nideal smoke=s,s-1;matrix smokeU;matrix smokeC=lift(smoke,ideal(1),smokeU,"slimgb");matrix smokeP=matrix(smoke)*smokeC;\n'
script+='if (nrows(smokeP)!=1 || ncols(smokeP)!=1 || smokeP[1,1]!=1) {print("ISP_KE_LIFT_SMOKE_FAILED");quit;}\n'
script+='print("ISP_KE_LIFT_SMOKE_VERIFIED");\n'
script+="ideal I="+",\n".join(str(f) for label,f in polys)+";\n"
script+='if(size(I)!=8){print("ISP_KE_ORIGINAL_INPUT_SIZE_FAILED");quit;}\nprint("ISP_BEGIN_TRUE_KE_ORIGINAL_LIFT");\nmatrix unitU;matrix certificate=lift(I,ideal(1),unitU,"slimgb");\n'
script+='print("ISP_BEGIN_TRUE_KE_REMULTIPLICATION");\nmatrix product=matrix(I)*certificate;\n'
script+='if (nrows(product)==1 && ncols(product)==1 && product[1,1]==1) {\n'
script+='print("ISP_KE_ORIGINAL_UNIT_IDENTITY_VERIFIED");print(nrows(certificate));int ii;for(ii=1;ii<=nrows(certificate);ii++){print("ISP_CERT_PART");print(ii);print(deg(certificate[ii,1]));print(size(certificate[ii,1]));}\n'
script+='} else {print("ISP_KE_ORIGINAL_UNIT_IDENTITY_NOT_OBTAINED");}\nquit;\n'
out("singular_Ke_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),field="QQ[e]/G9",field_irreducibility="already proved by original prime-37 Rabin identities",physical_variables=["d=w-s","z","x","s"],inverse_variable="n=1/Pi",generators=len(polys),wall_limit_seconds=900,address_space_limit_bytes=4294967296)
def child_limits():
 import resource
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix="isp-h21-finite-true-Ke-") as td:
 path=os.path.join(td,"input.sing")
 with open(path,"w") as o:o.write(script)
 try:
  run=subprocess.run([sing,"-q",path],capture_output=True,text=True,timeout=900,preexec_fn=child_limits)
  output=run.stdout+run.stderr
  stdout_lines=set(run.stdout.splitlines())
  verified=(run.returncode==0 and all(marker in stdout_lines for marker in ("ISP_KE_FIELD_RELATION_VERIFIED","ISP_KE_LIFT_SMOKE_VERIFIED","ISP_KE_ORIGINAL_UNIT_IDENTITY_VERIFIED")))
  out("singular_Ke_output",returncode=run.returncode,identity_verified=verified,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  need(verified,"no actual characteristic-zero original unit identity obtained")
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  out("true_Ke_bounded_timeout",outcome="unresolved",limit_seconds=900,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  raise RuntimeError("true Ke lift unresolved after actual bounded execution")
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="actual LOWERED original seven-polynomial physical chart has exact unit certificate over QQ[e]/G9; six universal identities connect it to the original chart",identity="matrix(original_generators)*certificate=[1]",ordinary_isp_claim=False)
