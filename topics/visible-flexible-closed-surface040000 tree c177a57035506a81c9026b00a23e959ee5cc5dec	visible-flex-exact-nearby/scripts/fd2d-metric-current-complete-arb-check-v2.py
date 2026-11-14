#!/usr/bin/env python3
"""One small immutable current-field interval integration check.

No whole F/J, BVP, body, adaptive global certification or new solution is
computed. The full functions and their continuous local boxes are bound;
old floating outputs are retained only as actual finite comparisons.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as F
from pathlib import Path
import json,resource,time,traceback
import numpy as np
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField
from fd2d_gc_current_complete_field_arb import CompleteCurrentFieldArb
from fd2d_gc_current_frozen_atlas_arb import TwoJet
from fd2d_gc_current_native_interval import aq,rational,rational_pair,bound_record,ProfileBox,ChartBox,connection_box
from fd2d_gc_current_primitive_interval_v2 import ExactZeroEndPrimitive


def jet_record(q):
    return {k:None if getattr(q,k) is None else bound_record(getattr(q,k))
            for k in ('value','s','xi','xixi','sxi')}


def run(args):
    begun=time.monotonic();ctx.prec=args.precision
    root=args.out_prefix.parent;root.mkdir(parents=True,exist_ok=True)
    names={k:args.out_prefix.with_name(args.out_prefix.name+suffix) for k,suffix in
        (('report','-report.json'),('native','-native-definition.json'),
         ('definition','-definition.json'),('primitive','-primitive.json'))}
    if any(v.exists() for v in names.values()):raise FileExistsError('Use a new immutable output stem')
    report=dict(schema='fd2d-current-complete-Arb-small-actual-integration-v2',
        source=identity(__file__),field=identity(args.field),candidate=identity(args.candidate),
        profile_packet=identity(args.profile_packet),passed=False,
        whole_F_J_BVP_body_evaluated=False,whole_surface_certificate=False)
    try:
        before=identity(args.field)['sha256']
        reader=IndependentTailPositiveTraceNativeField(args.field,args.candidate,reference_inlet=args.inlet)
        names['native'].write_text(json.dumps(reader.definition(),indent=2,allow_nan=False)+'\n')
        full=CompleteCurrentFieldArb(names['native'],args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'],precision=args.precision)
        names['definition'].write_text(json.dumps(full.definition(),indent=2,allow_nan=False)+'\n')
        report['full_definition']=identity(names['definition'])
        report['native_definition']=identity(names['native'])
        report['full_binding_sha256']=full.binding_sha256
        report['actual_layout']=full.parts.layout
        report['saved_nodes']=len(full.parts.mesh)
        report['global_frozen_chart_positivity']=full.atlas.global_proof
        report['exact_exit_alignment']=dict(exit_sigma=rational_pair(full.atlas.exit_sigma),
            stored_length=rational_pair(full.atlas.stored_length),
            difference=rational_pair(full.atlas.exit_sigma-full.atlas.stored_length))
        report['tail_weight_width_difference']=rational_pair(full.tail_accurate_width-full.tail_old_independent_width)
        samples=[(.2,.31),(.4,.73),(.565,1.1),(.61,1.25),(.70,.78),(.85,1.34),
                 (1.0,.91),(1.3,1.41),(1.472,1.19),(1.48,.67)]
        rows=[];maximum=0.;scaled=0.
        keys=(('value',''),('s','_x'),('xi','_xi'),('xixi','_xixi'),('sxi','_x_xi'))
        for index,(s,xi) in enumerate(samples):
            cell=int(np.searchsorted(reader.nodes,s,side='right')-1)
            qs,qxi=rational(s),rational(xi)
            q=full.box(cell,qs,qs,qxi,qxi,angle_unit='radians',side='right')
            observed=reader.evaluate_native(np.array([s]),np.array([xi]),side='right')
            comparisons={}
            for component,field in zip(('n','m','l'),q['fields']):
                comparisons[component]={}
                for local,suffix in keys:
                    value=float(np.asarray(observed[component+suffix]).ravel()[0])
                    error=getattr(field,local)-aq(value)
                    absolute=float(abs(error).upper())
                    maximum=max(maximum,absolute);scaled=max(scaled,absolute/(1+abs(value)))
                    comparisons[component][local]=dict(actual_numeric=value,
                        accurate_target_minus_numeric=bound_record(error))
            # A genuine positive-width rectangle, restricted to this P1
            # cell; this is a local continuous box, never global coverage.
            sr=F(1,2**24);ar=F(1,2**22)
            box_left=max(full.parts.mesh[cell],qs-sr)
            box_right=min(full.parts.mesh[cell+1],qs+sr)
            if not box_left<box_right or not box_left<=qs<=box_right:
                raise ValueError('No positive-width local box inside the declared saved P1 cell')
            local=full.box(cell,box_left,box_right,qxi-ar,qxi+ar,angle_unit='radians',side='right')
            scalar=[getattr(f,key) for f in local['fields'] for key,unused in keys]
            scalar+=list(local['connection']['h_vector'])
            if not all(x.is_finite() for x in scalar):raise ArithmeticError('Nonfinite complete actual local interval')
            rows.append(dict(index=index,cell=cell,physical_s=rational_pair(qs),label_xi=rational_pair(qxi),
                comparison=comparisons,
                continuous_box=dict(s=[rational_pair(box_left),rational_pair(box_right)],
                    xi=[rational_pair(qxi-ar),rational_pair(qxi+ar)],angle_unit='radians',
                    fields=[jet_record(v) for v in local['fields']],
                    full_connection={k:bound_record(local['connection'][k]) for k in ('G','Rn','Rm')},
                    actual_drift=bound_record(local['chart'].drift())),
                observed_numeric_outputs_are_not_interval_verdicts=True))
        report['actual_local_rows']=rows
        report['finite_numeric_comparison']=dict(scalar_jet_count=len(rows)*15,
            maximum_absolute_error_upper_display=maximum,
            maximum_error_over_one_plus_actual_upper_display=scaled,
            only_actual_finite_point_outputs=True,uniform_float_program_error_asserted=False)
        interfaces=[]
        for s in (full.atlas.entry_start,full.atlas.entry,full.atlas.exit,full.atlas.exit_stop):
            left=full.atlas.box(s,s,F(1,4),F(1,4),side='left')['U']
            right=full.atlas.box(s,s,F(1,4),F(1,4),side='right')['U']
            overlap={key:bool(getattr(left,key).overlaps(getattr(right,key))) for key in ('value','xi','xixi')}
            if not all(overlap.values()):raise AssertionError('Common complete angular atlas traces are not enclosed')
            interfaces.append(dict(s=rational_pair(s),angular_pi_multiple=['1','4'],
                full_function_identity='R149 uses the same seed/old/closed-coast endpoint functions',
                point_enclosure_overlap=overlap,Us_right_minus_left=bound_record(right.s-left.s),
                radial_common_trace_claimed=False))
        report['atlas_interface_queries']=interfaces
        reference=[]
        for fraction in (F(0),F(1,2),F(1)):
            s=full.atlas.entry+fraction*full.atlas.exit_sigma
            data=full.atlas.angular(F(1,4),F(1,4))
            q=full.atlas.ruling(s,s,data)
            if not all(v.contains(0) for v in q['differentiated_angle_identity_residuals'].values()):
                raise AssertionError('Differentiated angle and D/(vQ) identity disagree')
            U=q['U'];a=full.atlas.a+full.atlas.v*aq(s-full.atlas.entry)
            base=ProfileBox(a,full.atlas.v,arb(0),arb(0))
            C=connection_box(tuple(v.native() for v in q['fields']),base,ChartBox(U.xi,U.s,U.xixi,U.sxi))
            if not all(C[k].contains(0) for k in ('G','Rn','Rm')):
                raise AssertionError('Complete frozen reference native GC identities are not enclosed')
            reference.append(dict(s=rational_pair(s),
                angle_derivative_identity={k:bound_record(v) for k,v in q['differentiated_angle_identity_residuals'].items()},
                base_only_GC={k:bound_record(C[k]) for k in ('G','Rn','Rm')},
                current_nonzero_delta_GC_asserted=False))
        report['reference_analytic_identities']=reference
        cuts=[]
        for phi in (F(0),F(1,8),F(1,4),F(1,2)):
            q=full.accurate_cut_angular(phi,phi)
            if any(f.s is not None or f.sxi is not None for f in q['fields']):
                raise AssertionError('The accurate cut gained an unproved radial II jet')
            cuts.append(dict(phi_pi_multiple=rational_pair(phi),fields=[jet_record(f) for f in q['fields']],
                             radial_II_jets_assigned=False))
        report['accurate_rational_tail_cut_angular_queries']=cuts
        # Nonzero exact zero-end primitive obtained from two actual local
        # forcing evaluations. The finite coefficient representatives
        # define P; all H-P error is then enclosed from complete functions.
        s,xi=.7,.78;cell=int(np.searchsorted(reader.nodes,s,side='right')-1)
        center=rational(s);width=F(1,2**17);left,right=center-width,center+width
        angle=rational(xi)
        H0=full.box(cell,left,left,angle,angle,angle_unit='radians')['connection']['h_vector']
        H1=full.box(cell,right,right,angle,angle,angle_unit='radians')['connection']['h_vector']
        cosine=[]
        for a,b in zip(H0,H1):
            v0=rational(float(a.mid()));v1=rational(float(b.mid()))
            cosine.append([[v0],[v1-v0]])
        primitive=ExactZeroEndPrimitive(left,right,cosine,[[[F(0)],[F(0)]] for unused in range(3)],
            field_binding_sha256=full.binding_sha256,
            provenance=dict(kind='actual small local complete-H endpoint secant in xi-independent finite P',
                accurate_full_field=full.binding_sha256,physical_cell=cell,chosen_label_exact=rational_pair(angle),
                fitting_accuracy_asserted=False,actual_H_minus_P_paid_by_complete_interval_evaluation=True))
        names['primitive'].write_text(json.dumps(primitive.definition(),indent=2)+'\n')
        budget=full.primitive_box(primitive,cell,left,right,angle-F(1,2**22),angle+F(1,2**22),angle_unit='radians')
        report['actual_small_primitive']=dict(packet=identity(names['primitive']),
            exact_identities=primitive.exact_identities,
            complete_actual_H_minus_P=[bound_record(v) for v in budget['remainder']],
            E=[bound_record(v) for v in budget['E']],E_norm_upper=bound_record(budget['E_norm_upper']),
            physical_Us_term_included=budget['physical_Us_term_included'],
            Gauss_third_component_included=budget['Gauss_third_component_included'],
            global_field_coverage_or_initial_defect_claimed=False)
        if identity(args.field)['sha256']!=before:raise AssertionError('Immutable actual field changed')
        report['actual_field_unchanged']=True
        report['sources']=[identity(Path(__file__).parent/name) for name in
            ('fd2d_gc_current_frozen_atlas_arb.py','fd2d_gc_current_complete_field_arb.py',
             'fd2d_gc_r136_arb_profile.py','fd2d_gc_current_native_interval.py','fd2d_gc_current_primitive_interval_v2.py')]
        report['scope']='Complete continuous local functions and R125 interface on an immutable bad/unfinished candidate; no full-domain nonlinear solution or surface certificate.'
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
    p.add_argument('--field',type=Path,required=True)
    p.add_argument('--candidate',type=Path,default=root/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json')
    p.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    p.add_argument('--profile-packet',type=Path,default=root/'notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz')
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--precision',type=int,default=256)
    run(p.parse_args())
