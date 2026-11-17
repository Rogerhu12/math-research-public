#!/usr/bin/env python3
"""Extract one completed raw-prefix fixed-g refinement without field tables."""
import argparse
import gzip
import json
from pathlib import Path
from record_design_terminal import sha,scalars,scalar_tree,indexed,core_summary


def checkpoint(path):
    record=json.loads(gzip.decompress(path.read_bytes()));chunks={}
    for chunk in record['pp_coefficient_chunks']:
        assert sha(path.parent/chunk['file'])==chunk['sha256'],chunk['file']
        chunks[chunk['file']]={key:value for key,value in chunk.items()if key!='file'}
    return record,dict(file=path.name,sha256=sha(path),chunk_hashes=chunks)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix',type=Path,required=True)
    parser.add_argument('--input-record',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=args.prefix.with_suffix('.json')
    row=json.loads(result.read_text());input_record=json.loads(args.input_record.read_text())
    if not row['success']:raise ValueError('A completed successful finite BVP is required')
    before=input_record['row']
    old_path=Path(row['arguments']['checkpoint'])
    oldcp,oldhash=checkpoint(old_path);cp,newhash=checkpoint(args.prefix.with_suffix('.json.gz'))
    assert oldhash['sha256']==input_record['checkpoint']['sha256']==row['input_checkpoint_sha256']
    assert cp['fixed_metric']
    assert cp['physical_profile']==oldcp['physical_profile']==row['physical_profile']==before['physical_profile']
    assert cp['physical_port_sha256']==oldcp['physical_port_sha256']==row['physical_port_sha256']
    assert cp['raw_control_anchor_modes']==oldcp['raw_control_anchor_modes']==row['core_projection_order']
    assert cp['angular_chart_eta']==oldcp['angular_chart_eta']
    assert cp['plateau_settings']==oldcp['plateau_settings']
    after=scalars(row)
    after.update(parameters=indexed(row['parameters']),
                 central_correction_scales=indexed(cp['central_correction_scales']),
                 domain_newton=row['domain_newton'],summary=scalars(row['summary']),
                 core=core_summary(cp['core_summary']),config=cp['config'])
    keys=('complete_core_identity_error','core_embedding','complete_map_projection_error',
          'input_core_summary_diagnostic','old_lift_initial_source','input_inlet_coefficient_residual',
          'input_mesh_nodes','seed_mesh_nodes','input_mesh_coverage_max','inlet_repair_max',
          'seed_boundary_max','boundary_evaluated')
    initial={key:row[key]for key in keys}
    for key in ('parameter_jac_checks','boundary_jac_checks'):
        initial[key]=indexed(row[key])
    out=dict(scope='Completed finite linear-port raw-prefix refinement at the same complete physical metric and fixed circle-homotopy parameter. Core c8 is explicitly free; eta and frozen J remain fixed. Sampled validation is separate from a true nonlinear tail and a closed family.',
             collector_sha256=sha(__file__),input_record_sha256=sha(args.input_record),
             result_sha256=sha(result),log_sha256=sha(args.prefix.with_suffix('.log')),
             newton_trace_sha256=sha(args.prefix.with_name(args.prefix.name+'-newton.jsonl')),
             fixed_physical_profile=cp['physical_profile'],physical_port_sha256=cp['physical_port_sha256'],
             plateau_settings=cp['plateau_settings'],raw_control_anchor_modes=cp['raw_control_anchor_modes'],
             before=before,after=after,initial=initial,arguments=row['arguments'],
             source_sha256=row['source_sha256'],core_transform=scalar_tree(row['core_transform']),
             coefficient_certificate=scalar_tree(row['coefficient_certificate']),
             input_checkpoint=oldhash,output_checkpoint=newhash,
             observed_ratios={key:after['summary'][key]/before['summary'][key]for key in ('metric_l1','darboux_l1','flow_defect')},
             complete_sampled_metric_below_1e_minus_6=after['summary']['metric_l1']<1e-6)
    args.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size,sha256=sha(args.out),
                          metric=after['summary']['metric_l1'],darboux=after['summary']['darboux_l1'],
                          ratios=out['observed_ratios'])))


if __name__=='__main__':main()
