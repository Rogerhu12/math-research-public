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


const input=arguments[0],start=Date.now(),names=["N1","Ns","Ps"],R=names.map(n=>input.results[n].remaining.map(qparse));
let current=R[0],comb=[[uo()],[],[]],steps=[];
for(let i=1;i<3;i++){
 const t=Date.now(),[g,a,b]=ugx(current,R[i]);
 if(us(ua(um(a,current),um(b,R[i])),g).length)throw Error("whole original QQ Bezout");
 comb=comb.map(c=>um(a,c));comb[i]=ua(comb[i],b);current=g;
 if(us(comb.reduce((s,c,j)=>ua(s,um(c,R[j])),[]),current).length)throw Error("three original resultants return");
 steps.push({input:i,gcdDegree:g.length-1,gcd:g.map(c=>c.str()),multiplierDegrees:[a.length-1,b.length-1],seconds:(Date.now()-t)/1000});
 if(g.length===1)break;
}
return{stage:"whole_equal_half_weight_original_resultant_Bezout",gcd:current.map(c=>c.str()),gcdDegree:current.length-1,combination:comb.map(p=>p.map(c=>c.str())),originalNecessaryResultants:names,steps,allProductsMultipliedBack:true,unit:current.length===1&&current[0].eq(1),seconds:(Date.now()-start)/1000};
