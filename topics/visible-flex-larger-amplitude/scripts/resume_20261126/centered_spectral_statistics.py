#!/usr/bin/env python3
"""R687 positive-polynomial evaluation of Phi minus its fixed constant.

The only change is evaluation of the scalar loss/statistics. The original
true gradient, R664 residual Hessian, observation weights, variable space,
and damping units are unchanged. Public Actions are the scientific runtime.
All displayed values are ordinary binary64, never outward certificates.
No arrays or physical fields are created or evaluated by importing this file.
"""
from functools import lru_cache
from pathlib import Path
import hashlib
import math
import os

import numpy as np


@lru_cache(maxsize=1)
def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _inverse_centered_bound(loss, weight, parameters):
    """eps*sqrt(expm1(log1p(loss/(a*(eps/scale)^p))/k)).

    The log argument is formed through log(1+exp(log_ratio)) to avoid a
    gratuitous division overflow. This is a floating formula, not a bound
    with directed rounding. No negative loss is clipped to zero.
    """
    if loss < 0 or not math.isfinite(loss) or weight <= 0 or not math.isfinite(weight):
        raise ValueError('A finite nonnegative centered loss and positive weight are required')
    if loss == 0:
        return 0.
    p = parameters
    log_ratio = math.log(loss)-math.log(weight)-p.p*(math.log(p.epsilon)-math.log(p.scale))
    if log_ratio > 0:
        log_one_plus = log_ratio+math.log1p(math.exp(-log_ratio))
    else:
        log_one_plus = math.log1p(math.exp(log_ratio))
    return p.epsilon*math.sqrt(math.expm1(log_one_plus/p.k))


def augment_statistics(residual, radial_weights, multiplicity, parameters,
                       original_statistics, *, stage_block=64):
    """Add R687 fields while retaining every original statistics field.

    Input residual is RAW (e,f,d), not native sqrt-orbit residual. Each
    original radial/orbit weight is applied once. No derivative, J, J*,
    geometry, or field evaluation occurs. The caller may explicitly select
    centered_phi_normalized for a same-Phi-minus-constant line search.
    """
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific R687 statistics require this public repository Actions')
    p = parameters
    r = np.asarray(residual)
    radial = np.asarray(radial_weights, dtype=float)
    orbit = np.asarray(multiplicity, dtype=float)
    if (r.ndim != 3 or r.shape[-1] != 3 or np.iscomplexobj(r)
            or radial.shape != (r.shape[0],) or orbit.shape != (r.shape[1],)
            or not np.isfinite(r).all() or not np.isfinite(radial).all()
            or not np.isfinite(orbit).all() or np.any(radial <= 0) or np.any(orbit <= 0)):
        raise ValueError('Keep every finite raw stage/angle/component and its positive original weight')
    if (p.p != 2*p.k or p.k < 1 or p.k != int(p.k)
            or not math.isfinite(p.epsilon) or p.epsilon <= 0
            or not math.isfinite(p.scale) or p.scale <= 0
            or stage_block < 1 or stage_block != int(stage_block)):
        raise ValueError('Use even p>=2, positive finite epsilon/scale and an integer stage block')
    for name, expected in (('p', p.p), ('epsilon', p.epsilon), ('scale', p.scale)):
        if original_statistics.get(name) != expected:
            raise ValueError('The original statistics must use these exact stage parameters')
    normalizer = float(radial.sum()*orbit.sum())
    if not math.isfinite(normalizer) or normalizer <= 0:
        raise ValueError('The complete positive weight normalization is not finite')
    if original_statistics.get('normalization') != normalizer:
        raise ValueError('Do not combine original and centered statistics with different weights')
    k = int(p.k)
    eps_scaled = p.epsilon/p.scale
    coefficients = [math.comb(k, j)*eps_scaled**(2*(k-j)) for j in range(1, k+1)]
    if any(not math.isfinite(value) or value <= 0 for value in coefficients):
        raise ArithmeticError('Finite arithmetic cannot retain every positive polynomial term')
    weighted_pieces = []
    with np.errstate(over='raise', invalid='raise', divide='raise', under='ignore'):
        for start in range(0, r.shape[0], int(stage_block)):
            stop = min(r.shape[0], start+int(stage_block))
            block = r[start:stop]/p.scale
            a, b, d = block[..., 0], block[..., 1], block[..., 2]
            # (u,v,w) are the three symmetric entries of (E/scale)^j.
            u, v, w = np.ones_like(a), np.zeros_like(b), np.ones_like(d)
            centered = np.zeros_like(a)
            for coefficient in coefficients:
                # Exact powers commute. Averaging the two off-diagonal
                # products defines the declared floating evaluation.
                u, v, w = (u*a+v*b,
                    .5*(u*b+v*d+v*a+w*b), v*b+w*d)
                centered += coefficient*(u*u+2*v*v+w*w)
            weighted_pieces.append(float(radial[start:stop]@(centered@orbit)))
    centered_loss = math.fsum(weighted_pieces)/normalizer
    if centered_loss < 0 or not math.isfinite(centered_loss):
        raise ArithmeticError('The computed positive centered loss is not finite/nonnegative')
    minimum_weight = float(radial.min()*orbit.min()/normalizer)
    if minimum_weight <= 0 or not math.isfinite(minimum_weight):
        raise ArithmeticError('No positive orbit weight may disappear in finite normalization')
    loss_zero = 2*eps_scaled**(2*k)
    if loss_zero <= 0 or not math.isfinite(loss_zero):
        raise ArithmeticError('The stated fixed constant floor is not representable')
    near_zero_factor = (p.scale*p.scale/k)*(p.scale/p.epsilon)**(2*k-2)
    normalized_centered = near_zero_factor*centered_loss
    if not math.isfinite(normalized_centered):
        raise ArithmeticError('The reported near-zero normalization overflows')
    maximum = float(original_statistics['max_gram'])
    ratio = maximum/p.epsilon
    block_ratio = 1. if k == 1 else (1+ratio*ratio)**(k-2)*(1+(2*k-1)*ratio*ratio)
    legacy_phi = float(original_statistics['phi_normalized'])
    result = dict(original_statistics)
    result.update(
        centered_statistics_schema='R687-positive-polynomial-centered-spectral-statistics-v1',
        centered_statistics_source_sha256=source_sha256(),
        centered_phi_normalized=centered_loss,
        centered_phi_fixed_constant=loss_zero,
        centered_phi_plus_fixed_constant=centered_loss+loss_zero,
        legacy_phi_minus_centered_plus_constant=legacy_phi-(centered_loss+loss_zero),
        centered_phi_near_zero_quadratic_units=normalized_centered,
        centered_finite_max_formula_lower=_inverse_centered_bound(centered_loss, 2., p),
        centered_finite_max_formula_upper=_inverse_centered_bound(centered_loss, minimum_weight, p),
        centered_finite_max_quadratic_upper=math.sqrt(normalized_centered/minimum_weight),
        centered_hessian_Frobenius_weight_ratio_upper=block_ratio,
        centered_hessian_raw_three_component_ratio_upper=2*block_ratio,
        centered_evaluation_stage_block=int(stage_block),
        centered_evaluation='sum positive binomial coefficients times Frobenius squares of (E/scale)^j; positive original radial/orbit weights exactly once',
        centered_original_phi_field_retained=True,
        centered_same_mathematical_objective_up_to_fixed_constant=True,
        centered_true_gradient_unchanged=True,
        centered_residual_hessian_unchanged=True,
        centered_damping_units_unchanged=True,
        centered_near_zero_units_used_for_optimization=False,
        centered_formula_evaluation_outward=False,
        centered_underflow_and_roundoff_still_possible=True,
        centered_no_field_or_J_evaluations=True)
    return result
