#!/usr/bin/env python3
"""Independently consume the complete saved q106 angular-mean certificate.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Exact Fraction arithmetic verifies every physical interval and saved analytic
premise. A positive rational Taylor polynomial, rather than the producer's
Arb exponential, supplies the exponential lower bound in the alias formula.
The saved integrand caps are rounded outward again before all single-anchor
payments are combined. Original floating evaluation remains a separate cost.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(x):return F(int(x[0]))*F(2)**int(x[1])
def exact(x):
    x=F(x);return dict(numerator=str(x.numerator),denominator=str(x.denominator))
def up(x,bits=160):
    x=F(x)
    if x<0:raise ArithmeticError('Nonnegative bound required')
    if not x:return ['0',0]
    e=x.numerator.bit_length()-x.denominator.bit_length()-bits
    scaled=x/F(2)**e
    m=(scaled.numerator+scaled.denominator-1)//scaled.denominator
    out=[str(m),e]
    if dy(out)<x:raise ArithmeticError('Exact upward dyadic rounding failed')
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('certificate','resource','producer','domain','primary','prior','prior-resource','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh independent saved mean consumer required')
    data,owned,domain,primary,prior,prior_owned=map(read,
        (a.certificate,a.resource,a.domain,a.primary,a.prior,a.prior_resource))
    gates={}
    def check(name,ok):
        gates[name]=gates.get(name,0)+1
        if not ok:raise ArithmeticError(name)
    check('actual_producer_owned_exit0',owned['exitcode']==0 and owned['wait4_observed'] and owned['automatic_restarts']==0)
    check('actual_boundary_predecessor_owned_exit0',prior_owned['exitcode']==0 and prior_owned['wait4_observed'])
    check('actual_producer_source',data['source_sha256']==sha(a.producer))
    check('same_actual_primary_and_original_domain',data['primary_sha256']==sha(a.primary)==domain['primary_sha256'] and data['input_sha256'].get(str(a.domain))==sha(a.domain))
    check('same_completed_boundary_input',data['input_sha256'].get(str(a.prior))==sha(a.prior) and data['input_sha256'].get(str(a.prior_resource))==sha(a.prior_resource))
    check('actual_complete_positive_cover',data['all_complex_domain_gates'] and data['complete_domain_cover'] and not data['failed_atoms'] and data['original_parents']==3326)
    check('same_complete_original_mean',data['exact_mean_angular']==1360 and primary['modes']==28)
    check('same_actual_comparison_definitions',all(data[k]==domain[k]==prior[k] for k in ('state_comparison_definition_sha256','background_comparison_definition_sha256')))
    check('unpaid_costs_remain_explicit',not data['original_IEEE_libm_and_node_evaluation_or_coordinate_alignment_paid'] and not data['radial_Gauss6_error_paid'] and not data['original_g_PDE_reach_or_closed_surface_certified'])
    parents=domain['rows'];rows=data['rows'];mesh=list(map(F.from_float,map(float,primary['mesh'])))
    check('actual_original_parent_count',len(parents)==len(prior['rows'])==3326 and len(rows)==data['complete_atoms'])
    exponentials={};payments=[];cursor=F(0);parent_cover={i:[] for i in range(len(parents))}
    height=F(0);maxima=[F(0),F(0)];old_height=F(0);old_maxima=[F(0),F(0)];retained=0;new=0
    for index,row in enumerate(rows):
        parent_id=row['parent_atom'];parent=parents[parent_id];before=prior['rows'][parent_id]
        left,right=map(F,row['s_interval']);pl,pr=map(F,parent['s_interval']);j=row['original_interval']
        check('exact_whole_radial_cover',row['atom']==index and left==cursor and pl<=left<right<=pr and mesh[j]<=left<right<=mesh[j+1])
        check('same_original_state_and_background_piece',j==parent['original_interval'] and row['background_piece']==parent['background_piece'])
        check('complete_actual_complex_domain_premise',row['positive_complex_domain'] and row['whole_physical_interval_and_complex_angular_strip'] and row['whole_repair_homotopy'] and row['actual_original_quintics_restricted_exactly'])
        check('strict_saved_positive_divisor_halfplanes',min(F.from_float(float(row[k])) for k in ('real_part_W_lower','real_part_D_lower','real_part_chart_rho_lower','actual_radius_lower'))>0)
        width=F(row['strip_width']);check('actual_positive_angular_strip',0<width<=F(1,16) and row['angular_boxes']>=512)
        if row['retained_prior_successful_atom']:
            check('successful_parent_retained_exactly',before['positive_complex_domain'] and all(row[k]==v for k,v in before.items() if k!='atom') and row['subdivision_path']=='')
            retained+=1
        else:
            check('new_rows_only_refine_unpaid_original_parent',not before['positive_complex_domain'] and row['subdivision_path'] and all(ch in '01' for ch in row['subdivision_path']))
            lo,hi=pl,pr
            for ch in row['subdivision_path']:
                mid=(lo+hi)/2
                if ch=='0':hi=mid
                else:lo=mid
            check('exact_bisection_path_matches',left==lo and right==hi)
            check('whole_periodic_cylinder_argument_explicit',row['evaluated_upper_boundary_with_exact_fixed_imaginary_coordinate'] and row['lower_boundary_by_real_coefficient_conjugation'] and row['whole_strip_by_periodic_harmonic_minimum_and_maximum_principles'])
            new+=1
        key=str(width)
        if key not in exponentials:
            x=1360*width;term=F(1);lower=F(1)
            for k in range(1,257):
                term*=x/k;lower+=term
            check('positive_Taylor_exponential_lower',x>0 and lower>1 and term>0)
            exponentials[key]=dict(argument=exact(x),degree=256,lower=exact(lower))
        rec=exponentials[key]['lower'];den=F(int(rec['numerator']),int(rec['denominator']))-1
        caps=[dy(row[k]) for k in ('complex_mean_integrand_Vz_absolute_upper','complex_mean_derivative_Vsz_absolute_upper')]
        check('positive_full_holomorphic_integrand_caps',min(caps)>0)
        old=list(map(dy,row['complete_periodic_mean_Hs_Hss_alias_upper']))
        check('positive_saved_alias_pair',len(old)==2 and min(old)>0)
        # The producer's internal Arb cap and its stored upper endpoint need
        # not be identical. This independent consumer uses the stored upper
        # endpoint itself and safely intersects neither at sub-ulp level.
        paid=[up(max(old[k],2*caps[k]/den)) for k in (0,1)]
        fees=list(map(dy,paid))
        check('independent_complete_alias_costs_dominate_both_forms',all(fees[k]>=old[k] and fees[k]*den>=2*caps[k] for k in (0,1)))
        height+=(right-left)*fees[0];maxima=[max(x,y) for x,y in zip(maxima,fees)]
        old_height+=(right-left)*old[0];old_maxima=[max(x,y) for x,y in zip(old_maxima,old)]
        payments.append(dict(atom=index,parent_atom=parent_id,s_interval=row['s_interval'],strip_width=key,
            complete_mean_Hs_Hss_alias_upper=paid,same_zero_anchor=True))
        parent_cover[parent_id].append([left,right]);cursor=right
    for index,cover in parent_cover.items():
        pl,pr=map(F,parents[index]['s_interval'])
        check('every_original_parent_fully_partitioned',bool(cover) and cover[0][0]==pl and cover[-1][1]==pr and all(x[1]==y[0] for x,y in zip(cover,cover[1:])))
    check('same_complete_meridian',cursor==mesh[-1] and cursor==F.from_float(float(primary['meridian_length'])))
    check('exact_retained_and_new_counts',retained==data['retained_prior_successful_atoms'] and retained+new==len(rows))
    saved=list(map(dy,data['complete_mean_alias_H_Hs_Hss_upper']))
    check('producer_global_saved_aggregation_is_outward',all(x>=y for x,y in zip(saved,[old_height,*old_maxima])))
    total=[up(x) for x in (height,*maxima)]
    check('new_independent_global_aggregation_is_outward',all(dy(x)>=y for x,y in zip(total,[height,*maxima])))
    out=dict(schema='actual-q106-independent-complete-complex-mean-consumer-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gate_count=sum(gates.values()),gate_multiplicities=gates,
        source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (a.certificate,a.resource,a.producer,a.domain,a.primary,a.prior,a.prior_resource)},
        analytic_enclosure_premise_source_sha256=data['source_sha256'],actual_original_physical_parents=len(parents),
        complete_radial_atoms=len(rows),retained_prior_successes=retained,new_radial_children=new,exact_mean_angular=1360,
        independent_positive_Taylor_exponential_lowers=exponentials,rows=payments,
        complete_mean_alias_H_Hs_Hss_upper=total,full_mean_alias_H_Hs_Hss_display=[float(dy(x)) for x in total],
        aggregation='One exact zero anchor: integral of positive Hs alias along the complete original radial domain; Hs and Hss by maximum of their whole-interval bounds.',
        saved_caps_used_as_exact_upper_dyadics=True,producer_sub_ulp_cap_rounding_not_assumed_equal=True,
        original_IEEE_libm_and_node_evaluation_or_coordinate_alignment_paid=False,radial_Gauss6_error_paid=False,
        new_ODE_Node_Newton_or_geometry_calls=0,original_g_PDE_reach_or_closed_surface_certified=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as z:
            z.write((json.dumps(out,separators=(',',':'))+'\n').encode())
    print(json.dumps(dict(all_gates=True,gates=out['gate_count'],atoms=len(rows),
        H_Hs_Hss=out['full_mean_alias_H_Hs_Hss_display'],path=str(a.out),sha256=sha(a.out))),flush=True)

if __name__=='__main__':main()
