#!/usr/bin/env python3
"""Nine actual QQ factors, total degree 1535, of the original C/X resultant.

Rebuild C and X from the published original Gram/cofactor source prefix.
No scratch JSON, modular reconstruction, or full QQ resultant is used.
Every coefficient division, actual kernel identity, and row replacement is
multiplied back.  The 39/34 fixed binary degrees retain all degenerate fibres.
"""
import argparse
import hashlib
import json
import resource
import signal
import time
from pathlib import Path

from flint import fmpq, fmpq_poly, fmpq_mat

FIXED_CASES = json.loads(r'''[{"label":"w","phi":["0","1"],"target":815,"initialExtraction":810,"transform":"projective","finiteCenter":["1/2","1","-4","28","-248","60048/25"],"poleCenter":["0","-6","24"],"dualRows":[63,65,68,70,72,74,76,78,79,80,81,82,81,80,79,78,77,76,75,74,73,72,71,70,69,67,66,63,60,57,54,51,48,45,65,68,70,73,75,77,79,80,81,82,82,82,82,82,82,82,82,82,81,80,79,78,77,76,75,74,73,72,71,69,68,66,63,60,57,54,51,47,43],"dualColumns":[-46,-49,-51,-54,-56,-59,-61,-63,-65,-67,-69,-71,-73,-75,-76,-77,-78,-79,-80,-81,-82,-82,-82,-82,-82,-82,-82,-82,-82,-81,-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67,-66,-65,-64,-63,-62,-61,-60,-59,-58,-56,-55,-53,-52,-50,-47,-44,-41,-38,-35,-32,-29,-26,-23,-20,-17,-14,-10,-6,0],"matching":[1,2,8,9,10,11,12,13,14,15,16,28,30,41,42,32,33,34,35,36,37,38,39,51,52,53,57,58,59,65,66,67,68,71,0,3,4,5,6,7,17,18,19,20,21,22,23,24,25,26,27,31,29,43,44,45,46,47,48,40,49,50,54,55,56,60,61,62,63,64,69,70,72]},{"label":"w+1","phi":["1","1"],"target":63,"initialExtraction":63,"transform":"identity","dualRows":[7,8,9,10,11,12,13,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,9,10,11,12,13,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],"dualColumns":[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-14,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15],"matching":[7,8,9,10,11,12,13,14,15,16,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,41,43,44,45,46,47,0,1,2,3,4,5,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,65,42,67,68,69,70,71,72]},{"label":"J2a","phi":["3/2","2","1"],"target":107,"initialExtraction":72,"transform":"translation","finiteCenter":["1","2/3"],"dualRows":[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,15,14,13,12,11,10,9,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,15,14,13,12,11,10,9,8],"dualColumns":[-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0],"matching":[0,1,2,3,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,64,65,66,67,68,69,70,71,72]},{"label":"J2b","phi":["1/2","1","1"],"target":36,"initialExtraction":28,"transform":"translation","finiteCenter":["1","1"],"dualRows":[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,11,10,8,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,11,10,9,8,6],"dualColumns":[-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-11,-10,-9,-8,-7,-6,-4,-2,0],"matching":[0,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,69,70,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,63,64,65,66,71,72]},{"label":"J3","phi":["-3/4","-1/4","1","1"],"target":5,"initialExtraction":4,"transform":"translation","finiteCenter":["3/4","1/3","-1/3"],"dualRows":[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2],"dualColumns":[-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-1,0],"matching":[34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,65,66,67,71,72]},{"label":"J6","phi":["-1/28","5/56","1/14","4/7","75/28","20/7","1"],"target":12,"initialExtraction":9,"transform":"translation","finiteCenter":["10079/11502","-2357/1917","392/81","-26759/1917","-16816/639","-68180/5751"],"dualRows":[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,3],"dualColumns":[-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-4,-3,-2,-1,0],"matching":[34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,64,65,70,71,72]},{"label":"J10","phi":["3/32","-23/32","-1/4","-255/32","-281/8","-1773/32","-69/16","115/4","4","-6","1"],"target":4,"initialExtraction":2,"transform":"translation","finiteCenter":["137663593/445081770","177048107/95374665","720943364/133524531","2979082573/267049062","-4448399479/445081770","-548796265/44508177","1214235116/222540885","2531123824/667622655","-1404849616/667622655","187317104/667622655"],"dualRows":[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],"dualColumns":[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,0],"matching":[34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,65,66,67,71,72]}]''')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    output=args.output or here/'2026-11-27-unit211-L0-nine-original-resultant-factors-certificate-8542.json'
    start=time.perf_counter()
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    results=[]
    state={'sourceSha256':sha(Path(__file__).read_bytes()),'results':results,
           'computedFullQQResultant':False,'ordinaryISPClaim':False,
           'wholeL0Excluded':False,'allFactorsProved':False}

    def say(stage,**kwargs):
        print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-start,6),**kwargs),sort_keys=True),flush=True)

    def save(stage):
        state.update(stage=stage,elapsedSeconds=round(time.perf_counter()-start,6),
                     peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        output.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n')

    def timeout(signum,frame):
        save('timeout_incomplete')
        say('timeout_incomplete',completedFactors=len(results),wholeL0Excluded=False)
        raise SystemExit(124)

    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(360)
    original=here/'2026-11-27-unit211-L0-CX-lambda-exact-degree-cover-original-return-8542.py'
    original_bytes=original.read_bytes()
    original_hash='d69a91dec3849562e2b7b465878e9e763d2ca680e32303691154d059e95a1199'
    assert sha(original_bytes)==original_hash
    marker='# NEW: exact QQ determinant-degree upper bound and actual full modular lower bound.'
    source=original_bytes.decode();assert source.count(marker)==1
    prefix=source.split(marker,1)[0]
    scope={'__file__':str(original),'__name__':'__original_gram_reconstruction__'}
    # This prefix includes the original rho resultant and all 8x8 cofactor
    # identities, but excludes the already published 73x73 degree algorithm.
    exec(compile(prefix,str(original),'exec'),scope)
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(max(1,360-int(time.perf_counter()-start)))
    C,X=scope['C'],scope['X']
    assert sha(str(C).encode())=='6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c'
    assert sha(str(X).encode())=='519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68'
    assert tuple(map(int,C.degrees()))==(0,39,53)
    assert tuple(map(int,X.degrees()))==(0,34,52)
    state.update(originalReconstructionSourceSha256=original_hash,
                 originalReconstructionPrefixSha256=sha(prefix.encode()),
                 originalPolynomialHashes=[sha(str(C).encode()),sha(str(X).encode())],
                 originalLambdaDegrees=[39,34],matrixSize=73)
    zero,one=fmpq_poly([]),fmpq_poly([1])
    n=73

    def coefficients(polynomial):
        degree=int(polynomial.degrees()[1])
        groups=[{} for _ in range(degree+1)]
        for exponent,value in polynomial.to_dict().items():
            assert exponent[0]==0
            groups[int(exponent[1])][int(exponent[2])]=value
        out=[fmpq_poly([group.get(k,0) for k in range(max(group,default=-1)+1)]) for group in groups]
        ctx=scope['ctx']
        assert ctx.from_dict({(0,j,k):v for j,p in enumerate(out) for k,v in enumerate(p.coeffs()) if v})==polynomial
        return out

    originals=[coefficients(C),coefficients(X)]

    def shift(cs,root):
        out=[cs[-1]]
        for a in cs[-2::-1]:
            out=[root*out[0]+a]+[root*out[j]+out[j-1] for j in range(1,len(out))]+[out[-1]]
        return out

    def sylvester(cs):
        assert list(map(len,cs))==[40,35]
        cp,xp=[row[::-1] for row in cs]
        out=[[zero]*i+cp+[zero]*(33-i) for i in range(34)]
        out += [[zero]*i+xp+[zero]*(38-i) for i in range(39)]
        assert len(out)==n and all(len(row)==n for row in out)
        return out

    def linear_local(root,target,label):
        """Previously successful complete QQ constant-row extraction."""
        began=time.perf_counter()
        phi=fmpq_poly([-root,1])
        matrix=sylvester(originals)
        exponent=0;rounds=[];row_checks=0;division_checks=0;trace=hashlib.sha256()
        while exponent<target:
            constants=[[p(root) for p in row] for row in matrix]
            operations=[];rank=0
            for column in range(n):
                choices=[i for i in range(rank,n) if constants[i][column]]
                if not choices:continue
                def complexity(i):
                    a=constants[i][column]
                    return abs(int(a.numerator)).bit_length()+int(a.denominator).bit_length()
                pivot_row=min(choices,key=lambda i:(complexity(i),i))
                if pivot_row!=rank:
                    constants[rank],constants[pivot_row]=constants[pivot_row],constants[rank]
                    operations.append(('swap',rank,pivot_row,None))
                pivot=constants[rank][column];assert pivot
                for i in range(rank+1,n):
                    value=constants[i][column]
                    if not value:continue
                    factor=value/pivot;assert factor*pivot==value
                    before=constants[i]
                    after=[a-factor*b for a,b in zip(before,constants[rank])]
                    assert all(c+factor*b==a for a,b,c in zip(before,constants[rank],after))
                    assert not after[column]
                    constants[i]=after;operations.append(('subtract',i,rank,factor))
                rank+=1
                if rank==n:break
            assert rank<n and all(not any(row) for row in constants[rank:])
            for kind,i,j,factor in operations:
                if kind=='swap':matrix[i],matrix[j]=matrix[j],matrix[i]
                else:
                    before=matrix[i]
                    after=[a-factor*b for a,b in zip(before,matrix[j])]
                    assert all(c+factor*b==a for a,b,c in zip(before,matrix[j],after))
                    matrix[i]=after;row_checks+=n
                trace.update(json.dumps([kind,i,j,None if factor is None else str(factor)],separators=(',',':')).encode())
            assert all(p(root)==constants[i][j] for i,row in enumerate(matrix) for j,p in enumerate(row))
            for i in range(rank,n):
                divided=[]
                for p in matrix[i]:
                    q,r=divmod(p,phi);assert not r and q*phi==p
                    divided.append(q);division_checks+=1
                matrix[i]=divided
            exponent+=n-rank;assert exponent<=target
            rounds.append({'rankModuloPhi':rank,'rowsDivided':n-rank,'extractedTotal':exponent})
            say('linear_original_exact_row_extraction',factor=label,extracted=exponent,target=target,rank=rank)
        return {'factor':label,'factorCoefficientsAscending':list(map(str,phi.coeffs())),
                'target':target,'provedQQExponent':exponent,'initialExtraction':0,
                'method':'complete QQ constant-row operations and exact phi division',
                'rounds':rounds,'rowPolynomialMultiplyBackChecks':row_checks,
                'divisionMultiplyBackChecks':division_checks,'operationTraceSha256':trace.hexdigest(),
                'elapsedSeconds':round(time.perf_counter()-began,6)}

    def fixed_dual_local(case):
        began=time.perf_counter()
        label=case['label'];target=case['target'];phi=fmpq_poly([fmpq(c) for c in case['phi']])
        assert phi.leading_coefficient()==1
        finite=fmpq_poly([fmpq(c) for c in case.get('finiteCenter',[])])
        pole=fmpq_poly([fmpq(c) for c in case.get('poleCenter',[])])
        if case['transform']=='projective':
            cs=[shift(shift(co,finite)[::-1],pole)[::-1] for co in originals]
            assert all(shift(shift(co[::-1],-pole)[::-1],-finite)==old for co,old in zip(cs,originals))
        elif case['transform']=='translation':
            cs=[shift(co,finite) for co in originals]
            assert all(shift(co,-finite)==old for co,old in zip(cs,originals))
        else:
            assert case['transform']=='identity';cs=originals
        matrix=sylvester(cs)
        u,v,matching=case['dualRows'],case['dualColumns'],case['matching']
        assert len(u)==len(v)==len(matching)==n and sorted(matching)==list(range(n))
        E=sum(u)+sum(v);assert E==case['initialExtraction']<=target
        divisions=0;inverse_checks=0;trace=hashlib.sha256();rounds=[]

        def divide(p,q):
            nonlocal divisions
            a,b=divmod(p,q);assert a*q+b==p
            assert not b or b.degree()<q.degree()
            divisions+=1
            return a,b

        # Every dual inequality is checked directly as divisibility.  Each
        # matching edge has exact order u_i+v_j, proving primal equality too.
        for i in range(n):
            for j in range(n):
                p=matrix[i][j];power=u[i]+v[j]
                if power>=0:
                    q,r=divide(p,phi**power);assert not r;matrix[i][j]=q
                else:matrix[i][j]=p*(phi**(-power))
                if j==matching[i]:
                    assert p and power>=0 and divide(matrix[i][j],phi)[1]
        result={'factor':label,'factorCoefficientsAscending':list(map(str,phi.coeffs())),
                'target':target,'initialExtraction':E,'method':'fixed full dual plus actual quotient-kernel row extraction',
                'transform':case['transform'],'finiteCenter':case.get('finiteCenter',[]),
                'poleCenter':case.get('poleCenter',[]),'fullTransformInverseVerified':True,
                'transformedCoefficientHashes':[sha('|'.join(map(str,row)).encode()) for row in cs],
                'completeDualConstraintCount':n*n,'completeDualAndPrimalEqualityVerified':True,
                'rounds':rounds}
        if E==target:
            result.update(provedQQExponent=E,divisionMultiplyBackChecks=divisions,
                          elapsedSeconds=round(time.perf_counter()-began,6))
            return result
        total_precision=target+1;precision=total_precision-E;d=phi.degree()
        for i in range(n):
            for j in range(n):matrix[i][j]=divide(matrix[i][j],phi**precision)[1]

        class FE:
            def __init__(self,value=0):
                if isinstance(value,FE):self.p=value.p;return
                polynomial=value if isinstance(value,fmpq_poly) else fmpq_poly([value])
                self.p=divide(polynomial,phi)[1]
            def __bool__(self):return bool(self.p)
            def __add__(self,other):return FE(self.p+FE(other).p)
            __radd__=__add__
            def __neg__(self):return FE(-self.p)
            def __sub__(self,other):return FE(self.p-FE(other).p)
            def __mul__(self,other):return FE(self.p*FE(other).p)
            __rmul__=__mul__
            def __eq__(self,other):return self.p==FE(other).p
            def inv(self):
                nonlocal inverse_checks
                assert self
                g,a,b=self.p.xgcd(phi)
                assert a*self.p+b*phi==g and g.degree()==0
                inverse=FE(a/g[0]);assert self*inverse==1
                inverse_checks+=1
                return inverse

        while E<target:
            residue=[[divide(p,phi)[1] for p in row] for row in matrix]
            dim=n*d;data=[[fmpq(0)]*dim for _ in range(dim)]
            for i in range(n):
                for j in range(n):
                    if not residue[i][j]:continue
                    for a in range(d):
                        p=divide(residue[i][j]*fmpq_poly([0]*a+[1]),phi)[1]
                        for b,c in enumerate(p.coeffs()):data[i*d+a][j*d+b]=c
            rational_matrix=fmpq_mat(data)
            echelon,rank=rational_matrix.transpose().rref()
            pivots=[next(j for j in range(dim) if echelon[i,j]) for i in range(rank)]
            assert all(echelon[i,j]==1 for i,j in enumerate(pivots))
            free=[j for j in range(dim) if j not in pivots];assert free
            basis=[]
            for free_column in free:
                vector=[fmpq(0)]*dim;vector[free_column]=1
                for i,j in enumerate(pivots):vector[j]=-echelon[i,free_column]
                assert fmpq_mat([vector])*rational_matrix==fmpq_mat(1,dim)
                kernel=[FE(fmpq_poly(vector[i*d:(i+1)*d])) for i in range(n)]
                for pivot,old in basis:
                    factor=kernel[pivot]
                    if factor:kernel=[a-factor*b for a,b in zip(kernel,old)]
                nonzero=next((j for j,a in enumerate(kernel) if a),None)
                if nonzero is None:continue
                inverse=kernel[nonzero].inv();kernel=[inverse*a for a in kernel]
                for k,(pivot,old) in enumerate(basis):
                    factor=old[nonzero]
                    if factor:basis[k]=(pivot,[a-factor*b for a,b in zip(old,kernel)])
                basis.append((nonzero,kernel));basis.sort(key=lambda item:item[0])
            assert basis
            chosen=[i for i,_ in basis]
            for i,vector in basis:
                assert all(vector[j]==(1 if i==j else 0) for j in chosen)
                for j in range(n):
                    p=sum((value.p*residue[ii][j] for ii,value in enumerate(vector)),zero)
                    assert not divide(p,phi)[1]
            # Lift the chosen-column identity to QQ[w].  P=I+N with N^2=0,
            # and apply all changed rows simultaneously to the same matrix.
            updated={};raw_updated={}
            for i,vector in basis:
                raw=[];row=[]
                for j in range(n):
                    p=sum((value.p*matrix[ii][j] for ii,value in enumerate(vector) if value),zero)
                    q,r=divide(p,phi);assert not r
                    raw.append(p);row.append(q)
                raw_updated[i]=raw;updated[i]=row
                trace.update(str((i,[list(map(str,value.p.coeffs())) for value in vector])).encode())
            # Explicit inverse row identity: subtract only unchanged rows.
            for i,vector in basis:
                for j in range(n):
                    recovery=raw_updated[i][j]-sum((value.p*matrix[ii][j]
                        for ii,value in enumerate(vector) if ii not in chosen and value),zero)
                    assert recovery==matrix[i][j]
            for i,row in updated.items():matrix[i]=row
            E+=len(updated);assert E<=target
            precision=total_precision-E
            for i in range(n):
                for j in range(n):matrix[i][j]=divide(matrix[i][j],phi**precision)[1]
            assert E+precision==total_precision
            rounds.append({'rationalRepresentationDimension':dim,'rationalRank':rank,
                           'actualQuotientKernelRows':len(updated),'chosenRows':chosen,
                           'extractedTotal':E,'remainingPrecision':precision,
                           'allKernelInverseAndDivisionIdentitiesVerified':True})
            say('actual_original_local_kernel_factor',factor=label,extracted=E,target=target,precision=precision)
        result.update(provedQQExponent=E,divisionMultiplyBackChecks=divisions,
                      actualQuotientInverseMultiplyBackChecks=inverse_checks,
                      kernelTraceSha256=trace.hexdigest(),elapsedSeconds=round(time.perf_counter()-began,6))
        return result

    say('original_CX_rebuilt_without_cached_inputs',sourceSha256=state['sourceSha256'],originalReconstructionSourceSha256=original_hash)
    for case in FIXED_CASES:
        result=fixed_dual_local(case)
        assert result['provedQQExponent']==case['target']
        results.append(result);save('factor_completed')
        say('complete_one_QQ_original_factor',factor=result['factor'],exponent=result['provedQQExponent'],factorSeconds=result['elapsedSeconds'])
    for root,target,label in [(fmpq(1),203,'w-1'),(fmpq(-1,2),41,'2w+1')]:
        result=linear_local(root,target,label)
        assert result['provedQQExponent']==target
        results.append(result);save('factor_completed')
        say('complete_one_QQ_original_factor',factor=label,exponent=target,factorSeconds=result['elapsedSeconds'])
    assert len(results)==9
    factors=[fmpq_poly([fmpq(c) for c in result['factorCoefficientsAscending']]) for result in results]
    coprime_checks=0
    for i in range(len(factors)):
        for j in range(i):
            g,a,b=factors[i].xgcd(factors[j])
            assert a*factors[i]+b*factors[j]==g and g==one
            coprime_checks+=1
    degree=sum(phi.degree()*result['provedQQExponent'] for phi,result in zip(factors,results))
    assert degree==1535 and coprime_checks==36
    # All factors are monic and 1009-integral, so their product is too.
    assert all(phi.leading_coefficient()==1 for phi in factors)
    assert all(int(c.denominator)%1009 for phi in factors for c in phi.coeffs())
    state.update(allFactorsProved=True,productDegree=degree,productDividesOriginalQQResultant=True,
                 pairwiseBezoutMultiplyBackChecks=coprime_checks,productMonicAnd1009Integral=True,
                 expectedResidualDegreeFromPublished3352=3352-degree)
    signal.alarm(0);save('complete_nine_original_QQ_resultant_factors')
    say('complete_nine_original_QQ_resultant_factors',factorCount=9,productDegree=degree,
        expectedResidualDegree=3352-degree,receiptSha256=sha(output.read_bytes()),
        sourceSha256=state['sourceSha256'],peakRssKiB=state['peakRssKiB'],wholeL0Excluded=False)


if __name__=='__main__':
    main()
