#!/usr/bin/env python3
"""One saved23b3 P1 injection at its two frozen Gauss plateau endpoints.

No midpoint is selected here. This is a small same-function comparison,
not a finite objective, Jacobian, BVP, body, or continuous certificate.
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
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import same_bits, decoded, remap_old_cells
from fd2d_gc_physical_point_refinement import (
    create_physical_point_refined_problem, checkpoint_arrays, saved_gauss_plateau_points)
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField


EXPECTED_INPUT_SHA='a485ca86233a196223f16fc2f9c01b7cf3592ae5499d9a04fd94bd7f2511e81e'


def stripped(packet, excluded=()):
    out=copy.deepcopy(decoded(packet))
    for key in excluded:out.pop(key,None)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','input','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix;here=Path(__file__).resolve().parent
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new output stem, preserving any previous actual attempt')
    start=time.monotonic()
    report=dict(schema='fd2d-explicit-physical-point-P1-refinement-check-v1',
        source=identity(__file__),helper=identity(here/'fd2d_gc_physical_point_refinement.py'),
        input=identity(args.input),candidate=identity(args.candidate),
        reused_R163_provider=identity(here/'fd2d_gc_midpoint_refined_positive_trace_v3.py'),
        native_reader=identity(here/'fd2d_gc_independent_tail_native_field.py'),
        completed=False,whole_finite_objective_evaluated=False,Jacobian_assembled=False,
        nonlinear_BVP_performed=False,body_performed=False,continuous_certificate_claimed=False)
    def save():
        report.update(seconds=time.monotonic()-start,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        if report['input']['sha256']!=EXPECTED_INPUT_SHA:
            raise ValueError('This one bounded check is bound to the immutable actual23b3 input')
        old=load_npz(args.input)
        packet=json.loads(args.radius_packet.read_text())
        if not packet['passed'] or packet['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Wrong actual base-radius proof packet')
        common=dict(max_step=.04,gap=.9,reference_inlet=args.reference_inlet,
            reference_cache=args.reference_cache,base_lower_bound='4/5',
            base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=packet['candidate_sha256']),
            radius_floor=.1)
        problem=create_physical_point_refined_problem(args.candidate,saved_field=old,
            include_saved_gauss_plateau=True,**common)
        vector,definition=problem.inject_saved_field(canonicalize_redundant=True)
        definition['input']=report['input'];report['refinement']=definition
        arrays=checkpoint_arrays(problem,vector,report['candidate']['sha256'],refinement_definition=definition)
        field_path=stem.with_name(stem.name+'-field.npz')
        report['new_field']=save_npz(field_path,**arrays)
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
            row=definition['old_cell_to_new_cells'][j]
            children=row['new_cells']
            mappings.append(dict(old_cell=j,old_interval=row['old_interval'],new_cells=children,
                children_exactly_cover_same_binary_endpoints=(
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

        # Both archives are consumed by the unchanged explicit-layout native
        # reader. Only four interior points and the two newly inserted
        # endpoints, on eight common angles, are queried. The exact real
        # P1 identity follows from R163, not from this bounded finite check.
        native_args=dict(reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            geometry=problem.geometry)
        native_old=IndependentTailPositiveTraceNativeField(args.input,args.candidate,**native_args)
        native_new=IndependentTailPositiveTraceNativeField(field_path,args.candidate,**native_args)
        points=[]
        for row in definition['requested_point_rows']:
            s=row['point'];left,right=row['old_interval']
            points.extend([.5*(left+s),s,.5*(s+right)])
        points=np.array(sorted(set(points)),float)
        angles=2*np.pi*np.arange(8)/8
        xx,xi=np.meshgrid(points,angles,indexing='ij')
        lhs=native_old.evaluate_angular_native(xx,xi)
        rhs=native_new.evaluate_angular_native(xx,xi)
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
        check=report['definition_checks']
        report['completed']=bool(report['input_unchanged'] and all(byte_checks.values()) and all(packet_checks.values())
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
