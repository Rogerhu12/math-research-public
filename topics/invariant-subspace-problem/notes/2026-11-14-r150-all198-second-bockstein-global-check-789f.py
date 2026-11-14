#!/usr/bin/env python3
"""Reconcile actual selected global sources with the complete315 torsion class.

Canonical source reduction may change a jet solution by the genuine first
Bockstein image. This script pays that difference from actual global remainders.
"""
import argparse,gzip,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat
STATE='06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf'
READER='8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2'
SECOND='fa9fda1c0176cbf3e8163fcfd26ed11ea4f92947587d3d455859d2b912cb38a4'
FOUR='f1f6594b19e844dbc8e387cc7efb822d582b26b9348fb8ab03996e985f94188b'
def sha(b):return hashlib.sha256(b).hexdigest()
def actual(p,expected):
 b=p.read_bytes();b=gzip.decompress(b) if p.suffix=='.gz' else b
 if sha(b)!=expected:raise ValueError('actual input SHA '+str(p))
 return b
def matrix(b,o,n,m):return nmod_mat([[b[o+i*m+j] for j in range(m)] for i in range(n)],31)
def serial(M):return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def polyprod(a,b):
 c=[0]*(len(a)+len(b)-1) if a and b else []
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%31
 while c and not c[-1]:c.pop()
 return c
def main():
 p=argparse.ArgumentParser()
 for k in ('notes-root','second-system','four-system','primary-result','original-metadata','image-metadata','image-remainders','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();started=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 local=json.loads(a.primary_result.read_text());original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if not local.get('allNinePrimaryCompatible') or not local.get('all202HighKernelDirectionsCovered'):raise ValueError('complete positive primary source polynomials required')
 if original.get('status')!='completed' or original.get('targetCount')!=9 or original.get('divisor')!=961 or original.get('targetMode')!=0 or not original.get('allOriginalProductCoefficientsDivisible') or not original.get('originalRowScaleTransportVerified'):raise ValueError('actual nine original17 selected delta sources')
 if image.get('status')!='completed' or not image.get('fullImageQuotientIdentity') or not image.get('everyRemainderIsIrreducible'):raise ValueError('actual global selected delta remainder identity')
 reader=a.notes_root/'2026-11-14-r150-torsion-characteristic-789f.py';actual(reader,READER)
 spec=importlib.util.spec_from_file_location('r150_actual_selected_state',reader);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 temp=a.out/'state-input.bin';temp.write_bytes(actual(a.notes_root/'2026-11-14-r150-torsion-state.bin-789f.gz',STATE));state=helper.load_state(temp);temp.unlink()
 b=a.image_remainders.read_bytes();wide=b[:8]==b'R150NX31'
 if (not wide and b[:8]!=b'R150NF31') or struct.unpack_from('<3I',b,8)!=(0,9,1034):raise ValueError('actual nine complete G remainders')
 coord=state['coordinates'];index={tuple(c):i for i,c in enumerate(coord)};V=nmod_mat(820,9,31);o=20
 for j in range(9):
  raw,label,n=struct.unpack_from('<IHI',b,o);o+=10
  if raw or label!=j+2:raise ValueError('actual nine global source labels')
  previous=0
  for k in range(n):
   c=struct.unpack_from('<H',b,o)[0];o+=2;nbytes=2 if wide else 1;length=int.from_bytes(b[o:o+nbytes],'little');o+=nbytes
   if c<=previous or c>1034 or length<1:raise ValueError('actual selected remainder dictionary')
   previous=c
   for d in range(length):
    v=b[o];o+=1
    if v>30:raise ValueError('remainder field')
    if v:
     if (c,d) not in index:raise ValueError('actual selected global delta has a high free term')
     V[index[c,d],j]=v
 if o!=len(b):raise ValueError('complete global remainder tail')
 free=[i for i in range(820) if i+1 not in set(state['pivotStateCoordinates'])]
 D=nmod_mat([[int(V[i,j]) for j in range(9)] for i in free],31)
 K=nmod_mat(state['matrices']['kernelTranspose'],31).transpose();O=nmod_mat(state['observabilityEchelon'],31);J=nmod_mat(state['matrices']['action'],31)
 if K*D!=V or O*V!=nmod_mat(505,9,31):raise ValueError('all505 global free observations must vanish')
 sec=actual(a.second_system,SECOND);R=matrix(sec,28+820*9,315,9);W=matrix(sec,28+820*9+315*9,315,2)
 four=actual(a.four_system,FOUR);old=matrix(four,28+6*4,315,4)
 if W!=matrix(four,28+6*4+315*4,315,2):raise ValueError('same whole first beta image')
 polys=local['solutionPolynomialsAscending'];oldpolys=polys[198:202];oldcomb=nmod_mat(315,9,31)
 for i in range(4):
  current=nmod_mat([[int(old[k,i])] for k in range(315)],31)
  for e in range(max([len(c) for c in oldpolys[i]]+[0])):
   oldcomb+=current*nmod_mat([[c[e] if e<len(c) else 0 for c in oldpolys[i]]],31);current=J*current
 projector=local['globalProjectorAscending'];Id=nmod_mat([[int(i==j) for j in range(315)] for i in range(315)],31);PJ=nmod_mat(315,315,31)
 for c in reversed(projector):PJ=PJ*J+c*Id
 if PJ*PJ!=PJ or PJ*R!=R or PJ*W!=W or PJ.rank()!=39:raise ValueError('actual full315 global primary projector')
 projected=PJ*(D+oldcomb);diff=R-projected
 rr,rank=W.transpose().rref();piv=[next(c for c in range(315) if rr[i,c]) for i in range(rank)]
 if rank!=2:raise ValueError('whole first beta rank')
 inverse=nmod_mat([[int(W[i,j]) for j in range(2)] for i in piv],31).inv()
 F=inverse*nmod_mat([[int(diff[i,j]) for j in range(9)] for i in piv],31)
 residual=diff-W*F
 packed=bytearray(b'R150GP31')+struct.pack('<4I',31,315,9,2)
 for mat in (D,R,oldcomb,projected,W,F,residual):packed.extend(serial(mat))
 out=a.out/'selected-global315-reconciliation.bin.gz';out.write_bytes(gzip.compress(packed,mtime=0))
 if residual!=nmod_mat(315,9,31):
  (a.out/'selected-global315-failure.json').write_text(json.dumps({'status':'failed','reason':'actual selected global sources differ outside complete first image','systemSHA256':sha(packed)},indent=2)+'\n')
  raise ValueError('actual global source projection mismatch; no original17 final claim')
 beta=[[[int(F[i,j])] if F[i,j] else [] for j in range(9)] for i in range(2)]+[[[] for j in range(9)] for _ in range(2)]
 old_projected=[[polyprod(projector,c) for c in row] for row in oldpolys]
 bound=max([86,original['provedSourceCostBound']+len(projector)-1]+[87+len(c)-1 for row in old_projected for c in row if c])
 if bound>373:raise ValueError('explicit selected/projector budget373 exceeded')
 result={'format':'r150-actual-selected-global315-second-source-reconciliation-v1','status':'completed',
 'sourceSHA256':sha(Path(__file__).read_bytes()),'actualNineRemaindersSHA256':sha(b),'actualOriginalMetadataSHA256':sha(a.original_metadata.read_bytes()),
 'all820GlobalCoordinatesRetained':True,'all505GlobalObservationsVerified':True,'allNineActualGlobalDeltaClassesInTorsion':True,
 'sameRank39GlobalPrimaryProjectionVerified':True,'full315ProjectedDifferenceInCompleteFirstImage':True,
 'firstBetaCorrectionPolynomialsAscending':beta,'oldFourProjectedPolynomialsAscending':old_projected,
 'selectedNineGlobalProjectorAscending':projector,'actualSelectedSourceCosts':original['actualSourceCosts'],
 'finalRHSCostBound':bound,'finalTemporarySourceCostBound':bound+96,
 'actualStandardSourceKernelChangePaidByWholeFirstImage':True,
 'fullOriginalMod29791IdentityVerified':False,'finite_budget_verified':False,
 'system':{'file':out.name,'bytes':len(packed),'sha256':sha(packed),'gzipBytes':out.stat().st_size,'gzipSHA256':sha(out.read_bytes())},
 'elapsedSeconds':time.monotonic()-started}
 (a.out/'selected-global315-result.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('status','all505GlobalObservationsVerified','full315ProjectedDifferenceInCompleteFirstImage','finalRHSCostBound','finalTemporarySourceCostBound','elapsedSeconds')}),flush=True)
if __name__=='__main__':main()
