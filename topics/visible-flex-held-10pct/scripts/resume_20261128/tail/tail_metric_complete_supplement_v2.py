#!/usr/bin/env python3
"""Complete only unproved metric spans of the unchanged actual finite tail.

Immutable original per-stage certificates supply their already proved spans
and all original geometric bounds.  The frozen true-w Taylor Gram proof pays
only the remaining spans.  No old producer, field, target, or certificate is
modified.  The deep collar and absolute placement remain separate obligations.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import tail_metric_true_w_taylor as v1
from geometry_disk_guard import install as install_disk_guard

original, kernel = v1.original, v1.kernel
V1_SHA = '9b3a6d07cf27149e6af48fb1280d2fbb02a6964af8e00f8cbee4a159edea3e3c'
GATE = Q(1, 10**6)
ref, write = v1.ref, v1.write


def checked_plain(reference):
    path = Path(reference['path'])
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != reference['sha256']:
        raise ValueError('Previously bound proof bytes changed: '+str(path))
    return json.loads(raw)


def upward(value):
    value = Q(value)
    out = float(value)
    return math.nextafter(out, math.inf) if Q.from_float(out) < value else out


def selected_data(bundle, manifest, constants, entry):
    data = original.checked(entry)
    original.validate_spectrum_container(data, bundle['spectrum'], stage=True)
    if (data['spectrumContract'] != bundle['spectrum_contract']
            or data['stage'] != entry['stage']
            or data['sharing']['mapHash'] != entry['mapHash']
            or data['boundInput'] != manifest['input']
            or data['status'] != 'literal_R_stage_with_exact_common_boundary_two_jets'):
        raise ValueError('Original selected finite-stage input identity gate failed')
    if not all(data['physicalParameters'].get(k) == value
               for k, value in constants['parameters'].items()):
        raise ValueError('Original selected physical-background gate failed')
    if len(data['nodes']) != entry['nodes'] or len(data['midpoints']) != entry['midpoints']:
        raise ValueError('The actual nonuniform span inventory differs')
    return data


def actual_source_knots(data):
    result = []
    for node in data['nodes']:
        receiver = node.get('receiverOriginalSource', node)
        if receiver['sourceStage'] != data['stage']:
            raise ValueError('A shared node does not identify this receiving source stage')
        result.append(Q.from_float(receiver['sourceX']))
    if (result[0] != Q.from_float(data['rawLeft'])
            or result[-1] != Q.from_float(data['rawRight'])
            or not all(a < b for a, b in zip(result, result[1:]))):
        raise ValueError('The complete actual source-knot list is not increasing')
    return result


def true_w_at_actual_knots(o, data, span, left, right, parent, knots):
    """The same proved Taylor estimate, with actual node locations as guesses.

Neither this interpolation nor its source anchor asserts an inverse-radius
identity.  The unchanged strict monotone primitive cover proves inclusion.
    """
    source_a, source_b = knots[parent:parent+2]
    xa = source_a + (source_b-source_a)*left
    xb = source_a + (source_b-source_a)*right
    mini = dict(data, rawLeft=float(xa), rawRight=float(xb),
                nodes=[dict(radiusJS=v1.outward_float(span['r0'], False)),
                       dict(radiusJS=v1.outward_float(span['r1'], True))])
    cover, _, _ = kernel.local_background_cover(o, mini)
    anchor_x = (Q.from_float(mini['rawLeft'])+Q.from_float(mini['rawRight']))/2
    anchor = o.local_jets(data['rawCell'], data['rawSegment'], anchor_x)
    radius = o.primitives(data['rawCell'], data['rawSegment'], anchor_x)['r']
    w0, ew = v1.interval_center(o, anchor['w'])
    slope, es = v1.interval_center(o, anchor['h_RR'])
    Rstar, er = v1.interval_center(o, radius)
    second, components = Q(0), []
    anchor_covered = False
    for n, j, aa, bb in cover['source_ranges']:
        aa, bb = Q(aa), Q(bb)
        anchor_covered |= ((n, j) == (data['rawCell'], data['rawSegment'])
                           and aa <= anchor_x <= bb)
        for k in range(8):
            lo, hi = aa+(bb-aa)*Q(k,8), aa+(bb-aa)*Q(k+1,8)
            jets = o.local_jets(n, j, lo, hi)
            rx, rxx = jets['r_x'], jets['r_xx_one_sided_hull']
            if o.lo(rx) <= 0:
                raise ArithmeticError('Strictly positive source-to-R derivative required')
            value = (jets['w_xx']*rx-jets['w_x']*rxx)/(rx**3)
            bound = max(abs(v1.mpf_fraction(o.lo(value))),
                        abs(v1.mpf_fraction(o.hi(value))))
            second = max(second, bound)
            components.append(dict(cell=n, segment=j, source_x=[str(lo), str(hi)],
                                   absolute_w_RR_upper_exact=str(bound)))
    if not anchor_covered:
        raise ArithmeticError('The true Taylor anchor is outside the proved source cover')
    H = max(abs(span['r0']-Rstar), abs(span['r1']-Rstar))+er
    error = ew+es*H+abs(slope)*er+second*H*H/2
    poly = [w0+slope*(span['r0']-Rstar), slope*span['h']]
    proof = dict(original_true_R_cover=cover, anchor_source_x=str(anchor_x),
                 actual_original_source_knots=list(map(str, (source_a, source_b))),
                 anchor_actual_source_piece=[data['rawCell'], data['rawSegment']],
                 actual_anchor_in_proved_source_cover=True,
                 anchor_R_center_exact=str(Rstar), anchor_R_error_exact=str(er),
                 anchor_w_center_exact=str(w0), anchor_w_error_exact=str(ew),
                 anchor_w_R_center_exact=str(slope), anchor_w_R_error_exact=str(es),
                 absolute_w_RR_upper_exact=str(second),
                 absolute_R_minus_true_anchor_upper_exact=str(H),
                 polynomial_in_exact_span_coordinate=list(map(str, poly)),
                 absolute_w_minus_polynomial_upper_exact=str(error),
                 second_derivative_component_bounds=components,
                 true_background_same_R58_C1_w_and_piecewise_second_derivatives=True)
    return poly, error, proof


def exact_cover(rows):
    intervals = sorted((Q(row['proof_t'][0]), Q(row['proof_t'][1])) for row in rows)
    return (bool(intervals) and intervals[0][0] == 0 and intervals[-1][1] == 1
            and all(a < b for a, b in intervals)
            and all(a[1] == b[0] for a, b in zip(intervals, intervals[1:])))


def seed_leaves(paths, bundle_ref, bundle, files, oracle):
    seeds = {}
    for path in paths:
        reference = ref(path)
        value = checked_plain(reference)
        stage = value['stage']
        if (value['source']['sha256'] != V1_SHA
                or value['geometry_bundle'] != bundle_ref
                or value['actual_stage_data'] != files[stage]
                or value['actual_map_hash'] != files[stage]['mapHash']
                or value['accepted_packet'] != bundle['accepted_packet']
                or value['original_entire_mean_chain'] != bundle['mean_chain']
                or value['oracle_provenance'] != oracle.provenance
                or not value['all_selected_spans_covered_exactly']
                or not value['all_selected_metric_gates_passed']):
            raise ValueError('A reused Taylor certificate has a different field or proof scope')
        for row in value['leaves']:
            leaf = checked_plain(row['certificate'])
            if (row['original_span'] != leaf['original_span']
                    or row['proof_t'] != leaf['proof_t']
                    or not leaf['metric_gate_passed']
                    or Q(leaf['metric_operator_upper']['upper_exact']) >= GATE):
                raise ValueError('Reused Taylor leaf did not prove the exact metric gate')
            seeds.setdefault((stage, row['original_span']), []).append(
                dict(certificate=row['certificate'], source_summary=reference,
                     original_span=row['original_span'], proof_t=row['proof_t'],
                     literal_R_interval_exact=leaf['literal_R_interval_exact'],
                     metric_upper_exact=leaf['metric_operator_upper']['upper_exact'],
                     metric_gate_passed=True, reused=True))
    if not all(exact_cover(rows) for rows in seeds.values()):
        raise ValueError('Reused selected Taylor leaves overlap or do not cover a whole span')
    return seeds


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('geometry-bundle', 'constants', 'normalization-certificate', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--original-certificate-dir', type=Path, action='append', required=True)
    p.add_argument('--reuse-taylor-summary', type=Path, action='append', default=[])
    p.add_argument('--max-depth', type=int, default=3)
    p.add_argument('--quadratic-mode-cutoff', type=int, default=12)
    p.add_argument('--disk-reserve-mib', type=int, default=128)
    p.add_argument('--resume', action='store_true')
    args = p.parse_args()
    if (not 0 <= args.max_depth <= 12 or args.quadratic_mode_cutoff < 0
            or args.disk_reserve_mib < 128):
        raise ValueError('Preserve the proof, all quadratic products, and disk reserve')
    if ref(v1.__file__)['sha256'] != V1_SHA:
        raise ValueError('The reviewed frozen Taylor Gram proof changed')
    if ref(kernel.__file__)['sha256'] != v1.ORIGINAL_KERNEL_SHA:
        raise ValueError('The reviewed original exact Gram kernel changed')
    out = args.outdir.resolve()
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
    contract = dict(schema='same-actual-finite-tail-metric-supplement-v2',
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
                if path.exists():
                    row = json.loads(path.read_text())
                    if (row['contract'] != contract_ref or row['stage'] != stage
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
                leaf = dict(certificate=ref(path), original_span=j, proof_t=row['proof_t'],
                            metric_upper_exact=row['metric_upper_exact'],
                            metric_gate_passed=row['metric_gate_passed'], reused=False)
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
