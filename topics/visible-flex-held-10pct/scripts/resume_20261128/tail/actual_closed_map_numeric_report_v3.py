#!/usr/bin/env python3
"""Run the frozen full-map query, converting NumPy scalar diagnostics to JSON.

The mathematical source, all geometry operations and original acceptance
checks are unchanged. A long-double sampled error is rounded only for its
diagnostic JSON display; this is not an outward bound or a continuous proof.
The earlier genuine failed report remains a separate execution record.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import numpy as np

import actual_closed_map_v2 as original


ORIGINAL_SHA = '3742d3041daad388cc26d63fb7e4300732459f076327938a39ef92b7f3603ee5'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--out', type=Path, required=True)
    args, unused = parser.parse_known_args()
    source = ref(original.__file__)
    if source['sha256'] != ORIGINAL_SHA:
        raise ValueError('The frozen mathematical query source changed')
    output = args.out.resolve()
    if output.exists():
        raise ValueError('Use a new diagnostic report path')
    original_dumps = json.dumps
    conversions = {}

    def diagnostic_dumps(value, *positional, **options):
        old_default = options.get('default')

        def display_scalar(item):
            if isinstance(item, np.floating):
                displayed = float(item)
                if not np.isfinite(item) or not math.isfinite(displayed):
                    raise ValueError('A diagnostic scalar is not finite in JSON')
                if item != 0 and displayed == 0:
                    raise ValueError('A nonzero diagnostic would underflow in JSON')
                name = type(item).__name__
                conversions[name] = conversions.get(name, 0) + 1
                return displayed
            if old_default is not None:
                return old_default(item)
            raise TypeError('Unsupported diagnostic JSON value: ' + type(item).__name__)

        options['default'] = display_scalar
        return original_dumps(value, *positional, **options)

    start = time.monotonic()
    record = dict(source=ref(__file__), unchanged_mathematical_query_source=source,
                  actual_argv=list(sys.argv), geometry_operations_changed=False,
                  original_checks_changed=False, numerical_display_conversion_only=True,
                  diagnostic_is_outward_bound=False, continuous_certificate=False)
    try:
        json.dumps = diagnostic_dumps
        original.main()
        record.update(status='frozen_complete_map_query_report_serialized',
                      report=ref(output))
    except Exception as exc:
        record.update(status='frozen_complete_map_query_report_failed', error=repr(exc))
        raise
    finally:
        json.dumps = original_dumps
        record.update(seconds=time.monotonic() - start,
                      scalar_display_conversion_counts=conversions)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.with_name(output.stem + '-rendering.json').write_text(
            original_dumps(record, indent=2, allow_nan=False) + '\n')


if __name__ == '__main__':
    main()
