#!/usr/bin/env python3
"""R6 bounds for the exact integrated-tail endpoint coefficients themselves.

The background is unchanged. Bounds cover the finite endpoint Hermite
perturbation, not an exact nonlinear infinite tail. A supplied background
curvature value is an explicit hypothesis, never a certificate generated here.
"""
import argparse,hashlib,importlib.util,json,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
sys.dont_write_bytecode=True


def exact(x):return Q.from_float(float(x))
def show(q):return dict(numerator=str(q.numerator),denominator=str(q.denominator),approximate=float(q))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','manifest','out'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--assume-background-curvature',type=float);a=p.parse_args()
    reader=a.source_topic/'scripts/db6f_tail_integrated.py';spec=importlib.util.spec_from_file_location('geometric_collar_integrated',reader)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod);tail=mod.IntegratedTail(a.manifest)
    r=exact(tail.meta['radialGeometry']['innerAnchor']);cuff=exact(tail.meta['parameters']['rCuff']);L=r-cuff
    if not 0<L<=cuff:raise ValueError('R6 simplified bounds require 0<L<=cuff')
    # At the first node, these are the actual defining binary V,Vr,Vrr;
    # no endpoint radius subtraction, quadrature, or interpolation is used.
    rows=[tail.source_values[0],tail.first[0],tail.second[0]];norms=[]
    for c in rows:
        planar=sum(2*(1+abs(int(m)))**2*abs(exact(v))for m,v in zip(tail.planar_modes,c[:tail.P]))
        height=sum((1+int(m))**2*abs(exact(v))for m,v in zip(tail.height_modes,c[tail.P:]))
        norms.append(planar+height)
    K=norms[0]/L**2+norms[1]/L+norms[2];eta1=Q(9,4)*L*K;metric=2*eta1+eta1*eta1
    if eta1>=1:raise ValueError('R6 local immersion bound is insufficient')
    theorem=a.source_topic.parents[1]/'topics/smooth-unrippled-twist-flex/results/R6-fixed-metric-c2-collar-closure.md'
    result=dict(status='exact-rational-finite-Hermite-perturbation-budget',scope=__doc__,
        manifest=dict(file=str(a.manifest.resolve()),sha256=sha(a.manifest)),reader_sha256=sha(reader),script_sha256=sha(__file__),
        theorem=dict(file=str(theorem.resolve()),sha256=sha(theorem)),source_revision='869436630c99aa5a68afb55bd8877c826034d117',
        norm_majorant='2 sum_m (1+|m|)^2 |a_m| + sum_k (1+k)^2 |c_k| for horizontal sum a_m exp(i m theta) and height sum c_k cos(k theta). Triangle inequality bounds the vector Fourier C2 norm.',
        cuff=show(cuff),inner=show(r),L=show(L),endpoint_norms=[show(x)for x in norms],K=show(K),eta1=show(eta1),
        metric_operator_defect_upper=show(metric),local_immersion_minimum_singular_value_lower=show(1-eta1),
        nested_planar_projection_sufficient_conditions=bool(L*L*K/cuff<=Q(1,10)and 2*L*K<=Q(1,4)),
        background_flat_C2_limit_certified_here=False,source_ODE_certified=False,infinite_nonlinear_tail_certified=False,fixed_g_C2_Cauchy_convergence_certified=False)
    if a.assume_background_curvature is not None:
        B=exact(a.assume_background_curvature)
        if B<=0 or L*B>1:raise ValueError('Simplified second-jet bound requires B>0 and LB<=1')
        eta2=15*K;full=Q(3,2)*B*eta2+eta2*eta2/2+B*B*metric;curvature=(B+eta2)/(1-eta1)**2
        result['conditional_on_background_curvature']=dict(assumed_B=show(B),background_bound_certified_here=False,eta2=show(eta2),full_vector_Darboux_operator_upper=show(full),principal_curvature_upper=show(curvature))
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),K=float(K),eta1=float(eta1),metric_upper=float(metric),nested_projection=result['nested_planar_projection_sufficient_conditions'],conditional_background_curvature=a.assume_background_curvature)))


if __name__=='__main__':main()
