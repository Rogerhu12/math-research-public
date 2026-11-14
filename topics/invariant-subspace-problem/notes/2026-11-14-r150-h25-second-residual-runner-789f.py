#!/usr/bin/env python3
"""One shared60s original second-residual/NF/image/beta computation."""
from __future__ import annotations
import argparse,gzip,hashlib,json,shutil,subprocess,time
from pathlib import Path

CPP={'residual':'2026-11-14-r150-h25-second-original-residual-789f.cpp',
     'normal':'2026-11-14-r150-h25-second-residual-normal-form-789f.cpp',
     'image':'2026-11-14-r150-h25-second-residual-image-789f.cpp'}
X_SHA='6ff5083ce8567c5a333acb8e26bba9e3bb64a53c5dda8d693c1411b163566e32'
MODEL_SHA='291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6'
GRAPH_SHA='bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce'

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  while block:=f.read(1048576):h.update(block)
 return h.hexdigest()

def main():
 p=argparse.ArgumentParser()
 for name in ('model','graph','primitive-source','h25-results','complete-beta-results','notes-root','out'):
  p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--seconds',type=int,default=60);p.add_argument('--memory-mib',type=int,default=512);p.add_argument('--compile-seconds',type=int,default=30)
 a=p.parse_args()
 if min(a.seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError('explicit positive resource limits')
 root=Path(__file__).resolve().parent;a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
 results=a.out/'results';recovery=a.out/'recovery';binaries=a.out/'bin'
 for f in (results,recovery,binaries):f.mkdir(exist_ok=True)
 rp=results/'second-residual-pipeline-receipt.json'
 receipt={'format':'r150-h25-second-residual-pipeline-v1','status':'preparing','prime':31,'integerModulus':29791,'inputActualSourceModulus':961,'targetMultiplier':'H0=(s-2)*h0','inputActualSourceRun':43611215116,'sharedMathematicalSecondsLimit':a.seconds,'perChildAddressSpaceMiBLimit':a.memory_mib,'perCompilationSecondsLimit':a.compile_seconds,'oldBocksteinsGraphOrImageBasisRecomputed':False,'finite_budget_verified':False,'allMod961KernelFreedomIncluded':False,'characteristicZeroIdentityAsserted':False,'inputs':{},'sources':{},'compilations':{},'stages':{},'deadlineRule':'After exact input validation, integer-model residue encoding and separately bounded compilation, all4 mathematical stages share one deadline. Each child has the actual remaining time and10-second forced-kill grace. Final compression/manifests only preserve actual output.'}
 def save():rp.write_text(json.dumps(receipt,indent=2)+'\n')
 save()
 try:
  for name,path,expected in [('model',a.model,MODEL_SHA),('graph',a.graph,GRAPH_SHA),('actualPrimitiveSource',a.primitive_source,X_SHA)]:
   if sha(path)!=expected:raise ValueError('actual input checksum: '+name)
   receipt['inputs'][name]={'file':str(path),'bytes':path.stat().st_size,'sha256':expected}
  old=json.loads((a.h25_results/'h25-mod961-pipeline-receipt.json').read_text());identity=json.loads((a.h25_results/'h25-original-seventeen-mod961.json').read_text())
  if old.get('status')!='completed' or not identity.get('fullOriginalSeventeenEquationIdentityMod961') or not identity.get('originalRowScaleTransportVerified') or identity.get('actualFullSourceCost')!=86:raise ValueError('actual completed original H0 source with cost86')
  manifest=json.loads((a.h25_results/'certificate-manifest.json').read_text())
  entries=[x for x in manifest['files'] if x['originalFile'].endswith('h25-primitive-source-mod961.bin')]
  if len(entries)!=1 or entries[0]['uncompressedSHA256']!=X_SHA:raise ValueError('actual original X certificate manifest')
  shutil.copyfile(a.h25_results/'h25-original-seventeen-mod961.json',results/'input-actual-original-mod961.json')
  for f in list(CPP.values())+['2026-11-14-r150-h25-mod29791-model-789f.py','2026-11-14-r150-h25-second-residual-beta-test-789f.py',Path(__file__).name]:receipt['sources'][f]=sha(root/f)
  for f in ['2026-11-14-r150-f31-bitplane-789f.hpp','2026-11-14-r150-torsion-characteristic-789f.py']:receipt['sources'][f]=sha(a.notes_root/f)
  modeldir=recovery/'integer-model';modeldir.mkdir(exist_ok=True)
  command=['timeout','--kill-after=10s','30s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--','python3',str(root/'2026-11-14-r150-h25-mod29791-model-789f.py'),'--exact-json',str(a.notes_root/'r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz'),'--original-model',str(a.model),'--out',str(modeldir)]
  r=subprocess.run(command,capture_output=True,text=True);(results/'integer-model-preparation.log').write_text(r.stdout+r.stderr)
  if r.returncode:raise RuntimeError('original mod29791 residue encoding failed')
  model_receipt=json.loads((modeldir/'mod29791-model-receipt.json').read_text())
  if model_receipt.get('status')!='exact-original-model-reduced' or model_receipt.get('modulus')!=29791:raise ValueError('actual original higher integer model')
  receipt['integerModelPreparation']=model_receipt;shutil.copyfile(modeldir/'mod29791-model-receipt.json',results/'mod29791-model-receipt.json');save()
  exe={}
  for name,file in CPP.items():
   exe[name]=binaries/name;command=['timeout','--kill-after=10s',f'{a.compile_seconds}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--','g++','-O2','-std=c++17','-I',str(a.notes_root),str(root/file),'-o',str(exe[name])]
   start=time.monotonic();r=subprocess.run(command,capture_output=True,text=True);(results/('compile-'+name+'.log')).write_text(r.stdout+r.stderr)
   receipt['compilations'][name]={'command':command,'exitCode':r.returncode,'elapsedSeconds':time.monotonic()-start}
   if r.returncode:raise RuntimeError('bounded compilation failed: '+name)
   receipt['compilations'][name]['binarySHA256']=sha(exe[name]);save()
  mathematical_start=time.monotonic();deadline=mathematical_start+a.seconds;receipt['status']='running';save()
  def run(name,command,marker,required):
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('shared mathematical deadline before '+name)
   bounded=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--']+[str(x) for x in command]
   stage={'status':'running','command':bounded,'remainingSecondsAtStart':remaining};receipt['stages'][name]=stage;save();start=time.monotonic()
   child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1);events=[]
   with (results/(name+'.log')).open('w') as log:
    for line in child.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:event=json.loads(line);events.append(event);stage['lastProgress']=event;save()
     except (ValueError,TypeError):pass
   code=child.wait();last=events[-1] if events else {};complete=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items())
   stage.update(status='completed' if complete else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-start,nativeStatistics=last);receipt['mathematicalElapsedSeconds']=time.monotonic()-mathematical_start;save()
   if not complete:raise RuntimeError('actual stage incomplete: '+name)
  original=recovery/'original';normal=recovery/'normal';image=recovery/'image'
  for d in (original,normal,image):d.mkdir(exist_ok=True)
  op=original/'h25';np=normal/'second';ip=image/'second'
  run('residual',[exe['residual'],a.model,modeldir/'original-integer-h25-mod29791.txt',a.primitive_source,op],
   'h25-second-original-padic-residual-complete',{'actualFullOriginalIdentityMod961':True,'allOriginalWeightedBoundsVerified':True,'actualSourceCost':86,'sourceCorrectionComputed':False})
  original_meta=Path(str(op)+'-second-residual.json');shutil.copyfile(original_meta,results/original_meta.name)
  run('normal',[exe['normal'],a.model,Path(str(op)+'-second-residual.bin'),np],
   'h25-second-original-rhs-normal-forms-complete',{'sources':0,'targets':9,'components':1034,'originalRHSCost':86})
  for suffix,expected in [('forward','66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e'),('backward','cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f')]:
   if sha(Path(str(np)+'-'+suffix+'.bin'))!=expected:raise ValueError('original constant prebasis changed in new RHS normalization')
  run('image',[exe['image'],a.graph,Path(str(np)+'-normal-forms.bin'),ip],
   'h25-second-residual-complete-image-certificate',{'fullImageQuotientIdentity':True,'everyRemainderIsIrreducible':True})
  image_meta=Path(str(ip)+'-image-certificate.json');shutil.copyfile(image_meta,results/image_meta.name)
  run('beta-test',['python3',root/'2026-11-14-r150-h25-second-residual-beta-test-789f.py','--notes-root',a.notes_root,'--complete-beta-results',a.complete_beta_results,'--original-metadata',original_meta,'--image-metadata',image_meta,'--image-quotients',Path(str(ip)+'-image-quotients.bin'),'--image-remainders',Path(str(ip)+'-image-remainders.bin'),'--out',results],
   'h25-second-residual-torsion-and-beta-test-complete',{'allOriginalNormalCoordinatesRetained':True,'allMod961KernelFreedomIncluded':False,'finite_budget_verified':False})
  outcome=json.loads((results/'second-residual-full-beta-result.json').read_text())
  receipt['nextDigitCondition']={k:outcome[k] for k in ['residualsInTorsion','sameMod31InitialSourceLiftCompatibility','commonMinimumModuloFullFirstBetaImage']}
  receipt.update(status='completed',mathematicalElapsedSeconds=time.monotonic()-mathematical_start);save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc));save()
 finally:
  state=results/'state-input.bin'
  if state.exists():shutil.move(str(state),str(recovery/'state-input.bin'))
  certificates=results/'certificates';certificates.mkdir(exist_ok=True);compressed=[]
  for folder in [recovery/'original',recovery/'normal',recovery/'image']:
   if not folder.exists():continue
   for f in sorted(folder.glob('*.bin')):
    name=str(f.relative_to(recovery)).replace('/','__');temporary=recovery/(name+'.gz.tmp')
    with f.open('rb') as src,temporary.open('wb') as dest:
     with gzip.GzipFile(filename='',mode='wb',fileobj=dest,mtime=0) as zipped:shutil.copyfileobj(src,zipped)
    record={'originalFile':str(f.relative_to(a.out)),'uncompressedBytes':f.stat().st_size,'uncompressedSHA256':sha(f),'compressedBytes':temporary.stat().st_size,'compressedSHA256':sha(temporary),'parts':[]}
    with temporary.open('rb') as zipped:
     number=1
     while block:=zipped.read(4_500_000):
      fpart=certificates/(name+'.gz' if record['compressedBytes']<=4_500_000 else name+f'.gz.part{number:03d}');fpart.write_bytes(block);record['parts'].append({'file':str(fpart.relative_to(results)),'bytes':len(block),'sha256':hashlib.sha256(block).hexdigest()});number+=1
    temporary.unlink();compressed.append(record)
  (results/'certificate-manifest.json').write_text(json.dumps({'format':'r150-h25-second-residual-certificates-v1','pipelineStatus':receipt['status'],'files':compressed},indent=2)+'\n')
  files=[{'file':str(f.relative_to(a.out)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(recovery.rglob('*')) if f.is_file()]
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-h25-second-residual-recovery-v1','pipelineStatus':receipt['status'],'files':files},indent=2)+'\n')
  receipt['recoveryFiles']=len(files);receipt['recoveryBytes']=sum(f['bytes'] for f in files);save()
 print(json.dumps({'status':receipt['status'],'mathematicalElapsedSeconds':receipt.get('mathematicalElapsedSeconds'),'nextDigitCondition':receipt.get('nextDigitCondition'),'allMod961KernelFreedomIncluded':False,'characteristicZeroIdentityAsserted':False}),flush=True)
 if receipt['status']!='completed':raise SystemExit(1)

if __name__=='__main__':main()
