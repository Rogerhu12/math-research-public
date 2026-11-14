#!/usr/bin/env python3
"""Compare disk QR and full CSC on actual nonaxisymmetric M128 blocks."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
import tempfile
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import splu

P=Path(__file__).resolve().parent


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,P/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


base=load('qr_compare_driver','geometry_20261114_r225_free_core_bvp.py')
qrmod=load('qr_compare_factor','geometry_20261114_separated_qr_bvp.py')
normal=load('qr_compare_normal','geometry_20261114_normal_terminal_projector.py')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    data=base.fixed.read(args.input);g=base.fixed.read(args.profile)
    ident=data['original_metric_identity'];law=ident['law']
    c=np.array([float(Fraction(v))for v in ident['coefficients_rational']]);M,N=data['M'],data['N']
    if M!=128:
        raise ValueError('This recorded full-frequency comparison uses M128')
    q=base.native.outward.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    base.fixed.fft.enable_fft(q)
    jref=int(np.argmin(abs(np.array(data['state_locations'])-.98)))
    refrow=data['rows'][jref];ref=np.array(data['augmented_states'][jref])
    q.profile=lambda ignored:(float(ref[0]),float(ref[1]),refrow['app'])
    end_rows,unused,end_info=normal.projector(q,float(refrow['s']),ref[2:],33)
    q.profile=base.fixed.FixedProfile(g['geometry']).profile
    flow=base.BatchedFFTFlow(q)
    indices=[int(np.argmin(abs(np.array(data['state_locations'])-s)))for s in (.978,.981,.984)]
    x=np.array(data['state_locations'])[indices];y=np.array(data['augmented_states'])[indices,2:].T
    n=q.n;m=len(x);h=np.diff(x);f=flow(x,y)
    ym=(y[:,:-1]+y[:,1:])/2-h/8*(f[:,1:]-f[:,:-1])
    df=flow.jac(x,y);dm=flow.jac((x[:-1]+x[1:])/2,ym)
    K=32;nl=2*M+K+2;left=np.zeros((n,n));right=np.zeros_like(left)
    left[:K+1,:K+1]=np.eye(K+1)
    j=np.arange(M);left[K+1+j,1+j]=q.freq[1:];left[K+1+j,M+1+j]=1
    j=np.arange(M+1);left[K+1+M+j,2*M+1+j]=1;right[nl:]=end_rows
    J=base.block_csc.assemble(n,m,h,df,dm,left,right)
    expected=np.sin(np.arange(n*m)*.17)*1e-3;rhs=J@expected
    args.work.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='qr-actual-compare-',dir=args.work)as work:
        factor=qrmod.DiskQRFactor(n,m,left,right,nl,work)
        for j in range(m-1):
            factor.append(j,*qrmod.local_blocks(h[j],df[:,:,j],dm[:,:,j],df[:,:,j+1]))
        factor.finish();actual=factor.solve(rhs);direct=splu(J).solve(rhs)
        result=dict(scope=__doc__,n=n,m=m,stations=x.tolist(),free_dimensions=n-nl,
                    qr_residual_max=float(abs(J@actual-rhs).max()),
                    direct_residual_max=float(abs(J@direct-rhs).max()),rhs_max=float(abs(rhs).max()),
                    qr_vs_direct_max=float(abs(actual-direct).max()),
                    qr_known_solution_max=float(abs(actual-expected).max()),
                    direct_known_solution_max=float(abs(direct-expected).max()),
                    projector_diagnostics=end_info,nonlinear_BVP=False,
                    source_dependencies={name:hashlib.sha256((P/name).read_bytes()).hexdigest()for name in
                      ('geometry_20261114_separated_qr_compare.py','geometry_20261114_separated_qr_bvp.py',
                       'geometry_20261114_normal_terminal_projector.py','geometry_20261114_r225_free_core_bvp.py',
                       'geometry_20261114_block_csc_bvp.py')},
                    input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                    profile_sha256=hashlib.sha256(args.profile.read_bytes()).hexdigest())
        factor.close()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('n','m','qr_residual_max','direct_residual_max','rhs_max','qr_vs_direct_max')}),flush=True)


if __name__=='__main__':
    main()
