#!/usr/bin/env python3
"""Nonlinear finite-annulus continuation for the geometry screen candidates.

Uses the repository's full spatial Frenet ODE and exact reflected core.
Endpoint conditions are LINEAR ROBIN data, possibly synthetic.  A numerical
solution here is not a compact-tail, rotational-boundary, closed-surface,
all-phase reach, or fixed-geometry full-convergence result.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_bvp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--modes',type=int,default=4)
    parser.add_argument('--amplitudes',type=float,nargs='+',default=[.01,.025,.04,.06,.08,.1,.125,.15])
    parser.add_argument('--nodes',type=int,default=121)
    parser.add_argument('--max-nodes',type=int,default=3500)
    parser.add_argument('--angular',type=int,default=128)
    parser.add_argument('--audit-angular',type=int,default=256)
    parser.add_argument('--audit-points',type=int,default=201)
    parser.add_argument('--tol',type=float,default=1e-7)
    parser.add_argument('--bc-tol',type=float,default=1e-8)
    parser.add_argument('--restart',type=Path)
    args = parser.parse_args()
    scripts = args.source_root/'topics/large-amplitude-twist-flex/scripts'
    sys.path.insert(0,str(scripts))
    from f6curve_outward_bridge_linear import read_port
    from f6curve_outward_bridge_bvp import OutwardTailBVP
    from f6curve_domain_newton import install,STATS
    from f6curve_local_frame import install_local_frame
    from f6curve_core_variation import install_analytic_core_jacobian
    from curve_stable_prefix_bvp import save_checkpoint
    from repo_scan_gentle import scaled_port,port_from_core_halfwidth,finite_value
    from repo_scan_inward_model import InwardCycleBridge
    cfg = json.loads(args.config.read_text())
    source = read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port = scaled_port(source,cfg['cut_radius'],cfg.get('cut_slope'),cfg.get('dimensionless_D'))
    design = None
    if 'core_halfwidth' in cfg:
        port,design = port_from_core_halfwidth(port,cfg,cfg['core_halfwidth'])
    install()
    cls = InwardCycleBridge if cfg.get('direction','outward') == 'inward' else OutwardTailBVP
    report = dict(scope=__doc__,candidate_config=cfg,port=port,
                  synthetic_port_design=design,solver_args={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},rows=[])
    report['source_hashes'] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [
        Path(__file__),Path(__file__).with_name('repo_scan_gentle.py'),
        Path(__file__).with_name('repo_scan_inward_model.py'),
        scripts/'f6curve_outward_bridge_bvp.py',scripts/'curve_stable_prefix_bvp.py']}
    previous = args.restart
    start = time.time()
    for q in args.amplitudes:
        begin = time.time()
        suffix = ('%.6f'%q).rstrip('0').rstrip('.').replace('.','p')
        checkpoint = args.out_prefix.with_name(args.out_prefix.name+f'_m{args.modes}_q{suffix}.json.gz')
        row = dict(amplitude=q,modes=args.modes,checkpoint=checkpoint.name,solver_success=False)
        out = None
        try:
            obj = cls(port,modes=args.modes,amplitude=q,delta=cfg['delta'],vu=cfg['vu'],
                      vd=cfg['vd'],eps=cfg['ramp'],cycles=cfg['cycles'],angular=args.angular,base_mode=2)
            install_local_frame(obj)
            install_analytic_core_jacobian(obj)
            x,y,p = obj.restart(previous,args.nodes) if previous else obj.seed(args.nodes)
            print(json.dumps(dict(event='start',q=q,modes=args.modes,h0=obj.h0,
                                  initial_nodes=len(x),restart=str(previous) if previous else None)),flush=True)
            sol = solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,
                            max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=0)
            sol.sol = obj.c2_interpolant(sol)
            config = dict(delta=cfg['delta'],v_up=cfg['vu'],v_down=cfg['vd'],ramp=cfg['ramp'],
                          cycles=cfg['cycles'],base_mode=2,modes=args.modes,amplitude=q,
                          direction=cfg.get('direction','outward'),port=port,
                          angular=args.angular,tol=args.tol,bc_tol=args.bc_tol)
            out = dict(scope=__doc__,config=config,success=bool(sol.success),solver_success=bool(sol.success),
                message=sol.message,parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,
                rhos=obj.rhos.tolist(),nodes=len(sol.x),
                max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                newton_domain_audit=dict(STATS),mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
            out = save_checkpoint(checkpoint,out)
            audit = obj.audit_streamed(sol,args.audit_points,args.audit_angular)
            seam = obj.seam_audit(sol)
            out.update(summary=audit,seam=seam,seconds=time.time()-begin)
            save_checkpoint(checkpoint,out)
            D = audit['finite_symmetric_band_cylinder_diameter_upper']
            kappa = audit['maximum_surface_principal_curvature']
            rho_est = (D*D/4-(audit['prefix_height_integral']+audit['port_mean_height'])**2)**.5
            row.update(solver_success=bool(sol.success),message=sol.message,nodes=len(sol.x),
                core_halfwidth=out['core']['halfwidth'],central_PV=audit['central_PV'],
                cylinder_diagonal=D,kappa_sample=kappa,kappa_times_cylinder_diagonal=kappa*D,
                PV_over_cylinder_diagonal=audit['central_PV']/D,
                height_integral=audit['prefix_height_integral'],port_mean_height=audit['port_mean_height'],
                metric_l1=audit['metric_theta_Fourier_l1_bound'],
                metric_relative_operator_bound=audit['metric_relative_operator_bound_from_components'],
                darboux_l1=audit['darboux_tensor_theta_Fourier_l1_frobenius_bound'],
                full_flow_defect=audit['full_unprojected_flow_defect'],
                root_margin=audit['minimum_root_margin'],
                boundary_residual=audit['boundary_residual_max'],
                core_join_error=audit['initial_exact_core_projection_error'],
                terminal_noncircle_rms=audit['fixed_axis_noncircle_rms_final'],
                terminal_height_max=float(np.max(np.abs(seam.get('terminal_physical_height',[0])))),
                approximate_radius_for_ranking=float(rho_est.real if isinstance(rho_est,complex) else rho_est))
            if sol.success:
                previous = checkpoint
        except Exception as exc:
            row['error'] = repr(exc)
            if out is not None:
                out.update(audit_error=repr(exc),success=False)
                save_checkpoint(checkpoint,out)
        row['seconds'] = time.time()-begin
        report['rows'].append(finite_value(row))
        report['elapsed_seconds'] = time.time()-start
        reportpath = args.out_prefix.with_name(args.out_prefix.name+'_summary.json')
        reportpath.write_text(json.dumps(finite_value(report),indent=2,allow_nan=False)+'\n')
        print(json.dumps(finite_value(dict(event='result',**row))),flush=True)
        if not row['solver_success']:
            break


if __name__ == '__main__':
    main()
