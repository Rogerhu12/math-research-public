#!/usr/bin/env python3
"""Consume actual background/state repairs in all required nonmean jets.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All estimates use exact rational full-angle bounds and the complete saved
radial suprema. The seventh jet X_spsipsi is included for the radial derivative
of the complete mean map. This does not itself pay or evaluate that mean.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

BACKGROUND_SOURCE='483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08'
STATE_SOURCE='71c929c36847500dd236e2d1750e4dd82d4ce1e428ad27fcf82053ae42901063'
CHART_SOURCE='7678b2b43984b74c94b948efb21ea014f75a25841ed40527e0b76c569190e0cb'
SYNTH_SOURCE='d319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def binary(x):return F.from_float(float(x))
def dyadic(z):return F(int(z[0]))*F(2)**int(z[1])
def rational(z):return {'numerator':str(z.numerator),'denominator':str(z.denominator)}
def upper(z,bits=160):
    if z<0:raise ArithmeticError('Positive error upper required')
    if not z:return ['0',0]
    e=z.numerator.bit_length()-z.denominator.bit_length()-bits
    scaled=z/F(2)**e
    m=(scaled.numerator+scaled.denominator-1)//scaled.denominator
    out=[str(m),e]
    if dyadic(out)<z:raise ArithmeticError('Inward Cartesian rounding')
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('background','background-resource','background-check','chart-source','synthesis-source','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--state-repair',type=Path,nargs='*',default=[])
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh complete Cartesian transfer required')
    d,res,audit=map(read,(a.background,a.background_resource,a.background_check));checks=[]
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        checks.append(name)
    check('actual_complete_background_comparison',d['all_gates'] and all(d['gates'].values()) and
          d['source_sha256']==BACKGROUND_SOURCE and res['exitcode']==0 and res['wait4_observed'])
    check('independent_saved_background_consumption',audit['all_gates'] and
          audit['input_sha256'][str(a.background)]==sha(a.background) and audit['input_sha256'][str(a.background_resource)]==sha(a.background_resource))
    check('frozen_original_chart_and_synthesis',sha(a.chart_source)==CHART_SOURCE and sha(a.synthesis_source)==SYNTH_SOURCE)
    states={}
    inputids={str(p):sha(p) for p in (a.background,a.background_resource,a.background_check,a.chart_source,a.synthesis_source)}
    for path in a.state_repair:
        s=read(path)
        check('actual_complete_original_state_repair',s['all_gates'] and all(s['gates'].values()) and s['source_sha256']==STATE_SOURCE)
        identity=s['input_identity']['primary_sha256']
        check('one_state_repair_per_original_field',identity not in states)
        states[identity]=s;inputids[str(path)]=sha(path)
    requests=[('X',0,0),('Xs',1,0),('Xpsi',0,1),('Xss',2,0),('Xspsi',1,1),('Xpsipsi',0,2),('Xspsipsi',1,2)]
    profiles=[]
    for bg in d['profiles']:
        path=Path(bg['accepted_primary']);saved=read(path);identity=sha(path);inputids[str(path)]=identity
        check('same_accepted_field',identity==bg['accepted_primary_sha256'] and saved['solver_success'] and
              not saved.get('audit_pending',True) and saved['angular_chart']=='general-support-core-blend-v1')
        q=[binary(z) for z in saved['chart_reference_coefficients']]
        modes=list(saved['chart_reference_frequencies'])
        check('complete_original_material_reference',len(q)==len(modes) and all(isinstance(m,int) and m>=2 for m in modes))
        L=binary(saved['meridian_length']);start_t=binary(saved.get('chart_transition_start',0));end_t=binary(saved.get('chart_transition_end',1))
        span=L*(end_t-start_t)
        check('full_positive_chart_transition',L>0 and 0<=start_t<end_t<=1)
        A=sum((abs((1-m*m)*c)/m for m,c in zip(modes,q)),F(0))
        B=sum((abs((1-m*m)*c) for m,c in zip(modes,q)),F(0))
        C=sum((m*abs((1-m*m)*c) for m,c in zip(modes,q)),F(0))
        P=sum(((1+m)*abs(c) for m,c in zip(modes,q)),F(0))
        rho=1+B;b1=F(15,8)/span;b2=6/span**2
        check('whole_angle_chart_positive',B<1)
        basis={
            'B':1+P,
            'Bpsi':rho,
            'Bpsipsi':C+rho*rho,
            'Bs':b1*(P+2*A),
            'Bss':b2*(P+2*A)+b1*b1*(A*A+2*A),
            'Bspsi':b1*(2*B+2*rho*A),
            'Bspsipsi':b1*(2*C+(1+3*rho)*B+2*A*(C+rho*rho)),
        }
        E0,E1,E2=map(dyadic,bg['global_explicit_repair_C0_C1_C2_upper'])
        background={
            'X':E0*basis['B'],
            'Xs':E1*basis['B']+E0*basis['Bs'],
            'Xpsi':E0*basis['Bpsi'],
            'Xss':E2*basis['B']+2*E1*basis['Bs']+E0*basis['Bss'],
            'Xspsi':E1*basis['Bpsi']+E0*basis['Bspsi'],
            'Xpsipsi':E0*basis['Bpsipsi'],
            'Xspsipsi':E1*basis['Bpsipsi']+E0*basis['Bspsipsi'],
        }
        state=states.get(identity);state_errors=None
        if state is not None:
            ident=state['input_identity'];M=saved['modes'];n=3*M+1
            check('same_full_state_metric_and_gauge',ident['primary_sha256']==identity and ident['gauge_amplitude']==saved['gauge_amplitude'] and
                  state['modes']==M and state['state_count']==n and [r['state_index'] for r in state['state_bounds']]==list(range(n)))
            gauge=abs(binary(saved['gauge_amplitude']))
            state_errors={}
            for name,so,ao in requests:
                cost=F(0)
                for j,row in enumerate(state['state_bounds']):
                    if j==0:weight=1
                    else:
                        m=2*((j-1)%M+1)
                        weight=1 if ao==0 else m if ao==1 else m*m+(j<=2*M)
                    cost+=gauge*weight*dyadic(row['global_correction_C0_C1_C2'][so])
                state_errors[name]=cost
        jets=[]
        for name,so,ao in requests:
            value=background[name]+(state_errors[name] if state_errors is not None else 0)
            rounded=upper(value)
            check('complete_exact_nonmean_transfer_sum',dyadic(rounded)>=value>=0)
            jets.append({'jet':name,'physical_s_order':so,'computational_psi_order':ao,
                'background_repair_uniform_Euclidean_upper':upper(background[name]),
                'state_repair_uniform_Euclidean_upper':upper(state_errors[name]) if state_errors is not None else None,
                'combined_paid_repair_uniform_Euclidean_upper':rounded,
                'exact_combined_unrounded':rational(value)})
        profiles.append({'accepted_primary_sha256':identity,'background_comparison_definition_sha256':bg['comparison_definition_sha256'],
            'state_comparison_definition_sha256':state['comparison_field_definition_sha256'] if state is not None else None,
            'full_state_repair_included':state is not None,'modes':saved['modes'],'gauge':rational(abs(binary(saved['gauge_amplitude']))),
            'chart_reference_coefficients_exact':list(map(rational,q)),'chart_reference_frequencies':modes,
            'physical_chart_transition_span_exact':rational(span),
            'full_angle_sums':{k:rational(v) for k,v in [('arc_offset_A',A),('rho_variation_B',B),('rho_derivative_C',C),('support_position_perturbation_P',P)]},
            'global_chart_weight_first_second':list(map(rational,(b1,b2))),
            'global_dimensionless_base_jet_upper':{k:rational(v) for k,v in basis.items()},'jet_rows':jets,
            'complete_physical_s_and_every_real_psi':True,
            'complete_mean_H_Hs_Hss_paid':False,'floating_or_coordinate_alignment_costs_paid':False,
            'original_accepted_field_or_target_g_changed':False})
    result={'schema':'actual-background-and-state-repair-to-nonmean-seven-Cartesian-jets-v1','scope':__doc__,
        'author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)','all_gates':True,'gate_count':len(checks),'checks':checks,
        'source_sha256':sha(__file__),'input_identities':inputids,'profiles':profiles,
        'seventh_jet_required_for_radial_mean_derivative_explicitly_paid':True,
        'wholefield_mean_change_paid':False,'PDE_metric_curvature_reach_closed_surface_certified':False,
        'all_original_candidate_and_g_identities_retained':True,'new_ODE_Node_Newton_or_spatial_sampling':0,
        'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_gates':True,'gates':len(checks),'path':str(a.out),'sha256':sha(a.out),
        'jet_displays':[{r['jet']:float(dyadic(r['combined_paid_repair_uniform_Euclidean_upper'])) for r in p['jet_rows']} for p in profiles]}),flush=True)


if __name__=='__main__':main()
