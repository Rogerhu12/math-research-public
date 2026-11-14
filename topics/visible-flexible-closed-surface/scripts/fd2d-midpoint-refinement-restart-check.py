#!/usr/bin/env python3
"""Check only the new empty-split saved-mesh restoration; no field/F/J/body."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import (
    create_midpoint_refined_problem,checkpoint_arrays,same_bits)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('candidate','input','radius-packet','reference-inlet','reference-cache','out'):
        p.add_argument('--'+n,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    started=time.perf_counter();old=load_npz(a.input)
    proof=json.loads(a.radius_packet.read_text())
    witness=dict(**identity(a.radius_packet),candidate_sha256=proof['candidate_sha256'])
    problem=create_midpoint_refined_problem(a.candidate,saved_field=old,split_cells=(),
        max_step=.04,gap=.9,reference_inlet=a.reference_inlet,reference_cache=a.reference_cache,
        base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1)
    vector,definition=problem.inject_saved_field()
    new=checkpoint_arrays(problem,vector,str(old['candidate_sha256']),refinement_definition=definition)
    same={key:same_bits(old[key],new[key]) for key in old}
    passed=all(same.values()) and definition['operation']=='restore_saved_mesh'
    passed=passed and definition['gauge_canonicalization_skipped_for_exact_restore']
    report=dict(schema='fd2d-midpoint-empty-split-restart-check-v1',passed=bool(passed),
        source=identity(__file__),provider=identity(Path(__file__).with_name('fd2d_gc_midpoint_refined_positive_trace_v3.py')),
        input=identity(a.input),candidate=identity(a.candidate),modes=problem.K,
        node_count=problem.N,parameter_count=problem.parameter_count,original_array_byte_identity=same,
        operation=definition['operation'],inactive_l_nodes=problem.inactive_l_raw_nodes.tolist(),
        inactive_trace_nodes=problem.inactive_trace_nodes.tolist(),
        constructor_rebound_saved_original_schema=True,
        common_field_or_native_check_repeated=False,no_F=True,no_J=True,no_BVP=True,no_body=True,
        independent_tail_full_constructor_check_performed=False,seconds=time.perf_counter()-started)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','modes','node_count','parameter_count','seconds')}))
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()
