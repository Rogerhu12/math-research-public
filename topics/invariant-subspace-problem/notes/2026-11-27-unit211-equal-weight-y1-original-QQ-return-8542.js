"use strict";
const t0=Date.now();
function abs(x){return x<0n?-x:x;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){let z=a%b;a=b;b=z;}return a;}
class Q {
 constructor(n=0n,d=1n){if(n instanceof Q){this.n=n.n;this.d=n.d;return;}n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(o){o=new Q(o);return new Q(this.n*o.d+o.n*this.d,this.d*o.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(o){return this.add(new Q(o).neg());}
 mul(o){o=new Q(o);return new Q(this.n*o.n,this.d*o.d);}
 div(o){o=new Q(o);return new Q(this.n*o.d,this.d*o.n);}
 eq(o){o=new Q(o);return this.n===o.n&&this.d===o.d;}
 str(){return this.d===1n?""+this.n:this.n+"/"+this.d;}
}
class P {
 constructor(v=0){this.c=new Map();if(v instanceof P){this.c=new Map(v.c);return;}const q=new Q(v);if(q.n)this.c.set("0,0,0",q);}
 static term(e,c=1){const p=new P();const q=new Q(c);if(q.n)p.c.set(e.join(","),q);return p;}
 add(v){v=new P(v);const p=new P(this);for(const[k,a]of v.c){const z=(p.c.get(k)||new Q()).add(a);if(z.n)p.c.set(k,z);else p.c.delete(k);}return p;}
 neg(){const p=new P();for(const[k,a]of this.c)p.c.set(k,a.neg());return p;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const p=new P();for(const[k,a]of this.c){const e=k.split(",").map(Number);for(const[j,b]of v.c){const f=j.split(",").map(Number),key=e.map((z,i)=>z+f[i]).join(",");const z=(p.c.get(key)||new Q()).add(a.mul(b));if(z.n)p.c.set(key,z);else p.c.delete(key);}}return p;}
 scale(n,d=1){return this.mul(new Q(n,d));}
 pow(n){let a=this,b=new P(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=this.sub(v);return !v.c.size;}
 degree(i){return Math.max(-1,...Array.from(this.c.keys(),k=>+k.split(",")[i]));}
 json(){return Array.from(this.c,([k,c])=>[k.split(",").map(Number),c.str()]).sort((a,b)=>{for(let i=0;i<3;i++)if(a[0][i]!=b[0][i])return b[0][i]-a[0][i];return 0;});}
}
const m=P.term([1,0,0]),q=P.term([0,1,0]),t=P.term([0,0,1]),one=new P(1),d=one.sub(q),a=one.sub(m);
class E{
 constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;}else{this.a=new P(a);this.b=new P(b);}}
 add(v){v=new E(v);return new E(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new E(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new E(v).neg());}
 mul(v){v=new E(v);return new E(this.a.mul(v.a).add(d.mul(this.b).mul(v.b)),this.a.mul(v.b).add(this.b.mul(v.a)));}
 scale(n,dd=1){return this.mul(new E(new Q(n,dd)));}
 pow(n){let a=this,b=new E(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=new E(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
 conj(){return new E(this.a,this.b.neg());}
}
const b=new E(m.scale(1,2)),c=b,p=new E(1,1),pp=p.conj();
const X=new E(m,1),Y=X.conj(),f=m.sub(q.scale(1,4));
const rg=X.sub(new E(a).mul(p)).sub(c.mul(new E(t))),sg=Y.sub(new E(a).mul(pp)).sub(b.mul(new E(t)));
const Ag=new E(f.scale(2)).sub(b.mul(X).scale(2)).sub(c.mul(Y).scale(2)).add(b.mul(c).mul(new E(t)).scale(2));
const rows=[[new E(),new E(),p,pp],[new E(),Ag,rg,sg],[p,rg,new E(),new E(t)],[pp,sg,new E(t),new E()]];
const unit=[new E(1),new E(),new E(1),new E(1)];
const va=(v,w)=>v.map((z,i)=>z.add(w[i]));
const vs=(s,v)=>v.map(z=>new E(s).mul(z));
const vm=(v,w)=>[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])];
const tau=v=>new E(a).mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3]));
const DK=v=>rows.map(row=>tau(vm(row,v)));
const dv=DK(unit),F2=tau(dv),Kd=DK(dv);
if(!F2.eq(new E(f.scale(2))))throw Error("F2");
function mean(j){const ee=j===1?tau(vm(rows[0],rows[1])).scale(2):tau(vm(rows[j],rows[j]));return ee.sub(Kd[j].scale(2)).sub(vm(dv,dv)[j].scale(2)).add(F2.mul(dv[j]).scale(2));}
const E1=mean(1),EB=mean(2),EC=mean(3);
if(!mean(0).eq(0)||!EB.b.eq(0)||!EB.eq(EC)||!E1.b.eq(0))throw Error("same mean identities");
const E1expected=q.pow(2).scale(1,2).sub(m.scale(2)).add(m.pow(2).scale(2)).sub(m.pow(2).mul(t));
const Rtexp=t.pow(2).sub(t.scale(2)).mul(m).add(d.mul(m.sub(1)).scale(4));
if(!E1.a.eq(E1expected)||!EB.a.scale(2).eq(Rtexp))throw Error("hand mean identity");
function N4(v){return tau(vm(dv,vm(v,v))).scale(2).sub(F2.mul(tau(vm(v,v)))).sub(tau(v).mul(tau(vm(dv,v))).scale(4)).add(F2.mul(tau(v).pow(2)).scale(2)).add(tau(vm(v,DK(v))));}
function P2(v){const z=va(v,vs(tau(v).neg(),unit));return tau(vm(vm(z,z),z));}
const v=rows[0],z=rows[1],Nv=N4(va(v,z)).sub(N4(v)).sub(N4(z));
const vc=va(v,vs(tau(v).neg(),unit)),zc=va(z,vs(tau(z).neg(),unit)),Jnum=tau(vm(vm(vc,vc),zc));
const P02=m.mul(m.sub(1)).mul(m.scale(2).add(q.scale(3)).sub(4));
if(!P2(rows[0]).eq(new E(P02)))throw Error("P02");
const Lnum=N4(rows[0]).scale(1,2);
if(!Lnum.b.eq(0)||!Nv.b.eq(0)||!Jnum.b.eq(0))throw Error("even N");
const nw=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))),pw=b.mul(P2(rows[2])).add(c.mul(P2(rows[3])));
if(!nw.b.eq(0)||!pw.b.eq(0))throw Error("even weighted");
const L=Lnum.a,J=Jnum.a,NN=Nv.a;
const N1=P02.mul(NN).sub(L.mul(J).scale(4));
const Ns=P02.pow(2).mul(nw.a).sub(m.sub(1).mul(L).mul(P02.pow(2)).scale(2)).add(L.mul(J).mul(P02).scale(4)).sub(L.pow(3).scale(4));
const Ps=P02.pow(2).mul(pw.a).sub(m.sub(1).mul(P02.pow(3))).add(J.mul(P02.pow(2)).scale(3)).sub(L.pow(3).scale(4));
const nt=m.mul(m.sub(1)).scale(4).add(q.pow(2)),dt=m.pow(2).scale(2);
function substituteT(v){const degree=v.degree(2);let out=new P();for(const[key,c]of v.c){const e=key.split(",").map(Number);out=out.add(P.term([e[0],e[1],0],c).mul(nt.pow(e[2])).mul(dt.pow(degree-e[2])));}return {poly:out,power:degree};}
const rt=substituteT(Rtexp),n1=substituteT(N1),ns=substituteT(Ns),ps=substituteT(Ps);
const G=q.pow(4).add(m.mul(m.sub(2)).mul(q.pow(2)).scale(4)).add(m.pow(2).mul(m.sub(1).pow(2)).scale(16)).sub(m.pow(3).mul(m.sub(1)).mul(q).scale(16));
if(!rt.poly.eq(m.mul(G)))throw Error("quartic exact return");
function remainderQ(v){let z=new P(v);while(z.degree(1)>=4){let degree=z.degree(1);let lead=new P();for(const[key,c]of z.c){let e=key.split(",").map(Number);if(e[1]===degree)lead=lead.add(P.term([e[0],e[1]-4,0],c));}z=z.sub(lead.mul(G));}return z;}
const result={stage:"equal_weight_y_one_original_low_degree_input",seconds:(Date.now()-t0)/1000,originalMeanIdentities:true,wholeYOneForcesXEqualM:true,uniqueT:"2-2/m+Q^2/(2m^2)",originalN0P0:true,quarticReturn:true,excluded:false,polys:{}};
for(const[name,value]of [["G",G],["N1",remainderQ(n1.poly)],["Ns",remainderQ(ns.poly)],["Ps",remainderQ(ps.poly)]])result.polys[name]={degrees:[value.degree(0),value.degree(1)],terms:value.c.size,coefficients:value.json()};
result.Lnum=L.json();result.Jnum=J.json();result.Nv=NN.json();result.denominatorP02=P02.json();result.substitutionPowers={N1:n1.power,Ns:ns.power,Ps:ps.power};

const stageStart=Date.now();
function qparse(v){let a=v.split("/");return new Q(a[0],a[1]||1);}
const uz=()=>new Q(0),uo=()=>new Q(1);
function ut(p){p=p.slice();while(p.length&&!p[p.length-1].n)p.pop();return p;}
function ua(p,q){return ut(Array.from({length:Math.max(p.length,q.length)},(_,i)=>(p[i]||uz()).add(q[i]||uz())));}
function un(p){return p.map(x=>x.neg());}
function us(p,q){return ua(p,un(q));}
function um(p,q){let z=Array.from({length:Math.max(0,p.length+q.length-1)},uz);if(!p.length||!q.length)return [];for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)z[i+j]=z[i+j].add(p[i].mul(q[j]));return ut(z);}
function uc(p,c){return ut(p.map(x=>x.mul(c)));}
function ud(p,q){p=ut(p);q=ut(q);if(!q.length)throw Error("zero polynomial divisor");const original=p.slice(),z=Array.from({length:Math.max(0,p.length-q.length+1)},uz);while(p.length>=q.length){const j=p.length-q.length,c=p[p.length-1].div(q[q.length-1]);z[j]=c;p=us(p,Array.from({length:j},uz).concat(uc(q,c)));}if(us(ua(um(z,q),p),original).length)throw Error("division return");return[ut(z),p];}
function ue(p,q){const [z,r]=ud(p,q);if(r.length)throw Error("not exact");return z;}
function ug(p,q){while(q.length){let r=ud(p,q)[1];p=q;q=r;}return p.length?uc(p,uo().div(p[p.length-1])):[];}
function ugx(p,q){let a=[uo()],b=[],c=[],d=[uo()];while(q.length){const[z,r]=ud(p,q);[p,q]=[q,r];[a,c]=[c,us(a,um(z,c))];[b,d]=[d,us(b,um(z,d))];}const sc=uo().div(p[p.length-1]);return[uc(p,sc),uc(a,sc),uc(b,sc)];}
function coeffM(poly){const out=Array.from({length:poly.degrees[1]+1},()=>[]);for(const[e,c]of poly.coefficients){while(out[e[1]].length<=e[0])out[e[1]].push(uz());out[e[1]][e[0]]=qparse(c);}return out.map(ut);}
const originalM={},primitiveM={},contents={};
for(const name of ["G","N1","Ns","Ps"]){const cc=coeffM(result.polys[name]);originalM[name]=cc;let content=[];for(const p of cc)content=ug(content,p);if(!content.length)throw Error("zero row");contents[name]=content;primitiveM[name]=cc.map(p=>ue(p,content));}
function det(A){A=A.map(r=>r.map(p=>p.slice()));let sign=1,prev=[uo()];for(let k=0;k<A.length-1;k++){if(!A[k][k].length){let i=k+1;while(i<A.length&&!A[i][k].length)i++;if(i===A.length)return[];[A[k],A[i]]=[A[i],A[k]];sign=-sign;}const piv=A[k][k];for(let i=k+1;i<A.length;i++){for(let j=k+1;j<A.length;j++)A[i][j]=ue(us(um(A[i][j],piv),um(A[i][k],A[k][j])),prev);A[i][k]=[];}prev=piv;}return uc(A[A.length-1][A.length-1],new Q(sign));}
function resultant(f,g){const n=f.length-1,m=g.length-1,N=n+m,mat=Array.from({length:N},()=>Array.from({length:N},()=>[]));for(let i=0;i<m;i++)for(let j=0;j<=n;j++)mat[i][i+j]=f[n-j];for(let i=0;i<n;i++)for(let j=0;j<=m;j++)mat[m+i][i+j]=g[m-j];return det(mat);}
const rs={};
for(const name of ["N1","Ns","Ps"])rs[name]=resultant(primitiveM.G,primitiveM[name]);
let gg=ug(rs.N1,rs.Ns);gg=ug(gg,rs.Ps);
const report={stage:"equal_weight_y_one_complete_Q_resultants",seconds:(Date.now()-stageStart)/1000,content:Object.fromEntries(Object.entries(contents).map(([k,p])=>[k,p.map(x=>x.str())])),resultantDegrees:Object.fromEntries(Object.entries(rs).map(([k,p])=>[k,p.length-1])),gcdDegree:gg.length-1,gcd:gg.map(x=>x.str()),primitiveRows:Object.fromEntries(Object.entries(primitiveM).map(([k,cc])=>[k,cc.map(p=>p.map(x=>x.str()))])),resultants:Object.fromEntries(Object.entries(rs).map(([k,p])=>[k,p.map(x=>x.str())])),excluded:false};
return {original:result,report};
