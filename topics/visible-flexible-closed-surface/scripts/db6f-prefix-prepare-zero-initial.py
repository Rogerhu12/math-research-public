#!/usr/bin/env python3
"""Prepare an UNSOLVED zero-shape initial guess for the unchanged original DN.

This script only writes input files. It never imports or starts a solver.
"""
import argparse
import gzip
import hashlib
import json
import math
import sys
from pathlib import Path


def read(path):
    p=Path(path);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path,data,compress=False):
    p=Path(path)
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(data,indent=None if compress else 2,allow_nan=False)+'\n').encode()
    if compress:raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000 or (not compress and len(raw)>1_000_000):
        raise ValueError('Output exceeds repository file limit')
    p.write_bytes(raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ['config','checkpoint','target-prefix','previous-launch','out-prefix','pilot-prefix']:
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();script=Path(__file__).resolve();repo=script.parents[3]
    cfg=read(args.config);old=read(args.checkpoint);cp=old['checkpoint'];p=cp['parameters']
    launch=read(args.previous_launch);prefix=read(args.target_prefix)
    if old['status']!='iteration-recovery-only' or old['iteration']['iteration']!=4:
        raise ValueError('Expected the closed interrupted iteration-4 input')
    if (p['modes'],p['quadrature'],p['physicalDepth'],p['shootingParts'],p['steps'],p['projectionFloor'])!=(15,256,12,8,32,.05):
        raise ValueError('Unexpected numerical problem')
    if cfg['solveTolerance']!=2e-9:raise ValueError('Original tolerance changed')
    height=cp['cutHeight'];goal=prefix['predicted_cut_height'];M=p['modes'];K=2*M
    if len(height)!=M or height[0]==0 or not all(math.isfinite(x) for x in height):
        raise ValueError('Nonzero finite physical request required for warm ratio')
    if any(height[j]!=goal[j]*(.25**(j+1)) for j in range(M)):
        raise ValueError('Input height is not the fixed s=.25 target')
    if len(cp['states'])!=865 or any(len(row)!=K for row in cp['states']):
        raise ValueError('Unexpected state shape')
    for item in launch['bound_files']:
        if sha(item['path'])!=item['sha256']:raise ValueError('Earlier source/input binding changed: '+item['path'])
    out=args.out_prefix.resolve();pilot=args.pilot_prefix.resolve()
    cp_path=Path(str(out)+'-input.json.gz');cfg_path=Path(str(out)+'-config.json')
    binding_path=Path(str(out)+'-launch.json');record_path=Path(str(out)+'-preparation.json')
    for f in [cp_path,cfg_path,binding_path,record_path]:
        if f.exists():raise FileExistsError(f)
    states=[[0.]*K for _ in cp['states']]
    zero_cp=dict(parameters=p,states=states,rawNode=cp['rawNode'],
        rawStates=[states[n].copy() for n in cp['rawNode']],cutHeight=height.copy(),
        scope='UNCONVERGED ZERO SHAPE INITIAL GUESS. cutHeight is the nonzero requested target label, not the zero state physical boundary height. The original cut residual is intentionally nonzero; no solved DN or geometric claim.')
    zero_record=dict(status='UNCONVERGED_ZERO_SHAPE_FIXED_NONZERO_TARGET',checkpoint=zero_cp,
        preparation_only=True,source_checkpoint=str(args.checkpoint.resolve()),source_checkpoint_sha256=sha(args.checkpoint),
        fixed_scale=.25,source_target_prefix=str(args.target_prefix.resolve()),source_target_prefix_sha256=sha(args.target_prefix),
        expected_initial_residual_from_zero_shape_identity=1,
        expectation_scope='Algebraic/source prediction only, not a recorded numerical evaluation.',
        actual_solver_runs=0)
    save(cp_path,zero_record,True)
    zero_config=dict(cfg)
    zero_config.update(initialCheckpoint=str(cp_path),correctInitialBoundary=False,maxIterations=8,
        traceFile=str(pilot)+'-trace.jsonl',iterationCheckpointFile=str(pilot)+'-iteration.json.gz',
        trialDiagnosticFile=str(pilot)+'-trials.jsonl',trialStatePrefix=str(pilot)+'-stage-input')
    save(cfg_path,zero_config)
    runner=script.with_name('db6f-prefix-tail-trial-run.py')
    source_root=repo/'topics/visible-flexible-closed-surface/repro/source-root'
    command=[sys.executable,str(runner),'--source-root',str(source_root),'--config',str(cfg_path),
        '--checkpoint',str(cp_path),'--out-prefix',str(pilot),'--max-iterations','8','--node-heap','1536']
    files={Path(row['path']).resolve() for row in launch['bound_files']}
    files.update([script,runner,cp_path,cfg_path,args.config.resolve(),args.checkpoint.resolve(),
                  args.target_prefix.resolve(),args.previous_launch.resolve()])
    bindings=[dict(path=str(f),sha256=sha(f),bytes=f.stat().st_size) for f in sorted(files)]
    binding=dict(status='PREPARED_ONLY_NO_SOLVER_STARTED',cwd=str(repo),command=command,
        stdout_log=str(pilot)+'-run.log',stderr='redirect to stdout_log',out_prefix=str(pilot),
        scope='Eight original Newton iterations from an explicitly unconverged zero-shape state at the identical nonzero s=.25 target. No source, metric, root/guard, RK, residual, or tolerance changes.',
        bound_files=bindings,projectionFloor=.05,solveTolerance=2e-9,maxIterations=8,
        correctInitialBoundary=False,requestHeightEqualsCheckpointTarget=True,
        zeroCheckpointCurrentPhysicalHeightIsZero=True,targetPhysicalHeightIsNonzero=True,
        requestedMeanSlots='Original worker appends zero initial means; background mean then evolves normally.',
        warmPipeline='last.jets.height is the nonzero target label, request is the same target, ratio=1; original remesh copies zeros and the exact JSON false disables linear boundary correction.',
        expectedInitialNormalizedResidual=1,expectedResidualIsNotMeasured=True,
        successRule='Only an original converged response meeting solveTolerance is a solved finite DN. Eight-iteration pilot completion or a smaller residual is not sufficient.')
    save(binding_path,binding)
    preparation=dict(status='INPUTS_PREPARED_NO_SOLVER_EXECUTED',generator_sha256=sha(script),
        command=[sys.executable,str(script),*sys.argv[1:]],
        inputs=[dict(path=str(f.resolve()),sha256=sha(f)) for f in [args.config,args.checkpoint,args.target_prefix,args.previous_launch]],
        outputs=[dict(path=str(f),sha256=sha(f),bytes=f.stat().st_size) for f in [cp_path,cfg_path,binding_path]],
        original_worker_or_controller_modified=False,actual_solver_runs=0)
    save(record_path,preparation)
    print(json.dumps(dict(prepared=True,checkpoint=str(cp_path),checkpoint_sha256=sha(cp_path),
        config=str(cfg_path),config_sha256=sha(cfg_path),launch=str(binding_path),launch_sha256=sha(binding_path),
        actual_solver_runs=0)),flush=True)


if __name__=='__main__':main()
