#!/usr/bin/env python3
"""Publish only this CI batch with ordinary commit/rebase/push.

Only this batch's own ROOT LOG append and owned HANDOFF CI block can be
resolved automatically during rebase. Other conflicts remain for root.
Every git pull is immediately followed by the two-README comparison.
This new source still needs an actual CI execution.
"""
from __future__ import annotations
import argparse,gzip,json,os,subprocess,sys
from pathlib import Path
import fd2d_ci_run_recovery as common


def append_once(text,entry,marker):
    if marker in text:return text
    return text+('' if text.endswith('\n') else '\n')+entry+'\n'


def log_entry(rid,attempt,code,relative,root=False):
    marker='[fd2d-ci:'+rid+':a'+attempt+']'
    text=common.utc()+' | '
    if root:text+='visible-flexible-closed-surface | '
    text+=marker+' process exit '+str(code)+'; report '+relative+'-batch-report.json; strong goal remains open.'
    if len(text)>200:
        text=common.utc()+' | visible-flexible-closed-surface '+marker+' process exit '+str(code)+\
             '; see topic HANDOFF and the actual CI batch receipt; strong goal remains open.'
    if len(text)>200:raise ValueError('CI log entry exceeds 200 characters')
    return text,marker


def rotate_root_log(repo,rid,attempt):
    """Apply root rule 7 without dropping a byte of the previous log."""
    path=repo/common.ROOT_LOG
    if not path.exists() or path.stat().st_size<=50000:return []
    stamp=common.datetime.datetime.now(common.datetime.timezone.utc).strftime('%Y%m%d-%H%M')
    name='log/LOG-archive-'+stamp+'-ci'+rid+'-a'+attempt+'.md'
    dest=repo/name
    if dest.exists():raise FileExistsError('A root log archive already exists; no overwrite')
    dest.parent.mkdir(parents=True,exist_ok=True)
    payload=path.read_bytes()
    if len(payload)>=100000:
        dest=Path(str(dest)+'.gz');name+='.gz'
        if dest.exists():raise FileExistsError('Existing gzip log archive is not overwritten')
        dest.write_bytes(gzip.compress(payload,compresslevel=9,mtime=0))
    else:
        dest.write_bytes(payload)
    restored=gzip.decompress(dest.read_bytes()) if dest.suffix=='.gz' else dest.read_bytes()
    if restored!=payload:raise ArithmeticError('Root log archive differs from source')
    if dest.stat().st_size>=common.FIVE_MB:
        raise ValueError('Root log archive exceeds the repository file limit')
    path.write_text('# 工作日志\n\n',encoding='utf-8')
    return [name]


def prepare_logs(repo,rid,attempt,code,relative):
    extra=rotate_root_log(repo,rid,attempt)
    root_entry,marker=log_entry(rid,attempt,code,relative,root=True)
    topic_entry,unused=log_entry(rid,attempt,code,relative,root=False)
    existing=[line for line in (repo/common.ROOT_LOG).read_text(encoding='utf-8').splitlines() if marker in line]
    if len(existing)>1:raise ValueError('Ambiguous repeated owned root LOG marker')
    if existing:
        # Preserve the exact original UTC/text across every push retry.
        root_entry=existing[0]
    for name,entry in ((common.ROOT_LOG,root_entry),(common.TOPIC_LOG,topic_entry)):
        path=repo/name
        old=path.read_text(encoding='utf-8')
        new=append_once(old,entry,marker)
        if len(new.encode('utf-8'))>=100000:
            raise ValueError(name+' would exceed 100 KB; no unrelated topic log is trimmed')
        path.write_text(new,encoding='utf-8')
    return extra,root_entry,marker


def stage_commit(repo,paths,message):
    existing=sorted(set(paths))
    for name in existing:
        path=repo/common.safe_relative(name)
        if not path.is_file() or path.is_symlink():
            raise ValueError('Missing or symlink publication path: '+name)
        if path.stat().st_size>=common.FIVE_MB:
            raise ValueError('Oversized publication path: '+name)
        if path.suffix=='.md' and path.stat().st_size>=100000:
            raise ValueError('Oversized Markdown: '+name)
    common.checked_git(repo,['add','--sparse','--',*existing])
    changed=common.git(repo,['diff','--cached','--quiet'])
    if changed['returncode']==0:return None
    if changed['returncode']!=1:raise RuntimeError(json.dumps(changed))
    result=common.git(repo,['commit','-m',message])
    if result['returncode']!=0:raise RuntimeError(json.dumps(result))
    return common.checked_git(repo,['rev-parse','HEAD'])


def conflict_paths(repo):
    result=common.git(repo,['diff','--name-only','--diff-filter=U'])
    if result['returncode']!=0:raise RuntimeError(json.dumps(result))
    return [name for name in result['output'].splitlines() if name]


def stage_text(repo,stage,path):
    result=common.git(repo,['show',':'+str(stage)+':'+path])
    if result['returncode']!=0:
        raise RuntimeError('Missing rebase stage for '+path)
    return result['output']


def resolve_owned_conflicts(repo,root_entry,marker,block,root_archived):
    """Stage 2 is current upstream, stage 3 is our rebased commit.

    Validate that stage 3 differs from the base only by the precise owned
    append/block, then apply that same small change to untouched stage 2.
    """
    for unused in range(50):
        conflicts=conflict_paths(repo)
        if not conflicts:return True,[]
        if any(p not in (common.ROOT_LOG,common.HANDOFF) for p in conflicts):
            return False,conflicts
        if root_archived and common.ROOT_LOG in conflicts:
            return False,conflicts
        for path in conflicts:
            base=stage_text(repo,1,path)
            upstream=stage_text(repo,2,path)
            replay=stage_text(repo,3,path)
            if path==common.ROOT_LOG:
                if replay!=append_once(base,root_entry,marker):
                    return False,conflicts
                merged=append_once(upstream,root_entry,marker)
            else:
                if common.strip_ci_block(replay)!=common.strip_ci_block(base):
                    return False,conflicts
                merged=common.replace_ci_block(upstream,block)
            (repo/path).write_text(merged,encoding='utf-8')
            common.checked_git(repo,['add','--',path])
        env=os.environ.copy();env['GIT_EDITOR']='true'
        result=subprocess.run(['git','rebase','--continue'],cwd=repo,env=env,
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,errors='replace',check=False)
        print(common.redact(result.stdout),flush=True)
        if result.returncode==0:return True,[]
        if not conflict_paths(repo):
            return False,['rebase --continue failed without a supported file conflict']
    return False,['rebase conflict continuation limit']


def load_batch(repo,request_path):
    rid,attempt=common.run_identity()
    pointer=common.pointer_path(repo,rid,attempt)
    if pointer.exists():
        data=json.loads(pointer.read_text(encoding='utf-8'))
        request=json.loads((repo/common.safe_relative(data['request_snapshot'])).read_text(encoding='utf-8'))
        relative=data['run_prefix']
        manifest_path=repo/common.safe_relative(data['manifest'])
    else:
        request,relative,rid,attempt=common.request_context(repo,request_path)
        manifest_path=repo/common.TOPIC/(relative+'-publish-manifest.json')
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest['run_id']!=rid or manifest['attempt']!=attempt:
        raise ValueError('Publication manifest belongs to a different CI run')
    return request,relative,rid,attempt,manifest,manifest_path


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--request',required=True)
    args=parser.parse_args()
    repo=common.repository()
    request,relative,rid,attempt,manifest,manifest_path=load_batch(repo,args.request)
    status_path=repo/common.TOPIC/(relative+'-publish-status.json')
    history=[]
    def status(phase,**extra):
        value=dict(phase=phase,run_id=rid,attempt=attempt,utc=common.utc(),history=history)
        value.update(extra)
        common.atomic_json(status_path,value)
        print(json.dumps(value,ensure_ascii=False),flush=True)
    if manifest.get('automatic_publication_stopped'):
        status('stopped_for_changed_or_unreadable_README',batch_manifest=str(manifest_path.relative_to(repo)))
        return 78
    paths=[]
    for name in manifest['paths']:
        name=common.safe_relative(name)
        if not any(name.startswith(common.TOPIC+'/'+folder+'/') for folder in ('notes','scripts','results')):
            raise ValueError('Manifest has a path outside this research batch: '+name)
        paths.append(name)
    for row in manifest.get('files',[]):
        if common.digest(repo/common.safe_relative(row['path']))!=row['sha256']:
            raise ValueError('A supposedly closed artifact changed: '+row['path'])
    code=manifest['process_exit_code']
    read_sha=manifest.get('read_rules_sha')
    read_time=manifest.get('read_rules_utc')
    block=common.ci_block(read_sha,read_time,rid,attempt,code,relative+'-batch-report.json')
    common.update_handoff(repo,block)
    extra,root_entry,marker=prepare_logs(repo,rid,attempt,code,relative)
    root_archived=bool(extra)
    paths+=extra+[common.HANDOFF,common.TOPIC_LOG,common.ROOT_LOG]
    commit=stage_commit(repo,paths,'visible flexible: CI recovery '+rid+' attempt '+attempt)
    status('local_batch_committed',commit=commit,process_exit_code=code)
    # Remaining unstaged tracked changes are never hidden by an auto-stash.
    dirty=common.git(repo,['diff','--name-only'])
    if dirty['returncode']!=0 or dirty['output'].strip():
        status('unmanifested_tracked_changes',paths=dirty['output'].splitlines())
        return 1
    for number in range(1,21):
        check=common.pull_and_check(repo,request,relative,number)
        history.append(dict(attempt=number,pull=check))
        if check['rules_changed_or_unreadable']:
            status('stopped_for_changed_or_unreadable_README',
                   difference_note=check.get('difference_note'))
            return 78
        block=common.ci_block(check['read_sha'],check['checked_utc'],rid,attempt,
                             code,relative+'-batch-report.json')
        if check['pull']['returncode']!=0:
            conflicts=conflict_paths(repo)
            if not conflicts:
                status('ordinary_pull_failed',returncode=check['pull']['returncode'])
                return 1
            ok,remaining=resolve_owned_conflicts(repo,root_entry,marker,block,root_archived)
            if not ok:
                status('unresolved_conflicts_left_for_root',paths=remaining)
                return 1
        common.update_handoff(repo,block)
        # Rule 7 can also become relevant after another author's latest log
        # is replayed. The full old root log is retained in a new archive.
        extra2,root_entry,marker=prepare_logs(repo,rid,attempt,code,relative)
        root_archived=root_archived or bool(extra2)
        sync=stage_commit(repo,[common.HANDOFF,common.TOPIC_LOG,common.ROOT_LOG,*extra2],
            'visible flexible: CI README sync '+rid+' attempt '+str(number))
        pushed=common.git(repo,['push','origin','HEAD:main'])
        history[-1].update(sync_commit=sync,push=pushed)
        if pushed['returncode']==0:
            status('published',published_head=common.checked_git(repo,['rev-parse','HEAD']),
                final_rules_read_sha=check['read_sha'],final_rules_read_utc=check['checked_utc'],
                process_exit_code=code)
            return 0
        output=pushed['output'].lower()
        ordinary_race=any(word in output for word in
            ('non-fast-forward','fetch first','[rejected]','failed to push some refs'))
        if not ordinary_race:
            status('push_failed_without_normal_ref_race',returncode=pushed['returncode'])
            return 1
        status('ordinary_push_race_retry',push_attempt=number)
    status('normal_push_race_limit_reached',attempts=20)
    return 1


if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as error:
        print('CI_PUBLISH_EXCEPTION '+common.redact(type(error).__name__+': '+str(error)),flush=True)
        sys.exit(1)
