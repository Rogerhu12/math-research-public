#!/usr/bin/env python3
"""Continue the saved H0 image quotient through actual VQ and original17.

This pipeline never reruns NF, image division, old graph or Bocksteins.
Two native stages share one bounded mathematical deadline.  The packed VQ
stage saves real partial arrays and may resume a compatible checkpoint.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,shutil,subprocess,time
from pathlib import Path

ARTIFACT_INPUTS={
 'graph':(['reweighted-basis.bin'],'bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce'),
 'model':(['normal-form-input.txt','native-normal-form-input.txt'],'291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6'),
 'originalNF':(['nf-normal-forms.bin'],'eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840'),
 'normalTrace':(['nf-reduction.bin'],'e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b'),
 'forward':(['nf-forward.bin'],'66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e'),
 'backward':(['nf-backward.bin'],'cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f'),
}
IMAGE_INPUTS={
 'rhs':('combined-rhs-normal-forms.bin.gz','581ce943262ba4dea66e9562889ec8cdd62e3808e34a8aeff33afb966c84bdf4'),
 'quotients':('image-image-quotients.bin.gz','c3dc4656e8cf56b579913002c4b210775420eeb7870d68993f135965b075a99c'),
 'remainders':('image-image-remainders.bin.gz','09bc43a84b590f93e885b57ead50f48a4047b2a5498c664d1e4a7a835193dd6a'),
}
SELECTED_INPUTS={
 'kernels':('cost85-selected-original-kernels.bin.gz','5cf08a41a81647dab8522c84e64de2ea442103063f6d870a820d5dd18bb226c7'),
 'betaTrace':('cost85-selected-normal-reduction.bin.gz','a489146317d14a3225c864e4b945c5c405b72ebbd03b1e2cbff8ff8dd71b8932'),
}
NOTE_INPUTS={
 'initial':('r150-first-padic-residual-789f/initial-standard-source.bin.gz','265b0b420afd925d72eb1ab2e2e329fe6232644d740a78aede67866da3545c96'),
 'firstTrace':('r150-first-residual-image-obstruction-789f/rhs-normal-form/reduction.bin.gz','6e1e0894d6cafa180f482129e19a387e64f401a28f566e96eefcb2b9761742be'),
}
INTEGER_SHA='71630a822927659a58a7b9df4cdcdb5385b9ea71be9f246097bbbfd1fdc9a5f8'
CPP={'source':'2026-11-14-r150-packed-image-source-checkpoint-789f.cpp',
     'original':'2026-11-14-r150-h25-original-seventeen-mod961-789f.cpp'}

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--t96-recovery-root',type=Path,required=True)
 p.add_argument('--image-inputs',type=Path)
 p.add_argument('--selected-inputs',type=Path)
 p.add_argument('--notes-root',type=Path)
 p.add_argument('--out',type=Path,required=True)
 p.add_argument('--resume-checkpoint',type=Path)
 p.add_argument('--seconds',type=int,default=300)
 p.add_argument('--memory-mib',type=int,default=512)
 p.add_argument('--compile-seconds',type=int,default=30)
 p.add_argument('--prepare-only',action='store_true')
 a=p.parse_args()
 if min(a.seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError('explicit positive resource bounds required')
 root=Path(__file__).resolve().parent;notes=(a.notes_root or root).resolve()
 image_inputs=(a.image_inputs or notes/'r150-h25-image-and-vq-prefix-789f').resolve()
 selected_inputs=(a.selected_inputs or notes/'r150-h25-selected-inputs-789f').resolve()
 a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
 results=a.out/'results';recovery=a.out/'recovery';binary_dir=a.out/'bin';inputs=recovery/'inputs'
 for folder in (results,recovery,binary_dir,inputs):folder.mkdir(exist_ok=True)
 rp=results/'h25-mod961-pipeline-receipt.json'
 receipt={'format':'r150-h25-original-mod961-pipeline-v1','status':'preparing',
  'prime':31,'targetModulus':961,'targetMultiplier':'H0=(s-2)*h0',
  'oldNFImageGraphOrBocksteinRecomputed':False,'characteristicZeroIdentityAsserted':False,
  'sharedMathematicalSecondsLimit':a.seconds,'perChildAddressSpaceMiBLimit':a.memory_mib,
  'perCompilationSecondsLimit':a.compile_seconds,
  'deadlineRule':'Input validation/decompression and separately bounded compilation precede the mathematical timer. Packed VQ plus canonical source recovery plus full original17 transport and multiplication share one deadline. Each child receives the actual remaining time with10-second forced-kill grace. Actual partial VQ arrays are saved every100 rows and at a caught termination boundary. Final lossless compression/manifests are bookkeeping outside the mathematical timer.',
  'originalT96Artifact':{'run':43597823809,'artifact':14114364261},
  'inputs':{},'sources':{},'compilations':{},'stages':{}}
 def save():rp.write_text(json.dumps(receipt,indent=2)+'\n')
 def record_input(name,path,expected,compressed=None):
  if sha(path)!=expected:raise ValueError('frozen input checksum: '+name)
  receipt['inputs'][name]={'file':str(path),'bytes':path.stat().st_size,'sha256':expected}
  if compressed is not None:receipt['inputs'][name]['compressedOrigin']={'file':str(compressed),'bytes':compressed.stat().st_size,'sha256':sha(compressed)}
 save();found={}
 try:
  for name,(filenames,expected) in ARTIFACT_INPUTS.items():
   candidates=sorted({f for short in filenames for f in a.t96_recovery_root.rglob(short) if f.is_file()})
   if name=='model':candidates+=sorted(notes.rglob('native-normal-form-input.txt'))
   good=[f for f in candidates if sha(f)==expected]
   if not good:raise ValueError('missing exact original T96 input: '+name)
   found[name]=good[0].resolve();record_input(name,found[name],expected)
  for directory,entries in ((image_inputs,IMAGE_INPUTS),(selected_inputs,SELECTED_INPUTS),(notes,NOTE_INPUTS)):
   for name,(filename,expected) in entries.items():
    compressed=directory/filename;f=inputs/(name+'.bin')
    with gzip.open(compressed,'rb') as source,f.open('wb') as destination:shutil.copyfileobj(source,destination)
    record_input(name,f,expected,compressed);found[name]=f
  image_meta=json.loads((image_inputs/'image-image-certificate.json').read_text())
  if image_meta.get('status')!='completed' or not image_meta.get('fullImageQuotientIdentity') or not image_meta.get('completeRHSInImage') or image_meta.get('remainderNonzeroCoefficients')!=[0]*9:raise ValueError('actual completed nine-target GQ identity required')
  selected_meta=json.loads((selected_inputs/'selected-inputs-receipt.json').read_text())
  if selected_meta.get('status')!='completed-storage-selection-only' or selected_meta.get('allOriginalRawRowsRetained')!=6188 or selected_meta.get('selectedLabels')!=[[2192,2275,85,1241,3485],[2193,2276,85,1242,3497]]:raise ValueError('actual cost85 source projection identity required')
  if selected_meta.get('originalKernelSHA256')!='ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88' or selected_meta.get('originalNormalTraceSHA256')!='85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae':raise ValueError('actual full200 origin required')
  found['integerModel']=notes/'r150-first-padic-residual-789f/original-integer-mod961.txt';record_input('integerModel',found['integerModel'],INTEGER_SHA)
  for filename in list(CPP.values())+[Path(__file__).name]:receipt['sources'][filename]=sha(root/filename)
  header=notes/'2026-11-14-r150-f31-bitplane-789f.hpp';receipt['sources'][header.name]=sha(header)
  shutil.copyfile(image_inputs/'image-image-certificate.json',results/'input-complete-image-certificate.json')
  shutil.copyfile(selected_inputs/'selected-inputs-receipt.json',results/'input-selected-original-sources.json')
  binding_fields={name:receipt['inputs'][name]['sha256'] for name in ('graph','originalNF','rhs','quotients','remainders')}
  binding_fields['sourceCode']=receipt['sources'][CPP['source']]
  binding=hashlib.sha256(json.dumps(binding_fields,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  receipt['sourceCheckpointBinding']={'sha256':binding,'fields':binding_fields};save()
  binaries={}
  for name,filename in CPP.items():
   binaries[name]=binary_dir/name
   command=['timeout','--kill-after=10s',f'{a.compile_seconds}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--','g++','-O2','-std=c++17','-I',str(notes),str(root/filename),'-o',str(binaries[name])]
   t=time.monotonic();r=subprocess.run(command,capture_output=True,text=True)
   (results/('compile-'+name+'.log')).write_text(r.stdout+r.stderr)
   receipt['compilations'][name]={'command':command,'exitCode':r.returncode,'elapsedSeconds':time.monotonic()-t}
   if r.returncode:raise RuntimeError('bounded source compilation failed: '+name)
   receipt['compilations'][name]['binarySHA256']=sha(binaries[name]);save()
  if a.prepare_only:
   receipt['status']='prepared-no-mathematics-executed';save();return
  source_dir=recovery/'source';source_dir.mkdir(exist_ok=True);source_prefix=source_dir/'source'
  if a.resume_checkpoint:
   checkpoint=Path(str(source_prefix)+'-vq-checkpoint.bin')
   if a.resume_checkpoint.resolve()!=checkpoint.resolve():shutil.copyfile(a.resume_checkpoint,checkpoint)
   receipt['resumedCheckpoint']={'file':str(checkpoint),'bytes':checkpoint.stat().st_size,'sha256':sha(checkpoint),'nativeBindingCheckRequired':True};save()
  math_start=time.monotonic();deadline=math_start+a.seconds;receipt['status']='running';save()
  def run_stage(name,command,marker,required):
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('shared mathematical deadline before '+name)
   bounded=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--']+[str(x) for x in command]
   stage={'status':'running','command':bounded,'remainingSecondsAtStart':remaining};receipt['stages'][name]=stage;save();t=time.monotonic()
   child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   events=[]
   with (results/(name+'.log')).open('w') as log:
    for line in child.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:event=json.loads(line);events.append(event);stage['lastProgress']=event;save()
     except (ValueError,TypeError):pass
   code=child.wait();last=events[-1] if events else {}
   complete=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items())
   stage.update(status='completed' if complete else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-t,nativeStatistics=last)
   receipt['mathematicalElapsedSeconds']=time.monotonic()-math_start;save()
   if not complete:raise RuntimeError('actual mathematical stage incomplete: '+name)
  run_stage('source',[binaries['source'],found['graph'],found['originalNF'],found['rhs'],found['quotients'],found['remainders'],source_prefix,binding],
   'packed-image-source-convolution-complete',{'fullNormalFormDecompositionIdentity':True,'standardKernelNormalForm':True,'completeRHSInImage':True,'originalSeventeenEquationTransported':False})
  source_meta=Path(str(source_prefix)+'-source-certificate.json');shutil.copyfile(source_meta,results/source_meta.name)
  receipt['original2195NormalSourceIdentity']=json.loads(source_meta.read_text());save()
  original_dir=recovery/'original';original_dir.mkdir(exist_ok=True);original_prefix=original_dir/'h25'
  run_stage('original',[binaries['original'],Path(str(source_prefix)+'-standard-coefficients.bin'),found['model'],found['normalTrace'],found['forward'],found['backward'],found['integerModel'],found['initial'],found['kernels'],found['firstTrace'],found['betaTrace'],original_prefix],
   'h25-full-original-seventeen-mod961-complete',{'prime':31,'modulus':961,'fullOriginalSeventeenEquationIdentityMod961':True,'fullOriginalMacaulayIdentityMod961':True,'originalRowScaleTransportVerified':True,'allWeightedBoundsVerified':True,'characteristicZeroIdentityAsserted':False})
  original_meta=Path(str(original_prefix)+'-original-seventeen-mod961.json');shutil.copyfile(original_meta,results/original_meta.name)
  receipt['originalSeventeenConclusion']=json.loads(original_meta.read_text())
  receipt.update(status='completed',mathematicalElapsedSeconds=time.monotonic()-math_start);save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc));save()
 finally:
  # Every actual generated certificate or partial VQ checkpoint is retained.
  # The original uncompressed file remains in recovery; published gzip payloads
  # are split below the repository's decimal5MB individual-file limit.
  certificates=results/'certificates';certificates.mkdir(exist_ok=True);certificate_files=[]
  for folder in (recovery/'source',recovery/'original'):
   if not folder.exists():continue
   for f in sorted(folder.glob('*.bin')):
    name=str(f.relative_to(recovery)).replace('/','__');temporary=recovery/(name+'.gz.tmp')
    with f.open('rb') as src,temporary.open('wb') as dest:
     with gzip.GzipFile(filename='',mode='wb',fileobj=dest,mtime=0) as zipped:shutil.copyfileobj(src,zipped)
    record={'originalFile':str(f.relative_to(a.out)),'uncompressedBytes':f.stat().st_size,'uncompressedSHA256':sha(f),'compressedBytes':temporary.stat().st_size,'compressedSHA256':sha(temporary),'parts':[]}
    with temporary.open('rb') as zipped:
     part=1
     while block:=zipped.read(4_500_000):
      target=certificates/(name+'.gz' if record['compressedBytes']<=4_500_000 else name+f'.gz.part{part:03d}')
      target.write_bytes(block);record['parts'].append({'file':str(target.relative_to(results)),'bytes':len(block),'sha256':hashlib.sha256(block).hexdigest()});part+=1
    temporary.unlink();certificate_files.append(record)
  (results/'certificate-manifest.json').write_text(json.dumps({'format':'r150-h25-actual-original-certificates-v1','pipelineStatus':receipt['status'],'partialSourceCheckpointIsNotIdentity':True,'files':certificate_files},indent=2)+'\n')
  recovery_files=[]
  for f in sorted(recovery.rglob('*')):
   if f.is_file():recovery_files.append({'file':str(f.relative_to(a.out)),'bytes':f.stat().st_size,'sha256':sha(f)})
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-h25-mod961-complete-recovery-v1','pipelineStatus':receipt['status'],'files':recovery_files},indent=2)+'\n')
  receipt['recoveryFiles']=len(recovery_files);receipt['recoveryBytes']=sum(f['bytes'] for f in recovery_files);receipt['losslessCertificateFiles']=len(certificate_files);save()
 print(json.dumps({'status':receipt['status'],'mathematicalElapsedSeconds':receipt.get('mathematicalElapsedSeconds'),'original2195NormalSourceIdentityVerified':bool(receipt.get('original2195NormalSourceIdentity')),'fullOriginalSeventeenEquationIdentityMod961':receipt.get('originalSeventeenConclusion',{}).get('fullOriginalSeventeenEquationIdentityMod961',False),'characteristicZeroIdentityAsserted':False,'recoveryBytes':receipt['recoveryBytes']}),flush=True)
 if receipt['status']!='completed':raise SystemExit(1)

if __name__=='__main__':main()
