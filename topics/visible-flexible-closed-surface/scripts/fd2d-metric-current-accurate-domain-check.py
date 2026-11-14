#!/usr/bin/env python3
"""Small R173 domain-composition check; no new solve or global certificate."""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as F
from pathlib import Path
import json,resource,time,traceback
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import rational,aq,bound_record,UnresolvedInterval
from fd2d_gc_current_accurate_domain_arb import AccurateDomainCurrentFieldArb,ExactNormalizedCellPrimitive


def jets(values):
    return [{k:None if getattr(v,k) is None else bound_record(getattr(v,k))
             for k in ('value','s','xi','xixi','sxi')} for v in values]


def run(args):
    begun=time.monotonic();ctx.prec=args.precision
    names={key:args.out_prefix.with_name(args.out_prefix.name+suffix) for key,suffix in
        (('report','-report.json'),('definition','-definition.json'),('primitive','-primitive.json'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(path.exists() for path in names.values()):raise FileExistsError('Use a new immutable output stem')
    report=dict(schema='fd2d-current-accurate-domain-small-check-v1',source=identity(__file__),
        native_definition=identity(args.native_definition),profile_packet=identity(args.profile_packet),
        passed=False,whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        full=AccurateDomainCurrentFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'],precision=args.precision,
            profile_backend='bernstein_bumps')
        before=identity(full.reader.arrays_path)
        names['definition'].write_text(json.dumps(full.definition(),indent=2,allow_nan=False)+'\n')
        report.update(definition=identity(names['definition']),actual_field=before,
            actual_layout=full.parts.layout,saved_nodes=len(full.saved_mesh),
            binding_sha256=full.binding_sha256,last_cell=full.cell_definition(full.last_cell),
            accurate_profile_target_binding=full.profile.input_binding_sha256,
            exact_profile_target_matches_interior_and_terminal=True)
        # Three previously uncontroversial small interior boxes: only the
        # same-function R175 range backend changes their enclosure method.
        rows=[]
        for s,xi in ((.61,1.25),(.85,1.34),(1.472,1.19)):
            qs,qxi=rational(s),rational(xi)
            cell=next(j for j,(a,b) in enumerate(zip(full.saved_mesh,full.saved_mesh[1:])) if a<=qs<b)
            sr,ar=F(1,2**24),F(1,2**22)
            left,right=max(full.saved_mesh[cell],qs-sr),min(full.saved_mesh[cell+1],qs+sr)
            row=full.box(cell,left,right,qxi-ar,qxi+ar,angle_unit='radians',side='right')
            for value in row['connection']['h_vector']:
                if not value.is_finite():raise AssertionError('Nonfinite complete interior forcing')
            rows.append(dict(cell=cell,fields=jets(row['fields']),
                G=bound_record(row['connection']['G']),Rn=bound_record(row['connection']['Rn']),
                Rm=bound_record(row['connection']['Rm']),drift=bound_record(row['chart'].drift()),
                source_binding=row['binding_sha256']))
        report['small_same_target_interior_boxes']=rows
        # R172 changes radial evaluation on its whole final cell, but its
        # left complete value and angular two-jets equal the old interior.
        b=full.saved_mesh[-2];angle=F(1,4)
        left=full.box(full.last_cell-1,b,b,angle,angle,side='left')
        right=full.cell_box(full.last_cell,F(0),F(0),angle,angle)
        overlap={name:[bool(getattr(a,name).overlaps(getattr(c,name))) for a,c in zip(left['fields'],right['fields'])]
                 for name in ('value','xi','xixi')}
        if not all(all(v) for v in overlap.values()):raise AssertionError('R172 left full angular traces do not match')
        report['accurate_last_cell_left_trace']=dict(angular_twojet_overlap=overlap,
            true_identity='sigma(b)=b, eta same, accurate radius and K same; R155 same angular function',
            radial_II_jump_not_identified_with_zero=True)
        terminal=[]
        for tlo,thi in ((F(1,4),F(1,4)),(F(1,2),F(1,2)),(F(3,4),F(3,4))):
            q=full.cell_box(full.last_cell,tlo,thi,angle,angle)
            if not all(x.is_finite() for x in q['connection']['h_vector']):raise AssertionError('Nonfinite final-cell interior forcing')
            terminal.append(dict(t=[str(tlo),str(thi)],fields=jets(q['fields']),
                defects={k:bound_record(q['connection'][k]) for k in ('G','Rn','Rm')},
                actual_drift=bound_record(q['chart'].drift())))
        report['R172_interior_full_forcing_queries']=terminal
        cut=full.accurate_cut_angular(angle,angle)
        if cut['connection'] is not None or any(v.s is not None or v.sxi is not None for v in cut['fields']):
            raise AssertionError('Cut acquired an unproved radial II or forcing value')
        report['accurate_cut']=dict(fields=jets(cut['fields']),full_forcing_assigned=False,radial_II_jets_assigned=False)
        unresolved=False
        try:full.cell_box(full.last_cell,F(3,4),F(1),angle,angle)
        except UnresolvedInterval as exc:
            unresolved=True;report['cut_touching_box']=dict(status='explicitly unresolved',reason=str(exc))
        if not unresolved:raise AssertionError('A degenerate cut box was silently assigned full derivative bounds')
        # A finite P is defined by actual forcing samples. Exact zero-end
        # identities refer to the true S-b length; the full interval H-P
        # below pays its approximation error on the requested small box.
        H=[]
        for t in (F(1,4),F(3,4)):
            H.append(full.cell_box(full.last_cell,t,t,angle,angle)['connection']['h_vector'])
        cosine=[]
        for a,bv in zip(*H):
            a,bv=rational(float(a.mid())),rational(float(bv.mid()))
            cosine.append([[F(3,2)*a-F(1,2)*bv],[2*(bv-a)]])
        primitive=ExactNormalizedCellPrimitive(full,full.last_cell,cosine,
            [[[F(0)],[F(0)]] for unused in range(3)],
            provenance=dict(kind='actual last-cell two-point forcing secant; finite rational P only',
                sample_labels=['1/4','3/4'],angular_pi_multiple='1/4',sample_fit_error_claimed=False))
        names['primitive'].write_text(json.dumps(primitive.definition(),indent=2,allow_nan=False)+'\n')
        # The query is a genuinely positive-width local rectangle. It does
        # not approach the unresolved degenerate endpoint.
        t0=F(1,2);dt=F(1,2**16);da=F(1,2**22)
        budget=full.cell_primitive_box(primitive,full.last_cell,t0-dt,t0+dt,angle-da,angle+da)
        endpoint_zero=[]
        for t in (F(0),F(1)):
            p=primitive.polynomial_boxes(full,t,t,angle,angle)
            endpoint_zero.append(all(v.is_zero() for v in p['q']+p['q_xi']))
        if not all(endpoint_zero):raise AssertionError('True-length normalized primitive lost exact zero endpoints')
        report['normalized_final_cell_primitive']=dict(packet=identity(names['primitive']),
            exact_identities=primitive.exact_identities,actual_endpoint_zero=endpoint_zero,
            complete_H_minus_P=[bound_record(v) for v in budget['remainder']],
            E=[bound_record(v) for v in budget['E']],E_norm_upper=bound_record(budget['E_norm_upper']),
            physical_cell_length_enclosure=budget['physical_cell_length_enclosure'],
            physical_Us_term_included=budget['physical_Us_term_included'],
            Gauss_third_component_included=budget['Gauss_third_component_included'],
            whole_final_cell_forcing_bound_asserted=False)
        if identity(full.reader.arrays_path)!=before:raise AssertionError('Actual input bytes changed')
        report['actual_field_unchanged']=True
        report['sources']=[identity(Path(__file__).parent/name) for name in
            ('fd2d_gc_current_accurate_domain_arb.py','fd2d_gc_current_complete_field_arb.py',
             'fd2d_gc_current_frozen_atlas_arb.py','fd2d_gc_accurate_last_cell.py',
             'fd2d_gc_r136_bernstein_bumps.py','fd2d_gc_current_primitive_interval_v2.py')]
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-begun
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        names['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(names['report']),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'],whole_surface_certificate=False),allow_nan=False))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    p.add_argument('--native-definition',type=Path,required=True)
    p.add_argument('--profile-packet',type=Path,default=root/'notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz')
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--precision',type=int,default=256)
    run(p.parse_args())
