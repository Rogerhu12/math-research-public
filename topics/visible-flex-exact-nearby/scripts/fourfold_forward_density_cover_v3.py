#!/usr/bin/env python3
"""Continue the exact forward density cover as proved field domains arrive.

Each completed leaf is a genuine continuous true-density certificate.  The
controller pays every local quadratic term and keeps every cross-leaf Fourier
mode.  It can reuse completed certificates from the two original pilots only
after matching the complete finite reference, time interval, field object,
source and dependencies.  A growing prefix is never called a full return.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction
import gc
import hashlib
from pathlib import Path
import time
import traceback

from flint import arb, acb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_domain_cover_verify import Closure, Time
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_phase_unified_scalar_time_circle import exact_time
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_density_pipeline_optimal_time_v6 import (
    run_leaf, save, decode_ball, add_ordered_segment, save_accumulator,
    coefficient_norms, checked_extended_domain,
)
from fourfold_forward_density_pipeline_expanded_time_v5 import checked_extended_domain as checked_v5_domain


def check_reference_seams(path, descriptor, reference):
    """Bind the existing exact 549-seam proof to this very reference."""
    summary = read(path)
    report_path = Path(summary['report'])
    if sha(report_path) != summary['report_sha256']:
        raise ValueError('full-reference seam report changed')
    report = read(report_path)
    identity = summary['identity']
    if (not summary.get('complete') or not summary.get('all_550_segments_passed')
        or not summary.get('all_549_base_seams_bitwise_checked')
        or not summary.get('all_549_Q_seams_bitwise_checked')
        or summary['segment_count'] != 550
        or identity['retarget_descriptor_sha256'] != sha(descriptor)
        or identity['manifest_sha256'] != reference.doc['old_forward_reference']['sha256']
        or identity['leg'] != 'forward' or report['identity'] != identity):
        raise ValueError('the complete exact reference/seam proof has a different identity')
    return dict(path=str(path), sha256=sha(path), report_path=str(report_path),
                report_sha256=sha(report_path), all_549_base_and_Q_seams_exact=True)


def load_cover(path, descriptor, reference, closure):
    index = read(path)
    if (index['retarget_descriptor_sha256'] != sha(descriptor)
        or index['target_object_sha256'] != reference.doc['target_object']['sha256']
        or index['target_root_sha256'] != reference.doc['target_root']['sha256']):
        raise ValueError('field-domain cover belongs to another exact target')
    if 'forward' not in index['time_grid_sha256'] or any(
            leg not in ('forward','backward') for leg in index['time_grid_sha256']):
        raise ValueError('field cover has no forward grid or an unknown leg')
    for leg in index['time_grid_sha256']:
        item = reference.doc['old_'+leg+'_reference']
        if index['time_grid_sha256'][leg] != item['sha256']:
            raise ValueError('field-domain cover time-grid mismatch')
    closure.check_sources(index)
    requested = [tuple(row) for row in index['requested_cases']]
    if len(requested) != len(set(requested)):
        raise ValueError('duplicate field-cover request')
    cases = {}
    for case in index['cases']:
        key = case['leg'], int(case['segment'])
        if key in cases or key not in requested or not case.get('proved'):
            raise ValueError('duplicate, unrequested or unproved completed cover case')
        cases[key] = case
    return index, cases


def exact_case_leaves(case, index, grid, closure):
    leg, segment = case['leg'], int(case['segment'])
    a, b = map(Time.parse, grid['exact_time_endpoints'][segment:segment+2])
    leaves = []
    for row in case['leaves']:
        left, right = map(Fraction, row['normalized_subspan'])
        if not 0 <= left < right <= 1:
            raise ValueError('invalid normalized leaf interval')
        doc = closure.domain(row['path'], row['sha256'])
        if (doc['leg'] != leg or int(doc['segment']) != segment
            or doc['branch_sign'] != grid['trace_identity']['sign']
            or doc['source_sha256'] != index['source_sha256']
            or list(map(Fraction, doc['normalized_subspan'])) != [left, right]
            or list(map(Time.parse, doc['exact_time_endpoints'])) !=
                [a+(b-a).scale(left), a+(b-a).scale(right)]
            or doc['time_grid_manifest_sha256'] != index['time_grid_sha256'][leg]):
            raise ValueError('field-domain leaf does not cover its claimed exact time span')
        for key in ('time_radius', 'larger_time_radius', 'physical_theta_strip',
                    'wider_physical_theta_strip', 'primitive_nodes',
                    'independent_root_nodes', 'angles', 'cutoff', 'time_order',
                    'bits', 'R59_sha256'):
            if doc.get(key) != index.get(key):
                raise ValueError('field-domain leaf/cover mismatch: '+key)
        leaves.append((left, right, Path(row['path']), row['sha256'], doc))
    leaves.sort(key=lambda row: row[0])
    if (not leaves or leaves[0][0] != 0 or leaves[-1][1] != 1
        or any(a[1] != b[0] for a, b in zip(leaves, leaves[1:]))):
        raise ValueError('completed case has a time gap or overlap')
    return leaves


def validate_saved(path, reference, args, closure, allowed_sources):
    report = read(path)
    if not report.get('complete') or not report.get('complete_continuous_true_density_proved'):
        raise ValueError('the saved density certificate is not complete')
    source = report['source_sha256']
    if source not in allowed_sources or sha(allowed_sources[source]) != source:
        raise ValueError('the saved density source is absent or has changed')
    if (Fraction(report['label_strip']) != Fraction(args.label_strip)
        or Fraction(report['inner_strip']) != Fraction(args.inner_strip)):
        raise ValueError('saved density uses different nested label strips')
    for name, wanted in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name)) != wanted:
            raise ValueError('saved density dependency differs: '+name)
    doc = closure.domain(report['domain_path'], report['domain_sha256'])
    enlarged=report.get('expanded_true_field_domain')
    if enlarged and enlarged['proved']:
        if sha(enlarged['path'])!=enlarged['sha256']:
            raise ValueError('saved enlarged true field domain changed')
        checker=(checked_extended_domain if allowed_sources[source].name==
                 'fourfold_forward_density_pipeline_optimal_time_v6.py' else checked_v5_domain)
        checker(enlarged['path'],report['domain_path'],enlarged['selected_germ_index'],closure)
    left, right = map(Fraction, doc['normalized_subspan'])
    current = CompleteReferenceSegment(reference, 'forward', int(doc['segment']), left, right)
    if (doc['leg'] != 'forward' or report['identity']['reference'] != current.identity
        or report['identity']['field']['descriptor_sha256'] != sha(args.descriptor)
        or report['identity']['field']['domain_sha256'] != report['domain_sha256']
        or tuple(map(exact_time, report['identity']['exact_time_endpoints'])) !=
            tuple(map(exact_time, doc['exact_time_endpoints']))):
        raise ValueError('saved true density has a different exact reference or field interval')
    first_row = report['first_integral_file']
    if sha(first_row['path']) != first_row['sha256']:
        raise ValueError('saved exact first integral changed')
    first_doc = read(first_row['path'])
    if (first_doc['identity'] != report['identity']
        or first_doc['density_coefficient_sha256'] != report['density_coefficient_sha256']):
        raise ValueError('saved first integral belongs to a different finite density')
    first = [decode_ball(row) for row in first_doc['coefficients']]
    if not first or any(not z.is_finite() for z in first):
        raise ValueError('saved first integral has nonfinite coefficients')
    return report, first, doc


def main():
    p = argparse.ArgumentParser(description=__doc__)
    base = Path('data/phase_ring_continuation')
    p.add_argument('--descriptor', type=Path, default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--cover', type=Path, default=base/'type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward.json.gz')
    p.add_argument('--out-directory', type=Path, default=base/'step5_forward_density_complete')
    p.add_argument('--reference-seams', type=Path, default=Path('notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'))
    p.add_argument('--real-gate-directory', type=Path, default=base/'step5_complete_reference_real_time_gates_forward')
    p.add_argument('--expanded-domain-directory', type=Path, default=base/'step5_expanded_time_domain_full')
    p.add_argument('--seed', type=Path, action='append', default=[])
    p.add_argument('--label-strip', default='1/256')
    p.add_argument('--inner-strip', default='3/1024')
    p.add_argument('--target', default='1e-20')
    p.add_argument('--circle-radius', default='1')
    p.add_argument('--outer-domains', default='6:1/64,3:1/64,2:1/32,3/2:1/32')
    p.add_argument('--gate-nodes', type=int, default=512)
    p.add_argument('--gate-order', type=int, default=8)
    p.add_argument('--primitive-nodes', type=int, default=1024)
    p.add_argument('--root-nodes', type=int, default=1024)
    p.add_argument('--turn-primitive-nodes', type=int, default=512)
    p.add_argument('--turn-root-nodes', type=int, default=512)
    p.add_argument('--radial-degree', type=int, default=96)
    p.add_argument('--bits', type=int, default=320)
    p.add_argument('--coefficient-bits', type=int, default=128)
    p.add_argument('--max-degree', type=int, default=8191)
    p.add_argument('--max-terms', type=int, default=160)
    p.add_argument('--anchors', type=int, default=512)
    p.add_argument('--evaluation-tail', default='1e-36')
    p.add_argument('--preserve-rectangles', action='store_true')
    p.add_argument('--follow', action='store_true')
    p.add_argument('--wait-seconds', type=float, default=20)
    p.add_argument('--stop-segment', type=int, default=550)
    p.add_argument('--stop-file',type=Path)
    args = p.parse_args()
    if not 0 < args.stop_segment <= 550 or not 0 < args.wait_seconds <= 60:
        raise ValueError('invalid stop segment or wait interval')
    ctx.prec = args.bits
    ctx.cap = 24
    args.out_directory.mkdir(parents=True, exist_ok=True)
    reference = RetargetReference(args.descriptor)
    closure = Closure(Path.cwd(), reference.doc['target_object']['sha256'],
                      reference.doc['target_root']['sha256'])
    for key in ('target_object', 'target_root', 'old_forward_reference', 'old_backward_reference'):
        item = reference.doc[key]
        closure.read(item['path'], item['sha256'], key)
    grid = read(reference.doc['old_forward_reference']['path'])
    if len(grid['exact_time_endpoints']) != 551:
        raise ValueError('this reference does not have the expected 550 exact segments')
    seams = check_reference_seams(args.reference_seams, args.descriptor, reference)
    sources = [Path(__file__).with_name(name) for name in (
        'fourfold_forward_density_pipeline_optimal_time_v6.py',
        'fourfold_forward_density_pipeline_expanded_time_v5.py',
        'fourfold_forward_density_pipeline_minimal_time.py',
        'fourfold_forward_density_pipeline_Q1024_v3.py',
        'fourfold_forward_density_pipeline_turn0_v1.py')]
    allowed_sources = {sha(path): path for path in sources}
    seeds = {}
    for path in args.seed:
        report, first, doc = validate_saved(path, reference, args, closure, allowed_sources)
        key = (int(doc['segment']), *map(Fraction, doc['normalized_subspan']))
        if key in seeds:
            raise ValueError('duplicate seed interval')
        seeds[key] = (path, report, first, doc)
    C1, C2 = [acb(0)], [acb(0)]
    A, E, local_J = arb(0), arb(0), arb(0)
    last = PiTime(Fraction(0), Fraction(-1, 2))
    index_path = args.out_directory/'index.json'
    old = read(index_path) if index_path.exists() else None
    previous_controllers=[Path(__file__).with_name(name) for name in
        ('fourfold_forward_density_cover.py','fourfold_forward_density_cover_v2.py')]
    allowed_controllers={sha(__file__),*[sha(path) for path in previous_controllers]}
    if old is not None and (old['source_sha256'] not in allowed_controllers
            or old['descriptor_sha256'] != sha(args.descriptor)):
        raise ValueError('refuse to resume a different cover controller or exact descriptor')
    old_leaves = {(int(row['segment']), *map(Fraction, row['normalized_subspan'])): row
                  for row in old['leaves']} if old else {}
    index = dict(kind='complete_exact_forward_density_and_ordered_flow', complete=False,
        source_sha256=sha(__file__), descriptor_sha256=sha(args.descriptor),
        pipeline_sources={str(path): digest for digest, path in allowed_sources.items()},
        reference_seams=seams, label_strip=args.label_strip, inner_strip=args.inner_strip,
        exact_initial_time=last.record(), leaves=[], completed_segments=0,
        whole_forward_leg=False, input_cover_snapshots=[])
    if old is not None and old['source_sha256']!=sha(__file__):
        previous_controller=next(path for path in previous_controllers if sha(path)==old['source_sha256'])
        index['resumed_previous_controller']=dict(path=str(previous_controller),
            sha256=old['source_sha256'],completed_segments=old['completed_segments'])
    start = time.monotonic()
    for segment in range(args.stop_segment):
        while True:
            cover, cases = load_cover(args.cover, args.descriptor, reference, closure)
            if ('forward', segment) in cases:
                break
            index['waiting_for_field_domain_segment'] = segment
            index['wall_seconds_this_process'] = time.monotonic()-start
            save(index_path, index)
            if not args.follow:
                print({'stage': 'incomplete_field_cover', 'next_segment': segment}, flush=True)
                return
            print({'stage': 'waiting_for_field_domain', 'next_segment': segment}, flush=True)
            time.sleep(args.wait_seconds)
        index.pop('waiting_for_field_domain_segment', None)
        leaves = exact_case_leaves(cases[('forward', segment)], cover, grid, closure)
        cover_record = dict(path=str(args.cover), sha256=sha(args.cover),
                            completed_cases=len(cover['cases']))
        if not index['input_cover_snapshots'] or index['input_cover_snapshots'][-1] != cover_record:
            index['input_cover_snapshots'].append(cover_record)
        for left, right, domain_path, domain_sha, doc in leaves:
            key = segment, left, right
            suffix = hashlib.sha256((str(left)+':'+str(right)).encode()).hexdigest()[:10]
            output = args.out_directory/f'forward_{segment:04d}_{suffix}.json.gz'
            if key in old_leaves:
                old_row = old_leaves[key]
                output = Path(old_row['path'])
                if sha(output) != old_row['sha256']:
                    raise ValueError('completed prefix density certificate changed')
                report, first, used_doc = validate_saved(output, reference, args, closure, allowed_sources)
                reused = 'completed_prefix'
            elif key in seeds:
                output, report, first, used_doc = seeds.pop(key)
                reused = 'existing_true_density_certificate'
            elif output.exists() and read(output).get('complete'):
                report, first, used_doc = validate_saved(output, reference, args, closure, allowed_sources)
                reused = 'completed_leaf_before_index_checkpoint'
            else:
                if args.stop_file and args.stop_file.exists():
                    index['paused_between_completed_leaves']=True
                    save(index_path,index)
                    print({'stage':'paused_between_completed_leaves',
                           'next_segment':segment,'stop_file':str(args.stop_file)},flush=True)
                    return
                leaf_args=copy.copy(args)
                if all(row.get('curvature',{}).get('kind')=='root_deflated_Q' for row in doc['germs']):
                    leaf_args.primitive_nodes=args.turn_primitive_nodes
                    leaf_args.root_nodes=args.turn_root_nodes
                report, first = run_leaf(domain_path, reference, leaf_args, output)
                used_doc, reused = doc, False
            endpoints = tuple(map(exact_time, used_doc['exact_time_endpoints']))
            if (endpoints != tuple(map(exact_time, doc['exact_time_endpoints']))
                or endpoints[0] != last):
                raise ValueError('true density leaves do not have exact chronological seams')
            inputs = report['R72_inputs']
            A = (A+upper(inputs['common_integrated_majorant_A'])).upper()
            E = (E+upper(inputs['integrated_approximation_error_E'])).upper()
            local_J = (local_J+upper(inputs['omitted_local_second_integral_bound_on_inner_strip'])).upper()
            C1, C2 = add_ordered_segment(C1, C2, first)
            last = endpoints[1]
            gap = exact_arb(Fraction(args.label_strip)-Fraction(args.inner_strip))
            summary = dict(A=ball_record(A), E=ball_record(E), omitted_local_J=ball_record(local_J),
                R=ball_record(gap), R72_smallness_passed=bool(A <= gap/2),
                finite_first_A_inner=ball_record(coefficient_norms([C1], exact_arb(Fraction(args.inner_strip)))[0][0]),
                finite_cross_second_A_inner=ball_record(coefficient_norms([C2], exact_arb(Fraction(args.inner_strip)))[0][0]))
            if A <= gap/2:
                error = (E*(1+A/gap)+A**3/(2*(gap-A)**2)+local_J).upper()
                summary['true_coordinate_flow_error_with_all_local_J_paid'] = ball_record(error)
            else:
                raise ValueError('full prefix exceeds the R72 smallness gate')
            index['leaves'].append(dict(path=str(output), sha256=sha(output), bytes=output.stat().st_size,
                segment=segment, normalized_subspan=[str(left), str(right)], reused=reused,
                current_field_cover_domain=str(domain_path), current_field_cover_domain_sha256=domain_sha))
            accumulator = args.out_directory/'ordered_accumulator.json.gz'
            accumulator_sha = save_accumulator(accumulator, C1, C2,
                dict(descriptor_sha256=sha(args.descriptor), leaves=index['leaves']), summary)
            index.update(summary=summary, exact_final_time=last.record(),
                accumulator_path=str(accumulator), accumulator_sha256=accumulator_sha,
                all_listed_time_and_finite_reference_seams_exact=True,
                completed_segments=segment+(right == 1), wall_seconds_this_process=time.monotonic()-start)
            save(index_path, index)
            print({'stage': 'ordered_prefix_saved', 'segment': segment,
                   'subspan': [str(left), str(right)], 'reused': reused,
                   'A': str(A), 'E': str(E), 'local_J': str(local_J)}, flush=True)
            del first, report
            gc.collect()
    index['whole_forward_leg'] = (args.stop_segment == 550
        and last == PiTime(Fraction(0), Fraction(1, 2)))
    index['complete'] = index['whole_forward_leg']
    index['requested_prefix_finished'] = True
    index['wall_seconds_this_process'] = time.monotonic()-start
    save(index_path, index)
    print({'stage': 'whole_forward_leg_complete' if index['complete'] else 'requested_prefix_finished',
           'completed_segments': index['completed_segments'], 'index_sha256': sha(index_path)}, flush=True)


if __name__ == '__main__':
    main()
