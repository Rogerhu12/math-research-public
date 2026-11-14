#!/usr/bin/env python3
"""Assemble disjoint actually completed initial-row products of R151.

The v2 prefix is an explicitly identified observed stdout receipt, not a
fabricated final solver report. The v3 prefix is its source-written completed
row checkpoint. The v4 suffix must be its naturally completed full requested
row range, with no unresolved boxes. Only unchanged physical input SHAs and
the exact partition [0,6)+[6,9)+[9,32) are combined.
"""
import argparse,json,time
from pathlib import Path
from collections import Counter
from fd2d_k0_ruling_metric_convolution import digest,load,from_bounds
from flint import arb,ctx


def require(condition,message):
    if not condition:raise ValueError(message)


def tree_count(calls,methods,products):
    leaves=sum(methods.values())
    require(calls==2*leaves-products,'Completed binary-tree node count mismatch')
    return leaves


def main():
    root=Path(__file__).resolve().parent.parent;ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v2',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-all-pair-v2-completed-rows-receipt.json')
    ap.add_argument('--v3',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-all-pair-v3-completed-rows-checkpoint.json')
    ap.add_argument('--v3-stop',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-all-pair-v3-owner-stop-receipt.json')
    ap.add_argument('--v4',type=Path,default=root/'notes/2026-11-12-fd2d-k0-ruling-all-pair-normal-balls-04.json')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();ctx.prec=160
    v2,v3,stop,v4=(load(p) for p in (args.v2,args.v3,args.v3_stop,args.v4))
    sources={'v2':'fd2d_k0_ruling_all_pair_normal_balls_taylor.py','v3':'fd2d_k0_ruling_all_pair_normal_balls_extended.py','v4':'fd2d_k0_ruling_all_pair_normal_balls_frame.py'}
    require(v2['source_sha256']==digest(root/'scripts'/sources['v2']),'v2 source binding mismatch')
    require(v3['binding']['source_sha256']==digest(root/'scripts'/sources['v3']),'v3 source binding mismatch')
    require(v4['source_sha256']==digest(root/'scripts'/sources['v4']),'v4 source binding mismatch')
    require(v2['exit_code']==130 and v2['owner_requested_stop'] and not v2['whole_run_complete'],'v2 owner-stop status was altered')
    require(stop['exit_code']==130 and stop['owner_requested_stop'] and stop['closed_checkpoint_sha256']==digest(args.v3),'v3 owner-stop checkpoint binding mismatch')
    require(v2['completed_initial_rows']==[0,6] and v2['initial_angle_boxes']==32,'Unexpected v2 row domain')
    require([r['row'] for r in v2['completed_row_records']]==list(range(6)),'v2 completed rows missing')
    require(all(r['unresolved']==0 for r in v2['completed_row_records']) and v2['completed_unresolved']==0,'v2 unresolved complete product')
    require(v3['binding']['initial_angles']==32 and v3['binding']['first_row']==6 and v3['next_row']==9,'Unexpected v3 row domain')
    require([r['row'] for r in v3['rows']]==[6,7,8] and not v3['unresolved'],'v3 incomplete/unresolved rows')
    require(v4['initial_angle_boxes']==32 and v4['initial_rows']==[9,32] and v4['passed'] and not v4['unresolved'],'v4 suffix not completed')
    require([r['row'] for r in v4['rows']]==list(range(9,32)),'v4 completed row list mismatch')
    require(v4['normal_owner_explicit_even_for_identical_angle_cache'] and not v4['changed_delta_target'],'v4 object/owner definition mismatch')
    physical_keys=('inlet_sha256','candidate_sha256','moments_sha256','means_sha256')
    for key in physical_keys:require(v2[key]==v3['binding'][key]==v4[key],'Physical definition mismatch: '+key)
    # 17/125 is not dyadic. The stored Arb endpoints must include this
    # rational; demanding radius zero would wrongly reject its enclosure.
    rho=from_bounds(v4['radius']);require(rho.contains(arb(17)/125),'Normal radius mismatch')
    p2=sum(32-i for i in range(6));p3=sum(32-i for i in range(6,9));p4=sum(32-i for i in range(9,32))
    require(v2['completed_initial_products']==p2 and v3['completed_initial_products']==p3 and v4['completed_initial_products']==p4,'Initial product counts mismatch')
    m2=v2['completed_leaf_methods'];m3=v3['methods'];m4=v4['methods']
    l2=tree_count(v2['completed_recursive_calls'],m2,p2);l3=tree_count(v3['recursive_box_calls'],m3,p3);l4=tree_count(v4['recursive_box_calls'],m4,p4)
    for row in v3['rows']+v4['rows']:tree_count(row['calls'],row['leaves'],32-row['row'])
    total=Counter(m2);total.update(m3);total.update(m4)
    require(p2+p3+p4==32*33//2,'The complete angular product triangle is not covered')
    # Uniform decimal minima from an interrupted run are deliberately not
    # reconstructed. Positivity was the actual acceptance branch for each
    # completed far leaf, which is the statement needed for the theorem.
    report=dict(schema='fd2d-R151-complete-actual-coast-normal-ball-coverage-v1',actual_execution=True,
        source_sha256=digest(__file__),input_sha256={k:digest(getattr(args,k)) for k in ('v2','v3','v3_stop','v4')},
        verifier_source_sha256={k:digest(root/'scripts'/v) for k,v in sources.items()},
        physical_definition_sha256={k:v4[k] for k in physical_keys},
        exact_row_partition=[[0,6],[6,9],[9,32]],initial_angle_boxes=32,completed_initial_products=p2+p3+p4,
        segment_products=[p2,p3,p4],segment_leaves=[l2,l3,l4],accepted_leaf_methods=dict(total),accepted_leaves=l2+l3+l4,
        recursive_box_calls=v2['completed_recursive_calls']+v3['recursive_box_calls']+v4['recursive_box_calls'],
        unresolved_products=0,complete_original_coast_product_covered=True,
        radius_rational=[17,125],both_endpoint_both_sign_normal_balls=True,
        original_parameter_annulus_embedded=True,its_normal_tube_is_injective_for_absolute_offset_less_than_radius=True,
        actual_F_changed_between_segments=False,nonzero_delta_target_included=False,
        boundary_normal_cone_set_reach_claimed=False,whole_closed_surface_reach_claimed=False,
        v2_uniform_far_numeric_margin_and_leaf_chain_not_reconstructed=True,
        v3_leaf_hash_chain_sha256=v3['leaf_hash_chain_sha256'],v4_leaf_hash_chain_sha256=v4['leaf_hash_chain_sha256'],
        v4_minimum_strict_far_Phi_lower=v4['minimum_strict_far_Phi_lower'],
        mathematical_scope='Actual original delta=0 coast only. Strict complete normal balls and self normal-tube injectivity; cross-patch normal balls remain separate.',
        passed=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),passed=True,initial_products=p2+p3+p4,accepted_leaves=l2+l3+l4,seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
