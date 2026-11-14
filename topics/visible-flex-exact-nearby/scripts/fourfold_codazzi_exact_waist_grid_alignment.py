#!/usr/bin/env python3
"""Compare the saved whole waist grid with its exact canonical support curve.

This uses every exact angle pi*k/1024, the complete saved terminal frame,
the actual dyadic waist coefficients, the complete angular certificate,
and the original exact common height translation.  The missing radial
endpoint error is retained as an independent additive quantity.  No ODE
or primitive is rerun and no old floating point cloud becomes a surface.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
GEOMETRY='49870375c7397a53b867d67ce94aa8fcd2d86a69bfe7fc3a7f482b9232d30a2e'
CHAIN='4d87057a72944913d013636f57c1b90688a5df95264825f86241e47535e5ffa1'
ANGULAR='7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90'
WAIST='8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b'
ALPHA=Fraction(6890507429876859,9007199254740992)
HEIGHT=Fraction(4347844570122155,4503599627370496)
N=512


def digest(raw):return hashlib.sha256(raw).hexdigest()


def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==bytes((31,139)) else raw),digest(raw)


def ar(value):return exact_arb(Fraction(value))


def dyadic(value):return ar(Fraction.from_float(float(value)))


def norm(values):
    # Use nonnegative upper endpoints before squaring and taking a root.
    return sum((abs(x).upper()**2 for x in values),arb(0)).sqrt().upper()


def save(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if str(path).endswith('.gz'):raw=gzip.compress(raw,mtime=0)
    tmp=Path(str(path)+'.partial');tmp.write_bytes(raw);tmp.replace(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry-report',type=Path,required=True)
    ap.add_argument('--last-block',type=Path,required=True)
    ap.add_argument('--angular',type=Path,required=True)
    ap.add_argument('--waist',type=Path,default=Path('notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256
    if args.out.exists():raise FileExistsError('keep every actual complete waist alignment result')
    geometry,gh=load(args.geometry_report);angular,ah=load(args.angular);waist,wh=load(args.waist)
    if (gh,ah,wh)!=(GEOMETRY,ANGULAR,WAIST):raise ValueError('the original complete waist or geometry input changed')
    block_sha=digest(args.last_block.read_bytes())
    if block_sha!=CHAIN or geometry['last_complete_block_sha256']!=CHAIN:
        raise ValueError('the last actual original block chain differs')
    gi=geometry['identity']
    if (not geometry['complete'] or geometry['failure'] is not None
        or gi['candidate_sha256']!=CANDIDATE or gi['angles']!=N
        or not angular['complete'] or angular['failure'] is not None
        or angular['candidate_sha256']!=CANDIDATE or angular['common_closed_box_count']!=7722
        or not angular['full_real_angular_circle'] or not angular['complete_original_6143_value_jumps_paid']
        or not waist['complete'] or waist['candidate_sha256']!=CANDIDATE
        or Fraction(waist['exact_alpha'])!=ALPHA):
        raise ValueError('a complete original scientific domain or parameter is missing')
    if Fraction.from_float(float(geometry['global_sampled_geometry']['common_world_height_translation']))!=HEIGHT:
        raise ValueError('do not replace the original common world translation')
    with np.load(args.last_block,allow_pickle=False) as z:
        if json.loads(str(z['identity']))!=gi or int(z['indices'][-1])!=0:
            raise ValueError('the actual original terminal row must be at the waist')
        state=z['last_state'].copy()
        if (state.shape!=(N,12) or not np.all(np.isfinite(state))
            or not np.array_equal(state[:,:3],z['geometry'][-1,:,:3])
            or not np.array_equal(state[:,9:12],z['geometry'][-1,:,3:6])):
            raise ValueError('the saved full terminal state is incomplete')
    values=list(map(Fraction,waist['exact_full_V_coefficients']))
    if len(values)!=33:raise ValueError('retain the actual full even waist vector and mean')
    a0=ar(waist['exact_target_waist_radius_enclosure'][0]).union(ar(waist['exact_target_waist_radius_enclosure'][1]))
    coefficients=[ar(ALPHA*x) for x in values]
    mean=-a0+coefficients[0]
    V=(abs(mean)+sum((abs(x) for x in coefficients[1:]),arb(0))).upper()
    V1=sum((4*j*abs(x) for j,x in enumerate(coefficients[1:],1)),arb(0)).upper()
    canonical_F2=norm((V,V1))
    rows=[];maximum_F=arb(0);maximum_Q=arb(0)
    for k in range(N):
        phi=arb.pi()*k/(2*N);co,si=phi.cos(),phi.sin()
        support=-mean;slope=arb(0)
        for j,vj in enumerate(coefficients[1:],1):
            angle=4*j*phi;cj=vj/(16*j*j-1)
            support+=cj*angle.cos();slope-=4*j*cj*angle.sin()
        canonical_F=[support*co-slope*si,support*si+slope*co,arb(0)]
        canonical_Q=[arb(0),arb(0),arb(1),-si,co,arb(0),co,si,arb(0)]
        sampled_F=[dyadic(state[k,j])+(ar(HEIGHT) if j==2 else arb(0)) for j in range(3)]
        sampled_Q=[dyadic(state[k,j]) for j in range(3,12)]
        error_F=norm([x-y for x,y in zip(sampled_F,canonical_F)])
        error_Q=norm([x-y for x,y in zip(sampled_Q,canonical_Q)])
        maximum_F=max(maximum_F,error_F).upper();maximum_Q=max(maximum_Q,error_Q).upper()
        rows.append(dict(angle_grid_index=k,exact_angle='pi*'+str(k)+'/1024',
                         saved_grid_to_canonical_position=record(error_F),
                         saved_grid_to_canonical_frame_Frobenius=record(error_Q)))
    F2=box_from_record(angular['bounds']['position_second_angular_derivative']).upper()
    Q2=box_from_record(angular['bounds']['frame_second_angular_derivative']).upper()
    factor=((arb.pi()/1024)**2/8).upper()
    fee_F=(factor*(F2+canonical_F2)).upper()
    # Canonical Q''=(0,-Y,-N), whose operator norm is exactly one.
    fee_Q=(factor*(Q2+1)).upper()
    aF=(maximum_F+fee_F).upper();aQ=(maximum_Q+fee_Q).upper()
    gates=[dict(name=n,passed=bool(ok)) for n,ok in (
        ('same actual original terminal block and common world translation',True),
        ('complete 33 even waist coefficients with the actual mean retained',len(values)==33),
        ('all 512 exact angular grid points and all frame columns evaluated',len(rows)==N),
        ('complete angular native includes every original radial value jump',angular['complete_original_6143_value_jumps_paid']),
        ('the canonical radius and its full derivative are finite',V.is_finite() and V1.is_finite()),
        ('the actual full-grid position discrepancy is below one micrometre in model units',maximum_F<ar('1/1000000')),
        ('the actual full-frame grid discrepancy is below one billionth',maximum_Q<ar('1/1000000000')),
        ('both complete circle interpolation fees are finite',aF.is_finite() and aQ.is_finite()),
    )]
    doc=dict(kind='actual_complete_exact_waist_grid_to_canonical_alignment_v1',
        complete=all(x['passed'] for x in gates),source_sha256=digest(Path(__file__).read_bytes()),
        inputs={str(args.geometry_report):gh,str(args.last_block):block_sha,str(args.angular):ah,str(args.waist):wh},
        candidate_sha256=CANDIDATE,exact_alpha=str(ALPHA),exact_height_translation=str(HEIGHT),
        exact_target_waist_radius_enclosure=waist['exact_target_waist_radius_enclosure'],
        exact_complete_V_coefficients=waist['exact_full_V_coefficients'],
        exact_angle_definition='phi_k=pi*k/1024, k=0,...,511; final endpoint is the genuine quarter turn',
        canonical_frame='X=(0,0,1), Y=(-sin(phi),cos(phi),0), N=(cos(phi),sin(phi),0)',
        original_model_orientation_retained=True,canonical_frame_second_derivative_operator_norm='1',
        whole_fourfold_wrap_paid=True,
        bounds=dict(reference_waist_v_sup=record(V),reference_waist_v_phi_sup=record(V1),
            canonical_waist_position_second_derivative=record(canonical_F2),
            saved_grid_position_error=record(maximum_F),saved_grid_frame_operator_error_majorant=record(maximum_Q),
            difference_position_interpolation_fee=record(fee_F),difference_frame_interpolation_fee=record(fee_Q),
            position_alignment_additive_constant=record(aF),frame_alignment_additive_constant=record(aQ)),
        contract='b_F0 <= actual_radial_waist_position_error + position_alignment_additive_constant; b_Q0 <= actual_radial_waist_frame_operator_error + frame_alignment_additive_constant',
        missing_radial_waist_error_not_set_to_zero=True,
        full_model_alignment_already_closed=False,exact_GC_solution_or_true_caps_claimed=False,
        rows=rows,gates=gates,seconds=time.monotonic()-started)
    save(args.out,doc)
    print(json.dumps(dict(complete=doc['complete'],points=len(rows),seconds=doc['seconds'],bounds=doc['bounds'])))
    if not doc['complete']:raise RuntimeError('a complete true waist grid gate failed')


if __name__=='__main__':main()
