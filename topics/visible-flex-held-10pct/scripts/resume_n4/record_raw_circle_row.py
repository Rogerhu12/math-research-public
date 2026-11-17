#!/usr/bin/env python3
"""Freeze one completed raw-circle stage and extract only its scalar evidence."""
import argparse
import gzip
import json
from pathlib import Path
from record_design_terminal import sha,scalars,scalar_tree,indexed,core_summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result',type=Path,required=True)
    parser.add_argument('--lambda-value',type=float,required=True)
    parser.add_argument('--snapshot-dir',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    content=args.result.read_bytes();raw=json.loads(content)
    rows=[r for r in raw['rows']if abs(r['homotopy']-args.lambda_value)<1e-15]
    if len(rows)!=1:raise ValueError('Exactly one completed stage must match')
    row=rows[0]
    args.snapshot_dir.mkdir(parents=True,exist_ok=True)
    snapshot=args.snapshot_dir/(args.result.stem+f'-stage{args.lambda_value:g}-source.json')
    snapshot.write_bytes(content)
    logsnapshot=snapshot.with_suffix('.log')
    logsnapshot.write_bytes(args.result.with_suffix('.log').read_bytes())
    out=dict(scope='One completed finite linear-port prefix stage. BVP success and the complete sampled metric gate are reported separately; no actual nonlinear tail, closed family or completion claim.',
             collector_sha256=sha(__file__),source_snapshot_sha256=sha(snapshot),
             log_snapshot_sha256=sha(logsnapshot),arguments=raw['arguments'],
             source_sha256=raw['source_sha256'],
             raw_control_definition=raw['raw_control_definition'],
             coefficient_certificate=scalar_tree(raw['coefficient_certificate']),
             complete_core_guard=scalar_tree(raw['complete_core_guard']),
             row=scalars(row))
    for key in ('physical_profile','domain_newton','material_restart'):
        if key in row:out['row'][key]=scalar_tree(row[key])
    for key in ('seed_core','core'):
        if key in row:out['row'][key]=core_summary(row[key])
    if 'parameters'in row:out['row']['parameters']=indexed(row['parameters'])
    if 'summary'in row:
        out['row']['summary']=scalars(row['summary'])
        out['complete_sampled_metric_below_1e_minus_6']=row['summary']['metric_l1']<1e-6
    for key in ('parameter_jac_checks','boundary_jac_checks'):
        if key in row:out['row'][key]=indexed(row[key])
    stem=Path(raw['arguments']['out'])
    cp_path=stem.with_name(stem.name+f'-lam{args.lambda_value:g}.json.gz')
    cp=json.loads(gzip.decompress(cp_path.read_bytes()))
    assert cp['solver_success']==row['success']
    assert cp['raw_control_anchor_modes']==out['raw_control_definition']['anchor_modes']
    assert cp['physical_profile']==row['physical_profile']
    chunks={}
    for chunk in cp['pp_coefficient_chunks']:
        assert sha(cp_path.parent/chunk['file'])==chunk['sha256'],chunk['file']
        chunks[chunk['file']]={k:v for k,v in chunk.items()if k!='file'}
    out['checkpoint']=dict(file=cp_path.name,sha256=sha(cp_path),chunk_hashes=chunks,
                           physical_port_sha256=cp['physical_port_sha256'],
                           raw_control_anchor_modes=cp['raw_control_anchor_modes'],
                           central_correction_scales=indexed(cp['central_correction_scales']))
    out['input_files']={}
    for key in ('port','profile','restart','previous'):
        if raw['arguments'].get(key):
            path=Path(raw['arguments'][key])
            if not path.is_absolute():path=args.result.parent/path
            out['input_files'][key]=dict(path=str(path),sha256=sha(path))
    args.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size,sha256=sha(args.out),
                          lambda_value=args.lambda_value,bvp_success=row['success'],
                          complete_metric=row.get('summary',{}).get('metric_l1'))))


if __name__=='__main__':main()
