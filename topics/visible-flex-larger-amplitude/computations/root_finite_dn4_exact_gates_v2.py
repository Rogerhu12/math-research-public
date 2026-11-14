#!/usr/bin/env python3
"""Consume the complete 18-group DN4 run using exact Fractions; never rerun ODEs."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

PRIMARY_SHA = '58e86a63b9b23894c45477fdcbbbe172c36ff8087ff8739e475ff8ed90d8d57d'
SOURCE_SHA = '3eeb508e6a865ca3549bd25f2824a580a758a9f55a13a4b15bf016cc917a6bc0'
RESOURCE_SHA = '067d17a88417e3410b043cfe13a952fcc8095dc36be15c8b751a0ecf24b00c37'
FIELDS_SHA = '94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def dyadic(v):
    if not isinstance(v,list) or len(v)!=2 or not all(isinstance(x,int) for x in v):
        raise ValueError('Exact two-integer dyadic required')
    return F(v[0])*F(2)**v[1]

def frac(v):
    return {'numerator':str(v.numerator),'denominator':str(v.denominator),
            'display_only':float(v)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists(): raise FileExistsError('Use a fresh output')
    t=a.topic
    files={
      'primary':t/'notes/2026-11-13-root-finite-dn4-normalized-r2.json.gz',
      'resource':t/'notes/2026-11-13-root-finite-dn4-normalized-r2-resource.json',
      'source':t/'computations/root_outer_actual_finite_dn4_v2.py',
      'fields':t/'notes/2026-11-12-root-linear-centre-local-restored-r1-summary.json',
      'R106':t/'results/R106-physical-correlation-and-complete-mean-remainder.md',
      'R109':t/'results/R109-complete-source-polynomial-and-frequency-jacobian.md'}
    hashes={k:digest(p) for k,p in files.items()}
    gates={}
    def gate(name,condition):
        gates[name]=bool(condition)
        if not condition: raise ArithmeticError(name)
    for k,h in [('primary',PRIMARY_SHA),('resource',RESOURCE_SHA),('source',SOURCE_SHA),('fields',FIELDS_SHA)]:
        gate(k+'_identity',hashes[k]==h)
    d=json.load(gzip.open(files['primary'],'rt'))
    resource=json.loads(files['resource'].read_text())
    fields=json.loads(files['fields'].read_text())
    gate('formal_exit_zero',resource['exitcode']==0 and resource['termination_signal'] is None)
    gate('producer_and_fields_identity',d['source_sha256']==SOURCE_SHA and d['fields_summary_sha256']==FIELDS_SHA)
    gate('full_material_cover',d['full_material_cover'] and len(d['groups'])==18 and sum(g['rows'] for g in d['groups'])==10793)
    gate('all_exact_product_rule_equalities',d['exact_algebra_checks']=={
      'all_full_product_rule_coefficients_equal':True,'exact_rational_equalities':4232,
      'includes_full_mean_derivative_and_absent_centre_input_modes':True})
    gate('radial_sup_before_sum',d['global_radial_sup_before_modal_sum'])
    gate('stable_material_normalization_and_every_finite_entry',d['all_finite_entries_checked'] and d['schema']=='actual-r109-full46-normalized-material-dn4-v2')
    expected={(g['cell'],g['segment']):g for g in fields['groups']}
    gate('all_original_groups_once',len(expected)==18 and set(expected)=={(g['cell'],g['segment']) for g in d['groups']})
    matrices=[]
    material_hashes={}
    for g in d['groups']:
        key=(g['cell'],g['segment']); original=expected[key]
        gate('complete_rows_%s_%s'%key,g['complete'] and g['rows']==original['panels'])
        wanted={Path(c['path']).name:c['sha256'] for c in original['chunks']}
        got={Path(p).name:h for p,h in g['input_hashes'].items()}
        gate('all_original_chunks_%s_%s'%key,wanted==got)
        for c in original['chunks']:
            p=t/c['path']; actual=digest(p)
            gate('chunk_'+p.name,actual==c['sha256'])
            material_hashes[str(p.relative_to(t))]=actual
        A=g['weighted_source_jacobian_upper']; E=g['weighted_complete_derivative_remainder_upper']
        gate('all_92_by_46_entries_%s_%s'%key,len(A)==len(E)==92 and all(len(r)==46 for r in A+E))
        A=[[dyadic(x) for x in row] for row in A]
        E=[[dyadic(x) for x in row] for row in E]
        gate('complete_tail_included_%s_%s'%key,all(F(0)<=E[i][j]<=A[i][j] for i in range(92) for j in range(46)))
        gate('tilts_count_only_legal_rows_%s_%s'%key,set(g['tilted_derivative_domains_accepted'])=={'2','4','8','16'} and all(0<=v<=g['rows'] for v in g['tilted_derivative_domains_accepted'].values()))
        matrices.append(A)
    exact_columns=[sum(max(A[i][j] for A in matrices) for j in range(46)) for i in range(92)]
    stored=d['global_input_column_sums']
    gate('full_input_column_order',[(n,c) for n,c,_ in stored]==[(n,c) for n in range(2,93,2) for c in ('P','K')])
    gate('all_saved_column_sums_outward',all(x<=dyadic(v[2]) for x,v in zip(exact_columns,stored)))
    bound=dyadic(d['global_complete_source_derivative_operator_upper'])
    gate('global_upper_outward',max(dyadic(v[2]) for v in stored)<=bound)
    gate('strict_operator_below_10',bound<10)
    R=F(1,128)
    d64=1-F(5,4)*F(1,64)-4*F(1,64)**2
    J64=(50+128*F(1,64)+F(23,9)*(F(5,4)+4*F(1,64))+F(23,18)*(F(5,4)+16*F(1,64)))/d64+F(1,64)*(10+16*F(1,64)+F(23,18)*(F(5,4)+4*F(1,64)))*(F(5,4)+16*F(1,64))/d64**2
    gate('R106_complete_derivative_constant',J64==F(177343168,3018027) and J64<60)
    gate('Cauchy_circle_inside_full_domain',F(3,2)*R<F(1,64))
    hessian=F(23,9)+270*R
    gate('complete_hessian_below_5',hessian==F(2687,576) and hessian<5)
    gate('complete_Taylor_coefficient',hessian/2<F(5,2))
    out={'scope':'Actual fixed-centre low46 derivative and conditional full-source Hessian; no Green, beta, cut, or whole-ball fixed point is claimed',
      'source_sha256':digest(Path(__file__)),'inputs':{k:{'path':str(p.relative_to(t)),'sha256':hashes[k]} for k,p in files.items()},
      'gates':gates,'all_gates':all(gates.values()),'material_hashes':material_hashes,
      'counts':{'original_groups':18,'original_material_rows':10793,'input_columns':92,'output_modes':46,'exact_product_rule_comparisons':4232},
      'operator_upper_exact':d['global_complete_source_derivative_operator_upper'],
      'operator_upper_display':float(bound),'strict_10_slack':frac(10-bound),
      'largest_column':max(stored,key=lambda v:dyadic(v[2]))[:2],
      'Cauchy_radius':frac(R/2),'complete_hessian_at_Rmax':frac(hessian),
      'strict_5_slack':frac(5-hessian),'Taylor_coefficient_used':frac(F(5,2))}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_gates':out['all_gates'],'gates':len(gates),'operator_upper_display':float(bound),'output_sha256':digest(a.out)},ensure_ascii=False))

if __name__=='__main__': main()
