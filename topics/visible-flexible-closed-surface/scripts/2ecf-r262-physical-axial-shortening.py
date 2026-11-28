#!/usr/bin/env python3
"""Shorten two actual R262 halves before adding a central band.

The fixed new g is a recorded radial function. The full original spatial
tail undergoes an exact constant translation; its old differential is equal.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[key] = "1"
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline
from scipy.optimize import linprog


def settings(path):
    name = "new_prefix_axial_reduction"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source(a):
    module = settings(a.scripts / "2ecf-r262-small-input-full-xyz-positive-metric-v2.py")
    g = a.work / "h2-c2-m48-g12-04r1"
    a.grid = g / "grid.json"
    a.data = a.work / "m12-prefix-data.npz.gz"
    a.query_report = g / "exact-tail-queries.json"
    a.query_cache = Path(str(a.query_report) + ".npz")
    a.field = g / "result.json.field.npz"
    return module, module.Source(a)


def spline_basis(n):
    knots = np.r_[np.zeros(6), np.arange(1, n)/n, np.ones(6)]
    # Value and first two derivatives of H' vanish at both ends.
    coeff = np.eye(len(knots)-6)[:, 3:-3]
    return BSpline(knots, coeff, 5)


def gather(src, t, angles, shifted):
    u, J, rho = src.prefix(t, angles, shifted)
    return dict(t=t, theta=u, J=J, rho=rho)


def velocities(src, data):
    t, jets = data["t"], data["J"]
    v = jets[:, 1, :, 2]
    h = jets[:, 2, :, 2]/data["rho"]
    return np.mean(v, axis=1), v, h


def choose(src, data, b, mean, reduction, vmax, accel):
    s = src.S
    t = data["t"]
    B = b(t)
    derivative = b(t, 1)/s
    n = B.shape[1]
    mu, v, u = velocities(src, data)
    m = mean(t)
    # Largest absolute normalized entry charge before the new g rescaling.
    # Its norm is bounded above by the absolute diagonal plus the off-diagonal.
    w = 2*np.max(abs(v-m[:, None]), axis=1) + np.max(abs(u), axis=1)
    A = np.vstack((np.c_[w[:, None]*B, -np.ones(len(t))],
                   np.c_[derivative, np.zeros(len(t))],
                   np.c_[-derivative, np.zeros(len(t))]))
    y = np.r_[np.zeros(len(t)), np.full(2*len(t), accel)]
    integral = s*(b.antiderivative()(1)-b.antiderivative()(0))
    out = linprog(np.r_[np.full(n, 1e-10), 1.], A_ub=A, b_ub=y,
                  A_eq=np.r_[integral, 0.][None], b_eq=[reduction],
                  bounds=[(0., vmax)]*n+[(0., None)], method="highs")
    return out.x[:-1] if out.success else None


def observe(module, src, data, b, mean, coeff, maxima=False):
    s = src.S
    t = data["t"]
    ant = b.antiderivative()
    h = s*((ant(t)-ant(0))@coeff)
    v = b(t)@coeff
    acc = b(t, 1)@coeff/s
    J = data["J"].copy()
    J[:,0,:,2] -= h[:,None]
    J[:,1,:,2] -= v[:,None]
    J[:,3,:,2] -= acc[:,None]
    m = mean(t)
    Q = 1-2*v*m+v*v
    if np.min(Q)<=0:
        return {"positive":False}
    residual, err, _ = module.gram(J,Q[:,None],np.ones((len(t),1)),data["rho"])
    k, area = module.curvature(J)
    loc = lambda a: [int(i) for i in np.unravel_index(np.argmax(a),a.shape)]
    i,j = loc(err)
    ik,jk = loc(k)
    report = dict(positive=True, peak=float(err[i,j]), curvature=float(k[ik,jk]),
      metricPeakMaterial=[float(s*t[i]),float(data["theta"][j])],
      curvaturePeakMaterial=[float(s*t[ik]),float(data["theta"][jk])],
      rms=float(np.sqrt(np.mean(residual*residual))),
      minQ=float(Q.min()),minAreaSquared=float(area.min()),
      materialNodes=len(t),angularNodes=len(data["theta"]))
    if maxima:
        nh=np.cross(J[:,1],J[:,2])
        a=np.sqrt(area)
        support=(nh*J[:,0]).sum(-1)/a
        report.update(prefixAbsZ=float(abs(J[:,0,:,2]).max()),
                      prefixMaxRadius=float(np.linalg.norm(J[:,0,:,:2],axis=-1).max()),
                      prefixOriginNorm=float(np.linalg.norm(J[:,0],axis=-1).max()),
                      orientationIndependentSupport=min(abs(float(support.min())),abs(float(support.max())))
                          if np.all(support>0) or np.all(support<0) else 0.)
    return report


def run(a):
    module, src = source(a)
    t = np.linspace(0,1,a.radial+1)
    train = gather(src,t,a.angles,False)
    mu, _, _ = velocities(src,train)
    # This actual stored spline, including its knots, defines the radial target
    # in every independent evaluation, even if the evaluation grid is shifted.
    mean = make_interp_spline(t,mu,k=3)
    b = spline_basis(a.spans)
    rows = []
    for vmax in (.24,.32,.42):
        for accel in (.4,.8,1.6):
            coeff = choose(src,train,b,mean,a.reduction,vmax,accel)
            if coeff is None:
                continue
            obs = observe(module,src,train,b,mean,coeff)
            if obs["positive"]:
                score = obs["peak"]+.015*max(0.,obs["curvature"]-8.5)
                rows.append((score,vmax,accel,coeff,obs))
    if not rows:
        raise ValueError("No positive actual compression satisfied the specified integral")
    rows.sort(key=lambda z: z[0])
    _,vmax,accel,coeff,first = rows[0]
    baseline = observe(module,src,train,b,mean,0*coeff)
    del train
    independent_t = np.unique(np.r_[0.,1.,(np.arange(a.radial+27)+.371)/(a.radial+27)])
    independent = gather(src,independent_t,a.angles+48,True)
    last = observe(module,src,independent,b,mean,coeff,True)
    base_independent = observe(module,src,independent,b,mean,0*coeff,True)
    pos = BSpline(b.t,b.c@coeff,5)
    reduction = src.S*(pos.antiderivative()(1)-pos.antiderivative()(0))
    e = 1-2*max(abs(mean.c))*max(abs(pos.c))
    global_q = float(e-1e-10)
    if global_q<=0:
        raise ValueError("The explicit smooth continuous target requires a tighter positivity enclosure")
    report = dict(schema="physical-R262-both-halves-axial-reduction-real-prefix-v1",
       originalFieldSHA256=src.source_sha,sourceSHA256=sha(__file__),
       sourceDefinition="old physical prefix P, z-H(q); entire tail translated by -H(S); lower reflected",
       metricDefinition="g_new,qq=1-2*v(q)*m(q)+v(q)^2; g_new,qu=0; angular coefficient is old",
       oldCuffAndFullTailDerivativesPreserved=True,peakScope="finite full-prefix observation",
       observedOldTraining=baseline,observedOldIndependent=base_independent,
       observedNewTraining=first,observedNewIndependent=last,
       radialLength=src.S,coefficientUpper=vmax,estimatedAccelerationLimit=accel,
       fullDomainTargetQLower=global_q,actualReduction=float(reduction),
       requestedReduction=a.reduction,physicalVelocitySpline=dict(degree=5,knots=pos.t.tolist(),
       coefficients=pos.c.tolist()),recordedMeanSpline=dict(degree=3,knots=mean.t.tolist(),coefficients=mean.c.tolist()),
       allPhysicalDesigns=[{"velocity":v,"acceleration":a0,"observed":result} for _,v,a0,_,result in rows])
    with a.out.open("x") as f:
        json.dump(report,f,indent=2,allow_nan=False)
        f.write("\n")
    print("ACTUAL_AXIAL_REDUCTION",reduction,"INDEPENDENT",last,flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--scripts",type=Path,required=True)
    p.add_argument("--work",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--reduction",type=float,default=.16)
    p.add_argument("--radial",type=int,default=176)
    p.add_argument("--angles",type=int,default=144)
    p.add_argument("--spans",type=int,default=24)
    run(p.parse_args())
