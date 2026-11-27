from pathlib import Path
import json,hashlib,signal,itertools
root=Path('/workspace/scratch/8542378f2b73/r150-scratch');source=Path('/workspace/scratch/8542378f2b73/math-research-public/topics/invariant-subspace-problem/notes/2026-11-27-unit211-S0-Lt0-five-quadrics-parameter-curve-original-return-8542.py')
code=source.read_text().split('# Full original base-column identities')[0].replace('signal.alarm(150)','signal.alarm(180)');exec(compile(code,str(source),'exec'))
base=[('E1',E1.a),('EB_even',EB.a),('EB_odd',EB.b),('N1elim',NH.a)]
bctx=fmpq_mpoly_ctx.get(('l','u','Q','lam'),'lex');bl,bu,bQ,bla=bctx.gens();bo=bctx.constant(1);bz=bctx.constant(0)
mons=sorted([(i,j) for i in range(4) for j in range(4-i)],key=lambda m:(sum(m),m),reverse=True);assert len(mons)==10 and mons[-1]==(0,0)
rows=[];rowlabels=[]
for label,po in base:
 assert all(int(m[6])==int(m[7])==0 for m in po.n.to_dict())
 # Only clear paid original denominators, and remove common paid coefficients.
 poly0=po.n;original=poly0;paid=oo;hist=[]
 for nm,at in [('Q',Qp),('1-Q',1-Qp),('bc',2*lp*up-up*up-lp*lp*Qp),('u',up),('u-1',up-1)]:
  ct=0
  while poly0:
   gg=poly0.gcd(at)
   if gg.total_degree()==0:break
   red=poly0/gg;assert red*gg==poly0;poly0=red;paid*=gg;ct+=1
  if ct:hist.append([nm,ct])
 assert poly0*paid==original
 for nm,at in [('f',fp),('t',tp),('1',oo)]:
  pp=poly0*at;rr=[bctx.from_dict({tuple(map(int,m[:4])):aa for m,aa in pp.to_dict().items() if (int(m[4]),int(m[5]))==mon}) for mon in mons]
  recon=zz
  for mon,cf in zip(mons,rr):
   for mm,aa in cf.to_dict().items():recon+=aa*lp**int(mm[0])*up**int(mm[1])*Qp**int(mm[2])*Lp**int(mm[3])*fp**mon[0]*tp**mon[1]
  assert recon==pp;rows.append(rr);rowlabels.append(label+'*'+nm)
 say({'stage':'original_generic_quadratic_input','name':label,'degrees':list(map(int,poly0.degrees())),'terms':len(poly0.to_dict()),'paidRemoved':hist,'claimExcluded':False})
inds=list(range(9))+[11];M=[rows[i] for i in inds];say({'stage':'new_generic_two_variable_M10_begin','rowIndices':inds,'rowNames':[rowlabels[i] for i in inds],'monomials':mons,'originalRowsMultipliedBack':True,'claimExcluded':False})
AA=[list(row) for row in M];prev=bo;steps=[]
for z in range(9):
 swap=z
 if not AA[z][z]:
  swap=next(i for i in range(z+1,10) if AA[i][z]);AA[z],AA[swap]=AA[swap],AA[z]
 pivot=AA[z][z];assert pivot;lower=[AA[i][z] for i in range(z+1,10)];steps.append((pivot,lower,swap))
 for i in range(z+1,10):
  for j in range(z+1,10):
   num=AA[i][j]*pivot-AA[i][z]*AA[z][j];rr=num/prev;assert rr*prev==num;AA[i][j]=rr
  AA[i][z]=bz
 prev=pivot;say({'stage':'new_generic_M10_fraction_free_step','index':z,'swap':swap,'degrees':list(map(int,pivot.degrees())),'terms':len(pivot.to_dict()),'claimExcluded':False})
DD=AA[-1][-1];assert DD
cofactor=[bz]*10;cofactor[-1]=steps[-1][0]
for z in range(8,-1,-1):
 pivot,lower,swap=steps[z];num=-sum((cofactor[i]*lower[i-z-1] for i in range(z+1,10)),bz);cofactor[z]=num/pivot;assert cofactor[z]*pivot==num
 if swap!=z:cofactor[z],cofactor[swap]=cofactor[swap],cofactor[z]
for j in range(10):assert sum((cofactor[i]*M[i][j] for i in range(10)),bz)==(DD if j==9 else bz)
say({'stage':'new_generic_M10_original_constant_column_return','degrees':list(map(int,DD.degrees())),'terms':len(DD.to_dict()),'allTenCofactorIdentitiesVerified':True,'claimExcluded':False})
scalar,fac=DD.factor();prod=bctx.constant(scalar);ff=[]
for pp,n in fac:
 prod*=pp**n;ff.append({'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'multiplicity':int(n),'sha256':hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest(),'poly':[[list(map(int,m)),str(a)] for m,a in pp.to_dict().items()]})
assert prod==DD;say({'stage':'new_generic_M10_full_factorization','factors':[{k:v for k,v in x.items() if k!='poly'} for x in ff],'claimExcluded':False})
(root/'generic_four_quad_M10_factors.json').write_text(json.dumps(ff));signal.alarm(0)
