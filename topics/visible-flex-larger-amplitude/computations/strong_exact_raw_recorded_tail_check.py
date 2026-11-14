#!/usr/bin/env python3
"""Original audited-H protocol checks with an explicit primary ready record.

Seven original checks run with one true packet. The three optional live-release
checks require a second true audited packet of the same numerical source set;
no substitute response or relabelled source identity is manufactured.
"""
from pathlib import Path
import hashlib
HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_actual_recorded_tail_check.py'
EXPECTED='e009628fe6a94f8537a6513c6a017e18948c4f9024b94c8dfe7660b627548f5d'
EDITS=[("    parser.add_argument('--second-packet', type=Path)", "    parser.add_argument('--packet-ready', type=Path)\n    parser.add_argument('--second-packet', type=Path)"), ('    checks = {}', '    if args.packet_ready:\n        hashes[str(args.packet_ready)] = sha(args.packet_ready)\n    hashes[str(EXACT_RAW_CHECK_ENTRY)] = sha(EXACT_RAW_CHECK_ENTRY)\n    checks = {}'), ("        ready_file.write_text(json.dumps(reference['actual_tail']['ready']))", "        ready_file.write_text(json.dumps(read(args.packet_ready) if args.packet_ready else reference['actual_tail']['ready']))"), ('    report = dict(scope=__doc__, passed=', '    report = dict(scope=__doc__, source_transform=EXACT_RAW_CHECK_TRANSFORM, passed=')]

def main():
    original=TEMPLATE.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=EXPECTED:
        raise ValueError('Original protocol-check source changed')
    source=original
    for before,after in EDITS:
        if source.count(before)!=1:raise ValueError('Protocol source anchor changed')
        source=source.replace(before,after)
    namespace=dict(__file__=str(TEMPLATE),__name__='strong_exact_raw_recorded_check',
        EXACT_RAW_CHECK_ENTRY=Path(__file__),EXACT_RAW_CHECK_TRANSFORM=dict(
        template_sha256=EXPECTED,transformed_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a,after=b,count=1) for a,b in EDITS]))
    exec(compile(source,str(TEMPLATE)+':explicit-ready','exec'),namespace)
    namespace['main']()

if __name__=='__main__':main()
