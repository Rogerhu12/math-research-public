#!/usr/bin/env python3
"""Recovered implementation check for the raw P1 three-field reader.

No BVP is solved. A bound real saved field is compared with its raw provider,
then the independent fixed-u frame/two-jet ODE is checked on an exact flat tail.
A named synthetic positive-clock fixture checks the alternative factory only;
it is not a compatible prefix or a new research candidate.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_gc_raw_native_field import (RawLiftedNativeField,load_arrays,
    curvature_second_y,pack_body_state,body_rhs_from_fields,actual_body_twojet)
from fd2d_flat_developable_tail import FlatDevelopableTail
from fd2d_flat_developable_family import FlatDevelopableFamily

HERE=Path(__file__).resolve().parent
TOP=HERE.parent


def identity(path):
    p=Path(path);raw=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def maximum(x):
    return float(np.max(np.abs(x),initial=0.))


def relative(x,y):
    return maximum((np.asarray(x)-np.asarray(y))/(1+np.abs(y)))


def probe(reader,prefix):
    nodes=reader.nodes
    selected=np.unique(np.linspace(0,len(nodes)-2,7,dtype=int))
    center=(nodes[selected]+nodes[selected+1])/2
    x=center[:,None]
    xi=(2*np.pi*(np.arange(19)+.137)/19)[None,:]
    q=reader.evaluate_native(x,xi)
    angular=[]
    for h in (2e-5,1e-5,5e-6):
        plus=reader.evaluate_native(x,xi+h);minus=reader.evaluate_native(x,xi-h)
        row=dict(step=h)
        for name in ('n','m','l'):
            row[name+'_first_relative']=relative((plus[name]-minus[name])/(2*h),q[name+'_xi'])
            row[name+'_second_relative']=relative((plus[name]-2*q[name]+minus[name])/h**2,q[name+'_xixi'])
            row[name+'_mixed_relative']=relative((plus[name+'_x']-minus[name+'_x'])/(2*h),q[name+'_x_xi'])
        angular.append(row)
    h=(nodes[selected+1]-nodes[selected])[:,None]*1e-4
    xp=reader.evaluate_native(x+h,xi);xm=reader.evaluate_native(x-h,xi)
    radial={name:relative((xp[name]-xm[name])/(2*h),q[name+'_x']) for name in ('n','m','l')}
    endpoints=nodes[1:-1,None];angles=xi[:,:7]
    left=reader.evaluate_native(endpoints,angles,side='left')
    right=reader.evaluate_native(endpoints,angles,side='right')
    continuity={name+suffix:maximum(left[name+suffix]-right[name+suffix])
        for name in ('n','m','l') for suffix in ('','_xi','_xixi')}
    target_u=2*np.pi*(np.arange(23)+.19)/23
    physical=reader.physical(center[:,None],target_u[None,:])
    definition=Path(str(prefix)+'-definition.json')
    definition.write_text(json.dumps(reader.definition(),indent=2)+'\n')
    restored=RawLiftedNativeField.from_definition(definition)
    repeated=restored.evaluate_native(x,xi)
    roundtrip={name:maximum(repeated[name]-q[name]) for name in ('n','m','l')}
    return dict(definition=identity(definition),angular_derivatives=angular,
        radial_derivatives=radial,shared_node_continuity=continuity,
        definition_roundtrip=roundtrip,
        inverse_angle_error=maximum(physical['angle_inverse_error']),
        scope='Floating implementation checks at specified points, not continuous residual bounds')


def exact_tail_body_check():
    tail=FlatDevelopableTail(amplitude=.9,quadrature_order=96)
    family=FlatDevelopableFamily([.9],cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)
    angles=2*np.pi*(np.arange(24)+.173)/24
    sn,cs=np.sin(angles),np.cos(angles)
    v=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
    vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
    vuu=np.stack((-2*(cs*cs-sn*sn),4*sn*cs,2*(cs*cs-sn*sn)),axis=-1)
    def field(x):
        radius=.8-x;y=radius*sn;yu=radius*cs;yuu=-radius*sn
        c=family.angle_jets(y)
        k,ky=np.asarray(c['kappa']),np.asarray(c['kappa_y'])
        kyy=curvature_second_y(family,y,'signed_bubble')
        val=k[:,None]*v
        first=(ky*yu)[:,None]*v+k[:,None]*vu
        second=(kyy*yu*yu+ky*yuu)[:,None]*v+2*(ky*yu)[:,None]*vu+k[:,None]*vuu
        return val,first,second
    initial=tail.evaluate(.8,angles)
    val,first,_=field(0.)
    F=np.stack((initial['e1'],initial['e2'],initial['N']),axis=-1)
    r=np.stack((.8*val[:,0],-.8*val[:,1],-np.ones(len(angles))),axis=-1)
    b=np.zeros_like(r);b[:,1]=.8
    ru=np.stack((.8*first[:,0],-.8*first[:,1],np.zeros(len(angles))),axis=-1)
    state=pack_body_state(initial['X'],F,r,b,ru,np.zeros_like(r))
    def rhs(x,y):
        val,first,second=field(x)
        return body_rhs_from_fields(y.reshape(len(angles),24),J=1.,
            l=val[:,2],m=val[:,1],l_u=first[:,2],m_u=first[:,1],
            l_uu=second[:,2],m_uu=second[:,1]).ravel()
    sample=np.array([0.,.07,.19,.31,.48])
    solution=solve_ivp(rhs,(0.,.48),state.ravel(),method='DOP853',
        rtol=2e-11,atol=2e-12,max_step=.01,t_eval=sample)
    if not solution.success:raise RuntimeError(solution.message)
    rows=[]
    for j,x in enumerate(sample):
        truth=tail.evaluate(.8-x,angles)
        val,_,_=field(x)
        actual=actual_body_twojet(solution.y[:,j].reshape(len(angles),24),a=.8-x,l=val[:,2])
        errors={key:maximum(actual[key]-truth[key]) for key in ('X','X_s','X_u','X_ss','X_su','X_uu')}
        rows.append(dict(x=float(x),errors=errors,
            metric_error=maximum(actual['metric_relative_operator_error']),
            frame_error=maximum(actual['frame_orthogonality_error'])))
    return dict(angles=len(angles),u_formula='2*pi*(j+.173)/24, j=0,...,23',
        amplitude=.9,method='DOP853',rtol=2e-11,atol=2e-12,max_step=.01,
        success=bool(solution.success),nfev=solution.nfev,rows=rows,
        scope='Independent actual frame/two-jet implementation check on the explicit R128 tail')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--arrays',type=Path,default=TOP/'notes/2026-11-12-fd2d-root-flat-dae-jac01-initial.npz')
    p.add_argument('--candidate',type=Path,default=TOP/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    p.add_argument('--mesh-step',type=float,default=.06)
    p.add_argument('--profile-kind',choices=('legacy_coast','positive_clock'),default='legacy_coast')
    p.add_argument('--tail-kind',choices=('signed_bubble','positive_bernstein'),default='signed_bubble')
    p.add_argument('--out-prefix',type=Path,default=TOP/'notes/2026-11-12-fd2d-metric-raw-native-field-check-recovery01')
    args=p.parse_args()
    report_path=Path(str(args.out_prefix)+'-report.json')
    if report_path.exists():raise FileExistsError('Use a new output stem')
    report_path.parent.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();saved=load_arrays(args.arrays)
    K=(saved['corrections'].shape[1]-2)//3
    problem=RawLiftedDAE(args.candidate,modes=K,max_step=args.mesh_step,gap=.9,
        profile_kind=args.profile_kind,tail_kind=args.tail_kind)
    if not np.array_equal(problem.x,saved['mesh']):
        raise ValueError('Input uses a different actual radial mesh; select the recorded mesh-step/chart')
    reader=RawLiftedNativeField(args.arrays,args.candidate,reference_T=problem.profile.reference_T,
        blend_interval=problem.blend,profile_kind=args.profile_kind,tail_kind=args.tail_kind,
        geometry=problem.geometry)
    vector=np.r_[saved['corrections'].ravel(),saved['parameters']]
    _,data=problem.evaluate(vector)
    xi=np.asarray(problem.chart.theta,float)
    actual=reader.evaluate_native(problem.x[None,:],xi[:,None])
    comparisons={name:relative(actual[name],data['fields'][:,:,j])
        for j,name in enumerate(('n','m','l'))}
    first=probe(reader,Path(str(args.out_prefix)+'-bound-input'))
    # This separately named fixture selects the positive factory and does not
    # claim compatibility of unchanged arbitrary corrections.
    synthetic_parameters=saved['parameters'].copy()
    synthetic_parameters[K:-1]=np.linspace(.9,1.1,K+1)
    synthetic_parameters[-1]=min(.11,.6*problem.profile.model.Tmax)
    fixture=Path(str(args.out_prefix)+'-synthetic-positive-fixture.npz')
    np.savez_compressed(fixture,mesh=saved['mesh'],corrections=saved['corrections'],
        parameters=synthetic_parameters)
    positive=RawLiftedNativeField(fixture,args.candidate,reference_T=problem.profile.reference_T,
        blend_interval=problem.blend,profile_kind='positive_clock',tail_kind='positive_bernstein',
        geometry=problem.geometry)
    second=probe(positive,Path(str(args.out_prefix)+'-synthetic-positive'))
    second['fixture']=identity(fixture)
    second['synthetic_only_not_BVP']=True
    body=exact_tail_body_check()
    identity_files=[__file__,HERE/'fd2d_gc_raw_native_field.py',HERE/'fd2d_gc_three_field_residual.py',
        HERE/'fd2d_gc_raw_lifted_dae.py',HERE/'fd2d_flat_developable_tail.py']
    checks=dict(node_provider_relative_error=max(comparisons.values())<5e-11,
        shared_node_values_and_angular_jets=all(max(q['shared_node_continuity'].values())==0. for q in (first,second)),
        definition_roundtrip=all(max(q['definition_roundtrip'].values())==0. for q in (first,second)),
        monotone_inverse=all(q['inverse_angle_error']<5e-12 for q in (first,second)),
        flat_actual_twojet=max(max(r['errors'].values()) for r in body['rows'])<2e-7,
        flat_actual_metric=max(r['metric_error'] for r in body['rows'])<2e-8)
    report=dict(schema='fd2d-raw-native-reader-check-recovery-v1',
        sources=[identity(z) for z in identity_files],candidate=identity(args.candidate),
        arrays=identity(args.arrays),modes=K,nodes=len(saved['mesh']),
        explicit_factory=dict(profile_kind=args.profile_kind,tail_kind=args.tail_kind),
        provider_node_comparison=comparisons,bound_input_probe=first,
        synthetic_positive_probe=second,actual_flat_body=body,
        implementation_checks=checks,implementation_checks_passed=all(checks.values()),
        elapsed_seconds=time.monotonic()-started,
        no_new_BVP_solve=True,no_surface_or_residual_certificate=True,
        recovery='This report exists only if this reconstructed source actually ran; old missing reports are not replayed.')
    report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(report_path),checks=checks,complete=True,
        elapsed_seconds=report['elapsed_seconds'])),flush=True)
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())
