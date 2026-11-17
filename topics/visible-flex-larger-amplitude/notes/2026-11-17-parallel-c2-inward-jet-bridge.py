#!/usr/bin/env python3
"""An explicit common-jet bridge from the old prefix to a short high-M field.

This changes the actual map on a finite overlap. It is not an accepted BVP
or a proof of fixed-metric refinement. The supplied immutable parent and
local field define the two sides; shared binary 0/1/2 jets define C2 seams.
Only the new local bridge is sampled here, not the already-read old prefix.
"""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

READER=Path(__file__).with_name('2026-11-17-parallel-geometry-short-ivp-field.py')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(args):
    parent_raw=args.parent.read_bytes();field_raw=args.field.read_bytes()
    parent=json.loads(gzip.decompress(parent_raw))
    original=json.loads(gzip.decompress(field_raw))
    if not parent.get('success') or not original.get('ivp_reached_end'):
        raise ValueError('Need the accepted original prefix and a completed local IVP')
    parent_sha=hashlib.sha256(parent_raw).hexdigest()
    if original['reference_sha256']!=parent_sha:
        raise ValueError('The local trajectory does not start from this parent')
    if sha(READER)!=original['source_sha256']:
        raise ValueError('The frozen common-jet reader identity changed')
    spec=importlib.util.spec_from_file_location('frozen_local_common_jets',READER)
    reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
    profile=reader.h.profile_from(original)
    old=reader.h.Frenet(parent['M'],parent['N']);lift=reader.lift
    M=original['M'];x=np.asarray(original['mesh']);ys=np.asarray(original['states'])
    dy=np.asarray(original['rhs']);ddy=np.asarray(original['d2'])
    j=args.join_index
    if not 1<=j<len(x):raise ValueError('Join index must be an interior or final actual node')
    if x[0]!=parent['mesh'][-1]:raise ValueError('The common cut is not an exact shared node')
    core=np.pad(np.asarray(parent['core']['coefficients']),(0,M-parent['M']))
    if not np.array_equal(core,np.asarray(original['original_core_coefficients'])):
        raise ValueError('The actual original density changed')
    old_y=np.asarray(parent['states'][-1]);old_v=np.asarray(parent['rhs'][-1])
    a,ap,app=profile(float(x[0]));k=ap/a
    old_acc=old.jvp(old_y,k,old_v,dk=app/a-k*k)
    y0=lift(old_y,old.M,M);v0=lift(old_v,old.M,M);a0=lift(old_acc,old.M,M)
    if not np.array_equal(y0,ys[0]):raise ValueError('The cut positions differ')
    delta_v=dy[0]-v0;delta_a=ddy[0]-a0;width=float(x[j]-x[0])
    p1=np.array([0.,1.,0.,-6.,8.,-3.])
    p2=np.array([0.,0.,.5,-1.5,1.5,-.5])
    d1=np.arange(1,6)*p1[1:];d2=np.arange(1,6)*p2[1:]
    dd1=np.arange(2,6)*np.arange(1,5)*p1[2:]
    dd2=np.arange(2,6)*np.arange(1,5)*p2[2:]
    Y,V,A=ys.copy(),dy.copy(),ddy.copy()
    for i in range(1,j):
        u=float((x[i]-x[0])/width)
        Y[i]-=width*np.polynomial.polynomial.polyval(u,p1)*delta_v+width**2*np.polynomial.polynomial.polyval(u,p2)*delta_a
        V[i]-=np.polynomial.polynomial.polyval(u,d1)*delta_v+width*np.polynomial.polynomial.polyval(u,d2)*delta_a
        A[i]-=np.polynomial.polynomial.polyval(u,dd1)/width*delta_v+np.polynomial.polynomial.polyval(u,dd2)*delta_a
    # Bind both interfaces by exact shared data, not approximate evaluation
    # of Hermite basis endpoint identities in floating arithmetic.
    Y[0]=y0;V[0]=v0;A[0]=a0
    definition=dict(parent_sha256=parent_sha,local_field_sha256=hashlib.sha256(field_raw).hexdigest(),
        join_index=j,cut=float(x[0]),end=float(x[j]),width=width,
        first_basis=p1.tolist(),second_basis=p2.tolist(),
        formula='F_new=F_local-width*p1(u)*delta_first-width^2*p2(u)*delta_second',
        initial_position_equal=bool(np.array_equal(Y[0],y0)),
        initial_first_equal=bool(np.array_equal(V[0],v0)),
        initial_second_equal=bool(np.array_equal(A[0],a0)),
        final_position_equal=bool(np.array_equal(Y[j:],ys[j:])),
        final_first_equal=bool(np.array_equal(V[j:],dy[j:])),
        final_second_equal=bool(np.array_equal(A[j:],ddy[j:])),
        original_recorded_first_difference=float(np.max(abs(np.asarray(original['old_cut_jets']['first'])-v0))),
        original_recorded_second_difference=float(np.max(abs(np.asarray(original['old_cut_jets']['second'])-a0))),
        old_prefix_is_unchanged=True,common_physical_density=True,
        source_sha256=sha(__file__),reader_sha256=sha(READER))
    data=copy.deepcopy(original);data.update(schema='explicit-local-C2-jet-bridge-v1',scope=__doc__,
        states=Y.tolist(),rhs=V.tolist(),d2=A.tolist(),
        bvp_accepted=False,complete_prefix=False,old_prefix_C2_join_completed=True,
        geometry_definition='Unique quintic matching stored shared 0/1/2 jets in every cell',
        old_cut_jets=dict(value=y0.tolist(),first=v0.tolist(),second=a0.tolist()),
        explicit_jet_bridge=definition)
    data['ivp_reached_end']=False
    data['source_ivp_reached_end']=True
    data['source_sha256']=sha(__file__)
    args.out.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))
    report=dict(scope=__doc__,bridge=definition,bridge_field_sha256=sha(args.out),
        actual_local_quintic=reader.read_field(data,profile,args.angles,args.radial_subdivisions),
        full_prefix_readout_performed=False,closed_surface=False,reach_certificate=False,
        fixed_metric_refinement_complete=False)
    report_path=args.out.with_suffix('.readout.json')
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    print(json.dumps(dict(report_path=str(report_path),report_sha256=sha(report_path))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent',type=Path,required=True);p.add_argument('--field',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--join-index',type=int,default=32)
    p.add_argument('--angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
    main(p.parse_args())
