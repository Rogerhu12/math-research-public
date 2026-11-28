"""Actual R248 suffix h-refinement on its three leftmost spans, retaining all harmonics."""
import bisect
import copy
import hashlib
import json
from fractions import Fraction as Q

import numpy as np
from scipy.interpolate import BSpline


def build(parent):
    if parent.nb != 36 or parent.definition["schema"] != "2ecf-R248-exact-position-suffix-v1":
        raise ValueError("The original clamped suffix with all 36 radial functions is required")
    old_knots = [Q.from_float(float(a)) for a in parent.knots]
    breaks = sorted(set(old_knots))
    # Round the new knot positions once. All subsequent insertion identities
    # refer to those exact dyadic positions, including the non-dyadic span splits.
    inserted = [Q.from_float(float(a+(b-a)*Q(i,4)))
                for a,b in zip(breaks[:3],breaks[1:4]) for i in range(1,4)]
    knots = old_knots[:]
    transform = [[Q(i==j) for j in range(parent.full_count)] for i in range(parent.full_count)]
    for knot in inserted:
        k = bisect.bisect_right(knots,knot)-1
        if knot in knots:
            raise ValueError("Actual strictly interior knots required")
        out = transform[:k-4]
        for i in range(k-4,k+1):
            alpha = (knot-knots[i])/(knots[i+5]-knots[i])
            out.append([(1-alpha)*a+alpha*b for a,b in zip(transform[i-1],transform[i])])
        out.extend(transform[k:])
        knots.insert(k+1,knot)
        transform = out
    if any(sum(row)!=1 or min(row)<0 for row in transform):
        raise ArithmeticError("Invalid exact insertion stencil")
    new=copy.copy(parent)
    new.knots=np.array(list(map(float,knots)))
    new.breaks=np.unique(new.knots)
    new.full_count=len(knots)-6
    new.nb=new.full_count-6
    new.dimension=new.nb*new.na
    new._spline=BSpline(new.knots,np.eye(new.full_count),5,extrapolate=False)
    if any(any(row[3:-3]) for row in transform[:3]+transform[-3:]):
        raise ArithmeticError("Exact old endpoint constraints do not survive")
    restricted = [row[3:-3] for row in transform[3:-3]]
    serialized = [[str(x) for x in row] for row in restricted]
    digest = hashlib.sha256(json.dumps(serialized,separators=(",",":")).encode()).hexdigest()
    new.definition = dict(parent.definition,schema="actual-first-three-suffix-spans-quarter-h-v1",
        radialBasisCount=new.nb,dimension=new.dimension,physicalKnots=new.knots.tolist(),
        omittedEndpointColumns=[0,1,2,new.full_count-3,new.full_count-2,new.full_count-1],
        coarseRadialBasisCount=parent.nb,insertedPhysicalKnots=list(map(float,inserted)),
        exactBoehmSHA256=digest,allInheritedKnotsRetained=True)
    return new,restricted


def transfer(z,transform):
    ratios=[[Q.from_float(float(x)) for x in row] for row in z]
    exact=[]
    for row in transform:
        active=[(i,w) for i,w in enumerate(row) if w]
        exact.append([sum((w*ratios[i][j] for i,w in active),Q(0)) for j in range(z.shape[1])])
    result=np.array([[float(q) for q in row] for row in exact])
    rounding=max(abs(q-Q.from_float(float(y))) for row,yr in zip(exact,result) for q,y in zip(row,yr))
    return result,str(rounding)
