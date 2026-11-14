#!/usr/bin/env python3
"""True time-weighted Jacobians and the complete unshifted density evolution.

The exact dyadic 550x8 Fourier/Bernstein reference is evaluated by native
Arb DFTs on a closed real circle. Its time log-slope is proved after the
whole angular cell fee. Complete retarget and true-flow errors remain.
The resulting actual transport bound is consumed with the complete
height and two waves; every mean, original source and head path remains.
"""
from __future__ import annotations
import argparse,hashlib,io,gzip,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(z):return stored(z).upper()
def lo(z):return stored(z).lower()
def exact_time(z):
    q=exact_arb(Fraction(z['numerator'])/int(z['denominator']))
    if z['kind']=='rational_multiple_of_pi':return q*arb.pi()
    if z['kind']=='rational':return q
    raise ValueError('unknown exact original time')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old-jacobian',type=Path,default=Path(
        'notes/2026-11-13-R106-complete-relative-real-Jacobian.json.gz'))
    p.add_argument('--reference-gate',type=Path,default=Path(
        'notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz'))
    p.add_argument('--ray',type=Path,default=Path(
        'notes/2026-11-13-R106-integrated-source-ray-refinement.json'))
    p.add_argument('--fields',type=Path,default=Path(
        'notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--energy',type=Path,default=Path(
        'notes/2026-11-13-R46-unshifted-half-density-energy.json'))
    p.add_argument('--nodes',type=int,default=4096)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.nodes<2 or a.nodes&(a.nodes-1) or a.bits<160:
        raise ValueError('fresh native output, full power-of-two circle and directed precision required')
    ctx.prec=a.bits;tick=time.monotonic()
    old=checked(a.old_jacobian,'fourfold_true_relative_ray_jacobian_cells.py')
    fields=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    energy=checked(a.energy,'fourfold_strict_unshifted_half_density_energy.py')
    if old['identity']!=fields['identity'] or fields['identity']!=energy['identity']:
        raise ValueError('same complete original actual field/ray/parameter family required')
    for parent,path in ((old,a.reference_gate),(old,a.ray),(energy,a.fields)):
        if parent['inputs'].get(str(path))!=sha(path):
            raise ValueError('the actual continuous input changed: '+str(path))
    if (len(fields['cells'])!=215 or not fields['mean_retained']
            or energy['exact_fixed_height_weight']!='9'):
        raise ValueError('the original complete strict cover and fixed height energy are required')
    gate=read(a.reference_gate);ray=read(a.ray);identity=gate['identity']
    if not gate['complete'] or not gate['full_branch_nonzero_proved'] or not ray['complete']:
        raise ValueError('the complete true-flow and reference gate are required')
    if identity['source_sha256']!=sha(Path(__file__).with_name('fourfold_reference_derivative_gate.py')):
        raise ValueError('reference derivative producer changed')
    for name,digest in gate['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('reference derivative dependency changed: '+name)
    mp=Path(identity['manifest_path']);manifest=read(mp)
    dp=Path(identity['retarget_descriptor']);descriptor=read(dp)
    if (sha(mp)!=identity['manifest_sha256']
            or sha(dp)!=identity['retarget_descriptor_sha256']
            or old['inputs'].get(str(mp))!=sha(mp)
            or old['inputs'].get(str(dp))!=sha(dp)):
        raise ValueError('the exact original reference/retarget definition changed')
    if (descriptor['target_object']['sha256']!=fields['identity']['object_sha256']
            or descriptor['target_exact_delta_fraction']!=fields['identity']['exact_center_parameter']
            or ray['proved_region']['parameter_center']!=fields['identity']['exact_center_parameter']
            or ray['proved_region']['parameter_half_width']!=fields['identity']['exact_parameter_half_width']):
        raise ValueError('the complete real affine parameter interval differs')
    degree=manifest['Fourier_degree']
    if (manifest['time_basis']!='bernstein' or manifest['time_degree']!=7
            or manifest['fields']!=['U','L'] or manifest['segment_count']!=550
            or len(gate['segments'])!=550 or a.nodes<=2*degree):
        raise ValueError('all original exact Fourier modes and 550x8 controls required')
    error=4*exact_arb(Fraction(ray['bounds']['true_J_minus_reference_q']['exact']))
    if not 0<error<arb(1)/75:
        raise ValueError('complete normalized true-Jacobian error outside scope')
    inputs={str(z):sha(z) for z in (
        a.old_jacobian,a.reference_gate,a.ray,a.fields,a.energy,mp,dp)}
    half=arb.pi()/a.nodes;half2=half*half/2
    rows=[];count=0;previous_end=None;delta=arb(0);log_integral=arb(0)
    last=tick;digest=hashlib.sha256();checkpoint=Path(str(a.out)+'.checkpoint.json')
    resume_count=0;prior_seconds=0.;base_inputs=dict(inputs)
    if checkpoint.exists():
        saved=read(checkpoint)
        if (saved['source_sha256']!=sha(__file__) or saved['base_inputs']!=base_inputs
                or saved['bits']!=a.bits or saved['nodes']!=a.nodes
                or saved['identity']!=fields['identity']):
            raise ValueError('the saved strict prefix has a different exact producer or input')
        rows=saved['reference_segments'];resume_count=len(rows)
        if not 0<=resume_count<=550 or [z['segment'] for z in rows]!=list(range(resume_count)):
            raise ValueError('saved exact reference prefix is not consecutive')
        for row in rows:
            if row['exact_times']!=manifest['exact_time_endpoints'][row['segment']:row['segment']+2]:
                raise ValueError('saved prefix uses a different exact reference time')
            delta=max(delta,up(row['complete_relative_J_error']))
            log_integral+=up(row['complete_time_integral_log_J_derivative'])
            digest.update((row['closed_cell_digest_60_digits']+'\n').encode())
        prior_seconds=float(saved['seconds'])
    def checkpoint_prefix():
        save(checkpoint,dict(kind='complete_directed_reference_prefix_checkpoint',
            complete=False,source_sha256=sha(__file__),base_inputs=base_inputs,
            bits=a.bits,nodes=a.nodes,identity=fields['identity'],
            reference_segments=rows,seconds=prior_seconds+time.monotonic()-tick))
    print(dict(stage='complete_inputs_checked',segments=550,controls=8,
               nodes=a.nodes,resumed_exact_segments=resume_count,
               normalized_first_two_angle_derivatives=True),flush=True)
    for shard in manifest['shards']:
        path=mp.parent/shard['path'];payload=path.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=shard['sha256'] or len(payload)!=shard['bytes']:
            raise ValueError('exact full reference shard changed')
        inputs[str(path)]=shard['sha256']
        with np.load(io.BytesIO(gzip.decompress(payload))) as z:
            re=z['coefficient_real'];im=z['coefficient_imag'];meta=json.loads(str(z['metadata']))
        start=shard['start_segment'];number=shard['segment_count']
        if (start!=count or re.shape!=(number,8,2,degree+1) or re.shape!=im.shape
                or re.dtype!=np.dtype('float64') or im.dtype!=np.dtype('float64')
                or not np.all(np.isfinite(re)) or not np.all(np.isfinite(im))
                or np.any(im[...,0]!=0) or meta['start_segment']!=start
                or meta['segment_count']!=number
                or meta['exact_times']!=manifest['exact_time_endpoints'][start:start+number+1]):
            raise ValueError('the exact complete reference scalar definition differs')
        for local in range(number):
            index=start+local;g=gate['segments'][index]
            if (g['segment']!=index or g['base_source']['sha256']!=shard['sha256']
                    or g['exact_times']!=manifest['exact_time_endpoints'][index:index+2]):
                raise ValueError('reference derivative gate uses a different segment')
            if previous_end is not None and (not np.array_equal(previous_end[0],re[local,0])
                    or not np.array_equal(previous_end[1],im[local,0])):
                raise ValueError('an original exact Bernstein seam is discontinuous')
            previous_end=re[local,-1].copy(),im[local,-1].copy()
            if index<resume_count:
                count+=1
                continue
            width=g['widths']['1/512']
            if not width['positive_real_part_gate_proved']:
                raise ValueError('complete retarget control gate failed')
            dt=exact_time(g['exact_times'][1])-exact_time(g['exact_times'][0])
            if not dt>0:raise ValueError('original exact time interval is not positive')
            values=[];angles=[];curvatures=[];coefficients=[]
            E=max((4*up(z)+error for z in width['retarget_C1_fees'])).upper()
            for control in range(8):
                cf=[acb(0) for _ in range(a.nodes)];cf[0]=acb(1)
                dcf=[acb(0) for _ in range(a.nodes)];Q2=arb(0);positive=[acb(0)]
                for k in range(1,degree+1):
                    u=acb(arb(float(re[local,control,0,k])),
                          arb(float(im[local,control,0,k])))
                    q=4*acb(0,k)*u;qx=acb(0,k)*q
                    positive.append(q)
                    cf[k]=q;cf[-k]=q.conjugate()
                    dcf[k]=qx;dcf[-k]=qx.conjugate()
                    Q2+=2*k*k*abs(q)
                vs=acb.dft(cf,inverse=True);xs=acb.dft(dcf,inverse=True)
                vr=[];xr=[]
                for v,x in zip(vs,xs):
                    v*=a.nodes;x*=a.nodes
                    if (not v.is_finite() or not x.is_finite()
                            or not v.imag.contains(0) or not x.imag.contains(0)):
                        raise ValueError('the complete finite real Fourier jets lost reality')
                    vr.append(v.real);xr.append(x.real)
                values.append(vr);angles.append(xr)
                curvatures.append(Q2.upper());coefficients.append(positive)
            time_second=[]
            for control in range(7):
                time_second.append((sum((2*k*k*abs(
                    7*(coefficients[control+1][k]-coefficients[control][k])/dt)
                    for k in range(1,degree+1)),arb(0))).upper())
            qmin=None;L=arb(0);Qt=arb(0);qmax=arb(0);variation_max=arb(0)
            segment_digest=hashlib.sha256()
            for node in range(a.nodes):
                variations=[(abs(angles[k][node])*half+curvatures[k]*half2).upper()
                            for k in range(8)]
                qlo=min((values[k][node].lower()-variations[k]).lower() for k in range(8))
                qhi=max((values[k][node].upper()+variations[k]).upper() for k in range(8))
                if not qlo>E:
                    raise ValueError('reference positivity must precede the actual relative division')
                T=max((abs(7*(values[k+1][node]-values[k][node])/dt)
                       +abs(7*(angles[k+1][node]-angles[k][node])/dt)*half
                       +time_second[k]*half2).upper() for k in range(7))
                L=max(L,(T/qlo).upper());Qt=max(Qt,T)
                qmin=qlo if qmin is None else min(qmin,qlo);qmax=max(qmax,qhi)
                variation_max=max(variation_max,*variations)
                segment_digest.update((qlo.str(60)+' '+T.str(60)+'\n').encode())
            di=(E/qmin).upper();delta=max(delta,di)
            cost=(dt*L).upper();log_integral+=cost
            rows.append(dict(segment=index,exact_times=g['exact_times'],
                finite_normalized_reference_J_lower=record(qmin),
                finite_normalized_reference_J_upper=record(qmax),
                complete_normalized_retarget_and_true_J_fee=record(E),
                complete_relative_J_error=record(di),
                complete_finite_angular_cell_variation=record(variation_max),
                finite_reference_time_J_modulus=record(Qt),
                whole_real_reference_log_J_time_derivative=record(L),
                complete_time_integral_log_J_derivative=record(cost),
                closed_cell_digest_60_digits=segment_digest.hexdigest()))
            digest.update((segment_digest.hexdigest()+'\n').encode())
            count+=1
            if count%5==0 or count==550:
                checkpoint_prefix()
            if time.monotonic()-last>20:
                print(dict(stage='true_time_weight',segments=count,
                           log_reference_integral=log_integral.str(10),
                           seconds=prior_seconds+time.monotonic()-tick),flush=True);last=time.monotonic()
    if count!=550 or not delta<1:
        raise ValueError('complete time cover or positive true reference comparison failed')
    D=((1+delta)/(1-delta)).sqrt().upper()
    Q=arb(0);strict_rows=[];cursor=Fraction(0)
    for i,c in enumerate(fields['cells']):
        left,right=Fraction(c['left']),Fraction(c['right'])
        if left!=cursor or not left<right:raise ValueError('full strict field cover gap')
        cursor=right;h=2*exact_arb(right-left)
        M={k:up(v) for k,v in c['complete_complex_field_moduli'].items()}
        mu=lo(c['geometry']['mu_modulus_lower'])
        if not mu>0:raise ValueError('complete strict real density positivity missing')
        A=(3*((M['nu']**2+M['v']**2)/mu).sqrt()).upper()
        B=(M['d']/(3*mu.sqrt())).upper()
        C=((M['Lr']+(M['v']+M['nu'])*M['Ltheta'])/2).upper()
        trace=A*A+B*B+C*C
        disc=((B*B+C*C-A*A)**2+4*A*A*C*C).sqrt()
        norm=((trace+disc)/2).sqrt().upper()
        Q+=h*norm
        strict_rows.append(dict(cell=i,left=str(left),right=str(right),
            complete_wave_to_height=record(A),complete_height_to_wave=record(B),
            complete_wave_cross=record(C),full_zero_order_block_norm=record(norm),
            reflected_integral=record((h*norm).upper())))
    if str(cursor)!=energy['exact_physical_interval'][1]:
        raise ValueError('the complete original strict endpoint differs')
    log_integral=log_integral.upper();Q=Q.upper()
    logarithm=(D.log()+log_integral/2+D*Q).upper()
    growth=logarithm.exp().upper()
    eb=energy['bounds'];mulo=lo(eb['full_mu_lower'])
    rawsource=(growth/mulo.sqrt()).upper()
    meanw=up(eb['old_density_mean_conversion']);meany=up(eb['old_density_y_conversion'])
    newrows=[]
    for row in energy['rows']:
        N=row['scale'];low=lo(row['energy_comparison_lower'])
        high=up(row['energy_comparison_upper'])
        frame=up(row['full_original_normal_frame_and_inverse_at_base'])
        physical=(growth*(high/low).sqrt()).upper()
        sourcehalf=(rawsource/low.sqrt()).upper()
        initial=(growth*high.sqrt()).upper()
        newrows.append(dict(scale=N,energy_comparison_lower=record(low),
            energy_comparison_upper=record(high),
            full_physical_Cauchy_positive_half=record(physical),
            full_physical_Cauchy_flux_dual_negative_half=record(physical),
            full_physical_Cauchy_all_between_minus_half_and_half=record(physical),
            full_physical_L1L2_source_to_positive_half=record(sourcehalf),
            full_physical_L1_HNminus_half_source_to_zero=record(physical),
            full_original_normal_frame_and_inverse_at_base=record(frame),
            same_full_original_L2_amplitude_and_inverse=record((frame*physical*frame).upper()),
            same_full_original_L1_HNminus_half_source_to_L2_amplitude=record((frame*physical).upper()),
            old_density_base_mean_initial=record((meanw*initial).upper()),
            old_density_base_y_initial=record((meany*initial).upper()),
            old_density_base_mean_source=record((meanw*rawsource).upper()),
            old_density_base_y_source=record((meany*rawsource).upper())))
    best=min(newrows,key=lambda z:up(z['same_full_original_L2_amplitude_and_inverse']))
    gates=[]
    def check(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    check('all exact reference segments, eight controls and continuous joins retained',count==550)
    check('full finite positivity precedes the entire retarget and true-flow division',delta<arb(1)/10)
    check('the true transport-weight evolution improves the complete previous energy',
          logarithm<lo(eb['full_energy_logarithm']))
    check('the same original complete amplitude propagation improves',
          up(best['same_full_original_L2_amplitude_and_inverse'])<lo(energy['best_complete_original_base_amplitude']))
    out=dict(kind='actual_complete_time_weighted_true_transport_and_unshifted_density_energy',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,nodes=a.nodes,
        identity=fields['identity'],inputs=inputs,native_geometric_cells_recomputed=0,
        exact_physical_interval=energy['exact_physical_interval'],
        exact_fixed_height_weight='9',entire_original_real_parameter_box=True,
        actual_parameter_scope=energy['actual_parameter_scope'],
        all_550_true_segments_and_4400_full_controls=True,all_549_exact_seams_checked=True,
        reference_Fourier_modes_not_truncated=True,closed_real_angular_circle=True,
        finite_reference_time_derivative_definition='degree-seven Bernstein derivative: seven times adjacent exact controls divided by the exact segment length',
        actual_Jacobian_error_definition='4 times (complete retarget C1 control error + complete true-flow J error)',
        true_time_weighted_density_bound='D_error * exp(abs(w(t)-w(s))); w prime is L_reference/2 in true monotone tau; holds in both directions and all interior pairs',
        exact_no_height_transport='sqrt(lambda)*u_r=sqrt(lambda)/(sqrt(2*mu))*((nu-v)*Y_plus-(nu+v)*Y_minus)',
        exact_zero_order_block_majorant='[[0,A],[B,C]], A=sqrt(lambda*(nu^2+v^2)/mu), B=abs(d)/sqrt(lambda*mu), C=(abs(ell_r)+(abs(v)+nu)*abs(ell_theta))/2',
        full_state='(sqrt(lambda)*u,Y_plus,Y_minus), with the original full u and physical p; no nonzero-mode substitution for u',
        actual_source='(0,+f/sqrt(2*mu),-f/sqrt(2*mu)), original ordinary scalar in dr',
        full_Cauchy_and_source_bound='D_error * exp(total_reference_log_slope/2 + D_error*integral_full_B_norm)',
        original_full_physical_energy_and_frame_unchanged=True,
        height_mean_flux_mean_every_head_path_and_all_ordinary_source_modes_retained=True,
        both_real_time_directions_and_every_strict_subinterval=True,
        source_weight_does_not_require_a_time_derivative_of_the_source=True,
        no_bare_pullback_small_operator_difference_used=True,
        no_new_complex_angle_or_time_domain_claimed=True,
        bounds={k:record(v) for k,v in dict(
            full_relative_reference_J_error=delta,complete_true_transport_error_factor=D,
            full_reference_log_J_time_integral=log_integral,
            complete_full_zero_order_block_integral=Q,
            full_energy_logarithm=logarithm,full_energy_Cauchy_growth=growth,
            full_L1L2_source_to_energy=rawsource,full_mu_lower=mulo,
            old_density_mean_conversion=meanw,old_density_y_conversion=meany,
            prior_energy_logarithm=up(eb['full_energy_logarithm']),
            gain_over_prior_energy=(lo(eb['full_energy_Cauchy_growth'])/growth).lower()).items()},
        reference_segments=rows,reference_segment_digest_chain_60_digits=digest.hexdigest(),
        complete_strict_zero_order_blocks=strict_rows,rows=newrows,
        best_base_amplitude_scale=best['scale'],
        best_complete_original_base_amplitude=best['same_full_original_L2_amplitude_and_inverse'],
        higher_density_bootstrap_reconsumed=False,full_returned_Rstar_recomputed=False,
        finite_head_inverse_proved=False,full_feedback_inverse_proved=False,
        new_nonlinear_body_or_changed_tail_transfer_proved=False,
        resumed_strict_prefix_segments=resume_count,
        gates=gates,seconds=prior_seconds+time.monotonic()-tick,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_reference_derivative_gate.py')})
    save(a.out,out)
    print(dict(complete=True,logarithm=logarithm.str(14),growth=growth.str(14),
               true_transport_factor=D.str(14),reference_log_slope=log_integral.str(14),
               out=str(a.out),sha256=sha(a.out),seconds=out['seconds']),flush=True)


if __name__=='__main__':main()
