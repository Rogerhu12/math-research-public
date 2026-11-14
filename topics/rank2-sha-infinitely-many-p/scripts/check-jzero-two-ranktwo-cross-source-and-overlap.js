/* R399: original two-target cross source and full overlapping-domain certificate. */
function verifyR399(){

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

function evalK(p,x){let r=zero;for(let j=p.length-1;j>=0;j--)r=r.mul(x).add(p[j]);return r;}
const rows=[],hs=Array.from({length:13},(_,i)=>i+2),ts=hs.map(h=>k(BigInt(h)**3n));
for(const h of hs){
 let f=psub(ma.num,pscale(ma.den,k(h)));f=pscale(f,f.at(-1).inv());
 const ratio=mod(pmul(qb7,pinv(q7,f)),f),xb=mod(pmul(mb.num,pinv(mb.den,f)),f),step=ppow(xb,3,f);
 let val=ppow(ratio,72,f),row=[];
 for(let j=0;j<13;j++){row.push(traceR(val,f));val=mod(pmul(val,step),f);}
 rows.push(row);
}
const M=Array.from({length:13},()=>Array.from({length:13},()=>zero));
for(let r=0;r<13;r++){
 let L=[one],den=one;
 for(let j=0;j<13;j++)if(j!==r){L=pmul(L,[ts[j].neg(),one]);den=den.mul(ts[r].sub(ts[j]));}
 L=pscale(L,den.inv());
 for(let i=0;i<13;i++)for(let j=0;j<13;j++)M[i][j]=M[i][j].add(L[i].mul(rows[r][j]));
}
const vp=g.mul(k(0,1)),N=M.map(row=>row.map(x=>x.div(vp)));
const mv=(A,v)=>A.map(row=>row.reduce((s,x,j)=>s.add(x.mul(v[j]||zero)),zero));
const I=Array.from({length:13},(_,i)=>Array.from({length:13},(_,j)=>i===j?one:zero));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k0)=>s.add(x.mul(B[k0][j])),zero)));
let N9=I;for(let i=0;i<9;i++)N9=mm(N9,N);
const N18=mm(N9,N9);if(!N18.every((row,i)=>row.every((x,j)=>x.eq(I[i][j]))))throw Error("N18");
const q4=pmul([k(4),one],[k(64),k(48),k(-96),one]),Cpol=pscale(pmul([k(-8),one],[k(16),k(-4),k(7)]),k(7).inv());
const common=pmul([zero,one],pmul(q4,Cpol)),R2=[k(-8),k(20),one],Xp=[one,one];
const Qv=pmul(common,pmul(Xp,Xp)),T=pmul(common,pmul(Xp,R2)),P=pmul(common,pmul(R2,R2));
const out={};
for(const[name,v]of[["Q",Qv],["T",T],["P",P]]){
 const im=mv(N9,v);out[name]={v:v.map(x=>x.str()),N9:im.map(x=>x.str())};
}
const matrices={N:N.map(r=>r.map(x=>x.str())),N9:N9.map(r=>r.map(x=>x.str())),out,N18_identity:true};

let checks=0;function ok(c,s){if(!c)throw Error(s);checks++;}
const md=(a,m)=>(a%m+m)%m;
function mn(a,b,m){return[md(a[0]*b[0]-a[1]*b[1],m),md(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],m)];}
function ip(a,m){a=md(a,m);for(let j=1;j<m;j++)if(md(a*j,m)===1)return j;throw Error("inverse");}
function rn(a,m){return mn(mn(a,a,m),[ip(a[0]*a[0]-a[0]*a[1]+a[1]*a[1],m),0],m);}
function pn(a,n,m){let r=[1,0];while(n){if(n%2)r=mn(r,a,m);a=mn(a,a,m);n=Math.floor(n/2);}return r;}
const ray=[261631,198018],modulus=279072;
for(const[m,want]of[[32,[31,2]],[27,[1,0]],[17,[1,2]],[19,[1,0]]])
 ok(String(ray.map(x=>md(x,m)))===String(want),"original CRT "+m);
for(const[m,want]of[[32,[27,8]],[36,[19,0]],[68,[67,0]],[76,[39,0]],[108,[55,0]]])
 ok(String(rn(ray,m))===String(want),"whole ratio "+m);
ok(md(ray[0]*ray[0]-ray[0]*ray[1]+ray[1]*ray[1],8)===7,"actual quadratic dyadic sign");
ok(String(pn([1,2],48,17))==="16,0","original 17 phase");
ok(String(pn(rn([-1,2],144),9,144))==="91,72","pure dyadic ninth operator");
ok(String(pn(rn([-1,2],144),18,144))==="73,0","central eighteenth operator");
ok(N18.every((row,i)=>row.every((x,j)=>x.eq(I[i][j]))),"full N18");
const dec=x=>new K(new Q(...x[0].split("/")),new Q(...x[1].split("/")));
const outQ=matrices.out.Q, outT=matrices.out.T, outP=matrices.out.P;
ok(outQ.N9.map(dec).every((x,j)=>x.eq(dec(outQ.v[j]||["0","0"]))),"actual Q plus");
ok(outT.N9.map(dec).every((x,j)=>x.eq(dec(outT.v[j]||["0","0"]).neg())),"actual target minus");
ok(dec(outP.N9[12]).eq(new K(new Q(5,21))),"P output mass");
ok(dec(outP.N9[0]).eq(new K(new Q(-16777216,21))),"nonzero full residual column");
function powPoly(a,n){let r=[one];while(n--)r=pmul(r,a);return r;}
const P3=[k(64),k(48),k(-96),one];
const theta6=pmul(P3,psub(powPoly(P3,3),pscale(pmul([zero,zero,one],powPoly([k(4),one],6)),k(5832))));
ok(mv(N,theta6).every((x,j)=>x.eq(theta6[j]||zero)),"same-degree absolute Theta6 anchor");
const targetExpected=[0,262144,-229376,-1253376,159744,463872,-153216,391872,76440,-11484,-557,7,0].map(k0=>k(k0));
ok(T.every((x,j)=>x.mul(k(7)).eq(targetExpected[j])),"actual R398 target polynomial");
const d38=pmul(Xp,q4),h38=pmul(R2,q4);
ok(pmul(Xp,h38).every((x,j)=>x.eq(pmul(R2,d38)[j])),"entire 54 cross product");
ok(new Q(1,210).mul(q((-19683-1)+(4096-64))).eq(new Q(-1118,15)),"original H38 sixth coefficient");
ok(new Q(-1118,15).mul(q(720)).eq(q(-53664)),"ordinary original sixth moment");
ok(k(1,2).div(k(72)).mul(k(24,48)).eq(k(-1)),"original J squared");

function gp(rows,ws){return rows.map(r=>rows.map(s=>r.reduce((a,x,i)=>a+x*ws[i]*s[i],0)));}
ok(JSON.stringify(gp([[1,1],[19,-8]],[16,38]))===JSON.stringify([[54,0],[0,8208]]),"54 actual Gram");
ok(JSON.stringify(gp([[1,1],[9,-8]],[16,18]))===JSON.stringify([[34,0],[0,2448]]),"34 actual Gram");
ok(1*(-8)-19===-27&&1*(-8)-9===-17,"original lattice determinants");
ok((-8)*(-8)-17*27===-395,"actual collision intersection");

const pp0=[],pp1=[one],tt=[zero,one];
const ppInt=n=>n?[k(n)]:[],sc=(p,n,d=1)=>pscale(p,new K(new Q(n,d)));
const plusInt=(p,n)=>padd(p,ppInt(n));
const A54=[
 [sc(plusInt(sc(tt,8),19),1,27),sc(plusInt(tt,-1),8,27),pp0],
 [sc(plusInt(tt,-1),19,27),sc(plusInt(sc(tt,19),8),1,27),pp0],
 [pp0,pp0,pp1]];
const A34=[
 [sc(plusInt(sc(tt,-8),9),1,17),pp0,sc(plusInt(tt,1),-8,17)],
 [pp0,pp1,pp0],
 [sc(plusInt(tt,1),-9,17),pp0,sc(plusInt(sc(tt,-9),8),1,17)]];
const peq=(p,r)=>psub(p,r).length===0;
const rowAct=(r,M)=>M[0].map((_,j)=>r.reduce((a,x,i)=>padd(a,sc(M[i][j],x)),[]));
function assertRow(r,M,w,label){ok(rowAct(r,M).every((x,j)=>peq(x,w[j])),label);}
assertRow([1,1,0],A54,[tt,tt,pp0],"54 true output core");
assertRow([19,-8,0],A54,[ppInt(19),ppInt(-8),pp0],"54 preserves complement");
assertRow([1,0,1],A34,[sc(tt,-1),pp0,sc(tt,-1)],"34 full reflected core");
assertRow([9,0,-8],A34,[ppInt(9),pp0,ppInt(-8)],"34 preserves complement");
assertRow([1,1,1],A54,[tt,tt,pp1],"54 keeps whole output");
assertRow([1,1,1],A34,[sc(tt,-1),pp1,sc(tt,-1)],"34 keeps whole output with sign");
function detPoly(M){let o=[];for(let i=0;i<3;i++){
 const a=pmul(M[1][(i+1)%3],M[2][(i+2)%3]);
 const b=pmul(M[1][(i+2)%3],M[2][(i+1)%3]);
 o=padd(o,pmul(M[0][i],psub(a,b)));
}return o;}
ok(peq(detPoly(A54),tt),"54 determinant kappa");
ok(peq(detPoly(A34),sc(tt,-1)),"34 determinant minus kappa");
const ll=Array.from({length:3},(_,i)=>17*[1,1,0][i]-8*[1,0,1][i]);
const rr=Array.from({length:3},(_,i)=>27*[1,0,1][i]-8*[1,1,0][i]);
ok(String(ll)==="9,17,-8"&&String(rr)==="19,-8,27","two original unit tubes");
return {status:"PASS",checks,field:"Q(omega), omega^2+omega+1=0",ray,modulus,
whole_core_degrees:[38,54],reflected_degree:34,
source_order:{D:6,H:0,K:6,L:0,S:6,T:6,Q:12,P:0},
collision_intersection_determinant:-395,
Theta6_anchor:theta6.map(x=>x.str()),matrices};

}
const certificate=verifyR399();
console.log(JSON.stringify(certificate,null,2));
