/* Self-contained exact original Q=1-u, ell=0 return.
 * Date: 2026-11-27 Asia/Taipei. Only BigInt QQ arithmetic is used.
 * All divisions and extended identities are multiplied back.
 */
(function(){
"use strict";
const emit=v=>{if(typeof text==="function")text(v);else console.log(JSON.stringify(v));};

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
class P{constructor(v=0){if(v instanceof P){this.m=v.m;return;}this.m=new Map();if(v instanceof Map){for(let[k,a]of v){a=new F(a);if(!a.is0())this.m.set(k,a);}return;}v=new F(v);if(!v.is0())this.m.set("0,0",v);}add(b){b=new P(b);let m=new Map(this.m);for(let[k,v]of b.m)m.set(k,(m.get(k)||new F()).add(v));return new P(m);}neg(){return new P(new Map([...this.m].map(([k,v])=>[k,v.neg()])));}sub(b){return this.add(new P(b).neg());}mul(b){b=new P(b);let m=new Map();for(let[k,v]of this.m)for(let[l,w]of b.m){let a=k.split(",").map(Number),c=l.split(",").map(Number),t=(a[0]+c[0])+","+(a[1]+c[1]);m.set(t,(m.get(t)||new F()).add(v.mul(w)));}return new P(m);}div(b){b=new P(b);if(b.m.size!==1||!b.m.has("0,0"))throw Error("P denominator not scalar");let d=b.m.get("0,0");return new P(new Map([...this.m].map(([k,v])=>[k,v.div(d)])));}pow(n){let r=new P(1),a=this;while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}is0(){return !this.m.size;}eq(b){return this.sub(b).is0();}json(){return [...this.m].sort().map(([k,v])=>({e:k.split(",").map(Number),...v.json()}));}}

function makeAtT(tt){
const u=new P(new F([0,1])),ell=new P(0),Qp=new P(1).sub(u);
const x=new P(new Map([["1,0",new F(1)]])),y=new P(new Map([["0,1",new F(1)]]));
const t=new P(tt);
class E{constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;return;}this.a=new P(a);this.b=new P(b);}add(o){o=new E(o);return new E(this.a.add(o.a),this.b.add(o.b));}neg(){return new E(this.a.neg(),this.b.neg());}sub(o){return this.add(new E(o).neg());}mul(o){o=new E(o);return new E(this.a.mul(o.a).add(u.mul(this.b).mul(o.b)),this.a.mul(o.b).add(this.b.mul(o.a)));}pow(n){let z=new E(1);for(let i=0;i<n;i++)z=z.mul(this);return z;}eq(o){o=new E(o);return this.a.eq(o.a)&&this.b.eq(o.b);}conj(){return new E(this.a,this.b.neg());}}
const b=new E(ell.div(2),u.sub(ell).div(u.mul(2))),c=b.conj(),a=new E(new P(1).sub(ell)),p=new E(1,1),q=p.conj(),bc=b.mul(c).a;
const V2=u.mul(2).sub(ell.mul(Qp)),T0=V2.sub(u.pow(2).mul(2)),P02=new P(2).sub(u.mul(3)).mul(V2).sub(Qp.mul(u)).add(u.pow(3).mul(2));
const X=new E(x,y),Y=X.conj(),f=u.mul(x).add(u.sub(ell.mul(Qp)).mul(y)).sub(T0.div(2)).div(u.mul(2));
const W2=V2.mul(x).add(u.mul(2).sub(u.mul(Qp)).sub(ell.mul(Qp)).mul(y));
const lam=W2.sub(u.mul(T0)).sub(V2.add(u.pow(2).mul(2)).mul(f)).add(bc.mul(Qp).mul(t)).div(P02);
const J=u.mul(new P(1).sub(u)).mul(2).add(ell.mul(Qp)),Phi=T0.add(u.mul(4)).sub(4).add(Qp),Pf=T0.mul(J.sub(Qp));
const g=lam.mul(P02).sub(new P(1).sub(u).mul(T0));
const T=g.mul(T0).sub(Pf.mul(f)).sub(Phi.mul(bc).mul(Qp).mul(t)).div(Qp.mul(P02)).sub(ell);
const rg=X.sub(a.mul(p)).sub(c.mul(new E(t))),sg=Y.sub(a.mul(q)).sub(b.mul(new E(t))),A1=new E(f.mul(2)).sub(b.mul(X).mul(2)).sub(c.mul(Y).mul(2)).add(new E(bc.mul(t).mul(2)));
const rows=[[new E(),new E(),p,q],[new E(),A1,rg,sg],[p,rg,new E(),new E(t)],[q,sg,new E(t),new E()]],one=[new E(1),new E(),new E(1),new E(1)];
const va=(v,w)=>v.map((z,i)=>z.add(w[i])),vs=(k,v)=>v.map(z=>new E(k).mul(z)),vm=(v,w)=>[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])],tau=v=>a.mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3])),DK=v=>rows.map(row=>tau(vm(row,v)));
const dd=DK(one),F2=tau(dd),Kd=DK(dd);
if(!F2.eq(new E(f.mul(2))))throw Error("bad f");
function mean(j){let e=j===1?tau(vm(rows[0],rows[1])).mul(2):tau(vm(rows[j],rows[j]));return e.sub(Kd[j].mul(2)).sub(vm(dd,dd)[j].mul(2)).add(F2.mul(dd[j]).mul(2));}
if(!mean(0).eq(0))throw Error("bad E0");
const E1=mean(1),EB=mean(2),EC=mean(3);
function N4(v){return tau(vm(dd,vm(v,v))).mul(2).sub(F2.mul(tau(vm(v,v)))).sub(tau(v).mul(tau(vm(dd,v))).mul(4)).add(F2.mul(tau(v).pow(2)).mul(2)).add(tau(vm(v,DK(v))));}
function P2(v){let cen=va(v,vs(tau(v).neg(),one));return tau(vm(cen,vm(cen,cen)));}
let v=rows[0],zv=rows[1],Nv=N4(va(v,zv)).sub(N4(v)).sub(N4(zv)),vc=va(v,vs(tau(v).neg(),one)),zc=va(zv,vs(tau(zv).neg(),one));
const Pj=tau(vm(vm(vc,vc),zc)).mul(3),NH=Nv.sub(new E(lam.mul(new F(4).div(3))).mul(Pj));
if(!N4(rows[0]).eq(new E(lam.mul(P02).mul(2))))throw Error("bad N0");
if(!Pj.eq(new E(lam.sub(1).sub(T).mul(P02).mul(3))))throw Error("bad P1");
if(!P2(rows[0]).eq(new E(P02)))throw Error("bad P0");
const A2=lam.pow(2).mul(2).sub(lam.mul(2)).add(1),B3=lam.pow(3).mul(4).sub(lam.pow(2).mul(6)).add(lam.mul(3)).sub(1);
const NS=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))).sub(new E(lam.mul(P02).mul(2).mul(ell.add(T.mul(2)).add(A2))));
const PS=b.mul(P2(rows[2])).add(c.mul(P2(rows[3]))).sub(new E(P02.mul(ell.add(T.mul(3)).add(A2.mul(3)).add(B3))));
const Rt=EB.b.add(u.sub(ell.mul(Qp)).div(u).mul(EB.a).div(u)).mul(u).div(bc.mul(2)),Ry=EB.a.neg().add(ell.mul(Rt).div(2));


return {E1:E1.a,Rt,Ry,N1:NH.a,NS:NS.a,PS:PS.a};
}

function rq(s){let[a,b]=s.split("/");return new Q(BigInt(a),b?BigInt(b):1n);}
const at=[0,1,2,3].map(makeAtT), cs={},degrees={E1:1,Rt:2,Ry:1,N1:2,NS:3,PS:3};
for(const name of Object.keys(degrees)){
 let[a,b,c,d]=at.map(v=>v[name]);
 let vv=[a,a.mul(-11).add(b.mul(18)).sub(c.mul(9)).add(d.mul(2)).div(6),a.mul(2).sub(b.mul(5)).add(c.mul(4)).sub(d).div(2),a.neg().add(b.mul(3)).sub(c.mul(3)).add(d).div(6)];
 for(let i=0;i<4;i++){let r=new P();for(let j=0;j<4;j++)r=r.add(vv[j].mul(i**j));if(!r.eq(at[i][name]))throw Error("t interpolation");}
 for(let j=degrees[name]+1;j<4;j++)if(!vv[j].is0())throw Error("t degree");
 cs[name]=vv.slice(0,degrees[name]+1);
}
const uu=new P(new F([0,1])),yv=new P(new Map([["0,1",new F(1)]])),AA=cs.Ry[0].neg(),BB=uu.mul(yv.sub(1));
if(!cs.Ry[1].eq(BB))throw Error("t leading");
const hr={};for(const name of ["E1","Rt","N1","NS","PS"]){let p=new P(),n=degrees[name];for(let j=0;j<=n;j++)p=p.add(cs[name][j].mul(AA.pow(j)).mul(BB.pow(n-j)));hr[name]=p;}

function pfrom(data){return new P(new Map(data.map(z=>[z.e.join(","),new F(z.n.map(rq),z.d.map(rq))])));}
function xc(pp,i){return new P(new Map([...pp.m].filter(([k,v])=>Number(k.split(",")[0])===i).map(([k,v])=>["0,"+k.split(",")[1],v])));}
function detP(a){if(a.length===1)return a[0][0];let r=new P();for(let j=0;j<a.length;j++){let b=a.slice(1).map(row=>row.filter((_,k)=>k!==j)),v=a[0][j].mul(detP(b));r=j%2?r.sub(v):r.add(v);}return r;}
function halfPaid(a){a=a.slice();let hist=[];for(let[nm,p]of [["u",[q0,q1]],["u-1",[new Q(-1),q1]],["2u-3",[new Q(-3),new Q(2)]]]){let n=0;while(a.length>1){let g=pg(a,p);if(g.length<2)break;let z=pd(a,g);if(z[1].length)throw Error("half unit division");a=z[0];n++;}if(n)hist.push([nm,n]);}return{rest:a,hist};}
function cleanHalf(pp){if([...pp.m.keys()].some(k=>!k.startsWith("0,")))throw Error("not y");let deg=Math.max(...[...pp.m.keys()].map(k=>Number(k.split(",")[1]))),ar=Array.from({length:deg+1},()=>new F());for(let[k,v]of pp.m)ar[Number(k.split(",")[1])]=v;let den=[q1];for(let c of ar){let z=pd(pm(den,c.q),pg(den,c.q));if(z[1].length)throw Error("lcm");den=z[0];}if(halfPaid(den).rest.length>1)throw Error("unpaid denominator");let nums=ar.map(c=>pm(c.p,pd(den,c.q)[0])),content=[];for(let p of nums)content=pg(content,p);let unpaid=halfPaid(content).rest,paid=pd(content,unpaid)[0];nums=nums.map(p=>{let z=pd(p,paid);if(z[1].length)throw Error("content return");return z[0];});let count=0;while(nums.length>1){let q=Array.from({length:nums.length-1},()=>[]);q[q.length-1]=nums[nums.length-1];for(let j=nums.length-2;j>=1;j--)q[j-1]=pa(nums[j],q[j]);let rem=pa(nums[0],q[0]);if(rem.length)break;nums=q;count++;}return{row:nums.map(p=>new F(p).json()),den:den.map(z=>z.str()),paidContent:paid.map(z=>z.str()),unpaidContent:unpaid.map(z=>z.str()),y1Removed:count};}

function pxgcd(a,b){let A=a.slice(),B=b.slice(),s0=[q1],s1=[],t0=[],t1=[q1];while(B.length){let [q,r]=pd(A,B);if(!pe(pa(pm(q,B),r),A))throw Error("QQ division");A=B;B=r;[s0,s1]=[s1,ps(s0,pm(q,s1))];[t0,t1]=[t1,ps(t0,pm(q,t1))];}if(!A.length)return {g:[],s:[],t:[]};let k=q1.div(A[A.length-1]);A=pc(A,k);s0=pc(s0,k);t0=pc(t0,k);if(!pe(pa(pm(s0,a),pm(t0,b)),A))throw Error("QQ Bezout return");return {g:A,s:s0,t:t0};}
const phi=[q1,q0,q1];
let kinverses=0,kdivisions=0,kbezouts=0;
function kr(a){let [q,r]=pd(a,phi);if(!pe(pa(pm(q,phi),r),a))throw Error("K reduction");return r;}
function ka(a,b){return kr(pa(a,b));}
function kn(a){return pn(a);}
function ks(a,b){return ka(a,kn(b));}
function km(a,b){return kr(pm(a,b));}
function ki(a){let r=pxgcd(a,phi);if(r.g.length!==1||r.g[0].is0())throw Error("nonunit K");let v=kr(pc(r.s,q1.div(r.g[0])));if(!pe(km(v,a),[q1]))throw Error("K inverse return");kinverses++;return v;}
function kp(a,n){let r=[q1];while(n){if(n&1)r=km(r,a);a=km(a,a);n>>=1;}return r;}
function kt(a){a=a.slice();while(a.length&&!a[a.length-1].length)a.pop();return a;}
function kpa(a,b){let z=[];for(let i=0;i<Math.max(a.length,b.length);i++)z.push(ka(a[i]||[],b[i]||[]));return kt(z);}
function kpn(a){return a.map(kn);}
function kps(a,b){return kpa(a,kpn(b));}
function kpm(a,b){if(!a.length||!b.length)return [];let z=Array.from({length:a.length+b.length-1},()=>[]);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]=ka(z[i+j],km(a[i],b[j]));return kt(z);}
function kpd(a,b){let r=a.slice(),q=Array.from({length:Math.max(0,a.length-b.length+1)},()=>[]),iv=ki(b[b.length-1]);while(r.length>=b.length&&r.length){let j=r.length-b.length,c=km(r[r.length-1],iv);q[j]=ka(q[j],c);r=kps(r,Array.from({length:j},()=>[]).concat(b.map(z=>km(z,c))));}if(kps(a,kpa(kpm(q,b),r)).length)throw Error("K polynomial division return");kdivisions++;return {q:kt(q),r};}
function kxgcd(a,b){let A=a.slice(),B=b.slice(),s0=[[q1]],s1=[],t0=[],t1=[[q1]];while(B.length){let z=kpd(A,B);A=B;B=z.r;[s0,s1]=[s1,kps(s0,kpm(z.q,s1))];[t0,t1]=[t1,kps(t0,kpm(z.q,t1))];}if(!A.length)return {g:[],s:[],t:[]};let iv=ki(A[A.length-1]);A=A.map(z=>km(z,iv));s0=s0.map(z=>km(z,iv));t0=t0.map(z=>km(z,iv));if(kps(kpa(kpm(s0,a),kpm(t0,b)),A).length)throw Error("K Bezout return");kbezouts++;return {g:A,s:s0,t:t0};}
function kval(z){return km(kr(z.n.map(rq)),ki(kr(z.d.map(rq))));}
function yK(rows){return kt(rows.map(kval));}
function xK(rows,y0){let n=1+Math.max(...rows.map(z=>z.e[0])),a=Array.from({length:n},()=>[]);for(let z of rows)a[z.e[0]]=ka(a[z.e[0]],km(kval(z),kp(y0,z.e[1])));return kt(a);}

function requireIt(v,m){if(!v)throw Error(m);}
const E=hr.E1,L=xc(E,1),CC=xc(E,0);
requireIt(L.eq(uu.mul(new P(1).sub(uu)).mul(yv.mul(2).sub(1).pow(2))),"original E1 leading x");
requireIt(cs.Ry[0].eq(yv.sub(1).mul(uu.mul(yv).mul(2).sub(new P(new Map([["1,0",new F(1)]])).mul(2))).add(new P(1).sub(uu).mul(yv.mul(2).sub(1)))),"original ell=0 Ry");
const cleaned={};
for(const name of ["Rt","N1","NS","PS"]){const raw=hr[name],degree=Math.max(...[...raw.m.keys()].map(k=>+k.split(",")[0]));let r=new P();for(let i=0;i<=degree;i++)r=r.add(xc(raw,i).mul(CC.neg().pow(i)).mul(L.pow(degree-i)));cleaned[name]=cleanHalf(r);}
const vv=yv,ysub=vv.add(1).div(2),vrows={},vp={};
for(const[name,obj]of Object.entries(cleaned)){let r=new P();for(let j=0;j<obj.row.length;j++){const z=obj.row[j];r=r.add(ysub.pow(j).mul(new F(z.n.map(rq),z.d.map(rq))));}vp[name]=r;const degree=Math.max(...[...r.m.keys()].map(k=>+k.split(",")[1]));vrows[name]=Array.from({length:degree+1},(_,j)=>(r.m.get("0,"+j)||new F()).json());}
requireIt(vp.Rt.eq(vv.pow(2).add(1).pow(2).mul(uu.mul(vv.pow(3)).mul(new P(2).sub(vv)).mul(4).sub(vv.pow(2).add(1).pow(2))).div(16)),"actual factored Rt return");
function fromVU(data){const max=Math.max(...data.map(z=>z.n.length));let row=Array.from({length:max},()=>[]);for(let j=0;j<data.length;j++){requireIt(JSON.stringify(data[j].d)==='["1"]',"polynomial coefficient");for(let k=0;k<data[j].n.length;k++)row[k]=ka(row[k],Array(j).fill(q0).concat([rq(data[j].n[k])]));}return kt(row);}
const krrows=Object.fromEntries(Object.entries(vrows).map(([k,v])=>[k,fromVU(v)]));
let kg=krrows.N1;
const expectedN1=[[],[],[new Q(3,2),new Q(1,2)],[new Q(-1),q1]];
requireIt(kg.length===expectedN1.length&&kg.every((a,i)=>pe(a,expectedN1[i])),"original quadratic-fibre N1");
for(const name of ["NS","PS"])kg=kxgcd(kg,krrows[name]).g;
requireIt(kg.length===3&&!kg[0].length&&!kg[1].length&&pe(kg[2],[q1]),"whole quadratic-fibre gcd u^2");
function kvalpoly(row,x){let r=[];for(let i=row.length-1;i>=0;i--)r=ka(km(r,x),row[i]);return r;}
const kv=kvalpoly(krrows.NS,[new Q(1,2),q1]);
requireIt(pe(kv,[new Q(-109,64),new Q(787,64)]),"original quadratic-fibre trace return");
function ppow(a,n){let z=[q1];while(n){if(n&1)z=pm(z,a);a=pm(a,a);n>>=1;}return z;}
const AU=[0,0,0,8,-4].map(z=>new Q(z)),BU=[1,0,2,0,1].map(z=>new Q(z)),polys={};
for(const name of ["N1","NS","PS"]){let row=vrows[name],degree=Math.max(...row.map(z=>z.n.length-1)),co=Array.from({length:degree+1},()=>[]);for(let j=0;j<row.length;j++)for(let k=0;k<row[j].n.length;k++){while(co[k].length<=j)co[k].push(q0);co[k][j]=co[k][j].add(rq(row[j].n[k]));}let r=[];for(let k=0;k<=degree;k++)r=pa(r,pm(co[k],pm(ppow(BU,k),ppow(AU,degree-k))));polys[name]=tr(r);}
requireIt(polys.N1.length===21&&polys.NS.length===41&&polys.PS.length===41,"original univariate degree");
const gNS=pxgcd(polys.N1,polys.NS),gPS=pxgcd(gNS.g,polys.PS);
const expectedG=pm(Array(4).fill(q0).concat([q1]),ppow([q1,q0,q1],4));
requireIt(pe(gNS.g,expectedG)&&pe(gPS.g,expectedG),"full QQ gcd equals paid factors");
const result={
 kind:"ell=0 complete exclusion on Q=1-u",
 originalHomogeneousDegrees:{E1x:1,Rtx:2,N1x:2,NSx:3,PSx:3},
 originalRtFactor:"(v^2+1)^2*(4*u*v^3*(2-v)-(v^2+1)^2)/16",
 exceptionalQuadraticGcd:"u^2",
 exceptionalTraceAtUhalfPlusV:kv.map(z=>z.str()),
 exactQuotientCounts:{inverses:kinverses,divisions:kdivisions,bezouts:kbezouts},
 univariateOriginalDegrees:[20,40,40],
 fullQQgcd:gPS.g.map(z=>z.str()),
 fullQQBezoutDegrees:[gNS.s.length-1,gNS.t.length-1],
 parameterUnitsUsed:["u","u-1","2u-3"],
 scope:"Original general LS; no assertion about the remaining ell nonzero branch or ordinary ISP"
};
emit(result);return result;
})();
