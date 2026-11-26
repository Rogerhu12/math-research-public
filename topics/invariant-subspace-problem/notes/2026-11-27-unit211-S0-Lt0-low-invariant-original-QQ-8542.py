#!/usr/bin/env python3
"""R150 S0/Lt0: low invariant original input, paid units, actual QQ lift.
Every polynomial comes from the original Frobenius Gram or an exact paid
coordinate transformation. Build-only is not an exclusion claim.
Singular unit claims require matrix(original necessary generators)*cert == [1].
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
start=time.perf_counter()
def say(x):x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('l','u','Q','lam','f','t'),'lex');lp,up,Qp,Lp,fp,tp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
l,u,Q,lam,f,t=map(R,ctx.gens());Delta=1-Q
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
W1=E(T0/2+2*u*f);W2=E(u*T0+lam*P02+(V2+2*u*u)*f-bc*Q*t)
X=ivbp*(q*W1-W2);Y=ivcq*(W2-p*W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b


# Full original base-column identities, using the dual product throughout.
v0c=va(rows[0],vs(-tau(rows[0]),one))
assert tau(vm(vm(v0c,v0c),v0c))==E(P02)
assert N4(rows[0])==E(2*lam*P02)
raw=[('E1',E1.a),('EBeven',EB.a),('EBodd',EB.b),('N1elim',NH.a)]
original_data=[]
for label,val in raw:
 den=val.d;paid=[]
 for nm,atom in [('pq',Qp),('distinct_p_q',1-Qp),('bc',2*lp*up-up*up-lp*lp*Qp)]:
  count=0
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   q0=den/gg;assert q0*gg==den;den=q0;count+=1
  if count:paid.append((nm,count))
 assert den.total_degree()==0
 original_data.append((label,val.n.to_dict()))
 say({'stage':'original_universal_necessary_polynomial','label':label,'numSha256':hashlib.sha256(str(sorted(val.n.to_dict().items())).encode()).hexdigest(),'paidDenominatorAtoms':paid,'dualProductChecked':True})
# e=u-1, k=Q/e; these symbols have no relation to the U-value named k.
ctx=fmpq_mpoly_ctx.get(('e','k','lam','f','v','eta','invUnit'),'lex')
e,k,la,fp,v,eta,invUnit=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
j=k+2-2*e;x=k+4;qq=e*k;Dq=qq-1
D3=4*e**3-3*e**2*k-4*e**2+e*k*k+4*e*k+4*e-k-4
assert 2*j*k*(e+1)-(e+1)**2*k*k-j*j*qq==-k*D3
# Thus bc=D3/(4*k*(e*k-1)), and the reversible t change is v=4*k*bc*t.
polys=[];names=[]
smallunits=[('e',e),('k',k),('distinct_p_q',Dq),('ell',j),('bc',D3),('T0',x)]
for label,terms in original_data:
 ml=max(int(m[0]) for m in terms);praw=zz
 for m,aa in terms.items():
  il,iu,iq,ia,iff,it=map(int,m)
  praw+=aa*j**il*k**(ml-il)*(e+1)**iu*qq**iq*la**ia*fp**iff*v**it
 pp=praw;removed=[];removed_product=oo
 for nm,atom in smallunits:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   rr=pp/gg;assert rr*gg==pp;pp=rr;removed_product*=gg;count+=1
  if count:removed.append((nm,count))
 assert pp*removed_product==praw
 small=zz;left=zz
 for n in range(3):
  cc=ctx.from_dict({tuple(int(m[i]) if i!=4 else 0 for i in range(7)):aa for m,aa in pp.to_dict().items() if int(m[4])==n})
  paidscale=Dq**(2-n)*D3**n;reduced=cc/paidscale
  assert reduced*paidscale==cc
  small+=reduced*v**n;left+=cc*Dq**n*D3**(2-n)*v**n
 assert left==Dq*Dq*D3*D3*small
 assert all(int(m[2])+int(m[3])+int(m[4])<=2 for m in small.to_dict())
 polys.append(small);names.append(label)
 say({'stage':'original_low_quadratic','label':label,'degrees':list(map(int,small.degrees())),'terms':len(small.to_dict()),'sha256':hashlib.sha256(str(sorted(small.to_dict().items())).encode()).hexdigest(),'removedOnlyPaidFactors':removed,'exactCoordinateMultiplicationVerified':True})
def coeff(p,na,nf,nv):
 return ctx.from_dict({(int(m[0]),int(m[1]),0,0,0,0,0):aa for m,aa in p.to_dict().items() if int(m[2])==na and int(m[3])==nf and int(m[4])==nv})
assert coeff(polys[0],0,0,2)==j/8
assert coeff(polys[3],0,0,2)==j/4
Cmat=[[coeff(p,2,0,0),coeff(p,1,1,0),coeff(p,0,2,0)] for p in polys]
a0,b0,c0=Cmat[:3]
detC=a0[0]*(b0[1]*c0[2]-b0[2]*c0[1])-a0[1]*(b0[0]*c0[2]-b0[2]*c0[0])+a0[2]*(b0[0]*c0[1]-b0[1]*c0[0])
expected=-512*e*(e+1)*(4*e-k-4)*k*k*(-j)**3*D3**3
assert detC==expected
adj=[]
for i in range(3):
 rr=[]
 for q in range(3):
  sub=[[Cmat[row][col] for col in range(3) if col!=i] for row in range(3) if row!=q]
  rr.append((-1)**(i+q)*(sub[0][0]*sub[1][1]-sub[0][1]*sub[1][0]))
 adj.append(rr)
for i in range(3):
 for q in range(3):
  assert sum((Cmat[i][ii]*adj[ii][q] for ii in range(3)),zz)==(detC if i==q else zz)
weights=[-sum((Cmat[3][i]*adj[i][q] for i in range(3)),zz) for q in range(3)]+[detC]
Lraw=sum((ww*pp for ww,pp in zip(weights,polys)),zz);Lsmall=Lraw;Lpaid=oo;Lhistory=[]
for nm,atom in smallunits:
 count=0
 while Lsmall:
  gg=Lsmall.gcd(atom)
  if gg.total_degree()==0:break
  rr=Lsmall/gg;assert rr*gg==Lsmall;Lsmall=rr;Lpaid*=gg;count+=1
 if count:Lhistory.append((nm,count))
assert Lsmall*Lpaid==sum((ww*pp for ww,pp in zip(weights,polys)),zz)
assert all(int(m[2])+int(m[3])<=1 for m in Lsmall.to_dict())
say({'stage':'entire_original_matrix_multiplication_verified','matrixDeterminant':'-512 e(e+1)(4e-k-4) k^2 (-j)^3 D3^3','unpaidDeterminantFactors':[],'halfWeightPaidBy':'R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-half-base-weight-exclusion.md','adjugateIdentities':9,'normalizedDerivedRowTerms':len(Lsmall.to_dict()),'normalizedDerivedRowPaidDivisions':Lhistory,'claimExcluded':False})
# Exact low equations of the SAME S0 value parameter and original N(V).
s=2*la-3;AA=2*la*la-2*la+1;CC=-4*la*la+5*la-2;RR=3-4*la
Tnum=x*x-2*j*j-2*la*j*x-4*x*fp;Tden=2*j*k
Znum=s*Tnum-2*j*k*AA;Zden=2*j*j
Dnum=s*s*Zden-4*Znum
Bnum=Tnum-j*j*s;Unum=e*k+2*e-2
Mmoment=Znum*Tnum-CC*Zden*Tden
Malign=Unum*Dnum-2*j*eta*Bnum
Mnorm=eta*eta*Zden-(1-e*k)*Dnum
Enum=2*j*j+Tnum;Wnum=(la-1)*Tden-Tnum
Lnum=j+k*(e+1);Ynum=j*Lnum*s-Tnum-j*j*eta
Mnormal=2*k*k*x*(RR*Zden-Znum)*fp-2*e*k*Enum*Znum-x*Wnum*Ynum
# Multiply every rational-coordinate identity back before using it.
lv=R(j,k);uv=R(e+1);Qv=R(e*k);Tv=R(Tnum,Tden);Zv=R(Znum,Zden);Dv=R(Dnum,Zden);wv=R(la-1)-Tv
assert lv*Zv==R(s)*Tv-R(AA)
assert Zv*Tv-R(CC)==R(Mmoment,Zden*Tden)
assert Dv==R(s*s)-4*Zv
Bval=2*Tv-lv*R(s)
assert (uv-lv)*Dv-R(eta)*Bval==R(Malign,k*Zden)
assert R(eta*eta)-(1-Qv)*Dv==R(Mnorm,Zden)
T0v=-R(e*x)
assert (2*uv-lv*Qv-2*uv*uv)==T0v
assert 4*R(e)*T0v*R(fp)==-T0v*T0v+2*lv*Qv*Qv*(lv+Tv)-2*R(la)*lv*Qv*T0v
normal_expr=2*(R(RR)-Zv)*R(fp)-4*lv*(lv+Tv)*Qv*Zv/R(x)-wv*((lv+uv)*R(s)-2*Tv-lv*R(eta))
assert normal_expr==R(Mnormal,Zden*k*k*x)
# Verify the original K-to-N(V) relation before taking any quotient.
oldctx=fmpq_mpoly_ctx.get(('L','Z','TH','F'),'lex');ll,zz0,tt0,ff0=oldctx.gens()
ss=2*ll-3;ac=2*ll*ll-2*ll+1;cc=-4*ll*ll+5*ll-2;dd=ss*cc-ac*zz0;de=ss*ss-4*zz0;bb=2*cc*zz0-dd*ss
uu=dd+tt0*bb;vv=uu-zz0*zz0;qu=1-tt0*tt0*de;ee=dd+cc*zz0;tn=-4*vv-zz0*zz0*qu;ww=(ll-1)*zz0-cc;yy=2*(dd*ss-cc*zz0)+tt0*(bb*ss-dd*de)
fn=-tn*tn+2*dd*ee*qu*qu-2*ll*dd*qu*tn
korig=zz0**3*(3-4*ll-zz0)*fn+8*dd*ee*qu*vv*vv-2*vv*tn*ww*yy
nlin=2*zz0**3*(3-4*ll-zz0)*tn*ff0+4*dd*ee*qu*vv-tn*ww*yy
assert 2*vv*nlin-korig==zz0**3*(3-4*ll-zz0)*(4*vv*tn*ff0-fn)
say({'stage':'same_parameter_original_moment_alignment_norm_P1_Nvalue_identities_verified','divisionAtoms':['e','k','j','k+4'],'originalKIdentity':True,'noNormEmbeddingMismatch':True,'claimExcluded':False})
# Every saturation atom is an original physical unit or a fully closed boundary.
Afnum=RR*k*Zden-Znum*(k-4*e)
Lnumpaid=Dnum-eta*s*Zden
paid=[('u-1',e),('Q/(u-1)',k),('u',e+1),('ell*k',j),('T0/(1-u)',x),('distinct_p_q',Dq),('bc',D3),('lambda',la),('z',Znum),('distinct_h_k',Dnum),('L',Lnumpaid),('Af',Afnum),('closed_base_a0',e-1),('closed_base_a_half',2*j-k),('closed_parameter_leading_linear',4*la-1),('closed_parameter_leading_A',AA)]
original_polys=polys+[Mmoment,Malign,Mnorm,Mnormal]
original_names=names+['original_U_moment','original_pairing_alignment','original_Q_norm','original_Nvalue']
# Lsmall is a paid normalization of an explicitly verified polynomial row
# combination of the first four original equations, so the localized ideals agree.
original_polys.append(Lsmall);original_names.append('paid_original_matrix_row')
for nm,pp in zip(original_names,original_polys):
 assert pp
 say({'stage':'final_original_necessary_generator','name':nm,'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'sha256':hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest()})
Stext='*'.join('('+str(pp)+')' for nm,pp in paid)
script='LIB "modstd.lib";\nring isp=0,(invUnit,eta,v,f,lam,k,e),dp;\noption(redSB);\n'
script+='ideal smoke=invUnit,invUnit-1;matrix smokec;ideal smokeg=liftstd(smoke,smokec,"modstd");matrix smokep=matrix(smoke)*smokec;\n'
script+='if(size(smokeg)!=1 || smokeg[1]!=1 || ncols(smokep)!=1 || smokep[1,1]!=1){print("ISP_LT0_QQ_SMOKE_FAILED");quit;}print("ISP_LT0_QQ_SMOKE_VERIFIED");\n'
script+='poly saturationProduct='+Stext+';\nideal I='+',\n'.join(str(pp) for pp in original_polys)+',invUnit*saturationProduct-1;\n'
script+='print("ISP_LT0_BEGIN_ORIGINAL_LOW_QQ_LIFT");matrix cert;ideal GB=liftstd(I,cert,"modstd");print("ISP_LT0_LIFT_RETURNED");matrix product=matrix(I)*cert;\n'
script+='if(size(GB)==1 && GB[1]==1 && nrows(product)==1 && ncols(product)==1 && product[1,1]==1){print("ISP_LT0_ORIGINAL_QQ_UNIT_VERIFIED");int q;for(q=1;q<=nrows(cert);q++){print(q);print(deg(cert[q,1]));print(size(cert[q,1]));}}else{print("ISP_LT0_NO_UNIT_IDENTITY");print(size(GB));print(dim(GB));}quit;\n'
say({'stage':'entire_low_QQ_input_built','scriptBytes':len(script.encode()),'scriptSha256':hashlib.sha256(script.encode()).hexdigest(),'saturationAtoms':[nm for nm,pp in paid],'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'ordinaryISPClaim':False,'claimExcluded':False})
if '--build-only' in sys.argv:
 say({'stage':'build_only_complete','allOriginalCoordinateAndMatrixChecksPassed':True,'claimExcluded':False});raise SystemExit(0)
singular=shutil.which('Singular');assert singular is not None,'Singular required for the new QQ certificate'
version=subprocess.run([singular,'--version'],capture_output=True,text=True,timeout=15)
say({'stage':'singular_version','returncode':version.returncode,'version':(version.stdout+version.stderr).splitlines()[0]})
limit=int(os.environ.get('ISP_ALG_SECONDS','1200'))
def limits():resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
with tempfile.TemporaryDirectory(prefix='isp-Lt0-low-original-') as td:
 path=Path(td)/'input.sing';path.write_text(script)
 try:
  rr=subprocess.run([singular,'-q',str(path)],capture_output=True,text=True,timeout=limit,preexec_fn=limits)
  output=rr.stdout+rr.stderr;lines=set(rr.stdout.splitlines());passed=rr.returncode==0 and 'ISP_LT0_QQ_SMOKE_VERIFIED' in lines and 'ISP_LT0_ORIGINAL_QQ_UNIT_VERIFIED' in lines
  say({'stage':'actual_QQ_return','returncode':rr.returncode,'actualUnitVerified':passed,'stdoutSha256':hashlib.sha256(output.encode()).hexdigest(),'stdoutBytes':len(output.encode()),'text':output[:30000],'claimExcluded':passed})
  assert passed,'new low original QQ input has not produced an actual unit certificate'
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b'')+(ex.stderr or b'')
  if isinstance(output,bytes):output=output.decode(errors='replace')
  say({'stage':'actual_QQ_timeout','seconds':limit,'stdoutSha256':hashlib.sha256(output.encode()).hexdigest(),'text':output[:30000],'claimExcluded':False});raise
say({'stage':'complete','identity':'matrix(original necessary localized generators)*certificate=[1]','scope':'remaining distinct-value S0 Lt0 L!=0 Af!=0 after all listed closed boundaries','ordinaryISPClaim':False,'claimExcluded':True})
