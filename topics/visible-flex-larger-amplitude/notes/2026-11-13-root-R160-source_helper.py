#!/usr/bin/env python3
"""Restrict the same finite CL, then rebuild its complete nonlinear source.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the known finite low46 centre is widened. The unknown R127 field,
its positive high tail, Green operators, axes and true boundary are unchanged.
The positive Laurent formula is the original R101 source majorant, with
32 inverse powers and the strictly positive full geometric remainder.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, arb_poly, ctx

MODES = list(range(2, 93, 2))
TAU = F(18, 125)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def ex(v):
    if isinstance(v, (F, int)):
        return F(v)
    if isinstance(v, dict):
        if 'upper' in v:
            return ex(v['upper'])
        return F(int(v['numerator']), int(v['denominator']))
    return F(int(v[0])) * F(2)**v[1] if isinstance(v[1], int) else F(int(v[0]), int(v[1]))


def ab(v):
    v = ex(v)
    return arb(v.numerator) / arb(v.denominator)


def pack(v):
    v = v if isinstance(v, arb) else ab(v)
    if not v.is_finite() or v.upper() < 0:
        raise ArithmeticError('A positive complete bound is not finite')
    u = v.upper()
    if u == 0:
        return ['0', 0]
    m, e = map(int, u.man_exp())
    shift = max(0, m.bit_length()-192)
    if shift:
        m, e = (m+(1 << shift)-1) >> shift, e+shift
    if not arb(m)*arb(2)**e >= u:
        raise ArithmeticError('Outward rounding failed')
    return [str(m), e]


def up(v):
    return ex(pack(v))


def exact(v):
    v = ex(v)
    return dict(numerator=str(v.numerator), denominator=str(v.denominator))


def shifted(p, k):
    return arb_poly([arb(0)]*k+p.coeffs())


def mass(p):
    return up(sum((p[k].upper() for k in range(len(p))), arb(0)))


def complete_source(caps, V0, degree):
    """R101 joint-pair majorant; all zero coefficients retained until output."""
    A = sum(caps, F(0))
    u, d = [arb(0)]*93, [arb(0)]*93
    for i, (m, cap) in enumerate(zip(MODES, caps)):
        v = ab(cap)/(2*(1+m))
        for k in (46+i+1, 46-i-1):
            u[k], d[k] = v, m*v
    u, d = arb_poly(u), arb_poly(d)
    q = arb(5)/4*d*d + arb(1)/4*u*u
    L = arb(5)/4*d
    mean = up(4*V0**2*A**2)
    lead = ab(V0)*L + arb_poly([arb(0)]*46+[ab(mean)])
    mean_num = 8*ab(V0*A*A)*shifted(L, 46)
    mean_num += arb_poly([arb(0)]*92+[ab(up(16*V0**2*A**4))])
    numerator = q+mean_num
    rho, numerator_mass = mass(lead), mass(numerator)
    if not 0 < rho < F(1, 2) or not V0*A < F(1, 64):
        raise ArithmeticError('Complete mean/inverse domain is not paid')
    inverse = arb_poly([arb(0)]*(degree*46)+[arb(1)])
    term = arb_poly([1])
    for k in range(1, degree+1):
        term = term*lead
        inverse += shifted(term, (degree-k)*46)
    poly = numerator*inverse
    centre = (degree+2)*46
    tail = up(ab(numerator_mass)*ab(rho)**(degree+1)/(1-ab(rho)))
    if tail <= 0:
        raise ArithmeticError('A strictly positive infinite inverse tail is required')
    pairs = [up(poly[centre+k]+poly[centre-k]) for k in range(1, centre+1)]
    return dict(centre_norm=pack(A), inverse_leading_mass=pack(rho),
                mean_zero_cap=pack(mean), numerator_mass=pack(numerator_mass),
                source_zero_before_output_projection=pack(poly[centre]),
                support_max_mode=2*centre, inverse_degree=degree,
                polynomial_pair_rows=[dict(mode=2*k+2, bound=pack(v)) for k, v in enumerate(pairs)],
                shared_complete_inverse_tail=pack(tail),
                tail_is_one_mass_for_any_joint_frequency_partition=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--inverse-degree', type=int, default=32)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Fresh immutable output required')
    if not 16 <= a.inverse_degree <= 64:
        raise ValueError('An explicit finite inverse degree is required')
    ctx.prec, ctx.threads = 512, 1
    started = time.monotonic()
    ids, data, gates = read(a.inputs), {}, {}

    def gate(name, ok):
        gates[name] = bool(ok)
        if not ok:
            raise ArithmeticError(name)

    for name, rec in ids.items():
        gate('identity_'+name, sha(rec['path']) == rec['sha256'])
        if not rec.get('source_only'):
            data[name] = read(rec['path'])
    r, ru, linear, old, full, head, lift = [data[k] for k in
        ('R153', 'R153_resource', 'linear_centre', 'R101_spectrum', 'R141', 'r6_head', 'r6_lift')]
    gate('actual_R153_complete_same_projected_field', r['all_gates'] and all(r['gates'].values())
         and r['same_existing_R124_projected_field'] and r['same_unique_R143_fixed_point_in_valid_domain']
         and ru['exitcode'] == 0 and ru['termination_signal'] is None)
    gate('true_LR_identity_and_all_modes', linear['all_gates'] and all(linear['gates'].values())
         and linear['modes'] == MODES and r['inputs']['centre']['sha256'] == ids['linear_centre']['sha256'])
    gate('same_R101_low46_centre_original_norm', old['all_gates'] and all(old['gates'].values())
         and [x['mode'] for x in old['final_caps']] == MODES
         and 'V_I' in old['centre_norm'] and 'source-x' in old['physical_source_units'])
    gate('same_R141_complete_field_and_r6_head', full['all_gates'] and all(full['gates'].values())
         and full['same_existing_R127_field'] and full['complete_mean_inverse_and_infinite_high_retained']
         and full['inputs']['new_head_export']['sha256'] == ids['r6_head']['sha256']
         and data['R141_resource']['exitcode'] == 0 and data['R141_resource']['termination_signal'] is None)
    domain, expanded = r['valid_domain'], head['domain']
    gate('explicit_actual_P_not_original_unit_domain', domain['name'] == 'R148_actual_full_cut_posterior'
         and ex(domain['S_product_radius']) == F(3,8) and ex(domain['T_l1_radius']) == F(1,64)
         and domain['simultaneous_original_coordinates'])
    gate('retained_r6_expanded_original_domain', head['all_gates'] and head['complete_mean_inverse_far']
         and lift['all_gates'] and all(lift['gates'].values())
         and expanded['name'] == 'expanded_profile'
         and ex(expanded['S_product_radius']) == F(3,4) and ex(expanded['T_l1_radius']) == F(1,32))
    gate('P_subset_r6_expanded_shared_norms',
         ex(domain['S_product_radius']) <= ex(expanded['S_product_radius'])
         and ex(domain['T_l1_radius']) <= ex(expanded['T_l1_radius']))
    for i, m in enumerate(MODES):
        gate('P_subset_original_r6_axis_'+str(m),
             ex(domain['T_coordinate_caps_by_mode'][i]) <= ex(expanded['T_coordinate_caps_by_mode'][i]))
    sigma, V0 = ex(r['original_sigma']), ex(r['original_V0'])
    gate('same_sigma_local_V_and_all92_components', sigma == F(1,64) and V0 == F(1,2**40)
         and len(r['all92_component_caps']) == 92 and ex(r['original_S']) == 8)
    caps, rows = [], []
    for i, m in enumerate(MODES):
        z = sum((ex(linear['true_linear_norms'][str(m)][c]) for c in ('P','K')), F(0))
        h = ex(r['all92_component_caps'][2*i])+ex(r['all92_component_caps'][2*i+1])
        oldcap = ex(old['final_caps'][i]['bound'])
        transferred = up(ab(z+h)*ab((TAU-sigma)*m).exp())
        cap = min(oldcap, transferred)
        gate('same_finite_CL_mode_'+str(m), 0 < cap <= oldcap and cap <= transferred)
        caps.append(cap)
        rows.append(dict(mode=m, old_tau_pair_cap=pack(oldcap), original_LR_sigma_pair=pack(z),
                         R153_error_sigma_pair=pack(h), transferred_tau_pair=pack(transferred),
                         same_CL_new_tau_pair_cap=pack(cap)))
    gate('same_complete_low_centre_below10', sum(caps,F(0)) <= sum((ex(x['bound']) for x in old['final_caps']),F(0)) < 10)
    widths = []
    for width in (TAU, TAU+1):
        wider = [up(ab(c)*ab((width-TAU)*m).exp()) for m,c in zip(MODES,caps)]
        src = complete_source(wider, V0, a.inverse_degree)
        gate('complete_known_centre_source_at_'+str(width), ex(src['shared_complete_inverse_tail']) > 0
             and ex(src['source_zero_before_output_projection']) > 0
             and src['support_max_mode'] == (a.inverse_degree+2)*92)
        widths.append(dict(width=exact(width), finite_centre_caps=list(map(pack,wider)), **src))
        print(json.dumps(dict(event='complete_known_finite_centre_source',width=str(width),
              centre_norm=float(ex(src['centre_norm'])),inverse_norm=float(ex(src['inverse_leading_mass'])),
              tail_log2_display=float(ab(ex(src['shared_complete_inverse_tail'])).log()/arb(2).log()))),flush=True)
    result = dict(schema='same-CL-P-restriction-finite-spectrum-and-complete-source-v1',
        author='/root (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        input_manifest_sha256=sha(a.inputs), inputs=ids, all_gates=all(gates.values()), gates=gates,
        gate_count=len(gates), precision_bits=ctx.prec, valid_domain=domain,
        r6_parent_domain_retained_without_relabelling=expanded, same_unique_R143_a_star_in_domain=True,
        same_CL_as_R101_R124_R127_and_R153=True, no_centre_redefinition=True,
        finite_centre_modes=MODES, original_sigma=exact(sigma), original_tau=exact(TAU),
        original_V0=exact(V0), rows=rows, widths=widths,
        physical_source_units='source-x N / ((s+|ell|) V_I^2); no extra r_x; all signed pair masses',
        full_mean_before_projection=True, positive_infinite_inverse_remainder=True,
        only_known_finite_centre_has_new_wider_source=True,
        unknown_field_or_unknown_infinite_tail_widened=False,
        original_R127_field_and_nonlow_correction_unchanged=True,
        new_ODE_or_Green_or_fixed_point=False, full_parameter_selfmap_on_P_claimed=False,
        closed_surface_or_outer9_continuation_claimed=False,
        elapsed_seconds=time.monotonic()-started, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0,compresslevel=9)
    if len(raw)>=5_000_000:
        raise ArithmeticError('Partition oversized primary')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=True,gate_count=len(gates),primary_sha256=sha(a.out),
          improved_finite_modes=sum(ex(x['same_CL_new_tau_pair_cap'])<ex(x['old_tau_pair_cap']) for x in rows),
          mode92_new=float(caps[-1]),elapsed_seconds=result['elapsed_seconds'])),flush=True)


if __name__=='__main__':
    main()
