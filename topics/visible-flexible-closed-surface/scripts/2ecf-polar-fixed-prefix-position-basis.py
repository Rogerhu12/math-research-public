"""Exact suffix restriction inverse to R248. Keep only clamped b..S XYZ functions."""
import copy
import hashlib
import json
import numpy as np
from scipy.interpolate import BSpline


def canonical(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def restrict(parent):
    b=parent.definition['formerLeftPort']
    offset=parent.definition['inheritedRadialRowOffset']
    if parent.nb!=87 or offset!=51 or parent.definition['formerPortMultiplicity']!=3:
        raise ValueError('The actual R248 prefix extension is required')
    out=copy.copy(parent)
    out.c=b
    out.knots=np.r_[np.repeat(b,6),parent.knots[parent.knots>b]]
    out.breaks=np.unique(out.knots)
    out.full_count=len(out.knots)-6
    out.nb=out.full_count-6
    out.dimension=out.nb*out.na
    out._spline=BSpline(out.knots,np.eye(out.full_count),5,extrapolate=False)
    if out.nb!=36 or out.dimension!=5292:raise ValueError('Incorrect original suffix dimension')
    for j in range(out.nb):
        if not np.array_equal(out.knots[j+3:j+10],parent.knots[offset+j+3:offset+j+10]):
            raise ArithmeticError('Inherited B-spline seven-knot window differs')
    out.definition=dict(schema='2ecf-R248-exact-position-suffix-v1',physicalDomain=[b,out.end],
        degree=5,radialBasisCount=out.nb,physicalKnots=out.knots.tolist(),
        maxAngularFrequency=out.M,angularChannels=out.na,dimension=out.dimension,
        omittedEndpointColumns=[0,1,2,out.full_count-3,out.full_count-2,out.full_count-1],
        parentBasisSHA256=canonical(parent.definition),parentCoefficientRowOffset=offset,
        allRetainedLocalKnotWindowsExactlyEqual=True,allCorrectionsZeroThroughPrefixPort=True,
        positionCorrectionTwoJetAtPortExactlyZero=True,allXYZAngularChannelsUnchanged=True)
    return out,offset
