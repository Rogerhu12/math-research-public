#!/usr/bin/env python3
"""Compare next velocity projections on an unchanged saved prefix.

No initial guess is improved here and no BVP/DN/ODE is solved. This is a small
floating diagnostic for selecting an actual next frequency computation.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name,path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def ident(path):
    path = Path(path).resolve()
    return {'path':str(path),'bytes':path.stat().st_size,
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--modes',type=int,nargs='+',default=[15,16,18,22])
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    begin = time.monotonic()
    # The reused diagnosis() has no production-plan/approval dependency.
    old = module('next_mode_original_diagnostic',HERE/'78718-prefix-fixed-state-projection-v1.py')
    np = old.np
    loader = module('next_mode_original_source',HERE/'db6f-prefix-flat-geometry-source.py')
    port = TOPIC/'notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'
    source_root = TOPIC/'repro/source-root'
    rec,obj,flow,sol = loader.source(args.checkpoint,port,source_root)
    positions = np.unique(np.r_[np.linspace(0,flow.end,33),
        0.00196561545,.05,.11814752887,.2,.27472985991302756,.27483516074,.4,.7,1.])
    positions = positions[(positions>=0)&(positions<=flow.end)]
    rows = []
    for M in args.modes:
        if M < obj.M:raise ValueError('This diagnostic only adds exact zero modes')
        result,_ = old.diagnosis(rec,obj,sol,positions,M,2048,2048)
        rows.append(result)
    resources = []
    for M in args.modes:
        n,k = 3*M+1,M
        minimum = max(512,8*(3*M+1))
        N = 1 << (minimum-1).bit_length()
        sizes = {}
        for radial in [2633,6599,8000]:
            dim = n*radial+k
            nnz = (2*n+k)*dim
            index_bytes = 4 if max(dim,nnz) <= np.iinfo(np.int32).max else 8
            sizes[str(radial)] = nnz*(8+index_bytes)+(dim+1)*index_bytes
        resources.append({'M':M,'states':n,'parameters':k,'default_angular':N,
            'canonical_CSC_bytes_by_nodes':sizes,
            'n2N_relative_to_M16':n*n*N/(49*49*512),
            'scope':'Final explicit CSC storage only; no LU/Jacobian/worker peak guarantee.'})
    small = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    inputs = [ident(args.checkpoint),ident(port)]
    for chunk in small['pp_coefficient_chunks']:
        row = ident(args.checkpoint.parent/chunk['file'])
        if row['bytes'] != chunk['bytes'] or row['sha256'] != chunk['sha256']:
            raise ValueError('Input coefficient bytes differ')
        inputs.append(row)
    report = {'scope':__doc__,'script':ident(__file__),
        'defining_functions':[ident(HERE/'78718-prefix-fixed-state-projection-v1.py'),
                              ident(HERE/'db6f-prefix-flat-geometry-source.py')],
        'inputs':inputs,'source_modes':obj.M,'source_solver_success':rec.get('solver_success'),
        'physical_radial_points':positions.tolist(),'diagnostics':rows,'resource_estimates':resources,
        'new_curve_generated':False,'continuous_error_bound':False,
        'BVP_calls':0,'DN_calls':0,'flow_integrations':0,'seconds':time.monotonic()-begin}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':ident(args.out),'seconds':report['seconds'],
        'radial_points':len(positions),'projections':[{
            'M':row['projection_modes'],
            'source_E_FFT_l1':row['projected_source']['max_E_FFT_l1'],
            'source_F_FFT_l1':row['projected_source']['max_F_FFT_l1'],
            'fixed_G_FFT_l1':row['projected_source']['max_G_FFT_l1']}
            for row in rows],'resource_estimates':resources,'BVP_calls':0,'DN_calls':0},sort_keys=True))


if __name__ == '__main__':
    main()
