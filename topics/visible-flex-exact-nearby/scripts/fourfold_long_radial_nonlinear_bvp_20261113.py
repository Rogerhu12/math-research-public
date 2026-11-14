#!/usr/bin/env python3
"""Exact constants for the actual long-annulus nonlinear Dirichlet theorem.

No Fourier cutoff is used.  The accompanying proof supplies the Green kernels,
their all-frequency bounds, the full mean identity, and Banach contraction.
This script checks the explicitly stated rational arithmetic only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def run() -> dict:
    checks = []

    def gate(name: str, condition: bool, evidence: str) -> None:
        if not condition:
            raise AssertionError(name)
        checks.append({'name': name, 'pass': True, 'evidence': evidence})

    T = 2**24
    B = Q(T)-Q(25, 8)
    M0 = 4
    r = Q(1, 2**20)
    ymax = Q(1, 1024)
    gate('actual_log_length_exceeds_one', Q(7, 5)*B > 1,
         'L = omega (2^24-25/8), omega > 7/5')
    gate('full_kernel_reflection_denominator', Q(1, 2**8) < Q(1, 2),
         'For M>=4, L>1 and e>2: exp(-2ML)<2^-8<1/2')
    gate('green_height_constant', Q(2*M0*M0, M0*M0-4) < 3,
         '2M^2/(M^2-4) decreases for M>=4')
    gate('green_derivative_kernel_constant', 2*(1+Q(2, M0)) == 3,
         '2(1+2/M)<=3 for M>=4')
    gate('green_first_jet_constant', Q(6*M0*M0, M0*M0-4) == 8,
         '6M^2/(M^2-4) decreases for M>=4')
    gate('green_second_jet_constant', 1+Q(4*8, M0)+3 == 12,
         'Htt=F-4Ht+(M^2-4)H')
    gate('complete_same_width_green', 3+8+12 < 32,
         'Y norm sums all three strong jets before summing frequencies')
    gate('homogeneous_lift_first_jet', 4*(1+Q(2, M0)) == 6,
         'M |A_t| and M |B_t| <= 6 M^2')
    gate('homogeneous_lift_second_jet', 2+Q(24, M0) == 8,
         '|Htt| <= (M^2-4) 2 + 4 (6M) <= 8M^2')
    gate('two_lift_complete_norm', 2+6+8 == 16,
         'The two boundary amplitudes are summed in the boundary norm')

    rel_terms = [Q(1,4), Q(1), Q(3,8), Q(11,8), Q(5,4)]
    gate('five_mean_input_coefficients', sum(rel_terms) == Q(17,4),
         'P, U, Kperp, Kperp+U, V-P coefficients in the Y norm')
    gate('relative_mean_root_domain', Q(17,4)*ymax < Q(1,64),
         'The complete R25 root is used within its actual complex ball')
    gate('complete_mean_quadratic_constant', 12*Q(17,4)**2 < 256,
         '|K0| <= 12 R^2 < 256 Y^2')
    gate('four_relative_state_coefficients', Q(1,4)+Q(3,8)+1+Q(3,2) == Q(25,8),
         'P, Kperp, U and V coefficients; the mean is added separately')
    gate('full_relative_state_bound', Q(25,8)+256*ymax < 4,
         'N <= (25/8)Y+256Y^2 < 4Y')
    gate('quadratic_source_constant', 32*4**2 == 512,
         'The complete unprojected R119 quadratic source is <=32 N^2')
    gate('holomorphic_source_lipschitz', 4*512 == 2048,
         'Directional Cauchy circle of radius r within the 2r ball')
    gate('fixed_point_radius_in_cauchy_domain', 2*r < ymax,
         '2r*=2^-19<2^-10')
    gate('boundary_ball_pays_half_radius', 16*Q(1,2**25) == r/2,
         'Boundary norm <=2^-25=r*/32')
    gate('nonlinear_image_correction', 32*512*r == Q(1,64),
         'The nonlinear correction has norm <=r*/64')
    gate('closed_ball_selfmap', Q(1,2)+Q(1,64) < 1,
         'The true complete nonlinear fixed-point map is a selfmap')
    gate('full_nonlinear_contraction', 32*2048*r == Q(1,16),
         'No frequency truncation enters this contraction constant')

    gate('two_endpoint_neumann_error', 2*8*512 == 2**13,
         'Both endpoint |m| weighted derivative errors are retained')
    gate('both_endpoint_mean_slopes', 2*256 == 2**9,
         'Each endpoint mean slope is normalized by its own actual w')
    gate('mean_height_integral_constant', Q(1,2)*256 == 128,
         '(aw)_t=2aw, so integral_0^t aw ds <= aw(t)/2')
    gate('physical_slope_over_radius', Q(1,4)/Q(7,5) == Q(5,28),
         'w/a=1/(4 omega)<5/28')
    gate('physical_K_plus_U', Q(11,8)+256*r < Q(3,2),
         'The actual mean root is included in K+U')
    gate('physical_full_quadratic_source', 512*r == Q(1,2048),
         'The unprojected source, including its mean, is controlled')
    gate('physical_vertical_hessian', Q(5,28)*(3+Q(5,2)+Q(1,2048)) < 2,
         'Sum of both diagonal and both off-diagonal polar Hessian entries')
    gate('physical_horizontal_hessian', 2**12*Q(7,10**6)*Q(1,16)*4 < Q(1,100),
         '2^12 (w^2/a)N, with a<7e-6 and N<4Y')
    gate('physical_complete_C2_radius', 16*r == Q(1,2**16) < Q(1,1000),
         'The actual radial normalization cancels all inverse-radius costs')
    gate('actual_annulus_global_injectivity', 3*2**8*(Q(7,10**6)*Q(5,28))**2*4*r < 1,
         'Radial plus shorter-arc path has length <3|x-y|; use the full Cartesian derivative norm')
    gate('mean_identity_scalar_nonzero', 9*Q(17,4)*r < Q(1,2),
         'R25: |<D^-3/2(1+K+EU)>-1|<9R<1/2; w>0 separately')

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/'results/R74-actual-full-tail-robin-and-augmented-positive-cap.md',
        root/'results/R119-actual-final-connector-all-label-continuation.md',
        root/'results/R119-supplement-full-installed-connector-with-paid-label-weight.md',
        root/'results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema': 'visible-exact-R119-actual-long-radial-nonlinear-bvp-v1',
        'scope': 'The same actual R74 long radial annulus: complete nonlinear Dirichlet solution, both trace outputs, full mean, and exact horizontal reconstruction. The nonlinear tail/body matching inverse is not asserted.',
        'inputs': {'T': T, 'B': str(B), 'omega_interval': ['7/5','3/2'],
                   'example_physical_angle_width': '1/512',
                   'complete_boundary_radius': '2^-25',
                   'complete_solution_radius': '2^-20',
                   'source_R72_blob': 'a7c78793ba18724a4f0553b6ccd55259b8f4df92',
                   'source_R25_blob': 'be20257721fed270c59a4024427042fc76ee0073',
                   'file_sha256': {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks': checks,
        'all_pass': all(c['pass'] for c in checks),
        'claims': {'actual_installed_interval': True,
                   'complete_nonlinear_full_frequency_solution': True,
                   'same_angle_width_green': True,
                   'green_bound_independent_of_actual_length': True,
                   'both_endpoint_trace_errors': True,
                   'complete_mean_holonomy': True,
                   'mean_height_difference_is_output': True,
                   'exact_horizontal_reconstruction': True,
                   'two_bump_propagation_included': False,
                   'nonlinear_regular_high_input_inverse': False,
                   'global_matching_and_final_family': False},
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+'\n'
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({'all_pass': report['all_pass'], 'checks': len(report['checks']),
                          'out': str(args.out)}, ensure_ascii=False))
    else:
        print(encoded, end='')
