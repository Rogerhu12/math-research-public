#!/usr/bin/env python3
"""Same original low46 mode kernels, factored and rescaled to R100 V-prime.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
The original mode-by-mode Green construction is observed before its common
supremum. Both original physical branches and all213 source/target cells
are retained. No new ODE, radial integration, or nonlinear closure claim.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import fmpq as Q


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p); b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def ex(z, side='upper'):
    if isinstance(z, (int, str)): return Q(z)
    if isinstance(z, list): return Q(int(z[0]))*Q(2)**int(z[1])
    if side in z: return ex(z[side], side)
    if 'mantissa' in z: return Q(int(z['mantissa']))*Q(2)**int(z['binary_exponent'])
    return Q(int(z['numerator']), int(z['denominator']))


def pack(z, bits=160):
    if z < 0: raise ArithmeticError('Positive factor became negative')
    if not z: return ['0', 0]
    n, d = int(z.numerator), int(z.denominator)
    e = n.bit_length()-d.bit_length()-bits+1
    if e >= 0:
        den = d << e
        m = (n+den-1)//den
    else:
        num = n << (-e)
        m = (num+d-1)//d
    result = [str(m), e]
    if ex(result) < z: raise ArithmeticError('Factor rounded inward')
    return result


def save(p, obj):
    if p.exists(): raise FileExistsError(p)
    raw = (json.dumps(obj, separators=(',', ':'))+'\n').encode()
    if p.suffix == '.gz': raw = gzip.compress(raw, compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000 or len(raw) > 1_000_000 and p.suffix != '.gz':
        raise ArithmeticError('Partition output')
    p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(raw)
    return dict(path=str(p), sha256=sha(p), bytes=len(raw))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    a = ap.parse_args(); start = time.monotonic(); ids = read(a.inputs)
    gates = {}; counts = {}; count = 0

    def gate(k, v):
        nonlocal count
        if not v: raise ArithmeticError(k)
        gates[k] = True; counts[k] = counts.get(k, 0)+1; count += 1

    def checked(k):
        r = ids[k]; gate('identity_'+k, sha(r['path']) == r['sha256'])
        return read(r['path'])

    original = checked('observed_original_q')
    usage = checked('observer_resource')
    strong = checked('original_strong_green')
    density = checked('R42_density')
    gate('formal_observer_success', usage['exitcode'] == 0 and usage['termination_signal'] is None)
    gate('original_aggregate_bitwise_identity', original['all_original_aggregate_math_fields_bitwise_identical']
         and original['original_aggregate_sha256'] == '31c65d6c8053325502542c008720f880d7386cd39168be79ca466851e76bb7ee')
    gate('original_strong_pin', ids['original_strong_green']['sha256']
         == '841c42ff527f2ca3846abf7ede8e9e03eb296a1f979cf7b01f48069197d312ac')
    gate('original_same_q_and_density_rescaling', original['original_aggregate_sha256'] in strong['input_hashes'].values()
         and ids['R42_density']['sha256'] == 'e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'
         and ids['R42_density']['sha256'] in strong['input_hashes'].values()
         and strong['rescaling']['radial_integrations'] == 0 == strong['rescaling']['linear_flow_solves'])
    modes = list(range(2, 93, 2)); cells = list(range(12, 225)); N = 213
    gate('all213_and_all46', original['cells'] == strong['cells'] == cells
         and original['modes'] == strong['modes'] == modes
         and [r['cell'] for r in strong['source_profiles']] == cells
         and [r['cell'] for r in density['rows']] == cells)
    S, Z = Q(257, 256), Q(2)**-2200
    sigma_lower = [ex(r['sigma'], 'lower') for r in strong['source_profiles']]
    source_scale = [ex(r['source_factors']['base']) for r in strong['source_profiles']]
    gate('all_positive_paid_scales', all(x > 0 for x in sigma_lower+source_scale))
    common = [[S*ex(z) for z in row] for row in strong['gamma_upper']['base']]
    common_far = [S*S*ex(z)/Z for z in strong['far_z_source_upper']['base']]
    common_boundary = [ex(row['B_low'])/S for row in strong['rows']]
    gate('complete_common_comparison', len(common) == N and all(len(r) == N for r in common)
         and len(common_far) == len(common_boundary) == N
         and all(z > 0 for row in common for z in row))
    parts = []; source_parts = []; seen = []; exceed = 0; all_improvements = []
    for part in original['modal_factor_parts']:
        path = Path(part['path']); gate('original_modal_part_pin', sha(path) == part['sha256'])
        data = read(path); source_parts.append(part); result_rows = []
        for row in data['modal_rows']:
            m = row['mode']; seen.append(m)
            gate('complete_original_modal_record', row['cells'] == cells and row['observer_only']
                 and row['no_new_ODE_or_integral'] and m in modes)
            ph = [ex(pack(S*ex(z)/sigma_lower[k])) for k, z in enumerate(row['phi_target_strong'])]
            ps = [ex(pack(S*ex(z)/sigma_lower[k])) for k, z in enumerate(row['psi_target_strong'])]
            mu = list(map(ex, row['mu_ratio']))
            ip = [ex(pack(ex(z)*source_scale[n])) for n, z in enumerate(row['base_phi_source'])]
            isp = [ex(pack(ex(z)*source_scale[n])) for n, z in enumerate(row['base_psi_source'])]
            diag = [ex(pack(S*ex(z)*source_scale[k]/sigma_lower[k])) for k, z in enumerate(row['base_ordered_diagonal'])]
            far = [min(common_far[n], ex(pack(S*S*ex(z)*source_scale[n]/Z))) for n, z in enumerate(row['far_source'])]
            boundary = [min(common_boundary[k], ex(pack(ex(z)/(S*sigma_lower[k])))) for k, z in enumerate(row['far_homogeneous'])]
            gate('all_complete_factor_rows', all(len(r) == N for r in (ph, ps, mu, ip, isp, diag, far, boundary)))
            ratio12 = None; minimum = None; maximum = None
            for k in range(N):
                for n in range(N):
                    factored = diag[k] if k == n else mu[n]*(ph[k]*isp[n] if k > n else ps[k]*ip[n])
                    gate('positive_full_mode_kernel', factored > 0)
                    if factored > common[k][n]: exceed += 1
                    used = min(factored, common[k][n])
                    ratio = used/common[k][n]
                    minimum = ratio if minimum is None else min(minimum, ratio)
                    maximum = ratio if maximum is None else max(maximum, ratio)
                    if k == 0 and n == 0: ratio12 = ratio
            result_rows.append(dict(mode=m, phi_target=list(map(pack, ph)), psi_target=list(map(pack, ps)),
                mu_ratio=list(map(pack, mu)), phi_source=list(map(pack, ip)), psi_source=list(map(pack, isp)),
                ordered_diagonal=list(map(pack, diag)), far_source_normalized_by_Z=list(map(pack, far)),
                homogeneous_far_field=list(map(pack, boundary)),
                field_rule='min(common_field_matrix[k][n], ordered_diagonal[k] if k==n else mu_ratio[n]*(phi_target[k]*psi_source[n] if k>n else psi_target[k]*phi_source[n]))',
                material='dprime=Vprime^2/(r*w)+abs(w_r/w)*Vprime^2/w',
                field_unit='same original continuous strip strong P+K / Vprime, Vprime=(257/256)*Vs',
                far_source_unit='original far z consistency, divided by Z=2^-2200; no nonlinear constant',
                far_homogeneous_unit='same original physical deep Dirichlet z parameter at width38; nonlinear far graph and its derivative must be supplied separately'))
            all_improvements.append(dict(mode=m, cell12_diagonal_over_old_common=pack(ratio12),
                smallest_vertex_ratio=pack(minimum), largest_vertex_ratio=pack(maximum)))
        out = Path(str(a.out_prefix)+f'-modes-{seen[-len(result_rows)]:03d}-{seen[-1]:03d}.json.gz')
        ref = save(out, dict(schema='R100-inner-low46-factored-source-field-kernels-part-v1', rows=result_rows))
        ref['modes'] = [r['mode'] for r in result_rows]; parts.append(ref)
        print(json.dumps(dict(event='mode_kernel_part_complete', through_mode=seen[-1], gates=count,
                              elapsed_seconds=time.monotonic()-start)), flush=True)
    gate('all46_modes_and213_squared_vertices', seen == modes and counts['positive_full_mode_kernel'] == 46*N*N)
    ans = dict(schema='same-R100-inner-low46-factored-field-kernels-v1', author='/root (GPT-6 Astra Pro, AI-assisted)',
        all_gates=True, gate_count=count, gates=gates, gate_multiplicities=counts,
        source_sha256=sha(__file__), input_manifest_sha256=sha(a.inputs), inputs=ids,
        original_mode_factor_parts=source_parts, mode_kernel_parts=parts, modes=modes, cells=cells,
        common_field_matrix=[[pack(z) for z in row] for row in common],
        common_far_source_normalized_by_Z=list(map(pack, common_far)),
        common_homogeneous_far_field=list(map(pack, common_boundary)),
        original_common_comparison_retained=True, factor_vertices_exceeding_old_common_before_min=exceed,
        per_mode_improvements=all_improvements, S=['257', -8], Z=['1', -2200],
        original_continuous_strip_origin=density['continuous_strip_origin'],
        nonlinear_constants_or_complete_source_not_preinserted=True,
        all_mean_inverse_and_true_far_still_required=True,
        no_new_ODE_or_radial_quadrature=True, no_new_field_existence_or_cut_claimed=True,
        elapsed_seconds=time.monotonic()-start, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    ref = save(Path(str(a.out_prefix)+'.json.gz'), ans)
    print(json.dumps(dict(all_gates=True, gate_count=count, primary=ref,
        factor_vertices_exceeding_common=exceed, mode92_cell12_ratio=float(ex(all_improvements[-1]['cell12_diagonal_over_old_common'])),
        elapsed_seconds=ans['elapsed_seconds'], peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__': main()
