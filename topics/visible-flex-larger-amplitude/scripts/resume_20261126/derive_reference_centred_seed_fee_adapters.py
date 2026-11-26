#!/usr/bin/env python3
"""Pure full-source derivation of strict R715 seed-fee consumers.

No actual batch is selected here. No scientific module is imported. The
unchanged R713 arithmetic and complete accurate-mean integrator are emitted
with independent report/request/journal schemas and one exact new source
contract. Existing consumers and their guards are never modified.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint

ORIGINAL_FEES = 'supported_smooth_triangle_seed_angular_jet_error_bounds.py'
ORIGINAL_FEES_SHA = '82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76'
ORIGINAL_MEAN = 'supported_smooth_triangle_accurate_mean_residuals.py'
ORIGINAL_MEAN_SHA = '581fbcc397d379b64ee4a1d36b864b9a9e3b537f7b1be962ae03e22920c72202'
PROVIDER_SHA = '0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b'
MEAN_SHA = 'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'
BASE_SHA = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
CONTRACTS = {
    'reference-centred': dict(
        stem='reference_centred_smooth_triangle',
        report_schema='complete-R711-reference-centred-fixed-normal-plane-SO3-QP-v1',
        driver_name='fullclosed_reference_centred_smooth_triangle_normal_lift_so3_qp.py',
        driver_sha256='92233b4ffb0aaff1644e0c4bc9e7357a8eae37bd68e6d02ef0c6e0dcfbb31b81',
        reader_name='read_reference_centred_smooth_triangle_normal_lift_so3_report.py',
        reader_sha256='7fc213c108245cb2c555d573a52961fd07f1b941d85411e8e6e8d8c22f20a5bb',
        field_schema='complete-R711-reference-centred-SO3-fixed-normal-plane-six-control-layer-v1',
        field_name='so3_reference_centred_smooth_triangle_normal_lift_operator.py',
        field_sha256='b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d',
        calibration_name='reference_centred_smooth_triangle_calibration.py',
        calibration_sha256='a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873',
        C1_role=None,C1_sha256=None)
}


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def bound(path, expected):
    text = path.read_text()
    if digest(text) != expected:
        raise ValueError('The complete source input changed: '+str(path))
    return text


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Need one complete original source fragment: '+old[:100])
    return text.replace(old,new,1)


def assignment(text, name, value):
    nodes = [n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets)]
    if len(nodes) != 1:
        raise ValueError('Need one complete literal assignment: '+name)
    node,lines = nodes[0],text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+name+' = '+pprint.pformat(value,width=110,sort_dicts=False)+'\n'+''.join(lines[node.end_lineno:])


def literal(text, name):
    return next(ast.literal_eval(n.value) for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == name for t in n.targets))


def functions(text, cls=None):
    tree = ast.parse(text)
    if cls is not None:
        tree = next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name == cls)
    return {n.name:ast.dump(n,include_attributes=False) for n in tree.body if isinstance(n,ast.FunctionDef)}


def compare(before, after, allowed=(), cls=None):
    a,b = functions(before,cls),functions(after,cls)
    changed = [key for key in a if a[key] != b.get(key)]
    if any(name not in allowed for name in changed):
        raise ValueError('Changed complete mathematical implementation: '+repr(changed))
    return dict(unchanged=len(a)-len(changed),changed=changed,added=sorted(set(b)-set(a)))


NEW_BINDING = '''
def bind_outer_report_scope(raw, pure):
    """Exact NEW source/model attribution; fixed seed fees are not outer-field fees."""
    model = raw.get("representation")
    roles = raw.get("source_sha256_by_role",{})
    expected = ADAPTER_SOURCE_CONTRACT
    if (raw.get("schema") != expected["report_schema"]
            or raw.get("source_sha256") != expected["driver_sha256"]
            or pure.get("actual_driver_sha256") != expected["driver_sha256"]
            or pure.get("actual_endpoint_source_sha256") != expected["field_sha256"]
            or not isinstance(model,dict)
            or model.get("schema") != expected["field_schema"]
            or model.get("source_sha256") != expected["field_sha256"]
            or canonical(model) != raw.get("model_identity_sha256")
            or raw.get("model_identity_sha256") != pure.get("model_identity_sha256")
            or roles.get("endpoint") != expected["field_sha256"]
            or roles.get("reference_calibration") != expected["calibration_sha256"]
            or roles.get("seed_reference") != PROVIDER_SHA
            or roles.get("seed_mean") != KERNEL_SHA
            or roles.get("meridian") != "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"):
        raise ValueError("This independent fee consumer requires its exact complete NEW outer source/model")
    center = model.get("reference_centering_definition")
    attribution = pure.get("reference_centering")
    if (not isinstance(center,dict) or not isinstance(attribution,dict)
            or center.get("source_sha256") != expected["calibration_sha256"]
            or center.get("endpoint_source_sha256") != expected["field_sha256"]
            or raw.get("reference_centering_definition") != center
            or attribution.get("definition") != center
            or attribution.get("definition_identity_sha256") != canonical(center)
            or center.get("original_reference_point_sha256") != raw.get("actual_reference_initial_full_point_sha256")
            or center.get("original_reference_point_sha256") != raw.get("frozen_original_reference_point_sha256")
            or center.get("base_model_identity_sha256") != model.get("base_model_identity_sha256")
            or center.get("fixed_supported_reference_identity_sha256") != raw.get("supported_unit_seed_identity_sha256")
            or raw.get("radial_metric_error_identically_zero") is not False
            or raw.get("radial_Gram_uses_complete_hprime_Delta") is not True
            or pure.get("working_radial_metric_error_identically_zero") is not False):
        raise ValueError("Retain the exact frozen baseline and complete WORKING physical calibration scope")
    C1_identity = None
    if expected["C1_role"] is None:
        if "normal_frame_C1_reuse" in model:
            raise ValueError("A cached field cannot be relabelled as the independent plain-centred model")
    else:
        C1 = model.get("normal_frame_C1_reuse")
        if (roles.get(expected["C1_role"]) != expected["C1_sha256"]
                or not isinstance(C1,dict) or C1.get("source_sha256") != expected["C1_sha256"]
                or C1.get("complete_first_outer_parameter_derivative_retained") is not True
                or C1.get("original_normal_stages_and_implicit_matrices_retained") is not True
                or C1.get("root_or_stage_or_control_variable_deleted") is not False):
            raise ValueError("Bind the complete actual cached-C1 source and its full-stage derivative contract")
        C1_identity = canonical(C1)
    return dict(outer_report_schema=expected["report_schema"],
        outer_model_identity_sha256=raw["model_identity_sha256"],
        outer_operator_source_sha256=expected["field_sha256"],
        outer_calibration_source_sha256=expected["calibration_sha256"],
        outer_reference_centering_definition_identity_sha256=canonical(center),
        outer_frozen_original_reference_point_sha256=center["original_reference_point_sha256"],
        outer_C1_definition_identity_sha256=C1_identity,
        fixed_seed_is_not_reselected_from_current_outer_point=True,
        outer_report_identity_is_attribution_not_an_outer_error_certificate=True,
        raw_calibration_or_centered_normal_or_full_physical_lift_error_computed=False)

'''


def derive_consumer(original, contract):
    text = assignment(original,'SCHEMA','complete-'+contract['stem'].replace('_','-')+'-actual-seed-angular-node-fees-v1')
    text = assignment(text,'REQUEST_SCHEMA','actual-'+contract['stem'].replace('_','-')+'-seed-accurate-fee-request-v1')
    text = assignment(text,'READER_SHA',contract['reader_sha256'])
    text = assignment(text,'DRIVER_SHA',contract['driver_sha256'])
    text = once(text,'MEAN_VECTOR_KEYS = ',
        'ADAPTER_SOURCE_CONTRACT = '+pprint.pformat(contract,width=110,sort_dicts=False)+'\n'
        +'DERIVED_FROM_COMPLETE_R713_SOURCE_SHA256 = '+repr(ORIGINAL_FEES_SHA)+'\n'
        +'MEAN_VECTOR_KEYS = ')
    text = text.replace('read_supported_smooth_triangle_normal_lift_so3_report.py',contract['reader_name'])
    text = once(text,'def bind_actual_batch(repo, report_path, batch_index, array_override=None):',
        NEW_BINDING+'\ndef bind_actual_batch(repo, report_path, batch_index, array_override=None):')
    text = once(text,'    seed = raw["supported_unit_seed_definition"]',
        '    outer = bind_outer_report_scope(raw,pure)\n    seed = raw["supported_unit_seed_definition"]')
    text = once(text,'        complete_actual_batch_metadata=batch)',
        '        complete_actual_batch_metadata=batch,complete_outer_attribution=outer)')
    text = once(text,'    rows = request["angles"]',
        '''    if request["binding"].get("complete_outer_attribution") != binding["complete_outer_attribution"]:
        raise ValueError("Do not move fee inputs between distinct complete centred/cached representations")
    if request["binding"].get("actual_completed_batch_index") != binding["actual_completed_batch_index"]:
        raise ValueError("Keep the exact actual completed batch index in its own report")
    rows = request["angles"]''')
    text = once(text,'        external_profile_moment_errors_used=False, results=[])',
        '''        external_profile_moment_errors_used=False,
        complete_outer_source_attribution=binding["complete_outer_attribution"],
        fixed_seed_reference_fees_only=True,
        numerical_raw_reference_calibration_paid=False,
        complete_outer_normal_root_and_implicit_error_paid=False,
        complete_R715_physical_lift_and_sixjet_error_paid=False,
        outer_history_or_field_certificates_transferred=False, results=[])''')
    return text


def derive_producer(original, contract, fee_name, fee_sha):
    text = assignment(original,'SCHEMA','complete-'+contract['stem'].replace('_','-')+'-accurate-total-mean-residuals-v1')
    text = assignment(text,'JOURNAL_SCHEMA','same-'+contract['stem'].replace('_','-')+'-actual-batch-complete-integral-journal-v1')
    pins = literal(text,'PINS')
    pins['fees'] = ('scripts/resume_20261126/'+fee_name,fee_sha)
    text = assignment(text,'PINS',pins)
    text = once(text,"REFERENCE_UNIT_LAW = ",
        'DERIVED_FROM_COMPLETE_MEAN_PRODUCER_SHA256 = '+repr(ORIGINAL_MEAN_SHA)+'\nREFERENCE_UNIT_LAW = ')
    text = assignment(text,'SOURCE_SCOPE',
        'complete accurate fixed-seed candidate mean residuals for this exact centred/cached outer report and whole actual batch; '
        'not its raw calibration defect, current normal root, whole-angle cover, physical lift, metric, reach or embedding certificate')
    text = once(text,'        current_F_J_or_endpoint_roots_recomputed=False,',
        '''        current_F_J_or_endpoint_roots_recomputed=False,
        complete_outer_source_attribution=actual.actual_binding['complete_outer_attribution'],
        fixed_reference_mean_equation_is_not_actual_outer_Q_total=True,
        raw_reference_calibration_and_current_normal_fees_paid=False,
        complete_R715_physical_lift_and_sixjet_fees_paid=False,''')
    text = once(text,'                current_outer_field_or_geometry_certified=False),',
        '''                current_outer_field_or_geometry_certified=False,
                complete_outer_source_attribution=actual.actual_binding['complete_outer_attribution'],
                raw_reference_calibration_or_current_normal_error_certified=False,
                complete_R715_physical_lift_error_certified=False),''')
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--variant',choices=tuple(CONTRACTS),required=True)
    parser.add_argument('--entry-source-directory',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    a = parser.parse_args()
    repo,out = a.repo.resolve(),a.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Stage complete derived sources outside the repository')
    src = repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    original_fees = bound(src/ORIGINAL_FEES,ORIGINAL_FEES_SHA)
    original_mean = bound(src/ORIGINAL_MEAN,ORIGINAL_MEAN_SHA)
    contract = CONTRACTS[a.variant]
    actual_sources = {}
    for role in ('driver','reader','field','calibration'):
        text = bound(a.entry_source_directory/contract[role+'_name'],contract[role+'_sha256'])
        actual_sources[role] = text
    driver_pins = literal(actual_sources['driver'],'SOURCE_PINS')
    if (literal(actual_sources['driver'],'SCHEMA') != contract['report_schema']
            or literal(actual_sources['reader'],'REPORT_SCHEMA') != contract['report_schema']
            or literal(actual_sources['reader'],'DRIVER_SHA') != contract['driver_sha256']
            or literal(actual_sources['field'],'SCHEMA') != contract['field_schema']
            or literal(actual_sources['calibration'],'ENDPOINT_SCHEMA') != contract['field_schema']):
        raise ValueError('Only an actual complete source-closed new representation may be adapted')
    for role,digest_ in dict(endpoint=contract['field_sha256'],
            reference_calibration=contract['calibration_sha256'],seed_reference=PROVIDER_SHA,
            seed_mean=MEAN_SHA,meridian=BASE_SHA).items():
        if driver_pins[role][1] != digest_:
            raise ValueError('Complete new source role changed: '+role)
    if contract['C1_role'] is not None and driver_pins[contract['C1_role']][1] != contract['C1_sha256']:
        raise ValueError('The complete cached-C1 entry must bind its actual helper source')
    fee_name = contract['stem']+'_seed_angular_jet_error_bounds.py'
    mean_name = contract['stem']+'_accurate_mean_residuals.py'
    fees = derive_consumer(original_fees,contract)
    mean = derive_producer(original_mean,contract,fee_name,digest(fees))
    checks = dict(consumer=compare(original_fees,fees,{'bind_actual_batch','main'}),
        consumer_interval=compare(original_fees,fees,cls='Interval'),
        mean_top=compare(original_mean,mean,{'main'}),
        accurate_mean_batch=compare(original_mean,mean,cls='ActualMeanBatch'),
        complete_leaf_journal=compare(original_mean,mean,cls='CompleteLeafJournal'))
    out.mkdir(parents=True,exist_ok=True)
    records = {}
    for name,text in ((fee_name,fees),(mean_name,mean)):
        tree = ast.parse(text)
        compile(tree,name,'exec')
        assert len(text.encode()) < 100000
        assert all(line.rstrip() == line for line in text.splitlines())
        for node in ast.walk(tree):
            keys = ([k.value for k in node.keys if isinstance(k,ast.Constant) and isinstance(k.value,str)]
                if isinstance(node,ast.Dict) else [k.arg for k in node.keywords if k.arg is not None]
                if isinstance(node,ast.Call) else [])
            assert len(keys) == len(set(keys)),(name,getattr(node,'lineno',None))
        (out/name).write_text(text)
        records[name] = dict(bytes=len(text.encode()),sha256=digest(text))
    report = dict(schema='complete-source-bound-new-representation-seed-fee-adapters-v1',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_fee_source_sha256=ORIGINAL_FEES_SHA,original_mean_source_sha256=ORIGINAL_MEAN_SHA,
        complete_new_outer_source_contract=contract,outputs=records,static_AST_comparisons=checks,
        scientific_modules_imported=False,actual_batch_selected=False,actual_batch_or_fee_generated=False,
        proof_of_current_reference_outer_root_or_geometry_claimed=False,
        new_solver_admission_prerequisite=False)
    (out/(contract['stem']+'-fee-adapter-source-lock.json')).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
