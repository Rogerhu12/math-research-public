#!/usr/bin/env python3
"""Exact text/identity check for R32/R33 adoption; no scalar or solver rerun."""
import argparse
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
SPECS = [
    ('2026-11-09-db6f-audit-c3-exact-diameter.md',
     'R32-c3-n7-exact-global-diameter.md',
     '3fdc8b16d5e54bbc56d054328695142838fb4f5f28b2205ecb015f8ec5fc3e16',
     [('状态：完整有限有理证明及实际标量账本已生成，待另一代理全文独审。',
       '状态：已证明；完整有限有理证明及标量账本已获全文独审和独立算术重放。')]),
    ('2026-11-09-db6f-audit-fixed-marker-diameter-model-v2.md',
     'R33-fixed-marker-diameter-gap-and-one-sided-transfer.md',
     '9868f6e4d2a95613154776e37ff51f936411e192d3c3b2fea64902ec5ba471a9',
     [('状态：新通用证明及固定有理模型账本，待独立全文审查。',
       '状态：已证明；新通用证明及固定有理模型账本已经全文独审和独立算术重放。'),
      ('所有当前结论仍待另一代理的完整独审。',
       '上述全文已由未参与新增证明实现者独立审查通过，详见本文件采纳说明。')]),
]


def identity(p):
    p = Path(p).resolve()
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    out = a.out.resolve()
    assert out.parent.is_dir() and not out.exists()
    ledger_path = TOPIC / 'notes/2026-11-09-db6f-root-r32-r34-adoption-check.json'
    ledger = json.loads(ledger_path.read_text())
    assert len(ledger['checked_files']) == 27
    verified = []
    for row in ledger['checked_files']:
        x = identity(REPO / row['path'])
        assert x['bytes'] == row['bytes'] and x['sha256'] == row['sha256']
        verified.append(x)
    results = []
    for source_name, result_name, expected_sha, replacements in SPECS:
        source, result = TOPIC / 'notes' / source_name, TOPIC / 'results' / result_name
        original, adopted = source.read_text(), result.read_text()
        assert identity(result)['sha256'] == expected_sha
        # Remove the old title only. The independently stated replacements
        # concern status sentences, never formulas/assumptions/parameters.
        body = original.split('\n', 1)[1].lstrip('\n')
        for old, new in replacements:
            assert body.count(old) == 1
            body = body.replace(old, new, 1)
        assert adopted.count('\n---\n\n') == 1
        introduction, actual_body = adopted.split('\n---\n\n')
        assert body == actual_body
        assert '不是 README 完成结果' in introduction
        assert '全时嵌入/完整 reach' in introduction and 'G5' in introduction
        if result_name.startswith('R32'):
            assert '并非整个闭面直径' in introduction
        else:
            assert '完整单向凸包包围与实际点见证' in introduction
            assert '不能由连通像实现' in introduction
        root_entry = next(x for x in ledger['adoptions'] if Path(x['result']['path']).name == result_name)
        assert hashlib.sha256(body.encode()).hexdigest() == root_entry['proof_body_after_metadata_sha256']
        results.append({'source': identity(source), 'result': identity(result),
                        'metadata_sentence_replacements': len(replacements),
                        'full_body_after_exact_metadata_replacements_identical': True,
                        'body_sha256': hashlib.sha256(body.encode()).hexdigest(),
                        'mathematical_formula_hypothesis_parameter_changes': False})
    report = {'status': 'PASS_R32_R33_FORMAL_ADOPTION_TEXT_AND_SCOPE',
              'scope': 'Only R32/R33 proof-copy and scope review. The shared 27-file root ledger is rehashed; R34 is not newly mathematically reviewed here. No scalar recomputation, root, flow, BVP or candidate.',
              'script': identity(Path(__file__)), 'root_ledger': identity(ledger_path),
              'shared_root_ledger_source_count_rehashed': len(verified),
              'shared_root_ledger_sources': verified, 'adoptions': results,
              'solver_calls': 0, 'new_scalar_runs': 0}
    data = (json.dumps(report, indent=2, ensure_ascii=False) + '\n').encode()
    assert len(data) < 100000
    with out.open('xb') as f:
        f.write(data)
    print(json.dumps({'status': report['status'], **identity(out)}))


if __name__ == '__main__':
    main()
