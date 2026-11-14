// Exact R229 certificate. Run with Node.js; no packages or files are read.
// All coefficients below are fixed original theta inputs, not fitted data.

const Z=()=>[0n,0n,0n,0n], O=()=>[1n,0n,0n,0n];
const zzero=x=>x.every(t=>t===0n);
const zeq=(x,y)=>x.every((t,j)=>t===y[j]);
const zadd=(x,y)=>x.map((t,j)=>t+y[j]);
const zneg=x=>x.map(t=>-t);
const zscale=(x,n)=>x.map(t=>t*BigInt(n));
const zmul=(x,y)=>{
 const cm=(a,b,c,d)=>[a*c-b*d,a*d+b*c];
 const a=cm(x[0],x[1],y[0],y[1]),b=cm(x[2],x[3],y[2],y[3]);
 const c=cm(x[0],x[1],y[2],y[3]),d=cm(x[2],x[3],y[0],y[1]);
 return[a[0]+2n*b[0],a[1]+2n*b[1],c[0]+d[0],c[1]+d[1]];
};
const zpow=(x,n)=>{let r=O();for(let j=0;j<n;j++)r=zmul(r,x);return r;};
const zi=k=>[[1n,0n,0n,0n],[0n,1n,0n,0n],[-1n,0n,0n,0n],[0n,-1n,0n,0n]][((k%4)+4)%4];
const zs2=k=>k%2?[0n,0n,2n**BigInt((k-1)/2),0n]:[2n**BigInt(k/2),0n,0n,0n];
const gcd=(a,b)=>{if(a<0n)a=-a;if(b<0n)b=-b;while(b){[a,b]=[b,a%b];}return a;};
const lcm=(a,b)=>a/gcd(a,b)*b;
const zser=x=>x.map(String);
const zdes=x=>x.map(BigInt);
const binom=(n,k)=>{let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r;};
const matid=()=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>j===k?O():Z()));
const mmul=(a,b)=>a.map(row=>b[0].map((_,k)=>row.reduce((s,x,j)=>zadd(s,zmul(x,b[j][k])),Z())));
const mscale=(a,n)=>a.map(row=>row.map(x=>zscale(x,n)));
const mnormal=(a,d)=>{let g=d;for(const row of a)for(const x of row)for(const t of x)g=gcd(g,t);return{a:a.map(row=>row.map(x=>x.map(t=>t/g))),d:d/g};};
const mrmul=(a,b)=>mnormal(mmul(a.a,b.a),a.d*b.d);
const mrpow=(a,n)=>{let r={a:matid(),d:1n};for(let j=0;j<n;j++)r=mrmul(r,a);return r;};
const zint=n=>[BigInt(n),0n,0n,0n];
const M={a:[
 [0,2,2,0],
 [1,0,0,1],
 [1,0,0,-1],
 [0,-2,2,0]
].map(r=>r.map(zint)),d:2n};
const N={a:[
 [Z(),zint(2),zint(-2),Z()],
 [O(),Z(),Z(),zneg(zi(1))],
 [zint(-1),Z(),Z(),zneg(zi(1))],
 [Z(),zscale(zi(1),-2),zscale(zi(1),-2),Z()]
],d:2n};
const polyadd=(p,key,c)=>{if(zzero(c))return;const t=zadd(p.get(key)||Z(),c);if(zzero(t))p.delete(key);else p.set(key,t);};
const lpow=(row,n)=>{
 let p=new Map([["0,0,0,0",O()]]);
 for(let k=0;k<n;k++){
  const q=new Map();
  for(const[key,c]of p){const es=key.split(",").map(Number);for(let j=0;j<4;j++)if(!zzero(row[j])){const fs=[...es];fs[j]++;polyadd(q,fs.join(","),zmul(c,row[j]));}}
  p=q;
 }
 return p;
};
const polymul=(p,q)=>{
 const r=new Map();for(const[k,c]of p){const a=k.split(",").map(Number);for(const[l,d]of q){const b=l.split(",").map(Number);polyadd(r,a.map((t,j)=>t+b[j]).join(","),zmul(c,d));}}return r;
};
const reduce=(p)=>{
 const r=new Map();for(const[key,c]of p){
  const[T,F,G,H]=key.split(",").map(Number),u=Math.floor(T/2),v=Math.floor(H/2);
  const cc=zscale(zmul(c,zs2(u+v)),2n**BigInt(v));
  for(let j=0;j<=u;j++)polyadd(r,[T%2,F+v+2*j,G+v+2*(u-j),H%2].join(","),zscale(cc,binom(u,j)));
 }return r;
};
const pscale=(p,c)=>new Map([...p].map(([k,d])=>[k,zmul(c,d)]).filter(([,d])=>!zzero(d)));
const pplus=(p,q)=>{const r=new Map(p);for(const[k,c]of q)polyadd(r,k,c);return r;};
const pzero=p=>p.size===0;
const peq=(p,q)=>pzero(pplus(p,pscale(q,zint(-1))));
const pserialize=p=>[...p].sort(([a],[b])=>a.localeCompare(b)).map(([k,c])=>[k,zser(c)]);
const pdeserialize=p=>new Map(p.map(([k,c])=>[k,zdes(c)]));
const transform=(src,A)=>{
 const out=new Map(),cache={};
 for(const[es,c]of src){
  let p=new Map([["0,0,0,0",O()]]);
  for(let j=0;j<4;j++)if(es[j]){const key=j+","+es[j];cache[key]??=lpow(A[j],es[j]);p=polymul(p,cache[key]);}
  p=reduce(p);
  for(const[k,d]of p)polyadd(out,k,zmul(c,d));
 }return out;
};
const getmaps=()=>{
 const maps=[];
 for(let k=0;k<4;k++)for(let j=0;j<4;j++){
  const m=mrmul(mrpow(N,j),mrpow(M,k));
  if(4n%m.d)throw Error("matrix denom "+m.d);
  maps.push({k,j,a:mscale(m.a,4n/m.d)});
 }return maps;
};
const project=(src,v)=>{
 const out=new Map();let terms=0;
 const norm=v.reduce((s,x)=>s+x*x,0);
 const maps=getmaps();
 for(const{k,j,a}of maps){
  let coeff=Z();
  for(let x=0;x<4;x++)coeff=zadd(coeff,zscale(zi(-k*x),v[x]*v[(x-j+4)%4]));
  if((k+j)%2)coeff=zneg(coeff);
  if(zzero(coeff))continue;
  const p=transform(src,a); terms++;
  for(const[key,c]of p)polyadd(out,key,zmul(coeff,c));
 }
 return{p:out,den:4n*BigInt(norm)*4n**17n,terms};
};

const frac=s=>{const[a,b="1"]=s.split("/");return[BigInt(a),BigInt(b)];};
const rat=(a,b)=>{const g=gcd(a,b);a/=g;b/=g;if(b<0n){a=-a;b=-b;}return b===1n?String(a):a+"/"+b;};
const make=ts=>{let D=1n;for(const t of ts)D=lcm(D,frac(t.c)[1]);return{src:ts.map(t=>[t.e,zscale(t.f||O(),frac(t.c)[0]*(D/frac(t.c)[1]))]),D};};
const PB=["-2261/81920","953/102400","-2887/192000","1501/22400","-49/600","101/2310","-4/455"];
const PA=["-17/1155","-53/3850","16/4125","-128/525"];
const b=[0,5,-18,140,-400,496,-288,64],bt=[-1,11,-14,20,0,-112,160,-64];
const phiSource=pp=>make(pp.map((c,k)=>({e:[16-2*k,0,2*k+1,0],c,f:zs2(k)})));
const ss={
 tauB:phiSource(bt.map(c=>c+"/20")),
 B:make(b.map((c,k)=>({e:[16-2*k,1,2*k,0],c:c+"/20",f:zs2(k)}))),
 A:make(["1","48/5","-256/5","4096/5"].map((c,j)=>{const k=j+1,[n,d]=frac(c);return{e:[17-4*k,0,0,4*k],c:n+"/"+(d*16n**BigInt(k))};})),
 CB:phiSource(PB),
 CA:make(PA.map((c,k)=>{const[n,d]=frac(c);return{e:[15-4*k,0,0,4*k+2],c:n+"/"+(d*16n**BigInt(k))};}))
};
const original=s=>reduce(new Map(s.src.map(([e,c])=>[e.join(","),c])));
const must=(b,label)=>{if(!b)throw Error("FAIL: "+label);};
const checks={};
const put=(label,b)=>{must(b,label);checks[label]=true;};
const m4=mrpow(M,4),n4=mrpow(N,4),mn=mrmul(N,M),nm=mrmul(M,N);
put("M4_identity",m4.d===1n&&m4.a.every((r,j)=>r.every((x,k)=>zeq(x,j===k?O():Z()))));
put("N4_identity",n4.d===1n&&n4.a.every((r,j)=>r.every((x,k)=>zeq(x,j===k?O():Z()))));
put("MN_equals_iNM",mn.a.every((r,j)=>r.every((x,k)=>zeq(zscale(x,nm.d),zmul(zi(1),zscale(nm.a[j][k],mn.d))))));
for(const[name,v]of [["tauB",[1,-1,-1,-1]],["B",[1,1,-1,1]],["A",[1,0,1,0]],["CA",[1,0,1,0]]]){
 const P=project(ss[name].src,v);
 put("actual_"+name+"_pure_dyadic",peq(P.p,pscale(original(ss[name]),zint(P.den))));
}
const minus=project(ss.CB.src,[1,-1,-1,-1]),plus=project(ss.CB.src,[1,1,-1,1]);
put("CB_two_blocks_sum_exact",peq(pplus(minus.p,plus.p),pscale(original(ss.CB),zint(minus.den))));
put("CB_other_two_blocks_zero",project(ss.CB.src,[1,0,1,0]).p.size===0&&project(ss.CB.src,[0,1,0,-1]).p.size===0);
put("CB_both_blocks_nonzero",minus.p.size>0&&plus.p.size>0);
const polynomial=proj=>{
 const den=proj.den*ss.CB.D*16n,nums=Array(9).fill(0n);
 for(const[key,c]of proj.p){
  const[T,F,G,H]=key.split(",").map(Number);
  must(!T&&!H&&F%2===0&&G%2===1&&c.slice(1).every(x=>x===0n),"projected polynomial shape");
  const j=F/2,base=(G-1)/2;
  for(let k=0;k<=j;k++)nums[base+k]+=c[0]*binom(j,k)*(k%2?-1n:1n);
 }
 return nums.map(x=>rat(x,den));
};
const Pminus=polynomial(minus),Pplus=polynomial(plus);
const expectedMinus=["-2261/163840","18649/6758400","-24157/4224000","-692257/1478400","39049/147840","7016189/1848000","-13951679/1716000","298820917/48048000","-80295779/48048000"];
const expectedPlus=["-2261/163840","44249/6758400","-13119/1408000","791323/1478400","-255613/739200","-6935389/1848000","97556153/12012000","-298820917/48048000","80295779/48048000"];
put("Pminus_all_exact_coefficients",Pminus.every((x,k)=>x===expectedMinus[k]));
put("Pplus_all_exact_coefficients",Pplus.every((x,k)=>x===expectedPlus[k]));
for(const[label,p,proj]of [["minus",Pminus,minus],["plus",Pplus,plus]]){
 const s=phiSource(p),lhs=pscale(original(s),zint(proj.den*ss.CB.D)),rhs=pscale(proj.p,zint(s.D));
 put("converted_"+label+"_identity",peq(lhs,rhs));
}
const m2=mrpow(M,2),m2B=transform(ss.B.src,mscale(m2.a,4n/m2.d));
put("M2_B_is_actual_tauB",peq(pscale(m2B,zint(ss.tauB.D)),pscale(original(ss.tauB),zint(ss.B.D*4n**17n))));
const report={
 status:"PASS",
 arithmetic:"exact BigInt in Z[i,sqrt(2)], degree-17 quotient of two quadrics",
 target_prime_scan:false,
 checks,
 variable:"t=4q",
 P_B:PB,
 P_minus:Pminus,
 P_plus:Pplus,
 first_G_constants:{minus:"-2261/81920",plus:"-2261/81920",total:"-2261/40960"},
 tame_i_minus_exponents_mod16:[2,6,10,14],
 tame_i_plus_exponents_mod16:[0,4,8,12],
 note:"Character labels use the actual finite theta decomposition; no central nonvanishing is asserted."
};
console.log(JSON.stringify(report,null,2));
