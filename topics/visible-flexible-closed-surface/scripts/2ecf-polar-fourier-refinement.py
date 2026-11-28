#!/usr/bin/env python3
"""Literal zero extension of a full Cartesian Fourier correction space.

Physical quintic knots, every radial basis function, and the mathematical
target g stay fixed. This helper declares a larger position space only.
It does not validate finite angular quadrature or certify the total source.
"""
from __future__ import annotations
import copy
import hashlib
import json
import numpy as np


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def full_channels(M):
    channels=[]
    for component in range(3):
        channels.append((component,0,'cos'))
        for k in range(1,M+1):
            channels.extend(((component,k,'cos'),(component,k,'sin')))
    return channels


def refine(old,M):
    if (type(M) is not int or M<=old.M or old.degree!=5
            or old.channels!=full_channels(old.M)
            or old.na!=3*(2*old.M+1) or old.dimension!=old.nb*old.na):
        raise ValueError('A larger explicit degree and all original XYZ Fourier channels are required')
    new=copy.copy(old);new.M=M;new.channels=full_channels(M);new.na=len(new.channels)
    new.modes=np.asarray([k for component,k,kind in new.channels],dtype=int)
    new.dimension=new.nb*new.na
    new.definition=copy.deepcopy(old.definition)
    new.definition.update(schema='2ecf-full-XYZ-physical-quintic-Fourier-refinement-v1',
        maxAngularFrequency=M,angularChannels=new.na,dimension=new.dimension,
        channelOrder=[dict(component=i,frequency=k,kind=t) for i,k,t in new.channels],
        parentPositionBasisDefinitionSHA256=canonical(old.definition),
        parentMaxAngularFrequency=old.M,allPhysicalRadialFunctionsIdentical=True,
        inheritedAllCartesianChannels=True,addedChannelsInitiallyExactlyZero=True,
        targetMetricModified=False,angularQuadratureAccuracyCertified=False)
    if not np.array_equal(new.knots,old.knots) or new._spline is not old._spline:
        raise ArithmeticError('Every physical radial function must be unchanged')
    mapping=np.asarray([new.channels.index(row) for row in old.channels],dtype=int)
    return new,mapping


def prolongate(old,new,mapping,z):
    source=np.asarray(z)
    if (source.dtype!=np.dtype('float64') or source.shape!=(old.nb,old.na)
            or not np.all(np.isfinite(source))
            or new.definition['parentPositionBasisDefinitionSHA256']!=canonical(old.definition)
            or new.channels!=full_channels(new.M)
            or any(new.channels[j]!=old.channels[i] for i,j in enumerate(mapping))):
        raise ValueError('The full actual finite coarse field and its exact channel mapping are required')
    out=np.zeros((new.nb,new.na),dtype=np.float64);out[:,mapping]=source
    if out[:,mapping].tobytes()!=source.tobytes():
        raise ArithmeticError('A saved inherited position coefficient changed')
    return out,dict(oldDimension=old.dimension,newDimension=new.dimension,
        oldMaxAngularFrequency=old.M,newMaxAngularFrequency=new.M,
        inheritedColumns=old.dimension,addedColumns=new.dimension-old.dimension,
        inheritedCoefficientBytesExact=True,newCoefficientsExactlyZero=True,
        oldBasisDefinitionSHA256=canonical(old.definition),newBasisDefinitionSHA256=canonical(new.definition),
        sourceCoefficientSHA256=hashlib.sha256(source.tobytes()).hexdigest(),
        targetCoefficientSHA256=hashlib.sha256(out.tobytes()).hexdigest(),
        inheritedAngularFunctionsIdentical=True,allPhysicalRadialFunctionsIdentical=True,
        mathematicalOldFieldAndAllMixedDerivativesUnchanged=True,
        fixedMetricUnchanged=True,newOptimizationAttempts=0,newOptimizationAccepts=0,
        actualFiniteEvaluationEqualityStillRequiresMeasurement=True,
        continuousTotalGeometryCertified=False)
