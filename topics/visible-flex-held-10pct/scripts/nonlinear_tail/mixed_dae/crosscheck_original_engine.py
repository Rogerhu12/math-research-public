"""Compare the mixed variables directly with the immutable momentum engine.

This check includes nonzero angular flux, either radial sign, nonconstant w,
both original orientation signs, and two distinct internal mu scales.
"""
import argparse, hashlib, json, subprocess
from pathlib import Path
import numpy as np
from mu_free_fields import MuFreeFields

SCRIPT = r'''
import {pathToFileURL} from 'node:url';
import fs from 'node:fs';
const {createMomentumTailEngine}=await import(pathToFileURL(process.argv[1]));
const input=JSON.parse(fs.readFileSync(0,'utf8')),out=[];
for(const p of input){
 const M=p.M,N=p.N,engine=createMomentumTailEngine({modes:M,quadrature:N,spacing:2,mu:p.mu,orientation:p.orientation,projectionFloor:.01});
 const raw=new Float64Array(2*M);
 for(let j=0;j<M;j++){
  raw[j]=Math.SQRT2*p.w*p.v[j]/p.r**3;
  raw[M+j]=Math.SQRT2*p.w*p.L[j]/(Math.sqrt(12)*p.r**3);
 }
 const profile=x=>({r:p.r+p.rx*x,drdx:p.rx,logw:Math.log(p.w)+p.ell*x,dlogwdx:p.ell});
 const init=engine.initializeFromRaw(raw,profile),rt=engine.root(init.state,profile,0,init.L),rhs=engine.rhs(init.state,profile,0,false,rt);
 const vf=p.r**3/(Math.SQRT2*p.w),tf=p.orientation*Math.sqrt(12)*p.mu/(Math.SQRT2*p.r**4*p.w**2),s=p.rx/p.r;
 const v=Array.from(init.state.slice(0,M),x=>vf*x),t=Array.from(init.state.slice(M,2*M),x=>tf*x);
 const mixedFlow=Array.from(rhs.slice(0,2*M),(x,j)=>j<M?vf*x+(3*s-p.ell)*v[j]:tf*x-(4*s+2*p.ell)*t[j-M]);
 out.push({v,t,L:Array.from(init.L),mixedFlow,gram:Array.from(rt.e.B),minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,rootRelative:rt.err/rt.scale});
}
console.log(JSON.stringify(out));
'''


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-module', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(551751)
    inputs = []
    for M in (4, 8):
        freq = 2*np.arange(1, M+1)
        for w in (.00358, .08, .3):
            for orientation, mu, rx, ell in ((1, .6, .17, .37), (-1, 1e-17, -.21, -1.4)):
                v = rng.normal(size=M)*.003/freq**2
                L = -(freq**2-1)*v+rng.normal(size=M)*.002
                inputs.append(dict(M=M, N=256, r=.35, w=w, rx=rx, ell=ell,
                                   orientation=orientation, mu=mu, v=v.tolist(), L=L.tolist()))
    run = subprocess.run(['node', '--input-type=module', '-e', SCRIPT, str(args.source_module.resolve())],
                         input=json.dumps(inputs), text=True, capture_output=True, check=True)
    originals = json.loads(run.stdout)
    rows = []
    for p, original in zip(inputs, originals):
        f = MuFreeFields(p['M'], 2, p['N'], False, .01)
        Y = np.r_[original['v'], original['t'], original['L']]
        e = f.evaluate(Y, p['r'], p['w'], p['rx'], p['ell'], True)
        flow_error = float(np.max(abs(e['flow'][0]-original['mixedFlow'])))
        rows.append(dict(parameters={k:v for k,v in p.items() if k not in ('v','L')},
                         original_root_relative=original['rootRelative'],
                         mixed_root_relative=float(e['root_relative'][0]),
                         complete_flow_linf_error=flow_error,
                         gram_linf_error=float(np.max(abs(e['gram'][0].ravel()-original['gram']))),
                         minimum_A=e['minA'], minimum_D=e['minD'], minimum_S=e['minS']))
    report = dict(scope=__doc__, source_module=dict(path=str(args.source_module), sha256=digest(args.source_module)),
                  checker_sha256=digest(__file__), mixed_fields_sha256=digest(Path(__file__).with_name('mu_free_fields.py')),
                  state_generator_seed=551751, rows=rows,
                  maximum_flow_error=max(row['complete_flow_linf_error'] for row in rows),
                  maximum_gram_error=max(row['gram_linf_error'] for row in rows))
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
