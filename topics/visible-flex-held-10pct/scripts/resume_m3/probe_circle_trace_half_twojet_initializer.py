#!/usr/bin/env python3
"""The single predeclared half step on the failed full-twojet control ray.

Keep the new T/U finite space, full old source, first 13 controls, q/profile,
chart, original guard, projection and C2 inlet repair. Only the two physical
trace coordinates are multiplied by .5. There is no parameter scan, BVP or
actual tail solve. Completed zero-trace/primitive interface checks are reused
by their source-bound output identity; they are not rerun as new evidence.
"""
import hashlib
from pathlib import Path


SOURCE=Path(__file__).with_name('probe_circle_trace_replacement_initializer.py')
SOURCE_SHA='240019c426ee50983c1cd7b38d75147abeddb7a019774ba82b045bd73e356dce'
FULL_STEP_SHA='409d398f7e78f67fbce4ccc6e2402c66de70be72aaa201701c4f50e8e08f2df3'
text=SOURCE.read_text()
if hashlib.sha256(text.encode()).hexdigest()!=SOURCE_SHA:
    raise ValueError('The frozen full-step initializer source changed')


def replace_once(old,new):
    global text
    if text.count(old)!=1:raise ValueError('The half-step source boundary is not unique: '+old[:80])
    text=text.replace(old,new)


replace_once("    p.add_argument('--reference-run',type=Path,required=True)",
    "    p.add_argument('--reference-run',type=Path,required=True)\n"
    "    p.add_argument('--full-step-probe',type=Path,required=True)")
replace_once('    chosen[-2:]=[delta_rho,delta_h]',
    '    chosen[-2:]=.5*np.array([delta_rho,delta_h])')
replace_once('trace_coordinates=dict(t=delta_rho,u=delta_h,A=delta_rho,B=delta_h-delta_rho),',
    'trace_coordinates=dict(t=float(chosen[-2]),u=float(chosen[-1]),A=float(chosen[-2]),B=float(chosen[-1]-chosen[-2])),\n'
    '        full_twojet_trace_coordinates=dict(t=delta_rho,u=delta_h,A=delta_rho,B=delta_h-delta_rho),\n'
    '        predeclared_trace_step_factor=.5,')
replace_once("rule='Keep the first 13 raw physical coefficients; t=old rho-new base rho, u=old h-new base h. No parameter scan.',",
    "rule='Keep the first 13 raw physical coefficients; apply exactly .5 of the previous complete centre-twojet trace step. No scan or second step.',")
begin=text.index('    # A zero-trace identity checks the changed interface, not another initializer.\n')
end=text.index('    output=dict(',begin)
old_interface=text[begin:end]
new_interface='''    previous=json.loads(args.full_step_probe.read_text())
    if sha(args.full_step_probe)!=FULL_STEP_SHA:
        raise ValueError('The completed full-step identity changed')
    if (previous['actual_seed_checkpoint']['sha256']!=sha(checkpoint) or
            previous['new_core_settings']!=settings or
            previous['initialization_mapping']['trace_coordinates']!=mapping['full_twojet_trace_coordinates']):
        raise ValueError('The half step does not lie on exactly the recorded control ray')
    for path,digest in previous['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('The interface/source identity changed: '+path)
    interface=previous['interface_checks']
    reused_interface=dict(path=str(args.full_step_probe.resolve()),sha256=sha(args.full_step_probe),
        scope='The completed zero-trace, retained-jet and primitive checks are reused, not rerun.')
'''
replace_once(old_interface,new_interface)
replace_once("'probe_circle_trace_replacement_initializer.py','circle_trace_replacement_basis.py',",
    "'probe_circle_trace_replacement_initializer.py','probe_circle_trace_half_twojet_initializer.py','circle_trace_replacement_basis.py',")
replace_once('initialization_mapping=mapping,interface_checks=interface,modes=M,angular=N,',
    'initialization_mapping=mapping,interface_checks=interface,reused_interface_checks=reused_interface,modes=M,angular=N,')
replace_once("    args.out.write_text(json.dumps(output,indent=2)+'\\n')",
    "    output['half_step_source_transform']=HALF_STEP_PROVENANCE\n"
    "    args.out.write_text(json.dumps(output,indent=2)+'\\n')")
# Use the explicit half-step scope in the derived program, including its JSON.
doc_start=text.index('"""');doc_end=text.index('"""',doc_start+3)+3
text=text[:doc_start]+repr(__doc__)+text[doc_end:]
PROVENANCE=dict(parent_source=str(SOURCE.resolve()),parent_source_sha256=SOURCE_SHA,
    previous_full_step_sha256=FULL_STEP_SHA,trace_factor=.5,
    transformed_program_sha256=hashlib.sha256(text.encode()).hexdigest(),
    only_mathematical_input_change='Multiply the last two physical trace coordinates by exactly .5; all preceding controls/profile/q/core-space and original gates are retained.',
    reused_completed_checks=True,no_BVP_or_actual_tail_solve=True)
namespace=dict(__name__='__main__',__file__=str(Path(__file__).resolve()),
    FULL_STEP_SHA=FULL_STEP_SHA,HALF_STEP_PROVENANCE=PROVENANCE)
exec(compile(text,str(Path(__file__).resolve())+'::half_trace_step','exec'),namespace)
