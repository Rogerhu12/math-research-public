#!/usr/bin/env python3
"""Build the complete R136 one-dimensional Arb profile packet.

Only scalar target data are consumed. Saved field arrays supply immutable
mesh/physical delta data; no F/J, BVP, frame, body, or tail solver is run.
Finite runtime comparisons use actual old scalar outputs and are explicitly
separate from the continuous accurate-target interval proof.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import resource
import time
import traceback

import numpy as np
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_current_native_interval import aq,rational,rational_pair,bound_record
from fd2d_gc_r136_arb_profile import R136ArbProfile,hull,ends
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_frozen_ellipse_candidate import Candidate


def json_gzip(path,data):
    if path.exists():raise FileExistsError(path)
    raw=(json.dumps(data,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
    with path.open('wb') as stream:
        with gzip.GzipFile(filename='',mode='wb',fileobj=stream,mtime=0) as out:out.write(raw)
    return dict(**identity(path),uncompressed_bytes=len(raw),uncompressed_sha256=hashlib.sha256(raw).hexdigest())


def scalar_record(packet):
    return {key:bound_record(packet[key]) for key in ('a','a_s','a_ss','a_sss','c','K','K_s') if key in packet}


def run(args):
    started=time.monotonic();stem=args.out_prefix
    out={key:stem.with_name(stem.name+suffix) for key,suffix in
        (('report','-report.json'),('packet','-packet.json.gz'),('queries','-queries.json.gz'))}
    if any(path.exists() for path in out.values()):raise FileExistsError('Closed outputs must not be overwritten')
    stem.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-R136-full-one-dimensional-profile-consumption-v1',source=identity(__file__),
        candidate=identity(args.candidate),saved_arrays=identity(args.field),
        scalar_target_only=True,whole_F_J_BVP_body_evaluated=False,passed=False,
        whole_surface_certificate=False)
    try:
        saved=load_npz(args.field)
        before=identity(args.field)['sha256']
        profile=R136ArbProfile(args.candidate,moments=args.moments,
            radius_certificate=args.radius_certificate,field_arrays=args.field,
            precision=args.precision,taylor_order=args.order)
        report['definition']=profile.definition()
        runtime=RadialBumpProfile(args.candidate,supports=np.asarray(saved['profile_supports']),
            coefficients=np.asarray(saved['parameters'])[-int(saved['profile_count']):])
        numeric=runtime.base
        if len(numeric.segments)!=len(profile.pieces):raise ValueError('Actual and accurate raw segment lists differ')
        piece_rows=[];whole=[]
        differences={key:arb(0) for key in ('s0','s1','L','a_start','a_end')}
        for index,piece in enumerate(profile.pieces):
            q=profile.piece_box(index)
            whole.append(q)
            old=numeric.segments[index]
            delta={key:piece[key]-aq(float(old[key])) for key in differences}
            for key,value in delta.items():differences[key]=max(differences[key],abs(value).upper())
            piece_rows.append(dict(index=index,kind=piece['kind'],label=piece['label'],
                accurate_s0=bound_record(piece['s0']),accurate_s1=bound_record(piece['s1']),
                accurate_length=bound_record(piece['L']),complete_jet_box=scalar_record(q),
                actual_old_resolved_differences={key:bound_record(value) for key,value in delta.items()},
                exact_raw_length=None if piece.get('L_exact') is None else rational_pair(piece['L_exact']),
                phase_branches=[dict(lo=rational_pair(b['lo']),hi=rational_pair(b['hi']),
                    sine_remainder=bound_record(b['uniform_sine_remainder']),
                    radius_remainder=bound_record(b['radius_error']),
                    physical_left=bound_record(piece['s0']+piece['L']*aq(b['lo'])),
                    physical_right=bound_record(piece['s0']+piece['L']*aq(b['hi']))) for b in piece.get('branches',[])]))
        report['piece_rows']=piece_rows
        report['continuous_whole_profile_ranges']={key:bound_record(hull(q[key] for q in whole))
            for key in ('a','a_s','a_ss','a_sss','c','K','K_s')}
        report['maximum_actual_resolved_scalar_differences']={key:bound_record(value) for key,value in differences.items()}
        joins=[]
        for index in range(1,len(profile.pieces)):
            join=profile.interface_jets(index)
            overlap={key:bool(join['left'][key].overlaps(join['right'][key])) for key in ('a','a_s','a_ss')}
            if not all(overlap.values()):raise AssertionError('Enclosures contradict a proved shared two-jet at '+str(index))
            joins.append(dict(index=index,shared_two_jet_identity=join['shared_two_jet_identity'],
                enclosure_overlap=overlap,third_jet_left=bound_record(join['left']['a_sss']),
                third_jet_right=bound_record(join['right']['a_sss']),
                common_third_jet_claimed=False))
        report['one_sided_interfaces']=joins
        cut=profile.endpoint_jets()
        report['accurate_cut']=dict(physical_endpoint=bound_record(profile.end),jets=scalar_record(cut),
            exact_radius_two_jet=['4/5','-1','0'],exact_radius_left_third='0',
            R155_second_form_radial_jet_inferred=False)
        # These are the actual old floating observations, each compared at
        # the same fixed physical dyadic s. The last saved number is an
        # endpoint label and is handled separately, not promoted to S_exact.
        mesh=np.asarray(saved['mesh'],float)
        numeric_jets=runtime.jet(mesh)
        query_rows=[]
        maxima={key:dict(upper=arb(0),node=None) for key in ('a','a_s','a_ss','c','K')}
        for index,s in enumerate(mesh[:-1]):
            exact=profile.physical_box(rational(s),rational(s),side='both')
            deltas={key:exact[key]-aq(float(numeric_jets[key][index])) for key in maxima}
            for key,value in deltas.items():
                upper=abs(value).upper()
                if upper>maxima[key]['upper']:maxima[key]=dict(upper=upper,node=index)
            query_rows.append(dict(saved_node=index,physical_s_exact=rational_pair(s),
                possible_accurate_pieces=exact['piece_indices'],accurate_jets=scalar_record(exact),
                actual_runtime={key:float(numeric_jets[key][index]) for key in maxima},
                target_minus_actual_runtime={key:bound_record(value) for key,value in deltas.items()},
                scope='finite actual numerical outputs at the same physical point; not a whole-program floating error theorem'))
        last={key:cut[key]-aq(float(numeric_jets[key][-1])) for key in maxima}
        report['last_saved_endpoint_label_comparison']=dict(saved_label_exact=rational_pair(mesh[-1]),
            accurate_physical_endpoint=bound_record(profile.end),
            endpoint_coordinate_difference=bound_record(profile.end-aq(mesh[-1])),
            paired_accurate_cut_minus_old_label_output={key:bound_record(value) for key,value in last.items()},
            same_physical_coordinate_claimed=False,
            finite_field_extension_or_reparameterization_performed=False)
        report['finite_saved_physical_query_count']=len(query_rows)
        report['finite_same_point_runtime_error_maxima']={key:dict(upper=bound_record(value['upper']),
            saved_node=value['node']) for key,value in maxima.items()}
        report['runtime_scope']=dict(profile_ODE_or_dense_interpolation_used=False,
            radius='actual Candidate 40-point floating Gauss on each explicit phase branch',
            reported_derivatives='analytic sin(phi), cos(phi)*phi_s plus physical bump derivatives',
            derivative_of_floating_quadrature_program_asserted=False,
            entire_runtime_float_program_continuous_error_certified=False,
            accurate_target_directly_enclosed=True)
        report['queries_packet']=json_gzip(out['queries'],dict(input_field_sha256=before,
            target_binding_sha256=profile.input_binding_sha256,rows=query_rows))
        report['profile_packet']=profile.save_packet(out['packet'])
        restored=R136ArbProfile.from_packet(out['packet'],expected_sha256=report['profile_packet']['sha256'])
        reuse=[]
        for s in (F(1,5),F(3,5),F(6,5)):
            a=profile.physical_box(s,s);b=restored.physical_box(s,s)
            ok=all(a[key].overlaps(b[key]) for key in ('a','a_s','a_ss','a_sss','K_s'))
            if not ok:raise AssertionError('Closed scalar packet did not reproduce valid overlapping jet enclosures')
            reuse.append(dict(s_exact=rational_pair(s),overlap=bool(ok)))
        report['closed_packet_reuse']=reuse
        shifted=profile.shifted(F(7,50));shift_rows=[]
        for s in (F(0),F(1,2),F(1)):
            child=shifted.physical_box(s,s);parent=profile.physical_box(s+F(7,50),s+F(7,50))
            ok=all(child[key].overlaps(parent[key]) for key in ('a','a_s','a_ss','a_sss','K_s'))
            if not ok:raise AssertionError('Exact physical translation changed a scalar jet')
            shift_rows.append(dict(new_s_exact=rational_pair(s),same_parent_query_enclosed=True))
        report['exact_cylinder_shift']=dict(definition=shifted.definition(),small_queries=shift_rows)
        report['maximum_phase_Taylor_radius_remainder']=bound_record(max(
            (b['radius_error'] for p in profile.pieces for b in p.get('branches',[])),default=arb(0)))
        if identity(args.field)['sha256']!=before:raise AssertionError('Actual defining field bytes changed')
        report['actual_field_unchanged']=True
        report['scalar_interval_source']=identity(Path(__file__).parent/'fd2d_gc_r136_arb_profile.py')
        report['scope']='Complete accurate one-dimensional physical target/physical bumps; no complete affine field, angular atlas, metric or embedding posterior.'
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-started
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        out['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(out['report']),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'],whole_surface_certificate=False),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    root=Path(__file__).resolve().parent.parent
    parser.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    parser.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    parser.add_argument('--radius-certificate',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json')
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--order',type=int,default=24)
    run(parser.parse_args())
