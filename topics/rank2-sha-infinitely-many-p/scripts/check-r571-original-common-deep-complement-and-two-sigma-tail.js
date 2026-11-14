'use strict';
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}


const certificate = (function(){

const w=c(q(-1,2),q(1,2)), w2=cp(w,2), delta=c(0,1), one=c(1), zero=c(), six=c(6);
const Cw=(a,b=0)=>ca(c(a),cm(c(b),w));
const va=(x,y)=>x.map((a,i)=>ca(a,y[i])),vs=(x,y)=>x.map((a,i)=>cs(a,y[i])),vm=(k,x)=>x.map(a=>cm(k,a));
const row=(...x)=>x.map(a=>Array.isArray(a)?a:c(a));
const d4=row(1,w2,cm(c(-2),w),0,0,0), cv=row(0,0,0,0,1,0), dv=row(0,0,0,0,0,1);
const C=vm(ci(delta),row(1,0,-1,1,0,0)),H1=row(-1,2,w,ca(one,w),0,0);
const ac=Cw(2,3),lc=Cw(1,3),gg=Cw(3,-2),aa=cd(Cw(1,6),six);
const D=va(d4,va(cv,vm(ac,dv))),E=va(D,vm(c(14),C)),G=va(vm(c(13),H1),vm(gg,va(D,C)));
const A=row(delta,cm(c(2),delta),Cw(3,1),Cw(2,-1),0,0);
const Y=va(A,va(cv,vm(c(2),dv))),W=va(A,va(vm(cm(c(3),delta),cv),vm(c(4),dv))),L=va(vm(lc,cv),dv);
const Cstar=va(C,vm(ci(six),d4)),Hstar=va(H1,vm(cd(gg,six),d4));
const Es=vm(c(14),Cstar),Gs=va(vm(c(13),Hstar),vm(gg,Cstar)),As=vs(A,vm(aa,d4));
const e=va(vm(c(q(-4,3)),d4),va(cv,vm(ac,dv)));
const yy=va(vm(aa,d4),va(cv,vm(c(2),dv))),ww=va(vm(aa,d4),va(vm(cm(c(3),delta),cv),vm(c(4),dv)));
const X=vs(cv,vm(c(q(1,14)),D)),Z=va(dv,vm(cd(lc,c(14)),D));
const u=vm(c(q(1,2)),va(vm(w,cv),vm(cs(one,w),dv))),P=vs(u,vm(cd(w2,c(7)),D));
const Zs=vs(Z,vm(cd(Cw(8,3),c(10)),P));
let checks=0;function asserte(x,y,label){checks++;if(!ce(x,y))throw Error(label+": "+JSON.stringify([cj(x),cj(y)]));}
function assertrow(x,y,label){for(let i=0;i<x.length;i++)asserte(x[i],y[i],label+" "+i);}
assertrow(E,va(Es,e),"E split");assertrow(G,va(Gs,vm(gg,e)),"G split");
assertrow(Y,va(As,yy),"Y split");assertrow(W,va(As,ww),"W split");assertrow(vs(ww,yy),vm(c(2),L),"W-Y");
asserte(dot(d4,d4),six,"D4 norm");
for(const [name,r]of [["Es",Es],["Gs",Gs],["As",As]]){asserte(dot(r,d4),zero,name+" orth D4");asserte(r[4],zero,name+" no c");asserte(r[5],zero,name+" no d");}
for(const r of [e,yy,ww,L])asserte(dot(r,D),zero,"normal plane orth D");
assertrow(P,vm(cd(w,c(2)),vs(X,vm(Cw(2,1),Z))),"P/XZ");
asserte(dot(P,Zs),zero,"P orth Zstar");asserte(dot(D,P),zero,"D orth P");asserte(dot(D,Zs),zero,"D orth Zstar");
asserte(dot(P,P),c(q(5,7)),"norm P");asserte(dot(Zs,Zs),c(q(3,20)),"norm Zstar");
asserte(cm(lc,ac),c(-7),"l*a=-7");asserte(ca(one,cm(lc,ac)),c(-6),"sigma mixed coefficient");
function det(M){M=M.map(r=>r.slice());let ans=one;for(let j=0;j<M.length;j++){let k=j;while(k<M.length&&ce(M[k][j],zero))k++;if(k===M.length)return zero;if(k!==j){[M[k],M[j]]=[M[j],M[k]];ans=cn(ans);}const piv=M[j][j];ans=cm(ans,piv);for(let i=j+1;i<M.length;i++){const f=cd(M[i][j],piv);for(let q=j;q<M.length;q++)M[i][q]=cs(M[i][q],cm(f,M[j][q]));}}return ans;}
const frameDet=det([d4,cv,dv,Es,Gs,As]);
if(ce(frameDet,zero))throw Error("singular frame");
const primal=row(1,w2,cm(c(-2),w),0,0,0);
const conjRows=[primal,row(cn(w),w2,cs(one,w),w2,0,0),row(cs(one,w),w2,cn(w),cn(w),0,0)];
for(const r of conjRows)asserte(dot(r,r),six,"conjugate norm6");
const p7=ca(cs(cm(c(3),lc),cm(c(41),ac)),cm(cp(ac,5),cs(cp(ac,2),c(3))));
const output={status:"exact rational CM verification passed",checks,field:"Q(delta), delta^2=-3",norms:{D4:"6",D:"14",P:"5/7",Zstar:"3/20"},frame_det:cj(frameDet),frame_det_norm:qs(norm(frameDet)),axes:{D4:d4.map(cj),E_star:Es.map(cj),G_star:Gs.map(cj),A_star:As.map(cj),e_normal:e.map(cj),y_normal:yy.map(cj),w_normal:ww.map(cj)},mixed_sigma_factor:"1+(1+3omega)(2+3omega)=-6",first_log_sigma_factor:"12*(p-1)*Omega^2",next_high_sigma_check:cj(p7),scope:"All original conditional cuts remain; no nonvanishing of K1 or complete arithmetic total is asserted."};
return output;

})();
console.log(JSON.stringify(certificate,null,2));
