#!/usr/bin/env python3
"""Actual positive-n nonlinear GC prefix initializer on an explicitly supplied flat-cut g.

Recovery generalization: the physical matching-coast parameter is read from
the candidate, with no restriction to the old candidate value 0.02. The ODE
still uses physical meridian s and exactly the same equations/integrator.

Only the finite n,m field is Fourier truncated.  Position and frame are
integrated pointwise for an independent actual-metric pollution diagnostic.
The constant central cylinder is translated analytically.  Every saved
nontrivial node is a real accepted DOP853 state.  No tail or BVP is solved.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy import fft
from scipy.integrate import DOP853
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('flat_prefix_hybrid',HERE/'fd2d-gc-ellipse-hybrid-flow.py')
hybrid=importlib.util.module_from_spec(spec);sys.modules[spec.name]=hybrid;spec.loader.exec_module(hybrid)
base=hybrid.base


def identity(path):
    path=Path(path)
    return dict(path=str(path.resolve()),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())


class AccurateBalanced(hybrid.Hybrid):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry=FixedBalancedGeometry()
        self.core=BalancedCurvatureCore((),base_kind='balanced_seed',geometry=self.geometry)
        self.seed=self.core.evaluate_normal_angle(self.theta)
        self.ell0=np.asarray(self.geometry.radius(self.theta),dtype=np.longdouble)
        self.a0=self.geometry.a0
        self.A,self.B=self.geometry.A,self.geometry.B

    def initial(self):
        return self.encode(np.asarray(self.seed['gc_values'],dtype=np.longdouble))

    def translated_cylinder_state(self,state,s):
        values=self.decode(state)
        values[:,4]+=s
        return self.encode(values)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--stem',type=Path,required=True)
    ap.add_argument('--modes',type=int,default=191)
    ap.add_argument('--oversample',type=int,default=2)
    ap.add_argument('--stop-at',type=float,default=.9)
    ap.add_argument('--max-step',type=float,default=.001)
    ap.add_argument('--metric-stop',type=float,default=2e-6)
    ap.add_argument('--discarded-rhs-stop',type=float,default=.01)
    ap.add_argument('--minimum-n-stop',type=float,default=.01)
    args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):
        raise FileExistsError('Choose an unused initializer stem')
    args.stem.parent.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    bundle=json.loads(args.candidate.read_text())
    candidate=base.frozen.Candidate(bundle)
    T=bundle['segments'][next(i for i,p in enumerate(bundle['segments']) if p.get('label')=='partial_return_matching_coast')]['L']
    if not np.isfinite(T) or T<=0:
        raise ValueError('The supplied candidate must have a positive physical matching-coast T')
    cylinder=candidate.segments[0]
    if cylinder['kind']!='coast' or cylinder['p0']!=0 or cylinder['p1']!=0:
        raise ValueError('The analytic startup requires the actual zero-phase cylinder')
    flow=AccurateBalanced(candidate,args.modes,args.oversample,100000)
    initial=flow.initial()
    geometry=flow.geometry
    u_phi=geometry.material_coordinate(flow.theta)
    frequencies=np.arange(0,args.modes+1,2)
    positive=frequencies[1:]
    # Small point table is accompanied by full finite Fourier coefficients;
    # l is the actual rational field (K+m^2)/n, not a projected l polynomial.
    sample_ids=np.arange(0,flow.work,6)
    srows=[];nrows=[];mrows=[];nsrows=[];msrows=[];lmnrows=[];diagnostics=[];kinds=[]
    report=dict(schema='fd2d-flat-prefix-actual-balanced-ivp-initializer-v1',
        scope=__doc__,source=identity(__file__),candidate=identity(args.candidate),
        source_dependencies=[identity(HERE/p) for p in ('fd2d-gc-ellipse-hybrid-flow.py','fd2d-gc-ellipse-flow.py',
            'fd2d_frozen_ellipse_candidate.py','fd2d_balanced_curvature_core.py','fd2d_metric_curvature_core.py')],
        exact_seed_moments=identity(geometry.moments_path),exact_seed_means=identity(geometry.means_path),
        T=T,physical_metric_changed_during_run=False,
        central_cylinder_length=cylinder['L'],requested_stop=min(candidate.end,args.stop_at),
        coordinate='fixed exact balanced-seed normal phi; material u=U_seed(phi), all parameters share this map',
        radial_coordinate='physical meridian s; no radial design-clock coordinate is used in this IVP',
        physical_reference_T=T,original_source_sha256='87c48bec7d906e1f7aa78177a733d601ec2dbef6d9942acda2e1fa4b63ef3326',
        scalar_fields='orthonormal l,m,n; no coordinate-speed scaling of values',
        finite_state='real amplitudes n0+sum n_k cos(k phi), m=sum m_k sin(k phi), k=2,4,...',
        stored_first='actual finite projected ODE RHS at saved state; not claimed to be a dense polynomial derivative',
        modes=args.modes,angular_work=flow.work,rtol=2e-12,max_step=args.max_step,
        initializer_only=True,BVP_solved=False,closed_surface=False,
        guards=dict(metric=args.metric_stop,discarded_rhs=args.discarded_rhs_stop,minimum_n=args.minimum_n_stop,
                    meaning='initialization pollution/coordinate guards, not nonexistence or final geometry gates'),
        rows=diagnostics,completed=False)

    def save_node(s,state,kind):
        frame=flow.frame(float(s),state)
        value=frame['values']
        rhs=flow.decode(frame['coefficients'])[:,:2]
        raw=fft.rfft(value[:,:2],axis=0,norm='forward')
        draw=fft.rfft(rhs,axis=0,norm='forward')
        nreal=np.r_[raw[0,0].real,2*raw[positive,0].real]
        mreal=-2*raw[positive,1].imag
        nsreal=np.r_[draw[0,0].real,2*draw[positive,0].real]
        msreal=-2*draw[positive,1].imag
        n,m=value[:,0],value[:,1]
        l=(m*m+frame['K'])/n
        srows.append(float(s));nrows.append(np.asarray(nreal,float));mrows.append(np.asarray(mreal,float))
        nsrows.append(np.asarray(nsreal,float));msrows.append(np.asarray(msreal,float))
        lmnrows.append(np.asarray(np.stack((l[sample_ids],m[sample_ids],n[sample_ids]),axis=-1),float))
        row=flow.diagnostics(float(s),state)
        row['n_top16_coefficient_l1']=float(np.sum(abs(nreal[-16:])))
        row['m_top16_coefficient_l1']=float(np.sum(abs(mreal[-16:])))
        row['kind']=kind
        diagnostics.append(row);kinds.append(kind)
        return row

    def checkpoint(state,status):
        report.update(last_s=srows[-1],rhs_calls=flow.calls,seconds=time.monotonic()-started,
                      saved_nodes=len(srows),status=status,max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        args.stem.with_name(args.stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        np.savez_compressed(args.stem.with_name(args.stem.name+'-trajectory.npz'),
            s=np.asarray(srows),frequencies=frequencies,
            n_phi_cos=np.asarray(nrows),m_phi_sin=np.asarray(mrows),
            n_s_phi_cos=np.asarray(nsrows),m_s_phi_sin=np.asarray(msrows),
            phi_sample=np.asarray(flow.theta[sample_ids],float),
            material_u_sample=np.asarray(u_phi['u'][sample_ids],float),
            l_m_n_sample=np.asarray(lmnrows),
            final_hybrid_state=np.asarray(state,float),
            candidate_sha256=report['candidate']['sha256'],modes=args.modes,
            fixed_chart='balanced_seed_normal_phi',T=T)

    for s in np.linspace(0,cylinder['s1'],6):
        state=flow.translated_cylinder_state(initial,float(s))
        save_node(float(s),state,'analytic_exact_cylinder_translation')
    last_state=state.copy()
    checkpoint(last_state,'analytic cylinder complete')
    atol=2e-14/(1+flow.active_wave)**2
    stopped=False
    try:
        for j,seg in enumerate(candidate.segments[1:],1):
            if seg['s0']>=report['requested_stop']-1e-14:
                break
            right=min(seg['s1'],report['requested_stop'])
            solver=DOP853(flow.rhs,seg['s0'],last_state,right,max_step=args.max_step,
                          rtol=2e-12,atol=atol)
            while solver.status=='running':
                message=solver.step()
                if solver.status=='failed':
                    report['integrator_failure']=dict(segment=j,message=message,t=float(solver.t))
                    stopped=True;break
                diag=flow.diagnostics(float(solver.t),solver.y)
                failures=[]
                if diag['metric']>args.metric_stop:failures.append('actual_position_metric_pollution')
                if diag['projection_defect']>args.discarded_rhs_stop:failures.append('discarded_finite_rhs_pollution')
                if diag['minimum_n']<args.minimum_n_stop:failures.append('positive_n_chart_margin')
                if failures:
                    report['first_guard_state']=dict(segment=j,diagnostic=diag,reasons=failures)
                    np.savez_compressed(args.stem.with_name(args.stem.name+'-guard-state.npz'),
                                        s=float(solver.t),hybrid_state=solver.y,candidate_sha256=report['candidate']['sha256'])
                    stopped=True;break
                save_node(float(solver.t),solver.y,'actual_accepted_DOP853')
                last_state=solver.y.copy()
            checkpoint(last_state,'guard or solver stop' if stopped else 'accepted nonlinear stage')
            if j%8==0 or stopped:
                print(json.dumps(dict(segment=j,s=srows[-1],metric=diagnostics[-1]['metric'],
                    minimum_n=diagnostics[-1]['minimum_n'],actual_curvature=diagnostics[-1]['actual_curvature'],
                    rhs_calls=flow.calls,saved_nodes=len(srows),stopped=stopped)),flush=True)
            if stopped or right>=report['requested_stop']-1e-14:
                break
    except Exception as exc:
        report['failure']=dict(type=type(exc).__name__,message=str(exc),last_saved_s=srows[-1])
    report['completed']=True
    report['reached_requested_stop']=abs(srows[-1]-report['requested_stop'])<1e-12
    report['final_state_identity_scope']='Last saved accepted state, before any explicitly separate guard state'
    checkpoint(last_state,'closed finite initializer')
    print(json.dumps({k:report.get(k) for k in ('last_s','saved_nodes','rhs_calls','seconds','reached_requested_stop','failure','first_guard_state')}),flush=True)


if __name__=='__main__':
    main()
