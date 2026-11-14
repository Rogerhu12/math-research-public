#!/usr/bin/env python3
"""Zero-pad an actual native eta/zeta Hermite field for angular refinement.

Every old value and first-x coefficient, the mesh, central coefficient,
physical-height normalization and T are retained. The old modes of the new
linear port must be identical. Added coefficients are zero. This constructs
an unchanged mathematical field as an initial guess, not a refined solve.
"""
import argparse, json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field',type=Path,required=True)
    p.add_argument('--old-port',type=Path,required=True)
    p.add_argument('--new-port',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    a=p.parse_args(); old=load_npz(a.field)
    left=json.loads(a.old_port.read_text()); right=json.loads(a.new_port.read_text())
    old_K=(old['values'].shape[0]-1)//2; new_K=len(right['rows'])
    if new_K<=old_K or old['parameters'].shape!=(2*old_K+1,):
        raise ValueError('A strictly higher angular space and the actual T-design state are required')
    left_rows={v['mode']:v['slope'] for v in left['rows']}
    right_rows={v['mode']:v['slope'] for v in right['rows']}
    if left['cut']!=right['cut'] or any(left_rows[2*j]!=right_rows[2*j] for j in range(1,old_K+1)):
        raise ValueError('This exact padding entry requires the same physical cut and identical retained port columns')
    arrays={'mesh':old['mesh'].copy()}
    for key in ('values','first'):
        value=np.zeros((2*new_K+1,len(old['mesh'])),dtype=old[key].dtype)
        value[:old_K+1]=old[key][:old_K+1]
        value[new_K+1:new_K+1+old_K]=old[key][old_K+1:]
        arrays[key]=value
    par=np.zeros(2*new_K+1,dtype=old['parameters'].dtype)
    par[:old_K]=old['parameters'][:old_K]
    par[new_K:new_K+old_K]=old['parameters'][old_K:2*old_K]
    par[-1]=old['parameters'][-1]; arrays['parameters']=par
    for key in ('physical_s','radial_scale'):
        if key in old: arrays[key]=old[key].copy()
    result=save_npz(a.out_prefix.with_name(a.out_prefix.name+'-field.npz'),**arrays)
    report=dict(schema='fd2d-exact-native-mode-padding-v1',source=identity(__file__),
        source_field=identity(a.field),old_port=identity(a.old_port),new_port=identity(a.new_port),
        old_dimension=2*old_K+1,new_dimension=2*new_K+1,radial_nodes=len(arrays['mesh']),
        original_T=float(par[-1]),all_old_coefficients_copied_without_arithmetic=True,
        all_added_coefficients_exactly_zero=True,retained_port_columns_bitwise_identical=True,
        same_exact_native_Hermite_Fourier_field=True,new_solution=False,output=result)
    path=a.out_prefix.with_name(a.out_prefix.name+'-report.json')
    if path.exists(): raise FileExistsError(path)
    path.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
