#!/usr/bin/env python3
"""Bind one q060-cosine to M8 circle-trace design, then optionally its initializer.

The default command performs source/metadata binding and the unique scalar
primary match only. It does not call native_reference, construct either core,
reproject a state, or call any solver. An explicit --evaluate-initializer with
the frozen --evaluation-plan is the separate finite diagnostic entry.

Old: genuine accepted cosine q=.06, M8, 25 physical-quintic states, original
adaptive chart and warp reference .06. The final frozen profile is used as-is;
the historical fixed=False p0 is not added to it again. New: lambda1, a=.21,
bp=.32, bc=.4, M8 space B2..B6 plus T=SA-SB,U=SB, and q=.06/Pnew. This is a
new physical design and finite span, not fixed-g refinement or M16 embedding.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
READER=HERE.parent/'resume_closed/q060_cosine_reference.py'
READER_SHA='776bd257f9a299cce73d215597dcf2d02d161bf493deb2a66f9ece0972a327d4'
BINDING_SHA='01bfeedc8a160daf8ccae91a66b2f65d99c934166d26592b6a0e2b25049b0897'
TAIL_SHA='ae01f13ad7b28b82481a3417471c4fd5511b145bb50bd2be73a4386897a0db1e'
MOMENT_SOURCE_SHA='bdcca0c9f12db1fed025b53e905e6e274b7bd61ec39c4a697e1ec066b214e302'
SETTINGS=dict(halfwidth=.21,transition=.32,control_transition=.4,homotopy=1.,
    center=math.pi/3,bimodal_eta=0.,lock_fundamental=True,coefficient_precision=80,
    positivity_grid_max=32768)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()
def payload_sha(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def bind_design(binding_path):
    """No source object evaluation: only identity checks and scalar arithmetic."""
    if sha(READER)!=READER_SHA or sha(binding_path)!=BINDING_SHA:
        raise ValueError('The reviewed original cosine reader/binding changed')
    if sha(HERE/'match_m3_circle_primary_moment.py')!=MOMENT_SOURCE_SHA:
        raise ValueError('The reviewed defining primary factor changed')
    spec=importlib.util.spec_from_file_location('bound_q060_cosine_reference',READER)
    reader=importlib.util.module_from_spec(spec);sys.modules[spec.name]=reader;spec.loader.exec_module(reader)
    original=load(binding_path)
    bound=reader.bind_reference(original['checkpoint']['path'],original['terminal_record']['path'],
        original['source_topic'],original['short_bridge']['path'])
    cp=bound.record;controls=bound.actual_controls
    if controls.shape!=(7,) or cp['config']['modes']!=8:raise ValueError('Keep the genuine seven-control M8 anchor')
    from match_m3_circle_primary_moment import rational_factor,outward_decimal
    from moment_interval_bounds import scale,divide
    factor=rational_factor(SETTINGS)['P'];qold=F.from_float(cp['actual_primary_amplitude'])
    if factor[0]<=0:raise ArithmeticError('The existing primary factor enclosure is not positive')
    qstar=scale(divide((F(1),F(1)),factor),qold)
    qnew=float((qstar[0]+qstar[1])/2)
    rounding_bin=((F.from_float(math.nextafter(qnew,-math.inf))+F.from_float(qnew))/2,
                  (F.from_float(qnew)+F.from_float(math.nextafter(qnew,math.inf)))/2)
    if not rounding_bin[0]<qstar[0]<=qstar[1]<rounding_bin[1]:
        raise ArithmeticError('The scalar interval does not identify a unique nearest binary64 q')
    exact_controls=[F.from_float(float(c)) for c in controls]
    h_exact=F(1)-qold+sum(F((-1)**j)*c for j,c in enumerate(exact_controls,2))
    rho_exact=F(1)+8*qold+sum(F((1-9*j*j)*(-1)**j)*c for j,c in enumerate(exact_controls,2))
    tail_path=bound.checkpoint.with_name('seed_tail_0003.json.gz')
    if sha(tail_path)!=TAIL_SHA:raise ValueError('The final original actual tail identity changed')
    tail=load(tail_path);response=tail['response'];tcfg=tail['config']
    if (response.get('converged') is not True or not math.isfinite(response['residual']) or
        not response['residual']<tcfg['solveTolerance'] or tcfg['solveTolerance']!=2e-9 or
        tail['request']['jacobian'] is not True or tail['request']['audit'] is not True):
        raise ValueError('The final original finite tail/Jac/audit is required')
    J=np.asarray(response['heightJetJacobian'],float)
    if J.size!=208 or not np.all(np.isfinite(J)):raise ValueError('All original M8 height-jet derivatives are required')
    for key,value in cp['physical_tail_parameters'].items():
        if tcfg[key]!=value:raise ValueError('The old tail physical parameter changed: '+key)
    if tcfg['modes']!=8 or tcfg['spacing']!=3:raise ValueError('Do not change the original actual-tail frequency class')
    source_paths=[Path(__file__),READER,HERE/'match_m3_circle_primary_moment.py',
        HERE/'circle_trace_controls.py',HERE/'circle_trace_replacement_basis.py',
        HERE/'circle_trace_replacement_core.py',HERE/'raw_second_order_core.py',
        HERE/'m3_raw_diagnostic_model.py',*sorted((HERE/'round_raw_lib').glob('*.py')),
        bound.source_topic/'scripts/db6f-prefix-coupled.py',
        bound.source_topic/'scripts/78718-prefix-fourier-jacobian.py']
    sources={**bound.current_reference_source_sha256,
             **{str(path.resolve()):sha(path) for path in source_paths}}
    design=dict(old_reference_binding=ref(binding_path),old_checkpoint=ref(bound.checkpoint),
        old_coefficient_chunks=original['coefficient_chunks'],reader=ref(READER),
        actual_affine_tail_anchor=dict(**ref(tail_path),residual=response['residual'],Jacobian_entries=208,
            full_H=tail['request']['height'],full_H_binary64_sha256=binary_sha(tail['request']['height'])),
        old_core='Literal original finite cosine support; no raw/circle metadata or exact integral lift is attached to it.',
        old_modes=8,new_modes=8,old_state_components=25,new_state_components=25,
        old_q_gauge=cp['gauge_amplitude'],old_actual_core_q=cp['actual_primary_amplitude'],old_primary_factor=1,
        old_primary_Q=cp['actual_primary_amplitude'],
        new_q=dict(rule='q_old/Pnew, because the original cosine primary factor is exactly one',
            exact_enclosure=outward_decimal(qstar),binary64=qnew,binary64_hex=qnew.hex(),
            nearest_binary64_proved=True,Pnew_enclosure=outward_decimal(factor)),
        new_core_settings=SETTINGS,
        old_complete_controls=controls.tolist(),retained_old_indices=list(range(2,7)),
        removed_old_indices=[7,8],new_columns=['B2','B3','B4','B5','B6','T=SA-SB','U=SB'],
        trace_rule='Use all seven old cosine coefficients in h_old and rho_old. t=rho_old-(1+8*qnew), u=h_old-h_base_new, (A,B)=(t,u-t). The new retained B2..B6 vanish on the protected arc.',
        exact_old_centre=dict(normal_angle='pi/3',h=outward_decimal((h_exact,h_exact)),
            rho=outward_decimal((rho_exact,rho_exact)),h_prime=0,
            formula_h='1-q_old+sum((-1)^j*c_j,j=2..8)',
            formula_rho='1+8*q_old+sum((1-9*j*j)*(-1)^j*c_j,j=2..8)'),
        physical_profile=cp['frozen_profile'],physical_profile_payload_sha256=payload_sha(cp['frozen_profile']),
        old_historical_delta_parameter=cp['parameters'][0],new_initial_p0=0.,
        delta_semantics='Old fixed=False p0 has already entered frozen_profile.delta. Start the new design at this final profile with p0=0; do not add the historical p0 again.',
        meridian_length_binary64=cp['meridian_length'],warp_reference_q=cp['warp_reference_q'],
        original_chart=original['original_inputs']['chart'],chart_payload_sha256=original['chart_payload_sha256'],
        physical_port=original['original_inputs']['linear_port'],
        original_physical_polynomial=dict(mesh_nodes=1934,shape=[6,1933,25],coordinate='Physical s',extrapolate=False),
        full_map_scope='Original Flow.geo plus q_old times all25-state quintic, plus the original height_integral mean-height primitive. Projection uses the represented part because the vertical mean has no state column; its physical trajectory is never assumed zero.',
        new_reference_lift='Install the actual new integral core lift once, with the existing (.5,.9)*prefix_end window, on a fresh new Flow class only.',
        reprojection='Keep the identical old chart/warp/profile. Reproject old geo+q_old*old_field-new_geo into the new M8 field, divide by qnew, repair inlet using the original shared C2 window; no ratio-power restart.',
        full_H_scope='Re-encode the complete old actual H by H_old/(sigma*qnew), record the actual multiply-back H and all last-bit differences. The saved response is an affine initial-residual anchor only.',
        unchanged_core_guard=dict(rho_floor=1e-5,grid_ceiling=32768,combined_trace_analytic_bounds=True),
        unchanged_initial_discretization=dict(nodes_argument=257,projection_angular=4096,angular=cp['config']['angular']),
        unchanged_BC_weights=dict(physical_bc_tol=cp['config']['physical_bc_tol'],bc_tol=cp['config']['bc_tol']),
        no_claim='No fixed-g refinement, M16 embedding, BVP acceptance, new actual-tail acceptance, complete metric or inherited R38/R40/R41 geometry.')
    plan=dict(scope=__doc__,source_sha256=sources,design=design,
        identity_sha256=payload_sha(dict(source_sha256=sources,design=design)),
        native_reference_constructed=False,new_core_constructed=False,initializer_projected=False,
        BVP_solver_invoked=False,actual_tail_solver_invoked=False)
    return bound,tail,plan


def evaluate_initializer(bound,tail,plan):
    """The separate, explicit finite initial-state diagnostic; never a solve."""
    from scipy.integrate import _bvp
    from m3_raw_diagnostic_model import RawDiagnosticEnvironment
    native=bound.native_reference() # Must precede any replacement of the core factory.
    oldcore,oldf,oldpp=native.core,native.flow,native.polynomial
    cfg=copy.deepcopy(native.physical_profile);cp=bound.record;M=8
    design=plan['design'];q=design['new_q']['binary64'];settings=copy.deepcopy(SETTINGS)
    port=load(design['physical_port']['path']);port['_sha256']=design['physical_port']['sha256']
    env=RawDiagnosticEnvironment(bound.source_topic,bound.short_bridge,cp['chart'],settings)
    from plateau_core import PlateauSupportCore
    from circle_trace_replacement_core import make_core_class,PROVENANCE
    Core=make_core_class(PlateauSupportCore)
    factory=lambda amplitude,corrections=(),base_mode=3:Core(amplitude,corrections,base_mode,arc_nodes=1024,**settings)
    __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
    NewFlow,NewBase=env.coupler.adaptive.build_classes(cp['chart'])
    from exact_core_lift import install_core_lift
    from analytic_adaptive_core_jac import install as install_parameter_jac
    NewLift=install_core_lift(NewFlow,NewBase,window=(.5,.9));install_parameter_jac(NewLift)
    class NewBVP(env.coupler.TailMixin,NewLift):pass
    obj=NewBVP(cfg,port,q,M,cp['config']['angular'],False,cp['warp_reference_q'])
    obj.bcweights=np.full(M,cp['config']['physical_bc_tol']/cp['config']['bc_tol'])
    chosen=bound.actual_controls.copy();chosen[-2:]=0.;par=np.zeros(M)
    par[1:]=chosen/obj.pscale
    result=dict(plan_identity_sha256=plan['identity_sha256'],native_reference_constructed=True,
        core_definition_provenance=PROVENANCE,old_map_scope=design['full_map_scope'],
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,original_restart_called=False)
    try:
        obj.initial(par);basecore=obj._core;centre=np.array([math.pi/3])
        if not isinstance(basecore,Core):raise ValueError('The new class did not capture the new trace core')
        og=oldcore.normal_geometry(centre);ng=basecore.normal_geometry(centre)
        chosen[-2:]=[float(og['rho'][0]-ng['rho'][0]),float(og['h'][0]-ng['h'][0])]
        result['trace_mapping']=dict(old_h=float(og['h'][0]),old_rho=float(og['rho'][0]),
            new_base_h=float(ng['h'][0]),new_base_rho=float(ng['rho'][0]),
            t=float(chosen[-2]),u=float(chosen[-1]),A=float(chosen[-2]),B=float(chosen[-1]-chosen[-2]),
            old_all_seven_controls=bound.actual_controls.tolist(),intended_new_seven_controls=chosen.tolist())
        par[1:]=chosen/obj.pscale;obj.initial(par);f=obj.flow(0.);core=obj._core
        if float(f.end).hex()!=float(oldf.end).hex() or float(f.end).hex()!=float(cp['meridian_length']).hex():
            raise ValueError('The original frozen physical profile/domain changed')
        if hasattr(oldf,'exact_lift_core'):raise ValueError('The old original cosine reference was mutated by the new lift')
        from fixed_metric_mode3_bvp import merge_profile_mesh
        t=merge_profile_mesh(np.linspace(0,1,257),obj.chart_breaks);s,_=obj.chart(t,0.)
        oldy=oldpp(s);Nproj=4096;B,B1,B2=f.basis(Nproj);oldbasis=oldf.basis(Nproj)
        y=np.empty((25,len(s)));represented_errors=np.zeros(3)
        for first in range(0,len(s),24):
            sl=slice(first,first+24);ogeo=oldf.geo(s[sl],Nproj);ngeo=f.geo(s[sl],Nproj)
            if not np.array_equal(ogeo['theta'],ngeo['theta']):raise ValueError('A changed angular chart requires a new pullback design')
            represented=ogeo['pos']+oldf.q*oldf.values(oldy[:,sl],oldbasis[0])
            y[:,sl]=f.project(represented-ngeo['pos'],B)/q
            for j,(key,bb,oldbb) in enumerate(zip(['pos','p1','p2'],[B,B1,B2],oldbasis)):
                error=ngeo[key]+q*f.values(y[:,sl],bb)-ogeo[key]-oldf.q*oldf.values(oldy[:,sl],oldbb)
                represented_errors[j]=max(represented_errors[j],float(np.max(abs(error))))
        H0=np.asarray(tail['request']['height'],float);prior_cut=y[obj.iz:,-1].copy()
        y[obj.iz:,-1]=H0/(obj.bridge.sigma*q)
        correction=obj.initial(par)-y[:,0];u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
        weight=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u));y+=correction[:,None]*weight[None,:]
        H=obj.bridge.sigma*q*y[obj.iz:,-1]
        obj.tail=env.coupler.AffineTailForInnerBVP(H0,tail['response'],M)
        h=np.diff(t);col,middle,rhs,rhs_middle=_bvp.collocation_fun(obj.fun,y,par,t,h)
        spline=_bvp.create_spline(y,rhs,t,h)
        rms=_bvp.estimate_rms_residuals(obj.fun,spline,t,h,par,1.5*col/h,rhs_middle)
        margin=1.
        for x,field in [(t,y),((t[:-1]+t[1:])/2,middle)]:
            physical,_=obj.chart(x,0.)
            for first in range(0,len(x),32):
                sl=slice(first,first+32)
                margin=min(margin,float(np.min(f.frame(physical[sl],q*field[:,sl])['margin'].real)))
        actual=par[1:]*obj.pscale;cg=core.normal_geometry(centre)
        result['actual_core']=dict(physical_controls=actual.tolist(),parameters=par.tolist(),
            parameter_scales=obj.pscale.tolist(),summary={k:v for k,v in core.summary().items() if not isinstance(v,(dict,list))},
            centre_h_difference=float(cg['h'][0]-og['h'][0]),centre_rho_difference=float(cg['rho'][0]-og['rho'][0]),
            retained_control_roundoff=float(np.max(abs(actual[:5]-bound.actual_controls[:5]))))
        result['finite_initializer']=dict(original_initial_domain_passed=True,nodes=len(t),
            original_collocation_rms=float(np.max(rms)),collocation_residual_max=float(np.max(abs(col))),
            boundary_residual=float(np.max(abs(obj.bc(y[:,0],y[:,-1],par)))),sampled_min_frenet_margin=margin,
            represented_pos_angular1_angular2_errors=represented_errors.tolist(),
            full_H=H.tolist(),old_H=H0.tolist(),full_H_binary64_equal=H.tobytes()==H0.tobytes(),
            full_H_binary64_sha256=binary_sha(H),old_H_binary64_sha256=binary_sha(H0),
            full_H_changed_components=np.flatnonzero(H.view(np.uint64)!=H0.view(np.uint64)).tolist(),
            full_H_difference_max=float(np.max(abs(H-H0))),cut_reencoding_max=float(np.max(abs(y[obj.iz:,-1]-prior_cut))),
            inlet_error=float(np.max(abs(y[:,0]-obj.initial(par)))),actual_q=obj.support_amplitude,
            final_frozen_delta=cfg['delta'],new_p0=float(par[0]),state_binary64_sha256=binary_sha(y),
            parameter_binary64_sha256=binary_sha(par),full_metric_computed=False,mean_height_reconstructed=False)
    except (FloatingPointError,ValueError) as error:
        result['finite_initializer']=dict(original_initial_domain_passed=False,error=str(error),
            failed_stage='Original new core/geometry/domain/RMS evaluation; no Newton, BVP or actual tail call')
    result['source_sha256']={**plan['source_sha256'],**env.sources}
    bound.check_sources()
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-binding',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--evaluate-initializer',action='store_true')
    parser.add_argument('--evaluation-plan',type=Path)
    args=parser.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh output; do not overwrite a frozen record')
    bound,tail,plan=bind_design(args.reference_binding)
    if args.evaluate_initializer:
        if args.evaluation_plan is None:raise ValueError('The separate diagnostic requires its frozen metadata plan')
        prior=load(args.evaluation_plan)
        if prior['identity_sha256']!=plan['identity_sha256']:
            raise ValueError('The declared metadata/source/design identity changed')
        result=dict(plan=plan,evaluation_plan=ref(args.evaluation_plan),
            evaluation=evaluate_initializer(bound,tail,plan))
    else:
        if args.evaluation_plan is not None:raise ValueError('An evaluation plan is only for the explicit evaluation entry')
        result=plan
    result['command']=[sys.executable,*sys.argv];result['seconds']=time.monotonic()-began
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('x') as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),metadata_only=not args.evaluate_initializer,
        q_new=plan['design']['new_q']['binary64'],identity_sha256=plan['identity_sha256'],
        finite_initializer=result.get('evaluation',{}).get('finite_initializer'),seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
