#!/usr/bin/env python3
"""R181: two explicit shorter NEW physical R136 scalar metrics.

Primary B retains the exact .8 cut and the current flat-tail family, removes
the outward spacer, and changes only the redeepen turn rate to 9/2.
Secondary A removes the spacer, keeps that turn rate, and uses cut 23/32.
Exact Fraction enclosures prove positive derived coasts and bound the
rotational height; only the existing scalar reader is evaluated numerically.
No saved nonround field, atlas, lifting, bumps, F/J or BVP is transferred.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import time

from fd2d_flat_cut_prefix_candidate import FlatCutCandidate


ROOT = Path(__file__).resolve().parent.parent
PARENT = ROOT / 'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json'
PARENT_SHA = '7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1'
OLD_DEEP = (Q(439,100000), Q(2803,500000))
FAMILIES = {
    'B_standard_cut': dict(cut=Q(4,5), new_rate=Q(9,2), safe_T=Q(1,40)),
    'A_cut23over32': dict(cut=Q(23,32), new_rate=None, safe_T=Q(1,10)),
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_float(x):
    return Q.from_float(float(x))


def record(x):
    x=Q(x)
    return dict(exact=str(x), approximate=float(x))


def interval_record(pair):
    return [record(x) for x in pair]


def add(x,y):
    return x[0]+y[0],x[1]+y[1]


def mul(x,y):
    values=[a*b for a in x for b in y]
    return min(values),max(values)


def div(x,y):
    if y[0]<=0:
        raise ValueError('Positive denominator interval required')
    values=[a/b for a in x for b in y]
    return min(values),max(values)


def scale(x,c):
    return mul(x,(c,c))


def trig_interval(x,kind):
    """Exact alternating Taylor bounds, 0<=x<=3/2; no float trig."""
    x=Q(x)
    if not 0<=x<=Q(3,2):
        raise ValueError('Outside the proved monotone trigonometric range')
    offset=1 if kind=='sin' else 0
    partial=Q(0)
    upper=None
    for j in range(10):
        partial+=(-1)**j*x**(2*j+offset)/factorial(2*j+offset)
        if j==8:
            upper=partial
    lower=partial
    assert lower<=upper
    return lower,upper


def soft_turn_integrals(m,pd,K,subdivisions=32):
    """Enclose positive sin/cos integrals of the old normalized soft turn.

    The middle phase has speed K and is integrated exactly by its primitive.
    Each end ramp is split into fixed rational boxes, using monotonic phase
    and exact alternating Taylor sine/cosine enclosures at the endpoints.
    """
    d=pd-m
    if not 0<m<pd<Q(3,2) or K<=0:
        raise ValueError('Expected the retained positive absolute phases')
    ramp_time=2*d/(23*K)
    left_phase=m+d/23
    right_phase=pd-d/23
    cs_left=trig_interval(left_phase,'cos')
    cs_right=trig_interval(right_phase,'cos')
    sn_left=trig_interval(left_phase,'sin')
    sn_right=trig_interval(right_phase,'sin')
    radial=((cs_left[0]-cs_right[1])/K,(cs_left[1]-cs_right[0])/K)
    height=((sn_right[0]-sn_left[1])/K,(sn_right[1]-sn_left[0])/K)
    for side in ('left','right'):
        def phase(t):
            if side=='left':
                return m+2*d*(t**3-t**4/2)/23
            v=1-t
            return pd-2*d*(v**3-v**4/2)/23
        for i in range(subdivisions):
            plo,phi=phase(Q(i,subdivisions)),phase(Q(i+1,subdivisions))
            assert m<=plo<=phi<=pd
            slo,shi=trig_interval(plo,'sin'),trig_interval(phi,'sin')
            clo,chi=trig_interval(plo,'cos'),trig_interval(phi,'cos')
            dt=ramp_time/subdivisions
            radial=add(radial,(dt*slo[0],dt*shi[1]))
            height=add(height,(dt*chi[0],dt*clo[1]))
    assert radial[0]>0 and height[0]>0
    return dict(radial_magnitude=radial,height=height,ramp_time=ramp_time,
                full_length=(pd-m)/(Q(23,25)*K),subdivisions_per_ramp=subdivisions)


def parent_parameters(source):
    rows={p.get('label'):p for p in source['segments'] if p.get('label')!='frozen_feedback_prefix'}
    feedback=[p for p in source['segments'] if p.get('label')=='frozen_feedback_prefix']
    assert feedback[-1]['jet1'][2]==0
    E=exact_float(rows['outward_peak_spacer']['L'])
    v=exact_float(feedback[-1]['jet1'][1])
    rate=exact_float(rows['redeepen_after_partial_return']['K'])
    m=-exact_float(rows['partial_return_matching_coast']['p0'])
    pd=-exact_float(rows['redeepen_after_partial_return']['p1'])
    T0=exact_float(rows['partial_return_matching_coast']['L'])
    Lfeedback=sum((exact_float(p['L']) for p in feedback),Q(0))
    Lcontraction=sum((exact_float(rows[k]['L']) for k in (
        'partial_return_acceleration_entry','partial_return_acceleration_plateau',
        'partial_return_acceleration_exit')),Q(0))
    early=rows['early_shallow_return']
    early_start=-exact_float(rows['partial_return_acceleration_exit']['p1'])
    Learly=abs(early_start-m)/(Q(23,25)*exact_float(early['K']))
    Lbrake=exact_float(rows['cut_second_jet_brake']['L'])
    assert 0<v<Q(13,50)
    assert 1-v*v>Q(193,200)**2
    assert trig_interval(Q(3,10),'sin')[0]>v
    assert max(early_start,m)<Q(121,1000)
    return dict(E=E,v=v,rate=rate,m=m,pd=pd,T0=T0,
        Lfeedback=Lfeedback,Lcontraction=Lcontraction,Learly=Learly,Lbrake=Lbrake,
        feedback_count=len(feedback))


def exact_family_certificate(source,family):
    p=parent_parameters(source)
    config=FAMILIES[family]
    rate=config['new_rate'] or p['rate']
    cut=config['cut']
    oldturn=soft_turn_integrals(p['m'],p['pd'],p['rate'])
    ratio=p['rate']/rate
    radial_gain=scale(oldturn['radial_magnitude'],1-ratio)
    constant=Q(4,5)-cut-p['E']*p['v']
    radial_change=add((constant,constant),radial_gain)
    sind=trig_interval(p['pd'],'sin')
    cosd=trig_interval(p['pd'],'cos')
    sinm=trig_interval(p['m'],'sin')
    cosm=trig_interval(p['m'],'cos')
    deep=add(OLD_DEEP,div(radial_change,sind))
    assert deep[0]>0, (family,'nonpositive exact derived coast lower bound')
    Tmax=add((p['T0'],p['T0']),div(mul(deep,sind),sinm))
    shift=config['safe_T']-p['T0']
    Lsafe=add(deep,scale(div(sinm,sind),-shift))
    assert Lsafe[0]>0 and Tmax[0]>config['safe_T']
    # R136 proves 0<=a_s<=v on the retained feedback and all unchanged
    # phase contraction pieces have |phase|<.3. No numerical grid is used.
    feedback_height=(p['Lfeedback']*Q(193,200),p['Lfeedback'])
    contraction_height=(p['Lcontraction']*trig_interval(Q(3,10),'cos')[0],p['Lcontraction'])
    early_height=(p['Learly']*trig_interval(Q(121,1000),'cos')[0],p['Learly'])
    shallow_height=scale(cosm,p['T0'])
    turn_height=scale(oldturn['height'],ratio)
    deep_height=mul(deep,cosd)
    brake_height=(Q(0),p['Lbrake']*cosd[1])
    height_without_cylinder=(Q(0),Q(0))
    pieces=dict(feedback=feedback_height,contraction=contraction_height,
                early_return=early_height,matching_coast=shallow_height,
                redeepen=turn_height,derived_deep_coast=deep_height,brake=brake_height)
    for value in pieces.values():
        height_without_cylinder=add(height_without_cylinder,value)
    height_T_derivative=add(cosm,scale(div(mul(cosd,sinm),sind),-1))
    assert 0<height_T_derivative[0]<=height_T_derivative[1]<1
    assert cut>=Q(7,10) and 1/cut<7 and rate<7
    return dict(parameters=p,cut=cut,rate=rate,old_turn=oldturn,
        radial_change=radial_change,deep=deep,Tmax=Tmax,L_at_safe_T=Lsafe,
        safe_T=config['safe_T'],height_without_cylinder=height_without_cylinder,
        height_pieces=pieces,height_T_derivative=height_T_derivative,
        tail_curvature=Q(315,128)*Q(6,5)/(cut-Q(17,50)),
        tail_normal_radius=Q(128,315)*(cut-Q(17,50))/Q(6,5),
        tail_depression=Q(3,5)*(cut-Q(17,50)))


def public_certificate(cert):
    out={k:record(cert[k]) for k in ('cut','rate','safe_T','tail_curvature','tail_normal_radius','tail_depression')}
    out.update({k:interval_record(cert[k]) for k in
        ('radial_change','deep','Tmax','L_at_safe_T','height_without_cylinder','height_T_derivative')})
    out['parameters']={k:(v if k=='feedback_count' else record(v)) for k,v in cert['parameters'].items()}
    out['height_pieces']={k:interval_record(v) for k,v in cert['height_pieces'].items()}
    out['old_turn']={k:(v if k=='subdivisions_per_ramp' else
        interval_record(v) if isinstance(v,tuple) else record(v)) for k,v in cert['old_turn'].items()}
    out.update(old_derived_coast_interval_from_R136=interval_record(OLD_DEEP),
        radius_continuous_lower=record(cert['cut']),
        round_reference_curvature_strict_upper=record(Q(7)),
        round_curvature_scope='R166 unchanged feedback/bridge/brake bounds plus the explicit changed redeepen rate; not a nonround field curvature certificate',
        actual_nonround_Z_known=False,old_nonround_field_transferred=False,
        old_R139_coast_lifting_transferred=False)
    return out


def build(source,family,cylinder,cert):
    cylinder=Q(cylinder)
    if cylinder<=0:
        raise ValueError('Positive new central cylinder length required')
    rows=copy.deepcopy(source['segments'])
    rows=[p for p in rows if p.get('label')!='outward_peak_spacer']
    rows[0]['L']=float(cylinder)
    for row in rows:
        if row.get('label')=='redeepen_after_partial_return':
            row['K']=float(cert['rate'])
            row['L']=float((cert['parameters']['pd']-cert['parameters']['m'])/(Q(23,25)*cert['rate']))
        if row.get('label')=='final_deep_coast':
            row['radius_after_next']=float(cert['cut'])
            row['exact_radius_after_next']=str(cert['cut'])
    for old,new in zip(
            [p for p in source['segments'] if p.get('label')=='frozen_feedback_prefix'],
            [p for p in rows if p.get('label')=='frozen_feedback_prefix']):
        assert old==new
    cut=copy.deepcopy(source['cut']);cut['r']=float(cert['cut'])
    cut['exact_radius']=str(cert['cut'])
    cut['tail_definition']='R132 exact positive-function flat tail at the explicitly changed cut radius; all widths use this cut'
    cut['tail_bending_amplitude_interval']=[0.,1.2]
    bundle=dict(
        schema=source['schema'],ellipse=copy.deepcopy(source['ellipse']),
        exact_a0_definition=source['exact_a0_definition'],segments=rows,
        cut_reference=dict(r=float(cert['cut']),exact_radius=str(cert['cut']),w=0.,wr=0.,
                           meaning='Accurate flat endpoint; never divide by w or reference n'),
        cut=cut,
        exact_definition='R136 shared dyadic endpoint jets and unchanged phase rules; omit the outward spacer; replace only the redeepen rate when specified. New central length and cut radius have the explicit exact values below. The final coast is defined by exact phase integrals to reach the exact cut; numeric quadrature is an evaluation, not a second definition.',
        generated_by=Path(__file__).name,generator_sha256=digest(__file__),
        inputs=dict(parent_candidate=PARENT.name,parent_candidate_sha256=PARENT_SHA,
                    retained_feedback_and_other_phase_data_unchanged=True),
        shorter_design_definition=dict(family=family,cylinder_exact=str(cylinder),
            cut_radius_exact=str(cert['cut']),redeepen_rate_exact=str(cert['rate']),
            removed_outward_spacer=True,normalized_turn_integral='23/25',
            terminal_phase='-pi/2',matching_coast_exact=str(cert['parameters']['T0']),
            final_coast_definition='L_old(T0) + (4/5-r-E_old*v_star+(1-K_old/K_new)*M_old)/sin(p_deep), then subtract sin(p_match)/sin(p_deep)*(T-T0)',
            physical_metric_changed=True,same_central_a0=True,
            old_nonround_arrays_or_atlas_or_lifting_transferred=False),
        status=dict(metric_frozen=True,nonlinear_prefix_solved=False,
                    nonlinear_tail_matched=False,closed_nonround_surface=False,
                    reach_certified=False,strong_target_complete=False))
    return bundle


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent',type=Path,default=PARENT)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    if digest(args.parent)!=PARENT_SHA:
        raise ValueError('The proof is bound to the original immutable R136 candidate')
    stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh candidate/report stem')
    stem.parent.mkdir(parents=True,exist_ok=True)
    start=time.perf_counter();source=json.loads(args.parent.read_text())
    certs={k:exact_family_certificate(source,k) for k in FAMILIES}
    # These are two outer shapes with exact cylinder-length variants, not
    # five independently solved or scanned nonround candidate fields.
    selections=[
        ('B_standard_cut','cyl032',exact_float(source['segments'][0]['L']),'D4',(Q(229,250),Q(29,25))),
        ('B_standard_cut','cyl3over16',Q(3,16),'D35',(Q(393,500),Q(93,100))),
        ('B_standard_cut','cyl13over128',Q(13,128),'D32',(Q(18,25),Q(39,50))),
        ('A_cut23over32','cyl3over16',Q(3,16),'D35',(Q(393,500),Q(93,100))),
        ('A_cut23over32','cyl3over64',Q(3,64),'D32',(Q(18,25),Q(39,50))),
    ]
    results=[]
    for family,label,cylinder,cap,zwindow in selections:
        cert=certs[family]
        bundle=build(source,family,cylinder,cert)
        path=stem.with_name(stem.name+'-'+family+'-'+label+'-candidate.json')
        path.write_text(json.dumps(bundle,indent=2,allow_nan=False)+'\n')
        model=FlatCutCandidate(bundle)
        deep=next(p for p in model.segments if p.get('label')=='final_deep_coast')
        actualcut=[float(v[0]) for v in model.profile([model.end])]
        height=add(cert['height_without_cylinder'],(cylinder,cylinder))
        assert zwindow[0]<height[0]<height[1]<zwindow[1],(family,label,'background height bound outside selected window')
        assert min(p['L'] for p in model.segments)>0
        assert max(abs(actualcut[0]-float(cert['cut'])),abs(actualcut[1]+1),abs(actualcut[2]))<1e-13
        assert float(height[0])<=model.background_cut_height<=float(height[1])
        assert float(cert['deep'][0])<=deep['L']<=float(cert['deep'][1])
        results.append(dict(family=family,cylinder_label=label,cylinder_exact=str(cylinder),
            candidate_file=path.name,candidate_sha256=digest(path),cap_window_label=cap,
            background_height_exact_enclosure=interval_record(height),
            cap_actual_Z_window=interval_record(zwindow),
            numeric_rotational_height=model.background_cut_height,
            numeric_derived_deep_coast=deep['L'],numeric_meridian_length=model.end,
            numeric_cut_jet=actualcut,all_actual_reader_lengths_positive=True,
            scalar_reader='fd2d_flat_cut_prefix_candidate.FlatCutCandidate',
            old_nonround_field_transferred=False,actual_nonround_Z_known=False,
            all_other_complete_core_conditions_unpaid=True))
    report=dict(schema='fd2d-R181-shorter-physical-phase-and-cut-design-v1',theorem='R181',
        source_sha256=digest(__file__),parent_sha256=PARENT_SHA,
        dependency_sha256={p.name:digest(p) for p in [
            ROOT/'scripts/fd2d_flat_cut_prefix_candidate.py',
            ROOT/'scripts/fd2d_frozen_ellipse_candidate.py',
            ROOT/'results/R136-peak-spacer-prefix-continuous-radius-and-outer-design-domain.md',
            ROOT/'results/R166-exact-round-prefix-and-complete-increment-equations.md',
            ROOT/'results/R168-smaller-corner-caps-and-shorter-cylinder-window.md',
            ROOT/'results/R179-complete-caps-for-diameter-three-point-five-and-three-point-two.md']},
        exact_certificates={k:public_certificate(v) for k,v in certs.items()},
        candidates=results,body_or_BVP_runs=0,old_solver_or_field_mutations=0,
        strict_height_scope='Only the exact rotational reference height at the parent T0. The nonround matched cut Z remains unknown.',
        elapsed_seconds=time.perf_counter()-start)
    out=stem.with_name(stem.name+'-report.json');out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(out),passed=True,
        families={k:dict(deep=[float(x) for x in v['deep']],safe_T=float(v['safe_T']),
                        Tmax=[float(x) for x in v['Tmax']]) for k,v in certs.items()},
        candidates=[dict(file=x['candidate_file'],Z=x['numeric_rotational_height'],
            enclosure=[q['approximate'] for q in x['background_height_exact_enclosure']]) for x in results],
        elapsed_seconds=report['elapsed_seconds'])),flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
