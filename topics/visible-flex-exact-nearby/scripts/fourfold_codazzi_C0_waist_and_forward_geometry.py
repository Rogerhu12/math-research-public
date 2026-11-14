#!/usr/bin/env python3
"""Consume completed coefficients for the C0 waist and forward model.

The exact full-circle Green kernel gives a C0 waist witness, including
the unknown mean and every angular mode. Forward integration reuses the
complete local geometry gains without rerunning any primitive or ODE.
The canonical waist model remains distinct from the saved outer-anchor
model until their actual waist alignment error has been paid.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

RESPONSE='00efc0322a9aa82cd1f234899599ed3fbaff87edd35b8c9ac1331b229b276a55'
WAIST='2404a832efd9079b8f82c8c251904b6b776f02d7ebd131559b065b881a2e8b24'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'


def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==bytes((31,139)) else raw),hashlib.sha256(raw).hexdigest()


def hi(value):return box_from_record(value).upper()


def save(path,data):
    raw=(json.dumps(data,indent=2,allow_nan=False)+'\n').encode()
    if str(path).endswith('.gz'):raw=gzip.compress(raw,mtime=0)
    temporary=Path(str(path)+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--response',type=Path,default=Path('notes/2026-11-14-R133-complete-C0-state-nu-geometry-response-native.json.gz'))
    ap.add_argument('--waist',type=Path,default=Path('notes/2026-11-13-R133-waist-outward-tube-and-fifth-marker-rational.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256
    if args.out.exists():raise FileExistsError('preserve every actual complete forward geometry report')
    response,rh=load(args.response);waist,wh=load(args.waist)
    if (rh,wh)!=(RESPONSE,WAIST):raise ValueError('the complete original native identities differ')
    if not response['complete'] or not waist['all_gates_passed'] or response['candidate_sha256']!=waist['candidate_sha256']!=CANDIDATE:
        raise ValueError('the original candidate or a completed input is missing')
    if response['candidate_sha256']!=CANDIDATE or waist['candidate_sha256']!=CANDIDATE:
        raise ValueError('the same exact original final candidate is required')
    if (response['state_C0_radius'],response['nu_radius'],response['common_parameter_half_width'])!=('1/1000','1/100000','0'):
        raise ValueError('the common actual state/metric/affine scope differs')
    sqrt2=arb(2).sqrt()
    sec=(4-2*sqrt2).sqrt()
    slope=sqrt2-1
    witness=2*(sec-1)
    center=Fraction(waist['values']['exact_centre_waist_normal_displacement']['exact'])
    epsilon=Fraction(1,1000)
    fee=(witness*exact_arb(epsilon)).upper()
    lower=(exact_arb(center)-fee).lower();upper=(exact_arb(center)+fee).upper()
    ratio=(lower/exact_arb(Fraction(511,200))).lower()
    rows=[];cursor=Fraction(0);Ou,On,Pu,Pn,length=map(arb,(0,0,0,0,0))
    for source in response['rows']:
        left,right=map(Fraction,source['interval'])
        if left!=cursor or not left<right:raise ValueError('the true full cover has a gap or overlap')
        cursor=right;h=exact_arb(right-left);g={k:hi(z) for k,z in source['gains'].items()}
        L=g['reference_speed'];gu=g['connection_state_gain'];gn=g['connection_nu_gain']
        Pu=(Pu+h*L*Ou+h*h*L*gu/2+h*g['position_velocity_state_gain']).upper()
        Pn=(Pn+h*L*On+h*h*L*gn/2+h*g['position_velocity_nu_gain']).upper()
        Ou=(Ou+h*gu).upper();On=(On+h*gn).upper();length=(length+h*L).upper()
        rows.append(dict(interval=source['interval'],
            complete_forward_state_to_frame=record(Ou),complete_forward_nu_to_frame=record(On),
            complete_forward_state_to_position=record(Pu),complete_forward_nu_to_position=record(Pn),
            complete_forward_frame_anchor_to_position=record(length)))
    if cursor!=Fraction(25,8) or len(rows)!=7722:raise ValueError('the complete 7722-cell interval is required')
    gates=[dict(name=n,passed=bool(ok)) for n,ok in (
        ('complete original geometry and exact waist inputs retained',True),
        ('the complete canonical waist displacement operator gain is below the stated rational',witness<exact_arb(Fraction(164785,1000000))),
        ('complete waist position error includes its mean',sec<exact_arb(Fraction(1082393,1000000))),
        ('complete waist support derivative gain is bounded',slope<exact_arb(Fraction(414214,1000000))),
        ('the full C0 waist ball keeps the positive displacement witness',lower>0),
        ('the entire displacement is below the existing outward tube radius',upper<exact_arb(Fraction(27,196))),
        ('the conditional held ratio exceeds five percent',ratio>exact_arb(Fraction(1,20))),
        ('the complete forward interval has all original coefficient cells',cursor==Fraction(25,8) and len(rows)==7722),
        ('all new forward propagation coefficients are finite',all(x.is_finite() for x in (Ou,On,Pu,Pn,length))),
    )]
    bounds=dict(waist_C0_to_support=record(arb(1)),waist_C0_to_support_derivative=record(slope),
        waist_C0_to_planar_position=record(sec),waist_C0_to_normal_displacement=record(witness),
        exact_original_waist_displacement=str(center),state_C0_radius=str(epsilon),
        conditional_waist_displacement_lower=record(lower),conditional_waist_displacement_upper=record(upper),
        conditional_held_to_diameter_lower=record(ratio),
        forward_state_to_frame=record(Ou),forward_nu_to_frame=record(On),
        forward_radial_state_to_position=record(Pu),forward_nu_to_position=record(Pn),
        full_canonical_waist_state_to_position=record((sec+Pu).upper()),
        forward_frame_anchor_to_position=record(length))
    doc=dict(kind='complete_C0_waist_witness_and_canonical_forward_model_response_v1',
        complete=all(x['passed'] for x in gates),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256={str(args.response):rh,str(args.waist):wh},candidate_sha256=CANDIDATE,
        exact_interval=['0','25/8'],common_parameter_half_width='0',
        whole_unknown_angular_output_and_mean_retained=True,
        actual_nonlinear_solution_or_state_radius_proved=False,
        canonical_waist_model_is_not_saved_outer_anchor_model=True,
        original_outer_model_waist_alignment_error_still_required=True,
        original_GC_closure_and_flat_caps_not_granted=True,
        bounds=bounds,rows=rows,gates=gates,seconds=time.monotonic()-started)
    save(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(gates),bounds=bounds,seconds=doc['seconds'])))
    if not doc['complete']:raise RuntimeError('a necessary actual C0 waist budget failed')


if __name__=='__main__':main()
