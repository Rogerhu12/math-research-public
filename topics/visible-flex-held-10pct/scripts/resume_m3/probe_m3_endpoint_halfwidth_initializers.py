#!/usr/bin/env python3
"""Compare lambda-one halfwidth designs at the initial-guess level only.

The original shared-C2 restart, affine actual-tail anchor, physical equations
and all original domain tests are used.  There is no BVP or new tail solve.
Changing the protected halfwidth is a physical core design, not fixed-g
refinement or a transfer of the final a=.21 geometric witness.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import _bvp
from couple_m3_smallcut_secant import accepted_anchor
from install_endpoint_c2_restart import install
from m3_raw_diagnostic_model import RawDiagnosticEnvironment, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--halfwidths', type=float, nargs='+', default=[.01,.05,.10,.15,.21])
    p.add_argument('--nodes', type=int, default=257)
    a = p.parse_args(); began = time.monotonic()
    launch = json.loads((a.run/'continuation-command.json').read_text())
    command = launch['command']
    arg = lambda name: command[command.index('--'+name)+1]
    restart = Path(arg('restart'))
    rec = json.loads(gzip.decompress(restart.read_bytes())); accepted_anchor(rec,restart)
    settings = json.loads((a.run/'seed-round-record.json').read_text())['settings']
    if settings['homotopy'] != 1.:
        raise ValueError('This is an exact-circle endpoint design probe')
    profile = json.loads(Path(arg('profile')).read_text())
    chart = json.loads(Path(arg('chart')).read_text())
    port_path = Path(arg('linear-port'))
    port = json.loads(port_path.read_text()); port['_sha256'] = sha(port_path)
    tail_path = a.run/'seed_tail_0002.json.gz'
    tail = json.loads(gzip.decompress(tail_path.read_bytes()))
    if not tail['response']['converged'] or not np.isfinite(tail['response']['residual']):
        raise ValueError('The actual affine tail anchor was not accepted')
    if tail['response']['residual'] >= rec['tail_config']['solveTolerance']:
        raise ValueError('The actual affine tail residual does not pass its original tolerance')
    if chart != rec['chart'] or profile != rec['frozen_profile']:
        raise ValueError('This finite probe requires the recorded same seed profile and chart')
    env = RawDiagnosticEnvironment(Path(arg('source-topic')),Path(arg('short-bridge')),chart,settings)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    install(env.BVP,a.out.with_name(a.out.stem+'-last-seed.json'))
    N, M = int(arg('angular')),int(arg('modes'))
    q = float(arg('amplitude'))
    rows=[]
    for halfwidth in a.halfwidths:
        chosen={**settings,'halfwidth':halfwidth}
        obj=env.make(chosen,profile,port,q,M,N,False,float(arg('warp-reference')))
        obj.restart_remesh=a.nodes
        obj.bcweights=np.full(M,float(arg('physical-bc-tol'))/float(arg('bc-tol')))
        row=dict(halfwidth=halfwidth,core_settings=chosen)
        try:
            t,y,par=obj.restart(restart);obj.initial(par);f=obj.flow(par[0])
            H0=np.asarray(tail['request']['height'])
            H=obj.bridge.sigma*obj.q*y[obj.iz:,-1]
            if not np.array_equal(H,H0):
                raise ValueError('The initial tail height is not the exact actual anchor')
            obj.tail=env.coupler.AffineTailForInnerBVP(H0,tail['response'],M)
            h=np.diff(t)
            col,middle,rhs,rhs_middle=_bvp.collocation_fun(obj.fun,y,par,t,h)
            spline=_bvp.create_spline(y,rhs,t,h)
            rms=_bvp.estimate_rms_residuals(obj.fun,spline,t,h,par,1.5*col/h,rhs_middle)
            minimum=1.
            for xx,yy in ((t,y),((t[:-1]+t[1:])/2,middle)):
                physical,_=obj.chart(xx,par[0])
                for first in range(0,len(xx),32):
                    sl=slice(first,first+32)
                    minimum=min(minimum,float(np.min(f.frame(physical[sl],obj.q*yy[:,sl])['margin'].real)))
            row.update(original_initial_domain_passed=True,nodes=len(t),
                original_collocation_rms=float(np.max(rms)),
                collocation_residual_max=float(np.max(abs(col))),
                boundary_residual=float(np.max(abs(obj.bc(y[:,0],y[:,-1],par)))),
                sampled_min_frenet_margin=minimum,initial_rho_lower=obj._core.rho_lower,
                actual_q=obj.support_amplitude,delta=float(par[0]+profile['delta']),
                physical_controls=(par[1:]*obj.pscale).tolist(),
                tail_height_identical_to_actual_anchor=True)
        except (FloatingPointError,ValueError) as error:
            row.update(original_initial_domain_passed=False,error=str(error))
        rows.append(row);print(json.dumps(row),flush=True)
    output=dict(scope=__doc__,command=sys.argv,seconds=time.monotonic()-began,
        source_sha256={**env.sources,str(Path(__file__).resolve()):sha(__file__),
            str(Path(__file__).with_name('install_endpoint_c2_restart.py').resolve()):
                sha(Path(__file__).with_name('install_endpoint_c2_restart.py'))},
        actual_seed_checkpoint=dict(path=str(restart.resolve()),sha256=sha(restart)),
        actual_affine_tail_anchor=dict(path=str(tail_path.resolve()),sha256=sha(tail_path),
            residual=tail['response']['residual']),
        coefficient_chunks={str(f.resolve()):sha(f) for f in sorted(
            restart.parent.glob(restart.name.split('.')[0]+'_coeff_*.npy.gz'))},
        primary_transition=settings['transition'],control_transition=settings['control_transition'],
        q_gauge=q,warp_reference=float(arg('warp-reference')),modes=M,angular=N,
        initial_nodes_argument=a.nodes,rows=rows,
        boundary='Only finite initial guesses have been compared. A smaller halfwidth '
            'changes the exact core and has no inherited a=.21 holding witness. '
            'No predictor, BVP, actual tail, physical profile, or running source was changed.')
    a.out.write_text(json.dumps(output,indent=2)+'\n')


if __name__=='__main__':
    main()
