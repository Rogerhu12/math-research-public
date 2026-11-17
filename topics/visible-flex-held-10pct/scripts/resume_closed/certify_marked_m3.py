#!/usr/bin/env python3
"""Exact rational assembly of a nonzero fixed marker on the R23 closed m3 map.

Consumes the earlier full continuous geometry and recovered interval moment
bounds. It does not rerun the BVP or interval boxes. The marker radius is the
actual query radius a/2, rather than the radius a in the legacy moment report.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json
p=argparse.ArgumentParser(description=__doc__)
for name in ['geometry','moments','collar','out']:
    p.add_argument('--'+name,type=Path,required=True)
a=p.parse_args()
g=json.loads(a.geometry.read_text());m=json.loads(a.moments.read_text());c=json.loads(a.collar.read_text())
def q(x):return Q(int(x['numerator']),int(x['denominator']))
def view(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display_only=float(x))
assert m['success'] and g['marker_strength']==0
ac=q(c['a']);rc=ac/2;epsilon=eta=Q(1,2);b=1+eta
Zlo,Zhi=map(q,g['corrected_cap_height_interval']);K=q(g['curvature_upper']);R=q(g['radius_upper'])
d=Q(27,256)*epsilon*b*rc**2
v=2*epsilon*b*rc
normal_denominator=Q(1001,1000)
assert 1+v*v<normal_denominator**2
support=(Zlo-2*epsilon*b*rc**2)/normal_denominator
marker_K=10*epsilon*b
cap_norm2=ac**2+(Zhi+d)**2
assert marker_K<K and support>Q(4,5) and cap_norm2<R*R
base_gap=q(m['baseline_Qxx_minus_Qzz_lower'])
# For positive f, added Qzz <= area*2*fmax*(Zhi+fmax)^2.
# The rational enclosure 3 < pi < 22/7 suffices for strict eigenspace order.
marker_zz=2*Q(22,7)*rc**2*d*(Zhi+d)**2
xy_gap=3*epsilon*eta*rc**6/60
yz_gap=base_gap-marker_zz
assert xy_gap>0 and yz_gap>Q(2865,10000)
D=2*R;reach=Q(1,10)
assert D<Q(115121,50000) and reach/D>Q(434,10000)
H_diameter=2*Zlo
assert H_diameter/D>Q(69,100)
held_pi3=Q.from_float(m['held_support_difference_lower_pi3_pi6'][0])
held_pi6=Q.from_float(m['held_support_difference_lower_pi3_pi6'][1])
assert held_pi3>Q(12517,10**6) and held_pi6>Q(3242,10**6)
record=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 inputs={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest()for f in [a.geometry,a.moments,a.collar]},
 marker=dict(epsilon=view(epsilon),eta=view(eta),radius=view(rc),radius_is_query_a_over_2=True),
 marker_displacement_upper=view(d),marker_gradient_upper=view(v),marker_curvature_upper=view(marker_K),
 marker_support_lower=view(support),cap_radius_squared_upper=view(cap_norm2),
 centered_Qxx_minus_Qyy_strict_lower=view(xy_gap),centered_Qyy_minus_Qzz_lower=view(yz_gap),
 diameter_upper=view(D),reach_lower=view(reach),reach_over_D_lower=view(reach/D),
 held_H_diameter_lower=view(H_diameter),held_H_over_D_lower=view(H_diameter/D),
 delta_hold_lower=view(held_pi3),delta_hold_over_D_lower=view(held_pi3/D),
 noncongruent_phase='pi/6; inertia axes fixed, core cos(3 phi) becomes sin(3 phi)',
 noncongruent_pair_unaligned_hausdorff_lower=view(held_pi6),
 delta_E_strictly_positive=True,delta_E_numerical_lower_bound_computed=False,
 metric_on_modified_caps_exactly_fixed=True,whole_metric_certified=False,
 ten_percent_completion_asserted=False)
a.out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k]for k in ['marker_displacement_upper','marker_support_lower','centered_Qxx_minus_Qyy_strict_lower','centered_Qyy_minus_Qzz_lower','reach_over_D_lower','held_H_over_D_lower','delta_hold_over_D_lower','delta_E_strictly_positive']}))
