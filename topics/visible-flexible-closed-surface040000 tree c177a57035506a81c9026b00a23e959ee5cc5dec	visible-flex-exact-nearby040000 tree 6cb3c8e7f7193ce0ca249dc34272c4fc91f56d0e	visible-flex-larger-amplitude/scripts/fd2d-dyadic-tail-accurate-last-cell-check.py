#!/usr/bin/env python3
"""Bind actual negative-global-control state30 to its accurate final cell.

Small domain/definition/cut/interior checks only; no whole body, F/J or BVP.
The supplied accurate profile must be rebound to the same actual NPZ bytes.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import time

from flint import arb,ctx

from fd2d_gc_dyadic_tail_accurate_last_cell import DyadicTailAccurateLastCell
from fd2d_gc_current_native_interval import aq,bound_record
from fd2d_gc_dyadic_tail_archive_native import bind_dyadic_tail_archive_native
from fd2d_gc_terminal_angular_majorant import encode

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
FIELD=ROOT/'notes/2026-11-12-fd2d-raw-bump-dyadic30-trial-back01-a01-accepted.npz'
FIELD_SHA='3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981'
FOUNDATION=ROOT/'notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json'


def identity(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return dict(path=path.relative_to(ROOT).as_posix(),bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest())


def write(path,value):
    path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    return identity(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--profile-packet',type=Path,required=True)
    ap.add_argument('--profile-sha256',required=True)
    ap.add_argument('--output-stem',type=Path,
        default=ROOT/'notes/2026-11-12-fd2d-dyadic-tail-accurate-last-cell-30-01')
    args=ap.parse_args();start=time.perf_counter();ctx.prec=256
    if identity(FIELD)['sha256']!=FIELD_SHA:
        raise ValueError('The immutable accepted30 field bytes changed')
    model=DyadicTailAccurateLastCell(FIELD,args.profile_packet,
                                     profile_sha256=args.profile_sha256)
    if (model.tail_control_certificate['global_control_box_passed'] or
            not model.tail_control_certificate['passed']):
        raise ValueError('This check specifically binds the actual enlarged-domain state')
    definition=model.definition()
    definition_path=args.output_stem.with_name(args.output_stem.name+'-definition.json')
    definition_id=write(definition_path,definition)
    native=bind_dyadic_tail_archive_native(FIELD,foundation_definition=FOUNDATION)
    native_definition=native.definition()
    if (native_definition['arrays']['sha256']!=FIELD_SHA or
            native.tail.control_certificate!=model.tail_control_certificate):
        raise ValueError('Complete native and final-cell domains bind different actual data')
    native_path=args.output_stem.with_name(args.output_stem.name+'-native-definition.json')
    native_id=write(native_path,native_definition)
    cuts=[]
    for u in (F(0),F(1,6),F(1,2)):
        result=model.box(1,1,u,u)
        if (not result['cut'] or result['radial_II_jets_assigned'] or
                any(v.s is not None or v.sxi is not None for v in result['fields'])):
            raise ArithmeticError('A cut angular-only query acquired radial II jets')
        if u in (F(0),F(1,2)):
            if not all(getattr(v,k).contains(0) for v in result['fields']
                       for k in ('value','xi','xixi')):
                raise ArithmeticError('Exact flat-angle zero trace was lost')
        else:
            q=F(3,23)
            P=sum((F(comb(15,j))*c*q**j*(1-q)**(15-j)
                   for j,c in enumerate(model.tail)),F(0))
            k=aq(F(630)/F(23,50)*q**4*(1-q)**4*P)
            expected=(3*k/4,-arb(3).sqrt()*k/4,k/4)
            if not all(v.value.overlaps(t) for v,t in zip(result['fields'],expected)):
                raise ArithmeticError('Cut pi/6 does not enclose the separate exact polynomial formula')
        cuts.append(dict(angle_multiple_of_pi=str(u),
                         fields=[v.record() for v in result['fields']],
                         radial_jets_missing=True))
    inside=model.box(F(1,2),F(1,2),F(1,6),F(1,6))
    n,m,l=inside['fields'];p=inside['profile'];K=-p['a_ss']/p['a']
    G=n.value*l.value-m.value*m.value-K
    if not (K>0 and G.contains(0)):
        raise ArithmeticError('The interior full R155 interval identity was not enclosed')
    majorant=model.angular_majorant()
    majorant_path=args.output_stem.with_name(args.output_stem.name+'-majorant.json')
    majorant_id=write(majorant_path,encode(majorant))
    report=dict(schema='fd2d-R170-accurate-last-cell-small-consumer-v1',passed=True,
        inputs=dict(field=identity(FIELD),profile=identity(args.profile_packet),
                    foundation=identity(FOUNDATION)),
        sources=[identity(HERE/name) for name in (
            'fd2d-dyadic-tail-accurate-last-cell-check.py',
            'fd2d_gc_dyadic_tail_accurate_last_cell.py',
            'fd2d_gc_accurate_last_cell.py','fd2d_gc_dyadic_tail_archive_native.py')],
        definition=definition_id,native_definition=native_id,majorant=majorant_id,
        exact_domain=model.tail_control_certificate,
        accurate_physical_binding=model.profile.input_binding_sha256,
        cut_checks=cuts,one_interior_check=dict(normalized_t='1/2',angle_multiple_of_pi='1/6',
            K=bound_record(K),Gauss_identity=bound_record(G),
            fields=[v.record() for v in inside['fields']]),
        terminal_majorant_display={k:float(v) for k,v in majorant['constants'].items()},
        original_global_domain_constructor_invoked=False,
        inherited_interval_formulas_unchanged=True,
        whole_interval_geometry_or_body_or_F_J_BVP_evaluated=False,
        old_arrays_metric_or_closed_sources_modified=False,
        seconds=time.perf_counter()-start)
    report_path=args.output_stem.with_name(args.output_stem.name+'-report.json')
    report_id=write(report_path,report)
    print(json.dumps(dict(report=report_id,definition=definition_id,native=native_id,
        majorant=majorant_id,passed=True,seconds=report['seconds']),allow_nan=False))


if __name__=='__main__':
    main()
