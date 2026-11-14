#!/usr/bin/env python3
"""One bounded four-column delta2 attempt, continuing positive results to original17.

No old graph, original2195 NF or first Bockstein is recomputed.  Both VQ stages
save actual resumable arrays.  Completed stages have content-bound caches.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,shutil,struct,subprocess,time
from pathlib import Path

ARTIFACT={
 'graph':(['reweighted-basis.bin'],'bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce'),
 'model':(['normal-form-input.txt','native-normal-form-input.txt'],'291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6'),
 'originalNF':(['nf-normal-forms.bin'],'eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840'),
 'normalTrace':(['nf-reduction.bin'],'e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b'),
 'forward':(['nf-forward.bin'],'66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e'),
 'backward':(['nf-backward.bin'],'cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f')}
SELECTED={
 'betaNF':('four-beta-nf.bin','7f716fd2ed58088c1e8d8d2e4f77771d65d6b039418e884b226991b3a58afdcc'),
 'betaQ':('four-beta-quotients.bin','934c42fb9979b91743af2d4e66bdcf5ed30f99555ba35aa6cec01a5e33fec667'),
 'betaRem':('four-beta-rem.bin','eec6e8ae82e3bb3581e1817e85a479bc1951d6b819273c1df4bde7e72fbd0cdd'),
 'betaTrace':('four-beta-trace.bin','2705394b3744d8a1140edcbf3a269c9739ed6a39a6ceda63cb2cfb3f644922f2'),
 'kernels':('four-original-kernels.bin','c6ebd427d59033755a8f9852f64d7509f249727e05c0d62834537aa0a3bdbf7f')}
NOTE_INPUTS={
 'actualX':('r150-h25-original-mod961-actions-789f/43611215116-1/certificates/original__h25-primitive-source-mod961.bin.gz','6ff5083ce8567c5a333acb8e26bba9e3bb64a53c5dda8d693c1411b163566e32'),
 'r2NF':('r150-h25-second-residual-789f/certificates/normal__second-normal-forms.bin.gz','392169882cdf20075bdb6dfa18efb0a7bc181eda855aef7313aa3e69e872bd36'),
 'r2Q':('r150-h25-second-residual-789f/certificates/image__second-image-quotients.bin.gz','262cf26bfc144dd541fb094dbe263710f958303b55d4bfd614cf446169cc0dfd'),
 'r2Rem':('r150-h25-second-residual-789f/certificates/image__second-image-remainders.bin.gz','e6a5f269a0d01fe11e75934d128fb3fe43f2b0f3e5c7247ee52303716a470d76'),
 'r2Trace':('r150-h25-second-residual-789f/certificates/normal__second-reduction.bin.gz','43157d0ba3a1e34480d3285df1b657a1d2b24118b615820cd1f53ec33996fcae')}
PLAIN_INPUTS={
 'integerModel':('r150-h25-second-residual-789f/original-integer-h25-mod29791.txt','2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc'),
 'firstSystem':('r150-last-two-kernel-bockstein-actions-789f/43608688492-1/complete-polynomial-bockstein-image.bin.gz','f755f05723bcdd79193d40fea984fdd532248e50a99b0d755fac2c5433661aa5'),
 'secondSystem':('r150-h25-second-residual-789f/second-residual-full-beta-system.bin.gz','3f35ab42bdf4949eb08b01d89431d192cb1185f4f1ab87dd54d2efa04952a77a')}
CPP={
 'image':('2026-11-14-r150-second-bockstein-image-mixture-789f.cpp',[]),
 'source4':('2026-11-14-r150-second-bockstein-source-checkpoint-789f.cpp',['-DR150_TARGETS=4']),
 'source9':('2026-11-14-r150-second-bockstein-source-checkpoint-789f.cpp',['-DR150_TARGETS=9']),
 'transport':('2026-11-14-r150-second-bockstein-original-transport-789f.cpp',[]),
 'original':('2026-11-14-r150-second-bockstein-original-combination-789f.cpp',[]),
 'normal':('2026-11-14-r150-second-bockstein-normal-form-789f.cpp',[])}
QUOTIENT='2026-11-14-r150-four-second-bockstein-quotient-test-789f.py'
RELATIONS=[[[-10,-12],[-21,-25],[-21,-16],[2,-3,1]],[[1],[],[],[]],[[],[1],[],[]],[[],[],[1],[]]]

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def suffix(p,s):return Path(str(p)+s)
def identity(n,c=1):return [[[c] if i==j else [] for j in range(n)] for i in range(n)]
def normalize(p,modulus):
 p=[x%modulus for x in p]
 while p and not p[-1]:p.pop()
 return p
def write_mix(path,labels,N,families):
 lines=['R150_RHS_MIX_V1',f'{len(labels)} {N} {len(families)}',' '.join(map(str,labels))]
 for f in families:
  lines.append(' '.join(str(f[k]) for k in ('nf','q','rem','trace'))+' '+str(len(f['labels'])))
  lines.append(' '.join(map(str,f['labels'])))
  for row in f['polys']:
   for poly in row:
    p=normalize(poly,31);lines.append(' '.join(map(str,[len(p)]+p)))
 path.write_text('\n'.join(lines)+'\n')
def write_original(path,labels,B,divisor,target,families):
 lines=['R150_ORIGINAL_COMBINATION_V1',f'{len(labels)} {B} {divisor} {target} {len(families)}',' '.join(map(str,labels))]
 for f in families:
  lines.append(str(f['file'])+' '+str(len(f['labels'])));lines.append(' '.join(map(str,f['labels'])))
  for row in f['polys']:
   for poly in row:
    p=normalize(poly,29791);lines.append(' '.join(map(str,[len(p)]+p)))
 path.write_text('\n'.join(lines)+'\n')
def uniform_actual_x(original,out):
 b=original.read_bytes()
 if b[:8]!=b'R150P961' or struct.unpack_from('<6I',b,8)!=(31,961,6188,9,182,25):raise ValueError('actual frozen H0 source header')
 offset=32+26*2+2+17*2
 # Only the header is converted. Every original row record and u16 coefficient
 # is copied verbatim, retaining the actual canonical modulo961 source.
 out.write_bytes(b'R150PS31'+struct.pack('<5I',31,961,6188,9,182)+struct.pack('<9H',*range(2,11))+b[offset:])
 return {'originalSHA256':sha(original),'originalHeaderBytes':offset,'outputSHA256':sha(out),'sourceRecordsCopiedVerbatim':True}

def main():
 p=argparse.ArgumentParser()
 for k in ('notes-root','t96-recovery','selected-inputs','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--math-seconds',type=int,default=300);p.add_argument('--memory-mib',type=int,default=512);p.add_argument('--compile-seconds',type=int,default=30)
 p.add_argument('--resume-recovery',type=Path);p.add_argument('--prepare-only',action='store_true');a=p.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError('explicit positive bounded resources')
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
 results=a.out/'results';recovery=a.out/'recovery';binaries_dir=a.out/'bin'
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery.resolve():shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 for d in (results,recovery,binaries_dir):d.mkdir(exist_ok=True)
 inputs=recovery/'inputs';cache=recovery/'stage-cache'
 for d in (inputs,cache):d.mkdir(exist_ok=True)
 rp=results/'four-second-bockstein-pipeline-receipt.json'
 receipt={'format':'r150-four-second-bockstein-original-continuation-v1','status':'preparing','prime':31,'targetModulus':29791,'targetMultiplier':'H0=(s-2)*h0','fullOriginalMod29791IdentityVerified':False,'fourColumnsOnly':True,'remaining198DirectionsComputed':False,'fullSecondBocksteinImageClaimed':False,'characteristicZeroIdentityAsserted':False,'oldGraphOriginalNFOrFirstBocksteinRecomputed':False,'sharedMathematicalSecondsLimit':a.math_seconds,'perChildAddressSpaceMiBLimit':a.memory_mib,'perCompilationSecondsLimit':a.compile_seconds,'deadlineRule':'Validation, lossless input conversion and individually bounded compilation precede the timer. All new mathematical stages share one300-second deadline. Each child receives only the remaining time; a10-second SIGTERM checkpoint grace precedes forced kill. Final lossless compression and manifests follow outside the mathematical timer. Both VQ stages save actual arrays every100 rows and at termination boundaries. Content-bound complete stages can be reused from recovery.','inputs':{},'sources':{},'compilations':{},'stages':{}}
 def save():rp.write_text(json.dumps(receipt,indent=2)+'\n')
 def record(name,f,expected):
  if sha(f)!=expected:raise ValueError('exact frozen input SHA '+name)
  receipt['inputs'][name]={'file':str(f),'bytes':f.stat().st_size,'sha256':expected};return f
 found={};math_start=None
 try:
  for name,(names,expected) in ARTIFACT.items():
   candidates=sorted({p for n in names for p in a.t96_recovery.rglob(n) if p.is_file()})
   if name=='model':candidates+=sorted(notes.rglob('native-normal-form-input.txt'))
   good=next((p.resolve() for p in candidates if sha(p)==expected),None)
   if good is None:raise ValueError('missing original T96 artifact input '+name)
   found[name]=record(name,good,expected)
  for directory,entries in ((a.selected_inputs,{n:(p+'.gz',h) for n,(p,h) in SELECTED.items()}),(notes,NOTE_INPUTS)):
   for name,(relative,expected) in entries.items():
    f=inputs/(name+'.bin')
    with gzip.open(directory/relative,'rb') as src,f.open('wb') as dst:shutil.copyfileobj(src,dst)
    found[name]=record(name,f,expected)
  selected=json.loads((a.selected_inputs/'selection-receipt.json').read_text())
  if selected.get('status')!='completed' or selected.get('selectedHighKernelNumbers')!=[199,200,201,202] or selected.get('oldBocksteinRecomputed') is not False:raise ValueError('actual four-column byte selection receipt')
  shutil.copyfile(a.selected_inputs/'selection-receipt.json',results/'input-four-column-selection.json')
  for name,(relative,expected) in PLAIN_INPUTS.items():found[name]=record(name,notes/relative,expected)
  found['uniformX']=inputs/'actualX-uniform.bin';receipt['actualXHeaderConversion']=uniform_actual_x(found['actualX'],found['uniformX'])
  source_names=sorted({f for f,_ in CPP.values()}|{QUOTIENT,Path(__file__).name,'2026-11-14-r150-second-bockstein-common-789f.hpp'})
  for name in source_names:receipt['sources'][name]=sha(root/name)
  for name,expected in [('2026-11-14-r150-f31-bitplane-789f.hpp','73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec'),('2026-11-14-r150-torsion-characteristic-789f.py','8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2')]:
   if sha(notes/name)!=expected:raise ValueError('frozen shared implementation '+name)
   receipt['sources'][name]=expected
  labels4=list(range(4001,4005));labels9=list(range(2,11));oldlabels=list(range(2275,2279))
  beta={'nf':found['betaNF'],'q':found['betaQ'],'rem':found['betaRem'],'trace':found['betaTrace'],'labels':oldlabels,'polys':RELATIONS}
  first_mix=inputs/'four-relations.mix';write_mix(first_mix,labels4,87,[beta])
  executables={}
  for name,(file,flags) in CPP.items():
   exe=binaries_dir/name;command=['timeout','--kill-after=10s',f'{a.compile_seconds}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--','g++','-O3','-std=c++17','-I',str(root),'-I',str(notes)]+flags+[str(root/file),'-o',str(exe)]
   t=time.monotonic();r=subprocess.run(command,capture_output=True,text=True);(results/('compile-'+name+'.log')).write_text(r.stdout+r.stderr)
   receipt['compilations'][name]={'command':command,'exitCode':r.returncode,'elapsedSeconds':time.monotonic()-t};save()
   if r.returncode:raise RuntimeError('bounded compilation '+name)
   executables[name]=exe
  if a.prepare_only:receipt['status']='prepared-no-mathematics-executed';save();return
  math_start=time.monotonic();deadline=math_start+a.math_seconds;receipt['status']='running';save()
  def path(name):
   d=recovery/name;d.mkdir(exist_ok=True);return d/name
  def run_stage(name,command,marker,required,infiles,outfiles,logical):
   keyfields={'sources':receipt['sources'],'inputs':[sha(f) for f in infiles],'logical':logical};key=hashlib.sha256(json.dumps(keyfields,sort_keys=True,separators=(',',':')).encode()).hexdigest();saved=cache/(name+'.json')
   if saved.exists():
    old=json.loads(saved.read_text())
    if old.get('inputBindingSHA256')==key and all(f.exists() and sha(f)==old.get('outputs',{}).get(str(f.relative_to(recovery))) for f in outfiles):
     receipt['stages'][name]={'status':'completed','reusedCompletedActualStage':True,'inputBindingSHA256':key,'nativeStatistics':old['nativeStatistics'],'elapsedSeconds':0};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('shared deadline before '+name)
   bounded=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit',f'--as={a.memory_mib*1048576}','--core=0','--']+[str(c) for c in command]
   stage={'status':'running','inputBindingSHA256':key,'command':bounded,'remainingSecondsAtStart':remaining};receipt['stages'][name]=stage;save();t=time.monotonic();events=[]
   child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   with (results/(name+'.log')).open('w') as log:
    for line in child.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:event=json.loads(line);events.append(event);stage['lastProgress']=event;save()
     except (ValueError,TypeError):pass
   code=child.wait();last=events[-1] if events else {};complete=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items()) and all(f.exists() for f in outfiles)
   stage.update(status='completed' if complete else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-t,nativeStatistics=last);receipt['mathematicalElapsedSeconds']=time.monotonic()-math_start;save()
   if not complete:raise RuntimeError('actual stage failed or incomplete: '+name)
   saved.write_text(json.dumps({'inputBindingSHA256':key,'inputs':keyfields,'outputs':{str(f.relative_to(recovery)):sha(f) for f in outfiles},'nativeStatistics':last},indent=2)+'\n')
  def image_stage(name,mixfile,N,labels,families,infiles,require_zero):
   prefix=path(name);outs=[suffix(prefix,s) for s in ('-normal-forms.bin','-image-quotients.bin','-image-remainders.bin','-image-certificate.json')]
   required={'fullImageQuotientIdentity':True}
   if require_zero:required['completeRHSInImage']=True
   run_stage(name,[executables['image'],found['graph'],mixfile,prefix],'saved-quotient-mixture-complete',required,[found['graph']]+infiles,outs,{'bound':N,'labels':labels,'polynomials':families})
   return prefix
  def source_stage(name,image,nt,N):
   prefix=path(name);data=[found['graph'],found['originalNF'],suffix(image,'-normal-forms.bin'),suffix(image,'-image-quotients.bin'),suffix(image,'-image-remainders.bin')]
   binding=hashlib.sha256(json.dumps({'inputs':[sha(f) for f in data],'source':receipt['sources'][CPP['source4'][0]],'targets':nt},sort_keys=True,separators=(',',':')).encode()).hexdigest()
   run_stage(name,[executables['source'+str(nt)]]+data+[prefix,binding],'packed-image-source-convolution-complete',{'fullNormalFormDecompositionIdentity':True,'standardKernelNormalForm':True,'completeRHSInImage':True},data,[suffix(prefix,'-standard-coefficients.bin'),suffix(prefix,'-source-certificate.json'),suffix(prefix,'-vq-checkpoint.bin')],{'bound':N,'targets':nt,'checkpointBinding':binding})
   return prefix
  def transport_stage(name,source,mixfile,tracefiles,logic):
   prefix=path(name);data=[suffix(source,'-standard-coefficients.bin'),found['model'],found['normalTrace'],found['forward'],found['backward']]
   run_stage(name,[executables['transport']]+data+[mixfile,prefix],'original-source-transport-complete',{},data+tracefiles,[suffix(prefix,'-primitive-source-mod31.bin'),suffix(prefix,'-original-transport.json')],logic);return prefix
  first=image_stage('relations-image',first_mix,87,labels4,RELATIONS,[found[k] for k in ('betaNF','betaQ','betaRem')],True)
  firstsource=source_stage('relations-source',first,4,87)
  firstoriginal=transport_stage('relations-original',firstsource,first_mix,[found['betaTrace']],{'relations':RELATIONS,'bound':87})
  qmeta=json.loads(suffix(firstoriginal,'-original-transport.json').read_text());delta_bound=max([87]+qmeta['sourceCosts'])
  if delta_bound>183:raise ValueError('first four actual source exceeds proved87+96 bound')
  delta=path('delta-original');delta_recipe=inputs/'delta-original.recipe'
  write_original(delta_recipe,labels4,delta_bound,961,0,[{'file':found['kernels'],'labels':oldlabels,'polys':RELATIONS},{'file':suffix(firstoriginal,'-primitive-source-mod31.bin'),'labels':labels4,'polys':identity(4,-31)}])
  run_stage('delta-original',[executables['original'],found['model'],found['integerModel'],delta_recipe,delta],'full-original-combination-complete',{'divisor':961,'allOriginalProductCoefficientsDivisible':True},[found['model'],found['integerModel'],found['kernels'],suffix(firstoriginal,'-primitive-source-mod31.bin')],[suffix(delta,s) for s in ('-primitive-source-mod29791.bin','-original-seventeen-source-mod29791.bin','-divided-original-rhs.bin','-original-product.json')],{'bound':delta_bound,'relations':RELATIONS,'correction':-31})
  normal=path('delta-normal');run_stage('delta-normal',[executables['normal'],found['model'],suffix(delta,'-divided-original-rhs.bin'),normal],'four-second-bockstein-original-normal-forms-complete',{'targets':4,'components':1034},[found['model'],suffix(delta,'-divided-original-rhs.bin')],[suffix(normal,s) for s in ('-normal-forms.bin','-reduction.bin','-forward.bin','-backward.bin')],{'bound':delta_bound,'labels':labels4})
  if sha(suffix(normal,'-forward.bin'))!=ARTIFACT['forward'][1] or sha(suffix(normal,'-backward.bin'))!=ARTIFACT['backward'][1]:raise ValueError('new RHS did not use identical original prebasis DAG')
  delta_mix=inputs/'delta-image.mix';fresh={'nf':suffix(normal,'-normal-forms.bin'),'q':'-','rem':'-','trace':suffix(normal,'-reduction.bin'),'labels':labels4,'polys':identity(4)};write_mix(delta_mix,labels4,delta_bound,[fresh])
  deltaimage=image_stage('delta-image',delta_mix,delta_bound,labels4,identity(4),[suffix(normal,'-normal-forms.bin')],False)
  testdir=recovery/'quotient-test';testdir.mkdir(exist_ok=True)
  run_stage('quotient-test',['python',root/QUOTIENT,'--notes-root',notes,'--first-system',found['firstSystem'],'--second-system',found['secondSystem'],'--original-metadata',suffix(delta,'-original-product.json'),'--image-metadata',suffix(deltaimage,'-image-certificate.json'),'--image-quotients',suffix(deltaimage,'-image-quotients.bin'),'--image-remainders',suffix(deltaimage,'-image-remainders.bin'),'--out',testdir],'completed',{'remaining198DirectionsComputed':False},[found['firstSystem'],found['secondSystem'],suffix(delta,'-original-product.json'),suffix(deltaimage,'-image-certificate.json'),suffix(deltaimage,'-image-quotients.bin'),suffix(deltaimage,'-image-remainders.bin')],[testdir/'four-second-bockstein-result.json',testdir/'four-second-bockstein-system.bin.gz'],{'fourLabels':labels4})
  test=json.loads((testdir/'four-second-bockstein-result.json').read_text());receipt['fourColumnQuotientConclusion']=test;save()
  if not test['allNineCompatible']:
   receipt.update(status='completed',outcome='four-column-insufficiency-only',mathematicalElapsedSeconds=time.monotonic()-math_start,remaining198DirectionsRequired=True);save();return
  polys=test['solutionPolynomialsAscending'];dpolys=polys[:4];fpolys=polys[4:]+[[[] for _ in range(9)] for _ in range(2)]
  final_bound=max([86]+[delta_bound+len(p)-1 for row in dpolys for p in row if p]+[85+len(p)-1 for row in fpolys[:2] for p in row if p])
  if final_bound>498:raise ValueError('full315 polynomial multiplier budget exceeded')
  r2family={'nf':found['r2NF'],'q':found['r2Q'],'rem':found['r2Rem'],'trace':found['r2Trace'],'labels':labels9,'polys':identity(9)}
  deltafamily={'nf':suffix(normal,'-normal-forms.bin'),'q':suffix(deltaimage,'-image-quotients.bin'),'rem':suffix(deltaimage,'-image-remainders.bin'),'trace':suffix(normal,'-reduction.bin'),'labels':labels4,'polys':[[[-a for a in p] for p in row] for row in dpolys]}
  betafinal={**beta,'polys':[[[-a for a in p] for p in row] for row in fpolys]}
  final_mix=inputs/'nine-correction.mix';write_mix(final_mix,labels9,final_bound,[r2family,deltafamily,betafinal])
  imagefiles=[f[k] for f in (r2family,deltafamily,betafinal) for k in ('nf','q','rem')]
  finalimage=image_stage('nine-image',final_mix,final_bound,labels9,[f['polys'] for f in (r2family,deltafamily,betafinal)],imagefiles,True)
  finalsource=source_stage('nine-source',finalimage,9,final_bound)
  finaloriginal=transport_stage('nine-original',finalsource,final_mix,[f['trace'] for f in (r2family,deltafamily,betafinal)],{'bound':final_bound,'polynomials':[f['polys'] for f in (r2family,deltafamily,betafinal)]})
  zmeta=json.loads(suffix(finaloriginal,'-original-transport.json').read_text());paid_bound=max([final_bound]+zmeta['sourceCosts'])
  final_recipe=inputs/'nine-final-original.recipe';final=path('final-original')
  write_original(final_recipe,labels9,paid_bound,29791,1,[{'file':found['uniformX'],'labels':labels9,'polys':identity(9)},{'file':suffix(delta,'-primitive-source-mod29791.bin'),'labels':labels4,'polys':dpolys},{'file':found['kernels'],'labels':oldlabels,'polys':[[[31*a for a in p] for p in row] for row in fpolys]},{'file':suffix(finaloriginal,'-primitive-source-mod31.bin'),'labels':labels9,'polys':identity(9,961)}])
  run_stage('final-original',[executables['original'],found['model'],found['integerModel'],final_recipe,final],'full-original-combination-complete',{'divisor':29791,'allOriginalProductCoefficientsDivisible':True,'fullOriginalSeventeenEquationIdentityMod29791':True},[found['model'],found['integerModel'],found['uniformX'],found['kernels'],suffix(delta,'-primitive-source-mod29791.bin'),suffix(finaloriginal,'-primitive-source-mod31.bin')],[suffix(final,s) for s in ('-primitive-source-mod29791.bin','-original-seventeen-source-mod29791.bin','-original-product.json')],{'bound':paid_bound,'deltaPolynomials':dpolys,'betaPolynomials':fpolys})
  receipt['originalSeventeenConclusion']=json.loads(suffix(final,'-original-product.json').read_text());receipt.update(status='completed',outcome='full-original-mod29791-certificate',fullOriginalMod29791IdentityVerified=True,finite_budget_verified=True,mathematicalElapsedSeconds=time.monotonic()-math_start);save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc))
  if math_start is not None:receipt['mathematicalElapsedSeconds']=time.monotonic()-math_start
  save()
 finally:
  # Preserve every actual output and partial VQ array, with lossless parts below
  # the decimal5MB repository limit. Input copies remain in the recovery artifact.
  certificates=results/'certificates';certificates.mkdir(exist_ok=True);files=[]
  for f in sorted(recovery.rglob('*.bin')):
   if f.is_relative_to(inputs):continue
   relative=f.relative_to(recovery);name=str(relative).replace('/','__');tmp=recovery/(name+'.gz.tmp')
   with f.open('rb') as src,tmp.open('wb') as dst:
    with gzip.GzipFile(filename='',mode='wb',fileobj=dst,mtime=0) as zipped:shutil.copyfileobj(src,zipped)
   item={'originalFile':str(relative),'uncompressedBytes':f.stat().st_size,'uncompressedSHA256':sha(f),'compressedBytes':tmp.stat().st_size,'compressedSHA256':sha(tmp),'parts':[]}
   with tmp.open('rb') as source:
    part=1
    while block:=source.read(4_500_000):
     dest=certificates/(name+'.gz' if item['compressedBytes']<=4_500_000 else name+f'.gz.part{part:03d}');dest.write_bytes(block);item['parts'].append({'file':str(dest.relative_to(results)),'bytes':len(block),'sha256':hashlib.sha256(block).hexdigest()});part+=1
   tmp.unlink();files.append(item)
  for f in sorted(recovery.rglob('*.json')):
   if not f.is_relative_to(inputs) and not f.is_relative_to(cache):shutil.copyfile(f,results/str(f.relative_to(recovery)).replace('/','__'))
  for f in sorted((recovery/'quotient-test').glob('*.bin.gz')) if (recovery/'quotient-test').exists() else []:shutil.copyfile(f,results/f.name)
  (results/'certificate-manifest.json').write_text(json.dumps({'format':'r150-four-delta2-complete-generated-certificates-v1','pipelineStatus':receipt['status'],'partialCheckpointIsNotIdentity':True,'files':files},indent=2)+'\n')
  recovery_files=[{'file':str(f.relative_to(recovery)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(recovery.rglob('*')) if f.is_file()]
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-four-delta2-full-recovery-v1','pipelineStatus':receipt['status'],'files':recovery_files},indent=2)+'\n')
  receipt['recoveryFiles']=len(recovery_files);receipt['recoveryBytes']=sum(f['bytes'] for f in recovery_files);receipt['losslessGeneratedBinaryFiles']=len(files);save()
  print(json.dumps({k:receipt.get(k) for k in ('status','outcome','mathematicalElapsedSeconds','fullOriginalMod29791IdentityVerified','remaining198DirectionsComputed','remaining198DirectionsRequired','recoveryBytes')}),flush=True)
 if receipt['status']!='completed':raise SystemExit(1)
if __name__=='__main__':main()
