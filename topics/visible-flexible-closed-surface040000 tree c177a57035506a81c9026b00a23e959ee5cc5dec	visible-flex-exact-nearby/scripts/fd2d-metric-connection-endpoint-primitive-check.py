#!/usr/bin/env python3
"""One actual nonzero R180 cell and one continuous rectangle; no whole solve."""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,json,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    rational,bound_record,connection_box)
from fd2d_gc_current_primitive_interval_v2 import cross,norm_upper
from fd2d_gc_dyadic_tail_complete_arb import DyadicTailAccurateDomainFieldArb
from fd2d_gc_connection_endpoint_primitive import ExactConnectionEndpointPrimitive


def run(args):
    started=time.monotonic();ctx.prec=args.precision
    outputs={key:args.out_prefix.with_name(args.out_prefix.name+suffix)
             for key,suffix in (('report','-report.json'),('primitive','-primitive.json'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(p.exists() for p in outputs.values()):
        raise FileExistsError('Use a new immutable output stem')
    report=dict(schema='fd2d-R180-one-actual-cell-check-v1',
        source=identity(__file__),native_definition=identity(args.native_definition),
        profile_packet=identity(args.profile_packet),passed=False,
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        field=DyadicTailAccurateDomainFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'],
            precision=args.precision)
        before=identity(field.reader.arrays_path)
        s,xi=rational(.7),rational(.78)
        cell=next(j for j,(a,b) in enumerate(zip(field.saved_mesh,field.saved_mesh[1:]))
                  if a<=s<b)
        primitive=ExactConnectionEndpointPrimitive(field,cell)
        outputs['primitive'].write_text(json.dumps(
            primitive.definition(),indent=2,allow_nan=False)+'\n')
        center=primitive.box(field,F(1,2),F(1,2),xi,xi,angle_unit='radians')
        if not any(not value.contains(0) for value in center['q']):
            raise AssertionError('The selected actual endpoint primitive is not proved nonzero')
        q=center['actual'];p=q['profile'];n,m,l=q['fields']
        current=connection_box(q['fields'],p,q['chart'])
        if n.s is None or m.s is None:
            raise AssertionError('The interior comparison requires declared radial jets')
        v_s=(-p.a_s*n.value-p.a*n.s,p.a_s*m.value+p.a*m.s,arb(0))
        q_s=tuple(a-b for a,b in zip(v_s,center['endpoint_slope']))
        commutator=cross(center['q'],center['alpha'])
        direct=tuple(H-ds+center['physical_drift']*du+comm for H,ds,du,comm in
                     zip(current['h_vector'],q_s,center['q_xi'],commutator))
        differences=tuple(a-b for a,b in zip(direct,center['E']))
        if not all(v.contains(0) for v in differences):
            raise AssertionError('Native/physical derivative cancellation has the wrong interval identity')
        endpoint_zero=[]
        for t in (F(0),F(1)):
            endpoint=primitive.box(field,t,t,xi,xi,angle_unit='radians')
            endpoint_zero.append(all(v.is_zero() for v in endpoint['q']+endpoint['q_xi']))
        if not all(endpoint_zero):
            raise AssertionError('The exact full endpoint identities failed')
        dt,du=F(1,2**16),F(1,2**22)
        continuous=primitive.box(field,F(1,2)-dt,F(1,2)+dt,
                                 xi-du,xi+du,angle_unit='radians')
        if not all(v.is_finite() for v in continuous['E']+continuous['q']):
            raise AssertionError('The genuine continuous rectangle is unresolved')
        report.update(actual_field=before,
            complete_field_binding_sha256=field.binding_sha256,
            actual_cell_definition=field.cell_definition(cell),
            primitive=identity(outputs['primitive']),
            primitive_source=identity(Path(__file__).with_name(
                'fd2d_gc_connection_endpoint_primitive.py')),
            exact_endpoint_zero=endpoint_zero,
            nonzero_actual_q=[bound_record(v) for v in center['q']],
            physical_drift=bound_record(center['physical_drift']),
            actual_point_H_norm_upper=bound_record(norm_upper(current['h_vector'])),
            actual_point_E=[bound_record(v) for v in center['E']],
            actual_point_E_norm_upper=bound_record(center['E_norm_upper']),
            direct_derivative_formula_minus_reduced_formula=[bound_record(v) for v in differences],
            continuous_rectangle=dict(
                t=[str(F(1,2)-dt),str(F(1,2)+dt)],
                xi=[str(xi-du),str(xi+du)],angle_unit='radians',
                E=[bound_record(v) for v in continuous['E']],
                E_norm_upper=bound_record(continuous['E_norm_upper']),
                Q_norm_upper=bound_record(continuous['Q_norm_upper']),
                physical_drift=bound_record(continuous['physical_drift']),
                exact_G_scope=continuous['Gauss_scope']),
            actual_q_is_full_function_not_fitted=True,
            actual_E_does_not_consume_n_s_m_s=True,
            whole_cell_or_global_budget_asserted=False)
        if identity(field.reader.arrays_path)!=before:
            raise AssertionError('Actual archive changed')
        report['actual_field_unchanged']=True
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),
                             traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-started
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        outputs['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(outputs['report']),
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'],
            whole_surface_certificate=False),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--native-definition',type=Path,required=True)
    parser.add_argument('--profile-packet',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
