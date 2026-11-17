#!/usr/bin/env python3
"""Refine a different-metric guess by the two actual finite linear responses.

The old nonlinear remainder is added to the new metric's linear state. This
constructs only initial coordinates; the unchanged new nonlinear equations and
all their original gates determine acceptance.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-topic',type=Path,required=True)
    a=p.parse_args()
    file=a.source_topic/'scripts/950f-tail-stage-port-v3.mjs'
    before=file.read_text()
    marker=" last={states:prior.states.map(row=>Float64Array.from(row)),jets:{height:Array.from(prior.cutHeight)}};\n"
    if before.count(marker)!=1:
        raise ValueError('Expected explicit first-valley design initializer')
    replacement=''' const oldPhysical=createRecalibrationFactory(record.config).assemble();
 const oldDn=createCompactTailDN({...record.config,tail:oldPhysical});
 const oldCut=oldDn.cutJets(new Float64Array(2*M));
 const oldLinear=oldDn.tail.initial(Float64Array.from(prior.cutHeight,v=>v/oldCut.radius**4));
 const newLinear=dn.tail.initial(Float64Array.from(prior.cutHeight,v=>v/zero.radius**4));
 let correctionLinf=0;
 const guess=prior.states.map((row,n)=>Float64Array.from(row,(v,j)=>{
   const correction=newLinear[n][j]-oldLinear[n][j];
   correctionLinf=Math.max(correctionLinf,Math.abs(correction));
   return v+correction;
 }));
 last={states:guess,jets:{height:Array.from(prior.cutHeight)}};
 trace({event:'different_metric_linear_difference_initial',correctionLinf,
        scope:'New actual linear response plus old nonlinear remainder, only an initial state; the original nonlinear equations and tolerance still decide acceptance.'});
'''
    after=before.replace(marker,replacement)
    file.write_text(after)
    print(json.dumps(dict(scope=__doc__,before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                          after_sha256=hashlib.sha256(after.encode()).hexdigest()),indent=2))


if __name__=='__main__':main()
