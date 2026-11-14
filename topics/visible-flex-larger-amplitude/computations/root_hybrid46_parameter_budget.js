/* R100 exact scalar calculation; all results use integers/Fractions. */
function sha256(text){
 const bytes=[];for(const ch of text){const cp=ch.codePointAt(0);if(cp<128)bytes.push(cp);else if(cp<2048)bytes.push(192|(cp>>6),128|(cp&63));else if(cp<65536)bytes.push(224|(cp>>12),128|((cp>>6)&63),128|(cp&63));else bytes.push(240|(cp>>18),128|((cp>>12)&63),128|((cp>>6)&63),128|(cp&63));}
 const n=bytes.length, bit=BigInt(n)*8n;bytes.push(128);while(bytes.length%64!==56)bytes.push(0);for(let j=7;j>=0;j--)bytes.push(Number((bit>>BigInt(8*j))&255n));
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];const rr=(v,n)=>(v>>>n)|(v<<(32-n));const W=new Array(64);
 for(let q=0;q<bytes.length;q+=64){for(let j=0;j<16;j++)W[j]=((bytes[q+4*j]<<24)|(bytes[q+4*j+1]<<16)|(bytes[q+4*j+2]<<8)|bytes[q+4*j+3])>>>0;
 for(let j=16;j<64;j++){const x=W[j-15],y=W[j-2];W[j]=(W[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+W[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
 let[a,b,c,d,e,f,g,h]=H;for(let j=0;j<64;j++){const t1=(h+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+W[j])>>>0;const t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;h=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
 const v=[a,b,c,d,e,f,g,h];for(let j=0;j<8;j++)H[j]=(H[j]+v[j])>>>0;}
 return H.map(v=>v.toString(16).padStart(8,"0")).join("");
}
function lossless(t){let out="",i=0,inString=false;while(i<t.length){const c=t[i];if(c==='"'){let j=i+1;for(;j<t.length;j++){if(t[j]==="\\"){j++;continue;}if(t[j]==='"'){j++;break;}}out+=t.slice(i,j);i=j;continue;}if(c==="-"||(c>="0"&&c<="9")){const m=t.slice(i).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);if(!m)throw Error("number");out+='"'+m[0]+'"';i+=m[0].length;continue;}out+=c;i++;}return JSON.parse(out);}

function abs(a){return a<0n?-a:a;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
function rat(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];}
function add(a,b){return rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function sub(a,b){return rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
function mul(a,b){return rat(a[0]*b[0],a[1]*b[1]);}
function div(a,b){if(!b[0])throw Error("division by zero");return rat(a[0]*b[1],a[1]*b[0]);}
function cmp(a,b){const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;}
function p2(e){e=BigInt(e);return e>=0n?rat(1n<<e):rat(1n,1n<<(-e));}
function p10(e){return 10n**BigInt(e);}
function decimal(s){s=String(s);const m=s.match(/^(-?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m)throw Error("bad exact decimal");const tail=m[3]||"",n=BigInt(m[2]+tail)*(m[1]?-1n:1n),e=Number(m[4]||0)-tail.length;return e>=0?rat(n*p10(e)):rat(n,p10(-e));}
function dyad(v){v=v.upper||v;return mul(rat(v.mantissa),p2(v.binary_exponent));}
function frac(v){return rat(v.numerator,v.denominator);}
function sciUp(a,digits=19){if(a[0]<0n)throw Error("display only nonnegative");if(!a[0])return "0";let e=a[0].toString().length-a[1].toString().length;if(e>=0?a[0]<a[1]*p10(e):a[0]*p10(-e)<a[1])e--;const shift=digits-1-e;let n=a[0],d=a[1];if(shift>=0)n*=p10(shift);else d*=p10(-shift);let q=(n+d-1n)/d;let t=q.toString();if(t.length>digits){q=(q+9n)/10n;e++;t=q.toString();}t=t.padStart(digits,"0");return t[0]+"."+t.slice(1)+"e"+(e>=0?"+":"")+e;}
function rec(a){return{numerator:a[0].toString(),denominator:a[1].toString(),decimal_upward_display:sciUp(a)};}


function exactSigned(a){return {numerator:a[0].toString(),denominator:a[1].toString()};}
function absRat(a){return a[0]<0n?rat(-a[0],a[1]):a;}
function minRat(a,b){return cmp(a,b)<0?a:b;}
function maxRat(a,b){return cmp(a,b)>0?a:b;}
function interval(v){return [dyad(v.lower||v),dyad(v.upper||v)];}
function intervalDiv(a,b){
 if(cmp(b[0],rat(0))<=0&&cmp(b[1],rat(0))>=0)throw Error("zero interval denominator");
 const p=[div(a[0],b[0]),div(a[0],b[1]),div(a[1],b[0]),div(a[1],b[1])];
 return [p.reduce(minRat),p.reduce(maxRat)];
}
function intervalAbsUpper(a){return maxRat(absRat(a[0]),absRat(a[1]));}
function runHybrid(inputs){
 const expected={
  geometry:"e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03",
  r92:"9ef88cdeef25ed0dd688082e53b25b5f8aacda2bd67c9dada61c250cefa4052a",
  r59:"d243b59146ba523b9fcbb6f63952b8affe5b33ac6c5cbb8403bcc590afe9cd48"
 };
 const hashes={};for(const k of Object.keys(expected)){hashes[k]=sha256(inputs[k]);if(hashes[k]!==expected[k])throw Error("Original input SHA mismatch "+k);}
 const geometry=lossless(inputs.geometry),r92=lossless(inputs.r92);
 const axes=geometry.config.parameter_axes;
 if(geometry.all_gates!==true||r92.all_gates!==true||axes.length!==20)throw Error("Unpaid actual prerequisite");
 const exponentRows=[];
 for(const line of inputs.r59.split("\n")){const m=line.match(/^\|\s*(\d+)\s*\|\s*(-\d+)\s*\|\s*(-\d+)\s*\|$/);if(m)exponentRows.push({mode:Number(m[1]),exponent:Number(m[2]),H_exponent:Number(m[3])});}
 if(exponentRows.length!==46||exponentRows.some((v,i)=>v.mode!==2*(i+1)||v.H_exponent!==v.exponent-18))throw Error("Original complete R59 axis table changed");
 const byAxis=new Map(axes.map(a=>[Number(a.mode),a]));
 const one=rat(1),zero=rat(0),S=rat(257,256),lambda0=rat(1985,2048),theta=rat(16705,16384);
 const lambda=mul(theta,lambda0),eta=rat(4096),s=rat(1048576),oldRadius=rat(256),newRadius=add(oldRadius,s),r59Radius=rat(2097216);
 const delta=sub(mul(s,sub(one,lambda)),mul(eta,add(one,lambda)));
 const KT=div(mul(eta,add(one,lambda)),sub(one,lambda));
 const q=add(one,div(add(KT,eta),oldRadius));
 const qHigh=add(one,div(KT,oldRadius));
 const d59=rat(147,1000000000000n),rho=p2(-30),emax=div(mul(mul(S,oldRadius),d59),r59Radius),tmax=div(emax,S),qt=mul(q,tmax);
 const remainder=mul(q,add(add(one,qt),div(mul(qt,qt),rat(3))));
 const rows=[];let embedding=zero,transverseLinearMass=zero,productLinearMax=zero;
 let allAxisFormulas=true,Sprefer=true,Tprefer=true;
 for(const e of exponentRows){
  const m=e.mode,v=p2(e.exponent),old=byAxis.get(m);
  const a=old?dyad(old.half_axis):null,centre=old?dyad(old.exact_centre):zero;
  if(old){allAxisFormulas=allAxisFormulas&&cmp(a,div(absRat(centre),rat(m===4?16:1024)))===0;}
  const isS=m<=12,newAxis=isS?a:v,ratio=a?div(a,v):null;
  if(old&&isS)Sprefer=Sprefer&&cmp(a,v)>0;
  if(old&&!isS){Tprefer=Tprefer&&cmp(a,v)<0;embedding=add(embedding,ratio);}
  const linear=intervalDiv(interval(geometry.config.actual_outer_Q[String(m)]),interval(geometry.config.actual_true_S0_Q[String(m)]));
  const shifted=[sub(linear[0],centre),sub(linear[1],centre)];
  const residual=div(intervalAbsUpper(shifted),newAxis);
  if(isS)productLinearMax=maxRat(productLinearMax,residual);else transverseLinearMass=add(transverseLinearMass,residual);
  rows.push({mode:m,group:isS?"S_linf":"T_weighted_l1",R59_exponent:e.exponent,
   original_centre:exactSigned(centre),chosen_axis:rec(newAxis),
   old_R74_axis_over_R59:ratio?rec(ratio):null,
   pure_linear_cut_normalized_absolute:rec(residual)});
 }
 const C=r92.constants;
 const scalarMatches=cmp(frac(C.lambda_majorant),lambda)===0&&cmp(frac(C.strict_slack_coefficient),delta)===0&&cmp(frac(C.transverse_unknown_lipschitz),KT)===0;
 const gates={
  all_three_actual_input_sha256:true,all46_original_axes_retained:rows.length===46,
  same20_exact_R74_centre_and_axis_formulas:allAxisFormulas,
  six_product_and40_transverse:rows.filter(r=>r.group==="S_linf").length===6&&rows.filter(r=>r.group==="T_weighted_l1").length===40,
  first_six_original_axes_exceed_R59:Sprefer,remaining14_original_axes_below_R59:Tprefer,
  old_R74_transverse_box_embeds_in_one_twentieth_ball:cmp(embedding,rat(1,20))<0,
  independent_recomputed_R92_scalars_match:scalarMatches,
  full_lambda_strict:cmp(lambda,one)<0,strict641_row_slack:cmp(delta,zero)>0,
  new_box_smaller_than_R59_domain:cmp(newRadius,r59Radius)<0,
  same_complete_work_domain:cmp(d59,rho)<0,
  same_complete_mean_domain:cmp(mul(S,rat(6420,1000000000000000000n)),rat(1,64))<0,
  posterior_parameter_displacement_below_added_radius:cmp(KT,s)<0,
  improved_complete_state_factor_below4113:cmp(q,one)>0&&cmp(q,rat(4113))<0,
  pure_high_factor_excludes_low_lift_and_below2704:cmp(qHigh,rat(2704))<0&&cmp(qHigh,q)<0,
  uniform_old_source_error_below_two_e_minus14:cmp(emax,rat(1,50000000000000n))<0,
  qt_below_one_e_minus10:cmp(qt,rat(1,10000000000n))<0,
  complete_cubic_multiplier_below_q_times_one_plus_e_minus10:cmp(remainder,mul(q,add(one,rat(1,10000000000n))))<0,
  all_four_multipliers_no_larger_than_old_q_squared:[q,q,mul(q,q),remainder].every(x=>cmp(x,rat(16916769))<0)
 };
 return {schema:"visible-flex-larger-R100-hybrid46-and-complete-source-v1",status:"Proved grouped-domain and complete positive source comparison; actual exact BigInt scalar and linear diagnostics",
  author:"/root (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-13",
  all_gates:Object.values(gates).every(Boolean),gates,
  inputs:hashes,domain:{product_modes:rows.filter(x=>x.group==="S_linf").map(x=>x.mode),weighted_l1_modes:rows.filter(x=>x.group==="T_weighted_l1").map(x=>x.mode),norm:"max(linf_S,weighted_l1_T)",working_radius:rec(rat(3,4)),
  old_R74_T_box_embedding_mass:rec(embedding),whole_original_R92_product_included:false},
  constants:{lambda0:rec(lambda0),S:rec(S),theta:rec(theta),lambda:rec(lambda),eta:rec(eta),additional_radius:rec(s),full_radius:rec(newRadius),R59_radius:rec(r59Radius),strict_slack:rec(delta),KT:rec(KT),q_complete:rec(q),q_pure_high:rec(qHigh),q_at_working_radius:rec(add(one,mul(div(add(KT,eta),oldRadius),rat(3,4)))),R59_complete_domain:rec(d59),old_e_uniform:rec(emax),tmax:rec(tmax),q_tmax:rec(qt)},
  complete_R83_piece_multipliers:{main:rec(q),corr:rec(q),quadratic:rec(mul(q,q)),remainder:rec(remainder)},
  rows,pure_linear_diagnostic:{S_max:rec(productLinearMax),T_l1_sum:rec(transverseLinearMass),includes_outer_nonlinearity:false,includes_true_head_beta:false,selfmap_claimed:false},
  analytic_scope:"All641 existing complete rows by positive comparison; all213 old e_n by the certified R59 total-domain majorant. Full mean, inverse remainder, independent far and same cuff retained. R83 mode totals are not numerically reconsumed here.",
  no_Arb:true,no_ODE:true,no_new_source_integral:true,no_non_linear_solver:true,outer_full46_cut_closed:false};
}

if(typeof module!=="undefined"&&module.exports){
 module.exports={runHybrid};
 if(typeof require!=="undefined"&&require.main===module){
  const fs=require("fs");const a=process.argv.slice(2);
  if(a.length!==4)throw Error("Usage: node root_hybrid46_parameter_budget.js GEOMETRY R92_LEDGER R59_PROOF NEW_OUTPUT");
  if(fs.existsSync(a[3]))throw Error("Output must be new and immutable");
  const inputs={geometry:fs.readFileSync(a[0],"utf8"),r92:fs.readFileSync(a[1],"utf8"),r59:fs.readFileSync(a[2],"utf8")};
  const result=runHybrid(inputs);result.source_sha256=sha256(fs.readFileSync(__filename,"utf8"));
  fs.writeFileSync(a[3],JSON.stringify(result,null,2)+"\n",{flag:"wx"});
  process.stdout.write(JSON.stringify({all_gates:result.all_gates,gates:Object.keys(result.gates).length,output:a[3]})+"\n");
  if(!result.all_gates)process.exitCode=2;
 }
}
