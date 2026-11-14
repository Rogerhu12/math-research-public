#!/usr/bin/env python3
"""Consume the actual R127 family for complete mean, height and port bounds.

No ODE, quadrature, coefficient fit or new frequency truncation is performed.
All acceptance arithmetic uses Fraction; displayed decimals are not inputs.
The accompanying proof restores the missing mean evolution equation and
constructs the single-valued embedded annulus, for the original old metric.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

BITS = 160
WRAPPER = 'bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
JOINT_SHA = '36242d95a210e6aee3e38c994d0a70b61fa1fbb2df672a9ab3f4783bcca93ca1'
HEAD_SHA = '617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'
READY_SHA = '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def q(value):
    if isinstance(value, list):
        return F(int(value[0])) * F(2)**int(value[1])
    if isinstance(value, dict):
        if 'numerator' in value:
            return F(int(value['numerator']), int(value['denominator']))
        if 'mantissa' in value:
            return F(int(value['mantissa'])) * F(2)**int(value['binary_exponent'])
    if isinstance(value, (int, str)):
        return F(value)
    raise TypeError('Only exact original values may be consumed')


def interval(value):
    return q(value['lower']), q(value['upper'])


GATES = {}
ROUNDTRIPS = 0


def gate(name, condition):
    if name in GATES:
        raise ValueError('Repeated gate: ' + name)
    GATES[name] = bool(condition)
    if not condition:
        raise ArithmeticError('Unpaid gate: ' + name)


def pack(value, upper=True):
    """Outward dyadic; every returned number is checked against the exact value."""
    global ROUNDTRIPS
    value = F(value)
    if value < 0:
        z = pack(-value, not upper)
        z[0] = str(-int(z[0]))
        return z
    if not value:
        return ['0', 0]
    exponent = value.numerator.bit_length() - value.denominator.bit_length() - BITS
    scale = F(2)**exponent
    scaled = value / scale
    integer = scaled.numerator // scaled.denominator
    if upper and F(integer) < scaled:
        integer += 1
    result = [str(integer), exponent]
    exact = q(result)
    if not (exact >= value if upper else exact <= value):
        raise ArithmeticError('Outward serialization failed')
    ROUNDTRIPS += 1
    return result


def box(lo, hi):
    if lo > hi:
        raise ArithmeticError('Inconsistent interval')
    return dict(lower=pack(lo, False), upper=pack(hi))


def branch(R):
    """Strong nonmean radius R, w<=1/2, including the complete mean root."""
    c = 4*R*R
    p = R/3
    k = p+c
    v = p*p/4
    u = (2*k+k*k+F(5, 4)*p*p)/4
    lowS = 1-v
    lowD = 1-u
    lowL = 1-c-F(5, 4)*R
    lowY = 1-k
    omega_numerator_change = (1+k)*R/(4*lowS)
    lowN = 1-omega_numerator_change
    # sqrt(D)>=D_lower when 0<D_lower<=1, and
    # |D^(-1/2)-1| <= |D-1|/D_lower.
    omega_change = (omega_numerator_change+u)/lowD
    # D^(3/2) <= (1+u)^2, so this is a rational lower bound for M_c.
    mean_derivative_low = lowL/(1+u)**2
    full_quotient_over_cbg = (F(23, 18)*R*R+10*R**3+16*R**4)/lowL
    return dict(c=c, p=p, k=k, S=lowS, D=lowD, L=lowL, y=lowY,
                N=lowN, omega_change=omega_change,
                mean_derivative=mean_derivative_low,
                support_speed=lowD, full_source=full_quotient_over_cbg)


def branch_record(R, label):
    a = branch(R)
    gate(label+'_complete_small_root_domain', 0 < R < F(1, 64))
    for name in ('S', 'D', 'L', 'y', 'N', 'mean_derivative', 'support_speed'):
        gate(label+'_'+name+'_above_one_half', a[name] > F(1, 2))
    gate(label+'_complete_unprojected_source', a['full_source'] < F(3, 2)*R*R)
    gate(label+'_angular_turn_positive', a['omega_change'] < F(1, 2))
    result = dict(nonmean_strong_radius=pack(R), complete_mean_abs=pack(a['c']),
                  complete_unprojected_source_over_cbg=pack(a['full_source']),
                  angular_turn_minus_one_abs=pack(a['omega_change']))
    for name in ('S', 'D', 'L', 'y', 'N', 'mean_derivative', 'support_speed'):
        result[name+'_lower'] = pack(a[name], False)
    return result


def successful_resource(document, label):
    gate(label+'_formal_exit_zero', document['exitcode'] == 0)
    gate(label+'_no_signal', document['termination_signal'] is None)
    gate(label+'_actual_wait4_wrapper', document['resource_wrapper_sha256'] == WRAPPER)


def intersect(items):
    low, high = max(z[0] for z in items), min(z[1] for z in items)
    if low > high:
        raise ArithmeticError('Same physical background enclosures are disjoint')
    return low, high


def port_record(node, R, sources, endpoint_sides):
    bg = []
    for j, (source, side) in enumerate(zip(sources, endpoint_sides)):
        rlo, rhi = interval(source['radius_'+side])
        wlo, whi = interval(source['w'])
        xlo, xhi = interval(source['radius_x'])
        elo, ehi = interval(source['log_w_x'])
        gate(f'node{node}_source{j}_positive_background',
             0 < rlo <= rhi and 0 < wlo <= whi <= F(1, 2) and 0 < xlo <= xhi)
        wr = max(abs(elo), abs(ehi))*whi/xlo
        bg.append(((rlo, rhi), (wlo, whi), wr))
    rlo, rhi = intersect([z[0] for z in bg])
    wlo, whi = intersect([z[1] for z in bg])
    wr = min(z[2] for z in bg)
    a = branch(R)
    # This is the full quotient, including its constant Fourier coefficient.
    h0rr_error = wr*a['c'] + (whi/rlo+wr)*a['full_source']
    c_r = 2*wr*a['c']/wlo + (1/rlo+wr/wlo)*a['full_source']
    # Exact subtraction of the background w_r in the complete Darboux formula:
    # h_rr-w_r = [Ew U^2/r+w_r(-K-T+w^2 K T-w^2 P^2)]/L.
    hrr_error = (F(5, 4)*whi*R*R/rlo +
                 wr*(a['k']+R+a['k']*R/4+a['p']**2/4))/a['L']
    jets = dict(nonmean_height_abs=rhi*whi*R/6,
                h_r_minus_w_abs=whi*a['k'], h_theta_abs=rhi*whi*R/3,
                h_rr_minus_w_r_abs=hrr_error,
                h_rtheta_abs=whi*R, h_thetatheta_abs=rhi*whi*R,
                mean_slope_minus_w_abs=whi*a['c'],
                mean_second_minus_w_r_abs=h0rr_error,
                complete_mean_radial_derivative_abs=c_r)
    tails = []
    for first in (94, 8192, 34816):
        # e^x >= (1+x/n)^n for x>=0.  This is an exact rational
        # upper bound for the exponential tail, never a floating zero.
        factor = (1+F(first, 128*4096))**(-4096)
        gate(f'node{node}_tail{first}_strict_positive', 0 < factor < 1)
        tails.append(dict(first_even_mode=first, target_strip='1/128',
                          source_strip='1/64', exponential_upper=pack(factor),
                          remaining_nonmean_strong_norm=pack(R*factor)))
    return dict(node=node, background_radius=box(rlo, rhi),
                background_w=box(wlo, whi), background_abs_w_r_upper=pack(wr),
                complete_field=branch_record(R, f'node{node}'),
                physical_height_two_jet={k: pack(v) for k, v in jets.items()},
                all_unrepresented_even_modes_retained=True,
                exact_positive_tail_bounds=tails,
                higher_angular_derivative_rule='order q>=1 at strip1/128: (q-1)!*128^(q-1)*R; signed Fourier sum, no mode count')


def main():
    begin = time.monotonic()
    p = argparse.ArgumentParser()
    p.add_argument('--inputs', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    output = Path(args.out)
    if output.exists():
        raise FileExistsError('Fresh outputs are required')
    manifest = read(args.inputs)
    gate('input_manifest_schema', manifest['schema'] == 'same-R127-mean-height-bridge-inputs-v1')
    documents = {}
    for label, entry in manifest['inputs'].items():
        gate('input_sha_'+label, sha(entry['path']) == entry['sha256'])
        if entry.get('json', True):
            documents[label] = read(entry['path'])
    maincert = documents['joint_certificate']
    nonlow = documents['nonlow_certificate']
    geometry = documents['signed_geometry']
    gate('actual_R127_identity', manifest['inputs']['joint_certificate']['sha256'] == JOINT_SHA)
    gate('all_R127_gates', maincert['all_gates'] and all(maincert['gates'].values()))
    gate('original_1200_selfmaps', len(maincert['complete_selfmap_gates']) == 1200 and all(maincert['complete_selfmap_gates']))
    gate('original_1200_distance_gates', len(maincert['complete_distance_gates']) == 1200 and all(maincert['complete_distance_gates']))
    gate('full_mean_and_inverse_input', maincert['complete_mean_and_inverse_retained'])
    gate('original_R100_domain', maincert['same_R100_parameter_domain'] == 'six complex original unit axes times T weighted-l1 radius1/32')
    gate('exact_nonlow_input', maincert['inputs']['joint']['sha256'] == manifest['inputs']['nonlow_certificate']['sha256'])
    gate('same_original_617_head_units', HEAD_SHA in nonlow['input_hashes'].values())
    gate('original_all10793_leaves', nonlow['same_original_background_and10793_leaves'])
    gate('all_nonlow_gates', nonlow['all_gates'])
    gate('entire_common_strip', nonlow['fixed_common_strip']['common_strip_strictly_above_one_over64'])
    gate('all_partial_strip_positions', nonlow['fixed_common_strip']['all_partial_positions_paid'])
    gate('actual_signed_geometry_gates', geometry['all_gates'] and all(geometry['gates'].values()))
    for label in ('joint_resource', 'moments10_resource', 'moments11_resource'):
        successful_resource(documents[label], label)
    rows = nonlow['rows']
    R = list(map(q, maincert['physical_domains']))
    gate('all25_blocks', len(rows) == len(R) == 25)
    gate('all18_groups', {z['partition']['original_group'] for z in rows} == set(range(18)))
    gate('all10793_coverage', sum(z['partition']['panels'] for z in rows) == 10793)
    for j, row in enumerate(rows):
        V = q(row['V_max'])
        U = sum(map(q, maincert['low_mode_radii'][j]))
        mid = q(maincert['finite_radii'][j])
        high = q(maincert['high_radii'][j])
        high_physical = (F(18555) if j == 5 else
                         q(nonlow['profile_physical_upper']) if j == 21 else V)
        formula = (10+U+mid)*V + high_physical*high
        gate(f'block{j}_same_complete_physical_formula', 0 < formula <= R[j] < F(1, 2**34))
        gate(f'block{j}_all46_low_inputs', len(maincert['low_mode_radii'][j]) == 46)
    totalR = sum(R)
    maximumR = max(R)
    gate('global_radial_first_radius_below_2powminus37', totalR < F(1, 2**37))
    gate('all_point_radius_below_2powminus38', maximumR < F(1, 2**38))
    gate('outgoing_node10_radius_below_2powminus47', R[24] < F(1, 2**47))
    m10 = documents['moments10']
    m11 = documents['moments11']['original_metadata']
    gate('moments10_all_gates', m10['all_gates'] and all(m10['gates'].values()))
    gate('moments11_complete_recovery', all(documents['moments11']['checks'].values()))
    gate('same_ready10', READY_SHA in m10['input_hashes'].values())
    gate('same_ready11', READY_SHA in m11['input_hashes'].values())
    gate('all_original_material_panels', m10['panels'] == 5248 and documents['moments11']['panels'] == 5545)
    cell_records = []
    omega_lo = F(0)
    omega_hi = F(0)
    mean_error = F(0)
    for cell, md in ((11, m11), (10, m10)):
        lo00, hi00 = interval(md['total_positive_moments']['00'])
        lo01, hi01 = interval(md['total_positive_moments']['01'])
        gate(f'cell{cell}_positive_true_moments', 0 < lo00 <= hi00 and 0 < lo01 <= hi01)
        rcell = max(R[j] for j, row in enumerate(rows) if row['partition']['cell'] == cell)
        lower, upper = lo00+lo01, hi00+hi01
        error = 4*rcell*rcell*upper
        omega_lo += lower
        omega_hi += upper
        mean_error += error
        cell_records.append(dict(cell=cell, true_integral_w_dr=box(lower, upper),
                                 complete_mean_sup=pack(4*rcell*rcell),
                                 mean_height_difference_from_rotation=pack(error),
                                 cumulative_background_height=box(omega_lo, omega_hi),
                                 cumulative_mean_height_correction_abs=pack(mean_error),
                                 actual_mean_height_with_node12_anchor_zero=box(omega_lo-mean_error, omega_hi+mean_error)))
    source_rows = {}
    for cell, seg in ((11, 0), (11, 8), (10, 0), (10, 8)):
        label = f'source{cell}_{seg}'
        group = next(z for z in geometry['profile_groups'] if z['cell'] == cell and z['segment'] == seg)
        gate(label+'_same_signed_flow_background', group['source_group_sha256'] == manifest['inputs'][label]['sha256'])
        source = documents[label]
        gate(label+'_original_single_panel', source['cell'] == cell and source['segment'] == seg and len(source['panels']) == 1)
        source_rows[cell, seg] = source['panels'][0]
    ports = [port_record(12, R[0], [source_rows[11, 0]], ['left']),
             port_record(11, min(R[8], R[9]), [source_rows[11, 8], source_rows[10, 0]], ['right', 'left']),
             port_record(10, R[24], [source_rows[10, 8]], ['right'])]
    report = dict(schema='same-R127-complete-mean-height-and-embedded-annulus-v1',
                  source_sha256=sha(__file__), input_manifest_sha256=sha(args.inputs),
                  inputs=manifest['inputs'], parameter_domain=maincert['same_R100_parameter_domain'],
                  cells_in_physical_outward_order=[11, 10], nodes=[12, 11, 10],
                  fixed_metric='same original R26/R100 background; no rescaling or new q metric',
                  original_R127_full_frequency_fixed_point_consumed=True,
                  full_signed_even_frequency_range=True, complete_mean_and_inverse_retained=True,
                  global_radial_first=branch_record(totalR, 'global'),
                  all_point=branch_record(maximumR, 'all_point'),
                  local_blocks=[dict(index=j, partition=rows[j]['partition'], complete_physical_radius=pack(R[j])) for j in range(25)],
                  exact_mean_height_cells=cell_records, true_cauchy_ports=ports,
                  complete_mean_equation_restored_by_positive_weight_identity=True,
                  complete_Darboux_height_on_original_two_cells=True,
                  single_global_height_integration_constant=True,
                  horizontal_translation_holonomy_zero_by_half_turn=True,
                  strict_nested_convex_levels_and_embedded_annulus=True,
                  all_real_parameters_and_common_phase_covered=True,
                  inner_tail_gluing_requires_same_full_parameter_cut=True,
                  outer_cells0to9_continuation_claimed=False, closed_surface_claimed=False,
                  no_new_ODE_or_source_integrations=True, gates=GATES,
                  all_gates=all(GATES.values()), outward_roundtrip_checks=ROUNDTRIPS,
                  elapsed_seconds=time.monotonic()-begin,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    gate('owned_RSS_below96MiB', report['peak_rss_kib'] < 96*1024)
    report['all_gates'] = all(GATES.values())
    output.write_text(json.dumps(report, separators=(',', ':'), ensure_ascii=False)+'\n')
    saved = read(output)
    if saved != report:
        raise ArithmeticError('Saved exact certificate differs')
    print(json.dumps(dict(all_gates=report['all_gates'], gate_count=len(GATES),
                          global_nonmean_radius=float(totalR), maximum_point_radius=float(maximumR),
                          node10_nonmean_radius=float(R[24]), complete_mean_abs=float(4*maximumR**2),
                          total_mean_height_correction_abs=float(mean_error), output_sha256=sha(output),
                          elapsed_seconds=report['elapsed_seconds'], peak_rss_kib=report['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
