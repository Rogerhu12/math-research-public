#!/usr/bin/env python3
"""Read the completed first-beta module and derive its exact polynomial kernel.

Only the already saved small complete matrices are used.  No original kernel,
Bockstein, NF or VQ source is recomputed or claimed lifted to the next modulus.
"""
import argparse,gzip,hashlib,importlib.util,json,struct,time
from pathlib import Path
from flint import nmod_mat

FIRST='71b3ffd524cca40f36ac59fb29694798013987c6153edb0c771420d75780daf8'
SECOND='fa9fda1c0176cbf3e8163fcfd26ed11ea4f92947587d3d455859d2b912cb38a4'
STATE='06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
READER='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def zero(M):return not any(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def actual(p,expected):
 b=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
 if hashlib.sha256(b).hexdigest()!=expected:raise ValueError('actual complete small-matrix checksum')
 return b

def main():
 p=argparse.ArgumentParser()
 for k in ('complete-beta-results','second-results','notes-root','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 first=actual(a.complete_beta_results/'complete-polynomial-bockstein-image.bin.gz',FIRST)
 if first[:8]!=b'R150FB31' or struct.unpack_from('<7I',first,8)!=(31,315,4,2,9,202,6):raise ValueError('complete first-beta dimensions')
 o=36;labels=[]
 for _ in range(4):labels.append(list(struct.unpack_from('<IHHII',first,o)));o+=16
 descriptors=[]
 for _ in range(2):descriptors.append(list(struct.unpack_from('<4H',first,o)));o+=8
 if descriptors!=[[199,2275,0,85],[200,2276,0,85]]:raise ValueError('actual first-beta basis')
 matrices=[]
 for nr,nc in [(315,4),(315,2),(315,9),(2,9),(2,2)]:
  matrices.append(nmod_mat([[first[o+i*nc+j] for j in range(nc)] for i in range(nr)],31));o+=nr*nc
 B,W,oldR,oldC,L=matrices
 if o+9!=len(first) or W.rank()!=2:raise ValueError('complete first-beta matrix length')
 red,rank=W.transpose().rref();piv=[next(j for j in range(315) if int(red[i,j])) for i in range(rank)]
 square=nmod_mat([[int(W[i,j]) for j in range(2)] for i in piv],31)
 coordinates=square.inv()*nmod_mat([[int(B[i,j]) for j in range(4)] for i in piv],31)
 if W*coordinates!=B:raise ValueError('actual full315 four-column identity')
 aa,cc=int(L[0,0]),int(L[1,0]);ci=pow(cc,-1,31)
 rho=[-aa*ci%31,ci]
 polynomials=[[(int(coordinates[0,j])+int(coordinates[1,j])*rho[0])%31,int(coordinates[1,j])*rho[1]%31] for j in range(4)]
 e0=nmod_mat([[1],[0]],31)
 for j,(constant,linear) in enumerate(polynomials):
  if (e0*constant+L*e0*linear)!=nmod_mat([[int(coordinates[i,j])] for i in range(2)],31):raise ValueError('exact scalar polynomial relation')
 if not zero(L*L-L*3+nmod_mat([[2,0],[0,2]],31)) or nmod_mat([[1,int(L[0,0])],[0,int(L[1,0])]],31).rank()!=2:raise ValueError('cyclic generator exact minimum ell')
 hp=a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py'
 if hashlib.sha256(hp.read_bytes()).hexdigest()!=READER:raise ValueError('state reader checksum')
 spec=importlib.util.spec_from_file_location('actual_r150_state_for_kernel',hp);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 sf=a.out/'state-input.bin';sf.write_bytes(actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE));state=helper.load_state(sf);J=nmod_mat(state['matrices']['action'],31)
 if J*W!=W*L:raise ValueError('same actual full315 action')
 second=actual(a.second_results/'second-residual-full-beta-system.bin.gz',SECOND)
 if second[:8]!=b'R150R231' or struct.unpack_from('<5I',second,8)!=(31,820,315,2,9):raise ValueError('actual second residual system')
 o=28+820*9+315*9
 W2=nmod_mat([[second[o+i*2+j] for j in range(2)] for i in range(315)],31);o+=630+18
 R=nmod_mat([[second[o+i*9+j] for j in range(9)] for i in range(315)],31)
 if W2!=W:raise ValueError('same Bockstein quotient section')
 E=rows(red);other=[i for i in range(315) if i not in set(piv)]
 def project(M):
  z=rows(M)
  for j in range(M.ncols()):
   for k,pivot in enumerate(piv):
    v=z[pivot][j]
    for i in other:z[i][j]=(z[i][j]-v*E[k][i])%31
   for pivot in piv:z[pivot][j]=0
  return nmod_mat(z,31)
 JR=project(J*R);primary1=R*2-JR;primary2=JR-R
 if not zero(project(J*primary1)-primary1) or not zero(project(J*primary2)-primary2*2) or primary1+primary2!=R:raise ValueError('complete second-residual primary decomposition')
 data={'format':'r150-exact-first-beta-kernel-module-v1','status':'completed','field':31,'sourceSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'firstCompleteBetaSystemSHA256':FIRST,'secondResidualSystemSHA256':SECOND,'stateSHA256':STATE,'actualHighLabels':labels,'actualRestrictedAction':rows(L),'actualFourColumnBasisCoordinates':rows(coordinates),'fourPolynomialsOverFirstGeneratorAscending':polynomials,'firstGeneratorMinimumPolynomialAscending':[2,28,1],'full315PolynomialRelationsVerified':True,'old198ZeroImageDirectionsRetained':True,'fullHighKernelBasisCount':202,'newFourSourceCostUpperBounds':[86,86,86,87],'newWeightedBasisMinimalityAsserted':False,'originalSecondBocksteinColumnsComputed':False,'secondResidualQuotientPrimaryDimensions':{'sMinus1':primary1.rank(),'sMinus2':primary2.rank(),'wholeGeneratedModule':nmod_mat([rows(primary1)[i]+rows(primary2)[i] for i in range(315)],31).rank()},'elapsedSeconds':time.monotonic()-start}
 (a.out/'kernel-basis-and-second-primary-receipt.json').write_text(json.dumps(data,indent=2)+'\n');sf.unlink();print(json.dumps(data),flush=True)

if __name__=='__main__':main()
