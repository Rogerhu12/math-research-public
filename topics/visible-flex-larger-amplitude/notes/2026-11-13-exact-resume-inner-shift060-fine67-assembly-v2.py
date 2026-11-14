#!/usr/bin/env python3
"""Assemble actual owned fine67 DQ and original-panel endpoint batches.

This only joins complete, frozen successful batches and pins every original
numerical payload. RAM-to-disk relocation preserves bytes and is explicit.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,resource,time
E=Path('/workspace/scratch/d1aa462cfc02/exact-work')
WRAPPER='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
DQ_SOURCE='d75f7b5728a1b86cb24db6e9592e6e76025872e057165d05896bdcc01ad6b698'
DQ_PINS=['b2fa2a9322b710fe69d32a98d42400d8162e13ec1ee6bba248f35ac48489b802','2ac1158a360edb85d94c92897b0827a17a8c291bd9f3e38f6d05da9d307bc76c','7fbddc84c90c3e77ac8b7d3d04e9e95fe737b7e7b1a619f7cf0657eda81f61be','fd3e2455148f2c1095adcd658bed31a2cf9e0e0bf94ffac05e8a003d7f551ffa']
DQ_RPINS=['0408ae971df06eda6c33a8c856b6f2d0de808c90cb452d5f93826d05b05e5da9','1cc65aceb0225c664ae9899efc45e9416a4b190bf88b392f9af285f217e6ba91','b44b12891178e160093c4e5e03993aec4668eba553471f7feeb6403347da0ff4','3e3a1e391cf40a0572d50f09f7dbf46831b186dbea5dcbd1dd8186f52ebdbaaa']
END_SOURCE='34f06d057a75b67598d55ff13d461daf93838ffa8d6f3c010c9dde3987a333e2'
END_PINS=['c33ee02b83cdc6e755b88d4e07e7898385ee8f4eb9a2c07e830edc86f99b0cd5','cc2caf0afd53cf787294464baf620c5e5f0bfe8d7b23ebc3afa4fbd728572820','0f111fd08efb09eea165fb0b94ab142740b50b0aaafe3b5984e21e8ff4459b5e','5bcd10d73d48f0e4800f961a95f2b172af0c8fbf697ae2374779b4c4429c8ee8']
END_RPINS=['e9da9ff1354db2235ffcab0e1ddf8136f8c6e3eb90d6c181971ba1d495c83131','ad4b7040b58a179b3d942e0695dd7f7ab860a62d7b2458c0f82bd196c35a1645','7b620e7ac6faf57d938bf2d0ac8c5f3fa85d7830da8799f40f7254e19a204f92','f25e7793e5de8aaa29b3a1cc1e77d03682594968498614bc4f1010da39fab845']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def owned(r):return r['exitcode']==0 and r['termination_signal'] is None and r['peak_rss_kib']<98304 and r['resource_wrapper_sha256']==WRAPPER
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('immutable new aggregate')
 start=time.monotonic();g={};counts={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True;counts[k]=counts.get(k,0)+1
 relocation=E/'fine67-RAM-relocation-r1.json';gate('frozen_relocation',sha(relocation)=='8ac7253a5550c1326b21df165bb20a4a690da422a99355be7d938ce7fcc07c29')
 batches=[];chunks=[];payload=hashlib.sha256();first=None;expected=12
 for i in range(1,5):
  folder=E/f'inner-actual-LF-shift060-fine67-DQ-r2-batch{i:02d}';p=folder/'certificate.json.gz';rp=E/f'inner-actual-LF-shift060-fine67-DQ-r2-batch{i:02d}-resource.json'
  gate('DQ_batch_pins',sha(p)==DQ_PINS[i-1] and sha(rp)==DQ_RPINS[i-1]);d=read(p);r=read(rp)
  gate('DQ_batch_owned_success',owned(r) and d['all_gates'] and all(d['gates'].values()) and d['source_sha256']==DQ_SOURCE)
  if first is None:first=d
  for k in ('input_identities','domain','angular_weight_translation','windows_out','windows_in','membership_partition','membership_intervals','material_units','operator_contract'):
   gate('same_DQ_definition_'+k,d[k]==first[k])
  gate('ordered_source_batch',d['first_cell']==expected and d['cells']==list(range(d['first_cell'],d['last_cell']+1)))
  for cr in d['chunk_records']:
   q=folder/Path(cr['path']).name;gate('exact_chunk_and_relocated_bytes',cr['cell']==expected and q.stat().st_size==cr['bytes'] and sha(q)==cr['sha256']);expected+=1
   row=read(q);gate('complete_saved_DQ_shape',row['cell']==cr['cell'] and len(row['kernels_s_upper'])==len(row['kernels_ell_upper'])==67 and all(len(z)==68 for key in ('kernels_s_upper','kernels_ell_upper') for z in row[key]))
   payload.update((json.dumps(row,separators=(',',':'),sort_keys=True)+'\n').encode())
   chunks.append(dict(**{k:v for k,v in cr.items() if k!='path'},path=str(q),original_batch_path=cr['path']))
  batches.append(dict(path=str(p),sha256=sha(p),resource_path=str(rp),resource_sha256=sha(rp),original_source_sha256=DQ_SOURCE,original_gate_count=d['gate_count'],first_cell=d['first_cell'],last_cell=d['last_cell']))
 gate('all213_fine67_source_cells',expected==225 and len(chunks)==213)
 eb=[];erows=[];efirst=None;expected=0
 for i in range(1,5):
  p=E/f'inner-cell12-logr-rest67-batch{i:02d}.json';rp=E/f'inner-cell12-logr-rest67-batch{i:02d}-resource.json'
  gate('endpoint_batch_pins',sha(p)==END_PINS[i-1] and sha(rp)==END_RPINS[i-1]);d=read(p);r=read(rp)
  gate('endpoint_batch_owned_success',owned(r) and d['all_gates'] and all(d['gates'].values()) and d['source_sha256']==END_SOURCE and d['original_panels']==1873)
  if efirst is None:efirst=d
  for k in ('input_identities','windows','segment_panel_counts','source_scale_squared_upper','true_w_out_lower','input_nextcell_Vprime_boundary_upper','input_strip_original','output_strip_original'):
   gate('same_endpoint_definition_'+k,d[k]==efirst[k])
  gate('ordered_endpoint_batches',d['first_window']==expected)
  for row in d['rows']:
   gate('complete_endpoint_row',row['index']==expected and row['window']==d['windows'][expected]);expected+=1;erows.append(row)
  eb.append(dict(path=str(p),sha256=sha(p),resource_path=str(rp),resource_sha256=sha(rp),original_source_sha256=END_SOURCE,original_gate_count=d['gate_count']))
 gate('all17_refined_rest_windows',expected==17 and len(erows)==17 and sum((list(range(lo,hi+1,2)) for lo,hi in efirst['windows']),[])==list(range(186,513,2)))
 gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 out=dict(schema='inner-actual-LF-shift060-fine67-DQ-and-rest-endpoint-aggregate-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=True,gates=g,gate_categories=counts,gate_count=sum(counts.values()),DQ_batches=batches,endpoint_batches=eb,relocation_record=dict(path=str(relocation),sha256=sha(relocation)),input_identities=first['input_identities'],domain=first['domain'],angular_weight_translation=first['angular_weight_translation'],windows_out=first['windows_out'],windows_in=first['windows_in'],modes_center=first['modes_center'],chunk_records=chunks,canonical_DQ_rows_sha256=payload.hexdigest(),endpoint_windows=efirst['windows'],endpoint_rows=erows,endpoint_metadata={k:efirst[k] for k in ('source_scale_squared_upper','true_w_out_lower','input_nextcell_Vprime_boundary_upper','input_strip_original','output_strip_original','source_units','output_units')},low_projection_fixed=True,all213_source_cells=True,all1873_original_panels_each_endpoint_batch=True,complete_mean_inverse_and_quadratic_remainders_not_in_DQ=True,original_parent_mass_constraints_required=True,no_new_ODE_or_Green_or_integral=True,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0);gate('small_complete_aggregate',len(raw)<1000000);a.out.write_bytes(raw)
 print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
