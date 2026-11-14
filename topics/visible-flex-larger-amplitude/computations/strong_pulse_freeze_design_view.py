#!/usr/bin/env python3
"""Use the real fixed-view verification with the explicit pulse provider.

The complete accepted raw state, physical quintics, core, numerical/material
charts, physical tail, RMS and boundary conditions are unchanged. Only the
provider loader is extended so a saved nonzero initial_speed_pulse remains
the same physical metric. This is a representation conversion, not a solve.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE/'root_actual_freeze_design_view.py'
EXPECTED = '4209f87b8cae531f8899c5fa9af48a13666411c340981ae759daa9034315628b'
PULSE_EXPECTED = 'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73'


def transformed_source():
    sha = lambda value: hashlib.sha256(value).hexdigest()
    original = TEMPLATE.read_text()
    if sha(original.encode()) != EXPECTED:
        raise ValueError('Retained genuine fixed-view source changed')
    if sha((HERE/'strong_initial_speed_pulse.py').read_bytes()) != PULSE_EXPECTED:
        raise ValueError('The explicit physical pulse provider changed')
    edits = [
        ("        if Path(path).name == 'root_dual_core_bvp.py':\n            original_main = loaded.main",
         "        if Path(path).name == 'root_dual_core_bvp.py':\n"
         "            original_provider_loader = loaded.module\n"
         "            def pulse_provider_loader(provider_name,provider_path):\n"
         "                value = original_provider_loader(provider_name,provider_path)\n"
         "                if Path(provider_path).name=='alternative-neck-provider.py':\n"
         "                    import strong_initial_speed_pulse as pulse_hook\n"
         "                    pulse_hook.install(value)\n"
         "                return value\n"
         "            loaded.module = pulse_provider_loader\n"
         "            original_main = loaded.main"),
        ("        hashes[str(HERE / name)] = digest(HERE / name)\n    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):",
         "        hashes[str(HERE / name)] = digest(HERE / name)\n"
         "    hashes.update(PULSE_FIXED_VIEW_TRANSFORM['source_sha256'])\n"
         "    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):"),
        ("        mapped = copy.deepcopy(record)",
         "        report['initial_speed_pulse_fixed_view_adapter'] = PULSE_FIXED_VIEW_TRANSFORM\n"
         "        mapped = copy.deepcopy(record)"),
    ]
    source = original
    for before,after in edits:
        if source.count(before) != 1:
            raise ValueError('Pulse fixed-view anchor not unique: '+repr(before))
        source = source.replace(before,after,1)
    ast.parse(source,filename='<pulse-provider-original-genuine-fixed-view>')
    reverse = source
    for before,after in reversed(edits):
        if reverse.count(after) != 1:
            raise ValueError('Pulse fixed-view reverse anchor not unique')
        reverse = reverse.replace(after,before,1)
    if reverse != original:
        raise ValueError('Pulse fixed-view changed additional source')
    provenance = dict(scope=__doc__,original_sha256=EXPECTED,
        transformed_sha256=sha(source.encode()),
        source_sha256={str(TEMPLATE):EXPECTED,
            str(HERE/'strong_initial_speed_pulse.py'):PULSE_EXPECTED,
            str(Path(__file__).resolve()):sha(Path(__file__).read_bytes())},
        replacements=[dict(before=a,after=b,count=1) for a,b in edits],
        exact_reverse_recovers_original_fixed_view=True,
        pulse_is_part_of_frozen_physical_profile=True,
        original_full_H_RMS_BC_identity_and_no_worker_gates_preserved=True)
    return source,provenance


def main():
    parser = argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--prepare-pulse-source-record',type=Path)
    own,remaining = parser.parse_known_args()
    source,record = transformed_source()
    if own.prepare_pulse_source_record:
        with own.prepare_pulse_source_record.open('x') as stream:
            json.dump(dict(scope='Source-only preparation; no physical object, raw residual, BVP or worker evaluated.',
                prepared=True,conversion_executed=False,provenance=record),stream,indent=2)
            stream.write('\n')
        print(json.dumps(dict(prepared=True,conversion_executed=False,
            transformed_source_sha256=record['transformed_sha256'])),flush=True)
        return
    namespace = dict(__file__=str(Path(__file__).resolve()),
        __name__='strong_pulse_genuine_fixed_view',PULSE_FIXED_VIEW_TRANSFORM=record)
    old = sys.argv
    sys.argv = [old[0],*remaining]
    try:
        exec(compile(source,'<pulse-provider-original-genuine-fixed-view>','exec'),namespace)
        namespace['main']()
    finally:
        sys.argv = old


if __name__ == '__main__':
    main()
