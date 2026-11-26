#!/usr/bin/env python3
"""Read-only streaming background from the frozen actual Cauchy oracle.

The complete source is queried at the requested physical points. No Fourier,
Hermite, radial, or angular projection is made. Default construction rejects
the deliberately separate interface-probe states.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import time
import numpy as np


JET_ORDER = ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu")
METADATA_SCHEMA = "6a65-frozen-actual-Cauchy-core-and-true-R205-tail-source-v1"


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _array_sha(array):
    return hashlib.sha256(np.asarray(array, dtype="<f8").tobytes(order="C")).hexdigest()


class OracleBackground:
    """Persistent actual source and full physical radius, with immutable blocks.

    sample(s,u) returns jets[ns,6,nu,3], point_jets[ns,nu,6,3],
    radius[ns,3]=(a,as,ass), and bb[ns,nu]=a. The two jet layouts
    are views of the same array; neither is a new position representation.
    """

    def __init__(self, scripts_dir, candidate, checkpoint, *,
                 wrapper=None, node="node", expected_hashes=None,
                 allow_interface_probe=False, heap_mb=256):
        self.scripts_dir = Path(scripts_dir).resolve()
        self.candidate = Path(candidate).resolve()
        self.checkpoint = Path(checkpoint).resolve()
        self.wrapper = (Path(wrapper) if wrapper else Path(__file__).with_name(
            "6a65-geometry-cauchy-source-radial-cuts.cjs")).resolve()
        self.source_file = self.wrapper.with_name("6a65-geometry-cauchy-tail-source.cjs")
        if type(heap_mb) is not int or heap_mb < 64:
            raise ValueError("Explicit Node heap limit >= 64 MiB required")
        saved = json.loads(self.checkpoint.read_text())
        if saved.get("baseModel") != "short-cauchy-v1":
            raise ValueError("This adapter binds the declared actual short-Cauchy source")
        if not isinstance(saved.get("z"), list) or not saved["z"]:
            raise ValueError("Complete explicit actual checkpoint z required")
        # ECMAScript JSON.stringify is part of the original vector hash.
        # This child reads only input.z, and never instantiates a provider.
        vector_digest = subprocess.run(
            [node, "-e", "const fs=require('node:fs'),c=require('node:crypto');"
             "const q=JSON.parse(fs.readFileSync(process.argv[1]));"
             "if(!Array.isArray(q.z)||q.z.some(x=>!Number.isFinite(x)))throw Error('finite z required');"
             "process.stdout.write(c.createHash('sha256').update(JSON.stringify(q.z)).digest('hex'));",
             str(self.checkpoint)], capture_output=True, text=True, check=True,
        ).stdout
        files = {
            "sourceStateSHA256": self.checkpoint,
            "candidateSHA256": self.candidate,
            "sourceFileSHA256": self.source_file,
            "sourceMetadataAdapterSHA256": self.wrapper,
            "providerEntrySHA256": self.scripts_dir/"6a65-cauchy-global-position.cjs",
            "positionSourceSHA256": self.scripts_dir/"fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs",
            "baseSourceSHA256": self.scripts_dir/"6a65-geometry-short-cauchy-base.cjs",
            "tailSourceSHA256": self.scripts_dir/"fd2d-bent-annulus-reference-R205.cjs",
        }
        self.expected_hashes = {key: sha256(path) for key, path in files.items()}
        self.expected_hashes["parameterVectorSHA256"] = vector_digest
        self.adapter_sha256 = sha256(__file__)
        for key, value in (expected_hashes or {}).items():
            if key in self.expected_hashes and self.expected_hashes[key] != value:
                raise ValueError("Independent expected source identity mismatch: "+key)
        self.expected_hashes.update(expected_hashes or {})
        self.command = [node, "--expose-gc", f"--max-old-space-size={heap_mb}",
                        str(self.wrapper), "serve", str(self.scripts_dir),
                        str(self.candidate), str(self.checkpoint)]
        self.stderr = tempfile.TemporaryFile(mode="w+t")
        self.started = time.monotonic()
        self.process = subprocess.Popen(self.command, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=self.stderr, text=True, bufsize=1)
        self.request_count = 0
        self.closed = False
        self.exit_receipt = None
        try:
            self.metadata = self._request(method="metadata")["metadata"]
            self._bind_metadata(saved, allow_interface_probe)
        except BaseException:
            self.close()
            raise

    def _bind_metadata(self, saved, allow_interface_probe):
        m = self.metadata
        if m.get("schema") != METADATA_SCHEMA:
            raise ValueError("Actual complete source metadata required")
        for key in ("sourceStateSHA256", "candidateSHA256", "parameterVectorSHA256",
                    "sourceFileSHA256", "sourceMetadataAdapterSHA256",
                    "providerEntrySHA256", "positionSourceSHA256", "baseSourceSHA256", "tailSourceSHA256"):
            if m.get(key) != self.expected_hashes[key]:
                raise ValueError("Live actual source identity mismatch: "+key)
        is_probe = m.get("interfaceProbeOnly") is True
        if is_probe and not allow_interface_probe:
            raise ValueError("Interface probe cannot initialize an actual source solve")
        expected_kind = ("explicit-new-zero-free-coefficient-interface-probe"
                         if is_probe else "actual-Cauchy-checkpoint")
        if m.get("sourceIdentityKind") != expected_kind:
            raise ValueError("Actual source/probe identity mismatch")
        if (m.get("sourceCheckpointSchema") != saved.get("schema") or saved.get("schema") not in
                ("6a65-Cauchy-global-position-initial-v1", "6a65-Cauchy-global-position-checkpoint-v1")):
            raise ValueError("Own actual Cauchy checkpoint schema required")
        if m.get("sourceHasNoClaimedBaselineOrAcceptance") is not is_probe:
            raise ValueError("Actual source/probe claim receipt mismatch")
        if m.get("completeParameterDimension") != len(saved["z"]):
            raise ValueError("Complete original parameter dimension mismatch")
        if m.get("checkpointDeclaredAcceptedSteps") != saved.get("cauchyAcceptedSteps"):
            raise ValueError("Actual accepted-count metadata mismatch")
        if type(saved.get("cauchyAcceptedSteps")) is not int or saved["cauchyAcceptedSteps"] < 0:
            raise ValueError("Actual declared accepted count required")
        for key in ("completeCoefficientsFrozen", "amplitudeAndCuffHeightUnchanged",
                    "sourceAngularPrimitiveUnchanged", "sourceMetricUnchanged",
                    "radialCutsAreOriginalPositionProviderCuts", "adapterChangesOnlyMetadata"):
            if m.get(key) is not True:
                raise ValueError("Missing frozen-source receipt: "+key)
        if m.get("FourierOrHermiteBackgroundProjection") is not False:
            raise ValueError("Projected background is not allowed")
        self.c, self.S, self.cuff = (float(m[key]) for key in ("c", "S", "cuff"))
        if not (0 < self.c < self.S and self.cuff == self.S+.48):
            raise ValueError("Full source domain must include the true flat cuff")
        if m.get("primitiveAngles") != saved["options"]["angles"]:
            raise ValueError("Source primitive angle count changed")
        cuts = np.asarray(m["completeIntegrationCuts"], dtype=np.float64)
        radial = np.asarray(m["radialCuts"], dtype=np.float64)
        if (cuts.ndim != 1 or not len(cuts) or not np.all(np.isfinite(cuts))
                or np.any(np.diff(cuts) <= 0) or cuts[0] != 0 or cuts[-1] != self.cuff):
            raise ValueError("Complete exact physical integration partition required")
        if any(q not in set(cuts.tolist()) for q in radial.tolist()):
            raise ValueError("Original physical background partition was dropped")
        cuts.setflags(write=False)
        self.integration_cuts = cuts

    def _request(self, **request):
        if self.closed:
            raise RuntimeError("Actual oracle has been closed")
        self.request_count += 1
        request["id"] = self.request_count
        self.process.stdin.write(json.dumps(request, allow_nan=False, separators=(",", ":"))+"\n")
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            self.stderr.flush()
            self.stderr.seek(0)
            raise RuntimeError("Actual source oracle terminated: "+self.stderr.read())
        answer = json.loads(line)
        if answer.get("id") != self.request_count or answer.get("ok") is not True:
            raise RuntimeError("Actual source query failed: "+str(answer.get("error", answer)))
        return answer

    @staticmethod
    def _block(s, u, jets, radius):
        jets.setflags(write=False)
        radius.setflags(write=False)
        return dict(s=s, u=u, jets=jets, point_jets=jets.swapaxes(1, 2),
                    radius=radius, a=radius[:, 0], a_s=radius[:, 1], a_ss=radius[:, 2],
                    bb=np.broadcast_to(radius[:, 0, None], (len(s), len(u))))

    def sample(self, s, u):
        sx, angles = np.atleast_1d(np.asarray(s, dtype=np.float64)), np.atleast_1d(np.asarray(u, dtype=np.float64))
        if (sx.ndim != 1 or angles.ndim != 1 or not len(sx) or not len(angles)
                or not np.all(np.isfinite(sx)) or not np.all(np.isfinite(angles))
                or np.min(sx) < 0 or np.max(sx) > self.cuff):
            raise ValueError("Finite physical s and material-angle vectors within the complete domain required")
        jets = np.empty((len(sx), 6, len(angles), 3), dtype=np.float64)
        radius = np.empty((len(sx), 3), dtype=np.float64)
        rows = []
        for j, position in enumerate(sx):
            answer = self._request(method="sample", s=float(position), u=angles.tolist(), deep=False)
            if answer["s"] != position or answer["u"] != angles.tolist():
                raise ValueError("Source changed requested physical coordinates")
            for k, name in enumerate(JET_ORDER):
                jet = np.asarray(answer["jets"][name], dtype=np.float64)
                if jet.shape != (len(angles), 3):
                    raise ValueError("Actual complete source jet shape mismatch: "+name)
                jets[j, k] = jet
            radius[j] = [answer["radius"][key] for key in ("a", "as", "ass")]
            rows.append(answer["diagnostics"])
        if not (np.all(np.isfinite(jets)) and np.all(np.isfinite(radius)) and np.all(radius[:, 0] > 0)):
            raise ArithmeticError("Actual source has nonfinite jets or nonpositive physical radius")
        self._request(method="clear")
        out = self._block(sx, angles, jets, radius)
        out["source_point_diagnostics"] = rows
        return out

    def cache(self, s, u, prefix, *, batch_size=4):
        """Write direct actual sample blocks to fresh external NumPy memmaps.

        The returned arrays reopen the maps read-only. These arrays hold
        actual samples, never coefficients of a surrogate representation.
        """
        sx, angles = np.atleast_1d(np.asarray(s, dtype=np.float64)), np.atleast_1d(np.asarray(u, dtype=np.float64))
        if type(batch_size) is not int or batch_size < 1:
            raise ValueError("Positive radial batch count required")
        if (sx.ndim != 1 or angles.ndim != 1 or not len(sx) or not len(angles)
                or not np.all(np.isfinite(sx)) or not np.all(np.isfinite(angles))
                or np.min(sx) < 0 or np.max(sx) > self.cuff):
            raise ValueError("Finite nonempty actual physical sample grid required")
        prefix = Path(prefix).resolve()
        repository = self.scripts_dir.parents[2]
        if prefix == repository or repository in prefix.parents:
            raise ValueError("Actual arrays must remain outside the Git repository")
        files = {key: Path(str(prefix)+suffix) for key, suffix in (
            ("jets", "-jets.npy"), ("radius", "-radius.npy"), ("report", "-cache.json"))}
        if any(path.exists() for path in files.values()):
            raise FileExistsError("Fresh actual background memmap paths required")
        prefix.parent.mkdir(parents=True, exist_ok=True)
        jets = np.lib.format.open_memmap(files["jets"], mode="w+", dtype="<f8",
                                        shape=(len(sx), 6, len(angles), 3))
        radius = np.lib.format.open_memmap(files["radius"], mode="w+", dtype="<f8", shape=(len(sx), 3))
        start = time.monotonic()
        rows = []
        for lo in range(0, len(sx), batch_size):
            hi = min(lo+batch_size, len(sx))
            block = self.sample(sx[lo:hi], angles)
            jets[lo:hi], radius[lo:hi] = block["jets"], block["radius"]
            rows.extend(block["source_point_diagnostics"])
            jets.flush()
            radius.flush()
        del jets, radius
        receipt = dict(
            schema="6a65-actual-Cauchy-direct-background-samples-memmap-v1",
            source=self.metadata, independentlyExpectedHashes=self.expected_hashes,
            pythonAdapterSHA256=self.adapter_sha256,
            interfaceProbeOnly=self.metadata["interfaceProbeOnly"],
            jetOrder=JET_ORDER, shape=[len(sx), 6, len(angles), 3], dtype="little-endian Float64",
            s=sx.tolist(), u=angles.tolist(), physicalGridSHA256=_array_sha(sx), materialGridSHA256=_array_sha(angles),
            jetsSHA256=sha256(files["jets"]), radiusSHA256=sha256(files["radius"]),
            sourcePointDiagnostics=rows, seconds=time.monotonic()-start,
            directOriginalSourceSamples=True, FourierOrHermiteBackgroundProjection=False,
            unchangedSourceCoefficients=True, unchangedTargetMetric=True,
            actualAcceptedSteps=0, continuousCertificate=False,
            sourceStillOpen=True, externalNaturalExitReceiptRequired=True,
        )
        files["report"].write_text(json.dumps(receipt, indent=2, allow_nan=False)+"\n")
        out = self._block(sx, angles, np.load(files["jets"], mmap_mode="r"),
                          np.load(files["radius"], mmap_mode="r"))
        out.update(receipt=receipt, files={key: str(path) for key, path in files.items()},
                   source_point_diagnostics=rows)
        return out

    def close(self):
        if self.closed:
            return self.exit_receipt
        self.closed = True
        if self.process.stdin and not self.process.stdin.closed:
            self.process.stdin.close()
        try:
            code = self.process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            code = self.process.wait(timeout=10)
            self.exit_receipt = dict(actualOSExitCode=code, naturalExit=False,
                                     seconds=time.monotonic()-self.started)
            raise RuntimeError("Source failed to exit naturally after EOF")
        finally:
            self.stderr.flush()
            self.stderr.seek(0)
            error_text = self.stderr.read()
            self.stderr.close()
        self.exit_receipt = dict(actualOSExitCode=code, naturalExit=True,
            seconds=time.monotonic()-self.started, requests=self.request_count,
            sourceStateSHA256=self.expected_hashes["sourceStateSHA256"],
            parameterVectorSHA256=self.expected_hashes["parameterVectorSHA256"],
            pythonAdapterSHA256=self.adapter_sha256,
            stderrSHA256=hashlib.sha256(error_text.encode()).hexdigest())
        if code:
            raise RuntimeError("Actual source child exited nonzero: "+str(code)+"\n"+error_text)
        return self.exit_receipt

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False
