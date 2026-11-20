#!/usr/bin/env python3
"""Locate the single actual full/quarter raw-gradient discrepancy.

No new acceptance threshold and no nonlinear solve.  The original failed
diagnostic remains unchanged; this records scaling and a direct bilinear
identity at the same actual point.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rel(a, b):
    return float(np.linalg.norm((a-b).ravel())/max(1., np.linalg.norm(a.ravel()), np.linalg.norm(b.ravel())))


def decode_coordinate(op, index):
    ncore = op.M-op.K
    if index < ncore:
        return dict(kind='core support coefficient', mode=index+op.K+1)
    index -= ncore
    if index < 2*op.M+1:
        node, jet, component = 0, 2, index
    else:
        index -= 2*op.M+1
        if index == 3*(op.J-2)*op.n:
            return dict(kind='cap height')
        node = 1+index//(3*op.n)
        rest = index % (3*op.n)
        jet, component = rest//op.n, rest % op.n
    if component <= op.M:
        label, mode = 'radial cosine', component
    elif component <= 2*op.M:
        label, mode = 'tangential sine', component-op.M
    else:
        label, mode = 'vertical cosine', component-(2*op.M+1)
    return dict(kind='residual jet', node=int(node), s=float(op.mesh[node]),
                jet=('Y', 'U', 'A')[jet], component=label, mode=int(mode),
                left_h=float(op.mesh[node]-op.mesh[node-1]) if node else None,
                right_h=float(op.mesh[node+1]-op.mesh[node]) if node+1 < op.J else None)


def scalar_rel(x, y):
    return float(abs(x-y)/max(1., abs(x), abs(y)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'operator', 'implementation', 'scale-source', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise ValueError('Do not overwrite a completed diagnostic')
    m = load('actual_gradient_diagnostic_batch', args.implementation)
    sm = load('actual_gradient_diagnostic_scale', args.scale_source)
    data = np.load(args.bundle, allow_pickle=False)
    M = (data['qjets'].shape[-1]-2)//3
    pos = (args.operator, data['mesh'], data['a_stages'], float(data['radius']), data['fixed_core_first3'])
    kw = dict(M=M, N=2048, width=float(data['width']), stage_block=64)
    full, quarter = m.create(*pos, quarter=False, **kw), m.create(*pos, quarter=True, **kw)
    x, _ = full.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    full.set_base(x)
    quarter.set_base(x)
    rfull, rquarter = full.residual(x), quarter.residual(x)
    W = np.array([1., 2., 1.])
    gf, gq = full.vjp(x, rfull*W), quarter.vjp(x, rquarter*W)
    difference = gf-gq
    index = int(np.argmax(np.abs(difference)))
    S = sm.local_scale(full)
    h = np.diff(full.mesh)
    min_index = int(np.argmin(h))
    scaled_full, scaled_quarter = S*gf, S*gq
    scaled_index = int(np.argmax(np.abs(scaled_full-scaled_quarter)))
    rng = np.random.default_rng(20261120)
    z = rng.standard_normal(full.free_size)/np.sqrt(full.free_size)
    direction = S*z
    jf, jq = full.jvp(x, direction), quarter.jvp(x, direction)
    lhs_f, rhs_f = float(np.sum(jf*rfull*W)), float(np.dot(direction, gf))
    lhs_q, rhs_q = float(np.sum(jq*rquarter*W)), float(np.dot(direction, gq))
    report = dict(
        schema='actual-full-quarter-gradient-scaling-diagnostic-20261120-v1',
        source_sha256=sha(__file__), implementation_sha256=sha(args.implementation),
        scale_source_sha256=sha(args.scale_source), bundle_sha256=sha(args.bundle),
        original_diagnostic_threshold_not_changed=True, no_new_acceptance_gate=True,
        original_raw_relative=rel(gf, gq),
        full_raw_gradient_norm=float(np.linalg.norm(gf)),
        quarter_raw_gradient_norm=float(np.linalg.norm(gq)),
        difference_norm=float(np.linalg.norm(difference)),
        max_absolute_difference=float(abs(difference[index])),
        maximum_difference_free_index=index,
        maximum_difference_coordinate=decode_coordinate(full, index),
        full_value_at_max_difference=float(gf[index]),
        quarter_value_at_max_difference=float(gq[index]),
        scale_at_max_difference=float(S[index]),
        minimum_mesh_h=float(h[min_index]),minimum_mesh_cell=min_index,
        minimum_mesh_interval=[float(full.mesh[min_index]),float(full.mesh[min_index+1])],
        local_scaled_gradient_relative=rel(scaled_full, scaled_quarter),
        full_scaled_gradient_norm=float(np.linalg.norm(scaled_full)),
        quarter_scaled_gradient_norm=float(np.linalg.norm(scaled_quarter)),
        scaled_difference_norm=float(np.linalg.norm(scaled_full-scaled_quarter)),
        scaled_max_difference=float(abs(scaled_full[scaled_index]-scaled_quarter[scaled_index])),
        scaled_max_difference_coordinate=decode_coordinate(full, scaled_index),
        direct_Jv_direction_seed=20261120,
        direction_definition='local_scale * standard_normal(free_size) / sqrt(free_size)',
        full_direct_Jv_inner_product=lhs_f,full_gradient_inner_product=rhs_f,
        full_bilinear_relative=scalar_rel(lhs_f,rhs_f),
        quarter_direct_Jv_inner_product=lhs_q,quarter_gradient_inner_product=rhs_q,
        quarter_bilinear_relative=scalar_rel(lhs_q,rhs_q),
        full_quarter_direct_Jv_inner_product_relative=scalar_rel(lhs_f,lhs_q),
        full_quarter_gradient_inner_product_relative=scalar_rel(rhs_f,rhs_q),
        scope='Floating observations at one actual point; not a rigorous roundoff upper bound or a new scientific acceptance rule')
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
