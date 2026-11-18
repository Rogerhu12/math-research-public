#!/usr/bin/env python3
"""Bind native n4 core and material-angle definitions to explicit source bytes.

The prior reader/constructor is unchanged. This version adds the original
bimodal chart source to the binding and requires the supported definition
fingerprint. A later accepted checkpoint may change q/c/windows/profile,
but a different definition must use an explicitly updated reader. No m3
projection, integral constant or positivity certificate is imported.
"""
import argparse
from dataclasses import replace
import json
import math
from pathlib import Path
import sys

import n4_integral_core_binding as original


BASE_READER_SHA256='48c5651fca495f6abe35c95e3cdbcd1eaa678e6d97108c49db634a73fca2ee2e'
SUPPORTED_DEFINITION={
    'raw_fixed_core.py':'8d7880398f95a3e5cc52030e2b08682d46571a761060562eaff79a56e4d7c182',
    'raw_n4_free_complementary.py':'5fbd11f9fa534af6a6871eaca3787627b15d7fea38059481afc6af64ea21efd9',
    'raw_n4_complementary.py':'4ff42d590fa6ad5a97bf4cf7c1447041260a3aa3a23ff158d90b5f7d2f03c778',
    'large_radius_local_core.py':'d59f6114b9f24c4c8e128f848c4738655802c0ca5689ae4b8bc56528ada06b39',
    'second_order_large_radius_core.py':'ea0e0e70b704d83b4c5fc3bcc13f1b84f2161fc274c898f65f498e7a9a3f0c94',
    'fixed_large_radius_core.py':'00f23e03fb736ece6d461ffb082c8bb598a8c4200d3f60b5e8d752731163ffba',
    'plateau_core.py':'0db6b2aaf7ecce94eb2f2cda926b5e1f12c3da99656c0e5d0f4b9e3c7dddee34',
    'complementary_moment_basis.py':'2ef6b57270bb0213a5ec6f581e24330c3da7086ea86e615c11f28b1fbd18dc6c',
    'moment_interval_bounds.py':'467195b13ce970ee7360494776ea58b6fd56ab893d196065ecbbb475c7e02481',
    'bimodal_chart_loader.py':'f2c868076e476a431e35dd7ddbc6bfc684267d05c590c7470446ccd54f7678b6',
}


def file_ref(path):
    return dict(path=str(Path(path).resolve()),sha256=original.sha(path))


def load_binding(checkpoint,execution_record,source_root):
    if original.sha(original.__file__)!=BASE_READER_SHA256:
        raise ValueError('The original reader/constructor implementation changed')
    bound=original.load_binding(checkpoint,execution_record,source_root)
    execution=json.loads(Path(execution_record).read_text())
    sources=dict(bound.source_sha256)
    for name,digest in SUPPORTED_DEFINITION.items():
        path=bound.source_root/name
        if original.sha(path)!=digest or execution['source_sha256'].get(name)!=digest:
            raise ValueError('Unsupported native core/material-chart definition: '+name)
        sources[str(path)]=digest
    if not math.isfinite(float(bound.record['angular_chart_eta'])):
        raise ValueError('The independent material-chart eta must be explicit and finite')
    return replace(bound,source_sha256=sources)


def check_prior_native_evidence(bound,evidence_path):
    """Reuse only the actual same-core construction already completed by v1."""
    prior=json.loads(Path(evidence_path).read_text())
    if (prior['reader_sha256']!=BASE_READER_SHA256 or
            prior['checkpoint']['sha256']!=bound.checkpoint_sha256 or
            prior['execution_record']['sha256']!=original.sha(bound.execution_record) or
            prior.get('native_constructed') is not True):
        raise ValueError('Native evidence is not the prior construction of this exact checkpoint')
    now=bound.descriptor()
    for key in ('q_gauge','q_actual','complete_controls','parameters','central_correction_scales',
                'native_arguments','modes','raw_control_anchor_modes','meridian_length_binary64',
                'physical_profile_payload_sha256','physical_port_payload_sha256','angular_chart_eta'):
        if prior[key]!=now[key]:
            raise ValueError('Prior native constructor used another physical input: '+key)
    for path,digest in prior['source_sha256'].items():
        if bound.source_sha256.get(path)!=digest or original.sha(path)!=digest:
            raise ValueError('Prior native constructor definition changed: '+path)
    identity=prior['native_constructor_identity']
    if not identity['all_controls_retained'] or not identity['actual_q_retained']:
        raise ValueError('Prior constructor did not retain the complete input')
    return dict(file=file_ref(evidence_path),reader_sha256=prior['reader_sha256'],
                command=prior['command'],native_constructor_identity=identity,
                reused_without_reconstructing=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('checkpoint','execution-record','source-root','output'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--prior-native-evidence',type=Path)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError('Use a fresh binding record')
    bound=load_binding(args.checkpoint,args.execution_record,args.source_root)
    result=bound.descriptor()
    result.update(binding_scope=__doc__,reader=file_ref(__file__),
        original_reader=file_ref(original.__file__),
        supported_definition='native-n4-raw-free-c8-frozen-J-bimodal-chart-v1',
        source_definition_count=len(SUPPORTED_DEFINITION),
        material_chart_source=file_ref(bound.source_root/'bimodal_chart_loader.py'),
        chart_eta_equals_core_eta_required=False,
        chart_derivatives_scope='The original algebraic material-angle chain; e, e_s and e_ss must come from the same physical radial profile and atlas. Their values are not selected or recomputed here.',
        future_checkpoint_rule='All new q/c/profile/width/lambda data must come from a complete accepted checkpoint and its execution record. No current positivity, integral or inverse bound transfers automatically.',
        native_constructed_in_this_run=False,flow_or_metric_audit_repeated=False,
        original_production_modified=False,command=[sys.executable,*sys.argv])
    if args.prior_native_evidence:
        result['prior_native_constructor_evidence']=check_prior_native_evidence(bound,args.prior_native_evidence)
    with args.output.open('x') as stream:
        json.dump(result,stream,ensure_ascii=False,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=str(args.output),sha256=original.sha(args.output),
                         q_actual=bound.q_actual,controls=len(bound.controls),
                         native_reconstructed=False,flow_repeated=False)))


if __name__=='__main__':
    main()
