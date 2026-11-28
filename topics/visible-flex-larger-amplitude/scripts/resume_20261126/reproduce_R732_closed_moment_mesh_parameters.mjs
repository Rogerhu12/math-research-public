#!/usr/bin/env node
// Reproduce complete parameter documents from original whole-file values. This program executes no science.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const BINDING={"role":"complete downstream original scopes, evidence, source build and parameter binding","name":"fixed-fejer-R732-closed-moment-mesh-parameter-binding.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-R732-closed-moment-mesh-parameter-binding.json","bytes":20847,"sha256":"9a36801a6faef7f333cea18d1c346d0881586751c1048675506c5f080a69a086","git_blob_sha":"7e05765d7629100cb6191801a8e9d351b5ba1c18"};
const RESULTS={"closed":{"role":"complete R732 closed direct and normal build argv, domain, selectors and outputs","name":"fixed-fejer-R732-R723-closed-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-R732-R723-closed-complete-ready.json","bytes":13013,"sha256":"8884939673464d9304bcfbdd46a3e99a964905e960dddb93b6ad2538cb989b6b","git_blob_sha":"c983acb3579d6e18e31d3201a2248e4bb0a83a98"},"moment":{"role":"complete R732 moment direct and normal build argv, domain, selectors and outputs","name":"fixed-fejer-R732-R723-moment-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-R732-R723-moment-complete-ready.json","bytes":19980,"sha256":"afe80efb22492d951829d9236bb8ab87a23b5e36c7cebdcb466964e66a62e340","git_blob_sha":"5c059b9981e7f23799990998a6b56f5c9d015aab"},"packet":{"role":"complete R732 packet direct and normal build argv, domain, selectors and outputs","name":"fixed-fejer-R732-R723-packet-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-R732-R723-packet-complete-ready.json","bytes":34087,"sha256":"1e23909d6b56c9369f8fc0908152de6a5d71cba1679296ecbd716ba9a6d92f82","git_blob_sha":"9c2409dcf536814d4891bd2be2653335d0a40ba2"},"final":{"role":"complete R732 final direct and normal build argv, domain, selectors and outputs","name":"fixed-fejer-R732-R723-final-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-R732-R723-final-complete-ready.json","bytes":34052,"sha256":"ff96de79282f9311efe0ee5efa6d56a1929d26de9478569ee74e1322930a03fa","git_blob_sha":"e6426070ed0e8bf819f37fbcd6e1a9546fe5acc4"}};
function prepare(mode,parent,config,binding){
    const rename = Object.entries(config.namespace_substitutions).sort((a,b)=>b[0].length-a[0].length);
    function changed(value){
        if(typeof value==='string'){
            for(const [old,next] of rename)value=value.split(old).join(next);
            return value;
        }
        if(Array.isArray(value))return value.map(changed);
        if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([key,item])=>[changed(key),changed(item)]));
        return value;
    }
    const roles=config.plan_roles[mode], original=config.original_scope_by_mode[mode];
    const metadataPath=(key)=>'postprocess/'+config.namespace+'-R732-'+mode+'-'+key+'-source-build.json';
    const steps=[],inner=[],optionals=[];
    function count(fields){return Object.values(fields||{}).reduce((n,v)=>n+Object.keys(v).length,0)}
    for(let i=0;i<roles.length;i++){
        const role=roles[i],target=config.complete_direct_targets[role],old=parent.steps[i];
        if(!old||old.args.length!==original.inner_argument_words[i]||count(old.summary)!==original.original_formal_scalar_selectors[i]||count(old.progress_summary)!==original.original_live_scalar_selectors[i])throw Error('Complete parent parameter scope differs for '+mode+' '+role);
        const targetStep=changed(old);
        targetStep.id=config.namespace+'-R732-'+mode+'-'+role+'-20261128';
        targetStep.script=target.path;
        targetStep.scope=config.entry_scopes[role];
        inner.push(targetStep);
        if(role==='mesh'){
            const opt=targetStep.args.indexOf('--closed-phase-report');
            if(opt+2!==targetStep.args.length)throw Error('Whole R723 production evidence option expected');
            optionals.push({explicit_choice:'run the complete mesh without an attached closed proof',original_direct_script:target.path,
                original_complete_target_arguments:targetStep.args.slice(0,opt),
                actual_source_closed_evidence_not_supplied:true,actual_closed_geometric_claims:null});
        }
        const built=JSON.parse(JSON.stringify(targetStep)),file=metadataPath(role);
        built.script=config.complete_wrapper.path;
        built.args=['--entry',role,'--build-record','{work}/'+file,'--',...targetStep.args];
        built.outputs.push(file);
        const scalar={complete:'complete',phase:'phase',entry:'entry',source_commit:'source_commit',node:'node_executable',
            wrapper_source:'wrapper_source.sha256',target_source:'actual_target.sha256',target_bytes:'actual_target.bytes',
            scientific_roles:'scientific_role_count',runtime_count:'complete_scientific_runtime_count',
            child_started:'child_started',child_returncode:'child_returncode',successful_process_return:'successful_process_return',
            error_type:'error.type',error_message:'error.message',scientific_preflight:'extra_scientific_preflight_or_execution'};
        const builders=['science','accurate','closed_moment'];
        if(role==='mesh'||role==='mesh_read')builders.push('mesh');
        for(const b of builders){
            const prefix='complete_builds.'+b+'.';
            scalar[b+'_source']=prefix+'source.sha256';
            scalar[b+'_returncode']=prefix+'returncode';
            scalar[b+'_materialization_sha256']=prefix+'record.sha256';
            scalar[b+'_complete']=prefix+'complete_materialization.complete';
            scalar[b+'_generated_count']=prefix+'complete_materialization.'+config.complete_builders[b].count_key;
        }
        built.summary[file]=scalar;
        steps.push(built);
    }
    if(roles.length!==parent.steps.length)throw Error('An original complete step was omitted');
    return {schema:'complete-R732-R723-'+mode+'-ready-v1',prepared_utc:config.prepared_utc,namespace:config.namespace,
        executed:false,admitted:false,complete_current_parameter_binding:binding,complete_original_ready:config.original_ready_files[mode],
        whole_parent_preserves_all_nested_metadata_and_original_step_values:true,
        complete_source_family:mode==='closed'||mode==='moment'?config.complete_closed_flux_moment_source:config.complete_mesh_source,
        complete_original_direct_targets:inner.map((x,i)=>({step_index:i,script:x.script,id:x.id,
            args:x.args,original_parent_bundle:x.parent_bundle,outputs:x.outputs,
            original_summary_selector_maps:'see this steps array at the identical original output keys',
            original_live_selectors:'preserved under the same progress_summary key on its wrapped step'})),
        optional_original_32_word_mesh_without_closed_evidence:optionals,
        all_original_numerical_parameters_available_from_binding:true,
        original_target_argument_counts:inner.map(x=>x.args.length),actual_outer_wrapper_argument_counts:steps.map(x=>x.args.length),
        original_selector_counts:original,current_selector_counts:steps.map(x=>({formal:count(x.summary),live:count(x.progress_summary)})),
        complete_target_arguments_given_unchanged_to_original_direct_entry:true,
        original_working_fixed_S_terminal_band_and_all_current_free_controls_retained:true,
        complete_source_materialization_adds_no_scientific_calls_or_time_limit:true,
        actual_point_model_snapshot_and_fee_results:config.future_actual,steps};
}

const argv=process.argv.slice(2);
function option(name){const i=argv.indexOf(name);if(i<0||!argv[i+1])throw Error('Missing '+name);return argv[i+1];}
const source=path.resolve(option('--source-repository')),out=path.resolve(option('--output-repository'));
function checked(bytes,record){
    const git=crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob '+bytes.length+'\0'),bytes])).digest('hex');
    return record.bytes===bytes.length&&record.sha256===crypto.createHash('sha256').update(bytes).digest('hex')&&record.git_blob_sha===git;
}
function read(record,commit){
    let bytes;
    const local=path.join(source,record.path);
    if(fs.existsSync(local)){const b=fs.readFileSync(local);if(checked(b,record))bytes=b;}
    if(!bytes&&commit)bytes=execFileSync('git',['-C',source,'show',commit+':'+record.path],{maxBuffer:100000});
    if(!bytes||!checked(bytes,record))throw Error('Whole original fixed parameter identity differs: '+record.path);
    return JSON.parse(bytes.toString('utf8'));
}
const binding=read(BINDING,null);
for(const [mode,record] of Object.entries(RESULTS)){
    const parent=read(binding.original_ready_files[mode],binding.parent_metadata_commit);
    const next=Buffer.from(JSON.stringify(prepare(mode,parent,binding,BINDING),null,2)+'\n','utf8');
    if(!checked(next,record))throw Error('Whole reconstructed ready differs: '+record.path);
    const file=path.join(out,record.path);
    if(fs.existsSync(file)){
        if(!checked(fs.readFileSync(file),record))throw Error('Existing full ready differs: '+file);
    }else{
        fs.mkdirSync(path.dirname(file),{recursive:true});
        const temp=file+'.writing-'+process.pid;
        fs.writeFileSync(temp,next,{flag:'wx'});fs.renameSync(temp,file);
    }
    process.stdout.write(JSON.stringify({mode,path:file,bytes:record.bytes,sha256:record.sha256,git_blob_sha:record.git_blob_sha})+'\n');
}
