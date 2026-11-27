/* Exact original R150 Q=1-u mean-leading s=0 return.
 * 2026-11-27 Asia/Taipei. Only BigInt rational arithmetic and certified CRT.
 * Complete original reconstruction; no external file, cache, or library.
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

function polyDivideMonicParameter(PP,VV,index=0){
 let rr=PP,qq=new P(),d=Math.max(...[...VV.m.keys()].map(k=>+k.split(",")[index])),ld=coeff(VV,index,d);
 if(ld.m.size!==1||!ld.m.has(ZK))throw Error("parameter leading nonscalar");
 while(!rr.is0()){let deg=Math.max(...[...rr.m.keys()].map(k=>+k.split(",")[index]));if(deg<d)break;
 let lead=coeff(rr,index,deg).div(ld),step=lead.mul(variable(index).pow(deg-d));qq=qq.add(step);rr=rr.sub(step.mul(VV));}
 if(!qq.mul(VV).add(rr).eq(PP))throw Error("parameter division return");return{q:qq,r:rr};
}

function scalarUnitStrip(pp){let row=pp,hist=[];for(const[nm,pf]of [["u",[q0,q1]],["u-1",[new Q(-1),q1]],["2u-1",[new Q(-1),new Q(2)]]]){let best=Infinity;for(const cf of row.m.values()){let a=cf.p,n=0;while(a.length){const z=pd(a,pf);if(z[1].length)break;a=z[0];n++;}let b=cf.q;while(b.length){const z=pd(b,pf);if(z[1].length)break;b=z[0];n--;}best=Math.min(best,n);}if(best>0&&Number.isFinite(best)){row=row.div(new F(pf).pow(best));hist.push([nm,best]);}}return{row,hist};}
const m=ell.pow(2).mul(u.sub(1)).add(ell.mul(2)).sub(1),Hh=u.mul(2).sub(1).mul(ell).add(1),Jm=new P(1).sub(u.mul(2).sub(1).mul(ell)),P0h=u.mul(3).sub(2).mul(ell).sub(u.mul(2)).add(3);
function cleanSZ(pp){let row=pp,hist=[];for(const[nm,div]of [["h",ell],["m",m],["Hh",Hh],["Jminus",Jm],["P0h",P0h]]){let n=0;while(!row.is0()){const z=polyDivideMonicParameter(row,div);if(!z.r.is0())break;row=z.q;n++;}if(n)hist.push([nm,n]);}const s=scalarUnitStrip(row);return{row:s.row,hist:hist.concat(s.hist)};}

function directSZeroGrouped(pp){
 const XN=u.mul(ell).add(ell.sub(1).mul(y)),TN=ell.mul(u.mul(3).sub(1)).add(Qp.mul(ell).sub(1).mul(y).mul(2));
 const dx=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[1])),dt=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[3]));
 const groups=new Map();
 for(const[key,cf]of pp.m){const e=key.split(",").map(Number),gkey=[e[1],e[2],e[3]].join(","),part=u.mul(ell).pow(e[0]).mul(cf);groups.set(gkey,(groups.get(gkey)||new P()).add(part));}
 const xp=Array.from({length:dx+1},(_,i)=>XN.pow(i)),tp=Array.from({length:dt+1},(_,i)=>TN.pow(i));
 let res=new P();for(const[key,param]of groups){const e=key.split(",").map(Number);res=res.add(param.mul(xp[e[0]]).mul(y.pow(e[1])).mul(tp[e[2]]).mul(ell.pow(dx-e[0])).mul(u.mul(ell).pow(dt-e[2])));}
 return cleanSZ(res);
}

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

function zg(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let c=a%b;a=b;b=c;}return a;}
function zt(p){p=p.slice();while(p.length&&p[p.length-1]===0n)p.pop();return p;}
function zprim(p){p=zt(p);if(!p.length)return p;let g=0n;for(let c of p)g=zg(g,c);if(p[p.length-1]<0n)g=-g;let q=p.map(c=>c/g);if(q.some((c,i)=>c*g!==p[i]))throw Error("primitive return");return q;}
function zrem(A,B){let r=A.slice(),steps=0;while(r.length>=B.length&&r.length){let j=r.length-B.length,a=r[r.length-1],b=B[B.length-1],n=r.map(c=>c*b);for(let k=0;k<B.length;k++)n[j+k]-=a*B[k];n=zt(n);if(n.length>=r.length)throw Error("degree did not drop");r=zprim(n);steps++;}return {r,steps};}
function zgcd(A,B){let a=zprim(A),b=zprim(B),trace=[];while(b.length){let z=zrem(a,b);trace.push({a:a.length-1,b:b.length-1,r:z.r.length-1,steps:z.steps});a=b;b=z.r;}return {g:zprim(a),trace};}

function zdiv(A,B){let r=A.slice(),q=Array(Math.max(0,A.length-B.length+1)).fill(0n);while(r.length>=B.length&&r.length){let j=r.length-B.length;if(r[r.length-1]%B[B.length-1]!==0n)return null;let c=r[r.length-1]/B[B.length-1];q[j]+=c;for(let k=0;k<B.length;k++)r[j+k]-=c*B[k];r=zt(r);}return {q:zt(q),r};}
function zmul(a,b){if(!a.length||!b.length)return [];let z=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]+=a[i]*b[j];return zt(z);}

function pxgcd(a,b){let A=a.slice(),B=b.slice(),s0=[q1],s1=[],t0=[],t1=[q1];while(B.length){let [q,r]=pd(A,B);if(!pe(pa(pm(q,B),r),A))throw Error("QQ division");A=B;B=r;[s0,s1]=[s1,ps(s0,pm(q,s1))];[t0,t1]=[t1,ps(t0,pm(q,t1))];}if(!A.length)return {g:[],s:[],t:[]};let k=q1.div(A[A.length-1]);A=pc(A,k);s0=pc(s0,k);t0=pc(t0,k);if(!pe(pa(pm(s0,a),pm(t0,b)),A))throw Error("QQ Bezout return");return {g:A,s:s0,t:t0};}
const phi=[new Q(-1),new Q(-1),new Q(4)];
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
function rq(s){let[a,b]=s.split("/");return new Q(BigInt(a),b?BigInt(b):1n);}
const initial={};
for(const[name,pp]of [["E",E1.a],["R",Rt0],["N1",NH0.a],["NS",NS0.a]])initial[name]=directSZeroGrouped(pp);
const EE=initial.E.row,ay=coeff(EE,2,1),by=coeff(EE,2,0);
requireIt(ay.eq(m.mul(Jm)),"E1 linear y leading");
requireIt(by.eq(ell.mul(new P(-1).add(u.mul(ell).mul(2)).add(u.sub(1).mul(u.mul(4).sub(1)).mul(ell.pow(2)).div(2)))),"E1 constant");
const par={};
for(const name of ["R","N1","NS"]){const rr=initial[name].row,n=Math.max(...[...rr.m.keys()].map(k=>+k.split(",")[2]));let result=new P();for(let j=0;j<=n;j++)result=result.add(coeff(rr,2,j).mul(by.neg().pow(j)).mul(ay.pow(n-j)));par[name]=cleanSZ(result).row;}
function kvF(c){return km(kr(c.p),ki(kr(c.q)));}
function evaluateHUtoKY(pp,hval){const n=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[2])),r=Array.from({length:n+1},()=>[]);for(const[key,c]of pp.m){const e=key.split(",").map(Number);r[e[2]]=ka(r[e[2]],km(kvF(c),kp(hval,e[0])));}return kt(r);}
const hCritical=ki([new Q(-1),new Q(2)]),rCritical=evaluateHUtoKY(initial.R.row,hCritical),nCritical=evaluateHUtoKY(initial.N1.row,hCritical),jreturn=kxgcd(rCritical,nCritical);
requireIt(jreturn.g.length===1&&pe(jreturn.g[0],[q1]),"whole Jminus zero quadratic fibre");

const gh=u.mul(ell).mul(2).sub(1),residual={};
for(const name of ["R","N1"]){const z=polyDivideMonicParameter(par[name],gh);requireIt(z.r.is0(),"actual QQ common factor division");requireIt(!polyDivideMonicParameter(z.q,gh).r.is0(),"common factor exponent one");residual[name]=z.q;}
function specializeOriginal(pp){for(const[i,value]of [[0,new P(new F(1).div(2))],[1,new P(new F(1).div(2))],[2,new P(new F(1).div(2))],[3,new P(0)]])pp=substitute(pp,i,value);return pp;}
for(const z of rows[1])requireIt(specializeOriginal(z.a).is0()&&specializeOriginal(z.b).is0(),"ell half original germ row zero");
requireIt(specializeOriginal(Lnum.sub(P02.div(2))).is0(),"ell half lambda");
requireIt(specializeOriginal(Tnum.add(P02.div(2))).is0(),"ell half T");
requireIt(specializeOriginal(ell.mul(Lnum.pow(2).mul(2).sub(Lnum.mul(P02).mul(2)).add(P02.pow(2))).sub(Tnum.pow(2))).is0(),"ell half original value variance");
const hHalf=new P(new F(1).div(new F([0,2])));
const Ehalf=substitute(EE,0,hHalf),mhalf=substitute(m,0,hHalf);
requireIt(Ehalf.eq(mhalf.div(u.mul(2)).mul(y.sub(new F(1).div(2)))),"half weight original mean point");

function integerHRow(pp){const n=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[0])),row=Array.from({length:n+1},()=>({n:[],d:["1"]}));for(const[key,c]of pp.m){const e=key.split(",").map(Number);requireIt(e.slice(1).every(j=>j===0),"parameter polynomial");row[e[0]]=c.json();}return integerRows(row).a;}
const ir=integerHRow(residual.R),in1=integerHRow(residual.N1),cover=crtRes(ir,in1);
requireIt(cover.degree===31&&cover.degreeBound===40,"full exact parameter cover");
let remainder=cover.coeff.map(BigInt),product=[1n],factorHistory=[];
for(const[name,fac,expected]of [["u",[0n,1n],7],["u-1",[-1n,1n],2],["4u-1",[-1n,4n],3],["3u-1",[-1n,3n],2],["4u2-u-1",[-1n,-1n,4n],4]]){let count=0;for(;;){let z=zdiv(remainder,fac);if(!z||z.r.length)break;requireIt(JSON.stringify(zmul(z.q,fac).map(String))===JSON.stringify(remainder.map(String)),"factor multiply back");remainder=z.q;product=zmul(product,fac);count++;}requireIt(count===expected,"factor multiplicity "+name);factorHistory.push([name,count]);}
requireIt(JSON.stringify(zmul(remainder,product).map(String))===JSON.stringify(cover.coeff),"complete QQ factor multiply back");
requireIt(remainder.length===10,"degree nine exact remainder");

function qeval(p,a){let r=q0;for(let i=p.length-1;i>=0;i--)r=r.mul(a).add(p[i]);return r;}
function qHRow(pp,a){const n=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[0])),row=Array.from({length:n+1},()=>q0);for(const[key,c]of pp.m){row[+key.split(",")[0]]=qeval(c.p,a).div(qeval(c.q,a));}return tr(row);}
for(const[uv,constant]of [[new Q(1,4),new Q(-2)],[new Q(1,3),new Q(-3)]]){const g=pxgcd(qHRow(residual.R,uv),qHRow(residual.N1,uv)).g;requireIt(pe(g,[constant,q1]),"original rational parameter fibre");}
function kHRow(pp){const n=Math.max(...[...pp.m.keys()].map(k=>+k.split(",")[0])),row=Array.from({length:n+1},()=>[]);for(const[key,c]of pp.m)row[+key.split(",")[0]]=kvF(c);return kt(row);}
const qreturn=kxgcd(kHRow(residual.R),kHRow(residual.N1));
const expectedQuad=[[new Q(5),new Q(12)],[new Q(-2),new Q(-8)],[q1]];
requireIt(qreturn.g.length===3&&qreturn.g.every((c,i)=>pe(c,expectedQuad[i])),"whole quadratic parameter fibre");
requireIt(pe(km([new Q(-1),new Q(2)],[q1,new Q(4)]),[q1]),"quadratic fibre equals paid Jminus zero");

const is=integerHRow(par.NS),prior=(ir.length-1)*Math.max(...is.map(c=>c.length-1))+(is.length-1)*Math.max(...ir.map(c=>c.length-1)),prime=1009;
requireIt(ir.length===5&&is.length===14&&prior===104,"fixed original third Sylvester degrees");
const projection=mt(interpolate(Array.from({length:prior+1},(_,v)=>sylv(ir,is,v,prime)),prime)),candidate=reduceZ(remainder,prime);
requireIt(projection.length===82&&candidate.length===10&&candidate.at(-1)===938,"original Gauss input degree and leading unit");
const gauss=mxgcd(candidate,projection,prime);
requireIt(JSON.stringify(gauss.g)==="[1]","actual complete original Gauss Bezout");
const result={
 kind:"Q=1-u original s=0 mean-leading boundary complete",
 parameterChart:"h=ell/u, s=h(1-w)-1; s=0 is u(t+2y)-2x+1-u=0",
 JminusZeroQuadratic:"4u^2-u-1",JminusOriginalGcd:"1",
 originalCommonCurve:"2uh-1",commonCurveGermRowZero:true,commonCurveValueVarianceZero:true,
 exactResultant:{degree:cover.degree,priorBound:cover.degreeBound,primeCount:cover.primes.length,strictCRT:BigInt(cover.modulus)>2n*BigInt(cover.bound)},
 exactFactors:factorHistory,remainderDegree:remainder.length-1,
 rationalFibres:{"1/4":"h-2 -> m=0","1/3":"h-3 -> Hh=0"},
 quadraticFibre:"(h-(1+4u))^2 -> Jminus=0",
 actualGauss:{prime,originalFixedMatrixSize:17,priorBound:prior,degree:projection.length-1,coverLeading:candidate.at(-1),bezoutDegrees:[gauss.s.length-1,gauss.t.length-1],return:gauss.g},
 exactQuotientCounts:{inverses:kinverses,divisions:kdivisions,bezouts:kbezouts},
 ordinaryISPClaim:false,remainingQBoundaryClaim:false
};
emit(result);return result;
})();
