#!/usr/bin/env python3
"""Complete physical v1 Fourier enclosure from the original actual root grid."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grid',type=Path,default=Path('data/root_finite_grid/grid4096_h1e9/manifest.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits
    grid=read(a.grid)
    if not grid['complete'] or sha(grid['worker_path'])!=grid['worker_sha256']:
        raise ValueError('actual root grid or source changed')
    rows=[]
    for entry in grid['chunks']:
        if sha(entry['path'])!=entry['sha256']:raise ValueError('actual grid shard changed')
        doc=read(entry['path'])
        if not doc['complete'] or doc['identity']!=grid['identity']['identity']:
            raise ValueError('actual root grid is incomplete or belongs to another family')
        for name,digest in doc['dependencies'].items():
            if sha(Path('scripts')/name)!=digest:raise ValueError('actual grid dependency changed: '+name)
        rows.extend(doc['rows'])
    N=grid['grid'];K=N//2
    if [r['index'] for r in rows]!=list(range(K+1)):raise ValueError('half-grid gap or duplicate')
    outer_path=Path(doc['complex_root_path'])
    if sha(outer_path)!=doc['complex_root_sha256']:raise ValueError('outer root source changed')
    outer=read(outer_path)
    if not outer['proved'] or outer['pending'] or outer['failed_cells']:
        raise ValueError('actual complete complex strip is missing')
    identity=grid['identity']['identity'];oi=outer['object']
    for k in ('origin_inputs_sha256','direction_sha256'):
        if identity[k]!=oi[k]:raise ValueError('different underlying exact object')
    l,r=map(Fraction,identity['exact_parameter_interval'])
    ol,orr=map(Fraction,oi['exact_parameter_interval'])
    if not ol<=l<=r<=orr:raise ValueError('outer parameter box does not cover actual root family')
    S=arb(outer['exact_physical_angle_strip'])
    M=stored(outer['uniform_bounds']['v1_complex_modulus_upper']).upper()
    half=[stored(row['V_xi_root']) for row in rows]
    vals=half+list(reversed(half[1:-1]));mid=[v.mid() for v in vals]
    radii=[abs(v-c).upper() for v,c in zip(vals,mid)]
    node_rms=(sum((e*e for e in radii),arb(0))/N).sqrt().upper()
    node_max=max(radii);transformed=[z/N for z in acb.dft([acb(v) for v in mid])]
    coeff=np.empty(K+1);rounding=[]
    for n in range(K+1):
        z=transformed[n]
        if not z.imag.contains(0):raise ValueError('exact even DFT lost real axis')
        v=z.real if n in (0,K) else z.real.intersection(transformed[-n].real)
        c=float(v.mid());coeff[n]=c;rounding.append(abs(v-arb(c)).upper())
    r=(-4*S).exp();alias=(4*M*r**K/(1-r)).upper()
    round1=(rounding[0]+2*sum(rounding[1:K],arb(0))+rounding[K]).upper()
    round2=(rounding[0]**2+2*sum((e*e for e in rounding[1:K]),arb(0))+rounding[K]**2/2).sqrt().upper()
    lebesgue=1+4/arb.pi()*(1+arb(N-1).log()/2)
    err2=(node_rms+alias+round2).upper()
    errinf=(lebesgue*node_max+alias+round1).upper()
    cp=a.out.with_suffix('.npz');cp.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(cp,v1=coeff)
    report=dict(kind='actual_physical_v1_full_Fourier_enclosure',proved=True,
        source_path=str(Path(__file__).relative_to(Path.cwd())),source_sha256=sha(__file__),bits=a.bits,
        identity=identity,grid_path=str(a.grid),grid_sha256=sha(a.grid),
        original_v1_complex_path=str(outer_path),original_v1_complex_sha256=sha(outer_path),
        exact_physical_strip=outer['exact_physical_angle_strip'],physical_grid=N,
        coefficient_path=str(cp),coefficient_sha256=sha(cp),
        coefficient_representation='P=c0+2*sum(c_n*cos(4n theta),1<=n<K)+c_K*cos(4K theta); exact binary64 dyadics',
        even_reflection_from_exact_original_geometry=True,mean_retained=True,
        complete_original_infinite_primitive_error_retained=True,
        fields={'v1':dict(complete_complex_modulus=ball_record(M),
            discrete_nodal_RMS_error=ball_record(node_rms),maximum_nodal_ball_error=ball_record(node_max),
            full_analytic_alias_error=ball_record(alias),finite_DFT_L1_rounding=ball_record(round1),
            finite_DFT_L2_rounding=ball_record(round2),real_L2_error=ball_record(err2),
            real_uniform_error=ball_record(errinf))},
        dependencies={name:sha(Path('scripts')/name) for name in
            ('fourfold_phase_beta_interval.py','fourfold_phase_root_fourier_fit.py')})
    save(a.out,report)
    print(dict(proved=True,sha256=sha(a.out),physical_L2_upper=str(err2),physical_uniform_upper=str(errinf)),flush=True)


if __name__=='__main__':main()
