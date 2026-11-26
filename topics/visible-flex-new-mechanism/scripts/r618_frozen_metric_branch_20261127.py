#!/usr/bin/env python3
"""Pure fixed-target identity, same-root derivative budget and branch solver.

No reference q, source input, angular rule, ODE, candidate or execution scope
is invented here. The caller supplies an actual completed public checkpoint
and a complete mathematical field definition. A target's continuous root is
fixed by that definition; subsequent numerical calls approximate it.

All scientific calls require a later explicitly declared public Actions
scope. Interval consequences retain the caller's unresolved radial/tail/
roundoff status. This interface never promotes an angular-only budget into
a continuous whole-field or README certificate.
"""
from dataclasses import dataclass
from collections import defaultdict
import hashlib
import json
import math
import os
from pathlib import Path

BACKEND_SHA = 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'
backend_path = Path(__file__).with_name('r611_circular_reference_global_geometry_20261127.py')
if hashlib.sha256(backend_path.read_bytes()).hexdigest() != BACKEND_SHA:
    raise RuntimeError('the outward arithmetic backend changed')
from r611_circular_reference_global_geometry_20261127 import I, exp_i
COUNTS = defaultdict(int)


def require_public_science():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('scientific evaluation requires the named public Actions scope')


@dataclass(frozen=True)
class FrozenTargetIdentity:
    source_state_json: str
    source_state_sha256: str
    mathematical_field_json: str
    mathematical_field_sha256: str
    target_sha256: str

    @classmethod
    def bind(cls, source_state_json, source_state_sha256,
             mathematical_field_json, mathematical_field_sha256):
        """Only JSON/hash work: no source root, field or geometry is evaluated.

        The complete source input is kept literally. The field manifest must
        name actual q/reconstruction/source identities and endpoint meanings;
        a node table alone is rejected. Correct provenance remains reviewable
        against the original completed public log, not inferred from a hash.
        """
        for raw, digest in ((source_state_json,source_state_sha256),
                            (mathematical_field_json,mathematical_field_sha256)):
            if not isinstance(raw,str) or hashlib.sha256(raw.encode()).hexdigest() != digest:
                raise ValueError('literal complete frozen input identity differs')
        source, definition = json.loads(source_state_json), json.loads(mathematical_field_json)
        if not isinstance(source,dict) or not isinstance(definition,dict):
            raise ValueError('complete source and field manifests must be objects')
        required = ('actual_accepted_q_sha256', 'completed_public_origin',
            'reconstruction_source_sha256', 'all_source_sha256',
            'radial_domain', 'accurate_inner_tail_definition',
            'complete_connector_core_definition', 'all_literal_parameters',
            'unresolved_evaluation_errors')
        if any(key not in definition for key in required):
            raise ValueError('a full field definition, not a node table, is required')
        if definition.get('canonical_mean_points') != 512:
            raise ValueError('the original canonical512 height definition changed')
        if definition.get('metric_definition') != 'continuous_turning_root_of_this_fixed_reference_height':
            raise ValueError('the target must be the one continuous reference-root function')
        if definition.get('metric_derivative_definition') != '2_W_Wr_plus_2_continuous_weighted_G_mean':
            raise ValueError('the metric derivative must belong to the same scalar root')
        payload = (source_state_sha256+'\n'+mathematical_field_sha256+'\n').encode()
        return cls(source_state_json,source_state_sha256,mathematical_field_json,
                   mathematical_field_sha256,hashlib.sha256(payload).hexdigest())


def split_metric_from_same_root(identity, *, W, W_r, e_N, mu_N,
        root_radius, N, rho, Omega, G_norm, G_e_norm, velocity_gap,
        weight_lower, input_error_status):
    """One outward evaluation of the fixed target's e and true e_r.

    All supplied scalar quantities are I-values. mu_N must already include
    its own paid numerical error. root_radius includes the original root
    residual/angular budget. The five majorants hold on that WHOLE root
    interval, not just at e_N. input_error_status explicitly preserves any
    conditional exact-radial-coefficient assumption from the original scope.
    """
    require_public_science()
    COUNTS['split_same_root_metric_evaluations'] += 1
    if not isinstance(identity,FrozenTargetIdentity) or not isinstance(N,int) or N <= 0:
        raise TypeError('fixed source identity and actual angular count required')
    values = (W,W_r,e_N,mu_N,root_radius,rho,Omega,G_norm,G_e_norm,
              velocity_gap,weight_lower)
    if not all(isinstance(value,I) for value in values):
        raise TypeError('outward same-root input intervals required')
    if (rho.lo <= 0 or velocity_gap.lo <= 0 or weight_lower.lo <= 0
            or min(root_radius.lo,Omega.lo,G_norm.lo,G_e_norm.lo) < 0):
        raise ArithmeticError('continuous angular root-budget domain unresolved')
    if input_error_status not in ('all_input_errors_enclosed',
            'conditional_exact_radial_coefficients_and_roundoff'):
        raise ValueError('unresolved source errors must be explicit')
    alias = 2*exp_i(-N*rho)*Omega*G_norm/weight_lower
    mu_e = (3*Omega*G_norm/velocity_gap+Omega*G_e_norm)/weight_lower
    extra = alias+root_radius*mu_e
    e = e_N+I(-root_radius.hi,root_radius.hi)
    mu = mu_N+I(-extra.hi,extra.hi)
    e_r = 2*mu
    return {'target_sha256':identity.target_sha256,
        'W':W,'W_r':W_r,'e':e,'e_r':e_r,
        'E':W**2+e,'E_r':2*W*W_r+e_r,
        'mu_alias_upper':alias.hi,'mu_e_upper':mu_e.hi,
        'additional_e_r_radius_upper':(2*extra).hi,
        'input_error_status':input_error_status,
        'same_continuous_root_function_at_every_grid':True,
        'complete_radial_or_whole_surface_certificate':False}


def center_same_canonical_height(canonical_jets, W, W_r, angular_mean):
    """Synchronous (7)--(8); no old height or derivative is replaced.

    The caller supplies f,fr,frr,ft,ftt,frt at ONE radius on one angular domain.
    angular_mean may be an accurately enclosed continuous functional or a
    declared numerical approximation; its uncertainty is not erased here.
    """
    require_public_science()
    COUNTS['same_height_mean_transfers'] += 1
    means = [angular_mean(canonical_jets[key]) for key in ('f','fr','frr')]
    result = dict(canonical_jets)
    for key, mean in zip(('f','fr','frr'),means):
        result[key] = canonical_jets[key]-mean
    return {'centered_jets':result,'mean_height_correction':means[0],
        'reference_p0':-W+means[1],'reference_p0_r':-W_r+means[2],
        'same_field_synchronous_mean_transfer':True,
        'continuous_mean_errors_certified_by_this_call':False}


@dataclass(frozen=True)
class MeanBranch:
    target_sha256: str
    response_sha256: str
    variable: str
    lower: float
    upper: float
    derivative_on_entire_bracket: object
    all_positive_domain_margins_on_entire_bracket: bool
    input_error_status: str


class UnresolvedMeanBranch(ArithmeticError):
    pass


def solve_same_decreasing_branch(branch, evaluate, *, absolute_width,
                                 maximum_steps=100, maximum_effort=8):
    """Safeguarded interval scalar root with the ONE supplied target identity.

    evaluate(x,effort) returns residual I for T-1 (or its declared stable
    endpoint normalization), target_sha256, response_sha256, input_error_status.
    The derivative enclosure is valid on the original ENTIRE branch box.
    No E solve, branch replacement or amplitude reset is a fallback here.
    Increasing effort requests a tighter evaluation of the SAME function.
    """
    require_public_science()
    COUNTS['same_branch_root_calls'] += 1
    if not isinstance(branch,MeanBranch) or branch.variable not in (
            'bulk_p0','inner_rationalized_lambda','core_zeta'):
        raise TypeError('one explicit stable mean-root variable required')
    derivative = branch.derivative_on_entire_bracket
    if (not isinstance(derivative,I) or derivative.hi >= 0
            or not branch.all_positive_domain_margins_on_entire_bracket):
        raise UnresolvedMeanBranch('complete positive-domain/negative-derivative box missing')
    lo,hi = branch.lower,branch.upper
    if not (math.isfinite(lo) and math.isfinite(hi) and lo < hi and absolute_width > 0):
        raise ValueError('finite ordered branch and positive requested width required')
    kappa = I(-derivative.hi)
    calls = effort_increases = 0
    effort = 0
    def read(x,level):
        nonlocal calls
        calls += 1
        COUNTS['mean_residual_enclosure_evaluations'] += 1
        row = evaluate(x,level)
        if (row['target_sha256'] != branch.target_sha256
                or row['response_sha256'] != branch.response_sha256
                or row['input_error_status'] != branch.input_error_status):
            raise UnresolvedMeanBranch('target, response or uncertainty identity changed during a root')
        value = row['residual']
        if not isinstance(value,I):
            raise TypeError('same-function residual enclosure required')
        return value
    while True:
        left,right = read(lo,effort),read(hi,effort)
        if left.lo >= 0 and right.hi <= 0:
            break
        if effort >= maximum_effort:
            raise UnresolvedMeanBranch('original mean branch lacks opposite enclosed endpoint signs')
        effort += 1
        effort_increases += 1
        COUNTS['mean_enclosure_effort_increases'] += 1
    for iteration in range(maximum_steps):
        COUNTS['mean_root_interval_steps'] += 1
        if (I(hi)-lo).hi <= absolute_width:
            COUNTS['mean_root_calls_completed_to_width'] += 1
            return {'root':I(lo,hi),'target_sha256':branch.target_sha256,
                'response_sha256':branch.response_sha256,'variable':branch.variable,
                'input_error_status':branch.input_error_status,
                'iterations':iteration,'residual_evaluations':calls,
                'effort_increases':effort_increases,
                'same_bracketed_root_no_new_metric':True,
                'whole_radial_or_README_certificate':False}
        middle = lo/2+hi/2
        if not lo < middle < hi:
            raise UnresolvedMeanBranch('floating midpoint resolution exhausted before declared width')
        residual = read(middle,effort)
        # With F'<=-kappa, the true root lies in this directed interval.
        enclosure = I(middle)+I(min(0.,residual.lo),max(0.,residual.hi))/kappa
        newlo,newhi = max(lo,enclosure.lo),min(hi,enclosure.hi)
        if residual.lo >= 0:
            newlo = max(newlo,middle)
        if residual.hi <= 0:
            newhi = min(newhi,middle)
        if newlo > newhi:
            raise UnresolvedMeanBranch('inconsistent mean-root boxes')
        if newlo == lo and newhi == hi:
            if effort >= maximum_effort:
                raise UnresolvedMeanBranch('same-function quadrature/error radius prevents contraction')
            effort += 1
            effort_increases += 1
            COUNTS['mean_enclosure_effort_increases'] += 1
        else:
            lo,hi = newlo,newhi
    raise UnresolvedMeanBranch('declared scalar root iteration limit reached')


def core_homotopy_height_coefficient(target_current, target_reference,
                                    bare_P1_change, reference_mismatch, tau):
    """Coefficient multiplying the actual R618 radial Kc height function.

    At bare response=0,tau=0 this is exactly zero when the same cached
    target_reference is reused. At tau=1 the full continuous core graph is
    restored. The caller differentiates and inserts all six actual jets;
    this function never edits residual rows or a stored target metric.
    """
    require_public_science()
    COUNTS['core_homotopy_height_coefficients'] += 1
    if not 0 <= tau <= 1:
        raise ValueError('the explicit original-core repair parameter belongs to [0,1]')
    return target_current-target_reference-bare_P1_change+tau*reference_mismatch


def core_homotopy_full_residual(R, tau, reference_mismatch, current_u,
                              angular_mean):
    """Full-angle (14), including the current root's weighted constant."""
    require_public_science()
    COUNTS['core_homotopy_full_residuals'] += 1
    weighted_mean = angular_mean(reference_mismatch/current_u**3)/angular_mean(current_u**-3)
    return R*(1-tau)*(reference_mismatch-weighted_mean)
