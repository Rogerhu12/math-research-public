#!/usr/bin/env python3
"""Actual root-germ complex angular inverse with every Fourier mode paid.

The radial domain is real and lies in the proved common scalar/candidate
germ. A finite exact dyadic inverse proposal is certified in the complete
weighted Wiener algebra. The curvature-angle inverse is then certified on
an explicit complex strip. This supplies no complex radial disk or PDE
existence theorem.
"""
from __future__ import annotations
import argparse,gzip,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_curvature_angle_energy_prefix import polynomial_ranges,dyadic
from fourfold_codazzi_reciprocal_Wiener_boundary import Laurent,finite_inverse_proposal
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def finite_fields(values,m,alpha,s):
    u=[acb(0)]*(2*m+1);v=[acb(0)]*(2*m+1)
    v[m]=acb(s+alpha*values[m])
    for j in range(1,m+1):
        b=alpha*values[j-1]/2;c=alpha*values[m+j]/2
        u[m+j]=acb(0,-b);u[m-j]=acb(0,b)
        v[m+j]=v[m-j]=acb(c)
    return Laurent(-m,u),Laurent(-m,v)


def norm(poly,weights,order=0):
    return sum((abs(z)*weights[abs(j)]*(4*abs(j))**order for j,z in
        zip(range(poly.lower,poly.upper+1),poly.coefficients)),arb(0)).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root',type=Path,default=Path('notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz'))
    ap.add_argument('--sigma',type=Fraction,default=Fraction(1,1024))
    ap.add_argument('--parts',type=int,default=8)
    ap.add_argument('--inverse-degree',type=int,default=1024)
    ap.add_argument('--proposal-grid',type=int,default=8192)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve every genuine angular-domain attempt')
    root=read(args.root);saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if (not root['complete'] or root['object_sha256']!=sha(args.object)
        or meta['object_sha256']!=sha(args.object) or meta['coordinates']!=COORDINATES):
        raise ValueError('the complete actual root and candidate identities differ')
    if not any(row['candidate_sha256']==sha(args.candidate) for row in root['candidate_germs']):
        raise ValueError('this actual complete candidate was not checked against the common root germ')
    if args.parts<=0 or args.sigma<=0:raise ValueError('positive real subdivision and angular width required')
    gl,gr=map(Fraction,root['common_real_analytic_germ'])
    # Stay strictly inside the common polynomial germ, so neither endpoint
    # is silently assigned a different side of a saved PPoly interface.
    padding=Fraction(1,10**8);left,right=gl+padding,gr-padding
    rl,rr=map(Fraction,root['exact_root_interval'])
    if not left<rl<rr<right:raise ValueError('the full true root must remain inside this real collar')
    nodes=list(map(dyadic,saved['radial_nodes']));piece=bisect_right(nodes,left)-1
    if not nodes[piece]<left<right<nodes[piece+1]:raise ValueError('the actual centre does not have one polynomial germ')
    m=int(meta['modes']);alpha=exact_arb(dyadic(meta['amplitude']));sigma=exact_arb(args.sigma)
    weights=[(4*j*sigma).exp().upper() for j in range(m+args.inverse_degree+1)]
    target=CodazziCoefficientTarget(args.object,Fraction(root['parameter_half_width']),512,4096)
    doc=dict(kind='actual_whole_eta_root_germ_complex_angular_inverse',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.candidate,args.object,args.root)},
        object_sha256=sha(args.object),candidate_metadata=meta,actual_fixed_nu=meta['exact_float_nu'],
        exact_affine_center=root['exact_center_parameter'],parameter_half_width=root['parameter_half_width'],
        whole_affine_parameter_interval=True,complete_original_primitive_tail=True,
        exact_real_radial_interval=[str(left),str(right)],entire_true_root_box=root['exact_root_interval'],
        exact_actual_candidate_piece=piece,exact_common_scalar_germ=root['actual_common_scalar_germ'],
        exact_physical_theta_strip=str(args.sigma),radial_parts=args.parts,
        complete_infinite_Wiener_inverse=True,complex_radial_domain_not_certified=True,
        true_PDE_or_turning_operator_not_proved=True,original_finite_BVP_outcome_not_changed=True,
        rows=[],failure=None,dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_reciprocal_candidate_tools.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
            'fourfold_codazzi_reciprocal_Wiener_boundary.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_metric_defect.py')})
    try:
        for i in range(args.parts):
            lo=left+(right-left)*i/args.parts;hi=left+(right-left)*(i+1)/args.parts
            c=target.coefficients(lo,hi)
            if list(map(str,target.cell))!=root['actual_common_scalar_germ']:
                raise ValueError('the real collar left the actual common scalar germ')
            gap=c['E']-c['a1']**2
            if not c['a']>0 or not c['E']>0 or not gap>0:raise ValueError('the true rotational chart is unresolved')
            s=-c['a']*(c['E']/gap).sqrt()
            y,_=polynomial_ranges(saved,nodes,piece,lo,hi);u,v=finite_fields(y,m,alpha,s)
            W,positive,info=finite_inverse_proposal(v,args.inverse_degree,args.proposal_grid)
            error=Laurent(0,[1])-v*W
            e0=norm(error,weights);e1=norm(error,weights,1)
            if not e0<1:raise ValueError('the entire weighted Wiener Neumann gate failed')
            W0=norm(W,weights);W1=norm(W,weights,1);v1=norm(v,weights,1)
            I0=(W0/(1-e0)).upper();I1raw=(I0*I0*v1).upper()
            T1=(I1raw*e0+I0*e1).upper();I1=min(I1raw,(W1+T1).upper()).upper()
            epsA0=error.norm();I0A0=(W.norm()/(1-epsA0)).upper();T0A0=(I0A0*epsA0).upper()
            D=W.get(0).real+arb(0,T0A0)
            negative=sum(v.coefficients,acb(0))
            if not negative.imag.contains(0) or not negative.real<0 or not D<0:
                raise ValueError('the true negative real inverse or its complete mean is unresolved')
            v0=v.norm();dmin=(-D).lower();dmax=abs(D).upper()
            derivative_lower=(1/(v0*dmax)).lower()
            second_upper=(I1/dmin).upper()
            tau=min((sigma/2).lower(),(derivative_lower/(4*second_upper)).lower()).lower()
            rho=(derivative_lower*tau/2).lower()
            if not tau>0 or not rho>0:raise ValueError('the complete curvature-angle inverse strip collapsed')
            out=dict(interval=[str(lo),str(hi)],actual_scalar_germ=list(map(str,target.cell)),
                actual_target={k:record(c[k]) for k in ('a','a1','E','K','K1','primitive_tail')},
                actual_s=record(s),proposal=info,W_nonnegative_exact_float_coefficients=positive,
                complete_residual_support=[error.lower,error.upper],
                bounds={name:record(value) for name,value in dict(
                    full_Wiener_residual_A_sigma=e0,full_Wiener_residual_derivative_A_sigma=e1,
                    full_C_A_sigma=I0,full_C_theta_A_sigma=I1,
                    full_C_A0=I0A0,full_C_minus_W_A0=T0A0,
                    true_complete_mean_C=D,full_u_A_sigma=norm(u,weights),full_v_A_sigma=norm(v,weights),
                    real_phi_theta_lower=derivative_lower,complex_phi_second_derivative_upper=second_upper,
                    theta_univalence_strip=tau,inverse_phi_strip=rho,
                    inverse_theta_derivative_upper=(4/(3*derivative_lower)).upper(),
                    complete_A_half_rho_composition_fee=(1/rho.tanh()).upper()).items()})
            doc['rows'].append(out)
            doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
            print(dict(row=i+1,eps=e0.str(10),rho=rho.str(10)),flush=True)
        from fourfold_codazzi_rotational_cap_jacobi import box_from_record
        minima=('real_phi_theta_lower','theta_univalence_strip','inverse_phi_strip')
        maxima=('full_Wiener_residual_A_sigma','full_C_A_sigma','full_C_theta_A_sigma',
                'full_u_A_sigma','full_v_A_sigma','inverse_theta_derivative_upper')
        global_bounds={k:record(min(box_from_record(r['bounds'][k]).lower() for r in doc['rows']).lower()) for k in minima}
        global_bounds.update({k:record(max(box_from_record(r['bounds'][k]).upper() for r in doc['rows']).upper()) for k in maxima})
        rho=box_from_record(global_bounds['inverse_phi_strip']).lower()
        global_bounds['complete_A_half_rho_composition_fee']=record((1/rho.tanh()).upper())
        doc.update(complete=True,all_real_radial_closed_boxes_passed=True,
            all_complex_angular_strips_and_infinite_inverse_tails_paid=True,global_bounds=global_bounds)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
        bounds=doc.get('global_bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
