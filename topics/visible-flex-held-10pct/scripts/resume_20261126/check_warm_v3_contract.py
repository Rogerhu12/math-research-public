#!/usr/bin/env python3
"""Small synthetic v3 parameter/core check; no accepted BVP is created."""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


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
    a=p.parse_args()
    path=a.repo/'topics/visible-flex-held-10pct/scripts/resume_transfer/material_flattened_support_core.py'
    sys.path.insert(0,str(path.parent))
    ref=module('_warm_v3_test_original',a.reference_source)
    flatten=module('_warm_v3_test_flatten',path)
    here=Path(__file__).resolve().parent
    provider=module('_warm_v3_test_provider',here/'warm_complement_core_factory_v3.py')
    q=.06;M=24
    options=dict(homotopy=.002,curvature_blend=1.,halfwidth=.5,transition=.2,
                 target_curvature=.2,quadrature_order=12,integration_cells=64,
                 transition_cells=24)
    original=ref.PlanarSupportCore(q,np.zeros(M-1),3)
    baseline=flatten.MaterialFlattenedSupportCore(original,**options)
    definition=dict(gauge_q=q,phase_control_scale=1.,
        anchor_support_coefficients=original.coefficients.tolist(),anchor_core_settings=options,
        homotopy=.002,phase_basis=provider.BASIS_RULE,phase_parameter_scale_rule=dict(legacy_power_start=2,legacy_floor=1e-9,
            physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)'))
    factory=provider.make_factory(definition,reference_class=ref.PlanarSupportCore,
                                  anchor_baseline=baseline)
    scales=np.maximum(q**np.arange(2,M+1),1e-9)
    zero=factory(q,np.zeros(M-1),3)
    theta=np.linspace(0,2*np.pi,37)
    old,new=baseline.evaluate(theta),zero.evaluate(theta)
    identity={name:bool(np.array_equal(old[name],new[name])) for name in ('F','Ft','Ftt')}
    if not all(identity.values()):
        raise AssertionError('Literal zero-control geometry identity failed')
    parameters=np.linspace(-.001,.001,M)
    nonzero=factory(q*np.exp(parameters[0]),parameters[1:]*scales,3)
    scale_error=float(np.max(abs(nonzero.controls-parameters)))
    if scale_error>2e-15:
        raise AssertionError('Actual phase control/solver parameter contract failed')
    jets=zero.jet_parameter_derivatives(theta)
    checks=[]
    for index in (0,7,8,M-1):
        step=1e-6
        par=np.zeros(M);par[index]=step
        plus=factory(q*np.exp(par[0]),par[1:]*scales,3).evaluate(theta)
        minus=factory(q*np.exp(-par[0]),-par[1:]*scales,3).evaluate(theta)
        error=max(float(abs((plus[key]-minus[key])/(2*step)-
            jets[j][index]*np.r_[q,scales][index]).max())
            for j,key in enumerate(('F','Ft','Ftt')))
        checks.append(dict(column=index,max_absolute_two_jet_error=error))
        if error>1e-7:
            raise AssertionError('Actual-scale parameter derivative check failed')
    small=factory(q,np.zeros(7),3)
    prefix_frequency_identity=bool(np.array_equal(small.omega,zero.omega[:8]))
    if not prefix_frequency_identity:
        raise AssertionError('Frequency fitting changed the common infinite family')
    final_options=dict(options,homotopy=1.)
    final_baseline=flatten.MaterialFlattenedSupportCore(original,**final_options)
    final_definition=dict(definition,homotopy=1.)
    final_factory=provider.make_factory(final_definition,reference_class=ref.PlanarSupportCore,
                                        anchor_baseline=final_baseline)
    final_core=final_factory(q*np.exp(parameters[0]),parameters[1:]*scales,3)
    protected=final_baseline.halfperiod+np.linspace(-.49,.49,31)
    final_values=final_core.evaluate(protected)
    arc_error=float(np.max(abs(final_values['kappa']-final_baseline.k)))
    reflection=float(final_core.reflection_roundoff)
    if arc_error>2e-13 or reflection>1e-11:
        raise AssertionError('Protected arc or reflection closure check failed')
    result=dict(synthetic_only=True,BVP_invoked=False,accepted_BVP_field=False,
        literal_zero_core_identity=identity,actual_phase_scale_max_error=scale_error,
        common_prefix_frequencies_bitwise_equal=prefix_frequency_identity,
        lambda_one_nonzero_controls_protected_curvature_error=arc_error,
        lambda_one_nonzero_controls_reflection_roundoff=reflection,
        derivative_checks=checks,source_sha256={str(file):hashlib.sha256(file.read_bytes()).hexdigest()
            for file in (Path(__file__),path,a.reference_source,here/'warm_complement_core_factory_v3.py',
                         here/'warm_supported_core_factory.py')})
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
