#!/usr/bin/env python3
"""Complete actual fixed-label high-density Volterra block, with all head ports.

The full low-label histories and both independent means are external inputs.
This is not a full returned high inverse or a finite-head closure.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_negative_root_physical_graph_operator import mult
from fourfold_strict_high_energy_triangular import positive_matrix_bound,weighted_principal


def up(v): return stored(v).upper()
def lo(v): return stored(v).lower()


def label_comparisons(N, Cr, Cc, width, order):
    """Scalar pullback and true density pullback, keeping the L2 Jacobian."""
    H=[arb(0),Cr]+[(math.factorial(j-1)*Cc/(width/2)**(j-1)).upper()
                   for j in range(2,order+2)]
    B=[[arb(0) for _ in range(order+2)] for _ in range(order+2)]
    B[0][0]=arb(1)
    for j in range(1,order+2):
        for k in range(1,j+1):
            B[j][k]=sum((math.comb(j-1,l-1)*H[l]*B[j-l][k-1]
                         for l in range(1,j-k+2)),arb(0)).upper()
    P=acb_mat(order+1,order+1);D=acb_mat(order+1,order+1)
    for j in range(order+1):
        for k in range(j+1):
            P[j,k]=B[j][k]/arb(N)**(j-k)
            # Divide the exact density Bell coefficient by H' before
            # applying its L2 Jacobian, so the leading entry is (H')^j.
            D[j,k]=(Cr**j if k==j else Cr*B[j+1][k+1]/arb(N)**(j-k))
    scalar=[];density=[]
    for j in range(order+1):
        scalar.append((Cr.sqrt()*positive_matrix_bound(weighted_principal(P,j))).upper())
        density.append((Cr.sqrt()*positive_matrix_bound(weighted_principal(D,j))).upper())
    return H,P,D,scalar,density


def matrix_record(A):
    return [[record(A[j,k].real) for k in range(A.ncols())] for j in range(A.nrows())]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--density',type=Path,default=Path('notes/2026-11-13-R46-complete-density-transport-bootstrap.json'))
    p.add_argument('--windows',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--scales',type=int,nargs='+',default=[4096,16384,65536,1048576])
    p.add_argument('--order',type=int,default=4)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.order<2 or a.order>8 or min(a.scales)<1:
        raise ValueError('fresh output, positive scales and a finite paid angular order required')
    ctx.prec=a.bits;tick=time.monotonic()
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    d=checked(a.density,'fourfold_strict_density_transport_bootstrap.py')
    w=checked(a.windows,'fourfold_strict_windowed_density_R46.py')
    if not f['identity']==d['identity']==w['identity']:
        raise ValueError('the same complete old-object parameter family is required')
    if (d['inputs'].get(str(a.fields))!=sha(a.fields)
        or w['inputs'].get(str(a.fields))!=sha(a.fields)
        or w['inputs'].get(str(a.density))!=sha(a.density)):
        raise ValueError('the same full native fields and density identity are required')
    Cr=up(w['real_relative_derivative'])
    Cc=up(w['unchanged_complex_relative_derivative'])
    X=lo(w['unchanged_normalized_complex_flow_strip'])
    fieldwidth=4*exact_arb(Fraction(f['physical_angle_strip']))
    q=arb(0);displacement=arb(0);mm=[];mu=[];shear=[]
    cursor=Fraction(0)
    for row in f['cells']:
        l,r=Fraction(row['left']),Fraction(row['right'])
        if l!=cursor or not l<r:
            raise ValueError('the actual full strict cover has a gap')
        cursor=r;length=exact_arb(r-l)
        M={k:up(v) for k,v in row['complete_complex_field_moduli'].items()}
        mulow=lo(row['geometry']['mu_modulus_lower'])
        if not mulow>0: raise ValueError('actual density denominator lost its gap')
        # Native field named "kappa" is -K_target, not Fcal/mu.
        # The full reduced density coupling is explicitly reconstructed here.
        q+=2*length*M['Fcal']/mulow
        displacement+=8*length*(M['v']+M['nu'])
        mm.append(up(row['geometry']['m_modulus_upper']))
        mu.append(M['mu']);shear.append(M['T'])
    if len(f['cells'])!=215 or str(cursor)!=d['exact_physical_interval'][1]:
        raise ValueError('all original 215 cells and their exact reflection are required')
    q=q.upper();single_displacement=displacement.upper()
    delta_displacement=(2*single_displacement).upper()
    Mm=max(mm).upper();Mr=max(mu).sqrt().upper();MT=max(shear).upper()
    mean_row=(Cr/4+delta_displacement/8).upper()
    rows=[]
    for N in a.scales:
        H,P,D,ps,ds=label_comparisons(N,Cr,Cc,X,a.order)
        k0=(Cr*q/(4*N)).upper()
        gain=[k0.exp().upper()]
        entries=[]
        for j in range(a.order+1):
            unit=mult(N,j,arb(1),fieldwidth)
            if j==0:
                K=k0
            else:
                K=(arb(2).sqrt()*ds[j]*ps[j]*unit*q/(4*N)).upper()
                gain.append((1+K*gain[j-1]).upper())
            src=(gain[j]*ds[j]*mult(N,j,Mm,fieldwidth)/arb(2).sqrt()).upper()
            low=(gain[j]*ds[j]*unit*q/arb(2).sqrt()).upper()
            Delta=(sum((math.comb(j,k)*
                       ((delta_displacement if k==0 else 2*H[k])/arb(N)**k)**2
                        for k in range(j+1)),arb(0))).sqrt().upper()
            entries.append(dict(order=j,scalar_composition=record(ps[j]),
                complete_density_pullback=record(ds[j]),
                integrated_high_kernel=record(K),
                full_both_direction_high_Volterra_resolvent=record(gain[j]),
                ordinary_physical_source_to_high_state=record(src),
                complete_low_height_history_to_high_state=record(low),
                low_height_from_nonzero_head_state=record((ps[j]/(2*arb(2).sqrt())).upper()),
                low_height_from_mean_flux=record((Delta/4).upper()),
                low_height_from_independent_height=record(arb(1)),
                actual_inverse_label_difference_HN_norm=record(Delta),
                high_height_reconstruction_from_high_state=record((ps[j]/(2*arb(2).sqrt()*N)).upper())))
        interp={}
        for s in (Fraction(1,2),Fraction(5,6),Fraction(4,3),Fraction(3,2),Fraction(2)):
            if s>a.order:continue
            k=s.numerator//s.denominator;t=s-k
            v=gain[k] if not t else gain[k]**exact_arb(1-t)*gain[k+1]**exact_arb(t)
            interp[str(s)]=record(v.upper())
        high_u=(Mm*Cr.sqrt()/(2*arb(2).sqrt()*N)).upper()
        high_p=(Mr*(2*Cr).sqrt()+MT*high_u).upper()
        rows.append(dict(scale=N,high_frequencies='abs(n)>=N in each of the two separate actual characteristic labels',
            base_integrated_high_to_high_kernel=record(k0),
            base_kernel_less_than_one=bool(k0<1),
            base_full_Volterra_gain=record(gain[0]),
            complete_scalar_comparison_matrix=matrix_record(P),
            complete_density_comparison_matrix=matrix_record(D),
            integer_levels=entries,interpolated_high_Volterra_gains=interp,
            complete_base_physical_high_reconstruction=dict(
                u=record(high_u),physical_p=record(high_p),
                density_state_to_z_and_zeta=record((2*Cr).sqrt().upper())),
            full_integrated_high_to_head_columns=dict(
                both_nonzero_label_head_rows=record(k0),
                independent_mean_flux_row=record((q*(2*Cr).sqrt()/(8*N)).upper()),
                independent_mean_height_row=record((mean_row*q*(2*Cr).sqrt()/(4*N)).upper())),
            high_equation_closed_only_for_given_complete_low_history=True))
    out=dict(kind='actual_full_strict_fixed_label_high_density_Volterra_block',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),
        identity=d['identity'],inputs={str(z):sha(z) for z in (a.fields,a.density,a.windows)},
        native_cells_recomputed=0,positive_cells=215,exact_physical_interval=d['exact_physical_interval'],
        entire_real_affine_parameter_box=True,
        true_relative_real_derivative=record(Cr),true_relative_complex_derivative=record(Cc),
        unchanged_normalized_complex_flow_strip=record(X),normalized_field_strip=record(fieldwidth),
        complete_integrated_density_kappa=record(q),
        density_kappa_definition='Fcal/mu; native field named kappa=-K_target is explicitly not used',
        full_m_modulus=record(Mm),full_sqrt_mu_modulus=record(Mr),full_T_modulus=record(MT),
        complete_single_inverse_label_displacement=record(single_displacement),
        complete_inverse_label_difference=record(delta_displacement),
        complete_independent_height_mean_row=record(mean_row),
        variables='x=4 theta; X_sigma=H_sigma_prime*(y_sigma o H_sigma), H_sigma is the actual flow from the common left strict cut, S_sigma=H_sigma_inverse',
        exact_high_kernel='K_sigma,tau=(i*sigma/8)*P_H*(C_Ssigma)^* M_(Fcal/mu) C_Stau D^(-1)*P_H; D=-i partial_x, D^-1 mean zero',
        all_projections_in_their_actual_positions=True,
        full_low_head=['all nonzero label modes abs(n)<N in both X components',
            'alpha=<X_plus>=-<X_minus>, the actual mean zeta divided by two',
            'c, the independent scalar height integration constant'],
        exact_height='w=c+alpha*(S_plus-S_minus)/4-(i/4)*sum_sigma C_Ssigma D^-1 (X_sigma with mean removed)',
        exact_flux_mean_row='alpha_prime=0.5*mean(m*f-kappa*w)',
        exact_height_mean_row='c_prime=-alpha_prime*mean(S_plus-S_minus)/4-0.25*sum_sigma mean(C_Ssigma partial_x^-1 P_nonzero X_sigma_prime)',
        exact_nonzero_head_row='P_L X_sigma_prime=(sigma/2)*P_L*(C_Ssigma)^*(m*f-kappa*w)',
        exact_physical_reconstruction='u=m*w; z=y_plus+y_minus, zeta=y_plus-y_minus; y_sigma=(S_sigma_prime)*(X_sigma o S_sigma); p=sqrt(mu)*zeta-T*u',
        ordinary_source_scope='The original scalar density f in physical dr, pulled to x=4theta; source norm L1(dr;HN^j). No weak residual is renamed.',
        rows=rows,low_to_high_high_to_low_and_mean_paths_retained=True,
        high_inverse_conditional_on_complete_low_history_proved=True,
        complete_infinite_high_space_not_truncated=True,
        full_returned_high_remainder_proved=False,finite_head_time_problem_solved=False,
        fixed_positive_angular_weight_proved=False,full_feedback_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_root_physical_graph_operator.py','fourfold_strict_high_energy_triangular.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,Q=q.str(12),rows=[dict(N=z['scale'],base=z['base_full_Volterra_gain']['upper'],
        order_one=z['integer_levels'][1]['full_both_direction_high_Volterra_resolvent']['upper'],
        order_two=z['integer_levels'][2]['full_both_direction_high_Volterra_resolvent']['upper']) for z in rows],
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
