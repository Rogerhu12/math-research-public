#!/usr/bin/env python3
"""Read the one saved23b3 plateau-refined entity after report serialization failed.

The new archive is already the actual first-run injection. This checker
does not inject, subdivide, fit, project, or change a coefficient again.
It rebinds the saved mesh with the original R163 empty-split interface.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import (
    create_midpoint_refined_problem, same_bits, decoded, remap_old_cells)
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField
from fd2d_gc_physical_point_refinement import saved_gauss_plateau_points


EXPECTED_INPUT_SHA='a485ca86233a196223f16fc2f9c01b7cf3592ae5499d9a04fd94bd7f2511e81e'


def encode_scalar(value):
    if isinstance(value,np.generic):return value.item()
    raise TypeError('Unsupported report object: '+type(value).__name__)


def stripped(packet, excluded=()):
    out=copy.deepcopy(decoded(packet))
    for key in excluded:out.pop(key,None)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','input','prepared-field','failed-receipt','radius-packet',
                 'reference-inlet','reference-cache','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();here=Path(__file__).resolve().parent
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic()
    report=dict(schema='fd2d-explicit-physical-point-P1-saved-recovery-check-v1',
        source=identity(__file__),helper=identity(here/'fd2d_gc_physical_point_refinement.py'),
        first_checker=identity(here/'fd2d-physical-point-refinement-check.py'),
        first_process_receipt=identity(args.failed_receipt),input=identity(args.input),
        candidate=identity(args.candidate),new_field=identity(args.prepared_field),
        reused_R163_provider=identity(here/'fd2d_gc_midpoint_refined_positive_trace_v3.py'),
        native_reader=identity(here/'fd2d_gc_independent_tail_native_field.py'),
        completed=False,second_P1_injection_performed=False,whole_finite_objective_evaluated=False,
        Jacobian_assembled=False,nonlinear_BVP_performed=False,body_performed=False,
        continuous_certificate_claimed=False)
    def save():
        report.update(seconds=time.monotonic()-start,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        args.out.write_text(json.dumps(report,indent=2,allow_nan=False,default=encode_scalar)+'\n')
    save()
    try:
        if report['input']['sha256']!=EXPECTED_INPUT_SHA:
            raise ValueError('This bounded check uses only the stated actual23b3 input')
        receipt=json.loads(args.failed_receipt.read_text())
        if receipt['actual_exit_code']!=1 or receipt['saved_field']['sha256']!=report['new_field']['sha256']:
            raise ValueError('The saved prepared entity must be exactly the failed-report run output')
        old,arrays=load_npz(args.input),load_npz(args.prepared_field)
        definition=decoded(arrays['radial_refinement_definition'])
        if definition['input']['sha256']!=report['input']['sha256']:
            raise ValueError('The actual saved refinement has a different parent')
        report['refinement']=definition
        packet=json.loads(args.radius_packet.read_text())
        if not packet['passed'] or packet['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Wrong actual base-radius proof packet')
        problem=create_midpoint_refined_problem(args.candidate,saved_field=arrays,split_cells=(),
            max_step=.04,gap=.9,reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),
                candidate_sha256=packet['candidate_sha256']),radius_floor=.1)
        vector,restore_definition=problem.inject_saved_field()
        restored_y,restored_p=problem.unpack(vector)
        report['actual_saved_mesh_rebind']=dict(
            no_new_insertion=restore_definition['operation']=='restore_saved_mesh',
            raw_bytes_identical=same_bits(restored_y,arrays['corrections']),
            parameter_bytes_identical=same_bits(restored_p,arrays['parameters']),
            gauge_skipped=restore_definition['gauge_canonicalization_skipped_for_exact_restore'])
        requested=saved_gauss_plateau_points(old)
        old_ids=np.asarray(definition['old_node_to_new_node'],int)
        byte_keys=('parameters','profile_supports','fixed_base_T','base_kind','blend','tail_kind',
            'modes','tail_parameter_count','central_parameter_count','profile_count',
            'candidate_sha256','representation_kind','seed_weight_definition',
            'angular_atlas_definition','coast_reference_definition','reference_evaluation_definition',
            'nested_angular_definition','angular_embedding_definition')
        byte_checks={key:same_bits(old[key],arrays[key]) for key in byte_keys}
        packet_checks={key:stripped(old[key],[index])==stripped(arrays[key],[index])
            for key,index in (('gauss_l_definition','inactive_l_raw_nodes'),
                              ('positive_trace_definition','inactive_raw_trace_nodes'),
                              ('central_field_definition','fixed_node_indices'))}
        expected_l=np.array([j for j in range(1,problem.N-1)
            if problem.x[j-1]>=requested[0] and problem.x[j+1]<=requested[1]],int)
        terminal=decoded(old['positive_trace_definition'])
        expected_trace=np.array([j for j in range(1,problem.N-1)
            if problem.x[j-1]>=terminal['ramp_stop'] and problem.x[j+1]<=terminal['cut']],int)
        expected_pairs=np.array([(j*problem.q+k,j*problem.q+problem.d+k)
            for j in expected_trace for k in range(problem.e)],int).reshape(-1,2)
        old_interior=decoded(old['finite_interior_rows_definition'])
        new_interior=decoded(arrays['finite_interior_rows_definition'])
        mapped=remap_old_cells(definition,old_interior['cells'])
        mappings=[]
        for j in old_interior['cells']:
            row=definition['old_cell_to_new_cells'][j];children=row['new_cells']
            mappings.append(dict(old_cell=j,old_interval=row['old_interval'],new_cells=children,
                children_exactly_cover_same_binary_endpoints=bool(
                    problem.x[children[0]]==old['mesh'][j] and problem.x[children[-1]+1]==old['mesh'][j+1])))
        report['definition_checks']=dict(unchanged_original_array_bytes=byte_checks,
            unchanged_full_function_packets_except_mesh_indices=packet_checks,
            all_old_mesh_bytes_preserved=same_bits(problem.x[old_ids],old['mesh']),
            both_requested_coordinates_exactly_present=all(bool(np.any(problem.x==s)) for s in requested),
            requested_coordinates_hex=[s.hex() for s in requested],
            whole_hat_l_indices_correct=np.array_equal(expected_l,problem.inactive_l_raw_nodes),
            whole_hat_trace_indices_correct=np.array_equal(expected_trace,problem.inactive_trace_nodes),
            trace_gauge_pairs_correct=np.array_equal(expected_pairs,problem.trace_gauge_pairs),
            old_interior_cells=old_interior['cells'],new_interior_cells=new_interior['cells'],
            interior_cells_equal_all_children=(new_interior['cells']==mapped),
            physical_interval_mapping=mappings,
            old_node_count=len(old['mesh']),new_node_count=problem.N,
            tail_parameter_count=problem.tail_parameter_count,angular_modes=problem.K,
            parameter_count=problem.parameter_count,representation_kind=str(arrays['representation_kind']))
        # Save identity checks before the only repeated bounded native
        # evaluation, so no array/definition evidence can be lost again.
        save()
        native_args=dict(reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            geometry=problem.geometry)
        native_old=IndependentTailPositiveTraceNativeField(args.input,args.candidate,**native_args)
        native_new=IndependentTailPositiveTraceNativeField(args.prepared_field,args.candidate,**native_args)
        points=[]
        for row in definition['requested_point_rows']:
            s=row['point'];left,right=row['old_interval']
            points.extend([.5*(left+s),s,.5*(s+right)])
        points=np.array(sorted(set(points)),float);angles=2*np.pi*np.arange(8)/8
        xx,xi=np.meshgrid(points,angles,indexing='ij')
        lhs=native_old.evaluate_angular_native(xx,xi);rhs=native_new.evaluate_angular_native(xx,xi)
        names=[name+suffix for name in ('n','m','l') for suffix in ('','_xi','_xixi')]
        names += ['a','a_s','a_ss','u','U_x','U_xi','U_xixi']
        errors={name:float(np.max(np.abs(np.asarray(lhs[name])-np.asarray(rhs[name])))) for name in names}
        scaled={name:float(np.max(np.abs(np.asarray(lhs[name])-np.asarray(rhs[name]))/(1+np.abs(lhs[name])))) for name in names}
        report['bounded_common_native_angular_check']=dict(radial_points=points.tolist(),
            angle_definition='2*pi*j/8; identical coordinates for both actual fields',angle_count=len(angles),
            angular_point_count=int(xx.size),maximum_absolute_errors=errors,maximum_scaled_errors=scaled,
            source_native_reader_unmodified=True,no_new_field_schema=True,
            radial_jets_not_requested=True,continuous_certificate=False,
            real_arithmetic_identity_not_inferred_from_samples=True,
            active_n_sample_min=float(np.min(lhs['n'])))
        report['input_unchanged']=identity(args.input)['sha256']==report['input']['sha256']
        report['injected_entity_unchanged']=identity(args.prepared_field)['sha256']==report['new_field']['sha256']
        check=report['definition_checks']
        report['completed']=bool(report['input_unchanged'] and report['injected_entity_unchanged']
            and all(report['actual_saved_mesh_rebind'].values()) and all(byte_checks.values()) and all(packet_checks.values())
            and check['all_old_mesh_bytes_preserved'] and check['both_requested_coordinates_exactly_present']
            and check['whole_hat_l_indices_correct'] and check['whole_hat_trace_indices_correct']
            and check['trace_gauge_pairs_correct'] and check['interior_cells_equal_all_children']
            and all(row['children_exactly_cover_same_binary_endpoints'] for row in mappings)
            and len(definition['inserted_coordinates'])==2 and not definition['blocked_point_rows']
            and max(scaled.values())<1e-9)
        save()
        print(json.dumps(dict(completed=report['completed'],field=report['new_field'],
            old_nodes=len(old['mesh']),new_nodes=problem.N,new_inactive_l=problem.inactive_l_raw_nodes.tolist(),
            old_interior=old_interior['cells'],new_interior=new_interior['cells'],
            max_angular_scaled_error=max(scaled.values()),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'])),flush=True)
        if not report['completed']:raise SystemExit(1)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();raise


if __name__=='__main__':main()
