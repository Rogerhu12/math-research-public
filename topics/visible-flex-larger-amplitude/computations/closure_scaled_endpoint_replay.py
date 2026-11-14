#!/usr/bin/env python3
"""Same-new-g physical-depth refinement with actual endpoint log diagnostics.

The worker solves the unchanged complete finite nonlinear equations. Its
recorded far-to-endpoint map is LINEAR and remains labelled as such. This
driver does not infer exact shallow matching from an amplitude margin.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import time


def load(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),raw


def cut_jet_norm_comparison(a,b,spacing):
    """Floating coefficient bounds in the common physical polar metric."""
    for field in ['radius','E','Ep','backgroundSlope','backgroundSecond']:
        if a.get(field)!=b.get(field):
            raise ValueError('The common cut background changed: '+field)
    r,E,Ep=a['radius'],a['E'],a['Ep']
    M=max(len(a['height']),len(b['height']))
    def differences(field):
        left=a[field]+[0.]*(M-len(a[field]))
        right=b[field]+[0.]*(M-len(b[field]))
        return [y-x for x,y in zip(left,right)]
    dh,dk,dkr=[differences(field) for field in ['height','slope','second']]
    k0=b['meanSlopeCorrection']-a['meanSlopeCorrection']
    kr0=b['meanSecondCorrection']-a['meanSecondCorrection']
    m=[spacing*(j+1) for j in range(M)]
    h_l1=sum(map(abs,dh))
    radial_grad=(abs(k0)+sum(map(abs,dk)))/math.sqrt(E)
    angular_grad=sum(n*abs(h) for n,h in zip(m,dh))/r
    hrr=(abs(kr0-Ep*k0/(2*E))+
         sum(abs(v-Ep*u/(2*E)) for u,v in zip(dk,dkr)))/E
    hrt=sum(n*abs(u-h/r) for n,h,u in zip(m,dh,dk))/(r*math.sqrt(E))
    htt=(abs(r*k0/E)+sum(abs(-n*n*h+r*u/E) for n,h,u in zip(m,dh,dk)))/(r*r)
    return dict(nonmean_height_l1=h_l1,
                physical_gradient_l2_upper=math.hypot(radial_grad,angular_grad),
                covariant_Hessian_Frobenius_upper=math.sqrt(hrr*hrr+2*hrt*hrt+htt*htt),
                gradient_components=[radial_grad,angular_grad],
                Hessian_components=[hrr,hrt,htt],
                mean_slope_correction_change=k0,mean_second_correction_change=kr0,
                scope='Floating Fourier-l1 bounds on the complete two saved finite spectra, including newly added modes. No source evaluation, floating rounding or missing exact radial-solution error is enclosed.')


def endpoint_diagnostic(ready,response):
    bridge=ready['deepLinearBridge']
    cp=response.get('checkpoint')
    if not cp:return None
    raw=cp['rawStates'][-1];M=cp['parameters']['modes']
    p=ready['rationalDeepModel']['physicalParameters']
    far=bridge['farPhysicalNode'];F=bridge['farMathematicalPort']
    rc=p['rCuff'];eps=p['epsilonScale'];ld=math.log(.006)-F*math.log(2)
    tau=math.log(2)/4
    rows=[]
    canonical=response.get('endpointCanonicalTrace')
    for j,g in enumerate(bridge['endpoint']['rows']):
        q,pi=raw[j],raw[M+j]
        xi=None if canonical is None else canonical['canonicalXi'][j]
        log2z=None
        if q:
            logQfar=math.log(abs(q))-g['logAbsoluteQGain']
            log2z=(10*math.log(rc)+logQfar-math.log(eps)-5.5*ld+g['mode']*tau)/math.log(2)
        rows.append(dict(mode=g['mode'],actual_endpoint_Q=q,
                         actual_endpoint_connection_momentum=pi,
                         actual_endpoint_linear_canonical_Xi=xi,
                         connection_minus_canonical=None if xi is None else pi-xi,
                         far_to_endpoint_log_Q_gain=g['logAbsoluteQGain'],
                         endpoint_linear_slope=g['rawSlope'],
                         endpoint_connection_boundary_residual=pi-g['rawSlope']*q,
                         endpoint_canonical_boundary_residual=None if xi is None else xi-g['rawSlope']*q,
                         log2_abs_z_from_linear_continuation=log2z))
    logs=[x['log2_abs_z_from_linear_continuation'] for x in rows
          if x['log2_abs_z_from_linear_continuation'] is not None]
    norm=None
    if logs:
        top=max(logs);norm=top+math.log2(sum(2**(x-top) for x in logs))
    strips=[]
    for strip in [tau,1.,8.,80.,96.,128.]:
        wide=[x['log2_abs_z_from_linear_continuation']+
              x['mode']*(strip-tau)/math.log(2) for x in rows
              if x['log2_abs_z_from_linear_continuation'] is not None]
        value=None
        if wide:
            top=max(wide);value=top+math.log2(sum(2**(x-top) for x in wide))
        strips.append(dict(tau_F=strip,retained_modes=M,
            log2_low_height_l1=value,
            numerical_margin_to_trace_domain=None if value is None else -1947-value))
    return dict(status='ACTUAL nonlinear endpoint, followed by an UNVERIFIED linear continuation',
                physical_depth=bridge['nonlinearPhysicalDepth'],
                far_physical_node=far,far_mathematical_port=F,tau_F=tau,rows=rows,
                log2_low_height_l1=norm,
                numerical_margin_to_trace_domain=None if norm is None else -1947-norm,
                numerical_margin_to_Robin_envelope=None if norm is None else -2048-norm,
                strip_diagnostics=strips,
                canonical_coordinate_conversion_available=canonical is not None,
                limits=['No omitted nonlinear flow or radial integration error is enclosed here.',
                        'Only retained finite modes enter these linear label diagnostics; unrepresented low modes through 46 are not bounded by this report.',
                        'No unrepresented Fourier mode is declared zero in the exact problem.',
                        'R18 applies only after a true trace inclusion and its complete residual are controlled.'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--depth',type=int,default=12)
    p.add_argument('--modes',type=int)
    p.add_argument('--steps',type=int)
    p.add_argument('--quadrature',type=int)
    p.add_argument('--linear-far',type=int,default=225)
    p.add_argument('--linear-steps',type=int)
    p.add_argument('--node-heap',type=int,default=768)
    args=p.parse_args()
    prior,input_bytes=load(args.input)
    oldmodel=prior.get('ready',{}).get('rationalDeepModel')
    if not oldmodel or oldmodel['definition']!='visible-larger-rational-deep-alpha-v1':
        raise ValueError('A completed explicitly new-g response is required')
    cfg=dict(prior['config'])
    if args.depth<cfg['depth']:
        raise ValueError('This refinement must not shorten the nonlinear physical depth')
    height=list(prior['request']['height'])
    old_modes=cfg['modes']
    modes=old_modes if args.modes is None else args.modes
    if not (old_modes<=modes<=46):
        raise ValueError('This R18 low-height diagnostic requires nondecreasing modes, at most 46')
    if len(height)!=old_modes:
        raise ValueError('The prior request does not contain its complete saved height vector')
    quadrature=cfg['quadrature'] if args.quadrature is None else args.quadrature
    steps=cfg['steps'] if args.steps is None else args.steps
    if quadrature<cfg['quadrature'] or steps<cfg['steps']:
        raise ValueError('Radial and angular refinement must not coarsen the saved resolution')
    if args.depth!=cfg['depth'] and (modes!=old_modes or quadrature!=cfg['quadrature']):
        raise ValueError('Refine physical depth first; angular Q/L prolongation needs equal depths')
    # This retains exactly the same finite polynomial Dirichlet function.
    # New nonlinear momentum coefficients are prepared by the source Q/L map.
    height.extend([0.0]*(modes-old_modes))
    pre=args.out_prefix.resolve()
    paths={name:Path(str(pre)+suffix) for name,suffix in [
        ('config','-config.json'),('response','-response.json.gz'),
        ('summary','-summary.json'),('trace','-trace.jsonl'),('ready','-ready.json'),
        ('iteration','-iteration-recovery.json.gz'),('trials','-trials.jsonl')]}
    if any(x.exists() for x in paths.values()):
        raise FileExistsError('Use a fresh output prefix')
    pre.parent.mkdir(parents=True,exist_ok=True)
    for k in ['traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix','initialCheckpoint']:
        cfg.pop(k,None)
    cfg.update(initialCheckpoint=str(args.input.resolve()),depth=args.depth,modes=modes,
               quadrature=quadrature,steps=steps,
               auditSteps=max(cfg.get('auditSteps',0),steps),
               linearFar=args.linear_far,traceFile=str(paths['trace']),
               iterationCheckpointFile=str(paths['iteration']),trialDiagnosticFile=str(paths['trials']),
               rationalPointCacheLimit=96,rationalFrozenWarpAlpha=oldmodel['frozenWarpAlpha'])
    if args.linear_steps is not None:cfg['linearSteps']=args.linear_steps
    paths['config'].write_text(json.dumps(cfg,indent=2)+'\n')
    topic=args.source_topic.resolve();root=topic/'repro/source-root'
    env=dict(os.environ,VISIBLE_FLEX_SOURCE_TOPIC=str(topic),VISIBLE_FLEX_SOURCE_ROOT=str(root),
             CLOSING_TAIL_CACHE=str(root/'topics/large-amplitude-twist-flex/scripts'),
             VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',
             NODE_OPTIONS=f'--max-old-space-size={args.node_heap}')
    worker=Path(__file__).with_name('closure_scaled_endpoint_worker.mjs')
    hashes={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),worker]}
    started=time.monotonic()
    proc=subprocess.Popen(['node','--expose-gc',str(worker),str(paths['config'])],stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
    try:
        line=proc.stdout.readline()
        if not line:
            raise RuntimeError(f'Worker initialization failed: exit {proc.wait()}')
        ready=json.loads(line)
        paths['ready'].write_text(json.dumps(ready,indent=2)+'\n')
        if ready.get('endpointJacobianAdapter',{}).get('name')!='closure-scaled-endpoint-worker-v1':
            raise RuntimeError('Wrong scaled-endpoint worker')
        model=ready['rationalDeepModel']
        fields=['definition','start','deepAlpha','exactSourceConstants','frozenWarpAlpha','headFingerprint']
        mismatch=[k for k in fields if model[k]!=oldmodel[k]]
        if mismatch:raise RuntimeError('Fixed-new-g identity changed: '+', '.join(mismatch))
        print(json.dumps(dict(event='ready',elapsed=time.monotonic()-started,
                              depth=args.depth,far=args.linear_far,fixed_new_g=True)),flush=True)
        request=dict(height=height,jacobian=False,audit=True)
        proc.stdin.write(json.dumps(request)+'\n');proc.stdin.flush()
        line=proc.stdout.readline()
        if not line:raise RuntimeError('Worker ended without an actual response')
        response=json.loads(line)
        proc.stdin.write('{"stop":true}\n');proc.stdin.flush()
        if proc.wait():raise RuntimeError('Worker failed after response')
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill();proc.wait()
        for stream in [proc.stdin,proc.stdout]:
            if stream:stream.close()
    diagnostic=endpoint_diagnostic(ready,response)
    comparisons={}
    a=prior['response'].get('jets',{});b=response.get('jets',{})
    for field in ['height','slope','second','meanSlopeCorrection','meanSecondCorrection']:
        if field not in a or field not in b:continue
        av=a[field] if isinstance(a[field],list) else [a[field]]
        bv=b[field] if isinstance(b[field],list) else [b[field]]
        comparisons[field]=dict(max_absolute=max(abs(x-y) for x,y in zip(av,bv)),
                                added_modes_max=max(map(abs,bv[len(av):]),default=0.),
                                old=av,new=bv)
    physical_cut_comparison=cut_jet_norm_comparison(a,b,cfg['spacing']) if a and b else None
    record=dict(request=request,response=response,config=cfg,ready=ready,
                endpoint_diagnostic=diagnostic,
                provenance=dict(input=str(args.input.resolve()),
                                input_sha256=hashlib.sha256(input_bytes).hexdigest(),
                                entrypoint_sha256=hashes,
                                semantic_change='Same new fixed rational metric and finite polynomial Dirichlet data; only specified numerical depths, grids and angular cutoffs are refined.'))
    data=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(data)>=5_000_000:raise RuntimeError('Response exceeds repository file cap')
    paths['response'].write_bytes(data)
    summary=dict(status='Actual finite nonlinear physical-depth refinement on the same new fixed g',
                 converged=response.get('converged',False),residual=response.get('residual'),
                 failed=response.get('failed'),audit=response.get('audit'),history=response.get('history'),
                 old_depth=prior['config']['depth'],new_depth=args.depth,
                 old_modes=old_modes,new_modes=modes,
                 old_steps=prior['config']['steps'],new_steps=cfg['steps'],
                 old_quadrature=prior['config']['quadrature'],new_quadrature=cfg['quadrature'],
                 old_linear_far=prior['config']['linearFar'],new_linear_far=args.linear_far,
                 old_linear_steps=prior['config']['linearSteps'],new_linear_steps=cfg['linearSteps'],
                 fixed_new_g_fields_verified=fields,
                 elapsed=time.monotonic()-started,
                 peak_child_RSS_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                 endpoint_diagnostic=diagnostic,cut_jet_comparisons=comparisons,
                 physical_cut_comparison=physical_cut_comparison,
                 response=str(paths['response']),response_bytes=len(data),
                 response_sha256=hashlib.sha256(data).hexdigest(),
                 limits=['Finite Fourier and finite nonlinear depth only.',
                         'An amplitude margin is not the exact F224 trace match.',
                         'No complete strong closed surface or reach claim.'])
    paths['summary'].write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(converged=summary['converged'],residual=summary['residual'],
                          failed=summary['failed'],audit=summary['audit'],
                          elapsed=summary['elapsed'],peak_child_RSS_KiB=summary['peak_child_RSS_KiB'],
                          linear_only_log2_z=None if diagnostic is None else diagnostic['log2_low_height_l1'],
                          cut_jet_maxima={k:v['max_absolute'] for k,v in comparisons.items()})),flush=True)


if __name__=='__main__':
    main()
