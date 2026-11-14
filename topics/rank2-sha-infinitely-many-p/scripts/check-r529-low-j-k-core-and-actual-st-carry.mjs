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

const om=c(q(-1,2),q(1,2)),o2=cp(om,2),ga=c(q(5,2),q(1,2)),bg=cc(ga);
const plus=(a,b)=>a.map((t,i)=>ca(t,b[i])),minus=(a,b)=>a.map((t,i)=>cs(t,b[i])),sc=(a,r)=>r.map(t=>cm(a,t));
const Y=[c(0,1),c(0,2),ga,bg,c(1),c(2)],W=[c(0,1),c(0,2),ga,bg,c(0,3),c(4)];
const X=[c(),c(),c(),c(1),c(),c()],X2=[c(),c(1),c(),c(),c(),c()],D0=[c(),c(),c(),c(),c(),c(1)];
const C=[c(q(1,2)),c(),cm(c(q(1,2)),o2),cm(c(q(-1,2)),om),c(q(-1,2)),c()];
const H0=[c(1),c(),c(-1),c(1),c(),c()],J=minus(C,X),K=minus(C,sc(o2,X));
const eta=cd(cm(c(2),cs(c(1),om)),c(3)),E=minus(H0,sc(eta,K));
const R3=[c(1),c(),o2,c(),c(-1),c()],R=sc(c(q(1,2)),R3),aa=cd(ca(c(2),om),c(2));
const U1=[cn(om),c(),c(1),c(),c(),c()],U2=[c(1),c(),c(),c(),c(1),c()];
if(!ce(dot(J,K),c())||!ce(dot(J,J),c(q(3,2)))||!ce(dot(K,K),c(q(3,2)))||!ce(dot(E,E),c(1))||!ce(dot(E,K),c())||!ce(dot(E,J),c()))throw Error("orthogonal low axes");
for(let i=0;i<6;i++)if(!ce(J[i],cs(R[i],cm(aa,X[i])))||!ce(K[i],ca(R[i],cm(aa,X[i]))))throw Error("sigma pair");
const I=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const ids=[0,2,3,4],TI=[[cn(om),c(1),o2,om],[cn(o2),cn(om),c(1),cn(o2)],[c(-1),cn(o2),cn(om),c(1)],[cn(om),c(1),cn(o2),cn(om)]].map(r=>sc(c(q(1,2)),r));
const TT=I.map(r=>r.slice());for(let i=0;i<4;i++)for(let j=0;j<4;j++)TT[ids[i]][ids[j]]=TI[i][j];
function assertrow(a,b,m){for(let i=0;i<a.length;i++)if(!ce(a[i],b[i]))throw Error(m+" "+i)}
assertrow(mm([J],TT)[0],J,"J T");assertrow(mm([K],TT)[0],sc(o2,K),"K T");assertrow(mm([E],TT)[0],sc(o2,E),"E T");
for(const r of [K,E,H0])if(!ce(dot(Y,r),c()))throw Error("pure Y");
const pi=[J,Y,X2,D0];for(const r of pi)for(const a of [K,E,H0])if(!ce(dot(r,a),c()))throw Error("fixed four output");
const F=[...pi,K,E];
function inverse(M){const n=M.length,A=M.map((r,i)=>r.concat(I[i]));for(let i=0;i<n;i++){let k=i;while(k<n&&ce(A[k][i],c()))k++;if(k===n)throw Error("singular");if(k!==i)[A[k],A[i]]=[A[i],A[k]];const p=A[i][i];A[i]=A[i].map(x=>cd(x,p));for(let j=0;j<n;j++)if(j!==i){const f=A[j][i];A[j]=A[j].map((x,t)=>cs(x,cm(f,A[i][t])));}}return A.map(r=>r.slice(n))}
function det(M){let A=M.map(r=>r.slice()),v=c(1);for(let i=0;i<A.length;i++){let k=i;while(k<A.length&&ce(A[k][i],c()))k++;if(k===A.length)return c();if(k!==i){[A[k],A[i]]=[A[i],A[k]];v=cn(v)}const p=A[i][i];v=cm(v,p);for(let j=i+1;j<A.length;j++){const f=cd(A[j][i],p);for(let t=i;t<A.length;t++)A[j][t]=cs(A[j][t],cm(f,A[i][t]));}}return v}
const Gpi=pi.map(r=>pi.map(s=>dot(r,s)));if(!ce(det(Gpi),c(6))||!eq(norm(det(F)),q(9)))throw Error("complete frame determinants");
const Fi=inverse(F),wc=mm([W],Fi)[0],Wp=mm([W],TT)[0],Wpp=mm([W],mm(TT,TT))[0];
const pj=J.map(a=>J.map(b=>cd(cm(cc(a),b),c(q(3,2)))));
const yshift=cd(dot(Y,J),c(q(3,2))),wshift=cd(dot(W,J),c(q(3,2)));
for(const w of [W,Wp,Wpp])if(!ce(cd(dot(w,J),c(q(3,2))),wshift))throw Error("three W shifts");
function O(z){const a=add(z[0],z[1]),b=mul(q(2),z[1]);return {a:qs(a),omega:qs(b),integral:a[1]===1n&&b[1]===1n}}
const axes=[sc(c(2),J),sc(c(2),K),sc(c(3),E),R3],dims=[6,6,9,3];
axes.forEach((r,i)=>{if(!ce(dot(r,r),c(dims[i]))||r.map(O).some(t=>!t.integral))throw Error("integral degree "+i)});
const src=[0,1,2,4,5],zr=src.map(i=>Y[i]),el=src.map(i=>E[i]),fl=src.map(i=>cs(H0[i],E[i]));
if(!ce(E[3],c()))throw Error("j0 retains free sigma");
let pol=[[c(1)]];
for(let i=0;i<5;i++){
 const out=Array.from({length:pol.length+1},()=>Array.from({length:6},()=>c()));
 for(let a=0;a<pol.length;a++)for(let j=0;j<pol[a].length;j++){
  out[a][j]=ca(out[a][j],cm(pol[a][j],el[i]));
  if(j+1<6)out[a][j+1]=ca(out[a][j+1],cm(pol[a][j],fl[i]));
  out[a+1][j]=ca(out[a+1][j],cm(pol[a][j],zr[i]));
 }
 pol=out.map(r=>r);
}
function fact(n){let x=1n;for(let i=2;i<=n;i++)x*=BigInt(i);return x}
const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
const coeff=Array.from({length:7},()=>c());
for(let a=1;a<=5;a++){
 const cc0=cd(c(q((a%2?1n:-1n)*choose(6,5-a)*fact(a)*fact(5-a),BigInt(a))),c(-84*216));
 const fac=cm(cc0,cp(ci(bg),a));
 for(let j=0;j<pol[a].length;j++)if(j+1+a<=6)coeff[j+1+a]=ca(coeff[j+1+a],cm(fac,pol[a][j]));
}
const alpha=cd(ca(c(-3221),cm(c(5000),om)),c(27n*7n**6n));
if(!ce(coeff.reduce(ca,c()),alpha)||coeff.slice(0,3).some(t=>!ce(t,c())))throw Error("complete fifth coefficient");
if(!eq(norm(alpha),q(1021n,3n**5n*7n**7n)))throw Error("unit norm");


function fifthFor(zv){
 let pp=[[c(1)]];
 for(let i=0;i<5;i++){const oo=Array.from({length:pp.length+1},()=>Array.from({length:6},()=>c()));for(let a=0;a<pp.length;a++)for(let j=0;j<pp[a].length;j++){oo[a][j]=ca(oo[a][j],cm(pp[a][j],el[i]));if(j+1<6)oo[a][j+1]=ca(oo[a][j+1],cm(pp[a][j],fl[i]));oo[a+1][j]=ca(oo[a+1][j],cm(pp[a][j],zv[i]));}pp=oo;}
 const qq=Array.from({length:7},()=>c());for(let a=1;a<=5;a++){const c0=cd(c(q((a%2?1n:-1n)*choose(6,5-a)*fact(a)*fact(5-a),BigInt(a))),c(-84*216));const fac=cm(c0,cp(ci(bg),a));for(let j=0;j<pp[a].length;j++)if(j+1+a<=6)qq[j+1+a]=ca(qq[j+1+a],cm(fac,pp[a][j]));}return qq;
}
const cw=fifthFor(src.map(i=>W[i])),diff=cw.map((t,j)=>cs(t,cm(c(0,6),coeff[j])));
if(!ce(diff.reduce(ca,c()),c()))throw Error("uncorrected S/T leading relation");
if(!eq(norm(diff[3]),q(400n,3n**8n*7n**3n)))throw Error("corrected S/T difference unit");
return {
 status:"all low-degree full-source geometry and the entire fifth coefficient exactly verified",
 J:J.map(cj),K:K.map(cj),E_K:E.map(cj),eta:cj(eta),
 R3:R3.map(cj),independent_sigma_coefficient:cj(aa),R_companions:[U1.map(cj),U2.map(cj)],
 clear_axes:axes.map(r=>r.map(O)),theta_degrees:dims,
 current_center:{S6:"g=7=1+6 mod12",S9:"g=1 mod18",S3:"g=1 mod6"},
 absolute_anchors:["Theta(delta z) for both S6","sigma(3z) for S9","sigma(delta z) for S3"],
 T:TT.map(r=>r.map(cj)),complete_frame:F.map(r=>r.map(cj)),complete_inverse:Fi.map(r=>r.map(cj)),
 frame_Gram:F.map(r=>F.map(s=>dot(r,s))).map(r=>r.map(cj)),
 fixed_four_outputs:["J","Y","xi2","d0"],fixed_four_Gram_determinant:cj(det(Gpi)),complete_determinant:cj(det(F)),old_W_in_complete_frame:wc.map(cj),
 J_projector:pj.map(r=>r.map(cj)),Y_shift:cj(yshift),all_three_W_shift:cj(wshift),
 corrected_test:"sum binom6j E_K^(6-j)(eta K)^j/(216 b Omega^6 (1+lambda kappa^j))",
 exact_fifth_coefficients:coeff.map(cj),old_W_fifth_coefficients:cw.map(cj),W_minus_6delta_Y_fifth:diff.map(cj),norm_first_difference:qs(norm(diff[3])),difference_valuation:"exactly 5n+3 for the same corrected-test W-6delta Y integral",sum_fifth:cj(alpha),norm_alpha:qs(norm(alpha)),
 exact_fifth_formula:"(d/b)(1+lambda kappa) sum_j=3..6 q_j/(1+lambda kappa^j)",
 local_mass:"identically zero because xi2 and d0 are independent zero-mass sigma inputs absent from the test and domain",
 actual_pipe:"U1,U2,xi2,d0 deep n; K unit; J/kappa^r+K deep n",
 J_core_transport:"all positive r, scalar beta; entire K/E test unchanged",
 warning:"K/E orthogonal pushforward preserves the four T-fixed outputs, not the old W output; W transposes and compensating domains remain."
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
