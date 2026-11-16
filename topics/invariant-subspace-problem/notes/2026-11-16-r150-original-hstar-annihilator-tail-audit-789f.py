#!/usr/bin/env python3
"""Read-only audit of paid hstar carries, common true16 basis and socle lines.
AI-assisted: GPT-6 Astra Pro / literature_audit, 2026-11-16.
No original source solve, integer carry, or elimination is repeated.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,sys,time
from pathlib import Path
from flint import nmod_mat
FORMAT='r150-original-hstar-annihilator-tail-audit-v1'
READER_SHA='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
EXP=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
PARENT='712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093'
CARRY='4044954d51c3d23ced04aa55ae8355c6877c2153f92984807c6454572e85e4cd'
SOCLE='dce92fb5bbd50efc3cf5bd39a5b7fbf27dec7f88e4c3e0b9308cfff47b042b98'
PINS={
'state':('global197-original-inputs/state.bin',1470456,'06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'),
'recipe':('root2-fourth-complete210-preparation/complete210-fourth-source-recipes.json.gz',33227,'4c40ce9af0ad97eb38bf6e754e8f08ab106fa30028ab829fb1657c2a8dc607a2'),
'parentReceipt':('root2-fourth-complete210-p7/root2-fourth-complete210-receipt.json',42372,'dd867cfbbefcce2d7a846016807b1da6f56c73fd82ea9a364036348467bdc5b9'),
'D5':('root2-fourth-complete210-p7/stages/L5-all208-paid-class-check/exact-class.json',138587,'d00f76626a0a5d80ce9a826315562170d9d32bbc5a44ba6f00197a4bf7006705'),
'parentResult':('root2-fourth-complete210-p7/complete210-exact-result.json',141288,'30d9c04e68e337e2ac5019e527e97e211104b1e9276ff7caf24619a804fde8b9'),
'C1':('original-hstar-first-carry/hstar-first-carry-in-true16-coordinates.json',515,'2aeda22a10ca9a7f13b82649f48fe9fd6913c2346c1d848db8b0a5dca2528c3d'),
'carryReceipt':('original-hstar-first-carry/original-hstar-first-carry-receipt.json',16583,'86aa0442ee2b24373fbc23b27495b0546f640c679e05c3c4727a5953fab605ea'),
'D1':('original-hstar-first-carry/stages/hstar-first-carry-complete315/complete315-class.json',6889,'ed45b987a205d025d2128ff9df119a279a4f6622bf649f42732d449859ae45c2'),
'carryResult':('original-hstar-first-carry/complete-hstar-first-carry-result.json',1741,'3b3ef60c19b77594fda9f931d4831f140a7e326df34cb4977d83f7c357c5adbb'),
'socleReceipt':('original-h0-seven-socle/original-h0-seven-socle-receipt.json',23423,'6533b887811d674adfcfbb0fd09b440710db40df7eb341326af75739b0564e5f'),
'socleResult':('original-h0-seven-socle/complete-seven-socle-result.json',1028,'ebd9b1bb82ca732e2a0acb6ebf5aed8046eeed9d0cbeab82eac803ee63967f82')
}
def req(x,s):
    if not x:raise AssertionError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def record(M):return {'rows':M.nrows(),'columns':M.ncols(),'sha256':sha(bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols())))}
def sub(M,I,J):return nmod_mat([[int(M[i,j]) for j in J] for i in I],31)
def join(*M):return nmod_mat([[int(A[i,j]) for A in M for j in range(A.ncols())] for i in range(M[0].nrows())],31)
def iszero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def main():
    ar=argparse.ArgumentParser();ar.add_argument('--work',type=Path,required=True);ar.add_argument('--reader',type=Path,required=True);ar.add_argument('--out',type=Path,required=True);a=ar.parse_args();start=time.monotonic()
    req(sha(a.reader.read_bytes())==READER_SHA,'Exact original whole315 state reader')
    data={};identities={}
    for name,(rel,size,hs) in PINS.items():
        raw=(a.work/rel).read_bytes();req(len(raw)==size and sha(raw)==hs,'Exact paid input '+name);identities[name]={'path':rel,'bytes':size,'sha256':hs}
        if name!='state':data[name]=json.loads(gzip.decompress(raw) if rel.endswith('.gz') else raw)
    for name,binding in [('parentReceipt',PARENT),('carryReceipt',CARRY),('socleReceipt',SOCLE)]:
        req(data[name]['binding']==binding and data[name]['status']=='completed','Actual completed original ancestor '+name)
    for name,binding in [('D5',PARENT),('parentResult',PARENT),('C1',CARRY),('D1',CARRY),('carryResult',CARRY),('socleResult',SOCLE)]:
        req(data[name]['binding']==binding,'Exact actual source binding '+name)
    cr=data['carryResult'];sr=data['socleResult']
    for name in ['all104LocalFreeChecks','all505GlobalFreeChecks','allComplete315SpanIdentitiesVerified','allOriginal17IntegerProductsVerified','allOriginalSourceCorrectionsRetained']:
        req(cr[name] and sr[name],'Paid complete original gate '+name)
    req(cr['exactExponentsWhenClosed']==[5]*9 and sr['minimum31DenominatorExponents']==[2]*9,'Previously completed original exponent statements')
    req(cr['trueGeneratorExponents']==EXP and sr['socleRowExponents']==[4,4,4,4,5,5,6],'Common true source orders')
    req(sr['socleSourceLabels']==[15001,15002,15003,15004,20011,20012,30013] and sr['targetLabels']==list(range(2,11)) and cr['targetLabels']==list(range(2,11)),'Identical original source and target labels')
    spec=importlib.util.spec_from_file_location('paid_original_state_reader',a.reader);reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
    state=reader.load_state(a.work/PINS['state'][0]);J=nmod_mat(state['matrices']['action'],31)
    U13=nmod_mat(data['recipe']['true13Full315'],31);D5=nmod_mat(data['D5']['matrixRows'],31);D6=nmod_mat(data['parentResult']['whole315Classes'],31)
    req(record(D5)==data['parentReceipt']['parameters']['comparisons']['L5-all208-paid-class-check']['matrix'],'All paid L5 columns')
    req(record(D6)==data['parentReceipt']['parameters']['comparisons']['L6-all210-complete-quotient']['matrix'],'All paid L6 columns')
    U15=join(U13,sub(D5,range(315),[10,11]));U16=join(U15,sub(D6,range(315),[12]))
    for name,M in [('true13',U13),('true15',U15),('true16',U16)]:
        req(record(M)==data['carryReceipt']['parameters']['trueBasisIdentities'][name]==data['socleReceipt']['parameters']['trueBasisIdentities'][name],'Same whole315 true source basis '+name)
    req(U16.rank()==16,'Complete actual true16 independent basis')
    rr,r=U16.transpose().rref();I=[next(j for j in range(315) if rr[i,j]) for i in range(r)]
    JU=J*U16;J16=sub(U16,I,range(16)).inv()*sub(JU,I,range(16));req(U16*J16==JU,'All 5040 original parameter-action products')
    req(all(not J16[i,j] for i in range(16) for j in range(16) if EXP[i]>EXP[j]),'Order-respecting mod-p action in the actual true basis')
    C1=nmod_mat(data['C1']['coordinates'],31);D1=nmod_mat(data['D1']['matrixRows'],31)
    req(record(C1)==cr['firstCarryCoordinates'] and record(D1)==cr['firstCarry'],'Same original first-carry matrices')
    req(U16*C1==D1,'All 2835 original first-carry coordinate products')
    high4=[i for i,e in enumerate(EXP) if e>=4];high5=[i for i,e in enumerate(EXP) if e>=5]
    C4=sub(C1,high4,range(9));C5=sub(C1,high5,range(9));J4=sub(J16,high4,high4);J5=sub(J16,high5,high5)
    req(C4.rank()==4 and C5.rank()==3,'Actual complete high-layer ranks')
    req(J4*C4==C4*2 and J5*C5==C5*2,'Every high-layer carry column has the actual root2 parameter action')
    O=nmod_mat(sr['obstructionRows'],31);req(record(O)==sr['obstruction'] and O.nrows()==7 and O.ncols()==9,'Exact full seven-socle matrix')
    req(iszero(sub(O,range(4),range(9))) and O.rank()==1,'No e4 socle component; complete image rank one')
    N=nmod_mat(7,9,31)
    for j in range(9):N[6,j]=C1[15,j]
    req(all(C1[15,j] and O[4,j] for j in range(9)),'Each original target has both actual independent nonzero socle readings')
    for j in range(9):req(join(sub(O,range(7),[j]),sub(N,range(7),[j])).rank()==2,'Separate two-socle independence for every original target')
    req(join(O,N).rank()==2,'Two distinct complete socle image lines')
    semantic={'sourceSHA256':sha(Path(__file__).read_bytes()),'readerSHA256':READER_SHA,'inputs':identities,'sourceExponents':EXP,'prime':31}
    result={'format':FORMAT,'status':'completed','binding':sha(canonical(semantic)),'inputIdentities':identities,'sourceSHA256':semantic['sourceSHA256'],'readerSHA256':READER_SHA,
       'true16':record(U16),'parameterAction16':record(J16),'all5040OriginalParameterActionProducts':True,'all2835OriginalCarryCoordinateProducts':True,
       'sameTrueBasisForCarryAndSevenSocle':True,'highAtLeastFourDimension':7,'highAtLeastFourCarryRank':4,'highAtLeastFiveDimension':3,'highAtLeastFiveCarryRank':3,
       'highCarryImagesKilledBySMinusTwo':True,'oldHZeroSocleFirstFourRowsZero':True,'oldHZeroSocleImageRank':1,'fourthPStarImageRank':1,'jointTwoSocleImageRank':2,
       'allNineIndividualTwoSoclePairsIndependent':True,'bothNonzeroReadingsForEveryOriginalTarget':True,
       'newIntegerCarriesOrSourceSolvesExecuted':False,'rootOneHiddenSocleNotDiscarded':True,'mathematicalArraysRemainTemporary':True,
       'elapsedSeconds':time.monotonic()-start,'peakResidentKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(canonical(result)+b'\n');print(json.dumps(result,sort_keys=True),flush=True)
if __name__=='__main__':main()
