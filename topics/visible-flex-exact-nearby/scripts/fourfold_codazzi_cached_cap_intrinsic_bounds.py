#!/usr/bin/env python3
"""Consume complete old intrinsic rows on the exact cap; no target evaluation."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

KIND='actual_cached_complete_cap_intrinsic_beta_gamma_K_maxima_v1'
ORIGINAL_KIND='complete_current_moving_positive_body_coefficients_v1'
LEFT=Fraction(9,10);RIGHT=Fraction(25,8)
ORIGINAL_LEFT=Fraction('0.2384058742994')
ETA=Fraction(-7789843107295549,4611686018427387904)
NU=Fraction(-2572625729470897,72057594037927936)
ALPHA=Fraction(6890507429876859,9007199254740992)
EXPECTED=dict(
    native='ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d',
    split_manifest='32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3',
    original_source='1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c',
    object='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848',
    joint_summary='67fa3c6664ab90a1dbbc91960b10f4f75c8f6372fee272ddca8f780f834efb86',
    joint_process='61896c151fcd7593076195e0d320713f829a087cb9e3b597bbbd61b0c650ae61')
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CAP_CACHE='3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22'
ZDEF='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def encoded(d):return (json.dumps(d,indent=2,allow_nan=False)+'\n').encode()
def row_sha(d):return hashlib.sha256(encoded(d)).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix=='.gz' else raw)
def save(path,d):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=encoded(d)
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_bytes(raw);os.replace(tmp,path)
def record(x):
    x=arb(x)
    return dict(ball=x.str(80),lower=x.lower().str(80),upper=x.upper().str(80))
def ball(r):
    x=arb(r['ball'])
    if not x.is_finite():raise ValueError('nonfinite original intrinsic enclosure')
    return x
def exact(q):
    q=Fraction(q);return arb(q.numerator)/q.denominator

def inputs(a):
    for name,h in EXPECTED.items():
        if sha(getattr(a,name))!=h:raise ValueError('an exact completed input changed: '+name)
    old,parts,obj,joint,process=(read(getattr(a,k)) for k in
        ('native','split_manifest','object','joint_summary','joint_process'))
    if (parts.get('kind')!='complete_native_lossless_container_binary_parts_v2'
        or parts.get('original_sha256')!=EXPECTED['native'] or parts.get('original_bytes')!=6223338
        or len(parts.get('parts',[]))!=4 or not parts.get('native_complete')
        or parts.get('native_failure') is not None or parts.get('complete_native_rows')!=4650
        or parts.get('original_source_sha256')!=EXPECTED['original_source']
        or not parts.get('no_numerical_record_changed') or not parts.get('original_container_restored_exactly')):
        raise ValueError('the original four-part complete native identity differs')
    if (obj.get('kind')!='exact_affine_symmetric_infinite_R33_graph'
        or Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))!=ETA):
        raise ValueError('the original exact intrinsic eta object changed')
    ident=old.get('identity',{})
    if (old.get('kind')!=ORIGINAL_KIND or not old.get('complete')
        or not old.get('coefficient_cover_complete') or old.get('failure') is not None
        or old.get('pending') or not old.get('whole_original_eta')
        or len(old.get('rows',[]))!=4650
        or ident.get('source_sha256')!=EXPECTED['original_source']
        or ident.get('candidate_sha256')!=CANDIDATE or ident.get('object_sha256')!=EXPECTED['object']
        or ident.get('cap_cache_sha256')!=CAP_CACHE
        or Fraction(ident['exact_eta_center'])!=ETA
        or Fraction(ident['parameter_half_width'])!=Fraction(1,10**9)
        or Fraction(ident['actual_nu'])!=NU or Fraction(ident['actual_alpha'])!=ALPHA
        or ident['modes']!=32 or Fraction(ident['left'])!=ORIGINAL_LEFT
        or Fraction(ident['right'])!=RIGHT
        or list(map(Fraction,old['covered_interval']))!=[ORIGINAL_LEFT,RIGHT]):
        raise ValueError('the full old native eta/nu/candidate/cap-cache scope differs')
    if (joint.get('kind')!='actual_complete_cap_full193_Z_joint_coefficient_suprema_v1'
        or not joint.get('complete') or joint.get('failure') is not None
        or len(joint.get('gates',[]))!=10 or not all(g['passed'] for g in joint['gates'])
        or joint.get('source_sha256')!='d909f2fc5eff54e42c3dcfe9355016f42c08cef1a6b04298cc62022fe6bf7d1e'
        or joint.get('native_sha256')!='dd236bb30e17ed457a45bd38a24ff3188d896562e5e2e4189d5f3a5579cdc39c'
        or joint.get('input_sha256',{}).get('complete_direction_definition')!=ZDEF
        or joint.get('exact_interval')!=['9/10','25/8']
        or joint.get('completed_cap_piece_count')!=660
        or joint.get('all_original_repair_target_FFT_ODE_and_cap_residual_recomputations')!=0
        or process.get('run_id')!='43674204314' or process.get('run_attempt')!='1'
        or process.get('kind')!='actual_public_complete_cap_Z_joint_coefficient_process'
        or process.get('complete_native_sha256')!=joint['native_sha256']
        or not any(c.get('label')=='complete_cap193_coefficientwise_Bernstein_and_joint_norms'
                   and c.get('actual_returncode')==0 for c in process.get('children',[]))):
        raise ValueError('the already complete 660-piece joint result or actual child0 receipt changed')
    endpoint=ORIGINAL_LEFT;cap_endpoint=LEFT;selected=[]
    for i,row in enumerate(old['rows']):
        l,r=map(Fraction,row['interval'])
        if l!=endpoint or not l<r:raise ValueError('the original 4650 closed rows are not a complete ordered cover')
        endpoint=r
        lo,hi=max(l,LEFT),min(r,RIGHT)
        if not lo<hi:continue
        if lo!=cap_endpoint:raise ValueError('the exact cap intersections have a gap or overlap')
        gl,gr=map(Fraction,row['actual_scalar_germ'])
        provenance=row.get('intrinsic_provenance',{})
        if (not gl<=l<r<=gr or provenance.get('kind')!='same_intrinsic_cap_v2'
            or not isinstance(provenance.get('row'),int) or provenance['row']<0
            or provenance['row']>=1334 or not provenance.get('part')
            or not all(k in row.get('intrinsic',{}) for k in ('beta','gamma','K'))):
            raise ValueError('a selected closed row has another intrinsic germ or provenance')
        selected.append(dict(original_row_index=i,original_row_sha256=row_sha(row),
            original_interval=list(row['interval']),exact_cap_intersection=[str(lo),str(hi)],
            actual_scalar_germ=list(row['actual_scalar_germ']),
            intrinsic_provenance=dict(provenance),
            intrinsic={k:row['intrinsic'][k] for k in ('beta','gamma','K')}))
        cap_endpoint=hi
    if endpoint!=RIGHT or cap_endpoint!=RIGHT or not selected:
        raise ValueError('the original or selected complete cap does not end at25/8')
    return old,joint,selected

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in EXPECTED:p.add_argument('--'+name.replace('_','-'),type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;started=time.monotonic()
    old,joint,selected=inputs(a)
    input_identity=dict(EXPECTED,exact_cap_interval=['9/10','25/8'],exact_eta=str(ETA),
        original_parameter_half_width='1/1000000000',original_exact_nu=str(NU),
        original_candidate=CANDIDATE,original_intrinsic_cap_cache=CAP_CACHE,
        complete_Z_definition=ZDEF)
    doc=dict(kind=KIND,source_sha256=sha(__file__),input_sha256=input_identity,
        complete=False,failure=None,gates=[],seconds=None,exact_interval=['9/10','25/8'],
        original_complete_row_count=4650,selected_cap_row_count=len(selected),
        original_full_native_sha256=EXPECTED['native'],original_native_bytes=6223338,
        original_four_lossless_parts_only=True,old_target_ODE_FFT_and_repair_recomputations=0,
        completed_new_Bernstein_joint_cells=0,already_complete_joint_cells_reused=660,
        original_joint_summary_sha256=EXPECTED['joint_summary'],
        original_joint_native_sha256=joint['native_sha256'],
        same_intrinsic_cap_v2_complete_rows=True,rows=[],completed_cap_rows=0,
        intrinsic_maxima={k:record(0) for k in ('beta_absolute','gamma_positive','K_positive')},
        maximal_record_rows={k:None for k in ('beta_absolute','gamma_positive','K_positive')},
        scoped_to_original_fixed_eta0=True,whole_original_eta_half_width_also_covers_eta0=True,
        no_new_target_or_intrinsic_coefficient_enclosure_created=True,
        no_new_nonlinear_solution_or_infinite_inverse_claimed=True)
    start=0
    if a.resume:
        previous=read(a.resume)
        if (previous.get('kind')!=KIND or previous.get('source_sha256')!=sha(__file__)
            or previous.get('input_sha256')!=input_identity or previous.get('failure')):
            raise ValueError('preserve an unmatched or failed scientific prefix')
        start=previous.get('completed_cap_rows',-1)
        if (start<0 or start>len(selected) or previous.get('rows')!=selected[:start]
            or previous.get('selected_cap_row_count')!=len(selected)):
            raise ValueError('the exact completed intrinsic prefix is not a true prefix')
        if previous.get('complete'):
            if not previous.get('gates') or not all(g['passed'] for g in previous['gates']):
                raise ValueError('an original complete native has failed gates')
            if a.out.exists() and a.out.read_bytes()!=a.resume.read_bytes():
                raise FileExistsError('preserve another native')
            if a.out!=a.resume:a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(a.resume.read_bytes())
            print(json.dumps(dict(complete=True,already_complete=True,rows=start,new_rows=0)),flush=True);return
        doc=previous
    elif a.out.exists():
        raise FileExistsError('use the exact original scientific prefix explicitly')
    maximum={k:ball(v).upper() for k,v in doc['intrinsic_maxima'].items()}
    doc.update(reused_cap_rows=start,new_cap_rows_this_child=0)
    save(a.out,doc)
    try:
        for i,row in enumerate(selected[start:],start=start):
            beta,gamma,K=(ball(row['intrinsic'][k]) for k in ('beta','gamma','K'))
            if not gamma>0 or not K>0:raise ValueError('the original complete intrinsic positivity is unresolved')
            values=dict(beta_absolute=abs(beta).upper(),gamma_positive=gamma.upper(),K_positive=K.upper())
            for name,x in values.items():
                if x>maximum[name]:
                    maximum[name]=x;doc['maximal_record_rows'][name]=row['original_row_index']
            doc['rows'].append(row);doc['completed_cap_rows']=i+1
            doc['intrinsic_maxima']={k:record(v) for k,v in maximum.items()}
            doc['new_cap_rows_this_child']=i+1-start
            if (i+1)%64==0:
                doc['seconds']=time.monotonic()-started;save(a.out,doc)
                print(json.dumps(dict(completed_cap_rows=i+1,selected_cap_row_count=len(selected))),flush=True)
        kstar=max(arb(1),maximum['K_positive']).upper()
        doc['complete_cap_intrinsic_constants']=dict(
            b_star=record(maximum['beta_absolute']),g_star=record(maximum['gamma_positive']),
            K_star=record(maximum['K_positive']),k_star=record(kstar),
            meanings=dict(b_star='sup_r |beta|',g_star='sup_r gamma',
                K_star='sup_r K',k_star='max(1,sup_r K)'),
            actual_maximal_original_rows=dict(doc['maximal_record_rows']))
        names=[
            'exact_original_four_part_4650_native_restored_without_reproduction',
            'original_complete_positive_native_source_candidate_cache_eta_nu_identical',
            'all4650_original_closed_rows_cover_the_exact_original_interval',
            'every_cap_intersection_is_same_intrinsic_cap_v2_and_same_actual_scalar_germ',
            'selected_closed_rows_cover_exact_9over10_to25over8_without_gap_or_overlap',
            'all_selected_gamma_and_K_intervals_strictly_positive',
            'complete_cap_beta_gamma_K_maxima_are_finite',
            'complete660_joint_source_and_child0_receipt_consumed_without_new_Bernstein_rows',
            'no_old_target_intrinsic_grid_FFT_ODE_repair_or_cap_residual_recomputed']
        if not all(x.is_finite() for x in [*maximum.values(),kstar]):
            raise ValueError('a complete intrinsic maximum is not finite')
        doc['gates']=[dict(name=n,passed=True) for n in names]
        doc['complete']=True
    except Exception as error:
        doc.update(complete=False,failure=dict(type=type(error).__name__,message=str(error)))
        doc['seconds']=time.monotonic()-started;save(a.out,doc);raise
    doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,original_rows=4650,selected_rows=len(selected),
        new_rows=doc['new_cap_rows_this_child'],gates=len(doc['gates']),
        complete_cap_intrinsic_constants=doc['complete_cap_intrinsic_constants'])),flush=True)

if __name__=='__main__':main()
