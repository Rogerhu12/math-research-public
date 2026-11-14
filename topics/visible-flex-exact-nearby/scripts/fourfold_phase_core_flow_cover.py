#!/usr/bin/env python3
"""Bounded-memory complete pieces of the actual parameter-uniform core flow.

Each original common span is kept exactly. Failed analytic boxes are bisected
as real subintervals of the same fixed scalar germ, and every resulting leaf
is saved independently. Missing or failed leaves never produce a complete
piece. The worker does not assemble a core DN map or a Schur inverse.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import traceback

import numpy as np
from flint import arb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_parameter_taylor import ParameterCoreTarget, core_provenance
from fourfold_phase_core_cell_flow import local_flow


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def finite_json(path):
    def reject(value):
        raise ValueError('nonfinite JSON constant '+value)
    return json.loads(Path(path).read_text(), parse_constant=reject)


def save(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--first-span', type=int, required=True)
    ap.add_argument('--last-span', type=int, required=True)
    ap.add_argument('--parameter-half-width', type=Fraction, default=Fraction(1, 10**9))
    ap.add_argument('--modes', type=int, default=4)
    ap.add_argument('--primitive-nodes', type=int, default=512)
    ap.add_argument('--angles', type=int, default=1024)
    ap.add_argument('--bits', type=int, default=192)
    ap.add_argument('--native-order', type=int, default=32)
    ap.add_argument('--native-radius', type=Fraction, default=Fraction(1, 64))
    ap.add_argument('--outer-radius', type=Fraction, default=Fraction(3))
    ap.add_argument('--sample-radius', type=Fraction, default=Fraction(5, 4))
    ap.add_argument('--time-nodes', type=int, default=40)
    ap.add_argument('--time-terms', type=int, default=24)
    ap.add_argument('--flow-degree', type=int, default=32)
    ap.add_argument('--normalized-strip', type=Fraction, default=Fraction(1, 16))
    ap.add_argument('--momentum-scale', type=Fraction, default=Fraction(8))
    ap.add_argument('--max-depth', type=int, default=8)
    ap.add_argument('--out-dir', type=Path, required=True)
    args = ap.parse_args()
    ctx.prec, ctx.cap = args.bits, 4
    if not args.parameter_half_width > 0:
        raise ValueError('this complete cover requires its explicit positive family half-width')
    wall, cpu = time.monotonic(), time.process_time()
    source_dir = Path(__file__).parent
    dependencies = [
        'fourfold_phase_core_cell_flow.py','fourfold_phase_core_radial_taylor.py',
        'fourfold_phase_core_waist_taylor.py','fourfold_phase_core_parameter_taylor.py',
        'fourfold_phase_beta_parameter_germ.py','fourfold_native_series_fft.py',
        'fourfold_phase_beta_affine.py','fourfold_phase_beta_bulk_interval.py',
        'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_interval.py',
        'fourfold_phase_core_low_coefficients.py','fourfold_phase_actual_positive_cap.py']
    hashes = {name:sha(source_dir/name) for name in dependencies}
    target = ParameterCoreTarget(args.object, args.parameter_half_width,
        args.primitive_nodes, args.angles, arb('.003'), arb('.0025'), arb('.32'),
        native_order=args.native_order, native_radius=args.native_radius)
    provenance = core_provenance(target, args.object)
    provenance = {key:value for key,value in provenance.items()
                  if key not in ('source_sha256','dependency_sha256')}
    cuts = sorted({Fraction(0), Fraction(1, 4)}
        |{x for x in target.common_cells() if 0 < x < Fraction(1, 4)})
    if not 0 <= args.first_span < args.last_span <= len(cuts)-1:
        raise ValueError('invalid exact common-span range')
    config = dict(modes=args.modes, primitive_nodes=args.primitive_nodes,
        angular_nodes=args.angles, bits=args.bits, native_order=args.native_order,
        native_radius=str(args.native_radius), outer_radius=str(args.outer_radius),
        sample_radius=str(args.sample_radius), time_nodes=args.time_nodes,
        time_terms=args.time_terms, flow_degree=args.flow_degree,
        normalized_angular_strip=str(args.normalized_strip),
        momentum_scale=str(args.momentum_scale))
    identity = dict(**provenance, **config,
        worker_source_sha256=sha(__file__), dependency_sha256=hashes)
    manifest_path = args.out_dir/'manifest.json'
    manifest = dict(kind='complete_piece_of_true_uniform_core_flow',
        complete=False, identity=identity, first_span=args.first_span,
        last_span_exclusive=args.last_span, total_original_common_spans=len(cuts)-1,
        exact_piece_interval=[str(cuts[args.first_span]),str(cuts[args.last_span])],
        original_spans=[], complete_leaves=[], terminal_failures=[], rejected_boxes=[],
        scope='Exactly the declared common-span piece of the true finite angular core family. No omitted interval is assigned zero and no full core DN or full Schur inverse is claimed.')
    args.out_dir.mkdir(parents=True, exist_ok=True)

    def save_manifest():
        manifest.update(CPU_seconds=time.process_time()-cpu,
                        wall_seconds=time.monotonic()-wall)
        save(manifest_path, manifest)

    save_manifest()
    for index in range(args.first_span, args.last_span):
        original_left, original_right = cuts[index:index+2]
        target.set_cell(original_left, original_right)
        manifest['original_spans'].append(
            dict(index=index, exact_interval=[str(original_left),str(original_right)]))
        pending = [(original_left, original_right, '')]
        while pending:
            left, right, word = pending.pop()
            name = 'span_%04d_%s' % (index, word or 'root')
            path = args.out_dir/(name+'.json')
            leaf_identity = dict(**identity, common_span_index=index,
                exact_common_span=[str(original_left),str(original_right)],
                exact_real_interval=[str(left),str(right)])
            # Only byte-bound complete leaves of this identical source/model
            # are reusable. Invalidated NaN reports are rejected by finite_json.
            if path.exists():
                old = finite_json(path)
                if old.get('complete') and old.get('cover_identity') == leaf_identity:
                    arrays = old['arrays']
                    error = arb(old['true_scaled_local_transfer_operator_error']['ball'])
                    if not error.is_finite() or not error >= 0:
                        raise ValueError('saved leaf has no finite true transfer error')
                    if sha(arrays['path']) != arrays['sha256']:
                        raise ValueError('saved leaf exact arrays changed')
                    manifest['complete_leaves'].append(dict(index=index, word=word,
                        exact_interval=[str(left),str(right)], path=str(path),
                        sha256=sha(path), arrays=arrays,
                        transfer_error=old['true_scaled_local_transfer_operator_error']))
                    save_manifest()
                    continue
            local_wall, local_cpu = time.monotonic(), time.process_time()
            report = dict(kind='true_single_common_span_scaled_core_transfer', complete=False,
                **provenance, **config,
                common_span_index=index,
                exact_common_span=[str(original_left),str(original_right)],
                source_sha256=hashes['fourfold_phase_core_cell_flow.py'],
                dependency_sha256=hashes, cover_identity=leaf_identity,
                scheduler_source_sha256=sha(__file__),
                scope='One actual leaf in the parameter-uniform physical core cover; no full Schur inverse.')
            def save_leaf():
                report.update(CPU_seconds=time.process_time()-local_cpu,
                              wall_seconds=time.monotonic()-local_wall)
                save(path, report)
            save_leaf()
            try:
                polynomial, transfer = local_flow(target, left, right, args.modes,
                    exact_arb(args.normalized_strip), args.outer_radius, args.sample_radius,
                    args.time_nodes, args.time_terms, args.flow_degree, args.momentum_scale,
                    report, save_leaf)
                arrays = path.with_suffix('.npz')
                np.savez_compressed(arrays,
                    exact_dyadic_generator_coefficients=polynomial,
                    exact_dyadic_local_transfer_center=transfer)
                del polynomial, transfer
                report.update(complete=True, arrays=dict(path=str(arrays),
                    sha256=sha(arrays),bytes=arrays.stat().st_size))
                save_leaf()
                manifest['complete_leaves'].append(dict(index=index, word=word,
                    exact_interval=[str(left),str(right)], path=str(path), sha256=sha(path),
                    arrays=report['arrays'],
                    transfer_error=report['true_scaled_local_transfer_operator_error']))
                print(json.dumps(dict(stage='completed actual core leaf',
                    span=index, word=word, error=report['true_scaled_local_transfer_operator_error']['ball'])),
                    flush=True)
            except Exception as exc:
                report.update(complete=False,failure=repr(exc),traceback=traceback.format_exc())
                save_leaf()
                failed=dict(index=index,word=word,exact_interval=[str(left),str(right)],
                            path=str(path),sha256=sha(path),failure=repr(exc))
                if len(word) < args.max_depth:
                    manifest['rejected_boxes'].append(failed)
                    midpoint=(left+right)/2
                    pending.extend([(midpoint,right,word+'1'),(left,midpoint,word+'0')])
                else:
                    manifest['terminal_failures'].append(failed)
                print(json.dumps(dict(stage='subdivide actual core leaf',
                    span=index,word=word,failure=repr(exc))),flush=True)
            save_manifest()
    leaves=sorted(manifest['complete_leaves'],key=lambda row:Fraction(row['exact_interval'][0]))
    cursor=cuts[args.first_span]
    for leaf in leaves:
        left,right=map(Fraction,leaf['exact_interval'])
        if left!=cursor or not left<right:
            raise ValueError('the actual completed leaf cover has a gap or overlap')
        cursor=right
    manifest['complete_leaves']=leaves
    manifest['complete']=(cursor==cuts[args.last_span] and not manifest['terminal_failures'])
    save_manifest()
    print(json.dumps(dict(complete=manifest['complete'],first_span=args.first_span,
        last_span=args.last_span,leaves=len(leaves),rejected=len(manifest['rejected_boxes']),
        failures=len(manifest['terminal_failures']),CPU_seconds=manifest['CPU_seconds'])),flush=True)
    if not manifest['complete']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
