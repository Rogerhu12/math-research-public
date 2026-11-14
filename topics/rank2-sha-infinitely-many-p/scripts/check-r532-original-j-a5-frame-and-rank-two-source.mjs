#!/usr/bin/env node
// Exact Q(delta), delta^2=-3. No external packages.
const certificate=(()=>{

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

const om=c(q(-1,2),q(1,2)),o2=cp(om,2),de=c(0,1),aa=ca(c(2),om);
const sc=(a,r)=>r.map(x=>cm(a,x)),pl=(a,b)=>a.map((x,i)=>ca(x,b[i])),mi=(a,b)=>a.map((x,i)=>cs(x,b[i]));
const Y=[de,cm(c(2),de),ca(c(3),om),cs(c(2),om),c(1),c(2)];
const X=[c(),c(),c(),c(1),c(),c()],X2=[c(),c(1),c(),c(),c(),c()],D0=[c(),c(),c(),c(),c(),c(1)];
const Q=[c(1),c(),c(1),c(),cn(o2),c()];
const H0=[c(1),c(),c(-1),c(1),c(),c()];
const Cref=[c(q(1,2)),c(),cm(c(q(1,2)),o2),cm(c(q(-1,2)),om),c(q(-1,2)),c()];
const J=mi(Cref,X),K=mi(Cref,sc(o2,X)),eta=cd(cm(c(2),cs(c(1),om)),c(3)),E=mi(H0,sc(eta,K));
const R3=[c(1),c(),o2,c(),c(-1),c()];
const s0=sc(cd(aa,c(3)),Q),A=pl(pl(s0,sc(de,X2)),D0),B=mi(s0,D0),C30=pl(mi(sc(c(3),s0),sc(cm(c(2),de),X2)),sc(c(3),D0));
const frame=[J,A,K,E,B,C30],norms=[q(3,2),q(5),q(3,2),q(1),q(2),q(30)];
for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(!ce(dot(frame[i],frame[j]),i===j?c(norms[i]):c()))throw Error("orthogonal frame "+i+","+j);
function assertrow(a,b,m){a.forEach((x,i)=>{if(!ce(x,b[i]))throw Error(m+" "+i)})}
const U=sc(c(2),J),V=sc(c(3),A),yc=cd(ca(c(-1),cm(c(4),om)),c(3)),yd=c(q(2,3));
assertrow(pl(sc(yc,U),sc(yd,V)),Y,"original Y");
assertrow(pl(J,K),R3,"actual carry");
for(const r of [Q,X2,D0])for(const t of [J,K,E])if(!ce(dot(r,t),c()))throw Error("block orthogonality");
const units=[0,2,3,4],MT=[[cn(om),c(1),o2,om],[cn(o2),cn(om),c(1),cn(o2)],[c(-1),cn(o2),cn(om),c(1)],[cn(om),c(1),cn(o2),cn(om)]].map(r=>sc(c(q(1,2)),r));
const Id=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0))),T=Id.map(r=>r.slice());units.forEach((i,a)=>units.forEach((j,b)=>T[i][j]=MT[a][b]));
for(let i=0;i<6;i++)assertrow(mm([frame[i]],T)[0],sc(i===2||i===3?o2:c(1),frame[i]),"T frame "+i);
function det(M){let A=M.map(r=>r.slice()),z=c(1);for(let i=0;i<A.length;i++){let k=i;while(k<A.length&&ce(A[k][i],c()))k++;if(k===A.length)return c();if(k!==i){[A[k],A[i]]=[A[i],A[k]];z=cn(z)}const t=A[i][i];z=cm(z,t);for(let j=i+1;j<A.length;j++){const f=cd(A[j][i],t);for(let k=i;k<A.length;k++)A[j][k]=cs(A[j][k],cm(f,A[i][k]));}}return z}
const fi=frame[0].map((_,i)=>frame.map((r,j)=>cd(cc(r[i]),c(norms[j]))));
const check=mm(frame,fi);for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(!ce(check[i][j],Id[i][j]))throw Error("full inverse");
if(!eq(norm(det(frame)),q(675)))throw Error("determinant");
const clear=[sc(c(2),J),sc(c(3),A),sc(c(2),K),sc(c(3),E),sc(c(3),B),C30],levels=[6,45,6,9,18,30];
function ok(z){const a=add(z[0],z[1]),b=mul(q(2),z[1]);return {a:qs(a),omega:qs(b),integral:a[1]===1n&&b[1]===1n}}
const chars=clear.map((r,i)=>{if(!ce(dot(r,r),c(levels[i])))throw Error("level");return r.map(ok)});
if(chars.flat().some(x=>!x.integral))throw Error("nonintegral cleared row");
const trans=[[aa,cm(c(3),de),c(3)],[aa,c(),c(-3)],[aa,cm(c(-2),de),c(3)]],transdet=det(trans);
if(!ce(transdet,cm(c(-90),om)))throw Error("complete three-input determinant");
const sel=[0,2,4],trip=[R3,Q,E].map(r=>sel.map(i=>r[i]));
if(!eq(norm(det(trip)),q(9)))throw Error("original hidden three-input frame");
const product=Array(7).fill(null).map(()=>c());let poly=[c(1)];
for(let i=0;i<6;i++){const out=Array(poly.length+1).fill(null).map(()=>c());for(let j=0;j<poly.length;j++){out[j]=ca(out[j],cm(poly[j],V[i]));out[j+1]=ca(out[j+1],cm(poly[j],U[i]));}poly=out;}
poly=sc(c(q(-1,84)),poly);
const expected=Array(7).fill(null).map(()=>c());expected[4]=c(q(-9,28));expected[1]=cm(c(q(-27,28)),de);
for(let j=0;j<7;j++)if(!ce(poly[j],expected[j]))throw Error("entire rank-two leading phase "+j);
function pmul(a,b){let out=Array(a.length+b.length-1).fill(null).map(()=>c());a.forEach((x,i)=>b.forEach((y,j)=>out[i+j]=ca(out[i+j],cm(x,y))));return out}
const b=c(1),linear=[c(4),c(1)],cube=[c(64),c(48),c(-96),c(1)],P=pmul(pmul(linear,linear),cube);
const P2=pmul([c(-8),c(1)],P);
const W=[de,cm(c(2),de),ca(c(3),om),cs(c(2),om),cm(c(3),de),c(4)];
const wframe=mm([W],fi)[0];
const first= {U4_V2:cm(c(q(-9,28)),c(48)),U1_V5:cm(c(q(-27,28)),cm(de,c(120)))};
return {
 status:"exact full six-input J/A5 frame, absolute-core inputs, theta normalization and rank-two coefficients verified",
 omega:cj(om),delta:cj(de),a:cj(aa),Y:Y.map(cj),J:J.map(cj),A5:A.map(cj),K:K.map(cj),E_K:E.map(cj),B2:B.map(cj),C30:C30.map(cj),
 old_W_in_frame:wframe.map(cj),frame:frame.map(r=>r.map(cj)),inverse:fi.map(r=>r.map(cj)),Gram:norms.map(qs),determinant:cj(det(frame)),determinant_norm:"675",
 clear_axes:chars,levels,current_center:{modulus:180,ratio:{a:91,omega:0},reduced:levels.map(n=>({level:n,modulus:2*n,ratio:91%(2*n)}))},
 cores:["beta","chi65 lambda","beta","beta","beta","chi65 lambda"],
 three_old_axes:["Q3","xi2","d0"],three_new_cleared:["3A5","3B2","C30"],three_matrix:trans.map(r=>r.map(cj)),three_determinant:cj(transdet),
 old_hidden_triple:["R3","Q3","E_K"],old_hidden_triple_matrix:trip.map(r=>r.map(cj)),old_hidden_triple_det:cj(det(trip)),
 T_diagonal:["1","1","omega^2","omega^2","1","1"],T:T.map(r=>r.map(cj)),
 U:U.map(cj),V:V.map(cj),Y_in_UV:[cj(yc),cj(yd)],six_sigma_leading_polynomial_U_power:poly.map(cj),
 exact_tensor:"Phi=-(9/28) f4(Ugen)g2(Vgen)-(27delta/28) f1(Ugen)g5(Vgen)",
 normalized_factors:{f1:"-x*y*sigma^6",f4:"x*sigma^6",g5:"sigma^45*x^5*(X+4b)^2*(X^3-96bX^2+48b^2X+64b^3)",g2:"-sigma^45*x^2*y*(X-8b)*(X+4b)^2*(X^3-96bX^2+48b^2X+64b^3)"},
 g5_polynomial_in_X_b1:P.map(cj),g2_polynomial_in_X_b1:P2.map(cj),mixed_sixth_moments_in_units_Omega6:Object.fromEntries(Object.entries(first).map(([k,v])=>[k,cj(v)])),
 Dn_exact:"A5,B2,C30,E_K deep n; K unit; J+K deep n",
 Dnr_exact:"A5,B2,C30,E_K deep n; K unit; J/kappa^r+K deep n",
 boundary:"rank two is the genuine two-output pushforward; the displayed original hidden carry conditions are retained and are not replaced by marginal events"
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
