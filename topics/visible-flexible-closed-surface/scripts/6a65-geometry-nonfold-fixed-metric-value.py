#!/usr/bin/env python3
"""Own full point-value of the new polar field against a separately frozen g.

The old zero-parameter oracle is used ONLY to define the original target radius.
It stays explicitly an unaccepted interface/definition state. Its old value,
old full cache and any CI checkpoint are not replayed or inherited.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse,hashlib,importlib.util,json,sys,time
from dataclasses import asdict
from pathlib import Path
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out
    spec.loader.exec_module(out);return out


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class FrozenWindowMetric:
    def __init__(self,scripts,candidate,definition,ramp,coast):
        scripts=Path(scripts)
        oracle=module(scripts/"6a65-cartesian-oracle-background.py","nonfold_metric_original_oracle")
        gap=module(scripts/"6a65-geometry-gap-window-background.py","nonfold_metric_window_binding")
        windows=module(scripts/"6a65-geometry-cauchy-short-window.py","nonfold_metric_exact_window")
        self.background=oracle.OracleBackground(scripts,candidate,definition,
            wrapper=scripts/"6a65-geometry-cauchy-source-radial-cuts.cjs",
            allow_interface_probe=True,heap_mb=128)
        if self.background.metadata["interfaceProbeOnly"] is not True:
            self.background.close();raise ValueError("Explicit new target-definition state required")
        self.deep=gap.DeepBoundSource(self.background)
        self.window=windows.ShortWindowMaster(self.deep,scripts,ramp,coast,.2)
        self.ug=2*np.pi*np.arange(1024)/1024
        self.radius_cache={}
        self.identity=dict(originalOracle=self.background.metadata,
            targetDefinitionOnly=True,sourceOldBaselineComputed=False,
            sameMathematicalRecipeAndZeroParameterTargetAsColdPipeline=True,
            noCIStateBytesOrLiteralCacheIdentityClaimed=True,
            targetFieldDoesNotDependOnNewPolarPosition=True,
            targetWindowDefinitionSHA256=sha(scripts/"6a65-geometry-cauchy-short-window.py"),
            window=.2,quadrature=1024,rampMasterSHA256=sha(ramp),coastMasterSHA256=sha(coast),
            radiusDefinition="prefix original scalar; compact original window natural perimeter; original zero-parameter radius after stop")
    def radius(self,s):
        s=float(s)
        if s in self.radius_cache:return self.radius_cache[s]
        if s<=self.window.b:
            value=self.window.prefix.scalar(s)[:3]
        elif s>=self.window.stop:
            packet=self.background.sample([s],[0.])
            value=packet["radius"][0].tolist()
        else:
            q=self.window.window_raw(s,self.ug)
            speed=np.linalg.norm(q["Xu"],axis=1)
            if np.min(speed)<=1e-6:raise ArithmeticError("Frozen target window angular curve is singular")
            speed_s=np.sum(q["Xu"]*q["Xsu"],axis=1)/speed
            speed_ss=(np.sum(q["Xsu"]**2,axis=1)+np.sum(q["Xu"]*q["Xssu"],axis=1))/speed-speed_s**2/speed
            value=(float(np.mean(speed)),float(np.mean(speed_s)),float(np.mean(speed_ss)))
        self.radius_cache[s]=tuple(value)
        self.background._request(method="clear")
        return self.radius_cache[s]
    def close(self):return self.background.close()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--polar-source",type=Path,required=True)
    ap.add_argument("--candidate",type=Path,required=True)
    ap.add_argument("--target-definition",type=Path,required=True)
    ap.add_argument("--ramp-master",type=Path,required=True)
    ap.add_argument("--coast-master",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--angles",type=int,default=128)
    ap.add_argument("--connector-radials",type=int,default=65)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError("Fresh new-field value required")
    start=time.monotonic()
    polar=module(args.polar_source,"nonfold_value_polar_field")
    field=polar.NonfoldPolarConnector(args.scripts,args.ramp_master,args.coast_master)
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","nonfold_value_complete_stream")
    saved=json.loads(args.target_definition.read_text())
    if saved.get("targetMetricDefinitionOnly") is not True:raise ValueError("Explicit isolated target definition required")
    cv=saved["curvatureOptions"];gv=saved["geometryOptions"]
    config=stream.point.PointConfig(metric_tau=float(saved["metricTau"]),
        curvature_tau=float(saved["curvatureTau"]),curvature_guide=float(cv["guide"]),
        true_cuff_height=field.master.Z,central_a=field.master.A)
    t=np.sin(.5*np.pi*np.linspace(0,1,args.connector_radials))**2
    nodes=np.unique(np.r_[np.linspace(0,field.master.c,5),
        field.master.c+field.master.sx,
        np.linspace(field.master.ramp_end,field.b,5),
        field.b+field.L*t,
        field.S+np.asarray([0,.03,.06,.1,.2,.3,.4,.46,.48])])
    ds=np.empty(len(nodes));ds[0]=(nodes[1]-nodes[0])/2;ds[-1]=(nodes[-1]-nodes[-2])/2
    ds[1:-1]=(nodes[2:]-nodes[:-2])/2
    u=2*np.pi*np.arange(args.angles)/args.angles
    metric=FrozenWindowMetric(args.scripts,args.candidate,args.target_definition,args.ramp_master,args.coast_master)
    rows=[];total=None
    try:
        if abs(field.S-metric.background.S)>1e-14 or abs(field.cuff-metric.background.cuff)>1e-14:
            raise ValueError("Physical domains changed")
        for j,s in enumerate(nodes):
            q=field.jet(float(s),u);f,fs,fss=metric.radius(s)
            q.update(f=f,fs=fs,fss=fss)
            point_jets=np.stack([q[k] for k in stream.point.JET_ORDER],axis=1)[None]
            weights={key:np.asarray([[ds[j]/field.S/args.angles*factor]]) for key,factor in
                (("metric",1.),("curvature",float(cv["weight"])),("geometry",float(gv["weight"])))}
            point=stream.point.PointLinearized(point_jets,np.full((1,args.angles),f),config,weights)
            stats=stream._block_statistics(point,np.asarray([s]),args.angles)
            total=stream._merge_statistics(total,stats)
            own=polar.geometry_statistics(q,field.master.A)
            row=dict(s=float(s),segment=q.get("segment"),radius=[f,fs,fss],geometry=own,
                pointStatistics=stats)
            if field.b<=s<=field.S:
                row["polarBudget"]={k:q[k] for k in ("minimumClockControl","minimumHeightControl",
                    "minimumInteriorHeightControl","minimumRho","minimumThetaU",
                    "minimumFixedThetaZs","maximumInverseResidual")}
            rows.append(row)
            if j%8==0 or j==len(nodes)-1:
                print(json.dumps(dict(row=j,total=len(nodes),s=float(s),
                    metric=stats["maxRelativeMetric"],curvature=stats["maxCurvature"],
                    eta=stats["minImmersion"],held=stats["minHeldDistance"])),flush=True)
        target_identity=metric.identity
    finally:
        exit_receipt=metric.close()
    extrema={key:(min if key.startswith("min") else max)(r["geometry"][key] for r in rows)
        for key in rows[0]["geometry"]}
    report=dict(schema="6a65-own-polar-field-complete13-against-frozen-window-metric-v1",
        sourceSHA256=sha(__file__),polarSourceSHA256=sha(args.polar_source),
        targetDefinitionSHA256=sha(args.target_definition),candidateSHA256=sha(args.candidate),
        pointOperatorSHA256=sha(args.scripts/"6a65-cartesian-complete-point-operator.py"),
        streamSHA256=sha(args.scripts/"6a65-cartesian-complete-stream.py"),
        field=field.identities,targetMetric=target_identity,pointConfig=asdict(config),
        parameters=dict(b=field.b,S=field.S,cuff=field.cuff,L=field.L,
            centralA=field.master.A,centralB=field.master.B,amplitude=field.master.amplitude,
            Z=field.master.Z,velocityDegree=field.degree),
        grid=dict(radials=len(nodes),angles=args.angles,physicalNodes=nodes.tolist(),
            radialRule="explicit nonuniform trapezoid ds/S; sine-squared connector nodes including both true endpoints",
            allOriginalThirteenRows=True,sameAsCITrainingGrid=False),
        baseline=total,ownGeometryExtrema=extrema,rows=rows,
        originalTargetDefinitionOracleExit=exit_receipt,
        actualNewPolarValueBaselinesComputed=1,actualOldCauchyValueBaselinesComputed=0,
        actualOptimizationAttempts=0,actualAcceptedSteps=0,
        fullSameTargetMetricUsed=True,newPerimeterNotSubstitutedForTarget=True,
        continuousAngularPositivityCertified=False,continuousReachCertified=False,
        exactIsometryClaimed=False,seconds=time.monotonic()-start,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(reportSHA256=sha(args.output),baseline=total,
        ownGeometryExtrema=extrema,originalOracleExit=exit_receipt,
        seconds=report["seconds"]),allow_nan=False),flush=True)


if __name__=="__main__":main()
