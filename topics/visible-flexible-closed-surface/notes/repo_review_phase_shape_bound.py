#!/usr/bin/env python3
"""Small, dependency-free reproduction of the existing phase family's shape bound.

This does not solve a flexible surface.  It verifies exact scalar constants in
notes/2026-11-08-repo-amplitude-review.md.  Its geometric inequality is proved
there and does not use meshes, point correspondence, or a finite rotation grid.
"""
from fractions import Fraction as Q
import json

r = Q.from_float(.86)
sigma = Q.from_float(.94)
b = min(r/10, sigma/20)
A = b*b/(100*sigma)
cap_height = 2*A
D_collar_lower = 2*r
H_reported = Q('4.1965850822557265')
kappa_sampled = Q('94.69335042775782')
assert b == sigma/20
assert cap_height == sigma/20000
assert cap_height < Q(48,1000000)
assert cap_height/D_collar_lower < Q(28,1000000)
outward_ratio = '2.7325581396e-5'
assert cap_height/D_collar_lower < Q(outward_ratio)
# phi(t) <= (1-u)^4 (1+u) <= 1 for u=t^2 in [0,1].
# derivative of the middle polynomial is -(1-u)^3*(3+5*u) <= 0.
print(json.dumps({
 'status':'proved phase/cap inequality; reported H and kappa used only as numerical context',
 'cap_support_radius':float(b),
 'maximum_cap_bump_exact':str(cap_height),
 'maximum_cap_bump':float(cap_height),
 'delta_upper_all_phases':float(cap_height),
 'diameter_lower_exact':str(D_collar_lower),
 'diameter_lower_from_cap_boundary_approx':float(D_collar_lower),
 'delta_over_D_bound_exact':str(cap_height/D_collar_lower),
 'delta_over_D_upper_outward_decimal':outward_ratio,
 'delta_over_D_bound_approx':float(cap_height/D_collar_lower),
 'target_delta_over_D':0.05,
 'all_amplitude_local_marker_product_bound':float(Q(1,3200)),
 'required_delta_times_reach_over_D_squared':float(Q(3,2000)),
 'delta_over_D_upper_if_reach_at_least_003D_exact':str(Q(1,96)),
 'delta_over_D_upper_if_reach_at_least_003D_approx':float(Q(1,96)),
 'target_over_rigorous_upper':float(Q(1,20)*D_collar_lower/cap_height),
 'reported_cap_separation':float(2*H_reported),
 'delta_over_reported_cap_separation':float(cap_height/(2*H_reported)),
 'sampled_kappa_max':float(kappa_sampled),
 'reach_over_reported_cap_separation_upper_if_sample_validated':float(1/(kappa_sampled*2*H_reported)),
 'reach_target_at_reported_cap_separation':float(Q(3,100)*2*H_reported),
},indent=2))
