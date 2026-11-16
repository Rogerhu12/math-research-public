#!/usr/bin/env sage -python
"""R873: rigorous original CM Petersson norms and Hom degree bounds.

Run only in the public research Actions workflow:
  sage -python check-r873-original-cm-petersson-degree.py \
    --M 1024 --bits 384 --unit-window 6 --top 6

No prime scan, external data file, or inferred integral parametrization.
All algebraic coefficients are exact; transcendental bounds use Arb balls.
"""
import os
import time
from pathlib import Path
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Mathematical execution is restricted to the public repository Actions.")
STARTED = time.monotonic()
import argparse
import hashlib
import json
import math
from sage.all import QQ, ZZ, CyclotomicField, RealBallField, ComplexBallField
from sage.all import matrix, vector, identity_matrix
from sage.env import SAGE_VERSION


def fp2_mul(x, y):
    a, b = x
    c, d = y
    return ((a*c-b*d) % 17, (a*d+b*c-b*d) % 17)


def unit_orbit(a, b):
    return [(a, b), (-a, -b), (-b, a-b), (b, b-a),
            (b-a, -a), (a-b, a)]


def exact_coefficients(M):
    K = CyclotomicField(9, 'z')
    z = K.gen()
    om = z**3
    alpha = -1 + 2*om
    c = -1 - 19*om
    assert (alpha*z**2)**3 == c
    powers = {}
    v = (1, 0)
    for j in range(288):
        assert v not in powers
        powers[v] = j
        v = fp2_mul(v, (16, 2))
    assert v == (1, 0) and len(powers) == 288
    # a_m are the ORIGINAL weight-two coefficients, including the prime 2.
    # A_m are coefficients of beta^2, including the restored prime 3.
    a_coeff = [K(0) for _ in range(M+1)]
    A_coeff = [K(0) for _ in range(M+1)]
    lim = math.isqrt((4*M)//3) + 2
    ideal_count = 0
    for aa in range(-lim, lim+1):
        for bb in range(-lim, lim+1):
            m = aa*aa-aa*bb+bb*bb
            if m < 1 or m > M:
                continue
            if (aa, bb) != min(unit_orbit(aa, bb)):
                continue
            if aa % 17 == 0 and bb % 17 == 0:
                continue
            rr = powers[(aa % 17, bb % 17)] % 9
            u = aa + bb*om
            square_value = u*u*z**(4*rr)
            # Check the principal-ideal convention, not just a norm label.
            for ua, ub in unit_orbit(aa, bb):
                ur = powers[(ua % 17, ub % 17)] % 9
                assert (ua+ub*om)**2*z**(4*ur) == square_value
            A_coeff[m] += square_value
            ideal_count += 1
            if m % 3:
                eps = 1 if (aa+bb) % 3 == 1 else -1
                value = eps*u*z**(2*rr)
                for ua, ub in unit_orbit(aa, bb):
                    ur = powers[(ua % 17, ub % 17)] % 9
                    ue = 1 if (ua+ub) % 3 == 1 else -1
                    assert ue*(ua+ub*om)*z**(2*ur) == value
                a_coeff[m] += value
    conjugation = K.hom([z**(-1)], K)
    assert a_coeff[1] == 1 and A_coeff[1] == 1
    if M >= 4:
        assert a_coeff[3] == 0 and a_coeff[4] == -2
        assert A_coeff[3] == -3 and A_coeff[4] == 4
    for m in range(1, M+1):
        assert conjugation(a_coeff[m]) == a_coeff[m]
        assert conjugation(A_coeff[m]) == A_coeff[m]
        if 3*m <= M:
            assert A_coeff[3*m] == -3*A_coeff[m]
        if 17*m <= M:
            assert a_coeff[17*m] == 0
        if 289*m <= M:
            assert A_coeff[289*m] == 0
    rows = []
    for m in range(1, M+1):
        ap = list(a_coeff[m].polynomial())
        Ap = list(A_coeff[m].polynomial())
        ap += [QQ(0)]*(6-len(ap))
        Ap += [QQ(0)]*(6-len(Ap))
        rows.append([m, [str(x) for x in ap], [str(x) for x in Ap]])
    digest = hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
    return K, a_coeff, A_coeff, ideal_count, digest


def main():
    pa = argparse.ArgumentParser()
    pa.add_argument('--M', type=int, default=1024)
    pa.add_argument('--bits', type=int, default=384)
    pa.add_argument('--unit-window', type=int, default=6)
    pa.add_argument('--top', type=int, default=6)
    args = pa.parse_args()
    assert args.M >= 17 and args.bits >= 192
    assert 0 <= args.unit_window <= 50 and 1 <= args.top <= 20
    R = RealBallField(args.bits)
    C = ComplexBallField(args.bits)
    K, ac, Ac, ideals, coeff_hash = exact_coefficients(args.M)
    pi = R.pi()
    ii = C(0, 1)
    z0 = (2*pi*ii/9).exp()
    om = z0**3
    alpha = -1 + 2*om
    c = -1 - 19*om
    # The three embeddings fix omega.  Their b-values are b, omega*b,
    # omega^2*b, in precisely the R862 order g_10, g_16, g_4.
    embed_exponents = [1, 7, 4]
    roots = [z0**e for e in embed_exponents]

    def evaluate(x, zz):
        ans = C(0)
        for u in reversed(list(x.polynomial())):
            ans = ans*zz + C(u)
        return ans

    def is_zero(x):
        return C(x).contains_zero()

    def real(x):
        x = C(x)
        assert x.imag().contains_zero()
        return x.real()

    def pow_positive(x, num, den):
        assert x > 0
        return (x.log()*R(num)/R(den)).exp()

    def ball(x):
        return str(x)

    def abs_square(x):
        return real(x*x.conjugate())

    a = (R(17).log()/3).exp()
    v = -R(122465)-R(47628)*a-(R(314892)/17)*a*a
    assert v < 0
    assert is_zero(v**3+367395*v**2+147*v+R(1)/17)

    def ell(t):
        return ((21905009-23122022*om)
                +(112353990182+54575060764*om)*t
                +(305813+148546*om)*t*t)/25505280

    ell0 = ell(C(v))
    tv = alpha**3*v/ell0**3
    ell1 = ell(tv)
    ttv = alpha**3*tv/ell1**3
    ell2 = ell(ttv)
    tttv = alpha**3*ttv/ell2**3
    assert is_zero(tttv-v)
    assert is_zero(ell0*ell1*ell2-c)
    u1, u2 = ell2, c/ell0
    bvalues = [alpha*z0**(2+3*j) for j in range(3)]
    G = [1+u1/bb+u2/(bb*bb) for bb in bvalues]
    assert is_zero(sum(G)-3)
    for gg in G:
        assert gg.imag().contains_zero()
        assert abs_square(gg) > 0

    def H_coefficient(m):
        return sum((G[j]/3)*evaluate(ac[m], roots[j]) for j in range(3))

    assert is_zero(H_coefficient(1)-1)
    assert is_zero(H_coefficient(4)+2)
    h7 = (1378521263+57978976034*v+157811*v*v)/531360
    assert is_zero(H_coefficient(7)-h7)

    Q = R(867).sqrt()/(2*pi)
    rr = (-1/Q).exp()
    M = args.M
    tail = rr**(M+1)*(1/(1-rr)+(2/Q)*((M+1)/(1-rr)+rr/(1-rr)**2))
    assert tail > 0
    Lvalues = []
    partials = []
    for j in range(3):
        total = R(0)
        for m in range(1, M+1):
            am = real(evaluate(Ac[m], roots[j]))
            total += am*(-R(m)/Q).exp()*(R(1)/(m*m)+R(2)/(Q*m))
        val = total.add_error(tail)
        assert val > 0
        partials.append(total)
        Lvalues.append(val)

    area0 = R(QQ(1)/3).gamma()**2 * R(QQ(1)/6).gamma()**2/(4*pi*R(3).sqrt())
    dabs2 = pow_positive(-v/2, 2, 3)
    areav = area0/dabs2
    Nj = [lv/(24*R(3).sqrt()*pi*pi) for lv in Lvalues]
    weights = [R(136)*abs_square(G[j])*Lvalues[j]/(R(3).sqrt()*areav)
               for j in range(3)]
    # Independently retain the original source index 3672 and the factor 1/3.
    for j in range(3):
        check = 8*pi*pi*3672*abs_square(G[j]/3)*Nj[j]/areav
        assert (check-weights[j]).contains_zero()
        assert weights[j] > 0
    degree0 = sum(weights)
    geom_mean = pow_positive(weights[0]*weights[1]*weights[2], 1, 3)
    universal = 3*geom_mean

    eps1 = [real(z0**(2+3*j)+z0**(-2-3*j)) for j in range(3)]
    eps2 = [ee*ee-2 for ee in eps1]
    for ee in eps1+eps2:
        assert not ee.contains_zero()
    assert is_zero(eps1[0]*eps1[1]*eps1[2]+1)
    assert is_zero(eps2[0]*eps2[1]*eps2[2]+1)

    M1 = matrix(ZZ, [[0, 2, -1], [1, 0, 1], [0, 1, 0]])
    M2 = matrix(ZZ, [[0, -1, 2], [0, 1, -1], [1, 0, -1]])
    eye = identity_matrix(ZZ, 3)
    assert M1*(eye-M2) == eye
    assert M2*(eye+M1+M2) == eye
    unit_rows = []
    for ue in range(-args.unit_window, args.unit_window+1):
        for ve in range(-args.unit_window, args.unit_window+1):
            deg = sum(weights[j]*(eps1[j]**(2*ue))*(eps2[j]**(2*ve))
                      for j in range(3))
            assert deg > 0
            coeff = (M1**ue)*(M2**ve)*vector(ZZ, [1, 0, 0])
            e0, e1, e2 = [ZZ(x) for x in coeff]
            HU1 = u1/alpha+(alpha/c)*u2
            HU2 = (alpha*alpha/c)*u1+u2/(alpha*alpha)
            leading = C(e0)+e1*HU1+e2*HU2
            assert leading.imag().contains_zero()
            assert not leading.contains_zero()
            unit_rows.append((float(deg.mid()), {
                "unit_exponents": [ue, ve],
                "coefficients_in_1_eps1_eps2": [str(e0), str(e1), str(e2)],
                "original_first_coefficient": ball(real(leading)),
                "quasidegree": ball(deg),
                "necessary_n17_degree_lower": ball(289*deg)
            }))
    unit_rows.sort(key=lambda x: (x[0], x[1]["unit_exponents"]))

    # Synchronous target change: it never changes the true map degree.
    e = 18-7*a
    einv = 324+126*a+49*a*a
    assert is_zero(e*einv-1)
    assert is_zero(-a*v-einv*einv)
    vs = e**3*v
    assert is_zero(vs-(7-R(18)*a*a/17))
    assert is_zero(vs**3-21*vs**2+147*vs+R(1)/17)
    areasmall = areav/(e*e)
    assert is_zero((8*pi*pi*3672/areasmall)/(e*e)
                   -(8*pi*pi*3672/areav))

    bounds = {}
    for k in [2, 4, 6, 8]:
        cap = 102*k
        bounds[str(k)] = {
            "degree_cap": cap,
            "all_units_n_ge_1_excluded": bool(universal > cap),
            "all_units_true_integer_n_excluded": bool(289*universal > cap),
            "all_three_isogeny_units_n_ge_1_excluded": bool(geom_mean > cap),
            "all_three_isogeny_true_integer_n_excluded": bool(289*geom_mean > cap)
        }

    output = {
        "status": "PASS",
        "sage_version": SAGE_VERSION,
        "parameters": vars(args),
        "original_source": {
            "curve": "X0(2601)",
            "index": 3672,
            "ordered_forms": ["g10", "g16", "g4"],
            "squared_character_conductor": "(17)",
            "weight_three_level": 867,
            "root_number": 1,
            "finite_field_generator": [-1, 2],
            "finite_field_generator_order": 288,
            "cyclotomic9_embedding_exponents": embed_exponents,
            "ideal_count": ideals,
            "full_exact_coefficient_sha256": coeff_hash,
            "a4": "-2",
            "A3": "-3",
            "A4": "4",
            "h0_q7": ball(real(H_coefficient(7)))
        },
        "AFE": {
            "Q": ball(Q),
            "uniform_absolute_tail": ball(tail),
            "partial_sums": [ball(x) for x in partials],
            "L_beta_squared_at_2": [ball(x) for x in Lvalues],
            "normalized_petersson_norms": [ball(x) for x in Nj]
        },
        "geometry": {
            "v_real_embedding": ball(v),
            "area_E0_dx_over_2y": ball(area0),
            "d_absolute_square": ball(dabs2),
            "area_Cv": ball(areav),
            "G_coefficients": [ball(real(x)) for x in G],
            "positive_degree_weights": [ball(x) for x in weights],
            "Xi0_quasidegree": ball(degree0),
            "geometric_mean_g": ball(geom_mean),
            "global_unit_lower_3g": ball(universal),
            "true_integer_global_unit_lower_17sq_3g": ball(289*universal),
            "true_integer_three_isogeny_lower_17sq_g": ball(289*geom_mean),
            "small_model_unit_e": ball(e),
            "small_model_parameter": ball(vs),
            "small_model_area": ball(areasmall)
        },
        "rigorous_low_weight_exclusions": bounds,
        "finite_unit_window_best": [row for _, row in unit_rows[:args.top]],
        "scope": {
            "degrees_are_rounded_to_integers": False,
            "Xi0_integral_is_assumed": False,
            "n17_is_proved_sufficient": False,
            "unit_window_is_global_minimum_certificate": False,
            "global_lower_bound_uses_all_units": True,
            "original_shadow_computed": False
        }
    }
    output["run"] = {
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
            "topics/rank2-sha-infinitely-many-p/README.md":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED
    }
    payload = json.dumps(output, sort_keys=True, separators=(',', ':'))
    print("RANK2_CM_NORM_RESULT "+payload,flush=True)
    print("RANK2_CM_NORM_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == '__main__':
    main()
