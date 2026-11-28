#!/usr/bin/env python3
"""Reserve only the next native input after the current final fresh J is done.

The current request must not request an output height Jacobian: after its
successful final fresh-J trace, the original source uses only its original JS
cut/audit path before returning and recording that request.  A new directory
at the NEXT native input pathname prevents any later request from entering
native integration.  The previous packet and its accepted summary row remain
unmodified.  The later EEXIST response is an explicit execution handoff, never
a mathematical rejection.  No source, native executable, or manifest changes.
"""
import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path
import time


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--stage-dir', type=Path, required=True)
    p.add_argument('--call', type=int, required=True)
    p.add_argument('--tolerance', type=float, default=2e-9)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    stage = a.stage_dir.resolve()
    trace = stage/'worker-trace.jsonl'
    native = stage/'native-runs'
    while True:
        rows = []
        if trace.exists():
            for line in trace.read_text().splitlines():
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
        requests = [r for r in rows if r.get('event') == 'request']
        if requests and requests[-1].get('call', 0) > a.call:
            raise RuntimeError('The successor request already began; no late barrier is installed')
        req = next((r for r in requests if r.get('call') == a.call), None)
        if req is not None and req.get('jacobian') is not False:
            raise ValueError('The safe source boundary is for an output-J-free current request only')
        failures = [r for r in rows if r.get('call') == a.call and r.get('event') == 'failure']
        if failures:
            raise RuntimeError('Current request actually failed before the scheduling boundary')
        accepted_j = [r for r in rows if r.get('event') == 'iteration' and r.get('call') == a.call
            and r.get('jacobianMode') in ('fresh-J', 'fresh-final-J')
            and not r.get('phase') and isinstance(r.get('norm'), (int, float))
            and math.isfinite(r['norm']) and 0 <= r['norm'] < a.tolerance]
        if accepted_j:
            if req is None or req.get('audit') is not True:
                raise ValueError('Original audited current request was not observed')
            records = sorted(native.glob('*-record.json'))
            if not records:
                raise ValueError('No actual native evaluation is retained')
            last_path = records[-1]
            last = json.loads(last_path.read_text())
            if last.get('withJac') is not True or last.get('status') != 'complete' or last.get('returncode') != 0:
                raise ValueError('The last actual native call is not a completed full J')
            for key in ('input', 'output', 'manifest', 'static_metadata'):
                if ref(last[key]['path']) != last[key]:
                    raise ValueError('Changed final original native evidence: '+key)
            next_call = int(last['call'])+1
            barrier = native/f'{next_call:04d}-jac-input.bin'
            barrier.mkdir(exist_ok=False)
            result = dict(scope=__doc__, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                source=ref(__file__), current_request=req, final_fresh_J_trace=accepted_j[-1],
                completed_native_record=ref(last_path), barrier_path=str(barrier),
                next_native_call=next_call, original_current_equations_interrupted=False,
                current_request_original_audit_still_required=True,
                original_current_packet_or_summary_modified=False,
                native_source_or_binary_modified=False, subsequent_native_integration_prevented=True,
                current_request_accepted=False,
                acceptance_scope='Only a later real original packet and its acceptance row may establish current-request acceptance')
            (barrier/'scheduling-barrier.json').write_text(json.dumps(result, indent=2)+'\n')
            a.out.parent.mkdir(parents=True, exist_ok=True)
            a.out.write_text(json.dumps(result, indent=2)+'\n')
            print(json.dumps(result), flush=True)
            return
        time.sleep(.25)


if __name__ == '__main__':
    main()
