#!/usr/bin/env python3
"""A posteriori modal caps for the EXISTING R105 true solution; full source kept.

Use the actual R116 centre derivative, exact Q(h) frequency convolution, and
the full mean/inverse higher Taylor remainder. No ODE or interval flow rerun.
The R105 common l1 error remains a separate simultaneous constraint.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from root_hybrid46_cut_consumer import exact as num,up,record,exp_bounds,sum_up

PINS={
 'derivative':('notes/2026-11-13-root-finite-dn4-normalized-r2.json.gz','58e86a63b9b23894c45477fdcbbbe172c36ff8087ff8739e475ff8ed90d8d57d'),
 'derivative_gates':('notes/2026-11-13-root-finite-dn4-normalized-exact-gates.json','a476cf4a353a2fca325ea530718efbeb70820032bbb33080de23672eb4b3aa7c'),
 'ball':('notes/2026-11-13-root-signed46-projected-ball-r1.json','cbf948ece6dcbad4f7a11c85d7ad721006fd7cf295da9baea87cf4f9de80c0a8'),
 'ordered':('notes/2026-11-13-root-signed46-ordered-v2-summary.json','e30a95b57dc4ba7b64af5f6e95ea30b233611c3703b5f5111793482b368a8ca3'),
 'fields':('notes/2026-11-12-root-linear-centre-local-restored-r1-summary.json','94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'),
 'head':('notes/2026-11-13-root-r100-source-reweight-r1.json','617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'),
 'spectral':('notes/2026-11-13-closure-r100-spectral-r1.json','1c12cde9889048daaced137a79a1504a4780d7f5315a5950c5fde4fda0d38651'),
 'budget':('notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json','86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'),
 'chart':('notes/2026-11-13-root-r100-hybrid46-exact-ledger.json','7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9')}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.load(gzip.open(p,'rt')) if p.suffix=='.gz' else json.loads(p.read_text())

def interval_abs(x):return max(abs(num(x[0])),abs(num(x[1])))

def constrained_dot(coeffs,caps,total):
    """Exact support function of 0<=x_i<=caps_i, sum x_i<=total."""
    left=total;answer=F(0)
    for i in sorted(range(len(caps)),key=lambda i:coeffs[i],reverse=True):
        amount=min(left,caps[i]);answer+=coeffs[i]*amount;left-=amount
        if not left:break
    return up(answer)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--rounds',type=int,default=8)
    a=ap.parse_args();beg=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh output path required')
    data={};ids={};gates={}
    def gate(k,v):
        gates[k]=bool(v)
        if not v:raise ArithmeticError(k)
    for k,(rel,sha) in PINS.items():
        p=a.topic/rel;gate('identity_'+k,digest(p)==sha);data[k]=read(p);ids[k]={'path':rel,'sha256':sha}
        if 'all_gates' in data[k]:gate('all_gates_'+k,data[k]['all_gates'])
    dn,b,op,fields,head,spec,budget,chart=[data[k] for k in ('derivative','ball','ordered','fields','head','spectral','budget','chart')]
    modes=list(range(2,93,2));M=len(modes);r0=up(num(b['a_posteriori_radius']))
    V0=F(1,2**40);S=F(8)
    gate('same_existing_R100_true_low46_solution',spec['same_existing_low_centre'] and spec['complete_R100_primary_sha256']==PINS['head'][1])
    gate('complete_stable_derivative',dn['full_material_cover'] and dn['all_finite_entries_checked'] and sum(g['rows'] for g in dn['groups'])==10793 and len(dn['groups'])==18)
    gate('joint_radius_and_weighted_complete_Cauchy_domain',r0<F(1,10**9) and num(b['centre_norm_upper'])+r0<S and F(3,2)*V0*S<F(1,64))
    A=[[max(num(g['weighted_source_jacobian_upper'][i][j]) for g in dn['groups']) for i in range(2*M)] for j in range(M)]
    d=[];beta=[];G=[];Gdn=[];kernel=[];axes=[];Z=[];spectral=[]
    for j,m in enumerate(modes):
        br=budget['mode_rows'][j];gate('same_mode_'+str(m),br['mode']==head['mode_rows'][j]['mode']==chart['rows'][j]['mode']==spec['final_caps'][j]['mode']==m)
        cap=next(v for v in br['densities'] if v['density']=='weak_candidate_cap')
        dc=next(v for v in br['densities'] if v['density']=='weak_local_rho_16')
        axis=num(chart['rows'][j]['chosen_axis']);axes.append(axis)
        kernel.append(up(num(cap['canonical_cut_absolute_mode_bound'])/(F(17,16)**2*axis)))
        bm=num(head['mode_rows'][j]['both_strips']['Wsigma1']['complete']['chosen_complete_true_DN_minus_exact_linear']['uniform_value_upper'])
        beta.append(up(num(br['complete_weighted_inner_K_trace_to_field_norm'])*bm))
        spec_sigma=up(num(spec['final_caps'][j]['bound'])/exp_bounds(m*(F(18,125)-F(1,64)))[0]);spectral.append(spec_sigma)
        zrow=fields['true_linear_selected_component_mass'].get(str(m),fields['original_mode_component_mass'].get(str(m),{'P':0,'K':0}))
        for component in ('P','K'):
            d.append(num(op['mode_residual_norms'][str(m)][component]));Z.append(num(zrow[component]))
            G.append(up(num(cap[component+'_sup'])/(F(17,16)**2)))
            Gdn.append(2*num(dc[component+'_sup']))
    gate('positive_all_matrix_and_kernel_entries',all(x>=0 for row in A for x in row) and all(x>=0 for x in G+Gdn+kernel+d+beta+Z))
    caps=[min(r0,up(spectral[i//2]+Z[i]),up(d[i]+beta[i//2]+Gdn[i]*r0)) for i in range(2*M)]
    initial=caps[:]
    eps3=up(135*V0*S*r0*r0)
    qtotal=up(F(23,18)*r0*r0)
    def source_bounds(caps):
        am={}
        for j,m in enumerate(modes):am[m]=am[-m]=up((caps[2*j]+caps[2*j+1])/2)
        linear=[];quad=[]
        for j,m in enumerate(modes):
            linear.append(constrained_dot(A[j],caps,r0))
            q=sum((x*am.get(m-n,F(0)) for n,x in am.items()),F(0))
            quad.append(min(up(F(23,9)*q),qtotal))
        return linear,quad
    rounds=[]
    for iteration in range(a.rounds):
        lin,q=source_bounds(caps)
        nxt=[min(caps[i],up(d[i]+beta[i//2]+G[i]*(lin[i//2]+q[i//2]+eps3))) for i in range(2*M)]
        gate('finite_existing_solution_substitution_'+str(iteration),all(0<=x<=y for x,y in zip(nxt,caps)))
        rounds.append({'round':iteration+1,'caps':[record(x) for x in nxt],
          'sum_caps_is_only_a_separate_upper':record(sum_up(nxt)),
          'common_R105_joint_radius_retained':record(r0)})
        caps=nxt
    lin,q=source_bounds(caps)
    outrows=[];outer_errors=[];headcut=[];basecut=[]
    for j,m in enumerate(modes):
        base=interval_abs(op['cut_rows'][j]['signed_affine_cut_minus_original_Q'])/axes[j]
        bm=num(head['mode_rows'][j]['both_strips']['Wsigma1']['complete']['chosen_complete_true_DN_minus_exact_linear']['uniform_value_upper'])
        angular=exp_bounds(F(m,64))[0]
        hb=num(budget['mode_rows'][j]['inner_K_trace_to_canonical_cut_absolute'])*bm/(axes[j]*(1+m)*angular)
        error=up(kernel[j]*(lin[j]+q[j]));outer_errors.append(error);headcut.append(up(hb));basecut.append(up(base))
        outrows.append({'mode':m,'P_error_cap':record(caps[2*j]),'K_error_cap':record(caps[2*j+1]),
          'complete_centre_derivative_source':record(lin[j]),'quadratic_error_source':record(q[j]),
          'source_to_normalized_cut':record(kernel[j]),'fixed_signed_affine_cut_absolute':record(up(base)),
          'outer_correction_without_common_high_order':record(error),
          'complete_head_cut_using_current_R100_bound':record(up(hb)),
          'full_cut_value_individual_upper':record(up(base+hb+error+kernel[j]*eps3))})
    # Shared complete higher-order source mass is paid once through max column.
    tbase=sum_up(basecut[6:]);terror=sum_up(outer_errors[6:]);trem=up(max(kernel[6:])*eps3)
    thead=sum_up(headcut[6:])
    # Head row caps each contain far; recover a legal single-far sum directly.
    far=num(head['true_far_added_once_per_whole_mass']);nonfar=[];headkern=[]
    for j,m in enumerate(modes):
        row=head['mode_rows'][j]['both_strips']['Wsigma1']
        nonfar.append(num(row['old_auxiliary'])+num(row['new_complete_difference']))
        headkern.append(up(num(budget['mode_rows'][j]['inner_K_trace_to_canonical_cut_absolute'])/(axes[j]*(1+m)*exp_bounds(F(m,64))[0])))
    thead_once=up(sum_up(headkern[j]*nonfar[j] for j in range(6,M))+max(headkern[6:])*far)
    result={'schema':'true-low46-modal-correction-v1','scope':'Finite a posteriori bounds for the same existing R105 true projected solution on R100; old complete inner-head bounds retained, all-cut acceptance separate',
      'all_gates':all(gates.values()),'gates':gates,'input_identities':ids,'source_sha256':digest(Path(__file__)),
      'helper_sha256':digest(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),
      'common_joint_error_radius':record(r0),'normalized_total_field_radius':record(S),'Vmax':record(V0),
      'complete_high_order_source_mass':record(eps3),'quadratic_shared_norm_upper':record(qtotal),
      'initial_component_caps':[record(x) for x in initial],'rounds':rounds,'mode_rows':outrows,
      'T_fixed_affine_cut':record(tbase),'T_outer_linear_and_quadratic_correction':record(terror),
      'T_complete_shared_high_order_correction':record(trem),'T_outer_without_head':record(up(tbase+terror+trem)),
      'T_current_inner_head_once_far':record(thead_once),
      'T_current_full_value':record(up(tbase+terror+trem+thead_once)),
      'S_current_full_values':[outrows[j]['full_cut_value_individual_upper'] for j in range(6)],
      'whole_common_l1_constraints_retained':True,'frequency_zero_and_complete_mean_inverse_tail_retained':True,
      'source_residual_r1_rejected_DN_not_used':True,'new_fixed_point_claimed':False,
      'all46_cut_selfmap_or_contraction_claimed':False,'elapsed_seconds':time.monotonic()-beg,
      'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    raw=(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if len(raw)>1_000_000:
        if a.out.suffix!='.gz':raise ValueError('Large result needs gzip')
        raw=gzip.compress(raw,mtime=0)
    elif a.out.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000:raise ValueError('Per-file cap')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(raw)
    print(json.dumps({'all_gates':result['all_gates'],'T_outer_without_head':float(tbase+terror+trem),'T_correction':float(terror),'T_high_order':float(trem),'T_head':float(thead_once),'S_values':[r['display_upward'] for r in result['S_current_full_values']],'sha256':digest(a.out),'seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
