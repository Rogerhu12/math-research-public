#!/usr/bin/env python3
"""Project the actual second residual, retaining every free-coordinate test.

The complete known first Bockstein image tests all possible lifts with the
current mod31 initial source.  It does not cover other mod31 initial sources,
all kernels modulo961, or characteristic-zero sources with31 denominators.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,time
from pathlib import Path
import flint
from flint import nmod_mat,nmod_poly

STATE='06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
READER='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
SYSTEM='71b3ffd524cca40f36ac59fb29694798013987c6153edb0c771420d75780daf8'

def sha(data):return hashlib.sha256(data).hexdigest()
def actual(path,expected):
 data=path.read_bytes()
 if path.suffix=='.gz':data=gzip.decompress(data)
 if sha(data)!=expected:raise ValueError('frozen input checksum: '+str(path))
 return data
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def zero(M):return not any(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def pivots(M,rank):return [next(j for j in range(M.ncols()) if int(M[i,j])) for i in range(rank)]

def main():
 p=argparse.ArgumentParser()
 for name in ('notes-root','complete-beta-results','original-metadata','image-metadata','image-quotients','image-remainders','out'):
  p.add_argument('--'+name,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 hp=a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py'
 if sha(hp.read_bytes())!=READER:raise ValueError('frozen state reader')
 spec=importlib.util.spec_from_file_location('actual_complete_r150_state',hp);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 statefile=a.out/'state-input.bin';statefile.write_bytes(actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE));state=helper.load_state(statefile)
 if (state['stateDimension'],state['torsionDimension'])!=(820,315):raise ValueError('complete original state')
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get('status')!='completed' or not original.get('actualFullOriginalIdentityMod961') or original.get('divisor')!=961 or original.get('actualSourceCost')!=86 or original.get('residualOutputCostBound')!=86:raise ValueError('actual complete original second residual with cost86')
 if image.get('status')!='completed' or not image.get('fullImageQuotientIdentity') or not image.get('everyRemainderIsIrreducible') or image.get('originalRightHandSideCostBound')!=86:raise ValueError('full actual image quotient identity')
 q=a.image_quotients.read_bytes()
 if q[:8]!=b'R150IQ31' or struct.unpack_from('<4I',q,8)!=(1034,1021,9,86):raise ValueError('actual nine image quotients')
 offset=24;heads={}
 for _ in range(1021):
  c,d,lc=struct.unpack_from('<HBB',q,offset);offset+=4
  if c in heads or not 1<=c<=1034 or d>8 or not 1<=lc<=30:raise ValueError('complete image head dictionary')
  heads[c]=d
  for j in range(9):n=struct.unpack_from('<H',q,offset)[0];offset+=2+n
 coordinates=[[c,d] for d in range(8) for c in range(1,1035) if c not in heads or d<heads[c]]
 if offset!=len(q) or sum(heads.values())!=716 or coordinates!=state['coordinates'] or [c for c in range(1,1035) if c not in heads]!=state['freeComponents']:raise ValueError('identical complete standard coordinate dictionary')
 index={tuple(x):i for i,x in enumerate(coordinates)}
 data=a.image_remainders.read_bytes()
 if data[:8]!=b'R150NF31' or struct.unpack_from('<3I',data,8)!=(0,9,1034):raise ValueError('full nine original irreducible remainders')
 offset=20;V=[[0]*9 for _ in range(820)];high=[[] for _ in range(9)]
 for j in range(9):
  raw,target,n=struct.unpack_from('<IHI',data,offset);offset+=10
  if raw or target!=j+2:raise ValueError('actual original target labels')
  previous=0
  for _ in range(n):
   c,length=struct.unpack_from('<HB',data,offset);offset+=3
   if c<=previous or c>1034 or not 1<=length<=87:raise ValueError('actual remainder polynomial')
   previous=c
   for d in range(length):
    value=data[offset];offset+=1
    if value>30 or (value and c in heads and d>=heads[c]):raise ValueError('nonstandard remainder coordinate')
    if value:
     if (c,d) in index:V[index[c,d]][j]=value
     else:high[j].append([c,d,value])
 if offset!=len(data):raise ValueError('trailing complete remainder')
 beta_meta=json.loads((a.complete_beta_results/'complete-polynomial-bockstein-image-result.json').read_text())
 if beta_meta.get('status')!='completed' or beta_meta.get('allOriginalPolynomialKernelRowsAccountedFor')!=1834 or beta_meta.get('wholePolynomialBocksteinImageDimension')!=2 or not beta_meta.get('full315JInvarianceVerified'):raise ValueError('complete existing polynomial Bockstein image')
 data=actual(a.complete_beta_results/'complete-polynomial-bockstein-image.bin.gz',SYSTEM)
 if data[:8]!=b'R150FB31' or struct.unpack_from('<7I',data,8)!=(31,315,4,2,9,202,6):raise ValueError('complete actual Bockstein system')
 offset=36;labels=[]
 for _ in range(4):labels.append(list(struct.unpack_from('<IHHII',data,offset)));offset+=16
 descriptors=[]
 for _ in range(2):descriptors.append(list(struct.unpack_from('<4H',data,offset)));offset+=8
 if descriptors!=[[199,2275,0,85],[200,2276,0,85]]:raise ValueError('actual Bockstein image basis source')
 matrices=[]
 for nr,nc in [(315,4),(315,2),(315,9),(2,9),(2,2)]:
  matrices.append(nmod_mat([[data[offset+i*nc+j] for j in range(nc)] for i in range(nr)],31));offset+=nr*nc
 B,W,oldR,oldC,action=matrices;offset+=9
 if offset!=len(data) or W.rank()!=2:raise ValueError('complete Bockstein system length and rank')
 J=nmod_mat(state['matrices']['action'],31);K=nmod_mat(state['matrices']['kernelTranspose'],31).transpose();observation=nmod_mat(state['observabilityEchelon'],31)
 if J*W!=W*action or nmod_mat([rows(W)[i]+rows(B)[i] for i in range(315)],31).rank()!=2:raise ValueError('whole existing polynomial beta image')
 free=[i for i in range(820) if i+1 not in set(state['pivotStateCoordinates'])]
 VV=nmod_mat(V,31);R=nmod_mat([[V[i][j] for j in range(9)] for i in free],31);observed=observation*VV;represented=K*R
 in_torsion=[not high[j] and all(not int(observed[i,j]) for i in range(observed.nrows())) and all(int(represented[i,j])==V[i][j] for i in range(820)) for j in range(9)]
 E,rank=W.transpose().rref();eps=pivots(E,rank);Erows=rows(E);others=[i for i in range(315) if i not in set(eps)]
 def project(M):
  z=rows(M)
  for j in range(M.ncols()):
   for k,p in enumerate(eps):
    v=z[p][j]
    if v:
     for i in others:z[i][j]=(z[i][j]-v*Erows[k][i])%31
   for p in eps:z[p][j]=0
  return nmod_mat(z,31)
 projected=project(R);square=nmod_mat([[int(W[p,j]) for j in range(2)] for p in eps],31)
 coefficients=square.inv()*nmod_mat([[int(R[p,j]) for j in range(9)] for p in eps],31)
 compatible=[in_torsion[j] and all(not int(projected[i,j]) for i in range(315)) for j in range(9)]
 duals=[]
 for j,good in enumerate(compatible):
  if good:
   if any(int((W*coefficients)[i,j])!=int(R[i,j]) for i in range(315)):raise ValueError('full315 original beta solution')
   continue
  if high[j]:
   c,d,v=high[j][0];duals.append({'target':j+2,'kind':'higher-free-normal-coordinate','coordinates':[{'normalFormComponent':c,'parameterExponent':d,'weight':pow(v,-1,31)}],'annihilatesWholePolynomialBocksteinImage':True,'rightHandSide':1});continue
  if not in_torsion[j]:
   r=next(i for i in range(observed.nrows()) if int(observed[i,j]));scale=pow(int(observed[r,j]),-1,31)
   coeff=[int(observation[r,i])*scale%31 for i in range(820)]
   if any(sum(coeff[i]*int((K*W)[i,k]) for i in range(820))%31 for k in range(2)) or sum(coeff[i]*V[i][j] for i in range(820))%31!=1:raise ValueError('actual free-quotient dual')
   duals.append({'target':j+2,'kind':'full-state-observation','coordinates':[{'normalFormComponent':coordinates[i][0],'parameterExponent':coordinates[i][1],'weight':v} for i,v in enumerate(coeff) if v],'annihilatesWholePolynomialBocksteinImage':True,'rightHandSide':1});continue
  f=next(i for i in others if int(projected[i,j]));scale=pow(int(projected[f,j]),-1,31);weights={f:scale}
  for k,p in enumerate(eps):
   v=(-scale*Erows[k][f])%31
   if v:weights[p]=v
  if any(sum(v*int(W[i,k]) for i,v in weights.items())%31 for k in range(2)) or sum(v*int(R[i,j]) for i,v in weights.items())%31!=1:raise ValueError('full original beta-dual identity')
  duals.append({'target':j+2,'kind':'torsion-modulo-full-beta-image','coordinates':[{'torsionCoordinate':i+1,'stateCoordinate':free[i]+1,'normalFormComponent':coordinates[free[i]][0],'parameterExponent':coordinates[free[i]][1],'weight':v} for i,v in sorted(weights.items())],'annihilatesWholePolynomialBocksteinImage':True,'rightHandSide':1})
 minima=[];common=nmod_poly([1],31)
 if all(in_torsion):
  powers=[];current=projected
  for k in range(316):
   powers.append(rows(current))
   if k<315:current=project(J*current)
  for j in range(9):
   M=nmod_mat([[powers[k][i][j] for k in range(316)] for i in range(315)],31);red,r=M.rref()
   if pivots(red,r)!=list(range(r)):raise ValueError('initial quotient Krylov independence')
   co=[(-int(red[i,r]))%31 for i in range(r)]+[1]
   if not zero(M*nmod_mat([[v] for v in co+[0]*(316-len(co))],31)):raise ValueError('complete quotient recurrence')
   poly=nmod_poly(co,31);common=(common*poly)//common.gcd(poly)
   minima.append({'target':j+2,'degree':r,'coefficientsAscending':co,**helper.factored(poly),'full315QuotientRelationVerified':True})
  common_result={'degree':len(common)-1,'coefficientsAscending':[int(x) for x in common],**helper.factored(common)}
 else:common_result=None
 for j,good in enumerate(compatible):
  if not good:
   for i in range(2):coefficients[i,j]=0
 packed=bytearray(b'R150R231')+struct.pack('<5I',31,820,315,2,9)
 for M in (VV,R,W,coefficients,projected):packed.extend(bytes(v for row in rows(M) for v in row))
 packed.extend(bytes(in_torsion));packed.extend(bytes(compatible));file=a.out/'second-residual-full-beta-system.bin.gz';file.write_bytes(gzip.compress(packed,mtime=0))
 result={'format':'r150-h25-second-residual-full-first-beta-test-v1','status':'completed','prime':31,'originalTargetMultiplier':'H0=(s-2)*h0','sourceSHA256':sha(Path(__file__).read_bytes()),'stateSHA256':STATE,'completeFirstBetaSystemSHA256':SYSTEM,'originalSecondResidualMetadataSHA256':sha(a.original_metadata.read_bytes()),'actualRemainderSHA256':sha(a.image_remainders.read_bytes()),'allOriginalNormalCoordinatesRetained':True,'sameCompleteStandardDictionary':True,'residualsInTorsion':in_torsion,'higherFreeNormalCoordinates':high,'completeFirstBocksteinImageDimension':2,'full315JInvarianceVerified':True,'sameMod31InitialSourceLiftCompatibility':compatible,'kernelBasisDescriptors':descriptors,'kernelImageBasisCoefficients':rows(coefficients),'dualCertificates':duals,'minimumPolynomialsModuloFullFirstBetaImage':minima,'commonMinimumModuloFullFirstBetaImage':common_result,'finite_budget_verified':False,'allMod961KernelFreedomIncluded':False,'characteristicZeroIdentityAsserted':False,'system':{'file':str(file),'bytes':len(packed),'sha256':sha(packed),'gzipBytes':file.stat().st_size,'gzipSHA256':sha(file.read_bytes())},'pythonFlintVersion':flint.__version__,'flintVersion':flint.__FLINT_VERSION__,'elapsedSeconds':time.monotonic()-start,'scope':'The actual second residual is tested against the COMPLETE first Bockstein image. This is the affine necessary-and-sufficient class condition for a polynomial original-source lift modulo29791 with the CURRENT source fixed modulo31: Y=X+31*kappa_hat+961*z. A positive result still requires an actual finite-cost source. A failure does not exclude changing the original mod31 kernel part, all kernels modulo961, or a Q-source with31 denominators.'}
 (a.out/'second-residual-full-beta-result.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':'h25-second-residual-torsion-and-beta-test-complete','allOriginalNormalCoordinatesRetained':True,'residualsInTorsion':in_torsion,'sameMod31InitialSourceLiftCompatibility':compatible,'commonMinimumModuloFullFirstBetaImage':common_result,'allMod961KernelFreedomIncluded':False,'finite_budget_verified':False,'elapsedSeconds':result['elapsedSeconds']}),flush=True)

if __name__=='__main__':main()
