#!/usr/bin/env python3
"""Original actual M+3 continuation with explicit exact-raw same-grid tail warm storage.

No prefix equation, Newton gate, full-H tail acceptance or audited-cache guard
changes. Every changed H still uses the original live nonlinear tail solve.
"""
from pathlib import Path
import hashlib

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_actual_three_control_bvp.py'
EXPECTED='a84c8587c8ed605fdc0627c1183d79ff0afaa26d21f2b78e00c7091fa5ba6da4'
EDITS=[("        'strong_frozen_calibration_factory.mjs', 'strong_actual_recorded_tail_port.py')", "        'strong_frozen_calibration_factory.mjs', 'strong_actual_recorded_tail_port.py',\n        'strong_exact_raw_three_control_bvp.py', 'strong_exact_raw_tail_client.py',\n        'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs')"), ('    provenance = dict(scope=__doc__, status=', '    provenance = dict(scope=__doc__, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status='), ("        if path.name == 'tail_frozen_client.py' and options.initial_audited_tail_packet:", "        if path.name == 'tail_frozen_client.py':\n            loaded = original_loader(name+'_exact_raw', HERE/'strong_exact_raw_tail_client.py')\n        if path.name == 'tail_frozen_client.py' and options.initial_audited_tail_packet:")]

def main():
    original=TEMPLATE.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=EXPECTED:
        raise ValueError('Actual production source changed before exact-raw wrapping')
    source=original
    for before,after in EDITS:
        if source.count(before)!=1:
            raise ValueError('Actual exact-raw source anchor is not unique')
        source=source.replace(before,after)
    provenance=dict(scope=__doc__,template_sha256=EXPECTED,
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in EDITS],
        only_same_discretization_raw_warm_and_GC_changes=True,
        original_mathematical_equations_and_all_acceptance_preserved=True)
    namespace=dict(__file__=str(TEMPLATE),__name__='strong_exact_raw_actual_source',
        EXACT_RAW_SOURCE_TRANSFORM=provenance)
    exec(compile(source,str(TEMPLATE)+':exact-raw-adapter','exec'),namespace)
    namespace['main']()

if __name__=='__main__':main()
