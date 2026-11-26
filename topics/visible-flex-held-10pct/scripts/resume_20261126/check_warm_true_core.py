#!/usr/bin/env python3
"""Small synthetic runtime check of the new true warm-core interval API.

This is not an accepted field, prefix certificate, or completion result.
It checks a small lambda-one core with nonzero phase controls and compares
floating source values only as diagnostics, never as interval proofs.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
import mpmath as mp


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--reference-source',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--family',choices=('v2','v3'),default='v2')
    a=p.parse_args()
    scripts=a.repo/'topics/visible-flex-held-10pct/scripts'
    path=scripts/'resume_transfer/material_flattened_support_core.py'
    sys.path.insert(0,str(path.parent))
    ref=module('_true_warm_check_original',a.reference_source)
    flatten=module('_true_warm_check_flatten',path)
    here=Path(__file__).resolve().parent
    provider_path=here/('warm_complement_core_factory_v3.py' if a.family=='v3'
                        else 'warm_supported_core_factory_v2.py')
    provider=module('_true_warm_check_provider',provider_path)
    validated=module('_true_warm_check_oracle',here/'warm_phase_validated_core.py')
    q=.001;M=2
    options=dict(homotopy=1.,curvature_blend=1.,halfwidth=.5,transition=.2,
        target_curvature=.2,quadrature_order=12,integration_cells=64,transition_cells=24)
    original=ref.PlanarSupportCore(q,np.zeros(M-1),3)
    baseline=flatten.MaterialFlattenedSupportCore(original,**options)
    definition=dict(gauge_q=q,phase_control_scale=1.,
        anchor_support_coefficients=original.coefficients.tolist(),anchor_core_settings=options,
        homotopy=1.,phase_parameter_scale_rule=dict(legacy_power_start=2,legacy_floor=1e-9,
            physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)'))
    if a.family=='v3':
        definition['phase_basis']=provider.BASIS_RULE
    factory=provider.make_factory(definition,reference_class=ref.PlanarSupportCore,
                                  anchor_baseline=baseline)
    parameters=np.array([.001,-.0002])
    core=factory(q*np.exp(parameters[0]),parameters[1:]*np.maximum(q**np.arange(2,M+1),1e-9),3)
    start=time.monotonic()
    def progress(value):
        print(json.dumps(value,allow_nan=False),flush=True)
    v=validated.build_oracle(core,scripts/'resume_m3',
        scripts/'resume_m3/certify_r59_fixed_mean_ranges.py',
        scripts/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py',progress=progress)
    points=np.array([.031,.31,.53,.77,1.01,1.3,1.7,2.01,2.3,4.3,6.17])
    if a.family=='v3':
        half=mp.pi/3;S,b=mp.mpf(core.halfwidth),mp.mpf(core.transition)
        joins=np.array([float(x) for x in (0,half-S-b,half-S,half,half+S,half+S+b,2*half)])
        points=np.unique(np.r_[points,np.nextafter(joins,-np.inf),joins,
                               np.nextafter(joins,np.inf)])
    float_values=core.evaluate(points)
    gaps={key:0. for key in ('F','Ft','Ftt')}
    widths={key:0. for key in gaps}
    for i,point in enumerate(points):
        true=v.point(v.I(point))
        for key in gaps:
            for j,box in enumerate(true[key]):
                lo,hi=map(float,box.x)
                value=float(float_values[key][i,j])
                gaps[key]=max(gaps[key],max(lo-value,value-hi,0.))
                widths[key]=max(widths[key],hi-lo)
    if max(gaps.values())>1e-6:
        raise AssertionError('Large source/true-core discrepancy in API check')
    protected=v.curvature_jets(v.L)
    if not float(protected[0].x[0])<=.2<=float(protected[0].x[1]):
        raise AssertionError('The literal target curvature is not enclosed on the protected arc')
    bounds=v.all_angle_curvature_bounds()
    if not bounds['positive_curvature_certified']:
        raise AssertionError('The small synthetic phase example was not positively enclosed')
    independent=[]
    if a.family=='v3':
        # Independent high-precision differentiation is a finite API check,
        # not the interval proof. It also resolves the true irrational
        # frequencies independently of the numerical provider's floats.
        def mpq(value):
            from fractions import Fraction
            value=Fraction(float(value))
            return mp.mpf(value.numerator)/value.denominator
        S,b=mpq(core.halfwidth),mpq(core.transition)
        half=mp.pi/3;P=2*half;length=half-S
        coefficients=[mpq(x) for x in core.controls]
        def exact_increment(u):
            local=u-mp.floor(u/P)*P
            t=(abs(local-half)-S)/b
            W=(mp.mpf(0) if t<=0 else mp.mpf(1) if t>=1 else
               126*t**5-420*t**6+540*t**7-315*t**8+70*t**9)
            vv=local if local<half else local-P
            return sum(d*W*mp.sin((j+1)*mp.pi/length*vv)/
                       ((j+1)*mp.pi/length+mp.mpf(630)/(256*b))
                       for j,d in enumerate(coefficients))
        for j in range(M):
            omega=(j+1)*mp.pi/length
            if not mpq(v.freq.x[0][j])<=omega<=mpq(v.freq.x[1][j]):
                raise AssertionError('True complementary frequency lies outside its interval')
        for value in (.031,.31,.53,.77,1.01,1.3,1.7,2.01):
            boxes=v.phase_increment(v.I(value))
            checks=[]
            for order,box in enumerate(boxes):
                exact=mp.diff(exact_increment,mpq(value),order)
                contained=bool(mpq(box.x[0])<=exact<=mpq(box.x[1]))
                checks.append(contained)
                if not contained:
                    raise AssertionError('True complementary phase derivative is outside its interval')
            independent.append(dict(material_angle=value,phase_through_third_contains_mp=checks))
        if any(np.any(np.asarray(z.x)!=0) for z in v.phase_increment(v.L)):
            raise AssertionError('The wrap point must have exactly zero supported increment')
        for left,right in zip(v.phase_increment(v.I(0)),v.phase_increment(v.T)):
            difference=left-right
            if not float(difference.x[0])<=0<=float(difference.x[1]):
                raise AssertionError('The two true sector ends fail the same periodic jet check')
    sources=[Path(__file__),provider_path,here/'warm_phase_validated_core.py',
             here/'warm_supported_core_factory.py',path,a.reference_source,
             scripts/'resume_m3/r53_validated_material_core.py',
             scripts/'resume_m3/certify_r59_fixed_mean_ranges.py',
             scripts/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py']
    result=dict(synthetic_only=True,accepted_BVP_field=False,complete_surface=False,family=a.family,
        oracle=v.metadata(),source_float_values_are_only_diagnostics=True,
        sampled_material_angles=points.tolist(),
        independent_phase_derivative_diagnostics=independent,
        pointwise_float_cache_outside_interval_gap=gaps,point_interval_max_width=widths,
        protected_center_curvature_jets=[list(map(float,z.x)) for z in protected],
        continuous_synthetic_core_curvature_bounds=bounds,seconds=time.monotonic()-start,
        source_hashes={str(file.resolve()):hashlib.sha256(file.read_bytes()).hexdigest() for file in sources})
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False),flush=True)


if __name__=='__main__':
    main()
