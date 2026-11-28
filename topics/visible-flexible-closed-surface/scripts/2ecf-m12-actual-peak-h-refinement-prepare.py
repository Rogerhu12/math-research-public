#!/usr/bin/env python3
"""Refine actual finite-peak physical spans and retain every ancestor query.

The original g, angular space and Gauss orders stay fixed. Actual selected
physical spans gain midpoint knots of explicitly declared multiplicity. Current and every inherited independent radial observer form an exact
binary64 point superset with the new independent rule. This prepares source
queries and provenance; it does not solve or observe a new field.
"""
import argparse,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','old-grid','old-result','old-field','out'):ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--prefix-elements',type=int,default=8);ap.add_argument('--tail-elements',type=int,default=8)
 ap.add_argument('--new-knot-multiplicity',type=int,default=3);a=ap.parse_args();began=time.monotonic()
 old=json.loads(a.old_grid.read_text());oq=Path(str(a.old_grid)+'.queries.json');query_path=Path(str(a.out)+'.queries.json')
 if a.out.exists() or query_path.exists():raise FileExistsError('Fresh quadrature-refinement outputs required')
 result=json.loads(a.old_result.read_text())
 for key,p in [('grid_sha256',a.old_grid),('field_sha256',a.old_field)]:
  if result[key]!=sha(p):raise ValueError('Actual diagnostic field identity changed '+key)
 if a.new_knot_multiplicity not in (1,2,3) or min(a.prefix_elements,a.tail_elements)<0 or a.prefix_elements+a.tail_elements<1:raise ValueError('Positive declared C2 radial refinement required')
 if max(a.prefix_elements,a.tail_elements)>24:raise ValueError('Only actually reported top24 region spans may be selected')
 probe=result['independent_radial_peak_diagnostics']['after']
 with np.load(a.old_field,allow_pickle=False) as saved:
  if hashlib.sha256(saved['coefficients'].tobytes()).hexdigest()!=probe['coefficient_bytes_sha256']:raise ValueError('Peak diagnostic is not the saved field')
 if not result['independent_radial_peak_diagnostics']['all_current_physical_spans_sampled']:raise ValueError('The current original observer must cover every old element')
 chosen=[]
 for region,count in [('prefix',a.prefix_elements),('tail',a.tail_elements)]:
  rows=probe['top_'+region+'_physical_spans']
  if len(rows)<count:raise ValueError('Too few actually reported '+region+' physical spans')
  chosen.extend(rows[:count])
 selected=sorted(set(row['basis_element'] for row in chosen))
 if len(selected)!=len(chosen):raise ValueError('Selected region lists overlap')
 if sha(oq)!=old['query_file_sha256']:raise ValueError('Old exact source query identity changed')
 core=load('new_quadrature_same_whole',a.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
 joint=load('new_quadrature_same_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py')
 bg=load('new_quadrature_same_background',a.scripts/'6a65-m12-original-tail-background.py')
 a.background_tolerance=old['background_tolerance'];_,mp,bp,_,_,chart=core.definition(a,joint,bg)
 for k,p in [('data_sha256',a.data),('common_meta_sha256',mp),('bridge_sha256',bp),('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
  if old[k]!=sha(p):raise ValueError('Changed original geometry '+k)
 old_mesh=np.asarray(old['unit_mesh']);old_z,_=core.quadrature(old_mesh,old['gauss']+2,chart)
 added=[]
 for row in chosen:
  i=row['basis_element']
  if row['unit_span']!=list(old_mesh[i:i+2]) or not old_mesh[i]<=row['unit_coordinate']<=old_mesh[i+1]:raise ValueError('Actual radial diagnostic span changed')
 for i in selected:
  lo,hi=old_mesh[i:i+2];mid=float(lo+(hi-lo)/2)
  if not lo<mid<hi:raise ArithmeticError('No representable physical midpoint')
  added.append(mid)
 mesh=np.sort(np.r_[old_mesh,added]);knots=sorted(old['unit_knots']+list(np.repeat(added,a.new_knot_multiplicity)))
 train_z,_=core.quadrature(mesh,old['gauss'],chart);new_z,_=core.quadrature(mesh,old['gauss']+2,chart)
 original_queries=json.loads(oq.read_text());radii=set(original_queries['radii']);prior_count=len(radii)
 for z in np.r_[train_z,new_z]:
  if np.longdouble(z)*chart.total>chart.S:radii.add(core.exact_key(chart.radius(z)[0]))
 prev=old.get('comparison_observer',{});origins={}
 for i,z in enumerate(old_z):origins.setdefault(float(z),[]).append({'origin_grid_sha256':sha(a.old_grid),'origin_radial_index':i,'origin_gauss':old['gauss']+2})
 for z,entries in zip(prev.get('missing_old_unit_nodes',[]),prev.get('missing_old_observer_origins',[])):
  origins.setdefault(float(z),[]).extend(entries)
 new_values=set(map(float,new_z));missing=sorted(set(origins)-new_values)
 if not set(map(float,old_z))<=new_values|set(missing):raise ArithmeticError('An actual old independent point was lost')
 if not set(map(float,prev.get('missing_old_unit_nodes',[])))<=new_values|set(missing):raise ArithmeticError('An inherited independent point was lost')
 for z in missing:
  if np.longdouble(z)*chart.total>chart.S and core.exact_key(chart.radius(z)[0]) not in radii:raise ValueError('An inherited actual source query is missing')
 query={'schema':'2ecf-original-M12-physical-h-refined-union-radii-v1','radii':sorted(radii,key=Q),'all_old_exact_radii_retained':True,'parent_query_file_sha256':sha(oq)}
 query_path.write_text(json.dumps(query,indent=2)+'\n')
 out=dict(old);out.update(schema='2ecf-original-M12-actual-peak-physical-h-refinement-v1',script_sha256=sha(__file__),parent_grid_sha256=sha(a.old_grid),unit_mesh=mesh.tolist(),unit_knots=knots,query_file_sha256=sha(query_path))
 comp=dict(prev);comp.update(old_gauss=old['gauss']+2,current_gauss=old['gauss']+2,angular_nodes=2*old['angular'],old_radial_nodes=len(old_z),new_radial_nodes=len(new_z),
  missing_old_unit_nodes=missing,missing_old_radial_indices=[origins[z][0]['origin_radial_index'] for z in missing],missing_old_observer_origins=[origins[z] for z in missing],
  all_old_nodes_contained_in_union=True,all_unchanged_element_nodes_retained_exactly=True,all_ancestor_observers_contained_in_union=True,
  ancestor_grid_sha256s=sorted(set(prev.get('ancestor_grid_sha256s',[])+[sha(a.old_grid)])),
  ancestor_gauss_orders=sorted(set(prev.get('ancestor_gauss_orders',[])+[old['gauss']+2])),
  previous_current_points_now_missing=len(set(map(float,old_z))-new_values),inherited_missing_points_kept=len(prev.get('missing_old_unit_nodes',[])),
  same_physical_mesh_despite_different_quadrature_rules=False)
 out['comparison_observer']=comp
 out['actual_peak_radial_refinement']={'actual_parent_field_sha256':sha(a.old_field),'actual_parent_result_sha256':sha(a.old_result),
  'parent_finite_independent_metric_peak':probe['metric_peak'],'selected_old_physical_elements':selected,'selected_actual_peak_rows':chosen,
  'inserted_unit_midpoints':added,'new_knots_multiplicity':a.new_knot_multiplicity,'old_elements':len(old_mesh)-1,'new_elements':len(mesh)-1,
  'old_radial_columns':len(old['unit_knots'])-12,'new_radial_columns':len(knots)-12,
  'same_original_g_parameters_time_angular_space_and_Gauss_orders':True,'all_old_knots_and_source_queries_retained':True,
  'finite_peak_selection_not_a_continuous_maximum_claim':True,'actual_exact_transfer_and_new_LM_not_yet_executed':True,
  'exact_source_radial_knot_coincidence_claimed':False,'true_current_and_ancestor_observer_union_required':True}
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'schema':out['schema'],'script_sha256':sha(__file__),'old_grid_sha256':sha(a.old_grid),'new_grid_sha256':sha(a.out),'query_file_sha256':sha(query_path),
  'old_source_queries':prior_count,'new_union_source_queries':len(radii),'new_distinct_source_queries':len(radii)-prior_count,
  'new_training_radial_nodes':len(train_z),'new_independent_radial_nodes':len(new_z),'old_and_ancestor_points_missing_from_new_rule':len(missing),
  'true_observer_union_radial_points':len(new_z)+len(missing),'old_elements':len(old_mesh)-1,'new_elements':len(mesh)-1,'old_radial_columns':len(old['unit_knots'])-12,'new_radial_columns':len(knots)-12,'same_original_g':True,'new_nonlinear_field_claimed':False,'seconds':time.monotonic()-began}),flush=True)
if __name__=='__main__':main()
