from pathlib import Path
import itertools,json,hashlib,signal
root=Path('/workspace/scratch/8542378f2b73/r150-scratch');source=Path('/workspace/scratch/8542378f2b73/math-research-public/topics/invariant-subspace-problem/notes/2026-11-27-unit211-S0-Lt0-five-quadrics-parameter-curve-original-return-8542.py')
code=source.read_text().split('# Full original base-column identities')[0].replace('signal.alarm(150)','signal.alarm(120)');exec(compile(code,str(source),'exec'))
mons=[(2,0),(1,1),(0,2),(1,0),(0,1),(0,0)]
base=[E1.a,EB.a,EB.b,NH.a]
def co(po,mon):return R(ctx.from_dict({m:aa for m,aa in po.n.to_dict().items() if (int(m[4]),int(m[5]))==mon})/(fp**mon[0]*tp**mon[1]),po.d)
def wedge(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def ad(a,b):return [x+y for x,y in zip(a,b)]
def sm(a,b):return [a*x for x in b]
allout=[]
for inds in [(0,1,2),(0,1,3)]:
 qs=[base[i] for i in inds];cs=[[co(q0,m) for q0 in qs] for m in mons];AA,BB,CC,DD,EE,FF=cs
 assert all(qs[j]==sum((cs[i][j]*f**m[0]*t**m[1] for i,m in enumerate(mons)),R()) for j in range(3))
 alpha=ad(ad(sm(f,AA),sm(t,BB)),DD);beta=ad(sm(t,CC),EE)
 # Every determinant below expands along its first row into the three original quadratics.
 derived=[wedge(qs,AA,beta)+wedge(qs,alpha,BB),wedge(qs,alpha,CC),wedge(qs,alpha,beta)]
 out=[]
 for i,rr in enumerate(qs+derived):
  assert all(int(m[4])+int(m[5])<=2 for m in rr.n.to_dict())
  assert all(int(m[4])==int(m[5])==int(m[6])==int(m[7])==0 for m in rr.d.to_dict())
  original=rr.n;pp=original;paid=oo;rem=[]
  for nm,atom in [('Q',Qp),('1-Q',1-Qp),('bc',2*lp*up-up*up-lp*lp*Qp),('u',up),('u-1',up-1)]:
   cc=0
   while pp:
    gg=pp.gcd(atom)
    if gg.total_degree()==0:break
    pp=pp/gg;paid*=gg;cc+=1
   if cc:rem.append([nm,cc])
  assert pp*paid==original
  out.append({'poly':[[list(map(int,m)),str(a)] for m,a in pp.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()],'paid':[[list(map(int,m)),str(a)] for m,a in paid.to_dict().items()]})
  say({'stage':'generic_Dixon_quadratic_original_combination','originalRows':list(inds),'row':i,'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'paidRemoved':rem,'degreeAtMostTwoVerified':True,'claimExcluded':False})
 allout.append({'indices':list(inds),'rows':out})
(root/'generic_three_quad_Dixon_rows.json').write_text(json.dumps(allout));signal.alarm(0)
