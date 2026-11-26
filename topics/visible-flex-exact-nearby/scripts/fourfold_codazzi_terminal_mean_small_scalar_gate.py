#!/usr/bin/env python3
"""One new small-scalar terminal-to-compact-root certificate, public Actions only.

Read completed C0/profile scalars, the old saved initial D0 and the old
complete waist L2 receiver. No old target, native scan, radial ODE,
primitive, DFT or future forward endpoint is evaluated.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import time

REPO = 'Rogerhu12/math-research-public'
KIND = 'R144_terminal_mean_small_scalar_root_gate_v1'
C0_SHA = '0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641'
C0_EXEC_SHA = '9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc'
C0_SOURCE = '2f94b9a223fa99e63b2971c22f37796123b601565feb403ab81d2704438661a8'
INITIAL_SHA = '7cddc5856510c7e602a2e22d504492c8ab4732f900331c02e646f14b04da1635'
READABLE_SHA = '232a4bf0741eed57c5d5ae7e149795df1541e05236dc7afa05a60dc997094991'
RAW_SHA = '84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e'
PROOF_SHA = '5a7a5bf8b6873976d173bfc5be8c3b25fbcd03174e97ba56a4abd99e06440986'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
MEAN_NATIVE = 'e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b'
OLD_MEAN_SOURCE = '6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
ALPHA = '6890507429876859/9007199254740992'
NU = '-2572625729470897/72057594037927936'
ETA = '-7789843107295549/4611686018427387904'
WAIST_FIELD = 'complete_waist_mean_gain_if_log_Gamma_below_100/ordinary_mean_source_L2_r'
ZEROS = ('old_scientific_targets_recomputed native_rows_scanned radial_ODE_calls '
         'primitive_or_DFT_calls forward_W_targets_called published_arrays').split()


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


class UnprovedGate(Exception):
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--c0-result', type=Path, required=True)
    ap.add_argument('--c0-execution', type=Path, required=True)
    ap.add_argument('--initial-result', type=Path, required=True)
    ap.add_argument('--old-readable', type=Path, required=True)
    ap.add_argument('--raw-bounds', type=Path, required=True)
    ap.add_argument('--proof', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO, 'authorized public Actions only')
    require(not args.output.exists(), 'preserve each old complete, false, and partial attempt')
    from flint import arb, ctx
    ctx.prec = 320
    began = time.monotonic()

    def rat(value):
        q = Fraction(value)
        return arb(q.numerator)/arb(q.denominator)

    def unpack(value):
        require(value['kind'] == 'complete_decimal_ball_v1'
                and int(value['radius_integer']) >= 0, 'whole original decimal-ball schema')
        e = int(value['decimal_exponent'])
        scale = rat(10**e) if e >= 0 else rat(Fraction(1, 10**(-e)))
        m, r = rat(int(value['midpoint_integer']))*scale, rat(int(value['radius_integer']))*scale
        out = (m-r).lower().union((m+r).upper())
        require(out.is_finite(), 'finite whole decimal-ball readback')
        return out

    def old_ball(value):
        out = arb(value['lower']).lower().union(arb(value['upper']).upper())
        require(out.is_finite(), 'finite entire old waist-source ball')
        return out

    def record(value, direction='enclosure'):
        require(value.is_finite(), 'finite new scalar expression')
        m, r, e = value.mid_rad_10exp(75)
        result = dict(kind='complete_decimal_ball_v1', mathematical_direction=direction,
                      midpoint_integer=str(int(m)), radius_integer=str(int(r)),
                      decimal_exponent=str(int(e)))
        require(unpack(result).contains(value), 'complete saved scalar ball contains its value')
        return result

    doc = dict(identity=dict(kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
        original_candidate_sha256=CANDIDATE, original_mean_native_sha256=MEAN_NATIVE,
        exact_alpha=ALPHA, exact_nu=NU, exact_eta=ETA, exact_interval=['0', '25/8'],
        arithmetic_bits=320, proof_sha256=PROOF_SHA,
        c0_result_sha256=C0_SHA, c0_execution_sha256=C0_EXEC_SHA,
        initial_result_sha256=INITIAL_SHA, old_readable_sha256=READABLE_SHA,
        raw_bounds_sha256=RAW_SHA, old_waist_source_field=WAIST_FIELD,
        old_initial_field='complete_new_scalars.initial_D'),
        complete=False, proved=False, failure=None, unproved_gate=None, stage='input-admission',
        completed_scalar_stages=0, complete_new_scalars={}, exact_parameters={},
        saved_readback_count=0,
        strict_gates=dict(zero_parameter_contraction_gap='unknown',
            zero_parameter_ball='unknown', zero_parameter_Lipschitz='unknown',
            zero_parameter_mean_negative='unknown', waist_relative_shift_below_one='unknown',
            root_radius_in_unit_interval='unknown', unique_compact_root='unknown',
            uniform_contraction_gap='unknown', uniform_mean_ball='unknown',
            uniform_mean_Lipschitz='unknown', uniform_mean_negative='unknown',
            density_positive='unknown', same_phi_moving_C0_sufficient_1e4='unknown'),
        scope=dict(original_raw_eta0_nu0_only=True, old_initial_full_ball_retained=True,
            old_waist_L2_field_exact=True, all_raw_mean_jumps_retained=True,
            actual_future_forward_endpoint_consumed=False,
            proposals_are_exact_upper_endpoint_rationals=True,
            passed_scalar_mean_root=False, physical_angle_C0_proved=False,
            old_selected_phase_or_inverse_inherited=False, nonmean_equations_solved=False,
            nonmean_jumps_repaired=False, outer_radial_jet_or_height_matched=False,
            body_inverse_proved=False, final_topic_complete=False,
            failed_sufficient_test_is_not_nonexistence=True),
        seconds=0., **{k: 0 for k in ZEROS})

    def snapshot():
        doc['seconds'] = time.monotonic()-began
        atomic(args.output, encode(doc))

    def saved():
        return parse(args.output.read_bytes())

    def upper(name, value):
        doc['complete_new_scalars'][name] = record(value.upper(), 'upper')
        snapshot()
        back = saved()['complete_new_scalars'][name]
        out = unpack(back).upper()
        doc['saved_readback_count'] += 1
        return out

    def exact_upper_parameter(name, value):
        upper(name+'_proposal_upper', value)
        field = saved()['complete_new_scalars'][name+'_proposal_upper']
        exponent = int(field['decimal_exponent'])
        scale = Fraction(10**exponent) if exponent >= 0 else Fraction(1, 10**(-exponent))
        # This is the full saved upper endpoint, including the saved radius.
        q = Fraction(int(field['midpoint_integer'])+int(field['radius_integer']))*scale
        require(q > 0, 'strictly positive exact rational proposal')
        doc['exact_parameters'][name] = str(q)
        snapshot()
        qback = Fraction(saved()['exact_parameters'][name])
        require(qback == q, 'exact rational radius actual file readback')
        doc['saved_readback_count'] += 1
        return rat(qback)

    def gate(name, condition):
        doc['strict_gates'][name] = bool(condition)
        snapshot()
        if not saved()['strict_gates'][name]:
            raise UnprovedGate(name)

    snapshot()
    try:
        inputs = [
            (args.c0_result, C0_SHA), (args.c0_execution, C0_EXEC_SHA),
            (args.initial_result, INITIAL_SHA), (args.old_readable, READABLE_SHA),
            (args.raw_bounds, RAW_SHA), (args.proof, PROOF_SHA)]
        for path, expected in inputs:
            require(sha(path.read_bytes()) == expected, 'exact original small input '+path.name)
        c0, execution = parse(args.c0_result.read_bytes()), parse(args.c0_execution.read_bytes())
        require(c0['complete'] is True and c0['proved'] is True and c0['failure'] is None
                and c0['scalar_scope'] == 'complete_whole_target'
                and c0['completed_common_cells'] == 7721
                and c0['completed_mean_interfaces'] == 6143
                and c0['completed_weighted_reverse_cells'] == 7721
                and c0['current_exact_right'] == '25/8' and c0['current_H_exact_right'] == '9/50'
                and len(c0['complete_new_scalars']) == 52
                and c0['strict_gates']['compact_leverage_positive'] is True
                and c0['identity']['source_sha256'] == C0_SOURCE
                and c0['identity']['original_candidate_sha256'] == CANDIDATE
                and c0['identity']['original_mean_native_sha256'] == MEAN_NATIVE
                and c0['identity']['exact_alpha'] == ALPHA and c0['identity']['exact_nu'] == NU
                and c0['identity']['exact_eta'] == ETA,
                'actual complete original C0 and eleven-profile receiver')
        require(execution['complete'] is True and execution['failure'] is None
                and execution['actual_child_returncode'] == 0
                and execution['scientific_children'] == 1
                and execution['completed_new_compact_moment_and_C0_receiver_targets'] == 1
                and execution['old_completed_targets_recomputed'] == 0
                and execution['old_numerical_producers_called'] == 0
                and execution['run_id'] == '45787608966' and execution['run_attempt'] == '1'
                and execution['scientific_files'][0]['sha256'] == C0_SHA,
                'actual complete public C0 scientific execution')
        initial = parse(args.initial_result.read_bytes())
        require(initial['complete'] is True and initial['failure'] is None
                and initial['completed_common_cells'] == 7721
                and initial['completed_mean_interfaces'] == 6143
                and initial['identity']['original_candidate_sha256'] == CANDIDATE
                and initial['identity']['original_mean_native_sha256'] == MEAN_NATIVE
                and initial['identity']['exact_alpha'] == ALPHA
                and initial['identity']['exact_nu'] == NU
                and initial['identity']['original_parameter_half_width'] == '1/1000000000'
                and initial['identity']['initial_condition'] == 'Y_flat(0)=1; Y=a^2/m^2',
                'whole old saved initial D0 of the same raw fixed-centre enclosure')
        old = parse(args.old_readable.read_bytes())
        require(old['complete'] is True and old['native_sha256'] == MEAN_NATIVE
                and old['candidate_sha256'] == CANDIDATE
                and old['original_native_source_sha256'] == OLD_MEAN_SOURCE
                and old['actual_closed_cells'] == 7721
                and old['actual_candidate_mean_interfaces'] == 6143,
                'same complete old ordinary-mean waist operator')
        ww = [x for x in old['gates'] if x['name'] == WAIST_FIELD]
        require(len(ww) == 1 and ww[0]['passed'] is True,
                'exact complete old waist L2 field, not the whole-body L2 coefficient')
        Lw = old_ball(ww[0]['value']).upper()
        values = c0['complete_new_scalars']
        for item in values.values():
            unpack(item)
        def up(name):
            return unpack(values[name]).upper()
        K0, KJ = up('K0_ordinary_mean_C0_upper'), up('KJ_all_common_jumps_C0_upper')
        Rstar, Jstar = up('raw_mean_residual_upper'), up('raw_mean_jump_sum_upper')
        mstar = unpack(values['mean_abs_lower']).lower()
        vgap = unpack(values['raw_v_gap_lower']).lower()
        a_lower = unpack(values['abar']).lower()
        Vstar, Zstar = up('variance_upper'), up('density_variance_ratio_sqrt_upper')
        C = {key: up('C'+key+'_profile_kernel_upper')
             for key in ('01', '02', '10', '11', '12', '20', '21', '22', '30', '31', '32')}
        require(mstar > 0 and vgap > 0 and a_lower > 0
                and all(x >= 0 for x in (K0, KJ, Rstar, Jstar, Vstar, Zstar, Lw, *C.values())),
                'complete positive original charts and nonnegative receiver uppers')
        doc['stage'] = 'zero-parameter-terminal-fixed-point'
        E = upper('E_ordinary_and_mean_jumps_upper', K0*Rstar+KJ*Jstar)
        gap0 = 1-C['10']
        gate('zero_parameter_contraction_gap', gap0.lower() > 0)
        b0 = exact_upper_parameter('b0', 17*E/(16*gap0.lower()))
        S0 = upper('zero_parameter_selfmap_upper', E+C['10']*b0+C['20']*b0**2+C['30']*b0**3)
        L0 = upper('zero_parameter_Lipschitz_upper', C['10']+2*C['20']*b0+3*C['30']*b0**2)
        gate('zero_parameter_ball', S0.upper() <= b0.lower())
        gate('zero_parameter_Lipschitz', L0.upper() < 1)
        gate('zero_parameter_mean_negative', b0.upper() < mstar)
        doc['completed_scalar_stages'] = 1
        doc['stage'] = 'terminal-waist-and-normalized-forward-constant'
        Ev = upper('physical_raw_Rv_L2_upper', rat(ALPHA)*rat(Fraction(8194504, 10**14)))
        Bw = upper('terminal_waist_from_L2_upper',
                   Lw*Ev+KJ*Jstar+C['10']*b0+C['20']*b0**2+C['30']*b0**3)
        bw = upper('terminal_waist_shift_upper', min(b0.upper(), Bw).upper())
        t = upper('terminal_waist_relative_shift_upper', bw/mstar)
        gate('waist_relative_shift_below_one', t.upper() < 1)
        d0 = upper('absolute_saved_initial_D_upper',
                   abs(unpack(initial['complete_new_scalars']['initial_D'])))
        # t is a saved whole upper endpoint. The exact scalar function below
        # is increasing on [0,1); its denominator is a positive endpoint gap.
        d = upper('normalized_forward_constant_absolute_upper',
                  d0+(1+d0)*t*(2-t)/(1-t)**2)
        doc['completed_scalar_stages'] = 2
        doc['stage'] = 'unique-compact-quadratic-root'
        rho = exact_upper_parameter('rho', 17*d/(16*a_lower))
        gate('root_radius_in_unit_interval', rho.lower() > 0 and rho.upper() < 1)
        # This is an inequality with a LOWER rhs. Keep its full directed
        # lower record separately; an rhs upper cannot prove the root gate.
        rhs = a_lower*rho*(1-rho/2)
        doc['complete_new_scalars']['root_margin_rhs_lower'] = record(rhs.lower(), 'lower')
        snapshot()
        rhs_lower = unpack(saved()['complete_new_scalars']['root_margin_rhs_lower']).lower()
        doc['saved_readback_count'] += 1
        gate('unique_compact_root', d.upper() < rhs_lower)
        doc['completed_scalar_stages'] = 3
        doc['stage'] = 'uniform-parameter-terminal-fixed-point'
        A0 = upper('profile_A0_upper', rho*C['01']+rho**2*C['02'])
        A1 = upper('profile_A1_upper', C['10']+rho*C['11']+rho**2*C['12'])
        A2 = upper('profile_A2_upper', C['20']+rho*C['21']+rho**2*C['22'])
        A3 = upper('profile_A3_upper', C['30']+rho*C['31']+rho**2*C['32'])
        gap = 1-A1
        gate('uniform_contraction_gap', gap.lower() > 0)
        b = exact_upper_parameter('b', 17*(E+A0)/(16*gap.lower()))
        S = upper('uniform_selfmap_upper', E+A0+A1*b+A2*b**2+A3*b**3)
        L = upper('uniform_Lipschitz_upper', A1+2*A2*b+3*A3*b**2)
        gate('uniform_mean_ball', S.upper() <= b.lower())
        gate('uniform_mean_Lipschitz', L.upper() < 1)
        gate('uniform_mean_negative', b.upper() < mstar)
        doc['completed_scalar_stages'] = 4
        doc['stage'] = 'density-and-independent-moving-norm'
        density = upper('density_numerator_change_upper', 8*rho*Vstar.sqrt().upper())
        gate('density_positive', density.upper() < vgap)
        moving = upper('same_phi_moving_C0_upper',
                       b*(1+(1+rho)*8*Zstar)+8*rho*Vstar.sqrt().upper())
        doc['strict_gates']['same_phi_moving_C0_sufficient_1e4'] = bool(moving.upper() <= rat(Fraction(1, 10000)).lower())
        doc['completed_scalar_stages'] = 5
        doc['stage'] = 'all-gates-saved-awaiting-final-readback'
        snapshot()
        final = saved()
        require(final['complete'] is False and final['proved'] is False
                and final['completed_scalar_stages'] == 5
                and all(final['strict_gates'][k] is True
                        for k in final['strict_gates'] if k != 'same_phi_moving_C0_sufficient_1e4'),
                'actual saved complete dependent scalar gates')
        final['scope']['passed_scalar_mean_root'] = True
        final['proved'] = True
        final['complete'] = True
        final['stage'] = 'complete-terminal-mean-small-scalar-root-certificate'
        final['seconds'] = time.monotonic()-began
        atomic(args.output, encode(final))
        print(json.dumps(dict(complete=True, proved_scalar_mean_root=True,
            same_phi_moving_C0_sufficient_1e4=final['strict_gates']['same_phi_moving_C0_sufficient_1e4'],
            native_rows_scanned=0, forward_W_targets_called=0,
            old_waist_field=WAIST_FIELD), sort_keys=True), flush=True)
    except UnprovedGate as exc:
        doc = saved()
        doc['complete'] = True
        doc['proved'] = False
        doc['failure'] = None
        doc['stage'] = 'complete-sufficient-gate-not-proved'
        doc['unproved_gate'] = str(exc)
        doc['scope']['passed_scalar_mean_root'] = False
        doc['seconds'] = time.monotonic()-began
        atomic(args.output, encode(doc))
        print(json.dumps(dict(complete=True, proved_scalar_mean_root=False,
                              unproved_sufficient_gate=str(exc),
                              no_nonexistence_claim=True), sort_keys=True), flush=True)
    except BaseException as exc:
        doc = saved()
        doc['complete'] = False
        doc['proved'] = False
        doc['stage'] = 'failed-with-saved-scalar-prefix'
        doc['failure'] = dict(type=type(exc).__name__, message=str(exc))
        doc['scope']['passed_scalar_mean_root'] = False
        doc['seconds'] = time.monotonic()-began
        atomic(args.output, encode(doc))
        raise


if __name__ == '__main__':
    main()
