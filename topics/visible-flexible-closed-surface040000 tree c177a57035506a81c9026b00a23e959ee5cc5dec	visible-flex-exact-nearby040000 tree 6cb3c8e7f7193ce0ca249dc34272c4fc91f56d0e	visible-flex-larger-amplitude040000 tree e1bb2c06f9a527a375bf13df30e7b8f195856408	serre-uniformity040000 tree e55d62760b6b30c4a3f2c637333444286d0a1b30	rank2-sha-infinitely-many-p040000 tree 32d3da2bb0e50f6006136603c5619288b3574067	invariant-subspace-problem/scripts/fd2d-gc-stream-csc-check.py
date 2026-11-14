#!/usr/bin/env python3
"""One actual-state algebra check of the stream CSC change, not another BVP."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,importlib.util,io,json,time
from pathlib import Path
import numpy as np
from fd2d_gc_intrinsic import identity
import fd2d_gc_stream_csc as streaming


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for arg in ('candidate','linear-tail','warm-field','output'):p.add_argument('--'+arg,type=Path,required=True)
    a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    source=Path(__file__).resolve().with_name('fd2d-gc-bvp-design-warm.py')
    spec=importlib.util.spec_from_file_location('actual_warm_csc_check',source)
    warm=importlib.util.module_from_spec(spec);spec.loader.exec_module(warm)
    profile=warm.CoastDesignProfile(a.candidate);geometry=warm.FixedBalancedGeometry()
    flow=warm.DesignLogShapeGC(profile,95,2,reference=warm.CertifiedReference(geometry),blend_interval=[.58,1.40])
    problem=warm.Problem(flow,geometry,json.loads(a.linear_tail.read_text()),.00008,{})
    raw=a.warm_field.read_bytes()
    if a.warm_field.name.endswith('.gz'):raw=gzip.decompress(raw)
    with np.load(io.BytesIO(raw)) as z:
        mesh=z['mesh'];values=z['values'];parameters=z['parameters'].copy()
    indices=np.unique(np.linspace(0,len(mesh)-1,9).astype(int));x=mesh[indices];y=values[:,indices]
    n,m=y.shape;k=len(parameters);h=np.diff(x)
    args=(n,m,k,problem.fun,problem.bc,problem.fun_jac,problem.bc_jac,x,h)
    old_fun,old_jac=streaming.ORIGINAL_PREPARE(*args);new_fun,new_jac=streaming.prepare_sys(*args)
    residual,ym,f,fm=old_fun(y,parameters);br=problem.bc(y[:,0],y[:,-1],parameters)
    began=time.monotonic();old=old_jac(y,parameters,ym,f,fm,br);old_seconds=time.monotonic()-began
    began=time.monotonic();new=new_jac(y,parameters,ym,f,fm,br);new_seconds=time.monotonic()-began
    difference=old-new;largest=float(np.max(abs(difference.data),initial=0.))
    scale=max(1.,float(np.max(abs(old.data),initial=0.)))
    vector=np.sin(np.arange(old.shape[0])*.173)+np.cos(np.arange(old.shape[0])*.317)
    mv=float(np.max(abs(old@vector-new@vector)))
    residual_new=new_fun(y,parameters)[0]
    passed=largest<=64*np.finfo(float).eps*scale and np.array_equal(residual,residual_new)
    report=dict(schema='fd2d-actual-warm-state-csc-assembly-check-v1',passed=bool(passed),
        mathematical_claim='same Lobatto residual and full analytic Jacobian; only storage representation changes',
        another_BVP_solved=False,maximum_mode=95,dimension=n,nodes=m,parameters=k,
        actual_mesh_indices=indices.tolist(),inputs=[identity(z) for z in (a.candidate,a.linear_tail,a.warm_field)],
        sources=[identity(z) for z in (Path(__file__),Path(streaming.__file__),source)],
        maximum_entry_difference=largest,maximum_entry_scale=scale,
        maximum_entry_relative_difference=largest/scale,matrix_vector_difference=mv,
        residual_bitwise_equal=bool(np.array_equal(residual,residual_new)),
        original_stored_entries=int(old.nnz),stream_stored_entries=int(new.nnz),
        last_parameter_nonzero_collocation_entries=int(np.count_nonzero(new[:n*(m-1),-1].data)),
        original_seconds=old_seconds,stream_seconds=new_seconds,stream_status=dict(streaming.STATUS))
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()
