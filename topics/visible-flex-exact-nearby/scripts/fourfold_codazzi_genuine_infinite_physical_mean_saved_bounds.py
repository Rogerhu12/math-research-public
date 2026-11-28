"""Whole-source admission and new exact GMI bounds on the infinite physical mean."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import fourfold_codazzi_negative_circle_inverse_saved_bounds as jcr

FILES = {
    'W': ('notes/whole_root_signed_reference_Taylor_ci/run-43694458725-1/execution.json', 39214, '777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1'),
    'Ws': ('scripts/fourfold_codazzi_whole_root_signed_reference_Taylor.py', 42067, 'a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be'),
    'Wm': ('notes/2026-11-15-R133-whole-root-signed-reference-Taylor-CI-inputs.json', 25430, '11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65'),
    'Ww': ('scripts/fourfold_codazzi_whole_root_signed_reference_Taylor_public_worker.py', 18332, '599ce272ecd4b54ab8d7e1e40eb7d783e48f847d5b990cb7806b1d997c2c4786'),
    'V': ('notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json', 27645, 'd4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9'),
    'Vs': ('scripts/fourfold_codazzi_common_radial_potential_budget.py', 30953, '042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7'),
    'Vm': ('notes/2026-11-15-R133-common-radial-potential-budget-CI-inputs.json', 11519, '44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437'),
    'Vw': ('scripts/fourfold_codazzi_common_radial_potential_budget_public_worker.py', 17311, 'f67fa3f9b63834715d0aa7711bee2e836979c55dacd3c83055c09dfd035e2cd0'),
    'JCR': ('notes/2026-11-28-JCR-new-actual-root-circle-rational-comparisons.json', 1796, '73907a2fb13c0db588e599d5ce8b0c3e83760b29c75d9c11b2fdc0e245e53a00'),
    'JCRs': ('scripts/fourfold_codazzi_negative_circle_inverse_saved_bounds.py', 8433, 'e28a39e6a5380000f229022ebe8d354ec80f14d63f1d82d92feaf44de72cbfde'),
    'JCRproof': ('results/R149-supplement-uniform-negative-circle-inverse-through-the-true-root.md', 4910, '829a32a09c4c88a2d5f2107e902bf0bdd440e4d1911854f20b435840fe5f545b'),
    'GNF': ('results/R149-supplement-complete-root-collar-nonlocal-source-with-both-physical-circle-inverses.md', 13815, 'a860d28794587b24c33daafb10b4b5257c7d6f836707a5bb00fe98f88bfacd23'),
    'G16': ('results/R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md', 22688, 'c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e'),
    'oldproduct': ('results/R133-supplement-old-root-product-and-separated-first-Airy-amplitude-budgets.md', 13623, 'fca8fcdda1d284011b540535d494f8f81dbdb8fd83e03ca8540496d0274fafa3'),
    'GAF': ('results/R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md', 5756, 'fcc7a1f89447bb1d6e6c7ea0013a1962d4e61cccb15e6048e45ec99ebdf7e925'),
    'WUA': ('results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md', 40111, '9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad'),
    'PW': ('results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md', 16459, '246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562'),
    'SP': ('notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json', 35259, 'a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12'),
    'WEA': ('notes/paid_waist_strong_error_assembly_ci/run-43769746581-1/actual-scientific-conclusion.json', 18532, '3d73b56f604b012b66f2f502aea481b59383f5566fb5d12c676843220d39956a'),
    'WEAp': ('notes/paid_waist_strong_error_assembly_ci/run-43769746581-1/execution.json', 12841, '8c1cc71fd5ae792695fe809f561512e2e426e8de8552b7b200a10fe8616fadc6'),
    'GSW': ('results/R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md', 5769, '34bccc6e9822771767527918644498e6fcf49b089ec64db6c480b8bf0ef627a9'),
    'GSWr': ('notes/2026-11-28-GSW-root-new-rational-comparisons.json', 2106, 'ff2ff7a331577081711097cfa7f0a0275824a486b48a4336f248478e1da50218'),
    'GMI': ('results/R149-supplement-infinite-genuine-physical-mean-through-iterated-circle-derivatives.md', 7826, 'bf469cb1adf5b94f2c86335d6bd7c9440489ed0569637fadae6cb6ad305c51b7'),
}


def require(ok, label):
    if not ok:
        raise ValueError(label)


def whole(topic):
    documents = {}
    for role, (name, size, digest) in FILES.items():
        raw = (topic / name).read_bytes()
        require((len(raw), sha256(raw).hexdigest()) == (size, digest), role)
        if name.endswith('.json'):
            documents[role] = json.loads(raw)
    return documents


def historical(docs, role, run, event, count, gates, native, process):
    e = docs[role]
    r = e['actual_scientific_receipt']
    require(e['run_id'] == run and e['run_attempt'] == '1' and e['workflow_commit'] == event
            and e['complete'] and r['complete'] and r['proved']
            and e['actual_returncode'] == r['actual_returncode'] == 0
            and e['actual_failure'] is r['failure'] is None
            and e['actual_source_budget_processes'] == 1 and e['actual_verified_input_count'] == count
            and len(r['gates']) == gates and all(g['passed'] for g in r['gates'])
            and e['worker_source_sha256'] == FILES[role + 'w'][2]
            and e['source_budget_source_sha256'] == r['source_sha256'] == FILES[role + 's'][2]
            and e['input_manifest_sha256'] == r['input_manifest_sha256'] == FILES[role + 'm'][2],
            role + ' actual historical child, selected original fields and gates')
    require((r['temporary_native_bytes'], r['temporary_native_sha256']) == native
            and dict(file='consumers/process.json', bytes=process[0], sha256=process[1]) in e['output_hashes']
            and sum(x['bytes'] == native[0] and x['sha256'] == native[1] for x in e['output_hashes']) == 1,
            role + ' original recorded full process and temporary native')
    return r


def admit(topic):
    docs = whole(topic)
    strict, af = jcr.admit(topic)
    jc = docs['JCR']
    require(jc['proved'] and len(jc['checks']) == 20 and all(jc['checks'].values())
            and jc['real_full_negative_D_lower'] == '0.785'
            and jc['whole_inputs'] == {k: v[2] for k, v in jcr.FILES.items()}, 'actual JCR identity')
    w = historical(docs, 'W', '43694458725', '014c5f3e5e1d5b5631cdf06b65c92401504228f5', 67, 9,
                   (1729937, '675453a825f1ad09e6b496676f4c2f139f083bf96bfc34e999c9ba240a272c7c'),
                   (33919, 'f1c729cd3896e17616fba6bc6e7514853f835fb035149e5e31fb50480dea0199'))
    p = historical(docs, 'V', '43685624307', '1ca03990aed2531717528d8f51d1156138f1988a', 20, 16,
                   (6607, 'eb2b1323b0c01497ceddf28abac6223b41ad2c313055bce3428076bea0148ee1'),
                   (16990, 'ec9f4e61493e4f3c24530a5c7163d98f2bf2a741fbd3569ffa1bbf881df94e23'))
    pc, = [case for case in p['cases'] if case['exact_complex_radial_radius'] == '1/6000']
    dom = w['complete_domain_conclusion']
    ref = w['new_radial_reference_conclusion']
    scope = w['scope']
    require(pc['complete'] and pc['proved'] and pc['failure'] is None and pc['whole_complex_bilinear_family']
            and pc['fixed_intrinsic_parameter'] == scope['fixed_intrinsic_parameter'] == 'eta_0'
            and pc['exact_complex_delta_square_halfwidth'] == af['exact_complex_parameter_radius'] == '1/100000000'
            and pc['exact_complex_z_square_halfwidth'] == ref['exact_complex_z_square_halfwidth'] == '1/9409'
            and pc['both_carrier_signs_retained'] and ref['both_carrier_signs']
            and ref['all_input_labels_abs_at_least'] == pc['all_integer_modes_abs_j_at_least'] == 97
            and ref['rho_to_r_derivative_sign'] == -1 and ref['intermediate_modes'] == list(range(1, 97))
            and pc['reference_image']['entire_original_physical_root_piece_covered']
            and dom['original_potential_execution_sha256'] == FILES['V'][2] and dom['same_complex_delta_and_z_squares']
            and dom['same_reference_T_not_old_r_substituted'] and scope['entire_original_physical_piece2549']
            and scope['both_root_sides_with_original_uncertain_root_interval']
            and scope['new_reference_first_correction_identified_by_exact_integral']
            and scope['independent_physical_even_mean_equation_retained'] and scope['all_actual_physical_and_reference_seam_jumps_retained'],
            'same true collar, potential composition and signed correction')
    case, = [v for v in w['cases'] if v['exact_output_old_phi_width'] == '1/512']
    require(case['complete'] and case['proved']
            and case['exact_whole_piece_cover_radius'] == dom['exact_whole_physical_piece_cover_radius']
            == pc['reference_image']['exact_whole_physical_root_cover_radius'], 'same complete original piece')
    fields = {}
    for name in ('a1', 'b1'):
        f, = [v for v in case['fields'] if v['field'] == name]
        rows = f['complete_mixed_derivative_rows']
        require(f['exact_output_old_phi_width'] == '1/512' and f['full_output_zero_mode_retained']
                and f['joint_sum_of_radial_coefficient_suprema'] and f['finite_signed_addition_precedes_modulus_and_sum']
                and f['common_outer_angle_strip'] == '1/128' and f['old_tail_radius'] == '1/6000'
                and f['added_term_tail_radius'] == '3/40000' and [t['radial_derivative_order'] for t in rows] == [0, 1, 2]
                and all(t['angular_derivative_orders'] == [0, 1, 2, 3] for t in rows), 'complete corrected field ' + name)
        fields[name] = [row['complete_joint_Wiener_upper'][0] for row in rows[:2]]
    sp = docs['SP']
    ss = sp['actual_scientific_receipt']
    raw = (json.dumps(ss, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()
    require(sp['run_id'] == ss['run_id'] == '43731464771' and sp['run_attempt'] == ss['run_attempt'] == '1'
            and sp['complete'] and ss['complete'] and ss['proved'] and sp['actual_returncode'] == ss['actual_returncode'] == 0
            and len(ss['gates']) == 20 and all(g['passed'] for g in ss['gates'])
            and dict(file='consumers/process.json', bytes=len(raw), sha256=sha256(raw).hexdigest()) in sp['output_hashes'],
            'whole strict propagation')
    ws, we = docs['WEA'], docs['WEAp']
    require(we['run_id'] == ws['run_id'] == '43769746581' and we['run_attempt'] == ws['run_attempt'] == '1'
            and we['complete'] and ws['complete'] and ws['proved'] and we['actual_returncode'] == ws['actual_returncode'] == 0
            and we['actual_failure'] is ws['failure'] is None and len(ws['gates']) == 22 and all(g['passed'] for g in ws['gates'])
            and we['source_sha256'] == ws['source_sha256'] and we['input_manifest_sha256'] == ws['input_manifest_sha256']
            and dict(file='actual-scientific-conclusion.json', bytes=FILES['WEA'][1], sha256=FILES['WEA'][2]) in we['output_hashes']
            and docs['GSWr']['proved'] and docs['GSWr']['whole_GSW_proof_sha256'] == FILES['GSW'][2]
            and all(docs['GSWr']['new_exact_comparisons'].values()), 'real common and physical waist normalization')
    return strict['mathematical_parameters'], af, pc, fields


def new(params, af, pot, fields):
    def hi(value):
        return jcr.endpoints(value)[1]

    def column_sum(matrix):
        return max(sum(hi(row[k]) for row in matrix) for k in range(2))

    J = 2 ** 20 + 1
    N = 4 * J
    width, s = Q(1, 512), Q(1, 1024)
    a = af['complete_coefficient_budget_numeric']
    cut = Q(params['exact_strict_cut'])
    lo, rt = map(Q, af['exact_root_interval'])
    rg, collar = Q('9e-6'), Q('4e-6')
    u, v, vphi = Q('1.513'), Q('4.301'), Q('6.730')
    eta, den, beta = Q('1.253'), Q('.785'), Q('.210552')
    angle_loss = width - s
    vpot = Q(276)
    tau, ch, cw = Q(2), Q(6), Q(4)
    k = 64
    cost = 3 * k / s
    squared = 2 * (8 * 10 ** 8) ** 2 * N ** 5 * (cost / N) ** (2 * k) * (1 + Q(J, 122))
    return dict(
        whole_true_collar_length=cut < lo <= rt and rt - cut < collar,
        widths_cover_strip=0 < s < width < Q(3, 256) and width < jcr.endpoints(a['sigma'])[0],
        original_whole_leading=hi(a['M']) + hi(a['B2']) * hi(a['Tplus']) ** 2 < 2,
        leading_radial_cauchy=rg - collar == Q('5e-6') and 2 / (rg - collar) == 400000,
        corrected_whole_value=sum(hi(f[0]) for f in fields.values()) < 20,
        corrected_whole_radial=sum(hi(f[1]) for f in fields.values()) < 6400000,
        supported_true_potential=hi(pot['complete_modulus_upper']['V']) < vpot and hi(a['Tplus']) < Q('.000042') < Q(1, 4000),
        true_potential_image=jcr.endpoints(pot['reference_image']['guaranteed_old_fold_rho_radius_lower'])[0] > rg,
        angular_and_D_matrices=column_sum(a['H_inverse']) < 2 and column_sum(a['HD']) < 5 and hi(a['HD'][1][0]) < 5,
        angular_perturbation=hi(a['Tphi']) < Q('5e-9') and 2 * Q('5e-9') * vpot / N ** 2 < Q(1, 3),
        inverse_and_D_complete=2 / (1 - 2 * Q('5e-9') * vpot / N ** 2) < 3 and 5 + Q(5) * vpot / N ** 2 < 6,
        normalized_w=2 + Q(20, N) < 9 and 400000 + Q(6400000, N) < 2000000,
        w_drift=hi(a['d0']) < Q('.122') and 2000000 + Q('.122') * 9 / angle_loss < 2100000,
        complete_h_g=jcr.endpoints(a['eta_lower'])[0] > eta and Q(162) / eta < 130 and 2100000 + 162 / angle_loss < 2300000,
        actual_U_V=hi(a['U'][0]) < u and hi(a['V'][0]) < v and hi(a['V'][1]) < vphi,
        complete_physical_coefficients=hi(a['beta']) < beta and hi(a['b0']) < 1 and hi(a['K']) < Q('.002')
            and 2 * beta * Q('.002') < Q('.001'),
        exponential_wiener=2 * beta / eta * u * v / 4 < Q('.6') and 1 / (1 - Q('.6')) < 3,
        complete_tau_Ch=3 * u / (4 * eta * den) < tau and 3 * u / den < ch,
        complete_Cw=Q('.002') * v + tau + Q('.001') * v * vphi * tau / 4 < cw,
        independent_mean_coefficient=2 * beta * v < 2 and 2 * (tau * 2300000 + ch * 130 + cw * 9) < 10 ** 8,
        both_genuine_rows=Q(6, 5) ** 2 * (1 + Q('.000042')) < 4 ** 2,
        full_input_weight=(1 + Q(1, N ** 2)) ** 2 < 2 ** 3,
        exact_64_derivatives=cost == 196608 and 2 * k - 5 == 123,
        both_signs_whole_two_column_squared_HS=squared < Q('1e-110'),
        ordinary_full_collar=Q('1e-55') * collar == Q('4e-61'),
        physical_common_mean_only=Q('4e-61') * 2039 * Q('.719') * Q('12.4') < Q('1e-56'))


def main():
    checks = new(*admit(Path(__file__).resolve().parents[1]))
    require(all(checks.values()), 'failed GMI comparisons: ' + str([k for k, v in checks.items() if not v]))
    print(json.dumps(dict(proved=True, checks=checks, whole_inputs={k: x[2] for k, x in {**jcr.FILES, **FILES}.items()},
                          min_abs_j=2 ** 20 + 1, both_signed_carriers=True, genuine_terminal_columns=2,
                          closed_true_negative_root_collar=True, true_independent_mean_pointwise_upper='1e-55',
                          same_mean_L1_dr_upper='4e-61', same_mean_C97_upper='1e-56',
                          old_scientific_targets_recomputed=0, complete_nonlocal_first_row_and_full_inverse_proved=False),
                     sort_keys=True))


if __name__ == '__main__':
    main()
