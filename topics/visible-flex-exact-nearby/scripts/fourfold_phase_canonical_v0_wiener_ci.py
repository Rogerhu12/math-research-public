#!/usr/bin/env python3
"""Actual canonical v0 Wiener moments from the exact physical residual fit.

The 5050 constant is added only to the canonical zero coefficient, with
its conversion roundoff paid. All actual geometry, inverse-angle, nodal,
DFT, alias and infinite analytic tail errors remain present.
"""
from __future__ import annotations
import argparse,math,time
from pathlib import Path
import numpy as np
from flint import acb,arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_box import CBox,DirectedFFT,arb_box,zeros
from fourfold_phase_root_interval import Box,stack
from fourfold_phase_root_fourier_fit import read,save,sha,stored,decode


def array_box(values):
    return stack([arb_box(v) for v in values])


def geometric_moments(r,maximum):
    st=[[0]*(maximum+1) for _ in range(maximum+1)];st[0][0]=1
    for p in range(1,maximum+1):
        for j in range(1,p+1):st[p][j]=st[p-1][j-1]+j*st[p-1][j]
    return [sum((st[p][j]*math.factorial(j)*r**j/(1-r)**(j+1)
                 for j in range(p+1)),arb(0)) for p in range(maximum+1)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--nominal',type=Path,default=Path('notes/2026-11-12-actual-to-nominal-root-shear.json'))
    p.add_argument('--physical-grid',type=int,default=16384)
    p.add_argument('--canonical-grid',type=int,default=16384)
    p.add_argument('--modes',type=int,default=4096)
    p.add_argument('--taylor-order',type=int,default=16)
    p.add_argument('--high-cutoffs',type=int,nargs='+',default=[16,32,52,64,96,128,192,256,512])
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits;wall=time.monotonic()
    nominal=read(a.nominal);fit=read(nominal['fit_path'])
    if (not nominal['proved'] or not fit['proved']
        or sha(nominal['fit_path'])!=nominal['fit_sha256']
        or fit['identity']!=nominal['identity']):
        raise ValueError('incomplete, changed, or different actual root family')
    if (sha('scripts/fourfold_phase_root_fourier_fit.py')!=fit['source_sha256']
        or sha('scripts/fourfold_phase_nominal_root_shear.py')!=nominal['source_sha256']):
        raise ValueError('defining proof source changed')
    physical_fit=fit['fields']['residual_v0']
    physical_error=(stored(physical_fit['discrete_nodal_RMS_error']).upper()
        +stored(physical_fit['complete_real_interpolation_alias']).upper()
        +stored(physical_fit['finite_DFT_rounding_L2']).upper()).upper()
    reference=arb(5050)
    G,Q,M,J=a.physical_grid,a.canonical_grid,a.modes,a.taylor_order
    vc=[decode(v) for v in physical_fit['nonnegative_cosine_DFT_coefficients']]
    yc=[decode(v) for v in fit['fields']['Y_prime']['nonnegative_cosine_DFT_coefficients']]
    K=len(vc)-1;q0=decode(nominal['nominal_frequency_dyadic'])
    if (len(yc)!=K+1 or G<=2*K or Q<=2*M or G&(G-1) or Q&(Q-1)
        or J<1 or M<512 or any(k<1 for k in a.high_cutoffs)):
        raise ValueError('incompatible exact polynomial or grid degrees')
    frequencies=np.arange(-K,K+1,dtype=np.int64);hp=[];vv=[];phi=[]
    for n in frequencies:
        n=int(n);k=abs(n)
        hv=arb(1) if n==0 else q0*yc[k]/(2 if k==K else 1)
        v=vc[k]/(2 if k==K else 1)
        hp.append(hv);vv.append(v);phi.append(acb(0) if n==0 else acb(0,-hv/(4*n)))
    R=arb.pi()/(4*G)*(1+arb(2)**(-24));radius=arb_box(R);pi_box=arb_box(arb.pi())
    coefficient=CBox(stack([array_box([z.real for z in phi]),array_box(hp),array_box(vv)],axis=1),
        stack([array_box([z.imag for z in phi]),Box(np.zeros(2*K+1)),Box(np.zeros(2*K+1))],axis=1))
    factors=CBox(np.ones(2*K+1));d=CBox(0,Box(4*frequencies)*radius)
    data=zeros((G,J+1,3))
    for j in range(J+1):
        data[frequencies%G,j,:]=coefficient*factors.reshape(-1,1);factors=factors*d/(j+1)
    derivatives=DirectedFFT().fft(data,inverse=True)*G;del data,coefficient
    remainders=[]
    for field in (phi,[acb(v) for v in hp],[acb(v) for v in vv]):
        remainders.append(sum((abs(c)*(4*abs(int(n))*R).exp()
            *(4*abs(int(n))*R)**(J+1)/math.factorial(J+1)
            for n,c in zip(frequencies,field)),arb(0)).upper())
    pad=array_box(remainders)
    derivative_v=sum((4*abs(int(n))*abs(c) for n,c in zip(frequencies,vv)),arb(0)).upper()

    def evaluate(theta):
        nearest=np.rint(theta*(2*G/math.pi)).astype(np.int64)
        offset=(Box(theta)-pi_box*Box(nearest)/(2*G))/radius
        if np.any(offset.abs_upper()>1):raise ValueError('Taylor cell misses exact dyadic point')
        value=zeros((len(theta),3))
        for j in range(J,-1,-1):value=value*offset.reshape(-1,1)+derivatives[nearest%G,j,:]
        value=value.pad(pad)
        if np.any(value.imag.lo>0) or np.any(value.imag.hi<0):
            raise ValueError('exact real finite polynomial lost real axis')
        return value.real

    exact_psi=[arb.pi()*j/(2*Q) for j in range(Q//2+1)]
    psi=array_box(exact_psi);psi_mid=np.asarray([float(v.mid()) for v in exact_psi])
    theta=psi_mid.copy()
    for iteration in range(10):
        v=evaluate(theta)
        theta=theta-(theta+v.lo[:,0]/2+v.hi[:,0]/2-psi_mid)/(v.lo[:,1]/2+v.hi[:,1]/2)
    value=evaluate(theta);residual=Box(theta)+value[:,0]-psi
    m0=stored(nominal['nominal_map_derivative_real_lower']).lower()
    inverse_error=Box(residual.abs_upper())/arb_box(m0)
    fee=(inverse_error*arb_box(derivative_v)).hi;nodes=value[:,2]+Box(-fee,fee)
    lo=np.concatenate([nodes.lo,nodes.lo[-2:0:-1]])
    hi=np.concatenate([nodes.hi,nodes.hi[-2:0:-1]])
    centers=lo/2+hi/2;rms=arb(0)
    for l,h,c in zip(lo,hi,centers):
        e=max(abs(arb(float(l))-arb(float(c))),abs(arb(float(h))-arb(float(c))))
        rms+=e*e
    rms=(rms/Q).sqrt().upper()
    print(dict(stage='certified_nominal_inverse_grid',nodes=Q,node_RMS=str(rms),
        inverse_residual=float(np.max(residual.abs_upper())),wall=time.monotonic()-wall),flush=True)
    del derivatives
    transformed=[z/Q for z in acb.dft([acb(float(c)) for c in centers])]
    S=arb(fit['exact_physical_strip'])
    u0=(arb(7)/8*stored(nominal['nominal_Hprime_complex_real_lower']).lower()*S).lower()
    nominal_modulus=sum((abs(c)*(4*abs(int(n))*S).cosh() for n,c in zip(frequencies,vv)),arb(0)).upper()
    denominator=1-(-4*u0*Q).exp();coeff=np.empty(M+1);round_square=alias_square=arb(0)
    for n in range(M+1):
        z=transformed[n]
        if not z.imag.contains(0):raise ValueError('even nominal DFT lost real Fourier symmetry')
        v=z.real if n==0 else z.real.intersection(transformed[-n].real)
        if n==0:v+=reference
        c=float(v.mid());coeff[n]=c;mult=1 if n==0 else 2
        round_square+=mult*abs(v-arb(c)).upper()**2
        alias=nominal_modulus*((-4*u0*(Q-n)).exp()+(-4*u0*(Q+n)).exp())/denominator
        alias_square+=mult*alias*alias
    rounding=round_square.sqrt().upper();aliases=alias_square.sqrt().upper()
    coefficient_error=(rms+rounding+aliases).upper()
    mtrue=stored(fit['true_Hprime_complex_real_lower']).lower()
    Mtrue=stored(fit['true_Hprime_complex_modulus_upper']).upper()
    Herror=stored(nominal['true_map_real_error']).upper()
    comparison=(Mtrue.sqrt()*physical_error+derivative_v*Herror/mtrue).upper()
    total_error=(comparison+coefficient_error).upper()
    u=stored(nominal['true_canonical_inverse_strip']).lower()
    actual_modulus=stored(physical_fit['complete_outer_strip_modulus']).upper()
    r=(-4*u).exp();moments=geometric_moments(r,5)
    splits=sorted(set(j for j in (128,256,384,512,768,1024,1280,1536,1792,2048,2304,2560,2816,3072,3328,3584,3840,M) if j<=M))
    partial={};finite=[arb(0)]*6;squares=[0]*11
    for n in range(M+1):
        mult=1 if n==0 else 2
        for j in range(6):finite[j]+=mult*abs(arb(float(coeff[n])))*n**j
        for j in range(11):squares[j]+=mult*n**j
        if n in splits:
            N=n+1
            tails=[(r**N*sum((math.comb(p,j)*N**(p-j)*moments[j] for j in range(p+1)),arb(0))).upper() for p in range(6)]
            partial[n]=(finite.copy(),squares.copy(),tails)
    budgets=[];qlo=stored(nominal['true_frequency']).lower()
    for cutoff in a.high_cutoffs:
        denominator=arb(cutoff+1)
        for order in range(5):
            for moment in (0,1):
                candidates=[]
                for split,(sums,powers,tails) in partial.items():
                    finite=sum((math.comb(order,j)*sums[j+moment]/denominator**j for j in range(order+1)),arb(0))
                    l2weight=sum((math.comb(2*order,j)*arb(powers[j+2*moment])/denominator**j for j in range(2*order+1)),arb(0)).sqrt()
                    tail=2*actual_modulus*sum((math.comb(order,j)*tails[j+moment]/denominator**j for j in range(order+1)),arb(0))
                    error=(l2weight*total_error).upper();total=(finite+error+tail).upper()
                    candidates.append((total,dict(split=split,
                        finite_reference_sum=ball_record(finite.upper()),
                        complete_low_coefficient_L2_fee=ball_record(error.upper()),
                        complete_true_analytic_tail=ball_record(tail.upper()),
                        true_scaled_Wiener_upper=ball_record(total))))
                _,best=min(candidates,key=lambda row:float(row[0]))
                row=dict(high_cutoff=cutoff,weight_order=order,moment=moment,**best)
                if moment==0:
                    row['P_Hs_operator_upper_for_abs_s_le_order']=ball_record((stored(best['true_scaled_Wiener_upper']).upper()/(4*qlo*(cutoff+1))**2).upper())
                budgets.append(row)
                print(dict(K=cutoff,a=order,moment=moment,split=best['split'],
                    upper=best['true_scaled_Wiener_upper']['upper']),flush=True)
    cp=a.out.with_suffix('.npz');np.savez_compressed(cp,nominal_v0_nonnegative=coeff)
    report=dict(kind='actual_canonical_v0_scaled_Wiener_enclosure',proved=True,
        source_path='scripts/'+Path(__file__).name,source_sha256=sha(__file__),bits=a.bits,
        physical_residual_fit_path=nominal['fit_path'],physical_residual_fit_sha256=nominal['fit_sha256'],
        nominal_path=str(a.nominal),nominal_sha256=sha(a.nominal),
        fit_path=nominal['fit_path'],fit_sha256=nominal['fit_sha256'],identity=fit['identity']['identity'],
        physical_grid=G,canonical_grid=Q,canonical_projection_cutoff=M,finite_Taylor_order=J,
        coefficient_path=str(cp),coefficient_sha256=sha(cp),
        coefficient_convention='exact binary64 nominal canonical v0 midpoints; NOT actual geometry',
        norm='sum_l |(v0)_hat(l)| |l|^moment (1+|l|/(K+1))^a; moment0 includes mean',
        exact_nominal_angle='H0=theta+q0 I(P_Yprime), mean-zero I and exact dyadic q0',
        exact_reference_constant=5050,actual_physical_residual_L2_error=ball_record(physical_error),
        actual_full_v0_complex_modulus=ball_record(actual_modulus+reference),
        nominal_physical_v0_derivative_modulus=ball_record(derivative_v),
        complete_finite_Taylor_remainders={n:ball_record(v) for n,v in zip(('H0_minus_theta','H0_prime','P_v0'),remainders)},
        maximum_nominal_inverse_angle_error=ball_record(arb(float(np.max(inverse_error.hi)))),
        nominal_inverse_strip=ball_record(u0),nominal_residual_v0_complex_modulus=ball_record(nominal_modulus),
        nominal_node_discrete_RMS_error=ball_record(rms),nominal_DFT_L2_rounding=ball_record(rounding),
        nominal_complete_alias_L2=ball_record(aliases),nominal_projected_coefficient_L2_error=ball_record(coefficient_error),
        actual_to_nominal_canonical_L2_error=ball_record(comparison),
        actual_projected_coefficient_L2_error=ball_record(total_error),
        actual_canonical_inverse_strip=ball_record(u),actual_residual_v0_complex_modulus=ball_record(actual_modulus),
        low_coefficient_fee='Cauchy-Schwarz: complete actual-to-nominal L2 plus nodal, DFT, aliases',
        full_tail_fee='binomial/Stirling sums of actual analytic tails, every |l|>split',
        high_shear_operator_definition='P=P_>K Gamma^-1 M_v0 Gamma^-1 P_>K, Gamma_n=4q|n|',
        budgets=budgets,wall_seconds=time.monotonic()-wall,full_strong_inverse_claimed=False,
        dependencies={name:sha(Path('scripts')/name) for name in
            ('fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_box.py','fourfold_phase_root_interval.py',
             'fourfold_phase_uniform_tail.py','fourfold_phase_root_fourier_fit.py')})
    save(a.out,report)
    small=dict(kind='small_exact_extraction_from_complete_canonical_v0_report',proved=True,
        report_path=str(a.out),report_sha256=sha(a.out),source_sha256=sha(__file__),
        coefficient_sha256=report['coefficient_sha256'],identity=fit['identity']['identity'],
        actual_to_nominal_canonical_L2_upper=comparison.str(40),
        actual_projected_coefficient_L2_upper=total_error.str(40),
        true_frequency=nominal['true_frequency'],actual_canonical_inverse_strip=ball_record(u),
        actual_residual_v0_complex_modulus=ball_record(actual_modulus),budgets=[])
    for row in budgets:
        small['budgets'].append({key:(value['upper'] if isinstance(value,dict) else value) for key,value in row.items()})
    save(a.out.with_name(a.out.stem+'-summary.json'),small)
    print(dict(proved=True,sha256=sha(a.out),wall=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
