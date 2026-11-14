#!/usr/bin/env python3
"""Resume a frozen finite Codazzi candidate near a target turning root.

Floating diagnostic only.  The two-field formula itself does not divide by
K0; this probe records K0 crossing zero independently of the C denominator.
No hyperbolic energy estimate is asserted on the positive-curvature side.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_evolution_probe import Evolution,diagnose


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--state-in',type=Path,required=True);p.add_argument('--right',type=float,required=True)
    p.add_argument('--samples',type=int,default=45);p.add_argument('--max-step',type=float,default=.0001)
    p.add_argument('--rtol',type=float,default=3e-10);p.add_argument('--atol',type=float,default=3e-12)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--state',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();last_progress=started
    original=np.load(args.state_in,allow_pickle=False);metadata=json.loads(str(original['metadata']))
    if metadata['object_sha256']!=sha(args.object):raise ValueError('different initial object')
    left=float(original['r']);state=original['state'];N=len(state)
    if not left<args.right:raise ValueError('forward continuation required')
    geometry,definition=load_exact_object(args.object,512);evolution=Evolution(geometry,N,2)
    solver=DOP853(evolution.evaluate,left,state.ravel(),args.right,
        rtol=args.rtol,atol=args.atol,max_step=args.max_step)
    grid=np.linspace(left,args.right,args.samples);next_sample=1;rows=[]
    def row_at(r,y):
        row=diagnose(evolution,r,y);target=scalar_target(geometry,r)
        row['target_K']=target['K'];row['target_minus_K_derivative']=target['minus_K_x']
        row['strictly_negative_target']=bool(target['K']<0)
        return row
    rows.append(row_at(left,state.ravel()));status='running';exception=None
    try:
        while solver.status=='running':
            message=solver.step()
            if solver.status=='failed':status='integrator_failed: '+str(message);break
            dense=solver.dense_output()
            while next_sample<len(grid) and grid[next_sample]<=solver.t:
                r=float(grid[next_sample]);rows.append(row_at(r,dense(r)));next_sample+=1
            check=evolution.evaluate(solver.t,solver.y,True)
            if check['minimum_abs_n']<.02:status='angular_second_form_denominator_gate';break
            if evolution.calls>50000:status='diagnostic_rhs_limit';break
            now=time.monotonic()
            if now-last_progress>20:
                target=scalar_target(geometry,solver.t)
                print({'r':solver.t,'K0':target['K'],'min_abs_C':check['minimum_abs_n'],'rhs':evolution.calls},flush=True);last_progress=now
        if solver.status=='finished':status='finished'
    except Exception as exc:status='diagnostic_exception';exception=repr(exc)
    if rows[-1]['r']!=float(solver.t):
        try:rows.append(row_at(float(solver.t),solver.y))
        except Exception as exc:exception=(exception or '')+' endpoint: '+repr(exc)
    np.savez_compressed(args.state,r=solver.t,state=solver.y.reshape(N,14),columns=original['columns'],
        metadata=np.array(json.dumps({'kind':'floating_dealiased_Codazzi_endpoint','object_sha256':sha(args.object),'source_sha256':sha(__file__),'parent_state_sha256':sha(args.state_in)})))
    doc=dict(kind='floating_Codazzi_turning_continuation',complete=status=='finished',certified=False,status=status,exception=exception,
        source_sha256=sha(__file__),parent_state_sha256=sha(args.state_in),parent_state_path=str(args.state_in),
        object_sha256=sha(args.object),origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_center_parameter=definition['delta_fraction'],angular_grid=N,nonlinear_grid=2*N,primitive_nodes=512,
        original_target_fixed=True,mean_retained=True,whole_parameter_interval=False,whole_real_angular_circle=False,whole_radial_domain=False,
        requested_radial_interval=[left,args.right],finished_radial_interval=[left,float(solver.t)],
        rtol=args.rtol,atol=args.atol,max_step=args.max_step,rows=rows,
        sampled_minimum_abs_C=min(row['minimum_abs_n'] for row in rows),
        sampled_K_range=[min(row['target_K'] for row in rows),max(row['target_K'] for row in rows)],
        sampled_source_max=max(row['updated_source_C0'] for row in rows),
        sampled_metric_defect_max=max(row['updated_metric_defect_C0'] for row in rows),
        endpoint_state_path=str(args.state),endpoint_state_sha256=sha(args.state),rhs_calls=evolution.calls,
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_local_correction_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        wall_seconds=time.monotonic()-started,
        limitations=['Finite Fourier, sampled, floating continuation only; the initial endpoint already has unvalidated errors.',
            'No time/roundoff/alias/infinite-tail bound or whole-eta enclosure.',
            'When K0 reaches zero the strictly hyperbolic symmetrizer degenerates even if C stays nonzero.',
            'Positive-K0 continuation is not covered by the negative-curvature energy framework. No global cap closure is claimed.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({k:doc[k] for k in ('status','finished_radial_interval','sampled_K_range','sampled_minimum_abs_C','sampled_source_max','sampled_metric_defect_max','wall_seconds')},flush=True)


if __name__=='__main__':main()
