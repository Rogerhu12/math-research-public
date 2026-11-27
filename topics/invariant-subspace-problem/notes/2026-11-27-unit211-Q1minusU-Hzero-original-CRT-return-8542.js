/* Exact original H=0 return on Q=1-u. All arithmetic is rational/BigInt.
   Requires the already proved exclusion y=1; no scratch files or packages.
   Run with node, or evaluate in a V8 isolate providing text(). */
(() => {
const sourceStart=Date.now(),lines=[];
function emit(v){const s=JSON.stringify(v);lines.push(s);if(typeof text==='function')text(s);else console.log(s);}

function sha256Ascii(s){
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19],b=[...s].map(c=>{const n=c.charCodeAt(0);if(n>127)throw Error("nonASCII hash");return n;}),len=b.length;b.push(128);while(b.length%64!==56)b.push(0);const high=Math.floor(len/0x20000000),low=(len*8)>>>0;for(let j=3;j>=0;j--)b.push((high>>>(j*8))&255);for(let j=3;j>=0;j--)b.push((low>>>(j*8))&255);
 const rr=(x,n)=>(x>>>n)|(x<<(32-n));
 for(let k=0;k<b.length;k+=64){const w=Array(64).fill(0);for(let j=0;j<16;j++)w[j]=(b[k+4*j]<<24)|(b[k+4*j+1]<<16)|(b[k+4*j+2]<<8)|b[k+4*j+3];for(let j=16;j<64;j++){const a=w[j-15],z=w[j-2];w[j]=(w[j-16]+(rr(a,7)^rr(a,18)^(a>>>3))+w[j-7]+(rr(z,17)^rr(z,19)^(z>>>10)))|0;}let [a,c,d,e,f,g,i,j]=h;for(let z=0;z<64;z++){const t1=(j+(rr(f,6)^rr(f,11)^rr(f,25))+((f&g)^(~f&i))+K[z]+w[z])|0,t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&c)^(a&d)^(c&d)))|0;j=i;i=g;g=f;f=(e+t1)|0;e=d;d=c;c=a;a=(t1+t2)|0;}const v=[a,c,d,e,f,g,i,j];for(let z=0;z<8;z++)h[z]=(h[z]+v[z])>>>0;}
 return h.map(x=>x.toString(16).padStart(8,"0")).join("");
}

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
const u=new P(new F([0,1])),ell=u.neg().div(u.mul(2).sub(1)),Qp=new P(1).sub(u);
const x=new P(new Map([["1,0",new F(1)]])),y=new P(new Map([["0,1",new F(1)]]));
const t=x.mul(2).add(u).sub(1).div(u).sub(y.mul(2));
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

function rq(s){let z=String(s).split("/");return new Q(z[0],z.length>1?z[1]:1);}
function yfrom(data){let a=Array.from({length:1+Math.max(...data.map(z=>z.e[1]))},()=>new F());for(let z of data){if(z.e[0])throw Error("not y");a[z.e[1]]=new F(z.n.map(rq),z.d.map(rq));}return a;}
function paidPoly(a){a=a.slice();const hist=[];for(let [nm,p]of [["u",[q0,q1]],["u-1",[new Q(-1),q1]],["2u-1",[new Q(-1),new Q(2)]],["4u-1",[new Q(-1),new Q(4)]]]){let n=0;while(a.length>1){let g=pg(a,p);if(g.length<=1)break;let qr=pd(a,g);if(qr[1].length)throw Error("bad division");a=qr[0];n++;}if(n)hist.push([nm,n]);}if(a.length>1)throw Error("unpaid content "+a.map(z=>z.str()));return hist;}
function primitive(a){let den=[q1];for(let c of a){let g=pg(den,c.q);let qr=pd(pm(den,c.q),g);if(qr[1].length)throw Error("lcm");den=qr[0];}let paidDen=paidPoly(den),ar=a.map(c=>{let qr=pd(den,c.q);if(qr[1].length)throw Error("den");return pm(c.p,qr[0]);}),g=[];for(let p of ar)g=pg(g,p);let paidContent=paidPoly(g);let out=ar.map(p=>{let qr=pd(p,g);if(qr[1].length)throw Error("content");return new F(qr[0]);});return {out,paidDen,paidContent};}

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

function zg(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let c=a%b;a=b;b=c;}return a;}
function zt(p){p=p.slice();while(p.length&&p[p.length-1]===0n)p.pop();return p;}
function zprim(p){p=zt(p);if(!p.length)return p;let g=0n;for(let c of p)g=zg(g,c);if(p[p.length-1]<0n)g=-g;let q=p.map(c=>c/g);if(q.some((c,i)=>c*g!==p[i]))throw Error("primitive return");return q;}
function zrem(A,B){let r=A.slice(),steps=0;while(r.length>=B.length&&r.length){let j=r.length-B.length,a=r[r.length-1],b=B[B.length-1],n=r.map(c=>c*b);for(let k=0;k<B.length;k++)n[j+k]-=a*B[k];n=zt(n);if(n.length>=r.length)throw Error("degree did not drop");r=zprim(n);steps++;}return {r,steps};}
function zgcd(A,B){let a=zprim(A),b=zprim(B),trace=[];while(b.length){let z=zrem(a,b);trace.push({a:a.length-1,b:b.length-1,r:z.r.length-1,steps:z.steps});a=b;b=z.r;}return {g:zprim(a),trace};}

function zdiv(A,B){let r=A.slice(),q=Array(Math.max(0,A.length-B.length+1)).fill(0n);while(r.length>=B.length&&r.length){let j=r.length-B.length;if(r[r.length-1]%B[B.length-1]!==0n)return null;let c=r[r.length-1]/B[B.length-1];q[j]+=c;for(let k=0;k<B.length;k++)r[j+k]-=c*B[k];r=zt(r);}return {q:zt(q),r};}
function zmul(a,b){if(!a.length||!b.length)return [];let z=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]+=a[i]*b[j];return zt(z);}

function pxgcd(a,b){let A=a.slice(),B=b.slice(),s0=[q1],s1=[],t0=[],t1=[q1];while(B.length){let [q,r]=pd(A,B);if(!pe(pa(pm(q,B),r),A))throw Error("QQ division");A=B;B=r;[s0,s1]=[s1,ps(s0,pm(q,s1))];[t0,t1]=[t1,ps(t0,pm(q,t1))];}if(!A.length)return {g:[],s:[],t:[]};let k=q1.div(A[A.length-1]);A=pc(A,k);s0=pc(s0,k);t0=pc(t0,k);if(!pe(pa(pm(s0,a),pm(t0,b)),A))throw Error("QQ Bezout return");return {g:A,s:s0,t:t0};}
const phi=[new Q(-1),new Q(2),new Q(-4),new Q(16)];
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

const FF=x.pow(2).sub(u.add(1).mul(x)).add(u.add(1).div(4)).add(u.mul(u.mul(2).add(1)).mul(y)).sub(u.mul(x).mul(y).mul(2));
const GG=x.pow(2).sub(x.div(2)).sub(u.mul(x).mul(y).mul(4)).add(u.mul(y.pow(2))).add(u.mul(u.mul(4).add(1)).mul(y).div(2)).sub(u.mul(u.mul(2).sub(1)).div(2));
const du=u.mul(2).sub(1),ku=u.mul(4).sub(1),vu=u.sub(1);
if(!E1.a.eq(FF.mul(ku.mul(vu).mul(2).div(du.pow(2)))))throw Error("E1 factor");
if(!Rt.eq(FF.mul(vu.mul(-4).div(u.pow(2)))))throw Error("Rt factor");
if(!NH.a.eq(GG.mul(u.mul(vu.pow(2)).mul(ku).mul(4).div(du.pow(3)))))throw Error("N1 factor");
const L=GG.sub(FF).mul(4),l1=u.mul(4).add(2).sub(u.mul(y).mul(8)),l0=u.mul(y.pow(2)).mul(4).sub(u.mul(y).mul(2)).sub(u.pow(2).mul(4)).add(u).sub(1);
if(!L.eq(l1.mul(x).add(l0)))throw Error("linear");
function xcoeff(pp,i){return new P(new Map([...pp.m].filter(([k,v])=>Number(k.split(",")[0])===i).map(([k,v])=>["0,"+k.split(",")[1],v])));}
function linres(pp){let deg=Math.max(...[...pp.m.keys()].map(k=>Number(k.split(",")[0]))),rr=new P();for(let i=0;i<=deg;i++)rr=rr.add(xcoeff(pp,i).mul(l0.neg().pow(i)).mul(l1.pow(deg-i)));return rr;}
const fy=linres(FF),ny=linres(NS.a),py=linres(PS.a);
for(let obj of [f,lam,T,FF,GG,NS.a,PS.a,Rt,Ry,...rows.flat().flatMap(e=>[e.a,e.b])])for(let cf of obj.m.values())paidPoly(cf.q);
const prF=primitive(yfrom(fy.json())),prN=primitive(yfrom(ny.json())),prP=primitive(yfrom(py.json()));
const primitiveRows={F:prF.out.map(z=>z.json()),N:prN.out.map(z=>z.json()),P:prP.out.map(z=>z.json())};
emit({stage:"original_Gram_and_low_rows",E0_N0_P1:true,meanAndN1ExactFactors:true,homogeneousXElimination:true,newUnitsInverted:false,profiles:[prF,prN,prP].map(z=>({yDegree:z.out.length-1,uDegree:Math.max(...z.out.map(v=>v.p.length-1)),paidDen:z.paidDen,paidContent:z.paidContent}))});
const AA=integerRows(primitiveRows.F),BB=integerRows(primitiveRows.N),CC=integerRows(primitiveRows.P);
const resN=crtRes(AA.a,BB.a),resP=crtRes(AA.a,CC.a);
if(resN.degree!==53||resP.degree!==53||resN.degreeBound!==54||resP.degreeBound!==54)throw Error("wrong full degrees");
const RN=resN.coeff.map(BigInt),RP=resP.coeff.map(BigInt),gcdReturn=zgcd(RN,RP),zG=gcdReturn.g;
let prod=[1n];for(let [v,n]of [[[0n,1n],4],[[-1n,4n],4],[[-1n,2n,-4n,16n],6]])for(let j=0;j<n;j++)prod=zmul(prod,v);
if(zG.length!==prod.length||zG.some((v,i)=>v!==prod[i]))throw Error("gcd factorization return");
for(let pp of [RN,RP]){let z=zdiv(pp,zG);if(!z||z.r.length)throw Error("gcd exact quotient");let ret=zmul(z.q,zG);if(ret.length!==pp.length||ret.some((v,i)=>v!==pp[i]))throw Error("gcd quotient multiplication");}
emit({stage:"complete_integer_resultants_and_QQ_gcd",N:{degree:resN.degree,degreeBound:54,primes:resN.primes,bound:resN.bound,modulus:resN.modulus,sha256:sha256Ascii(JSON.stringify(resN.coeff))},P:{degree:resP.degree,degreeBound:54,primes:resP.primes,bound:resP.bound,modulus:resP.modulus,sha256:sha256Ascii(JSON.stringify(resP.coeff))},primitivePRSDegrees:gcdReturn.trace.map(z=>[z.a,z.b,z.r]),gcd:"u^4(4u-1)^4(16u^3-4u^2+2u-1)^6",factorAndQuotientMultiplications:true,scales:[String(AA.s),String(BB.s),String(CC.s)]});
const YF=yK(primitiveRows.F),YN=yK(primitiveRows.N),YP=yK(primitiveRows.P);
let yg=kxgcd(YF,YN).g;yg=kxgcd(yg,YP).g;
const yy=[new Q(1),new Q(-1),new Q(4)],lin=[kn(yy),[q1]],sq=kpm(lin,lin);
if(kps(yg,sq).length)throw Error("unexpected y gcd");
const U=[q0,q1],ONE=[q1],uu1=ka(U,ONE),XF=[ka(pc(uu1,new Q(1,4)),km(km(U,ka(pc(U,new Q(2)),ONE)),yy)),kn(ka(uu1,pc(km(U,yy),new Q(2)))),ONE];
const XN=xK(NS.a.json(),yy),XP=xK(PS.a.json(),yy);
let xg=kxgcd(XF,XN).g;xg=kxgcd(xg,XP).g;
if(xg.length!==1||!pe(xg[0],ONE))throw Error("original x fibre not empty");
const receipt={stage:"complete",scope:"Q=1-u, (2u-1)ell+u=0, y!=1 excluded",combineWithPaidY1ToExcludeWholeHLine:true,wholeQBoundaryExcluded:false,ordinaryISPClaim:false,wholeCubicQuotient:true,yGcd:"(y-(4u^2-u+1))^2",originalXGcd:1,coefficientInverseReturns:kinverses,polynomialDivisionReturns:kdivisions,BezoutReturns:kbezouts,elapsedMs:Date.now()-sourceStart};
emit(receipt);
return {receipt,stdoutSha256:sha256Ascii(lines.join("\n")+"\n"),stdoutBytes:lines.join("\n").length+1};

})();
