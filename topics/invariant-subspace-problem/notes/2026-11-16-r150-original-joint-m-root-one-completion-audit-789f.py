#!/usr/bin/env python3
"""Read-only audit of the completed original root-one two-digit computation.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
No source reconstruction or original linear solve is repeated. Mathematical
arrays remain in the temporary completed computation, never in this source.
"""
import argparse, hashlib, json, math, time
from pathlib import Path
from flint import nmod_mat

RECEIPT=(13523,'342f10fce9639bf879e86eb60eea307afa960062ffff28b39315e3892eebbe78')
QUALIFICATION=(2112889,'a7a21b4c00e306ee0278451217491aedf88c6bcb59c3ca23668198516a74a29d')
BINDING='c7a18e56374d223e1653fd48561d5f5c7dd4d2548e77486bdb4cbd9cf5ffe3df'
def canonical(x):
 return (json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')
def identity(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return {'bytes':p.stat().st_size,'sha256':h.hexdigest()}
def require(c,m):
 if not c:raise ValueError(m)
def pin(p,s):
 q=identity(p);require(q=={'bytes':s[0],'sha256':s[1]},'exact input '+str(p));return q
def sub(A,cols):return nmod_mat([[int(A[i,j]) for j in cols] for i in range(A.nrows())],31)
def joined(*blocks):return nmod_mat([[int(A[i,j]) for A in blocks for j in range(A.ncols())] for i in range(blocks[0].nrows())],31)
def record(A):return {'rows':A.nrows(),'columns':A.ncols(),'sha256':hashlib.sha256(bytes(int(A[i,j]) for i in range(A.nrows()) for j in range(A.ncols()))).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--completed-dir',type=Path,required=True);ap.add_argument('--qualification-data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.monotonic()
 rp=a.completed_dir/'original-joint-m-root-one-complete-two-digits-receipt.json'
 rid=pin(rp,RECEIPT);qid=pin(a.qualification_data,QUALIFICATION)
 r=json.loads(rp.read_bytes());q=json.loads(a.qualification_data.read_bytes());p=r['parameters']
 require(r['status']=='completed' and r['binding']==BINDING,'actual completed identity')
 require(hashlib.sha256(canonical(p['inputIdentity'])).hexdigest()==BINDING,'entire canonical input binding')
 require(len(p['stages'])==11,'all eleven actual stages')
 outputs=0;unique={};stages=[]
 for name,s in sorted(p['stages'].items()):
  require(s['status']=='completed' and s['exitCode']==0,'actual completed stage '+name)
  d=json.loads((a.completed_dir/'stage-cache'/(name+'.json')).read_bytes())
  c=json.loads((a.completed_dir/'stage-cache'/(name+'.context.json')).read_bytes())
  require(d['inputBinding']==c['inputBinding']==s['inputBinding'],'same stage input binding '+name)
  require(d['statistics']==s['statistics'],'same complete stage statistics '+name)
  for rel,pin0 in d['outputs'].items():
   out=(a.completed_dir/rel).resolve();require(out.is_relative_to(a.completed_dir.resolve()),'only same temporary completion outputs')
   got=identity(out);require(got==pin0,'complete output hash '+rel);unique[rel]=got;outputs+=1
  require(identity(a.completed_dir/'logs'/(name+'.log'))==s['log'],'actual complete stage log '+name)
  stages.append({'name':name,'inputBinding':s['inputBinding'],'outputCount':len(d['outputs'])})
 primary=[z for z in q['primaryMatrices'] if z['factor']==[30,1]]
 require(len(primary)==1,'same entire original root-one primary')
 U=nmod_mat(primary[0]['originalTorsion'],31);X=nmod_mat(primary[0]['originalTargets'],31);J16=nmod_mat(q['true16Action'],31)
 basis=joined(sub(U,[0,2]),sub(X,[0]));require(basis.rank()==3,'primitive free line and both true coefficient directions')
 require(record(basis)==p['coordinateChecks']['root-one-initial-coordinate']['basis'],'same original315 basis')
 for name,cl in [('root-one-initial-coordinate','root-one-initial-complete315'),('root-one-next-coordinate','root-one-next-complete315')]:
  c=json.loads((a.completed_dir/(name+'-coordinates.json')).read_bytes());d=json.loads((a.completed_dir/'stages'/cl/'complete315-class.json').read_bytes())
  require(c['binding']==d['binding']==BINDING,'same true coordinate pipeline')
  C=nmod_mat(c['coordinates'],31);D=nmod_mat(d['matrixRows'],31)
  require(basis*C==D,'all315 coordinate products '+name)
  require(record(C)==p['coordinateChecks'][name]['coordinates'] and record(D)==p['classes'][cl]['matrix'],'exact coordinate and class logical identities')
 zero=json.loads((a.completed_dir/'stages'/'root-one-corrected-zero315'/'complete315-class.json').read_bytes())
 require(all(z==0 for row in zero['matrixRows'] for z in row),'all315 free-corrected field classes are zero')
 datafile=a.completed_dir/'root-one-complete-two-digit-coordinates.json';did=identity(datafile)
 require(did=={k:v for k,v in p['final']['temporaryCompleteDataFile'].items() if k!='file'},'complete actual coordinate file')
 d=json.loads(datafile.read_bytes());require(d['binding']==BINDING and d['ambientExponents']==[1,2] and d['basisOriginalTrue16Indices']==[0,2],'true root-one coordinate frame')
 c0=json.loads((a.completed_dir/'root-one-initial-coordinate-coordinates.json').read_bytes())['coordinates'];c1=json.loads((a.completed_dir/'root-one-next-coordinate-coordinates.json').read_bytes())['coordinates']
 require(all(z==0 for row in c0[:2] for z in row),'initial exact torsion residue zero')
 A=[[31*c1[i][j]%(31**e) for j in range(8)] for i,e in enumerate([1,2])]
 require(A==d['coordinateRows'],'exact second-digit to true socle conversion')
 require(all(z==0 for z in A[0]) and math.gcd(31**2,*A[1])==31,'independent integer gcd proves the image is precisely D/(31)')
 require(d['freeCoefficientsModuloP2']==[(c0[2][j]+31*c1[2][j])%961 for j in range(8)],'both free digits retained')
 s2=sub(U*J16,[2])-sub(U,[2]);require(joined(sub(U,[0]),s2).rank()==1,'parameter s is one on the actual remaining p-socle')
 require(d['freeTailNotSetToZero'] and p['final']['higherFreeTailRetained'],'no uncomputed free tail set to zero')
 result={'format':'r150-root-one-readonly-completion-audit-v1','status':'completed','source':identity(Path(__file__)),'inputs':{'receipt':rid,'qualificationData':qid},'parentBinding':BINDING,'completeData':did,'actualCompletedStages':len(stages),'stageOutputHashChecks':outputs,'distinctOutputFiles':len(unique),'allCanonicalAndStageBindingsVerified':True,'all315CoordinateProductsVerified':True,'all315CorrectedClassesZero':True,'socleImageVerifiedByIntegerGCD':True,'parameterSActsAsOneOnSocle':True,'rootOneDExponents':[1],'rootOneLength':1,'higherFreeTailRetained':True,'originalSolveRepeated':False,'mathematicalArraysStoredInRepository':False,'elapsedSeconds':time.monotonic()-start}
 a.out.write_bytes(canonical(result));print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
