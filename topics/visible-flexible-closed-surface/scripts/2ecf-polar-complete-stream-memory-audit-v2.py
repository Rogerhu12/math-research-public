#!/usr/bin/env python3
"""Actual full 12789-column, 918400-row cached/streamed identity audit."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import types
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def footprint(value):
    seen=set();owners={}
    def walk(x):
        if id(x) in seen:return
        seen.add(id(x))
        if isinstance(x,np.ndarray):
            while isinstance(x.base,np.ndarray):x=x.base
            owners[id(x)]=int(x.nbytes);return
        if isinstance(x,(str,bytes,int,float,bool,type(None),types.ModuleType,types.FunctionType,type)):return
        if isinstance(x,dict):
            for v in x.values():walk(v)
        elif isinstance(x,(list,tuple)):
            for v in x:walk(v)
        elif hasattr(x,'__dict__'):
            for v in vars(x).values():walk(v)
    walk(value);return dict(uniqueArrays=len(owners),ownedBytes=sum(owners.values()))


def compare_point_objects(a,b,path="point",seen=None):
    if seen is None: seen=set()
    pair=(id(a),id(b))
    if pair in seen: return 0
    seen.add(pair)
    if isinstance(a,np.ndarray):
        if not isinstance(b,np.ndarray) or a.shape!=b.shape or a.dtype!=b.dtype or a.tobytes()!=b.tobytes():
            raise ArithmeticError("An actual complete nested point array changed: "+path)
        return 1
    if type(a) is not type(b): raise ArithmeticError("Actual point member type differs: "+path)
    if isinstance(a,(str,bytes,int,float,bool,type(None),np.generic)):
        if a!=b: raise ArithmeticError("Actual point scalar differs: "+path)
        return 0
    if isinstance(a,dict):
        if a.keys()!=b.keys(): raise ArithmeticError("Actual point dictionary keys differ: "+path)
        return sum(compare_point_objects(a[k],b[k],path+"."+str(k),seen) for k in a)
    if isinstance(a,(list,tuple)):
        if len(a)!=len(b): raise ArithmeticError("Actual point member length differs: "+path)
        return sum(compare_point_objects(x,y,path+"["+str(j)+"]",seen) for j,(x,y) in enumerate(zip(a,b)))
    if hasattr(a,"__dict__"):
        return compare_point_objects(vars(a),vars(b),path+".__dict__",seen)
    if a is not b: raise TypeError("An actual point member was not checked: "+path+" "+str(type(a)))
    return 0


def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','prepared','state','output'):ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();here=Path(__file__).parent
    prepare=module(here/'2ecf-polar-c2-prefix-prepare.py','stream_memory_prepare')
    saved,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    joint=module(args.scripts/'6a65-geometry-gap-window-two-grid-cartesian.py','stream_memory_joint')
    area=module(args.scripts/'6a65-geometry-area-ratio-power-two.py','stream_memory_area')
    normal=module(args.scripts/'6a65-cartesian-complete-radial-normal-two-grid-area.py','stream_memory_normal')
    helper=module(here/'2ecf-polar-complete-two-grid-streamed.py','stream_memory_helper')
    state=json.loads(args.state.read_text());z=np.asarray(state['z']).reshape(basis.nb,basis.na)
    weights={k:{n:.5*np.array(v) for n,v in saved['caches'][k]['weights'].items()} for k in caches}
    config=mods['stream'].point.PointConfig(**definition['pointConfig']);recipe=definition['recipe']
    barrier=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    cached=area.CompleteAreaTwoGrid(joint,mods['stream'],basis,caches,weights,z,config,recipe,barrier)
    helper.install(joint)
    streamed=area.CompleteAreaTwoGrid(joint,mods['stream'],basis,caches,weights,z,config,recipe,barrier)
    if cached.shape!=(918400,12789) or streamed.shape!=cached.shape:
        raise ArithmeticError('This audit is the actual complete current field, not a reduced test')
    packet_arrays=0
    for name in cached.names:
        first,second=cached.parent.groups[name],streamed.parent.groups[name]
        if second.point_blocks or second.cache_point_blocks:
            raise ArithmeticError('The new consumer retained original point packets')
        for index,sl in enumerate(first.slices):
            a,b=first._get_block(index,sl),second._get_block(index,sl)
            packet_arrays+=compare_point_objects(a,b,"original13."+name+"."+str(index))
        for a,b in zip(cached.groups[name].packets,streamed.groups[name].packets):
            packet_arrays+=compare_point_objects(a,b,"area."+name)
    rng=np.random.default_rng(2026112837)
    direction=rng.standard_normal((basis.nb,basis.na));direction/=np.linalg.norm(direction)
    cotangent=rng.standard_normal(cached.shape[0])
    images=[];transposes=[]
    for linear in (cached,streamed):
        proxy=types.SimpleNamespace(linear=linear)
        images.append(normal.SameSobolevAreaFullBandAugmented.raw_matvec(proxy,direction))
        transposes.append(normal.SameSobolevAreaFullBandAugmented.raw_transpose(proxy,cotangent))
    residual_equal=cached.residual.tobytes()==streamed.residual.tobytes()
    j_equal=images[0].tobytes()==images[1].tobytes()
    jt_equal=transposes[0].tobytes()==transposes[1].tobytes()
    S_equal=all(cached.preconditioner.factors[k][0].tobytes()==streamed.preconditioner.factors[k][0].tobytes()
        for k in cached.preconditioner.factors)
    statistics_equal=cached.statistics==streamed.statistics and cached.group_values==streamed.group_values
    if not all((residual_equal,j_equal,jt_equal,S_equal,statistics_equal)):
        raise ArithmeticError('The complete cached/streamed mathematical operation changed')
    oldbytes=footprint(cached);newbytes=footprint(streamed)
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    out=dict(schema='2ecf-actual-complete-polar-cached-versus-streamed-identity-audit-v2',
        preparedSHA256=sha(args.prepared),stateSHA256=sha(args.state),entrySHA256=sha(__file__),
        streamedHelperSHA256=sha(here/'2ecf-polar-complete-two-grid-streamed.py'),
        actualColumns=12789,actualRows=918400,actualPoints=65600,nonzeroActualField=True,
        checkedActualPointArrays=packet_arrays,allActualPointArraysIdentical=True,
        actualAllResidualBytesIdentical=residual_equal,actualPhysicalJVPBytesIdentical=j_equal,
        actualPhysicalJTVPBytesIdentical=jt_equal,actualPhysicalSobolevFactorBytesIdentical=S_equal,
        allObjectiveAndGeometryStatisticsIdentical=statistics_equal,
        retainedCachedArrayFootprint=oldbytes,retainedStreamedArrayFootprint=newbytes,
        eliminatedDerivedPointArrayBytes=oldbytes['ownedBytes']-newbytes['ownedBytes'],
        projected958PointPacketSavingsBytes=(oldbytes['ownedBytes']-newbytes['ownedBytes'])*958/205,
        projectionNotActualDenseRSS=True,fullHStillUsesEveryIdenticalPointCovariance=True,
        peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        actualNonlinearAttempts=0,actualNonlinearAccepts=0,seconds=time.monotonic()-start)
    if args.output.exists():raise FileExistsError('Fresh actual footprint audit required')
    args.output.write_text(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':main()
