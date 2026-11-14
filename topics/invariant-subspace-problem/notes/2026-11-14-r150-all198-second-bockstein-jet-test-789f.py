#!/usr/bin/env python3
"""Complete primary second image from all198 new and all4 actual old columns.

Every143 local coordinate and every104 free constraint is retained. A positive
answer is followed by real global source recovery; it is not a global identity.
"""
import argparse,gzip,hashlib,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat

MAP='3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716'
RECEIPT='5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df'
def sha(b):return hashlib.sha256(b).hexdigest()
def zero(M):return M==nmod_mat(M.nrows(),M.ncols(),31)
def serial(M):return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def readmap(binary,receipt):
 b=binary.read_bytes();r=receipt.read_bytes()
 if sha(b)!=MAP or sha(r)!=RECEIPT:raise ValueError('same exact143 quotient map and receipt')
 meta=json.loads(r);M={}
 for name,spec in meta['matrices'].items():
  off,n,m=spec['offset'],spec['rows'],spec['columns'];data=b[off:off+n*m]
  if len(data)!=n*m or sha(data)!=spec['sha256']:raise ValueError('complete matrix '+name)
  M[name]=nmod_mat([[data[i*m+j] for j in range(m)] for i in range(n)],31)
 return meta,M
def main():
 p=argparse.ArgumentParser()
 for key in ('map','map-receipt','state','product-metadata','normal-metadata','out'):p.add_argument('--'+key,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 meta,M=readmap(a.map,a.map_receipt)
 pr=json.loads(a.product_metadata.read_text());nf=json.loads(a.normal_metadata.read_text())
 if pr.get('status')!='completed' or pr.get('targetCount')!=198 or not all(pr.get(k) for k in ('sameOriginalIntegerKernelRepresentative','qJetsFromSameGlobalVQAndOriginalDAG','allOriginalProductJetCoefficientsDivisible','originalRowScaleTransportVerified')):raise ValueError('all198 genuine integer original17 jet products')
 if nf.get('status')!='completed' or nf.get('targets')!=198 or not all(nf.get(k) for k in ('sameOriginalConstantPrebasis','fullLocalPrebasisSourceIdentity','fullLocalGQuotientIdentity','allRemaindersStandard')):raise ValueError('all198 complete local source identities')
 data=a.state.read_bytes()
 if data[:8]!=b'R150JE31' or struct.unpack_from('<4I',data,8)!=(31,820,198,8):raise ValueError('all198 full820 state')
 labels=list(struct.unpack_from('<198H',data,24));off=24+396
 coordinates=[list(struct.unpack_from('<HB',data,off+3*i)) for i in range(820)];off+=820*3
 if coordinates!=meta['standardCoordinates'] or len(data)!=off+820*198 or len(set(labels))!=198:raise ValueError('same complete820 coordinate/source dictionary')
 V=nmod_mat([[data[off+i*198+j] for j in range(198)] for i in range(820)],31)
 Y=M['Pi']*V;free=M['freeChecks']*Y;D=M['torsionCoordinates']*Y
 if not zero(free) or M['torsionEmbedding']*D!=Y:
  failures=[[i+1,labels[j],int(free[i,j])] for i in range(104) for j in range(198) if free[i,j]]
  (a.out/'all198-free-failure.json').write_text(json.dumps({'status':'failed','reason':'nonzero-in-retained104-free-directions','failures':failures},indent=2)+'\n')
  raise ValueError('a new local column has a retained free component; no37 solvability claim')
 J=M['J39'];W=M['W39'];old=M['D39'];R=M['R39']
 # Priority preserves old work. Output polynomial order:198 new,4 old,2 beta.
 generators=[nmod_mat([[int(W[i,j])] for i in range(39)],31) for j in range(2)]
 generators += [nmod_mat([[int(old[i,j])] for i in range(39)],31) for j in range(4)]
 generators += [nmod_mat([[int(D[i,j])] for i in range(39)],31) for j in range(198)]
 echelon=[];basis=[];descriptors=[];pivots=[];relations=[]
 for gi,vector in enumerate(generators):
  current=vector
  for exponent in range(9):
   raw=[int(current[i,0]) for i in range(39)];red=raw[:]
   for pivot,row in echelon:
    c=red[pivot]
    if c:red=[(a-c*b)%31 for a,b in zip(red,row)]
   if not any(red):relations.append([gi,exponent]);break
   if exponent==8:raise ValueError('g-degree8 complete primary closure failed')
   pivot=next(i for i,x in enumerate(red) if x);inv=pow(red[pivot],-1,31);red=[x*inv%31 for x in red]
   echelon.append((pivot,red));pivots.append(pivot);basis.append(raw);descriptors.append([gi,exponent]);current=J*current
 rank=len(basis);B=nmod_mat([[basis[j][i] for j in range(rank)] for i in range(39)],31)
 inv=nmod_mat([[basis[j][i] for j in range(rank)] for i in pivots],31).inv()
 JB=J*B;action=inv*nmod_mat([[int(JB[i,j]) for j in range(rank)] for i in pivots],31)
 if B*action!=JB:raise ValueError('whole204-generator polynomial primary span is not invariant')
 solution=inv*nmod_mat([[int(R[i,j]) for j in range(9)] for i in pivots],31);difference=R-B*solution
 compatible=[all(not difference[i,j] for i in range(39)) for j in range(9)]
 polys=[[[] for _ in range(9)] for _ in range(204)]
 def output_index(g):return 202+g if g<2 else 198+g-2 if g<6 else g-6
 for k,(g,e) in enumerate(descriptors):
  for j in range(9):
   if compatible[j] and (v:=int(solution[k,j])):
    row=polys[output_index(g)][j]
    if len(row)<=e:row.extend([0]*(e+1-len(row)))
    row[e]=(row[e]+v)%31
 for row in polys:
  for co in row:
   while co and not co[-1]:co.pop()
 check=nmod_mat(39,9,31)
 for gi,v in enumerate(generators):
  row=polys[output_index(gi)];current=v
  for e in range(max([len(c) for c in row]+[0])):
   coefficients=nmod_mat([[c[e] if e<len(c) else 0 for c in row]],31);check+=current*coefficients;current=J*current
 for j,ok in enumerate(compatible):
  if ok and any(check[i,j]!=R[i,j] for i in range(39)):raise ValueError('complete39 positive polynomial identity')
 duals=[]
 for j,ok in enumerate(compatible):
  if ok:continue
  r=next(i for i in range(39) if difference[i,j]);scale=pow(int(difference[r,j]),-1,31)
  row=nmod_mat(1,39,31);row[0,r]=scale;co=nmod_mat([[int(B[r,k]) for k in range(rank)]],31)*inv
  for k,i in enumerate(pivots):row[0,i]=int(row[0,i])-scale*int(co[0,k])
  if not zero(row*B) or int((row*R)[0,j])!=1:raise ValueError('whole202-generator exact negative dual')
  state=row*M['torsionCoordinates']*M['Pi']
  duals.append({'target':j+2,'rightHandSide':1,'annihilatesWhole202HighKernelPolynomialPrimarySecondImageAndFullFirstImage':True,'torsion39Weights':[int(row[0,i]) for i in range(39)],'all820StateWeights':[{'component':coordinates[i][0],'parameterExponent':coordinates[i][1],'weight':int(state[0,i])} for i in range(820) if state[0,i]]})
 packed=bytearray(b'R150J2S1')+struct.pack('<8I',31,143,104,39,37,198,rank,9)
 for g,e in descriptors:packed+=struct.pack('<HH',g,e)
 for mat in (Y,free,D,W,old,R,B,action,solution,difference):packed.extend(serial(mat))
 system=a.out/'all198-second-primary-system.bin.gz';system.write_bytes(gzip.compress(packed,mtime=0))
 result={'format':'r150-complete198-genuine-jet-second-primary-image-v1','status':'completed','prime':31,
 'sourceSHA256':sha(Path(__file__).read_bytes()),'mapSHA256':MAP,'mapReceiptSHA256':RECEIPT,
 'stateSHA256':sha(data),'originalProductMetadataSHA256':sha(a.product_metadata.read_bytes()),'localNormalMetadataSHA256':sha(a.normal_metadata.read_bytes()),
 'all143LocalCoordinatesRetained':True,'all104FreeChecksVerified':True,'all198GenuineColumnsComputed':True,'oldFourGenuineColumnsReused':True,
 'all202HighKernelDirectionsCovered':True,'other1632ExactKoszulDirectionsHaveZeroSecondImage':True,
 'relevantPrimaryImageComplete':True,'all198Coverage':True,'old4Coverage':True,'low1632Coverage':True,
 'completeFirstImageDimension':2,'completeSecondPrimaryImageWithFirstDimension':rank,'secondPrimaryImageModuloFirstDimension':rank-2,
 'completePrimaryPolynomialInvarianceVerified':True,'nineTargetsPrimaryCompatible':compatible,'allNinePrimaryCompatible':all(compatible),
 'globallyObstructedTargetLabels':[j+2 for j,ok in enumerate(compatible) if not ok],
 'numberOfGloballyObstructedTargets':sum(not ok for ok in compatible),'allNineGloballyObstructed':not any(compatible),
 'selectedKrylovBasisDescriptors':descriptors,'firstDependentExponents':relations,'actual198KernelHeadLabels':labels,
 'generatorOrder':['beta199','beta200','deltaS200','deltaS201','deltaS202','deltaSell']+[f'deltaK{i+1}' for i in range(198)],
 'solutionRowOrder':[f'deltaK{i+1}' for i in range(198)]+['deltaS200','deltaS201','deltaS202','deltaSell','beta199','beta200'],
 'solutionPolynomialsAscending':polys,'maximumSolutionDegree':max([len(c)-1 for row in polys for c in row]+[-1]),
 'allPublishedPositiveFull39IdentitiesVerified':True,'dualCertificates':duals,
 'globalProjectorAscending':meta['globalPrimaryProjectorAscending'],'globalProjectorDegree':189,
 'negativeScope':'For each listed negative target, no integer polynomial source of any degree can lift the fixed H0 target to modulus29791, including all changes of lower-precision kernel representative. This does not exclude a rational source with a31-divisible denominator.',
 'positiveScope':'A compatible primary class requires actual global nine-combination source restoration and the full original17 product; no such identity is claimed here.',
 'fullGlobalSecondImageComputed':False,'finite_budget_verified':False,'fullOriginalMod29791IdentityVerified':False,
 'outcome':'primary-compatible-global-source-continuation-required' if all(compatible) else 'complete-second-primary-obstruction',
 'system':{'file':system.name,'bytes':len(packed),'sha256':sha(packed),'gzipBytes':system.stat().st_size,'gzipSHA256':sha(system.read_bytes())},
 'elapsedSeconds':time.monotonic()-start}
 (a.out/'all198-second-primary-result.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('status','completeSecondPrimaryImageWithFirstDimension','secondPrimaryImageModuloFirstDimension','nineTargetsPrimaryCompatible','outcome','elapsedSeconds')}),flush=True)
if __name__=='__main__':main()
