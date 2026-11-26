#!/usr/bin/env python3
"""True characteristic-zero labelled-source gate for primitive reduced H3,
degenerate Gram, Hp=0, essential six. The whole remaining finite-center chart
c!=0,2 is retained, including c=-6. Individual H/V source points avoid the
large expanded quadratic trace input. All three original N first derivatives
and both original highest V first derivatives are kept.
"""
import os,time,json,hashlib,math,shutil,subprocess,tempfile
import sympy as S
from flint import fmpq_poly,fmpq,fmpz_mpoly_ctx
started=time.monotonic()
def out(stage,**kw):
 print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def need(v,msg):
 if not v:raise AssertionError(msg)
# Exact single coefficient field for e, primitive omega, and delta.
# theta=e+eta, eta a primitive twelfth root, delta=eta^3*e, omega=eta^4.
th,er=S.symbols("theta er")
fs=S.Poly(S.resultant(2*er**3+1,(th-er)**4-(th-er)**2+1,er),th,domain=S.QQ)
need(fs.degree()==12,"degree-twelve original constant field")
F=fmpq_poly([fmpq(int(fs.nth(i).p),int(fs.nth(i).q)) for i in range(13)])
F=F/F[12]
factor_content,factors=F.factor()
check=fmpq_poly([factor_content])
for ff,mul in factors:check*=fmpq_poly(ff)**int(mul)
need(check==F,"exact QQ field factorization remultiplication")
need(len(factors)==1 and factors[0][0].degree()==12 and int(factors[0][1])==1,"actual irreducible degree-twelve field")
zz=fmpq_poly([]);oo1=fmpq_poly([1]);theta=fmpq_poly([0,1])
fr=lambda p:p%F
def fm(p,q):return fr(p*q)
def fp(p,n):
 ans=oo1
 while n:
  if n&1:ans=fm(ans,p)
  n//=2
  if n:p=fm(p,p)
 return ans
field_inverse_count=0
def fi(p):
 global field_inverse_count
 p=fr(p);need(bool(p),"nonzero exact coefficient inverse")
 g,a,b=p.xgcd(F)
 need(g.degree()==0 and g[0],"irreducible-field QQ gcd is a unit")
 need(a*p+b*F==g,"full QQ field inverse Bezout remultiplication")
 inv=fr(a/g[0]);need(fm(inv,p)==oo1,"exact coefficient-field inverse product")
 field_inverse_count+=1
 return inv
def trim(v):
 v=list(v)
 while v and not v[-1]:v.pop()
 return v
def padd(v,w):
 outp=[zz for i in range(max(len(v),len(w)))]
 for i in range(len(outp)):outp[i]=fr((v[i] if i<len(v) else zz)+(w[i] if i<len(w) else zz))
 return trim(outp)
def pmul(v,w):
 if not v or not w:return []
 outp=[zz for i in range(len(v)+len(w)-1)]
 for i,a in enumerate(v):
  for j,b in enumerate(w):outp[i+j]=fr(outp[i+j]+fm(a,b))
 return trim(outp)
def pdiv(v,w):
 v=trim(v);w=trim(w);need(bool(w),"nonzero field polynomial divisor")
 rem=list(v);quo=[zz for i in range(max(0,len(v)-len(w)+1))]
 il=fi(w[-1])
 while rem and len(rem)>=len(w):
  j=len(rem)-len(w);cc=fm(rem[-1],il);quo[j]=fr(quo[j]+cc)
  for i,bb in enumerate(w):rem[i+j]=fr(rem[i+j]-fm(cc,bb))
  rem=trim(rem)
 need(padd(pmul(trim(quo),w),rem)==v,"whole coefficient-field polynomial division")
 return trim(quo),rem
ep=[fmpq_poly([fmpq(1,2)]),zz,zz,oo1]
hp=[fr(fp(theta,4)-fp(theta,2)+oo1),fr(-4*fp(theta,3)+2*theta),fr(6*fp(theta,2)-oo1),fr(-4*theta),oo1]
left,right=ep,hp
while right:
 _,rem=pdiv(left,right);left,right=right,rem
need(len(left)==2,"unique original e over the primitive field")
leadinv=fi(left[1]);EE=fr(-fm(left[0],leadinv));ETA=fr(theta-EE)
OM=fp(ETA,4);II=fp(ETA,3);DD=fm(II,EE)
need(fr(2*fp(EE,3)+oo1)==zz,"actual e relation")
need(fr(fp(ETA,4)-fp(ETA,2)+oo1)==zz,"actual primitive twelfth-root relation")
need(fr(fp(OM,2)+OM+oo1)==zz,"actual primitive third-root relation")
need(fr(fp(II,2)+oo1)==zz,"actual imaginary-unit relation")
need(fr(fp(DD,2)+fp(EE,2))==zz,"actual delta square relation")
need(EE and OM and DD,"all original Gram constants nonzero")
out("exact_original_constant_field_complete",degree=12,monic_minpoly=str(F),QQ_inverse_checks=field_inverse_count,irreducible=True,e_representation_sha256=hashlib.sha256(str(EE).encode()).hexdigest(),omega_representation_sha256=hashlib.sha256(str(OM).encode()).hexdigest(),delta_representation_sha256=hashlib.sha256(str(DD).encode()).hexdigest())
# Physical points remain individually labelled; ee,oo,dd are constant-field
# symbols only and will be declared as exact Singular numbers, not variables.
ctx=fmpz_mpoly_ctx.get(("n","c","a","b","u","v","ee","oo","dd"),"lex")
n,c,a,b,u,v,ee,om,dd=ctx.gens()
zero=ctx.from_dict({})
a3=-c*c*(c-2)*(c+6);a21=-2*c*(c*c+3*c-6);a20=-6*c*c-12*c+32
def Q(s,p):
 return a3*p**3+(a21*s+a20)*p*p+(-5*s*s-6*(c+1)*s-5)*p+(c+1)*s**3+s*s
def QX(s,p):
 return a21*p*p+(-10*s-6*(c+1))*p+3*(c+1)*s*s+2*s
def QZ(s,p):
 return 3*a3*p*p+2*(a21*s+a20)*p-5*s*s-6*(c+1)*s-5
def K(s,t):
 return -(s-t)**2*Q(s+t,s*t)
def K1(s,t):
 return -2*(s-t)*Q(s+t,s*t)-(s-t)**2*(QX(s+t,s*t)+t*QZ(s+t,s*t))
def L(s):
 return -a3*s**3-a21*s*s+5*s-c-1
def LP(s):
 return -3*a3*s*s-2*a21*s+5
def M(s):
 return 2*a3*s**4+a21*s**3-a20*s*s+5*(c+1)*s-1
def derivative(f,i):
 D={}
 for mon,value in f.to_dict().items():
  if mon[i]:
   key=list(mon);key[i]-=1;D[tuple(key)]=int(value)*mon[i]
 return ctx.from_dict(D)
Koriginal=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
changed=zero
for i in range(6):
 for j in range(6):
  if Koriginal[i][j]:changed+=Koriginal[i][j]*u**(5-i)*(c*u+1)**i*v**(5-j)*(c*v+1)**j
need(changed==K(u,v),"entire original basis-transformed K, all c")
def coefficient(fpoly,index,power):
 D={}
 for mon,value in fpoly.to_dict().items():
  if mon[index]==power:
   key=list(mon);key[index]=0;D[tuple(key)]=value
 return ctx.from_dict(D)
need(coefficient(K(u,v),5,5)==L(u),"actual central polar leading coefficient")
need(coefficient(K(u,v),5,4)==M(u),"actual adjacent central polar coefficient")
need(derivative(K(u,v),4)==K1(u,v),"actual first derivative with other V source held fixed")
need(derivative(L(u),4)==LP(u),"actual central-polar derivative")
LA,LB,LU,LV=L(a),L(b),L(u),L(v)
EV=LU*LV;k=K(u,v);f=K(a,u);g=K(a,v)
Su=LB*f+LA*K(b,u);Sv=LB*g+LA*K(b,v)
Phase=LU*g-om*om*LV*f
Delta=dd*LA*k+om*LV*f
MA=LV*f+LU*g;MB=LV*K(b,u)+LU*K(b,v)
MAp=LV*K1(a,u)+LU*K1(a,v)
MBp=LV*K1(b,u)+LU*K1(b,v)
need(derivative(MA,2)==MAp and derivative(MB,3)==MBp,"full polar derivatives before any source relation")
rA=MA-dd*LA*k;rB=MB+dd*LB*k
need(rA==Phase-Delta+(om*om+om+1)*LV*f,"original primitive phase gives signed H value")
need(LA*rB==LV*Su+LU*Sv-LB*rA,"other H sign and entire source identity")
GA=-k*LB*LP(a)+ee*ee*(dd+1)*EV*K1(a,b)+2*ee*dd*LB*MAp
GB=-k*LA*LP(b)+ee*ee*(1-dd)*EV*K1(b,a)-2*ee*dd*LA*MBp
oldGA=-k*k*LB*LA*LP(a)+ee*ee*EV*(MA+k*LA)*K1(a,b)+2*ee*LB*MA*MAp
oldGB=-k*k*LA*LB*LP(b)+ee*ee*EV*(MB+k*LB)*K1(b,a)+2*ee*LA*MB*MBp
need(oldGA-LA*k*GA==rA*(ee*ee*EV*K1(a,b)+2*ee*LB*MAp),"same original finite-H N derivative at a")
need(oldGB-LB*k*GB==rB*(ee*ee*EV*K1(b,a)+2*ee*LA*MBp),"same original finite-H N derivative at b")
DC=(dd-1)*M(a)*LB*EV+(-dd-1)*M(b)*LA*EV-2*om*M(u)*LA*LB*LV-2*om*om*M(v)*LA*LB*LU
# Original highest first derivatives at V: their Pprime coefficients vanish
# by Hcal(v)=P(v)^2/2. These lowered expressions retain all cross derivatives.
HU=2*dd*LA*LB*K1(u,v)+LV*((dd-1)*LB*K1(u,a)+(dd+1)*LA*K1(u,b))-2*LB*K(a,v)*LP(u)
HV=2*dd*LA*LB*K1(v,u)+LU*((dd-1)*LB*K1(v,a)+(dd+1)*LA*K1(v,b))-2*LB*K(a,u)*LP(v)
# Exact unexpanded derivative lowering, with the required original cross k.
# C'(alpha)=0 gives Hcal'(alpha)=sigma^2*k*K1(alpha,beta).
DerU=(dd-1)*LB*K1(u,a)+(dd+1)*LA*K1(u,b)
DerV=(dd-1)*LB*K1(v,a)+(dd+1)*LA*K1(v,b)
DirectU=-k*k*LA*LA*LB*LP(u)+ee*LU*LV*LV*f*DerU-om*om*k*LA*LA*LB*LU*K1(u,v)
DirectV=-k*k*LA*LA*LB*LP(v)+ee*LV*LU*LU*g*DerV-om*k*LA*LA*LB*LV*K1(v,u)
NormA=2*ee*EV*f*g-k*k*LA*LA
need(DirectU-ee*EV*f*HU==NormA*LB*LP(u)-LA*LB*LU*(om*om*k*LA+2*ee*dd*LV*f)*K1(u,v),"entire highest-first lowering at alpha, original cross k retained")
need(DirectV-ee*EV*g*HV==NormA*LB*LP(v)-LA*LB*LV*(om*k*LA+2*ee*dd*LU*g)*K1(v,u),"entire highest-first lowering at beta, original cross k retained")
Pi=c*(c-2)*(a-b)*LA*LB*LU*LV*k
raw=[("original_H_zero_edge",Q(a+b,a*b)),("original_cross_sum_u",Su),("original_cross_sum_v",Sv),("original_primitive_phase",Phase),("original_delta_pairing",Delta),("original_N_endpoint_a",GA),("original_N_endpoint_b",GB),("original_N_central",DC),("original_highest_first_u",HU),("original_highest_first_v",HV),("only_original_physical_units",n*Pi-1)]
polys=[]
for label,fpoly in raw:
 need(bool(fpoly),"nonzero displayed original generator")
 content=0
 for value in fpoly.to_dict().values():content=math.gcd(content,abs(int(value)))
 if content>1:
  fp0=ctx.from_dict({mon:int(value)//content for mon,value in fpoly.to_dict().items()})
  need(fp0*content==fpoly,"only nonzero rational scalar content removed");fpoly=fp0
 polys.append((label,fpoly))
 out("labelled_original_equation",label=label,degrees=list(map(int,fpoly.degrees())),terms=len(fpoly.to_dict()),integer_content_removed=content,sha256=hashlib.sha256(str(fpoly).encode()).hexdigest())
out("labelled_original_identities_complete",field="QQ(e,zeta12)",physical_variables=["c","a","b","alpha","beta"],physical_unit="c(c-2)(a-b)LA*LB*LU*LV*kV",finite_exceptions_removed=[0,2],center_minus_six_retained=True,extra_open_factors=[])
def number_expression(poly):
 terms=[]
 for i in range(poly.degree()+1):
  if poly[i]:
   term="("+str(poly[i])+")"
   if i:term+="*theta"+("^"+str(i) if i>1 else "")
   terms.append(term)
 return "+".join(terms) if terms else "0"
sing=shutil.which("Singular");need(sing is not None,"dedicated Singular dependency")
ver=subprocess.run([sing,"--version"],capture_output=True,text=True,timeout=15)
out("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script="ring isp=(0,theta),(n,v,u,b,a,c),dp;\nminpoly="+number_expression(F)+";\noption(redSB);\n"
script+="number ee="+number_expression(EE)+";\nnumber oo="+number_expression(OM)+";\nnumber dd="+number_expression(DD)+";\n"
script+='number echeck=2*ee^3+1;number ocheck=oo^2+oo+1;number dcheck=dd^2+ee^2;\nif(echeck!=0 || ocheck!=0 || dcheck!=0){print("ISP_L12_FIELD_FAILED");quit;}\nprint("ISP_L12_FIELD_VERIFIED");\n'
script+='ideal smoke=c,c-1;matrix smokeU;matrix smokeC=lift(smoke,ideal(1),smokeU,"slimgb");matrix smokeP=matrix(smoke)*smokeC;\n'
script+='if(nrows(smokeP)!=1 || ncols(smokeP)!=1 || smokeP[1,1]!=1){print("ISP_L12_SMOKE_FAILED");quit;}\nprint("ISP_L12_SMOKE_VERIFIED");\n'
script+="ideal I="+",\n".join(str(fpoly) for label,fpoly in polys)+";\n"
script+='if(size(I)!=11){print("ISP_L12_INPUT_SIZE_FAILED");quit;}\nprint("ISP_BEGIN_LABELLED_ORIGINAL_L12_LIFT");\nmatrix unitU;matrix certificate=lift(I,ideal(1),unitU,"slimgb");\n'
script+='print("ISP_BEGIN_LABELLED_ORIGINAL_REMULTIPLICATION");\nmatrix product=matrix(I)*certificate;\n'
script+='if(nrows(product)==1 && ncols(product)==1 && product[1,1]==1){print("ISP_LABELLED_ORIGINAL_L12_UNIT_VERIFIED");print(nrows(certificate));int ii;for(ii=1;ii<=nrows(certificate);ii++){print("ISP_CERT_PART");print(ii);print(deg(certificate[ii,1]));print(size(certificate[ii,1]));}}else{print("ISP_LABELLED_ORIGINAL_L12_UNIT_NOT_OBTAINED");}\nquit;\n'
out("singular_L12_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),generators=len(polys),field="actual irreducible QQ[theta]/f12",wall_limit_seconds=900,address_space_limit_bytes=4294967296)
def child_limits():
 import resource
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix="isp-H3-labelled-original-L12-") as td:
 path=os.path.join(td,"input.sing")
 with open(path,"w") as file:file.write(script)
 try:
  run=subprocess.run([sing,"-q",path],capture_output=True,text=True,timeout=900,preexec_fn=child_limits)
  output=run.stdout+run.stderr;lines=set(run.stdout.splitlines())
  markers=("ISP_L12_FIELD_VERIFIED","ISP_L12_SMOKE_VERIFIED","ISP_LABELLED_ORIGINAL_L12_UNIT_VERIFIED")
  verified=run.returncode==0 and all(s in lines for s in markers) and not any(s.lstrip().startswith("?") for s in output.splitlines())
  out("singular_L12_output",returncode=run.returncode,identity_verified=verified,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  need(verified,"actual labelled original characteristic-zero unit identity not obtained")
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  out("labelled_L12_bounded_timeout",outcome="unresolved",limit_seconds=900,text=output[:30000],stdout_sha256=hashlib.sha256(output.encode()).hexdigest())
  raise RuntimeError("labelled original L12 lift unresolved after actual bounded execution")
out("complete",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),scope="all remaining finite central sources c!=0,2, including c=-6, have an actual original N/highest necessary-system unit identity",identity="matrix(original_generators)*certificate=[1] over actual irreducible QQ[theta]/f12",ordinary_isp_claim=False)
