// NEW fixed original Phi main point, exact rational polynomial identity.
// (u,Q,ell,lambda)=(3/4,5/4,1/2,1/2), D!=0.
// Complete original means R/W/O and N1; direct Macaulay QQ rows.
// No existing resultant or field-inverse gate is replayed.
// 2026-11-28 Asia/Taipei. Runs in fresh JavaScript with BigInt only.
const started=Date.now();
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function rat(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(!n)return {n:0n,d:1n};if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
const Z=rat(0),I=rat(1);
function ra(a,b){return rat(a.n*b.d+b.n*a.d,a.d*b.d);}
function rn(a){return {n:-a.n,d:a.d};}
function rs(a,b){return ra(a,rn(b));}
function rm(a,b){return rat(a.n*b.n,a.d*b.d);}
function rd(a,b){return rat(a.n*b.d,a.d*b.n);}
function eq(a,b){return a.n===b.n&&a.d===b.d;}
function str(a){return a.d===1n?String(a.n):String(a.n)+"/"+String(a.d);}
function P(c=Z){return c.n?new Map([[0,c]]):new Map();}
function pa(a,b){const o=new Map(a);for(const [k,c]of b){const v=ra(o.get(k)||Z,c);if(v.n)o.set(k,v);else o.delete(k);}return o;}
function pn(a){return new Map([...a].map(([k,c])=>[k,rn(c)]));}
function ps(a,b){return pa(a,pn(b));}
function pm(a,b){const o=new Map();for(const[k,c]of a)for(const[j,d]of b){const t=Math.floor(k/16)+Math.floor(j/16),z=k%16+j%16;if(z>=16||t>=16)throw Error("degree encoding overflow");const e=16*t+z,v=ra(o.get(e)||Z,rm(c,d));if(v.n)o.set(e,v);else o.delete(e);}return o;}
function pp(a,n){if(n<0||!Number.isSafeInteger(n))throw Error("bad power");let o=P(I);while(n){if(n&1)o=pm(o,a);n=Math.floor(n/2);if(n)a=pm(a,a);}return o;}
function pd(a,b){if(b.size!==1||!b.has(0))throw Error("only constant original inverse");const v=b.get(0);return new Map([...a].map(([k,c])=>[k,rd(c,v)]));}
function peq(a,b){return ps(a,b).size===0;}
function degree(a){return Math.max(-1,...[...a.keys()].map(k=>Math.floor(k/16)+k%16));}
function pdata(a){return [...a].sort((x,y)=>x[0]-y[0]).map(([k,c])=>[Math.floor(k/16),k%16,str(c)]);}
const env={Tr:new Map([[16,I]]),z:new Map([[1,I]])};
function parse(s){
 const ts=s.match(/\d+|\*\*|[A-Za-z_][A-Za-z_0-9]*|[-+*/()]/g)||[];
 if(ts.join("")!==s.replace(/\s/g,""))throw Error("unparsed token "+s);
 let pos=0;
 function atom(){const q=ts[pos++];if(q==="("){const a=add();if(ts[pos++]!==")")throw Error("parenthesis");return a;}if(/^\d+$/.test(q||""))return P(rat(q));if(!env[q])throw Error("unknown "+q);return env[q];}
 function power(){let a=atom();if(ts[pos]==="**"){pos++;const e=unary();if(e.size!==1||!e.has(0)||e.get(0).d!==1n)throw Error("integer exponent");a=pp(a,Number(e.get(0).n));}return a;}
 function unary(){if(ts[pos]==="+"){pos++;return unary();}if(ts[pos]==="-"){pos++;return pn(unary());}return power();}
 function mul(){let a=unary();while(ts[pos]==="*"||ts[pos]==="/"){const op=ts[pos++],b=unary();a=op==="*"?pm(a,b):pd(a,b);}return a;}
 function add(){let a=mul();while(ts[pos]==="+"||ts[pos]==="-"){const op=ts[pos++],b=mul();a=op==="+"?pa(a,b):ps(a,b);}return a;}
 const ans=add();if(pos!==ts.length)throw Error("extra tokens");return ans;
}
const defs=[
["u","3/4"],["Q","5/4"],["ell","1/2"],["lam","1/2"],
["delta","1-Q"],["m","u-ell"],["V2","2*u-ell*Q"],["T0","V2-2*u*u"],
["J","2*u*(1-u)+ell*Q"],["P02","(2-3*u)*V2-Q*u+2*u**3"],["Pf","T0*(J-Q)"],
["M","ell*V2-u*u"],["bc","M/(4*delta)"],["A2","2*lam*lam-2*lam+1"],
["G","lam*P02+(u-1)*T0"],["Pc","Q*P02*(ell+Tr)-G*T0"],["ff","-Pc/Pf"],
["aa","1-ell"],["vn","J*ff-G+bc*z"],["wstar","T0+4*u*ff"],["nn","Q*wstar-2*vn"],["ww","lam-1-Tr"],
["ii","(vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q-4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn)"],
["Rbar","ii+(m/(2*delta))*z*nn"],
["W4","8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn+4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z+32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn"],
["s0","2*ell*vn-(m/delta)*nn"],["d0","-2*m*vn+ell*nn"],
["Obar","32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0+32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff+4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z-16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn"],
["al","ell*(1-u)-m"],["ber","ell*delta-m*(1-u)"],["av","(2*u-1)*ell+3*m"],["bur","(2*u-1)*m+3*ell*delta"],
["Nstar","al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn+8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar+16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff-32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff+16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*z*vn-2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aa*Q)-8*u*bc*bc*delta*z*z"],
["N1","Nstar-16*bc*delta*Q*Q*lam*P02*ww"],["D","ell*A2-Tr*Tr"]
];
for(const [k,s]of defs)env[k]=parse(s);
if(!peq(parse("Pf*ff+Pc"),P()))throw Error("original P1");
if(!peq(parse("T0+4*u-4+Q"),P()))throw Error("original Phi");
if(!peq(env.D,parse("1/4-Tr*Tr")))throw Error("physical D");
if(!peq(env.ff,parse("7/2+25*Tr/4")))throw Error("actual f");
const names=["Rbar","W4","Obar","N1"],original=names.map(k=>env[k]);
if(original.some(p=>degree(p)!==2))throw Error("original quadratic degree");
function primitive(p){let den=1n;for(const c of p.values())den=den/gcd(den,c.d)*c.d;let con=0n;for(const c of p.values())con=gcd(con,c.n*(den/c.d));if(!con)throw Error("zero original");const scale=rat(den,con),out=pm(P(scale),p);if([...out.values()].some(c=>c.d!==1n)||!peq(out,pm(P(scale),p)))throw Error("primitive return");return {p:out,scale};}
const prim=original.map(primitive),maxDegree=6;
const monomials=[];for(let d=0;d<=maxDegree;d++)for(let t=0;t<=d;t++)monomials.push(16*t+d-t);
const rows=[],sources=[];
for(let i=0;i<prim.length;i++)for(let d=0;d<=maxDegree-2;d++)for(let t=0;t<=d;t++){
 const m=new Map([[16*t+d-t,I]]),p=pm(m,prim[i].p);
 rows.push(monomials.map(k=>p.get(k)||Z));sources.push({original:i,m});
}
const basis=[];
function tagScaled(a,s){return new Map([...a].map(([k,c])=>[k,rm(c,s)]).filter(([k,c])=>c.n));}
function tagSub(a,b,s){const o=new Map(a);for(const [k,c]of b){const q=rs(o.get(k)||Z,rm(s,c));if(q.n)o.set(k,q);else o.delete(k);}return o;}
for(let i=0;i<rows.length;i++){
 let row=rows[i].slice(),tag=new Map([[i,I]]);
 for(const b of basis){const c=row[b.pivot];if(!c.n)continue;row=row.map((a,j)=>rs(a,rm(c,b.row[j])));tag=tagSub(tag,b.tag,c);}
 const pivot=row.findIndex(c=>c.n);if(pivot<0)continue;
 const inv=rd(I,row[pivot]);row=row.map(c=>rm(c,inv));tag=tagScaled(tag,inv);
 for(let j=0;j<monomials.length;j++){let actual=Z;for(const[k,c]of tag)actual=ra(actual,rm(c,rows[k][j]));if(!eq(actual,row[j]))throw Error("full original row product");}
 basis.push({pivot,row,tag});basis.sort((a,b)=>a.pivot-b.pivot);
}
const attempts=[];let found=null;
for(let power=0;power<=3;power++){
 const target=pp(env.D,power);let row=monomials.map(k=>target.get(k)||Z),tag=new Map();
 for(const b of basis){const c=row[b.pivot];if(!c.n)continue;row=row.map((a,j)=>rs(a,rm(c,b.row[j])));tag=tagSub(tag,b.tag,rn(c));}
 const zero=row.every(c=>!c.n);attempts.push({power,returned:zero});
 if(!zero)continue;
 const mult=names.map(()=>P());
 for(const [i,c]of tag){const src=sources[i];mult[src.original]=pa(mult[src.original],pm(P(c),src.m));}
 let total=P();for(let i=0;i<names.length;i++)total=pa(total,pm(mult[i],prim[i].p));
 if(!peq(total,target))throw Error("complete final original ideal identity");
 found={power,target:pdata(target),primitiveOriginalMultipliers:mult.map(pdata)};break;
}
const result={schema:"isp-Phi-main-minus-quarter-half-exact-original-identity-v1",
date:"2026-11-28 Asia/Taipei",originalParameters:{u:"3/4",Q:"5/4",ell:"1/2",lambda:"1/2"},
variables:["T","z=Q*t"],physicalD:"1/4-T^2",actualF:"7/2+25*T/4",
originalInput:"the complete compact original mean_R/mean_W/mean_O/N1, with f=-Pc/Pf",
primitiveQuadratics:prim.map((x,i)=>({name:names[i],originalScale:str(x.scale),polynomial:pdata(x.p)})),
macaulay:{degree:6,rows:rows.length,columns:monomials.length,actualRank:basis.length,allBasisRowProductsReturned:true},
attempts,identity:found,originalConstantFiberExcluded:found!==null,
oldProjectionReplayed:false,wholeH7Excluded:false,wholePhiFaceExcluded:false,ordinaryISPClaim:false,
elapsedMilliseconds:Date.now()-started};
