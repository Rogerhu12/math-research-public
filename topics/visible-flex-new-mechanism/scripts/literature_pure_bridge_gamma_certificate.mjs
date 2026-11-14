#!/usr/bin/env node
// Exact finite formal identities only. No profile, geometry, or optimization.
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;};
const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const plus=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const times=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
const accum=(out,k,v)=>{v=plus(out.get(k)||R(0),v);if(v[0])out.set(k,v);else out.delete(k);};
const add=(...xs)=>{let o=new Map;for(const x of xs)for(const[k,v]of x)accum(o,k,v);return o;};
const scale=(x,n,d=1)=>{let o=new Map;for(const[k,v]of x)accum(o,k,times(v,R(n,d)));return o;};
const atom=s=>new Map([[s,R(1)]]);
const empty=()=>new Map;
const op=(coeff,f,g)=>{let o=new Map;for(const[name,c]of coeff)for(const[k,u]of f)for(const[l,v]of g){const a=k<l?k:l,b=k<l?l:k;accum(o,JSON.stringify([name,a,b]),times(c,times(u,v)));}return o;};
const A=new Map([['A',R(1)]]), S=new Map([['S',R(1)]]), minusA=new Map([['A',R(-1)]]);
const q=atom('q'), a=op(A,q,q);
const Gamma=(X,E)=>{const aa=op(X,q,q),ee=op(E,q,q);return add(scale(op(X,aa,ee),1,16),scale(op(E,aa,aa),-1,16),scale(op(X,q,op(E,q,aa)),1,4),scale(op(E,q,op(X,q,aa)),-1,8),scale(op(X,q,op(X,q,ee)),-1,8));};
const P3=(X,w,v)=>{const aa=op(X,q,q);return add(scale(op(X,w,w),-1,16),scale(op(X,w,aa),-1,16),scale(op(X,aa,aa),-1,48),scale(op(X,q,v),1,4),scale(op(X,q,op(X,q,w)),-1,8),scale(op(X,q,op(X,q,aa)),-1,24));};
const D=x=>({v:x,d:empty()});
const dadd=(...xs)=>({v:add(...xs.map(x=>x.v)),d:add(...xs.map(x=>x.d))});
const dscale=(x,n,d=1)=>({v:scale(x.v,n,d),d:scale(x.d,n,d)});
const dop=(X,f,g)=>({v:op(X.v,f.v,g.v),d:add(op(X.d,f.v,g.v),op(X.v,f.d,g.v),op(X.v,f.v,g.d))});
const X={v:minusA,d:S}, Q=D(q), W=D(a), V=D(scale(op(A,q,a),-1,2)), AA=dop(X,Q,Q);
const p3dual=dadd(dscale(dop(X,W,W),-1,16),dscale(dop(X,W,AA),-1,16),dscale(dop(X,AA,AA),-1,48),dscale(dop(X,Q,V),1,4),dscale(dop(X,Q,dop(X,Q,W)),-1,8),dscale(dop(X,Q,dop(X,Q,AA)),-1,24));
const flow=(X,w,v,z)=>{const aa=op(X,q,q);return{w:add(w,aa),v:add(v,scale(op(X,q,w),-1),scale(op(X,q,aa),-1,2)),z:add(z,P3(X,w,v))};};
const flow2=(X,state)=>{const {w,v,b,c,p}=state,aa=op(X,q,q);return{
w:add(w,aa),v:add(v,scale(op(X,q,w),-1),scale(op(X,q,aa),-1,2)),
b,c:add(c,scale(op(X,q,b),-1)),
p:add(p,scale(op(X,b,w),-1,8),scale(op(X,q,c),1,4),scale(op(X,b,aa),-1,16),scale(op(X,q,op(X,q,b)),-1,8))};};
const bridge=(E,state)=>({w:state.w,v:state.v,b:add(state.b,op(E,q,q)),
c:add(state.c,scale(op(E,q,state.w),-1)),
p:add(state.p,scale(op(E,state.w,state.w),-1,16),scale(op(E,q,state.v),1,4))});
const wi=atom('incoming_w'),vi=atom('incoming_v'),zi=atom('incoming_p3');
const f1=flow(A,wi,vi,zi),f2=flow(minusA,f1.w,f1.v,f1.z);
const start2={w:wi,v:vi,b:atom('incoming_b0'),c:atom('incoming_c1'),p:atom('incoming_p2')};
const inverse2=flow2(minusA,flow2(A,start2));
const internalStart={...start2,w:empty(),v:empty()};
const internalResult=flow2(minusA,bridge(S,flow2(A,internalStart)));
const differences={
Gamma_derivative:add(scale(p3dual.d,3),scale(Gamma(A,S),-1)),
Gamma_parity:add(Gamma(A,S),scale(Gamma(minusA,S),-1)),
Gamma_self:Gamma(A,A),
inverse_w:add(f2.w,scale(wi,-1)),
inverse_v:add(f2.v,scale(vi,-1)),
inverse_p3:add(f2.z,scale(zi,-1)),
inverse_p2:add(inverse2.p,scale(start2.p,-1)),
inverse_b0:add(inverse2.b,scale(start2.b,-1)),
inverse_c1:add(inverse2.c,scale(start2.c,-1)),
internal_bridge_p2:add(internalResult.p,scale(internalStart.p,-1),scale(Gamma(A,S),-1))
};
for(const[name,value]of Object.entries(differences))if(value.size)throw Error('exact free-bilinear identity failed: '+name);
const report={schema:'pure-bridge-Gamma-free-bilinear-exact-v2',
arithmetic:'BigInt rational; free symmetric bilinear operators A and S; no associativity or commutation assumed',
independent_symbols:['q','incoming_w','incoming_v','incoming_p3','incoming_b0','incoming_c1','incoming_p2'],
derivative_pair_equals_Gamma_over_three:true,Gamma_even_under_A_sign:true,Gamma_A_A_zero:true,
full_highest_inverse_pair_for_arbitrary_incoming_history:true,
P2_inverse_pair_for_arbitrary_incoming_history:true,internal_bridge_P2_equals_Gamma:true,
difference_monomial_counts:Object.fromEntries(Object.entries(differences).map(([k,v])=>[k,v.size])),
Gamma_monomials:Gamma(A,S).size,actual_profile_geometry_compiler_or_optimization_run:false};

const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node literature_pure_bridge_gamma_certificate.mjs --out FILE');
report.source_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await mkdir(dirname(args[1]),{recursive:true});
await writeFile(args[1],JSON.stringify(report,null,2)+'\n');
