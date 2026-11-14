#!/usr/bin/env python3
"""R160 small nonzero parameter/angle-jet check on actual saved inputs."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_cut_material_tail_lifting import (fixed_late_window,cut_material_tail_packet,
    blend_cut_material_lifting)


def common_view(problem,points,angles):
    view=copy.copy(problem);view.x=np.asarray(points,float);view.N=len(points);view.h=np.diff(view.x)
    view.size=view.N*view.q+view.parameter_count;view.work=len(angles)
    f=2*np.arange(view.K+1)
    view.E=np.cos(angles[:,None]*f);view.O=np.sin(angles[:,None]*f[1:])
    view.Ex=-np.sin(angles[:,None]*f)*f;view.Ox=np.cos(angles[:,None]*f[1:])*f[1:]
    view.PE=2*view.E.T/view.work;view.PE[0]*=.5;view.PO=2*view.O.T/view.work
    view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x,coordinate=angles).items()}
    rho=np.asarray(view.geometry.radius(angles),float);rp=np.asarray(view.geometry.radius_derivative(angles),float)
    view.seed=1/rho;view.seed_xi=-rp/rho**2;view._operator_cache={}
    return view


def actual_profile_forcing_jacobian(packet,ops):
    V,Xi=packet['values'],packet['xi']
    P,Xp,Pxi=packet['profile_parameters'],packet['profile_x_parameters'],packet['profile_xi_parameters']
    a=ops['jet']['a'];inv=ops['inv'][...,None];adv=ops['adv'][...,None]
    c=ops['jet']['c'][None,:,None];cp=ops['jet']['c_parameters'][None,:,:]
    invp=-inv*ops['jet']['a_parameters'][None,:,:]/a[None,:,None]
    fn=invp*Xi[:,:,1,None]+inv*Pxi[:,:,1]+cp*(V[:,:,2]-V[:,:,0])[...,None]+c*(P[:,:,2]-P[:,:,0])+adv*Pxi[:,:,0]-Xp[:,:,0]
    fm=invp*Xi[:,:,2,None]+inv*Pxi[:,:,2]-2*cp*V[:,:,1,None]-2*c*P[:,:,1]+adv*Pxi[:,:,1]-Xp[:,:,1]
    return np.stack((fn,fm),axis=2)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('candidate','input','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a new report stem')
    started=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-cut-material-tail-lifting-actual-parameter-check-v1',source=identity(__file__),
        helper=identity(here/'fd2d_gc_cut_material_tail_lifting.py'),input=identity(args.input),
        candidate=identity(args.candidate),completed=False,exception=None,
        nonlinear_BVP_performed=False,actual_old_field_preserved=False,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        old=load_npz(args.input);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong radius input')
        p=PositiveTraceRawBumpDAE(args.candidate,modes=int(old['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256']),radius_floor=.1)
        if str(old['candidate_sha256'])!=report['candidate']['sha256'] or not np.array_equal(old['mesh'],p.x):raise ValueError('Different actual input')
        parameters=old['parameters'];tailp=parameters[p.tail_parameter_slice];delta=parameters[p.profile_parameter_slice]
        points=np.array([.1,.65,1.31,1.36,1.405,1.46,1.48,p.profile.end])
        angles=2*np.pi*(np.arange(64)+.17)/64
        v=common_view(p,points,angles)
        chi,chis=fixed_late_window(points,1.3,p.trace_ramp_stop)
        def evaluate(dp,bp,view=v):
            ops=view.operators(dp);lift=view.lifting(dp,bp)
            cut=cut_material_tail_packet(lift['tail'],view.coords,cut_radius=.8)
            new=blend_cut_material_lifting(lift,cut,chi,chis,operators=ops,
                project_even=view.PE,project_odd=view.PO)
            return new,lift,cut,ops
        packet,previous,cut,ops=evaluate(delta,tailp)
        bdir=.03*np.cos(.2+np.arange(len(tailp))*.71)*tailp*(1.2-tailp)
        ddir=.0003*np.cos(.4+np.arange(len(delta))*.59)
        profile_forcing=actual_profile_forcing_jacobian(packet,ops)
        comparisons=[];eps=1e-5
        for name,db,dd in (('tail',bdir,np.zeros_like(ddir)),('physical_profile',np.zeros_like(bdir),ddir)):
            plus,_,_,_=evaluate(delta+eps*dd,tailp+eps*db)
            minus,_,_,_=evaluate(delta-eps*dd,tailp-eps*db)
            keys=(('values','parameters','profile_parameters'),('x','x_parameters','profile_x_parameters'),
                  ('xi','xi_parameters','profile_xi_parameters'),('forcing_full','forcing_parameters_full',None))
            for key,tkey,pkey in keys:
                pj=profile_forcing if key=='forcing_full' else packet[pkey]
                predicted=packet[tkey]@db+pj@dd
                fd=(plus[key]-minus[key])/(2*eps)
                comparisons.append(dict(direction=name,quantity=key,
                    analytic_maximum=float(np.max(np.abs(predicted))),
                    max_error=float(np.max(np.abs(fd-predicted))),
                    relative_L2=float(np.linalg.norm(fd-predicted)/max(1e-14,np.linalg.norm(predicted)))))
        # Full angular two-jet of the exact cut packet includes the actual
        # U_xi/U_xixi chain, including the nonconstant atlas transition.
        angular_step=1e-6
        cp=cut_material_tail_packet(p.tail(tailp),p.chart.coordinates(points,coordinate=angles+angular_step))
        cm=cut_material_tail_packet(p.tail(tailp),p.chart.coordinates(points,coordinate=angles-angular_step))
        angle_error=float(np.max(np.abs((cp['values']-cm['values'])/(2*angular_step)-cut['xi'])))
        angle2_error=float(np.max(np.abs((cp['xi']-cm['xi'])/(2*angular_step)-cut['xixi'])))
        cut_errors={key:float(np.max(np.abs(packet[key][:,-1]-previous[key][:,-1]))) for key in ('values','xi','parameters','xi_parameters','profile_parameters','profile_xi_parameters')}
        zero_region=float(np.max(np.abs(packet['values'][:,chi==0]-previous['values'][:,chi==0]),initial=0.))
        report.update(definition=packet['cut_material_lifting_definition'],fixed_window=dict(start=1.3,stop=p.trace_ramp_stop),
            physical_points=points.tolist(),angle_count=len(angles),tail_parameter_count=len(tailp),profile_parameter_count=len(delta),
            nonzero_parameter_checks=comparisons,difference_step=eps,
            cut_angular_twojet_check=dict(step=angular_step,first_max_error=angle_error,second_max_error=angle2_error),
            exact_cut_value_and_allowed_parameter_errors=cut_errors,
            cut_radial_II_lifting_change=float(np.max(np.abs(packet['x'][:,-1]-previous['x'][:,-1]))),
            old_lifting_unchanged_where_window_zero=zero_region,
            nonzero_lifting_change=float(np.max(np.abs(packet['values']-previous['values']))),
            material_coordinate_has_nonzero_radial_chain=bool(np.any(v.coords['u_s'][:,chi>0]!=0)),
            source_input_unchanged=identity(args.input)['sha256']==report['input']['sha256'])
        report['completed']=all(row['relative_L2']<2e-5 for row in comparisons) and max(cut_errors.values())<2e-12 and angle2_error<2e-4 and zero_region==0
        save();print(json.dumps(dict(completed=report['completed'],checks=comparisons,cut=cut_errors,
            angular2_error=angle2_error,radial_cut_change=report['cut_radial_II_lifting_change'],
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)
        if not report['completed']:raise SystemExit(1)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise


if __name__=='__main__':main()
