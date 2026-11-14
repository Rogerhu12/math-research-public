#!/usr/bin/env python3
"""Read the three completed exact-mean arrays of the preserved v2 failure.

This adapter never makes the failed body certificate complete.  Only the
already evaluated full coefficient/forward/backward arrays supply endpoint
or source-pairing consumers that do not require body residual rows.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import json

OLD_KIND = 'actual_final_exact_mean_completed_response_adjoint_body_residual_v2'
OLD_SOURCE = 'e0a2442f8c9f63d4fe4ca733facc601e4db206a14d03a1bba80dd4816e2385b3'
OLD_REPORT = '69c4c6fa2a3e53b5751bb44744a916050703fd5f9ebe99b205edc2c9bf1b3c4a'
FAILURE = dict(type='TypeError', message="unsupported operand type(s) for /: 'Finite' and 'int'")


def read_completed_mean_prefix(path):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=OLD_REPORT:
        raise ValueError('this adapter binds the actual immutable v2 failed container')
    body=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    if (body.get('kind')!=OLD_KIND or body.get('source_sha256')!=OLD_SOURCE
        or body.get('complete') is not False or body.get('failure')!=FAILURE
        or body.get('stage')!='full_body_residuals'
        or body.get('exact_interval')!=['0','25/8']
        or not body.get('whole_original_eta') or not body.get('full_primitive_tail_reused')):
        raise ValueError('the preserved full-cover mean prefix identity changed')
    n=body['total_common_cells'];end=Fraction(0)
    keys=('coefficient_rows','adjoint_flow','response_flow_reverse')
    if n!=7721 or any(len(body[k])!=n for k in keys):
        raise ValueError('all three actual completed 7721-row arrays are required')
    if any(body[k] for k in ('residual_rows','response_jumps','adjoint_jumps')):
        raise ValueError('this adapter imports no body residual or trial jump result')
    for i,row in enumerate(body['coefficient_rows']):
        left,right=map(Fraction,row['interval'])
        gl,gr=map(Fraction,row['actual_scalar_germ'])
        if row['common_row']!=i or left!=end or not gl<=left<right<=gr:
            raise ValueError('the complete coefficient cover or analytic germ changed')
        for flow in (body['adjoint_flow'][i],body['response_flow_reverse'][n-1-i]):
            if flow['common_row']!=i or flow['interval']!=row['interval']:
                raise ValueError('the completed mean flow lost its original direction')
        end=right
    if end!=Fraction(25,8):raise ValueError('the actual whole body mean cover is incomplete')
    def digest(rows):
        text=json.dumps(rows,sort_keys=True,separators=(',',':'),allow_nan=False)
        return hashlib.sha256(text.encode()).hexdigest()
    # These are already evaluated traces, not a new solution or any use of
    # the still absent full operator residuals.
    body['endpoint_mean_traces']=dict(
        response_R=body['outer_response_mean'],
        response_0=body['response_flow_reverse'][-1]['left'],
        adjoint_0=body['adjoint_initial_mean'],
        adjoint_R=body['adjoint_flow'][-1]['right'])
    body['completed_mean_prefix_provenance']=dict(
        container_sha256=OLD_REPORT,original_kind=OLD_KIND,
        original_source_sha256=OLD_SOURCE,original_complete=False,
        original_failure=FAILURE,
        complete_array_hashes={k:digest(body[k]) for k in keys},
        completed_mean_arrays_only=True,body_residual_complete=False)
    return body
