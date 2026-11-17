#!/usr/bin/env python3
"""A fixed thin-SVD combination of all 327 omitted velocity rows.

Reuse every ODE, analytic Jacobian, core row, QR and feasibility policy of
the frozen omitted-Z driver. Only the 109 right functions change to U.T v;
U and the parent vector are immutable inputs, without Sigma inverse.
Optional beta fixes the target to beta U.T v(parent); beta!=0 is not a
solution of the zero-target problem. No new solve is implied by this file.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

BASE=Path(__file__).with_name('2026-11-17-parallel-model-inward-omitted-velocity-bvp.py')
BASE_SHA='d6b9f58cf75f2e9dc0aa6777263d901edd71f4e5216eff3bbe82c59c8782b4eb'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read_state(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main(args):
    if not 0<=args.beta<=1:raise ValueError('Need beta in [0,1]')
    if sha(BASE)!=BASE_SHA:raise ValueError('The frozen complete BVP driver changed')
    spec=importlib.util.spec_from_file_location('complete_omitted_bvp',BASE)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    parent=read_state(args.target_parent);warm=read_state(args.input)
    parent_sha=sha(args.target_parent)
    if not parent.get('success') or not warm.get('success'):
        raise ValueError('Original parent and warm field must both be accepted')
    for key in ('M','N','inward_scalar_profile','fixed_scalar_profile','analytic_extension_origin'):
        if parent[key]!=warm[key]:raise ValueError('Incompatible parent/warm '+key)
    if parent['mesh'][-1]!=warm['mesh'][-1]:raise ValueError('This is duration zero')
    rows=json.loads(args.row_report.read_bytes());svd=json.loads(args.svd_report.read_bytes())
    if rows['input_sha256']!=parent_sha or svd['parent_sha256']!=parent_sha:
        raise ValueError('Both fixed operator reports must use the original parent')
    if svd['selection_report_sha256']!=sha(args.row_report):
        raise ValueError('The SVD and full-row reports do not match')
    if (rows['M'],rows['N'])!=(warm['M'],warm['N']):raise ValueError('Angular dimensions changed')
    array_path=args.svd_report.parent/svd['array_path']
    if sha(array_path)!=svd['array_sha256']:raise ValueError('Fixed SVD arrays changed')
    row_source=base.SCRIPTS/'parallel_20261117_omitted_reachable_rows.py'
    svd_source=base.SCRIPTS/'parallel_20261117_omitted_svd_boundary.py'
    if sha(row_source)!=rows['sources'][row_source.name] or sha(svd_source)!=svd['source_sha256']:
        raise ValueError('Frozen row/SVD source identity changed')
    r_spec=importlib.util.spec_from_file_location('immutable_full_omitted_rows',row_source)
    r_module=importlib.util.module_from_spec(r_spec);r_spec.loader.exec_module(r_module)
    with np.load(array_path,allow_pickle=False) as arrays:
        u=arrays['U'].copy();parent_raw=arrays['raw_parent_values'].copy()
        parent_combined=arrays['combined_parent_targets'].copy()
    m=warm['M'];free=m-3;n=3*m+2;left_count=2*m+5
    if u.shape!=(3*free,free) or parent_raw.shape!=(3*free,):raise ValueError('Fixed operator shape changed')
    u_sha=hashlib.sha256(np.asarray(u,dtype='<f8',order='C').tobytes(order='C')).hexdigest()
    if u_sha!=svd['U_float64_c_order_sha256']:raise ValueError('Fixed U coefficients changed')
    if not np.array_equal(parent_raw,np.asarray(rows['raw_values'])):
        raise ValueError('Original raw parent vector changed')
    target=args.beta*parent_combined;operator=u.T
    if np.max(abs(operator@parent_raw-parent_combined))>1e-12:
        raise ValueError('Combined parent vector does not equal U.T times its raw vector')
    previous=warm.get('fixed_omitted_svd_boundary')
    if previous and (previous['parent_sha256']!=parent_sha or previous['U_float64_c_order_sha256']!=u_sha):
        raise ValueError('A continuation stage must keep the original parent and U')
    old_boundary=base.OmittedVelocityBoundary
    class FixedSVD(old_boundary):
        def __init__(self,q,k,fixed=3):
            super().__init__(q,k,fixed);self.full=r_module.OmittedRows(q,k)
        def value(self,state):return operator@self.full.value(state)
        def jacobian(self,state):return operator@self.full.jacobian(state)
    base.OmittedVelocityBoundary=FixedSVD
    core=np.asarray(parent['core']['coefficients'][:3])
    shift=np.zeros(n);shift[1:4]=core-np.asarray(warm['core']['coefficients'][:3]);shift[left_count:]=target
    definition=dict(type='fixed_thin_svd_U_transpose_all_omitted_velocity',beta=args.beta,
        parent_sha256=parent_sha,row_report_sha256=sha(args.row_report),svd_report_sha256=sha(args.svd_report),
        array_sha256=sha(array_path),U_float64_c_order_sha256=u_sha,
        operator='U.T, no inverse singular values',raw_components=['R','T','Z'],
        candidate_modes=list(range(m+1,2*m-2)),candidate_rows=3*free,right_rows=free,
        all_ode_components=n,left_rows=left_count,core_targets=core.tolist(),
        parent_raw_values=parent_raw.tolist(),parent_combined_values=parent_combined.tolist(),
        right_target=target.tolist(),source_sha256=sha(__file__),base_driver_sha256=BASE_SHA)
    def bind(report):
        report['fixed_omitted_svd_boundary']=definition
        report['terminal_boundary']=definition.copy()
        report['terminal_projector']='none: fixed finite U.T combinations of raw omitted velocity'
    native_solve=base.solve_bvp
    def solve_with_target(fun,bc,x,y,**kw):
        def actual_bc(ya,yb):return bc(ya,yb)-shift
        config=args.out.with_suffix('.definition.json');record=json.loads(config.read_bytes())
        bind(record);config.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(dict(event='fixed_svd_bvp_start',beta=args.beta,
            actual_initial_boundary=float(np.max(abs(actual_bc(y[:,0],y[:,-1])))),
            parent_sha256=parent_sha,U_float64_c_order_sha256=u_sha)),flush=True)
        return native_solve(fun,actual_bc,x,y,**kw)
    base.solve_bvp=solve_with_target
    output=args.out;temporary=output.with_name(output.name+'.solver.gz')
    args.out=temporary;args.angles=warm['N'];args.fixed_modes=3;args.probe_only=False
    try:base.main(args)
    finally:args.out=output
    report=read_state(temporary);bind(report);report['scope']=__doc__
    actual=np.asarray(report.pop('right_raw_coefficients'))
    report['right_functional_values']=actual.tolist()
    report['right_functional_max']=report.pop('right_raw_coefficient_max')
    residual=actual-target;ya=np.asarray(report['states'][0])
    left=np.r_[ya[0]-1,ya[1:4]-core,2*np.arange(1,m+1)*ya[1:m+1]+ya[m+1:2*m+1],ya[2*m+1:]]
    report['boundary_residual_max']=float(max(np.max(abs(left)),np.max(abs(residual))))
    report['right_target_residual_max']=float(np.max(abs(residual)))
    report['right_target_residuals']=residual.tolist();report['core_fixed_targets']=core.tolist()
    profile_spec=warm['inward_scalar_profile']
    profile=base.InwardProfile(warm['fixed_scalar_profile']['geometry'],warm['analytic_extension_origin'],
        profile_spec['cut'],profile_spec['curvature'],profile_spec['ramp_in'],profile_spec['ramp_out'],profile_spec['quadrature'])
    a,ap,_=profile(float(warm['mesh'][-1]));q=base.Frenet(m,warm['N'])
    full=r_module.OmittedRows(q,ap/a).value(np.asarray(report['states'][-1]))
    report['full_raw_omitted_velocity_coefficients']=full.tolist()
    report['full_raw_omitted_velocity_max']=float(np.max(abs(full)))
    report['full_raw_component_maxima']={c:float(np.max(abs(v))) for c,v in zip(('R','T','Z'),np.split(full,3))}
    probe=report['initial_probe'];probe['functional_values']=probe.pop('raw_coefficients')
    probe['functional_max']=probe.pop('raw_coefficient_max');probe['functional_kind']='fixed U.T combinations'
    report['sources'].update({Path(__file__).name:sha(__file__),row_source.name:sha(row_source),svd_source.name:sha(svd_source)})
    output.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps(dict(event='fixed_svd_bvp_saved',beta=args.beta,success=report['success'],
        rms=report['collocation_rms_max'],boundary=report['boundary_residual_max'],
        full_raw_omitted_max=report['full_raw_omitted_velocity_max'],output_sha256=sha(output))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--target-parent',type=Path,required=True)
    p.add_argument('--row-report',type=Path,required=True);p.add_argument('--svd-report',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--beta',type=float,default=0.)
    p.add_argument('--tol',type=float,default=1e-8);p.add_argument('--bc-tol',type=float,default=1e-11)
    p.add_argument('--max-nodes',type=int,default=1800)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    main(p.parse_args())
