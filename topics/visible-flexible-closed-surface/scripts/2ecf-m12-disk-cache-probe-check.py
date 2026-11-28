#!/usr/bin/env python3
"""Actual original-source checks for angle-group cache eviction and passive peaks."""
import argparse,hashlib,importlib.util,json,shutil,tempfile,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','grid','field','result','query-report','query-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();began=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh actual-source check required')
 grid=json.loads(a.grid.read_text());result=json.loads(a.result.read_text())
 for k,p in [('field_sha256',a.field),('grid_sha256',a.grid),('query_report_sha256',a.query_report),('query_cache_sha256',a.query_cache)]:
  if result[k]!=sha(p):raise ValueError('Actual field/source identity changed '+k)
 core=load('check_original_whole',a.scripts/'6a65-m12-entire-half-cartesian-warm-refinement.py')
 joint=load('check_original_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py')
 bg=load('check_original_background',a.scripts/'6a65-m12-original-tail-background.py')
 entry=load('check_new_cache_probe',HERE/'2ecf-m12-h2-disk-normal-cached-lm.py');trig=[];entry.cache_tail_apply(core.TailQueries,trig)
 a.background_tolerance=grid['background_tolerance'];_,mp,bp,_,_,chart=core.definition(a,joint,bg)
 tail=core.TailQueries(a.query_report,a.query_cache);src=joint.CommonCutSource(a.data,mp,bp,a.query_report,a.query_cache)
 _,c=joint.ad.exact_section(a.data,core.Q(0));central=joint.ad.NativeCurve(c,512,32)
 original=core.WholePosition(src,central,chart,tail,joint)
 root=Path(tempfile.mkdtemp(prefix='check-one-angle-cache-',dir=a.out.parent));records=[]
 binding={k:sha(getattr(a,k.replace('-','_'))) for k in ('grid','data','query-report','query-cache')}
 Cached=entry.cache_fixed_packets(core.WholePosition,root,binding,records);cached=Cached(src,central,chart,tail,joint)
 z=np.array([0.10051113271659154,0.8580820609795288,0.999998533768839]);checks=[]
 for N in [384,768,384]:
  expected,bb=original(z,N);actual,target=cached(z,N)
  equal=expected.tobytes()==actual.tobytes() and bb.tobytes()==target.tobytes()
  actual.fill(123);target.fill(-7);restored,restored_bb=cached(z,N)
  preserved=expected.tobytes()==restored.tobytes() and bb.tobytes()==restored_bb.tobytes()
  if not equal or not preserved:raise ArithmeticError('Actual original source cache changed')
  checks.append({'N':N,'miss_or_return_bytes_equal':equal,'hit_after_inplace_mutation_bytes_equal':preserved,
     'live_files':len(list(root.rglob('*.npz'))),'actual_evicted_blocks':records[0]['evicted_blocks_when_angle_count_changed']})
 helper=load('check_C2_basis',HERE/'2ecf-m12-h2-c2-direct-lm.py')
 basis=helper.checked_basis(core.basis_for,joint,np.asarray(grid['unit_mesh']),grid['order'],chart,grid['unit_knots'])
 with np.load(a.field,allow_pickle=False) as f:coeff=f['coefficients'].copy()
 before=joint.stream.observe(basis,z,np.ones(3),cached,coeff,384,2)
 observations=[];entry.attach_radial_peak_probe(joint.stream,grid,observations)
 after=joint.stream.observe(basis,z,np.ones(3),cached,coeff,384,2)
 if before!=after or observations[-1]['metric_peak']!=after['metric_peak']:raise ArithmeticError('Passive peak probe changed original finite statistics')
 rec={'schema':'2ecf-M12-actual-angle-cache-eviction-passive-radial-probe-check-v1','script_sha256':sha(__file__),
   'tested_entry_sha256':sha(entry.__file__),'grid_sha256':sha(a.grid),'field_sha256':sha(a.field),
   'actual_original_source_identity':src.source_identity,'actual_radial_points':z.tolist(),'cache_checks':checks,
   'passive_observer_exact_original_statistics':before==after,'observed_physical_spans':observations[-1]['physical_spans_observed'],
   'finite_statistics':after,'cache_records':records,'all_checks_passed':True,'actual_exit':0,
   'new_nonlinear_field_or_full_mesh_claimed':False,'seconds':time.monotonic()-began}
 shutil.rmtree(root);rec['actual_private_cache_removed']=True
 a.out.write_text(json.dumps(rec,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in rec.items() if k not in ('actual_original_source_identity','cache_records')}),flush=True)
if __name__=='__main__':main()
