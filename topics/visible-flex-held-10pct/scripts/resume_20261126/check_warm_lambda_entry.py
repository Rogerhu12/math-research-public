#!/usr/bin/env python3
"""Small core API check for the new lambda override; no BVP field is claimed."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--reference-source',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    flat_path=a.repo/'topics/visible-flex-held-10pct/scripts/resume_transfer/material_flattened_support_core.py'
    sys.path.insert(0,str(flat_path.parent))
    ref=module('_warm_entry_original',a.reference_source)
    flatten=module('_warm_entry_flatten',flat_path)
    provider_path=Path(__file__).with_name('warm_supported_core_factory.py')
    warm=module('_warm_entry_provider',provider_path)
    q=.06
    count=8
    options=dict(homotopy=.002,curvature_blend=1.,halfwidth=.5,transition=.2,
                 target_curvature=.2,quadrature_order=12,integration_cells=64,
                 transition_cells=24)
    original=ref.PlanarSupportCore(q,np.zeros(count-1),3)
    definition=dict(gauge_q=q,phase_control_scale=1.,
        anchor_support_coefficients=original.coefficients.tolist(),
        anchor_core_settings=copy.deepcopy(options))
    theta=np.r_[np.linspace(0,2*np.pi,31),np.pi/3+np.array([-.5,0,.5])]
    scales=np.maximum(q**np.arange(2,count+1),1e-10)
    rows=[]
    for lam in (.002,.5,1.):
        baseline=flatten.MaterialFlattenedSupportCore(original,**dict(options,homotopy=lam))
        definition['homotopy']=lam
        automatic=warm.make_factory(definition,reference_class=ref.PlanarSupportCore)
        live=warm.make_factory(definition,reference_class=ref.PlanarSupportCore,anchor_baseline=baseline)
        auto=automatic(q,np.zeros(count-1),3)
        core=live(q,np.zeros(count-1),3)
        geometry=baseline.evaluate(theta)
        identity={key:bool(np.array_equal(geometry[key],core.evaluate(theta)[key]))
                  for key in ('F','Ft','Ftt')}
        reconstructed={key:float(np.max(abs(geometry[key]-auto.evaluate(theta)[key])))
                       for key in ('F','Ft','Ftt')}
        jets=core.jet_parameter_derivatives(theta)
        derivative=[]
        for index in (0,count-1):
            h=1e-6
            vec=np.zeros(count);vec[index]=h
            plus=live(q*np.exp(vec[0]),vec[1:]*scales,3).evaluate(theta)
            minus=live(q*np.exp(-vec[0]),-vec[1:]*scales,3).evaluate(theta)
            derivative.append(dict(parameter=index,max_absolute_two_jet_error=max(
                float(abs((plus[key]-minus[key])/(2*h)-jets[j][index]*np.r_[q,scales][index]).max())
                for j,key in enumerate(('F','Ft','Ftt')))))
        row=dict(homotopy=lam,literal_live_identity=identity,
                 independently_reconstructed_baseline_errors=reconstructed,
                 parameter_chain_checks=derivative)
        if not all(identity.values()) or max(reconstructed.values())>1e-13:
            raise AssertionError('Zero-control lambda reconstruction changed the anchor')
        if max(x['max_absolute_two_jet_error'] for x in derivative)>1e-7:
            raise AssertionError('Auxiliary p0/phase-control derivative chain failed')
        if definition['anchor_core_settings']['homotopy']!=.002:
            raise AssertionError('The source anchor metadata was mutated')
        rows.append(row)
    result=dict(synthetic_only=True,accepted_BVP_field=False,
        source_hashes={str(path):hashlib.sha256(path.read_bytes()).hexdigest()
                       for path in (a.reference_source,flat_path,provider_path,Path(__file__))},
        rows=rows,complete_surface=False)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
