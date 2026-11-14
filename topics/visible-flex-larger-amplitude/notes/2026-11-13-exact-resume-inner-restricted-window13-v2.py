#!/usr/bin/env python3
"""Frequency-resolved full quadratic13-window plus infinite finite readout.

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
    for k in ('topic','field','field-resource','modal-input','source-summary','source-resource',
              'dq-kernels','dq-resource','scalar-endpoint','scalar-resource',
              'canonical-endpoint','canonical-resource','previous-window-primary','previous-window-resource','window-gamma','window-gamma-resource','out-prefix'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--steps',type=int,default=32);p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;t0=time.monotonic()
    out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Preserve every actual13-window attempt')
    if not 1<=a.steps<=256:raise ValueError('A finite declared substitution count is required')
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array,metadata_without_array
    ids={}
    for k in ('field','field_resource','modal_input','source_summary','source_resource','dq_kernels',
              'dq_resource','scalar_endpoint','scalar_resource','canonical_endpoint','canonical_resource','previous_window_primary','previous_window_resource','window_gamma','window_gamma_resource'):
        f=getattr(a,k);ids[k]=dict(path=str(f),sha256=sha(f))
    paths={k:a.topic/'notes'/v[0] for k,v in PINS.items()}
    for k,f in paths.items():
        if sha(f)!=PINS[k][1]:raise ArithmeticError('Original pinned full Green/density changed: '+k)
        ids[k]=dict(path=str(f),sha256=sha(f))
    field,source,scalar,canonical=(read(getattr(a,k)) for k in ('field','source_summary','scalar_endpoint','canonical_endpoint'))
    for k,obj in [('field',field),('source_summary',source),('scalar_endpoint',scalar),('canonical_endpoint',canonical)]:
        if not obj.get('all_gates') or not all(obj['gates'].values()):raise ArithmeticError('Actual completed input required: '+k)
    for k in ('field_resource','source_resource','dq_resource','scalar_resource','canonical_resource','previous_window_resource','window_gamma_resource'):
        if not completed(read(getattr(a,k))):raise ArithmeticError('Formal successful resource required: '+k)
    if field['schema']!='same-R100-restricted-complete-nonlinear641-finite-bootstrap-v1':raise ArithmeticError('Same existing full field required')
    if field['input_identities']['source_summary']['sha256']!=sha(a.source_summary) or field['input_identities']['modal_input']['sha256']!=sha(a.modal_input):raise ArithmeticError('Field/source/centre identities differ')
    if sha(a.scalar_endpoint)!='8f90a5b5e617c3059736d4b80ba0008f456ad7412e2e9bf9159049ebd873e716' or sha(a.canonical_endpoint)!='5741ce64f40e252c7b568bc8be61ae14695a41faf6fbaa3cbac13eaab5c9a5c9':raise ArithmeticError('Original fixed geometry endpoint columns required')
    if not(0<ex(field['domain']['S_product_radius'])<=1 and 0<ex(field['domain']['T_l1_radius'])<=F(1,32) and field['domain']['simultaneous_original_coordinates'] and source['domain']==field['domain']):raise ArithmeticError('Exact restricted original parameter domain required')
    if canonical['original_scalar_endpoint_primary']['sha256']!=sha(a.scalar_endpoint):raise ArithmeticError('Canonical intersection must use the same actual scalar kernel')
    if canonical['domain']!=dict(S_product_radius=['1',0],T_l1_radius=['1',-5]):raise ArithmeticError('Original unrestricted unit S/T1over32 domain required')
    dqmeta=metadata_without_array(a.dq_kernels,'rows')
    if not(dqmeta['schema']=='inner-CsLambda-DQ-two-material-window-kernels-v1' and dqmeta['all_gates'] and all(dqmeta['gates'].values())
           and dqmeta['cells']==list(range(12,225)) and dqmeta['windows_out']==WINDOWS
           and dqmeta['windows_in']==[[2,92]]+WINDOWS+[[8192,None]]
           and dqmeta['input_identities']['input']['sha256']==sha(a.modal_input)
           and dqmeta['input_identities']['density']['sha256']==PINS['density'][1]):raise ArithmeticError('Complete actual DQ source window contract required')
    del dqmeta;gc.collect()
    density=read(paths['density']);S=arb(257)/256;Theta=arb(16705)/16384
    aa=[up(S*ab(r['V_over_w_upper'])) for r in density['rows']]
    if [r['cell'] for r in density['rows']]!=list(range(12,225)):raise ArithmeticError('Complete original density cells required')
    W=list(map(ab,field['same_original_metric_weights']));vcap=list(map(ab,field['full641_checkpoints'][-1]['all641_W_scaled_caps']))
    raw=[up(v*w) for v,w in zip(vcap,W)]
    low=raw[:213];old_common=[[raw[213+n],raw[426+n]] for n in range(213)]
    infinite,far=raw[639],raw[640]
    caps=[[old_common[n][int(w>=6)] for w in range(13)] for n in range(213)]
    prev=read(a.previous_window_primary)
    if not(sha(a.previous_window_primary)=='3fbbabfa9c2936c36013a915a9fd8959be06756b55cd7f923e6a4350122886dd' and prev['all_gates'] and all(prev['gates'].values()) and prev['domain']==canonical['domain'] and prev['windows']==WINDOWS):raise ArithmeticError('Original full-domain existing field window bound required')
    infinite=min(infinite,ab(prev['complete_infinite_cap']));far=min(far,ab(prev['fixed_far_cap']))
    for n,row in enumerate(prev['rows']):
        if row['cell']!=n+12 or len(row['window_caps'])!=13:raise ArithmeticError('Previous complete coordinate identity changed')
        low[n]=min(low[n],ab(row['fixed_low_cap']))
        old_common[n]=[min(old_common[n][g],ab(row['near_rest_common_caps'][g])) for g in range(2)]
        for k,z in enumerate(row['window_caps']):
            z=ab(z)
            if not z>0:raise ArithmeticError('Positive old finite cap required')
            caps[n][k]=min(z,caps[n][k],old_common[n][int(k>=6)])
    modalref=[];lamb=[]
    for n,r in enumerate(iter_array(a.modal_input,'rows')):
        if r['cell']!=n+12:raise ArithmeticError('Modal cell ordering differs')
        modalref.append(ab(r['Cs_plus_Lambda_common_cap']));lamb.append(ab(r['Lambda_common_cap_on_domain']))
    if len(modalref)!=213:raise ArithmeticError('All213 modal source cells required')
    kernels=[];permutations=[]
    for n,r in enumerate(iter_array(a.dq_kernels,'rows')):
        if r['cell']!=n+12 or not ex(r['reference_common_cap'])==ex(pack(modalref[n])):raise ArithmeticError('Fixed DQ centre identity differs')
        cell=[];cellorder=[]
        for name in ('kernels_s_upper','kernels_ell_upper'):
            mat=[[ab(z) for z in row] for row in r[name]]
            if len(mat)!=13 or any(len(row)!=15 for row in mat):raise ArithmeticError('Complete13x15 DQ table required')
            if any(not z.is_finite() or not z>=0 for row in mat for z in row):raise ArithmeticError('Nonfinite DQ coefficient')
            cell.append(mat);cellorder.append([[order(row[1:7]),order(row[7:14])] for row in mat])
        kernels.append(cell);permutations.append(cellorder)
    if len(kernels)!=213:raise ArithmeticError('All213 actual DQ coefficient rows required')
    # Separate complete reference polynomial coefficients and the single
    # shared full inverse tail.  A per-window bound may use that tail, but
    # the final common trace pays it only once via the maximum readout.
    poly=[{mat:[arb(0)]*13 for mat in MATERIALS} for n in range(213)]
    tails=[];bandref=[]
    for n,r in enumerate(source['rows']):
        if r['cell']!=n+12:raise ArithmeticError('Complete reference source order differs')
        tails.append({mat:ab(r['source_common_mass'][mat]['shared_complete_inverse_tail']) for mat in MATERIALS})
        bandref.append({mat:[ab(r['source_common_mass'][mat][g]) for g in ('near94to184','rest186to8190')] for mat in MATERIALS})
    seen=[];partids=[]
    for part in source['source_parts']:
        path=a.source_summary.parent/Path(part['path']).name
        if sha(path)!=part['sha256']:raise ArithmeticError('Complete polynomial source part changed')
        partids.append(dict(path=str(path),sha256=sha(path)))
        with gzip.open(path,'rt') as f:
            for line in f:
                r=json.loads(line);n=r['cell']-12
                if n!=len(seen):raise ArithmeticError('Complete source cell coverage differs')
                seen.append(n)
                rr=r['high_polynomial_pair_rows']
                if [q['mode'] for q in rr]!=list(range(94,737,2)) or not r['complete_mean_and_inverse_retained'] or not r['polynomial_support_max736']:raise ArithmeticError('Entire source Laurent polynomial and full inverse required')
                for q in rr:
                    mode=q['mode'];w=next(i for i,(lo,hi) in enumerate(WINDOWS) if lo<=mode<=hi)
                    for mat in MATERIALS:poly[n][mat][w]+=ab(q[mat])
                for mat in MATERIALS:poly[n][mat]=list(map(up,poly[n][mat]))
    if len(seen)!=213:raise ArithmeticError('Incomplete actual reference source parts')
    qref=[[min(up(poly[n]['common_d'][w]+tails[n]['common_d']),bandref[n]['common_d'][int(w>=6)]) for w in range(13)] for n in range(213)]
    split=metadata_without_array(paths['split'],'gamma_rows')
    far_source=[]
    for n,row in enumerate(split['cells']):
        far_source.append([up(ab(row['far_boundary_'+g])/S+4*Theta*ab(row['far_boundary_'+g])*far) for g in ('near','rest')])
    gamma=read(a.window_gamma)
    if not(gamma['schema']=='original-inner-eleven-window-Gamma-replay-v1' and gamma['original_maximum_bitwise_identity'] and gamma['original_complete_far_and_pure_identity'] and gamma['Vprime_scale']==[257,256] and gamma['new_ODE_integrations']==0):raise ArithmeticError('Actual same-geometry eleven-window kernels required')
    mapping=gamma['requested_window_restrictions']
    if [r['window'] for r in mapping]!=WINDOWS:raise ArithmeticError('Whole13-window kernel coverage required')
    gamma_arrays=[]
    for index,entry in enumerate(gamma['files']):
        path=a.window_gamma.parent/entry['path']
        if entry['index']!=index or sha(path)!=entry['sha256']:raise ArithmeticError('Frozen actual window kernel pin')
        mm=array('Q',[0])*22791;ee=array('q',[0])*22791;seen=bytearray(22791)
        for row in iter_array(path,'entries'):
            k,n,m,e=row;k-=12;n-=12
            if not 0<=k<=n<213:raise ArithmeticError('Complete per-window causal coverage')
            index0=k*213-k*(k+1)//2+n
            if seen[index0]:raise ArithmeticError('Repeated actual causal kernel vertex')
            seen[index0]=1
            m,e=int(m),int(e)
            while m>=1<<64 and m%2==0:m//=2;e+=1
            if not 0<m<1<<64:raise ArithmeticError('Exactly represented positive kernel mantissa required')
            mm[index0]=m;ee[index0]=e
        if sum(seen)!=22791:raise ArithmeticError('Complete213 causal triangle required')
        gamma_arrays.append((mm,ee))
    if len(gamma_arrays)!=11:raise ArithmeticError('All eleven original windows required')
    gamma_window_groups=[[w for w,row in enumerate(mapping) if row['saved_window_index']==i] for i in range(11)]
    del gamma;gc.collect()
    GI=up(S*ab(density['gamma_high']))
    infinite_far=up(ab(split['deep_high_boundary'])/S+4*Theta*ab(split['deep_high_boundary'])*far)
    infinite_reference=[ab(row['source_common_mass']['common_d']['infinite8192up']) for row in source['rows']]
    del split,density,vcap,W;gc.collect()
    def common(n):return [min(old_common[n][g],up(sum((caps[n][w] for w in GROUPS[g]),arb(0)))) for g in range(2)]
    def source_row(n):
        cm=common(n);t=up(low[n]+cm[0]+cm[1]+infinite);C=modalref[n]
        if not(t+lamb[n]<arb(2)**-30 and aa[n]*(C+t)<arb(1)/128):raise ArithmeticError('Complete original Hessian physical domain unpaid')
        square=up(arb(23)*t*t/18);remainder=up(270*aa[n]*(C+t)*(C*t+t*t/2));dq=[]
        for mat in range(2):
            vals=[]
            for w,row in enumerate(kernels[n][mat]):
                vals.append(up(row[0]*low[n]+row[14]*infinite+
                    support(row[1:7],caps[n][:6],cm[0],permutations[n][mat][w][0])+
                    support(row[7:14],caps[n][6:],cm[1],permutations[n][mat][w][1])))
            dq.append(vals)
        def projected_square(lower):
            # Whole input blocks below lower/2 form f; Q(f) has no target
            # frequency. For g=e-f, ||f+s*g||<=||e|| in the pointwise
            # Fourier l1 norm, so Q(e)-Q(f)<= (23/9)*t*||g||.
            G=low[n] if 2*92>=lower else arb(0)
            for group in range(2):
                selected=[caps[n][w] for w in GROUPS[group] if 2*WINDOWS[w][1]>=lower]
                G+=min(cm[group],up(sum(selected,arb(0))))
            G=min(t,up(G+infinite))
            return min(square,up((arb(23)/9)*t*G))
        squares=[projected_square(lo) for lo,hi in WINDOWS]
        infinite_square=projected_square(8192)
        return cm,t,square,remainder,dq,squares,infinite_square
    checkpoints=[];infinite_steps=[];last_infinite_sources=None
    def checkpoint(step):
        checkpoints.append(dict(step=step,cell12_caps=[pack(z) for z in caps[0]],cell13_caps=[pack(z) for z in caps[1]],
                                cell12_common=[pack(z) for z in common(0)],cell13_common=[pack(z) for z in common(1)],complete_infinite_cap=pack(infinite)))
        print(json.dumps(dict(event='same_R100_window13_finite_substitution',step=step,
              cell12_first2_display=[str(z) for z in caps[0][:2]],cell13_first2_display=[str(z) for z in caps[1][:2]],infinite_display=str(infinite),
              elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    checkpoint(0)
    for step in range(1,a.steps+1):
        src=arb_mat(213,13);infinite_sources=[]
        for n in range(213):
            cm,t,square,remainder,dq,squares,infinite_square=source_row(n)
            for w in range(13):src[n,w]=up(qref[n][w]+max(dq[0][w],dq[1][w])+squares[w]+remainder)
            # Centre support is2..92. Below4098 all input sums are below8192;
            # the entire last rest window is conservatively kept, as is all infinity.
            dq_inf=up((arb(23)/9)*modalref[n]*(caps[n][-1]+infinite))
            infinite_sources.append(up(infinite_reference[n]+dq_inf+infinite_square+remainder))
        images=arb_mat(213,13)
        for (mm,ee),ws in zip(gamma_arrays,gamma_window_groups):
            green=arb_mat(213,213);z=0
            for k in range(213):
                for n in range(k,213):green[k,n]=arb(mm[z])*arb(2)**ee[z];z+=1
            selected=arb_mat([[src[n,w] for w in ws] for n in range(213)])
            product=green*selected
            for j,w in enumerate(ws):
                for n in range(213):images[n,w]=product[n,j]
            del green,selected,product
        nxt=[]
        for n in range(213):
            vals=[]
            for w in range(13):
                g=int(w>=6);v=min(caps[n][w],up(images[n,w]+far_source[n][g]))
                if not(v.is_finite() and v>0 and v<=caps[n][w]):raise ArithmeticError('Monotone finite positive window substitution failed')
                vals.append(v)
            nxt.append(vals)
        infinite_image=up(GI*sum(infinite_sources,arb(0))+infinite_far)
        next_infinite=min(infinite,infinite_image)
        if not(next_infinite.is_finite() and next_infinite>0 and next_infinite<=infinite):raise ArithmeticError('Complete infinite finite substitution failed')
        infinite_steps.append(dict(step=step,before=pack(infinite),complete_image=pack(infinite_image),after=pack(next_infinite)))
        if step==a.steps:last_infinite_sources=list(map(pack,infinite_sources))
        infinite=next_infinite;caps=nxt
        if step&(step-1)==0 or step==a.steps:checkpoint(step)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual13-window RSS guard')
    # Endpoint: canonical/physical initial intersection, unchanged complete
    # two-material source columns, and this same field's current13 windows.
    sg={tuple(r['window']):r for r in scalar['rows']};cg={tuple(r['window']):r for r in canonical['rows']}
    initcols=[];kcols=[]
    for lo,hi in WINDOWS:
        cover=next(k for k in sg if k[0]<=lo and hi<=k[1])
        initcols.append(ab(cg[cover]['chosen_initial_column']))
        kcols.append([ab(sg[cover]['source_two_material_to_cut'][mat]) for mat in MATERIALS[:2]])
    cm,t,square,remainder,dq,squares,infinite_square=source_row(0)
    endpoint_rows=[]
    epsilon=ab(field['point_physical_epsilon_prime'])
    for w,window in enumerate(WINDOWS):
        g=int(w>=6);incoming=up(initcols[w]*caps[1][w])
        ref=up(sum((kcols[w][mat]*min(up(poly[0][name][w]+tails[0][name]),bandref[0][name][g]) for mat,name in enumerate(MATERIALS[:2])),arb(0)))
        diff=up(sum((kcols[w][mat]*dq[mat][w] for mat in range(2)),arb(0))+sum(kcols[w],arb(0))*up(squares[w]+remainder))
        val=up(incoming+ref+diff);whole=up(caps[0][w]*epsilon)
        chosen=min(val,whole,ab(canonical['actual_R100_head_band_masses'][g]))
        endpoint_rows.append(dict(window=window,initial_column=pack(initcols[w]),initial_cell13_mass=pack(caps[1][w]),incoming=pack(incoming),
             complete_reference_source=pack(ref),complete_error_source=pack(diff),endpoint_sum=pack(val),
             whole_cell_same_window_bound=pack(whole),chosen_same_field_bound=pack(chosen),
             source_two_material_kernels={name:pack(kcols[w][m]) for m,name in enumerate(MATERIALS[:2])},
             DQ_two_material_source={name:pack(dq[m][w]) for m,name in enumerate(MATERIALS[:2])},
             full_new_quadratic_source=pack(squares[w]),full_mean_inverse_difference_source=pack(remainder)))
    bands=[]
    cm13=common(1)
    for g,indices in enumerate(GROUPS):
        incoming=support([initcols[w] for w in indices],[caps[1][w] for w in indices],cm13[g])
        reference=arb(0)
        for m,mat in enumerate(MATERIALS[:2]):
            weighted=up(sum((kcols[w][m]*poly[0][mat][w] for w in indices),arb(0))+max(kcols[w][m] for w in indices)*tails[0][mat])
            reference+=min(weighted,up(max(kcols[w][m] for w in indices)*bandref[0][mat][g]))
        reference=up(reference)
        # Aggregate the positive DQ coefficients before consuming the same
        # input masses, and pay each shared square/T remainder once.
        coeff=[up(sum((kcols[w][m]*kernels[0][m][w][j] for w in indices for m in range(2)),arb(0))) for j in range(15)]
        dqcost=up(coeff[0]*low[0]+coeff[14]*infinite+
                  support(coeff[1:7],caps[0][:6],cm[0])+support(coeff[7:14],caps[0][6:],cm[1]))
        other=up(max(sum(kcols[w],arb(0)) for w in indices)*up(squares[indices[0]]+remainder))
        val=up(incoming+reference+dqcost+other)
        sum_individual=up(sum((ab(endpoint_rows[w]['chosen_same_field_bound']) for w in indices),arb(0)))
        chosen=min(val,sum_individual,ab(canonical['actual_R100_head_band_masses'][g]),up(cm[g]*epsilon))
        bands.append(dict(group=('near','rest')[g],incoming=pack(incoming),complete_reference_source=pack(reference),
             DQ_source_readout=pack(dqcost),shared_full_new_square_and_mean_inverse=pack(other),
             aggregate_endpoint_sum=pack(val),sum_separate_window_bounds=pack(sum_individual),chosen_same_field_bound=pack(chosen),
             shared_complete_inverse_reference_tail_paid_once=True,shared_square_and_T_difference_paid_once=True))
    infinite_point=up(infinite*epsilon);infinite_head=min(infinite_point,ab(canonical['actual_R100_head_band_masses'][2]))
    actual=[r['chosen_same_field_bound'] for r in bands]+[pack(infinite_head)]
    rows=[]
    for n in range(213):
        cmn,tn,sqn,rn,dqn,squares_n,infinite_square_n=source_row(n)
        rows.append(dict(cell=n+12,window_caps=[pack(z) for z in caps[n]],near_rest_common_caps=list(map(pack,cmn)),
             fixed_low_cap=pack(low[n]),complete_infinite_cap=pack(infinite),total_error=pack(tn),
             full_new_quadratic_source=pack(sqn),full_new_quadratic_window_sources=list(map(pack,squares_n)),full_new_quadratic_infinite_source=pack(infinite_square_n),full_mean_inverse_difference_source=pack(rn),
             DQ_two_material_window_sources={name:list(map(pack,dqn[m])) for m,name in enumerate(MATERIALS[:2])}))
    output=dict(schema='same-R100-restricted-inner13-window-and-infinite-finite-bootstrap-head-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
      all_gates=True,gates=dict(same_existing_complete_R100_field=True,exact_restricted_original_profile_and_all_T_axes=True,
      all213_source_cells_and_replayed_eleven_actual_green_triangles=True,all13_even_windows94to8190=True,actual_CsLambda_DQ_two_material_frequency_support=True,
      common_near_rest_mass_constraints_retained=True,all_full_new_quadratic_and_mean_inverse_remainder=True,exact_quadratic_support_only_with_complete_T_unchanged=True,
      all_true_far_in_initial_field_and_causal_source=True,all_infinite_frequencies_retained_and_repaid=True,all_complete_Hessian_physical_domains=True,
      every_comparison_finite_positive_outward=True,finite_monotone_substitution_only=True,original_endpoint_columns_and_frame_strip_paid=True,
      shared_reference_inverse_tail_once_in_common_readout=True,shared_square_T_once_in_common_readout=True),
      input_identities=ids,source_parts=partids,source_sha256=sha(__file__),steps=a.steps,windows=WINDOWS,
      domain=field['domain'],parent_full_domain=canonical['domain'],head_strip=canonical['head_strip'],head_bands=canonical['head_bands'],units=canonical['units'],
      actual_R100_head_band_masses=actual,actual_R100_head_window_masses=[r['chosen_same_field_bound'] for r in endpoint_rows],
      checkpoints=checkpoints,rows=rows,endpoint_rows=endpoint_rows,complete_band_budgets=bands,
      endpoint_reuses_original_94to96_columns_for_both_singleton_windows=True,
      complete_infinite_cap=pack(infinite),infinite_readout=dict(whole_cell_point_bound=pack(infinite_point),chosen_same_field_bound=pack(infinite_head),physical_epsilon_prime=field['point_physical_epsilon_prime']),
      infinite_steps=infinite_steps,last_infinite_source_caps=last_infinite_sources,infinite_kernel=pack(GI),complete_infinite_far_source=pack(infinite_far),
      exact_quadratic_support_bound='For target m>=a, f is the union of full input blocks with2*upper<a, g is its frequency complement. Q(f) has no target frequency. ||f+s*g||<=t for0<=s<=1, hence projected Q(e)<=min(23/18*t^2,23/9*t*G). G consumes selected window caps and original shared near/rest mass, with all infinite modes.',
      infinite_centre_support='DQ(C)e can enter8192up only from retained rest4098to8190 or infinite inputs; all other input modes at most4096 plus centre92 remain below8192. Complete Q(e), T and reference inverse tails retain all infinite modes.',fixed_far_cap=pack(far),
      complete_mean_inverse_far=True,no_ODE_or_new_Green_or_geometry=True,original_eleven_window_Green_replay_consumed=True,new_fixedpoint_or_outer_cut_claimed=False,
      elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_bytes(gzip.compress((json.dumps(output,separators=(',',':'))+'\n').encode(),mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Split actual output to retain repository artifact limits')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual13-window final RSS guard')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,
          head_display=[str(ab(v)) for v in actual],window_display=[str(ab(v)) for v in output['actual_R100_head_window_masses']],
          elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)


if __name__=='__main__':main()
