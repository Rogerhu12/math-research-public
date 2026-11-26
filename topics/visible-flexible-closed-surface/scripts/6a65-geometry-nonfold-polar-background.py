#!/usr/bin/env python3
"""Actual polar geometry, with an independently frozen window target metric.

This source is neither an old Cauchy checkpoint nor the old gap geometry.
The explicitly probe-only zero parameter file defines g, never a claimed
old accepted position. Every new position six-jet is evaluated directly.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import hashlib,importlib.util,json,re,sys,time
from pathlib import Path
import numpy as np

SCHEMA="6a65-actual-positive-height-polar-independent-metric-background-v1"
SOURCE_KIND="positive-height-polar-with-independent-zero-window-target-v1"
JET_ORDER=("X","Xs","Xu","Xss","Xsu","Xuu")
POLAR_SHA="9918079d1e4356104c0e0c8c6df10714643b052de33f4eca1593fa77f3a42ea6"
TARGET_SHA="e5ea3ada40f81d1eda8f0b90b4191c382adf84089a16fc9bbc34c7245679cb29"
RAMP_SHA="0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7"
COAST_SHA="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out
    spec.loader.exec_module(out);return out

class NonfoldPolarBackground:
    def __init__(self,scripts,candidate,target_definition,ramp_master,coast_master):
        self.scripts_dir=Path(scripts).resolve()
        self.candidate=Path(candidate).resolve();self.target_definition=Path(target_definition).resolve()
        self.ramp_master=Path(ramp_master).resolve();self.coast_master=Path(coast_master).resolve()
        self.started=time.monotonic();self.closed=False;self.exit_receipt=None
        polar_path=self.scripts_dir/"6a65-geometry-nonfold-height-allocation.py"
        target_path=self.scripts_dir/"6a65-geometry-nonfold-fixed-metric-value.py"
        for path,digest in ((polar_path,POLAR_SHA),(target_path,TARGET_SHA),
                (self.ramp_master,RAMP_SHA),(self.coast_master,COAST_SHA)):
            if sha(path)!=digest:raise ValueError("Frozen actual definition bytes changed: "+str(path))
        saved=json.loads(self.target_definition.read_text())
        if (saved.get("interfaceProbeOnly") is not True or
            saved.get("targetMetricDefinitionOnly") is not True or
            saved.get("actualAcceptedSteps")!=0 or saved.get("actualValueBaseline") is not False):
            raise ValueError("Explicit zero-parameter target definition required; no old acceptance may be borrowed")
        polar=module(polar_path,"nonfold_background_actual_polar")
        target=module(target_path,"nonfold_background_independent_target")
        self.field=polar.NonfoldPolarConnector(self.scripts_dir,self.ramp_master,self.coast_master)
        self.metric=target.FrozenWindowMetric(self.scripts_dir,self.candidate,self.target_definition,
            self.ramp_master,self.coast_master)
        try:
            self.c=self.field.master.c;self.b=self.field.b;self.S=self.field.S;self.cuff=self.field.cuff
            self.stop=self.metric.window.stop
            if abs(self.S-self.metric.background.S)>1e-14 or abs(self.cuff-self.metric.background.cuff)>1e-14:
                raise ValueError("Polar and independent target have different physical domains")
            self.integration_cuts=np.unique(np.r_[self.metric.background.integration_cuts,
                self.c+self.field.master.sx,self.field.master.ramp_end,self.b,self.stop,self.S,self.cuff])
            self.integration_cuts.setflags(write=False)
            old=self.metric.background.expected_hashes
            self.expected_hashes=dict(adapter=sha(__file__),polar=POLAR_SHA,
                originalPolar=sha(self.scripts_dir/"6a65-geometry-nonfold-polar-connector.py"),
                independentMetric=TARGET_SHA,targetDefinition=sha(self.target_definition),
                candidate=sha(self.candidate),rampMaster=RAMP_SHA,coastMaster=COAST_SHA,
                warm=sha(self.scripts_dir/"6a65-geometry-cauchy-unit-t-warm.py"),
                ports=sha(self.scripts_dir/"6a65-geometry-r137-two-connectors.py"),
                targetWindow=sha(self.scripts_dir/"6a65-geometry-cauchy-short-window.py"),
                targetOracle=old["sourceFileSHA256"],targetMetadataAdapter=old["sourceMetadataAdapterSHA256"],
                targetParameters=old["parameterVectorSHA256"],
                targetPythonAdapter=sha(self.scripts_dir/"6a65-cartesian-oracle-background.py"))
            physical=dict(c=self.c,b=self.b,S=self.S,cuff=self.cuff,L=self.field.L,targetWindowStop=self.stop)
            geometry=dict(centralA=self.field.master.A,centralB=self.field.master.B,
                amplitude=self.field.master.amplitude,Z=self.field.master.Z,degree=self.field.degree)
            definition=dict(sourceKind=SOURCE_KIND,sourceHashes=self.expected_hashes,
                physicalDomain=physical,actualGeometry=geometry,
                positionDefinition="R233 formal normalized prefix; positive-height weighted polar connector; original R205 true tail",
                metricDefinition=self.metric.identity["radiusDefinition"],
                targetEvaluation=dict(window=.2,normalizationQuadrature=1024,
                    targetZeroParameterVectorFrozen=True,targetDefinitionWasInterfaceProbeOnly=True,
                    targetDefinitionHadValueBaseline=False,targetDefinitionHadAcceptedSteps=0),
                polarPerimeterUsedAsTarget=False,geometryHasOwnAcceptanceCounter=True,
                noPositionProjection=True,allSixJetsFromOneActualField=True)
            self.metadata=dict(schema=SCHEMA,sourceKind=SOURCE_KIND,
                sourceIdentityKind="actual-new-polar-geometry-with-separately-defined-fixed-g",
                sourceDefinition=definition,sourceDefinitionSHA256=canonical(definition),
                positionIsInterfaceProbe=False,targetDefinitionWasInterfaceProbeOnly=True,
                actualOldCauchyBaselinesBorrowed=0,actualOldCauchyAcceptedStepsBorrowed=0,
                ownCartesianAcceptedSteps=0,**physical,**geometry,
                completeIntegrationCuts=self.integration_cuts.tolist(),
                primitiveAngles=self.metric.background.metadata["primitiveAngles"],
                independentTargetMetricFrozen=True,polarPerimeterUsedAsTarget=False,
                completeTrueTailAndCuffRetained=True,noBackgroundProjection=True,
                formalPrefixMasterIdentitiesMatchR233=True,literalPrefixEvaluationCertified=False,
                continuousPolarAngleHypothesesCertified=False,wholeClosedReachCertified=False)
        except BaseException:
            self.metric.close();self.closed=True;raise

    def sample(self,s,u):
        nodes=np.atleast_1d(np.asarray(s,float));angles=np.atleast_1d(np.asarray(u,float))
        if (nodes.ndim!=1 or angles.ndim!=1 or not len(nodes) or not len(angles)
            or not np.all(np.isfinite(nodes)) or not np.all(np.isfinite(angles))
            or np.min(nodes)<0 or np.max(nodes)>self.cuff):
            raise ValueError("Finite physical coordinates through the true cuff required")
        jets=np.empty((len(nodes),6,len(angles),3));radius=np.empty((len(nodes),3));diagnostics=[]
        for j,position in enumerate(nodes):
            q=self.field.jet(float(position),angles)
            jets[j]=np.stack([q[k] for k in JET_ORDER])
            radius[j]=self.metric.radius(float(position))
            diagnostics.append(dict(s=float(position),segment=q.get("segment"),
                analyticSixJets=True,backgroundProjection=False))
        if not np.all(np.isfinite(jets)) or not np.all(np.isfinite(radius)) or np.min(radius[:,0])<=0:
            raise ArithmeticError("Finite actual six jets and positive independent radius required")
        jets.setflags(write=False);radius.setflags(write=False)
        return dict(s=nodes,u=angles,jets=jets,point_jets=jets.swapaxes(1,2),radius=radius,
            a=radius[:,0],a_s=radius[:,1],a_ss=radius[:,2],
            bb=np.broadcast_to(radius[:,0,None],(len(nodes),len(angles))),
            source_point_diagnostics=diagnostics)

    def cache(self,s,u,prefix,*,batch_size=1):
        nodes=np.asarray(s,float);angles=np.asarray(u,float);prefix=Path(prefix).resolve()
        repository=self.scripts_dir.parents[2]
        if prefix==repository or repository in prefix.parents:raise ValueError("Raw arrays must remain outside Git")
        paths={k:Path(str(prefix)+v) for k,v in (("jets","-jets.npy"),("radius","-radius.npy"),("report","-cache.json"))}
        if any(p.exists() for p in paths.values()):raise FileExistsError("Fresh actual direct cache required")
        if type(batch_size)is not int or batch_size<1:raise ValueError("Positive source batch required")
        prefix.parent.mkdir(parents=True,exist_ok=True)
        jets=np.lib.format.open_memmap(paths["jets"],mode="w+",dtype="<f8",shape=(len(nodes),6,len(angles),3))
        radius=np.lib.format.open_memmap(paths["radius"],mode="w+",dtype="<f8",shape=(len(nodes),3))
        diagnostics=[]
        for lo in range(0,len(nodes),batch_size):
            packet=self.sample(nodes[lo:lo+batch_size],angles)
            jets[lo:lo+batch_size]=packet["jets"];radius[lo:lo+batch_size]=packet["radius"]
            diagnostics.extend(packet["source_point_diagnostics"]);jets.flush();radius.flush()
            if lo%8==0 or lo+batch_size>=len(nodes):
                print(json.dumps(dict(event="actual_polar_six_jet_cache",completed=min(lo+batch_size,len(nodes)),
                    radials=len(nodes),angles=len(angles),seconds=time.monotonic()-self.started)),flush=True)
        del jets,radius
        receipt=dict(schema=SCHEMA+"-direct-memmap",source=self.metadata,
            actualJetOrder=list(JET_ORDER),physicalSamples=nodes.tolist(),angles=angles.tolist(),
            rawJetSHA256=sha(paths["jets"]),rawRadiusSHA256=sha(paths["radius"]),
            literalSourceSamplesOnly=True,backgroundProjection=False,oldCauchyPositionUsed=False,
            newPolarCartesianAcceptedSteps=0,sourcePointDiagnostics=diagnostics)
        paths["report"].write_text(json.dumps(receipt,separators=(",",":"),allow_nan=False)+"\n")
        return dict(s=nodes,u=angles,files={k:str(v) for k,v in paths.items()},receipt=receipt)

    def close(self):
        if self.closed:return self.exit_receipt
        child=self.metric.close()
        self.exit_receipt=dict(schema=SCHEMA+"-target-definition-oracle-exit",
            sourceDefinitionSHA256=self.metadata["sourceDefinitionSHA256"],targetDefinitionOracle=child,
            actualOldCauchyPositionValueComputed=False,seconds=time.monotonic()-self.started)
        self.closed=True;return self.exit_receipt
    def __enter__(self):return self
    def __exit__(self,*args):self.close();return False

def bind_new_source_metadata(metadata,expected):
    if (metadata.get("schema")!=SCHEMA or metadata.get("sourceKind")!=SOURCE_KIND or
        metadata.get("sourceIdentityKind")!="actual-new-polar-geometry-with-separately-defined-fixed-g" or
        metadata.get("positionIsInterfaceProbe") is not False):
        raise ValueError("Independent actual polar source kind required")
    definition=metadata["sourceDefinition"];digest=canonical(definition)
    if metadata.get("sourceDefinitionSHA256")!=digest:raise ValueError("Source definition digest changed")
    if definition["sourceHashes"]!=expected:raise ValueError("Independent source hash map changed")
    for key,value in expected.items():
        if not isinstance(value,str) or not re.fullmatch("[0-9a-f]{64}",value):
            raise ValueError("Literal SHA256 source identity required: "+key)
    for key in ("independentTargetMetricFrozen","completeTrueTailAndCuffRetained","noBackgroundProjection"):
        if metadata.get(key)is not True:raise ValueError("Incomplete new polar source: "+key)
    if metadata.get("polarPerimeterUsedAsTarget")is not False:raise ValueError("Polar position cannot silently redefine g")
    c,b,S,cuff=(float(metadata[k]) for k in ("c","b","S","cuff"))
    if not 0<c<b<S or cuff!=S+.48:raise ValueError("Full physical domain changed")
    return dict(schema=SCHEMA+"-identity",sourceKind=SOURCE_KIND,identitySHA256=digest,
        sourceDefinition=definition,completeHalfDomain=[0,cuff],correctionDomain=[b,S],
        centralA=metadata["centralA"],amplitude=metadata["amplitude"],Z=metadata["Z"],
        fixedSourceAndIndependentMetric=True,newPolarCartesianAcceptedSteps=0,
        wholeClosedReachCertified=False)
