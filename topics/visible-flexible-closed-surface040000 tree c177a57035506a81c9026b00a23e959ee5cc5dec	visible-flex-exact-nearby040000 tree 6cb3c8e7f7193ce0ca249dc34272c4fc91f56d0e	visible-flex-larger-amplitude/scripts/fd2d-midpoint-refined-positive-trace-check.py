#!/usr/bin/env python3
"""R163: one bounded shared-point refinement check; no whole F/J or BVP."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import importlib.util
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_midpoint_refined_positive_trace import (
    MidpointRefinedPositiveTraceDAE, checkpoint_arrays, same_bits)
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','input','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--split-cells',type=int,nargs='+',default=[63,65,71,118,119,121])
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new complete output stem')
    started=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-same-g-midpoint-P1-refinement-check-v1',
        source=identity(__file__),input=identity(args.input),candidate=identity(args.candidate),
        mesh_helper=identity(here/'fd2d_gc_midpoint_refined_positive_trace.py'),
        original_provider=identity(here/'fd2d_gc_raw_bump_positive_trace.py'),
        original_native_reader=identity(here/'fd2d_gc_positive_trace_native_field_v2.py'),
        reused_local_function_reader=identity(here/'fd2d-nested-angular-positive-trace-check.py'),
        completed=False,whole_finite_objective_evaluated=False,Jacobian_assembled=False,
        nonlinear_BVP_performed=False,body_performed=False,continuous_geometry_claim=False)
    def save():
        report.update(seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        old=load_npz(args.input)
        packet=json.loads(args.radius_packet.read_text())
        if not packet['passed'] or packet['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Wrong physical-radius proof packet')
        common=dict(max_step=.04,gap=.9,reference_inlet=args.reference_inlet,
            reference_cache=args.reference_cache,base_lower_bound='4/5',
            base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=packet['candidate_sha256']),
            radius_floor=.1,minimum_active_n=.05)
        low=PositiveTraceRawBumpDAE(args.candidate,modes=int(old['modes']),**common)
        high=MidpointRefinedPositiveTraceDAE(args.candidate,saved_field=old,
            split_cells=args.split_cells,**common)
        if not same_bits(low.x,old['mesh']):
            raise ValueError('This diagnostic is bound to the actual original 19 mesh')
        old_vector=np.r_[old['corrections'].ravel(),old['parameters']]
        vector,definition=high.inject_saved_field(canonicalize_redundant=True)
        definition['input']=report['input']
        report['refinement']=definition
        arrays=checkpoint_arrays(high,vector,report['candidate']['sha256'],refinement_definition=definition)
        field_path=stem.with_name(stem.name+'-field.npz')
        report['new_field']=save_npz(field_path,**arrays)
        report['old_layout']=low.parameter_layout()
        report['new_layout']=high.parameter_layout()
        report['new_interior_rows_definition']=json.loads(str(arrays['finite_interior_rows_definition']))

        # Reuse the existing closed local whole-function evaluator. It only
        # evaluates actual fields at the explicitly common finite points.
        path=here/'fd2d-nested-angular-positive-trace-check.py'
        spec=importlib.util.spec_from_file_location('fd2d_r158_local_reader',path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        points=[0.,.1,.4,.57,low.trace_cut]
        for j in sorted(set(args.split_cells)):
            left,right=old['mesh'][j:j+2]
            points.extend(left+(right-left)*np.array([0.,.25,.5,.75,1.]))
        points=np.unique(points);angles=2*np.pi*np.arange(64)/64
        lhs=module.local_complete_fields(low,old_vector,points,angles)
        rhs=module.local_complete_fields(high,vector,points,angles)
        names=('lifting','lifting_angular','actual','actual_angular','a','a_s','K','U','U_s','U_xi')
        errors={name:float(np.max(np.abs(lhs[name]-rhs[name]))) for name in names}
        scales={name:float(np.max(np.abs(lhs[name]-rhs[name])/(1+np.abs(lhs[name])))) for name in names}
        report['common_function_check']=dict(radial_points=points.tolist(),angle_count=len(angles),
            maximum_absolute_errors=errors,maximum_scaled_errors=scales,
            raw_gauge_functions_may_differ_but_complete_fields_compared=True,
            real_arithmetic_identity_is_a_proof_not_inferred_from_these_samples=True)

        # Existing native reader must accept the explicit new mesh and
        # recomputed inactive-hat metadata without a new field schema.
        native_args=dict(reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
                         geometry=low.geometry)
        native_old=PositiveTraceNativeField(args.input,args.candidate,**native_args)
        native_new=PositiveTraceNativeField(field_path,args.candidate,**native_args)
        samples=np.array([.1,.4,
            .25*old['mesh'][63]+.75*old['mesh'][64],
            .75*old['mesh'][65]+.25*old['mesh'][66],
            .5*(old['mesh'][71]+old['mesh'][72]),
            .5*(old['mesh'][118]+old['mesh'][119]),
            .5*(old['mesh'][119]+old['mesh'][120]),low.trace_cut])
        xx,xi=np.meshgrid(samples,2*np.pi*np.arange(16)/16,indexing='ij')
        left=native_old.evaluate_angular_native(xx,xi)
        right=native_new.evaluate_angular_native(xx,xi)
        angular_names=[n+s for n in ('n','m','l') for s in ('','_xi','_xixi')]
        native_errors={name:float(np.max(np.abs(left[name]-right[name]))) for name in angular_names}
        native_scaled={name:float(np.max(np.abs(left[name]-right[name])/(1+np.abs(left[name])))) for name in angular_names}
        # Two interior points: real one-sided radial and mixed jets, with
        # the exact cut deliberately excluded from this unnecessary query.
        sx=np.array([samples[3],samples[6]])[:,None]
        su=(2*np.pi*np.arange(8)/8)[None,:]
        ljet=native_old.evaluate_native(sx,su);rjet=native_new.evaluate_native(sx,su)
        for name in [n+s for n in ('n','m','l') for s in ('_x','_x_xi')]:
            native_errors[name]=float(np.max(np.abs(ljet[name]-rjet[name])))
            native_scaled[name]=float(np.max(np.abs(ljet[name]-rjet[name])/(1+np.abs(ljet[name]))))
        report['original_native_reader_check']=dict(new_schema_required=False,
            same_representation_kind=native_old.representation_kind==native_new.representation_kind,
            angular_point_count=int(xx.size),radial_mixed_point_count=int(np.broadcast(sx,su).size),
            maximum_absolute_errors=native_errors,maximum_scaled_errors=native_scaled,
            exact_cut_radial_derivative_not_requested=True)
        report['physical_parameter_bytes_unchanged']=same_bits(arrays['parameters'],old['parameters'])
        report['old_mesh_bytes_preserved']=same_bits(high.x[np.array(definition['old_node_to_new_node'])],old['mesh'])
        report['input_unchanged']=identity(args.input)['sha256']==report['input']['sha256']
        report['completed']=(report['input_unchanged'] and report['physical_parameter_bytes_unchanged']
            and report['old_mesh_bytes_preserved'] and max(scales.values())<1e-9 and max(native_scaled.values())<1e-9)
        save()
        print(json.dumps(dict(completed=report['completed'],field=report['new_field'],
            old_nodes=low.N,new_nodes=high.N,physical_parameter_count=high.parameter_count,
            max_common_scaled_error=max(scales.values()),max_native_scaled_error=max(native_scaled.values()),
            old_equations=low.residual_size,new_equations=high.residual_size,
            mapped_interior_cells=report['new_interior_rows_definition']['cells'],
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)
        if not report['completed']:raise SystemExit(1)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();raise


if __name__=='__main__':main()
