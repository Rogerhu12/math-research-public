#!/usr/bin/env python3
"""Exact bookkeeping for the real-parameter principal-return existence gate.

All saved binary64 bounds are interpreted as exact dyadic rationals.  This
combines completed real target-type and R73 strip certificates; it does not
compute an effective KAM strip, a return residual, or parameter flow bounds.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data)if path.suffix=='.gz'else data)
def exact(value):return Fraction.from_float(float(value))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--strip',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_step5_small_parameter_modulus_1over56.json.gz'))
    p.add_argument('--type',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_affine_core_target_type.json'))
    p.add_argument('--root',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json'))
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    obj,strip,typ,root=map(read,(args.object,args.strip,args.type,args.root))
    ip,dp=Path(obj['origin_inputs']['path']),Path(obj['direction']['path'])
    if sha(ip)!=obj['origin_inputs']['sha256']or sha(dp)!=obj['direction']['sha256']:
        raise ValueError('actual affine input identity differs')
    origin,direction=sha(ip),sha(dp)
    if (not strip.get('proved_uniform_denominator_nonzero')or strip['status']!='complete'
        or not strip['complete_radial_coverage']or not all(row['passed']for row in strip['cells'])
        or strip['origin_inputs_sha256']!=origin or strip['frozen_direction_sha256']!=direction
        or strip['target_center_object_sha256']!=sha(args.object)):
        raise ValueError('completed same-object R73 strip certificate required')
    if (not typ.get('complete')or not typ.get('proved_exactly_two_target_roots_for_every_parameter')
        or not typ['exact_dyadic_outside_collar_coverage']or typ['failed_cells']or typ['pending']
        or typ['configuration']['origin_inputs_sha256']!=origin
        or typ['configuration']['frozen_direction_sha256']!=direction
        or typ['configuration']['common_root_certificate_sha256']!=sha(args.root)):
        raise ValueError('completed same-family whole-core target-type certificate required')
    if (not root.get('proved')or root['origin_inputs_sha256']!=origin or root['frozen_direction_sha256']!=direction):
        raise ValueError('same-family uniform simple-root certificate required')
    center=Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))
    interval=(center-Fraction(1,2000000),center+Fraction(1,2000000))
    for name,container in [('strip',strip['exact_parameter_interval']),('target_type',typ['configuration']['exact_parameter_interval']),('root',root['exact_parameter_interval'])]:
        lo,hi=map(exact,container)
        if not lo<=interval[0]<interval[1]<=hi:raise ValueError('parameter interval leaves '+name)
    radial=exact(typ['radial_core'][1]);S=Fraction(1,56)
    if exact(strip['radial_core'][1])<radial or exact(strip['angular_strip_width'])<S:
        raise ValueError('angular or radial strip is too small')
    tlo,thi=map(exact,typ['common_positive_root_bracket'])
    clo,chi=map(exact,typ['common_monotone_collar'])
    if not 0<clo<tlo<thi<chi<radial<Fraction(1,4):raise ValueError('root/collar/core nesting failed')
    if exact(typ['common_collar_Kprime'][0])<=0:raise ValueError('root collar is not strictly monotone')
    cells=sorted(typ['cells'],key=lambda row:row['x'][0]);gaps=[]
    if exact(cells[0]['x'][0])!=0 or exact(cells[-1]['x'][1])!=radial:
        raise ValueError('outside-collar cover endpoints differ')
    for a,b in zip(cells,cells[1:]):
        right,left=exact(a['x'][1]),exact(b['x'][0])
        if right>left:raise ValueError('outside-collar cells overlap out of order')
        if right<left:gaps.append((right,left))
    if gaps!=[(clo,chi)]:raise ValueError('the only missing interval must be the proved root collar')
    outside=max(abs(exact(v))for row in cells for v in row['K'])
    collar=max(abs(exact(v))for v in typ['common_collar_Kprime'])*(chi-clo)
    Kmax=max(outside,collar)
    if not Kmax<2 or exact(typ['minimum_a'])<=0 or exact(typ['minimum_E'])<=0:
        raise ValueError('uniform real metric/curvature bounds failed')
    drift=max(exact(row['drift_derivative_bounds'][0])for row in strip['cells'])
    wave=max(exact(row['wave_factor_derivative_bounds'][0])for row in strip['cells'])
    nmin=min(exact(row['Nraw_modulus_lower'])for row in strip['cells'])
    if not drift<9 or not wave<7 or not nmin>Fraction(2259,10000):
        raise ValueError('the exact quotient bounds are too large')
    with np.load(ip,allow_pickle=False)as z:frozen={k:z[k].copy()for k in z.files}
    with np.load(dp,allow_pickle=False)as z:
        if json.loads(str(z['metadata']))['origin_inputs_sha256']!=origin:
            raise ValueError('direction does not preserve the same frozen scalar grids')
        if z['phase_direction_coefficients'].shape!=frozen['phase_coefficients'].shape:
            raise ValueError('phase affine direction has a different coefficient shape')
    profiles=[('base',int(frozen['base_degree']),4),('phase',5,4),('shift',int(frozen['shift_degree']),4)]
    profiles.extend(('mean'+str(j),int(frozen['mean'+str(j)+'_degree']),4)for j in range(3))
    profiles.extend(('height'+str(j)+'_primitive',int(frozen['height'+str(j)+'_primitive_degree']),5)for j in range(4))
    continuity=[];common=set()
    for name,degree,minimum in profiles:
        knots=list(map(exact,frozen[name+'_knots']))
        left,right=knots[degree],knots[-degree-1]
        if not (left<-radial and radial<right):raise ValueError('core leaves scalar physical domain')
        count=Counter(knots);interior={v:m for v,m in count.items()if left<v<right}
        achieved=min((degree-m for m in interior.values()),default=degree)
        if achieved<minimum:raise ValueError('actual scalar continuity is insufficient')
        common.update(knots);common.update(-v for v in knots)
        continuity.append(dict(profile=name,degree=degree,minimum_interior_continuity=achieved,
            distinct_interior_knots=len(interior),exact_equal_knots_counted=True))
    if any(tlo<=k<=thi for k in common):raise ValueError('the family root bracket crosses an actual scalar knot')
    root_span=max(k for k in common if k<tlo),min(k for k in common if k>thi)
    physical_bound=Fraction(1,4)*(9+7*Fraction(3,2))
    if not physical_bound==Fraction(39,8)or not physical_bound<5:raise ValueError('field constant arithmetic failed')
    result=dict(kind='exact_real_parameter_principal_return_existence_inputs',proved=True,
        source_sha256=sha(__file__),target_object_sha256=sha(args.object),origin_inputs_sha256=origin,
        frozen_direction_sha256=direction,strip_certificate_sha256=sha(args.strip),
        target_type_certificate_sha256=sha(args.type),common_root_certificate_sha256=sha(args.root),
        exact_parameter_interval=list(map(str,interval)),physical_theta_strip=str(S),
        exact_root_common_span=list(map(str,root_span)),scalar_continuity=continuity,
        curvature_bound_exact=dict(outside_collar=str(outside),inside_collar=str(collar),global_upper=str(Kmax),less_than_two=True),
        quotient_bounds_exact=dict(drift=str(drift),wave=str(wave),Nraw_lower=str(nmin)),
        coarse_physical_time_field_bound='5',inner_state_strip='1/112',theta_Lipschitz_bound='560',
        total_two_leg_time='2*pi',real_return_derivative_bounds=['exp(-1120*pi)','exp(1120*pi)'],
        common_physical_initial_strip='exp(-1120*pi)/224',common_normalized_initial_strip='exp(-1120*pi)/56',
        limitations=['The common existence strip is deliberately extremely small and is not an effective R31 input',
            'No quantitative parameter derivatives, twist, conjugacy residual, or full PDE inverse are supplied',
            'This is the exact R37 modified principal field with the synchronous target g0(delta), not an isometric surface family'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(proved=True,K_upper=float(Kmax),physical_field_bound=5,scalar_profiles=len(continuity),sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()

