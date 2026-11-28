#!/usr/bin/env python3
"""Resume unchanged v2 tail metric mathematics with a separate small-file storage gate.

The predecessor was explicitly interrupted only during its 128 MiB write wait.
All complete stage receipts and every durable partial leaf keep their original
bytes/source/contract. New receipts identify this v3 controller and its actual
16 MiB plus serialized-write reservation. The old mathematical target, full
field, Fourier spectrum, all Gram terms, Taylor remainder and strict 1e-6 gate
are unchanged. This controller delegates all mathematical routines to frozen v2.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import tail_metric_complete_supplement_v2 as v2
from tail_metric_complete_supplement_v2 import (
    v1, original, kernel, V1_SHA, GATE, ref, write, checked_plain, upward,
    selected_data, actual_source_knots, true_w_at_actual_knots,
    exact_cover, seed_leaves, install_disk_guard)

V2_SHA = 'ad10604269a322d33f26f5e9e926d68d06b6ca8f836437ecf0ed585384abd115'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('geometry-bundle', 'constants', 'normalization-certificate', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--original-certificate-dir', type=Path, action='append', required=True)
    p.add_argument('--reuse-taylor-summary', type=Path, action='append', default=[])
    p.add_argument('--max-depth', type=int, default=3)
    p.add_argument('--quadratic-mode-cutoff', type=int, default=12)
    p.add_argument('--disk-reserve-mib', type=int, default=16)
    p.add_argument('--inherit-v2-terminal', type=Path, required=True)
    p.add_argument('--resume', action='store_true')
    args = p.parse_args()
    if (not 0 <= args.max_depth <= 12 or args.quadratic_mode_cutoff < 0
            or args.disk_reserve_mib < 16):
        raise ValueError('Preserve the proof and all quadratic products; small proof writes require at least 16 MiB plus their real serialized length')
    if ref(v1.__file__)['sha256'] != V1_SHA:
        raise ValueError('The reviewed frozen Taylor Gram proof changed')
    if ref(kernel.__file__)['sha256'] != v1.ORIGINAL_KERNEL_SHA:
        raise ValueError('The reviewed original exact Gram kernel changed')
    if ref(v2.__file__)['sha256'] != V2_SHA:
        raise ValueError('The unchanged original v2 mathematical controller changed')
    terminal_ref = ref(args.inherit_v2_terminal)
    terminal = checked_plain(terminal_ref)
    if (terminal['status'] != 'owned_v2_write_wait_interrupted_for_independent_small_file_storage_successor'
            or terminal['actual_returncode'] != 130
            or not terminal['old_process_is_no_longer_running']
            or not terminal['old_durable_full_SHA_and_size_reverified_after_exit']):
        raise ValueError('An actually stopped owned predecessor with intact durable evidence is required')
    before = checked_plain(terminal['before'])
    previous_root = Path(terminal['old_root']).resolve()
    previous_contract_ref = ref(previous_root/'contract.json')
    if previous_contract_ref['sha256'] != terminal['old_contract']['sha256']:
        raise ValueError('The original v2 proof contract changed')
    previous_contract = checked_plain(previous_contract_ref)
    previous_summary = checked_plain(before['old_summary_snapshot'])
    if previous_summary['contract'] != previous_contract_ref:
        raise ValueError('The saved predecessor summary binds another actual proof contract')
    previous_completed = {row['stage']:row for row in previous_summary['stages']}
    previous_durable = {row['path']:row for row in before['durable_proof_files']}
    for name, item in previous_durable.items():
        raw = Path(name).read_bytes()
        if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise ValueError('A frozen actual predecessor proof changed: '+name)
    out = args.outdir.resolve()
    if out == previous_root or previous_root in out.parents:
        raise ValueError('The new execution must have an independent output root')
    out.mkdir(parents=True, exist_ok=args.resume)
    guard = install_disk_guard(out, args.disk_reserve_mib*1024**2)
    bundle, chain, manifest, index, constants = original.validate_inputs(
        args.geometry_bundle, args.constants, args.normalization_certificate)
    files = {row['stage']: row for row in manifest['files']}
    if (not index['all_stages_exported'] or not bundle['all_stages_exported']
            or set(files) != set(range(index['finite_stage_count']))):
        raise ValueError('A true complete original finite-tail bundle is required')
    oracle = v1.Q060TrueBackgroundOracle(args.constants, args.normalization_certificate)
    bundle_ref = ref(args.geometry_bundle)
    contract = dict(schema='same-actual-finite-tail-metric-supplement-storage-v3',
                    source=ref(__file__), Taylor_Gram_source=ref(v1.__file__),
                    original_Gram_source=ref(kernel.__file__),
                    original_validator=ref(original.__file__), geometry_bundle=bundle_ref,
                    shared_R_manifest=bundle['shared_R_manifest'],
                    spectrum_contract=bundle['spectrum_contract'],
                    accepted_packet=bundle['accepted_packet'], entire_mean=bundle['mean_chain'],
                    constants=ref(args.constants), normalization=ref(args.normalization_certificate),
                    oracle_provenance=oracle.provenance, exact_metric_gate=str(GATE),
                    quadratic_mode_cutoff=args.quadratic_mode_cutoff,
                    max_proof_depth=args.max_depth, disk_guard=guard,
                    original_certificate_directories=[str(x.resolve()) for x in args.original_certificate_dir],
                    seed_Taylor_summaries=[ref(x) for x in args.reuse_taylor_summary])
    ignored = {'schema', 'source', 'disk_guard'}
    old_math = {k:v for k,v in previous_contract.items() if k not in ignored}
    new_math = {k:v for k,v in contract.items() if k not in ignored}
    if old_math != new_math:
        raise ValueError('Only the actual controller identity and independent storage gate may differ')
    contract.update(original_mathematical_controller=ref(v2.__file__),
                    inherited_v2_contract=previous_contract_ref,
                    actual_storage_handoff=terminal_ref,
                    predecessor_proof_parameters_identical=True,
                    predecessor_proof_output_bytes_unchanged=True)
    contract_path = out/'contract.json'
    if args.resume:
        if json.loads(contract_path.read_text()) != contract:
            raise ValueError('Resume must keep every complete field, proof, and source binding')
    else:
        write(contract_path, contract)
    contract_ref = ref(contract_path)
    seeds = seed_leaves(args.reuse_taylor_summary, bundle_ref, bundle, files, oracle)
    result = dict(status='running', contract=contract_ref, stages=[],
                  finite_stage_count=len(files), original_literal_span_count=sum(x['nodes']-1 for x in files.values()),
                  field_mean_spectrum_or_target_changed=False,
                  original_passed_metric_spans_recomputed=False,
                  original_geometric_or_curvature_bounds_recomputed=False,
                  proof_interval_subdivision_only=True,
                  complete_finite_chain_metric_certified=False,
                  deep_collar_metric_claimed=False, whole_tail_metric_claimed=False,
                  absolute_placement_claimed=False, complete_closed_surface_claimed=False)
    summary = out/'summary.json'
    write(summary, result)
    result.update(inherited_v2_contract=previous_contract_ref,
                  actual_storage_handoff=terminal_ref,
                  actual_small_file_disk_guard=guard,
                  old_complete_stage_certificates_reused=0,
                  old_partial_stage_Taylor_leaves_reused=0,
                  old_v2_source_or_128MiB_guard_modified=False)
    start = time.monotonic()
    try:
        for stage, entry in sorted(files.items()):
            old_path = None
            while old_path is None:
                candidates = [directory/f'stage-{stage:04d}.json' for directory in args.original_certificate_dir]
                present = [path for path in candidates if path.exists()]
                if len(present) > 1:
                    if len({ref(path)['sha256'] for path in present}) != 1:
                        raise ValueError('Conflicting original certificates for a stage')
                if present:
                    try:
                        old = json.loads(present[0].read_text())
                    except json.JSONDecodeError:
                        time.sleep(2)
                        continue
                    old_path = present[0]
                else:
                    print(json.dumps(dict(event='waiting_for_original_stage_certificate', stage=stage)), flush=True)
                    time.sleep(5)
            old_ref = ref(old_path)
            old = checked_plain(old_ref)
            data = selected_data(bundle, manifest, constants, entry)
            if (old['stage'] != stage or old['data'] != entry
                    or old['map_hash'] != entry['mapHash']
                    or old['spans'] != len(data['nodes'])-1
                    or [row['span'] for row in old['rows']] != list(range(old['spans']))):
                raise ValueError('Original certificate does not cover this unchanged complete stage')
            radii = [Q.from_float(node['radiusJS']) for node in data['nodes']]
            for row in old['rows']:
                j = row['span']
                if list(map(Q, row['R_exact'])) != radii[j:j+2]:
                    raise ValueError('Original certificate uses other literal radial knots')
            if stage in previous_completed:
                inherited = previous_completed[stage]
                certificate = checked_plain(inherited['certificate'])
                if (certificate['contract'] != previous_contract_ref
                        or certificate['actual_data'] != entry
                        or certificate['stage'] != stage
                        or certificate['original_certificate'] != old_ref
                        or not certificate['all_original_selected_input_gates_checked']
                        or not certificate['all_original_spans_covered_exactly']
                        or [r['original_span'] for r in certificate['spans']] != list(range(len(data['nodes'])-1))
                        or not certificate['metric_gate_passed']
                        or not inherited['metric_gate_passed']):
                    raise ValueError('A completed predecessor stage is not the same proved complete stage')
                inherited_peak = max(Q(r['metric_upper_exact']) for r in certificate['spans'])
                if inherited_peak != Q(certificate['metric_upper_exact']) or inherited_peak >= GATE:
                    raise ValueError('The actual predecessor stage gate was not passed')
                for r in certificate['spans']:
                    if not r['metric_gate_passed']:
                        raise ValueError('An inherited complete stage contains an unpaid span')
                result['stages'].append(dict(inherited, inherited_complete_v2_stage=True))
                result['old_complete_stage_certificates_reused'] += 1
                result['seconds_this_process'] = time.monotonic()-start
                write(summary, result)
                print(json.dumps(dict(event='prior_complete_v2_metric_stage_reused',stage=stage,
                                      metric_upper=upward(inherited_peak),prior_certificate=inherited['certificate'],
                                      Gram_polynomial_or_Taylor_leaf_recomputed=False)),flush=True)
                continue
            stage_dir = out/f'stage-{stage:04d}'
            stage_dir.mkdir(exist_ok=True)
            stage_result = dict(stage=stage, contract=contract_ref, actual_data=entry,
                                original_certificate=old_ref,
                                all_original_selected_input_gates_checked=True,
                                spans=[], original_geometric_bounds_reused_from=old_ref)
            pending = [row['span'] for row in old['rows']
                       if Q(row['metric_upper_exact']) >= GATE and (stage,row['span']) not in seeds]
            if pending:
                pm, hm, spans, identities = kernel.prepare(data)
                knots = actual_source_knots(data)
                _, w0, dw = kernel.local_background_cover(oracle, data)
                baseline = kernel.gram_span(spans[pending[0]], pm, hm, w0, dw, args.quadratic_mode_cutoff)
                constant = v1.gram_span_variable(spans[pending[0]], pm, hm, [w0], dw, args.quadratic_mode_cutoff)
                if any(baseline[key] != constant[key] for key in
                       ('metric','components','merged','quadratic_remainder')):
                    raise ArithmeticError('Constant-w specialization lost original exact equality')
                stage_result.update(exact_original_endpoint_scalar_identities=identities,
                                    constant_w_specialization_exactly_original=True,
                                    actual_source_knots_preserved=True)

            def visit(j, left, right, depth):
                name = hashlib.sha256(f'{j}:{left}:{right}'.encode()).hexdigest()[:24]
                path = stage_dir/('Taylor-'+name+'.json')
                span = v1.restricted_span(spans[j], left, right, pm, hm)
                expected_contract = contract_ref
                inherited_leaf = False
                old_leaf = previous_root/f'stage-{stage:04d}'/path.name
                if not path.exists() and old_leaf.exists():
                    bound = previous_durable.get(str(old_leaf))
                    if (bound is None or ref(old_leaf)['sha256'] != bound['sha256']):
                        raise ValueError('An old partial-stage leaf was not in the preserved actual inventory')
                    path, expected_contract, inherited_leaf = old_leaf, previous_contract_ref, True
                if path.exists():
                    row = json.loads(path.read_text())
                    if (row['contract'] != expected_contract or row['stage'] != stage
                            or row['actual_map_hash'] != entry['mapHash']
                            or row['original_span'] != j or row['proof_t'] != list(map(str,(left,right)))
                            or row['literal_R_interval_exact'] != list(map(str,(span['r0'],span['r1'])))):
                        raise ValueError('Durable proof leaf is not this same subinterval')
                else:
                    W, error, background = true_w_at_actual_knots(oracle, data, span, left, right, j, knots)
                    bound = v1.gram_span_variable(span, pm, hm, W, error, args.quadratic_mode_cutoff)
                    row = dict(contract=contract_ref, stage=stage, actual_map_hash=entry['mapHash'],
                               original_span=j, proof_t=list(map(str,(left,right))), depth=depth,
                               literal_R_interval_exact=list(map(str,(span['r0'],span['r1']))),
                               true_w_linear_Taylor=background,
                               metric_upper_exact=str(bound['metric']), metric_upper=upward(bound['metric']),
                               exact_Gram_component_upper=list(map(str,bound['components'])),
                               exact_merged_Fourier_upper=list(map(str,bound['merged'])),
                               exact_complete_quadratic_remainder=list(map(str,bound['quadratic_remainder'])),
                               metric_gate_passed=bound['metric'] < GATE)
                    write(path, row)
                if row['metric_gate_passed'] != (Q(row['metric_upper_exact']) < GATE):
                    raise ValueError('Persisted exact metric gate differs')
                if not row['metric_gate_passed'] and depth < args.max_depth:
                    middle = (left+right)/2
                    return visit(j,left,middle,depth+1)+visit(j,middle,right,depth+1)
                if inherited_leaf:
                    result['old_partial_stage_Taylor_leaves_reused'] += 1
                leaf = dict(certificate=ref(path), original_span=j, proof_t=row['proof_t'],
                            metric_upper_exact=row['metric_upper_exact'],
                            metric_gate_passed=row['metric_gate_passed'], reused=inherited_leaf,
                            storage_predecessor_leaf=inherited_leaf)
                print(json.dumps(dict(event='actual_metric_supplement_leaf', stage=stage, span=j,
                                      depth=depth, metric_upper=upward(row['metric_upper_exact']),
                                      passed=row['metric_gate_passed'])), flush=True)
                return [leaf]

            for old_row in old['rows']:
                j = old_row['span']
                if Q(old_row['metric_upper_exact']) < GATE:
                    row = dict(original_span=j, origin='unchanged_original_certificate',
                               certificate=old_ref, metric_upper_exact=old_row['metric_upper_exact'],
                               metric_gate_passed=True)
                else:
                    if (stage,j) in seeds:
                        leaves = seeds[(stage,j)]
                        for leaf in leaves:
                            a,b = map(Q,leaf['proof_t'])
                            if list(map(Q,leaf['literal_R_interval_exact'])) != [radii[j]+(radii[j+1]-radii[j])*a,radii[j]+(radii[j+1]-radii[j])*b]:
                                raise ValueError('Reused Taylor leaf uses other exact original radii')
                    else:
                        leaves = visit(j,Q(0),Q(1),0)
                    if not exact_cover(leaves):
                        raise ArithmeticError('Supplement proof leaves do not cover the original span exactly')
                    peak = max(Q(leaf['metric_upper_exact']) for leaf in leaves)
                    row = dict(original_span=j, origin='same_map_true_w_Taylor', leaves=leaves,
                               metric_upper_exact=str(peak), metric_gate_passed=peak < GATE)
                stage_result['spans'].append(row)
                if row['origin'] == 'same_map_true_w_Taylor':
                    write(stage_dir/'progress.json', stage_result)
            peak = max(Q(row['metric_upper_exact']) for row in stage_result['spans'])
            stage_result.update(all_original_spans_covered_exactly=True,
                                metric_upper_exact=str(peak), metric_upper=upward(peak),
                                metric_gate_passed=peak < GATE)
            stage_path = stage_dir/'certificate.json'
            write(stage_path, stage_result)
            result['stages'].append(dict(stage=stage, certificate=ref(stage_path),
                                         spans=len(stage_result['spans']), metric_upper=upward(peak),
                                         metric_gate_passed=peak < GATE,
                                         original_passed_spans_reused=sum(row['origin']=='unchanged_original_certificate' for row in stage_result['spans']),
                                         Taylor_spans=sum(row['origin']=='same_map_true_w_Taylor' for row in stage_result['spans'])))
            result['seconds_this_process']=time.monotonic()-start
            write(summary, result)
            print(json.dumps(dict(event='actual_metric_supplement_stage', stage=stage,
                                  metric_upper=upward(peak), passed=peak < GATE)),flush=True)
        if sum(row['spans'] for row in result['stages']) != result['original_literal_span_count']:
            raise ArithmeticError('The complete literal finite-span inventory was not preserved')
        passed = all(row['metric_gate_passed'] for row in result['stages'])
        result.update(status='same_actual_complete_finite_tail_metric_certified' if passed else 'same_actual_finite_tail_metric_supplement_incomplete',
                      complete_finite_chain_metric_certified=passed,
                      maximum_metric_upper=max(row['metric_upper'] for row in result['stages']),
                      original_passed_spans_reused=sum(row['original_passed_spans_reused'] for row in result['stages']),
                      Taylor_spans=sum(row['Taylor_spans'] for row in result['stages']),
                      seconds_this_process=time.monotonic()-start)
    except Exception as exc:
        result.update(status='metric_supplement_execution_failed', error=repr(exc),
                      seconds_this_process=time.monotonic()-start)
        write(summary,result)
        raise
    write(summary,result)
    print(json.dumps(dict(status=result['status'], summary=ref(summary),
                          complete_finite_chain_metric_certified=result['complete_finite_chain_metric_certified'])),flush=True)


if __name__ == '__main__':
    main()
