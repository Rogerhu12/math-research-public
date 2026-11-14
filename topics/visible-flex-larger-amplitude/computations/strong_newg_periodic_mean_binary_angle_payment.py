#!/usr/bin/env python3
"""Pay q106 exact-mean node displacement to all actual binary angular nodes.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
For each existing whole radial/complex-angle atom, Cauchy gives |dpsi f|<=M/delta.
The full average absolute displacement of the original binary angular table
then pays its exact mathematical mean. Internal function evaluation, modal
argument rounding, dot products, radial nodes and coordinate alignment remain
separate. No actual accepted field or original mean implementation is modified.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import ast
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import struct
import time
import numpy as np
from flint import arb,ctx

STRIP_SHA='6439232c6375cb2646c20893c2ffc7879865bc991ac39da6089f7908e878a4d2'
PRIMARY_SHA='83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293'
HEIGHT_SOURCE_SHA='e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)
def binary(x):return F.from_float(float(x))
def aq(q):
    q=F(q);return arb(q.numerator)/q.denominator
def dy(q):return F(int(q[0]))*F(2)**int(q[1])
def upper(q):
    m,e=arb(q).upper().man_exp();return [str(m),int(e)]
def rat(q):
    q=F(q);return dict(numerator=str(q.numerator),denominator=str(q.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('strip','primary','height-source','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();started=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists():raise FileExistsError('A fresh binary-angle payment certificate is required')
    counts={}
    def check(name,ok):
        counts[name]=counts.get(name,0)+1
        if not ok:raise ArithmeticError(name)
    for path,wanted in ((a.strip,STRIP_SHA),(a.primary,PRIMARY_SHA),(a.height_source,HEIGHT_SOURCE_SHA)):
        check('frozen_actual_source_identity',sha(path)==wanted)
    strip,primary=read(a.strip),read(a.primary)
    check('complete_actual_repaired_strip_domain',strip['complete_domain_cover'] and
          strip['all_complex_domain_gates'] and not strip['failed_atoms'] and
          strip['complete_atoms']==3327 and len(strip['rows'])==3327 and strip['exact_mean_angular']==1360 and
          strip['primary_sha256']==PRIMARY_SHA)
    check('accepted_original_q106_identity',primary['solver_success'] and not primary.get('audit_pending',True) and primary['modes']==28)
    parsed=ast.parse(a.height_source.read_text())
    cls=next(n for n in parsed.body if isinstance(n,ast.ClassDef) and n.name=='CylindricalPrefix')
    basis=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='basis')
    assign=next(n for n in basis.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='theta' for t in n.targets))
    literal=ast.unparse(assign.value)
    expected=ast.parse('2*np.pi*np.arange(n)/n',mode='eval').body
    check('exact_original_theta_expression',ast.dump(assign.value,include_attributes=False)==ast.dump(expected,include_attributes=False))
    # Execute only the already identified pure node expression, never the basis,
    # field, BVP or any trigonometric/function evaluation of the geometry.
    N=1360
    expr=ast.Expression(body=assign.value);ast.fix_missing_locations(expr)
    theta=np.asarray(eval(compile(expr,'<original-binary-angular-node-expression>','eval'),{'np':np,'n':N}),dtype=np.float64)
    check('complete_actual_binary_node_table',theta.shape==(N,) and np.isfinite(theta).all() and theta[0]==0 and np.all(np.diff(theta)>0))
    errors=[];nodes=[]
    for j,x in enumerate(theta):
        target=2*arb.pi()*j/N
        error=upper(abs(aq(binary(x))-target));q=dy(error)
        check('rigorous_nonnegative_node_displacement',q>=0 and (j!=0 or q==0))
        errors.append(q)
        nodes.append(dict(j=j,binary64_bits_big_endian=struct.pack('>d',float(x)).hex(),absolute_displacement_upper=error))
    E=sum(errors,F(0))/N
    check('mean_displacement_positive_and_finite',0<E<F(1,10**12))
    cursor=F(0);length=binary(primary['meridian_length']);mesh=list(map(binary,primary['mesh']))
    h_total=F(0);hs_max=F(0);hss_max=F(0);payments=[];covered_cells=set()
    for i,row in enumerate(strip['rows']):
        lo,hi=map(F,row['s_interval']);delta=F(row['strip_width']);cell=row['original_interval']
        check('complete_current_radial_atom_coverage',lo==cursor and lo<hi and mesh[cell]<=lo<hi<=mesh[cell+1])
        check('same_complete_holomorphic_comparison_field',row['whole_physical_interval_and_complex_angular_strip'] and
              row['whole_repair_homotopy'] and row['positive_complex_domain'] and
              row['actual_original_quintics_restricted_exactly'] and 0<delta<=F(1,16))
        M0=dy(row['complex_mean_integrand_Vz_absolute_upper'])
        M1=dy(row['complex_mean_derivative_Vsz_absolute_upper'])
        check('complete_mean_integrand_caps_are_positive',M0>0 and M1>=0)
        f0=M0*E/delta;f1=M1*E/delta;h=(hi-lo)*f0
        h_total+=h;hs_max=max(hs_max,f0);hss_max=max(hss_max,f1)
        payments.append(dict(atom=i,original_interval=cell,source_atom=row['atom'],
            s_interval=[str(lo),str(hi)],strip_width=str(delta),
            mean_Hs_node_displacement_upper=upper(aq(f0)),
            mean_Hss_node_displacement_upper=upper(aq(f1)),
            anchored_H_atom_node_displacement_upper=upper(aq(h))))
        covered_cells.add(cell);cursor=hi
    check('complete_original_length_and_cells',cursor==length and covered_cells==set(range(len(mesh)-1)))
    bounds=[h_total,hs_max,hss_max]
    previous_alias=list(map(dy,strip['complete_mean_alias_H_Hs_Hss_upper']))
    total_alias_and_nodes=[x+y for x,y in zip(bounds,previous_alias)]
    out=dict(schema='actual-q106-complete-periodic-mean-binary-angle-node-payment-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (a.strip,a.primary,a.height_source)},
        primary_sha256=PRIMARY_SHA,background_comparison_definition_sha256=strip['background_comparison_definition_sha256'],
        state_comparison_definition_sha256=strip['state_comparison_definition_sha256'],
        all_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,
        original_angular_expression=literal,mean_angular=N,numpy_version=np.__version__,arb_precision_bits=ctx.prec,
        actual_binary_node_table_bytes_sha256=hashlib.sha256(theta.astype('<f8').tobytes()).hexdigest(),
        exact_actual_binary_node_table_and_displacement_upper=nodes,
        exact_average_absolute_node_displacement_upper=rat(E),average_displacement_display=float(E),
        maximum_absolute_node_displacement_upper=rat(max(errors)),maximum_displacement_display=float(max(errors)),
        complete_radial_atoms=len(payments),complete_original_cells=len(mesh)-1,per_atom=payments,
        exact_anchored_H_Hs_Hss_node_displacement_upper=list(map(rat,bounds)),
        anchored_H_Hs_Hss_node_displacement_upper=[upper(aq(q)) for q in bounds],
        anchored_H_Hs_Hss_node_displacement_display=list(map(float,bounds)),
        exact_alias_plus_node_displacement_upper=list(map(rat,total_alias_and_nodes)),
        alias_plus_node_displacement_display=list(map(float,total_alias_and_nodes)),
        Cauchy_argument='For every fixed real radial/homotopy parameter use a disk of radius d<delta centered at any real angle, |dpsi f|<=M/d; let d increase to delta. Integrate on the real interval between corresponding nodes and average all 1360 complete terms.',
        same_uniform_angular_average_measure=True,same_zero_height_anchor=True,
        exact_mathematical_f_at_actual_binary_nodes_only=True,
        internal_libm_modal_argument_rounding_dot_products_or_mean_summation_paid=False,
        radial_affine_nodes_or_coordinate_alignment_paid=False,
        original_floating_implementation_or_full_continuous_surface_certified=False,
        new_ODE_Node_Newton_or_geometry_calls=0,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(out,separators=(',',':')).encode()
    a.out.write_bytes(gzip.compress(data,compresslevel=9,mtime=0) if a.out.suffix=='.gz' else data)
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),all_gates=True,gates=out['gate_count'],
        complete_atoms=len(payments),mean_angular=N,node_error_display=out['anchored_H_Hs_Hss_node_displacement_display'],
        bytes=a.out.stat().st_size,seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
