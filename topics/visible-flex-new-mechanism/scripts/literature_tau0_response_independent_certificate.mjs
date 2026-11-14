/**
 * Exact formal-jet checks for the reachable cubic direction tau0 = -J(q''^3)/3.
 * J(F)(x) = integral_x^r F, so J' = -F.
 * Variables x,f,g,h,j,k represent x,q,q',q'',q''',q''''.
 * J is the independent tail integral of (1+x^2)q''^2+2q'^2.
 * Only polynomial differentiation and rational arithmetic are evaluated.
 * This is not an evaluation of a profile, curve, surface, or research candidate.
 *
 * Import certificate() and check report.passed.
 * The three checked derivative identities use zero right-collar boundary data
 * when converted to Volterra identities. They do not establish span membership
 * for the other 27 cubic commutator directions.
 */
export function certificate() {

const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;};
const rat=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
const ra=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),rm=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const size=7,z=()=>Array(size).fill(0),key=e=>e.join(",");
const con=(n,d=1)=>BigInt(n)===0n?new Map():new Map([[key(z()),rat(n,d)]]);
const variable=i=>{const e=z();e[i]=1;return new Map([[key(e),rat(1)]]);};
const plus=(...xs)=>{const r=new Map();for(const p of xs)for(const[k,v]of p){const q=ra(r.get(k)||rat(0),v);if(q[0])r.set(k,q);else r.delete(k);}return r;};
const times=(a,b)=>{let r=new Map();for(const[ka,va]of a)for(const[kb,vb]of b){const ea=ka.split(",").map(Number),eb=kb.split(",").map(Number),k=key(ea.map((v,i)=>v+eb[i]));const v=ra(r.get(k)||rat(0),rm(va,vb));if(v[0])r.set(k,v);else r.delete(k);}return r;};
const scale=(a,n,d=1)=>times(a,con(n,d));
const pow=(a,n)=>{let p=con(1);for(let i=0;i<n;i++)p=times(p,a);return p;};
const sub=(a,b)=>plus(a,scale(b,-1));
const [x,f,g,h,j,k,J]=Array.from({length:size},(_,i)=>variable(i));
const Q=plus(con(1),pow(x,2)),L=sub(pow(x,2),con(1)),m=sub(f,times(x,g));
const Dvars=[con(1),g,h,j,k,con(0),scale(plus(times(Q,pow(h,2)),scale(pow(g,2),2)),-1)];
const derivative=p=>{let r=con(0);for(const[term,coef]of p){const es=term.split(",").map(Number);for(let i=0;i<size;i++)if(es[i]){const e=es.slice(),n=e[i];e[i]--;r=plus(r,times(new Map([[key(e),rm(coef,rat(n))]]),Dvars[i]));}}return r;};
const a=plus(scale(times(x,pow(f,2)),1,2),scale(times(Q,times(f,g)),-1,2),scale(times(times(Q,x),pow(g,2)),1,4),scale(times(L,J),1,8));
const ap2=plus(times(f,g),scale(times(x,times(m,h)),-1),scale(times(x,pow(g,2)),-1,2),scale(times(times(x,L),pow(h,2)),-1,4),scale(J,1,4),scale(times(Q,times(plus(scale(m,2),times(L,h)),j)),-1,4));
const F=plus(scale(times(f,times(g,pow(h,2))),-1),scale(times(x,times(pow(g,2),pow(h,2))),1,2),scale(times(x,times(m,pow(h,3))),2,3),scale(times(times(x,sub(scale(pow(x,2),2),con(1))),pow(h,4)),1,12),scale(times(J,pow(h,2)),-1,4));
const G=plus(scale(times(x,pow(h,4)),-1,2),scale(times(g,pow(h,3)),2,3));
const localD=plus(scale(times(Q,times(m,pow(h,3))),-1,6),scale(times(times(Q,L),pow(h,4)),-1,16));
const localK=scale(times(Q,pow(h,4)),-1,4);
const differences={
 A_second_derivative:sub(derivative(derivative(a)),ap2),
 tau_directional_IBP:sub(sub(derivative(localD),F),times(pow(h,2),ap2)),
 mixed_primitive_IBP:plus(sub(derivative(localK),G),plus(times(Q,times(pow(h,3),j)),scale(times(g,pow(h,3)),2,3)))
};
return {schema:"formal-jet-tau0-response-check-v1",arithmetic:"BigInt exact rational polynomial jets",no_profile_or_geometry_evaluated:true,nonzero_monomial_counts:Object.fromEntries(Object.entries(differences).map(([k,v])=>[k,v.size])),passed:Object.values(differences).every(x=>x.size===0)};
}
