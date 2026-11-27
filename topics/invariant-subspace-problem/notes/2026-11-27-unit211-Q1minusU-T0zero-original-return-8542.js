// Exact original Q=1-u, T0=0 return. Date: 2026-11-27 Asia/Taipei (UTC+8).
// No external files, packages, caches, random input, or floating algebra.
// Rational arithmetic uses BigInt; all finite-field products stay below 1009^2.
// The floating Date clock records elapsed time only.
function runCertificate(){
const start=Date.now();

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

const u=new P(new F([0,1])),ell=u.mul(2),x=variable(1),y=variable(2),t=variable(3),Qp=new P(1).sub(u);
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

function directH2Chart(pp){
 const Xh=u.add(y.sub(x.mul(y.sub(1))).div(2)),Th=u.mul(3).sub(1).add(new P(1).sub(u.mul(2)).mul(y)).add(x.mul(u.sub(y)));
 const maxT=Math.max(0,...[...pp.m.keys()].map(k=>+k.split(",")[3]));let row=new P();
 for(const[key,c]of pp.m){const e=key.split(",").map(Number);if(e[0])throw Error("ell was not actually specialized");row=row.add(Xh.pow(e[1]).mul(y.pow(e[2])).mul(Th.pow(e[3])).mul(u.pow(maxT-e[3])).mul(c));}return row;
}
function cleanH2Scalar(pp){let row=pp,hist=[];
for(const[name,pol]of [["u",[q0,q1]],["u-1",[new Q(-1),q1]],["2u-1",[new Q(-1),new Q(2)]],["4u-1",[new Q(-1),new Q(4)]]]){let n=0;
while(!row.is0()){const nxt=new Map();let okay=true;for(const[k,v]of row.m){if(v.q.length!==1||!v.q[0].eq(1))throw Error("polynomial denominator");const[q,r]=pd(v.p,pol);if(r.length){okay=false;break;}nxt.set(k,new F(q));}if(!okay)break;const rr=new P(nxt);if(!rr.mul(new F(pol)).eq(row))throw Error("scalar strip return");row=rr;n++;}
if(n)hist.push([name,n]);}return{row,hist};}
if(!directH2Chart(Ry0).is0())throw Error("actual Ry0 solve");
const h2OriginalRows={E:cleanH2Scalar(directH2Chart(E1.a)),R:cleanH2Scalar(directH2Chart(Rt0)),N1:cleanH2Scalar(directH2Chart(NH0.a)),NS:cleanH2Scalar(directH2Chart(NS0.a))};

function multivariateDivide(PP,VV){
 const order=[1,0,2,3],cmp=(a,b)=>{for(const j of order)if(a[j]!==b[j])return a[j]-b[j];return 0;};
 const lead=pp=>[...pp.m].map(([key,value])=>({key,e:key.split(",").map(Number),value})).sort((a,b)=>cmp(b.e,a.e))[0];
 const lv=lead(VV);if(!lv.value.eq(1))throw Error("multivariate divisor must have leading one");
 let pending=PP,quotient=new P(),remainder=new P();
 while(!pending.is0()){const lt=lead(pending);
 if(lt.e.every((a,j)=>a>=lv.e[j])){const e=lt.e.map((a,j)=>a-lv.e[j]),q=new P(new Map([[e.join(","),lt.value]]));quotient=quotient.add(q);pending=pending.sub(q.mul(VV));}
 else{const mon=new P(new Map([[lt.key,lt.value]]));remainder=remainder.add(mon);pending=pending.sub(mon);}}
 if(!quotient.mul(VV).add(remainder).eq(PP))throw Error("multivariate division return");
 return{q:quotient,r:remainder};
}

const ss=x,yy=y,DY=y.sub(1).mul(4),UN=x.mul(y.pow(2)).mul(4).add(new P(3).sub(x.mul(6)).sub(x.pow(2)).mul(y)).add(x.pow(2)).add(x).sub(2);
function substituteUHom(pp){
 let maxU=0;const polys=[];
 for(const[key,c]of pp.m){if(c.q.length!==1||!c.q[0].eq(1))throw Error("u polynomial required");maxU=Math.max(maxU,c.p.length-1);
 for(let j=0;j<c.p.length;j++)if(!c.p[j].is0())polys[j]=(polys[j]||new P()).add(new P(new Map([[key,new F(c.p[j])]])));}
 const up=Array.from({length:maxU+1},(_,i)=>UN.pow(i)),dp=Array.from({length:maxU+1},(_,i)=>DY.pow(i));let out=new P();
 for(let j=0;j<=maxU;j++)if(polys[j])out=out.add(polys[j].mul(up[j]).mul(dp[maxU-j]));return out;
}
function normalizeConstantLead(pp){const order=[1,0,2,3],cmp=(a,b)=>{for(const j of order)if(a[j]!==b[j])return a[j]-b[j];return 0;},ls=[...pp.m].map(([k,v])=>({e:k.split(",").map(Number),v})).sort((a,b)=>cmp(b.e,a.e));const c=ls[0].v;if(c.p.length!==1||c.q.length!==1)throw Error("constant leading needed");return pp.div(c);}
const unitList=[["y-1",y.sub(1)],["s",x],["u",UN],["u-1",UN.sub(DY)],["2u-1",UN.mul(2).sub(DY)],["4u-1",UN.mul(4).sub(DY)]];
function cleanH2Mean(pp){let row=pp,hist=[];for(const[name,vv]of unitList){const v=normalizeConstantLead(vv);let n=0;while(!row.is0()){const z=multivariateDivide(row,v);if(!z.r.is0())break;row=z.q;n++;}if(n)hist.push([name,n]);}return {row,hist};}

const abs=z=>z<0n?-z:z;
function imod(a,p){a%=p;return a<0?a+p:a;}
function ipow(a,n,p){let r=1;while(n){if(n&1)r=r*a%p;a=a*a%p;n=Math.floor(n/2);}return r;}
function iinv(a,p){a=imod(a,p);if(!a)throw Error("zero mod inverse");let v=ipow(a,p-2,p);if(v*a%p!==1)throw Error("inverse multiply");return v;}
function isprime(n){if(n<2)return false;for(let d=2;d*d<=n;d++)if(n%d===0)return false;return true;}
function integerRows(data){let a=data.map(z=>{if(z.d.length!==1||z.d[0]!=="1")throw Error("row denominator");return z.n.map(rq);}),s=1n;for(let p of a)for(let c of p)s=s/gg(s,c.d)*c.d;return{a:a.map(p=>p.map(c=>c.n*(s/c.d))),s};}
function eva(p,u,mod){let r=0;for(let i=p.length-1;i>=0;i--)r=(r*u+Number((p[i]%BigInt(mod)+BigInt(mod))%BigInt(mod)))%mod;return r;}
function detmod(a,p){a=a.map(z=>z.slice());let r=1,n=a.length;for(let j=0;j<n;j++){let k=j;while(k<n&&!a[k][j])k++;if(k===n)return 0;if(k!==j){[a[k],a[j]]=[a[j],a[k]];r=imod(-r,p);}let piv=a[j][j],iv=iinv(piv,p);r=r*piv%p;for(let i=j+1;i<n;i++){let c=a[i][j]*iv%p;if(c)for(let l=j;l<n;l++)a[i][l]=imod(a[i][l]-c*a[j][l],p);}}return r;}
function sylv(A,B,u,p){let a=A.map(z=>eva(z,u,p)),b=B.map(z=>eva(z,u,p)),m=a.length-1,n=b.length-1,N=m+n,mat=Array.from({length:N},()=>Array(N).fill(0));for(let i=0;i<n;i++)for(let j=0;j<=m;j++)mat[i][i+j]=a[m-j];for(let i=0;i<m;i++)for(let j=0;j<=n;j++)mat[n+i][i+j]=b[n-j];return detmod(mat,p);}
function interpolate(vals,p){let dif=[],v=vals.slice();while(v.length){dif.push(v[0]);v=v.slice(1).map((z,i)=>imod(z-v[i],p));}let D=vals.length-1,out=Array(D+1).fill(0),base=[1],fact=1;for(let k=0;k<=D;k++){let c=dif[k]*iinv(fact,p)%p;for(let j=0;j<base.length;j++)out[j]=(out[j]+c*base[j])%p;let nb=Array(base.length+1).fill(0);for(let j=0;j<base.length;j++){nb[j]=imod(nb[j]-k*base[j],p);nb[j+1]=(nb[j+1]+base[j])%p;}base=nb;fact=fact*(k+1)%p;}for(let x=0;x<=D;x++){let r=0;for(let j=D;j>=0;j--)r=(r*x+out[j])%p;if(r!==vals[x])throw Error("interpolation return");}return out;}
function crtRes(A,B){let m=A.length-1,n=B.length-1,da=Math.max(...A.map(p=>p.length-1)),db=Math.max(...B.map(p=>p.length-1)),D=n*da+m*db,la=A.flat().reduce((s,z)=>s+abs(z),0n),lb=B.flat().reduce((s,z)=>s+abs(z),0n),bound=la**BigInt(n)*lb**BigInt(m),M=1n,v=Array(D+1).fill(0n),primes=[],p=Math.max(101,D+1);while(M<=2n*bound){while(!isprime(p))p++;let vals=Array.from({length:D+1},(_,i)=>sylv(A,B,i,p)),ar=interpolate(vals,p),pB=BigInt(p),iv=BigInt(iinv(Number(M%pB),p));for(let j=0;j<=D;j++){let delta=(BigInt(ar[j])-v[j]%pB+pB)%pB;v[j]+=M*(delta*iv%pB);if(v[j]%pB!==BigInt(ar[j]))throw Error("CRT return");}M*=pB;primes.push(p);p++;}v=v.map(z=>z*2n>M?z-M:z);for(let z of v)if(abs(z)>bound)throw Error("coefficient bound");while(v.length&&v[v.length-1]===0n)v.pop();return{coeff:v.map(String),bound:String(bound),modulus:String(M),primes,degreeBound:D,degree:v.length-1};}

function mt(a){a=a.slice();while(a.length&&a[a.length-1]===0)a.pop();return a;}
function ma(a,b,p){let v=[];for(let i=0;i<Math.max(a.length,b.length);i++)v.push(((a[i]||0)+(b[i]||0))%p);return mt(v);}
function ms(a,b,p){let v=[];for(let i=0;i<Math.max(a.length,b.length);i++)v.push(imod((a[i]||0)-(b[i]||0),p));return mt(v);}
function mm(a,b,p){if(!a.length||!b.length)return [];let v=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)v[i+j]=(v[i+j]+a[i]*b[j])%p;return mt(v);}
function md(a,b,p){let r=a.slice(),q=Array(Math.max(0,a.length-b.length+1)).fill(0),iv=iinv(b[b.length-1],p);while(r.length>=b.length&&r.length){let j=r.length-b.length,c=r[r.length-1]*iv%p;q[j]=(q[j]+c)%p;for(let k=0;k<b.length;k++)r[j+k]=imod(r[j+k]-c*b[k],p);r=mt(r);}let ret=ma(mm(q,b,p),r,p);if(ret.length!==a.length||ret.some((z,i)=>z!==a[i]))throw Error("mod division return");return {q:mt(q),r};}
function mg(a,b,p){while(b.length){let r=md(a,b,p).r;a=b;b=r;}if(!a.length)return a;let iv=iinv(a[a.length-1],p);return a.map(z=>z*iv%p);}
function mxgcd(a,b,p){let A=a.slice(),B=b.slice(),s0=[1],s1=[],t0=[],t1=[1];while(B.length){let z=md(A,B,p);A=B;B=z.r;[s0,s1]=[s1,ms(s0,mm(z.q,s1,p),p)];[t0,t1]=[t1,ms(t0,mm(z.q,t1,p),p)];}let iv=iinv(A[A.length-1],p);A=A.map(z=>z*iv%p);s0=s0.map(z=>z*iv%p);t0=t0.map(z=>z*iv%p);let ret=ma(mm(s0,a,p),mm(t0,b,p),p);if(ret.length!==A.length||ret.some((z,i)=>z!==A[i]))throw Error("mod Bezout return");return{g:A,s:s0,t:t0};}
function reduceZ(A,p){return mt(A.map(v=>Number((v%BigInt(p)+BigInt(p))%BigInt(p))));}

function rq(z){const[a,b]=z.split("/");return new Q(BigInt(a),b?BigInt(b):1n);}
function primitiveActual(row){let den=1n;
 for(const f of row.m.values()){if(f.p.length!==1||f.q.length!==1||!f.q[0].eq(1))throw Error("constant QQ coefficients required");den=den/gg(den,f.p[0].d)*f.p[0].d;}
 let num=0n;for(const f of row.m.values())num=gg(num,f.p[0].n*(den/f.p[0].d));const first=[...row.m].map(([k,v])=>({e:k.split(",").map(Number),v})).sort((a,b)=>a.e[1]-b.e[1]||a.e[2]-b.e[2]||a.e[0]-b.e[0]||a.e[3]-b.e[3])[0];if(first.v.p[0].n<0n)num=-num;const scalar=new Q(num,den),out=row.div(new F(scalar));if(!out.mul(new F(scalar)).eq(row))throw Error("primitive exact return");return{row:out,scalar:scalar.str()};
}
function rowInS(pp){const d=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[1])),rows=Array.from({length:d+1},()=>[]);
for(const[key,c]of pp.m){const e=key.split(",").map(Number);if(e[0]||e[3]||c.p.length!==1||c.q.length!==1||!c.q[0].eq(1))throw Error("QQ[y,s] row");let a=rows[e[1]];while(a.length<=e[2])a.push(q0);a[e[2]]=a[e[2]].add(c.p[0]);}return rows.map(a=>({n:tr(a).map(z=>z.str()),d:["1"]}));}
function fromRows(rows){let out=new P();for(let i=0;i<rows.length;i++)for(let j=0;j<rows[i].n.length;j++)out=out.add(x.pow(i).mul(y.pow(j)).mul(new F(rq(rows[i].n[j]))));return out;}
const eclean=x.mul(y.pow(2)).mul(4).add(new P(3).sub(u.mul(4)).sub(x.mul(6)).sub(x.pow(2)).mul(y)).add(u.mul(4)).sub(2).add(x).add(x.pow(2));
if(!h2OriginalRows.E.row.mul(2).eq(eclean))throw Error("original E exact low-degree formula");
if(!substituteUHom(h2OriginalRows.E.row).is0())throw Error("full original E u recovery");
if(!Lnum.eq(P02.mul(y.add(t.div(4))))||!Tnum.eq(P02.mul(t.mul(3).div(4).sub(u.mul(2)))))throw Error("actual original lambda and T");
const transformed={},hist={};for(const key of ["R","N1","NS"]){const c=cleanH2Mean(substituteUHom(h2OriginalRows[key].row)),pr=primitiveActual(c.row);transformed[key]=pr.row;hist[key]={scalar:h2OriginalRows[key].hist,uRecovery:c.hist,primitive:pr.scalar};}
const rb=[
 {n:["2","-5","6","-4"],d:["1"]},
 {n:["-3","14","-22","20","-8"],d:["1"]},
 {n:["-1","1"],d:["1"]}],
 nb=[
 {n:["0","2","-6","4"],d:["1"]},
 {n:["-2","8","-1","-14","8"],d:["1"]},
 {n:["0","-12","37","-32","8"],d:["1"]},
 {n:["3","-14","17","-6"],d:["1"]},
 {n:["1","-2","1"],d:["1"]}];
const g=x.add(1).sub(y.mul(2)),Rbar=fromRows(rb),Nbar=fromRows(nb);
if(!transformed.R.eq(g.mul(Rbar))||!transformed.N1.eq(g.mul(Nbar)))throw Error("original R/N exact common-curve factors");
const v=y.mul(2).sub(1),uCurve=v.pow(2).add(1).div(4);
if(!substitute(UN,1,v).eq(DY.mul(uCurve)))throw Error("common curve exact u");
const sx=x,Xc=x.add(1).div(2),Uc=x.pow(2).add(1).div(4),
 Xchart=Uc.add(Xc.sub(x.mul(Xc.sub(1))).div(2)),
 Tchart=Uc.mul(3).sub(1).add(new P(1).sub(Uc.mul(2)).mul(Xc)).add(x.mul(Uc.sub(Xc)));
if(!Xchart.eq(Xc)||!Tchart.is0())throw Error("common curve actual x and t");
const Dcurve=Uc.mul(2).mul(Xc.pow(2).mul(2).sub(Xc.mul(2)).add(1)).sub(Uc.pow(2).mul(4));
if(!Dcurve.is0())throw Error("common curve physical Dval");
const cr=crtRes(integerRows(rb).a,integerRows(nb).a),ym1=[new Q(-1),q1],qa=[q1,new Q(-2),new Q(2)],qb=[q1,new Q(-6),new Q(4)];let prod=[new Q(-16)];
for(let i=0;i<6;i++){prod=pm(prod,ym1);prod=pm(prod,qa);}prod=pm(prod,qb);
if(!pe(prod,cr.coeff.map(rq)))throw Error("full QQ resultant factorization multiplyback");
const Ap=y.pow(2).mul(2).sub(y.mul(2)).add(1),corr=new P(3).sub(y.mul(4)).add(x.mul(new P(-1).add(y.mul(6)).sub(y.pow(2).mul(4))));
if(!Rbar.sub(y.sub(1).mul(g.pow(2))).eq(Ap.mul(corr)))throw Error("whole A fiber exact square identity");
const NSrow=rowInS(transformed.NS),rr=integerRows(rb).a,nsIntRows=integerRows(NSrow).a,pmod=1009,
 degreeBound=(nsIntRows.length-1)*Math.max(...rr.map(a=>a.length-1))+(rr.length-1)*Math.max(...nsIntRows.map(a=>a.length-1)),
 values=Array.from({length:degreeBound+1},(_,i)=>sylv(rr,nsIntRows,i,pmod)),projection=mt(interpolate(values,pmod)),
 bz=mxgcd([1,pmod-6,4],projection,pmod);
if(bz.g.length!==1||bz.g[0]!==1)throw Error("actual original NS Gauss return");
return {input:"original Gram and E0/N0/P1; Q=1-u, ell=2u",units:["u","1-u","4u-1","y-1"],trace:hist,
 meanFormula:"4*s*y^2+(3-4*u-6*s-s^2)*y+4*u-2+s+s^2",
 commonCurve:"s+1-2*y; exact original Dval=0",
 residualSylvester:{size:6,...cr,factorization:"-16*(y-1)^6*(2*y^2-2*y+1)^6*(4*y^2-6*y+1)"},
 wholeQuadraticFiber:"Rbar=(y-1)*(s+1-2*y)^2+(2*y^2-2*y+1)*(3-4*y+(-1+6*y-4*y^2)*s)",
 originalNS:{sDegree:nsIntRows.length-1,yDegree:Math.max(...nsIntRows.map(a=>a.length-1)),fixedSylvesterSize:rr.length+nsIntRows.length-2,degreeBound,modulus:pmod,degree:projection.length-1,coverDegree:2,coverLeading:4,projection,bezout:bz},
 conclusion:"Q=1-u, T0=0 has no original admissible LS solution in the already paid chart",elapsedMs:Date.now()-start};

}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module){console.log(JSON.stringify(runCertificate()));}
