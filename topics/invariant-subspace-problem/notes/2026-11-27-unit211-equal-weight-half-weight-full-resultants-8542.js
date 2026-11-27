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

const input=arguments[0],start=Date.now();
function from(a){let f=[];for(const[e,c]of a){while(f.length<=e[1])f.push([]);while(f[e[1]].length<=e[0])f[e[1]].push(uz());f[e[1]][e[0]]=qparse(c);}return f.map(ut);}
const E=from(input.E),out={stage:"whole_equal_half_weight_full_original_QQ_z_resultants",fixedDegreeE:E.length-1,results:{},excluded:false};
for(const name of ["N1","Ns","Ps"]){
 const f=from(input.rows[name].polynomial),t=Date.now(),res=resultant(E,f);let r=res,removed=[uo()],paid=[];
 for(const[label,u]of [["d",[uz(),uo()]],["Q",[new Q(-1),uo()]]]){let n=0;while(r.length){const[a,b]=ud(r,u);if(b.length)break;r=a;removed=um(removed,u);n++;}if(n)paid.push([label,n]);}
 if(us(um(r,removed),res).length)throw Error("resultant unit stripping");
 out.results[name]={degree:res.length-1,remainingDegree:r.length-1,fixedZDegrees:[E.length-1,f.length-1],paid,coefficients:res.map(c=>c.str()),remaining:r.map(c=>c.str()),seconds:(Date.now()-t)/1000};
}
out.seconds=(Date.now()-start)/1000;return out;
