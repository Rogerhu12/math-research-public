#!/usr/bin/env python3
"""Finite endpoint diagnostics for the exact-g spatial meridian length bound.

No source evaluation, optimization, acceptance or continuum certification is
performed. Input ports must be bound to their separately recorded source.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def scale(a,x):return [x*v for v in a]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def norm(a):return math.sqrt(dot(a,a))
def unit(a):
    length=norm(a)
    if not length>0:raise ValueError("Nonzero actual endpoint tangent required")
    return scale(a,1/length)
def angle(a,b):return math.acos(max(-1.,min(1.,dot(a,b))))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def evaluate(row,radius):
    t0,t1=unit(row["V0"]),unit(row["V1"])
    d=sub(row["P1"],row["P0"]);length=row["L"];chord=norm(d)
    theta=angle(t0,t1)
    if not 0<theta<math.pi:raise ValueError("This finite diagnostic uses distinct nonantipodal tangents")
    n=unit(sub(t1,scale(t0,math.cos(theta))))
    arc=scale(add(scale(t0,math.sin(theta)),scale(n,1-math.cos(theta))),radius)
    remainder=sub(d,arc)
    x,y=dot(remainder,t0),dot(remainder,n)
    phi=math.atan2(y,x)
    choices=[(0.,x),(theta,x*math.cos(theta)+y*math.sin(theta))]
    if 0<=phi<=theta:choices.append((phi,math.hypot(x,y)))
    best_phi,best_projection=max(choices,key=lambda item:item[1])
    v=add(scale(t0,math.cos(best_phi)),scale(n,math.sin(best_phi)))
    arc_bound=radius*theta+best_projection
    alpha0,alpha1=angle(t0,v),angle(t1,v)
    direct_form=dot(d,v)+radius*(alpha0+alpha1-math.sin(alpha0)-math.sin(alpha1))
    if abs(arc_bound-direct_form)>1e-12:raise AssertionError("Two exact identities disagree numerically")
    vd=unit(d);d0,d1=angle(t0,vd),angle(t1,vd)
    disjoint=length>=radius*(d0+d1)
    chord_direction_bound=(chord+radius*(d0+d1-math.sin(d0)-math.sin(d1))) if disjoint else None
    values=[chord,radius*theta,arc_bound]
    if disjoint:values.append(chord_direction_bound)
    strongest=max(values)
    projected=add(scale(t0,x),scale(n,y))
    return dict(curvatureBound=1/radius,radius=radius,availableLength=length,chord=chord,
        tangentSpeedSquaredErrors=[dot(row["V0"],row["V0"])-1,dot(row["V1"],row["V1"])-1],
        tangentAngle=theta,minimumTurningLength=radius*theta,
        minorArcSupportBound=arc_bound,chosenMinorArcParameter=best_phi,
        minorArcAdmissibleDirection=v,constantTurnDisplacement=arc,
        remainingDisplacementOutOfEndpointPlane=norm(sub(remainder,projected)),
        chordDirectionBound=chord_direction_bound,chordDirectionSupportDisjoint=disjoint,
        strongestOfTheseNecessaryBounds=strongest,remainingLengthMargin=length-strongest,
        finitePortsNotExcludedByTheseBounds=length>=strongest,
        exactMetricOrIndependentCurveCurvatureHypothesisRequired=True,
        continuumSourceErrorCertified=False,fullSurfaceOrC2ExistenceCertified=False)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ports",type=Path,required=True);parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError("A fresh finite diagnostic report is required")
    source=json.loads(args.ports.read_text())
    if source.get("scope")!="actual-frozen-source-cache-port-diagnostic-only":
        raise ValueError("Explicit actual frozen port diagnostic required")
    rows=[]
    for row in source["rows"]:
        if abs(row["S"]-row["b"]-row["L"])>2e-15:raise ValueError("Actual source length disagrees")
        rows.append(dict(u=row["u"],b=row["b"],S=row["S"],
            requiredReachRadius=evaluate(row,.097),
            stricterGuide=evaluate(row,1/9.5)))
    result=dict(schema="6a65-frozen-prefix-nonorthogonal-spatial-port-budget-v1",
        scriptSHA256=sha(__file__),portsSHA256=sha(args.ports),
        sourceDefinitionSHA256=source["sourceDefinitionSHA256"],rows=rows,
        arithmetic="binary64 finite diagnostic; no interval enclosure claimed",
        sourceEvaluationRepeated=False,normalOrNonlinearTrialComputed=False,
        acceptedSteps=0,completeTopicClaim=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(report=str(args.out),reportSHA256=sha(args.out),
        rows=[dict(u=r["u"],reachBound=r["requiredReachRadius"]["strongestOfTheseNecessaryBounds"],
          reachMargin=r["requiredReachRadius"]["remainingLengthMargin"],
          guideBound=r["stricterGuide"]["strongestOfTheseNecessaryBounds"],
          guideMargin=r["stricterGuide"]["remainingLengthMargin"]) for r in rows])))
if __name__=="__main__":main()

