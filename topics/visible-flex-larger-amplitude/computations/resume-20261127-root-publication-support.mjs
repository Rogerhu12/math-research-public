// Complete text-only publication support; no credentials or scientific computation.
// The MCP tools and session stores are explicitly provided by the calling environment.
export const utf8LengthBody="let n=0;for(const ch of input){const c=ch.codePointAt(0);n+=c<128?1:c<2048?2:c<65536?3:4;}return n;";
export const sha256jsBody="const raw=unescape(encodeURIComponent(input)),a=Array.from(raw,c=>c.charCodeAt(0)),L=a.length; a.push(128);while(a.length%64!==56)a.push(0);const hi=Math.floor(L/536870912),lo=(L*8)>>>0;for(let i=3;i>=0;i--)a.push((hi>>>(i*8))&255);for(let i=3;i>=0;i--)a.push((lo>>>(i*8))&255);\nconst K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2],H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19],rr=(v,n)=>(v>>>n)|(v<<(32-n)),w=new Array(64);\nfor(let off=0;off<a.length;off+=64){for(let i=0;i<16;i++){const k=off+4*i;w[i]=((a[k]<<24)|(a[k+1]<<16)|(a[k+2]<<8)|a[k+3])>>>0;}for(let i=16;i<64;i++){let x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[i-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}let [A,B,C,D,E,F,G,J]=H;for(let i=0;i<64;i++){const t1=(J+(rr(E,6)^rr(E,11)^rr(E,25))+((E&F)^(~E&G))+K[i]+w[i])>>>0,t2=((rr(A,2)^rr(A,13)^rr(A,22))+((A&B)^(A&C)^(B&C)))>>>0;J=G;G=F;F=E;E=(D+t1)>>>0;D=C;C=B;B=A;A=(t1+t2)>>>0;}const v=[A,B,C,D,E,F,G,J];for(let i=0;i<8;i++)H[i]=(H[i]+v[i])>>>0;}return H.map(v=>v.toString(16).padStart(8,\"0\")).join(\"\");";
export const sha1jsBody="const raw=unescape(encodeURIComponent(input)),a=Array.from(raw,c=>c.charCodeAt(0)),L=a.length;a.push(128);while(a.length%64!==56)a.push(0);const hi=Math.floor(L/536870912),lo=(L*8)>>>0;for(let i=3;i>=0;i--)a.push((hi>>>(i*8))&255);for(let i=3;i>=0;i--)a.push((lo>>>(i*8))&255);const H=[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0],rot=(x,n)=>(x<<n)|(x>>>(32-n)),w=new Array(80);for(let off=0;off<a.length;off+=64){for(let i=0;i<16;i++){const k=off+4*i;w[i]=(a[k]<<24)|(a[k+1]<<16)|(a[k+2]<<8)|a[k+3];}for(let i=16;i<80;i++)w[i]=rot(w[i-3]^w[i-8]^w[i-14]^w[i-16],1);let[A,B,C,D,E]=H;for(let i=0;i<80;i++){const f=i<20?(B&C)|(~B&D):i<40?B^C^D:i<60?(B&C)|(B&D)|(C&D):B^C^D,k=i<20?0x5a827999:i<40?0x6ed9eba1:i<60?0x8f1bbcdc:0xca62c1d6,t=(rot(A,5)+f+E+k+w[i])>>>0;E=D;D=C;C=rot(B,30);B=A;A=t;}const v=[A,B,C,D,E];for(let i=0;i<5;i++)H[i]=(H[i]+v[i])>>>0;}return H.map(v=>v.toString(16).padStart(8,\"0\")).join(\"\");";
export async function publishTopicBundle(env,task){
 const {tools,load,store,text}=env,repo="Rogerhu12/math-research-public",p="topics/visible-flex-larger-amplitude/";
 const u=r=>{let s=r.structuredContent??r;while(s?.structuredContent)s=s.structuredContent;return s;},j=r=>{const s=u(r);return typeof s.content==="string"?JSON.parse(s.content):s;};
 const len=new Function("input",load("utf8LengthBody")),s1=new Function("input",load("sha1jsBody")),gb=b=>s1("blob "+len(b)+"\0"+b);
 const blockRE=/<!-- visible-larger-parallel-(\d+):start -->[\s\S]*?<!-- visible-larger-parallel-\1:end -->/g;
 const outside=b=>b.replace(blockRE,"").trimEnd();
 const base=load(task+"-publish-base-documents"),planned=load(task+"-publish-planned-documents"),adds=load(task+"-publish-added-records")??[],dels=load(task+"-publish-delete-records")??[],replaces=load(task+"-publish-replace-records")??[];
 for(let attempt=0;attempt<8;attempt++){
  const head=j(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/ref/heads/main"})).object.sha;
  const urls=["https://api.github.com/repos/"+repo+"/git/commits/"+head,"https://api.github.com/repos/"+repo+"/contents?ref="+head,"https://api.github.com/repos/"+repo+"/contents/"+p.slice(0,-1)+"?ref="+head];
  const rr=await Promise.allSettled(urls.map(url=>tools.mcp__codex_apps__github_fetch({url})));for(const r of rr)if(r.status!=="fulfilled")throw Error("metadata fetch failed "+String(r.reason));
  const [commit,root,topic]=rr.map(r=>j(r.value));
  if(root.find(x=>x.name==="README.md").sha!=="282e86b03385d3b6245ce7100ae2e2af7b103c2d"||topic.find(x=>x.name==="README.md").sha!=="bff8aea253a9e6a7a4fac28d810ac454c5499fec")throw Error("README changed; read differences before continuing");
  for(const name of ["log.md","open.md"])if(base[p+name]!==undefined&&topic.find(x=>x.name===name).sha!==gb(base[p+name]))throw Error("concurrent topic edit "+name);
  const hm=topic.find(x=>x.name==="HANDOFF.md");if(!hm||hm.size>=100000)throw Error("HANDOFF size");
  const hb=hm.sha===gb(base[p+"HANDOFF.md"])?base[p+"HANDOFF.md"]:u(await tools.mcp__codex_apps__github_fetch_blob({repository_full_name:repo,blob_sha:hm.sha})).content;
  if(outside(hb)!==outside(base[p+"HANDOFF.md"]))throw Error("concurrent HANDOFF content edit");
  const topics=j(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/trees/"+root.find(x=>x.name==="topics").sha}));
  const tm=topics.tree.find(x=>x.path==="visible-flex-larger-amplitude");
  const tree=j(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/trees/"+tm.sha+"?recursive=1"}));
  if(tree.truncated)throw Error("topic tree truncated");
  const bypath=new Map(tree.tree.map(x=>[p+x.path,x]));
  for(const x of [...dels,...replaces]){const n=bypath.get(x.path);if(!n||n.size!==x.bytes||n.sha!==x.sha)throw Error("changed existing input "+x.path);}
  for(const x of adds){const n=bypath.get(x.path);if(n&&(n.sha!==x.sha||n.size!==x.bytes))throw Error("new path collision "+x.path);if(x.bytes>=100000)throw Error("new API source too large "+x.path);}
  const docs={...base};for(const[path,body]of Object.entries(planned))docs[path]=body.replaceAll("__FRESH_HEAD__",head);
  const overrides=new Set(load(task+"-publish-explicit-slot-overrides")??[]);
  for(const match of hb.matchAll(blockRE)){
   if(overrides.has(Number(match[1])))continue;
   const re=new RegExp("<!-- visible-larger-parallel-"+match[1]+":start -->[\\s\\S]*?<!-- visible-larger-parallel-"+match[1]+":end -->");
   if(re.test(docs[p+"HANDOFF.md"]))docs[p+"HANDOFF.md"]=docs[p+"HANDOFF.md"].replace(re,match[0]);
   else docs[p+"HANDOFF.md"]=docs[p+"HANDOFF.md"].trimEnd()+"\n\n"+match[0]+"\n";
  }
  docs[p+"HANDOFF.md"]=docs[p+"HANDOFF.md"].replace(/云核至`[0-9a-f]{40}`/,"云核至`"+head+"`");
  const entries=load(task+"-publish-entries").map(x=>({...x}));for(const e of entries)if(planned[e.path]!==undefined)e.content=docs[e.path];
  let total=tree.tree.filter(x=>x.type==="blob").reduce((a,x)=>a+x.size,0),before=total;
  for(const e of entries){if(!e.path.startsWith(p))continue;const old=bypath.get(e.path);let size=0;if(e.content!==undefined)size=len(e.content);else if(e.sha!==null){const a=adds.find(x=>x.path===e.path&&x.sha===e.sha);if(!a)throw Error("size record absent "+e.path);size=a.bytes;}total+=size-(old?.size??0);}
  if(total>200000000||len(docs[p+"HANDOFF.md"])>=10000||len(docs[p+"open.md"])>=30000||len(docs[p+"log.md"])>=100000)throw Error("publication capacity");
  store(task+"-publish-current-topic-tree",tree);store(task+"-publish-head",head);store(task+"-publish-documents",docs);store(task+"-publish-predicted-bytes",total);store(task+"-publish-entries",entries);
  const t=u(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:commit.tree.sha,tree_elements:entries}));if(!t.sha)throw Error(JSON.stringify(t));
  const c=u(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:head,tree_sha:t.sha,message:load(task+"-publish-message")}));if(!c.sha)throw Error(JSON.stringify(c));
  const result=u(await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:"main",expected_sha:head,sha:c.sha,force:false}));
  store(task+"-created-commit",c);store(task+"-update-result",result);text({task,attempt,parent:head,commit:c.sha,current_topic_bytes:before,predicted_topic_bytes:total,result});
  if(result.success){const out={sha:c.sha,parent:head,predicted_topic_bytes:total};store(task+"-published",out);return out;}
  const next=j(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/ref/heads/main"})).object.sha;
  if(next===c.sha){const out={sha:c.sha,parent:head,predicted_topic_bytes:total,ref_confirmed_after_unknown_result:true};store(task+"-published",out);return out;}
  if(next===head)throw Error("update failed without concurrent movement: "+JSON.stringify(result));
 }
 throw Error("eight ordinary races; continue from fresh HEAD without force");
}
