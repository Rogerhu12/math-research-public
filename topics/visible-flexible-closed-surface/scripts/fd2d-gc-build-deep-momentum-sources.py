#!/usr/bin/env python3
"""Create named arithmetic forks; never alter archived numerical sources."""
import argparse
import hashlib
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--verified-sources', type=Path, required=True)
a = p.parse_args()
here = Path(__file__).resolve().parent
inputs, outputs = {}, {}

def read(name, external=False):
    path = (a.verified_sources if external else here) / name
    data = path.read_bytes()
    inputs[str(path)] = hashlib.sha256(data).hexdigest()
    return data.decode()

def replace(text, old, new, count=1):
    found = text.count(old)
    if found != count:
        raise RuntimeError(f'Expected {count}, got {found}: {old[:90]}')
    return text.replace(old, new)

def save(name, text):
    path = here / name
    if path.exists() and path.read_text() != text:
        raise RuntimeError(f'Refuse to replace an existing different arithmetic fork: {path}')
    path.write_text(text)
    outputs[name] = hashlib.sha256(text.encode()).hexdigest()

root = read('general_root_tail_momentum.mjs', True)
root = replace(root, 'import {createRawTailEngine} from "./general_exact_tail_cauchy_raw.mjs";',
'''// Deep arithmetic fork: same finite root, branch floor, and stopping thresholds.
import {loadClosingTailSource} from './closing_tail_sources.mjs';
import {momentumGeometry,deepWeightedTerms} from './fd2d-gc-tail-deep-factors.mjs';
const {createRawTailEngine}=await loadClosingTailSource('general_exact_tail_cauchy_raw.mjs');''')
root = replace(root, ' const legacy=createRawTailEngine({modes:M,quadrature:N,spacing,projectionFloor:floor});',
               ' let legacy=null; // Allocate legacy diagnostics only if explicitly requested.')
start = root.index(' function geometry(profile,x){')
end = root.index(' function data(Q,g){', start)
root = root[:start] + ' function geometry(profile,x){return momentumGeometry(profile,x,{mu,orientation});}\n' + root[end:]
root = replace(root, 'p[j]=-freq[j]*g.r**3*Q[j]/(sq2*g.w);',
               'p[j]=g.deepScaled?-freq[j]*g.momentumPFactor*Q[j]:-freq[j]*g.r**3*Q[j]/(sq2*g.w);')
root = replace(root,
 'const K=Lv-Pt,T=2*K+K*K+g.E*P*P,u=g.w2*T,D=1-u,S=1-g.w2*P*P,A=1+Lv+g.w2*Pt;',
 '''const K=Lv-Pt,T=2*K+K*K+g.E*P*P,z=g.deepScaled?deepWeightedTerms(g,K,P,Pt,Lv):null,
    u=z?z.u:g.w2*T,D=1-u,S=z?z.S:1-g.w2*P*P,A=z?z.A:1+Lv+g.w2*Pt;''')
root = replace(root, 'const gc=g.w2*(P*P+S*T/(1+sd))/(S*sd);',
               'const gc=z?(z.wp*z.wp+S*u/(1+sd))/(S*sd):g.w2*(P*P+S*T/(1+sd))/(S*sd);')
root = replace(root, 'const q=.5*(K*K+g.E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc;',
 '''const q=.5*(K*K+g.E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc;
   if(!Number.isFinite(q))throw Error('Momentum projected quadratic outside binary64 range');''')
root = replace(root, 'const am=Lv+g.w2*Pt,bm=', 'const am=Lv+(z?g.w*z.wpt:g.w2*Pt),bm=')
root = replace(root, 'const f=orientation*sq12*mu/(sq2*g.r**4*g.w2);', 'const f=g.momentumTargetFactor;')
root = replace(root, 'const f=orientation*sq2*g.r**4*g.w2/(sq12*mu);', 'const f=g.momentumInverseFactor;')
root = replace(root, 'const pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu);', 'const pref=g.momentumFluxFactor;', 2)
root = replace(root, 'const diag=legacy.rhs(old,profile,x,true);',
 '''if(g.deepScaled)throw Error('Use the actual deep physical-jet evaluator, not legacy raw diagnostics');
  legacy??=createRawTailEngine({modes:M,quadrature:N,spacing,projectionFloor:floor});
  const diag=legacy.rhs(old,profile,x,true);''')
root = replace(root, 'const rt=root(state,profile,x),g=rt.g,Kdim=2*M,sigma=g.drdx/g.r;',
 '''const rt=root(state,profile,x),g=rt.g,Kdim=2*M,sigma=g.drdx/g.r;
  if(g.deepScaled)throw Error('Use the combined Fourier-product Jacobian for a deep cell');''')
save('fd2d-gc-tail-deep-root.mjs', root)

split = read('f6tail_momentum_split_flux.mjs', True)
split = replace(split, "from './general_root_tail_momentum.mjs'", "from './fd2d-gc-tail-deep-root.mjs'")
split = replace(split, 'function rhs(state,profile,x,detail=false,knownRoot=null){',
                'function rhsWithComponents(state,profile,x,knownRoot=null){')
split = replace(split, 'pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu);',
                'pref=g.momentumFluxFactor,momentumFlux=new Float64Array(M);')
split = replace(split,
 '''const v=rt.e.rows[n],u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
        factor=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),''',
 '''const v=rt.e.rows[n],wp=g.w*v.P,wk=g.w*v.K,
        u=g.deepScaled?2*g.w*wk+wk*wk+g.E*wp*wp:g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
        wP2=g.deepScaled?wp*wp:g.w2*v.P*v.P,
        factor=(v.K+u/(1+v.sd)+wP2*v.sd)/(v.S*v.sd),''')
split = replace(split, 'p=-m*g.r**3*state[j]/(sq2*g.w),',
                'p=g.deepScaled?-m*g.momentumPFactor*state[j]:-m*g.r**3*state[j]/(sq2*g.w),')
split = replace(split, 'd[M+j]=4*sigma*state[M+j]+pref*m*(linearFlux+nonlinearFlux[j]);',
 '''momentumFlux[j]=linearFlux+nonlinearFlux[j];
      d[M+j]=4*sigma*state[M+j]+pref*m*momentumFlux[j];''')
split = replace(split,
 '''if(!detail)return d;
    return {...base.rhs(state,profile,x,true,rt),derivative:d,
      nonlinearFlux:Array.from(nonlinearFlux),splitFlux:true};''',
 '''return {derivative:d,momentumFlux,nonlinearFlux,root:rt};
  }
  function rhs(state,profile,x,detail=false,knownRoot=null){
    const f=rhsWithComponents(state,profile,x,knownRoot);
    if(!detail)return f.derivative;
    if(f.root.g.deepScaled)return {...f,splitFlux:true,legacyUnavailable:true};
    return {...base.rhs(state,profile,x,true,f.root),derivative:f.derivative,
      nonlinearFlux:Array.from(f.nonlinearFlux),momentumFlux:f.momentumFlux,splitFlux:true};''')
split = replace(split, 'return {...base,rhs,rk4,statistics};', 'return {...base,rhs,rhsWithComponents,rk4,statistics};')
save('fd2d-gc-tail-deep-split-flux.mjs', split)

jac = read('78718-tail-fourier-product-jacobian.mjs')
jac = replace(jac,
 'pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu),targetFac=orientation*sq12*mu/(sq2*g.r**4*g.w2),pFac=g.r**3/(sq2*g.w),',
 'pref=g.momentumFluxFactor,targetFac=g.momentumTargetFactor,pFac=g.momentumPFactor,')
old = '''const v=rt.e.rows[n],omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd),
    FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd),
    FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho,
    flux=(1+v.K)*v.U/(v.S*v.sd),CK=v.U/(v.S*v.sd)+flux*g.w2*(1+v.K)/v.D,
    u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),CU=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),
    CP=flux*(2*g.w2*v.P/v.S+g.w2*g.E*v.P/v.D),am=v.L+g.w2*v.Pt,
    bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));'''
new = '''const v=rt.e.rows[n];let FP,FT,CK,CU,CP,bm;
   if(!g.deepScaled){
    const omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd);
    FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd);
    FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho;
    const flux=(1+v.K)*v.U/(v.S*v.sd);CK=v.U/(v.S*v.sd)+flux*g.w2*(1+v.K)/v.D;
    const u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P);CU=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd);
    CP=flux*(2*g.w2*v.P/v.S+g.w2*g.E*v.P/v.D);
    const am=v.L+g.w2*v.Pt;bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
   }else{
    const wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,
     omega=1+g.w*(g.w*(v.L+v.quad)),rho=1/(v.D*v.sd),
     u=2*g.w*wk+wk*wk+g.E*wp*wp;
    FP=g.E*v.P*omega/v.D+2*(1+v.K)*wpt*wp/(v.S*v.S*v.sd);
    FT=-(g.E*v.Pt+(1+v.K)*(g.w*(g.w*wp*wp)+2*g.w*wk+wk*wk)/v.S)*rho;
    const flux=(1+v.K)*v.U/(v.S*v.sd);
    CK=v.U/(v.S*v.sd)+flux*g.w*(g.w*(1+v.K))/v.D;
    CU=(v.K+u/(1+v.sd)+wp*wp*v.sd)/(v.S*v.sd);
    CP=flux*(2*g.w*wp/v.S+g.w*g.E*wp/v.D);
    const am=v.L+g.w*wpt;bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
   }'''
jac = replace(jac, old, new)
jac = replace(jac, 'const right=new Float64Array(J*K),FL=',
 '''// For a deep cell solve B*(pref*dL)=pref*right directly.
  // pref*targetFac=dr/r; no vanishing pref or enormous dL is formed separately.
  const pf=g.deepScaled?g.momentumFluxTimesP:pFac,tf=g.deepScaled?sigma:targetFac;
  const right=new Float64Array(J*K),FL=''')
jac = replace(jac, 'right[i*K+j]=pFac*', 'right[i*K+j]=pf*')
jac = replace(jac, 'right[i*K+M+j]=-targetFac*', 'right[i*K+M+j]=-tf*')
jac = replace(jac, 'FQ[i*M+j]=pFac*', 'FQ[i*M+j]=pf*')
jac = replace(jac,
 '''for(let j=0;j<M;j++)for(let col=0;col<K;col++){
   let df=-freq[j]*dL''',
 '''if(g.deepScaled){
   for(let j=0;j<M;j++)for(let col=0;col<K;col++){
    const f=freq[j];
    let pdf=-f*dL[(j+1)*K+col]+(col<M?FQ[j*M+col]:FL[j*J+col-M+1]*sigma);
    for(let i=0;i<J;i++)pdf+=FL[j*J+i]*dL[i*K+col];
    jacobian[j*K+col]=(col===j?(f*f-4)*sigma:0)+g.momentumScaledQFactor*dL[(j+1)*K+col]+(col===M+j?g.momentumLinearPiQFactor:0);
    jacobian[(M+j)*K+col]=(col===M+j?(4-f*f)*sigma:0)+(col===j?-g.momentumFluxTimesP*f*f*(f*f-1):0)+f*pdf;
   }
   for(let col=0;col<K;col++)jacobian[2*M*K+col]=g.momentumScaledMeanFactor*dL[col];
   if(!jacobian.every(Number.isFinite))throw Error('Combined momentum Jacobian outside binary64 range');
   return {derivative,jacobian,root:rt};
  }
  for(let j=0;j<M;j++)for(let col=0;col<K;col++){
   let df=-freq[j]*dL''')
save('fd2d-gc-tail-deep-product-jacobian.mjs', jac)

flow=read('78718-tail-fourier-product-flow.mjs')
flow=replace(flow, "from './78718-tail-fourier-product-jacobian.mjs'", "from './fd2d-gc-tail-deep-product-jacobian.mjs'")
save('fd2d-gc-tail-deep-product-flow.mjs',flow)

retr=read('78718-tail-geometric-newton-retraction.mjs')
retr=replace(retr,'targetFactor=orientation*sq12*mu/(sq2*g.r**4*g.w2),','targetFactor=g.momentumTargetFactor,')
retr=replace(retr,'pFactor=g.r**3/(sq2*g.w),','pFactor=g.momentumPFactor,')
old='''const v=rt.e.rows[n],omega=1+g.w2*(v.L+v.quad),invD32=1/(v.D*v.sd),
   FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd),
   FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*invD32;'''
new='''const v=rt.e.rows[n],wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,
   omega=1+(g.deepScaled?g.w*(g.w*(v.L+v.quad)):g.w2*(v.L+v.quad)),invD32=1/(v.D*v.sd),
   FP=g.E*v.P*omega/v.D+(g.deepScaled?2*(1+v.K)*wpt*wp:2*g.w2*(1+v.K)*v.Pt*v.P)/(v.S*v.S*v.sd),
   FT=-(g.E*v.Pt+(g.deepScaled?(1+v.K)*(g.w*(g.w*wp*wp)+2*g.w*wk+wk*wk):g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K))/v.S)*invD32;'''
retr=replace(retr,old,new)
save('fd2d-gc-tail-deep-retraction-differential.mjs',retr)
retr2=read('78718-tail-geometric-newton-retraction-v2.mjs')
retr2=replace(retr2,"from './78718-tail-geometric-newton-retraction.mjs'","from './fd2d-gc-tail-deep-retraction-differential.mjs'")
retr2=replace(retr2,'factor=orientation*sq2*g.r**4*g.w2/(sq12*mu);','factor=g.momentumInverseFactor;')
save('fd2d-gc-tail-deep-retraction-mean.mjs',retr2)
retr3=read('78718-tail-geometric-newton-retraction-centered-v3.mjs')
retr3=replace(retr3,"from './78718-tail-geometric-newton-retraction.mjs'","from './fd2d-gc-tail-deep-retraction-differential.mjs'")
retr3=replace(retr3,"from './78718-tail-geometric-newton-retraction-v2.mjs'","from './fd2d-gc-tail-deep-retraction-mean.mjs'",2)
save('fd2d-gc-tail-deep-retraction-centered.mjs',retr3)

core=read('fd2d-gc-tail-full160-cached-core.mjs')
core=replace(core,
 "const {createMomentumTailEngine}=await import(sourceURL('general_root_tail_momentum.mjs'));\nconst {createFastMomentumTailEngine}=await import(sourceURL('f6tail_fast_momentum.mjs'));",
 "import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';")
core=replace(core,
 "const {createMomentumPhysicalJetEvaluator}=await import(sourceURL('f6tail_momentum_physical_jets.mjs'));",
 "import {createMomentumPhysicalJetEvaluator} from './fd2d-metric-deep-momentum-physical-jets.mjs';")
core=replace(core,'const engineFactory=fastJacobian?createFastMomentumTailEngine:createMomentumTailEngine;',
             'const engineFactory=createDeepSplitMomentumEngine;')
core=replace(core,'Math.abs(t.darboux*g.E*g.E*g.r*g.drdx/g.w2)',
             'Math.abs(t.normalizedDarboux)')
save('fd2d-gc-tail-deep-cached-core.mjs',core)

split_wrapper=read('fd2d-gc-tail-full160-cached-split.mjs')
start=split_wrapper.index("import {createCompactTailDN}")
end=split_wrapper.index('  dn.tail.parameters.rhsEvaluation=')
split_wrapper=split_wrapper[:start]+'''import {createCompactTailDN} from './fd2d-gc-tail-deep-cached-core.mjs';
export function createSplitFluxCompactTailDN(options={}){
  const dn=createCompactTailDN({...options,fastJacobian:true});
'''+split_wrapper[end:]
save('fd2d-gc-tail-deep-cached-split.mjs',split_wrapper)

worker=read('fd2d-gc-tail-partition-worker-v5.mjs')
worker='// v6: complete deep arithmetic and direct single-engine construction; physical equations unchanged.\n'+worker
worker=replace(worker,"from './fd2d-gc-tail-full160-cached-split.mjs'","from './fd2d-gc-tail-deep-cached-split.mjs'")
worker=replace(worker,"from './78718-tail-geometric-newton-retraction-centered-v3.mjs'","from './fd2d-gc-tail-deep-retraction-centered.mjs'")
worker=replace(worker,"import {createFourierProductVariationalEngine} from './78718-tail-fourier-product-flow.mjs';\n",'')
worker=replace(worker,
 "const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));",
 "import {createDeepSplitMomentumEngine as createFastSplitFluxMomentumTailEngine} from './fd2d-gc-tail-deep-engine.mjs';")
worker=replace(worker,"!['fourier','fourier-root'].includes(backend)","backend!=='fourier'")
worker=replace(worker,
 "const backendLabel=backend==='fourier-root'?'fourier-root-and-product-moments-v1':'fourier-product-moments-v1';",
 "const backendLabel='deep-combined-fourier-product-moments-v1';")
worker=replace(worker,
 "const createFourierRootSplitFluxEngine=backend==='fourier-root'?\n (await import('./78718-tail-fourier-root-split-engine.mjs')).createFourierRootSplitFluxEngine:null;\n",'')
worker=replace(worker,'pointsPerEntry:cfg.pointCachePerEntry??64','pointsPerEntry:cfg.pointCachePerEntry??8')
start=worker.index('const transformedEngines=new Set();')
end=worker.index('actualStageCache=createSequentialStageCache',start)
worker=worker[:start]+'''const transformedEngines=new Set(dn.tail.cells.map(cell=>cell.engine));
// The deep split/product engine is constructed once in the core. No second
// engine allocation or mutation is needed after cutJets captured its object.
'''+worker[end:]
save('fd2d-gc-tail-partition-worker-v6.mjs',worker)

print(json.dumps({'inputs':inputs,'outputs':outputs},indent=2))
