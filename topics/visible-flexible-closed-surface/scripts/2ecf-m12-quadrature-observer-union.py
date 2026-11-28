#!/usr/bin/env python3
"""True same-field before/after union for changing M12 radial quadrature.

The full current G+2 observer and every inherited independent point are
retained. Extra points are streamed with both the actual warm input field
and actual returned field; the zero-source before field is never mixed with
a nonzero warm field. No union quadrature energy or continuous bound is claimed.
"""
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
CACHE_SHA='b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745'
BASIS_SHA='34fb3936a57bef17ceb3c326bdfad885fe7372366e373030ec7a83a4202f8814'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','grid','field','initial-field','result','query-report','query-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--block',type=int,default=24);a=ap.parse_args();began=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh actual union observation required')
 grid=json.loads(a.grid.read_text());result=json.loads(a.result.read_text());comp=grid['comparison_observer']
 for k,p in [('field_sha256',a.field),('actual_initial_field_sha256',a.initial_field),('grid_sha256',a.grid),('query_report_sha256',a.query_report),('query_cache_sha256',a.query_cache)]:
  if result[k]!=sha(p):raise ValueError('Changed actual before/after binding '+k)
 for k in ('all_old_nodes_contained_in_union','all_unchanged_element_nodes_retained_exactly','all_ancestor_observers_contained_in_union'):
  if comp.get(k) is not True:raise ValueError('Missing actual observer superset provenance '+k)
 N=comp['angular_nodes'];current_gauss=comp.get('current_gauss',comp['old_gauss'])
 if N!=2*grid['angular'] or current_gauss!=grid['gauss']+2:raise ValueError('Current independent quadrature identity changed')
 if any(N%n for n in comp.get('ancestor_angular_nodes',[])):raise ValueError('An inherited angle set is lost')
 z=np.asarray(comp['missing_old_unit_nodes'],dtype=float)
 if len(comp['missing_old_observer_origins'])!=len(z):raise ValueError('Missing inherited point origins')
 core=load('true_union_original_whole',a.scripts/'6a65-m12-entire-half-cartesian-bvp.py');joint=load('true_union_original_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py');bg=load('true_union_original_background',a.scripts/'6a65-m12-original-tail-background.py')
 cp=HERE/'2ecf-m12-h2-cached-direct-lm-v2.py';bp=HERE/'2ecf-m12-h2-c2-direct-lm.py'
 if sha(cp)!=CACHE_SHA or sha(bp)!=BASIS_SHA:raise ValueError('Tested exact-value or C2 basis adapter changed')
 cached=[];load('true_union_cache',cp).cache_tail_apply(core.TailQueries,cached)
 a.background_tolerance=grid['background_tolerance'];_,mp,bridge,_,_,chart=core.definition(a,joint,bg)
 for k,p in [('data_sha256',a.data),('common_meta_sha256',mp),('bridge_sha256',bridge),('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
  if grid[k]!=sha(p):raise ValueError('Changed original source/metric '+k)
 tail=core.TailQueries(a.query_report,a.query_cache)
 if tail.record['query_file_sha256']!=grid['query_file_sha256']:raise ValueError('Actual source query recipe changed')
 src=joint.CommonCutSource(a.data,mp,bridge,a.query_report,a.query_cache);_,c=joint.ad.exact_section(a.data,core.Q(0));central=joint.ad.NativeCurve(c,512,32)
 position=core.WholePosition(src,central,chart,tail,joint);mesh=np.asarray(grid['unit_mesh'])
 basis=(load('true_union_C2_basis',bp).checked_basis(core.basis_for,joint,mesh,grid['order'],chart,grid['unit_knots']) if 'unit_knots' in grid else core.basis_for(joint,mesh,grid['order'],chart))
 def field(path):
  with np.load(path,allow_pickle=False) as f:
   coeff=f['coefficients'].copy()
   for k,v in [('unit_knots',basis.knots),('planar_modes',basis.pm),('vertical_modes',basis.zm)]:
    if not np.array_equal(f[k],v):raise ValueError('Actual field basis mismatch '+k)
  if coeff.shape!=(basis.nb,basis.na):raise ValueError('Incomplete actual correction')
  return coeff
 initial,actual=field(a.initial_field),field(a.field)
 def update(best,stat,start):
  stat=dict(stat);stat.pop('weighted_energy',None);i=start+stat['peak_radial_index'];stat['peak_radial_index']=i
  stat['peak_material_q']=float(z[i]*chart.total);stat['original_observer_origins']=comp['missing_old_observer_origins'][i]
  if best is None:return stat
  if stat['metric_peak']>best['metric_peak']:
   kappa=max(best['curvature_peak'],stat['curvature_peak']);support=min(best['support_lower'],stat['support_lower']);best=stat;best['curvature_peak']=kappa;best['support_lower']=support
  else:best['curvature_peak']=max(best['curvature_peak'],stat['curvature_peak']);best['support_lower']=min(best['support_lower'],stat['support_lower'])
  return best
 before=after=None
 for sl in joint.stream.chunks(len(z),a.block):
  p,b=position(z[sl],N);B=basis.matrices(z[sl]);weights=np.ones(len(z[sl]))
  before=update(before,joint.bvp.statistics(p+joint.stream.packet(basis,B,initial,N),b,weights),sl.start)
  after=update(after,joint.bvp.statistics(p+joint.stream.packet(basis,B,actual,N),b,weights),sl.start)
 def union(main,extra):
  if extra is None:return {k:main[k] for k in ('metric_peak','curvature_peak','support_lower')}
  return {'metric_peak':max(main['metric_peak'],extra['metric_peak']),'curvature_peak':max(main['curvature_peak'],extra['curvature_peak']),'support_lower':min(main['support_lower'],extra['support_lower'])}
 report={'schema':'2ecf-M12-true-field-quadrature-observer-union-v1','script_sha256':sha(__file__),'field_sha256':sha(a.field),'actual_initial_field_sha256':sha(a.initial_field),'grid_sha256':sha(a.grid),'solver_result_sha256':sha(a.result),'query_report_sha256':sha(a.query_report),'query_cache_sha256':sha(a.query_cache),
  'current_independent_gauss':current_gauss,'ancestor_gauss_orders':comp.get('ancestor_gauss_orders',[comp['old_gauss']]),'angular_nodes':N,'missing_old_radial_points':len(z),'current_radial_points':comp['new_radial_nodes'],'total_union_radial_points':len(z)+comp['new_radial_nodes'],
  'old_missing_points_actual_initial_before':before,'old_missing_points_actual_after':after,'union_before':union(result['independent_observer_before'],before),'union_after':union(result['independent_observer_after'],after),
  'all_recorded_ancestor_observers_retained':True,'before_is_actual_initial_field_at_every_point':True,'after_is_actual_saved_field_at_every_point':True,'same_original_source_and_g':True,'all_actual_physical_s_six_jets_used':True,'ancestor_grid_sha256s':comp['ancestor_grid_sha256s'],
  'no_union_quadrature_energy_claim':True,'continuous_metric_certificate':False,'exact_isometry_proved':False,'exact_value_angular_cache':cached,'seconds':time.monotonic()-began}
 a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('exact_value_angular_cache','old_missing_points_actual_initial_before','old_missing_points_actual_after')}),flush=True)
if __name__=='__main__':main()
