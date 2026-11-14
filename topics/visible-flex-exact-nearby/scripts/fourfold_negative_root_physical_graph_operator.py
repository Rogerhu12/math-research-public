#!/usr/bin/env python3
"""Actual nonconstant root cut: full Cauchy rows, source and strong R46 gluing.

The graph is the same true physical cut consumed by the full strict certificate.
All modes, the exact mean matrices and every path through the head remain.
Only canceled composites need the wider complex graph domain; the original
second-order time coefficient is required to be positive on the real domain.
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
from fourfold_strict_high_energy_triangular import (
    positive_matrix_bound, weighted_principal, stirling_rows, power_tail)


def upper(row):
    return stored(row).upper()


def lower(row):
    return stored(row).lower()


def matrix_record(A):
    return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]


def complete_moment(N, width, power, lag=0):
    """Full sum (1+|n|/N)^power |n|^lag exp(-width*|n|)."""
    q=(-width).exp(); st=stirling_rows(power+lag)
    ans=arb(int(lag==0))
    for j in range(power+1):
        ans+=2*math.comb(power,j)*power_tail(1,q,j+lag,st)/arb(N)**j
    return ans.upper()


def mult(N, power, M, width):
    p=abs(Fraction(power))
    k=(p.numerator+p.denominator-1)//p.denominator
    T=acb_mat(k+1,k+1)
    for j in range(k+1):
        for ell in range(j+1):
            T[j,ell]=math.comb(j,ell)*math.factorial(j-ell)*M/(N*width)**(j-ell)
    # This complete derivative comparison has no unnecessary 1/width fee in
    # its zeroth order. Real duality and interpolation pay noninteger orders.
    return max(positive_matrix_bound(weighted_principal(T,j))
               for j in range(k+1)).upper()


def compositions(N, CJ, width, order=11):
    """Complete scaled Bell matrices, including the inverse-Jacobian adjoint."""
    H=[arb(0)]+[(math.factorial(j-1)*CJ/(width/2)**(j-1)).upper()
                 for j in range(1,order+1)]
    bell=[[arb(0) for _ in range(order+1)] for _ in range(order+1)]
    bell[0][0]=arb(1)
    for j in range(1,order+1):
        for ell in range(1,j+1):
            bell[j][ell]=sum((math.comb(j-1,b-1)*H[b]*bell[j-b][ell-1]
                             for b in range(1,j-ell+2)),arb(0)).upper()
    matrix=acb_mat([[bell[j][ell]/arb(N)**(j-ell) if ell<=j else 0
                    for ell in range(order+1)] for j in range(order+1)])
    positive=[];negative=[]
    for k in range(order+1):
        b=(CJ.sqrt()*positive_matrix_bound(weighted_principal(matrix,k))).upper()
        positive.append(b)
        negative.append((mult(N,k,CJ,width)*b).upper())
    return dict(matrix=matrix,positive=positive,negative=negative,
                uniform=max(positive+negative).upper())


def cross_bound(N, width, real_complex_derivative_lower, M, input_order,
                gain, same_order):
    """Full opposite-sign/zero-row norm, from genuine contour displacement.

    The output order is at most 10.5 and is rounded to 11. The input absolute
    order is bounded by input_order. All geometric sums include every mode.
    """
    decay=(real_complex_derivative_lower*width/2).lower()
    output=complete_moment(N,2*decay,22)
    inp=complete_moment(N,2*decay,2*input_order)
    direct=(M*(output*inp).sqrt()).upper()
    # Keep the same-order true composition, and only pay the gained
    # derivatives from the contour estimate. J_N <= I+|D|/N and
    # J_N^2=I+D^2/N^2. No head is removed in this splitting.
    differentiated=complete_moment(N,2*decay,2*input_order,2*gain)
    split=(same_order+M*(differentiated*inp).sqrt()/arb(N)**gain).upper()
    return min(direct,split).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--domain',type=Path,default=Path('notes/2026-11-13-negative-root-full-canonical-domain.json'))
    ap.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-negative-root-complete-potential-density.json'))
    ap.add_argument('--cut',type=Path,default=Path('notes/2026-11-13-negative-canonical-full-real-cut.json'))
    ap.add_argument('--root-operator',type=Path,default=Path('notes/2026-11-13-negative-root-full-Airy-operator-additional-scale.json'))
    ap.add_argument('--field-phi-strip',type=Fraction,default=Fraction(1,400000))
    ap.add_argument('--scales',type=int,nargs='+',default=[1,4096,16384,65536,1048576])
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or any(N<1 for N in a.scales):
        raise ValueError('new output and positive norm scales required')
    ctx.prec=a.bits; tick=time.monotonic()
    dom=checked(a.domain,'fourfold_negative_root_full_canonical_domain.py')
    pot=checked(a.potential,'fourfold_negative_root_complete_potential_density.py')
    cut=checked(a.cut,'fourfold_negative_canonical_full_real_cut.py')
    root=checked(a.root_operator,'fourfold_negative_root_full_Airy_operator.py')
    if not dom['identity']==pot['identity']==cut['identity']==root['identity']:
        raise ValueError('actual root/physical-cut families differ')
    rootrows={r['scale']:r for r in root['rows']}
    if any(N not in rootrows for N in a.scales):
        raise ValueError('a norm scale lacks the full original-root strong operator')
    qlo=lower(dom['actual_quarter_circle_frequency'][0])
    qhi=upper(dom['actual_quarter_circle_frequency'][1])
    L=exact_arb(Fraction(dom['canonical_real_height']))
    sigma=exact_arb(Fraction(dom['canonical_complex_angle_strip']))
    eps=exact_arb(Fraction(dom['canonical_complex_radial_halo']))
    fieldphi=exact_arb(a.field_phi_strip)
    S1=exact_arb(Fraction(pot['physical_characteristic_start_strip']))
    e=upper(pot['complete_moduli']['Delta_minus_one'])
    U=upper(pot['complete_moduli']['U0']); Ulo=lower(pot['U0_real_lower'])
    chilo=lower(cut['actual_physical_cut_canonical_graph_range'][0])
    chihi=upper(cut['actual_physical_cut_canonical_graph_range'][1])
    rholo=lower(cut['actual_physical_cut_root_distance'][0])
    amin=(L-chihi).lower(); amax=(L-chilo).upper()
    V=upper(dom['full_canonical_V_modulus'])
    ptheta=(2*Ulo*(1-e)).lower()
    # Lift phi at the fixed true rho_cut. No radial inverse is used here.
    chi_strip=sigma
    beta=(e/(1-e)/(rholo*(1-e)**(arb(2)/3)).sqrt()).upper()
    movement=(beta*fieldphi).upper()
    xi0=(chilo-movement).lower();xiM=(L+movement).upper()
    aM=(amax+movement).upper()
    Dlo=(1-xiM*beta**2).lower();DM=(1+xiM*beta**2).upper()
    mu0=xi0.sqrt().lower();muM=xiM.sqrt().upper()
    tilt=(muM*beta).upper();Sder=(1-tilt).lower()
    fieldx=(qlo*fieldphi).lower()
    CJ=((1+tilt)/(1-tilt)).upper()
    flowstrip=(fieldx/(4*CJ**2)).lower()
    flow_positive_complex_derivative=((1-tilt)/(1+tilt)**2).lower()
    betax=(beta/(qlo*(chi_strip-fieldphi))).upper()
    ax=(beta/qlo).upper()
    Vxi=(V/(eps-movement)).upper()
    Vphi=(V/(sigma-fieldphi)).upper()
    F0=(V+arb(5)/(16*xi0**2)).upper()
    F1=(Vxi+arb(5)/(8*xi0**3)).upper()
    Fcal=(aM*F0/qlo).upper()
    Sxt=(muM*beta*(1+aM/(2*xi0))).upper()
    Sxx=(muM*(betax+ax*beta/(2*xi0))).upper()
    g0=(F0/(2*qlo*mu0*Sder)).upper()
    g0t=((aM*F1+F0*(aM/(2*xi0)+Sxt/Sder))/(2*qlo*mu0*Sder)).upper()
    g0x=((Vphi/qlo+ax*F1+F0*(ax/(2*xi0)+Sxx/Sder))/(2*qlo*mu0*Sder)).upper()
    w=(qhi*muM/Sder).upper()
    Hphase=(aM*g0).upper()
    Br_times_a=(2*xiM*beta**2/qlo+aM*xiM*betax+aM/(2*qlo*xi0)).upper()
    m=xi0**(-arb(1)/4)
    Pmh=(m*(Fcal*Hphase+DM/qlo*(g0t+aM*w*g0x+w*ax*g0)
            +2*muM*(ax*g0+aM*g0x)+Br_times_a*g0)).upper()
    initial_defect_field=(m*DM*F0/(2*qlo**2*mu0)).upper()
    remaining_momentum_field=(DM*F0/(2*qlo**2*xi0*Sder)).upper()
    complex_coeff=dict(alpha=(qhi*aM/Dlo).upper(),
        gamma=(qhi*xiM*aM/Dlo).upper(),
        v=(qhi*xiM*beta*aM/Dlo).upper(),d=(aM*V/qlo).upper())
    # Positive real energy. These bounds do not divide by complex a.
    br=(upper(cut['real_global_bounds']['graph_sqrt_xi_times_slope_modulus'])/chilo.sqrt()).upper()
    dr=(1-L*br**2).lower()
    arlo=(qlo*amin).lower(); arhi=(qhi*amax/dr).upper()
    grlo=(chilo*arlo).lower(); grhi=(L*arhi).upper()
    vr=(qhi*L*br*amax/dr).upper();dmr=(amax*V/qlo).upper()
    Dxr=(br**3/qlo+2*L*br*betax).upper()
    logat=((amax+2*L)*br**2/dr).upper()
    logax=(br/(qlo*amin)+Dxr/dr).upper()
    loggx=(logax+br/(qlo*chilo)).upper()
    vx=(qhi*((br**2*amax/qlo+L*betax*amax+L*br**2/qlo)/dr
              +L*br*amax*Dxr/dr**2)).upper()
    nux=(L.sqrt()*arhi*(logax+br/(2*qlo*chilo))).upper()
    base_diag=max(vx,logat+amax/chilo+vr*loggx+vx,logat+vr*logax+vx).upper()
    base=(base_diag+arhi.sqrt()*(1+dmr)).upper()
    stretch=(vx+nux).upper()
    # True normalized physical angle H(z)=q*phi(rho_cut,z/4).
    Hlo=(qlo/4*(2*Ulo-2*U*e)).lower()
    HM=(qhi/4*2*U*(1+e)).upper()
    Cphys=max(HM,1/Hlo).upper()
    physical_strip=(min(4*S1,Hlo*4*S1)/2).lower()
    physical_positive_complex_derivative=min(Hlo,Hlo/HM**2).lower()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the entire true physical cut is strictly below the constant section',amin>0 and amax>amin)
    gate('the fixed-rho true angle inverse exists on the whole chi strip',chi_strip/ptheta<S1/2)
    gate('the graph complex radial image stays in the paid V halo',movement<eps/2 and xi0>0)
    gate('both entire graph characteristics are uniformly spacelike',0<tilt<arb(1)/8 and Dlo>0)
    gate('all contour and flow strips have strict reserve',0<fieldphi<chi_strip and flowstrip<fieldx/4)
    gate('the exact real graph energy weights are positive',min(amin,arlo,grlo,dr)>0)
    gate('the complete physical normalized angle and inverse have positive real derivative',Hlo>0 and physical_strip>0)
    # The exact original Airy -> R46 regular-cut matrix, including the mean.
    c=upper(root['reference_bounds']['c'])
    c_exact=(1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())/
             (1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma()))).sqrt()
    c=c_exact
    gamma_hi=(arb(2)/arb.pi()).sqrt()*c/qlo.sqrt()
    gamma_lo=(arb(2)/arb.pi()).sqrt()*c/qhi.sqrt()
    Rheight=(10*c/qlo.sqrt()).upper()
    Rmomentum=(10*c*(qlo**(-arb(1)/2)*(1+1/(L*qlo**(arb(2)/3)))**(arb(1)/4)
                     +1/(4*qlo**(arb(4)/3)*L**(arb(5)/4)))).upper()
    Phi_nonzero=(2*(Rheight**2+Rmomentum**2)).sqrt().upper()
    rootmean=(1+(L/arb.pi())**2).sqrt()
    Rmean=(c*L**(arb(1)/4)*rootmean).upper()
    Tmean=(c*L**(-arb(1)/4)/qlo*(1/arb.pi()+rootmean/(4*L))).upper()
    Phi_mean=(2*(Rmean**2+Tmean**2)).sqrt().upper()
    Phi=max(Phi_nonzero,Phi_mean).upper()
    Phi_inv=(Phi/gamma_lo**2).upper()
    subphase=(arb(5)/(48*qlo*L**(arb(3)/2))).upper()
    Phi_model=max(Phi_mean,gamma_hi*(1+subphase)).upper()
    transition=int((1/(qlo*L**(arb(3)/2))).ceil().unique_fmpz())
    Astar=arb(5)/72
    high_interface=(gamma_hi*arb(9)/4*(Astar+arb(1)/2)/(qlo**2*L**3)).upper()
    gate('the whole finite Airy transition head is retained',transition>0 and qlo*transition*L**(arb(3)/2)>=1)
    bounds=dict(real_gap_lower=amin,real_gap_upper=amax,complete_chi_phi_derivative=beta,
        complete_chi_phi_strip=chi_strip,complex_graph_radial_motion=movement,
        complex_xi_modulus_lower=xi0,complex_xi_modulus_upper=xiM,complex_gap_modulus=aM,
        complete_D_lower=Dlo,complete_D_modulus=DM,complete_mu_lower=mu0,complete_mu_modulus=muM,
        complete_tilt=tilt,complete_Sx_lower=Sder,field_x_strip=fieldx,
        true_flow_strip=flowstrip,true_flow_and_inverse_derivative=CJ,
        true_flow_complex_derivative_real_lower=flow_positive_complex_derivative,
        complete_Vxi_at_graph_image=Vxi,complete_Vphi_at_graph_image=Vphi,
        F0=F0,F1=F1,Fcal=Fcal,g0=g0,g0_t=g0t,g0_x=g0x,
        complete_h=Hphase,Br_times_a=Br_times_a,complete_P_mh=Pmh,
        complete_initial_momentum_defect_field=initial_defect_field,
        complete_remaining_momentum_field=remaining_momentum_field,
        real_alpha_lower=arlo,real_alpha_upper=arhi,real_gamma_lower=grlo,real_gamma_upper=grhi,
        real_base_squared_energy_rate=base,real_first_characteristic_rate=stretch,
        physical_angle_derivative_real_lower=Hlo,physical_angle_derivative_modulus=HM,
        physical_angle_and_inverse_common_strip=physical_strip,physical_CJ=Cphys,
        full_Airy_to_strict_matrix=Phi,full_inverse_Airy_to_strict_matrix=Phi_inv,
        complete_Airy_interface_model=Phi_model,original_Airy_geometric_subphase=subphase,
        Airy_flux_normalization_lower=gamma_lo,Airy_flux_normalization_upper=gamma_hi)
    out=dict(kind='actual_full_negative_root_to_physical_cut_graph_strong_operator',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.domain,a.potential,a.cut,a.root_operator)},
        identity=dom['identity'],physical_cut=cut['physical_cut'],
        exact_constant_canonical_section=dom['canonical_real_height'],
        exact_field_phi_strip=str(a.field_phi_strip),
        full_graph_formula='xi=L-t*a(x), a=L-chi(x/q), x=q*phi, beta=q*a_x, D=1-xi*t^2*beta^2',
        full_graph_second_order_coefficients='A=D/(q*a), B=xi*t*beta, C=-q*xi*a, d=a*V/q',
        exact_graph_conormal='p_t=-(U_xi+xi*t*chi_phi*U_phi)/q',
        exact_normal_shear='T=-1/(4*q*xi)',
        exact_characteristic_labels='S_sigma=x+sigma*q*(2*L^(3/2)/3-2*xi^(3/2)/3)',
        complete_canceled_residual='g=a*g0; A*D_sigma(g)=D/q*(D_sigma(g0)+w_sigma*a_x*g0); a*Br=-2*xi*t*beta^2/q+a*xi*t*beta_x+a/(2*q*xi)',
        complex_a_nonvanishing_assumed=False,
        exact_mean_physical_normalization='nonzero modes multiply by 2; mean matrix [[5,-3],[-3,5]]/2, in the two amplitude branches',
        exact_regular_cut_mean='Phi_0=F_normal(L)^(-1)*diag(1,1/q)*c*[[1+i*L/pi,1-i*L/pi],[i/pi,-i/pi]]; it is retained exactly in the model',
        exact_regular_cut_nonzero_model='sqrt(2/pi)*c/sqrt(q)*diag_tau exp(i*tau*(q*abs(n)*2*L^(3/2)/3+pi/4))*(1-5*i*tau/(48*q*abs(n)*L^(3/2)))',
        finite_Airy_transition_head_through=transition,
        ordinary_graph_source='f_t=(a/q)*f_c(L-t*a(x),x/q); its L1(dt;H_N^(s-1/2)) norm is paid as stated, not identified with a different tilted radial norm',
        original_height_source='f_c=alpha_c^(-1/2)*(f_ground/J_Psi) composed with the true inverse; f_ground=u_z*f_original when using the original-height equation',
        physical_source_coordinate_norm_not_silently_identified=True,
        complete_bounds={k:record(v) for k,v in bounds.items()},
        complex_energy_coefficient_moduli={k:record(v) for k,v in complex_coeff.items()},
        gates=gates,rows=[],all_parameter_values_modes_means_and_head_crossings_retained=True,
        positive_Ai_contact_proved=False,full_returned_b_minus_beta_identified=False,
        full_returned_Rstar_proved=False,effective_feedback_cutoff_proved=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_strict_high_energy_triangular.py')})
    deriv={name:[(math.factorial(j)*M/fieldx**j).upper() for j in range(12)]
           for name,M in complex_coeff.items()}
    for N in a.scales:
        C=acb_mat(11,11)
        for j in range(11):
            C[j,j]=base/2+j*stretch
            for ell in range(j):
                n=j-ell;c0=math.comb(j,ell);c1=math.comb(j+1,ell)
                vals=(c0*deriv['v'][n]/grlo.sqrt(),
                      c0*deriv['alpha'][n]/arlo.sqrt(),
                      c1*deriv['v'][n+1]*(grhi/grlo).sqrt(),
                      c1*deriv['alpha'][n+1]*(grhi/arlo).sqrt(),
                      c0*deriv['d'][n]*arhi.sqrt(),
                      c1*deriv['gamma'][n+1]*(arhi/grlo).sqrt(),
                      c1*deriv['v'][n+1]*(arhi/arlo).sqrt())
                C[j,ell]=sum((z*z for z in vals),arb(0)).sqrt()/arb(N)**n
        energy_map=C.exp()
        hmin=min(arb(1),grlo*N*N,arlo).lower()
        hmax=max(arb(1),grhi*N*N,arhi).upper()
        energies=[((hmax/hmin).sqrt()*positive_matrix_bound(weighted_principal(energy_map,k))).upper()
                  for k in range(11)]
        E=max(energies).upper()
        comp=compositions(N,CJ,flowstrip)
        physical=compositions(N,Cphys,physical_strip)
        Ns=comp['uniform'];Np=physical['uniform']
        Mm=mult(N,Fraction(21,2),m,fieldx)
        Mr=mult(N,Fraction(21,2),xiM**(arb(1)/4),fieldx)
        Mt=mult(N,Fraction(21,2),1/(4*qlo*xi0),fieldx)
        uf=arb(2)**(arb(1)/4)*Mm
        frame=(uf*uf+(Mt*uf+arb(N).sqrt()*Mr)**2).sqrt().upper()
        iframe=(N*Mr*Mr+arb(2).sqrt()*Mm*Mm*(1+Mt*Mt)).sqrt().upper()
        defect=(arb(2)**(arb(3)/4)*mult(N,Fraction(19,2),initial_defect_field,fieldx)).upper()
        residual=(4*arb(2)**(arb(1)/4)*Ns*mult(N,Fraction(19,2),Pmh,flowstrip)).upper()
        Cerr=(iframe*E*(defect+residual+frame)+1).upper()
        X1=cross_bound(N,flowstrip,flow_positive_complex_derivative,arb(1),9,2,Ns)
        Xh=cross_bound(N,flowstrip,flow_positive_complex_derivative,Hphase,10,1,
                      mult(N,10,Hphase,flowstrip)*Ns)
        X=(arb(N).sqrt()*(arb(2)**(arb(1)/4)*X1+arb(2)**(arb(3)/4)*Xh)).upper()
        Lrem=(2*mult(N,Fraction(19,2),remaining_momentum_field,flowstrip)*Ns).upper()
        ordering=(2*Hphase*complete_moment(N,flowstrip,10,1)).upper()
        Qflow=(arb(2)**(arb(1)/4)*arb(N).sqrt()*Ns).upper()
        Rgraph=(Cerr+4*(2*X+Lrem+Qflow*ordering)).upper()
        Wgraph=max(arb(1),Qflow*(1+mult(N,11,Hphase,flowstrip))).upper()
        Cgraph=(iframe*E*frame).upper()
        Sgraph=(iframe*E).upper()
        Gphysical=(arb(2)**(arb(1)/4)*arb(N).sqrt()*Np).upper()
        Xphysical=cross_bound(N,physical_strip,physical_positive_complex_derivative,arb(1),9,2,Np)
        Gphysical_R2=(2*arb(2)**(arb(1)/4)*arb(N).sqrt()*Xphysical
                      +arb(2)**(arb(1)/4)*mult(N,10,Cphys,physical_strip)).upper()
        Rphi=max((Phi+Phi_model)*(1+arb(transition)**2/N**2),
                 high_interface*(1/arb(transition)**2+1/arb(N)**2)).upper()
        rr=rootrows[N]
        Cr=upper(rr['original_R39_full_amplitude_propagation_and_inverse'])
        Sr=upper(rr['original_R39_full_ordinary_source'])
        Rr=upper(rr['full_strong_R4over3_in_scaled_spaces'])
        root_to_cut=(4*Gphysical*Cgraph*Phi*Cr).upper()
        cut_to_root=(Cr*Phi_inv*Cgraph*Gphysical).upper()
        Rfull=(4*(Gphysical*Rgraph*Phi*Cr
                   +Gphysical*Wgraph*Rphi*Cr
                   +Gphysical_R2*Wgraph*Phi_model*Cr
                   +Gphysical*Wgraph*Phi_model*Rr)).upper()
        source_root=(4*Gphysical*Cgraph*Phi*Sr).upper()
        source_graph=(4*Gphysical*Sgraph).upper()
        row=dict(scale=N,energy_comparison_matrix=matrix_record(C),
            energy_propagation_matrix=matrix_record(energy_map),
            energy_norm_equivalence=[record(hmin),record(hmax)],
            half_integer_graph_Cauchy_bounds={str(Fraction(2*k+1,2)):record(v) for k,v in enumerate(energies)},
            graph_base_order_exponential=record((base/2).exp().upper()),
            graph_tenth_derivative_diagonal_exponential=record((base/2+10*stretch).exp().upper()),
            graph_Cauchy_window=[str(Fraction(-21,2)),str(Fraction(21,2))],
            flow_composition_integer_positive=[record(v) for v in comp['positive']],
            flow_composition_integer_negative=[record(v) for v in comp['negative']],
            physical_composition_integer_positive=[record(v) for v in physical['positive']],
            physical_composition_integer_negative=[record(v) for v in physical['negative']],
            flow_composition_comparison_matrix=matrix_record(comp['matrix']),
            physical_composition_comparison_matrix=matrix_record(physical['matrix']),
            complete_graph_normal_frame=record(frame),complete_inverse_graph_normal_frame=record(iframe),
            full_graph_Cauchy=record(E),full_graph_amplitude_and_inverse=record(Cgraph),
            full_graph_ordinary_source=record(Sgraph),full_graph_W0=record(Wgraph),
            full_graph_R2=record(Rgraph),full_graph_initial_momentum_defect=record(defect),
            full_graph_residual_source=record(residual),full_graph_cross_and_mean=record(X),
            complete_physical_GH_and_inverse=record(Gphysical),
            physical_GH_minus_diagonal_QH_R2=record(Gphysical_R2),
            entire_Airy_interface_R2=record(Rphi),
            full_root_to_actual_physical_cut=record(root_to_cut),
            full_actual_physical_cut_to_root=record(cut_to_root),
            full_root_to_physical_cut_R4over3=record(Rfull),
            root_source_leg_gain=record(source_root),graph_source_leg_gain=record(source_graph),
            exact_strong_model='D4*diag(Q_H,Q_H)*W0_graph*branch_swap*Phi_model*(I+B_original)',
            full_source_formula='D4*G_H*(C_graph*branch_swap*Phi*source_root + source_graph)',
            ordinary_source_norms=['L1(dxi; H_N^(s-1/3)) for the complete canonical root source',
                                  'L1(dt; H_N^(s-1/2)) for the exact pulled graph source a*f_c/q'],
            strong_window=[-8,8],proved=True)
        out['rows'].append(row)
        print(dict(N=N,Cauchy=E.str(9),graph_R2=Rgraph.str(9),
            root_to_cut=root_to_cut.str(9),full_R4over3=Rfull.str(9)),flush=True)
    out.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='The actual whole negative root-to-physical-cut full two-row operator and strong four-thirds model, with complete graph/mean/angle/Airy interface factors and two exact ordinary-source norms. Positive Ai/contact, full returned phase and feedback inverse remain separate.')
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=out['seconds']),flush=True)


if __name__=='__main__':
    main()
