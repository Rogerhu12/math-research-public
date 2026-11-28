"""New JCR rational comparisons from the two original whole real-circle domains."""
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import re

FILES={
 'strict':('notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json',46318,'2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88'),
 'rectangle':('notes/complex_inner_root_first_Airy_forcing_ci/run-43638232415-1/consumers/process.json',43790,'f8ab9fbf35c39df97f7318e3b71d1c1f08dba6a62290a8ab3144fe7f7446a274'),
 'worker':('notes/complex_inner_root_first_Airy_forcing_ci/run-43638232415-1/worker-process.json',2356,'0095009ea377af94c727b8dc0ddc923270c40149f2241186290abbe58d21ab0a'),
 'manifest':('notes/2026-11-14-R133-complex-inner-root-first-Airy-forcing-CI-inputs.json',8303,'4d76f6f1379fde842a9c58ec30943e0af463d1e34e0b5b9dd709c3c0c9791a73'),
 'source':('scripts/fourfold_codazzi_complex_inner_root_first_Airy_forcing.py',28540,'a203227a2286cd0ad7257addf6d5014c9b2c62dc7fb12d42b6c14b8679f175b4'),
 'JWS':('results/R133-supplement-joint-Wiener-contraction-and-small-complete-angular-inverse.md',8197,'52944b39487cb34690c733529b88e45b964b0028d5fd5c487ec4a73c630dfa09'),
 'JI':('results/R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md',11769,'01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1'),
 'H':('results/R133-supplement-exact-complex-root-coefficient-derivatives-for-first-Airy-forcing.md',8821,'c138161b01a1d29dec3ee79b608416fc1c884e0165c5f45ca16aebf6504d0890'),
 'A':('results/R133-supplement-actual-complex-inner-root-first-Airy-forcing.md',10482,'8b5bb31b91242b514a486945a101050aad0668a716dcbde25c68c24fc0930642'),
 'SPNproof':('results/R149-supplement-true-positive-seven-port-graph-around-the-selected-member.md',9590,'83c787877cca06ea22b575da1d50c24a67a054e056abdabe94d7a66232549092'),
 'SPN':('notes/2026-11-28-SPN-complete-saved-consequence.json',3087,'ac82ab9942eb4bbd8a7fa6522fbc4d8b7e4cd414db0e42bfa55bf1c4f8e8a4c2'),
}


def require(ok, msg):
    if not ok:
        raise ValueError(msg)


def admit(topic):
    records={}
    for role,(p,n,h) in FILES.items():
        b=(topic/p).read_bytes()
        require((len(b),sha256(b).hexdigest())==(n,h),'original whole '+role)
        if p.endswith('.json'):
            records[role]=json.loads(b)
    s,r,w=records['strict'],records['rectangle'],records['worker']
    t=s['actual_scientific_receipt']
    raw=(json.dumps(t,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode()
    require(s['run_id']==t['run_id']=='43768006977' and s['run_attempt']==t['run_attempt']=='1'
            and s['complete'] and t['complete'] and t['proved'] and s['actual_returncode']==t['actual_returncode']==0
            and s['actual_failure'] is t['failure'] is None and len(t['gates'])==26 and all(g['passed'] for g in t['gates'])
            and dict(file='consumers/process.json',bytes=len(raw),sha256=sha256(raw).hexdigest()) in s['output_hashes']
            and t['temporary_native_sha256']=='b993132933924df69f6a0a0acee4c673092d1ba59d223bdf204c24c84741d09e',
            'original complete strict embedded process and native identity')
    p=t['mathematical_parameters']
    require(p['exact_complete_radial_interval']==['0',p['exact_strict_cut']]
            and p['exact_strict_cut']=='76285779072683/320000000000000' and p['complete_physical_mean_coordinates']==2
            and p['exact_real_delta_radius']==r['exact_complex_parameter_radius']=='1/100000000'
            and p['fixed_intrinsic_parameter']==r['actual_intrinsic_parameter']=='eta_0'
            and p['exact_root_interval']==r['exact_root_interval']==['1191984371497/5000000000000','2383968743003/10000000000000']
            and p['exact_compact_metric_support']==['1/20','9/50'] and
            [p[k] for k in ('whole_background_A0','whole_background_angle_A0','whole_response_A0','whole_response_angle_A0')]==[7,6,19,83],
            'original root, parameter, both means and joint Wiener units')
    require(r['run_id']==w['run_id']=='43638232415' and r['run_attempt']==w['run_attempt']=='1' and r['complete'] and
            r['mathematical_complete'] and w['complete'] and r['actual_returncode']==w['actual_returncode']==0 and
            r['failure'] is r['mathematical_failure'] is None and r['complete_coefficient_budget'] and r['complete_forcing_cases']==3
            and r['verified_input_files']==22 and len(r['mathematical_gates'])==14 and all(g['passed'] for g in r['mathematical_gates'])
            and r['workflow_event_commit']==w['workflow_commit']=='242092cfc86d1b506b0c81f12b4e329fde5dcbee'
            and r['mathematical_source_sha256']==FILES['source'][2] and r['manifest_sha256']==w['manifest_sha256']==FILES['manifest'][2]
            and r['all65_base_and193_direction_components_retained'] and r['independent_even_mean_retained']
            and (r['native_bytes'],r['native_sha256'])==(51084,'41dc8aace27c9eaa7e10154c1ec0f5f590d945a66f2c1b4d8765ab213cb0063f')
            and r['background_definition_sha256']=='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
            and r['explicit_direction_definition_sha256']=='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04',
            'original root execution, full rectangle, repaired family, native and all three cases')
    sp=records['SPN']
    require(sp['proved'] and len(sp['checks'])==32 and all(sp['checks'].values()) and not sp['actual_complete_nonlinear_family_proved'],
            'complete physical rate used to bound the changed root mean')
    return t,r


def endpoints(rec):
    s=rec['ball']
    if s.startswith('['):
        m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s)
        require(m is not None,'original complete ball')
        z,e=map(Q,m.groups());require(e>=0,'nonnegative radius')
        return z-e,z+e
    return Q(s),Q(s)


def new(t,r):
    tol=Q('1e-7');d=Q('1e-8')
    p=t['mathematical_parameters'];s=t['complete_new_selected_intrinsic_conclusion']
    lo,hi=map(Q,p['exact_root_interval']); left,right=map(Q,r['exact_original_complex_radial_rectangle']['real_interval'])
    pc0,pc1=map(Q,r['exact_original_root_piece_interval']); cut=Q(p['exact_strict_cut'])
    angle=s['complete_radial_0_3_absolute_maxima'];b=Q('.2106');e=Q('1.10865')-Q('1.12')*tol
    S=7+19*d+tol;E=6+83*d+tol;L=2*b*(E*S/4-3*E*E/64)
    z=r['complete_coefficient_budget_numeric'];Br=Q('.210552');Er=Q('1.253');U,V,V1=map(Q,('1.513','4.301','6.730'))
    return dict(
        real_rectangle_is_original=left==lo-Q('1e-5') and right==hi+Q('1e-5') and Q(r['exact_original_complex_radial_rectangle']['imaginary_half_width'])==Q('1e-5'),
        original_piece_covers_all_negative_root_and_sliver=Q('0.18')<pc0<left<cut<lo<hi<right<pc1,
        strict_beta=max(map(abs,endpoints(angle['beta'][0])))<b,
        strict_gamma=max(map(abs,endpoints(angle['gamma'][0])))<Q('1.12'),
        strict_original_eta=endpoints(s['complete_eta_lower'])[0]>Q('1.10865'),
        strict_true_alpha=2*b/e<Q(2,5), strict_joint_product_branch=E/4<S/2,
        strict_perturbed_mean_fraction=Q(2,5)*E*E/256<Q(1,16),
        strict_perturbed_neumann_gap=4*e-L>Q(5,7),
        root_beta=max(map(abs,endpoints(z['beta'])))<Br,
        root_corrected_eta=endpoints(z['eta_lower'])[0]-14*tol>Er,
        root_wiener_u=endpoints(z['U'][0])[1]+tol<U,
        root_wiener_v=endpoints(z['V'][0])[1]+tol<V,
        root_wiener_vphi=endpoints(z['V'][1])[1]+tol<V1,
        root_true_alpha=2*Br/Er<Q('.337'),
        root_perturbed_denominator=1-Q('.337')*U*V1/16>Q('.785'),
        root_angular_operator=2*Br*U*(V+V1/4)<Q('3.815'),
        root_neumann_and_ordinary_inverse=4*Er-Q('3.815')>1/Q('.837'),
        root_left_derivative=(1+Q('3.815')*Q('.837'))/Er<Q('3.35'),
        root_complete_H1=Q('.837')**2+Q('3.35')**2<Q('3.46')**2)


def main():
    checks=new(*admit(Path(__file__).resolve().parents[1]))
    require(all(checks.values()),'every new directed rational comparison')
    print(json.dumps(dict(proved=True,checks=checks,whole_inputs={k:v[2] for k,v in FILES.items()},
        real_full_negative_D_lower='0.785',strict_D_lower='15/16',root_L2_upper='0.837',root_H1_upper='3.46',
        whole_negative_L2_upper='7/5',corrected_full_A3_radius='1e-7',old_scientific_targets_recomputed=0,
        global_physical_inverse_or_matched_core_proved=False),sort_keys=True))


if __name__=='__main__':
    main()
