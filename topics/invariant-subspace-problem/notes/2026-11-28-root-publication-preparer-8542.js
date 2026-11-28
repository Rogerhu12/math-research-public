return (async()=>{

const u=new Function("return ("+load("isp_root_unwrap_helper")+")")();
const repo="Rogerhu12/math-research-public", root="topics/invariant-subspace-problem/";
const byte=s=>unescape(encodeURIComponent(s)).length;
const paths={H:"HANDOFF.md",O:"open.md",I:"results.md",L:"log.md"};
const rulesExpected={"README.md":"282e86b03385d3b6245ce7100ae2e2af7b103c2d",[root+"README.md"]:"5fbd905291dd044c88d35bd9c07ac0e586ff795a"};
const headRef=u(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/ref/heads/main"}));
const head=headRef.object.sha;
const required=[...Object.keys(rulesExpected),...Object.values(paths).map(p=>root+p)];
const rr=await Promise.allSettled(required.map(async path=>{
 const raw=await tools.mcp__codex_apps__github_fetch_file({repository_full_name:repo,path,ref:head});
 const meta=raw.structuredContent||{};
 return {path,text:u(raw),sha:meta.sha};
}));
const read={};
for(let i=0;i<rr.length;i++){if(rr[i].status!=="fulfilled")throw rr[i].reason;read[required[i]]=rr[i].value;}
for(const path of Object.keys(rulesExpected)){
 if(read[path].sha!==rulesExpected[path]){
  const old=u(await tools.mcp__codex_apps__github_fetch_blob({repository_full_name:repo,blob_sha:rulesExpected[path]}));
  const a=old.split("\n"),b=read[path].text.split("\n");
  let i=0,j=0;while(i<a.length&&i<b.length&&a[i]===b[i])i++;
  while(j<a.length-i&&j<b.length-i&&a[a.length-1-j]===b[b.length-1-j])j++;
  const diff={path,oldBlob:rulesExpected[path],newBlob:read[path].sha,head,removed:a.slice(i,a.length-j).join("\n"),added:b.slice(i,b.length-j).join("\n")};
  store("isp_changed_rules_read",diff);text(diff);throw Error("README changed: apply this difference before publication");
 }
}
const treeInfo=u(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/trees/"+head}));
const utc=(await tools.clock__curr_time({})).current_time;
const taipei=new Date(Date.parse(utc.replace(" UTC","Z").replace(" ","T"))+8*3600000).toISOString().slice(0,16).replace("T"," ");
let H=read[root+paths.H].text,O=read[root+paths.O].text,I=read[root+paths.I].text,L=read[root+paths.L].text;
const files=(spec.files||[]).map(v=>({...v}));
if(spec.archiveH)files.push({path:root+spec.archiveH,content:H});
if(spec.archiveOpen)files.push({path:root+spec.archiveOpen,content:O});
if(spec.archiveLog){files.push({path:root+spec.archiveLog,content:L});const chunks=L.split(/(?=^2026-\d\d-\d\d \d\d:\d\d Asia\/Taipei)/m).filter(x=>/^2026-/.test(x));L="# 研究日志\n\n此前全部日志见[完整快照]("+spec.archiveLog+")及其归档链。\n\n"+chunks.slice(-10).join("");}
if(spec.archiveResults){files.push({path:root+spec.archiveResults,content:I});const marker="## 新增结论";let at=I.indexOf(marker);if(at<0)throw Error("results index marker");const recent=I.slice(at+marker.length).trim().split(/\n\n(?=- \[)/).slice(0,30).join("\n\n");I=I.slice(0,at)+"此前完整索引见[完整快照]("+spec.archiveResults+")及归档链。\n\n"+marker+"\n\n"+recent+"\n";}
function replaceUnique(s,a,b,label){if(typeof a!=="string"||!a||s.split(a).length!==2)throw Error("nonunique or missing "+label+": "+a?.slice(0,140));return s.replace(a,b);}
for(const [a,b]of spec.hReplacements||[])H=replaceUnique(H,a,b,"H replacement");
for(const [a,b]of spec.openReplacements||[])O=replaceUnique(O,a,b,"open replacement");
if(spec.hBefore)H=replaceUnique(H,spec.hBefore.marker,spec.hBefore.text+"\n"+spec.hBefore.marker,"H insertion");
if(spec.openAppend)O=O.replace(/\s*$/,"")+"\n\n"+spec.openAppend+"\n";
if(spec.archiveH)H=H.replace(/^\- 所有被压缩的精确结论\/来源\/失败身份保\[最新完整H\]\([^)]*\)/m,"- 所有被压缩的精确结论/来源/失败身份保[最新完整H]("+spec.archiveH+")");
if(spec.archiveOpen)O=O.replace(/此前全部原条目、来源、失败范围与开放接口保\[本次完整快照\]\([^)]*\)/,"此前全部原条目、来源、失败范围与开放接口保[本次完整快照]("+spec.archiveOpen+")");
H=H.replace(/^\- \*\*终端断开后远端已读：\*\*[^\n]*$/m,"- **终端断开后远端已读：** "+head+"（"+utc+"）；只读检查不冒称实际pull。");
H=H.replace(/^\- \*\*终端断开：\*\*[^\n]*$/m,"- **终端断开：** 2026-11-28 09:05 UTC复探仍不可用；按规矩8/13小文本准备、Actions真实部分克隆/pull/rebase/push，拒推立即循环。10:05再探，旧故障保归档。");
if(spec.indexEntry){I=replaceUnique(I,"## 新增结论\n","## 新增结论\n\n"+spec.indexEntry+"\n","index entry");}
if(spec.indexNotice)I=I.replace("# 已得结果\n","# 已得结果\n\n"+spec.indexNotice+"\n");
if(spec.logLines?.length){if(spec.logLines.length>4)throw Error("at most four log lines");L=L.replace(/\s*$/,"")+"\n\n"+taipei+" Asia/Taipei｜Astra-ISP-8542378f-20261127\n"+spec.logLines.map(s=>"- "+s).join("\n")+"\n";}
for(const [key,body]of Object.entries({H,O,I,L})){
 if(key==="H"&&byte(body)>10000)throw Error("HANDOFF "+byte(body));
 if(byte(body)>=100000)throw Error("Markdown 100KB "+key);
 files.push({path:root+paths[key],content:body});
}
const requestPath=root+"notes/2026-11-27-root-terminal-publication-request-8542.json";
const knownAllowed=[root+"notes/2026-11-27-root-terminal-publication-8542.py",".github/workflows/invariant-subspace-8542-root-terminal-publication.yml"];
const allowed=[...new Set([...files.map(f=>f.path),...knownAllowed,requestPath])];
const request={message:spec.message,parentCommit:head,rulesGitBlobs:rulesExpected,allowedPaths:allowed,dispatchWorkflows:spec.dispatchWorkflows||[]};
files.push({path:requestPath,content:JSON.stringify(request,null,2)+"\n"});
const seen=new Set;
for(const f of files){
 if(seen.has(f.path))throw Error("duplicate file "+f.path);seen.add(f.path);
 if(!/^[A-Za-z0-9_./-]+$/.test(f.path)||f.path.split("/").includes("..")||!(f.path.startsWith(root)||f.path.startsWith(".github/workflows/invariant-subspace")))throw Error("scope "+f.path);
 if(f.content!==undefined&&f.path.endsWith(".md")&&byte(f.content)>=100000)throw Error("large Markdown "+f.path);
}
const elements=files.map(f=>({path:f.path,mode:"100644",type:"blob",...(f.content!==undefined?{content:f.content}:{sha:f.sha})}));
const tree=u(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:treeInfo.sha,tree_elements:elements}));
const commit=u(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,message:spec.message,parent_sha:head,tree_sha:tree.sha}));
store("isp_last_prepared",{head,time:utc,files,name:spec.message,commit:commit.sha,branch:spec.branchName});
const branch=u(await tools.mcp__codex_apps__github_create_branch({repository_full_name:repo,branch_name:spec.branchName,sha:commit.sha}));
store("isp_pending_actions_publication",{branch:spec.branchName,sourceCommit:commit.sha,parentCommit:head,time:utc,mainPushPending:true});
store("isp_current_prepared_H",H);store("isp_current_prepared_O",O);
text({preparedBranch:spec.branchName,sourceCommit:commit.sha,parentCommit:head,time:utc,name:spec.message,actualMainPushPending:true,mainRefUntouchedByAPI:true});

})();
