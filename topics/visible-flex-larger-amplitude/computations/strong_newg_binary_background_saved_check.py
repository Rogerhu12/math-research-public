#!/usr/bin/env python3
"""Independent rational checks of the saved continuous background repair.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No provider, quadrature, transcendental or surface evaluator is rerun.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import resource
import time


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(z):return F(int(z[0]))*F(2)**int(z[1])
def rat(z):return F(int(z['numerator']),int(z['denominator']))
def ev(p,t,order=0):
    return sum((p[k]*F(factorial(k),factorial(k-order))*t**(k-order)
                for k in range(order,len(p))),F(0))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('certificate','resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh saved comparison audit required')
    d=json.loads(a.certificate.read_text());res=json.loads(a.resource.read_text());checks=[]
    def check(name,ok):
        if not ok:raise ArithmeticError(name)
        checks.append(name)
    check('observed_original_complete_certificate',d['all_gates'] and all(d['gates'].values()) and
          res['exitcode']==0 and res['wait4_observed'] and res['termination_signal'] is None)
    bases=[[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,1,-2,1]]
    bounds=[[F(1),F(2,5),F(1,10)],[F(5),F(2),F(1,2)],[F(20),F(12),F(4)]]
    for j,b in enumerate(bases):
        for order in range(3):
            check('left_jets_zero',ev(b,F(0),order)==0)
            check('right_endpoint_Hermite_identity',ev(b,F(1),order)==([1,1,2][j] if order==j else 0))
            degree=5-order
            coeff=[F(b[k+order])*F(factorial(k+order),factorial(k)) for k in range(degree+1)]
            bernstein=[sum((coeff[k]*F(comb(i,k),comb(degree,k)) for k in range(i+1)),F(0))
                       for i in range(degree+1)]
            check('exact_Bernstein_basis_uniform_bound',max(map(abs,bernstein))<=bounds[order][j])
    summary=[]
    for profile in d['profiles']:
        definition=profile['comparison_definition']
        check('frozen_explicit_comparison_definition',hashlib.sha256(json.dumps(definition,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==profile['comparison_definition_sha256'])
        rows=profile['piece_rows'];previous=F(0);maxima=[F(0)]*3
        check('complete_actual_profile_source_identity',sha(profile['accepted_primary'])==profile['accepted_primary_sha256'] and
              profile['original_floating_candidate_or_target_g_modified'] is False)
        for i,row in enumerate(rows):
            left,right=map(rat,row['physical_interval']);h=right-left
            check('continuous_interval_cover',left==previous and h>0);previous=right
            E=[max(abs(exact(z[0])),abs(exact(z[1]))) for z in row['next_left_minus_current_right']]
            coefficients=[E[0],h*E[1],h*h*E[2]/2]
            for order in range(3):
                needed=sum((bounds[order][j]*coefficients[j] for j in range(3)),F(0))/h**order
                saved=exact(row['quintic_repair_uniform_C0_C1_C2_upper'][order])
                check('full_saved_repair_bound',saved>=needed>=0)
                maxima[order]=max(maxima[order],saved)
            if i==len(rows)-1:
                check('last_piece_unchanged',E==[0,0,0])
        global_caps=list(map(exact,profile['global_explicit_repair_C0_C1_C2_upper']))
        check('global_repair_is_complete_piece_max',all(x>=y for x,y in zip(global_caps,maxima)))
        lo=min(exact(row['complete_radius_interval'][0]) for row in rows)-global_caps[0]
        hi=max(exact(row['complete_radius_interval'][1]) for row in rows)+global_caps[0]
        v=max(exact(row['continuous_first_absolute_upper']) for row in rows)+global_caps[1]
        acc=max(exact(row['continuous_second_absolute_upper']) for row in rows)+global_caps[2]
        check('saved_repaired_positive_radius',0<exact(profile['new_C2_comparison_radius_bounds'][0])<=lo)
        check('saved_repaired_radius_upper',exact(profile['new_C2_comparison_radius_bounds'][1])>=hi)
        check('saved_strictly_subunit_speed',v<=exact(profile['new_C2_comparison_speed_absolute_upper'])<1)
        check('saved_complete_acceleration',acc<=exact(profile['new_C2_comparison_acceleration_absolute_upper']))
        summary.append({'accepted_sha256':profile['accepted_primary_sha256'],'pieces':len(rows),
            'repair_upper_displays':list(map(float,global_caps)),
            'comparison_definition_sha256':profile['comparison_definition_sha256']})
    out={'schema':'binary-background-C2-saved-exact-Fraction-consumption-v1','scope':__doc__,
         'all_gates':True,'gate_count':len(checks),'checks':checks,'source_sha256':sha(__file__),
         'input_sha256':{str(p):sha(p) for p in (a.certificate,a.resource)},'profiles':summary,
         'new_original_target_g_or_surface_claim':False,'no_background_or_quadrature_recomputation':True,
         'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gates':len(checks),'path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
