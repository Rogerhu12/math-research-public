#!/usr/bin/env python3
"""Scale all 32 nonconstant R225 support coefficients, then fix a new metric.

The finite core is exact rational data. A scalar profile can be retained,
but its angular metric changes with the new core: this is a design change,
not a fixed-g comparison with R225. No closed-surface claim is made.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def r225_coefficients():
    b = [Q(1)]
    for k in range(96):
        b.append(b[-1]*(Q(1, 2)-k)/(k+1))
    t = Q(7, 13)
    return [Q(52, 35)*sum(b[k+n]*b[k]*t**(n+2*k) for k in range(65))
            for n in range(1, 33)]


def interval(x, digits=24):
    scale = 10**digits
    lower = (x.numerator*scale)//x.denominator
    def decimal(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return sign+str(n//scale)+'.'+str(n % scale).zfill(digits)
    return [decimal(lower), decimal(lower+1)]


def describe(c, factor, k0):
    hmax = 1+sum(c)
    hmin = 1+sum((-1)**n*x for n, x in enumerate(c, 1))
    rmin = 1+sum((1-4*n*n)*x for n, x in enumerate(c, 1))
    rmax = 1+sum((-1)**n*(1-4*n*n)*x for n, x in enumerate(c, 1))
    gap = hmax-hmin
    assert factor > 0 and rmin > 0 and hmin > 0
    vals = dict(hmax=hmax, hmin=hmin, rho_min=rmin, rho_max=rmax,
                core_gap=gap, core_diameter=2*hmax,
                core_principal_curvature=max(1/rmin, k0*rmax),
                inlet_ball_second_order_product=k0*gap*rmax,
                amplitude_diameter_limit=5*gap,
                curvature_only_diameter_limit=Q(100, 3)/max(1/rmin, k0*rmax))
    return dict(scale=str(factor), k0=str(k0),
                exact={k:str(v) for k,v in vals.items()},
                decimal_intervals={k:interval(v) for k,v in vals.items()},
                estimates={k:float(v) for k,v in vals.items()},
                inlet_ball_second_order_pass=vals['inlet_ball_second_order_product'] < 1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--scale', default='6/5')
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args()
    factor = Q(a.scale)
    source = a.profile.read_bytes()
    saved = json.loads(source)
    old = saved['geometry']
    k0 = Q(float(old['initial_law']['k0']))
    assert canonical_hash(old) == saved['geometry_sha256']
    original = r225_coefficients()
    assert [Q(x) for x in old['coefficients_rational']] == original
    scaled = [factor*x for x in original]
    core = dict(schema='scaled-r225-exact-32-core-v1', scale=str(factor),
                base_definition='R225 equation 225.1; all 32 rational coefficients recomputed',
                coefficients_rational=[str(x) for x in scaled],
                statement='The constant support coefficient remains exactly one.',
                bounds=describe(scaled, factor, k0))
    core_hash = canonical_hash(core)
    geometry = dict(old)
    geometry['coefficients_rational'] = core['coefficients_rational']
    geometry['core_sha256'] = core_hash
    profile = dict(saved)
    profile.update(schema='scaled-r225-fixed-scalar-profile-v1', geometry=geometry,
                   geometry_sha256=canonical_hash(geometry),
                   source_profile_sha256=hashlib.sha256(source).hexdigest(),
                   source_scalar_coefficient_sha256=saved['exact_coefficient_sha256'],
                   new_metric_design=True,
                   description='All scalar knots and exact polynomial coefficients are unchanged. '
                               'The full core, rho0 and hence the angular metric are new.')
    sweep = [describe([f*x for x in original], f, k0)
             for f in map(Q, ('1','11/10','23/20','6/5','49/40','5/4'))]
    summary = dict(scope=__doc__, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   input_profile_sha256=hashlib.sha256(source).hexdigest(),
                   core_definition_sha256=core_hash,
                   selected=core['bounds'], sweep=sweep,
                   exact_scalar_profile_unchanged=True,
                   geometry_sha256=profile['geometry_sha256'],
                   original_geometry_sha256=saved['geometry_sha256'],
                   full_core_and_material_density_must_be_recomputed=True,
                   actual_ode_solved=False)
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    for name, value in (('core',core), ('profile',profile), ('summary',summary)):
        out = Path(str(a.out_prefix)+'-'+name+'.json')
        with out.open('x') as f:
            json.dump(value,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(scale=str(factor), estimates=core['bounds']['estimates'],
                          geometry_sha256=profile['geometry_sha256']),indent=2))


if __name__ == '__main__':
    main()
