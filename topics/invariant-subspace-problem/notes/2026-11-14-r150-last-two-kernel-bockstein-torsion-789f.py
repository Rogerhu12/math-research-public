#!/usr/bin/env python3
"""Complete polynomial Bockstein image after only the missing cost86 pair.

The972 low kernels and660 deleted N-N kernels have exact O[s] lifts.
All200 other high kernels are reused, never reconstructed or recomputed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,time
from pathlib import Path
import flint
from flint import nmod_mat,nmod_poly

STATE='06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
BASE='9d5e8398f8bd586a1c91eaa5ab93868c9ec1d813c40c7131152d866c287d2b95'
SYSTEM='b46b9f338f961c33d528651c515fec1335943417574f8b83dd942407b87e7ef2'
READER='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read_actual(path,expected):
    data=path.read_bytes()
    if path.suffix=='.gz':data=gzip.decompress(data)
    if hashlib.sha256(data).hexdigest()!=expected:raise ValueError('actual input checksum: '+str(path))
    return data
def zero(M):return not any(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def pivots(M,r):return [next(j for j in range(M.ncols()) if int(M[i,j])) for i in range(r)]
def parse_nf(data,labels,index):
    if data[:8]!=b'R150NF31' or struct.unpack_from('<3I',data,8)!=(0,len(labels),1034):raise ValueError('complete NF header')
    offset=20;out=[[0]*len(labels) for _ in range(820)]
    for j,label in enumerate(labels):
        raw,number,count=struct.unpack_from('<IHI',data,offset);offset+=10
        if raw or number!=label:raise ValueError('actual NF source label')
        previous=0
        for _ in range(count):
            c,length=struct.unpack_from('<HB',data,offset);offset+=3
            if c<=previous or c>1034 or not 1<=length<=8:raise ValueError('NF outside standard state')
            previous=c
            for d in range(length):
                v=data[offset];offset+=1
                if v>30 or (v and (c,d) not in index):raise ValueError('NF nonstandard coordinate')
                if v:out[index[c,d]][j]=v
    if offset!=len(data):raise ValueError('NF trailing input')
    return out

def main():
    p=argparse.ArgumentParser()
    for key in ('notes-root','known-results','original-metadata','image-metadata','image-quotients','image-remainders','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
    hp=a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py'
    if digest(hp)!=READER:raise ValueError('frozen state reader')
    spec=importlib.util.spec_from_file_location('frozen_complete_state',hp)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    data=read_actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE)
    state_file=a.out/'state-input.bin';state_file.write_bytes(data);state=helper.load_state(state_file)
    sr=json.loads((a.notes_root/'2026-11-14-r150-native-torsion-state-receipt-789f.json').read_text())
    if sr.get('status')!='completed' or sr['outputs']['state.bin']['sha256']!=STATE:raise ValueError('complete original state receipt')
    original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
    if original.get('status')!='completed' or original.get('highKernelColumns')!=2 or original.get('fixedSourceBudget')!=86 or not original.get('fullOriginalBocksteinDivisionIdentity') or not original.get('allIndividualWeightedBoundsVerified'):raise ValueError('complete original missing pair identities')
    labels2=original['labels']
    if len(labels2)!=2 or any(L[2]!=86 for L in labels2):raise ValueError('only missing cost86 pair allowed')
    if image.get('status')!='completed' or not image.get('fullImageQuotientIdentity') or not image.get('everyRemainderIsIrreducible') or image.get('fixedOriginalSourceBudget')!=86:raise ValueError('full missing-pair image certificate')
    # Verify the actual complete G dictionary before using the saved state.
    qdata=a.image_quotients.read_bytes()
    if qdata[:8]!=b'R150IQ31' or struct.unpack_from('<4I',qdata,8)!=(1034,1021,2,86):raise ValueError('actual missing-pair image quotients')
    offset=24;heads={}
    for _ in range(1021):
        c,d,lc=struct.unpack_from('<HBB',qdata,offset);offset+=4
        if c in heads or not 1<=c<=1034 or d>8 or not 1<=lc<=30:raise ValueError('complete G head')
        heads[c]=d
        for _ in range(2):
            n=struct.unpack_from('<H',qdata,offset)[0];offset+=2+n
    coordinates=[[c,d] for d in range(8) for c in range(1,1035) if c not in heads or d<heads[c]]
    if offset!=len(qdata) or sum(heads.values())!=716 or coordinates!=state['coordinates'] or [c for c in range(1,1035) if c not in heads]!=state['freeComponents']:raise ValueError('same full original module standard coordinates')
    index={tuple(cd):i for i,cd in enumerate(coordinates)}
    new820=parse_nf(a.image_remainders.read_bytes(),[L[1] for L in labels2],index)
    observation=nmod_mat(state['observabilityEchelon'],31)
    K=nmod_mat(state['matrices']['kernelTranspose'],31).transpose()
    J=nmod_mat(state['matrices']['action'],31)
    free=[i for i in range(820) if i+1 not in set(state['pivotStateCoordinates'])]
    NB=nmod_mat([[new820[i][j] for j in range(2)] for i in free],31)
    if not zero(observation*nmod_mat(new820,31)) or K*NB!=nmod_mat(new820,31):raise ValueError('missing kernel has a nonzero free component; no torsion projection may replace it')
    base=read_actual(a.known_results/'all200-torsion-columns.bin.gz',BASE)
    if base[:8]!=b'R150BV31' or struct.unpack_from('<3I',base,8)!=(31,315,200):raise ValueError('all200 old base format')
    offset=20;oldlabels=[]
    for _ in range(200):oldlabels.append(list(struct.unpack_from('<IHHII',base,offset)));offset+=16
    if len(base)!=offset+315*200:raise ValueError('all200 base full length')
    old=[[base[offset+i*200+j] for j in range(200)] for i in range(315)]
    if [j for j in range(200) if any(old[i][j] for i in range(315))]!=[198,199]:raise ValueError('known200 base profile')
    if len({L[1] for L in oldlabels+labels2})!=202:raise ValueError('202 distinct genuine high kernel sources')
    system=read_actual(a.known_results/'complete-infinite-quotient-system.bin.gz',SYSTEM)
    if system[:8]!=b'R150BI31' or struct.unpack_from('<7I',system,8)!=(31,315,200,1152,9,2,6):raise ValueError('actual original residual system')
    offset=36
    for L in oldlabels:
        if list(struct.unpack_from('<IHHII',system,offset))!=L:raise ValueError('old source identity')
        offset+=16
    offset+=1152*8+315*1152
    R=nmod_mat([[system[offset+i*9+j] for j in range(9)] for i in range(315)],31)
    labels=oldlabels[198:]+labels2
    B=nmod_mat([[old[i][198],old[i][199],int(NB[i,0]),int(NB[i,1])] for i in range(315)],31)
    powers=[];v=B
    for k in range(316):
        powers.append(rows(v))
        if k<315:v=J*v
    minima=[]
    for j,L in enumerate(labels):
        M=nmod_mat([[powers[k][i][j] for k in range(316)] for i in range(315)],31)
        red,rank=M.rref()
        if pivots(red,rank)!=list(range(rank)):raise ValueError('initial full-vector Krylov independence')
        co=[(-int(red[i,rank]))%31 for i in range(rank)]+[1]
        if not zero(M*nmod_mat([[c] for c in co+[0]*(316-len(co))],31)):raise ValueError('full315 annihilator identity')
        minima.append({'baseColumn':199+j,'originalLabel':L,'minimumDegree':rank,'coefficientsAscending':co,
                       **helper.factored(nmod_poly(co,31)),'full315RelationZero':True,'initialKrylovIndependent':True})
    # A cost-ordered column basis records the exact kernel-source filtration
    # of the Bockstein image, without pretending to pay the later correction.
    descriptors=sorted([[199+j,L[1],k,L[2]+k] for j,L in enumerate(labels) for k in range(316)],key=lambda x:(x[3],x[1],x[2]))
    columns=[[powers[D[2]][i][D[0]-199] for i in range(315)] for D in descriptors]
    C=nmod_mat([[c[i] for c in columns] for i in range(315)],31)
    reduced,dim=C.rref();selected=pivots(reduced,dim)
    W=nmod_mat([[columns[j][i] for j in selected] for i in range(315)],31)
    E,rank=W.transpose().rref();eps=pivots(E,rank);Erows=rows(E)
    if rank!=dim:raise ValueError('complete image basis')
    others=[i for i in range(315) if i not in set(eps)]
    def project(M):
        z=rows(M)
        for j in range(M.ncols()):
            for k,pivot in enumerate(eps):
                c=z[pivot][j]
                if c:
                    for i in others:z[i][j]=(z[i][j]-c*Erows[k][i])%31
            for pivot in eps:z[pivot][j]=0
        return nmod_mat(z,31)
    JW=J*W
    if not zero(project(C)) or not zero(project(JW)):raise ValueError('all1264 polynomial image columns and J invariance')
    PR=project(R);compatible=[all(not int(PR[i,j]) for i in range(315)) for j in range(9)]
    Wrows=rows(W);Rrows=rows(R)
    augmented=nmod_mat([Wrows[i]+Rrows[i] for i in range(315)],31).rank()
    square=nmod_mat([[int(W[p,j]) for j in range(dim)] for p in eps],31)
    coeff=square.inv()*nmod_mat([[int(R[p,j]) for j in range(9)] for p in eps],31)
    product=W*coeff
    costs=[]
    for j in range(9):
        if compatible[j]:
            if any(int(product[i,j])!=int(R[i,j]) for i in range(315)):raise ValueError('full315 target image solution')
            costs.append(max((descriptors[selected[k]][3] for k in range(dim) if int(coeff[k,j])),default=-1))
        else:
            costs.append(None)
            for k in range(dim):coeff[k,j]=0
    duals=[]
    for j,good in enumerate(compatible):
        if good:continue
        f=next(i for i in others if int(PR[i,j]));anchor=pow(int(PR[f,j]),-1,31)
        w={f:anchor}
        for k,pivot in enumerate(eps):
            c=(-anchor*Erows[k][f])%31
            if c:w[pivot]=c
        if any(sum(c*int(W[i,z]) for i,c in w.items())%31 for z in range(dim)) or sum(c*int(R[i,j]) for i,c in w.items())%31!=1:raise ValueError('complete polynomial kernel-image dual')
        duals.append({'target':j+2,'coordinates':[{'torsionCoordinate':i+1,'stateCoordinate':free[i]+1,
                 'normalFormComponent':coordinates[free[i]][0],'parameterExponent':coordinates[free[i]][1],'weight':c}
                  for i,c in sorted(w.items())],'annihilatesWholePolynomialBocksteinImage':True,'rightHandSide':1})
    action=square.inv()*nmod_mat([[int(JW[p,j]) for j in range(dim)] for p in eps],31)
    if W*action!=JW:raise ValueError('complete beta restricted action')
    packed=bytearray(b'R150FB31')+struct.pack('<7I',31,315,4,dim,9,202,augmented)
    for L in labels:packed.extend(struct.pack('<IHHII',*L))
    for j in selected:packed.extend(struct.pack('<4H',*descriptors[j]))
    for M in (B,W,R,coeff,action):packed.extend(bytes(v for row in rows(M) for v in row))
    packed.extend(bytes(compatible))
    file=a.out/'complete-polynomial-bockstein-image.bin.gz';file.write_bytes(gzip.compress(packed,mtime=0))
    result={'format':'r150-complete-original-polynomial-bockstein-image-v1','status':'completed','field':31,
      'finite_budget_verified':False,'allOriginalPolynomialKernelRowsAccountedFor':1834,
      'exactlyLiftedNNKernelRows':660,'exactlyLiftedLowKernelRows':972,'computedHighKernelRows':202,
      'newKernelColumns':2,'old200ColumnsRecomputed':False,'allNewBocksteinsInTorsion':True,
      'full505ObservationsZero':True,'full820CoordinatesVerified':True,'sameCompleteStandardDictionary':True,
      'sourceSHA256':digest(__file__),'stateSHA256':STATE,'oldBaseSHA256':BASE,'oldSystemSHA256':SYSTEM,
      'originalMetadataSHA256':digest(a.original_metadata),'imageMetadataSHA256':digest(a.image_metadata),
      'newImageRemaindersSHA256':digest(a.image_remainders),'minimumPolynomials':minima,
      'wholePolynomialBocksteinImageDimension':dim,'augmentedNineTargetRank':augmented,
      'basisDescriptors':[descriptors[j] for j in selected],'full1264KrylovColumnsVerified':True,
      'full315JInvarianceVerified':True,'targetCompatibility':compatible,
      'allNineTargetsPassCompletePolynomialNecessaryTest':all(compatible),
      'minimumKernelSourceCostsForInfiniteClasses':costs,
      'minimumCostScope':'Cost-ordered greedy independent image columns give the true minimum cost of a polynomial original kernel whose Bockstein has the specified infinite quotient class. Later original source corrections and finite cokernel conditions are not included.',
      'kernelImageBasisCoefficients':rows(coeff),'full315SolutionIdentitiesVerified':True,'dualCertificates':duals,
      'system':{'file':str(file),'bytes':len(packed),'sha256':hashlib.sha256(packed).hexdigest(),
                'gzipBytes':file.stat().st_size,'gzipSHA256':digest(file)},
      'pythonFlintVersion':flint.__version__,'flintVersion':flint.__FLINT_VERSION__,
      'elapsedSeconds':time.monotonic()-start,
      'coverageJustification':'The exact cost-preserving N-N compression gives660 original O[s] syzygies. The actual972 low reduced kernels have exact O[s] lifts. Together with the reused200 high kernels and the two newly restored cost86 kernels, all1834 original polynomial kernel basis directions are covered. Full315-dimensional J closure includes every polynomial multiple. No finite-budget sufficiency or characteristic-zero membership is asserted.'}
    (a.out/'complete-polynomial-bockstein-image-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'last-two-complete-polynomial-bockstein-test-complete',
       'allNewBocksteinsInTorsion':True,'allOriginalPolynomialKernelRowsAccountedFor':1834,
       'wholePolynomialBocksteinImageDimension':dim,'augmentedNineTargetRank':augmented,
       'targetCompatibility':compatible,'minimumKernelSourceCostsForInfiniteClasses':costs,
       'finite_budget_verified':False,'elapsedSeconds':result['elapsedSeconds']}),flush=True)

if __name__=='__main__':main()
