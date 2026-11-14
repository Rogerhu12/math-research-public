#!/usr/bin/env python3
"""Small R158 native same-function check on the actual zero-injection archive.

All comparisons use common physical (s,u) points. This does not solve a BVP,
integrate a body, certify a continuous residual or bless the old bad field.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import json
import time
import resource
import traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField


def maximum(value):
    return float(np.max(abs(np.asarray(value)),initial=0.))


def comparison(left,right):
    return dict(absolute_maximum=maximum(np.asarray(left)-np.asarray(right)),
        scaled_maximum=maximum(np.asarray(left)-np.asarray(right))/max(1.,maximum(left),maximum(right)))


def packed(value,suffix=''):
    return np.stack([value[name+suffix] for name in ('n','m','l')],axis=-1)


def same_bytes(left,right):
    left,right=np.asarray(left),np.asarray(right)
    return left.dtype==right.dtype and left.shape==right.shape and left.tobytes()==right.tobytes()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','old-field','candidate','inlet','cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh output stem; put external console elsewhere')
    start=time.monotonic();here=Path(__file__).resolve().parent
    names=['fd2d_gc_independent_tail_native_field.py','fd2d-metric-independent-tail-native-check.py',
           'fd2d_gc_nested_angular_positive_trace.py','fd2d_gc_positive_trace_native_field_v2.py']
    sources={name:identity(here/name) for name in names}
    report=dict(schema='fd2d-R158-independent-tail-native-small-check-v1',
        source=sources,field=identity(args.field),original_field=identity(args.old_field),
        candidate=identity(args.candidate),reference_inlet=identity(args.inlet),reference_cache=identity(args.cache),
        status='running',passed=False,no_BVP=True,no_body_integration=True,
        finite_samples_only=True,continuous_certificate=False)
    try:
        a,b=load_npz(args.old_field),load_npz(args.field)
        old=PositiveTraceNativeField(args.old_field,args.candidate,
            reference_inlet=args.inlet,reference_cache=args.cache)
        new=IndependentTailPositiveTraceNativeField(args.field,args.candidate,
            reference_inlet=args.inlet,reference_cache=args.cache)
        embedding=new.angular_embedding_definition
        if embedding is None or embedding['input']['sha256']!=identity(args.old_field)['sha256']:
            raise ValueError('The saved zero injection does not bind this original field')
        k,K=old.K,new.K;nt=new.tail_parameter_count;J=new.profile_count
        copy_checks=dict(mesh=same_bytes(a['mesh'],b['mesh']),supports=same_bytes(a['profile_supports'],b['profile_supports']),
            raw_n=same_bytes(a['corrections'][:,:k+1],b['corrections'][:,:k+1]),
            raw_m=same_bytes(a['corrections'][:,k+1:2*k+1],b['corrections'][:,K+1:K+1+k]),
            raw_l=same_bytes(a['corrections'][:,2*k+1:],b['corrections'][:,2*K+1:2*K+k+2]),
            central=same_bytes(a['parameters'][:k],b['parameters'][:k]),
            tail=same_bytes(a['parameters'][old.tail_parameter_slice],b['parameters'][new.tail_parameter_slice]),
            profile=same_bytes(a['parameters'][old.profile_parameter_slice],b['parameters'][new.profile_parameter_slice]))
        zeros=np.r_[b['parameters'][k:K],b['corrections'][:,k+1:K+1].ravel(),
            b['corrections'][:,K+1+k:2*K+1].ravel(),b['corrections'][:,2*K+k+2:].ravel()]
        copy_checks['new_coefficients_positive_binary_zero']=bool(np.all(zeros==0.) and not np.any(np.signbit(zeros)))
        packets=('seed_weight_definition','coast_reference_definition','angular_atlas_definition',
            'reference_evaluation_definition','gauss_l_definition','positive_trace_definition')
        copy_checks['all_original_complete_definition_packets']=all(json.loads(str(a[key]))==json.loads(str(b[key])) for key in packets)
        if not all(copy_checks.values()):
            raise ValueError('The actual saved archive is not the claimed coefficient-preserving injection')
        if (K,nt,J,len(new.parameters))!=(31,16,7,54):
            raise ValueError('This actual check is explicitly the 31/16/7 input')
        legacy_rejected=False;legacy_message=None
        try:
            PositiveTraceNativeField(args.field,args.candidate,
                reference_inlet=args.inlet,reference_cache=args.cache)
        except ValueError as exc:
            legacy_message=str(exc)
            legacy_rejected='tail K+1' in legacy_message
        u=np.array([0.,.13,np.pi/6,np.pi/2,np.pi,5*np.pi/4])
        ref=new.coast_reference;rim=ref.length*new.reference_rim_fraction
        points=[('central',0.),('coast_rim',ref.entry_s+.5*rim),
            ('coast_plateau',(ref.entry_s+ref.exit_s)/2),
            ('between_windows',(ref.exit_s+new.trace_start)/2),
            ('terminal_rim',(new.trace_start+new.trace_ramp_stop)/2),
            ('terminal_plateau',(new.trace_ramp_stop+new.trace_cut)/2),('exact_cut',new.trace_cut)]
        rows=[];samples={'physical_u':u};max_scaled=0.;max_abs=0.
        for index,(label,s) in enumerate(points):
            qa,qb=old.physical_angular(s,u),new.physical_angular(s,u)
            delta={suffix or 'value':comparison(packed(qa,suffix),packed(qb,suffix))
                for suffix in ('','_u','_uu')}
            metric={key:comparison(qa[key],qb[key]) for key in ('a','a_s','a_ss','J')}
            max_scaled=max(max_scaled,*(q['scaled_maximum'] for q in delta.values()))
            max_abs=max(max_abs,*(q['absolute_maximum'] for q in delta.values()))
            for suffix in ('','_u','_uu'):
                samples[f'old_{index}{suffix}']=packed(qa,suffix)
                samples[f'new_{index}{suffix}']=packed(qb,suffix)
            rows.append(dict(label=label,physical_s=float(s),physical_angular_jets=delta,metric=metric,
                old_inverse_error=maximum(qa['angle_inverse_error']),new_inverse_error=maximum(qb['angle_inverse_error'])))
        native=[]
        xi=np.array([0.,.21,np.pi/6,np.pi/2,np.pi,7*np.pi/6])
        for label,s in (points[2],points[4]):
            qa,qb=old.evaluate_native(s,xi),new.evaluate_native(s,xi)
            differences={suffix or 'value':comparison(packed(qa,suffix),packed(qb,suffix))
                for suffix in ('','_x','_xi','_xixi','_x_xi')}
            max_scaled=max(max_scaled,*(q['scaled_maximum'] for q in differences.values()))
            max_abs=max(max_abs,*(q['absolute_maximum'] for q in differences.values()))
            native.append(dict(label=label,physical_s=s,native_jet_differences=differences))
        cut=new.physical_angular(new.trace_cut,u)
        exact=new.tail.cut_port(u)
        cut_difference=comparison(packed(cut),packed(exact))
        radial_cut_rejected=False
        try:new.evaluate_native(new.trace_cut,xi)
        except ValueError as exc:
            radial_cut_rejected='radial II jets are not claimed' in str(exc)
        definition=stem.with_name(stem.name+'-definition.json')
        meta=new.definition();definition.write_text(json.dumps(meta,indent=2,allow_nan=False)+'\n')
        restored=IndependentTailPositiveTraceNativeField.from_definition(definition)
        reload_error=0.
        for label,s in (points[2],points[-1]):
            qa,qb=new.physical_angular(s,u),restored.physical_angular(s,u)
            reload_error=max(reload_error,*(maximum(packed(qa,suffix)-packed(qb,suffix)) for suffix in ('','_u','_uu')))
        record=save_npz(stem.with_name(stem.name+'-samples.npz'),**samples)
        all_frozen=[q for q in meta['sources']]
        sources_unchanged=all(identity(Path(row['path']))['sha256']==row['sha256'] for row in all_frozen)
        report.update(status='completed',layout=new.explicit_parameter_layout,counts=dict(raw_and_central=K,tail=nt,profile=J,parameters=len(new.parameters)),
            exact_byte_injection_checks=copy_checks,original_packets=packets,
            original_legacy_reader_rejected=legacy_rejected,original_legacy_rejection_message=legacy_message,
            physical_point_count=len(points)*len(u),common_physical_point_checks=rows,
            additional_two_native_interior_checks=native,
            maximum_same_field_scaled_difference=max_scaled,maximum_same_field_absolute_difference=max_abs,
            accurate_tail_value_comparison=cut_difference,accurate_cut_zero_II_sample_count=int(np.count_nonzero(np.all(packed(cut)==0.,axis=-1))),
            exact_cut_radial_jet_rejected=radial_cut_rejected,definition_reload_difference=reload_error,
            definition=identity(definition),samples=record,sources_unchanged=sources_unchanged,
            inherited_spatial_evaluation_source_unchanged=True,
            mathematical_same_function_reason='Exact copied old coefficients plus positive zero high coefficients, unchanged tail Bernstein degree and parameters, same profile/atlas/full lifting and pointwise nonlinear maps (R158)',
            future_nonzero_high_coefficients_supported=True,
            current_embedding_provenance_not_a_future_solution_certificate=True)
        report['passed']=bool(all(copy_checks.values()) and legacy_rejected and radial_cut_rejected
            and max_scaled<2e-11 and cut_difference['scaled_maximum']<2e-12 and reload_error<2e-12 and sources_unchanged)
    except BaseException as exc:
        report.update(status='failed',exception_type=type(exc).__name__,exception=str(exc),traceback=traceback.format_exc())
        print(report['traceback'],flush=True)
    report['seconds']=time.monotonic()-start;report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['new_sources_unchanged']=all(identity(here/name)['sha256']==row['sha256'] for name,row in sources.items())
    if not report['new_sources_unchanged']:report['passed']=False
    destination=stem.with_name(stem.name+'-report.json')
    destination.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='independent_tail_native_complete',status=report['status'],passed=report['passed'],seconds=report['seconds'],report=str(destination))),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
