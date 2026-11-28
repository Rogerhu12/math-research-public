"""Whole original V/SV admission and only new exact root-right-matrix inequalities."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
import json
from fourfold_codazzi_negative_circle_inverse_saved_bounds import endpoints
FILES = {'V': ['notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json', 27645, 'd4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9'], 'Vs': ['scripts/fourfold_codazzi_common_radial_potential_budget.py', 30953, '042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7'], 'Vw': ['scripts/fourfold_codazzi_common_radial_potential_budget_public_worker.py', 17311, 'f67fa3f9b63834715d0aa7711bee2e836979c55dacd3c83055c09dfd035e2cd0'], 'Vm': ['notes/2026-11-15-R133-common-radial-potential-budget-CI-inputs.json', 11519, '44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437'], 'SV': ['notes/saved_genuine_first_column_density_one_sources_ci/run-43724817779-1/execution.json', 42780, '107845165a3fefa5b0fb6e244e4efd0eb90bfdddda2b93977bf8962b4636f649'], 'SVs': ['scripts/fourfold_codazzi_saved_genuine_first_column_density_one_sources.py', 28530, '09a2cb90b2d86d0f81a2ae0fae2cb3db1500878c6611ea142eae651d46d158d8'], 'SVw': ['scripts/fourfold_codazzi_saved_genuine_first_column_density_one_sources_public_worker.py', 34229, 'add608a27da6cdca232b2c1f398630ab1e0066e97f7775eee814dd606e65fcbc'], 'SVm': ['notes/2026-11-15-R133-saved-genuine-first-column-density-one-sources-CI-inputs.json', 36386, 'ae9c1bbeccb5c2718ef98f3c0c473ab325861e7f67d5e77b3f4a3a9903f9f38e'], 'IN': ['results/R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md', 33894, 'd4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75'], 'SE': ['results/R133-supplement-natural-stable-port-Fredholm-and-exact-reference-elimination.md', 21356, '93266089706d71dfa9ee6e5fd48be9cd796354a25b5801f0386d225e4fea2572'], 'WUA': ['results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md', 40111, '9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad'], 'SVproof': ['results/R133-supplement-actual-saved-genuine-first-column-density-one-SV-sources.md', 16144, '12263fd8d36ffac227c5645d6a89e49917385ea446a92d879448ed362b295257'], 'GIV': ['results/R149-supplement-actual-sharpened-infinite-source-from-both-Airy-root-values.md', 2918, 'f36e4deaf7425bc833ec3341cf8317f7b11b10ba741d6dcf9e2a28c7fc9ce5fe'], 'GDM': ['results/R149-supplement-exact-root-matched-right-matrix-and-signed-physical-trial-exchange.md', 8028, '2f5b613c16818d631de92b4522c53224c1a5cdc7e9522b3560818294202bc83b'], 'endpoints': ['scripts/fourfold_codazzi_negative_circle_inverse_saved_bounds.py', 8433, 'e28a39e6a5380000f229022ebe8d354ec80f14d63f1d82d92feaf44de72cbfde']}

def require(ok,label):
    if not ok:raise ValueError(label)

def admit(topic):
    docs={}
    for k,(name,size,digest) in FILES.items():
        raw=(topic/name).read_bytes();require((len(raw),sha256(raw).hexdigest())==(size,digest),k)
        if name.endswith('.json'):docs[k]=json.loads(raw)
    for role,run,event,count,gates in [('V','43685624307','1ca03990aed2531717528d8f51d1156138f1988a',20,16),
            ('SV','43724817779','cbb63584806fa90e7c5532170b5ac75abb1bdf0c',77,21)]:
        e=docs[role];s=e['actual_scientific_receipt']
        require(e['run_id']==run and e['run_attempt']=='1'
          and e['workflow_commit']==event and e['complete'] and s['complete'] and s['proved']
          and e['actual_returncode']==s['actual_returncode']==0 and e['actual_failure'] is s['failure'] is None
          and e['actual_verified_input_count']==count and e['actual_source_budget_processes']==1
          and len(s['gates'])==gates and all(v['passed'] for v in s['gates'])
          and e['worker_source_sha256']==FILES[role+'w'][2]
          and e['source_budget_source_sha256']==s['source_sha256']==FILES[role+'s'][2]
          and e['input_manifest_sha256']==s['input_manifest_sha256']==FILES[role+'m'][2],role+' entire historical success')
        if role=='SV':
            require(s['run_id']==run and s['run_attempt']=='1'
              and s['workflow_event_commit']==event,'SV nested original execution identity')
        native=[x for x in e['output_hashes'] if x['file'].endswith('.json.gz')]
        require(len(native)==1 and native[0]['bytes']==s['temporary_native_bytes']
          and native[0]['sha256']==s['temporary_native_sha256'],role+' complete original native identity')
    p=docs['V']['actual_scientific_receipt']['cases'][0]
    require(p['complete'] and p['proved'] and p['exact_complex_radial_radius']=='9/1000000'
      and p['exact_complex_delta_square_halfwidth']=='1/100000000' and p['exact_complex_z_square_halfwidth']=='1/9409'
      and p['fixed_intrinsic_parameter']=='eta_0' and p['both_carrier_signs_retained'], 'original entire root parameter product')
    sv=docs['SV']['actual_scientific_receipt'];g=sv['complete_saved_genuine_column_conclusion'];s=sv['scope']
    require(g['entire_saved_arrays_checked'] and g['full_zero_mode_both_genuine_columns_and_both_carriers_retained']
      and g['angular_derivative_orders']==[0,1,2] and g['genuine_amplitude_identity']=='w1V=free_w1+(T*b0,a0)*B(T)'
      and s['same_genuine_w1V_not_free_first_correction'] and s['full_amplitude_means_and_independent_physical_even_mean_retained']
      and s['original_fixed_intrinsic_parameter']=='eta_0' and not s['positive_growing_column_operator_paid'], 'whole true gamma and original positive restriction')
    return p['complete_modulus_upper'],g['complete_b1_value_derivative_upper']

def new(v,g):
    hi=lambda x:endpoints(x)[1]
    N=388;root=Q(29,4);pi=Q(22,7);m1=Q(69,250);V=245;B1=7325
    den=1-Q(B1,N*N)
    eps=(pi*m1*V/(N*root)+Q(7,6)*B1/(N*N))/den
    coef=(pi*m1*V+Q(7,6)*B1/root**2)/den
    elo=sum((Q(1,factorial(k)) for k in range(9)),Q(0))+Q(10,9*factorial(9))
    gamma=3-Q(3,4)+Q(3,14)-Q(1,20)+Q(1,104)-Q(1,640)+Q(25,68)*Q(629,1000)
    return dict(whole_V0=hi(v['V'])<V,whole_Bprime=hi(v['V_T'])/3<B1,
      whole_second=hi(v['V_TT'])<2929766,exponential_upper=elo<Q(68,25),
      inverse_two_power=4*Q(629,1000)**3<1,gamma_integral_lower=gamma>Q(53,20),
      three_power=Q(207,100)**3<9,derivative_Airy_row=4/(Q(207,100)*Q(53,20)**2)<m1,
      cube_root_floor=root**3<N,wronskian_pair_factor=Q(4,3)<Q(7,6)**2,
      true_denominator=den>0,uniform_rank_inverse=eps<Q(7,50),uniform_decaying_rank_inverse=coef<396,
      true_whole_right_factor=(1+Q(7,50))*(1+100/(N*root))<Q(6,5),
      whole_right_difference=396+(1+Q(7,50))*100<511,
      genuine_zero_anchor_slope=Q(2929766,5)+245**2<647000,
      whole_gamma=hi(g[0])<Q('.938'),whole_gamma_first=hi(g[1])<Q('4.249'),
      whole_gamma_second=hi(g[2])<Q('21.575'),
      two_real_Airy_row_condition=pi*(Q(18,25)**2+m1)<Q(5,2),
      matched_correction_left_right_factor=Q(5,2)*Q(6,5)==3)

def main():
    topic=Path(__file__).resolve().parents[1];checks=new(*admit(topic));require(all(checks.values()),str(checks))
    print(json.dumps(dict(proved=True,checks=checks,whole_inputs={k:v[2] for k,v in FILES.items()},
      minimum_physical_frequency=388,uniform_right_matrix_upper='6/5',right_difference_n4over3_upper='511',
      full_root_physical_error_zero_proved=False,arbitrary_Bi_positive_solution_proved=False,
      old_scientific_targets_recomputed=0),sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
