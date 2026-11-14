#!/usr/bin/env python3
"""Resume only the three unfinished projector-free stages; no mathematics on import."""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, os, shutil, struct, subprocess, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
CONTRACT = '2026-11-14-r150-projector-free-three-stage-resume-inputs-789f.json'
OLD_HELPER = '2026-11-14-r150-four-second-bockstein-runner-789f.py'
OLD_HELPER_SHA = '9fc1d9e6f64f520365bddea2d0d3387a32d42123f38efcf36f8798c9f36e6cba'
SOURCE_BINDING = 'dc5426e2614e00fd69bde3a56f560ee5a2f7962b86dc6fcf7135784c6a7a0bc5'
PROGRAMS = {
 'source9': '2026-11-14-r150-second-bockstein-source-checkpoint-789f.cpp',
 'transport': '2026-11-14-r150-second-bockstein-all198-global-original-transport-789f.cpp',
 'original': '2026-11-14-r150-second-bockstein-all198-global-original-combination-789f.cpp',
}
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''): h.update(block)
 return h.hexdigest()
def suffix(p,s): return Path(str(p)+s)
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 p=argparse.ArgumentParser()
 for name in ('original-out','notes-root','out'): p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--math-seconds',type=int,default=90);p.add_argument('--memory-mib',type=int,default=512)
 a=p.parse_args()
 if min(a.math_seconds,a.memory_mib)<1: raise ValueError('positive shared budget required')
 root=Path(__file__).resolve().parent;oldout=a.original_out.resolve();notes=a.notes_root.resolve();out=a.out.resolve()
 if out==oldout: raise ValueError('separate lossless continuation directory required')
 results=out/'results';recovery=out/'recovery';before=recovery/'before';continued=recovery/'continued'
 for d in (out,results,recovery): d.mkdir(parents=True,exist_ok=True)
 work=oldout/'recovery';cache=work/'stage-cache';cache.mkdir(exist_ok=True)
 receipt_path=results/'projector-free-three-stage-continuation-receipt.json'
 receipt={'format':'r150-projector-free-three-stage-continuation-v1','status':'preparing','sharedMathematicalSecondsLimit':a.math_seconds,
  'perChildAddressSpaceMiBLimit':a.memory_mib,'noRecompilation':True,'imageRecomputed':False,'preceding300SourceRowsRecomputed':False,
  'nativeInputBinding':SOURCE_BINDING,'fullOriginalMod29791IdentityVerified':False,'finite_budget_verified':False,
  'characteristicZeroIdentityAsserted':False,'deadlineRule':'Initial lossless snapshot and SHA verification precede one shared90-second mathematical clock. The three stages receive only its remaining time; timeout sends SIGTERM then permits up to10seconds for actual checkpoint serialization before SIGKILL. Compression and recovery copies follow outside that clock.',
  'sources':{},'executables':{},'stages':{}}
 def save(): receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
 started=None
 try:
  fixed=json.loads((root/CONTRACT).read_text());receipt['inputContractSHA256']=sha(root/CONTRACT)
  initial_receipt=oldout/'results/projector-free-second-lift-pipeline-receipt.json'
  if sha(initial_receipt)!=fixed['receiptSHA256']: raise ValueError('frozen initial interrupted receipt changed')
  initial=json.loads(initial_receipt.read_text())
  if not before.exists():
   for relative,item in fixed['initialRecovery'].items():
    f=work/relative
    if f.stat().st_size!=item['bytes'] or sha(f)!=item['sha256']: raise ValueError('initial recovery file changed '+relative)
   shutil.copytree(work,before/'recovery')
   (before/'results').mkdir()
   for f in sorted((oldout/'results').iterdir()):
    if f.is_file() and f.suffix in ('.json','.log'): shutil.copyfile(f,before/'results'/f.name)
  for relative,item in fixed['initialRecovery'].items():
   f=before/'recovery'/relative
   if f.stat().st_size!=item['bytes'] or sha(f)!=item['sha256']: raise ValueError('initial lossless snapshot mismatch '+relative)
  if sha(before/'results'/initial_receipt.name)!=fixed['receiptSHA256']: raise ValueError('initial receipt snapshot mismatch')
  receipt['initialSnapshot']={'recoveryFiles':len(fixed['initialRecovery']),'recoveryBytes':sum(f['bytes'] for f in fixed['initialRecovery'].values()),'allEightRecoveryFilesExact':True,'initialReceiptAndAllLogsSaved':True}
  found={}
  for name,item in initial['inputs'].items():
   f=Path(item['file'])
   if sha(f)!=item['sha256']: raise ValueError('actual input SHA '+name)
   found[name]=f
  for name,expected in initial['sources'].items():
   f=notes/name
   if sha(f)!=expected: raise ValueError('frozen source dependency '+name)
   receipt['sources'][name]=expected
  receipt['sources'][Path(__file__).name]=sha(Path(__file__));receipt['sources'][CONTRACT]=sha(root/CONTRACT)
  executables={}
  for name,expected in fixed['executables'].items():
   f=oldout/'bin'/name
   if sha(f)!=expected: raise ValueError('already compiled executable SHA '+name)
   executables[name]=f;receipt['executables'][name]={'file':str(f),'sha256':expected}
  helperfile=notes/OLD_HELPER
  if sha(helperfile)!=OLD_HELPER_SHA: raise ValueError('frozen recipe writer')
  spec=importlib.util.spec_from_file_location('r150_three_stage_lossless_recipe',helperfile);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
  image=work/'projector-free-image/projector-free-image';source=work/'projector-free-source/projector-free-source'
  source_args=[found['graph'],found['originalNF'],suffix(image,'-normal-forms.bin'),suffix(image,'-image-quotients.bin'),suffix(image,'-image-remainders.bin'),source,SOURCE_BINDING]
  if list(map(str,source_args))!=initial['stages']['source']['command'][8:]: raise ValueError('same exact native source argv required')
  checkpoint=suffix(source,'-vq-checkpoint.bin')
  with checkpoint.open('rb') as f: header=f.read(116)
  if header[:8]!=b'R150VQ31' or struct.unpack_from('<6I',header,8)!=(1,87,183,2195,9,1034) or header[52:116].decode()!=SOURCE_BINDING: raise ValueError('actual source checkpoint binding/dimensions')
  done=struct.unpack_from('<I',header,32)[0]
  if done<300 or done>1021: raise ValueError('actual source checkpoint continuation prefix')
  receipt['resumeSourceAtImageRowOneBased']=done+1
  proof=initial['projectorFreeSavedIdentity'];old_four=proof['oldFourPolynomialsAscending'];beta=proof['firstBetaCorrectionPolynomialsAscending']
  labels9=list(range(2,11));labels4=list(range(4001,4005));betalabels=list(range(2275,2279))
  mix=work/'inputs/projector-free-nine-image.mix';headers={k:v for k,v in initial['sources'].items() if k.endswith('.hpp')}
  def binding(data,logical,program): return digest({'inputs':[sha(f) for f in data],'logical':logical,'program':initial['sources'][PROGRAMS[program]],'headers':headers})
  started=time.monotonic();deadline=started+a.math_seconds;receipt['status']='running';save()
  def stage(name,program,args,marker,required,key,outputs):
   cached=cache/(name+'.json')
   if cached.exists():
    saved=json.loads(cached.read_text())
    if saved.get('inputBindingSHA256')==key and all(f.exists() and sha(f)==saved.get('outputs',{}).get(str(f.relative_to(work))) for f in outputs):
     receipt['stages'][name]={'status':'completed','reusedCompletedActualStage':True,'inputBindingSHA256':key,'nativeStatistics':saved['nativeStatistics'],'elapsedSeconds':0};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0: raise TimeoutError('shared mathematical deadline before '+name)
   command=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit','--as='+str(a.memory_mib*1048576),'--core=0','--',str(executables[program])]+list(map(str,args))
   row={'status':'running','inputBindingSHA256':key,'remainingSecondsAtStart':remaining,'command':command};receipt['stages'][name]=row;save();start=time.monotonic();events=[]
   process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1);row['wrapperPID']=process.pid;save()
   with (results/(name+'.log')).open('w') as log:
    for line in process.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:
      event=json.loads(line)
      if isinstance(event,dict): events.append(event);row['lastProgress']=event;save()
     except (ValueError,TypeError): pass
   code=process.wait();last=events[-1] if events else {};complete=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items()) and all(f.exists() for f in outputs)
   row.update(status='completed' if complete else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-start,nativeStatistics=last);receipt['mathematicalElapsedSeconds']=time.monotonic()-started;save()
   if not complete: raise RuntimeError('actual stage incomplete '+name)
   cached.write_text(json.dumps({'inputBindingSHA256':key,'outputs':{str(f.relative_to(work)):sha(f) for f in outputs},'nativeStatistics':last},indent=2)+'\n')
  stage('source','source9',source_args,'packed-image-source-convolution-complete',{'fullNormalFormDecompositionIdentity':True,'standardKernelNormalForm':True,'completeRHSInImage':True},initial['stages']['source']['inputBindingSHA256'],[suffix(source,s) for s in ('-standard-coefficients.bin','-source-certificate.json','-vq-checkpoint.bin')])
  transport=work/'projector-free-transport/projector-free-transport';transport.parent.mkdir(exist_ok=True)
  transport_data=[suffix(source,'-standard-coefficients.bin'),found['model'],found['normalTrace'],found['forward'],found['backward']]
  negative=lambda polys:[[[-c for c in poly] for poly in row] for row in polys]
  polyfamilies=[helper.identity(9),helper.identity(9,-1),negative(old_four),negative(beta)]
  transport_key=binding(transport_data+[found[k] for k in ('r2Trace','selectedTrace','fourTrace','betaTrace')],{'bound':87,'polynomials':polyfamilies},'transport')
  stage('transport','transport',transport_data+[mix,transport],'original-source-transport-complete',{},transport_key,[suffix(transport,'-primitive-source-mod31.bin'),suffix(transport,'-original-transport.json')])
  transported=json.loads(suffix(transport,'-original-transport.json').read_text());paid=max([87]+transported['sourceCosts'])
  if paid>183: raise ValueError('actual final source exceeds183')
  families=[{'file':found['uniformX'],'labels':labels9,'polys':helper.identity(9)},
   {'file':found['selectedK2'],'labels':labels9,'polys':helper.identity(9)},
   {'file':found['fourK2'],'labels':labels4,'polys':old_four},
   {'file':found['kernels'],'labels':betalabels,'polys':[[[31*c for c in p] for p in row] for row in beta]},
   {'file':suffix(transport,'-primitive-source-mod31.bin'),'labels':labels9,'polys':helper.identity(9,961)}]
  recipe=work/'inputs/projector-free-nine-original.recipe';helper.write_original(recipe,labels9,paid,29791,1,families)
  original=work/'projector-free-original/projector-free-original';original.parent.mkdir(exist_ok=True)
  data=[found['model'],found['integerModel']]+[f['file'] for f in families];logical={'bound':paid,'divisor':29791,'targetMode':1,'polynomials':[f['polys'] for f in families]}
  key=binding(data,logical,'original');cachekey=binding(data,{**logical,'checkpointBinding':key},'original')
  stage('original','original',[found['model'],found['integerModel'],recipe,original,key],'full-original-combination-complete',{'divisor':29791,'allOriginalProductCoefficientsDivisible':True,'fullOriginalSeventeenEquationIdentityMod29791':True},cachekey,[suffix(original,s) for s in ('-primitive-source-mod29791.bin','-original-seventeen-source-mod29791.bin','-original-product.json')])
  conclusion=json.loads(suffix(original,'-original-product.json').read_text())
  if not all(conclusion[k] for k in ('fullOriginalSeventeenEquationIdentityMod29791','fullOriginalMacaulayIdentityMod29791','originalRowScaleTransportVerified','allWeightedBoundsVerified')): raise ValueError('full original17 completion flags')
  receipt.update(status='completed',outcome='projector-free-full-original-mod29791-certificate',fullOriginalMod29791IdentityVerified=True,finite_budget_verified=True,actualSourceCosts=conclusion['actualSourceCosts'],originalSeventeenConclusion=conclusion,mathematicalElapsedSeconds=time.monotonic()-started);save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc))
  if started is not None: receipt['mathematicalElapsedSeconds']=time.monotonic()-started
  save()
 finally:
  if work.exists(): shutil.copytree(work,continued,dirs_exist_ok=True)
  certificates=results/'certificates';certificates.mkdir(exist_ok=True);certs=[]
  for f in sorted(recovery.rglob('*')):
   if not f.is_file(): continue
   relative=f.relative_to(recovery);flat=str(relative).replace('/','__')
   if f.suffix in ('.json','.log','.mix','.recipe'):
    shutil.copyfile(f,results/flat);continue
   temporary=out/(flat+'.gz.tmp')
   with f.open('rb') as src,temporary.open('wb') as dst:
    with gzip.GzipFile(filename='',mode='wb',fileobj=dst,mtime=0) as compressed: shutil.copyfileobj(src,compressed)
   item={'originalFile':str(relative),'uncompressedBytes':f.stat().st_size,'uncompressedSHA256':sha(f),'compressedBytes':temporary.stat().st_size,'compressedSHA256':sha(temporary),'parts':[]}
   with temporary.open('rb') as src:
    index=1
    while block:=src.read(4_500_000):
     target=certificates/(flat+'.gz' if item['compressedBytes']<=4_500_000 else flat+f'.gz.part{index:03d}');target.write_bytes(block);item['parts'].append({'file':str(target.relative_to(results)),'bytes':len(block),'sha256':hashlib.sha256(block).hexdigest()});index+=1
   temporary.unlink();certs.append(item)
  (results/'certificate-manifest.json').write_text(json.dumps({'format':'r150-three-stage-initial-and-continued-lossless-certificates-v1','pipelineStatus':receipt['status'],'partialCheckpointIsNotIdentity':True,'files':certs},indent=2)+'\n')
  files=[{'file':str(f.relative_to(recovery)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(recovery.rglob('*')) if f.is_file()]
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-three-stage-full-recovery-v1','pipelineStatus':receipt['status'],'files':files},indent=2)+'\n')
  receipt.update(recoveryFiles=len(files),recoveryBytes=sum(f['bytes'] for f in files));save();print(json.dumps({k:receipt.get(k) for k in ('status','outcome','mathematicalElapsedSeconds','fullOriginalMod29791IdentityVerified','actualSourceCosts','resumeSourceAtImageRowOneBased')}),flush=True)
 if receipt['status']!='completed': raise SystemExit(1)
if __name__=='__main__': main()
