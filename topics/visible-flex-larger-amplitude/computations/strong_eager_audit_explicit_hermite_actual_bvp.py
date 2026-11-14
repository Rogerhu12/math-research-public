#!/usr/bin/env python3
"""Compose the frozen eager audit scheduler with an explicit first-live warm input.

The complete supplied Hermite report and its accepted baseline/input identities
are checked before production assembly. Only an exactly matching complete first
live H may select it as the original worker's unaccepted initial checkpoint.
The existing audited cache and all original equations/acceptance remain.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_eager_true_H_audit_initial_laws_actual_bvp.py':
        'e5f80623cf995d392c3a980630b8d5809997367ae39997782419d0b6aa227fac',
    'strong_actual_recorded_tail_port.py':
        '7fc687bd4608f5656140dc19abebccfb66074684c46651513efe68818ec311f0',
    'strong_recorded_port_explicit_hermite_warm.py':
        '9e1082ab8a9525255ded620cf3cb69e38b414301c535f72a74ff93f99ab80bfc',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def compose_outer(previous_outer, report_path, preparation):
    def outer(original_outer):
        retained_outer = previous_outer(original_outer)

        def resource_outer(original):
            retained_installed = retained_outer(original)

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
                    after = ("    source_names += ('strong_eager_audit_explicit_hermite_actual_bvp.py',\n"
                        "        'strong_recorded_port_explicit_hermite_warm.py')\n"+before+'\n'
                        '    hashes['+repr(str(report_path.resolve()))+'] = sha(Path('+repr(str(report_path.resolve()))+'))')
                    edits = [(anchor, added), (before, after)]
                    changed = source
                    for a, b in edits:
                        if changed.count(a) != 1:
                            raise ValueError('Explicit first warm source anchor changed: '+repr(a))
                        changed = changed.replace(a, b, 1)
                    ast.parse(changed, filename='<initial-laws-eager-audit-explicit-first-warm>')
                    reverse = changed
                    for a, b in reversed(edits):
                        if reverse.count(b) != 1:
                            raise ValueError('Explicit first warm reverse anchor changed')
                        reverse = reverse.replace(b, a, 1)
                    if reverse != source:
                        raise ValueError('More than the declared input-path adapter changed')
                    own = {str(HERE/name): sha(HERE/name) for name in
                           ('strong_eager_audit_explicit_hermite_actual_bvp.py',
                            'strong_recorded_port_explicit_hermite_warm.py')}
                    record = dict(prior)
                    record['source_sha256'] = {**prior['source_sha256'], **own}
                    record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
                    record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
                    record['replacements'] = list(prior['replacements']) + [
                        dict(before=a, after=b, count=1) for a, b in edits]
                    record['explicit_first_live_unaccepted_Hermite_input'] = preparation
                    return changed, record

                return build

            return installed

        return resource_outer

    return outer


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--initial-hermite-warm-report', type=Path, required=True)
    own, remaining = parser.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen audit scheduler/recorded port differs: '+name)

    def argument(name):
        if remaining.count(name) != 1 or remaining.index(name)+1 >= len(remaining):
            raise ValueError('Give one explicit '+name)
        return Path(remaining[remaining.index(name)+1])

    from strong_recorded_port_explicit_hermite_warm import verified_warm
    record, unused = verified_warm(argument('--tail-warm-checkpoint'), own.initial_hermite_warm_report,
        argument('--actual-reference'), argument('--initial-audited-tail-packet'))
    import strong_eager_true_H_audit_initial_laws_actual_bvp as entry
    original, old_argv = entry.wrap_resource_outer, sys.argv
    entry.wrap_resource_outer = compose_outer(original, own.initial_hermite_warm_report, record)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        entry.wrap_resource_outer, sys.argv = original, old_argv


if __name__ == '__main__':
    main()
