#!/usr/bin/env python3
"""Read a bounded actual failed-child traceback inside the same public runner.

The full controller journal and log stay in runner scratch. No scientific
arrays, field operators, report arithmetic or retry is executed here.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--step-id',required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('Read actual scientific-run failure evidence only in public repository Actions')
    work=a.work.resolve();journal_path=work/'followup-journal.json'
    journal=json.loads(journal_path.read_text())
    matches=[x for x in journal['records'] if x.get('step_id')==a.step_id]
    if len(matches)!=1:raise ValueError('Need exactly one naturally returned actual followup record')
    r=matches[0]
    if r.get('state')!='failed':raise ValueError('The named actual followup did not fail')
    path=Path(r['log']).resolve()
    if work not in path.parents or path.parent!=work/'followup-logs':
        raise ValueError('Actual failed-child log must remain in the same runwork log directory')
    body=''
    if path.is_file():
        with path.open('rb') as stream:
            stream.seek(max(0,path.stat().st_size-64000))
            body=stream.read().decode(errors='replace')
    blocks=body.split('Traceback (most recent call last):')[1:]
    traces=[];exceptions=[]
    for block in blocks:
        lines=[]
        for line in block.splitlines():
            if line.startswith(('subprocess.CalledProcessError:','TypeError:','ValueError:',
                    'RuntimeError:','KeyError:','FileNotFoundError:','AssertionError:',
                    'AttributeError:','IndexError:','ImportError:','NameError:')):
                exceptions.append(line[:1200])
            if line.lstrip().startswith('{'):
                continue
            lines.append(line if len(line)<=700 else line[:700]+' [line shortened]')
        traces.append('Traceback (most recent call last):'+ '\n'.join(lines))
    trace='\n'.join(traces)[:6000]
    trace=re.sub(r'(?:github_pat_|gh[pousr]_)[A-Za-z0-9_]+','[redacted-token]',trace)
    exceptions=[re.sub(r'(?:github_pat_|gh[pousr]_)[A-Za-z0-9_]+',
        '[redacted-token]',value) for value in exceptions]
    exception=exceptions[-1] if exceptions else None
    summary=dict(schema='actual-returned-followup-failure-trace-v2',
        reader_sha256=sha(__file__),github_run_id=os.environ.get('GITHUB_RUN_ID'),
        step_id=a.step_id,actual_state=r['state'],actual_returncode=r.get('returncode'),
        actual_source_commit=r.get('source_commit'),actual_source_sha256=r.get('source_sha256'),
        actual_parent_sha256=r.get('parent_sha256'),actual_seconds=r.get('seconds'),
        actual_log_sha256=sha(path) if path.is_file() else None,
        actual_log_bytes=path.stat().st_size if path.is_file() else None,
        actual_exception_line=exception,actual_traceback_tail=trace or None,
        actual_exception_lines_json=json.dumps(exceptions,ensure_ascii=False),
        actual_traceback_count=len(blocks),
        actual_setup_error=r.get('metrics',{}).get('setup_error'),
        actual_reported_output_count=len(r.get('outputs',[])),
        trace_is_bounded=True,full_log_published=False,
        field_evaluations=0,J_calls=0,scientific_arrays_read=0,retry_performed=False)
    if a.out.exists():raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(summary,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),actual_exception_line=exception)),flush=True)


if __name__=='__main__':main()
