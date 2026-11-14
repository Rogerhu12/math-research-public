#!/usr/bin/env python3
"""Use the original inlet projection on a genuinely prepared fine warm core.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This input is explicitly a complete unsolved core prepared from accepted
M32 raw parameters and the original verified M28 response increment. It is
not a fabricated finished geometry screen. The original inlet formulas and
reference chart are unchanged; profile construction is not claimed here.
"""
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
OLD=HERE/'strong_warm_core_inlet_resolution_diagnostic.py'
EXPECTED='770eb7872b17e59626f76bfbb2138aa0bbb889737007aae1951a5edc242badfa'


def main():
    original=OLD.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=EXPECTED:raise ValueError('Original complete inlet diagnostic changed')
    first=original.index('    warm,saved=read(a.warm_screen),read(a.reference)\n')
    last=original.index("    scripts=a.source_topic/",first)
    before=original[first:last]
    after='''    prepared,saved=read(a.prepared_core),read(a.reference)
    if (prepared.get('schema')!='actual-fine-complete-core-before-full-warm-geometry-v1'
            or not prepared['geometry_not_yet_run'] or prepared['nonlinear_solution']
            or not prepared['original_low_target_correction_replayed']
            or not prepared['new_fine_mode_baselines_bitwise_preserved']):
        raise ValueError('A genuinely prepared complete unsolved fine core is required')
    if (not saved.get('solver_success') or saved.get('audit_pending',True)
            or saved['angular_chart']!='general-support-core-blend-v1'
            or prepared['actual_reference_sha256']!=sha(a.reference)
            or Path(prepared['actual_reference']).resolve()!=a.reference.resolve()):
        raise ValueError('The actual fine reference chart or its SHA differs')
'''
    edits=[("('warm-screen','reference','source-topic','chart-source','original-diagnostic-source','out')",
            "('prepared-core','reference','source-topic','chart-source','original-diagnostic-source','out')"),
           (before,after),("np.asarray(warm['actual_core'],dtype=np.float64)","np.asarray(prepared['actual_complete_core'],dtype=np.float64)"),
           ('a.warm_screen,a.reference','a.prepared_core,a.reference'),
           ("warm_physical_profile=warm['warm_profile']","requested_profile_parameters_not_yet_evaluated=prepared['requested_profile_parameters']"),
           ("schema='explicit-unsolved-warm-full-core-inlet-resolution-diagnostic-v1'","schema='actual-prepared-fine-warm-core-inlet-resolution-diagnostic-v1'"),
           ("source_and_input_sha256=sources,","source_and_input_sha256=sources,original_inlet_source_sha256=EXPECTED,\n        exact_reversible_input_adapter=True,prepared_core_sha256=sha(a.prepared_core),geometry_field_computed=False,"),
           ("default=[28,32,40,64]","default=[32,40,64]"),
           ("Retain the complete original M28 support core","Retain the complete actual fine support core")]
    transformed=original
    for old,new in edits:
        if transformed.count(old)!=1:raise ValueError('Exact original input adapter site differs')
        transformed=transformed.replace(old,new,1)
    reverse=transformed
    for old,new in reversed(edits):reverse=reverse.replace(new,old,1)
    if reverse!=original:raise ValueError('An unlisted original inlet formula changed')
    ast.parse(transformed)
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_prepared_fine_inlet',EXPECTED=EXPECTED)
    exec(compile(transformed,'<same-original-inlet-with-actual-prepared-fine-core>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
