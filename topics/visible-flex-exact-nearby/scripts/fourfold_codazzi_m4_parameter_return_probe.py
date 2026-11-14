#!/usr/bin/env python3
"""Two-sided floating m=4 return along the actual separate metric family g_delta.

Each sample is a new exact binary64 parameter object with the same saved
origin/direction. Its target mean E_delta and actual natural graft are
recomputed, and both waist and true regular rotational Jacobi lines are
transported. These samples never alter the already fixed g0 certificates.
"""
from __future__ import annotations
import argparse,copy,json,time
from concurrent.futures import ProcessPoolExecutor,as_completed
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def run_one(task):
    path,label,rtol,atol=task;path=Path(path);start=time.monotonic();ctx.prec=192;ctx.cap=6
    geometry,definition=load_exact_object(path,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,path)
    counts=[0,0]
    def target(r):return body.point(float(r)) if r<=3 else graft.point(float(r))
    def cap_rhs(r,y):
        counts[0]+=1;t=target(r);q=y[0]
        return [4*t['gamma']*(q*q-t['lambda_ref'])+t['beta']*(t['lambda_ref']-1)*q]
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    cap=solve_ivp(cap_rhs,(3.125,.239),[qstar],method='DOP853',rtol=rtol,atol=atol,max_step=.005)
    def waist_rhs(r,y):
        counts[1]+=1;t=body.point(float(r));b,c=y
        return [-2*t['beta']*b+4*t['gamma']*t['lambda_ref']*c,
                4*t['gamma']*b-t['beta']*(t['lambda_ref']+1)*c]
    waist=solve_ivp(waist_rhs,(0.,.239),[0.,1.],method='DOP853',rtol=rtol,atol=atol,max_step=.00025)
    finite=bool(np.all(np.isfinite(cap.y)) and np.all(np.isfinite(waist.y)))
    success=bool(cap.success and waist.success and finite)
    row=dict(label=label,object_path=str(path),object_sha256=sha(path),delta=geometry.delta,
        delta_hex=geometry.delta.hex(),delta_fraction=str(Fraction.from_float(geometry.delta)),
        success=success,cap_message=cap.message,waist_message=waist.message,
        reached_cap_radius=float(cap.t[-1]),reached_waist_radius=float(waist.t[-1]),
        cap_calls=counts[0],waist_calls=counts[1],rtol=rtol,atol=atol,
        true_R74_m4_fee='Exactly zero for this true regular family; lambda_4=-4 omega.',
        target_samples=[target(r) for r in (0.,.239,3.,3.125)],wall_seconds=time.monotonic()-start)
    if success:
        b,c=waist.y[:,-1];q=cap.y[0,-1];f=b+q*c
        row.update(returned_B_sine=float(b),returned_C_cosine=float(c),cap_q4=float(q),
            m4_return_mismatch=float(f),signed_angle_sine=float(f/(np.hypot(b,c)*np.sqrt(1+q*q))))
    return row


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--step',type=float,default=1e-7);ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--rtol',type=float,default=2e-11);ap.add_argument('--atol',type=float,default=2e-13)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a parameter diagnostic')
    original=json.loads(a.object.read_text());center=float.fromhex(original['delta_hex'])
    r74_center=Fraction(-7789866024620307,4611686018427387904);r74_half=Fraction(1,2000000)
    tasks=[];inputs=[]
    for index,label in ((0,'center'),(-1,'minus1'),(1,'plus1'),(-2,'minus2'),(2,'plus2')):
        delta=float(center+index*a.step);exact=Fraction.from_float(delta)
        if not r74_center-r74_half<=exact<=r74_center+r74_half:raise ValueError('sample exceeds actual R74 family')
        definition=copy.deepcopy(original)
        definition.update(delta=delta,delta_hex=delta.hex(),delta_fraction=dict(numerator=str(exact.numerator),denominator=str(exact.denominator)),
            scope='Separate exact affine metric-family input for a floating m4 parameter diagnostic; not a replacement for the fixed g0.',
            construction_note='Same exact frozen origin/direction; only the recorded binary64 affine parameter differs.',
            diagnostic_parent_object_sha256=sha(a.object),diagnostic_sample_label=label)
        path=a.out.with_name(a.out.stem+'-'+label+'-object.json')
        if path.exists():raise FileExistsError('refusing to overwrite parameter input')
        path.write_text(json.dumps(definition,indent=2)+'\n')
        inputs.append(dict(label=label,path=str(path),sha256=sha(path),delta_fraction=str(exact)))
        tasks.append((str(path),label,a.rtol,a.atol))
    report=dict(kind='floating_actual_rotational_m4_two_sided_metric_parameter_return',certified=False,
        source_sha256=sha(__file__),original_object_sha256=sha(a.object),
        original_fixed_metric_certificates_modified=False,origin_sha256=original['origin_inputs']['sha256'],
        direction_sha256=original['direction']['sha256'],requested_step=a.step,workers=a.workers,
        exact_original_delta=str(Fraction.from_float(center)),physical_frequency=4,inputs=inputs,rows=[],
        actual_R74_parameter_interval=[str(r74_center-r74_half),str(r74_center+r74_half)],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py',
            'fourfold_phase_cap_graft_tail_energy.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        complete=False,limitations=['Separate target metric g_delta at each sample; no change to the existing fixed g0 theorem.',
            'Floating finite-primitive and unvalidated ODE outputs only; the finite differences are not directed derivatives.',
            'No nonlinear bifurcation, cap closure, common-metric flex or root existence follows from sampled signs.',
            'All real nonmean/mean regular position conditions still need the full nonlinear reconstruction.'])
    def save():
        report['wall_seconds']=time.monotonic()-started;a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    with ProcessPoolExecutor(max_workers=a.workers) as pool:
        future={pool.submit(run_one,t):t[1] for t in tasks}
        for job in as_completed(future):
            try:row=job.result()
            except Exception as error:row=dict(label=future[job],success=False,error=type(error).__name__+': '+str(error))
            report['rows'].append(row);save()
            print({k:row[k] for k in ('label','success','m4_return_mismatch','wall_seconds') if k in row},flush=True)
    rows={x['label']:x for x in report['rows']};report['complete']=bool(len(rows)==5 and all(x['success'] for x in rows.values()))
    if report['complete']:
        center_row=rows['center'];derivatives=[]
        for j in (1,2):
            lo,hi=rows['minus'+str(j)],rows['plus'+str(j)];delta_span=hi['delta']-lo['delta']
            slope=(hi['m4_return_mismatch']-lo['m4_return_mismatch'])/delta_span
            derivatives.append(dict(radius_index=j,actual_delta_span=delta_span,central_secant=slope,
                sampled_Newton_delta=center-center_row['m4_return_mismatch']/slope if slope else None,
                minus_mismatch=lo['m4_return_mismatch'],plus_mismatch=hi['m4_return_mismatch']))
        report['two_sided_secants']=derivatives
        report['secant_change']=derivatives[1]['central_secant']-derivatives[0]['central_secant']
    save();print(dict(complete=report['complete'],secants=report.get('two_sided_secants'),wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
