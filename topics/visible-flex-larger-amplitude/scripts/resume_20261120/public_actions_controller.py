#!/usr/bin/env python3
"""Run the declared research recipe in public Actions and publish compact facts.

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
        self.note=f'{TOPIC}/notes/2026-11-20-public-actions-{self.run_id}-{self.attempt}.md'
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
        lines=[f'# 公开Actions实际运行 {self.run_id}/{self.attempt}', '',
            f'状态记录时间：{utc()}。本记录由已刊控制器在真实公开Actions运行中生成。', '',
            f'- 运行：[GitHub Actions {self.run_id}]({self.run_url})。',
            f'- 请求：`{self.request["request_id"]}`；请求文件SHA256 `{self.request_sha}`。',
            f'- 初始执行源码提交：`{self.source_commit}`；控制器实际加载SHA256 `{self.controller_sha}`；后继步骤各自另记固定源码提交。',
            f'- 当前阶段：`{status.get("stage","not_reported")}`；阶段状态：`{status.get("state","not_reported")}`。',
            f'- 实际子进程退出码：`{exit_code if exit_code is not None else "尚未退出"}`。', '',
            '这些是本次实际数组的输入材料化或新数值结果，不因与旧文件同名而继承旧SHA、旧几何证书或课题完成状态。所有科学数组、逐点/逐胞报告和完整日志只在临时计算目录；本仓库只保存完整源码、参数、运行编号、哈希及以下紧凑事实。', '',
            '## 已实际返回的阶段', '']
        completed=status.get('completed',[])
        if not completed:
            lines.append('尚无已返回的科学阶段。启动成功不能替代科学返回。')
        # The recipe contract provides metadata here, never field arrays.
        fields=('name','stage','state','returncode','seconds','scope','input_sha256',
                'bundle_sha256','report_sha256','metrics','outputs','output_files',
                'input_files','historical_output_sha256','same_as_historical',
                'output_bundle','output_report','parent_sha256','output_bundle_sha256',
                'historical_bundle_sha256','historical_bytes_match','Phi','max_gram',
                'weighted_sse','raw_sse','product','final_known_point_safety_pass',
                'final_damping','status','source_commit','source_sha256','command',
                'cleanup_generated','step_id')
        for number,record in enumerate(completed,1):
            compact={key:record[key] for key in fields if key in record}
            if 'command' in compact and 'input_files' in compact:
                compact['input_files']=[{key:value for key,value in item.items() if key!='command'} for item in compact['input_files']]
            lines += [f'### {number}. {record.get("name",record.get("stage","returned stage"))}', '',
                      '```json',json.dumps(compact,ensure_ascii=False,indent=2),'```','']
        if status.get('failed'):
            compact={key:status['failed'][key] for key in fields if key in status['failed']}
            lines += ['## 实际失败或未完整返回的阶段','',
                      '这不是已完成阶段；实际退出码、已有输出和未付范围如下。','',
                      '```json',json.dumps(compact,ensure_ascii=False,indent=2),'```','']
        if status.get('error'):
            lines += ['实际编排错误：`'+str(status['error']).replace('`','\\`')+'`。','']
        lines += ['## 完整可复现参数','',
                  '下列请求配合同一执行源码提交中的编排器给出完整命令及其依赖；重建后的浮点数组独立命名和记录身份，所有新场的几何均重新评估。', '',
                  '```json',json.dumps(self.request,ensure_ascii=False,indent=2),'```','',
                  '有限采样下降、内部几何余量、进程exit0和输入重建均不等于README的连续度量、全t reach或固定参数精化标准。未返、未启动、真正拒绝和已接受以各阶段实际记录区分。','']
        text='\n'.join(lines)
        if len(text.encode())>=95000:
            raise RuntimeError('Compact Actions note exceeds the repository Markdown bound; retain raw metadata in scratch and revise the renderer')
        return text

    def publish(self,status,exit_code=None,force=False):
        snapshot=json.dumps({'completed':status.get('completed',[]),
            'state':status.get('state'),'exit_code':exit_code},sort_keys=True)
        if snapshot==self.last_snapshot and not force:
            return
        self.sync()
        note=self.repo/self.note
        note.write_text(self.render(status,exit_code))
        handoff=self.repo/TOPIC/'HANDOFF.md'
        text=handoff.read_text()
        marker='\n## 当前公开Actions执行\n'
        if marker in text:
            text=text[:text.index(marker)]
        text+=marker+'\n'+f'run [{self.run_id}/{self.attempt}]({self.run_url})，源码`{self.source_commit}`；[实际紧凑记录](notes/{note.name})。当前`{status.get("stage","not_reported")}`/{status.get("state","not_reported")}，返回阶段{len(status.get("completed",[]))}；退出码{exit_code if exit_code is not None else "未返"}。\n\n'
        text+=f'Actions规则核查：{utc()}，真实pull至`{self.rule_commit}`，双README相对已读无变化。\n'
        if len(text.encode())>=10000:
            raise RuntimeError('HANDOFF must be condensed before appending the actual Actions status')
        handoff.write_text(text)
        topic_bytes=sum(path.stat().st_size for path in (self.repo/TOPIC).rglob('*') if path.is_file())
        if topic_bytes>200000000:
            raise RuntimeError('The topic exceeds the explicit 200 MB repository bound; preserve provenance and retire reproducible old raw before publication')
        self.git('diff','--check',capture=False)
        self.git('add',self.note,str(handoff.relative_to(self.repo)),capture=False)
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
            self.sync()
            text=handoff.read_text()
            text=re.sub(r'Actions规则核查：[^\n]*',
                f'Actions规则核查：{utc()}，真实pull至`{self.rule_commit}`，双README相对已读无变化。',text)
            handoff.write_text(text)
            self.git('add',str(handoff.relative_to(self.repo)),capture=False)
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
        followup_path=source/TOPIC/'scripts/resume_20261120/public_actions_followups.py'
        spec=importlib.util.spec_from_file_location('pinned_public_actions_followups',followup_path)
        followups=importlib.util.module_from_spec(spec);sys.modules[spec.name]=followups
        spec.loader.exec_module(followups)
    for name,expected in request['rules_sha256'].items():
        if name not in RULES or digest(source/name)!=expected:
            raise RuntimeError('The pinned source rule bytes differ from the request actually read by the research agent')
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
