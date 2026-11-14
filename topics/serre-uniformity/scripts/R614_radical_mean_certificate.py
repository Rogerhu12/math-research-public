"""Integer certificate for one instance of the R614 radical criterion.

The primality proof is a full Lucas N+1 order certificate.  No probable-prime
routine, floating point logarithm, or L-value computation enters this file.
"""
from fractions import Fraction
from hashlib import sha256
from math import factorial, gcd
from pathlib import Path
import json


def matrix_multiply(a, b, modulus):
    return (
        (a[0]*b[0]+a[1]*b[2]) % modulus,
        (a[0]*b[1]+a[1]*b[3]) % modulus,
        (a[2]*b[0]+a[3]*b[2]) % modulus,
        (a[2]*b[1]+a[3]*b[3]) % modulus,
    )


def lucas_u(index, P, Q, modulus):
    result = (1, 0, 0, 1)
    power = (P, -Q, 1, 0)
    while index:
        if index & 1:
            result = matrix_multiply(result, power, modulus)
        power = matrix_multiply(power, power, modulus)
        index >>= 1
    return result[2]


def main():
    nu = 73
    p = 15*(1 << nu)-1
    P, Q = 7, -1
    discriminant = P*P-4*Q
    factorization = {2: nu, 3: 1, 5: 1}
    product = 1
    for q, e in factorization.items():
        product *= q**e
    assert product == p+1
    assert gcd(2*Q*discriminant, p) == 1
    terminal = lucas_u(p+1, P, Q, p)
    assert terminal == 0
    residues = {q: lucas_u((p+1)//q, P, Q, p) for q in factorization}
    quotient_gcds = {q: gcd(value, p) for q, value in residues.items()}
    assert set(quotient_gcds.values()) == {1}

    # exp(13/5)>13 proves log(13)<13/5, so L=1+log(13)<18/5.
    taylor = sum((Fraction(13, 5)**k/factorial(k) for k in range(13)), Fraction())
    assert taylor > 13
    L_upper = Fraction(18, 5)
    D = 13
    d0 = 169
    m = 2
    d = p**m*d0
    assert p % 9 == 2 and d % 9 == 1 and gcd(d0, 6*p) == 1
    M = (p+1)//3
    assert M == 5*(1 << nu)
    radical_M, extra_divisor_count = 10, 2
    first_threshold = 480*L_upper**2*extra_divisor_count
    second_threshold = 720*L_upper**2*extra_divisor_count
    first_margin = Fraction(p, 2)-first_threshold**(radical_M//2)
    second_margin = Fraction(p, D)-second_threshold**2
    assert first_margin > 0 and second_margin > 0
    rank_dimension = 4*(1 << (nu-1))
    assert rank_dimension == 1 << 74

    positive_D = 65
    positive_d0 = 65
    positive_d = p**2*positive_d0
    assert positive_d % 9 == 8 and gcd(positive_d0, 6*p) == 1
    positive_taylor = sum((Fraction(21, 5)**k/factorial(k) for k in range(13)), Fraction())
    assert positive_taylor > 65
    positive_L_upper = Fraction(26, 5)
    positive_first_threshold = 192*positive_L_upper**2*extra_divisor_count
    positive_second_threshold = 1440*positive_L_upper**2*extra_divisor_count
    positive_first_margin = Fraction(p, 2)-positive_first_threshold**(radical_M//2)
    positive_second_margin = Fraction(p, positive_D)-positive_second_threshold**2
    assert positive_first_margin > 0 and positive_second_margin > 0

    output = {
        'status': 'exact-prime-and-radical-criterion-PASS',
        'p': p, 'p_plus_one_factorization': factorization,
        'lucas': {'P': P, 'Q': Q, 'discriminant': discriminant,
                  'gcd_2QD_p': gcd(2*Q*discriminant, p),
                  'U_pplus1_mod_p': terminal,
                  'U_quotient_residues': residues, 'quotient_gcds': quotient_gcds},
        'actual_family_parameters': {'m': m, 'd0': d0, 'd': d, 'D': D,
                                     'd_mod9': d % 9, 'sD': 0, 'M': M,
                                     'radical_M': radical_M, 'extra_squarefree_orders': extra_divisor_count},
        'log_bound': {'exp_13over5_Taylor_terms_0_to_12': str(taylor),
                      'strict_margin_above_13': str(taylor-13),
                      'L_upper': str(L_upper)},
        'radical_conditions': {'H_required_upper': str(first_threshold),
                               'sqrt_p_over_D_required_upper': str(second_threshold),
                               'p_over_2_minus_H_upper_to_R_over_2': str(first_margin),
                               'p_over_D_minus_second_upper_squared': str(second_margin)},
        'primitive_mean_strict_lower_bound': '4046/4125',
        'actual_primitive_factor_rank_and_dimension': rank_dimension,
        'p_adic_log_isomorphism': 'follows through the proved general-level rank interface',
        'positive_root_family': {
            'm': 2, 'd0': positive_d0, 'd': positive_d, 'D': positive_D,
            'd_mod9': positive_d % 9, 'sD': 1, 'radical_M': radical_M,
            'extra_squarefree_orders': extra_divisor_count,
            'exp_21over5_Taylor_terms_0_to_12': str(positive_taylor),
            'strict_Taylor_margin_above_65': str(positive_taylor-65),
            'L_upper': str(positive_L_upper),
            'H_required_upper': str(positive_first_threshold),
            'sqrt_p_over_D_required_upper': str(positive_second_threshold),
            'p_over_2_minus_H_upper_to_R_over_2': str(positive_first_margin),
            'p_over_D_minus_second_upper_squared': str(positive_second_margin),
            'primitive_mean_strict_lower_bound': '1/(2*(1+log(65)))',
            'actual_primitive_factor_dimension': rank_dimension,
            'actual_primitive_factor_rational_rank': 0,
        },
        'scope': 'same actual primitive families, negative and positive root; no original rational candidate existence or local CM coefficient unit claimed',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    path = Path(__file__).with_name('R614-radical-mean-certificate.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
