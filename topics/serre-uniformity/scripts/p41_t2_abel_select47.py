#!/usr/bin/env python3
"""Find a Frobenius-stable actual Abel chart with disjoint T2-support at47."""
import gzip,hashlib,json,random,sys
from pathlib import Path
folder=Path('/workspace/scratch/64b49fd2bdbb/math-research/topics/serre-uniformity/scripts');sys.path.insert(0,str(folder))
import p41_r2_matrix as r
from p41_group_operations47 import load_sources,make_model
from p41_cm4_divisor47 import kernel
from p41_formal47_multiply import write_checkpoint
sources,hashes=load_sources(folder/'data');M=make_model(sources);d=sources[1]
hr=Path('/tmp/p41_hecke47_checkpoint.json.gz').read_bytes();hecke=json.loads(gzip.decompress(hr));op=hecke['operators']['2']
raw=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz').read_bytes();base=json.loads(gzip.decompress(raw))
P=47
def key(row):
 vals=[(a%P,b%P) for a,b in row];a,b=next((a,b) for a,b in vals if a or b);inv=pow((a*a+b*b)%P,-1,P);u=a*inv%P;v=-b*inv%P
 return tuple(((x*u-y*v)%P,(x*v+y*u)%P) for x,y in vals)
W=r.to_json(M['W']);keys=[key(w) for w in W];assert len(set(keys))==820
perm=[j-1 for j in op['necklace_transport_1based']]
tkeys=[[key(target['evaluation_matrix'][perm[j]]) for j in range(820)] for target in op['targets']]
lookup={v:j for j,v in enumerate(keys)};matches=[[lookup.get(v,-1) for v in ts] for ts in tkeys]
print('T2 target overlap with original fibre',[[i,sum(j>=0 for j in p),len(set(p)-{-1})] for i,p in enumerate(matches)],flush=True)
foot=[{keys[j],*(t[j] for t in tkeys)} for j in range(820)]
tau=[j-1 for j in sources[0]['frobenius_permutation_1based']];assert all(tau[tau[j]]==j for j in range(820))
prior=[]
for fi,f in enumerate(base['families']):
 pts=[j-1 for j in f['points_1based']];u=set().union(*(foot[j] for j in pts));prior.append({'family_index':fi,'expected_total_length':216,'distinct_supports_mod47':len(u)});print('existing family',prior[-1],flush=True)
K=r.from_json(kernel(73,d['cusp_rank_columns_1based'],d['cusp_free_columns_1based'],d['canonical_kernel_block']));Omega=r.mm(M['W'],K)
orbits=[[j,tau[j]] for j in range(820) if j<tau[j]]
rng=random.Random(4104717001);rng.shuffle(orbits);selected=[];used=set()
for orb in orbits:
 f=set().union(*(foot[j] for j in orb))
 if len(f)!=4*len(orb) or f&used:continue
 pts=selected+orb;rank=len(r.rank_pivots(r.rows(Omega,pts))[0])
 if rank!=len(pts):continue
 selected=pts;used|=f
 if len(selected)==54:break
assert len(selected)==54 and len(used)==216,(len(selected),len(used))
assert {tau[j] for j in selected}==set(selected)
O=r.rows(Omega,selected);Oi=r.inverse_matrix(O);assert r.equal(r.mm(O,Oi),r.eye(54))
out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'raw_hecke_sha256':hashlib.sha256(hr).hexdigest(),'original_abel_bases_sha256':hashlib.sha256(raw).hexdigest(),'original_family_support_counts':prior,'points_1based':[j+1 for j in selected],'all_216_supports_distinct_mod47':True,'source_frobenius_permutation_1based':[selected.index(tau[j])+1 for j in selected],'target_to_source_index_1based':[[j+1 if j>=0 else 0 for j in p] for p in matches],'canonical_evaluation_inverse':r.to_json(Oi),'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'actual Frobenius-stable54-point Abel basis and disjoint216-point T2/source support; no formal correspondence function yet'}
sha,size=write_checkpoint(Path('/tmp/p41_t2_abel_select47_checkpoint.json.gz'),out);print('ACTUAL T2 ABEL CHART SELECTED',out['points_1based'],'bytes',size,'sha',sha,flush=True)
