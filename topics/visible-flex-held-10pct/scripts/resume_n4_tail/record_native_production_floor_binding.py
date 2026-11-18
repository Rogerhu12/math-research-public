#!/usr/bin/env python3
"""Read-only discovery of the original DN .05 versus frozen capsule .1 floor.

Read exact source literals, the existing failed CP and saved three-stage trace.
Do not import engines, reconstruct geometry, solve a root or call a flow.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def load(path):
    path=Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes())


def packed(values):
    return struct.pack('<'+'d'*len(values),*values)


def occurrence(path,needle):
    lines=Path(path).read_text().splitlines()
    found=[dict(line_number=i+1,literal=line.strip()) for i,line in enumerate(lines) if needle in line]
    if len(found)!=1:
        raise ValueError('Expected one exact source binding: '+needle)
    return dict(source=ref(path),needle=needle,**found[0])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();w=a.workspace.resolve()
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    scripts=topic/'scripts/resume_n4_tail'
    original=w/'n4_work/shared-periodic-source/scripts'
    cp=w/'n4_work/raw-primaryb016-lam002-actual-m20-parts32-v1/one-ulp-tail.json.gz'
    capsule=w/'n4_work/parts32-frozen-mp-baseline-v1/capsule-summary.json'
    cpp=scripts/'native_extended/frozen_flow.cpp'
    bridge=scripts/'frozen_stage_arithmetic_bridge.mjs'
    if sha(cp)!='b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e':
        raise ValueError('Different original complete failed CP')
    if sha(capsule)!='3785fff5412ec751d2275d3f774b6c7503bfecb7ad781a38068f811f06ab35f7':
        raise ValueError('Different existing frozen capsule')
    if sha(cpp)!='916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f':
        raise ValueError('Executed original native source changed')
    record,cs=load(cp),load(capsule)
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path)!=digest:
                raise ValueError('Bound original source changed: '+path)
    for key in ('input','fixture','original_output','coefficients','reference'):
        if ref(cs[key]['path'])!=cs[key]:
            raise ValueError('Saved capsule provenance changed: '+key)
    config=record['config'];parameters=record['response']['checkpoint']['parameters']
    if ('projectionFloor' in config or parameters['projectionFloor']!=.05 or cs['root_rules']['floor']!=.1):
        raise ValueError('This report is restricted to the observed default-propagation case')
    locations={
        'DN_factory_default':occurrence(original/'950f-tail-stage-core.mjs','projectionFloor=.05'),
        'DN_engine_explicit_argument':occurrence(original/'950f-tail-stage-core.mjs','mu:c.mu,orientation,projectionFloor'),
        'split_engine_explicit_argument':occurrence(original/'950f-tail-stage-split.mjs','projectionFloor:p.projectionFloor'),
        'direct_engine_default':occurrence(original/'periodic-quadrature/general_root_tail_momentum.mjs','floor=options.projectionFloor??.1'),
        'capsule_imports_original_config':occurrence(bridge,'cfg=frozen.config'),
        'capsule_direct_engine_constructor':occurrence(bridge,'createSplitFluxMomentumTailEngine({...cfg,mu:fixture.mu'),
        'capsule_reported_floor':occurrence(bridge,'floor:cfg.projectionFloor??.1'),
        'native_validation_hard_lock':occurrence(cpp,'c.floor!=.1')}
    reference=load(cs['reference']['path']);old=load(cs['original_output']['path'])
    rows=[]
    for stage in (43,38,175):
        r=next(v for v in reference['rows'] if v['stage']==stage)
        prior=next(v for v in old['rows'] if v['stage']==stage)
        domain=[e for e in r['events'] if e['event']=='domain']
        if not domain or any(e['floor']!=.1 for e in domain):
            raise ValueError('The complete saved domain stream has another floor')
        all_pass=all(e['D_pass'] and e['S_compared'] and e['S_pass']
                     and e['A_compared'] and e['A_pass'] for e in domain)
        same=packed(prior['reference42'])==packed(r['state'])
        if not same:
            raise ValueError('The existing capsule no longer matches the original DN output42')
        rows.append(dict(stage=stage,saved_domain_events=len(domain),
            every_saved_D_S_A_comparison_passed_capsule_point1=all_pass,
            minimum_saved_D=min(e['D'] for e in domain),
            minimum_saved_S=min(e['S'] for e in domain),
            minimum_saved_A=min(e['A'] for e in domain),
            original_DN_and_capsule_output42_bitwise_identical=same,
            output42_sha256=hashlib.sha256(packed(r['state'])).hexdigest()))
    result=dict(scope=__doc__,source=ref(__file__),command=sys.argv,original_CP=ref(cp),
        capsule_summary=ref(capsule),capsule_reference=cs['reference'],original_DN_output=cs['original_output'],
        source_locations=locations,config_projectionFloor_key_present=False,
        production_checkpoint_projectionFloor=parameters['projectionFloor'],
        production_DN_default_projectionFloor=.05,direct_engine_default_projectionFloor=.1,
        capsule_root_rule_floor=cs['root_rules']['floor'],native_current_allowed_floor=.1,
        current_failed_CP_minA=record['response']['lastIteration']['minA'],named_saved_trace_results=rows,
        all_saved_three_stage_domain_comparisons_passed_stronger_floor=all(
            r['every_saved_D_S_A_comparison_passed_capsule_point1'] for r in rows),
        interpretation='The existing three-stage capsule and arithmetic comparisons are explicitly for floor.1. Their complete saved domain comparisons all pass.1 and the original DN42 outputs are already bitwise identical; this does not identify the two domain gates for arbitrary states or the entire tail.',
        required_production_binding='Keep the original DN projectionFloor.05. The executed native validate hard-locks.1, so direct production attachment is not yet valid. An independently owned version must explicitly support/bind.05 while retaining.1 for saved-interface checks; no other formula/threshold may be changed.',
        existing_source_or_library_modified=False,new_compilation=False,new_flow_root_or_Jacobian=False,
        original_tail_tolerance=record['config']['solveTolerance'],new_actual_tail_acceptance=False)
    with a.out.open('x') as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),rows=rows)),flush=True)


if __name__=='__main__':
    main()
