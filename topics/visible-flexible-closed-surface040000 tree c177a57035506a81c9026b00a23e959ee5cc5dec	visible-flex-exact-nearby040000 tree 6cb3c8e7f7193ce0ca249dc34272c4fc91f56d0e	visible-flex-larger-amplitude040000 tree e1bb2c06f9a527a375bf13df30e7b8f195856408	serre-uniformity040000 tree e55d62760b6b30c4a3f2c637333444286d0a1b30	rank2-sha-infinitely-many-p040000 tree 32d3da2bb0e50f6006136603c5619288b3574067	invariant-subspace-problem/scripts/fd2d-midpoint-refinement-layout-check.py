#!/usr/bin/env python3
"""Only array layout/commutation for R163 v2; no new field/BVP evaluation."""
import argparse
import inspect
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_nested_angular_positive_trace import zero_extend_angular_arrays,FixedTailDegreePositiveTraceDAE
from fd2d_gc_midpoint_refined_positive_trace import midpoint_refine_arrays
from fd2d_gc_midpoint_refined_positive_trace_v2 import MidpointRefinedFixedTailDAE


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    started=time.perf_counter();old=load_npz(a.input)
    k,J=int(old['modes']),int(old['profile_count']);nt=len(old['parameters'])-k-J
    kk=2*k+1;cells=[63,65,71,118,119,121]
    x,y,d=midpoint_refine_arrays(old['mesh'],old['corrections'],cells)
    y1,p1,unused=zero_extend_angular_arrays(y,old['parameters'],old_modes=k,new_modes=kk,
        tail_parameter_count=nt,profile_count=J)
    yp,pp,unused=zero_extend_angular_arrays(old['corrections'],old['parameters'],old_modes=k,new_modes=kk,
        tail_parameter_count=nt,profile_count=J)
    x2,y2,unused=midpoint_refine_arrays(old['mesh'],yp,cells)
    passed=np.array_equal(x,x2) and np.array_equal(y1,y2) and np.array_equal(p1,pp)
    passed=passed and FixedTailDegreePositiveTraceDAE in inspect.getmro(MidpointRefinedFixedTailDAE)
    here=Path(__file__).resolve().parent
    out=dict(schema='fd2d-radial-angular-array-commutation-check-v1',passed=bool(passed),
        input=identity(a.input),source=identity(__file__),
        provider_v2=identity(here/'fd2d_gc_midpoint_refined_positive_trace_v2.py'),
        interpolation_provider=identity(here/'fd2d_gc_midpoint_refined_positive_trace.py'),
        old_modes=k,new_modes=kk,tail_parameter_count=nt,profile_parameter_count=J,
        old_raw_columns=old['corrections'].shape[1],new_raw_columns=y1.shape[1],
        old_parameter_count=len(old['parameters']),new_parameter_count=len(p1),
        mesh_and_coefficients_equal=bool(np.array_equal(y1,y2) and np.array_equal(x,x2)),
        parameter_arrays_equal=bool(np.array_equal(p1,pp)),
        maximum_commutation_difference=float(np.max(np.abs(y1-y2))),
        independent_tail_mro=[c.__name__ for c in inspect.getmro(MidpointRefinedFixedTailDAE)],
        preferred_consumption_order='R158 angular zero extension on the identical original mesh, then R163 radial subdivision; preserve and remap old physical interior-row intervals',
        v2_complete_K31_field_or_constructor_check_performed=False,
        no_BVP=True,no_full_function_recheck=True,no_whole_objective=True,no_Jacobian=True,
        seconds=time.perf_counter()-started)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ('passed','old_modes','new_modes','tail_parameter_count',
        'new_raw_columns','new_parameter_count','maximum_commutation_difference','seconds')}))
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()
