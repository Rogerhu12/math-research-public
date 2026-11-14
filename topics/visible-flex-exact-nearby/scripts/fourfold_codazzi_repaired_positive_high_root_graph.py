#!/usr/bin/env python3
"""Glue the two already certified repaired positive high blocks in one Z frame."""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

COLLAR_PROCESS='7ac4224cf5260137e98e941b9816baf06058025ef0c1963b47098f2f4a1ae25c'
COLLAR_NATIVE='86d31a375d6ee07f3919cae565dc16e47361f24cbcd6ee3ef2df8b4f23946605'
COLLAR_SOURCE='5a0f191b11d64169aad8eccdaeb3fc428977b51e3a1ca797602eee1d7c7c0add'
BODY_PROCESS='459745352095624995f1a4c0864eb1e6dec7de5eff87c54ec1f2e3fce5ea99f1'
BODY_SUMMARY='fde40b46beb474e10a92e6f6b92bc93beecb91da33eefc073a72dbc60964a9a5'
BODY_NATIVE='eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68'
BODY_SOURCE='8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
INPUT_ORDER=('root_stable_Z_port','collar_ordinary_Hthird_source',
    'body_ordinary_Hthird_source','body_outer_mean_head_and_weighted_jumps',
    'collar_weighted_affine_jumps','cut_stable_Z_jump','cut_unstable_Z_jump')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def q(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator
def interval(v):return arb(v['lower']).lower().union(arb(v['upper']).upper())
def upper(v):
    value=interval(v).upper()
    if not value.is_finite() or not value>=0:raise ValueError('invalid saved positive upper coefficient')
    return value
def rec(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('nonfinite positive graph coefficient')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)


def run(a,doc):
    def gate(name,passed):
        doc['gates'].append(dict(name=name,passed=bool(passed)))
        if not passed:raise ValueError('actual positive high interface failed: '+name)
    collar=read(a.collar_process);body=read(a.body_summary);process=read(a.body_process)
    gate('exact_published_process_and_summary_bytes_of_both_actual_successes',
        sha(a.collar_process)==COLLAR_PROCESS and sha(a.body_process)==BODY_PROCESS
        and sha(a.body_summary)==BODY_SUMMARY)
    gate('actual_complete_repaired_collar_23_gates_and_native_identity',
        collar.get('complete') and collar.get('public_repository')=='Rogerhu12/math-research-public'
        and str(collar.get('run_id'))=='43600926806' and collar.get('actual_returncode')==0
        and collar.get('native_sha256')==COLLAR_NATIVE
        and collar.get('mathematical_source_sha256')==COLLAR_SOURCE
        and collar.get('mathematical_complete') and len(collar.get('mathematical_gates',[]))==23
        and all(g['passed'] for g in collar['mathematical_gates']))
    gate('actual_complete_repaired_body_8_gates_and_native_and_summary_identity',
        process.get('complete') and not process.get('failure')
        and process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))=='43601149891'
        and process.get('complete_native_sha256')==BODY_NATIVE
        and len(process.get('children',[]))==2
        and all(c.get('actual_returncode')==0 for c in process['children'])
        and any(f.get('logical_file')=='evidence/repaired-complete-positive-N97-high-inverse-summary.json'
            and f.get('sha256')==BODY_SUMMARY for f in process.get('native_files',[]))
        and body.get('native_sha256')==BODY_NATIVE and body.get('source_sha256')==BODY_SOURCE
        and body.get('complete') and not body.get('failure')
        and len(body.get('gates',[]))==8 and all(g['passed'] for g in body['gates']))
    gate('same_M32_repair_global_reference_and_actual_fixed_cut_all4650_rows',
        body.get('original_candidate_sha256')==CANDIDATE
        and body.get('derived_definition_sha256')==REPAIR
        and body.get('exact_affine_parameter_offset')=='0'
        and body.get('exact_radial_interval')==['1192029371497/5000000000000','25/8']
        and body.get('complete_original_rows')==4650
        and body.get('original_right_interfaces_preserved')==3594
        and body['genuine_global_reference']['g_initial']=='M^-1/3 at the genuine root'
        and body['genuine_global_reference']['p_final']=='q_star/(-m_repaired(R))'
        and body['genuine_global_reference']['interior_g_zero_is_only_a_lower_comparison']
        and collar['uniform_positive_extension_reference']['same_reference_at_body_cut'])
    order=body['orders'][0]
    gate('base_high_order_closes_actual_exterior_but_retains_all_head_mean_source_columns',
        order.get('homogeneous_angular_order')==0 and order.get('complete') and not order.get('failure')
        and order.get('actual_scalar_comparison_rows')==4650
        and order.get('full_unbounded_high_indices')=='every |j|>=97'
        and order.get('physical_minimum')==388 and order.get('canonical_exterior_feedback_closed')
        and order.get('independent_right_high_port') is False
        and body['source_contract']['ordinary_order0']=='L2_r H_phi^(1/3)'
        and body['source_contract']['all_head_to_high_source_rows_retained']
        and body['source_contract']['all_high_to_head_source_rows_retained']
        and body['source_contract']['independent_even_mean_own_rate_feedback_and_rank_rows_retained'])
    h=Fraction(9,10**6);rlo=Fraction(1191984371497,5000000000000)
    rb_cut=Fraction(1192029371497,5000000000000)
    contract=collar['exact_rational_contract'];c=q(contract['high_contraction_upper'])
    qc=q(Fraction(3000,2999));rc=q(Fraction(1,2999));Bc=q(Fraction(9,1000))
    gate('whole_true_collar_length_and_sup_Z_Green_constants',
        rb_cut-rlo==h and c>=0 and c<q(Fraction(1,3000))
        and Fraction(contract['high_resolvent'])==Fraction(3000,2999)
        and Fraction(9,1000)**2==9*h)
    chi=upper(order['bounds']['total_feedback'])
    Bf=upper(order['bounds']['ordinary_source_to_unperturbed_Z_sup'])
    gate('complete_body_contraction_is_strict_and_less_than31over100',
        chi>=0 and chi<q(Fraction(31,100)) and Bf>0)
    qb=(1/(1-chi)).upper();rb=(chi*qb).upper()
    loop=(rc*rb).upper();margin=(1-loop).lower()
    gate('true_two_port_interface_loop_is_below1over6000',margin>0 and loop<q(Fraction(1,6000)))
    sigma=(1/margin).upper()
    # Input order retains arbitrary collar jumps and both components
    # of an affine cut jump, in addition to every body/exterior source.
    zero=arb(0)
    X=[sigma*qc,sigma*qc*Bc,sigma*rc*qb*Bf,sigma*rc*qb,sigma*qc,sigma,sigma*rc]
    UB=[zero,zero,qb*Bf,qb,zero,zero,arb(1)]
    Y=[(rb*x+b).upper() for x,b in zip(X,UB)]
    U=[(qc*y).upper() for y in Y]
    U[0]=(U[0]+rc).upper();U[1]=(U[1]+qc*Bc).upper();U[4]=(U[4]+qc).upper()
    gate('actual_complete_given_head_root_reflection_is_below_one_half',U[0]<q(Fraction(1,2)))
    body_add=[zero,zero,Bf,arb(1),zero,zero,zero]
    body_sup=[(qb*(x+b)).upper() for x,b in zip(X,body_add)]
    collar_add=[arb(1),Bc,zero,zero,arb(1),zero,zero]
    collar_sup=[(qc*(y+b)).upper() for y,b in zip(Y,collar_add)]
    global_sup=[x.union(y).upper() for x,y in zip(body_sup,collar_sup)]
    body_reconstruction=upper(order['bounds']['raw_reconstruction_L2_multiplier'])
    raw_L2=[((q(h)*9*x*x+body_reconstruction**2*y*y).sqrt()).upper()
        for x,y in zip(collar_sup,body_sup)]
    gate('all_full_source_jump_and_port_response_coefficients_are_finite_nonnegative',
        len(X)==len(INPUT_ORDER) and all(x.is_finite() and x>=0
            for row in (X,Y,U,body_sup,collar_sup,global_sup,raw_L2) for x in row))
    doc.update(complete=True,original_candidate_sha256=CANDIDATE,derived_definition_sha256=REPAIR,
        exact_affine_parameter_offset='0',physical_parameter='fixed physical eta0 and original nu',
        entire_positive_interval=['the genuine intrinsic root','25/8'],
        fixed_body_cut=str(rb_cut),collar_length_upper=str(h),
        all_unbounded_high_indices='every |j|>=97',physical_minimum=388,
        original_collar_native_sha256=COLLAR_NATIVE,original_complete_body_native_sha256=BODY_NATIVE,
        original_collar_mathematics_recomputed=0,original_4650_body_rows_recomputed=0,
        exact_same_global_Z_reference=True,
        constants={name:rec(value) for name,value in dict(collar_contraction_upper=c,
            collar_resolvent=qc,collar_reflection_upper=rc,collar_ordinary_source_gain=Bc,
            body_feedback=chi,body_resolvent=qb,body_cut_reflection_upper=rb,
            body_unperturbed_source_gain=Bf,interface_loop_upper=loop,
            positive_interface_margin=margin,interface_resolvent=sigma,
            root_reflection_upper=U[0]).items()},
        input_order=list(INPUT_ORDER),
        response_rows={name:[rec(x) for x in row] for name,row in dict(
            body_incoming_stable_cut_port=X,collar_incoming_unstable_cut_port=Y,
            full_root_outgoing_unstable_port=U,body_Z_sup=body_sup,
            collar_Z_sup=collar_sup,entire_positive_Z_sup=global_sup,
            entire_positive_raw_L2=raw_L2).items()},
        ordinary_source_contract='L2_r H_phi^(1/3); complete head-to-high forcing is included',
        original_mean_and_head_outer_columns_retained_in_body_source=True,
        original_body_weighted_affine_jumps_retained=True,
        collar_and_both_cut_affine_jump_columns_retained=True,
        unknown_head_is_supplied_as_a_source_not_set_to_zero=True,
        given_complete_head_positive_high_inverse_and_root_graph_proved=True,
        full_low_high_Schur_inverse_proved=False,complete_infinite_BVP_inverse_proved=False,
        negative_root_return_proved=False,actual_full_PDE_response_error_proved=False,
        true_parameter_Schur_proved=False,nonlinear_background_neighbourhood_proved=False,
        nonzero_delta_M96_family_proved=False,order1_exterior_upgrade_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('collar-process','body-process','body-summary','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;start=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual positive interface outcome')
    doc=dict(kind='actual_same_reference_repaired_root_to_regular_given_head_high_graph_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={n:sha(getattr(a,n.replace('-','_'))) for n in ('collar-process','body-process','body-summary')})
    try:run(a,doc)
    except BaseException as error:doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-start;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],gates=len(doc['gates']),
        root_reflection=doc['constants']['root_reflection_upper']['upper'],
        seconds=doc['seconds'],full_low_high_Schur_inverse_proved=False)),flush=True)


if __name__=='__main__':main()
