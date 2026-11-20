#!/usr/bin/env python3
"""Preserve every manifest value while compacting whitespace in public Actions.

Also read bounded tails from explicitly named returned logs. This performs
no field or scalar evaluation and does not change a source driver or gate.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--log',type=Path,action='append',default=[])
    p.add_argument('--journal',type=Path)
    p.add_argument('--step-id',action='append',default=[])
    a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise SystemExit('Run this actual returned-file preparation in the stated public repository Actions.')
    if a.output.exists() or a.report.exists():
        raise FileExistsError('Preserve the previous manifest and metadata.')
    value=json.loads(a.input.read_text())
    if not isinstance(value,dict) or not all(isinstance(value.get(k),list) for k in ('curvature_points','radius_points')):
        raise ValueError('Need the complete immutable geometric position manifest.')
    compact=json.dumps(value,separators=(',',':'),ensure_ascii=False,allow_nan=False)+'\n'
    if json.loads(compact)!=value:
        raise ValueError('Compaction changed a manifest value.')
    if len(compact.encode())>100000:
        raise ValueError('Complete compact manifest still exceeds the frozen driver byte limit; no points may be dropped.')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(compact)
    logs=list(a.log)
    if a.journal:
        journal=json.loads(a.journal.read_text())
        for wanted in a.step_id:
            for record in journal.get('records',[]):
                if record.get('step_id')==wanted and record.get('log'):
                    logs.append(Path(record['log']))
    tails=[]
    for log in logs:
        item=dict(path=str(log.resolve()),exists=log.is_file())
        if log.is_file():
            raw=log.read_bytes()
            text=raw[-12000:].decode(errors='replace')
            lines=text.splitlines()[-24:]
            item.update(sha256=sha(log),bytes=len(raw),last_lines='\n'.join(lines)[-6000:])
        tails.append(item)
    result=dict(schema='complete-geometric-position-whitespace-compaction-v1',source_sha256=sha(__file__),
        execution={k:os.environ.get(k) for k in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')},
        input_path=str(a.input.resolve()),input_sha256=sha(a.input),input_bytes=a.input.stat().st_size,
        output_path=str(a.output.resolve()),output_sha256=sha(a.output),output_bytes=a.output.stat().st_size,
        json_value_equality=True,all_keys_and_ordered_positions_preserved=True,
        curvature_points=len(value['curvature_points']),radius_points=len(value['radius_points']),
        protected_curvature_points=len(value.get('protected_curvature_points',[])),
        field_evaluations=0,logs=tails,scope='Whitespace compaction only; original complete manifest remains unchanged; actual child failures are read, never inferred as scientific rejection.')
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,allow_nan=False),flush=True)


if __name__=='__main__':
    main()
