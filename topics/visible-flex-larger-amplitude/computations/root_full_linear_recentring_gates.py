#!/usr/bin/env python3
"""Exact actual full-L_R recentering of the same R105/R100 true low46 solution.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as Q

SOURCE_SHA='58ae9b5d9332ce09530d2380b00348eb50efa3693a27294ecf185d9ea6f175db'
BALL_SHA='cbf948ece6dcbad4f7a11c85d7ad721006fd7cf295da9baea87cf4f9de80c0a8'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def n(x):
    if isinstance(x,dict):
        if 'numerator' in x:return Q(int(x['numerator']),int(x['denominator']))
        if 'upper' in x:return n(x['upper'])
        return Q(int(x['mantissa']))*Q(2)**int(x['binary_exponent'])
    return Q(x[0])*Q(2)**x[1]
def record(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator),'display_only':float(x)}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('source-summary','source-resource','old-ball','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();gates={}
    def gate(k,v):
        gates[k]=bool(v)
        if not v:raise ArithmeticError(k)
    gate('same_actual_all_linear_source',digest(a.source_summary)==SOURCE_SHA)
    gate('same_existing_R105_true_solution',digest(a.old_ball)==BALL_SHA)
    d=json.loads(a.source_summary.read_text());b=json.loads(a.old_ball.read_text());r=json.loads(a.source_resource.read_text())
    gate('actual_owned_source_formal_zero',r['exitcode']==0 and r['termination_signal'] is None)
    gate('all_source_gates',d['all_gates'] and all(d['gates'].values()))
    gate('all_existing_solution_gates',b['all_gates'] and all(b['gates'].values()))
    gate('exact_all46_modes',d['modes']==list(range(2,93,2)))
    gate('complete_original_materials',sum(g['original_panels'] for g in d['groups'])==10793 and len(d['groups'])==18)
    gate('complete_actual_geometry',sum(g['subpanels'] for g in d['groups'])==d['whole_geometry_subpanels']==10878)
    centre=n(d['joint_true_linear_norm_upper']);res=n(d['joint_strong_PK_green_upper'])
    gate('joint_centre_covers_separate_radial_suprema',centre>=sum(n(v) for row in d['true_linear_norms'].values() for v in row.values()))
    gate('joint_green_covers_separate_radial_suprema',res>=sum(n(v) for row in d['mode_green_norms'].values() for v in row.values()))
    head=n(b['complete_head_field']);gamma=n(b['full_ball_contraction']);rho=Q(3,2*10**13)
    gate('same_complete_head_far_and_full_mean',b['head_far_paid_once_in_complete_mass'] and head>0)
    gate('same_absolute9_complete_contraction',0<gamma<Q(1,400))
    gate('all_linear_centre_inside_absolute9',centre<8)
    gate('whole_recentered_ball_inside_absolute9',centre+rho<8)
    image=res+head+gamma*rho;posterior=(res+head)/(1-gamma)
    gate('strict_recentered_selfmap',image<rho)
    gate('posterior_is_inside_recentered_ball',posterior<rho)
    gate('actual_posterior_below_1p31e_minus13',posterior<Q(131,10**15))
    result={'schema':'true-all-linear-recentring-v1','scope':'Same existing R105/R100 low46 solution, now centred at the full true L_R on the unchanged full unit parameter domain. No cut or all-frequency PDE closure asserted.','all_gates':all(gates.values()),'gates':gates,'inputs':{str(a.source_summary):SOURCE_SHA,str(a.old_ball):BALL_SHA,str(a.source_resource):digest(a.source_resource)},'source_sha256':digest(Path(__file__)),'centre_norm_upper':record(centre),'complete_fixed_centre_green':record(res),'same_complete_head_field':record(head),'same_absolute9_contraction':record(gamma),'chosen_radius':record(rho),'complete_image':record(image),'strict_selfmap_slack':record(rho-image),'a_posteriori_radius':record(posterior),'all46_cut_claimed':False,'all_frequency_PDE_claimed':False}
    if a.out.exists():raise FileExistsError('Fresh exact gate output required')
    a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_gates':result['all_gates'],'gate_count':len(gates),'posterior_display':float(posterior),'sha256':digest(a.out)}))
if __name__=='__main__':main()
