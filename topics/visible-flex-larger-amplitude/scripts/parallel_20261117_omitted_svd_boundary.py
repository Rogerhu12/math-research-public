#!/usr/bin/env python3
"""A fixed SVD combination of complete reachable omitted-velocity rows.

Consumes identified output of omitted_reachable_rows.py. U is fixed at the
accepted parent; the new 109 functions are U.T v_out, without Sigma inverse.
Only linear algebra is performed. No nonlinear solution, geometry, or full
omitted-spectrum cancellation is implied by the projected linear residual.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def norms(x):return dict(l2=float(np.linalg.norm(x)),linf=float(np.max(abs(x))))


def main(a):
    if sha(a.arrays)!=a.arrays_sha256 or sha(a.selection_report)!=a.selection_sha256:
        raise ValueError('Input identity mismatch')
    d=json.loads(a.selection_report.read_bytes())
    if d['array_sha256']!=a.arrays_sha256:raise ValueError('Selection report belongs to another array source')
    v=np.load(a.arrays);Z=v['terminal_basis'];A=v['reachable_jacobian'];b=v['raw_values']
    U,s,Vt=np.linalg.svd(A,full_matrices=False)
    inside=U@(U.T@b);outside=b-inside;c=Vt.T@((U.T@b)/s);delta=Z@c
    comparisons={}
    for name in ['only_Z','local_unit_qr','reachable_raw_qr','reachable_unit_qr']:
        I=np.array(d['selections'][name]['row_indices']);ci=np.linalg.solve(A[I],b[I]);error=b-A@ci
        comparisons[name]=dict(endpoint_correction=norms(Z@ci),all_rows_linear_residual=norms(error),
            selected_linear_residual=norms(error[I]),reduced_condition=d['selections'][name]['reduced']['condition'])
    singular=np.linalg.svd(U.T@A,compute_uv=False)
    matrices=a.out.with_suffix('.arrays.npz')
    np.savez_compressed(matrices,U=U,singular_values=s,Vt=Vt,endpoint_correction=delta,
        raw_parent_values=b,combined_parent_targets=U.T@b,unreachable_linear_residual=outside)
    report=dict(scope=__doc__,source_sha256=sha(__file__),input_array_sha256=sha(a.arrays),selection_report_sha256=sha(a.selection_report),
        parent_sha256=d['input_sha256'],M=d['M'],N=d['N'],endpoint=d['endpoint'],all_ode_components=d['all_ode_components'],left_rows=d['left_rows'],
        rows=int(A.shape[0]),free=int(A.shape[1]),combination_definition='B(y)=U.T v_out(y); U is fixed at the original accepted parent, without whitening by Sigma inverse.',
        array_path=str(matrices),array_sha256=sha(matrices),U_shape=list(U.shape),U_float64_c_order_sha256=hashlib.sha256(U.astype('<f8').tobytes(order='C')).hexdigest(),
        singular_max=float(s[0]),singular_min=float(s[-1]),condition=float(s[0]/s[-1]),combined_reduced_condition=float(singular[0]/singular[-1]),
        svd_relative_frobenius=float(np.linalg.norm(A-U@(s[:,None]*Vt))/np.linalg.norm(A)),combination_orthogonality=float(np.max(abs(U.T@U-np.eye(A.shape[1])))),
        parent_raw=norms(b),parent_range_projection=norms(inside),parent_orthogonal_residual=norms(outside),outside_l2_fraction=float(np.linalg.norm(outside)/np.linalg.norm(b)),
        parent_combined_value=norms(U.T@b),least_squares_endpoint_correction=norms(delta),least_squares_linear_residual=norms(b-A@c),
        combined_linear_residual=norms(U.T@(b-A@c)),full_normal_equation_defect=norms(A.T@(b-A@c)),row_selection_comparisons=comparisons)
    a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--arrays',type=Path,required=True);p.add_argument('--arrays-sha256',required=True)
    p.add_argument('--selection-report',type=Path,required=True);p.add_argument('--selection-sha256',required=True);p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
