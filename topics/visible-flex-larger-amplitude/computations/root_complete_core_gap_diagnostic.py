#!/usr/bin/env python3
"""Exact axial support gaps of complete finite warm cores, not whole held gaps.

Reads every coefficient from the original complete geometry reports.  The
identity d=2 sum_{j odd} c_{2j} is the axial quarter-phase support difference
used by R40.  No new surface, RHS, Jacobian, tail or BVP is evaluated.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, sys

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def rat(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),'decimal_display':float(x)}
def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--plan',type=Path,required=True)
    a.add_argument('--baseline-report',type=Path,required=True)
    a.add_argument('--combined-report',type=Path,required=True)
    a.add_argument('--out',type=Path,required=True)
    o=a.parse_args()
    if o.out.exists():raise FileExistsError(o.out)
    plan=json.loads(o.plan.read_text()); records=[]; gaps={}; sources={}
    cases=[(x['name'],Path(x['report'])) for x in plan['candidates']]+[('combined',o.combined_report)]
    if cases[0] != ('baseline',o.baseline_report):raise ValueError('Explicit baseline differs from saved plan')
    # The original enriched plan contains baseline and ten perturbations; never
    # drop or silently duplicate a direction if its schema is later changed.
    if len(cases)!=12 or len(set(x[0] for x in cases))!=len(cases):raise ValueError('Require baseline, ten directions and combined')
    grid_sha=None
    for name,path in cases:
        data=json.loads(path.read_text());g=data['geometry_fields']
        if not data.get('finished') or not data.get('finite_domain_passed') or data.get('nonlinear_solution') or data.get('true_new_H_tail_evaluated') or data.get('worker_start_attempts')!=0:raise ValueError('Require a completed unaccepted warm diagnostic')
        if grid_sha is None:grid_sha=g['grid_sha256']
        if g['grid_sha256']!=grid_sha or len(g['actual_core'])!=24:raise ValueError('Complete common-grid core identity differs')
        coeff=[F.from_float(x) for x in g['actual_core']]
        d=2*sum(coeff[::2],F(0));gaps[name]=d
        radius=F.from_float(g['twice_radius_max_sample'])
        sources[str(path)]=sha(path)
        records.append({'case':name,'complete_core_exact':[rat(x) for x in coeff],'axial_core_gap_exact':rat(d),'future_full_D_budget_5d_exact':rat(5*d),'ratio_to_finite_sample_origin_sphere_diagnostic':rat(d/radius),'finite_radius_sample':float(radius),'primary_amplitude':float(coeff[0]),'whole_held_or_diameter_certified':False})
    derivatives=[]
    for row in plan['directions']:
        name=row['name'];step=F.from_float(row['step']);plus,minus=gaps[name+'-plus'],gaps[name+'-minus']
        derivatives.append({'name':name,'original_step_exact':rat(step),'centered_gap_sensitivity_exact':rat((plus-minus)/(2*step)),'one_original_step_gap_change_exact':rat((plus-minus)/2),'second_difference_exact':rat(plus+minus-2*gaps['baseline'])})
    sources[str(o.plan)]=sha(o.plan);sources[str(Path(__file__))]=sha(__file__)
    out={'scope':__doc__,'completed':True,'source_sha256':sources,'common_grid_sha256':grid_sha,'records':records,'gap_sensitivities':derivatives,'actual_combined_gap_change_exact':rat(gaps['combined']-gaps['baseline']),'old_LP_objective':'maximize first coefficient c2 in a bounded local step, not the exact complete d or its ratio','limitations':['The displayed d is the exact finite planar support identity for the saved binary64 coefficients.','No new core is relabeled as a converged prefix or closed surface.','2r is a sample of an origin sphere expression on an open warm prefix, not the full continuous closed diameter D.','No non-occlusion, fixed-H, actual held, Euclidean separation, reach, exact isometry or refinement gate is established.'],'physical_RHS_evaluations':0,'Jacobian_evaluations':0,'Node_workers':0,'BVP_solves':0}
    o.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'file':str(o.out),'baseline_d':float(gaps['baseline']),'combined_d':float(gaps['combined']),'change':float(gaps['combined']-gaps['baseline']),'all_24_coefficients':True}),flush=True)
if __name__=='__main__':main()
