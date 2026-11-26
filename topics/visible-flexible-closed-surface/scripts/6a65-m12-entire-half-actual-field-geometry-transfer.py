#!/usr/bin/env python3
"""Transfer the R21 all-phase geometry to one saved whole-half M12 field.

Consumes continuous source C_X and the actual R226 six-jet field budget,
with exact file identities. A failed conservative inequality is reported
as unresolved; it is never relabelled as a mathematical nonexistence claim.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path

DATA_SHA='359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
META_SHA='253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'
BRIDGE_SHA='1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
R226_SHA='81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def u(p):return Q(p['upper_exact'])
def show(q,kind='upper'):
    return {kind+'_exact':str(q),'display':float(q)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('source-bounds','correction-bounds','field','grid','result','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh actual-field transfer report required')
    began=time.monotonic()
    source=json.loads(args.source_bounds.read_text());change=json.loads(args.correction_bounds.read_text())
    result=json.loads(args.result.read_text());grid=json.loads(args.grid.read_text())
    for record in (source,change):
        for key,expected in (('data_sha256',DATA_SHA),('common_meta_sha256',META_SHA),
                             ('bridge_sha256',BRIDGE_SHA),('tail_manifest_sha256',MANIFEST_SHA)):
            if record.get(key)!=expected:raise ValueError('Changed original source identity '+key)
    if change['script_sha256']!=R226_SHA:raise ValueError('Unreviewed continuous field-bound implementation')
    if change['reference_only']:raise ValueError('Actual whole-half solver field is required')
    if not source['continuous_all_spans_and_all_angles'] or not source['exact_common_cut_change_included']:
        raise ValueError('Incomplete original source C_X')
    if not change['continuous_all_knots_and_all_angles'] or not change['central_reference_change_included']:
        raise ValueError('Incomplete actual change budget')
    if not all(change['exact_zero_endpoint_jets']):raise ValueError('Central/cuff two-jets are not fixed')
    field_sha,grid_sha=sha(args.field),sha(args.grid)
    for record in (change,result):
        if record['field_sha256']!=field_sha or record['grid_sha256']!=grid_sha:
            raise ValueError('Actual saved field identity mismatch')
    if not result.get('original_exact_metric_unchanged') or not result.get('true_flat_cuff_included'):
        raise ValueError('This transfer requires the original complete half through the true cuff')
    if source['tail_cache_sha256']!=result['query_cache_sha256'] or source['tail_report_sha256']!=result['query_report_sha256']:
        raise ValueError('Source C_X and actual solver use different exact tail endpoints')
    eta=u(change['combined_change_from_original_R21_map_jets']['W'])
    p=Q(change['target_orthonormal_differential_l1_upper'])
    cw=Q(change['target_scaled_coordinate_second_jet_l1_upper'])
    cx=u(source['entire_half_original_C_X'])
    d=Q(257212,10**13);K0=Q(4763997235009095,562949953421312)
    R=Q(2131902881202937,1125899906842624)
    metric=d+2*(1+d)*p+p*p;normal=(3*p+p*p)/(1-d)
    support=Q(737,1000)-Q(19,10)*normal-eta;diameter=2*(R+eta)
    moment_loss=2400*eta*(1+9*eta)**2
    basic={'same_original_source_and_actual_field':True,'exact_C2_central_and_true_cuff':True,
           'normal_change_bound_hypothesis':2*(1+d)<Q(9,4),
           'homotopy_metric_immersion':metric<1,'original_tube_covers_displacement':eta<1/K0,
           'swept_tube_inside_radius_2':R+eta<2,
           'activity_real_third_moment_positive':moment_loss<Q(44016,10**5)}
    quantities={'displacement':show(eta),'target_differential':show(p),'actual_change_scaled_second_jets':show(cw),
                'original_source_scaled_second_jets':show(cx),'global_metric_triangle':show(metric),
                'normal_change':show(normal),'support':show(support,'lower'),
                'diameter':show(diameter),'activity_third_moment_loss':show(moment_loss)}
    thresholds={'metric_below_1e_6':metric<Q(1,10**6)}
    if metric<1:
        K=(K0*(1+d)+normal*cx+cw)/(1-metric)
        reach=1/(K*diameter);held=(Q(19989114,10**8)-2*eta)/diameter
        cap=Q(35426,10**4)/diameter
        basic.update({'positive_support_exceeds_inverse_curvature':support>1/K,
                      'new_normal_tube_contains_fixed_marker_height':K<2000})
        quantities.update({'actual_principal_curvature':show(K),'reach_over_diameter':show(reach,'lower'),
                           'held_over_diameter':show(held,'lower'),'fixed_cap_diameter_ratio':show(cap,'lower')})
        thresholds.update({'reach_ratio_above_0_03':reach>Q(3,100),'reach_ratio_above_0_0312':reach>Q(312,10**4),
                           'held_ratio_above_0_05':held>Q(5,100),'held_ratio_above_0_05278':held>Q(5278,10**5),
                           'fixed_cap_diameter_above_0_93':cap>Q(93,100)})
    else:
        basic['positive_support_exceeds_inverse_curvature']=False
        basic['new_normal_tube_contains_fixed_marker_height']=False
    proved=all(basic.values())
    report={'schema':'6a65-actual-M12-whole-half-continuous-geometry-transfer-v1',
            'script_sha256':sha(__file__),'source_bounds_sha256':sha(args.source_bounds),
            'correction_bounds_sha256':sha(args.correction_bounds),'result_sha256':sha(args.result),
            'field_sha256':field_sha,'grid_sha256':grid_sha,'data_sha256':DATA_SHA,
            'scope':'Original R21 exact common-cut map plus the R226 deterministic central correction plus this actual saved entire-half Cartesian field.',
            'continuous_all_space_and_all_phase_times':proved,
            'homotopy_embedded_and_reach_transfer_proved':proved,'checks':basic,
            'optional_numeric_thresholds':thresholds,'rational_quantities':quantities,
            'all_phase_argument':'Same spatial rotation/material-angle action, original rotational g, complete fixed caps and zero endpoint two-jets.',
            'noncongruence_argument':'D3 and reflection symmetry plus positive actual A3; fixed marker B3>0; R16 full E(3) tensor invariant.',
            'inherited_theorems':['R10 positive support global normal tube','R16 fixed cap third moment noncongruence','R21 original complete M12','R25 original enclosing radius','R223 common chart','R226 actual field continuous six jets'],
            'new_degree5_exact_isometry_claim':False,'README_completion_claim':False,
            'failed_bound_means':'Only this conservative transfer remains unresolved; it is not nonexistence.',
            'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))

if __name__=='__main__':main()

