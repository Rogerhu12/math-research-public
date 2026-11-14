#!/usr/bin/env python3
"""Reusable replay of the R180 subcell check first executed as a here-document.

The initial receipt records that actual entry separately. This configurable
replay entry is not retroactively claimed as its executed source identity.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,json,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
from flint import ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import rational,bound_record
from fd2d_gc_dyadic_tail_complete_arb import DyadicTailAccurateDomainFieldArb
from fd2d_gc_connection_primitive_subcell import RestrictedConnectionEndpointPrimitive


def run(args):
    start=time.monotonic();ctx.prec=256
    out=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if out.exists():raise FileExistsError(out)
    out.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-R180-exact-subcell-actual-small-check-v1',
        replay_entry_source=identity(__file__),passed=False,
        native_definition=identity(args.native_definition),
        profile_packet=identity(args.profile_packet),
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        field=DyadicTailAccurateDomainFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'])
        primitive=RestrictedConnectionEndpointPrimitive(field,69,F(1,4),F(3,4))
        u=rational(.78)
        point=primitive.box(field,F(1,2),F(1,2),u,u,angle_unit='radians')
        if point['source_cell']!=69 or point['original_normalized_query']!=[['1','2'],['1','2']]:
            raise AssertionError('The verification subcell changed the actual cell identity')
        zeros=[]
        for t in (F(0),F(1)):
            q=primitive.box(field,t,t,u,u,angle_unit='radians')
            zeros.append(all(v.is_zero() for v in q['q']+q['q_xi']))
        if not all(zeros) or not any(not v.contains(0) for v in point['q']):
            raise AssertionError('Require exact zero endpoints and a genuine nonzero interior primitive')
        dt,du=F(1,2**16),F(1,2**22)
        box=primitive.box(field,F(1,2)-dt,F(1,2)+dt,u-du,u+du,angle_unit='radians')
        report.update(source=identity(Path(__file__).with_name('fd2d_gc_connection_primitive_subcell.py')),
            actual_field=identity(field.reader.arrays_path),primitive=primitive.definition(),
            original_cell_index_retained=69,
            point_q=[bound_record(v) for v in point['q']],
            point_E_norm_upper=bound_record(point['E_norm_upper']),
            continuous_E_norm_upper=bound_record(box['E_norm_upper']),
            continuous_Q_norm_upper=bound_record(box['Q_norm_upper']),
            physical_length=bound_record(point['physical_subcell_length']),
            actual_query_original_t=point['original_normalized_query'],
            endpoint_zero=zeros,actual_field_mesh_or_functions_changed=False,passed=True)
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),
                             traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(out),
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native-definition',type=Path,required=True)
    p.add_argument('--profile-packet',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    run(p.parse_args())
