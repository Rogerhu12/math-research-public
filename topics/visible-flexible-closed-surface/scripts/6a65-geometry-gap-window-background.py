#!/usr/bin/env python3
"""Explicit new gap1.05 prefix/window background for complete Cartesian work.

The frozen original Cauchy oracle is independently bound first. This class
declares a different sourceKind and a different natural-perimeter metric.
After the compact window, all original six jets and the true tail are
returned directly. No background Fourier/Hermite projection is introduced.
"""
from __future__ import annotations
import os
for _key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[_key]="1"
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import time
import numpy as np


SCHEMA="6a65-explicit-gap105-prefix-window-natural-metric-source-v1"
SOURCE_KIND="gap105-short-window-natural-metric-v1"
JET_ORDER=("X","Xs","Xu","Xss","Xsu","Xuu")
CERTIFIED_RAMP_SHA="0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7"
CERTIFIED_COAST_SHA="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False).encode()).hexdigest()


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def emit(event,**value):
    print(json.dumps(dict(event=event,**value),allow_nan=False),flush=True)


class DeepBoundSource:
    """Same already-bound live oracle, exposing its exact higher-jet request."""
    def __init__(self,background):
        self.background=background
        self.metadata=background.metadata
        self.maximum_consistency=dict(Xu=0.,Xsu=0.,Xuu=0.,meanPhase=0.)

    def sample(self,s,u,deep=True):
        angles=np.asarray(u,float).reshape(-1)
        answer=self.background._request(method="sample",s=float(s),u=angles.tolist(),deep=bool(deep))
        if answer["s"]!=float(s) or answer["u"]!=angles.tolist():
            raise ValueError("Original source changed requested physical coordinates")
        if deep:
            for key,value in answer["higherJetConsistency"].items():
                self.maximum_consistency[key]=max(self.maximum_consistency[key],float(value))
                if not np.isfinite(value) or value>2e-8:
                    raise ArithmeticError("Original higher-jet consistency failed: "+key)
        jets={}
        for key,value in answer["jets"].items():
            array=np.asarray(value,float)
            if array.shape!=(len(angles),3) or not np.all(np.isfinite(array)):
                raise ValueError("Complete original higher-jet packet required: "+key)
            jets[key]=array
        return dict(**jets,f=float(answer["radius"]["a"]),fs=float(answer["radius"]["as"]),
            fss=float(answer["radius"]["ass"]),segment="preserved_actual_Cauchy_source")


class GapPrefixWindowBackground:
    """Same sample/cache shapes as OracleBackground, explicit different identity."""
    def __init__(self,scripts_dir,candidate,checkpoint,ramp_master,coast_master,*,
                 window=.2,quadrature=1024,heap_mb=128,expected_hashes=None):
        self.scripts_dir=Path(scripts_dir).resolve()
        self.candidate=Path(candidate).resolve()
        self.checkpoint=Path(checkpoint).resolve()
        self.ramp_master=Path(ramp_master).resolve()
        self.coast_master=Path(coast_master).resolve()
        if type(quadrature) is not int or quadrature<128 or quadrature%2:
            raise ValueError("Declared even normalization quadrature >=128 required")
        self.quadrature=quadrature
        self.started=time.monotonic()
        self.adapter_sha256=sha(__file__)
        oracle_path=self.scripts_dir/"6a65-cartesian-oracle-background.py"
        window_path=self.scripts_dir/"6a65-geometry-cauchy-short-window.py"
        oracle=module(oracle_path,"new_gap_validated_original_background")
        windows=module(window_path,"new_gap_actual_compact_window")
        self.original=oracle.OracleBackground(self.scripts_dir,self.candidate,self.checkpoint,
            wrapper=self.scripts_dir/"6a65-geometry-cauchy-source-radial-cuts.cjs",heap_mb=heap_mb)
        self.closed=False
        self.exit_receipt=None
        try:
            self.deep=DeepBoundSource(self.original)
            self.master=windows.ShortWindowMaster(self.deep,self.scripts_dir,
                self.ramp_master,self.coast_master,window)
            self.c=self.master.prefix.c
            self.S=self.master.cut
            self.cuff=self.master.cuff
            self.b,self.stop=self.master.b,self.master.stop
            self.integration_cuts=np.unique(np.r_[self.original.integration_cuts,
                self.c+self.master.prefix.sx,self.master.prefix.ramp_end,self.b,self.stop])
            self.integration_cuts.setflags(write=False)
            self.expected_hashes=dict(
                originalSourceStateSHA256=sha(self.checkpoint),candidateSHA256=sha(self.candidate),
                originalParameterVectorSHA256=self.original.expected_hashes["parameterVectorSHA256"],
                originalOracleSHA256=self.original.expected_hashes["sourceFileSHA256"],
                originalMetadataAdapterSHA256=self.original.expected_hashes["sourceMetadataAdapterSHA256"],
                originalPythonAdapterSHA256=sha(oracle_path),windowDefinitionSourceSHA256=sha(window_path),
                prefixDefinitionSourceSHA256=sha(self.scripts_dir/"6a65-geometry-cauchy-unit-t-warm.py"),
                rampMasterSHA256=sha(self.ramp_master),coastMasterSHA256=sha(self.coast_master),
                newSourceAdapterSHA256=self.adapter_sha256)
            for key,value in (expected_hashes or {}).items():
                if self.expected_hashes.get(key)!=value:
                    raise ValueError("Independent new source identity mismatch: "+key)
            definition=dict(sourceKind=SOURCE_KIND,sourceHashes=self.expected_hashes,
                originalSourceHashes=self.original.expected_hashes,
                physicalDomain=dict(c=self.c,b=self.b,window=float(window),stop=self.stop,S=self.S,cuff=self.cuff),
                actualGeometry=dict(centralA=self.master.prefix.A,centralB=self.master.prefix.B,
                    amplitude=self.original.metadata["amplitude"],Z=self.original.metadata["Z"]),
                radiusDefinition="prefix scalar; compact-window exact natural perimeter; outside original frozen source radius",
                positionDefinition="R233 formal normalized prefix; complete compact C2 Hermite port correction; direct old source after stop",
                evaluation=dict(normalizationQuadrature=quadrature,angleInverseTolerance=5e-13,
                    sourcePrimitiveAngles=self.original.metadata["primitiveAngles"],
                    literalFiniteEvaluationErrorCertified=False),
                originalParameterVectorFrozen=True,newPhysicalClock=False,
                noBackgroundProjection=True)
            self.metadata=dict(schema=SCHEMA,sourceKind=SOURCE_KIND,
                sourceIdentityKind="explicit-new-gap-prefix-window-field",
                sourceDefinition=definition,sourceDefinitionSHA256=canonical_sha(definition),
                sourceWasInterfaceProbeOnly=False,originalSource=self.original.metadata,
                newSourceAcceptedSteps=0,c=self.c,S=self.S,cuff=self.cuff,b=self.b,window=float(window),stop=self.stop,
                centralA=self.master.prefix.A,centralB=self.master.prefix.B,
                centralGap=self.master.prefix.A-self.master.prefix.B,
                amplitude=self.original.metadata["amplitude"],Z=self.original.metadata["Z"],
                completeIntegrationCuts=self.integration_cuts.tolist(),
                primitiveAngles=self.original.metadata["primitiveAngles"],
                normalizationQuadrature=quadrature,originalParameterVectorFrozen=True,
                originalSourceReturnedDirectlyAfterWindow=True,
                originalTrueTailAndCuffUnchanged=True,amplitudeAndCuffHeightUnchanged=True,
                newNaturalMetricFrozen=True,metricDiffersFromOriginalSource=True,
                noBackgroundProjection=True,
                R233FormalPrefixCertificateAppliesToSameSavedMasters=(
                    self.expected_hashes["rampMasterSHA256"]==CERTIFIED_RAMP_SHA
                    and self.expected_hashes["coastMasterSHA256"]==CERTIFIED_COAST_SHA),
                literalFinitePrefixEvaluationErrorCertified=False,
                exactProperHalfTurnOfUnfilteredSavedPrefixCertified=False,
                wholeFieldContinuousCertificate=False,wholeClosedReachCertified=False)
        except BaseException:
            self.original.close()
            self.closed=True
            raise

    def sample(self,s,u):
        sx=np.atleast_1d(np.asarray(s,float))
        angles=np.atleast_1d(np.asarray(u,float))
        if (sx.ndim!=1 or angles.ndim!=1 or not len(sx) or not len(angles)
            or not np.all(np.isfinite(sx)) or not np.all(np.isfinite(angles))
            or np.min(sx)<0 or np.max(sx)>self.cuff):
            raise ValueError("Complete physical sample vectors within true cuff required")
        jets=np.empty((len(sx),6,len(angles),3))
        radius=np.empty((len(sx),3))
        rows=[]
        for j,position in enumerate(sx):
            if position>=self.stop:
                direct=self.original.sample([position],angles)
                jets[j]=direct["jets"][0]
                radius[j]=direct["radius"][0]
                rows.append(dict(s=float(position),segment="direct_original_after_window",
                    originalSixJetsReturnedDirectly=True))
                continue
            q=self.master.normalized(float(position),angles,self.quadrature)
            for k,name in enumerate(JET_ORDER):
                jets[j,k]=q[name]
            radius[j]=[q["f"],q["fs"],q["fss"]]
            rows.append(dict(s=float(position),segment=q["segment"],
                materialInverseResidual=float(q.get("materialInverseResidual",0)),
                originalSixJetsReturnedDirectly=False))
        self.original._request(method="clear")
        if not np.all(np.isfinite(jets)) or not np.all(np.isfinite(radius)) or np.min(radius[:,0])<=0:
            raise ArithmeticError("Finite new-source six jets and positive target radius required")
        jets.setflags(write=False)
        radius.setflags(write=False)
        return dict(s=sx,u=angles,jets=jets,point_jets=jets.swapaxes(1,2),
            radius=radius,a=radius[:,0],a_s=radius[:,1],a_ss=radius[:,2],
            bb=np.broadcast_to(radius[:,0,None],(len(sx),len(angles))),
            source_point_diagnostics=rows)

    def cache(self,s,u,prefix,*,batch_size=4):
        sx=np.atleast_1d(np.asarray(s,float))
        angles=np.atleast_1d(np.asarray(u,float))
        prefix=Path(prefix).resolve()
        repository=self.scripts_dir.parents[2]
        if prefix==repository or repository in prefix.parents:
            raise ValueError("Direct raw arrays must remain outside the repository")
        if type(batch_size) is not int or batch_size<1:
            raise ValueError("Positive physical batch count required")
        paths={key:Path(str(prefix)+suffix) for key,suffix in (
            ("jets","-jets.npy"),("radius","-radius.npy"),("report","-cache.json"))}
        if any(p.exists() for p in paths.values()):
            raise FileExistsError("Fresh actual new-source memmaps required")
        prefix.parent.mkdir(parents=True,exist_ok=True)
        jets=np.lib.format.open_memmap(paths["jets"],mode="w+",dtype="<f8",shape=(len(sx),6,len(angles),3))
        radius=np.lib.format.open_memmap(paths["radius"],mode="w+",dtype="<f8",shape=(len(sx),3))
        rows=[]
        for lo in range(0,len(sx),batch_size):
            block=self.sample(sx[lo:lo+batch_size],angles)
            jets[lo:lo+batch_size]=block["jets"]
            radius[lo:lo+batch_size]=block["radius"]
            rows.extend(block["source_point_diagnostics"])
            jets.flush()
            radius.flush()
        del jets,radius
        receipt=dict(schema="6a65-explicit-new-gap-natural-metric-direct-background-memmap-v1",
            source=self.metadata,independentlyExpectedHashes=self.expected_hashes,
            sourceAdapterSHA256=self.adapter_sha256,jetOrder=list(JET_ORDER),
            physicalSamples=sx.tolist(),angles=angles.tolist(),
            rawJetSHA256=sha(paths["jets"]),rawRadiusSHA256=sha(paths["radius"]),
            literalSourceSamplesOnly=True,backgroundProjection=False,
            originalCheckpointUpdated=False,newSourceAcceptedSteps=0)
        paths["report"].write_text(json.dumps(receipt,indent=2,allow_nan=False)+"\n")
        j=np.load(paths["jets"],mmap_mode="r")
        r=np.load(paths["radius"],mmap_mode="r")
        return dict(s=sx,u=angles,jets=j,point_jets=j.swapaxes(1,2),
            radius=r,a=r[:,0],a_s=r[:,1],a_ss=r[:,2],
            bb=np.broadcast_to(r[:,0,None],(len(sx),len(angles))),
            source_point_diagnostics=rows,receipt=receipt,
            files={key:str(value) for key,value in paths.items()})

    def close(self):
        if self.closed:
            return self.exit_receipt
        original=self.original.close()
        self.exit_receipt=dict(schema="6a65-new-gap-background-natural-child-exit-v1",
            sourceDefinitionSHA256=self.metadata["sourceDefinitionSHA256"],
            originalOracle=original,seconds=time.monotonic()-self.started,
            originalHigherJetConsistency=self.deep.maximum_consistency)
        self.closed=True
        return self.exit_receipt

    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc,tb):
        self.close()
        return False


def bind_new_source_metadata(metadata,expected):
    if (metadata.get("schema")!=SCHEMA or metadata.get("sourceKind")!=SOURCE_KIND
        or metadata.get("sourceIdentityKind")!="explicit-new-gap-prefix-window-field"
        or metadata.get("sourceWasInterfaceProbeOnly") is not False):
        raise ValueError("Explicit actual new gap/natural-metric source required")
    definition=metadata["sourceDefinition"]
    digest=canonical_sha(definition)
    if metadata.get("sourceDefinitionSHA256")!=digest:
        raise ValueError("New source definition digest mismatch")
    for key,value in definition["sourceHashes"].items():
        if not re.fullmatch("[0-9a-f]{64}",value) or expected.get(key)!=value:
            raise ValueError("Independently bound actual new source hash required: "+key)
    for key in ("originalParameterVectorFrozen","originalSourceReturnedDirectlyAfterWindow",
                "originalTrueTailAndCuffUnchanged","newNaturalMetricFrozen","metricDiffersFromOriginalSource",
                "noBackgroundProjection"):
        if metadata.get(key) is not True:
            raise ValueError("Missing new-source receipt: "+key)
    c,S,cuff=(float(metadata[key]) for key in ("c","S","cuff"))
    if not 0<c<S or cuff!=S+.48:
        raise ValueError("Complete actual new-source domain including true cuff required")
    return dict(schema="6a65-Cartesian-frozen-gap105-window-source-and-new-g-v1",
        identitySHA256=digest,sourceKind=SOURCE_KIND,sourceDefinition=definition,
        completeHalfDomain=[0,cuff],correctionDomain=[c,S],
        centralA=metadata["centralA"],amplitude=metadata["amplitude"],Z=metadata["Z"],
        fixedSourceAndMetric=True,originalCauchyStateUnchanged=True,
        newCartesianAcceptedSteps=0,continuumCertificate=False)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("mode",choices=("check","value"))
    ap.add_argument("--scripts-dir",type=Path,required=True)
    ap.add_argument("--candidate",type=Path,required=True)
    ap.add_argument("--checkpoint",type=Path,required=True)
    ap.add_argument("--ramp-master",type=Path,required=True)
    ap.add_argument("--coast-master",type=Path,required=True)
    ap.add_argument("--window",type=float,default=.2)
    ap.add_argument("--quadrature",type=int,default=1024)
    ap.add_argument("--angles",type=int,default=128)
    ap.add_argument("--heap-mb",type=int,default=128)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual new-field receipt required")
    start=time.monotonic()
    saved=json.loads(args.checkpoint.read_text())
    with GapPrefixWindowBackground(args.scripts_dir,args.candidate,args.checkpoint,
        args.ramp_master,args.coast_master,window=args.window,quadrature=args.quadrature,heap_mb=args.heap_mb) as source:
        identity=bind_new_source_metadata(source.metadata,source.expected_hashes)
        angles=np.asarray([.173,.947,2.197,3.641,5.897])
        left=source.master.window_raw(source.b,angles)
        right=source.master.window_raw(source.stop,angles)
        left_ref=source.master.prefix.jet(source.b,angles)
        right_ref=source.deep.sample(source.stop,angles,True)
        def diff(a,b):
            return {key:float(np.max(np.linalg.norm(a[key]-b[key],axis=1))) for key in JET_ORDER}
        check=dict(leftRawCompleteTwoJetDifference=diff(left,left_ref),
            rightRawCompleteTwoJetDifference=diff(right,right_ref),
            interfacePointsAreNotWholeDomainCertificate=True)
        sample_s=(source.stop+source.S)/2
        outside=source.sample([sample_s,source.cuff],angles)
        original=source.original.sample([sample_s,source.cuff],angles)
        check["outsideAndTrueCuffSixJetDifference"]=float(np.max(np.abs(outside["jets"]-original["jets"])))
        check["outsideAndTrueCuffRadiusDifference"]=float(np.max(np.abs(outside["radius"]-original["radius"])))
        output=dict(schema="6a65-explicit-new-gap-window-actual-source-receipt-v1",mode=args.mode,
            source=source.metadata,sourceIdentity=identity,sourceSHA256=sha(__file__),
            actualNewFieldAcceptedSteps=0,oldSourceStateUnchanged=True,checks=check,
            newFieldOwnBaselineComputed=False,wholeClosedReachCertified=False,continuousCertificate=False)
        if args.mode=="value":
            stream=module(args.scripts_dir/"6a65-cartesian-complete-stream.py","new_gap_complete_stream")
            entry=module(args.scripts_dir/"6a65-cartesian-independent-experiment-v3.py","new_gap_shared_quadrature")
            cv,gv=saved["curvatureOptions"],saved["geometryOptions"]
            config=stream.point.PointConfig(metric_tau=float(saved["metricTau"]),
                curvature_tau=float(saved["curvatureTau"]),curvature_guide=float(cv["guide"]),
                true_cuff_height=source.metadata["Z"],central_a=source.metadata["centralA"])
            nodes,weights=entry.quadrature(source.integration_cuts,source.S,2,2,2,
                float(cv["nodeShare"]),float(gv["nodeShare"]),float(cv["weight"]),float(gv["weight"]))
            u=2*np.pi*np.arange(args.angles)/args.angles
            total=None
            for j,s in enumerate(nodes):
                block=source.sample([s],u)
                linear=stream.point.PointLinearized(block["point_jets"],block["bb"],config,
                    {key:value[j:j+1,None]/args.angles for key,value in weights.items()})
                stat=stream._block_statistics(linear,np.asarray([s]),args.angles)
                total=stream._merge_statistics(total,stat)
                if j%12==0 or j==len(nodes)-1:
                    emit("actual_new_gap_complete_point_value",row=j,total=len(nodes),s=float(s),
                        metric=stat["maxRelativeMetric"],curvature=stat["maxCurvature"],
                        held=stat["minHeldDistance"],seconds=time.monotonic()-start)
            output.update(newFieldOwnBaselineComputed=True,baseline=total,
                baselineGrid=dict(radialPoints=len(nodes),angles=args.angles,completeHalfDomain=[0,source.cuff],
                    cuts=source.integration_cuts.tolist(),gaussOrders=[2,2,2],
                    fullThirteenPointRows=True,normalizedPhysicalWeights="ds/original S",
                    pointConfig=asdict(config)),originalCauchyAcceptedSteps=saved["cauchyAcceptedSteps"],
                pointOperatorSHA256=sha(args.scripts_dir/"6a65-cartesian-complete-point-operator.py"),
                streamSHA256=sha(args.scripts_dir/"6a65-cartesian-complete-stream.py"))
        else:
            q=source.sample([source.b+.071],angles)
            output["oneNormalizationProbe"]=dict(s=source.b+.071,finiteSixJets=True,
                radius=q["radius"][0].tolist(),
                relativeGError=float(np.max(np.abs(np.sum(q["jets"][0,2]**2,axis=1)/q["radius"][0,0]**2-1))),
                notAWholeFieldBaseline=True)
    output.update(originalOracleNaturalExit=source.exit_receipt,seconds=time.monotonic()-start,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(output,indent=2,allow_nan=False)+"\n")
    emit("actual_new_gap_source_complete",reportSHA256=sha(args.output),
        newFieldOwnBaselineComputed=output["newFieldOwnBaselineComputed"],
        metric=output.get("baseline",{}).get("maxRelativeMetric"),
        curvature=output.get("baseline",{}).get("maxCurvature"),seconds=output["seconds"])


if __name__=="__main__":
    main()

