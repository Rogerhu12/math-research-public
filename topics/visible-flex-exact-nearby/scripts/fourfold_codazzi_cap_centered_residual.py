#!/usr/bin/env python3
"""Whole-parameter, full-Fourier residual around a complete finite cap centre.

Finite polynomial convolutions retain their individual interval coefficients.
The global norm is sum_m sup_r, never max_r sum_m. The rational Neumann
remainder is paid separately in that global norm. All means and four driven
ports remain present; no nonlinear regular-tail identity is substituted.
"""
from __future__ import annotations
import argparse,gzip,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_box import Box,arb_box,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def total(array):return arb(float(reduce_box(Box(array)).hi)).upper()


def norm(value):return total(value.abs_upper())


def pad(value,degree):
    old=(len(value.lo)-1)//2
    if degree<old:raise ValueError('no finite-mode truncation allowed')
    result=Box(np.zeros(2*degree+1));result[degree-old:degree+old+1]=value
    return result


def convolution(a,b):
    """Exact finite convolution enclosed by directed interval operations."""
    result=Box(np.zeros(len(a.lo)+len(b.lo)-1))
    for j in range(len(a.lo)):
        if a.lo[j]==0 and a.hi[j]==0:continue
        result[j:j+len(b.lo)]=result[j:j+len(b.lo)]+a[j]*b
    return result


def polynomials(saved,nodes,piece,left,right,alpha,m):
    if not nodes[piece]<=left<=right<=nodes[piece+1]:raise ValueError('centre crosses its exact polynomial join')
    x=arb_box(real_interval(left-nodes[piece],right-nodes[piece]))
    cc=saved['piece_coefficients'][:,piece]
    value=Box(cc[0]);derivative=Box(np.zeros_like(cc[0]))
    for row in cc[1:]:
        derivative=derivative*x+value;value=value*x+Box(row)
    value=value*alpha;derivative=derivative*alpha
    zero=np.all(cc==0,axis=0);value[zero]=0;derivative[zero]=0
    def fields(v):
        b=Box(np.zeros(2*m+1));imaginary=Box(np.zeros(2*m+1));c=Box(np.zeros(2*m+1))
        b[m+1:]=v[:m]/2;b[:m]=v[:m][::-1]/2
        imaginary[m+1:]=-v[:m]/2;imaginary[:m]=v[:m][::-1]/2
        c[m]=v[m];c[m+1:]=v[m+1:]/2;c[:m]=v[m+1:][::-1]/2
        return b,imaginary,c
    return (*fields(value),*fields(derivative))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,500))
    ap.add_argument('--outer-port-budget',type=Fraction,default=Fraction(1,100000000))
    ap.add_argument('--series-order',type=int,default=3)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;tick=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve completed centred consumers and failures')
    if args.series_order<1:raise ValueError('at least one complete Neumann term is required')
    native,kernels=read(args.native),read(args.kernels)
    if (not native['complete'] or not native['cap_linear_reference_certified'] or native['failure'] is not None
        or native['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py'))):
        raise ValueError('complete actual cap coefficient native is required')
    if (kernels['kind']!='actual_all_mode_A0_cap_with_translation_regularization'
        or not kernels['complete'] or not kernels['unweighted_nonzero_rates_positive']
        or not kernels['backward_mean_rates_positive']
        or kernels['input_sha256']!=sha(args.native)
        or kernels['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_A0_translation_budget.py'))):
        raise ValueError('the actual all-mode linear kernel certificate is required')
    # The zero-centred nonlinear gate in this input is allowed to fail.
    # Only its already successful complete linear kernel construction is used.
    for doc in (native,kernels):
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('coefficient scope changed')
        for name,h in doc.get('dependency_sha256',doc.get('dependencies',{})).items():
            if sha(Path(__file__).with_name(name))!=h:raise ValueError('dependency changed: '+name)
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if native[key]!=kernels[key]:raise ValueError('target identity changed: '+key)
    left,right=map(Fraction,kernels['exact_requested_interval'])
    if right!=Fraction(25,8) or left<Fraction(18,100):raise ValueError('invalid unchanged positive-cap target')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=native['object_sha256'] or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('incorrect actual centre target/coordinates')
    nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
    if not nodes[0]<=left<right<=nodes[-1]:raise ValueError('complete centre misses a cap endpoint')
    alpha=arb_box(exact_arb(Fraction.from_float(float(meta['amplitude']))))
    degree=(args.series_order+2)*m;frequencies=4*np.arange(-degree,degree+1)
    divide=np.ones(2*degree+1);divide[frequencies!=0]=1/np.abs(frequencies[frequencies!=0])
    # The reciprocal physical integers are enclosed rather than treated as
    # exact binary numbers.
    reciprocal=Box(np.nextafter(divide,-np.inf),np.nextafter(divide,np.inf));reciprocal[degree]=0
    rbmax=np.zeros(2*degree+1);rcmax=np.zeros_like(rbmax)
    bmax=np.zeros(2*m+1);cmax=np.zeros_like(bmax);mean_residual=arb(0)
    gamma_max=beta_max=arb(0);rows=[];cursor=left
    report=dict(kind='actual_complete_nonzero_centre_cap_residual_and_contraction',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.native,args.kernels,args.candidate)},
        object_sha256=native['object_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,
        exact_requested_interval=[str(left),str(right)],covered_interval=[str(left),str(left)],
        centre_all_modes=m,complete_Neumann_order=args.series_order,finite_residual_degree=degree,
        norm='sum over all physical Fourier modes of the radial supremum; means retained',
        old_zero_ball_passed=kernels['nonlinear_contraction_certified'],rows=rows,
        nonlinear_regular_tail_matched=False,body_matched=False,periodic_frame_holonomy_proved=False,
        closed_surface_complete=False)
    save(args.out,report)
    for kernel_row in kernels['rows']:
        native_index=kernel_row['native_index'];nr=native['rows'][native_index]
        nl,nh=map(Fraction,nr['interval']);lo,hi=map(Fraction,kernel_row['interval'])
        gl,gh=map(Fraction,nr['actual_scalar_germ'])
        if lo!=cursor or not gl<=nl<=lo<hi<=nh<=gh:raise ValueError('complete scalar/germ cover changed')
        values={k:box_from_record(v) for k,v in nr['coefficients'].items()}
        if not values['Cref']<0 or not values['lambda_ref']>0:raise ValueError('strict reference chart missing')
        beta,gamma,ell,Cr=(arb_box(values[k]) for k in ('beta','gamma','lambda_ref','Cref'))
        gamma_max=max(gamma_max,values['gamma'].upper()).upper()
        beta_max=max(beta_max,abs(values['beta']).upper()).upper()
        cuts=[lo,*[x for x in nodes if lo<x<hi],hi]
        for ll,rr in zip(cuts[:-1],cuts[1:]):
            piece=min(len(nodes)-2,bisect_right(nodes,ll)-1)
            b,imag,c,br,imagr,cr=polynomials(saved,nodes,piece,ll,rr,alpha,m)
            bmax=np.maximum(bmax,b.abs_upper());cmax=np.maximum(cmax,c.abs_upper())
            P=-convolution(imag,imag)+ell*convolution(c,c)
            term=P/Cr;Q=pad(term,degree);w=-c/Cr
            for j in range(1,args.series_order+1):
                term=convolution(term,w);Q=Q+pad(term,degree)
            bp,cp,brp,crp=(pad(v,degree) for v in (b,c,br,cr))
            rb=(brp+2*beta*bp)*reciprocal-gamma*ell*cp+gamma*Q
            rc=(crp+beta*(ell+1)*cp-beta*Q)*reciprocal-gamma*bp
            rb[degree]=0;rc[degree]=0
            mean=(crp+beta*(ell+1)*cp-beta*Q)[degree]
            rbmax=np.maximum(rbmax,rb.abs_upper());rcmax=np.maximum(rcmax,rc.abs_upper())
            mean_residual=max(mean_residual,norm(mean)).upper()
            rows.append(dict(native_index=native_index,centre_piece=piece,interval=[str(ll),str(rr)],
                complete_native_interval=nr['interval'],actual_scalar_germ=nr['actual_scalar_germ'],
                centre_B_local_A0=record(norm(b)),centre_c_local_A0=record(norm(c)),
                finite_B_residual_over_frequency_local_A0=record(norm(rb)),
                finite_C_residual_over_frequency_local_A0=record(norm(rc)),
                finite_C_mean_residual=record(norm(mean))))
        cursor=hi;report['covered_interval']=[str(left),str(cursor)]
        if len(rows)%20<2:
            save(args.out,report)
            print(dict(rows=len(rows),right=str(cursor),wall_seconds=time.monotonic()-tick),flush=True)
    if cursor!=right:raise ValueError('incomplete actual cap residual cover')
    const={k:box_from_record(v) for k,v in kernels['constants'].items()}
    Bn,Cn=total(bmax),total(cmax);Cmin=const['reference_C_abs_lower'].lower()
    L=max(arb(1),const['ell_upper']).upper();ratio=(Cn/Cmin).upper()
    if not ratio<1:raise ValueError('global complete rational series does not converge')
    remainder=((Bn*Bn+L*Cn*Cn)/Cmin*ratio**(args.series_order+1)/(1-ratio)).upper()
    RB=(total(rbmax)+gamma_max*remainder).upper()
    RC=(total(rcmax)+beta_max*remainder/4).upper()
    R0=(mean_residual+beta_max*remainder).upper()
    # Exact centre right trace versus the entire genuine R74 regular line.
    last=len(nodes)-2
    b,imag,c,*_=polynomials(saved,nodes,last,right,right,alpha,m)
    entry=native['true_R74_entrance'];aR=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    qR=1/(1+(aR/(4*omega))**2).sqrt()
    fee=box_from_record(native['Jacobi']['full_frequency_interval']['complete_true_tail_fee']).upper()
    qR=qR+arb(0,fee);dr=b+arb_box(qR)*c;dr[m]=0
    budget=exact_arb(args.outer_port_budget)
    boundary=(const['boundary_d_factor']*(norm(dr)+budget)
        +budget+norm(c[m])+budget).upper()
    Dsource=(const['boundary_d_factor']/const['D_rate_per_frequency']).upper()
    Csource=(Dsource*const['q_upper']+const['boundary_c_factor']/const['C_rate_per_frequency']).upper()
    residual=(boundary+Dsource*RB+Csource*RC+const['forced_C_mean_kernel']*R0).upper()
    radius=exact_arb(args.radius);dmin=(Cmin-Cn-radius).lower()
    if not dmin>0:raise ValueError('nonzero-centred actual denominator failed')
    Bplus=(Bn+radius).upper();Cplus=(Cn+radius).upper()
    Qn=(Bplus*Bplus+L*Cplus*Cplus).upper()
    DB=(2*Bplus/dmin).upper();DC=(2*L*Cplus/dmin+Qn/(dmin*dmin)).upper()
    lip=(const['complete_pair_nonlinear_kernel']*max(DB,DC)).upper()
    image=(residual+lip*radius).upper();passed=bool(lip<1 and image<radius)
    result=dict(centre_B_global_A0=Bn,centre_c_global_A0=Cn,global_Neumann_ratio=ratio,
        complete_infinite_Neumann_remainder_A0=remainder,
        full_B_residual_over_frequency_A0=RB,full_C_residual_over_frequency_A0=RC,
        full_C_mean_residual=R0,outer_boundary_residual=boundary,
        B_source_kernel=Dsource,C_source_kernel=Csource,
        fixed_point_residual_upper=residual,correction_radius=radius,
        actual_C_abs_lower=dmin,full_Q_B_derivative=DB,full_Q_c_derivative=DC,
        full_contraction_factor=lip,closed_ball_image_upper=image,
        closed_ball_margin=(radius-image).lower(),contraction_margin=(1-lip).lower())
    report.update(complete=True,nonzero_centred_contraction_certified=passed,
        actual_driven_cap_exists=passed,failure=None if passed else 'actual full residual or full DQ contraction gate failed',
        bounds={k:record(v) for k,v in result.items()},
        complete_global_coefficient_suprema=dict(B=bmax.tolist(),c=cmax.tolist(),
            finite_B_residual_over_frequency=rbmax.tolist(),finite_C_residual_over_frequency=rcmax.tolist()),
        outer_nonzero_d_A2_budget=str(args.outer_port_budget),outer_B_mean_budget=str(args.outer_port_budget),
        outer_c_mean_budget=str(args.outer_port_budget),inner_C_nonzero_exactly_the_complete_centre=True,
        mean_at_left_is_an_output=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_A0_translation_budget.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_codazzi_rotational_cap_jacobi_v2.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        wall_seconds=time.monotonic()-tick)
    save(args.out,report);print(dict(passed=passed,rows=len(rows),
        bounds={k:v.str(14) for k,v in result.items()},wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
