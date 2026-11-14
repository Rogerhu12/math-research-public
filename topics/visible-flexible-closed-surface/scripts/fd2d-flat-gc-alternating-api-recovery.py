#!/usr/bin/env python3
"""Optional, explicitly requested fixed-parameter initialization experiment.

This source reconstructs the previously unsuccessful alternating trials
and also exposes the as-yet-unexecuted common-Frobenius variant. It is not
part of the default bridge recovery and must not be a gate for the BVP.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,gzip,hashlib,io,json,resource,time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
from fd2d_gc_raw_bridge_api_snapshot_01 import RawLiftedDAE
from fd2d_flat_gc_codazzi_api_projector import FixedCodazziProjector


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_npz(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.gz'):raw=gzip.decompress(raw)
    return np.load(io.BytesIO(raw),allow_pickle=False)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',default='notes/2026-11-12-fd2d-api-bridge-recovery-01-amount075.npz')
    parser.add_argument('--source',default='notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    parser.add_argument('--stem',required=True)
    parser.add_argument('--repair',choices=('positive','spectral'),required=True)
    parser.add_argument('--norm',choices=('legacy','frobenius'),default='legacy')
    parser.add_argument('--iterations',type=int,required=True)
    parser.add_argument('--cap',type=float,default=7.)
    parser.add_argument('--codazzi-fraction',type=float,default=1.)
    args=parser.parse_args()
    if args.iterations<1:raise ValueError('Positive explicit iteration count required')
    if not 0<args.codazzi_fraction<=1:raise ValueError('Direction fraction must lie in (0,1]')
    started=time.time()
    if args.repair=='positive':
        from fd2d_gauss_curvature_cap import project_gauss_curvature_cap as repair
        repair_path=Path(__file__).resolve().parent/'fd2d_gauss_curvature_cap.py'
    else:
        from fd2d_spectral_gauss_api_cap import spectral_gauss_curvature_cap as repair
        repair_path=Path(__file__).resolve().parent/'fd2d_spectral_gauss_api_cap.py'
    stem=Path(args.stem);stem.parent.mkdir(parents=True,exist_ok=True)
    rp=Path(str(stem)+'-report.json')
    if rp.exists():raise FileExistsError('Use a new stem for a new actual run')
    saved=load_npz(args.input)
    model=RawLiftedDAE(args.source,modes=7,max_step=.04,gap=.91,
        profile_kind='positive_clock',tail_kind='positive_bernstein')
    if not np.array_equal(saved['x'],model.x):
        raise ValueError('Input and finite initialization grids differ')
    if str(saved['candidate_sha256'])!=sha(args.source):
        raise ValueError('The input binds another physical metric')
    initial=np.asarray(saved['vector'],float)
    y0,p=model.unpack(initial);p=p.copy()
    projector=FixedCodazziProjector(model,p,l_weight=.5 if args.norm=='legacy' else 1.)
    if args.norm=='frobenius':
        # n^2+2m^2+l^2 in physical radial quadrature and uniform xi.
        inverse=projector.inverse_weight.reshape(model.N-2,model.q)
        inverse[:,model.e:model.d]/=np.sqrt(2.)
        weighted=projector.C@sparse.diags(projector.inverse_weight)
        projector.row_scale=1/np.sqrt(np.asarray(weighted.multiply(weighted).sum(axis=1)).ravel())
        projector.A=sparse.diags(projector.row_scale)@weighted
        normal=(projector.A@projector.A.T).tocsc()
        projector.factor=splu(normal)
        projector.definition.update(norm='matrix Frobenius n^2+2m^2+l^2; uniform xi and radial quadrature',
            m_weight=float(np.sqrt(2.)),l_weight=1.,normal_nnz=int(normal.nnz),
            lu_nnz=int(projector.factor.L.nnz+projector.factor.U.nnz))
    lift=model.lifting(p[-1],p[model.K:-1])['values']
    K=np.asarray(model.operators(p[-1])['jet']['K'],float)[None,:]
    keep=np.zeros((model.work,model.N),bool);keep[:,[0,-1]]=True
    radial=.5*np.r_[model.h[0],model.h[:-1]+model.h[1:],model.h[-1]]
    rows=[];vectors=[];labels=[]
    def measure(vector,iteration,phase,extra=None):
        unused,data=model.evaluate(vector)
        d=model.diagnostics(vector,data)
        fields=data['fields']
        point=repair(fields[...,0],fields[...,1],fields[...,2],K,cap=args.cap,preserve=keep)
        dist=(point['n']-fields[...,0])**2+2*(point['m']-fields[...,1])**2+(point['l']-fields[...,2])**2
        d.update(iteration=iteration,phase=phase,
            codazzi_maximum=float(np.max(np.abs(data['codazzi_cells']))),
            projected_gauss_maximum=float(np.max(np.abs(data['projected_gauss']))),
            frobenius_gap_to_selected_pointwise_repair=float(np.sqrt(np.sum(dist*radial[None,:])/model.work)))
        if extra is not None:d.update(extra)
        y,pp=model.unpack(vector)
        d['fixed_parameters_and_endpoints_unchanged']=bool(np.array_equal(pp,p) and
            np.array_equal(y[[0,-1]],y0[[0,-1]]))
        if not d['fixed_parameters_and_endpoints_unchanged']:
            raise ArithmeticError('Physical parameter or endpoint mutation')
        d['index']=len(rows);rows.append(d);vectors.append(vector.copy())
        labels.append(str(iteration)+'_'+phase)
        return d,data
    base,unused=measure(initial,0,'input')
    vector=initial.copy()
    for it in range(1,args.iterations+1):
        unused,data=model.evaluate(vector)
        n,m,l=[data['fields'][...,j] for j in range(3)]
        point=repair(n,m,l,K,cap=args.cap,preserve=keep)
        target=np.stack((point['n'],point['m'],point['l']),axis=-1)
        correction=target-lift
        yy=np.concatenate(((model.PE@correction[...,0]).T,
                           (model.PO@correction[...,1]).T,
                           (model.PE@correction[...,2]).T),axis=1)
        yy[[0,-1]]=y0[[0,-1]]
        gauss=np.r_[yy.ravel(),p]
        grow,unused=measure(gauss,it,'after_pointwise_and_angular',
                           dict(pointwise_diagnostics=point['diagnostics']))
        vector,linear=projector.project(gauss,amount=args.codazzi_fraction)
        crow,unused=measure(vector,it,'after_codazzi',dict(linear_projection=linear))
        print(json.dumps({k:crow[k] for k in ('iteration','phase','residual_maximum',
            'full_gauss_node_maximum','formal_curvature_node_maximum','codazzi_maximum',
            'frobenius_gap_to_selected_pointwise_repair')}),flush=True)
        rp.write_text(json.dumps(dict(body_completed=False,initializer_only=True,
            rows=rows,elapsed_seconds=time.time()-started),indent=2)+'\n')
    best={k:min(rows,key=lambda r:r[k])['index'] for k in
        ('residual_maximum','full_gauss_node_maximum','formal_curvature_node_maximum')}
    cp=[r['frobenius_gap_to_selected_pointwise_repair'] for r in rows if r['phase']=='after_codazzi']
    mono_applicable=args.repair=='spectral' and args.norm=='frobenius' and args.codazzi_fraction==1.
    monotonic=dict(expected_for_exact_same_metric_projections=mono_applicable,
        maximum_observed_increase=max([cp[i+1]-cp[i] for i in range(len(cp)-1)]+[0.]),
        values=cp,not_an_existence_or_convergence_certificate=True)
    selected=[]
    for j,index in enumerate(sorted(set(best.values()))):
        vec=vectors[index];yy,pp=model.unpack(vec);unused,data=model.evaluate(vec)
        out=Path(str(stem)+f'-selected-{j+1:02d}.npz')
        buf=io.BytesIO()
        np.savez_compressed(buf,x=model.x,corrections=yy,parameters=pp,vector=vec,
            fields_n_m_l=data['fields'],material_u=model.coords['u'],
            candidate_sha256=np.array(sha(args.source)),modes=np.array(model.K),
            blend=np.array(model.blend),profile_kind=np.array(model.profile_kind),
            tail_kind=np.array(model.tail_kind),base_kind=np.array(model.base_kind),
            label=np.array(labels[index]),initializer_only=np.array(True))
        payload=buf.getvalue()
        if len(payload)>1000000:
            payload=gzip.compress(payload,compresslevel=9,mtime=0);out=Path(str(out)+'.gz')
        if len(payload)>=5000000:raise ValueError('Single artifact exceeds repository limit')
        out.write_bytes(payload)
        selected.append(dict(path=str(out),bytes=len(payload),sha256=sha(out),index=index))
    buf=io.BytesIO()
    np.savez_compressed(buf,vectors=np.asarray(vectors),labels=np.asarray(labels),x=model.x)
    allpath=Path(str(stem)+'-all-initialization-states.npz.gz')
    payload=gzip.compress(buf.getvalue(),compresslevel=9,mtime=0)
    if len(payload)>=5000000:raise ValueError('Split this optional trajectory before publishing')
    allpath.write_bytes(payload)
    report=dict(kind='optional_actual_alternating_initialization_only',body_completed=True,
        args=vars(args),input_sha256=sha(args.input),candidate_sha256=sha(args.source),
        projector=projector.definition,source_sha256={str(Path(__file__).name):sha(__file__),
            str(repair_path.name):sha(repair_path)},baseline=base,rows=rows,best=best,
        outputs=selected,all_states=dict(path=str(allpath),bytes=len(payload),sha256=sha(allpath)),
        monotonic_distance_diagnostic=monotonic,runtime_seconds=time.time()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        nonlinear_solution=False,continuous_certificate=False,
        fixed_parameters_and_endpoints_unchanged=all(r['fixed_parameters_and_endpoints_unchanged'] for r in rows))
    rp.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(body_completed=True,report=str(rp),report_sha256=sha(rp),
                         best=best,runtime_seconds=report['runtime_seconds'])),flush=True)


if __name__=='__main__':main()
