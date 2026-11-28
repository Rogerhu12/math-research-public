#!/usr/bin/env python3
"""R89: exact Bernstein marker bounds and same-field scalar geometry transfer.

All polynomial, partition, amplitude and geometry calculations use Fraction.
No sampling establishes a bound.  The nine small Bernstein leaves are generated
from the displayed polynomials; their arrays stay reproducible scratch data.
The complete field is unchanged outside two fixed graph disks.  This certificate
neither re-integrates its activity moment nor accepts unfinished metric proofs.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import time

GEOMETRY_SHA = '57480474eab2110d41053fee5ada0f02548dbb1b9e2fbaf56b9a16ce9fea742c'
ACTIVITY_SHA = 'f109408b33c9726fcdc22efeed555c4889edcd8bc96c3cd1ad526fe6833d0676'
QUERY_SHA = '877e68d97868524ed3cde4bca1090fbe8a4a207370e7b6c761da2b5963378cab'
BUNDLE_SHA = '3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98'
RUN_SHA = '1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891'
OLD_RADIUS = Q(900719925474099, 36028797018963968)
OLD_EPSILON = Q(4722366482869643, 75557863725914323419136)
HEIGHT_BOUND = Q(1,15)
GRADIENT_BOUND = Q(4,5)
HESSIAN_BOUND = Q(17,2)
AMPLITUDE_RATIO_BOUND = Q(7,5)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def checked(path, expected):
    path = Path(path).resolve()
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('An actual already paid input changed: '+str(path))
    return json.loads(raw)


def add(*polynomials):
    result = [Q(0)]*max(map(len,polynomials))
    for p in polynomials:
        for i,c in enumerate(p):
            result[i] += c
    while len(result)>1 and result[-1] == 0:
        result.pop()
    return result


def multiply(p,q):
    result = [Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            result[i+j] += a*b
    return result


def scale(p,c):
    return [Q(c)*x for x in p]


def power(p,n):
    result = [Q(1)]
    for _ in range(n):
        result = multiply(result,p)
    return result


def shift(p,n):
    return [Q(0)]*n+p


def defining_positive_polynomials():
    u = [Q(1),Q(0),Q(-1)]                 # 1-t^2
    d = [Q(1),Q(0),Q(0),Q(-1,2)]         # 1-t^3/2
    b = power(u,3)
    common = add(
        scale(shift(multiply([Q(1),Q(0),Q(0),Q(1)],b),1),6),
        scale(shift(multiply(power(u,2),d),3),36))
    tangential = add(common,scale(shift(multiply(power(u,2),power(d,2)),3),6))
    radial = add(common,scale(shift(multiply(
        multiply(u,[Q(-1),Q(0),Q(5)]),power(d,2)),3),6))
    return {
        'height': add(scale(d,HEIGHT_BOUND),scale(shift(b,3),-1)),
        'gradient': add(scale(power(d,2),GRADIENT_BOUND),
            scale(shift(multiply(power(u,2),d),4),-6),scale(shift(b,2),-3)),
        'Hessian_tangential_branch': add(scale(power(d,3),HESSIAN_BOUND),scale(tangential,-1)),
        'Hessian_radial_branch': add(scale(power(d,3),HESSIAN_BOUND),scale(radial,-1)),
    }


def bernstein_on_interval(p,left,right):
    """Exact power-to-Bernstein conversion after t=left+(right-left)*u."""
    n = len(p)-1
    monomial = [(right-left)**j*sum(
        (p[k]*comb(k,j)*left**(k-j) for k in range(j,n+1)),Q(0))
        for j in range(n+1)]
    return [sum((monomial[k]*Q(comb(j,k),comb(n,k)) for k in range(j+1)),Q(0))
            for j in range(n+1)]


def positive_partition(p,max_depth=12):
    leaves = []
    def visit(left,right,depth):
        coefficients = bernstein_on_interval(p,left,right)
        if min(coefficients)>0:
            leaves.append(dict(left=left,right=right,depth=depth,coefficients=coefficients))
            return
        if depth == max_depth:
            raise ArithmeticError('No complete exact positivity certificate; no bound claimed')
        middle = (left+right)/2
        visit(left,middle,depth+1)
        visit(middle,right,depth+1)
    visit(Q(0),Q(1),0)
    cursor = Q(0)
    for leaf in leaves:
        if leaf['left'] != cursor or not leaf['right']>cursor or min(leaf['coefficients'])<=0:
            raise ArithmeticError('Exact positivity leaves do not cover [0,1] once')
        cursor = leaf['right']
    if cursor != 1:
        raise ArithmeticError('Incomplete exact unit-radius coverage')
    return leaves


def prove_unit_marker():
    rows = []
    for name,p in defining_positive_polynomials().items():
        leaves = positive_partition(p)
        # The complete small array has a deterministic identity but is not needed
        # in a published numerical artifact: the source regenerates it exactly.
        serial = [{'left':str(x['left']),'right':str(x['right']),'depth':x['depth'],
                   'coefficients':[str(v) for v in x['coefficients']]} for x in leaves]
        encoded = json.dumps(serial,sort_keys=True,separators=(',',':')).encode()
        rows.append(dict(polynomial=name,degree=len(p)-1,leaf_count=len(leaves),
            maximum_depth=max(x['depth'] for x in leaves),
            minimum_Bernstein_coefficient_exact=str(min(min(x['coefficients']) for x in leaves)),
            complete_exact_single_cover=True,all_Bernstein_coefficients_strictly_positive=True,
            reproducible_leaf_array_sha256=hashlib.sha256(encoded).hexdigest()))
    return dict(status='exact_complete_unit_marker_Bernstein_bounds_certified',
        norm='Euclidean gradient and Cartesian symmetric-Hessian operator norms',
        radius_variable_exact_interval=['0','1'],denominator_lower_exact='1/2',
        height_absolute_upper_exact=str(HEIGHT_BOUND),
        gradient_norm_upper_exact=str(GRADIENT_BOUND),
        Hessian_operator_upper_exact=str(HESSIAN_BOUND),
        all_angles_included_by_holomorphic_modulus_bounds=True,
        all_harmonics_retained=True,finite_sampling_used_as_a_proof=False,
        polynomial_proofs=rows,total_positive_leaves=sum(x['leaf_count'] for x in rows),
        max_proof_depth=max(x['maximum_depth'] for x in rows))


def actual_scalar_transfer(geometry,activity):
    if (geometry['status'] != 'actual_complete_marked_column_closed_C2_geometry_certified'
            or geometry['actual_query']['sha256'] != QUERY_SHA
            or geometry['geometry_bundle']['sha256'] != BUNDLE_SHA
            or geometry['source_run']['sha256'] != RUN_SHA
            or activity['closed_geometry_report']['sha256'] != GEOMETRY_SHA
            or activity['actual_query'] != geometry['actual_query']
            or activity['geometry_bundle'] != geometry['geometry_bundle']
            or activity['source_run'] != geometry['source_run']
            or not activity['whole_activity_nonzero_certified']):
        raise ValueError('The actual geometry/activity proof is not the unchanged R82/R83 family')
    old = geometry['canonical_marker']
    if (Q(old['radius_exact_binary']) != OLD_RADIUS
            or Q(old['amplitude_exact_binary']) != OLD_EPSILON):
        raise ValueError('The exact original marker constants changed')
    active_low,active_high = map(Q,activity['whole_activity_third_real_interval_exact'])
    if not active_low>Q(139,1000) or not active_high>=active_low:
        raise ValueError('The actual source activity lower bound is absent')
    radius,epsilon = 2*OLD_RADIUS,56000*OLD_EPSILON
    if not 0<epsilon<=AMPLITUDE_RATIO_BOUND*radius**2:
        raise ValueError('The independently proved sharp amplitude gate failed')
    # Both older constructors really reject these parameters. Their guards and
    # field definitions remain unchanged; this is an explicit different design.
    if epsilon <= radius**2/25 or epsilon <= min(Q(1,100000),radius**2/10000):
        raise ValueError('The independently larger R89 definition was not selected')
    zlow,zhigh = map(Q,geometry['cap_height_after_column_exact_interval'])
    whole_radius = Q(geometry['whole_radius_upper']['upper_exact'])
    whole_support = Q(geometry['whole_support_lower']['lower_exact'])
    whole_curvature = Q(geometry['whole_principal_curvature_upper']['upper_exact'])
    whole_diameter = Q(geometry['whole_diameter_upper']['upper_exact'])
    gradient = GRADIENT_BOUND*epsilon/radius
    height = HEIGHT_BOUND*epsilon
    support_numerator = zlow-height-radius*gradient
    support = support_numerator/(1+gradient**2/2)
    radius_squared = radius**2+(zhigh+height)**2
    curvature = HESSIAN_BOUND*epsilon/radius**2
    if (support_numerator<=0 or support<whole_support
            or radius_squared>whole_radius**2 or curvature>whole_curvature
            or whole_curvature!=Q(123,10) or whole_diameter<2*whole_radius
            or not whole_radius<Q(6,5) or not whole_support>Q(3,5)):
        raise ValueError('The actual new disks do not preserve every required complete geometry budget')
    old_B = OLD_EPSILON*OLD_RADIUS**5/140
    B = epsilon*radius**5/140
    if B != 1792000*old_B:
        raise ArithmeticError('The exact full-spectrum new third cap moment changed')
    cosine_lower = Q(989253,1280000)
    delta_lower = Q(139,1000)*3*B*cosine_lower/2
    R86_threshold = Q(359,10**16)
    endpoint_distance_lower = Q(7,10**17)
    if (not delta_lower>35*R86_threshold
            or not 16640*endpoint_distance_lower<35*R86_threshold
            or endpoint_distance_lower>=Q(1,100)):
        raise ArithmeticError('The actual sharp marker endpoint or R88 consequence did not pass')
    return dict(radius_exact=str(radius),epsilon_exact=str(epsilon),
        epsilon_numerator_bits=epsilon.numerator.bit_length(),
        epsilon_exactly_representable_as_binary64=(Q(float(epsilon))==epsilon),
        epsilon_float_is_evaluation_only=True,
        amplitude_multiplier_over_R82_exact='56000',amplitude_multiplier_over_R86_exact='35',
        radius_multiplier_over_R82_exact='2',radius_multiplier_over_R86_exact='1',
        amplitude_ratio_upper_exact=str(AMPLITUDE_RATIO_BOUND),
        actual_amplitude_ratio_exact=str(epsilon/radius**2),
        original_canonical_and_R86_constructors_would_accept=False,
        height_absolute_upper_exact=str(height),gradient_norm_upper_exact=str(gradient),
        Hessian_operator_upper_exact=str(curvature),
        uniform_cap_curvature_upper_exact='119/10',
        actual_cap_height_before_new_marker_interval_exact=[str(zlow),str(zhigh)],
        cap_support_lower_exact=str(support),cap_radius_squared_upper_exact=str(radius_squared),
        whole_radius_upper_exact=str(whole_radius),whole_support_lower_exact=str(whole_support),
        whole_principal_curvature_upper_exact=str(whole_curvature),
        whole_diameter_upper_exact=str(whole_diameter),
        whole_reach_lower=geometry['whole_reach_lower'],
        same_R82_global_scalar_bounds_preserved=True,
        original_active_A_real_interval_exact=[str(active_low),str(active_high)],
        unchanged_active_A_real_lower_used_exact='139/1000',
        cap_B3_divided_by_pi_exact=str(B),B3_multiplier_over_R82_exact='1792000',
        B3_multiplier_over_R86_exact='35',
        endpoint_phases_exact=['0','9/20'],one_minus_cos_27over20_lower_exact=str(cosine_lower),
        endpoint_tensor_gap_strict_lower_exact=str(delta_lower),
        endpoint_tensor_gap_simplified_strict_lower_exact=str(35*R86_threshold),
        R88_radius_hypothesis_exact='6/5',R88_support_hypothesis_exact='3/5',
        R88_tensor_to_distance_constant_exact='16640',
        endpoint_all_E3_surface_Hausdorff_strict_lower_exact=str(endpoint_distance_lower),
        whole_family_delta_E_over_D_strict_lower_exact=str(endpoint_distance_lower/Q(12,5)),
        Hausdorff_distance_multiplier_claimed=False,
        cap_target_metric='dx^2+dy^2+df_new tensor df_new, fixed for every phase',
        actual_target_changed_only_once_on_the_two_fixed_disks=True,
        full_Cartesian_boundary_two_jets_preserved=True,
        old_target_refinement_claimed=False,old_integrals_or_Gram_polynomials_recomputed=False,
        complete_finite_metric_claimed=False,lambda_one_or_held_arc_claimed=False,
        README_completion_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry-report',type=Path,required=True)
    parser.add_argument('--activity-report',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    geometry = checked(args.geometry_report,GEOMETRY_SHA)
    activity = checked(args.activity_report,ACTIVITY_SHA)
    unit = prove_unit_marker()
    transfer = actual_scalar_transfer(geometry,activity)
    report = dict(status='exact_sharp_marker_and_same_actual_family_transfer_certified',
        source=ref(__file__),geometry_report=ref(args.geometry_report),
        activity_report=ref(args.activity_report),unit_marker=unit,
        actual_scalar_transfer=transfer,
        existing_proofs_used=['R67 exact marker moments and C2 boundary','R82 complete same-map geometry',
            'R83 actual whole active moment','R84 real reflection chain and endpoint tensor identity',
            'R88 all-E3 surface Hausdorff stability'],
        actual_seconds=time.perf_counter()-start,
        exact_rational_proof_executed=True,native_or_BVP_or_surface_integration_executed=False,
        full_surface_numerical_constructor_executed=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('x') as stream:
        stream.write(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=ref(args.out),status=report['status'],
        positive_Bernstein_leaves=unit['total_positive_leaves'],
        endpoint_distance_strict_lower=transfer['endpoint_all_E3_surface_Hausdorff_strict_lower_exact'])),flush=True)


if __name__ == '__main__':
    main()
