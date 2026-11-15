#!/usr/bin/env python3
"""True endpoint and infinite-high output Grams of the exact97-input adjoint trial."""
from __future__ import annotations
import argparse,hashlib,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_cap_adjoint_residual_Gram_core as core
import fourfold_codazzi_cap_adjoint_residual_Gram_pilot as pilot
import fourfold_codazzi_cached_cap_adjoint_proposal_v2 as original
from fourfold_codazzi_physical_cap_coefficient_jets import weighted_amplitude_norm,bsum
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,arb_box,reduce_box,complex_sincos
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record
from fourfold_codazzi_cap128_CI_worker import read,digest

KIND='actual_same97_adjoint_true_endpoints_and_complete_high_output_Grams_v1'
CORE='689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc'
PILOT_SOURCE='ae3b90c15e65343a0d5bdeb80cba4d6eb2a6f519155bff9a175b0f48a2f72310'
PILOT_NATIVE='eb58b97ae182cedf621c4ff122b421ffb844e3839266a6a7d6df86b9134d8cfb'
PILOT_WORKER='3f7c1f5862530cf13bda0a30466fc16998ef2a1f0f60ab97a8e5bc9506d81222'
PILOT_MANIFEST='467cd31f6d62b834d3a0cf07a1ef92efe1a2ef218e27d862140122c37a9ce71f'
REFERENCE='ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b'
Q_NATIVE='2f2469091ae6893b56f869fc7753ed015cf9d7ebf2171ccd8c5a580dd770d4d2'
N,K,HIGH,INPUTS=4096,512,97,97
RHO=Fraction(1,16)
save=pilot.save
gate=pilot.gate
canonical=pilot.canonical


def exact_identity(a,paths,pd):
    return dict(original_inputs={k:digest(v) for k,v in paths.items()},
        actual_proposal_native_sha256=digest(a.proposal),actual_proposal_process_sha256=digest(a.proposal_process),
        actual_proposal_array_receipts=pd['proposal_array_receipts'],
        original_complete_Hessian_local_native_sha256=digest(a.local),
        original_complete_physical_background_native_sha256=digest(a.background),
        core_source_sha256=digest(core.__file__),pilot_indices=list(pilot.PILOT))


def validate_pilot(a,identity,doc):
    d,p=read(a.pilot),read(a.pilot_process)
    if (digest(a.pilot)!=PILOT_NATIVE or d.get('kind')!=pilot.KIND or d.get('source_sha256')!=PILOT_SOURCE
        or d.get('exact_identity')!=identity or not d.get('complete') or d.get('failure')
        or len(d.get('gates',[]))!=9 or not all(x.get('passed') for x in d['gates'])
        or str(p.get('run_id'))!='43664278200' or str(p.get('run_attempt'))!='1'
        or p.get('worker_source_sha256')!=PILOT_WORKER or p.get('input_manifest_sha256')!=PILOT_MANIFEST
        or not any(x.get('sha256')==PILOT_NATIVE for x in p.get('native_files',[]))
        or not any(x.get('label')=='four_actual_closed_quarters_complete97_ordinary_adjoint_and_Hessian_Grams'
            and x.get('actual_returncode')==0 for x in p.get('children',[]))):
        raise ValueError('the same actually successful complete-input residual pilot is required')
    gate(doc,'same_exact_proposal_centre_input_basis_and_successful_body_pilot',True)


def boundary_values(nodes,state,dl,dr):
    if nodes[0]<core.LEFT or nodes[-1]!=core.RIGHT:
        raise ValueError('the original true endpoint convention changed')
    poly,_=core.hermite_series(state[0],state[1],dl[0],dr[0],nodes[0],nodes[1],core.LEFT,core.LEFT)
    if len(poly)!=4 or any(v.lo.shape!=(257,97) for v in poly):
        raise ValueError('the first exact complete Hermite polynomial changed dimensions')
    left=poly[0];right=Box(np.asarray(state[-1],dtype=float))
    return left,right


def point_background(candidate,repair,row):
    cached=core.CachedCoefficientProvider(candidate,repair);p=cached.provider
    if row['request']!=[0,4,0] or Fraction(row['interval'][0])!=core.LEFT:
        raise ValueError('the original first true closed quarter is required')
    left,right=map(Fraction,row['interval'])
    germ=tuple(map(Fraction,row['actual_scalar_germ']))
    piece=bisect_right(p.knots,core.LEFT)-1
    if not (germ[0]<=core.LEFT<=right<=germ[1] and p.knots[piece]<=core.LEFT<=p.knots[piece+1]):
        raise ValueError('the saved whole intrinsic jets do not cover the true endpoint')
    whole={k:box_from_record(v) for k,v in row['all_original_target_coefficients'].items()}
    jets=p.local_jets(piece,core.LEFT,core.LEFT,whole)
    p.N=N;p.cutoff=K;p.width=RHO
    seed=zeros((N,128))
    for j in range(128):seed[j+1,j]=1.
    roots=p.fft.fft(seed,inverse=True)*N;p.roots=roots[:,:32]
    analytic=p.analytic_bounds(jets)
    if not (analytic['psi']<exact_arb(RHO) and analytic['psi_phi']<1 and analytic['mean_gap']>0):
        raise ArithmeticError('the complete true inverse Picard self-map or contraction failed')
    return cached,p,jets,analytic,roots,dict(
        exact_endpoint='9/10',original_first_quarter_sha256=canonical(row),
        original_whole_jet_sha256=canonical(row['all_original_target_coefficients']),
        original_actual_scalar_germ=row['actual_scalar_germ'],candidate_piece=piece,
        new_intrinsic_target_calls=0,
        actual_inverse_Picard_selfmap=record(analytic['psi']),
        actual_inverse_Picard_contraction=record(analytic['psi_phi']),
        inverse_displacement_A_rho_bound=record(analytic['psi']),
        exact_physical_analytic_width=str(RHO),analytic_gap=record(analytic['mean_gap']))


def inverse_angle_samples(p,jets):
    """Floating centres followed by exact directed signs and interval Newton."""
    coeff=(jets['psi'][0].lo+jets['psi'][0].hi)/2
    theta=np.arange(N)*np.pi/(2*N);x=np.zeros(N)
    for _ in range(12):
        phase=(theta+x)[:,None]*p.freq
        value=x+np.sin(phase)@coeff
        deriv=1+np.cos(phase)@(coeff*p.freq)
        x-=value/deriv
    radius=2.**-34;accepted=False
    for _ in range(10):
        left=np.nextafter(x-radius,-np.inf);right=np.nextafter(x+radius,np.inf)
        low=Box(left)+p.sine(jets['psi'][0],p.trig(Box(left)))
        high=Box(right)+p.sine(jets['psi'][0],p.trig(Box(right)))
        if np.all(low.hi<0) and np.all(high.lo>0):
            accepted=True;break
        radius*=8
    if not accepted:raise ArithmeticError('the true inverse endpoint brackets failed')
    X=Box(left,right)
    for _ in range(4):
        mid=np.minimum(np.maximum(X.lo/2+X.hi/2,X.lo),X.hi)
        F=Box(mid)+p.sine(jets['psi'][0],p.trig(Box(mid)))
        J=1+p.sine(jets['psi'][0],p.trig(X),1)
        if not np.all(J.lo>0):raise ArithmeticError('the exact real inverse derivative is not positive')
        Z=Box(mid)-F/J;lo=np.maximum(X.lo,Z.lo);hi=np.minimum(X.hi,Z.hi)
        if np.any(lo>hi):raise ArithmeticError('the true inverse Newton intersection is empty')
        X=Box(lo,hi)
    J=1+p.sine(jets['psi'][0],p.trig(X),1)
    return X,dict(initial_sign_bracket_radius=radius,
        maximum_final_inverse_width=float(np.max((X.hi-X.lo))),
        minimum_true_inverse_node_J_lower=float(np.min(J.lo)))


def shifted_trig(roots,shift):
    frequencies=Box(4*np.arange(1,129,dtype=float)).reshape(1,128)
    phase=shift.reshape(N,1)*frequencies;halvings=0
    while np.max(phase.abs_upper())>=2:
        phase=phase/2;halvings+=1
        if halvings>20:raise ArithmeticError('the actual trigonometric shift is not finite at a usable scale')
    sn,cs=complex_sincos(CBox(phase));unit=CBox(cs.real,sn.real)
    for _ in range(halvings):unit=unit*unit
    exp=roots*unit
    return exp.imag,exp.real


def odd_imaginary(dft,first,last):
    outlo=np.empty((last-first+1,INPUTS));outhi=np.empty_like(outlo)
    for j in range(first,last+1):
        pos,neg=dft.imag[j],-dft.imag[-j]
        lo=np.maximum(pos.lo,neg.lo);hi=np.minimum(pos.hi,neg.hi)
        if np.any(lo>hi):raise ArithmeticError('the complete odd Fourier parity enclosures disagree')
        outlo[j-first]=lo;outhi[j-first]=hi
    return Box(outlo,outhi)


def column_tail_matrix(bounds,alias_divisor=1,tail_divisor=1):
    rho=exact_arb(RHO)
    alias_factor=(-4*rho*(N-K)).exp()/alias_divisor
    tail_factor=(-4*rho*(K+1)).exp()/tail_divisor
    totals=[(x*(alias_factor+tail_factor)).upper() for x in bounds]
    hs2=sum((x*x for x in totals),arb(0)).upper()
    G=core.scale_matrix(Box(np.eye(INPUTS)),hs2)
    return G,dict(complete_analytic_column_norms=[record(x) for x in bounds],
        complete_alias_factor=record(alias_factor),complete_tail_factor=record(tail_factor),
        full_column_error_L2_uppers=[record(x) for x in totals],
        complete_unknown_remainder_HS_squared=record(hs2),
        no_spurious_retained_mode_count_factor=True,
        unknown_column_errors_not_assumed_orthogonal=True)


def pair_endpoint_Gram(odd,mean):
    return core.scale_matrix(core.gram_rows(odd),arb(1)/2)+core.gram_rows(mean.reshape(1,INPUTS))


def assign_box(destination,key,value):
    value=Box.coerce(value)
    destination.lo[key]=value.lo;destination.hi[key]=value.hi


def left_Grams(p,jets,analytic,roots,left):
    X,inversion=inverse_angle_samples(p,jets)
    sine,_=shifted_trig(roots,X)
    target=Box(np.zeros((N,INPUTS)))
    assign_box(target,(slice(None),slice(0,96)),jets['mean'][0]*arb_box(arb(2).sqrt())*sine[:,:96])
    dft=p.fft.fft(CBox(target))/N
    finite_target=-2*odd_imaginary(dft,1,K)
    exact=Box(np.zeros((K,INPUTS)));assign_box(exact,slice(0,128),left[:128])
    defect=exact-finite_target
    mean_target=np.zeros(INPUTS);mean_target[96]=1
    mean=left[128]-Box(mean_target)
    finite=pair_endpoint_Gram(defect,mean)
    mabs=arb(float(jets['mean'][0].abs_upper())).upper();P0=analytic['psi']
    bounds=[(mabs*arb(2).sqrt()*(4*j*(exact_arb(RHO)+P0)).exp()).upper()
        for j in range(1,97)]+[arb(0)]
    remainder,fees=column_tail_matrix(bounds)
    complete,weights=core.cauchy_Gram([('finite_true_left_defect',1,finite),
        ('all_inverse_composition_alias_and_infinite_tail',1,remainder)])
    extras=dict(left_finite_nonmean_defect_lower=defect.lo,left_finite_nonmean_defect_upper=defect.hi,
        left_independent_mean_defect_lower=mean.lo,left_independent_mean_defect_upper=mean.hi,
        true_inverse_displacement_lower=X.lo,true_inverse_displacement_upper=X.hi)
    return dict(W_L=complete,W_L_finite=finite,W_L_full_tail=remainder),dict(
        true_left='9/10',inverse=inversion,full_alias_and_tail=fees,complete_Young_weights=weights,
        independent_mean_target_input=96,physical_nonmean_square_weight='1/2',
        physical_even_mean_square_weight='1'),extras


def directed_product(samples,coefficients):
    """All signed columns; every finite product and reduction is directed."""
    samples=Box.coerce(samples);coefficients=Box.coerce(coefficients)
    if samples.lo.shape!=(N,128) or coefficients.lo.shape!=(128,INPUTS):
        raise ValueError('a complete128 by97 physical derivative composition is required')
    lo=np.empty((N,INPUTS));hi=np.empty_like(lo)
    for first in range(0,N,16):
        count=min(16,N-first)
        part=reduce_box(samples[first:first+count].reshape(count,128,1)
            *coefficients.reshape(1,128,INPUTS),1)
        lo[first:first+count]=part.lo;hi[first:first+count]=part.hi
    return Box(lo,hi)


def high_Grams(p,jets,roots,left):
    zero=Box(np.zeros(N));trig=p.trig(zero)
    u=p.sine(jets['u'][0],trig)
    v=jets['s'][0]+p.cosine(jets['dv'][0],trig)
    if not np.all(v.hi<0):raise ArithmeticError('the real endpoint reciprocal v lost its actual negative gap')
    psi=p.sine(jets['psi'][0],trig)
    forward_sine,_=shifted_trig(roots,psi)
    derivative=-left[129:]*Box(4*np.arange(1,129,dtype=float)).reshape(128,1)
    composed=directed_product(forward_sine,derivative)
    fprime=Box(np.zeros((N,INPUTS)))
    assign_box(fprime,(slice(None),slice(0,96)),arb_box(arb(2).sqrt())*roots.real[:,:96]
        *Box(4*np.arange(1,97,dtype=float)).reshape(1,96))
    minv=jets['mean'][0].reciprocal()
    forcing=(u/v).reshape(N,1)*fprime+(minv*minv)*composed
    dft=p.fft.fft(CBox(forcing))/N
    high=2*odd_imaginary(dft,HIGH,K)/Box(4*np.arange(HIGH,K+1,dtype=float)).reshape(K-HIGH+1,1)
    finite=core.scale_matrix(core.gram_rows(high),arb(1)/2)
    U=weighted_amplitude_norm(jets['u'][0],p.freq,RHO)
    V=weighted_amplitude_norm(jets['dv'][0][1:],p.freq,RHO)
    psiA=weighted_amplitude_norm(jets['psi'][0],p.freq,RHO)
    mgap=arb(float(-jets['mean'][0].hi)).lower();gap=(mgap-V).lower()
    if not gap>0:raise ArithmeticError('the complete complex reciprocal v is not enclosed on the analytic strip')
    column=[]
    magnitudes=left[129:].abs_upper()
    for j in range(INPUTS):
        field=arb(0)
        if j<96:
            freq=4*(j+1)
            field=U/gap*arb(2).sqrt()*freq*(freq*exact_arb(RHO)).exp()
        composed_bound=sum((arb(float(magnitudes[k-1,j]))*(4*k)
            *(4*k*(exact_arb(RHO)+psiA)).exp() for k in range(1,129)),arb(0))
        column.append((field+composed_bound/(mgap*mgap)).upper())
    remainder,fees=column_tail_matrix(column,4*HIGH,4*(K+1))
    complete,weights=core.cauchy_Gram([('all_retained_moving_high_trial_outputs',1,finite),
        ('all_unretained_composition_and_alias_primitive_outputs',1,remainder)])
    extras=dict(known_high_even_amplitude_lower=high.lo,known_high_even_amplitude_upper=high.hi)
    return dict(W_T=complete,W_T_finite=finite,W_T_full_tail=remainder),dict(
        lowest_moving_high_index=HIGH,retained_moving_high_indices=[HIGH,K],
        true_complete_high_output_is_not_truncated=True,
        actual_analytic_u=record(U),actual_analytic_v_nonmean=record(V),
        actual_analytic_displacement=record(psiA),actual_analytic_reciprocal_gap=record(gap),
        full_alias_and_tail=fees,complete_Young_weights=weights,
        independent_mean_input_retained_in_all_zC_nonmean_amplitudes=True,
        exact_formula='P_H I_phi[(u/v) f_phi + m^-2 (zC_theta composed with Theta)]'),extras


def outer_Grams(reference,qnative,qvector,right):
    if (not reference.get('complete') or reference.get('exact_interval')!=['9/10','25/8']
        or not reference.get('complete_unknown_Fourier_modes')
        or not qnative.get('complete') or not qnative.get('whole_affine_parameter_interval')
        or qnative.get('object_sha256')!=qvector.get('object_sha256')):
        raise ValueError('the original complete reference and true regular qstar enclosure are required')
    qs=box_from_record(qnative['bounds']['actual_qstar'])
    comparison=core.positive(reference['bounds']['historical_to_current_outer_q_comparison'])
    if not comparison>0:raise ArithmeticError('the actual old/current reference comparison fee may not be erased')
    qlower=(qs.lower()-comparison).lower();qupper=(qs.upper()+comparison).upper()
    qref=arb_box(qlower.union(qupper))
    B=right[:128];C=right[129:];mean=right[128]
    defect=C-qref*B
    WR=core.scale_matrix(core.gram_rows(defect),arb(1)/2)
    WRB=core.scale_matrix(core.gram_rows(B),arb(1)/2)
    WR0=core.gram_rows(mean.reshape(1,INPUTS))
    original_LD=core.positive(reference['bounds']['true_outer_DN_L2_derivative'])
    original_L0=core.positive(reference['bounds']['true_outer_mean_derivative'])
    LD=max(original_LD,(exact_arb(Fraction(5898255,10**12))+comparison).upper()).upper()
    L0=max(original_L0,exact_arb(Fraction(7372818,10**13)).upper()).upper()
    if not (LD.is_finite() and L0.is_finite()):
        raise ArithmeticError('the complete positive outer DN or independent mean fee is not finite')
    extras=dict(true_outer_defect_lower=defect.lo,true_outer_defect_upper=defect.hi)
    return dict(W_R=WR,W_RB=WRB,W_R0=WR0),dict(
        true_right='25/8',complete_reference_q_interval=record(qlower.union(qupper)),
        original_complete_qstar=record(qs),strictly_positive_historical_comparison=record(comparison),
        all128_reference_rows_retained=True,outer_DN_LD=record(LD),outer_mean_L0=record(L0),
        original_floating_proposal_q_not_identified_with_reference=True,
        original_outer_DN_LD=record(original_LD),original_outer_mean_L0=record(original_L0),
        physical_q_units='same actual_qstar and q_values as the frozen packed_v5 boundary_error, physical b+q c',
        comparison_fee_not_subtracted_from_LD=True),extras


def complete_constants(local,jets,p):
    if (not local.get('complete') or local.get('derived_definition_sha256')!=core.CENTRE
        or not all(x.get('passed') for x in local.get('gates',[]))):
        raise ValueError('the original complete repaired Hessian/Green native is required')
    corrected=core.positive(local['original_closed_physical_Green_gains']['inner_C_port'])
    chi=core.positive(local['original_complete_bridge_feedback'])
    base=exact_arb(Fraction(13316116,10**6));threshold=exact_arb(Fraction(3840162,10**9))
    if not (corrected<base and chi<threshold and threshold<1):
        raise ArithmeticError('the original full repaired Green/Hessian constants failed their genuine gates')
    mabs=arb(float(jets['mean'][0].abs_upper())).upper()
    mgap=arb(float(-jets['mean'][0].hi)).lower()
    V0=weighted_amplitude_norm(jets['dv'][0][1:],p.freq,Fraction(0))
    V1=weighted_amplitude_norm(jets['dv'][0][1:],p.freq,Fraction(0),1)
    gap=(mgap-V0).lower()
    if not gap>0:raise ArithmeticError('the complete real even map lost its reciprocal denominator')
    C=(1/gap).upper();C1=(mabs*V1/gap**3).upper()
    J=(1+V0/mgap).upper()
    cstar2=(J*(C*C+C1*C/4)**2).upper()
    return dict(corrected_original_inner_C_port=record(corrected),
        original_complete_Hessian_feedback=record(chi),
        full_repaired_cap_kappa=record((base/(1-threshold)).upper()),
        same_repaired_centre_definition_sha256=core.CENTRE,
        actual_true_left_complete_even_map_norm_squared=record(cstar2),
        actual_true_left_C_sup=record(C),actual_true_left_Ctheta_sup=record(C1),
        actual_true_left_theta_phi_upper=record(J),
        actual_true_left_v_gap=record(gap),actual_true_left_mean_gap=record(mgap),
        actual_true_left_mean_abs_upper=record(mabs))


def verify_stage(stage,root):
    receipt=stage['array_receipt'];path=root/pilot.valid_relative(receipt['file'])
    if path.stat().st_size!=receipt['bytes'] or digest(path)!=receipt['sha256']:
        raise ValueError('one previously successful complete endpoint/high Gram array changed')
    with np.load(path,allow_pickle=False) as z:
        for key,item in stage['complete_signed97_Gram_receipts'].items():
            if item['dimension']!=97 or z[item['array_key']].shape!=(4753,):
                raise ValueError('one saved boundary/high Gram lost a complete input coordinate')


def new_stage(name,make,root):
    started=time.monotonic();grams,metadata,arrays=make()
    receipts={};traces={}
    for key,G in grams.items():
        bounded,receipt=core.covariance_enclosure(G,key,arrays)
        receipts[key]=receipt;traces[key]=record(core.matrix_trace(bounded))
    path=root/('true-adjoint-'+name+'-Grams.npz')
    array=pilot.save_npz(path,arrays)
    return dict(stage=name,complete=True,complete_signed97_Gram_receipts=receipts,
        complete_Gram_trace_uppers=traces,metadata=metadata,array_receipt=array,
        seconds=time.monotonic()-started)


def run(a,doc):
    paths,rows,_=original.load_inputs(SimpleNamespace(input_index=a.input_index),doc)
    pd,nodes,state,dl,dr=pilot.exact_proposal(a,{k:digest(v) for k,v in paths.items()},doc)
    for path,expected in ((a.local,core.LOCAL),(a.background,core.BACKGROUND),
        (a.reference,REFERENCE),(a.q_native,Q_NATIVE)):
        if digest(path)!=expected:raise ValueError('one complete original cap boundary input changed')
    identity=exact_identity(a,paths,pd);validate_pilot(a,identity,doc)
    identity.update(reference_cap_native_sha256=digest(a.reference),true_regular_qstar_native_sha256=digest(a.q_native),
        original_pilot_native_sha256=digest(a.pilot),original_pilot_process_sha256=digest(a.pilot_process),
        actual_analytic_width=str(RHO),directed_grid=N,retained_output_cutoff=K)
    left,right=boundary_values(nodes,state,dl,dr)
    gate(doc,'both_true_endpoints_use_the_same_complete_original_Hermite_trial',True)
    cached,p,jets,analytic,roots,point=point_background(paths['candidate'],paths['repair'],rows[0])
    gate(doc,'complete_inverse_Picard_selfmap_and_contraction_not_displacement_alone',
        analytic['psi']<exact_arb(RHO) and analytic['psi_phi']<1)
    reference,qnative,qvector=read(a.reference),read(a.q_native),read(paths['q-vector'])
    constants=complete_constants(read(a.local),jets,p)
    gate(doc,'full_repaired_Green_Hessian_and_complete_even_map_constants_retained',True)
    doc.update(exact_identity=identity,exact_identity_sha256=canonical(identity),stages=[],
        completed_stages=0,exact_true_endpoints=['9/10','25/8'],point_background_receipt=point,
        original_trial_node_count=len(nodes),all_internal_exact_physical_value_jumps_zero=True,
        original_one_sided_derivatives_remain_independent=True,complete_constants=constants,
        scope='same fixed physical eta0 and original nu, complete repaired M32 delta0, reflection odd/even',
        original_intrinsic_target_calls=0,old_adjoint_trial_recomputed=False,
        complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False)
    a.arrays.mkdir(parents=True,exist_ok=True)
    names=('left','outer','high')
    if a.resume:
        old=read(a.resume)
        if (old.get('kind')!=KIND or old.get('source_sha256')!=digest(__file__)
            or old.get('exact_identity')!=identity or old.get('failure')):
            raise ValueError('resume requires the exact original successful endpoint/high stages')
        for index,stage in enumerate(old.get('stages',[])):
            if index>=len(names) or stage.get('stage')!=names[index] or not stage.get('complete'):
                raise ValueError('the original successful stage order changed')
            verify_stage(stage,a.arrays);doc['stages'].append(stage)
    doc['reused_completed_stages']=len(doc['stages']);doc['completed_stages']=len(doc['stages'])
    save(a.out,doc)
    makers=dict(left=lambda:left_Grams(p,jets,analytic,roots,left),
        outer=lambda:outer_Grams(reference,qnative,qvector,right),
        high=lambda:high_Grams(p,jets,roots,left))
    for name in names[len(doc['stages']):]:
        item=new_stage(name,makers[name],a.arrays);doc['stages'].append(item)
        doc['completed_stages']=len(doc['stages']);save(a.out,doc)
        print(json.dumps(dict(actual_stage=name,complete=True,Grams=item['complete_Gram_trace_uppers'],
            original_targets_recomputed=0)),flush=True)
    gate(doc,'all_true_left_outer_mean_and_complete_infinite_high_output_Grams_exist',
        [s['stage'] for s in doc['stages']]==list(names))
    gate(doc,'all97_inputs_and_all128_physical_trial_modes_retained',True)
    gate(doc,'no_intrinsic_target_scalar_domain_native_point_or_adjoint_trial_recomputed',cached.old_target_calls==0)
    doc.update(complete=True,mathematical_certificate_for_true_endpoints_and_trial_high_output=True,
        body_ordinary_source_Gram_still_requires_all7908_actual_quarters=True,
        unknown_high_operator_not_replaced_by_a_finite_output_cutoff=True,
        complete_full_cap_high_to_low_bound_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('input-index','proposal','proposal-process','proposal-arrays','pilot','pilot-process',
        'local','background','reference','q-native','arrays','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--resume',type=Path)
    a=ap.parse_args();ctx.prec=256;ctx.cap=6;start=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual complete endpoint/high attempt')
    if digest(core.__file__)!=CORE or digest(pilot.__file__)!=PILOT_SOURCE:
        raise ValueError('the exact successful physical normalization/core inputs changed')
    doc=dict(kind=KIND,source_sha256=digest(__file__),repository=original.PUBLIC,
        core_source_sha256=CORE,complete=False,failure=None,gates=[],stages=[])
    try:run(a,doc)
    except Exception as error:doc['failure']=dict(type=type(error).__name__,message=str(error))
    finally:doc['seconds']=time.monotonic()-start;save(a.out,doc)
    print(json.dumps({k:doc.get(k) for k in ('kind','complete','failure','gates','seconds','completed_stages')}),flush=True)
    if doc['failure']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
