#!/usr/bin/env python3
"""Transfer a genuinely complete same-field metric proof to the exact R89 disks.

The new target equals the old target outside both disks and is df_new^2+I on
the fixed graph disks.  Complete Cartesian two-jet equality at their boundaries
is already paid by R89.  This is a new fixed target, not refinement of the old
one. No old pending finite proof can pass this entry.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

GATE = Q(1,1000000)
EXACT_SHA = '0ce3540173910c2b8caf91ce1162dea9e642bbb0f5dba7ebd03704f52ee3147a'
CONSTRUCTOR_SHA = 'f1edf2d8ef335ad4cc23062a9f94427722fe232f690b2f78c3675cd225f94ce4'
GEOMETRY_SHA = '57480474eab2110d41053fee5ada0f02548dbb1b9e2fbaf56b9a16ce9fea742c'
CORE_SHA = 'e44cbdaab91969e0bdfeec432a5e6c52126c9b6d6219cbca0e22c91233200f96'
CLI_SHA = 'd42c160ffb60d03cda3ff57399191cb582e4bf2be9058d0bbcc4916c479c82cd'
PROOF_SHA = '6d8362efb9c589441ff1264f6fb7ebd2cf114309b0d26e58a3da43b060c4e36f'
COLLECTOR_SHA = 'dcec6b1957c481aab03e6d8446d198e55b2f7e1d51919944907f772f8773057f'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def checked(item):
    if ref(item['path']) != item:
        raise ValueError('An exact actual proof dependency changed')
    return json.loads(Path(item['path']).read_text())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('canonical-metric','exact-marker-proof','actual-constructor','out'):
        p.add_argument('--'+name,type=Path,required=True)
    args = p.parse_args()
    exact_ref,constructor_ref,metric_ref = map(ref,
        (args.exact_marker_proof,args.actual_constructor,args.canonical_metric))
    if exact_ref['sha256']!=EXACT_SHA or constructor_ref['sha256']!=CONSTRUCTOR_SHA:
        raise ValueError('Use the actual R89 exact proof and successful full constructor')
    exact,constructor,metric = map(checked,(exact_ref,constructor_ref,metric_ref))
    here = Path(__file__).resolve().parent
    sources = [('sharp_marker_exact_certificate.py',PROOF_SHA),
               ('actual_closed_sharp_full_disk_marker.py',CORE_SHA),
               ('actual_closed_sharp_full_disk_marker_cli_v2.py',CLI_SHA),
               ('closed_map_complete_metric_recovery_v2.py',COLLECTOR_SHA)]
    source_refs = []
    for name,expected in sources:
        item = ref(here/name)
        if item['sha256'] != expected:
            raise ValueError('An actually checked exact implementation changed')
        source_refs.append(item)
    if (metric['status']!='actual_complete_marked_column_closed_metric_certified'
            or not metric['full_same_fixed_metric_gate_passed']
            or not metric['all_angles_radii_and_phases_included']
            or Q(metric['exact_metric_gate'])!=GATE
            or not 0<=Q(metric['complete_closed_metric_operator_upper']['upper_exact'])<GATE
            or metric['source']!=source_refs[-1]
            or metric['closed_geometry']['sha256']!=GEOMETRY_SHA):
        raise ValueError('A genuinely complete original whole-surface metric proof is required')
    old = checked(metric['closed_geometry'])
    if (metric['closed_geometry']!=exact['geometry_report']
            or metric['closed_geometry']!=constructor['original_geometry_report']
            or constructor['original_query_sha256']!=old['actual_query']['sha256']
            or not constructor['entry_constructor_actually_returned']
            or constructor['source_sha256']!=CORE_SHA
            or constructor['actual_cli_source']['sha256']!=CLI_SHA
            or not constructor['target_metric_fixed_for_all_phases']
            or not constructor['all_boundary_Cartesian_two_jets_preserved']
            or not constructor['disk_target_changed_once_at_design']):
        raise ValueError('The R89 constructor is not the same actual complete geometry outside the fixed disks')
    for key in ('geometry_bundle','source_run','accepted_packet','entire_mean','cut_prefix','physical_R_identity'):
        if metric[key]!=old[key]:
            raise ValueError('A complete original field component changed: '+key)
    if (metric['canonical_marker']!=old['canonical_marker']
            or metric['cut_width_exact']!=old['cut_width_exact']
            or metric['cylinder_total_length_exact_binary']!=old['cylinder_total_length_exact_binary']):
        raise ValueError('A complete original chart or target changed outside the disks')
    transfer = exact['actual_scalar_transfer']
    if (Q(constructor['new_marker']['radius_exact'])!=Q(transfer['radius_exact'])
            or Q(constructor['new_marker']['epsilon_exact'])!=Q(transfer['epsilon_exact'])
            or not exact['unit_marker']['all_angles_included_by_holomorphic_modulus_bounds']
            or not transfer['same_R82_global_scalar_bounds_preserved']
            or not constructor['exact_geometry_transfer']['same_R82_global_scalar_bounds_preserved']):
        raise ValueError('The exact new graph/geometry contract changed')
    report = dict(status='actual_R89_complete_same_fixed_metric_certified',source=ref(__file__),
        source_dependencies=source_refs,canonical_complete_metric=metric_ref,
        exact_marker_proof=exact_ref,actual_complete_constructor=constructor_ref,
        same_original_complete_geometry=metric['closed_geometry'],
        geometry_bundle=metric['geometry_bundle'],source_run=metric['source_run'],
        accepted_packet=metric['accepted_packet'],entire_mean=metric['entire_mean'],
        complete_closed_metric_operator_upper=metric['complete_closed_metric_operator_upper'],
        exact_metric_gate=str(GATE),all_angles_radii_and_phases_included=True,
        finite_stage_count=metric['finite_stage_count'],original_literal_span_count=metric['original_literal_span_count'],
        target_outside_fixed_disks='Exactly the original complete canonical target',
        target_on_fixed_disks='I + df89 tensor df89 in the same Cartesian disk chart, fixed at all phases',
        new_disk_relative_metric_error_exact='0',
        all_boundary_Cartesian_two_jets_preserved=True,
        complete_same_fixed_metric_gate_passed=True,
        original_target_fixed_problem_refinement_claimed=False,
        exact_lambda_one_or_ten_percent_held_claimed=False,
        fixed_complete_problem_convergence_claimed=False,
        any_native_Gram_Taylor_or_integral_recomputed=False,README_completion_claimed=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('x') as stream:
        stream.write(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=ref(args.out),status=report['status'],
        global_metric_upper=report['complete_closed_metric_operator_upper']['upper'])),flush=True)


if __name__ == '__main__':
    main()
