"""R178 whole-angle first-order forcing at the accurate completed cut.

The constants use actual exact finite coefficients, the R171 accurate
terminal phase and R172 physical length.  No radial II jet is assigned at
tau=0.  No unknown n division is used.  The original R170 upper 6/5 is
verified; this source does not silently consume a later enlarged domain.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import rational, rational_pair, bound_record
from fd2d_gc_r136_arb_profile import ends
from fd2d_gc_terminal_angular_majorant import (
    cubic_terminal_K_bounds,tail_curvature_bounds,raw_vector_slope_bounds,
    sqrt_bounds,encode)

SCHEMA='fd2d-R178-accurate-terminal-whole-angle-forcing-v1'
ALLOWED_SCHEMAS=(
    'fd2d-accurate-last-P1-cell-physical-tail-v1',
    'fd2d-R170-accurate-last-P1-cell-physical-tail-v1',
)


def terminal_forcing_majorant(terminal, *, tau_upper=None, sqrt_bits=128):
    """Bound actual H=(-a Rn,a Rm,-a G) for 0<tau<=min(tau0,S-b).

    A rational upper bound on S-b is used only in inequalities.  S and the
    physical field remain the accurate definitions from the input object.
    """
    definition=terminal.definition()
    if definition.get('schema') not in ALLOWED_SCHEMAS:
        raise ValueError('Bind the explicit original 6/5-domain accurate last-cell constructor')
    if (not definition.get('identity_chart_on_entire_completed_cell')
            or not definition.get('seed_coast_and_bumps_zero')):
        raise ValueError('This exact terminal bound requires the declared protected physical region')
    lo,hi=ends(terminal.length)
    if lo<=0:
        raise ValueError('No positive accurate physical last-cell length enclosure')
    tau0=hi if tau_upper is None else rational(tau_upper)
    if not 0<tau0<=hi:
        raise ValueError('Use a positive terminal cutoff no larger than the bound last-cell width')
    last=terminal.profile.pieces[terminal.last_piece]
    raw_phase=last['raw']
    if (last['kind']!='phase_bridge'
            or raw_phase.get('exact_endpoint_phase')!='-pi/2'
            or raw_phase.get('ps0')!=0 or raw_phase.get('ps1')!=0):
        raise ValueError('The bound accurate phase is not the explicit cubic zero-slope terminal phase')
    ac=F(4,5)
    K=cubic_terminal_K_bounds(last['L_exact'],last['p0_exact'],tau0,
                             cut_radius=ac)
    # This routine rechecks every exact local coefficient against [0,6/5].
    # The old universal curvature cap is never borrowed for another domain.
    tail=tail_curvature_bounds(terminal.tail,ac+tau0)
    raw=raw_vector_slope_bounds(terminal.c0,terminal.K,lo)
    B0,B1=raw['B0'],raw['B1']
    Q0,Q1=tail['curvature'],tail['curvature_y']
    L=rational(last['L_exact'])
    delta_hi=K['phase_difference_upper']
    Ks2=54*delta_hi*delta_hi/(L**4*ac)+18*delta_hi*delta_hi*tau0/(L**4*ac*ac)
    sqrt_lo,sqrt_hi=sqrt_bounds(K['lower'],bits=int(sqrt_bits))
    if sqrt_lo<=0:
        raise ArithmeticError('Increase sqrt_bits to resolve the already-positive K coefficient')
    Ksqrt=Ks2/sqrt_lo
    old_width=terminal.E-terminal.b
    weight_length=rational(terminal.weight_length)
    if (old_width<=0 or weight_length<=0 or old_width>=weight_length
            or terminal.weight_start+weight_length!=terminal.E):
        raise ValueError('The actual pulled-back quintic tail weight has a different endpoint contract')
    q=old_width/(lo*weight_length)
    # eta=1-S5(q_exact*tau); eta_s<=30*q_upper^3*tau^2.
    weight_s_coefficient=30*q**3
    radius_upper=ac+tau0
    rs0=B0+Q1
    rs2=weight_s_coefficient*Q0
    ru0=radius_upper*Q1+2*Q0
    rn=dict(constant=rs0+ru0/(2*ac)+Q0/ac,
            sqrt_tau=Ksqrt/2,linear_tau=(B1/2+B0)/ac,
            quadratic_tau=rs2)
    rm=dict(constant=rs0/2+ru0/ac+Q0/ac,
            sqrt_tau=F(0),linear_tau=(B1+B0)/ac,
            quadratic_tau=rs2/2)
    H={key:radius_upper*(rn[key]+rm[key]) for key in rn}
    return dict(schema=SCHEMA,source=identity(__file__),
        angular_majorant_source=identity(Path(__file__).with_name(
            'fd2d_gc_terminal_angular_majorant.py')),
        terminal_definition=definition,
        actual_field_identity=terminal.inputs['field_arrays'],
        accurate_profile_target_binding=terminal.profile.input_binding_sha256,
        exact_tail_domain_upper=F(6,5),tail=tail,raw=raw,K=K,
        accurate_last_width=dict(lower=lo,upper=hi),
        accurate_endpoint_enclosure=bound_record(terminal.S),
        tau_upper=tau0,actual_domain='0<tau<=min(tau_upper,S-b); physical tau=S-s',
        physical_target_radius_lower=ac,physical_target_radius_upper=radius_upper,
        precise_weight=dict(old_width=old_width,weight_start=terminal.weight_start,
            weight_length=weight_length,q_upper=q,
            actual_q_times_last_width=old_width/weight_length,
            eta_s_over_tau_squared_upper=weight_s_coefficient),
        K_s_absolute_over_tau_squared_upper=Ks2,
        sqrt_K_coefficient_bounds=dict(lower=sqrt_lo,upper=sqrt_hi),
        K_s_over_sqrt_K_over_sqrt_tau_upper=Ksqrt,
        vector_bounds=dict(
            r_value='|r|<=Q0+B0*tau',
            r_s_constant=rs0,r_s_quadratic_tau=rs2,
            r_u_constant=ru0,r_u_linear_tau=B1,
            h_s='|h_s|<=|r_s|+|K_s|/sqrt(K)',
            h_u='|h_u|<=|r_u|'),
        Rn_absolute=rn,Rm_absolute=rm,
        H_norm_upper_coefficients=H,
        bound_meaning='norm(H)<=H0+Hhalf*sqrt(tau)+H1*tau+H2*tau^2',
        exact_G_is_zero_on_trace_platform=True,
        exact_G_proof='n=(h+d)/2,l=(h-d)/2,m=r2/2,h^2=d^2+4m^2+4K',
        no_n_denominator_used=True,
        U_s_is_exactly_zero_on_bound_region=True,
        all_angles_continuous_bound=True,
        cut_radial_II_derivative_assigned=False,
        II_uu_uniform_cut_limit_required=False,
        whole_surface_certificate=False)


def terminal_forcing_integrals(majorant, epsilon):
    """Actual H integral and its R119 position weight, fully rational upper bounds.

    The actual integration length may be smaller than epsilon (for example,
    the accurate last length is bounded by its rational upper endpoint).
    The returned numbers are monotone upper bounds for that shorter length.
    """
    eps=rational(epsilon)
    if not 0<=eps<=majorant['tau_upper']:
        raise ValueError('The requested cut window is outside the proved terminal region')
    root=sqrt_bounds(eps,bits=128)[1]
    c=majorant['H_norm_upper_coefficients']
    I=c['constant']*eps+F(2,3)*c['sqrt_tau']*eps*root
    I+=c['linear_tau']*eps**2/2+c['quadratic_tau']*eps**3/3
    J=c['constant']*eps**2/2+F(2,5)*c['sqrt_tau']*eps**2*root
    J+=c['linear_tau']*eps**3/3+c['quadratic_tau']*eps**4/4
    sup=c['constant']+c['sqrt_tau']*root+c['linear_tau']*eps+c['quadratic_tau']*eps**2
    return dict(epsilon_upper=eps,H_sup_upper=sup,
        H_integral_upper=I,tau_H_integral_upper=J,
        exact_full_angle_G_integral=F(0),
        scope='Actual terminal subinterval of physical length at most epsilon, lying in the bound accurate last cell',
        integral_values_are_rational_upper_bounds=True,
        no_value_of_radial_II_at_cut_required=True)


def complete_R119_terminal(majorant, epsilon, *, initial_D_upper,initial_C_upper):
    """Conditional last-interval update; actual initial bounds must be supplied."""
    d,c=map(rational,(initial_D_upper,initial_C_upper))
    if min(d,c)<0:
        raise ValueError('Supply genuine nonnegative initial D and C norm upper bounds')
    out=terminal_forcing_integrals(majorant,epsilon)
    eps=out['epsilon_upper']
    d1=d+out['H_integral_upper']
    c1=c+eps*d+out['tau_H_integral_upper']
    ratio=c1/majorant['physical_target_radius_lower']
    return dict(integrals=out,
        conditional_on_actual_initial_bounds=dict(D=d,C=c),
        final_D_upper=d1,whole_interval_C_upper=c1,
        whole_interval_relative_metric_upper=2*ratio+ratio*ratio,
        initial_bounds_verified_here=False,
        actual_frame_or_body_integrated=False,
        final_seam_or_reach_certificate=False)


__all__=['terminal_forcing_majorant','terminal_forcing_integrals',
         'complete_R119_terminal','encode']
