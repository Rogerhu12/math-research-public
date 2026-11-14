#!/usr/bin/env python3
"""Exact density characteristics and lower-order bootstrap of all strict cells.

The unchanged physical equation becomes two exact density transports with
only kappa*w coupling. The angular mean of w and the base density norm are
paid by the original zeroth-order physical energy. Higher angular orders
use the actual all-time maps, not repeated characteristic-supremum growth.
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


def up(x):return stored(x).upper()
def lo(x):return stored(x).lower()
def matrix_record(A):
    return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]


def density_transport(N,real_J,complex_J,width,order=10):
    # Only derivatives of order >=2 use the complex Cauchy reserve.
    jets=[arb(0),real_J]+[(math.factorial(j-1)*complex_J/(width/2)**(j-1)).upper()
                                for j in range(2,order+2)]
    bell=[[arb(0) for _ in range(order+2)] for _ in range(order+2)]
    bell[0][0]=arb(1)
    for j in range(1,order+2):
        for ell in range(1,j+1):
            bell[j][ell]=sum((math.comb(j-1,b-1)*jets[b]*bell[j-b][ell-1]
                for b in range(1,j-ell+2)),arb(0)).upper()
    # d^j[S' f(S)]=S' sum_l (Bell[j+1,l+1]/S') f^(l)(S).
    # The leading coefficient is exactly (S')^j. The actual density
    # change of variables has L2 norm <=sqrt(real_J), including its mean.
    D=acb_mat(order+1,order+1)
    for j in range(order+1):
        for ell in range(j+1):
            D[j,ell]=(real_J**j if ell==j else
                real_J*bell[j+1][ell+1]/arb(N)**(j-ell))
    norms=[(real_J.sqrt()*positive_matrix_bound(weighted_principal(D,k))).upper()
           for k in range(order+1)]
    return D,norms


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scaled',type=Path,default=Path(
        'notes/2026-11-13-R46-215-cell-scaled-strong-operator.json'))
    ap.add_argument('--fields',type=Path,default=Path(
        'notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    ap.add_argument('--real-ray',type=Path,default=Path(
        'notes/2026-11-13-R106-complete-relative-real-Jacobian.json.gz'))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('new complete output required')
    ctx.prec=a.bits;tick=time.monotonic()
    old=checked(a.scaled,'fourfold_strict_scaled_complete_R46_budget.py')
    fields=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    ray=checked(a.real_ray,'fourfold_true_relative_ray_jacobian_cells.py')
    if (old['kind']!='actual_complete_215_cell_strict_scaled_strong_operator'
        or ray['kind']!='actual_complete_same_label_real_relative_ray_Jacobian'
        or fields['identity']!=old['identity'] or ray['identity']!=old['identity']
        or old['inputs'].get(str(a.fields))!=sha(a.fields)
        or ray['inputs'].get(str(a.scaled))!=sha(a.scaled)):
        raise ValueError('same complete old physical operator and parameter family required')
    if not (old['full_mean_full_sources_and_all_intermediate_head_paths_retained']
        and ray['all_550_true_segments_and_all_relative_times']
        and ray['real_and_complex_bounds_deliberately_distinct']):
        raise ValueError('whole true source/flow scope missing')
    C=up(ray['full_real_relative_map_and_inverse_derivative'])
    CJ=up(old['true_relative_flow_derivative_and_inverse']);X=lo(old['normalized_flow_strip'])
    fieldwidth=lo(old['normalized_field_strip'])
    if not 1<C<CJ:raise ValueError('genuine improved real derivative gate failed')
    raw_kappa=arb(0);base_log=arb(0);cursor=Fraction(0)
    wm=arb(0);ym=arb(0);mmax=arb(0);rootmumax=arb(0);Tmax=arb(0);alphamax=arb(0)
    # wm and ym map the unchanged constraint energy e0 to |mean w| and
    # ||(y+,y-)||_L2. Compute them on each original cell before taking max.
    for cell in fields['cells']:
        left,right=Fraction(cell['left']),Fraction(cell['right'])
        if left!=cursor or not left<right:raise ValueError('original closed-cell gap')
        cursor=right;length=exact_arb(right-left)
        M={k:up(v) for k,v in cell['complete_complex_field_moduli'].items()}
        mulow=lo(cell['geometry']['mu_modulus_lower'])
        m=up(cell['geometry']['m_modulus_upper']);rootmu=M['mu'].sqrt().upper()
        raw_kappa+=2*length*M['Fcal']/mulow
        ranges=cell['energy']['positive_ranges']
        lam=lo(ranges['lambda'][0]);alpha=lo(ranges['alpha'][0]);gamma=lo(ranges['gamma'][0])
        if not min(lam,alpha,gamma,mulow)>0:raise ValueError('true base weights not positive')
        wc=(rootmu/lam.sqrt()).upper()
        zc=(rootmu*(1/gamma.sqrt()+M['Ltheta']/(2*lam.sqrt()))).upper()
        pc=(m*(1/alpha.sqrt()+M['T']/lam.sqrt())).upper()
        yc=((zc*zc+pc*pc)/2).sqrt().upper()
        wm=max(wm,wc);ym=max(ym,yc)
        mmax=max(mmax,m);rootmumax=max(rootmumax,rootmu);Tmax=max(Tmax,M['T'])
        alphamax=max(alphamax,up(ranges['alpha'][1]))
        for side in ('forward','backward'):
            base_log+=length*max(arb(0),up(cell['energy']['base_energy_rate_'+side])/2)
    if len(fields['cells'])!=215 or str(cursor)!=old['exact_physical_interval'][1]:
        raise ValueError('the entire actual strict interval is not covered')
    Ebase=base_log.exp().upper();raw_kappa=raw_kappa.upper()
    out=dict(kind='actual_complete_strict_density_transport_lower_order_bootstrap',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.scaled,a.fields,a.real_ray)},identity=old['identity'],
        exact_physical_interval=old['exact_physical_interval'],native_cells_recomputed=0,
        exact_variables=['w=sqrt(mu)*u','zeta=(p+T*u)/sqrt(mu)',
            'y_sigma=(w_theta+sigma*zeta)/2'],
        exact_equations=['(y_sigma)_r+partial_theta((v-sigma*nu)*y_sigma)=-sigma*kappa*w/2+sigma*f/(2*sqrt(mu))',
            'kappa=Fcal/mu','w_theta=y_plus+y_minus',
            'w_r=nu*(y_plus-y_minus)-v*(y_plus+y_minus)'],
        unchanged_physical_momentum=True,no_mixed_radial_angular_differentiation=True,
        complete_mean_w_paid_by_original_base_energy=True,complete_mean_zeta_retained=True,
        full_550_actual_relative_density_flows=True,
        true_real_map_derivative=record(C),true_complex_map_derivative=record(CJ),
        complex_flow_strip=record(X),field_strip=record(fieldwidth),
        complete_integrated_kappa_modulus=record(raw_kappa),
        full_base_energy_log=record(base_log.upper()),full_base_energy_gain=record(Ebase),
        base_mean_w_conversion=record(wm),base_density_conversion=record(ym),
        rows=[],full_return_inverse_proved=False,effective_feedback_cutoff_proved=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_negative_root_physical_graph_operator.py',
            'fourfold_strict_high_energy_triangular.py',
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')})
    for previous in old['rows']:
        N=previous['scale'];scale=arb(4*N)
        D,Dnorm=density_transport(N,C,CJ,X)
        cN=((1+arb(N)**-2).sqrt()/4).upper()
        hplus=up(previous['energy_weights'][1]);init=Ebase*hplus.sqrt();forced=Ebase*alphamax.sqrt()
        meanC=(wm*init).upper();meanS=(wm*forced).upper()
        Cy=[(ym*init).upper()];Sy=[(ym*forced).upper()]
        polyC=[[Cy[0]]];polyS=[[Sy[0]]]
        oldE=[up(previous['half_integer_full_Cauchy'][str(Fraction(2*k+1,2))]) for k in range(11)]
        fullC=[oldE[0]];fullS=[oldE[0]];details=[]
        Kunit=[mult(N,k,arb(1),fieldwidth) for k in range(11)]
        K=[(raw_kappa*x).upper() for x in Kunit]
        for k in range(11):
            Mm=mult(N,k,mmax,fieldwidth);Mr=mult(N,k,rootmumax,fieldwidth)
            Mt=mult(N,k,Tmax,fieldwidth)
            Mmnext=mult(N,k+1,mmax,fieldwidth)
            Mrnext=mult(N,k+1,rootmumax,fieldwidth)
            # Full physical initial state P_(k+1/2), no projection.
            FY=((scale*Mrnext+Mm*(1+Mt*Mt).sqrt())/arb(2).sqrt()).upper()
            if k:
                # Preserve chronological integration. If q(r) is the full
                # scalar |kappa| majorant and Q(t)=integral q, the previous
                # polynomial p(Q(t)) integrates exactly as integral_0^Q p.
                # This retains every 1/(j+1), instead of replacing the
                # previous order by its final-time supremum at every step.
                pc=[(Dnorm[k]*FY).upper(),
                    (Dnorm[k]*Kunit[k]*meanC/arb(2).sqrt()).upper()]
                ps=[(Dnorm[k]*Mm/arb(2).sqrt()).upper(),
                    (Dnorm[k]*Kunit[k]*meanS/arb(2).sqrt()).upper()]
                coupling=(Dnorm[k]*Kunit[k]*cN).upper()
                for j,value in enumerate(polyC[k-1]):
                    while len(pc)<=j+1:pc.append(arb(0))
                    pc[j+1]+=(coupling*value/(j+1)).upper()
                for j,value in enumerate(polyS[k-1]):
                    while len(ps)<=j+1:ps.append(arb(0))
                    ps[j+1]+=(coupling*value/(j+1)).upper()
                pc=[x.upper() for x in pc];ps=[x.upper() for x in ps]
                polyC.append(pc);polyS.append(ps)
                yc=sum((value*raw_kappa**j for j,value in enumerate(pc)),arb(0)).upper()
                ys=sum((value*raw_kappa**j for j,value in enumerate(ps)),arb(0)).upper()
                Cy.append(min(yc,(FY*oldE[k]).upper()).upper())
                Sy.append(min(ys,(FY*oldE[k]).upper()).upper())
            # For k=0, the full base density vector already includes both
            # mean fluxes; for k>=1 the source loses one angular order only.
            lowerC=Cy[max(0,k-1)];lowerS=Sy[max(0,k-1)]
            uc=(Mmnext*(meanC+arb(2).sqrt()*cN*Cy[k])).upper()
            pc=(arb(2).sqrt()*Mr*Cy[k]+Mt*Mm*(meanC+arb(2).sqrt()*cN*lowerC)).upper()
            us=(Mmnext*(meanS+arb(2).sqrt()*cN*Sy[k])).upper()
            ps=(arb(2).sqrt()*Mr*Sy[k]+Mt*Mm*(meanS+arb(2).sqrt()*cN*lowerS)).upper()
            candidateC=(uc*uc+pc*pc).sqrt().upper();candidateS=(us*us+ps*ps).sqrt().upper()
            if k:
                fullC.append(min(oldE[k],candidateC).upper())
                fullS.append(min(oldE[k],candidateS).upper())
            details.append(dict(half_integer=str(Fraction(2*k+1,2)),
                actual_density_transport=record(Dnorm[k]),integrated_kappa_multiplier=record(K[k]),
                complete_initial_density_frame=record(FY),full_density_homogeneous=record(Cy[k]),
                full_density_source=record(Sy[k]),physical_Cauchy_candidate=record(candidateC),
                ordered_kappa_homogeneous_polynomial=[record(x) for x in polyC[k]],
                ordered_kappa_source_polynomial=[record(x) for x in polyS[k]],
                physical_source_candidate=record(candidateS),full_physical_Cauchy=record(fullC[k]),
                positive_ordinary_physical_source=record(fullS[k]),original_Cauchy=record(oldE[k])))
        E=max(fullC).upper();F=up(previous['full_normal_frame']);I=up(previous['full_inverse_normal_frame'])
        defect=up(previous['full_initial_momentum_defect']);residual=up(previous['full_ordinary_residual_budget'])
        Cerr=(I*E*(defect+residual+F)+1).upper()
        Nc=max(up(v) for v in previous['composition_integer_positive']+previous['composition_integer_negative'])
        Q=(arb(2)**(arb(1)/4)*scale.sqrt()*Nc).upper()
        rest=4*(2*up(previous['full_cross_and_mean_output'])
            +up(previous['full_remaining_momentum_term'])+Q*up(previous['full_ordering_fee']))
        R2=(Cerr+rest).upper()
        out['rows'].append(dict(scale=N,physical_derivative_scale=4*N,
            density_transport_complete_comparison_matrix=matrix_record(D),
            angular_antiderivative_full_nonmean_gain=record(cN),
            complete_mean_homogeneous=record(meanC),complete_mean_source=record(meanS),
            derivative_rows=details,full_Cauchy_window=['-21/2','21/2'],full_Cauchy=record(E),
            full_amplitude_and_inverse=record((I*E*F).upper()),
            full_ordinary_physical_source=record((I*E).upper()),
            full_source_and_mean_correction=record(Cerr),unchanged_remaining_strong_terms=record(rest.upper()),
            full_strong_R2=record(R2),full_W0_bound=previous['full_W0_bound'],
            all_original_four_branches_and_all_head_paths_retained=True,
            only_Cauchy_bound_replaced_in_original_R46_consumer=True))
        print(dict(N=N,real_J=C.str(8),Cauchy=E.str(10),R2=R2.str(10)),flush=True)
    out.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='The same full actual strict Cauchy map, inverse, ordinary physical source and strong R46 remainder, using exact true density characteristics and one-angular-order triangular bootstrap; every mean and intermediate head crossing is retained.')
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=out['seconds']),flush=True)


if __name__=='__main__':main()
