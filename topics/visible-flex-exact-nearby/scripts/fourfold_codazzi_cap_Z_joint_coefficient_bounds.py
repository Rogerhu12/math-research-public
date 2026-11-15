#!/usr/bin/env python3
"""Exact cap coefficientwise Bernstein bounds for the original full193 Z.

Only two original raw cubic shards and the already certified complete
repair suprema are read. No target, ODE, FFT, repair, or old cap cell is
recomputed. Radial suprema are taken separately for every Fourier mode
before summation. The physical even mean and all96 pairs remain.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,os,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx

KIND='actual_complete_cap_full193_Z_joint_coefficient_suprema_v1'
INDEX='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
DIRECTION='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88'
ZDEF='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
CENTRE='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
WIDTHS=(Fraction(0),Fraction(1,256),Fraction(1,128),Fraction(1,64))
PARTS={
 'response-full-part012.npz.gz':('777337c853329f26719b148e34db079c5ca0ed34991aa40220f25624e4af0b3c',2698989,5436,5889),
 'response-full-part013.npz.gz':('4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037',1517845,5889,6144)}
FREQUENCY=tuple(4*j for j in range(1,97))+(0,)+tuple(4*j for j in range(1,97))

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(value):
    return hashlib.sha256((json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_bytes(raw);os.replace(tmp,path)
def f64(value):return Fraction.from_float(float(value))
def ball(value):
    q=Fraction(value)
    return arb(q.numerator)/arb(q.denominator)
def record(value):
    value=arb(value)
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def gate(doc,name,condition):
    ok=bool(condition);doc['gates'].append(dict(name=name,passed=ok))
    if not ok:raise ValueError(name)

def exact_Bernstein_bound(descending,x0,length):
    """Same exact polynomial restricted to x=x0+length*t, 0<=t<=1."""
    c3,c2,c1,c0=map(f64,descending)
    p0=((c3*x0+c2)*x0+c1)*x0+c0
    p1=length*((3*c3*x0+2*c2)*x0+c1)
    p2=length*length*(3*c3*x0+c2)
    p3=length**3*c3
    bernstein=(p0,p0+p1/3,p0+2*p1/3+p2/3,p0+p1+p2+p3)
    return max(map(abs,bernstein))

def complete_parts(index,parts_dir):
    selected=[];previous=0
    if index['kind']!='complete_lossless_radial_cubic_shards_v1':
        raise ValueError('the original lossless full193 index is required')
    if (index['coefficient_shape']!=[4,6144,193] or index['radial_nodes_count']!=6145
        or index['polynomial_order']!='numpy/scipy PPoly descending local powers'):
        raise ValueError('the original complete physical cubic schema changed')
    for part in index['parts']:
        if Path(part['file']).name!=part['file'] or part['first_interval']!=previous:
            raise ValueError('the original global shard index lost its exact ordered coverage')
        previous=part['last_interval_exclusive']
        if f64(part['radial_left'])<RIGHT and f64(part['radial_right'])>LEFT:
            selected.append(part)
    if previous!=6144 or [p['file'] for p in selected]!=list(PARTS):
        raise ValueError('the complete cap does not use exactly the two original pinned shards')
    cells=[];last_node=None
    for part in selected:
        h,size,first,end=PARTS[part['file']]
        if (part['sha256'],part['bytes'],part['first_interval'],part['last_interval_exclusive'])!=(h,size,first,end):
            raise ValueError('one original cap shard index entry changed')
        path=parts_dir/part['file']
        if path.stat().st_size!=size or digest(path)!=h:
            raise ValueError('one complete original cap cubic shard is absent or changed')
        with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
            if set(z.files)!={'radial_nodes','piece_coefficients'}:
                raise ValueError('an original cap shard has different scientific arrays')
            nodes=z['radial_nodes'];coeff=z['piece_coefficients']
        if (nodes.dtype!=np.dtype('float64') or coeff.dtype!=np.dtype('float64')
            or nodes.shape!=(end-first+1,) or coeff.shape!=(4,end-first,193)
            or not np.isfinite(nodes).all() or not np.isfinite(coeff).all()
            or not np.all(np.diff(nodes)>0)):
            raise ValueError('one full193 cap cubic array has the wrong exact shape or values')
        exact_nodes=list(map(f64,nodes))
        if exact_nodes[0]!=f64(part['radial_left']) or exact_nodes[-1]!=f64(part['radial_right']):
            raise ValueError('the original shard boundary does not match its exact index')
        if last_node is not None and exact_nodes[0]!=last_node:
            raise ValueError('the two original cap shards have different exact shared nodes')
        last_node=exact_nodes[-1]
        for j in range(end-first):
            lo,hi=max(LEFT,exact_nodes[j]),min(RIGHT,exact_nodes[j+1])
            if lo<hi:cells.append((first+j,lo,hi,exact_nodes[j],coeff[:,j,:],h))
    cursor=LEFT
    for _,lo,hi,_,_,_ in cells:
        if lo!=cursor or not lo<hi:raise ValueError('the actual cap cubic restrictions have a gap or overlap')
        cursor=hi
    if cursor!=RIGHT or not cells:raise ValueError('the exact complete cap was not covered')
    return selected,cells

def joint_bounds(coefficients):
    result={}
    for width in WIDTHS:
        weights=[(ball(width*k)).exp() for k in FREQUENCY]
        result[str(width)]={}
        for order in range(3):
            factors=[weights[i]*(k**order if order else 1) for i,k in enumerate(FREQUENCY)]
            first=sum((ball(coefficients[i])*factors[i] for i in range(96)),arb(0))
            second=sum((ball(coefficients[i])*factors[i] for i in range(96,193)),arb(0))
            result[str(width)][str(order)]=dict(xi=record(first.upper()),zeta=record(second.upper()),
                complete_pair=record((first+second).upper()))
    return result

def run(a,doc):
    gate(doc,'same_original_full193_physical_trial_index',digest(a.index)==INDEX)
    gate(doc,'same_already_complete_continuous_Z_repair_certificate',digest(a.direction_native)==DIRECTION)
    index,direction=read(a.index),read(a.direction_native)
    meta=index['metadata']
    gate(doc,'physical_unnormalized193_trial_no_alpha_or_mean_projection',
        meta['role']=='response_full' and meta['modes']==96 and meta['physical_frequency_factor']==4
        and meta['background_candidate_sha256']==CANDIDATE
        and meta['original_full_state_preserved']
        and not meta['exact_zero_mean_projection_for_separate_scalar_completion'])
    gate(doc,'same_complete_Z_definition_and_repaired_centre',
        direction['complete'] and direction['original_trial_sha256']==INDEX
        and direction['derived_direction_definition_sha256']==ZDEF
        and direction['background_definition_sha256']==CENTRE
        and direction['gates'] and all(g['passed'] for g in direction['gates']))
    offset=list(map(Fraction,direction['exact_complete_repair_coefficient_suprema']))
    gate(doc,'all193_original_complete_offset_suprema_including_even_mean',
        len(offset)==193 and all(q>=0 for q in offset))
    selected,cells=complete_parts(index,a.parts_dir)
    identity=dict(index=INDEX,direction=DIRECTION,
        selected_original_shards={p['file']:p['sha256'] for p in selected},
        exact_domain=[str(LEFT),str(RIGHT)],complete_direction_definition=ZDEF)
    doc.update(input_sha256=identity,selected_original_cap_parts=selected,
        requested_cap_piece_count=len(cells),actual_first_piece=cells[0][0],
        actual_last_piece=cells[-1][0],exact_interval=[str(LEFT),str(RIGHT)])
    maxima=[Fraction(0)]*193;maximizing=[None]*193;rows=[];old_count=0
    if a.resume:
        old=read(a.resume)
        gate(doc,'resumed_prefix_exact_scientific_identity',
            old['kind']==KIND and old['source_sha256']==digest(__file__) and old['input_sha256']==identity
            and 0<=old.get('completed_cap_piece_count',-1)<=len(cells))
        rows=old['rows'];old_count=len(rows)
        if old_count!=old['completed_cap_piece_count'] or old_count>len(cells):
            raise ValueError('the saved prefix count changed')
        maxima=list(map(Fraction,old['exact_raw_coefficientwise_radial_supremum_upper']))
        maximizing=old['maximizing_piece_per_raw_coefficient']
        if len(maxima)!=193 or len(maximizing)!=193 or any(x<0 for x in maxima):
            raise ValueError('the saved complete coefficient maxima changed')
        for row,cell in zip(rows,cells):
            piece,lo,hi,_,_,h=cell
            if (row['piece']!=piece or row['interval']!=[str(lo),str(hi)]
                or row['original_shard_sha256']!=h or not row['complete']
                or len(row['exact193_Bernstein_bound_sha256'])!=64):
                raise ValueError('one previously completed cap restriction has another identity')
        doc['original_prefix_native_sha256']=digest(a.resume)
        doc['original_prefix_failure_preserved']=old.get('failure')
    doc.update(rows=rows,completed_cap_piece_count=old_count,
        exact_raw_coefficientwise_radial_supremum_upper=list(map(str,maxima)),
        maximizing_piece_per_raw_coefficient=maximizing,
        reused_complete_cap_pieces=old_count,new_complete_cap_pieces=0)
    save(a.out,doc)
    for cell in cells[old_count:]:
        piece,lo,hi,node,coeff,h=cell
        bounds=[exact_Bernstein_bound(coeff[:,k],lo-node,hi-lo) for k in range(193)]
        for k,value in enumerate(bounds):
            if maximizing[k] is None or value>maxima[k]:
                maxima[k]=value;maximizing[k]=piece
        rows.append(dict(complete=True,piece=piece,interval=[str(lo),str(hi)],
            original_shard_sha256=h,exact193_Bernstein_bound_sha256=canonical(list(map(str,bounds))),
            exact_restricted_degree=3,physical_even_mean_index=96))
        doc.update(completed_cap_piece_count=len(rows),
            exact_raw_coefficientwise_radial_supremum_upper=list(map(str,maxima)),
            maximizing_piece_per_raw_coefficient=maximizing,new_complete_cap_pieces=len(rows)-old_count)
        if (len(rows)-old_count)%32==0:
            save(a.out,doc);print(json.dumps(dict(cap_pieces=len(rows),total=len(cells))),flush=True)
    gate(doc,'every_original_cap_cubic_piece_consumed_once_on_exact_closed_domain',
        len(rows)==len(cells) and rows[0]['interval'][0]==str(LEFT) and rows[-1]['interval'][1]==str(RIGHT))
    complete=[a+b for a,b in zip(maxima,offset)]
    doc.update(exact_complete_repair_coefficient_suprema=list(map(str,offset)),
        exact_complete_Z_coefficientwise_radial_supremum_upper=list(map(str,complete)),
        raw_joint_homogeneous_angular_derivative_norms=joint_bounds(maxima),
        repair_joint_homogeneous_angular_derivative_norms=joint_bounds(offset),
        complete_Z_joint_homogeneous_angular_derivative_norms=joint_bounds(complete),
        exact_complete_Z_mean_absolute_upper=str(complete[96]),
        exact_complete_Z_pair_A0_upper=str(sum(complete,Fraction(0))),
        physical_frequency_per_state=list(FREQUENCY),
        angular_state_order='odd sine j1..96; true even mean; even cosine j1..96',
        no_extra_alpha_or_sqrt2_factor=True,
        homogeneous_derivative_zero_mode='retained for order0; exactly zero for orders1and2',
        joint_norm_order='sum over Fourier coefficients after each complete cap radial supremum',
        all_original_repair_target_FFT_ODE_and_cap_residual_recomputations=0,
        fixed_physical_parameter='eta0 and original nu0; same exact physical full193 Z',
        coordinate='original moving phi; no unknown-changing-angle composition claimed',
        ordinary_row_suprema_not_relabelled_as_joint=True,
        nonlinear_solution_or_full_infinite_inverse_claimed=False,
        intrinsic_beta_gamma_K_bounds_consumed=False,
        intrinsic_bound_scope='this first consumer only pays the complete cap Z coefficient norms')
    gate(doc,'all_four_exact_widths_and_all_three_complete_angular_orders',
        set(doc['complete_Z_joint_homogeneous_angular_derivative_norms'])==set(map(str,WIDTHS))
        and all(set(v)=={'0','1','2'} for v in doc['complete_Z_joint_homogeneous_angular_derivative_norms'].values()))
    gate(doc,'full193_independent_even_mean_and_both_reflected_components_preserved',len(complete)==193)
    gate(doc,'new_joint_bounds_finite_in_all_requested_domains',
        all(arb(z['upper']).is_finite()
            for width in doc['complete_Z_joint_homogeneous_angular_derivative_norms'].values()
            for order in width.values() for z in order.values()))
    gate(doc,'old_successful_repair_target_and_cap_residuals_not_recomputed',True)
    doc['complete']=True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('index','parts-dir','direction-native','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--resume',type=Path);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve every actual cap-joint native and prefix')
    ctx.prec=320;ctx.cap=6;start=time.monotonic()
    doc=dict(kind=KIND,source_sha256=digest(__file__),complete=False,failure=None,gates=[],
        arithmetic_bits=320,rows=[],completed_cap_piece_count=0,
        all_original_repair_target_FFT_ODE_and_cap_residual_recomputations=0,
        nonlinear_solution_or_full_infinite_inverse_claimed=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:
        doc['seconds']=time.monotonic()-start;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],pieces=doc['completed_cap_piece_count'],
        original_piece_first=doc['actual_first_piece'],original_piece_last=doc['actual_last_piece'],
        gates=len(doc['gates']),seconds=doc['seconds'],
        complete_pair_A0=doc.get('exact_complete_Z_pair_A0_upper'))),flush=True)

if __name__=='__main__':main()
