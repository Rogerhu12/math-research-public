#!/usr/bin/env python3
"""Increase actual whole-half quadrature while retaining every old source query.

The physical mesh, full C2 knot multiset, original g and angular space stay
fixed. Current and every inherited independent radial observer form an exact
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
 for k in ('scripts','data','old-grid','out'):ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--gauss',type=int,default=12);a=ap.parse_args();began=time.monotonic()
 old=json.loads(a.old_grid.read_text());oq=Path(str(a.old_grid)+'.queries.json');query_path=Path(str(a.out)+'.queries.json')
 if a.out.exists() or query_path.exists():raise FileExistsError('Fresh quadrature-refinement outputs required')
 if a.gauss<=old['gauss']:raise ValueError('The actual quadrature order must increase')
 if sha(oq)!=old['query_file_sha256']:raise ValueError('Old exact source query identity changed')
 core=load('new_quadrature_same_whole',a.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
 joint=load('new_quadrature_same_joint',a.scripts/'6a65-m12-global-common-cut-position-recovered.py')
 bg=load('new_quadrature_same_background',a.scripts/'6a65-m12-original-tail-background.py')
 a.background_tolerance=old['background_tolerance'];_,mp,bp,_,_,chart=core.definition(a,joint,bg)
 for k,p in [('data_sha256',a.data),('common_meta_sha256',mp),('bridge_sha256',bp),('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
  if old[k]!=sha(p):raise ValueError('Changed original geometry '+k)
 mesh=np.asarray(old['unit_mesh']);old_z,_=core.quadrature(mesh,old['gauss']+2,chart)
 train_z,_=core.quadrature(mesh,a.gauss,chart);new_z,_=core.quadrature(mesh,a.gauss+2,chart)
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
 query={'schema':'2ecf-original-M12-quadrature-refined-union-radii-v1','radii':sorted(radii,key=Q),'all_old_exact_radii_retained':True,'parent_query_file_sha256':sha(oq)}
 query_path.write_text(json.dumps(query,indent=2)+'\n')
 out=dict(old);out.update(schema='2ecf-original-M12-same-space-quadrature-refinement-v1',script_sha256=sha(__file__),parent_grid_sha256=sha(a.old_grid),gauss=a.gauss,query_file_sha256=sha(query_path))
 comp=dict(prev);comp.update(old_gauss=old['gauss']+2,current_gauss=a.gauss+2,angular_nodes=2*old['angular'],old_radial_nodes=len(old_z),new_radial_nodes=len(new_z),
  missing_old_unit_nodes=missing,missing_old_radial_indices=[origins[z][0]['origin_radial_index'] for z in missing],missing_old_observer_origins=[origins[z] for z in missing],
  all_old_nodes_contained_in_union=True,all_unchanged_element_nodes_retained_exactly=True,all_ancestor_observers_contained_in_union=True,
  ancestor_grid_sha256s=sorted(set(prev.get('ancestor_grid_sha256s',[])+[sha(a.old_grid)])),
  ancestor_gauss_orders=sorted(set(prev.get('ancestor_gauss_orders',[])+[old['gauss']+2])),
  previous_current_points_now_missing=len(set(map(float,old_z))-new_values),inherited_missing_points_kept=len(prev.get('missing_old_unit_nodes',[])),
  same_physical_mesh_despite_different_quadrature_rules=True)
 out['comparison_observer']=comp
 out['quadrature_refinement']={'old_training_order':old['gauss'],'new_training_order':a.gauss,'old_independent_order':old['gauss']+2,'new_independent_order':a.gauss+2,
  'same_physical_mesh_full_knots_angular_space_and_original_g':True,'same_parameter_and_time_range':True,'all_old_source_queries_retained':True,'no_new_finite_space_columns':True,
  'true_current_and_ancestor_observer_union_required':True,'finite_space_or_exact_solution_convergence_not_claimed':True}
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
 print(json.dumps({'schema':out['schema'],'script_sha256':sha(__file__),'old_grid_sha256':sha(a.old_grid),'new_grid_sha256':sha(a.out),'query_file_sha256':sha(query_path),
  'old_source_queries':prior_count,'new_union_source_queries':len(radii),'new_distinct_source_queries':len(radii)-prior_count,
  'new_training_radial_nodes':len(train_z),'new_independent_radial_nodes':len(new_z),'old_and_ancestor_points_missing_from_new_rule':len(missing),
  'true_observer_union_radial_points':len(new_z)+len(missing),'same_original_g':True,'new_nonlinear_field_claimed':False,'seconds':time.monotonic()-began}),flush=True)
if __name__=='__main__':main()
