
return (async()=>{
const repo="Rogerhu12/math-research-public",base="topics/invariant-subspace-problem/";
const bytes=s=>unescape(encodeURIComponent(s)).length;
function data(r,label){if(r.isError||!r.structuredContent)throw Error(label+": "+JSON.stringify(r));return r.structuredContent;}
function replaceOnce(s,a,b,label){if(!a||!s.includes(a))throw Error("missing patch "+label);return s.replace(a,()=>b);}
const hd=data(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/ref/heads/main"}),"head"),head=JSON.parse(hd.content).object.sha;
const paths=["README.md",base+"README.md",base+"HANDOFF.md",base+"open.md",base+"results.md",base+"log.md"];
const rr=await Promise.allSettled([tools.clock__curr_time({}),tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/commits/"+head}),...paths.map(path=>tools.mcp__codex_apps__github_fetch_file({repository_full_name:repo,path,ref:head}))]),ds=[];
for(let i=0;i<rr.length;i++){if(rr[i].status!=="fulfilled")throw Error("read "+i+": "+String(rr[i].reason));ds.push(i===0?rr[i].value:data(rr[i].value,"read "+i));}
const time=ds[0].current_time,tree=JSON.parse(ds[1].content).tree.sha;
if(ds[2].sha!=="282e86b03385d3b6245ce7100ae2e2af7b103c2d"||ds[3].sha!=="5fbd905291dd044c88d35bd9c07ac0e586ff795a"){store("isp_changed_rules_read",{head,time,root:ds[2],topic:ds[3]});throw Error("README changed; inspect only differences before continuing");}
let h=ds[4].content,o=ds[5].content,ix=ds[6].content,log=ds[7].content;
if(spec.resultLeaf&&ix.includes("("+spec.resultLeaf+")")){store("isp_last_published",{head,alreadyPresent:true,name:spec.message});text({alreadyPresent:true,head,name:spec.message});return;}
const files=(spec.files||[]).map(f=>({...f}));
if(spec.archiveResults){files.push({path:base+spec.archiveResults,content:ix});const at=ix.indexOf("## 新增结论\n\n");if(at<0)throw Error("results archive marker absent");let intro=ix.slice(0,at).replace(/\[完整索引快照\]\([^)]*\)/,"[完整索引快照]("+spec.archiveResults+")");const entries=ix.slice(at+"## 新增结论\n\n".length).split(/\n\n(?=- )/);ix=intro+"## 新增结论\n\n"+entries.slice(0,30).join("\n\n").trimEnd()+"\n";}
if(spec.archiveLog){files.push({path:base+spec.archiveLog,content:log});const blocks=log.split(/\n\n(?=\d{4}-\d{2}-\d{2} \d{2}:\d{2} Asia\/Taipei｜)/);log="# 研究日志\n\n本次压缩前的全部日志及更早归档链见[完整日志快照]("+spec.archiveLog+")。以下保最近条目；归档不改变任何结论或开放范围。\n\n"+blocks.slice(-10).join("\n\n");}
if(spec.archiveH){files.push({path:base+spec.archiveH,content:h});h=h.replace(/所有被压缩的精确结论\/来源\/失败身份保\[最新完整H\]\([^)]*\)/,()=> "所有被压缩的精确结论/来源/失败身份保[最新完整H]("+spec.archiveH+")");}
if(spec.archiveOpen){files.push({path:base+spec.archiveOpen,content:o});o=o.replace(/此前全部原条目、来源、失败范围与开放接口保\[本次完整快照\]\([^)]*\)/,()=> "此前全部原条目、来源、失败范围与开放接口保[本次完整快照]("+spec.archiveOpen+")");}
for(const [a,b]of spec.hReplacements||[])h=replaceOnce(h,a,b,"H");
for(const [a,b]of spec.openReplacements||[])o=replaceOnce(o,a,b,"open");
if(spec.hBefore)h=replaceOnce(h,spec.hBefore.marker,spec.hBefore.text+"\n"+spec.hBefore.marker,"H before");
if(spec.openAppend)o=o.trimEnd()+"\n\n"+spec.openAppend+"\n";
if(spec.indexEntry)ix=replaceOnce(ix,"## 新增结论\n\n","## 新增结论\n\n"+spec.indexEntry+"\n\n","index");
const taipei=new Date(new Date(time.replace(" UTC","Z").replace(" ","T")).getTime()+8*3600000).toISOString().slice(0,16).replace("T"," ");
if(spec.logLines?.length)log=log.trimEnd()+"\n\n"+taipei+" Asia/Taipei｜Astra-ISP-8542378f-20261127\n"+spec.logLines.map(x=>"- "+x).join("\n")+"\n";
h=h.replace(/(\*\*终端断开后远端已读：\*\* )\x60[^\x60]+\x60（[^）]+）/,(_,prefix)=>prefix+"\x60"+head+"\x60（"+time+"）");
if(bytes(h)>=10000)throw Error("H too big "+bytes(h));
files.push({path:base+"HANDOFF.md",content:h},{path:base+"open.md",content:o},{path:base+"results.md",content:ix},{path:base+"log.md",content:log});
const requestPath=base+"notes/2026-11-27-root-terminal-publication-request-8542.json";
files.push({path:base+"notes/2026-11-27-root-terminal-publication-8542.py",content:load("isp_root_actions_publisher_driver_source")},{path:".github/workflows/invariant-subspace-8542-root-terminal-publication.yml",content:load("isp_root_actions_publisher_workflow_source")});
const request={message:spec.message,parentCommit:head,rulesGitBlobs:{"README.md":ds[2].sha,[base+"README.md"]:ds[3].sha},allowedPaths:[...files.map(f=>f.path),requestPath],dispatchWorkflows:spec.dispatchWorkflows||[]};
files.push({path:requestPath,content:JSON.stringify(request,null,2)+"\n"});
for(const f of files)if(f.content!==undefined&&bytes(f.content)>=100000)throw Error("file exceeds connector limit "+f.path+" "+bytes(f.content));
store("isp_last_prepared",{head,time,files,name:spec.message});
const tr=data(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:tree,tree_elements:files.map(f=>({path:f.path,mode:"100644",type:"blob",...(Object.prototype.hasOwnProperty.call(f,"sha")?{sha:f.sha}:{content:f.content})}))}),"tree");
const cr=data(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:head,tree_sha:tr.sha,message:spec.message}),"commit");
const branch=spec.branchName||("isp-8542-root-publish-"+Date.now());
data(await tools.mcp__codex_apps__github_create_branch({repository_full_name:repo,branch_name:branch,sha:cr.sha}),"new publication branch");
store("isp_pending_actions_publication",{branch,sourceCommit:cr.sha,parentCommit:head,time,name:spec.message,preparedFiles:files.map(f=>f.path),dispatchWorkflows:spec.dispatchWorkflows||[]});
text({preparedBranch:branch,sourceCommit:cr.sha,parentCommit:head,time,name:spec.message,actualMainPushPending:true,mainRefUntouchedByAPI:true});
})();