#!/usr/bin/env python3
"""Small mapping/definition/endpoint check for the R168 parent wrapper.

No body ODE, field residual, whole Jacobian or BVP is run. This does not
repeat the existing native reader's full jet validation.
"""
from __future__ import annotations
import os
for _thread_key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_raw_native_field import identity
from fd2d_gc_shortened_cylinder_native import (
    ShortenedCylinderNativeField,load_shortened_body_reader,rational)


def maximum(value):return float(np.max(np.abs(np.asarray(value)),initial=0.))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-definition',type=Path,required=True)
    ap.add_argument('--delta',default='7/50')
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh wrapper/check stem')
    started=time.monotonic()
    child=ShortenedCylinderNativeField(args.parent_definition,args.delta)
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    definition=Path(str(args.out_prefix)+'-definition.json')
    definition.write_text(json.dumps(child.definition(),indent=2,allow_nan=False)+'\n')
    view=load_shortened_body_reader(definition)
    assert view.definition()['radial_mapping']==child.definition()['radial_mapping']
    assert view.parameters.dtype==child.parent.parameters.dtype
    assert view.parameters.tobytes()==child.parent.parameters.tobytes()
    u=np.array([.271,.93])
    # One exact central point, one actual retained coast node, one ordinary
    # exterior coordinate and the explicit cut. This is not a domain cover.
    old=child.parent.nodes
    coast_ids=np.flatnonzero((old>child.parent.coast_reference.entry_s)&
                            (old<child.parent.coast_reference.exit_s))
    if not len(coast_ids):raise ValueError('No existing coast knot is available for this small check')
    parent_index=int(coast_ids[len(coast_ids)//2])
    child_index=child.mapping.parent_indices.index(parent_index)
    ordinary=.7*child.mapping.end
    points=[0.,float(child.nodes[child_index]),ordinary,child.mapping.end]
    keys=['a','a_s','a_ss','J','n','m','l']+[q+s for q in ('n','m','l') for s in ('_u','_uu')]
    rows=[];worst=0.
    for s in points:
        ps=float(child.mapping(s))
        actual=view.physical(s,u)
        expected=child.parent.physical_angular(ps,u)
        differences={key:maximum(actual[key]-expected[key]) for key in keys}
        worst=max(worst,max(differences.values()))
        profile=child.profile.jet([s]);parent_profile=child.parent.profile.jet([ps])
        profile_difference=max(maximum(profile[k]-parent_profile[k]) for k in ('a','a_s','a_ss','c','K'))
        assert profile_difference==0.
        rows.append(dict(mapping=child.mapping.point_record(s),
            value_and_angular_twojet_absolute_differences=differences,
            target_profile_absolute_difference=profile_difference,
            sampled_parent_values={k:np.asarray(expected[k]).tolist() for k in keys},
            child_reported_physical_s=np.asarray(actual['s']).tolist(),
            parent_s_evaluated=np.asarray(actual['parent_s_evaluated']).tolist()))
    assert worst==0.
    cut=float(child.mapping(child.mapping.end))
    assert cut==float(child.parent.nodes[-1])
    # Preserve the existing deliberate radial-cut refusal. This is not a
    # missing body datum: the body path above uses the angular interface.
    rejected=False
    try:child.physical(child.mapping.end,u)
    except ValueError as exc:
        rejected='Exact cut radial II jets are not claimed' in str(exc)
    assert rejected
    initial=child.body_initial(u);parent_initial=child.parent.body_initial(u)
    assert initial.tobytes()==parent_initial.tobytes()
    # Exact-cylinder state constructed algebraically, not from an ODE or
    # an invented saved intermediate state. Only X_z changes.
    parent_cylinder=parent_initial.copy()
    parent_cylinder[...,2]+=child.mapping.delta_float
    translated=child.translate_parent_body_state(parent_cylinder)
    cylinder_transport_error=maximum(translated-initial)
    report=dict(schema='fd2d-shortened-cylinder-small-native-check-v1',
        source=identity(__file__),wrapper_source=identity(Path(__file__).with_name('fd2d_gc_shortened_cylinder_native.py')),
        parent_native_definition=identity(args.parent_definition),parent_field=identity(child.arrays_path),
        child_definition=identity(definition),Delta_exact=str(rational(args.delta)),
        parent_node_count=len(child.parent.nodes),child_integration_node_count=len(child.nodes),
        mode_count=child.K,parameter_layout=child.explicit_parameter_layout,
        parent_parameter_bytes_retained=True,child_P1_coefficients_created=False,
        mathematical_metric_changed=True,parent_full_functions_composed_without_reprojection=True,
        cylinder_structure=child.cylinder_certificate,
        material_u=u.tolist(),radial_point_count=len(points),rows=rows,
        maximum_mapped_value_and_angular_jet_difference=worst,
        parent_cut_selected_exactly=True,radial_cut_II_refusal_retained=rejected,
        body_initial_bitwise_equal=True,algebraic_cylinder_state_transport_maximum_error=cylinder_transport_error,
        child_definition_reload_passed=True,
        ordinary_mapping_errors_are_coordinate_evaluation_errors_not_new_mathematical_P1_knots=True,
        full_R158_jet_check_repeated=False,body_ODE_runs=0,whole_F_or_J_runs=0,BVP_runs=0,
        actual_cut_Z_paid=False,whole_held_or_global_reach_paid=False,
        passed=True,seconds=time.monotonic()-started)
    report_path=Path(str(args.out_prefix)+'-report.json')
    report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(report_path),passed=True,Delta_exact=str(child.mapping.delta),
        parent_nodes=len(child.parent.nodes),child_nodes=len(child.nodes),
        mapped_jet_difference=worst,cut_exact=True,body_ODE_runs=0,
        seconds=report['seconds'])),flush=True)
    return 0


if __name__=='__main__':raise SystemExit(main())
