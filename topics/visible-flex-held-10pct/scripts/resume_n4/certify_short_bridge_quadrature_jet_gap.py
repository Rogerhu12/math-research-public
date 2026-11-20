#!/usr/bin/env python3
"""Exact rational moment certificate for the current ShortBridge GL64 formula.

Certifies the continuous real formula with frozen binary64 nodes, weights,
peak/eps/lengths against true primitives; it is not a blanket libm rounding
certificate and does not turn a tiny formal join-jet jump into exact C2.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, importlib.util, hashlib, json, math
import mpmath as mp
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--run',type=Path,required=True)
p.add_argument('--source',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--prefix-end',type=float,required=True)
p.add_argument('--end',type=float,required=True)
p.add_argument('--extension',default='1e-12')
a=p.parse_args()
mp.mp.dps=110
iv=mp.iv
iv.dps=85
def q(x):
    f=x if isinstance(x,F)else F.from_float(float(x))
    return iv.mpf(f.numerator)/f.denominator
def lower(x):return mp.make_mpf(x._mpi_[0])
def upper(x):return mp.make_mpf(x._mpi_[1])
def mag(x):return max(abs(lower(x)),abs(upper(x)))
def iv0():return iv.mpf(0)
def enclose_error(x):return iv.mpf([-upper(x),upper(x)])
def bounds(x):
    l=math.nextafter(float(lower(x)),-math.inf)
    h=math.nextafter(float(upper(x)),math.inf)
    return dict(lower=l,upper=h,lower_exact=str(F.from_float(l)),upper_exact=str(F.from_float(h)))
def upper_bound(x):
    y=math.nextafter(float(upper(x)),math.inf)
    return dict(upper=y,upper_exact=str(F.from_float(y)))
def mul(x,y):
    out=[x[0]*0 for _ in range(len(x)+len(y)-1)]
    for i,u in enumerate(x):
        for j,v in enumerate(y):out[i+j]+=u*v
    return out
def trig_poly(phi,kind,degree=28):
    zero=phi[0]*0
    one=zero+1
    out=[zero for _ in range(degree*(len(phi)-1)+1)]
    power=[one]
    for k in range(degree+1):
        if (kind=='sin' and k%2==1)or(kind=='cos'and k%2==0):
            sign=(-1)**((k-1)//2 if kind=='sin'else k//2)
            for j,v in enumerate(power):out[j]+=v*sign/math.factorial(k)
        power=mul(power,phi)
    return out
def exact_trig_poly(phi,kind,degree=28):
    out=[F(0)]*(degree*(len(phi)-1)+1)
    power=[F(1)]
    for k in range(degree+1):
        if (kind=='sin'and k%2==1)or(kind=='cos'and k%2==0):
            coeff=F((-1)**((k-1)//2 if kind=='sin'else k//2),math.factorial(k))
            for j,v in enumerate(power):out[j]+=v*coeff
        power=mul(power,phi)
    return out
run_bytes=a.run.read_bytes()
run=json.loads(run_bytes)
spec=importlib.util.spec_from_file_location('held10_short_bridge_gap_source',a.source)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
cut=run['physical_tail_cut']
bspec=run['physical_profile']['prefix_bridge']
assert bspec['curvature']==4 and bspec['peak_fraction']==.2
b=module.ShortBridge(cut,a_start=1.,curvature=4.,peak_fraction=.2)
node=[F.from_float(float((1+g)/2))for g in b.g]
weight=[F.from_float(float(w/2))for w in b.gw]
assert len(node)==len(weight)==64 and all(0<t<1 for t in node) and all(w>0 for w in weight)
ws=sum(weight,F(0))
degree=28
moments=[sum((w*t**j for w,t in zip(weight,node)),F(0))-F(1,j+1)for j in range(3*degree+1)]
peak_s,eps_s=F.from_float(b.peak),F.from_float(b.eps)
L1s,L2s,L3s=[F.from_float(x)for x in(b.L1,b.L2,b.L3)]
Ls=F.from_float(a.end)-F.from_float(a.prefix_end)
U=F(1)+F(a.extension)
assert 1<=U<=F(100000001,100000000)
assert 0<Ls and (Ls-L1s-L2s)/L3s<=U
P=q(F(151,100))
D1=q(F(6))
D2=q(F(10))
r0=P**29/math.factorial(29)
r1=P**28/math.factorial(28)*D1
r2=P**27/math.factorial(27)*D1**2+P**28/math.factorial(28)*D2
rem=[(q(ws)+1)*q(U)*r0,(q(ws)+1)*(r0+q(U)*r1),(q(ws)+1)*(2*r1+q(U)*r2)]
rows=[]
gaps={}
for part,phi in [(0,[F(0),F(0),3*peak_s,-2*peak_s]),(2,[peak_s,F(0),-eps_s])]:
    assert 0<eps_s<peak_s<F(151,100)
    for kind in ['sin','cos']:
        poly=exact_trig_poly(phi,kind,degree)
        coeff=[v*moments[j]for j,v in enumerate(poly)]
        jet=[]
        exact_sums=[]
        for r in range(3):
            total=F(0)
            for j,c in enumerate(coeff):
                if j+1>=r:
                    factor=math.prod(range(j+2-r,j+2))if r else 1
                    total+=abs(c)*factor*U**(j+1-r)
            exact_sums.append(total)
            jet.append(q(total)+rem[r])
        gaps[(part,kind)]=jet
        rows.append(dict(part=part,trig=kind,polynomial_degree=len(poly)-1,
          normalized_primitive_jet_bounds=[upper_bound(v)for v in jet],
          polynomial_moment_jet_bounds=[upper_bound(q(v))for v in exact_sums]))
# The reference is exactly R59: same literal cut, true elementary operations,
# curvature 4 and rational peak fraction 1/5.
R,w,wr=[q(F.from_float(float(cut[k])))for k in('radius','backgroundSlope','backgroundSecond')]
pt=iv.atan2(iv.mpf(1),w)
peak=pt+(iv.pi/2-pt)/5
eps=peak-pt
ps=wr/((1+w*w)*iv.sqrt(1+w*w))
L1=3*peak/8
L3=2*eps/(-ps)
assert 0<lower(peak)<upper(peak)<1.51
# Taylor remainder over [0,1] uses the same conservative 1.51 radius.
refs={}
for part,phi in [(0,[iv0(),iv0(),3*peak,-2*peak]),(2,[peak,iv0(),-eps])]:
    for kind in ['sin','cos']:
        poly=trig_poly(phi,kind,degree)
        integ=sum((v/(j+1)for j,v in enumerate(poly)),iv0())
        refs[(part,kind)]=integ+enclose_error(r0)
L2=(1-R-L1*refs[(0,'sin')]-L3*refs[(2,'sin')])/iv.sin(peak)
Lref=L1+L2+L3
c=q(Ls)/Lref
assert lower(L2)>0 and lower(c)>0
cp=max(abs(lower(c-1)),abs(upper(c-1)))
du=upper(Lref*iv.mpf(mag(c/q(L1s)-1/L1)))
dv=upper(Lref*iv.mpf(mag(c/q(L3s)-1/L3))+iv.mpf(mag(q(L1s+L2s)/q(L3s)-(L1+L2)/L3)))
angle=q(F.from_float(0.0))+mag(q(peak_s)-peak)+q(U)**2*mag(q(eps_s)-eps)
angle+=q(peak_s)*q(F(3,2))*du+2*q(eps_s)*q(U)*dv
Dangle=iv.mpf(mag(c*q(peak_s)/q(L1s)-peak/L1))*q(F(3,2))
Dangle+=(peak/L1)*6*du
Dangle+=(2*eps/L3)*dv+q(U)*mag(c*2*q(eps_s)/q(L3s)-2*eps/L3)
# The first source turn has maximum phase speed 4; the terminal speed <2.
assert upper(-ps)<2
physical={}
pulled={}
plateau_errors={}
repair={}
for kind in ['sin','cos']:
    exact_value=getattr(iv,kind)(q(peak_s))
    literal_value=F.from_float(getattr(math,kind)(b.peak))
    plateau_error=iv.mpf(mag(q(literal_value)-exact_value))
    plateau_errors[kind]=upper_bound(plateau_error)
    E0=q(L1s)*gaps[(0,kind)][0]+q(L3s)*gaps[(2,kind)][0]+q(L2s)*plateau_error
    E1=iv.mpf(max(upper(gaps[(0,kind)][1]),upper(gaps[(2,kind)][1]),upper(plateau_error)))
    E2=iv.mpf(max(upper(gaps[(0,kind)][2]/q(L1s)),upper(gaps[(2,kind)][2]/q(L3s))))
    physical[kind]=[upper_bound(x)for x in(E0,E1,E2)]
    # Absolute primitives start at the same zero; piecewise C1 is sufficient
    # for this first-derivative integration bound, but exact C2 is not claimed.
    d1=angle+cp+c*E1
    d0=Lref*d1
    d2=c*Dangle+(angle+cp)*4+c*c*E2
    pulled[kind]=[upper_bound(x)for x in(d0,d1,d2)]
    rr=[]
    for part,length,original_length in [(0,L1s,L1s),(2,Ls-L1s-L2s,L3s)]:
        ell=q(length)
        e1=gaps[(part,kind)][1]+plateau_error
        e2=gaps[(part,kind)][2]/q(original_length)
        hh=[ell*e1*q(F(4,5))+ell*ell*e2/10,
            4*e1+ell*e2/2,24*e1/ell+4*e2]
        rr.append(dict(part=part,physical_length_exact=str(length),jet_bounds=[upper_bound(x)for x in hh]))
    repair[kind]=rr
overrun=max(F(0),Ls-L1s-L2s-L3s)
vextra=q(overrun/L3s)
clip_phase_gap=q(eps_s)*(2*vextra+vextra*vextra)
clip_phase_derivative_gap=2*q(eps_s)*vextra/q(L3s)
clip_oracle_first_gap=clip_phase_gap
clip_oracle_second_gap=clip_phase_gap*2*q(eps_s)/q(L3s)+clip_phase_derivative_gap
clip_radius_gap=q(overrun)*(1+gaps[(2,'sin')][1])
radius_primitive_gap=q(F(physical['sin'][0]['upper_exact']))+clip_radius_gap
true_radius_lower=R-q(F(pulled['sin'][0]['upper_exact']))-q(F(physical['sin'][0]['upper_exact']))
assert lower(true_radius_lower)>mp.mpf(299)/1000
relative_radius=radius_primitive_gap/q(F(299,1000))
metric_radius_gap=2*relative_radius+relative_radius**2
raw_node_text=json.dumps(dict(node=[str(t)for t in node],weight=[str(w)for w in weight]),sort_keys=True,separators=(',',':'))
out=dict(scope=__doc__,status='exact_moment_and_true_parameter_bounds_passed',
 source_sha256=hashlib.sha256(a.source.read_bytes()).hexdigest(),
 certificate_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 run_sha256=hashlib.sha256(run_bytes).hexdigest(),
 rule=dict(nodes=64,binary_node_weight_sha256=hashlib.sha256(raw_node_text.encode()).hexdigest(),sum_weights=str(ws),maximum_moment_abs=upper_bound(q(max(abs(v)for v in moments))),moments_through=3*degree),
 source_parameters={k:repr(getattr(b,k))for k in('peak','eps','L1','L2','L3','L')},
 source_endpoints=dict(prefix_end=repr(a.prefix_end),end=repr(a.end),exact_span=str(Ls),span_minus_bridge_L=str(Ls-F.from_float(b.L))),
 normalized_analytic_domain_upper_exact=str(U),
 terminal_phase_interpretation='Analytic p-eps*u^2 continuation through the actual end; no upper clipping. This is an explicitly declared new continuous representation.',
 exact_terminal_span_overrun=str(overrun),
 true_reference_parameters={k:bounds(v)for k,v in [('peak',peak),('eps',eps),('L1',L1),('L2',L2),('L3',L3),('L',Lref)]},
 source_minus_reference={k:bounds(q(v)-true)for k,v,true in [('peak',peak_s,peak),('eps',eps_s,eps),('L1',L1s,L1),('L2',L2s,L2),('L3',L3s,L3),('L',Ls,Lref)]},
 endpoint_pullback_scale= bounds(c),
 endpoint_pullback_scale_minus_one=bounds(c-1),
 phase_gap=upper_bound(angle),phase_derivative_gap=upper_bound(Dangle),
 same_literal_parameters_primitive_physical_jet_bounds=physical,
 frozen_plateau_trig_constant_errors=plateau_errors,
 endpoint_pulled_primitive_vs_R59_piecewise_jet_bounds=pulled,
 available_shared_jet_quintic_repair_bounds=repair,
 shared_jet_repair_applied_to_live_map=False,
 clipped_source_radius_vs_analytic_GL_value_gap=upper_bound(clip_radius_gap),
 clipped_source_hand_geo_jet_vs_analytic_phase_gaps=[upper_bound(clip_oracle_first_gap),upper_bound(clip_oracle_second_gap)],
 clipped_source_radius_vs_true_primitive_gap=upper_bound(radius_primitive_gap),
 true_primitive_radius_lower=bounds(true_radius_lower),
 radius_only_relative_metric_transfer_bound=upper_bound(metric_radius_gap),
 radius_only_relative_metric_transfer_scope='Same physical s and material angle, radial coefficient one, radius denominator >=.299; changes only the radius coefficient. Not equality of g and not a full map certificate.',
 normalized_rules=rows,
 literal_formal_primitive_global_C2_certified=False,
 libm_evaluation_roundoff_certified=False,
 current_nonrotating_field_geometry_certified=False,
 exact_parameter_and_moment_arithmetic=True,interval_digits=iv.dps)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in('status','source_parameters','endpoint_pullback_scale_minus_one','phase_gap','phase_derivative_gap','same_literal_parameters_primitive_physical_jet_bounds','endpoint_pulled_primitive_vs_R59_piecewise_jet_bounds')}))

