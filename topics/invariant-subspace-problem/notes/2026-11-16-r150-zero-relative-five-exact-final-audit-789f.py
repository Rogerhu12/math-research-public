#!/usr/bin/env python3
"""Independent exact audit of the five original zero detectors.
AI-assisted, 2026-11-16. Reads only completed temporary outputs; never resolves a
unit or modifies a parent checkpoint. All original 6188 equations are rebuilt.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,resource,sys,time
from pathlib import Path
from flint import fmpq,fmpq_mat
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
FORMAT='r150-zero-relative-five-exact-final-audit-v1'
BINDING='f50f05947ab0a71758683fe1355b5c9f4b1cd471f321eea10374aba9c36891f0'
RECEIPT_SHA='a3c4537b55021529b2e96cde3e04e56fda2218b5d8c04968bc81a38984e7f8ac'
MANIFEST_SHA='9bfb317570971b2bd45e7f0925a2d6657653ec2f2fe0b95d1b75d92269ec9758'
GEN_SHA='2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186'
ACT_SHA='2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332'
def req(x,s):
    if not x:raise AssertionError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def mh(M):
    h=hashlib.sha256();h.update(f'{M.nrows()},{M.ncols()}\n'.encode())
    for i in range(M.nrows()):h.update(('\t'.join(str(M[i,j]) for j in range(M.ncols()))+'\n').encode())
    return h.hexdigest()
def decode(x):
    req(len(x['entries'])==x['rows']*x['columns'],'Full matrix entry count')
    M=fmpq_mat(x['rows'],x['columns'],[fmpq(z) for z in x['entries']])
    req(mh(M)==x['logicalSHA256'],'Complete mathematical matrix identity');return M
def mod(name,p,h):
    req(sha(Path(p).read_bytes())==h,'Frozen '+name)
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sub(M,rows,cols):return fmpq_mat([[M[i,j] for j in cols] for i in rows])
def zero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def main():
    ar=argparse.ArgumentParser()
    for x in ('checkpoints','receipt','generator','actions','out'):ar.add_argument('--'+x,required=True)
    a=ar.parse_args();start=time.monotonic();cp=Path(a.checkpoints)
    rb=Path(a.receipt).read_bytes();req(sha(rb)==RECEIPT_SHA,'Complete executed receipt')
    r=json.loads(rb);req(r['status']=='completed' and r['exitCode']==0 and r['binding']==BINDING,'Actual completed original calculation')
    mb=(cp/'manifest.json').read_bytes();req(sha(mb)==MANIFEST_SHA,'Complete immutable final inventory');man=json.loads(mb);req(man['binding']==BINDING,'Original child identity')
    def phase(name):
        z=man['phases'][name];req(z['verified'],'Only a completed verified phase')
        b=(cp/z['file']).read_bytes();req(len(b)==z['bytes'] and sha(b)==z['sha256'],'Phase compressed identity')
        raw=gzip.decompress(b);req(sha(raw)==z['payloadSHA256'],'Phase uncompressed identity')
        x=json.loads(raw);req(x['binding']==BINDING and x['phase']==name,'Phase semantic identity');return x['value']
    final=phase('complete-result');J=decode(final['action']);C=decode(final['targetCoordinates']);pair=decode(final['finitePairing'])
    req((J.nrows(),J.ncols(),C.nrows(),C.ncols(),pair.nrows(),pair.ncols())==(5,5,5,27,27,5),'Exact completed shapes')
    lam=[decode(phase(f'candidate-cochain-00-{k:02d}')['matrix']) for k in range(11)]
    req([mh(x) for x in lam]==r['parameters']['newCochainSHA256'],'All eleven original cochain identities')
    g=mod('audit_original_generator',a.generator,GEN_SHA);act=mod('audit_original_actions',a.actions,ACT_SHA)
    selection=[(d,c) for d in (0,1,2) for c in act.target_columns(d) if d<2 or sum(c[:2])==0 or (c[1]==0 and 1<=c[0]<=3 and all(2<=j<=5 for j in c[2]))]
    req(len(selection)==230 and all((x.nrows(),x.ncols())==(230,5) for x in lam),'All output coordinates')
    coeff=act.original_coefficients(g,'zero',10)
    req(coeff['physical']==r['parameters']['originalPhysicalHashes'],'Original physical Taylor coefficients')
    rows=[(d,row) for d in range(4) for row in act.source_rows(d)];req(len(rows)==6188,'Every original source row')
    ix={d:{c:i for i,(dd,c) in enumerate(selection) if dd==d} for d in (0,1,2)}
    terms=[[] for k in range(11)]
    for row_index,(_,row) in enumerate(rows):
        for k in range(11):
            for d in (0,1,2):
                for j,q in act.sparse_row_terms(coeff,k,row,d,ix[d]):
                    if q:terms[k].append((row_index,j,q))
    for k in range(11):
        E=fmpq_mat(6188,5)
        for i in range(k+1):
            for row,j,q in terms[i]:
                for c in range(5):E[row,c]+=q*lam[k-i][j,c]
        req(zero(E),'Complete original product at coefficient '+str(k))
    targets=[selection.index((2,(0,0,(j,j)))) for j in range(2,11)]
    got=fmpq_mat(27,5)
    for a0 in range(3):
        for q,j in enumerate(targets):
            for c in range(5):got[9*a0+q,c]=lam[10-a0][j,c]
    req(got==pair,'Original square readout in all 27 columns')
    for a0 in range(3,11):req(all(not lam[10-a0][j,c] for j in targets for c in range(5)),'All higher original shifted squares vanish')
    basis_cols=r['parameters']['targetBasisColumnIndices'];B=sub(pair.transpose(),range(5),basis_cols)
    req(B.rank()==5 and B*C==pair.transpose(),'Faithful full five-dimensional target coordinates')
    for j in range(27):req(J*sub(C,range(5),[j])==(sub(C,range(5),[j+9]) if j<18 else fmpq_mat(5,1)),'Every actual parameter action')
    powers=[fmpq_mat([[int(i==j) for j in range(5)] for i in range(5)])]
    for k in range(3):powers.append(powers[-1]*J)
    ranks=[x.rank() for x in powers];req(ranks==[5,2,1,0],'Exact rational zero partition')
    req(sub(C,range(5),range(9,27)).rank()==2 and sub(C,range(5),range(18,27)).rank()==1,'All positive-shift images')
    cyclic=[]
    for j in range(9):cyclic.append(fmpq_mat([[C[i,j],C[i,j+9],C[i,j+18]] for i in range(5)]).rank())
    req(cyclic==[3]*9,'Each original target has exact zero annihilator s^3')
    generators=None
    for js in itertools.combinations(range(9),3):
        cols=[j+9*k for j in js for k in range(3)]
        if sub(C,range(5),cols).rank()==5:generators=[j+2 for j in js];break
    req(generators is not None,'Three actual original targets generate the zero primary')
    out={'format':FORMAT,'status':'completed','parentBinding':BINDING,'parentReceiptSHA256':RECEIPT_SHA,'parentManifestSHA256':MANIFEST_SHA,
         'all340340OriginalProductsZero':True,'all27OriginalTargetPairingsVerified':True,'all27ParameterActionsVerified':True,
         'rationalActionRanks':ranks,'exactZeroPartition':[3,1,1],'originalTargetBasisLabels':[j+2 for j in basis_cols],
         'everyOriginalTargetCyclicZeroDimension':3,'threeOriginalTargetGenerators':generators,
         'completeOriginalTargetImageDimension':5,'positiveShiftImageDimension':2,'secondShiftImageDimension':1,
         'sourceSHA256':sha(Path(__file__).read_bytes()),'elapsedSeconds':time.monotonic()-start,'peakResidentKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'mathematicalArraysRemainTemporary':True}
    Path(a.out).write_bytes(canon(out)+b'\n');print(json.dumps(out,sort_keys=True),flush=True)
if __name__=='__main__':main()

