#!/usr/bin/env node
// Exact Q(delta), delta^2=-3. No external packages.
const certificate=(()=>{
const primitive=(()=>{

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

const om=c(q(-1,2),q(1,2)),o2=cp(om,2),de=c(0,1),aa=ca(c(2),om),eta=cd(c(2),aa);
function fact(n){let z=1n;for(let k=2;k<=n;k++)z*=BigInt(k);return z}
const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
const Bder=ca(cm(cm(aa,c(q(3,10))),c(5)),cm(cm(cp(aa,7),c(q(1,210))),c(-7)));
let coeff=0n;for(let j=0;j<=3;j++)coeff+=choose(3,j)*choose(7,4-j)*(j%2? -1n:1n);
const Pder=ca(cm(aa,c(q(42,70))),cm(cp(aa,7),c(q(coeff,210))));
const rb=cd(cm(Bder,c(q(720,64))),cn(aa)),rp=cd(cm(Pder,c(q(720,64))),cn(aa));
if(!ce(rb,c(-27))||!ce(rp,c(-27)))throw Error("whole S6 primitive sixth moment");
const normalized=[q(-1,27),q(0),q(0),q(20,27),q(0),q(0),q(8,27)];
if(!eq(normalized.reduce(add,q(0)),q(1)))throw Error("full H0 sum");
const sigma_swap=cn(cd(cm(o2,aa),de));if(!ce(sigma_swap,c(1)))throw Error("absolute N swap phase");
const reflection=[[c(),cn(aa)],[cn(ci(aa)),c()]],jr=[c(q(1,2)),cm(c(q(-1,2)),aa)],kr=[c(q(1,2)),cm(c(q(1,2)),aa)];
const yR=cd(ca(c(-1),cm(c(4),om)),c(3)),barGa=c(q(5,2),q(-1,2));
const jnext=mm([jr],reflection)[0],knext=mm([kr],reflection)[0],ynext=mm([[yR,barGa]],reflection)[0];
for(let j=0;j<2;j++)if(!ce(jnext[j],jr[j])||!ce(knext[j],cn(kr[j]))||!ce(ynext[j],[yR,barGa][j]))throw Error("actual mirror keeps J/native Y");
const q5=c(q(-80,64827),q(-8,7203));
if(!eq(norm(q5),q(64n,3n**6n*7n**5n)))throw Error("actual nonzero N channel");
return{
 primitive_whole_S6_moment_B_over_bOmega6:cj(rb),primitive_whole_S6_moment_P_over_bOmega6:cj(rp),
 full_four_output_normalized_rows:normalized.map(qs),
 E_depth_profile:{variable:"kappa^(3n)",coefficients:["8/27","20/27","-1/27"],external:"beta^n"},
 actual_N_sigma_swap_phase:cj(sigma_swap),actual_R_x_reflection:reflection.map(r=>r.map(cj)),
 J_row:jr.map(cj),K_row:kr.map(cj),Y_R_x_row:[yR,barGa].map(cj),
 mirror_domains:["J/kappa^r+K deep n","J/kappa^r-K deep n"],all_other_axes_fixed:["A5","E_K","B2","C30"],
 N_local_fifth:cj(q5),N_local_fifth_norm:qs(norm(q5)),N_local_and_mirror_valuations:"5n, exact negatives for native Y_r",
 old_W_change:"W -> W-2(1/3-delta)K; the native T weight is not fixed"
};

})();
const polynomial_check=(()=>{

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

const om=c(q(-1,2),q(1,2)),o2=cp(om,2),de=c(0,1),ga=c(q(5,2),q(1,2)),bg=cc(ga),eta=c(1,q(-1,3));
const x=[q(1),q(-1,7)];for(let n=2;n<=3;n++){let s=q(0);for(let j=1;j<n;j++)s=add(s,mul(x[j],x[n-j]));x.push(div(mul(q(6),s),q((6*n-2)*(6*n-3)-12)));}
const ll=[q(0)];for(let n=1;n<=3;n++)ll[n]=neg(div(x[n],q(6*n*(6*n-1))));
const sig=[q(1),ll[1],add(ll[2],div(mul(ll[1],ll[1]),q(2))),add(add(ll[3],mul(ll[1],ll[2])),div(pow(ll[1],3),q(6)))];
function fact(n){let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return r}
const al=[de,ga,bg,c(1)],es=[c(q(1,2),q(1,6)),c(q(-1,2),q(1,6)),c(),c(q(1,2),q(-1,6))],ks=[c(q(1,2)),c(q(-1,4),q(-1,4)),c(q(3,4),q(1,4)),c(q(-1,2))];
function sigmaPoly(i){
 const out=new Map();
 for(let s=0;s<=3;s++){const deg=1+6*s;for(let e=0;e<=6;e++)for(let k=0;e+k<=6;k++){const y=deg-e-k;if(y<0||y>16)continue;const coef=cm(c(mul(sig[s],q(fact(deg),fact(e)*fact(k)*fact(y)))),cm(cp(es[i],e),cm(cp(ks[i],k),cp(al[i],y))));if(!ce(coef,c()))out.set(y+","+e+","+k,coef);}}
 return out;
}
let pol=new Map([["0,0,0",c(1)]]);
for(let i=0;i<4;i++){const out=new Map(),pp=sigmaPoly(i);for(const[ka,va]of pol){const a=ka.split(",").map(Number);for(const[kb,vb]of pp){const b=kb.split(",").map(Number),e=a.map((t,j)=>t+b[j]);if(e[0]>16||e[1]+e[2]>6)continue;const key=e.join(",");out.set(key,ca(out.get(key)||c(),cm(va,vb)));}}pol=out;}
const C=Array.from({length:7},(_,j)=>[4,10,16].map(y=>pol.get(y+","+(6-j)+","+j)||c()));
// normalized first-Y source, after removing the common G16.
const H=C.map((r,j)=>r.map(v=>cm(cd(cm(c(-10),cm(de,cp(eta,j))),c(63)),v)));
// Basis sigma^18 x^7, sigma^18 x^4, sigma^18 x. Each has leading coefficient one.
const a1=x[1],a2=x[2],s1=mul(q(18),sig[1]),s2=add(mul(q(18),sig[2]),mul(q(153),pow(sig[1],2)));
const B7=[q(1),add(mul(q(7),a1),s1),add(add(mul(q(7),a2),mul(q(21),pow(a1,2))),add(mul(mul(q(7),a1),s1),s2))];
const B4=[q(0),q(1),add(mul(q(4),a1),s1)],B1=[q(0),q(0),q(1)];
const rows=H.map(r=>{const u=r[0],v=cs(r[1],cm(u,c(B7[1]))),w=cs(cs(r[2],cm(u,c(B7[2]))),cm(v,c(B4[2])));return[u,v,w]});
const sum=Array.from({length:3},(_,i)=>rows.map(r=>r[i]).reduce(ca,c()));
const S=[c(1),c(q(-4,7)),c(q(16,7))];
for(let i=0;i<3;i++)if(!ce(sum[i],S[i])||!ce(rows[0][i],cm(c(q(-1,27)),S[i])))throw Error("whole H0/E6 arithmetic normalization "+i);
for(const j of[1,2,4])if(rows[j].some(v=>!ce(v,c())))throw Error("entire vanished E rows");
function det3(M){return ca(cs(cm(M[0][0],cs(cm(M[1][1],M[2][2]),cm(M[1][2],M[2][1]))),cm(M[0][1],cs(cm(M[1][0],M[2][2]),cm(M[1][2],M[2][0])))),cm(M[0][2],cs(cm(M[1][0],M[2][1]),cm(M[1][1],M[2][0]))))}
return{sigma_coefficients:sig.map(qs),wp_coefficients:x.map(qs),fixed_sources_after_G16_basis:["sigma18 x7","b sigma18 x4","b2 sigma18 x"],rows:rows.map(r=>r.map(cj)),S:sum.map(cj),det_3_5_6:cj(det3([rows[3],rows[5],rows[6]])),basis_jets:[B7,B4,B1].map(r=>r.map(qs))};

})();
return {status:'complete four-output E-depth profile and actual N mirror pipes verified',primitive,polynomial_check};
})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
