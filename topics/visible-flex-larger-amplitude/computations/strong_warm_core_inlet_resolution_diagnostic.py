#!/usr/bin/env python3
"""Inspect a complete unsolved warm core in its genuine reference chart.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The geometry screen is explicitly an unsolved warm field. Its complete core
is projected with the original PlanarSupportCore/GeneralCoreChart and exact
original cylindrical basis/project/values routines. No accepted endpoint is
invented, no original accepted file is modified, and no Flow/ODE/BVP/Node is
constructed. Higher-M rows are inlet projection diagnostics only.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np

DIAGNOSTIC_SHA='95e4ee845167bc95f54c92272fba192c80fa5fe5810dcab344fa4bcdf6ffefca'
CHART_SHA='7678b2b43984b74c94b948efb21ea014f75a25841ed40527e0b76c569190e0cb'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj
def rational(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('warm-screen','reference','source-topic','chart-source','original-diagnostic-source','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--modes',type=int,nargs='+',default=[28,32,40,64])
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh explicit warm-inlet diagnostic required')
    if sha(a.original_diagnostic_source)!=DIAGNOSTIC_SHA or sha(a.chart_source)!=CHART_SHA:
        raise ValueError('Original diagnostic/chart identity changed')
    warm,saved=read(a.warm_screen),read(a.reference)
    if not warm.get('finished') or warm.get('nonlinear_solution') is not False or not warm.get('finite_domain_passed') or warm.get('worker_start_attempts')!=0:
        raise ValueError('A complete explicit unsolved zero-worker geometry screen is required')
    if not saved.get('solver_success') or saved.get('audit_pending',True) or saved['angular_chart']!='general-support-core-blend-v1':
        raise ValueError('The genuine accepted reference chart is required')
    if Path(warm['actual_reference']).resolve()!=a.reference.resolve():
        raise ValueError('The warm reference path differs')
    reference_ids=[h for k,h in warm['source_sha256'].items() if Path(k).resolve()==a.reference.resolve()]
    if not reference_ids or any(h!=sha(a.reference) for h in reference_ids):
        raise ValueError('The warm reference SHA differs')
    geom=warm['geometry_fields']
    if geom['actual_core']!=warm['actual_core'] or geom['physical_profile']!=warm['warm_profile'] or warm['gauge']!=saved['gauge_amplitude']:
        raise ValueError('The complete warm core/profile/gauge identity differs')
    scripts=a.source_topic/'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    sys.path[:0]=[str(a.source_topic/'notes'),str(scripts)]
    from fixed_metric_mode3_core import PlanarSupportCore
    from curve_stable_prefix_bvp import CylindricalPrefix
    charts=module('explicit_warm_inlet_original_chart',a.chart_source)
    coef=np.asarray(warm['actual_core'],dtype=np.float64);base=int(saved['core']['base_mode'])
    freq=base*np.arange(1,len(coef)+1);original_m=int(saved['modes']);gauge=saved['gauge_amplitude']
    if coef.shape!=(original_m,) or base!=2 or not np.isfinite(coef).all():
        raise ValueError('Retain the complete original M28 support core')
    core=PlanarSupportCore(coef[0],coef[1:],base)
    # inlet_geometry uses no length/profile derivative: only the fixed
    # material reference and computational angle. Keep the real reference L.
    chart=charts.GeneralCoreChart(saved['chart_reference_coefficients'],saved['chart_reference_frequencies'],saved['meridian_length'])
    original_n=max(2048,128*original_m);cases=[(original_m,original_n),(original_m,2*original_n)]
    cases.extend((int(m),max(4096,128*int(m))) for m in a.modes if int(m)!=original_m)
    rows=[];same_core=np.array_equal(coef,np.asarray(saved['core']['coefficients'],dtype=np.float64))
    for M,N in cases:
        if not original_m<=M<=128:raise ValueError('Only retained or increased projection order')
        obj=SimpleNamespace(M=M,n=3*M+1,iz=2*M+1,even=base*np.arange(1,M+1))
        B,B1,B2=CylindricalPrefix.basis(obj,N);gi=chart.inlet_geometry(N);exact=core.evaluate(gi['theta'])
        state=CylindricalPrefix.project((exact['F']-gi['pos'])[None,:,:],B)[:,0]/gauge
        mapped=gi['pos']+gauge*CylindricalPrefix.values(state[:,None],B)[0]
        first=gi['p1']+gauge*CylindricalPrefix.values(state[:,None],B1)[0]
        second=gi['p2']+gauge*CylindricalPrefix.values(state[:,None],B2)[0]
        true1=exact['Ft']*gi['rho'][:,None]
        true2=exact['Ftt']*gi['rho'][:,None]**2+exact['Ft']*gi['rhop'][:,None]
        error=np.sum(first*first,axis=1)/gi['rho']**2-1
        row=dict(modes=M,angular=N,position=float(np.linalg.norm(mapped-exact['F'],axis=1).max()),
            first=float(np.linalg.norm(first-true1,axis=1).max()),second=float(np.linalg.norm(second-true2,axis=1).max()),
            metric_l1=float(np.sum(abs(np.fft.fft(error)/N))),metric_pointwise_max=float(np.max(abs(error))),
            arc_inversion_residual=float(np.max(abs(exact['arc_residual']))),is_new_bvp_solution=False)
        if same_core and (M,N)==(original_m,original_n):
            row['same_complete_core_baseline_regression']={k:abs(row[k]-saved['summary']['inlet'][k]) for k in ('position','first','second','metric_l1')}
            if max(row['same_complete_core_baseline_regression'].values())>3e-12:
                raise ValueError('The same-core warm formula did not reproduce original inlet diagnostics')
        rows.append(row);print(json.dumps(row),flush=True)
        del B,B1,B2
    sources={str(path):sha(path) for path in (Path(__file__),a.warm_screen,a.reference,a.chart_source,
        a.original_diagnostic_source,a.source_topic/'notes/fixed_metric_mode3_core.py',scripts/'curve_stable_prefix_bvp.py')}
    tails=[]
    for cutoff in (40,48,56):
        pairs=[(int(m),F.from_float(float(c))) for m,c in zip(freq,coef) if m>=cutoff]
        tails.append(dict(minimum_frequency=cutoff,complete_saved_core_mode_count=len(pairs),
            coefficient_l1_exact=rational(sum((abs(c) for m,c in pairs),F(0))),
            support_curvature_radius_l1_exact=rational(sum(((m*m-1)*abs(c) for m,c in pairs),F(0)))))
    out=dict(schema='explicit-unsolved-warm-full-core-inlet-resolution-diagnostic-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_and_input_sha256=sources,
        full_warm_core_coefficients=coef.tolist(),frequencies=freq.tolist(),warm_physical_profile=warm['warm_profile'],
        material_reference_coefficients=chart.coefficients.tolist(),material_reference_frequencies=chart.frequencies.tolist(),
        real_reference_length_used_only_as_positive_chart_constructor=saved['meridian_length'],
        inlet_formula_independent_of_profile_and_length=True,gauge=gauge,rows=rows,full_core_tail_diagnostics=tails,
        same_complete_core_as_accepted_reference=bool(same_core),no_new_accepted_endpoint=True,
        original_accepted_candidate_or_g_modified=False,new_Flow_ODE_Node_Newton_calls=0,
        continuous_metric_reach_or_closed_surface_certificate=False)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'event':'explicit_warm_core_inlet_diagnostic_finished','path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
