#!/usr/bin/env python3
"""Retain the old independent observer when only one radial element changes.

The refined Gauss set and the old points missing from that set form a true
superset of the old observer. Only the few missing points are evaluated
again. The actual saved h-field, original g, exact query cache and complete
physical jets are used. No union quadrature-energy claim is made.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('scripts','data','grid','query-report','query-cache','field','result','out'):
        ap.add_argument('--'+n,type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh observer-union report required')
    began=time.monotonic();grid=json.loads(args.grid.read_text());result=json.loads(args.result.read_text())
    for key,path in [('grid_sha256',args.grid),('field_sha256',args.field),('query_report_sha256',args.query_report),('query_cache_sha256',args.query_cache)]:
        if result[key]!=sha(path):raise ValueError('Saved h-field identity mismatch '+key)
    comp=grid['comparison_observer']
    if not comp['all_old_nodes_contained_in_union'] or not comp['all_unchanged_element_nodes_retained_exactly']:
        raise ValueError('Old observer inclusion was not verified')
    whole=load('union_original_whole',args.scripts/'6a65-m12-entire-half-cartesian-bvp.py')
    joint=load('union_original_joint',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    bg=load('union_original_background',args.scripts/'6a65-m12-original-tail-background.py')
    args.background_tolerance=grid['background_tolerance']
    notes,meta_path,bridge_path,meta,native,chart=whole.definition(args,joint,bg)
    for key,path in [('data_sha256',args.data),('common_meta_sha256',meta_path),('bridge_sha256',bridge_path),
                     ('joint_source_sha256',Path(joint.__file__)),('background_source_sha256',Path(bg.__file__))]:
        if grid[key]!=sha(path):raise ValueError('Changed original observer definition '+key)
    tail=whole.TailQueries(args.query_report,args.query_cache)
    if tail.record['query_file_sha256']!=grid['query_file_sha256']:raise ValueError('Refined exact-radius cache not locked to grid')
    src=joint.CommonCutSource(args.data,meta_path,bridge_path,args.query_report,args.query_cache)
    unused,c=joint.ad.exact_section(args.data,Q(0));central=joint.ad.NativeCurve(c,512,32)
    position=whole.WholePosition(src,central,chart,tail,joint)
    basis=whole.basis_for(joint,np.asarray(grid['unit_mesh']),grid['order'],chart)
    with np.load(args.field,allow_pickle=False) as f:
        coeff=f['coefficients'].copy()
        if not np.array_equal(f['unit_knots'],basis.knots) or not np.array_equal(f['planar_modes'],basis.pm) or not np.array_equal(f['vertical_modes'],basis.zm):
            raise ValueError('Saved h-field basis mismatch')
    if coeff.shape!=(basis.nb,basis.na):raise ValueError('Incomplete actual h-field')
    z=np.asarray(comp['missing_old_unit_nodes']);N=comp['angular_nodes']
    if N!=2*grid['angular'] or comp['old_gauss']!=grid['gauss']+2:
        raise ValueError('Independent angle/quadrature identity changed')
    if len(z):
        p,bb=position(z,N)
        before=joint.bvp.statistics(p,bb,np.ones(len(z)))
        p+=joint.stream.packet(basis,basis.matrices(z),coeff,N)
        after=joint.bvp.statistics(p,bb,np.ones(len(z)))
        for stat in (before,after):
            stat.pop('weighted_energy',None)
            stat['peak_common_q']=float(z[stat['peak_radial_index']]*chart.total)
            stat['old_radial_index']=comp['missing_old_radial_indices'][stat['peak_radial_index']]
    else:
        before=after=None
    def union(main,extra):
        if extra is None:return {key:main[key] for key in ('metric_peak','curvature_peak','support_lower')}
        return {'metric_peak':max(main['metric_peak'],extra['metric_peak']),
                'curvature_peak':max(main['curvature_peak'],extra['curvature_peak']),
                'support_lower':min(main['support_lower'],extra['support_lower'])}
    report={'schema':'6a65-M12-local-h-old-independent-observer-union-v1','script_sha256':sha(__file__),
            'field_sha256':sha(args.field),'grid_sha256':sha(args.grid),'result_sha256':sha(args.result),
            'query_report_sha256':sha(args.query_report),'query_cache_sha256':sha(args.query_cache),
            'missing_old_radial_points':len(z),'angular_nodes':N,
            'old_missing_points_before':before,'old_missing_points_after':after,
            'union_before':union(result['independent_observer_before'],before),
            'union_after':union(result['independent_observer_after'],after),
            'union_contains_full_old_independent_observer':True,
            'all_old_knots_retained_and_same_original_g':True,
            'no_union_quadrature_energy_claim':True,'continuous_metric_certificate':False,
            'exact_isometry_proved':False,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()

