#!/usr/bin/env python3
"""No force push, no source checkout mutation, no credential storage.

Inputs are explicit already-complete artifacts and a known common base.
Unchanged remote paths are copied by their Git tree identities, not fetched as
large blobs. A normal Git conflict or changed README stops the attempt so the
owner can read and reconcile it; it never requests extra user approval.
"""
import argparse,datetime,json,os,re,subprocess,sys,time
from pathlib import Path
parser=argparse.ArgumentParser(description='Publish an explicit owned-file overlay by ordinary git push, preserving fresh main and checking both READMEs after every pull.')
parser.add_argument('--snapshot',type=Path,required=True)
parser.add_argument('--receipt',type=Path,required=True)
parser.add_argument('--attempts',type=int,default=30)
parser.add_argument('--live-handoff',type=Path)
parser.add_argument('--attempt-log',type=Path)
parser.add_argument('--checkpoint-ref')
parser.add_argument('--checkpoint-only', action='store_true')
args=parser.parse_args()
def record(value):
 print(json.dumps(value),flush=True)
 if args.attempt_log:
  with args.attempt_log.open('a') as stream:stream.write(json.dumps(value)+'\n')
def rules_update(text,base,now):
 a=text.index('## 2.');b=text.index('## 3.');part=text[a:b]
 part=re.sub(r'`[0-9a-f]{40}`（[0-9-]{10} [0-9:]+ UTC）',f'`{base}`（{now:%Y-%m-%d %H:%M} UTC）',part,count=1)
 part=re.sub(r'下次不晚于[0-9:]+ UTC',f'下次不晚于{now+datetime.timedelta(hours=1):%H:%M} UTC',part,count=1)
 result=text[:a]+part+text[b:];assert len(result.encode())<10000
 return result
checkpoint_done=False
if args.checkpoint_ref and not args.checkpoint_ref.startswith('refs/heads/visible-flex-fd2d-'):
 raise ValueError('Use an explicit owned checkpoint branch')
snapshot=json.loads(args.snapshot.read_text())
message=snapshot['message'];handoff=snapshot['handoff'];hp='topics/visible-flexible-closed-surface/HANDOFF.md'
entry=snapshot['root_log_entry']
assert len(entry)<=200, 'Own root LOG entry must stay within 200 characters'
def run(args,input=None,check=True):
 p=subprocess.run(args,input=input,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 if check and p.returncode:raise RuntimeError(p.stdout)
 return p
old=re.search(r'`([0-9a-f]{40})`',handoff.split('## 2.',1)[1].split('## 3.',1)[0]).group(1)
def blob(text):return run(['git','hash-object','-w','--stdin'],input=text).stdout.strip()
def overlay(tree,patch):
 entries={}
 if tree:
  for row in run(['git','ls-tree','-z',tree]).stdout.split('\0'):
   if not row:continue
   bits,name=row.split('\t',1);mode,kind,sha=bits.split();entries[name]=(mode,kind,sha)
 groups={}
 for path,(mode,sha) in patch.items():
  first,sep,rest=path.partition('/')
  if sep:groups.setdefault(first,{})[rest]=(mode,sha)
  else:entries[first]=(mode,'blob',sha)
 for name,sub in groups.items():
  previous=entries.get(name)
  if previous and previous[1]!='tree':raise RuntimeError('Parent path is not a directory')
  entries[name]=('040000','tree',overlay(previous[2] if previous else None,sub))
 # Canonical tree encoding avoids mktree's per-entry object lookup in this
 # large partial clone. Entries still come only from fresh main or explicit
 # owned hashes. This exact encoding reproduced an existing 5,040-entry tree.
 encoded=[]
 for name,(mode,kind,sha) in entries.items():
  raw_name=name.encode('utf-8')
  if b'\0' in raw_name or b'/' in raw_name:raise ValueError('Invalid tree basename')
  key=raw_name+(b'/' if kind=='tree' else b'')
  value=format(int(mode,8),'o').encode()+b' '+raw_name+b'\0'+bytes.fromhex(sha)
  encoded.append((key,value))
 body=b''.join(value for _,value in sorted(encoded))
 process=subprocess.run(['git','hash-object','-w','-t','tree','--stdin'],input=body,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if process.returncode:raise RuntimeError(process.stderr.decode())
 return process.stdout.decode().strip()
for attempt in range(1,args.attempts+1):
 t=time.monotonic();pull=run(['git','pull','--ff-only','--no-stat','origin','main'],check=False)
 base=run(['git','rev-parse','origin/main']).stdout.strip()
 diff=run(['git','diff',old,base,'--','README.md','topics/visible-flexible-closed-surface/README.md']).stdout
 record(dict(attempt=attempt,pull_exit=pull.returncode,readme_previous=old,readme_current=base,readme_diff_empty=not bool(diff)))
 if diff:print(diff,flush=True);sys.exit(78)
 if pull.returncode:print(pull.stdout,flush=True);sys.exit(pull.returncode)
 if args.live_handoff:
  args.live_handoff.write_text(rules_update(args.live_handoff.read_text(),base,datetime.datetime.now(datetime.timezone.utc)))
 if snapshot.get('base_commit'):
  paths=[path for mode,sha,path in snapshot['entries'] if path!='LOG.md']
  def versions(ref):
   out={}
   for row in run(['git','ls-tree','-r','-z',ref,'--',*paths]).stdout.split('\0'):
    if not row:continue
    bits,path=row.split('\t',1);out[path]=bits.split()[2]
   return out
  previous,current=versions(snapshot['base_commit']),versions(base)
  desired={path:sha for mode,sha,path in snapshot['entries']}
  conflicts=[path for path in paths if previous.get(path)!=current.get(path) and current.get(path)!=desired.get(path)]
  if conflicts:
   print(json.dumps(dict(status='overlapping_remote_changes_require_reading',paths=conflicts)),flush=True)
   sys.exit(79)
 now=datetime.datetime.now(datetime.timezone.utc);h=rules_update(handoff,base,now);old=base
 patch={path:(mode,sha) for mode,sha,path in snapshot['entries'] if path not in ('LOG.md',hp)}
 patch[hp]=('100644',blob(h));log=run(['git','show',base+':LOG.md']).stdout
 if len(log.encode())>50000:
  archive=f'log/LOG-archive-{now:%Y%m%d-%H%M}.md'
  if run(['git','cat-file','-e',base+':'+archive],check=False).returncode==0:raise RuntimeError('Archive collision')
  patch[archive]=('100644',blob(log));log='# 总日志\n\n'
 if entry not in log:log+='\n'+entry
 patch['LOG.md']=('100644',blob(log))
 tree=overlay(run(['git','rev-parse',base+'^{tree}']).stdout.strip(),patch)
 commit=run(['git','commit-tree',tree,'-p',base],input=message+'\n').stdout.strip()
 record(dict(attempt=attempt,tree_ready_seconds=time.monotonic()-t,commit=commit))
 if args.checkpoint_ref and not checkpoint_done:
  valid=run(['git','check-ref-format',args.checkpoint_ref],check=False)
  if valid.returncode:raise ValueError('Invalid checkpoint branch')
  saved=run(['git','push','origin',commit+':'+args.checkpoint_ref],check=False)
  record(dict(attempt=attempt,checkpoint_ref=args.checkpoint_ref,checkpoint_commit=commit,checkpoint_push_exit=saved.returncode,message=saved.stdout))
  if saved.returncode:sys.exit(saved.returncode)
  checkpoint_done=True
  args.receipt.with_name(args.receipt.stem+'-checkpoint.json').write_text(json.dumps(dict(commit=commit,ref=args.checkpoint_ref,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='ordinary push of the complete explicit payload to an owned recovery branch; main integration continues'),indent=2)+'\n')
 if args.checkpoint_only:
  if not checkpoint_done:raise ValueError('--checkpoint-only requires --checkpoint-ref')
  sys.exit(0)
 pushed=run(['git','push','origin',commit+':refs/heads/main'],check=False)
 record(dict(attempt=attempt,push_exit=pushed.returncode,message=pushed.stdout,seconds=time.monotonic()-t))
 if pushed.returncode==0:
  run(['git','reset','--hard',commit])
  args.receipt.write_text(json.dumps(dict(commit=commit,rules_read_sha=base,attempt=attempt,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='ordinary terminal git push; fresh main parent; canonical binary tree overlay preserving all unowned entries'),indent=2)+'\n')
  sys.exit(0)
 # A remote compare-and-swap race after ref advertisement is also a
 # normal non-fast-forward race. Read fresh main before the next attempt.
 normal_race=('fetch first' in pushed.stdout or 'non-fast-forward' in pushed.stdout or
     ("cannot lock ref 'refs/heads/main': is at" in pushed.stdout and 'but expected' in pushed.stdout))
 if not normal_race:sys.exit(pushed.returncode)
raise SystemExit('Ordinary push race allocation ended; explicit file snapshot and source remain preserved')
