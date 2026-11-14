#!/usr/bin/env python3
"""Finite alternating low46 and high13 reads of the same existing field.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This orchestration changes no source, domain, kernel, or mathematical gate.
Every owned child has an individual true wait4 resource record.
"""
import argparse,gzip,hashlib,json,subprocess,sys,time
from pathlib import Path


def read(p):
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def update(command,changes):
    out=command[:]
    for key,value in changes.items():
        key='--'+key
        if key in out:out[out.index(key)+1]=str(value)
        else:out.extend([key,str(value)])
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--cycles',type=int,default=4)
    p.add_argument('--steps',type=int,default=8)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Preserve every alternating certificate')
    if not 1<=a.cycles<=16 or not 1<=a.steps<=64:raise ValueError('Declared finite substitution counts required')
    low_resource=a.work/'inner-restricted-expanded-low46-r1-resource.json'
    high_resource=a.work/'inner-restricted-expanded-window13-low46-r3-resource.json'
    low_command=read(low_resource)['command'];high_command=read(high_resource)['command']
    if read(low_resource)['exitcode'] or read(high_resource)['exitcode']:raise ArithmeticError('Formal original finite bounds required')
    low=a.work/'inner-restricted-expanded-low46-r1.json.gz'
    high=a.work/'inner-restricted-expanded-window13-low46-r3.json.gz'
    wrapper=a.work/'strong_resource_run.py';records=[]
    for cycle in range(1,a.cycles+1):
        lp=a.work/f'inner-restricted-alternate{cycle}-low46'
        hp=a.work/f'inner-restricted-alternate{cycle}-window13'
        lr=Path(str(lp)+'-resource.json');hr=Path(str(hp)+'-resource.json')
        lcmd=update(low_command,dict(window_field=high)) if False else update(low_command,{'window-field':high,'window-resource':high_resource,'previous-low-field':low,'previous-low-resource':low_resource,'out-prefix':lp,'steps':a.steps})
        for label,command,res in [('low46',lcmd,lr)]:
            proc=subprocess.run([sys.executable,str(wrapper),'--out',str(res),'--']+command)
            if proc.returncode:raise RuntimeError('Actual alternating child failed: '+label)
        low=Path(str(lp)+'.json.gz');low_resource=lr
        hcmd=update(high_command,{'previous-window-primary':high,'previous-window-resource':high_resource,'low-mode-field':low,'low-mode-resource':low_resource,'out-prefix':hp,'steps':a.steps})
        proc=subprocess.run([sys.executable,str(wrapper),'--out',str(hr),'--']+hcmd)
        if proc.returncode:raise RuntimeError('Actual alternating high child failed')
        high=Path(str(hp)+'.json.gz');high_resource=hr
        x=read(high)
        row=dict(cycle=cycle,low=dict(path=str(low),sha256=sha(low)),low_resource=dict(path=str(lr),sha256=sha(lr)),
                 high=dict(path=str(high),sha256=sha(high)),high_resource=dict(path=str(hr),sha256=sha(hr)),
                 actual_R100_head_band_masses=x['actual_R100_head_band_masses'],actual_R100_head_window_masses=x['actual_R100_head_window_masses'])
        records.append(row)
        print(json.dumps(dict(event='complete_alternating_cycle',**row,elapsed_seconds=time.monotonic()-start)),flush=True)
    result=dict(schema='same-R100-restricted-finite-alternating-low46-window13-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
      all_gates=True,source_sha256=sha(Path(__file__)),domain=read(high)['domain'],cycles=a.cycles,steps_per_child=a.steps,
      completed=records,new_fixedpoint_claimed=False,complete_mean_inverse_far_and_infinite=True,elapsed_seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(path=str(a.out),sha256=sha(a.out),complete_cycles=a.cycles)))


if __name__=='__main__':main()
