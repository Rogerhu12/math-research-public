#!/usr/bin/env python3
"""Start continuation from complete raw tail states without preloading a tangent.

A previous environment's tangent snapshot is an optional warm predictor, not a
mathematical input or acceptance certificate. This entry explicitly declines
all preloaded tangent snapshots, retaining the original complete raw state/H
checkpoint and every original nonlinear solve, full Jacobian, positivity,
physical boundary, RMS and final audit check. Freshly computed tangent snapshots
are still saved and used normally within this run. No MJS or identity comparator
is modified.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path
import sys
import strong_full_tangent_actual_bvp_v2 as storage
import strong_20261114_loop_actual_bvp as entry

HERE=Path(__file__).resolve().parent

def main():
    if '--initial-full-tangent-manifest' in sys.argv:
        raise ValueError('Raw-state startup explicitly requires no preloaded tangent manifest')
    prior=storage.resource_outer
    def outer(original):
        retained=prior(original)
        def installed(original_build,old_heap,semi_space):
            retained_build=retained(original_build,old_heap,semi_space)
            def build(merit,disk):
                source,record=retained_build(merit,disk)
                before="loaded = original_loader(name+'_full_tangent', HERE/'strong_full_tangent_tail_client.py')"
                if source.count(before)!=1:
                    raise ValueError('Complete full-tangent client installation anchor differs')
                line=next(x for x in source.splitlines() if before in x)
                indent=line[:len(line)-len(line.lstrip())]
                after=before+"\n"+indent+"loaded.checkpoint_snapshot = lambda config: None"
                changed=source.replace(before,after,1)
                ast.parse(changed)
                if changed.replace(after,before,1)!=source:
                    raise ValueError('Raw startup altered unrelated production code')
                result=dict(record)
                result['source_sha256']={**record['source_sha256'],str(Path(__file__).resolve()):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
                result['prior_transformed_source_sha256']=record['transformed_source_sha256']
                result['transformed_source_sha256']=hashlib.sha256(changed.encode()).hexdigest()
                result['replacements']=list(record['replacements'])+[dict(before=before,after=after,count=1)]
                result['raw_tail_start']=dict(scope=__doc__,optional_tangent_preload_disabled=True,
                    complete_raw_state_and_height_checkpoint_preserved=True,
                    all_MJS_and_identity_comparators_unchanged=True,
                    fresh_current_H_full_solve_Jacobian_positivity_and_audit_required=True,
                    newly_generated_tangents_saved_and_used_normally=True)
                return changed,result
            return build
        return installed
    storage.resource_outer=outer
    try:entry.main()
    finally:storage.resource_outer=prior

if __name__=='__main__':main()
