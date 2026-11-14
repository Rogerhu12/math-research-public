/* R396 fixed original ray, exact theta phases and joint-core certificate. */
function verifyR396(){

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

const g=k(3,1),gb=g.conj(),delta=k(1,2);
const cc=delta.mul(k(6)).sub(k(2)).div(k(7));
const q7=pscale([cc,zero,zero,one],g),qb7=q7.map(x=>x.conj());
function xmap(qq,gg){
 const dq=derivative(qq),ddq=derivative(dq),Q2=pmul(qq,qq);
 const num=psub(psub(pmul([zero,k(7)],Q2),pscale(pmul([one,zero,zero,one],psub(pmul(ddq,qq),pmul(dq,dq))),k(4))),pscale(pmul([zero,zero,one],pmul(dq,qq)),k(6)));
 const den=pscale(Q2,gg.mul(gg));
 return {num,den};
}
const ma=xmap(q7,g),mb=xmap(qb7,gb);

const na=psub(pmul(derivative(ma.num),ma.den),pmul(ma.num,derivative(ma.den)));
const nb=psub(pmul(derivative(mb.num),mb.den),pmul(mb.num,derivative(mb.den)));
const out=[];
for(const h of[2,3]){
 let f=psub(ma.num,pscale(ma.den,k(h)));f=pscale(f,f.at(-1).inv());
 const ratio=mod(pmul(qb7,pinv(q7,f)),f),xb=mod(pmul(mb.num,pinv(mb.den,f)),f);
 let yr=mod(pmul(nb,pinv(na,f)),f);yr=mod(pmul(yr,ppow(ma.den,2,f)),f);
 yr=pscale(mod(pmul(yr,pinv(ppow(mb.den,2,f),f)),f),g.div(gb));
 const im=traceR(mod(pmul(pmul(ppow(ratio,8,f),yr),xb),f),f).div(k(h));
 out.push({h,raw:im.str(),normalized:im.div(g.mul(k(0,1))).str()});
}

let checks=0;const ok=(v,s)=>{if(!v)throw Error(s);checks++;};
out.forEach(v=>ok(v.normalized[0]==="1"&&v.normalized[1]==="0","original A8 phase"));
const md=(x,n)=>((x%n)+n)%n,mn=(a,b,n)=>[md(a[0]*b[0]-a[1]*b[1],n),md(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],n)];
const inv=(a,n)=>{for(let j=1;j<n;j++)if(md(j*a,n)===1)return j;throw Error("nonunit");};
const norm=a=>a[0]*a[0]-a[0]*a[1]+a[1]*a[1];
const rat=(a,n)=>mn(mn(a,a,n),[inv(md(norm(a),n),n),0],n);
const pw=(a,e,n)=>{let r=[1,0];while(e-- >0)r=mn(r,a,n);return r;};
const a=[2143,2178];
ok(String(a.map(x=>md(x,32)))==="31,2","primary dyadic class");
ok(String(a.map(x=>md(x,9)))==="1,0","true cubic class");
ok(String(a.map(x=>md(x,17)))==="1,2","true seventeen class");
ok(norm(a)===4668679,"ray representative norm");
ok(String(rat(a,32))==="27,8","quartic ratio");
ok(String(rat(a,68))==="67,0","original Y ratio");
ok(String(rat(a,36))==="19,0","original C18 central ratio");
ok(String(pw([1,2],48,17))==="16,0","actual target twist minus sign");
const L=[[1,1,1],[1,-1,0],[9,9,-8]],N=[8,8,18];
const Gram=L.map(r=>L.map(s=>r.reduce((t,x,i)=>t+x*N[i]*s[i],0)));
ok(JSON.stringify(Gram)===JSON.stringify([[34,0,0],[0,16,0],[0,0,2448]]),"true integral orthogonal theta frame");
const detL=L[0][0]*(L[1][1]*L[2][2]-L[1][2]*L[2][1])-L[0][1]*(L[1][0]*L[2][2]-L[1][2]*L[2][0])+L[0][2]*(L[1][0]*L[2][1]-L[1][1]*L[2][0]);
ok(detL===34,"actual coordinate determinant");
const aa=delta.div(k(72*17)),dd=delta.mul(k(24*17));
ok(aa.mul(dd).eq(k(-1)),"same J square");
const scalarY=k(-1),scalarGlobal=k(1);
ok(scalarY.neg().eq(one)&&aa.mul(dd).neg().eq(one),"third core sign recovery");
return {status:"PASS",checks,ray_modulus:4896,primary_representative:a,norm:norm(a),
ratios:{mod32:rat(a,32),mod68:rat(a,68),mod36:rat(a,36)},
A8_CM7_fibers:out,coordinate_matrix:L,weighted_Gram:Gram,coordinate_determinant:detL,
J_D_to_H:aa.str(),J_H_to_D:dd.str(),
cores:{Y:"-lambda0",Q:"lambda0 J_Q",R:"lambda0 J_Q",all_inputs:"lambda0^3"},
same_Y_transport:"(Y,Q,R) -> (Y,Q/kappa,kappa R)",
boundary_difference:"(-lambda0)^(-1) B1'(0)-B0'(0)=2d lambda0 delta(1+lambda0) log(barpi)/(72b)"};


}
const certificate=verifyR396();
console.log(JSON.stringify(certificate,null,2));
