#!/usr/bin/env python3
"""NEW original-N Hermite input over the unchanged physical degree-nine field.
Adds the actual N second coefficient at the double H source and the already
proved N first coefficient at the isolated source. No old modular GB is rerun.
Only a characteristic-zero certificate whose original product is exactly one
can exclude this chart. Build-only mode checks new polynomial identities.
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

# Further exact lowering on the same Pi: retain Nnew to force A invertible.
# The C and G equations are now linear in d, without selecting a new chart.
gamma=12*EE*(EE**2+1)
Je=8*EE**3+6*EE+1
h0=gamma*ES*AF
h1=4*H0*VS+3*C0*EP*AF
h2=2*H0*WS+3*C0*AF
g0=3*EE**2*C0**2*QN*ES**2*AF**2
Dv=4*RE*VS-3*C0*EP*AF
need(not(Dv-(2*gamma*VS-h1)),"small cubic-reduction constant identity")
Clinear=(2*gamma**2*ES*AF*LS-h2*Dv)*DDvar+2*gamma**2*ES*AF*WS-gamma*ES*AF*h2-h1*Dv
need(not(gamma**2*ES*AF*Cnew-(h0+Dv*DDvar)*Hnew-DDvar**2*Clinear),"entire C linear lowering identity")
BB=AF*EP-2*VS
Cs=3*EP*AF-4*VS
Ld=12*EE**2*(EE**2+1)*C0**2*QN*BB**2+8*RE*(EE**2+1)*DS*QP*BS*AF**2-EE*C0**2*QN*ES*AF*h2
Glinear=Ld*DDvar-EE*C0**2*QN*ES*AF*Je*Cs
need(not(h0*Gnew-g0*Hnew-3*EE*ES*AF*DDvar*Glinear),"entire G linear lowering identity")
need(Clinear.degrees()[1]<=1 and Glinear.degrees()[1]<=1,"two genuine isolated-source linear equations")
polys=[
 ("source_Jred",JF),("linear_source_equation",Clinear),
 ("lowered_highest_w_quadratic",Hnew),("lowered_mean_norm_quadratic",Nnew),
 ("linear_original_jet_equation",Glinear),("original_single_ratio",KF),
 ("lowered_highest_source_derivative",Vnew),("original_physical_units",old["original_physical_units"])]
for label,f in polys:
 need(bool(f),label+" exact nonzero")
 out("two_linear_original_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
out("two_linear_universal_identities_complete",count=2,new_open_factors=[],unit_A_reason="retained Nnew and unchanged Pi",scope="same localized ideal: C and G now each degree <=1 in d")

# New original N second-Hermite input. All derivatives keep w,x,z fixed.
# With d=w-s, this derivative is partial_s-partial_d, not partial_s alone.
def Ds(f):return f.derivative('s')-f.derivative('d')
NS=ES**2*QN
KS=-DDvar**2*QW
KSS=Ds(KS)
WH=DDvar*ES*WD
need(not(WH-(KS*Ds(NS)-2*NS*KSS)),"actual original W numerator with physical derivative")
PG=3*EE**2*WH**2+2*RE*DS*QP*BS*NS*KS**2
need(not(PG-ES**2*DDvar**2*GF),"actual original jet equation before paid factors")
N2full=3*EE**2*(2*BS*NS*Ds(WH)-2*BS*Ds(NS)*WH-NS*Ds(BS)*WH)-(8*EE**3+1)*DS*QP*BS**2*NS*KS
N2,rr=divmod(N2full,ES**2)
need(not rr and not(N2*ES**2-N2full),"new N2 division only by original paid E squared")
# Verify the full formal Hermite coefficient identity before any field relation.
bf,bpf,nf,npf,nppf,kf,kpf,kppf,qpf=S.symbols('bf bpf nf npf nppf kf kpf kppf qpf')
rf=2*ee**3+1;wf=kf*npf-2*nf*kpf
wpf=kf*nppf-npf*kpf-2*nf*kppf
lamf=qpf/(4*ee**2*nf);qf=2*rf*nf*kf/(3*wf)
coeff2=nppf/(2*lamf*nf)-(kpf**2+kf*kppf)/(lamf*kf**2)+qf*bpf+6*qf*bf*kpf/kf+bf
pjet=3*ee**2*wf**2+2*rf*qpf*bf*nf*kf**2
n2formal=3*ee**2*(2*bf*nf*wpf-2*bf*npf*wf-nf*bpf*wf)-(8*ee**3+1)*qpf*bf**2*nf*kf
mult=(bpf+6*bf*kpf/kf)/(12*ee**2*wf*bf*nf*kf)+1/(6*ee**2*nf**2*kf**2)
need(S.cancel(lamf*coeff2-n2formal/(12*ee**2*bf*nf**2*kf)-pjet*mult)==0,"universal exact N second coefficient identity")
# Literal original kernel Taylor jets used in that coefficient.
need(S.expand(S.diff(ker(s,r),r,2).subs(r,s)+bs)==0,"original f second coefficient")
need(S.expand(S.diff(ker(s,r),s,r).subs(r,s)-bs)==0,"original j first coefficient")
need(S.expand(2*S.diff(ker(s,r),s,r,2).subs(r,s)-S.diff(bs,s))==0,"original j second coefficient")
# The isolated-source N first derivative is the already proved equation (6.1)
# of the full original finite-source reconstruction. Preserve all its factors.
NW=NS.compose(NN,DDvar,ZZvar,XXvar,SSvar+DDvar,EE)
KW=KS.derivative('d')
WHW=KS*NW.derivative('d')-2*NW*KW
CROSS=KS*Ds(KW)-KSS*KW
Nwfull=QF*WH*WHW-8*RE*NS*NW*CROSS
# Use the original Sstar(w)=0 and single ratio, never differentiate a relation
# which only holds at a solution. The differentiated identity below is instead
# a universal norm determinant identity, valid before all equations.
SSW=DDvar*ES*JF+DDvar**2*CF
need(not(L2**2-4*NS*NW-DS*SSW**2),"universal two-source norm determinant")
need(not(2*L2*L2.derivative('d')-4*NS*NW.derivative('d')-2*DS*SSW*SSW.derivative('d')),"derivative only of a universal determinant identity")
need(not(KF-(2*EE**2*QF*L2-DF*DS*QP*KS)),"original unsquared single ratio")
MID=QF*WH*(KS*L2.derivative('d')-L2*KW)-4*RE*NS*L2*CROSS
Nwlow=QF*WH*(2*EE**2*QF*L2.derivative('d')-DF*DS*QP*KW)-4*RE*DF*NS*DS*QP*CROSS
ERR=DS*SSW*(-2*QF*WH*KS*SSW.derivative('d')+2*QF*WH*SSW*KW+8*RE*NS*SSW*CROSS)
need(not(4*NS*Nwfull-2*L2*MID-ERR),"exact first lowering of original Nw coefficient")
need(not(2*EE**2*QF*MID-KS*Nwlow+KF*(QF*WH*KW+4*RE*NS*CROSS)),"exact second lowering of original Nw coefficient")
Nw=Nwlow
paid=[]
for label,fac in [('E',ES),('d',DDvar),('Qw',QW),('Qn',QN),('Delta',DS),('q',QP)]:
 count=0
 while True:
  qq,rr=divmod(Nw,fac)
  if rr:break
  need(not(qq*fac-Nw),"exact new Nw paid-factor division")
  Nw=qq;count+=1
 if count:paid.append([label,count])
for label,f in [('original_N_second_at_double_source',N2),('original_N_first_at_isolated_source',Nw)]:
 need(bool(f),label+" nonzero original input")
 out("new_original_N_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
polys=polys[:-1]+[("original_N_second_at_double_source",N2),("original_N_first_at_isolated_source",Nw),polys[-1]]
out("new_original_N_input_checked",Nw_removed_only_old_units=paid,formal_coefficient_identity=True,new_open_factors=[],ordinary_isp_claim=False)
if '--build-only' in sys.argv:
 out("build_only_complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),claim_excluded=False)
 sys.exit(0)
sing=shutil.which("Singular");need(sing is not None,"new dedicated Singular computation")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script='LIB "nfmodstd.lib";\nring isp=(0,e),(n,d,z,x,s),dp;\n'
script+='minpoly=(16*e^9-108*e^8+36*e^7-15*e^6+18*e^4-1)/16;\noption(redSB);\n'
script+='number fc=16*e^9-108*e^8+36*e^7-15*e^6+18*e^4-1;\nif(fc!=0){print("ISP_N2_FIELD_FAILED");quit;}\nprint("ISP_N2_FIELD_VERIFIED");\n'
script+='ideal smi=s,s-1;matrix smc;print("ISP_N2_BEGIN_NFMOD_SMOKE");ideal smg=liftstd(smi,smc,"nfmod");matrix smp=matrix(smi)*smc;\n'
script+='if(size(smg)!=1 || smg[1]!=1 || ncols(smp)!=1 || smp[1,1]!=1){print("ISP_N2_NFMOD_SMOKE_FAILED");quit;}\nprint("ISP_N2_NFMOD_SMOKE_VERIFIED");\n'
script+='ideal I='+',\n'.join(str(f) for label,f in polys)+';\n'
script+='print("ISP_N2_BEGIN_ORIGINAL_N_HERMITE_LIFT");\nmatrix cert;ideal G=liftstd(I,cert,"nfmod");\nprint("ISP_N2_LIFT_RETURNED");\nmatrix product=matrix(I)*cert;\n'
script+='if(size(G)==1 && G[1]==1 && nrows(product)==1 && ncols(product)==1 && product[1,1]==1){\nprint("ISP_N2_ACTUAL_CHARACTERISTIC_ZERO_UNIT_VERIFIED");int ii;for(ii=1;ii<=nrows(cert);ii++){print(ii);print(deg(cert[ii,1]));print(size(cert[ii,1]));}\n}else{print("ISP_N2_NO_UNIT_IDENTITY");}\nquit;\n'
out("new_Ke_N_Hermite_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),field="QQ[e]/G9",generators=len(polys),wall_limit_seconds=900,address_space_limit_bytes=4294967296,algorithm="liftstd nfmod with actual remultiplication",claim_excluded=False)
def limits():
 import resource
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix='isp-h21-new-N-Hermite-') as td:
 path=os.path.join(td,'input.sing')
 with open(path,'w') as o:o.write(script)
 try:
  run=subprocess.run([sing,'-q',path],capture_output=True,text=True,timeout=900,preexec_fn=limits)
  output=run.stdout+run.stderr;lines=set(run.stdout.splitlines())
  markers=['ISP_N2_FIELD_VERIFIED','ISP_N2_NFMOD_SMOKE_VERIFIED','ISP_N2_ACTUAL_CHARACTERISTIC_ZERO_UNIT_VERIFIED']
  success=run.returncode==0 and all(m in lines for m in markers)
  out('new_Ke_N_Hermite_output',returncode=run.returncode,identity_verified=success,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  need(success,'no actual original N-Hermite unit certificate obtained')
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b'')+(ex.stderr or b'')
  if isinstance(output,bytes):output=output.decode(errors='replace')
  out('new_Ke_N_Hermite_timeout',outcome='unresolved',limit_seconds=900,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest(),claim_excluded=False)
  raise RuntimeError('new original N-Hermite input unresolved in this execution')
out('complete',source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),identity='matrix(original_generators)*certificate=[1]',scope='finite H21 Hp0 physical chart only',ordinary_isp_claim=False)
