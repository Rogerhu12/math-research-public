#!/usr/bin/env python3
"""Exact arithmetic for the conditional wide-strip linear head envelope.

No ODE is solved here. This bounds the exact linear image of R18's high-mode
deep trace. It does not bound nonlinear forcing generated within the head.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path


def two(n):
    return Q(2**n) if n>=0 else Q(1,2**(-n))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--ready',type=Path)
    p.add_argument('--prior-ledger',type=Path,default=Path('notes/2026-11-12-closure-scaled-f224-radius-ledger.json'))
    args=p.parse_args()
    checks={}
    checks['sqrt12_above_24over7']=Q(24,7)**2<12
    checks['old_radius_exponent_below_1over65']=Q(33,640)*Q(7,24)<Q(1,65)
    checks['old_cell_length_below_rc_delta']=Q(65,64)*Q(27,8)*Q(7,24)<1
    checks['quarter_root_upper']=Q(27,32)**4>Q(1,2)
    checks['geometric_w_ratio_upper']=Q(3,10)**4>Q(1,128)
    width=163*two(-18)+11*two(-12)*Q(27,32)/(1-Q(3,10))
    checks['radius_ratio_257over256']=width<Q(1,256)
    checks['radius_sixth_power']=Q(257,256)**6<Q(17,16)
    checks['radius_seventh_power']=Q(257,256)**7<2
    r1,r2=Q(91,128),Q(35,64)
    checks['r1_bound']=r1*r1>Q(1,2)
    checks['r2_bound']=r2**8>Q(1,128)
    checks['sqrt21_bound']=Q(23,5)**2>21
    checks['angle_first_coefficient']=Q(21,4)**2>=Q(4*163*5,128)
    checks['angle_second_coefficient']=(Q(320**2,220))**4>2**35
    geom=lambda r:1/(1-r)+r/(42*(1-r)**2)
    beta=Q(23,5)*(Q(21,4)*two(-6)*geom(r1)+320*two(-10)*r1*geom(r2))
    checks['total_linear_angle_loss_below4']=beta<4
    checks['short_base_cost']=Q(6*2**13,12)*two(-16)<=Q(1,16)
    checks['short_curvature_b_cost_at64']=two(33*4)*two(-71*3)<two(-20*4)
    checks['short_curvature_a_cost_at64']=2**5*73*two(-71*2)<two(-100)
    checks['short_curvature_diagonal_cost_at64']=two(17*2)*two(-71*3)<two(-80*2)
    checks['short_total_cost']=Q(1,16)+two(-19)<Q(1,8)
    checks['platform_weak_total_cost']=3*two(20)*two(-32)<Q(1,8)
    checks['warped_dominant_product']=(2**14+1)*(2**9+1)*(2**8+1)<2**32
    checks['unwarped_dominant_product']=65*3*2<2**9
    checks['physical_far_high_remainder']=Q(15)+15-Q(231*11,2)+1967-2*1947<-3167
    checks['angular_binary_penalty']=Q(175*7,10)<128-1-4
    bins=[]
    for k in range(6,25):
        m=94 if k==6 else 2**k
        switch=min(225,8*k+33)
        s=switch-1
        count=s-12+1
        energy=3*(12+s)*count//2+32*count
        conversion=(s+18)//2  # ceil((s+17)/2)
        warped=max(0,160-switch)
        unwarped=225-max(160,switch)
        degree=4*(1+warped+unwarped)
        power_bits=(m**degree-1).bit_length()
        exponent=-3167+energy+conversion+31*warped+11*unwarped+power_bits-175*m
        row=dict(binary_mode_bin=k,smallest_physical_frequency=m,
                 upper_frequency_exclusive=None if k==24 else 2**(k+1),
                 low_transfer_start=switch,energy_last_cell=s,
                 energy_log2_bound=energy,coordinate_conversion_log2_bound=conversion,
                 warped_low_cells=warped,unwarped_low_cells=unwarped,
                 polynomial_degree=degree,polynomial_at_first_log2_upper=power_bits,
                 final_physical_balanced_norm_log2_upper=exponent)
        bins.append(row)
    worst=max(x['final_physical_balanced_norm_log2_upper'] for x in bins)
    checks['within_bin_monotonicity']=max(x['polynomial_degree'] for x in bins)*2<175*94
    checks['all_high_modes_below_2pow_minus872']=worst<=-872
    finite_parameters=None
    hashes={}
    if args.ready:
        raw=args.ready.read_bytes();ready=json.loads(raw)
        params=ready['rationalDeepModel']['physicalParameters']
        rows=ready['shallowSourceParameters']['cells']
        used=[r for r in rows if r['n']>=12]
        alphas=[Q.from_float(r['alpha']) for r in used]
        def at(name,n,default):
            values=params.get(name) or []
            return values[n] if n<len(values) else default
        finite_parameters=dict(path=str(args.ready),count=len(used),
            all_required_cells_present=[r['n'] for r in used]==list(range(12,160)),
            all_alpha_in_half_to_two=all(Q(1,2)<=a<=2 for a in alphas),
            all_R_in_two_to64=all(2<=Q.from_float(r['R'])<=64 for r in used),
            all_R_equal64_after16=all(r['R']==64 for r in used if r['n']>=16),
            all_length_scale_one=all(r['lengthScale']==1 for r in used),
            all_delta_match_dyadic_recipe=all(Q.from_float(r['delta'])==Q.from_float(params['delta0'])*two(-r['n']) for r in used),
            all_deep_valley_controls_zero=all(at('valleyControls',n,0)==0 for n in range(12,160)),
            all_deep_warp_weights_one=all(at('warpWeightLevels',n,[1]*5)==[1]*5 for n in range(12,160)),
            all_deep_custom_caps_absent=all(not at('pulseCaps',n,None) and not at('valleyCaps',n,None) for n in range(12,160)),
            no_flat_override_after12=params.get('flatOuterThroughCell') is None or params['flatOuterThroughCell']<12,
            source_recipe_parameters=params['a']==2.75 and params['etaPower']==1.5 and params['etaRatioAtN0']==.05 and params['delta0']==.006 and params['protectCell']==160 and params['orientation']==1 and params.get('rejoinR20At') is None,
            cap_and_warp_parameters=Q(2)<Q.from_float(ready['rationalDeepModel']['frozenWarpAlpha'])<162 and params['curvatureBound']==8 and params['capTransition']==2 and params['slopeCap']==.02,
            radius_and_epsilon_parameters=Q(3,64)<Q.from_float(params['rCuff'])<Q(1,16) and 0<Q.from_float(params['epsilonScale'])/Q.from_float(params['rCuff'])**7<2**15,
            minimum_alpha=str(min(alphas)),maximum_alpha=str(max(alphas)),
            meaning='Ranges of the fixed binary source parameters, not exact-root claims.')
        for key,value in finite_parameters.items():
            if isinstance(value,bool):checks['finite_source_'+key]=value
        hashes[str(args.ready)]=hashlib.sha256(raw).hexdigest()
    diagnostic=None
    if args.prior_ledger.exists():
        raw=args.prior_ledger.read_bytes();old=json.loads(raw)['numerical_linear_diagnostic']
        vals=[x['F224']['log2_abs_low_height_coordinate']+(128-old['tau_F'])*x['mode']/math.log(2)
              for x in old['rows']]
        top=max(vals);norm=top+math.log2(sum(2**(x-top) for x in vals))
        diagnostic=dict(status='UNVERIFIED old finite-linear labels, not the depth12 actual trace',
                        tau_F=128,log2_low_height_l1=norm,
                        margin_to_wide_chart_bits=-1947-norm,
                        per_mode_log2=vals)
        hashes[str(args.prior_ledger)]=hashlib.sha256(raw).hexdigest()
    if not all(checks.values()):raise AssertionError([k for k,v in checks.items() if not v])
    out=dict(status='Exact arithmetic checks for a conditional exact-LINEAR head-envelope theorem',
             checks=checks,check_count=len(checks),
             width_over_rc_upper=dict(exact=str(width),decimal=float(width)),
             total_linear_angle_loss_upper=dict(exact=str(beta),decimal=float(beta)),
             physical_far_high_trace_norm_log2_upper=-3167,
             head_high_image_balanced_analytic_tau1_log2_upper=worst,
             bins=bins,finite_source_parameter_check=finite_parameters,
             unverified_wide_strip_diagnostic=diagnostic,input_hashes=hashes,
             entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             hypotheses=[
                 'Fixed source alpha_n in [1/2,2] for 12<=n<160; exact alpha=65/64 thereafter.',
                 'Current fixed warp alpha in (2,162), curvature cap 8, r_c>3/64, epsilon_normalized<2^15, and unchanged source length constants.',
                 'Source cells n>=12 have zero valley control, unit warp weights and no custom pulse/valley cap.',
                 'The R18 low46 height vector belongs to the tau_F=128 chart with l1 norm <=2^-1947.',
             ],
             limits=[
                 'This propagates the exact deep nonlinear HIGH trace through the exact LINEAR head only.',
                 'Nonlinear forcing generated inside the head and its coupling to the low46 trace are not included.',
                 'High cut height is an output and is allowed to change; no arbitrary full Dirichlet DN is asserted.',
                 'Neither floating ODE integration error nor source quadrature error is inferred from a profile fingerprint.',
             ])
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),checks=len(checks),angle_loss=float(beta),
                          high_image_log2=worst,wide_diagnostic=diagnostic)))


if __name__=='__main__':main()
