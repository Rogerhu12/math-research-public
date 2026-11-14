from pathlib import Path
import subprocess,os,json,shutil,tempfile,hashlib
BASE=Path('/tmp/fd2d-ci-static-20261112')
TOPIC='topics/visible-flexible-closed-surface'
def command(argv,cwd,env=None,check=True):
 r=subprocess.run(argv,cwd=cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 if check and r.returncode:raise RuntimeError((argv,r.returncode,r.stdout[-3000:]))
 return r

def fixture(label,case):
 root=Path(tempfile.mkdtemp(prefix='fd2d-ci-fixture-'+label+'-',dir='/tmp'))
 remote=root/'remote.git';work=root/'work';human=root/'human'
 command(['git','init','--bare','--initial-branch=main',str(remote)],root)
 command(['git','clone',str(remote),str(work)],root)
 command(['git','config','user.email','fixture@example.invalid'],work)
 command(['git','config','user.name','Fixture'],work)
 topic=work/TOPIC;(topic/'notes').mkdir(parents=True);(topic/'scripts').mkdir()
 (work/'README.md').write_text('root rules v1\n')
 (topic/'README.md').write_text('topic rules v1\n')
 (topic/'HANDOFF.md').write_text('# H\nHuman base stays.\n')
 (topic/'log.md').write_text('# Topic log\n')
 (work/'LOG.md').write_text('# Root log\n')
 for name in ('fd2d_ci_run_recovery.py','fd2d_ci_publish_recovery.py'):
  shutil.copyfile(BASE/name,topic/'scripts'/name)
 command(['git','add','.'],work);command(['git','commit','-m','fixture input'],work)
 command(['git','push','origin','main'],work)
 baseline=command(['git','rev-parse','HEAD'],work).stdout.strip()
 create="from pathlib import Path; import sys,json; p=sys.argv[1]; Path(p+'-accepted-0001.json').write_text('old'); Path(p+'-accepted-0002.json').write_text('z'*1100001); Path(p+'-progress.json').write_text(json.dumps({'state':'actual'})); print('actual fixture console')"
 commands=[{'name':'actual-fixture','argv':['python','-c',create,'{prefix}']}]
 if case=='rules':
  commands=[{'name':'fails-seven','argv':['python','-c','print("actual failure"); raise SystemExit(7)']},
            {'name':'must-not-run','argv':['python','-c','from pathlib import Path; Path("notes/SHOULD_NOT_EXIST").write_text("bad")']}]
 req={'rules_read_sha':baseline,'run_prefix':'fixture-'+label,'commands':commands}
 request=topic/'notes/fd2d-ci-request.json';request.write_text(json.dumps(req))
 command(['git','add',str(request.relative_to(work))],work);command(['git','commit','-m','fixture request'],work);command(['git','push','origin','main'],work)
 env=os.environ.copy();env.update(GITHUB_RUN_ID='900'+label,GITHUB_RUN_ATTEMPT='1')
 result=command(['python',TOPIC+'/scripts/fd2d_ci_run_recovery.py','--request',TOPIC+'/notes/fd2d-ci-request.json'],work,env,False)
 expected=7 if case=='rules' else 0
 if result.returncode!=expected:raise RuntimeError(('run wrong',result.returncode,result.stdout[-6000:]))
 prefix='fixture-'+label+'-900'+label+'-a1'
 report=json.loads((topic/'notes'/(prefix+'-batch-report.json')).read_text())
 if case=='rules':
  assert len(report['commands'])==1 and not (topic/'notes/SHOULD_NOT_EXIST').exists()
 else:
  manifest=json.loads((topic/'notes'/(prefix+'-publish-manifest.json')).read_text())
  assert not any('accepted-0001' in p for p in manifest['paths'])
  assert any('accepted-0002.json.gz' in p for p in manifest['paths'])
 if case in ('conflict','rules'):
  command(['git','clone',str(remote),str(human)],root)
  command(['git','config','user.email','human@example.invalid'],human)
  command(['git','config','user.name','Other human'],human)
  if case=='conflict':
   for name in ('LOG.md',TOPIC+'/HANDOFF.md'):
    with (human/name).open('a') as f:f.write('OTHER HUMAN WORDS MUST SURVIVE\n')
  else:
   with (human/'README.md').open('a') as f:f.write('new rule v2 must be read\n')
  command(['git','add','.'],human);command(['git','commit','-m','independent human change'],human);command(['git','push','origin','main'],human)
  remote_before=command(['git','rev-parse','HEAD'],human).stdout.strip()
 publish=command(['python',TOPIC+'/scripts/fd2d_ci_publish_recovery.py','--request',TOPIC+'/notes/fd2d-ci-request.json'],work,env,False)
 expected_publish=78 if case=='rules' else 0
 if publish.returncode!=expected_publish:
  raise RuntimeError(('publish wrong',case,publish.returncode,publish.stdout[-9000:]))
 remote_head=command(['git','rev-parse','refs/heads/main'],remote).stdout.strip()
 if case=='rules':assert remote_head==remote_before
 if case=='conflict':
  for name in ('LOG.md',TOPIC+'/HANDOFF.md'):
   content=command(['git','show','main:'+name],remote).stdout
   assert 'OTHER HUMAN WORDS MUST SURVIVE' in content
 status=json.loads((topic/'notes'/(prefix+'-publish-status.json')).read_text())
 return dict(case=case,path=str(root),run_code=result.returncode,publish_code=publish.returncode,
   phase=status['phase'],report_process_exit=report['process_exit_code'],remote_head=remote_head,
   source_blob_run=hashlib.sha1(b'blob '+str((BASE/'fd2d_ci_run_recovery.py').stat().st_size).encode()+b'\0'+(BASE/'fd2d_ci_run_recovery.py').read_bytes()).hexdigest())
rows=[]
for label,case in [('1','normal'),('2','conflict'),('3','rules')]:
 row=fixture(label,case);rows.append(row);print(json.dumps(row),flush=True)
(BASE/'fixture-report.json').write_text(json.dumps(rows,indent=2)+'\n')
