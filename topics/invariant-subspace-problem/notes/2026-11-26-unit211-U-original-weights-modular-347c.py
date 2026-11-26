#!/usr/bin/env python3
"""New R150 generic U chart in original weight variables.
Keep the two moment equations instead of expanding the rational b/c graph.
Generate the original nine equations plus N(V) with one paid denominator.
Finite-field output is structural only, never a characteristic-zero claim.
"""
import hashlib,json,os,resource,signal,subprocess,tempfile,time
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpz_mpoly_ctx
started=time.perf_counter()
def say(stage,**kw):
 print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-started,6),**kw),sort_keys=True),flush=True)
def alarm(signum,frame):
 say("source_timeout",claimExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(420)
names=("n","t","f","lam","Y","X","q","c","b")
ctx=fmpq_mpoly_ctx.get(names,"lex")
n,t,f,lam,Y,X,q,c,b=ctx.gens();onep=ctx.constant(1);zero=ctx.constant(0)
a=1-b-c;h=1+X;k=1+Y;w=lam-1-b*X-c*Y
u=b+c*q;V2=b+c*q*q
P02=b+c*q**3-3*u*V2+2*u**3
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
moment2=b*X*X+c*Y*Y-A
moment3=b*X**3+c*Y**3-B
D=2*b*c*q*(q-1)
W12=V2-2*u*u+4*f*u
W22=2*u*V2-4*u**3+2*lam*P02+2*f*(V2+2*u*u)-2*b*c*q*t
bxD=c*q*(q*W12-W22);cyD=b*(W22-W12)
rD=bxD-a*D-c*t*D
sD=cyD-a*q*D-b*t*D
A1D=2*f*D-2*b*bxD-2*c*cyD+2*b*c*t*D
rows=[[zero,zero,D,q*D],[zero,A1D,rD,sD],[D,rD,zero,t*D],[q*D,sD,t*D,zero]]
one=[onep,zero,onep,onep]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(p,v):return [p*x for x in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DKnum(v):return [tau(vm(row,v)) for row in rows]
dN=DKnum(one);F2N=tau(dN)
assert F2N==2*f*D
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def Pjet2(v,z):
 vc=va(v,vs(-tau(v),one));zc=va(z,vs(-tau(z),one))
 return 3*tau(vm(vm(vc,vc),zc))
def N4num(v):
 return 2*tau(vm(dN,vm(v,v)))-F2N*tau(vm(v,v))-4*tau(v)*tau(vm(dN,v))+2*F2N*tau(v)**2+tau(vm(v,DKnum(v)))
def Njet4num(v,z):return N4num(va(v,z))-N4num(v)-N4num(z)
ev=[tau(vm(rows[0],rows[0])),2*tau(vm(rows[0],rows[1])),tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
E=va(va(ev,vs(-2,DKnum(dN))),va(vs(-2,vm(dN,dN)),vs(2*F2N,dN)))
VV=[onep,w,h,k]
assert tau(VV)==lam
assert tau(vm(VV,VV))-2*lam*lam==moment2
assert tau(vm(vm(VV,VV),VV))-4*lam**3==moment3+3*moment2
assert P2(VV)==moment3+3*(1-lam)*moment2
assert not E[0]
assert P2(rows[0])==P02*D**3
assert N4num(rows[0])==2*lam*P02*D**3
NV=N4num(VV)
def ft_degree(po):
 return int(max((m[1]+m[2] for m in po.to_dict()),default=-1))
assert ft_degree(NV)<=1
original=[
 ("E1",E[1]),("EB",E[2]),("EC",E[3]),
 ("P1",Pjet2(rows[0],rows[1])-3*w*P02*D**3),
 ("PB",P2(rows[2])-h**3*P02*D**3),
 ("PC",P2(rows[3])-k**3*P02*D**3),
 ("N1",Njet4num(rows[0],rows[1])-4*lam*w*P02*D**3),
 ("NB",N4num(rows[2])-2*lam*h*h*P02*D**3),
 ("NC",N4num(rows[3])-2*lam*k*k*P02*D**3)]
assert ft_degree(original[3][1])<=1
assert [ft_degree(po) for label,po in original]==[2,2,2,1,3,3,2,3,3]
# Every stripped factor is a proven unit on the specified original chart.
L=q*X-Y;S=X+Y+3-2*lam
atoms=[b,c,q,q-1,q+1,lam,u,P02,X,Y,X-Y,L,S]
def strip(po):
 for atom in atoms:
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg
 return po
equations=[("moment2",moment2),("moment3",moment3),("NV",NV)]+original
equations=[(label,strip(po)) for label,po in equations]
# The chart excludes only already-paid base, value-collision and L/S faces.
Pi=onep
for atom in atoms:Pi*=atom
equations.append(("original_chart_units",n*Pi-1))
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
for label,po in equations:
 assert po
 say("original_weight_equation",label=label,totalDegree=int(po.total_degree()),ftDegree=ft_degree(po),terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())
say("original_weight_graph_verified",sourceSha256=source_sha,originalEquationCount=9,momentCount=2,additionalOriginalNV=True,chart="b*c*q*(q-1)*(q+1)*lambda*u*P0*X*Y*(X-Y)*L*S != 0",rationalWeightElimination=False,claimExcluded=False)
prime=1031
mctx=fmpz_mpoly_ctx.get(names)
def modp(po):
 out={}
 for mon,co in po.to_dict().items():
  ss=str(co).split("/");num=int(ss[0]);den=int(ss[1]) if len(ss)==2 else 1
  assert den%prime
  v=num*pow(den,-1,prime)%prime
  if v:out[mon]=v if v<=prime//2 else v-prime
 return mctx.from_dict(out)
mods=[modp(po) for label,po in equations]
script="ring isp=1031,("+",".join(names)+"),dp;\noption(redSB);\nideal I="+",\n".join(str(po) for po in mods)+";\n"
script+='print("ISP_BEGIN_GENERIC_WEIGHT_ORIGINAL");\nideal G=slimgb(I);\nprint("ISP_ORIGINAL_BASIS_SIZE");print(size(G));\n'
script+='if(size(G)==1 && G[1]==1){print("ISP_MODULAR_GENERIC_WEIGHT_UNIT");}else{print("ISP_MODULAR_GENERIC_WEIGHT_NONUNIT");print(dim(G));print(vdim(G));}\nquit;\n'
say("singular_input",bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),prime=prime,variables=list(names),generators=len(mods),claimExcluded=False)
def child_limits():
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix="isp-unit211-original-weights-") as td:
 path=os.path.join(td,"original.sing")
 Path(path).write_text(script)
 try:
  rr=subprocess.run(["Singular","-q",path],capture_output=True,text=True,timeout=180,preexec_fn=child_limits)
  output=rr.stdout+rr.stderr
  unit=rr.returncode==0 and "ISP_MODULAR_GENERIC_WEIGHT_UNIT" in output.splitlines()
  nonunit=rr.returncode==0 and "ISP_MODULAR_GENERIC_WEIGHT_NONUNIT" in output.splitlines()
  say("singular_output",returncode=rr.returncode,outcome="modular_unit" if unit else "modular_nonunit" if nonunit else "unresolved",text=output[:12000],stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),claimExcluded=False)
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  say("singular_timeout",limitSeconds=180,outcome="unresolved",text=output[:12000],stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),claimExcluded=False)
signal.alarm(0)
say("complete_structural_probe",sourceSha256=source_sha,scope="original generic U-weight chart, modular direction only",claimLambdaLayerEmpty=False,ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
