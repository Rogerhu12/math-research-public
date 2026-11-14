#!/usr/bin/env python3
"""Floating positive comparison weights with complete degree-seven time data."""
from __future__ import annotations
import argparse,gzip,io,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from fourfold_codazzi_positive_weights_probe import WeightEvolution
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha
from fourfold_phase_codazzi_dense_candidate import positive_hermitian
from fourfold_codazzi_sharded_candidate import ShardedDenseCandidate
from fourfold_codazzi_positive_weight_candidate import KIND,pack,DenseWeightCandidate


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--right',type=Fraction,default=Fraction(1,5))
    ap.add_argument('--angles',type=int,default=512);ap.add_argument('--grid',type=int,default=2048)
    ap.add_argument('--smoothing',type=float,default=3.);ap.add_argument('--max-step',type=float,default=.0005)
    ap.add_argument('--rtol',type=float,default=2e-10);ap.add_argument('--atol',type=float,default=2e-12)
    ap.add_argument('--raw',type=Path,required=True);ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();tick=time.monotonic()
    if any(p.exists() for p in (a.raw,a.manifest,a.out)):raise FileExistsError('new complete weight paths required')
    geometry,_=load_exact_object(a.object,512);candidate=ShardedDenseCandidate(a.candidate)
    if a.angles%2 or a.grid<max(2*a.angles,2*candidate.grid) or a.smoothing<=0:
        raise ValueError('positive complete Fourier support and smoothing required')
    if candidate.metadata['object_sha256']!=sha(a.object):raise ValueError('actual target mismatch')
    right=float(a.right)
    if Fraction.from_float(right)<a.right:right=float(np.nextafter(right,np.inf))
    if right>candidate.nodes[-1]:raise ValueError('complete candidate interval is insufficient')
    rhs=WeightEvolution(geometry,candidate,a.angles,a.grid,a.smoothing)
    stages=sorted({0.,right}|{float(x) for x in candidate.nodes if 0<x<right})
    initial=np.zeros((a.angles//2,2),complex);initial[0]=1
    nodes=[0.];ends=[initial];corrections=[];diagnostic=[];state=np.ones(2*a.angles)
    replacement=0.
    for stage,(left,end) in enumerate(zip(stages,stages[1:])):
        solver=DOP853(rhs,left,state,end,rtol=a.rtol,atol=a.atol,max_step=a.max_step)
        while solver.status=='running':
            message=solver.step()
            if solver.status=='failed':raise ValueError('floating dense weight solver failed: '+str(message))
            dense=solver.dense_output();value=positive_hermitian(solver.y.reshape(a.angles,2))
            higher=np.stack([positive_hermitian(v.reshape(a.angles,2)) for v in dense.F[1:]])
            f0=positive_hermitian(dense.F[0].reshape(a.angles,2))
            replacement=max(replacement,float(np.sum(abs(value-ends[-1]-f0))))
            nodes.append(float(solver.t));ends.append(value);corrections.append(higher)
        state=solver.y
        row=dict(stage=stage,r=end,minimum=float(state.min()),maximum=float(state.max()))
        diagnostic.append(row)
        if stage%30==0:print(row,flush=True)
    nodes=np.asarray(nodes);ends=np.asarray(ends);corrections=np.asarray(corrections)
    metadata=dict(kind=KIND,positivity_certified=False,weight_inequalities_certified=False,
        continuation_certified=False,all_coefficients_exact_dyadic=True,mean_retained=True,
        angular_grid=a.angles,full_evaluation_grid=a.grid,physical_frequencies='4*k; exact negative conjugates; real mean; Nyquist zero',
        initial_weights_exactly_one=True,shared_endpoint_continuity_exact=True,radial_derivative_continuity_claimed=False,
        polynomial_contract='(1-x)L+xR+x(1-x)*(F1+x*(F2+(1-x)*(F3+x*(F4+(1-x)*(F5+x*F6))))))',
        time_nodes_exact_fractions=[str(Fraction.from_float(float(x))) for x in nodes],
        exact_requested_right=str(a.right),source_sha256=sha(__file__),object_sha256=sha(a.object),
        candidate_manifest_sha256=sha(a.candidate),candidate_original_sha256=candidate.original_payload_sha256,
        exact_center_parameter=candidate.metadata['exact_center_parameter'],smoothing=a.smoothing)
    buffer=io.BytesIO();np.savez(buffer,time_nodes=nodes,positive_endpoint_coefficients=ends,
                               positive_dense_corrections=corrections,metadata=np.array(json.dumps(metadata)))
    a.raw.write_bytes(gzip.compress(buffer.getvalue(),compresslevel=6,mtime=0))
    storage=pack(a.raw,a.manifest)
    loaded=DenseWeightCandidate(a.manifest)
    if loaded.original_payload_sha256!=sha(a.raw):raise ValueError('exact stored dense weight identity differs')
    report=dict(**metadata,complete=True,certified=False,pieces=len(nodes)-1,
        raw_sha256=sha(a.raw),raw_bytes=a.raw.stat().st_size,
        manifest=str(a.manifest),manifest_sha256=sha(a.manifest),parts=len(storage['shards']),
        rtol=a.rtol,atol=a.atol,max_step=a.max_step,rhs_calls=rhs.calls,
        maximum_endpoint_replacement_l1=replacement,diagnostic_samples=diagnostic,
        source_dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_positive_weights_probe.py','fourfold_codazzi_positive_weight_candidate.py',
            'fourfold_codazzi_sharded_candidate.py','fourfold_phase_codazzi_dense_candidate.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_local_correction_probe.py',
            'fourfold_phase_codazzi_evolution_probe.py','fourfold_phase_geometry.py')},
        wall_seconds=time.monotonic()-tick,
        scope='A complete exact finite auxiliary comparison function chosen by floating arithmetic. Positivity, weight residuals, true-tube closure and PDE continuation are not certified.')
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print({k:report[k] for k in ('complete','pieces','raw_bytes','parts','wall_seconds')},flush=True)


if __name__=='__main__':main()
