#!/usr/bin/env python3
"""Bind returned exact finite certificates; never rerun coefficient computation."""
import argparse,gzip,hashlib,json
from math import isqrt
from pathlib import Path


def read(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def primes(lower,upper):
 sieve=bytearray(b'\1')*(upper+1);sieve[0:2]=b'\0\0'
 for p in range(2,isqrt(upper)+1):
  if sieve[p]:sieve[p*p:upper+1:p]=b'\0'*(((upper-p*p)//p)+1)
 return [p for p in range(lower,upper+1) if sieve[p] and p%9 in (2,5)]


def collect(topic):
 run='43585949869-1';source='0202228ff67b38a0e41302cd491cf40e949b7396'
 expected=primes(2001,200000);rows=[];shards=[]
 for shard in range(4):
  base=topic/'computations'/('R698-window-'+str(shard))/run
  summary=read(base/'summary.json');initial=read(base/'public-actions-input.json')
  assert summary['complete'] and summary['source_commit']==initial['source_commit']==source
  assert summary['expected_primes']==initial['selected_primes']==expected[shard::4]
  assert initial['all_window_primes']==expected
  current=read(base/'rows.json.gz');assert sha(base/'rows.json.gz')==summary['rows_sha256']
  assert summary['tested_count']==len(current)==len(expected[shard::4])
  assert [row['prime'] for row in current]==expected[shard::4]
  arithmetic=base/'R698_fast_scalar_window.py.gz';wrapper=base/'R698_public_window.py.gz'
  parameters=base/'R698-public-window-request.json.gz'
  for file,key in [(arithmetic,'arithmetic_source_sha256'),(wrapper,'wrapper_source_sha256'),(parameters,'parameters_sha256')]:
   assert hashlib.sha256(gzip.decompress(file.read_bytes())).hexdigest()==summary[key]==initial[key]
  for row in current:
   cert=base/row['certificate'];assert sha(cert)==row['certificate_sha256']
   value=read(cert);p=row['prime'];assert value['source_commit']==source and 6*value['N']+5==p
   assert value['full_exponential_recurrence_checked'] and value['maximum_divisor']<p
   assert value['first_excluded_H_denominator']==p
   for key in ['arithmetic_source_sha256','wrapper_source_sha256','parameters_sha256']:
    assert value[key]==summary[key]
   for key in ['prime','N','A_p','A_p_minus_3','C_p','C_p_minus_3','coefficient_TC','coefficient_TZ3','zero_channels']:
    assert value[key]==row[key]
   for key in ['A_p','A_p_minus_3','C_p','C_p_minus_3','coefficient_TC','coefficient_TZ3']:
    assert 0<=row[key]<p
   ell2=pow(2,(p-1)//2,p)
   assert row['A_p']==-ell2*row['coefficient_TC']%p
   assert row['A_p_minus_3']==2*pow(3,-1,p)*ell2*row['coefficient_TZ3']%p
   assert row['C_p']==-3*row['A_p']**2%p and row['C_p_minus_3']==-3*row['A_p_minus_3']**2%p
   assert row['zero_channels']==[key for key in ['C_p','C_p_minus_3'] if row[key]==0]
  assert summary['zeros']==[row for row in current if row['zero_channels']]
  shards.append({'shard':shard,'count':len(current),'summary_file':str((base/'summary.json').relative_to(topic)),
   'summary_sha256':sha(base/'summary.json'),'rows_sha256':sha(base/'rows.json.gz'),
   'arithmetic_source_sha256':summary['arithmetic_source_sha256']})
  rows.extend(current)
 rows.sort(key=lambda r:r['prime']);assert [row['prime'] for row in rows]==expected
 zero=[r for r in rows if r['zero_channels']];assert len(zero)==1 and zero[0]['prime']==137147
 assert zero[0]['zero_channels']==['C_p_minus_3'] and zero[0]['C_p']==80155
 old=read(topic/'notes/R689-exact-window.json');assert old['finite_window_complete'] and old['prime_count']==99 and not old['zeros']
 assert [r['p'] if 'p' in r else r['prime'] for r in old['rows']]==primes(41,2000)
 allprimes=primes(41,200000);assert len(allprimes)==len(expected)+old['prime_count']==5992
 original=topic/'computations/R706-original-z-137147/43587480525-1'
 summary=read(original/'summary.json');assert summary['complete'] and summary['agrees_with_original_window']
 cert=original/summary['certificate'];assert sha(cert)==summary['certificate_sha256']
 value=read(cert);assert value['prime']==137147 and value['N']==22857
 assert not value['uses_R698_H_T_Z_or_Lagrange_Frobenius_reduction'] and not value['division_by_p_used']
 assert value['all_sigma_logarithm_relations_checked']==22857
 assert value['newton_steps'][0]['from_precision']==1 and value['newton_steps'][-1]['to_precision']==22858
 for step in value['newton_steps']:assert step['full_energy_equation_checked']
 for key in ['A_p','A_p_minus_3','C_p','C_p_minus_3']:assert value[key]==zero[0][key]
 assert value['coefficient_x_sigma6']==103259 and value['coefficient_minus_xy_sigma6']==0
 for name,arr in value['coefficients'].items():
  assert len(arr)==22858 and all(0<=a<137147 for a in arr)
  assert hashlib.sha256(json.dumps(arr,separators=(',',':')).encode()).hexdigest()==value['coefficient_sha256'][name]
 assert len(value['F_last_summands'])==len(value['G_last_summands'])==22858
 assert sum(value['F_last_summands'])%137147==103259 and sum(value['G_last_summands'])%137147==0
 return {'result':'R706','finite_window_complete':True,'all_window_prime_count':5992,
  'lower':41,'upper':200000,'residues_mod9':[2,5],'new_window_count':len(expected),
  'previous_result':'R689','previous_manifest_sha256':sha(topic/'notes/R689-exact-window.json'),
  'shards':shards,'unique_zero':zero[0],'all_Cp_nonzero':True,'other_Cp_minus3_nonzero':True,
  'window_run':43585949869,'window_source_commit':source,'independent_original_z_run':43587480525,
  'independent_original_z_source_commit':summary['source_commit'],'independent_original_z_certificate_sha256':sha(cert),
  'independent_original_z_values':summary['values'],'coefficient_computation_repeated_by_collector':False,
  'M2_itself_proved_zero':False,'all_prime_minimum_M2_valuation_claim_refuted':True,
  'Serre_counterexample_claimed':False,'collector_sha256':sha(Path(__file__))}


if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--topic',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 result=collect(args.topic);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'new_count':result['new_window_count'],'all_count':result['all_window_prime_count'],'unique_zero':result['unique_zero']['prime'],'original_z_values':result['independent_original_z_values']}))
