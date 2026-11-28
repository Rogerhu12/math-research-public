#!/usr/bin/env python3
"""Compare complete sparse-jet angular algebra on actual nonzero G10 packets."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np

def module(p,n):
    spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec)
    sys.modules[n]=m;spec.loader.exec_module(m);return m

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def reference(spectrum,channels,N,normal):
    nr=spectrum.shape[0];nc=len(channels)
    frequency,coefficient=normal.channel_terms(channels)
    components=np.array([c for c,k,kind in channels],int)
    A=np.zeros((nc,3,6));A[:,0,0]=1.;A[:,0,5]=[-k*k for c,k,kind in channels]
    A[:,1,1]=1.;A[:,2,3]=1.;C=np.zeros((3,6));C[0,2]=C[1,4]=1.
    Q=np.empty((nr,nc,nc,3,3))
    for ca in range(3):
        ia=np.flatnonzero(components==ca)
        for cb in range(3):
            ib=np.flatnonzero(components==cb)
            moments=[np.zeros((nr,len(ia),len(ib),6,6),complex) for k in range(4)]
            for sa in range(2):
                fa=frequency[sa,ia][:,None];za=coefficient[sa,ia][:,None]
                for sb in range(2):
                    fb=frequency[sb,ib][None,:];zb=coefficient[sb,ib][None,:]
                    weight=za*zb
                    if not np.any(weight):continue
                    F=normal.positive_exponential_moment(spectrum[:,:,ca,cb],fa+fb,N)
                    factors=(weight,weight*(1j*fb),weight*(1j*fa),-weight*fa*fb)
                    for moment,factor in zip(moments,factors):moment+=F*factor[None,...,None,None]
            aa,ab=A[ia],A[ib]
            q=(np.einsum('mdi,smnij,nej->smnde',aa,moments[0].real,ab,optimize=True)+
                np.einsum('mdi,smnij,ej->smnde',aa,moments[1].real,C,optimize=True)+
                np.einsum('di,smnij,nej->smnde',C,moments[2].real,ab,optimize=True)+
                np.einsum('di,smnij,ej->smnde',C,moments[3].real,C,optimize=True))
            Q[:,ia[:,None],ib[None,:],:,:]=q
    return Q

def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','prepare-entry','prepared','state','output'):ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    if args.output.exists():raise FileExistsError(args.output)
    prepare=module(args.prepare_entry,'sparse_jet_prepare')
    prepared,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    op=module(Path(__file__).with_name('2ecf-polar-log-radius-operator.py'),'sparse_jet_operator')
    deps=op.dependencies(args.scripts);stream=mods['stream']
    module(Path(__file__).with_name('2ecf-polar-complete-two-grid-streamed.py'),'sparse_jet_memory').install(deps['joint'])
    fastpath=Path(__file__).with_name('2ecf-polar-complete-sparse-jet-angular.py');fast=module(fastpath,'sparse_jet_fast')
    recipe=copy.deepcopy(definition['recipe']);recipe['cachePointBlocks']=False
    config=stream.point.PointConfig(**definition['pointConfig']);area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    weights={k:{n:.5*np.asarray(v,float) for n,v in prepared['caches'][k]['weights'].items()} for k in caches}
    saved=json.loads(args.state.read_text());z=np.array(saved['z']).reshape(basis.nb,basis.na)
    linear=deps['area'].CompleteAreaTwoGrid(deps['joint'],stream,basis,caches,weights,z,config,recipe,area)
    rows=[]
    for name in linear.names:
        original=linear.parent.groups[name]
        for index in (1,10,60):
            sl=original.slices[index];part=original._get_block(index,sl)
            gram=np.zeros(part.residual.shape[:2]+(3,3,6,6));cot=np.zeros_like(part.residual)
            for row in range(13):
                cot[...,row]=1.;derivative=part.vjp(cot)
                gram+=np.einsum('suic,sujd->sucdij',derivative,derivative,optimize=True);cot[...,row]=0.
            packet=linear.groups[name].packets[index]
            derivative=np.zeros(part.residual.shape[:2]+(6,3));derivative[:,:,1]=packet.gs;derivative[:,:,2]=packet.gu
            gram+=np.einsum('suic,sujd->sucdij',derivative,derivative,optimize=True)
            spectrum=np.fft.rfft(gram,axis=1)
            tick=time.monotonic();old=reference(spectrum,basis.channels,original.N,deps['normal']);oldt=time.monotonic()-tick
            tick=time.monotonic();new,meta=fast.contract(spectrum,basis.channels,original.N);newt=time.monotonic()-tick
            error=float(np.linalg.norm(new-old)/max(1.,np.linalg.norm(old)))
            row=dict(grid=name,radialBlock=index,actualRadials=len(original.nodes[sl]),actualAngles=original.N,
                allCartesianAngularColumns=basis.na,originalSeconds=oldt,newSeconds=newt,
                fullQRelativeFrobenius=error,maximumAbsoluteDifference=float(np.max(abs(new-old))),**meta)
            print(json.dumps(dict(event='actual_sparse_jet_angular_comparison',**row)),flush=True)
            if error>3e-13:raise ArithmeticError('Full actual angular contraction differs')
            rows.append(row)
    out=dict(schema='2ecf-actual-complete-sparse-jet-angular-audit-v1',entrySHA256=sha(__file__),kernelSHA256=sha(fastpath),
        preparedSHA256=sha(args.prepared),stateSHA256=sha(args.state),rows=rows,
        originalAngularSeconds=sum(r['originalSeconds'] for r in rows),newAngularSeconds=sum(r['newSeconds'] for r in rows),
        fullProductionNormalNotYetRun=True,optimizationAttempts=0,optimizationAccepts=0,seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_sparse_jet_angular_audit_complete',seconds=out['seconds'],
        originalSeconds=out['originalAngularSeconds'],newSeconds=out['newAngularSeconds'])),flush=True)

if __name__=='__main__':main()
