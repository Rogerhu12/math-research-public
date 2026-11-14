#!/usr/bin/env python3
"""Preserve actual endpoint rows; save the true denominator as a lower bound.
The heavy producer used the correct lower bound in every kernel formula,
but its one descriptive true_w_out_lower field used the generic upward
serializer. This exact readout fixes only that metadata and retains the
original packet, producer, resource and all numerical rows unchanged.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**v[1]
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**v['binary_exponent']
 return F(int(v['numerator']),int(v['denominator']))
def dyad(q):
 assert q>0 and q.denominator&(q.denominator-1)==0
 return [str(q.numerator),-(q.denominator.bit_length()-1)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--primary',type=Path,required=True);p.add_argument('--sha256',required=True);p.add_argument('--resource',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError(a.out)
 assert sha(a.primary)==a.sha256
 d,u=read(a.primary),read(a.resource)
 assert d['all_gates'] and d['original_panels']==1873 and u['exitcode']==0 and u['termination_signal'] is None and u['peak_rss_kib']<98304
 assert d['source_sha256']=='24bd1c9fa56df5b52950b490779536358b6806760ed48d4ca820eef970d01173'
 got={}
 for name in ('base','point'):
  rec=d['input_identities'][name];path=Path(rec['path']);assert sha(path)==rec['sha256'];got[name]=read(path)
 base=got['base'];port=next(c for c in got['point']['cells'] if c['cell']==12)
 true_lower=min(ex(base['true_w_out_lower']),ex(port['true_w_out_lower']));old=d['true_w_out_lower'];rows_hash=hashlib.sha256(json.dumps(d['rows'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
 d['schema']='inner-cell12-true-singleton-logr-exponential-endpoint-normalized-v2'
 d['normalization_readout_correction']=dict(original_field=old,verified_exact_lower=dyad(true_lower),formula='min(base.true_w_out_lower,point.cell12.true_w_out_lower), exact dyadic with no upward rounding',original_field_not_to_be_used_as_a_lower_bound=True,all_kernel_formulas_used_this_correct_lower_before_serialization=True,all_numerical_rows_unchanged=True,canonical_numeric_rows_sha256=rows_hash)
 d['true_w_out_lower']=dyad(true_lower);d['original_actual_primary']=dict(path=str(a.primary),sha256=sha(a.primary));d['original_actual_resource']=dict(path=str(a.resource),sha256=sha(a.resource));d['original_producer_source_sha256']=d['source_sha256'];d['source_sha256']=sha(Path(__file__))
 d['gates']['same_numeric_rows_and_exact_original_denominator']=True;d['gate_count']+=1
 assert hashlib.sha256(json.dumps(d['rows'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==rows_hash
 a.out.write_text(json.dumps(d,separators=(',',':'))+'\n');print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),canonical_rows_sha256=rows_hash,old_field_differs=ex(old)!=true_lower)))
if __name__=='__main__':main()
