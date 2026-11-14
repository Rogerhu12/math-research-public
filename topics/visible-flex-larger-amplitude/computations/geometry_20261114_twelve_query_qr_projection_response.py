#!/usr/bin/env python3
"""Original complete affine Rphi FD on an actual twelve-query QR-H warm.

Only the actual producer schema and provenance reporting change. Every
original FD direction, step, Richardson comparison and implementation
threshold remains in the frozen original consumer. No nonlinear native
tail solve is performed or inferred from this warm or this check.
"""
from __future__ import annotations

from pathlib import Path

import geometry_20261114_constrained_trust_response as original_response
import geometry_20261114_twelve_query_qr_projection_warm as producer


HERE=Path(__file__).resolve().parent
ORIGINAL_RESPONSE_SHA='7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78'


def main():
    original=original_response.original
    if original.sha(Path(original_response.__file__))!=ORIGINAL_RESPONSE_SHA:
        raise ValueError('Retain the frozen original complete actual-warm FD consumer')
    for name,digest in producer.FROZEN.items():
        if original.sha(HERE/name)!=digest:
            raise ValueError('A frozen twelve-query QR dependency changed: '+name)
    old_schema,old_doc=original_response.SCHEMA,original_response.__doc__
    old_write=original.write
    identity=dict(entry_source_sha256=original.sha(__file__),
        original_response_source_sha256=ORIGINAL_RESPONSE_SHA,
        optimizer_schema=producer.SCHEMA,
        query_specs=[dict(q) for q in producer.baseline.domain.QUERY_SPECS],
        complete_QR_H_and_fixed_support_C_are_only_warm_algorithms=True,
        original_complete_boundary_FD_recomputed=True,
        original_directions_steps_Richardson_and_threshold_unchanged=True,
        prior_warm_or_FD_pass_not_relabelled=True,nonlinear_native_solved=False)

    def write(path,report):
        if Path(path).name=='response-check.json' and isinstance(report,dict):
            report['twelve_query_QR_response_entry']=identity
            report['source_sha256']=identity['entry_source_sha256']
            for name in (Path(__file__).name,*producer.SOURCE_NAMES):
                report['consumed_source_sha256'][name]=original.sha(HERE/name)
        old_write(path,report)

    original_response.SCHEMA,original_response.__doc__=producer.SCHEMA,__doc__
    original.write=write
    try:
        return original_response.main()
    finally:
        original_response.SCHEMA,original_response.__doc__=old_schema,old_doc
        original.write=old_write


if __name__=='__main__':
    raise SystemExit(main())
