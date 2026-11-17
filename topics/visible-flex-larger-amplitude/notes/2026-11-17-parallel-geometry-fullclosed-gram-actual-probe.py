#!/usr/bin/env python3
"""One complete Jv/complex-step/adjoint probe of a SHA-bound actual warm.

No warm is invented here.  No solve, line search, resampling, or domain
repair is performed.  The supplied q shared jets must already satisfy the
exact affine core/terminal definition.  Ordinary floating observations do
not certify the continuous fullclosed geometry or exact scalar integrals.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import zipfile
import numpy as np

OPERATOR_SHA = 'e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'
SEED = 20261117
CS_STEP = 1e-30


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def emit(value):
    print(json.dumps(value,ensure_ascii=False,allow_nan=False),flush=True)


def load_bundle(path):
    if Path(path).suffix == '.npz':
        with np.load(path,allow_pickle=False) as actual:
            return {name:actual[name] for name in actual.files}
    data = Path(path).read_bytes()
    if data[:2] == b'\x1f\x8b':
        data = gzip.decompress(data)
    return json.loads(data)


def direction(op,rng):
    """One direction with nonzero entries in every free variable block.

    These fixed scales balance physical first-derivative responses.  They
    are only test-vector scales, not an optimization preconditioner.
    """
    v = rng.normal(size=op.free_size)
    at = op.M-op.K
    v[:at] /= np.sqrt(op.M)*(1+op.freq[op.K:]**2)
    h = np.diff(op.mesh)
    v[at:at+2*op.M+1] /= h[0]
    at += 2*op.M+1
    interior = v[at:-1].reshape((op.J-2,3,op.n))
    for j in range(op.J-2):
        interior[j,0] *= min(h[j],h[j+1])
        interior[j,2] /= max(h[j],h[j+1])
    v[-1] *= op.width
    return v


def gram_summary(op,residual):
    ss,cross,pp = residual[...,0],residual[...,1],residual[...,2]
    values = (np.abs(ss+pp)+np.sqrt((ss-pp)**2+4*cross*cross))/2
    at = np.unravel_index(int(np.argmax(values)),values.shape)
    det = (1+ss)*(1+pp)-cross*cross
    amin = np.unravel_index(int(np.argmin(det)),det.shape)
    return dict(kind='Actual shared-quintic nodes and midpoints; finite angle samples only',
                maximum_relative_Gram_operator=float(values[at]),
                maximum_location=dict(stage=int(at[0]),kind='node' if at[0]%2==0 else 'actual_quintic_midpoint',
                                      s=float(op.times[at[0]]),angle=float(op.phi[at[1]])),
                node_maximum=float(values[::2].max()),midpoint_maximum=float(values[1::2].max()),
                component_maximum=np.max(np.abs(residual),axis=(0,1)).tolist(),
                sampled_relative_Gram_determinant_min=float(det[amin]),
                determinant_location=dict(stage=int(amin[0]),s=float(op.times[amin[0]]),angle=float(op.phi[amin[1]])),
                continuous_metric_or_immersion_certified=False)


def main(args):
    began = time.perf_counter()
    if sha(args.operator) != OPERATOR_SHA:
        raise ValueError('The prepared matrix-free operator changed')
    if sha(args.bundle) != args.bundle_sha:
        raise ValueError('Not the identity-bound actual warm/scalar bundle')
    if args.out.exists() or args.arrays.exists():
        raise FileExistsError('This one-probe report path already exists; do not silently repeat')
    data = load_bundle(args.bundle)
    spec = importlib.util.spec_from_file_location('fullclosed_actual_gram_operator',args.operator)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if int(data.get('M',160)) != 160:
        raise ValueError('This declared preparation uses the actual M160 warm')
    op = module.ClosedGram(data['mesh'],data['a_stages'],data['radius'],
                          data['fixed_core_first3'],M=160,N=2048,
                          width=data.get('width',0.05))
    if op.K != 3:
        raise ValueError('Keep the original three fixed core coefficients')
    jets = np.asarray(data['qjets'],dtype=float)
    if not np.isfinite(jets).all() or not np.isfinite(data['Hcap']):
        raise ValueError('Actual warm is nonfinite; no repair is defined')
    x,projection = op.pack(jets,float(data['Hcap']),require_affine=True)
    prep = op.prepare(x)
    if not np.isfinite(prep.rho).all() or not np.all(prep.rho > 0):
        raise ValueError('The supplied core fails even the prescribed finite angular positivity check')
    report = dict(scope=__doc__,schema='fullclosed-actual-C2-angle-Gram-one-Jacobian-probe-v1',
                  source_sha256=sha(__file__),operator_sha256=OPERATOR_SHA,
                  base_probe_source_sha256='f949db0a4df672846dce464d4c6d44419c854918a93da55b1c08dec26279cdd2',
                  array_probe_source_sha256='7db784193eba0ddb063c74139c3a43334bc8111178ba85f99f8d9cc662111b66',
                  bundle_path=str(args.bundle.resolve()),bundle_sha256=args.bundle_sha,
                  M=op.M,N=op.N,nodes=op.J,stages=op.P,variables=op.free_size,
                  residual_values=op.P*op.N*3,radius=op.R,S=op.S,width=op.width,Hcap=float(data['Hcap']),
                  input_affine_check=projection,structural_checks=op.affine_diagnostics(x),
                  sampled_core_rho_min=float(prep.rho.min()),sampled_core_rho_max=float(prep.rho.max()),
                  core_first3=prep.core[:3].tolist(),input_keys=sorted(data),
                  fixed_input_interpretation='Use the supplied same-Hold scalar carrier/oracle metadata; this floating probe does not replace its exact definition.',
                  nonlinear_solve_executed=False,finite_spectrum_completeness_claimed=False,
                  exact_scalar_or_continuous_geometry_certified=False)
    emit(dict(event='bound_actual_input',variables=op.free_size,residual_values=report['residual_values'],
              bundle_sha256=args.bundle_sha,operator_sha256=OPERATOR_SHA))
    array_names=[]
    with zipfile.ZipFile(args.arrays,'x',compression=zipfile.ZIP_STORED,allowZip64=True) as archive:
        def save_array(name,value):
            with archive.open(name+'.npy','w',force_zip64=True) as target:
                np.lib.format.write_array(target,np.asarray(value),allow_pickle=False)
            array_names.append(name)
        t=time.perf_counter();res=op.residual(x);report['residual_seconds']=time.perf_counter()-t
        report['actual_warm_finite_Gram']=gram_summary(op,res)
        save_array('dense_residual',res)
        del res
        rng=np.random.default_rng(SEED);v=direction(op,rng)
        save_array('x',x);save_array('direction',v)
        t=time.perf_counter();jv=op.jvp(x,v);report['jvp_seconds']=time.perf_counter()-t
        save_array('dense_jvp',jv)
        emit(dict(event='actual_direction_complete',seconds=report['jvp_seconds']))
        t=time.perf_counter();cs=op.residual(x.astype(complex)+1j*CS_STEP*v).imag/CS_STEP
        report['complex_step_seconds']=time.perf_counter()-t
        difference=jv-cs
        denominator=max(float(np.linalg.norm(jv.ravel())),float(np.linalg.norm(cs.ravel())),np.finfo(float).tiny)
        report['full_Jacobian_check']=dict(method='One complete complex-step direction in all free blocks',
            seed=SEED,step=CS_STEP,absolute_max=float(np.abs(difference).max()),
            relative_l2=float(np.linalg.norm(difference.ravel())/denominator),
            response_norm=float(np.linalg.norm(jv.ravel())),direction_norm=float(np.linalg.norm(v)),
            block_scales='core 1/[sqrt(M)(1+nu^2)]; A0 1/h0; interior Y min(hL,hR), U 1, A 1/max(hL,hR); H width')
        del cs,difference
        weights=rng.normal(size=jv.shape)/np.sqrt(jv.size)
        save_array('weights',weights)
        left=float(np.dot(weights.ravel(),jv.ravel()))
        del jv
        t=time.perf_counter();jt=op.vjp(x,weights);report['adjoint_seconds']=time.perf_counter()-t
        save_array('dense_vjp',jt)
        right=float(np.dot(jt,v))
        report['full_adjoint_check']=dict(left=left,right=right,absolute_error=abs(left-right),
            relative_error=abs(left-right)/max(abs(left),abs(right),np.finfo(float).tiny),
            complete_angle_values=True,all_free_Y_U_A_H_and_core_lift_chain=True)
    report['dense_array_archive']=dict(path=str(args.arrays.resolve()),sha256=sha(args.arrays),bytes=args.arrays.stat().st_size,names=array_names,scope='Only already-computed arrays, retained for the single FFT equivalence comparison; no extra dense evaluation.')
    report['elapsed_seconds']=time.perf_counter()-began
    args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    emit(dict(event='complete_one_actual_probe',report_sha256=sha(args.out),
              Jacobian=report['full_Jacobian_check'],adjoint=report['full_adjoint_check'],
              sampled_Gram=report['actual_warm_finite_Gram'],nonlinear_solve_executed=False))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--bundle',type=Path,required=True)
    parser.add_argument('--bundle-sha',required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--arrays',type=Path,required=True)
    main(parser.parse_args())
