#!/usr/bin/env python3
"""Same proved P1 field: complete translated-strip 13-window posterior.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The complete R100 field already exists.  This script intersects its bounds
with actual source/Green images; it does not posit a new fixed point.  Every
low, far and infinite component stays in the original certified field.
"""
import argparse
from array import array
from fractions import Fraction as F
import gc
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb, arb_mat, ctx

WINDOWS = [[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],
           [186,192],[194,256],[258,512],[514,1024],[1026,2048],
           [2050,4096],[4098,8190]]
GROUPS = [list(range(6)),list(range(6,13))]
MATERIALS = ('d1','d_lambda','common_d')
PINS = {
 'split':('2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
}


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def ab(v):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if 'upper' in v:return ab(v['upper'])
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def pack(z,bits=160):
    if not z.is_finite():raise ArithmeticError('Every window comparison coefficient must be finite')
    z=z.upper()
    if not z>=0:raise ArithmeticError('Negative positive-comparison coefficient')
    if z==0:return ['0',0]
    m,e=z.man_exp();m,e=int(m),int(e);shift=max(0,m.bit_length()-bits)
    if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
    ans=[str(m),e]
    if not ab(ans)>=z:raise ArithmeticError('Outward rounding failed')
    return ans


def up(z):return ab(pack(z))


def completed(r):
    code=r.get('exitcode',r.get('exit_code',None))
    return code==0 and r.get('termination_signal',None) is None


def order(weights):return sorted(range(len(weights)),key=lambda k:ex(pack(weights[k])),reverse=True)


def support(weights,caps,mass,permutation=None):
    """Upper support of caps intersect one shared nonnegative l1 mass.

    Greedy allocation in descending exact dyadic coefficients is exact
    before rounding.  Rounding a remaining mass upward only enlarges that
    feasible set.  The whole result is also intersected with two elementary
    valid upper bounds.  No independent mass is assigned to every mode.
    """
    if permutation is None:permutation=order(weights)
    rem=mass;total=arb(0)
    for i in permutation:
        if rem==0:break
        take=min(rem,caps[i]);total+=weights[i]*take
        rem=up(max(arb(0),(rem-take).upper()))
    if not weights:return arb(0)
    return min(up(total),up(max(weights)*mass),up(sum((c*w for c,w in zip(caps,weights)),arb(0))))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-json',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--steps',type=int,default=32);p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;t0=time.monotonic()
    out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Fresh translated-strip posterior output')
    if not 1<=a.steps<=128:raise ValueError('Finite declared substitution count')
    cfg=read(a.input_json);ids=cfg['inputs'];paths={k:Path(v['path']) for k,v in ids.items()}
    for k,path in paths.items():
        if sha(path)!=ids[k]['sha256']:raise ArithmeticError('Frozen complete input pin: '+k)
    topic=Path(cfg['topic']);sys.path.insert(0,str(topic/'computations'))
    from closure_split_joint_io_v2 import iter_array,metadata_without_array
    gates={};counts={}
    def gate(name,b):
        if not b:raise ArithmeticError(name)
        gates[name]=True;counts[name]=counts.get(name,0)+1
    for k in paths:
        if k.endswith('_resource'):
            z=read(paths[k]);gate('formal_owned_input_'+k,completed(z))
    c40,c45,modal,source,old,lo,point,h40,h45=(read(paths[k]) for k in ('certificate040','certificate045','modal','source','original_window','original_low','original_point','head040','head045'))
    for k,d in zip(('certificate040','certificate045','modal','source','original_window','original_low','original_point','head040','head045'),(c40,c45,modal,source,old,lo,point,h40,h45)):
        gate('all_saved_input_math_'+k,d.get('all_gates') and all(d['gates'].values()))
    domain=c40['domain'];delta=arb(2)/5;gap=arb(1)/20
    gate('same_exact_complex_P1_domain',all(d['domain']==domain for d in (c45,modal,source,old,lo,point,h40,h45)) and domain['name']=='R156_actual_full_cut_posterior' and ex(domain['S_product_radius'])==F(3,8) and ex(domain['T_l1_radius'])==F(1,64) and domain['simultaneous_original_coordinates'])
    gate('actual_new_full_fields_identified',all(d['schema']=='new-uniformly-shifted-complete641-fixedpoint-v1' and d['new_complete_fixedpoint_proved'] and d['same_original_full_field_identified'] and d['full_source_mean_inverse_far_retained'] and not d['old_infinite_caps_reweighted'] for d in (c40,c45)))
    gate('exact_40_and45_translations',ex(c40['angular_weight_translation'])==ex(modal['angular_weight_translation'])==ex(source['angular_weight_translation'])==F(2,5) and ex(c45['angular_weight_translation'])==F(9,20))
    gate('same_actual_shifted_source',c40['input_identities']['modal_input']['sha256']==ids['modal']['sha256'] and c40['input_identities']['source_summary']['sha256']==ids['source']['sha256'] and source['all213_original_cells'] and not modal['full_error_or_infinite_tail_reweighted'])
    parent=modal['input_identities']['parent_modal']['sha256']
    gate('same_original_finite_error_field',old['input_identities']['modal_input']['sha256']==lo['input_identities']['modal_input']['sha256']==parent and point['input_identities']['field']['sha256']==ids['original_window']['sha256'] and old['windows']==point['windows']==WINDOWS and lo['modes']==list(range(2,93,2)))
    gate('complete_head_identity',h40['primary']['sha256']==ids['certificate040']['sha256'] and h45['primary']['sha256']==ids['certificate045']['sha256'] and h40['same_original617_units']==h45['same_original617_units'])
    r40=list(map(ab,c40['complete_image']));r45=list(map(ab,c45['complete_image']))
    gate('all_complete_image_coordinates',len(r40)==len(r45)==641 and all(v.is_finite() and v>0 for v in r40+r45))
    density=read(paths['density']);S=arb(257)/256
    gate('same_full_density',sha(paths['density'])==PINS['density'][1] and all(density['gates'].values()) and [r['cell'] for r in density['rows']]==list(range(12,225)))
    aa=[up(S*ab(r['V_over_w_upper'])) for r in density['rows']]
    C=[ab(r['Cs_plus_Lambda_common_cap']) for r in modal['rows']]
    L=[ab(r['Lambda_common_cap_on_domain']) for r in modal['rows']]
    gate('full_shifted_modal_order',modal['cells']==list(range(12,225)) and modal['modes']==list(range(2,93,2)))
    for mr,dr in zip(modal['rows'],density['rows']):
        gate('same_Vprime_and_translated_tau',mr['cell']==dr['cell'] and ex(mr['translated_tau_outer_lower'])==ex(mr['original_tau_outer_lower'])+F(2,5))
    fw=[up((m*delta).exp()) for m in range(2,93,2)]
    wf=[up((hi*delta).exp()) for lower,hi in WINDOWS]
    descend=[up((-lower*gap).exp()) for lower,hi in WINDOWS]
    low=[];low_modes=[];caps=[];old_common=[];initial=[]
    for n,(wr,lr) in enumerate(zip(old['rows'],lo['rows'])):
        gate('all213_finite_old_rows',wr['cell']==lr['cell']==n+12 and len(wr['window_caps'])==13 and len(wr['low_mode_caps'])==len(lr['low_mode_caps'])==46)
        lm=[min(ab(x),ab(y)) for x,y in zip(wr['low_mode_caps'],lr['low_mode_caps'])]
        lc=min(ab(wr['fixed_low_cap']),ab(lr['low_common_cap']))
        lnew=min(r40[n],up(r45[n]*(-2*gap).exp()),support(fw,lm,lc))
        modes=[min(lnew,up(z*w),up(r45[n]*(-m*gap).exp())) for z,w,m in zip(lm,fw,range(2,93,2))]
        lnew=min(lnew,up(sum(modes,arb(0))))
        low.append(lnew);low_modes.append([min(z,lnew) for z in modes])
        cm=[]
        for g,ix in enumerate(GROUPS):
            base=r40[213*(g+1)+n];wide=up(r45[213*(g+1)+n]*(-(94 if g==0 else 186)*gap).exp())
            finite=support([wf[w] for w in ix],[ab(wr['window_caps'][w]) for w in ix],ab(wr['near_rest_common_caps'][g]))
            cm.append(min(base,wide,finite))
        row=[min(cm[int(w>=6)],up(ab(wr['window_caps'][w])*wf[w]),up(r45[213*(1+int(w>=6))+n]*descend[w])) for w in range(13)]
        cm=[min(cm[g],up(sum((row[w] for w in GROUPS[g]),arb(0)))) for g in range(2)]
        row=[min(z,cm[int(w>=6)]) for w,z in enumerate(row)]
        old_common.append(cm);caps.append(row)
        gate('finite_positive_only_legal_strip_transfer',lnew>0 and all(z.is_finite() and z>0 for z in row+modes+cm))
        initial.append(dict(cell=n+12,low=pack(lnew),low_mode_caps=list(map(pack,modes)),near_rest=list(map(pack,cm)),windows=list(map(pack,row))))
    gate('all213_seed_rows',len(low)==len(C)==len(caps)==213)
    infinite=min(r40[639],up(r45[639]*(-8192*gap).exp()))
    far=min(r40[640],up(r45[640]*(-2*gap).exp()))
    far_source=[[ab(c40['new_far_absolute_high_image'][213+n]),ab(c40['new_far_absolute_high_image'][426+n])] for n in range(213)]
    infinite_far=ab(c40['new_far_absolute_high_image'][639])
    GI=up(S*ab(density['gamma_high']))
    head_strip_original=h40['head_strip'];eps=ab(h40['point_physical_epsilon_prime']);units=h40['same_original617_units']
    head_old=list(map(ab,point['actual_R100_head_window_masses']));head_parent=list(map(ab,point['actual_R100_head_band_masses']))
    known40=list(map(ab,h45['translated_head_band_masses']));known34816=ab(h45['shift040_tail_split']['upper_masses'][1])
    # New far image is the complete absolute D bound on Zdom. It is not an
    # old small-domain constant plus a falsely rescaled unknown linear term.
    gate('complete_new_far_absolute_readout',all(z>0 and z.is_finite() for row in far_source for z in row) and infinite_far>0 and ex(c40['far']['new_graph_domain'])==ex(modal['far_domain']['proposed_new_graph_ball']))
    del c40,c45,modal,old,lo,point,h40,h45,density,r40,r45;gc.collect()
    dqmeta=metadata_without_array(paths['dq'],'rows')
    gate('complete_actual_shifted_DQ',dqmeta['schema']=='inner-CsLambda-DQ-two-material-window-kernels-v1' and dqmeta['all_gates'] and all(dqmeta['gates'].values()) and dqmeta['cells']==list(range(12,225)) and dqmeta['windows_out']==WINDOWS and dqmeta['windows_in']==[[2,92]]+WINDOWS+[[8192,None]] and dqmeta['input_identities']['input']['sha256']==ids['modal']['sha256'] and dqmeta['input_identities']['density']['sha256']==ids['density']['sha256'])
    del dqmeta;gc.collect()
    kernels=[];permutations=[];low_kernels=[];low_orders=[]
    for n,r in enumerate(iter_array(paths['dq'],'rows')):
        gate('same_actual_DQ_centre',r['cell']==n+12 and ex(r['reference_common_cap'])==ex(pack(C[n])))
        cell=[];cellorder=[]
        for name in ('kernels_s_upper','kernels_ell_upper'):
            mat=[[ab(z) for z in row] for row in r[name]]
            gate('all_13_by15_DQ_entries',len(mat)==13 and all(len(row)==15 for row in mat) and all(z.is_finite() and z>=0 for row in mat for z in row))
            cell.append(mat);cellorder.append([[order(row[1:7]),order(row[7:14])] for row in mat])
        kernels.append(cell);permutations.append(cellorder);lc=[];orders=[]
        for name in ('low_singleton_kernels_s_upper','low_singleton_kernels_ell_upper'):
            gate('all_13_by46_low_singletons',len(r[name])==13 and all(len(z)==46 for z in r[name]) and all(ex(z)==0 for row in r[name][6:] for z in row))
            mat=[[ab(z) for z in row] for row in r[name][:6]]
            gate('every_low_DQ_entry_finite',all(z.is_finite() and z>=0 for row in mat for z in row))
            lc.append(mat);orders.append([order(row) for row in mat])
        low_kernels.append(lc);low_orders.append(orders)
        gate('s_same_coefficient_common_majorant',all(cell[0][w][j]>=cell[1][w][j] for w in range(13) for j in range(15)) and all(lc[0][w][j]>=lc[1][w][j] for w in range(6) for j in range(46)))
    gate('all213_DQ_rows',len(kernels)==213)
    poly=[{mat:[arb(0)]*13 for mat in MATERIALS} for n in range(213)];tails=[];bandref=[]
    for n,r in enumerate(source['rows']):
        gate('all213_complete_reference_order',r['cell']==n+12)
        tails.append({mat:ab(r['source_common_mass'][mat]['shared_complete_inverse_tail']) for mat in MATERIALS})
        bandref.append({mat:[ab(r['source_common_mass'][mat][g]) for g in ('near94to184','rest186to8190')] for mat in MATERIALS})
    partids=[];seen=[]
    for part in source['source_parts']:
        path=paths['source'].parent/Path(part['path']).name
        gate('full_source_part_pin',sha(path)==part['sha256']);partids.append(dict(path=str(path),sha256=sha(path)))
        with gzip.open(path,'rt') as stream:
            for line in stream:
                r=json.loads(line);n=r['cell']-12
                gate('complete_Laurent_poly_and_inverse_tail',n==len(seen) and [q['mode'] for q in r['high_polynomial_pair_rows']]==list(range(94,737,2)) and r['complete_mean_and_inverse_retained'] and r['polynomial_support_max736']);seen.append(n)
                for q in r['high_polynomial_pair_rows']:
                    w=next(i for i,(lower,hi) in enumerate(WINDOWS) if lower<=q['mode']<=hi)
                    for mat in MATERIALS:poly[n][mat][w]+=ab(q[mat])
                for mat in MATERIALS:poly[n][mat]=list(map(up,poly[n][mat]))
    gate('all213_complete_source_rows',len(seen)==213)
    qref=[[min(up(poly[n]['common_d'][w]+tails[n]['common_d']),bandref[n]['common_d'][int(w>=6)]) for w in range(13)] for n in range(213)]
    infinite_reference=[ab(row['source_common_mass']['common_d']['infinite8192up']) for row in source['rows']]
    gamma=read(paths['gamma']);mapping=gamma['requested_window_restrictions']
    gate('same_actual_eleven_mode_uniform_Greens',gamma['schema']=='original-inner-eleven-window-Gamma-replay-v1' and gamma['original_maximum_bitwise_identity'] and gamma['original_complete_far_and_pure_identity'] and gamma['Vprime_scale']==[257,256] and gamma['new_ODE_integrations']==0 and [r['window'] for r in mapping]==WINDOWS)
    gamma_arrays=[]
    for index,entry in enumerate(gamma['files']):
        path=paths['gamma'].parent/entry['path'];gate('actual_Gamma_chunk_pin',entry['index']==index and sha(path)==entry['sha256'])
        mm=array('Q',[0])*22791;ee=array('q',[0])*22791;seen=bytearray(22791)
        for row in iter_array(path,'entries'):
            k,n,m,e=row;k-=12;n-=12
            gate('causal_actual_vertex',0<=k<=n<213)
            index0=k*213-k*(k+1)//2+n;gate('unique_actual_vertex',not seen[index0]);seen[index0]=1
            m,e=int(m),int(e)
            while m>=1<<64 and m%2==0:m//=2;e+=1
            gate('exact_64bit_positive_Gamma',0<m<1<<64);mm[index0]=m;ee[index0]=e
        gate('complete_213_causal_triangle',sum(seen)==22791);gamma_arrays.append((mm,ee))
    gamma_groups=[[w for w,row in enumerate(mapping) if row['saved_window_index']==i] for i in range(11)]
    gate('all_eleven_original_Green_matrices',len(gamma_arrays)==11)
    del gamma,source;gc.collect()
    def common(n):return [min(old_common[n][g],up(sum((caps[n][w] for w in GROUPS[g]),arb(0)))) for g in range(2)]
    def source_row(n):
        cm=common(n);t=up(low[n]+cm[0]+cm[1]+infinite);cc=C[n]
        gate('full_mean_inverse_Hessian_physical_domain',aa[n]*(cc+t)<arb(1)/128)
        square=up((arb(23)/18)*t*t);rem=up(270*aa[n]*(cc+t)*(cc*t+t*t/2));dq=[]
        for mat in range(2):
            vals=[]
            for w,row in enumerate(kernels[n][mat]):
                lc=min(up(row[0]*low[n]),support(low_kernels[n][mat][w],low_modes[n],low[n],low_orders[n][mat][w])) if w<6 else arb(0)
                vals.append(up(lc+row[14]*infinite+support(row[1:7],caps[n][:6],cm[0],permutations[n][mat][w][0])+support(row[7:14],caps[n][6:],cm[1],permutations[n][mat][w][1])))
            dq.append(vals)
        def sqproject(lower):
            G=low[n] if 2*92>=lower else arb(0)
            for g in range(2):G+=min(cm[g],up(sum((caps[n][w] for w in GROUPS[g] if 2*WINDOWS[w][1]>=lower),arb(0))))
            G=min(t,up(G+infinite))
            return min(square,up((arb(23)/9)*t*G))
        return cm,t,square,rem,dq,[sqproject(lower) for lower,hi in WINDOWS],sqproject(8192)
    checkpoints=[];infinite_steps=[]
    def checkpoint(step):
        head=[min(up(common(0)[g]*eps),known40[g]) for g in range(2)]+[min(up(infinite*eps),known40[2])]
        cp=dict(step=step,cell12_windows=list(map(pack,caps[0])),cell13_windows=list(map(pack,caps[1])),cell12_common=list(map(pack,common(0))),complete_infinite_cap=pack(infinite),wholecell_head=list(map(pack,head)))
        checkpoints.append(cp);print(json.dumps(dict(event='proved_shift040_finite13_window_posterior',step=step,head_display=[str(z) for z in head],cell12_first2=[str(z) for z in caps[0][:2]],elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    checkpoint(0)
    for step in range(1,a.steps+1):
        src=arb_mat(213,13);isrc=[]
        for n in range(213):
            cm,t,sq,rem,dq,squares,isq=source_row(n)
            for w in range(13):src[n,w]=up(qref[n][w]+max(dq[0][w],dq[1][w])+squares[w]+rem)
            di=up((arb(23)/9)*C[n]*(caps[n][-1]+infinite))
            isrc.append(up(infinite_reference[n]+di+isq+rem))
        images=arb_mat(213,13)
        for (mm,ee),ws in zip(gamma_arrays,gamma_groups):
            green=arb_mat(213,213);idx=0
            for k in range(213):
                for n in range(k,213):green[k,n]=arb(mm[idx])*arb(2)**ee[idx];idx+=1
            selected=arb_mat([[src[n,w] for w in ws] for n in range(213)]);product=green*selected
            for j,w in enumerate(ws):
                for n in range(213):images[n,w]=product[n,j]
            del green,selected,product
        nxt=[]
        for n in range(213):
            vals=[]
            for w in range(13):
                v=min(caps[n][w],up(images[n,w]+far_source[n][int(w>=6)]))
                gate('each_actual_window_monotone_finite_positive',v.is_finite() and v>0 and v<=caps[n][w]);vals.append(v)
            nxt.append(vals)
        iv=up(GI*sum(isrc,arb(0))+infinite_far);newi=min(infinite,iv)
        gate('complete_infinite_actual_monotone',newi.is_finite() and 0<newi<=infinite)
        infinite_steps.append(dict(step=step,before=pack(infinite),full_image=pack(iv),after=pack(newi)))
        caps=nxt;infinite=newi
        if step&(step-1)==0 or step==a.steps:checkpoint(step)
        gate('owned_RSS_96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<a.rss_kib)
    # The point bound of the finite old spectrum may be raised to the new
    # width. No old infinite cap is raised. Whole-cell new bounds and the
    # genuine45-to40 infinity remain independent same-field intersections.
    head_rows=[];head_windows=[]
    for w,win in enumerate(WINDOWS):
        whole=up(caps[0][w]*eps);finite=up(head_old[w]*wf[w]);chosen=min(whole,finite,known40[int(w>=6)])
        gate('full_finite_window_point_readout',chosen.is_finite() and chosen>0)
        head_windows.append(chosen);head_rows.append(dict(window=win,wholecell=pack(whole),old_finite_point_reweighted=pack(finite),actual_translated_head=pack(chosen)))
    head=[];hb=[]
    for g,ix in enumerate(GROUPS):
        whole=up(common(0)[g]*eps);separate=up(sum((head_windows[w] for w in ix),arb(0)))
        finite=support([wf[w] for w in ix],[head_old[w] for w in ix],head_parent[g])
        val=min(whole,separate,finite,known40[g]);head.append(val)
        hb.append(dict(group=('near','rest')[g],wholecell_shared=pack(whole),sum_separate=pack(separate),old_finite_group_reweighted=pack(finite),known040_and045=pack(known40[g]),actual_translated_head=pack(val)))
    head.append(min(up(infinite*eps),known40[2]))
    original=[]
    for g,m in enumerate((94,186,8192)):original.append(min(up(head[g]*(-m*delta).exp()),head_parent[g]))
    rows=[]
    for n in range(213):
        cm,t,sq,rem,dq,squares,isq=source_row(n)
        rows.append(dict(cell=n+12,window_caps=list(map(pack,caps[n])),near_rest_common_caps=list(map(pack,cm)),fixed_low_cap=pack(low[n]),low_mode_caps=list(map(pack,low_modes[n])),complete_infinite_cap=pack(infinite),total_error=pack(t),full_new_quadratic_source=pack(sq),full_new_quadratic_window_sources=list(map(pack,squares)),full_new_quadratic_infinite_source=pack(isq),full_mean_inverse_difference_source=pack(rem),DQ_two_material_window_sources={MATERIALS[k]:list(map(pack,dq[k])) for k in range(2)}))
    tau=ex(head_strip_original)+F(2,5)
    result=dict(schema='same-P1-complete-shift040-window13-finite-posterior-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,gate_count=sum(counts.values()),gate_categories=counts,
        domain=domain,angular_weight_translation=dict(numerator='2',denominator='5'),input_identities=ids,input_config_sha256=sha(a.input_json),source_sha256=sha(__file__),source_parts=partids,
        windows=WINDOWS,steps=a.steps,initial_same_field_intersection=initial,rows=rows,checkpoints=checkpoints,infinite_steps=infinite_steps,
        complete_infinite_cap=pack(infinite),fixed_far_cap=pack(far),complete_far_source_by_cell=[[pack(z) for z in row] for row in far_source],complete_infinite_far_source=pack(infinite_far),
        source_material_units='Same physical x-source s*Vprime^2/w and abs(ell)*Vprime^2/w; field strong pair /Vprime. Uniform angular translation leaves modewise Green kernels invariant.',
        head_strip_original=head_strip_original,head_strip=dict(numerator=str(tau.numerator),denominator=str(tau.denominator)),head_bands=[[94,184],[186,8190],[8192,None]],
        translated_head_band_masses=list(map(pack,head)),translated_head_window_masses=list(map(pack,head_windows)),actual_R100_head_band_masses=list(map(pack,original)),
        head_window_readout=head_rows,complete_band_readout=hb,point_physical_epsilon_prime=pack(eps),same_original617_units=units,
        complete_tail34816_at040=pack(min(known34816,up(infinite*eps))),parent_full_infinite_mass_at040=pack(head[2]),
        complete_mean_inverse_far=True,finite_old_modes_only_reweighted=True,old_infinite_reweighted=False,new_045_infinite_only_lowered=True,
        original_rho_gate_not_used='The complete shifted field was independently proved; all posterior segments use its paid R116 physical domain, not old2^-30.',
        source_tail_accounting='Each single output window pays its complete positive inverse/Q/T tails. A sum of single-window bounds is valid but may pay these tails repeatedly; shared parent near/rest masses remain imposed.',
        no_new_ODE_or_integral=True,new_fixedpoint_claimed=False,scope='Only finite posteriors of the already proved same complex P1 field at tau+.4; no outer transfer is asserted.',
        elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Complete output strict size limit')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>=a.rss_kib:raise MemoryError('Owned final96MiB limit')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,gate_count=sum(counts.values()),head040=[str(z) for z in head],infinite34816=str(min(known34816,up(infinite*eps))),elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)

if __name__=='__main__':main()
