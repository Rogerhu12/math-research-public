#!/usr/bin/env python3
"""Evaluate the actual R165 Hecke transport on the two actual R141 Abel charts.

Both direct shifted section products and independently truncated logarithmic
jets are checked. This computes function norms, not a complete local height.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--script-dir',type=Path,required=True)
 ap.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
 ap.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
 ap.add_argument('--output',type=Path,default=Path('/tmp/p41_cm16_transport_norms47_checkpoint.json.gz'))
 args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
 import numpy as np
 import p41_r2_matrix as r
 from p41_group_operations47 import load_sources,make_model
 from p41_formal47_multiply import write_checkpoint
 from p41_hecke3_hessian47 import section_jets
 from p41_poincare_miller47 import log_pair
 from p41_poincare_miller_jets47 import evaluate_jet
 from p41_poincare_norms47 import pair_mul,pair_inverse
 from verify_p41_hecke3_hessian47 import cubic_basis
 def read(path):
  raw=path.read_bytes();return json.loads(gzip.decompress(raw)),hashlib.sha256(raw).hexdigest()
 sources,hashes=load_sources(folder/'data');M=make_model(sources)
 paths=[folder/'data/p41_cm16_divisor47_checkpoint.json.gz',folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz',args.bases,args.jets]
 loaded=[read(p) for p in paths];cm,end,base,jets=[v[0] for v in loaded];ih={p.name:v[1] for p,v in zip(paths,loaded)}
 assert cm['source_sha256']==end['source_sha256']==base['source_sha256']==hashes
 assert base['jets_sha256']==ih[args.jets.name]
 tr=cm['principal_transport']
 coeffs={'fa':(r.from_json(tr['numerator_cubic_coefficients']),3),'fd':(r.from_json(tr['denominator_cubic_coefficients']),3),'qB':(r.from_json(tr['denominator_quadratic_coefficients']),2),'f0':(r.from_json(tr['base_linear_coefficients']),1)}
 _,_,C3=cubic_basis(M['W'],r.zeros(820,73),sources,M,None,r)
 sq=sources[1]['square_basis_monomials_1based'];C2=r.from_json(sources[1]['square_basis_inverse'])
 result=[]
 for fi,fam in enumerate(base['families']):
  pts=[v-1 for v in fam['points_1based']]
  W=[r.rows(r.from_json(v),pts) for v in jets['evaluation_coefficients']]
  V2,V3=section_jets(W,sources,M,r);spaces={1:W,2:V2,3:V3}
  assert r.equal(V2[0],r.rows(M['V2'],pts)) and r.equal(V3[0],r.rows(M['V3'],pts))
  section_values={name:[r.mm(V,co) for V in spaces[d]] for name,(co,d) in coeffs.items()}
  for name,v in section_values.items():
   bad=np.where(~r.units(v[0]).reshape(-1))[0].tolist()
   assert not bad,('actual numerator/denominator meets Abel base',fi,name,bad)
  def logarithmic_jet(v):
   iv=r.inverse_values(v[0]);a,b,c=[r.mul(x,iv) for x in v[1:]];a2=r.mul(a,a)
   return r.hcat(a,r.sub(b,tuple(x*pow(2,-1,r.Q)%r.Q for x in a2)),r.add(r.sub(c,r.mul(a,b)),tuple(x*pow(3,-1,r.Q)%r.Q for x in r.mul(a2,a))))
  J={name:logarithmic_jet(v) for name,v in section_values.items()}
  JH=r.add(r.sub(r.sub(J['fa'],J['fd']),J['qB']),tuple(2*x%r.Q for x in J['f0']))
  def product(v):
   a=[1,0]
   for k in range(54):a=pair_mul(a,[int(v[0][k,0]),int(v[1][k,0])])
   return a
  def hvalues(vals):
   return r.mul(r.mul(vals['fa'],r.mul(vals['f0'],vals['f0'])),r.inverse_values(r.mul(vals['fd'],vals['qB'])))
  basevals={name:v[0] for name,v in section_values.items()};hbase=hvalues(basevals);hb=product(hbase)
  evals=[]
  for name in ('x12','x7'):
   for mult in ('m','H47'):
    witness=end['targets'][name]['targets'][mult]['exponentials'][fi];pr=r.from_json(witness['parameters']);tt=pr[0].T,pr[1].T
    assert all(np.all(a%47==0) for a in tt)
    wt=r.zeros(54,73)
    for w in W[::-1]:wt=r.add(r.mul(wt,tt),w)
    v2t=r.mm(r.mul(r.cols(wt,[a-1 for a,b in sq]),r.cols(wt,[b-1 for a,b in sq])),C2)
    v3t,_,_=cubic_basis(wt,r.zeros(54,73),sources,M,C3,r)
    directspaces={1:wt,2:v2t,3:v3t}
    vals={name:r.mm(directspaces[d],co) for name,(co,d) in coeffs.items()}
    for sec,v in vals.items():
     check=r.zeros(54,1)
     for w in section_values[sec][::-1]:check=r.add(r.mul(check,tt),w)
     assert r.equal(v,check),(fi,name,mult,sec)
    hv=hvalues(vals);norm=pair_mul(product(hv),pair_inverse(hb));ln=log_pair(norm,r)
    lj=evaluate_jet(JH,witness['parameters'],r);assert ln==lj
    record={'class':name,'multiplier':mult,'family_index':fi,'point_sha256':witness['point_sha256'],'norm_hT':norm,'log_norm_hT':ln,'direct_shifted_monomials_equal_cubic_jets':True}
    evals.append(record);print('ACTUAL hT NORM',record,flush=True)
  result.append({'family_index':fi,'point_indices_1based':fam['points_1based'],'base_hT_values':r.to_json(hbase),'log_hT_norm_jets':r.to_json(JH),'all_four_sections_units_on_base':True,'evaluations':evals})
 out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'input_sha256':ih,'actual_function':tr['actual_function'],'actual_divisor':tr['actual_divisor'],'families':result,'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'actual R165 principal transport on both R141 Abel charts; all eight CM-endpoint function norms and 54x3 jets verified by direct shifted section products; no complete local-height claim'}
 sha,size=write_checkpoint(args.output,out);print('ACTUAL HECKE TRANSPORT NORMS SAVED',size,sha,flush=True)

if __name__=='__main__':main()
