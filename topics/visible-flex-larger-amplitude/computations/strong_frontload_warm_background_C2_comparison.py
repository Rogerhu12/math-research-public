#!/usr/bin/env python3
"""Complete binary-background radius comparison for an actual frontload warm.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Fresh, reversible adaptation of the previously executed complete binary-
background comparison. The input is explicitly a completed unsolved warm.
The degree23 stored Bernstein radius replaces only the original first cubic
Hermite radius; all subsequent split Gauss64/phase/repair formulas remain
unchanged. Original angle, pulse, then corrected frontload hooks are installed
in that order. No original candidate, target g or active BVP is modified.
"""
import ast
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_binary_background_C2_comparison.py'
ORIGINAL_SHA='483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08'

def main():
    original=ORIGINAL.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=ORIGINAL_SHA:
        raise ValueError('Frozen full background source changed')
    edits=[]
    def add(before,after,count=1):
        if original.count(before)!=count:
            raise ValueError('Frozen edit count differs: '+before[:100])
        edits.append((before,after,count))
    olddoc=ast.get_docstring(ast.parse(original),clean=False)
    add('"""'+olddoc+'"""',json.dumps(__doc__))
    add("TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'",
        "PINS.update({\n"
        "    'strong_initial_speed_pulse.py':'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',\n"
        "    'strong_monotone_initial_speed.py':'12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',\n"
        "    'strong_monotone_initial_speed_anchor.py':'583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',\n"
        "})\n"
        "TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'")
    add("    p.add_argument('--accepted', type=Path, nargs='+', required=True)",
        "    p.add_argument('--warm-screen', type=Path, required=True)\n"
        "    p.add_argument('--warm-resource', type=Path, required=True)\n"
        "    p.add_argument('--first-piece-certificate', type=Path, required=True)")
    add("    spec.loader.exec_module(provider)\n    actual_table =",
        "    spec.loader.exec_module(provider)\n"
        "    check('original_angle_hook_precedes_initial_laws', getattr(provider,'_strong_angle_boost_installed',False))\n"
        "    import strong_initial_speed_pulse as pulse_hook\n"
        "    import strong_monotone_initial_speed_anchor as frontload_hook\n"
        "    pulse_hook.install(provider)\n"
        "    frontload_hook.install(provider)\n"
        "    actual_table =")
    add("    for accepted_path in a.accepted:","    for accepted_path in [a.warm_screen]:")
    before="""        cfg = saved['frozen_profile']
        check('actually_accepted_original_profile', saved['solver_success'] and not saved.get('audit_pending',True) and
              saved['config']['actual_nonlinear_tail'] and saved['physical_port_sha256'] == sha(a.port))
        check('original_zero_optional_initial_laws', float(cfg.get('initial_speed_frontload',0)) == 0 and
              float(cfg.get('initial_speed_pulse',0)) == 0 and cfg['boost_law'] == 'angle')
"""
    after="""        cfg = saved['warm_profile']
        owned=read(a.warm_resource)
        first=read(a.first_piece_certificate)
        chart_path=Path(saved['geometry_fields']['actual_exact_chart_order_bridge']['path'])
        chart=read(chart_path)
        warm_physical_length=chart['actual_physical_breaks'][-1]
        check('actually_completed_unsolved_warm', saved['finished'] and saved['finite_domain_passed'] and
              not saved['nonlinear_solution'] and not saved['true_new_H_tail_evaluated'] and
              saved['worker_start_attempts']==0 and owned['exitcode']==0 and owned['wait4_observed'] and
              owned['termination_signal'] is None and
              owned['command'][owned['command'].index('--inspect-warm-output')+1]==str(a.warm_screen))
        check('complete_same_actual_chart_and_first_piece', chart['physical_profile']==cfg and
              sha(chart_path)==saved['geometry_fields']['actual_exact_chart_order_bridge']['sha256'] and
              first['all_gates'] and first['actual_profile']==cfg and
              first['input_kind']=='completed-unsolved-warm' and
              sha(a.warm_screen) in first['input_sha256'].values())
        check('actual_nonzero_frontload_domain', 0<float(cfg.get('initial_speed_frontload',0))<=1 and
              float(cfg.get('initial_speed_pulse',0))==0 and cfg['boost_law']=='angle')
        for source_path in (a.warm_resource,a.first_piece_certificate,chart_path):
            input_ids[str(source_path)]=sha(source_path)
"""
    add(before,after)
    add("saved['meridian_length']","(warm_physical_length)",3)
    start=original.index("            if seg['kind'] == 'hermite':\n")
    end=original.index("            pp = phase_pieces(seg)\n",start)
    before=original[start:end]
    after="""            if seg['kind'] == 'hermite':
                check('only_actual_first_frontload_piece', index==0 and s0==0 and h==L and
                      seg.get('strong_initial_speed_frontload',0)==cfg['initial_speed_frontload'])
                controls=list(map(binary,seg['strong_initial_speed_frontload_radius_controls']))
                n=len(controls)-1
                data=first['exact_provider_first_piece_data']
                check('same_stored_frontload_controls', n==23 and all(seg[k]==v for k,v in data.items()) and
                      L==F(first['exact_binary_length']['numerator'])/F(first['exact_binary_length']['denominator']))
                derivatives=[controls]
                for order in range(2):
                    derivatives.append([F(n-order)*(y-x)/h for x,y in zip(derivatives[-1],derivatives[-1][1:])])
                left=[aq(values[0]) for values in derivatives]
                right=[aq(values[-1]) for values in derivatives]
                rlo,rhi=aq(min(controls)).lower(),aq(max(controls)).upper()
                vcap=aq(max(map(abs,derivatives[1]))).upper()
                acap=aq(max(map(abs,derivatives[2]))).upper()
                check('whole_first_polynomial_radius_speed_domain', rlo>0 and vcap<1 and n==23)
                pieces.append({'segment':index,'phase_piece':0,'physical_left':s0,'physical_right':s0+h,
                    'left':left,'right':right,'radius_lower':rlo,'radius_upper':rhi,
                    'first_absolute_upper':vcap,'second_absolute_upper':acap,
                    'Gauss_first_second_error':[arb(0),arb(0)],'constructor_rate_discrepancy':arb(0)})
                continue
"""
    add(before,after)
    add("'accepted_primary_sha256'","'completed_warm_screen_sha256'",2)
    add("'accepted_primary':str(accepted_path)","'completed_warm_screen':str(accepted_path)")
    add("'accepted':str(accepted_path)","'completed_warm':str(accepted_path)")
    add("Hermite radius is the exact polynomial.","Frontload radius is the exact stored degree23 Bernstein polynomial.")
    add("'schema':'actual-binary-background-piecewise-primitive-explicit-C2-comparison-v1'",
        "'schema':'actual-unsolved-frontload-binary-background-explicit-C2-comparison-v1',\n"
        "        'input_kind':'completed-unsolved-warm', 'accepted_new_solution':False,\n"
        "        'frozen_background_parent_sha256':FROZEN_BACKGROUND_PARENT_SHA,\n"
        "        'explicit_initial_law_source_identity':frontload_hook.source_identity(),\n"
        "        'exact_reversal_of_all_listed_adaptations':True")
    source=original
    for before,after,count in edits:
        if source.count(before)!=count:raise ValueError('Overlapping adaptation changed a frozen site')
        source=source.replace(before,after)
    ast.parse(source)
    reverse=source
    for before,after,count in reversed(edits):
        if reverse.count(after)!=count:raise ValueError('Reversal edit count differs')
        reverse=reverse.replace(after,before)
    if reverse!=original:raise ValueError('Unlisted original background change')
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_unsolved_frontload_background',
                   FROZEN_BACKGROUND_PARENT_SHA=ORIGINAL_SHA)
    exec(compile(source,'<actual-unsolved-frontload-background-C2>','exec'),namespace)
    namespace['main']()

if __name__=='__main__':main()
