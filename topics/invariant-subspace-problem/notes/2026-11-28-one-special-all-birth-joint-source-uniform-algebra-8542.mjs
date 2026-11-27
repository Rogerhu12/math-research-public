// Uniform original one-special-weight joint-source numerator certificate.
// 2026-11-28 Asia/Taipei; all arithmetic is exact BigInt.
const api=(()=>{

const ONE=new Map([[0,1n]]),T=new Map([[1,1n]]),U=new Map([[16,1n]]);
const add=(a,b)=>{const r=new Map(a);for(const[k,v]of b){const c=(r.get(k)||0n)+v;if(c)r.set(k,c);else r.delete(k);}return r;};
const scale=(a,c)=>new Map([...a].map(([k,v])=>[k,v*c]).filter(x=>x[1]));
const mul=(a,b)=>{const r=new Map;for(const[k,c]of a)for(const[h,d]of b){const v=(r.get(k+h)||0n)+c*d;if(v)r.set(k+h,v);else r.delete(k+h);}return r;};
const pow=(a,n)=>{let r=ONE;while(n--)r=mul(r,a);return r;};
const cn=x=>scale(ONE,BigInt(x));
const same=(a,b)=>a.size===b.size&&[...a].every(([k,c])=>b.get(k)===c);
const assert=(b,m)=>{if(!b)throw Error(m);};
const serialize=a=>[...a].sort((a,b)=>a[0]-b[0]).map(([k,c])=>({u:Math.floor(k/16),t:k%16,coefficient:String(c)}));
function run(){
 const start=Date.now(),r=add(U,cn(2)),rm1=add(r,cn(-1)),a=add(scale(T,2n),rm1),b=add(scale(T,3n),U),tr=add(T,r);
 const P=add(add(scale(pow(T,2),2n),scale(mul(rm1,T),4n)),mul(rm1,U));
 const s1gap=add(scale(mul(pow(tr,2),P),3n),scale(mul(mul(add(r,ONE),T),pow(add(T,cn(-1)),2)),-16n));
 const s1sos=add(scale(mul(pow(T,2),add(pow(add(T,cn(-1)),2),cn(27))),6n),
  mul(U,add(add(scale(pow(T,3),8n),mul(add(scale(r,33n),cn(65)),pow(T,2))),
    add(mul(add(add(scale(pow(r,2),18n),scale(r,6n)),cn(8)),T),scale(mul(pow(r,2),rm1),3n)))));
 assert(same(s1gap,s1sos),"S1 quarter SOS identity");
 const epsgap=add(scale(mul(add(r,ONE),P),3n),scale(mul(mul(rm1,tr),b),-2n));
 const epstarget=add(add(scale(pow(T,2),12n),scale(mul(mul(rm1,add(r,cn(4))),T),4n)),mul(mul(rm1,U),add(r,cn(3))));
 assert(same(epsgap,epstarget),"relative precision third identity");
 const s2gap=add(scale(mul(mul(r,add(pow(T,2),r)),pow(a,3)),9n),
 scale(mul(mul(mul(rm1,T),pow(add(T,cn(-1)),2)),pow(add(scale(T,3n),add(scale(r,2n),cn(-1))),2)),-8n));
 assert(s2gap.size===24&&[...s2gap.values()].every(c=>c>0n),"complete active S2 positive coefficients");
 const inactive=add(scale(mul(mul(add(r,ONE),add(T,add(r,cn(2)))),add(scale(T,3n),r)),4n),
  scale(mul(r,pow(add(scale(T,2n),add(r,ONE)),2)),-3n));
 const inactiveTarget=add(add(scale(pow(T,2),12n),scale(mul(mul(add(r,ONE),add(r,cn(6))),T),4n)),mul(mul(r,add(r,ONE)),add(r,cn(5))));
 assert(same(inactive,inactiveTarget),"inactive S2 two-thirds identity");
 assert([...epsgap.values()].every(c=>c>=0n)&&[...inactive.values()].every(c=>c>0n),"other uniform signs");
 return {schema:"isp-one-special-all-birth-joint-source-uniform-algebra-v1",elapsed_ms:Date.now()-start,
  variables:["u=r-2","t"],domain:"u>=0, t>0; actual model r=n-2s+1 is an integer >=2",
  exact_identities:{S1_quarter_SOS:true,precision_third:true,active_S2_half:true,inactive_S2_two_thirds:true},
  complete_active_S2_gap:serialize(s2gap),
  scope:"Exact integer numerator identities only; the actual full physical source, hard-top convention and complete tail decomposition are proved in the accompanying paper."};
}
return {run};

})();
console.log(JSON.stringify(api.run(),null,2));
