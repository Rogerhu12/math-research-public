"use strict";
const fs=require("fs"),crypto=require("crypto");
const INPUT={"q":"225196170077769188459647075003723446506290334538374935594311805764766375462943717166814768844511612408106442292450018627544384538312646994045716899229168141998348680872046002490066651342968053955905931120521143569132718008762168959999","fEven":[-43,3311,-76153,826804,-5167525,20764055,-57500460,115000920,-171655785,195747825,-173376645,120609840,-66335412,28915436,-9970840,2701776,-567987,90687,-10621,860,-43,1],"gDesc":["-16327464","-32688421","636891359","1274935920","-11499057732","-23015414551","127514905483","255172444283","-971797090418","-1944212323820","5396336469305","10792866388653","-22587509701367","-45159020373021","72727111706911","145335749598988","-182217408061576","-363930604369013","357097929861227","712705416840667","-547342458917037","-1091448273129748","652960441564111","1300653911277333","-600343727043585","-1194244952187508","418862136280342","831849342428810","-216820614311075","-429721377031810","80633423316371","159411803435470","-20568043093764","-40542627535269","3358230515416","6597209427096","-314344985758","-615241450575","13843605713","26972100150","-181634213","-351643330"],"e":[1,-14,-19,8,17,20,21,7,-12,-4,13,-10,11,18,6,2,15,5,16,-9,-3,-1,14,19,-8,-17,-20,-21,-7,12,4,-13,10,-11,-18,-6,-2,-15,-5,-16,9,3]};

function assert(x,m){if(!x)throw Error(m);}
function sign(v){return v<0n?-1:v>0n?1:0;}
function dyadEval(a,n,den){let y=0n,d=1n;for(let j=a.length-1;j>=0;j--){y=y*n+a[j]*d*den;d*=den;}return y;}
function intervalEval(a,n,den){let lo=0n,hi=0n,d=1n;for(let j=a.length-1;j>=0;j--){let v=[lo*n,lo*(n+1n),hi*n,hi*(n+1n)];let nl=v.reduce((x,y)=>x<y?x:y),nh=v.reduce((x,y)=>x>y?x:y);d*=den;lo=nl+a[j]*d;hi=nh+a[j]*d;}return [lo,hi,d];}
function rootBound(C){const f=Array(43).fill(0n);C.fEven.forEach((v,j)=>f[2*j]=BigInt(v));const g=C.gDesc.slice().reverse().map(BigInt);let k=1,ints=[],powers=[];for(let j=0;j<42;j++){let b=40,D=1n<<40n,n=BigInt(Math.floor(2*Math.cos(2*Math.PI*k/172)*2**40));let s=sign(dyadEval(f,n,D)),t=sign(dyadEval(f,n+1n,D));assert(s*t<0,"seed interval");while(b<220){n*=2n;D*=2n;const m=sign(dyadEval(f,n+1n,D));assert(m!==0,"dyadic root");if(m===s)n++;else t=m;b++;}assert(sign(dyadEval(f,n,D))*sign(dyadEval(f,n+1n,D))<0,"root interval");let [a,bv,d]=intervalEval(g,n,D);let jl=(2n*D-n-1n)**22n,jh=(2n*D-n)**22n,den=d*D**22n;let vals=[a*jl,a*jh,bv*jl,bv*jh],nu=vals.reduce((x,y)=>{y=y<0n?-y:y;return x>y?x:y;},0n);let u=nu.toString(2).length-den.toString(2).length;if(u>=0){if(nu>(den<<BigInt(u)))u++;}else if((nu<<BigInt(-u))>den)u++;powers.push(u);ints.push({index:j,angle_index:k,lo_num:n.toString(),denominator_power:220,h_log2_upper:u});k=(3*k+86)%172;}assert(k===1,"angle period");let ns=ints.map(x=>BigInt(x.lo_num)).sort((a,b)=>a<b?-1:1);for(let i=1;i<42;i++)assert(ns[i-1]+1n<ns[i],"disjoint");const e=C.e.map(x=>(x+43)%43),loga=Array.from({length:42},(_,i)=>e.reduce((s,x,j)=>s+x*powers[(i+j)%42],0)),alpha=loga.map(x=>Math.ceil(x/43));assert(alpha.every(x=>x>=0),"positive bounds");const R=alpha.reduce((s,x)=>s+(1n<<BigInt(x)),0n),B=(R+1n)**43n;return {intervals:ints,positive_exponents:e,log2_a_upper:loga,log2_alpha_upper:alpha,theta_root_bound:R.toString(),uniform_coefficient_bound:B.toString(),bound_bits:B.toString(2).length,required_crt_bits:(2n*B).toString(2).length};}

function modular43(C){
let p=0;function mul(a,b){return a*b%p;}function pw(a,n){let s=1;for(;n>0;n=Math.floor(n/2),a=mul(a,a))if(n%2)s=mul(s,a);return s;}function inv(a){if(a===0)throw Error("inverse zero");return pw(a,p-2);}function smod(s){let neg=s[0]==="-",a=0;for(let i=neg?1:0;i<s.length;i++)a=(a*10+Number(s[i]))%p;return neg&&a?p-a:a;}function add(a,b){let x=a+b;return x>=p?x-p:x;}function ev(a,x){let y=0;for(let j=a.length-1;j>=0;j--)y=add(mul(y,x),a[j]);return y;}const ee=C.e.map(x=>(x+43)%43),dd=ee.map((x,j)=>(ee[(j+41)%42]-3*x)/43);
function prime(n){if(n<2)return false;for(const a of[2,3,5,7,11,13,17,19,23,29,31,37]){if(n===a)return true;if(n%a===0)return false;}const old=p;p=n;let d=n-1,s=0;while(d%2===0){d/=2;s++;}for(const a of[2,3,5,7,11]){let x=pw(a,d);if(x===1||x===n-1)continue;let ok=false;for(let j=1;j<s;j++){x=mul(x,x);if(x===n-1){ok=true;break;}}if(!ok){p=old;return false;}}p=old;return true;}
function rm(a,b,aa){const c=Array(85).fill(0);for(let i=0;i<43;i++)if(a[i])for(let j=0;j<43;j++)if(b[j])c[i+j]=add(c[i+j],mul(a[i],b[j]));for(let j=84;j>=43;j--)c[j-43]=add(c[j-43],mul(c[j],aa));return c.slice(0,43);}
function poly(pp,seed=2){p=pp;if(p>50000000)throw Error("safe integer prime bound");let xi;for(let b=seed;;b++){let x=pw(b,(p-1)/172);if(pw(x,86)!==1&&pw(x,4)!==1){xi=x;break;}}let gg=C.gDesc.slice().reverse().map(smod),ff=Array(43).fill(0);C.fEven.forEach((x,j)=>ff[2*j]=(x%p+p)%p);const rr=Array(42),h=Array(42),aa=Array(42),ww=Array(42);rr[0]=add(xi,inv(xi));for(let l=0;l<42;l++){if(ev(ff,rr[l]))throw Error("f root");h[l]=mul(ev(gg,rr[l]),pw((2-rr[l]+p)%p,22));if(h[l]===0)throw Error("h zero");const r3=mul(mul(rr[l],rr[l]),rr[l]),rn=(mul(3,rr[l])-r3+p)%p;if(l<41)rr[l+1]=rn;else if(rn!==rr[0])throw Error("r period");}if(new Set(rr).size!==42)throw Error("r distinct");
for(let l=0;l<42;l++){aa[l]=ww[l]=1;for(let j=0;j<42;j++){aa[l]=mul(aa[l],pw(h[(l+j)%42],ee[j]));ww[l]=mul(ww[l],pw(inv(h[(l+j)%42]),-dd[j]));}}
for(let l=0;l<42;l++)if(aa[(l+1)%42]!==mul(pw(aa[l],3),pw(ww[l],43)))throw Error("sigma a");
let cc=Array(42).fill(1),tt=Array(43).fill(0),k=1;for(let j=0;j<42;j++){if(tt[k])throw Error("duplicate power");tt[k]=cc[0];const cn=Array(42);for(let l=0;l<42;l++)cn[l]=mul(mul(cc[(l+1)%42],pw(ww[l],k)),pw(aa[l],Math.floor(3*k/43)));cc=cn;k=3*k%43;}if(k!==1||cc.some(x=>x!==1))throw Error("lift period");
let power=Array(43).fill(0);power[0]=1;const tr=Array(44).fill(0),out=Array(44).fill(0);out[0]=1;for(let j=1;j<=43;j++){power=rm(power,tt,aa[0]);tr[j]=mul(43,power[0]);let s=0;for(let i=1;i<=j;i++)s=add(s,mul(out[j-i],tr[i]));out[j]=s?mul(p-s,inv(j)):0;}if(out[1]!==0)throw Error("nonzero trace");return out;}
return {prime,poly};
}

function runCRT(C,modsrc,bound,state,count){
const api=Function("C",modsrc+"\nreturn modular43(C);")(C);bound=BigInt(bound);
let M=BigInt(state.modulus),cs=state.coefficients.map(BigInt),p=state.next;
function inv(a,m){let b=m,x=1n,y=0n;while(b){const q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}if(a!==1n)throw Error("CRT non-coprime");return (x%m+m)%m;}
for(let n=0;n<count&&M<=2n*bound;){if(!api.prime(p)){p+=172;continue;}const v=api.poly(p),P=BigInt(p),iv=inv(M%P,P);for(let j=0;j<44;j++){let t=((BigInt(v[j])-cs[j]%P)*iv)%P;if(t<0n)t+=P;cs[j]+=M*t;}M*=P;state.rows.push({prime:p,coefficients:v});p+=172;n++;}
state.next=p;state.modulus=M.toString();state.coefficients=cs.map(String);return state;
}
function validateRootBound(C,B){
const f=Array(43).fill(0n);C.fEven.forEach((x,j)=>f[2*j]=BigInt(x));
const phi=Array(85).fill(0n);for(let k=0;k<=42;k++){let bc=1n;for(let j=0;j<=k;j++){phi[42+k-2*j]+=f[k]*bc;bc=bc*BigInt(k-j)/BigInt(j+1);}}
for(let j=0;j<85;j++)assert(phi[j]===(j%2===0?(j%4===0?1n:-1n):0n),"cyclotomic identity");
const rows=B.intervals.slice().sort((a,b)=>BigInt(a.lo_num)<BigInt(b.lo_num)?-1:1);
let previous=86;for(let j=0;j<42;j++){const a=rows[j],ang=Math.min(a.angle_index,172-a.angle_index);assert(ang<previous,"cosine ordering");previous=ang;if(j)assert(BigInt(rows[j-1].lo_num)+1n<BigInt(a.lo_num),"disjoint intervals");}
assert(new Set(B.intervals.map(a=>Math.min(a.angle_index,172-a.angle_index))).size===42,"all primitive cosine roots");
}
function trialPrime(n){if(n<2)return false;if(n%2===0)return n===2;for(let d=3;d*d<=n;d+=2)if(n%d===0)return false;return true;}
function finalCertificate(C,B,S,extra){
const M=BigInt(S.modulus),bound=BigInt(B.uniform_coefficient_bound),q=BigInt(C.q);
assert(M>2n*bound,"strict CRT bound");
for(const row of S.rows)assert(row.prime%172===1&&trialPrime(row.prime),"trial primality");
const coeff=S.coefficients.map(s=>{let c=BigInt(s);return c>M/2n?c-M:c;});
assert(coeff[0]===1n&&coeff[1]===0n,"monic and trace zero");
for(const c of coeff)assert((c<0n?-c:c)<=bound,"integer coefficient bound");
assert(coeff.slice(1).every(c=>c%q===0n),"Eisenstein divisibility");
assert(coeff[43]%(q*q)!==0n,"Eisenstein constant exact valuation");
for(const row of extra){assert(trialPrime(row.prime),"extra prime");const P=BigInt(row.prime);assert(row.coefficients.every((v,j)=>BigInt(v)===(coeff[j]%P+P)%P),"unused prime reduction");}
return {schema:"R207-gaussian-trace-degree43-v1",coefficient_order:"descending",input:C,root_bound:B,crt:{modulus:S.modulus,rows:S.rows},polynomial:coeff.map(String),extra_reductions:extra,summary:{prime_count:S.rows.length,crt_bits:M.toString(2).length,required_bound_bits:(2n*bound).toString(2).length,maximum_coefficient_bits:Math.max(...coeff.map(c=>(c<0n?-c:c).toString(2).length)),eisenstein_at_input_q:true,norm_witness_found:false,canonical_residue_L_computed:false}};
}
function makeCertificate(C){
const B=rootBound(C);validateRootBound(C,B);
const S=runCRT(C,modular43.toString(),B.uniform_coefficient_bound,{next:1000000+(172-(1000000-1)%172)%172,rows:[],modulus:"1",coefficients:Array(44).fill("0")},10000);
const api=modular43(C);let p=3000000+(172-(3000000-1)%172)%172,extra=[];for(let j=0;j<3;p+=172){if(!api.prime(p))continue;extra.push({prime:p,coefficients:api.poly(p,31)});j++;}
return finalCertificate(C,B,S,extra);
}

const args=process.argv.slice(2),mode=args[0]==="--certificate"?"write":"check",target=mode==="write"?args[1]:(args[0]==="--check"?args[1]:args[0]);
if(!target)throw Error("usage: node verify_r207_gaussian_trace_degree43.js [--check|--certificate] FILE.json");
const started=Date.now(),made=makeCertificate(INPUT),encoded=JSON.stringify(made);
if(mode==="write")fs.writeFileSync(target,JSON.stringify(made)+"\n");
else {const old=JSON.parse(fs.readFileSync(target,"utf8"));assert(JSON.stringify(old)===encoded,"certificate differs");}
console.log(JSON.stringify({status:"PASS",...made.summary,certificate_sha256:crypto.createHash("sha256").update(fs.readFileSync(target)).digest("hex"),seconds:(Date.now()-started)/1000}));
