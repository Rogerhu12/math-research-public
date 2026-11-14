#!/usr/bin/env python3
"""Fresh actual continuation with exact complete-call prefix persistence.

Original fixed-S Newton, disk QR, true full-H tail and all final gates remain.
The new Python storage wrapper never changes a mathematical source or MJS.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
RESOURCE_SHA='26f0c2ba1bdbb413ba7819f8f1aaafa7892787a7e14509357b6a28821e8c808f'
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def build_wrapper(original, configuration):
    def build(merit,disk):
        source,record=original(merit,disk)
        edits=[
            ('    domain_runtime = DomainObservation(out, FRESH_MERIT_CONFIGURATION, hashes, emit=merit_runtime.emit)',
             '    domain_runtime = DomainObservation(out, FRESH_MERIT_CONFIGURATION, hashes, emit=merit_runtime.emit)\n'
             '    from strong_prefix_evaluation_cache import Runtime as PrefixCacheRuntime\n'
             "    prefix_cache = PrefixCacheRuntime(out, hashes, Path(argument('--source-topic')), bounded.adapter,\n"
             "        dict(radial=options.radial_batch_size,collocation=options.collocation_batch_size))"),
            ('                domain_runtime.install_class(cls)',
             '                domain_runtime.install_class(cls)\n                prefix_cache.install_class(cls)'),
            ('                    if options.inspect_local_output:',
             "                    if prefix_cache.configuration.get('inspect_output'):\n"
             '                        return prefix_cache.inspect(self,x,y,p)\n'
             '                    if options.inspect_local_output:'),
            ('        domain_runtime.finish()',
             '        prefix_cache.finish()\n        domain_runtime.finish()'),
            ("    source_names = ('strong_actual_three_control_bvp.py', 'strong_actual_augmented_core.py',",
             "    source_names = ('strong_cached_prefix_actual_bvp.py', 'strong_prefix_evaluation_cache.py',\n"
             "        'strong_actual_three_control_bvp.py', 'strong_actual_augmented_core.py',")]
        for before,after in edits:
            if source.count(before)!=1:
                raise ValueError('Complete-call cache transform anchor is not unique: '+repr(before))
            source=source.replace(before,after,1)
        ast.parse(source,filename='<actual-complete-call-prefix-cache>')
        result=dict(record)
        result['source_sha256']=dict(record['source_sha256'])
        for name in ('strong_cached_prefix_actual_bvp.py','strong_prefix_evaluation_cache.py'):
            result['source_sha256'][str(HERE/name)]=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        result['prior_transformed_source_sha256']=record['transformed_source_sha256']
        result['transformed_source_sha256']=hashlib.sha256(source.encode()).hexdigest()
        result['replacements']=list(record['replacements'])+[dict(before=a,after=b,count=1) for a,b in edits]
        result['exact_prefix_call_storage']=dict(configuration,
            original_equations_assembly_RMS_boundary_true_H_audit_unchanged=True,
            complete_state_and_parameter_Jacobian_outputs=True,
            cached_complete_inputs_required=True, MJS_unchanged=True)
        return source,result
    return build


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--prefix-cache-directory',type=Path,required=True)
    parser.add_argument('--prefix-cache-budget-MiB',type=int,default=192)
    parser.add_argument('--inspect-prefix-cache-output',type=Path)
    own,remaining=parser.parse_known_args()
    if not 1<=own.prefix_cache_budget_MiB<=256:
        raise ValueError('Prefix cache budget is explicitly bounded at 256 MiB')
    path=HERE/'strong_fresh_resource_actual_bvp.py'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=RESOURCE_SHA:
        raise ValueError('Retained fresh resource entry differs')
    spec=importlib.util.spec_from_file_location('strong_cached_prefix_resource',path)
    entry=importlib.util.module_from_spec(spec);spec.loader.exec_module(entry)
    import strong_prefix_evaluation_cache as cache
    config=dict(directory=str(own.prefix_cache_directory.resolve()),
        budget_bytes=own.prefix_cache_budget_MiB*1024**2,
        inspect_output=str(own.inspect_prefix_cache_output.resolve()) if own.inspect_prefix_cache_output else None)
    old_configuration=cache.RUNTIME_CONFIGURATION
    cache.RUNTIME_CONFIGURATION=config
    retained=entry.retained_module
    def load():
        fresh=retained()
        fresh.build_source=build_wrapper(fresh.build_source,config)
        return fresh
    entry.retained_module=load
    old_argv=sys.argv;sys.argv=[old_argv[0],*remaining]
    try:
        entry.main()
    except cache.InspectionComplete:
        if not own.inspect_prefix_cache_output:
            raise
        result=json.loads(own.inspect_prefix_cache_output.read_text())
        if not result.get('passed'):
            raise ValueError('No completed actual prefix cache equivalence check')
    finally:
        sys.argv=old_argv
        cache.RUNTIME_CONFIGURATION=old_configuration
        entry.retained_module=retained


if __name__=='__main__':main()
