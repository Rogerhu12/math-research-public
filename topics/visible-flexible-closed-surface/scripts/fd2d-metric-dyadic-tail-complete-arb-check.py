#!/usr/bin/env python3
"""Small actual R170/R173 constructor and forcing interface check.

The selected boxes are explicitly local. No whole-domain solver, F/J,
body integration or surface certificate is run or inferred.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,gzip,json,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import rational,rational_pair,aq,bound_record
from fd2d_gc_dyadic_tail_complete_arb import (
    DyadicTailAccurateDomainFieldArb,ExactNormalizedCellPrimitive)


def jets(fields):
    return [{k:None if getattr(v,k) is None else bound_record(getattr(v,k))
             for k in ('value','s','xi','xixi','sxi')} for v in fields]


def write_gzip_json(path,value):
    raw=(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
    with Path(path).open('wb') as stream:
        with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as out:
            out.write(raw)
    return dict(**identity(path),uncompressed_bytes=len(raw))


def run(args):
    started=time.monotonic();ctx.prec=args.precision
    outputs={key:args.out_prefix.with_name(args.out_prefix.name+suffix) for key,suffix in
             (('report','-report.json'),('definition','-definition.json.gz'),
              ('primitive','-primitive.json'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(path.exists() for path in outputs.values()):
        raise FileExistsError('Use an unused immutable output stem')
    report=dict(schema='fd2d-R170-complete-current-field-small-check-v1',
        source=identity(__file__),native_definition=identity(args.native_definition),
        profile_packet=identity(args.profile_packet),passed=False,
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        field=DyadicTailAccurateDomainFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'],
            precision=args.precision,profile_backend='bernstein_bumps')
        reader=field.reader;before=identity(reader.arrays_path)
        certificate=reader.tail.control_certificate
        if not certificate['passed']:
            raise AssertionError('The actual exact local-coefficient domain was not proved')
        report.update(actual_field=before,actual_layout=field.parts.layout,
            saved_nodes=len(field.saved_mesh),tail_search_domain_certificate=certificate,
            binding_sha256=field.binding_sha256,
            new_actual_delta_binding=field.profile.input_binding_sha256,
            definition=write_gzip_json(outputs['definition'],field.definition()))
        rows=[];maximum=0.;scaled=0.
        keys=(('value',''),('s','_x'),('xi','_xi'),
              ('xixi','_xixi'),('sxi','_x_xi'))
        for s,xi in ((.61,1.25),(.85,1.34),(1.472,1.19)):
            qs,qxi=rational(s),rational(xi)
            cell=int(np.searchsorted(reader.nodes,s,side='right')-1)
            point=field.box(cell,qs,qs,qxi,qxi,angle_unit='radians',side='right')
            approximate=reader.evaluate_native(np.array([s]),np.array([xi]),side='right')
            comparisons={}
            for name,value in zip(('n','m','l'),point['fields']):
                comparisons[name]={}
                for attribute,suffix in keys:
                    old=float(np.asarray(approximate[name+suffix]).ravel()[0])
                    error=getattr(value,attribute)-aq(old)
                    absolute=float(abs(error).upper())
                    maximum=max(maximum,absolute)
                    scaled=max(scaled,absolute/(1+abs(old)))
                    comparisons[name][attribute]=dict(numeric_native=old,
                        accurate_function_minus_numeric=bound_record(error))
            ds,du=F(1,2**24),F(1,2**22)
            left=max(field.saved_mesh[cell],qs-ds)
            right=min(field.saved_mesh[cell+1],qs+ds)
            if not left<right:
                raise AssertionError('Local box has no positive physical width')
            q=field.box(cell,left,right,qxi-du,qxi+du,angle_unit='radians',side='right')
            if not all(v.is_finite() for v in q['connection']['h_vector']):
                raise AssertionError('The selected actual full-forcing box is not finite')
            rows.append(dict(cell=cell,s=rational_pair(qs),xi=rational_pair(qxi),
                numeric_comparison=comparisons,
                continuous_rectangle=dict(s=[rational_pair(left),rational_pair(right)],
                    xi=[rational_pair(qxi-du),rational_pair(qxi+du)],angle_unit='radians'),
                actual_fields=jets(q['fields']),
                defects={k:bound_record(q['connection'][k]) for k in ('G','Rn','Rm')},
                physical_drift=bound_record(q['chart'].drift())))
        report['three_local_complete_boxes']=rows
        report['numeric_comparison']={
            'absolute_maximum_upper':maximum,
            'scaled_by_one_plus_numeric_maximum_upper':scaled,
            'numeric_values_promoted_to_exact_or_continuous_bounds':False}
        # One trace query exercises the completed-domain dispatch. Its
        # independent geometry/majorant check was already closed elsewhere.
        cut=field.accurate_cut_angular(F(1,4),F(1,4))
        if cut['connection'] is not None or any(
                q.s is not None or q.sxi is not None for q in cut['fields']):
            raise AssertionError('The accurate cut incorrectly acquired radial II jets')
        report['exact_cut_dispatch']=dict(fields=jets(cut['fields']),
            radial_II_or_full_forcing_assigned=False)
        # A new, explicitly exact finite secant P in one actual coast cell.
        # The later H-P box, not the point fitting step, pays its error.
        s,xi=rational(.7),rational(.78)
        cell=next(j for j,(a,b) in enumerate(zip(field.saved_mesh,field.saved_mesh[1:]))
                  if a<=s<b)
        samples=[field.cell_box(cell,t,t,xi,xi,angle_unit='radians')['connection']['h_vector']
                 for t in (F(1,4),F(3,4))]
        cosine=[]
        for first,last in zip(*samples):
            a,b=rational(float(first.mid())),rational(float(last.mid()))
            cosine.append([[F(3,2)*a-F(1,2)*b],[2*(b-a)]])
        primitive=ExactNormalizedCellPrimitive(field,cell,cosine,
            [[[F(0)],[F(0)]] for unused in range(3)],
            provenance=dict(kind='actual R170 complete forcing secant at fixed native xi',
                t=['1/4','3/4'],xi_exact=rational_pair(xi),fit_is_not_certificate=True))
        outputs['primitive'].write_text(json.dumps(
            primitive.definition(),indent=2,allow_nan=False)+'\n')
        dt,du=F(1,2**16),F(1,2**22)
        budget=field.cell_primitive_box(primitive,cell,F(1,2)-dt,F(1,2)+dt,
                                       xi-du,xi+du,angle_unit='radians')
        zeros=[]
        for t in (F(0),F(1)):
            p=primitive.polynomial_boxes(field,t,t,xi,xi,angle_unit='radians')
            zeros.append(all(v.is_zero() for v in p['q']+p['q_xi']))
        if not all(zeros):
            raise AssertionError('The actual physical normalized primitive lost its exact zero endpoints')
        report['one_actual_coast_primitive_box']=dict(packet=identity(outputs['primitive']),
            cell=cell,endpoint_zero=zeros,
            physical_Us_term_included=budget['physical_Us_term_included'],
            Gauss_third_component_included=budget['Gauss_third_component_included'],
            E_norm_upper=bound_record(budget['E_norm_upper']),
            complete_H_minus_P=[bound_record(v) for v in budget['remainder']],
            whole_cell_or_global_forcing_budget_asserted=False)
        if identity(reader.arrays_path)!=before:
            raise AssertionError('The bound actual archive changed during evaluation')
        report['actual_field_unchanged']=True
        report['constructor_source']=identity(Path(__file__).with_name(
            'fd2d_gc_dyadic_tail_complete_arb.py'))
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
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native-definition',type=Path,required=True)
    p.add_argument('--profile-packet',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--precision',type=int,default=256)
    run(p.parse_args())
