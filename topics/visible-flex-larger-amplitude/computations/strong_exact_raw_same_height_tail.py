#!/usr/bin/env python3
"""Same full-H true-tail audit with an explicit same-grid exact raw warm guess.

The original independent runner and all its guards are source-hash locked.
Only client selection, complete provenance and additional source hashes change.
"""
from pathlib import Path
import hashlib

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_actual_same_height_tail.py'
EXPECTED='ef8ffa1ceaa813d3a04f3551c3b44111d0e0af2d60953a750e7ec25e46a72ea3'
EDITS=[('    from tail_frozen_client import WeightedTailPort', '    from strong_exact_raw_tail_client import WeightedTailPort'), ("        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs')]", "        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs',\n        'strong_exact_raw_same_height_tail.py', 'strong_exact_raw_tail_client.py',\n        'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs')]"), ('    plan = dict(scope=__doc__, source_sha256=', '    plan = dict(scope=__doc__, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, source_sha256=')]

def main():
    original=TEMPLATE.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=EXPECTED:
        raise ValueError('Independent full-H source changed before exact-raw wrapping')
    source=original
    for before,after in EDITS:
        if source.count(before)!=1:
            raise ValueError('Independent exact-raw source anchor is not unique')
        source=source.replace(before,after)
    provenance=dict(scope=__doc__,template_sha256=EXPECTED,
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in EDITS],
        new_worker='strong_exact_raw_tail_worker.mjs',
        same_full_discretization_and_H_required_for_raw_preservation=True,
        no_prior_norm_is_accepted_without_original_full_solve_and_audit=True)
    namespace=dict(__file__=str(TEMPLATE),__name__='strong_exact_raw_independent_source',
        EXACT_RAW_SOURCE_TRANSFORM=provenance)
    exec(compile(source,str(TEMPLATE)+':exact-raw-adapter','exec'),namespace)
    namespace['main']()

if __name__=='__main__':main()
