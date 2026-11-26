#!/usr/bin/env python3
"""Localized complete moving C0 and compact-centre sources; public Actions only.

Read the actual complete TM radii, original whole mean enclosures and
all original finite cubic Fourier coefficients.  Compute only the new
localized state norm, five whole source receivers and rescaled full
moving jump bound.  No old target, mean solve, primitive or DFT is run.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from math import comb
import os
from pathlib import Path
import time

REPO = 'Rogerhu12/math-research-public'
KIND = 'R144_raw_nu0_localized_full_state_C0_and_compact_sources_v1'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
MEAN = 'e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b'
MEAN_SOURCE = '6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
TM_SHA = 'a74d11052da41570a7588d5a79545cfb7295ccf437b3bae971390d59f2b99de6'
TM_EXEC_SHA = 'af0b8f547c4e4215bbfcd42f7e0546391ec247765c3a94c9634c3950acd5fe34'
TM_SOURCE = 'df04e841a8812eab1942d10371f0dcd20d97ec6ab5a6d6fe134bc9b71e35f7f0'
C0_SHA = '0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641'
C0_EXEC_SHA = '9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc'
RAW_SHA = '84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e'
CS_SHA = '72252cbf0e2972e4f2248ce6711a0274c3d9a1b134b2aad276ccdb0304177d11'
LC_SHA = '16ed825fea674e2239c8e727c294cce2a396e5edf7064cc422f4ccef3652b471'
GEOMETRY_SHA = '366914bfb1ad8acfba99fe77c4a37237957ed6a777eef01072a039370525f2fe'
ALPHA = '6890507429876859/9007199254740992'
NU = '-2572625729470897/72057594037927936'
ETA = '-7789843107295549/4611686018427387904'
ROWS, JOINS, PIECES, MODES = 7721, 6143, 6144, 32
LEFT, RIGHT, END = Fraction(1, 20), Fraction(9, 50), Fraction(25, 8)
ZERO_FIELDS = ('old_scientific_targets_recomputed old_mean_Green_or_Gamma_calls '
               'old_residual_target_calls old_compact_moment_calls '
               'terminal_mean_gate_targets_called radial_ODE_calls '
               'primitive_or_DFT_calls forward_W_targets_called '
               'physical_theta_grid_calls published_arrays').split()
PREFIX_FIELDS = ('same_phi_C0_upper sine_A0_upper cosine_nonmean_A0_upper '
                 'density_A0_upper fu_squared_integral_upper qu_squared_integral_upper '
                 'fv_chi_squared_integral_upper qv_squared_integral_upper '
                 'cv_operator_upper').split()
FINAL_FIELDS = ('fu_L2_upper qu_L2_upper fv_chi_L2_upper qv_L2_upper '
                'Fu_complete_L2_upper Qu_complete_L2_upper Fv_complete_L2_upper Qv_complete_L2_upper '
                'unchanged_raw_Ru_L2_upper unchanged_raw_Rv_L2_upper '
                'unchanged_raw_u_jump_A0_upper unchanged_raw_v_jump_A0_upper '
                'new_complete_v_jump_A0_upper '
                'first_row_Hminus2over3_upper second_row_Hminus2over3_upper '
                'second_row_Hminus1_upper isotropic_Hminus2over3_pair_upper '
                'anisotropic_Hminus2over3_Hminus1_pair_upper').split()


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
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def compact_max(left, right):
    require(left < right, 'nonempty exact closed cell')
    if right <= LEFT or left >= RIGHT:
        return Fraction(0)
    require(LEFT <= left < right <= RIGHT, 'exact compact support cuts')
    width = RIGHT-LEFT
    a, b = (left-LEFT)/width, (right-LEFT)/width
    t = min(b, max(a, Fraction(1, 2)))
    return 4096*t**6*(1-t)**6


def compact_derivative_square_mass(left, right):
    if right <= LEFT or left >= RIGHT:
        return Fraction(0)
    require(LEFT <= left < right <= RIGHT, 'complete compact derivative mass domain')
    width = RIGHT-LEFT
    a, b = (left-LEFT)/width, (right-LEFT)/width
    value = sum((Fraction((-1)**k*comb(10, k)*c, 11+k+j)
                 *(b**(11+k+j)-a**(11+k+j))
                 for k in range(11) for j, c in enumerate((1, -4, 4))), Fraction(0))
    value *= Fraction(24576**2, 1)/width
    require(value >= 0, 'nonnegative exact squared compact derivative integral')
    return value


def load_candidate(path):
    import numpy as np
    path = Path(path)
    require(sha(path.read_bytes()) == CANDIDATE, 'original complete candidate index')
    index = parse(path.read_bytes())
    require(index['kind'] == 'complete_lossless_radial_cubic_shards_v1'
            and index['coefficient_shape'] == [4, PIECES, 65]
            and index['radial_nodes_count'] == PIECES+1
            and index['polynomial_order'] == 'numpy/scipy PPoly descending local powers',
            'all original radial cubic and Fourier coordinates')
    nodes, blocks, endpoint, next_piece = [], [], None, 0
    for item in index['parts']:
        require(Path(item['file']).name == item['file'], 'safe original candidate shard')
        raw = (path.parent/item['file']).read_bytes()
        require(len(raw) == item['bytes'] and sha(raw) == item['sha256'],
                'unchanged original complete candidate shard')
        with np.load(io.BytesIO(gzip.decompress(raw)), allow_pickle=False) as data:
            r, c = data['radial_nodes'].copy(), data['piece_coefficients'].copy()
        require(item['first_interval'] == next_piece and c.shape == (4, len(r)-1, 65)
                and bool(np.all(np.diff(r) > 0)) and bool(np.all(np.isfinite(c))),
                'entire original exact cubic piece coverage')
        if endpoint is not None:
            require(r[0].view(np.uint64) == endpoint.view(np.uint64), 'bitwise shared shard endpoint')
        nodes.append(r if endpoint is None else r[1:])
        blocks.append(c)
        endpoint, next_piece = r[-1], item['last_interval_exclusive']
    r, c = np.concatenate(nodes), np.concatenate(blocks, axis=1)
    require(c.shape == (4, PIECES, 65) and len(r) == PIECES+1 and next_piece == PIECES,
            'all original candidate intervals materialized')
    meta = index['metadata']
    require(meta['modes'] == MODES and meta['physical_frequency_factor'] == 4
            and meta['object_sha256'] == OBJECT
            and meta['exact_float_amplitude'] == ALPHA and meta['exact_float_nu'] == NU,
            'same complete raw centre and physical amplitude')
    require(np.array_equal(c[3, 0, :], np.asarray(index['initial_state'], dtype=np.float64)),
            'initial state is the original exact first trace')
    knots = [Fraction.from_float(float(x)) for x in r]
    require(knots[0] == 0 and knots[-1] == END, 'whole original radial domain')
    return knots, c


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mean', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--old-process', type=Path, required=True)
    ap.add_argument('--tm-result', type=Path, required=True)
    ap.add_argument('--tm-execution', type=Path, required=True)
    ap.add_argument('--c0-result', type=Path, required=True)
    ap.add_argument('--c0-execution', type=Path, required=True)
    ap.add_argument('--raw-bounds', type=Path, required=True)
    ap.add_argument('--source-proof', type=Path, required=True)
    ap.add_argument('--localized-proof', type=Path, required=True)
    ap.add_argument('--geometry-proof', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO,
            'scientific arithmetic only in authorized public Actions')
    require(not args.output.exists(), 'preserve every completed and partial scientific target')
    from flint import arb, ctx
    ctx.prec = 320
    began = time.monotonic()

    def rat(value):
        q = Fraction(value)
        return arb(q.numerator)/arb(q.denominator)

    def old_ball(value):
        require(isinstance(value, dict) and 'lower' in value and 'upper' in value,
                'complete original lower/upper enclosure')
        out = arb(value['lower']).lower().union(arb(value['upper']).upper())
        require(out.is_finite(), 'finite original entire-row bound')
        return out

    def unpack(value):
        require(value['kind'] == 'complete_decimal_ball_v1', 'complete saved decimal ball')
        e = int(value['decimal_exponent'])
        scale = rat(10**e) if e >= 0 else rat(Fraction(1, 10**(-e)))
        m = rat(int(value['midpoint_integer']))*scale
        r = rat(int(value['radius_integer']))*scale
        require(int(value['radius_integer']) >= 0, 'nonnegative full saved radius')
        out = (m-r).lower().union((m+r).upper())
        require(out.is_finite(), 'finite complete saved decimal ball')
        return out

    def record(value):
        require(value.is_finite(), 'finite new full upper bound')
        m, r, e = value.mid_rad_10exp(75)
        out = dict(kind='complete_decimal_ball_v1', mathematical_direction='upper',
                   midpoint_integer=str(int(m)), radius_integer=str(int(r)),
                   decimal_exponent=str(int(e)))
        require(unpack(out).contains(value), 'complete serialization encloses its directed value')
        return out

    def saved_endpoint_fraction(value):
        n = int(value['midpoint_integer'])+int(value['radius_integer'])
        e = int(value['decimal_exponent'])
        return Fraction(n*10**e) if e >= 0 else Fraction(n, 10**(-e))

    def up(value):
        result = value.upper()
        require(result.is_finite() and result >= 0, 'finite nonnegative upper endpoint')
        return result

    def positive_inverse(value):
        require(value > 0, 'positive directed denominator endpoint')
        return (1/value).upper()

    def sqrt_upper(value):
        return up(value.upper().sqrt())

    identity = dict(kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
        original_candidate_sha256=CANDIDATE, original_mean_native_sha256=MEAN,
        original_mean_source_sha256=MEAN_SOURCE, object_sha256=OBJECT,
        exact_alpha=ALPHA, exact_nu=NU, exact_eta=ETA, arithmetic_bits=320,
        exact_interval=['0', '25/8'], compact_interval=['1/20', '9/50'],
        original_parameter_half_width='1/1000000000',
        intrinsic_box_used_only_as_enclosure_of_original_centre=True,
        original_modes=MODES, original_pieces=PIECES,
        tm_result_sha256=sha(args.tm_result.read_bytes()),
        tm_execution_sha256=sha(args.tm_execution.read_bytes()),
        c0_result_sha256=sha(args.c0_result.read_bytes()),
        c0_execution_sha256=sha(args.c0_execution.read_bytes()),
        old_process_sha256=sha(args.old_process.read_bytes()),
        raw_bounds_sha256=sha(args.raw_bounds.read_bytes()),
        source_proof_sha256=sha(args.source_proof.read_bytes()),
        localized_proof_sha256=sha(args.localized_proof.read_bytes()),
        geometry_proof_sha256=sha(args.geometry_proof.read_bytes()),
        geometry_norm='max component complete physical unnormalized C0_r_phi at the same moving angle')
    doc = dict(identity=identity, complete=False, proved=False, failure=None,
        stage='input-admission', expected_common_cells=ROWS, expected_mean_interfaces=JOINS,
        completed_common_cells=0, completed_mean_interfaces=0, completed_compact_cells=0,
        finite_coefficient_rows_evaluated=0, current_exact_right='0', current_candidate_piece=0,
        exact_parameters={}, complete_new_scalars={}, scalar_scope='accepted_row_prefix_only',
        saved_readback_count=0, strict_gates=dict(full_geometry_state_C0_sufficient_1e4='unknown'),
        scope=dict(original_Qraw_nu0_eta0_only=True, actual_complete_TM_radii_consumed=False,
            same_moving_phi_geometry_norm=True, complete_physical_amplitude_retained=True,
            original_all32_modes_retained=True, all_original_mean_interfaces_retained=True,
            old_raw_residual_and_jump_sums_read_only=True, detailed_rows_private_only=True,
            full_closed_row_sources=False, nonmean_equations_solved=False,
            nonmean_jumps_repaired=False, same_physical_theta_bound_computed=False,
            selected_delta_or_phase_inherited=False, exterior_jet_or_height_matched=False,
            remaining_exact_correction_must_be_added=True, failed_sufficient_gate_is_not_nonexistence=True,
            body_inverse_proved=False, final_topic_complete=False),
        private_trace=dict(records=0, bytes=0, sha256=hashlib.sha256().hexdigest(),
                           content_published=False, scope='accepted_complete_row_prefix'),
        seconds=0.0, **{key: 0 for key in ZERO_FIELDS})
    trace = args.output.with_name('private-localized-geometry-source.ndjson')
    candidate_file = args.output.with_name('candidate-localized-checkpoint.json')
    atomic(args.output, encode(doc))
    trace_hash, trace_bytes, trace_records = hashlib.sha256(), 0, 0

    try:
        expected = dict(tm_result_sha256=TM_SHA, tm_execution_sha256=TM_EXEC_SHA,
            c0_result_sha256=C0_SHA, c0_execution_sha256=C0_EXEC_SHA,
            raw_bounds_sha256=RAW_SHA, source_proof_sha256=CS_SHA,
            localized_proof_sha256=LC_SHA, geometry_proof_sha256=GEOMETRY_SHA)
        require(all(identity[key] == value for key, value in expected.items()),
                'exact complete actual and analytic inputs')
        tm, tex = parse(args.tm_result.read_bytes()), parse(args.tm_execution.read_bytes())
        require(tm['complete'] is True and tm['proved'] is True and tm['failure'] is None
                and tm['completed_scalar_stages'] == 5 and tm['saved_readback_count'] == 24
                and tm['scope']['passed_scalar_mean_root'] is True
                and tm['identity']['source_sha256'] == TM_SOURCE
                and tm['identity']['original_candidate_sha256'] == CANDIDATE
                and tm['identity']['original_mean_native_sha256'] == MEAN
                and tm['identity']['exact_alpha'] == ALPHA
                and tm['identity']['exact_nu'] == NU and tm['identity']['exact_eta'] == ETA
                and all(value is True for key, value in tm['strict_gates'].items()
                        if key != 'same_phi_moving_C0_sufficient_1e4'),
                'complete already proved terminal mean, compact root and density')
        require(tex['complete'] is True and tex['failure'] is None
                and tex['actual_child_returncode'] == 0 and tex['scientific_children'] == 1
                and tex['completed_new_terminal_mean_scalar_gate_targets'] == 1
                and tex['run_id'] == '45791979634' and tex['run_attempt'] == '1'
                and tex['scientific_files'][0]['sha256'] == TM_SHA
                and tex['old_completed_targets_recomputed'] == 0,
                'actual complete public terminal-mean execution')
        c0, cex = parse(args.c0_result.read_bytes()), parse(args.c0_execution.read_bytes())
        require(c0['complete'] is True and c0['proved'] is True and c0['failure'] is None
                and c0['scalar_scope'] == 'complete_whole_target'
                and c0['completed_common_cells'] == ROWS and c0['completed_mean_interfaces'] == JOINS
                and c0['completed_weighted_reverse_cells'] == ROWS
                and c0['identity']['original_candidate_sha256'] == CANDIDATE
                and c0['identity']['original_mean_native_sha256'] == MEAN
                and c0['identity']['exact_alpha'] == ALPHA
                and c0['identity']['exact_nu'] == NU and c0['identity']['exact_eta'] == ETA,
                'complete old whole mean and jump norm bounds')
        require(cex['complete'] is True and cex['failure'] is None
                and cex['actual_child_returncode'] == 0 and cex['scientific_children'] == 1
                and cex['completed_new_compact_moment_and_C0_receiver_targets'] == 1
                and cex['run_id'] == '45787608966' and cex['run_attempt'] == '1'
                and cex['scientific_files'][0]['sha256'] == C0_SHA,
                'actual original complete C0 execution')
        for value in tm['complete_new_scalars'].values():
            unpack(value)
        for value in c0['complete_new_scalars'].values():
            unpack(value)
        exact_rho, exact_b = Fraction(tm['exact_parameters']['rho']), Fraction(tm['exact_parameters']['b'])
        require(exact_rho == saved_endpoint_fraction(tm['complete_new_scalars']['rho_proposal_upper'])
                and exact_b == saved_endpoint_fraction(tm['complete_new_scalars']['b_proposal_upper'])
                and 0 < exact_rho < 1 and exact_b > 0,
                'actual saved complete upper endpoints, not midpoint proposals')
        rho, b, alpha = rat(exact_rho).upper(), rat(exact_b).upper(), rat(ALPHA)
        cs = c0['complete_new_scalars']
        mstar = unpack(cs['mean_abs_lower']).lower()
        Mstar = unpack(cs['mean_abs_upper']).upper()
        Jmean = unpack(cs['raw_mean_jump_sum_upper']).upper()
        require(mstar > 0 and Mstar >= mstar and Jmean >= 0 and b < mstar,
                'same actual complete strictly negative mean ball')
        doc['exact_parameters'] = dict(rho=str(exact_rho), b=str(exact_b))
        doc['scope']['actual_complete_TM_radii_consumed'] = True

        raw = args.mean.read_bytes()
        require(sha(raw) == MEAN, 'original complete unchanged mean native')
        native = parse(gzip.decompress(raw))
        process = parse(args.old_process.read_bytes())
        require(process['complete'] is True and process['actual_returncode'] == 0
                and process['result_complete'] is True and process['result_failure'] is None
                and process['out_sha256'] == MEAN and process['source_sha256'] == MEAN_SOURCE
                and process['completed_rows'] == ROWS and process['total_closed_cells'] == ROWS,
                'complete original scalar-mean process')
        require(native['kind'] == 'actual_final_complete_scalar_mean_Green_cached_full_target'
                and native['complete'] is True and native['failure'] is None
                and native['source_sha256'] == MEAN_SOURCE
                and native['candidate_sha256'] == CANDIDATE
                and native['exact_amplitude'] == ALPHA and native['exact_nu'] == NU
                and native['exact_interval'] == ['0', '25/8']
                and native['original_parameter_half_width'] == '1/1000000000'
                and native['whole_original_affine_parameter_interval'] is True
                and native['all_exact_mean_interfaces_retained'] is True
                and native['candidate_metadata']['modes'] == MODES
                and native['candidate_metadata']['object_sha256'] == OBJECT
                and len(native['rows']) == ROWS and len(native['interfaces']) == JOINS,
                'entire original point-enclosing raw object and all actual mean joins')
        rows = native['rows']
        joins = {item['common_row']: item for item in native['interfaces']}
        require(len(joins) == JOINS, 'all distinct original mean interfaces')
        cuts = {Fraction(row['interval'][0]) for row in rows}|{END}
        require(LEFT in cuts and RIGHT in cuts, 'both exact compact support boundaries')
        knots, coefficients = load_candidate(args.candidate)
        acc = {key: arb(0) for key in PREFIX_FIELDS}
        current_right, previous_piece = Fraction(0), None
        doc['stage'] = 'whole-row-localized-state-and-source-receivers'
        atomic(args.output, encode(doc))

        def coefficient_A0(piece, left, right):
            x = rat(left-knots[piece]).union(rat(right-knots[piece]))
            umax, wmax = arb(0), arb(0)
            for coordinate in tuple(range(MODES))+tuple(range(MODES+1, 2*MODES+1)):
                val = arb(0)
                for degree in range(4):
                    exact = Fraction.from_float(float(coefficients[degree, piece, coordinate]))
                    val = val*x+rat(exact)
                bound = up(abs(alpha*val))
                if coordinate < MODES:
                    umax = up(umax+bound)
                else:
                    wmax = up(wmax+bound)
            return umax, wmax

        with trace.open('wb') as stream:
            for i, row in enumerate(rows):
                left, right = map(Fraction, row['interval'])
                piece = int(row['candidate_piece'])
                require(row['common_row'] == i and left == current_right and left < right
                        and 0 <= piece < PIECES and knots[piece] <= left < right <= knots[piece+1],
                        'whole original closed row, exact piece and adjacency')
                gl, gr = map(Fraction, row['actual_scalar_germ'])
                require(gl <= left < right <= gr, 'original entire scalar germ containment')
                changed = previous_piece is not None and piece != previous_piece
                require((i in joins) is changed, 'every and only actual mean interface retained')
                if changed:
                    item = joins[i]
                    require(piece == previous_piece+1 and left == knots[piece]
                            and item['candidate_join'] == piece and Fraction(item['radius']) == left,
                            'all original consecutive candidate joins')
                target, mean = row['actual_target'], row['scalar_mean']
                mm = -old_ball(mean['actual_m'])
                ml, mu = max(mm.lower(), mstar).lower(), mm.upper()
                require(mm > 0 and ml > 0 and ml <= mu, 'complete actual negative mean enclosure')
                invm = positive_inverse(ml)
                beta = up(abs(old_ball(target['beta'])))
                K = up(abs(old_ball(target['K'])))
                gamma = old_ball(target['gamma'])
                require(gamma > 0, 'actual saved complete gamma row, not an inferred missing field')
                gamma = gamma.upper()
                U = up(old_ball(mean['nonmean_u_square']))
                V = up(old_ball(mean['nonmean_v_square']))
                us, vs = sqrt_upper(U), sqrt_upper(V)
                Z = up(vs*invm)
                UA, WA = coefficient_A0(piece, left, right)
                UA = min(UA, up(8*us)).upper()
                ZA = min(up(WA*invm), up(8*Z)).upper()
                chi = rat(compact_max(left, right)).upper()
                E = up(rho*chi)
                J = up(1+(1+E)*WA*invm)
                state_change = up(b*J+E*WA)
                Mb = up(mu+b)
                Kd = up(K*b*(2*mu+b))
                Kb = up(K*Mb**2)
                Ap, Bp = up(Kd+Kb*E), up(Kd+Kb*(2*E+E**2))
                T = up((2*Ap+Bp*ZA)*Z/4)
                D = up(beta*(UA*us+K*mu**2*(2+ZA)*Z)/4)
                fu = up(beta*(Kd+Bp*Z**2)*us)
                qu = up(beta*UA*T+gamma*Ap*Z)
                cv = up((1+b*invm)*(1+E)*sqrt_upper(1+Z**2))
                qv = up(Mb*(E*(D+gamma*us)+beta*(1+(1+E)*ZA)*T))
                length = rat(right-left)
                derivative_mass = rat(compact_derivative_square_mass(left, right))
                candidate = dict(acc)
                candidate['same_phi_C0_upper'] = max(acc['same_phi_C0_upper'], state_change).upper()
                candidate['sine_A0_upper'] = max(acc['sine_A0_upper'], UA).upper()
                candidate['cosine_nonmean_A0_upper'] = max(acc['cosine_nonmean_A0_upper'], WA).upper()
                candidate['density_A0_upper'] = max(acc['density_A0_upper'], J).upper()
                candidate['fu_squared_integral_upper'] = up(acc['fu_squared_integral_upper']+length*fu**2)
                candidate['qu_squared_integral_upper'] = up(acc['qu_squared_integral_upper']+length*qu**2)
                candidate['fv_chi_squared_integral_upper'] = up(
                    acc['fv_chi_squared_integral_upper']+(Mb*rho*Z)**2*derivative_mass)
                candidate['qv_squared_integral_upper'] = up(acc['qv_squared_integral_upper']+length*qv**2)
                candidate['cv_operator_upper'] = max(acc['cv_operator_upper'], cv).upper()
                item = dict(original_row=i, candidate_piece=piece,
                    exact_interval=[str(left), str(right)], same_phi_upper=record(state_change),
                    u_A0_upper=record(UA), w_A0_upper=record(WA),
                    source_squared_prefix={key: record(candidate[key]) for key in PREFIX_FIELDS
                                           if 'squared_integral' in key})
                trace_raw = encode(item)
                next_hash = trace_hash.copy()
                next_hash.update(trace_raw)
                prospective = parse(encode(doc))
                prospective['completed_common_cells'] = i+1
                prospective['completed_mean_interfaces'] += int(changed)
                prospective['completed_compact_cells'] += int(left >= LEFT and right <= RIGHT)
                prospective['finite_coefficient_rows_evaluated'] = i+1
                prospective['current_exact_right'] = str(right)
                prospective['current_candidate_piece'] = piece
                prospective['saved_readback_count'] += 1
                prospective['complete_new_scalars'] = {key: record(candidate[key]) for key in PREFIX_FIELDS}
                prospective['private_trace'] = dict(records=trace_records+1, bytes=trace_bytes+len(trace_raw),
                    sha256=next_hash.hexdigest(), content_published=False, scope='accepted_complete_row_prefix')
                prospective['seconds'] = time.monotonic()-began
                saved_raw = encode(prospective)
                atomic(candidate_file, saved_raw)
                readback_raw = candidate_file.read_bytes()
                require(readback_raw == saved_raw, 'exact complete prospective checkpoint bytes read back')
                saved = parse(readback_raw)
                require(saved == prospective and saved['completed_common_cells'] == i+1
                        and saved['current_exact_right'] == str(right)
                        and all(unpack(saved['complete_new_scalars'][key]).contains(candidate[key])
                                for key in PREFIX_FIELDS),
                        'whole prospective row saved and read back before acceptance')
                # The formal checkpoint is always a complete row.  If a later
                # step fails, exception handling reads this file, not partially
                # advanced local accumulators or counters.
                stream.write(trace_raw)
                stream.flush()
                atomic(args.output, readback_raw)
                doc = saved
                acc = {key: unpack(doc['complete_new_scalars'][key]).upper() for key in PREFIX_FIELDS}
                trace_hash, trace_bytes, trace_records = next_hash, trace_bytes+len(trace_raw), trace_records+1
                current_right, previous_piece = right, piece

        doc = parse(args.output.read_bytes())
        require(doc['completed_common_cells'] == ROWS
                and doc['completed_mean_interfaces'] == JOINS
                and doc['completed_compact_cells'] == c0['completed_compact_cells']
                and doc['finite_coefficient_rows_evaluated'] == ROWS
                and doc['current_exact_right'] == '25/8' and previous_piece == PIECES-1,
                'all original closed rows, compact rows and actual interfaces complete')
        acc = {key: unpack(doc['complete_new_scalars'][key]).upper() for key in PREFIX_FIELDS}
        fu, qu, fv, qv = (sqrt_upper(acc[key]) for key in
            ('fu_squared_integral_upper', 'qu_squared_integral_upper',
             'fv_chi_squared_integral_upper', 'qv_squared_integral_upper'))
        Eu = up(alpha*rat(Fraction(4201205, 10**14)))
        Ev = up(alpha*rat(Fraction(8194504, 10**14)))
        Ju = up(alpha*rat(Fraction(4404428, 10**19)))
        Jv = up(alpha*rat(Fraction(6408789, 10**19)))
        Fu, Fv = up(Eu+fu), up(acc['cv_operator_upper']*Ev+fv)
        invstar = positive_inverse(mstar)
        new_Jv = up((Mstar+b)*(1+rho)
            *(Jv*invstar+acc['cosine_nonmean_A0_upper']*Jmean*invstar**2))
        ordinary23 = (-(rat(4).log())*rat(Fraction(2, 3))).exp().upper()
        flux23 = ((rat(384).log())/3).exp().upper()
        u23 = up(ordinary23*Fu+flux23*qu)
        v23 = up(ordinary23*Fv+flux23*qv)
        v1 = up(Fv/4+qv)
        extra = dict(fu_L2_upper=fu, qu_L2_upper=qu, fv_chi_L2_upper=fv, qv_L2_upper=qv,
            Fu_complete_L2_upper=Fu, Qu_complete_L2_upper=qu,
            Fv_complete_L2_upper=Fv, Qv_complete_L2_upper=qv,
            unchanged_raw_Ru_L2_upper=Eu, unchanged_raw_Rv_L2_upper=Ev,
            unchanged_raw_u_jump_A0_upper=Ju, unchanged_raw_v_jump_A0_upper=Jv,
            new_complete_v_jump_A0_upper=new_Jv,
            first_row_Hminus2over3_upper=u23, second_row_Hminus2over3_upper=v23,
            second_row_Hminus1_upper=v1,
            isotropic_Hminus2over3_pair_upper=sqrt_upper(u23**2+v23**2),
            anisotropic_Hminus2over3_Hminus1_pair_upper=sqrt_upper(u23**2+v1**2))
        require(set(extra) == set(FINAL_FIELDS), 'all complete new derived output fields')
        doc['complete_new_scalars'].update({key: record(value) for key, value in extra.items()})
        doc['stage'] = 'all-complete-norms-saved-awaiting-readback'
        doc['saved_readback_count'] += 1
        doc['seconds'] = time.monotonic()-began
        raw = encode(doc)
        atomic(candidate_file, raw)
        readback_raw = candidate_file.read_bytes()
        require(readback_raw == raw, 'exact complete final derived checkpoint bytes read back')
        final = parse(readback_raw)
        require(final == doc and all(unpack(final['complete_new_scalars'][key]).contains(value)
                    for key, value in extra.items())
                and len(final['complete_new_scalars']) == len(PREFIX_FIELDS)+len(FINAL_FIELDS),
                'actual complete derived scalar readback')
        atomic(args.output, readback_raw)
        final = parse(args.output.read_bytes())
        upper = unpack(final['complete_new_scalars']['same_phi_C0_upper']).upper()
        final['strict_gates']['full_geometry_state_C0_sufficient_1e4'] = bool(
            upper <= rat(Fraction(1, 10000)).lower())
        final['complete'] = True
        final['proved'] = True
        final['scope']['full_closed_row_sources'] = True
        final['scalar_scope'] = 'complete_whole_target'
        final['stage'] = 'complete-localized-full-state-and-compact-source-receivers'
        final['seconds'] = time.monotonic()-began
        atomic(args.output, encode(final))
        print(json.dumps(dict(complete=True, complete_new_whole_bounds=True,
            whole_geometry_state_gate=final['strict_gates']['full_geometry_state_C0_sufficient_1e4'],
            common_cells=ROWS, original_interfaces=JOINS,
            same_physical_theta_grid_calls=0, old_targets_recomputed=0), sort_keys=True), flush=True)
    except BaseException as exc:
        doc = parse(args.output.read_bytes())
        doc['complete'] = False
        doc['proved'] = False
        doc['scope']['full_closed_row_sources'] = False
        doc['scalar_scope'] = 'accepted_row_prefix_only'
        doc['strict_gates']['full_geometry_state_C0_sufficient_1e4'] = 'unknown'
        doc['stage'] = 'failed-with-complete-accepted-row-prefix'
        doc['failure'] = dict(type=type(exc).__name__, message=str(exc))
        doc['seconds'] = time.monotonic()-began
        # A trace append may precede a failed formal checkpoint publication.
        # Remove only that unaccepted private tail; the saved prefix is intact.
        if trace.exists():
            with trace.open('r+b') as stream:
                stream.truncate(doc['private_trace']['bytes'])
        atomic(args.output, encode(doc))
        raise


if __name__ == '__main__':
    main()
