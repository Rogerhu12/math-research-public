#!/usr/bin/env python3
"""Compose actual continuous source-cell receipts without a sampling shortcut."""
import argparse,gzip,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def intervals_union(pairs):
 out=[]
 for left,right in sorted(set(pairs)):
  if right<left:raise ValueError('Reversed interval')
  if not out or left>out[-1][1]:out.append([left,right])
  else:out[-1][1]=max(out[-1][1],right)
 return out
def integer_ranges(values):
 return [[a,b+1] for a,b in intervals_union([(int(v),int(v)) for v in []])] if not values else _integer_ranges(values)
def _integer_ranges(values):
 out=[]
 for v in sorted(set(values)):
  if out and out[-1][1]==v:out[-1][1]=v+1
  else:out.append([v,v+1])
 return out
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('scripts','data','grid','field','result','correction-bounds','primitive','raw-cache','inner-collar','out'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--reports',nargs='+',type=Path,required=True);p.add_argument('--allow-partial',action='store_true');a=p.parse_args()
 if a.out.exists():raise FileExistsError('Fresh exact coverage-composition output required')
 manifest=a.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
 if sha(manifest)!='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104':raise ValueError('Original manifest differs')
 meta=json.loads(manifest.read_text());radial=meta['radialGeometry'];beta=F(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
 nodes=[F(radial['innerAnchor'])];expected_raw=[];previous=None
 for info in meta['files']:
  path=a.raw_cache/Path(info['path']).name;raw=path.read_bytes()
  if len(raw)!=info['bytes'] or sha(path)!=info['sha256']:raise ValueError('Original source file identity differs')
  data=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
  if not np.all(np.isfinite(data)) or (previous is not None and not np.array_equal(data[0],previous)):raise ValueError('Original source seam differs')
  for ell in data[1:,-1]:
   length=beta*F.from_float(float(ell))
   if length<=0:raise ValueError('Nonpositive original source length')
   nodes.append(nodes[-1]+length)
  previous=data[-1].copy();expected_raw.append({'file':path.name,'sha256':info['sha256'],'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()})
 if len(nodes)!=18553 or nodes[-1]!=F(radial['outerAnchor']):raise ArithmeticError('Incomplete exact original node range')
 expected={name:sha(getattr(a,name)) for name in ('data','grid','field','result','correction_bounds','primitive')}
 if expected['field']!='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8':raise ValueError('This composition is for the declared actual G12 field')
 allowed={'03c3f0ea36b1003a2d6b91e3e5b9cae2d493ca6a8784563ce4a26a82956948cf','d7b6c58f17c8b61e64eb2ad57ed21306abaf0a6633fdeb1299b410c7c167bcc7'}
 U=F(0);covered={};sources=[];piece_count=0
 for path in a.reports:
  d=json.loads(path.read_text())
  if d['inputs']!=expected or d['manifest_sha256']!=sha(manifest) or d['script_sha256'] not in allowed:raise ValueError('Cell receipt belongs to a different field, input, or declared consumer')
  if not d['all_angles_by_original_D3_and_reflection'] or d['source_polynomials_sha256'] is not None:raise ValueError('A complete original-source angular cell receipt is required')
  actual=[{k:v[k] for k in ('file','sha256','git_blob')} for v in d['all_original_raw_blobs_verified']]
  if actual!=expected_raw or d['all_original_raw_blobs_verified'][-1]['spans_through']!=18552:raise ValueError('Original source was not completely verified')
  rowpath=path.parent/d['row_stream_path']
  if sha(rowpath)!=d['row_stream_sha256']:raise ValueError('Exact row stream identity differs')
  ids=[];local=F(0)
  with rowpath.open() as stream:
   for line in stream:
    row=json.loads(line);i=row['source_span']
    if not 0<=i<18552 or i in covered:raise ValueError('Repeated or invalid original source cell')
    if list(map(F,row['source_radius_exact']))!=nodes[i:i+2] or not row['whole_original_source_cell_and_all_angles_covered']:raise ValueError('Cell does not cover its true original interval')
    parts=row['pieces'];piecesU=max(F(v['metric_upper_exact']) for v in parts)
    if piecesU!=F(row['metric_upper_exact']):raise ValueError('Cell maximum differs from actual pieces')
    branches=[tuple(map(F,v['radius_branch_exact'])) for v in parts]
    if any(left<nodes[i] or right>nodes[i+1] for left,right in branches) or intervals_union(branches)!=[nodes[i:i+2]]:raise ValueError('Physical source-cell subdivision has a gap')
    for piece in parts:
     zlo,zhi=map(F,piece['unit_interval_exact'])
     if zlo>=zhi:raise ValueError('Invalid actual W intersection')
    covered[i]={'metric_upper_exact':str(piecesU),'receipt':path.name};ids.append(i);local=max(local,piecesU);piece_count+=len(parts)
  if ids!=d['covered_source_spans'] or local!=F(d['metric_upper_exact']):raise ValueError('Final receipt does not match its actual completed row stream')
  U=max(U,local);sources.append({'report':path.name,'sha256':sha(path),'row_stream_sha256':sha(rowpath),'source_ranges':integer_ranges(ids),'metric_upper_exact':str(local)})
 missing=sorted(set(range(18552))-set(covered))
 if missing and not a.allow_partial:raise ValueError('Original finite tail is not completely covered')
 inner=json.loads(a.inner_collar.read_text());cuff=F.from_float(meta['parameters']['rCuff'])
 if inner['inputs']!=expected or F(inner['finite_inner_exact'])!=nodes[0] or F(inner['true_cuff_exact'])!=cuff:raise ValueError('Inner collar is not the same original field and exact domain')
 if not inner['whole_true_inner_collar_and_all_angles_covered'] or inner['all_original_raw_blobs_and_exact_radial_nodes_checked']!=expected_raw:raise ValueError('Incomplete original inner-collar coverage')
 collar=inner['certificate'];collarU=max(F(v['metric_upper_exact']) for v in collar['pieces'])
 if collarU!=F(inner['metric_upper_exact']) or collarU!=F(collar['metric_upper_exact']):raise ValueError('Inner-collar maximum differs')
 if intervals_union([tuple(map(F,v['radius_branch_exact'])) for v in collar['pieces']])!=[[cuff,nodes[0]]]:raise ValueError('Inner-collar physical coverage has a gap')
 total=max(U,collarU);B=F(1,500000000)
 out={'schema':'2ecf-M12-exact-original-tail-cell-and-inner-collar-composition-v1','script_sha256':sha(__file__),'inputs':expected,
  'manifest_sha256':sha(manifest),'finite_source_cells_covered':len(covered),'finite_source_ranges':integer_ranges(covered),'missing_source_ranges':integer_ranges(missing),
  'all_original_finite_source_cells_covered':not missing,'actual_finite_W_intersection_pieces':piece_count,'finite_metric_upper_exact':str(U),
  'inner_collar_report_sha256':sha(a.inner_collar),'inner_collar_metric_upper_exact':str(collarU),
  'true_whole_tail_covered':not missing,'tail_metric_upper_exact':str(total),'tail_metric_upper_display':float(total),
  'below_original_solver_tolerance':total<=B,'whole_surface_claim':False,'prefix_and_fixed_caps_require_separate_composition':True,
  'reports':sources,'same_actual_field_original_source_and_g':True,'all_angles_and_original_phase_orbit':True}
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({'output':str(a.out),'sha256':sha(a.out),'covered':len(covered),'missing':len(missing),'upper':float(total),'complete':not missing}),flush=True)
if __name__=='__main__':main()
