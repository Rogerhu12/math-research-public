#!/usr/bin/env python3
"""R157 actual fixedpoint-domain restriction of the same R100 modal input.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Adapted from the unchanged exact_closure R133 modal restriction; identity gates
now require the actual R157-domain lift and its membership certificate.
Cs keeps the original full-unit-S bounds. All Lambda pair/common/far bounds
are recomputed by the parent's exact support producer on a declared profile.
"""
import argparse,copy,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import fmpq as Q


def read(p):
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def q(v):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if 'upper' in v:return q(v['upper'])
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))


def pack(v):
    if v<0:raise ArithmeticError('Nonnegative modal bound required')
    if not v:return ['0',0]
    e=v.numerator.bit_length()-v.denominator.bit_length()
    if v<Q(2)**e:e-=1
    e-=159;t=v/Q(2)**e
    m=(t.numerator+t.denominator-1)//t.denominator
    assert Q(m)*Q(2)**e>=v
    return [str(m),e]


def rat(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('modal-input','modal-resource','lambda-primary','lambda-resource','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--domain',choices=('R156_actual_full_cut_posterior',),required=True)
    a=p.parse_args();start=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve each actual restricted input')
    original,origres,lp,lr=map(read,(a.modal_input,a.modal_resource,a.lambda_primary,a.lambda_resource));counts={}
    def check(name,value):
        if not value:raise ArithmeticError('Restricted modal gate: '+name)
        counts[name]=counts.get(name,0)+1
    for obj in (original,lp):check('actual_completed_input',obj['all_gates'] and all(obj['gates'].values()))
    for obj in (origres,lr):check('formal_input_success',obj['exitcode']==0 and obj['termination_signal'] is None)
    check('same_original_full_modal_pin',sha(a.modal_input)=='0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93')
    check('same_actual_R157_lift_pin',sha(a.lambda_primary)=='e9724edbce6515de15ac40ef0fa12824b269dd3438b528056db9fbee2ae240c2')
    check('actual_R157_domain_contains_same_a_star',lp['schema']=='R157-actual213-transverse-lift-fixedpoint-posterior-v1' and lp['same_R143_unique_a_star_in_new_domain'] and lp['existing_R100_field_restricted_not_new_field'])
    selected=next(d for d in lp['domains'] if d['name']==a.domain)
    check('simultaneous_parameter_profile',selected['coordinate_constraints_and_shared_T_mass_are_simultaneous'])
    check('domain_inside_original_R100',0<q(selected['S_linf_radius'])<=1 and 0<q(selected['T_l1_radius'])<=Q(1,32))
    check('same_213_cells_46_modes',lp['cells']==original['cells']==list(range(12,225)) and lp['modes']==original['modes']==list(range(2,93,2)))
    check('same_original_Vprime_normalization',lp['normalization']==original['normalization'] and q(original['R100_envelope_scale'])==Q(257,256))
    check('Cs_full_unit_envelope_valid_on_subset',selected['C_S_may_keep_original_unit_S_caps_conservatively'])
    rows=[]
    for old,new in zip(original['rows'],selected['rows']):
        check('all213_cell_identity',old['cell']==new['cell'])
        check('all_actual_46_unit_columns',new['actual_all46_original_unit_columns_retained'] and len(new['Lambda_pair_caps_on_domain'])==46)
        row=copy.deepcopy(old)
        lam=[min(q(z),q(t)) for z,t in zip(new['Lambda_pair_caps_on_domain'],old['Lambda_pair_caps_at_radius1over32'])]
        lc=min(q(new['Lambda_common_cap_on_domain']),q(old['Lambda_common_cap_at_radius1over32']),sum(lam,Q(0)))
        caps=[min(q(t),q(c)+z) for c,z,t in zip(old['Cs_complete_pair_caps'],lam,old['Cs_plus_Lambda_pair_caps'])]
        total=min(q(old['Cs_plus_Lambda_common_cap']),q(old['Cs_common_cap'])+lc,sum(caps,Q(0)))
        row['Lambda_pair_caps_on_domain']=list(map(pack,lam));row['Lambda_common_cap_on_domain']=pack(lc)
        row['Cs_plus_Lambda_pair_caps']=list(map(pack,caps));row['Cs_plus_Lambda_common_cap']=pack(total)
        for z,t in zip(row['Cs_plus_Lambda_pair_caps'],old['Cs_plus_Lambda_pair_caps']):check('every_new_pair_within_old_bound',q(z)<=q(t))
        check('complete_common_within_old_bound',q(row['Cs_plus_Lambda_common_cap'])<=q(old['Cs_plus_Lambda_common_cap']))
        del row['Lambda_pair_caps_at_radius1over32'],row['Lambda_common_cap_at_radius1over32']
        row['shared_parameter_budget']='Exact original T coordinate caps together with the declared T l1 radius; Cs keeps the original full unit S envelope.'
        rows.append(row)
    far=min(q(original['far_common_at_radius1over32']),q(selected['transverse_far_common_unscaled_by_S']))
    check('complete_positive_restricted_far',far>0)
    result=copy.deepcopy(original)
    result.update(schema='inner-R100-Cs-Lambda-restricted-profile-modal-input-v1',source_sha256=sha(__file__),
      scope='Same original R100 field restricted to the exact R157 posterior domain containing the existing unique R143 fixed point. Original full unit S bounds for Cs are kept conservatively. The pre-existing parameter cut existence and uniqueness are inputs, not results of this restriction.',
      all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,
      domain=dict(name=a.domain,S_product_radius=selected['S_linf_radius'],T_l1_radius=selected['T_l1_radius'],
        T_coordinate_caps_by_mode=selected['original_normalized_T_coordinate_caps'],simultaneous_original_coordinates=True),
      transverse_radius=selected['T_l1_radius'],far_common_on_domain=pack(far),rows=rows,
      parameter_domain='Explicit domain object, including all 40 individual T caps and the shared T mass simultaneously.',
      parent_full_domain=dict(S_product_radius=rat(Q(1)),T_l1_radius=rat(Q(1,32))),
      restriction_provenance={k:dict(path=str(getattr(a,k)),sha256=sha(getattr(a,k))) for k in ('modal_input','modal_resource','lambda_primary','lambda_resource')},
      elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    del result['far_common_at_radius1over32']
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(path=str(out),sha256=sha(out),bytes=out.stat().st_size,all_gates=True,gate_count=result['gate_count'],domain=a.domain,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
