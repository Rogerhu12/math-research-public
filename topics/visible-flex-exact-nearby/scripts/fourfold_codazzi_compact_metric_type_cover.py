#!/usr/bin/env python3
"""All real curvature signs on [0,3/2] for a genuine compact-metric range.

Reuse the original full [0,.2] coefficient boxes by the exact E_nu law,
prove the remaining real-root strip by the full primitive provider, and
retain the original unchanged positive-cap interval. No PDE candidate is
used, and no old target certificate is transferred inside the new bump.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_two_jet_newton_source import common_cells
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def bump(l,r):
    a,b=Fraction(1,20),Fraction(9,50)
    if r<=a or l>=b:return arb(0),arb(0)
    if l<a or r>b:raise ValueError('split the true compact bump seam')
    t=(real_interval(l,r)-exact_arb(a))/exact_arb(b-a)
    return 4096*t**6*(1-t)**6,24576*t**5*(1-t)**5*(1-2*t)/exact_arb(b-a)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--prefix',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--positive-cap',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--nu-left',type=Fraction,default=Fraction(-1,25));ap.add_argument('--nu-right',type=Fraction,default=Fraction(-1,40))
    ap.add_argument('--root-left',type=Fraction,default=Fraction(119,500));ap.add_argument('--root-right',type=Fraction,default=Fraction(239,1000))
    ap.add_argument('--max-step',type=Fraction,default=Fraction(1,2000));ap.add_argument('--max-depth',type=int,default=18)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve the entire type-cover attempt')
    if not args.nu_left<=args.nu_right<0:raise ValueError('the proposed metric interval must be explicit and negative')
    prior=read(args.prefix);cap=read(args.positive_cap)
    if (not prior['complete'] or prior['exact_requested_interval']!=['0','1/5']
        or not cap['complete'] or not cap['cap_linear_reference_certified']
        or prior['object_sha256']!=sha(args.object) or cap['object_sha256']!=sha(args.object)
        or prior['exact_center_parameter']!=cap['exact_center_parameter']
        or prior['parameter_half_width']!=cap['parameter_half_width']
        or prior['coefficient_provider_sha256']!=sha(Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py'))
        or not prior['whole_affine_parameter_interval'] or not prior['whole_real_angular_circle']):
        raise ValueError('complete same-object original scalar inputs are required')
    if not Fraction(1,5)<args.root_left<args.root_right==Fraction(cap['rows'][0]['interval'][0]):
        raise ValueError('the requested root strip must end at the real positive cap entrance')
    doc=dict(kind='actual_full_compact_metric_curvature_type_cover',complete=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),inputs={str(p):sha(p) for p in (args.object,args.prefix,args.positive_cap)},
        exact_center_parameter=prior['exact_center_parameter'],parameter_half_width=prior['parameter_half_width'],
        exact_nu_interval=[str(args.nu_left),str(args.nu_right)],exact_requested_interval=['0','3/2'],
        whole_affine_parameter_interval=True,complete_primitive_tail=True,whole_real_radial_interval=False,
        root_strip=[str(args.root_left),str(args.root_right)],prefix_rows=[],new_rows=[],positive_rows=[],
        subdivisions=[],failure=None,no_PDE_candidate_used=True,body_PDE_or_inverse_not_proved=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_coefficients.py','fourfold_phase_newton_source_centered.py',
            'fourfold_phase_two_jet_newton_source.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    def persist():doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    try:
        nu=real_interval(args.nu_left,args.nu_right);cursor=Fraction(0)
        for j,row in enumerate(prior['rows']):
            left,right=map(Fraction,row['interval']);gl,gr=map(Fraction,row['actual_scalar_germ'])
            if left!=cursor or not gl<=left<right<=gr:raise ValueError('old prefix cover/germ changed')
            c={k:box_from_record(row['true_target_coefficients'][k]) for k in ('K','E','beta')}
            if not c['E']>0:raise ValueError('true E positivity lost')
            seams=[left,*[q for q in (Fraction(1,20),Fraction(9,50)) if left<q<right],right]
            for l,r in zip(seams,seams[1:]):
                h,hp=bump(l,r);Kn=(c['K']+nu*c['beta']*hp/(2*c['E']))*(-nu*h).exp()
                passed=bool(Kn<0)
                doc['prefix_rows'].append(dict(original_row=j,interval=[str(l),str(r)],
                    actual_scalar_germ=row['actual_scalar_germ'],K_nu=record(Kn),strict_negative=passed))
                if not passed:raise ValueError('strict new-metric K sign failed at prefix row '+str(j))
            cursor=right
        if cursor!=Fraction(1,5):raise ValueError('incomplete old prefix')
        persist();print(dict(stage='new_nu_prefix',rows=len(doc['prefix_rows']),
            K_upper=max(box_from_record(x['K_nu']).upper() for x in doc['prefix_rows']).str(14)),flush=True)
        target=CodazziCoefficientTarget(args.object,Fraction(prior['parameter_half_width']),512,4096)
        allcuts=common_cells(target)
        cuts=sorted({Fraction(1,5),args.root_left,args.root_right}|{q for q in allcuts if Fraction(1,5)<q<args.root_right})
        pending=[]
        for l,r in reversed(list(zip(cuts,cuts[1:]))):
            count=max(1,-(-(r-l)//args.max_step))
            for k in reversed(range(count)):
                ll=l+(r-l)*k/count;rr=l+(r-l)*(k+1)/count
                pending.append((ll,rr,0,'negative' if rr<=args.root_left else 'increasing'))
        cursor=Fraction(1,5);last=time.monotonic()
        while pending:
            l,r,depth,mode=pending.pop()
            if l!=cursor:raise ValueError('new exact native cover is discontinuous')
            c=target.coefficients(l,r)
            passed=bool(c['K']<0 if mode=='negative' else c['K1']>0)
            if not passed:
                doc['subdivisions'].append(dict(interval=[str(l),str(r)],depth=depth,mode=mode,
                    original_K=record(c['K']),original_K1=record(c['K1'])))
                if depth>=args.max_depth:raise ValueError('complete true root-strip gate remains unresolved')
                mid=(l+r)/2;pending.append((mid,r,depth+1,mode));pending.append((l,mid,depth+1,mode));continue
            doc['new_rows'].append(dict(interval=[str(l),str(r)],actual_scalar_germ=list(map(str,target.cell)),
                mode=mode,K=record(c['K']),K1=record(c['K1']),primitive_tail=record(c['primitive_tail']),
                strict_requested_gate=True,depth=depth))
            cursor=r
            if time.monotonic()-last>20:
                persist();print(dict(stage='new_actual_root_neighborhood',rows=len(doc['new_rows']),
                    right=str(r),mode=mode,seconds=time.monotonic()-started),flush=True);last=time.monotonic()
        if cursor!=args.root_right:raise ValueError('incomplete true root neighborhood')
        left=target.coefficients(args.root_left,args.root_left);right=target.coefficients(args.root_right,args.root_right)
        if not left['K']<0 or not right['K']>0:raise ValueError('true simple-root bracket signs failed')
        doc['root_endpoint_values']=dict(left=record(left['K']),right=record(right['K']))
        cursor=args.root_right
        for j,row in enumerate(cap['rows']):
            l,r=map(Fraction,row['interval'])
            if l>=Fraction(3,2):break
            rr=min(r,Fraction(3,2));gl,gr=map(Fraction,row['actual_scalar_germ'])
            if l!=cursor or not gl<=l<rr<=r<=gr:raise ValueError('true unchanged positive-cap cover differs')
            K=box_from_record(row['coefficients']['K'])
            if not K>0:raise ValueError('an old positive-cap row is not strictly positive')
            doc['positive_rows'].append(dict(original_row=j,interval=[str(l),str(rr)],
                actual_scalar_germ=row['actual_scalar_germ'],K=record(K),strict_positive=True))
            cursor=rr
        if cursor!=Fraction(3,2):raise ValueError('true positive suffix is incomplete')
        doc.update(complete=True,whole_real_radial_interval=True,exactly_one_real_K_root=True,
            root_simple_for_whole_eta_and_nu=True,root_independent_of_nu=True,
            strict_negative_until_root=True,strict_positive_after_root=True,
            original_target_not_reused_inside_compact_bump=True,
            unchanged_true_positive_cap_reused_only_after_exact_bump_endpoint=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    persist();print(dict(complete=doc['complete'],failure=doc['failure'],prefix=len(doc['prefix_rows']),
        new=len(doc['new_rows']),positive=len(doc['positive_rows']),seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
