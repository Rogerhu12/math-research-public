#!/usr/bin/env python3
"""Same-g .997 warm solve with .995 moving-frame fast-Schur terminal rows.

Only the terminal 109-row definition changes.  This is a new finite BVP,
not an exact nonlinear tail DN condition and not a closed surface.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from scipy.linalg import eigvals, solve

TOPIC=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(TOPIC/'scripts'))
import parallel_20261117_continue_inward as inward

HELPER=Path(__file__).with_name('2026-11-17-parallel-geometry-frenet-schur.py')
spec=importlib.util.spec_from_file_location('moving_frame_schur',HELPER)
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(args):
    if args.duration!=0 or args.boundary_input is None:
        raise ValueError('This comparison requires duration zero and an explicit earlier boundary reference')
    warm=json.loads(gzip.decompress(args.input.read_bytes()))
    reference=json.loads(gzip.decompress(args.boundary_input.read_bytes()))
    if not warm.get('inward_scalar_profile') or not warm.get('success') or not reference.get('success'):
        raise ValueError('Need an accepted inward warm field and an accepted reference')
    if warm['M']!=reference['M'] or warm['N']!=reference['N']:
        raise ValueError('This comparison keeps the finite M/N definition fixed')
    metadata={}
    def projector(q,y,profile,s,fixed):
        z=inward.solver.physical(q,y,profile,s)
        T,Ts=helper.moving_frame_map(q,z)
        B=solve(T.T,(T@z['J']+Ts).T).T
        ev=eigvals(B);re=np.sort(ev.real);count=q.M-fixed
        lower,upper=float(re[-count-1]),float(re[-count])
        if upper-lower<=1e-8:
            raise ValueError('No separated real-part threshold at the required dimension')
        threshold=(lower+upper)/2
        diagnostics,LB=helper.selected_left(B,lambda x:x>threshold,q.M,None)
        if diagnostics['dimension']!=count:
            raise ValueError('Cannot split a conjugate pair to force the boundary count')
        L=LB@T
        metadata.update(reference_endpoint=float(s),M=q.M,N=q.N,fixed_modes=fixed,
                        real_growth_threshold=threshold,selection_real_gap=upper-lower,
                        T_condition_2=float(np.linalg.cond(T)),rows_condition_2=float(np.linalg.cond(L)),
                        schur={k:v for k,v in diagnostics.items() if k!='modal_energy'})
        print(json.dumps(dict(event='moving_schur_terminal_ready',**metadata)),flush=True)
        return L,z
    inward.solver.projector=projector
    inward.main(args)
    result=json.loads(gzip.decompress(args.out.read_bytes()))
    result['terminal_projector']='moving_actual_frame_fast_real_Schur_at_explicit_reference_Taylor2_target'
    result['moving_frame_schur_boundary']=dict(
        scope=__doc__,driver_sha256=sha(__file__),helper_sha256=sha(HELPER),
        input_sha256=sha(args.input),reference_sha256=sha(args.boundary_input),
        method='T=P_M(deltaF.es,deltaF.ephi,deltaF.n); B=(T A+T_s)T^-1; L=Qfast.T T',
        target='L@(y_reference+dt*rhs_reference+0.5*dt**2*second_reference)',
        exact_tail_DN=False,**metadata)
    args.out.write_bytes(gzip.compress((json.dumps(result)+'\n').encode(),mtime=0))
    print(json.dumps(dict(event='moving_schur_result_bound',success=result['success'],
                         output_sha256=sha(args.out),output=str(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--boundary-input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--duration',type=float,default=0.)
    p.add_argument('--step',type=float,default=.00025)
    p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--tol',type=float,default=1e-8)
    p.add_argument('--max-nodes',type=int,default=1800)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    p.set_defaults(modes=None,angles=None,core_first=None,curvature=None,ramp=.02)
    main(p.parse_args())
