#!/usr/bin/env python3
"""Full A0 nonlinear derivative bounds using the actual relative finite centre.

Only the centre is finite. The Frechet bounds act on arbitrary full Fourier
corrections in the absolute pair X0 norm. No residual or existence is supplied.
"""
from __future__ import annotations
import argparse,gzip,json
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_cap_centered_residual_v3 import polynomials,total
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_box import arb_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-r09-linear-kernels-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,2000))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve all relative-centre attempts')
    native,kernels=read(args.native),read(args.kernels)
    if (not native['complete'] or not native['cap_linear_reference_certified']
        or not kernels['complete'] or not kernels['unweighted_nonzero_rates_positive']
        or not kernels['backward_mean_rates_positive'] or kernels['input_sha256']!=sha(args.native)
        or kernels['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_A0_translation_budget.py'))):
        raise ValueError('the complete actual target and full Green kernel are required')
    for doc in (native,kernels):
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('true target scope changed')
        for name,h in doc.get('dependencies',doc.get('dependency_sha256',{})).items():
            if sha(Path(__file__).with_name(name))!=h:raise ValueError('dependency changed: '+name)
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if native[key]!=kernels[key]:raise ValueError('target identity changed')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=native['object_sha256'] or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('wrong complete centre')
    left,right=map(Fraction,kernels['exact_requested_interval'])
    if left<Fraction(18,100):raise ValueError('compact metric has not returned to the original target')
    nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
    alpha=arb_box(exact_arb(Fraction.from_float(float(meta['amplitude']))))
    ba=np.zeros(2*m+1);ca=ba.copy();br=ba.copy();cr=ba.copy();cursor=left;rows=[]
    for kr in kernels['rows']:
        nr=native['rows'][kr['native_index']];lo,hi=map(Fraction,kr['interval'])
        nl,nh=map(Fraction,nr['interval']);gl,gh=map(Fraction,nr['actual_scalar_germ'])
        if lo!=cursor or not gl<=nl<=lo<hi<=nh<=gh:raise ValueError('actual closed cover changed')
        Cref=arb_box(box_from_record(nr['coefficients']['Cref']))
        if not np.all(Cref.hi<0):raise ValueError('relative centre denominator unresolved')
        cuts=[lo,*[x for x in nodes if lo<x<hi],hi]
        for ll,rr in zip(cuts[:-1],cuts[1:]):
            piece=min(len(nodes)-2,bisect_right(nodes,ll)-1)
            b,imag,c,*_=polynomials(saved,nodes,piece,ll,rr,alpha,m)
            ba=np.maximum(ba,b.abs_upper());ca=np.maximum(ca,c.abs_upper())
            br=np.maximum(br,(b/Cref).abs_upper());cr=np.maximum(cr,(c/Cref).abs_upper())
            rows.append(dict(native_index=kr['native_index'],centre_piece=piece,interval=list(map(str,(ll,rr))),actual_scalar_germ=nr['actual_scalar_germ']))
        cursor=hi
    if cursor!=right:raise ValueError('relative centre cover is incomplete')
    B,C,Brel,Crel=map(total,(ba,ca,br,cr))
    cc={k:box_from_record(v) for k,v in kernels['constants'].items()}
    Cstar=cc['reference_C_abs_lower'].lower();Lambda=max(arb(1),cc['ell_upper']).upper()
    G=cc['complete_pair_nonlinear_kernel'].upper();rho=exact_arb(args.radius)
    rb=(Brel+rho/Cstar).upper();rc=(Crel+rho/Cstar).upper();d=(1-rc).lower()
    if not d>0:raise ValueError('complete relative Neumann denominator failed')
    DB=(2*rb/d).upper();DC=(2*Lambda*rc/d+(rb*rb+Lambda*rc*rc)/(d*d)).upper()
    lam=(G*max(DB,DC)).upper();gap=(Cstar*d).lower()
    room=(rho*(1-lam)).lower()
    report=dict(kind='actual_complete_relative_centre_full_Fourier_DQ_budget',complete=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.native,args.kernels,args.candidate)},
        object_sha256=native['object_sha256'],exact_center_parameter=native['exact_center_parameter'],parameter_half_width=native['parameter_half_width'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        exact_requested_interval=kernels['exact_requested_interval'],rows=rows,
        correction_norm='absolute pair X0 = sum_m sup_r |B_m| + sum_m sup_r |c_m|; no omitted output modes',
        centre_all_modes=m,complete_coefficient_suprema=dict(B=ba.tolist(),c=ca.tolist(),B_over_Cref=br.tolist(),c_over_Cref=cr.tolist()),
        bounds={k:record(v) for k,v in dict(centre_B_absolute=B,centre_c_absolute=C,centre_B_relative=Brel,centre_c_relative=Crel,
            correction_radius=rho,relative_B_tube=rb,relative_c_tube=rc,actual_C_abs_lower=gap,
            full_Q_B_derivative=DB,full_Q_c_derivative=DC,full_contraction_factor=lam,
            maximum_allowed_complete_fixed_point_residual=room).items()},
        full_DQ_strict_contraction=bool(lam<1),complete_residual_computed=False,actual_driven_cap_exists=False,
        nonlinear_regular_tail_matched=False,body_matched=False,periodic_frame_holonomy_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_centered_residual_v3.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_cap_A0_translation_budget.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(complete=True,rows=len(rows),Brel=Brel.str(14),Crel=Crel.str(14),
        contraction=lam.str(14),allowed_residual=room.str(14)),flush=True)


if __name__=='__main__':main()
