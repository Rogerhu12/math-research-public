#!/usr/bin/env python3
"""Exact-rational low-order error algebra for the declared closed SO3 field.

This kernel consumes valid point/enclosure bounds supplied by a same-field
continuous evaluator. It does NOT manufacture those bounds or convert a
floating sample into a continuous certificate. No calculation runs on
import. Scientific use, including exact bound evaluation, belongs only in
Rogerhu12/math-research-public Actions.

The Peano functional includes signed partial weights and nonzero mass.
Normalization and rotation bounds need Fs,Fss and their two angular jets;
no third radial derivative of the frozen parent is assumed.
"""
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path


SCHEMA = 'closed-SO3-exact-rational-low-order-error-algebra-v1'
ORIGINAL_OPERATOR_SHA = '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific same-field error bounds require public repository Actions')


def rational(value):
    """A binary64 input is interpreted as its exact rational word, never rounded."""
    if isinstance(value, bool):
        raise TypeError('A Boolean is not an exact numeric enclosure endpoint')
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError('Every exact rational input must be finite')
        return Fraction.from_float(value)
    if isinstance(value, str):
        if value.lower().startswith(('0x', '-0x', '+0x')):
            result = float.fromhex(value)
            if not math.isfinite(result):
                raise ValueError('Every exact binary carrier must be finite')
            return Fraction.from_float(result)
        return Fraction(value)
    raise TypeError('Use exact integers/rationals or explicitly retained binary64 carriers')


def nonnegative(value, name):
    value = rational(value)
    if value < 0:
        raise ValueError('A norm/error upper bound must be nonnegative: '+name)
    return value


def positive(value, name):
    value = rational(value)
    if value <= 0:
        raise ValueError('A strict lower bound must be positive: '+name)
    return value


def interval(value, name):
    if isinstance(value, (list, tuple)):
        if len(value) != 2:
            raise ValueError('Use two exact enclosure endpoints: '+name)
        lower, upper = map(rational, value)
    else:
        lower = upper = rational(value)
    if lower > upper:
        raise ValueError('Reversed enclosure endpoints: '+name)
    return lower, upper


def sqrt_upper(value, bits=96):
    """A proved dyadic upper square root, including exact zero."""
    require_actions()
    value = nonnegative(value, 'square-root argument')
    if bits != int(bits) or bits < 1:
        raise ValueError('Use a positive integer dyadic precision')
    denominator = 1 << int(bits)
    numerator = value.numerator*denominator*denominator
    root = math.isqrt(numerator//value.denominator)
    if root*root*value.denominator < numerator:
        root += 1
    return Fraction(root, denominator)


def _absolute_linear_integral(width, left, right):
    if width == 0:
        return Fraction(0)
    if left*right >= 0:
        return width*(abs(left)+abs(right))/2
    return width*(left*left+right*right)/(2*(abs(left)+abs(right)))


def peano_functional(nodes, weights, *, split=1, density_left=1, density_right=0):
    """Exact mass and L1 Peano kernel for a signed quadrature functional.

    mu = [alpha*1_[0,u]+beta*1_[u,1]]dt - sum_j weights_j delta_nodes_j.
    M(t)=alpha*min(t,u)+beta*max(t-u,0)-sum_(nodes_j<=t) weights_j.
    Every atom, including endpoints and duplicate literal nodes, is kept.
    No Gaussian-polynomial exactness or positivity of weights is assumed.
    """
    require_actions()
    if len(nodes) != len(weights) or not len(nodes):
        raise ValueError('Keep each actual quadrature node and its actual weight')
    u, alpha, beta = map(rational, (split, density_left, density_right))
    if not 0 <= u <= 1:
        raise ValueError('The exact query split must lie in its physical cell')
    atoms = {}
    literal = []
    for node, weight in zip(nodes, weights):
        node, weight = rational(node), rational(weight)
        if not 0 <= node <= 1:
            raise ValueError('An actual quadrature node lies outside the physical cell')
        atoms[node] = atoms.get(node, Fraction(0))+weight
        literal.append((node, weight))
    breaks = sorted(set([Fraction(0), Fraction(1), u, *atoms]))
    cumulative, kappa, pieces = Fraction(0), Fraction(0), []
    for left, right in zip(breaks[:-1], breaks[1:]):
        cumulative += atoms.get(left, Fraction(0))
        # Atom jumps at the right endpoint have measure zero in this L1
        # integral and are included on the following segment instead.
        ml = alpha*min(left, u)+beta*max(left-u, 0)-cumulative
        mr = alpha*min(right, u)+beta*max(right-u, 0)-cumulative
        contribution = _absolute_linear_integral(right-left, ml, mr)
        kappa += contribution
        pieces.append(dict(left=left, right=right, kernel_left=ml,
            kernel_right_before_atom=mr, absolute_integral=contribution))
    mass = alpha*u+beta*(1-u)-sum(weight for node, weight in literal)
    return dict(schema=SCHEMA, mass=mass, mass_absolute=abs(mass), peano_L1=kappa,
        split=u, density_left=alpha, density_right=beta,
        literal_nodes=[node for node, weight in literal],
        literal_weights=[weight for node, weight in literal],
        sum_absolute_weights=sum(abs(weight) for node, weight in literal),
        signed_weights_retained=True, duplicate_atoms_combined_only_at_exact_rational_equality=True,
        gaussian_exactness_assumed=False, segments=pieces,
        formula='integral X dmu = mass*X(1) - integral M(t)*X_prime(t) dt')


def quadrature_error(peano, *, physical_width, width_carrier,
                     value_norm_upper, radial_derivative_norm_upper,
                     node_value_errors, arithmetic_error):
    """A full scalar norm bound, including width and actual node errors.

    Node errors refer to the same exact affine physical nodes. If a field
    was evaluated on a shifted carrier point, that shift must already be
    included in node_value_errors. arithmetic_error pays actual reduction,
    multiplication and accumulation errors of the reported numerical sum.
    """
    require_actions()
    lower, upper = interval(physical_width, 'physical cell width')
    if lower <= 0:
        raise ValueError('The same exact physical cell width must be strictly positive')
    carrier = positive(width_carrier, 'working width carrier')
    B = nonnegative(value_norm_upper, 'integrand norm')
    L = nonnegative(radial_derivative_norm_upper, 'integrand radial derivative norm')
    errors = [nonnegative(value, 'actual node evaluation error') for value in node_value_errors]
    weights = [rational(value) for value in peano['literal_weights']]
    if len(errors) != len(weights):
        raise ValueError('Pay the error of every original signed quadrature node')
    mass = nonnegative(peano['mass_absolute'], 'functional mass defect')
    kappa = nonnegative(peano['peano_L1'], 'Peano L1 coefficient')
    width_error = max(abs(lower-carrier), abs(upper-carrier))
    exact_rule_error = upper*mass*B+upper*upper*kappa*L
    width_term = width_error*sum(abs(w) for w in weights)*B
    node_term = carrier*sum(abs(w)*error for w, error in zip(weights, errors))
    arithmetic = nonnegative(arithmetic_error, 'actual floating integral arithmetic')
    return dict(upper_error=exact_rule_error+width_term+node_term+arithmetic,
        exact_functional_error=exact_rule_error,
        mass_defect_error=upper*mass*B,
        radial_Lipschitz_error=upper*upper*kappa*L,
        physical_width_carrier_error=width_term,
        all_signed_node_evaluation_errors=node_term,
        actual_arithmetic_error=arithmetic,
        physical_width_lower=lower, physical_width_upper=upper,
        full_error_not_only_Gauss_truncation=True,
        supplied_norm_enclosures_independently_verified_by_this_kernel=False)


def normalized_parent_jet_bounds(*, Fs_norm_lower, Fs_s, Fs_phi,
                                 Fs_phiphi, Fs_sphi, Fs_sphiphi):
    """Bounds for U=Fs/|Fs| using only Fs,Fss and their two angular jets."""
    require_actions()
    nu = positive(Fs_norm_lower, 'continuous same-parent Fs norm lower')
    a, b, c, d, e = [nonnegative(value, name) for value, name in
        ((Fs_s, 'Fss'), (Fs_phi, 'Fsphi'), (Fs_phiphi, 'Fsphiphi'),
         (Fs_sphi, 'Fssphi'), (Fs_sphiphi, 'Fssphiphi'))]
    return dict(value=Fraction(1), s=a/nu, phi=b/nu,
        phiphi=c/nu+6*b*b/(nu*nu),
        sphi=d/nu+6*a*b/(nu*nu),
        sphiphi=e/nu+6*(a*c+2*d*b)/(nu*nu)+36*a*b*b/(nu**3),
        Fs_norm_lower=nu,
        normalization_first_Frechet_norm=1/nu,
        normalization_second_Frechet_norm=6/(nu*nu),
        normalization_third_Frechet_norm=36/(nu**3),
        parent_third_radial_derivative_used=False,
        classical_mixed_angular_jets_required=True)


def rotation_jet_bounds(*, omega_s, omega_phi, omega_phiphi,
                        omega_sphi, omega_sphiphi):
    """Global SO(3) norm bounds; no small omega or Rodrigues division used."""
    require_actions()
    a, b, c, d, e = [nonnegative(value, name) for value, name in
        ((omega_s, 'omega_s'), (omega_phi, 'omega_phi'),
         (omega_phiphi, 'omega_phiphi'), (omega_sphi, 'omega_sphi'),
         (omega_sphiphi, 'omega_sphiphi'))]
    return dict(value=Fraction(1), s=a, phi=b, phiphi=c+b*b,
        sphi=d+a*b, sphiphi=e+a*c+2*d*b+a*b*b,
        skew_exponential_Frechet_bound='||D^k exp(W)[A1,...,Ak]|| <= product ||Aj|| for real skew W',
        small_rotation_assumed=False, parallel_gauge_removed=False)


def meridian_jet_bounds(normalized_parent, rotation):
    """Uniform norms and radial Lipschitz bounds for T,Tphi,Tphiphi."""
    require_actions()
    names = ('value', 's', 'phi', 'phiphi', 'sphi', 'sphiphi')
    U = {name: nonnegative(normalized_parent[name], 'normalized parent '+name) for name in names}
    R = {name: nonnegative(rotation[name], 'rotation '+name) for name in names}
    if U['value'] != 1 or R['value'] != 1:
        raise ValueError('Use the exact unit meridian and orthogonal rotation bounds')
    return dict(
        T_norm=Fraction(1),
        Tphi_norm=R['phi']+U['phi'],
        Tphiphi_norm=R['phiphi']+2*R['phi']*U['phi']+U['phiphi'],
        T_radial_Lipschitz=R['s']+U['s'],
        Tphi_radial_Lipschitz=R['sphi']+R['s']*U['phi']+R['phi']*U['s']+U['sphi'],
        Tphiphi_radial_Lipschitz=R['sphiphi']+2*R['sphi']*U['phi']
            +R['s']*U['phiphi']+R['phiphi']*U['s']+2*R['phi']*U['sphi']+U['sphiphi'],
        parent_Fsss_needed=False, all_required_omega_and_parent_mixed_jets_retained=True)


def inverse_core_error(*, true_equation_residual_upper, rho_current_lower,
                       rho_current_phi_upper, rho_frozen_upper,
                       rho_frozen_phi_upper, core_jet_arithmetic_errors):
    """Inverse-chart contribution to Gamma,Gammaphi,Gammaphiphi.

    true_equation_residual_upper must include evaluating BOTH Theta_current
    and the fixed theta0, not only the observed floating Newton residual.
    A positive continuous rho_current bound is needed on the intervening
    branch; global circle positivity suffices. Angles use a common lift.
    The arithmetic errors include the complete support/trig/rho0/rho0prime/
    rho_current evaluation chain, not only the last vector addition.
    """
    require_actions()
    epsilon = nonnegative(true_equation_residual_upper, 'true inverse equation residual')
    delta = positive(rho_current_lower, 'current rho on the actual inverse branch')
    L = nonnegative(rho_current_phi_upper, 'current rho derivative')
    r0 = nonnegative(rho_frozen_upper, 'fixed parent rho')
    rp0 = nonnegative(rho_frozen_phi_upper, 'fixed parent rho derivative')
    if len(core_jet_arithmetic_errors) != 3:
        raise ValueError('Pay all three actual core-jet arithmetic evaluations')
    arithmetic = [nonnegative(value, 'actual core-jet arithmetic') for value in core_jet_arithmetic_errors]
    angle_error = epsilon/delta
    e0 = epsilon
    e1 = r0*angle_error
    e2 = (rp0+r0*r0/delta+r0*r0*L/(delta*delta))*angle_error
    return dict(inverse_angle_error=angle_error,
        Gamma_error=e0+arithmetic[0],
        Gammaphi_error=e1+arithmetic[1],
        Gammaphiphi_error=e2+arithmetic[2],
        core_value_bound_uses_unit_material_speed=True,
        inverse_equation_error_includes_function_evaluation=True,
        no_error_enclosure_inferred_from_plain_floating_residual=True,
        root_positivity_bound_independently_produced=False)


def complete_field_error(*, h_carrier, hp_carrier, hpp_carrier,
                         h_error, hp_error, hpp_error,
                         core_jet_errors, cap_jet_errors, total_integral_errors,
                         closure_arithmetic_errors,
                         field_integral_errors, delta_norm_uppers,
                         direct_T_error, direct_Ts_error, direct_Tphi_error,
                         field_arithmetic_errors):
    """Propagate every term of F=G+hDelta into the complete six physical jets.

    field_integral_errors[j] bounds the signed integral functional
    hhat*integral_0^s T_(phi^j) -(1-hhat)*integral_s^S T_(phi^j).
    total_integral_errors pay integral_0^S for Delta and its angular jets.
    closure_arithmetic_errors pay the actual Delta=Gamma-P+Istar operations.
    delta_norm_uppers bound the TRUE Delta_(phi^j). No Delta=0 is assumed.
    field_arithmetic_errors pay every remaining actual six-jet operation,
    including products and reductions, not only its last addition.
    """
    require_actions()
    def triple(values, name):
        if len(values) != 3:
            raise ValueError('Keep every angular jet: '+name)
        return [nonnegative(value, name) for value in values]
    h, hp, hpp = map(rational, (h_carrier, hp_carrier, hpp_carrier))
    eh, ehp, ehpp = [nonnegative(value, name) for value, name in
        ((h_error, 'h evaluation'), (hp_error, 'h prime evaluation'), (hpp_error, 'h second evaluation'))]
    C, P = triple(core_jet_errors, 'core jet'), triple(cap_jet_errors, 'cap jet')
    total = triple(total_integral_errors, 'complete total meridian integral')
    closure_arithmetic = triple(closure_arithmetic_errors, 'actual closure subtraction/addition')
    signed = triple(field_integral_errors, 'complete signed partial meridian integral')
    D = triple(delta_norm_uppers, 'actual closure discrepancy norm')
    errors = {key: nonnegative(field_arithmetic_errors[key], 'actual six-jet arithmetic '+key)
        for key in ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')}
    delta_errors = [C[j]+P[j]+total[j]+closure_arithmetic[j] for j in range(3)]
    for j, key in enumerate(('F', 'Fphi', 'Fphiphi')):
        errors[key] += abs(1-h)*P[j]+abs(h)*C[j]+signed[j]+eh*D[j]
    errors['Fs'] += nonnegative(direct_T_error, 'direct T evaluation')+abs(hp)*delta_errors[0]+ehp*D[0]
    errors['Fsphi'] += nonnegative(direct_Tphi_error, 'direct Tphi evaluation')+abs(hp)*delta_errors[1]+ehp*D[1]
    errors['Fss'] += nonnegative(direct_Ts_error, 'direct Ts evaluation')+abs(hpp)*delta_errors[0]+ehpp*D[0]
    return dict(six_jet_norm_errors=errors, closure_three_jet_errors=delta_errors,
        hprime_Delta_and_hsecond_Delta_retained=True,
        current_H_and_all_core_errors_retained=True,
        radial_Gram_identically_one_assumed=False,
        supplied_arithmetic_and_normalization_errors_independently_produced=False)


def relative_gram_error(*, Fs_hat_norm_upper, Fphi_hat_norm_upper,
                        Fs_error, Fphi_error, target_denominator_interval,
                        target_denominator_carrier, numerical_Gram_arithmetic_error,
                        sqrt_bits=96):
    """Bound the spectral-norm error of all three normalized Gram entries.

    numerical_Gram_arithmetic_error is a proved operator-norm bound for the
    complete numerical 2-by-2 normalized Gram arithmetic, not an individual
    scalar-entry error or a floating machine epsilon declaration.
    """
    require_actions()
    U = nonnegative(Fs_hat_norm_upper, 'computed Fs norm upper')
    W = nonnegative(Fphi_hat_norm_upper, 'computed Fphi norm upper')
    eu = nonnegative(Fs_error, 'complete Fs error')
    ew = nonnegative(Fphi_error, 'complete Fphi error')
    lo, hi = interval(target_denominator_interval, 'same exact a*rho0 denominator')
    if lo <= 0:
        raise ValueError('The exact same fixed target denominator must be strictly positive')
    carrier = positive(target_denominator_carrier, 'actual target denominator carrier')
    denominator_error = max(abs(lo-carrier), abs(hi-carrier))
    V = W/carrier
    ev = ew/lo+W*denominator_error/(lo*carrier)
    A = 2*U*eu+eu*eu
    B = U*ev+V*eu+eu*ev
    D = 2*V*ev+ev*ev
    eigen_bound = (A+D+sqrt_upper((A-D)**2+4*B*B, bits=sqrt_bits))/2
    row_bound = max(A+B, B+D)
    arithmetic = nonnegative(numerical_Gram_arithmetic_error, 'actual normalized Gram arithmetic')
    return dict(ss_error=A, sphi_error=B, phiphi_error=D,
        normalized_Fphi_error=ev, exact_target_denominator_lower=lo,
        spectral_norm_error=min(eigen_bound, row_bound)+arithmetic,
        actual_Gram_arithmetic_error=arithmetic, every_metric_component_retained=True,
        fixed_target_denominator_not_recomputed_from_current_core=True)


def serialize(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    return value


def metadata():
    return dict(schema=SCHEMA, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_original_SO3_operator_sha256=ORIGINAL_OPERATOR_SHA,
        exact_rational_error_algebra=True,
        numerical_field_or_J_recomputed=False,
        continuous_input_enclosures_required_from_caller=True,
        arbitrary_inputs_not_promoted_to_certificates=True,
        full_new_field_continuous_certificate_implemented=False,
        numerical_phase_or_isometry_acceptance_performed=False)
