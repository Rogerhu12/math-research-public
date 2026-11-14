#!/usr/bin/env python3
"""Compose the genuine anchor-provider BVP with a first-live Hermite input.

AI-assisted research, strong_recovery, 2026-11-13.
The already verified input adapter may choose one explicitly unaccepted full
shooting checkpoint only when every first live target-H bit matches. All
later requests and the original audit scheduling stay unchanged. The original
anchor provider, nonlinear equations, full J, positivity, line search, RMS,
true-H physical boundary and final audit decide acceptance. No MJS is changed.
This entry is neither an eager-audit adapter nor a new mathematical solver.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_full_tangent_initial_laws_anchor_actual_bvp.py':
        'd151cb67c2dbfbadd5ba35a9f386c5e15ff98f056df45d89677b989cd887f651',
    'strong_full_tangent_initial_laws_actual_bvp.py':
        '31868ba1465e489a9eecc1423a9bde567de0946b0f75e02c9bc627b998991b42',
    'strong_actual_recorded_tail_port.py':
        '7fc687bd4608f5656140dc19abebccfb66074684c46651513efe68818ec311f0',
    'strong_recorded_port_explicit_hermite_warm.py':
        '9e1082ab8a9525255ded620cf3cb69e38b414301c535f72a74ff93f99ab80bfc',
    'strong_monotone_initial_speed_anchor.py':
        '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'root_actual_neck_bvp.py':
        '03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def with_first_warm(previous_outer, report_path, preparation):
    def outer(original):
        retained_installed = previous_outer(original)

        def installed(original_build, old_heap, semi_space):
            retained = retained_installed(original_build, old_heap, semi_space)

            def build(merit, disk):
                source, prior = retained(merit, disk)
                anchor = '                release_between_responses=options.release_tail_worker_between_responses)'
                added = (anchor+'\n'
                    '            from strong_recorded_port_explicit_hermite_warm import make_first_warm_port_class\n'
                    '            loaded.WeightedTailPort = make_first_warm_port_class(\n'
                    '                loaded.WeightedTailPort, options.tail_warm_checkpoint,\n'
                    '                Path('+repr(str(report_path.resolve()))+'), options.actual_reference,\n'
                    '                options.initial_audited_tail_packet)')
                before = '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'
                after = ("    source_names += ('strong_explicit_hermite_anchor_actual_bvp.py',\n"
                    "        'strong_recorded_port_explicit_hermite_warm.py')\n"+before+'\n'
                    '    hashes['+repr(str(report_path.resolve()))+'] = sha(Path('+repr(str(report_path.resolve()))+'))')
                edits = [(anchor, added), (before, after)]
                changed = source
                for old, new in edits:
                    if changed.count(old) != 1:
                        raise ValueError('Original first-live input source site is not unique')
                    changed = changed.replace(old, new, 1)
                ast.parse(changed, filename='<original-anchor-first-live-Hermite-input>')
                reverse = changed
                for old, new in reversed(edits):
                    if reverse.count(new) != 1:
                        raise ValueError('Original first-live input reverse site differs')
                    reverse = reverse.replace(new, old, 1)
                if reverse != source:
                    raise ValueError('An undeclared production operation changed')
                own = {str(HERE/name):sha(HERE/name) for name in
                    ('strong_explicit_hermite_anchor_actual_bvp.py',
                     'strong_recorded_port_explicit_hermite_warm.py')}
                record = dict(prior)
                record['source_sha256'] = {**prior['source_sha256'], **own}
                record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
                record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
                record['replacements'] = list(prior['replacements'])+[
                    dict(before=old,after=new,count=1) for old,new in edits]
                record['explicit_first_live_unaccepted_Hermite_input'] = dict(preparation,
                    current_anchor_provider_sha256=EXPECTED['strong_monotone_initial_speed_anchor.py'],
                    original_actual_neck_source_sha256=EXPECTED['root_actual_neck_bvp.py'],
                    original_audit_request_order_unchanged=True,
                    original_anchor_full_tangent_production_retained=True,
                    exact_reverse_recovers_original_anchor_source=True,
                    new_numerical_solution_created_by_input_adapter=False)
                return changed, record
            return build
        return installed
    return outer


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--initial-hermite-warm-report', type=Path, required=True)
    own, remaining = parser.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('The frozen original/provider/input source differs: '+name)

    def argument(name):
        if remaining.count(name) != 1 or remaining.index(name)+1 >= len(remaining):
            raise ValueError('Give exactly one '+name)
        return Path(remaining[remaining.index(name)+1])

    from strong_recorded_port_explicit_hermite_warm import verified_warm
    preparation, unused_height = verified_warm(argument('--tail-warm-checkpoint'),
        own.initial_hermite_warm_report, argument('--actual-reference'),
        argument('--initial-audited-tail-packet'))
    argument('--initial-audited-tail-ready')
    import strong_full_tangent_initial_laws_actual_bvp as full
    import strong_full_tangent_initial_laws_anchor_actual_bvp as entry
    previous, old_argv = full.resource_outer, sys.argv
    full.resource_outer = with_first_warm(previous, own.initial_hermite_warm_report, preparation)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        full.resource_outer, sys.argv = previous, old_argv


if __name__ == '__main__':
    main()
