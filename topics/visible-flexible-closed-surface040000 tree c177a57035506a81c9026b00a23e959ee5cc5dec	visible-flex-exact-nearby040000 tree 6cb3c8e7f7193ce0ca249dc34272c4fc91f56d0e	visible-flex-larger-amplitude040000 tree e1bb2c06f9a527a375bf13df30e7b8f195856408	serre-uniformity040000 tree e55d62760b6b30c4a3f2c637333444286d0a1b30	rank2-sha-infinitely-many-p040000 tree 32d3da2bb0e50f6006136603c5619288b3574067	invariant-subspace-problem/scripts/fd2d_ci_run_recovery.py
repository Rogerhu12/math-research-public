#!/usr/bin/env python3
"""Finite CI research batch with real exits, rule checks and selected outputs.

New recovery source: not executed merely by committing this file.
Commands are argv arrays run in the topic directory; shell=False.
No credential values are read, serialized or intentionally printed.
"""
from __future__ import annotations
import argparse,datetime,gzip,hashlib,json,os,re,subprocess,sys,time
from pathlib import Path,PurePosixPath

TOPIC='topics/visible-flexible-closed-surface'
READMES=('README.md',TOPIC+'/README.md')
HANDOFF=TOPIC+'/HANDOFF.md'
TOPIC_LOG=TOPIC+'/log.md'
ROOT_LOG='LOG.md'
CI_BEGIN='<!-- fd2d-ci-recovery-status:begin -->'
CI_END='<!-- fd2d-ci-recovery-status:end -->'
ONE_MB=1000000
FIVE_MB=5000000


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')


def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def atomic_json(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=Path(str(path)+'.tmp')
    temp.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    os.replace(temp,path)


def safe_relative(value):
    path=PurePosixPath(str(value))
    if path.is_absolute() or not path.parts or any(x in ('','..','.') for x in path.parts):
        raise ValueError('Unsafe repository-relative path')
    if '.git' in path.parts:
        raise ValueError('Git internal paths are not research artifacts')
    return str(path)


def repository():
    result=subprocess.run(['git','rev-parse','--show-toplevel'],check=True,
                          stdout=subprocess.PIPE,text=True)
    return Path(result.stdout.strip()).resolve()


def redact(text):
    text=re.sub(r'(https?://)[^/@\s]+:[^/@\s]+@',r'\1[redacted]@',text)
    return re.sub(r'\b(?:github_pat_|ghp_)[A-Za-z0-9_]+','[redacted-token]',text)


def git(repo,args,timeout=180):
    start=time.monotonic();began=utc()
    try:
        result=subprocess.run(['git']+list(args),cwd=repo,stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,text=True,errors='replace',timeout=timeout,check=False)
        code=result.returncode;output=result.stdout;timed_out=False
    except subprocess.TimeoutExpired as e:
        code=124;output=e.stdout or ''
        if isinstance(output,bytes):output=output.decode('utf-8','replace')
        timed_out=True
    return dict(argv=['git']+list(args),returncode=code,started_utc=began,
        finished_utc=utc(),seconds=time.monotonic()-start,output=redact(output),
        timed_out=timed_out)


def checked_git(repo,args,timeout=180):
    result=git(repo,args,timeout)
    if result['returncode']!=0:
        raise RuntimeError('git command failed: '+json.dumps(result))
    return result['output'].strip()


def run_identity():
    rid=os.environ.get('GITHUB_RUN_ID','')
    attempt=os.environ.get('GITHUB_RUN_ATTEMPT','')
    if not re.fullmatch(r'[0-9]+',rid) or not re.fullmatch(r'[0-9]+',attempt):
        raise ValueError('Real GITHUB_RUN_ID and GITHUB_RUN_ATTEMPT are required')
    return rid,attempt


def request_context(repo,request_path):
    path=Path(request_path)
    if not path.is_absolute():path=repo/path
    request=json.loads(path.read_text(encoding='utf-8'))
    if not re.fullmatch(r'[0-9a-fA-F]{40}',str(request.get('rules_read_sha',''))):
        raise ValueError('rules_read_sha must identify the actually read full commit')
    name=str(request.get('run_prefix',''))
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,95}',name):
        raise ValueError('run_prefix must be a plain bounded filename stem')
    commands=request.get('commands')
    if not isinstance(commands,list):
        raise ValueError('commands must be a list of name/argv records')
    for row in commands:
        if not isinstance(row,dict) or not isinstance(row.get('name'),str):
            raise ValueError('Every command needs a name')
        argv=row.get('argv')
        if not isinstance(argv,list) or not argv or not all(isinstance(a,str) for a in argv):
            raise ValueError('Every command needs a nonempty string argv list')
    # The user's PAT is not an allowed request-file value.
    if re.search(r'\b(?:github_pat_|ghp_)[A-Za-z0-9_]+',json.dumps(request)):
        raise ValueError('Credential-like values are not stored in CI requests')
    rid,attempt=run_identity()
    relative='notes/'+name+'-'+rid+'-a'+attempt
    return request,relative,rid,attempt


def pointer_path(repo,rid,attempt):
    return repo/TOPIC/'notes'/('fd2d-ci-runtime-'+rid+'-a'+attempt+'.json')


def pull_and_check(repo,request,relative,sequence):
    """The README diff is the very next git operation after every pull."""
    pulled=git(repo,['pull','--rebase','origin','main'])
    diff=git(repo,['diff',request['rules_read_sha'],'origin/main','--',*READMES])
    # No merge resolution, calculation or publication occurs before diff.
    origin=git(repo,['rev-parse','origin/main'])
    read_sha=origin['output'].strip() if origin['returncode']==0 else None
    changed=diff['returncode']!=0 or bool(diff['output'])
    check=dict(sequence=sequence,pull=pulled,readme_diff=diff,
        rules_base_sha=request['rules_read_sha'],read_sha=read_sha,checked_utc=utc(),
        rules_changed_or_unreadable=changed)
    cp=repo/TOPIC/(relative+'-pull-'+str(sequence).zfill(2)+'.json')
    atomic_json(cp,check)
    if changed:
        note=repo/TOPIC/(relative+'-rules-diff-'+str(sequence).zfill(2)+'.md')
        content='# CI README difference: automatic work stopped\n\n'
        content+='Baseline '+request['rules_read_sha']+'; origin '+str(read_sha)+'.\n'
        content+='Root must read and apply these new instructions before a new request.\n\n~~~diff\n'
        content+=diff['output']+'\n~~~\n'
        note.write_text(content,encoding='utf-8')
        print('README_CHANGED_OR_UNREADABLE\n'+diff['output'],flush=True)
        check['difference_note']=str(note.relative_to(repo))
    print(json.dumps(dict(event='pull_and_readme_check',sequence=sequence,
        pull_returncode=pulled['returncode'],read_sha=read_sha,
        rules_changed_or_unreadable=changed)),flush=True)
    return check


def ci_block(read_sha,checked_utc,rid,attempt,code,report_relative):
    block=(CI_BEGIN+'\n### CI recovery status\n'+checked_utc+' | run '+rid+
        '/a'+attempt+' | process exit '+str(code)+'\nRead README commit: '+
        str(read_sha)+'\nReport: '+report_relative+'\n'+CI_END)
    if len(block.encode('utf-8'))>600:
        block=(CI_BEGIN+'\nCI '+rid+'/a'+attempt+' exit '+str(code)+'; '+
            checked_utc+'; README '+str(read_sha)+'.\n'+CI_END)
    if len(block.encode('utf-8'))>600:raise ValueError('CI H block exceeds 600 bytes')
    return block


def replace_ci_block(text,block):
    if (CI_BEGIN in text)!=(CI_END in text):
        raise ValueError('Malformed existing owned CI block; no surrounding H is rewritten')
    pattern=re.compile(re.escape(CI_BEGIN)+r'.*?'+re.escape(CI_END),re.S)
    found=list(pattern.finditer(text))
    if len(found)>1:raise ValueError('Ambiguous duplicate owned CI blocks')
    if found:
        value=pattern.sub(lambda unused:block,text,count=1)
    else:
        value=text+('' if text.endswith('\n') else '\n')+'\n'+block+'\n'
    if len(value.encode('utf-8'))>=10000:
        raise ValueError('H would exceed 10 KB; no human H text is trimmed automatically')
    return value


def strip_ci_block(text):
    pattern=re.compile(re.escape(CI_BEGIN)+r'.*?'+re.escape(CI_END),re.S)
    found=list(pattern.finditer(text))
    if not found:return text.rstrip('\n')
    if len(found)!=1:raise ValueError('Ambiguous owned CI block')
    return (text[:found[0].start()]+text[found[0].end():]).rstrip('\n')


def update_handoff(repo,block):
    path=repo/HANDOFF
    text=path.read_text(encoding='utf-8')
    path.write_text(replace_ci_block(text,block),encoding='utf-8')


def inventory(directory):
    out={}
    if not directory.exists():return out
    for path in directory.rglob('*'):
        if path.is_file() and not path.is_symlink():
            s=path.stat()
            out[str(path.relative_to(directory))]=(s.st_size,s.st_mtime_ns)
    return out


def source_inputs(repo,argv):
    result={}
    for arg in argv:
        if arg.startswith('-'):continue
        path=Path(arg)
        if not path.is_absolute():path=repo/TOPIC/path
        try:
            path=path.resolve()
            path.relative_to(repo)
            if path.is_file():
                result[str(path.relative_to(repo))]=dict(bytes=path.stat().st_size,sha256=digest(path))
        except (ValueError,OSError):
            # Literal -c programs and other non-file arguments can exceed
            # the filesystem filename length; they are still valid argv.
            continue
    return result


def process_code(raw):
    if raw is None:return 124
    return raw if raw>=0 else 128-raw


def choose_latest_accepted(paths):
    """Retain each last actual accepted/iteration file type, plus progress."""
    pattern=re.compile(r'(?i)(.*?(?:accepted|iteration|iter)[-_]?)([0-9]+)(.*)$')
    groups={};ordinary=[]
    for path in paths:
        if 'progress' in Path(path).name.lower():
            ordinary.append(path);continue
        match=pattern.fullmatch(path)
        if not match:
            ordinary.append(path);continue
        key=(match.group(1),match.group(3))
        old=groups.get(key)
        number=int(match.group(2))
        if old is None or number>old[0]:groups[key]=(number,path)
    keep=sorted(set(ordinary+[row[1] for row in groups.values()]))
    return keep,sorted(set(paths)-set(keep))


def file_record(repo,relative):
    path=repo/safe_relative(relative)
    return dict(path=relative,bytes=path.stat().st_size,sha256=digest(path))


def pack_file(repo,relative):
    """Keep raw local data; publish gzip or verified independently gzipped parts."""
    path=repo/safe_relative(relative);size=path.stat().st_size
    must_compress=(size>ONE_MB and path.suffix!='.gz') or (path.suffix=='.md' and size>=100000)
    source_sha=digest(path)
    if not must_compress and size<FIVE_MB:
        return [file_record(repo,relative)],None
    destination=path if path.suffix=='.gz' and not must_compress else Path(str(path)+'.gz')
    if destination!=path:
        with path.open('rb') as src,destination.open('wb') as dst:
            with gzip.GzipFile(filename='',mode='wb',fileobj=dst,mtime=0) as out:
                for block in iter(lambda:src.read(1024*1024),b''):out.write(block)
    if destination.stat().st_size<FIVE_MB:
        rel=str(destination.relative_to(repo))
        return [file_record(repo,rel)],dict(original_path=relative,
            original_bytes=size,original_sha256=source_sha,published_paths=[rel],
            reconstruction='gzip-decompress if a .gz suffix was added; raw local original retained')
    # Large data are not forced into git. Preserve the local file, its hash
    # and generating request/source identities for explicit regeneration.
    return [],dict(original_path=relative,original_bytes=size,
        original_sha256=source_sha,gzip_path=str(destination.relative_to(repo)),
        gzip_bytes=destination.stat().st_size,gzip_sha256=digest(destination),
        not_published_reason='compressed single file is at least 5 MB',
        raw_local_original_retained=True)


def finish_batch(repo,request,relative,rid,attempt,before_notes,before_scripts,
                 checks,receipts,code,error=None):
    notes=repo/TOPIC/'notes';scripts=repo/TOPIC/'scripts'
    after_notes=inventory(notes);after_scripts=inventory(scripts)
    changed=[TOPIC+'/notes/'+p for p,stat in after_notes.items() if before_notes.get(p)!=stat]
    changed += [TOPIC+'/scripts/'+p for p,stat in after_scripts.items() if before_scripts.get(p)!=stat]
    # Explicit run metadata may predate the after-pull baseline inventory.
    for path in notes.glob(Path(relative).name+'*'):
        if path.is_file() and not path.name.endswith('.tmp'):
            changed.append(str(path.relative_to(repo)))
    pp=pointer_path(repo,rid,attempt)
    if pp.exists():changed.append(str(pp.relative_to(repo)))
    selected,excluded=choose_latest_accepted(sorted(set(changed)))
    temporary=[p for p in selected if p.endswith(('.tmp','.lock'))]
    excluded=sorted(set(excluded+temporary))
    selected=[p for p in selected if p not in temporary and not p.endswith('-publish-manifest.json')]
    records=[];transport=[]
    for path in selected:
        if not (repo/path).is_file():continue
        packed,mapping=pack_file(repo,path)
        records.extend(packed)
        if mapping is not None:transport.append(mapping)
    inventory_path=repo/TOPIC/(relative+'-output-inventory.json')
    atomic_json(inventory_path,dict(new_or_modified_note_paths=[p for p in changed if '/notes/' in p],
        new_or_modified_source_paths=[p for p in changed if '/scripts/' in p],
        excluded_regenerable_intermediates=[file_record(repo,p) for p in excluded if (repo/p).is_file()],
        transport=transport,raw_local_originals_not_deleted=True))
    ipacked,imapping=pack_file(repo,str(inventory_path.relative_to(repo)))
    records.extend(ipacked)
    if imapping:transport.append(imapping)
    report=repo/TOPIC/(relative+'-batch-report.json')
    last=checks[-1] if checks else {}
    stopped=any(c.get('rules_changed_or_unreadable') for c in checks)
    atomic_json(report,dict(kind='actual CI research batch receipt',body_completed=True,
        run_id=rid,attempt=attempt,run_prefix=relative,request=request,
        process_exit_code=code,error=error,commands=receipts,
        rules_checks=checks,rules_changed_or_unreadable=stopped,
        automatic_publication_stopped=stopped,
        read_rules_sha=last.get('read_sha'),read_rules_utc=last.get('checked_utc'),
        output_inventory=str(inventory_path.relative_to(repo)),
        selected_artifact_count=len(records),excluded_intermediate_count=len(excluded),
        computation_success_is_not_a_mathematical_completion_claim=True))
    records.append(file_record(repo,str(report.relative_to(repo))))
    unique={r['path']:r for r in records}
    manifest=repo/TOPIC/(relative+'-publish-manifest.json')
    atomic_json(manifest,dict(kind='explicit CI publication path list',
        run_id=rid,attempt=attempt,run_prefix=relative,
        request_snapshot=TOPIC+'/'+relative+'-request.json',
        batch_report=str(report.relative_to(repo)),
        paths=sorted(unique),files=[unique[k] for k in sorted(unique)],
        transport=transport,process_exit_code=code,
        automatic_publication_stopped=stopped,
        read_rules_sha=last.get('read_sha'),read_rules_utc=last.get('checked_utc')))
    # The manifest lists itself by path; no self-referential hash.
    data=json.loads(manifest.read_text(encoding='utf-8'))
    data['paths'].append(str(manifest.relative_to(repo)))
    atomic_json(manifest,data)
    print(json.dumps(dict(event='batch_closed',process_exit_code=code,
        report=str(report.relative_to(repo)),manifest=str(manifest.relative_to(repo)),
        automatic_publication_stopped=stopped)),flush=True)
    return report,manifest


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--request',required=True)
    args=parser.parse_args()
    repo=repository()
    request,relative,rid,attempt=request_context(repo,args.request)
    before_notes=inventory(repo/TOPIC/'notes')
    before_scripts=inventory(repo/TOPIC/'scripts')
    checks=[];receipts=[];code=0;error=None
    try:
        check=pull_and_check(repo,request,relative,0);checks.append(check)
        # Pulled research files belong to origin, not to this batch.
        before_notes=inventory(repo/TOPIC/'notes')
        before_scripts=inventory(repo/TOPIC/'scripts')
        atomic_json(repo/TOPIC/(relative+'-request.json'),request)
        atomic_json(pointer_path(repo,rid,attempt),dict(
            request_snapshot=TOPIC+'/'+relative+'-request.json',
            source_request_path=str(Path(args.request)),
            run_prefix=relative,manifest=TOPIC+'/'+relative+'-publish-manifest.json'))
        if check['rules_changed_or_unreadable']:
            code=78
        elif check['pull']['returncode']!=0:
            code=process_code(check['pull']['returncode'])
            error='Initial ordinary pull failed; no computation was started'
        else:
            update_handoff(repo,ci_block(check['read_sha'],check['checked_utc'],rid,attempt,
                'pending',relative+'-batch-report.json'))
            deadline=time.monotonic()+1800
            for index,command in enumerate(request['commands'],1):
                remaining=deadline-time.monotonic()
                if remaining<=0:
                    code=124;error='Thirty-minute compute budget exhausted before next command';break
                argv=[a.replace('{prefix}',relative) for a in command['argv']]
                name=re.sub(r'[^A-Za-z0-9_.-]+','-',command['name'])[:48] or 'command'
                console=repo/TOPIC/(relative+'-c'+str(index).zfill(2)+'-'+name+'.console.log')
                receipt_path=repo/TOPIC/(relative+'-c'+str(index).zfill(2)+'-'+name+'-receipt.json')
                commit=checked_git(repo,['rev-parse','HEAD'])
                inputs=source_inputs(repo,argv)
                began=utc();start=time.monotonic();raw_code=None;timed_out=False;spawn_error=None
                print(json.dumps(dict(event='command_started',index=index,name=command['name'],
                    argv=argv,source_commit=commit,utc=began)),flush=True)
                with console.open('wb') as output:
                    try:
                        result=subprocess.run(argv,cwd=repo/TOPIC,stdout=output,
                            stderr=subprocess.STDOUT,timeout=remaining,check=False)
                        raw_code=result.returncode
                    except subprocess.TimeoutExpired:
                        timed_out=True
                    except OSError as e:
                        spawn_error=redact(type(e).__name__+': '+str(e))
                        output.write((spawn_error+'\n').encode('utf-8'))
                code=127 if spawn_error is not None else process_code(raw_code)
                receipt=dict(index=index,name=command['name'],argv=argv,
                    working_directory=TOPIC,started_utc=began,finished_utc=utc(),
                    seconds=time.monotonic()-start,subprocess_returncode=raw_code,
                    runner_exit_code=code,timed_out=timed_out,spawn_error=spawn_error,
                    source_git_sha=commit,input_files=inputs,
                    console=file_record(repo,str(console.relative_to(repo))),
                    negative_subprocess_codes_use_shell_128_plus_signal_mapping=True)
                atomic_json(receipt_path,receipt)
                receipts.append(dict(path=str(receipt_path.relative_to(repo)),**receipt))
                print(json.dumps(dict(event='command_finished',index=index,
                    subprocess_returncode=raw_code,runner_exit_code=code,
                    seconds=receipt['seconds'],console=str(console.relative_to(repo)))),flush=True)
                if code!=0:break
            update_handoff(repo,ci_block(check['read_sha'],check['checked_utc'],rid,attempt,
                code,relative+'-batch-report.json'))
    except Exception as e:
        error=redact(type(e).__name__+': '+str(e))
        if code==0:code=1
        print('CI_RUN_EXCEPTION '+error,flush=True)
    try:
        finish_batch(repo,request,relative,rid,attempt,before_notes,before_scripts,
                     checks,receipts,code,error)
    except Exception as e:
        if code==0:code=1
        emergency=repo/TOPIC/(relative+'-emergency-report.json')
        atomic_json(emergency,dict(error=redact(str(e)),process_exit_code=code,
            commands=receipts,rules_checks=checks,
            publication_manifest_incomplete=True,finished_utc=utc()))
        print('CI_OUTPUT_COLLECTION_EXCEPTION '+redact(str(e)),flush=True)
    return code


if __name__=='__main__':
    sys.exit(main())
