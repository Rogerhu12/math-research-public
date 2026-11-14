#!/usr/bin/env python3
"""Floating construction of complete positive comparison-weight candidates.

These are auxiliary finite functions, never approximations certified as true
solutions.  All saved coefficients, including their real mean, define exact
dyadic, continuous piecewise-linear radial/Fourier functions.  A separate
closed-box consumer must prove positivity, the full actual-tube inequalities
and the final unweighted bootstrap.  No sampled gate proves continuation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip, io, json, time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha, scalar_target
from fourfold_phase_codazzi_dense_candidate import positive_hermitian, full_coefficients
from fourfold_codazzi_sharded_candidate import ShardedDenseCandidate
from fourfold_phase_codazzi_evolution_probe import resample, scalar_derivative


class WeightEvolution:
    def __init__(self, geometry, candidate, modes, grid, smoothing):
        self.geometry=geometry;self.candidate=candidate
        self.modes=modes;self.grid=grid;self.smoothing=smoothing;self.calls=0

    def __call__(self,r,y):
        raw=self.candidate.evaluate(float(r),self.grid)
        B,C=raw['BC'].T;Bt,Ct=raw['BC_theta'].T
        t=scalar_target(self.geometry,float(r))
        K=t['K'];k=np.sqrt(-K);gamma=np.sqrt(t['E'])/t['a']
        beta=t['a_x']/t['a'];kappa=t['minus_K_x']/(-4*K)
        P=(B+k)/C;Q=(B-k)/C
        Pt=Bt/C-(B+k)*Ct/C**2;Qt=Bt/C-(B-k)*Ct/C**2
        a=-2*beta*P*Q+kappa
        b=gamma*Pt-beta*(1+P*P)-kappa
        c=gamma*Qt-beta*(1+Q*Q)-kappa
        W=resample(y.reshape(self.modes,2),self.grid)
        Wt=scalar_derivative(W)
        rhs=np.column_stack((gamma*Q*Wt[:,0]+a*W[:,0]+np.hypot(b,self.smoothing)*W[:,1],
                             gamma*P*Wt[:,1]+a*W[:,1]+np.hypot(c,self.smoothing)*W[:,0]))
        self.calls+=1
        return resample(rhs,self.modes).ravel()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--right',type=Fraction,default=Fraction(1,5))
    ap.add_argument('--angles',type=int,default=256)
    ap.add_argument('--grid',type=int,default=2048)
    ap.add_argument('--smoothing',type=float,default=3.)
    ap.add_argument('--max-step',type=float,default=.0005)
    ap.add_argument('--rtol',type=float,default=2e-8)
    ap.add_argument('--atol',type=float,default=2e-10)
    ap.add_argument('--weights',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.weights.exists() or a.out.exists():raise FileExistsError('new finite candidate paths required')
    if a.angles%2 or a.grid<2*a.angles or a.smoothing<=0:raise ValueError('positive complete finite weights required')
    geometry,definition=load_exact_object(a.object,512)
    candidate=ShardedDenseCandidate(a.candidate)
    if a.grid<2*candidate.grid:raise ValueError('all candidate modes must be evaluated without truncation')
    if candidate.metadata['object_sha256']!=sha(a.object):raise ValueError('candidate actual target differs')
    rhs=WeightEvolution(geometry,candidate,a.angles,a.grid,a.smoothing)
    right=float(a.right)
    if Fraction.from_float(right)<a.right:right=float(np.nextafter(right,np.inf))
    if right>candidate.nodes[-1]:raise ValueError('finite candidate interval is insufficient')
    stages=sorted({0.,right}|{float(x) for x in candidate.nodes if 0<x<right})
    state=np.ones(2*a.angles)
    initial=np.zeros((a.angles//2,2),complex);initial[0]=1
    times=[0.];values=[initial];diagnostic=[];failure=None
    try:
        for stage,(left,end) in enumerate(zip(stages,stages[1:])):
            solver=DOP853(rhs,left,state,end,rtol=a.rtol,atol=a.atol,max_step=a.max_step)
            while solver.status=='running':
                message=solver.step()
                if solver.status=='failed':raise ValueError('floating weight integration failed: '+str(message))
                value=positive_hermitian(solver.y.reshape(a.angles,2))
                times.append(float(solver.t));values.append(value)
            state=solver.y
            row=dict(stage=stage,r=end,minimum=float(state.min()),maximum=float(state.max()))
            diagnostic.append(row)
            if stage%20==0:print(row,flush=True)
    except Exception as exc:
        failure=repr(exc)
    nodes=np.array(times);coefficients=np.array(values)
    metadata=dict(kind='exact_finite_piecewise_linear_Fourier_positive_weight_candidate',
        candidate_positivity_certified=False,weight_inequalities_certified=False,continuation_certified=False,
        coefficient_semantics='Stored binary64 real and imaginary parts are exact dyadic rationals.',
        radial_contract='(1-x)*left+x*right with exact shared endpoint coefficients',
        angular_contract='physical frequencies 4*k; all negative modes conjugate; real mean; Nyquist zero',
        angular_grid=a.angles,full_evaluation_grid=a.grid,mean_retained=True,
        time_nodes_exact_fractions=[str(Fraction.from_float(float(x))) for x in nodes],
        exact_requested_right=str(a.right),covered_interval=['0',str(Fraction.from_float(float(nodes[-1])))],
        source_sha256=sha(__file__),object_sha256=sha(a.object),
        candidate_manifest_sha256=sha(a.candidate),candidate_original_sha256=candidate.original_payload_sha256,
        exact_center_parameter=candidate.metadata['exact_center_parameter'],
        smoothing=a.smoothing,complete_finite_arrays=True)
    buffer=io.BytesIO();np.savez(buffer,time_nodes=nodes,positive_endpoint_coefficients=coefficients,
                               metadata=np.array(json.dumps(metadata)))
    a.weights.write_bytes(gzip.compress(buffer.getvalue(),compresslevel=6,mtime=0))
    report=dict(**metadata,complete=failure is None,failure=failure,certified=False,
        weight_file=str(a.weights),weight_sha256=sha(a.weights),weight_bytes=a.weights.stat().st_size,
        pieces=len(nodes)-1,rtol=a.rtol,atol=a.atol,max_step=a.max_step,
        rhs_calls=rhs.calls,wall_seconds=time.monotonic()-start,diagnostic_samples=diagnostic,
        diagnostic_minimum=min(row['minimum'] for row in diagnostic),
        diagnostic_maximum=max(row['maximum'] for row in diagnostic),
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_local_correction_probe.py',
            'fourfold_phase_codazzi_dense_candidate.py','fourfold_codazzi_sharded_candidate.py',
            'fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_geometry.py')},
        limitations=['Floating auxiliary weight construction only; not a PDE existence or residual certificate.',
            'A complete true-tube closed-box comparison must verify positivity and include all eta and Fourier tails.',
            'Piecewise-linear radial interpolation is the saved exact object; DOP853 dense functions are not reused.',
            'Final bootstrap is unweighted max(W)*z<T, with the actual gap and negative curvature separately paid.'])
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print({k:report[k] for k in ('complete','failure','pieces','weight_bytes','rhs_calls','wall_seconds',
                                'diagnostic_minimum','diagnostic_maximum')},flush=True)


if __name__=='__main__':main()
