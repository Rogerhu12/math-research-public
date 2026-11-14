#!/usr/bin/env python3
"""Run the unchanged cached new-H audit from its exact unaccepted initial seed.

The prepared stage-check runner is retained at its recorded source hash.
This entry only makes its warm provenance conditional on the seed argument;
all original complete-H/physical/configuration/Jacobian/audit gates remain.
"""
from pathlib import Path
import ast
import hashlib
import sys
import strong_cached_target_tail_audit as prior


def main():
    if '--initial-seed' not in sys.argv:
        raise ValueError('This recovery entry requires the explicit exact initial seed')
    source,record=prior.build_source()
    before="warm_guess_kind='old accepted full shooting state at a different H; original predictor/Newton remain required',"
    after=("warm_guess_kind=('exact unaccepted initial full shooting state restored byte for byte; "
        "old norm not used and original full Newton/Jacobian/audit still required' if args.initial_seed "
        "else 'old accepted full shooting state at a different H; original predictor/Newton remain required'),")
    if source.count(before)!=1:raise ValueError('Prepared provenance field changed')
    source=source.replace(before,after,1);ast.parse(source)
    record['seed_provenance_only_revision']=dict(
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        prior_entry_sha256=hashlib.sha256(Path(prior.__file__).read_bytes()).hexdigest(),
        replacement=dict(before=before,after=after,count=1),
        combined_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        original_warm_loading_solver_and_final_acceptance_unchanged=True)
    namespace=dict(__file__=str(prior.TEMPLATE),__name__='strong_cached_exact_seed_audit_source',
        STAGE_SOURCE_TRANSFORM=record)
    exec(compile(source,'<exact-initial-seed-audit-provenance>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
