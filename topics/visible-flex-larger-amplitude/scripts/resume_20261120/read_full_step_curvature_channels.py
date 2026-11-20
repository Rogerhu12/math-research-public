#!/usr/bin/env python3
"""Attribute an actually computed complete step's curvature differential.

This only reads selected actual physical points; no new nonlinear direction,
no repeated global Gram probe, and no continuous maximum certificate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def parse_point(text):
    cell,u,phi=text.split(',')
    return int(cell),float(u),float(phi)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--bundle',type=Path,required=True)
    ap.add_argument('--direction',type=Path,required=True)
    ap.add_argument('--point-source',type=Path,required=True)
    ap.add_argument('--geometry-source',type=Path,required=True)
    ap.add_argument('--point',type=parse_point,action='append',required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Use a fresh actual diagnostic path')
    topic=a.repo/'topics/visible-flex-larger-amplitude'
    dense_path=topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    observed_path=topic/'scripts/resume_20261120/gauss_observed_closed_gram.py'
    dense=load('curvature_channel_dense',dense_path)
    observed=load('curvature_channel_weights',observed_path)
    point=load('curvature_channel_point',a.point_source)
    geometry=load('curvature_channel_geometry',a.geometry_source)
    data=np.load(a.bundle,allow_pickle=False)
    M=(data['qjets'].shape[-1]-2)//3
    q=dense.ClosedGram(data['mesh'],data['a_stages'],float(data['radius']),
        data['fixed_core_first3'],M=M,N=2,width=float(data['width']))
    x,affine=q.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    step=np.load(a.direction,allow_pickle=False)['step']
    if step.shape!=x.shape:raise ValueError('The actual direction has a different full-free space')
    p=q.prepare(x);pc=q.prepare(x+1j*1e-30*step);pfull=q.prepare(x+step)
    nc=M-q.K;na0=2*M+1;start=nc+na0
    jet_step=step[start:-1].reshape(q.J-2,3,q.n)
    modes=np.r_[np.arange(M+1),np.arange(1,M+1),np.arange(M+1)]
    bands=[('mean',0,0),('m1_to_12',1,12),('m13_to_32',13,32),
           ('m33_to_80',33,80),('m81_to_160',81,M)]
    records=[]
    for cell,u,phi in a.point:
        fields=point.fields_at(q,p,cell,u,phi,observed)
        branches=[geometry.curvature_cotangent(fields,j)for j in (0,1)]
        branch=int(np.argmax([abs(v[0])for v in branches]))
        k,cot,meta=branches[branch]
        free_covector=point.pullback_at(q,p,cell,u,phi,cot,observed)
        contributions=free_covector*step
        jet_product=contributions[start:-1].reshape(q.J-2,3,q.n)
        core=float(contributions[:nc].sum());core_A=float(contributions[nc:start].sum())
        height=float(contributions[-1]);interior=float(jet_product.sum())
        by_jet=jet_product.sum(axis=(0,2));by_jet[2]+=core_A
        by_band=[]
        for name,low,high in bands:
            mask=(modes>=low)&(modes<=high)
            v=jet_product[:,:,mask].sum(axis=(0,2))
            v[2]+=float(contributions[nc:start][mask[:na0]].sum())
            free_modes=np.arange(q.K+1,M+1)
            core_band=float(contributions[:nc][(free_modes>=low)&(free_modes<=high)].sum())
            by_band.append(dict(band=name,minimum_mode=low,maximum_mode=high,
                Y_U_A=v.tolist(),core=core_band,total=float(v.sum()+core_band),
                interior_sum_absolute_coefficient_products=float(np.abs(jet_product[:,:,mask]).sum())))
        fc=point.fields_at(q,pc,cell,u,phi,observed)
        physical={key:float(cot[key]@(np.imag(fc[key])/1e-30))for key in fields}
        full_fields=point.fields_at(q,pfull,cell,u,phi,observed)
        actual=[geometry.curvature_cotangent(full_fields,j)[0]for j in (0,1)]
        total=float(contributions.sum())
        records.append(dict(cell=cell,u=u,phi=phi,
            s=float(q.mesh[cell]+u*(q.mesh[cell+1]-q.mesh[cell])),
            selected_parent_branch=branch,parent_signed_kappa=k,
            actual_full_step_principal_curvatures=actual,
            actual_full_step_maximum_absolute_curvature=max(abs(v)for v in actual),
            predicted_signed_kappa_differential=total,
            parent_plus_linear_prediction=k+total,
            raw_free_channels=dict(core=core,core_horizontal_A=core_A,interior=interior,H=height),
            nodal_Y_U_A_differential=by_jet.tolist(),fourier_mode_bands=by_band,
            physical_sixjet_channels=physical,
            decomposition_sum_discrepancy=float(sum(physical.values())-total),
            principal_metadata=meta))
    report=dict(schema='actual-full-step-curvature-channel-readout-v1',
        source_sha256=sha(__file__),bundle_sha256=sha(a.bundle),direction_sha256=sha(a.direction),
        source_sha256_by_role=dict(dense=sha(dense_path),observed=sha(observed_path),
            point=sha(a.point_source),geometry=sha(a.geometry_source)),
        original_variables=q.free_size,M=M,affine=affine,records=records,
        scope='First-order signed curvature contributions at actual points of the parent; signed cancellations retained, not a global or continuous curvature bound',
        new_solve_performed=False)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)


if __name__=='__main__':main()
