#!/usr/bin/env python3
"""Export compact coupled-run evidence, never numerical state or DN arrays."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def digest(path):
    path=Path(path)
    return dict(path=str(path),bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())
def scalars(value):
    return {key:item for key,item in value.items()
            if isinstance(item,(str,int,float,bool))or item is None}
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--adapter',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--context',default='')
    a=parser.parse_args();summary_path=a.run/'summary.json'
    summary=json.loads(summary_path.read_text());args=summary['arguments']
    command=[sys.executable,'-u',str(a.adapter)]
    for key,value in args.items():
        if key=='lagged_tail' or value is None:continue
        option='--'+key.replace('_','-')
        if isinstance(value,bool):
            if value:command.append(option)
        elif isinstance(value,list):command.extend([option]+[str(x)for x in value])
        else:command.extend([option,str(value)])
    outputs=[summary_path]
    outputs.extend(sorted(a.run.glob('prefix*.json.gz')))
    outputs.extend(sorted(a.run.glob('prefix_coeff_*.npy.gz')))
    seam=summary.get('tail_seam',{})
    tail_audit={}
    if seam.get('tail_record'):
        tail_path=a.run/seam['tail_record'];outputs.append(tail_path)
        tail=json.loads(gzip.decompress(tail_path.read_bytes()))['response']
        tail_audit=scalars(tail.get('audit',{}))
    inputs=[]
    for key in ('prefix_driver','coupler_source','worker','profile','chart','port','tail_config','restart'):
        if args.get(key):inputs.append(digest(args[key]))
    seed_status=None
    if args.get('restart'):
        seed=json.loads(gzip.decompress(Path(args['restart']).read_bytes()))
        seed_status={key:seed.get(key)for key in ('solver_success','gauge_amplitude','actual_primary_amplitude')}
    config=json.loads(Path(args['tail_config']).read_text())
    initial_tail=digest(config['initialCheckpoint'])if config.get('initialCheckpoint')else None
    record=dict(schema='compact-finite-coupled-run-v1',session='true_a_analysis',scope=__doc__,
        context=a.context,command=command,command_scope='Equivalent command with all recorded default values made explicit.',
        adapter=digest(a.adapter),exporter=digest(__file__),solver_success=summary['solver_success'],
        q=summary.get('gauge_amplitude',args['amplitude']),modes=args['modes'],tail_depth=config.get('depth'),
        nodes=summary.get('nodes'),seconds=summary.get('seconds'),error=summary.get('error'),
        max_rms_collocation_residual=summary.get('max_rms_collocation_residual'),
        frozen_profile=summary.get('frozen_profile'),prefix_audit=scalars(summary.get('summary',{})),
        actual_outer_checks=summary.get('actual_outer_checks'),tail_seam=scalars(seam),tail_audit=tail_audit,
        tail_calls=summary.get('tail_calls'),initial_prefix_status=seed_status,initial_tail=initial_tail,
        input_hashes=inputs,output_hashes=[digest(path)for path in outputs],
        numerical_settings={key:config.get(key)for key in ('spacing','modes','depth','steps','quadrature','linearFar','linearSteps','shootingParts','projectionFloor','solveTolerance','auditSteps')},
        limitations=['Finite Fourier and finite depth only.','Prefix FFT l1 and curvature are sampled diagnostics.','Complete Cartesian/global C2 closing, infinite tail, all-time reach and the held 10 percent goal are not certified by this solver success.'])
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.output),sha256=digest(a.output)['sha256'],success=record['solver_success'],q=record['q'],metric_l1=record['prefix_audit'].get('metric_l1'),tail_audit=tail_audit)),flush=True)
if __name__=='__main__':main()
