#!/usr/bin/env python3
"""Record an actual fixed-g prefix refinement using parameters/scalars/hashes."""
import argparse,gzip,hashlib,json,shlex
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def scalars(value):return {k:v for k,v in value.items()if not isinstance(v,(dict,list))}
def indexed(values):return {str(i):v for i,v in enumerate(values)}
def checkpoint(path):return json.loads(gzip.decompress(path.read_bytes()))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--design',default='q015-m20')
    p.add_argument('--fixed',default='q015-fixed-m20')
    p.add_argument('--runtime',type=Path)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();runtime=a.runtime or a.work/'refine-runtime'
    before_raw=json.loads((a.work/(a.design+'.json')).read_text())
    before=before_raw['rows'][-1]
    after=json.loads((a.work/(a.fixed+'.json')).read_text())
    before_cp=checkpoint(a.work/(a.design+'-lam0.json.gz'))
    after_cp=checkpoint(a.work/(a.fixed+'.json.gz'))
    assert before['success'] and after['success']
    assert before_cp['physical_profile']==after_cp['physical_profile']==after['physical_profile']
    assert before_cp['physical_port_sha256']==after_cp['physical_port_sha256']==after['physical_port_sha256']
    assert after_cp['fixed_metric'] is True
    assert before_cp['config']['modes']==after_cp['config']['modes']==after['modes']
    assert before_cp['config']['angular']==after_cp['config']['angular']==after['arguments']['angular']
    names=['refine_fixed_large_radius.py','fixed_large_radius_core.py','nested_large_radius_core.py',
           'nested_projection_core.py','run_large_radius_circle.py','large_radius_local_core.py',
           'bimodal_chart_loader.py','plateau_core.py','complementary_moment_basis.py',
           'moment_interval_bounds.py','exact_core_lift.py','exact_lift_parameter_jac.py',
           'analytic_adaptive_core_jac.py','trace_domain_newton.py','fixed_bimodal_core.py','bimodal_core.py']
    dependencies={name:after['source_sha256'][name]for name in names}
    for name,h in dependencies.items():assert sha(runtime/name)==h,name
    observer=after['observer_provenance']
    assert observer['base_sha256']==dependencies['refine_fixed_large_radius.py']
    assert observer['observer_sha256']==dependencies['trace_domain_newton.py']
    wrapper=Path(__file__).with_name('run_observed_fixed.py')
    assert sha(wrapper)==observer['wrapper_sha256']
    def outcome(row,raw,cp,cp_path,stem):
        out=scalars(row)
        for key in ['physical_profile','domain_newton']:
            if key in row:out[key]=row[key]
        out.update(parameters=indexed(row['parameters']),summary=scalars(row['summary']),
                   central_correction_scales=indexed(cp['central_correction_scales']),
                   core=scalars(cp['core_summary']),arguments=raw['arguments'],
                   result_sha256=sha(a.work/(stem+'.json')),
                   checkpoint_sha256=sha(cp_path),log_sha256=sha(a.work/(stem+'.log')))
        chunks={}
        for chunk in cp['pp_coefficient_chunks']:
            assert sha(a.work/chunk['file'])==chunk['sha256'],chunk['file']
            chunks[chunk['file']]={k:v for k,v in chunk.items()if k!='file'}
        out['coefficient_chunk_hashes']=chunks
        return out
    first=outcome(before,before_raw,before_cp,a.work/(a.design+'-lam0.json.gz'),a.design)
    last=outcome(after,after,after_cp,a.work/(a.fixed+'.json.gz'),a.fixed)
    for key in ['complete_core_identity_error','complete_map_projection_error','input_core_summary_diagnostic',
                'old_lift_initial_source','input_inlet_coefficient_residual','input_mesh_nodes','seed_mesh_nodes',
                'input_mesh_coverage_max','inlet_repair_max','seed_boundary_max','boundary_evaluated']:
        if key in after:last[key]=after[key]
    trace=a.work/(a.fixed+'-newton.jsonl')
    trace_summary={}
    for line in trace.read_text().splitlines():
        row=json.loads(line)
        if row['event'].endswith('_end'):
            phase=row['event'];value=trace_summary.setdefault(phase,dict(calls=0,seconds=0.))
            value['calls']+=1;value['seconds']+=row.get('seconds',0.)
    result=dict(scope='One completed same-physical-metric M20 radial refinement. Full sampled metric/Darboux remain on a plateau; no continuous-angle, circle, nonlinear-tail or closed-family conclusion.',
                fixed_physical_profile=after['physical_profile'],physical_port_sha256=after['physical_port_sha256'],
                same_modes=after['modes'],same_angular=after['arguments']['angular'],
                design=first,refinement=last,
                design_input_sha256={k:dict(path=before_raw['arguments'][k],sha256=sha(Path(before_raw['arguments'][k])))for k in ('port','profile','restart','previous')if before_raw['arguments'].get(k)},
                observed_ratios={k:last['summary'][k]/first['summary'][k]for k in ['metric_l1','darboux_l1','flow_defect']},
                executed_dependencies_sha256=dependencies,observer_provenance=scalars(observer),
                actual_command=shlex.join(observer['original_command']),
                newton_trace_sha256=sha(trace),newton_phase_totals=trace_summary,
                collector_sha256=sha(__file__),collector_arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
                reproducibility='Regenerate the accepted q015-m20 design with its recorded arguments, prepare the listed fixed driver dependencies, then execute the recorded run_observed_fixed.py command. Arrays/checkpoints remain scratch-only; their hashes are retained.')
    a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out),ratios=result['observed_ratios'])))


if __name__=='__main__':main()
