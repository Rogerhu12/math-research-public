#!/usr/bin/env python3
"""After the existing B chain completes, freeze it and run the exact norm pipeline sequentially."""
import argparse,gzip,hashlib,json,subprocess,sys,time
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True);args=p.parse_args()
    rolling=Path('/tmp/p41_poincare_miller_jets47_rolling.json.gz')
    complete=Path('/tmp/p41_poincare_miller_jets47_complete.json.gz');last=None
    while True:
        raw=rolling.read_bytes();data=json.loads(gzip.decompress(raw))
        if data['bits_done']!=last:
            last=data['bits_done'];print('PIPELINE WAIT',last,'bits',len(data['steps']),'steps',flush=True)
        if data['bits_done']==304 and 'actual_initial_fibre_Lie_gradient_mod47_cubed' in data:break
        del data,raw
        time.sleep(10)
    assert len(data['steps'])==454 and data['sign']==1
    complete.write_bytes(raw)
    print('COMPLETE B SNAPSHOT',len(raw),hashlib.sha256(raw).hexdigest(),'local',data['actual_hecke_local_log_initial_fibre'],flush=True)
    del raw,data
    prefix=[sys.executable,'-B'];folder=str(args.script_dir);runner=Path(__file__).parent
    commands=[
        ['/tmp/p41_miller_cm_prepared47.py','--script-dir',folder,'--miller',str(complete),'--output','/tmp/p41_miller_cm_prepared47_complete.json.gz'],
        ['/tmp/p41_miller_canonical_low47.py','--script-dir',folder,'--miller',str(complete),'--output','/tmp/p41_miller_canonical_low47_complete.json.gz'],
        ['/tmp/p41_miller_canonical_high47.py','--script-dir',folder,'--miller',str(complete),'--output','/tmp/p41_miller_canonical_high47_complete.json.gz'],
        ['/tmp/p41_canonical_high_endpoint47.py','--script-dir',folder,'--high-norms','/tmp/p41_miller_canonical_high47_complete.json.gz','--output','/tmp/p41_canonical_high_endpoint47_complete.json.gz'],
        ['/tmp/p41_miller_completion47.py','--script-dir',folder]]
    for command in commands:command[0]=str(runner/Path(command[0]).name)
    for command in commands:
        print('RUN',command[0],flush=True)
        subprocess.run(prefix+command,check=True)
    print('COMPLETE ACTUAL B MILLER AND ALL CM/CANONICAL NORMS',flush=True)

if __name__=='__main__':main()

