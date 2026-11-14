#!/usr/bin/env python3
"""Finite physical columns of the exact nominal root shear, with full errors.

All finite column centers are exact binary64 numbers.  Directed Taylor/FFT
evaluation, native Arb DFTs, physical aliases, canonical coefficient errors,
the infinite canonical tail, and the full actual-to-nominal operator change
are paid separately.  No finite polynomial is substituted for the geometry.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import time

import numpy as np
from flint import acb, arb, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_box import CBox, DirectedFFT, arb_box, zeros
from fourfold_phase_root_interval import Box, stack
from fourfold_phase_root_fourier_fit import read, save, sha, stored, decode
from fourfold_phase_nominal_potential_modes import evaluate_cosine, evaluate_angle


def array_box(values):
    return stack([arb_box(value) for value in values])


def midpoint_dft(values, cutoff, modulus, strip):
    """Projected Fourier error from nodal RMS, Arb rounding, and all aliases."""
    Q = len(values.real.lo)
    real = values.real.lo/2+values.real.hi/2
    imag = values.imag.lo/2+values.imag.hi/2
    # The centers themselves are exact dyadics; their construction needs no
    # rounding claim.  Subtraction in Arb measures the complete box distance.
    square = arb(0)
    for j in range(Q):
        er = max(abs(arb(float(values.real.lo[j]))-arb(float(real[j]))),
                 abs(arb(float(values.real.hi[j]))-arb(float(real[j]))))
        ei = max(abs(arb(float(values.imag.lo[j]))-arb(float(imag[j]))),
                 abs(arb(float(values.imag.hi[j]))-arb(float(imag[j]))))
        square += er*er+ei*ei
    node_rms = (square/Q).sqrt().upper()
    transformed = [z/Q for z in acb.dft([acb(float(r),float(i)) for r,i in zip(real,imag)])]
    centers = np.empty(2*cutoff+1,dtype=np.float64)
    round_square = alias_square = arb(0)
    denominator = 1-(-4*strip*Q).exp()
    for index,n in enumerate(range(-cutoff,cutoff+1)):
        z = transformed[n%Q]
        center = float(z.real.mid()); centers[index] = center
        # The actual function has f(-theta)=conjugate(f(theta)), hence all
        # exact Fourier coefficients are real.  Keeping the imaginary DFT
        # discrepancy here makes this enclosure valid even without that fact.
        rounding = abs(z-acb(center)).upper()
        round_square += rounding*rounding
        alias = modulus*((-4*strip*(Q-abs(n))).exp()
                       +(-4*strip*(Q+abs(n))).exp())/denominator
        alias_square += alias*alias
    rounding = round_square.sqrt().upper()
    aliases = alias_square.sqrt().upper()
    return centers,dict(nodal_discrete_RMS_error=ball_record(node_rms),
        native_DFT_and_center_error_L2=ball_record(rounding),
        complete_physical_alias_L2=ball_record(aliases),
        projected_column_L2_error=ball_record((node_rms+rounding+aliases).upper()))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--modes-report',type=Path,
        default=Path('notes/2026-11-12-nominal-root-potential-canonical-modes.json.gz'))
    p.add_argument('--physical-tail',type=Path,
        default=Path('notes/2026-11-12-actual-canonical-physical-column-weighted-tails.json'))
    p.add_argument('--physical-grid',type=int,default=16384)
    p.add_argument('--physical-cutoff',type=int,default=4096)
    p.add_argument('--canonical-grid',type=int,default=8192)
    p.add_argument('--taylor-order',type=int,default=16)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out-dir',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits
    wall,cpu=time.monotonic(),time.process_time()
    Q,N,G,J=a.physical_grid,a.physical_cutoff,a.canonical_grid,a.taylor_order
    if Q&(Q-1) or G&(G-1) or Q<=2*N or N<1 or J<1:
        raise ValueError('power-of-two grids and a strict physical Nyquist margin are required')
    modes=read(a.modes_report)
    if not modes['complete'] or sha(modes['nominal_path'])!=modes['nominal_sha256']:
        raise ValueError('incomplete or changed nominal canonical modes')
    nominal=read(modes['nominal_path']);fit=read(nominal['fit_path'])
    if not nominal['proved'] or sha(nominal['fit_path'])!=nominal['fit_sha256']:
        raise ValueError('changed full actual-to-nominal comparison')
    potential=[decode(c['midpoint_dyadic']) for c in modes['coefficients']]
    rho=[stored(c['midpoint_error']).upper() for c in modes['coefficients']]
    M=modes['modes'];K=nominal['canonical_nominal_low_cutoff']
    if len(potential)!=M+1 or M<=2*K or G<=2*(M+K):
        raise ValueError('canonical degrees or finite multiplication range are insufficient')
    q0=decode(nominal['nominal_frequency_dyadic']);L=arb(2048)
    A=lambda n: arb(1) if n==0 else 1/(4*q0*abs(n))
    T=lambda n: 1/max(L,arb(1) if n==0 else 4*q0*abs(n))
    ds=[A(k)-T(k) for k in range(K+1)]
    kappas=[5050*(A(k)**2-T(k)**2) for k in range(K+1)]
    delta=ds[0]
    for k in range(K+1):
        if not ds[k]>0 or not kappas[k]>0:
            raise ValueError('unexpected nominal low support')
    if not 4*q0*(K+1)>=L:
        raise ValueError('nominal low support is incomplete')
    yc=[decode(c) for c in fit['fields']['Y_prime']['nonnegative_cosine_DFT_coefficients']]
    yy=evaluate_cosine(yc,Q);angles=evaluate_angle(yc,q0,Q)
    hp=[1+q0*(v-yc[0]) for v in yy]
    if any(not v>0 for v in hp):raise ValueError('positive nominal half-density is unresolved')
    sqrt_hp=[v.sqrt() for v in hp]
    half_density=array_box(sqrt_hp)
    unit_roots=[acb(0,4*v).exp() for v in angles]
    powers=[acb(1) for _ in angles]
    R=arb.pi()/(4*G)*(1+arb(2)**(-30))
    nearest=[];offset=[]
    for angle in angles:
        j=int(round(float((angle*2*G/arb.pi()).mid())))
        z=(angle-arb.pi()*j/(2*G))/R
        if not abs(z)<1:raise ValueError('nearest-grid Taylor evaluation does not cover its node')
        nearest.append(j%G);offset.append(z)
    nearest=np.asarray(nearest,dtype=np.int64);offset_box=array_box(offset)
    S=arb(fit['exact_physical_strip'])
    Hp=stored(nominal['nominal_Hprime_complex_modulus']).upper()
    HI=stored(nominal['nominal_H_imaginary_modulus']).upper()
    fmax=M+K
    exp_H=[(4*n*HI).exp().upper() for n in range(fmax+1)]
    remainders=[((4*n*R).exp()*(4*n*R)**(J+1)/math.factorial(J+1)).upper()
                for n in range(fmax+1)]
    t_values=[T(n) for n in range(-fmax,fmax+1)]
    frequencies=np.arange(-fmax,fmax+1,dtype=np.int64)
    phase_derivative=CBox(0,Box(4*frequencies)*arb_box(R))
    # Exact finite polynomial coefficient derivatives are enclosed once for
    # every frequency, then reused in all 53 canonical columns.
    derivative_factors=[CBox(np.ones(len(frequencies)))]
    for j in range(1,J+1):derivative_factors.append(derivative_factors[-1]*phase_derivative/j)
    fft=DirectedFFT();a.out_dir.mkdir(parents=True,exist_ok=True)
    manifest=dict(kind='complete_actual_root_shear_finite_physical_reference',complete=False,
        source_sha256=sha(__file__),bits=a.bits,modes_report_path=str(a.modes_report),
        modes_report_sha256=sha(a.modes_report),nominal_sha256=modes['nominal_sha256'],
        physical_tail_path=str(a.physical_tail),physical_tail_sha256=sha(a.physical_tail),
        identity=nominal['identity'],physical_grid=Q,physical_cutoff=N,canonical_grid=G,
        canonical_potential_cutoff=M,canonical_low_cutoff=K,taylor_order=J,
        exact_nominal_frequency=nominal['nominal_frequency_dyadic'],
        dependencies={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_box.py',
             'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py',
             'fourfold_phase_root_fourier_fit.py','fourfold_phase_nominal_potential_modes.py')},
        columns=[],negative_column_rule='column(-k,n)=column(k,-n)',
        exact_matrix='B diag(kappa) B* + B diag(d) C* + C diag(d) B* + B diag(d) WLL diag(d) B*',
        WLL='real symmetric Toeplitz: WLL[i,j]=stored exact binary64 nu_mid[abs(i-j)]',
        finite_matrix_is_geometry_definition=False)
    report_path=a.out_dir/'manifest.json'
    save(report_path,manifest)
    Berr=[];Cerr=[]
    for k in range(K+1):
        coefficients=[arb(0) for _ in frequencies]
        for m in range(-M,M+1):coefficients[m+k+fmax]=potential[abs(m)]*t_values[m+k+fmax]
        coefficient_box=array_box(coefficients)
        data=zeros((G,J+1))
        for j,factor in enumerate(derivative_factors):
            data[frequencies%G,j]=CBox(coefficient_box)*factor
        derivatives=fft.fft(data,inverse=True)*G
        value=zeros(Q)
        for j in range(J,-1,-1):value=value*offset_box+derivatives[nearest,j]
        remainder=sum((abs(c)*remainders[abs(int(n))] for n,c in zip(frequencies,coefficients)),arb(0)).upper()
        Cnodes=value.pad(arb_box(remainder))*half_density
        Bnodes=CBox(array_box([p.real*s for p,s in zip(powers,sqrt_hp)]),
                    array_box([p.imag*s for p,s in zip(powers,sqrt_hp)]))
        Bmodulus=(Hp.sqrt()*exp_H[k]).upper()
        Cmodulus=(Hp.sqrt()*sum((abs(c)*exp_H[abs(int(n))]
                       for n,c in zip(frequencies,coefficients)),arb(0))).upper()
        b,budget_b=midpoint_dft(Bnodes,N,Bmodulus,S)
        c,budget_c=midpoint_dft(Cnodes,N,Cmodulus,S)
        Berr.append(stored(budget_b['projected_column_L2_error']).upper())
        Cerr.append(stored(budget_c['projected_column_L2_error']).upper())
        path=a.out_dir/f'column_{k:03d}.npz'
        np.savez_compressed(path,B=b,C=c)
        manifest['columns'].append(dict(k=k,path=str(path),sha256=sha(path),
            physical_modes=[-N,N],format='NPZ real binary64, exact dyadic centers, allow_pickle=False',
            B=budget_b,C=budget_c,finite_Taylor_uniform_remainder=ball_record(remainder),
            finite_B_complex_modulus=ball_record(Bmodulus),finite_C_complex_modulus=ball_record(Cmodulus)))
        manifest.update(wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu)
        save(report_path,manifest)
        print(dict(k=k,requested=K,B_error=str(Berr[-1]),C_error=str(Cerr[-1]),
                   wall_seconds=manifest['wall_seconds']),flush=True)
        powers=[p*z for p,z in zip(powers,unit_roots)]
    mult=lambda k:1 if k==0 else 2
    EB=sum((mult(k)*Berr[k]**2 for k in range(K+1)),arb(0)).sqrt().upper()
    EBK=sum((mult(k)*(kappas[k]*Berr[k])**2 for k in range(K+1)),arb(0)).sqrt().upper()
    EBd=sum((mult(k)*(ds[k]*Berr[k])**2 for k in range(K+1)),arb(0)).sqrt().upper()
    ECd=sum((mult(k)*(ds[k]*Cerr[k])**2 for k in range(K+1)),arb(0)).sqrt().upper()
    Vmid=(abs(potential[0])+2*sum((abs(c) for c in potential[1:]),arb(0))).upper()
    finite_column_error=((2+EB)*EBK+2*(EBd*Vmid/L+(1+EB)*ECd)
                         +EBd*Vmid*(2*delta+EBd)).upper()
    coefficient_square=arb(0)
    for k in range(K+1):
        coefficient_square+=mult(k)*ds[k]**2*sum((T(k+m)**2*rho[abs(m)]**2
                                                  for m in range(-M,M+1)),arb(0))
    low_W_error=(rho[0]+2*sum(rho[1:2*K+1],arb(0))).upper()
    coefficient_error=(2*coefficient_square.sqrt()+delta**2*low_W_error).upper()
    u=stored(nominal['true_canonical_inverse_strip']).lower()
    trueV=stored(nominal['true_residual_potential_complex_modulus']).upper()
    comparison=stored(nominal['true_minus_nominal_canonical_potential_uniform_error']).upper()
    rr=(-4*u).exp()
    true_tail=(arb(2).sqrt()*trueV*rr**(M+1)/(1-rr*rr).sqrt()).upper()
    nominal_tail=(true_tail+comparison).upper()
    tail_square=sum((mult(k)*(ds[k]*nominal_tail/(4*q0*(M+1-k)))**2
                     for k in range(K+1)),arb(0))
    canonical_tail_error=(2*tail_square.sqrt()).upper()
    physical_tail=read(a.physical_tail)
    # Keep this selection explicit: the published R92 supplement is a full
    # actual-family corner-removal estimate, not a nominal projection claim.
    candidates=physical_tail.get('cutoffs',physical_tail.get('physical_cutoffs',[]))
    if isinstance(candidates,dict):candidates=list(candidates.values())
    rows=[r for r in candidates if r.get('physical_fourfold_cutoff')==N]
    if len(rows)!=1:
        raise ValueError('one complete actual physical tail at the exact cutoff is required')
    tailrow=rows[0]
    if not physical_tail['proved']:
        raise ValueError('actual physical tail certificate is not proved')
    actual_tail=stored(tailrow['full_shear_finite_corner_L2_error_upper']).upper()
    geometry=stored(nominal['complete_actual_minus_nominal_shear_operator_error']).upper()
    total=(actual_tail+geometry+coefficient_error+canonical_tail_error+finite_column_error).upper()
    manifest.update(complete=True,full_error_budget=dict(
        actual_family_physical_corner_removal=ball_record(actual_tail),
        full_actual_to_nominal_operator_error=ball_record(geometry),
        canonical_finite_coefficient_error=ball_record(coefficient_error),
        complete_canonical_tail_error=ball_record(canonical_tail_error),
        finite_physical_column_error=ball_record(finite_column_error),
        actual_shear_minus_exact_finite_physical_reference=ball_record(total)),
        norms=dict(B_column_error_HS=ball_record(EB),B_kappa_error_HS=ball_record(EBK),
                   B_d_error_HS=ball_record(EBd),C_d_error_HS=ball_record(ECd),
                   exact_finite_potential_Wiener_modulus=ball_record(Vmid),
                   true_canonical_potential_L2_tail=ball_record(true_tail),
                   nominal_canonical_potential_L2_tail=ball_record(nominal_tail)),
        wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu,
        scope=['Full actual narrow parameter family, both angular unitaries, mean and all low/high cross terms.',
               'Physical projection is applied to the actual operator before comparison, using the complete R92 bound.',
               'This is the root shear only; other frame operators and the full strong feedback Schur inverse remain separate.'])
    save(report_path,manifest)
    print(dict(complete=True,full_error=manifest['full_error_budget'],
               wall_seconds=manifest['wall_seconds']),flush=True)


if __name__=='__main__':main()
