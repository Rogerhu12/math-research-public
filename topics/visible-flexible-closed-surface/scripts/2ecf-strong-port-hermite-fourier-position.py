#!/usr/bin/env python3
"""Define a new accurate-port physical Hermite/Fourier suffix from one frozen strong G10 position."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import sys
import time
import types
from pathlib import Path
for n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[n]="1"
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def sha(file):
    d=hashlib.sha256()
    with Path(file).open('rb') as fp:
        for chunk in iter(lambda:fp.read(2**20),b''):d.update(chunk)
    return d.hexdigest()


def weights(t,h,j):
    # Radial derivatives are in physical units. Core data are P,V,A on both ends.
    poly=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
                   [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])
    p=np.arange(j,6)
    powers=np.power(t,p-j)*np.array([math.factorial(i)//math.factorial(i-j) for i in p])
    return (poly[:,p]@powers)*np.array([1,h,h*h,1,h,h*h])/h**j


def metrics(jets,rad):
    X,V,U,SS,SU,UU=jets.swapaxes(0,1)
    dot=lambda a,b:np.sum(a*b,axis=-1)
    a=rad[:,None];E=dot(V,V);F=dot(V,U);G=dot(U,U)
    e=E-1;g=G/(a*a)-1
    er=abs(e+g)/2+np.hypot((e-g)/2,F/a)
    N=np.cross(V,U);A=np.linalg.norm(N,axis=-1);N=N/A[:,:,None];det=A*A
    l=dot(N,SS);m=dot(N,SU);n=dot(N,UU)
    tr=(G*l-2*F*m+E*n)/det
    k=abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-(l*n-m*m)/det))
    return er,k,A/a


def numerical_endpoint_pair(scripts,ramp,coast,u):
    raw=module(scripts/'6a65-geometry-nonfold-polar-connector.py','hf_polar')
    source=raw.NonfoldPolarConnector(scripts,ramp,coast)
    pairs=[func(u) for func in source.providers]
    ans=[]
    for port in pairs:
        # j radial, k angular, Cartesian vector.
        ans.append(np.stack([np.stack([port[root+"u"*k] for k in range(3)]) for root in ('P','V','A')]))
    return ans


def phases(u,M):
    m=np.arange(M+1)
    return np.stack([(1j*m[None,:])**k*np.exp(1j*u[:,None]*m[None,:]) for k in range(3)])


def evaluate(nodes,u,base,knots,coeff,endpoint):
    phase=phases(u,coeff.shape[2]-1)
    curve=np.einsum('kum,nrmc->nrkuc',phase,coeff,optimize=True).real
    curve[0]=endpoint[0];curve[-1]=endpoint[1]
    result=base.copy()
    for i,s in enumerate(nodes):
        if not knots[0]<=s<=knots[-1]:continue
        j=min(len(knots)-2,max(0,np.searchsorted(knots,s,side='right')-1))
        h=knots[j+1]-knots[j];t=(s-knots[j])/h
        ports=np.concatenate((curve[j],curve[j+1]))
        mat=np.stack([weights(t,h,k) for k in range(3)])
        z=np.einsum('lp,pkuc->lkuc',mat,ports,optimize=True)
        result[i]=np.stack((z[0,0],z[1,0],z[0,1],z[2,0],z[1,1],z[0,2]))
    return result


def design(args):
    st=time.monotonic();sp=args.scripts
    prepare=module(sp/'2ecf-polar-raw-ramp-source-compose.py','hf_prepare')
    saved,definition,fullbasis,caches,mods,*_=prepare.validate_prepared(args)
    coarse=module(sp/'2ecf-polar-fixed-prefix-position-basis.py','hf_coarse').restrict(fullbasis)[0]
    fine=module(sp/'2ecf-polar-local-suffix-boehm.py','hf_fine').build(coarse)[0]
    direct=module(sp/'2ecf-polar-c2-independent-g11-resume-observe.py','hf_g11')
    g=module(sp/'2ecf-polar-log-radius-operator.py','hf_original_target')
    state=json.loads(args.state.read_bytes());frozen=json.loads(args.frozen.read_bytes())
    model=state['modelDefinition'];fmodel=frozen['provisionalMetricDefinition']
    if (sha(args.frozen)!=model['frozenMetricDesignStateSHA256'] or
            frozen['provisionalMetricDefinitionSHA256']!=model['frozenTargetDefinitionSHA256'] or
            model['basis']!=fine.definition or fmodel['physicalSplineBasis']!=coarse.definition):
        raise ValueError("Actual frozen target and saved parent position required")
    alpha=np.asarray(frozen['logRadiusCoefficients'])
    if fmodel['exactCoefficientHex']!=[float(a).hex() for a in alpha]:
        raise ValueError("Frozen alpha identity failed")
    z=np.asarray(state['z']).reshape(fine.nb,fine.na)
    observer=caches['observer'];grid=observer.nodes;N=len(observer.u);M=args.modes
    if not 2<=M<N//2:raise ValueError("Retain genuine full-angle true harmonic pairs")
    targets=np.linspace(coarse.c,coarse.end,args.cells+1)
    ids=np.array([np.argmin(abs(grid-v)) for v in targets])
    knots=grid[ids]
    if knots[0]!=coarse.c or knots[-1]!=coarse.end or np.any(np.diff(knots)<=0):
        raise ValueError("Nearest true G10 rows did not produce distinct prescribed boundary knots")
    parent=observer.jets[ids]+fine.packet(fine.matrices(knots),z,N)
    raw=parent[:,(0,1,3)]
    coeff=(2./N)*np.fft.rfft(raw,axis=2)[:,:,:M+1]
    coeff[:,:,0]*=.5
    # The two boundary entries are placeholders. Accurate P,V,A at both ports
    # supersede these coefficients in the mathematical and numerical consumers.
    coeff[0]=0;coeff[-1]=0
    fieldfile=Path(str(args.output)+'.field.npz')
    np.savez(fieldfile,knots=knots,coefficients=coeff)
    ind=json.loads(args.independent.read_bytes())
    baseind=np.load(ind['files']['jets'],mmap_mode='r')
    arind=np.load(ind['files']['radius'],mmap_mode='r')
    entries={k:(v.nodes,v.u,v.jets,v.radius) for k,v in caches.items()}
    entries['independent']=(np.asarray(ind['physicalNodes']),np.asarray(ind['angles']),baseind,arind)
    out={}
    for label,(ns,u,base,target) in entries.items():
        endpoint=numerical_endpoint_pair(sp,args.ramp,args.coast,u)
        field=evaluate(ns,u,base,knots,coeff,endpoint)
        a=g.LogRadiusCache(coarse,types.SimpleNamespace(nodes=ns,u=u,jets=None,radius=target),alpha).radius[:,0]
        err,k,area=metrics(field,a)
        actual=base+direct.direct_packet(fine,ns,z,u)
        aerr,ak,aa=metrics(actual,a)
        diff=np.max(np.linalg.norm(field-actual,axis=-1),axis=(0,2))
        q={}
        for name,val,sign in [('newMetric',err,1),('newCurvature',k,1),('newAreaRatio',area,-1),
               ('oldMetric',aerr,1),('oldCurvature',ak,1),('oldAreaRatio',aa,-1)]:
            ij=np.unravel_index(np.argmax(val*sign),val.shape)
            q[name]=[float(val[ij]),float(ns[ij[0]]),float(u[ij[1]])]
        q.update(nodes=len(ns),angles=len(u),newOldAbsoluteJetSup=diff.tolist())
        out[label]=q
        print(label,q,flush=True)
    obj=dict(schema="accurate-Gamma95-R205-complete-Hermite-Fourier-frozen-strong-position-v1",
        sourceSHA256=sha(__file__),stateSHA256=sha(args.state),frozenStateSHA256=sha(args.frozen),
        preparedSHA256=sha(args.prepared),independentSHA256=sha(args.independent),
        targetDefinitionSHA256=frozen['provisionalMetricDefinitionSHA256'],fieldSHA256=sha(fieldfile),
        rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),trueBoundarySource="R265 accurate Gamma95/R205 P,V,A, all angular derivatives",
        endpointEvaluation="old literal high port packet only in finite observations, true functions in definition",
        radialHermiteElements=len(knots)-1,nonnegativeFourierModes=M+1,
        knotSelection="G10 192-angle complete corrected source nearest to a uniform physical grid",
        parentSixJetsOnlyUsedToDefineNewDyadicPositionCoefficients=True,fullNumericalObservations=out,
        seconds=time.monotonic()-st)
    with args.output.open('x') as f:json.dump(obj,f,indent=2);f.write('\n')


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for key in ('scripts','prepared','state','frozen','independent','ramp','coast','output'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--cells',type=int,default=64);ap.add_argument('--modes',type=int,default=72)
    design(ap.parse_args())
