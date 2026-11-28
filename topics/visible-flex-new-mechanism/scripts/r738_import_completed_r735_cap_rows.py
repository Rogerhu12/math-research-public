"""Administrative import of byte-bound, naturally completed R735 cap rows into an R738 checkpoint."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import time
import numpy as np
import scipy


def file_bytes(path,sha):
    data=Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest()!=sha:raise ValueError('Wrong administrative source '+str(path))
    return data


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public':
        raise RuntimeError('Public completed-receipt Actions consumer required.')
    start=time.monotonic()
    ap=argparse.ArgumentParser()
    for name in ('geometry','r735-bind','r735-geometry','r735-journal','r735-final','r734-journal','r734-final'):ap.add_argument('--'+name,required=True)
    z=ap.parse_args();opt=json.loads(Path(z.geometry).read_bytes());req=json.loads(Path(os.environ['R738_REQUEST']).read_bytes())
    def bound(path):
        p=Path(path);key=p.as_posix()
        if key not in req['source_sha256']:
            root=Path(os.environ['GITHUB_WORKSPACE']);key=p.resolve().relative_to(root.resolve()).as_posix()
        return file_bytes(p,req['source_sha256'][key])
    runtime=(Path(os.environ['RUNNER_TEMP'])/'r735-completed-donor-binding.json').resolve()
    if Path(z.r735_bind).resolve()==runtime:
        bind=json.loads(runtime.read_bytes());expected=req['completed_r735']
        keys=('source_run','source_job','source_head','source_run_conclusion','artifact','zip_bytes','zip_sha256',
              'journal_member','terminal_sha256','terminal_bytes')
        if any(k not in bind or bind[k]!=expected[k] for k in keys):
            raise ValueError('Transported donor differs from the exact completed source requested.')
        if (bind.get('member_zip_verified') is not True or
                Path(bind['journal_member']).name!='central.jsonl' or Path(bind['journal_member']).is_absolute()
                or '..' in Path(bind['journal_member']).parts):
            raise ValueError('A member verified inside the bound original ZIP is required.')
        if Path(z.r735_journal).stat().st_size!=bind['journal_bytes'] or Path(z.r735_final).stat().st_size!=bind['terminal_bytes']:
            raise ValueError('Incorrect exact donor member length.')
        for name,digest in bind['donor_source_sha256'].items():
            dep='topics/visible-flex-new-mechanism/scripts/'+name
            if req['source_sha256'].get(dep)!=digest:raise ValueError('Donor and current scientific source bytes differ.')
    else:
        bind=json.loads(bound(z.r735_bind))
    oldcfg=json.loads(bound(z.r735_geometry));bound(z.geometry)
    if bind['source_run_conclusion']!='success' or not bind['source_run'] or not bind['source_job'] or not bind['source_head']:
        raise ValueError('Natural donor metadata required.')
    # The workflow verifies donor job, immutable archive metadata, actual ZIP bytes, member names and literal hashes.
    old=json.loads(file_bytes(z.r734_final,opt['paid_r734']['terminal_sha256']))
    source=file_bytes(z.r734_journal,opt['paid_r734']['journal_sha256'])
    donor=json.loads(file_bytes(z.r735_final,bind['terminal_sha256']))
    paid=file_bytes(z.r735_journal,bind['journal_sha256'])
    if (donor['prior_R734_fingerprint']!=old['source_fingerprint'] or donor['prior_R734_paid_units']!=8558
            or oldcfg['paid_r734']!=donor['prior_R734_metadata'] or oldcfg['paid_r734']!=opt['paid_r734']):
        raise ValueError('Different original R734 cap normalization or receipt.')
    d=Path(__file__).resolve().parent;h=hashlib.sha256()
    for name in ('r734_true_dyadic_tail.py','r735_paid_tail_beta_envelope.py','r735_actual_two_port_match.py'):
        h.update(file_bytes(d/name,bind['donor_source_sha256'][name]))
    h.update(json.dumps({k:v for k,v in oldcfg.items() if k not in ('maximum_depth','maximum_head')},sort_keys=True).encode())
    if h.hexdigest()!=donor['new_fingerprint']:raise ValueError('Donor script/geometry differs from paid enclosure.')
    depths={}
    for line in source.splitlines():
        a=json.loads(line);m=re.fullmatch(r'side(-?1)_m([23])_n(\d+)_accepted_line',a['key'])
        if m:depths[tuple(map(int,m.groups()))]=a['value']['data']['depth']
    totals={j:old['completed_modes']['outer'+str(j)]['asymptotic_cone']['cone_index'] for j in (2,3)}
    if totals!={2:78,3:89}:raise ValueError('Unexpected original depths.')
    seen=set();chosen={}
    for line in paid.splitlines():
        a=json.loads(line);key=a['key']
        if key in seen or a['fingerprint']!=donor['new_fingerprint']:raise ValueError('Mixed paid donor journal.')
        seen.add(key)
        m=re.fullmatch(r'absolute_cap_side(-?1)_j([23])_n(\d+)',key)
        if not m:continue
        sg,j,n=map(int,m.groups());v=a['value']['data']
        if n>=totals[j] or n!=v['true_cell'] or v['accepted_R734_depth']!=depths[sg,j,n]:
            raise ValueError('Donor cap row does not reference this exact original cell.')
        chosen[key]=a['value']
    if len(seen)!=donor['total_new_units']:raise ValueError('Incomplete donor journal.')
    if not chosen:raise ValueError('No genuine cap rows to transport.')
    scripts={k:v for k,v in req['source_sha256'].items() if k.endswith('.py')}
    semantic=dict(schema='r738-native-v1',sources=scripts,geometry=opt,runtime=[np.__version__,scipy.__version__])
    fid=hashlib.sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    folder=Path(os.environ['RUNNER_TEMP'])/'r738-paid';folder.mkdir(parents=True,exist_ok=True)
    ledger=folder/'ledger.json'
    if ledger.is_file() and json.loads(ledger.read_bytes())['fingerprint']!=fid:raise ValueError('Wrong R738 restore target.')
    target=folder/'r738-negative-and-deep.jsonl'
    original=target.read_bytes() if target.is_file() else b''
    if original and not original.endswith(b'\n'):raise ValueError('Truncated original R738 receipt.')
    merged={};rows=[]
    for line in original.splitlines():
        r=json.loads(line);k=r['key']
        if r['identity']!=fid or k in merged:raise ValueError('Mixed existing R738 tail journal.')
        if k in chosen and r['value']['data']!=chosen[k]['data']:raise ValueError('Existing paid cap data disagree.')
        merged[k]=r['value']
    manifest=folder/'r735-cap-row-import.json'
    previous=json.loads(manifest.read_bytes()) if manifest.is_file() else {}
    if previous and (previous['recipient_fingerprint']!=fid or previous['donor_fingerprint']!=donor['new_fingerprint']):
        raise ValueError('Previous R735 transfer metadata differs.')
    imported=set(previous.get('net_imported_keys',[]));shared=sorted(set(merged)&set(chosen))
    for key,value in chosen.items():
        if key in merged:continue
        rows.append(json.dumps(dict(key=key,value=value,identity=fid),separators=(',',':'),allow_nan=False).encode()+b'\n')
        imported.add(key)
    # Prepare both files before the side effect. Re-run is idempotent if interrupted between renames.
    pending=folder/'r735-cap-import-intent.json'
    if pending.exists():
        intent=json.loads(pending.read_bytes())
        if intent['recipient_fingerprint']!=fid or intent['donor_fingerprint']!=donor['new_fingerprint']:
            raise ValueError('Different pending cap transfer.')
        imported.update(intent['net_imported_keys'])
    if not imported.issubset(chosen):raise ValueError('Invalid imported provenance set.')
    report=dict(recipient_fingerprint=fid,donor_fingerprint=donor['new_fingerprint'],source_job=bind['source_job'],
         donor_original_journal_sha256=bind['journal_sha256'],donor_original_final_sha256=bind['terminal_sha256'],
         eligible_actual_donor_keys=len(chosen),eligible_when_all_complete=334,additional_rows_this_invocation=len(rows),
         existing_identical_keys=len(shared),net_imported_keys=sorted(imported),net_imported_keys_count=len(imported),
         inherited_per_unit_seconds=sum(chosen[k]['seconds'] for k in imported),
         donor_cumulative_cost_fields={k:donor[k] for k in ('total_new_units','current_elapsed_seconds','previous_new_paid_seconds')},
         recipient_count_beyond_R734_includes_imported=True,new_scientific_evaluations=0)
    def atom(path,body):
        tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_bytes(body);os.replace(tmp,path)
    encode=lambda obj:json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    atom(pending,encode(report))
    if rows:atom(target,original+b''.join(rows))
    report['administrative_seconds']=time.monotonic()-start
    atom(manifest,encode(report));pending.unlink(missing_ok=True)
    print('R738_IMPORTED_CAP_RECEIPTS',json.dumps(report,sort_keys=True,separators=(',',':')),flush=True)


if __name__=='__main__':main()
