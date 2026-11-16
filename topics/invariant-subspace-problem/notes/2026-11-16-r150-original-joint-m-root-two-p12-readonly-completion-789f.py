#!/usr/bin/env python3
"""Complete only the small postprocessing of the actual42-stage p12 run.
Author: ChatGPT (AI), literature_audit. Date:2026-11-16.
The original failed receipt is immutable. No original source solve is repeated.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,time,sys
sys.dont_write_bytecode=True
DRIVER='2026-11-16-r150-original-joint-m-root-two-complete-p12-789f.py'
DRIVER_PIN=(41088,'d43f2b3af1f629d0ee0fb880a51ea1667f30a2b0f2079793537644aa71a210a8')
PARENT_PIN=(37792,'e6867a8f20e37f90aeaa08b8df44ead2fdac73475a6725a5114285609142afc2')
COORD_PIN=(9046,'c31f78775508475bc62e8c772309b006356593a0547307f8cb9bc83fc66bc8ca')
PARENT_BINDING='38139cd17a0a87190fc7302d7f9a271cd6370e379090de91ed9706eb3fa673e9'
EXPECTED_ERROR='independent complete original joint-B type and parameter images are reproduced from the new raw targets'
def check(ok,text):
 if not ok:raise ValueError(text)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def identity(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return {'bytes':p.stat().st_size,'sha256':h.hexdigest()}
def pinned(p,pin):
 z=identity(p);check(z==dict(zip(('bytes','sha256'),pin)),'exact paid input '+str(p));return z
def atomic_json(p,x):
 q=p.with_name(p.name+'.tmp');q.write_bytes(canonical(x));q.replace(p)
def product(A,B):
 C=[0]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):C[i+j]+=x*y
 return C
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--notes-root',type=Path,required=True);ap.add_argument('--parent-out',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 rec={'format':'r150-original-joint-m-root-two-p12-readonly-completion-v1','status':'running','parameters':{}}
 rp=a.out/'original-joint-m-root-two-p12-readonly-completion-receipt.json'
 try:
  path=a.notes_root/DRIVER;source_identity=pinned(path,DRIVER_PIN)
  spec=importlib.util.spec_from_file_location('r150_paid_p12_math',path);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
  parent_path=a.parent_out/'original-joint-m-root-two-complete-p12-receipt.json';parent_identity=pinned(parent_path,PARENT_PIN);old=json.loads(parent_path.read_bytes())
  check(old['status']=='failed' and old['binding']==PARENT_BINDING and old['errorType']=='ValueError' and old['error']==EXPECTED_ERROR,'exact failed terminal crosscheck and untouched source binding')
  check(old['parameters']['inputIdentity']['driver']==source_identity,'actual parent source identity')
  stage=old['parameters']['stages'];check(len(stage)==42 and all(v['status']=='completed' and v['exitCode']==0 for v in stage.values()),'all42 original mathematical stages actually completed')
  stage_identities={};output_count=0
  for name,record in stage.items():
   cp=a.parent_out/'stage-cache'/(name+'.json');c=json.loads(cp.read_bytes());check(c['inputBinding']==record['inputBinding'],'same original stage input binding '+name)
   for relative,expected in c['outputs'].items():
    target=(a.parent_out/relative).resolve();check(target.is_relative_to(a.parent_out.resolve()),'stage output stays within actual parent');check(identity(target)==expected,'complete original stage output hash '+name+'/'+relative);output_count+=1
   stage_identities[name]=identity(cp)
  coord_path=a.parent_out/'root-two-complete-six-digit-coordinates.json';coord_identity=pinned(coord_path,COORD_PIN);d=json.loads(coord_path.read_bytes())
  check(d['binding']==PARENT_BINDING and d['rootTwoCompletionOnly'] and d['freeRemainderNotSetToZero'],'complete six-digit scope and retained free tail')
  E=d['ambientExponents'];A=d['coordinateRows'];beta=d['betaModuloP6'];free_coefficients=d['freeCoefficientsModuloP6'];mod=31**6;nt=26
  check(E==[1,2,2,2,2,3,3,4,4,4,4,5,5,6] and len(A)==14 and all(len(row)==26 for row in A),'all14 true torsion basis directions and26 original generators')
  from flint import nmod_mat
  for k in range(6):
   C=json.loads((a.parent_out/('digit%d-complete-line-coordinates-coordinates.json'%k)).read_bytes())
   check(C['binding']==PARENT_BINDING and C['coordinates']==d['torsionDigits'][k]+[d['freeDigits'][k]],'all six actual complete315 coordinate digits')
  check(A==[[sum(31**k*d['torsionDigits'][k][i][j] for k in range(6))%(31**e) for j in range(nt)] for i,e in enumerate(E)],'complete true torsion coordinates from all actual six digits')
  check(free_coefficients==[sum(31**k*d['freeDigits'][k][j] for k in range(6))%mod for j in range(nt)],'all six retained original free digits')
  check(p.integer_record(A)==old['parameters']['completeCoordinates']['matrix'],'same original26 coordinate logical identity')
  fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
  hs=product([0,0,0,1],product(product(fp,fp),product(product(fm,fm),e8)))
  ht=[sum(hs[d]*math.comb(d,k)*2**(d-k) for d in range(k,len(hs)))%mod for k in range(len(hs))]
  c0=[1]+free_coefficients[:8];c1=free_coefficients[8:17];c2=free_coefficients[17:26]
  check(beta%31==0 and c1==[beta*c%mod for c in c0] and c2==[beta*beta*c%mod for c in c0],'all nine original free-coordinate Hensel transports')
  check(sum(ht[k]*pow(beta,k,mod) for k in range(len(ht)))%mod==0 and ht[1]%31!=0,'same unique simple original hstar Hensel root')
  image=p.group_image(A,E)
  Z=[[31**(6-e)*x%mod for x in row] for e,row in zip(E,A)]
  sn=p.smith_mod(Z,6);r=len(sn['valuations']);relation_powers=[6-v for v in sn['valuations']]+[0]*(nt-r)
  Rels=[[sn['right'][i][j]*31**relation_powers[j] for j in range(nt)] for i in range(nt)]
  check(p.null_image(p.mm(A,Rels,mod),E) and sum(relation_powers)==image['length'],'complete unreduced true D relation lattice, including every p6 column')
  X=[[0]*nt for _ in range(nt)];u=[[int(i==8)] for i in range(nt)]
  for j in range(1,9):X[8+j][j-1]=1;X[8][j-1]=(X[8][j-1]-c0[j])%mod
  for j in range(9):
   X[17+j][8+j]=1;X[8][8+j]=(X[8][8+j]-beta*c0[j])%mod
   X[17+j][17+j]=beta;X[8][17+j]=(X[8][17+j]-beta*beta*c0[j])%mod
  check(p.null_image(p.mm(p.mm(A,X,mod),Rels,mod),E),'original x action preserves every actual D relation')
  X2=p.mm(X,X,mod);X3=p.mm(X2,X,mod)
  check(p.null_image(p.mm(A,p.add(X3,[[-beta*z%mod for z in row] for row in X2],mod),mod),E),'complete x squared times x minus beta identity')
  q=[0]*(len(ht)-1);q[-1]=ht[-1]
  for i in range(len(q)-2,-1,-1):q[i]=(ht[i+1]+beta*q[i+1])%mod
  check((ht[0]+beta*q[0])%mod==0,'same original synthetic hstar division')
  hX=p.matrix_poly(ht,X,mod);qX=p.matrix_poly(q,X,mod);bfree=p.mm(qX,u,mod)
  Bgen=[[(c0[j]*bfree[i][0]+(hX[i][j-1] if j else 0))%mod for j in range(9)] for i in range(nt)]
  Bcoords=p.reduce_rows(p.mm(A,Bgen,mod),E);BXcoords=p.reduce_rows(p.mm(p.mm(A,X,mod),Bgen,mod),E)
  # B is R-generated. Both its nine b columns and nine x*b columns are required.
  Bimage=p.group_image(p.joined(Bcoords,BXcoords),E);BX=p.group_image(BXcoords,E);BPX=p.group_image(p.scaled(BXcoords,31,E),E)
  check(Bimage['exponents']==[1,1,1,1,1,1,2,3,4,4,5] and Bimage['length']==24 and BX['exponents']==[1,1,1,2] and BPX['exponents']==[1],'complete independently paid R-generated B and both parameter images')
  check(p.null_image(p.mm(A,p.mm(X2,Bgen,mod),mod),E),'all original x squared hstar targets vanish')
  single=[]
  for j in range(9):
   single.append(p.group_image(p.joined([[row[j]] for row in Bcoords],[[row[j]] for row in BXcoords]),E)['exponents'])
  check(single==[[2,5]]*9,'all nine independently paid single-target cyclic modules')
  relf=nmod_mat([[x%31 for x in row] for row in Rels],31);xf=nmod_mat([[x%31 for x in row] for row in X],31);uf=nmod_mat(u,31)
  join=lambda *ms:nmod_mat([[int(z) for mat in ms for z in [mat[i,j] for j in range(mat.ncols())]] for i in range(ms[0].nrows())],31)
  s_min=nt-join(relf,xf).rank();m_min=1+nt-join(relf,xf,uf).rank()
  check(8<=m_min<=9,'original complete joint-M generator interval')
  sx=p.group_image(p.reduce_rows(p.mm(A,X,mod),E),E);px=p.group_image(p.scaled(p.reduce_rows(p.mm(A,X,mod),E),31,E),E)
  semantic={'source':identity(Path(__file__)),'parentSource':source_identity,'actualFailedParentReceipt':parent_identity,'parentBinding':PARENT_BINDING,'completeSixDigitCoordinates':coord_identity,'actualCompletedStageIdentities':stage_identities}
  binding=hashlib.sha256(canonical(semantic)).hexdigest();rec['binding']=binding;rec['parameters']['inputIdentity']=semantic
  data={'format':'r150-original-joint-m-root-two-complete-D-presentation-and-action-readonly-v1','binding':binding,'parentBinding':PARENT_BINDING,'ambientExponents':E,'basisOriginalTrue16Indices':d['basisOriginalTrue16Indices'],'original26TargetDefinitions':{'rawLabels':list(range(3,11)),'xLabels':list(range(2,11)),'xSquaredLabels':list(range(2,11))},'coordinateRows':A,'completeDRelationMatrix':Rels,'relationLatticeRightUnit':sn['right'],'relationPowers':relation_powers,'xActionOnOriginal26Generators':X,'xOfPrimitiveFreeGeneratorTorsionColumn':u,'betaModuloP6':beta,'freeActionIsExactSimpleHenselRootNotZeroPadded':True,'originalNineHstarCoordinates':Bcoords,'originalNineXHstarCoordinates':BXcoords,'freeCoefficientDigits':free_coefficients,'completeSmallSmithTransformation':sn}
  datafile=a.out/'root-two-complete-presentation-and-action.json';atomic_json(datafile,data)
  rec['parameters']['final']={'completeRootTwoCoefficientTorsion':image,'xImage':sx,'pxImage':px,'minimumRootTwoPolynomialGeneratorsOfTorsion':s_min,'minimumRootTwoPolynomialGeneratorsOfOriginalM':m_min,'minimumGlobalPolynomialGeneratorsOfOriginalM':m_min,'otherMaximalGeneratorCountsBoundedByThree':True,'fullGlobalCoefficientTorsionStillNeedsRootOneSocleCheck':True,'rootOneHiddenSocleNotDiscarded':True,'originalJointBReproduced':Bimage,'originalJointBXReproduced':BX,'originalJointBPXReproduced':BPX,'allNineSingleTargetCyclicTypes':single,'completeDRelations':p.integer_record(Rels),'originalXAction':p.integer_record(X),'allOriginalRelationProductsVerified':True,'allOriginalParameterTransportsVerified':True,'actualParentCompletedStageCount':42,'actualParentCompletedOutputIdentitiesVerified':output_count,'noOriginalProductOrSolveRepeated':True,'parentFailureRetainedWithoutMutation':True,'originalErrorWasMissingNineXColumnsInDSpanCrosscheck':True,'completeSixDigitCoordinates':old['parameters']['completeCoordinates'],'temporaryCompleteDataFile':{'file':datafile.name,**identity(datafile)},'noHighPActionInferredFromResidueJ16':True,'noParentAProductZeroPadding':True,'primitiveFreeTailNotSetToZero':True,'complete210NotRecomputed':True,'globalPolynomialSourceClaimed':False}
  rec['status']='completed';return 0
 except BaseException as exc:
  rec['status']='failed';rec['parameters']['error']={'type':type(exc).__name__,'message':str(exc)};return 1
 finally:
  rec['elapsedSeconds']=time.monotonic()-start;atomic_json(rp,rec);print(json.dumps(rec,sort_keys=True,separators=(',',':')),flush=True)
if __name__=='__main__':raise SystemExit(main())
