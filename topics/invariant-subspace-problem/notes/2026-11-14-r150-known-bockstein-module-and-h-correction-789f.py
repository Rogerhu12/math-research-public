#!/usr/bin/env python3
"""Full315-vector closure of the two known nonzero Bocksteins.

No original DAG is replayed. Intended unique bound:60s,512MiB.
The two uncomputed kernel rows of cost86 are explicitly outside this result.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import time
import flint
from flint import nmod_mat, nmod_poly

STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
BASE_SHA="9d5e8398f8bd586a1c91eaa5ab93868c9ec1d813c40c7131152d866c287d2b95"
SYSTEM_SHA="b46b9f338f961c33d528651c515fec1335943417574f8b83dd942407b87e7ef2"
READER_SHA="8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
H31=[0,0,0,7,25,15,20,20,15,22,9,26,15,29,26,28,8,4,21,15,11,29,5,21,1]

def sha(data):return hashlib.sha256(data).hexdigest()
def actual(path,expected):
    x=path.read_bytes()
    if path.suffix=='.gz':x=gzip.decompress(x)
    if sha(x)!=expected:raise ValueError('actual input checksum: '+str(path))
    return x
def pivots(red,rank):
    return [next(j for j in range(red.ncols()) if int(red[i,j])) for i in range(rank)]
def to_rows(m):return [[int(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]
def zero(m):return all(not int(m[i,j]) for i in range(m.nrows()) for j in range(m.ncols()))

def solve_one(rows,b):
    """Exact solution or explicit dual for a complete one-RHS system."""
    nr=len(rows);nc=len(rows[0]);M=nmod_mat(rows,31)
    A=nmod_mat([r+[b[i]] for i,r in enumerate(rows)],31)
    rank=M.rank();arank=A.rank()
    result={'coefficientRank':rank,'augmentedRank':arank,'compatible':rank==arank}
    if arank==rank:
        red,rr=A.rref();ps=pivots(red,rr);x=[0]*nc
        for i,p in enumerate(ps):
            if p>=nc:raise ValueError('spurious augmented pivot')
            x[p]=int(red[i,nc])
        product=M*nmod_mat([[a] for a in x],31)
        if any(int(product[i,0])!=b[i] for i in range(nr)):raise ValueError('full solution')
        result.update(solution=x,fullVectorIdentity=True)
        return result
    red,rr=A.transpose().rref();selected=pivots(red,rr)
    if rr!=rank+1:raise ValueError('one RHS augmented rank')
    small=nmod_mat([rows[i] for i in selected],31).transpose()
    sr,srank=small.rref();ps=pivots(sr,srank)
    if srank!=rank:raise ValueError('selected coefficient rank')
    f=next(j for j in range(rr) if j not in ps);w=[0]*rr;w[f]=1
    for i,p in enumerate(ps):w[p]=(-int(sr[i,f]))%31
    anchor=sum(w[i]*b[r] for i,r in enumerate(selected))%31
    if not anchor:raise ValueError('dual anchor')
    w=[a*pow(anchor,-1,31)%31 for a in w]
    if any(sum(w[i]*rows[r][j] for i,r in enumerate(selected))%31 for j in range(nc)):raise ValueError('dual matrix')
    if sum(w[i]*b[r] for i,r in enumerate(selected))%31!=1:raise ValueError('dual RHS')
    result.update(dualSelectedRowsOneBased=[r+1 for r in selected],dualWeights=w,
                  fullCoefficientDualZero=True,dualRightHandSide=1)
    return result

def main():
    p=argparse.ArgumentParser()
    for k in ('notes','results','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
    hp=a.notes/'2026-11-14-r150-torsion-characteristic-789f.py'
    if sha(hp.read_bytes())!=READER_SHA:raise ValueError('state reader')
    spec=importlib.util.spec_from_file_location('frozen_r150_state',hp)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    raw=actual(a.notes/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE_SHA)
    state_path=a.out/'state-input.bin';state_path.write_bytes(raw);state=helper.load_state(state_path)
    if (state['stateDimension'],state['torsionDimension'])!=(820,315):raise ValueError('state dimensions')
    J=nmod_mat(state['matrices']['action'],31)
    free=[i for i in range(820) if i+1 not in set(state['pivotStateCoordinates'])]
    coordinates=state['coordinates']
    base=actual(a.results/'all200-torsion-columns.bin.gz',BASE_SHA)
    if base[:8]!=b'R150BV31' or struct.unpack_from('<3I',base,8)!=(31,315,200):raise ValueError('base format')
    off=20;labels=[]
    for _ in range(200):labels.append(list(struct.unpack_from('<IHHII',base,off)));off+=16
    if len(base)!=off+315*200:raise ValueError('complete base length')
    B=[[base[off+i*200+j] for j in range(200)] for i in range(315)]
    active=[j for j in range(200) if any(B[i][j] for i in range(315))]
    if active!=[198,199]:raise ValueError('actual nonzero Bockstein columns changed')
    system=actual(a.results/'complete-infinite-quotient-system.bin.gz',SYSTEM_SHA)
    if system[:8]!=b'R150BI31' or struct.unpack_from('<7I',system,8)!=(31,315,200,1152,9,2,6):raise ValueError('system format')
    off=36
    sylabels=[]
    for _ in range(200):sylabels.append(list(struct.unpack_from('<IHHII',system,off)));off+=16
    if labels!=sylabels:raise ValueError('original source mapping')
    off+=1152*8+315*1152
    R=nmod_mat([[system[off+i*9+j] for j in range(9)] for i in range(315)],31)
    active_matrix=nmod_mat([[B[i][j] for j in active] for i in range(315)],31)
    powers=[];v=active_matrix
    for k in range(316):
        powers.append(to_rows(v))
        if k<315:v=J*v
    mins=[]
    for b,j in enumerate(active):
        cols=[[powers[k][i][b] for i in range(315)] for k in range(316)]
        K=nmod_mat([[cols[k][i] for k in range(316)] for i in range(315)],31)
        red,rank=K.rref()
        if pivots(red,rank)!=list(range(rank)):raise ValueError('initial Krylov independence')
        co=[(-int(red[i,rank]))%31 for i in range(rank)]+[1]
        relation=K*nmod_mat([[x] for x in co+[0]*(316-len(co))],31)
        if not zero(relation):raise ValueError('whole315 minimal recurrence')
        mins.append({'baseColumn':j+1,'originalLabel':labels[j],'degree':rank,'coefficientsAscending':co,
                     **helper.factored(nmod_poly(co,31)),'full315RelationZero':True,
                     'initialKrylovColumnsIndependent':True})
    columns=[];descriptors=[]
    for k in range(316):
        for b,j in enumerate(active):
            columns.append([powers[k][i][b] for i in range(315)])
            descriptors.append([j+1,labels[j][1],k,labels[j][2]+k])
    full=nmod_mat([[c[i] for c in columns] for i in range(315)],31)
    red,dim=full.rref();selected=pivots(red,dim)
    W=nmod_mat([[columns[j][i] for j in selected] for i in range(315)],31)
    E,erank=W.transpose().rref();eps=pivots(E,erank)
    if erank!=dim:raise ValueError('module basis rank')
    nonpivot=[i for i in range(315) if i not in set(eps)]
    Erows=to_rows(E)
    def project(m,full=False):
        rr=to_rows(m)
        for c in range(m.ncols()):
            for i,pivot in enumerate(eps):
                v=rr[pivot][c]
                if v:
                    for r in nonpivot:rr[r][c]=(rr[r][c]-v*Erows[i][r])%31
            for pivot in eps:rr[pivot][c]=0
        return nmod_mat(rr if full else [rr[r] for r in nonpivot],31)
    if not zero(project(full)) or not zero(project(J*W)):raise ValueError('complete invariant module closure')
    PR=project(R)
    no_h=[all(not int(PR[i,j]) for i in range(len(nonpivot))) for j in range(9)]
    T=nmod_mat(state['matrices']['targetCoordinates'],31).transpose()
    Tp=[];Tcurrent=T
    for k in range(25):
        Tp.append(Tcurrent)
        if k<24:Tcurrent=J*Tcurrent
    check=nmod_mat(315,9,31)
    for k,coeff in enumerate(H31):
        if coeff:check=check+Tp[k]*coeff
    if not zero(check):raise ValueError('actual common h31 target annihilator')
    Ptargets=[project(t) for t in Tp[:24]]
    rows=[];rhs=[]
    for j in range(9):
        for i in range(len(nonpivot)):
            rows.append([(-int(Ptargets[k][i,j]))%31 for k in range(24)])
            rhs.append(int(PR[i,j]))
    common=solve_one(rows,rhs)
    common.update(unknowns=24,equations=len(rows),allPolynomialCorrectionsReduceModuloH31=True)
    individual=[]
    for j in range(9):
        qdim=len(nonpivot);rj=rows[j*qdim:(j+1)*qdim];bj=rhs[j*qdim:(j+1)*qdim]
        individual.append({'target':j+2,**solve_one(rj,bj)})
    def expand_dual(cert):
        weights={};qdim=len(nonpivot)
        for row1,w in zip(cert['dualSelectedRowsOneBased'],cert['dualWeights']):
            r=row1-1;j=r//qdim;i=nonpivot[r%qdim]
            weights[j,i]=(weights.get((j,i),0)+w)%31
            for z,pivot in enumerate(eps):
                weights[j,pivot]=(weights.get((j,pivot),0)-w*Erows[z][i])%31
        witness=[]
        for (j,i),w in sorted(weights.items()):
            if w:
                c,d=coordinates[free[i]]
                witness.append({'target':j+2,'torsionCoordinate':i+1,'stateCoordinate':free[i]+1,
                                'normalFormComponent':c,'parameterExponent':d,'weight':w})
        # Check against every independent per-target kernel-module direction
        # and all24 common scalar directions in the original315 coordinates.
        if any(sum(weights.get((j,i),0)*int(W[i,z]) for i in range(315))%31 for j in range(9) for z in range(dim)):
            raise ValueError('expanded kernel-module dual')
        if any(sum(weights.get((j,i),0)*int(Tp[k][i,j]) for j in range(9) for i in range(315))%31 for k in range(24)):
            raise ValueError('expanded all-polynomial h dual')
        if sum(weights.get((j,i),0)*int(R[i,j]) for j in range(9) for i in range(315))%31!=1:
            raise ValueError('expanded original residual anchor')
        return witness
    if not common['compatible']:
        common['expandedOriginalNormalFormDual']=expand_dual(common)
        common['fullOriginalKernelAndScalarDualVerified']=True
    else:
        g=common['solution'];V=R
        for k,c in enumerate(g):
            if c:V=V+Tp[k]*c
        if not zero(project(V)):raise ValueError('common g final module membership')
        square=nmod_mat([[int(W[p,j]) for j in range(dim)] for p in eps],31)
        coeff=square.inv()*nmod_mat([[int(V[p,j]) for j in range(9)] for p in eps],31)
        if W*coeff!=V:raise ValueError('all target module source identity')
        common['kernelModuleBasisCoefficients']=to_rows(coeff)
        common['full315OriginalIdentity']=True
    # Retain complete source labels, module columns, quotient projection and
    # the entire common correction system. All sizes are finite and small.
    packed=bytearray(b'R150BM31')+struct.pack('<6I',31,315,200,dim,len(nonpivot),9)
    for L in labels:packed.extend(struct.pack('<IHHII',*L))
    for j in selected:packed.extend(struct.pack('<4H',*descriptors[j]))
    packed.extend(bytes(v for row in to_rows(W) for v in row))
    packed.extend(struct.pack(f'<{dim}H',*eps))
    packed.extend(bytes(v for row in Erows for v in row))
    packed.extend(bytes(v for row in to_rows(R) for v in row))
    for row,b in zip(rows,rhs):packed.extend(bytes(row+[b]))
    pp=a.out/'complete-known-bockstein-module-system.bin.gz';pp.write_bytes(gzip.compress(packed,mtime=0))
    out={'format':'r150-known-bockstein-polynomial-module-and-common-h-v1','status':'completed','field':31,
         'sourceSHA256':sha(Path(__file__).read_bytes()),'stateSHA256':STATE_SHA,'baseColumnsSHA256':BASE_SHA,
         'originalB85SystemSHA256':SYSTEM_SHA,'stateReaderSHA256':READER_SHA,
         'all200BaseColumnsRetained':True,'nonzeroBaseColumnsOneBased':[j+1 for j in active],
         'twoUnknownCost86KernelsIncluded':False,'finite_budget_verified':False,
         'minimumPolynomials':mins,'wholePolynomialModuleDimension':dim,
         'basisDescriptors':[descriptors[j] for j in selected],
         'all632KrylovColumnsVerified':True,'full315JInvarianceVerified':True,
         'originalResidualsInKnownPolynomialImage':no_h,
         'commonHCorrection':common,'individualHCorrections':individual,
         'pythonFlintVersion':flint.__version__,'flintVersion':flint.__FLINT_VERSION__,
         'system':{'file':str(pp),'bytes':len(packed),'sha256':sha(packed),
                   'gzipBytes':pp.stat().st_size,'gzipSHA256':sha(pp.read_bytes())},
         'elapsedSeconds':time.monotonic()-start,
         'scope':'All polynomial multiples of the200 computed original kernel Bocksteins are included via their full315-dimensional J-invariant span. The two original cost86 kernel rows are not computed and are not silently set to zero. Common scalar changes h0+31g reduce modulo the actual h31 target annihilator. Any positive infinite-module result still requires an original finite-cost source identity.'}
    (a.out/'known-bockstein-module-and-h-correction.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'known-bockstein-module-and-h-complete','moduleDimension':dim,
       'minimumDegrees':[x['degree'] for x in mins],'residualMembership':no_h,
       'commonCoefficientRank':common['coefficientRank'],'commonAugmentedRank':common['augmentedRank'],
       'commonCompatible':common['compatible'],'individualCompatible':[x['compatible'] for x in individual],
       'elapsedSeconds':out['elapsedSeconds']}),flush=True)

if __name__=='__main__':main()
