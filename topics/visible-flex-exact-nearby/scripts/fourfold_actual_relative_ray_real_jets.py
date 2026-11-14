#!/usr/bin/env python3
"""Whole-time actual real relative-flow jets from all original Fourier controls.

The complete true-Jacobian error and each symbolic retarget derivative fee
are differentiated on their paid complex label strips before real evaluation.
The relative jets cover every pair of times, not just the two endpoints.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_phase_beta_bulk_box import Box,CBox,reduce_box
from fourfold_negative_root_physical_graph_operator import mult
from fourfold_strict_high_energy_triangular import positive_matrix_bound,weighted_principal
from fourfold_actual_high_density_first_phase import derivative_multiplier


def up(v):return stored(v).upper()
def lo(v):return stored(v).lower()


def bell_table(H,order):
    B=[[arb(0) for _ in range(order+1)] for _ in range(order+1)]
    B[0][0]=arb(1)
    for n in range(1,order+1):
        for k in range(1,n+1):
            B[n][k]=sum((math.comb(n-1,j-1)*H[j]*B[n-j][k-1]
                         for j in range(1,n-k+2)),arb(0)).upper()
    return B


def complete_comparisons(N,Cr,H,order):
    B=bell_table(H,order+1)
    P=acb_mat(order+1,order+1);D=acb_mat(order+1,order+1)
    for j in range(order+1):
        for k in range(j+1):
            P[j,k]=B[j][k]/arb(N)**(j-k)
            D[j,k]=(Cr**j if j==k else Cr*B[j+1][k+1]/arb(N)**(j-k))
    ps=[(Cr.sqrt()*positive_matrix_bound(weighted_principal(P,j))).upper()
        for j in range(order+1)]
    ds=[(Cr.sqrt()*positive_matrix_bound(weighted_principal(D,j))).upper()
        for j in range(order+1)]
    return ps,ds


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference-gate',type=Path,default=Path('notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz'))
    p.add_argument('--reference-summary',type=Path,default=Path('notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'))
    p.add_argument('--ray',type=Path,default=Path('notes/2026-11-13-R106-integrated-source-ray-refinement.json'))
    p.add_argument('--jacobian',type=Path,default=Path('notes/2026-11-13-R106-complete-relative-real-Jacobian.json.gz'))
    p.add_argument('--high',type=Path,default=Path('notes/2026-11-13-actual-fixed-label-high-density-Volterra.json'))
    p.add_argument('--phase',type=Path,default=Path('notes/2026-11-13-actual-high-density-first-phase-two-window.json'))
    p.add_argument('--order',type=int,default=12)
    p.add_argument('--scales',type=int,nargs='+',default=[4096,16384,65536,1048576,2**30,2**40])
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or not 4<=a.order<=16 or min(a.scales)<1:
        raise ValueError('fresh output and a finite true order at least four are required')
    ctx.prec=a.bits;tick=time.monotonic()
    gate=read(a.reference_gate);summary=read(a.reference_summary);ray=read(a.ray)
    realjac=checked(a.jacobian,'fourfold_true_relative_ray_jacobian_cells.py')
    high=checked(a.high,'fourfold_actual_label_high_density_volterra.py')
    phase=checked(a.phase,'fourfold_actual_high_density_first_phase.py')
    if (not gate['complete'] or not gate['full_branch_nonzero_proved']
        or not summary['complete'] or summary['report_sha256']!=sha(a.reference_gate)
        or not ray['complete'] or realjac['identity']!=high['identity']
        or phase['identity']!=high['identity']
        or phase['inputs'].get(str(a.high))!=sha(a.high)):
        raise ValueError('the same complete actual upstream object is required')
    ident=gate['identity']
    if ident['source_sha256']!=sha(Path(__file__).with_name('fourfold_reference_derivative_gate.py')):
        raise ValueError('complete finite reference producer changed')
    for name,digest in gate['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('finite reference dependency changed')
    prov=ray['provenance']
    if sha(Path(prov['source']))!=prov['source_sha256']:
        raise ValueError('true whole-time ray producer changed')
    for z in prov['inputs']:
        if sha(Path(z['path']))!=z['sha256']:raise ValueError('whole-time ray proof input changed')
    for path in (a.reference_gate,a.reference_summary,a.ray):
        if realjac['inputs'].get(str(path))!=sha(path):
            raise ValueError('real first-jet and higher-jet certificates use different inputs')
    mp=Path(ident['manifest_path']);dp=Path(ident['retarget_descriptor'])
    manifest=read(mp);descriptor=read(dp)
    if sha(mp)!=ident['manifest_sha256'] or sha(dp)!=ident['retarget_descriptor_sha256']:
        raise ValueError('exact original reference identity changed')
    if (descriptor['target_object']['sha256']!=high['identity']['object_sha256']
        or descriptor['target_exact_delta_fraction']!=high['identity']['exact_center_parameter']
        or ray['proved_region']['parameter_center']!=high['identity']['exact_center_parameter']
        or ray['proved_region']['parameter_half_width']!=high['identity']['exact_parameter_half_width']):
        raise ValueError('different original whole real parameter family')
    if (manifest['time_basis']!='bernstein' or manifest['time_degree']!=7
        or manifest['fields']!=['U','L'] or manifest['segment_count']!=550
        or len(gate['segments'])!=550 or ray['proved_region']['segments']!=550
        or ray['proved_region']['time_endpoints']!=['-pi/2','pi/2']):
        raise ValueError('all 550 true segments and all eight controls are required')
    if [z['segment'] for z in gate['segments']]!=list(range(550)):
        raise ValueError('the complete control gate has a gap')
    sr=exact_arb(Fraction(ray['proved_region']['label_strip']))
    sf=exact_arb(Fraction('1/512'))
    error=exact_arb(Fraction(ray['bounds']['true_J_minus_reference_q']['exact'])).upper()
    Cr=up(high['true_relative_real_derivative']);Cc=up(high['true_relative_complex_derivative'])
    X=lo(high['unchanged_normalized_complex_flow_strip'])
    physical_lower=max(lo(realjac['common_true_label_derivative_lower']),
        exact_arb(Fraction(ray['bounds']['true_label_J_real_lower']['exact'])).lower())
    physical_upper=min(up(realjac['common_true_label_derivative_upper']),
        exact_arb(Fraction(ray['bounds']['true_label_J_modulus']['exact'])).upper())
    m=(4*physical_lower).lower();M1=(4*physical_upper).upper()
    if not m>0:raise ValueError('complete true real initial-label derivative is not positive')
    degree=manifest['Fourier_degree'];n=Box(np.arange(1,degree+1,dtype=float))
    weights=[Box(np.ones(degree))]
    for j in range(1,a.order+1):weights.append(weights[-1]*n)
    absolute=[arb(0),M1]+[arb(0) for _ in range(2,a.order+1)]
    inputs={str(z):sha(z) for z in (a.reference_gate,a.reference_summary,a.ray,
                                  a.jacobian,a.high,a.phase,mp,dp)}
    segments=[];count=0;previous_end=None;last=tick
    print(dict(stage='all_complete_certificates_checked',segments=550,order=a.order),flush=True)
    for shard in manifest['shards']:
        path=mp.parent/shard['path'];payload=path.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=shard['sha256'] or len(payload)!=shard['bytes']:
            raise ValueError('exact original finite Fourier shard changed')
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
            raise ValueError('the exact original continuous reference definition changed')
        # Exact binary64 coefficient inputs; complex modulus is bounded by
        # the directed L1 rectangle modulus. Each frequency multiplication
        # and every pairwise sum is rounded outward by the existing Box kernel.
        mag=Box(CBox(Box(re[:,:,0,1:]),Box(im[:,:,0,1:])).magnitude_upper())
        moments={}
        for j in range(2,a.order+1):
            moments[j]=reduce_box(mag*weights[j].reshape(1,1,-1),axis=-1).hi
        for local in range(number):
            index=start+local;old=gate['segments'][index]
            if (old['base_source']['sha256']!=shard['sha256']
                or old['exact_times']!=manifest['exact_time_endpoints'][index:index+2]):
                raise ValueError('complete control gate belongs to different exact coefficients')
            if previous_end is not None and (not np.array_equal(previous_end[0],re[local,0])
                    or not np.array_equal(previous_end[1],im[local,0])):
                raise ValueError('exact original Fourier/Bernstein seam is discontinuous')
            previous_end=re[local,-1].copy(),im[local,-1].copy()
            gate_width=old['widths']['1/512']
            if not gate_width['positive_real_part_gate_proved']:raise ValueError('a complete finite gate failed')
            fees=[up(z) for z in gate_width['retarget_C1_fees']]
            if len(fees)!=8:raise ValueError('all eight symbolic retarget fees are required')
            values=[];control_witness=[]
            for j in range(2,a.order+1):
                full=[(8*arb(float(moments[j][local,k]))
                    +4*math.factorial(j-1)*(fees[k]/sf**(j-1)+error/sr**(j-1))).upper()
                    for k in range(8)]
                witness=max(range(8),key=lambda k:full[k]);bound=full[witness]
                absolute[j]=max(absolute[j],bound)
                values.append(record(bound));control_witness.append(witness)
            segments.append(dict(segment=index,all_eight_controls=True,
                exact_times=old['exact_times'],normalized_true_real_derivative_orders=list(range(2,a.order+1)),
                complete_derivative_moduli=values,control_witnesses=control_witness))
            count+=1
        if time.monotonic()-last>20:
            print(dict(stage='complete_Fourier_controls',segments=count,seconds=time.monotonic()-tick),flush=True)
            last=time.monotonic()
    if count!=550:raise ValueError('whole-time reference incomplete')
    # From F_t=H_(t,s) o F_s. Divide each Bell monomial by (F_s')^j
    # before bounding; its first-derivative variable is exactly one.
    normalized=[arb(0),arb(1)]+[(absolute[j]/m**j).upper() for j in range(2,a.order+1)]
    B=bell_table(normalized,a.order)
    best=[arb(0),Cr];bounds=[]
    for j in range(2,a.order+1):
        new=(normalized[j]+sum((best[k]*B[j][k] for k in range(1,j)),arb(0))).upper()
        old=(math.factorial(j-1)*Cc/(X/2)**(j-1)).upper()
        selected=min(old,new).upper();best.append(selected)
        bounds.append(dict(order=j,true_absolute_normalized_flow_derivative=record(absolute[j]),
            whole_time_relative_derivative_from_actual_Fourier=record(new),
            prior_small_strip_Cauchy_derivative=record(old),
            accepted_complete_relative_derivative=record(selected),
            improvement_factor=record((old/selected).lower()),
            actual_Fourier_bound_improves=bool(new<old)))
    qk=up(phase['full_integrated_density_kappa'])
    qQ=up(phase['full_integrated_material_ratio_derivative'])
    R=up(phase['full_ratio_modulus']);fieldstrip=lo(high['normalized_field_strip'])
    jac=best[1:4]
    lj=[Cr*best[2],Cr*best[3]+Cr**2*best[2]**2,
        Cr*best[4]+3*Cr**2*best[3]*best[2]+2*Cr**3*best[2]**3]
    budget=[]
    for N in a.scales:
        ps,ds=complete_comparisons(N,Cr,best,2)
        unit=[mult(N,j,arb(1),fieldstrip) for j in range(3)]
        jm=[derivative_multiplier(N,j,jac) for j in range(3)]
        lm=[derivative_multiplier(N,j,lj) for j in range(3)]
        k0=(Cr*qk/(4*N)).upper();G=k0.exp().upper()
        kf=[None]+[(arb(2).sqrt()*ds[j]*ps[j]*unit[j]*qk/(4*N)).upper() for j in (1,2)]
        ka=[None]+[(arb(2).sqrt()*ds[j-1]*ps[j-1]*unit[j-1]*qk/(4*N)).upper() for j in (1,2)]
        E=[(ds[j]*ps[j]*unit[j]*jm[j]*R/64).upper() for j in range(3)]
        Z=[(ds[j]*ps[j]*unit[j]*(jm[j]*qQ/64+lm[j]*qk/8)).upper() for j in range(3)]
        c0=min((k0/2).upper(),((2*E[0]+Z[0])/arb(N)**2).upper())
        cp=(2*(2*E[2]+Z[2])/arb(N)**2).upper()
        cm=(2*(2*E[0]+Z[0])/arb(N)**2).upper()
        b0=min((G-1-k0).upper(),(k0*k0*G/2).upper())
        bp=(kf[2]*kf[1]*G/2).upper();bm=(ka[2]*ka[1]*G/2).upper()
        r0=(c0+b0).upper();rp=(cp+bp).upper();rm=(cm+bm).upper()
        budget.append(dict(scale=N,base_high_gain=record(G),
            complete_scalar_pullbacks=[record(z) for z in ps],
            complete_density_pullbacks=[record(z) for z in ds],
            complete_base_remainder=record(r0),
            complete_forward_two_remainder=record(rp),
            complete_opposite_two_remainder=record(rm),
            complete_forward_four_thirds_remainder=record((r0**(arb(1)/3)*rp**(arb(2)/3)).upper()),
            complete_opposite_four_thirds_remainder=record((r0**(arb(1)/3)*rm**(arb(2)/3)).upper()),
            high_Volterra_gain_order_one=record((1+kf[1]*G).upper()),
            high_Volterra_gain_order_two=record((1+kf[2]*(1+kf[1]*G)).upper()),
            ordinary_source_error_forward_two=record((rp*Cr.sqrt()*up(high['full_m_modulus'])/arb(2).sqrt()).upper()),
            low_height_history_error_forward_two=record((rp*Cr.sqrt()*qk/arb(2).sqrt()).upper()),
            ordinary_source_error_opposite_two=record((rm*ps[2]*mult(N,2,up(high['full_m_modulus']),fieldstrip)/arb(2).sqrt()).upper()),
            low_height_history_error_opposite_two=record((rm*ps[2]*unit[2]*qk/arb(2).sqrt()).upper())))
    report=dict(kind='actual_all_time_relative_real_ray_derivatives_and_same_high_phase_budget',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,order=a.order,
        identity=high['identity'],inputs=inputs,entire_original_parameter_box=True,
        all_550_true_segments_and_4400_exact_controls=True,all_549_exact_seams_checked=True,
        all_real_angles=True,all_pairs_of_strict_times_and_both_directions=True,
        original_complex_ray_J_error_strip=record(sr),
        original_symbolic_retarget_derivative_fee_strip=record(sf),
        complete_true_physical_label_J_error=record(error),
        true_normalized_initial_label_derivative_lower=record(m),
        true_normalized_initial_label_derivative_upper=record(M1),
        accepted_relative_first_derivative=record(Cr),
        complete_absolute_normalized_flow_derivatives=[record(z) for z in absolute[1:]],
        whole_time_relative_derivative_bounds=bounds,
        exact_relative_identity='F_t=H_(t,s) o F_s, F_t=4*actual physical Y_t; H and H_inverse are covered for every real pair s,t',
        exact_normalized_Bell_variables='x1=1; xj=M_j/(inf F_s_prime)^j; divide each full Bell monomial before bounding',
        same_label_high_phase_budgets=budget,segments=segments,
        no_new_complex_width_or_complex_derivative_bound=True,
        original_projection_mean_source_and_reconstruction_positions_unchanged=True,
        fixed_angular_weight_bound_proved=False,finite_head_feedback_solved=False,
        complete_returned_remainder_claimed=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py',
            'fourfold_negative_root_physical_graph_operator.py','fourfold_strict_high_energy_triangular.py',
            'fourfold_actual_high_density_first_phase.py')},
        seconds=time.monotonic()-tick)
    save(a.out,report)
    print(dict(complete=True,derivatives=[dict(j=z['order'],bound=z['accepted_complete_relative_derivative']['upper'],
        improved=z['actual_Fourier_bound_improves']) for z in bounds],
        budgets=[dict(N=z['scale'],forward_two=z['complete_forward_two_remainder']['upper'],
        opposite_two=z['complete_opposite_two_remainder']['upper']) for z in budget],
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
