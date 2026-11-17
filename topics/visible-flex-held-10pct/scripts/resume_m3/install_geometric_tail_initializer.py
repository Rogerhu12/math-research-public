#!/usr/bin/env python3
"""Install the existing physical Q/L amplitude guess with its known root L.

Only warm initialization changes. Full nonlinear state equations and all local
and global gates remain. The input must be a task-local source copy.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-topic', type=Path, required=True)
    a = p.parse_args()
    scripts = a.source_topic / 'scripts'
    helper = scripts / '78718-tail-geometric-amplitude-warm.mjs'
    text = helper.read_text()
    needle = 'nextRoot=engine.root(initialized.state,profile,x);'
    if text.count(needle) != 1:
        raise ValueError('Expected original physical Q/L amplitude helper')
    updated = text.replace(needle, 'nextRoot=engine.root(initialized.state,profile,x,initialized.L);')
    (scripts / 'held10-geometric-amplitude-warm.mjs').write_text(updated)
    worker = scripts / '950f-tail-stage-port-v3.mjs'
    before = worker.read_text()
    needle = '   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4)initial=last.states.map(row=>row.map((v,j)=>v*(cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0)?ratio**(j%M+1):ratio)));'
    if before.count(needle) != 1 or 'geometricAmplitudeWarm' in before:
        raise ValueError('Expected original complete-state warm scaling block')
    replacement = '''   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4){
    if(cfg.geometricAmplitudePredictor===true){
     const guess=geometricAmplitudeWarm(last.states,dn,ratio);initial=guess.states;
     trace({event:'geometric_amplitude_initial',call,...guess.diagnostics});
    }else initial=last.states.map(row=>row.map((v,j)=>v*(cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0)?ratio**(j%M+1):ratio)));
   }'''
    after = "import {geometricAmplitudeWarm} from './held10-geometric-amplitude-warm.mjs';\n" + before.replace(needle, replacement)
    worker.write_text(after)
    sha = lambda s: hashlib.sha256(s.encode()).hexdigest()
    print(json.dumps(dict(scope=__doc__, helper_original_sha256=sha(text), helper_derived_sha256=sha(updated),
                          worker_original_sha256=sha(before), worker_derived_sha256=sha(after)), indent=2))


if __name__ == '__main__':
    main()
