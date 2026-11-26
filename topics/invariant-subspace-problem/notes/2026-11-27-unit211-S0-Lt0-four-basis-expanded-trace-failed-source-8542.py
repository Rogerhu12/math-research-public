from pathlib import Path
src=Path('/workspace/scratch/8542378f2b73/r150-scratch/Lt_five_quadratic_rules_probe.py').read_text().split('rows=[]\ndef serbr')[0]
exec(src)
signal.alarm(180)
# The lambda*v, f*v overlap has no v^3; its v^2 coefficient is the already
# completely returned H16,13 parameter boundary.
p=subp(shiftp(RULES[3],(0,1,0,0)),shiftp(RULES[4],(1,0,0,0)))
input_trace=[addp(scalep(shiftp({(0,0,0,0):INV[3][q]},(0,1,0,0)),BR(-1)),shiftp({(0,0,0,0):INV[4][q]},(1,0,0,0))) for q in range(5)]
check=dict(p)
for q in range(5):check=subp(check,mulp(input_trace[q],S5[q]))
assert not check
out,tr=fnf(p)
assert (0,0,3,0) not in out
trace_out=[subp(input_trace[q],tr[q]) for q in range(5)]
check=dict(out)
for q in range(5):check=subp(check,mulp(trace_out[q],S5[q]))
assert not check
alpha=out[(0,0,2,0)];c0,fac=alpha.n.factor();assert len(fac)==1 and int(fac[0][1])==1;H16=fac[0][0];assert c0*H16==alpha.n
assert hashlib.sha256(str(sorted(H16.to_dict().items())).encode()).hexdigest()=='a17adccb80b9ec09219643cbee3c47a64f1ed3c27716623da8adfe559fc8b93e'
bpaid.append(H16)
rule6=scalep({m:a for m,a in out.items() if m!=(0,0,2,0)},-BR(1)/alpha)
trace6=[scalep(t,BR(1)/alpha) for t in trace_out]
L6=leadmons+[(0,0,2,0)];R6=[];T6=[];v2coeff=[]
for i in range(5):
 c=RULES[i].get((0,0,2,0),BR());v2coeff.append(c)
 new=addp({m:a for m,a in RULES[i].items() if m!=(0,0,2,0)},scalep(rule6,c));R6.append(new)
 T6.append([addp({(0,0,0,0):INV[i][q]},scalep(trace6[q],c)) for q in range(5)])
R6.append(rule6);T6.append(trace6)
for i in range(6):
 assert all(sum(m)<=1 for m in R6[i])
 chk=subp({L6[i]:BR(1)},R6[i])
 for q in range(5):chk=subp(chk,mulp(T6[i][q],S5[q]))
 assert not chk
 for a in R6[i].values():check_den(a.d)
 for trr in T6[i]:
  for a in trr.values():check_den(a.d)
# Reverse ideal identities: the original five polynomials are combinations of
# these six monic relations, so this is the same localized selected ideal.
Rel6=[subp({m:BR(1)},rhs) for m,rhs in zip(L6,R6)]
for q in range(5):
 ck=dict(S5[q])
 for i in range(5):ck=subp(ck,scalep(subp(Rel6[i],scalep(Rel6[5],v2coeff[i])),CM[q][i]))
 assert not ck
say({'stage':'six_quadratic_original_rewrites_complete','spanningMonomials':['1','lambda','f','v'],'selectedOriginalIdealEqualityVerifiedBothDirections':True,'sameParameterBase':'QQ(e,k)','newDenominators':['H64','H16'],'claimFreeBasis':False,'claimExcluded':False})
@functools.lru_cache(None)
def n6mon(m):
 ii=next((i for i,h in enumerate(L6) if all(x>=y for x,y in zip(m,h))),None)
 if ii is None:return {m:BR(1)},[{} for _ in range(5)]
 sh=tuple(x-y for x,y in zip(m,L6[ii]));o={};tr=[shiftp(t,sh) for t in T6[ii]]
 for n,a in R6[ii].items():
  rr,qt=n6mon(tuple(x+y for x,y in zip(n,sh)));o=addp(o,scalep(rr,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(qt[q],a))
 return o,tr

def n6(p):
 out={};tr=[{} for _ in range(5)]
 for m,a in p.items():
  rr,qt=n6mon(m);out=addp(out,scalep(rr,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(qt[q],a))
 ck=subp(p,out)
 for q in range(5):ck=subp(ck,mulp(tr[q],S5[q]))
 assert not ck
 assert all(sum(m)<=1 for m in out)
 for a in out.values():check_den(a.d)
 for trr in tr:
  for a in trr.values():check_den(a.d)
 return out,tr
for p in S5:assert not n6(p)[0]
returned=[]
def ser(a):return {'n':[[list(map(int,m)),str(v)] for m,v in a.n.to_dict().items()],'d':[[list(map(int,m)),str(v)] for m,v in a.d.to_dict().items()]}
def rowlog(label,out):
 den=bo
 for a in out.values():den=den*a.d/den.gcd(a.d)
 check_den(den);cf=[out.get(m,BR()).n*(den/out[m].d) if m in out else bz for m in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,0)]]
 rawcf=list(cf);paid=bo
 for at in bpaid:
  while True:
   gg=at
   for cc in cf:gg=gg.gcd(cc)
   if gg.total_degree()==0:break
   cf=[cc/gg for cc in cf];paid*=gg
 for aa,bb in zip(rawcf,cf):assert aa==paid*bb
 say({'stage':'four_basis_original_row','name':label,'degrees':[max(int(a.degrees()[i]) for a in cf if a) for i in [0,1]],'terms':sum(len(a.to_dict()) for a in cf),'sha256':hashlib.sha256('|'.join(str(sorted(a.to_dict().items())) for a in cf).encode()).hexdigest(),'originalTraceAndPaidDivisionsVerified':True,'claimExcluded':False})
 returned.append({'name':label,'coefficients':[[[list(map(int,m)),str(a)] for m,a in p.to_dict().items()] for p in cf]})
for i,j0 in itertools.combinations(range(6),2):
 lcm=tuple(max(x,y) for x,y in zip(L6[i],L6[j0]))
 if sum(lcm)>3:continue
 p=subp(shiftp(R6[i],tuple(x-y for x,y in zip(lcm,L6[i]))),shiftp(R6[j0],tuple(x-y for x,y in zip(lcm,L6[j0]))))
 origtrace=[subp(shiftp(T6[j0][q],tuple(x-y for x,y in zip(lcm,L6[j0]))),shiftp(T6[i][q],tuple(x-y for x,y in zip(lcm,L6[i])))) for q in range(5)]
 ck=dict(p)
 for q in range(5):ck=subp(ck,mulp(origtrace[q],S5[q]))
 assert not ck
 out,tr=n6(p);rowlog('cubic_overlap_'+str(i)+'_'+str(j0),out)
# Same eta in ALL remaining original N/P equations.
nd=2*j*Bnum;nn=Unum*Dnum
assert Malign==nn-nd*eta
assert Zden*nn*nn-(1-e*k)*Dnum*nd*nd==Zden*Dnum*Qa
elist=[]
for label,p in [('Nvalue',Mnormal),('NB_odd',polys[5]),('PB_odd',polys[7])]:
 p0=ctx.from_dict({tuple(map(int,m)):a for m,a in p.to_dict().items() if int(m[5])==0})
 p1=ctx.from_dict({(int(m[0]),int(m[1]),int(m[2]),int(m[3]),int(m[4]),0,0):a for m,a in p.to_dict().items() if int(m[5])==1})
 assert p==p0+p1*eta
 rr=nd*p0+nn*p1;assert rr==nd*p+p1*Malign;elist.append((label,rr))
extra=[('U_moment',Mmoment),elist[0],('NB_even',polys[4]),elist[1],('PB_even',polys[6]),elist[2]]
for label,p in extra:
 out,tr=n6(split(p));rowlog(label,out)
Path('/workspace/scratch/8542378f2b73/r150-scratch/Lt_four_basis_original_rows.json').write_text(json.dumps(returned))
say({'stage':'complete','rows':len(returned),'paidCoefficientDenominatorChecks':den_checks,'claimExcluded':False})
