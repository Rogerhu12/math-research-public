#!/usr/bin/env python3
"""Actual wide entry: whole original cells9..7 homogeneous infinite tail.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the existing full trace and existing complete positive frame budget
are consumed. No ODE, source integral, or nonlinear tube is inferred.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx, fmpq


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def dy(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    if 'upper' in v:
        return dy(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def ar(v):
    return arb(fmpq(v.numerator, v.denominator))


def endpoint(v, upper=True):
    y = v.upper() if upper else v.lower()
    if not y.is_finite():
        raise ArithmeticError('Finite outward endpoint required')
    m, e = y.man_exp()
    return [str(m), int(e)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    if a.out.exists():
        raise FileExistsError('Preserve each actual output')
    ctx.prec, ctx.threads = 256, 1
    started = time.monotonic()
    ids = read(a.inputs)
    gates = {}

    def gate(name, v):
        gates[name] = bool(v)
        if not v:
            raise ArithmeticError(name)

    for name, rec in ids.items():
        gate('identity_' + name, sha(rec['path']) == rec['sha256'])
    get = lambda k: read(ids[k]['path'])
    wide, phase = get('R163'), get('phase')
    joint, block, sources, oldids = (get(k) for k in
                                    ('original_nonlow', 'block24', 'low_sources', 'R160_inputs'))
    for k in ('R163_resource', 'phase_resource'):
        r = get(k)
        gate('actual_owned0_' + k, r['exitcode'] == 0 and r['termination_signal'] is None)
    gate('same_actual_full_field', wide['all_gates'] and all(wide['gates'].values())
         and wide['actual_complete_new_width_nonlow_field']
         and wide['same_original_actual_full_field_identified']
         and wide['complete_mean_inverse_far_and_shared_T_retained']
         and not wide['old_unknown_infinite_caps_reweighted'])
    gate('full_original_phase_paid', phase['all_gates'] and all(phase['gates'].values())
         and phase['original_material_panels'] == 14069
         and [r['cell'] for r in phase['cells']] == [9, 8, 7]
         and phase['whole_radial_first_output_norm'])
    gate('same_original_nonlow_source', wide['inputs']['R160_inputs']['sha256'] == ids['R160_inputs']['sha256']
         and oldids['nonlow']['sha256'] == ids['original_nonlow']['sha256']
         and oldids['low_sources']['sha256'] == ids['low_sources']['sha256'])
    gate('same_complete_localV_and_strip', joint['all_gates'] and all(joint['gates'].values())
         and sources['all_gates'] and all(sources['gates'].values())
         and wide['comparison_partition'] == joint['comparison_partition'] == sources['comparison_partition']
         and sources['source_records'][24]['sha256'] == ids['block24']['sha256'])
    row = joint['rows'][24]
    gate('whole_node10_last_block', block['index'] == row['index'] == 24
         and row['partition']['cell'] == 10 and row['partition']['segment'] == 8
         and row['partition']['first_panel'] == 0 and row['partition']['last_panel_exclusive'] == 1
         and row['high_space'] == 'physical_localV' and joint['high_cutoff'] == 34816)
    shift = F(wide['angular_shift'])
    sigma0 = F(int(block['sigma_min'][0]), int(block['sigma_min'][1])) + shift
    sigma = F(1, 64)
    gamma = dy(phase['complete_phase'])
    D = dy(phase['complete_nonnegative_diagonal']) + dy(phase['complete_nonnegative_frame_jumps'])
    bmin, bmax = dy(phase['minimum_frame']), dy(phase['maximum_frame'])
    convert = 2 * max(F(1), bmax) * max(F(1), 1 / bmin)
    gate('same_conservative_whole_radial_conversion', bmin > 0 and bmin <= 1
         and convert <= dy(phase['all_suffix_physical_conversion']))
    delta = sigma0 - sigma - gamma
    gate('positive_actual_entry_strip_reserve', delta > 0 and shift == F(2, 5))
    V = dy(row['V_max'])
    r, h = dy(wide['finite_caps'][24]), dy(wide['high_caps'][24])
    gate('complete_positive_actual_entry_masses', min(V, r, h) > 0)
    common = ar(convert) * ar(D).exp()
    outputs = []
    for cutoff in (8192, 16384, 24576, 28672, 32768, 34816):
        # Below the old high cutoff, restriction of the entire finite mass
        # is valid but deliberately coarse; no spectral split is invented.
        initial = V * (r + h if cutoff < 34816 else h)
        bound = common * ar(initial) * (-cutoff * ar(delta)).exp()
        gate('positive_full_infinite_mass_' + str(cutoff), bound.is_finite() and bound > 0)
        outputs.append(dict(minimum_physical_even_mode=cutoff,
            whole_original9to7_homogeneous_strong_sigma1over64=endpoint(bound),
            bound_log2_upper=endpoint(bound.log() / arb(2).log()),
            initial_physical_strong_mass=endpoint(ar(initial)),
            below_one_sixteenth=bool(bound < arb(1) / 16),
            input_is_whole_high=bool(cutoff == 34816),
            complete_infinite_sum_not_truncated=True))
    gate('whole_true_high_homogeneous_is_small', outputs[-1]['below_one_sixteenth'])
    out = dict(schema='actual-R163-wide-entry-original9to7-homogeneous-tail-v1',
        author='/root (GPT-6 Astra Pro; AI-assisted)', inputs=ids,
        input_manifest_sha256=sha(a.inputs), source_sha256=sha(__file__),
        all_gates=all(gates.values()), gates=gates, precision_bits=ctx.prec,
        same_real_R143_fixed_point=True, actual_R163_trace=True,
        parameter_domain=wide['parameter_domain'], original_blocks=[9, 8, 7],
        original_material_panels=14069,
        entry_strip_lower={'numerator': str(sigma0.numerator), 'denominator': str(sigma0.denominator)},
        output_strip='1/64', angular_reserve={'numerator': str(delta.numerator), 'denominator': str(delta.denominator)},
        whole_nonnegative_phase=phase['complete_phase'],
        whole_diagonal_plus_frame_cost=endpoint(ar(D)),
        physical_input_output_conversion=endpoint(ar(convert)),
        actual_localV_upper=row['V_max'], actual_entry_high_radius=wide['high_caps'][24],
        estimates=outputs, strong_to_strong_no_extra_angular_derivative=True,
        no_new_ODE_or_background_quadrature=True,
        complete_nonlinear_feedback_still_unpaid=True,
        outer_complete_nonlinear_solution_claimed=False, closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps(dict(primary=str(a.out), sha256=sha(a.out), all_gates=out['all_gates'],
        gate_count=len(gates), estimates=[dict(mode=z['minimum_physical_even_mode'],
            log2=float(ar(dy(z['bound_log2_upper'])))) for z in outputs],
        elapsed_seconds=out['elapsed_seconds'], peak_rss_kib=out['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
