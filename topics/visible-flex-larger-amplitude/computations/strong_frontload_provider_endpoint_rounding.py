#!/usr/bin/env python3
"""Pay complete stored provider endpoint arithmetic against exact Gauss sums.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This consumes all twelve actual binary segment records of the completed
unsolved warm. All original quadrature operands are treated exactly and
sin/cos/sqrt are enclosed by Arb. Differences from the stored dr/dh and
height accumulators pay their actual endpoint evaluation/assembly errors.
They do not assert a uniform libm error or derivatives of a rounded function.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
BASE='strong_newg_binary_background_C2_comparison.py'
BASE_SHA='483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08'
BRIDGE='strong_newg_gauss64_piecewise_C2_bridge.py'
BRIDGE_SHA='a830cdd1da8c4dc187b0ca4e27c0c67d4834c92b8539677f6ef32fbb93e60ea6'
TABLE_SHA='0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def q(z):return F(z['numerator'])/F(z['denominator'])
def binary(z):return F.from_float(float(z))
def aq(z):
    z=F(z);return arb(z.numerator)/z.denominator
def dy(z):return F(int(z[0]))*F(2)**int(z[1])
def upper(z):
    m,e=arb(z).upper().man_exp();return [str(m),int(e)]
def lower(z):
    m,e=arb(z).lower().man_exp();return [str(m),int(e)]
def box(z):return [lower(z),upper(z)]
def bernstein(c,u):
    c=list(c)
    for n in range(len(c)-1,0,-1):c=[(1-u)*c[j]+u*c[j+1] for j in range(n)]
    return c[0]
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('background','background-resource','first-piece','table','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists():raise FileExistsError(a.out)
    bg,owned,first,table=map(read,(a.background,a.background_resource,a.first_piece,a.table))
    gates={}
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates[name]=True
    check('completed_matching_warm_background',bg['all_gates'] and bg['input_kind']=='completed-unsolved-warm'
        and not bg['accepted_new_solution'] and len(bg['profiles'])==1 and owned['exitcode']==0
        and owned['wait4_observed'] and owned['termination_signal'] is None)
    profile=bg['profiles'][0]
    check('same_complete_first_piece',first['all_gates'] and first['actual_profile']==profile['frozen_profile']
        and first['input_kind']=='completed-unsolved-warm'
        and sha(a.first_piece) in bg['input_identities'].values())
    check('frozen_original_helpers',sha(HERE/BASE)==BASE_SHA and sha(HERE/BRIDGE)==BRIDGE_SHA)
    check('complete_certified_actual_table',sha(a.table)==TABLE_SHA and table['all_gates']
        and len(table['root_weight_rows'])==64)
    base=module('exact_provider_endpoint_base',HERE/BASE)
    helper=module('exact_provider_endpoint_gauss',HERE/BRIDGE)
    nodes=[aq(q(r['actual_binary_gu'])) for r in table['root_weight_rows']]
    weights=[aq(q(r['actual_normalized_binary_weight'])) for r in table['root_weight_rows']]
    Ew=dy(table['certified_error_bounds']['normalized_total_weight_error'])
    Eu=dy(table['certified_error_bounds']['maximum_normalized_node_error'])
    remainder=helper.remainder_jet(F(2),F(1<<20))
    rows=[];component_exact={};component_actual={};ideal_fee=F(0);qnode_count=0
    for index,record in enumerate(profile['comparison_definition']['actual_binary_segments']):
        seg=record['original_binary_segment'];L=binary(seg['length']);component=record['component']
        if component not in component_exact:component_exact[component]=arb(0)
        a0=binary(seg['a0'])
        if seg['kind']=='hermite':
            check('only_actual_frontload_polynomial',index==0 and seg['strong_initial_speed_frontload_degree']==22)
            speed=[aq(binary(x)) for x in seg['strong_initial_speed_frontload_velocity_controls']]
            radius=list(map(binary,seg['strong_initial_speed_frontload_radius_controls']))
            dr=aq(radius[-1]-a0);dh=arb(0)
            for i,(u,w) in enumerate(zip(nodes,weights)):
                v=bernstein(speed,u);rad=1-v*v
                check('actual_first_Gauss_sqrt_domain_'+str(i),rad.lower()>0)
                dh+=w*rad.sqrt();qnode_count+=1
            dh*=aq(L)
            fee=q(first['physical_first_piece_partial_height_C0_C1_C2'][0])
            first_exact_sum=box(dh)
        else:
            dr=arb(0);dh=arb(0);fee=F(0)
            for piece_index,(lo,hi,phi) in enumerate(base.phase_pieces(seg)):
                span=hi-lo
                norm=base.affine_poly(phi,lo,span)
                centered=base.affine_poly(norm,F(1,2),F(1))
                cap=sum((abs(c)*2**j for j,c in enumerate(centered)),F(0))
                check('phase_entire_disk_'+str(index)+'_'+str(piece_index),aq(cap).exp()<1<<20)
                ds=[]
                for order in range(1,4):
                    p=norm
                    for unused in range(order):p=base.derivative(p)
                    ds.append(sum(map(abs,p),F(0)))
                d1,d2,d3=ds
                M=[F(1),d1,d1*d1+d2,d1**3+3*d1*d2+d3]
                table_error,exact_error,total=helper.primitive_errors(Ew,Eu,M,remainder)
                fee+=L*span*total[0]
                for u,w in zip(nodes,weights):
                    theta=base.polyeval(phi,aq(lo)+aq(span)*u)
                    dr+=aq(L*span)*w*theta.sin()
                    dh+=aq(L*span)*w*theta.cos();qnode_count+=1
        ideal_fee+=fee
        drerr=aq(binary(seg['dr']))-dr;dherr=aq(binary(seg['dh']))-dh
        component_exact[component]+=dh
        actual_local=aq(binary(seg['h1']))
        aggregate_error=actual_local-component_exact[component]
        accumulation_residual=binary(seg['h1'])-binary(seg['h0'])-binary(seg['dh'])
        component_actual[component]=float(seg['h1'])
        rows.append(dict(segment=index,component=component,local_segment=record['local_segment'],kind=seg['kind'],
            actual_stored_dr=seg['dr'],actual_stored_dh=seg['dh'],actual_local_h0=seg['h0'],actual_local_h1=seg['h1'],
            exact_radius_increment_box=box(dr),exact_height_increment_box=box(dh),
            stored_dr_minus_exact_quadrature_box=box(drerr),stored_dh_minus_exact_quadrature_box=box(dherr),
            stored_dr_internal_endpoint_error_upper=upper(abs(drerr)),stored_dh_internal_endpoint_error_upper=upper(abs(dherr)),
            exact_height_accumulation_rounding_residual=dict(numerator=str(accumulation_residual.numerator),denominator=str(accumulation_residual.denominator)),
            actual_component_height_minus_complete_exact_sum_box=box(aggregate_error),
            exact_Gauss_and_binary_table_to_analytic_height_error_upper=upper(aq(fee))))
    check('complete_all_original_segments',len(rows)==profile['segments']==12 and set(component_exact)=={'prefix','bridge'})
    # This is the original background constructor's explicit final addition.
    actual_combined=component_actual['prefix']+component_actual['bridge']
    exact_combined=component_exact['prefix']+component_exact['bridge']
    error=aq(binary(actual_combined))-exact_combined
    final_upper=abs(error)+aq(ideal_fee)
    output=dict(schema='actual-frontload-complete-provider-endpoint-arithmetic-v1',author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (a.background,a.background_resource,a.first_piece,a.table)},
        frozen_helper_sha256={BASE:BASE_SHA,BRIDGE:BRIDGE_SHA},input_kind='completed-unsolved-warm',
        warm_screen_sha256=profile['completed_warm_screen_sha256'],profile=profile['frozen_profile'],rows=rows,
        all_original_segments=12,complete_quadrature_nodes_evaluated=qnode_count,
        actual_binary_component_endpoint_heights=component_actual,actual_binary_combined_provider_height=actual_combined,
        exact_mathematical_binary_Gauss_combined_height_box=box(exact_combined),
        actual_combined_minus_exact_binary_Gauss_box=box(error),actual_complete_endpoint_arithmetic_error_upper=upper(abs(error)),
        complete_binary_Gauss_and_table_to_analytic_endpoint_fee=upper(aq(ideal_fee)),
        actual_combined_provider_height_minus_analytic_piecewise_height_upper=upper(final_upper),
        analytic_reference='Constructor-length integrals of the stored first velocity square-root and the subsequent exact binary phase cosines, all with one zero global height anchor.',
        all_actual_endpoint_integral_evaluation_and_height_accumulation_differences_included=True,
        phase_parameter_initialization_relative_to_ideal_physical_parameters_paid=False,
        uniform_libm_or_floating_function_derivative_error_claimed=False,
        repaired_radius_induced_height_or_complete_surface_mean_or_closed_D_certified=False,
        ideal_length_root_global_alignment_or_new_solution_claimed=False,
        new_ODE_Node_Newton_or_geometry_samples=0,gates=gates,gate_count=len(gates),all_gates=True,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),gates=len(gates),quadrature_nodes=qnode_count,
        actual_height=actual_combined,internal_error_upper=float(abs(error).upper()),
        complete_analytic_error_upper=float(final_upper.upper()))),flush=True)

if __name__=='__main__':main()
