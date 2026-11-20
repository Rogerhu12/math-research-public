#!/usr/bin/env python3
"""One small, explicit implementation check; no geometric candidate claim."""
from pathlib import Path
import importlib.util
import json
import argparse
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
DENSE = HERE.parent/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def rel(a, b):
    return float(np.linalg.norm(np.asarray(a).ravel()-np.asarray(b).ravel())
                 /max(1., np.linalg.norm(np.asarray(a).ravel()), np.linalg.norm(np.asarray(b).ravel())))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='Scratch report path; generated output is not committed')
    args = parser.parse_args()
    dense = load('small_batched_check_dense', DENSE)
    batch = load('small_batched_check_operator', HERE/'resume_20261120_batched_closed_gram.py')
    M, N = 4, 64
    mesh = np.array([0., .03, .09, .17, .31, .56, .83, 1.05, 1.21])
    times = np.empty(2*len(mesh)-1)
    times[::2] = mesh
    times[1::2] = (mesh[:-1]+mesh[1:])/2
    R = .7
    a = 1.+(R-1.)*times/mesh[-1]
    a[[0, -1]] = [1., R]
    kwargs = dict(M=M, N=N, width=.28)
    original = dense.ClosedGram(mesh, a, R, [1e-4, -2e-5], **kwargs)
    full = batch.create(dense, mesh, a, R, [1e-4, -2e-5], stage_block=3, **kwargs)
    quarter = batch.create(dense, mesh, a, R, [1e-4, -2e-5],
                           stage_block=3, quarter=True, **kwargs)
    rng = np.random.default_rng(20261120)
    x = rng.normal(scale=3e-5, size=original.free_size)
    x[-1] = .63
    jets, height, _ = original.unpack(x)
    jets[1:-1, 0, 0] += 1.-.4*mesh[1:-1]
    jets[1:-1, 0, 2*M+1] += .5*mesh[1:-1]
    jets[1:-1, 1, 0] -= .4
    jets[1:-1, 1, 2*M+1] += .5
    x, _ = original.pack(jets, height)
    v = rng.normal(scale=.003, size=x.shape)
    w = rng.normal(size=(original.P, original.N, 3))
    wq = rng.normal(size=(quarter.P, quarter.N, 3))
    rd, rf, rq = original.residual(x), full.residual(x), quarter.residual(x)
    jd, jf, jq = original.jvp(x, v), full.jvp(x, v), quarter.jvp(x, v)
    gd, gf = original.vjp(x, w), full.vjp(x, w)
    full_gradient = full.vjp(x, rf)
    quarter_gradient = quarter.vjp(x, rq)
    full_normal = full.vjp(x, jf)
    quarter_normal = quarter.vjp(x, jq)
    h = 1e-20
    full_cs = full.residual(x+1j*h*v).imag/h
    quarter_cs = quarter.residual(x+1j*h*v).imag/h
    adjoint_lhs = np.sum(jq*wq)
    adjoint_rhs = np.dot(v, quarter.vjp(x, wq))
    cache_full = full.set_base(x)
    cache_quarter = quarter.set_base(x)
    report = dict(
        purpose='Small synthetic implementation check, not a geometric solution or full warm audit',
        random_seed=20261120, M=M, full_N=N, quarter_N=quarter.N,
        mesh=mesh.tolist(), radius=R, width=.28, fixed_core=[1e-4, -2e-5],
        free_size=original.free_size, stage_block=3,
        original_vs_batched_residual_rel=rel(rd, rf),
        original_vs_batched_Jv_rel=rel(jd, jf),
        original_vs_batched_transpose_rel=rel(gd, gf),
        full_CS_rel=rel(jf, full_cs), quarter_CS_rel=rel(jq, quarter_cs),
        quarter_adjoint_rel=float(abs(adjoint_lhs-adjoint_rhs)/max(1., abs(adjoint_lhs), abs(adjoint_rhs))),
        full_quarter_residual_squared_norm_rel=float(abs(np.sum(rf*rf)-np.sum(rq*rq))/max(1., np.sum(rf*rf))),
        full_quarter_Jv_squared_norm_rel=float(abs(np.sum(jf*jf)-np.sum(jq*jq))/max(1., np.sum(jf*jf))),
        full_quarter_gradient_rel=rel(full_gradient, quarter_gradient),
        full_quarter_normal_action_rel=rel(full_normal, quarter_normal),
        full_cached_residual_rel=rel(rf, full.residual(x)),
        full_cached_Jv_rel=rel(jf, full.jvp(x, v)),
        full_cached_transpose_rel=rel(gf, full.vjp(x, w)),
        quarter_cached_residual_rel=rel(rq, quarter.residual(x)),
        quarter_cached_Jv_rel=rel(jq, quarter.jvp(x, v)),
        raw_quarter_sample_rel=rel(quarter.raw_residual(x), full.raw_residual(x)[:, :quarter.N]),
        full_cache=cache_full, quarter_cache=cache_quarter,
        affine_diagnostics=quarter.affine_diagnostics(x))
    errors = {k: value for k, value in report.items() if k.endswith('_rel')}
    report['passed'] = all(value < 2e-11 for value in errors.values())
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    if not report['passed']:
        raise SystemExit('Small batched operator verification failed')

if __name__ == '__main__':
    main()
