#!/usr/bin/env python3
"""Extract accepted actual-coupling scalars and hashes, without field arrays."""
import argparse,gzip,hashlib,json
from pathlib import Path

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scalars(v):return {k:x for k,x in v.items() if not isinstance(x,(dict,list))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--periodic-manifest',type=Path)
    p.add_argument('--periodic-source',type=Path)
    a=p.parse_args();stem=a.prefix;summary_path=stem.with_name(stem.name+'-summary.json')
    summary=json.loads(summary_path.read_text())
    if not summary['solver_success']:raise ValueError('This extractor requires a completed accepted solve')
    keys=['command','solver_success','input_checkpoint_sha256','script_sha256',
          'prefix_loader_sha256','prefix_replay_sources','warmup_path','warmup',
          'linear_dn_difference','config','angular_chart_eta','physical_profile',
          'physical_port_sha256','plateau_settings','gauge_amplitude','parameters',
          'meridian_length','nodes','actual_outer_checks','max_rms','max_bc',
          'domain_newton','seconds','tail_calls','tail_source_sha256',
          'worker_returncode_before_close','worker_returncode_after_close']
    out={k:summary[k] for k in keys if k in summary}
    out.update(scope=__doc__,summary_sha256=sha(summary_path),prefix_scalars=scalars(summary['summary']),
               seam_scalars=scalars(summary['tail_seam']),same_metric_refinement=bool(summary['config'].get('fixed_metric',False)))
    out['tail_responses']=[]
    for f in sorted(stem.parent.glob(stem.name+'-tail_*.json.gz')):
        raw=json.loads(gzip.decompress(f.read_bytes()));r=raw['response'];h=r.get('history',[])
        row=dict(file=f.name,sha256=sha(f),converged=r['converged'],residual=r['residual'],
                 request_jacobian=raw['request'].get('jacobian'),request_audit=raw['request'].get('audit'),
                 final_iteration=h[-1]if h else None)
        if 'audit'in r:row['audit']=r['audit']
        out['tail_responses'].append(row)
    cp=stem.with_suffix('.json.gz');raw=json.loads(gzip.decompress(cp.read_bytes()))
    out['actual_checkpoint']=dict(file=cp.name,sha256=sha(cp),coefficient_chunks=raw.get('pp_coefficient_chunks',[]))
    for chunk in out['actual_checkpoint']['coefficient_chunks']:
        if sha(stem.parent/chunk['file'])!=chunk['sha256']:raise ValueError('Actual checkpoint chunk hash mismatch')
    out['run_file_hashes']={f.name:sha(f) for f in sorted(stem.parent.glob(stem.name+'*'))if f.is_file()}
    if a.periodic_manifest:
        if not a.periodic_source:raise ValueError('Runtime periodic source is required for hash verification')
        manifest=json.loads(a.periodic_manifest.read_text())
        actual={}
        for name,want in manifest['derived_sha256'].items():
            got=sha(a.periodic_source/'scripts/periodic-quadrature'/name)
            if got!=want:raise ValueError('Periodic runtime hash mismatch: '+name)
            actual[name]=got
        for name,hashes in manifest['patched_sha256'].items():
            if sha(a.periodic_source/name)!=hashes['after']:raise ValueError('Patched runtime hash mismatch: '+name)
        out['periodic_runtime']=dict(manifest_sha256=sha(a.periodic_manifest),verified_derived_sha256=actual,
                                    patched_sha256=manifest['patched_sha256'],declared_grid=summary['tail_config']['quadrature'],
                                    mathematical_identity='R30; public N and every original guard retained')
    a.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),bytes=a.out.stat().st_size)))

if __name__=='__main__':main()
