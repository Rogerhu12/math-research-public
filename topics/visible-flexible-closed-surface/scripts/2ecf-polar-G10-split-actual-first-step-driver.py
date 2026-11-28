#!/usr/bin/env python3
"""Wait for actual source exits, pay all dense baselines, run the first step.

This driver never promotes a partial cache or an old quadrature cost.  Every
scientific subprocess has a separate natural OS exit and cost receipt.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import json
import hashlib
from pathlib import Path
import resource
import subprocess
import time

W=Path(__file__).resolve().parent
S=Path('/workspace/scratch/2ecfcd6930d6/math-research-public/topics/visible-flexible-closed-surface/scripts')


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(command,prefix):
    prefix=W/prefix;start=time.monotonic()
    log=Path(str(prefix)+'.log');exitfile=Path(str(prefix)+'-exit.json')
    if log.exists() or exitfile.exists():raise FileExistsError('Fresh actual subprocess receipt required')
    with log.open('x') as output:
        p=subprocess.Popen(list(map(str,command)),stdout=output,stderr=subprocess.STDOUT)
        (W/'polar-G10-split-actual-driver-live.json').write_text(json.dumps(dict(pid=p.pid,command=list(map(str,command)),prefix=str(prefix))))
        code=p.wait()
    receipt=dict(returncode=code,seconds=time.monotonic()-start,
        peakChildRSSKiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        command=list(map(str,command)),peakRSSIsCumulativeChildMaximum=True)
    exitfile.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(event='actual_dense_subprocess_exit',prefix=str(prefix),**receipt)),flush=True)
    if code!=0:raise RuntimeError('Actual dense subprocess failed: '+str(prefix))
    return receipt


start=time.monotonic()
for group in ('polar-c2-G10r-training','polar-c2-G10s-chunk502-610','polar-c2-G10s-chunk610-753'):
    path=W/(group+'-source-exit.json')
    while not path.exists():time.sleep(5)
    receipt=json.loads(path.read_text())
    if receipt['returncode']!=0:raise RuntimeError('Incomplete actual source group: '+group)
print(json.dumps(dict(event='both_actual_dense_sources_exited_zero',waitSeconds=time.monotonic()-start)),flush=True)
prepare=W/'2ecf-polar-c2-g10-split-prepare.py'
prepared=W/'polar-c2-G10s-prepared.json'
run(['python3','-u',prepare,'assemble','--scripts',S,'--parent-prepared',W/'polar-c2-extended-prepared.json',
    '--third-observer',W/'polar-independent-G3-shifted256-independent.json','--prefix',W/'polar-c2-G10s',
    '--candidate',S.parent/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json',
    '--target-definition',W/'target-zero.json','--ramp-master',W/'gap105-prefix-ramp-master.npz',
    '--coast-master',W/'gap105-prefix-coast-master.npz',
    '--completed-training-prefix',W/'polar-c2-G10r-training',
    '--failed-observer-prefix',W/'polar-c2-G10r-observer',
    '--chunk-prefixes',W/'polar-c2-G10s-chunk502-610',W/'polar-c2-G10s-chunk610-753'],
    'polar-c2-G10s-assemble')
solver=W/'2ecf-polar-c2-g10-solve.py'
base=['python3','-u',solver,'--scripts',S,'--prepare-entry',prepare,'--prepared',prepared]
candidates=[('warm03',W/'polar-c2-step03-step01-state.json'),
    ('warm02',W/'polar-c2-step02-step01-state.json'),
    ('zero06',W/'polar-c2-zero-step06-step01-state.json'),('zero00',None)]
baselines=[]
for label,parent in candidates:
    prefix='polar-G10s-baseline-'+label
    command=base+['--prefix',W/prefix,'--steps','0']+(['--zero'] if parent is None else ['--warm-state',parent])
    receipt=run(command,prefix)
    path=W/(prefix+'-initial.json');state=json.loads(path.read_text());v=state['evaluation']
    baselines.append(dict(label=label,baseline=str(path),baselineSHA256=sha(path),
        parentStateSHA256=None if parent is None else sha(parent),
        ownNewAcceptedSteps=state['ownExtendedAcceptedSteps'],ownNewAttempts=state['ownExtendedAttempts'],
        squaredNorm=v['squaredNorm'],metric=v['maxRelativeMetric'],curvature=v['maxCurvature'],
        sigma=v['areaBarrierStatistics']['minAreaRatio'],areaSquaredNorm=v['areaBarrierStatistics']['squaredNorm'],
        actualExit=receipt))
best=min(baselines,key=lambda x:x['squaredNorm'])
selection=dict(schema='2ecf-actual-G10-complete-two-grid-parent-selection-v1',preparedSHA256=sha(prepared),
    actualRows=json.loads(Path(best['baseline']).read_text())['evaluation']['rowCount'],
    baselines=baselines,selected=best,rule='smallest actual complete G10 original14-row squared norm',
    old205OrThirdObserverCostBorrowed=False,sourceAndMetricFixed=True,selectionPerformedNoAccepts=True)
path=W/'polar-G10s-actual-baseline-selection.json'
if path.exists():raise FileExistsError('Fresh selection required')
path.write_text(json.dumps(selection,separators=(',',':'),allow_nan=False)+'\n')
print(json.dumps(dict(event='actual_dense_parent_selected',selected=best,selectionSHA256=sha(path))),flush=True)
run(base+['--state',best['baseline'],'--prefix',W/'polar-G10s-step01','--steps','1'],'polar-G10s-step01')
state=W/'polar-G10s-step01-step01-state.json'
observer=W/'polar-independent-G11r-shifted256-independent.json'
observer_exit=W/'polar-independent-G11r-cache-exit.json'
if observer.exists() and observer_exit.exists() and json.loads(observer_exit.read_text())['returncode']==0:
    run(['python3','-u',W/'2ecf-polar-c2-independent-g11-resume-observe.py','observe','--scripts',S,
        '--prepare-entry',prepare,'--prepared',prepared,'--state',state,'--observer',observer,
        '--output',W/'polar-G11r-G10s-step01.json'],'polar-G11r-G10s-step01')
print(json.dumps(dict(event='actual_dense_first_step_driver_complete',stateSHA256=sha(state))),flush=True)
