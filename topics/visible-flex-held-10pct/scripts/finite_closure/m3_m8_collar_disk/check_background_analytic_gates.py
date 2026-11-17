#!/usr/bin/env python3
"""Small outward-interval gates used in the fixed-background proof.

This checks literal parameters and elementary constants, without integrating
or running the nonlinear tail. The first-16-cell integral certificate remains
a separate input. Arrays of regenerated calibration constants stay scratch.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, json
import mpmath as mp

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--constants',type=Path,required=True)
p.add_argument('--integrals',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
d=json.loads(a.constants.read_text());c=d['parameters']
b=json.loads(a.integrals.read_text())
iv=mp.iv;iv.dps=60
def q(x):
    v=Q.from_float(float(x));return iv.mpf(v.numerator)/v.denominator
def lo(x):return mp.make_mpf(x._mpi_[0])
def hi(x):return mp.make_mpf(x._mpi_[1])
def record(x):return {'lower_display':float(lo(x)),'upper_display':float(hi(x))}
assert c['R']==64 and c['a']==2.75 and c['etaPower']==1.5
assert c['rCut']==.3 and c['wCut']==.08 and c['width']==.25
assert c['curvatureBound']==8 and c['orientation']==1 and c['protectCell']==160
assert c['prefixEnd']==15 and c['capMode']=='cut-preserving'
assert c['rejoinR20At'] is None and not c.get('flatOuterThroughCell',False)
assert c['pulseCaps']==[[.4,.02]] and c['valleyCaps']==[.1]
assert c['warpWeightLevels']==[[1,.5,3,.05,1]]
assert c['valleyControls'][:6]==[3.125,2.8125,4.0625,5,5.25,4.0625]
assert all(x==0 for x in c['valleyControls'][6:])
assert all(.5<=x['calibrationAlpha']<=2 for x in d['cells'])
assert all(x['R']==64 for x in d['cells'][16:])
assert all(x['lengthScale']==1 for x in d['cells'])
aa=q(c['rCuff']);dc=q(c['delta0']);cc=q(c['etaRatioAtN0'])
Y=6*dc+6*dc*cc/(1-iv.mpf(2)**(-iv.mpf(3)/2))
oldcut=aa*iv.exp(Y/iv.sqrt(12))
gates={
    'Y':Y,'exp7YoverSqrt12':iv.exp(7*Y/iv.sqrt(12)),
    'two_to_11over4':iv.mpf(2)**(iv.mpf(11)/4),
    'cut_over_oldcut_minus_one':q(c['rCut'])/oldcut-1,
    'raw_first_cell_plateau_slope_bound':q(c['wCut'])/dc*iv.mpf(2)**(-iv.mpf(11)/4)*iv.exp(7*Y/iv.sqrt(12)),
    'outer_last_port_slope_bound':q(c['wCut'])*iv.exp(7*dc*cc/iv.sqrt(12)),
    'last_log_jump':iv.ln(dc)+(iv.mpf(11)/4)*iv.ln(2),
    'log_point02':iv.ln(q(.02)),
    'log_four':iv.ln(4),
    'exp_three_over_two':iv.exp(iv.mpf(3)/2),
    'base_Wn_constant':q(c['wCut'])/dc*iv.mpf(2)**(-iv.mpf(11)/4)*64*iv.exp(7*Y/iv.sqrt(12)),
}
assert hi(Y)<iv.mpf(1)/20
assert hi(gates['exp7YoverSqrt12'])<iv.mpf(6)/5
assert lo(gates['two_to_11over4'])>6 and hi(gates['two_to_11over4'])<7
assert lo(gates['cut_over_oldcut_minus_one'])>4
assert hi(gates['raw_first_cell_plateau_slope_bound'])<4
assert hi(gates['outer_last_port_slope_bound'])<iv.mpf(1)/10
assert hi(gates['last_log_jump'])<-3
assert hi(gates['log_point02'])<-iv.mpf(19)/5
assert hi(gates['log_four'])<iv.mpf(7)/5
assert lo(gates['exp_three_over_two'])>4
assert hi(gates['base_Wn_constant'])<256
assert Q(b['positive_exact_normalization']['lower_exact'])>100
assert Q(41,100)/Q(b['cell0_inner_radius']['lower_exact'])<8
out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    constants_sha256=hashlib.sha256(a.constants.read_bytes()).hexdigest(),
    integrals_sha256=hashlib.sha256(a.integrals.read_bytes()).hexdigest(),
    all_assertions_passed=True,interval_precision=60,
    gates={k:record(v)for k,v in gates.items()},
    statement='The fixed rotational background has |kappa_i|<=8 and C2 flat-cuff extension, subject only to the cited original deep calibration-root bracket.')
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'gates':len(gates)}))
