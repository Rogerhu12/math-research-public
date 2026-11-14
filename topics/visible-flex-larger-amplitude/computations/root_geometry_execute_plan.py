#!/usr/bin/env python3
"""Execute owned finite geometry cases sequentially, retaining every outcome.

Each field's existing formal resource wrapper remains authoritative.  Completed
cases are reused after their full manifests and recorded hashes are checked.
A pause file is observed between fields so the main nonlinear solver may own
the larger numerical slot; this driver never interrupts another process.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def inspect_complete(row):
    resource=json.loads(Path(row['resource']).read_text())
    report=json.loads(Path(row['report']).read_text())
    field=report['geometry_fields']
    manifest=json.loads(Path(row['field']).read_text())
    if (resource['exitcode']!=0 or resource.get('termination_signal') is not None
            or not report.get('finished') or not report.get('finite_domain_passed')
            or report.get('worker_start_attempts') or report.get('nonlinear_solution')
            or report.get('true_new_H_tail_evaluated')
            or field['sha256']!=sha(row['field']) or manifest!=field['storage']
            or not manifest['complete']):
        raise ValueError('The field did not reach its complete formal outcome')
    at=0
    chunks=[]
    for item in manifest['chunks']:
        path=Path(row['field']).with_name(item['file'])
        if (item['start']!=at or item['end']<=at or path.stat().st_size!=item['bytes']
                or sha(path)!=item['sha256']):
            raise ValueError('A complete field chunk is missing or changed')
        at=item['end'];chunks.append(dict(path=str(path),sha256=item['sha256'],bytes=item['bytes']))
    if at!=manifest['shape'][0]:raise ValueError('A completed field omitted radial rows')
    return dict(exitcode=0,complete_finite_field=True,shape=manifest['shape'],
        report_sha256=sha(row['report']),resource_sha256=sha(row['resource']),
        field_manifest_sha256=sha(row['field']),chunks=chunks,
        kappa_abs_max_sample=field['kappa_abs_max_sample'],
        twice_norm_max_sample=field['twice_radius_max_sample'],
        height_abs_max_sample=field.get('height_abs_max_sample'),
        peak_rss_kib=resource['peak_rss_kib'],wall_seconds=resource['wall_seconds'],
        accepted_nonlinear_solution=False,continuous_geometry_certified=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan',type=Path,required=True)
    ap.add_argument('--ledger',type=Path,required=True)
    ap.add_argument('--cases',nargs='*')
    ap.add_argument('--pause-file',type=Path)
    args=ap.parse_args()
    plan=json.loads(args.plan.read_text())
    if Path.cwd()!=Path(plan['cwd']):raise ValueError('Preserve the prepared plan cwd')
    for path,wanted in plan['source_and_input_sha256'].items():
        if sha(path)!=wanted:raise ValueError('A prepared input/source differs: '+path)
    rows=plan['candidates']
    if args.cases:
        names={row['name'] for row in rows}
        if set(args.cases)-names:raise ValueError('An unknown field was requested')
        rows=[row for row in rows if row['name'] in args.cases]
    if args.ledger.exists():raise FileExistsError('Use a fresh driver ledger')
    ledger=dict(scope=__doc__,plan=str(args.plan),plan_sha256=sha(args.plan),
        source_sha256=sha(__file__),cwd=str(Path.cwd()),cases=[],paused=False,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        accepted_nonlinear_solution=False,continuous_geometry_certified=False)

    def save():
        args.ledger.parent.mkdir(parents=True,exist_ok=True)
        args.ledger.write_text(json.dumps(ledger,indent=2)+'\n')

    save()
    for row in rows:
        if args.pause_file and args.pause_file.exists():
            ledger['paused']=True;ledger['pending_from']=row['name'];save()
            print(json.dumps(dict(event='paused_between_fields',next=row['name'])),flush=True)
            return
        print(json.dumps(dict(event='geometry_case_start',name=row['name'])),flush=True)
        record=dict(name=row['name'],started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        if Path(row['resource']).exists() or Path(row['log']).exists() or Path(row['field']).exists():
            record['reused_existing_complete_case']=True
            try:
                record.update(inspect_complete(row))
            except (OSError,ValueError,KeyError) as error:
                record.update(complete_finite_field=False,error=repr(error),
                    existing_partial_or_failed_outputs_not_overwritten=True)
                ledger['cases'].append(record);save()
                raise RuntimeError('Use a fresh output plan for this incomplete case: '+row['name']) from error
        else:
            record['reused_existing_complete_case']=False
            with Path(row['log']).open('x') as log:
                result=subprocess.run(row['command'],stdout=log,stderr=subprocess.STDOUT,cwd=plan['cwd'])
            record['process_returncode']=result.returncode
            try:
                record.update(inspect_complete(row))
            except (OSError,ValueError,KeyError) as error:
                record.update(complete_finite_field=False,error=repr(error))
            outcome=Path(row['resource']).with_name(Path(row['resource']).stem.replace('-resource','-execution')+'.json')
            if outcome.exists():raise FileExistsError('Do not overwrite an existing execution record')
            outcome.write_text(json.dumps(record,indent=2)+'\n')
        record['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        ledger['cases'].append(record);save()
        print(json.dumps({key:record.get(key) for key in ('name','complete_finite_field',
            'reused_existing_complete_case','peak_rss_kib','wall_seconds','kappa_abs_max_sample')}),flush=True)
        if not record['complete_finite_field']:
            raise RuntimeError('The requested field failed; its formal outcome remains saved')
    ledger['all_requested_cases_completed']=True
    ledger['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();save()
    print(json.dumps(dict(event='all_requested_fields_completed',cases=len(rows),ledger=str(args.ledger))),flush=True)


if __name__=='__main__':
    main()
