#!/usr/bin/env python3
"""Collect the complete actual cap mismatch and physical angular derivative.

Every body element, the full natural graft, and the genuine Robin boundary
must be present. The resulting two input Grams and coefficient commutator
give strong high-left-flux errors through the same r=1/4 physical lift.
Only a local parameter comparison on the lift window is needed to transfer
that fixed competitor to the whole real eta family.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
import math
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import FiniteTrial,sha
from fourfold_phase_cap_wiener_cover import read_json,write_json
from fourfold_phase_low_feedback_paid_inputs import norm

KINDS={
 'body':('actual_complete_body_complementary_mismatch_angular_Gram',
         'fourfold_phase_cap_angular_mismatch.py'),
 'graft':('actual_whole_parameter_graft_and_Robin_mismatch_angular_Gram',
          'fourfold_phase_cap_graft_angular_mismatch.py')}
GRAM_KEYS=('mismatch','angular_derivative_mismatch')


def finite(x,name):
    if not x.is_finite():raise ValueError('nonfinite '+name)
    return x


def upper(record,name='majorant'):
    x=finite(arb(record['ball']).upper(),name)
    if not x>=0:raise ValueError('negative '+name)
    return x


def eye(n):
    M=acb_mat(n,n)
    for i in range(n):M[i,i]=1
    return M


def adjoint(M):
    return acb_mat([[M[j,i].conjugate() for j in range(M.nrows())]
                   for i in range(M.ncols())])


def exact_matrix(data,n=None):
    if not isinstance(data,list) or not data or any(len(row)!=len(data[0]) for row in data):
        raise ValueError('invalid saved exact matrix shape')
    if n is not None and (len(data)!=n or len(data[0])!=n):
        raise ValueError('wrong full input Gram shape')
    result=[]
    for row in data:
        out=[]
        for pair in row:
            if len(pair)!=2 or not all(isinstance(t,(int,float)) and math.isfinite(t) for t in pair):
                raise ValueError('nonfinite or nonbinary saved matrix entry')
            out.append(acb(float(pair[0]),float(pair[1])))
        result.append(out)
    return acb_mat(result)


def check_exact_hermitian(M):
    if M.nrows()!=M.ncols() or any(M[i,j]!=M[j,i].conjugate()
        for i in range(M.nrows()) for j in range(M.ncols())):
        raise ValueError('the selected midpoint is not exact Hermitian data')


def serialize(M):
    return [[[ball_record(finite(M[i,j].real,'matrix real')),
              ball_record(finite(M[i,j].imag,'matrix imaginary'))]
             for j in range(M.ncols())] for i in range(M.nrows())]


def select_hermitian(M):
    n=M.nrows();C=acb_mat(n,n);data=[[[0.,0.] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        value=float(M[i,i].real.mid())
        if not math.isfinite(value):raise ValueError('nonfinite selected diagonal')
        C[i,i]=value;data[i][i]=[value,0.]
        for j in range(i+1,n):
            z=(M[i,j]+M[j,i].conjugate())/2
            re,im=float(z.real.mid()),float(z.imag.mid())
            if not math.isfinite(re) or not math.isfinite(im):
                raise ValueError('nonfinite selected offdiagonal')
            C[i,j],C[j,i]=acb(re,im),acb(re,-im)
            data[i][j],data[j][i]=[re,im],[re,-im]
    # Squaring a crossing-zero Arb ball via **2 is deliberately avoided.
    error=arb(0)
    for i in range(n):
        for j in range(n):
            x=abs(M[i,j]-C[i,j]).upper()
            error+=x*x
    check_exact_hermitian(C)
    return C,data,error.sqrt().upper()


def checked_source(report,source):
    if report.get('source_sha256')!=sha(Path(__file__).with_name(source)):
        raise ValueError('actual proof producer changed: '+source)
    for name,digest in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('actual proof dependency changed: '+name)


def check_trial(trial):
    if trial.report['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_cap_moment_space.py')):
        raise ValueError('the exact finite trial producer and P2 basis changed')
    if not trial.report.get('mean_slots_retained'):
        raise ValueError('the regular mean input was removed')
    if trial.degree!=2 or trial.B>trial.M:
        raise ValueError('this collector expects the saved exact P2 trial')
    if not np.array_equal(trial.frequency,4*np.arange(-trial.M,trial.M+1)):
        raise ValueError('the saved frequencies are not exact physical 4k')
    if any(not np.all(np.isfinite(x)) for x in (trial.mesh,trial.V,trial.flux)):
        raise ValueError('nonfinite exact finite trial')
    if (Fraction(float(trial.mesh[0]))!=Fraction(1,4)
            or Fraction(float(trial.mesh[-1]))!=Fraction(25,8)
            or np.any(np.diff(trial.mesh)<=0)):
        raise ValueError('wrong actual full cap mesh')
    left=np.zeros((trial.n,trial.d),complex)
    for j in range(2*trial.B+1):left[trial.M-trial.B+j,j]=1
    right_mean=np.zeros(trial.d,complex);right_mean[-1]=1
    if not np.array_equal(trial.V[:trial.n],left):
        raise ValueError('primal left trace is not the exact stated finite input')
    if not np.array_equal(trial.V[-trial.n+trial.M],right_mean):
        raise ValueError('primal regular trace is not its exact separate input')
    # FiniteTrial's representation has continuous p on all radial seams,
    # p_mean independent of r, and q_k=-p_k,r/(4ik), k!=0. Thus div j=0
    # identically, not by a small sampled PDE residual.
    if trial.nodes!=trial.degree*trial.cells+1:
        raise ValueError('invalid shared radial nodal layout')


def check_identity(report,trial,path,half_width):
    if not report.get('complete') or report.get('unresolved_intervals'):
        raise ValueError('an incomplete complementary mismatch input cannot be collected')
    if report.get('failure'):
        raise ValueError('a failed mismatch report cannot be collected')
    if (report['object_sha256']!=trial.report['object_sha256']
        or report['trial_report']['sha256']!=sha(path)
        or report['exact_trial_arrays']!=trial.report['arrays']
        or report['input_columns']!=trial.d
        or not report['regular_mean_input_retained']):
        raise ValueError('mismatch input belongs to another exact trial or omits a mean column')
    center=Fraction(trial.report['exact_delta_fraction'])
    if (Fraction(report['exact_center_parameter'])!=center
            or Fraction(report['exact_parameter_half_width'])!=half_width
            or list(map(Fraction,report['exact_parameter_interval']))!=
               [center-half_width,center+half_width]):
        raise ValueError('mismatch input has a different whole real parameter family')


def interval_rows(report,left,right,trial,kind):
    rows=sorted(report['intervals'],key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=left
    for row in rows:
        a,b=map(Fraction,row['exact_radial_interval'])
        if a!=cursor or not a<b<=right:
            raise ValueError('a completed actual integral has a gap or overlap')
        element=row['finite_element']
        if not isinstance(element,int) or not 0<=element<trial.cells:
            raise ValueError('unknown exact finite element')
        u,v=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        if not u<=a<b<=v:
            raise ValueError('integrated polynomial belongs to another finite element')
        if kind=='body':
            if not Fraction(1,4)<=u<v<=3:
                raise ValueError('a body report substitutes for the natural graft')
            if report['element']!=element:
                raise ValueError('a body report mixes different exact finite elements')
            lo,hi=map(Fraction,row['actual_common_span'])
            if not lo<=a<b<=hi:raise ValueError('body interval crosses its true scalar germ')
            gate=row['full_continuous_coefficient_gate']
            if not arb(gate['diagonalized_positive_A_lower']['ball'])>0:
                raise ValueError('body form A is not continuously positive')
            if not arb(gate['diagonalized_positive_K_lower']['ball'])>0:
                raise ValueError('body form K is not continuously positive')
        elif not Fraction(3)<=u<v<=Fraction(25,8):
            raise ValueError('a graft report substitutes for a body element')
        cursor=b
    if cursor!=right:raise ValueError('a completed actual integral misses its final endpoint')
    return rows


def add_gram(record,total,fees,n):
    for j,key in enumerate(GRAM_KEYS):
        M=exact_matrix(record[key]['matrix_middle'],n);check_exact_hermitian(M)
        total[j]+=M
        fees[j]+=upper(record[key]['full_operator_error'],'complete Gram error')


def local_uniform_lift(lift_path,comparison_paths,trial,half_width):
    point=read_json(lift_path)
    if (not point.get('complete') or point['kind']!='true_quarter_cut_full_cap_lift_and_dual_gap_contact'
        or point.get('failed') or point['object_sha256']!=trial.report['object_sha256']
        or Fraction(point['exact_delta_fraction'])!=Fraction(trial.report['exact_delta_fraction'])
        or point['exact_physical_interface']!='1/4'):
        raise ValueError('the actual same-cut point lift certificate is incomplete or different')
    checked_source(point,'fourfold_phase_cut_cap_lift.py')
    for path,digest in point['input_sha256'].items():
        if sha(path)!=digest:raise ValueError('point lift input changed: '+path)
    left,right=map(Fraction,point['exact_lift_window'])
    if left!=Fraction(1,4) or not left<right<=3:
        raise ValueError('wrong physical short lift window')
    rows=sorted(point['intervals'],key=lambda row:Fraction(row['exact_radial_interval'][0]))
    cursor=left;resistance=Fraction(0);M=arb(0)
    for row in rows:
        a,b=map(Fraction,row['exact_radial_interval'])
        if a!=cursor or not a<b<=right:raise ValueError('the point lift cover is incomplete')
        A=Fraction(row['exact_alpha_upper'])
        if A<=0:raise ValueError('the exact mean competitor has no positive resistance')
        resistance+=(b-a)/A
        M=max(M,upper(row['matrix_upper'],'point form upper'))
        cursor=b
    if cursor!=right or resistance<=0:raise ValueError('the point lift window is not complete')
    center=Fraction(trial.report['exact_delta_fraction'])
    parameter=[center-half_width,center+half_width]
    comparisons=[];identities=[]
    for path in comparison_paths:
        doc=read_json(path)
        if doc['kind']!='actual_full_parameter_finite_cap_relative_form':
            raise ValueError('a native R111 actual form comparison is required')
        checked_source(doc,'fourfold_phase_cap_parameter_comparison.py')
        if (doc['object_sha256']!=trial.report['object_sha256']
            or Fraction(doc['exact_center'])!=center
            or list(map(Fraction,doc['exact_parameter_interval']))!=parameter):
            raise ValueError('the local lift comparison uses a different actual parameter family')
        identities.append(dict(path=str(path),sha256=sha(path),
            input_global_complete=bool(doc.get('complete')),
            use='Only individually proved accepted body rows on the exact short window are consumed; uncomputed outside intervals are not transferred.'))
        for bad in doc.get('unresolved_intervals',[]):
            if bad.get('kind')=='body':
                a,b=map(Fraction,bad['radial_interval'])
                if max(a,left)<min(b,right):
                    raise ValueError('an unresolved comparison intersects the actual lift window')
        body=[r for r in doc['intervals'] if r['kind']=='body']
        a,b=map(Fraction,doc['requested_body_interval'])
        body.sort(key=lambda r:Fraction(r['radial_interval'][0]));previous=a
        for row in body:
            l,r=map(Fraction,row['radial_interval'])
            if not a<=l<r<=b or l<previous:
                raise ValueError('an accepted R111 row overlaps or leaves its declared body interval')
            previous=r
            e=upper(row['relative_form_error'],'actual local form error')
            if not e<1:raise ValueError('relative form error does not preserve the positive form')
            if max(l,left)<min(r,right):
                comparisons.append((max(l,left),min(r,right),e))
    comparisons.sort(key=lambda x:x[0]);cursor=left;epsilon=arb(0)
    for a,b,e in comparisons:
        if a!=cursor:raise ValueError('overlap or gap in selected local parameter comparisons')
        epsilon=max(epsilon,e);cursor=b
    if cursor!=right:raise ValueError('the whole real eta lift window is not covered')
    # Use ONLY the explicit local regular competitor. A smaller global
    # point-only alternative is not silently transferred to the eta family.
    Exi=((1+epsilon)*exact_arb(1/resistance)).upper()
    result=dict(point_input=dict(path=str(lift_path),sha256=sha(lift_path)),
        actual_parameter_comparison_inputs=identities,
        exact_window=[str(left),str(right)],exact_local_mean_resistance=str(resistance),
        same_window_relative_form_error=ball_record(epsilon),
        uniform_form_upper=ball_record(((1+epsilon)*M).upper()),
        uniform_regular_extension_energy=ball_record(Exi),
        transfer='Only the exact short-window competitors are used. The nonmean ramp is zero and the regular competitor constant outside that window; the entire true nonmean Robin contribution vanishes for both.')
    return result,((1+epsilon)*M).upper(),Exi,right-left


def exact_dual_boundary(trial):
    left=np.zeros((trial.n,trial.d),complex)
    left[trial.nonzero]=trial.flux[:trial.nn]
    left[trial.M]=trial.flux[trial.nodes*trial.nn]
    data=np.vstack((-left,left[trial.M:trial.M+1]))
    matrix=acb_mat([[acb(float(z.real),float(z.imag)) for z in row] for row in data])
    return matrix,[[[float(z.real),float(z.imag)] for z in row] for row in data]


def positive_choice(value):
    x=float(value.mid())
    if not math.isfinite(x) or x<=0:return Fraction(1)
    return Fraction(x)


def high_output_budget(G0,G1,CB,M,Exi,length,dual,trial,N):
    if N<0:raise ValueError('physical high cutoff must be nonnegative')
    n0,n1=norm(G0).upper(),norm(G1).upper()
    if n0>0 and n1>0 and CB>0:
        t=positive_choice(CB*(n0/n1).sqrt())
    else:t=Fraction(1)
    tt=exact_arb(t)
    derivative_major=(1+tt)*G1+(1+1/tt)*(CB*CB)*G0
    frequency=4*(N+1)
    z=min(Fraction(1),length*frequency)
    EN=(M*(1/exact_arb(z)+exact_arb(z)/3)).upper()
    error_major=EN*derivative_major
    error_norm=norm(error_major).sqrt().upper()
    dual_gram=acb_mat(trial.d,trial.d)
    for row,k in enumerate(range(-trial.M,trial.M+1)):
        if abs(k)<=N:continue
        for i in range(trial.d):
            for j in range(trial.d):
                dual_gram[i,j]+=4*abs(k)*dual[row,i].conjugate()*dual[row,j]
    dual_norm=norm(dual_gram).sqrt().upper()
    if N>=trial.M:
        if any(dual_gram[i,j]!=0 for i in range(trial.d) for j in range(trial.d)):
            raise ValueError('an allegedly zero high dual output is not exact zero')
        true_major=error_major;combination=Fraction(0)
    else:
        combination=positive_choice(error_norm/dual_norm) if dual_norm>0 else Fraction(1)
        t2=exact_arb(combination)
        true_major=(1+t2)*dual_gram+(1+1/t2)*error_major
    result=dict(physical_cutoff=N,physical_high_trace_extension_energy=ball_record(EN),
        exact_derivative_Young_parameter=str(t),
        full_input_strong_error_Gram_majorant=serialize(error_major),
        strong_error_operator_upper=ball_record(error_norm),
        exact_finite_high_dual_Gram=serialize(dual_gram),
        exact_finite_high_dual_operator_upper=ball_record(dual_norm),
        high_dual_exactly_zero=N>=trial.M,
        finite_dual_plus_error_Young_parameter=str(combination),
        whole_true_high_Hhalf_Gram_majorant=serialize(true_major),
        whole_true_high_Hhalf_operator_upper=ball_record(norm(true_major).sqrt().upper()),
        physical_frequency_convention='Hdot^(1/2) output squared norm uses sum |4k| |flux_k|^2.')
    return result,Exi*G0


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trial',type=Path,default=Path(
        'notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    ap.add_argument('--body',type=Path,nargs='+',required=True)
    ap.add_argument('--graft',type=Path,required=True)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--point-lift',type=Path,default=Path(
        'notes/2026-11-12-actual-quarter-cut-cap-lift.json'))
    ap.add_argument('--lift-comparison',type=Path,nargs='+',required=True)
    ap.add_argument('--cutoffs',type=int,nargs='+',default=[4,16,64,256])
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    wall,cpu=time.monotonic(),time.process_time()
    report=dict(kind='complete_whole_parameter_cap_complementary_strong_flux',
        complete=False,complete_body_graft_and_true_Robin=False,
        whole_cap_strong_flux_certified=False,source_sha256=sha(__file__),
        actual_global_core_cap_inverse_certified=False,bits=args.bits)
    write_json(args.out,report)
    try:
        if args.half_width<0:raise ValueError('negative parameter radius')
        trial=FiniteTrial(args.trial);check_trial(trial)
        totals=[acb_mat(trial.d,trial.d),acb_mat(trial.d,trial.d)]
        fees=[arb(0),arb(0)];all_body=[];CB=arb(0);inputs=[]
        for path in args.body:
            doc=read_json(path)
            if doc['kind']!=KINDS['body'][0]:raise ValueError('wrong body producer kind')
            checked_source(doc,KINDS['body'][1]);check_identity(doc,trial,args.trial,args.half_width)
            left,right=map(Fraction,doc['requested_exact_radial_interval'])
            rows=interval_rows(doc,left,right,trial,'body')
            inputs.append(dict(path=str(path),sha256=sha(path)))
            for row in rows:all_body.append((row,path))
        all_body.sort(key=lambda item:Fraction(item[0]['exact_radial_interval'][0]))
        cursor=Fraction(1,4)
        for row,path in all_body:
            a,b=map(Fraction,row['exact_radial_interval'])
            if a!=cursor:raise ValueError('the full actual body has an overlap or missing interval')
            add_gram(row,totals,fees,trial.d)
            CB=max(CB,upper(row['full_continuous_coefficient_gate']['full_actual_angular_commutator']))
            cursor=b
        if cursor!=3:raise ValueError('the full actual body has not reached r=3')
        graft=read_json(args.graft)
        if graft['kind']!=KINDS['graft'][0] or graft.get('tail_only'):
            raise ValueError('a tail-only report does not supply the complete graft')
        checked_source(graft,KINDS['graft'][1]);check_identity(graft,trial,args.trial,args.half_width)
        if list(map(Fraction,graft['requested_exact_radial_interval']))!=[Fraction(3),Fraction(25,8)]:
            raise ValueError('the actual graft reports a different full radial interval')
        rows=interval_rows(graft,Fraction(3),Fraction(25,8),trial,'graft')
        inputs.append(dict(path=str(args.graft),sha256=sha(args.graft)))
        for row in rows:
            add_gram(row,totals,fees,trial.d)
            CB=max(CB,upper(row['full_continuous_coefficient_gate']['full_actual_angular_commutator']))
        robin=graft['true_Robin_boundary']
        if (not robin['exact_Robin_angular_commutator_zero']
            or robin['true_Robin_report']['input_sha256']!=trial.cache['exact_tail_input_sha256']):
            raise ValueError('wrong actual infinite-tail angular or family identity')
        add_gram(robin,totals,fees,trial.d)
        majors=[];parts=[]
        for j,key in enumerate(GRAM_KEYS):
            C,data,rounding=select_hermitian(totals[j])
            error=(fees[j]+rounding).upper()
            major=C+error*eye(trial.d)
            majors.append(major)
            parts.append(dict(name=key,exact_selected_Gram_center=data,
                complete_integral_and_selection_operator_error=ball_record(error),
                final_selection_error=ball_record(rounding),
                positive_Gram_majorant=serialize(major),
                complete_operator_upper=ball_record(norm(major).upper())))
        report.update(complete_body_graft_and_true_Robin=True,
            object_sha256=trial.report['object_sha256'],
            exact_center_parameter=trial.report['exact_delta_fraction'],
            exact_parameter_half_width=str(args.half_width),
            exact_parameter_interval=graft['exact_parameter_interval'],
            exact_trial_report=dict(path=str(args.trial),sha256=sha(args.trial)),
            exact_trial_arrays=trial.report['arrays'],
            exact_full_radial_cover=['1/4','25/8'],
            input_reports=inputs,input_columns=trial.d,regular_mean_input_retained=True,
            full_complementary_mismatch_Grams=parts,
            complete_coefficient_angular_commutator_upper=ball_record(CB))
        write_json(args.out,report)
        lift,M,Exi,length=local_uniform_lift(
            args.point_lift,args.lift_comparison,trial,args.half_width)
        dual,dual_data=exact_dual_boundary(trial)
        high=[];regular=Exi*majors[0]
        for N in args.cutoffs:
            row,_=high_output_budget(majors[0],majors[1],CB,M,Exi,length,dual,trial,N)
            high.append(row)
        report.update(complete=True,whole_cap_strong_flux_certified=True,
            actual_uniform_short_window_lift=lift,
            exact_dual_boundary_output=dict(
                physical_modes=list(range(-trial.M,trial.M+1)),
                regular_mean_flux_last=True,matrix_binary64=dual_data),
            complete_high_left_flux_budgets=high,
            complete_regular_flux_error_Gram_majorant=serialize(regular),
            complete_regular_flux_error_operator_upper=ball_record(norm(regular).sqrt().upper()),
            scope=[
                'The same r=1/4 physical cap, whole real parameter interval, all body/graft intervals and genuine Robin tail.',
                'R0 is the full complementary mismatch; R1 differentiates that unweighted mismatch in physical theta.',
                'The full input matrices and every regular input/output slot are retained.',
                'For N below the trial cutoff the exact nonzero high dual output is added, never discarded.',
                'This is a complete cap high-output estimate, not a claim of a full core/cap inverse or nonlinear convergence.'])
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_angular_mismatch.py','fourfold_phase_cap_graft_angular_mismatch.py',
            'fourfold_phase_cap_parameter_comparison.py','fourfold_phase_cut_cap_lift.py',
            'fourfold_phase_cap_energy_interval.py','fourfold_phase_cap_moment_space.py',
            'fourfold_phase_cap_wiener_cover.py',
            'fourfold_phase_low_feedback_paid_inputs.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py')})
    write_json(args.out,report)
    print(json.dumps({key:report.get(key) for key in ('complete','failure',
        'complete_body_graft_and_true_Robin','whole_cap_strong_flux_certified',
        'complete_coefficient_angular_commutator_upper','CPU_seconds')},indent=2),flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':main()
