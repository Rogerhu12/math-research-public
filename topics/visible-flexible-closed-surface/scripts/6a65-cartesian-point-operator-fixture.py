#!/usr/bin/env python3
"""Small reproducible point-chain checks; never a surface or source solve.

Usage: python THIS.py TOPIC_SCRIPTS_DIR FRESH_REPORT_JSON
The original JS R191 and R210 files are called on the same synthetic point
jets. No actual Cauchy coefficients, metric profile or checkpoint is used.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
MODULE = HERE/"6a65-cartesian-complete-point-operator.py"
spec = importlib.util.spec_from_file_location("complete_point_fixture_module", MODULE)
point = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = point
spec.loader.exec_module(point)

REFERENCE = r"""
const fs=require("node:fs"),path=require("node:path");
const input=JSON.parse(fs.readFileSync(0,"utf8")),dir=process.argv[1];
const base=require(path.join(dir,"fd2d-position-curvature-chain-R191.cjs")).createR191Algebra();
const tauFactory=require(path.join(dir,"6a65-explicit-tau-curvature-hinge.cjs")).createExplicitTauCurvatureAlgebra;
const p={dimension:2,base:{height:input.Z,end:1},radialCuts:[0,1],
 definition:{schema:"fd2d-R206-appended-global-parameter-provider-v1",
 positionFamilySchema:"fd2d-R201-R205-variable-amplitude-position-family-v1",
 parentMetric:{fullEquivalentAngles:2,centralA:input.centralA,stateLayout:{cutHeight:0}}},
 slice(){throw Error("The finite point fixture must not evaluate a source slice");}};
const geometry=require(path.join(dir,"fd2d-R210-amplitude-height-allowance-geometric-guide.cjs"))
 .createR210AmplitudeGeometryProvider(p,{radius:1.59,width:.885,held:.65,weight:10,
 nodeShare:.5,cutWindow:[.41,.52],
 heightAllowance:{maximum:.0195,radialStart:.52,radialEnd:.54}});
const out=input.cases.map(q=>{
 const c=base.curvature(q.jets),dS=base.variation(q.jets,c,q.variation);
 const gs=geometry.constraints({jets:q.jets,indices:[1],parameterJets:[q.variation]},[0,0],true);
 return {S:c.S,E:c.E,F:c.F,G:c.G,w2:c.w2,kappa:c.kappa,dS,
   curvature:input.taus.map(tau=>{const h=tauFactory(base,{tau}).hinge(c.S,input.guide);
     return {residual:h.residual,squared:h.squared,jvp:h.apply(dS),
             threshold:h.threshold,jacobianColumns:[[1,0,0],[0,1,0],[0,0,1]].map(e=>h.apply(e))};}),
   geometry:{signed:gs.signed,residual:gs.residual,
     jvp:gs.jacobian.map(row=>row[gs.indices.indexOf(1)])}};
});
process.stdout.write(JSON.stringify({node:process.version,cases:out})+"\n");
"""


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fixture():
    rng = np.random.default_rng(20261126)
    targets = np.array([
        [0, 0, 0], [13, 1, 12], [-13, 1, -12], [14, .5, 0],
        [-14, -.5, 0], [15, 3, -12], [3, 1, 5], [12, 0, 12],
        [-12, 0, -12], [9.5, 0, 9.5], [-9.5, 0, -9.5],
        [9.5, 0, 0], [-9.5, 0, 0], [9.5, 0, 12], [-9.5, 0, -12],
        [0, 10, 0],
    ], dtype=float)
    positions = np.array([
        [1.7, .95, .65], [.02, 1.10, .45], [-.10, -1.10, -.45],
        [.53, 0, .56], [.3, .15, .5], [.01, .01, .001],
        [.1, .885, .20], [.2, .1, .51], [.1, -.885, -.20],
        [1.1, .3, .7], [.4, -.2, -.6], [.53, .01, .52],
        [.3, -.1, -.51], [.03, 1.1, .2], [.03, -1.1, -.2], [.6, .7, .2],
    ], dtype=float)
    jets = np.zeros((16, 6, 3), dtype=float)
    jets[:, 0] = positions
    for k, (a, b, c) in enumerate(targets):
        if 9 <= k <= 14:
            U, V = np.array([1., 0, 0]), np.array([0., 1, 0])
        else:
            U = np.array([1.1+.01*k, .2, -.1])
            V = np.array([.3, .85+.003*k, .17])
        W = np.cross(U, V)
        w = np.linalg.norm(W)
        n, E = W/w, U@U
        r, P = (U@V)/E, w*w/E
        L = a*E
        M = b*w+r*L
        NN = c*P+2*r*M-r*r*L
        jets[k, 1], jets[k, 2] = U, V
        # Nonzero tangential second jets exercise the normal variation.
        jets[k, 3] = L*n+.13*U-.11*V
        jets[k, 4] = M*n-.07*U+.19*V
        jets[k, 5] = NN*n+.05*U+.03*V
    direction = rng.normal(size=jets.shape)*.17
    cotangent = rng.normal(size=(16, 13))
    radius = .73+.013*np.arange(16)
    weights = {
        "metric": .01+.002*np.arange(16),
        "curvature": .0003+.0001*np.arange(16),
        "geometry": .03+.003*np.arange(16),
    }
    return jets, direction, cotangent, radius, weights


def main():
    if len(sys.argv) != 3:
        raise SystemExit("TOPIC_SCRIPTS_DIR FRESH_REPORT_JSON required")
    scripts, report_path = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if report_path.exists():
        raise SystemExit("Fresh report path required")
    begin = time.monotonic()
    jets, direction, cotangent, radius, weights = fixture()
    taus = [2., 1e6]
    config_data = dict(metric_tau=.05, curvature_guide=9.5,
                       true_cuff_height=.51, central_a=1.436024268143396)
    payload = {
        "taus": taus, "guide": config_data["curvature_guide"],
        "Z": config_data["true_cuff_height"], "centralA": config_data["central_a"],
        "cases": [{"jets": {name: j[k].tolist() for k, name in enumerate(point.JET_ORDER)},
                   "variation": {name: d[k].tolist() for k, name in enumerate(point.JET_ORDER)}}
                  for j, d in zip(jets, direction)],
    }
    encoded = json.dumps(payload, separators=(",", ":"), allow_nan=False).encode()
    actual = subprocess.run(["node", "-e", REFERENCE, str(scripts)], input=encoded,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if actual.returncode != 0:
        raise RuntimeError("Original JS point reference failed: "+
                           actual.stderr.decode(errors="replace"))
    reference = json.loads(actual.stdout)
    comparisons = []

    def compare(value, expected, label, tolerance=2e-12):
        value, expected = np.asarray(value), np.asarray(expected)
        if value.shape != expected.shape:
            raise AssertionError(label+" shape mismatch")
        error = np.abs(value-expected)
        relative = error/(1+np.abs(expected))
        record = dict(label=label, scalarCount=int(value.size),
                      maxAbs=float(np.max(error)), maxRelative=float(np.max(relative)))
        comparisons.append(record)
        if not np.all(np.isfinite(relative)) or record["maxRelative"] > tolerance:
            raise AssertionError(json.dumps(record))

    def extract(key):
        return np.array([case[key] for case in reference["cases"]])

    curv = point.curvature_cache(jets)
    for name in ("S", "E", "F", "G", "w2"):
        compare(curv[name], extract(name), "R191 curvature "+name)
    compare(np.max(np.abs(curv["eigenvalues"]), axis=-1), extract("kappa"), "R191 curvature peak")
    compare(point.curvature_jvp(jets, curv, direction), extract("dS"), "R191 five-jet forward variation")
    adjoints, finite_differences, statistics = [], [], []
    for itau, tau in enumerate(taus):
        config = point.PointConfig(curvature_tau=tau, **config_data)
        linear = point.PointLinearized(jets.reshape(2, 8, 6, 3), radius.reshape(2, 8), config,
                        {key: value.reshape(2, 8) for key, value in weights.items()})
        djets, rows = direction.reshape(2, 8, 6, 3), cotangent.reshape(2, 8, 13)
        hinge = point.spectral_hinge(curv["S"], config.curvature_guide, tau)
        cases = [case["curvature"][itau] for case in reference["cases"]]
        for key in ("residual", "squared"):
            compare(hinge[key], np.array([case[key] for case in cases]), f"tau={tau} original amplified {key}")
        original_jac = np.array([case["jacobianColumns"] for case in cases]).swapaxes(-1, -2)
        compare(hinge["jacobian"], original_jac, f"tau={tau} original local 3x3 derivative")
        if not np.array_equal(hinge["threshold"], np.array([case["threshold"] for case in cases])):
            raise AssertionError("Exact threshold conventions differ")
        dS = point.curvature_jvp(jets, curv, direction)
        compare(np.einsum("...ij,...j->...i", hinge["jacobian"], dS),
                np.array([case["jvp"] for case in cases]), f"tau={tau} original composed curvature JVP")
        geometry = point.geometry_cache(jets[:, 0], config)
        for key in ("signed", "residual"):
            compare(geometry[key], np.array([case["geometry"][key] for case in reference["cases"]]),
                    f"tau={tau} original R210 seven geometry {key}")
        compare(np.einsum("...ij,...j->...i", geometry["jacobian"], direction[:, 0]),
                np.array([case["geometry"]["jvp"] for case in reference["cases"]]),
                f"tau={tau} original R210 seven geometry JVP")
        jv = linear.jvp(djets)
        for name, sl in (("metric", slice(0, 3)), ("curvature", slice(3, 6)),
                         ("geometry", slice(6, 13)), ("all", slice(0, 13))):
            y = np.zeros_like(rows)
            y[..., sl] = rows[..., sl]
            jt = linear.vjp(y)
            left, right = float(np.sum(jv*y)), float(np.sum(djets*jt))
            defect = abs(left-right)/(1+abs(left)+abs(right))
            adjoints.append(dict(tau=tau, group=name, left=left, right=right, relativeDefect=defect))
            if defect > 3e-14:
                raise AssertionError("Full bilinear adjoint identity failed")
        # Pointwise identities prevent cancellation between unrelated points.
        jt = linear.vjp(rows)
        left = np.sum(jv*rows, axis=-1)
        right = np.sum(djets*jt, axis=(-2, -1))
        pointwise = np.abs(left-right)/(1+np.abs(left)+np.abs(right))
        if np.max(pointwise) > 3e-14:
            raise AssertionError("Pointwise complete adjoint identity failed")
        adjoints.append(dict(tau=tau, group="all-pointwise",
                             relativeDefect=float(np.max(pointwise))))
        # Nonlinear finite differences are restricted to smooth active branches.
        eig = curv["eigenvalues"]
        smooth = ((np.min(np.abs(np.abs(eig)-config.curvature_guide), axis=-1) > 1e-5) &
                  (np.min(np.abs(geometry["signed"]), axis=-1) > 1e-5))
        for eps in (1e-5, 1e-6, 1e-7):
            plus = point.PointLinearized(jets+eps*direction, radius, config, weights).residual
            minus = point.PointLinearized(jets-eps*direction, radius, config, weights).residual
            fd = (plus-minus)/(2*eps)
            exact = jv.reshape(16, 13)
            error = np.abs(fd[smooth]-exact[smooth])
            relative = error/(1+np.abs(exact[smooth]))
            finite_differences.append(dict(tau=tau, step=eps, smoothPoints=int(np.count_nonzero(smooth)),
                                           maxAbs=float(np.max(error)), maxRelative=float(np.max(relative))))
        if min(row["maxRelative"] for row in finite_differences if row["tau"] == tau) > 1e-7:
            raise AssertionError("Complete nonlinear finite difference failed")
        # Scalar point and multidimensional batch must implement the same map.
        scalar = point.PointLinearized(jets[0], radius[0], config, {k: v[0] for k, v in weights.items()})
        compare(scalar.residual, linear.residual[0, 0], f"tau={tau} scalar/batch residual", 0)
        compare(scalar.jvp(direction[0]), jv[0, 0], f"tau={tau} scalar/batch JVP", 0)
        statistics.append(dict(tau=tau, **linear.statistics()))
    # The interface-only source is never accepted as an actual checkpoint.
    refused = False
    try:
        point.bind_source_metadata({
            "schema": "6a65-frozen-actual-Cauchy-core-and-true-R205-tail-source-v1",
            "interfaceProbeOnly": True,
            "sourceIdentityKind": "explicit-new-zero-free-coefficient-interface-probe",
        }, {})
    except ValueError as error:
        refused = "interface probe" in str(error)
    if not refused:
        raise AssertionError("Interface-only source rejection missing")
    result = {
        "schema": "6a65-complete-Cartesian-point-chain-small-fixture-v1",
        "moduleSHA256": sha(MODULE), "fixtureSHA256": sha(__file__),
        "referenceSHA256": {name: sha(scripts/name) for name in (
            "fd2d-position-curvature-chain-R191.cjs",
            "6a65-explicit-tau-curvature-hinge.cjs",
            "fd2d-R210-amplitude-height-allowance-geometric-guide.cjs")},
        "generatedPointInputSHA256": hashlib.sha256(encoded).hexdigest(),
        "originalNodeReferenceStdoutSHA256": hashlib.sha256(actual.stdout).hexdigest(),
        "originalNodeReferenceOSExitCode": actual.returncode,
        "node": reference["node"], "numpy": np.__version__,
        "syntheticPointCount": 16, "completeRowsPerPoint": 13,
        "metricIncludesG": True, "allFiveCurvatureJetDirections": True,
        "allSevenR219GeometryRows": True, "actualSourceEvaluated": False,
        "fullSurfaceSolvePerformed": False, "acceptedSurfaceSteps": 0,
        "continuumCertificate": False, "strongTargetComplete": False,
        "sourceInterfaceProbeRefused": refused,
        "comparisons": comparisons, "adjointIdentities": adjoints,
        "finiteDifferencesAwayFromThresholds": finite_differences,
        "finiteFixtureStatistics": statistics,
        "seconds": time.monotonic()-begin, "OSExitCode": None,
        "externalExitReceiptRequired": True,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"event": "complete-point-fixture-passed", "reportSHA256": sha(report_path),
        "pointCount": 16, "scalarComparisons": sum(c["scalarCount"] for c in comparisons),
        "maxReferenceRelative": max(c["maxRelative"] for c in comparisons),
        "maxAdjointRelative": max(c["relativeDefect"] for c in adjoints),
        "seconds": result["seconds"], "actualSourceEvaluated": False}))


if __name__ == "__main__":
    main()
