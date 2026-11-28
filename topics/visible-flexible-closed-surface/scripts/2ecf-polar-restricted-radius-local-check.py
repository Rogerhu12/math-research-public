#!/usr/bin/env python3
"""Actual small full-row joint XYZ/log-radius derivative and cross-H audit."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    for key in ("scripts", "prepared", "output"):
        ap.add_argument("--"+key, type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    here = Path(__file__).parent
    prepare = module(here/"2ecf-polar-c2-prefix-prepare.py", "log_radius_local_prepare")
    operator = module(here/"2ecf-polar-log-radius-operator.py", "log_radius_local_operator")
    saved, definition, fullbasis, source, mods, *_ = prepare.validate_prepared(args)
    stream = mods["stream"]
    basis = mods["generic"].periodic_basis(stream, fullbasis.c, fullbasis.end, 8, 2)
    deps = operator.dependencies(args.scripts)
    config = stream.point.PointConfig(**definition["pointConfig"])
    recipe = definition["recipe"]
    area = dict(targetAreaRatio=.5, strength=1., reciprocalPower=2)
    indices = np.unique(np.linspace(0,len(source["training"].nodes)-1,33,dtype=int))
    caches,weights = {},{}
    for key in ("training","observer"):
        parent = source[key]
        angles = parent.u[::8]
        if not np.array_equal(angles,2*np.pi*np.arange(len(angles))/len(angles)):
            raise ArithmeticError("Exact inherited physical angle subset required")
        caches[key] = operator.ArrayCache(parent.nodes[indices], angles,
            parent.jets[indices][:,:,::8], parent.radius[indices])
        weights[key] = {name:.5*np.asarray(values)[indices]
            for name,values in saved["caches"][key]["weights"].items()}
    rng = np.random.default_rng(2026112807)
    z = rng.standard_normal((basis.nb,basis.na))*1e-5
    alpha = .017*np.sin(np.arange(basis.nb)+.31)
    locked = 3
    alpha[:locked] = 0
    restriction = module(here/"2ecf-polar-restricted-radius-operator.py", "restricted_operator")
    def build(z,alpha):
        return restriction.RestrictedLinear(operator.FullDesignLinear(deps,stream,basis,caches,weights,z,alpha,config,recipe,area),locked)
    linear = build(z,alpha)
    FD=[]
    for kind in ("XYZ","radius","joint"):
        dz = rng.standard_normal(z.shape) if kind != "radius" else np.zeros_like(z)
        da = rng.standard_normal(alpha.shape) if kind != "XYZ" else np.zeros_like(alpha)
        direction=linear.pack(dz,da)
        direction/=np.linalg.norm(direction)
        dz,da=linear.split(direction)
        image=linear.matvec(direction)
        cot=rng.standard_normal(linear.shape[0])
        lhs=float(image@cot);rhs=float(direction@linear.transpose(cot))
        adjoint=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
        differences=[]
        for step in (1e-6,1e-7,1e-8):
            plus=build(z+step*dz,alpha+step*da).residual
            minus=build(z-step*dz,alpha-step*da).residual
            error=float(np.linalg.norm((plus-minus)/(2*step)-image)/max(1.,np.linalg.norm(image)))
            differences.append(dict(epsilon=step,relativeL2=error))
        row=dict(kind=kind,actualActionNorm=float(np.linalg.norm(image)),
            adjointRelativeError=adjoint,finiteDifferences=differences)
        FD.append(row);print(json.dumps(dict(event="actual_joint_direction_check",**row)),flush=True)
        if (np.linalg.norm(image)==0 or adjoint>2e-11
                or min(row["relativeL2"] for row in differences)>2e-5):
            raise ArithmeticError("The actual nonzero joint derivative check failed")
    dimension=linear.shape[1]
    identity=np.eye(dimension)
    J=np.column_stack([linear.matvec(row) for row in identity])
    S=np.column_stack([linear.sobolev_apply(row) for row in identity])
    damping=.003
    factor=restriction.RestrictedNormal(operator,linear,damping)
    dense=np.zeros((dimension,dimension))
    for offset in range(factor.half_bandwidth+1):
        c=np.arange(dimension-offset);r=c+offset
        dense[r,c]=factor.unscaled_band[offset,:len(c)]
        if offset:dense[c,r]=dense[r,c]
    expected=J.T@J+damping*S
    error=float(np.linalg.norm(dense-expected)/np.linalg.norm(expected))
    gradient=linear.transpose(linear.residual)
    direction=-factor.solve(gradient)
    normal_residual=factor.residual(direction)
    relative=float(np.linalg.norm(normal_residual)/np.linalg.norm(gradient))
    direct_error=float(np.linalg.norm(direction-np.linalg.solve(expected,-gradient))/max(1.,np.linalg.norm(direction)))
    cross,gram=linear.cross_normal()
    ix=linear.position_indices;ia=linear.radius_indices
    cross_error=float(np.linalg.norm(cross-J[:,ix].T@J[:,ia])/max(1.,np.linalg.norm(cross)))
    radius_error=float(np.linalg.norm(gram-J[:,ia].T@J[:,ia])/max(1.,np.linalg.norm(gram)))
    alpha_active=sum(int(np.count_nonzero(pair[1])) for values in linear.full.radius_packets.values() for pair in values)
    if max(error,cross_error,radius_error)>5e-12 or relative>1e-9 or direct_error>1e-8 or alpha_active==0:
        raise ArithmeticError("Complete physical cross-H or active area derivative audit failed")
    out=dict(schema="2ecf-actual-small-restricted-Cartesian-log-radius-J-JT-H-audit-v1",
        preparedSHA256=sha(args.prepared),sourceIdentity=definition["sourceIdentity"],
        operatorEntrySHA256=sha(here/"2ecf-polar-log-radius-operator.py"),entrySHA256=sha(__file__),
        inputDefinition=dict(basis=basis.definition,physicalNodes=caches["training"].nodes.tolist(),
            angles={k:v.u.tolist() for k,v in caches.items()},
            weights={k:{n:v.tolist() for n,v in w.items()} for k,w in weights.items()},
            z=z.tolist(),alpha=alpha.tolist(),area=area,pointConfig=definition["pointConfig"]),
        actualRows=linear.shape[0],actualColumns=dimension,
        actualCartesianColumns=basis.dimension,actualLogRadiusColumns=basis.nb-locked,lockedPrefix=locked,restrictionSHA256=sha(here/"2ecf-polar-restricted-radius-operator.py"),
        allFourteenRowsAtEveryActualFixturePoint=True,
        alphaIsNonzero=True,activeAreaRadiusDerivativePoints=alpha_active,
        directionChecks=FD,fullNormalRelativeDifference=error,
        CartesianRadiusCrossBlockRelativeDifference=cross_error,radiusBlockRelativeDifference=radius_error,
        actualPhysicalNormalRelativeResidual=relative,denseSolveRelativeDifference=direct_error,
        fullNormalAssembly=factor.receipt,metricQuarticDerivativeIncluded=True,
        backgroundPositionIndependentOfAlpha=True,allWeightsNodesAndPointGuidesIndependentOfAlpha=True,
        declaredMetricDesignNotSameMetricContinuation=True,
        original12789ProductionSolvePerformed=False,nonlinearAcceptsPerformed=0,
        seconds=time.monotonic()-start)
    if args.output.exists():raise FileExistsError("Fresh actual check output required")
    args.output.write_text(json.dumps(out,separators=(",",":"),allow_nan=False)+"\n")
    print(json.dumps(dict(event="actual_joint_full_normal_audit_complete",SHA256=sha(args.output),
        rows=out["actualRows"],columns=dimension,normalDifference=error,crossDifference=cross_error,
        physicalNormalResidual=relative,seconds=out["seconds"])),flush=True)


if __name__ == "__main__":main()
