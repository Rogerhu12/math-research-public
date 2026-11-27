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
function minExp(v,i){return Math.min(...Array.from(v.c.keys(),k=>Number(k.split(",")[i])));}
function ld(v){return v.json()[0];}
function pdiv(v,dv){let work=new P(v),quot=new P(),rem=new P();const [ed,cd]=ld(dv),dc=new Q(...cd.split("/"));let steps=0;while(work.c.size){if(++steps>10000)throw Error("division step cap");const[ew,cw]=ld(work),wc=new Q(...cw.split("/"));if(ew.every((e,i)=>e>=ed[i])){const mon=P.term(ew.map((e,i)=>e-ed[i]),wc.div(dc));quot=quot.add(mon);work=work.sub(mon.mul(dv));}else{const mon=P.term(ew,wc);rem=rem.add(mon);work=work.sub(mon);}}if(!quot.mul(dv).add(rem).eq(v))throw Error("multivariate division return");return[quot,rem];}

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
function det(A){A=A.map(r=>r.map(p=>p.slice()));let sign=1,prev=[uo()];for(let k=0;k<A.length-1;k++){if(!A[k][k].length){let i=k+1;while(i<A.length&&!A[i][k].length)i++;if(i===A.length)return[];[A[k],A[i]]=[A[i],A[k]];sign=-sign;}const piv=A[k][k];for(let i=k+1;i<A.length;i++){for(let j=k+1;j<A.length;j++)A[i][j]=ue(us(um(A[i][j],piv),um(A[i][k],A[k][j])),prev);A[i][k]=[];}prev=piv;}return uc(A[A.length-1][A.length-1],new Q(sign));}
function resultant(f,g){const n=f.length-1,m=g.length-1,N=n+m,mat=Array.from({length:N},()=>Array.from({length:N},()=>[]));for(let i=0;i<m;i++)for(let j=0;j<=n;j++)mat[i][i+j]=f[n-j];for(let i=0;i<n;i++)for(let j=0;j<=m;j++)mat[m+i][i+j]=g[m-j];return det(mat);}

const input=arguments[0],selection=arguments[1],report=arguments[2]||(()=>{}),started=Date.now();
function coeffK(row){const cc=Array.from({length:row.degrees[0]+1},()=>[]);for(const[e,c]of row.coefficients){while(cc[e[0]].length<=e[1])cc[e[0]].push(uz());cc[e[0]][e[1]]=qparse(c);}return cc.map(ut);}
const E=coeffK(input.E),out={stage:"original_v_minus_one_complete_resultants",fixedEdegree:E.length-1,rows:{},excluded:false};
for(const name of selection){
 const F=coeffK(input.rows[name]),res=resultant(E,F);let f=res,paid=[];
 for(const[label,u]of [["w",[uz(),uo()]],["w_minus_one",[new Q(-1),uo()]]]){let ct=0;while(f.length){const[q,r]=ud(f,u);if(r.length)break;f=q;ct++;}if(ct)paid.push([label,ct]);}
 const sc=f.length?uo().div(f[f.length-1]):uo();f=uc(f,sc);
 out.rows[name]={fixedRowDegree:F.length-1,fullDegree:res.length-1,paid,monicScale:sc.str(),degree:f.length-1,coefficients:f.map(z=>z.str()),fullCoefficients:res.map(z=>z.str())};
 report({name,seconds:(Date.now()-started)/1000,fullDegree:res.length-1,paid,degree:f.length-1});
}
out.seconds=(Date.now()-started)/1000;return out;
