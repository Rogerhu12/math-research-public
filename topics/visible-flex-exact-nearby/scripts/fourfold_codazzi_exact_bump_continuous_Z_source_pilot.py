#!/usr/bin/env python3
"""Exact compact-source coefficients and full continuous-Z residual pilot.

The same scalar bump is expanded over Fraction before interval evaluation.
All original scalar jets, including the 80 completed fixed-eta calls, are
reused. The raw full mean is retained for Z; qstar is a separate diagnostic.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from bisect import bisect_left,bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_correlated_head_residual_rows import scalar_models
from fourfold_codazzi_correlated_radial_Fourier import RadialFourier,candidate_fields,norms
from fourfold_codazzi_nu_full_adjoint_kernel import operator_action
from fourfold_phase_beta_bulk_box import Box,CBox,DirectedFFT,zeros

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
REPAIR_SOURCE='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
RIGHT=Fraction(25,8);CUT=Fraction(9,10)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
CONTROL_LEFT=Fraction(1,20);CONTROL_RIGHT=Fraction(9,50)
FIXED='a73382575ca2b14afb810c2ed43ae0aec9d59aef563635a19f6785b414111993'
FIXED_SOURCE='51a7f917aeb3849aafb44de17be709664ff19e39b92ca4ee08fbb5df1bbfda7f'
FIXED_WORKER='37a226b90c5989011e9060253e1b676a791df8d77669b9bc11c5c45bd57685e1'
FIXED_MANIFEST='f0fae9a54a8a5655b81c0721bee613e45b4efbbc8549f284317e5ae680449bb8'
Z_NATIVE='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
Z_DEFINITION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temp=path.with_suffix(path.suffix+'.partial');temp.write_bytes(raw);temp.replace(path)


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a projected source enclosure is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def actual(process,run_id):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run_id) and process.get('complete')
        and not process.get('failure') and bool(process.get('children'))
        and all(c.get('actual_returncode')==0 for c in process['children']))


def project(field,low,high):
    """Exact Fourier coordinate projection of the complete polynomial/error."""
    if not 0<=low<=high<field.grid//2:raise ValueError('invalid true finite Fourier projection')
    retained_degree=min(high,field.degree)
    if retained_degree<low:return field.coerce(0)
    z=field.Fourier()
    out=CBox(Box(z.real.lo.copy(),z.real.hi.copy()),Box(z.imag.lo.copy(),z.imag.hi.copy()))
    j=np.arange(field.grid);j=np.where(j<field.grid//2,j,j-field.grid)
    out[(abs(j)<low)|(abs(j)>high)]=0
    # Coordinate projections contract Wiener A0. The retained uniform
    # scalar remainder now has exactly the projected finite support.
    error=field.error if field.error_degree>=low else arb(0)
    return field.from_Fourier(out,retained_degree,error,min(retained_degree,field.error_degree))


def budgets(pair,length):
    return {key:record(value) for key,value in norms(pair,length,Fraction(1,2048)).items()}



def field_stats(field):
    return dict(complete_finite_support=field.degree,complete_remainder_support=field.error_degree,
        polynomial_A0_upper=record(field.norm),complete_uniform_A0_error=record(field.error))


def direct_mean_correction(R,column,ez):
    """Keep cached Fourier boxes; do not lose them through IFFT/sample/FFT."""
    e0=float(ez.mid());e0a=arb(e0);epsilon=abs(ez-e0a).upper()
    output=[]
    for residual,coupling in zip(R,column):
        zr=residual.Fourier();zc=coupling.Fourier()
        length=max(zr.real.lo.shape[1],zc.real.lo.shape[1])
        rr=zeros((residual.grid,length));cc=zeros((residual.grid,length))
        rr[:,:zr.real.lo.shape[1]]=zr;cc[:,:zc.real.lo.shape[1]]=zc
        znew=rr-cc*Box(e0)
        error=(residual.error+abs(e0a)*coupling.error
            +epsilon*(coupling.norm+coupling.error)).upper()
        degree=max(residual.degree,coupling.degree)
        # Including a zero remainder at a larger finite degree is safe.
        edegree=max(residual.error_degree,coupling.error_degree,coupling.degree)
        output.append(residual.from_Fourier(znew,degree,error,edegree))
    return tuple(output),dict(exact_dyadic_mean_reference_hex=e0.hex(),
        whole_interval_distance_to_reference=record(epsilon),
        mean_error_derivative_not_inserted_into_nonmean_rows=True,
        direct_Fourier_linear_combination_without_sample_retransform=True)


def rational_product(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def rational_power(a,n):
    out=[Fraction(1)]
    for _ in range(n):out=rational_product(out,a)
    return out


def exact_compact_source(Q,scalar,left,right):
    """The unchanged exact bump, with coefficient cancellations done first."""
    u,v=Q;zero=u.coerce(0)
    if right<=CONTROL_LEFT or left>=CONTROL_RIGHT:
        return (zero,zero),dict(compact_source_exactly_zero=True)
    if not CONTROL_LEFT<=left<right<=CONTROL_RIGHT:
        raise ValueError('the exact original compact-source piecewise seam was crossed')
    width=CONTROL_RIGHT-CONTROL_LEFT;half=(right-left)/2;mid=(left+right)/2
    t0=(mid-CONTROL_LEFT)/width;t1=half/width
    p=[t0*(1-t0),t1*(1-2*t0),-t1*t1]
    wcoef=[4096*x for x in rational_power(p,6)]
    wrcoef=[(Fraction(24576)/width)*x for x in
        rational_product(rational_power(p,5),[1-2*t0,-2*t1])]
    derivative=[(j+1)*wcoef[j+1]/half for j in range(len(wcoef)-1)]
    if derivative!=wrcoef:
        raise ValueError('the exact original bump radial derivative identity failed')
    w=RadialFourier.scalar([exact(x) for x in wcoef],u.grid,u.fft)
    wr=RadialFourier.scalar([exact(x) for x in wrcoef],u.grid,u.fft)
    beta,K,gamma,T=(scalar[n] for n in ('beta','K','gamma','T'))
    Knu=-K*w+T*wr;m=v.mean();v2=v*v;I=v2.primitive();up=u.derivative();vp=v.derivative()
    source=(-beta*Knu*(I*up+v2*u)+gamma*m*(K*w*.5+Knu)*vp,
        -beta*Knu*(I*vp+v2*v)-(gamma*m*w*.5)*up)
    return source,dict(compact_source_exactly_zero=False,
        exact_original_compact_interval=[str(CONTROL_LEFT),str(CONTROL_RIGHT)],
        exact_local_t_coefficients=list(map(str,(t0,t1))),
        exact_compact_bump_coefficients=list(map(str,wcoef)),
        exact_radial_bump_derivative_coefficients=list(map(str,wrcoef)),
        exact_derivative_coefficient_identity_checked=True,
        every_Arb_and_binary_scalar_coefficient_radius_retained=True,
        bump_model=field_stats(w),radial_derivative_model=field_stats(wr))


def complete_Z_repair_fee(repair,whole,context):
    """Transfer raw full residual to the same continuous Z and repaired Q."""
    Q0=interval(repair['original_background_pair_A0']).upper()
    Q1=interval(repair['original_background_angular_derivative_pair_A0']).upper()
    B=abs(whole['beta']).upper();G=abs(whole['gamma']).upper()
    K=max(arb(1),abs(whole['K']).upper()).upper()
    E0,E1=context['Z_offset_A0'],context['Z_offset_angle_A0']
    a1=(G*K*Q0+B*K*Q0*Q0/4).upper()
    a0=(B*(1+3*K*Q0*Q0)+B*K*Q0*Q1/2+G*K*Q1).upper()
    operator_offset=(a0*E0+a1*E1).upper()
    M0=interval(repair['zero_order_operator_difference_M0']).upper()
    M1=interval(repair['first_order_operator_difference_M1']).upper()
    base_fee=interval(repair['complete_repair_source_pair_A0_sup']).upper()
    extra=(M0*E0+M1*E1).upper();total=(operator_offset+base_fee+extra).upper()
    return total,dict(raw_full_operator_order1_A0_coefficient=record(a1),
        raw_full_operator_order0_A0_coefficient=record(a0),
        whole_interval_Z_minus_raw_A0=record(E0),
        whole_interval_angular_derivative_Z_minus_raw_A0=record(E1),
        raw_operator_applied_to_piecewise_constant_direction_offset=record(operator_offset),
        already_paid_complete_repaired_centre_source_fee=record(base_fee),
        additional_operator_difference_applied_to_direction_offset=record(extra),
        total_complete_Z_source_transfer_A0=record(total),
        original_mean_completed_trial_norm_bound_also_bounds_raw_by_its_Bernstein_construction=True,
        Z_minus_raw_is_constant_in_radius_on_each_original_piece=True,
        full_even_mean_in_Z_residual_retained=True)


def physical_coefficients(pair):
    result=[]
    for component,field in enumerate(pair):
        z=field.Fourier()
        for j in range(0 if component else 1,97):
            value=z[j].real*(1 if j==0 else 2) if component else z[j].imag*(-2)
            result.append(dict(component=component,mode=j,physical_frequency=4*j,
                physical_sine_or_cosine_amplitude_coefficients=[
                    dict(lower_hex=float(a).hex(),upper_hex=float(b).hex())
                    for a,b in zip(value.lo,value.hi)]))
    if len(result)!=193:raise ValueError('the full independent mean or angular slot was removed')
    return result


def projection_at(row,old,repair,background,trial,nodes,alpha,context,left,right,whole,midpoint):
    ci=row['pieces']['background'];hi=row['pieces']['response']
    if not (nodes[ci]<=left<right<=nodes[ci+1] and nodes[hi]<=left<right<=nodes[hi+1]):
        raise ValueError('a source diagnostic crosses an original complete physical cubic')
    scalar=scalar_models(context,left,right,whole,midpoint)
    bg=candidate_fields(background['piece_coefficients'][:,ci],nodes[ci],left,right,32,
        context['grid'],context['fft'],alpha,scalar['s'])
    response=candidate_fields(trial['piece_coefficients'][:,hi],nodes[hi],left,right,96,
        context['grid'],context['fft'])
    Q=(bg[0],bg[1]);h=(response[0],response[1]);hr=(response[4],response[5])
    D=operator_action(Q,h,hr,scalar)
    F,bump_evidence=exact_compact_source(Q,scalar,left,right)
    Rfull=(D[0]-F[0],D[1]-F[1])
    R=(Rfull[0],Rfull[1].nonmean())
    zero=Q[0].coerce(0);one=Q[0].coerce(1)
    negcol=operator_action(Q,(zero,one),(zero,zero),scalar)
    column=(-negcol[0],(-negcol[1]).nonmean())
    # Exact angular support applies to complete scalar remainders too.
    if (any(x.degree>160 or x.error_degree>160 for x in D)
        or any(x.degree>96 or x.error_degree>96 for x in F)
        or any(x.degree>64 or x.error_degree>64 for x in column)):
        raise ValueError('complete D/F/Ae2 angular support changed')
    ez=interval(old['response_mean_error'])
    corrected,mean_contract=direct_mean_correction(R,column,ez)
    low=tuple(project(field,0,96) for field in corrected)
    high=tuple(project(field,97,160) for field in D)
    low_R=tuple(project(field,0,96) for field in R)
    low_C=tuple(project(field,0,96) for field in column)
    length=right-left;width=Fraction(1,2048)
    low_bounds=norms(low,length,width)
    r_bounds=norms(low_R,length,width);c_bounds=norms(low_C,length,width)
    triangle={key:(r_bounds[key]+abs(ez)*c_bounds[key]).upper() for key in r_bounds}
    minima={key:min(low_bounds[key].upper(),triangle[key]).upper() for key in low_bounds}
    fee=interval(repair['complete_repair_source_pair_A0_sup']).upper()
    repaired_sup=(minima['L2_sup']+fee).upper()
    repaired_radial=(minima['L2_L2_radial']+exact(length).sqrt()*fee).upper()
    coefficients=physical_coefficients(low)
    Zlow=tuple(project(field,0,96) for field in Rfull)
    raw_full=norms(Rfull,length,width);raw_low=norms(Zlow,length,width)
    raw_high=norms(high,length,width)
    Zfee,Zfee_evidence=complete_Z_repair_fee(repair,whole,context)
    Zbudgets={}
    for label,raw in (('full_through160',raw_full),('low193',raw_low),('high97_through160',raw_high)):
        Zbudgets[label]=dict(
            L2_sup=record((raw['L2_sup']+Zfee).upper()),
            L2_L2_radial=record((raw['L2_L2_radial']+exact(length).sqrt()*Zfee).upper()))
    return dict(interval=list(map(str,(left,right))),complete_new_enclosure=True,
        same_original_completed_mean_error=old['response_mean_error'],
        exact_compact_source_coefficient_evidence=bump_evidence,
        raw_full_residual_before_any_mean_completion={k:record(v) for k,v in raw_full.items()},
        continuous_Z_complete_residual=Zbudgets,complete_Z_source_transfer_evidence=Zfee_evidence,
        continuous_Z_low193_raw_polynomial_physical_amplitudes=physical_coefficients(Zlow),
        continuous_Z_low193_raw_polynomial_component_A0_remainders=[record(x.error) for x in Zlow],
        continuous_Z_low193_additional_full_pair_A0_remainder=record(Zfee),
        continuous_Z_exact_direction_definition_sha256=Z_DEFINITION,
        continuous_Z_mean_not_set_to_zero=True,
        original_whole_row_complete_nonmean_residual_bound=old['response_complete_nonmean_residual'],
        direct_Fourier_low193_polynomial_with_own_remainders={k:record(v) for k,v in low_bounds.items()},
        independent_separate_low193_triangle_bound={k:record(v) for k,v in triangle.items()},
        minimum_of_two_valid_low193_norm_bounds={k:record(v) for k,v in minima.items()},
        high97_through160_from_complete_D_alone=budgets(high,length),
        low193_uncorrected_trial_residual={k:record(v) for k,v in r_bounds.items()},
        low193_complete_mean_coupling_column={k:record(v) for k,v in c_bounds.items()},
        repaired_low193_complete_residual_L2_sup=record(repaired_sup),
        repaired_low193_complete_residual_L2_radial=record(repaired_radial),
        complete_new_repair_source_pair_A0_sup=repair['complete_repair_source_pair_A0_sup'],
        scalar_model_budgets={key:field_stats(value) for key,value in scalar.items()},
        D_component_budgets=[field_stats(x) for x in D],
        Fnu_component_budgets=[field_stats(x) for x in F],
        Rnon_component_budgets=[field_stats(x) for x in R],
        Ae2_component_budgets=[field_stats(x) for x in column],
        mean_decomposition=mean_contract,
        low193_radial_polynomial_physical_amplitudes=coefficients,
        low_component_uniform_A0_remainders=[record(x.error) for x in low],
        smaller_norm_is_not_substituted_for_the_saved_polynomial_remainder=True,
        known_high_Fnu_and_Ae2_exactly_zero_including_all_scalar_remainders=True,
        original_background_completed_mean_residual_exactly_zero=True,
        repaired_background_independent_mean_residual_retained_in_complete_repair_fee=True)


def row_projection(row,old,repair,background,trial,nodes,alpha,context):
    left,right=map(Fraction,row['interval']);prior=context['fixed_rows'][row['common_row']]
    if (prior['cached_scalar_row_sha256']!=sha_row(row) or prior['interval']!=row['interval']
        or not prior.get('actual_projection_complete')):
        raise ValueError('the previously completed scalar-jet row identity changed')
    whole={key:interval(value) for key,value in row['intrinsic_whole_third_jets'].items()}
    midpoint={key:interval(value) for key,value in row['intrinsic_midpoint_jets'].items()}
    cached=projection_at(row,old,repair,background,trial,nodes,alpha,context,left,right,whole,midpoint)
    fresh=[]
    for original in prior['new_fixed_eta_selected_refinements']:
        subdivisions=original['subdivisions'];children=[];edge=left
        if original['exact_parameter_half_width']!='0' or len(original['children'])!=subdivisions:
            raise ValueError('the original completed fixed-eta subdivision changed')
        for original_child in original['children']:
            lo,hi=map(Fraction,original_child['interval'])
            if lo!=edge or not lo<hi<=right:
                raise ValueError('the actual reused fixed-eta child cover has a gap')
            germ=list(map(Fraction,original_child['actual_new_fixed_eta_target_germ']))
            if not germ[0]<=lo<hi<=germ[1]:
                raise ValueError('the reused exact coefficient interval crosses its germ')
            wh={key:interval(value) for key,value in original_child['actual_new_fixed_eta_whole_third_jets'].items()}
            md={key:interval(value) for key,value in original_child['actual_new_fixed_eta_midpoint_jets'].items()}
            child=projection_at(row,old,repair,background,trial,nodes,alpha,context,lo,hi,wh,md)
            child.update(original_completed_fixed_eta_child_sha256=sha_row(original_child),
                actual_reused_fixed_eta_target_germ=original_child['actual_new_fixed_eta_target_germ'],
                actual_new_target_provider_calls=0)
            children.append(child);edge=hi
        if edge!=right:raise ValueError('the reused fixed-eta cover is incomplete')
        Zbudgets={}
        for name in ('full_through160','low193','high97_through160'):
            Zbudgets[name]=dict(
                L2_sup=record(max(interval(x['continuous_Z_complete_residual'][name]['L2_sup']).upper() for x in children)),
                L2_L2_radial=record(sum((interval(x['continuous_Z_complete_residual'][name]['L2_L2_radial']).upper()**2
                    for x in children),arb(0)).sqrt().upper()))
        upper_sup=max(interval(x['repaired_low193_complete_residual_L2_sup']).upper() for x in children)
        square=sum((interval(x['repaired_low193_complete_residual_L2_radial']).upper()**2 for x in children),arb(0))
        fresh.append(dict(subdivisions=subdivisions,exact_parameter_half_width='0',
            all_previously_completed_fixed_eta_jets_reused=True,new_target_provider_calls=0,
            same_old_complete_eta_mean_error_enclosure_retained=True,
            complete_original_row_covered=True,children=children,
            repaired_low193_complete_residual_L2_sup=record(upper_sup),
            repaired_low193_complete_residual_L2_radial=record(square.sqrt()),
            continuous_Z_complete_residual=Zbudgets))
    return dict(common_row=row['common_row'],interval=row['interval'],pieces=row['pieces'],
        actual_projection_complete=True,cached_scalar_row_sha256=sha_row(row),
        original_completed_fixed_eta_row_sha256=sha_row(prior),
        original_closed_scalar_germ=row['actual_scalar_germ'],
        original_complete_nonmean_residual_bound=old['response_complete_nonmean_residual'],
        exact_bump_cached_complete_eta=cached,reused_fixed_eta_refinements=fresh,
        original_fixed_eta_cached_direct_low193_sup=
            prior['direct_Fourier_cached_complete_eta']['repaired_low193_complete_residual_L2_sup'],
        no_old_scalar_mean_ODE_or_target_certificate_recomputed=True,
        actual_new_target_provider_calls=0)


def sha_row(row):
    return hashlib.sha256((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('actual projected-source pilot failed: '+name)
    manifest=read(a.original_manifest);body=read(a.body);bp=read(a.body_process)
    repair=read(a.repair_source);rp=read(a.repair_process)
    fixed=read(a.fixed_jets);fp=read(a.fixed_process);Z=read(a.direction)
    gate('all_fixed_original_inputs_and_both_actual_completed_source_processes',
        sha(a.original_manifest)==OLD_MANIFEST and sha(a.candidate)==ORIGINAL and sha(a.response)==TRIAL
        and sha(a.body)==BODY and sha(a.body_process)==BODY_PROCESS and actual(bp,43586413510)
        and sha(a.object)==manifest['row_identity']['object_sha256']
        and sha(a.repair_source)==REPAIR_SOURCE and sha(a.repair_process)==REPAIR_PROCESS
        and actual(rp,43597921732) and body.get('complete') and repair.get('complete')
        and repair.get('complete_common_rows')==7721 and body.get('complete_original_common_cells')==7721
        and body.get('row_identity')==manifest['row_identity'])
    gate('actual_completed_fixed_eta_native_and_process_are_unchanged',
        sha(a.fixed_jets)==FIXED and actual(fp,43607383671)
        and fp.get('worker_source_sha256')==FIXED_WORKER
        and fp.get('input_manifest_sha256')==FIXED_MANIFEST
        and fp.get('complete_native_sha256')==FIXED
        and fixed.get('source_sha256')==FIXED_SOURCE and fixed.get('complete')
        and not fixed.get('failure') and len(fixed.get('gates',[]))==7
        and all(x['passed'] for x in fixed['gates'])
        and fixed.get('new_fixed_eta_target_evaluations_in_this_child')==80)
    gate('same_complete_exact_continuous193_direction_and_full_interval_offset_bounds',
        sha(a.direction)==Z_NATIVE and Z.get('complete')
        and Z.get('original_trial_sha256')==TRIAL
        and Z.get('derived_direction_definition_sha256')==Z_DEFINITION
        and Z['derived_direction_definition']['exact_interval']==['0','25/8']
        and Z['derived_direction_definition'].get('all193_states_and_mean_retained')
        and Z.get('exact_interface_count')==6143
        and len(Z.get('gates',[]))==7 and all(x['passed'] for x in Z['gates']))
    rows=[];parts=[]
    for path in a.parts:
        original=read(path)
        if (original.get('identity')!=manifest['row_identity']
            or original.get('kind')!=manifest['residual_kind']
            or not original.get('selected_cells_complete') or original.get('failure')):
            raise ValueError('an original cached full scalar-jet row part changed')
        first,end=original['selected_indices']
        if [x['common_row'] for x in original['rows']]!=list(range(first,end)):
            raise ValueError('an original cached row range is not exact')
        rows.extend(original['rows']);parts.append(dict(indices=[first,end],sha256=sha(path)))
    rows.sort(key=lambda x:x['common_row'])
    gate('the_exact_original_forty_parts_and_all7721_cached_scalar_rows',
        len(parts)==40 and len(rows)==7721 and [x['common_row'] for x in rows]==list(range(7721)))
    gate('every_original_part_byte_hash_matches_both_completed_body_and_repair_natives',
        sorted(x['sha256'] for x in parts)==sorted(body.get('inputs',{}).values())
        and sorted((tuple(x['indices']),x['sha256']) for x in parts)
            ==sorted((tuple(x['indices']),x['sha256']) for x in repair.get('original_parts',[])))
    background=load_candidate(a.candidate);trial=load_candidate(a.response)
    nodes=[Fraction(float(x)) for x in background['radial_nodes']]
    gate('all_original_physical_cubics_and_full193_response_mean_retained',
        background['piece_coefficients'].shape==(4,6144,65)
        and trial['piece_coefficients'].shape==(4,6144,193)
        and np.array_equal(background['radial_nodes'],trial['radial_nodes'])
        and nodes[0]==0 and nodes[-1]==RIGHT)
    edge=Fraction(0)
    for i,row in enumerate(rows):
        left,right=map(Fraction,row['interval'])
        if (left!=edge or not left<right or row['interval']!=body['residual_rows'][i]['interval']
            or row['interval']!=repair['rows'][i]['interval'] or repair['rows'][i]['common_row']!=i):
            raise ValueError('the original cached mean, scalar and repair partitions disagree')
        edge=right
    gate('the_complete_original_joint_partition_is_unchanged',edge==RIGHT)
    # Ranking is only a reproducible pilot choice, not a proof of a
    # maximum over the body. Every selected exact row index is retained.
    eligible=[i for i,row in enumerate(rows) if Fraction(row['interval'][0])<CUT]
    ranked=sorted(eligible,key=lambda i:float(interval(
        body['residual_rows'][i]['response_complete_nonmean_residual']['L2_L2_radial']).upper()),reverse=True)
    selected=set(ranked[:8]);lefts=[Fraction(row['interval'][0]) for row in rows]
    for radius in (Fraction(0),Fraction(1,20),Fraction(9,50),PHASE_RIGHT,Fraction(1,2),CUT):
        index=(bisect_left(lefts,radius)-1 if radius==CUT else bisect_right(lefts,radius)-1)
        selected.add(index)
    selected=sorted(selected)
    fresh_selected={1280,1283,1284,1289,1519,1524,3070,6375}
    gate('same_fourteen_selected_rows_and_all_eighty_completed_target_calls_reused',
        selected==fixed['selected_original_rows']
        and [x['common_row'] for x in fixed['rows']]==selected)
    context=dict(grid=512,fft=DirectedFFT(),fixed_rows={x['common_row']:x for x in fixed['rows']},
        Z_offset_A0=interval(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][0]).upper(),
        Z_offset_angle_A0=interval(Z['direction_repair_full_interval_joint_derivative_norms']['1/64'][1]).upper())
    alpha=exact(Fraction(manifest['row_identity']['exact_alpha']))
    doc.update(selected_original_rows=selected,selection_only_float_rank_of_existing_bounds=True,
        all_original_parts=parts,original_full_eta_target_certificates_recomputed=0,
        selected_new_fixed_eta_refinement_rows=sorted(fresh_selected),
        new_fixed_eta_refinement_subdivisions=[1,4],
        original_mean_flows_recomputed=0,original_complete_residual_certificates_unchanged=True,
        cached_complete_eta_scalar_jets_reused=True,
        previously_completed_fixed_eta_scalar_jets_reused=True,
        actual_new_target_provider_calls=0,exact_bump_scalar_coefficients_newly_consumed=True,
        continuous_Z_full_mean_retained=True,rows=[])
    if a.resume:
        prior=read(a.resume)
        if (prior.get('kind')!=doc['kind'] or prior.get('source_sha256')!=doc['source_sha256']
            or prior.get('input_sha256')!=doc['input_sha256']
            or prior.get('selected_original_rows')!=selected):
            raise ValueError('a projected-source prefix has a different mathematical identity')
        saved=prior.get('rows',[])
        if [x['common_row'] for x in saved]!=selected[:len(saved)]:
            raise ValueError('the actual projected-source prefix is not ordered and complete')
        for result in saved:
            if (not result.get('actual_projection_complete')
                or result['cached_scalar_row_sha256']!=sha_row(rows[result['common_row']])):
                raise ValueError('a previously completed projected-source cell changed')
        doc['rows']=saved
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_complete=prior.get('complete'),original_failure=prior.get('failure'),
            actual_completed_selected_rows=len(saved),no_completed_selected_cell_rerun=True)
    for i in selected[len(doc['rows']):]:
        tick=time.monotonic()
        result=row_projection(rows[i],body['residual_rows'][i],repair['rows'][i],
            background,trial,nodes,alpha,context)
        result['seconds']=time.monotonic()-tick;doc['rows'].append(result);save(a.out,doc)
        print(json.dumps(dict(actual_selected_row=i,
            cached_exact_bump_qstar_low193_L2_sup=result['exact_bump_cached_complete_eta']['repaired_low193_complete_residual_L2_sup']['upper'],
            cached_exact_bump_Z_low193_L2_sup=result['exact_bump_cached_complete_eta']['continuous_Z_complete_residual']['low193']['L2_sup']['upper'],
            reused_fixed_eta_Z_low193_L2_sup=[x['continuous_Z_complete_residual']['low193']['L2_sup']['upper']
                for x in result['reused_fixed_eta_refinements']],
            old_full160_L2_sup=result['original_complete_nonmean_residual_bound']['L2_sup']['upper'],
            seconds=result['seconds'])),flush=True)
    gate('every_new_selected_direct_Fourier_low193_and_true_high_source_diagnostic_completed',
        [x['common_row'] for x in doc['rows']]==selected)
    gate('all_requested_new_fixed_eta_rows_and_four_subcells_completed',
        all(len(x['reused_fixed_eta_refinements'])==2
            and [y['subdivisions'] for y in x['reused_fixed_eta_refinements']]==[1,4]
            and all(len(y['children'])==y['subdivisions'] for y in x['reused_fixed_eta_refinements'])
            for x in doc['rows'] if x['common_row'] in fresh_selected)
        and fresh_selected.issubset(selected))
    doc.update(new_fixed_eta_target_evaluations_in_this_child=0,
        previous_successful_fixed_eta_native_sha256=FIXED,
        complete_continuous_direction_native_sha256=Z_NATIVE,
        complete_continuous_direction_definition_sha256=Z_DEFINITION,
        complete=True,selected_cells_complete=True,complete_body_projection_cover=False,
        original_candidate_sha256=ORIGINAL,original_full_physical_trial_sha256=TRIAL,
        original_body_and_mean_native_sha256=BODY,actual_complete_repair_source_native_sha256=REPAIR_SOURCE,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        actual_finite193_response_error_bound_proved=False,complete_infinite_inverse_proved=False,
        true_parameter_Schur_proved=False,
        all_original_target_tails_and_independent_mean_retained=True,
        unknown_high_input_feedback_not_removed_by_projecting_known_source=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('original-manifest','candidate','response','body','body-process','repair-source','repair-process','object','fixed-jets','fixed-process','direction','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--parts',type=Path,nargs='+',required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual selected projected-source outcome')
    doc=dict(kind='actual_exact_rational_bump_and_full_continuous_Z_residual_pilot_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),rows=[],
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in
            ('original-manifest','candidate','response','body','body-process','repair-source','repair-process','object','fixed-jets','fixed-process','direction')},
        complete_body_projection_cover=False,actual_finite193_response_error_bound_proved=False,
        complete_infinite_inverse_proved=False,true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],selected_rows=len(doc['rows']),
        seconds=doc['seconds'],complete_body_projection_cover=False)),flush=True)


if __name__=='__main__':main()
