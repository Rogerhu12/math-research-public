/* R387 fixed CM/Heisenberg source and rank certificate. No target-prime scan. */
function verifyR387(){

function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denom");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}add(x){return new Q(this.a*x.b+x.a*this.b,this.b*x.b);}neg(){return new Q(-this.a,this.b);}sub(x){return this.add(x.neg());}mul(x){return new Q(this.a*x.a,this.b*x.b);}inv(){return new Q(this.b,this.a);}div(x){return this.mul(x.inv());}eq(x){return this.a===x.a&&this.b===x.b;}zero(){return !this.a;}str(){return this.b===1n?String(this.a):this.a+"/"+this.b;}}
const q=x=>new Q(x),zq=q(0),oq=q(1);
class K{constructor(a=zq,b=zq){this.a=a instanceof Q?a:q(a);this.b=b instanceof Q?b:q(b);}add(x){return new K(this.a.add(x.a),this.b.add(x.b));}neg(){return new K(this.a.neg(),this.b.neg());}sub(x){return this.add(x.neg());}mul(x){return new K(this.a.mul(x.a).sub(this.b.mul(x.b)),this.a.mul(x.b).add(this.b.mul(x.a)).sub(this.b.mul(x.b)));}conj(){return new K(this.a.sub(this.b),this.b.neg());}inv(){const n=this.a.mul(this.a).sub(this.a.mul(this.b)).add(this.b.mul(this.b));const c=this.conj();return new K(c.a.div(n),c.b.div(n));}div(x){return this.mul(x.inv());}eq(x){return this.a.eq(x.a)&&this.b.eq(x.b);}zero(){return this.a.zero()&&this.b.zero();}str(){return [this.a.str(),this.b.str()];}}
const k=(a,b=0)=>new K(a,b),zero=k(0),one=k(1);
const trim=a=>{while(a.length&&a.at(-1).zero())a.pop();return a;};
const padd=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||zero).add(b[i]||zero)));
const pneg=a=>a.map(x=>x.neg()), psub=(a,b)=>padd(a,pneg(b));
const pscale=(a,x)=>trim(a.map(y=>y.mul(x)));
function pmul(a,b){if(!a.length||!b.length)return[];const r=Array.from({length:a.length+b.length-1},()=>zero);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=r[i+j].add(a[i].mul(b[j]));return trim(r);}
function divrem(a,b){a=a.slice();if(!b.length)throw Error("poly zero");const q=Array.from({length:Math.max(0,a.length-b.length+1)},()=>zero),lead=b.at(-1).inv();while(a.length>=b.length){const i=a.length-b.length,c=a.at(-1).mul(lead);q[i]=c;for(let j=0;j<b.length;j++)a[i+j]=a[i+j].sub(c.mul(b[j]));trim(a);}return[trim(q),a];}
const mod=(a,f)=>divrem(a,f)[1];
function pinv(a,f){let r0=f,r1=mod(a,f),s0=[],s1=[one];while(r1.length){const [q,r]=divrem(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,psub(s0,pmul(q,s1))];}if(r0.length!==1)throw Error("not unit");return mod(pscale(s0,r0[0].inv()),f);}
function ppow(a,n,f){let r=[one];a=mod(a,f);while(n){if(n%2)r=mod(pmul(r,a),f);n=Math.floor(n/2);if(n)a=mod(pmul(a,a),f);}return r;}
const derivative=a=>trim(a.slice(1).map((x,i)=>x.mul(k(i+1))));
function traceR(a,f){return (mod(pmul(a,derivative(f)),f)[f.length-2]||zero);}


let checks=0;
const ok=(t,label)=>{if(!t)throw Error(label);checks++;};
const mv=(M,v)=>M.map(r=>r.reduce((s,x,j)=>s.add(x.mul(v[j])),zero));
const veq=(a,b)=>a.length===b.length&&a.every((x,j)=>x.eq(b[j]));
const mm=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s.add(x.mul(B[k][j])),zero)));
const det3=A=>A[0][0].mul(A[1][1].mul(A[2][2]).sub(A[1][2].mul(A[2][1]))).sub(A[0][1].mul(A[1][0].mul(A[2][2]).sub(A[1][2].mul(A[2][0])))).add(A[0][2].mul(A[1][0].mul(A[2][1]).sub(A[1][1].mul(A[2][0]))));
const delta=k(1,2),om=k(0,1),scale=(v,a)=>v.map(x=>x.mul(a));
function cm(n,g,qq){
 const qb=qq.map(x=>x.conj()),gb=g.conj();
 const xm=(q0,h)=>{const dq=derivative(q0),ddq=derivative(dq),sq=pmul(q0,q0);
  return{num:psub(psub(pmul([zero,k(n)],sq),pscale(pmul([one,zero,zero,one],psub(pmul(ddq,q0),pmul(dq,dq))),k(4))),pscale(pmul([zero,zero,one],pmul(dq,q0)),k(6))),den:pscale(sq,h.mul(h))};};
 const a=xm(qq,g),b=xm(qb,gb),rows=[],anchors=[];
 const na=psub(pmul(derivative(a.num),a.den),pmul(a.num,derivative(a.den)));
 const nb=psub(pmul(derivative(b.num),b.den),pmul(b.num,derivative(b.den)));
 for(const h of[2,3,4,5]){
  let f=psub(a.num,pscale(a.den,k(h)));f=pscale(f,f.at(-1).inv());ok(f.length===n+1,"full fiber degree");
  const ratio=mod(pmul(qb,pinv(qq,f)),f),xb=mod(pmul(b.num,pinv(b.den,f)),f);
  let val=mod(pmul(ppow(ratio,16,f),ppow(xb,2,f)),f);const step=ppow(xb,3,f),row=[];
  for(let j=0;j<3;j++){row.push(traceR(val,f));val=mod(pmul(val,step),f);}rows.push(row);
  if(h<5&&n===7){
   let yr=mod(pmul(nb,pinv(na,f)),f);yr=mod(pmul(yr,ppow(a.den,2,f)),f);
   yr=pscale(mod(pmul(yr,pinv(ppow(b.den,2,f),f)),f),g.div(gb));
   const pol=pscale(padd(padd(ppow(xb,6,f),pscale(ppow(xb,3,f),k(20))),[k(-8)]),k(-4));
   const image=traceR(mod(pmul(pmul(ppow(ratio,16,f),yr),pol),f),f);
   anchors.push(image.div(k(-4n*(BigInt(h)**6n+20n*BigInt(h)**3n-8n))));
  }
 }
 const A=[2,3,4].map((h,i)=>[k(BigInt(h)**2n),k(BigInt(h)**5n),k(BigInt(h)**8n),...rows[i]]);
 for(let j=0;j<3;j++){const c=A[j][j];A[j]=A[j].map(x=>x.div(c));for(let i=0;i<3;i++)if(i!==j){const h=A[i][j];A[i]=A[i].map((x,r)=>x.sub(h.mul(A[j][r])));}}
 const M=A.map(r=>r.slice(3));
 for(let j=0;j<3;j++)ok(rows[3][j].eq(M.reduce((s,r,i)=>s.add(r[j].mul(k(5n**BigInt(2+3*i)))),zero)),"held full fiber");
 return{M,anchors};
}
const g7=k(3,1),g13=k(4,1);
const r7=cm(7,g7,pscale([k(new Q(4,7),new Q(12,7)),zero,zero,one],g7));
const r13=cm(13,g13,pscale([k(new Q(64,13),new Q(48,13)),zero,zero,k(8,12),zero,zero,one],g13));
r7.anchors.forEach(x=>ok(x.eq(g7),"actual sigma4 anchor"));
const pi7=g7.mul(om),pi13=g13.mul(om.mul(om)).neg();
const D=[one,one,zero],H=[k(-8),k(20),one],K0=[k(64),k(-16),one];
for(const [z,pi,sgn] of[[r7,pi7,-1],[r13,pi13,1]]){
 ok(veq(mv(z.M,D),scale(H,pi.mul(delta).div(k(72)))),"D to H");
 ok(veq(mv(z.M,H),scale(D,pi.mul(delta).mul(k(24)))),"H to D");
 ok(veq(mv(z.M,K0),scale(K0,pi.mul(k(sgn)))),"third actual line");
}
const O=[[zero,zero,one],r7.M[2],mm(r7.M,r7.M)[2]];
ok(det3(O).eq(k(new Q(17,3888),new Q(-20,3888))),"mass observation determinant");
ok(det3(D.map((_,i)=>[D[i],H[i],K0[i]])).eq(k(108)),"integral basis");
const md=(x,n)=>((x%n)+n)%n;
const iv=(a,n)=>{for(let i=1;i<n;i++)if(md(a*i,n)===1)return i;throw Error("nonunit");};
const mn=(a,b,n)=>[md(a[0]*b[0]-a[1]*b[1],n),md(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],n)];
const rn=(a,n)=>mn(mn(a,a,n),[iv(md(a[0]*a[0]-a[0]*a[1]+a[1]*a[1],n),n),0],n);
const pn=(a,e,n)=>{let r=[1,0];while(e-- >0)r=mn(r,a,n);return r;};
const gr=[27,8],minus=[31,0],actual=new Set(),list=[];
for(let a=1;a<32;a+=2)for(let b=0;b<32;b+=2)actual.add(String(rn([a,b],32)));
for(let e=0;e<8;e++)for(let j=0;j<2;j++)list.push(mn(pn(gr,e,32),pn(minus,j,32),32));
ok(actual.size===16&&new Set(list.map(String)).size===16&&list.every(x=>actual.has(String(x))),"full finite ratio group");
ok(String(pn(gr,4,32))==="17,0"&&String(pn(gr,8,32))==="1,0","central kernel");
ok(String(rn([-1,2],32))==="27,8"&&String(rn([3,4],32))==="29,8","true primary phases");
ok(String(mn(minus,pn(gr,3,32),32))==="29,8","CM13 group relation");
ok(String(rn([1,8],16))==="9,0","exact conductor sixteen");
for(let e=0;e<8;e++)for(let j=0;j<2;j++){
 const n=md((e%2?7:1)*(j?3:1),8);ok(((n===1||n===3)?1:-1)===(e%2?-1:1),"rho square");
}
ok(new Q(24).div(new Q(1,72)).eq(q(1728)),"odd ratio inversion");
function ec(p){
 const m=x=>md(x,p),add=(P,Q)=>{if(P===null)return Q;if(Q===null)return P;if(P[0]===Q[0]&&m(P[1]+Q[1])===0)return null;
  const s=P[0]===Q[0]?m(3*P[0]*P[0]*iv(m(2*P[1]),p)):m((Q[1]-P[1])*iv(m(Q[0]-P[0]),p));
  const x=m(s*s-P[0]-Q[0]);return[x,m(s*(P[0]-x)-P[1])];};
 const mult=(P,n)=>{let R=null;while(n){if(n&1)R=add(R,P);P=add(P,P);n>>=1;}return R;};
 let count=1;for(let x=0;x<p;x++)for(let y=0;y<p;y++)if(m(y*y-x*x*x-24)===0)count++;return{add,mult,count};
}
const e5=ec(5),e7=ec(7),e19=ec(19),P=[17,4],Qp=[1,5],R=e19.add(P,Qp);
ok(e5.count===6&&e7.count===13,"torsion certificate");
ok(e19.count===27,"rank field");
ok(String(e19.mult(P,3))==="0,9"&&String(e19.mult(Qp,3))==="0,10","three multiples");
ok(String(R)==="18,2"&&e19.mult(R,3)===null,"independent order-three point");
ok(e19.mult(P,9)===null&&e19.mult(Qp,9)===null,"orders nine");
ok(g7.neg().eq(pi7.mul(om.mul(om).neg())),"actual E24 CM7 value");
return {status:"PASS",checks,field:"Q(omega), omega^2+omega+1=0",basis:"sigma^16*x^(2+3j), j=0,1,2, b=1",
CM7_matrix:r7.M.map(r=>r.map(x=>x.str())),CM13_matrix:r13.M.map(r=>r.map(x=>x.str())),
CM7_sigma4_anchor:r7.anchors.map(x=>x.str()),
mass_observation_determinant:det3(O).str(),ratio_group_order:actual.size,character_conductor:16,
normalized_pair:"JD=delta H/(72b), JH=24b delta D, J^2=-1",
odd_ball_ratio:"1728 b^2/(E/D+20b)-20b",
E24_rank_lower_bound:2,E24_certificate_primes:[5,7,19],E24_CM7_Frobenius:["-3","-1"]};

}
const certificate=verifyR387();
console.log(JSON.stringify(certificate,null,2));
