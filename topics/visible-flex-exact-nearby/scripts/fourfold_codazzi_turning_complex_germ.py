#!/usr/bin/env python3
"""Actual reciprocal-body complex radial/angle germ at the true K root.

The complete original intrinsic primitive, its infinite remainder, and the
whole real affine parameter interval are retained.  The selected reciprocal
candidate is its exact finite dyadic PPoly, inside one true scalar germ and
one candidate piece.  Complex energy uses bilinear zero convolution, never
complex conjugation or real_part.  This is a coefficient-domain certificate;
its existence flags do not assert a nonlinear solution or a turning inverse.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx

from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_phase_beta_bulk_box import Box,cdot,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def complex_record(z):
    z=acb(z)
    return dict(real=record(z.real),imag=record(z.imag),modulus_upper=record(abs(z).upper()))


def genuine_complex_target(target,radial):
    FF,_,aa,EF,_,primitive_tail=target.scalar_jets_and_fourier(radial)
    aa=[x.to_acb() for x in aa]
    rev=(-np.arange(target.nodes))%target.nodes
    norms=[arb(float(np.max(reduce_box(Box(f.magnitude_upper())).hi))).upper() for f in FF]
    product_fees={}
    def mean(i,j):
        finite=cdot(FF[i],FF[j][rev]).sum().to_acb()
        fee=(3*(norms[i]*EF[j][0]+norms[j]*EF[i][0]+EF[i][0]*EF[j][0])).upper()
        product_fees[str(i)+','+str(j)]=fee
        # |error| <= fee entails these two rectangular coordinate bounds.
        return finite+acb(arb(0,fee),arb(0,fee))
    E=mean(1,1);E1=2*mean(1,2);E2=2*mean(2,2)+2*mean(1,3)
    a,a1,a2,a3=aa
    gap=E-a1*a1
    if not a.real>0 or not E.real>0 or not gap.real>0:
        raise ValueError('the complete complex intrinsic denominators do not stay in the right half-plane')
    K=-a2/(a*E)+a1*E1/(2*a*E*E)
    K1=(-a3/(a*E)+a1*a2/(a*a*E)+3*a2*E1/(2*a*E*E)
        +a1*E2/(2*a*E*E)-a1*a1*E1/(2*a*a*E*E)-a1*E1*E1/(a*E**3))
    gamma=E.sqrt()/a;beta=a1/a;s=-a*(E/gap).sqrt()
    if not K1.real>0 or not s.real<0:
        raise ValueError('the true complex simple-root slope or rotational reciprocal branch is unresolved')
    return dict(a=a,a1=a1,a2=a2,a3=a3,E=E,E1=E1,E2=E2,
        rotational_gap=gap,K=K,K1=K1,gamma=gamma,beta=beta,s=s),primitive_tail,product_fees


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root',type=Path,default=Path('notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--theta-strip',type=Fraction,default=Fraction(1,1024))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every actual complex-domain attempt')
    doc=dict(kind='actual_reciprocal_body_complete_complex_turning_germ',complete=False,
        proved=False,source_sha256=sha(__file__),failure=None,
        inputs={str(p):sha(p) for p in (args.object,args.root,args.candidate)},
        complex_radial_radius=str(args.radius),physical_theta_strip=str(args.theta_strip),
        bits=args.bits,nonlinear_body_solution_proved=False,actual_fold_constructed=False,
        full_turning_or_feedback_inverse_proved=False,gates=[])
    try:
        root=read(args.root)
        if (not root['complete'] or not root['whole_affine_parameter_interval']
            or not root['complete_original_primitive_and_tail']
            or root['object_sha256']!=sha(args.object)
            or not root['root_independent_of_compact_metric_nu']):
            raise ValueError('a complete same-object true root is required')
        lo,hi=map(Fraction,root['exact_root_interval']);gl,gr=map(Fraction,root['actual_common_scalar_germ'])
        left,right=lo-args.radius,hi+args.radius
        if not gl<left<right<gr or not left>Fraction(9,50):
            raise ValueError('the whole complex rectangle must stay inside the original root germ beyond the compact bump')
        radial=acb(real_interval(left,right),arb(0,exact_arb(args.radius)))
        target=CodazziCoefficientTarget(args.object,Fraction(root['parameter_half_width']),512,4096)
        target.set_cell(gl,gr)
        coeff,primitive_tail,product_fees=genuine_complex_target(target,radial)
        saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
        if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object) or meta['physical_frequency_factor']!=4:
            raise ValueError('different actual reciprocal candidate identity')
        al=Fraction(meta['exact_float_amplitude']);nu=Fraction(meta['exact_float_nu'])
        if al!=Fraction.from_float(float(meta['amplitude'])) or nu!=Fraction.from_float(float(meta['nu'])):
            raise ValueError('candidate exact dyadic parameter identity failed')
        nulo,nuhi=map(Fraction,root['exact_nu_interval'])
        if not nulo<=nu<=nuhi:raise ValueError('candidate compact parameter leaves the certified true root family')
        nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
        j=bisect_right(nodes,left)-1
        if not 0<=j<len(nodes)-1 or not nodes[j]<left<right<nodes[j+1]:
            raise ValueError('actual complex radial domain crosses a candidate PPoly join')
        local=radial-acb(exact_arb(nodes[j]));cc=saved['piece_coefficients'][:,j,:]
        vals=[]
        for k in range(cc.shape[1]):
            value=acb(0)
            for degree in range(4):value=value*local+acb(arb(float(cc[degree,k])))
            vals.append(exact_arb(al)*value)
        m=int(meta['modes'])
        if len(vals)!=2*m+1:raise ValueError('all exact sine/cosine and mean rows are required')
        strip=exact_arb(args.theta_strip);U=[];V=[]
        for q in range(5):
            U.append(sum((abs(vals[k-1])*(4*k)**q*(4*k*strip).exp() for k in range(1,m+1)),arb(0)).upper())
            V.append(sum((abs(vals[m+k])*(4*k)**q*(4*k*strip).exp() for k in range(1,m+1)),arb(0)).upper())
        vmean=coeff['s']+vals[m]
        V[0]=(V[0]+abs(vmean)).upper()
        vnonmean=(V[0]-abs(vmean)).upper()
        # Re v < 0 on the whole complex product. No sampled minimum is used.
        vgap=(-vmean.real.upper()-vnonmean).lower()
        if not vgap>0:raise ValueError('complete reciprocal candidate v fails the complex nonzero gate')
        ga,be,KM=map(lambda x:abs(coeff[x]).upper(),('gamma','beta','K'))
        d=(ga*U[0]).upper();a=(ga*V[0]).upper()
        dtheta=(ga*U[1]).upper();atheta=(ga*V[1]).upper()
        a_real=(-coeff['gamma']*vmean).real.lower()-ga*vnonmean
        sqrtk=coeff['K1'].sqrt()
        aq=(a*abs(sqrtk)).upper()
        aq_real=(-coeff['gamma']*vmean*sqrtk).real.lower()-ga*vnonmean*abs(sqrtk)
        if not a_real>0 or not aq_real>0:
            raise ValueError('the true characteristic root amplitude fails its complex positive-branch gate')
        g=(ga*V[1]+2*be*U[0]*V[0]).upper()
        L11=(ga*U[1]+be*(1+3*U[0]**2+KM*V[0]**2)).upper()
        L22=(ga*U[1]+be*(1+U[0]**2+3*KM*V[0]**2)).upper()
        Lsum=(L11+L22+(1+KM)*g).upper()
        doc.update(object_sha256=sha(args.object),exact_center_parameter=root['exact_center_parameter'],
            exact_parameter_half_width=root['parameter_half_width'],whole_affine_parameter_interval=True,
            actual_fixed_nu=str(nu),exact_amplitude=str(al),root_interval=list(map(str,(lo,hi))),
            original_scalar_germ=list(map(str,(gl,gr))),actual_candidate_piece=j,
            exact_candidate_piece_interval=list(map(str,nodes[j:j+2])),
            complex_radial_rectangle=dict(real=list(map(str,(left,right))),imag=['-'+str(args.radius),str(args.radius)]),
            domain_contains_disks_about_every_true_parameter_root=True,
            compact_bump_identically_zero_on_entire_actual_germ=True,
            finite_energy_is_bilinear_zero_convolution_without_conjugation=True,
            complete_primitive_tail=record(primitive_tail),
            complete_energy_product_fees={k:record(v) for k,v in product_fees.items()},
            complex_intrinsic_coefficients={k:complex_record(v) for k,v in coeff.items()},
            exact_candidate_metadata=meta,all_finite_candidate_modes_retained=True,
            exact_mean_v=complex_record(vmean),candidate_U_derivative_Astrip=[record(x) for x in U],
            candidate_v_derivative_Astrip=[record(x) for x in V],
            bounds={k:record(v) for k,v in dict(
                complete_v_nonmean=vnonmean,minus_Re_v=vgap,
                d=d,a=a,dtheta=dtheta,atheta=atheta,Re_a_lower=a_real,
                sqrtk=abs(sqrtk).upper(),Re_k_lower=coeff['K1'].real.lower(),
                aq=aq,Re_aq_lower=aq_real,aqtheta=(atheta*abs(sqrtk)).upper(),
                complete_g=g,complete_L11=L11,complete_L22=L22,complete_L_matrix=Lsum).items()},
            dependencies={n:sha(Path(__file__).with_name(n)) for n in (
                'fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_candidate_shards.py',
                'fourfold_codazzi_reciprocal_candidate_tools.py','fourfold_phase_metric_defect.py',
                'fourfold_phase_newton_source_centered.py','fourfold_phase_cap_scaled_body.py',
                'fourfold_phase_cap_parameter_comparison.py','fourfold_phase_beta_bulk_box.py',
                'fourfold_phase_beta_bulk_interval.py')})
        for name in ('same true complete intrinsic object and all real affine parameters',
            'one original scalar germ and one complete dyadic candidate piece',
            'complete bilinear analytic energy and its infinite primitive remainder',
            'complex a E rotational gap and K1 nonzero before division and branches',
            'full angular strip reciprocal nonzero and positive characteristic root amplitude',
            'every finite mode and both original physical component means retained'):
            doc['gates'].append(dict(name=name,passed=True))
        doc.update(complete=True,proved=True)
    except Exception as error:
        doc['failure']=repr(error)
    doc['seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],out=str(args.out),sha256=sha(args.out),
        bounds={k:v['ball'] for k,v in doc.get('bounds',{}).items()},seconds=doc['seconds']),flush=True)
    if not doc['complete']:raise SystemExit(1)


if __name__=='__main__':main()
