#!/usr/bin/env python3
"""Complete fixed-g Cartesian point value/JVP/JT.

The last two jet axes are (X, Xs, Xu, Xss, Xsu, Xuu), Cartesian component.
Leading axes are arbitrary point batches. All 3 metric, 3 curvature and
7 R219 geometry rows are retained. Weights already include every external
radial/angular/guide factor. This module makes no source evaluation,
surface-solve, reach, or continuum-certificate claim.

R191's exact-threshold convention is preserved: the inactive slope is zero.
The spectral 3x3 Jacobian is local; no parameter-by-parameter Jacobian or
normal matrix is formed. Input jet arrays are borrowed read-only for the
lifetime of PointLinearized.
"""
from dataclasses import dataclass
import hashlib
import json
import re
import numpy as np

SCHEMA = "6a65-complete-fixed-g-Cartesian-point-operator-v1"
JET_ORDER = ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu")
GEOMETRY_ROWS = (
    "ball", "width_plus", "width_minus", "height_plus", "height_minus",
    "held_plus", "held_minus",
)
SQ2 = np.sqrt(2.0)


def bind_source_metadata(metadata, expected):
    """Bind an actual oracle receipt; a schema label alone is insufficient.

The caller must obtain metadata from the live oracle and independently
compute the expected file hashes in the same runner. This validates that
receipt, not the mathematical correctness of an arbitrary JSON document.
    """
    if metadata.get("schema") != "6a65-frozen-actual-Cauchy-core-and-true-R205-tail-source-v1":
        raise ValueError("Actual complete Cauchy oracle metadata required")
    if (metadata.get("interfaceProbeOnly") is not False or
            metadata.get("sourceIdentityKind") != "actual-Cauchy-checkpoint" or
            metadata.get("sourceHasNoClaimedBaselineOrAcceptance") is not False):
        raise ValueError("An interface probe cannot initialize an actual source solve")
    if metadata.get("sourceCheckpointSchema") not in (
            "6a65-Cauchy-global-position-initial-v1",
            "6a65-Cauchy-global-position-checkpoint-v1"):
        raise ValueError("Own actual Cauchy checkpoint schema required")
    hash_keys = (
        "sourceStateSHA256", "candidateSHA256", "parameterVectorSHA256",
        "sourceFileSHA256", "providerEntrySHA256", "positionSourceSHA256",
        "baseSourceSHA256", "tailSourceSHA256",
    )
    for key in hash_keys:
        value = metadata.get(key)
        if not isinstance(value, str) or not re.fullmatch("[0-9a-f]{64}", value):
            raise ValueError("Missing actual source hash: " + key)
        if value != expected.get(key):
            raise ValueError("Actual source identity mismatch: " + key)
    for key in ("completeCoefficientsFrozen", "amplitudeAndCuffHeightUnchanged",
                "sourceAngularPrimitiveUnchanged", "sourceMetricUnchanged"):
        if metadata.get(key) is not True:
            raise ValueError("Missing unchanged-source receipt: " + key)
    if metadata.get("FourierOrHermiteBackgroundProjection") is not False:
        raise ValueError("Projected background is not the actual oracle source")
    count = metadata.get("checkpointDeclaredAcceptedSteps")
    angles = metadata.get("primitiveAngles")
    if type(count) is not int or count < 0:
        raise ValueError("Actual declared accepted count required")
    if type(angles) is not int or angles < 2 or angles % 2:
        raise ValueError("Actual even source primitive angle count required")
    if metadata.get("sourceOptions", {}).get("angles") != angles:
        raise ValueError("Source primitive/options angle mismatch")
    c, end, cuff = (metadata.get(k) for k in ("c", "S", "cuff"))
    if not all(isinstance(v, (int, float)) and np.isfinite(v) for v in (c, end, cuff)):
        raise ValueError("Finite actual physical domain required")
    if not (0 < c < end and cuff == end + .48):
        raise ValueError("Actual domain must extend through the true r=.32 cuff")
    for key in ("amplitude", "Z", "centralA", "centralB", "centralGap"):
        if not isinstance(metadata.get(key), (int, float)) or not np.isfinite(metadata[key]):
            raise ValueError("Finite actual source geometry required: " + key)
    if metadata["centralA"] < 1.4 or not (.41 <= metadata["Z"] <= .52):
        raise ValueError("Actual source does not belong to the declared R219 guide")
    if type(expected.get("runId")) is not int or expected["runId"] < 1:
        raise ValueError("Actual same-job run ID required")
    if not re.fullmatch("[0-9a-f]{64}", expected.get("observerSHA256", "")):
        raise ValueError("Actual matching observer hash required")
    if not re.fullmatch("[0-9a-f]{40}", expected.get("sourceEpoch", "")):
        raise ValueError("Explicit loaded source epoch required")
    if not isinstance(metadata.get("radialMetricDefinition"), dict):
        raise ValueError("Complete radial metric definition required")
    fixed = {
        "schema": "6a65-Cartesian-frozen-actual-source-and-g-v1",
        **{key: metadata[key] for key in hash_keys},
        "runId": expected["runId"], "sourceEpoch": expected["sourceEpoch"],
        "observerSHA256": expected["observerSHA256"],
        "sourceCheckpointSchema": metadata["sourceCheckpointSchema"],
        "sourceAcceptedSteps": count, "sourcePrimitiveAngles": angles,
        "c": c, "S": end, "cuff": cuff,
        "amplitude": metadata["amplitude"], "Z": metadata["Z"],
        "centralA": metadata["centralA"],
        "radialMetricDefinition": metadata["radialMetricDefinition"],
        "targetMetric": "ds^2+a_star(s)^2 du^2; actual complete source rho is frozen",
        "correctionDomain": [c, end],
        "completeHalfDomain": [0, cuff],
        "fixedSourceAndMetric": True, "continuumCertificate": False,
    }
    encoded = json.dumps(fixed, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=True, allow_nan=False).encode()
    fixed["identitySHA256"] = hashlib.sha256(encoded).hexdigest()
    return fixed


@dataclass(frozen=True)
class PointConfig:
    metric_tau: float
    curvature_tau: float
    curvature_guide: float
    true_cuff_height: float
    central_a: float
    radius: float = 1.59
    width: float = .885
    held: float = .65
    height_maximum: float = .0195
    height_radial_start: float = .52
    height_radial_end: float = .54

    def __post_init__(self):
        values = tuple(self.__dict__.values())
        if not all(np.isfinite(v) for v in values):
            raise ValueError("Finite explicit point parameters required")
        if not (self.metric_tau > 0 and self.curvature_tau > 0 and
                self.curvature_guide > 0 and self.central_a >= 1.4):
            raise ValueError("Positive taus/guide and R219 central support required")
        if not (.41 <= self.true_cuff_height <= .52):
            raise ValueError("Actual fixed R219 cuff height outside its guide")
        if (self.radius, self.width, self.held) != (1.59, .885, .65):
            raise ValueError("This operator retains the actual R219 guide")
        if (self.height_maximum, self.height_radial_start,
                self.height_radial_end) != (.0195, .52, .54):
            raise ValueError("This operator retains the actual R219 height allowance")
        if not all(np.isfinite(t*t) and t*t > 0 for t in
                   (self.metric_tau, self.curvature_tau)):
            raise ValueError("Finite positive squared taus required")


def dot(a, b):
    return np.sum(a*b, axis=-1)


def validate_jets(jets):
    jets = np.asarray(jets, dtype=np.float64)
    if jets.ndim < 2 or jets.shape[-2:] != (6, 3) or not np.all(np.isfinite(jets)):
        raise ValueError("Finite full Cartesian six-jets required")
    return jets


def curvature_cache(jets):
    U, V, B, C, D = (jets[..., k, :] for k in range(1, 6))
    W = np.cross(U, V)
    w2, E, F, G = dot(W, W), dot(U, U), dot(U, V), dot(V, V)
    if not (np.all(E > 0) and np.all(w2 > 0)):
        raise ValueError("Actual Cartesian position is not immersed")
    w = np.sqrt(w2)
    n = W/w[..., None]
    L, M, NN = dot(n, B), dot(n, C), dot(n, D)
    r, P = F/E, w2/E
    S = np.stack((L/E, (M-r*L)/w, (NN-2*r*M+r*r*L)/P), axis=-1)
    if not np.all(np.isfinite(S)):
        raise ValueError("Nonfinite actual second form")
    mid, delta = (S[..., 0]+S[..., 2])/2, (S[..., 0]-S[..., 2])/2
    spread = np.hypot(delta, S[..., 1])
    eigenvalues = np.stack((mid+spread, mid-spread), axis=-1)
    return dict(E=E, F=F, G=G, W=W, w2=w2, w=w, n=n,
                L=L, M=M, NN=NN, r=r, P=P, S=S, eigenvalues=eigenvalues)


def curvature_jvp(jets, cache, variation):
    U, V, B, C, D = (jets[..., k, :] for k in range(1, 6))
    dU, dV, dB, dC, dD = (variation[..., k, :] for k in range(1, 6))
    E, w, n, r, P = (cache[k] for k in ("E", "w", "n", "r", "P"))
    L, M, S = (cache[k] for k in ("L", "M", "S"))
    dW = np.cross(dU, V)+np.cross(U, dV)
    dw = dot(n, dW)
    dn = (dW-n*dw[..., None])/w[..., None]
    dE, dF = 2*dot(U, dU), dot(dU, V)+dot(U, dV)
    dL, dM, dNN = dot(dn, B)+dot(n, dB), dot(dn, C)+dot(n, dC), dot(dn, D)+dot(n, dD)
    dr, dP = (dF-r*dE)/E, P*(2*dw/w-dE/E)
    dA = (dL-S[..., 0]*dE)/E
    dBshape = (dM-dr*L-r*dL-S[..., 1]*dw)/w
    numerator = dNN-2*dr*M-2*r*dM+2*r*dr*L+r*r*dL
    dCshape = (numerator-S[..., 2]*dP)/P
    return np.stack((dA, dBshape, dCshape), axis=-1)


def curvature_vjp(jets, cache, cotangent):
    U, V, B, C, D = (jets[..., k, :] for k in range(1, 6))
    E, w, n, r, P, L, M, S = (
        cache[k] for k in ("E", "w", "n", "r", "P", "L", "M", "S"))
    alpha, beta, gamma = (cotangent[..., k] for k in range(3))
    barL = alpha/E-beta*r/w+gamma*r*r/P
    barM, barN = beta/w-2*gamma*r/P, gamma/P
    barr = -beta*L/w+gamma*(-2*M+2*r*L)/P
    barP, barw, barE = -gamma*S[..., 2]/P, -beta*S[..., 1]/w, -alpha*S[..., 0]/E
    barF = barr/E
    barE = barE-barr*r/E-P*barP/E
    barw = barw+2*w*barP/E
    barn = barL[..., None]*B+barM[..., None]*C+barN[..., None]*D
    barW = (barn-n*dot(n, barn)[..., None])/w[..., None]+barw[..., None]*n
    out = np.zeros_like(jets)
    out[..., 1, :] = 2*barE[..., None]*U+barF[..., None]*V+np.cross(V, barW)
    out[..., 2, :] = barF[..., None]*U+np.cross(barW, U)
    out[..., 3, :] = barL[..., None]*n
    out[..., 4, :] = barM[..., None]*n
    out[..., 5, :] = barN[..., None]*n
    return out


def spectral_hinge(S, guide, tau):
    """R191 plus explicit positive-tau amplification, all spectral branches."""
    A, B, C = (S[..., k] for k in range(3))
    h, d = (A+C)/2, (A-C)/2
    radius = np.hypot(d, B)
    lp, lm = h+radius, h-radius
    fp = np.where(lp > guide, lp-guide, np.where(lp < -guide, lp+guide, 0.0))
    fm = np.where(lm > guide, lm-guide, np.where(lm < -guide, lm+guide, 0.0))
    sp, sm = (np.abs(lp) > guide).astype(float), (np.abs(lm) > guide).astype(float)
    same = ((sp == sm) & (((lp > guide) & (lm > guide)) |
            ((lp < -guide) & (lm < -guide)) |
            ((lp >= -guide) & (lp <= guide) & (lm >= -guide) & (lm <= guide))))
    general = ~same
    if np.any(general & (radius <= 0)):
        raise ValueError("Unexpected R191 repeated-eigenvalue branch")
    safe = np.where(general, radius, 1.0)
    alpha, u, v, mean = (fp-fm)/(2*safe), d/safe, B/safe, (fp+fm)/2
    offset = np.where(sp != 0, np.where(lp > guide, -guide, guide), 0.0)
    Qsame = np.stack((sp*A+offset, sp*B, sp*C+offset), axis=-1)
    Qother = np.stack((mean+alpha*d, alpha*B, mean-alpha*d), axis=-1)
    Q = np.where(same[..., None], Qsame, Qother)
    residual0 = Q*np.array((1.0, SQ2, 1.0))
    jac0 = np.empty(S.shape[:-1]+(3, 3))
    for k in range(3):
        H = np.eye(3)[k]
        dh, dd = (H[0]+H[2])/2, (H[0]-H[2])/2
        hp, hm = dh+u*dd+v*H[1], dh-u*dd-v*H[1]
        xp, xm = (sp-alpha)*hp, (sm-alpha)*hm
        column = np.stack((
            alpha*H[0]+xp*(1+u)/2+xm*(1-u)/2,
            SQ2*(alpha*H[1]+(xp-xm)*v/2),
            alpha*H[2]+xp*(1-u)/2+xm*(1+u)/2,
        ), axis=-1)
        simple = sp[..., None]*(np.array((1.0, SQ2, 1.0))*H)
        jac0[..., :, k] = np.where(same[..., None], simple, column)
    q, tau2 = dot(residual0, residual0), tau*tau
    amplification = np.sqrt(1+q/tau2)
    projection = np.einsum("...i,...ij->...j", residual0, jac0)/(tau2*amplification)[..., None]
    jacobian = amplification[..., None, None]*jac0+residual0[..., :, None]*projection[..., None, :]
    residual = amplification[..., None]*residual0
    if not np.all(np.isfinite(residual)) or not np.all(np.isfinite(jacobian)):
        raise ValueError("Nonfinite amplified curvature residual/derivative")
    return dict(residual=residual, jacobian=jacobian, original_residual=residual0,
                squared=q+q*q/tau2, threshold=((lp == guide) | (lp == -guide) |
                (lm == guide) | (lm == -guide)), eigenvalues=np.stack((lp, lm), axis=-1))


def geometry_cache(X, config):
    r = np.sqrt(dot(X, X))
    plus = X-np.array((0.0, config.central_a, 0.0))
    minus = X+np.array((0.0, config.central_a, 0.0))
    rp, rm = np.sqrt(dot(plus, plus)), np.sqrt(dot(minus, minus))
    if not (np.all(r > 0) and np.all(rp > 0) and np.all(rm > 0)):
        raise ValueError("R219 geometric distance differential domain")
    cylindrical = np.hypot(X[..., 0], X[..., 1])
    length = config.height_radial_end-config.height_radial_start
    t = np.clip((cylindrical-config.height_radial_start)/length, 0, 1)
    allowance = config.height_maximum*t*t*t*(10+t*(-15+6*t))
    derivative = config.height_maximum*30*t*t*(1-t)*(1-t)/length
    allowance = np.where(cylindrical <= config.height_radial_start, 0.0,
                np.where(cylindrical >= config.height_radial_end, config.height_maximum, allowance))
    derivative = np.where((cylindrical > config.height_radial_start) &
                          (cylindrical < config.height_radial_end), derivative, 0.0)
    grad_allowance = np.zeros_like(X)
    radial_scale = np.divide(derivative, cylindrical, out=np.zeros_like(cylindrical),
                             where=derivative != 0)
    grad_allowance[..., :2] = X[..., :2]*radial_scale[..., None]
    signed = np.stack((
        r-config.radius, X[..., 1]-config.width, -X[..., 1]-config.width,
        X[..., 2]-config.true_cuff_height-allowance,
        -X[..., 2]-config.true_cuff_height-allowance, config.held-rp, config.held-rm,
    ), axis=-1)
    grad = np.empty(X.shape[:-1]+(7, 3))
    grad[..., 0, :] = X/r[..., None]
    grad[..., 1, :] = (0., 1., 0.)
    grad[..., 2, :] = (0., -1., 0.)
    grad[..., 3, :] = np.array((0., 0., 1.))-grad_allowance
    grad[..., 4, :] = np.array((0., 0., -1.))-grad_allowance
    grad[..., 5, :] = -plus/rp[..., None]
    grad[..., 6, :] = -minus/rm[..., None]
    grad *= (signed > 0)[..., None]
    return dict(signed=signed, residual=np.maximum(signed, 0), jacobian=grad,
                radius=r, cylindrical_radius=cylindrical, allowance=allowance,
                held_distance=np.minimum(rp, rm),
                adjusted_height_excess=np.abs(X[..., 2])-config.true_cuff_height-allowance)


class PointLinearized:
    """All thirteen point rows, with complete Cartesian JVP and JT."""
    def __init__(self, jets, target_radius, config, weights):
        self.jets = validate_jets(jets)
        self.config = config
        shape = self.jets.shape[:-2]
        self.a = np.broadcast_to(np.asarray(target_radius, dtype=float), shape)
        if not np.all(np.isfinite(self.a)) or not np.all(self.a > 0):
            raise ValueError("Positive frozen actual target radius required")
        if set(weights) != {"metric", "curvature", "geometry"}:
            raise ValueError("All three explicit external point weights required")
        self.sqrt_weights = {}
        for key, value in weights.items():
            value = np.broadcast_to(np.asarray(value, dtype=float), shape)
            if not np.all(np.isfinite(value)) or not np.all(value >= 0):
                raise ValueError("Finite nonnegative external weights required")
            self.sqrt_weights[key] = np.sqrt(value)
        self.curvature = curvature_cache(self.jets)
        E, F, G = (self.curvature[k] for k in ("E", "F", "G"))
        self.metric = np.stack((E-1, SQ2*F/self.a, G/(self.a*self.a)-1), axis=-1)
        self.metric_h = np.sqrt(1+dot(self.metric, self.metric)/(config.metric_tau**2))
        self.hinge = spectral_hinge(self.curvature["S"], config.curvature_guide, config.curvature_tau)
        self.geometry = geometry_cache(self.jets[..., 0, :], config)
        self.residual = np.concatenate((
            (self.sqrt_weights["metric"]*self.metric_h)[..., None]*self.metric,
            self.sqrt_weights["curvature"][..., None]*self.hinge["residual"],
            self.sqrt_weights["geometry"][..., None]*self.geometry["residual"],
        ), axis=-1)
        if not np.all(np.isfinite(self.residual)):
            raise ValueError("Nonfinite complete point residual")

    def metric_apply(self, direction):
        projection = dot(self.metric, direction)/(self.config.metric_tau**2*self.metric_h)
        return self.metric_h[..., None]*direction+self.metric*projection[..., None]

    def jvp(self, variation):
        variation = validate_jets(variation)
        if variation.shape != self.jets.shape:
            raise ValueError("Complete matching six-jet direction required")
        U, V = self.jets[..., 1, :], self.jets[..., 2, :]
        dU, dV = variation[..., 1, :], variation[..., 2, :]
        dr = np.stack((2*dot(U, dU), SQ2*(dot(dU, V)+dot(U, dV))/self.a,
                       2*dot(V, dV)/(self.a*self.a)), axis=-1)
        metric = self.sqrt_weights["metric"][..., None]*self.metric_apply(dr)
        dS = curvature_jvp(self.jets, self.curvature, variation)
        curvature = self.sqrt_weights["curvature"][..., None]*np.einsum(
            "...ij,...j->...i", self.hinge["jacobian"], dS)
        geometry = self.sqrt_weights["geometry"][..., None]*np.einsum(
            "...ij,...j->...i", self.geometry["jacobian"], variation[..., 0, :])
        out = np.concatenate((metric, curvature, geometry), axis=-1)
        if not np.all(np.isfinite(out)):
            raise ValueError("Nonfinite complete point JVP")
        return out

    def vjp(self, cotangent):
        cotangent = np.asarray(cotangent, dtype=float)
        if cotangent.shape != self.residual.shape or not np.all(np.isfinite(cotangent)):
            raise ValueError("Complete thirteen-row cotangent required")
        U, V = self.jets[..., 1, :], self.jets[..., 2, :]
        t = self.metric_apply(self.sqrt_weights["metric"][..., None]*cotangent[..., :3])
        out = np.zeros_like(self.jets)
        out[..., 1, :] = 2*t[..., 0, None]*U+(SQ2*t[..., 1]/self.a)[..., None]*V
        out[..., 2, :] = (SQ2*t[..., 1]/self.a)[..., None]*U+(2*t[..., 2]/(self.a*self.a))[..., None]*V
        curv = self.sqrt_weights["curvature"][..., None]*cotangent[..., 3:6]
        shape_cotangent = np.einsum("...ij,...i->...j", self.hinge["jacobian"], curv)
        out += curvature_vjp(self.jets, self.curvature, shape_cotangent)
        geom = self.sqrt_weights["geometry"][..., None]*cotangent[..., 6:]
        out[..., 0, :] += np.einsum("...ij,...i->...j", self.geometry["jacobian"], geom)
        if not np.all(np.isfinite(out)):
            raise ValueError("Nonfinite complete point transpose")
        return out

    def statistics(self):
        e, sf, g = (self.metric[..., k] for k in range(3))
        relative = np.abs((e+g)/2)+np.hypot((e-g)/2, sf/SQ2)
        groups = dict(metric=slice(0, 3), curvature=slice(3, 6), geometry=slice(6, 13))
        return {
            "schema": SCHEMA, "pointCount": int(np.prod(self.jets.shape[:-2])),
            "rowCount": int(self.residual.size),
            "squaredNorm": float(np.sum(self.residual*self.residual)),
            "groupSquaredNorm": {k: float(np.sum(self.residual[..., sl]**2)) for k, sl in groups.items()},
            "maxRelativeMetric": float(np.max(relative)),
            "maxCurvature": float(np.max(np.abs(self.curvature["eigenvalues"]))),
            "minImmersion": float(np.min(self.curvature["w2"]/(self.a*self.a))),
            "maxRadius": float(np.max(self.geometry["radius"])),
            "maxAbsoluteY": float(np.max(np.abs(self.jets[..., 0, 1]))),
            "minHeldDistance": float(np.min(self.geometry["held_distance"])),
            "maxAdjustedHeightExcess": float(np.max(self.geometry["adjusted_height_excess"])),
            "geometryMaximumViolations": {name: float(np.max(self.geometry["residual"][..., k]))
                                          for k, name in enumerate(GEOMETRY_ROWS)},
            "curvatureThresholdPoints": int(np.count_nonzero(self.hinge["threshold"])),
            "continuousCertificate": False, "strongTargetComplete": False,
        }
