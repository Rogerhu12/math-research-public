#!/usr/bin/env python3
"""Exact zero extension of a quintic Cartesian correction across an old port.

The old active radial columns are clamped-quintic columns 3:-3.  A triple
knot at the former left port preserves their literal seven-knot windows,
while new columns allow its value and first two derivatives to vary.
This helper changes a declared approximation space, never a target metric,
source cache, old coefficient, or existing frozen execution.
"""
from __future__ import annotations
import copy
import hashlib
import json
import numpy as np
from scipy.interpolate import BSpline


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def validate_old_basis(old):
    knots=np.asarray(old.knots,dtype=float)
    if (old.degree!=5 or knots.ndim!=1 or not np.all(np.isfinite(knots))
            or np.any(np.diff(knots)<0) or old.full_count!=len(knots)-6
            or old.full_count!=old.nb+6 or old.dimension!=old.nb*old.na):
        raise ValueError("Complete clamped-quintic Cartesian basis required")
    if not (0<old.c<old.end and np.all(knots[:6]==old.c)
            and np.all(knots[-6:]==old.end)
            and np.all(knots[6:-6]>old.c) and np.all(knots[6:-6]<old.end)):
        raise ValueError("Exactly six endpoint knots and interior knots required")
    if len(set(old.channels))!=old.na:
        raise ValueError("Independent declared angular channels required")
    if len(knots[6:-6]):
        _,counts=np.unique(knots[6:-6],return_counts=True)
        if np.any(counts>3):
            raise ValueError("Old complete free space must be at least C2")
    if not np.array_equal(np.asarray(old._spline.t),knots) or old._spline.k!=5:
        raise ValueError("Actual basis evaluator disagrees with its physical knots")
    return knots


def extend_left_c2(old,left_breaks,left_multiplicities=None):
    """Return an independently declared basis and an exact old-row map.

    left_breaks includes the new left endpoint and the old left endpoint.
    Interior multiplicities may be 1, 2 or 3; the old endpoint has exactly
    multiplicity 3.  Every right-hand old physical knot remains bitwise fixed.
    """
    old_knots=validate_old_basis(old)
    left=np.asarray(left_breaks,dtype=float)
    if (left.ndim!=1 or len(left)<2 or not np.all(np.isfinite(left))
            or not 0<left[0]<left[-1] or left[-1]!=old.c
            or not np.all(np.diff(left)>0)):
        raise ValueError("Increasing positive left breaks must end at the exact old port")
    if left_multiplicities is None:
        multiplicities=np.ones(len(left)-2,dtype=int)
    else:
        raw=np.asarray(left_multiplicities)
        if (raw.shape!=(len(left)-2,) or raw.dtype.kind not in 'iu'
                or np.any(raw<1) or np.any(raw>3)):
            raise ValueError("Explicit integer interior multiplicities must be 1, 2 or 3")
        multiplicities=raw.astype(int,copy=True)
    interior=np.repeat(left[1:-1],multiplicities)
    shift=len(interior)+3
    knots=np.r_[np.repeat(left[0],6),interior,np.repeat(old.c,3),old_knots[6:]]
    new=copy.copy(old)
    new.c=float(left[0]);new.end=float(old.end)
    new.knots=knots;new.breaks=np.unique(knots)
    new.full_count=len(knots)-6;new.nb=new.full_count-6
    new.channels=list(old.channels);new.na=old.na
    new.modes=np.array(old.modes,copy=True)
    new.dimension=new.nb*new.na
    new._spline=BSpline(knots,np.eye(new.full_count),5,extrapolate=False)
    if new.nb!=old.nb+shift:
        raise ArithmeticError("The exact support-extension dimension is inconsistent")
    old_rows=np.arange(old.nb,dtype=int)
    new_rows=old_rows+shift
    for old_row,new_row in zip(old_rows,new_rows):
        # A degree-five B-spline depends on precisely this local knot tuple.
        if not np.array_equal(old_knots[old_row+3:old_row+10],
                knots[new_row+3:new_row+10]):
            raise ArithmeticError("An inherited seven-knot window changed")
    new.definition=copy.deepcopy(old.definition)
    # These belonged to the previous refinement operation, not this change
    # of domain.  Its complete identity is retained by the old-definition SHA.
    for key in ('addedPhysicalKnots','selectedOldCells','oldPhysicalKnotsRetainedExactly'):
        new.definition.pop(key,None)
    new.definition.update(
        schema="6a65-C2-triple-port-exact-left-support-extension-v1",
        degree=5,radialBasisCount=new.nb,fullRadialBasisCount=new.full_count,
        angularChannels=new.na,dimension=new.dimension,
        physicalDomain=[new.c,new.end],physicalBreaks=new.breaks.tolist(),
        normalizedBreaks=((new.breaks-new.c)/(new.end-new.c)).tolist(),
        physicalKnots=knots.tolist(),physicalKnotsAuthoritative=True,
        omittedEndpointColumns=[0,1,2,new.full_count-3,new.full_count-2,new.full_count-1],
        allSixEndpointJetsZero=True,minimumInteriorContinuity=2,
        oldBasisDefinitionSHA256=canonical(old.definition),
        formerLeftPort=float(old.c),formerPortMultiplicity=3,
        formerPortTwoJetsFree=True,newLeftBreaks=left.tolist(),
        newLeftInteriorMultiplicities=multiplicities.tolist(),
        inheritedRadialRowOffset=shift,oldRightInteriorKnotsRetainedExactly=True,
        oldLeftEndpointValueUnchanged=True,oldLeftEndpointMultiplicityBefore=6,
        inheritedLocalKnotWindowsEqual=True,targetMetricModified=False,
        sourceCacheReusedOrCertifiedByThisHelper=False)
    return new,new_rows


def prolongate_exact(old,new,old_coefficients):
    """Copy every old coefficient literally, and set every new coefficient to 0."""
    old_knots=validate_old_basis(old);new_knots=validate_old_basis(new)
    if (new.definition.get('schema')!="6a65-C2-triple-port-exact-left-support-extension-v1"
            or new.definition.get('oldBasisDefinitionSHA256')!=canonical(old.definition)
            or new.channels!=old.channels or new.c>=old.c or new.end!=old.end):
        raise ValueError("An exact declared extension of this old space is required")
    source=np.asarray(old_coefficients)
    if source.dtype!=np.dtype('float64') or source.shape!=(old.nb,old.na):
        raise ValueError("Actual full binary64 old coefficient matrix required")
    if not np.all(np.isfinite(source)):
        raise ValueError("Nonfinite old coefficients cannot be transferred")
    offset=new.nb-old.nb
    if offset!=new.definition['inheritedRadialRowOffset']:
        raise ValueError("Inherited radial mapping changed")
    out=np.zeros((new.nb,new.na),dtype=np.float64)
    out[offset:]=source
    for row in range(old.nb):
        if not np.array_equal(old_knots[row+3:row+10],
                new_knots[row+offset+3:row+offset+10]):
            raise ValueError("The receiving physical basis is not the declared exact embedding")
    if out[offset:].tobytes(order='C')!=source.tobytes(order='C'):
        raise ArithmeticError("An inherited coefficient byte changed")
    return out,dict(oldDimension=old.dimension,newDimension=new.dimension,
        inheritedColumns=old.dimension,addedColumns=new.dimension-old.dimension,
        inheritedCoefficientBytesExact=True,addedCoefficientsExactlyZero=True,
        oldBasisDefinitionSHA256=canonical(old.definition),
        newBasisDefinitionSHA256=canonical(new.definition),
        sourceCoefficientSHA256=hashlib.sha256(source.tobytes(order='C')).hexdigest(),
        targetCoefficientSHA256=hashlib.sha256(out.tobytes(order='C')).hexdigest(),
        inheritedLocalSevenKnotWindowsEqual=True,
        continuousOldFieldAndAllTwoJetsMathematicallyUnchanged=True,
        actualNonlinearAcceptedSteps=0,continuousGeometryCertified=False)
