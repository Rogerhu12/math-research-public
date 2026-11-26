#!/usr/bin/env python3
"""Exercise actual Git pull/NFF/README-change paths using only local repos."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os,subprocess,sys,tempfile,time
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--supervisor',type=Path,default=Path(__file__).with_name('6a65-m12-frozen-source-rules-supervisor.py'))
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh actual Git integration receipt required')
    start=time.monotonic();spec=importlib.util.spec_from_file_location('checked_M12_rules_supervisor',args.supervisor)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    with tempfile.TemporaryDirectory(prefix='m12-local-rules-check-',dir=args.out.parent) as tmp:
        root=Path(tmp);remote=root/'origin.git';seed=root/'seed';worker=root/'worker';writer=root/'writer'
        env={k:v for k,v in os.environ.items() if k not in ('M12_RECOVERY_TOKEN','GITHUB_TOKEN','GH_TOKEN')}
        def git(where,*argv,check=True):
            result=subprocess.run(['git','-c','user.name=Local M12 test','-c','user.email=local@example.invalid',*argv],
                                  cwd=where,env=env,text=True,capture_output=True)
            if check and result.returncode:raise RuntimeError(result.stderr)
            return result
        git(root,'init','--bare','--initial-branch=main',str(remote));git(root,'init','--initial-branch=main',str(seed))
        (seed/mod.TOPIC).mkdir(parents=True);(seed/'README.md').write_text('Initial root rules\n')
        (seed/mod.TOPIC/'README.md').write_text('Initial topic rules\n')
        (seed/mod.HANDOFF).write_text('# Shared handoff\nInitial other prose\n')
        git(seed,'add','.');git(seed,'commit','-m','Initial local fixture')
        git(seed,'remote','add','origin',str(remote));git(seed,'push','-u','origin','main')
        for target in (worker,writer):git(root,'clone',str(remote),str(target))
        head=git(worker,'rev-parse','HEAD').stdout.strip()
        monitor=mod.RulesMonitor(worker,head,'local-check','1',root/'rules.json')
        monitor.env.pop('M12_RECOVERY_TOKEN',None)
        monitor.check_and_publish()
        original_git=monitor.git;injected=[False]
        def with_race(*argv,check=True):
            if argv[:1]==('push',) and not injected[0]:
                injected[0]=True;git(writer,'pull','--rebase','origin','main')
                path=writer/mod.HANDOFF
                path.write_text(path.read_text()+'<!-- independent-root-marker --> retained upstream prose\n')
                git(writer,'add',mod.HANDOFF);git(writer,'commit','-m','Concurrent unrelated HANDOFF marker')
                git(writer,'push','origin','main')
            return original_git(*argv,check=check)
        monitor.git=with_race;monitor.check_and_publish()
        upstream=git(root,'--git-dir',str(remote),'show','main:'+mod.HANDOFF).stdout
        if '<!-- independent-root-marker --> retained upstream prose' not in upstream or mod.MARKER not in upstream:
            raise ArithmeticError('NFF rebase lost shared HANDOFF content')
        if not any(e.get('push_exit',0)!=0 for e in monitor.events):raise ArithmeticError('NFF path was not actually exercised')
        git(writer,'pull','--rebase','origin','main')
        (writer/'README.md').write_text('Initial root rules\nA genuinely changed local test rule\n')
        git(writer,'add','README.md');git(writer,'commit','-m','Change local fixture root rule')
        git(writer,'push','origin','main');changed_head=git(writer,'rev-parse','HEAD').stdout.strip()
        read_before=monitor.last_read;caught=False
        try:monitor.check_and_publish()
        except mod.RulesChanged:caught=True
        if not caught or not monitor.changed or monitor.last_read!=read_before:
            raise ArithmeticError('README changed path was bypassed or marked read')
        if git(root,'--git-dir',str(remote),'rev-parse','main').stdout.strip()!=changed_head:
            raise ArithmeticError('A post-rule-change marker commit was published')
        if git(worker,'config','--get','credential.helper',check=False).returncode==0:
            raise ArithmeticError('Credential helper persisted into local Git config')
        child=subprocess.Popen([sys.executable,'-c','import time; time.sleep(30)'],start_new_session=True,env=env)
        mod.terminate(child)
        if child.poll() is None:raise ArithmeticError('Numerical process group termination failed')
        record={'schema':'6a65-M12-rules-supervisor-local-Git-check-v1','script_sha256':sha(__file__),
                'supervisor_sha256':sha(args.supervisor),'external_network_or_ref_writes':False,
                'actual_initial_literal_pull_and_marker_push':True,'actual_non_fast_forward_push_observed':True,
                'ordinary_pull_rebase_retry_then_push_succeeded':True,
                'upstream_other_HANDFOFF_prose_and_marker_preserved':True,
                'actual_root_README_change_detected_after_pull':True,
                'changed_rules_not_marked_read_or_published_over':True,
                'credentials_not_persisted_to_Git_config':True,
                'process_group_termination_exit':child.returncode,
                'literal_pull_events':len(monitor.events),'exit_code':0,
                'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
if __name__=='__main__':main()
