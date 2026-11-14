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
args=parser.parse_args()
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
 body=''.join(mode+' '+kind+' '+sha+'\t'+name+'\0' for name,(mode,kind,sha) in entries.items())
 # Unchanged blobs are guaranteed by the fresh main tree, and owned blobs by
 # the saved reachable commit. --missing supports the required partial clone.
 return run(['git','mktree','--missing','-z'],input=body).stdout.strip()
for attempt in range(1,args.attempts+1):
 t=time.monotonic();pull=run(['git','pull','--ff-only','--no-stat','origin','main'],check=False)
 base=run(['git','rev-parse','origin/main']).stdout.strip()
 diff=run(['git','diff',old,base,'--','README.md','topics/visible-flexible-closed-surface/README.md']).stdout
 print(json.dumps(dict(attempt=attempt,pull_exit=pull.returncode,readme_previous=old,readme_current=base,readme_diff_empty=not bool(diff))),flush=True)
 if diff:print(diff,flush=True);sys.exit(78)
 if pull.returncode:print(pull.stdout,flush=True);sys.exit(pull.returncode)
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
 now=datetime.datetime.now(datetime.timezone.utc);a=handoff.index('## 2.');b=handoff.index('## 3.');part=handoff[a:b]
 part=re.sub(r'`[0-9a-f]{40}`（[0-9-]{10} [0-9:]+ UTC）',f'`{base}`（{now:%Y-%m-%d %H:%M} UTC）',part,count=1)
 part=re.sub(r'相对已读[^\n]+两README无差异。',f'相对已读{old}两README无差异。',part,count=1)
 part=re.sub(r'下次不晚于[0-9:]+ UTC。',f'下次不晚于{now+datetime.timedelta(hours=1):%H:%M} UTC。',part,count=1)
 h=handoff[:a]+part+handoff[b:];assert len(h.encode())<10000;old=base
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
 print(json.dumps(dict(attempt=attempt,tree_ready_seconds=time.monotonic()-t,commit=commit)),flush=True)
 pushed=run(['git','push','origin',commit+':refs/heads/main'],check=False)
 print(json.dumps(dict(attempt=attempt,push_exit=pushed.returncode,message=pushed.stdout,seconds=time.monotonic()-t)),flush=True)
 if pushed.returncode==0:
  run(['git','reset','--hard',commit])
  args.receipt.write_text(json.dumps(dict(commit=commit,rules_read_sha=base,attempt=attempt,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='ordinary terminal git push; fresh main parent; unchanged remote tree plus exact owned path overlay'),indent=2)+'\n')
  sys.exit(0)
 if 'fetch first' not in pushed.stdout and 'non-fast-forward' not in pushed.stdout:sys.exit(pushed.returncode)
raise SystemExit('Ordinary push race allocation ended; explicit file snapshot and source remain preserved')
