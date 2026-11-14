#!/usr/bin/env python3
"""Exact algebra behind the genuine three-site Schur phase calculation."""
import hashlib
import json
from pathlib import Path
import sympy as sp

S, e, f = sp.symbols('S e f', positive=True)
p2 = S**2 - 2*e
p3 = S**3 - 3*S*e + 3*f
p4 = S**4 - 4*S**2*e + 2*e**2 + 4*S*f
T = p3 - p2**2/S
bridge = sp.factor((S*T - 2*p4 + 4*p2*p3/S - 2*p2**3/S**2 - T**2/e)/e**2)
Z = sp.factor(S/e - 2/S - T/e**2)
phase = sp.factor(bridge + e*Z**2)
assert sp.cancel(bridge - f*(S*e-9*f)/e**3) == 0
assert sp.cancel(Z - (2/S-3*f/e**2)) == 0
assert sp.cancel(phase - (4*e/S**2+S*f/e**2-12*f/(S*e))) == 0
x, y, z = sp.symbols('x y z')
subs = {S: x+y+z, e: x*y+x*z+y*z, f: x*y*z}
numerator = S**2*e**2 - 4*e**3 - S**3*f + 12*S*e*f
squares = x**2*y**2*(x-y)**2 + x**2*z**2*(x-z)**2 + y**2*z**2*(y-z)**2
remainder = (f*(S**3+2*S*e+9*f)).subs(subs)
assert sp.expand(numerator.subs(subs)-squares-remainder) == 0
special = sp.factor(phase.subs({e:S, f:1}))
assert sp.cancel(sp.Rational(25,48)-special-(5*S-24)**2/(48*S**2)) == 0
output = {
    'status': 'exact-physical-Schur-and-positive-square-identities',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'bridge': str(bridge),
    'Z': str(Z),
    'complete_phase': str(phase),
    'one_minus_phase_numerator': str(numerator),
    'positive_square_identity_verified': True,
    'reciprocal_three_site_phase': str(special),
    'reciprocal_phase_bound': '25/48',
    'standard_representation_reduction': 'Full physical pool birth-one module, proved in the accompanying note.',
    'whole_five_site_lower_source_dimension': 4,
    'whole_five_site_phase_limit_upper_bound': '3/4, strict',
    'whole_six_site_critical_source_dimension': 9,
    'finite_weak_site_bound': '7/8 for each fixed r and sufficiently small positive a',
    'all_weights_general_phase_claim': False,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':output['status'],'positive_square_identity_verified':True}))
