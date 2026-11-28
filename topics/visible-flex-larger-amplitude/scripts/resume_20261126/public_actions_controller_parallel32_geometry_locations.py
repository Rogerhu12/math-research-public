#!/usr/bin/env python3
"""Run the declared research recipe in public Actions with its own HANDOFF slot.

Scientific arrays and complete logs stay in RUNNER_TEMP.  The executable source
tree is a detached partial worktree, so publication pulls cannot change a live
scientific module.  No token is written to a file or to a command argument.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time

TOPIC='topics/visible-flex-larger-amplitude'
RULES=['README.md',TOPIC+'/README.md']
HISTORICAL='60321451c058c6a51da58c37ae5ec6f2d1145f74'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def event(kind,**kwargs):
    print(json.dumps(dict(event=kind,**kwargs),ensure_ascii=False),flush=True)


class Publisher:
    def __init__(self,repo,source_commit,request,request_path):
        self.repo=repo
        self.source_commit=source_commit
        self.controller_sha=digest(__file__)
        self.request=request
        self.request_sha=digest(request_path)
        self.rule_commit=request['rules_read_commit']
        self.run_id=os.environ['GITHUB_RUN_ID']
        self.attempt=os.environ.get('GITHUB_RUN_ATTEMPT','1')
        self.run_url=f'https://github.com/Rogerhu12/math-research-public/actions/runs/{self.run_id}'
        self.note=f'{TOPIC}/notes/2026-11-28-public-actions-{self.run_id}-{self.attempt}.md'
        self.last_pull=0.
        self.last_snapshot=None

    def git(self,*args,capture=True,check=True):
        return subprocess.run(['git',*args],cwd=self.repo,check=check,
            text=True,stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None)

    def sync(self):
        if self.git('cat-file','-e',self.rule_commit+'^{commit}',check=False).returncode:
            self.git('fetch','--filter=blob:none','--depth=1','origin',self.rule_commit,capture=False)
        p=self.git('pull','--rebase','origin','main',capture=False)
        head=self.git('rev-parse','origin/main').stdout.strip()
        difference=self.git('diff',self.rule_commit,head,'--',*RULES).stdout
        if difference:
            print(difference,flush=True)
            raise RuntimeError('README changed: the research agent must read this exact diff before further computation/publication')
        self.rule_commit=head
        self.last_pull=time.monotonic()
        event('rules_unchanged_after_real_pull',read_commit=head,time=utc())

    def render(self,status,exit_code):
        def public_cleanup_metadata(value):
            # Only the rendered copy is compacted. Full original cleanup entries
            # remain in runner status.json and followup-journal.json.
            result=dict(value)
            for key in ('deleted','skipped'):
                entries=value.get(key,[])
                canonical=json.dumps(entries,ensure_ascii=False,sort_keys=True,
                    separators=(',',':'),allow_nan=False).encode('utf-8')
                result[key]=dict(
                    record_count=len(entries),
                    recorded_bytes=sum(item['bytes'] for item in entries if 'bytes' in item),
                    records_with_bytes=sum('bytes' in item for item in entries),
                    listed_file_count=sum(len(item['files']) for item in entries if 'files' in item),
                    records_with_file_lists=sum('files' in item for item in entries),
                    canonical_metadata_bytes=len(canonical),
                    canonical_metadata_sha256=hashlib.sha256(canonical).hexdigest(),
                    canonicalization="UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
                    detail_scope='Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists')
            return result

        # Every complete compact record is preserved in a bounded volume.
        # This changes publication only, never a scientific command or value.
        lines=[f'# 公开Actions实际运行 {self.run_id}/{self.attempt}', '',
            f'状态记录时间：{utc()}。本记录由分卷控制器在真实公开Actions生成。', '',
            f'- 运行：[GitHub Actions {self.run_id}]({self.run_url})。',
            f'- 请求：`{self.request["request_id"]}`；请求文件SHA256 `{self.request_sha}`。',
            f'- 初始执行源码提交：`{self.source_commit}`；控制器实际加载SHA256 `{self.controller_sha}`。',
            f'- 当前阶段：`{status.get("stage","not_reported")}`；阶段状态：`{status.get("state","not_reported")}`。',
            f'- 实际子进程退出码：`{exit_code if exit_code is not None else "尚未退出"}`。', '',
            '每项实际输入、完整命令、源码与输出SHA及紧凑数值完整保存在下列分卷。所有科学数组、逐点/逐胞报告和完整日志只留runner；输入重建不重复宣告旧科学结论。', '',
            '## 已实际返回的阶段与分卷', '']
        completed=status.get('completed',[])
        fields=('name','stage','state','returncode','seconds','scope','input_sha256',
                'bundle_sha256','report_sha256','metrics','outputs','output_files',
                'input_files','historical_output_sha256','same_as_historical',
                'output_bundle','output_report','parent_sha256','output_bundle_sha256',
                'historical_bundle_sha256','historical_bytes_match','Phi','max_gram',
                'weighted_sse','raw_sse','product','final_known_point_safety_pass',
                'final_damping','status','source_commit','source_sha256','command',
                'cleanup_generated','step_id','summary_errors','missing_outputs','setup_error')
        records=[]
        for number,record in enumerate(completed,1):
            compact={key:record[key] for key in fields if key in record}
            if 'cleanup_generated' in compact:
                compact['cleanup_generated']=public_cleanup_metadata(compact['cleanup_generated'])
            if 'command' in compact and 'input_files' in compact:
                compact['input_files']=[{key:value for key,value in item.items() if key!='command'} for item in compact['input_files']]
            body='\n'.join([f'## {number}. {record.get("name",record.get("stage","returned stage"))}', '',
                '```json',json.dumps(compact,ensure_ascii=False,indent=2),'```',''])
            if len(body.encode())>=58000:
                raise RuntimeError('One compact record exceeds its declared metadata bound; raw arrays do not belong in summaries')
            records.append((number,record,body))
        groups=[];current=[];size=0
        for entry in records:
            length=len(entry[2].encode())
            if current and size+length>58000:
                groups.append(current);current=[];size=0
            current.append(entry);size+=length
        if current:groups.append(current)
        self.rendered_volumes={}
        for number,group in enumerate(groups,1):
            relative=self.note[:-3]+f'-part-{number:03d}.md'
            title=f'# 公开Actions {self.run_id}/{self.attempt}：实际阶段 {group[0][0]}–{group[-1][0]}'
            header='\n'.join([title,'',f'[运行]({self.run_url})；[总索引]({Path(self.note).name})。', '',
                '本卷完整保留这些实际阶段的紧凑输入/源码/参数/输出身份，不存科学数组或逐点报告。',''])
            body=header+'\n'+''.join(item[2]+'\n' for item in group)
            if len(body.encode())>=60000:
                raise RuntimeError('A compact volume exceeded its explicit byte bound')
            self.rendered_volumes[relative]=body
            lines.append(f'- [第{number}卷：阶段{group[0][0]}–{group[-1][0]}]({Path(relative).name})。')
        if not completed:lines.append('尚无已返回的科学阶段。')
        else:
            lines += ['', '| 阶段 | 实际状态 | 退出码 |', '|---|---|---|']
            for number,record,body in records:
                name=str(record.get('name',record.get('stage','returned stage'))).replace('|','/')
                lines.append(f'| {number}. {name} | {record.get("state",record.get("status","returned"))} | {record.get("returncode","未返")} |')
        progress=status.get('active_progress_observation')
        if progress is not None:
            rendered=json.dumps(progress,ensure_ascii=False,indent=2,allow_nan=False)
            if len(rendered.encode('utf-8'))>=32768:
                raise RuntimeError('Optional complete progress metadata exceeded its bound')
            lines += ['', '## 进行中的实际只读进度', '',
                '以下只是尚未自然返回的同一子进程的有界标量记录；不计作已返回步骤或完整科学证书。', '',
                '```json',rendered,'```']
        failure=status.get('failed')
        if failure:
            lines += ['', '## 实际失败或未完整返回', '',
                '已在阶段卷记录的失败不重复复制；未付范围仍保持，不冒称成功。']
            if not any(record.get('name')==failure.get('name') and record.get('source_sha256')==failure.get('source_sha256') for record in completed):
                compact={key:failure[key] for key in fields if key in failure}
                if 'cleanup_generated' in compact:
                    compact['cleanup_generated']=public_cleanup_metadata(compact['cleanup_generated'])
                lines += ['','```json',json.dumps(compact,ensure_ascii=False,indent=2),'```']
        if status.get('error'):
            lines += ['', '实际编排错误：`'+str(status['error']).replace('`','\\`')+'`。']
        lines += ['', '## 完整可复现请求', '', '```json',json.dumps(self.request,ensure_ascii=False,indent=2),'```','',
            '科学完成标准仍是本题README的全域度量、全t几何和固定参数实际精化；单步或本job退出不构成研究完成。','']
        result='\n'.join(lines)
        if len(result.encode())>=95000:
            raise RuntimeError('The compact volume index exceeded its Markdown bound')
        return result

    def parallel_handoff_text(self,status,exit_code):
        """Render this run's complete slot without mutating the Git checkout."""
        handoff=self.repo/TOPIC/'HANDOFF.md'
        text=handoff.read_text()
        begin='<!-- visible-larger-parallel-32:start -->'
        end='<!-- visible-larger-parallel-32:end -->'
        if (begin in text)!=(end in text) or text.count(begin)>1 or text.count(end)>1:
            raise RuntimeError('Malformed independent parallel run HANDOFF slot')
        section='\n'.join([begin,
            f'Actions32：[run {self.run_id}/{self.attempt}]({self.run_url})；[全阶段记录](notes/{Path(self.note).name})。{status.get("state","not_reported")}；已返{len(status.get("completed",[]))}，exit={exit_code if exit_code is not None else "未返"}。',
            f'并行32规则核查：{utc()}，真实pull至`{self.rule_commit}`，双README无变化。',end])
        if begin in text:
            a=text.index(begin);b=text.index(end,a)+len(end)
            text=text[:a]+section+text[b:]
        else:
            marker='\n## 当前公开Actions执行\n'
            at=text.index(marker) if marker in text else len(text)
            text=text[:at].rstrip()+'\n\n'+section+'\n'+text[at:]
        return text

    def write_parallel_handoff(self,status,exit_code):
        text=self.parallel_handoff_text(status,exit_code)
        if len(text.encode())>=10000:
            raise RuntimeError('HANDOFF must be condensed before independent run publication')
        (self.repo/TOPIC/'HANDOFF.md').write_text(text)

    def prepare_complete_publication(self,status,exit_code):
        """Wait for a whole lawful publication; keep the original child/state.
        This waits only on repository/HANDOFF capacity. It does not shrink a
        volume, discard a completed step, alter a science budget or signal a
        scientific child. The runner's original complete status/journal/raw
        outputs remain in their original work directories.
        """
        while True:
            self.sync()
            note_text=self.render(status,exit_code)
            handoff_text=self.parallel_handoff_text(status,exit_code)
            pending={self.note:note_text,**self.rendered_volumes,
                     TOPIC+'/HANDOFF.md':handoff_text}
            current=sum(path.stat().st_size for path in (self.repo/TOPIC).rglob('*')
                        if path.is_file())
            projected=current
            for relative,body in pending.items():
                target=self.repo/relative
                projected+=len(body.encode())-(target.stat().st_size if target.exists() else 0)
            handoff_bytes=len(handoff_text.encode())
            if projected<=200000000 and handoff_bytes<10000:
                return pending
            event('complete_publication_waiting_for_capacity',
                  run_id=self.run_id,actual_source_rule_commit=self.rule_commit,
                  returned_stages=len(status.get('completed',[])),
                  current_topic_bytes=current,projected_topic_bytes=projected,
                  projected_handoff_bytes=handoff_bytes,
                  limits={'topic_bytes':200000000,'handoff_bytes_exclusive':10000},
                  complete_pending_files=[{'path':relative,'bytes':len(body.encode()),
                      'sha256':hashlib.sha256(body.encode()).hexdigest()}
                      for relative,body in pending.items()],
                  scientific_child_signalled=False,complete_records_discarded=False,
                  next_real_pull_seconds=30)
            time.sleep(30)

    def publish(self,status,exit_code=None,force=False):
        snapshot=json.dumps({'completed':status.get('completed',[]),
            'state':status.get('state'),'exit_code':exit_code},sort_keys=True)
        if snapshot==self.last_snapshot and not force:
            return
        pending=self.prepare_complete_publication(status,exit_code)
        for relative,body in pending.items():
            (self.repo/relative).write_text(body)
        self.git('diff','--check',capture=False)
        self.git('add',*pending,capture=False)
        if self.git('diff','--cached','--quiet',check=False).returncode==0:
            self.last_snapshot=snapshot
            return
        count=len(status.get('completed',[]))
        self.git('commit','-m',f'Record public Actions {self.run_id} actual stage {count}',capture=False)
        helper='!f() { if test "$1" = get; then printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; fi; }; f'
        while True:
            pushed=self.git('-c','credential.helper=','-c','credential.helper='+helper,
                            'push','origin','main',check=False)
            print(pushed.stdout+pushed.stderr,flush=True)
            if pushed.returncode==0:
                break
            if not any(word in pushed.stderr for word in ('fetch first','non-fast-forward','cannot lock ref')):
                raise RuntimeError('Terminal push failed without a non-fast-forward reason')
            # An ordinary rebase can increase the current tree. Recompute the
            # entire proposed note, all volumes and own slot before retrying.
            pending=self.prepare_complete_publication(status,exit_code)
            for relative,body in pending.items():
                (self.repo/relative).write_text(body)
            self.git('add',*pending,capture=False)
            self.git('commit','--amend','--no-edit',capture=False)
        self.last_snapshot=snapshot
        event('compact_conclusion_published',run_id=self.run_id,returned_stages=count,
              commit=self.git('rev-parse','HEAD').stdout.strip())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--request',type=Path,required=True)
    args=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('Scientific execution is restricted to the authorized public Actions repository')
    began=time.monotonic()
    repo=args.repo.resolve();work=args.work.resolve();work.mkdir(parents=True,exist_ok=True)
    request=json.loads(args.request.read_text())
    if work==repo or repo in work.parents:
        raise ValueError('All reproducible computation outputs must stay outside the Git checkout')
    source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
    subprocess.run(['git','switch','-C','main',source_commit],cwd=repo,check=True)
    for key,value in [('gc.auto','0'),('gc.autoPackLimit','0'),('maintenance.auto','false'),
                      ('user.name','visible-larger research Actions'),('user.email','actions@users.noreply.github.com')]:
        subprocess.run(['git','config',key,value],cwd=repo,check=True)
    publisher=Publisher(repo,source_commit,request,args.request)
    publisher.sync()
    source=work/'source'
    subprocess.run(['git','worktree','add','--no-checkout','--detach',str(source),source_commit],cwd=repo,check=True)
    subprocess.run(['git','sparse-checkout','set','--cone',TOPIC],cwd=source,check=True)
    subprocess.run(['git','reset','--hard',source_commit],cwd=source,check=True)
    subprocess.run(['git','fetch','--filter=blob:none','--depth=1','origin',HISTORICAL],cwd=repo,check=True)
    followups=None
    if request.get('followup_file'):
        followup_path=source/TOPIC/'scripts/resume_20261126/public_actions_followups_with_geometry_location_progress.py'
        spec=importlib.util.spec_from_file_location('pinned_public_actions_followups',followup_path)
        followups=importlib.util.module_from_spec(spec);sys.modules[spec.name]=followups
        spec.loader.exec_module(followups)
    for name,expected in request['rules_sha256'].items():
        if name not in RULES or digest(source/name)!=expected:
            raise RuntimeError('The pinned source rule bytes differ from the request actually read by the research agent')
    if request.get('bootstrap_mode')=='followups_only':
        if followups is None:
            raise ValueError('A direct full-input execution requires its complete followup queue')
        runwork=work/'research';runwork.mkdir()
        status=dict(stage='complete_fixed_input_pending',state='running',completed=[])
        publisher.publish(status)
        followups.run_followups(repo,work,runwork,publisher,status,request,began)
        return
    recipe=source/request['recipe']
    if source not in recipe.resolve().parents:
        raise ValueError('Recipe must be in the pinned source repository')
    runwork=work/'research';runwork.mkdir()
    command=[sys.executable,'-u',str(recipe),'--repo',str(source),'--work',str(runwork),
             '--stop-after',request['stop_after']]
    environment={key:value for key,value in os.environ.items()
                 if key not in ('GITHUB_TOKEN','GH_TOKEN','TASK_GITHUB_TOKEN')}
    environment.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
                       NUMEXPR_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1',PYTHONUNBUFFERED='1')
    status=dict(stage='recipe_start',state='running',completed=[])
    publisher.publish(status)
    log=work/'complete-research.log'
    with log.open('w') as output:
        child=subprocess.Popen(command,cwd=source,env=environment,stdout=output,
                               stderr=subprocess.STDOUT,start_new_session=True)
        try:
            while True:
                path=runwork/'status.json'
                if path.exists():
                    try:
                        status=json.loads(path.read_text())
                    except json.JSONDecodeError:
                        pass
                code=child.poll()
                publisher.publish(status,code)
                if code is not None:
                    break
                if time.monotonic()-publisher.last_pull>=3000:
                    publisher.publish(status,force=True)
                time.sleep(10)
        except BaseException:
            if child.poll() is None:
                os.killpg(child.pid,signal.SIGINT)
                try:
                    child.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid,signal.SIGTERM);child.wait(timeout=30)
            raise
    event('public_scientific_recipe_returned',exit_code=code,log_sha256=digest(log),
          status_sha256=digest(runwork/'status.json') if (runwork/'status.json').exists() else None)
    if code:
        # Authentication variables were excluded from the scientific child.
        print(''.join(log.read_text(errors='replace').splitlines(keepends=True)[-70:]),flush=True)
        failed_log=status.get('failed',{}).get('log')
        if failed_log and Path(failed_log).is_file():
            content=Path(failed_log).read_text(errors='replace')
            event('failed_scientific_log_excerpt',path=failed_log,sha256=digest(failed_log),
                  complete=len(content.encode())<=64000)
            print(content if len(content.encode())<=64000 else content[-32000:],flush=True)
        raise SystemExit(code)
    if followups is not None:
        followups.run_followups(repo,work,runwork,publisher,status,request,began)


if __name__=='__main__':
    main()
