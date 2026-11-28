#!/usr/bin/env python3
"""Extend exact original tail queries using verified local original raw blobs.

Every inherited extension is checked against the actual old/new cache chain.
Only new radii are evaluated by the unchanged registered Fraction streamer.
Existing exact evaluator values are copied, not refitted. Every original raw
blob is checked by manifest bytes, SHA256 and Git-blob SHA1 before use. No
network or credential is needed. Full source and endpoint identities, all
original diagnostic windows and old query inclusion are checked before merge.
"""
import argparse,hashlib,importlib.util,json,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


V1_EXTENSION_SOURCE_SHA='78d9d18434598cfd2174112221d26e5c57972d5e701ec66f7aeb15f1b1f89ee0'
SOURCE_RECEIPT_KEYS=('manifest_sha256','continuous_bounds_helper_sha256','continuous_original_source_second_jets','diagnostic_groups','diagnostic_windows_exact','diagnostic_source_spans','true_cuff_exact','finite_inner_exact','outer_cut_exact','integrated_spans')
QUERY_KEYS={'query_fraction','query_radius','coefficients'}

def read_bound_bundle(bundle,manifest,streamer):
 report_path,cache_path,queries_path=map(Path,bundle);report=json.loads(report_path.read_text())
 for key,path in [('manifest_sha256',manifest),('endpoint_cache_sha256',cache_path),('query_file_sha256',queries_path)]:
  if report[key]!=sha(path):raise ValueError('Actual parent bundle binding changed '+key)
 if 'source_regularization' in report:raise ValueError('This extension only consumes the original Q-free source')
 with np.load(cache_path,allow_pickle=False) as saved:arrays={k:saved[k].copy() for k in saved.files}
 requested=set(str(Q(x)) for x in json.loads(queries_path.read_text())['radii'])
 if requested!=set(map(str,arrays['query_fraction'])):raise ValueError('Parent cache query values do not match its exact declared recipe')
 return report,arrays

def same_query_rows(target,target_map,source,source_map,keys):
 for left in range(0,len(keys),256):
  rr=keys[left:left+256];ii=[target_map[r] for r in rr];jj=[source_map[r] for r in rr]
  for name in ('query_radius','coefficients'):
   if target[name].dtype!=source[name].dtype or not np.array_equal(target[name][ii],source[name][jj]):raise ArithmeticError('Parent extension changed exact evaluator values '+name)

def verify_actual_parent_chain(bundle,bundles,manifest,streamer,receipts,active=None):
 active=set() if active is None else active;identity=sha(bundle[0])
 if identity in active:raise ValueError('Cyclic exact-source parent chain')
 active.add(identity);old,arrays=read_bound_bundle(bundle,manifest,streamer)
 source=old['script_sha256']
 if source==sha(streamer):
  receipts.append({'report_sha256':identity,'producer_sha256':source,'cache_sha256':sha(bundle[1]),'queries':len(arrays['query_fraction']),'kind':'original_registered_Fraction_streamer'})
 else:
  if source not in (V1_EXTENSION_SOURCE_SHA,sha(__file__)):raise ValueError('Unknown exact-query extension source; no implicit identity exception')
  if old.get('schema') not in ('2ecf-original-M12-exact-tail-queries-local-extension-v1','2ecf-original-M12-exact-tail-queries-local-extension-v2'):raise ValueError('Unknown exact-query extension schema')
  if old.get('original_Fraction_streamer_sha256')!=sha(streamer):raise ValueError('Original exact streamer changed in extension')
  for k in ('original_exact_source_unchanged','original_g_unchanged','old_query_values_copied_without_refit','original_endpoint_and_diagnostic_arrays_exact_value_equal','full_source_continuous_receipt_exactly_equal'):
   if old.get(k) is not True:raise ValueError('Missing explicit original-source parent condition '+k)
  parent_id=old['old_report_sha256']
  if parent_id not in bundles:raise ValueError('Provide the actual --ancestor-bundle for report '+parent_id)
  parent_bundle=bundles[parent_id]
  if old['old_cache_sha256']!=sha(parent_bundle[1]):raise ValueError('Parent exact cache mismatch')
  parent,previous=verify_actual_parent_chain(parent_bundle,bundles,manifest,streamer,receipts,active)
  p=Path(bundle[0]);new_bundle=(Path(str(p)+'.new-only.json'),Path(str(p)+'.new-only.json.npz'),Path(str(p)+'.new-only.queries.json'))
  for key,path in [('new_only_report_sha256',new_bundle[0]),('new_only_cache_sha256',new_bundle[1]),('new_only_query_recipe_sha256',new_bundle[2])]:
   if old[key]!=sha(path):raise ValueError('Actual original new-only source output changed '+key)
  new,additional=read_bound_bundle(new_bundle,manifest,streamer)
  if new['script_sha256']!=sha(streamer):raise ValueError('New-only values must come from unchanged registered Fraction streamer')
  for k in SOURCE_RECEIPT_KEYS:
   if old[k]!=parent[k] or old[k]!=new[k]:raise ArithmeticError('Parent full exact original-source proof changed '+k)
  if set(arrays)!=set(previous) or set(arrays)!=set(additional):raise ValueError('Source array schema changed along parent chain')
  for k in set(arrays)-QUERY_KEYS:
   if arrays[k].dtype!=previous[k].dtype or arrays[k].dtype!=additional[k].dtype or not np.array_equal(arrays[k],previous[k]) or not np.array_equal(arrays[k],additional[k]):raise ArithmeticError('Parent endpoint/diagnostic array changed '+k)
  target_map={str(r):i for i,r in enumerate(arrays['query_fraction'])};parent_map={str(r):i for i,r in enumerate(previous['query_fraction'])};new_map={str(r):i for i,r in enumerate(additional['query_fraction'])}
  if set(parent_map)&set(new_map) or set(target_map)!=set(parent_map)|set(new_map):raise ValueError('Parent extension does not exactly partition old and genuinely new source rows')
  same_query_rows(arrays,target_map,previous,parent_map,list(parent_map));same_query_rows(arrays,target_map,additional,new_map,list(new_map))
  receipts.append({'report_sha256':identity,'producer_sha256':source,'cache_sha256':sha(bundle[1]),'queries':len(target_map),'kind':'fully_checked_old_plus_new_exact_extension','parent_report_sha256':parent_id,'new_only_report_sha256':sha(new_bundle[0]),'old_and_new_actual_values_verified':True})
 active.remove(identity);return old,arrays

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','manifest','raw-directory','old-report','old-cache','old-queries','queries','out'):ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--ancestor-bundle',type=Path,nargs=3,action='append',default=[],metavar=('REPORT','CACHE','QUERIES'))
 a=ap.parse_args();began=time.monotonic();output_cache=Path(str(a.out)+'.npz')
 if a.out.exists() or output_cache.exists():raise FileExistsError('Fresh exact-query extension outputs required')
 whole=json.loads(a.queries.read_text());streamer=a.scripts/'6a65-m12-stream-tail-multiple-diagnostic-windows.py'
 actual_bundle=(a.old_report,a.old_cache,a.old_queries);bundles={sha(b[0]):b for b in [actual_bundle,*a.ancestor_bundle]};chain_receipts=[]
 old,old_arrays=verify_actual_parent_chain(actual_bundle,bundles,a.manifest,streamer,chain_receipts)
 old_map={str(r):i for i,r in enumerate(old_arrays['query_fraction'])};requested=sorted(set(str(Q(r)) for r in whole['radii']),key=Q)
 if not set(old_map)<=set(requested):raise ValueError('An old source query would be lost')
 additional=[r for r in requested if r not in old_map]
 if not additional or len(additional)>12000:raise ValueError('Use the unchanged producer on 1..12000 genuinely new source queries')
 temporary_query=Path(str(a.out)+'.new-only.queries.json');temporary_report=Path(str(a.out)+'.new-only.json')
 if temporary_query.exists() or temporary_report.exists():raise FileExistsError('Fresh exact-query extension intermediates required')
 temporary_query.write_text(json.dumps({'schema':'2ecf-original-M12-new-radii-for-exact-extension-v1','radii':additional},indent=2)+'\n')
 entry=load('unchanged_original_M12_Fraction_streamer',streamer);raw_receipts=[]
 def verified_local(producer,blob,info,transport,headers):
  path=a.raw_directory/Path(info['path']).name;raw=path.read_bytes()
  if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256']:raise ValueError('Wrong actual original local raw payload '+path.name)
  if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:raise ValueError('Wrong original local Git blob '+path.name)
  raw_receipts.append({'name':path.name,'bytes':len(raw),'sha256':info['sha256'],'git_blob':blob});return raw
 entry.recover_payload=verified_local
 argv=[str(streamer),'--manifest',str(a.manifest),'--endpoint-producer',str(a.scripts/'6a65-m12-stream-tail-exact-endpoint.py'),'--queries',str(temporary_query),'--out',str(temporary_report),'--source-transport','raw-known-commit','--diagnostic-subdivisions',str(old['diagnostic_subdivisions'])]
 for pair in old['diagnostic_windows_exact']:argv+=['--diagnostic-window',*pair]
 sys.argv=argv;entry.main();new=json.loads(temporary_report.read_text());new_arrays={}
 with np.load(str(temporary_report)+'.npz',allow_pickle=False) as f:
  for k in f.files:new_arrays[k]=f[k].copy()
 for k in ('manifest_sha256','continuous_bounds_helper_sha256','continuous_original_source_second_jets','diagnostic_groups','diagnostic_windows_exact','diagnostic_source_spans','true_cuff_exact','finite_inner_exact','outer_cut_exact','integrated_spans'):
  if new[k]!=old[k]:raise ArithmeticError('Unchanged exact-source certificate identity differs '+k)
 query_keys={'query_fraction','query_radius','coefficients'}
 if set(old_arrays)!=set(new_arrays):raise ValueError('Original numerical cache schema changed')
 for k in set(old_arrays)-query_keys:
  if old_arrays[k].dtype!=new_arrays[k].dtype or not np.array_equal(old_arrays[k],new_arrays[k]):raise ArithmeticError('An original endpoint/diagnostic array changed '+k)
 new_map={str(r):i for i,r in enumerate(new_arrays['query_fraction'])}
 if set(new_map)!=set(additional):raise ArithmeticError('Not all genuinely new exact source queries returned')
 merged={k:v for k,v in old_arrays.items() if k not in query_keys};merged['query_fraction']=np.asarray(requested)
 merged['query_radius']=np.empty(len(requested),dtype=old_arrays['query_radius'].dtype)
 merged['coefficients']=np.empty((len(requested),*old_arrays['coefficients'].shape[1:]),dtype=old_arrays['coefficients'].dtype)
 for i,r in enumerate(requested):
  source,index=(old_arrays,old_map[r]) if r in old_map else (new_arrays,new_map[r]);merged['query_radius'][i]=source['query_radius'][index];merged['coefficients'][i]=source['coefficients'][index]
 for r,i in old_map.items():
  j=requested.index(r)
  if not np.array_equal(merged['coefficients'][j],old_arrays['coefficients'][i]):raise ArithmeticError('Stored old evaluator values changed during exact-query extension')
 np.savez_compressed(output_cache,**merged)
 report=dict(old);report.update(script_sha256=sha(__file__),schema='2ecf-original-M12-exact-tail-queries-local-extension-v2',
  original_Fraction_streamer_sha256=sha(streamer),actual_verified_parent_chain=chain_receipts,query_file_sha256=sha(a.queries),endpoint_cache_sha256=sha(output_cache),queries=len(requested),
  source_transport='verified-original-local-blob-cache-and-verified-prior-exact-evaluator',
  original_exact_source_unchanged=True,original_g_unchanged=True,old_query_values_copied_without_refit=True,
  original_endpoint_and_diagnostic_arrays_exact_value_equal=True,full_source_continuous_receipt_exactly_equal=True,
  old_report_sha256=sha(a.old_report),old_cache_sha256=sha(a.old_cache),new_only_report_sha256=sha(temporary_report),new_only_cache_sha256=sha(str(temporary_report)+'.npz'),
  new_only_query_recipe_sha256=sha(temporary_query),old_queries=len(old_map),new_distinct_queries=len(additional),verified_local_raw_blobs=raw_receipts,
  new_nonlinear_field_claimed=False,seconds=time.monotonic()-began)
 a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'actual_extended_exact_query_report':str(a.out),'report_sha256':sha(a.out),'cache_sha256':sha(output_cache),'old_queries':len(old_map),'new_distinct_queries':len(additional),'full_queries':len(requested),'same_original_source_and_g':True,'verified_original_raw_count':len(raw_receipts),'seconds':report['seconds']}),flush=True)
if __name__=='__main__':main()
