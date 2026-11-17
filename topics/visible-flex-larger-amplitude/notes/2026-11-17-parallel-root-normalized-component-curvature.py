#!/usr/bin/env python3
"""Consume actual finite-node scaling two-jets in component-box curvature.

The exact G, G_s and G_ss formulas are substituted before its component
angle/radial boxes and actual shape operator. Scaling jets are interval parameters, never differentiated as
constant functions. The fixed raw source and strict scaling-source identities
are checked. No candidate, target metric, or construction q4096 is changed.
"""
import argparse,hashlib
from pathlib import Path

PARENT_SHA='459dc01e8e5a7fb2b1910c2f0fb028f196eb0921855386c3858c26ba13a33afc'
SCALING_SHA='e6ddb8c54093b27b03984dac56f86c2864dac0d167c74f133600d50533427927'

SCALING_SETUP='''
 from fractions import Fraction
 scaling_hashes={str(p):sha(p)for p in a.scaling_reports};scaling_records=[];scaling_by_cell={}
 for path in a.scaling_reports:
  record=json.loads(path.read_bytes())
  if record['source_sha256']!=SCALING_SHA or record['input_sha256']!=expected or record['interval_source_sha256']!=dep or record['construction_angles']!=4096:
   raise ValueError('Different scaling certificate object or source')
  if not record.get('all_radius_covered')or not record.get('strict_under_stated_IEEE_arithmetic'):
   raise ValueError('Incomplete scaling certificate')
  values=[record[k]for k in ('lambda_minus_one_bound','lambda_s_bound','lambda_ss_bound')]
  if not all(np.isfinite(v)and v>=0 for v in values)or values[0]>=1:raise ValueError('Invalid scaling bounds')
  row=dict(cell=record['cell'],part=record['part'],left_exact=record['left_exact'],right_exact=record['right_exact'],bounds=values,report_sha256=scaling_hashes[str(path)])
  scaling_records.append(row);scaling_by_cell.setdefault(record['cell'],[]).append(row)
 scaling_bounds={}
 for cell in a.cells:
  if not 0<=cell<len(x)-1:raise ValueError('Invalid requested cell')
  pieces=sorted(scaling_by_cell.get(cell,[]),key=lambda z:Fraction(z['left_exact']))
  edge=Fraction.from_float(float(x[cell]))
  for piece in pieces:
   if Fraction(piece['left_exact'])!=edge or Fraction(piece['right_exact'])<=edge:raise ValueError('Gap/overlap in scaling certificate cover')
   edge=Fraction(piece['right_exact'])
  if edge!=Fraction.from_float(float(x[cell+1])):raise ValueError('Scaling certificates do not cover the whole cell')
  scaling_bounds[cell]=[max(p['bounds'][j]for p in pieces)for j in range(3)]
'''

SCALING_HELPERS='''
 def elevate(value,target):
  while len(value[0])-1<target:
   degree=len(value[0])-1;out=[I.at(value,0)]
   for j in range(1,degree+1):out.append(I.div(I.add(I.scale(I.at(value,j-1),j),I.scale(I.at(value,j),degree+1-j)),I.exact(degree+1)))
   out.append(I.at(value,-1));value=I.stack(out)
  return value
 def center_and_remainder(value):
  center=(np.zeros_like(value[0]),np.zeros_like(value[1]));remainder=(value[0].copy(),value[1].copy())
  for side in (0,1):
   center[side][:,2*M+1]=value[side][:,2*M+1];remainder[side][:,2*M+1]=0.
  return center,remainder
 def normalized_two_jets(b,db,ddb,cell):
  db=elevate(db,5);ddb=elevate(ddb,5)
  c,r=center_and_remainder(b);cs,rs=center_and_remainder(db);css,rss=center_and_remainder(ddb)
  d0,d1,d2=scaling_bounds[cell]
  lam=I.add(I.exact(1.),(-d0,d0));lamp=(-d1,d1);lampp=(-d2,d2)
  position=I.add(c,I.mul(lam,r))
  first=I.add(cs,I.add(I.mul(lam,rs),I.mul(lamp,r)))
  second=I.add(css,I.add(I.mul(lam,rss),I.add(I.scale(I.mul(lamp,rs),2),I.mul(lampp,r))))
  return position,first,second
'''

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main(a):
 if sha(a.raw_source)!=PARENT_SHA:raise ValueError('Frozen curvature kernel changed')
 text=a.raw_source.read_text()
 def replace(old,new):
  nonlocal text
  if text.count(old)!=1:raise ValueError('Expected unique frozen source anchor')
  text=text.replace(old,new)
 first=text.index('"""');last=text.index('"""',first+3)+3
 text=text[:first]+'"""Continuous normalized G curvature on certified unchanged pulse cells.\nExact scaling two-jets are interval parameters; only the declared cells are covered.\n"""'+text[last:]
 replace(' tr=I.Transform(Q);nu=2*np.arange(M+1)',SCALING_SETUP+'\n tr=I.Transform(Q);nu=2*np.arange(M+1)')
 replace(' def channels(b):',SCALING_HELPERS+'\n def channels(b):')
 replace('  cb,cdb,cddb=channels(b),channels(db),channels(ddb)','  b,db,ddb=normalized_two_jets(b,db,ddb,i)\n  cb,cdb,cddb=channels(b),channels(db),channels(ddb)')
 replace('raw_principal_curvature_upper=worst','normalized_principal_curvature_upper=worst,scaling_bounds=scaling_bounds[i]')
 replace(" if sha(__file__)!=source_sha or sha(a.input)!=expected or sha(a.interval_source)!=dep:raise ValueError('Input/source changed')", " if sha(__file__)!=source_sha or sha(a.input)!=expected or sha(a.interval_source)!=dep or sha(a.raw_source)!=PARENT_SHA or any(sha(p)!=s for p,s in scaling_hashes.items()):raise ValueError('Input/source/scaling evidence changed')")
 replace("full_prefix=False,parent_source_sha256='8fceba9ac17a3dc79ad4d35b6e38767007f1b45179c59f9589a7ff050349efb3')", "full_prefix=False,parent_source_sha256='8fceba9ac17a3dc79ad4d35b6e38767007f1b45179c59f9589a7ff050349efb3',raw_curvature_source_sha256=PARENT_SHA,scaling_source_sha256=SCALING_SHA,scaling_certificates=scaling_records,generated_kernel_sha256=GENERATED_SHA)")
 generated_sha=hashlib.sha256(text.encode()).hexdigest()
 namespace=dict(__name__='normalized_curvature_kernel',__file__=__file__,PARENT_SHA=PARENT_SHA,SCALING_SHA=SCALING_SHA,GENERATED_SHA=generated_sha)
 exec(compile(text,str(a.raw_source)+'::exact-normalization-two-jet-substitution','exec'),namespace)
 namespace['main'](a)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('input','interval-source','raw-source','out'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--scaling-reports',type=Path,nargs='+',required=True)
 p.add_argument('--cells',type=int,nargs='+',default=[458,817]);p.add_argument('--angles',type=int,default=16384);p.add_argument('--radial-subdivisions',type=int,default=4)
 main(p.parse_args())
