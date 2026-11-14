#!/usr/bin/env python3
"""Test four genuine delta2 columns plus the full old beta image against r2.

All820 standard coordinates and all505 observations are retained.  A negative
answer concerns these four columns only; the other198 high directions remain.
"""
import argparse,gzip,hashlib,importlib.util,json,struct,time
from pathlib import Path
from flint import nmod_mat

STATE='06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
READER='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
FIRST='71b3ffd524cca40f36ac59fb29694798013987c6153edb0c771420d75780daf8'
SECOND='fa9fda1c0176cbf3e8163fcfd26ed11ea4f92947587d3d455859d2b912cb38a4'
def sha(b):return hashlib.sha256(b).hexdigest()
def actual(p,expected):
 b=p.read_bytes();b=gzip.decompress(b) if p.suffix=='.gz' else b
 if sha(b)!=expected:raise ValueError('actual matrix SHA: '+str(p))
 return b
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def zero(M):return not any(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def read_remainder(path,coordinates,heads):
 b=path.read_bytes();wide=b[:8]==b'R150NX31'
 if (not wide and b[:8]!=b'R150NF31') or struct.unpack_from('<3I',b,8)!=(0,4,1034):raise ValueError('actual delta2 remainder dimensions')
 index={tuple(c):i for i,c in enumerate(coordinates)};V=[[0]*4 for _ in range(820)];offset=20;high=[[] for _ in range(4)]
 for j in range(4):
  raw,label,n=struct.unpack_from('<IHI',b,offset);offset+=10
  if raw or label!=4001+j:raise ValueError('actual delta2 source labels')
  previous=0
  for _ in range(n):
   c=struct.unpack_from('<H',b,offset)[0];offset+=2
   length=int.from_bytes(b[offset:offset+(2 if wide else 1)],'little');offset+=2 if wide else 1
   if c<=previous or c>1034 or length<1:raise ValueError('actual delta2 polynomial dictionary')
   previous=c
   for d in range(length):
    v=b[offset];offset+=1
    if v>30 or (v and c in heads and d>=heads[c]):raise ValueError('actual delta2 nonstandard coordinate')
    if v:
     if (c,d) in index:V[index[c,d]][j]=v
     else:high[j].append([c,d,v])
 if offset!=len(b):raise ValueError('complete delta2 remainder tail')
 return nmod_mat(V,31),high
def main():
 p=argparse.ArgumentParser()
 for k in ('notes-root','first-system','second-system','original-metadata','image-metadata','image-quotients','image-remainders','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 reader=a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py'
 if sha(reader.read_bytes())!=READER:raise ValueError('frozen torsion reader')
 spec=importlib.util.spec_from_file_location('actual_delta2_state',reader);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 statepath=a.out/'state-input.bin';statepath.write_bytes(actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE));state=helper.load_state(statepath)
 if (state['stateDimension'],state['torsionDimension'])!=(820,315):raise ValueError('full original state dimensions')
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get('status')!='completed' or original.get('divisor')!=961 or original.get('targetMode')!=0 or original.get('targetCount')!=4 or not original.get('allOriginalProductCoefficientsDivisible') or not original.get('originalRowScaleTransportVerified'):raise ValueError('four genuine original second Bockstein products')
 if image.get('status')!='completed' or not image.get('fullImageQuotientIdentity') or not image.get('everyRemainderIsIrreducible') or image.get('targets')!=4:raise ValueError('four complete image quotient identities')
 q=a.image_quotients.read_bytes()
 if q[:8]!=b'R150IQ31' or struct.unpack_from('<3I',q,8)!=(1034,1021,4):raise ValueError('actual delta2 Q')
 o=24;heads={}
 for _ in range(1021):
  c,d,lc=struct.unpack_from('<HBB',q,o);o+=4
  if c in heads or not 1<=c<=1034 or d>8 or not 1<=lc<=30:raise ValueError('actual G head')
  heads[c]=d
  for _ in range(4):n=struct.unpack_from('<H',q,o)[0];o+=2+n
 coordinates=[[c,d] for d in range(8) for c in range(1,1035) if c not in heads or d<heads[c]]
 if o!=len(q) or sum(heads.values())!=716 or coordinates!=state['coordinates']:raise ValueError('identical full standard-coordinate dictionary')
 V,high=read_remainder(a.image_remainders,coordinates,heads)
 J=nmod_mat(state['matrices']['action'],31);K=nmod_mat(state['matrices']['kernelTranspose'],31).transpose();O=nmod_mat(state['observabilityEchelon'],31)
 free=[i for i in range(820) if i+1 not in set(state['pivotStateCoordinates'])]
 D=nmod_mat([[int(V[i,j]) for j in range(4)] for i in free],31)
 if any(high) or not zero(O*V) or K*D!=V:raise ValueError('delta2 outside the fully paid315 torsion interface; no negative solvability claim')
 f=actual(a.first_system,FIRST)
 if f[:8]!=b'R150FB31' or struct.unpack_from('<7I',f,8)!=(31,315,4,2,9,202,6):raise ValueError('whole actual first beta system')
 o=36+4*16+2*8+315*4
 W=nmod_mat([[f[o+i*2+j] for j in range(2)] for i in range(315)],31)
 sec=actual(a.second_system,SECOND)
 if sec[:8]!=b'R150R231' or struct.unpack_from('<5I',sec,8)!=(31,820,315,2,9):raise ValueError('actual second residual matrix')
 o=28+820*9;R=nmod_mat([[sec[o+i*9+j] for j in range(9)] for i in range(315)],31);o+=315*9
 if W!=nmod_mat([[sec[o+i*2+j] for j in range(2)] for i in range(315)],31):raise ValueError('same whole first beta image')
 generators=[nmod_mat([[int(W[i,j])] for i in range(315)],31) for j in range(2)]+[nmod_mat([[int(D[i,j])] for i in range(315)],31) for j in range(4)]
 echelon=[];basis=[];descriptors=[];piv=[];recurrences=[]
 for g,v0 in enumerate(generators):
  v=v0
  for exponent in range(316):
   raw=[int(v[i,0]) for i in range(315)];red=raw[:]
   for pivot,e in echelon:
    c=red[pivot]
    if c:red=[(a-c*b)%31 for a,b in zip(red,e)]
   if not any(red):recurrences.append({'generator':g,'firstDependentExponent':exponent});break
   if exponent==315:raise ValueError('finite full315 Krylov failed')
   pivot=next(i for i,x in enumerate(red) if x);inv=pow(red[pivot],-1,31);red=[x*inv%31 for x in red]
   echelon.append((pivot,red));piv.append(pivot);basis.append(raw);descriptors.append([g,exponent]);v=J*v
 rank=len(basis);B=nmod_mat([[basis[j][i] for j in range(rank)] for i in range(315)],31)
 square=nmod_mat([[basis[j][i] for j in range(rank)] for i in piv],31);inv=square.inv()
 JB=J*B;action=inv*nmod_mat([[int(JB[i,j]) for j in range(rank)] for i in piv],31)
 if B*action!=JB:raise ValueError('complete six-generator polynomial span is not J invariant')
 solution=inv*nmod_mat([[int(R[i,j]) for j in range(9)] for i in piv],31);diff=R-B*solution
 compatible=[all(not int(diff[i,j]) for i in range(315)) for j in range(9)]
 polynomials=[[[] for _ in range(9)] for _ in range(6)]
 for k,(g,exponent) in enumerate(descriptors):
  out=g+4 if g<2 else g-2
  for j in range(9):
   if compatible[j] and (v:=int(solution[k,j])):
    co=polynomials[out][j]
    if len(co)<=exponent:co.extend([0]*(exponent+1-len(co)))
    co[exponent]=(co[exponent]+v)%31
 for row in polynomials:
  for co in row:
   while co and not co[-1]:co.pop()
 # Reconstruct every published positive column from all315 actual coordinates.
 verify=nmod_mat(315,9,31)
 for i,g in enumerate(generators):
  out=i+4 if i<2 else i-2;current=g
  for exponent in range(max([len(co) for co in polynomials[out]]+[0])):
   coeff=nmod_mat([[co[exponent] if exponent<len(co) else 0 for co in polynomials[out]]],31);verify+=current*coeff;current=J*current
 for j,ok in enumerate(compatible):
  if ok and any(int(verify[i,j])!=int(R[i,j]) for i in range(315)):raise ValueError('full315 published source polynomial identity')
 duals=[]
 for j,ok in enumerate(compatible):
  if ok:continue
  r=next(i for i in range(315) if int(diff[i,j]));scale=pow(int(diff[r,j]),-1,31)
  weights={r:scale};row=nmod_mat([[int(B[r,k]) for k in range(rank)]],31)*inv
  for k,i in enumerate(piv):weights[i]=(weights.get(i,0)-scale*int(row[0,k]))%31
  weights={i:v for i,v in weights.items() if v}
  if any(sum(v*int(B[i,k]) for i,v in weights.items())%31 for k in range(rank)) or sum(v*int(R[i,j]) for i,v in weights.items())%31!=1:raise ValueError('complete four-column negative dual')
  duals.append({'target':j+2,'annihilatesWholeFourDeltaPlusFirstBetaPolynomialImage':True,'rightHandSide':1,'coordinates':[{'torsionCoordinate':i+1,'stateCoordinate':free[i]+1,'normalFormComponent':coordinates[free[i]][0],'parameterExponent':coordinates[free[i]][1],'weight':v} for i,v in sorted(weights.items())]})
 packed=bytearray(b'R150D2S1')+struct.pack('<5I',31,315,4,rank,9)
 for g,e in descriptors:packed+=struct.pack('<HH',g,e)
 for M in (D,W,R,B,action,solution,diff):packed.extend(bytes(x for row in rows(M) for x in row))
 system=a.out/'four-second-bockstein-system.bin.gz';system.write_bytes(gzip.compress(packed,mtime=0))
 result={'format':'r150-four-genuine-second-bockstein-quotient-test-v1','status':'completed','prime':31,'sourceSHA256':sha(Path(__file__).read_bytes()),'stateSHA256':STATE,'firstBetaSystemSHA256':FIRST,'actualSecondResidualSystemSHA256':SECOND,'originalDeltaMetadataSHA256':sha(a.original_metadata.read_bytes()),'deltaRemaindersSHA256':sha(a.image_remainders.read_bytes()),'all820NormalCoordinatesRetained':True,'all505ObservationsVerified':True,'fourActualColumnsInTorsion':True,'completeFirstBocksteinImageDimension':2,'fourPlusFirstBetaPolynomialImageDimension':rank,'secondImageDimensionModuloFirstBeta':rank-2,'full315JInvarianceVerified':True,'actualPolynomialGeneratorOrder':['beta199','beta200','deltaS200','deltaS201','deltaS202','deltaSell'],'selectedKrylovBasisDescriptors':descriptors,'firstDependences':recurrences,'nineTargetsCompatibleWithFourColumns':compatible,'allNineCompatible':all(compatible),'solutionRowOrder':['deltaS200','deltaS201','deltaS202','deltaSell','beta199','beta200'],'solutionPolynomialsAscending':polynomials,'maximumSolutionDegree':max([len(c)-1 for row in polynomials for c in row]+[-1]),'allPublishedPositiveFull315IdentitiesVerified':True,'dualCertificates':duals,'remaining198DirectionsComputed':False,'fullSecondBocksteinImageClaimed':False,'finite_budget_verified':False,'fullOriginalMod29791IdentityVerified':False,'system':{'file':system.name,'bytes':len(packed),'sha256':sha(packed),'gzipBytes':system.stat().st_size,'gzipSHA256':sha(system.read_bytes())},'elapsedSeconds':time.monotonic()-start}
 (a.out/'four-second-bockstein-result.json').write_text(json.dumps(result,indent=2)+'\n');statepath.unlink();print(json.dumps({k:result[k] for k in ('status','fourPlusFirstBetaPolynomialImageDimension','secondImageDimensionModuloFirstBeta','nineTargetsCompatibleWithFourColumns','maximumSolutionDegree','remaining198DirectionsComputed','elapsedSeconds')}),flush=True)
if __name__=='__main__':main()
