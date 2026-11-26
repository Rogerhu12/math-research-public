#!/usr/bin/env python3
"""Strict same-run reuse of direct immutable physical source samples.

Only the original background is cached. Every Cartesian residual, full J/JT,
nonlinear trial, and dense observation is recomputed with the current own z.
A first cache is reusable by a later process only after its actual oracle
exited naturally with status zero. Raw arrays never leave the runner.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import numpy as np


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""):digest.update(block)
    return digest.hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def array_sha(value):
    return hashlib.sha256(np.asarray(value,dtype="<f8").tobytes(order="C")).hexdigest()


def write_fresh(path,value):
    with Path(path).open("x") as out:
        out.write(json.dumps(value,indent=2,allow_nan=False)+"\n")


class FixedSourceCachePool:
    """Validated direct samples; no fit, projection, or coefficient transfer."""
    def __init__(self,root,oracle,source_identity,*,allowed_directory,numerical_identity=None,local_interface_fixture=False):
        self.root=Path(root).resolve()
        allowed=Path(allowed_directory).resolve()
        if not (self.root==allowed or allowed in self.root.parents):
            raise ValueError("Cache must remain inside the explicit Git-external runner output directory")
        if any((p/".git").exists() for p in (self.root,*self.root.parents)):
            raise ValueError("Direct source caches may not be written inside any Git checkout")
        self.oracle=oracle
        self.identity=source_identity
        if local_interface_fixture:
            if source_identity.get("schema")!="6a65-explicit-local-cache-interface-identity-v1":
                raise ValueError("An explicitly labelled local interface identity is required")
        elif (source_identity.get("schema")!="6a65-Cartesian-frozen-actual-source-and-g-v1" or
              type(source_identity.get("runId")) is not int or source_identity["runId"]<1 or
              not re.fullmatch("[0-9a-f]{40}",source_identity.get("sourceEpoch","")) or
              oracle.metadata.get("interfaceProbeOnly") is not False):
            raise ValueError("Production reuse requires the actual same-run fixed-g identity")
        for key in ("sourceStateSHA256","candidateSHA256","parameterVectorSHA256"):
            if source_identity.get(key)!=oracle.expected_hashes.get(key):
                raise ValueError("Live original source and fixed identity disagree: "+key)
        if not isinstance(numerical_identity,dict) or not numerical_identity:
            raise ValueError("Explicit complete numerical model/grid/recipe identity required")
        execution_scope=dict(runId=os.environ.get("GITHUB_RUN_ID"),
            runAttempt=os.environ.get("GITHUB_RUN_ATTEMPT"),job=os.environ.get("GITHUB_JOB"))
        if not local_interface_fixture and (
                execution_scope["runId"]!=str(source_identity["runId"]) or
                not str(execution_scope["runAttempt"]).isdigit() or
                int(execution_scope["runAttempt"])<1 or not execution_scope["job"]):
            raise ValueError("Production cache must belong to this actual Actions job and attempt")
        self.expected=dict(
            schema="6a65-same-run-direct-fixed-source-cache-identity-v1",
            sourceIdentity=source_identity,sourceIdentitySHA256=digest(source_identity),
            numericalIdentity=numerical_identity,executionScope=execution_scope,
            sourceMetadataSHA256=digest(oracle.metadata),
            independentlyExpectedHashes=oracle.expected_hashes,
            originalPythonAdapterSHA256=oracle.adapter_sha256,
            reuseImplementationSHA256=sha(__file__),
            localInterfaceFixtureOnly=bool(local_interface_fixture),
            backgroundProjection=False,originalSourceAndPhysicalMetricFrozen=True)
        self.identity_file=self.root/"identity.json"
        self.seal_file=self.root/"sealed-original-oracle-exit.json"
        if self.root.exists() and not self.root.is_dir():
            raise ValueError("Cache root is not a directory")
        self.root.mkdir(parents=True,exist_ok=True)
        if self.identity_file.exists():
            self._ordinary(self.identity_file)
            if json.loads(self.identity_file.read_text())!=self.expected:
                raise ValueError("Source/run/epoch/g/metadata/implementation cache identity changed")
        else:
            if any(self.root.iterdir()):
                raise ValueError("A nonempty unrelated cache directory cannot be adopted")
            write_fresh(self.identity_file,self.expected)
        self.identity_sha=sha(self.identity_file)
        self.entries={}
        self.created=set()
        self.usage={}
        self.seal=None
        self.seal_sha=None
        if self.seal_file.exists():
            self._ordinary(self.seal_file)
            self.seal_sha=sha(self.seal_file)
            self.seal=json.loads(self.seal_file.read_text())
            if (self.seal.get("schema")!="6a65-direct-fixed-source-cache-natural-exit-seal-v1" or
                self.seal.get("identityFileSHA256")!=self.identity_sha or
                self.seal.get("sourceIdentitySHA256")!=digest(source_identity)):
                raise ValueError("Actual cache seal identity changed")
            self._check_exit(self.seal.get("actualOriginalOracleExit",{}))

    @staticmethod
    def _ordinary(path):
        if path.is_symlink() or not path.is_file():
            raise ValueError("Ordinary local cache file required")

    def _check_exit(self,receipt):
        if (receipt.get("actualOSExitCode")!=0 or receipt.get("naturalExit") is not True or
            receipt.get("sourceStateSHA256")!=self.oracle.expected_hashes["sourceStateSHA256"] or
            receipt.get("parameterVectorSHA256")!=self.oracle.expected_hashes["parameterVectorSHA256"] or
            receipt.get("pythonAdapterSHA256")!=self.oracle.adapter_sha256):
            raise ValueError("Actual successful natural exit of the same original oracle is required")

    def _paths(self,name):
        if name not in ("training","observing"):
            raise ValueError("Explicit fixed training or observing cache required")
        return {key:self.root/(name+suffix) for key,suffix in (
            ("jets","-jets.npy"),("radius","-radius.npy"),("report","-cache.json"),
            ("binding","-fixed-identity.json"))}

    def _grid(self,s,u):
        s=np.asarray(s,dtype=np.float64)
        u=np.asarray(u,dtype=np.float64)
        if (s.ndim!=1 or u.ndim!=1 or not len(s) or not len(u) or
            not np.all(np.isfinite(s)) or not np.all(np.isfinite(u)) or
            np.min(s)<0 or np.max(s)>self.oracle.cuff):
            raise ValueError("Complete finite requested physical grid required")
        return s,u

    def _validate_receipt(self,receipt,s,u):
        if (receipt.get("schema")!="6a65-actual-Cauchy-direct-background-samples-memmap-v1" or
            receipt.get("source")!=self.oracle.metadata or
            receipt.get("independentlyExpectedHashes")!=self.oracle.expected_hashes or
            receipt.get("pythonAdapterSHA256")!=self.oracle.adapter_sha256 or
            receipt.get("shape")!=[len(s),6,len(u),3] or
            tuple(receipt.get("jetOrder",()))!=("X","Xs","Xu","Xss","Xsu","Xuu") or
            receipt.get("dtype")!="little-endian Float64" or
            receipt.get("physicalGridSHA256")!=array_sha(s) or
            receipt.get("materialGridSHA256")!=array_sha(u) or
            not np.array_equal(np.asarray(receipt.get("s")),s) or
            not np.array_equal(np.asarray(receipt.get("u")),u)):
            raise ValueError("Original source receipt/grid/shape/order identity changed")
        for key in ("directOriginalSourceSamples","unchangedSourceCoefficients","unchangedTargetMetric"):
            if receipt.get(key) is not True:raise ValueError("Missing direct unchanged-background receipt")
        if receipt.get("FourierOrHermiteBackgroundProjection") is not False:
            raise ValueError("Background cache may not contain a projection")

    @staticmethod
    def _arrays(paths,s,u):
        for key in ("jets","radius"):
            if paths[key].is_symlink() or not paths[key].is_file():
                raise ValueError("Ordinary local immutable NumPy files required")
        jets=np.load(paths["jets"],mmap_mode="r",allow_pickle=False)
        radius=np.load(paths["radius"],mmap_mode="r",allow_pickle=False)
        if (jets.shape!=(len(s),6,len(u),3) or radius.shape!=(len(s),3) or
            jets.dtype!=np.dtype("<f8") or radius.dtype!=np.dtype("<f8") or
            not jets.flags.c_contiguous or not radius.flags.c_contiguous or
            jets.flags.writeable or radius.flags.writeable):
            raise ValueError("Cache array shape/dtype/layout/read-only contract changed")
        for start in range(0,len(s),16):
            if not np.all(np.isfinite(jets[start:start+16])):
                raise ValueError("Nonfinite immutable source jets")
        if not np.all(np.isfinite(radius)) or np.any(radius[:,0]<=0):
            raise ValueError("Nonfinite or nonpositive immutable target radius")
        sx,ux=s.copy(),u.copy()
        sx.setflags(write=False);ux.setflags(write=False)
        return dict(s=sx,u=ux,jets=jets,point_jets=jets.swapaxes(1,2),
            radius=radius,a=radius[:,0],a_s=radius[:,1],a_ss=radius[:,2],
            bb=np.broadcast_to(radius[:,0,None],(len(s),len(u))))

    def cache(self,name,s,u,*,batch_size=4):
        s,u=self._grid(s,u)
        paths=self._paths(name)
        created=False
        if not paths["binding"].exists():
            if self.seal is not None:
                raise ValueError("A sealed fixed cache cannot silently acquire a different grid")
            if any(paths[k].exists() for k in ("jets","radius","report")):
                raise ValueError("Partial unsealed raw outputs cannot be adopted")
            block=self.oracle.cache(s,u,self.root/name,batch_size=batch_size)
            receipt=block["receipt"]
            self._validate_receipt(receipt,s,u)
            binding=dict(schema="6a65-direct-fixed-source-sample-binding-v1",
                cacheName=name,identityFileSHA256=self.identity_sha,
                sourceIdentitySHA256=digest(self.identity),
                physicalGridSHA256=array_sha(s),materialGridSHA256=array_sha(u),
                shape=[len(s),6,len(u),3],radiusShape=[len(s),3],
                sourceReceiptSHA256=sha(paths["report"]),
                jetsSHA256=sha(paths["jets"]),radiusSHA256=sha(paths["radius"]),
                directOriginalSourceSamples=True,requiresSuccessfulNaturalExitBeforeReuse=True)
            write_fresh(paths["binding"],binding)
            self.created.add(name);created=True
            del block
        for path in paths.values():self._ordinary(path)
        binding=json.loads(paths["binding"].read_text())
        if (binding.get("schema")!="6a65-direct-fixed-source-sample-binding-v1" or
            binding.get("cacheName")!=name or binding.get("identityFileSHA256")!=self.identity_sha or
            binding.get("sourceIdentitySHA256")!=digest(self.identity) or
            binding.get("physicalGridSHA256")!=array_sha(s) or
            binding.get("materialGridSHA256")!=array_sha(u) or
            binding.get("shape")!=[len(s),6,len(u),3] or binding.get("radiusShape")!=[len(s),3]):
            raise ValueError("Cache fixed identity, grid, or declared shape changed")
        if name not in self.created:
            if self.seal is None or self.seal.get("bindings",{}).get(name)!=sha(paths["binding"]):
                raise ValueError("Prior cache lacks the actual matching natural-exit seal")
        if (sha(paths["report"])!=binding["sourceReceiptSHA256"] or
            sha(paths["jets"])!=binding["jetsSHA256"] or sha(paths["radius"])!=binding["radiusSHA256"]):
            raise ValueError("Immutable direct-source cache bytes changed")
        receipt=json.loads(paths["report"].read_text())
        self._validate_receipt(receipt,s,u)
        if receipt["jetsSHA256"]!=binding["jetsSHA256"] or receipt["radiusSHA256"]!=binding["radiusSHA256"]:
            raise ValueError("Actual original cache report and arrays differ")
        result=self._arrays(paths,s,u)
        result.update(receipt=receipt,files={k:str(v) for k,v in paths.items() if k!="binding"},
                      source_point_diagnostics=receipt["sourcePointDiagnostics"])
        self.entries[name]=dict(paths=paths,binding=binding,bindingSHA256=sha(paths["binding"]))
        self.usage[name]=dict(createdDirectSamplesThisProcess=created,reusedImmutableSamples=not created,
            bindingSHA256=sha(paths["binding"]),sourceReceiptSHA256=binding["sourceReceiptSHA256"],
            jetsSHA256=binding["jetsSHA256"],radiusSHA256=binding["radiusSHA256"],
            shape=binding["shape"],physicalGridSHA256=array_sha(s),materialGridSHA256=array_sha(u),
            allArraysReadOnly=True,backgroundProjection=False)
        return result

    def verify_unchanged(self):
        if sha(self.identity_file)!=self.identity_sha:raise ValueError("Cache identity bytes changed")
        for name,entry in self.entries.items():
            p,b=entry["paths"],entry["binding"]
            if (sha(p["binding"])!=entry["bindingSHA256"] or
                sha(p["report"])!=b["sourceReceiptSHA256"] or
                sha(p["jets"])!=b["jetsSHA256"] or sha(p["radius"])!=b["radiusSHA256"]):
                raise ValueError("A complete numerical attempt mutated fixed source cache bytes")
        if self.seal is not None:
            self._ordinary(self.seal_file)
            if sha(self.seal_file)!=self.seal_sha or json.loads(self.seal_file.read_text())!=self.seal:
                raise ValueError("Successful producer seal bytes changed")

    def seal_after_natural_exit(self,exit_receipt):
        self._check_exit(exit_receipt)
        self.verify_unchanged()
        if set(self.entries)!={"training","observing"}:
            raise ValueError("Both complete training and observation source caches must actually exist")
        if self.seal is None:
            seal=dict(schema="6a65-direct-fixed-source-cache-natural-exit-seal-v1",
                identityFileSHA256=self.identity_sha,sourceIdentitySHA256=digest(self.identity),
                bindings={name:entry["bindingSHA256"] for name,entry in self.entries.items()},
                actualOriginalOracleExit=exit_receipt,
                directOriginalSourceSamples=True,allOriginalSourceAndMetricIdentitiesRetained=True,
                actualCartesianAcceptanceNotAssertedByThisSeal=True)
            write_fresh(self.seal_file,seal);self.seal=seal;self.seal_sha=sha(self.seal_file)
        self.verify_unchanged()
        return dict(schema="6a65-fixed-source-cache-reuse-actual-receipt-v1",
            identityFileSHA256=self.identity_sha,sourceIdentitySHA256=digest(self.identity),
            sealedOriginalOracleReceiptSHA256=sha(self.seal_file),
            reuseImplementationSHA256=sha(__file__),usage=self.usage,
            originalSourceAndPhysicalMetricUnchanged=True,
            allCurrentCartesianRowsStillRecomputed=True,rawPublished=False,
            localInterfaceFixtureOnly=self.expected["localInterfaceFixtureOnly"])
