#!/usr/bin/env python3
"""Small synthetic API check, never an actual accepted near-1 field."""
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[name]="1"
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value;spec.loader.exec_module(value)
    return value

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo",type=Path,required=True)
parser.add_argument("--reference-source",type=Path,required=True)
parser.add_argument("--out",type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parent
flat_source=args.repo/"topics/visible-flex-held-10pct/scripts/resume_transfer/material_flattened_support_core.py"
old=module("_test_original_support",args.reference_source)
flatten=module("_test_original_flatten",flat_source)
warm=module("_test_warm_supported",root/"warm_supported_core_factory.py")
q=.06;M=8
settings=dict(homotopy=.95,curvature_blend=1.,halfwidth=.5,transition=.2,target_curvature=.2,
              quadrature_order=12,integration_cells=64,transition_cells=24)
original=old.PlanarSupportCore(q,np.zeros(M-1),3)
baseline=flatten.MaterialFlattenedSupportCore(original,**settings)
config=dict(gauge_q=q,phase_control_scale=1.,anchor_support_coefficients=original.coefficients.tolist(),
            anchor_core_settings=settings)
Factory=warm.make_factory(config,reference_class=old.PlanarSupportCore,anchor_baseline=baseline)
legacy=np.maximum(q**np.arange(2,M+1),1e-10)
theta=np.r_[np.linspace(0,2*np.pi,31),np.pi/3+np.array([-.5,-.3,0,.3,.5])]
core=Factory(q,np.zeros(M-1),3)
a,b=baseline.evaluate(theta),core.evaluate(theta)
identity={name:bool(np.array_equal(a[name],b[name])) for name in ("F","Ft","Ftt")}
jets=core.jet_parameter_derivatives(theta)
scales=np.r_[q,legacy]
rows=[]
for j in (0,3,7):
    h=1e-6
    p=np.zeros(M);p[j]=h
    plus=Factory(q*np.exp(p[0]),p[1:]*legacy,3).evaluate(theta)
    minus=Factory(q*np.exp(-p[0]),-p[1:]*legacy,3).evaluate(theta)
    errors=[]
    for k,name in enumerate(("F","Ft","Ftt")):
        derivative=(plus[name]-minus[name])/(2*h)
        errors.append(float(np.max(abs(derivative-jets[k][j]*scales[j]))))
    rows.append(dict(bvp_parameter=j,maximum_absolute_two_jet_errors=errors))
test=Factory(q*np.exp(.001),np.full(M-1,.0001)*legacy,3)
u=np.linspace(np.pi/3-.5,np.pi/3+.5,43)
fixed_arc=float(np.max(abs(test.evaluate(u)["kappa"]-baseline.evaluate(u)["kappa"])))
result=dict(synthetic_test_only=True,source_is_accepted_BVP=False,
    lambda_value=.95,zero_control_literal_identity=identity,parameter_chain_checks=rows,
    parameters=settings,material_samples=len(theta),
    source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
        (args.reference_source,flat_source,root/"warm_supported_core_factory.py",Path(__file__))},
    protected_arc_curvature_change=fixed_arc,complete_surface=False)
if args.out:
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
