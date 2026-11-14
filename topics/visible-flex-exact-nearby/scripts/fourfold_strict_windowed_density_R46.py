#!/usr/bin/env python3
"""Actual strict R46 bounds at the requested window, using the complete density proof.

No native field or ray is recomputed. The real Jacobian is used only for real
leading Bell coefficients and Jacobian factors; complex higher derivatives
and analytic strip widths retain their separately paid complete bounds.
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
from fourfold_strict_high_energy_triangular import positive_matrix_bound,weighted_principal
from fourfold_negative_root_physical_graph_operator import mult,complete_moment
from fourfold_strict_scaled_complete_R46_budget import scaled_ibp_cross,matrix_record
from fourfold_strict_complete_R46_budget import composition_constants


def upper(row):return stored(row).upper()
def lower(row):return stored(row).lower()
def ceiling(x):return -(-x.numerator//x.denominator)


def real_refined_compositions(N,Cr,Cc,width,order):
    H=[arb(0),Cr]+[(math.factorial(j-1)*Cc/(width/2)**(j-1)).upper()
                  for j in range(2,order+1)]
    B=[[arb(0) for _ in range(order+1)] for _ in range(order+1)]
    B[0][0]=arb(1)
    for j in range(1,order+1):
        for ell in range(1,j+1):
            B[j][ell]=sum((math.comb(j-1,b-1)*H[b]*B[j-b][ell-1]
                          for b in range(1,j-ell+2)),arb(0)).upper()
    A=acb_mat([[B[j][ell]/arb(N)**(j-ell) if ell<=j else 0
               for ell in range(order+1)] for j in range(order+1)])
    T=acb_mat(order+1,order+1)
    for j in range(order+1):
        for ell in range(j+1):
            v=Cr if j==ell else math.factorial(j-ell)*Cc/(N*width/2)**(j-ell)
            T[j,ell]=math.comb(j,ell)*v
    pos=[];neg=[];jac=[]
    for k in range(order+1):
        p=(Cr.sqrt()*positive_matrix_bound(weighted_principal(A,k))).upper()
        m=positive_matrix_bound(weighted_principal(T,k)).upper()
        pos.append(p);jac.append(m);neg.append((m*p).upper())
    return dict(matrix=A,inverse_Jacobian_matrix=T,positive=pos,negative=neg,
                inverse_Jacobian=jac,uniform=max(pos+neg).upper())


def true_cross(N,width,derivative_lower,M,p,gain,same):
    decay=(derivative_lower*width/2).lower()
    inp=complete_moment(N,2*decay,2*p)
    out=complete_moment(N,2*decay,2*(p+gain))
    direct=(M*(inp*out).sqrt()).upper()
    diff=complete_moment(N,2*decay,2*p,2*gain)
    split=(same+M*(diff*inp).sqrt()/arb(N)**gain).upper()
    return min(direct,split).upper()


def energy_window(row,T):
    """Exact half-integer interpolation, with flux-dual negative indices."""
    T=abs(Fraction(T))
    levels={Fraction(v['half_integer']):upper(v['full_physical_Cauchy'])
            for v in row['derivative_rows']}
    if T>max(levels):raise ValueError('requested Cauchy window exceeds the paid density proof')
    vals=[v for k,v in levels.items() if k<=T]
    if T<=Fraction(1,2):
        endpoint=levels[Fraction(1,2)]
        description=dict(lower='-1/2',upper='1/2',flux_dual_equal_bound=True)
    elif T in levels:
        endpoint=levels[T];description=dict(exact_half_integer=str(T))
    else:
        left=max(k for k in levels if k<T);right=min(k for k in levels if k>T)
        t=(T-left)/(right-left)
        endpoint=(levels[left]**exact_arb(1-t)*levels[right]**exact_arb(t)).upper()
        description=dict(lower=str(left),upper=str(right),upper_fraction=str(t))
    return max(vals+[endpoint]).upper(),dict(endpoint=str(T),interpolation=description,
        endpoint_bound=record(endpoint),uniform_bound=record(max(vals+[endpoint]).upper()))


def frame(N,T,mp,mup,tp,field_width):
    power=Fraction(T)+Fraction(1,2);scale=arb(4*N)
    Mm=mult(N,power,mp,field_width)
    Mr=mult(N,power,mup.sqrt(),field_width)
    Mt=mult(N,power,tp,field_width)
    u=arb(2)**(arb(1)/4)*Mm
    F=(u*u+(Mt*u+scale.sqrt()*Mr)**2).sqrt().upper()
    I=(scale*Mr*Mr+arb(2).sqrt()*Mm*Mm*(1+Mt*Mt)).sqrt().upper()
    return F,I


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-complete-actual-strict-operator.json'))
    p.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--density',type=Path,default=Path('notes/2026-11-13-R46-complete-density-transport-bootstrap.json'))
    p.add_argument('--real-rays',type=Path,default=Path('notes/2026-11-13-R106-complete-relative-real-Jacobian.json.gz'))
    p.add_argument('--scales',type=int,nargs='+',default=[4096,16384,65536,1048576])
    p.add_argument('--windows',type=Fraction,nargs='+',default=[Fraction(0),Fraction(4,3),Fraction(2),Fraction(8)])
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or any(N<1 for N in a.scales) or any(S<0 or S>8 for S in a.windows):
        raise ValueError('fresh output, positive scales and paid finite windows required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.strict,'fourfold_strict_complete_R46_budget.py')
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    b=checked(a.density,'fourfold_strict_density_transport_bootstrap.py')
    r=checked(a.real_rays,'fourfold_true_relative_ray_jacobian_cells.py')
    if not d['identity']==f['identity']==b['identity']==r['identity']:
        raise ValueError('actual strict/ray/density families differ')
    if d['inputs'].get(str(a.fields))!=sha(a.fields) or f['object_sha256']!=sha(f['object_path']):
        raise ValueError('actual complete field identity differs')
    if len(f['cells'])!=215 or d['positive_cells']!=215:
        raise ValueError('the entire original 215-cell cover is required')
    cursor=Fraction(0);Ms=[];mp=[];mup=[];tp=[];mumin=[]
    for cell in f['cells']:
        left,right=Fraction(cell['left']),Fraction(cell['right'])
        if left!=cursor or not left<right:raise ValueError('actual continuous cover has a gap')
        cursor=right
        Ms.append({k:upper(v) for k,v in cell['complete_complex_field_moduli'].items()})
        mp.append(upper(cell['geometry']['m_modulus_upper']))
        mup.append(Ms[-1]['mu']);tp.append(Ms[-1]['T'])
        mumin.append(lower(cell['geometry']['mu_modulus_lower']))
    if str(cursor)!=d['exact_physical_interval'][1]:
        raise ValueError('actual complete physical endpoint is missing')
    rows={x['scale']:x for x in b['rows']}
    if any(N not in rows for N in a.scales):raise ValueError('a requested scale lacks the complete density proof')
    Cr=upper(r['full_real_relative_map_and_inverse_derivative'])
    Cc=upper(d['actual_relative_flow']['relative_derivative_modulus'])
    width=4*lower(d['actual_relative_flow']['full_physical_angle_strip'])
    fw=4*exact_arb(Fraction(f['physical_angle_strip']))
    if not 1<Cr<Cc:raise ValueError('real and complex derivative permissions are not separated')
    H=upper(d['full_strict_phase_modulus']);RP=upper(d['full_both_sides_Pmh_integral'])
    ep=Ms[-1];mu=mumin[-1]
    initfield=mp[-1]*ep['Fcal']*ep['a']/(2*mu)
    momfield=Cc*ep['Fcal']*ep['a']/(2*mu**2)
    oldcross=composition_constants(Cc,width)
    B24=oldcross['cross_constant'](arb(1),constant=True)
    Bh24=oldcross['cross_constant'](H)
    cross_strip=(width/(4*Cr*Cc)).lower()
    cross_lower=(1/(2*Cr)).lower()
    out=dict(kind='actual_full_strict_R46_requested_window_density_budget',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(x):sha(x) for x in (a.strict,a.fields,a.density,a.real_rays)},
        identity=d['identity'],exact_physical_interval=d['exact_physical_interval'],
        native_cells_recomputed=0,all_215_original_cells_reused=True,
        real_relative_derivative=record(Cr),unchanged_complex_relative_derivative=record(Cc),
        unchanged_normalized_complex_flow_strip=record(width),normalized_field_strip=record(fw),
        real_and_complex_permissions_separate=True,
        complete_positive_real_cross_strip=record(cross_strip),
        complete_cross_complex_derivative_real_lower=record(cross_lower),
        actual_full_phase_modulus=record(H),actual_full_Pmh_integral=record(RP),
        unchanged_physical_Lambda='max(1,4*abs(n)); exact mean one',
        ordinary_source='unchanged physical scalar f in L1(dr;H_N^(s-1/2))',
        rows=[],all_four_branches_means_and_all_head_paths_retained=True,
        full_returned_Rstar_proved=False,effective_feedback_cutoff_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_strict_scaled_complete_R46_budget.py','fourfold_strict_complete_R46_budget.py',
            'fourfold_strict_high_energy_triangular.py','fourfold_negative_root_physical_graph_operator.py',
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')})
    for N in a.scales:
        scale=arb(4*N);entries=[]
        amplitudes=[]
        for T in sorted(set([Fraction(0),Fraction(4,3),Fraction(2)]+[S+2 for S in a.windows])):
            E,interp=energy_window(rows[N],T)
            F,I=frame(N,T,max(mp),max(mup),max(tp),fw)
            amplitudes.append(dict(window=str(T),Cauchy=record(E),Cauchy_interpolation=interp,
                frame=record(F),inverse_frame=record(I),
                amplitude_and_inverse=record((I*E*F).upper()),
                ordinary_source_to_amplitude=record((I*E).upper())))
        for S in a.windows:
            T=S+2;E,interp=energy_window(rows[N],T)
            F,I=frame(N,T,max(mp),max(mup),max(tp),fw)
            degree=ceiling(S+Fraction(5,2))
            comp=real_refined_compositions(N,Cr,Cc,width,degree);Nc=comp['uniform']
            p1=ceiling(S+Fraction(1,2));ph=ceiling(S+Fraction(3,2));po=ceiling(S+2)
            defect=(arb(2)**(arb(3)/4)*mult(N,S+Fraction(3,2),initfield,fw)).upper()
            residual=(4*arb(2)**(arb(1)/4)*Nc*mult(N,S+Fraction(3,2),RP,width)).upper()
            Cerr=(I*E*(defect+residual+F)+1).upper()
            X1a=true_cross(N,cross_strip,cross_lower,arb(1),p1,2,Nc)
            Xha=true_cross(N,cross_strip,cross_lower,H,ph,1,mult(N,ph,H,width)*Nc)
            X1b=scaled_ibp_cross(N,B24,p1,2,Nc)
            Xhb=scaled_ibp_cross(N,Bh24,ph,1,mult(N,ph,H,width)*Nc)
            X1=min(X1a,X1b);Xh=min(Xha,Xhb)
            X=(scale.sqrt()*(arb(2)**(arb(1)/4)*X1+arb(2)**(arb(3)/4)*Xh)).upper()
            mom=(2*mult(N,S+Fraction(3,2),momfield,width)*Nc).upper()
            order=(8*H*complete_moment(N,width,po,1)).upper()
            Qbound=(arb(2)**(arb(1)/4)*scale.sqrt()*Nc).upper()
            R2=(Cerr+4*(2*X+mom+Qbound*order)).upper()
            W=max(arb(1),(Qbound*(1+mult(N,degree,H,width))).upper()).upper()
            row=dict(strong_window=str(S),Cauchy_window=str(T),Cauchy=record(E),
                Cauchy_interpolation=interp,largest_frame_multiplier_order=str(S+Fraction(5,2)),
                largest_defect_and_residual_multiplier_order=str(S+Fraction(3,2)),
                largest_composition_integer=degree,
                composition_positive=[record(v) for v in comp['positive']],
                composition_negative=[record(v) for v in comp['negative']],
                inverse_Jacobian_multiplier=[record(v) for v in comp['inverse_Jacobian']],
                complete_composition_matrix=matrix_record(comp['matrix']),
                complete_inverse_Jacobian_matrix=matrix_record(comp['inverse_Jacobian_matrix']),
                uniform_composition=record(Nc),frame=record(F),inverse_frame=record(I),
                full_initial_momentum_defect=record(defect),full_ordinary_residual=record(residual),
                full_source_and_mean_correction=record(Cerr),
                cross_unit_analytic=record(X1a),cross_h_analytic=record(Xha),
                cross_unit_IBP=record(X1b),cross_h_IBP=record(Xhb),
                full_cross_and_mean_output=record(X),full_remaining_momentum=record(mom),
                full_ordering=record(order),full_Q=record(Qbound),
                full_W0_bound=record(W),full_strong_R2=record(R2),proved=True)
            entries.append(row)
            print(dict(N=N,window=str(S),Cauchy=E.str(9),composition=Nc.str(9),R2=R2.str(9)),flush=True)
        out['rows'].append(dict(scale=N,physical_derivative_scale=4*N,
            complete_amplitude_windows=amplitudes,complete_strong_windows=entries))
    out.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='The same complete strict R46 decomposition, with constants paid at their requested finite window rather than the largest available window. All physical sources, full mean, four branches and all finite-head paths remain. The actual real Jacobian improves only real leading coefficients; every complex derivative and cross-cone estimate retains its full paid domain.')
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=out['seconds']),flush=True)


if __name__=='__main__':main()
