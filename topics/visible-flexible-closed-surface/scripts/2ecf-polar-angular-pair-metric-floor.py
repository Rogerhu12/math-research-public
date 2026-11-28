#!/usr/bin/env python3
"""Sharp two-angle obstruction to an arbitrary angularly invariant target metric."""
import os
for env_key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[env_key] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def module(path, name):
    spec=importlib.util.spec_from_file_location(name,path)
    loaded=importlib.util.module_from_spec(spec)
    sys.modules[name]=loaded
    spec.loader.exec_module(loaded)
    return loaded


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ring(derivative_s, derivative_u):
    E=np.einsum("ij,ij->i",derivative_s,derivative_s)
    F=np.einsum("ij,ij->i",derivative_s,derivative_u)
    G=np.einsum("ij,ij->i",derivative_u,derivative_u)
    det=E*G-F*F
    if np.any(det<=0):
        raise ArithmeticError("Every sampled first form must be positive definite")
    # Columns are denominators A_j, rows numerators A_i.
    trace=(E[:,None]*G[None,:]+G[:,None]*E[None,:]-2*F[:,None]*F[None,:])/det[None,:]
    ratio=det[:,None]/det[None,:]
    delta=trace*trace-4*ratio
    if np.min(delta)<-1e-10:
        raise ArithmeticError("Unexpected complex generalized eigenvalues")
    root=(trace+np.sqrt(np.maximum(0.,delta)))/2
    i,j=np.unravel_index(np.argmax(root),root.shape)
    lam=float(root[i,j])
    pair=(lam-1)/(lam+1)
    # Direct symmetric eigenvalue at the maximizing pair (small explicit pencil).
    first=np.array([[E[i],F[i]],[F[i],G[i]]])
    second=np.array([[E[j],F[j]],[F[j],G[j]]])
    chol=np.linalg.cholesky(second)
    lower=np.linalg.solve(chol,first)
    sym=np.linalg.solve(chol,lower.T).T
    check=float(np.linalg.eigvalsh(sym)[-1])
    if abs(check-lam)>2e-7*max(1.,abs(check)):
        raise ArithmeticError("Scalar and symmetric pencil disagree")
    return dict(lowerBound=pair,generalizedRatio=lam,angleIndices=[int(i),int(j)],
                independentWitnessEigenvalue=check,firstForm=first.tolist(),secondForm=second.tolist())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('scripts','prepared','prepare-entry','observer','output'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--states',type=Path,nargs='+',required=True)
    args=parser.parse_args()
    here=Path(__file__).parent
    original_entry=here/'2ecf-polar-c2-independent-g11-resume-observe.py'
    original=module(original_entry,'angle_pair_g11')
    spatial=module(here/'2ecf-polar-fourier-refinement.py','angle_pair_refinement')
    _,definition,coarse,_=original.source_and_basis(args)
    source=json.loads(args.observer.read_text())
    if source['sourceEntrySHA256']!=digest(original_entry) or source['sourceIdentity']!=definition['sourceIdentity'] or source['basis']!=coarse.definition:
        raise ValueError("Original independent G11 source and physical basis required")
    if digest(source['files']['jets'])!=source['SHA256']['jets']:
        raise ValueError("Actual source jets changed")
    jets=np.load(source['files']['jets'],mmap_mode='r')
    nodes=np.asarray(source['physicalNodes']);angles=np.asarray(source['angles']);rows=[]
    for state_path in args.states:
        state=json.loads(state_path.read_text()); basis=coarse
        if state['modelDefinition']['basis']!=coarse.definition:
            modes=state['modelDefinition']['basis']['maxAngularFrequency']
            basis,_=spatial.refine(coarse,modes)
        if state['preparedSHA256']!=digest(args.prepared) or state['modelDefinition']['basis']!=basis.definition:
            raise ValueError("The actual state coefficients and prepared physical basis must match")
        z=np.asarray(state['z']).reshape(basis.nb,basis.na)
        winner=dict(lowerBound=-1.)
        for lo in range(0,len(nodes),12):
            packet=original.direct_packet(basis,nodes[lo:lo+12],z,angles)+jets[lo:lo+12]
            for local,jet in enumerate(packet):
                result=ring(jet[1],jet[2])
                if result['lowerBound']>winner['lowerBound']:
                    winner=dict(result,s=float(nodes[lo+local]),radialIndex=lo+local,
                                angles=[float(angles[idx]) for idx in result['angleIndices']])
        rows.append(dict(state=state_path.name,stateSHA256=digest(state_path),**winner))
        print(json.dumps(rows[-1]),flush=True)
    with args.output.open('x') as out:
        json.dump(dict(schema='complete-G11-ordered-angular-pair-metric-floors-v1',samples=len(nodes)*len(angles),
                       testedOrderedPairsPerField=len(nodes)*len(angles)**2,sourceSHA256=digest(args.observer),
                       rows=rows,finiteSamplesOnly=True,positionsUnchanged=True),out,indent=2)
        out.write('\n')


if __name__=="__main__":main()
