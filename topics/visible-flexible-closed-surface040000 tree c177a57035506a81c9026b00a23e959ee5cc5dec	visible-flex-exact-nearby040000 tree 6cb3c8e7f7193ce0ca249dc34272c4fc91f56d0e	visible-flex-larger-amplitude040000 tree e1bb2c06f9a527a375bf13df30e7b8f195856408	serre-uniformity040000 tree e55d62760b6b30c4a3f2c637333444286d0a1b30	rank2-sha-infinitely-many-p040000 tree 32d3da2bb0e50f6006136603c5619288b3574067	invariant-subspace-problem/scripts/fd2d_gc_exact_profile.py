#!/usr/bin/env python3
"""Accurate physical profile and C2 clock, reconstructed after executor reset.

Raw shared jets and design inputs are binary64 rationals. Derived phases,
lengths and radius integrals remain exact analytic quantities. The ramp
uses e=2/25, 1-e=23/25. Every saved binary x piece is calibrated to its
accurate physical length by a quintic with J=1,J_x=0 at both endpoints.
This defines a slightly different finite reconstructed X from the former
floating clock. No old body values are certified by this packet.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
from fd2d_frozen_ellipse_candidate import Candidate
from fd2d_gc_native_log_field import NativeLogField,identity,locate_near

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
DEFAULT_MOMENTS=ROOT/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json'
RAMP=Q(2,25);AREA=1-RAMP

def rational(value):
    if isinstance(value,Q):return value
    return Q(value) if isinstance(value,(int,str)) else Q(float(value))

def exact_binary(parts):
    sign,mantissa,exponent,_=map(int,parts)
    return (-1 if sign else 1)*Q(mantissa)*Q(2)**exponent

def endpoints(x):return tuple(exact_binary(v) for v in x._mpi_)

def I(value):
    if hasattr(value,'_mpi_'):return value
    value=rational(value);return mp.iv.mpf(value.numerator)/value.denominator

def interval(lo,hi):
    lo,hi=rational(lo),rational(hi)
    if lo>hi:raise ValueError('Reversed interval')
    return I((lo+hi)/2)+mp.iv.mpf([-1,1])*I((hi-lo)/2)

def from_record(row):return interval(exact_binary(row['binary_lower']),exact_binary(row['binary_upper']))

def upper_float(x):
    x=rational(x);v=float(x)
    return math.nextafter(v,math.inf) if Q(v)<x else v

def lower_float(x):
    x=rational(x);v=float(x)
    return math.nextafter(v,-math.inf) if Q(v)>x else v

def record(x):
    x=I(x);lo,hi=endpoints(x)
    return dict(binary_lower=list(x._mpi_[0]),binary_upper=list(x._mpi_[1]),midpoint=float((lo+hi)/2),width_upper=upper_float(hi-lo))

def magnitude(x):return max(map(abs,endpoints(I(x))))

def hull(values):
    bounds=[endpoints(I(v)) for v in values]
    return interval(min(x[0] for x in bounds),max(x[1] for x in bounds))

def add(a,b):
    c=[I(0) for _ in range(max(len(a),len(b)))]
    for j,v in enumerate(a):c[j]+=v
    for j,v in enumerate(b):c[j]+=v
    return c

def scale(a,q):return [v*I(q) for v in a]

def mul(a,b):
    c=[I(0) for _ in range(len(a)+len(b)-1)]
    for j,v in enumerate(a):
        for k,w in enumerate(b):c[j+k]+=v*w
    return c

def derivative(a,order=1):
    for _ in range(order):a=[j*a[j] for j in range(1,len(a))]
    return a or [I(0)]

def value(a,t):
    out=I(0)
    for v in reversed(a):out=out*I(t)+v
    return out

def affine(a,center,width):
    out=[I(0)]
    for v in reversed(a):out=mul(out,[I(center),I(width)]);out[0]+=v
    return out[:-1] if len(out)>len(a) else out

def bernstein_range(a):
    n=len(a)-1
    return hull([sum((I(Q(math.comb(j,k),math.comb(n,k)))*a[k] for k in range(j+1)),I(0)) for j in range(n+1)])

def hermite(L,j0,j1):
    L=I(L);j0,j1=[[I(v) for v in jet] for jet in (j0,j1)]
    c0,c1,c2=j0[0],L*j0[1],L*L*j0[2]/2
    d,v,acc=j1[0]-c0-c1-c2,L*j1[1]-c1-2*c2,L*L*j1[2]-2*c2
    return [c0,c1,c2,10*d-4*v+acc/2,-15*d+7*v-acc,6*d-3*v+acc/2]

def phase_branches(p):
    p0,d=p['p0'],p['p1']-p['p0'];kind=p['kind']
    if kind=='turn':
        e=RAMP;left=[I(0),I(0),I(0),I(1/e**2),I(-1/(2*e**3))]
        middle=[I(-e/2),I(1)];right=[I(1-e)]
        for n,factor in ((3,-1/e**2),(4,1/(2*e**3))):
            right=add(right,[I(factor*math.comb(n,j)*(-1)**j) for j in range(n+1)])
        out=[]
        for lo,hi,c in ((Q(),e,left),(e,1-e,middle),(1-e,Q(1),right)):
            phi=scale(c,d/I(AREA));phi[0]+=p0;out.append((lo,hi,phi))
        return out
    if kind=='brake':return [(Q(),Q(1),[p0,I(0),d])]
    if kind=='phase_bridge':
        q0,q1=p['L']*p['ps0'],p['L']*p['ps1']
        return [(Q(),Q(1),[p0,q0,3*d-2*q0-q1,-2*d+q0+q1])]
    return [(Q(),Q(1),[p0])]

def trig_taylor(phi,lo,hi,order):
    center,width=(lo+hi)/2,(hi-lo)/2;shifted=affine(phi,center,width)
    constant=shifted[0];delta=list(shifted);delta[0]=I(0)
    radius=sum(map(magnitude,delta[1:]),Q())
    s,c=mp.iv.sin(constant),mp.iv.cos(constant)
    sine,cosine,power=[I(0)],[I(0)],[I(1)]
    sc,cc=(s,c,-s,-c),(c,-s,-c,s)
    for k in range(order+1):
        sine=add(sine,scale(power,sc[k%4]/math.factorial(k)))
        cosine=add(cosine,scale(power,cc[k%4]/math.factorial(k)))
        if k!=order:power=mul(power,delta)
    remainder=radius**(order+1)/math.factorial(order+1)
    integral=I(width)*sum((I(Q(2,j+1))*sine[j] for j in range(0,len(sine),2)),I(0))
    integral+=interval(-1,1)*I((hi-lo)*remainder)
    primitive=[I(0)]+[I(width)*v/(j+1) for j,v in enumerate(sine)]
    primitive[0]-=value(primitive,-1)
    return dict(lo=lo,hi=hi,phi=phi,sine=sine,cosine=cosine,primitive=primitive,
        delta_radius=radius,remainder=remainder,normalized_integral=integral)

def strict_asin(v):return mp.iv.atan2(v,mp.iv.sqrt(1-v*v))
def step(t):return t**3*(10+t*(-15+6*t))

def root_bracket(L,h,target,iterations=112):
    lo,hi=Q(),Q(1)
    for _ in range(iterations):
        mid=(lo+hi)/2;f=I(h*mid)+(L-I(h))*I(step(mid))-L*I(target)
        a,b=endpoints(f)
        if b<0:lo=mid
        elif a>0:hi=mid
        else:break
    return lo,hi

def structural_joins(bundle):
    raw=bundle['segments'];out=[]
    for j in range(1,len(raw)):
        before,after=raw[j-1],raw[j]
        if before['kind']==after['kind']=='hermite':
            ok=before['jet1']==after['jet0'];reason='identical shared raw endpoint jets'
        elif j==1 and before['kind']=='coast' and after['kind']=='hermite':
            ok=before['p0']==0 and after['jet0']==[0.,0.,0.];reason='exact central cylinder and zero initial offset/speed/acceleration'
        elif before['kind']=='hermite' and after['kind']=='turn':
            ok=before['jet1'][2]==0 and bool(after.get('start_from_previous'));reason='shared radius, exact asin of shared speed, zero ramp acceleration'
        elif before['kind'] in ('turn','coast','coast_to') and after['kind'] in ('turn','coast','coast_to','brake'):
            ok=bool(after.get('start_from_previous'));reason='shared radius and phase, both endpoint accelerations zero'
        else:raise ValueError(f'Analytic join not established at {j}')
        if not ok:raise ValueError(f'Failed shared physical jet identity at {j}')
        out.append(dict(left=j-1,right=j,identity=reason))
    return out

def resolve(bundle,T,a0,order):
    raw=copy.deepcopy(bundle['segments']);shallow=[j for j,p in enumerate(raw) if p.get('label')=='partial_return_matching_coast']
    if len(shallow)!=1:raise ValueError('Expected one identified shallow physical coast')
    raw[shallow[0]]['L']=T;resolved=[];pv,pa,pp=I(0),I(0),I(0)
    for j,source in enumerate(raw):
        p=dict(index=j,kind=source['kind'],label=source.get('label',''))
        for key in ('L','p0','p1','ps0','ps1','K'):
            if key in source:p[key]=I(source[key])
        if p['kind']=='hermite':
            if 'jet0' not in source:raise ValueError('Shared Hermite jets required')
            p['radius_coefficients']=hermite(p['L'],source['jet0'],source['jet1']);p['radius_coefficients'][0]+=a0
            pv,pa,pp=I(source['jet1'][1]),I(source['jet1'][2]),None
        else:
            if source.get('start_from_previous'):p['p0']=strict_asin(pv) if pp is None else pp
            if 'end_phase_add' in source:p['p1']=p['p0']+I(source['end_phase_add'])
            if 'end_radial_speed' in source:p['p1']=strict_asin(I(source['end_radial_speed']))
            if source.get('start_second_from_previous'):p['ps0']=pa/mp.iv.cos(p['p0'])
            if p['kind'] in ('coast','coast_to'):p['p1']=p['p0']
            if source.get('length_from_turn_rate'):p['L']=abs(p['p1']-p['p0'])/(p['K']*I(AREA))
            if source.get('end_from_cut'):
                cut=bundle['cut_reference'];w,wr=I(cut['w']),I(cut['wr'])
                p['p1']=-mp.iv.atan2(I(1),w);ps=-wr/((1+w*w)*mp.iv.sqrt(1+w*w))
                p['L']=2*(p['p1']-p['p0'])/ps
            pp,pv=p['p1'],mp.iv.sin(p['p1'])
            if p['kind']=='brake':pa=mp.iv.cos(pp)*2*(p['p1']-p['p0'])/p['L']
            elif p['kind']=='phase_bridge':pa=mp.iv.cos(pp)*p['ps1']
            else:pa=I(0)
            p['branches']=[trig_taylor(phi,lo,hi,order) for lo,hi,phi in phase_branches(p)]
            p['normalized_integral']=sum((b['normalized_integral'] for b in p['branches']),I(0))
        resolved.append(p)
    s,radius=I(0),a0
    for j,p in enumerate(resolved):
        source=raw[j];p['s0'],p['a_start']=s,radius
        if p['kind']=='coast_to':
            if 'radius_after_next' in source:
                following=resolved[j+1];target=I(source['radius_after_next'])-following['L']*following['normalized_integral']
            else:target=I(source['radius_end'])
            p['L']=(target-radius)/mp.iv.sin(p['p0']);radius=target
        elif p['kind']=='hermite':radius=a0+I(source['jet1'][0])
        else:radius+=p['L']*p['normalized_integral']
        if endpoints(p['L'])[0]<=0:raise ValueError('Physical length is not proved positive')
        p['s1'],p['a_end']=s+p['L'],radius;s=p['s1']
        if p['kind']!='hermite':
            running=p['a_start']
            for b in p['branches']:
                b['radius_polynomial']=scale(b['primitive'],p['L']);b['radius_polynomial'][0]+=running
                b['radius_remainder']=magnitude(p['L'])*(b['hi']-b['lo'])*b['remainder']
                running+=p['L']*b['normalized_integral']
    return resolved

def packet_piece(p,x0,x1,old,reference,order):
    h=x1-x0;L=p['L'];rlo,rhi=endpoints(L/I(h)-1)
    Jlo,Jhi=1+Q(15,8)*min(Q(),rlo),1+Q(15,8)*max(Q(),rhi)
    if Jlo<=0:raise ValueError('Exact clock is not proved monotone')
    out=dict(index=p['index'],kind=p['kind'],label=p['label'],x_left_exact=str(x0),x_right_exact=str(x1),x_width_exact=str(h),
        physical_length=record(L),physical_s_left=record(p['s0']),physical_s_right=record(p['s1']),
        radius_left=record(p['a_start']),radius_right=record(p['a_end']),J_range=record(interval(Jlo,Jhi)),
        calibration=dict(local_s_polynomial_in_t=[record(v) for v in (I(0),I(h),I(0),10*(L-I(h)),-15*(L-I(h)),6*(L-I(h)))],
            exact_endpoint_J=1,exact_endpoint_J_x=0,same_physical_metric=True),
        old_resolved_float_comparison=dict(length_difference=record(L-I(old['L'])),
            reference_binary_width_minus_old_stored_length_exact=str(h-Q(float(reference['L']))),
            radius_left_difference=record(p['a_start']-I(old['a_start'])),
            note='Scalar coefficient comparison only; old floating body readings have not been transferred.'))
    if p['kind']=='hermite':
        c=p['radius_coefficients'];ap=scale(derivative(c),1/L);app=scale(derivative(c,2),1/(L*L))
        out['radius_polynomial_in_physical_tau']=[record(v) for v in c]
        out['physical_jet_bounds']=dict(a=record(bernstein_range(c)),a_s=record(bernstein_range(ap)),a_ss=record(bernstein_range(app)))
        return out
    out.update(phase_left=record(p['p0']),phase_right=record(p['p1']),branches=[])
    all_a,all_ap,all_app=[],[],[]
    for b in p['branches']:
        lo,hi=b['lo'],b['hi'];phi_bound=bernstein_range(affine(b['phi'],lo,hi-lo))
        ps_bound=bernstein_range(affine(scale(derivative(b['phi']),1/L),lo,hi-lo))
        arange=bernstein_range(affine(b['radius_polynomial'],-1,2))+interval(-1,1)*I(b['radius_remainder'])
        aprange,apprange=mp.iv.sin(phi_bound),mp.iv.cos(phi_bound)*ps_bound
        all_a.append(arange);all_ap.append(aprange);all_app.append(apprange);cuts=[]
        for target in (lo,hi):
            if target==0:lower=upper=Q()
            elif target==1:lower=upper=Q(1)
            else:lower,upper=root_bracket(L,h,target)
            cuts.append(dict(physical_tau_exact=str(target),clock_t_lower_exact=str(lower),clock_t_upper_exact=str(upper),
                             x_lower_exact=str(x0+h*lower),x_upper_exact=str(x0+h*upper)))
        out['branches'].append(dict(physical_tau_interval_exact=[str(lo),str(hi)],variable='y=(2*tau-lo-hi)/(hi-lo), -1 <= y <= 1',
            phase_polynomial_in_physical_tau=[record(v) for v in b['phi']],
            phase_polynomial_in_y=[record(v) for v in affine(b['phi'],(lo+hi)/2,(hi-lo)/2)],
            sine_polynomial_in_y=[record(v) for v in b['sine']],cosine_polynomial_in_y=[record(v) for v in b['cosine']],
            radius_polynomial_in_y=[record(v) for v in b['radius_polynomial']],trig_taylor_order=order,
            delta_phase_radius_upper_exact=str(b['delta_radius']),sine_cosine_uniform_remainder_upper_exact=str(b['remainder']),
            radius_uniform_remainder_upper_exact=str(b['radius_remainder']),normalized_sine_integral=record(b['normalized_integral']),
            physical_jet_bounds=dict(a=record(arange),a_s=record(aprange),a_ss=record(apprange)),branch_x_cuts=cuts))
    out['physical_jet_bounds']=dict(a=record(hull(all_a)),a_s=record(hull(all_ap)),a_ss=record(hull(all_app)))
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True);parser.add_argument('--moments',type=Path,default=DEFAULT_MOMENTS)
    parser.add_argument('--precision',type=int,default=70);parser.add_argument('--order',type=int,default=24)
    parser.add_argument('--packet',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.packet.exists() or args.out.exists():raise FileExistsError('Use a new actual run name')
    if args.packet.suffix!='.gz':raise ValueError('Coefficient packet must be compressed')
    started=time.monotonic();mp.iv.dps=args.precision;native=NativeLogField(args.field)
    target=locate_near(args.field,native.meta['target_input']);bundle=json.loads(target.read_text())
    if bundle['ellipse']!={'A':1.4,'B':.5}:raise ValueError('Original rational 7/5 by 1/2 ellipse required')
    if identity(args.moments)['sha256']!=native.meta['initial_geometry']['exact_moments']['sha256']:raise ValueError('Exact a0 input changed')
    moments=json.loads(args.moments.read_text());a0=from_record(moments['enclosures']['a0']);joins=structural_joins(bundle)
    shallow=[j for j,p in enumerate(bundle['segments']) if p.get('label')=='partial_return_matching_coast'][0]
    reference=copy.deepcopy(bundle);reference['segments'][shallow]['L']=native.meta['radial_chart']['reference_T']
    current=copy.deepcopy(bundle);current['segments'][shallow]['L']=native.meta['actual_T']
    ref,old=Candidate(reference),Candidate(current)
    if len(ref.segments)!=len(bundle['segments']) or len(old.segments)!=len(bundle['segments']):raise ValueError('All reference pieces must have positive lengths')
    x=[Q(float(v)) for v in ref.breaks];nodes={Q(float(v)) for v in native.nodes}
    if not set(x).issubset(nodes):raise ValueError('Reference x endpoints are not all saved native nodes')
    if [str(x[0]),str(x[-1])]!=native.meta['radial_domain_exact']:raise ValueError('Native x interval changed')
    pieces=resolve(bundle,native.meta['actual_T'],a0,args.order)
    stored=[packet_piece(p,a,b,o,r,args.order) for p,a,b,o,r in zip(pieces,x[:-1],x[1:],old.segments,ref.segments)]
    arange=hull([from_record(p['physical_jet_bounds']['a']) for p in stored])
    aprange=hull([from_record(p['physical_jet_bounds']['a_s']) for p in stored])
    apprange=hull([from_record(p['physical_jet_bounds']['a_ss']) for p in stored])
    Jrange=hull([from_record(p['J_range']) for p in stored]);v2lo=1-magnitude(aprange)**2
    if endpoints(arange)[0]<=0 or v2lo<=0:raise ValueError('Global positive physical normalization not proved')
    cut=bundle['cut_reference'];w,wr=I(cut['w']),I(cut['wr'])
    cutjet=dict(a=record(I(cut['r'])),a_s=record(-1/mp.iv.sqrt(1+w*w)),a_ss=record(-w*wr/(1+w*w)**2))
    packet=dict(schema='fd2d-exact-physical-profile-calibrated-clock-v1',source=identity(__file__),native_field=identity(args.field),
        target_input=identity(target),exact_moments=identity(args.moments),exact_a0=record(a0),
        actual_T_exact=str(Q(float(native.meta['actual_T']))),reference_T_binary_exact=str(Q(float(native.meta['radial_chart']['reference_T']))),
        reference_x_generator=identity(HERE/'fd2d_frozen_ellipse_candidate.py'),
        scalar_input_convention='raw parsed binary64 scalars are exact rationals; a0 and derived phases/lengths/radii remain exact analytic quantities',
        analytic_ramp_constants=dict(edge_exact=str(RAMP),area_exact=str(AREA),half_edge_exact=str(RAMP/2)),
        exact_physical_definition='shared endpoint Hermite jets, derived phases and exact phase sine integrals; compensated final coast fixes cut jets',
        exact_clock_definition='S=s_left+h*t+(L-h)*(10*t^3-15*t^4+6*t^5) on every recorded binary x piece',
        physical_angular_chart=native.meta['angular_chart'],new_finite_reconstructed_map=True,
        old_floating_body_readings_are_not_bounds_for_this_map=True,old_field_arrays_and_manifest_unchanged=True,
        physical_metric_changed_by_clock_calibration=False,physical_profile_C2_by_shared_definition=True,
        clock_C2_by_exact_endpoint_jets=True,complete=True,all_physical_pieces_covered=True,
        radial_domain_exact=[str(x[0]),str(x[-1])],physical_endpoint=record(pieces[-1]['s1']),structural_join_identities=joins,
        global_profile_bounds=dict(a=record(arange),a_s=record(aprange),a_ss=record(apprange),one_minus_a_s_squared_lower_exact=str(v2lo),J=record(Jrange)),
        exact_cut_jet=cutjet,precision_decimal=args.precision,trig_taylor_order=args.order,pieces=stored,
        reconstructed_after_executor_reset=True,no_continuous_Codazzi_metric_or_seam_certificate_claimed=True)
    raw=(json.dumps(packet,separators=(',',':'),allow_nan=False)+'\n').encode();args.packet.write_bytes(gzip.compress(raw,mtime=0))
    widths=[endpoints(p['L'])[1]-endpoints(p['L'])[0] for p in pieces]
    length_change=max(magnitude(from_record(p['old_resolved_float_comparison']['length_difference'])) for p in stored)
    xchange=max(abs(Q(p['old_resolved_float_comparison']['reference_binary_width_minus_old_stored_length_exact'])) for p in stored)
    internal=[b['branch_x_cuts'][1] for p in stored for b in p.get('branches',[]) if b['physical_tau_interval_exact'][1]!='1']
    report=dict(schema='fd2d-exact-physical-profile-calibrated-clock-summary-v1',source=identity(__file__),packet=identity(args.packet),
        raw_packet_sha256=hashlib.sha256(raw).hexdigest(),raw_packet_bytes=len(raw),field=identity(args.field),target=identity(target),exact_moments=identity(args.moments),
        pieces=len(pieces),shared_physical_C2_joins=len(joins),complete=True,all_reference_x_boundaries_are_actual_field_nodes=True,
        maximum_physical_length_interval_width_upper=upper_float(max(widths)),maximum_length_difference_from_old_float_upper=upper_float(length_change),
        maximum_reference_binary_width_minus_old_length_upper=upper_float(xchange),global_profile_bounds=packet['global_profile_bounds'],
        physical_endpoint=packet['physical_endpoint'],exact_cut_jet=cutjet,internal_phase_x_cut_enclosures=internal,
        new_finite_reconstructed_map=True,old_body_results_transfer_not_claimed=True,accurate_constants_are_not_redefined_as_midpoints=True,
        no_fixed_metric_or_physical_target_changed_by_clock_calibration=True,reconstructed_after_executor_reset=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(pieces=len(pieces),a_lower=lower_float(endpoints(arange)[0]),abs_a_s_upper=upper_float(magnitude(aprange)),
        abs_a_ss_upper=upper_float(magnitude(apprange)),J_lower=lower_float(endpoints(Jrange)[0]),J_upper=upper_float(endpoints(Jrange)[1]),
        physical_endpoint=record(pieces[-1]['s1']),maximum_length_interval_width_upper=upper_float(max(widths)),
        maximum_length_difference_from_old_float_upper=upper_float(length_change),raw_packet_bytes=len(raw),packet_bytes=args.packet.stat().st_size,
        seconds=report['seconds'])),flush=True)

if __name__=='__main__':main()
