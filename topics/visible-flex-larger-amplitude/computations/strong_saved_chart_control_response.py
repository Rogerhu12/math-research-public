#!/usr/bin/env python3
"""Restore the recorded material chart before the original fixed response.

The original fixed loader reconstructs default neck reference knots. A saved
same-metric refinement may deliberately preserve a different reference grid.
This wrapper restores the accepted binary64 reference knots and selected core
before the original complete raw identity check. No equation, finite
difference, full Jacobian, half-step check, or acceptance gate is replaced.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--response-checkpoint', type=Path, required=True)
    parser.add_argument('--response-raw', type=Path, required=True)
    parser.add_argument('--response-out-prefix', type=Path, required=True)
    args, _ = parser.parse_known_args()
    saved, record = read(args.response_checkpoint), read(args.response_raw)
    ident = record['identity']
    if ident['numerical_reference_knots'] != saved['numerical_meridian_chart']['reference_t']:
        raise ValueError('The accepted raw/physical material chart differs')
    if ident['profile'] != saved['frozen_profile']:
        raise ValueError('The accepted raw/physical metric differs')
    import numpy as np
    import root_raw_collocation as raw
    import strong_disk_actual_fixed_control_response as entry
    original_read = raw.read
    report = dict(scope=__doc__, original_source_files_unchanged=True,
                  raw_reads=0, complete_original_raw_identity_guard_retained=True,
                  profile_length_physical_breaks_unchanged=True,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    report_file = Path(str(args.response_out_prefix)+'-saved-chart.json')

    def restored(path, obj, options):
        if Path(path).resolve() != args.response_raw.resolve():
            return original_read(path, obj, options)
        obj._neck_knots = np.asarray(ident['numerical_reference_knots'], dtype=float).copy()
        obj.chart_breaks = obj._neck_knots.copy()
        obj.select(np.asarray(record['parameter_state'], dtype=float))
        solution, info = original_read(path, obj, options)
        flow = obj.flow(solution.p[0])
        if (flow.cfg != saved['frozen_profile'] or flow.end != saved['meridian_length']
                or np.asarray(flow.breaks, dtype=np.float64).tobytes() !=
                np.asarray(saved['numerical_meridian_chart']['physical_s'], dtype=np.float64).tobytes()):
            raise ValueError('Restoring reference coordinates changed the physical geometry')
        report['raw_reads'] += 1
        report_file.write_text(json.dumps(report, indent=2)+'\n')
        return solution, info

    raw.read = restored
    try:
        entry.main()
    finally:
        raw.read = original_read


if __name__ == '__main__':
    main()
