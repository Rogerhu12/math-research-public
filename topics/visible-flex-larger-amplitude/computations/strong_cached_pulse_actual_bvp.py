#!/usr/bin/env python3
"""Compose explicit pulse geometry with complete-input prefix persistence.

This only joins the separately recorded provider and cache adapters. The full
actual 27-parameter equations, physical-coordinate Newton merit, disk QR,
true changed-H tail and final acceptance all remain the retained workflow.
Nonzero pulse changes physical g; caching and representation do not certify it.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import strong_fresh_resource_actual_bvp as resource
import strong_pulse_actual_bvp as pulse
import strong_cached_prefix_actual_bvp as cached
import strong_prefix_evaluation_cache as cache

HERE=Path(__file__).resolve().parent
EXPECTED={
    'strong_fresh_resource_actual_bvp.py':'26f0c2ba1bdbb413ba7819f8f1aaafa7892787a7e14509357b6a28821e8c808f',
    'strong_pulse_actual_bvp.py':'bf34b54857ca35e270f4198344ec9b96f5b210781d2a95afb92b044c8f61738f',
    'strong_cached_prefix_actual_bvp.py':'986de6d32371144d20dc5a511dd027875e0b43aa976201447e75a7151e940faa',
    'strong_prefix_evaluation_cache.py':'97a2b5b0eccbef3a9645167b2c91c73503a820507136b10bfdb300a97df7f6ea'}
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def composed_build(original,configuration):
    for name,expected in EXPECTED.items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=expected:
            raise ValueError('Retained pulse/cache source differs: '+name)
    prior=cached.build_wrapper(pulse.pulse_build(original),configuration)
    def build(merit,disk):
        source,record=prior(merit,disk)
        before='    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'
        after="    source_names += ('strong_cached_pulse_actual_bvp.py',)\n"+before
        if source.count(before)!=1:raise ValueError('Composed source identity anchor differs')
        source=source.replace(before,after,1)
        ast.parse(source,filename='<pulse-with-complete-call-prefix-persistence>')
        result=dict(record)
        result['source_sha256']={**record['source_sha256'],str(Path(__file__).resolve()):SELF_SHA}
        result['prior_transformed_source_sha256']=record['transformed_source_sha256']
        result['transformed_source_sha256']=hashlib.sha256(source.encode()).hexdigest()
        result['replacements']=[*record['replacements'],dict(before=before,after=after,count=1)]
        result['composed_pulse_and_complete_call_storage']=dict(
            independent_source_adapters=EXPECTED,composition_source_sha256=SELF_SHA,
            provider_hook_applied_before_actual_Flow_construction=True,
            nonzero_pulse_is_explicit_physical_g_change=True,
            cache_key_includes_full_physical_profile_and_compiled_provider=True,
            original_complete_equations_and_final_gates_unchanged=True,
            all_MJS_unchanged=True)
        return source,result
    return build


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--prefix-cache-directory',type=Path)
    parser.add_argument('--prefix-cache-budget-MiB',type=int,default=256)
    parser.add_argument('--inspect-prefix-cache-output',type=Path)
    parser.add_argument('--prepare-composed-source-record',type=Path)
    own,remaining=parser.parse_known_args()
    if not 1<=own.prefix_cache_budget_MiB<=256:raise ValueError('Prefix cache budget exceeds 256 MiB')
    if own.prepare_composed_source_record:
        fresh=resource.retained_module()
        configuration=dict(directory='SOURCE-ONLY-NOT-A-PRODUCTION-CACHE',budget_bytes=256*1024**2,inspect_output=None)
        source,record=resource.resource_build(composed_build(fresh.build_source,configuration),96,4)(
            dict(stage_cache_directory='SOURCE-ONLY-NOT-A-PRODUCTION-CACHE'),
            dict(temporary_parent=None,backward_error_tolerance=5e-11,heartbeat_seconds=20.))
        result=dict(scope='Exact composition and AST only; no raw, Flow, RHS, Jacobian, BVP or Node.',
            prepared=True,production_executed=False,source_bytes=len(source.encode()),
            transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),provenance=record)
        cache.atomic_new(own.prepare_composed_source_record,json.dumps(result,indent=2).encode()+b'\n')
        print(json.dumps(dict(prepared=True,production_executed=False,
            transformed_source_sha256=result['transformed_source_sha256'])),flush=True)
        return
    if own.prefix_cache_directory is None:raise ValueError('Explicit prefix cache directory is required')
    configuration=dict(directory=str(own.prefix_cache_directory.resolve()),
        budget_bytes=own.prefix_cache_budget_MiB*1024**2,
        inspect_output=str(own.inspect_prefix_cache_output.resolve()) if own.inspect_prefix_cache_output else None)
    original_retained,old_configuration,old_argv=resource.retained_module,cache.RUNTIME_CONFIGURATION,sys.argv
    def retained():
        fresh=original_retained();fresh.build_source=composed_build(fresh.build_source,configuration);return fresh
    resource.retained_module=retained;cache.RUNTIME_CONFIGURATION=configuration;sys.argv=[old_argv[0],*remaining]
    try:
        resource.main()
    except cache.InspectionComplete:
        if not own.inspect_prefix_cache_output:raise
        if not json.loads(own.inspect_prefix_cache_output.read_text()).get('passed'):
            raise ValueError('Actual composed cache check did not pass')
    finally:
        resource.retained_module=original_retained;cache.RUNTIME_CONFIGURATION=old_configuration;sys.argv=old_argv


if __name__=='__main__':main()
