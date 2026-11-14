#!/usr/bin/env python3
"""Retain all fine warm samples with a proved binary-chart ordering bridge.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original raw physical knots must remain strictly increasing in Float64.
Only a displayed equality between two common-grid values can use an exact
same-piece binary-polynomial comparison. No point is moved, discarded or
replaced, and no physical candidate parameter changes. The full mean and
geometric formulas remain the original ones. This is a finite warm diagnostic;
it is not a continuous floating-chart or closed-surface certificate.
"""
from fractions import Fraction as F
import hashlib
import inspect
import json
from pathlib import Path
import sys
import textwrap

HERE = Path(__file__).resolve().parent
PINS = {
    'root_actual_geometry_field_complete_mean.py':
        '614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86',
    'root_actual_coarse_increment_geometry_complete_mean.py':
        'c986073622d4ebabb2be7d1eea46fe8ac4966a404b56bbc6a6af3b48371092bc',
    'root_actual_warm_chart_orientation_probe.py':
        'cd9aedc0edc0b3d13dcc4bd4724c386b0f5ddb847fa0317f9e4b16c559e88868',
}
HEIGHT_FUNCTION_SHA = 'ad9ba92e667ebbf572c6d31622959b804aba482d506e6523a7538e33569cd282'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def binary(value):
    return F.from_float(float(value))


def exact(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def chart_order(obj, x, t, flow, parameters, output, physical_nodes, physical_grid):
    import numpy as np
    from root_actual_warm_chart_orientation_probe import probe
    from root_neck_chart import NeckChart
    if (not np.isfinite(physical_nodes).all() or not np.isfinite(physical_grid).all()
            or not np.all(np.diff(physical_nodes) > 0)
            or not np.all(np.diff(physical_grid) >= 0)):
        raise ValueError('Original raw strict chart gate or common nondecreasing values failed')
    proof_path = output.with_name(output.stem+'-exact-chart-order.json')
    if proof_path.exists():
        raise FileExistsError('Fresh exact chart-order proof required')
    probe(obj, x, t, flow, parameters, proof_path)
    proof = json.loads(proof_path.read_text())
    bad = proof['grid_nonpositive_spacings']
    if (not proof['raw_strict_increase'] or
            not proof['all_exact_binary_polynomial_piece_derivatives_positive'] or
            any(row['displayed_ds'] != 0. or not row['same_piece_strict_positive_exact_ds']
                for row in bad)):
        raise ValueError('A nonpositive common-grid comparison lacks the exact same-piece bridge')

    # Interpret every stored binary chart coefficient as its exact rational.
    # This verifies complete sample ordering, not arbitrary seam continuity.
    chart = NeckChart(obj._neck_knots, flow.breaks)
    v, w, r = chart.v[:-1], chart.v[1:], chart.r
    c3 = 10*r-6*v-4*w
    c4 = -15*r+8*v+7*w
    c5 = 6*r-3*v-3*w

    def exact_values(points):
        answer = []
        for z in points:
            j = int(np.clip(np.searchsorted(chart.t, z, side='right')-1, 0, len(chart.h)-1))
            u = (binary(z)-binary(chart.t[j]))/binary(chart.h[j])
            answer.append(binary(chart.s[j])+binary(chart.h[j])*(binary(v[j])*u+
                binary(c3[j])*u**3+binary(c4[j])*u**4+binary(c5[j])*u**5))
        differences = [b-a for a, b in zip(answer, answer[1:])]
        if not differences or min(differences) <= 0:
            raise ValueError('Complete exact binary-polynomial sample ordering failed')
        return dict(points=len(answer), exact_adjacent_pairs=len(differences),
                    all_strict=True, minimum_exact_spacing=exact(min(differences)))

    raw_order, common_order = exact_values(x), exact_values(t)
    height = textwrap.dedent(inspect.getsource(flow.height_integral.__func__))
    if hashlib.sha256(height.encode()).hexdigest() != HEIGHT_FUNCTION_SHA:
        raise ValueError('The reviewed raw-cell positive Gauss6 height method changed')
    proof.update(actual_exact_order_adapter=dict(source_sha256=sha(__file__),
        original_sources=PINS, height_function_sha256=HEIGHT_FUNCTION_SHA,
        raw_physical_float_knots_remain_strict=True,
        raw_exact_binary_polynomial_sample_order=raw_order,
        common_exact_binary_polynomial_sample_order=common_order,
        displayed_equal_pairs=len(bad), exact_same_piece_ties_all_positive=True,
        no_input_t_physical_s_raw_state_or_parameter_changed=True,
        both_displayed_equal_samples_retained=True,
        cubic_knots_only_original_strict_raw_nodes=True,
        geometry_jets_are_analytic_cubic_derivatives_not_common_grid_differences=True,
        Gauss6_full_widths_only_original_raw_intervals=True,
        partial_Gauss6_widths_multiply_only_and_are_not_derivative_denominators=True,
        no_common_grid_adjacent_s_difference_used_as_a_denominator=True,
        original_float_strict_common_gate_would_pass=not bad,
        arbitrary_binary_polynomial_seam_continuity_not_claimed=True,
        continuous_chart_alignment_error_not_certified=True))
    proof_path.write_text(json.dumps(proof, indent=2)+'\n')
    return dict(path=str(proof_path), sha256=sha(proof_path),
        source_sha256=sha(__file__), exact_binary_sample_order_passed=True,
        original_raw_float_gate_preserved=True, displayed_equal_pairs=len(bad),
        complete_common_grid_points_retained=len(t), exact_common_pairs=len(t)-1,
        derivative_denominators_do_not_use_common_grid_differences=True,
        continuous_chart_or_alignment_certificate=False)


def main():
    for name, wanted in PINS.items():
        if sha(HERE/name) != wanted:
            raise ValueError('Reviewed original finite warm source changed: '+name)
    import root_actual_geometry_field_complete_mean as geometry
    import root_actual_coarse_increment_geometry_complete_mean as fine
    original = inspect.getsource(geometry.main)
    before = "        if not np.all(np.diff(physical_nodes) > 0) or not np.all(np.diff(physical_grid) > 0):\n            raise ValueError('The physical chart lost orientation')\n"
    after = "        exact_chart_order_record = verified_exact_chart_order(\n            obj,x,t,flow,p,output,physical_nodes,physical_grid)\n"
    metadata_before = "                wrapper_sha256=sha(__file__), signed_normal='Fs cross F_eta',\n"
    metadata_after = "                wrapper_sha256=sha(__file__), signed_normal='Fs cross F_eta',\n                actual_exact_chart_order_bridge=exact_chart_order_record,\n"
    source = original
    for old, new in ((before, after), (metadata_before, metadata_after)):
        if source.count(old) != 1:
            raise ValueError('Original geometry source anchor changed')
        source = source.replace(old, new, 1)
    if source.replace(metadata_after, metadata_before, 1).replace(after, before, 1) != original:
        raise ValueError('A geometric or mean formula changed beyond the declared order bridge')
    namespace = dict(geometry.main.__globals__, verified_exact_chart_order=chart_order)
    exec(compile(source, '<original-fine-geometry-with-exact-binary-chart-order>', 'exec'), namespace)
    previous = geometry.main
    geometry.main = namespace['main']
    try:
        fine.main()
    finally:
        geometry.main = previous
    index = sys.argv.index('--inspect-warm-output')
    path = Path(sys.argv[index+1])
    report = json.loads(path.read_text())
    if (not report['finite_domain_passed'] or
            not report['geometry_fields']['actual_exact_chart_order_bridge']['exact_binary_sample_order_passed']):
        raise ValueError('The completed full field did not retain its exact chart bridge')
    report['source_sha256'][str(Path(__file__).resolve())] = sha(__file__)
    report['actual_fine_geometry_exact_chart_order_adapter'] = dict(
        source_sha256=sha(__file__), original_sources=PINS,
        original_geometry_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        executed_geometry_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_geometry_main=True,
        actual_physical_parameters_and_all_sampling_coordinates_unchanged=True,
        all_original_mean_and_geometry_formulas_unchanged=True,
        original_raw_orientation_and_all_other_domain_gates_preserved=True,
        exact_binary_sample_order_substitutes_for_float_ties_only=True,
        original_float_grid_rejection_is_preserved_separately=True,
        new_solution_fine_Jacobian_or_continuous_geometry_claimed=False)
    temporary = path.with_name(path.name+'.exact-chart-provenance.tmp')
    temporary.write_text(json.dumps(report, indent=2)+'\n')
    temporary.replace(path)
    print(json.dumps(dict(event='actual_fine_complete_mean_exact_chart_bridge_finished',
        path=str(path), sha256=sha(path), original_mean_and_field_formulas_unchanged=True)), flush=True)


if __name__ == '__main__':
    main()
