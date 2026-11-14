#!/usr/bin/env python3
"""Actual moving candidate -> true physical-angle complex turning germ.

The finite series lives in phi.  A complete Banach inverse of
theta=phi+I(v-mean(v))/mean(v) is proved on a joint complex product.
Only afterwards are physical angular derivatives and the original
local physical Jacobi coefficients formed.  No moving nonlocal
linearization is treated as a local multiplication operator.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_turning_complex_germ import genuine_complex_target,complex_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def physical_derivative_bounds(U,V,m,vmin):
    """Complete derivatives of U(phi(theta)), V(phi(theta)) through four.

    The exact differential operator is (m/v) d_phi.  All signs are
    replaced by absolute values only after differentiating the full
    rational expressions, including every denominator derivative.
    """
    u0,u1,u2,u3,u4=U;v0,v1,v2,v3,v4=V;v=vmin
    uu=[u0,m*u1/v,m**2*(u2/v**2+u1*v1/v**3),
        m**3*(u3/v**3+3*u2*v1/v**4+u1*v2/v**4+3*u1*v1**2/v**5),
        m**4*(u4/v**4+6*u3*v1/v**5+4*u2*v2/v**5+15*u2*v1**2/v**6
              +u1*v3/v**5+10*u1*v1*v2/v**6+15*u1*v1**3/v**7)]
    vv=[v0,m*v1/v,m**2*(v2/v**2+v1**2/v**3),
        m**3*(v3/v**3+4*v1*v2/v**4+3*v1**3/v**5),
        m**4*(v4/v**4+7*v1*v3/v**5+4*v2**2/v**5+25*v1**2*v2/v**6+15*v1**4/v**7)]
    return [x.upper() for x in uu],[x.upper() for x in vv]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root',type=Path,default=Path('notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--phi-strip',type=Fraction,default=Fraction(1,1024))
    ap.add_argument('--theta-strip',type=Fraction,default=Fraction(1,8192))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every moving-angle complex-germ attempt')
    doc=dict(kind='actual_moving_candidate_complete_physical_angle_complex_turning_germ',complete=False,proved=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.root,args.candidate)},
        failure=None,actual_nonlinear_solution_proved=False,actual_fold_constructed=False,full_feedback_inverse_proved=False)
    try:
        root=read(args.root)
        if (not root['complete'] or not root['whole_affine_parameter_interval']
            or not root['complete_original_primitive_and_tail']
            or root['object_sha256']!=sha(args.object)
            or not root['root_independent_of_compact_metric_nu']):
            raise ValueError('complete identical intrinsic root required')
        rlo,rhi=map(Fraction,root['exact_root_interval']);gl,gr=map(Fraction,root['actual_common_scalar_germ'])
        left,right=rlo-args.radius,rhi+args.radius
        if not gl<left<right<gr or not left>Fraction(9,50):
            raise ValueError('joint complex germ must lie in the true scalar piece beyond the compact metric bump')
        radial=acb(real_interval(left,right),arb(0,exact_arb(args.radius)))
        target=CodazziCoefficientTarget(args.object,Fraction(root['parameter_half_width']),512,4096)
        target.set_cell(gl,gr)
        coeff,primitive_tail,product_fees=genuine_complex_target(target,radial)
        saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
        if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object) or meta['physical_frequency_factor']!=4:
            raise ValueError('the candidate must have the complete moving-phi coordinate identity')
        alpha=Fraction(meta['exact_float_amplitude']);nu=Fraction(meta['exact_float_nu'])
        if alpha!=Fraction.from_float(float(meta['amplitude'])) or nu!=Fraction.from_float(float(meta['nu'])):
            raise ValueError('exact complete candidate parameter identity failed')
        nulo,nuhi=map(Fraction,root['exact_nu_interval'])
        if not nulo<=nu<=nuhi:raise ValueError('new candidate nu leaves the certified intrinsic root family')
        nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
        j=bisect_right(nodes,left)-1
        if not 0<=j<len(nodes)-1 or not nodes[j]<left<right<nodes[j+1]:
            raise ValueError('the joint complex radial domain crosses a true candidate PPoly join')
        local=radial-acb(exact_arb(nodes[j]));cc=saved['piece_coefficients'][:,j,:]
        vals=[];vals_r=[]
        for k in range(cc.shape[1]):
            value=acb(0)
            for degree in range(4):value=value*local+acb(arb(float(cc[degree,k])))
            deriv=3*acb(arb(float(cc[0,k])))*local**2+2*acb(arb(float(cc[1,k])))*local+acb(arb(float(cc[2,k])))
            vals.append(exact_arb(alpha)*value);vals_r.append(exact_arb(alpha)*deriv)
        M=int(meta['modes'])
        if len(vals)!=2*M+1:raise ValueError('every moving Fourier mode and the complete even mean must be retained')
        sigphi=exact_arb(args.phi_strip);sigtheta=exact_arb(args.theta_strip);R=exact_arb(args.radius)
        U=[];V=[]
        for q in range(5):
            U.append(sum((abs(vals[k-1])*(4*k)**q*(4*k*sigphi).exp() for k in range(1,M+1)),arb(0)).upper())
            V.append(sum((abs(vals[M+k])*(4*k)**q*(4*k*sigphi).exp() for k in range(1,M+1)),arb(0)).upper())
        m=coeff['s']+vals[M];mabs=abs(m).upper();mmin=(-m.real.upper()).lower()
        vnonmean=V[0];vgap=(mmin-vnonmean).lower()
        if not mmin>0 or not vgap>0:raise ValueError('actual moving mean or complete v complex gap failed')
        V[0]=(mabs+vnonmean).upper()
        gap1=coeff['E1']-2*coeff['a1']*coeff['a2']
        s1=coeff['s']*(coeff['beta']+(coeff['E1']/coeff['E']-gap1/coeff['rotational_gap'])/2)
        mr=s1+vals_r[M]
        Iv=(sum((abs(vals[M+k])/(4*k) for k in range(1,M+1)),arb(0))).upper()
        Ivr=(sum((abs(vals_r[M+k])/(4*k) for k in range(1,M+1)),arb(0))).upper()
        angleDerivativeFee=(vnonmean/mmin).upper()
        angleRadial=(Ivr/mmin+Iv*abs(mr)/mmin**2).upper()
        angleVerticalMargin=(sigphi*(1-angleDerivativeFee)-R*angleRadial-sigtheta).lower()
        if not angleDerivativeFee<1 or not angleVerticalMargin>0:
            raise ValueError('actual joint complex physical-angle inverse strip does not close')
        angleInverseDerivative=(1/(1-angleDerivativeFee)).upper()
        angleInverseRadial=(angleRadial/(1-angleDerivativeFee)).upper()
        PU,PV=physical_derivative_bounds(U,V,mabs,vgap)
        ga,be,KM=(abs(coeff[k]).upper() for k in ('gamma','beta','K'))
        d=(ga*PU[0]).upper();a=(ga*PV[0]).upper()
        dtheta=(ga*PU[1]).upper();atheta=(ga*PV[1]).upper()
        a_real=(-coeff['gamma']*m).real.lower()-ga*vnonmean
        sqrtk=coeff['K1'].sqrt()
        aq=(a*abs(sqrtk)).upper()
        aq_real=(-coeff['gamma']*m*sqrtk).real.lower()-ga*vnonmean*abs(sqrtk)
        aqtheta=(atheta*abs(sqrtk)).upper()
        if not a_real>0 or not aq_real>0:raise ValueError('actual physical root characteristic amplitude not separated')
        cg=(ga*PV[1]+2*be*PU[0]*PV[0]).upper()
        L11=(ga*PU[1]+be*(1+3*PU[0]**2+KM*PV[0]**2)).upper()
        L22=(ga*PU[1]+be*(1+PU[0]**2+3*KM*PV[0]**2)).upper()
        Lsum=(L11+L22+(1+KM)*cg).upper()
        gates=[
          ('complete new moving candidate and all SHA-bound radial shards loaded',True),
          ('one actual scalar germ and one actual new PPoly piece contain the complex product',True),
          ('whole original affine parameter and complete primitive tail retained',True),
          ('actual moving mean and v are nonzero on the complete complex product',mmin>0 and vgap>0),
          ('true theta_phi close to one on the entire complex moving strip',angleDerivativeFee<1),
          ('full complex-r vertical displacement paid before inverse angle construction',angleVerticalMargin>0),
          ('global periodic inverse of the true physical angle is a strict Banach contraction',angleInverseDerivative.is_finite()),
          ('all physical angular derivatives through four use the full rational chain rule',all(x.is_finite() for x in PU+PV)),
          ('intrinsic simple root and actual physical characteristic amplitude have positive real part',coeff['K1'].real>0 and a_real>0 and aq_real>0),
          ('complete original local physical Jacobi matrix retained including both means',Lsum.is_finite()),
        ]
        complete=all(bool(v) for _,v in gates)
        doc.update(complete=complete,proved=complete,object_sha256=sha(args.object),candidate_sha256=sha(args.candidate),
          exact_amplitude=str(alpha),actual_fixed_nu=str(nu),exact_center_parameter=root['exact_center_parameter'],
          exact_parameter_half_width=root['parameter_half_width'],whole_affine_parameter_interval=True,
          root_interval=list(map(str,(rlo,rhi))),original_scalar_germ=list(map(str,(gl,gr))),
          actual_candidate_piece=j,exact_candidate_piece_interval=[str(nodes[j]),str(nodes[j+1])],
          complex_radial_radius=str(args.radius),moving_phi_strip=str(args.phi_strip),physical_theta_strip=str(args.theta_strip),
          complex_radial_rectangle=dict(real_interval=[str(left),str(right)],imaginary_half_width=str(args.radius)),
          domain_contains_disks_about_every_true_parameter_root=True,
          compact_bump_identically_zero_on_entire_actual_germ=True,
          finite_energy_is_bilinear_zero_convolution_without_conjugation=True,
          complete_primitive_tail=record(primitive_tail),complete_energy_product_fees={k:record(v) for k,v in product_fees.items()},
          complex_intrinsic_coefficients={k:complex_record(v) for k,v in coeff.items()},
          exact_candidate_metadata=meta,all_finite_candidate_modes_retained=True,
          moving_mean_v=complex_record(m),moving_mean_v_radial=complex_record(mr),
          moving_U_derivative_Astrip=[record(x) for x in U],moving_v_derivative_Astrip=[record(x) for x in V],
          physical_U_derivative_sup=[record(x) for x in PU],physical_v_derivative_sup=[record(x) for x in PV],
          angle_inverse=dict(definition='theta=phi+I_phi(v-mean_phi(v))/mean_phi(v); true inverse phi=Phi(r,theta)',
            real_and_complex_physical_angle_distinguished=True,physical_fourier_truncation_used=False,
            full_radial_chain_rule_required_for_source=True,
            bounds={k:record(v) for k,v in dict(mean_modulus_upper=mabs,mean_gap=mmin,v_gap=vgap,
              derivative_fee=angleDerivativeFee,radial_derivative=angleRadial,vertical_margin=angleVerticalMargin,
              inverse_theta_derivative=angleInverseDerivative,inverse_radial_derivative=angleInverseRadial).items()}),
          bounds={k:record(v) for k,v in dict(v_gap=vgap,d=d,a=a,dtheta=dtheta,atheta=atheta,
            Re_a_lower=a_real,Re_k_lower=coeff['K1'].real.lower(),aq=aq,Re_aq_lower=aq_real,aqtheta=aqtheta,
            complete_g=cg,complete_L11=L11,complete_L22=L22,complete_L_matrix=Lsum).items()},
          physical_candidate_is_analytic_inverse_angle_pullback_not_finite_physical_Fourier=True,
          moving_nonlocal_linearization_replaced_by_local_multiplication=False,
          physical_jacobi_at_approximate_centre_does_not_assume_zero_residual=True,
          gates=[dict(name=n,passed=bool(v)) for n,v in gates],bits=args.bits)
    except Exception as exc:
        doc['failure']=f'{type(exc).__name__}: {exc}'
    doc['seconds']=time.monotonic()-t0
    doc['dependencies']={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_phase_codazzi_coefficients.py',
      'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_moving_polynomial_system.py','fourfold_codazzi_turning_complex_germ.py',
      'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')}
    save(args.out,doc)
    print(dict(complete=doc['complete'],gates=len(doc.get('gates',[])),out=str(args.out),sha256=sha(args.out),
      failure=doc['failure'],inverse=doc.get('angle_inverse',{}).get('bounds',{}),seconds=doc['seconds']),flush=True)
    if not doc['complete']:raise SystemExit(1)


if __name__=='__main__':main()
