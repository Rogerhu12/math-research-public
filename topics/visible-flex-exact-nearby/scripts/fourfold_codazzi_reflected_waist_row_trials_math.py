"""Pure complete reflected waist-row trials from the saved exact G definition.

R149 RW.1--26: no IO and no numerical imports.  A public owner supplies the
pinned flint API and complete exact rational H_fin/K48 coefficient lists.
The exact trial is the finite sampled DFT, never the midpoint of an enclosure.
"""
from __future__ import annotations
from fractions import Fraction

PARAMETERS = {
    "arithmetic_bits": 320,
    "row_modes": 96,
    "grid_points": 4096,
    "trial_fourier_cutoff": 1024,
    "fixed_original_waist_normalizer_cutoff": 268435456,
    "physical_frequency_factor": 4,
    "original_conjugacy_strip": "1/128",
    "original_selected_run": "43588332723/1",
    "original_selected_loss": "1/250",
    "exact_H_constant_term": "0",
    "exact_K48_constant_term": "0",
    "exact_H_nonmean_degree": 24,
    "exact_real_basis": "sqrt(2)*cos(4*j*(x-a/2)); a=2*H(0); j=1..96",
    "compound_lift": "(G(phi)-G(-phi))/2; G=K48 composed with H_fin",
    "exact_trial": "truncated exact L-point DFT of sqrt(2)*cos(4*j*G_odd)",
    "arbitrary_midpoint_trial_selection": False,
    "incoming_row_full_old_angle_mean_retained": True,
    "physical_primitive_row_has_two_half_nonmean_components": True,
    "independent_density_mean_rows": 2,
    "target_B_inverse_or_Theta_rows_included": False,
    "old_KAM_or_old_receiver_scientific_calls": 0,
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exact(api, value):
    q = Fraction(value)
    return api.arb(q.numerator)/api.arb(q.denominator)


def nonnegative_upper(value, label):
    require(value.is_finite() and value.lower() >= 0,
            "finite nonnegative complete upper: "+label)
    return value.upper()


def magnitude_upper(value):
    require(value.is_finite(), "complete finite real coefficient enclosure")
    return abs(value).upper()


def finite_periodic_value(api, x, sines, cosines, constant_term):
    """The whole original rational trigonometric polynomial at one real ball."""
    require(len(sines) == len(cosines) and len(sines) > 0,
            "complete matching sine/cosine lists")
    argument = 4*x
    unit = api.acb(argument.cos(), argument.sin())
    power = unit
    result = exact(api, constant_term)
    for a, b in zip(sines, cosines):
        result = result+exact(api, a)*power.imag+exact(api, b)*power.real
        power = power*unit
    require(result.is_finite(), "whole finite periodic evaluation")
    return result


def complete_compound_periodic_value(api, x, Hs, Hc, Ks, Kc, H_constant, K_constant):
    """G(x)-x = h(x)+k(x+h(x)); no Fourier truncation of the composition."""
    h = finite_periodic_value(api, x, Hs, Hc, H_constant)
    return h+finite_periodic_value(api, x+h, Ks, Kc, K_constant)


def complete_odd_compound_lift(api, x, Hs, Hc, Ks, Kc, H_constant, K_constant):
    plus = complete_compound_periodic_value(api, x, Hs, Hc, Ks, Kc, H_constant, K_constant)
    minus = complete_compound_periodic_value(api, -x, Hs, Hc, Ks, Kc, H_constant, K_constant)
    result = x+(plus-minus)/2
    require(result.is_finite(), "whole signed odd compound lift")
    return result


def _bit_reverse_indices(length):
    require(length >= 2 and length & (length-1) == 0, "radix-two complete grid")
    bits = length.bit_length()-1
    result = []
    for index in range(length):
        source, reversed_index = index, 0
        for bit in range(bits):
            reversed_index = (reversed_index << 1) | (source & 1)
            source >>= 1
        result.append(reversed_index)
    return result


def fft_tables(api, length):
    """Directed roots of unity for the exact negative-sign unnormalized DFT."""
    permutation = _bit_reverse_indices(length)
    stages = []
    width = 2
    while width <= length:
        angle = 2*api.arb.pi()/width
        step = api.acb(angle.cos(), -angle.sin())
        power = api.acb(1)
        roots = []
        for k in range(width//2):
            roots.append(power)
            power = power*step
        stages.append((width, roots))
        width *= 2
    return permutation, stages


def complete_directed_dft(api, real_samples, tables):
    length = len(real_samples)
    permutation, stages = tables
    require(len(permutation) == length and all(value.is_finite() for value in real_samples),
            "whole exact finite real sample grid")
    work = [api.acb(real_samples[index]) for index in permutation]
    for width, roots in stages:
        require(len(roots) == width//2 and length % width == 0,
                "all complete FFT butterfly factors")
        half = width//2
        for start in range(0, length, width):
            for k in range(half):
                left = work[start+k]
                right = roots[k]*work[start+k+half]
                work[start+k] = left+right
                work[start+k+half] = left-right
    require(all(value.is_finite() for value in work), "all DFT outputs finite")
    return work


class ReflectedRowFactory:
    """One new whole compound grid; all 96 exact row trials in fixed order."""

    def __init__(self, api, Hs, Hc, Ks, Kc, *, H_constant, K_constant):
        self.api = api
        self.length = PARAMETERS["grid_points"]
        self.cutoff = PARAMETERS["trial_fourier_cutoff"]
        self.rows = PARAMETERS["row_modes"]
        require(2*self.cutoff < self.length
                and self.cutoff < PARAMETERS["fixed_original_waist_normalizer_cutoff"],
                "complete alias separation and exact old normalizer finite-complement domain")
        self.Hs, self.Hc, self.Ks, self.Kc = [
            tuple(Fraction(value) for value in values) for values in (Hs, Hc, Ks, Kc)]
        self.H_constant, self.K_constant = Fraction(H_constant), Fraction(K_constant)
        require(len(self.Hs) == len(self.Hc) == PARAMETERS["exact_H_nonmean_degree"]
                and len(self.Ks) == len(self.Kc) == 48
                and self.H_constant == Fraction(PARAMETERS["exact_H_constant_term"])
                and self.K_constant == Fraction(PARAMETERS["exact_K48_constant_term"]),
                "all original H24/K48 coefficients and their explicitly admitted zero translations")
        self.tables = fft_tables(api, self.length)
        self.base_cosines = None
        self.next_row = 1

    def materialize_whole_compound_grid(self):
        """New required carrier, no old ray integration or KAM iteration."""
        require(self.base_cosines is None, "one whole compound grid per new row target")
        api, length = self.api, self.length
        values = [None]*length
        values[0], values[length//2] = api.arb(1), api.arb(-1)
        for index in range(1, length//2):
            angle = api.arb.pi()*index/(2*length)
            lift = complete_odd_compound_lift(
                api, angle, self.Hs, self.Hc, self.Ks, self.Kc,
                self.H_constant, self.K_constant)
            value = (4*lift).cos()
            require(value.is_finite(), "complete compound cosine sample")
            # Exact evenness of cos(4*G_odd), not a fitted numerical symmetry.
            values[index] = value
            values[length-index] = value
        require(all(value is not None and value.is_finite() for value in values),
                "every declared compound sample, including both fixed endpoints")
        self.base_cosines = values
        self.previous = [api.arb(1) for index in range(length)]
        self.current = list(values)
        return values

    def next_complete_row(self):
        """All 1025 real coefficients of the next exact DFT polynomial."""
        require(self.base_cosines is not None and 1 <= self.next_row <= self.rows,
                "whole grid and one still-uncomputed declared row")
        api, j = self.api, self.next_row
        root_two = api.arb(2).sqrt()
        samples = [root_two*value for value in self.current]
        transform = complete_directed_dft(api, samples, self.tables)
        coefficients = []
        for k in range(self.cutoff+1):
            value = transform[k]/self.length
            require(value.is_finite() and value.imag.contains(api.arb(0)),
                    "the full even real DFT coefficient encloses its exact zero imaginary part")
            coefficients.append(value.real)
        require(len(coefficients) == self.cutoff+1, "no retained trial Fourier mode omitted")
        if j < self.rows:
            following = [2*base*value-old for base, value, old in
                         zip(self.base_cosines, self.current, self.previous)]
            require(all(value.is_finite() for value in following),
                    "complete exact Chebyshev recurrence")
            self.previous, self.current = self.current, following
        self.next_row += 1
        return j, coefficients


def complete_trial_l2_upper(api, coefficients):
    """Parseval for c0+2 sum_{k=1}^N ck cos(4k phi), with the full mean."""
    require(len(coefficients) == PARAMETERS["trial_fourier_cutoff"]+1,
            "whole finite row coefficient carrier")
    value = magnitude_upper(coefficients[0])**2
    for coefficient in coefficients[1:]:
        value = value+2*magnitude_upper(coefficient)**2
    return value.upper().sqrt().upper()


def compound_row_error_upper(api, j, saved_H_minus_G_upper, saved_G_periodic_upper):
    """RW.18 complete bound; both input records must be old whole saved uppers."""
    require(type(j) is int and 1 <= j <= PARAMETERS["row_modes"], "one of the exact 96 rows")
    eh = nonnegative_upper(saved_H_minus_G_upper, "same selected H-G")
    g0 = nonnegative_upper(saved_G_periodic_upper, "whole exact G periodic norm")
    sigma = exact(api, PARAMETERS["original_conjugacy_strip"])
    root_two = api.arb(2).sqrt().upper()
    N, L = PARAMETERS["trial_fourier_cutoff"], PARAMETERS["grid_points"]
    weighted_bound = (root_two*(4*j*(sigma+g0)).exp()).upper()
    truncation = (-4*sigma*(N+1)).exp().upper()
    alias = (-4*sigma*(L-N)).exp().upper()
    value = 4*root_two*j*eh+weighted_bound*(truncation+alias)
    require(value.is_finite() and value.lower() >= 0, "complete new compound row error")
    return value.upper()


def incoming_row_error_upper(api, saved_compound_error_upper, saved_fixed_Js_inverse_upper):
    error = nonnegative_upper(saved_compound_error_upper, "formally saved compound row error")
    kw = nonnegative_upper(saved_fixed_Js_inverse_upper, "same actual fixed Js inverse")
    require(kw >= 1, "the original same-space full normalizer inverse upper")
    return (kw*error).upper()


def physical_primitive_row_error_upper(api, saved_compound_error_upper):
    error = nonnegative_upper(saved_compound_error_upper, "formally saved compound row error")
    # Multiply an upper for 1/sqrt(2), never divide by an upper for sqrt(2).
    return (exact(api, "1/2").sqrt().upper()*error).upper()


def incoming_trial_density(api, coefficients):
    """SC density format, including the possibly nonzero old-angle row mean."""
    require(len(coefficients) == PARAMETERS["trial_fourier_cutoff"]+1,
            "complete exact DFT row before receiver injection")
    zero = api.arb(0)
    primitive = {}
    for k, value in enumerate(coefficients[1:], 1):
        require(value.is_finite(), "complete signed row coefficient")
        primitive[k] = (value, zero)
        primitive[-k] = (value, zero)
    return {"primitive_pair": (primitive, {}),
            "both_physical_means": (coefficients[0], zero)}


def physical_primitive_trial_density(api, coefficients):
    """RW.22: both half nonmean components; density means remain separate rows."""
    incoming = incoming_trial_density(api, coefficients)
    half = {k: (value[0]/2, value[1]/2)
            for k, value in incoming["primitive_pair"][0].items()}
    zero = api.arb(0)
    return {"primitive_pair": (dict(half), dict(half)),
            "both_physical_means": (zero, zero)}


def independent_density_mean_row(api, component):
    require(component in (0, 1), "one of the two full independent density mean coordinates")
    zero, one = api.arb(0), api.arb(1)
    means = (one, zero) if component == 0 else (zero, one)
    return {"primitive_pair": ({}, {}), "both_physical_means": means}


def finite_trial_below_original_normalizer(density):
    """Exact support qualification for RW.26; does not bound the true PDE column."""
    cutoff = PARAMETERS["fixed_original_waist_normalizer_cutoff"]
    require(len(density["primitive_pair"]) == len(density["both_physical_means"]) == 2,
            "complete primitive pair and both density means")
    return all(type(k) is int and 0 < abs(k) < cutoff
               for component in density["primitive_pair"] for k in component)
