/* Self-contained reconstruction of the actually completed segmented exact returns.
 * R150 / Q=1-u / u=Q=1/2, 2026-11-27 Asia/Taipei.
 * BigInt QQ arithmetic; no external library, cache or numerical root finding.
 * The individual construction, fixed-degree CRT, exact factor division,
 * three-polynomial modular Bezout and original rational-fibre returns were
 * executed in V8. This assembled file has NOT been executed end-to-end.
 * Run with Node.js or another ES2022 engine; only console.log is required.
 */
(function(){
"use strict";
const emit=v=>console.log(JSON.stringify(v));
function rq(s){let[a,b]=s.split("/");return new Q(BigInt(a),b?BigInt(b):1n);}

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
const u=new P(new F(1).div(2)),ell=new P(new F([0,1])),Qp=new P(1).sub(u);
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

function pfrom(data){return new P(new Map(data.map(z=>[z.e.join(","),new F(z.n.map(rq),z.d.map(rq))])));}
function xc(pp,i){return new P(new Map([...pp.m].filter(([k,v])=>Number(k.split(",")[0])===i).map(([k,v])=>["0,"+k.split(",")[1],v])));}
function detP(a){if(a.length===1)return a[0][0];let r=new P();for(let j=0;j<a.length;j++){let b=a.slice(1).map(row=>row.filter((_,k)=>k!==j)),v=a[0][j].mul(detP(b));r=j%2?r.sub(v):r.add(v);}return r;}
function halfPaid(a){a=a.slice();let hist=[];for(let[nm,p]of [["ell-2",[new Q(-2),q1]],["2ell2-4ell+1",[q1,new Q(-4),new Q(2)]]]){let n=0;while(a.length>1){let g=pg(a,p);if(g.length<2)break;let z=pd(a,g);if(z[1].length)throw Error("half unit division");a=z[0];n++;}if(n)hist.push([nm,n]);}return{rest:a,hist};}
function cleanHalf(pp){if([...pp.m.keys()].some(k=>!k.startsWith("0,")))throw Error("not y");let deg=Math.max(...[...pp.m.keys()].map(k=>Number(k.split(",")[1]))),ar=Array.from({length:deg+1},()=>new F());for(let[k,v]of pp.m)ar[Number(k.split(",")[1])]=v;let den=[q1];for(let c of ar){let z=pd(pm(den,c.q),pg(den,c.q));if(z[1].length)throw Error("lcm");den=z[0];}if(halfPaid(den).rest.length>1)throw Error("unpaid denominator");let nums=ar.map(c=>pm(c.p,pd(den,c.q)[0])),content=[];for(let p of nums)content=pg(content,p);let unpaid=halfPaid(content).rest,paid=pd(content,unpaid)[0];nums=nums.map(p=>{let z=pd(p,paid);if(z[1].length)throw Error("content return");return z[0];});let count=0;while(nums.length>1){let q=Array.from({length:nums.length-1},()=>[]);q[q.length-1]=nums[nums.length-1];for(let j=nums.length-2;j>=1;j--)q[j-1]=pa(nums[j],q[j]);let rem=pa(nums[0],q[0]);if(rem.length)break;nums=q;count++;}return{row:nums.map(p=>new F(p).json()),den:den.map(z=>z.str()),paidContent:paid.map(z=>z.str()),unpaidContent:unpaid.map(z=>z.str()),y1Removed:count};}

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
function zt(a){a=a.slice();while(a.length&&a.at(-1)===0n)a.pop();return a;}

function zdiv(A,B){let r=A.slice(),q=Array(Math.max(0,A.length-B.length+1)).fill(0n);while(r.length>=B.length&&r.length){let j=r.length-B.length;if(r[r.length-1]%B[B.length-1]!==0n)return null;let c=r[r.length-1]/B[B.length-1];q[j]+=c;for(let k=0;k<B.length;k++)r[j+k]-=c*B[k];r=zt(r);}return {q:zt(q),r};}
function zmul(a,b){if(!a.length||!b.length)return [];let z=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]+=a[i]*b[j];return zt(z);}

function sameJSON(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function requireIt(v,m){if(!v)throw Error(m);}
const at=[0,1,2,3].map(makeAtT), coefficients={};
const degrees={E1:1,Rt:2,Ry:1,N1:2,NS:3,PS:3};
for(const name of Object.keys(degrees)){
  const [a,b,c,d]=at.map(z=>z[name]);
  const cs=[a,a.mul(-11).add(b.mul(18)).sub(c.mul(9)).add(d.mul(2)).div(6),
    a.mul(2).sub(b.mul(5)).add(c.mul(4)).sub(d).div(2),
    a.neg().add(b.mul(3)).sub(c.mul(3)).add(d).div(6)];
  for(let k=0;k<4;k++){let r=new P();for(let j=0;j<4;j++)r=r.add(cs[j].mul(k**j));requireIt(r.eq(at[k][name]),"cubic interpolation return");}
  for(let j=degrees[name]+1;j<4;j++)requireIt(cs[j].is0(),"original t degree");
  coefficients[name]=cs.slice(0,degrees[name]+1);
}
const yvar=new P(new Map([["0,1",new F(1)]])), AA=coefficients.Ry[0].neg(),BB=yvar.sub(1).div(2);
requireIt(coefficients.Ry[1].eq(BB),"actual Ry t coefficient");
const hrows={};
for(const name of ["E1","Rt","N1","NS","PS"]){
 let r=new P(),n=degrees[name];
 for(let j=0;j<=n;j++)r=r.add(coefficients[name][j].mul(AA.pow(j)).mul(BB.pow(n-j)));
 hrows[name]=r;
}
const {E1,Rt,N1,NS,PS}=hrows;
const vec=(r,shift=0)=>[3,2,1,0].map(i=>xc(r,i-shift));
const minors={
 C:cleanHalf(detP([E1,Rt,N1].map(r=>[2,1,0].map(i=>xc(r,i))))),
 N:cleanHalf(detP([vec(E1,1),vec(E1),vec(Rt),vec(NS)])),
 P:cleanHalf(detP([vec(E1,1),vec(E1),vec(Rt),vec(PS)])),
 A:cleanHalf(detP([vec(E1,1),vec(E1),vec(N1),vec(NS)]))
};
const ints=Object.fromEntries(Object.entries(minors).map(([k,v])=>[k,integerRows(v.row).a]));
for(const [nm,yd,pd0]of [["C",6,9],["N",9,15],["P",9,17],["A",9,18]]){
 requireIt(ints[nm].length-1===yd,"minor y degree");
 requireIt(Math.max(...ints[nm].map(p=>p.length-1))===pd0,"minor parameter degree");
 requireIt(minors[nm].y1Removed===2,"paid y-1 multiplicity");
}
const RN=crtRes(ints.C,ints.N),RP=crtRes(ints.C,ints.P);
requireIt(RN.degree===158&&RN.degreeBound===171,"full N resultant degree");
requireIt(RP.degree===170&&RP.degreeBound===183,"full P resultant degree");
requireIt(BigInt(RP.coeff[0])!==0n,"ell=0 original P return");
function strip(A,fs){
 let r=A.map(BigInt),rebuild=[1n],history=[];
 for(const[name,p,expected]of fs){let count=0;for(;;){
   const z=zdiv(r,p);if(!z||z.r.length)break;
   requireIt(sameJSON(zmul(z.q,p).map(String),r.map(String)),"QQ factor multiplication");
   r=z.q;rebuild=zmul(rebuild,p);count++;
 }
 requireIt(count===expected,"actual QQ factor exponent "+name);history.push([name,count]);}
 requireIt(sameJSON(zmul(r,rebuild).map(String),A),"complete factor multiplication");
 return{r,history};
}
const factorsN=[["M",[1n,-4n,2n],19],["ell",[0n,1n],6],["2ell-1",[-1n,2n],6],["ell-1",[-1n,1n],4]];
const factorsP=[["M",[1n,-4n,2n],24],["2ell-1",[-1n,2n],6],["ell-1",[-1n,1n],4]];
const sn=strip(RN.coeff,factorsN),sp=strip(RP.coeff,factorsP),prime=1009;
const qn=reduceZ(sn.r,prime),qp=reduceZ(sp.r,prime);
requireIt(qn.length===105&&qp.length===113,"1009 degree-preserving QQ covers");
const first=mxgcd(qn,qp,prime);requireIt(first.g.length===15,"first modular common factor");
const boundA=(ints.A.length-1)*Math.max(...ints.C.map(p=>p.length-1))+(ints.C.length-1)*Math.max(...ints.A.map(p=>p.length-1));
requireIt(boundA===189,"fixed full Sylvester degree bound");
const valuesA=Array.from({length:boundA+1},(_,u)=>sylv(ints.C,ints.A,u,prime));
const projectedA=mt(interpolate(valuesA,prime));requireIt(projectedA.length===178,"original full modular projection degree");
const second=mxgcd(first.g,projectedA,prime);
requireIt(sameJSON(second.g,[1]),"three original projections are coprime");
const ss=mm(second.s,first.s,prime),tt=mm(second.s,first.t,prime),vv=second.t;
requireIt(sameJSON(ma(ma(mm(ss,qn,prime),mm(tt,qp,prime),prime),mm(vv,projectedA,prime),prime),[1]),"complete three-term Bezout");
function smallScalarReturn(){
const u=new P(new F(1).div(2)),ell=new P(new F(1).div(2)),Qp=new P(1).sub(u);
const zz=new F([0,1]),x=new P(zz.pow(2).sub(zz).add(new F(3).div(2)).div(2)),y=new P(zz.add(1).add(new F(1).div(zz.mul(2))).div(2));
const t=new P(zz.add(new F(1).div(zz.mul(2))).mul(zz.mul(2).sub(1)));
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
if(!Ry.is0())throw Error("Ry must vanish");

const er=E1.a.m.get("0,0"),nr=NH.a.m.get("0,0");
const expectedE=new F([new Q(-5,16),q0,new Q(-1,2),q0,new Q(1,4)]);
const expectedN=new F([new Q(1,96),new Q(1,32),new Q(1,8),new Q(-1,24),new Q(5,24),new Q(-5,24),new Q(1,12)],[q0,q0,q1]);
requireIt(er.eq(expectedE)&&nr.eq(expectedN),"original rational-fibre E1 and N1");
requireIt(pe(pg(er.p,nr.p),[q1]),"original rational-fibre QQ gcd");
return{E1:er.json(),N1:nr.json()};
}
const scalar=smallScalarReturn();
emit({
 kind:"Q1minusU_uHalf_completed_original_returns",
 fullResultants:[{degree:RN.degree,bound:RN.degreeBound,primes:RN.primes.length},{degree:RP.degree,bound:RP.degreeBound,primes:RP.primes.length}],
 exactDivisions:[sn.history,sp.history],
 remainingDegrees:[qn.length-1,qp.length-1],
 prime,remainingLeading:[qn.at(-1),qp.at(-1)],
 firstGcdDegree:first.g.length-1,originalThirdDegree:projectedA.length-1,
 tripleBezoutDegrees:[ss.length-1,tt.length-1,vv.length-1],
 rationalFibre:scalar
});
})();
