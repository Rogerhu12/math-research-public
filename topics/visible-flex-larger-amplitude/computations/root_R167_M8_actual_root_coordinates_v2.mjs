// Actual finite M8 knot conversion. No ODE, far graph, or BVP is repeated.
// Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const argv=process.argv.slice(2), arg=k=>argv[argv.indexOf(k)+1];
const input=arg('--inputs'),out=arg('--out');
if(!input||!out||fs.existsSync(out))throw Error('Fresh output and explicit input manifest required');
const started=performance.now(),sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const hash=p=>sha(fs.readFileSync(p));
const read=p=>JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
const ids=read(input),gates={};
function gate(k,v){gates[k]=!!v;if(!v)throw Error(k);}
for(const [k,r] of Object.entries(ids.files))gate('identity_'+k,hash(r.path)===r.sha256);
const sourceTopic=ids.source_topic,sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_TOPIC=sourceTopic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
const packet=read(ids.files.response.path),prior=packet.response,cp=prior.checkpoint;
const cfg=packet.config,M=cp.parameters.modes,spacing=cp.parameters.spacing;
gate('actual_completed_finite_M8',prior.converged===true&&Number.isFinite(prior.residual)&&prior.residual<=cfg.solveTolerance&&M===8&&spacing===2);
gate('all_saved_states',cp.states.length===433&&cp.states.every(s=>s.length===16&&s.every(Number.isFinite)));
gate('raw_nodes_are_copies_not_coordinate_changes',cp.rawNode.length===13&&cp.rawNode.every((v,i)=>v===36*i)
    &&cp.rawStates.every((r,i)=>r.length===16&&r.every((v,k)=>Object.is(v,cp.states[cp.rawNode[i]][k]))));
const oldManifest=packet.ready.endpointJacobianAdapter.ownHashes;
gate('same_model_and_cache_source',ids.files.model.sha256===oldManifest['closure_rational_tail_model.mjs']
    &&ids.files.point_cache.sha256===oldManifest['closure_bounded_point_cache.mjs']);
const {createRationalDeepTail}=await import(pathToFileURL(ids.files.model.path));
const {subdividePhysical}=await import(pathToFileURL(ids.files.subdivision.path));
const {createFourierRootMomentumTailEngine}=await import(pathToFileURL(ids.files.root_engine.path));
const model=await createRationalDeepTail(cfg,{sourceTopic,frozenWarpAlpha:cfg.rationalFrozenWarpAlpha,pointCacheLimit:96});
gate('same_binary_shallow_model',model.assertFrozenHead()
    &&model.manifest.headFingerprint===cp.parameters.rationalDeepExtension.headFingerprint
    &&model.manifest.frozenWarpAlpha===cp.parameters.rationalFrozenWarpAlpha);
const stages=subdividePhysical(model.head,12,4);
gate('same_full_actual_stage_layout',stages.cells.length===432&&stages.rawNode.every((v,i)=>v===cp.rawNode[i]));
const engines=new Map();
function engine(stage){
    if(!engines.has(stage.mu))engines.set(stage.mu,createFourierRootMomentumTailEngine({modes:M,spacing,
        quadrature:cp.parameters.quadrature,mu:stage.mu,orientation:1,projectionFloor:cp.parameters.projectionFloor}));
    return engines.get(stage.mu);
}
function convert(index,side){
    // At an outer stage endpoint, the saved Pi is in its outer mu chart.
    // cellFlow divides its output by portRatio; undo that exact convention.
    const stageIndex=side==='inner_of_previous'?index-1:index;
    const st=stages.cells[stageIndex],x=side==='inner_of_previous'?0:1;
    const state=new Float64Array(2*M+2);state.set(cp.states[index]);
    const factor=side==='inner_of_previous'?1:st.portRatio;
    for(let j=0;j<M;j++)state[M+j]*=factor;
    const e=engine(st),rt=e.root(state,st.profiles[0],x),g=rt.g,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
    const p=[],k=[],xi=[],oldRaw=e.toRaw(state,st.profiles[0],x,rt).raw;
    for(let j=0;j<M;j++){
        const m=spacing*(j+1);
        p.push(-m*g.r**3*state[j]/g.w);
        k.push(sq2*rt.L[j+1]-m*p[j]);
        xi.push(sq2*g.r**4*g.w2*rt.L[j+1]/(sq12*st.mu));
    }
    const strong=(sigma)=>p.reduce((s,v,j)=>s+(1+spacing*(j+1))*Math.exp(sigma*spacing*(j+1))*(Math.abs(v)+Math.abs(k[j])),0);
    const normalizedPi=Array.from(state.slice(M,2*M));
    const maxDifference=Math.max(...xi.map((v,j)=>Math.abs(v-normalizedPi[j])));
    gate('all_original_root_outputs_finite_'+index+'_'+side,[...p,...k,...xi,rt.L[0],rt.err/rt.scale,g.r,g.w].every(Number.isFinite));
    gate('original_root_branch_'+index+'_'+side,rt.e.minD>cp.parameters.projectionFloor
        &&rt.e.minS>cp.parameters.projectionFloor&&rt.e.minA>cp.parameters.projectionFloor);
    return {saved_node:index,side,stage_index:stageIndex,raw_cell:st.rawCell,raw_segment:st.rawSegment,
        quarter:st.part,source_x:side==='inner_of_previous'?st.rawLeft:st.rawRight,
        mu:st.mu,port_ratio_applied_to_Pi:factor,radius:g.r,w:g.w,r_x:g.drdx,log_w_x:g.dlogwdx,
        Q:Array.from(state.slice(0,M)),connection_Pi:normalizedPi,canonical_Xi:xi,
        relative_P_sine:p,relative_K_cosine:k,complete_finite_mean_c:rt.L[0],L_orthonormal:Array.from(rt.L),
        root_relative_residual:rt.err/rt.scale,root_iterations:rt.iterations,root_roundoff_fallback:rt.roundoffFallback===true,
        minD:rt.e.minD,minS:rt.e.minS,minA:rt.e.minA,
        strong_pair_sigma0:strong(0),strong_pair_sigma1over64:strong(1/64),
        canonical_minus_connection_max:maxDifference,
        legacy_raw_second:Array.from(oldRaw.slice(M,2*M)),
        same_saved_binary_Q:true,finite_angular_quadrature:cp.parameters.quadrature};
}
const rows=[],joins=[];
for(let i=252;i<=360;i++){
    const row=convert(i,'inner_of_previous');rows.push(row);
    if(i<360){
        const alternate=convert(i,'outer_of_current');
        joins.push({node:i,other_cell:alternate.raw_cell,other_segment:alternate.raw_segment,
            port_ratio_applied_to_Pi:alternate.port_ratio_applied_to_Pi,
            P_difference:row.relative_P_sine.map((v,j)=>v-alternate.relative_P_sine[j]),
            K_difference:row.relative_K_cosine.map((v,j)=>v-alternate.relative_K_cosine[j]),
            mean_difference:row.complete_finite_mean_c-alternate.complete_finite_mean_c,
            radius_difference:row.radius-alternate.radius,w_difference:row.w-alternate.w});
    }
}
gate('whole_original9to7_knot_coverage',rows.length===109&&rows[0].saved_node===252&&rows.at(-1).saved_node===360);
gate('same_input_bytes_after_readout',Object.values(ids.files).every(r=>hash(r.path)===r.sha256));
const maximum=(key)=>rows.reduce((a,r)=>r[key]>a.value?{value:r[key],node:r.saved_node,cell:r.raw_cell,segment:r.raw_segment}:a,{value:-Infinity});
const summary={strong_sigma1over64:maximum('strong_pair_sigma1over64'),strong_sigma0:maximum('strong_pair_sigma0'),
    canonical_minus_connection:maximum('canonical_minus_connection_max'),root_relative_residual:maximum('root_relative_residual'),
    endpoint_node10:rows.at(-1),endpoint_node7:rows[0],
    maximum_join_P_difference:Math.max(...joins.flatMap(r=>r.P_difference.map(Math.abs))),
    maximum_join_K_difference:Math.max(...joins.flatMap(r=>r.K_difference.map(Math.abs)))};
const result={schema:'original-M8-actual-full-root-knot-coordinate-readout-v1',author:'/root (GPT-6 Astra Pro; AI-assisted)',
    source_sha256:hash(new URL(import.meta.url)),input_manifest_sha256:hash(input),inputs:ids,
    all_gates:Object.values(gates).every(Boolean),gates,actual_saved_finite_response:true,
    no_new_ODE_or_BVP:true,no_new_far_graph:true,rows,joins,summary,
    root_is_full_finite_M8_not_infinite_angle_certificate:true,
    binary_background_not_silently_identified_with_R26_real_background:true,
    between_knot_continuous_residual_unpaid:true,
    same_R143_actual_solution_or_closed_surface_claimed:false,
    elapsed_seconds:(performance.now()-started)/1000,peak_rss_kib:process.resourceUsage().maxRSS};
fs.writeFileSync(out,JSON.stringify(result)+'\n',{flag:'wx'});
console.log(JSON.stringify({primary:out,sha256:hash(out),all_gates:result.all_gates,gate_count:Object.keys(gates).length,
    summary:{strong:summary.strong_sigma1over64,root:summary.root_relative_residual,canonical_minus_connection:summary.canonical_minus_connection},
    elapsed_seconds:result.elapsed_seconds,peak_rss_kib:result.peak_rss_kib}));
