"""Continue an actual finite GC iteration in naturally closed child batches.

This releases all process memory between batches. It preserves the same
declared equations/parameters and uses only an actually saved accepted state
as the next input. An observed SIGKILL after a newly saved accepted state can resume from that
entity; the signal remains recorded and the chain returns a nonzero status.
Other failed/no-progress children stop. No convergence label is inferred.
"""
import argparse,datetime,hashlib,json,subprocess,sys,time
from pathlib import Path


def identity(path):
    p=Path(path);data=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--driver',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--warm-start',type=Path,required=True)
    ap.add_argument('--radius-packet',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--owner-stop-file',type=Path,required=True)
    ap.add_argument('--blocks',type=int,default=8)
    ap.add_argument('--iterations-per-block',type=int,default=1)
    ap.add_argument('--modes',type=int,default=15)
    args=ap.parse_args();start=time.monotonic();stem=args.out_prefix
    if args.blocks<1 or args.iterations_per_block<1:raise ValueError('Positive batch counts required')
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a unique chain stem')
    stem.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-natural-finite-GC-batch-chain-recover-accepted-v3',source=identity(__file__),
        driver=identity(args.driver),candidate=identity(args.candidate),initial_input=identity(args.warm_start),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        settings={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        batches=[],actual_accepted_steps=0,completed=False,finite_success=False,
        strong_target_completed=False,stop_reason=None)
    destination=stem.with_name(stem.name+'-chain-report.json')
    def save():
        report['seconds']=time.monotonic()-start
        destination.write_text(json.dumps(report,indent=2)+'\n')
    warm=args.warm_start;save();returncode=0
    for index in range(args.blocks):
        if args.owner_stop_file.exists():
            report['stop_reason']='Owner stop observed between naturally closed batches';returncode=130;break
        child=stem.with_name(stem.name+'-b%04d'%(index+1))
        receipt=child.with_name(child.name+'-process-receipt.json')
        argv=[sys.executable,'-u',str(Path(__file__).parent/'fd2d-run-monitored-command-v2.py'),
            '--receipt',str(receipt),'--',sys.executable,'-u',str(args.driver),
            '--candidate',str(args.candidate),'--warm-start',str(warm),
            '--radius-packet',str(args.radius_packet),'--out-prefix',str(child),
            '--owner-stop-file',str(args.owner_stop_file),
            '--max-iterations',str(args.iterations_per_block),'--modes',str(args.modes)]
        batch_start=time.monotonic();observed=subprocess.run(argv,check=False)
        entry=dict(index=index+1,stem=str(child),input=identity(warm),
            actual_wrapper_returncode=observed.returncode,seconds=time.monotonic()-batch_start)
        if receipt.exists():entry['actual_process_receipt']=identity(receipt)
        rp=child.with_name(child.name+'-report.json')
        if rp.exists():
            actual=json.loads(rp.read_text());entry['driver_report']=identity(rp)
            entry['actual_accepted_steps']=actual.get('accepted_steps',0)
            entry['completed']=actual.get('completed',False)
            entry['finite_success']=actual.get('finite_success',False)
            entry['last_diagnostics']=actual.get('final',actual.get('latest',actual.get('initial')))
            if 'latest_checkpoint' in actual:
                entity=Path(actual['latest_checkpoint']['path'])
                bound=identity(entity)
                if bound['sha256']!=actual['latest_checkpoint']['sha256']:
                    raise ValueError('Actual saved accepted entity no longer matches its report')
                entry['latest_checkpoint']=bound
            report['actual_accepted_steps']+=entry['actual_accepted_steps']
        if 'latest_checkpoint' in entry:
            report['latest_checkpoint']=entry['latest_checkpoint']
        report['batches'].append(entry);save()
        print(json.dumps(dict(event='closed_batch',index=index+1,returncode=observed.returncode,
            accepted=entry.get('actual_accepted_steps',0),seconds=entry['seconds'],
            latest=entry.get('latest_checkpoint'))),flush=True)
        if observed.returncode!=0:
            process=json.loads(receipt.read_text()) if receipt.exists() else {}
            if process.get('actual_child_returncode')==-9 and entry.get('actual_accepted_steps',0)>0 and 'latest_checkpoint' in entry:
                entry['continued_from_actual_accepted_after_observed_SIGKILL']=True
                report.setdefault('recorded_interrupted_children',[]).append(index+1)
                warm=Path(entry['latest_checkpoint']['path'])
                returncode=137
                save()
                continue
            report['stop_reason']='A child returned nonzero without an eligible newly accepted signal checkpoint; owner diagnosis required'
            returncode=observed.returncode;break
        if entry.get('finite_success'):
            report['finite_success']=True;report['stop_reason']='Finite driver tolerance reached; strong-target obligations are separate';break
        if not entry.get('actual_accepted_steps') or 'latest_checkpoint' not in entry:
            report['stop_reason']='No new complete accepted state in this batch; owner can inspect the true finite failure';break
        warm=Path(entry['latest_checkpoint']['path']);report['latest_checkpoint']=entry['latest_checkpoint'];save()
    else:report['stop_reason']='Requested finite batches naturally closed; next actual state is ready for autonomous continuation'
    report['completed']=True;save()
    return returncode


if __name__=='__main__':raise SystemExit(main())
