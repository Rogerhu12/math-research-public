#!/usr/bin/env python3
"""Combine the literal closed-map geometry certificates using exact Fractions.

R21 used the directly recovered source mean at the cut. The new shared-jet
prefix has a slightly different finite mean constant. This script pays that
one global vertical translation on both collar/cap copies before combining
the three pieces. No isometry or strict noncongruence is asserted.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,math

p=argparse.ArgumentParser(description=__doc__)
for k in ['prefix-audit','prefix-certificate','tail-certificate','collar-certificate','out']:
    p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args()
pre=json.loads(a.prefix_audit.read_text())
pc=json.loads(a.prefix_certificate.read_text())
tc=json.loads(a.tail_certificate.read_text())
cc=json.loads(a.collar_certificate.read_text())
def q(v):return Q(int(v['numerator']),int(v['denominator']))
def view(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))
assert pc['success'] and not pc['failed_boxes']
shift=Q.from_float(pre['zcut_mean'])-q(cc['zcut'])
sigma_collar=min(q(cc['collar_support_lower']),q(cc['disk_support_lower']))-abs(shift)
Zlo=q(cc['Zcap_lower'])+shift;Zhi=q(cc['Zcap_upper'])+shift
collar_norm=Q(817,1000)+abs(shift)
sigma=min(Q.from_float(pc['bounds']['support_lower']),q(tc['support_lower']),sigma_collar)
K=max(Q.from_float(pc['thresholds']['curvature']),q(tc['curvature_upper']),q(cc['collar_curvature_upper']))
radius=max(Q.from_float(pc['bounds']['radius_upper']),q(tc['radius_upper']),collar_norm)
reach=min(sigma,1/K);diameter=2*radius
assert sigma>Q(7,10) and K<=10 and radius<Q(115121,100000)
assert reach>=Q(1,10) and reach/diameter>Q(434,10000)
out=dict(scope=__doc__,inputs={str(x.resolve()):hashlib.sha256(x.read_bytes()).hexdigest()for x in
    [a.prefix_audit,a.prefix_certificate,a.tail_certificate,a.collar_certificate]},
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    previous_to_shared_mean_translation=view(shift),corrected_collar_support_lower=view(sigma_collar),
    corrected_cap_height_interval=[view(Zlo),view(Zhi)],support_lower=view(sigma),curvature_upper=view(K),
    radius_upper=view(radius),diameter_upper=view(diameter),reach_lower=view(reach),
    reach_over_diameter_lower=view(reach/diameter),safe_bounds=dict(support_strict_lower=.7,curvature_upper=10,
        radius_strict_upper=1.15121,diameter_strict_upper=2.30242,reach_lower=.1,reach_over_diameter_strict_lower=.0434),
    all_phase_reason='At marker strength 0 every phase image is a spatial rotation of the certified closed C2 surface; reflected lower charts and the two cap disks share exact two-jets.',
    embedding_and_reach_lemma='R1 / positive-support normal-offset lemma for a C2 immersion of S2',
    marker_strength=0,isometry_certified=False,strict_noncongruence_asserted=False,ten_percent_completion_asserted=False)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['safe_bounds','previous_to_shared_mean_translation']}))
