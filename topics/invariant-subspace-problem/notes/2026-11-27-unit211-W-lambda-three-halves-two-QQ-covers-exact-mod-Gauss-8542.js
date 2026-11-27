/* R150 W lambda=3/2: actual full modular Bezout for two already computed monic QQ covers.
No new resultant or QQ xgcd is executed. */
(function(){
const sha256Ascii=function sha256Ascii(s){
for(let i=0;i<s.length;i++)if(s.charCodeAt(i)>127)throw new Error("non-ASCII hash input");
const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
const n=Math.ceil((s.length+9)/64)*64,bytes=new Uint8Array(n);for(let i=0;i<s.length;i++)bytes[i]=s.charCodeAt(i);bytes[s.length]=128;let bits=BigInt(s.length)*8n;for(let j=0;j<8;j++){bytes[n-1-j]=Number(bits&255n);bits>>=8n;}
const rr=(x,k)=>(x>>>k)|(x<<(32-k));let h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
for(let off=0;off<n;off+=64){const w=new Uint32Array(64);for(let j=0;j<16;j++)w[j]=(bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3];for(let j=16;j<64;j++){let x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
let[a,b,c,d,e,f,g,z]=h;for(let j=0;j<64;j++){let t1=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0;let t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;[z,g,f,e,d,c,b,a]=[g,f,e,(d+t1)>>>0,c,b,a,(t1+t2)>>>0];}h=h.map((x,j)=>(x+[a,b,c,d,e,f,g,z][j])>>>0);}
return h.map(x=>x.toString(16).padStart(8,"0")).join("");
};
const INPUTS=[{"name":"N1","QQSHA256":"c62029f87e6028973a5b54c72814ccc411b525c69f364c8fd5c51be20b57473f","modSHA256":"0a4b4a1074411bc274d42cde9c89154c5e7418134acc4fdd8244afa782d28138","coefficients":[828,24,1005,842,188,225,351,261,335,141,318,572,236,266,529,854,232,569,166,329,277,53,234,115,522,894,414,48,840,103,638,605,32,268,766,896,925,820,268,89,803,415,867,384,419,220,829,1,453,389,655,793,650,748,729,899,564,695,283,477,862,390,717,245,207,291,990,929,722,647,453,153,975,576,710,745,602,261,768,371,137,343,64,309,920,925,295,253,754,233,540,554,978,749,498,885,8,249,296,821,922,154,165,823,323,123,895,351,185,345,92,613,420,802,168,205,635,415,532,92,720,134,548,520,734,314,807,374,866,346,470,214,64,213,678,8,809,365,994,676,377,929,771,337,177,691,280,943,124,138,364,498,776,308,731,346,459,869,29,20,396,15,288,970,548,279,894,660,526,954,686,580,981,959,666,231,897,167,434,898,609,140,744,862,184,309,124,535,342,661,244,655,741,350,699,707,576,799,84,375,977,656,990,172,649,500,906,871,389,991,129,561,515,6,588,337,764,740,992,379,661,827,714,220,956,405,817,220,118,342,940,525,131,424,561,228,473,164,349,994,472,510,57,603,717,345,1002,411,486,926,33,2,281,523,957,128,188,441,640,692,99,684,825,479,530,241,25,509,603,361,366,153,389,586,1004,705,975,353,960,561,885,784,111,326,996,257,344,643,877,881,837,664,753,481,898,751,810,560,883,928,657,101,578,368,737,117,441,246,433,960,513,844,530,536,193,570,352,116,823,124,602,532,525,118,915,582,777,971,116,580,824,925,389,602,65,940,101,902,753,602,431,681,735,141,659,356,469,87,922,601,671,416,696,90,910,245,560,229,746,910,893,531,976,383,405,404,50,296,735,812,790,396,1]},{"name":"NS","QQSHA256":"204f429d348a8c19a3c131c068e1e369325577f756b0dbdab221ad551dc84a4a","modSHA256":"347e3456ec46f3dafe1644128ad2f22bd06e57e21ee2b61d594d120501283785","coefficients":[956,256,820,391,416,971,751,17,249,767,592,770,965,186,219,243,625,427,544,188,859,525,656,293,785,140,133,177,986,141,487,843,198,159,507,528,100,543,418,263,477,795,626,255,819,200,753,894,668,336,456,574,191,268,784,797,594,923,412,39,673,638,914,478,628,921,560,735,388,251,217,927,258,593,413,556,680,967,330,191,471,88,43,552,727,546,420,669,595,891,843,436,803,994,387,638,640,891,395,212,92,740,42,948,472,699,741,536,413,750,257,884,777,396,263,991,112,430,796,207,411,384,255,951,29,55,587,414,691,528,746,324,552,806,454,330,448,71,261,666,208,278,160,894,396,209,567,95,189,44,541,48,474,606,430,327,321,453,965,652,846,935,629,799,898,544,595,63,869,139,976,66,969,500,2,47,103,366,941,784,35,928,782,181,994,409,375,208,513,23,668,944,941,706,787,899,346,783,129,609,640,245,884,204,31,288,81,261,630,768,633,636,40,820,522,666,117,885,987,348,983,828,907,844,422,3,78,529,210,941,395,855,327,185,15,1007,25,907,143,862,727,98,197,70,156,269,48,429,395,897,300,647,629,718,634,236,192,353,305,992,715,879,886,310,897,130,702,77,589,748,11,634,640,987,622,710,778,1005,519,574,240,786,379,805,417,894,631,277,1005,272,505,1005,764,241,581,827,88,443,259,207,543,53,43,308,153,895,431,908,17,425,386,812,940,130,854,680,366,35,15,741,930,623,407,783,487,945,483,934,835,989,800,105,426,340,550,675,842,937,915,480,265,83,677,914,899,265,305,997,423,226,59,607,164,344,497,743,896,613,779,527,365,445,375,983,762,672,706,298,525,228,157,941,751,276,946,684,814,244,80,538,348,191,614,379,14,509,231,771,517,768,76,226,958,817,822,776,31,302,78,88,104,850,512,1]}];

const began=Date.now(),p=1009;
function assert(v,m){if(!v)throw Error(m||'exact assertion');}
for(let q=2;q*q<=p;q++)assert(p%q!==0,'prime');
const trim=a=>{while(a.length&&a[a.length-1]===0)a.pop();return a;};
const norm=x=>(x%p+p)%p;
const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>norm((a[i]||0)+(b[i]||0))));
const neg=a=>a.map(x=>norm(-x));
const sub=(a,b)=>add(a,neg(b));
function mul(a,b){
 if(!a.length||!b.length)return [];
 const c=Array(a.length+b.length-1).fill(0);
 for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=norm(c[i+j]+a[i]*b[j]);
 return trim(c);
}
function power(a,n){let v=1;while(n){if(n%2)v=norm(v*a);a=norm(a*a);n=Math.floor(n/2);}return v;}
const scale=(a,c)=>trim(a.map(x=>norm(x*c)));
function div(a,b){
 assert(b.length,'division by zero');
 let r=a.slice(),q=Array(Math.max(0,a.length-b.length+1)).fill(0),iv=power(b[b.length-1],p-2);
 assert(norm(iv*b[b.length-1])===1,'scalar inverse');
 while(r.length>=b.length){
  const j=r.length-b.length,c=norm(r[r.length-1]*iv);q[j]=c;
  for(let i=0;i<b.length;i++)r[j+i]=norm(r[j+i]-c*b[i]);
  trim(r);
 }
 return [trim(q),r];
}
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const A=INPUTS[0].coefficients,B=INPUTS[1].coefficients;
assert(A.length===373&&B.length===404&&A[A.length-1]===1&&B[B.length-1]===1,'both monic full degrees');
for(const x of [...A,...B])assert(Number.isInteger(x)&&0<=x&&x<p,'canonical residue');
for(const i of INPUTS)assert(sha256Ascii(JSON.stringify(i.coefficients))===i.modSHA256,'frozen input exact hash');
let r0=A,r1=B,s0=[1],s1=[],t0=[],t1=[1],steps=0;
while(r1.length){
 const [q,r]=div(r0,r1);
 [r0,r1]=[r1,r];[s0,s1]=[s1,sub(s0,mul(q,s1))];[t0,t1]=[t1,sub(q.length?mul(q,t1):[],t0)].map((x,i)=>i===1?neg(x):x);
 // The last assignment equals (t1, t0-q*t1), with the old arrays read first.
 steps++;
}
const iv=power(r0[r0.length-1],p-2),g=scale(r0,iv),s=scale(s0,iv),t=scale(t0,iv);
assert(same(g,[1]),'unit gcd');
const left=mul(s,A),right=mul(t,B),returned=add(left,right);
assert(same(returned,[1]),'both complete Bezout products');
const certificate={prime:p,A,B,s,t,left,right,returned};
const encoded=JSON.stringify(certificate);
return {
 schema:'isp-exact-univariate-local-Gauss-Bezout-v1',
 prime:p,QQInputRun:46023620737,QQInputJob:140589275823,
 QQInputSourceSHA256:'a267a41db72fd2359ec215fd65c95d8f4d495f9cc2085f0e891c442817699a3d',
 inputs:INPUTS.map(i=>({name:i.name,QQDegree:i.coefficients.length-1,QQMonicProfileSHA256:i.QQSHA256,modSHA256:i.modSHA256})),
 gcd:[1],bezoutDegrees:[s.length-1,t.length-1],bezoutLeft:s,bezoutRight:t,
 fullBothPolynomialProductsActuallyVerified:true,actualReturn:returned,
 allIntegerOperationsBelowTwoMillion:true,euclideanSteps:steps,
 certificate:{bytes:encoded.length,sha256:sha256Ascii(encoded)},
 elapsedMilliseconds:Date.now()-began,
 inferenceScope:'With the already executed monic QQ Z_(1009) inputs, Gauss excludes their common characteristic-zero root, hence the entire current W lambda=3/2 fiber.'
};

})()
