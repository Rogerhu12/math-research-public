#!/usr/bin/env python3
"""Install exact cyclic reuse of the declared finite angular quadrature.

For d=gcd(N,spacing), all projected angular integrands have period N/d on
the declared N-point grid. Evaluate these N/d rows with weight d/N, retain
the original N guards/public N, and restore all N root rows by periodic
copying. Floating summation/trigonometric paths change; bit identity is not
claimed. Canonical source-root modules are read-only. No reflection folding,
root tolerance, D/S/A guard, shooting equation or final gate is changed.
"""
import argparse
import hashlib
import json
from pathlib import Path


def digest(text):return hashlib.sha256(text.encode()).hexdigest()


def replace(text,old,new,count=1):
    if text.count(old)!=count:raise ValueError('Unexpected source marker/count: '+old)
    return text.replace(old,new)


def external_import(symbol,filename):
    return ("import path from 'node:path';\nimport {pathToFileURL} from 'node:url';\n"
            "const periodicSourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;\n"
            "if(!periodicSourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');\n"
            f"const {{{symbol}}}=await import(pathToFileURL(path.join(periodicSourceRoot,"
            f"'topics/large-amplitude-twist-flex/scripts/{filename}')));")


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--manifest',type=Path,required=True)
    a=p.parse_args();topic=a.source_topic.resolve();scripts=topic/'scripts'
    root=topic/'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    names=['general_root_tail_momentum.mjs','f6tail_fast_momentum.mjs',
           'f6tail_momentum_split_flux.mjs','f6tail_fast_split_flux_engine.mjs']
    original={name:(root/name).read_text() for name in names};derived={}
    header='// Optional exact periodic quadrature reuse; declared N and all original guards retained.\n'

    name=names[0];s=original[name]
    s=replace(s,'import {createRawTailEngine} from "./general_exact_tail_cauchy_raw.mjs";',
              external_import('createRawTailEngine','general_exact_tail_cauchy_raw.mjs'))
    s=replace(s,' const J=M+1,size=2*M+2,sq2=Math.sqrt(2),sq12=Math.sqrt(12);',
              ' let ga=N,gb=spacing;while(gb!==0){const t=ga%gb;ga=gb;gb=t;}\n'
              ' const periodicMultiplicity=ga,nq=N/periodicMultiplicity;\n'
              ' const J=M+1,size=2*M+2,sq2=Math.sqrt(2),sq12=Math.sqrt(12);')
    head,body=s.split(' const legacy=',1)
    head=replace(head,'length:N','length:nq',2)
    head=replace(head,'for(let n=0;n<N;n++)','for(let n=0;n<nq;n++)')
    body=replace(body,'for(let n=0;n<N;n++)','for(let n=0;n<nq;n++)',4)
    body=replace(body,'/N','/nq',5)
    body=replace(body,'  if(needJac)for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];',
                 '  for(let n=nq;n<N;n++)rows.push({...rows[n%nq]});\n'
                 '  if(needJac)for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];')
    body=replace(body,'return {M,N,size,mu,orientation,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian};',
                 'return {M,N,size,mu,orientation,quadratureIndependentNodes:nq,quadraturePeriodMultiplicity:periodicMultiplicity,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian};')
    derived[name]=header+head+' const legacy='+body

    name=names[1];s=original[name]
    s=replace(s,"import {integrationGrid} from './f6tail_cusp_grid.mjs';",
              external_import('integrationGrid','f6tail_cusp_grid.mjs'))
    s=replace(s,'const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,',
              'const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,\n    nq=base.quadratureIndependentNodes,')
    head,body=s.split('  function solveManySPD',1)
    head=replace(head,'length:N','length:nq',2)
    body=replace(body,'for(let n=0;n<N;n++)','for(let n=0;n<nq;n++)')
    body=replace(body,'/N','/nq',3)
    derived[name]=header+head+'  function solveManySPD'+body

    name=names[2];s=original[name]
    s=replace(s,'const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,',
              'const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,\n    nq=base.quadratureIndependentNodes,')
    head,body=s.split('  function rhs(',1)
    head=replace(head,'length:N','length:nq')
    body=replace(body,'for(let n=0;n<N;n++)','for(let n=0;n<nq;n++)')
    body=replace(body,'/N','/nq')
    derived[name]=header+head+'  function rhs('+body

    name=names[3];s=original[name]
    s=replace(s,"import {integrationGrid} from './f6tail_cusp_grid.mjs';",
              external_import('integrationGrid','f6tail_cusp_grid.mjs'))
    derived[name]=header+s

    patched={}
    file=scripts/'950f-tail-stage-core.mjs';s=file.read_text();t=s
    for symbol,name in [('createMomentumTailEngine',names[0]),('createFastMomentumTailEngine',names[1])]:
        t=replace(t,f"const {{{symbol}}}=await import(sourceURL('{name}'));",
                  f"import {{{symbol}}} from './periodic-quadrature/{name}';")
    patched[file]=(s,t)
    file=scripts/'950f-tail-stage-split.mjs';s=file.read_text()
    t=replace(s,"const {createFastSplitFluxMomentumTailEngine}=await import(sourceURL('f6tail_fast_split_flux_engine.mjs'));",
              "import {createFastSplitFluxMomentumTailEngine} from './periodic-quadrature/f6tail_fast_split_flux_engine.mjs';")
    patched[file]=(s,t)
    file=scripts/'950f-tail-stage-port-v3.mjs';s=file.read_text()
    t=replace(s,"const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));",
              "import {createFastSplitFluxMomentumTailEngine} from './periodic-quadrature/f6tail_fast_split_flux_engine.mjs';")
    patched[file]=(s,t)
    dest=scripts/'periodic-quadrature'
    if dest.exists():raise FileExistsError('Use a fresh source copy; derived directory already exists')
    dest.mkdir()
    for name,s in derived.items():(dest/name).write_text(s)
    for file,(_,s) in patched.items():file.write_text(s)
    if any((root/name).read_text()!=s for name,s in original.items()):
        raise RuntimeError('Canonical source unexpectedly changed')
    record=dict(scope=__doc__,source_topic=str(topic),canonical_unchanged=True,
                original_sha256={name:digest(s) for name,s in original.items()},
                derived_sha256={name:digest(s) for name,s in derived.items()},
                patched_sha256={str(file.relative_to(topic)):dict(before=digest(old),after=digest(new))
                                for file,(old,new) in patched.items()},
                installer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    a.manifest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))


if __name__=='__main__':main()
