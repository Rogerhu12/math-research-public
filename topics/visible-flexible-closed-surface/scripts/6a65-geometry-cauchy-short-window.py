#!/usr/bin/env python3
"""Compact C2 replacement of an actual Cauchy field by the new gap prefix.

The source is queried directly at every requested (s,u), without a Fourier
or Hermite projection of the background. Only [b,b+h] is modified; after it
the source is returned directly, including its complete original R205 tail.
"""
from __future__ import annotations
import os
for _thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_key] = "1"
import argparse
from collections import OrderedDict
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class ActualCauchyOracle:
    def __init__(self, source_script, scripts_dir, candidate, checkpoint):
        self.command = ["node", "--expose-gc", "--max-old-space-size=256",
                        str(source_script), "serve", str(scripts_dir), str(candidate), str(checkpoint)]
        self.process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, bufsize=1,
        )
        self.counter = 0
        self.metadata = self.request(method="metadata")["metadata"]
        if self.metadata["sourceStateSHA256"] != sha(checkpoint) or self.metadata["candidateSHA256"] != sha(candidate):
            raise ValueError("Actual source identity mismatch")
        self.maximum_consistency = dict(Xu=0., Xsu=0., Xuu=0., meanPhase=0.)

    def request(self, **message):
        self.counter += 1
        message["id"] = self.counter
        self.process.stdin.write(json.dumps(message, allow_nan=False)+"\n")
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            error = self.process.stderr.read()
            raise RuntimeError("Actual Cauchy oracle terminated: "+error)
        out = json.loads(line)
        if out.get("id") != self.counter or not out.get("ok"):
            raise RuntimeError("Actual Cauchy oracle request failed: "+str(out.get("error", out)))
        return out

    def sample(self, s, u, deep=True):
        out = self.request(method="sample", s=float(s), u=np.asarray(u, float).reshape(-1).tolist(), deep=deep)
        if deep:
            for key, value in out["higherJetConsistency"].items():
                self.maximum_consistency[key] = max(self.maximum_consistency[key], value)
                if value > 2e-8:
                    raise ArithmeticError("Actual checkpoint higher-jet consistency failed: "+key)
        return dict(
            **{key: np.asarray(value, float) for key, value in out["jets"].items()},
            f=float(out["radius"]["a"]), fs=float(out["radius"]["as"]), fss=float(out["radius"]["ass"]),
            segment="preserved_actual_Cauchy_source",
        )

    def close(self):
        if self.process.stdin and not self.process.stdin.closed:
            self.process.stdin.close()
        code = self.process.wait()
        if code:
            raise RuntimeError("Cauchy source process did not exit naturally with zero")
        return code


class ShortWindowMaster:
    def __init__(self, oracle, scripts_dir, ramp_master, coast_master, h=.2):
        self.old = oracle
        self.w = load("short_window_existing_warm", Path(scripts_dir)/"6a65-geometry-cauchy-unit-t-warm.py")
        meta = oracle.metadata
        self.prefix = self.w.WarmMaster(
            ramp_master, coast_master, amplitude=meta["amplitude"], Z=meta["Z"],
            right_length=meta["S"]-(13/128+.06+.02), coast_length=.02,
        )
        self.b = self.prefix.coast_end
        self.h = float(h)
        self.stop = self.b+self.h
        self.cut = float(meta["S"])
        self.cuff = float(meta["cuff"])
        if not 0 < self.h < self.cut-self.b:
            raise ValueError("A genuinely interior positive window is required")
        if abs(self.prefix.c-meta["c"]) > 1e-14 or abs(self.prefix.A-self.prefix.B-1.05) > 1e-13:
            raise ValueError("The explicit new gap1.05 prefix and the same central collar are required")
        if abs(self.prefix.v-.045) > 1e-15 or abs(self.prefix.ramp-.06) > 1e-15:
            raise ValueError("The actual new v=.045/ramp=.06 master is required")
        self.cache = OrderedDict()
        self.ramp_master, self.coast_master = Path(ramp_master), Path(coast_master)

    def correction_ports(self, u):
        u = np.asarray(u, float).reshape(-1)
        key = u.tobytes()
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        target = self.prefix.coast_port(self.prefix.coast, u)
        old = self.old.sample(self.b, u, True)
        pairs = dict(P="X", V="Xs", A="Xss", Pu="Xu", Vu="Xsu", Au="Xssu",
                     Puu="Xuu", Vuu="Xsuu", Auu="Xssuu")
        left = {key: target[key]-old[source] for key, source in pairs.items()}
        left.update(f=0., fs=0., fss=0.)
        right = {key: np.zeros_like(value) if isinstance(value, np.ndarray) else 0.
                 for key, value in left.items()}
        self.cache[key] = (left, right)
        while len(self.cache) > 4:
            self.cache.popitem(last=False)
        return left, right

    def window_raw(self, s, u):
        old = self.old.sample(s, u, True)
        left, right = self.correction_ports(u)
        t = max(0., min(1., (s-self.b)/self.h))
        correction = self.w.connector(t, self.h, left, right)
        for key in ("X", "Xs", "Xss", "Xu", "Xsu", "Xuu", "Xssu", "Xsuu"):
            old[key] = old[key]+correction[key]
        angular_second_ports = np.stack([
            left["Puu"], left["Vuu"], left["Auu"],
            right["Puu"], right["Vuu"], right["Auu"],
        ])
        old["Xssuu"] = old["Xssuu"]+np.einsum(
            "i,ijk->jk", self.w.ports.hermite_weights(t, self.h, 2), angular_second_ports
        )
        old["segment"] = "compact_C2_window"
        return old

    def raw(self, s, u):
        s = float(s)
        if s < 0 or s > self.cuff:
            raise ValueError("Point outside the complete true half-surface")
        if s <= self.b:
            return self.prefix.jet(s, u)
        if s >= self.stop:
            return self.old.sample(s, u, True)
        return self.window_raw(s, u)

    def normalized(self, s, u, quadrature=1024):
        s = float(s)
        u = np.asarray(u, float).reshape(-1)
        if s <= self.b:
            return self.prefix.normalized(s, u, quadrature)
        if s >= self.stop:
            q = self.old.sample(s, u, True)
            q.update(unitT=q["Xu"]/q["f"], mean=np.mean(q["X"], axis=0),
                     normalizationScale=1., materialInverseResidual=0.,
                     exactPieceBypass=True, oldSourceReturnedDirectly=True)
            return q
        ug = 2*np.pi*np.arange(quadrature)/quadrature
        q = self.window_raw(s, ug)
        h = np.linalg.norm(q["Xu"], axis=1)
        if np.min(h) <= 1e-6:
            raise ArithmeticError("Actual window angular curve is not regular")
        hs = np.einsum("ij,ij->i", q["Xu"], q["Xsu"])/h
        hss = (np.sum(q["Xsu"]**2, axis=1)+np.einsum("ij,ij->i", q["Xu"], q["Xssu"]))/h-hs**2/h
        a, a_s, a_ss = float(np.mean(h)), float(np.mean(hs)), float(np.mean(hss))
        wave = np.fft.fftfreq(quadrature, 1/quadrature)
        coeff = np.fft.fft(np.stack((h, hs, hss), axis=1), axis=0)/quadrature
        nz = wave != 0
        weights = coeff[nz]/(1j*wave[nz, None])
        moment = np.asarray([a, a_s, a_ss])
        def primitive(v):
            return (v[:, None]*moment+(np.exp(1j*v[:, None]*wave[nz])-1)@weights).real
        v = u.copy()
        for _ in range(12):
            I = primitive(v)
            raw = self.window_raw(s, v)
            speed = np.linalg.norm(raw["Xu"], axis=1)
            residual = I[:, 0]-u*a
            if np.max(np.abs(residual)) < 5e-13:
                break
            v = np.clip(v-residual/speed, 0, 2*np.pi)
        else:
            raise RuntimeError("Actual short-window arclength inverse did not converge")
        X, S, U, SS, SU, UU = (raw[k] for k in ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu"))
        speed_s = np.einsum("ij,ij->i", U, SU)/speed
        speed_u = np.einsum("ij,ij->i", U, UU)/speed
        vs = (u*a_s-I[:, 1])/speed
        vss = (u*a_ss-I[:, 2]-2*speed_s*vs-speed_u*vs**2)/speed
        vu = a/speed
        vuu = -a*a*speed_u/speed**3
        vsu = (a_s-(speed_s+speed_u*vs)*vu)/speed
        return dict(
            X=X, Xs=S+U*vs[:, None],
            Xss=SS+2*SU*vs[:, None]+UU*vs[:, None]**2+U*vss[:, None],
            Xu=U*vu[:, None],
            Xsu=(SU+UU*vs[:, None])*vu[:, None]+U*vsu[:, None],
            Xuu=UU*vu[:, None]**2+U*vuu[:, None],
            f=a, fs=a_s, fss=a_ss, unitT=U/speed[:, None],
            mean=np.mean(q["X"]*h[:, None], axis=0)/a,
            normalizationScale=1., materialInverseResidual=float(np.max(abs(residual))),
            segment="compact_window_natural_perimeter_metric", exactPieceBypass=False,
        )

    def target_config(self, old_checkpoint):
        keys = ("options", "cauchyDesign", "curvatureOptions", "geometryOptions", "metricTau",
                "curvatureTau", "nextLambda", "curvatureModel", "baseModel", "runtimeOptions")
        out = {key: copy.deepcopy(old_checkpoint[key]) for key in keys if key in old_checkpoint}
        out["options"]["gap"] = 1.05
        out["cauchyDesign"].update(
            centralLength=self.prefix.c, rampLength=self.prefix.ramp,
            coastLength=self.prefix.coast, rightLength=self.cut-self.b,
            v=self.prefix.v, amplitude=self.old.metadata["amplitude"], cuffHeight=self.old.metadata["Z"],
        )
        out.update(
            schema="6a65-Cauchy-global-position-initial-v1",
            shortWindowInput=dict(
                b=self.b, h=self.h, stop=self.stop,
                sourceStateSHA256=self.old.metadata["sourceStateSHA256"],
                candidateSHA256=self.old.metadata["candidateSHA256"],
                oracleSourceSHA256=self.old.metadata["sourceFileSHA256"],
                rampMasterSHA256=sha(self.ramp_master), coastMasterSHA256=sha(self.coast_master),
                sourceAmplitudeAndCuffHeightPreserved=True,
                completeSourceReturnedAfterWindow=True, noNewPhysicalClock=True,
                naturalPerimeterIsNewMetric=True, completeRhoFitRequired=True,
                sourceWasInterfaceProbeOnly=self.old.metadata["interfaceProbeOnly"],
            ),
            newProviderValueBaselinesComputed=0, actualAcceptedSteps=0,
            continuousCertificate=False, strongTargetComplete=False,
        )
        return out


def difference(a, b):
    return {key: float(np.max(np.linalg.norm(a[key]-b[key], axis=1)))
            for key in ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["probe", "export"])
    ap.add_argument("--scripts-dir", type=Path, required=True)
    ap.add_argument("--source-script", type=Path, default=Path(__file__).with_name("6a65-geometry-cauchy-source-radial-cuts.cjs"))
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--ramp-master", type=Path, required=True)
    ap.add_argument("--coast-master", type=Path, required=True)
    ap.add_argument("--window", type=float, default=.2)
    ap.add_argument("--angles", type=int, default=128)
    ap.add_argument("--quadrature", type=int, default=1024)
    ap.add_argument("--output-prefix", type=Path, required=True)
    args = ap.parse_args()
    prefix = str(args.output_prefix)
    if Path(prefix+"-report.json").exists() or Path(prefix+"-target-config.json").exists():
        raise FileExistsError("Fresh complete window outputs required")
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    old = ActualCauchyOracle(args.source_script, args.scripts_dir, args.candidate, args.checkpoint)
    try:
        master = ShortWindowMaster(old, args.scripts_dir, args.ramp_master, args.coast_master, args.window)
        config = master.target_config(json.loads(args.checkpoint.read_text()))
        Path(prefix+"-target-config.json").write_text(json.dumps(config, indent=2)+"\n")
        probe_u = np.asarray([.173, .947, 2.197, 3.641, 5.897])
        left = difference(master.window_raw(master.b, probe_u), master.prefix.jet(master.b, probe_u))
        right = difference(master.window_raw(master.stop, probe_u), old.sample(master.stop, probe_u, True))
        late_s = (master.stop+master.cut)/2
        outside = difference(master.normalized(late_s, probe_u), old.sample(late_s, probe_u, True))
        dc = master.correction_ports(probe_u)[0]
        ports = {key: float(np.max(np.linalg.norm(value, axis=1)))
                 for key, value in dc.items() if isinstance(value, np.ndarray)}
        report = dict(
            schema="6a65-direct-actual-Cauchy-source-compact-C2-window-v1", mode=args.mode,
            source=old.metadata, newCentralA=master.prefix.A, newCentralB=master.prefix.B,
            b=master.b, h=master.h, stop=master.stop, physicalCut=master.cut, physicalFlatCuff=master.cuff,
            fullLeftSeamTwoJetDifference=left, fullRightSeamTwoJetDifference=right,
            outsideWindowDirectSourceTwoJetDifference=outside, inletCorrectionPortNorms=ports,
            noNewPhysicalClock=True, sourceReturnedDirectlyAfterWindow=True,
            intendedNewMetric="prefix scalar; window natural perimeter; outside original exact source radius",
            sourceWasInterfaceProbeOnly=old.metadata["interfaceProbeOnly"],
            originalSourceAandZPreserved=True, actualNewProviderValueBaselines=0,
            actualAcceptedSteps=0, continuousCertificate=False, wholeClosedReachCertified=False,
            scriptSHA256=sha(__file__), targetConfigSHA256=sha(prefix+"-target-config.json"),
        )
        if args.mode == "probe":
            s = master.b+.071
            q = master.normalized(s, probe_u, min(args.quadrature, 256))
            report["oneNormalizationProbe"] = dict(
                s=s, quadrature=min(args.quadrature, 256),
                materialInverseResidual=q["materialInverseResidual"],
                maximumAbsGError=float(np.max(abs(np.sum(q["Xu"]**2, axis=1)/q["f"]**2-1))),
                actualTargetRadius=q["f"], actualTargetRadiusFirst=q["fs"], actualTargetRadiusSecond=q["fss"],
                notAWholeFieldBaseline=True,
            )
        else:
            radial = list(old.metadata["radialCuts"])
            sx = np.unique(np.r_[
                np.linspace(0, master.prefix.c, 5), master.prefix.c+master.prefix.sx,
                master.prefix.c+(master.prefix.sx[:-1]+master.prefix.sx[1:])/2,
                master.prefix.ramp_end+np.linspace(0, master.prefix.coast, 5),
                np.linspace(master.b, master.stop, 33), np.linspace(master.stop, master.cut, 49),
                radial, master.cut+np.array([0,.1,.2,.3,.4,.46]), master.cuff,
            ])
            u = 2*np.pi*np.arange(args.angles)/args.angles
            keys = ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu", "f", "fs", "fss", "mean", "unitT")
            saved = {key: [] for key in keys}
            rows = []
            for j, s in enumerate(sx):
                q = master.normalized(float(s), u, args.quadrature)
                diag = master.w.ports.diagnostics(q, master.prefix.A)
                diag["minimumRelativeArea"] = diag["minimumArea"]/q["f"]
                for key in keys:
                    saved[key].append(q[key])
                rows.append(dict(s=float(s), segment=q["segment"], normalized=diag,
                                 inverseResidual=q["materialInverseResidual"]))
                if j % 12 == 0 or j == len(sx)-1:
                    print(json.dumps(dict(event="actual_compact_window_row", index=j, total=len(sx), **rows[-1])), flush=True)
            sample = Path(prefix+"-samples.npz")
            np.savez_compressed(sample, s=sx, u=u, **{key: np.asarray(value) for key, value in saved.items()})
            report.update(
                samples=len(sx), angles=args.angles, quadrature=args.quadrature,
                rows=rows, outputSHA256=sha(sample),
                normalizedExtrema={key: max(row["normalized"][key] for row in rows) for key in (
                    "maximumRelativeMetric", "maximumOwnCurvature", "maximumAbsY", "maximumRadius", "maximumZ"
                )},
            )
            for key in ("minimumHeld", "minimumRelativeArea"):
                report["normalizedExtrema"][key] = min(row["normalized"][key] for row in rows)
        report["oracleMaximumHigherJetConsistency"] = old.maximum_consistency
        report["oracleRequests"] = old.counter
    finally:
        oracle_code = old.close()
    report.update(oracleActualOSExitCode=oracle_code, seconds=time.monotonic()-started,
                  OSExitCode=None, externalExitReceiptRequired=True)
    Path(prefix+"-report.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: value for key, value in report.items() if key not in ("source", "rows")}, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
