#!/usr/bin/env python3
"""Actual fixed-label high propagator: real first phase and two-window order two.

The complete low-label histories remain independent external inputs.  The
result is the same infinite high Volterra block, not a returned feedback inverse.
No native geometry is recomputed.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_negative_root_physical_graph_operator import mult
from fourfold_strict_high_energy_triangular import positive_matrix_bound, weighted_principal
from fourfold_actual_label_high_density_volterra import label_comparisons


def up(v): return stored(v).upper()
def lo(v): return stored(v).lower()


def derivative_multiplier(N, order, derivative_bounds):
    T=acb_mat(order+1,order+1)
    for j in range(order+1):
        for k in range(j+1):
            T[j,k]=math.comb(j,k)*derivative_bounds[j-k]/arb(N)**(j-k)
    return max(positive_matrix_bound(weighted_principal(T,j))
               for j in range(order+1)).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    ap.add_argument('--high',type=Path,default=Path('notes/2026-11-13-actual-fixed-label-high-density-Volterra.json'))
    ap.add_argument('--scales',type=int,nargs='+',default=[4096,16384,65536,1048576,2**30,2**40])
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or min(a.scales)<1:
        raise ValueError('a fresh output and positive cutoffs are required')
    ctx.prec=a.bits;tick=time.monotonic()
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    h=checked(a.high,'fourfold_actual_label_high_density_volterra.py')
    if f['identity']!=h['identity'] or h['inputs'].get(str(a.fields))!=sha(a.fields):
        raise ValueError('the same complete actual native object is required')
    Cr=up(h['true_relative_real_derivative'])
    Cc=up(h['true_relative_complex_derivative'])
    X=lo(h['unchanged_normalized_complex_flow_strip'])
    sf=lo(h['normalized_field_strip'])
    qk=arb(0);qQ=arb(0);maxR=arb(0);maxInvNu=arb(0)
    cells=[];cursor=Fraction(0)
    for row in f['cells']:
        left,right=Fraction(row['left']),Fraction(row['right'])
        if left!=cursor or not left<right:raise ValueError('actual native cover has a gap')
        cursor=right;length=exact_arb(right-left)
        M={k:up(v) for k,v in row['complete_complex_field_moduli'].items()}
        J={k:{t:up(v) for t,v in z.items()}
           for k,z in row['complete_complex_first_derivative_moduli'].items()}
        mu=lo(row['geometry']['mu_modulus_lower'])
        if not mu>0:raise ValueError('the complete actual density denominator has no gap')
        kappa=M['Fcal']/mu
        R=M['a']*M['Fcal']/mu**2
        Rr=((J['a']['radial']*M['Fcal']+M['a']*J['Fcal']['radial'])/mu**2
             +2*M['a']*M['Fcal']*J['mu']['radial']/mu**3)
        Rt=((J['a']['angular']*M['Fcal']+M['a']*J['Fcal']['angular'])/mu**2
             +2*M['a']*M['Fcal']*J['mu']['angular']/mu**3)
        Q=(Rr+(M['v']+M['nu'])*Rt+2*J['v']['angular']*R).upper()
        qk+=2*length*kappa;qQ+=2*length*Q
        maxR=max(maxR,R.upper());maxInvNu=max(maxInvNu,(M['a']/mu).upper())
        cells.append(dict(left=str(left),right=str(right),
            full_kappa_modulus=record(kappa.upper()),
            full_cleared_ratio_a_Fcal_over_mu_squared=record(R.upper()),
            full_ratio_radial_derivative=record(Rr.upper()),
            full_ratio_physical_angle_derivative=record(Rt.upper()),
            complete_material_ratio_derivative_Q=record(Q)))
    if len(cells)!=215 or str(cursor)!=h['exact_physical_interval'][1]:
        raise ValueError('all 215 cells and their exact reflection are required')
    qk,qQ,maxR,maxInvNu=(z.upper() for z in (qk,qQ,maxR,maxInvNu))
    if not qk.overlaps(stored(h['complete_integrated_density_kappa'])):
        raise ValueError('the actual complete density integral changed')
    H2=Cc/(X/2);H3=2*Cc/(X/2)**2;H4=6*Cc/(X/2)**3
    jac=[Cr,H2,H3]
    logjac=[Cr*H2,Cr*H3+Cr**2*H2**2,
            Cr*H4+3*Cr**2*H3*H2+2*Cr**3*H2**3]
    rows=[]
    for N in a.scales:
        H,P,D,ps,ds=label_comparisons(N,Cr,Cc,X,2)
        unit=[mult(N,j,arb(1),sf) for j in range(3)]
        jm=[derivative_multiplier(N,j,jac) for j in range(3)]
        lm=[derivative_multiplier(N,j,logjac) for j in range(3)]
        k0=(Cr*qk/(4*N)).upper();G=k0.exp().upper()
        # Forward one-order kernels use comparison at the output level.
        kf=[None]+[(arb(2).sqrt()*ds[j]*ps[j]*unit[j]*qk/(4*N)).upper()
                   for j in (1,2)]
        # The adjoint primitive is on the left, so the interior comparison
        # is one level lower. A right Duhamel expansion keeps T* at base.
        ka=[None]+[(arb(2).sqrt()*ds[j-1]*ps[j-1]*unit[j-1]*qk/(4*N)).upper()
                   for j in (1,2)]
        E=[(ds[j]*ps[j]*unit[j]*jm[j]*maxR/64).upper() for j in range(3)]
        Z=[(ds[j]*ps[j]*unit[j]*(jm[j]*qQ/64+lm[j]*qk/8)).upper()
           for j in range(3)]
        cross0=((2*E[0]+Z[0])/arb(N)**2).upper()
        cross0=min(cross0,(k0/2).upper())
        crossplus=(2*(2*E[2]+Z[2])/arb(N)**2).upper()
        crossminus=(2*(2*E[0]+Z[0])/arb(N)**2).upper()
        dyson0=(G-1-k0).upper()
        # Also save the direct noncancelling positive upper formula.
        dyson0=min(dyson0,(k0*k0*G/2).upper())
        dysonplus=(kf[2]*kf[1]*G/2).upper()
        dysonminus=(ka[2]*ka[1]*G/2).upper()
        R0=(cross0+dyson0).upper()
        Rp=(crossplus+dysonplus).upper()
        Rm=(crossminus+dysonminus).upper()
        Rgp=(R0**(arb(1)/3)*Rp**(arb(2)/3)).upper()
        Rgm=(R0**(arb(1)/3)*Rm**(arb(2)/3)).upper()
        src0=(Cr.sqrt()*up(h['full_m_modulus'])/arb(2).sqrt()).upper()
        low0=(Cr.sqrt()*qk/arb(2).sqrt()).upper()
        srcminus=(ps[2]*mult(N,2,up(h['full_m_modulus']),sf)/arb(2).sqrt()).upper()
        lowminus=(ps[2]*unit[2]*qk/arb(2).sqrt()).upper()
        rows.append(dict(scale=N,base_high_gain=record(G),
            first_real_diagonal_phase_modulus=record((Cr*qk/8).upper()),
            forward_one_order_kernel_integrals=[record(kf[j]) for j in (1,2)],
            adjoint_one_order_kernel_integrals=[record(ka[j]) for j in (1,2)],
            actual_flow_jacobian_multiplier=[record(z) for z in jm],
            actual_flow_log_jacobian_derivative_multiplier=[record(z) for z in lm],
            full_cross_endpoint_constants=[record(z) for z in E],
            full_cross_material_derivative_integrals=[record(z) for z in Z],
            cross_first_Born_base=record(cross0),
            cross_first_Born_forward_two=record(crossplus),
            cross_first_Born_opposite_two=record(crossminus),
            higher_Born_base=record(dyson0),
            higher_Born_forward_two=record(dysonplus),
            higher_Born_opposite_two=record(dysonminus),
            complete_remainder_base=record(R0),
            complete_remainder_forward_two=record(Rp),
            complete_remainder_opposite_two=record(Rm),
            complete_remainder_forward_four_thirds=record(Rgp),
            complete_remainder_opposite_four_thirds=record(Rgm),
            ordinary_physical_source_error_forward_two=record((Rp*src0).upper()),
            low_height_history_error_forward_two=record((Rp*low0).upper()),
            ordinary_physical_source_error_opposite_two=record((Rm*srcminus).upper()),
            low_height_history_error_opposite_two=record((Rm*lowminus).upper()),
            source_kernel_is_the_same_actual_subinterval_propagator=True))
    out=dict(kind='actual_fixed_label_high_density_first_phase_two_window_order_two',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),
        identity=h['identity'],inputs={str(z):sha(z) for z in (a.fields,a.high)},
        entire_real_parameter_box=True,complete_continuous_native_cover=True,
        native_cells_recomputed=0,positive_cells=215,
        exact_physical_interval=h['exact_physical_interval'],
        full_integrated_density_kappa=record(qk),
        full_integrated_material_ratio_derivative=record(qQ),
        full_ratio_modulus=record(maxR),
        true_nonstationary_inverse_speed_bound=record((maxInvNu*Cr/8).upper()),
        exact_cross_label='F_sigma,tau=S_tau o H_sigma, tau=-sigma',
        exact_cross_label_radial_velocity='F_r=-8*sigma*(nu*S_tau_prime) o H_sigma',
        exact_cleared_ratio='R=kappa/nu=a*Fcal/mu^2',
        exact_material_ratio='Q_sigma=R_r+(v-sigma*nu)*R_theta+2*v_theta*R',
        exact_cross_boundary_operator='L_sigma,tau=-(1/64)*P_H*D_Hsigma*M_R*C_Stau*M_Htau_prime*D^-2*P_H',
        exact_cross_amplitude_derivative_operator='Z_sigma,tau=-(1/64)*P_H*D_Hsigma*M_Qsigma*C_Stau*M_Htau_prime*D^-2*P_H+(sigma/8)*P_H*D_Hsigma*M_kappa*C_Stau*M_(Htau_double_prime/Htau_prime)*D^-2*P_H',
        exact_cross_first_Born='integral K_cross=L(t)-L(s)-integral Z',
        exact_real_phase='A_sigma(t,s)=sigma/8*integral_s^t Hsigma_prime*(kappa o Hsigma) dr',
        exact_high_propagator='T_H(t,s)=I+diag(i*P_H*M_Asigma*D^-1*P_H)+R_H(t,s)',
        exact_affine_source='X_H(t)=T_H(t,s)X_H(s)+integral_s^t T_H(t,r)*F_H(r) dr; F_H retains both complete low histories and both independent means',
        both_direction_all_subinterval_bounds=True,both_complete_two_order_windows=True,
        flow_jacobian_derivative_moduli=[record(z.upper()) for z in jac],
        flow_log_jacobian_derivative_moduli=[record(z.upper()) for z in logjac],
        every_head_mean_and_source_projection_unchanged=True,
        cells=cells,rows=rows,
        all_frequency_high_space_not_finite_truncation=True,
        low_head_time_problem_solved=False,full_returned_remainder_proved=False,
        final_circle_phase_identification_claimed=False,
        full_feedback_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_root_physical_graph_operator.py','fourfold_strict_high_energy_triangular.py',
            'fourfold_actual_label_high_density_volterra.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,Qkappa=qk.str(12),QQ=qQ.str(12),ratio=maxR.str(12),
        rows=[dict(N=z['scale'],base=z['complete_remainder_base']['upper'],
                   forward_two=z['complete_remainder_forward_two']['upper'],
                   opposite_two=z['complete_remainder_opposite_two']['upper']) for z in rows],
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
