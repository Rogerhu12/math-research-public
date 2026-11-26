#!/usr/bin/env python3
"""Small synthetic v5 fixed-q/high-phase-chain check; never runs a BVP."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value
    spec.loader.exec_module(value);return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--reference-source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();begin=time.monotonic()
    here=Path(__file__).resolve().parent
    scripts=args.repo/'topics/visible-flex-held-10pct/scripts'
    public=scripts/'resume_20261126'
    files=dict(v5_factory=here/'warm_delta_phase_factory_v5.py',
        v4_factory=public/'warm_homotopy_core_factory_v4.py',
        common_geometry=public/'warm_supported_core_factory.py',
        material_geometry=scripts/'resume_transfer/material_flattened_support_core.py')
    provider=module('_v5_small_provider',files['v5_factory'])
    v4=module('_v5_small_v4_formula',files['v4_factory'])
    reference=module('_v5_small_original',args.reference_source)
    flatten=module('_v5_small_flatten',files['material_geometry'])
    q=.06;M=24;scale=.5
    original=reference.PlanarSupportCore(q,np.zeros(M-1),3)
    options=dict(homotopy=.002,curvature_blend=1.,halfwidth=.5,transition=.2,
        target_curvature=.2,quadrature_order=12,integration_cells=64,transition_cells=24)
    definition=dict(model_kind=provider.KIND,fixed_metric=False,gauge_q=q,
        phase_control_scale=scale,phase_parameter_scale_rule=copy.deepcopy(provider.SCALE_RULE),
        phase_basis=copy.deepcopy(v4.BASIS_RULE),
        anchor_support_coefficients=original.coefficients.tolist(),
        anchor_core_settings=options,
        implementation_sources={k:dict(path=str(v.resolve()),sha256=sha(v)) for k,v in files.items()})
    p=np.linspace(-.001,.001,M);p[0]=.000271
    scales=np.maximum(q**np.arange(2,M+1),1e-9)
    theta=np.linspace(0,2*np.pi,37)
    rows=[]
    for lam in (.002,.5,1.):
        baseline=flatten.MaterialFlattenedSupportCore(original,**dict(options,homotopy=lam))
        factory=provider.make_factory(dict(definition,homotopy=lam),
            reference_class=reference.PlanarSupportCore,anchor_baseline=baseline)
        zero=factory(q,np.zeros(M-1),3)
        old,new=baseline.evaluate(theta),zero.evaluate(theta)
        identity={k:bool(np.array_equal(old[k],new[k])) for k in ('F','Ft','Ftt')}
        if not all(identity.values()):
            raise AssertionError('Zero-control complete core identity failed')
        core=factory(q,p[1:]*scales,3)
        expected=np.r_[0.,scale*(p[1:]*scales)/scales]
        if not np.array_equal(core.controls,expected) or core.input_chain[0]!=0.:
            raise AssertionError('Actual v5 phase controls or fixed-q API column changed')
        jets=core.jet_parameter_derivatives(theta)
        if not all(np.all(j[0]==0.) for j in jets):
            raise AssertionError('The forbidden first API column was not zero')
        errors=[]
        for index in (1,7,8,23):
            h=1e-6;plus=p.copy();minus=p.copy()
            plus[index]+=h;minus[index]-=h
            gplus=factory(q,plus[1:]*scales,3).evaluate(theta)
            gminus=factory(q,minus[1:]*scales,3).evaluate(theta)
            error=max(float(np.max(abs((gplus[k]-gminus[k])/(2*h)-
                jets[j][index]*scales[index-1]))) for j,k in enumerate(('F','Ft','Ftt')))
            if error>1e-7:
                raise AssertionError('High phase physical-parameter chain differs')
            errors.append(dict(column=index,maximum_absolute_two_jet_FD_error=error))
        rejected=False
        try:
            factory(np.nextafter(q,np.inf),p[1:]*scales,3)
        except FloatingPointError:
            rejected=True
        if not rejected:
            raise AssertionError('The fixed q API accepted a changed value')
        larger_scales=np.maximum(q**np.arange(2,33),1e-9)
        larger_p=np.r_[p,np.zeros(8)]
        larger=factory(q,larger_p[1:]*larger_scales,3)
        local=np.linspace(0,core.period,257,endpoint=False)
        nested=all(np.array_equal(a,b[:M]) for a,b in zip(core._basis(local),larger._basis(local)))
        phase_nested=(np.array_equal(larger.controls[:M],core.controls) and
                      np.all(larger.controls[M:]==0.))
        if not nested or not phase_nested:
            raise AssertionError('Complete fixed anchor and phase family do not nest')
        a,b=core.evaluate(theta),larger.evaluate(theta)
        gap=max(float(np.max(abs(a[k]-b[k]))) for k in ('F','Ft','Ftt'))
        if gap>2e-14:
            raise AssertionError('Zero extension changed complete core geometry beyond floating summation')
        rows.append(dict(homotopy=lam,literal_zero_core_identity=identity,
            actual_phase_chain_bitwise_equal=True,first_API_jet_zero=True,
            changed_q_API_rejected=True,high_phase_derivatives=errors,
            common_basis_bitwise_equal=nested,actual_phase_zero_extension_bitwise_equal=bool(phase_nested),
            zero_extension_two_jet_roundoff=gap))
    result=dict(scope=__doc__,synthetic_only=True,BVP_invoked=False,
        actual_reexpression_executed=False,accepted_BVP_field=False,
        rows=rows,modes=M,phase_control_scale=scale,seconds=time.monotonic()-begin,
        source_hashes={str(path.resolve()):sha(path) for path in
            (*files.values(),Path(__file__),args.reference_source)})
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False),flush=True)
    return 0


if __name__=='__main__':
    sys.exit(main())
