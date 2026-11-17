#!/usr/bin/env python3
"""Exact scalar geometry of the actual finite C2 collar and flat disk.

Input finite coefficients define the map, rather than enclosing an unknown
ODE solution. The separate interval background certificate supplies its true
integral height and positive normalization. No BVP is solved here.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,math
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--manifest',type=Path,required=True)
p.add_argument('--collar-exact',type=Path,required=True)
p.add_argument('--prefix-endpoint',type=Path,required=True)
p.add_argument('--background',type=Path,required=True)
p.add_argument('--reader',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
spec=importlib.util.spec_from_file_location('exact_collar_reader',a.reader)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
tail=module.IntegratedTail(a.manifest)
f=lambda x:Q.from_float(float(x))
def dec(x):return Q(int(x['numerator']),int(x['denominator']))
def show(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display_only=float(x))
meta=tail.meta;collar=json.loads(a.collar_exact.read_text())['rows'][0]
background=json.loads(a.background.read_text());prefix=json.loads(a.prefix_endpoint.read_text())
assert prefix['modes']==meta['parameters']['modes'] and meta['parameters']['spacing']==3
aa=f(meta['parameters']['rCuff']);b=f(meta['radialGeometry']['innerAnchor'])
c=f(meta['radialGeometry']['outerAnchor']);L=b-aa
assert L==dec(collar['L'])
K=dec(collar['K']);eta1=dec(collar['eta1']);eta2=dec(collar['eta2'])
B=f(8.001);assert L<=aa and L*B<=1 and eta1<1
assert Q(background['positive_exact_normalization']['lower_exact'])>100
assert Q(background['cell0_inner_radius']['lower_exact'])>b
assert Q(41,100)/Q(background['cell0_inner_radius']['lower_exact'])<8
# Exact integral of the finite mean perturbation; subsequent stored positions
# are diagnostics and do not define this coefficient.
P=tail.P
mean=f(tail.source_values[0,P])
for i,ell in enumerate(tail.unscaled_lengths):
    length=tail.radial_scale*f(ell)
    mean+=length*(Q(7,30)*(f(tail.first[i,P])+f(tail.first[i+1,P]))+
                  Q(8,15)*f(tail.midpoint[i,P])+
                  length*(f(tail.second[i,P])-f(tail.second[i+1,P]))/60)
zcut=f(prefix['mean_position'][2])
# The fixed target cut is nominal rCut. This finite representation's exact
# binary outer anchor is one ulp inside it; pay that tiny background interval.
target_cut=f(meta['parameters']['rCut']);assert 0<=target_cut-c<Q(1,10**14)
hlo=Q(background['exact_background_height']['lower_exact'])-Q(41,100)*(target_cut-c)
hhi=Q(background['exact_background_height']['upper_exact'])
zcap_lo=zcut+mean+hlo;zcap_hi=zcut+mean+hhi
V0=L*L*K;V1=2*L*K;Vt=V0
zlo=zcap_lo-L/Q(49)-V0;zhi=zcap_hi+V0
rhi=b+V0
jlo=1-V1-Vt/aa-V1*Vt/aa
jhi=1+V1+Vt/aa+V1*Vt/aa
nh=(Q(1,49)+V1)*(1+Vt/aa)+(Vt/aa)*(1+V1)
norm_hi=Q(1001,1000)
assert jlo>0 and jhi*jhi+nh*nh<norm_hi*norm_hi
support=(zlo*jlo-rhi*nh)/norm_hi
curvature=(B+eta2)/(1-eta1)**2
metric=2*eta1+eta1**2
norm_square=rhi*rhi+zhi*zhi
assert metric<Q(136,10**31) and curvature<Q(8002,1000)
assert support>Q(4,5) and norm_square<Q(817,1000)**2
assert rhi<Q(50563,10**6)
W160=Q(256,2**280);H160=Q(17)+Q(7,5)*160
deep_wr=Q(7,2)*Q(15,8)*W160*H160/(Q(1,25)*Q(1,5000*2**240))+7*W160/Q(1,25)
assert deep_wr<Q(1,20)
out=dict(scope=__doc__,inputs={str(z.resolve()):hashlib.sha256(z.read_bytes()).hexdigest()
    for z in [a.manifest,a.collar_exact,a.prefix_endpoint,a.background,a.reader]},
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actual_q=prefix['q'],mode=3,modes=prefix['modes'],physical_depth=8,
    exact_definition=dict(upper='X=(r e^{i theta}+V_xy, Zcap-h(r)-V_z)',
        background='h(r)=integral_a^r w(t)dt of the unchanged exact normalized rotational source; h=0 on the disk.',
        Zcap='zcut + exact_mean_V_at_outer_cut + integral_a^c w',
        collar='Quintic Hermite matches A0,A1,A2 at b and zero two-jets at a.',
        pole='The whole disk uses Cartesian (x,y,Zcap), including its center.',
        outer_boundary='Still requires an exact common-two-jet prefix repair; this component alone has one boundary.'),
    a=show(aa),b=show(b),c=show(c),L=show(L),target_cut_offset=show(target_cut-c),
    zcut=show(zcut),exact_mean_V_at_cut=show(mean),
    Zcap_lower=show(zcap_lo),Zcap_upper=show(zcap_hi),
    collar_Z_lower=show(zlo),collar_Z_upper=show(zhi),
    collar_XY_radius_upper=show(rhi),collar_and_disk_norm_squared_upper=show(norm_square),
    collar_support_lower=show(support),disk_support_lower=show(zcap_lo),
    collar_metric_upper=show(metric),collar_curvature_upper=show(curvature),
    background_deep_wr_upper_from_n160=show(deep_wr),
    safe_bounds=dict(collar_and_disk_support_strict_lower=.8,
       collar_and_disk_norm_strict_upper=.817,collar_xy_radius_strict_upper=.050563,
       collar_metric_strict_upper=1.36e-29,collar_curvature_strict_upper=8.002,
       disk_curvature=0,disk_metric_error_against_its_fixed_flat_metric=0),
    limits=['Only the collar/disk geometric bounds are continuous here.',
            'The outer finite tail retains the separate sampled audit.',
            'No full closed-sphere common-prefix seam or exact nonlinear infinite tail is asserted.'])
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(q=out['actual_q'],mean=float(mean),Zcap=[float(zcap_lo),float(zcap_hi)],
    support=float(support),norm_upper=math.sqrt(float(norm_square)),safe_bounds=out['safe_bounds'])),flush=True)
