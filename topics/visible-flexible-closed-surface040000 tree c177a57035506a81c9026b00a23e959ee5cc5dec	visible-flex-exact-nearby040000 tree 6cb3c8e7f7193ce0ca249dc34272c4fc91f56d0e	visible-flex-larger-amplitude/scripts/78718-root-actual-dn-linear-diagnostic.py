#!/usr/bin/env python3
"""Inspect saved physical tail slope Jacobians; no solver or certificate.

The finite tail DN derivative alone is not the full prefix-tail boundary
operator. Its floating point condition estimate does not prove any inverse
bound for the current coupled problem or the infinite-dimensional problem.
Arrays are read and kept in the terminal process; only scalar diagnostics
and source/input identities are saved.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old',type=Path,required=True)
    p.add_argument('--new',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise ValueError('Use a new report path')
    records=[]; matrices=[]
    for path in [args.old,args.new]:
        data=json.loads(gzip.decompress(path.read_bytes()))
        r=data['response'];m=r['checkpoint']['parameters']['modes']
        J=np.asarray(r['heightJetJacobian'],dtype=float).reshape(3*m+2,m)
        if J.shape!=(3*m+2,m) or not np.all(np.isfinite(J)):
            raise ValueError('Unexpected actual height-jet derivative shape')
        D=J[:m,:];sv=np.linalg.svd(D,compute_uv=False)
        diagonal=np.diag(np.diag(D)); off=D-diagonal
        row_dominance=np.abs(np.diag(D))-np.sum(np.abs(off),axis=1)
        col_dominance=np.abs(np.diag(D))-np.sum(np.abs(off),axis=0)
        records.append(dict(input=identity(path),modes=m,
            true_response_converged=r['converged'],response_residual=float(r['residual']),
            slope_singular_max=float(sv[0]),slope_singular_min=float(sv[-1]),
            slope_condition_estimate=float(sv[0]/sv[-1]),
            slope_diagonal_absolute_min=float(np.abs(np.diag(D)).min()),
            slope_diagonal_absolute_max=float(np.abs(np.diag(D)).max()),
            offdiagonal_spectral_norm=float(np.linalg.norm(off,2)),
            row_diagonal_dominance_margin_min=float(row_dominance.min()),
            column_diagonal_dominance_margin_min=float(col_dominance.min()),
            second_jet_derivative_spectral_norm=float(np.linalg.norm(J[m:2*m,:],2)),
            mean_slope_derivative_euclidean_norm=float(np.linalg.norm(J[2*m,:])),
            mean_second_derivative_euclidean_norm=float(np.linalg.norm(J[2*m+1,:])),
            height_identity_maximum_difference=float(np.max(np.abs(J[2*m+2:,:]-np.eye(m))))))
        matrices.append(D)
    k=min(len(matrices[0]),len(matrices[1]))
    delta=matrices[1][:k,:k]-matrices[0][:k,:k]
    report=dict(scope=__doc__,script=identity(__file__),records=records,
        common_block_order=k,common_block_spectral_difference=float(np.linalg.norm(delta,2)),
        common_block_relative_spectral_difference=float(np.linalg.norm(delta,2)/np.linalg.norm(matrices[0][:k,:k],2)),
        actual_new_solver_calls=0,actual_new_tail_calls=0,
        full_coupled_inverse_proved=False,infinite_inverse_proved=False)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(args.out),finite_slope_diagnostics=[
        {k:v for k,v in a.items() if k in ('modes','slope_condition_estimate','slope_singular_min','slope_singular_max','offdiagonal_spectral_norm','row_diagonal_dominance_margin_min')} for a in records],
        common_block_relative_difference=report['common_block_relative_spectral_difference'],solver_calls=0)))

if __name__=='__main__':main()
