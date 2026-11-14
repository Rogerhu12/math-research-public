#!/usr/bin/env python3
"""Audit the genuine post-RMS tail response before exact same-H final reuse.

This fresh Python scheduling entry changes exactly one request flag: the
original Hnew recheck after successful complete prefix RMS asks for the original
full audit as well as the original full Jacobian. The initial affine anchor and
the final audited request are untouched. The existing recorded-tail port may
then reuse that completed audited response at exactly the same complete H. It
still writes the normal final logical packet with its original provenance and
call counting. Different H always follows the original live request path.

No MJS, equation, solve tolerance, positivity test, Newton correction, RMS,
physical boundary or final seam acceptance gate is changed. No saved flow
snapshot is treated as a solved or audited new response. This entry requires
the existing verified initial audited packet and ready record; it does not
silently enable worker-release mode or request an audit at the initial anchor.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_full_tangent_initial_laws_actual_bvp.py':
        '31868ba1465e489a9eecc1423a9bde567de0946b0f75e02c9bc627b998991b42',
    'root_actual_neck_bvp.py':
        '03bd353875b4a7ca248c938887b706ce6e2d3115e9b82f2cf772ccc4b5ce98b7',
    'strong_actual_recorded_tail_port.py':
        '7fc687bd4608f5656140dc19abebccfb66074684c46651513efe68818ec311f0',
}
OLD_CLIENT = "'stored-resumable':HERE/'tail_resumable_client.py',"
NEW_CLIENT = "'stored-resumable':HERE/'tail_frozen_client.py',"
BEFORE = '                    actual=self.tail.solve(Hnew,jacobian=True,audit=False)'
AFTER = '                    actual=self.tail.solve(Hnew,jacobian=True,audit=True)'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def audited_actual_source(source):
    """Return the one-flag in-memory transform with a fully reversible record."""
    path = HERE/'root_actual_neck_bvp.py'
    original = path.read_text()
    if sha(path) != EXPECTED[path.name] or original.count(OLD_CLIENT) != 1:
        raise ValueError('The frozen complete actual-tail source changed')
    if source != original.replace(OLD_CLIENT, NEW_CLIENT, 1):
        raise ValueError('An undeclared prior actual-tail transform is present')
    if source.count(BEFORE) != 1 or AFTER in source:
        raise ValueError('The unique post-RMS true-H request anchor changed')
    changed = source.replace(BEFORE, AFTER, 1)
    ast.parse(changed, filename='<original-actual-with-post-RMS-audit>')
    if changed.replace(AFTER, BEFORE, 1) != source:
        raise ValueError('More than the declared audit request flag changed')
    # The unchanged finalizer remains authoritative, including its separate
    # request, exact physical-H selection, call count and seam tolerance.
    final = 'response=self.tail.solve(self.tail_height(y),jacobian=True,audit=True)'
    anchor = 'H=self.tail_height(y[:,-1]);response=self.tail.solve(H,jacobian=True,audit=False)'
    if changed.count(final) != 1 or changed.count(anchor) != 1:
        raise ValueError('The original initial/final complete-H requests changed')
    return changed, dict(
        scope=__doc__, original_file_sha256=sha(path),
        prior_compiled_sha256=hashlib.sha256(source.encode()).hexdigest(),
        compiled_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        scheduling_source=str(Path(__file__).resolve()),
        scheduling_source_sha256=sha(__file__),
        replacements=[dict(old=BEFORE, new=AFTER, count=1)],
        exact_reverse_recovers_prior_actual_source=True,
        initial_anchor_request_unchanged=True, final_audited_request_unchanged=True,
        full_actual_H_Jacobian_audit_BC_RMS_and_seam_gates_preserved=True,
        cached_response_must_already_have_genuine_full_audit=True,
        changed_final_H_requires_original_new_live_audit=True,
        all_MJS_unchanged=True, numerical_benefit_not_yet_measured=True)


def wrap_resource_outer(original_outer):
    """Install only after the complete retained initial-law/storage builder."""
    def resource_outer(original):
        installed_retained = original_outer(original)

        def installed(original_build, old_heap, semi_space):
            retained = installed_retained(original_build, old_heap, semi_space)

            def build(merit, disk):
                source, prior = retained(merit, disk)
                edits = [
                    ('    actual_source = original_actual.replace(old_client, new_client)',
                     '    actual_source = original_actual.replace(old_client, new_client)\n'
                     '    from strong_eager_true_H_audit_initial_laws_actual_bvp import audited_actual_source\n'
                     '    actual_source, eager_true_H_audit = audited_actual_source(actual_source)'),
                    ('            replacements=[dict(old=old_client, new=new_client, count=1)]),',
                     '            replacements=[dict(old=old_client, new=new_client, count=1)]\n'
                     "                + eager_true_H_audit['replacements'],\n"
                     '            eager_true_H_audit=eager_true_H_audit),'),
                    ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
                     "    source_names += ('strong_eager_true_H_audit_initial_laws_actual_bvp.py',)\n"
                     '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'),
                ]
                changed = source
                for before, after in edits:
                    if changed.count(before) != 1:
                        raise ValueError('Eager audit scheduling anchor is not unique: '+repr(before))
                    changed = changed.replace(before, after, 1)
                ast.parse(changed, filename='<initial-laws-post-RMS-audit-production>')
                reverse = changed
                for before, after in reversed(edits):
                    if reverse.count(after) != 1:
                        raise ValueError('Eager audit scheduling reverse anchor changed')
                    reverse = reverse.replace(after, before, 1)
                if reverse != source:
                    raise ValueError('The audit scheduler altered other production code')
                # Validate the nested source during source-only preparation too.
                unused, actual_record = audited_actual_source(
                    (HERE/'root_actual_neck_bvp.py').read_text().replace(OLD_CLIENT, NEW_CLIENT, 1))
                record = dict(prior)
                record['source_sha256'] = {**prior['source_sha256'],
                    str(Path(__file__).resolve()): sha(__file__)}
                record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
                record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
                record['replacements'] = list(prior['replacements']) + [
                    dict(before=a, after=b, count=1) for a, b in edits]
                record['eager_true_H_audit_scheduling'] = actual_record
                return changed, record

            return build

        return installed

    return resource_outer


def main():
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('The declared original entry differs: '+name)
    source_only = '--prepare-source-record' in sys.argv
    if not source_only:
        for name in ('--initial-audited-tail-packet', '--initial-audited-tail-ready'):
            if sys.argv.count(name) != 1 or sys.argv.index(name)+1 >= len(sys.argv):
                raise ValueError('Post-RMS audited reuse requires one explicit '+name)
            if not Path(sys.argv[sys.argv.index(name)+1]).is_file():
                raise ValueError('The explicit initial audited input is missing: '+name)
        if '--release-tail-worker-between-responses' in sys.argv:
            raise ValueError('This scheduler preserves the unaudited initial-anchor request; do not force every live response audited')
    import strong_full_tangent_initial_laws_actual_bvp as entry
    original_outer = entry.resource_outer
    entry.resource_outer = wrap_resource_outer(original_outer)
    try:
        entry.main()
    finally:
        entry.resource_outer = original_outer


if __name__ == '__main__':
    main()
