'use strict';
// Exact rational aggregation of already proved local operator error bounds.
// This is not a global product bound: actual prefix inverses remain required.
function gcd(a,b){while(b){const c=a%b;a=b;b=c;}return a<0n?-a:a;}
function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');
 if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
function cmp(a,b){const x=a.n*b.d-b.n*a.d;return x<0n?-1:x>0n?1:0;}
function rat(s){const z=String(s).split('/');return Q(z[0],z.length===2?z[1]:1);}
function decimal(s){
 s=String(s).trim();const match=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(s);
 if(!match||!(match[2]||match[3]))throw Error('invalid finite decimal '+s);
 let n=BigInt((match[2]||'')+(match[3]||''));if(match[1]==='-')n=-n;
 const shift=Number(match[4]||0)-(match[3]||'').length;
 return shift>=0?Q(n*10n**BigInt(shift)):Q(n,10n**BigInt(-shift));}
function arbUpper(s){
 s=String(s).trim();if(s[0]==='['&&s[s.length-1]===']')s=s.slice(1,-1).trim();
 const pieces=s.split('+/-');
 if(pieces.length===1)return decimal(s);
 if(pieces.length!==2)throw Error('invalid finite ball '+s);
 const midpoint=pieces[0].trim()?decimal(pieces[0]):Q(0);
 const radius=decimal(pieces[1]);if(radius.n<0n)throw Error('negative ball radius');
 return add(midpoint,radius);}
function ceilDecimal(q,places){
 if(q.n<0n)throw Error('expected nonnegative bound');
 const factor=10n**BigInt(places);let value=(q.n*factor+q.d-1n)/q.d;
 const s=value.toString().padStart(places+1,'0');
 return places?s.slice(0,-places)+'.'+s.slice(-places):s;}
function qstr(q){return q.n.toString()+'/'+q.d.toString();}
function sha256(text){
 const bytes=[];
 for(const character of text){let x=character.codePointAt(0);
  if(x<128)bytes.push(x);else if(x<2048)bytes.push(192|(x>>6),128|(x&63));
  else if(x<65536)bytes.push(224|(x>>12),128|((x>>6)&63),128|(x&63));
  else bytes.push(240|(x>>18),128|((x>>12)&63),128|((x>>6)&63),128|(x&63));}
 const length=BigInt(bytes.length)*8n;bytes.push(128);while(bytes.length%64!==56)bytes.push(0);
 for(let shift=56n;shift>=0n;shift-=8n)bytes.push(Number((length>>shift)&255n));
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
 const rotr=(x,n)=>(x>>>n)|(x<<(32-n));
 for(let offset=0;offset<bytes.length;offset+=64){
  const W=Array(64);for(let j=0;j<16;j++)W[j]=((bytes[offset+4*j]<<24)|(bytes[offset+4*j+1]<<16)|(bytes[offset+4*j+2]<<8)|bytes[offset+4*j+3])>>>0;
  for(let j=16;j<64;j++){let x=W[j-15],y=W[j-2];let s0=rotr(x,7)^rotr(x,18)^(x>>>3),s1=rotr(y,17)^rotr(y,19)^(y>>>10);W[j]=(W[j-16]+s0+W[j-7]+s1)>>>0;}
  let [a,b,c,d,e,f,g,h]=H;
  for(let j=0;j<64;j++){const S1=rotr(e,6)^rotr(e,11)^rotr(e,25),ch=(e&f)^(~e&g);
   const t1=(h+S1+ch+K[j]+W[j])>>>0;
   const S0=rotr(a,2)^rotr(a,13)^rotr(a,22),maj=(a&b)^(a&c)^(b&c),t2=(S0+maj)>>>0;
   h=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
  const state=[a,b,c,d,e,f,g,h];for(let j=0;j<8;j++)H[j]=(H[j]+state[j])>>>0;
 }
 return H.map(x=>x.toString(16).padStart(8,'0')).join('');
}
function collect(inputs){
 const docs=inputs.map(input=>({input,doc:JSON.parse(input.text)})).sort((a,b)=>a.doc.first_span-b.doc.first_span);
 if(!docs.length)throw Error('no actual manifests');
 const identity=JSON.stringify(docs[0].doc.identity),rows=[],original=[];
 let expected=0,cursor=Q(0),sum=Q(0),maximum=Q(0),rejected=0;
 for(const {input,doc} of docs){
  if(!doc.complete||doc.terminal_failures.length)throw Error('incomplete native piece '+input.path);
  if(JSON.stringify(doc.identity)!==identity)throw Error('different uniform parameter/source identity');
  if(doc.first_span!==expected)throw Error('common-span gap or overlap');
  expected=doc.last_span_exclusive;original.push(...doc.original_spans);
  rejected+=doc.rejected_boxes.length;
  for(const leaf of doc.complete_leaves){
   const [a,b]=leaf.exact_interval.map(rat);
   if(cmp(a,cursor)!==0||cmp(a,b)>=0)throw Error('accepted leaf gap or overlap');
   cursor=b;
   const bound=arbUpper(leaf.transfer_error.upper);
   if(bound.n<0n)throw Error('negative local bound');
   sum=add(sum,bound);if(cmp(bound,maximum)>0)maximum=bound;
   rows.push({path:leaf.path,report_sha256:leaf.sha256,arrays_sha256:leaf.arrays.sha256,
       exact_interval:leaf.exact_interval,local_error_upper_exact_rational:qstr(bound)});
  }
 }
 if(expected!==174||original.length!==174||cmp(cursor,Q(1,4))!==0)throw Error('not the full 174-span quarter core');
 let oc=Q(0);
 original.forEach((r,j)=>{const [a,b]=r.exact_interval.map(rat);
  if(r.index!==j||cmp(a,oc)!==0||cmp(a,b)>=0)throw Error('original common spans incomplete');oc=b;});
 if(cmp(oc,Q(1,4))!==0)throw Error('original spans miss the quarter cut');
 const id=docs[0].doc.identity;
 if(id.exact_parameter_half_width!=='1/1000000000'||!id.uniform_in_the_entire_real_parameter_interval)
   throw Error('not the actual eta family');
 return {kind:'exact_rational_sum_of_paid_uniform_local_transfer_errors',complete:true,
  actual_run_id:'43307149760',identity:id,original_common_spans:174,accepted_leaves:rows.length,rejected_boxes:rejected,
  exact_positive_coverage:['0','1/4'],additive_local_error_sum_exact_rational:qstr(sum),
  additive_local_error_sum_decimal_upper:ceilDecimal(sum,24),
  maximum_local_error_exact_rational:qstr(maximum),maximum_local_error_decimal_upper:ceilDecimal(maximum,24),
  arithmetic:'Decimal midpoint and radius strings are parsed as exact BigInt rationals. Each recorded Arb upper string is enlarged by its own printed decimal radius, then all 175 numbers are added exactly. Decimal display is rounded upward by integer ceiling.',
  input_manifests:docs.map(({input})=>({path:input.path,sha256:sha256(input.text),git_blob_sha:input.git_blob_sha||null})),
  local_error_inputs:rows,
  whole_core_product_error_certified:false,whole_core_DN_certified:false,
  scope:'This is the exact additive input sum for the ordered prefix-inverse bound, not the global transfer error. Actual matrix prefixes, their inverse norms and the finite B-block still require the native collector; no binary data was read through an integration.'};
}
if(typeof module!=='undefined')module.exports={collect,sha256,arbUpper};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('fs'),path=require('path');const root=process.argv[2],out=process.argv[3];
 if(!root||!out)throw Error('usage: node script.cjs COVER_ROOT OUT.json');
 const inputs=fs.readdirSync(root).filter(x=>x.startsWith('block_')).map(x=>{
  const p=path.join(root,x,'manifest.json');return {path:p,text:fs.readFileSync(p,'utf8')};});
 const report=collect(inputs);report.source_sha256=sha256(fs.readFileSync(__filename,'utf8'));
 fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
 console.log(JSON.stringify({accepted_leaves:report.accepted_leaves,sum_upper:report.additive_local_error_sum_decimal_upper,
   maximum_upper:report.maximum_local_error_decimal_upper}));
}
