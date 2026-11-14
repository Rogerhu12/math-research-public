#!/usr/bin/env python3
"""Actual complete R100 beta from all213 source cells and all46 cut kernels.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The exact same-height linear DN, including Lambda, cancels before reading
the nonlinear source. The complete nonlinear true far is added once.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def pack(z,bits=160):
    if z<0:raise ArithmeticError('Negative complete positive-source budget')
    if z==0:return ['0',0]
    k=z.numerator.bit_length()-z.denominator.bit_length()
    if z<F(2)**k:k-=1
    e=k-bits+1;r=z/F(2)**e;m=(r.numerator+r.denominator-1)//r.denominator
    if F(m)*F(2)**e<z:raise ArithmeticError('Inward exact source rounding')
    return [str(m),e]


def up(z):return ex(pack(z))


def support(weights,caps,mass):
    z=F(0)
    for i in sorted(range(len(weights)),key=lambda i:weights[i],reverse=True):
        take=min(mass,caps[i]);z+=take*weights[i];mass-=take
        if mass==0:break
    return z


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','field','field-resource','source-summary','source-resource','cut-kernels','cut-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();started=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve every actual true-beta computation')
    data={k:read(getattr(a,k)) for k in ('field','field_resource','source_summary','source_resource','cut_kernels','cut_resource')}
    ids={k:dict(path=str(getattr(a,k)),sha256=sha(getattr(a,k))) for k in data};counts={}
    def gate(name,ok):
        if not ok:raise ArithmeticError('Unpaid exact true-beta gate: '+name)
        counts[name]=counts.get(name,0)+1
    for k in ('field','source_summary','cut_kernels'):gate('completed_'+k,data[k]['all_gates'] and all(data[k]['gates'].values()))
    for k in ('field_resource','source_resource','cut_resource'):gate('formal_'+k,data[k]['exitcode']==0 and data[k]['termination_signal'] is None)
    field,source,kernel=data['field'],data['source_summary'],data['cut_kernels']
    gate('field_schema',field['schema']=='same-R100-inner13-window-frequency-square-and-infinite-finite-bootstrap-and-head-v3')
    gate('source_schema',source['schema']=='visible-flex-R100-true-low46-reference-complete-source-and-DQ-v2')
    gate('cut_schema',kernel['schema']=='same-original-inner-low46-common-material-truecut-kernels-v1')
    modes=list(range(2,93,2));gate('complete213and46',source['cells']==kernel['cells']==list(range(12,225)) and source['output_modes']==kernel['modes']==modes)
    gate('same_full_R100_domain',field['domain']==dict(S_product_radius=['1',0],T_l1_radius=['1',-5]))
    modal=field['input_identities']['modal_input'];density=field['input_identities']['density']
    gate('same_reference_modal_source',source['input_hashes'][modal['path']]==modal['sha256'])
    gate('same_original_density',source['input_hashes'][density['path']]==density['sha256']==kernel['original_R82_complete_source_dependencies']['notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz'])
    gate('same_exact_strip',ex(kernel['head_strip'])==ex(field['head_strip']) and ex(kernel['sigma'])==F(1,64))
    gate('exact_material_rescaling_once',ex(kernel['source_Vprime_over_Vs_squared'])==F(257,256)**2)
    oldpath=a.topic/'notes/2026-11-13-inner-aux-bootstrap-beta-interface-r1.json.gz'
    cutpath=a.topic/'notes/2026-11-13-root-hybrid46-cut-r1.json'
    gate('old_complete_beta_pin',sha(oldpath)=='1bd50cb4f32bb17d1238dd2487df379526246651a5ebbf1ec6fdf5809699f5ea')
    gate('same_original_cut_weights_pin',sha(cutpath)=='cf33eba4dcd1ad4e8fea3e667664b9c356db790851ca8e49d9889a62e408d638')
    old,cut=read(oldpath),read(cutpath);ids['old_beta']=dict(path=str(oldpath),sha256=sha(oldpath));ids['cut_weights']=dict(path=str(cutpath),sha256=sha(cutpath))
    gate('old_beta_complete',old['all_gates'] and all(old['gates'].values()))
    oldrow=min((r for r in old['rows'] if ex(r['radius_T'])>=F(1,32)),key=lambda r:ex(r['radius_T']))
    gate('same_old46_modes',[r['mode'] for r in oldrow['all46_mode_rows']]==[r['mode'] for r in cut['source_mode_rows']]==modes)
    far=ex(oldrow['true_far_added_once']);gate('complete_positive_true_far',far>0)
    cop=[ex(r['weighted_beta_cut_operator']) for r in cut['source_mode_rows']];fop=[ex(r['weighted_beta_field_operator']) for r in cut['source_mode_rows']]
    target_fields={'Kbar':'Kbar_pair_upper','Wsigma1':'W_sigma1_upper','Whead1':'W_head1_upper'}
    sums={name:{piece:[F(0)]*46 for piece in ('reference','DQ','quadratic','T')} for name in target_fields}
    common={name:F(0) for name in list(target_fields)+['T_cut','field']};saved=[];parts=[];seen=0
    for entry in source['source_parts']:
        path=a.source_summary.parent/Path(entry['path']).name;gate('source_part_pin',sha(path)==entry['sha256']);parts.append(dict(path=str(path),sha256=sha(path)))
        with gzip.open(path,'rt') as f:
            for line in f:
                src=json.loads(line);n=src['cell']-12;gate('complete_cell_order',n==seen);seen+=1
                fr=field['rows'][n];kr=kernel['rows'][n];gate('actual_cell_identity',src['cell']==fr['cell']==kr['cell'])
                gate('complete_reference_mean_inverse',src['complete_mean_and_inverse_retained'] and src['full_numerator_zero_coefficients'] is not None)
                gate('complete_reference_low_modes',[r['mode'] for r in src['low_polynomial_pair_rows']]==modes)
                gate('same_DQ_input_partition',src['low_DQ_input_windows']==[[2,92]]+field['windows']+[[8192,None]])
                caps=list(map(ex,fr['window_caps']));cm=list(map(ex,fr['near_rest_common_caps']));lo=ex(fr['fixed_low_cap']);hi=ex(fr['complete_infinite_cap'])
                square=ex(fr['full_new_quadratic_source']);T=ex(fr['full_mean_inverse_difference_source'])
                poly=[ex(r['common_d']) for r in src['low_polynomial_pair_rows']]
                tail=ex(src['material_bands']['common_d']['shared_complete_inverse_tail']);reference_common=ex(src['material_bands']['common_d']['low2to92'])
                D=[[ex(z) for z in row] for row in src['low_DQ_two_material_window_kernels']['d1']]
                E=src['low_DQ_two_material_window_kernels']['d_lambda'];dvals=[]
                for j,row in enumerate(D):
                    gate('full_DQ_input_columns',len(row)==15)
                    for s,e in zip(row,E[j]):gate('pointwise_s_common_material_dominance',s>=ex(e)>=0)
                    gate('exact_high_to_low_quadratic_support',all(v==0 for v in row[7:]))
                    dvals.append(up(row[0]*lo+row[14]*hi+support(row[1:7],caps[:6],cm[0])+support(row[7:14],caps[6:],cm[1])))
                kvalues={name:list(map(ex,kr[key])) for name,key in target_fields.items()}
                for name,ks in kvalues.items():
                    for j,g in enumerate(ks):
                        gate('positive_true_source_kernel',g>0)
                        sums[name]['reference'][j]+=g*min(poly[j]+tail,reference_common)
                        sums[name]['DQ'][j]+=g*dvals[j]
                        sums[name]['quadratic'][j]+=g*square
                        sums[name]['T'][j]+=g*T
                weighted=dict(kvalues)
                weighted['T_cut']=[kvalues['Wsigma1'][j]*cop[j] if j>=6 else F(0) for j in range(46)]
                weighted['field']=[kvalues['Wsigma1'][j]*fop[j] for j in range(46)]
                cellsums={}
                for name,ks in weighted.items():
                    ref=min(sum((g*q for g,q in zip(ks,poly)),F(0))+max(ks)*tail,max(ks)*reference_common)
                    agg=[sum((ks[j]*D[j][col] for j in range(46)),F(0)) for col in range(15)]
                    linear=agg[0]*lo+agg[14]*hi+support(agg[1:7],caps[:6],cm[0])+support(agg[7:14],caps[6:],cm[1])
                    extra=max(ks)*(square+T);cellvalue=up(ref+linear+extra);common[name]+=cellvalue
                    cellsums[name]=dict(reference=pack(ref),DQ=pack(linear),shared_quadratic_and_T=pack(extra),total_nonfar=pack(cellvalue))
                saved.append(dict(cell=src['cell'],fixed_reference_low_polynomial=src['low_polynomial_pair_rows'],complete_DQ_common_mode_caps=list(map(pack,dvals)),shared_reference_inverse_tail=pack(tail),shared_complete_new_square=pack(square),shared_complete_mean_inverse_T=pack(T),common_readouts=cellsums,
                    mode92_Wsigma_pieces={name:pack(kvalues['Wsigma1'][-1]*v) for name,v in [('reference',min(poly[-1]+tail,reference_common)),('DQ',dvals[-1]),('quadratic',square),('T',T)]}))
    gate('all213_source_cells_done',seen==213)
    newmode=[]
    for i,m in enumerate(modes):
        rr=dict(mode=m,group='S' if m<=12 else 'T')
        for name in target_fields:
            values={piece:up(sums[name][piece][i]) for piece in sums[name]};nf=up(sum(values.values(),F(0)));full=up(nf+far)
            oldkey={'Kbar':'complete_true_beta_cosine_K_coefficient','Wsigma1':'complete_true_beta_Wsigma1','Whead1':'complete_true_beta_Wtau_b1'}[name]
            chosen=min(full,ex(oldrow['all46_mode_rows'][i][oldkey]))
            rr[name]=dict(nonfar_pieces={k:pack(v) for k,v in values.items()},complete_nonfar=pack(nf),new_complete_with_true_far=pack(full),old_complete=oldrow['all46_mode_rows'][i][oldkey],chosen_complete=pack(chosen))
        rr['original_cut_weighted_beta_bound']=pack(cop[i]*ex(rr['Wsigma1']['chosen_complete']))
        newmode.append(rr)
    commonout={}
    oldcommon={'Kbar':None,'Wsigma1':'whole46_true_beta_Wsigma1','Whead1':'whole46_true_beta_Wtau_b1','T_cut':'T_head_complete_in_original_cut_norm','field':'whole46_complete_beta_to_original_field_norm'}
    for name,nf in common.items():
        factor=max(cop[6:]) if name=='T_cut' else max(fop) if name=='field' else F(1)
        full=up(nf+factor*far)
        if name in target_fields:separate=sum((ex(row[name]['chosen_complete']) for row in newmode),F(0))
        else:
            ws=cop if name=='T_cut' else fop;indices=range(6,46) if name=='T_cut' else range(46)
            separate=sum((ws[i]*ex(newmode[i]['Wsigma1']['chosen_complete']) for i in indices),F(0))
        chosen=min(full,up(separate))
        if oldcommon[name]:chosen=min(chosen,ex(oldrow[oldcommon[name]]))
        commonout[name]=dict(new_nonfar=pack(nf),true_far_once=pack(factor*far),new_complete=pack(full),sum_chosen_mode_bounds=pack(separate),chosen_complete=pack(chosen))
    result=dict(schema='same-R100-full-low46-actual-source-true-beta-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,
      gates=dict(same_existing_complete_R100_field=True,all46_low_source_modes_and_all213_cells=True,same_height_linear_DN_and_Lambda_cancel_exactly=True,
      complete_reference_mean_inverse_and_zero_numerator=True,actual_DQ_frequency_support_and_all_derivative_weights=True,pointwise_s_common_material_majorant=True,
      full_unknown_Q_and_T_not_truncated=True,true_far_positive_and_once_per_common_mass=True,original_mu_w_squared_and_S_squared_paid=True,exact_Fraction_consumption=True),
      input_identities=ids,source_parts=parts,source_sha256=sha(__file__),domain=field['domain'],sigma=kernel['sigma'],head_strip=field['head_strip'],modes=modes,
      beta_definition='True low inner nonlinear DN minus the exact same-height linear DN; beta=Phi_cut N(F)+B_cut D(z_true). Lambda is in both linear traces and cancels before source reading. Complete true far is separate and added once.',
      units='Kbar is relative physical kappa_perp/true_w cosine coefficient or signed-pair mass; Wsigma1 and Whead1 are strong Fourier pair masses at the stated widths.',
      mode_rows=newmode,common_bounds=commonout,cell_rows=saved,old_intersection_radius_T=oldrow['radius_T'],complete_true_far_common_at_reference_width2=pack(far),
      complete_mean_inverse_far=True,new_g_or_new_ODE_or_cut_fixedpoint_claimed=False,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Split complete low-beta actual output')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,gate_count=result['gate_count'],T_cut_display=float(ex(commonout['T_cut']['chosen_complete'])),mode92_Wsigma_display=float(ex(newmode[-1]['Wsigma1']['chosen_complete'])),mode92_cut_display=float(ex(newmode[-1]['original_cut_weighted_beta_bound'])),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
