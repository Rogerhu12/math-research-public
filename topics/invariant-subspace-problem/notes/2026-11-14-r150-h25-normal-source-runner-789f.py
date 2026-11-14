#!/usr/bin/env python3
"""One bounded H0=(s-2)h0 normal-source recovery; no original identity claim.

All three mathematical stages share one deadline.  Old NF, graph and Bockstein
data are read, not recomputed.  Original6188-row transport is a subsequent stage.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,subprocess,time
from pathlib import Path

EXPECTED={
 'graph':'bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce',
 'original_nf':'eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840',
 'first_normal_form':'5016b8e42f2ef1b36c9107b95616a190a47697b640599cb9eb98b2476be8f317',
 'beta_normal_form':'c1b0e2e79a52e312acb9a9b89a03c031a5d6bbd5afc34c862ff7c2ff35479b2b',
 'beta_metadata':'730ee02d91e53cbfc1463fbfb366ee35edaa908775af30f97dedef8cae1749e9',
 'common_g_result':'d5ce008439820c4ed9ff33f58ca33267f4e3badf429ab581311818d1fb5b3a76',
}
CPP={'image':'2026-11-14-r150-h25-combined-image-789f.cpp',
     'source':'2026-11-14-r150-packed-image-source-convolution-789f.cpp'}
COMBINE='2026-11-14-r150-h25-combined-normal-form-789f.py'

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()

def main():
 p=argparse.ArgumentParser()
 for k in EXPECTED:p.add_argument('--'+k.replace('_','-'),type=Path,required=True)
 p.add_argument('--out',type=Path,required=True)
 p.add_argument('--notes-root',type=Path)
 p.add_argument('--seconds',type=int,default=60)
 p.add_argument('--memory-mib',type=int,default=512)
 p.add_argument('--compile-seconds',type=int,default=30)
 p.add_argument('--prepare-only',action='store_true')
 a=p.parse_args()
 if min(a.seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError('explicit positive resource bounds')
 source=Path(__file__).resolve().parent;notes=(a.notes_root or source).resolve()
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 results=out/'results';recovery=out/'recovery';binaries=out/'bin'
 for q in (results,recovery,binaries):q.mkdir(exist_ok=True)
 receipt={'format':'r150-h25-normal-source-pipeline-v1','status':'preparing',
  'field':31,'originalTargetMultiplier':'H0=(s-2)*h0',
  'originalSeventeenEquationTransported':False,'oldNFGraphOrBocksteinsRecomputed':False,
  'sharedMathematicalSecondsLimit':a.seconds,'perChildAddressSpaceMiBLimit':a.memory_mib,
  'perCompilationSecondsLimit':a.compile_seconds,
  'deadlineRule':'After input validation and separately bounded compilation, NF combination, full image quotient and packed9-source convolution share one mathematical deadline. Each child receives the actual remaining time with10-second forced-kill grace. Final hash/manifests are bookkeeping outside that deadline.',
  'inputs':{},'sources':{},'compilations':{},'stages':{},'outputs':{}}
 rp=results/'h25-normal-source-pipeline-receipt.json'
 def save():rp.write_text(json.dumps(receipt,indent=2)+'\n')
 save()
 try:
  for name,expected in EXPECTED.items():
   f=getattr(a,name).resolve()
   if sha(f)!=expected:raise ValueError('actual frozen input checksum: '+name)
   receipt['inputs'][name]={'file':str(f),'bytes':f.stat().st_size,'sha256':expected}
  for f in [source/COMBINE,source/Path(__file__).name,*[source/x for x in CPP.values()],notes/'2026-11-14-r150-f31-bitplane-789f.hpp']:
   receipt['sources'][f.name]=sha(f)
  save()
  exe={}
  for name,filename in CPP.items():
   exe[name]=binaries/name
   command=['timeout','--kill-after=10s',f'{a.compile_seconds}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--','g++','-O2','-std=c++17','-I',str(notes),str(source/filename),'-o',str(exe[name])]
   start=time.monotonic();r=subprocess.run(command,capture_output=True,text=True)
   (results/('compile-'+name+'.log')).write_text(r.stdout+r.stderr)
   receipt['compilations'][name]={'command':command,'exitCode':r.returncode,'elapsedSeconds':time.monotonic()-start}
   if r.returncode:raise RuntimeError('bounded compilation failed: '+name)
   receipt['compilations'][name]['binarySHA256']=sha(exe[name]);save()
  if a.prepare_only:
   receipt['status']='prepared-no-mathematics-executed';save();return
  start=time.monotonic();deadline=start+a.seconds;receipt['status']='running';save()
  def run(name,command,marker,required):
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('shared mathematical deadline before '+name)
   bounded=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--']+[str(x) for x in command]
   stage={'status':'running','command':bounded,'remainingSecondsAtStart':remaining};receipt['stages'][name]=stage;save();t=time.monotonic()
   child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   events=[]
   with (results/(name+'.log')).open('w') as log:
    for line in child.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:
      event=json.loads(line);events.append(event);stage['lastProgress']=event;save()
     except (ValueError,TypeError):pass
   code=child.wait();last=events[-1] if events else {}
   good=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items())
   stage.update(status='completed' if good else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-t,nativeStatistics=last)
   receipt['mathematicalElapsedSeconds']=time.monotonic()-start;save()
   if not good:raise RuntimeError('actual mathematical stage incomplete: '+name)
  nf=recovery/'combined-normal-form';nf.mkdir(exist_ok=True)
  run('combine',['python3',source/COMBINE,'--first-normal-form',a.first_normal_form,'--beta-normal-form',a.beta_normal_form,'--beta-metadata',a.beta_metadata,'--common-g-result',a.common_g_result,'--out',nf],
   'h25-combined-normal-form-complete',{'actualTargets':9,'sourceTransported':False})
  rhs=nf/'combined-rhs-normal-forms.bin'
  img=recovery/'image';img.mkdir(exist_ok=True);ip=img/'image'
  run('image',[exe['image'],a.graph,rhs,ip],'h25-combined-residual-complete-image-certificate',{'fullImageQuotientIdentity':True,'everyRemainderIsIrreducible':True,'completeRHSInImage':True})
  sourceout=recovery/'source';sourceout.mkdir(exist_ok=True);sp=sourceout/'source'
  run('source',[exe['source'],a.graph,a.original_nf,rhs,Path(str(ip)+'-image-quotients.bin'),Path(str(ip)+'-image-remainders.bin'),sp],
   'packed-image-source-convolution-complete',{'fullNormalFormDecompositionIdentity':True,'standardKernelNormalForm':True,'completeRHSInImage':True,'originalSeventeenEquationTransported':False})
  receipt.update(status='completed',mathematicalElapsedSeconds=time.monotonic()-start)
  for f in (nf/'combined-normal-form-receipt.json',Path(str(ip)+'-image-certificate.json'),Path(str(sp)+'-source-certificate.json')):
   shutil.copyfile(f,results/f.name)
  final=json.loads(Path(str(sp)+'-source-certificate.json').read_text())
  receipt['normalSourceConclusion']={k:final[k] for k in ('fullNormalFormDecompositionIdentity','standardKernelNormalForm','completeRHSInImage','allStandardSourceCostsWithinInputBound','targetStandardSourceCosts','maximumCoefficientDegree','nonzeroSources','nonzeroCoefficients')}
  save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc));save()
 finally:
  files=[]
  for f in sorted(recovery.rglob('*')):
   if f.is_file():files.append({'file':str(f.relative_to(out)),'bytes':f.stat().st_size,'sha256':sha(f)})
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-h25-normal-source-recovery-v1','pipelineStatus':receipt['status'],'files':files},indent=2)+'\n')
  receipt['recoveryFiles']=len(files);receipt['recoveryBytes']=sum(f['bytes'] for f in files);save()
 print(json.dumps({'status':receipt['status'],'mathematicalElapsedSeconds':receipt.get('mathematicalElapsedSeconds'),'normalSourceConclusion':receipt.get('normalSourceConclusion'),'originalSeventeenEquationTransported':False,'recoveryBytes':receipt['recoveryBytes']}),flush=True)
 if receipt['status']!='completed':raise SystemExit(1)

if __name__=='__main__':main()
