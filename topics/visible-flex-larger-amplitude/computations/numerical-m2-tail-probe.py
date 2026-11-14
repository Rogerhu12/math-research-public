#!/usr/bin/env python3
"""Actual nonlinear finite-tail continuation for a saved m=2 prefix.

Uses the physical height vector, including every retained prefix mode when
tail-modes is at least the prefix order. The default harmonic path is
H_j(lambda)=lambda**(j+1)*H_j(1). The optional uniform path is
H(lambda)=lambda*external_multiplier*H_prefix, preserving the complete
direction. An externally enlarged boundary is not a solved larger prefix.
Every solve remains nonlinear. A finite response does not establish an
infinite collar, a coupled prefix-tail solution, or a closed flexible surface.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,math,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
from scipy.interpolate import PPoly


def source_revision(source_topic):
    origin=source_topic/'source-origin.json'
    if origin.exists():
        record=json.loads(origin.read_text())
        return record['source_revision']
    return subprocess.check_output(['git','-C',str(source_topic),'rev-parse','HEAD'],text=True).strip()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','checkpoint','port','out-prefix'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--tail-modes',type=int);p.add_argument('--depth',type=int,default=8);p.add_argument('--steps',type=int,default=16);p.add_argument('--parts',type=int,default=4);p.add_argument('--quadrature',type=int,default=256)
    p.add_argument('--initial-scale',type=float,default=1/64);p.add_argument('--maximum-step',type=float,default=.125);p.add_argument('--minimum-step',type=float,default=1/4096)
    p.add_argument('--target-scale',type=float,default=1.,help='Stop at this exact homotopy scale; full-target success still requires scale one')
    p.add_argument('--homotopy',choices=['harmonic','uniform'],default='harmonic',help='Uniform preserves all relative physical boundary modes')
    p.add_argument('--height-multiplier',type=float,default=1.,help='External scalar multiplying the complete saved prefix boundary; requires uniform homotopy unless one')
    p.add_argument('--projection-floor',type=float,default=.05,help='Strictly positive numerical branch guard; no change to physical metric or equations')
    p.add_argument('--tol',type=float,default=2e-9);p.add_argument('--max-iterations',type=int,default=32);p.add_argument('--max-requests',type=int,default=60)
    p.add_argument('--node-heap',type=int,default=1536);p.add_argument('--backend',choices=['original','fourier','fourier-root'],default='fourier-root');p.add_argument('--predictor',choices=['linear','tangent'],default='tangent');p.add_argument('--initial-tail',type=Path);p.add_argument('--initial-tail-scale',type=float,default=0.)
    p.add_argument('--client',choices=['source','analytic-first'],default='source',help='Optional owned adapter replaces first slope and mean derivative rows only')
    a=p.parse_args();start=time.time()
    if a.quadrature<1 or a.quadrature&(a.quadrature-1):p.error('Physical reconstruction audit requires power-of-two angular quadrature')
    if not 0<a.projection_floor<1:p.error('Positive-branch projection floor must lie strictly between zero and one')
    if not 0<=a.initial_tail_scale<=a.target_scale<=1 or a.target_scale==0:p.error('Require 0 <= initial tail scale <= target scale <= 1, with positive target')
    if not math.isfinite(a.height_multiplier) or a.height_multiplier<=0:p.error('External height multiplier must be finite and positive')
    if a.height_multiplier!=1. and a.homotopy!='uniform':p.error('An external height multiplier requires the explicitly uniform full-vector path')
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    source_root=a.source_topic/'repro/source-root';sys.path.insert(0,str(source_root/'topics/large-amplitude-twist-flex/scripts'))
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(a.checkpoint)
    if not rec['solver_success']:raise ValueError('An actual successful finite prefix is required')
    prefixM=int(rec['config']['modes']);M=a.tail_modes or prefixM
    if not 1<=M<=64:raise ValueError('Tail order outside implemented range')
    if a.homotopy=='uniform' and M<prefixM:raise ValueError('Uniform direction probes must retain every prefix height mode')
    if rec['config']['base_mode']!=2:raise ValueError('This probe is for the complete m2 vector')
    pp=PPoly.construct_fast(np.array(rec['pp_coefficients']),np.array(rec['mesh']),extrapolate=True,axis=1)
    port=json.loads(a.port.read_text());sigma=math.copysign(1.,port['cut']['radius']-1.)
    Hfull=sigma*float(rec['gauge_amplitude'])*pp(float(rec['meridian_length']))[2*prefixM+1:]
    Hbase=np.zeros(M);Hbase[:min(M,prefixM)]=Hfull[:min(M,prefixM)]
    H=a.height_multiplier*Hbase
    def height_at(scale):
        return (Hbase*(a.height_multiplier*scale) if a.homotopy=='uniform'
                else H*scale**np.arange(1,M+1))
    path=lambda suffix:a.out_prefix.with_name(a.out_prefix.name+suffix)
    cfg={**port['parameters'],'modes':M,'spacing':2,'projectionFloor':a.projection_floor,'depth':a.depth,'steps':a.steps,'quadrature':a.quadrature,'linearFar':48,'linearSteps':512,'linearMethod':'projective','fastJacobian':True,'cuspAwareFlow':True,'actualCuspGrid':True,'shootingParts':a.parts,'solveTolerance':a.tol,'maxIterations':a.max_iterations,'auditSteps':a.steps,'correctInitialBoundary':True,'harmonicAmplitudePredictor':True,'traceFile':str(path('-trace.jsonl').resolve()),'iterationCheckpointFile':str(path('-iteration.json.gz').resolve()),'trialDiagnosticFile':str(path('-trials.jsonl').resolve())}
    if a.initial_tail:cfg['initialCheckpoint']=str(a.initial_tail.resolve())
    cfgfile=path('-config.json');cfgfile.write_text(json.dumps(cfg,indent=2)+'\n')
    os.environ['VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND']=a.backend;os.environ['VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND']=a.predictor
    clientpath=(Path(__file__).with_name('numerical-tail-analytic-client.py') if a.client=='analytic-first' else a.source_topic/'scripts/78718-prefix-tail-geometric-client.py')
    spec=importlib.util.spec_from_file_location('numerical_true_m2_tail',clientpath);client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
    report={'scope':__doc__,'source_git_head':source_revision(a.source_topic),'prefix_checkpoint':str(a.checkpoint),'prefix_checkpoint_sha256':hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),'initial_tail_checkpoint':str(a.initial_tail) if a.initial_tail else None,'initial_tail_checkpoint_sha256':hashlib.sha256(a.initial_tail.read_bytes()).hexdigest() if a.initial_tail else None,'initial_tail_scale':a.initial_tail_scale,'config_file':str(cfgfile),'full_prefix_target_height':Hfull.tolist(),'full_target_height':H.tolist(),'prefix_modes':prefixM,'complete_prefix_vector_used':M>=prefixM,'modes':M,'target_height_max':float(abs(H).max()),'client_implementation':a.client,'source_client_sha256':hashlib.sha256(clientpath.read_bytes()).hexdigest(),'rows':[],'target_reached':False}
    report.update(homotopy=a.homotopy,external_height_multiplier=a.height_multiplier,
                  boundary_direction='H_tail = sigma * q * saved_nonmean_height_at_cut',
                  prefix_radial_orientation=sigma,
                  uniform_target_is_externally_scaled_boundary=a.homotopy=='uniform' and a.height_multiplier!=1.,
                  target_reached_definition='Unscaled original prefix boundary only; requested_target_reached may refer to an explicitly external scaled direction.',
                  probe_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    report['requested_target_scale']=a.target_scale;report['requested_target_reached']=False
    tail=None;scale=a.initial_tail_scale;step=a.initial_scale;last=None
    def save():report['seconds']=time.time()-start;path('-summary.json').write_text(json.dumps(report,indent=2)+'\n')
    save()
    try:
        tail=client.WeightedTailPort(cfgfile,source_root,path('-response'),node_heap=a.node_heap)
        report['ready']=tail.ready;report['source_sha256']=tail.sources;save()
        print(json.dumps({'event':'ready','modes':M,'physical_depth':a.depth,'shooting_nodes':tail.ready['parameters']['depth']+1,'target_height_max':float(abs(H).max()),'backend':a.backend,'predictor':a.predictor}),flush=True)
        for request in range(a.max_requests):
            trial=min(a.target_scale,scale+step);height=height_at(trial);final=trial==a.target_scale;started=time.time()
            try:
                response=tail.solve(height,jacobian=final,audit=final);last=response
                row={'success':True,'scale':trial,'physical_height_max':float(abs(height).max()),'response_file':str(path('-response').with_name(path('-response').name+f'_{tail.calls:04d}.json.gz')),'residual':response['residual'],'iterations':len(response.get('history',[])),'cut_formal_curvature':response['jets'].get('formalCurvature'),'cut_slope_first':response['jets']['slope'][0],'seconds':time.time()-started}
                if a.homotopy=='uniform':row['external_multiplier']=a.height_multiplier*trial
                if final:row['audit']=response.get('audit');report['requested_target_reached']=True;report['target_reached']=trial==1. and a.height_multiplier==1.
                report['rows'].append(row);scale=trial;report['last_successful_scale']=scale;report['last_successful_response']=row['response_file'];save();print(json.dumps(row),flush=True)
                if final:break
                step=min(a.maximum_step,step*1.5,a.target_scale-scale)
            except Exception as exc:
                row={'success':False,'attempted_scale':trial,'last_successful_scale':scale,'step':step,'error':repr(exc),'seconds':time.time()-started};report['rows'].append(row);save();print(json.dumps(row),flush=True)
                step/=2
                if step<a.minimum_step:report['stopped_reason']='minimum homotopy step after actual failed nonlinear trials';break
        else:report['stopped_reason']=('audit requested initial physical height only' if a.max_requests==0 else 'maximum requested nonlinear homotopy trials')
        if not report['requested_target_reached'] and scale>0:
            try:
                final=tail.solve(height_at(scale),jacobian=True,audit=True)
                report['last_successful_scale_audit']={'scale':scale,'residual':final['residual'],'jets':final['jets'],'audit':final.get('audit'),'response_file':str(path('-response').with_name(path('-response').name+f'_{tail.calls:04d}.json.gz'))}
                if a.homotopy=='uniform':report['last_successful_scale_audit']['external_multiplier']=a.height_multiplier*scale
                report['last_successful_scale']=scale;report['last_successful_response']=report['last_successful_scale_audit']['response_file'];report['target_reached']=scale==1. and a.height_multiplier==1.
                report['requested_target_reached']=scale==a.target_scale
            except Exception as exc:report['last_audit_error']=repr(exc)
    except Exception as exc:report['error']=repr(exc);print(json.dumps({'event':'error','error':repr(exc)}),flush=True)
    finally:
        if tail:tail.close()
        save()
    print(json.dumps({'event':'done','target_reached':report['target_reached'],'requested_target_reached':report['requested_target_reached'],'last_successful_scale':report.get('last_successful_scale',0.),'seconds':report['seconds']}),flush=True)

if __name__=='__main__':main()
