"""Keep actual parent positions as a literal carrier and release a genuine nested Cartesian space."""
import copy
from pathlib import Path
import json
import numpy as np
from scipy.interpolate import BSpline


def prepare(args,core):
    full=core.full;c=core.c
    definition,old,clock,physical,g11,weights,mods,radius,meta,expected=full.prepare(args)
    st=json.loads(args.warm.read_text());md=st["model"]
    if (md["warp"]!=meta["warp"] or md["actualMetric"]!=meta["actualMetric"]
        or md["physicalBasis"]!=meta["physicalBasis"] or md["entry"]!=c.sha(core.__file__)):
        raise ValueError("True same metric, positions and full source required")
    z=np.asarray(st.get("totalCoefficients",st["coefficients"])).reshape(old.nb,old.na)
    direct=core.load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","actual_refined_G11").direct_packet
    # Remove the physical-coordinate matrix override on this chart-only copy.
    chart=copy.copy(old)
    del chart.matrices
    chart.definition=old.definition["sourceChartBasis"]
    hknots=np.load(args.field)["knots"]
    added=np.array([x for x in hknots[1:-1:2] if x not in set(chart.knots)])
    chart.knots=np.sort(np.r_[chart.knots,added])
    chart.breaks=np.unique(chart.knots)
    chart.full_count=len(chart.knots)-6;chart.nb=chart.full_count-6
    chart._spline=BSpline(chart.knots,np.eye(chart.full_count),5,extrapolate=False)
    f=core.load(args.helpers/"2ecf-polar-fourier-refinement.py","refined_HF_frequency")
    chart.M=args.frequency;chart.channels=f.full_channels(chart.M);chart.na=len(chart.channels)
    chart.modes=np.array([k for _,k,_ in chart.channels]);chart.dimension=chart.nb*chart.na
    chart.definition=dict(schema="same-g-active-HF-source-knot-union-and-full-Fourier-release-v1",
        parentChart=old.definition["sourceChartBasis"],insertedKnots=added.tolist(),physicalKnots=chart.knots.tolist(),
        physicalDomain=[chart.c,chart.end],degree=5,omittedEndpointJets=2,dimension=chart.dimension,
        radialBasisCount=chart.nb,angularChannels=chart.na,maxAngularFrequency=chart.M)
    basis=c.physical_basis(chart,clock,md["actualMetric"])
    refined=np.zeros((basis.nb,basis.na))
    last=st["stages"][-1]
    expected=(last["allG10"]["original"],last["independent"]["metric"])
    if args.refined_state:
        r=json.loads(args.refined_state.read_text())
        if (r["model"]["literalParent"]!=c.sha(args.warm) or r["model"]["physicalBasis"]!=basis.definition
            or r["model"]["warp"]!=meta["warp"]):raise ValueError("Incompatible refined physical carrier")
        refined=np.asarray(r.get("totalRefinedCoefficients",r["coefficients"])).reshape(basis.nb,basis.na)
        expected=(r["stages"][-1]["allG10"]["original"],r["stages"][-1]["independent"]["metric"])
    for n,v in list(physical.items())+[("independent",g11)]:
        for j in range(0,len(v.nodes),24):
            sl=slice(j,j+24);x=v.nodes[sl]
            if n=="independent":
                v.jets[sl]+=direct(old,x,z,v.u)
                if args.refined_state:v.jets[sl]+=direct(basis,x,refined,v.u)
            else:
                v.jets[sl]+=old.packet(old.matrices(x),z,len(v.u))
                if args.refined_state:v.jets[sl]+=basis.packet(basis.matrices(x),refined,len(v.u))
    meta.update(literalParent=c.sha(args.warm),trueCarrierBasis=old.definition,
        sameFixedOldBasisRetainedAsExactBackground=True,zeroCoefficientExtensionExact=True,
        physicalBasis=basis.definition,xyzColumns=basis.dimension,angularFrequency=basis.M,
        addedInteriorHFKnotCount=len(added),actualRefinedParent=c.sha(args.refined_state) if args.refined_state else None)
    return definition,basis,clock,physical,g11,weights,mods,radius,meta,expected,refined
