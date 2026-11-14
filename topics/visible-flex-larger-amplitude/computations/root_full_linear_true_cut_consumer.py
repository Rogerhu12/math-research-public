#!/usr/bin/env python3
"""Complete actual low46 cut bounds around full L_R on the R100 unit domain.

Existing true solution only: finite a-posteriori modal substitutions retain
the separate common error radius. R116 complete Taylor remainder and the
new actual centre Jacobian are used with the R123 true beta interface.
Any closure result is only for this low46 projected exterior problem.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from fractions import Fraction as F
from root_hybrid46_cut_consumer import exact as num,up,record,exp_bounds,sum_up

PINS={
 'centre':('notes/2026-11-13-root-full-linear-source-r1-summary.json','58ae9b5d9332ce09530d2380b00348eb50efa3693a27294ecf185d9ea6f175db'),
 'ball':('notes/2026-11-13-root-full-linear-recentring-r1.json','a04967ff99f5c119636227b7e84c9be02a0fb80cec9d07ae7c8af69e03b89362'),
 'head':('notes/2026-11-13-inner-aux-bootstrap-beta-interface-r1.json.gz','1bd50cb4f32bb17d1238dd2487df379526246651a5ebbf1ec6fdf5809699f5ea'),
 'oldhead':('notes/2026-11-13-root-r100-source-reweight-r1.json','617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'),
 'spectral':('notes/2026-11-13-closure-r100-spectral-r1.json','1c12cde9889048daaced137a79a1504a4780d7f5315a5950c5fde4fda0d38651'),
 'budget':('notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json','86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'),
 'chart':('notes/2026-11-13-root-r100-hybrid46-exact-ledger.json','7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9')}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.load(gzip.open(p,'rt')) if p.suffix=='.gz' else json.loads(p.read_text())
def abs_interval(x):return max(abs(num(x[0])),abs(num(x[1])))
def support(coeffs,caps,total):
    left=total;ans=F(0)
    for i in sorted(range(len(caps)),key=lambda i:coeffs[i],reverse=True):
        amount=min(left,caps[i]);ans+=coeffs[i]*amount;left-=amount
        if not left:break
    return up(ans)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--topic',type=Path,required=True);p.add_argument('--derivative',type=Path,required=True)
    p.add_argument('--derivative-sha256',required=True);p.add_argument('--derivative-resource',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--rounds',type=int,default=10)
    a=p.parse_args();began=time.monotonic();gates={};data={};ids={}
    def gate(k,v):
        gates[k]=bool(v)
        if not v:raise ArithmeticError(k)
    for k,(rel,sha) in PINS.items():
        path=a.topic/rel;gate('identity_'+k,digest(path)==sha);data[k]=read(path);ids[k]={'path':rel,'sha256':sha}
        if 'all_gates' in data[k]:gate('all_gates_'+k,data[k]['all_gates'])
    gate('actual_new_centre_derivative_identity',digest(a.derivative)==a.derivative_sha256)
    dn=read(a.derivative);dr=read(a.derivative_resource)
    gate('actual_new_centre_derivative_formal_zero',dr['exitcode']==0 and dr['termination_signal'] is None)
    gate('same_centre_for_entire_new_derivative',dn['centre_summary_sha256']==PINS['centre'][1])
    gate('all_original_material_and_actual_geometry',dn['full_material_cover'] and len(dn['groups'])==18 and sum(g['rows'] for g in dn['groups'])==10878 and sum(g['original_panels'] for g in dn['groups'])==10793)
    gate('full_exact_Laurent_product_rule',dn['exact_algebra_checks']['all_full_product_rule_coefficients_equal'] and dn['exact_algebra_checks']['exact_rational_equalities']==4232)
    gate('all_derivative_coefficients_checked_finite',dn['all_finite_entries_checked'])
    centre,b,head,spec,budget,chart=[data[k] for k in ('centre','ball','head','spectral','budget','chart')]
    modes=list(range(2,93,2));M=46;r0=up(num(b['a_posteriori_radius']));V0=F(1,2**40);S=F(8)
    gate('same_existing_R100_true_low46_solution',spec['same_existing_low_centre'] and spec['complete_R100_primary_sha256']==PINS['oldhead'][1])
    gate('true_full_unit_R100_beta_domain',head['all46_modes']==modes)
    candidates=[row for row in head['rows'] if num(row['radius_T'])==1]
    gate('one_complete_unit_domain_head',len(candidates)==1);hb=candidates[0]
    gate('same_positive_true_far',0<num(hb['true_far_added_once'])==num(data['oldhead']['true_far_added_once_per_whole_mass']))
    gate('full_weighted_mean_inverse_Cauchy_domain',r0<F(131,10**15) and num(b['centre_norm_upper'])+r0<S and F(3,2)*V0*S<F(1,64))
    A=[[max(num(g['weighted_source_jacobian_upper'][i][j]) for g in dn['groups']) for i in range(92)] for j in range(M)]
    for gi,g in enumerate(dn['groups']):
        gate('full_matrix_shape_'+str(gi),len(g['weighted_source_jacobian_upper'])==92 and all(len(row)==46 for row in g['weighted_source_jacobian_upper']))
        gate('own_complete_tail_retained_'+str(gi),all(0<=num(g['weighted_complete_derivative_remainder_upper'][i][j])<=num(g['weighted_source_jacobian_upper'][i][j]) for i in range(92) for j in range(46)))
    d=[];beta=[];G=[];Gdn=[];kernel=[];axes=[];Z=[];spectral=[];headcut=[]
    for j,m in enumerate(modes):
        br=budget['mode_rows'][j];hr=hb['all46_mode_rows'][j]
        gate('same_original_mode_'+str(m),br['mode']==hr['mode']==chart['rows'][j]['mode']==spec['final_caps'][j]['mode']==centre['cut_rows'][j]['mode']==m)
        cap=next(v for v in br['densities'] if v['density']=='weak_candidate_cap');dc=next(v for v in br['densities'] if v['density']=='weak_local_rho_16')
        axis=num(chart['rows'][j]['chosen_axis']);axes.append(axis)
        kernel.append(up(num(cap['canonical_cut_absolute_mode_bound'])/(F(17,16)**2*axis)))
        bm=num(hr['complete_true_beta_Wsigma1']);beta.append(up(num(br['complete_weighted_inner_K_trace_to_field_norm'])*bm))
        headcut.append(up(num(br['inner_K_trace_to_canonical_cut_absolute'])*num(hr['complete_true_beta_cosine_K_coefficient'])/axis))
        spectral.append(up(num(spec['final_caps'][j]['bound'])/exp_bounds(m*(F(18,125)-F(1,64)))[0]))
        for component in ('P','K'):
            d.append(num(centre['mode_green_norms'][str(m)][component]));Z.append(num(centre['true_linear_norms'][str(m)][component]))
            G.append(up(num(cap[component+'_sup'])/(F(17,16)**2)));Gdn.append(2*num(dc[component+'_sup']))
    gate('all_positive_original_operators',all(v>=0 for row in A for v in row) and all(v>=0 for v in G+Gdn+kernel+d+beta+Z+headcut))
    caps=[min(r0,up(spectral[i//2]+Z[i]),up(d[i]+beta[i//2]+Gdn[i]*r0)) for i in range(92)]
    initial=caps[:];eps3=up(135*V0*S*r0*r0);qtotal=up(F(23,18)*r0*r0)
    def sources(caps):
        am={}
        for j,m in enumerate(modes):am[m]=am[-m]=up((caps[2*j]+caps[2*j+1])/2)
        lin=[];quad=[]
        for j,m in enumerate(modes):
            lin.append(support(A[j],caps,r0))
            conv=sum((v*am.get(m-n,F(0)) for n,v in am.items()),F(0))
            quad.append(min(up(F(23,9)*conv),qtotal))
        return lin,quad
    rounds=[]
    for iteration in range(a.rounds):
        lin,quad=sources(caps)
        new=[min(caps[i],up(d[i]+beta[i//2]+G[i]*(lin[i//2]+quad[i//2]+eps3))) for i in range(92)]
        gate('finite_existing_solution_substitution_'+str(iteration),all(0<=x<=y for x,y in zip(new,caps)))
        rounds.append({'round':iteration+1,'caps':[record(x) for x in new],'separate_sum_of_component_caps':record(sum_up(new)),'common_R119_radius_still_retained':record(r0)})
        caps=new
    lin,quad=sources(caps);rows=[];base=[];errors=[]
    for j,m in enumerate(modes):
        base.append(up(abs_interval(centre['cut_rows'][j]['full_fixed_centre_cut_minus_original_Q'])/axes[j]))
        err=up(kernel[j]*(lin[j]+quad[j]+eps3)+headcut[j]);errors.append(err)
        rows.append({'mode':m,'P_error_cap':record(caps[2*j]),'K_error_cap':record(caps[2*j+1]),'complete_centre_derivative_source':record(lin[j]),'quadratic_error_source':record(quad[j]),'complete_common_higher_order_source':record(eps3),'source_to_original_cut_axis':record(kernel[j]),'constant_fixed_centre_cut':record(base[j]),'complete_true_head_cut_individual':record(headcut[j]),'parameter_dependent_cut_error':record(err),'complete_cut_value_individual':record(up(base[j]+err))})
    comb=[sum_up(kernel[j]*A[j][i] for j in range(6,M)) for i in range(92)]
    tl=min(sum_up(kernel[j]*lin[j] for j in range(6,M)),support(comb,caps,r0))
    tq=min(sum_up(kernel[j]*quad[j] for j in range(6,M)),support(kernel[6:],quad[6:],qtotal))
    tr=up(max(kernel[6:])*eps3);th=num(hb['T_head_complete_in_original_cut_norm'])
    tbase=sum_up(base[6:]);terr=up(tl+tq+tr+th);tmap=up(tbase+terr)
    serr=max(errors[:6]);smap=max(up(base[j]+errors[j]) for j in range(6))
    errnorm=max(serr,terr);mapnorm=max(smap,tmap);working=F(3,4);lip=up(errnorm/(1-working))
    closure={'actual_complete_selfmap_at_radius3over4':mapnorm<working,'complete_parameter_Cauchy_contraction':lip<1}
    result={'schema':'full-linear-true-low46-cut-consumer-v1','scope':'Actual full unit-domain R100 inner head and existing true low46 projected outer solution, all46 cut parameters. Even if closure gates pass, middle/high feedback and the all-frequency outer PDE remain open.','all_gates':all(gates.values()),'gates':gates,'closure_gates':closure,'all46_projected_cut_consistency_paid':all(closure.values()),'all_frequency_PDE_or_closed_surface_claimed':False,'input_identities':ids,'derivative_sha256':a.derivative_sha256,'derivative_resource_sha256':digest(a.derivative_resource),'source_sha256':digest(Path(__file__)),'helper_sha256':digest(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),'common_joint_error_radius':record(r0),'normalized_total_radius':record(S),'Vmax':record(V0),'complete_shared_higher_order_source':record(eps3),'shared_quadratic_norm':record(qtotal),'initial_caps':[record(x) for x in initial],'rounds':rounds,'mode_rows':rows,'T_constant_fixed_centre':record(tbase),'T_complete_linear_correction':record(tl),'T_quadratic_correction':record(tq),'T_common_higher_order_correction':record(tr),'T_complete_true_head_once_far':record(th),'T_complete_parameter_dependent_error':record(terr),'T_full_map':record(tmap),'S_full_map_max':record(smap),'S_parameter_dependent_error_max':record(serr),'unit_domain_error_norm':record(errnorm),'working_radius':record(working),'full_map_norm':record(mapnorm),'Cauchy_Lipschitz_bound':record(lip),'complete_mean_inverse_and_positive_far_retained':True,'radial_sup_before_sum':True,'no_new_fixed_field_solution_claimed':True,'elapsed_seconds':time.monotonic()-began,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    if a.out.exists():raise FileExistsError('Fresh complete output required')
    raw=(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if a.out.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    if len(raw)>=5_000_000 or len(raw)>1_000_000 and a.out.suffix!='.gz':raise ValueError('Output file size rule')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(raw)
    print(json.dumps({'all_gates':result['all_gates'],'closure_gates':closure,'S_full_map':float(smap),'T_full_map':float(tmap),'T_linear':float(tl),'T_quadratic':float(tq),'T_high_order':float(tr),'T_head':float(th),'parameter_Lip':float(lip),'sha256':digest(a.out),'seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
