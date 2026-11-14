#!/usr/bin/env python3
"""Full finite first and second chronological integrals of a saved density.

No angular mode of the quadratic product is discarded. Native DFT padding
exceeds its entire degree; all integration, DFT and exact dyadic choices are
enclosed. Independent off-grid direct Laurent comparisons check the actual
density certificate without reusing its time-circle interpolation nodes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from flint import arb,acb,acb_poly,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import load_polynomial,encode_complex,decode_complex,write_json
from fourfold_actual_reference_density import load_density
from fourfold_packaged_reference_bidisk import PackageReference
from fourfold_retarget_reference_native_grid import RealTimeFourier
from fourfold_exact_fourier_multipoint import time_coefficients
from fourfold_saved_circle_field_multidomain_budget import read,upper


def choose(row,width):
    selected=[];error=arb(0);norm=arb(0)
    for k,value in enumerate(row):
        z=acb(value.real.mid(),0 if k==0 else value.imag.mid())
        if k==0 and not value.imag.contains(0):raise ValueError('zero-mode reality failed')
        w=(1 if k==0 else 2)*(k*width).exp()
        error+=w*abs(value-z);norm+=w*abs(z);selected.append(z)
    return selected,error.upper(),norm.upper()


def full_integrals(coefficients,nodes):
    m=len(coefficients);K=len(coefficients[0])-1
    if nodes<=4*K:raise ValueError('grid must exceed the full quadratic Fourier degree')
    values=[];derivatives=[]
    for row in coefficients:
        folded=[acb(0) for _ in range(nodes)];df=[acb(0) for _ in range(nodes)]
        for k in range(-K,K+1):
            z=row[abs(k)].conjugate() if k<0 else row[k]
            folded[k%nodes]+=z;df[k%nodes]+=acb(0,k)*z
        grid=[nodes*z for z in acb.dft(folded,inverse=True)]
        dgrid=[nodes*z for z in acb.dft(df,inverse=True)]
        if any(not z.imag.contains(0) for z in grid+dgrid):
            raise ValueError('real-label polynomial reality failed')
        values.append([acb(z.real) for z in grid]);derivatives.append([acb(z.real) for z in dgrid])
    J=[]
    for j in range(nodes):
        G=[sum(((-1)**i*values[i][j]/(i+1) for i in range(m)),acb(0))]
        G.extend(values[i][j]/(i+1) for i in range(m))
        product=acb_poly([derivatives[i][j] for i in range(m)])*acb_poly(G)
        J.append(sum((2*product[i]/(i+1) for i in range(0,2*m,2)),acb(0)))
    transformed=acb.dft(J)
    second=[transformed[k]/nodes for k in range(2*K+1)]
    first=[sum((2*coefficients[i][k]/(i+1) for i in range(0,m,2)),acb(0))
           for k in range(K+1)]
    return first,second


def off_grid_checks(reference,field,density,fee):
    finite=RealTimeFourier(density);checks=[]
    # Seven is incommensurate with the original 8192-point label grid.
    # Real times lie inside the disk, not on its radius-5/4 sampling circle.
    for ur,S in [(Fraction(-2,5),Fraction(1,128)),(Fraction(1,3),Fraction(-1,128))]:
        u=acb(exact_arb(ur));Y,Yu,q=reference.grid(u,7,S)
        approximation,_,_=finite.grid(u,7,S)
        row=time_coefficients(field,u);K=(len(row)-1)//2
        for j in [1,3,6]:
            P=sum((a*(acb(0,4*(k-K))*Y[j]).exp() for k,a in enumerate(row)),acb(0))
            direct=(reference.h*P-Yu[j])/q[j]
            difference=abs(direct-approximation[j]).upper()
            if not difference<fee:raise ValueError('off-grid finite-density error exceeds complete certificate')
            checks.append(dict(time=str(ur),label_node=j,label_nodes=7,label_imaginary=str(S),
                full_direct_Laurent_difference=ball_record(difference),below_complete_finite_proxy_error=True))
    return checks


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path('data/phase_ring_continuation')
    p.add_argument('--density-certificate',type=Path,default=Path('notes/2026-11-12-actual-forward419-complete-reference-density.json'))
    p.add_argument('--package',type=Path,default=base/'step5_forward419_exact_reference_package.npz.gz')
    p.add_argument('--field-polynomial',type=Path,default=base/'step5_reference419_time_circle_field_polynomial/manifest.json')
    p.add_argument('--nodes',type=int,default=16384);p.add_argument('--bits',type=int,default=320)
    p.add_argument('--inner-strip',default='1/256')
    p.add_argument('--polynomial',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;tic,cpu=time.monotonic(),time.process_time()
    cert=read(args.density_certificate)
    if not cert['complete'] or not cert['complete_continuous_true_density_proved_on_this_segment']:
        raise ValueError('complete actual true density certificate required')
    path=Path(cert['density_polynomial_manifest'])
    if sha(path)!=cert['density_polynomial_manifest_sha256']:raise ValueError('density manifest changed')
    manifest,coefficients=load_density(path);reference=PackageReference(args.package)
    fm,field=load_polynomial(args.field_polynomial)
    if (manifest['identity']!=cert['identity'] or manifest['identity']['reference']!=reference.identity
            or manifest['identity']['field_polynomial_manifest_sha256']!=sha(args.field_polynomial)):
        raise ValueError('integral input exact identities differ')
    s=exact_arb(Fraction(cert['initial_label_strip']));sigma=exact_arb(Fraction(args.inner_strip))
    if not 0<=sigma<s:raise ValueError('R72 needs a strictly smaller working strip')
    report=dict(kind='actual_full_finite_two_chronological_integrals_and_local_flow',complete=False,
        source_sha256=sha(__file__),density_certificate_sha256=sha(args.density_certificate),
        density_manifest_sha256=sha(path),reference_package_sha256=sha(args.package),
        field_polynomial_manifest_sha256=sha(args.field_polynomial),identity=cert['identity'],
        bits=args.bits,angular_nodes=args.nodes,outer_label_strip=cert['initial_label_strip'],
        inner_label_strip=args.inner_strip)
    def save():write_json(args.out,report)
    save()
    report['independent_off_grid_checks']=off_grid_checks(reference,field,coefficients,
                          upper(cert['complete_finite_proxy_reconstruction_error']['total']))
    save();print('OFF_GRID_COMPLETE',flush=True)
    first,second=full_integrals(coefficients,args.nodes)
    C1,e1,n1=choose(first,s);C2,e2,n2=choose(second,s)
    payload=dict(kind='exact_dyadic_two_chronological_integral_approximation',schema_version=1,
        density_manifest_sha256=sha(path),identity=cert['identity'],frequency_scale=1,
        definition='C1=integral ghat; C2=integral ghat_x(u)*integral_-1^u ghat(v)dv du; u in [-1,1]',
        negative_frequency_rule='coefficient at -k is conjugate of coefficient at k; zero mode real',
        first=[encode_complex(v) for v in C1],second=[encode_complex(v) for v in C2],
        complete_choice_error_on_outer_strip=dict(first=ball_record(e1),second=ball_record(e2)))
    data=gzip.compress((json.dumps(payload,separators=(',',':'))+'\n').encode(),compresslevel=9,mtime=0)
    args.polynomial.parent.mkdir(parents=True,exist_ok=True);args.polynomial.write_bytes(data)
    loaded=read(args.polynomial)
    for key,row in [('first',C1),('second',C2)]:
        again=[decode_complex(z) for z in loaded[key]]
        if len(again)!=len(row) or any(a!=b for a,b in zip(row,again)):
            raise ValueError('integral exact dyadic reload failed')
    A=upper(cert['R72_inputs_on_this_whole_segment']['common_integrated_majorant_A'])
    E=upper(cert['R72_inputs_on_this_whole_segment']['integrated_approximation_error_E'])
    R=s-sigma;d=R-A
    if not A<=R/2:raise ValueError('actual R72 radius hypothesis failed')
    truncation=(A**3/(2*d**2)).upper();field=(E*(1+A/R)).upper()
    B=(truncation+field+e1+e2).upper()
    report['finite_integrals']=dict(first_degree=len(C1)-1,second_degree=len(C2)-1,
        exact_density_time_terms=len(coefficients),full_quadratic_product_retained=True,
        padded_grid_has_no_quadratic_alias=args.nodes>4*(len(coefficients[0])-1),
        first_integral_A_norm=ball_record(n1),second_integral_A_norm=ball_record(n2),
        first_choice_and_arithmetic_A_error=ball_record(e1),second_choice_and_arithmetic_A_error=ball_record(e2))
    report['local_true_coordinate_flow']=dict(A=ball_record(A),E=ball_record(E),
        R=ball_record(R),d=ball_record(d),A_le_R_over_two=True,
        omitted_chronological_terms=ball_record(truncation),approximate_density_transfer=ball_record(field),
        full_error_X_minus_x_minus_C1_minus_C2=ball_record(B),
        exact_initial_condition='X(-1,x)=x for this same reference-coordinate segment',
        physical_flow='y(u,x)=Y(u,X(u,x)); physical initial data Y(-1,x)')
    report['polynomial']=str(args.polynomial);report['polynomial_sha256']=sha(args.polynomial)
    report['polynomial_bytes']=len(data);report['exactly_reloaded']=True;report['complete']=True
    report['wall_seconds']=time.monotonic()-tic;report['cpu_seconds']=time.process_time()-cpu
    report['limitations']=['One actual segment only; global ordered cross terms must still be accumulated.',
        'The primitive density is exact saved dyadic; its two integrals are enclosed by saved dyadics plus explicit errors.',
        'No full return, KAM parameter certification, nonlinear metric correction or geometric completion is inferred.']
    save();print(json.dumps(dict(complete=True,B=ball_record(B),first=ball_record(n1),second=ball_record(n2),
        cpu_seconds=report['cpu_seconds'],wall_seconds=report['wall_seconds'])),flush=True)


if __name__=='__main__':main()
