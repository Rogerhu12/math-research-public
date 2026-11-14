#!/usr/bin/env python3
"""New low193/high97:160 projections of cached actual correlated source rows.

Only saved exact scalar jet enclosures and original physical cubics are
used. No target primitive, mean ODE, original residual norm certificate,
projector or Green port is rerun. A selected pilot is not a full cover.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from bisect import bisect_left,bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_correlated_head_residual_rows import scalar_models,parameter_source
from fourfold_codazzi_correlated_radial_Fourier import candidate_fields,norms
from fourfold_codazzi_nu_full_adjoint_kernel import operator_action
from fourfold_phase_beta_bulk_box import Box,CBox,DirectedFFT

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
OLD_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
REPAIR_SOURCE='05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4'
REPAIR_PROCESS='16de872ce106e05b6add99d8406598de3cc87b94f4533a9fc3bb46294c66366a'
RIGHT=Fraction(25,8);CUT=Fraction(9,10)
PHASE_RIGHT=Fraction(2383968743003,10000000000000)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temp=path.with_suffix(path.suffix+'.partial');temp.write_bytes(raw);temp.replace(path)


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a projected source enclosure is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def actual(process,run_id):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run_id) and process.get('complete')
        and not process.get('failure') and bool(process.get('children'))
        and all(c.get('actual_returncode')==0 for c in process['children']))


def project(field,low,high):
    """Exact Fourier coordinate projection of the complete polynomial/error."""
    if not 0<=low<=high<field.grid//2:raise ValueError('invalid true finite Fourier projection')
    retained_degree=min(high,field.degree)
    if retained_degree<low:return field.coerce(0)
    z=field.Fourier()
    out=CBox(Box(z.real.lo.copy(),z.real.hi.copy()),Box(z.imag.lo.copy(),z.imag.hi.copy()))
    j=np.arange(field.grid);j=np.where(j<field.grid//2,j,j-field.grid)
    out[(abs(j)<low)|(abs(j)>high)]=0
    # Coordinate projections contract Wiener A0. The retained uniform
    # scalar remainder now has exactly the projected finite support.
    error=field.error if field.error_degree>=low else arb(0)
    return field.from_Fourier(out,retained_degree,error,min(retained_degree,field.error_degree))


def budgets(pair,length):
    return {key:record(value) for key,value in norms(pair,length,Fraction(1,2048)).items()}


def row_projection(row,old,repair,background,trial,nodes,alpha,context):
    left,right=map(Fraction,row['interval']);ci=row['pieces']['background'];hi=row['pieces']['response']
    if not (nodes[ci]<=left<right<=nodes[ci+1] and nodes[hi]<=left<right<=nodes[hi+1]):
        raise ValueError('the cached complete scalar row crosses an original cubic piece')
    whole={key:interval(value) for key,value in row['intrinsic_whole_third_jets'].items()}
    midpoint={key:interval(value) for key,value in row['intrinsic_midpoint_jets'].items()}
    scalar=scalar_models(context,left,right,whole,midpoint)
    bg=candidate_fields(background['piece_coefficients'][:,ci],nodes[ci],left,right,32,
        context['grid'],context['fft'],alpha,scalar['s'])
    response=candidate_fields(trial['piece_coefficients'][:,hi],nodes[hi],left,right,96,
        context['grid'],context['fft'])
    Q=(bg[0],bg[1]);h=(response[0],response[1]);hr=(response[4],response[5])
    D=operator_action(Q,h,hr,scalar);F=parameter_source(Q,scalar,left,right)
    R=(D[0]-F[0],(D[1]-F[1]).nonmean())
    zero=Q[0].coerce(0);one=Q[0].coerce(1)
    negcol=operator_action(Q,(zero,one),(zero,zero),scalar)
    column=(-negcol[0],(-negcol[1]).nonmean())
    # The original exact mean error is a genuinely varying scalar.
    # Its whole-interval enclosure is used as a uniform scalar model,
    # without differentiating it or setting the repaired mean to zero.
    ez=interval(old['response_mean_error'])
    corrected=(R[0]-column[0]*ez,R[1]-column[1]*ez)
    if any(field.degree>160 for field in corrected):raise ValueError('an original complete output mode was lost')
    low=tuple(project(field,0,96) for field in corrected)
    high=tuple(project(field,97,160) for field in corrected)
    low_uncorrected=tuple(project(field,0,96) for field in R)
    low_column=tuple(project(field,0,96) for field in column)
    length=right-left;low_bounds=norms(low,length,Fraction(1,2048))
    fee=interval(repair['complete_repair_source_pair_A0_sup']).upper()
    # Both projections of the complete new scalar/finite repair error
    # are bounded by the same full pair A0 fee. The independent new mean
    # belongs to the low state and is retained in this fee.
    repaired_low_sup=(low_bounds['L2_sup']+fee).upper()
    repaired_low_radial=(low_bounds['L2_L2_radial']+exact(length).sqrt()*fee).upper()
    coefficients=[]
    for component,field in enumerate(low):
        z=field.Fourier()
        for j in range(0 if component else 1,97):
            value=z[j].real*(1 if j==0 else 2) if component else z[j].imag*(-2)
            coefficients.append(dict(component=component,mode=j,physical_frequency=4*j,
                physical_sine_or_cosine_amplitude_coefficients=[
                    dict(lower_hex=float(a).hex(),upper_hex=float(b).hex())
                    for a,b in zip(value.lo,value.hi)]))
    return dict(common_row=row['common_row'],interval=row['interval'],pieces=row['pieces'],
        actual_projection_complete=True,
        original_closed_scalar_germ=row['actual_scalar_germ'],
        cached_scalar_row_sha256=sha_row(row),
        same_original_completed_mean_error=old['response_mean_error'],
        original_complete_nonmean_residual_bound=old['response_complete_nonmean_residual'],
        fresh_low193_original_background_nonmean_residual={key:record(value) for key,value in low_bounds.items()},
        fresh_high97_through160_original_background_nonmean_residual=budgets(high,length),
        fresh_low193_uncorrected_trial_residual=budgets(low_uncorrected,length),
        fresh_low193_mean_correction_column=budgets(low_column,length),
        complete_new_repair_source_pair_A0_sup=repair['complete_repair_source_pair_A0_sup'],
        repaired_low193_complete_residual_L2_sup=record(repaired_low_sup),
        repaired_low193_complete_residual_L2_radial=record(repaired_low_radial),
        low193_radial_polynomial_physical_amplitudes=coefficients,
        low_component_uniform_A0_remainders=[record(field.error) for field in low],
        full_angular_support_resolved_before_projection=160,
        source_projection_does_not_discard_unknown_high_inputs=True,
        original_background_completed_mean_residual_exactly_zero=True,
        repaired_background_independent_mean_residual_retained_in_complete_repair_fee=True)


def sha_row(row):
    return hashlib.sha256((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('actual projected-source pilot failed: '+name)
    manifest=read(a.original_manifest);body=read(a.body);bp=read(a.body_process)
    repair=read(a.repair_source);rp=read(a.repair_process)
    gate('all_fixed_original_inputs_and_both_actual_completed_source_processes',
        sha(a.original_manifest)==OLD_MANIFEST and sha(a.candidate)==ORIGINAL and sha(a.response)==TRIAL
        and sha(a.body)==BODY and sha(a.body_process)==BODY_PROCESS and actual(bp,43586413510)
        and sha(a.repair_source)==REPAIR_SOURCE and sha(a.repair_process)==REPAIR_PROCESS
        and actual(rp,43597921732) and body.get('complete') and repair.get('complete')
        and repair.get('complete_common_rows')==7721 and body.get('complete_original_common_cells')==7721
        and body.get('row_identity')==manifest['row_identity'])
    rows=[];parts=[]
    for path in a.parts:
        original=read(path)
        if (original.get('identity')!=manifest['row_identity']
            or original.get('kind')!=manifest['residual_kind']
            or not original.get('selected_cells_complete') or original.get('failure')):
            raise ValueError('an original cached full scalar-jet row part changed')
        first,end=original['selected_indices']
        if [x['common_row'] for x in original['rows']]!=list(range(first,end)):
            raise ValueError('an original cached row range is not exact')
        rows.extend(original['rows']);parts.append(dict(indices=[first,end],sha256=sha(path)))
    rows.sort(key=lambda x:x['common_row'])
    gate('the_exact_original_forty_parts_and_all7721_cached_scalar_rows',
        len(parts)==40 and len(rows)==7721 and [x['common_row'] for x in rows]==list(range(7721)))
    gate('every_original_part_byte_hash_matches_both_completed_body_and_repair_natives',
        sorted(x['sha256'] for x in parts)==sorted(body.get('inputs',{}).values())
        and sorted((tuple(x['indices']),x['sha256']) for x in parts)
            ==sorted((tuple(x['indices']),x['sha256']) for x in repair.get('original_parts',[])))
    background=load_candidate(a.candidate);trial=load_candidate(a.response)
    nodes=[Fraction(float(x)) for x in background['radial_nodes']]
    gate('all_original_physical_cubics_and_full193_response_mean_retained',
        background['piece_coefficients'].shape==(4,6144,65)
        and trial['piece_coefficients'].shape==(4,6144,193)
        and np.array_equal(background['radial_nodes'],trial['radial_nodes'])
        and nodes[0]==0 and nodes[-1]==RIGHT)
    edge=Fraction(0)
    for i,row in enumerate(rows):
        left,right=map(Fraction,row['interval'])
        if (left!=edge or not left<right or row['interval']!=body['residual_rows'][i]['interval']
            or row['interval']!=repair['rows'][i]['interval'] or repair['rows'][i]['common_row']!=i):
            raise ValueError('the original cached mean, scalar and repair partitions disagree')
        edge=right
    gate('the_complete_original_joint_partition_is_unchanged',edge==RIGHT)
    # Ranking is only a reproducible pilot choice, not a proof of a
    # maximum over the body. Every selected exact row index is retained.
    eligible=[i for i,row in enumerate(rows) if Fraction(row['interval'][0])<CUT]
    ranked=sorted(eligible,key=lambda i:float(interval(
        body['residual_rows'][i]['response_complete_nonmean_residual']['L2_L2_radial']).upper()),reverse=True)
    selected=set(ranked[:8]);lefts=[Fraction(row['interval'][0]) for row in rows]
    for radius in (Fraction(0),Fraction(1,20),Fraction(9,50),PHASE_RIGHT,Fraction(1,2),CUT):
        index=(bisect_left(lefts,radius)-1 if radius==CUT else bisect_right(lefts,radius)-1)
        selected.add(index)
    selected=sorted(selected)
    context=dict(grid=512,fft=DirectedFFT())
    alpha=exact(Fraction(manifest['row_identity']['exact_alpha']))
    doc.update(selected_original_rows=selected,selection_only_float_rank_of_existing_bounds=True,
        all_original_parts=parts,original_target_primitives_rerun=0,
        original_mean_flows_recomputed=0,original_complete_residual_certificates_unchanged=True,
        scalar_jets_reused_from_original_actual_rows=True,rows=[])
    if a.resume:
        prior=read(a.resume)
        if (prior.get('kind')!=doc['kind'] or prior.get('source_sha256')!=doc['source_sha256']
            or prior.get('input_sha256')!=doc['input_sha256']
            or prior.get('selected_original_rows')!=selected):
            raise ValueError('a projected-source prefix has a different mathematical identity')
        saved=prior.get('rows',[])
        if [x['common_row'] for x in saved]!=selected[:len(saved)]:
            raise ValueError('the actual projected-source prefix is not ordered and complete')
        for result in saved:
            if (not result.get('actual_projection_complete')
                or result['cached_scalar_row_sha256']!=sha_row(rows[result['common_row']])):
                raise ValueError('a previously completed projected-source cell changed')
        doc['rows']=saved
        doc['original_prefix_provenance']=dict(native_sha256=sha(a.resume),
            original_complete=prior.get('complete'),original_failure=prior.get('failure'),
            actual_completed_selected_rows=len(saved),no_completed_selected_cell_rerun=True)
    for i in selected[len(doc['rows']):]:
        tick=time.monotonic()
        result=row_projection(rows[i],body['residual_rows'][i],repair['rows'][i],
            background,trial,nodes,alpha,context)
        result['seconds']=time.monotonic()-tick;doc['rows'].append(result);save(a.out,doc)
        print(json.dumps(dict(actual_selected_row=i,
            low193_L2_sup=result['repaired_low193_complete_residual_L2_sup']['upper'],
            old_full160_L2_sup=result['original_complete_nonmean_residual_bound']['L2_sup']['upper'],
            seconds=result['seconds'])),flush=True)
    gate('every_new_selected_low193_and_high97_to160_source_projection_completed',
        [x['common_row'] for x in doc['rows']]==selected)
    doc.update(complete=True,selected_cells_complete=True,complete_body_projection_cover=False,
        original_candidate_sha256=ORIGINAL,original_full_physical_trial_sha256=TRIAL,
        original_body_and_mean_native_sha256=BODY,actual_complete_repair_source_native_sha256=REPAIR_SOURCE,
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        actual_finite193_response_error_bound_proved=False,complete_infinite_inverse_proved=False,
        true_parameter_Schur_proved=False,
        all_original_target_tails_and_independent_mean_retained=True,
        unknown_high_input_feedback_not_removed_by_projecting_known_source=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('original-manifest','candidate','response','body','body-process','repair-source','repair-process','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--parts',type=Path,nargs='+',required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual selected projected-source outcome')
    doc=dict(kind='actual_cached_scalar_jet_known_low193_residual_projection_pilot_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),rows=[],
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in
            ('original-manifest','candidate','response','body','body-process','repair-source','repair-process')},
        complete_body_projection_cover=False,actual_finite193_response_error_bound_proved=False,
        complete_infinite_inverse_proved=False,true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],selected_rows=len(doc['rows']),
        seconds=doc['seconds'],complete_body_projection_cover=False)),flush=True)


if __name__=='__main__':main()
