#!/usr/bin/env python3
"""Persist every actual original third-moment span without changing its math.

The frozen original entry supplies its complete source gate, optional full
cut correction, core integral, field extraction, interval quadrature and
final conclusions. This independent entry only adds a flushed journal and
summary after each completed span. It does not re-evaluate a completed span
or claim that an interrupted prefix is complete.
"""
from fractions import Fraction
import hashlib
import inspect
import json
import os
from pathlib import Path

import cartesian_third_activity_moment as original

ORIGINAL_SHA = 'fef214b4b49efb77e4493886431ec125553f842be7a13c3dadd357c0a9a9002e'


def reference(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def durable_leaf(out, report, count, row, total, write):
    endpoints = original.display(total)
    cumulative = dict(display=endpoints,
                      binary64_hex=[value.hex() for value in endpoints],
                      exact_binary_fractions=[str(Fraction.from_float(value))
                                             for value in endpoints])
    journal = out/'actual-prefix-moment-leaves.jsonl'
    item = dict(completed_radial_leaves=count, original_leaf=row,
                cumulative_full_prefix_partial_sum=cumulative)
    data = (json.dumps(item, allow_nan=False)+'\n').encode()
    with journal.open('ab', buffering=0) as stream:
        if stream.write(data) != len(data):
            raise IOError('The entire actual moment leaf was not written')
        os.fsync(stream.fileno())
        size = stream.tell()
    report.update(durable_entry=reference(__file__),
                  frozen_mathematical_entry=reference(original.__file__),
                  complete_interval_arithmetic_changed=False,
                  completed_radial_leaves=count,
                  current_prefix_flux_interval=endpoints,
                  current_prefix_flux_binary64=cumulative,
                  exact_current_radial_coverage=[
                      report['full_prefix_radial_domain_exact'][0],
                      row['radial_exact'][1]],
                  durable_leaf_journal=str(journal),
                  durable_complete_journal_bytes=size,
                  every_completed_leaf_fsynced=True)
    write(out/'summary.json', report)


def main():
    if reference(original.__file__)['sha256'] != ORIGINAL_SHA:
        raise ValueError('The frozen full moment mathematics changed')
    source = inspect.getsource(original.main)
    marker = '                exact_cover.append((left, right))\n'
    if source.count(marker) != 1:
        raise ValueError('The original complete-span record location changed')
    adapted = source.replace(marker, marker+
        '                _held_durable_leaf(out, report, len(leaves), row, total, write)\n')
    namespace = dict(original.__dict__)
    namespace['_held_durable_leaf'] = durable_leaf
    exec(compile(adapted, str(Path(__file__).resolve())+'::durable_original_main',
                 'exec'), namespace)
    return namespace['main']()


if __name__ == '__main__':
    main()
