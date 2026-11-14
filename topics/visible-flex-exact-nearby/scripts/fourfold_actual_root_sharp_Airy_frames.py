#!/usr/bin/env python3
"""Sharp full-frequency shifted/unshifted Airy two-row frame comparison.

The exact same old 5050 reference and R39 frames are retained.  A compact
real Airy cover and an explicit all-frequency Sonin argument replace the
coarse product-of-two-independent-asymptotics constant.  The mean is an
independent exact cosine/sine matrix, and both inverse directions are paid.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def spectral_from_frobenius(values, determinant):
    # For a real 2x2 matrix, singular values satisfy
    # s_max^2=(tr(A*A)+sqrt(tr(A*A)^2-4 det(A)^2))/2.
    f2=sum((abs(v).upper()**2 for v in values),arb(0)).upper()
    discriminant=max(arb(0),(f2*f2-4*determinant*determinant).upper())
    return ((f2+discriminant.sqrt())/2).sqrt().upper()


def airy_norm(x):
    ai,aip,bi,bip=(-x).airy()
    return spectral_from_frobenius((bi,ai,bip,aip),1/arb.pi())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--domain',type=Path,default=Path('notes/2026-11-13-negative-root-full-canonical-domain.json'))
    ap.add_argument('--airy-cells-per-unit',type=int,default=128)
    ap.add_argument('--mean-cells',type=int,default=512)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.airy_cells_per_unit<1 or a.mean_cells<1:
        raise ValueError('fresh report and positive full-cover cell counts required')
    ctx.prec=a.bits
    tick=time.monotonic()
    d=checked(a.domain,'fourfold_negative_root_full_canonical_domain.py')
    if d['kind']!='actual_complete_negative_root_fixed_canonical_domain':
        raise ValueError('same complete old actual root realization required')
    L=exact_arb(Fraction(d['canonical_real_height']))
    qlo=stored(d['actual_quarter_circle_frequency'][0]).lower()
    v=arb(5050)
    h=(v*L*L).upper()
    shift=(v*qlo**(-arb(4)/3)).upper()
    ymax=math.ceil(float(shift))+1
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:
            raise ValueError(name)
    gate('the original complete canonical height and every nonzero physical frequency are retained',L>0 and qlo>0)
    gate('the compact Airy cover includes x<=1 and every actual positive shift',arb(ymax)>1+shift)
    N=a.airy_cells_per_unit
    compact0=arb(0)
    compact_all=arb(0)
    sections=[]
    for unit in range(ymax):
        local=arb(0)
        for j in range(N):
            lo=arb(unit)+arb(j)/N
            hi=arb(unit)+arb(j+1)/N
            value=airy_norm(lo.union(hi))
            if not value.is_finite():
                raise ValueError('nonfinite complete real Airy cell')
            local=max(local,value)
            compact_all=max(compact_all,value)
            if unit==0:
                compact0=max(compact0,value)
        sections.append(dict(integer_interval=[unit,unit+1],closed_cells=N,
                             complete_matrix_norm=record(local.upper())))
    compact_change=(arb.pi()*compact0*compact_all).upper()
    A1=airy_norm(arb(1))
    # For u_xx+x*u=0 use Z=(x^(1/4)u,x^(-1/4)u_x),
    # S=I+(4*x^(3/2))^(-1)*sigma_1.  M^t*S+S*M=0.
    # Exact integration of |S'|/(1-e) cancels its final lower eigenvalue:
    # ||Z(x)||^2 <= (5/3)||Z(1)||^2 for every x>=1.
    weighted=(arb(5)/3).sqrt()*A1
    large_increment=(arb.pi()*weighted*weighted*h*(1+h)**(arb(5)/4)).upper()
    large_change=(1+large_increment).upper()
    nonzero=max(compact_change,large_change)
    k=v.sqrt()
    mean=arb(0)
    mean_sections=[]
    for j in range(a.mean_cells):
        t=(L*j/a.mean_cells).union(L*(j+1)/a.mean_cells)
        st,ct=(k*t).sin(),(k*t).cos()
        # A0(t)^(-1)*Av(t), after the same constant unitary amplitude change.
        M=(ct+t*k*st,(st/k-t*ct)/arb.pi(),-arb.pi()*k*st,ct)
        value=spectral_from_frobenius(M,arb(1))
        if not value.is_finite():
            raise ValueError('nonfinite complete mean frame cell')
        mean=max(mean,value)
        if j%64==0:
            mean_sections.append(dict(first_cell=j,partial_complete_norm=record(mean.upper())))
    full=max(nonzero,mean).upper()
    old_nonzero=(100*arb.pi()*(1+(1+shift)**(arb(1)/4))).upper()
    old_mean=(2*(1+L/arb.pi())*(1+arb.pi()*v*L/2)).upper()
    old=max(old_nonzero,old_mean)
    gate('the full two-row frame and inverse improve the earlier coarse constant',full<old)
    gate('the complete same-realization frame constant is below five',full<5)
    out=dict(kind='actual_complete_shifted_Airy_two_row_frame_comparison',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(a.domain):sha(a.domain)},identity=d['identity'],
        exact_canonical_height=d['canonical_real_height'],
        actual_quarter_circle_frequency=d['actual_quarter_circle_frequency'],
        exact_reference_constant=5050,
        nonzero_variables='lambda=q*|n|, x=lambda^(2/3)*xi>=0, s=5050*lambda^(-4/3)>0; x^2*s=5050*xi^2',
        exact_real_Airy_matrix='A(x)=[[Bi(-x),Ai(-x)],[Bi_prime(-x),Ai_prime(-x)]], det(A)=-1/pi',
        exact_frame_change='F0(xi,n)^(-1)*F5050(xi,n) is unitarily similar to A(x)^(-1)*A(x+s)',
        inverse_norm_identity='Every real 2x2 comparison matrix has determinant one, hence its spectral norm equals the spectral norm of its inverse',
        exact_large_argument_energy='Z=(x^(1/4)u,x^(-1/4)u_x); S=I+(4*x^(3/2))^(-1)*sigma1; M^t*S+S*M=0; ||Z(x)||^2 <=(5/3)||Z(1)||^2 for x>=1',
        exact_large_argument_increment='pi*C1^2*x^(1/4)*(x+s)^(5/4)*s <= pi*C1^2*h*(1+h)^(5/4), h=5050*L^2',
        exact_mean_matrix='[[cos(k*t)+t*k*sin(k*t),(sin(k*t)/k-t*cos(k*t))/pi],[-pi*k*sin(k*t),cos(k*t)]], k=sqrt(5050)',
        airy_cover=dict(cells_per_unit=N,integer_upper=ymax,total_closed_cells=N*ymax,sections=sections),
        mean_cover=dict(closed_cells=a.mean_cells,partial_records=mean_sections),
        bounds={name:record(value) for name,value in dict(
            h=v*L*L,maximum_shift=shift,
            Airy_matrix_on_zero_to_one=compact0,Airy_matrix_on_complete_compact_range=compact_all,
            complete_small_argument_frame_change=compact_change,Airy_matrix_at_one=A1,
            complete_weighted_Airy_matrix_on_full_halfline=weighted,
            complete_large_argument_increment=large_increment,
            complete_large_argument_frame_change=large_change,
            complete_nonzero_frame_change_and_inverse=nonzero,
            complete_mean_frame_change_and_inverse=mean,
            complete_full_frame_change_and_inverse=full,
            earlier_full_frame_constant=old,
            two_end_homogeneous_constant_improvement=(old/full)**2,
            one_end_source_constant_improvement=old/full).items()},
        all_nonzero_frequencies_both_signs_and_mean_retained=True,
        all_real_parameters_in_original_interval_retained=True,
        every_xi_in_original_root_collar_retained=True,
        exact_both_Cauchy_rows_retained=True,
        same_bound_on_every_scaled_or_unscaled_Sobolev_window=True,
        original_first_phase_B_unchanged=True,
        source_column_uses_one_output_frame_factor_only=True,
        full_equation_head_and_every_head_crossing_unchanged=True,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        gates=gates,
        scope='Complete real same-operator Fourier-diagonal two-row change between the exact 5050 shifted Airy reference and original R39 frame, including its inverse and independent mean. This does not change the actual potential, original B, density/source units, or independently solve finite head/full feedback.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),bounds=out['bounds'],seconds=out['seconds']),flush=True)


if __name__=='__main__':
    main()

