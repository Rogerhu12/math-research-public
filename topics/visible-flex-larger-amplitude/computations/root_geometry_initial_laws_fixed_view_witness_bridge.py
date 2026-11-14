#!/usr/bin/env python3
"""Extend the frozen physical witness bridge to its actual initial-law audit.

The original p31 audit identity is retained. Complete PPoly/raw/core/profile
equality and every original bridge gate remain mandatory. This starts no
field sampling, BVP, full-mean audit or Node worker.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BASE='root_geometry_fixed_view_witness_bridge.py'
BASE_SHA='ef519e4d24a199b3e2c395e3adfa775f9a405f8cb8b2953c058baa0acba80733'
AUDIT='strong_initial_laws_interior_fullmean_audit.py'
AUDIT_SHA='35155b17516ce3ff72ddfc957894e53cbd2c7a4a6707d57e62887a8d72e4fbe0'
FIXED='strong_initial_laws_freeze_design_view.py'
FIXED_SHA='785442ffad4a72f9671aef285dae4a4bfc11f410b2cec54027cd913a09a61ab3'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def transformed():
    if sha(HERE/BASE)!=BASE_SHA or sha(HERE/AUDIT)!=AUDIT_SHA:
        raise ValueError('The original witness bridge or actual initial-law audit source changed')
    original=(HERE/BASE).read_text();source=original
    edits=[("here/'strong_interior_jet_fullmean_audit.py'","here/'strong_initial_laws_interior_fullmean_audit.py'"),
           ("    args.out.parent.mkdir(parents=True, exist_ok=True)\n",
            "    result['initial_laws_source_bridge'] = INITIAL_LAWS_SOURCE_BRIDGE\n    args.out.parent.mkdir(parents=True, exist_ok=True)\n")]
    for before,after in edits:
        if source.count(before)!=1:raise ValueError('One exact source anchor required')
        source=source.replace(before,after,1)
    ast.parse(source,filename='<original-witness-bridge-initial-laws>')
    reverse=source
    for before,after in reversed(edits):reverse=reverse.replace(after,before,1)
    if reverse!=original:raise ValueError('The original full witness bridge was not recovered exactly')
    return source,{'base_source_sha256':BASE_SHA,'adapter_source_sha256':sha(__file__),
        'actual_audit_source_sha256':AUDIT_SHA,'transformed_source_sha256':hashlib.sha256(source.encode()).hexdigest(),
        'exact_reverse_recovers_original':True,'only_original_audit_source_name_and_extra_provenance_changed':True}


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--prepare-record',type=Path)
    for key in ('accepted-reference','fixed-report','interior-audit'):
        parser.add_argument('--'+key,type=Path)
    args,unused=parser.parse_known_args()
    source,provenance=transformed()
    if args.prepare_record:
        with args.prepare_record.open('x') as f:
            json.dump({'prepared_only':True,'actual_witness_bridge_run':False,'source':provenance},f,indent=2);f.write('\n')
        print(json.dumps({'prepared_only':True,'path':str(args.prepare_record),'sha256':sha(args.prepare_record)}),flush=True)
        return
    if any(getattr(args,k) is None for k in ('accepted_reference','fixed_report','interior_audit')):
        raise ValueError('An actual accepted primary, conversion report and audit are required')
    import gzip
    def read(p):
        data=p.read_bytes();return json.loads(gzip.decompress(data) if p.suffix=='.gz' else data)
    primary,report,audit=(read(p) for p in (args.accepted_reference,args.fixed_report,args.interior_audit))
    adapter=audit.get('initial_laws_provider_adapter',{})
    observations=adapter.get('observations',{});profile=primary['frozen_profile'];checks=[]
    def check(name,condition):
        if not condition:raise ValueError('Initial-law witness identity: '+name)
        checks.append({'name':name,'passed':True})
    check('original_audit_primary_SHA_kept',audit['input_sha256']==sha(args.accepted_reference))
    check('one_real_profile_loader',observations.get('provider_loads')==1 and len(observations.get('saved_fields',[]))==1)
    field=observations['saved_fields'][0]
    weight=float(profile.get('initial_speed_frontload',0.));pulse=float(profile.get('initial_speed_pulse',0.));degree=profile.get('initial_speed_frontload_degree',22)
    check('same_actual_initial_law_parameters',field['initial_speed_frontload']==weight and field['initial_speed_pulse']==pulse and field['initial_speed_frontload_degree']==degree)
    check('profile_and_physical_length_reloaded',field['physical_profile_unchanged'] and field['physical_length_original_gate_passed'] and field['physical_length']==primary['meridian_length'])
    check('unchanged_physical_formula_and_complete_mean',adapter.get('exact_reverse_recovers_original_complete_mean_source') is True and adapter.get('original_physical_quintic_and_all_metric_curvature_formulas_unchanged') is True and adapter.get('numerical_solution_or_continuous_certificate_created') is False)
    sources=adapter['source_sha256']
    check('actual_initial_laws_audit_source',audit['source_sha256']==AUDIT_SHA and sources[AUDIT]==AUDIT_SHA)
    for name,wanted in sources.items():
        check('complete_actual_audit_provider_source_'+name,Path(name).name==name and sha(HERE/name)==wanted)
    matched=[(p,h) for p,h in report['source_sha256'].items() if Path(p).name==FIXED]
    if weight!=0. or pulse!=0.:
        check('nonzero_law_conversion_uses_actual_provider_wrapper',len(matched)==1 and matched[0][1]==FIXED_SHA)
    elif not matched:
        check('legacy_conversion_only_at_exact_zero_laws',field['zero_weight_uses_original_arithmetic'] is True)
    if matched:
        check('initial_law_conversion_source_pinned',len(matched)==1 and matched[0][1]==FIXED_SHA and sha(HERE/FIXED)==FIXED_SHA)
    provenance.update({'checks':checks,'all_checks_passed':True,'actual_same_PP_bridge_required':True,
        'audit_original_input_sha256':audit['input_sha256'],
        'initial_speed_frontload':weight,'initial_speed_pulse':pulse,'initial_speed_frontload_degree':degree,
        'source_and_input_sha256':{str(p):sha(p) for p in (args.accepted_reference,args.fixed_report,args.interior_audit)}})
    namespace={'__file__':str(Path(__file__).resolve()),'__name__':'original_witness_bridge_with_initial_law_source',
               'INITIAL_LAWS_SOURCE_BRIDGE':provenance}
    exec(compile(source,'<original-witness-bridge-initial-laws>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
