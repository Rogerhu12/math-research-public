#!/usr/bin/env python3
"""Independent exact-rational reconstruction of the complete low46 beta ledger.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Uses FLINT fmpq exact rationals; no floating-point decisions or precision cap.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import fmpq as Q


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def q(v):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if 'upper' in v:return q(v['upper'])
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))


def outward_dyadic(z,bits=160):
    if z==0:return Q(0)
    exponent=z.numerator.bit_length()-z.denominator.bit_length()
    if z<Q(2)**exponent:exponent-=1
    exponent-=bits-1
    t=z/Q(2)**exponent
    return Q((t.numerator+t.denominator-1)//t.denominator)*Q(2)**exponent


def capped_linear(coeff,caps,budget):
    total=Q(0)
    for weight,cap in sorted(zip(coeff,caps),reverse=True):
        used=min(budget,cap);total+=weight*used;budget-=used
        if not budget:break
    return total


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','resource','reference-primary','reference-resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();t0=time.monotonic()
    if a.out.exists():raise FileExistsError('Keep earlier exact beta audits')
    x=read(a.primary);usage=read(a.resource);counts={}
    def check(name,v):
        if not v:raise ArithmeticError('Independent beta audit: '+name)
        counts[name]=counts.get(name,0)+1
    check('formal_success',usage['exitcode']==0 and usage['termination_signal'] is None)
    check('primary_completed',x['all_gates'] and all(x['gates'].values()))
    check('same_original_domain',x['domain']==dict(S_product_radius=['1',0],T_l1_radius=['1',-5]))
    paths={k:Path(v['path']) for k,v in x['input_identities'].items()}
    for k,path in paths.items():check('all_exact_input_pins',sha(path)==x['input_identities'][k]['sha256'])
    field=read(paths['field']);kernel=read(paths['cut_kernels']);source=read(paths['source_summary']);old=read(paths['old_beta']);cut=read(paths['cut_weights'])
    oldrow=next(r for r in old['rows'] if q(r['radius_T'])==q(x['old_intersection_radius_T']))
    check('old_bound_covers_current_domain',q(oldrow['radius_T'])>=Q(1,32))
    far=q(oldrow['true_far_added_once']);check('same_full_true_far',q(x['complete_true_far_common_at_reference_width2'])==outward_dyadic(far)>=far>0)
    check('S_squared_once',q(kernel['source_Vprime_over_Vs_squared'])==Q(257,256)**2)
    cop=[q(r['weighted_beta_cut_operator']) for r in cut['source_mode_rows']];fop=[q(r['weighted_beta_field_operator']) for r in cut['source_mode_rows']]
    keys={'Kbar':'Kbar_pair_upper','Wsigma1':'W_sigma1_upper','Whead1':'W_head1_upper'}
    sums={name:{piece:[Q(0)]*46 for piece in ('reference','DQ','quadratic','T')} for name in keys}
    shared={name:Q(0) for name in list(keys)+['T_cut','field']};n=-1
    for entry in source['source_parts']:
        path=paths['source_summary'].parent/Path(entry['path']).name;check('full_source_part_pin',sha(path)==entry['sha256'])
        with gzip.open(path,'rt') as f:
            for line in f:
                src=json.loads(line);n+=1;rec=x['cell_rows'][n];fr=field['rows'][n];kr=kernel['rows'][n]
                check('all213_cell_identity',src['cell']==rec['cell']==fr['cell']==kr['cell']==n+12)
                check('complete_polynomial_source_identity',src['low_polynomial_pair_rows']==rec['fixed_reference_low_polynomial'])
                check('complete_square_identity',rec['shared_complete_new_square']==fr['full_new_quadratic_source'])
                check('complete_T_identity',rec['shared_complete_mean_inverse_T']==fr['full_mean_inverse_difference_source'])
                check('complete_inverse_tail_identity',rec['shared_reference_inverse_tail']==src['material_bands']['common_d']['shared_complete_inverse_tail'])
                caps=list(map(q,fr['window_caps']));mass=list(map(q,fr['near_rest_common_caps']));lo=q(fr['fixed_low_cap']);hi=q(fr['complete_infinite_cap'])
                square=q(rec['shared_complete_new_square']);T=q(rec['shared_complete_mean_inverse_T']);tail=q(rec['shared_reference_inverse_tail']);refmass=q(src['material_bands']['common_d']['low2to92'])
                poly=[q(row['common_d']) for row in src['low_polynomial_pair_rows']];D=[list(map(q,row)) for row in src['low_DQ_two_material_window_kernels']['d1']]
                dvals=[]
                for j,coeff in enumerate(D):
                    v=coeff[0]*lo+coeff[14]*hi+capped_linear(coeff[1:7],caps[:6],mass[0])+capped_linear(coeff[7:14],caps[6:],mass[1])
                    check('independent_DQ_support',q(rec['complete_DQ_common_mode_caps'][j])>=v)
                    dvals.append(q(rec['complete_DQ_common_mode_caps'][j]))
                    for s,e in zip(coeff,src['low_DQ_two_material_window_kernels']['d_lambda'][j]):check('pointwise_material_majorant',s>=q(e)>=0)
                    check('no_free_high_to_low_Q_input',all(z==0 for z in coeff[7:]))
                kvals={name:list(map(q,kr[key])) for name,key in keys.items()}
                for name,coeff in kvals.items():
                    for j,k in enumerate(coeff):
                        sums[name]['reference'][j]+=k*min(poly[j]+tail,refmass)
                        sums[name]['DQ'][j]+=k*dvals[j]
                        sums[name]['quadratic'][j]+=k*square;sums[name]['T'][j]+=k*T
                weights=dict(kvals)
                weights['T_cut']=[kvals['Wsigma1'][j]*cop[j] if j>=6 else Q(0) for j in range(46)]
                weights['field']=[kvals['Wsigma1'][j]*fop[j] for j in range(46)]
                for name,coeff in weights.items():
                    reference=min(sum((coeff[j]*poly[j] for j in range(46)),Q(0))+max(coeff)*tail,max(coeff)*refmass)
                    columns=[sum((coeff[j]*D[j][col] for j in range(46)),Q(0)) for col in range(15)]
                    linear=columns[0]*lo+columns[14]*hi+capped_linear(columns[1:7],caps[:6],mass[0])+capped_linear(columns[7:14],caps[6:],mass[1])
                    rest=max(coeff)*(square+T);r=rec['common_readouts'][name]
                    check('independent_shared_reference',q(r['reference'])>=reference)
                    check('independent_shared_DQ',q(r['DQ'])>=linear)
                    check('independent_shared_square_T',q(r['shared_quadratic_and_T'])>=rest)
                    check('complete_shared_cell_sum',q(r['total_nonfar'])>=reference+linear+rest)
                    shared[name]+=q(r['total_nonfar'])
    check('complete213_source_coverage',n==212)
    oldkey={'Kbar':'complete_true_beta_cosine_K_coefficient','Wsigma1':'complete_true_beta_Wsigma1','Whead1':'complete_true_beta_Wtau_b1'}
    for i,row in enumerate(x['mode_rows']):
        check('all46_mode_identity',row['mode']==2*i+2)
        for name in keys:
            r=row[name]
            for piece,val in sums[name].items():check('all_mode_source_pieces',q(r['nonfar_pieces'][piece])>=val[i])
            check('all_mode_complete_nonfar',q(r['complete_nonfar'])>=sum((q(v) for v in r['nonfar_pieces'].values()),Q(0)))
            check('all_mode_true_far_retained',q(r['new_complete_with_true_far'])>=q(r['complete_nonfar'])+far)
            check('all_mode_old_true_bound_identity',r['old_complete']==oldrow['all46_mode_rows'][i][oldkey[name]])
            check('all_mode_chosen_intersection',q(r['chosen_complete'])==min(q(r['new_complete_with_true_far']),q(r['old_complete']))>0)
        check('same_original_per_mode_cut_weight',q(row['original_cut_weighted_beta_bound'])>=cop[i]*q(row['Wsigma1']['chosen_complete']))
    oldcommon={'Kbar':None,'Wsigma1':'whole46_true_beta_Wsigma1','Whead1':'whole46_true_beta_Wtau_b1','T_cut':'T_head_complete_in_original_cut_norm','field':'whole46_complete_beta_to_original_field_norm'}
    for name,total in shared.items():
        r=x['common_bounds'][name];factor=max(cop[6:]) if name=='T_cut' else max(fop) if name=='field' else Q(1)
        check('all213_common_sum',q(r['new_nonfar'])>=total)
        check('common_true_far_once',q(r['true_far_once'])>=factor*far)
        # Stored subfields are independently rounded displays. Reconstruct
        # the positive sum before their separate final rounding.
        check('common_complete_addition',q(r['new_complete'])>=total+factor*far)
        options=[q(r['new_complete']),q(r['sum_chosen_mode_bounds'])]
        if oldcommon[name]:options.append(q(oldrow[oldcommon[name]]))
        check('common_chosen_intersection',q(r['chosen_complete'])==min(options)>0)
    alternate=read(a.reference_primary);alternate_usage=read(a.reference_resource)
    check('independent_Fraction_primary_formal_success',alternate_usage['exitcode']==0 and alternate_usage['termination_signal'] is None)
    metadata={'schema','source_sha256','elapsed_seconds','peak_rss_kib','exact_rational_backend'}
    check('independent_Fraction_primary_all_scientific_fields',set(x)-metadata==set(alternate)-metadata)
    for key in set(x)-metadata:check('independent_Fraction_primary_exact_identity',x[key]==alternate[key])
    result=dict(schema='same-R100-complete-low46-true-beta-independent-audit-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,
      primary=dict(path=str(a.primary),sha256=sha(a.primary)),resource=dict(path=str(a.resource),sha256=sha(a.resource)),source_sha256=sha(__file__),
      reference_primary=dict(path=str(a.reference_primary),sha256=sha(a.reference_primary)),reference_resource=dict(path=str(a.reference_resource),sha256=sha(a.reference_resource)),
      exact_rational_backend='FLINT fmpq independent reconstruction plus scientific-field identity with Python Fraction primary; no floating point comparisons',same_original_Sunit_T1over32_domain=True,
      all9798_source_mode_outputs_and_shared_mass_consumed=True,complete_mean_inverse_and_true_far_retained=True,
      elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)


if __name__=='__main__':main()
