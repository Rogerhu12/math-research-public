#!/usr/bin/env python3
"""Recover the original current-centre Airy certificate on a real runner.

This is an actual replay of lost output. It does not infer success from
historical summaries, change the mathematical gates, or publish binary via API.
"""
from pathlib import Path
import datetime, gzip, hashlib, json, os, re, subprocess, sys, time
TOPIC=Path(__file__).resolve().parents[1]
REPO=TOPIC.parents[1]
NATIVE=TOPIC/'notes/2026-11-13-R133-current-moving0765-complete-fold-Airy-ports-native.json.gz'
PROCESS=TOPIC/'notes/2026-11-13-R133-current-moving0765-Airy-CI-recovery-process.json'
STDOUT=TOPIC/'notes/2026-11-13-R133-current-moving0765-Airy-CI-recovery-stdout.log.gz'
SOURCE=TOPIC/'scripts/fourfold_codazzi_current_moving_fold_Airy.py'
SOURCE_SHA='1bd118841981689d6e947fe4234e62d4ecca2a942b008746d469c4fe495a6a0b'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d): p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
if sha(SOURCE)!=SOURCE_SHA: raise RuntimeError('The original completed producer changed')
if NATIVE.exists(): raise FileExistsError('Do not overwrite an earlier actual native certificate')
started=time.monotonic()
command=[sys.executable,str(SOURCE),'--out',str(NATIVE.relative_to(TOPIC))]
doc=dict(kind='actual_replay_of_lost_final_centre_Airy_native',complete=False,
         historical_original_native_recovered=False,actual_fresh_computation=True,
         original_native_sha256='34aeb2a304d2ac814524b0e90553852bbea895b806b5cf26b64d11af46c41844',
         source_sha256=SOURCE_SHA,candidate_sha256=CANDIDATE,
         command=command,run_id=os.environ.get('GITHUB_RUN_ID'),
         workflow_commit=os.environ.get('GITHUB_SHA'),exit_code=None)
save(PROCESS,doc)
p=subprocess.run(command,cwd=TOPIC,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print(p.stdout,flush=True)
STDOUT.write_bytes(gzip.compress(p.stdout.encode(),mtime=0))
doc.update(exit_code=p.returncode,wall_seconds=time.monotonic()-started,stdout_sha256=sha(STDOUT))
if NATIVE.exists():
    native=json.loads(gzip.decompress(NATIVE.read_bytes()))
    doc.update(native_sha256=sha(NATIVE),native_bytes=NATIVE.stat().st_size,
               native_complete=native.get('complete'),gate_count=len(native.get('gates',[])))
    doc['complete']=bool(p.returncode==0 and native.get('complete') and native.get('proved')
        and native.get('source_sha256')==SOURCE_SHA and native.get('candidate_sha256')==CANDIDATE
        and len(native.get('gates',[]))==27 and all(g['passed'] for g in native['gates']))
save(PROCESS,doc)
print(json.dumps(doc),flush=True)
if not doc['complete']: raise RuntimeError('Actual recovery did not pass the original complete gates')
for f in (NATIVE,PROCESS,STDOUT):
    if f.stat().st_size>5_000_000: raise RuntimeError('Repository file limit exceeded')
    if f.stat().st_size>1_000_000 and f.suffix!='.gz': raise RuntimeError('Large output needs gzip')
if not os.environ.get('GITHUB_TOKEN'): raise RuntimeError('Runner Git authentication missing')
env=dict(os.environ,GIT_TERMINAL_PROMPT='0')
credential='!f() { printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; }; f'
base=['git','-c','safe.directory='+str(REPO),'-c','gc.auto=0',
      '-c','maintenance.auto=false','-c','credential.helper=','-c','credential.helper='+credential]
def git(args,check=True):
    q=subprocess.run(base+args,cwd=REPO,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and q.returncode:
        print(q.stdout,flush=True); raise RuntimeError('Git '+args[0]+' failed')
    return q
git(['config','user.name','github-actions[bot]'])
git(['config','user.email','41898282+github-actions[bot]@users.noreply.github.com'])
read=git(['rev-parse','HEAD']).stdout.strip()
rules=['README.md','topics/visible-flex-exact-nearby/README.md']
git(['pull','--rebase','--no-tags','origin','main'])
newread=git(['rev-parse','HEAD']).stdout.strip()
diff=git(['diff',read,newread,'--',*rules]).stdout
if diff:
    print('README_CHANGED_REQUIRES_CURRENT_RESEARCHER_REVIEW\n'+diff,flush=True)
    raise RuntimeError('New repository rules must be consumed before publication')
h=TOPIC/'HANDOFF.md';text=h.read_text()
text=re.sub(r'最后实际pull核对[0-9a-f]{40}', '最后实际pull核对'+newread,text)
text=text.replace('仅需实际重算小consumer','小consumer已由CI实际重算27门全过')
if len(text.encode())>=10000: raise RuntimeError('Handoff size limit')
h.write_text(text)
log=TOPIC/'log.md'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
with log.open('a') as stream:
    stream.write('\n- '+now+'｜visible-exact-astra-ac0d/CI：在真实runner用原源码重算丢失的新中心fold/Airy native，27门全部通过；保存新原生SHA与原实际退出0，未冒称找回旧二进制。真实pull后双README无变，继续完整全BVP/几何。\n')
paths=[str(f.relative_to(REPO)) for f in (NATIVE,PROCESS,STDOUT,h,log)]
git(['add','--sparse','--',*paths])
git(['commit','-m','visible-exact: recover the final-centre full Airy native by actual computation'])
read=newread
while True:
    push=git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
    print(push.stdout,flush=True)
    if push.returncode==0:
        print('ACTUAL_NATIVE_PUBLISHED',git(['rev-parse','HEAD']).stdout.strip(),flush=True);break
    if not any(s in push.stdout for s in ('fetch first','non-fast-forward','failed to update ref','remote rejected')):
        raise RuntimeError('Actual Git push failed; complete native remains in artifact')
    git(['pull','--rebase','--no-tags','origin','main'])
    newread=git(['rev-parse','origin/main']).stdout.strip()
    diff=git(['diff',read,newread,'--',*rules]).stdout
    if diff:
        print('README_CHANGED_REQUIRES_CURRENT_RESEARCHER_REVIEW\n'+diff,flush=True)
        raise RuntimeError('Repository rules changed during rebase')
    text=h.read_text();text=re.sub(r'最后实际pull核对[0-9a-f]{40}','最后实际pull核对'+newread,text)
    h.write_text(text);git(['add','--sparse','--',str(h.relative_to(REPO))])
    git(['commit','--amend','--no-edit'])
    read=newread
