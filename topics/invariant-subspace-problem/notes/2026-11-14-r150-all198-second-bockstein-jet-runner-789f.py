#!/usr/bin/env python3
"""One bounded complete198 continuation, including real positive original17 lift.

Only T96 and old200 large artifacts are needed. Frozen four/H25/r2 inputs can
be restored from notes. All new mathematical stages share one300-second timer.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,shutil,struct,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'

BASE='2026-11-14-r150-second-bockstein-'
OLD_RUNNER='2026-11-14-r150-four-second-bockstein-runner-789f.py'
OLD_RUNNER_SHA='9fc1d9e6f64f520365bddea2d0d3387a32d42123f38efcf36f8798c9f36e6cba'
JET_TEST='2026-11-14-r150-all198-second-bockstein-jet-test-789f.py'
GLOBAL_TEST='2026-11-14-r150-all198-second-bockstein-global-check-789f.py'
OLD200={
 'oldK':('kernel-original-kernels.bin','ec067d86ce7c838697369d1f6a986c823de8564823d85b6684fe7a2926127a88'),
 'oldNF':('beta-normal-forms.bin','c1b0e2e79a52e312acb9a9b89a03c031a5d6bbd5afc34c862ff7c2ff35479b2b'),
 'oldTrace':('beta-reduction.bin','85105ff9a84a81c05b88ee09d1f3a8de4bd9a1e7faf5657889c74e95f4f441ae'),
 'oldQ':('image-image-quotients.bin','0bd81e4ae045daef1e224922ff0cceabd81436dc1680af29595ba2e169865338'),
 'oldRem':('image-image-remainders.bin','1f33a90bb81566e900dd2fc56d5cba50a853d73e3f927b288c0e19936b29d9de')}
FOUR={
 'fourK2':('delta-original-primitive-source-mod29791.bin','653867bccc606ec234c65eacfbb014fe14e055fcd50f2ea3f2506344d2aad8c7','delta-original'),
 'fourNF':('delta-normal-normal-forms.bin','517801d261d62f525aa35b7dfc461585a03550d659f4832f2b0438141ceae8b4','delta-normal'),
 'fourTrace':('delta-normal-reduction.bin','dd134dd6ea43939639a68cd93e62ea210f3e4fd68042d95c334484361535472c','delta-normal'),
 'fourQ':('delta-image-image-quotients.bin','fb7e33645c4f670889714fa357b3a52a8582352892835d6cf3c74336af1d6bcb','delta-image'),
 'fourRem':('delta-image-image-remainders.bin','84d0f30fc12a9d1c16c53dec6ebe5b2f11d0b97d58c076b456da355736f8404f','delta-image')}
CPP={
 'jet-vq':(BASE+'jet-vq-789f.cpp',[]),
 'jet-transport':(BASE+'jet-original-transport-789f.cpp',[]),
 'jet-product':(BASE+'jet-original-product-789f.cpp',[]),
 'jet-normal':(BASE+'jet-local-normal-789f.cpp',[]),
 'image':(BASE+'all198-global-image-mixture-789f.cpp',[]),
 'source9':(BASE+'source-checkpoint-789f.cpp',['-DR150_TARGETS=9']),
 'transport':(BASE+'all198-global-original-transport-789f.cpp',[]),
 'original':(BASE+'all198-global-original-combination-789f.cpp',[]),
 'normal':(BASE+'all198-global-normal-form-789f.cpp',[])}

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def suffix(p,s):return Path(str(p)+s)
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def negative(polys):return [[[-a for a in c] for c in row] for row in polys]
def scaled(polys,n):return [[[n*a for a in c] for c in row] for row in polys]

def main():
 p=argparse.ArgumentParser()
 for k in ('notes-root','t96-recovery','old200-recovery','four-recovery','h25-recovery','second-recovery','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--math-seconds',type=int,default=300);p.add_argument('--memory-mib',type=int,default=512);p.add_argument('--compile-seconds',type=int,default=30)
 p.add_argument('--resume-recovery',type=Path);p.add_argument('--prepare-only',action='store_true');a=p.parse_args()
 if min(a.math_seconds,a.memory_mib,a.compile_seconds)<1:raise ValueError('explicit positive resource bounds')
 root=Path(__file__).resolve().parent;notes=a.notes_root.resolve();a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
 if sha(root/OLD_RUNNER)!=OLD_RUNNER_SHA:raise ValueError('frozen old lossless input/recipe helper')
 spec=importlib.util.spec_from_file_location('r150_frozen_four_helper',root/OLD_RUNNER);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
 results=a.out/'results';recovery=a.out/'recovery';binarydir=a.out/'bin'
 if a.resume_recovery and a.resume_recovery.resolve()!=recovery.resolve():shutil.copytree(a.resume_recovery,recovery,dirs_exist_ok=True)
 for d in (results,recovery,binarydir):d.mkdir(exist_ok=True)
 inputs=recovery/'inputs';cache=recovery/'stage-cache'
 for d in (inputs,cache):d.mkdir(exist_ok=True)
 receipt_path=results/'all198-second-bockstein-jet-pipeline-receipt.json'
 receipt={'format':'r150-all198-complete-primary-second-bockstein-original-continuation-v1','status':'preparing','prime':31,'targetModulus':29791,'targetMultiplier':'H0=(s-2)*h0',
 'fullOriginalMod29791IdentityVerified':False,'finite_budget_verified':False,'relevantPrimaryImageComplete':False,'all198Coverage':False,'old4Coverage':True,'low1632Coverage':True,
 'remaining198DirectionsComputed':False,'fullGlobal315SecondImageClaimed':False,'characteristicZeroIdentityAsserted':False,'oldGraphOriginalNFOrFirstBocksteinRecomputed':False,
 'sharedMathematicalSecondsLimit':a.math_seconds,'perChildAddressSpaceMiBLimit':a.memory_mib,'perCompilationSecondsLimit':a.compile_seconds,
 'deadlineRule':'Frozen input verification/lossless decoding and bounded compilation precede the clock. Every new native or matrix stage shares one mathematical deadline. SIGTERM has10seconds to save actual arrays before forced kill. Complete stages have content-bound caches. Generated output compression and recovery manifests follow outside the mathematical clock.',
 'inputs':{},'sources':{},'compilations':{},'stages':{}}
 def save():receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
 found={};math_start=None
 def record(name,path,expected):
  if sha(path)!=expected:raise ValueError('frozen input SHA '+name)
  receipt['inputs'][name]={'file':str(path),'bytes':path.stat().st_size,'sha256':expected};return path
 def locate(name,directories,names,expected,fallback=None):
  existing=inputs/(name+'.bin')
  if existing.exists() and sha(existing)==expected:return record(name,existing,expected)
  candidates=[]
  for directory in directories:
   for file in names:candidates.extend(directory.rglob(file))
  for candidate in sorted(set(candidates)):
   if candidate.is_file() and sha(candidate)==expected:return record(name,candidate.resolve(),expected)
  if fallback is not None:
   source=notes/fallback
   with gzip.open(source,'rb') as src,existing.open('wb') as dst:shutil.copyfileobj(src,dst)
   return record(name,existing,expected)
  raise ValueError('missing exact frozen input '+name)
 try:
  for name,(names,expected) in old.ARTIFACT.items():
   directories=[a.t96_recovery]+([notes] if name=='model' else [])
   found[name]=locate(name,directories,names,expected)
  for name,(filename,expected) in OLD200.items():found[name]=locate(name,[a.old200_recovery],[filename],expected)
  for name,(filename,expected) in old.SELECTED.items():
   found[name]=locate(name,[a.four_recovery],[filename],expected,'r150-four-second-bockstein-inputs-789f/'+filename+'.gz')
  for name,(relative,expected) in old.NOTE_INPUTS.items():
   names={'actualX':['h25-primitive-source-mod961.bin'],'r2NF':['second-normal-forms.bin'],'r2Q':['second-image-quotients.bin'],'r2Rem':['second-image-remainders.bin'],'r2Trace':['second-reduction.bin']}[name]
   found[name]=locate(name,[a.h25_recovery if name=='actualX' else a.second_recovery],names,expected,relative)
  for name,(relative,expected) in old.PLAIN_INPUTS.items():found[name]=record(name,notes/relative,expected)
  for name,(filename,expected,stage) in FOUR.items():found[name]=locate(name,[a.four_recovery],[filename],expected,'r150-four-second-bockstein-actions-789f/43615783424-1/certificates/'+stage+'__'+filename+'.gz')
  found['fourSystem']=record('fourSystem',notes/'r150-four-second-bockstein-actions-789f/43615783424-1/four-second-bockstein-system.bin.gz','57a5c3314281fd82cd4ba306b7d9c015a543b8aae05fd2713b50b303ca059f2d')
  for name,file,expected in [('jetMap','jet-quotient-map.bin','3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716'),('jetMapReceipt','jet-quotient-map-receipt.json','5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df')]:found[name]=record(name,notes/'r150-second-bockstein-jet-quotient-map-789f'/file,expected)
  found['uniformX']=inputs/'actualX-uniform.bin';receipt['actualXHeaderConversion']=old.uniform_actual_x(found['actualX'],found['uniformX'])
  with found['oldK'].open('rb') as f:
   header=f.read(24+200*16)
  if header[:8]!=b'R150KK31' or struct.unpack_from('<4I',header,8)!=(31,6188,200,85):raise ValueError('same original200 kernel header')
  oldlabels=[struct.unpack_from('<IHHII',header,24+16*j)[1] for j in range(200)]
  b=found['oldRem'].read_bytes();off=20
  if b[:8]!=b'R150NF31' or struct.unpack_from('<3I',b,8)!=(0,200,1034):raise ValueError('saved original200 remainder header')
  for j in range(200):
   raw,label,n=struct.unpack_from('<IHI',b,off);off+=10
   if raw or label!=oldlabels[j] or (j<198 and n):raise ValueError('first198 actual saved beta remainders must be exactly zero')
   for _ in range(n):c,length=struct.unpack_from('<HB',b,off);off+=3+length
  if off!=len(b):raise ValueError('all200 remainder file tail')
  receipt['first198SavedRemaindersExactlyZero']=True
  source_names={file for file,_ in CPP.values()}|{JET_TEST,GLOBAL_TEST,Path(__file__).name,OLD_RUNNER,BASE+'jet-common-789f.hpp',BASE+'common-789f.hpp',BASE+'all198-global-common-789f.hpp'}
  for name in sorted(source_names):receipt['sources'][name]=sha(root/name)
  for name,expected in [('2026-11-14-r150-f31-bitplane-789f.hpp','73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec'),('2026-11-14-r150-torsion-characteristic-789f.py','8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2')]:
   if sha(notes/name)!=expected:raise ValueError('same shared source '+name)
   receipt['sources'][name]=expected
  executables={};executable_sources={}
  for name,(file,flags) in CPP.items():
   exe=binarydir/name;command=['timeout','--kill-after=10s',str(a.compile_seconds)+'s','prlimit','--as='+str(a.memory_mib*1048576),'--core=0','--','g++','-O3','-std=c++17','-I',str(root),'-I',str(notes)]+flags+[str(root/file),'-o',str(exe)]
   start=time.monotonic();run=subprocess.run(command,capture_output=True,text=True);(results/('compile-'+name+'.log')).write_text(run.stdout+run.stderr)
   receipt['compilations'][name]={'command':command,'exitCode':run.returncode,'elapsedSeconds':time.monotonic()-start};save()
   if run.returncode:raise RuntimeError('bounded compilation failed '+name)
   executables[name]=exe;executable_sources[str(exe)]=file
  if a.prepare_only:receipt['status']='prepared-no-mathematics-executed';save();return
  math_start=time.monotonic();deadline=math_start+a.math_seconds;receipt['status']='running';save()
  def path(name):
   directory=recovery/name;directory.mkdir(exist_ok=True);return directory/name
  def binding(infiles,logical,program):
   return digest({'inputs':[sha(f) for f in infiles],'logical':logical,'program':receipt['sources'][program],
                  'headers':{k:v for k,v in receipt['sources'].items() if k.endswith('.hpp')}})
  def run_stage(name,command,marker,required,infiles,outfiles,logical):
   program=executable_sources.get(str(command[0]),Path(command[1]).name if str(command[0])=='python' else None)
   if program not in receipt['sources']:raise ValueError('stage must identify its frozen code')
   key=binding(infiles,logical,program);saved=cache/(name+'.json')
   if saved.exists():
    oldcache=json.loads(saved.read_text())
    if oldcache.get('inputBindingSHA256')==key and all(f.exists() and sha(f)==oldcache.get('outputs',{}).get(str(f.relative_to(recovery))) for f in outfiles):
     receipt['stages'][name]={'status':'completed','reusedCompletedActualStage':True,'inputBindingSHA256':key,'nativeStatistics':oldcache['nativeStatistics'],'elapsedSeconds':0};save();return
   remaining=deadline-time.monotonic()
   if remaining<=0:raise TimeoutError('shared mathematical deadline before '+name)
   bounded=['timeout','--kill-after=10s',f'{remaining:.3f}s','prlimit','--as='+str(a.memory_mib*1048576),'--core=0','--']+[str(c) for c in command]
   stage={'status':'running','inputBindingSHA256':key,'command':bounded,'remainingSecondsAtStart':remaining};receipt['stages'][name]=stage;save();start=time.monotonic();events=[]
   child=subprocess.Popen(bounded,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   with (results/(name+'.log')).open('w') as log:
    for line in child.stdout:
     log.write(line);log.flush();print(line,end='',flush=True)
     try:event=json.loads(line);events.append(event);stage['lastProgress']=event;save()
     except (ValueError,TypeError):pass
   code=child.wait();last=events[-1] if events else {};complete=code==0 and last.get('status')==marker and all(last.get(k)==v for k,v in required.items()) and all(f.exists() for f in outfiles)
   stage.update(status='completed' if complete else 'failed-or-incomplete',exitCode=code,elapsedSeconds=time.monotonic()-start,nativeStatistics=last);receipt['mathematicalElapsedSeconds']=time.monotonic()-math_start;save()
   if not complete:raise RuntimeError('actual stage failed or incomplete '+name)
   saved.write_text(json.dumps({'inputBindingSHA256':key,'outputs':{str(f.relative_to(recovery)):sha(f) for f in outfiles},'nativeStatistics':last},indent=2)+'\n')
  jetkeys=['model','graph','oldK','oldQ','normalTrace','oldTrace','forward','backward','integerModel']
  jet_binding=digest({'inputs':{k:receipt['inputs'][k]['sha256'] for k in jetkeys},'sources':{k:v for k,v in receipt['sources'].items() if 'jet-' in k and k.endswith('.cpp') or k.endswith('.hpp')}})
  receipt['jetSourceInputBindingSHA256']=jet_binding;save()
  vq=path('jet-vq');run_stage('jet-vq',[executables['jet-vq'],found['model'],found['graph'],found['oldQ'],found['oldK'],vq,jet_binding],'same-global198-VQ-jets-complete',{},[found[k] for k in ('model','graph','oldQ','oldK')],[suffix(vq,s) for s in ('-original2195-source-jets.bin','-vq-checkpoint.bin','-vq.json')],{'jetBinding':jet_binding})
  transport=path('jet-transport');run_stage('jet-transport',[executables['jet-transport'],found['model'],found['oldK'],suffix(vq,'-original2195-source-jets.bin'),found['normalTrace'],found['oldTrace'],found['forward'],found['backward'],transport,jet_binding],'actual-global198-source-jet-transport-complete',{},[found[k] for k in ('model','oldK','normalTrace','oldTrace','forward','backward')]+[suffix(vq,'-original2195-source-jets.bin')],[suffix(transport,s) for s in ('-original6188-q-jets.bin','-transport-checkpoint.bin','-transport.json')],{'jetBinding':jet_binding})
  product=path('jet-product');run_stage('jet-product',[executables['jet-product'],found['model'],found['integerModel'],found['oldK'],suffix(transport,'-original6188-q-jets.bin'),product,jet_binding],'all198-original17-integer-jet-products-divided',{},[found[k] for k in ('model','integerModel','oldK')]+[suffix(transport,'-original6188-q-jets.bin')],[suffix(product,s) for s in ('-primitive-k2-jets-mod29791.bin','-original-seventeen-k2-jets-mod29791.bin','-divided-original-delta-jets.bin','-original-product.json')],{'jetBinding':jet_binding})
  normal=path('jet-normal');run_stage('jet-normal',[executables['jet-normal'],found['model'],suffix(product,'-divided-original-delta-jets.bin'),found['graph'],found['oldK'],normal,jet_binding],'all198-complete-original-local-normal-forms',{},[found[k] for k in ('model','graph','oldK')]+[suffix(product,'-divided-original-delta-jets.bin')],[suffix(normal,s) for s in ('-all198-standard-state.bin','-local-G-quotient-jets.bin','-local-prebasis-source-jets.bin','-normal-checkpoint.bin','-forward.bin','-backward.bin','-local-normal.json')],{'jetBinding':jet_binding})
  if sha(suffix(normal,'-forward.bin'))!=old.ARTIFACT['forward'][1] or sha(suffix(normal,'-backward.bin'))!=old.ARTIFACT['backward'][1]:raise ValueError('new local normal form must retain identical original prebasis DAG')
  testdir=recovery/'primary-test';testdir.mkdir(exist_ok=True)
  run_stage('primary-test',['python',root/JET_TEST,'--map',found['jetMap'],'--map-receipt',found['jetMapReceipt'],'--state',suffix(normal,'-all198-standard-state.bin'),'--product-metadata',suffix(product,'-original-product.json'),'--normal-metadata',suffix(normal,'-local-normal.json'),'--out',testdir],'completed',{},[found['jetMap'],found['jetMapReceipt'],suffix(normal,'-all198-standard-state.bin'),suffix(product,'-original-product.json'),suffix(normal,'-local-normal.json')],[testdir/'all198-second-primary-result.json',testdir/'all198-second-primary-system.bin.gz'],{'allHighKernelDirections':202,'exactLowDirections':1632})
  test=json.loads((testdir/'all198-second-primary-result.json').read_text());receipt['completePrimaryConclusion']=test
  for key in ('relevantPrimaryImageComplete','all198Coverage','old4Coverage','low1632Coverage','globallyObstructedTargetLabels','numberOfGloballyObstructedTargets','allNineGloballyObstructed'):receipt[key]=test[key]
  receipt['remaining198DirectionsComputed']=True;save()
  if not test['allNinePrimaryCompatible']:
   receipt.update(status='completed',outcome='complete-second-primary-obstruction',mathematicalElapsedSeconds=time.monotonic()-math_start);save();return
  # Continue a positive primary answer to actual global nine-column sources.
  labels9=list(range(2,11));labels4=list(range(4001,4005));betalabels=list(range(2275,2279));polys=test['solutionPolynomialsAscending']
  def image_stage(name,mixfile,N,families,required_zero):
   prefix=path(name);data=[found['graph']]+[f[k] for f in families for k in ('nf','q','rem') if f[k]!='-'];required={'fullImageQuotientIdentity':True}
   if required_zero:required['completeRHSInImage']=True
   run_stage(name,[executables['image'],found['graph'],mixfile,prefix],'saved-quotient-mixture-complete',required,data,[suffix(prefix,s) for s in ('-normal-forms.bin','-image-quotients.bin','-image-remainders.bin','-image-certificate.json')],{'bound':N,'labels':labels9,'polynomials':[f['polys'] for f in families]});return prefix
  def source_stage(name,image,N):
   prefix=path(name);data=[found['graph'],found['originalNF'],suffix(image,'-normal-forms.bin'),suffix(image,'-image-quotients.bin'),suffix(image,'-image-remainders.bin')];key=binding(data,{'bound':N,'targets':9},CPP['source9'][0])
   run_stage(name,[executables['source9']]+data+[prefix,key],'packed-image-source-convolution-complete',{'fullNormalFormDecompositionIdentity':True,'standardKernelNormalForm':True,'completeRHSInImage':True},data,[suffix(prefix,s) for s in ('-standard-coefficients.bin','-source-certificate.json','-vq-checkpoint.bin')],{'bound':N,'checkpointBinding':key});return prefix
  def original_transport(name,source,mixfile,N,families):
   prefix=path(name);data=[suffix(source,'-standard-coefficients.bin'),found['model'],found['normalTrace'],found['forward'],found['backward']]
   run_stage(name,[executables['transport']]+data+[mixfile,prefix],'original-source-transport-complete',{},data+[f['trace'] for f in families],[suffix(prefix,'-primitive-source-mod31.bin'),suffix(prefix,'-original-transport.json')],{'bound':N,'polynomials':[f['polys'] for f in families]});return prefix
  def product_stage(name,recipe,B,divisor,targetmode,families):
   prefix=path(name);data=[found['model'],found['integerModel']]+[f['file'] for f in families];logical={'bound':B,'divisor':divisor,'targetMode':targetmode,'polynomials':[f['polys'] for f in families]};key=binding(data,logical,CPP['original'][0]);outs=[suffix(prefix,s) for s in ('-primitive-source-mod29791.bin','-original-seventeen-source-mod29791.bin','-original-product.json')]
   if divisor==961:outs.append(suffix(prefix,'-divided-original-rhs.bin'))
   required={'divisor':divisor,'allOriginalProductCoefficientsDivisible':True}
   if targetmode:required['fullOriginalSeventeenEquationIdentityMod29791']=True
   run_stage(name,[executables['original'],found['model'],found['integerModel'],recipe,prefix,key],'full-original-combination-complete',required,data,outs,{**logical,'checkpointBinding':key});return prefix
  newpolys=polys[:198]+[[[] for j in range(9)] for _ in range(2)]
  selected={'nf':found['oldNF'],'q':found['oldQ'],'rem':found['oldRem'],'trace':found['oldTrace'],'labels':oldlabels,'polys':newpolys}
  selected_bound=max([40]+[(80 if i<160 else 81)+len(c)-1 for i,row in enumerate(newpolys[:198]) for c in row if c])
  if selected_bound>88:raise ValueError('selected198 combination cost exceeds81+7')
  selected_mix=inputs/'selected-nine-beta.mix';old.write_mix(selected_mix,labels9,selected_bound,[selected])
  selected_image=image_stage('selected-image',selected_mix,selected_bound,[selected],True)
  selected_source=source_stage('selected-source',selected_image,selected_bound)
  selected_original=original_transport('selected-original',selected_source,selected_mix,selected_bound,[selected])
  qmeta=json.loads(suffix(selected_original,'-original-transport.json').read_text());delta_bound=max([selected_bound]+qmeta['sourceCosts'])
  if delta_bound>184:raise ValueError('selected global q cost exceeds88+96')
  delta_families=[{'file':found['oldK'],'labels':oldlabels,'polys':newpolys},{'file':suffix(selected_original,'-primitive-source-mod31.bin'),'labels':labels9,'polys':old.identity(9,-31)}]
  delta_recipe=inputs/'selected-nine-delta.recipe';old.write_original(delta_recipe,labels9,delta_bound,961,0,delta_families)
  delta=product_stage('selected-delta',delta_recipe,delta_bound,961,0,delta_families)
  globalnormal=path('selected-normal');run_stage('selected-normal',[executables['normal'],found['model'],suffix(delta,'-divided-original-rhs.bin'),globalnormal],'nine-selected-global-second-normal-forms-complete',{'targets':9,'components':1034},[found['model'],suffix(delta,'-divided-original-rhs.bin')],[suffix(globalnormal,s) for s in ('-normal-forms.bin','-reduction.bin','-forward.bin','-backward.bin')],{'bound':delta_bound})
  if sha(suffix(globalnormal,'-forward.bin'))!=old.ARTIFACT['forward'][1] or sha(suffix(globalnormal,'-backward.bin'))!=old.ARTIFACT['backward'][1]:raise ValueError('selected global normal form changed original DAG')
  fresh={'nf':suffix(globalnormal,'-normal-forms.bin'),'q':'-','rem':'-','trace':suffix(globalnormal,'-reduction.bin'),'labels':labels9,'polys':old.identity(9)}
  delta_mix=inputs/'selected-delta-image.mix';old.write_mix(delta_mix,labels9,delta_bound,[fresh]);delta_image=image_stage('selected-delta-image',delta_mix,delta_bound,[fresh],False)
  globaldir=recovery/'global-check';globaldir.mkdir(exist_ok=True)
  run_stage('global-check',['python',root/GLOBAL_TEST,'--notes-root',notes,'--second-system',found['secondSystem'],'--four-system',found['fourSystem'],'--primary-result',testdir/'all198-second-primary-result.json','--original-metadata',suffix(delta,'-original-product.json'),'--image-metadata',suffix(delta_image,'-image-certificate.json'),'--image-remainders',suffix(delta_image,'-image-remainders.bin'),'--out',globaldir],'completed',{'all505GlobalObservationsVerified':True,'full315ProjectedDifferenceInCompleteFirstImage':True},[found['secondSystem'],found['fourSystem'],testdir/'all198-second-primary-result.json',suffix(delta,'-original-product.json'),suffix(delta_image,'-image-certificate.json'),suffix(delta_image,'-image-remainders.bin')],[globaldir/'selected-global315-result.json',globaldir/'selected-global315-reconciliation.bin.gz'],{'sameActualSelectedGlobalSources':True})
  actual=json.loads((globaldir/'selected-global315-result.json').read_text());receipt['actualGlobalReconciliation']=actual;save()
  P=actual['selectedNineGlobalProjectorAscending'];diagonalP=[[P if i==j else [] for j in range(9)] for i in range(9)];oldProjected=actual['oldFourProjectedPolynomialsAscending'];betapolys=actual['firstBetaCorrectionPolynomialsAscending'];final_bound=actual['finalRHSCostBound']
  r2={'nf':found['r2NF'],'q':found['r2Q'],'rem':found['r2Rem'],'trace':found['r2Trace'],'labels':labels9,'polys':old.identity(9)}
  newdelta={'nf':suffix(globalnormal,'-normal-forms.bin'),'q':suffix(delta_image,'-image-quotients.bin'),'rem':suffix(delta_image,'-image-remainders.bin'),'trace':suffix(globalnormal,'-reduction.bin'),'labels':labels9,'polys':negative(diagonalP)}
  olddelta={'nf':found['fourNF'],'q':found['fourQ'],'rem':found['fourRem'],'trace':found['fourTrace'],'labels':labels4,'polys':negative(oldProjected)}
  beta={'nf':found['betaNF'],'q':found['betaQ'],'rem':found['betaRem'],'trace':found['betaTrace'],'labels':betalabels,'polys':negative(betapolys)}
  finalfamilies=[r2,newdelta,olddelta,beta];final_mix=inputs/'final-nine-image.mix';old.write_mix(final_mix,labels9,final_bound,finalfamilies)
  final_image=image_stage('final-image',final_mix,final_bound,finalfamilies,True);final_source=source_stage('final-source',final_image,final_bound)
  final_original=original_transport('final-source-original',final_source,final_mix,final_bound,finalfamilies)
  zmeta=json.loads(suffix(final_original,'-original-transport.json').read_text());paid_bound=max([final_bound]+zmeta['sourceCosts'])
  if paid_bound>469:raise ValueError('paid global final source bound469 exceeded')
  final_sources=[{'file':found['uniformX'],'labels':labels9,'polys':old.identity(9)},
   {'file':suffix(delta,'-primitive-source-mod29791.bin'),'labels':labels9,'polys':diagonalP},
   {'file':found['fourK2'],'labels':labels4,'polys':oldProjected},
   {'file':found['kernels'],'labels':betalabels,'polys':scaled(betapolys,31)},
   {'file':suffix(final_original,'-primitive-source-mod31.bin'),'labels':labels9,'polys':old.identity(9,961)}]
  final_recipe=inputs/'final-nine-original.recipe';old.write_original(final_recipe,labels9,paid_bound,29791,1,final_sources)
  final=product_stage('final-original',final_recipe,paid_bound,29791,1,final_sources)
  receipt['originalSeventeenConclusion']=json.loads(suffix(final,'-original-product.json').read_text());receipt.update(status='completed',outcome='full-original-mod29791-certificate',fullOriginalMod29791IdentityVerified=True,finite_budget_verified=True,mathematicalElapsedSeconds=time.monotonic()-math_start);save()
 except Exception as exc:
  receipt.update(status='failed-or-incomplete',errorType=type(exc).__name__,error=str(exc))
  if math_start is not None:receipt['mathematicalElapsedSeconds']=time.monotonic()-math_start
  save()
 finally:
  certificates=results/'certificates';certificates.mkdir(exist_ok=True);files=[]
  for f in sorted(recovery.rglob('*.bin')):
   if f.is_relative_to(inputs):continue
   relative=f.relative_to(recovery);name=str(relative).replace('/','__');temp=recovery/(name+'.gz.tmp')
   with f.open('rb') as src,temp.open('wb') as dst:
    with gzip.GzipFile(filename='',mode='wb',fileobj=dst,mtime=0) as zipped:shutil.copyfileobj(src,zipped)
   item={'originalFile':str(relative),'uncompressedBytes':f.stat().st_size,'uncompressedSHA256':sha(f),'compressedBytes':temp.stat().st_size,'compressedSHA256':sha(temp),'parts':[]}
   with temp.open('rb') as src:
    n=1
    while block:=src.read(4_500_000):
     dest=certificates/(name+'.gz' if item['compressedBytes']<=4_500_000 else name+f'.gz.part{n:03d}');dest.write_bytes(block);item['parts'].append({'file':str(dest.relative_to(results)),'bytes':len(block),'sha256':hashlib.sha256(block).hexdigest()});n+=1
   temp.unlink();files.append(item)
  for f in sorted(recovery.rglob('*.json')):
   if not f.is_relative_to(inputs) and not f.is_relative_to(cache):shutil.copyfile(f,results/str(f.relative_to(recovery)).replace('/','__'))
  for folder in ('primary-test','global-check'):
   if (recovery/folder).exists():
    for f in (recovery/folder).glob('*.bin.gz'):shutil.copyfile(f,results/f.name)
  (results/'certificate-manifest.json').write_text(json.dumps({'format':'r150-all198-lossless-generated-certificate-manifest-v1','pipelineStatus':receipt['status'],'partialCheckpointIsNotIdentity':True,'files':files},indent=2)+'\n')
  allfiles=[{'file':str(f.relative_to(recovery)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(recovery.rglob('*')) if f.is_file()]
  (results/'recovery-manifest.json').write_text(json.dumps({'format':'r150-all198-complete-recovery-v1','pipelineStatus':receipt['status'],'files':allfiles},indent=2)+'\n')
  receipt.update(recoveryFiles=len(allfiles),recoveryBytes=sum(f['bytes'] for f in allfiles),losslessGeneratedBinaryFiles=len(files));save()
  print(json.dumps({k:receipt.get(k) for k in ('status','outcome','mathematicalElapsedSeconds','relevantPrimaryImageComplete','remaining198DirectionsComputed','globallyObstructedTargetLabels','allNineGloballyObstructed','fullOriginalMod29791IdentityVerified','recoveryBytes')}),flush=True)
 if receipt['status'] not in ('completed','prepared-no-mathematics-executed'):raise SystemExit(1)
if __name__=='__main__':main()
