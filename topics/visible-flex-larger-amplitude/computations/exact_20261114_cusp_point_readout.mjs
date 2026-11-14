// Add actual source integration-breakpoint states to an existing regular readout.
// The underlying shooting solution and RK grid are unchanged. Only stages
// containing requested source breakpoints are replayed; old node bytes are
// referenced and hash-checked by the existing finite-field consumer.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';
import {gunzipSync,gzipSync}from'node:zlib';import{pathToFileURL,fileURLToPath}from'node:url';
const opt={};for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const k of ['--repo-root','--source-topic','--config','--response','--complete','--background','--stages','--out-dir'])if(!opt[k])throw Error('Missing '+k);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const write=(p,v)=>fs.writeFileSync(p,JSON.stringify(v)+'\n',{flag:'wx'});
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']),topic=path.join(repo,'topics/visible-flex-larger-amplitude');
const comp=path.join(topic,'computations'),notes=path.join(topic,'notes'),basePath=path.resolve(opt['--complete']);
const config=read(opt['--config']),record=read(opt['--response']),response=record.response??record,base=read(basePath),background=read(opt['--background']);
const binding=base.refinement_binding;
if(!base.finished||!binding||!response.converged||binding.response_sha256!==sha(fs.readFileSync(opt['--response']))||binding.config_sha256!==sha(fs.readFileSync(opt['--config'])))throw Error('Base readout must belong to this new converged response/config');
const out=path.resolve(opt['--out-dir']);fs.mkdirSync(out,{recursive:false});
Object.assign(process.env,{VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
  VISIBLE_FLEX_FROZEN_STORED_READY:path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')});
const scripts=process.env.CLOSING_TAIL_CACHE;
const sources=[fileURLToPath(import.meta.url),path.join(comp,'tail_frozen_geometry.mjs'),path.join(source,'scripts/950f-tail-subdivision.mjs'),
  path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs'),path.join(scripts,'f6tail_cusp_grid.mjs'),
  path.join(scripts,'f6tail_momentum_physical_jets.mjs'),path.join(scripts,'f6tail_relative_development.mjs')];
const sourceHashes=Object.fromEntries(sources.map(p=>[p,sha(fs.readFileSync(p))]));
const inputHashes=Object.fromEntries(['--config','--response','--complete','--background'].map(k=>[path.resolve(opt[k]),sha(fs.readFileSync(opt[k]))]));
write(path.join(out,'intent.json'),{started_utc:new Date().toISOString(),argv:process.argv.slice(2),source_sha256_at_start:sourceHashes,input_sha256:inputHashes});
const started=performance.now();
const{createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')));
const{subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')));
const{createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs')));
const{integrationGrid}=await import(pathToFileURL(path.join(scripts,'f6tail_cusp_grid.mjs')));
const{createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(scripts,'f6tail_momentum_physical_jets.mjs')));
const{relativeActualDevelopment}=await import(pathToFileURL(path.join(scripts,'f6tail_relative_development.mjs')));
const{physical,factory,manifest}=await createStoredPhysical(config),stages=subdividePhysical(physical,config.depth,config.shootingParts);
const S=stages.cells.length,M=config.modes,K=2*M,N=config.quadrature,factor=base.refinement,states=response.checkpoint.states;
if(base.completedNodes!==S*factor+1||background.stages!==S*factor||manifest.profileFingerprintAfter!==base.original_profile_fingerprint||background.original_profile_fingerprint!==base.original_profile_fingerprint)throw Error('Expected a matching regular source readout/background');
const selected=opt['--stages']==='all'?stages.cells.map((_,i)=>i):opt['--stages'].split(',').map(Number);
const rows=base.rows.map(row=>({...row,baseNode:row.node,file:path.relative(out,path.resolve(path.dirname(basePath),row.file))}));
const additions=[],replayed=[];let rkCalls=0;
for(const si of selected){
  if(!Number.isInteger(si)||si<0||si>=S)throw Error('Invalid requested stage');
  const c=stages.cells[si],p=c.profiles[0],cuts=(p.integrationBreakpoints??[]).filter(x=>Math.abs(x*factor-Math.round(x*factor))>1e-12);
  if(!cuts.length)continue;
  const engine=createFourierRootSplitFluxEngine({modes:M,spacing:config.spacing,quadrature:N,mu:c.mu,orientation:config.orientation,projectionFloor:config.projectionFloor,cuspAwareFlow:config.cuspAwareFlow});
  const evaluate=createMomentumPhysicalJetEvaluator(engine,{spacing:config.spacing}),grid=integrationGrid(config.steps,p.integrationBreakpoints??[]),got=new Set();
  let y=new Float64Array(K+2);y.set(states[si+1]);
  for(let k=0;k<grid.length-1;k++){
    y=engine.rk4(y,p,grid[k],grid[k+1]-grid[k]);rkCalls++;
    for(const x of cuts)if(Math.abs(grid[k+1]-x)<1e-13){
      if(got.has(x))throw Error('Duplicate source breakpoint');got.add(x);
      const point=Float64Array.from(y);point[K]=point[K+1]=0;
      const root=engine.root(point,p,x),jets=evaluate(point,p,x),g=root.g,d=relativeActualDevelopment(g,root.e.rows,jets.perAngle);
      if(!(g.r>0&&g.w>0&&g.drdx>0&&jets.minA>0&&jets.minD>0))throw Error('Invalid source breakpoint point domain');
      const bytes=Buffer.alloc(N*12*8);
      for(let j=0;j<N;j++){
        const v=jets.perAngle[j],values=[d.dx[j],d.dy[j],v.height,d.dxR[j],d.dyR[j],v.ur,d.dxT[j],d.dyT[j],v.ut,v.urr,v.urt,v.utt];
        for(let q=0;q<12;q++){if(!Number.isFinite(values[q]))throw Error('Nonfinite jet');bytes.writeDoubleLE(values[q],8*(j*12+q));}
      }
      const file='cusp-stage-'+si+'-'+additions.length+'.f64le.gz',compressed=gzipSync(bytes,{level:6});fs.writeFileSync(path.join(out,file),compressed,{flag:'wx'});
      const smallMean=base.rows[(si+1)*factor].meanPerturbationInnerAnchor+y[K];
      const entry=factory.getEntries(c.rawCell,config.valleyControls?.[c.rawCell]??0).entries[c.rawSegment];
      const primitive=entry.integrate(c.rawLeft,c.rawLeft+(c.rawRight-c.rawLeft)*x);
      const nativeMean=background.nodeHeightInnerAnchor[(si+1)*factor]+primitive[4]+physical.stats.alpha*primitive[5];
      const row={originalStage:si,rawCell:c.rawCell,rawSegment:c.rawSegment,x,nodePiMultiplier:1,file,shape:[N,12],
        sha256:sha(compressed),rawSha256:sha(bytes),geometry:{r:g.r,w:g.w,w2:g.w2,E:g.E,drdx:g.drdx,dlogwdx:g.dlogwdx},
        meanPerturbationInnerAnchor:smallMean,meanHeightInnerAnchor:nativeMean+smallMean,
        source:'actual source integration-breakpoint state on unchanged RK trajectory',sampleMetricRelativeOperatorError:d.actualMetricRelativeOperatorError,
        formalHeightCurvature:jets.formalHeightCurvature};rows.push(row);additions.push(row);
    }
  }
  if(got.size!==cuts.length)throw Error('Source breakpoint absent from actual RK grid');
  let endpoint=0;for(let j=0;j<K;j++)endpoint=Math.max(endpoint,Math.abs(y[j]/(j>=M?c.portRatio:1)-states[si][j]));
  replayed.push({stage:si,breakpoints:cuts,canonicalEndpointDifference:endpoint});
}
if(!additions.length)throw Error('No new source knots requested');
rows.sort((a,b)=>b.geometry.r-a.geometry.r);
for(let i=0;i<rows.length;i++){
  rows[i].node=i;if(i&&!(rows[i-1].geometry.r>rows[i].geometry.r))throw Error('Repeated or unordered radius');
}
const extra={kind:'source integration breakpoints',uniform_baseline_refinement:factor,added_nodes:additions.length,
  additions:additions.map(q=>({stage:q.originalStage,x:q.x,r:q.geometry.r,file:q.file,sha256:q.sha256,sampleMetric:q.sampleMetricRelativeOperatorError})),
  replayed_stages:replayed,RKCalls:rkCalls,no_new_shooting_solve:true,original_regular_node_bytes_unchanged:true,
  source_sha256_at_start:sourceHashes,input_sha256:inputHashes,seconds:(performance.now()-started)/1000};
write(path.join(out,'complete.json'),{...base,schema:'same-H-resolved-tail-with-source-cusp-knots-v1',finished:true,completedNodes:rows.length,rows,
  input_sha256:{...base.input_sha256,...inputHashes},source_knot_refinement:extra});
write(path.join(out,'result.json'),extra);console.log(JSON.stringify({event:'complete',out,added:additions.length,replayed,seconds:extra.seconds}));
