#!/usr/bin/env python3
"""R960: consume the same-job complete E65/E89 sources on the original angle.

No producer invocation, generated-file input, output file, numerical root or
coefficient table.  All divisibility and Bezout claims return every coefficient.
Called only by the public complete E65 producer after its full source gates.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
import math
from flint import fmpq as Q, fmpq_poly as Poly


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def encode(p):
    return [str(p[j]) for j in range(p.degree()+1)]


def exact_quotient(p, q):
    value, remainder = divmod(p, q)
    assert remainder == 0 and value*q == p
    return value


def factor_order(p, q):
    assert p != 0 and q.degree() > 0
    original, order = p, 0
    while True:
        quotient, remainder = divmod(p, q)
        if remainder != 0:
            break
        assert quotient*q == p
        order += 1
        p = quotient
    assert q**order*p == original
    assert p.gcd(q).degree() == 0
    return order, p


def floor(q):
    q = Fraction(q)
    return q.numerator//q.denominator


def ceil(q):
    return -floor(-Fraction(q))


def rational_receipt(value):
    value = Fraction(str(value))
    assert value
    return {"sha256":hashlib.sha256(str(value).encode()).hexdigest(),
            "numerator_bits":abs(value.numerator).bit_length(),
            "denominator_bits":value.denominator.bit_length()}


def product(factors, denominator=1):
    value = Poly([1])
    for factor in factors:
        value *= Poly(factor)
    return value/Q(denominator)


def low_jet_angle(p):
    # The same original sigma^(2n)*x^(n-3)*p(b/x^3), in t=-b/x^3.
    return Poly([0]+[(-1)**(j+1)*p[j] for j in range(p.degree()+1)])


def complete_source_angle(coefficients, degree):
    values = [Q(0)]*(degree+1)
    for j, c in enumerate(coefficients):
        values[degree-j] = (-1)**(degree-j)*Q(str(c))
    value = Poly(values)
    assert value[0] == 0 and value[1] == -1
    return value


def original_e65_angular_profile(coefficients, old_e89_coefficients):
    assert len(coefficients) == 65 and coefficients[-1] == 1
    assert len(old_e89_coefficients) == 29 and old_e89_coefficients[-1] == 1
    t = Poly([0,1])
    points = [("t0",t,1), ("t1",t-1,1),
              ("h7_two_geometric_roots",Poly([7,4,16]),2)]
    a = t*(t-1)*points[2][1]
    d = 1+8*t
    fS = a*d/7
    pS = product([[1,1],[1,-8],[7,-4,16]],7)
    pT = pS*product([[1,4],[1,-96,48,64],[1,20,-8]])
    pU = product([[1,1],[1,20,-8],[7,-4,16],
        [1,40,2112,3136,1792],[13,52,1536,1024,256],
        [1,1232,-58688,-49408,-439040,-2111488,-1949696,-851968,-32768]],91)
    pV = product([[1,1],[1,-8],[1,-8],[1,4],[7,-4,16],[1,228,48,64]],7)
    assert low_jet_angle(pS) == fS
    fT, fU, fV = [low_jet_angle(p) for p in (pT,pU,pV)]
    fW = complete_source_angle(old_e89_coefficients,29)
    fZ = complete_source_angle(coefficients,65)
    sources = [("S34",17,fS),("T72",36,fT),("U136",68,fU),
               ("V66",33,fV),("W178",89,fW),("Z390",195,fZ)]
    assert [p.degree() for name,charge,p in sources[:5]] == [5,11,22,10,29]
    denominator = math.lcm(*(Fraction(x).denominator for x in coefficients))
    integral = [int(Fraction(x)*denominator) for x in coefficients]
    assert math.gcd(*integral) == 1
    profile = {}
    for name,charge,p in sources:
        orders = {}
        for label,q,point_degree in points:
            order, quotient = factor_order(p,q)
            orders[label] = order
        profile[name] = {"charge":charge,"degree":p.degree(),"four_point_orders":orders,
                         "whole_angular_polynomial_sha256":digest(encode(p))}
    assert profile["Z390"]["four_point_orders"]["t0"] == 1
    assert set(profile["W178"]["four_point_orders"].values()) == {1}
    all_gcd = sources[0][2]
    for name,charge,p in sources[1:]:
        all_gcd = all_gcd.gcd(p)
    assert all_gcd != 0

    # Every common finite support is inside a, already from the complete old
    # ring.  Each new divisor coefficient is the true minimum of all sources.
    finite = {}
    for label,q,point_degree in points:
        actual = min(Fraction(profile[name]["four_point_orders"][label],charge)
                     for name,charge,p in sources)
        assert actual == min(Fraction(1,89),
                            Fraction(profile["Z390"]["four_point_orders"][label],195))
        finite[label] = actual
    infinity = max(Fraction(p.degree(),charge) for name,charge,p in sources)
    assert infinity == max(Fraction(29,89),Fraction(fZ.degree(),195))
    slope = infinity-sum(point_degree*finite[label] for label,q,point_degree in points)
    assert slope > Fraction(25,89)  # The old t0 slope strictly decreases.
    for name,charge,p in sources:
        assert p.degree() <= floor(charge*infinity)
        for label,q,point_degree in points:
            assert profile[name]["four_point_orders"][label] >= ceil(charge*finite[label])

    # Source membership returns use the whole angular polynomial, not samples.
    assert profile["Z390"]["four_point_orders"]["t0"] < ceil(Fraction(195,68))
    assert profile["Z390"]["four_point_orders"]["t0"] < ceil(Fraction(195,89))
    returned = {}
    for power,charge,alpha,degree_bound in ((4,263,68,85),(3,246,89,80)):
        p = fS**power*fZ
        expected_a_power = ceil(Fraction(charge,alpha))
        quotient = exact_quotient(p,a**expected_a_power)
        cap = floor(Fraction(11*charge,34)) if alpha == 68 else floor(Fraction(29*charge,89))
        assert cap == degree_bound and p.degree() <= cap
        assert a**expected_a_power*quotient == fS**power*fZ
        returned["old_B" if alpha == 68 else "five_source_Bplus"] = {
            "multiplier":"S34^{}".format(power),
            "target_charge":charge,
            "required_a_power":expected_a_power,
            "actual_angle_degree":p.degree(),
            "whole_angle_degree_bound":cap,
            "whole_return_identity_checked":True,
            "quotient_sha256":digest(encode(quotient))}
    sharp_returns = {}
    for label,alpha,top in (("old_B",68,Fraction(11,34)),
                            ("five_source_Bplus",89,Fraction(29,89))):
        for power in range(5):
            weight = 195+17*power
            p = fS**power*fZ
            required = ceil(Fraction(weight,alpha))
            if p.degree() > floor(top*weight):
                continue
            quotient,remainder = divmod(p,a**required)
            if remainder == 0:
                assert quotient*a**required == p
                sharp_returns[label] = {"smallest_S_power":power,"target_charge":weight,
                                        "degree":p.degree(),"a_power":required,
                                        "whole_quotient_sha256":digest(encode(quotient))}
                break
        assert label in sharp_returns

    # Same-ring Noether parameter candidates: all coefficients stay original.
    baseH = exact_quotient(fU,a)
    G = fZ
    common = Poly([1])
    for label,q,point_degree in points:
        power = profile["Z390"]["four_point_orders"][label]
        common *= q**power
    G = exact_quotient(fZ,common)
    assert a.gcd(G).degree() == 0
    assert (a*d).gcd(baseH).degree() == 0 and baseH.degree() == 18
    trials = []
    chosen = None
    for shear in range(G.degree()+1):
        Hc = baseH+shear*a**3*d**4/(7**4)
        assert Hc.degree() == 18 and (a*d).gcd(Hc).degree() == 0
        commonH = Hc.gcd(G)
        trials.append({"c":shear,"gcd_degree":commonH.degree()})
        if commonH.degree() == 0:
            chosen = shear
            break
    assert chosen is not None
    g,bezH,bezG = Hc.xgcd(G)
    assert g == 1 and bezH*Hc+bezG*G == 1
    assert Hc.gcd(fZ).degree() == 0
    assert fU+chosen*fS**4 == a*Hc
    u_angle = a*Hc
    actual_pair_finite = {
        label:min(Fraction(factor_order(u_angle,q)[0],68),
                  Fraction(profile["Z390"]["four_point_orders"][label],195))
        for label,q,point_degree in points}
    actual_pair_infinity = max(Fraction(u_angle.degree(),68),
                               Fraction(fZ.degree(),195))
    pair_pays_complete_divisor = (actual_pair_finite == finite and
                                 actual_pair_infinity == infinity)
    canceled_degree = sum(
        point_degree*min(195,68*profile["Z390"]["four_point_orders"][label])
        for label,q,point_degree in points)
    num_A_degree = 195*u_angle.degree()-canceled_degree
    den_A_degree = 68*fZ.degree()-canceled_degree
    degree_A = max(num_A_degree,den_A_degree)
    assert degree_A > 0
    # C=S^4/U_c=a^3*d^4/(7^4*H_c); this whole coprimality fixes its degree.
    num_C = a**3*d**4/(7**4)
    assert num_C.degree() == 16 and Hc.degree() == 18 and num_C.gcd(Hc) == 1
    finite_generator = None
    if pair_pays_complete_divisor:
        L = 68*195
        M = int(L*slope)
        assert Fraction(L)*slope == M and M == degree_A
        bad = []
        q_min = 0
        for r in range(L):
            qr = floor(r*infinity)-sum(
                point_degree*ceil(r*finite[label]) for label,q,point_degree in points)
            q_min = min(q_min,qr)
            if qr <= -2:
                bad.append(r)
        assert q_min >= -4 and M >= 3
        bound = max(2*L-1, 2*L+max(bad)) if bad else 2*L-1
        finite_generator = {"Veronese_weight":L,"complete_P1_degree":M,
                            "all_residue_classes_checked":L,
                            "minimum_residue_degree":q_min,
                            "residues_requiring_n2":bad,
                            "sufficient_generator_weight_bound":bound}
    # Fixed bad-prime data, printed only by value hashes/bit lengths.
    resultants = {
        "a_GZ":rational_receipt(a.resultant(G)),
        "Hc_GZ":rational_receipt(Hc.resultant(G)),
        "ad_Hc":rational_receipt((a*d).resultant(Hc)),
        "leading_GZ":rational_receipt(G.leading_coefficient())}
    whole_certificate = {"Z":encode(fZ),"W":encode(fW),"GZ":encode(G),
                         "Hc":encode(Hc),"bezout_Hc":encode(bezH),"bezout_GZ":encode(bezG)}
    return {
        "status":"PASS",
        "same_job_E65_and_E89_coefficients_consumed":True,
        "new_source_denominator":str(denominator),
        "new_source_integral_content":1,
        "all_six_source_profiles":profile,
        "all_six_common_gcd_degree":all_gcd.degree(),
        "complete_divisor_profile":{
            "infinity":str(infinity),
            "finite":{label:str(x) for label,x in finite.items()},
            "Hilbert_linear_slope":str(slope),
            "Hilbert_cumulative_slope":str(slope/2),
            "strict_gain_over_five_source_slope":str(slope-Fraction(25,89)),
            "all_six_full_source_memberships_checked":True},
        "Z390_in_original_B195":False,
        "Z390_in_five_source_Bplus195":False,
        "whole_old_lattice_returns":returned,
        "sharp_S_power_returns":sharp_returns,
        "same_ring_shear":{"parameter":"U136+c*S34^4","c":chosen,"all_trials":trials,
                           "full_Bezout_return":True,
                           "whole_source_identity_return":True},
        "actual_rational_maps":{
            "A":"U_c^195/Z390^68",
            "reduced_numerator_degree":num_A_degree,
            "reduced_denominator_degree":den_A_degree,
            "A_degree":degree_A,
            "C":"S34^4/U_c",
            "C_degree":18,
            "gcd_of_map_degrees":math.gcd(degree_A,18),
            "infinity_valuation_pair":[den_A_degree-num_A_degree,2]},
        "actual_parameter_pair_pays_complete_divisor":pair_pays_complete_divisor,
        "full_residue_weight_generator_bound":finite_generator,
        "fixed_bad_prime_resultants":resultants,
        "whole_Bezout_and_source_certificate_sha256":digest(whole_certificate),
        "full_field_primitivity_claimed_by_this_finite_reader":False,
        "conductor_claimed_by_this_finite_reader":False,
        "products_assigned_new_central_zero":False,
        "output_coefficient_tables":False,
        "output_files":False}
