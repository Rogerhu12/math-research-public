#!/usr/bin/env python3
"""Owned result queue; actual pull/read-diff/normal-push, no force, no credentials."""
import argparse,datetime,json,re,subprocess,time
from pathlib import Path
ROOT=Path('/workspace/scratch/d1aa462cfc02');REPO=ROOT/'math-research';TOP='topics/visible-flex-larger-amplitude';T=REPO/TOP
QUEUE=ROOT/'publish_queue.json';STATE=ROOT/'publish_queue_state.json';SNAP=ROOT/'handoff_current_snapshot.json'
def event(kind,**fields):
 record=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),kind=kind,**fields)
 with (ROOT/'publisher_events.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
 tmp=ROOT/'publisher_heartbeat.next.json';tmp.write_text(json.dumps(record)+'\n');tmp.replace(ROOT/'publisher_heartbeat.json')
def git(*a,capture=False,check=True):
 event('git_start',args=list(a))
 r=subprocess.run(['git',*a],cwd=REPO,text=True,stdout=subprocess.PIPE if capture else None,stderr=subprocess.STDOUT if capture else None)
 event('git_end',args=list(a),returncode=r.returncode)
 if check and r.returncode:
  if capture:print(r.stdout,flush=True)
  raise SystemExit(r.returncode)
 return r
def textgit(*a):return git(*a,capture=True).stdout.strip()
def commit(msg,paths):
 if paths:git('add','--',*paths)
 if git('diff','--cached','--quiet',check=False).returncode:git('commit','-m',msg)
def apply_snapshot(read,when):
 d=json.loads(SNAP.read_text());s=d['handoff'];mark='<!-- current-instruction-read -->';line=f'{mark}\n最近成功实际pull：{when}；已读双README提交：{read}；与上次相比无变化。\n'
 if mark in s:s=re.sub(re.escape(mark)+r'\n[^\n]*\n',lambda _:line,s,count=1)
 else:s=s.rstrip()+'\n\n'+line
 if len(s.encode())>=10000:raise SystemExit('Current HANDOFF snapshot exceeds10000B')
 (T/'HANDOFF.md').write_text(s)
 if d.get('open_section'):
  p=T/'open.md';s=p.read_text();start=s.index('## 2026-11-13 当前连续执行口');end=s.index('\n## ',start+5)
  s=s[:start]+d['open_section'].rstrip()+'\n'+s[end:];p.write_text(s)
def rotate_log_if_needed(read):
 p=T/'log.md';raw=p.read_bytes()
 if len(raw)<95000:return []
 if len(raw)>=100000:raise SystemExit('Topic log reached markdown size gate')
 name='2026-11-13-root-log-history-through-'+read[:12]+'.md';dest=T/'notes'/name
 if dest.exists():
  if dest.read_bytes()!=raw:raise SystemExit('Immutable log archive identity differs')
 else:dest.write_bytes(raw)
 lines=raw.decode().splitlines(keepends=True);target=max(0,len(raw)-22000);offset=0;cut=None
 for i,line in enumerate(lines):
  if offset>=target and (line.startswith('### ') or line.startswith('## ') or line.startswith('- 2026-')):
   cut=i;break
  offset+=len(line.encode())
 if cut is None:raise SystemExit('No complete log entry boundary found')
 p.write_text('# 日志\n\n早期完整日志逐字归档于 [历史日志](notes/'+name+')；以下保留最近完整条目，旧结论与失败记录均可追溯。\n\n'+''.join(lines[cut:]))
 print('LOG_HISTORY_ARCHIVED',name,len(raw),'CURRENT',p.stat().st_size,flush=True)
 return [TOP+'/notes/'+name]

def main():
 a=argparse.ArgumentParser();a.add_argument('--read-sha',required=True);a.add_argument('--watch',action='store_true');z=a.parse_args();read=z.read_sha
 state=json.loads(STATE.read_text()) if STATE.exists() else {'committed':[],'pushed':[]};last_when=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds');attempt=0
 while True:
  # Immediately following every rejected push, pull/rebase again before edits.
  git('pull','--rebase','--no-stat','origin','main')
  if git('merge-base','--is-ancestor','origin/main','HEAD',check=False).returncode:
   print('PULL_DID_NOT_FINISH_REBASE: preserve worktree state and diagnose before recording success',flush=True)
   return 5
  head=textgit('rev-parse','origin/main');last_when=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
  diff=git('diff',read,head,'--','README.md',TOP+'/README.md',capture=True).stdout
  print('ACTUAL_PULL',last_when,head,flush=True)
  if diff:print('INSTRUCTION_DIFF_REQUIRES_READING\n'+diff,flush=True);return 4
  read=head
  # A prior successful push may have completed before its local state write.
  if textgit('rev-parse','HEAD')==head:
   state['pushed']=state['committed'][:];STATE.write_text(json.dumps(state,indent=2)+'\n')
  apply_snapshot(read,last_when)
  pending=[i for i in state['committed'] if i not in state['pushed']]
  queue=json.loads(QUEUE.read_text());job=None if pending else next((j for j in queue if j['id'] not in state['committed']),None)
  if pending:
   # Publish this conclusion before staging the next one. Amend only an unpublished tip.
   if textgit('rev-parse','HEAD')==head:raise SystemExit('Unexpected published tip while pending')
   git('add','--',TOP+'/HANDOFF.md',TOP+'/open.md')
   if git('diff','--cached','--quiet',check=False).returncode:git('commit','--amend','--no-edit')
  elif job:
   if job.get('result_entry'):
    p=T/'results.md';s=p.read_text()
    if job['result_entry'] not in s:p.write_text(s.rstrip()+'\n\n'+job['result_entry'].rstrip()+'\n')
   if job.get('log_entry'):
    p=T/'log.md';s=p.read_text()
    if job['log_entry'] not in s:p.write_text(s.rstrip()+'\n\n'+job['log_entry'].rstrip()+'\n')
   archive_paths=rotate_log_if_needed(read)
   paths=sorted(set(job['paths']+archive_paths+[TOP+'/'+p for p in ('HANDOFF.md','open.md','results.md','log.md')]))
   commit(job['message'],paths);state['committed'].append(job['id']);STATE.write_text(json.dumps(state,indent=2)+'\n')
   print('QUEUED_CONCLUSION_COMMITTED',job['id'],textgit('rev-parse','HEAD'),flush=True)
  else:
   paths=[TOP+'/HANDOFF.md',TOP+'/open.md'];git('add','--',*paths)
   if git('diff','--cached','--quiet',check=False).returncode:
    if attempt and textgit('log','-1','--format=%s')=='visible-larger: record actual pull and current research checkpoint':git('commit','--amend','--no-edit')
    else:commit('visible-larger: record actual pull and current research checkpoint',[])
  pushed=git('push','origin','HEAD:main',capture=True,check=False);print(pushed.stdout,flush=True)
  if not pushed.returncode:
   state['pushed']=state['committed'][:];state['last_pushed_sha']=textgit('rev-parse','HEAD');STATE.write_text(json.dumps(state,indent=2)+'\n');print('PUSHED',state['last_pushed_sha'],flush=True)
   if all(j['id'] in state['committed'] for j in json.loads(QUEUE.read_text())):
    if not z.watch:return 0
    saved_snapshot=SNAP.read_bytes();idle_started=time.monotonic()
    event('queue_idle',last_pushed_sha=state['last_pushed_sha'],read_rules_sha=read)
    while (time.monotonic()-idle_started<3000 and SNAP.read_bytes()==saved_snapshot
           and all(j['id'] in state['committed'] for j in json.loads(QUEUE.read_text()))):
     time.sleep(10)
    attempt=0
    continue
  elif not any(t in pushed.stdout for t in ('non-fast-forward','fetch first','cannot lock ref','remote unpack failed','index-pack failed')):return pushed.returncode
  else:print('Retrying immediate normal pull/rebase after concurrent remote advance',flush=True)
  attempt+=1
if __name__=='__main__':raise SystemExit(main())
