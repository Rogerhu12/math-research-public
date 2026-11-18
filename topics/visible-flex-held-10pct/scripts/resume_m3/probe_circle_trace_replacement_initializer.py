#!/usr/bin/env python3
"""One explicit new-space two-jet initializer, with original domain/RMS only.

The old accepted finite prefix supplies its complete integral reference and
physical quintic field.  The new endpoint retains raw B2..B14 and replaces
B15/B16 by T=SA-SB,U=SB.  At the reflection centre choose (t,u) to match the
old actual rho and h; this keeps the circle midpoint and radius there.
The old complete represented map is then projected against the new reference
and repaired at the inlet with the previously reviewed shared C2 window.
No BVP or actual tail solve is performed; the actual saved tail is only the
explicit affine anchor for this finite initial-guess residual evaluation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import PPoly
from couple_m3_smallcut_secant import accepted_anchor
from install_endpoint_c2_restart import install as install_c2
from m3_raw_diagnostic_model import RawDiagnosticEnvironment,sha
from circle_trace_replacement_core import make_core_class,PROVENANCE


def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference-run',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--nodes',type=int,default=257)
    p.add_argument('--projection-angular',type=int,default=4096)
    args=p.parse_args();began=time.monotonic()
    launch=json.loads((args.reference_run/'continuation-command.json').read_text())
    command=launch['command'];arg=lambda name:command[command.index('--'+name)+1]
    checkpoint=Path(arg('restart'));rec=json.loads(gzip.decompress(checkpoint.read_bytes()))
    accepted_anchor(rec,checkpoint)
    if rec['config']['modes']!=16 or not rec['config']['fixed_metric']:
        raise ValueError('The declared actual fixed-g M16 source is required')
    settings=json.loads((args.reference_run/'seed-round-record.json').read_text())['settings']
    if settings['halfwidth']!=.21 or settings['transition']!=.32 or settings['control_transition']!=.4 or settings['homotopy']!=1.:
        raise ValueError('This probe is the predeclared a21/b32/w40 endpoint only')
    profile=json.loads(Path(arg('profile')).read_text());chart=json.loads(Path(arg('chart')).read_text())
    port_path=Path(arg('linear-port'));port=json.loads(port_path.read_text());port['_sha256']=sha(port_path)
    if profile!=rec['frozen_profile'] or chart!=rec['chart']:
        raise ValueError('The original physical profile and chart must be retained')
    tail_path=args.reference_run/'seed_tail_0002.json.gz';tail=json.loads(gzip.decompress(tail_path.read_bytes()))
    if tail['response'].get('converged') is not True or not math.isfinite(tail['response']['residual']) or not tail['response']['residual']<2e-9:
        raise ValueError('The original actual affine anchor must pass its original stopping gate')
    J=np.asarray(tail['response']['heightJetJacobian'],float)
    if J.size!=800 or not np.all(np.isfinite(J)):raise ValueError('The original complete finite DN Jacobian is required')
    M=16;N=int(arg('angular'));q=float(arg('amplitude'));warp=float(arg('warp-reference'))
    if q!=rec['actual_primary_amplitude'] or warp!=rec['warp_reference_q']:
        raise ValueError('The declared actual q and old sine chart must be retained')
    oldsettings=rec['core_round_settings']
    env=RawDiagnosticEnvironment(Path(arg('source-topic')),Path(arg('short-bridge')),chart,oldsettings)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    install_record=args.out.with_name(args.out.stem+'-original-gauge-seed.json')
    install_metadata=install_c2(env.BVP,install_record)
    # Obtain only the already reviewed original initializer's represented cut
    # coefficients in the new gauge. This supplies an exact full-H copy.
    gauge_seed=env.make(oldsettings,profile,port,q,M,N,False,warp)
    gauge_seed.restart_remesh=args.nodes
    _,gauge_y,gauge_p=gauge_seed.restart(checkpoint)
    H0=np.asarray(tail['request']['height'],float)
    if not np.array_equal(gauge_seed.bridge.sigma*q*gauge_y[gauge_seed.iz:,-1],H0):
        raise ValueError('The original gauge initializer does not preserve the recorded complete H')
    # Reconstruct the actual old full represented map in its recorded gauge.
    old=env.make(oldsettings,profile,port,rec['gauge_amplitude'],M,N,True,warp)
    oldp=np.asarray(rec['parameters'],float)
    if old.pscale.tobytes()!=np.asarray(rec['central_correction_scales'],float).tobytes():
        raise ValueError('The old physical control scale convention changed')
    old.initial(oldp);oldf=old.flow(oldp[0]);oldcore=old._core;OriginalCore=type(oldcore)
    from curve_stable_prefix_bvp import load_checkpoint
    from fixed_metric_mode3_bvp import merge_profile_mesh
    complete=load_checkpoint(checkpoint)
    oldpp=PPoly.construct_fast(np.asarray(complete['pp_coefficients']),np.asarray(complete['mesh']),extrapolate=False,axis=1)
    oldc=np.asarray(rec['parameters'][1:])*np.asarray(rec['central_correction_scales'])
    chosen=oldc.copy();chosen[-2:]=0.
    # All later constructions use an independent new core. Existing old flows
    # keep their attached immutable actual integral core and cached lift.
    from plateau_core import PlateauSupportCore
    Core=make_core_class(PlateauSupportCore)
    factory=lambda amplitude,corrections=(),base_mode=3:Core(amplitude,corrections,base_mode,arc_nodes=1024,**settings)
    __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
    # The warped BVP captures its core factory in a closure. Build a fresh
    # class family after installing the new factory; do not mutate the old
    # family or merely change a module global and assume the closure changed.
    NewFlow,NewBase=env.coupler.adaptive.build_classes(chart)
    from exact_core_lift import install_core_lift
    from analytic_adaptive_core_jac import install as install_parameter_jac
    NewLift=install_core_lift(NewFlow,NewBase,window=(.5,.9))
    install_parameter_jac(NewLift)
    class NewBVP(env.coupler.TailMixin,NewLift):pass
    obj=NewBVP(profile,port,q,M,N,False,warp)
    obj.bcweights=np.full(M,float(arg('physical-bc-tol'))/float(arg('bc-tol')))
    par=np.zeros(M);par[1:]=chosen/obj.pscale
    obj.initial(par);basecore=obj._core
    if not isinstance(basecore,Core):raise ValueError('The new BVP did not capture the new finite-space core')
    centre=np.array([settings['center']]);og=oldcore.normal_geometry(centre);ng=basecore.normal_geometry(centre)
    delta_h=float(og['h'][0]-ng['h'][0])
    delta_rho=float(og['rho'][0]-ng['rho'][0])
    delta_hpp=delta_rho-delta_h
    # Physical coordinates: t=A=delta rho, u=delta h; B=u-t=-delta h''.
    chosen[-2:]=[delta_rho,delta_h]
    mapping=dict(old_q_gauge=rec['gauge_amplitude'],new_q_gauge=q,actual_q=rec['actual_primary_amplitude'],
        old_full_controls=oldc.tolist(),retained_raw_indices=list(range(2,15)),
        removed_raw_indices=[15,16],removed_raw_coefficients=oldc[-2:].tolist(),
        trace_coordinates=dict(t=delta_rho,u=delta_h,A=delta_rho,B=delta_h-delta_rho),
        old_h=float(og['h'][0]),old_rho=float(og['rho'][0]),
        base_new_h=float(ng['h'][0]),base_new_rho=float(ng['rho'][0]),
        delta_h=delta_h,delta_hpp=delta_hpp,
        rule='Keep the first 13 raw physical coefficients; t=old rho-new base rho, u=old h-new base h. No parameter scan.',
        scale_chain='Physical retained controls and (t,u) equal p[1:]*pscale. The last columns are d/dt=T and d/du=U; (A,B)=(t,u-t).')
    # A zero-trace identity checks the changed interface, not another initializer.
    original_zero=OriginalCore(q,basecore.c.copy(),3,arc_nodes=1024,**settings)
    points=np.linspace(.013,2*np.pi-.019,17)
    left,right=original_zero.evaluate(points),basecore.evaluate(points)
    interface=dict(zero_trace_same_core_max_difference={key:float(np.max(abs(left[key]-right[key]))) for key in ['F','Ft','Ftt','kappa']},
        basis=basecore.basis.summary(),zero_trace_numerical_rho_lower=basecore.rho_lower)
    phi=2*np.pi*np.arange(4096)/4096
    newjets=basecore.basis.support_jets(phi,4);rawjets=basecore.basis.raw.support_jets(phi,4,1.)
    interface['retained_raw_jets_binary64_identical']=[new[:13].tobytes()==raw[:13].tobytes() for new,raw in zip(newjets,rawjets)]
    # Independent split quadrature checks the primitive needed by material
    # inversion and parameter jets at five predeclared positive sector points.
    gx,gw=np.polynomial.legendre.leggauss(128);basis=basecore.basis
    targets=[.5*basis.a,basis.a+.27*basis.eps,basis.a+.73*basis.eps,
             basis.a+basis.eps+.37*(basis.T/2-basis.a-basis.eps),basis.T/2]
    errors=[]
    for target in targets:
        integral=np.zeros(2)
        cuts=sorted(set([0.,target,*[z for z in [basis.a,basis.a+basis.eps] if 0<z<target]]))
        for lo,hi in zip(cuts[:-1],cuts[1:]):
            angles=basis.center+(lo+hi)/2+(hi-lo)/2*gx
            integral+=(hi-lo)/2*(basis.support_jets(angles,0)[0][-2:]@gw)
        computed=basis.trace_primitive(np.array([basis.center+target]))[:,0]
        errors.append(float(np.max(abs(integral-computed))))
    interface['primitive_split_quadrature_points']=targets
    interface['primitive_split_quadrature_max_errors']=errors
    output=dict(scope=__doc__,command=sys.argv,source_sha256={**env.sources,
        **{str(Path(__file__).with_name(name).resolve()):sha(Path(__file__).with_name(name)) for name in [
            'probe_circle_trace_replacement_initializer.py','circle_trace_replacement_basis.py',
            'circle_trace_replacement_core.py','circle_trace_controls.py','raw_second_order_core.py',
            'install_endpoint_c2_restart.py']}},
        actual_seed_checkpoint=dict(path=str(checkpoint.resolve()),sha256=sha(checkpoint)),
        coefficient_chunks={str(f.resolve()):sha(f) for f in sorted(checkpoint.parent.glob('seed_coeff_*.npy.gz'))},
        actual_affine_tail_anchor=dict(path=str(tail_path.resolve()),sha256=sha(tail_path),residual=tail['response']['residual']),
        core_definition_provenance=PROVENANCE,new_core_settings=settings,
        original_gauge_seed_record=dict(path=str(install_record),sha256=sha(install_record),source_transform=install_metadata),
        initialization_mapping=mapping,interface_checks=interface,modes=M,angular=N,
        projection_angular=args.projection_angular,initial_nodes_argument=args.nodes,
        actual_tail_solver_invoked=False,BVP_solver_invoked=False)
    try:
        par[1:]=chosen/obj.pscale;obj.initial(par);f=obj.flow(par[0]);core=obj._core
        actualc=par[1:]*obj.pscale;cg=core.normal_geometry(centre)
        output['actual_initial_core']=dict(physical_controls=actualc.tolist(),parameters=par.tolist(),
            central_correction_scales=obj.pscale.tolist(),summary=core.summary(),
            matched_h_error=float(cg['h'][0]-og['h'][0]),matched_rho_error=float(cg['rho'][0]-og['rho'][0]),
            retained_physical_control_max_roundoff=float(np.max(abs(actualc[:-2]-oldc[:-2]))),
            combined_whole_control_rho_bounds=list(core.basis.combined_control_rho_bounds(actualc)))
        t=merge_profile_mesh(np.linspace(0,1,args.nodes),obj.chart_breaks)
        s,_=obj.chart(t,par[0])
        if f.end!=oldf.end:raise ValueError('The supposedly unchanged physical profile has a new length')
        oy=oldpp(s);Nproj=args.projection_angular;B,B1,B2=f.basis(Nproj)
        y=np.empty((obj.n,len(s)));before_max=np.zeros(3)
        oldbasis=oldf.basis(Nproj)
        for first in range(0,len(s),24):
            sl=slice(first,first+24);oldgeo=oldf.geo(s[sl],Nproj);newgeo=f.geo(s[sl],Nproj)
            if not np.array_equal(oldgeo['theta'],newgeo['theta']):raise ValueError('A changed angular chart would require material pullback')
            previous=oldgeo['pos']+old.q*oldf.values(oy[:,sl],oldbasis[0])
            y[:,sl]=f.project(previous-newgeo['pos'],B)/obj.q
            for j,(key,BB,oldBB) in enumerate(zip(['pos','p1','p2'],[B,B1,B2],oldbasis)):
                error=newgeo[key]+obj.q*f.values(y[:,sl],BB)-oldgeo[key]-old.q*oldf.values(oy[:,sl],oldBB)
                before_max[j]=max(before_max[j],float(np.max(abs(error))))
        prior_cut=y[obj.iz:,-1].copy();y[obj.iz:,-1]=gauge_y[obj.iz:,-1]
        correction=obj.initial(par)-y[:,0]
        u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
        weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
        y+=correction[:,None]*weight[None,:]
        H=obj.bridge.sigma*obj.q*y[obj.iz:,-1]
        if H.tobytes()!=H0.tobytes():raise ValueError('The new complete initial H differs from the actual affine anchor')
        obj.tail=env.coupler.AffineTailForInnerBVP(H0,tail['response'],M)
        h=np.diff(t);col,middle,rhs,rhs_middle=_bvp.collocation_fun(obj.fun,y,par,t,h)
        spline=_bvp.create_spline(y,rhs,t,h)
        rms=_bvp.estimate_rms_residuals(obj.fun,spline,t,h,par,1.5*col/h,rhs_middle)
        minimum=1.
        for xx,yy in [(t,y),((t[:-1]+t[1:])/2,middle)]:
            physical,_=obj.chart(xx,par[0])
            for first in range(0,len(xx),32):
                sl=slice(first,first+32)
                minimum=min(minimum,float(np.min(f.frame(physical[sl],obj.q*yy[:,sl])['margin'].real)))
        output['finite_initializer']=dict(original_initial_domain_passed=True,nodes=len(t),
            original_collocation_rms=float(np.max(rms)),collocation_residual_max=float(np.max(abs(col))),
            boundary_residual=float(np.max(abs(obj.bc(y[:,0],y[:,-1],par)))),sampled_min_frenet_margin=minimum,
            before_repair_old_full_map_position_first_second_max=before_max.tolist(),
            copied_original_gauge_cut_height_coeff_max_change=float(np.max(abs(y[obj.iz:,-1]-prior_cut))),
            full_H_binary64_equal=True,full_H_binary64_sha256=binary_sha(H),
            final_inlet_coefficient_error=float(np.max(abs(y[:,0]-obj.initial(par)))),
            actual_q=obj.support_amplitude,delta=profile['delta']+float(par[0]),
            initializer_state_binary64_sha256=binary_sha(y),parameter_binary64_sha256=binary_sha(par))
    except (FloatingPointError,ValueError) as error:
        output['finite_initializer']=dict(original_initial_domain_passed=False,error=str(error),
            failed_stage='Original core/geometry/domain/RMS initializer evaluation; no Newton or actual-tail call')
    output['seconds']=time.monotonic()-began
    output['limits']='The endpoint space and initializer are new. Finite reference/jets/domain/RMS checks neither establish a BVP solution nor inherit R38/R41 geometry. No original acceptance gate, running source, physical profile, or actual tail has been changed.'
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),seconds=output['seconds'],
        initializer=output['finite_initializer'])),flush=True)


if __name__=='__main__':main()
