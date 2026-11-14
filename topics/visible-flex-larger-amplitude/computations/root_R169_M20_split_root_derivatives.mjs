// Original strong M20 finite-flow jets; no ODE/BVP/far graph is repeated.
// Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const argv=process.argv.slice(2),arg=k=>argv[argv.indexOf(k)+1];
const input=arg('--inputs'),out=arg('--out');
if(!input||!out||fs.existsSync(out))throw Error('Explicit inputs and fresh output required');
const started=performance.now(),hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
const ids=read(input),gates={};
function gate(k,v){gates[k]=!!v;if(!v)throw Error(k);}
for(const [key,r] of Object.entries(ids.files))gate('identity_'+key,hash(r.path)===r.sha256);
const parent=read(ids.files.R168_inputs.path);
for(const [key,r] of Object.entries(parent.files))gate('parent_identity_'+key,hash(r.path)===r.sha256);
const coordinates=read(ids.files.R168_primary.path),owned=read(ids.files.R168_resource.path);
gate('actual_completed_R168',owned.exitcode===0&&coordinates.all_gates
    &&coordinates.source_sha256===ids.files.R168_source.sha256
    &&coordinates.input_manifest_sha256===ids.files.R168_inputs.sha256
    &&coordinates.rows.length===217);
const sourceTopic=parent.source_topic,sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_TOPIC=sourceTopic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
process.env.CLOSURE_FROZEN_CALIBRATION_READY=parent.files.response.path;
process.env.CLOSURE_FROZEN_STORED_READY_FILES='[]';
const packet=read(parent.files.response.path),cfg=packet.config,cp=packet.response.checkpoint;
const M=cp.parameters.modes,spacing=cp.parameters.spacing;
gate('actual_original_finite_configuration',M===20&&spacing===2&&cp.parameters.quadrature===512&&cp.states.length===865);
const {createRationalDeepTail}=await import(pathToFileURL(parent.files.model.path));
const {subdividePhysical}=await import(pathToFileURL(parent.files.subdivision.path));
const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(ids.files.split_engine.path));
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(ids.files.physical_jets.path));
const model=await createRationalDeepTail(cfg,{sourceTopic,frozenWarpAlpha:cfg.rationalFrozenWarpAlpha,pointCacheLimit:96});
gate('same_frozen_model',model.assertFrozenHead()&&model.manifest.headFingerprint===cp.parameters.rationalDeepExtension.headFingerprint);
const stages=subdividePhysical(model.head,12,8),engines=new Map(),evaluators=new Map();
function engine(st){
    if(!engines.has(st.mu)){
        const e=createFourierRootSplitFluxEngine({modes:M,spacing,quadrature:cp.parameters.quadrature,mu:st.mu,
            orientation:1,projectionFloor:cp.parameters.projectionFloor});
        gate('original_split_engine_'+st.rawCell,e.rhsEvaluation==='split-linear-flux-v1');
        engines.set(st.mu,e);evaluators.set(st.mu,createMomentumPhysicalJetEvaluator(e,{spacing}));
    }
    return engines.get(st.mu);
}
function endpoint(i,x){
    const st=stages.cells[i],node=x===0?i+1:i,e=engine(st),state=new Float64Array(2*M+2);
    state.set(cp.states[node]);
    if(x===1)for(let j=0;j<M;j++)state[M+j]*=st.portRatio;
    const rt=e.root(state,st.profiles[0],x),g=rt.g,field=e.rhs(state,st.profiles[0],x,false,rt);
    // The old physical-jet evaluator differentiates the actual finite root
    // implicitly, including explicit background and original split RHS.
    const jet=evaluators.get(st.mu)(state,st.profiles[0],x),sq2=Math.sqrt(2);
    const P=[],K=[],Pdot=[],Kdot=[],directPdot=[];
    const s=g.drdx/g.r,l=g.dlogwdx;
    for(let j=0;j<M;j++){
        const m=spacing*(j+1),p=-m*g.r**3*state[j]/g.w,k=sq2*rt.L[j+1]-m*p;
        const pd=-(s+l)*p-m*s*k;
        P.push(p);K.push(k);Pdot.push(pd);Kdot.push(sq2*jet.Ldot[j+1]-m*pd);
        directPdot.push(-m*g.r**3/g.w*(field[j]+(3*s-l)*state[j]));
    }
    const row=coordinates.rows[node-504];
    gate('complete_finite_endpoint_'+i+'_'+x,[...P,...K,...Pdot,...Kdot,jet.Ldot[0],g.r,g.w].every(Number.isFinite)
        &&rt.e.minD>cp.parameters.projectionFloor&&rt.e.minS>cp.parameters.projectionFloor&&rt.e.minA>cp.parameters.projectionFloor);
    return {saved_node:node,stage_x:x,P,K,Pdot,Kdot,mean:rt.L[0],mean_dot:jet.Ldot[0],r:g.r,w:g.w,s,l,
        root_relative_residual:rt.err/rt.scale,max_Darboux_diagnostic:jet.maxDarboux,
        direct_kinematic_difference:Math.max(...Pdot.map((v,j)=>Math.abs(v-directPdot[j]))),
        single_canonical_node_P_difference:Math.max(...P.map((v,j)=>Math.abs(v-row.relative_P_sine[j]))),
        single_canonical_node_K_difference:Math.max(...K.map((v,j)=>Math.abs(v-row.relative_K_cosine[j])))};
}
const pieces=[];
for(let i=504;i<720;i++){
    const st=stages.cells[i],left=endpoint(i,0),right=endpoint(i,1);
    // Freeze one canonical value per node, independently of its chart readout.
    // The consumer interprets these binary values as exact rationals and forms
    // Hermite polynomials with exact arithmetic, ensuring exact C0 seams.
    const inner=coordinates.rows[i+1-504],outer=coordinates.rows[i-504];
    pieces.push({stage_index:i,raw_cell:st.rawCell,raw_segment:st.rawSegment,part:st.part,
        raw_left:st.rawLeft,raw_right:st.rawRight,inner_node:i+1,outer_node:i,
        P0:inner.relative_P_sine,P1:outer.relative_P_sine,K0:inner.relative_K_cosine,K1:outer.relative_K_cosine,
        dP0:left.Pdot,dP1:right.Pdot,dK0:left.Kdot,dK1:right.Kdot,endpoint_jets:[left,right],
        original_breakpoints:st.profiles[0].integrationBreakpoints??[]});
    if((i-504)%36===0)console.log(JSON.stringify({complete_pieces:pieces.length,stage:i,cell:st.rawCell}));
}
gate('all216_original_pieces',pieces.length===216&&pieces[0].stage_index===504&&pieces.at(-1).stage_index===719);
for(let j=0;j<pieces.length-1;j++){
    const a=pieces[j],b=pieces[j+1];
    gate('identical_saved_C0_nodes_'+j,a.P0.every((v,k)=>Object.is(v,b.P1[k]))&&a.K0.every((v,k)=>Object.is(v,b.K1[k])));
}
gate('all_input_bytes_unchanged',Object.values(ids.files).every(r=>hash(r.path)===r.sha256)
    &&Object.values(parent.files).every(r=>hash(r.path)===r.sha256));
const ends=pieces.flatMap(p=>p.endpoint_jets),max=key=>Math.max(...ends.map(e=>e[key]));
const result={schema:'original-strong-M20-split-flow-implicit-root-Hermite-jet-data-v1',author:'/root (GPT-6 Astra Pro; AI-assisted)',
    source_sha256:hash(new URL(import.meta.url)),input_manifest_sha256:hash(input),inputs:ids,all_gates:Object.values(gates).every(Boolean),gates,
    pieces,mode_count:M,spacing,angular_quadrature:cp.parameters.quadrature,
    summary:{root_relative_residual:max('root_relative_residual'),direct_kinematic_difference:max('direct_kinematic_difference'),
        canonical_node_P_difference:max('single_canonical_node_P_difference'),canonical_node_K_difference:max('single_canonical_node_K_difference'),
        finite_Darboux_diagnostic:max('max_Darboux_diagnostic')},
    no_new_ODE_BVP_or_far_graph:true,actual_original_split_RHS_and_implicit_root_derivative:true,
    polynomial_construction_requires_exact_binary_rational_consumer:true,continuous_residual_or_same_R143_solution_proved:false,
    full_mean_infinite_angle_and_real_background_certificate:false,
    elapsed_seconds:(performance.now()-started)/1000,peak_rss_kib:process.resourceUsage().maxRSS};
fs.writeFileSync(out,JSON.stringify(result)+'\n',{flag:'wx'});
console.log(JSON.stringify({primary:out,sha256:hash(out),all_gates:result.all_gates,gate_count:Object.keys(gates).length,
    summary:result.summary,elapsed_seconds:result.elapsed_seconds,peak_rss_kib:result.peak_rss_kib}));
