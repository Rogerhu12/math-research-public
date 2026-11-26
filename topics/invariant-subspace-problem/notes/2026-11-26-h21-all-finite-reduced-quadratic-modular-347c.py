#!/usr/bin/env python3
"""New reduced original 4-physical-variable modular direction probe."""
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
# Only these constant-polynomial identities are reduced modulo p: QQ was
# already specialized to its original value modulo p.
hcheck=S.Poly(d*(H0*Es*Bwd+3*c0*B0d*((s+d)**2-x*(s+d)+z))+H2-(3*H0*Es+3*c0*((s+d)**2-x*(s+d)+z))*CD,d,z,x,s)
need(all(int(c)%p==0 for c in hcheck.coeffs()),"highest single-point quadratic identity")
Norm2=c0*c0*U*U*Znd-25600*ee*(1-ee)*qpair*Qn*Es**4*d*d
Scale2=3*ee*ee*Wd**2+2*Re*delta*qpair*bs*Qn*d*d*qd**2
Single=2*ee*ee*QQ*Ls2+DD*delta*qpair*d*d*qd
Deriv=Wd*U+c0*Qn*d*d*qd*B1d*Es+c0*Qn*d*qd*U*(2*s-x)
# Pi has exactly the original paid nonzero factors, with redundant powers
# removed. No special source/fiber has been discarded without its original
# rank/Gram proof.
Pi=s*(s-2)*(s+6)*d*delta*qpair*Es*Qn*qd
eqs=[("source_Jred",Jred),("source_C3",CD),("highest_w_quadratic",H2),
     ("mean_norm_quadratic",Norm2),("original_jet_scale",Scale2),
     ("original_single_ratio",Single),("highest_source_derivative",Deriv),
     ("original_physical_units",n*Pi-1)]
gens2=(n,d,z,x,s);ctx2=fmpz_mpoly_ctx.get(tuple(map(str,gens2)))
def red(ex):
 dic={}
 for mon,c in S.Poly(ex,*gens2).terms():
  need(c.q==1,"integer original reduced coefficient")
  c=int(c)%p
  if c>p//2:c-=p
  if c:dic[mon]=c
 return ctx2.from_dict(dic)
def meta(f):
 return dict(degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),sha256=hashlib.sha256(str(f).encode()).hexdigest())
polys=[]
for label,expr in eqs:
 ff=red(expr);need(bool(ff),label+" nonzero")
 polys.append(ff);out("reduced_original_equation",label=label,**meta(ff))
sing=shutil.which("Singular");need(sing is not None,"dedicated Singular dependency")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script="ring isp=1031,(n,d,z,x,s),dp;\noption(redSB);\nideal I="+",\n".join(map(str,polys))+";\n"
script+='print("ISP_BEGIN_REDUCED_QUADRATIC");\nideal G=slimgb(I);\nprint("ISP_REDUCED_BASIS_SIZE");print(size(G));\n'
script+='if (size(G)==1 && G[1]==1) {print("ISP_MODULAR_UNIT_REDUCED");}\nelse {print("ISP_MODULAR_NONUNIT_REDUCED");print(dim(G));print(vdim(G));}\nquit;\n'
out("singular_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),physical_variables=["d=w-s","z","x","s"],auxiliary_variables=["n=1/Pi"],polynomial_count=len(polys),constant_prime=p,constant_e=ee)
with tempfile.TemporaryDirectory(prefix="isp-h21-finite-quadratic-") as td:
 path=os.path.join(td,"input.sing")
 with open(path,"w") as f:f.write(script)
 try:
  rr=subprocess.run([sing,"-q",path],capture_output=True,text=True,timeout=180)
  output=rr.stdout+rr.stderr
  outcome=("unit_reduced" if "ISP_MODULAR_UNIT_REDUCED" in output else "nonunit_reduced" if "ISP_MODULAR_NONUNIT_REDUCED" in output else "unresolved_or_error")
  out("singular_output",returncode=rr.returncode,outcome=outcome,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  out("singular_bounded_timeout",outcome="unresolved",limit_seconds=180,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
out("complete_probe",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="modular reduced original system only; no characteristic-zero exclusion")
