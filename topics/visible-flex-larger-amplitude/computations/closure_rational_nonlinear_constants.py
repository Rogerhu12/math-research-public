#!/usr/bin/env python3
"""Exact arithmetic ledger for R17's explicit local constants and N=4096.

Only the displayed constant comparisons are checked here. The proof of the
full nonlinear flow and its complete mean is in R17, using the pinned A/L/Q/F
equations. This file does not run or certify a finite nonlinear tail solve.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def two(k):
    return F(2**k) if k >= 0 else F(1, 2**(-k))


def record_fraction(q):
    return dict(exact=str(q), decimal=float(q))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-report', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    own_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw = args.source_report.read_bytes()
    data = json.loads(raw)
    model = data['model']
    physical = model['physicalParameters']
    epsilon_physical = F.from_float(physical['epsilonScale'])
    r_c = F.from_float(physical['rCuff'])
    epsilon_normalized = epsilon_physical / r_c**7

    n_local, n_tail = 512, 4096
    c0, cstar, Cstar = two(-240), two(-256), two(320)
    K0, Cmat, CG = two(16), two(52), two(27)
    M512 = 2**21 * (n_local + 8)
    M4096 = 2**21 * (n_tail + 8)
    relative_step = F(521, 520)

    # All log2 values below are *rational upper bounds* from the text.
    exponents = dict(
        forced_gain=F(6812 + 15*31) - F(14245, 2)*(n_local+7),
        forced_to_wmin=F(6812-240+8) - F(14247, 2)*(n_local+7),
        stronger_origin_radius=F(-192+6822) - F(14247, 2)*(n_local+7),
        jet_correction=F(6826+15*31) - F(7120)*(n_local+7),
        unit_local_radius=F(256+60*34) - F(3, 4)*(n_tail+7),
        unit_nonlinear_lipschitz=F(1+27+320)-F(11,2)+72*34-F(3,4)*(n_tail+7),
        actual_linear_perturbation=F(85)-F(n_tail,2),
        current_slope_local=F(6+15)-F(7,4)*(n_local+7),
        current_slope_tail=F(6+15)-F(7,4)*(n_tail+7),
        universal_slope_tail=F(6+7000)-F(7,4)*(n_tail+7),
    )

    checks = dict(
        source_definition=model['definition']=='visible-larger-rational-deep-alpha-v1',
        rational_region_starts_at160=model['start']==160,
        stored_epsilon_between_2pow14_and_2pow15=two(14)<epsilon_normalized<two(15),
        radius_positive=r_c>0,
        local_cutoff_base=M512**16 < 2**(n_local+7),
        local_cutoff_monotone=relative_step**16 < 2,
        one_plus_M512_below_2pow31=M512 < 2**31,
        one_plus_M4096_below_2pow34=M4096 < 2**34,
        short_transfer_integral=F(384)**4*two(-(n_local+7)) < F(2,3)**4,
        C_M_below23=1+F(15,8)/F(3,5)*7 < 23,
        exp_27over4_below_2pow11=F(27,4)<11*F(2,3),
        K_R_below_2pow6764=9+4*5+11+7*960 < 6764,
        low_Galerkin_bootstrap=4*Cmat*K0*K0*c0 < F(1,2),
        relative_mean_ball=two(36)*c0 < F(1,10000),
        global_physical_ball=two(40)*c0 < F(1,8000000),
        material_integral=106 < 2**7,
        raw_angular_derivative_bound=(1+F(576,7))**3 < 2**20,
        strong_envelope=1+16*6 < 2**7,
        raw_B_h=64*(1+12*6)**3 < 2**25,
        forced_gain=exponents['forced_gain'] < 0,
        forced_ball=exponents['forced_to_wmin'] < -22,
        stronger_origin_radius=exponents['stronger_origin_radius'] < 0,
        correction_jets=exponents['jet_correction'] < 0,
        Cauchy_ball=cstar <= c0/16,
        Cauchy_remainder=two(268) < Cstar,
        jets_constant=two(41) < Cstar,
        A_N_monotonicity=F(60,520) < F(3,4)*F(2,3),
        B_N_monotonicity=F(72,520) < F(3,8)*F(2,3),
        unit_local_radius=exponents['unit_local_radius'] < -2,
        unit_nonlinear_lipschitz=exponents['unit_nonlinear_lipschitz'] < -2,
        unit_linear_perturbation=exponents['actual_linear_perturbation'] < -2,
        current_slope_local=exponents['current_slope_local'] < 0,
        current_slope_tail=exponents['current_slope_tail'] < 0,
        universal_slope_tail=exponents['universal_slope_tail'] < 0,
        full_quarter_parameter_ball=32*2_000_000*two(-287) < 4,
        local_height_radius=F(1,4)/(2*2_000_000)==F(1,16_000_000),
    )
    result = dict(
        status='PASS' if all(checks.values()) else 'FAIL',
        exact_checks=checks,
        source_report=str(args.source_report),
        source_report_sha256=hashlib.sha256(raw).hexdigest(),
        entrypoint_sha256=own_hash,
        source_constants=dict(
            epsilon_physical=record_fraction(epsilon_physical),
            r_c=record_fraction(r_c),
            epsilon_normalized=record_fraction(epsilon_normalized),
            frozen_warp_alpha=physical.get('alpha', model['frozenWarpAlpha']),
            warp_scope='Retained shallow metric, outside the n>=160 unwarped deep estimates.',
        ),
        chosen_constants=dict(
            local_start=n_local, nonlinear_tail_start=n_tail,
            c_aux='2^-240', c_star='2^-256', C_star='2^320',
            low_propagator_constant='2^16', material_constant='2^52',
            forced_propagator_constant='2^6764',
            parameter_radius='1/4', low_height_radius='1/16000000',
        ),
        rational_log2_upper_bounds={k:record_fraction(v) for k,v in exponents.items()},
        limits=[
            'These constant inequalities accompany the full proof in R17.',
            'N4096 is an exact mathematical depth and is not directly representable as a double delta.',
            'A scaled bridge from numerical far192/256 to the exact nonlinear trace remains necessary.',
            'No shallow large-amplitude match, complete closed surface, or reach certificate is asserted.',
        ],
    )
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],checks=len(checks),
                          failed=[k for k,v in checks.items() if not v],
                          epsilon_normalized=float(epsilon_normalized),
                          N=n_tail,output=str(args.out))))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__=='__main__':
    main()
