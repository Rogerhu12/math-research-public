#!/usr/bin/env python3
"""Reconstruct the narrowly changed full-tail consumers from preserved sources.

This writes source only. It never creates a numerical result or exit receipt.
"""
import argparse
import hashlib
import json
from pathlib import Path


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Expected exactly one source anchor: ' + old[:100])
    return text.replace(old, new, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scripts', required=True)
    parser.add_argument('--base-worker', default='fd2d-gc-tail-partition-worker-v3.mjs')
    args = parser.parse_args()
    p = Path(args.scripts)
    rows = []

    def save(name, text, parent):
        raw = text.encode()
        f = p / name
        if f.exists() and f.read_bytes() != raw:
            raise ValueError('Refuse to replace a different archived source: ' + str(f))
        f.write_bytes(raw)
        rows.append(dict(path=name, sha256=hashlib.sha256(raw).hexdigest(), parent=parent))

    core = (p / '78718-tail-geometric-trial-core.mjs').read_text()
    if hashlib.sha256(core.encode()).hexdigest() != '30c63e305c70420e870e92df066ca98e39cdb178e3c771481d570fb9d542dfcb':
        raise ValueError('The preserved finite equation source has changed; inspect its actual diff')
    core = '// fd2d complete modified-prefix consumer; original solver retained below.\n' + replace_once(
        core, "from './950f-tail-subdivision.mjs'", "from './fd2d-gc-tail-stage-graphs.mjs'")
    save('fd2d-gc-tail-full160-core.mjs', core, '78718-tail-geometric-trial-core.mjs')
    split = (p / '78718-tail-geometric-trial-split.mjs').read_text()
    split = '// fd2d complete modified-prefix consumer; original solver retained below.\n' + replace_once(
        split, "from './78718-tail-geometric-trial-core.mjs'", "from './fd2d-gc-tail-full160-core.mjs'")
    save('fd2d-gc-tail-full160-split.mjs', split, '78718-tail-geometric-trial-split.mjs')
    worker = (p / args.base_worker).read_text()
    worker = replace_once(worker, "from './78718-tail-geometric-trial-split.mjs'",
                          "from './fd2d-gc-tail-full160-split.mjs'")
    worker = replace_once(worker, "import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';",
        "import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';\n"
        "import {appendUnchangedDeepSource} from './fd2d-gc-tail-deep-extension.mjs';\n"
        "import {stageGraphStatistics} from './fd2d-gc-tail-stage-graphs.mjs';")
    worker = replace_once(worker, 'const physical=factory.assemble();',
        "const finitePhysical=factory.assemble();\n"
        "if(cfg.depth<finitePhysical.parameters.protectCell)throw Error('Full160 entry must include all physically modified cells nonlinearly');\n"
        "const physical=appendUnchangedDeepSource(finitePhysical,cfg.linearFar);\n"
        "trace({event:'unchanged_deep_source_extension',...physical.deepExtension});")
    worker = replace_once(worker, 'const transformedEngines=new Set();',
        "trace({event:'bounded_stage_graph_complete',...stageGraphStatistics()});\nconst transformedEngines=new Set();")
    worker = replace_once(worker, 'pointsPerEntry:192', 'pointsPerEntry:cfg.pointCachePerEntry??64')
    worker = '// fd2d v4: complete modified tail plus unchanged deep source, bounded stage-local graph cache.\n' + worker
    save('fd2d-gc-tail-partition-worker-v4.mjs', worker, args.base_worker)

    cached_core = replace_once(core,
        '  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity,worst=null;',
        '  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity,worst=null;\n'
        '  const retained=options.stageEvaluationCache?.begin(states,withJac);')
    cached_core = replace_once(cached_core, '   try{f=cellFlow(n,states[n+1],withJac);}',
        '   try{\n    if(retained?.has(n))f=retained.get(n);\n'
        '    else{f=cellFlow(n,states[n+1],withJac);retained?.set(n,f);}\n   }')
    anchor = "    if(error&&typeof error==='object')Object.assign(error,{tailStage:n,tailRawCell:cells[n].rawCell,tailRawSegment:cells[n].rawSegment});"
    cached_core = replace_once(cached_core, anchor, '    retained?.flush();\n' + anchor)
    anchor = '  const end=new Float64Array(M);for(let j=0;j<M;j++){end[j]=states[depth][M+j]'
    cached_core = replace_once(cached_core, anchor, '  retained?.finish();\n' + anchor)
    anchor = '     states=trial;history.at(-1).step=lambda;accepted=true;'
    cached_core = replace_once(cached_core, anchor, anchor +
        "\n     opts.accepted?.({...diagnostic,kind:'accepted',trialNorm:test.norm},states.map(v=>Array.from(v)));")
    cached_core = '// Actual stage-block retention and immediate accepted-state recovery; equations unchanged.\n' + cached_core
    save('fd2d-gc-tail-full160-cached-core.mjs', cached_core, 'fd2d-gc-tail-full160-core.mjs')
    save('fd2d-gc-tail-full160-cached-split.mjs', replace_once(split,
        "from './fd2d-gc-tail-full160-core.mjs'", "from './fd2d-gc-tail-full160-cached-core.mjs'"),
        'fd2d-gc-tail-full160-split.mjs')
    worker = replace_once(worker, "from './fd2d-gc-tail-full160-split.mjs'",
        "from './fd2d-gc-tail-full160-cached-split.mjs'")
    worker = replace_once(worker, "import {stageGraphStatistics} from './fd2d-gc-tail-stage-graphs.mjs';",
        "import {stageGraphStatistics} from './fd2d-gc-tail-stage-graphs.mjs';\n"
        "import {createSequentialStageCache} from './fd2d-gc-tail-sequential-stage-cache.mjs';")
    worker = replace_once(worker,
        'const dn=createCompactTailDN({...cfg,tail:physical,retainTangentPredictor:useTangent}),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));',
        'let actualStageCache=null;\n'
        'const stageEvaluationCache={begin:(states,withJac)=>actualStageCache?.begin(states,withJac)};\n'
        'const dn=createCompactTailDN({...cfg,tail:physical,retainTangentPredictor:useTangent,stageEvaluationCache}),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));')
    anchor = 'const geometricTrial=createGeometricTrialHook(dn.tail.cells,{spacing:cfg.spacing});'
    worker = replace_once(worker, anchor,
        "actualStageCache=createSequentialStageCache({cacheRoot:cfg.stageCacheRoot,entryURL:import.meta.url,tail:dn.tail,backend:backendLabel,dependencyBlobs:JSON.parse(fs.readFileSync(new URL('../notes/closing_tail_dependency_blobs.json',import.meta.url),'utf8')),diagnostic:trace});\n"
        "trace({event:'actual_serial_stage_cache',metadata:actualStageCache?.metadata??null});\n" + anchor)
    retention = r"""function retainAccepted(row,states){
 if(!cfg.iterationCheckpointFile)return;
 const file=cfg.iterationCheckpointFile.replace(/\.json\.gz$/,'-accepted.json.gz');
 const checkpoint={parameters:dn.tail.parameters,states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:currentHeight,
  scope:'Actual accepted state-only trial. Recovery only: no new full-J residual or complete DN response is asserted.'};
 const bytes=zlib.gzipSync(JSON.stringify({status:'accepted-trial-recovery-only',call,iteration:row,checkpoint})+'\n');
 if(bytes.length>=5_000_000)throw Error('Accepted checkpoint exceeds repository file limit');
 fs.writeFileSync(file+'.tmp',bytes);fs.renameSync(file+'.tmp',file);
 trace({event:'accepted_state_saved',call,file,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),...row});
}
function retainRequestInitial(states){
 if(!cfg.iterationCheckpointFile)return;
 const file=cfg.iterationCheckpointFile.replace(/\.json\.gz$/,`-request-${String(call).padStart(4,'0')}-initial.json.gz`);
 const checkpoint={parameters:dn.tail.parameters,states:states.map(v=>Array.from(v)),
  rawNode:dn.tail.rawNode,cutHeight:currentHeight,
  scope:'Actual requested initial state. Its nonlinear residual has not yet completed; recovery data only.'};
 const bytes=zlib.gzipSync(JSON.stringify({status:'request-initial-recovery-only',call,checkpoint})+'\n');
 if(bytes.length>=5_000_000)throw Error('Initial checkpoint exceeds repository file limit');
 fs.writeFileSync(file,bytes,{flag:'wx'});
 trace({event:'request_initial_saved',call,file,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});
}
"""
    worker = replace_once(worker, 'function retainTrial(row,state){', retention + 'function retainTrial(row,state){')
    worker = replace_once(worker, '  const sol=dn.solve(req.height,{maxIterations:',
        '  if(!initial)initial=dn.tail.initial(Float64Array.from(req.height,v=>v/zero.radius**4));\n'
        '  retainRequestInitial(initial);\n  const sol=dn.solve(req.height,{accepted:retainAccepted,maxIterations:')
    worker = '// fd2d v5: exact completed stage retention and immediate actual accepted checkpoints.\n' + worker
    save('fd2d-gc-tail-partition-worker-v5.mjs', worker, 'fd2d-gc-tail-partition-worker-v4.mjs')
    print(json.dumps(rows, indent=2))


if __name__ == '__main__':
    main()
