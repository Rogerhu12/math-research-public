#!/usr/bin/env python3
"""Independent G11 for suffix-only positions against the original target."""
import argparse,hashlib,importlib.util,json,os,sys,time
from pathlib import Path
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import numpy as np

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for key in ("scripts","prepared","prepare-entry","observer","state","output"):
        ap.add_argument("--"+key,required=True,type=Path)
    args=ap.parse_args();start=time.monotonic();here=Path(__file__).parent
    actual=here/"2ecf-polar-c2-independent-g11-resume-observe.py"
    original=module(actual,"exact_original_G11_consumer")
    saved,definition,fullbasis,mods=original.source_and_basis(args)
    src=json.loads(args.observer.read_text());state=json.loads(args.state.read_text())
    helper=here/"2ecf-polar-fixed-prefix-position-basis.py"
    basis,offset=module(helper,"exact_suffix_basis").restrict(fullbasis)
    if (src["sourceEntrySHA256"]!=sha(actual) or src["basis"]!=fullbasis.definition
            or src["sourceIdentity"]!=definition["sourceIdentity"]
            or state["modelDefinition"]["basis"]!=basis.definition
            or state["modelDefinition"]["restrictionEntrySHA256"]!=sha(helper)
            or state["preparedSHA256"]!=sha(args.prepared)):
        raise ValueError("A genuine fixed-prefix original-g state and independent G11 source are required")
    for k,v in src["files"].items():
        if sha(v)!=src["SHA256"][k]:raise ValueError("Changed G11 source cache")
    nodes=np.asarray(src["physicalNodes"]);angles=np.asarray(src["angles"])
    jets=np.load(src["files"]["jets"],mmap_mode="r");radius=np.load(src["files"]["radius"],mmap_mode="r")
    designed=False
    direct_packet=original.direct_packet;write=original.write
    z = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
    stream = mods["stream"]
    config = stream.point.PointConfig(**definition["pointConfig"])
    total = None
    for lo in range(0, len(nodes), 12):
        ns = nodes[lo:lo+12]
        packet = jets[lo:lo+12]+direct_packet(basis, ns, z, angles)
        values = stream.point.PointLinearized(packet.swapaxes(1, 2),
            np.broadcast_to(radius[lo:lo+12, 0, None], (len(ns), len(angles))),
            config, {k: np.ones((len(ns), 1))/len(angles) for k in ("metric", "curvature", "geometry")})
        part = stream._block_statistics(values, ns, len(angles))
        # The statistics helper's labels assume an unshifted grid.  The
        # actual packet above was evaluated at the shifted physical angle.
        part["worstMetric"]["u"] += float(angles[0])
        part["worstCurvature"]["u"] += float(angles[0])
        total = stream._merge_statistics(total, part)
    # A concrete check of the direct Fourier consumer on the same actual
    # nonzero field, at unshifted points supported by the production FFT.
    checknodes = np.linspace(basis.c, basis.end, 9)
    u = 2*np.pi*np.arange(128)/128
    direct = direct_packet(basis, checknodes, z, u)
    fft = basis.packet(basis.matrices(checknodes), z, 128)
    errors = np.max(np.abs(direct-fft), axis=(0, 2, 3)).tolist()
    total.pop("squaredNorm", None)
    total.pop("groupSquaredNorm", None)
    report = dict(schema="2ecf-G11-fixed-entire-position-prefix-original-g-v1",
        entrySHA256=sha(__file__),allPrefixTwoJetsOriginal=True,actualFreeColumns=basis.dimension,preparedSHA256=sha(args.prepared), stateSHA256=sha(args.state),
        sourceObserverSHA256=sha(args.observer), ownExtendedAcceptedSteps=state.get("ownExtendedAcceptedSteps",0),
        ownMetricDesignAcceptedSteps=state.get("ownMetricDesignAcceptedSteps",0),
        explicitDesignedMetricUsed=designed,
        designedMetricDefinitionSHA256=state.get("provisionalMetricDefinitionSHA256"),
        sameMetricConvergenceClaim=False,
        actualRadialCount=len(nodes), actualAngularCount=len(angles),
        angularShiftInMeshSteps=.5, statistics=total,
        producerPreparedSHA256=src["preparedSHA256"],
        actualRadialsNotInCurrentTraining=int(len(np.setdiff1d(nodes, saved["caches"]["training"]["nodes"]))),
        originalProducerPreparedCanDifferOnlyInQuadrature=True,
        minAreaRatio=float(np.sqrt(total["minImmersion"])),
        sameActualFieldDirectVersusProductionFFTSixJetErrors=errors,
        objectiveCostNotClaimed=True, observerUsedInOptimization=False,
        finiteSamplesOnly=True, continuousMetricCertified=False, wholeClosedReachCertified=False,
        seconds=time.monotonic()-start)
    digest = write(args.output, report)
    print(json.dumps(dict(event="actual_independent_observation", SHA256=digest,
        ownAcceptedSteps=state.get("ownExtendedAcceptedSteps",state.get("ownMetricDesignAcceptedSteps",0)), metric=total["maxRelativeMetric"],
        curvature=total["maxCurvature"], sigma=report["minAreaRatio"],
        worstMetric=total["worstMetric"], worstCurvature=total["worstCurvature"],
        seconds=report["seconds"])), flush=True)


if __name__=="__main__":main()
