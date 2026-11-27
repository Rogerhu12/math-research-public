// Exact original Q-boundary four-quadratic leading certificate.
// 2026-11-27 Asia/Taipei (UTC+8). No imports or external data.
// BigInt exact QQ algebra only; clock is not used in mathematics.
function runCertificate(){const started=Date.now();

function gg(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
class Q{constructor(n=0n,d=1n){if(n instanceof Q){this.n=n.n;this.d=n.d;return;}n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gg(n,d);this.n=n/g;this.d=d/g;}add(b){b=new Q(b);return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}neg(){return new Q(-this.n,this.d);}sub(b){return this.add(new Q(b).neg());}mul(b){b=new Q(b);return new Q(this.n*b.n,this.d*b.d);}div(b){b=new Q(b);return new Q(this.n*b.d,this.d*b.n);}is0(){return this.n===0n;}eq(b){b=new Q(b);return this.n===b.n&&this.d===b.d;}str(){return this.d===1n?String(this.n):this.n+"/"+this.d;}}
const q0=new Q(),q1=new Q(1);
function tr(p){p=p.slice();while(p.length&&p[p.length-1].is0())p.pop();return p;}
function pa(a,b){let p=[];for(let i=0;i<Math.max(a.length,b.length);i++)p.push((a[i]||q0).add(b[i]||q0));return tr(p);}
function pn(a){return a.map(x=>x.neg());}
function ps(a,b){return pa(a,pn(b));}
function pm(a,b){if(!a.length||!b.length)return [];let p=Array.from({length:a.length+b.length-1},()=>q0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)p[i+j]=p[i+j].add(a[i].mul(b[j]));return tr(p);}
function pc(a,c){return tr(a.map(x=>x.mul(c)));}
function pd(a,b){if(!b.length)throw Error("zero polynomial division");let r=a.slice(),q=Array.from({length:Math.max(0,a.length-b.length+1)},()=>q0);while(r.length>=b.length&&r.length){let j=r.length-b.length,c=r[r.length-1].div(b[b.length-1]);q[j]=q[j].add(c);r=ps(r,Array.from({length:j},()=>q0).concat(pc(b,c)));}return[tr(q),r];}
function pg(a,b){while(b.length){let r=pd(a,b)[1];a=b;b=r;}return a.length?pc(a,q1.div(a[a.length-1])):[];}
function pe(a,b){return a.length===b.length&&a.every((x,i)=>x.eq(b[i]));}
class F{constructor(p=0,q=null){if(p instanceof F){this.p=p.p;this.q=p.q;return;}p=Array.isArray(p)?tr(p.map(x=>new Q(x))):tr([new Q(p)]);q=q===null?[q1]:tr(q.map(x=>new Q(x)));if(!q.length)throw Error("zero F denominator");if(!p.length){this.p=[];this.q=[q1];return;}let g=pg(p,q),ap=pd(p,g),aq=pd(q,g);if(ap[1].length||aq[1].length)throw Error("bad gcd");let c=q1.div(aq[0][aq[0].length-1]);this.p=pc(ap[0],c);this.q=pc(aq[0],c);}add(b){b=new F(b);return new F(pa(pm(this.p,b.q),pm(b.p,this.q)),pm(this.q,b.q));}neg(){return new F(pn(this.p),this.q);}sub(b){return this.add(new F(b).neg());}mul(b){b=new F(b);return new F(pm(this.p,b.p),pm(this.q,b.q));}div(b){b=new F(b);if(!b.p.length)throw Error("F zero divisor");return new F(pm(this.p,b.q),pm(this.q,b.p));}pow(n){let r=new F(1),a=this;while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}is0(){return !this.p.length;}eq(b){b=new F(b);return pe(pm(this.p,b.q),pm(b.p,this.q));}json(){return{n:this.p.map(x=>x.str()),d:this.q.map(x=>x.str())};}}

const ND=4,ZK="0,0,0,0";
class P{
 constructor(v=0){if(v instanceof P){this.m=v.m;return;}this.m=new Map();if(v instanceof Map){for(let[k,a]of v){a=new F(a);if(!a.is0())this.m.set(k,a);}return;}v=new F(v);if(!v.is0())this.m.set(ZK,v);}
 add(b){b=new P(b);let m=new Map(this.m);for(let[k,v]of b.m)m.set(k,(m.get(k)||new F()).add(v));return new P(m);}
 neg(){return new P(new Map([...this.m].map(([k,v])=>[k,v.neg()])));}
 sub(b){return this.add(new P(b).neg());}
 mul(b){b=new P(b);let m=new Map();for(let[k,v]of this.m)for(let[l,w]of b.m){let ka=k.split(",").map(Number),la=l.split(",").map(Number),key=ka.map((n,i)=>n+la[i]).join(",");m.set(key,(m.get(key)||new F()).add(v.mul(w)));}return new P(m);}
 div(b){b=new P(b);if(b.m.size!==1||!b.m.has(ZK))throw Error("P non-scalar divisor");let d=b.m.get(ZK);return new P(new Map([...this.m].map(([k,v])=>[k,v.div(d)])));}
 pow(n){let r=new P(1),a=this;while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}
 is0(){return !this.m.size;}eq(b){return this.sub(b).is0();}
 json(){return [...this.m].sort().map(([k,v])=>({e:k.split(",").map(Number),...v.json()}));}
}
function variable(i){let a=Array(ND).fill(0);a[i]=1;return new P(new Map([[a.join(","),new F(1)]]));}
function coeff(pp,i,n){return new P(new Map([...pp.m].filter(([k,v])=>Number(k.split(",")[i])===n).map(([k,v])=>{let a=k.split(",").map(Number);a[i]=0;return[a.join(","),v];})));}
function substitute(pp,i,value){let r=new P();for(let[k,v]of pp.m){let a=k.split(",").map(Number),n=a[i];a[i]=0;r=r.add(new P(new Map([[a.join(","),v]])).mul(value.pow(n)));}return r;}

const u=new P(new F([0,1])),ell=variable(0),x=variable(1),y=variable(2),t=variable(3),Qp=new P(1).sub(u);
class E{constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;return;}this.a=new P(a);this.b=new P(b);}add(o){o=new E(o);return new E(this.a.add(o.a),this.b.add(o.b));}neg(){return new E(this.a.neg(),this.b.neg());}sub(o){return this.add(new E(o).neg());}mul(o){o=new E(o);return new E(this.a.mul(o.a).add(u.mul(this.b).mul(o.b)),this.a.mul(o.b).add(this.b.mul(o.a)));}pow(n){let z=new E(1);for(let i=0;i<n;i++)z=z.mul(this);return z;}eq(o){o=new E(o);return this.a.eq(o.a)&&this.b.eq(o.b);}conj(){return new E(this.a,this.b.neg());}}
const b=new E(ell.div(2),u.sub(ell).div(u.mul(2))),c=b.conj(),a=new E(new P(1).sub(ell)),p=new E(1,1),q=p.conj(),bc=b.mul(c).a;
const V2=u.mul(2).sub(ell.mul(Qp)),T0=V2.sub(u.pow(2).mul(2)),P02=new P(2).sub(u.mul(3)).mul(V2).sub(Qp.mul(u)).add(u.pow(3).mul(2));
const X=new E(x,y),Y=X.conj(),f=u.mul(x).add(u.sub(ell.mul(Qp)).mul(y)).sub(T0.div(2)).div(u.mul(2));
const W2=V2.mul(x).add(u.mul(2).sub(u.mul(Qp)).sub(ell.mul(Qp)).mul(y));
const rg=X.sub(a.mul(p)).sub(c.mul(new E(t))),sg=Y.sub(a.mul(q)).sub(b.mul(new E(t))),A1=new E(f.mul(2)).sub(b.mul(X).mul(2)).sub(c.mul(Y).mul(2)).add(new E(bc.mul(t).mul(2)));
const rows=[[new E(),new E(),p,q],[new E(),A1,rg,sg],[p,rg,new E(),new E(t)],[q,sg,new E(t),new E()]],one=[new E(1),new E(),new E(1),new E(1)];
const va=(v,w)=>v.map((z,i)=>z.add(w[i])),vs=(k,v)=>v.map(z=>new E(k).mul(z)),vm=(v,w)=>[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])],tau=v=>a.mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3])),DK=v=>rows.map(row=>tau(vm(row,v)));
const dd=DK(one),F2=tau(dd),Kd=DK(dd);
if(!F2.eq(new E(f.mul(2))))throw Error("bad f");
function mean(j){let e=j===1?tau(vm(rows[0],rows[1])).mul(2):tau(vm(rows[j],rows[j]));return e.sub(Kd[j].mul(2)).sub(vm(dd,dd)[j].mul(2)).add(F2.mul(dd[j]).mul(2));}
if(!mean(0).eq(0))throw Error("bad E0");
const E1=mean(1),EB=mean(2),EC=mean(3);

const Rt0=u.mul(EB.b).add(u.sub(ell.mul(Qp)).div(u).mul(EB.a));
const Ry0=bc.mul(EB.a).mul(-4).add(ell.mul(Rt0));
const M=bc.mul(u).mul(4),H=u.mul(2).sub(1).mul(ell).add(u);
if(!coeff(Ry0,3,1).eq(M.mul(y.sub(1))))throw Error("Ry t coefficient");
if(!E1.b.is0()||!EB.conj().eq(EC))throw Error("conjugate mean");

const Lnum=W2.sub(u.mul(T0)).sub(V2.add(u.pow(2).mul(2)).mul(f)).add(bc.mul(Qp).mul(t));
const JJ=u.mul(new P(1).sub(u)).mul(2).add(ell.mul(Qp)),Phi=T0.add(u.mul(4)).sub(4).add(Qp),Pf=T0.mul(JJ.sub(Qp));
const Tnum=Lnum.sub(Qp.mul(T0)).mul(T0).sub(Pf.mul(f)).sub(Phi.mul(bc).mul(Qp).mul(t)).div(Qp).sub(ell.mul(P02));
function N4(v){return tau(vm(dd,vm(v,v))).mul(2).sub(F2.mul(tau(vm(v,v)))).sub(tau(v).mul(tau(vm(dd,v))).mul(4)).add(F2.mul(tau(v).pow(2)).mul(2)).add(tau(vm(v,DK(v))));}
function P2(v){const cen=va(v,vs(tau(v).neg(),one));return tau(vm(cen,vm(cen,cen)));}
const vz=rows[0],zw=rows[1],Nv=N4(va(vz,zw)).sub(N4(vz)).sub(N4(zw)),vc=va(vz,vs(tau(vz).neg(),one)),zc=va(zw,vs(tau(zw).neg(),one)),Pj=tau(vm(vm(vc,vc),zc)).mul(3);
if(!P2(rows[0]).eq(new E(P02))||!N4(rows[0]).eq(new E(Lnum.mul(2)))||!Pj.eq(new E(Lnum.sub(P02).sub(Tnum).mul(3))))throw Error("original E0/N0/P1 solve");
const NH0=Nv.mul(new E(P02)).sub(new E(Lnum.mul(new F(4).div(3))).mul(Pj));
const NS0=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))).mul(new E(P02.pow(2))).sub(new E(Lnum.mul(2).mul(ell.add(1).mul(P02.pow(2)).add(Tnum.mul(P02).mul(2)).add(Lnum.pow(2).mul(2)).sub(Lnum.mul(P02).mul(2)))));
const PS0=b.mul(P2(rows[2])).add(c.mul(P2(rows[3]))).mul(new E(P02.pow(2))).sub(new E(ell.add(2).mul(P02.pow(3)).add(Tnum.mul(P02.pow(2)).mul(3)).add(Lnum.pow(3).mul(4)).sub(Lnum.mul(P02.pow(2)).mul(3))));
if(!NH0.b.is0()||!NS0.b.is0()||!PS0.b.is0())throw Error("scalar original returns");

function originalHead(pp,mon){const out=new Map();for(const[key,c]of pp.m){const e=key.split(",").map(Number);if(e.slice(1).every((v,j)=>v===mon[j]))out.set([e[0],0,0,0].join(","),c);}return new P(out);}
function determinant(pp){const n=pp.length;if(n===0)return new P(1);let out=new P();for(let j=0;j<n;j++){if(pp[0][j].is0())continue;const part=pp[0][j].mul(determinant(pp.slice(1).map(row=>row.filter((v,k)=>k!==j))));out=j%2?out.sub(part):out.add(part);}return out;}
const mons2=[[2,0,0],[1,1,0],[1,0,1],[0,2,0],[0,1,1],[0,0,2]],
 originalQuadrics=[E1.a,Rt0,Ry0,NH0.a],Hrows=originalQuadrics.map(row=>mons2.map(mon=>originalHead(row,mon)));
function expected(rows){let out=new P();for(let i=0;i<rows.length;i++)out=out.add(ell.pow(i).mul(new F(rows[i])));return out;}
const G=[
 expected([[0,0,-32,80,-64],[0,32,0,-64],[-8,-72,192,-128],[24,-56,32]]),
 expected([[0,0,-16,40,-32],[0,24,-24,-16],[-8,-32,96,-64],[16,-32,16]]),
 expected([[0,0,-2],[0,-2,8,-8],[2],[-4,6]])
],cols=[[0,1,2,3],[0,1,2,4],[0,1,2,5]];
for(let i=0;i<3;i++){const dd=determinant(Hrows.map(row=>cols[i].map(j=>row[j])));
 if(!dd.mul(u.pow(4)).eq(M.pow(3).mul(Qp.pow(2)).mul(G[i])))throw Error("original four-row head minor "+i);}
const Lh=ell.add(u.mul(2)).sub(1),Khead=Qp.pow(2).mul(u.mul(12).sub(8).mul(ell.pow(2)).add(u.mul(new P(16).sub(u.mul(15))).mul(ell)).add(u.pow(2).mul(u.mul(2).sub(5))));
if(!G[1].sub(G[0].div(2)).eq(u.sub(1).mul(ell).mul(ell.sub(u.mul(2))).mul(Lh).mul(-4)))throw Error("original head minor difference");
if(!G[2].mul(Qp.pow(2)).mul(2).add(P02.pow(2)).eq(Lh.mul(Khead)))throw Error("global three-minor unit identity");
function homogeneous2(pp){return new P(new Map([...pp.m].filter(([k,v])=>k.split(",").slice(1).map(Number).reduce((a,b)=>a+b,0)===2)));}
const zLinear=t.sub(y.mul(2)).add(x.mul(2).div(u)),headZ=originalQuadrics.map(row=>substitute(homogeneous2(row),3,zLinear));
if(!headZ[2].eq(M.mul(y).mul(t)))throw Error("actual R_y head M*y*z");
const planeMons=[[[2,0,0],[1,0,1],[0,0,2]],[[2,0,0],[1,1,0],[0,2,0]]],
 planeMatrices=planeMons.map(ms=>[0,1,3].map(i=>ms.map(mon=>originalHead(headZ[i],mon)))),
 binDet=planeMatrices.map(a=>determinant(a));
function resultantBinary(a,b){const z=new P();return determinant([[a[2],a[1],a[0],z],[z,a[2],a[1],a[0]],[b[2],b[1],b[0],z],[z,b[2],b[1],b[0]]]);}
const binRes=planeMatrices.map(a=>resultantBinary(a[0],a[1])),
 Fy=u.mul(3).sub(2).mul(ell.pow(3)).add(ell.pow(2)).add(u.neg().add(u.pow(2).mul(4)).sub(u.pow(3).mul(4)).mul(ell)).sub(u.pow(2)),
 Kz=u.sub(1).mul(ell.pow(2)).add(u.mul(2).sub(u.pow(2)).mul(ell)).add(u.pow(2).mul(u.mul(2).sub(1)));
if(!binRes[0].mul(u.pow(3)).eq(M.pow(2).mul(u.sub(1)).mul(ell.mul(2).sub(1)).mul(u.sub(ell.pow(2)))))throw Error("y0 original ER resultant");
if(!binDet[0].mul(u.pow(3)).eq(M.pow(2).mul(Qp.pow(2)).mul(Fy)))throw Error("y0 original ERN coefficient determinant");
if(!binRes[1].mul(u.pow(10)).eq(M.pow(2).mul(H.pow(2)).mul(Qp.pow(4)).mul(ell.sub(u)).mul(ell.sub(u).sub(u.pow(2).mul(4))).mul(16)))throw Error("z0 original ER resultant");
if(!binDet[1].mul(u.pow(8)).eq(M.pow(2).mul(H).mul(ell.sub(u.mul(2))).mul(u.sub(1).pow(5)).mul(Kz).mul(-16)))throw Error("z0 original ERN coefficient determinant");
if(!substitute(Fy,0,new P(new F(new Q(1,2)))).eq(u.mul(u.mul(4).sub(1).pow(2)).div(-8)))throw Error("ell half Fy whole fiber");
if(!substitute(M,0,new P(new F(new Q(1,2)))).eq(u.sub(1).mul(u.mul(4).sub(1)).div(-4)))throw Error("ell half physical M");
function uToEllSquare(pp){let out=new P();for(const[key,c]of pp.m){if(c.q.length!==1||!c.q[0].eq(1))throw Error("u substitution polynomial required");const e=key.split(",").map(Number);for(let j=0;j<c.p.length;j++)out=out.add(new P(new Map([[key,new F(c.p[j])]])).mul(ell.pow(2*j)));}return out;}
if(!uToEllSquare(Fy).eq(ell.pow(2).mul(ell.sub(1)).mul(ell.add(1).pow(2)).mul(ell.mul(2).sub(1).pow(2)).neg()))throw Error("u=ell^2 complete Fy fiber");
if(!uToEllSquare(M).eq(ell.pow(2).mul(ell.mul(2).sub(1))))throw Error("u=ell^2 physical M");
if(!substitute(Kz,0,u).eq(u.pow(3).mul(2)))throw Error("ell=u Kz");
const second=u.add(u.pow(2).mul(4));
if(!substitute(Kz,0,second).eq(u.pow(3).mul(u.mul(4).sub(1)).mul(u.mul(2).sub(1)).mul(2)))throw Error("ell=u+4u^2 Kz");
if(!substitute(M,0,second).eq(u.pow(3).mul(u.mul(4).sub(1).pow(2))))throw Error("ell=u+4u^2 physical M");
return {date:"2026-11-27",timezone:"Asia/Taipei (UTC+8)",input:"original Q=1-u Gram, E0/N0/P1 and original E1,Rt0,Ry0,NH0",
 units:["u","1-u","ell","M","H","P02","ell-2u","2u-1"],
 originalMinorColumns:cols,originalMinorMonomials:mons2,
 minorFactor:"Delta_i=(M^3*(1-u)^2/u^4)*G_i",
 globalIdentities:["G1-G0/2=-4*(u-1)*ell*(ell-2*u)*(ell+2*u-1)","2*(1-u)^2*G2+P02^2=(ell+2*u-1)*Khead"],
 binaryReturns:{
 y0:{resultant:"M^2*(u-1)/u^3*(2*ell-1)*(u-ell^2)",coefficientDeterminant:"M^2*(u-1)^2/u^3*Fy",wholeFibers:["ell=1/2","u=ell^2"]},
 z0:{resultant:"16*M^2*H^2*(u-1)^4/u^10*(ell-u)*(ell-u-4*u^2)",coefficientDeterminant:"-16*M^2*H*(ell-2*u)*(u-1)^5/u^8*Kz",wholeFibers:["ell=u","ell=u+4*u^2"]}},
 allExactIdentitiesVerified:true,elapsedMs:Date.now()-started,
 consequenceByProof:"head rank 4 and no projective common zero; cubic head span has rank 10; actual quotient has dimension at most 6",
 generatingCharts:[["1","x","y","t","y*t","t^2"],["1","x","y","t","y^2","t^2"],["1","x","y","t","y^2","y*t"]],
 limitation:"six generators need not be independent; actual quotient multiplication requires all relations and same original parameter"};

}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module){console.log(JSON.stringify(runCertificate()));}
