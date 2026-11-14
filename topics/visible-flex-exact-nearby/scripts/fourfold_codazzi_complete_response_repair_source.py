#!/usr/bin/env python3
"""Pay the exact original-centre repair in the known complete response source.

Every scalar target enclosure and every completed scalar mean is reused
from the actual original complete body result. Only Bernstein coefficient
norms of the original saved cubics and the new explicit difference fees
are computed. The original residuals, mean flows and trial data are never
rerun or relabelled. This is a source certificate, not a response inverse.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_beta_bulk_box import Box,arb_box,reduce_box,scalar_arb

BODY='a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870'
BODY_PROCESS='0a5dc06520bad5a1230b65cba6e895e998e1f3ce6a32a65d9ffa8800b8ea1a9e'
ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
TRIAL='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6'
REPAIR_NATIVE='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
REPAIR_DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
ORIGINAL_MANIFEST='c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784'
CONTROL_LEFT=Fraction(1,20);CONTROL_RIGHT=Fraction(9,50)
RIGHT=Fraction(25,8);CUT=Fraction(9,10)
NORMS=('L2','H_one_third','H1')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2]==b'\x1f\x8b' else data)


def save(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def q(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def norm(value):return abs(arb(value)).upper()


def record(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a new complete repair-source bound is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def cubic_pair_norms(cube,knot,left,right,modes,scale=Fraction(1),reference=arb(0)):
    """Complete cubic Bernstein hull, every real amplitude and true mean."""
    if cube.shape!=(4,2*modes+1) or not knot<=left<right:
        raise ValueError('the full original polynomial support or radial order changed')
    x=arb_box(q(left-knot));h=arb_box(q(right-left))
    c0,c1,c2,c3=(Box(cube[j]) for j in range(4))
    a0=((c0*x+c1)*x+c2)*x+c3
    a1=((3*c0*x+2*c1)*x+c2)*h
    a2=(3*c0*x+c1)*h*h
    a3=c0*h*h*h
    bernstein=(a0,a0+a1/3,a0+(2*a1+a2)/3,a0+a1+a2+a3)
    lower=np.minimum.reduce([value.lo for value in bernstein])
    upper=np.maximum.reduce([value.hi for value in bernstein])
    amplitude=np.maximum(abs(lower),abs(upper))
    if not np.isfinite(amplitude).all():raise ArithmeticError('a complete cubic coefficient hull is nonfinite')
    freq=np.array([4*j for j in range(1,modes+1)]+[0]+[4*j for j in range(1,modes+1)],dtype=np.float64)
    zero=(abs(q(scale))*scalar_arb(reduce_box(Box(amplitude)))).upper()+norm(reference)
    first=(abs(q(scale))*scalar_arb(reduce_box(Box(amplitude)*Box(freq)))).upper()
    mean=(abs(q(scale))*arb(float(amplitude[modes]))+norm(reference)).upper()
    return zero.upper(),first.upper(),mean


def operator_fee(beta,gamma,K,Q0,Q1,E0,E1,mean_e,H0,H1):
    """A genuine first-order operator difference applied to a known trial."""
    B,G=norm(beta),norm(gamma);Kstar=max(arb(1),norm(K)).upper()
    deltaS=(Kstar*(2*Q0*E0+E0*E0)).upper()
    M1=(B*deltaS/4+G*Kstar*mean_e).upper()
    M0=(3*B*deltaS+B*Kstar*(E0*Q1+(Q0+E0)*E1)/2+G*Kstar*E1).upper()
    return (M1*H1+M0*H0).upper(),M0,M1


def parameter_fee(left,right,jets,Q0,Q1,mean_Q,E0,E1,mean_e):
    if right<=CONTROL_LEFT or left>=CONTROL_RIGHT:
        return arb(0),dict(compact_parameter_source_exactly_zero=True)
    if not CONTROL_LEFT<=left<right<=CONTROL_RIGHT:
        raise ValueError('an original compact parameter-source seam was crossed')
    beta,gamma,K,a=(interval(jets[name]) for name in ('beta','gamma','K','a'))
    if not gamma.lower()>0 or not a.lower()>0:
        raise ValueError('the complete original metric coefficient denominator is not separated')
    # w=4096[t(1-t)]^6, 0<=t<=1. Exactly |w|<=1 and
    # |w_r|<=24/(CONTROL_RIGHT-CONTROL_LEFT); no sampled extrema.
    wr=q(Fraction(24)/(CONTROL_RIGHT-CONTROL_LEFT))
    T=beta/(2*gamma*gamma*a*a)
    Kn=(norm(K)+norm(T)*wr).upper()
    Cn=max((Kn+norm(K)/2).upper(),arb(1)/2).upper()
    square_change=(2*Q0*E0+E0*E0).upper()
    square_after=((Q0+E0)*(Q0+E0)).upper()
    fee=(norm(beta)*Kn*(square_change*Q1/4+square_after*E1/4
                           +square_change*Q0+square_after*E0)
         +norm(gamma)*Cn*(mean_e*Q1+(mean_Q+mean_e)*E1)).upper()
    return fee,dict(compact_parameter_source_exactly_zero=False,
        exact_compact_interval=[str(CONTROL_LEFT),str(CONTROL_RIGHT)],
        exact_global_compact_weight_upper='1',exact_global_weight_derivative_upper=str(Fraction(24)/(CONTROL_RIGHT-CONTROL_LEFT)),
        original_complete_Knu_upper=record(Kn),original_complete_Jnu_upper=record(Cn),
        no_reference_s_nu_direction_added=True)


def run(a,doc):
    def gate(name,ok):
        doc['gates'].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError('complete known-response repair input failed: '+name)
    original=read(a.original_manifest);body=read(a.body);process=read(a.body_process);repair=read(a.repair)
    gate('same_original_full_body_manifest_and_actual_complete_mean_process',
        sha(a.original_manifest)==ORIGINAL_MANIFEST and sha(a.body)==BODY
        and sha(a.body_process)==BODY_PROCESS and body.get('complete') and not body.get('failure')
        and process.get('complete') and not process.get('failure')
        and str(process.get('run_id'))=='43586413510'
        and process.get('repository')=='Rogerhu12/math-research-public'
        and process.get('complete_native_sha256')==BODY
        and process.get('children') and all(child.get('actual_returncode')==0 for child in process['children'])
        and body.get('row_identity')==original['row_identity']
        and body.get('complete_original_common_cells')==7721
        and body.get('complete_mean_residuals_exactly_zero')
        and body.get('all_original_nonmean_PPoly_jumps_retained'))
    gate('same_distinct_exact_complete_centre_repair_and_independent_mean',
        sha(a.repair)==REPAIR_NATIVE and repair.get('complete')
        and repair.get('candidate_sha256')==ORIGINAL
        and repair.get('derived_definition_sha256')==REPAIR_DEFINITION
        and repair.get('exact_interface_count')==6143
        and repair.get('corrected_value_and_all_angular_derivatives_continuous')
        and len(repair.get('gates',[]))==6 and all(x['passed'] for x in repair['gates']))
    gate('original_complete_candidate_and_physical_response_trial_bytes',
        sha(a.candidate)==ORIGINAL and sha(a.response)==TRIAL)
    centre=load_candidate(a.candidate);trial=load_candidate(a.response)
    cmeta=json.loads(str(centre['metadata']));hmeta=json.loads(str(trial['metadata']))
    cnodes=[Fraction(float(x)) for x in centre['radial_nodes']]
    hnodes=[Fraction(float(x)) for x in trial['radial_nodes']]
    gate('all_original_6144_pieces_65_background_and_193_physical_response_states',
        centre['piece_coefficients'].shape==(4,6144,65)
        and trial['piece_coefficients'].shape==(4,6144,193)
        and cnodes==hnodes and len(cnodes)==6145 and cnodes[0]==0 and cnodes[-1]==RIGHT
        and hmeta.get('background_candidate_sha256')==ORIGINAL
        and hmeta.get('finite_head_mean_was_not_removed_from_the_solve') is True)
    alpha=Fraction(original['row_identity']['exact_alpha'])
    gate('same_exact_physical_alpha_and_zero_waist_repair',
        Fraction(cmeta['exact_float_amplitude'])==alpha
        and Fraction(repair['definition']['exact_alpha'])==alpha
        and all(Fraction(x)==0 for x in repair['special_piece_offsets']['0']['physical_offset']))
    E0=q(repair['exact_maximum_piece_pair_Ak']['0']).upper()
    E1=q(repair['exact_maximum_piece_pair_Ak']['1']).upper()
    mean_e=q(repair['exact_maximum_mean_correction']).upper()
    rows=[];parts=[]
    for path in a.parts:
        source=read(path)
        gate('original_complete_row_part_'+str(source.get('selected_indices')),
            source.get('kind')==original['residual_kind']
            and source.get('identity')==original['row_identity']
            and source.get('selected_cells_complete') and source.get('failure') is None)
        first,end=source['selected_indices']
        if [row['common_row'] for row in source['rows']]!=list(range(first,end)):
            raise ValueError('an original completed part has a gap or repeated row')
        rows.extend(source['rows']);parts.append(dict(indices=[first,end],sha256=sha(path)))
    rows.sort(key=lambda row:row['common_row'])
    gate('exact_original_40_parts_7721_row_cover',len(parts)==40 and len(rows)==7721
        and [row['common_row'] for row in rows]==list(range(7721))
        and len(body.get('residual_rows',[]))==7721)
    factors={'L2':arb(1),'H_one_third':(q(1+640**2).log()/6).exp(),'H1':q(1+640**2).sqrt()}
    fees={name:arb(0) for name in ('delta_operator','delta_parameter','complete_repair')}
    repaired={name:arb(0) for name in NORMS};maxima={name:arb(0) for name in fees}
    norms_max={name:arb(0) for name in ('background_A0','background_angle_A0','response_star_A0','response_angle_A0')}
    result=[];edge=Fraction(0)
    for i,row in enumerate(rows):
        left,right=map(Fraction,row['interval']);old=body['residual_rows'][i]
        if left!=edge or not left<right or old['common_row']!=i or old['interval']!=row['interval']:
            raise ValueError('the original complete residual/mean intervals do not agree')
        ci,hi=row['pieces']['background'],row['pieces']['response']
        if not (cnodes[ci]<=left<right<=cnodes[ci+1] and hnodes[hi]<=left<right<=hnodes[hi+1]):
            raise ValueError('a complete original cubic restriction crossed its true piece')
        jets=row['intrinsic_whole_third_jets']
        Q0,Q1,m=cubic_pair_norms(centre['piece_coefficients'][:,ci],cnodes[ci],left,right,32,alpha,interval(jets['s']))
        H0,H1,_=cubic_pair_norms(trial['piece_coefficients'][:,hi],hnodes[hi],left,right,96)
        H0=(H0+norm(interval(old['response_mean_error']))).upper()
        op,M0,M1=operator_fee(interval(jets['beta']),interval(jets['gamma']),interval(jets['K']),
            Q0,Q1,E0,E1,mean_e,H0,H1)
        param,pdata=parameter_fee(left,right,jets,Q0,Q1,m,E0,E1,mean_e)
        total=(op+param).upper();length=q(right-left)
        for name,value in zip(('delta_operator','delta_parameter','complete_repair'),(op,param,total)):
            fees[name]+=length*value*value;maxima[name]=max(maxima[name],value).upper()
        for name,value in zip(norms_max,(Q0,Q1,H0,H1)):norms_max[name]=max(norms_max[name],value).upper()
        complete={}
        for name in NORMS:
            old_bounds=old['response_complete_nonmean_residual']
            extra=(factors[name]*total).upper()
            sup=(interval(old_bounds[name+'_sup']).upper()+extra).upper()
            radial=(interval(old_bounds[name+'_L2_radial']).upper()+length.sqrt()*extra).upper()
            complete[name+'_sup']=record(sup);complete[name+'_L2_radial']=record(radial);repaired[name]+=radial*radial
        result.append(dict(common_row=i,interval=row['interval'],
            original_candidate_piece=ci,original_response_piece=hi,
            complete_original_scalar_germ=row['actual_scalar_germ'],
            original_body_row_sha256=hashlib.sha256((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest(),
            original_background_pair_A0=record(Q0),original_background_angular_derivative_pair_A0=record(Q1),
            complete_mean_corrected_response_pair_A0=record(H0),complete_response_angular_derivative_pair_A0=record(H1),
            first_order_operator_difference_M1=record(M1),zero_order_operator_difference_M0=record(M0),
            delta_operator_applied_to_known_response_pair_A0_sup=record(op),
            delta_parameter_source_pair_A0_sup=record(param),complete_repair_source_pair_A0_sup=record(total),
            complete_repaired_background_response_residual=complete,
            complete_difference_fourier_support=160,parameter_source_identity=pdata,
            independent_even_mean_included=True,new_repaired_response_mean_residual_set_to_zero=False))
        edge=right
        if (i+1)%256==0:
            doc['rows']=result;doc['actual_completed_common_rows']=i+1;save(a.out,doc)
            print(json.dumps(dict(actual_repair_source_rows=i+1,total=7721)),flush=True)
    gate('whole_original_body_including_the_complete_positive_cap',edge==RIGHT)
    doc.update(complete=True,rows=result,complete_common_rows=7721,exact_interval=['0','25/8'],
        original_parts=parts,original_body_and_mean_native_sha256=BODY,
        complete_repair_source_L2_radial={name:record(value.sqrt().upper()) for name,value in fees.items()},
        complete_repair_source_sup={name:record(value) for name,value in maxima.items()},
        complete_repaired_response_residual_L2_radial={name:record(value.sqrt().upper()) for name,value in repaired.items()},
        whole_original_known_state_bounds={name:record(value) for name,value in norms_max.items()},
        exact_centre_repair_bounds={name:record(value) for name,value in dict(A0=E0,angular_A0=E1,mean=mean_e).items()},
        exact_affine_parameter_offset='0',physical_parameter='fixed original physical eta0 and nu',
        original_candidate_sha256=ORIGINAL,derived_continuous_centre_definition_sha256=REPAIR_DEFINITION,
        original_full_physical_response_trial_sha256=TRIAL,
        true_complete_mean_correction_retained=True,all_original_nonmean_trial_jumps_still_required=True,
        original_waist_centre_and_its_amplitude_boundary_exactly_unchanged=True,
        entire_repaired_parameter_source_paid=True,original_target_primitives_rerun=0,
        original_residual_rows_recomputed=0,original_mean_flows_recomputed=0,
        actual_full_PDE_response_error_proved=False,complete_continuous_inverse_proved=False,
        full_high_input_feedback_and_true_regular_boundary_fees_still_required=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('original-manifest','candidate','response','body','body-process','repair','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--parts',nargs='+',type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual known-response centre-repair outcome')
    document=dict(kind='actual_complete_original_to_repaired_known_response_source_v1',
        complete=False,failure=None,gates=[],rows=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in
            ('original-manifest','candidate','response','body','body-process','repair')},
        first_order_principal_mean_change_not_called_L2_bounded=True,
        actual_full_PDE_response_error_proved=False,complete_continuous_inverse_proved=False)
    try:run(a,document)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:document['seconds']=time.monotonic()-started;save(a.out,document)
    print(json.dumps(dict(complete=True,rows=7721,seconds=document['seconds'],
        complete_repair_L2=document['complete_repair_source_L2_radial']['complete_repair']['upper'])),flush=True)


if __name__=='__main__':main()
