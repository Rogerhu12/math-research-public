#!/usr/bin/env python3
"""Run the unchanged complete-mean warm geometry with explicit inlet laws.

The retained actual entry receives the already reviewed optional-default
augmented core and the identical provider installation order angle, pulse,
then frontload. The full raw interpolation, mean, Cartesian jet, and finite
geometry loops are unchanged. A missing zero frontload is never inserted
into an accepted profile. Every nonzero response must be from the same
accepted field's complete actual Jacobian. No new solution is certified.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
EXPECTED={
 'strong_actual_three_control_bvp.py':'a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4',
 'strong_monotone_initial_speed.py':'12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
 'strong_initial_speed_pulse.py':'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
 'strong_initial_laws_augmented_core.py':'067940d3d2f581beebf1fd64e0649c80d9d5eaa61052fa8c2ab6cd54f5004646',
}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prepare_entry():
    import strong_actual_three_control_bvp as entry
    from strong_initial_laws_augmented_core import transformed_source
    source_inputs={}
    for name,wanted in EXPECTED.items():
        got=sha(HERE/name)
        if wanted is not None and got!=wanted:raise ValueError('Pinned actual initial-law geometry source changed: '+name)
        source_inputs[str(HERE/name)]=got
    unused,augmented=transformed_source()
    original=inspect.getsource(entry.main)
    edits=[
      ('    import strong_actual_augmented_core as augmented\n',
       '    from strong_initial_laws_augmented_core import load_augmented_core\n'
       '    augmented = load_augmented_core()\n'),
      ("        **{name: reference['frozen_profile'][name]+value for name, value in external_shifts.items()}}",
       "        **{name: (reference['frozen_profile'].get(name,0.) if name in ('initial_speed_pulse','initial_speed_frontload') else reference['frozen_profile'][name])+value for name, value in external_shifts.items()}}"),
      ('        source_factory = loaded.make_dual\n        original_main = loaded.main',
       '        original_provider_loader = loaded.module\n'
       '        def initial_laws_provider_loader(provider_name,provider_path):\n'
       '            value = original_provider_loader(provider_name,provider_path)\n'
       "            if Path(provider_path).name=='alternative-neck-provider.py':\n"
       "                if not getattr(value,'_strong_angle_boost_installed',False):\n"
       "                    raise ValueError('Original angle hook must be installed before inlet laws')\n"
       '                import strong_initial_speed_pulse as pulse_hook\n'
       '                pulse_hook.install(value)\n'
       '                import strong_monotone_initial_speed as frontload_hook\n'
       '                frontload_hook.install(value)\n'
       '            return value\n'
       '        loaded.module = initial_laws_provider_loader\n'
       '        source_factory = loaded.make_dual\n        original_main = loaded.main'),
      ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
       "    source_names += ('root_actual_geometry_field_initial_laws.py','strong_initial_laws_augmented_core.py',"
       "'strong_pulse_augmented_core.py','strong_initial_speed_pulse.py','strong_monotone_initial_speed.py')\n"
       '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'),
    ]
    source=original
    for before,after in edits:
        if source.count(before)!=1:raise ValueError('Initial-law geometry anchor must be unique')
        source=source.replace(before,after,1)
    ast.parse(source,filename='<actual-fullmean-geometry-initial-laws>')
    reverse=source
    for before,after in reversed(edits):
        if reverse.count(after)!=1:raise ValueError('Initial-law geometry reverse anchor differs')
        reverse=reverse.replace(after,before,1)
    if reverse!=original:raise ValueError('Initial-law geometry changed extra actual entry code')
    namespace=dict(entry.main.__globals__)
    if 'initial_speed_frontload' in namespace['EXTERNAL']:raise ValueError('The old control list is no longer the reviewed source')
    namespace['EXTERNAL']=(*namespace['EXTERNAL'],'initial_speed_frontload')
    exec(compile(source,'<actual-fullmean-geometry-initial-laws>','exec'),namespace)
    record=dict(schema='actual-fullmean-geometry-initial-laws-source-v1',scope=__doc__,
        source_sha256=sha(__file__),source_inputs=source_inputs,
        original_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        original_augmented_default_adapter=augmented,
        source_transforms=[dict(before=x,after=y,count=1) for x,y in edits],
        exact_reverse_recovers_original_main=True,
        reviewed_external_controls=list(namespace['EXTERNAL']),
        complete_mean_original_source_sha256=sha(HERE/'root_actual_geometry_field_complete_mean.py'),
        provider_install_order=['original angle at provider import','pulse','frontload'],
        absent_frontload_zero_profile_keys_inserted=False,
        actual_fullmean_geometry_or_new_solution_executed=False)
    return entry,namespace['main'],record


def main():
    ap=argparse.ArgumentParser(add_help=False,description=__doc__)
    ap.add_argument('--geometry-initial-laws-prepare-only',type=Path)
    own,remaining=ap.parse_known_args()
    entry,patched,record=prepare_entry()
    if own.geometry_initial_laws_prepare_only:
        out=own.geometry_initial_laws_prepare_only
    else:
        if '--inspect-warm-output' not in remaining or remaining.count('--out-prefix')!=1:
            raise ValueError('Only explicit full-mean warm geometry is supported')
        out=Path(remaining[remaining.index('--out-prefix')+1]+'-initial-laws-geometry-source.json')
    if out.exists():raise FileExistsError('Use a fresh initial-law geometry provenance path')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(record,indent=2)+'\n')
    if own.geometry_initial_laws_prepare_only:
        print(json.dumps(dict(prepared_only=True,ODE_Node_Flow_calls=0,out=str(out),sha256=sha(out))),flush=True);return
    import root_actual_geometry_field_complete_mean as geometry
    old_main,old_argv=entry.main,sys.argv
    entry.main=patched;sys.argv=[old_argv[0],*remaining]
    try:
        geometry.main()
        for p,h in record['source_inputs'].items():
            if sha(p)!=h:raise ValueError('A provider input changed during the complete geometry field')
    finally:entry.main,sys.argv=old_main,old_argv


if __name__=='__main__':main()
