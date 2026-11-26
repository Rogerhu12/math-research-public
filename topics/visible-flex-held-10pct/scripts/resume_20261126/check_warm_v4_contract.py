#!/usr/bin/env python3
"""Small executed v4 core/parameter check; no BVP or accepted field is made."""
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


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--reference-source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    start=time.monotonic()
    here=Path(__file__).resolve().parent
    installed=args.repo/'topics/visible-flex-held-10pct/scripts'
    flatten_path=installed/'resume_transfer/material_flattened_support_core.py'
    reference=module('_v4_check_original',args.reference_source)
    flatten=module('_v4_check_flatten',flatten_path)
    provider=module('_v4_check_provider',here/'warm_homotopy_core_factory_v4.py')
    prior=module('_v4_check_prior',installed/'resume_20261126/warm_complement_core_factory_v3.py')
    q=.06
    modes=24
    original=reference.PlanarSupportCore(q,np.zeros(modes-1),3)
    options=dict(homotopy=.002,curvature_blend=1.,halfwidth=.5,transition=.2,
        target_curvature=.2,quadrature_order=12,integration_cells=64,transition_cells=24)
    rule=dict(legacy_power_start=2,legacy_floor=1e-9,
        physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)')
    definition=dict(gauge_q=q,phase_control_scale=1.,
        anchor_support_coefficients=original.coefficients.tolist(),anchor_core_settings=options,
        homotopy=.002,phase_basis=provider.BASIS_RULE,phase_parameter_scale_rule=rule)
    scales=np.maximum(q**np.arange(2,modes+1),1e-9)
    parameters=np.linspace(-.001,.001,modes)
    theta=np.linspace(0,2*np.pi,37)
    rows=[]
    for lam in (.002,.5,1.):
        baseline=flatten.MaterialFlattenedSupportCore(original,**dict(options,homotopy=lam))
        current=dict(definition,homotopy=lam)
        factory=provider.make_factory(current,reference_class=reference.PlanarSupportCore,
                                      anchor_baseline=baseline)
        zero=factory(q,np.zeros(modes-1),3)
        old,new=baseline.evaluate(theta),zero.evaluate(theta)
        identity={key:bool(np.array_equal(old[key],new[key])) for key in ('F','Ft','Ftt')}
        if not all(identity.values()):
            raise AssertionError('Literal full zero-control identity failed')
        nonzero=factory(q*np.exp(parameters[0]),parameters[1:]*scales,3)
        scale_error=float(abs(nonzero.controls-parameters).max())
        if scale_error>2e-15:
            raise AssertionError('Actual inherited parameter scaling failed')
        jets=nonzero.jet_parameter_derivatives(theta)
        checks=[]
        for index in (0,7,8,modes-1):
            step=1e-6
            plus_p,minus_p=parameters.copy(),parameters.copy()
            plus_p[index]+=step
            minus_p[index]-=step
            plus=factory(q*np.exp(plus_p[0]),plus_p[1:]*scales,3).evaluate(theta)
            minus=factory(q*np.exp(minus_p[0]),minus_p[1:]*scales,3).evaluate(theta)
            input_scale=np.r_[q*np.exp(parameters[0]),scales][index]
            error=max(float(abs((plus[key]-minus[key])/(2*step)-
                jets[j][index]*input_scale).max()) for j,key in enumerate(('F','Ft','Ftt')))
            checks.append(dict(column=index,max_absolute_two_jet_error=error))
            if error>1e-7:
                raise AssertionError('Actual-scale nonzero-control derivative check failed')
        local=np.linspace(0,zero.period,401,endpoint=False)
        phase_columns=zero._basis(local)
        full=zero._full_basis(local)
        complement=zero._complement_basis(local)
        mixture_error=max(float(abs(value-((1-lam)*a+lam*b)).max())
            for value,a,b in zip(phase_columns,full,complement))
        curvature_column_sample=float(abs(phase_columns[1]).max())
        D1=630./(256.*zero.transition)
        D2=2520./(64.*zero.transition**2)
        D3=(7560./16.+5040./64.)/zero.transition**3
        omega=zero.omega
        bound=(3*D2+omega**2+D3/omega+3*omega*D1)/(1+D1/omega)
        lower_gap=float(np.min(bound-(3*zero.phase_harmonics)**2))
        bound_slack=float(np.min(bound[:,None]-abs(phase_columns[3])))
        if mixture_error>2e-14 or curvature_column_sample>1+2e-14 or min(lower_gap,bound_slack)<0:
            raise AssertionError('Convex mixture or conservative derivative guard failed')
        protected=zero.halfperiod+np.linspace(-.49,.49,31)
        protected_columns=zero._basis(protected)
        full_protected=zero._full_basis(protected)
        interior_error=max(float(abs(value-(1-lam)*full_value).max())
                           for value,full_value in zip(protected_columns,full_protected))
        if interior_error>2e-14:
            raise AssertionError('Intermediate protection-arc tangent columns differ')
        small=factory(q,np.zeros(7),3)
        nested_error=max(float(abs(a-b[:8]).max())
            for a,b in zip(small._basis(local),phase_columns))
        if nested_error!=0:
            raise AssertionError('Modal extension changed an existing basis column')
        row=dict(homotopy=lam,literal_zero_core_identity=identity,
            actual_phase_scale_max_error=scale_error,derivative_checks=checks,
            mixture_formula_sample_error=mixture_error,
            sampled_curvature_column_max=curvature_column_sample,
            conservative_third_bound_minus_full_bound_min=lower_gap,
            sampled_third_derivative_bound_slack_min=bound_slack,
            protected_arc_mixed_column_error=interior_error,
            common_prefix_basis_bitwise_equal=nested_error==0)
        if lam==1.:
            previous_definition=dict(current,phase_basis=prior.BASIS_RULE)
            previous_factory=prior.make_factory(previous_definition,
                reference_class=reference.PlanarSupportCore,anchor_baseline=baseline)
            previous=previous_factory(q*np.exp(parameters[0]),parameters[1:]*scales,3)
            before,after=previous.evaluate(theta),nonzero.evaluate(theta)
            endpoint_identity={key:bool(np.array_equal(before[key],after[key]))
                               for key in ('F','Ft','Ftt','phi','kappa','kappa_u','kappa_uu')}
            if not all(endpoint_identity.values()):
                raise AssertionError('Lambda-one v3 endpoint formula differs')
            protected_values=nonzero.evaluate(protected)
            arc_error=float(abs(protected_values['kappa']-baseline.k).max())
            if arc_error>2e-13:
                raise AssertionError('Nonzero-control lambda-one exact arc was changed')
            if nonzero.reflection_roundoff>1e-11:
                raise AssertionError('Reflection closure numerical evaluation changed')
            row.update(endpoint_nonzero_geometry_bitwise_equal_to_v3=endpoint_identity,
                lambda_one_protected_curvature_error=arc_error,
                reflection_roundoff=float(nonzero.reflection_roundoff))
        if lam==.5:
            h=1e-6
            perturbed=[]
            for direction in (-1,1):
                value=lam+direction*h
                base=flatten.MaterialFlattenedSupportCore(original,**dict(options,homotopy=value))
                fac=provider.make_factory(dict(definition,homotopy=value),
                    reference_class=reference.PlanarSupportCore,anchor_baseline=base)
                perturbed.append(fac(q*np.exp(parameters[0]),parameters[1:]*scales,3).evaluate(local))
            fields=baseline._fields(local)
            x,W,_,_,C=baseline._window(local)
            baseline_phi_lambda=baseline._omega(local)[:,0]+(x-C)*baseline.beta
            baseline_kappa_lambda=(1-W)*(baseline.k-fields['kappa'])+baseline.beta*W
            dlambda=nonzero._basis_lambda_derivative(local)
            expected_phi=baseline_phi_lambda+nonzero.controls@dlambda[0]
            expected_kappa=baseline_kappa_lambda+nonzero.controls@dlambda[1]
            phi_error=float(abs((perturbed[1]['phi']-perturbed[0]['phi'])/(2*h)-expected_phi).max())
            kappa_error=float(abs((perturbed[1]['kappa']-perturbed[0]['kappa'])/(2*h)-expected_kappa).max())
            if max(phi_error,kappa_error)>2e-8:
                raise AssertionError('Nonzero-control lambda derivative lost its mixed term')
            row['nonzero_control_lambda_partial']=dict(phi_error=phi_error,kappa_error=kappa_error,
                phase_cross_term_max=float(abs(nonzero.controls@dlambda[0]).max()),
                curvature_cross_term_max=float(abs(nonzero.controls@dlambda[1]).max()))
        rows.append(row)
    files=(Path(__file__),flatten_path,args.reference_source,
        here/'warm_homotopy_core_factory_v4.py',here/'warm_supported_core_factory.py',
        installed/'resume_20261126/warm_complement_core_factory_v3.py')
    result=dict(scope=__doc__,synthetic_only=True,BVP_invoked=False,accepted_BVP_field=False,
        modes=modes,rows=rows,seconds=time.monotonic()-start,
        source_sha256={str(file):hashlib.sha256(file.read_bytes()).hexdigest() for file in files})
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False),flush=True)
    return 0


if __name__=='__main__':
    sys.exit(main())
