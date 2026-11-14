#!/usr/bin/env python3
"""Complete density-Q bounds by the exact Bessel trace energy.

No sqrt(N) conversion is used.  Positive integer windows are a full Bell
triangle; opposite windows use the exact D/Lambda flux identity and the
complete mean row.  All maps and all inverse jets are those already paid.
"""
from __future__ import annotations
import argparse,math,time
from pathlib import Path
from flint import arb,acb_mat,ctx
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_strict_high_energy_triangular import positive_matrix_bound,weighted_principal


def up(z):return stored(z).upper()
def lo(z):return stored(z).lower()


def bell_with_derivative(jets,order):
    B=[[arb(0) for _ in range(order+1)] for _ in range(order+1)]
    E=[[arb(0) for _ in range(order+1)] for _ in range(order+1)]
    B[0][0]=arb(1)
    for j in range(1,order+1):
        for k in range(1,j+1):
            for v in range(1,j-k+2):
                c=math.comb(j-1,v-1)
                B[j][k]+=c*jets[v]*B[j-v][k-1]
                E[j][k]+=c*(jets[v+1]*B[j-v][k-1]+jets[v]*E[j-v][k-1])
            B[j][k]=B[j][k].upper();E[j][k]=E[j][k].upper()
    return B,E


def positive_triangle(N,jets,inverse_first,order):
    CJ=max(jets[1],inverse_first)
    B,E=bell_with_derivative(jets,order)
    T=acb_mat(order+1,order+1)
    for j in range(order+1):
        for l in range(j+1):
            value=CJ.sqrt()*B[j][l]
            if l<j:
                value+=(inverse_first/2).sqrt()*E[j][l+1]
            T[j,l]=value/arb(N)**(j-l)
    constants=[positive_matrix_bound(weighted_principal(T,j)).upper()
               for j in range(order+1)]
    return T,constants


def mean_row(N,inverse_jets,forward_first,order):
    # G=H^-1 has mean G'=1 and 1/forward_first <= G' <= inverse_jets[1].
    variance=((inverse_jets[1]-1)*(1-1/forward_first)).upper()
    if variance<0:raise ValueError('circle derivative bounds must contain their exact mean one')
    result=[]
    for k in range(order+1):
        value=variance
        for j in range(1,k+1):
            value+=math.comb(k,j)*inverse_jets[j+1]**2/arb(N)**(2*j)
        result.append(value.sqrt().upper())
    return result


def complete_pair(N,forward,inverse,order=2):
    if forward[1]<1 or inverse[1]<1:
        raise ValueError('complete degree-one circle derivative bounds required')
    Tf,pf=positive_triangle(N,forward,inverse[1],order)
    Ti,pi=positive_triangle(N,inverse,forward[1],order)
    # The actual old Lambda is max(1,|n|), not sqrt(1+n^2).
    # S=(Lambda/sqrt(1+D^2))^(1/2) has norm <=1 and inverse
    # norm <=2^(1/4), so Q_actual=S Q_Bessel S^-1.
    conversion=arb(2)**(arb(1)/4)
    pf=[(conversion*x).upper() for x in pf]
    pi=[(conversion*x).upper() for x in pi]
    mf=mean_row(N,inverse,forward[1],order)
    mi=mean_row(N,forward,inverse[1],order)
    base=(conversion*max(forward[1],inverse[1]).sqrt()).upper()
    # The actual nonzero J=D/Lambda is exactly sign(D); its norm and
    # inverse norm are one. Both complete mean rows are added separately.
    nf=[base]+[(pi[k]+mf[k]).upper() for k in range(1,order+1)]
    ni=[base]+[(pf[k]+mi[k]).upper() for k in range(1,order+1)]
    def matrix(A):return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]
    return dict(full_real_forward_jets=[record(v) for v in forward[1:]],
        full_real_inverse_jets=[record(v) for v in inverse[1:]],
        exact_Bessel_to_actual_Lambda_conversion=record(conversion),
        complete_unscaled_L2_Q_inverse_and_adjoints=record(base),
        full_forward_positive_triangle=matrix(Tf),full_inverse_positive_triangle=matrix(Ti),
        integer_windows=[dict(order=k,forward_positive=record(pf[k]),inverse_positive=record(pi[k]),
            forward_negative=record(nf[k]),inverse_negative=record(ni[k]),
            complete_forward_mean_adjoint_row=record(mf[k]),
            complete_inverse_mean_adjoint_row=record(mi[k])) for k in range(order+1)],
        full_Q_inverse_and_adjoints_plus_minus_two=record(max(pf+pi+nf+ni).upper()))


def symmetric_jets(C,width):
    return [arb(0)]+[(math.factorial(j-1)*C/(width/2)**(j-1)).upper() for j in range(1,4)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    ap.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    ap.add_argument('--real-rays',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz'))
    ap.add_argument('--scale',type=int,default=1048576)
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.scale<1:raise ValueError('new output and positive norm scale required')
    ctx.prec=a.bits;tick=time.monotonic()
    n=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    r=checked(a.real_rays,'fourfold_actual_relative_ray_real_jets.py')
    if n['inputs'].get(str(a.graph))!=sha(a.graph) or n['identity']!=r['identity']:
        raise ValueError('same complete actual normal form/graph/ray family required')
    if not (r['all_550_true_segments_and_4400_exact_controls']
        and r['all_549_exact_seams_checked'] and r['all_real_angles']
        and r['all_pairs_of_strict_times_and_both_directions']):
        raise ValueError('complete all-time actual real ray jets required')
    if a.scale!=n['scale']:raise ValueError('the requested old normal-form scale differs')
    b=g['complete_bounds']
    ph=symmetric_jets(up(b['physical_CJ']),lo(b['physical_angle_and_inverse_common_strip']))
    gr=symmetric_jets(up(b['true_flow_and_inverse_derivative']),lo(b['true_flow_strip']))
    jr={z['order']:up(z['accepted_complete_relative_derivative'])
        for z in r['whole_time_relative_derivative_bounds']}
    sr=[arb(0),up(r['accepted_relative_first_derivative']),jr[2],jr[3]]
    cj=n['final_root_label_bounds']['real_inverse_jet_calculation']
    cf=[arb(0)]+[up(z) for z in cj['full_real_derivative_jets'][:3]]
    ci=[arb(0)]+[up(z) for z in cj['full_inverse_real_derivative_jets'][:3]]
    pairs={'physical_cut':(ph,ph),'graph':(gr,gr),'strict':(sr,sr),'actual_final_circle':(cf,ci)}
    rows={name:complete_pair(a.scale,f,i) for name,(f,i) in pairs.items()}
    product=arb(1)
    for name,z in rows.items():
        count=n['Q_factor_budget'][name]['count']
        z['exact_word_factor_count']=count
        z['prior_full_Q_norm']=n['Q_factor_budget'][name]['norm']
        z['improvement_factor']=record((up(z['prior_full_Q_norm'])/up(z['full_Q_inverse_and_adjoints_plus_minus_two'])).upper())
        product*=max(arb(1),up(z['full_Q_inverse_and_adjoints_plus_minus_two']))**count
    base=up(rows['actual_final_circle']['complete_unscaled_L2_Q_inverse_and_adjoints'])
    qC=up(rows['actual_final_circle']['full_Q_inverse_and_adjoints_plus_minus_two'])
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    for name,z in rows.items():
        gate('complete '+name+' map inverse adjoints improve the prior real-window bound',
             up(z['full_Q_inverse_and_adjoints_plus_minus_two'])<up(z['prior_full_Q_norm']))
    gate('complete Q word product improves without dropping any original factors',
         product<up(n['bounds']['complete_Q_factor_product']))
    out=dict(kind='actual_complete_density_Q_Bessel_energy_and_mean_flux_windows',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,scale=a.scale,
        inputs={str(p):sha(p) for p in (a.normal_form,a.graph,a.real_rays)},
        identity=n['identity'],native_geometric_cells_recomputed=0,
        exact_Q='Lambda^(1/2) C_H Lambda^(-1/2), Lambda_n=max(1,abs(n)), including Lambda_0=1',
        exact_Bessel_trace_energy='||f||_H(1/2)^2 = inf_U integral_(y>=0) (|U_x|^2+|U_y|^2+|U|^2); minimum U=e^(-y*Lambda)f',
        exact_base_bound='||Q_H||_L2,||Q_H^-1||_L2 <= 2^(1/4)*sqrt(max(sup H_prime,1/inf H_prime)); the factor converts the actual max-Lambda from the Bessel trace weight',
        exact_tame_product='In Bessel half spaces: ||a*C_H*g||_H(1/2) <= ||a||inf sqrt(CJ)||g||_H(1/2) + ||a_prime||inf/sqrt(2*m) ||g||_H(-1/2)',
        derivative_reduction='||D^k Lambda^(-1)f||_2 <= ||D^(k-1) f||_2 for k>=1, without a projection',
        exact_full_flux_identity='Q_H^*(D/Lambda)Q_H=D/Lambda; the actual mean is the kernel and is retained as an independent full row',
        exact_mean_block='Q_H=[[1,b],[0,A]], A^*J A=J, J=sign(D) has norm and inverse norm one on all nonzero modes; b^*=Lambda^(-1/2)(G_prime-1), G=H^-1',
        mean_variance='integral(G_prime-1)^2 <= (sup G_prime-1)*(1-inf G_prime), because its exact mean is one',
        rows=rows,
        summary={name:record(value.upper()) for name,value in dict(
            full_Q_word_factor_product=product,prior_Q_word_factor_product=up(n['bounds']['complete_Q_factor_product']),
            whole_Q_word_product_improvement=up(n['bounds']['complete_Q_factor_product'])/product,
            actual_final_Q_base_and_inverse=base,actual_final_Q_plus_minus_two=qC,
            complete_physical_base_reconstruction=2*base).items()},
        both_base_strong_windows_and_their_adjoints_covered=True,
        all_mean_rows_inverse_columns_and_all_head_paths_retained=True,
        no_frequency_projection_or_compressed_equation_used=True,
        real_jets_used_only_for_real_Sobolev_norms=True,
        old_complex_strip_cross_and_phase_permissions_unchanged=True,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_strict_high_energy_triangular.py')},
        scope='Complete same-object density coordinate maps, inverses and adjoints on every H_N^s for -2<=s<=2, with exact Bessel base norm and full mean row. The old complex contour errors are not improved by this real theorem. Full return and finite head are separate.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),summary=out['summary'],
        maps={name:z['full_Q_inverse_and_adjoints_plus_minus_two'] for name,z in rows.items()},seconds=out['seconds']),flush=True)


if __name__=='__main__':main()

