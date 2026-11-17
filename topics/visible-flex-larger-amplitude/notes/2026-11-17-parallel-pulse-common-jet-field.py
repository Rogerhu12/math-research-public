#!/usr/bin/env python3
"""Actual C2 local field for the explicit pulse scalar, sharing the old cut jets.

Reuses the frozen nodal integrator and six-jet geometry reader. The scalar
adapter is explicit and only local to this module instance. Each cell is
the unique quintic of its stored shared two-jets; the first overlap uses
the R637 Hermite correction. This is a new map, not an accepted full BVP.
"""
import argparse,copy,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def module(name,filename,expected):
    path=ROOT/filename
    if sha(path)!=expected:raise ValueError('Frozen source changed: '+filename)
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj,path
field,FIELD=module('pulse_common_jet_reader','2026-11-17-parallel-geometry-short-ivp-field.py',
 'ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924')
pulse,PULSE=module('explicit_compact_pulse','2026-11-17-parallel-inward-curvature-pulse.py',
 '148dd6305df67c881ceb180249f4eaf34e3a996a6568c7378be467d41a92d157')

def bridge(data,parent,j):
    x=np.asarray(data['mesh']);Y=np.asarray(data['states']);V=np.asarray(data['rhs']);A=np.asarray(data['d2'])
    if not 1<=j<len(x):raise ValueError('Need a true interior join node')
    if x[0]!=parent['mesh'][-1]:raise ValueError('Different initial cut')
    old=data['old_cut_jets'];y0=np.asarray(old['value']);v0=np.asarray(old['first']);a0=np.asarray(old['second'])
    if not np.array_equal(Y[0],y0):raise ValueError('Different initial position')
    saved_v=field.lift(np.asarray(parent['rhs'][-1]),parent['M'],data['M'])
    if not np.array_equal(saved_v,v0):raise ValueError('Original saved and recomputed first jets differ')
    dv=V[0]-v0;da=A[0]-a0;w=x[j]-x[0]
    p=np.array([0.,1.,0.,-6.,8.,-3.]);q=np.array([0.,0.,.5,-1.5,1.5,-.5])
    for i in range(1,j):
        u=(x[i]-x[0])/w
        for order,target in [(0,Y),(1,V),(2,A)]:
            pp=np.polynomial.polynomial.polyder(p,order);qq=np.polynomial.polynomial.polyder(q,order)
            target[i]-=w**(1-order)*np.polynomial.polynomial.polyval(u,pp)*dv+w**(2-order)*np.polynomial.polynomial.polyval(u,qq)*da
    Y[0]=y0;V[0]=v0;A[0]=a0
    definition=dict(join_index=j,cut=float(x[0]),end=float(x[j]),width=float(w),
        first_basis=p.tolist(),second_basis=q.tolist(),
        formula='F_new=F_local-w*p(u)*delta_first-w^2*q(u)*delta_second',
        exact_shared_initial_jets=True,exact_unchanged_jets_from_join=True,
        old_prefix_is_unchanged=True,common_physical_density=True,
        source_local_field_sha256=data['frozen_local_field_sha256'])
    out=copy.deepcopy(data);out.update(states=Y.tolist(),rhs=V.tolist(),d2=A.tolist(),
        schema='pulse-explicit-local-C2-jet-bridge-v1',ivp_reached_end=False,
        source_ivp_reached_end=True,bvp_accepted=False,complete_prefix=False,
        old_prefix_C2_join_completed=True,explicit_jet_bridge=definition,
        geometry_definition='Unique quintic matching stored shared 0/1/2 jets in every cell')
    return out

def main(args):
    ref=json.loads(gzip.decompress(args.reference.read_bytes()));metric=json.loads(gzip.decompress(args.metric.read_bytes()))
    if not ref.get('success'):raise ValueError('An accepted old prefix is required')
    z=metric['inward_scalar_profile']
    profile=pulse.PulseProfile(ref['fixed_scalar_profile']['geometry'],ref['analytic_extension_origin'],
        z['cut'],z['curvature'],z['ramp_in'],z['ramp_out'],z['quadrature'],args.amplitude,args.half_width)
    # The reused integrator calls this factory once. Never use the unpulsed
    # scalar for either ODE jets or the subsequent metric/curvature read.
    field.h.profile_from=lambda unused:profile
    result=dict(scope=__doc__,source_sha256=sha(__file__),pulse_source_sha256=sha(PULSE),
        common_jet_source_sha256=sha(FIELD),reference_sha256=sha(args.reference),
        metric_carrier_sha256=sha(args.metric),scalar=profile.spec(),fields=[])
    for N in args.angles:
        record,data=field.nodal_field(args,ref,metric,N)
        if data is not None:
            data.update(scope=__doc__,inward_scalar_profile=profile.spec(),
                source_sha256=sha(__file__),common_jet_source_sha256=sha(FIELD),
                pulse_source_sha256=sha(PULSE),unmodified_inward_profile_sha256=data['inward_profile_sha256'])
            local_path=Path(record['field_path'])
            local_path.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))
            record['field_sha256']=sha(local_path)
            data['frozen_local_field_sha256']=record['field_sha256']
            joined=bridge(data,ref,args.join_index)
            joined_path=Path(str(args.output_stem)+f'-n{N}-c2.json.gz')
            joined_path.write_bytes(gzip.compress((json.dumps(joined)+'\n').encode(),mtime=0))
            record.update(c2_field_path=str(joined_path),c2_field_sha256=sha(joined_path),
                bridge=joined['explicit_jet_bridge'],
                actual_C2_quintic=field.read_field(joined,profile,args.read_angles,args.radial_subdivisions))
        result['fields'].append(record)
        report=Path(str(args.output_stem)+'-report.json');report.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(record),flush=True)
    print(json.dumps(dict(report=str(report),report_sha256=sha(report))),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('reference','metric','output-stem'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--amplitude',type=float,default=-5.);p.add_argument('--half-width',type=float,default=.005)
    p.add_argument('--modes',type=int,default=320);p.add_argument('--angles',nargs='+',type=int,default=[4096])
    p.add_argument('--read-angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
    p.add_argument('--join-index',type=int,default=32);p.add_argument('--end',type=float,default=1.)
    p.add_argument('--max-step',type=float,default=.000015625)
    p.add_argument('--rtol',type=float,default=1e-13);p.add_argument('--atol',type=float,default=1e-16)
    p.add_argument('--keep-terminal-microcells',action='store_true');main(p.parse_args())
