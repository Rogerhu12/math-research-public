#!/usr/bin/env python3
"""Certify the original quintic collar all the way to the actual fixed cuff."""
import argparse,gzip,hashlib,importlib.util,json,sys,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
prod=load('true_collar_correlated_production',HERE/'2ecf-m12-tail-correlated-production.py')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
class TrueCollar(prod.CachedTail):
 def inverse_r(self,r):
  # The true right material endpoint is z=1 exactly, for every allowed
  # bridge/root parameter. Intersect its inverse enclosure with that identity.
  if r==self.c-self.h:return prod.I(1)
  return super().inverse_r(r)
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('scripts','data','grid','field','result','correction-bounds','primitive','raw-cache','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--angular',type=int,default=32);p.add_argument('--radial-order',type=int,default=6);p.add_argument('--angular-order',type=int,default=8);p.add_argument('--max-radial-depth',type=int,default=12)
 a=p.parse_args();start=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh true-collar certificate required')
 manifest=a.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
 if sha(manifest)!='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104':raise ValueError('Original source manifest differs')
 meta=json.loads(manifest.read_text());C=meta['format']['coefficientCount'];radial=meta['radialGeometry'];beta=F(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
 helper=prod.load('true_collar_original_bernstein',a.scripts/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
 producer=prod.load('true_collar_original_blobs',a.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
 inner=F(radial['innerAnchor']);cuff=prod.base.fq(meta['parameters']['rCuff']);r=inner;count=0;previous=None;first=None;coverage=[]
 for info in meta['files']:
  name=Path(info['path']).name;raw=(a.raw_cache/name).read_bytes();key=name.split('-raw')[1].split('.f64')[0].replace('-part','-');blob=producer.BLOBS[key]
  if len(raw)!=info['bytes'] or sha(a.raw_cache/name)!=info['sha256'] or hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:raise ValueError('Original blob identity differs')
  data=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
  if not np.all(np.isfinite(data)) or (previous is not None and not np.array_equal(data[0],previous)):raise ValueError('Original raw seam differs')
  if first is None:first=data[0,2:2+4*C].reshape(4,C).copy()
  for ell in data[1:,-1]:
   length=beta*prod.base.fq(ell)
   if length<=0:raise ValueError('Nonpositive original source increment')
   r+=length;count+=1
  previous=data[-1].copy();coverage.append({'file':name,'sha256':info['sha256'],'git_blob':blob})
 if count!=18552 or r!=F(radial['outerAnchor']):raise ArithmeticError('Original source radial normalization differs')
 h=inner-cuff;row={'source_span':-1,'left_exact':str(cuff),'right_exact':str(inner),'V_controls':[],'Vr_controls':[]}
 for j in range(C):
  a0,a1,a2=[prod.base.fq(first[i,j]) for i in range(3)]
  power=[F(0),F(0),F(0),10*a0-4*h*a1+h*h*a2/2,-15*a0+7*h*a1-h*h*a2,6*a0-3*h*a1+h*h*a2/2]
  controls=helper.bernstein(power);row['V_controls'].append(controls);row['Vr_controls'].append(helper.derivative_controls(controls,h))
 source={'manifest_sha256':sha(manifest),'planar_modes':meta['format']['planarModes'],'height_modes':meta['format']['heightModes'],
  'integrated_value_from_exact_original_cumulative_sums':True,'exact_all_source_nodes_and_normalization_checked':True}
 consumer=TrueCollar(a,source)
 if consumer.c-consumer.h!=cuff:raise ArithmeticError('Common-chart true cuff differs from original source')
 cert=consumer.certify(row,a.angular,a.radial_order,a.angular_order);U=F(cert['metric_upper_exact'])
 result={'schema':'2ecf-original-M12-true-inner-collar-correlated-total-Gram-v1','script_sha256':sha(__file__),'production_sha256':sha(prod.__file__),
  'inputs':{name:sha(getattr(a,name)) for name in ('data','grid','field','result','correction_bounds','primitive')},'manifest_sha256':sha(manifest),
  'all_original_raw_blobs_and_exact_radial_nodes_checked':coverage,'true_cuff_exact':str(cuff),'finite_inner_exact':str(inner),
  'source':'Original quintic Hermite collar with zero cuff two-jet and original first finite source two-jet',
  'whole_true_inner_collar_and_all_angles_covered':True,'whole_surface_claim':False,'all_angles_by_original_D3_and_reflection':True,
  'certificate':cert,'metric_upper_exact':str(U),'metric_upper_display':float(U),'below_original_solver_tolerance':U<=F(1,500000000),'seconds':time.monotonic()-start}
 a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(a.out),'sha256':sha(a.out),'bound':float(U),'seconds':result['seconds']}),flush=True)
if __name__=='__main__':main()
