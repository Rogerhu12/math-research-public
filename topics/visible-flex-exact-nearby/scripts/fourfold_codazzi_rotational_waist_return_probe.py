#!/usr/bin/env python3
"""Actual fixed-target rotational Jacobi waist-to-regular mismatch.

The positive-cap graph is consumed from its explicitly floating diagnostic.
This producer integrates all requested true physical mode columns from the
closed planar waist condition B(0)=0, C_mode(0)=1, retaining the scalar mean
as a separate position/holonomy slot.  No interval or nonlinear claim follows.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-cap-Jacobi-floating.json'))
    ap.add_argument('--primitive-nodes',type=int,default=512)
    ap.add_argument('--rtol',type=float,default=2e-11);ap.add_argument('--atol',type=float,default=2e-13)
    ap.add_argument('--max-step',type=float,default=.00025)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a diagnostic')
    cap=json.loads(a.cap.read_text())
    if not cap['success'] or cap['object_sha256']!=sha(a.object):raise ValueError('incompatible positive-cap input')
    modes=np.array([x['physical_frequency'] for x in cap['entries']],dtype=float)
    q=np.array([x['q'] for x in cap['entries']]);right=float(cap['endpoint_radius']);n=len(modes)
    if not np.array_equal(modes,4*np.arange(1,n+1)) or not np.all(q>0):raise ValueError('invalid physical graph modes')
    geometry,definition=load_exact_object(a.object,a.primitive_nodes);target=RotationalBodyTarget(geometry)
    calls=0
    def rhs(r,y):
        nonlocal calls
        t=target.point(float(r));calls+=1;b,c=y.reshape(2,n)
        return np.r_[-2*t['beta']*b+t['gamma']*modes*t['lambda_ref']*c,
                     t['gamma']*modes*b-t['beta']*(t['lambda_ref']+1)*c]
    sol=solve_ivp(rhs,(0.,right),np.r_[np.zeros(n),np.ones(n)],method='DOP853',
        rtol=a.rtol,atol=a.atol,max_step=a.max_step)
    b,c=sol.y[:,-1].reshape(2,n);finite=np.all(np.isfinite(sol.y))
    success=bool(sol.success and finite)
    entries=[]
    if success:
        mismatch=b+q*c;norm=np.hypot(b,c)
        for m,bb,cc,qq,ff,nn in zip(modes,b,c,q,mismatch,norm):
            entries.append(dict(physical_frequency=int(m),waist_C_cosine_amplitude=1.,
                returned_B_sine=float(bb),returned_C_cosine=float(cc),cap_q=float(qq),
                true_regular_linear_mismatch=float(ff),
                mismatch_over_column_norm=float(ff/nn),
                signed_angle_sine=float(ff/(nn*np.sqrt(1+qq*qq))),
                column_euclidean_norm=float(nn)))
    report=dict(kind='floating_actual_fixed_target_rotational_waist_regular_return',certified=False,
        success=success,source_sha256=sha(__file__),object_sha256=sha(a.object),
        cap_input_path=str(a.cap),cap_input_sha256=sha(a.cap),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],
        requested_interval=[0.,right],reached_radius=float(sol.t[-1]),rhs_calls=calls,accepted_steps=len(sol.t)-1,
        primitive_nodes=a.primitive_nodes,rtol=a.rtol,atol=a.atol,max_step=a.max_step,
        solver_message=sol.message,finite_state=bool(finite),entries=entries,
        initial_geometric_condition='Linearized B(0)=0 and C mean fixed at -1/a0; nonmean C columns are independently normalized.',
        regular_mean_height='Retained separate axial translation; no forced mean flux or mean holonomy is solved.',
        body_target_fixed=True,actual_positive_cap_graph_used=True,whole_affine_parameter_interval=False,
        whole_radial_interval=False,complete_primitive_tail=False,whole_real_angular_circle=False,
        nonlinear_waist_branch_matched=False,closed_surface_complete=False,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_phase_symmetric_geometry.py',
            'fourfold_phase_geometry.py','fourfold_phase_local_correction_probe.py')},
        limitations=['Finite primitive and floating IVP integration only; no interval lower bound for the displayed mismatch.',
            'The positive-cap input is its floating stable-center representative; native propagation independently pays the true R74 fee.',
            'These are the rotational reference linear modes, not the nonlinear Cauchy branch or a full contact inverse.',
            'Only the listed physical modes are computed; no conclusion for omitted modes or changes of the fixed metric.'],
        wall_seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(success=success,entries=entries[:8],wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
