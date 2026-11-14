#!/usr/bin/env python3
"""Full old-object return word, symmetric density calculus and both scalar cones.

No native geometry is recomputed.  An exact finite H derivative cover is
evaluated, and the full, previously certified word is normalized on both
Fourier cones.  The output is a base unweighted strong normal form, not an
inverse or a useful finite-head cutoff.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read, save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_negative_root_physical_graph_operator import (
    mult, complete_moment, compositions)
from fourfold_strict_high_energy_triangular import (
    positive_matrix_bound, weighted_principal)
from fourfold_strict_windowed_density_R46 import real_refined_compositions


def up(row): return stored(row).upper()
def lo(row): return stored(row).lower()


def bell(derivatives, n):
    B = [[arb(0) for _ in range(n+1)] for _ in range(n+1)]
    B[0][0] = arb(1)
    for j in range(1, n+1):
        for k in range(1, j+1):
            B[j][k] = sum((math.comb(j-1, v-1)*derivatives[v]*B[j-v][k-1]
                          for v in range(1, j-k+2)), arb(0)).upper()
    return B


def real_jet_Q_bound(N, minimum, modulus, width):
    """Full Q_H, Q_H^-1 and adjoints for |s|<=2, using real inverse jets."""
    order = 3
    f = [arb(0)] + [(math.factorial(j-1)*modulus/(width/2)**(j-1)).upper()
                    for j in range(1, order+2)]
    inv = [arb(0), (1/minimum).upper()] + [arb(0)]*order
    for j in range(2, order+2):
        B = bell(inv, j)
        inv[j] = (sum((f[k]*B[j][k] for k in range(2, j+1)), arb(0))/minimum).upper()
    Bf, Bi = bell(f, order), bell(inv, order)
    def matrix(B):
        return acb_mat([[B[j][k]/arb(N)**(j-k) if k<=j else 0
                         for k in range(order+1)] for j in range(order+1)])
    Af, Ai = matrix(Bf), matrix(Bi)
    def leibniz(ds):
        return acb_mat([[math.comb(j,k)*ds[j-k+1]/arb(N)**(j-k) if k<=j else 0
                         for k in range(order+1)] for j in range(order+1)])
    Tf, Ti = leibniz(f), leibniz(inv)
    vals = []
    rows = []
    for k in range(order+1):
        p = ((1/minimum).sqrt()*positive_matrix_bound(weighted_principal(Af,k))).upper()
        pi = (modulus.sqrt()*positive_matrix_bound(weighted_principal(Ai,k))).upper()
        j = positive_matrix_bound(weighted_principal(Tf,k)).upper()
        ji = positive_matrix_bound(weighted_principal(Ti,k)).upper()
        neg, negi = (ji*pi).upper(), (j*p).upper()
        vals.extend((p, pi, neg, negi))
        rows.append(dict(integer=k,forward_positive=record(p),inverse_positive=record(pi),
                         forward_negative=record(neg),inverse_negative=record(negi)))
    C = max(vals).upper()
    return (arb(2)**(arb(1)/4)*arb(N).sqrt()*C).upper(), dict(
        full_real_derivative_jets=[record(x) for x in f[1:]],
        full_inverse_real_derivative_jets=[record(x) for x in inv[1:]],
        integer_compositions=rows,complete_composition_bound=record(C))


def Q_cross_and_adjoint(N, width, derivative_real_lower, derivative_modulus):
    """Both 0->2 and -2->0; all opposite cones and mean rows/columns."""
    decay = (width*min(arb(1), derivative_real_lower)/2).lower()
    z = complete_moment(N,2*decay,4)
    z1 = complete_moment(N,2*decay,4,1)
    result = (8*(1+derivative_modulus)*((z+z1)*z).sqrt()).upper()
    return result, decay


def phase_bounds(N, modulus, width, constant=False):
    zero = modulus if constant else mult(N,2,modulus,width)
    one = arb(2).sqrt()*(modulus if constant else mult(N,Fraction(3,2),modulus,width))
    if constant:
        ordering = cross = arb(0)
    else:
        z0 = complete_moment(N,width,0)
        z1 = complete_moment(N,width,0,1)
        z2 = complete_moment(N,width,0,2)
        ordering = modulus*(z1+(z1+z2)/arb(N)**2)
        cross = modulus*(z0+z2/arb(N)**2)
    return {k:v.upper() for k,v in dict(
        same_order=zero,gain_one=one,ordering_gain_two=ordering,
        cross_and_mean_gain_two=cross).items()}


def finite_H_cover(path, cells, strip):
    d = read(path)
    if d['kind']!='exact_dyadic_trigonometric_polynomials_H_and_q':
        raise ValueError('the original exact finite H is required')
    den = 2**int(d['denominator_power_of_two'])
    h = [acb(exact_arb(Fraction(int(z[0]),den)),
             exact_arb(Fraction(int(z[1]),den)))
         for z in d['h_nonnegative_integer_coefficients']]
    if len(h)!=int(d['H_degree'])+1:
        raise ValueError('the complete finite H degree changed')
    c = [acb(0)] + [acb(0,j)*h[j] for j in range(1,len(h))]
    M1 = (1+sum((2*j*abs(h[j])*((j*strip).exp())
                 for j in range(1,len(h))),arb(0))).upper()
    M2 = sum((2*j*j*abs(h[j]) for j in range(1,len(h))),arb(0)).upper()
    minimum = None
    maximum = arb(0)
    for k in range(cells):
        z = acb(0,2*arb.pi()*k/cells).exp()
        value = acb(0)
        for j in range(len(c)-1,0,-1):
            value = (value+c[j])*z
        hp = 1+2*value.real
        minimum = hp.lower() if minimum is None else min(minimum,hp.lower())
        maximum = max(maximum,hp.upper())
    movement = (arb.pi()*M2/cells).upper()
    lower = (minimum-movement).lower()
    if not lower>0:
        raise ValueError('finite real H derivative cover did not certify positivity')
    return lower, M1, dict(
        exact_path=str(path),exact_sha256=sha(path),closed_angular_cells=cells,
        complete_finite_degree=len(h)-1,all_dyadic_coefficients_retained=True,
        derivative_center_lower=record(minimum),derivative_center_upper=record(maximum),
        full_real_second_derivative_modulus=record(M2),
        full_cell_derivative_movement=record(movement),whole_real_derivative_lower=record(lower),
        analytic_derivative_strip=str(Fraction(1,2048)),
        full_analytic_derivative_modulus=record(M1))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--word',type=Path,default=Path('notes/2026-11-13-actual-central-strong-word.json'))
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--phase',type=Path,default=Path('notes/2026-11-13-R106-geometric-two-leg-final-circle-phase.json'))
    p.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-negative-root-complete-potential-density.json'))
    p.add_argument('--domain',type=Path,default=Path('notes/2026-11-13-negative-root-full-canonical-domain.json'))
    p.add_argument('--cells',type=int,default=2048)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.cells<1024:
        raise ValueError('a fresh output and a complete finite angular cover are required')
    ctx.prec=a.bits;tick=time.monotonic()
    w=checked(a.word,'fourfold_actual_central_strong_word.py')
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    st=checked(a.strict,'fourfold_strict_windowed_density_R46.py')
    phase=checked(a.phase,'fourfold_subprincipal_geometric_return_budget.py')
    pot=checked(a.potential,'fourfold_negative_root_complete_potential_density.py')
    dom=checked(a.domain,'fourfold_negative_root_full_canonical_domain.py')
    SC=Path('notes/2026-11-13-actual-central-scattering-and-source.json')
    SS=Path('notes/2026-11-13-actual-central-scattering-reflected-source.json')
    scbase=checked(SC,'fourfold_actual_central_scattering_and_source.py')
    ssbase=checked(SS,'fourfold_actual_central_scattering_reflected_source.py')
    if not w['identity']==st['identity'] or not g['identity']==pot['identity']==dom['identity']:
        raise ValueError('whole old-object parameter identities differ')
    for path in (a.graph,a.strict):
        if w['inputs'].get(str(path))!=sha(path):
            raise ValueError('the complete strong word used different geometry')
    if (not w['identity']==scbase['identity']==ssbase['identity']
        or w['inputs'].get(str(SC))!=sha(SC) or w['inputs'].get(str(SS))!=sha(SS)):
        raise ValueError('the full original source realization changed')
    for path in (a.potential,a.domain):
        if g['inputs'].get(str(path))!=sha(path):
            raise ValueError('the graph/root fields differ')
    if not phase['complete'] or not phase['proved']:
        raise ValueError('the entire actual geometric phase is required')
    for path,digest in phase['inputs'].items():
        if sha(path)!=digest: raise ValueError('actual final-circle identity changed: '+path)
    if sha(phase['forward_path'])!=phase['forward_sha256']:
        raise ValueError('the complete forward one-form changed')
    KAM=Path('notes/2026-11-12-split-Wiener-R31-exact.json')
    PRE=Path('data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json')
    DESC=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json')
    kam,pre,desc=map(read,(KAM,PRE,DESC))
    Hpath=Path(desc['target_H']['path'])
    if sha(Hpath)!=phase['initial_H_sha256'] or sha(Hpath)!=desc['target_H']['sha256']:
        raise ValueError('the same exact finite initial label is required')
    rr=lambda name: exact_arb(Fraction(kam['R31'][name]['exact_fraction']))
    phip=rr('conjugacy_derivative_movement');wp=up(pre['w_derivative_norms'][0])
    psi_lo=((1-phip)*(1-wp)).lower();psi_hi=((1+phip)*(1+wp)).upper()
    if not psi_lo>0: raise ValueError('final relative label lost its real derivative')
    N=int(w['scale']);gain=Fraction(4,3)
    gb=g['complete_bounds'];gr=next(z for z in g['rows'] if z['scale']==N)
    sr=next(z for z in st['rows'] if z['scale']==N)
    Hlo,HM,Hcover=finite_H_cover(Hpath,a.cells,exact_arb(Fraction(1,2048)))
    qlo=lo(dom['actual_quarter_circle_frequency'][0])
    qhi=up(dom['actual_quarter_circle_frequency'][1])
    Ulo=lo(pot['U0_real_lower']);UM=up(pot['complete_moduli']['U0'])
    Cstrip=exact_arb(Fraction(1,4096))
    fieldstrip=exact_arb(Fraction(pot['physical_characteristic_start_strip']))
    if not psi_hi*Cstrip<exact_arb(Fraction(1,2048)) or not HM*psi_hi*Cstrip/4<fieldstrip:
        raise ValueError('actual root-circle composition leaves the paid analytic strip')
    Cmin=(qlo*Ulo*Hlo*psi_lo/2).lower()
    CM=(qhi*UM*HM*psi_hi/2).upper()
    qC, Cjets=real_jet_Q_bound(N,Cmin,CM,Cstrip)
    # Exact circle H^(1/2) double-integral comparison, including the mean.
    # This is a true base bound, independent of the chosen scaled N.
    qC0=(max(CM,1/Cmin)+(arb.pi()*CM/(2*Cmin))**2).sqrt().upper()
    Cpositive=(min(Cstrip/4,Cmin*Cstrip/(8*CM))).lower()
    eC,Cdecay=Q_cross_and_adjoint(N,Cpositive,Cmin/2,CM)
    # These are full map and inverse bounds; no real-only derivative replaces
    # a complex derivative or enlarges a saved strip.
    phwidth=lo(gb['physical_angle_and_inverse_common_strip'])
    phCJ=up(gb['physical_CJ'])
    phM=up(gb['physical_angle_derivative_modulus'])
    phlo=lo(gb['physical_angle_derivative_real_lower'])
    phpositive=min(phlo,phlo/phM**2).lower()
    phcomp=compositions(N,phCJ,phwidth,order=3)
    qH=(arb(2)**(arb(1)/4)*arb(N).sqrt()*phcomp['uniform']).upper()
    eH,Hdecay=Q_cross_and_adjoint(N,phwidth,phpositive,phCJ)
    gw=lo(gb['true_flow_strip']);gCJ=up(gb['true_flow_and_inverse_derivative'])
    gpos=lo(gb['true_flow_complex_derivative_real_lower'])
    gc=compositions(N,gCJ,gw,order=3)
    qg=(arb(2)**(arb(1)/4)*arb(N).sqrt()*gc['uniform']).upper()
    eg,gdecay=Q_cross_and_adjoint(N,gw,gpos,gCJ)
    sw=lo(st['unchanged_normalized_complex_flow_strip'])
    Cr=up(st['real_relative_derivative']);Cc=up(st['unchanged_complex_relative_derivative'])
    sc=real_refined_compositions(N,Cr,Cc,sw,3)
    qs=(arb(2)**(arb(1)/4)*arb(N).sqrt()*sc['uniform']).upper()
    es,sdecay=Q_cross_and_adjoint(N,lo(st['complete_positive_real_cross_strip']),
                                 lo(st['complete_cross_complex_derivative_real_lower']),Cc)
    phases={}
    phases['root']=phase_bounds(N,up(w['norms']['root_first_symmetric_phase_modulus']),
        qlo*exact_arb(Fraction(dom['canonical_complex_angle_strip'])))
    phases['Airy']=phase_bounds(N,up(gb['original_Airy_geometric_subphase']),arb(1),True)
    phases['graph']=phase_bounds(N,up(gb['complete_h']),gw)
    phases['strict']=phase_bounds(N,up(st['actual_full_phase_modulus'])/4,sw)
    phase_counts={'root':4,'Airy':4,'graph':4,'strict':2}
    Qs={'physical_cut':dict(count=4,norm=qH,error=eH,decay=Hdecay),
        'graph':dict(count=4,norm=qg,error=eg,decay=gdecay),
        'strict':dict(count=2,norm=qs,error=es,decay=sdecay),
        'Airy_translation':dict(count=4,norm=arb(1),error=arb(0),decay=arb(0)),
        'actual_final_circle':dict(count=2,norm=qC,error=eC,decay=Cdecay)}
    Pq=Pphase=arb(1)
    sumE=sumA=sumA1=sumO=sumX=arb(0)
    for item in Qs.values():
        Pq*=max(arb(1),item['norm'])**item['count']
        sumE+=item['count']*item['error']
    for name,pb in phases.items():
        count=phase_counts[name]
        Pphase*=(1+pb['same_order'])**count
        sumA+=count*pb['same_order'];sumA1+=count*pb['gain_one']
        sumX+=count*pb['cross_and_mean_gain_two']
        if name in ('graph','strict'):
            sumO+=count*pb['ordering_gain_two']
    Ptot=(Pq*Pphase).upper()
    elementary=(8*Ptot*(sumE+sumO+sumX)).upper()
    quadratic=(Ptot*sumA1**2).upper()
    covariance=(Ptot*sumA*sumE).upper()
    bM=up(phase['two_leg_geometric_phase_modulus'])
    bs=exact_arb(Fraction(phase['sup_strip']))
    bp=phase_bounds(N,bM,bs)
    calculus=(elementary+quadratic+covariance+bp['ordering_gain_two']).upper()
    # Use the true scattering transmissions in the triangular operations.
    # They and their inverses have base norm at most 2.  Each difference
    # from its old model has both strong bounds at most RS.
    Tg=up(w['norms']['full_negative_transfer_word_HN_plus_minus_four_thirds'])
    RS=up(w['norms']['complete_scattering_word_error_both_base_windows'])
    cap_path=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json')
    cap=checked(cap_path,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    if w['inputs'].get(str(cap_path))!=sha(cap_path):
        raise ValueError('the original complete cap realization changed')
    capR=up(cap['complete_original_frame']['right_and_left_full_four_thirds_remainder'])
    Ea_p=(capR+RS).upper()
    Ea_m=(max(arb(1),Tg)*capR+3*RS).upper()
    return_change=((1+Tg)*RS).upper()
    newword_p=(2*(1+Tg)*Ea_p+6*RS+return_change).upper()
    newword_m=(2*(1+Tg)*Ea_m+6*RS+return_change).upper()
    Rp=(qC*qC0*newword_p+calculus).upper()
    Rm=(qC*qC0*newword_m+calculus).upper()
    R=max(Rp,Rm).upper()
    unscaled=(arb(N)**exact_arb(gain)*R).upper()
    sb=ssbase['bounds'];cb=scbase['bounds']
    base_cols=dict(strict_core=up(sb['strict_core_source']),
        either_canonical_root=up(sb['either_canonical_root_source']),
        either_tilted_graph=up(sb['either_tilted_graph_source']),
        negative_five_space_direct_sum=up(sb['five_space_direct_sum_source']),
        paired_positive_local_ordinary=up(cb['complete_positive_local_ordinary_source']),
        paired_positive_local_weak=up(cb['complete_positive_local_weak_source']),
        two_independent_physical_regular_fluxes=up(cb['actual_independent_regular_flux_to_wave_difference']))
    source={k:record((2*qC0*v).upper()) for k,v in base_cols.items()}
    reconstruction=(2*qC0).upper()
    out=dict(kind='actual_old_object_two_cone_symmetric_density_scalar_normal_form',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),
        identity=w['identity'],scale=N,actual_parameter_scope=phase['actual_parameter_scope'],
        inputs={str(z):sha(z) for z in (a.word,a.graph,a.strict,a.phase,a.potential,a.domain,SC,SS,cap_path)},
        extra_exact_inputs={str(z):sha(z) for z in (KAM,PRE,DESC,Hpath)},
        native_geometric_cells_recomputed=0,exact_finite_H_cover=Hcover,
        final_root_label='C(x)=q*Y0(chi(x)/4), chi=H o J o Phi, Y0_prime=2 U0',
        final_root_label_bounds=dict(real_derivative_lower=record(Cmin),
            complex_derivative_modulus=record(CM),original_complex_strip='1/4096',
            complete_Q_and_inverse_plus_minus_two=record(qC),
            exact_unscaled_base_Q_and_inverse=record(qC0),
            smaller_positive_real_derivative_strip=record(Cpositive),
            complex_derivative_real_lower_on_smaller_strip=record(Cmin/2),
            real_inverse_jet_calculation=Cjets),
        exact_symmetric_density_covariance=[
            'A(f)=Lambda^(-1/2) M_f Lambda^(-1/2), including the actual mean Lambda_0=1',
            'Q_H^* A(f) Q_H=A((f/H_prime) o H_inverse)',
            'Q_H^(-*) A(f) Q_H^(-1)=A((f o H)*H_prime)',
            'Q_H A(f)-A((f o H)*H_prime) Q_H=(Q_H-Q_H^(-*)) A(f)'],
        exact_anti_linear_word_relation='complex_conjugation*(U V)*complex_conjugation=(U V)^*, so the retained root+ negative cone is not merely declared the conjugate positive cone',
        exact_true_transmission_preconditioners='Ue=S12, Ve=S21; Le=[[I,-Ue],[0,I]], Re=[[I,0],[-Ve,I]], extended by I on regular slots. Their base norms and inverse norms are at most 2.',
        exact_true_reduced_word='Le*A*Re=diag(I-Ue*Ve,I,2I_regular)+Le*Ea*Re; Ea=-(Rcap^*+I)*S_ext+diag(S11,S22,0_regular)',
        exact_model_replacement='Replace Ue*Ve by U*V using (Ue-U)*Ve+U*(Ve-V), and the reverse telescoping after adjoint.',
        actual_positive_half_word='i*(I+i*A(h_circ))*Q_(d_star) modulo the fully paid order-two calculus error',
        actual_negative_half_word='i*Q_(-d_star)*(I+i*A(h_circ)) modulo the fully paid order-two calculus error',
        actual_positive_return_before_rotation='I+(I+i*A(b_geom))*Q_(2*d_star)',
        actual_negative_return_before_reflection='I+Q_(-2*d_star)*(I+i*A(b_geom))',
        exact_positive_rotation_conjugation='Q_omega*A_positive*Q_(-omega), omega=2*d_star',
        exact_negative_linear_reflection='J_ref f(x)=f(-x), a complex-linear isometry from the negative to the positive cone',
        positive_R104_coefficient='b_geom(x)=h_circ(x)+h_circ(x+d_star)',
        second_R104_coefficient='b_geom(-x)',
        both_diagonal_frequencies='j>=1, omega=2*d_star, same +beta/j on both blocks',
        model_full_augmented_space='two positive-frequency scalar normal forms, first-root mean 2, second-root block I, two regular blocks 2; all actual couplings remain in R',
        Q_factor_budget={name:{k:record(v) if isinstance(v,arb) else v for k,v in z.items()} for name,z in Qs.items()},
        phase_factor_budget={name:dict(count=phase_counts[name],**{k:record(v) for k,v in z.items()}) for name,z in phases.items()},
        bounds={k:record(v) for k,v in dict(
            complete_Q_factor_product=Pq,complete_one_plus_phase_product=Pphase,
            complete_word_product=Ptot,all_masks_means_ordering_and_adjoints=elementary,
            complete_two_or_more_phase_terms=quadratic,complete_symmetric_covariance_error=covariance,
            final_full_phase_left_to_symmetric_ordering=bp['ordering_gain_two'],
            true_transmission_feedback_error_forward=Ea_p,
            true_transmission_feedback_error_opposite=Ea_m,
            true_transmission_to_model_return_both_windows=return_change,
            true_transmission_preconditioned_word_forward=newword_p,
            true_transmission_preconditioned_word_opposite=newword_m,
            complete_order_two_word_calculus=calculus,full_R4over3_forward=Rp,
            full_R4over3_opposite=Rm,full_R4over3_both_base_windows=R,
            corresponding_unscaled_full_R4over3=unscaled,full_b_analytic_modulus=bM,
            complete_physical_reconstruction_L2=reconstruction).items()},
        full_b_analytic_strip=phase['sup_strip'],
        full_nonmean_Wiener_bounds=phase['complete_nonmean_Wiener_bounds_orders_0_through_12'],
        full_final_ordinary_and_contact_source_columns_L2=source,
        source_scope='The exact earlier physical ordinary/contact norms, transported to final L2. No H1 source bound or weak-to-ordinary relabeling is inferred.',
        scaled_strong_windows=[['0','4/3'],['-4/3','0']],
        interpolated_base_window=['-4/3','0'],
        same_actual_operator_b_identification_proved=True,
        entire_unweighted_base_Rstar_proved=True,
        all_four_branches_both_means_independent_regular_rows_and_head_paths_retained=True,
        uniform_higher_Sobolev_window_proved=False,weighted_same_width_Rstar_proved=False,
        effective_numerically_usable_cutoff_proved=False,finite_head_inverse_proved=False,
        feedback_inverse_proved=False,new_deep_tail_profile_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_root_physical_graph_operator.py','fourfold_strict_high_energy_triangular.py',
            'fourfold_strict_windowed_density_R46.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,qC=qC.str(10),calculus=calculus.str(10),
        forward=Rp.str(10),opposite=Rm.str(10),unscaled=unscaled.str(10),
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__': main()
