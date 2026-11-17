#!/usr/bin/env python3
"""True short IVP nodes and a common-two-jet C2 quintic geometry reader.

This is a local candidate only: no complete BVP, C2 join to the old prefix,
global flex, continuous interval certificate, or reach result is claimed.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853

BASE=Path(__file__).with_name('2026-11-17-parallel-geometry-short-ivp-refine.py')
spec=importlib.util.spec_from_file_location('frozen_ivp_refine',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
h=base.h
lift=base.base.lift_states


def nodal_field(args,ref,metric,N):
    profile=h.profile_from(metric);M=args.modes
    q=h.Frenet(M,N);old=h.Frenet(ref['M'],ref['N'])
    start=float(ref['mesh'][-1]);initial=np.asarray(ref['states'][-1])
    y0=lift(initial,old.M,M)
    a,ap,app=profile(start);k=ap/a
    old_v=old.rhs(initial,k)
    old_acc=old.jvp(initial,k,old_v,dk=app/a-k*k)
    def rhs(s,y):
        aa,ap1,_=profile(float(s));return q.rhs(y,ap1/aa)
    solver=DOP853(rhs,start,y0,args.end,rtol=args.rtol,atol=args.atol,
                  max_step=args.max_step,first_step=min(args.max_step,args.end-start))
    mesh=[start];states=[y0.copy()]
    while solver.status=='running':
        try:
            message=solver.step()
        except FloatingPointError as error:
            return dict(ivp_reached_end=False,last_accepted_time=mesh[-1],
                        domain_evaluation_error=str(error),nfev=solver.nfev),None
        if solver.status!='failed':
            mesh.append(float(solver.t));states.append(solver.y.copy())
    if solver.status!='finished':
        return dict(ivp_reached_end=False,last_accepted_time=mesh[-1],message=message),None
    integrator_nodes=len(mesh);dropped=[]
    terminal_threshold=64*abs(np.spacing(float(args.end)))
    if not args.keep_terminal_microcells:
        while len(mesh)>2 and mesh[-1]-mesh[-2]<terminal_threshold:
            dropped.append(mesh[-2]);del mesh[-2];del states[-2]
    velocities=[];accelerations=[]
    for s,y in zip(mesh,states):
        aa,ap1,app1=profile(s);kk=ap1/aa
        v=q.rhs(y,kk)
        velocities.append(v)
        accelerations.append(q.jvp(y,kk,v,dk=app1/aa-kk*kk))
    data=dict(schema='local-short-ivp-common-jets-v1',scope=__doc__,
        ivp_reached_end=True,bvp_accepted=False,complete_prefix=False,
        old_prefix_C2_join_completed=False,M=M,N=N,start=start,end=args.end,
        max_step=args.max_step,rtol=args.rtol,atol=args.atol,nfev=solver.nfev,
        integrator_accepted_nodes=integrator_nodes,
        reconstruction_node_policy='keep true endpoint; remove only penultimate nodes within 64 ulp' if not args.keep_terminal_microcells else 'keep all integrator nodes',
        terminal_microcell_threshold=terminal_threshold,dropped_terminal_node_times=dropped,
        mesh=mesh,states=np.asarray(states).tolist(),rhs=np.asarray(velocities).tolist(),
        d2=np.asarray(accelerations).tolist(),
        original_core_coefficients=np.pad(np.asarray(ref['core']['coefficients']),(0,M-old.M)).tolist(),
        old_cut_jets=dict(value=y0.tolist(),first=lift(old_v,old.M,M).tolist(),
                          second=lift(old_acc,old.M,M).tolist()),
        fixed_scalar_profile=ref['fixed_scalar_profile'],
        analytic_extension_origin=ref['analytic_extension_origin'],
        inward_scalar_profile=metric['inward_scalar_profile'],
        inward_profile_sha256=metric['inward_profile_sha256'],
        reference_sha256=h.sha(args.reference),metric_carrier_sha256=h.sha(args.metric),
        source_sha256=h.sha(__file__),base_sha256=h.sha(BASE))
    path=Path(str(args.output_stem)+f'-n{N}.json.gz')
    path.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))
    report=dict(ivp_reached_end=True,N=N,nodes=len(mesh),nfev=solver.nfev,
                integrator_nodes=integrator_nodes,dropped_terminal_node_times=dropped,
                field_path=str(path),field_sha256=h.sha(path))
    print(json.dumps(dict(event='local_nodal_field_ready',**report)),flush=True)
    return report,data


def read_field(data,profile,angles,subdivisions):
    q=h.Frenet(data['M'],angles)
    x=np.asarray(data['mesh']);ys=np.asarray(data['states'])
    dy=np.asarray(data['rhs']);ddy=np.asarray(data['d2'])
    core=np.asarray(data['original_core_coefficients'])
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core)
    cp,sp=np.cos(q.angle),np.sin(q.angle);major=1+sum(core)
    worst=dict(value=0.);curvature=dict(value=0.)
    minimum=dict(Q=float('inf'),W=float('inf'),H=float('inf'),Gram_determinant=float('inf'))
    witness=float('inf');normmax=0.;points=0
    for i,length in enumerate(np.diff(x)):
        c0=ys[i];c1=length*dy[i];c2=length*length*ddy[i]/2
        aa=ys[i+1]-c0-c1-c2;bb=length*dy[i+1]-c1-2*c2
        cc=length*length*ddy[i+1]-2*c2
        coef=np.array([c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2])
        first=np.arange(1,6)[:,None]*coef[1:]
        second=(np.arange(2,6)*np.arange(1,5))[:,None]*coef[2:]
        for u in np.linspace(0,1,subdivisions+1):
            s=x[i]+u*length
            y=np.polynomial.polynomial.polyval(u,coef)
            v=np.polynomial.polynomial.polyval(u,first)/length
            acc=np.polynomial.polynomial.polyval(u,second)/(length*length)
            F,d,e=q.jet(y);V,dV,_=q.jet(v);Acc,_,_=q.jet(acc)
            aa,ap,_=profile(float(s));kk=ap/aa
            E=np.sum(V*V,axis=1);C=np.sum(V*d,axis=1);G=np.sum(d*d,axis=1)
            er=E-1;gr=G/(aa*rho)**2-1;cr=C/(aa*rho)
            error=(abs(er+gr)+np.sqrt((er-gr)**2+4*cr*cr))/2
            j=int(np.argmax(error))
            if error[j]>worst['value']:
                worst=dict(value=float(error[j]),s=float(s),angle=float(q.angle[j]),cell=i,u=float(u),
                           rr=float(er[j]),mixed=float(cr[j]),angular=float(gr[j]))
            normal=np.cross(V,d);area=np.linalg.norm(normal,axis=1);normal/=area[:,None]
            bss=np.sum(Acc*normal,axis=1);bst=np.sum(dV*normal,axis=1);btt=np.sum(e*normal,axis=1)
            determinant=E*G-C*C
            if np.min(determinant)<=0:raise FloatingPointError('Actual quintic Gram is not positive definite')
            trace=(bss*G+btt*E-2*bst*C)/determinant
            gauss=(bss*btt-bst*bst)/determinant
            kmax=(abs(trace)+np.sqrt(np.maximum(0,trace*trace-4*gauss)))/2
            j=int(np.argmax(kmax))
            if kmax[j]>curvature['value']:
                curvature=dict(value=float(kmax[j]),s=float(s),angle=float(q.angle[j]),cell=i,u=float(u))
            W=np.sum(np.cross(d,e)**2,axis=1);H=W-kk*kk*G**3
            for name,value in [('Q',G),('W',W),('H',H),('Gram_determinant',determinant)]:
                minimum[name]=min(minimum[name],float(np.min(value)))
            normmax=max(normmax,float(np.max(np.linalg.norm(F,axis=1))))
            X=cp*F[:,0]-sp*F[:,1];Y=sp*F[:,0]+cp*F[:,1]
            witness=min(witness,float(np.min(np.sqrt(X*X+(Y-major)**2+F[:,2]**2))))
            points+=angles
    delta_v=dy[0]-np.asarray(data['old_cut_jets']['first'])
    delta_a=ddy[0]-np.asarray(data['old_cut_jets']['second'])
    return dict(read_angles=angles,radial_subdivisions=subdivisions,quintic_cells=len(x)-1,
        sampled_points=points,max_sample_relative_Gram_operator=worst,
        max_sample_principal_curvature=curvature,minimum_sample_domain=minimum,
        max_sample_position_norm=normmax,minimum_sample_core_witness_distance=witness,
        core_major=float(major),core_rho_min_sample=float(rho.min()),
        old_cut_velocity_jump_sample=float(np.max(np.linalg.norm(q.jet(delta_v)[0],axis=1))),
        old_cut_acceleration_jump_sample=float(np.max(np.linalg.norm(q.jet(delta_a)[0],axis=1))))


def main(args):
    ref=json.loads(gzip.decompress(args.reference.read_bytes()))
    metric=json.loads(gzip.decompress(args.metric.read_bytes()))
    if not ref.get('success') or not metric.get('inward_scalar_profile'):
        raise ValueError('Need genuine accepted cut and explicit inward scalar')
    out=dict(scope=__doc__,source_sha256=h.sha(__file__),reference_sha256=h.sha(args.reference),
             metric_sha256=h.sha(args.metric),M=args.modes,fields=[])
    fields=[]
    for N in args.angles:
        report,data=nodal_field(args,ref,metric,N)
        if data is not None:
            fields.append(data)
            report['actual_quintic']=read_field(data,h.profile_from(metric),args.read_angles,args.radial_subdivisions)
            print(json.dumps(dict(event='local_quintic_readout',**report)),flush=True)
        out['fields'].append(report)
    if len(fields)==2:
        a,b=fields
        out['two_N_endpoint_differences']=dict(
            value_coeff_max=float(np.max(abs(np.asarray(a['states'][-1])-np.asarray(b['states'][-1])))),
            first_coeff_max=float(np.max(abs(np.asarray(a['rhs'][-1])-np.asarray(b['rhs'][-1])))),
            second_coeff_max=float(np.max(abs(np.asarray(a['d2'][-1])-np.asarray(b['d2'][-1])))))
    path=Path(str(args.output_stem)+'-report.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='local_readout_report_ready',path=str(path),sha256=h.sha(path))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference',type=Path,required=True);p.add_argument('--metric',type=Path,required=True)
    p.add_argument('--output-stem',type=Path,required=True)
    p.add_argument('--modes',type=int,default=320);p.add_argument('--angles',nargs='+',type=int,default=[2048,4096])
    p.add_argument('--read-angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
    p.add_argument('--end',type=float,default=.997);p.add_argument('--max-step',type=float,default=.000015625)
    p.add_argument('--rtol',type=float,default=1e-13);p.add_argument('--atol',type=float,default=1e-16)
    p.add_argument('--keep-terminal-microcells',action='store_true')
    main(p.parse_args())
