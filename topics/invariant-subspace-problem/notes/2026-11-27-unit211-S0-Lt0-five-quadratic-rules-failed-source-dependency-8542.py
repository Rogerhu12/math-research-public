from pathlib import Path
import json,time,hashlib,resource,signal,itertools,functools
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
source=Path('/workspace/scratch/8542378f2b73/math-research-public/topics/invariant-subspace-problem/notes/2026-11-27-unit211-S0-Lt0-equal-singleton-weights-original-return-8542.py')
exec(source.read_text().split('# SAME eta alignment/norm:')[0])
Qa=Unum*Unum*Dnum-2*(1-e*k)*Bnum*Bnum
S5=[split(g) for g in [*polys[:4],Qa]]
leadmons=[(2,0,0,0),(1,1,0,0),(0,2,0,0),(1,0,1,0),(0,1,1,0)]
CM=[[p.get(m,BR()) for m in leadmons] for p in S5]
AB=[list(row)+[BR(1 if i==q else 0) for q in range(5)] for i,row in enumerate(CM)]
for z in range(5):
 if not AB[z][z]:
  j0=next(i for i in range(z+1,5) if AB[i][z]);AB[z],AB[j0]=AB[j0],AB[z]
 at=AB[z][z];AB[z]=[a/at for a in AB[z]]
 for i in range(5):
  if i==z:continue
  at=AB[i][z]
  if at:AB[i]=[a-at*b for a,b in zip(AB[i],AB[z])]
INV=[row[5:] for row in AB]
for i in range(5):
 for q in range(5):assert sum((INV[i][j0]*CM[j0][q] for j0 in range(5)),BR())==BR(1 if i==q else 0)
rawH=Path('/workspace/scratch/8542378f2b73/r150-scratch/Lt_five_quadrics_quadratic_heads.json')
H64=bctx.from_dict({tuple(m):fmpq(a) for m,a in json.loads(rawH.read_text())['minors'][0]})
bpaid=[bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in at.to_dict().items()}) for at in [e,k,j,x,Dq,D3,e+1,e-1,4*e-k-4,4*e-k]]+[H64]
den_checks=0
def check_den(d):
 global den_checks
 p=d
 for a in bpaid:
  while p.total_degree()>0:
   gg=p.gcd(a)
   if gg.total_degree()==0:break
   rr=p/gg;assert rr*gg==p;p=rr
 assert p and p.total_degree()==0;den_checks+=1
for row in INV:
 for a in row:check_den(a.d)
rest=[{m:a for m,a in p.items() if m not in leadmons} for p in S5]
RULES=[]
for i in range(5):
 r={}
 for q in range(5):r=addp(r,scalep(rest[q],-INV[i][q]))
 assert all(sum(m[:3])<=1 or m==(0,0,2,0) for m in r)
 check=subp({leadmons[i]:BR(1)},r)
 for q in range(5):check=subp(check,scalep(S5[q],INV[i][q]))
 assert not check
 for a in r.values():check_den(a.d)
 RULES.append(r)
 say({'stage':'five_original_quadratic_rules','head':leadmons[i],'rightMonomials':[list(m) for m in r],'coefficientNumeratorDegrees':[list(map(int,a.n.degrees())) for a in r.values()],'rawOriginalCombinationVerified':True,'claimExcluded':False})
@functools.lru_cache(None)
def fnfmon(m):
 possible=next((i for i,h in enumerate(leadmons) if all(x>=y for x,y in zip(m,h))),None)
 if possible is None:return {m:BR(1)},[{} for _ in range(5)]
 ii=possible;shift=tuple(x-y for x,y in zip(m,leadmons[ii]));out={};tr=[{shift:INV[ii][q]} for q in range(5)]
 for n,a in RULES[ii].items():
  rest,qt=fnfmon(tuple(x+y for x,y in zip(n,shift)))
  out=addp(out,scalep(rest,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(qt[q],a))
 return out,tr

def fnf(p):
 out={};tr=[{} for _ in range(5)]
 for m,a in p.items():
  rr,tt=fnfmon(m);out=addp(out,scalep(rr,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(tt[q],a))
 check=subp(p,out)
 for q in range(5):check=subp(check,mulp(tr[q],S5[q]))
 assert not check
 for a in out.values():check_den(a.d)
 for t in tr:
  for a in t.values():check_den(a.d)
 return out,tr
rows=[]
def serbr(a):return {'n':[[list(map(int,m)),str(vv)] for m,vv in a.n.to_dict().items()],'d':[[list(map(int,m)),str(vv)] for m,vv in a.d.to_dict().items()]}
for i,j0 in itertools.combinations(range(5),2):
 h1,h2=leadmons[i],leadmons[j0];lm=tuple(max(x,y) for x,y in zip(h1,h2))
 if sum(lm)>3:continue
 p=subp(shiftp(RULES[i],tuple(x-y for x,y in zip(lm,h1))),shiftp(RULES[j0],tuple(x-y for x,y in zip(lm,h2))))
 out,tr=fnf(p)
 assert all(m[0]+m[1]+m[3]<=1 and (m[0]+m[1]==0 or m[2]==0) for m in out)
 a=out.get((0,0,3,0),BR());lead=a.n;paid=bo
 for at in bpaid:
  while lead:
   gg=lead.gcd(at)
   if gg.total_degree()==0:break
   rr=lead/gg;assert rr*gg==lead;lead=rr;paid*=gg
 if lead:
  cf,fs=lead.factor();fact=[{'degrees':list(map(int,f.degrees())),'terms':len(f.to_dict()),'mult':int(n),'poly':str(f) if len(f.to_dict())<20 else None} for f,n in fs]
 else:fact=[]
 say({'stage':'original_cubic_overlap','heads':[i,j0],'rightMonomials':[list(m) for m in out],'v3LeadNumeratorDegrees':list(map(int,lead.degrees())) if lead else None,'v3LeadTerms':len(lead.to_dict()),'v3LeadFactors':fact,'allOriginalTracesVerified':True,'claimExcluded':False})
 rows.append({'heads':[i,j0],'out':[[list(m),serbr(a)] for m,a in out.items()]})
Path('/workspace/scratch/8542378f2b73/r150-scratch/Lt_five_quadratic_rules_data.json').write_text(json.dumps({'overlaps':rows}))
say({'stage':'complete','paidCoefficientDenominatorChecks':den_checks,'claimExcluded':False})
