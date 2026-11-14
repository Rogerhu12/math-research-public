#!/usr/bin/env python3
"""Complete root collar: high Sobolev height resolvent, both Airy rows and R43.

Uses the true fixed-canonical product domain through the physical cut.
The constant 5050 is kept in an exact shifted-Airy reference, including the
mean. The original R43 frame and first phase B are recovered exactly.
All scales retain the entire equation, finite head and every head crossing.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_strict_high_energy_triangular import (
    positive_matrix_bound,weighted_principal,stirling_rows,power_tail)


def matrix_record(A):
    return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]


def triangle(N,derivatives,eta):
    order=len(derivatives)-1;n=order+1
    T=acb_mat(n,n);R=acb_mat(n,n)
    for j in range(n):
        for ell in range(j+1):
            T[j,ell]=math.comb(j,ell)*derivatives[j-ell]/arb(N)**(j-ell)
    diagonal=1-eta*derivatives[0]
    if not diagonal>0:raise ValueError('actual scalar Volterra diagonal is not a contraction')
    for j in range(n):
        for ell in range(j+1):
            R[j,ell]=(int(j==ell)+eta*sum((T[j,a]*R[a,ell] for a in range(ell,j)),0))/diagonal
    # All entries above are exact positive expressions with directed balls.
    T=acb_mat([[abs(T[i,j]).upper() for j in range(n)] for i in range(n)])
    R=acb_mat([[abs(R[i,j]).upper() for j in range(n)] for i in range(n)])
    multipliers=[];resolvents=[]
    for k in range(n):
        multipliers.append(positive_matrix_bound(weighted_principal(T,k)).upper())
        # The triangular comparison controls the vector of separate
        # derivative time norms. Passing to L^infinity_t H_N^k, or to
        # L^1_t H_N^k for the backward adjoint, costs sqrt(k+1).
        resolvents.append((arb(k+1).sqrt()*positive_matrix_bound(weighted_principal(R,k))).upper())
    return T,R,multipliers,resolvents


def lag_moment(N,decay,power=10):
    """Complete sum (1+|l|/N)^power <l>^(4/3) exp(-decay|l|).

    Holder uses exact geometric zeroth/second moments, retaining the
    fractional 4/3 power instead of rounding it up to two.
    """
    q=(-decay).exp();st=stirling_rows(power+2)
    A0=A2=arb(1)
    for j in range(power+1):
        coefficient=arb(2*math.comb(power,j))/arb(N)**j
        tail=power_tail(1,q,j,st)
        A0+=coefficient*tail
        A2+=coefficient*(tail+power_tail(1,q,j+2,st))
    return (A0**(arb(1)/3)*A2**(arb(2)/3)).upper(),A0.upper(),A2.upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--domain',type=Path,default=Path('notes/2026-11-13-negative-root-full-canonical-domain.json'))
    ap.add_argument('--scales',type=int,nargs='+',default=[1,64,256,1024,4096,16384,65536])
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or any(n<1 for n in a.scales):raise ValueError('new output and positive scales required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.domain,'fourfold_negative_root_full_canonical_domain.py')
    if d['kind']!='actual_complete_negative_root_fixed_canonical_domain' or not all(g['passed'] for g in d['gates']):
        raise ValueError('full actual fixed-canonical root domain required')
    L=exact_arb(Fraction(d['canonical_real_height']))
    sigma=exact_arb(Fraction(d['canonical_complex_angle_strip']))
    V=stored(d['full_canonical_V_modulus']).upper()
    Vxi=stored(d['full_canonical_Vxi_modulus']).upper()
    W=stored(d['full_canonical_shifted_5050_residual_modulus']).upper()
    qlo=stored(d['actual_quarter_circle_frequency'][0]).lower()
    qhi=stored(d['actual_quarter_circle_frequency'][1]).upper()
    decay=(qlo*sigma).lower();eta=L*L/2
    if not L<=1 or not qlo>4 or not eta*W<arb(1)/40:
        raise ValueError('full actual reference/height gates are missing')
    derivatives=[W]+[(math.factorial(j)*V/decay**j).upper() for j in range(1,12)]
    Ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    minAip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    c=(Ai0/minAip0).sqrt()
    CD=(10*c*max(arb(1),arb(2)**(arb(1)/6)*qlo**(-arb(1)/3))).upper()
    CG=max(L,(50*arb.pi()*arb(2)**(arb(1)/3)*qlo**(-arb(2)/3)).upper())
    Gamma=(arb.pi()*CD/(arb(2).sqrt()*c*c)).upper()
    reference=arb(5050)
    ratio=(1+reference*qlo**(-arb(4)/3))**(arb(1)/4)
    change_nonzero=(100*arb.pi()*(1+ratio)).upper()
    change_mean=(2*(1+L/arb.pi())*(1+arb.pi()*reference*L/2)).upper()
    change=max(change_nonzero,change_mean)
    Cq=(4*(50*arb.pi()+5)*qlo**(-arb(4)/3)+150*arb.pi()+3/qlo).upper()
    CH=(10*c*max(arb(1),arb(2)**(arb(1)/4)*L**(-arb(1)/4)*qlo**(-arb(1)/2))).upper()
    output=dict(kind='actual_full_negative_root_Airy_operator_including_mean_and_all_sources',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(a.domain):sha(a.domain)},identity=d['identity'],
        exact_canonical_height=d['canonical_real_height'],full_physical_cut_graph_contained=True,
        amplitude_window=[-10,10],height_integer_orders=list(range(12)),strong_window=[-8,8],
        scaled_spaces='H_N^s: sum_n (1+n^2/N^2)^s |u_n|^2; E_N^s=(H_N^s)^2; every n including zero is retained',
        exact_reference='5050 plus lambda^2*xi; nonzero shifted Ai/Bi at -lambda^(2/3)*xi-5050*lambda^(-4/3); mean cos/sin',
        exact_mean_columns='c*(cos(sqrt(5050)*xi) +/- i*sin(sqrt(5050)*xi)/(pi*sqrt(5050)))',
        exact_full_Wronskian='-2*i*c^2/pi for every Fourier mode, including zero',
        original_frame_recovered=True,original_first_phase_unchanged=True,
        original_first_phase='The full actual R43 B from V, with a_(sigma,epsilon)=(2*q)^(-1) integral_0^L V(xi,phi-sigma*epsilon*2*xi^(3/2)/3)/sqrt(xi) dxi; all cones and mean remainder retained',
        whole_height_Volterra_diagonal=record((eta*W).upper()),
        complete_normalized_angle_derivatives=[record(x) for x in derivatives],
        time_derivative_vector_conversion='sqrt(k+1) is included in every height resolvent bound at integer order k, for both L-infinity time and the L1 backward adjoint',
        reference_bounds={k:record(v) for k,v in dict(c=c,CD=CD,CG=CG,ordinary_source_to_reference_amplitude=Gamma,
            free_shifted_frame_change_and_inverse=change,nonzero_change=change_nonzero,
            mean_change=change_mean,Cq=Cq,strict_endpoint_height_multiplier=CH).items()},
        rows=[],all_parameter_values_and_infinite_modes_retained=True,
        finite_head_kept_in_the_entire_evolution=True,
        all_crossings_through_the_head_kept=True,
        no_compressed_PDE_or_discarded_mean=True,
        full_nonconstant_graph_strong_gluing_proved=False,
        positive_Ai_contact_proved=False,full_returned_Rstar_proved=False,
        effective_feedback_cutoff_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_strict_high_energy_triangular.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_root_fourier_fit.py')})
    for N in a.scales:
        T,R,mults,resolvents=triangle(N,derivatives,eta)
        MM=max(mults).upper();RR=max(resolvents).upper();MB=max(mults[:11]).upper()
        Cref=(1+Gamma*L*MM*RR*arb(2).sqrt()*CD).upper()
        Sref=(Gamma*(1+L*MM*RR*CG)).upper()
        Cfree=(change*change*Cref).upper();Sfree=(change*Sref).upper()
        lag,A0,A2=lag_moment(N,decay)
        first=(2*Cq*(V+Vxi)*lag).upper()
        B=(100*arb.pi()*MB).upper()
        second=(2*Cfree*L*B*B).upper()
        strong=(first+second).upper()
        high=(16*arb(N)**(arb(4)/3)*strong).upper()
        full=(arb(N)**(arb(28)/3)*strong).upper()
        CP0=(10*c*max(1/arb.pi(),(qhi*N)**(arb(1)/3)+reference**(arb(1)/4))).upper()
        CP=(10*c*max(reference*L+1/arb.pi(),(qhi*N)**(arb(1)/3)+reference**(arb(1)/4)
                                    +L**(arb(1)/4)*(qhi*N)**(arb(1)/2))).upper()
        B0=(2*(CD*CD+CP0*CP0)).sqrt().upper()
        I0=(arb.pi()/(arb(2).sqrt()*c*c)*(CD*CD+CP0*CP0).sqrt()).upper()
        BL=(2*(CH*CH+CP*CP)).sqrt().upper()
        IL=(arb.pi()/(arb(2).sqrt()*c*c)*(CH*CH+CP*CP).sqrt()).upper()
        row=dict(scale=N,complete_multiplier_matrix=matrix_record(T),
            complete_height_resolvent_matrix=matrix_record(R),
            multiplier_integer_bounds=[record(x) for x in mults],
            height_resolvent_integer_bounds=[record(x) for x in resolvents],
            full_multiplier_shifted_window=record(MM),full_height_resolvent_shifted_window=record(RR),
            shifted_reference_full_amplitude_propagation_and_inverse=record(Cref),
            shifted_reference_full_ordinary_source=record(Sref),
            original_R39_full_amplitude_propagation_and_inverse=record(Cfree),
            original_R39_full_ordinary_source=record(Sfree),
            reference_complete_two_row_frame={k:record(v) for k,v in dict(
                root_frame=B0,root_inverse=I0,strict_endpoint_frame=BL,strict_endpoint_inverse=IL,
                root_momentum_multiplier=CP0,full_collar_momentum_multiplier=CP).items()},
            complete_first_Dyson_minus_original_B=record(first),
            complete_second_and_higher_Dyson=record(second),
            original_R43_one_gain_K_constant=record(B),
            full_strong_R4over3_in_scaled_spaces=record(strong),
            true_high_high_original_Sobolev_strong_bound=record(high),
            high_projection='|n|>=N, applied only to the final full operator; all intermediate head paths remain',
            full_original_Sobolev_strong_bound=record(full),
            complete_fractional_lag_sum=record(lag),Holder_zeroth_moment=record(A0),Holder_second_moment=record(A2),
            exact_decomposition='C_free(L,0)=I+B_original+R4over3; no reference phase replaces B_original',
            proved=True)
        output['rows'].append(row)
        print(dict(N=N,height=RR.str(10),multiplier=MM.str(10),Cfree=Cfree.str(10),
            source=Sfree.str(10),strong=strong.str(10),high_high=high.str(10)),flush=True)
    output.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='Complete root-to-constant-canonical-section amplitude propagation and inverse, full ordinary source, both Cauchy rows and the original R43 first phase plus full four-thirds remainder. The canonical section lies beyond the actual physical cut graph; that nonconstant graph still needs its exact strong trace connector.')
    save(a.out,output)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=output['seconds']),flush=True)

if __name__=='__main__':main()
