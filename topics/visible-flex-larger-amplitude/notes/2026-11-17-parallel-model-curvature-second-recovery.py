#!/usr/bin/env python3
"""Overlay complete e024 recovery reports, then use unchanged e024 execution.

This file changes bookkeeping only. The full original 818-cell plan and each
lambda/G kernel call are unchanged. Complete reports, including lambda at an
interrupted G call, are reused. No completed failed attempt is retried.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path

ENGINE_SHA='e024c7aa3d011090d79d00f8db97f931520e0b0abbacf9e24a7487cb71964627'
PRIOR_MANIFEST_SHA='f0e8b5859ff67d3af3220e0cda98163136188093929d3eb6879cae22ad24bac7'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def prepare(a,R,self_sha):
    c=R.config(a);manifest,H=R.inspect(a,c,ENGINE_SHA)
    progress_path=a.prior/'progress.json';progress=H.read(progress_path)
    if progress['source_sha256']!=ENGINE_SHA or progress['manifest_sha256']!=PRIOR_MANIFEST_SHA:
        raise ValueError('Different interrupted first recovery')
    if (a.prior/'result.json').exists():raise ValueError('Prior recovery has a terminal; do not repeat it')
    if progress['failures']or progress['counts']['new_exceptions']or progress['fatal']is not None:
        raise ValueError('Prior failed reports need explicit preservation, not automatic retries')
    scaling={}
    for name,digest in H.FIXTURES.items():
        if 'lambda2-nodes'in name:scaling[digest]=H.read(c.outdir/'reused'/name)
    for rec in manifest['records']:
        for z in rec['scaling']:
            if z['action']=='reuse':scaling[z['old']['sha256']]=H.read(Path(z['old']['path']))
    pending=False;first=True
    for rec in manifest['records']:
        if rec['action']=='reuse':continue
        row=rec['row'];i=row['cell']
        if list(a.prior.glob(f'failure-{i:04d}-*.json')):
            raise ValueError('An existing failure must not be rerun')
        for z in rec['scaling']:
            p=a.prior/f"lambda-cell-{i:04d}-{z['piece']['part']}.json"
            d,identity=R.complete_json(p)
            if d is not None:
                if z['action']=='reuse':raise ValueError('A complete scaling slot was already duplicated')
                H.scaling_ok(d,row,z['piece']);R.finite(d)
                z['old']=identity;z['action']='reuse';scaling[identity['sha256']]=d
        p=a.prior/f'curvature-cell-{i:04d}.json';d,identity=R.complete_json(p)
        if d is not None:
            if pending or any(z['action']!='reuse'for z in rec['scaling']):
                raise ValueError('Complete curvature has a gap or missing scaling evidence')
            H.curvature_ok(d,row,scaling);R.finite(d)
            rec.update(action='reuse',status='certified',curvature=identity)
            rec.pop('reason',None)
        else:
            if pending and any(z['action']=='reuse'for z in rec['scaling']):
                raise ValueError('A later scaling certificate follows a missing earlier cell')
            pending=True
            rec['curvature']=identity
            rec['reason']='interrupted_G_call_with_reused_lambda'if first else'not_reached'
            first=False
    reused=sum(r['action']=='reuse'for r in manifest['records'])
    if reused!=progress['completed']:
        raise ValueError('Complete reports disagree with the last durable prior progress')
    manifest['counts']=dict(planned_cells=818,reused_complete_cells=reused,
        remaining_cells=818-reused,reused_failed_cells=0,
        reused_new_scaling_calls=sum(z['action']=='reuse'for r in manifest['records']for z in r['scaling']),
        remaining_scaling_calls=sum(z['action']=='compute_once'for r in manifest['records']for z in r['scaling']),
        remaining_curvature_calls=818-reused)
    manifest.update(schema='fixed-curvature-second-recovery-manifest-v1',
        overlay_wrapper_source_sha256=self_sha,execution_source_sha256=ENGINE_SHA,
        prior_progress_path=str(progress_path),prior_progress_sha256=sha(progress_path),
        prior_active_call=H.read(a.prior/'active-call.json'),
        interruption_cause='prior tool session unknown, reports stopped, no matching OS worker; no terminal',
        completed_slots_recomputed=False,mathematical_parameters_changed=False)
    return c,manifest,H

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('engine','topic','work','prior','manifest','outdir'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--execute',action='store_true');a=p.parse_args();a.mode='curvature'
    if sha(a.engine)!=ENGINE_SHA:raise ValueError('Changed e024 execution source')
    spec=importlib.util.spec_from_file_location('unchanged_e024_recovery',a.engine)
    R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
    self_sha=sha(__file__);c,manifest,H=prepare(a,R,self_sha)
    if not a.execute:
        if a.manifest.exists():raise ValueError('Frozen manifest already exists')
        digest=R.save(a.manifest,manifest)
        print(json.dumps(dict(mode='prepare_only_no_geometry',wrapper_source_sha256=self_sha,
                              execution_source_sha256=ENGINE_SHA,manifest_sha256=digest,
                              counts=manifest['counts'])),flush=True);return
    if not a.manifest.exists()or json.loads(a.manifest.read_bytes())!=manifest:
        raise ValueError('Frozen overlay manifest changed')
    original_guard=R.sources_unchanged
    def guard(config,engine_sha):
        original_guard(config,engine_sha)
        if sha(__file__)!=self_sha:raise ValueError('Overlay wrapper changed')
        if sha(Path(manifest['prior_progress_path']))!=manifest['prior_progress_sha256']:
            raise ValueError('An earlier worker changed the recovery evidence')
    R.sources_unchanged=guard
    R.execute(a,c,manifest,H,ENGINE_SHA)
    binding=dict(wrapper_source_sha256=self_sha,execution_source_sha256=ENGINE_SHA,
                 manifest_sha256=sha(a.manifest),result_sha256=sha(a.outdir/'result.json'),
                 mathematical_parameters_changed=False,completed_slots_recomputed=False)
    R.save(a.outdir/'overlay-execution-binding.json',binding)

if __name__=='__main__':main()
