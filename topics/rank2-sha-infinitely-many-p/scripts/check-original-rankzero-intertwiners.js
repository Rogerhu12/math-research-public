// Exact R231 four-torsion certificate; no packages, network or files are used.

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

const intertwine=(src,w,v)=>{
 const out=new Map(),norm=v.reduce((s,x)=>s+x*x,0);let terms=0;
 for(const{k,j,a}of getmaps()){
  let coeff=Z();for(let x=0;x<4;x++)coeff=zadd(coeff,zscale(zi(-k*x),w[x]*v[(x-j+4)%4]));
  if((k+j)%2)coeff=zneg(coeff);if(zzero(coeff))continue;
  const p=transform(src,a);terms++;for(const[key,c]of p)polyadd(out,key,zmul(coeff,c));
 }
 return{p:out,den:4n*BigInt(norm)*4n**17n,terms};
};
const frac=s=>{const[a,b="1"]=s.split("/");return[BigInt(a),BigInt(b)];};
const make=ts=>{let D=1n;for(const t of ts)D=lcm(D,frac(t.c)[1]);return{src:ts.map(t=>[t.e,zscale(t.f||O(),frac(t.c)[0]*(D/frac(t.c)[1]))]),D};};
const original=s=>reduce(new Map(s.src.map(([e,c])=>[e.join(","),c])));
const PB=["-2261/81920","953/102400","-2887/192000","1501/22400","-49/600","101/2310","-4/455"];
const b=[0,5,-18,140,-400,496,-288,64];
const Q68=[1,20,0,-176,480,-1344,2048,-1280,256];
const Q289=[1,0,-18,16,1],Q4913=[1,-7,21,-5,-2];
const Q19652=[1,-76,608,-1456,3296,-4928,3584,-1280,256];
const thetaOld=p=>make(p.map((c,j)=>({e:[17-4*j,0,0,4*j],c:String(c)})));
const thetaNew=p=>make(p.map((c,j)=>({e:[16-2*j,1,2*j,0],c:String(c),f:zs2(j)})));
const A=make(["1","48/5","-256/5","4096/5"].map((c,j)=>{const k=j+1,[n,d]=frac(c);return{e:[17-4*k,0,0,4*k],c:n+"/"+(d*16n**BigInt(k))};}));
const kB=thetaNew(b.map(n=>n+"/20")),kS68=thetaNew(Q68),S289=thetaOld(Q289),S4913=thetaOld(Q4913),kS19652=thetaNew(Q19652);
const kCB=make(PB.map((c,j)=>({e:[16-2*j,0,2*j+1,0],c,f:zs2(j)})));
const Rcoeff=["19509103/28114944000","10318337/702873600","777767/27525120","721667/86016000","55879/275251200"];
const Rsource=thetaOld(Rcoeff);
const v0=[1,0,1,0],vp=[1,1,-1,1],vm=[1,-1,-1,-1],checks={};
const opcheck=(name,input,w,v,target,num,den=1n)=>{
 const P=intertwine(input.src,w,v);
 const lhs=pscale(P.p,zint(BigInt(den)*target.D));
 const rhs=pscale(original(target),zint(BigInt(num)*P.den*input.D));
 if(!peq(lhs,rhs))throw Error("FAIL "+name);checks[name]=true;
};
opcheck("Qplus0_A_equals_minus_kappa_S68_over80",A,vp,v0,kS68,-1n,80n);
opcheck("Q0plus_kappa_B_equals_minus_S289_over320",kB,v0,vp,S289,-1n,320n);
opcheck("reverse_Q0plus_kappa_S68_equals_minus80A",kS68,v0,vp,A,-80n);
opcheck("reverse_Qplus0_S289_equals_minus320kappaB",S289,vp,v0,kB,-320n);
opcheck("Qplus0_S4913_equals_minus_kappa_S19652",S4913,vp,v0,kS19652,-1n);
opcheck("Q0minus_kappa_CB_equals_exact_R",kCB,v0,vm,Rsource,1n);
const report={
 status:"PASS",arithmetic:"exact BigInt in Z[i,sqrt(2)]",target_prime_scan:false,
 checks,Q68:Q68.map(String),Q289:Q289.map(String),Q4913:Q4913.map(String),Q19652:Q19652.map(String),
 constants:{u1:"-kappa/80",u2:"-kappa^-1/320",u1_times_u2:"1/25600"},
 R_for_kappa_Q0minus_CB:Rcoeff,
 note:"Q4913's actual lambda^3 identity is proved independently by the CM norm-five trace certificate."
};
console.log(JSON.stringify(report,null,2));
