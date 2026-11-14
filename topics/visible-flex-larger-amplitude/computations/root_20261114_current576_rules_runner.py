#!/usr/bin/env python3
"""Actual public Actions rule synchronization in a separate sparse mirror.

Only metadata/Git work occurs here.  The science command retains its argv,
cwd, environment and inherited stdout/stderr.  Ordinary synchronization
failures are recorded while science continues; an actual README change is
different: retain and print its diff, terminate the science process group,
and return a nonzero code for the coordinator to read and apply the rules.
No force push, token file, science checkout mutation, or scientific gate.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time

REPOSITORY='Rogerhu12/math-research-public'
URL='https://github.com/Rogerhu12/math-research-public.git'
TOPIC='topics/visible-flex-larger-amplitude'
HANDOFF=TOPIC+'/HANDOFF.md'
RULE_PREFIX='规则同步记录：'
SUBJECT='visible-larger: record actual current576 rules synchronization'
TRAILER='Rules-Runner: current576-v1'
PERIOD_SECONDS=2700
BASELINES=json.loads("{\"README.md\":{\"blob\":\"6183b7f3eaa5edf22cd1a62fa19d84bf4ab3ba09\",\"text\":\"# math-research-public\\n\\n公开的数学研究工作仓库：可弯曲闭曲面的大振幅与精确解、Serre 一致性、秩二曲线的 Ш、Hilbert 空间不变子空间问题。由 ChatGPT Pro 会话持续写入，协调员和作者审阅。2026-11-14 从私有仓库 `Rogerhu12/math-research` 迁入（只迁当时的文件，不含历史提交）。\\n\\n课题：\\n\\n| 目录 | 问题 |\\n|---|---|\\n| `topics/visible-flex-larger-amplitude` | 把“瘪易拉罐”的可见弯曲幅度做大 |\\n| `topics/visible-flex-exact-nearby` | 证明“瘪易拉罐”附近有精确解 |\\n| `topics/visible-flexible-closed-surface` | 好看的可弯曲闭曲面（上面两题的数据来源） |\\n| `topics/visible-flex-new-mechanism` | 大振幅的可弯曲闭曲面（优先尝试新构造） |\\n| `topics/serre-uniformity` | Serre 一致性 |\\n| `topics/rank2-sha-infinitely-many-p` | 秩 $\\\\ge2$ 的椭圆曲线对无穷多个 $p$ 有 Ш$[p^\\\\infty]$ 有限 |\\n| `topics/invariant-subspace-problem` | Hilbert 空间上的不变子空间问题 |\\n\\n## 授权（作者原话，2026-11-12，对所有课题有效）\\n\\n授权：本任务中可以随时 git commit，并把本任务产生的全部文件（研究结果、笔记、日志、状态）推送到本仓库 origin/main，不需要再问我。禁止 force push；工作需要时可以改仓库里的任何文件，范围按下面规矩第 2 条（包括 workflow、共享文件和其他课题目录）；令牌只在命令行里用，不写进文件或提交。\\n如果某个操作被自动审批拒绝，不要停下来等我：记下来，继续做能做的，最后统一列出。\\n**达到课题 README 的完成标准之前不要停止。** 不要停在阶段报告、中间结果或\\\"下一步建议\\\"上等我回复，时长到了也不是停下的理由；做完一个子问题就接着做下一个。只有真正完成才收尾，`HANDOFF.md` 随时保持最新（详见规矩第 6 条）。\\n\\n## 规矩\\n\\n1. **课题范围**：本仓库只放上面表里列出的课题，由作者在私有仓库 `Rogerhu12/math-research` 的 `QUEUE.md` 分配；不要在这里新开课题。各课题的完成标准仍以本仓库里该课题的 `README.md` 为准。\\n2. **可以改任何文件，不用请求授权（2026-11-10 起）**：工作需要时，可以直接修改仓库里的任何文件，包括 `.github/` 下的 workflow、根 README 以外的共享文件和其他课题的目录，不必等作者或协调方批准。改了自己课题以外的文件，在自己课题的 `log.md` 追加一行说明改了什么、为什么。唯一的限制：不要强推，不要删除或改写别人已经推送的提交。**CI 或其他共享设施出故障时自己修**，修不好就在 log 里记一行，继续做其他能做的事；不要因为等待授权或等待 CI 而停下。\\n3. **区分可信度**：每条结论标明是\\\"已证明\\\"、\\\"猜想\\\"还是\\\"启发式/数值证据\\\"。只有给出完整证明的才能写进 `results/`；证明里有缺口的，写清缺口在哪，放进 `open.md`。\\n4. **写法**：Markdown，公式用 `$...$` 和 `$$...$$`。引用文献写清作者、标题、年份，能给出处就给定理编号或页码。\\n5. **勤提交**：每完成一个有意义的步骤（一个引理、一次计算、一条被排除的路线）就提交推送，不要攒。推送前先拉取最新 `main`。推送被拒（非快进）时立刻 `git pull --rebase` 再推，循环到成功。提交信息写清楚做了什么。失败的尝试也记进 `notes/`，它们同样有价值。\\n6. **持续工作**：一个子问题做完就记录结果，接着做 `open.md` 里下一个；课题做完（或确认卡死，写明原因）就在 `QUEUE.md` 标为\\\"完成\\\"或\\\"搁置\\\"，再领下一个。不要停在阶段报告上等人回复。**时间到了不是停下的理由**：即使 prompt 里写了\\\"至少持续若干小时\\\"，那也只是下限，到点后继续研究；只有按完成标准真正完成才收尾。\\\"搁置\\\"只用于确认卡死，并在 `open.md` 写清卡在哪里；不要因为时长已满就标搁置，也不要为了结束而放宽完成标准。收尾前更新 `HANDOFF.md`。\\n7. **日志**：每轮工作结束时，只在自己课题的 `log.md` 末尾追加一条（日期时间、会话名、做了什么、下一步，五行以内）。**2026-11-13 起不再写根目录 `LOG.md`，也不再归档它**：几十个会话同时往同一个文件末尾追加，会让推送反复冲突、合不进 `main`。\\n8. **少读大文件（重要）**：大文件会拖慢工作。\\n   - 接手或开始新一轮时，只读本 README、自己课题的 `HANDOFF.md` 和 `open.md`。\\n   - 不要整篇打开超过 100 KB 的文件，包括 `results/archive-*/` 的分卷、`log/` 下的旧日志和 `notes/` 里的大文件。需要旧结论时，先查 `results/archive-*/INDEX.md`，只打开它所在的那一卷。\\n   - 单个 Markdown 文件不超过 100 KB；`README.md`、`open.md` 尽量不超过 30 KB，超出就把旧内容移进 `notes/`。\\n   - 新结论写成新文件 `results/R<编号>-<短名>.md`，并在 `results.md` 的\\\"新增结论\\\"列表加一行。不要往大文件末尾追加。\\n   - 数据文件超过 1 MB 先压缩成 `.gz`；不要提交超过 5 MB 的文件。\\n   - **推送用终端 git（2026-11-09 起）**：经 GitHub 集成或 API 工具传送的内容都会进入对话，大数据会拖慢工作。有终端 git 认证时一律用终端 `git push`，令牌只在终端里使用，不写进任何文件、提交、日志、HANDOFF 或笔记，也不在回复里重复。只有 GitHub 集成可用时，集成只传文本和小于 100 KB 的文件；更大的数据文件不提交，只提交生成它的脚本、参数和哈希，保证可以重新生成。不要把数据分块或编码后经工具调用传送，也不要把二进制内容读进对话。这一条优先于课题 README 中直接提交数据的要求。\\n9. **交接摘要**：每轮结束时重写自己课题的 `HANDOFF.md`，不超过 10 KB：问题一句话、当前状态、已证结论的编号各一句、下一步、正在用的文件。下一个会话只靠它和 `open.md` 接手。\\n10. **不要完整克隆（2026-11-10 起）**：仓库有数 GB，几乎全是 `topics/` 下的数据。完整克隆或拉取会占满沙盒磁盘、耗费大量时间。一律用部分克隆，只检出需要的目录：\\n    ```\\n    git clone --filter=blob:none --sparse https://github.com/Rogerhu12/math-research-public.git\\n    cd math-research-public\\n    git sparse-checkout set topics/<你的课题> papers/<需要的论文>\\n    ```\\n    需要读其他目录时用 `git sparse-checkout add <目录>`，或 `git show origin/main:<路径>` 只取单个文件。已有的完整克隆也改成这样（`git sparse-checkout set ...`）。\\n    - 数据文件只提交复核真正需要的；可由脚本和参数重新生成的大中间数据不入库，只提交脚本、参数和哈希。每个课题的数据总量尽量控制在 200 MB 以内。\\n11. **规矩会更新，每次拉取后检查（2026-11-10 起）**：作者和协调方会随时修改本 README 和自己课题的 README。每次 `git pull` 之后（至少每小时一次）检查这两个文件有没有变：\\n    ```\\n    git diff <上次读过的提交> origin/main -- README.md topics/<你的课题>/README.md\\n    ```\\n    有变化就只读这段差异并立即照新规矩执行，没有变化就不用重读。把读过的提交号记在 `HANDOFF.md` 里，供下次比较和接手。\\n12. **不为防错设流程（2026-11-10 起）**：作者只担心做少，不担心做错或做多。新结论写出完整证明就直接登记进 `results/`，不必先冻结候选、请未参与者独立审查、逐字归档、机械核验或独立重跑；各课题 README（包括其状态段）里残留的这类要求一律作废，已经在走的这类流程可以停掉。省下来的时间用来推进问题本身。完成标准里写明“只算中间进展”的情形照旧不算完成。\\n13. **CI 直接用本仓库的 GitHub Actions（2026-11-14 起）**：本仓库公开，Actions 不受私有仓库计费故障影响（`ubuntu-latest`，4 核、16 GB 内存，单任务最长约 6 小时，账号内最多 20 个任务同时运行）。workflow 放在本仓库 `.github/workflows/`，按 push 或手动触发，结果提交回本仓库。只运行本仓库这些课题的计算。需要读取私有仓库 `Rogerhu12/math-research` 中其他课题的来源文件时，在 workflow 里用 `secrets.MR_TOKEN`。私有仓库里还没执行的 `ci-queue/` 请求不会再运行，需要的请改成本仓库的 workflow。\\n14. **本仓库公开**：所有内容任何人可见。令牌照旧只在命令行或 Actions secret 里用，不写进文件、提交、日志或 workflow 明文。\\n\"},\"topics/visible-flex-larger-amplitude/README.md\":{\"blob\":\"bff8aea253a9e6a7a4fac28d810ac454c5499fec\",\"text\":\"# 把“瘪易拉罐”的弯曲幅度做大\\n\\n> 2026-11-14 从私有仓库 `Rogerhu12/math-research` 迁入本公开仓库（路径不变）；之后只在本仓库工作，计算用本仓库的 GitHub Actions（根 README 规矩第 13 条）。\\n\\n## 问题\\n\\n`topics/visible-flexible-closed-surface` 在 flat17 参数下得到了一个数值上的闭曲面等距弯曲族，俗称“瘪易拉罐”，参数和数据见该课题的 HANDOFF。它目前的指标是：\\n- M12 网格上，$\\\\delta_{\\\\rm hold}/D>0.0528$，reach$/D>0.0312$，$\\\\delta_{\\\\rm E}>0$；\\n- 整面度量误差约 $2.6\\\\times10^{-8}$。\\n\\n拿在手里看，弯曲仍然不够明显。本题要把弯曲幅度做大。可以从 flat17 出发，也可以换别的机制。\\n\\n记号 $D$、握持区 $H$、$\\\\delta_{\\\\rm hold}$、$\\\\delta_{\\\\rm E}$、reach 的定义，都与 `topics/visible-flexible-closed-surface/README.md` 相同。\\n\\n## 完成标准\\n\\n给出满足以下全部条件的解，由可复现的脚本生成：\\n\\n1. $M$ 是连通闭曲面；对每个 $t$，$F_t$ 是 $C^2$ 嵌入，$t\\\\mapsto F_t$ 在 $C^2$ 拓扑下连续。\\n2. 握持区 $H$ 的内部非空，$\\\\operatorname{diam}F_0(H)\\\\ge0.2\\\\,D$，并且 $\\\\delta_{\\\\rm hold}\\\\ge0.2\\\\,D$、$\\\\delta_{\\\\rm E}>0$。\\n3. 对每个 $t$，reach $\\\\ge0.03\\\\,D$。\\n4. 全部 $F_t$ 对同一个度量 $g$ 等距：在整个曲面和全部 $t$ 上，诱导度量相对 $g$ 的最大相对误差不超过 $10^{-6}$。\\n5. 必须是某个精确解的近似：度量、参数和 $t$ 的范围都不变，在网格、频率和 $t$ 的加密下，等距误差持续下降，直到机器精度或求解容差。\\n6. 嵌入性和 reach 在全部 $t$ 上检查，不只检查端点。\\n7. 提供若干个 $t$ 的网格文件（单个文件小于 5 MB），并说明数值解与严格存在性之间还差什么。\\n\\n**更强的目标：** $\\\\delta_{\\\\rm hold}$ 和 $\\\\delta_{\\\\rm E}$ 越大越好。达到完成标准后继续推进，并报告能做到的最大 $\\\\delta_{\\\\rm hold}/D$、$\\\\delta_{\\\\rm E}/D$ 和 reach$/D$。\\n\\n以下只算中间进展：\\n- $\\\\delta_{\\\\rm hold}<0.2\\\\,D$ 或 reach $<0.03\\\\,D$ 的解，不论按环宽或其他长度算比例有多大；\\n- 带边的曲面片或环带；\\n- 某些时刻不嵌入的族；\\n- 误差不随加密趋于零的近似解；\\n- 只靠层数、尺度比等渐近参数把固有缺陷压小的构造；\\n- 不可能性或障碍类结果。\\n\\n## 来源\\n\\n- `topics/visible-flexible-closed-surface`（flat17 的参数、脚本和数据）、`topics/large-amplitude-twist-flex`、`topics/smooth-unrippled-twist-flex`、`topics/explicit-flexible-closed-surface`、`topics/flexible-surface-model`、`topics/continuous-flexibility-swarm`。\\n\"}}")


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


class SyncFailure(RuntimeError):
    pass


class RulesChanged(SyncFailure):
    pass


class Runner:
    def __init__(self,out):
        if (os.environ.get('GITHUB_ACTIONS')!='true' or
                os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY or
                os.environ.get('GITHUB_SERVER_URL','https://github.com')!='https://github.com'):
            raise SyncFailure('This metadata runner is restricted to the named public GitHub Actions repository')
        token=os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
        if not token:raise SyncFailure('An Actions GITHUB_TOKEN or GH_TOKEN environment value is required')
        self.private=[token,base64.b64encode(('x-access-token:'+token).encode()).decode()]
        for path,ref in BASELINES.items():
            if git_blob(ref['text'].encode())!=ref['blob']:
                raise SyncFailure('The embedded reviewed README bytes differ from their Git blob: '+path)
        root=Path(os.environ['RUNNER_TEMP']).resolve()
        if not root.is_dir():raise SyncFailure('A real RUNNER_TEMP directory is required')
        self.out=out.resolve()
        workspace=Path(os.environ['GITHUB_WORKSPACE']).resolve()
        if self.out==workspace or self.out.is_relative_to(workspace):
            raise SyncFailure('Rule receipts must be outside the fixed scientific checkout')
        self.out.mkdir(parents=True,exist_ok=False)
        self.scratch=Path(tempfile.mkdtemp(prefix='visible-current576-rules-',dir=root))
        self.mirror=self.scratch/'mirror'
        self.env=dict(os.environ)
        for key in list(self.env):
            if (key.startswith('GIT_CONFIG_') or key.startswith('GIT_TRACE') or
                    key in ('GIT_DIR','GIT_WORK_TREE','GIT_INDEX_FILE','GIT_OBJECT_DIRECTORY',
                            'GIT_ALTERNATE_OBJECT_DIRECTORIES','GIT_CURL_VERBOSE')):
                self.env.pop(key,None)
        self.env.update(GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never',
            GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=os.devnull,GIT_EDITOR='true')
        settings=[
            ('http.https://github.com/.extraheader','AUTHORIZATION: basic '+self.private[1]),
            ('http.followRedirects','false'),('credential.helper',''),
            ('gc.auto','0'),('gc.autoDetach','false'),('maintenance.auto','false'),
            ('commit.gpgSign','false'),('user.name','github-actions[bot]'),
            ('user.email','41898282+github-actions[bot]@users.noreply.github.com')]
        self.env['GIT_CONFIG_COUNT']=str(len(settings))
        for n,(key,value) in enumerate(settings):
            self.env['GIT_CONFIG_KEY_'+str(n)]=key
            self.env['GIT_CONFIG_VALUE_'+str(n)]=value
        self.round=0
        self.current_events=[]
        self.receipt('runner-identity.json',dict(
            schema='current576-rules-runner-identity-v1',source_sha256=digest(Path(__file__).read_bytes()),
            repository=REPOSITORY,created_utc=utc(),mirror=str(self.mirror),
            scientific_checkout=str(workspace),science_checkout_modified=False,
            reviewed_README_blobs={path:ref['blob'] for path,ref in BASELINES.items()},
            period_seconds=PERIOD_SECONDS,credential_scope='Git subprocess environment only',
            no_credential_written_to_file_or_git_config=True,no_force_push=True,
            scope='Git and rule metadata only; no RHS/J/ODE/matrix/solver computations'))

    def redact(self,text):
        for private in self.private:text=text.replace(private,'[REDACTED]')
        text=re.sub(r'(?im)^authorization:.*$','Authorization: [REDACTED]',text)
        return text

    def receipt(self,name,value):
        raw=(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
        if len(raw)>95000:raise SyncFailure('Rule receipt exceeds the small metadata budget')
        path=self.out/name
        with path.open('xb') as f:f.write(raw)
        return dict(file=name,bytes=len(raw),sha256=digest(raw))

    def git(self,*args,input_bytes=None,check=True):
        command=['git',*args]
        cwd=self.mirror if self.mirror.is_dir() else self.scratch
        try:
            result=subprocess.run(command,cwd=cwd,env=self.env,input=input_bytes,
                stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=300,check=False)
        except subprocess.TimeoutExpired as error:
            raise SyncFailure('Git metadata command timed out: '+args[0]) from error
        if check and result.returncode:
            detail=self.redact(result.stderr.decode('utf-8','replace'))[-12000:]
            raise SyncFailure('Git '+args[0]+' failed ('+str(result.returncode)+'): '+detail)
        return result

    def text(self,*args):
        return self.git(*args).stdout.decode('utf-8').strip()

    def initialize(self):
        self.git('clone','--filter=blob:none','--depth=1','--sparse','--no-checkout',
            '--single-branch','--branch','main','--origin','origin',URL,str(self.mirror))
        patterns='/README.md\n/'+TOPIC+'/README.md\n/'+HANDOFF+'\n'
        self.git('sparse-checkout','set','--no-cone','--stdin',input_bytes=patterns.encode())
        self.git('checkout','main')
        self.git('config','gc.auto','0')
        self.git('config','maintenance.auto','false')
        self.receipt('mirror-created.json',dict(created_utc=utc(),
            mirror=str(self.mirror),origin=URL,filter='blob:none',depth=1,
            sparse_files=['README.md',TOPIC+'/README.md',HANDOFF],
            HEAD=self.text('rev-parse','HEAD'),scientific_checkout_modified=False))

    def check_rules(self,attempt):
        origin=self.text('rev-parse','origin/main')
        observed={}
        differences=[]
        for path,reference in BASELINES.items():
            blob=self.text('rev-parse','origin/main:'+path)
            observed[path]=blob
            if blob==reference['blob']:continue
            size=int(self.text('cat-file','-s','origin/main:'+path))
            if size>100000:
                self.current_events.append(dict(event='README_changed_over_small_text_limit',
                    path=path,reviewed_blob=reference['blob'],observed_blob=blob,bytes=size,origin_main=origin))
                raise RulesChanged('README changed and exceeds100KB; retained its blob/size identity for coordinator')
            raw=self.git('show','origin/main:'+path).stdout
            if git_blob(raw)!=blob:raise SyncFailure('Actual README blob bytes disagree with Git identity')
            current=raw.decode('utf-8')
            delta=''.join(difflib.unified_diff(reference['text'].splitlines(True),current.splitlines(True),
                fromfile='reviewed/'+path,tofile='origin/main/'+path))
            differences.append(delta)
        if differences:
            diff=self.redact('\n'.join(differences))
            raw=diff.encode()
            basename='round-'+str(self.round).zfill(4)+'-attempt-'+str(attempt).zfill(4)+'-README.diff'
            if len(raw)>100000:
                filename=basename+'.gz';payload=gzip.compress(raw,mtime=0)
            else:filename=basename;payload=raw
            with (self.out/filename).open('xb') as f:f.write(payload)
            entry=dict(event='reviewed_README_changed',origin_main=origin,observed_blobs=observed,
                reviewed_blobs={path:ref['blob'] for path,ref in BASELINES.items()},
                diff=dict(file=filename,bytes=len(payload),sha256=digest(payload),
                          uncompressed_bytes=len(raw),uncompressed_sha256=digest(raw)),
                actual_pull_completed=True,time_utc=utc())
            self.current_events.append(entry)
            print(diff,end='' if diff.endswith('\n') else '\n',flush=True)
            raise RulesChanged('Root/topic README changed after actual pull; coordinator must read retained diff')
        return origin,observed

    def rewrite_rule_line(self,raw,origin):
        raw.decode('utf-8')
        lines=raw.splitlines(keepends=True);prefix=RULE_PREFIX.encode()
        locations=[i for i,line in enumerate(lines) if line.startswith(prefix)]
        if len(locations)!=1:raise SyncFailure('HANDOFF must contain exactly one existing rule synchronization record')
        index=locations[0]
        ending=b'\r\n' if lines[index].endswith(b'\r\n') else b'\n'
        when=utc()
        text=(RULE_PREFIX+when+' 真实 git pull --rebase origin main 后核双README；根'+
            BASELINES['README.md']['blob']+'、题'+BASELINES[TOPIC+'/README.md']['blob']+
            '未变，已读提交 '+origin+'。')
        lines[index]=text.encode()+ending
        result=b''.join(lines)
        if len(result)>10000:raise SyncFailure('Rule-line-only update would exceed the HANDOFF10000B rule')
        return result,when

    def own_rebase_commit(self):
        commit=self.git('show','-s','--format=%B','REBASE_HEAD',check=False)
        if commit.returncode:return False
        message=commit.stdout.decode('utf-8','replace')
        paths=self.git('diff-tree','--no-commit-id','--name-only','-r','REBASE_HEAD').stdout.decode('utf-8').splitlines()
        return message.splitlines()[0]==SUBJECT and TRAILER in message and paths==[HANDOFF]

    def rebase_active(self):
        return ((self.mirror/'.git/rebase-merge').is_dir() or
                (self.mirror/'.git/rebase-apply').is_dir())

    def pull(self,attempt):
        was_rebase_active=self.rebase_active()
        result=self.git('pull','--rebase','origin','main',check=False)
        while result.returncode:
            if not self.rebase_active():
                raise SyncFailure('Actual git pull failed: '+self.redact(result.stderr.decode('utf-8','replace'))[-12000:])
            names=self.git('diff','--name-only','--diff-filter=U','-z').stdout
            paths=[v.decode('utf-8') for v in names.split(b'\0') if v]
            if paths!=[HANDOFF] or not self.own_rebase_commit():
                raise SyncFailure('Rebase conflict is not solely this runner rule-line commit in HANDOFF: '+repr(paths))
            origin,_=self.check_rules(attempt)
            upstream=self.git('show',':2:'+HANDOFF).stdout
            rebuilt,when=self.rewrite_rule_line(upstream,origin)
            (self.mirror/HANDOFF).write_bytes(rebuilt)
            self.git('add','--sparse','--',HANDOFF)
            self.current_events.append(dict(event='own_H_rule_line_conflict_resolved',
                method='rebase stage2 latest upstream H, only unique rule line rewritten',
                rebase_head=self.text('rev-parse','REBASE_HEAD'),origin_main=origin,time_utc=when,
                upstream_H_sha256=digest(upstream),resolved_H_sha256=digest(rebuilt),
                all_other_upstream_H_bytes_retained=True))
            staged=self.git('diff','--cached','--quiet','--',HANDOFF,check=False)
            if staged.returncode==0:
                result=self.git('rebase','--skip',check=False)
            elif staged.returncode==1:
                result=self.git('rebase','--continue',check=False)
            else:raise SyncFailure('Could not inspect the resolved H index')
        if was_rebase_active:
            # Completing a rebase left by an earlier failed round is not a
            # fresh network pull. Perform the actual pull again before recording.
            return self.pull(attempt)
        self.current_events.append(dict(event='actual_pull_rebase_completed',time_utc=utc(),
            origin_main=self.text('rev-parse','origin/main'),HEAD=self.text('rev-parse','HEAD')))
        return self.check_rules(attempt)

    def retryable_push(self,result):
        text=(result.stdout+result.stderr).decode('utf-8','replace').lower()
        return any(marker in text for marker in (
            '[rejected]','non-fast-forward','fetch first','failed to update ref',
            'cannot lock ref','is at ','expected old','reference update failed'))

    def sync(self):
        number=self.round;self.round+=1;self.current_events=[]
        started=utc();attempt=0
        try:
            while True:
                origin,blobs=self.pull(attempt)
                raw=(self.mirror/HANDOFF).read_bytes()
                new,when=self.rewrite_rule_line(raw,origin)
                (self.mirror/HANDOFF).write_bytes(new)
                self.git('add','--sparse','--',HANDOFF)
                staged=self.git('diff','--cached','--quiet','--',HANDOFF,check=False)
                if staged.returncode==1:
                    names=self.git('diff','--cached','--name-only','-z').stdout
                    if names!=HANDOFF.encode()+b'\0':raise SyncFailure('Refuse to commit anything except the H rule line')
                    self.git('commit','-m',SUBJECT,'-m',TRAILER)
                elif staged.returncode!=0:raise SyncFailure('Could not inspect the H rule-line index')
                head=self.text('rev-parse','HEAD')
                pushed=self.git('push','origin','HEAD:refs/heads/main',check=False)
                record=dict(schema='current576-rules-sync-attempt-v1',round=number,attempt=attempt,
                    started_utc=started,read_utc=when,origin_main_read=origin,README_blobs=blobs,
                    H_before_sha256=digest(raw),H_after_sha256=digest(new),
                    local_commit=head,push_returncode=pushed.returncode,
                    stdout=self.redact(pushed.stdout.decode('utf-8','replace'))[-12000:],
                    stderr=self.redact(pushed.stderr.decode('utf-8','replace'))[-12000:],
                    events=self.current_events,force_used=False,science_checkout_modified=False)
                receipt=self.receipt('sync-'+str(number).zfill(4)+'-attempt-'+str(attempt).zfill(4)+'.json',record)
                self.current_events=[]
                if pushed.returncode==0:
                    answer=dict(schema='current576-rules-sync-completed-v1',round=number,
                        completed_utc=utc(),actual_read_utc=when,origin_main_read=origin,
                        published_commit=head,attempts=attempt+1,last_attempt=receipt,
                        README_blobs=blobs,ordinary_git_push_succeeded=True)
                    self.receipt('sync-'+str(number).zfill(4)+'-completed.json',answer)
                    print(json.dumps(dict(event='actual_rules_sync_completed',round=number,
                        time_utc=answer['completed_utc'],origin_main_read=origin,published_commit=head)),flush=True)
                    return answer
                if not self.retryable_push(pushed):
                    raise SyncFailure('Ordinary push failed without an NFF/concurrent-ref cause; retained its sanitized receipt')
                attempt+=1
                # A rejected push is followed immediately by actual pull/rebase.
                # No force, sleep, overwrite of remote refs, or science restart.
        except Exception as error:
            self.receipt('sync-'+str(number).zfill(4)+'-failed.json',dict(
                schema='current576-rules-sync-failure-v1',round=number,attempt=attempt,
                time_utc=utc(),error=self.redact(str(error)),error_type=type(error).__name__,
                events=self.current_events,actual_sync_succeeded=False,
                README_changed=isinstance(error,RulesChanged),science_checkout_modified=False))
            print(json.dumps(dict(event='rules_sync_failed',round=number,
                time_utc=utc(),error=self.redact(str(error)),README_changed=isinstance(error,RulesChanged))),flush=True)
            raise


def stop_for_rule_change(child):
    """Stop this launched science group, retaining all partial output files."""
    if child.poll() is not None:return
    try:os.killpg(child.pid,signal.SIGTERM)
    except ProcessLookupError:pass
    try:child.wait(timeout=15)
    except subprocess.TimeoutExpired:
        try:os.killpg(child.pid,signal.SIGKILL)
        except ProcessLookupError:pass
        child.wait()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--command',nargs=argparse.REMAINDER)
    a=p.parse_args()
    command=list(a.command or [])
    if command and command[0]=='--':command=command[1:]
    runner=None
    try:
        runner=Runner(a.out)
        runner.initialize()
        runner.sync()
    except Exception as error:
        message=runner.redact(str(error)) if runner is not None else type(error).__name__+': '+str(error)
        if runner is not None:
            runner.receipt('startup-failed.json',dict(time_utc=utc(),error=message,
                README_changed=isinstance(error,RulesChanged),science_started=False))
        print(json.dumps(dict(event='rules_startup_failed',error=message,science_started=False)),flush=True)
        return 77 if isinstance(error,RulesChanged) else 70
    if not command:return 0
    started=utc()
    runner.receipt('science-launch.json',dict(
        schema='current576-rules-runner-science-launch-v1',time_utc=started,
        original_argv_sha256=digest(json.dumps(command,ensure_ascii=False,separators=(',',':')).encode()),
        argument_count=len(command),executable=Path(command[0]).name,
        cwd=os.getcwd(),stdout_stderr_inherited=True,environment_unchanged=True,
        separate_process_group_for_rule_change_cancellation=True,
        scientific_budget_or_algorithms_modified=False))
    try:
        child=subprocess.Popen(command,stdout=None,stderr=None,start_new_session=True)
    except Exception as error:
        runner.receipt('science-launch-failed.json',dict(time_utc=utc(),error=runner.redact(str(error))))
        return 70
    next_sync=time.monotonic()+PERIOD_SECONDS;failures=[];rule_change=None
    while child.poll() is None:
        now=time.monotonic()
        if now>=next_sync:
            try:runner.sync()
            except RulesChanged as error:
                rule_change=runner.redact(str(error))
                stop_for_rule_change(child)
                break
            except Exception as error:
                failures.append(dict(time_utc=utc(),error=runner.redact(str(error))))
                # A transport/rebase failure is not a mathematical failure.
                # Keep original science running; report nonzero at completion.
            next_sync=time.monotonic()+PERIOD_SECONDS
            continue
        try:child.wait(timeout=min(1.0,next_sync-now))
        except subprocess.TimeoutExpired:pass
    code=child.wait()
    wrapper_code=77 if rule_change is not None else (code if code else (70 if failures else 0))
    if wrapper_code<0:wrapper_code=128-wrapper_code
    runner.receipt('runner-result.json',dict(
        schema='current576-rules-runner-result-v1',started_utc=started,finished_utc=utc(),
        science_returncode=code,wrapper_returncode=wrapper_code,
        periodic_sync_failures=failures,README_change=rule_change,
        science_terminated_for_actual_rule_change=rule_change is not None,
        partial_scientific_files_not_removed=True,scientific_checkout_modified=False,
        original_scientific_argv_and_budget_preserved=True,sync_rounds_started=runner.round))
    return wrapper_code


if __name__=='__main__':
    raise SystemExit(main())
