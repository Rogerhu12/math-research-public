"""One complete signed-window box and two native point comparisons.

No F/J, BVP or body integration is run. Floating comparisons are finite
implementation diagnostics; the interval box comes from the complete
accurate analytic definition, not those samples.
"""
from __future__ import annotations

import argparse,gzip,hashlib,json,resource,time,traceback
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import aq,bound_record,rational_pair,square
from fd2d_gc_r136_arb_profile import ends
from fd2d_gc_signed_trace_archive_native import SignedTraceArchiveNativeField
from fd2d_gc_signed_trace_complete_arb import SignedTraceAccurateDomainFieldArb


def vector_bound(values):
    return sum((square(v) for v in values)).sqrt().upper()


def serialized_box(packet):
    c=packet['connection']
    return dict(cell=packet['cell'],fields=[v.record() for v in packet['fields']],
        signed_components=[dict(name=v['name'],sign=v['sign'],weight=v['weight'].record())
            for v in packet['signed_components']],
        profile={k:bound_record(packet['profile_box'][k]) for k in ('a','a_s','a_ss','a_sss','K','K_s')},
        chart={k:bound_record(getattr(packet['chart'],k)) for k in ('U_xi','U_s','U_xixi','U_sxi')},
        connection={k:bound_record(c[k]) for k in ('G','Rn','Rm')},
        H=[bound_record(v) for v in c['h_vector']],
        H_norm_upper=bound_record(vector_bound(c['h_vector'])),
        complete_physical_Us_drift_retained=True)


def numeric_connection(q):
    scalar=lambda key:float(np.asarray(q[key]))
    a=scalar('a');c=scalar('a_s')/a
    drift=scalar('U_x')/scalar('U_xi')
    n,m,l=(scalar(k) for k in ('n','m','l'))
    ns=scalar('n_x')-drift*scalar('n_xi')
    ms=scalar('m_x')-drift*scalar('m_xi')
    mu=scalar('m_xi')/scalar('U_xi');lu=scalar('l_xi')/scalar('U_xi')
    G=l*n-m*m+scalar('a_ss')/a
    Rn=ns-mu/a-c*(l-n);Rm=ms-lu/a+2*c*m
    return dict(G=G,Rn=Rn,Rm=Rm,H=[-a*Rn,a*Rm,-a*G],drift=drift)


def run(args):
    start=time.monotonic();ctx.prec=256
    out={key:args.out_prefix.with_name(args.out_prefix.name+suffix) for key,suffix in
        [('native','-native-definition.json'),('definition','-interval-definition.json.gz'),('report','-report.json')]}
    if any(p.exists() for p in out.values()):
        raise FileExistsError('Use a new immutable output prefix')
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-R182-actual-signed-native-and-continuous-box-run-v2',
        source=identity(__file__),passed=False,whole_F_J_BVP_body_evaluated=False,
        field=identity(args.field),origin=identity(args.origin),
        floating_comparisons_are_diagnostics_not_interval_certificates=True)
    try:
        native=SignedTraceArchiveNativeField(args.field,origin_field=args.origin,
            foundation_definition=args.foundation_definition)
        out['native'].write_text(json.dumps(native.definition(),indent=2,allow_nan=False)+'\n')
        interval=SignedTraceAccurateDomainFieldArb(out['native'],args.profile_packet,
            profile_packet_sha256=args.profile_sha256)
        records=[];maximum_absolute=0.;maximum_scaled=0.
        for label,s,xi in [('middle_rising',F(363,400),F(7,20)),
                           ('late_falling',F(2887,2000),F(1,5))]:
            cell=int(np.searchsorted(native.nodes,float(s),side='right')-1)
            q=interval.box(cell,s,s,xi,xi,angle_unit='radians',side='right')
            approximate=native.evaluate_native(float(s),float(xi),side='right')
            comparisons=[]
            for j,name in enumerate(('n','m','l')):
                for attr,suffix in [('value',''),('s','_x'),('xi','_xi'),('xixi','_xixi'),('sxi','_x_xi')]:
                    value=float(np.asarray(approximate[name+suffix]))
                    v=getattr(q['fields'][j],attr);lo,hi=ends(v)
                    discrepancy=max(abs(value-float(lo)),abs(value-float(hi)))
                    maximum_absolute=max(maximum_absolute,discrepancy)
                    maximum_scaled=max(maximum_scaled,discrepancy/max(1.,abs(value)))
                    comparisons.append(dict(field=name,jet=attr,native_value=value,
                        accurate_interval=bound_record(v),endpoint_discrepancy=discrepancy))
            increment=q['fields'][0].value-q['coast_background_fields'][0].value
            if increment.contains(0):
                raise AssertionError('The selected signed change was not proved nonzero')
            records.append(dict(label=label,s_exact=rational_pair(s),xi_exact=rational_pair(xi),
                continuous_point=serialized_box(q),comparisons=comparisons,
                nonzero_signed_increment=bound_record(increment),
                floating_complete_connection=numeric_connection(approximate)))
        # Exactly one positive-size two-dimensional box, in the rising
        # middle window and moving chart, so both w_s and U_s are consumed.
        s,xi=F(363,400),F(7,20);ds,dxi=F(1,2**27),F(1,2**24)
        cell=int(np.searchsorted(native.nodes,float(s),side='right')-1)
        box=interval.box(cell,s-ds,s+ds,xi-dxi,xi+dxi,angle_unit='radians',side='right')
        if box['chart'].U_s.is_zero():
            raise AssertionError('The chosen complete box did not exercise material drift')
        if not any(not v['weight'].s.is_zero() for v in box['signed_components']):
            raise AssertionError('The chosen complete box did not exercise the fixed window derivative')
        cut=interval.accurate_cut_angular(F(1,5),F(1,5),angle_unit='radians')
        if any(v.s is not None or v.sxi is not None for v in cut['fields']):
            raise AssertionError('The exact angular cut acquired an undeclared radial II jet')
        raw=(json.dumps(interval.definition(),sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
        with out['definition'].open('wb') as stream:
            with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as target:
                target.write(raw)
        report.update(native_definition=identity(out['native']),interval_definition=identity(out['definition']),
            interval_binding_sha256=interval.binding_sha256,point_comparisons=records,
            continuous_box=serialized_box(box),
            continuous_box_domain=dict(s=[rational_pair(s-ds),rational_pair(s+ds)],
                xi_radians=[rational_pair(xi-dxi),rational_pair(xi+dxi)]),
            floating_jet_maximum_absolute_discrepancy=maximum_absolute,
            floating_jet_maximum_scaled_discrepancy=maximum_scaled,
            exact_cut=dict(fields=[v.record() for v in cut['fields']],
                radial_II_jets_assigned=False,additional_signed_windows_zero=True),
            defining_input_unchanged=identity(args.field)==report['field'],
            actual_complete_all_three_forcing_components=True)
        if not report['defining_input_unchanged']:
            raise AssertionError('The actual defining archive changed')
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        out['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(out['report']),
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib']),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--origin',type=Path,required=True)
    parser.add_argument('--foundation-definition',type=Path,required=True)
    parser.add_argument('--profile-packet',type=Path,required=True)
    parser.add_argument('--profile-sha256',required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    run(parser.parse_args())
