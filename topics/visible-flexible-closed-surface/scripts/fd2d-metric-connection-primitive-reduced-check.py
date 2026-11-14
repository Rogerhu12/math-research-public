#!/usr/bin/env python3
"""One already-defined R180 rectangle, comparing exact E3 enclosures only."""
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
from fd2d_gc_connection_endpoint_primitive import ExactConnectionEndpointPrimitive
from fd2d_gc_connection_primitive_gauss_reduction import reduce_gauss_component


def run(args):
    start=time.monotonic();ctx.prec=256
    out=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if out.exists():raise FileExistsError(out)
    out.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-R180-combined-Gauss-one-box-check-v1',
        source=identity(__file__),passed=False,
        native_definition=identity(args.native_definition),
        profile_packet=identity(args.profile_packet),
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        field=DyadicTailAccurateDomainFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'])
        s,xi=rational(.7),rational(.78)
        cell=next(j for j,(a,b) in enumerate(zip(field.saved_mesh,field.saved_mesh[1:]))
                  if a<=s<b)
        primitive=ExactConnectionEndpointPrimitive(field,cell)
        dt,du=F(1,2**16),F(1,2**22)
        original=primitive.box(field,F(1,2)-dt,F(1,2)+dt,
                                xi-du,xi+du,angle_unit='radians')
        reduced=reduce_gauss_component(original)
        if (reduced['primitive_sha256']!=original['primitive_sha256']
                or reduced['field_binding_sha256']!=original['field_binding_sha256']):
            raise AssertionError('An enclosure backend changed the mathematical object')
        report.update(actual_field=identity(field.reader.arrays_path),cell=cell,
            field_binding_sha256=field.binding_sha256,
            primitive_sha256=primitive.packet_sha256,
            original_E3=bound_record(original['E'][2]),
            combined_E3=bound_record(reduced['combined_E3_enclosure']),
            intersected_E3=bound_record(reduced['E'][2]),
            original_E_norm_upper=bound_record(original['E_norm_upper']),
            reduced_E_norm_upper=bound_record(reduced['E_norm_upper']),
            reducer_source=reduced['enclosure_source'],
            same_full_mathematical_E=True,full_Gauss_contribution_kept=True,
            interval_enclosure_only_no_new_actual_field=True,passed=True)
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
