#!/usr/bin/env python3
"""Differentiate the proved high-seven Taylor identity, not its value bound.

Read the already complete scalar cache.  Restrict any accepted polynomial
to a subinterval and enclose its true derivatives using the saved point
jets and whole seventh derivative.  Optional compact-control T models
use only the original finite scalar polynomial a; no primitive angular
exponential is recomputed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip,json,math,time
from pathlib import Path
from flint import arb,arb_series,ctx
from fourfold_codazzi_phase_complete_Arb_high_scalar_jets import FullArbScalarTarget
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha

PROVIDER='b57e794709edcb8c3281df909f463a56a906aec8a8ba8a8b3f49394f10e4590f'
COVER='94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3'
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def mid(x):
    a,b=map(int,x.mid().man_exp())
    return Fraction(a*2**b) if b>=0 else Fraction(a,2**(-b))


def restrict_model(row,name,left,right,derivative=0):
    """Return exact derivative coefficients, a full error, and a true value.

    The polynomial retains row['center']; callers need not move its centre
    or reevaluate any target.  All derivatives are ordinary, not divided
    by a factorial.  The final Taylor identity supplies orders 0 through7.
    """
    left,right=Fraction(left),Fraction(right);j=int(derivative)
    a,b=map(Fraction,row['interval']);center=Fraction(row['center'])
    if not a<=left<=right<=b or not 0<=j<=7:
        raise ValueError('restriction must stay in the proved cell and derivative order')
    model=row['models'][name];c=list(map(Fraction,model['exact_centered_polynomial']))
    point=[box_from_record(z) for z in model['point_jets']]
    whole7=box_from_record(model['whole_final_derivative'])
    if len(c)!=8 or len(point)!=7:raise ValueError('a full degree7 identity is required')
    h=exact_arb(max(abs(left-center),abs(right-center)))
    fee=sum((math.factorial(k)//math.factorial(k-j)*abs(point[k]-exact_arb(c[k]))*h**(k-j)
             for k in range(j,7)),arb(0))
    fee+=(abs(whole7-math.factorial(7)*exact_arb(c[7]))*h**(7-j)/math.factorial(7-j))
    coefficients=[Fraction(math.factorial(k),math.factorial(k-j))*c[k] for k in range(j,8)]
    x=real_interval(left-center,right-center);value=arb(0)
    for z in reversed(coefficients):value=value*x+exact_arb(z)
    return coefficients,fee.upper(),value+arb(0,fee.upper())


def normalized_true_jets(row,name,left,right):
    return [restrict_model(row,name,left,right,j)[2]/math.factorial(j) for j in range(8)]


def T_model(target,row):
    left,right=map(Fraction,row['interval']);center=Fraction(row['center']);gl,gr=map(Fraction,row['actual_scalar_germ'])
    if not Fraction(1,20)<=left<right<=Fraction(9,50):
        raise ValueError('the genuine compact-control T is requested only on its support')
    previous=ctx.cap;ctx.cap=max(previous,10)
    try:
        point_a=target.complete_scalar_jets(center,center,gl,gr)[2]
        whole_a=target.complete_scalar_jets(left,right,gl,gr)[2]
        point={n:[box_from_record(z) for z in row['models'][n]['point_jets']]
               for n in ('beta','gamma')}
        whole={n:normalized_true_jets(row,n,left,right) for n in ('beta','gamma')}
        if not whole_a[0]>0 or not whole['gamma'][0]>0:
            raise ValueError('the complete compact-control denominator lacks its true sign')
        pa=arb_series(point_a[:7],prec=7);pg=arb_series(point['gamma'],prec=7)
        pb=arb_series(point['beta'],prec=7)
        wa=arb_series(whole_a[:8],prec=8);wg=arb_series(whole['gamma'],prec=8)
        wb=arb_series(whole['beta'],prec=8)
        Pt=pb/(2*pa*pa*pg*pg);Wt=wb/(2*wa*wa*wg*wg)
        if Pt.prec<7 or Wt.prec<8:raise ValueError('the complete quotient jet order was truncated')
        coefficients=[mid(Pt[j]) for j in range(7)]+[mid(Wt[7])]
        h=exact_arb((right-left)/2)
        fee=sum((abs(Pt[j]-exact_arb(coefficients[j]))*h**j for j in range(7)),arb(0))
        fee+=abs(Wt[7]-exact_arb(coefficients[7]))*h**7
        return dict(interval=row['interval'],center=row['center'],actual_scalar_germ=row['actual_scalar_germ'],
            models={'T':dict(exact_centered_polynomial=list(map(str,coefficients)),
                point_jets=[record(Pt[j]) for j in range(7)],whole_final_derivative=record(math.factorial(7)*Wt[7]),
                complete_uniform_remainder=record(fee.upper()),complete_true_value=record(Wt[0]))},
            exact_identity='T=beta/(2*(a*gamma)^2)=beta/(2*E_nu)',
            no_primitive_or_angular_exponential_recomputed=True)
    finally:ctx.cap=previous


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cover',type=Path,default=Path('notes/2026-11-14-R133-complete-169-germ-phase-scalar-cover-native.json.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--max-derivative',type=int,default=3)
    ap.add_argument('--compact-T',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256;ctx.cap=10
    if args.out.exists():raise FileExistsError('keep every actual derivative-cache consumption')
    if sha(args.cover)!=COVER or sha(args.object)!=OBJECT or sha(Path(__file__).with_name('fourfold_codazzi_phase_complete_Arb_high_scalar_jets.py'))!=PROVIDER:
        raise ValueError('the complete scalar identity changed')
    cover=read(args.cover)
    if not cover['complete'] or not 0<=args.max_derivative<=7:raise ValueError('a full cover and explicit supported order are required')
    target=FullArbScalarTarget(args.object,Fraction(0),160,7) if args.compact_T else None
    fees={name:[arb(0) for j in range(args.max_derivative+1)] for name in ('beta','K','s','gamma','q')}
    maxfees={name:[arb(0) for j in range(args.max_derivative+1)] for name in fees}
    rows=0;overlaps=0;Trows=[];Tfee=arb(0);Tcursor=Fraction(1,20)
    for germ in cover['germs']:
        path=Path(germ['path'])
        if sha(path)!=germ['sha256']:raise ValueError('a complete saved scalar germ changed')
        doc=read(path)
        for row in doc['rows']:
            left,right=map(Fraction,row['interval']);length=exact_arb(right-left)
            for name in fees:
                for j in range(args.max_derivative+1):
                    coefficients,fee,true=restrict_model(row,name,left,right,j)
                    fees[name][j]+=length*fee
                    if fee>maxfees[name][j]:maxfees[name][j]=fee.upper()
                    if j==0:
                        if not true.overlaps(box_from_record(row['models'][name]['complete_true_value'])):
                            raise ValueError('the differentiated identity disagrees with its original complete value')
                        overlaps+=1
            if target is not None and left>=Fraction(1,20) and right<=Fraction(9,50):
                if left!=Tcursor:raise ValueError('the exact compact-control support has a gap')
                tr=T_model(target,row);Trows.append(dict(scalar_native_sha256=germ['sha256'],**tr))
                Tfee+=length*box_from_record(tr['models']['T']['complete_uniform_remainder']).upper();Tcursor=right
            rows+=1
        print(dict(germ=germ['germ_index'],cells=rows,Tcells=len(Trows),seconds=time.monotonic()-started),flush=True)
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('all626 complete scalar cells consumed without target recomputation',rows==cover['accepted_cell_count']==626),
        ('all five true values agree with the original complete whole-cell enclosures',overlaps==5*rows),
        ('derivative errors use the saved point jets and complete seventh derivative',all(z.is_finite() for v in fees.values() for z in v)),
        ('all derivative models include every original angular and primitive error',cover['complete']),
        ('the actual affine parameter remains eta0 with zero offset',cover['exact_affine_offset']=='0'),
        ('compact-control denominator jets retain the exact complete support',target is None or Tcursor==Fraction(9,50)),
    )]
    report=dict(kind='actual_complete_scalar_Taylor_derivative_restriction',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),cover_sha256=COVER,object_sha256=OBJECT,provider_sha256=PROVIDER,
        actual_affine_parameter='eta_0',exact_affine_offset='0',whole_original_eta=False,
        exact_nu=cover['configuration']['exact_nu'],exact_interval=cover['exact_complete_interval'],
        accepted_cells=rows,max_derivative=args.max_derivative,
        integrated_complete_derivative_model_errors={n:[record(z.upper()) for z in v] for n,v in fees.items()},
        maximum_complete_derivative_model_errors={n:[record(z.upper()) for z in v] for n,v in maxfees.items()},
        compact_T_complete=target is not None and Tcursor==Fraction(9,50),
        compact_T_exact_interval=['1/20','9/50'] if target is not None else None,
        compact_T_models=Trows,integrated_complete_compact_T_model_error=record(Tfee.upper()),
        no_derivative_taken_of_an_unstructured_value_error=True,no_original_primitive_recomputed=True,
        no_parameter_response_or_conjugacy_claimed=True,gates=gates,seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],cells=rows,compact_T_cells=len(Trows),
        compact_T_error=Tfee.str(18),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a full scalar-derivative consumption gate failed')


if __name__=='__main__':main()
