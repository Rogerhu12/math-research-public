#!/usr/bin/env python3
"""Inspect the original warm chart gate without evaluating a geometry field.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This explicit diagnostic installs the identical actual/provider/response path,
then stops at the original raw-node/common-grid orientation check. It records
every nonpositive displayed spacing and exact binary-coefficient polynomial
values. It neither accepts the failed field nor changes the production gate.
"""
from fractions import Fraction as F
import hashlib
import inspect
import json
from math import comb
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
ORIGINAL_SHA='614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binary(x):return F.from_float(float(x))
def exact(x):
    x=F(x);return dict(numerator=str(x.numerator),denominator=str(x.denominator))

def probe(obj,x,t,flow,p,output):
    from root_neck_chart import NeckChart
    nc=NeckChart(obj._neck_knots,flow.breaks)
    node,nd=obj.chart(x,0.);grid,gd=obj.chart(t,0.)
    mirror,mirror_d=nc.evaluate(t)
    if not np.array_equal(mirror,grid) or not np.array_equal(mirror_d,gd):
        raise ValueError('Direct inspected chart differs from actual object chart')
    v,w,r=nc.v[:-1],nc.v[1:],nc.r
    c3=10*r-6*v-4*w;c4=-15*r+8*v+7*w;c5=6*r-3*v-3*w
    bernstein=[]
    for j in range(len(r)):
        power=[binary(v[j]),F(0),3*binary(c3[j]),4*binary(c4[j]),5*binary(c5[j])]
        controls=[sum((power[i]*F(comb(k,i),comb(4,i)) for i in range(k+1)),F(0)) for k in range(5)]
        bernstein.append(dict(interval=j,t=[float(nc.t[j]),float(nc.t[j+1])],
            s=[float(nc.s[j]),float(nc.s[j+1])],secant=float(r[j]),
            exact_derivative_Bernstein_lower=exact(min(controls)),
            exact_binary_polynomial_strictly_increasing=min(controls)>0))
    def value(z):
        j=int(np.clip(np.searchsorted(nc.t,z,side='right')-1,0,len(nc.h)-1))
        u=(binary(z)-binary(nc.t[j]))/binary(nc.h[j])
        q=binary(nc.s[j])+binary(nc.h[j])*(binary(v[j])*u+binary(c3[j])*u**3+binary(c4[j])*u**4+binary(c5[j])*u**5)
        return j,q
    def bad_pairs(inputs,values,derivatives):
        result=[]
        for i in np.flatnonzero(np.diff(values)<=0):
            i=int(i);j0,q0=value(inputs[i]);j1,q1=value(inputs[i+1])
            result.append(dict(index=i,t=[float(inputs[i]),float(inputs[i+1])],
                t_hex=[float(inputs[i]).hex(),float(inputs[i+1]).hex()],
                exact_dt=exact(binary(inputs[i+1])-binary(inputs[i])),
                displayed_s=[float(values[i]),float(values[i+1])],displayed_ds=float(values[i+1]-values[i]),
                displayed_chart_derivatives=[float(derivatives[i]),float(derivatives[i+1])],
                chart_intervals=[j0,j1],exact_binary_coefficient_polynomial_ds=exact(q1-q0),
                same_piece_strict_positive_exact_ds=j0==j1 and q1>q0))
        return result
    nb,gb=bad_pairs(x,node,nd),bad_pairs(t,grid,gd)
    out=dict(schema='actual-warm-chart-orientation-diagnostic-v1',scope=__doc__,
        source_sha256=sha(__file__),original_geometry_source_sha256=ORIGINAL_SHA,
        original_chart_source_sha256=sha(HERE/'root_neck_chart.py'),
        raw_nodes=len(x),common_grid_nodes=len(t),all_actual_raw_nodes_retained=True,
        raw_min_displayed_spacing=float(np.diff(node).min()),grid_min_displayed_spacing=float(np.diff(grid).min()),
        raw_strict_increase=not nb,grid_strict_increase=not gb,
        raw_nonpositive_spacings=nb,grid_nonpositive_spacings=gb,
        raw_min_displayed_derivative=float(np.min(nd)),grid_min_displayed_derivative=float(np.min(gd)),
        physical_profile=dict(flow.cfg),actual_physical_breaks=list(map(float,flow.breaks)),
        original_numerical_knots=list(map(float,obj._neck_knots)),
        exact_binary_chart_piece_Bernstein=bernstein,
        all_exact_binary_polynomial_piece_derivatives_positive=all(z['exact_binary_polynomial_strictly_increasing'] for z in bernstein),
        original_geometry_gate_passed=not nb and not gb,
        geometry_field_computed=False,continuous_C2_chart_or_original_floating_function_certified=False,
        original_gate_changed_or_bypassed_for_geometry=False,new_ODE_Node_Newton_calls=0)
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='actual_warm_chart_probe_finished',raw_nonpositive=len(nb),grid_nonpositive=len(gb),
        all_exact_piece_derivatives_positive=out['all_exact_binary_polynomial_piece_derivatives_positive'],
        path=str(output),sha256=sha(output))),flush=True)
    return dict(finite_domain_passed=False,full_geometry_performed=False,
        original_chart_gate_diagnostic=dict(path=str(output),sha256=sha(output),
            original_gate_passed=out['original_geometry_gate_passed']),
        scope='Explicit chart-only diagnostic; finite_domain_passed is deliberately false because no complete field was requested.')

def main():
    import root_actual_geometry_field_complete_mean as geometry
    if sha(Path(geometry.__file__))!=ORIGINAL_SHA:raise ValueError('Original complete mean geometry source changed')
    original=inspect.getsource(geometry.main)
    before="        physical_nodes, unused_ds = obj.chart(x, 0.)\n        physical_grid, unused_ds = obj.chart(t, 0.)\n        if not np.all(np.diff(physical_nodes) > 0) or not np.all(np.diff(physical_grid) > 0):\n            raise ValueError('The physical chart lost orientation')\n"
    after="        completed = True\n        return chart_only_probe(obj,x,t,flow,p,output)\n"+before
    if original.count(before)!=1:raise ValueError('Original chart gate moved')
    changed=original.replace(before,after,1)
    if changed.replace(after,before,1)!=original:raise ValueError('Unexpected chart probe source modification')
    ns=dict(geometry.main.__globals__,chart_only_probe=probe)
    exec(compile(changed,'<explicit-chart-only-probe-before-original-gate>','exec'),ns)
    old=geometry.main;geometry.main=ns['main']
    from strong_frontload_anchor_loader_adapter import build
    anchor_ns,unused=build('geometry',HERE/'root_actual_geometry_field_anchor.py')
    try:anchor_ns['main']()
    finally:geometry.main=old

if __name__=='__main__':main()
