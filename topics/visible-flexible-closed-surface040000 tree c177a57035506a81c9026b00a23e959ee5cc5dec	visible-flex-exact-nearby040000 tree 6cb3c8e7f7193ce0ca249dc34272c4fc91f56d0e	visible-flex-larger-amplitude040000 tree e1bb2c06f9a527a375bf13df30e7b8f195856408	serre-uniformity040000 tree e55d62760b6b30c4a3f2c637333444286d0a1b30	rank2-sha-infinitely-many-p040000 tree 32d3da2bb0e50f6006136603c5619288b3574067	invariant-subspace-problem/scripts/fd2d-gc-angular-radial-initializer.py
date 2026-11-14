#!/usr/bin/env python3
"""Explicit R158 angular injection followed by R163 saved P1 subdivision.

This creates a new finite initializer, not a nonlinear solution.  The old
physical parameters/full functions are preserved.  Angular coefficients
are zero-injected exactly; saved radial coefficients have the separately
reported binary64 interpolation/gauge error.  No whole F/J is evaluated.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,datetime,json,time,resource,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_nested_angular_positive_trace import (
    FixedTailDegreePositiveTraceDAE,checkpoint_arrays as angular_arrays)
from fd2d_gc_midpoint_refined_positive_trace_v3 import (
    create_midpoint_refined_problem,checkpoint_arrays as radial_arrays)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path)
    ap.add_argument('--modes',type=int,default=31)
    ap.add_argument('--split-cells',type=lambda s:tuple(map(int,s.split(','))),
                    default=(63,65,71,118,119,121))
    args=ap.parse_args();stem=args.out_prefix;start=time.monotonic()
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a unique initializer stem')
    stem.parent.mkdir(parents=True,exist_ok=True)
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-explicit-angular-then-radial-injection-v1',
        source=identity(__file__),warm_input=identity(args.warm_start),candidate=identity(args.candidate),
        providers={n:identity(here/n) for n in (
            'fd2d_gc_nested_angular_positive_trace.py',
            'fd2d_gc_midpoint_refined_positive_trace.py',
            'fd2d_gc_midpoint_refined_positive_trace_v3.py',
            'fd2d_gc_raw_bump_positive_trace.py')},
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        nonlinear_solve_performed=False,whole_residual_evaluated=False,
        old_finite_residual_preservation_claimed=False,completed=False)
    def save():
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.warm_start);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Base radius packet does not bind this physical input')
        common=dict(reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            reference_rim_fraction=.12,max_step=.04,gap=.9,mesh_relative_tolerance=1e-12,
            minimum_active_n=json.loads(str(a['gauss_l_definition']))['selected_finite_evaluation_floor'],
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),
            candidate_sha256=proof['candidate_sha256']),radius_floor=.1)
        old_k=int(a['modes']);nt=int(a['tail_parameter_count']) if 'tail_parameter_count' in a else old_k+1
        angular=FixedTailDegreePositiveTraceDAE(args.candidate,modes=args.modes,
            tail_parameter_count=nt,**common)
        az,embedding=angular.inject_saved_field(a)
        aa=angular_arrays(angular,az,report['candidate']['sha256'],embedding_definition=embedding)
        for key in ('finite_radial_scheme','finite_interior_rows_definition'):
            if key in a:aa[key]=np.array(a[key],copy=True)
        report['angular_field']=save_npz(stem.with_name(stem.name+'-angular.npz'),**aa)
        report['angular_embedding']=embedding
        problem=create_midpoint_refined_problem(args.candidate,saved_field=aa,
            split_cells=args.split_cells,**common)
        z,refinement=problem.inject_saved_field(canonicalize_redundant=True)
        arrays=radial_arrays(problem,z,report['candidate']['sha256'],refinement_definition=refinement)
        if 'finite_radial_scheme' in a:arrays['finite_radial_scheme']=np.array(a['finite_radial_scheme'],copy=True)
        report['field']=save_npz(stem.with_name(stem.name+'-field.npz'),**arrays)
        _,p=problem.unpack(z);central=problem.seed+problem.core_basis@p[:problem.K]
        report.update(radial_refinement=refinement,layout=problem.parameter_layout(),
            old_modes=old_k,new_modes=problem.K,tail_parameter_count=nt,
            old_node_count=len(a['mesh']),new_node_count=problem.N,
            selected_interior_definition=json.loads(str(arrays['finite_interior_rows_definition'])),
            finite_central_minimum=float(central.min()),finite_central_maximum=float(central.max()),
            original_strict_search_domain=problem.parameter_domain(z,1/.136,.1),
            completed=True)
        save();print(json.dumps(dict(event='initializer_completed',field=report['field'],
            old_modes=old_k,new_modes=problem.K,old_nodes=len(a['mesh']),new_nodes=problem.N,
            central_minimum=report['finite_central_minimum'],strict_domain=report['original_strict_search_domain'],
            selected_cells=report['selected_interior_definition']['cells'])),flush=True)
        return 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();raise


if __name__=='__main__':raise SystemExit(main())
