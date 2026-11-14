#!/usr/bin/env python3
"""Finite nonlinear Codazzi high-mode BVP with explicit retained low outputs.

Keep B(0)=0, the total-turning mean C(0)=-1/a0, and the first L waist C
coefficients. Match only C modes L+1..M at the positive cut to the old
geometry. The omitted L outer rows are recorded as actual unmatched outputs;
they are not assigned a zero cap response or deleted from the target.
"""
from __future__ import annotations
import argparse,inspect,json,time
from pathlib import Path
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_two_end_probe import save_npz_gz,load_candidate
from fourfold_phase_codazzi_two_end_homotopy_probe import ChunkedTwoEnded,diagnostics
from fourfold_phase_codazzi_feasible_bvp_probe import guarded_newton


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=32);p.add_argument('--waist-low',type=int,default=4)
    p.add_argument('--angles',type=int,default=512);p.add_argument('--right',type=float,default=.25)
    p.add_argument('--radial-nodes',type=int,default=251);p.add_argument('--max-nodes',type=int,default=3000)
    p.add_argument('--tol',type=float,default=1e-5);p.add_argument('--newton-iterations',type=int,default=16)
    p.add_argument('--C-floor',type=float,default=.05);p.add_argument('--field-ceiling',type=float,default=20.)
    p.add_argument('--guess',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True);args=p.parse_args();start=time.monotonic()
    m,L=args.modes,args.waist_low;n=2*m+1
    if not 0<=L<m or args.angles<8*m or args.angles%4:raise ValueError('invalid retained space/angular grid')
    geometry,definition=load_exact_object(args.object,512);system=ChunkedTwoEnded(geometry,m,args.angles)
    r=np.linspace(0.,args.right,args.radial_nodes);guess=np.column_stack([system.old_fields(x) for x in r])
    a0=scalar_target(geometry,0.)['a'];left_old=system.old_fields(0.);right_old=system.old_fields(args.right)
    if args.guess:
        old=load_candidate(args.guess);meta=json.loads(str(old['metadata']))
        if meta['object_sha256']!=sha(args.object) or not np.all(np.isfinite(old['piece_coefficients'])):
            raise ValueError('invalid previous candidate')
        pm=int(meta['modes']);values=PPoly(old['piece_coefficients'],old['radial_nodes'])(r).T;count=min(pm,m)
        guess[:count]=values[:count];guess[m:m+count+1]=values[pm:pm+count+1]
    def bc(left,right):return np.r_[left[:m],left[m]+1/a0,
        left[m+1:m+L+1]-left_old[m+1:m+L+1],right[m+L+1:]-right_old[m+L+1:]]
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n));split=m+L+1
        jl[np.arange(split),np.arange(split)]=1;jr[np.arange(split,n),np.arange(split,n)]=1
        return jl,jr
    log=[];original=bvp.solve_newton
    bvp.solve_newton=guarded_newton(system,log,args.C_floor,args.field_ceiling,args.newton_iterations)
    try:
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
    finally:bvp.solve_newton=original
    d=diagnostics(system,result);d['valid']=bool(all(np.isfinite(v) for v in d.values()) and d['C_max']<0 and d['C_abs_min']>0)
    initial=result.y[:,0];end=result.y[:,-1]
    meta=dict(kind='floating_retained_low_nonlinear_Codazzi_BVP',coordinates='B,C',modes=m,
        source_sha256=sha(__file__),object_sha256=sha(args.object),physical_frequency_factor=4,
        state_order='B sine k=1..M, C cosine k=0..M',initial_waist_curve_changed=True,original_target_fixed=True,
        fixed_waist_C_modes=list(range(L+1)),matched_positive_C_modes=list(range(L+1,m+1)),
        unmatched_positive_C_modes=list(range(1,L+1)),
        right_boundary='old actual C modes L+1..M only; low C/mean and all B are explicit unmatched outputs, NOT a cap DN',
        finite_coefficients=bool(np.all(np.isfinite(result.sol.c))))
    save_npz_gz(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,
        initial_state=initial,right_boundary_C_nonmean=right_old[m+1:],metadata=np.array(json.dumps(meta)))
    doc=dict(**meta,certified=False,success=bool(result.success and d['valid']),solver_status=int(result.status),solver_message=result.message,
        guarded_Newton_history=log,diagnostics=d,radial_nodes=len(result.x),right=args.right,tol=args.tol,
        initial_radial_nodes=args.radial_nodes,max_nodes=args.max_nodes,newton_steps_per_mesh=args.newton_iterations,
        angular_grid=args.angles,diagnostic_grid=2*args.angles,C_search_floor=args.C_floor,field_search_ceiling=args.field_ceiling,
        initial_B_l1=float(np.sum(abs(initial[:m]))),initial_C_mean=float(initial[m]),initial_C_mean_gap=float(initial[m]+1/a0),
        initial_turn_number=float(-a0*initial[m]),initial_total_turn=float(-2*np.pi*a0*initial[m]),
        fixed_waist_C_coefficients=initial[m+1:m+L+1].tolist(),
        fixed_waist_C_difference_l1=float(np.sum(abs(initial[m+1:m+L+1]-left_old[m+1:m+L+1]))),
        full_initial_C_coefficients=initial[m:].tolist(),old_initial_C_coefficients=left_old[m:].tolist(),
        positive_B_coefficients=end[:m].tolist(),old_positive_B_coefficients=right_old[:m].tolist(),
        unmatched_positive_C_coefficients=end[m+1:m+L+1].tolist(),old_positive_C_low=right_old[m+1:m+L+1].tolist(),
        unmatched_positive_C_difference_l1=float(np.sum(abs(end[m+1:m+L+1]-right_old[m+1:m+L+1]))),
        positive_B_difference_l1=float(np.sum(abs(end[:m]-right_old[:m]))),free_positive_C_mean=float(end[m]),
        matched_positive_C_difference_l1=float(np.sum(abs(end[m+L+1:]-right_old[m+L+1:]))),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        guess_path=str(args.guess) if args.guess else None,guess_sha256=sha(args.guess) if args.guess else None,
        scipy_version=scipy.__version__,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_codazzi_feasible_bvp_probe.py','fourfold_phase_codazzi_two_end_probe.py',
             'fourfold_phase_codazzi_two_end_homotopy_probe.py','fourfold_phase_symmetric_geometry.py',
             'fourfold_phase_geometry.py','fourfold_phase_core_low_block.py','fourfold_phase_local_correction_probe.py')},
        mean_retained=True,regular_trace=None,regular_flux=None,whole_parameter_interval=False,whole_real_angular_circle=False,whole_radial_domain=False,
        wall_seconds=time.monotonic()-start,
        limitations=['Finite Fourier/floating collocation; no actual PDE or continuous radial/angular residual certificate.',
            'The low waist C rows are fixed, but the entire initial curve can still change through its higher modes.',
            'All unmatched low/mean and B outputs are displayed. No full cap, mean/regular response, Schur inverse, or closed surface is asserted.',
            'The guard may use a library singular-stop flag to stop lack of an admissible step; consult the explicit history rather than interpreting that flag as mathematical singularity.'])
    args.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(success=doc['success'],diagnostics=d,initial_low_gap=doc['fixed_waist_C_difference_l1'],
        unmatched_positive_C=doc['unmatched_positive_C_difference_l1'],stop=log[-1],wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
