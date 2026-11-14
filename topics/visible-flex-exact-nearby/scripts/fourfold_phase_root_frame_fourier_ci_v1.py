#!/usr/bin/env python3
"""Complete physical Wiener enclosures of the actual root Cauchy frame and v1."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored


def grid_rows(path):
    grid=read(path)
    if not grid['complete'] or sha(grid['worker_path'])!=grid['worker_sha256']:
        raise ValueError('actual grid incomplete or source changed')
    rows=[]
    for entry in grid['chunks']:
        if sha(entry['path'])!=entry['sha256']:raise ValueError('actual node shard changed')
        shard=read(entry['path'])
        if not shard['complete'] or shard['identity']!=grid['identity']['identity']:
            raise ValueError('different or incomplete actual node shard')
        for name,digest in shard['dependencies'].items():
            if sha(Path('scripts')/name)!=digest:raise ValueError('actual grid source changed: '+name)
        rows.extend(shard['rows'])
    if [r['index'] for r in rows]!=list(range(grid['grid']//2+1)):raise ValueError('grid has gap or duplicate')
    return grid,rows


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grid',type=Path,default=Path('data/root_finite_grid/ci_cauchy_frame_grid4096_h1e9/manifest.json'))
    p.add_argument('--complex-frame',type=Path,default=Path('notes/2026-11-12-ci-actual-root-Cauchy-frame-complex.json.gz'))
    p.add_argument('--original-grid',type=Path,default=Path('data/root_finite_grid/grid4096_h1e9/manifest.json'))
    p.add_argument('--original-complex',type=Path,default=Path('notes/2026-11-12-actual-root-complex-potential-variation.json.gz'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--cutoffs',type=int,nargs='+',default=[0,4,8,16,32,64,128,256,512,1024,2048])
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=a.bits
    grid,rows=grid_rows(a.grid);old,oldrows=grid_rows(a.original_grid)
    outer=read(a.complex_frame);oldouter=read(a.original_complex)
    if (not outer['proved'] or not outer['complete'] or outer['failed'] or outer['pending']
        or not oldouter['proved'] or oldouter['pending'] or oldouter['failed_cells']):
        raise ValueError('complete true outer strip missing')
    if (grid['identity']['identity']!=old['identity']['identity']
        or grid['identity']['identity']!=outer['identity'] or grid['grid']!=old['grid']):
        raise ValueError('frame and original v1 grid differ in actual family or grid')
    interval=list(map(Fraction,outer['identity']['exact_parameter_interval']))
    oi=list(map(Fraction,oldouter['object']['exact_parameter_interval']))
    if not oi[0]<=interval[0]<=interval[1]<=oi[1]:raise ValueError('outer v1 parameter box does not cover frame')
    for key in ('origin_inputs_sha256','direction_sha256'):
        if outer['identity'][key]!=oldouter['object'][key]:raise ValueError('different original object')
    S=arb(outer['exact_physical_strip'])
    if S!=arb(oldouter['exact_physical_angle_strip']):raise ValueError('outer strips differ')
    N=grid['grid'];K=N//2;r=(-4*S).exp();lebesgue=1+4/arb.pi()*(1+arb(N-1).log()/2)
    orders=[Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(1)]
    inputs={name:([stored(row[name]) for row in rows],stored(modulus).upper()) for name,modulus in outer['uniform_moduli'].items()}
    inputs['v1']=([stored(row['V_xi_root']) for row in oldrows],stored(oldouter['uniform_bounds']['v1_complex_modulus_upper']).upper())
    report=dict(kind='actual_full_root_Cauchy_frame_physical_Wiener_coefficients',proved=False,
        source_path='scripts/'+Path(__file__).name,source_sha256=sha(__file__),bits=a.bits,
        grid_path=str(a.grid),grid_sha256=sha(a.grid),complex_frame_path=str(a.complex_frame),complex_frame_sha256=sha(a.complex_frame),
        original_v1_grid_path=str(a.original_grid),original_v1_grid_sha256=sha(a.original_grid),
        original_v1_complex_path=str(a.original_complex),original_v1_complex_sha256=sha(a.original_complex),
        identity=outer['identity'],physical_grid=N,exact_physical_strip=outer['exact_physical_strip'],
        exact_even_physical_fields=True,physical_Piola_term_retained=True,root_mean_retained=True,
        coefficient_representation='P=c0+2*sum(c_n*cos(4n theta),1<=n<K)+c_K*cos(4K theta); NPZ exact binary64 dyadics',
        norm_definition='A_s=sum_n (1+4|n|)^s |fhat_n|, normalized physical Fourier',
        exact_Cauchy_matrix='[[h,0],[s,-c]], determinant=-Yprime, physical radial momentum',
        dependencies={name:sha(Path('scripts')/name) for name in ('fourfold_phase_beta_interval.py','fourfold_phase_root_fourier_fit.py')},
        fields={})
    arrays={}
    for name,(half,modulus) in inputs.items():
        values=half+list(reversed(half[1:-1]));middle=[v.mid() for v in values]
        radii=[abs(v-c).upper() for v,c in zip(values,middle)]
        node_rms=(sum((e*e for e in radii),arb(0))/N).sqrt().upper();node_max=max(radii)
        transformed=[z/N for z in acb.dft([acb(v) for v in middle])]
        coeff=[];rounding=[];array=np.empty(K+1)
        for n in range(K+1):
            z=transformed[n]
            if not z.imag.contains(0):raise ValueError('even midpoint DFT lost its real axis')
            value=z.real
            if 0<n<K:value=value.intersection(transformed[-n].real)
            c=float(value.mid());array[n]=c;coeff.append(arb(c));rounding.append(abs(value-arb(c)).upper())
        arrays[name]=array;budgets={}
        rounding_l2=(rounding[0]**2+2*sum((e*e for e in rounding[1:K]),arb(0))+rounding[K]**2/2).sqrt().upper()
        for order in orders:
            s=arb(order.numerator)/order.denominator
            weights=[(1+4*arb(n))**s for n in range(K+1)]
            finite=(abs(coeff[0])+2*sum((weights[n]*abs(coeff[n]) for n in range(1,K)),arb(0))+weights[K]*abs(coeff[K])).upper()
            rounding_fee=(rounding[0]+2*sum((weights[n]*rounding[n] for n in range(1,K)),arb(0))+weights[K]*rounding[K]).upper()
            aa=1+4*arb(K)
            alias=(4*modulus*r**K*(aa**s/(1-r)+4*s*aa**(s-1)*r/(1-r)**2)).upper()
            node_fee=(weights[K]*arb(N).sqrt()*node_rms).upper()
            error=(node_fee+rounding_fee+alias).upper();tails=[]
            for cutoff in a.cutoffs:
                if cutoff<0 or cutoff>K:raise ValueError('unsupported tail cutoff')
                retained=(2*sum((weights[n]*abs(coeff[n]) for n in range(max(1,cutoff+1),K)),arb(0))
                    +(weights[K]*abs(coeff[K]) if K>cutoff else 0))
                tails.append(dict(physical_fourfold_cutoff=cutoff,true_tail_upper=ball_record((retained+error).upper()),
                    true_tail_lower=ball_record(max(arb(0),(retained-error).lower()))))
            budgets[str(order)]=dict(exact_finite_polynomial_norm_upper=ball_record(finite),
                nodal_error=ball_record(node_fee),finite_DFT_rounding=ball_record(rounding_fee),
                complete_analytic_tail_and_alias=ball_record(alias),complete_actual_minus_finite_polynomial_error=ball_record(error),
                actual_full_norm_upper=ball_record((finite+error).upper()),tails=tails)
        e0=stored(budgets['0']['complete_analytic_tail_and_alias']).upper()
        real_error=(lebesgue*node_max+e0+stored(budgets['0']['finite_DFT_rounding']).upper()).upper()
        finite_norm=stored(budgets['0']['exact_finite_polynomial_norm_upper']).upper()
        nonconstant=finite_norm-abs(coeff[0]);real_modulus=min(modulus,(finite_norm+real_error).upper())
        report['fields'][name]=dict(complete_complex_modulus=ball_record(modulus),true_real_modulus_upper=ball_record(real_modulus),
            true_real_range=ball_record(coeff[0]+arb(0,(nonconstant+real_error).upper())),
            discrete_nodal_RMS_error=ball_record(node_rms),maximum_nodal_ball_error=ball_record(node_max),
            finite_DFT_L2_rounding=ball_record(rounding_l2),real_L2_error=ball_record((node_rms+e0+rounding_l2).upper()),
            real_uniform_error=ball_record(real_error),Wiener_budgets=budgets)
        print(dict(field=name,A0_error=str(stored(budgets['0']['complete_actual_minus_finite_polynomial_error'])),
            real_modulus=str(real_modulus)),flush=True)
    cp=a.out.with_name(a.out.name.removesuffix('.json.gz').removesuffix('.json')+'.npz')
    np.savez_compressed(cp,**arrays)
    report.update(proved=True,coefficient_path=str(cp),coefficient_sha256=sha(cp),full_strong_inverse_claimed=False)
    save(a.out,report)
    small=dict(kind='small_exact_extraction_of_actual_frame_bounds',proved=True,report_path=str(a.out),report_sha256=sha(a.out),
        identity=outer['identity'],coefficient_sha256=sha(cp),exact_Cauchy_matrix=report['exact_Cauchy_matrix'],fields={})
    for name,v in report['fields'].items():
        small['fields'][name]=dict(complex_modulus=v['complete_complex_modulus']['upper'],
            real_L2_error=v['real_L2_error']['upper'],real_uniform_error=v['real_uniform_error']['upper'],
            Wiener={s:dict(norm=b['actual_full_norm_upper']['upper'],error=b['complete_actual_minus_finite_polynomial_error']['upper'])
                    for s,b in v['Wiener_budgets'].items()})
    sp=a.out.with_name(a.out.name.removesuffix('.json.gz').removesuffix('.json')+'-summary.json');save(sp,small)
    print(dict(proved=True,fields=len(inputs),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
