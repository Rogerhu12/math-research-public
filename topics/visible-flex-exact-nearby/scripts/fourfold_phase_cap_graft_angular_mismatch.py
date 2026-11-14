#!/usr/bin/env python3
"""Complete-parameter natural-graft and true Robin mismatch derivative Grams.

This evaluates the actual C4 graft by infinite-angle Wiener majorants and
keeps the regular input columns. It does not turn the old cap gap into an
angular derivative gap. A complete full-cap certificate also needs every
body element from fourfold_phase_cap_angular_mismatch.py.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import math
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox,Box,zeros
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import (
    FiniteTrial,gauss_rule,sha,constant_array,matrix_product,conjugate,hermitian_midpoint)
from fourfold_phase_cap_wiener_box import real_wiener_form,real_part
from fourfold_phase_cap_graft_tail_energy import ExactGraftPoint
from fourfold_phase_natural_exterior_graft import NaturalGraft
from fourfold_phase_finite_tail_DN import finite_tail_entries
from fourfold_phase_cap_wiener_cover import write_json
from fourfold_phase_cap_angular_mismatch import ThetaJet,form_from_unit_angular_jets


def upper(value):
    return abs(value).upper()
def symmetric(radius):
    return arb(0,arb(radius).upper())
def cb(value):
    return CBox.from_acb(acb(value))


def wiener_angular_form(graft,left,right):
    jets=graft.jets(left-3,right-3)
    a=real_part(jets['radius'][0])
    L=real_part(jets['log_radius'][1])
    Lp=2*real_part(jets['log_radius'][2])
    C=real_part(jets['slope_ratio'][0])
    Cp=real_part(jets['slope_ratio'][1])
    beta=[[math.factorial(j)*real_part(v[j]) for v in jets['beta']] for j in range(3)]
    gamma=[[math.factorial(j)*real_part(v[j]) for v in jets['gamma']] for j in range(3)]
    _,paid=real_wiener_form(a,graft.Z_global,L,Lp,C,Cp,beta,gamma)
    ph=[arb(row['ball']) for row in paid['unit_horizontal_primitive_jet']]
    pz=[arb(row['ball']) for row in paid['unit_vertical_primitive_jet']]
    K=arb(paid['true_target_K']['ball'])
    def bound(group,r,t):
        return sum(((4*(k+1))**t*upper(x) for k,x in enumerate(group[r])),arb(0)).upper()
    def angle_jet(group,r,t):
        return ThetaJet(symmetric(bound(group,r,t)),symmetric(bound(group,r,t+1)))
    P=[symmetric(ph[0]),symmetric(ph[0]),symmetric(pz[0])]
    Pr=[symmetric(ph[1]),symmetric(ph[1]),symmetric(pz[1])]
    values,normal,domain=form_from_unit_angular_jets(
        P,Pr,L,C,1/a,a,graft.Z_global,K,
        angle_jet(beta,0,0),angle_jet(gamma,0,0),
        angle_jet(beta,1,0),angle_jet(gamma,1,0),
        angle_jet(beta,0,1),angle_jet(gamma,0,1))
    A,kappa,drift=normal
    for name,value in (('A',A.value),('kappa',kappa.value),
            ('D2',domain['D2']),('H1',domain['H1']),
            ('Fz',domain['Fz']),('W2',domain['W2']),('K',domain['K'])):
        if not value>0:raise ValueError('whole-angle actual graft '+name+' is not positive')
    ra=A.derivative/A.value;rk=kappa.derivative/kappa.value
    off2=A.value/kappa.value*(drift.derivative*drift.derivative)
    comm=((upper(ra+rk)+(upper(ra-rk)**2+4*upper(off2)).sqrt())/2).upper()
    return values,dict(full_Wiener_value_diagnostics=paid,
        true_form_and_inverse_boxes=[ball_record(x.value) for x in values],
        true_physical_angular_derivative_boxes=[ball_record(x.derivative) for x in values],
        full_actual_angular_commutator=ball_record(comm),
        exact_mean_height_enclosure=ball_record(graft.Z_global))


def kernel_matrices(values):
    B=[x.value for x in values[:3]]
    D=[x.derivative for x in values[:3]]
    I=[x.value for x in values[3:]]
    # Variables are R,T,P,Q,DR,DT,DP,DQ.  Every zero below is an exact
    # structural zero, not a small sampled high-frequency coefficient.
    C0=[[B[0],B[1],-1,0,0,0,0,0],
        [B[1],B[2],0,-1,0,0,0,0]]
    C1=[[D[0],D[1],0,0,B[0],B[1],-1,0],
        [D[1],D[2],0,0,B[1],B[2],0,-1]]
    answer=[]
    for C in (C0,C1):
        C=[[arb(x) for x in row] for row in C]
        K=[[I[0]*C[0][i]*C[0][j]
             +I[1]*(C[0][i]*C[1][j]+C[1][i]*C[0][j])
             +I[2]*C[1][i]*C[1][j] for j in range(8)] for i in range(8)]
        answer.append(K)
    return answer


def integrate_kernel(kernel,trial,element,left,right,nodes,weights):
    selected=[[0. for _ in range(8)] for _ in range(8)]
    for i in range(8):
        selected[i][i]=float(kernel[i][i].mid())
        for j in range(i+1,8):
            value=float(((kernel[i][j]+kernel[j][i])/2).mid())
            selected[i][j]=selected[j][i]=value
    if any(not np.isfinite(x) for row in selected for x in row):
        raise ValueError('nonfinite selected exact graft kernel')
    radius=max(sum((abs(kernel[i][j]-arb(selected[i][j])) for j in range(8)),arb(0)).upper()
               for i in range(8))
    active=[i for i in range(8) if any(not kernel[i][j]==0 for j in range(8))]
    center=exact_arb((left+right)/2);half=exact_arb((right-left)/2)
    result=zeros((trial.d,trial.d));trace=arb(0)
    for node,weight in zip(nodes,weights):
        raw=list(trial.coefficients(element,acb(center+half*node)))
        angular=[x*CBox(0.,Box(trial.frequency[:,None])) for x in raw]
        fields=raw+angular
        point=zeros((trial.d,trial.d))
        for i in active:
            for j in active:
                if selected[i][j]:
                    point+=selected[i][j]*matrix_product(
                        conjugate(fields[i]).transpose(1,0),fields[j])
        scale=half*weight
        result+=point*cb(scale)
        point_trace=arb(0)
        for i in active:
            value=(conjugate(fields[i])*fields[i]).sum().to_acb()
            if not value.imag.contains(0):
                raise ValueError('finite Parseval trace lost reality')
            point_trace+=value.real
        trace+=scale*point_trace
    if not trace.is_finite():raise ValueError('nonfinite exact finite trial norm')
    # Every component is a radial polynomial of degree at most two, so the
    # three-point true Gauss rule integrates all finite degree-four products.
    middle,rounding=hermitian_midpoint(result)
    variation=(radius*max(arb(0),trace.upper())).upper()
    return dict(matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
        full_operator_error=ball_record((rounding+variation).upper()),
        full_Wiener_kernel_variation_error=ball_record(variation),
        directed_finite_polynomial_Gauss_and_selection_error=ball_record(rounding),
        full_kernel_interval_radius=ball_record(radius),
        active_exact_polynomial_components=active,
        integrated_complete_trial_component_trace=ball_record(trace.upper()),
        exact_finite_kernel_center=selected)


def true_Robin_mismatch(trial,tail,parameter_interval):
    if tail['input_sha256']!=trial.cache['exact_tail_input_sha256']:
        raise ValueError('the exact finite trial uses different true Robin inputs')
    outer=list(map(Fraction,tail['exact_parameter_interval']))
    if not outer[0]<=parameter_interval[0]<=parameter_interval[1]<=outer[1]:
        raise ValueError('the requested real family exceeds the actual Robin enclosure')
    U=constant_array(trial.V[-trial.n:])
    P=zeros((trial.n,trial.d))
    begin=(trial.nodes-1)*trial.nn
    P[trial.nonzero]=constant_array(trial.flux[begin:begin+trial.nn])
    P[trial.M]=constant_array(trial.flux[trial.nodes*trial.nn])
    gamma=zeros((trial.n,1));inverse=zeros((trial.n,1))
    for index,k in enumerate(range(-trial.M,trial.M+1)):
        if k:
            value=arb(tail['entries'][abs(k)-1]['true_Robin']['ball'])
            if not value>0:raise ValueError('actual Robin eigenvalue is not positive')
            gamma[index,0]=cb(value);inverse[index,0]=cb(1/value)
    mismatch=gamma*U+P
    # Gamma and its inverse act on the complete NONMEAN boundary slot.
    # The regular trace and mean flux remain independent augmented ports.
    mismatch[trial.M]=zeros((trial.d,))
    matrices=[]
    for j in (0,1):
        row=mismatch if j==0 else mismatch*CBox(0.,Box(trial.frequency[:,None]))
        G=matrix_product(conjugate(row).transpose(1,0),inverse*row)
        middle,error=hermitian_midpoint(G)
        matrices.append(dict(
            matrix_middle=[[[float(z.real),float(z.imag)] for z in x] for x in middle],
            full_operator_error=ball_record(error),
            exact_boundary_expression=('sum |Gamma_k U_k+P_k|^2/Gamma_k' if j==0
                else 'sum (4k)^2 |Gamma_k U_k+P_k|^2/Gamma_k'),
            regular_input_columns_retained=True,mean_is_excluded_only_from_Gamma_inverse=True))
    return dict(mismatch=matrices[0],angular_derivative_mismatch=matrices[1],
        true_Robin_report=tail,exact_Robin_angular_commutator_zero=True,
        mean_output_rule='The regular lambda output is still paid from the complete R0 gap; its angular derivative is zero and is not a reason to remove that output.')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trial',type=Path,default=Path(
        'notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--graft-certificate',type=Path,default=Path(
        'notes/2026-11-12-positive-family-natural-graft.json'))
    ap.add_argument('--exterior-certificate',type=Path,default=Path(
        'notes/2026-11-12-actual-exterior-robin-certificate.json'))
    ap.add_argument('--common-parameter',type=Path,default=Path(
        'notes/2026-11-12-common-core-exterior-parameter-interval.json'))
    ap.add_argument('--error-per-length',type=Fraction,default=Fraction(1,10000))
    ap.add_argument('--max-depth',type=int,default=16)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--tail-only',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec,ctx.cap=args.bits,8
    wall,cpu=time.monotonic(),time.process_time()
    rows=[];failed=[];rejected=[]
    report=dict(kind='actual_whole_parameter_graft_and_Robin_mismatch_angular_Gram',
        complete=False,full_cap_complete=False,source_sha256=sha(__file__),
        whole_cap_strong_flux_certified=False)
    def save():
        report.update(intervals=rows,unresolved_intervals=failed,rejected_parent_boxes=rejected,
            CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall)
        write_json(args.out,report)
    save()
    try:
        if args.half_width<0:raise ValueError('negative real parameter interval')
        trial=FiniteTrial(args.trial)
        center=Fraction(trial.report['exact_delta_fraction'])
        parameter=(center-args.half_width,center+args.half_width)
        tail=finite_tail_entries(args.graft_certificate,args.exterior_certificate,
                                 args.common_parameter,trial.M)
        report.update(object_path=str(trial.object_path),object_sha256=sha(trial.object_path),
            exact_center_parameter=str(center),exact_parameter_interval=list(map(str,parameter)),
            exact_parameter_half_width=str(args.half_width),
            trial_report=dict(path=str(args.trial),sha256=sha(args.trial)),
            exact_trial_arrays=trial.report['arrays'],input_columns=trial.d,
            regular_mean_input_retained=True,bits=args.bits,
            requested_exact_radial_interval=['3','25/8'],
            true_Robin_boundary=true_Robin_mismatch(trial,tail,parameter),
            actual_graft_certificate=dict(path=str(args.graft_certificate),sha256=sha(args.graft_certificate)),
            tail_only=args.tail_only)
        if args.tail_only:
            report['complete']=True
            report['scope']='Only the actual complete nonmean Robin mismatch and its physical angular derivative. No body/graft integral or complete cap claim.'
        else:
            graft=(NaturalGraft(trial.object_path,args.half_width,Fraction(1,8))
                   if args.half_width else ExactGraftPoint(trial.object_path))
            nodes,weights=gauss_rule(trial.degree+1)
            if trial.degree!=2:
                raise ValueError('this exact finite kernel rule is for the saved quadratic trial')
            report['true_Gauss_rule']=dict(nodes=list(map(ball_record,nodes)),weights=list(map(ball_record,weights)))
            report['actual_graft_height_enclosure']=ball_record(graft.Z_global)
            for element in range(trial.cells):
                left,right=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
                if right<=3:continue
                if not Fraction(3)<=left<right<=Fraction(25,8):
                    raise ValueError('an exact finite trial crosses a graft interface')
                pending=[(left,right,0)]
                while pending:
                    l,r,depth=pending.pop()
                    try:
                        values,diagnostics=wiener_angular_form(graft,l,r)
                        kernels=kernel_matrices(values)
                        parts=[integrate_kernel(K,trial,element,l,r,nodes,weights) for K in kernels]
                        density=max(arb(x['full_operator_error']['ball']).upper() for x in parts)/exact_arb(r-l)
                        if not density<=exact_arb(args.error_per_length):
                            raise ValueError('full graft mismatch kernel variation exceeds error target')
                        rows.append(dict(exact_radial_interval=[str(l),str(r)],finite_element=element,
                            subdivision_depth=depth,full_continuous_coefficient_gate=diagnostics,
                            mismatch=parts[0],angular_derivative_mismatch=parts[1]))
                    except (ValueError,ZeroDivisionError) as exc:
                        item=dict(exact_radial_interval=[str(l),str(r)],depth=depth,reason=str(exc))
                        if depth==args.max_depth:failed.append(item)
                        else:
                            rejected.append(item);mid=(l+r)/2
                            pending.extend([(mid,r,depth+1),(l,mid,depth+1)])
                    save()
                print(json.dumps(dict(element=element,accepted=len(rows),unresolved=len(failed)),
                    allow_nan=False),flush=True)
                if failed:break
            rows.sort(key=lambda x:Fraction(x['exact_radial_interval'][0]))
            cursor=Fraction(3)
            for row in rows:
                l,r=map(Fraction,row['exact_radial_interval'])
                if l!=cursor:raise ValueError('gap or overlap in the actual graft mismatch cover')
                cursor=r
            report['complete']=not failed and cursor==Fraction(25,8)
            if rows:
                report['whole_graft_angular_commutator_upper']=ball_record(max(
                    arb(row['full_continuous_coefficient_gate']['full_actual_angular_commutator']['ball']).upper()
                    for row in rows))
                report['integrated_graft_operator_errors']={key:ball_record(sum((
                    arb(row[key]['full_operator_error']['ball']).upper() for row in rows),arb(0)).upper())
                    for key in ('mismatch','angular_derivative_mismatch')}
            report['scope']=[
                'Complete requested actual natural graft plus true whole-family Robin boundary, all input columns retained.',
                'Infinite tangent and primitive use real Wiener enclosures; finite trial kernels use exact Parseval and degree-four radial integration.',
                'No complete cap R0/R1 follows without every body interval and the same-family full-domain lift.',
                'The regular mean output remains separate and is not assigned a false Robin eigenvalue.']
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report['dependency_sha256']={name:sha(Path(__file__).with_name(name)) for name in (
        'fourfold_phase_cap_angular_mismatch.py','fourfold_phase_cap_energy_interval.py',
        'fourfold_phase_cap_wiener_box.py','fourfold_phase_cap_graft_tail_energy.py',
        'fourfold_phase_natural_exterior_graft.py','fourfold_phase_finite_tail_DN.py',
        'fourfold_phase_exterior_entry_jet.py','fourfold_phase_beta_parameter_germ.py')}
    save()
    print(json.dumps({key:report.get(key) for key in ('complete','failure',
        'whole_graft_angular_commutator_upper','integrated_graft_operator_errors',
        'CPU_seconds','wall_seconds')},indent=2,allow_nan=False),flush=True)
    if not report['complete']:raise SystemExit(1)


if __name__=='__main__':
    main()
