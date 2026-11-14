#!/usr/bin/env python3
"""Only derive success-only M15 plans from the frozen complete M14 plans.

No globals are changed in either old planner. The new finite auditor is pinned
and replayed completely; the downstream equations, argv and thresholds stay.
"""
import ast
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent/'notes'
ANCESTORS = {
    '78718-plan-post-restart8000-v1.py':'c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456',
    '78718-plan-post-restart8000-storage-v2.py':'99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc',
}
ROWS, DIFFS = [], []


def identity(path):
    data = path.read_bytes()
    return {'path':str(path.resolve()),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def emit(old_name,new_name,changes):
    old,new = HERE/old_name,HERE/new_name
    if old_name in ANCESTORS and identity(old)['sha256'] != ANCESTORS[old_name]:
        raise ValueError('Changed reviewed ancestor: '+old_name)
    text = before = old.read_text()
    edits = []
    for a,b,count in changes:
        if text.count(a) != count:
            raise ValueError((new_name,a,text.count(a),count))
        text = text.replace(a,b)
        edits.append({'before':a,'after':b,'count':count})
    ast.parse(text)
    new.open('x').write(text)
    ROWS.append({'ancestor':identity(old),'derived':identity(new),'literal_changes':edits})
    DIFFS.extend(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile=old_name,tofile=new_name))
    return identity(new)


def main():
    base = emit('78718-plan-post-restart8000-v1.py','78718-plan-post-m15-linear-v1.py',[
        ('original post-restart8000 chain','new M15/N512/W15 post-coupled chain',1),
        ('78718-prefix-audit-restart8000-v1.py','78718-prefix-audit-m15-linear-v1.py',1),
        ('cd090888e4552317bce183c3b5788710ced9e17eea965b9489252e96d2f3496f',
         'fd41b9ef4c2eea648cbb1ab1c3b638e61bc41d97d99d9213ad0370c042ff147e',1),
        ('78718-true-m14-w14-restart8000-launch-v1','78718-true-m15-w15-n512-linear-dn-launch-v1',1),
        ('PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE',
         'PASS_ROOT_OBSERVED_M15_N512_W15_LINEAR_DN_FINITE_COUPLED_CLOSE',1),
        ('post_restart8000_full_close_audit','post_m15_linear_full_close_audit',1),
        ('Not the restart8000 launch schema','Not the M15/N512 linear-DN launch schema',1),
        ('78718-post-restart8000-success-only-original-plan-v1','78718-post-m15-linear-success-only-original-plan-v1',1),
        ('The restart8000 ancestor failed CP is a declared true input, not an independent final rerun performed here.',
         'The old matched M15 prefix remains UNSOLVED and its old local N256 DN is only a declared warm input; no independent final rerun is performed here.',1),
    ])
    storage = emit('78718-plan-post-restart8000-storage-v2.py','78718-plan-post-m15-linear-storage-v1.py',[
        ('78718-plan-post-restart8000-v1.py','78718-plan-post-m15-linear-v1.py',1),
        (ANCESTORS['78718-plan-post-restart8000-v1.py'],base['sha256'],1),
        ('2026-11-10-78718-post-restart8000-storage-v2-', '2026-11-10-78718-post-m15-linear-storage-v1-',1),
        ('Use the distinct post-restart8000-storage-v2 production namespace',
         'Use the distinct post-m15-linear-storage-v1 production namespace',1),
        ('78718-post-restart8000-success-only-conditional-storage-plan-v2',
         '78718-post-m15-linear-success-only-conditional-storage-plan-v1',1),
    ])
    emit('78718-check-post-restart8000-storage-v2.py','78718-check-post-m15-linear-plans-v1.py',[
        ('78718-plan-post-restart8000-storage-v2.py','78718-plan-post-m15-linear-storage-v1.py',1),
        (ANCESTORS['78718-plan-post-restart8000-storage-v2.py'],storage['sha256'],1),
        ('78718-post-restart8000-storage-v2-static-input-check-v1',
         '78718-post-m15-linear-storage-v1-static-input-check-v1',1),
    ])
    diff = NOTES/'2026-11-10-78718-numerical-post-m15-linear-plans-v1.diff'
    diff.open('x').write(''.join(DIFFS))
    ledger = NOTES/'2026-11-10-78718-numerical-post-m15-linear-plans-v1-sources.json'
    report = {'status':'SUCCESS_ONLY_PLAN_SOURCES_FROZEN_NO_CANDIDATE_ARGV',
              'builder':identity(Path(__file__)),'files':ROWS,'complete_diff':identity(diff),
              'main_auditor':identity(HERE/'78718-prefix-audit-m15-linear-v1.py'),
              'original_terminal_bound_exact':'1/500000000',
              'solver_calls':0,'producer_calls':0,'candidate_success_claimed':False}
    ledger.open('x').write(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'sources':len(ROWS),
                      'ledger':identity(ledger),'diff':identity(diff),'solver_calls':0}))


if __name__ == '__main__':
    main()
