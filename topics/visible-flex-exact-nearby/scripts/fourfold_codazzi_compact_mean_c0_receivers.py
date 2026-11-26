#!/usr/bin/env python3
"""New compact positive moments and whole C0 mean receivers; public Actions only.

Read the original complete 7721-row scalar-mean native without invoking
any old producer.  Read Gamma and the two old row sums as already saved.
Compute only the new complete jump/weighted receivers, needed whole
norms, and normalized compact moments.  No forward endpoint, primitive,
DFT, old Green maximum, old residual, or selected-delta target is run.
Detailed rows remain in a private trace; only whole scalars are public.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb
import os
from pathlib import Path
import time

REPO = 'Rogerhu12/math-research-public'
KIND = 'R144_raw_nu0_compact_moments_complete_C0_receivers_v1'
NATIVE = 'e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b'
OLD_SOURCE = '6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
OBJECT = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
ALPHA = '6890507429876859/9007199254740992'
NU = '-2572625729470897/72057594037927936'
ETA = '-7789843107295549/4611686018427387904'
RAW_NOTE_SHA = '84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e'
STRICT_PROOF_SHA = '95d3abfe8f05a14e15f1570f85b379a06120700c157549e9d1f507ade2ee58aa'
CR_PROOF_SHA = '1f55171ae49a3cda07f44c2bc073a41887a7169c9fe210774a373f22599fe81f'
KERNEL_PROOF_SHA = 'c9b2469ce02c5553aceee6401a3cc388607aa7ea83d661759aa79078aef797a1'
KERNELS = ('01', '02', '10', '11', '12', '20', '21', '22', '30', '31', '32')
ROWS, JOINS = 7721, 6143
LEFT, RIGHT, END = Fraction(1, 20), Fraction(9, 50), Fraction(25, 8)
POINT_MEAN_GAP = Fraction(10687328018, 10**10)
POINT_V_GAP = Fraction(901531879, 10**10)
POINT_RV_UPPER = Fraction(4159086, 10**13)
ZERO_FIELDS = ('old_scientific_targets_called old_mean_Green_targets_called '
               'old_Gamma_or_old_row_maxima_recomputed old_residual_targets_called '
               'old_target_ODE_calls old_angular_solver_calls primitive_or_DFT_calls '
               'forward_W_targets_called published_arrays').split()
SCALARS = ('K0_ordinary_mean_C0_upper K1_full_nonmean_C0_upper '
           'KJ_all_common_jumps_C0_upper K_betaK_weighted_ordinary_C0_upper '
           'K2_nonlinear_C0_upper mean_abs_lower mean_abs_upper variance_upper '
           'density_variance_ratio_sqrt_upper beta_K_abs_upper '
           'raw_mean_residual_upper raw_mean_jump_sum_upper raw_v_gap_lower '
           'H_at_compact_right abar bbar weighted_suffix_before_Gamma '
           'weighted_maximum_before_Gamma prefix_inverse_tau_max').split()
SCALARS += ['C'+key+'_profile_kernel_upper' for key in KERNELS]
SCALARS += ['kernel_'+key+'_'+part for key in KERNELS for part in ('suffix', 'maximum_before_Gamma')]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode('utf-8')


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def atomic(path, raw):
    path = Path(path)
    temp = path.with_name(path.name+'.tmp')
    with temp.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def chi_integral(left, right, power):
    """Exact rational integral of chi**power, only in its actual support."""
    require(LEFT <= left <= right <= RIGHT and power in (1, 2),
            'exact compact polynomial integration domain')
    width = RIGHT-LEFT
    a, b = (left-LEFT)/width, (right-LEFT)/width
    degree = 6*power
    total = sum((Fraction((-1)**k*comb(degree, k), degree+k+1)
                 *(b**(degree+k+1)-a**(degree+k+1))
                 for k in range(degree+1)), Fraction(0))
    value = width*4096**power*total
    require(value >= 0, 'exact nonnegative compact polynomial mass')
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mean', type=Path, required=True)
    ap.add_argument('--old-process', type=Path, required=True)
    ap.add_argument('--old-readable', type=Path, required=True)
    ap.add_argument('--raw-bounds', type=Path, required=True)
    ap.add_argument('--strict-proof', type=Path, required=True)
    ap.add_argument('--receiver-proof', type=Path, required=True)
    ap.add_argument('--kernel-proof', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO,
            'scientific arithmetic only in the authorized public Actions repository')
    require(not args.output.exists(), 'preserve every completed and partial target')
    from flint import arb, ctx
    ctx.prec = 320
    began = time.monotonic()

    def rat(value):
        q = Fraction(value)
        return arb(q.numerator)/arb(q.denominator)

    def old_ball(value):
        require(isinstance(value, dict) and 'lower' in value and 'upper' in value,
                'full original lower and upper scalar record')
        x = arb(value['lower']).lower().union(arb(value['upper']).upper())
        require(x.is_finite(), 'finite original whole scalar enclosure')
        return x

    def unpack(value):
        e = int(value['decimal_exponent'])
        scale = rat(10**e) if e >= 0 else rat(Fraction(1, 10**(-e)))
        m = rat(int(value['midpoint_integer']))*scale
        r = rat(int(value['radius_integer']))*scale
        return (m-r).lower().union((m+r).upper())

    def recorded(value, direction='enclosure'):
        require(value.is_finite(), 'finite new complete scalar')
        m, r, e = value.mid_rad_10exp(75)
        out = dict(kind='complete_decimal_ball_v1', mathematical_direction=direction,
                   midpoint_integer=str(int(m)), radius_integer=str(int(r)),
                   decimal_exponent=str(int(e)))
        require(int(r) >= 0 and unpack(out).contains(value),
                'saved full decimal ball contains its directed Arb value')
        return out

    def nonnegative_endpoints(value):
        require(value.upper() >= 0, 'true nonnegative scalar lost its enclosure')
        return max(arb(0), value.lower()).lower(), value.upper()

    def positive_reciprocal(point):
        require(point > 0, 'strictly positive directed denominator endpoint')
        return 1/point

    doc = dict(
        identity=dict(kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
            original_mean_native_sha256=NATIVE, original_mean_source_sha256=OLD_SOURCE,
            original_candidate_sha256=CANDIDATE, exact_alpha=ALPHA, exact_nu=NU,
            exact_eta=ETA, original_parameter_half_width='1/1000000000',
            arithmetic_bits=320, original_modes=32, exact_interval=['0', '25/8'],
            compact_interval=['1/20', '9/50'],
            intrinsic_box_used_only_as_enclosure_of_its_original_centre=True,
            old_process_sha256=sha(args.old_process.read_bytes()),
            old_readable_sha256=sha(args.old_readable.read_bytes()),
            raw_bounds_sha256=sha(args.raw_bounds.read_bytes()),
            strict_proof_sha256=sha(args.strict_proof.read_bytes()),
            receiver_proof_sha256=sha(args.receiver_proof.read_bytes()),
            kernel_proof_sha256=sha(args.kernel_proof.read_bytes())),
        complete=False, proved=False, failure=None, stage='input-admission',
        expected_common_cells=ROWS, expected_mean_interfaces=JOINS,
        completed_common_cells=0, completed_mean_interfaces=0,
        completed_prefix_cells=0, completed_compact_cells=0,
        completed_weighted_reverse_cells=0, current_exact_right='0',
        current_H_exact_right='0', weighted_next_original_row=ROWS-1,
        old_saved_scalar_reads=0, complete_new_scalars={},
        scalar_scope='accepted_forward_prefix_and_reverse_suffix_only',
        strict_gates=dict(compact_leverage_positive='unknown',
                         actual_forward_endpoint_consumed=False,
                         actual_small_root='unknown',
                         actual_nonlinear_mean_small_ball='unknown'),
        scope=dict(original_Qraw_nu0_eta0_only=True,
            exact_original_affine_box_identity_required=True,
            all_original_mean_interfaces_retained=True,
            normalized_compact_moments_only_new=True,
            C0_receiver_is_not_old_L2_gain=True,
            detailed_rows_private_only=True,
            complete_new_receiver_and_moments=False,
            structural_bbar_between_zero_and_abar_over_two=True,
            old_saved_Gamma_and_row_sums_recomputed=False,
            point_intrinsic_carrier_reconstructed=False,
            forward_W_recomputed=False, selected_delta_or_phase_inherited=False,
            nonmean_equations_solved=False, outer_cap_or_height_matched=False,
            body_inverse_proved=False, final_topic_complete=False),
        private_trace=dict(records=0, bytes=0, sha256=None, content_published=False,
                           scope='saved_accepted_checkpoint_prefix'),
        seconds=0.0, **{key: 0 for key in ZERO_FIELDS})
    trace = args.output.with_name('private-compact-mean-receiver.ndjson')
    trace_hash = hashlib.sha256()
    trace_records, trace_bytes = 0, 0
    atomic(args.output, encode(doc))

    def snapshot():
        doc['private_trace'] = dict(records=trace_records, bytes=trace_bytes,
            sha256=trace_hash.hexdigest(), content_published=False,
            scope='saved_accepted_checkpoint_prefix')
        doc['seconds'] = time.monotonic()-began
        atomic(args.output, encode(doc))

    try:
        require(doc['identity']['raw_bounds_sha256'] == RAW_NOTE_SHA
                and doc['identity']['strict_proof_sha256'] == STRICT_PROOF_SHA
                and doc['identity']['receiver_proof_sha256'] == CR_PROOF_SHA
                and doc['identity']['kernel_proof_sha256'] == KERNEL_PROOF_SHA,
                'exact previously proved residual, strict sign, and complete receiver')
        raw = args.mean.read_bytes()
        require(sha(raw) == NATIVE, 'unchanged complete original scalar-mean container')
        native = parse(gzip.decompress(raw))
        old_process = parse(args.old_process.read_bytes())
        require(old_process['complete'] is True and old_process['actual_returncode'] == 0
                and old_process['result_complete'] is True and old_process['result_failure'] is None
                and old_process['out_sha256'] == NATIVE and old_process['source_sha256'] == OLD_SOURCE
                and old_process['completed_rows'] == ROWS
                and old_process['total_closed_cells'] == ROWS,
                'complete original scalar-mean process receipt')
        require(native['kind'] == 'actual_final_complete_scalar_mean_Green_cached_full_target'
                and native['complete'] is True and native['failure'] is None
                and native['source_sha256'] == OLD_SOURCE
                and native['candidate_sha256'] == CANDIDATE
                and native['exact_amplitude'] == ALPHA and native['exact_nu'] == NU
                and native['exact_interval'] == ['0', '25/8']
                and native['original_parameter_half_width'] == '1/1000000000'
                and native['whole_original_affine_parameter_interval'] is True
                and native['all_exact_mean_interfaces_retained'] is True
                and native['candidate_metadata']['modes'] == 32
                and native['candidate_metadata']['object_sha256'] == OBJECT
                and len(native['rows']) == ROWS and len(native['interfaces']) == JOINS,
                'same complete original centre, affine box, and actual mean interfaces')
        readable = parse(args.old_readable.read_bytes())
        require(readable['kind'] == 'actual_final_full_mean_Green_strict_readable_constants'
                and readable['complete'] is True and readable['native_sha256'] == NATIVE
                and readable['candidate_sha256'] == CANDIDATE
                and readable['original_native_source_sha256'] == OLD_SOURCE
                and readable['actual_closed_cells'] == ROWS
                and readable['actual_candidate_mean_interfaces'] == JOINS,
                'already completed whole readable Gamma, not a new exponential evaluation')
        gamma_gate = [x for x in readable['gates'] if x['name'] == 'complete_Gamma']
        require(len(gamma_gate) == 1 and gamma_gate[0]['passed'] is True,
                'one actual saved complete Gamma gate')
        Gamma = old_ball(gamma_gate[0]['value']).upper()
        require(Gamma > 0 and Gamma < rat(Fraction(1013237, 10**6)),
                'readback of the original strict complete Gamma bound')
        old_bounds = native['bounds']
        old_rows = old_bounds['complete_triangular_Schur_integral_upper']
        Rm = old_ball(old_rows['mean_source_row']).upper()
        Rnm = old_ball(old_rows['nonmean_row']).upper()
        Jm = old_ball(old_bounds['full_interface_log_upper']).upper()
        require(Rm > 0 and Rnm >= 0 and Jm >= 0, 'existing complete nonnegative row bounds')
        K0, K1 = (Gamma*Rm).upper(), (Gamma*Rnm).upper()
        doc['old_saved_scalar_reads'] = 4
        rows, joins = native['rows'], native['interfaces']
        jump_map = {item['common_row']: item for item in joins}
        require(len(jump_map) == JOINS, 'all distinct original mean interfaces')
        cuts = {Fraction(row['interval'][0]) for row in rows}|{END}
        require(LEFT in cuts and RIGHT in cuts,
                'exact compact support edges occur in the original common partition')
        Hlo = Hhi = arb(1)
        alo = ahi = blo = bhi = arb(0)
        M = Vmax = Z2 = Bmax = KJ = invtau_prefix = arb(0)
        mmin = None
        weighted_suffix = weighted_max = arb(0)
        kernel_suffix = {key: arb(0) for key in KERNELS}
        kernel_maximum = {key: arb(0) for key in KERNELS}
        compact_masses = {}
        rightmost, previous_piece = Fraction(0), None
        # Private scalar row data are read again only for the genuinely new
        # weighted reverse receiver, not to recompute old row maxima.
        def current_scalars(Kweighted=None):
            Z = Z2.sqrt().upper()
            kb = arb(0) if Kweighted is None else Kweighted
            k2 = (K0*Bmax).upper() if Kweighted is None else min((K0*Bmax).upper(), kb).upper()
            values = dict(
                K0_ordinary_mean_C0_upper=(K0, 'upper'),
                K1_full_nonmean_C0_upper=(K1, 'upper'),
                KJ_all_common_jumps_C0_upper=(KJ, 'upper'),
                K_betaK_weighted_ordinary_C0_upper=(kb, 'upper'),
                K2_nonlinear_C0_upper=(k2, 'upper'),
                mean_abs_lower=(arb(0) if mmin is None else mmin, 'lower'),
                mean_abs_upper=(M, 'upper'),
                variance_upper=(Vmax, 'upper'),
                density_variance_ratio_sqrt_upper=(Z, 'upper'),
                beta_K_abs_upper=(Bmax, 'upper'),
                raw_mean_residual_upper=((rat(ALPHA)*rat(POINT_RV_UPPER)).upper(), 'upper'),
                raw_mean_jump_sum_upper=((M*Jm/3).upper(), 'upper'),
                raw_v_gap_lower=(rat(POINT_V_GAP).lower(), 'lower'),
                H_at_compact_right=(Hlo.union(Hhi), 'enclosure'),
                abar=(alo.union(ahi), 'enclosure'),
                bbar=(blo.union(bhi), 'enclosure'),
                weighted_suffix_before_Gamma=(weighted_suffix, 'upper'),
                weighted_maximum_before_Gamma=(weighted_max, 'upper'),
                prefix_inverse_tau_max=(invtau_prefix, 'upper'))
            for key in KERNELS:
                values['C'+key+'_profile_kernel_upper'] = ((Gamma*kernel_maximum[key]).upper(), 'upper')
                values['kernel_'+key+'_suffix'] = (kernel_suffix[key], 'upper')
                values['kernel_'+key+'_maximum_before_Gamma'] = (kernel_maximum[key], 'upper')
            return {name: recorded(x, direction) for name, (x, direction) in values.items()}

        def append_trace(stream, item):
            nonlocal trace_records, trace_bytes
            raw = encode(item)
            stream.write(raw)
            stream.flush()
            trace_hash.update(raw)
            trace_records += 1
            trace_bytes += len(raw)

        doc['stage'] = 'new-forward-norms-and-compact-moments'
        with trace.open('wb') as stream:
            for i, row in enumerate(rows):
                left, right = map(Fraction, row['interval'])
                require(row['common_row'] == i and left == rightmost and left < right,
                        'complete original common-cell adjacency')
                gl, gr = map(Fraction, row['actual_scalar_germ'])
                require(gl <= left < right <= gr, 'unchanged original scalar germ')
                p = int(row['candidate_piece'])
                changed = previous_piece is not None and p != previous_piece
                require((i in jump_map) is changed, 'all and only original candidate mean joins')
                if changed:
                    item = jump_map[i]
                    require(p == previous_piece+1 and item['candidate_join'] == p
                            and Fraction(item['radius']) == left,
                            'original one-sided mean-interface identity')
                z, a = row['scalar_mean'], row['actual_target']
                mm = -old_ball(z['actual_m'])
                tau = old_ball(z['mean_transform_tau'])
                aa = old_ball(a['a'])
                beta, K = old_ball(a['beta']), old_ball(a['K'])
                ulo, uhi = nonnegative_endpoints(old_ball(z['nonmean_u_square']))
                vlo, vhi = nonnegative_endpoints(old_ball(z['nonmean_v_square']))
                require(mm > 0 and tau > 0 and aa > 0,
                        'complete original strictly negative mean and positive metric chart')
                ml = max(mm.lower(), rat(POINT_MEAN_GAP).lower()).lower()
                mu = mm.upper()
                require(ml <= mu, 'point raw mean lower gate consistent with old enclosing row')
                ti, bi = tau.upper(), positive_reciprocal(tau.lower()).upper()
                Brow = (abs(beta).upper()*abs(K).upper()).upper()
                M = max(M, mu).upper()
                mmin = ml if mmin is None else min(mmin, ml).lower()
                Vmax = max(Vmax, vhi).upper()
                Z2 = max(Z2, (vhi*positive_reciprocal(ml**2)).upper()).upper()
                Bmax = max(Bmax, Brow).upper()
                if i:
                    # Gamma includes the terminal T_i^{-1}; tau_i^+ is its
                    # correct transformed injection coefficient (CR10).
                    KJ = max(KJ, (Gamma*ti*invtau_prefix).upper()).upper()
                invtau_prefix = max(invtau_prefix, bi).upper()
                ainc = binc = arb(0)
                if left < RIGHT:
                    require(right <= RIGHT, 'no old cell crosses the exact compact right cut')
                    # The strict metric proof applies to this fixed centre.
                    # Its beta>=0, K<0 facts restrict an enclosing affine box.
                    bll = max(arb(0), beta.lower()).lower()
                    bhu = beta.upper()
                    require(bhu >= 0, 'strict-side beta sign compatible with the old enclosure')
                    clo, chi = (2*bll*ulo).lower(), (2*bhu*uhi).upper()
                    length = rat(right-left)
                    new_Hlo = (Hlo*(length*clo).exp()).lower()
                    new_Hhi = (Hhi*(length*chi).exp()).upper()
                    if right > LEFT:
                        require(left >= LEFT, 'no old cell crosses the exact compact left cut')
                        kll, khu = max(arb(0), (-K).lower()).lower(), (-K).upper()
                        require(khu > 0, 'strict negative K compatible with old whole enclosure')
                        Plo = (4*bll*kll*aa.lower()**2*vlo
                               *positive_reciprocal(mu**2*new_Hhi)).lower()
                        Phi = (4*bhu*khu*aa.upper()**2*vhi
                               *positive_reciprocal(ml**2*Hlo)).upper()
                        require(Plo >= 0 and Phi >= Plo,
                                'nonnegative whole compact integrand enclosure')
                        mass1, mass2 = chi_integral(left, right, 1), chi_integral(left, right, 2)
                        compact_masses[i] = (mass1, mass2)
                        c1, c2 = rat(mass1), rat(mass2)
                        da_lo, da_hi = (Plo*c1).lower(), (Phi*c1).upper()
                        db_lo, db_hi = (Plo*c2/2).lower(), (Phi*c2/2).upper()
                        alo, ahi = (alo+da_lo).lower(), (ahi+da_hi).upper()
                        blo, bhi = (blo+db_lo).lower(), (bhi+db_hi).upper()
                        ainc, binc = da_lo.union(da_hi), db_lo.union(db_hi)
                        doc['completed_compact_cells'] += 1
                    Hlo, Hhi = new_Hlo, new_Hhi
                    doc['completed_prefix_cells'] += 1
                    doc['current_H_exact_right'] = str(right)
                append_trace(stream, dict(stage='forward', original_row=i,
                    abar_increment=recorded(ainc), bbar_increment=recorded(binc),
                    H=recorded(Hlo.union(Hhi))))
                rightmost, previous_piece = right, p
                doc['completed_common_cells'] = i+1
                doc['completed_mean_interfaces'] += int(changed)
                doc['current_exact_right'] = str(right)
                doc['complete_new_scalars'] = current_scalars()
                snapshot()
            require(rightmost == END and previous_piece == JOINS
                    and doc['completed_mean_interfaces'] == JOINS
                    and doc['current_H_exact_right'] == str(RIGHT),
                    'full original body and all mean jumps, complete compact H prefix')
            doc['stage'] = 'new-weighted-ordinary-C0-reverse-receiver'
            snapshot()
            for i in range(ROWS-1, -1, -1):
                row = rows[i]
                left, right = map(Fraction, row['interval'])
                tau = old_ball(row['scalar_mean']['mean_transform_tau'])
                beta = old_ball(row['actual_target']['beta'])
                K = old_ball(row['actual_target']['K'])
                require(tau > 0, 'positive unchanged old conjugating factor')
                Brow = (abs(beta).upper()*abs(K).upper()).upper()
                length = rat(right-left)
                ti, bi = tau.upper(), positive_reciprocal(tau.lower()).upper()
                weighted_suffix = (weighted_suffix+length*ti*Brow).upper()
                weighted_max = max(weighted_max, (bi*weighted_suffix).upper()).upper()
                mm = -old_ball(row['scalar_mean']['actual_m'])
                _, vu = nonnegative_endpoints(old_ball(row['scalar_mean']['nonmean_v_square']))
                ml = max(mm.lower(), rat(POINT_MEAN_GAP).lower()).lower()
                mu = mm.upper()
                require(ml > 0 and mu >= ml, 'actual point mean for complete profile weights')
                invm = positive_reciprocal(ml).upper()
                invm2 = positive_reciprocal(ml**2).upper()
                mass1, mass2 = compact_masses.get(i, (Fraction(0), Fraction(0)))
                c1, c2 = rat(mass1), rat(mass2)
                # Every coefficient is a whole-row upper bound; only chi and
                # chi^2 are integrated exactly.  All weights are nonnegative.
                wm = dict(
                    **{'01': 2*Brow*mu*vu*c1, '02': Brow*mu*vu*c2},
                    **{'10': 2*Brow*vu*length,
                       '11': 6*Brow*vu*c1, '12': 3*Brow*vu*c2},
                    **{'20': 3*Brow*(mu+vu*invm)*length,
                       '21': 6*Brow*vu*invm*c1, '22': 3*Brow*vu*invm*c2},
                    **{'30': Brow*(1+vu*invm2)*length,
                       '31': 2*Brow*vu*invm2*c1, '32': Brow*vu*invm2*c2})
                require(set(wm) == set(KERNELS), 'all eleven actual profile-weighted sources')
                for key in KERNELS:
                    require(wm[key].lower() >= 0, 'nonnegative whole weighted source mass')
                    kernel_suffix[key] = (kernel_suffix[key]+ti*wm[key].upper()).upper()
                    kernel_maximum[key] = max(kernel_maximum[key],
                                              (bi*kernel_suffix[key]).upper()).upper()
                append_trace(stream, dict(stage='weighted_reverse', original_row=i,
                    new_weighted_suffix=recorded(weighted_suffix, 'upper'),
                    new_weighted_max=recorded(weighted_max, 'upper'),
                    profile_weight_masses={key: recorded(wm[key], 'enclosure') for key in KERNELS}))
                doc['completed_weighted_reverse_cells'] += 1
                doc['weighted_next_original_row'] = i-1
                doc['complete_new_scalars'] = current_scalars((Gamma*weighted_max).upper())
                snapshot()
        doc['stage'] = 'all-new-scalars-saved-awaiting-readback'
        snapshot()
        saved = parse(args.output.read_bytes())
        require(saved['completed_common_cells'] == ROWS
                and saved['completed_mean_interfaces'] == JOINS
                and saved['completed_weighted_reverse_cells'] == ROWS
                and saved['weighted_next_original_row'] == -1
                and set(saved['complete_new_scalars']) == set(SCALARS),
                'actual saved complete whole scalar readback')
        ab = unpack(saved['complete_new_scalars']['abar'])
        gate = True if ab.lower() > 0 else (False if ab.upper() <= 0 else 'unknown')
        saved['strict_gates']['compact_leverage_positive'] = gate
        saved['scope']['complete_new_receiver_and_moments'] = True
        saved['scalar_scope'] = 'complete_whole_target'
        saved['complete'] = True
        saved['proved'] = gate is True
        saved['failure'] = None
        saved['stage'] = 'complete-new-compact-moments-and-C0-receivers'
        saved['seconds'] = time.monotonic()-began
        atomic(args.output, encode(saved))
        print(json.dumps(dict(complete=True, new_receiver_and_compact_moment_target=True,
            compact_leverage_positive=gate, original_rows_read=ROWS,
            original_interfaces_retained=JOINS, primitive_or_DFT_calls=0,
            old_Green_or_row_maxima_recomputed=0, forward_endpoint_consumed=False),
            sort_keys=True), flush=True)
    except BaseException as exc:
        # Never pair a partially advanced in-memory state with an old cursor.
        # Only the last atomically saved accepted checkpoint is published.
        saved = parse(args.output.read_bytes())
        prefix_bytes = saved['private_trace']['bytes']
        if trace.exists():
            with trace.open('r+b') as stream:
                stream.truncate(prefix_bytes)
        saved['scalar_scope'] = 'accepted_forward_prefix_and_reverse_suffix_only'
        saved['complete'] = False
        saved['proved'] = False
        saved['stage'] = 'failed-with-complete-saved-prefix'
        saved['failure'] = dict(type=type(exc).__name__, message=str(exc))
        saved['seconds'] = time.monotonic()-began
        atomic(args.output, encode(saved))
        raise


if __name__ == '__main__':
    main()
