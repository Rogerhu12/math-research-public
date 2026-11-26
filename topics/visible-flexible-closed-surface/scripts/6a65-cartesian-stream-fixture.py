#!/usr/bin/env python3
"""Finite checks for the newly restored complete Cartesian stream text.

This is a new numerical fixture identity. It does not reuse prior scratch
receipts, an actual Cauchy source, a complete LM acceptance, or a certificate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("restored_cartesian_stream", HERE/"6a65-cartesian-complete-stream.py")
stream = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = stream
_spec.loader.exec_module(stream)


def source_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(left, right):
    return float(abs(left-right)/max(1., abs(left), abs(right)))


def background(nodes, N):
    s = np.asarray(nodes)[:, None]
    u = 2*np.pi*np.arange(N)[None, :]/N
    r = .80+.05*np.cos(12*s)
    rs, rss = -.60*np.sin(12*s), -7.2*np.cos(12*s)
    co, si = np.cos(u), np.sin(u)
    out = np.zeros((len(nodes), 6, N, 3))
    out[:, 0, 0:, 0], out[:, 0, 0:, 1] = r*co, r*si
    out[:, 0, 0:, 2] = .1+.3*s
    out[:, 1, 0:, 0], out[:, 1, 0:, 1], out[:, 1, 0:, 2] = rs*co, rs*si, .3
    out[:, 2, 0:, 0], out[:, 2, 0:, 1] = -r*si, r*co
    out[:, 3, 0:, 0], out[:, 3, 0:, 1] = rss*co, rss*si
    out[:, 4, 0:, 0], out[:, 4, 0:, 1] = -rs*si, rs*co
    out[:, 5, 0:, 0], out[:, 5, 0:, 1] = -r*co, -r*si
    target = np.broadcast_to(.76+.02*np.cos(3*s), (len(nodes), N))
    return out, target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual fixture output required")
    start = time.monotonic()
    rng = np.random.default_rng(20261126)
    basis = stream.HalfTurnBasis(.1, 1.1, 7, 8)
    N = 64
    angular_errors = []
    for derivative in range(3):
        a = rng.normal(size=(5, basis.na))
        q = rng.normal(size=(5, N, 3))
        angular_errors.append(relative(
            np.sum(basis.angular(a, N, derivative)*q),
            np.sum(a*basis.angular_adjoint(q, derivative))))
    nodes = np.linspace(0., 1.3, 19)
    weights = {k: np.linspace(.1, .3, len(nodes))/len(nodes)*factor
               for k, factor in (("metric", 1.), ("curvature", .003), ("geometry", 2.))}
    coeff = rng.normal(size=(basis.nb, basis.na))*1e-5
    config = stream.point.PointConfig(metric_tau=.05, curvature_tau=1e6,
                                     curvature_guide=9.5, true_cuff_height=.51,
                                     central_a=1.436024268143396)
    before = source_hash(HERE/"6a65-cartesian-complete-stream.py")
    linear = stream.CompleteStreamingLinearized(
        basis, nodes, weights, background, coeff, N, config, block=4,
        cache_point_blocks=True)
    uncached = stream.CompleteStreamingLinearized(
        basis, nodes, weights, background, coeff, N, config, block=4,
        cache_point_blocks=False)
    x, y = rng.normal(size=basis.dimension), rng.normal(size=linear.shape[0])
    left, right = linear.operator.matvec(x)@y, x@linear.operator.rmatvec(y)
    bilinear = relative(left, right)
    cache_matvec = float(np.max(np.abs(linear.operator.matvec(x)-uncached.operator.matvec(x))))
    cache_transpose = float(np.max(np.abs(linear.operator.rmatvec(y)-uncached.operator.rmatvec(y))))
    observed = stream.observe(basis, nodes, weights, background, coeff, N, config, block=4)
    norm_gap = abs(observed["squaredNorm"]-float(linear.residual@linear.residual))
    direction = linear.unpack(x)
    jv = linear.operator.matvec(x)
    fd = []
    for epsilon in (1e-5, 1e-6, 1e-7):
        plus = stream.CompleteStreamingLinearized(
            basis, nodes, weights, background, coeff+epsilon*direction, N, config, block=4).residual
        minus = stream.CompleteStreamingLinearized(
            basis, nodes, weights, background, coeff-epsilon*direction, N, config, block=4).residual
        error = float(np.linalg.norm((plus-minus)/(2*epsilon)-jv)/max(1., np.linalg.norm(jv)))
        fd.append(dict(epsilon=epsilon, relativeError=error))
    real_basis = stream.HalfTurnBasis(.1, 1.1, 80, 32)
    real_coeff = rng.normal(size=(real_basis.nb, real_basis.na))
    endpoint = real_basis.packet(real_basis.matrices(np.array([.1, 1.1])), real_coeff, 128)
    endpoint_error = float(np.max(np.abs(endpoint)))
    packet = real_basis.packet(real_basis.matrices(np.array([.23, .65, .98])), real_coeff, 128)
    parity = packet[:, :, :64]*np.array([-1., -1., 1.])
    parity_error = float(np.max(np.abs(packet[:, :, 64:]-parity)))
    verified = (max(angular_errors) < 2e-12 and bilinear < 2e-12 and
                cache_matvec == 0 and cache_transpose == 0 and
                norm_gap <= 2e-12*max(1., observed["squaredNorm"]) and
                fd[-1]["relativeError"] < 2e-6 and endpoint_error == 0 and parity_error == 0)
    report = dict(
        schema="6a65-restored-complete-Cartesian-stream-finite-fixture-v1",
        restoredSourceIdentity=True, sourceSHA256=before,
        fixtureSHA256=source_hash(__file__),
        pointOperatorSHA256=source_hash(HERE/"6a65-cartesian-complete-point-operator.py"),
        columns=basis.dimension, rows=linear.shape[0], angularAdjointRelativeErrors=angular_errors,
        fullBilinearLeft=float(left), fullBilinearRight=float(right),
        fullBilinearRelativeError=bilinear, cacheMatvecMaximumDifference=cache_matvec,
        cacheTransposeMaximumDifference=cache_transpose, fullValueSquaredNormDifference=norm_gap,
        finiteDifferences=fd, fullRequestedColumns=real_basis.dimension,
        fullRequestedEndpointSixJetMaximum=endpoint_error,
        properHalfTurnSixJetMaximumDifference=parity_error, verified=bool(verified),
        actualCauchySourceConsumed=False, completeLMAcceptances=0,
        continuousCertificate=False, seconds=time.monotonic()-start)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(report, allow_nan=False), flush=True)
    if source_hash(HERE/"6a65-cartesian-complete-stream.py") != before:
        raise ArithmeticError("Fixture changed its source")
    if not verified:
        raise AssertionError("Actual restored-stream finite check failed")


if __name__ == "__main__":
    main()
