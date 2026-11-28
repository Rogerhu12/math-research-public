"""Full-function factorization of the off-conjugacy raw phase derivative.

The spectral callbacks operate on the whole original circle (or enclose
the full tails). div_rotation solves D_R on the nonmean input; div_weighted
solves lambda I-R on its nonmean input. Neither acts on a zero mode.
"""
from fractions import Fraction


def factor_weighted_phase(*, multiplier, column, log, exp, mean,
                         rotate, div_rotation, div_weighted, excludes_zero):
    log_m = log(multiplier)
    log_lambda = mean(log_m)
    u = div_rotation(log_lambda - log_m)
    weight = exp(u)
    lam = exp(log_lambda)
    inverse_shifted_weight = exp(-rotate(u))
    weight_mean = mean(weight)

    def decompose(value):
        scaled = inverse_shifted_weight * value
        average = mean(scaled)
        nonmean = div_weighted(lam, scaled - average)
        zero_mode = -mean(weight * nonmean) / weight_mean
        compatibility = average - (lam - 1) * zero_mode
        return compatibility, nonmean + zero_mode

    column_mean, column_primitive = decompose(column)
    if not excludes_zero(column_mean):
        raise ValueError("complete weighted physical phase pivot contains zero")

    def solve(forcing):
        forcing_mean, forcing_primitive = decompose(forcing)
        metric = forcing_mean / column_mean
        return weight * (forcing_primitive - metric * column_primitive), metric

    return solve


def solve_weighted_phase(*, forcing, **coefficients):
    return factor_weighted_phase(**coefficients)(forcing)


def solve_mixed_jet(solve, value, first_i, first_j, mixed):
    """Each data jet is (forcing, multiplier, physical parameter column).

    value is the complete base (a,k) for these data. The returned directions
    are in the mean-zero gauge at this same base. Functions and scalar
    products use the supplied whole-function algebra.
    """
    a, k = value
    f_i, m_i, b_i = first_i
    f_j, m_j, b_j = first_j
    f_ij, m_ij, b_ij = mixed
    a_i, k_i = solve(f_i - m_i * a - b_i * k)
    a_j, k_j = solve(f_j - m_j * a - b_j * k)
    rhs_ij = (f_ij - m_ij * a - b_ij * k
              - m_i * a_j - m_j * a_i - b_i * k_j - b_j * k_i)
    return (a_i, k_i), (a_j, k_j), solve(rhs_ij)


def verify_neighbourhood():
    small = Fraction(1, 2**19)
    u_norm = 17 * small
    d = u_norm / 2
    distortion = (d / (1 - d)
                  + 18 * u_norm * small / ((1 - 3*d) * (1 - small/2)))
    assert 297 * distortion < Fraction(1, 120)
    assert 120 * (1 + distortion) < 121
    return distortion


if __name__ == "__main__":
    print(verify_neighbourhood())
