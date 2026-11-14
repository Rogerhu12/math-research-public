#!/usr/bin/env python3
"""Consume R172's immutable definition and actual coefficients for R174.

Only finite exact algebra and the already bound accurate-profile packet are
read. No ODE, body, F/J, normal, QP or BVP is evaluated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import time

import numpy as np
from flint import ctx

from fd2d_gc_r136_arb_profile import R136ArbProfile, ends
from fd2d_gc_terminal_angular_majorant import (
    rational, sqrt_bounds, terminal_angular_majorant, terminal_integrals,
    tail_curvature_bounds, encode)
from fd2d_dyadic_bernstein_tail import strict_witness_controls

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
FIELD=ROOT/'notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz'
PACKET=ROOT/'notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz'
DEFINITION=ROOT/'notes/2026-11-12-fd2d-accurate-last-cell-01-definition.json'
FIELD_SHA='2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f'
PACKET_SHA='7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c'


def identity(path):
    path=Path(path); data=path.read_bytes()
    return dict(path=path.relative_to(ROOT).as_posix(),bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest())


def dyadic(record):
    return F(int(record[0]))*F(2)**int(record[1])


def evaluate_bernstein(controls,q):
    n=len(controls)-1
    return sum((F(comb(n,i))*c*q**i*(1-q)**(n-i)
                for i,c in enumerate(controls)),F(0))


def exact_product_check(controls,tail):
    """Finite algebra identity check, not a sampled bound or domain test."""
    checked=0
    for j,row in enumerate(tail['local_curvature_controls']):
        for t in (F(0),F(1,2),F(1)):
            q=(j+t)/8
            actual=evaluate_bernstein(row,t)
            expected=F(630)*q**4*(1-q)**4*evaluate_bernstein(controls,q)/F(23,50)
            if actual!=expected:
                raise ArithmeticError('Exact Bernstein product identity failed')
            checked+=1
    return dict(exact_rational_identity_points=checked,all_equal=True,
                geometric_bounds_derived_from_control_hulls_not_these_points=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-stem',type=Path,
        default=ROOT/'notes/2026-11-12-fd2d-terminal-angular-majorant-01')
    args=parser.parse_args();start=time.perf_counter()
    ctx.prec=256
    field_id,packet_id,definition_id=map(identity,(FIELD,PACKET,DEFINITION))
    if field_id['sha256']!=FIELD_SHA or packet_id['sha256']!=PACKET_SHA:
        raise ValueError('The immutable actual inputs differ')
    definition=json.loads(DEFINITION.read_text())
    plain={k:v for k,v in definition.items() if k!='binding_sha256'}
    binding=hashlib.sha256(json.dumps(plain,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if binding!=definition['binding_sha256']:
        raise ValueError('The accurate last-cell definition binding differs')
    if (definition['inputs']['field_arrays']['sha256']!=FIELD_SHA or
        definition['inputs']['profile_packet']['sha256']!=PACKET_SHA):
        raise ValueError('R172 must bind these actual arrays and profile')
    profile=R136ArbProfile.from_packet(PACKET,expected_sha256=PACKET_SHA)
    if profile.inputs['field_arrays']['sha256']!=FIELD_SHA:
        raise ValueError('The accurate profile belongs to another field')
    with np.load(FIELD,allow_pickle=False) as saved:
        K=int(saved['modes'])
        counts=tuple(int(saved[k]) for k in
                     ('central_parameter_count','tail_parameter_count','profile_count'))
        mesh=np.array(saved['mesh'],copy=True)
        raw=np.array(saved['corrections'],copy=True)
        p=np.array(saved['parameters'],copy=True)
    if (counts!=(K,16,7) or raw.shape!=(len(mesh),3*K+2) or
        not np.all(raw[-1]==0)):
        raise ValueError('Require the explicit original layout and zero raw cut trace')
    b=rational(mesh[-2])
    if b!=F(*map(int,definition['saved_last_left'])):
        raise ValueError('Saved left endpoint differs')
    slo,shi=ends(profile.end)
    elllo=dyadic(definition['accurate_last_width']['lower_binary'])
    ellhi=dyadic(definition['accurate_last_width']['upper_binary'])
    # Both packets use rigorous enclosures; overlap is insufficient. The
    # already published R172 enclosure must cover this direct interval.
    if not elllo<=slo-b<=shi-b<=ellhi:
        raise ValueError('The claimed R172 width does not cover the bound profile')
    last=profile.pieces[-1]
    if (last['kind']!='phase_bridge' or last['raw']['exact_endpoint_phase']!='-pi/2'
            or last['raw']['ps0']!=0 or last['raw']['ps1']!=0):
        raise ValueError('R174 cubic terminal phase hypotheses are not present')
    controls=tuple(rational(v) for v in p[K:K+16])
    packet=terminal_angular_majorant(controls,raw[-2],K,
        cell_length_lower=elllo,cell_length_upper=ellhi,
        phase_length=last['L_exact'],phase0=last['p0_exact'])
    identities=exact_product_check(controls,packet['tail'])
    witness=tuple(strict_witness_controls())
    witness_bounds=tail_curvature_bounds(witness,packet['K']['radius_upper'])
    witness_identity=exact_product_check(witness,witness_bounds)
    if min(witness)>=0:
        raise ArithmeticError('The strict R170 enlargement witness was lost')
    remainders=[terminal_integrals(packet,ellhi/F(4)**j)
                for j in (0,2,4,8,12,16)]
    if not all(remainders[i+1]['alpha_uu_integral']<remainders[i]['alpha_uu_integral']
               for i in range(len(remainders)-1)):
        raise ArithmeticError('The proved terminal integral remainder must decrease')
    if sqrt_bounds(F(0))!=(F(0),F(0)) or sqrt_bounds(F(9,16))!=(F(3,4),F(3,4)):
        raise ArithmeticError('Exact-square endpoints were not preserved')
    packet_out=args.output_stem.with_name(args.output_stem.name+'-packet.json')
    packet_out.write_text(json.dumps(encode(dict(
        schema='fd2d-R174-actual-coefficient-majorant-packet-v1',
        inputs=dict(field=field_id,profile_packet=packet_id,accurate_last_definition=definition_id),
        accurate_last_binding_sha256=binding,majorant=packet,
        strict_negative_global_witness=dict(controls=witness,bounds=witness_bounds))),
        indent=2,allow_nan=False)+'\n')
    report=dict(schema='fd2d-R174-finite-coefficient-consumer-report-v1',
        passed=True,inputs=dict(field=field_id,profile_packet=packet_id,accurate_last_definition=definition_id),
        sources=[identity(Path(__file__)),identity(HERE/'fd2d_gc_terminal_angular_majorant.py'),
                 identity(HERE/'fd2d_dyadic_bernstein_tail.py'),
                 identity(HERE/'fd2d_gc_r136_arb_profile.py')],
        packet=identity(packet_out),modes=K,mesh_nodes=len(mesh),
        accurate_width_bounds=encode([elllo,ellhi]),
        terminal_phase=encode(dict(length=last['L_exact'],p0=last['p0_exact'],cut='-pi/2')),
        constants_display={k:float(v) for k,v in packet['constants'].items()},
        K_cubic_bounds_display=[float(packet['K'][k]) for k in ('lower','upper')],
        actual_tail_curvature_derivative_bounds_display=[float(packet['tail'][k]) for k in
                 ('curvature','curvature_y','curvature_yy')],
        actual_product_identity=identities,witness_product_identity=witness_identity,
        strict_negative_global_witness_minimum=encode(min(witness)),
        witness_local_domain_passed=witness_bounds['certificate']['passed'],
        terminal_integrals=encode(remainders),
        body_initial_norms_supplied=False,body_or_ODE_evaluated=False,
        F_J_normal_QP_BVP_evaluated=False,old_arrays_or_metric_modified=False,
        whole_surface_or_R126_seam_certified=False,
        seconds=time.perf_counter()-start)
    report_out=args.output_stem.with_name(args.output_stem.name+'-report.json')
    report_out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(report_out),packet=identity(packet_out),
        passed=True,constants_display=report['constants_display'],seconds=report['seconds']),allow_nan=False))


if __name__=='__main__':
    main()
