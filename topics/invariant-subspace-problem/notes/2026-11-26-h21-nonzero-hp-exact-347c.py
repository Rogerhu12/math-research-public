#!/usr/bin/env python3
"""NEW exact-QQ gate for H of type 2+1, Hp!=0, rankV2 reduced, essT3=6.
Necessary original-row equations only; complete exclusion is claimed only
after all exact resultant, exceptional-factor and QQ-unit assertions pass.
No modular empty-locus inference is used.
"""
import hashlib,json,time
from flint import fmpq,fmpq_poly,fmpz_mpoly_ctx
started=time.monotonic()
def need(v,label):
 if not v:raise AssertionError(label)
def out(stage,**kw):print(json.dumps(dict(stage=stage,seconds=time.monotonic()-started,**kw),sort_keys=True),flush=True)
def sha(f):return hashlib.sha256(str(f).encode()).hexdigest()
ctx=fmpz_mpoly_ctx.get(("chi","sigma","t"))
X,S,T=ctx.gens()
d=X*(X+2);k=5-2*X;n=-4*X**2+14*X-1
J=9-d*k*S
na=n-3*d*S;nb=2*(X-1)**2*(4-X)
Bt=(2*X+1)*J+3*na
At=Bt*S+8*nb-12*J
Ct=4*(1-X)*J*S-2*k*J-6*na
Lt=-3*na*S-4*nb
C=-2*X**2+10*X+1;E=-X**2+3*X+1
Phi=d*S**3-9*S+2*k
Ht=d*T**3-C*T+2*E
G1=3*J*Bt*T**2+3*J*Ct*T+At*Lt
G2=3*(6-d*S**2)*(Bt*T+Ct)**2+At**2*(3*d*T**2-2*C)
out("original_row_inputs",Phi_degrees=list(map(int,Phi.degrees())),Ht_degrees=list(map(int,Ht.degrees())),G1_degrees=list(map(int,G1.degrees())),G2_degrees=list(map(int,G2.degrees())))
RT1=Ht.resultant(G1,2)
RT2=Ht.resultant(G2,2)
need(int(RT1.degrees()[2])==0 and int(RT2.degrees()[2])==0,"first resultant variable eliminated")
out("first_resultants",RT1_degrees=list(map(int,RT1.degrees())),RT2_degrees=list(map(int,RT2.degrees())))
N1=Phi.resultant(RT1,1)
N2=Phi.resultant(RT2,1)
def univ(f):
 need(int(f.degrees()[1])<=0 and int(f.degrees()[2])<=0,"pure chi polynomial")
 a=[fmpq(0)]*(int(f.degrees()[0])+1)
 for mon,c in f.to_dict().items():a[mon[0]]+=fmpq(int(c))
 return fmpq_poly(a)
U1,U2=univ(N1),univ(N2)
need(U1 and U2,"both original nested resultants nonzero")
common=U1.gcd(U2)
Y=fmpq_poly([0,1])
Q2=4*Y**2-4*Y-27
Q4=8*Y**4-24*Y**3-30*Y**2+100*Y-27
allowed=Y*(Y-1)*(Y+2)*(Y-4)*Q2*Q4
r=common;removed=[]
while r.degree()>0:
 g=r.gcd(allowed)
 need(g.degree()>0,"no unhandled characteristic-zero chi factor")
 q,rem=divmod(r,g);need(not rem,"exact characteristic-zero factor removal")
 removed.append(int(g.degree()));r=q
need(r.degree()==0 and r[0]!=0,"entire generic chi spectrum covered")
out("generic_QQ_coverage",nested_degrees=[int(U1.degree()),int(U2.degree())],common_degree=int(common.degree()),removed_degrees=removed,common_sha256=sha(common))
# The two exceptional spectra are handled without discarding any good
# sigma fiber at a bad chi. All J-zero factors are already excluded by
# the proved original-node pairing lemma.
def mod_chi_zero(f,q,label):
 groups={}
 for (a,b,c),v in f.to_dict().items():
  groups[(b,c)]=groups.get((b,c),fmpq_poly([]))+fmpq_poly([0]*a+[int(v)])
 need(all(not (v%q) for v in groups.values()),label)
P2=3*S+2*k
P4=9*S**2+6*k*S-2*k**2
mod_chi_zero(27*Phi-d*(3*S-k)**2*P2,Q2,"Q2 entire sigma factorization")
mod_chi_zero(27*Phi-d*(3*S-2*k)*P4,Q4,"Q4 entire sigma factorization")
mod_chi_zero(27-d*k**2,Q2,"Q2 removed sigma factor has J=0")
mod_chi_zero(27-2*d*k**2,Q4,"Q4 removed sigma factor has J=0")
# Good sigma fibers retain the ORIGINAL first row equation G1 and Ht.
NQ2=univ(P2.resultant(RT1,1))
NQ4=univ(P4.resultant(RT1,1))
units=[]
def invmod(a,q,label):
 a=a%q;g,u,v=a.xgcd(q)
 need(g.degree()==0 and g[0]!=0,label+" QQ unit")
 iv=(u/g[0])%q
 need((a*iv)%q==fmpq_poly([1]),label+" QQ inverse remultiplication")
 units.append(dict(label=label,modulus_degree=int(q.degree()),value_degree=int(a.degree()),inverse_degree=int(iv.degree()),value_sha256=sha(a),inverse_sha256=sha(iv)))
 return iv
for tag,q,ob in (("Q2",Q2,NQ2),("Q4",Q4,NQ4)):
 need(q.gcd(q.derivative()).degree()==0,tag+" squarefree")
 invmod(Y*(Y+2)*(Y-1)*(Y-4),q,tag+" prior nonzero factors")
 invmod(5-2*Y,q,tag+" nonzero k")
 invmod(ob,q,tag+" original G1 and Ht obstruction on every good sigma")
out("complete",scope="H type 2+1, Hp nonzero, rankV2 reduced, essential dimension six: excluded",source_sha256=hashlib.sha256(open(__file__,"rb").read()).hexdigest(),nested_resultant_degrees=[int(U1.degree()),int(U2.degree())],common_degree=int(common.degree()),exceptional_obstruction_degrees=[int(NQ2.degree()),int(NQ4.degree())],QQ_units=units)
