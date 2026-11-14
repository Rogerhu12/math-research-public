#!/usr/bin/env python3
"""Actual three-target T2 cubic jets and full coefficient identities at level41."""
import argparse,gzip,hashlib,json,subprocess,sys
from pathlib import Path

def write_checkpoint(path,data):
 # This raw full-fibre intermediate stays in scratch; the deliverable is a
 # separate restricted certificate. It may exceed the repository file cap.
 assert str(path).startswith('/tmp/')
 raw=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
 packed=gzip.compress(raw,mtime=0);tmp=path.with_suffix(path.suffix+'.new')
 tmp.write_bytes(packed);tmp.replace(path)
 return hashlib.sha256(packed).hexdigest(),len(packed)

def evaluate_batched(Es,Hs,model,C,r,degree):
 import numpy as np
 from p41_hecke3_jets47 import trace_indices
 values=[]
 for H in Hs:
  gram=np.zeros((840,840),dtype=np.int64)
  for j in range(degree+1):
   first=(Es[j].T@H)%r.Q
   gram=(gram+first@Es[degree-j])%r.Q
  result=np.zeros((820,73),dtype=np.int64)
  for start in range(0,820,24):
   stop=min(start+24,820)
   mini={key:model[key] for key in ('sl2_normalizer_mod_signs','basis_pairs')}
   mini['sl2_representatives']=model['sl2_representatives'][start:stop]
   a,b,signs=trace_indices(mini)
   result[start:stop]=(gram[a,b]*signs).sum(axis=2)%r.Q
  values.append(result)
 return r.mm(tuple(values),C)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--script-dir',type=Path,required=True)
 ap.add_argument('--gp',default='/tmp/pari-2.19.0/gp')
 ap.add_argument('--source-jets',type=Path,default=Path('/tmp/p41_formal47_abel_jets_checkpoint.json.gz'))
 ap.add_argument('--source-cubic',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
 ap.add_argument('--hecke',type=Path,default=Path('/tmp/p41_hecke47_checkpoint.json.gz'))
 ap.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke2_cubic47_checkpoint.json.gz'))
 args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
 import numpy as np
 import p41_r2_matrix as r
 from p41_hecke3_jets47 import trace_indices

 def read(path):
  raw=path.read_bytes();return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()
 paths=[folder/'data/p41_local47_torsion_certificate.json',folder/'data/p41_makdisi47_certificate.json.gz',args.source_jets,args.source_cubic,args.hecke]
 loaded=[read(p) for p in paths];torsion,model,source,cubic,hecke=[v[0] for v in loaded];ih={p.name:v[1] for p,v in zip(paths,loaded)}
 scripts=[folder/n for n in ['p41_local47_torsion.gp','p41_makdisi47.gp','p41_cm3_makdisi47.gp','p41_cusp_divisors47.gp','p41_cm4_divisor47.gp','p41_formal47_abel_jets.gp']]+[Path(__file__).with_name('p41_hecke2_cubic_lowmem47.gp'),Path(__file__).with_suffix('.gp')]
 sh={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in scripts};sh[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 op=hecke['operators']['2'];curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
 C=r.from_json(model['basis_inverse'])
 out={'level':41,'auxiliary_prime':47,'precision':4,'input_sha256':ih,'generating_source_sha256':sh,'targets':[],'status':'actual T2 cubic targets in progress'}
 if args.output.exists():
  prev,_=read(args.output);assert prev['input_sha256']==ih and prev['generating_source_sha256']==sh;out=prev
 work=Path('/tmp/serre-p41-hecke2-cubic-work')/hashlib.sha256(json.dumps([ih,{k:v for k,v in sh.items() if k.endswith('.gp')}],sort_keys=True).encode()).hexdigest();work.mkdir(parents=True,exist_ok=True)
 for n,target in enumerate(op['targets']):
  if len(out['targets'])>n:continue
  inputs=[torsion['field_polynomial_ascending'],model['sqrt_minus_one_lift'],curve['weil_pairing'],source['P_jets'],source['Q_jets'],target['kernel_x']]
  ip=work/f'input-{n}.gp';opth=work/f'output-{n}.json';ip.write_text('jet_input='+json.dumps(inputs,separators=(',',':'))+';\n')
  if not opth.exists():
   code='\n'.join([f'read({json.dumps(str(s))});' for s in scripts]+[f'read({json.dumps(str(ip))});',f'p41_hecke2_cubic47(jet_input,{json.dumps(str(opth))});','quit;'])
   proc=subprocess.run([args.gp,'-q','-f','-s','67108864'],input=code,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
   print(proc.stdout,flush=True)
   if proc.returncode or '***' in proc.stdout or not opth.exists():raise RuntimeError('actual T2 cubic GP failure')
  rec=json.loads(opth.read_text());Hs=[np.array(x,dtype=np.int64)%r.Q for x in rec[:2]];Es=[np.array(x,dtype=np.int64)%r.Q for x in rec[2]]
  actual=[evaluate_batched(Es,Hs,model,C,r,k) for k in range(4)]
  assert r.to_json(actual[0])==target['evaluation_matrix']
  assert [p[0] for p in rec[3]]==target['P'] and [p[0] for p in rec[4]]==target['Q']
  out['targets'].append({'kernel_x':target['kernel_x'],'kernel_jets':rec[5],'P_jets':rec[3],'Q_jets':rec[4],'evaluation_coefficients':[r.to_json(a) for a in actual]})
  write_checkpoint(args.output,out);print('ACTUAL T2 TARGET',n+1,'all820x73 constants agree with R131 and all0..3 coefficients saved',flush=True)
 perm=[i-1 for i in op['necklace_transport_1based']];tau=[i-1 for i in model['frobenius_permutation_1based']];A=r.from_json(model['frobenius_basis_matrix']);T=r.from_json(op['weight2_operator'])
 roots=[t['kernel_x'] for t in out['targets']]
 for k in range(4):
  mats=[r.rows(r.from_json(t['evaluation_coefficients'][k]),perm) for t in out['targets']]
  for j,mat in enumerate(mats):
   conjugate=roots.index([roots[j][0],-roots[j][1]%r.Q]);assert r.equal(r.mm(mat,A),r.conjugate(r.rows(mats[conjugate],tau)))
  total=r.zeros(820,73)
  for mat in mats:total=r.add(total,mat)
  total=tuple(a*pow(2,-1,r.Q)%r.Q for a in total)
  assert r.equal(total,r.mm(r.from_json(cubic['evaluation_coefficients'][k]),T)),k
 out['necklace_transport_1based']=op['necklace_transport_1based'];out['status']='all actual T2 target cubic jets, independent Velu addition, full constants, four Frobenius identities and four differentiated T2 identities PASS'
 sha,size=write_checkpoint(args.output,out);print('ACTUAL T2 CUBIC COMPLETE',size,sha,flush=True)

if __name__=='__main__':main()
