#!/usr/bin/env python3
"""Compare original and long-precision Fourier transforms on a saved curve.

Only RHS, values/project and velocity evaluation are performed. No BVP, DN,
curve integration, or candidate output is produced. Reports contain scalars.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy import fft

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def identity(path):
    p = Path(path).resolve()
    raw = p.read_bytes()
    return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def lift(y, old, new):
    out = np.zeros((3*new+1, y.shape[1]))
    out[0] = y[0]
    for j in range(3):
        out[j*new+1:j*new+old+1] = y[j*old+1:(j+1)*old+1]
    return out


def difference(a, b):
    d = np.asarray(a)-np.asarray(b)
    norm = np.sqrt(np.sum(np.abs(a)**2))
    return {'max_absolute':float(np.max(np.abs(d))),
            'relative_l2':float(np.sqrt(np.sum(np.abs(d)**2))/max(norm,np.longdouble('1e-300')))}


def timing(call, repeat):
    samples = []
    for _ in range(repeat):
        begin = time.perf_counter()
        result = call()
        samples.append(time.perf_counter()-begin)
    return result, float(np.median(samples))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--repeat', type=int, default=5)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError('Use a fresh output')
    loader = module('long_fourier_loader', HERE/'db6f-prefix-flat-geometry-source.py')
    fast = module('long_fourier_transforms', HERE/'78718-prefix-long-fourier-transforms.py')
    rec, obj, reference, sol = loader.source(args.checkpoint,
        TOPIC/'notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json',
        TOPIC/'repro/source-root')
    s = np.linspace(0, reference.end, 32)
    source = sol.sol(s)
    rows = []
    for M,N in ((15,512),(22,1024)):
        if M < obj.M:
            continue
        flow = obj.Flow(obj.cfg,obj.port,M,obj.q,N,obj.base_mode,obj.bridge)
        y = lift(source, obj.M, M)
        p = np.zeros(M)
        yl = y.astype(np.longdouble)
        rng = np.random.default_rng(78718+M)
        direction = rng.normal(size=y.shape)/(1+np.arange(flow.n))[:,None]
        epsilon = np.longdouble('1e-25')
        yc = yl.astype(np.clongdouble)
        yc.imag = epsilon*direction
        old_rhs, old_rhs_seconds = timing(lambda:flow.fun(s,y,p), args.repeat)
        old_rhs_long = flow.fun(s, yl, p)
        old_complex = flow.fun(s,yc,p)
        old_velocity, old_velocity_seconds = timing(lambda:flow.velocity_s(s,yl,old_rhs_long), args.repeat)
        original_values, original_project = flow.values, flow.project
        old_values = [flow.values(yl, B) for B in (flow.B,flow.B1,flow.B2)]
        field = old_velocity[0]['V']-old_velocity[0]['geo']['s1']
        old_projected = [flow.project(field,B) for B in (flow.B,flow.B1,flow.B2)]
        original_value_complex = [flow.values(yc,B) for B in (flow.B,flow.B1,flow.B2)]
        begin = time.perf_counter()
        stats = fast.attach(flow)
        setup = time.perf_counter()-begin
        new_rhs, new_rhs_seconds = timing(lambda:flow.fun(s,y,p), args.repeat)
        new_rhs_long = flow.fun(s,yl,p)
        new_complex = flow.fun(s,yc,p)
        new_velocity, new_velocity_seconds = timing(lambda:flow.velocity_s(s,yl,old_rhs_long),args.repeat)
        values_rows = []
        for order,B in enumerate((flow.B,flow.B1,flow.B2)):
            value = flow.values(yl,B)
            projected = flow.project(field,B)
            complex_value = flow.values(yc,B)
            values_rows.append({'order':order,'values_dtype':str(value.dtype),
                'project_dtype':str(projected.dtype), 'complex_values_dtype':str(complex_value.dtype),
                'values_difference':difference(old_values[order],value),
                'project_difference':difference(old_projected[order],projected),
                'complex_values_direction_difference':difference(
                    original_value_complex[order].imag/epsilon,complex_value.imag/epsilon)})
        # Unknown/copied tables must use the original implementation, including
        # local-frame tables; this comparison exercises the actual fallback.
        copied = flow.B1.copy()
        fallback = flow.values(yl,copied)
        fallback_equal = bool(np.array_equal(fallback,original_values(yl,copied)))
        row = {'M':M,'N':N,'radial_points':len(s),'repetitions':args.repeat,
            'table_setup_seconds':setup,'original_RHS_median_seconds':old_rhs_seconds,
            'new_RHS_median_seconds':new_rhs_seconds,'RHS_speedup':old_rhs_seconds/new_rhs_seconds,
            'original_velocity_median_seconds':old_velocity_seconds,
            'new_velocity_median_seconds':new_velocity_seconds,
            'velocity_speedup':old_velocity_seconds/new_velocity_seconds,
            'RHS_difference':difference(old_rhs,new_rhs),
            'long_RHS_difference':difference(old_rhs_long,new_rhs_long),
            'long_RHS_dtype':str(new_rhs_long.dtype),'complex_RHS_dtype':str(new_complex.dtype),
            'complex_step_direction_difference':difference(old_complex.imag/epsilon,new_complex.imag/epsilon),
            'velocity_difference':difference(old_velocity[0]['V'],new_velocity[0]['V']),
            'F_s_psi_difference':difference(old_velocity[1],new_velocity[1]),
            'velocity_s_difference':difference(old_velocity[2],new_velocity[2]),
            'basis_transforms':values_rows,'unknown_basis_fallback_exact':fallback_equal,
            'transform_statistics':stats}
        rows.append(row)
        print(json.dumps({'M':M,'N':N,'RHS_speedup':row['RHS_speedup'],
            'velocity_speedup':row['velocity_speedup'],'RHS_difference':row['RHS_difference'],
            'complex_step_direction_difference':row['complex_step_direction_difference']}), flush=True)
    x = np.arange(8,dtype=np.longdouble)/7
    report = {'scope':__doc__,'script':identity(__file__),
        'backend':identity(HERE/'78718-prefix-long-fourier-transforms.py'),
        'checkpoint':identity(args.checkpoint),'source_was_successful':rec.get('solver_success') is True,
        'fft_dtype':{'longdouble_bits':np.finfo(np.longdouble).bits,
            'mantissa_bits_without_implicit_leading_bit':np.finfo(np.longdouble).nmant,
            'rfft':str(fft.rfft(x).dtype),'irfft':str(fft.irfft(fft.rfft(x)).dtype)},
        'rows':rows,'BVP_calls':0,'DN_calls':0,'new_surface_created':False}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':identity(args.out),'BVP_calls':0,'DN_calls':0}),flush=True)


if __name__ == '__main__':
    main()
