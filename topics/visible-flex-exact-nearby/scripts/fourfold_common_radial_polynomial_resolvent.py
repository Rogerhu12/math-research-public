#!/usr/bin/env python3
"""Exact finite budgets for the complete common radial port resolvent."""
from fractions import Fraction as Q
from pathlib import Path
import argparse,hashlib,json,time

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve each actual report')
    root=Path(__file__).resolve().parents[1]
    dependencies=[
      'R119-supplement-complete-radial-unitary-network-and-global-eigenphase.md',
      'R119-supplement-weighted-spectral-selection-one-common-radial-profile.md',
      'R119-supplement-scale-correct-polynomial-middle-scattering-generator.md',
      'R119-supplement-original-neutral-label-common-analytic-normalization.md']
    gates=[]
    def check(name,left,right,relation='<'):
        a,b=Q(left),Q(right)
        passed=(a<b) if relation=='<' else (a==b if relation=='=' else a<=b)
        gates.append(dict(name=name,left=str(a),right=str(b),relation=relation,passed=passed))
        if not passed:raise ArithmeticError(name)
    B,p=2200000,30697
    check('dimension_first_binary_block',16*985+642,16402,'=')
    check('dimension_block_slope',16,16402,'<=')
    check('dimension_binary_budget',16402,2**15)
    check('dimension_exponent_gap',15,984)
    check('resolvent_binary_constant',B+7,2200007,'=')
    check('resolvent_degree_before_dimension',p+2,30699,'=')
    check('resolvent_degree_after_dimension',p+3,30700,'=')
    check('original_label_remaining_degree',30960-30700,260,'=')
    check('generator_upper_below_phase_limit',Q(1,2**33),Q(1,8))
    check('positive_fourfold_bad_set_sum',Q(2,32*16),Q(1,256),'=')
    check('combined_bad_set',Q(1,256)+Q(83,16384),Q(147,16384),'=')
    check('joint_good_probability_positive',Q(147,16384),1)
    check('exp3_partial_sum_proves_log12point5',Q(25,2),1+3+Q(9,2)+Q(27,6))
    check('middle_log_constant',65536+320*3,66496,'=')
    check('middle_log_linear',204+320,524,'=')
    check('middle_log_constant_paid_at_first_layer',66496,(1024-524)*8198)
    check('generator_constant_paid_at_first_layer',B,512*8198)
    check('generator_complete_log_fee',p*1024+512,2**25)
    check('layer_block_initial_width',8193+511+5,8709,'=')
    check('layer_block_slope',512,8709,'<=')
    check('layer_block_binary_bound',8709,2**14)
    check('local_width_initial_exponent',155,Q(31*8193,256)-837)
    check('local_width_exponent_dominates_full_log_fee',25+14,155)
    check('local_width_block_growth',1,62)
    check('global_min_generator_log_block',B+985*p,2**25)
    check('global_min_generator_bound_by_M_over4',25,984-2)
    check('logM_Mover8_first_point',10,1024//8)
    check('logarithm_resolvent_L_remaining_constant',1+9,Q(11*1024,8))
    check('weighted_resolvent_log_at_first_layer',8,(8192-4096)*8198)
    check('weighted_resolvent_layer_exponent',13+14,155-3)
    check('two_local_weights_pay_generator_and_resolvent',1+Q(1,8),2)
    doc=dict(kind='complete_common_radial_polynomial_port_resolvent_exact_budget',
        complete=True,failure=None,gates=gates,checks=len(gates),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        proof_dependencies={n:hashlib.sha256((root/'results'/n).read_bytes()).hexdigest()
                            for n in dependencies},
        frequency_scope='M in 4N, M >= 2^984 * 25^(1/8)',
        generator_lower='2^-2200000 * M^-30697',
        complete_resolvent_upper='2^2200007 * d_M * M^30699 < 2^2200007 * M^30700',
        source_and_output_units='all exact canonical incoming ports of the full radial network',
        common_angular_width_preserved=True,port_derivative_loss=30700,
        old_local_two_sided_weights_preserved=True,
        ordinary_and_weak_physical_source_conversion_not_granted=True,
        nonlinear_or_nonradial_inverse_not_granted=True,
        wall_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print(json.dumps(dict(complete=True,checks=len(gates),out=str(args.out))))

if __name__=='__main__':main()
