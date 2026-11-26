#!/usr/bin/env python3
"""Actual characteristic-zero original N-first gate for the remaining finite
central source c of primitive reduced H3, degenerate Gram, Hp=0, ess(T3)=6.
Uses the original changed kernel, UNSQUARED primitive phase and all three
H-source first derivatives of the original polar N. No modular GB input.
The already excluded c=0,2 fibers are localized away; c=-6 is retained.
"""
import os,time,json,hashlib,math,shutil,subprocess,tempfile
from flint import fmpz_mpoly_ctx
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
ctx=fmpz_mpoly_ctx.get(("n","c","A","b","x","z","e","h","t"),"lex")
n,c,A,b,x,z,e,h,t=ctx.gens()
HI,TI=7,8
zero=ctx.from_dict({});one=ctx.from_dict({(0,)*9:1})
def coeff(f,i,p):
 D={}
 for mon,v in f.to_dict().items():
  if mon[i]==p:
   key=list(mon);key[i]=0;D[tuple(key)]=v
 return ctx.from_dict(D)
def derivative(f,i):
 D={}
 for mon,v in f.to_dict().items():
  if mon[i]:
   key=list(mon);key[i]-=1;D[tuple(key)]=int(v)*mon[i]
 return ctx.from_dict(D)
def replace_variable(f,i,j):
 D={}
 for mon,v in f.to_dict().items():
  key=list(mon);key[j]+=key[i];key[i]=0
  key=tuple(key);D[key]=D.get(key,0)+int(v)
 return ctx.from_dict(D)
def divmonic(f,g,i):
 dg=int(g.degrees()[i]);need(coeff(g,i,dg)==one,"exact monic input")
 rem=f;quo=zero
 while rem and rem.degrees()[i]>=dg:
  dr=int(rem.degrees()[i])
  term=coeff(rem,i,dr)*ctx.gen(i)**(dr-dg)
  quo+=term;rem-=term*g
 need(f==quo*g+rem,"exact monic quotient remultiplication")
 return quo,rem
Hq=h*h-A*h+b
Vq=t*t-x*t+z
rh=lambda f:divmonic(f,Hq,HI)[1]
rv=lambda f:divmonic(f,Vq,TI)[1]
def traceH(f):
 f=rh(f);return 2*coeff(f,HI,0)+A*coeff(f,HI,1)
def conjugateH(f):
 f=rh(f);return coeff(f,HI,0)+coeff(f,HI,1)*(A-h)
def normH(f):
 f=rh(f);f0=coeff(f,HI,0);f1=coeff(f,HI,1)
 return f0*f0+A*f0*f1+b*f1*f1
def traceV(f):
 f=rv(f);return 2*coeff(f,TI,0)+x*coeff(f,TI,1)
def conjugateV(f):
 f=rv(f);return coeff(f,TI,0)+coeff(f,TI,1)*(x-t)
def normV(f):
 f=rv(f);f0=coeff(f,TI,0);f1=coeff(f,TI,1)
 return f0*f0+x*f0*f1+z*f1*f1
a3=-c*c*(c-2)*(c+6)
a21=-2*c*(c*c+3*c-6)
a20=-6*c*c-12*c+32
def Q(s,p):
 return a3*p**3+(a21*s+a20)*p*p+(-5*s*s-6*(c+1)*s-5)*p+(c+1)*s**3+s*s
def L(s):
 return -a3*s**3-a21*s*s+5*s-c-1
def M4(s):
 return 2*a3*s**4+a21*s**3-a20*s*s+5*(c+1)*s-1
def kernel(s,v):
 return -(s-v)**2*Q(s+v,s*v)
Koriginal=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
khv=kernel(h,t)
changed=zero
for i in range(6):
 for j in range(6):
  if Koriginal[i][j]:
   changed+=Koriginal[i][j]*h**(5-i)*(c*h+1)**i*t**(5-j)*(c*t+1)**j
need(khv==changed,"entire original kernel under t_old=c+1/z, with changed K")
need(coeff(khv,TI,5)==L(h),"actual central polar")
need(coeff(khv,TI,4)==M4(h),"actual adjacent central polar")
LH=rh(L(h));LV=rv(L(t));MLH=rh(M4(h));MLV=rv(M4(t))
E0=normH(LH);EV=normV(LV)
DH=A*A-4*b;DV=x*x-4*z;k=-DV*Q(x,z)
QH=Q(A,b)
# Original negative endpoint-polar sum: no nonconstant leading division.
NH=-traceH(conjugateH(LH)*khv)
Ht=t*t-A*t+b
Cubic,Rema=divmonic(NH,Ht,TI)
need(Rema==DH*QH*replace_variable(LH,HI,TI),"complete endpoint divisor identity on the original zero edge")
q=2*E0
need(coeff(Cubic,TI,3)==-q,"paid leading V-source cubic q=2E0")
need(Cubic.degrees()[TI]==3,"full original V cubic before physical localization")
Cr=rv(Cubic)
C0=coeff(Cr,TI,0);C1=coeff(Cr,TI,1)
# The symmetric V-polar MV(h) is differentiated BEFORE H reduction.
MVfull=traceV(khv*conjugateV(LV))
MV=rh(MVfull)
MVprime=rh(derivative(MVfull,HI))
NHV=rh(normV(khv))
phaseH=rh(MV*MV-EV*NHV)
normHpoly=rh(2*e*MV*MV-k*k*LH*LH)
# Strong phase uses the actual primitive ratio, not its square.
# All original cross-pair norms are retained, and are also forced nonzero
# by these equations together with E0*EV*k != 0.
phase0=coeff(phaseH,HI,0);phase1=coeff(phaseH,HI,1)
norm0=coeff(normHpoly,HI,0);norm1=coeff(normHpoly,HI,1)
# First derivative of the original N at each finite H endpoint.
Qx=a21*b*b+(-10*A-6*(c+1))*b+3*(c+1)*A*A+2*A
Qz=3*a3*b*b+2*(a21*A+a20)*b-5*A*A-6*(c+1)*A-5
Kotherprime=-DH*(Qx+(A-h)*Qz)
Lother=conjugateH(LH);Lprime=rh(derivative(L(h),HI))
G=rh(-k*k*Lother*LH*Lprime+e*e*EV*(MV+k*LH)*Kotherprime+2*e*Lother*MV*MVprime)
Gbefore=rh(-k*k*Lother*LH*Lprime+e*e*EV*(MV+k*LH)*Kotherprime-4*e**4*Lother*MV*MVprime)
need(Gbefore-G==rh(-2*e*(2*e**3+1)*Lother*MV*MVprime),"exact original cubic-field reduction of endpoint N derivatives")
G0=coeff(G,HI,0);G1=coeff(G,HI,1)
# Original t^9 coefficient of N at the central source infinity.
# Rnum is numerator of Tr_V(M4(v)/k(h,v)); no derivative after reduction.
Rnum=rh(traceV(MLV*conjugateV(khv)))
Lc=conjugateH(LH)
Dcentral=k*traceH(MV*MLH*Lc*Lc)-k*k*E0*traceH(MLH*Lc)+2*e*traceH(MV*Rnum*Lc*Lc)
# The inverse-polynomial trace formula used above is checked universally.
need(rv(khv*conjugateV(khv))==normV(khv),"full V quadratic norm identity")
need(rh(LH*Lc)==E0,"full H quadratic polar norm identity")
# Only already proved c=0,2 are removed; in particular c=-6 is retained.
U=c*(c-2)*DH*E0*EV*k
raw=[
 ("original_H_zero_edge",QH),
 ("original_V_source_constant",C0),("original_V_source_linear",C1),
 ("unsquared_primitive_phase_constant",phase0),("unsquared_primitive_phase_linear",phase1),
 ("original_e_norm_constant",norm0),("original_e_norm_linear",norm1),
 ("original_N_H_endpoint_derivative_constant",G0),("original_N_H_endpoint_derivative_linear",G1),
 ("original_N_central_derivative",Dcentral),
 ("only_original_physical_units",n*U-1)]
polys=[]
for label,f in raw:
 need(not any(mon[HI] or mon[TI] for mon in f.to_dict()),"all auxiliary source roots eliminated exactly")
 if not f:
  out("redundant_zero_original_equation",label=label)
  continue
 content=0
 for v in f.to_dict().values():content=math.gcd(content,abs(int(v)))
 if content>1:
  ff=ctx.from_dict({mon:int(v)//content for mon,v in f.to_dict().items()})
  need(ff*content==f,"only nonzero integer content cancelled")
  f=ff
 need(f.degrees()[6]<=2,"coefficient field powers at most two")
 polys.append((label,f))
 out("original_Nfirst_equation",label=label,degrees=list(map(int,f.degrees())),terms=len(f.to_dict()),integer_content_removed=content,sha256=hashlib.sha256(str(f).encode()).hexdigest())
out("original_universal_identities_complete",scope="actual transformed K, monic H/V source divisors, unsquared primitive Gram phase, three original N first derivatives",field="QQ[e]/(2e^3+1)",finite_center_exceptions_removed=[0,2],center_minus_six_retained=True,physical_unit="c(c-2)*(A^2-4b)*E0*EV*kV")
sing=shutil.which("Singular");need(sing is not None,"dedicated Singular dependency")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script="ring isp=(0,e),(n,z,x,b,A,c),dp;\nminpoly=(2*e^3+1)/2;\noption(redSB);\n"
script+='number fieldcheck=2*e^3+1;\nif(fieldcheck!=0){print("ISP_KE3_FIELD_RELATION_FAILED");quit;}\nprint("ISP_KE3_FIELD_RELATION_VERIFIED");\n'
script+='ideal smoke=c,c-1;matrix smokeU;matrix smokeC=lift(smoke,ideal(1),smokeU,"slimgb");matrix smokeP=matrix(smoke)*smokeC;\n'
script+='if(nrows(smokeP)!=1 || ncols(smokeP)!=1 || smokeP[1,1]!=1){print("ISP_KE3_LIFT_SMOKE_FAILED");quit;}\nprint("ISP_KE3_LIFT_SMOKE_VERIFIED");\n'
script+="ideal I="+",\n".join(str(f) for label,f in polys)+";\n"
script+="if(size(I)!="+str(len(polys))+'){print("ISP_KE3_ORIGINAL_INPUT_SIZE_FAILED");quit;}\n'
script+='print("ISP_BEGIN_ORIGINAL_NFIRST_TRUE_KE3_LIFT");\nmatrix unitU;matrix certificate=lift(I,ideal(1),unitU,"slimgb");\n'
script+='print("ISP_BEGIN_ORIGINAL_NFIRST_REMULTIPLICATION");\nmatrix product=matrix(I)*certificate;\n'
script+='if(nrows(product)==1 && ncols(product)==1 && product[1,1]==1){\nprint("ISP_ORIGINAL_NFIRST_KE3_UNIT_IDENTITY_VERIFIED");\n'
script+='print(nrows(certificate));int ii;for(ii=1;ii<=nrows(certificate);ii++){print("ISP_CERT_PART");print(ii);print(deg(certificate[ii,1]));print(size(certificate[ii,1]));}\n'
script+='}else{print("ISP_ORIGINAL_NFIRST_KE3_UNIT_IDENTITY_NOT_OBTAINED");}\nquit;\n'
out("singular_Ke3_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),generators=len(polys),field="QQ[e]/(2e^3+1)",field_irreducibility="cubic has no rational root; equivalently reciprocal polynomial u^3+2 is Eisenstein at2",wall_limit_seconds=900,address_space_limit_bytes=4294967296)
def child_limits():
 import resource
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix="isp-H3-original-Nfirst-Ke3-") as td:
 path=os.path.join(td,"input.sing")
 with open(path,"w") as o:o.write(script)
 try:
  run=subprocess.run([sing,"-q",path],capture_output=True,text=True,timeout=900,preexec_fn=child_limits)
  output=run.stdout+run.stderr
  lines=set(run.stdout.splitlines())
  markers=("ISP_KE3_FIELD_RELATION_VERIFIED","ISP_KE3_LIFT_SMOKE_VERIFIED","ISP_ORIGINAL_NFIRST_KE3_UNIT_IDENTITY_VERIFIED")
  verified=run.returncode==0 and all(m in lines for m in markers) and not any(s.lstrip().startswith("?") for s in output.splitlines())
  out("singular_Ke3_output",returncode=run.returncode,identity_verified=verified,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  need(verified,"no actual original N-first characteristic-zero unit identity obtained")
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  out("true_Ke3_bounded_timeout",outcome="unresolved",limit_seconds=900,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  raise RuntimeError("original N-first true Ke3 lift unresolved after actual bounded execution")
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="actual original necessary equations for every remaining finite center, including c=-6, have a unit certificate over QQ[e]/(2e^3+1)",identity="matrix(original_generators)*certificate=[1]",ordinary_isp_claim=False)
