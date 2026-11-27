// Six-site original S2: exact physical one-parameter certificate.
// 2026-11-28 Asia/Taipei; session Astra-ISP-8542378f-20261127.
// This is a saved-polynomial continuation, not a replay of the 15x15 inverse.
// Optional input is the ASCII raw JSON from run 46052984288 / job 140688624777.
export const certificate = (() => {

const trim=a=>{while(a.length>1&&a[a.length-1]===0n)a.pop();return a;};
const P=a=>trim(a.map(BigInt));
const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const scale=(a,c)=>trim(a.map(x=>x*c));
const mul=(a,b)=>{const r=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]+=a[i]*b[j];return trim(r);};
const pow=(a,n)=>{let r=[1n];while(n--)r=mul(r,a);return r;};
const same=(a,b)=>{a=trim(a.slice());b=trim(b.slice());return a.length===b.length&&a.every((x,i)=>x===b[i]);};
const assert=(b,m)=>{if(!b)throw Error(m);};
const one=[1n],t=[0n,1n],plus=a=>P([a,1]);
const rf=(n,d=one)=>({n,d});
const rm=(a,b)=>rf(mul(a.n,b.n),mul(a.d,b.d));
const ra=(a,b)=>rf(add(mul(a.n,b.d),mul(b.n,a.d)),mul(a.d,b.d));
const req=(a,b)=>same(mul(a.n,b.d),mul(b.n,a.d));
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const x=a%b;a=b;b=x;}return a;};
const ev=(p,x)=>{let y=0n;for(let i=p.length-1;i>=0;i--)y=y*x+p[i];return y;};
const reduced=(a,b)=>{const g=gcd(a,b);return [String(a/g),String(b/g)];};
function mm(a,b){return a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>add(s,mul(x,b[k][j])),[0n])));}
function matEq(a,b){return a.every((r,i)=>r.every((p,j)=>same(p,b[i][j])));}
function certificate(raw){
 const start=Date.now(),three=plus(3),tp=plus(1);
 // Complete physical two-copy block, not a compressed inverse.
 const FU=[[P([3]),P([3])],[t,plus(4)]];
 const adj=[[plus(4),P([-3])],[scale(t,-1n),P([3])]];
 const I12=[[P([12]),P([0])],[P([0]),P([12])]];
 assert(matEq(mm(FU,adj),I12)&&matEq(mm(adj,FU),I12),"full FU inverse");
 const metric=[[t,P([0])],[P([0]),P([3])]];
 const mF=mm(metric,FU);assert(same(mF[0][1],mF[1][0]),"physical adjoint");
 const v=[[P([3])],[scale(t,-1n)]],Cv=scale(mul(t,plus(-1)),3n);
 const vn=scale(mul(t,three),3n);
 const av=mm(adj,v);
 const avInner=add(mul(mul(v[0][0],t),av[0][0]),scale(mul(v[1][0],av[1][0]),3n));
 const Gu=rf(tp,three),Cu=rf(three,tp),L2=rf(one,scale(tp,3n)),E=rf(P([1,3]));
 assert(req(rf(avInner,scale(vn,12n)),Gu),"actual Gu compression");
 const BB=rf(mul(Cv,Cv),vn),X=rm(rm(L2,E),L2);
 const source=ra(rm(Cu,L2),X);
 const K=rm(rm(BB,Gu),rm(rf(one,P([4])),rm(source,source)));
 const num=mul(t,mul(pow(plus(-1),2),pow(P([5,3]),2)));
 const den=scale(mul(pow(three,2),pow(tp,3)),27n);
 assert(req(K,rf(num,den)),"same two-term source with both cross terms");
 const thirdGap=add(den,scale(num,-3n));
 const fullGap=add(add(den,scale(num,-2n)),scale(pow(tp,4),-162n));
 assert(same(thirdGap,P([243,816,1302,888,207])),"one-third coefficient identity");
 assert(same(fullGap,P([81,193,310,214,57,9])),"full S2 one-half identity");
 assert(thirdGap.every(x=>x>0n)&&fullGap.every(x=>x>0n),"positive coefficients");
 const a=36n,kn=ev(num,a),kd=ev(den,a),traceN=4n*kn*kn,traceD=kd*kd;
 assert(4n*traceN>traceD,"actual trace-square quarter counterexample");
 let saved=null;
 if(raw!==undefined){
  const startTable=raw.indexOf('"complete_elementary_coefficients"');
  assert(startTable>=0,"saved table exists");
  const es=[a+5n,5n*a+10n,10n*a+10n,10n*a+5n,5n*a+1n,a];
  const powers=es.map(x=>{const r=[1n];for(let k=1;k<=144;k++)r.push(r[k-1]*x);return r;});
  const re=/\{"powers":\[([0-9,]+)\],"coefficients":\[(-?\d+),(-?\d+),(-?\d+)\]\}/g;
  const tail=raw.slice(startTable);let m,count=0,nn=0n,dd=0n,content=0n,nTerms=0;
  while((m=re.exec(tail))!==null){
   const p=m[1].split(",").map(Number),n=BigInt(m[2]),d=BigInt(m[3]),gap=BigInt(m[4]);
   assert(gap===d-4n*n,"saved same scalar gap");
   let mon=1n;for(let i=0;i<6;i++)mon*=powers[i][p[i]];
   nn+=n*mon;dd+=d*mon;count++;
   if(n){content=gcd(content,n);nTerms++;}
  }
  assert(count===119401&&nTerms===119367,"complete saved scalar support");
  assert(content===11555266180939776n,"original numerical content");
  assert(nn*traceD===dd*traceN,"same saved scalar at t=36");
  assert(dd>0n&&dd-4n*nn<0n,"saved positive denominator and negative gap");
  saved={records:count,numerator_terms:nTerms,numerical_content:String(content),at_t:"36",reduced_scalar:reduced(nn,dd),gap_sign:-1,exact_family_match:true};
 }
 return {schema:"isp-six-site-s2-one-parameter-exact-v1",elapsed_ms:Date.now()-start,
 physical_blocks:{FU_inverse:true,physical_metric:true,actual_compressed_inverse:true,same_source_both_cross_terms:true},
 kappa:{numerator:num.map(String),denominator:den.map(String),multiplicity:4,remaining_eigenvalue:"0"},
 one_third_gap:thirdGap.map(String),full_S2_half_gap:fullGap.map(String),
 counterexample:{t:"36",b:["6","1","1","1","1","1"],kappa:reduced(kn,kd),trace_square:reduced(traceN,traceD),strictly_greater_than_one_quarter:true},
 saved_scalar:saved,
 scope:"All t>0: the same complete S2 operator is strictly below I/2; the full cost K is strictly below I/3. Both constants are sharp on this family. The uniform six-site trace-square <1/4 gate is false; this is not a counterexample to general S2."};
}
return certificate;

})();
export default certificate;
